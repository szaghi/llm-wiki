---
type: Method
title: "Affine-invariant WENO weights"
description: "Wang & Don's Ai-WENO weights multiply the sensitivity parameter ε by the squared mean absolute deviation of the stencil data, which makes the nonlinear weights, hence the WENO operator, commute with every affine map f ↦ σf+μ; this restores the ENO property for small-amplitude offset data and gives intrinsic well-balancing for shallow water."
status: established
aliases: [Ai-WENO, Ai-WENO-Z, Ai-WENO-D, Ai-WENO-JS, affine-invariant WENO operator]
tags: [weno, reconstruction, well-balanced, finite-difference]
timestamp: 2026-10-22T16:24:00Z
---

# Affine-invariant WENO weights

Classical WENO weights depend on an absolute sensitivity parameter $\epsilon$, so they change when
the data are scaled or shifted. Wang & Don (2022) ask what happens when the reconstructed data are
an affine image $\mathcal Af=\sigma f+\mu$ of a function $f$ (page-local: $\sigma\ne0$ the scaling,
$\mu$ the translation, both constant over the global stencil). Their **Ai-WENO** weights make the
WENO operator $W$ satisfy the **Ai-property**

$$W[\sigma f+\mu,\epsilon]=\sigma\,W[f,\epsilon]+\mu\qquad\text{for every }\epsilon>0,$$

(Definitions 1–3, Eq. (3)), the affine case of [scale invariance](/properties/scale-invariance.md).

## Why invariance reduces to the weights

The candidate interpolants are linear and reproduce constants, so
$\hat f^{(k)}[\mathcal Af]=\mathcal A\hat f^{(k)}[f]$, and the weights sum to one. Hence

$$W[\mathcal Af,\epsilon]-\mathcal AW[f,\epsilon]=\sigma\sum_k\big(\omega_k[\mathcal Af,\epsilon]-\omega_k[f,\epsilon]\big)\,\hat f^{(k)}_{i+1/2}[f],$$

and invariance of the normalized weights implies the Ai-property (Eqs. (15)–(16)). The paper
states the converse too; only this direction is needed for its theorems.

## The weights

With exponents $q,q_{\mathrm o}>0$ (the paper's $p$ and $q$) and, for fifth order,
$\tau=|\beta_0-\beta_2|$ (Eqs. (9)–(14)):

$$\alpha_k=d_k\big(1+\Phi[f]\,Z_k[f,\epsilon]\big)^{q_{\mathrm o}},\qquad
Z_k=\Big(\frac{\tau[f]}{\beta_k[f]+\epsilon\,\mathsf m^2[f]}\Big)^q,$$

where (page-local symbols: $q_{\mathrm o}$, $Z_k$, $\Phi$, $\varphi$, $\mathsf m$, $\langle f\rangle$)

- the **modifier** is $\Phi=1$ (Z-type weights, [WENO-Z](/methods/weno-z.md)) or
  $\Phi=\min\{1,\varphi/\mathsf m\}$ with $\varphi=\sqrt{|\beta_0-2\beta_1+\beta_2|}$ (D-type,
  "sensitivity-parameter-free" weights of Wang, Wang & Don 2019);
- the **descaler** $\mathsf m[f]$ is $\mathsf m_0$ plus, over the $2r-1$ points of the global stencil,
  1 (classical, "Cl"), the mean of $|f_j|$ (scale-invariant, "Si", from Don, Li, Wang & Wang 2022), or
  the mean of $|f_j-\langle f\rangle|$ (affine-invariant, "Ai");
- the **averager** $\langle f\rangle$ is the stencil mean of $f_j$.

The Ai descaler is the mean absolute deviation of the stencil data, so the effective sensitivity
parameter $\epsilon\mathsf m^2$ is relative to the local spread of the data. Parameters: $q=2$,
$q_{\mathrm o}=1$ (with $\mathsf m=1$, $\Phi=1$, $q_{\mathrm o}=1$ the classical WENO-Z weights are recovered); floor
$\mathsf m_0=10^{-40}$ in double and $10^{-100}$ in quadruple precision. The naming hierarchy is
Ai $\xrightarrow{\langle f\rangle=0}$ Si $\xrightarrow{\mathsf m=1}$ Cl, combined with D
$\xrightarrow{\Phi=1}$ Z (§2.4).

**Theorem 1** (§2.3). With $\mathsf m_0=0$, the Ai-WENO operator satisfies the Ai-property. The proof
uses $\langle\mathcal Af\rangle=\mathcal A\langle f\rangle$, hence $\mathsf m[\mathcal Af]=|\sigma|\mathsf m[f]$
and $\varphi[\mathcal Af]=|\sigma|\varphi[f]$, and $\beta_k[\mathcal Af]=\sigma^2\beta_k[f]$,
$\tau[\mathcal Af]=\sigma^2\tau[f]$ (Eqs. (17)–(18)); $\Phi$ and $Z_k$ are therefore invariant.
**Theorem 2** (App. A) proves the same for Jiang–Shu weights
$\alpha_k=d_k/(\beta_k+\epsilon\mathsf m^2)^q$, which scale as $\sigma^{-2q}$
([WENO-JS](/methods/weno-js-reconstruction.md)).

**Remark 2** gives an equivalent implementation: subtract the stencil mean, apply the Si-WENO
operator, add the mean back. The extra cost of descaler and averager is "a few cache-friendly
flops", citing CPU timings of Don et al. 2022 (Remark 3).

## Consequences

- **ENO property for offset data.** With $\sigma=10^{-7}$, $\mu=1$ and $\epsilon=10^{-12}$, the Si
  descaler is $\approx|\mu|=1$, so $\beta_k=O(\sigma^2)=O(10^{-14})$ is swamped by
  $\epsilon\mathsf m^2\approx10^{-12}$, the weights become independent of $k$ and the scheme reverts
  to the linear fifth-order scheme: Si-WENO-Z then shows Gibbs oscillations in linear advection of
  a multi-wave profile ($N_x=200$, $t=2$), while Ai-WENO-Z is non-oscillatory with point-wise errors
  identical for $\mu=0$ and $\mu=1$ (§3.2.1, Figs. 4–5). In a two-blast-wave problem with background
  pressure $p_\infty=\mu=1$ and $\sigma=10^{-7}$, Cl-WENO-Z oscillates at strong and weak shocks,
  Si-WENO-Z reduces but does not remove the oscillations, Ai-WENO-Z is essentially non-oscillatory
  (Fig. 6). Wang & Don conclude that the [ENO property](/definitions/eno-property.md) of a
  non-affine-invariant WENO scheme can fail when $|\sigma|\ll|\mu|$.
- **Roundoff-level invariance.** In quadruple precision, $N_x=160$, $\epsilon=10^{-12}$, the
  normalized Ai-error (Eq. (21)) of Ai-WENO-Z/D is at machine precision for sine, ReLU and
  Heaviside data over $\sigma\in[10^{-19},10^{19}]$ and $\mu\in\{0,10^{-10},1,10^{10}\}$; Si-WENO
  is exact only for $\mu=0$, and Cl-WENO fails even for $\mu=0$ when $\sigma$ is small
  (§3.1, Figs. 1–3).
- **Well-balancing without linearization.** For shallow water written in $(H_{\mathrm s},hv)$, with depth
  $h$, bottom $b$, free-surface level $H_{\mathrm s}=h+b$ and gravity $g$ (page-local, as on the
  [well-balancing](/properties/well-balancing.md) page), the still-water flux component
  $\tfrac12gH_{\mathrm s}^2-gH_{\mathrm s}b$ is an affine image of $b$ with
  $(\sigma,\mu)=(-gH_{\mathrm s},\tfrac12gH_{\mathrm s}^2)$. The Ai-WENO derivative of the flux is then
  $-gH_{\mathrm s}$ times the WENO derivative of $b$, matching the source, also characteristic-wise because the
  projection is linear (§3.3). The characteristic-wise scheme of Li, Caleffi & Qi (2015) is thereby
  [well-balanced](/properties/well-balancing.md) without its "WENO linearization technique" (common
  weights for flux and source). In quadruple precision, $t=50$, $N_x\le1000$, $\epsilon=10^{-12}$,
  Ai-WENO-Z/D keep $\|H_{\mathrm s}-10\|_\infty$ at roundoff (about $10^{-33}$), while Cl/Si-WENO errors are
  $10^{-11}$–$10^{-23}$ on a smooth bottom and $\approx10^{-26}$ on a discontinuous one (Fig. 9). With
  $\epsilon=10^{-40}$ all operators are well-balanced except Cl- and Si-WENO-D on the smooth bottom,
  because the D-type modifier $\varphi/\mathsf m$ is not affine invariant there (Fig. 10).
- **Limits.** Ai-WENO is not positivity preserving: the Mach 2000 jet needs a positivity-preserving
  limiter, active only near the jet front and the inlet corners at the final time (§3.2.4, Fig. 8;
  [high-Mach jets](/benchmarks/high-mach-astrophysical-jet.md)). The linearization technique is still
  needed when $W$ acts on sums or products of two functions, as in two-$\gamma$ multicomponent
  equilibria (Introduction).

## Reuse of the descaler

Li, Li, Don & Wang (2023, §2.3, Eqs. (43)–(44)) carry the Si descaler over to the
[multi-resolution A-WENO](/methods/multi-resolution-weno.md) interpolation: with Z-type weights on
nested central stencils, $\alpha_k=d_k\big(1+\tau^*/(\beta_k+\epsilon\,\mathsf m^2)\big)$ and
$\mathsf m=\tfrac15\sum_{j=i-2}^{i+2}|f_j|+\mathsf m_0$, $\mathsf m_0=10^{-100}$, $\epsilon=10^{-6}$, citing
this paper and Don, Li, Wang & Wang for it. Their Theorem 4 proves scale invariance with $\mathsf m_0=0$,
since $\tau^*$, $\beta_k$ and $\mathsf m^2$ all scale by $\sigma^2$. They use the mean of $|f_j|$, not of
$|f_j-\langle f\rangle|$ *(compiler check, not in the sources: so the operator is scale- but not
affine-invariant, since $\mathsf m$ changes under $f\mapsto f+\mu$)*; it serves their
well-balanced scheme, where the characteristic variables at equilibrium are multiples of the
equilibrium pressure, a pure scaling ([scale invariance](/properties/scale-invariance.md),
[well-balancing](/properties/well-balancing.md)).

## Qualifications

- Theorem 1 holds with $\mathsf m_0=0$ in exact arithmetic; the implementation uses
  $\mathsf m_0=10^{-40}$ or $10^{-100}$, so invariance is approximate for
  $|\sigma|\,\mathsf m[f]\lesssim\mathsf m_0$.
- No convergence-order or critical-point test is presented. Replacing $\epsilon$ by $\epsilon\mathsf m^2$
  makes the effective $\epsilon$ small for smooth data of small local variation, which bears on
  [critical-point accuracy](/properties/critical-point-accuracy.md); the paper does not revisit it.
- "Well-balanced for any sensitivity parameter" is shown for $\epsilon\in\{10^{-12},10^{-40}\}$;
  well-balancing for the Euler equations under gravity is stated but not tested.
- The sign of the translation constant is printed inconsistently in §3.3: $\mu=\tfrac12gH_{\mathrm s}^2$
  on p. 643 (correct from the flux) and $-\tfrac12gH_{\mathrm s}^2$ on p. 644.
- §3.2.1 says the collapsed weights give "the central upwind scheme"; this is the linear
  upwind-biased fifth-order scheme, not a [central-upwind](/methods/central-upwind-scheme.md) scheme.

# Citations

- [Wang & Don (2022)](/sources/wang-2022-b.md) — §1, Defs. 1–4; §2, Eqs. (4)–(18), Theorem 1, Remarks 1–3; §3, Eqs. (19)–(30), Figs. 1–10; App. A, Theorem 2.
- [Li, Li, Don & Wang (2023)](/sources/li-2023.md) — §1; §2.3, Eqs. (42)–(45), Theorem 4; §4.2, Theorem 5.

---
type: Property
title: "Scale and affine invariance"
description: "A reconstruction or limiter is scale-invariant when it commutes with multiplication of the data by a constant, and affine-invariant when it also commutes with adding a constant; classical WENO weights have neither property because ε is absolute, and the sources reach it by normalised variables, relative ε, or globally normalised damping."
status: established
aliases: [scale-invariant, affine-invariant, Ai-property, Si-property, homogeneity of a reconstruction, normalisable scheme]
tags: [reconstruction, weno, limiting, dg]
timestamp: 2026-10-21T12:00:00Z
---

# Scale and affine invariance

Let $R$ be a reconstruction operator that maps stencil data to an interface value (or a limiter
that maps a solution to a limited one). With page-local constants $\sigma\ne0$ and $\mu$:

- $R$ is **scale-invariant** if $R[\sigma f]=\sigma R[f]$ (Deng 2023, Definition 7; the "Si-property"
  of Wang & Don 2022, Definition 4);
- $R$ is **affine-invariant** if $R[\sigma f+\mu]=\sigma R[f]+\mu$ (the "Ai-property" of Wang & Don
  2022, Definition 2, Eq. (3)).

Wang & Don (2022, §1) motivate the affine case with data that are affine images of other fields:
the momentum flux $\rho v^2+p$ is affine in $v^2$ where $\rho$ and $p$ are locally constant, and the
shallow-water still-water flux is affine in the bottom elevation. Peng, Sun & Wu (2024, §1.2) add a
dimensional argument: a damping coefficient that enters an exponential must be dimensionless.
Consistent linear reconstructions reproduce constants and are therefore affine invariant (Deng 2023,
§3.1, states that every consistent linear operator is normalisable); the property is lost through the
nonlinear parts (weights, indicators, damping coefficients) when these contain dimensional constants.

## Terminology across the sources

The three sources that use the word differ. Wang & Don (2022) separate scale invariance ($\mu=0$)
from affine invariance. Deng (2023) defines scale invariance as homogeneity only. Peng, Sun & Wu
(2024, Theorem 2.6) call "scale-invariant" what Wang & Don call affine invariant:
$\mathcal S(\sigma u_h+\mu)=\sigma\mathcal S(u_h)+\mu$ for their oscillation-eliminating step
$\mathcal S$ (page-local name). This page uses Wang & Don's split.

## How classical weights fail

In Jiang–Shu and WENO-Z weights the [smoothness indicators](/definitions/smoothness-indicator.md)
scale as $\beta_k[\sigma f+\mu]=\sigma^2\beta_k[f]$ while $\epsilon$ does not, so the weights
depend on $\sigma$ (Wang & Don 2022, Eq. (18)).

- Deng (2023, App. A.2, Fig. 13) measures the scale-invariance error
  $\max_x|R[\sigma\bar u]/\sigma-R[\sigma_0\bar u]/\sigma_0|$ with $\sigma_0=10^{20}$ on $N_x=320$
  cells: WENO-JS3 with $\epsilon=10^{-6}$ depends clearly on $\sigma$; with $\epsilon=10^{-40}$ the
  error grows for $\sigma<10^{-10}$; WENO-Z3 and WENO-P3 with $\epsilon=10^{-40}$ show errors too. Deng
  also recalls Don et al. (2022): WENO-Z with $\epsilon=10^{-12}$ and WENO-JS with $\epsilon=10^{-6}$
  oscillate on Sod's problem scaled by $10^{-7}$.
- Wang & Don (2022, §3.2) show that a scale-invariant but not affine-invariant scheme still fails:
  for data $10^{-7}f+1$, the Si descaler is dominated by the offset, $\epsilon$ swamps the
  $\beta_k$, and the weights collapse to the linear weights, destroying the
  [ENO property](/definitions/eno-property.md).
- Li et al. (2022, §4.1) object to the WENO-Z variant with $\epsilon=\Delta x^m$ of Don & Borges
  that $\beta_k$ and $\Delta x$ have different dimensions, so the solution depends on the reference
  values used to nondimensionalize the problem.

## Routes to invariance

**Relative sensitivity parameter.** Replace $\epsilon$ by $\epsilon\,\mathsf m^2[f]$ with
$\mathsf m$ the mean absolute value of the stencil data (Si-WENO, Don et al. 2022, as recalled) or
its mean absolute deviation (Ai-WENO); Wang & Don (2022, Theorems 1–2) prove the Ai-property for
Z-, D- and JS-type weights ([affine-invariant WENO](/methods/affine-invariant-weno.md)). The same
paper shows the practical payoff: shallow-water still water preserved to roundoff without the
"WENO linearization technique" ([well-balancing](/properties/well-balancing.md)).

**Normalised variables.** In a compact three-cell stencil, a reconstruction that depends on the
data only through the normalized cell average $\tilde u_i=(\bar u_i-\bar u_{i-1})/(\bar u_{i+1}-\bar u_{i-1})$
is called *normalisable*, $\tilde u_{i+1/2}=\hat R(\tilde u_i)$, and Deng (2023, Proposition 2) proves
it scale-invariant:
$u^-_{i+1/2}=(\bar u_{i+1}-\bar u_{i-1})\hat R(\tilde u_i)+\bar u_{i-1}$. *(Compiler check, not
in the sources: $\tilde u_i$ is unchanged by $\bar u\mapsto\sigma\bar u+\mu$, so the same formula
gives affine invariance as well.)* Consistent linear schemes are normalisable; WENO3-JS, WENO-Z3 and
WENO-P3 are not (§4.3). Proposition 6: a WENO3 operator whose weight depends only on $\tilde u_i$ is
normalisable, hence scale-invariant. Deng's NewWENO (Eq. (6.6)),
$\omega_0=\tfrac13+\tfrac23\big(1+\gamma_0\tilde u_i^{2}\big)^{-2}-\tfrac13\big(1+\gamma_0(1-\tilde u_i)^2\big)^{-2}$
with page-local $\gamma_0=25$ (the paper's $\gamma$, $m=1$, $n=2$), has a scale-invariance error near
machine precision for scaling factors in $[10^{-19},10^{19}]$ (Fig. 13). The
[ROUND schemes](/methods/round-scheme.md) are designed directly as functions $\hat R(\tilde u_i)$ on
the [normalised-variable diagram](/definitions/normalised-variable-diagram.md) and are scale-invariant
by construction (Deng 2023, §7; Huang et al. 2026, §2.2). Huang et al. (2026, §3.4) sample the
learned WENO3-NN on this diagram by *assuming* it is scale-independent; its input layer normalizes
differences by $\max(|\bar u_i-\bar u_{i-1}|,|\bar u_{i+1}-\bar u_i|,\epsilon)$, which the paper calls
"Galilean invariance" ([learned WENO weights](/methods/learned-weno-weights.md)).

**Globally normalized damping in DG.** Peng, Sun & Wu (2024, Eq. (2.6)) normalize the damping
coefficient of the [OEDG](/methods/oedg.md) step by $\|u_h-\mathrm{avg}(u_h)\|_{L^\infty(\Omega)}$ and
multiply it by a local wave-speed estimate. The coefficient is then invariant under
$u_h\mapsto\sigma u_h+\mu$, which gives affine invariance of the step (Theorem 2.6) and *evolution
invariance*: for $u_t+\lambda f(u)_x=0$ (page-local constant $\lambda$) at fixed CFL number the results after $n$ steps do not depend
on $\lambda>0$ (Theorem 2.10). The damping of the earlier oscillation-free DG scales as $|\sigma|$ and
carries no wave speed; it smears the Lax and Shu–Osher problems scaled by 100 and oscillates when
they are scaled by 0.01, while OEDG gives identical results for factors 1, 0.01 and 100 (Remark 2.8;
Ex. 5.6, 5.8). A locally normalized coefficient (Eq. (2.14)) is proposed, but no mesh-independent
constant for it has been found (Remark 2.9). Peng et al. also note that a characteristic
decomposition can destroy invariance, because eigenvectors are defined up to an arbitrary scaling
(Remark 2.12, Ex. 5.7; [characteristic decomposition](/methods/characteristic-decomposition.md)).

## Qualifications

- **Invariance and accuracy can conflict.** *(Compiler check, not in the sources.)* In smooth
  regions $\tilde u_i=\tfrac12+O(\Delta x)$ (Deng 2023, Lemma 1), and a weight that depends on
  $\tilde u_i$ alone tends to its value at $\tfrac12$, not to the linear weight. For NewWENO,
  $\omega_0(\tfrac12)=857/2523\approx0.3397$ against $d_0=\tfrac13$, an $O(1)$ defect, so the
  operator is second-order with an error constant close to the third-order scheme rather than
  uniformly third order. Deng states the accuracy condition $\omega_k-d_k=O(\Delta x^2)$ (§4.3) but
  reports only error-versus-$N$ plots, no observed orders.
- In OEDG the global $L^\infty$ normalization couples the damping strength to the global solution
  range; multi-scale data in one domain are not tested.
- The Ai-WENO theorems assume a zero floor in the descaler; the floors used in practice make
  invariance approximate for very small $|\sigma|$.

# Citations

- [Wang & Don (2022)](/sources/wang-2022-b.md) — §1, Defs. 1–4; §2.2–2.4, Eqs. (9)–(18), Theorem 1; §3.1–3.3; App. A.
- [Deng (2023)](/sources/deng-2023.md) — §1; §2.2–2.3, Lemma 1, Def. 7, Prop. 2; §4.3; §6.2, Prop. 6, Eq. (6.6); App. A.2, Fig. 13.
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — §1; §2, Eqs. (2.6), (2.13)–(2.14), Theorems 2.6, 2.10, Remarks 2.8–2.12; Ex. 5.6–5.8.
- [Huang et al. (2026)](/sources/huang-2026.md) — §2.2; §3.2, Eq. (3.10); §3.4.
- [Li et al. (2022)](/sources/li-2022-b.md) — §4.1.

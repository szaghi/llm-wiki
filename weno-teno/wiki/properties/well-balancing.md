---
type: Property
title: "Well-balancing"
description: "A scheme for a balance law is well-balanced if it preserves a steady state such as the lake at rest exactly; in this bundle it follows from affine-invariant WENO weights without the WENO linearization technique (shallow water) and from stationary-contact-preserving fluctuations (layered and debris-flow models)."
status: established
aliases: [well-balanced scheme, C-property, lake-at-rest property, exact preservation of still water]
tags: [well-balanced, weno, finite-difference, riemann-solver]
timestamp: 2026-10-21T00:00:00Z
---

# Well-balancing

For a balance law $\partial_tu+\partial_xf(u)=S(u)$, a discretization is **well-balanced** for
a given steady state if discrete data equal to that steady state stay unchanged up to
round-off, i.e. the discrete flux divergence and the discrete source cancel exactly. For the
shallow-water equations the steady state of interest is still water, "lake at rest";
[Wang & Don (2022)](/sources/wang-2022-b.md) (§2–§3.3) use "WB-property" and "C-property"
for its exact preservation. Below, $h$ is the water depth, $b$ the bottom, $H_{\mathrm s}=h+b$
the free-surface level and $g$ gravity (page-local; $h$ is not a numerical flux here).

## Shallow water: WB from affine invariance

Following Li, Caleffi & Qi (2015) as recalled by Wang & Don (§3.3, Eqs. (26)–(28)), the
equations are written in $(H_{\mathrm s},hv)$,

$$\partial_t\begin{pmatrix}H_{\mathrm s}\\ hv\end{pmatrix}+\partial_x\begin{pmatrix}hv\\ \dfrac{(hv)^2}{H_{\mathrm s}-b}+\tfrac12gH_{\mathrm s}^2-gH_{\mathrm s}b\end{pmatrix}=\begin{pmatrix}0\\ -gH_{\mathrm s}\,\partial_xb\end{pmatrix},$$

with still water $v=0$, $H_{\mathrm s}=$ const. The scheme is characteristic-wise
finite-difference WENO with global [Lax–Friedrichs splitting](/methods/lax-friedrichs-flux.md)
and Roe-averaged eigenvectors. Well-balancing requires that the discrete derivative of
$\tfrac12gH_{\mathrm s}^2-gH_{\mathrm s}b$ equal the discrete $-gH_{\mathrm s}\partial_xb$ at all
times. With classical WENO weights this needs the "WENO linearization technique" — using the
same nonlinear weights for flux and source (App. B of Li et al., as recalled).

Wang & Don observe that at still water this flux component is an **affine** function of $b$,
with scaling $-gH_{\mathrm s}$ and translation $\tfrac12gH_{\mathrm s}^2$. An
[affine-invariant WENO](/methods/affine-invariant-weno.md) operator commutes with affine maps
(their Thm. 1), so its derivative of the flux equals $-gH_{\mathrm s}$ times its derivative of
$b$, matching the source discretization; and because the characteristic projection is linear,
the property survives [characteristic decomposition](/methods/characteristic-decomposition.md)
(§3.3). Well-balancing is therefore intrinsic, without linearization (contribution).

**Evidence** (§3.3, Figs. 9–10): $x\in[0,10]$, smooth bottom $b_1=5e^{-\frac25(x-5)^2}$ and
discontinuous bottom $b_2=4$ on $[4,8]$, $H_{\mathrm s}=10$, $v=0$, $g=9.812$, $t=50$, up to
1000 points, quadruple precision, no linearization. With $\epsilon=10^{-12}$ the
affine-invariant Z- and D-type schemes keep $\lVert H_{\mathrm s}-10\rVert_\infty$ at round-off
(about $10^{-33}$), while classical and scale-invariant WENO errors fall from about
$10^{-11}$ to $10^{-23}$ with refinement on $b_1$ and stay near $10^{-26}$ on $b_2$. With
$\epsilon=10^{-40}$ all operators are well-balanced except the classical and scale-invariant
D-type ones on $b_1$, whose modifier is not affine invariant. See
[scale and affine invariance](/properties/scale-invariance.md).

## Layered and debris-flow models: WB from stationary contacts

[Balsara et al. (2024)](/sources/balsara-2024.md) link the lake-at-rest property to the
exact preservation of isolated stationary contact discontinuities (§III;
[stationary contact preservation](/properties/stationary-contact-preservation.md)). Their
[fluctuation-form FD-WENO](/methods/fluctuation-form-fd-weno.md), with the HLLI anti-diffusion
and the bottom carried as a variable with non-conservative products, reproduces perturbed
lake-at-rest tests "without any special modifications for the well-balancing":

- Pitman–Le debris flow: bump $b=0.25(\cos(10\pi(x-\tfrac12))+1)$ for $\lvert x-0.5\rvert\le0.1$,
  equilibrium with constant solid fraction and constant surface, perturbation $10^{-3}$ on
  $[-0.6,-0.5]$, 400 zones on $[-1.2,1.2]$, $t=1.25$ (§VIII.a, Fig. 4);
- two-layer shallow water: bump on $[1.4,1.6]$, interface at $0.65$, surface perturbation
  $0.2$ or $10^{-3}$ on $[1.1,1.2]$, 400 zones on $[0,2]$, $t=0.2$ (§VIII.c, Fig. 9).

## Qualifications

- Wang & Don's "well-balanced for any $\epsilon$" rests on two values of $\epsilon$; it follows
  from their Thm. 1 in exact arithmetic. The claim that characteristic-wise WB WENO is also
  well-balanced for the Euler equations under gravity without linearization is stated but not
  tested in their paper (Abstract, §3.3). The linearization is still required when the WENO
  operator acts on sums or products of functions, e.g. two-$\gamma$ multicomponent
  equilibria (Introduction).
- Balsara et al. write "We don't consider well-balancing in this paper" (§III) and later
  call the method well-balanced (§VIII.c); their evidence is visual agreement with the
  reference results of Dumbser & Balsara (2016), not a round-off equilibrium measurement.

# Citations

- [Wang & Don (2022)](/sources/wang-2022-b.md) — Introduction, §2.3 (Thm. 1), §3.3 (Eqs. (26)–(30), Figs. 9–10).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §III, §VIII.a (Fig. 4), §VIII.c (Fig. 9) (accepted manuscript).

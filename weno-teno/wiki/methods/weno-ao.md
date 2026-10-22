---
type: Method
title: "WENO-AO and multi-resolution WENO"
description: "WENO-AO nonlinearly hybridizes one large central high-order stencil with the three small stencils of third-order WENO, and multi-resolution WENO uses nested central stencils down to a low-order base; Balsara et al. show that both need fixes to reach orders 7 and 9 and their third-order version, and use them in fluctuation-form FD-WENO."
status: established
aliases: [WENO-AO, adaptive-order WENO, WENO-AO-(5,3), WENO-AO-(7,3), WENO-AO-(9,3), multi-resolution WENO, multiresolution WENO]
tags: [weno, cweno, reconstruction, finite-difference]
timestamp: 2026-10-21T00:00:00Z
---

# WENO-AO and multi-resolution WENO

**WENO-AO** ("adaptive order", Balsara, Garain & Shu 2016, as recalled by Balsara et al. 2024, §I) is
a [CWENO](/methods/cweno.md)-type reconstruction that "non-linearly hybridiz[es] large high order
central stencils with an $r=3$ WENO central scheme for stability". WENO-AO-$(\mathcal R,3)$ (page-local
$\mathcal R=5,7,9$) combines one large central stencil of order $\mathcal R$ with the three three-point
stencils; where the large stencil is judged smooth the high order is used, otherwise the reconstruction
falls back on third order. Balsara et al. (2024, §I) claim for it, against WENO-ZQ, that it preserves
local extrema, and recall its extension to unstructured meshes and its use as a DG limiter.

**Multi-resolution WENO** (Zhu & Shu 2018, as recalled by Balsara et al. 2024, §I, App. D) uses a
hierarchy of nested central stencils whose order decreases, down to a first-order base polynomial,
when smoothness is lost.

## WENO-AO weights and the high-order fix

Balsara et al. (2024, App. D, Eqs. (D.1)–(D.2)) rewrite the AO(5,3) weights of the original paper. Let
$\beta_{\mathrm H}$ be the indicator of the large stencil, $\beta_k$, $k=0,1,2$, those of the small
ones, $d_{\mathrm H}$ and $d_k$ the linear weights (page-local subscript $\mathrm H$), and

$$\tau=\tfrac13\big(|\beta_{\mathrm H}-\beta_0|+|\beta_{\mathrm H}-\beta_1|+|\beta_{\mathrm H}-\beta_2|\big).$$

The unnormalized weights are
$\alpha_{\mathrm H}=d_{\mathrm H}\big(1+\tau^2/(\beta_{\mathrm H}+\epsilon)^2\big)$ and
$\alpha_k=d_k\big(1+\tau^2/(\beta_k+\epsilon)^2\big)$, so that the nonlinear weights differ from the
linear ones by $O(\Delta x^5)$ in smooth flow. This is a [WENO-Z](/methods/weno-z.md)-type global
indicator built against the large stencil.

The formulas "cannot be extended as-is to seventh and ninth orders": Balsara et al. raise the power of
$\tau$ with the order (Eqs. (D.3)–(D.6)),

$$\alpha=d\Big(1+\frac{\tau^3}{(\beta+\epsilon)^2}\Big)\ \text{for AO}(7,3),\qquad
\alpha=d\Big(1+\frac{\tau^4}{(\beta+\epsilon)^2}\Big)\ \text{for AO}(9,3),$$

applied to the large and the small stencils alike, giving weight deviations $O(\Delta x^7)$ and
$O(\Delta x^9)$: "The power to which $\tau$ is raised increases with the order of accuracy. That is
the essential change". The smoothness indicators are closed-form sums of perfect squares (Balsara et
al. 2024, §I; [smoothness indicators](/definitions/smoothness-indicator.md)).

## Multi-resolution fix at third order

Balsara et al. (2024, §VII.a, App. D) found that the published third-order multi-resolution WENO "got
less than second order accuracy" on somewhat large meshes, because it jumps from third to first
order. Their fix replaces the first-order base polynomial by a limited linear one,
$\bar u_i+\mathrm{MC}_\theta(\bar u_{i+1}-\bar u_i,\bar u_i-\bar u_{i-1})$ or the van Albada form (Eqs.
(D.7)–(D.10)), with

$$\mathrm{MC}_\theta(a,b)=\tfrac12\big(\mathrm{sgn}\,a+\mathrm{sgn}\,b\big)\min\big(\tfrac12|a+b|,\theta|a|,\theta|b|\big),\ 1\le\theta\le2,\qquad
\mathrm{vA}_\epsilon(a,b)=\frac{(b^2+\epsilon)a+(a^2+\epsilon)b}{a^2+b^2+2\epsilon},$$

($\theta$ here is the MC parameter, page-local, not the Zhang–Shu factor of the registry); the van
Albada form is suggested for implicit problems because it is continuous in the slopes
([TVD limiters](/definitions/total-variation-diminishing.md)).

## Accuracy in fluctuation-form FD-WENO

Balsara et al. (2024) use both reconstructions in their
[fluctuation-form FD-WENO](/methods/fluctuation-form-fd-weno.md), reconstructing point values in the
characteristic variables of each zone (§VI). On the 2-D Euler
[isentropic vortex](/benchmarks/isentropic-vortex.md) with the LLF solver (§VII.a, Table I), the
$L_1$ density rates at the finest meshes are 2.59 (AO-3), 4.97 (AO(5,3)), 6.93 (AO(7,3)) and 8.78
(AO(9,3), $1.01355\times10^{-10}$ at $384^2$), and 2.74, 4.68, 6.93, 8.78 for multi-resolution WENO of
orders 3, 5, 7, 9. Design orders are also reached for a Baer–Nunziato smooth test (AO(7,3) 7.01–7.02,
AO(9,3) 9.03 then 8.76; Table II), a Baer–Nunziato vortex, and debris-flow and two-layer shallow-water
vortices (Tables III–V).

## Qualifications

- **Text–appendix mismatch.** §VII.a says that for WENO-AO "we had to change the '$\epsilon$' term ...
  so that it scales with the order of accuracy"; App. D changes the power of $\tau$ and leaves
  $\epsilon$ unchanged.
- §VII.b announces in Table III results with and without the nonlinear limiter, but the table shows
  WENO-AO against multi-resolution WENO; it also contains an unexplained rate of 12.06 for ninth-order
  multi-resolution WENO.
- The normalization of the AO weights is not restated in App. D.
- The claim against multi-resolution WENO is made by an author group that includes a co-author of the
  original scheme (Shu); it is a correction from within, not an independent test.

# Citations

- [Balsara et al. (2024)](/sources/balsara-2024.md) — §I; §VI; §VII.a–d, Tables I–V; App. D, Eqs. (D.1)–(D.10).

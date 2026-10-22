---
type: Method
title: "WENO-AO (adaptive-order WENO)"
description: "WENO-AO nonlinearly hybridizes one large central high-order stencil with the three small stencils of third-order WENO; Balsara et al. show that its weights need a higher power of the global indicator to reach orders 7 and 9, and Wang et al. measure the cost of its four sub-stencils; multi-resolution WENO has its own page."
status: established
aliases: [WENO-AO, adaptive-order WENO, WENO-AO-(5,3), WENO-AO-(7,3), WENO-AO-(9,3), WENOAO5]
tags: [weno, cweno, reconstruction, finite-difference]
timestamp: 2026-10-22T12:00:00Z
---

# WENO-AO (adaptive-order WENO)

**WENO-AO** ("adaptive order", Balsara, Garain & Shu 2016, as recalled by Balsara et al. 2024, §I) is
a [CWENO](/methods/cweno.md)-type reconstruction that "non-linearly hybridiz[es] large high order
central stencils with an $r=3$ WENO central scheme for stability". WENO-AO-$(\mathcal R,3)$ (page-local
$\mathcal R=5,7,9$) combines one large central stencil of order $\mathcal R$ with the three three-point
stencils, four candidates in all; where the large stencil is judged smooth the high order is used,
otherwise the reconstruction falls back on third order. Balsara et al. (2024, §I) claim for it, against
WENO-ZQ, that it preserves local extrema, and recall its extension to unstructured meshes and its use
as a DG limiter.

Its nested-stencil relative, **multi-resolution WENO** (Zhu & Shu), which falls back level by level
down to a one-point base, is recorded on [multi-resolution WENO](/methods/multi-resolution-weno.md),
together with the third-order fix of Balsara et al. (2024, App. D) and the fifth-order variant of
Wang et al. (2021).

## WENO-AO weights and the high-order fix

Balsara et al. (2024, App. D, Eqs. (D.1)–(D.2)) rewrite the AO(5,3) weights of the original paper. Let
$\beta_{\mathrm H}$ be the indicator of the large stencil, $\beta_k$, $k=0,1,2$, those of the small
ones, $d_{\mathrm H}$ and $d_k$ the linear weights (page-local subscript $\mathrm H$), and

$$\tau=\tfrac13\big(|\beta_{\mathrm H}-\beta_0|+|\beta_{\mathrm H}-\beta_1|+|\beta_{\mathrm H}-\beta_2|\big).$$

The unnormalized weights are
$\alpha_{\mathrm H}=d_{\mathrm H}\big(1+\tau^2/(\beta_{\mathrm H}+\epsilon)^2\big)$ and
$\alpha_k=d_k\big(1+\tau^2/(\beta_k+\epsilon)^2\big)$, so that the nonlinear weights differ from the
linear ones by $O(\Delta x^5)$ in smooth flow. This is a [WENO-Z](/methods/weno-z.md)-type global
indicator built against the large stencil, the same construction that multi-resolution WENO uses
against its largest stencil.

The formulas "cannot be extended as-is to seventh and ninth orders": Balsara et al. raise the power of
$\tau$ with the order (Eqs. (D.3)–(D.6)),

$$\alpha=d\Big(1+\frac{\tau^3}{(\beta+\epsilon)^2}\Big)\ \text{for AO}(7,3),\qquad
\alpha=d\Big(1+\frac{\tau^4}{(\beta+\epsilon)^2}\Big)\ \text{for AO}(9,3),$$

applied to the large and the small stencils alike, giving weight deviations $O(\Delta x^7)$ and
$O(\Delta x^9)$: "The power to which $\tau$ is raised increases with the order of accuracy. That is
the essential change". The smoothness indicators are closed-form sums of perfect squares (Balsara et
al. 2024, §I; [smoothness indicators](/definitions/smoothness-indicator.md)).

**Linear weights.** As comparator WENOAO5, Wang et al. (2021, §5) use
$d_{\mathrm H}=\gamma_{\mathrm{Hi}}$ for the large stencil and
$(1-\gamma_{\mathrm{Hi}})(1-\gamma_{\mathrm{Lo}})/2$, $(1-\gamma_{\mathrm{Hi}})\gamma_{\mathrm{Lo}}$,
$(1-\gamma_{\mathrm{Hi}})(1-\gamma_{\mathrm{Lo}})/2$ for the three small stencils, with
$\gamma_{\mathrm{Hi}}=\gamma_{\mathrm{Lo}}=0.85$ "the same as in" the original paper (page-local
parameters; the paper does not say which small stencil takes which weight)

## Accuracy in fluctuation-form FD-WENO

Balsara et al. (2024) use WENO-AO in their
[fluctuation-form FD-WENO](/methods/fluctuation-form-fd-weno.md), reconstructing point values in the
characteristic variables of each zone (§VI). On the 2-D Euler
[isentropic vortex](/benchmarks/isentropic-vortex.md) with the LLF solver (§VII.a, Table I), the
$L_1$ density rates at the finest meshes are 2.59 (AO-3), 4.97 (AO(5,3)), 6.93 (AO(7,3)) and 8.78
(AO(9,3), $1.01355\times10^{-10}$ at $384^2$). Design orders are also reached for a Baer–Nunziato
smooth test (AO(7,3) 7.01–7.02, AO(9,3) 9.03 then 8.76; Table II), a Baer–Nunziato vortex, and
debris-flow and two-layer shallow-water vortices (Tables III–V).

## Cost and resolution against three-stencil schemes

Wang et al. (2021, §5.1, p. 7) state that WENO-AO(5,3) costs more than the three-stencil fifth-order
schemes because it uses four sub-stencils. Over their 2-D and 3-D shock tests its cost relative to
WENO-JS5 is 1.29–1.80 (Table 5.8), against 1.09–1.60 for their multi-resolution scheme
([multi-resolution WENO](/methods/multi-resolution-weno.md)). In the same paper WENOAO5 gives the best
Shu–Osher solution at 200 points and the best Sedov peak, and is similar to the multi-resolution
scheme on the Woodward–Colella blast wave, but captures less roll-up on the 2-D Riemann problem and
the Rayleigh–Taylor instability (Examples 5.4–5.6, 5.9;
[Shu–Osher problem](/benchmarks/shu-osher-problem.md),
[Sedov blast wave](/benchmarks/sedov-blast-wave.md),
[Woodward–Colella blast wave](/benchmarks/woodward-colella-blast-wave.md)).

## Qualifications

- **Text–appendix mismatch.** Balsara et al. (2024, §VII.a) say that for WENO-AO "we had to change the
  '$\epsilon$' term ... so that it scales with the order of accuracy"; App. D changes the power of
  $\tau$ and leaves $\epsilon$ unchanged.
- Balsara et al. (2024, §VII.b) announce in Table III results with and without the nonlinear limiter,
  but the table shows WENO-AO against multi-resolution WENO.
- The normalization of the AO weights is not restated in App. D.
- Wang et al. (2021, §5.4) quote the WENOAO5 extra cost as "25%–80%"; their Table 5.8 starts at 1.29.

# Citations

- [Balsara et al. (2024)](/sources/balsara-2024.md) — §I; §VI; §VII.a–d, Tables I–V; App. D, Eqs. (D.1)–(D.6).
- [Wang et al. (2021)](/sources/wang-2021.md) — §5 (WENOAO5 linear weights); §5.1; Examples 5.4–5.9; §5.4, Table 5.8.

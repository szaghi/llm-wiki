---
type: Method
title: "WENO-AO (adaptive-order WENO)"
description: "WENO-AO nonlinearly hybridizes one large central high-order stencil with the three small stencils of third-order WENO; the sources raise the power of its global indicator for orders 7 and 9, measure the cost of its four sub-stencils, use it in compact gas-kinetic schemes and expose its loss of robustness when all stencils are non-smooth."
status: established
aliases: [WENO-AO, combination of ENO and WENO, adaptive-order WENO, WENO-AO-(5,3), WENO-AO-(7,3), WENO-AO-(9,3), WENOAO5]
tags: [weno, cweno, reconstruction, finite-difference]
timestamp: 2026-10-24T06:00:00Z
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
ones, $d_{\mathrm H}$ and $d_k$ the linear weights (page-local subscript $\mathrm H$; the global indicator $\tau$ below carries no point-count subscript), and

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
parameters; the paper does not say which small stencil takes which weight).
Zhang, Ji & Xu (2024d, §3.1, Eq. (35); arXiv v1) print the assignment: with
$d_{\mathrm H}=\gamma_{\mathrm{Hi}}=0.85$ and $\gamma_{\mathrm{Lo}}=0.85$, the two outer stencils take
$(1-\gamma_{\mathrm{Hi}})(1-\gamma_{\mathrm{Lo}})/2=0.01125$ and the central one
$(1-\gamma_{\mathrm{Hi}})\gamma_{\mathrm{Lo}}=0.1275$, within a recommended range $[0.85,0.95]$ for both
parameters. Their weights are the AO(5,3) ones above, with
$\tau=\tfrac13\sum_k\lvert\beta_{\mathrm H}-\beta_k\rvert$ and the squared ratio (Eqs. (36)–(39)), and they
print all four candidate polynomials in monomial form about the interface. *(Compiler check, not in
the sources: $2\times0.01125+0.1275+0.85=1$.)*

## Compact gas-kinetic variant

Zhao, Ji, Shyy & Xu (2023, §3.4, Eqs. (28)–(30); arXiv v1 read) reconstruct with the same structure,
which they call "a combination of ENO and WENO methodology", in compact gas-kinetic schemes that evolve
cell averages and cell-averaged gradients ([gas-kinetic schemes](/methods/gas-kinetic-scheme.md)). With
the large-stencil polynomial $P$ and $n$ small-stencil polynomials $q_k$ and the reconstruction $p^{\mathrm{AO}}$ (page-local),

$$p^{\mathrm{AO}}(x)=\sum_{k=1}^n\omega_kq_k(x)+\omega_0\Big(\frac{1+C}{C}P(x)-\sum_{k=1}^n\frac{C_k}{C}q_k(x)\Big),\qquad
d_0=\frac{C}{1+C},\quad d_k=\frac{C_k}{1+C},$$

$\sum_kC_k=1$, with $C=5$ and $C_k=1/n$ (page-local constants), and WENO-Z weights
$\alpha_k=d_k\big(1+(\tau_{\mathrm Z}/(\beta_k+\epsilon))^2\big)$, $\epsilon=10^{-5}$, where $\tau_{\mathrm Z}$
(page-local) is built from the small-stencil indicators ([smoothness indicators](/definitions/smoothness-indicator.md)).
To save cost the large-stencil indicator is replaced by $\max_k\beta_k$. Two stencil sets are used:

- **1-D, eighth order.** The large stencil holds four cell averages and four averaged slopes
  (a degree-7 polynomial); the small ones are three quadratics, including one from two averages and a
  slope, and two cubics with one slope each.
- **Triangles, fourth order.** A cubic from the cell, its neighbours, their neighbours and four averaged
  gradients; three linear polynomials, each from a face neighbour and its gradient; three quadratics.

The authors find the scheme insensitive to $C$ and $C_k$. On a 1-D density wave the $L_1$ errors fall
from $2.76\times10^{-4}$ to $5.97\times10^{-11}$ over $\Delta x=1/10$ to $1/80$ (orders 6.26, 8.15, 7.73)
with $\Delta t=0.5\Delta x^2$ (§4.1, Table 1); the shock tests run at CFL 0.8 unless stated, without
troubled-cell detection, which they credit to the two-sided interface update and the temporal limiter rather than to
the reconstruction (§3.4, §4).

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

## Robustness when every stencil is non-smooth

WENO-AO falls back to the third-order small stencils, which does not help when the discontinuity
lies in all of them. Zhang, Ji & Xu (2024d; arXiv v1) measure this in a characteristic-wise,
dimension-by-dimension finite-volume WENO-AO(5,3) with a gas-kinetic or a Lax–Friedrichs flux: it
survives the 123 problem only up to Mach 6.0 (gas-kinetic) or 7.9 (Lax–Friedrichs) and a
hurricane-like vacuum problem up to Mach 2.0 or 1.4, where a first-order fallback driven by a
discontinuity feedback factor raises these to 31.5, 84.1, 16.0 and 7.0 (Tables 5–6; see
[hybrid schemes](/methods/hybrid-weno.md)).

## Other uses and comparisons

- **Small stencils of third order.** Balsara, Samantaray & Subramanian (2023, §6.3), by an overlapping
  author group, contrast WENO-AO with CWENO and WENO-ZQ, whose small stencils are piecewise linear:
  WENO-AO's third-order small stencils "retain the prospect that local extrema could be somewhat
  represented". They take the Legendre basis and the perfect-square indicators of WENO-AO into their
  face-interpolation WENO for divergence-preserving prolongation (§3;
  [divergence-preserving prolongation](/methods/divergence-preserving-prolongation.md),
  [smoothness indicators](/definitions/smoothness-indicator.md)).
- **Unstructured meshes.** Ji, Liang & Fu (2022, §5.8) state, by comparison with a published figure,
  that unstructured WENO5-AO needs about twice their fifth-order TENO's resolution per direction to
  match its Mach-stem roll-up on [double Mach reflection](/benchmarks/double-mach-reflection.md); codes,
  meshes and fluxes differ ([targeted ENO](/methods/targeted-eno.md)).

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
- [Balsara, Samantaray & Subramanian (2023)](/sources/balsara-2023.md) — §3; §6.3.
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §5.8.
- [Zhao et al. (2023)](/sources/zhao-2023.md) — §3.4, Eqs. (28)–(32), Figs. 2–4; §4.1, Table 1.
- [Zhang et al. (2024d)](/sources/zhang-2024-d.md) — §3.1, Eqs. (33)–(39); §4.3, Tables 5–6 (arXiv v1).

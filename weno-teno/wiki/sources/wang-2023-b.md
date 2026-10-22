---
type: Source
title: "Wang et al. (2023) — Fifth-Order A-WENO Schemes Based on the Adaptive Diffusion Central-Upwind Rankine-Hugoniot Fluxes"
description: "Fifth-order A-WENO finite-difference schemes for the 1D and 2D Euler equations, using as two-point flux a central-upwind Rankine–Hugoniot flux whose one-sided speeds are reduced in smooth regions and, in 2D, scaled by a numerical dissipation switch; visibly less dissipative than the adaptive-diffusion central-flux A-WENO scheme."
resource: "doi:10.1007/s42967-021-00161-2"
source_kind: paper
authors: [Wang B.-S., Don W.S., Kurganov A., Liu Y.]
year: 2023
venue: "Commun. Appl. Math. Comput. 5:295-314"
local_file: "/home/stefano/papers/mosaic/weno-teno/2021_Crossref_Communications_on_Applied_Mathematics_and_Computation_Wang_Fifth-Order_A-WENO_Schemes_Based_on_the_Adaptive_Diffusion_C.pdf"
tags: [alternative-weno, central-scheme, numerical-dissipation, finite-difference, euler-equations]
timestamp: 2026-10-21T12:00:00Z
---

# Summary

The paper builds fifth-order [alternative WENO (A-WENO)](/methods/alternative-weno.md)
finite-difference schemes for the 1D and 2D Euler equations. A-WENO evolves point
values $u_i$ with a conservative flux difference. The numerical flux is a two-point
finite-volume flux $h(u^-_{i+1/2},u^+_{i+1/2})$, evaluated on one-sided values from
fifth-order [WENO-Z](/methods/weno-z.md) interpolation applied in
[characteristic variables](/methods/characteristic-decomposition.md), plus a Taylor
correction with central differences of $\partial_x^2f$ and $\partial_x^4f$.

The contribution is the two-point flux, the
[adaptive-diffusion central-upwind Rankine–Hugoniot flux](/methods/adaptive-diffusion-central-upwind-flux.md).
It starts from a [central-upwind flux](/methods/central-upwind-scheme.md) with a
built-in minmod anti-diffusion term, from the
[TVD limiter](/definitions/total-variation-diminishing.md) family. Its one-sided speeds
$a^\pm_{i+1/2}$ are first bounded by the extreme Jacobian eigenvalues and then
tightened with regularized discrete Rankine–Hugoniot speeds. Where a smoothness
detector, the largest relative interface jump of the conserved variables, is at most
$\Delta x^2$, the speeds become symmetric. They are built from the fluid velocity only
and capped at $0.1$ of the previous estimate. In 2D a numerical dissipation switch
scales the acoustic part of the speeds by a ratio of energy jumps, which damps it near
contacts and shear layers.

The paper proves no theorem. The new scheme is compared with the earlier A-WENO scheme
of the same group, which uses an adaptive-diffusion
[Rusanov-type flux](/methods/lax-friedrichs-flux.md). The steppers are both
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md). On the
[isentropic vortex](/benchmarks/isentropic-vortex.md) both reach fifth order, with
slightly larger errors for the new scheme. The new scheme shows less
[numerical dissipation](/definitions/numerical-dissipation.md) on the
[Woodward–Colella blast wave](/benchmarks/woodward-colella-blast-wave.md), the
[Shu–Osher problem](/benchmarks/shu-osher-problem.md),
[double Mach reflection](/benchmarks/double-mach-reflection.md),
[2D Riemann configuration 3](/benchmarks/two-dimensional-riemann-problems.md),
explosion, implosion,
[Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md) and
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md). The
[Lax problem](/benchmarks/sod-and-lax-shock-tubes.md) is run but not reported, and no
[high-Mach jet](/benchmarks/high-mach-astrophysical-jet.md) is run.

# Version read

Version of record (Springer typeset, © Shanghai University 2021): Commun. Appl. Math.
Comput. 5:295–314, published online 1 Nov 2021, with the issue year 2023. It has 20
pages and prints its DOI. Page 1 matches Crossref; Crossref spells the first author
"Wang B.S.", page 1 prints "Bao-Shan Wang". The file name carries the online year 2021.

# Key claims

1. A-WENO fluxes are fifth-order accurate when the sixth-order Taylor expansion $\hat f_{i+1/2}=h(u^-_{i+1/2},u^+_{i+1/2})-\frac1{24}\Delta x^2(\partial_x^2f)_{i+1/2}+\frac7{5760}\Delta x^4(\partial_x^4f)_{i+1/2}$ is used with fifth-order WENO-Z point values (§2, (3)). **Stated**
2. In the finite-difference setting a standard finite-volume flux is limited to second order; the high order of A-WENO comes from the Taylor expansion (§1). **Stated**
3. Until now A-WENO schemes have usually used the Rusanov (local Lax–Friedrichs) flux or its lower-dissipation extension, the adaptive-diffusion central flux (§1). **Stated**
4. Central-upwind fluxes need no Riemann solver, only one-sided local speeds bounded by the largest and smallest Jacobian eigenvalues. In general they carry more numerical dissipation than upwind fluxes (§1). **Stated**
5. The new adaptive-diffusion central-upwind Rankine–Hugoniot flux has less numerical dissipation than the adaptive-diffusion central flux (abstract, §3, §4). **Shown** (qualitatively, Figs. 1–9)
6. Discrete Rankine–Hugoniot speeds $\hat\sigma_{\max}$, $\hat\sigma_{\min}$, the extremes over components $l$ of $\hat\sigma^{(l)}=2[\![f^{(l)}]\!]/\big([\![u^{(l)}]\!]+[\![u^{(l)}]\!]^\epsilon\big)$, tighten the eigenvalue bounds (6) through the algorithm (9) ((7)–(9)). **Stated**
7. Where $\Theta_{i+1/2}\le\Delta x^2$, the one-sided speeds are replaced by symmetric speeds built from the fluid velocity only and capped at $c_{\varsigma}\hat a^\pm_{i+1/2}$ ((13)). This is the paper's new adaptive-diffusion modification. **Stated** (construction; its effect is **Shown**)
8. The numerical dissipation switch reduces the local speeds near contacts and shear layers, where the tangential velocity dominates. Setting $\Psi\equiv1$ recovers the direct 2D extension of (6) (§3.2, (16)–(18)). **Stated**
9. Time integration is three-stage third-order SSP Runge–Kutta, with CFL 0.45 in all examples except the accuracy test (Remark 1). **Stated**
10. The scheme extends to balance laws by adding $S(u_i)$ pointwise, with unchanged fluxes; this is used for Rayleigh–Taylor (Remark 2). **Stated**
11. The 2D scheme works dimension by dimension (Remark 3). **Stated**
12. Parameters: regularization $10^{-10}$ in (8), (9), (12), (16) and (A3); $c_{\varsigma}=0.1$ in (13) and (A1); $\gamma=1.4$ in Examples 1–8 and $\gamma=5/3$ in Example 9 (§4). **Stated**
13. In 1D the new scheme is as robust as the old one on the slowly moving contact, Lax, Shu–Osher and blast-wave problems, most of them unreported. Large differences are not expected in 1D, where the switch is inactive (§4.1). **Stated** (partly **Shown**, Figs. 1–2)
14. Blast wave (Example 1, $\Delta x=1/400$, $t=0.038$): the new scheme gives "a slightly better resolution" (Fig. 1). **Shown**
15. Shu–Osher (Example 2, 200 cells, $t=1.8$): the new scheme reduces the dissipation in the high-frequency waves behind the shock (Fig. 2). **Shown**
16. Isentropic vortex (Example 3, CFL $\Delta x^{2/3}$): both schemes reach fifth order. The $L^2$ density errors at $\Delta x=1/64$ are $3.45\times10^{-9}$ (old) and $3.62\times10^{-9}$ (new). The observed rates are irregular: old 3.27, 2.39, 6.38, 4.99, 6.20; new 3.24, 2.36, 6.37, 4.98, 6.22. The new errors are slightly larger on every grid (Table 1). **Shown**
17. Double Mach reflection (Example 4, $\Delta x=\Delta y=1/480$, $t=0.2$): the new scheme captures the wall-jet roll-up, the triple point and the Kelvin–Helmholtz instabilities along the slip line "much better" (Figs. 3–4). **Shown**
18. 2D Riemann configuration 3 (Example 5, $\Delta x=1/400$, $t=0.8$): the new scheme captures the sideband and neck instabilities of the jet better (Fig. 5). **Shown**
19. Explosion (Example 6, $\Delta x=3/800$, $t=3.2$): the new contact curve is "much curlier" and the mixing layer "slightly wider". The authors read this as lower dissipation, since the physically unstable contact "may be stabilized by the ND only" (Fig. 6). **Shown**
20. Implosion (Example 7, $\Delta x=3/4000$, $t=2.5$): the new jet travels further along $y=x$, taken as a sign of lower dissipation (Fig. 7). **Shown**
21. Kelvin–Helmholtz (Example 8, $\Delta x=1/400$, $t=1,2.5,4$): the new scheme forms more pronounced vortex streets and more complex mixing (Fig. 8). **Shown**
22. Rayleigh–Taylor (Example 9, $\Delta x=1/800$, $t=1.95,2.95$): the new scheme develops secondary mushrooms earlier and a "jellyfish-like" structure (Fig. 9). **Shown**
23. The new scheme outperforms the existing fifth-order A-WENO schemes "without compromising the robustness" (abstract). **Shown** (visual comparison with one earlier scheme; no efficiency data)

# Printed slips

- §4.4, Example 3: "where $r=(x-5)^2+(y-5)^2$", while the formulas use $e^{1-r^2}$ and $e^{0.5(1-r^2)}$; it should be $r^2=(x-5)^2+(y-5)^2$.
- §3.1, (7), (8), (12): $\Delta U^{(i)}_{j+1/2}$ and $\Delta F^{(i)}_{j+1/2}$ are used without definition; only Appendix A defines $\Delta U_{j+1/2}=U^+-U^-$ and the energy jump $\Delta F^{(3)}$.
- §3.1, (9): the first two branches ("if $s^{\max}>\varepsilon$", "if $s^{\min}<-\varepsilon$") can hold together, and the algorithm does not say whether the second overrides the first.
- §3.1, (12): the maximum runs over $1\le i\le3$, written for 1D Euler; the four-component 2D form is not restated.
- Section numbering: "4.1.1 Example 1", "4.2 Example 2", "4.3 2-D Examples", "4.4 Example 3", then "4.4.1 Example 4" to "4.4.6 Example 9".
- §4.4.6 heading: "Raleigh-Taylor" for Rayleigh–Taylor.
- Reference [37] *(compiler check, not in the sources)*: Woodward–Colella, J. Comput. Phys. 54, 115–173, is printed with the year 1988. Crossref gives April 1984 for that volume and page range.

# Notation map

| Wang et al. 2023 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $j$, $k$ (indices in $x$, $y$) | $i$, $j$ | |
| $U_j$ | $u_i$ | point values (finite difference), not cell averages |
| $U$, $F(U)$, $G(U)$ | $u$, $f(u)$, $f^{(2)}(u)$ | |
| $N$ (number of components) | $m$ | **collision** with the DG degree $N$ |
| $F_j:=F(U_j)$ | $f(u_i)$ | point flux used in the derivative stencils (4) |
| $\mathcal F_{j+1/2}$ | $\hat f_{i+1/2}$ | fifth-order A-WENO flux (3) |
| $\mathcal F^{\rm FV}_{j+1/2}$ | $h(u^-_{i+1/2},u^+_{i+1/2})$ | two-point finite-volume flux |
| $(F_{xx})_{j+1/2}$, $(F_{xxxx})_{j+1/2}$ | $(\partial_x^2f)_{i+1/2}$, $(\partial_x^4f)_{i+1/2}$ | |
| $U^-_{j+1/2}$, $U^+_{j+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | agree: $-$ is the left state |
| $\widetilde a^\pm$, $\widehat a^\pm$, $a^\pm$ | $\tilde a^\pm$, $\hat a^\pm$, $a^\pm_{i+1/2}$ | eigenvalue bound, Rankine–Hugoniot-corrected and final one-sided speeds; here $\pm$ means largest positive and smallest negative, not the side |
| $\lambda_1$, $\lambda_N$ | $\lambda_1$, $\lambda_m$ | |
| $\widehat s^{(i)}$, $s^{\max}$, $s^{\min}$ | $\hat\sigma^{(l)}$, $\hat\sigma_{\max}$, $\hat\sigma_{\min}$ (page-local, as on the [CURH flux](/methods/adaptive-diffusion-central-upwind-flux.md) page) | component index $l$ |
| $\Delta U^{(i)}$, $\Delta F^{(i)}$ | $[\![u^{(l)}]\!]$, $[\![f^{(l)}]\!]$ | jumps across the interface |
| $\Delta U^{(i),\varepsilon}$ | $[\![u^{(l)}]\!]^\epsilon$ (local) | sign-preserving jump floored at $10^{-10}$ |
| $U^*_{j+1/2}$, $\delta U_{j+1/2}$ | $u^*_{i+1/2}$, $\delta u_{i+1/2}$ | intermediate state and minmod anti-diffusion |
| $\theta_{j+1/2}$ | $\Theta_{i+1/2}$ (local) | smoothness detector; **collision** with the Zhang–Shu factor $\theta$ |
| $\sigma^\pm$ | $\varsigma^\pm$ (local) | smooth-region speeds (13) |
| $\kappa=0.1$ | $c_{\varsigma}$ (local) | **collision** with the kinetic energy $\kappa$ |
| $\varepsilon=10^{-10}$ | written $10^{-10}$ | regularization, not the WENO $\epsilon$ |
| $\alpha_{j+1/2,k}$, $\Delta\alpha^{(1)}$, $\Delta\alpha^{(2)}$ | $\Psi$, $\Delta^{(1)}$, $\Delta^{(2)}$ (local) | dissipation switch and its energy jumps; **collision** with $\alpha_k$ and the blending $\alpha$ |
| $\alpha_{j+1/2}$, $\alpha^{\min}$, $\alpha^{\max}$, $\widehat\alpha$ (App. A) | $a_{i+1/2}$ of the Rusanov-type flux | the old flux's adaptive diffusion coefficient |
| $\rho$, $u$, $v$, $p$, $E$, $c$, $\gamma$ | $\rho$, $v_1$, $v_2$, $p$, $E$, $c$, $\gamma$ | velocity translated |
| $S(U)$ | $S(u)$ | source term |

# Reference list

The paper prints 38 references, numbered [1]–[38] and sorted alphabetically by first
author, with no DOIs. The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` including `wang-2023-b`. Same-author
same-year pairs take suffixes in printed order (Kurganov 2021 [17]/[18], Schulz-Rinne
1993 [30]/[31]). [29] has the surname "Raghurama Rao". [31] prints only its start page.
[37] is keyed by its printed year. No item is unparseable.

# Pages created or updated

Chunk 1 (2026-10-21), cited further in chunk 2 (2026-10-22). This source is cited on:

* [Adaptive-diffusion central-upwind Rankine–Hugoniot flux](/methods/adaptive-diffusion-central-upwind-flux.md)
* [Alternative WENO (A-WENO)](/methods/alternative-weno.md)
* [Central-upwind schemes](/methods/central-upwind-scheme.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Rankine–Hugoniot jump condition](/definitions/rankine-hugoniot-condition.md)
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
* [WENO-Z weights](/methods/weno-z.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)

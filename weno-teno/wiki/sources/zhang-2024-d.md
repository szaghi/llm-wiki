---
type: Source
title: "Zhang et al. (2024) — A robustness-enhanced reconstruction based on discontinuity feedback factor for high-order finite volume scheme"
description: "Hybrid fifth-order finite-volume reconstruction that keeps WENO-AO unless the discontinuity feedback factor flags the cell and both neighbours, and then uses the central quadratic with its non-constant part scaled by that factor, down to first order; it raises the Mach number survived on near-vacuum tests with gas-kinetic and Lax–Friedrichs fluxes."
resource: "doi:10.1007/s10915-024-02655-6"
source_kind: paper
authors: [Zhang H., Ji X., Zhao Y., Ding Y., Xu K.]
year: 2024
venue: "J. Sci. Comput. 101:20"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Journal_of_Scientific_Computing_Zhang_A_Robustness-Enhanced_Reconstruction_Based_on_Discontinuity.pdf"
tags: [weno, hybrid-scheme, troubled-cell, finite-volume, positivity]
timestamp: 2026-10-30T08:43:00Z
---

# Summary

Zhang et al. (2024d) address the loss of robustness of fifth-order WENO-type finite-volume
reconstruction on 2D structured meshes when strong discontinuities lie in *every* candidate
stencil, for instance when the target cell and both neighbours contain one: nonlinear weights
then have no smooth stencil to select. The remedy is a [hybrid reconstruction](/methods/hybrid-weno.md).
It combines the *discontinuity feedback factor* (DF) of Ji, Shyy & Xu, in an improved form, with
[WENO-AO](/methods/weno-ao.md)(5,3) using WENO-Z-type weights. The DF of a cell,
$\alpha^{\mathrm{DF}}_{ij}\in[0,1]$, is the product over its eight interface Gauss points of
$1/(1+D^2)$, with $D$ built from the pressure jump and the jumps of the normal and tangential
Mach numbers between the left and right interface states. It acts as a physical
[troubled-cell indicator](/definitions/troubled-cell-indicator.md). If
$\max\{\alpha^{\mathrm{DF}}_{i-1,j},\alpha^{\mathrm{DF}}_{ij},\alpha^{\mathrm{DF}}_{i+1,j}\}<0.5$,
the reconstruction in that direction switches from WENO-AO to the central quadratic written in
zero-mean form, with its non-constant part multiplied by $\alpha^{\mathrm{DF}}_{ij}$. As the
factor tends to zero, the interface value tends to the cell average: the scheme falls to first
order. The same test is applied in the tangential sweep to the Gauss points.

Two flux solvers are used: a second-order [gas-kinetic scheme](/methods/gas-kinetic-scheme.md)
flux with two-stage fourth-order time stepping and the nonlinear time-derivative limiter of Zhao
et al., and a Lax–Friedrichs flux with SSP-RK3. Sine-wave advection in 1D and 2D shows fifth
order. On the Shu–Osher problem and two Lax–Liu Riemann configurations the hybrid scheme matches
WENO-AO. Robustness is measured by the largest Mach number a scheme survives: the hybrid raises
it on the 123 problem (gas-kinetic flux 6.0 → 31.5, Lax–Friedrichs flux 7.9 → 84.1), on a
hurricane-like problem (2.0 → 16.0, 1.4 → 7.0) and, less, on a planar-rarefaction Riemann
problem (1.8 → 2.1, 18.1 → 24.8). The evidence is numerical only; no theorem is proved.

# Version read

The archive file is arXiv:2402.10914v1 [math.NA], 19 January 2024, a Springer "Noname
manuscript" template, 25 pages, all read; pp. 6, 7, 10, 11, 19 and 21 were checked on the page
images. It carries three authors (H. Zhang, X. Ji, K. Xu); the Crossref record of the version of
record (J. Sci. Comput. 101:20) has five, adding Y. Zhao and Y. Ding, and the same title. The
DOI is not printed on the file. The version of record may differ in content; every claim,
equation and table number on this page is that of arXiv v1.

# Key claims

Registry notation (see the Notation map). Page-local: $\alpha^{\mathrm{DF}}_{ij}$ the cell DF,
$\alpha^{\mathrm{DF}}_{p,m}$ its value at Gauss point $m$ of face $p$,
$\alpha^{\mathrm{DF}}_{\mathrm{thr}}$ the switching threshold; $\zeta$ the characteristic
variables reconstructed; $u^{(1)}_{\mathrm{DF}}$ the DF-scaled central quadratic; "Ma" the
reference Mach number of a robustness test.

1. Strong discontinuities can lie in all candidate stencils of a WENO reconstruction, which reduces robustness; if cells $i-1$, $i$, $i+1$ all contain discontinuities, "any sub-stencil and large-stencil will not be effective" (Abstract; §3.3; Fig. 1). **Stated**
2. WENO's stencil selection "has relatively poor robustness in certain cases, such as high Mach flows of rarefaction waves" (§1). **Stated**
3. With DF, "the continuous assumption in each cell is no longer necessary for the high-order FVM", so the scheme can reduce to a first-order one, which "can easily achieve the essential positivity preserving property" (§1). **Stated**
4. DF supplies both the stencil weights of the hybrid scheme and its stencil-selection test (§1; §3.3, Eqs. 42–43). **Derived** (construction)
5. Switch: if $\max\{\alpha^{\mathrm{DF}}_{i-1,j},\alpha^{\mathrm{DF}}_{ij},\alpha^{\mathrm{DF}}_{i+1,j}\}<\alpha^{\mathrm{DF}}_{\mathrm{thr}}$ the DF-scaled quadratic is used, otherwise WENO-AO; $\alpha^{\mathrm{DF}}_{\mathrm{thr}}=0.5$ (Remark 1; Eq. 42; Algorithm 1). **Derived**
6. If $\alpha^{\mathrm{DF}}_{ij}\to0$ under (42), the interface value tends to the cell average $\bar\zeta_{ij}$, i.e. first order (§3.3, after Eq. 43). **Derived**
7. A threshold close to 0 "means more discontinuity", close to 1 "means higher resolution"; 0.5 balances robustness and resolution (Remark 1). **Stated** (no parameter study)
8. Fifth order on the 1D sine wave with both solvers: gas-kinetic orders 4.98–5.00, Lax–Friedrichs 4.87–4.98 ($\Delta t=0.25\Delta x$, "CFL ≈ 0.5", $t=2$; Tables 1–2). **Shown**
9. Fifth order on the 2D sine wave ($[-1,1]^2$, CFL 0.1, $20^2$–$160^2$): gas-kinetic orders 4.87–4.98, Lax–Friedrichs 4.73–4.95 (Tables 3–4). **Shown**
10. Shu–Osher problem ($\Delta x=1/40$, $t=1.8$, CFL 0.5): WENO-AO and the hybrid are both more accurate than van Leer; the hybrid's extrema are "slightly lower" than WENO-AO's (§4.2.1, Fig. 3). **Shown**
11. Lax–Liu configuration 3 ($500^2$, $t=0.6$): the hybrid resolves the shear layer better and shows stronger vortex-sheet instabilities than WENO-AO (§4.2.2, Fig. 4). **Shown**
12. Configuration 6 ($800^2$, $t=1.6$): WENO-AO and the hybrid give "very close results" (§4.2.3, Fig. 5). **Shown**
13. 123 problem, largest Mach number survived (100 cells, $t=0.14$): gas-kinetic flux WENO-AO 6.0, hybrid 31.5, van Leer 31.5; Lax–Friedrichs flux WENO-AO 7.9, hybrid 84.1, van Leer 119.5 (Table 5, Figs. 6–7). **Shown**
14. The text states that the hybrid "achieves the same robustness as using the van Leer limiter, similarly under the L-F solver" (§4.3.1), while Table 5 gives 84.1 against 119.5 for the Lax–Friedrichs flux. **Shown** (table) / **Stated** (text)
15. Hurricane-like problem ($[-2,2]^2$, $\Delta x=1/100$, 50 time steps): largest Mach number, gas-kinetic flux WENO-AO 2.0, hybrid 16.0; Lax–Friedrichs flux 1.4 and 7.0 (Table 6, Figs. 8–9). **Shown**
16. A scheme that survives the first 50 steps of the hurricane-like problem "will keep positivity in longer time simulation", since the strongest rarefaction occurs early (Remark 2). **Stated**
17. In the hurricane-like problem the low-DF region starts near the vacuum centre and spreads outward with the rarefaction (§4.3.2, Fig. 10). **Shown**
18. Planar rarefactions, configuration 2 ($\Delta x=1/400$, $t=0.15$): largest Mach number, gas-kinetic flux WENO-AO 1.8, hybrid 2.1; Lax–Friedrichs flux 18.1 and 24.8, a "limited improvement in robustness compared to the Hurricane-like problem" (Table 7, Figs. 12–13). **Shown**
19. In configuration 2, DF near 0 lies "mainly ... in the region where the rarefaction waves are in contact with the shocks" (Fig. 14). **Shown**
20. The Lax–Friedrichs solver with SSP Runge–Kutta "has the positive-preserving property", so its robustness "is only affected by the spatial reconstruction" (§2.3, §4). **Stated** (no proof or limiter)
21. The two-stage fourth-order method reaches fourth order in time with two stages, a "significant reduction in computational cost" against RK4, and "became the dominant approach in the development of high-order GKS" (§1). **Stated**
22. The two-stage method ignores possible temporal discontinuities of the flux, which affects stability; Zhao et al.'s nonlinear time-derivative limiter controls them (§2.2, Eqs. 27–29). **Stated**
23. The idea "operates primarily on spatial reconstruction" and generalizes easily to arbitrary order on structured or unstructured meshes (§5). **Stated**
24. A priori limiters (van Leer, van Albada, Michalak–Ollivier-Gooch, Kitamura–Shima) "usually have parameters that behave as distinct differences in different cases"; a posteriori limiters (MOOD) "are usually computationally expensive" (§1). **Stated**
25. A numerical collision time with $C_2=5$ gives $e^{-1/5}=0.8187$, "advantageous for the robustness" (§2.2, Eq. 20). **Stated**

*(Compiler checks, not in the sources.)* With $d_{\mathrm H}=d_{\mathrm L}=0.85$, Eq. (35) gives
$d_3=0.85$, $d_1=0.1275$, $d_0=d_2=0.01125$, summing to 1. With
$\alpha^{\mathrm{DF}}_{ij}=1$, the scaled quadratic (43) reduces to the central candidate
$p^{r3}_1$ of Eq. (33): its value at the interface is
$-\tfrac16\bar\zeta_{i-1}+\tfrac56\bar\zeta_i+\tfrac13\bar\zeta_{i+1}$. The reformulated update
(27) reduces to the two-stage update (21) when the limited derivative equals the unlimited one.

# Printed slips

- Eq. (24), second line: printed $\tfrac12\partial_t\mathbf F^n_{p,m}\Delta t+\tfrac18\partial_t\mathbf F^n_{p,m}\Delta t^2=\mathbb F(W^n,\Delta t/2)$ (checked on the page image of p. 6). *(Compiler check, not in the sources:)* integrating the linear flux (23) over $[0,\Delta t/2]$ gives $\tfrac12\mathbf F^n_{p,m}\Delta t+\tfrac18\partial_t\mathbf F^n_{p,m}\Delta t^2$, and the printed solution (25) solves this corrected system, so (24) differs from this integral and (25) agrees with it.
- Eq. (14) (checked on the page image of p. 5): the last two terms carry $e^{t/\tau_n}$, with a positive exponent, while the first terms carry $e^{-t/\tau_n}$ and the integral solution (13) has $e^{-t/\tau}$ on the initial-data term.
- p. 7: "According to Eq. (32), $W^*_i$ can be obtained", and the end of §3.4: "all components in Eq. (32) can be determined"; Eq. (32) is SSP-RK3, the two-stage stage is Eq. (21) and the gas-kinetic distribution Eq. (14).
- Eq. (28) prints the prefactor $-\frac1{\Omega_{ij}}$ where Eq. (26) has $-\frac1{\lvert\Omega_{ij}\rvert}$. §3.1 mentions coefficients "$c_0,\cdots,c_5$" of a quartic with $c_0,\dots,c_4$.
- Table 2, $L_2$ order 20 → 40: printed 4.87. *(Compiler check, not in the sources:)* $\log_2(9.691440\times10^{-5}/3.094034\times10^{-6})=4.97$.
- Table 4, $L_\infty$ order 20 → 40: printed 4.92. *(Compiler check, not in the sources:)* $\log_2(4.420067\times10^{-4}/9.380738\times10^{-6})=5.56$; either the $20^2$ error or the order is misprinted.
- Eq. (55), quadrant $x\ge0.5$, $y\ge0.5$: printed "(1.0.6323, 0.6323, 1.5)"; quadrants 2 and 4 give $\rho$ symbolically, while the text varies "the value of $p$" and the caption of Fig. 11 says "$p=0.4$".
- §4.3.2 defines the high-speed regime as $\mathrm{Ma}>\sqrt2$, yet Table 6 reports $\mathrm{Ma}=1.4<\sqrt2$ as the largest value survived by WENO-AO with the Lax–Friedrichs flux.
- §4.3.3 cites "Configuration 2 in Ref [27]" (Liska–Wendroff), configurations 3 and 6 to Lax–Liu [24].
- §1 cites [33] (Shu & Osher 1988, ENO) for TENO recovering "the robustness of the classical fifth-order WENO scheme".
- Algorithm 1, line 6: "if without condition min{max{...}, $\alpha_{threshold}$} then cycle termination", not a well-formed condition.
- Typos: "the 2rd-order GKS solver" (§4), "shokc-shock" (§4.2.2); "$e^{-1/5}$ approaches 1.0(0.8187)" (§2.2). The template placeholder "MSC code1 · MSC code2 · more" is unfilled. Ref. [42] prints its authors as "Yue, Z., Kun, X.".

# Notation map

| Zhang et al. (arXiv v1) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $W=(\rho,\rho U,\rho V,\rho E)$, $W_{ij}$ | $u$, $\bar u_{ij}$ | $E$ specific total energy in the source; registry $E$ is per volume |
| $U$, $V$ | $v_1$, $v_2$ | velocity |
| $Q$ | $\zeta$ | characteristic variables; **collision** with the SBP $Q$ |
| $\Omega_{ij}$, $\Gamma_{ij,p}$, $\mathbf x_{p,m}$, $A_m$ | cell, face $p$, Gauss points and weights $\tfrac12$ (local) | |
| $\mathcal L$ | $\mathcal L$ | agree |
| $p^{r3}_k$ ($k=0,1,2$), $p^{r5}_3$ | three quadratic candidates $u^{(k)}$ on $S_0,S_1,S_2$ and the quartic on the full stencil | |
| $d_k$, $d_H$, $d_L$ | $d_k$, $d_{\mathrm H}$, $d_{\mathrm L}$ | WENO-AO linear weights |
| $\beta_k$ | $\beta_k$ | Jiang–Shu form, up to the degree of each polynomial |
| $\tau_Z=\tfrac13\sum_{k=0}^2\lvert\beta_3-\beta_k\rvert$ | $\tau$ (local definition) | WENO-Z-type global indicator |
| $\omega_k$, $\bar\omega_k$ | $\alpha_k$, $\omega_k$ | **collision**: source $\omega_k$ are unnormalized |
| $\varepsilon$ | $\epsilon$ | $10^{-6}$ stated at Eq. (29) |
| $\alpha_{ij}$, $\alpha_{p,m}$, $D$ | $\alpha^{\mathrm{DF}}_{ij}$, $\alpha^{\mathrm{DF}}_{p,m}$, $D$ (local) | DF; **collision** with $\alpha_k$ and the DG–FV $\alpha$ |
| $\alpha_{thres}$ | $\alpha^{\mathrm{DF}}_{\mathrm{thr}}$ (local) | 0.5 |
| $\omega^t_p$, $\tilde\alpha^k_{1,2}$, $\alpha^k$ | time-derivative limiter weights (local) | **collision** of $\alpha^k$ with the DF |
| $f$, $g$, $\tau$, $\tau_n$, $C_1$, $C_2$ | distribution, Maxwellian, collision time, numerical collision time, constants (local) | $\tau$ is not the WENO-Z indicator |
| $\lambda$, $K$, $\xi$ | inverse temperature, internal degrees of freedom, internal velocity (local) | not eigenvalues, stencil size or DG nodes |
| $\mathrm{Ma}_n$, $\mathrm{Ma}_t$, Ma | normal and tangential Mach numbers, test Mach number | registry $M$ |

# Reference list

The file prints 44 references, numbered [1]–[44] in alphabetical order. The list is merged
complete into the [bibliography](/bibliography.md), with `citedby` including `zhang-2024-d`.
Two printed keys name works other than the existing entries of the same key and are re-keyed at
the merge: Li et al. 2023 (one-stage gas-kinetic scheme for multi-component flows, printed
without volume) and Ji, Shyy & Xu 2021 (the DF source, Int. J. Comput. Fluid Dyn.). The two
Harten 1997 items are resolved by title, volume and page against the existing entries. Ref. [42]
prints apparently inverted author names and is kept as printed; ref. [14] (ENO III) is printed
as "Springer (1997)" without a journal. No item is unparseable.

# Pages created or updated

Chunk 9 (2026-10-23), cited further in chunks 10–12 (2026-10-23/30). This source is cited on:

* [Gas-kinetic schemes](/methods/gas-kinetic-scheme.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [WENO-AO (adaptive-order WENO)](/methods/weno-ao.md)

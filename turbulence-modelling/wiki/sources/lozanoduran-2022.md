---
type: Source
title: "Lozano-Durán et al. (2022) — Performance of Wall-Modeled LES with Boundary-Layer-Conforming Grids for External Aerodynamics"
description: "Wall-modelled LES of the NASA Juncture Flow with charLES on constant-size and boundary-layer-conforming Voronoi grids: a cost model for conforming grids, error-scaling laws by flow region, a split of wall-model errors into external and internal parts, and non-monotonic grid convergence in channel flow."
resource: "doi:10.2514/1.j061041"
source_kind: paper
authors: [Lozano-Durán A., Bose S.T., Moin P.]
year: 2022
venue: "AIAA J. 60:747-766"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_AIAA_Journal_Lozano-Durán_Performance_of_Wall-Modeled_LES_with_Boundary-Layer-Conformi.pdf"
tags: [wmles, wall-model, les, boundary-layer, grid-requirements, separated-flow]
timestamp: 2026-10-26T20:47:00Z
---

# Summary

Lozano-Durán et al. (2022) measure the cost and the error scaling of
[wall-modelled LES](/methods/wall-modelled-les.md) on an
external-aerodynamics case, the [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md)
(wing–fuselage model, crank-chord $Re_c=2.4\times10^6$, $M_\infty=0.189$,
angle of attack $5^\circ$, trailing-edge corner separation). Every run uses
[CharLES](/software/charles.md): a second-order,
[kinetic-energy-conserving](/properties/kinetic-energy-preservation.md)
finite-volume code on Voronoi grids, with the
[dynamic](/methods/dynamic-procedure.md) [Smagorinsky model](/methods/smagorinsky-model.md)
and an algebraic [equilibrium wall model](/methods/equilibrium-wall-model.md)
(the [law of the wall](/definitions/law-of-the-wall.md) with a quadratic
near-wall branch) matched at the first off-wall cell centre.

The paper compares constant-size grids with
[boundary-layer-conforming grids](/methods/boundary-layer-conforming-grid.md),
whose local isotropic size is $\Delta\approx\delta/N_{bl}$, floored by a
minimum grid Reynolds number $Re_\Delta^{\min}$ and capped by half the
surface radius of curvature. The local $\delta$ comes from the deviation of
the wall-modelled mean velocity from an inviscid solution. A cost model
gives $N_{\mathrm{points}}\sim N_{bl}^{13/6}Re\,(Re_\Delta^{\min})^{-5/6}$
(see [grid-point requirements](/results/les-grid-point-requirements.md)).
An error model $e_q=b_q(\Delta/\delta)^{a_q}$ is
calibrated on [channel flow](/benchmarks/turbulent-channel-flow.md) at
$Re_\tau=4200$ ($e_u\approx0.08\,\Delta/\delta$), and a
propagation analysis of the wall model separates external errors (in the
LES velocity at $h_{\mathrm{wm}}$) from internal errors (in $\kappa$, $B$).

$C_p$ errors stay below 5% on every grid, even with 0–1 points per $\delta$,
and an inviscid run gives nearly the same $C_p$. Mean-velocity errors are
3–8% on the fuselage, about 15% at the wing–body juncture and about 100% in
the separated corner. Conforming grids lower the error constant $b_u$
but leave the rate $a_u$ unchanged: 12 M cells beat a 31 M
constant-size grid. The authors attribute this to errors advected
downstream from the under-resolved leading edge. An appendix documents
non-monotonic WMLES convergence in channel flow at
$\Delta/\delta\approx0.03$–$0.05$, where the grid begins to support
near-wall streaks; runs without an SGS model there are
[implicit LES](/definitions/implicit-les.md), with
[numerical dissipation](/properties/numerical-dissipation.md) as the model.
The paper cites [hybrid RANS/LES](/definitions/hybrid-rans-les.md) as the
other route to high Reynolds numbers, and uses
[DNS](/definitions/direct-numerical-simulation.md) data as the channel reference.

# Version read

arXiv preprint 2107.01506v1 [physics.flu-dyn], 3 July 2021, 43 pages (text
and appendices pp. 1–37, references pp. 38–43); not the AIAA version of
record. Page 1 title and authors match the published article. Metadata
(year, venue, DOI) are those of the published version. Equation, section,
figure and page numbers on this page are those of the preprint.

# Key claims

1. $C_p$ is predicted with less than 5% error on all grids, including boundary layers resolved with 0–1 points per $\delta$; errors are 1–5% overall (Abstract; §V.E; Fig. 21a). **Shown**
2. The $C_p$ accuracy follows from its inviscid nature: under the thin-boundary-layer approximation the wall-normal integral of the mean momentum equation gives $p_{\mathrm{wall}}=p_I$, the inviscid pressure, so $e_p=b_p(\Delta/\delta)^{a_p}Re^0$ with $b_p\ll1$ and $a_p\approx0$ (§IV.B, Eq. 10). **Derived**
3. A free-slip inviscid run on the C-D2 grid gives a $C_p$ "strikingly similar" to the wall-modelled run (§V.E, Fig. 20e). **Shown**
4. $C_p$ discrepancies concentrate at the wing leading edge (curvature radius not much larger than $\delta$; tripping differs from the experiment) and at the wing tip (tip-vortex roll-up); at the tip the error scales linearly, $e_p\sim\Delta/\delta_c$, and case C-N10-R2e3 is best (§V.E, Fig. 21b). **Shown**
5. For a flat-plate zero-pressure-gradient boundary layer with $\delta/x=K\,Re_x^{-1/7}$, $K=0.16$, the point count of a conforming grid is given exactly by Eq. (13) and scales as $N_{\mathrm{points}}\sim N_{bl}^{13/6}Re\,(Re_\Delta^{\min})^{-5/6}$ for $Re\gg Re_\Delta^{\min}$ (Eq. 6; App. A). **Derived**
6. Under a convective limit $\Delta t\sim\Delta_{\min}/U_\infty$, $N_{\mathrm{steps}}\sim\tilde T\,Re\,(Re_\Delta^{\min})^{-1}$ with $\tilde T=TU_\infty/L$ (Eq. 7). **Derived**
7. At $Re=5\times10^6$, $N_{bl}\approx5$ and $Re_\Delta^{\min}\approx10^4$ need $O(10)$ million points, while $N_{bl}\approx20$ and $Re_\Delta^{\min}\approx10^3$ need $O(1000)$ million points, "which renders WMLES unfeasible as a routine tool in industry"; flight $Re\approx5\times10^7$ multiplies $N_{\mathrm{points}}$ by about ten (§III.B, Fig. 6). **Derived** (numerical integration of Eq. 5 on the Juncture Flow geometry)
8. The subgrid-boundary-layer region for $Re_\Delta^{\min}<10^4$ is confined to less than 10% of the chord at the wing leading edge (§III.B, Fig. 6b). **Shown**
9. The expected mean-velocity error is $e_u=b_u(\Delta/\delta)^{a_u}Re^0$, with $a_u=0$ when $\Delta/\delta$ lies in the shear-dominated range and $a_u=1$ in the inertial range (Eq. 11, after Lozano-Durán & Bae [61]). **Derived** (scaling argument)
10. In WMLES of channel flow at $Re_\tau=4200$ with CharLES (dynamic Smagorinsky, equilibrium wall model, isotropic grids $\Delta/\delta=1/3,1/5,1/10$), $e_u\approx0.08\,\Delta/\delta$; a staggered finite-difference solver gives the same linear trend (§IV.B, Fig. 7b). **Shown**
11. The DNS–inviscid difference, about 15%, bounds the mean-velocity error in canonical flows: "even a low performance WMLES is bounded by a maximum error of ∼15%" (§IV.B, Fig. 7b). **Shown**
12. Near a corner the error is set by the shear length $L_s\approx u_\tau/S$; with $S\sim u_\tau/d$, $e_u\sim\Delta/d$, which motivates the compensated error $e_u d_{\min}/\delta$ (§IV.B, after [61]). **Derived**
13. In the equilibrium wall model, external errors (in the LES velocity at $h_{\mathrm{wm}}$) propagate roughly linearly, $e_{u_\tau}\propto e_{u_\parallel}$; internal errors $e_\kappa=10\%$ and $e_B=10\%$ give $e_{u_\tau}\approx6\%$ and $\approx3\%$, both below the $\approx10\%$ of an external error $e_{u_\parallel}=10\%$: "wall models are more resilient to internal errors than to external errors" (§IV.C, Eq. 12, Fig. 8). **Derived** (Eq. 12) and **Shown** (channel points on Fig. 8a)
14. Internal errors set a floor, so WMLES may not converge to DNS until $\Delta$ and $h_{\mathrm{wm}}$ reach the wall-resolved regime; external errors raise $b_u$ without changing $a_u$ appreciably (§IV.C). **Stated**
15. On the fuselage (station 1) mean-velocity errors are about 3–8% and scale as $e_u\approx b_u\,\Delta/\delta$ with $b_u\approx0.14$, above the channel value 0.08, which the authors attribute to upstream error propagation (§V.B, Fig. 15a). **Shown**
16. Errors are about 15% at the wing–body juncture (station 2) and about 100% at the separated trailing edge (station 3); after compensation by $d_{\min}/\delta$ the juncture converges at $a_u\approx0.4$, the trailing edge at $a_u\approx0.6$ with a larger $b_u$ (§V.B, Fig. 15). **Shown**
17. On constant-size grids the juncture and trailing edge have roughly 30–80 points per $\delta$, an order of magnitude more than the fuselage, yet worse accuracy (§V.B). **Shown**
18. Conforming case C-N5-R2e3 (12 M control volumes) outperforms constant-size case C-D2 (31 M) at the juncture and trailing edge "using only one fourth of the number of grid points in each spatial direction"; the number of control volumes is "a misleading metric" of WMLES quality (§V.C, Fig. 16). **Shown**
19. Conforming grids are more accurate at all three stations; at the juncture and the separation the gain is a reduction of $b_u$ with $a_u$ unchanged; on the fuselage the error saturates near 2%, consistent with an internal error from a 3% deviation in $\kappa$ (§V.C, Fig. 17a). **Shown**
20. Errors from the under-resolved leading edge propagate downstream over a recovery length $\Delta x_e\approx\Gamma U_\infty\delta_0/u_\tau$; with $\Delta x_e\approx300\delta_0$ [69] and $\delta_0\approx1$ mm this is about 300 mm, half the crank chord (§V.C). **Derived**
21. Plotting errors against an upstream Gaussian-averaged resolution $\Delta/\bar\delta$ collapses the constant-size fuselage errors onto the channel reference, "confirming that the diminished performance of constant-size grids is merely a matter of downstream error propagation" (§V.C, Fig. 17b). **Shown**
22. Halving $Re_\Delta^{\min}$ improves the velocity profiles; convergence goes as $(Re_\Delta^{\min})^{\alpha}$ with $\alpha\approx1$–2, steeper than in $N_{bl}$, so leading-edge resolution is less demanding than that of the downstream boundary layers (§V.D, Fig. 19d). **Shown**
23. The leading-edge propagation model $e_u\sim N_{bl}^{-1}\left[1+\Gamma Re_\Delta^{\min}N_{bl}/\left(Re_x-(Re_\Delta^{\min}N_{bl}/K)^{7/6}\right)\right]$, $\Gamma=300$, $K=0.16$, reproduces the trends of Fig. 19(d) (§V.D). **Derived** and **Shown**
24. WMLES (C-D0.5) predicts a separation bubble about 100 mm long and 60 mm wide, about 15% smaller than the oil-film measurement (120 × 80 mm), consistent with previous WMLES [26–28]; the two measures are not one-to-one comparable (§V.F, Fig. 22). **Shown**
25. Resolved tangential Reynolds stresses follow the experimental trends but are under-predicted at the juncture and trailing edge, as expected from $R_{ij}^{\exp}\approx\langle\bar u_i'\bar u_j'\rangle+\langle\tau_{ij}\rangle$; turbulence-intensity errors scale as $(\Delta/\delta)^{2/3}$ with values of 10–30% [61] (§V.B). **Shown** / **Stated**
26. Channel WMLES converges non-monotonically: both CharLES and the finite-difference solver depart from $e_u\sim\Delta$ for $\Delta/\delta\approx0.03$–$0.05$ and recover the linear trend below 0.03 (App. B, Fig. 23b). **Shown**
27. Without an SGS model and with the exact DNS mean wall stress imposed, channel-flow structure changes at $\Delta_c/\delta\approx0.03$–$0.05$: noisy for $\Delta>\Delta_c$, streaks for $\Delta<\Delta_c$ (Fig. 24, $y=0.3\delta$); $\Delta_c$ is about the same for both solvers, which suggests a physical origin (App. B). **Shown** (mechanism **Stated**)
28. Costs on Intel Xeon E5-2670 (NASA Pleiades): 31, 40, 75, 116, 398 thousand core-hours for C-D7, C-D4, C-D2, C-D1, C-D0.5 (14, 17, 31, 50, 174 M cells); 27, 90, 13 thousand core-hours for C-N5-R2e3, C-N10-R2e3, C-N5-R5e3 (12, 40, 6 M cells) (§V.A). **Shown**
29. All WMLES cost estimates in the literature [23, 57–59] presuppose conforming grids, yet "WMLES of an aircraft geometry has never been conducted using a true BL-conforming grids until the present work" (§III.B). **Stated**
30. RANS models predicted the onset and extent of three-dimensional separation in wing–fuselage junctions poorly in the Drag Prediction Workshops (§I, [11, 12]). **Stated**

# Printed slips

1. §III.B, p. 10: "$\delta\sim(x-x_e)[(x-x_e)U_\infty/\nu]^{-m}$ … and $m\approx-1/7$". With the printed sign this gives $\delta\sim x\,Re_x^{+1/7}$, against App. A, "$\delta/x=KRe_x^{-1/7}$". The same sentence calls $x_e$ "the streamwise distance to the leading edge" while using it as the leading-edge position.
2. App. A, p. 35: "the number of grid points for BL-conforming grids scales as $N_{bl}^{13/6}(Re_\Delta^{min})^{5/6}Re$"; Eq. (6) and Eq. (13) give $(Re_\Delta^{\min})^{-5/6}$.
3. Eq. (10), p. 14 (repeated p. 31): "$\varepsilon_p=\beta_p(\Delta/\delta)^{\alpha_p}Re^0$, with $\beta_p\ll1$, $\alpha_q\approx0$": the subscript should be $p$.
4. §V.A, p. 18: "Eight cases are considered. In the first six cases, we employ grids generated using strategy (i)": five constant-size cases are listed (C-D7, C-D4, C-D2, C-D1, C-D0.5), which with the three conforming cases make eight.
5. §V.A, p. 19: "Figure 9(a) features the resolution map for case C-D4", while the Fig. 9 caption reads "(a) constant-size grid for case C-D2".
6. §IV.C, p. 17: channel runs with "Δ/δ = 1/3, 1/5, and 1/10", while the Fig. 8 caption reads "Δ/δ = 1/3, 1/6 and 1/10".
7. §V.D, p. 27: "$Re_\Delta^{min}=2.6\times10^3$ and $Re_\Delta^{min}=5.8\times10^3$ for C-N5-R2e3 and C-N5-R5e3", while §V.A, the Fig. 18 caption and the case names give $2.8\times10^3$ and $5.6\times10^3$.
8. Fig. 20 caption, p. 31: "Panels (a), (b), (c) and (d) show $C_p$ for cases C-D7, C-D4, C-D2, C-N5-R2e3, and C-N5-R2e3": C-N5-R2e3 is listed twice (five cases for four panels).
9. §V.C, p. 26: in $\bar\delta=\int_{-\infty}^xG(x'-x)\delta(x',y,z)\,dx$ the differential is printed $dx$ instead of $dx'$.
10. Fig. 16 caption refers to a panel "(d) Error in the mean velocity profile …" that the three-panel figure does not have; the text uses Fig. 17(a) for it.
11. §IV.C, p. 17: "the sensitivity of $\varepsilon_{u_\tau}$ to $Re_{h_w}$ is weak and scales as $\varepsilon_{u_{||}}\sim\ln(Re_{h_w})$": the error named in the formula is not the one named in the sentence.
12. Reference list: [33] Deardorff "Vol. 41, No. 1970, 1970" (issue printed as the year); [66] first author printed "JCR, H." (Hunt J.C.R.); [55] year printed "????".

# Notation map

| Lozano-Durán et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x,y,z$ (aircraft frame: $x$ from the nose, $y$ spanwise, $z$ vertical) | — | **collision**: the source's $y$ is spanwise on the aircraft; the registry's wall-normal $y$ is the source's $y_\perp$ |
| $y_\perp$, $y_\perp^+$ | $y$, $y^+$ | local wall-normal coordinate |
| $u_{\vert\vert}$, $x_{\vert\vert}$, $z_{\vert\vert}$ | $u_\parallel$; wall-parallel coordinates | wall-parallel velocity of the wall model; equals $U_{\mathrm{LES}}$ at $h_{\mathrm{wm}}$ |
| $h_w$, $Re_{h_w}=\breve u_\tau h_w/\nu$ | $h_{\mathrm{wm}}$, $Re_{h_{\mathrm{wm}}}$ | matching height = first off-wall cell centre |
| $\kappa=0.41$, $B=5.2$, $a_1$ | $\kappa$, $B$ | $a_1$ fixes $C^1$ continuity of the quadratic branch at $y^+=23$; value not printed |
| $L$ (crank chord, 557.1 mm), $Re=LU_\infty/\nu$ | $Re_c$ | App. A reuses $Re=L_xU_\infty/\nu$ (plate length) |
| Ma | $M_\infty$ | |
| $\Delta$ | $\Delta$ | isotropic Voronoi grid size, the implicit filter width |
| $\delta$ | $\delta$ | here from a 1% deviation from an inviscid solution (Eqs. 3–4), not $\delta_{99}$ |
| $\bar\delta$ | — | upstream Gaussian-averaged $\delta$, not a filtered quantity |
| $\overline{(\cdot)}$ (§IV.B) | $\langle\cdot\rangle$ | **collision**: spanwise and time average there, not the LES filter |
| $\langle\cdot\rangle$, $(\cdot)'$ | $\langle\cdot\rangle$, $(\cdot)'$ | time average and fluctuation |
| $\langle u_i'u_j'\rangle$ (resolved) | $\langle\bar u_i'\bar u_j'\rangle$ | resolved part of $R_{ij}$, positive convention |
| $\tau_{ij}^{SGS}$ | $\tau_{ij}$ | definition and sign not printed |
| $\varepsilon_q$, $\beta_q$, $\alpha_q$ | $e_q$, $b_q$, $a_q$ (page-local, registry §11) | relative error, error constant, convergence rate of quantity $q$ ($p$ for $C_p$, $u$ for the mean velocity); renamed to avoid $\varepsilon$ (dissipation), $\beta(\boldsymbol x)$ and $\alpha$ |
| $\gamma=1.2$, $\beta=1/2$ | — | **collision** with $\gamma$ (ratio of specific heats) and $\beta$; safety factor on $\delta$ and curvature factor in Eq. (2) |
| $\breve q$, $q=\breve q(1+e_q)$ | — | exact value and its relative error |
| $E_k\sim\Delta^{-a}$ | $E(k)$ | energy at scale $\Delta$; $a$ the spectral slope |
| $S$, $L_s\approx u_\tau/S$ | $\mathrm d\langle u\rangle/\mathrm dy$ | **collision**: $S$ is the mean shear, not $\lvert S\rvert$ |
| $d$, $d_{\min}$ | $d$ | distance to the wall; to the closest of two walls |
| $N_{bl}$, $Re_\Delta^{\min}=\Delta_{\min}U_\infty/\nu$ | — | points per $\delta$; minimum grid Reynolds number |

# Reference list

72 printed references in numbered style ([1]–[72], order of citation),
merged complete into the [bibliography](/bibliography.md) with `citedby`
`lozanoduran-2022`. No printed duplicates. Irregular items: [5] has no
author (AIAA Recommended Practice R-154-2021, corporate author AIAA); [55]
has year "????" and is dated from its printed DOI; [66] prints its first
author as "JCR, H." (Hunt J.C.R.); [70] is a personal communication without
title; [33] prints its issue as "No. 1970".

# Pages created or updated

Chunk 1 (2026-10-25), cited further in chunks 2, 4. This source is cited on:

- [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Boundary-layer-conforming grids for wall-modelled LES](/methods/boundary-layer-conforming-grid.md)
- [Building-block-flow wall model](/methods/building-block-flow-wall-model.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [CharLES](/software/charles.md)

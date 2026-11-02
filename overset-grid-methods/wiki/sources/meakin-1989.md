---
type: Source
title: "Meakin & Suhs (1989) — Unsteady aerodynamic simulation of multiple bodies in relative motion"
description: "Moving-body Chimera paper: a thin-layer Navier–Stokes solver with time metrics, coupled each step to an unsteady PEGASUS (the domain connectivity function) whose search is restricted to bands around the previous hole boundaries, cutting assembly cost about threefold under a one-cell hole-motion constraint; store and Shuttle SRB separation demonstrations."
resource: "doi:10.2514/6.1989-1996"
source_kind: paper
authors: [Meakin R.L., Suhs N.E.]
year: 1989
venue: "AIAA 9th Computational Fluid Dynamics Conference, AIAA Paper 89-1996-CP, pp. 643-657"
local_file: "/home/stefano/papers/mosaic/overset-chimera/1989_Crossref_9th_Computational_Fluid_Dynamics_Conference_MEAKIN_Unsteady_aerodynamic_simulation_of_multiple_bodies_in_relati.pdf"
tags: [overset-grid, chimera, moving-grid, domain-connectivity, store-separation, compressible]
timestamp: 2026-11-02T11:26:00Z
---

# Summary

Meakin and Suhs present a prototype method for time-accurate simulation of
viscous flow about several bodies in relative motion, the earliest
[moving-overset-grid](/methods/moving-overset-grid.md) method among the
chunk-1 sources. The authors frame
the Chimera [overset grid](/definitions/overset-grid.md) as a Schwarz-type
overlapping decomposition with one added feature: bodies cut holes in
neighbouring grids ([hole cutting](/methods/hole-cutting.md)). The resulting
artificial boundaries receive interpolated data, and this is what makes
moving multi-body problems possible.

The method has three functions coupled in a cycle. The Aerodynamic Function
(ADF) is an implicit, approximately factored, partially flux-split
thin-layer Navier–Stokes solver, extended here with the time metrics
$\xi_t,\eta_t,\zeta_t$. The Body Dynamics Function (BDF) is not implemented;
trajectories are prescribed. The Domain Connectivity Function (DCF) is a
modified PEGASUS ([PEGSUS and PEGASUS 4](/software/pegasus.md); see also
[DCF and DCF3D](/software/dcf3d.md)) that recomputes
[domain connectivity](/definitions/domain-connectivity.md) at every step.
The flow solver sees the Chimera logic only through the 0/1 mask $i_b$
([point classification](/definitions/point-classification.md)), which
multiplies the time step and the dissipation so that hole points are frozen.

The DCF uses the hole and boundary positions at time level $n$ to restrict
the search at level $n+1$ to the points on either side of the old hole
boundaries ([donor search](/methods/donor-search.md)). This lowers the
assembly cost relative to one flow-solver step by about a factor of 3. It
also imposes a hole-motion constraint: no hole point may become a field
point without first being an interpolated boundary point, that is, a
[fringe point](/definitions/fringe-point.md). The solver extension is checked
on a plunging NACA 64A010 airfoil, and the two-grid static coupling on the
AFATL wing with an ogive-cylinder store against wind-tunnel data. Two moving
demonstrations follow: a [store separating](/benchmarks/store-separation.md)
from the wing and Space Shuttle SRB separation. The paper's
[inter-grid interpolation](/methods/inter-grid-interpolation.md) is
delegated to PEGASUS, and the authors state that the effect of the
inter-grid updating on time accuracy is not addressed.

# Version read

Version of record: the AIAA proceedings, AIAA Paper 89-1996-CP, pp. 643–657
(15 PDF pages: 6 of text, 1 of references, 6 of figures, 2 colour plates).
The PDF has a text layer. Equations (1) and (2), the time-metric relations
and the DCF/ADF value of the Shuttle row of Table 1 were read visually at
300 dpi. Page 1 ("Robert L. Meakin", "Norman E. Suhs") matches Crossref. No
DOI is printed. Locators are proceedings sections and pages.

# Key claims

Registry notation: the source's $\tau$ is $t$; its $\hat Q$ is
$\hat{\mathbf q}$ (see the slips); its $e$ is $E$; $i_b$ is the 0/1 mask,
translated to $\iota$; "interpolated (hole) boundary points" are receptors
$\mathcal R_k$; $\tilde K$ is $k_{\mathrm r}$.

1. The method aims at time-accurate simulation of 3-D multiple-body viscous flows with arbitrary grid combinations, body shapes and relative motion, while the primary and subordinate bodies still influence each other aerodynamically (Abstract, §I). **Stated**
2. Chimera differs from other Schwarz-type overlapping decompositions because bodies cut holes in neighbouring subdomains. Each hole creates an artificial boundary that receives interpolated data, and this two-way link between a primary grid and a fully embedded subordinate grid is what makes moving multi-body computations possible (§I, Figs. 1–2). **Stated**
3. Any pair of subdomains can be linked one way through hole boundaries and conventional outer boundaries (§I). **Stated**
4. The flow algorithm, Eq. (2), depends on the Chimera machinery only through $i_b$: $i_b=1$ at field points, $i_b=0$ at hole points. It multiplies $h$, $\Delta t$ and the dissipation terms, so at hole points the scheme reduces to $\Delta\hat{\mathbf q}^n=0$, i.e. $\hat{\mathbf q}^{n+1}=\hat{\mathbf q}^n$ (§II ADF, Eq. 2). **Derived**
5. For moving bodies the hole and inter-grid boundary positions depend on time, so $i_b$ and the interpolation coefficients must be recomputed every step. This couples the ADF, DCF and BDF in a cycle (§II). **Stated**
6. Unmodified PEGASUS costs 1.96 times one ADF iteration for the wing–body separation and 5.27 times for the Shuttle SRB separation (Table 1). **Shown**
7. In static PEGASUS applications, hole definition is usually the most time-consuming task (§II DCF). **Stated**
8. The DCF limits the search for level-$(n+1)$ hole points to the points on either side of the level-$n$ hole boundaries. The DCF/ADF ratio falls to 0.64 and 2.02, "a factor of ∼3" (§II DCF, Table 1); the ratios are 3.06 and 2.61 *(compiler check, not in the sources)*. **Shown**
9. The restricted search bounds how far a hole may move in one step: a hole point must never become a field point without first being updated by interpolation as a hole-boundary point, or undefined values enter the field computation (§II DCF, Fig. 3, 1-D illustration). **Derived**
10. In every time-accurate moving-body case examined so far, the time step needed to resolve the physics was much smaller than the limit set by the DCF search restriction (§II DCF). **Stated**
11. The DCF/ADF ratio depends on the problem, because the DCF cost depends on the subdomain configuration and some key DCF routines do not vectorize (§II DCF). **Stated**
12. The original VAPOR code neglected the time-metric terms $\xi_t,\eta_t,\zeta_t$; the ADF includes them (§III). **Stated**
13. Constant plunge of a NACA 64A010 at $M_\infty=0.8$, equivalent to $1^\circ$ incidence, run quasi-3-D: agreement with Magnus is good, but the weak lower-surface shock is diffused on the coarse grid (§III, Fig. 4). **Shown**
14. Sinusoidal plunge, $\pm1^\circ$, $k_{\mathrm r}=0.4$, $M_\infty=0.8$: $C_l$ over the 4th cycle shows "excellent agreement" with Magnus (§III, Fig. 5). **Shown**
15. AFATL wing alone, $M_\infty=1.05$, $\alpha=2^\circ$, $Re=2.4\times10^6$/ft: the computed $C_p$ agrees well with AEDC 4T data (§III, Figs. 7–8). **Shown**
16. Wing plus store on two overset grids, without pylon or sting: good agreement on the wing upper surface. Differences on the lower surface and on the body are attributed to the missing pylon and sting (§III, Figs. 7, 9, 10). **Shown**
17. The wing–store decomposition has three inter-grid boundaries: the wing hole in the body grid, the body hole in the wing grid, and the body-grid outer boundary. The wing outer boundary is at free stream, 10 chords away (§III). **Stated**
18. Store separation with a prescribed trajectory: the store is pinned at the tail, and its nose sweeps one body diameter of arc downward in 500 steps (150 ms) (§III, Plate 1). **Shown**
19. Shuttle SRB separation: 3 grids, about 350,000 points (357,330 in Table 1), 8 inter-grid boundaries (2 outer, 6 hole), $M_\infty=4.5$, $\alpha=2^\circ$, $Re=6.95\times10^6$ on orbiter length, $\Delta t=1.36\times10^{-3}$ s, 500 steps over the first characteristic interval. SRB bow shocks interact with the orbiter bow shock and impinge on the external tank and orbiter (§III, Fig. 11, Plate 2). **Shown**
20. Table 1: wing–body, 2 domains, 243,906 points, 2,090 interpolated boundary points; Shuttle, 3 domains, 357,330 points, 10,408 interpolated boundary points (Table 1). **Stated**
21. The effect of multiple subdomains and of the present inter-grid boundary updating on time accuracy has not been addressed. The BDF, hardwired for prescribed trajectories, is the "weak link" (§IV). **Stated**
22. The ADF predicts lift and moments accurately. Accurate drag for 3-D separated flow is out of reach, so a trajectory model must be built from what CFD can supply (§II BDF). **Stated**
23. Whether time-accurate Navier–Stokes simulation is needed for bodies in relative motion is debated. The authors expect quasi-steady calculations to suffice in some cases and fully unsteady methods to be needed in "pathological" ones (§IV). **Stated**

# Printed slips

- Time metrics (p. 647), printed "$\xi_t=x_t\xi_x-y_t\xi_y-z_t\xi_z=0$", and likewise for $\eta_t$ and $\zeta_t$. The identity $\xi_t=-\mathbf u_g\cdot\nabla\xi$ gives the same sign to all three terms, $\xi_t=-x_t\xi_x-y_t\xi_y-z_t\xi_z$ *(compiler check, not in the sources)*. The printed right-hand sides ($0$, $0$, $-M_\infty\sin(\pi/180)$) are given directly and are unaffected.
- Eq. (1) (p. 644): $\hat Q=[\rho,\rho u,\rho v,\rho w,e]^T$ is printed without the factor $J^{-1}$ that $\hat F,\hat G,\hat H$ carry, so the strong-conservation form is inconsistently scaled as printed.
- p. 644: "forward spacial difference operators $\delta^b_\xi$ and $\delta^f_\xi$". Eq. (2) applies $\delta^b_\xi$ to $\hat F^+$ and $\delta^f_\xi$ to $\hat F^-$, so one of them is backward; "spacial" is misspelled.
- p. 646: one sentence says the time steps that resolve the physics "are generally much smaller than the time-step limits imposed by the DCF search restriction". Its restatement says "the time-step size limitation imposed by the DCF search limits are generally much less than those required to accurately resolve the physical processes", which literally says the opposite.
- Ref. [9]: "AIAA Paper No. 86-2179, Aug. 1989". The paper number belongs to the 1986 series, and Crossref dates the paper 1986.

# Notation map

| Meakin & Suhs (1989) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tau$ | $t$ | time |
| $\xi,\eta,\zeta$ | $\boldsymbol\xi$ | $\xi$ upwinded, $\eta,\zeta$ central; $\zeta$ thin-layer direction |
| $\hat Q=[\rho,\rho u,\rho v,\rho w,e]^T$ | $\hat{\mathbf q}=\mathbf q/J$ | printed without $J^{-1}$ (slip) |
| $e$ | $E$ | total energy per unit volume; registry $e$ is the error |
| $\hat F,\hat G,\hat H$, $\hat S$ | $\hat{\mathbf F},\hat{\mathbf G},\hat{\mathbf H}$; viscous flux page-local | agree up to bold |
| $U,V,W$ | $U,V,W$ | unscaled contravariant velocities, agree |
| $J^{-1}$ | $J^{-1}$ | cell volume, "defined in the usual way" |
| $\xi_t,\eta_t,\zeta_t$ | $\xi_t,\eta_t,\zeta_t$ | $\xi_t=-\mathbf u_g\cdot\nabla\xi$ |
| $i_b$ (1 field, 0 hole) | 0/1 mask $i_b$, translated to $\iota$ | interpolated boundary points get no distinct value; $\iota=-k'$ in the registry |
| conventional field / hole / interpolated (hole) boundary points | $\mathcal D_k$ / $\mathcal H_k$ / $\mathcal R_k$ | |
| primary / subordinate grid | parent / embedded grid | |
| ADF, BDF, DCF | flow solver, 6-DOF body dynamics, domain connectivity | names kept on pages |
| $h$ ($\Delta t$ or $\Delta t/2$) | page-local | **collision**: registry $h$ is a spacing |
| $\delta$, $\bar\delta$, $\delta^b_\xi$, $\delta^f_\xi$ | $D_{0m}$-type central, midpoint, $D_{-m}$, $D_{+m}$ one-sided | |
| $D_e$, $D_i$ | page-local | explicit and implicit dissipation |
| $\tilde K$ | $k_{\mathrm r}$ | reduced frequency, reference length $L$ (not defined) |
| $\tilde t$, $\tilde t_p$, $\tilde\psi$, $a_o$, $L$ | page-local; $a$ for $a_o$ | |
| $M_\infty$, $Re$, $\alpha$ | $M_\infty$, $Re$, $\alpha$ | agree |

# Reference list

The paper prints 15 numbered references ([1]–[15], in order of citation),
merged complete into the [bibliography](/bibliography.md) with `citedby`
including this slug. Ref. [9] (AIAA Paper 86-2179) is printed with the date
"Aug. 1989". It is merged under the year of its paper number (1986), as
verified on Crossref, and the printed date is noted. Ref. [4] is a chapter of
*Advances in Grid Generation*, ASME FED-Vol. 5 (1983), with no pages printed.
Ref. [14] has no paper number. No DOIs are printed, and there are no printed
duplicates.

# Pages created or updated

Chunk 1 (2026-11-02). This source is cited on:

- [Wing–pylon–store separation and related moving-body cases](/benchmarks/store-separation.md)
- [Domain connectivity and overset grid assembly](/definitions/domain-connectivity.md)
- [Fringe (receptor) points and overlap width](/definitions/fringe-point.md)
- [Grid hierarchy and priority](/definitions/grid-hierarchy.md)
- [Orphan points](/definitions/orphan-point.md)
- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Point classification and the iblank mask](/definitions/point-classification.md)
- [Donor search](/methods/donor-search.md)
- [Hole cutting](/methods/hole-cutting.md)
- [Implicit hole cutting](/methods/implicit-hole-cutting.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Moving overset grids](/methods/moving-overset-grid.md)
- [DCF and DCF3D (Meakin's domain connectivity function and code)](/software/dcf3d.md)
- [PEGASUS (PEGSUS) versions 1–4](/software/pegasus.md)

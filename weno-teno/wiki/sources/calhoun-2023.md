---
type: Source
title: "Calhoun et al. (2023) — The Cartesian Grid Active Flux Method with Adaptive Mesh Refinement"
description: "First implementation of the third-order Cartesian Active Flux method on quadtree patch-based adaptive meshes in ForestClaw: conservative coarse–fine transfer of averages and point values, subcycling without time interpolation, refluxing, and constant-state-preserving variants for variable-velocity transport, with third-order convergence on AMR grids."
resource: "doi:10.1007/s10915-023-02106-8"
source_kind: paper
authors: [Calhoun D., Chudzik E., Helzel C.]
year: 2023
venue: "J. Sci. Comput. 94:54"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Journal_of_Scientific_Computing_Calhoun_The_Cartesian_Grid_Active_Flux_Method_with_Adaptive_Mesh_Ref.pdf"
tags: [active-flux, amr, finite-volume, free-stream-preservation, software]
timestamp: 2026-10-23T20:00:00Z
---

# Summary

Calhoun, Chudzik & Helzel present what they call the first implementation of the
[Active Flux](/methods/active-flux.md) (AF) method on adaptively refined Cartesian grids. AF is
a third-order finite-volume method. Its degrees of freedom are cell averages plus point values
at cell corners and edge midpoints, shared between neighbouring cells. On each cell a
biquadratic polynomial interpolates the eight boundary values and matches the average. The
flux is a $3\times3$ Simpson rule in space along the edge and in time. The point values at
later times come from an evolution operator applied to the continuous piecewise-biquadratic
reconstruction: exact for advection and acoustics, iterative for Burgers' equation.

The method is built into ForestClaw, a quadtree patch-based
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md) code on p4est with fixed-size
patches and 2:1 balance. Coarse-to-fine transfer evaluates the coarse reconstruction at the
fine point-value locations and computes fine averages by Simpson's rule. Simpson's rule is
exact for the reconstruction, so the transfer is conservative. Fine-to-coarse averages the
fine averages and copies vertex values. Subcycling uses no time interpolation of coarse ghost
data: two ghost layers are reconstructed and the first is advanced with the interior.
Berger–Colella refluxing keeps conservation at coarse–fine interfaces.

For [solid-body rotation](/benchmarks/solid-body-rotation.md) and a time-dependent swirl,
new AF variants preserve constant states (Remark 4.1, Theorem 4.2): the swirl velocities are
discrete stream-function differences and the flux freezes the velocity at the edge midpoint.
Corollary 4.3 extends this to AMR with global time stepping but not with subcycling
([free-stream preservation](/properties/free-stream-preservation.md)). The tests (smoothed-disc
advection, rotation, swirl, 2D [Burgers](/benchmarks/burgers-equation-tests.md), acoustics, a
stationary vortex) show third-order convergence on AMR grids. Solution-following refinement
matches the uniform grid at the finest level. The stationarity preservation of Barsukow's
acoustic operator, a [well-balancing](/properties/well-balancing.md)-type property, does not
carry over: with AMR that operator is unstable.

# Version read

arXiv preprint 2205.07572v2 [math.NA], stamped 7 Jun 2022, 24 pages; not the version of
record (no journal typesetting, no DOI printed), which appeared as J. Sci. Comput. 94, article
54 (2023). Title and authors on page 1 match Crossref. On p. 7 an embedded image of another
document's page leaks text into the extraction; that page was read visually. Equation, table
and figure numbers are those of arXiv v2.

# Key claims

Registry notation: $u$ the conserved variable, $\bar u_{i,j}$ the average of cell $(i,j)$,
$u_{i\pm1/2,j}$, $u_{i,j\pm1/2}$ edge-midpoint and $u_{i\pm1/2,j\pm1/2}$ corner point values,
$\hat f_{i+1/2,j}$, $\hat g_{i,j+1/2}$ the space–time averaged fluxes, $(v_1,v_2)$ the
advection velocity, $\Psi$ a page-local stream function, $\ell$ the refinement level.

1. AF is a third-order finite-volume method with point values and cell averages as degrees of freedom and a compact stencil in space and time (Abstract, §1). **Stated**
2. This is the first implementation of AF on adaptively refined Cartesian grids (Abstract). **Stated** (priority claim)
3. On 2D Cartesian grids AF has four degrees of freedom per cell: one average and three point values, $u_{i-1/2,j}$, $u_{i-1/2,j-1/2}$, $u_{i,j-1/2}$ (§2, p. 3). **Stated**
4. The numerical flux is a $3\times3$ Simpson rule with weights $\frac1{36}(1,4,1)\otimes(1,4,1)$ on the edge endpoints and midpoint at $t^n$, $t^{n+1/2}$, $t^{n+1}$ (Eq. (2)). **Stated** (Eymann–Roe)
5. For 2D advection the characteristic tracing needs $\nu=\max(\lvert v_1\rvert\Delta t/\Delta x,\lvert v_2\rvert\Delta t/\Delta y)\le1$ (Eq. (6)), but linear stability is stricter; the authors use $\nu\le0.75$ (§2.1, citing Helzel et al.). **Stated**
6. For 2D acoustics, $\max(c\Delta t/\Delta x,c\Delta t/\Delta y)\le\frac12$ (Eq. (15)) is necessary and, by Helzel et al., sufficient for linear stability on a regular Cartesian grid (§2.3). **Stated**
7. For Burgers' equation the fixed-point iteration (10) gains one order per iteration; two iterations from a first-order guess give third order, the most the quadratic reconstruction allows (§2.2). **Stated**
8. The pointwise guess $u^{n+1/2,(0)}=u^{n+1,(0)}=u^n$ at the same location is unstable where the characteristic speed changes sign; a guess from means of the neighbouring cell averages is stable (§2.2, citing Helzel et al.). **Stated**
9. Coarse-to-fine transfer by Simpson's rule on the coarse reconstruction gives fine averages that sum exactly to the coarse average, because Simpson's rule is exact for the biquadratic reconstruction; this is needed for conservation (§3.1). **Derived**
10. In AF subcycling, ghost cells at intermediate time levels are not filled by time interpolation from coarser grids, unlike Berger–Oliger–Colella. Two ghost layers are reconstructed and the first is advanced with the interior; at synchronized time levels the ghost data are replaced by averaged or interpolated data from neighbours (§3.2, Fig. 6). **Stated**
11. Global conservation at coarse–fine interfaces is enforced by the Berger–Colella fix: coarse and fine cells are updated with the fine-grid fluxes (§3.2). **Stated**
12. Smoothed-disc advection, $(v_1,v_2)=(1,0.5)$, CFL 0.6, $t=1$, $L^1$ errors (Table 1, §4.1): uniform levels 4/5, $6.46\times10^{-5}$ and $8.45\times10^{-6}$ (EOC 2.9347); diagonal AMR 4–5/5–6, $5.08\times10^{-5}$ and $6.61\times10^{-6}$ (2.9414); uniform 5/6, $8.45\times10^{-6}$ and $1.07\times10^{-6}$ (2.9865); solution-following AMR 3–5/3–6, $8.47\times10^{-6}$ and $1.07\times10^{-6}$ (2.9849). Solution-following AMR matches the finest uniform grid, diagonal AMR the coarser one. **Shown**
13. Solid-body rotation at $t=2$ (Table 2): with the exact-characteristics flux, uniform 6/7 gives $4.60\times10^{-6}$ and $5.83\times10^{-7}$ (EOC 2.9807) and AMR 3–6/3–7 gives $4.67\times10^{-6}$ and $5.92\times10^{-7}$ (2.9801). With the general flux of Eq. (26), uniform gives $5.79\times10^{-6}$ and $7.35\times10^{-7}$ (2.9786) and AMR the same errors (2.9781). **Shown**
14. Remark 4.1: the AF method for solid-body rotation preserves constant states on regular Cartesian grids, because the $x$-fluxes of a constant depend only on $y$ and the $y$-fluxes only on $x$. **Proved**
15. Theorem 4.2: AF with the fluxes (27)–(28) and velocities from the stream-function differences (25) preserves constant states of (24) on regular Cartesian grids. **Proved**
16. Corollary 4.3: the method preserves constant states on Cartesian AMR grids with global time stepping, since the coarse flux equals the mean of the two fine fluxes and reduces to the regular-grid flux (p. 16). **Proved**
17. With subcycling, the fine-flux sum contains intermediate-time contributions that no coarse flux balances, so constant states are not exactly preserved. Constant data at $t=1$ on diagonal levels 3–4 have error $10^{-13}$ with subcycling against about $10^{-16}$ without (pp. 16–17). **Derived** and **Shown**
18. Smooth swirl (two Gaussians), $t=1$ (Table 3): with subcycling, uniform 4/5 gives $5.72\times10^{-6}$ and $7.27\times10^{-7}$ (EOC 2.9771) and AMR 3–4/3–5 gives $5.76\times10^{-6}$ and $7.35\times10^{-7}$ (2.9705). Without subcycling, AMR 3–4/3–5 gives $5.72\times10^{-6}$ and $7.31\times10^{-7}$ (2.9703). Subcycling does not significantly change the accuracy. **Shown**
19. 2D Burgers with sine data reaches third order at $t=0.05$ with diagonal refinement, CFL $\le0.5$, subcycling and the conservative fix; the result is "not shown here" (§4.4). **Stated**
20. Unlimited AF oscillates along the curve where the characteristic speed changes sign; the bound-preserving limiter of Helzel et al. removes the oscillations (§4.4, Fig. 12). **Shown** (qualitative)
21. Acoustics convergence test of Lukáčová et al., $t=1$, CFL $\le0.4$ (Table 4): uniform levels 2/3 give $p$ errors $2.23\times10^{-4}$ and $2.79\times10^{-5}$ (EOC 2.9975) and $v$ errors $2.52\times10^{-5}$ and $2.65\times10^{-6}$ (3.2509). AMR 2–3/3–4 gives $p$ errors $1.64\times10^{-4}$ and $2.06\times10^{-5}$ (printed EOC 3.1045) and $v$ errors $3.33\times10^{-5}$ and $3.87\times10^{-6}$ (printed EOC 2.8564). AMR accuracy is comparable with the coarser uniform grid. **Shown** (the AMR-row EOCs do not follow from the printed errors; see Printed slips)
22. High-frequency acoustic wave on AMR levels 3–6, refining where $\lvert p_{\max}-p_{\min}\rvert\ge0.001$: no visible spurious grid effects, apart from smearing caused by the domain boundary (§4.5.2, Figs. 14–15). **Shown** (qualitative)
23. The AF method used here, with the Eymann–Roe acoustic operator, is not stationarity preserving; with third order and AMR the stationary vortex is still accurate at $t=100$ (§4.6, Fig. 16). **Shown** (qualitative)
24. With the stationarity-preserving operator of Barsukow et al., steady states are preserved on a regular Cartesian grid, but the solver becomes unstable with AMR (§4.6, Conclusions). **Shown** (observation, no figure)
25. Barsukow showed that the 2D Cartesian AF for acoustics with the exact evolution operator is stationarity preserving: it adds no dissipation to discrete representations of all stationary states (§1). **Stated** (cited)

# Printed slips

- Table 4, AMR rows: the printed EOCs (3.1045 for $p$, 2.8564 for $v$) do not follow from the printed errors. *(compiler check, not in the sources)*: $\log_2(1.64\times10^{-4}/2.06\times10^{-5})=2.993$ and $\log_2(3.33\times10^{-5}/3.87\times10^{-6})=3.105$. The printed $p$ value matches the $v$ ratio, and no pairing of the printed errors gives 2.8564. The uniform-row EOCs agree with the printed errors (2.999, 3.249) within rounding.
- Proof of Theorem 4.2 (p. 15): the last term of the $\Psi$ bracket is printed as $\Psi(x_{i-1/2},y_{j+1/2},t^n)$. *(compiler check, not in the sources)*: from Eq. (25), $v_2(x_i,y_{j+1/2})-v_2(x_i,y_{j-1/2})=\frac1{\Delta x}\big[\Psi(x_{i+1/2},y_{j+1/2})-\Psi(x_{i-1/2},y_{j+1/2})-\Psi(x_{i+1/2},y_{j-1/2})+\Psi(x_{i-1/2},y_{j-1/2})\big]$, so the last term is at $y_{j-1/2}$; the cancellation, and the theorem, are unaffected.
- Burgers refinement criterion (p. 18): printed $\frac{q_{i,j+1}-q_{i,j+1}}{2\Delta y}\ge15$, identically zero, for $q_{i,j+1}-q_{i,j-1}$; printed without absolute values.
- Eq. (31): an unbalanced parenthesis in $p(x,y,0)=-\frac1c((\sin(2\pi x)+\sin(2\pi y))$.
- §4.2: the text measures the error "after a half rotation", while the Table 2 caption gives $t=2$, one full rotation for the stated period 2.
- Corollary 4.3: "global time stepping (e.g. no subcycling)" for "i.e.".
- Ref. [4] (Berger & Colella) prints "82:484–512, 1984", the same year and pages as ref. [3] (Berger & Oliger, 53:484–512, 1984).
- Typo: "the the accuracy" (§4.5.1).

# Notation map

| Calhoun et al. 2023 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $q$ | $u$ | conserved variable, $\mathbb R^s$-valued; **collision** with the weight exponent $q$ |
| $f$, $g$ | $f$, $g$ | $x$- and $y$-fluxes; agree |
| $Q^n_{i,j}$ | $\bar u^n_{i,j}$ | cell average |
| $Q^n_{i\pm1/2,j}$, $Q^n_{i,j\pm1/2}$, $Q^n_{i\pm1/2,j\pm1/2}$ | $u_{i\pm1/2,j}$, $u_{i,j\pm1/2}$, $u_{i\pm1/2,j\pm1/2}$ (page-local) | shared point values; the source uses one letter $Q$ for averages and point values |
| $F_{i+1/2,j}$, $G_{i,j+1/2}$ | $\hat f_{i+1/2,j}$, $\hat g_{i,j+1/2}$ | Simpson $3\times3$ space–time fluxes |
| $q^{rec}(\xi,\eta)$, $c_{ij}$; $q^n$ | biquadratic reconstruction and its coefficients; global reconstruction (page-local) | reference cell $[-1,1]^2$; **collision**: $\xi$ DG nodes, $\eta$ entropy |
| $a$, $b$ | $v_1$, $v_2$ | advection velocity; **collision** with the wave speed $a$ |
| CFL | $\nu$ | 0.75 advection, 0.5 acoustics |
| $\ell$ | iteration index (Burgers) and refinement level | reused in the source |
| $p$, $u=(u,v)$, $c$ | $p$, $v$, $c$ | acoustic pressure, velocity, sound speed |
| $w=\nabla\times u$ | vorticity | |
| $M_R\{f\}$, $R=ct$ | weighted mean over a disc of radius $ct$ (page-local) | called a "spherical mean"; **collisions** with $M$ (mass matrix) and $R$ (eigenvectors) |
| $\Psi$ | $\Psi$ (page-local) | stream function, as on the Active Flux page |
| $\Delta t_\ell$, $\Delta x_\ell$ | step and spacing on level $\ell$ | $\Delta t_{\ell+1}=\Delta t_\ell/2$ |
| $H(r)$ | smoothed Heaviside $(\tanh(r/0.02)+1)/2$ | |
| EOC | observed order | $\log_2$ of successive $L^1$ error ratios |
| level $k$, $k$–$m$ | uniform grid at level $k$; AMR with levels $k$ to $m$ | $16\times16$ patches |

# Reference list

The arXiv v2 prints 21 references, numbered [1]–[21]. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` including `calhoun-2023`. [8] is the undated
ForestClaw web page; the citing year would give it this paper's own key, so it is keyed as a
distinct work. [1] (Barsukow 2020, stationarity preservation of AF) shares its author–year
key with a different, already recorded Barsukow & Berberich work, and [11]/[12] (Eymann & Roe
2011) take suffixes in printed order against an existing entry. Both are resolved by title at
the merge. [4] prints the year and pages of [3] (see Printed slips). [1] has no volume or pages,
[6] is a chapter in a volume numbered 25, [21] (AMReX) has no page or article number, and [9]
is an arXiv preprint (2017) kept as its own entry. No item is unparseable.

# Pages created or updated

Chunk 6 (2026-10-23), cited further in chunks 7–8 (2026-10-23). This source is cited on:

* [Active Flux](/methods/active-flux.md)
* [Block-structured adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [ForestClaw](/software/forestclaw.md)
* [Free-stream preservation](/properties/free-stream-preservation.md)
* [Solid-body rotation](/benchmarks/solid-body-rotation.md)
* [Well-balancing](/properties/well-balancing.md)

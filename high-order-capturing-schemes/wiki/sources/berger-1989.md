---
type: Source
title: "Berger & Colella (1989) — Local Adaptive Mesh Refinement for Shock Hydrodynamics"
description: "The block-structured AMR algorithm for 2D conservation laws: properly nested, grid-aligned rectangular patches refined by an even ratio in space and time, coupled conservatively by averaging down and a flux-register correction of the coarse cells next to fine grids, with bilinear-in-space and linear-in-time ghost interpolation, Richardson-extrapolation error estimation, bisection-and-merge clustering, an unchanged second-order Godunov integrator, a warning about strong shocks crossing grid interfaces, and oblique shock reflection tests with a timing breakdown."
resource: "doi:10.1016/0021-9991(89)90035-1"
source_kind: paper
authors: [Berger M.J., Colella P.]
year: 1989
venue: "J. Comput. Phys. 82:64-84"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1989-JCP-Berger.pdf"
tags: [amr, finite-volume, godunov, euler, mach-reflection, refluxing]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper that later block-structured AMR codes call "Berger–Colella".
Refined regions are a few logically rectangular patches whose edges lie
on coarse-grid lines; unlike Berger & Oliger's earlier algorithm, patches
are not rotated, which "greatly simplifies the maintenance of
conservation". Patches are properly nested and refined in time by the
same even ratio $r_{\mathrm{AMR}}$ as in space (subcycling). Two fix-ups
keep the hierarchy conservative: coarse cells under a fine grid are
replaced by the average of the fine cells, and coarse cells next to a fine
grid have their coarse flux replaced by the space–time sum of fine fluxes,
through a flux register applied as a correction pass. Fine-grid ghost
values come from same-level neighbours, otherwise from bilinear (space)
and linear (time) interpolation of coarser data. New grids come from
Richardson-extrapolation error estimates, a buffer zone and
bisection-plus-merging clustering. The integrator, a second-order Godunov
method, is used unchanged. The paper warns that strong captured shocks
crossing a coarse–fine interface emit $O(1)$ spurious waves. Tests are
oblique shock reflections on a Cray X-MP, with a timing table and an
estimated factor of 8 in CPU over a uniform grid. Everything is second
order: the paper bears on this bundle as the baseline that
[high-order AMR](/methods/high-order-amr.md) extends.

# Key claims

1. **Design choices** (§1). For unsteady flow with shocks, "maintaining
   global conservation form is a primary consideration". Patch boundaries
   "coinciding with the grid lines of the underlying coarse mesh" make
   conservation simpler than rotated subgrids. The integrator is separate
   from the adaptive strategy, so "an off-the-shelf integrator can be used
   without modification". The aim is fixed accuracy at minimum cost.
   Godunov-type schemes are argued to give more resolution per cost than
   Lax–Wendroff, citing [Woodward & Colella (1984)](/sources/woodward-1984.md).
2. **Equations** (§1). 2D Euler in conservation form,
   $\partial_t u + \partial_x f(u) + \partial_y g(u) = 0$, with
   $u = (\rho, \rho\mathbf v, E)$ and the ideal-gas pressure. "All the
   algorithms extend to three dimensions."
3. **Hierarchy** (§2, Fig. 2.1). Levels from 1 (coarsest, the whole domain)
   to the finest, each the union of rectangular patches with one spacing.
   Same-level patches align with one global discretization and may
   overlap; the discrete solution must not depend on how a level is split
   into rectangles. General quadrilateral meshes are possible but not
   used.
4. **Proper nesting** (§2). (i) A fine patch starts and ends at the corner
   of a cell of the next coarser level; (ii) at least one level-$(l-1)$
   cell separates a level-$l$ cell from a level-$(l-2)$ cell in the four
   coordinate directions, except at the physical boundary. A fine patch may
   span several coarser patches.
5. **Subcycling** (§2). The same ratio in time and space,
   $\Delta t_l/h_l$ equal on all levels, so one explicit scheme is stable
   everywhere and the finest step is not imposed globally. **Only even
   refinement ratios** are allowed, to simplify the error estimator. The
   solution at a point is that of the finest grid containing it.
6. **Ordering** (§3, eq. 1). The base scheme is the cell-centred
   conservative update with directional fluxes
   $(\hat f_x)_{i\pm1/2,j}$, $(\hat f_y)_{i,j\pm1/2}$. Each patch is advanced
   independently except for boundary values, and "before advancing a grid
   to time $t + \Delta t$, all the finer level grids have been integrated
   to time $t$": coarse first, then the finer levels catch up.
7. **Averaging down** (§3, Fig. 3.1). After each coarse step a covered
   coarse cell becomes the average of its $r_{\mathrm{AMR}}^2$ fine cells.
   This is equivalent, to round-off, to redefining the coarse fluxes around
   that cell as time sums of fine fluxes, without storing fluxes.
8. **Flux correction** (§3, eqs. 2–5, Fig. 3.2). "The fluxes into the fine
   grid across a coarse/fine cell boundary must equal the flux out of the
   coarse cell" (crediting Osher & Sanders). For a coarse cell whose face
   at $x_{i+1/2}$ borders a fine grid, the coarse flux through that face
   is replaced by the fine fluxes through its $r_{\mathrm{AMR}}$ fine
   faces, summed over the $r_{\mathrm{AMR}}$ fine steps and divided by
   $r_{\mathrm{AMR}}^2$ (eq. 2, coarse $h_x$, $h_y$ and coarse step). It is
   implemented as a flux register per fine grid: set to minus the coarse
   flux (eq. 3); after each fine step add $1/r_{\mathrm{AMR}}^2$ times the
   sum of the fine fluxes over the fine faces (eq. 4); after $r_{\mathrm{AMR}}$
   fine steps add $\Delta t_{\mathrm{coarse}}/h_{x}$ times the register to the
   uncovered coarse neighbour, with a minus sign on the other side
   (eq. 5). With overlapping fine grids each coarse edge is updated once (a
   marker array), so the result does not depend on grid order. Cost about
   0.3 % of a run. The word "refluxing" is not used: the paper calls this a
   correction pass, a "fix up" step that keeps the integrator separate from
   the hierarchy.
9. **Ghost values** (§4). For a stencil with a given number of points per
   side, the AMR code supplies a border of that width. Values come from
   adjacent same-level grids where available, "otherwise ... bilinear
   interpolation from coarser level solution values. If necessary, we also
   interpolate linearly in time." This runs on rectangular boundary patches:
   gather coarser data on a slightly larger patch (recursively if needed),
   interpolate, then overwrite with same-level fine data where it exists.
   The interpolation is second order; no limiter and no conservation
   constraint are stated. A first point-by-point version took 40 % of the
   run time. The interpolation that initializes new fine grids is not
   specified.
10. **Regridding** (§5). Recursive from the finest level down; at most one
    new level per regrid (several at the initial time). Steps: a buffer of
    flagged neighbours ("two cells in each direction is typical") so that
    features stay inside the fine grid until the next regrid; flags added
    and removed to keep proper nesting; clustering; subdivision of grids
    not properly contained in the base grids.
11. **Clustering** (§5). One rectangle around all flagged cells; if its
    efficiency (flagged over total cells) is below an input minimum, e.g.
    60 %, bisect the long side and repeat; then merge pairs when the merged
    grid costs less, the cost of an $m\times n$ patch being taken
    proportional to $mn + m + n$ ($m$, $n$ here patch sizes, not registry
    symbols). Grid generation is about 1.7 % of the CPU time.
12. **Richardson-extrapolation error estimate** (§6). For a scheme of a
    given order in space and time, two steps on the grid minus one step
    of twice the size on the grid coarsened by 2, divided by $2$ raised to
    (order + 1), minus 2, equals the local truncation error up to terms one
    order higher. Implemented on a virtual grid coarsened by 2; all four
    fine cells are flagged where the difference exceeds a tolerance. It
    needs only the order, not the scheme or the PDE.
13. **Its failure at discontinuities** (§6). The estimate always flags
    captured discontinuities, because there the pointwise difference does
    not shrink with $h$. Shocks need no refinement as such (they spread
    over a fixed number of zones), but contacts and other linearly
    degenerate discontinuities do, since they widen in time. A
    "distributional" error measure is suggested, not implemented.
14. **Strong shocks crossing an interface** (§6, Figs. 6.1–6.2). Near a
    shock, captured fluxes differ by $O(1)$ from exact fluxes. On a uniform
    grid these errors cancel in the time integral; at a coarse–fine
    interface the two grids' errors differ, and $O(1)$ spurious waves enter
    the post-shock state, with an amplitude observed to scale with the jump
    in the characteristic quantities across the shock. Weak shocks are
    acceptable; strong shocks "must be refined everywhere, if they are to be
    refined anywhere". Recommended: ignore the truncation-error estimate
    near shocks weaker than a threshold, or use knowledge of the flow
    (ignore it behind the incident shock).
15. **Integrator** (§§1, 5, 7). "a second-order Godunov method" by Colella
    (LBL-17023), needing five 2D scratch arrays plus four for the conserved
    quantities, and special slope calculations only for boundary fluxes.
    Whether it is split or unsplit is not stated.
16. **Efficiency** (§7, Tables I–II). Cray X-MP/22, 5674 s CPU. Table I:
    grid integration 78.29 %, interpolation 12.95 %, output 2.87 %, grid
    updates 2.78 %, grid generation 1.71 %, memory management 0.59 %; error
    estimation integrates at 3 % of the integration cost. Table II cell
    updates: level 1 $2.98\times10^5$, level 2 $4.59\times10^6$, level 3
    $1.13\times10^8$, error estimation $3.06\times10^6$; over 90 % of
    integrated cells are on the finest level. The finest grids cover about
    10 % of the domain, so a uniform grid would need "a factor of 8 more CPU
    time". Memory: about $4.5\times10^6$ words uniform against at most
    $8.94\times10^5$ for AMR; even with four full arrays, $2.0\times10^6$,
    "a factor of 2.2 larger".
17. **Conclusions** (§8). About 3000 lines of Fortran without the
    integrator; reused with FLO52 and a combustion induction-time model;
    already combined with conservative front tracking to track the strong
    incident shock so that no strong captured shock crosses a grid
    boundary. Implicit schemes on embedded grids for time-dependent
    problems are called a major open question.

# Tests

* **Strong shock through a forced grid boundary** (§6, Figs. 6.1–6.2).
  Refinement is forbidden above a certain height, so a Mach 10 incident
  shock passes from a fine grid into the coarse one; contours and a
  density profile just below the interface show the oscillations.
  Qualitative only.
* **Oblique shock reflection, $M_s = 10$, $\theta_{\mathrm w} = 30°$,
  $\gamma = 1.4$** (§7, Fig. 7.1). The angle is between the shock's
  direction of propagation and the reflecting surface. Domain
  $2.0\times0.4$, coarse $h = 0.02$, 149 coarse steps, error estimated every
  other step, buffer one cell, grid efficiency 65 %, tolerance 0.02 on the
  density truncation error (no tagging beyond a set distance behind the
  incident shock), $r_{\mathrm{AMR}} = 4$, three levels (finest
  $h = 0.00125$, uniform equivalent $1600\times320$), 4 times finer per
  direction than the finest run of Woodward & Colella. Result: a
  Kelvin–Helmholtz roll-up of the principal slip line, which is not
  self-similar, formed where the weak shock from the second triple point
  meets it and carried into the roll-up at the tip of the wall jet. The
  timings above are from this run. The frame, boundary conditions and
  initial shock position are not printed.
* **Oblique shock reflection, $M_s = 8$, $\theta_{\mathrm w} = 35°$,
  $\gamma = 1.107$** (§7, Fig. 7.2). Seven Mach triple points in the
  double-Mach region, including a third along the top shock. Not fully
  resolved at $t = 0.115$, adequately at $t = 0.230$, which by the flow's
  self-similarity is a higher effective resolution. Uniform-grid runs of
  Colella & Glaz were not fully resolved for $\gamma < 1.25$; this $\gamma$
  is called the resolution limit on the Cray X-MP.

# Notation map

| Berger & Colella (1989) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $f(u)$, $g(u)$ | $u$, the $x$ and $y$ components of $\mathbf f$ | |
| $u$, $v$ (velocity) | $\mathbf v$ | **collision** with the state $u$ |
| $\rho E$ | $E$ | paper $E$ is specific total energy; registry $E$ is the energy density |
| $u_{i,j}$ | $\bar u_{i,j}$ | cell average |
| $F_{i+1/2,j}$, $G_{i,j+1/2}$ | $(\hat f_x)_{i+1/2,j}$, $(\hat f_y)_{i,j+1/2}$ | numerical fluxes |
| $\Delta x$, $\Delta y$; $h$, $k$ (§6) | $h_x$, $h_y$; $h$, $\Delta t$ | |
| $r$ | $r_{\mathrm{AMR}}$ | **collision**: registry $r$ is the number of WENO candidate stencils |
| $l$, $l_{\max}$ | level index; $N_{\mathrm{lev}} = l_{\max} - 1$ | registry counts levels above the base |
| $G_{l,k}$, $G_l$ | words (patch $k$ of level $l$; level $l$) | no registry symbol; **collision** with the paper's own flux $G$ |
| $\delta F_{i+1/2,j}$ | words (flux register) | no registry symbol |
| $Q$, $Q_{2h}$ | words (one step on the grid; on the grid coarsened by 2) | no registry symbol |
| $q$ (order) | words | **collision**: registry $q$ is the weight power |
| $\tau$ (truncation error) | words | **collision**: registry $\tau$ is the WENO-Z global indicator |
| $d$ (stencil half-width) | words (ghost width) | |
| $M_s$, $\alpha$ | $M_s$, $\theta_{\mathrm w}$ | $\alpha$ is the angle between shock propagation and wall, the wedge angle of the equivalent geometry |

# Pages created or updated

* Updated [High-order adaptive mesh refinement for capturing schemes](/methods/high-order-amr.md) (batch-15 block: the primary algorithm, the flux register, ghost interpolation, error estimation, the strong-shock caveat, cost).
* Updated [AMReX and PeleC](/software/amrex.md) (batch-15 block: the multilevel step as the paper states it).
* Updated [Divergence-free reconstruction of face-centred magnetic fields](/methods/divergence-free-reconstruction.md) (batch-15 block: the face-flux original of the edge correction).
* Updated [Double Mach reflection](/benchmarks/double-mach-reflection.md) (batch-15 block: the AMR run of the same case).
* Updated [Regular and Mach reflection](/definitions/mach-reflection.md) (batch-15 block: seven triple points at $\gamma = 1.107$).
* Updated [Shu–Osher shock/entropy-wave interaction](/benchmarks/shu-osher-problem.md) (batch-15 block: what "Berger–Colella second-order interpolation" is in the paper).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/1989-JCP-Berger.pdf`.
   * **Version read.** The published journal version, a 21-page Academic
     Press scan with an OCR layer. Received 8 September 1987, revised
     20 May 1988; Courant Institute (Berger) and Lawrence Livermore
     (Colella).
   * **Identity.** doi:10.1016/0021-9991(89)90035-1, checked on Crossref:
     "Local adaptive mesh refinement for shock hydrodynamics", Berger M.J.,
     Colella P., J. Comput. Phys. 82(1):64–84, May 1989, in agreement with
     page 1. A first page printed as 67 by a later source is a misprint.
   * **How it was read.** Text layer for prose; pp. 3–7, 11–12, 15–17 and
     21 rendered and read from the page images for every equation, both
     tables and the reference list. Figures (contour plots) inspected at
     low resolution only; they carry no quantitative data.
   * **Recorded as printed.**
     - Eq. 2 keeps the coarse flux at $x_{i+1/2}$ and subtracts the fine sum
       in the position of the opposite face, while eqs. 3–5 correct cell
       $(i+1, j)$ through face $x_{i+1/2}$; reproduced in words, with the
       standard sign convention.
     - The left side of the averaging formula is printed with subscript
       $l,j$ (evidently $i,j$).
     - Fig. 7.1: the text gives $t = 1.20$, the caption $t = 0.12$; neither
       verified.
     - The first author is printed "Collela" in refs. 11 and 12; ref. 12,
       "Colella and Woodward, J. Comput. Phys. 59, 264 (1985)", carries the
       venue of Colella & Glaz.
   * **Reference list:** 22 entries, none with titles, all merged. Colella &
     Glaz's 9th ICNMFD paper is `colella-1985-c`; ref. 12 is merged into
     `colella-1985-b` (Colella & Glaz, by venue); Gropp, printed as vol. 4,
     into `gropp-1980` (vol. 1, same page); Bolstad's Stanford thesis is
     re-keyed `bolstad-1982` (dated June 1982, previously keyed by a citing
     year); Osher & Sanders is `osher-1983-b`; Winkler's Göttingen thesis is
     merged into `winkler-1976`, its identity with the MPI report marked
     unverified. Bibliography: 3122 entries.

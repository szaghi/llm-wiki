---
type: Source
title: "Berger & Colella (1989) — Local adaptive mesh refinement for shock hydrodynamics"
description: "The original conservative patch-based AMR for 2D shock hydrodynamics: properly nested, grid-aligned rectangular patches refined by one ratio in space and time, restriction plus a flux-register correction of the coarse cells next to fine grids, bilinear/linear-in-time ghost filling, Richardson truncation-error tagging with bisection-and-merge clustering, the O(1) error of strong shocks crossing coarse–fine interfaces, and a Cray X-MP cost breakdown (integration about 80 %, about 8 times cheaper than a uniform grid)."
resource: "doi:10.1016/0021-9991(89)90035-1"
source_kind: paper
authors: [Berger M.J., Colella P.]
year: 1989
venue: "J. Comput. Phys. 82:64–84"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/1989-JCP-Berger.pdf"
tags: [amr, conservation, performance, verification]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper turns the Berger–Oliger (1984) adaptive mesh refinement for
hyperbolic systems into a conservative, efficient tool for 2D shock
hydrodynamics. The mesh is a hierarchy of properly nested, logically
rectangular patches whose boundaries lie on the grid lines of the next
coarser level (Berger–Oliger allowed rotated patches), refined by one
ratio in space and time, so that each level takes $r_{\mathrm{ref}}$
steps per coarser step with one explicit scheme stable on all levels.
Conservation is kept by two operations: covered coarse cells are replaced
by the average of the fine cells, and the uncovered coarse cells next to
a fine grid are corrected with the space–time sum of the fine fluxes,
accumulated in a flux register stored per fine grid. Ghost values come
from same-level neighbours or else from bilinear interpolation in space
and linear interpolation in time from coarser levels. New grids are made
by Richardson-type truncation-error estimation, a buffer zone and a
bisection-and-merge clustering of flagged cells under an efficiency
threshold. The paper identifies the $O(1)$ error that a strong captured
shock emits when it crosses a coarse–fine interface, and gives a Cray
X-MP timing breakdown on oblique shock reflection: integration about
80 % of the run, AMR overhead about 20 %, about 8 times cheaper than an
equivalent uniform grid. The integrator is kept separate from the
adaptive strategy, so that "an off-the-shelf integrator can be used
without modification" (§1, §3). Merged into
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).

# Key claims

1. **Scope** (§1, p. 66). Systems $\partial_t u + \nabla\cdot\mathbf f(u) = 0$
   in 2D with boundary conditions; the Euler equations of an ideal gas.
   The work is 2D only; "all the algorithms extend to three dimensions".
2. **Differences from Berger & Oliger** (§1, p. 65): unsteady shocked
   flow, so "maintaining global conservation form is a primary
   consideration"; refined grids with "boundaries coinciding with the grid
   lines of the underlying coarse mesh", which "greatly simplifies the
   maintenance of conservation over the former approach, where the
   refined subgrids were allowed to be rotated"; efficiency on a
   supercomputer.
3. **Hierarchy** (§2, pp. 67–68). Levels from coarsest to finest (the
   paper counts the coarsest as level 1); each level is a union of
   rectangular grids that are all subsets of one discretization of the
   whole domain. **Grids on one level may overlap**, but the discrete
   solution must not depend on the decomposition into rectangles. The
   solution at a point is the value of the finest grid containing it.
4. **Proper nesting** (§2, p. 67): "(i) a fine grid starts and ends at the
   corner of a cell in the next coarser grid. (ii) There must be at least
   one level $l-1$ cell in some level $l-1$ grid separating a grid cell at
   level $l$ from a cell at level $l-2$, in the north, south, east, and
   west directions, unless the cell abuts the physical boundary of the
   domain." This is "not as stringent as requiring a fine grid to be
   contained in only one coarser level grid" (Fig. 2.1 shows a fine grid
   spanning two coarser grids).
5. **Refinement in time** (§2, pp. 67–68). One ratio in space and time,
   $\Delta t_l/h_l$ equal on all levels, "so the same explicit difference
   scheme is stable on all grids". Reasons: spatial and temporal
   truncation errors are often of the same order, and "the smaller time
   step of the fine grid is not imposed globally". Only even
   $r_{\mathrm{ref}}$ is allowed, to simplify the error estimator.
6. **Level interleaving** (§3, eq. 1). A cell-centred conservative scheme
   is applied on every grid; "Before advancing a grid to time $t+\Delta t$,
   all the finer level grids have been integrated to time $t$." The
   update is then modified for coarse cells covered by a finer grid and
   for uncovered coarse cells next to a fine-grid interface.
7. **Restriction** (§3, p. 69). After every coarse step a covered coarse
   cell takes the average of its $r_{\mathrm{ref}}^2$ fine cells, and the
   coarse value from eq. 1 is discarded. This is "equivalent (within
   roundoff error)" to redefining the coarse fluxes as time sums of fine
   fluxes, and needs no flux storage.
8. **Conservative flux correction** (§3, eqs. 2–3). The coarse flux through
   a coarse–fine face is replaced in the coarse update by the average of
   the fine fluxes over the $r_{\mathrm{ref}}$ fine faces and the
   $r_{\mathrm{ref}}$ fine steps ("the double sum is due to the refinement
   in time"). Implementation by a register per coarse–fine face: set to
   minus the coarse flux after the coarse step (eq. 3); after each fine
   step add $r_{\mathrm{ref}}^{-2}$ times the sum of the fine fluxes on
   that face; after the $r_{\mathrm{ref}}$ fine steps add $\Delta t_l/h_l$
   times the register to the uncovered coarse cell for which the face is
   the left face, and subtract it where the face is the cell's right face
   (similarly in $y$). The weight
   $r_{\mathrm{ref}}^{-2}$ is $1/r_{\mathrm{ref}}$ for the face area times
   $1/r_{\mathrm{ref}}$ for the step ratio. The idea of a conservative
   interface is credited to Osher & Sanders and to an earlier paper of Berger. The
   register is stored per fine grid; with overlapping fine grids a marker
   array ensures each coarse edge is corrected once, independent of grid
   order. Cost: "approximately 0.3% of a typical run time" (§3, p. 71).
9. **Ghost values** (§4). A border as wide as the stencil, filled from
   adjacent same-level grids where possible, otherwise by "bilinear
   interpolation from coarser level solution values" and, "if necessary",
   linear interpolation in time. Done per rectangular boundary patch:
   gather coarser data on a slightly larger patch (recursing to coarser
   levels), interpolate, overwrite with same-level data. The interpolation
   is not stated to be conservative or limited. A first point-by-point
   implementation "took 40% of the run time and had to be rewritten".
10. **Regridding** (§5, pp. 72–73). At specified intervals, from the finest
    level down; only one new level can be added per regrid (any number
    removed), except at $t = 0$. Steps: a buffer zone of flagged cells
    around flagged cells ("two cells in each direction is typical");
    flag cells under the interior of grids two levels finer, to keep the
    nesting, and unflag cells within one cell of a non-physical boundary;
    cluster; subdivide grids not contained in the base grids.
11. **Clustering** (§5, pp. 73–74). One patch around all flagged cells; its
    efficiency is flagged cells over patch cells; below a minimum (e.g.
    60 %) the patch is bisected along its long direction, recursively;
    then two grids are merged if the merged grid costs less, with the cost
    of an $m\times n$ grid proportional to $mn + m + n$ (fluxes plus
    perimeter work). Grid generation takes "approximately 1.7% of the CPU
    time for a typical run". This is not the Berger–Rigoutsos algorithm.
12. **Richardson error estimation** (§6, pp. 74–75). Two steps of the scheme
    on a grid, minus one step of twice the size on the grid coarsened by
    2, divided by $2^{q+1} - 2$ for a scheme of order $q$ (the paper's
    symbol), estimates the local truncation error to one order higher.
    Implemented on a virtual grid coarsened by 2; where the estimate
    exceeds a tolerance, all four fine cells are flagged. Independent of
    the scheme and the equations; always large at captured
    discontinuities.
13. **Which discontinuities need refinement** (§6, p. 75). Captured shocks
    spread over a fixed number of zones, so a shock between constant
    states need not be refined; contacts and slip lines spread with time
    and usually must be.
14. **Strong shocks crossing a coarse–fine interface** (§6, pp. 75–76).
    Near a shock the captured fluxes differ by $O(1)$ from the exact ones;
    on a uniform grid these errors cancel in the time integral, but across
    an interface between two mesh sizes they do not, and $O(1)$ errors
    enter the post-shock state. The spurious-wave amplitude is observed to
    be proportional to the jump in the characteristic quantities crossing
    the shock; above a threshold strength shocks "must be refined
    everywhere, if they are to be refined anywhere" (Figs. 6.1–6.2).
15. **Code** (§8). "Not counting the integration routine, our program
    consists of 3000 lines of Fortran"; also used with FLO52 for transonic
    flow, with an induction-time chemistry model, and with conservative
    front tracking to keep strong captured shocks off grid boundaries.
    Implicit schemes on embedded grids are left open.

# Tests

All runs use the second-order Godunov method of Colella on a Cray X-MP/22
(§7).

1. **Strong shock forced across a grid boundary** (§6, Figs. 6.1–6.2).
   Refinement is forbidden above a given height, so a Mach 10 incident
   shock passes from fine to coarse; oscillations appear in the contours
   and in a density cut below the interface. Qualitative.
2. **Oblique shock reflection, Mach 10, 30°, $\gamma = 1.4$** (§7, Fig. 7.1).
   Domain $2.0\times0.4$, coarse $h = 0.02$ ($100\times20$ cells), three
   levels with $r_{\mathrm{ref}} = 4$ each (finest equivalent
   $1600\times320$), 149 coarse steps, error estimated every other coarse
   step, buffer one cell, grid efficiency 65 %, tolerance 0.02 on the
   truncation error of density, no tagging beyond a set distance behind
   the incident shock. "The finest grids in this calculation represent a
   factor of 4 increase in resolution in each spatial direction over the
   finest grid calculation in [22]" (p. 79), [22] being
   [Woodward & Colella (1984)](/sources/woodward-1984.md). Finding: a
   Kelvin–Helmholtz roll-up of the principal slip line, swept into the
   wall-jet roll-up.
   * **Table I** (FLOWTRACE, % of 5674 CPU s): integration 78.29;
     interpolation 12.95; output 2.87; grid updates 2.78; grid generation
     1.71; memory management 0.59.
   * Error estimation is 3 % of the integration cost; over 90 % of the
     integrated cells are on the finest level, where no error is
     estimated.
   * **Table II** (cell updates): level 1 $2.98\times10^5$; level 2
     $4.59\times10^6$; level 3 $1.13\times10^8$; error estimation
     $3.06\times10^6$.
   * **Against a uniform grid** (p. 79): the finest grids cover about 10 %
     of the domain and integration is about 80 % of the run time, so "an
     equivalent uniform grid computation would require a factor of 8 more
     CPU time"; about half could be saved on a uniform grid by skipping
     the region ahead of the shock, but "In general, this could not be
     done".
   * **Memory**: the uniform grid needs 9 arrays, printed as
     "9·320·1600 ≈ 4.5 × 10^6 words"; the AMR maximum is
     $8.94\times10^5$ words; even with 4 arrays the uniform run needs
     $2.0\times10^6$ words, "a factor of 2.2 larger". Much AMR memory holds
     two time levels per grid.

(Batch 9 flag withdrawn at deep lint #4: consistent in $h/t$; see [double Mach reflection](/benchmarks/double-mach-reflection.md).)

3. **Low-$\gamma$ double Mach reflection, Mach 8, 35°, $\gamma = 1.107$**
   (§7, Fig. 7.2, $t = 0.115$ and $0.230$). Seven Mach triple points,
   including a third on the top shock; "the limit of resolution" on the
   machine; the uniform-grid runs of Colella & Glaz were not fully
   resolved for $\gamma < 1.25$. Qualitative.

See [double Mach reflection](/benchmarks/double-mach-reflection.md). The
wedge set-up (initial shock position, frame, boundary conditions) and the
Courant number are not printed.

(Batch 10: [Colella & Glaz (1985)](/sources/colella-1985.md), the J. Comput. Phys. paper, has no low-$\gamma$ runs. Its only 2D test is a 20° ramp at shock Mach number 7.19 in air with three EOSs, so the "not fully resolved for $\gamma < 1.25$" statement does not rest on it. The reference list also cites Colella & Glaz in Lecture Notes in Physics 218 (`colella-1985-b`, not ingested), which may be the work meant; not verified.)

# Notation map

| Berger & Colella (1989) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$ | $u$ | **collision:** the paper's $u$ is also the $x$-velocity |
| $f(u)$, $g(u)$ | components of $\mathbf f(u)$ | |
| $F_{i+1/2,j}$, $G_{i,j+1/2}$ | $\hat f_{i+1/2}$ per direction | **collision:** the paper's $G$ is the $y$-flux and $G_{l,k}$ a grid; the registry $G$ is the gravitational constant |
| $G_{l,k}$, $G_l$ | none (words: grid $k$ of level $l$, level union) | |
| $l = 1,\dots,l_{\max}$, 1 coarsest | $l = 0,\dots$, 0 root | **offset:** paper level $l$ is registry level $l-1$ |
| $r = \Delta x_{l-1}/\Delta x_l$ | $r_{\mathrm{ref}}$ | same ratio in time |
| $\Delta x_l$, $\Delta y$; $h$ (§6) | $h_l$ | square cells in the runs |
| $\Delta t_l$; $k$ (§6) | $\Delta t_l$ | **collision:** $k$ is also a cell index in §3 |
| $\Delta t_{\mathrm{coarse}}$, $\Delta t_{\mathrm{fine}}$ | $\Delta t_l$, $\Delta t_{l+1}$ | |
| $\delta F_{i+1/2,j}$ | none (words: flux register) | |
| $Q$, $Q_{2h}$, $q$ | none (words) | one-step solution operator on the grid and on the grid coarsened by 2; formal order |
| $\tau$ | none (words: local truncation error) | **collision:** registry $\tau$ is the Valencia energy or, subscripted, an optical depth |
| $d$ (§4) | $n_{\mathrm g}$ | stencil half-width; **collision:** registry $d$ is the number of dimensions |
| $M_s$, $\alpha$ | none (words: incident Mach number, wedge angle) | |
| $\rho$, $u$, $v$, $p$, $\gamma$ | $\rho$, $\mathbf v$, $p$, $\gamma$ | |
| $E$ | $E/\rho$ | **collision:** the paper's $E$ is per unit mass, the registry's per unit volume |
| $D$, $\partial D$ | none (words: domain) | **collision:** registry $D$ is the Valencia density |

# Pages created or updated

* Created this Source page.
* Updated [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md):
  the original hierarchy, nesting, time refinement, restriction, flux
  register, ghost filling, regridding, clustering, Richardson estimator,
  the coarse–fine shock error and the cost tables; the attributions to
  Berger & Colella checked.
* Updated [Enzo](/software/enzo.md) and [FLASH](/software/flash.md):
  how their AMR departs from the paper.
* Updated [Athena](/software/athena.md): the conservation attribution
  checked.

# Citations

1. Berger M.J., Colella P. (1989), "Local adaptive mesh refinement for
   shock hydrodynamics", J. Comput. Phys. 82(1):64–84,
   doi:10.1016/0021-9991(89)90035-1. Local file:
   `/home/stefano/papers/mosaic/astrophysical-simulation-codes/1989-JCP-Berger.pdf`.
   * **Version read.** The published journal version (21-page scan of the
     Academic Press print, pp. 64–84, with an OCR text layer); received
     September 8, 1987, revised May 20, 1988. Not a preprint.
   * **Identity.** Checked on Crossref (DOI from the PII on page 1):
     title, the two authors, vol. 82, issue 1, pp. 64–84, issued 1989-05;
     agrees with page 1.
   * **How it was read.** Text layer for the prose; eqs. 1–3, the
     restriction and register formulas, the §6 error-estimate formulas,
     Tables I–II and the reference list were read from rendered pages
     (pp. 66–70, 74–75, 78–80, 84), because the OCR garbles them. The
     contour figures (6.1, 6.2, 7.1, 7.2) give no quantitative values.
   * **Recorded as printed.** §7 says Fig. 7.1a shows the grids "at time
     $t = 1.20$", the Fig. 7.1 caption $t = 0.12$; the caption's 0.12 is the consistent value (see double Mach reflection). The
     restriction formula prints the coarse index as $l,j$ (p. 69). The
     uniform-grid memory is printed "≈ 4.5 × 10^6 words" for
     $9\cdot320\cdot1600 = 4.61\times10^6$ (computed at ingestion); the
     ratio "2.2" agrees with the printed $2.0\times10^6/8.94\times10^5 = 2.24$.
     The order of the interpolation that initializes new fine grids is not
     stated. The Godunov method used is cited without volume or year (an
     LBL report "to appear" in J. Comput. Phys.).
   * **Reference list:** 22 entries. "Collela & Woodward, J. Comput. Phys.
     59:264 (1985)" is Colella & Glaz by venue (Crossref) and lands on
     `colella-1985`; Colella & Glaz in Lecture Notes in Physics 218 is
     `colella-1985-b`; Colella's LBL-17023 (J. Comput. Phys., no title or
     year) is `colella-1989`, the year being the citing date (possibly the
     report version of `colella-1990`, not verified); Adjerid & Flaherty,
     Chern & Colella and Dwyer, printed without a year, are keyed with the
     citing year 1989. Berger & Oliger (J. Comput. Phys. 53:484) and
     [Woodward & Colella](/sources/woodward-1984.md) (54:115) land on the existing entries. The
     bibliography holds 2200 entries after the merge.

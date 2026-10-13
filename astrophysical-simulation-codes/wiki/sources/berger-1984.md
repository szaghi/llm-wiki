---
type: Source
title: "Berger & Oliger (1984) — Adaptive Mesh Refinement for Hyperbolic Partial Differential Equations"
description: "Origin of Berger–Oliger AMR: a base grid overlaid by a recursive hierarchy of independent, possibly rotated rectangular subgrids, refined by one integer ratio in space and time and advanced recursively, with a scheme-independent Richardson estimate of the truncation error, clustering and second-moment grid fitting, injection updates of the coarse grid and no flux correction; tested on Sod, a rotating cone and 2D Burgers."
resource: "doi:10.1016/0021-9991(84)90073-1"
source_kind: paper
authors: [Berger M.J., Oliger J.]
year: 1984
venue: "J. Comput. Phys. 53:484–512"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/1984-JCP-Berger-1010160021-99918490073-1.pdf"
tags: [amr, time-integration, refinement-criteria, verification]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper introduces adaptive mesh refinement for hyperbolic systems
solved by explicit finite differences. A fixed base grid is overlaid by a
recursive hierarchy of independent, locally uniform rectangular subgrids
of **arbitrary orientation**, each with its own storage, nested level by
level (§2). Fine grids are refined by the same integer ratio
$r_{\mathrm{ref}}$ in space and time, so $\Delta t_l/h_l$ is the same on
all levels, and one coarse step is a recursive procedure that advances
each finer level $r_{\mathrm{ref}}$ times (§3, Fig. 3.3). Refinement is
driven by a Richardson estimate of the local truncation error that is
independent of the equations and of the scheme (eq. 3.2). Flagged points
are clustered and each cluster is fitted with a rectangle aligned with the
eigenvectors of the points' second-moment matrix, plus a buffer zone
(§4). The coarse grid is updated by **injection** of fine values; no flux
correction is applied, and conservative interface conditions are
announced as "reported elsewhere" (§3). The grids are managed by a tree
(1D) or a forest (2D) with a first-fit storage allocator (§5). On a Sod
tube, a rotating cone and a 2D Burgers problem the method reaches about
the fine-grid error at a fraction of the uniform-fine cost (§6). See
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).

# Key claims

Registry notation: $h_l$, $\Delta t_l$, $r_{\mathrm{ref}}$, level $l$ with
$l = 0$ the base grid (see the Notation map).

1. **Space–time refinement as the main efficiency factor** (§1, p. 485;
   §3, p. 489). $h_l = h_{l-1}/r_{\mathrm{ref}}$ and
   $\Delta t_l = \Delta t_{l-1}/r_{\mathrm{ref}}$, so $\Delta t_l/h_l$ is
   constant on all grids. "We believe that our adaptive methods are the
   first to use such a space-time grid structure and find that this is a
   major factor in the efficiency of the method"; "the overly restrictive
   small time step of the finest grid is not applied over the entire
   domain". No run compares against a single global step on the same
   hierarchy.
2. **Overlaid, independent grids** (§2, pp. 486–487). "These subgrids are
   not patched into the coarse grid. Rather, a subgrid should be thought of
   as overlaying a coarser grid", with its own solution vector and storage.
   Merging fine points into one global grid is rejected because it
   destroys local uniformity and vectorization. The decomposition into
   regular blocks "can also be easily used for parallel or concurrent
   processing" (§1).
3. **Rotated rectangles** (§§1–3, pp. 486, 489–490). Subgrids are
   "rectangles of arbitrary orientation", to align with shocks and reduce
   the refined area. The difference equations are transformed
   conservatively to the rotated coordinates after Viviand.
4. **Hierarchy and nesting** (§2, pp. 487–488). The cell sizes
   $h_0, h_1, \dots$ are fixed in advance, each an integer multiple of the
   next. All intermediate levels are kept. Each fine point must lie in the
   **interior** of a next-coarser grid unless it is on the physical
   boundary; a fine grid may be nested in the **union** of several coarser
   grids ("level nesting", Fig. 2.1). Same-level grids may overlap in 2D.
   The solution at a point is that of the finest grid in whose interior it
   lies.
5. **Refinement ratio** (§2, p. 487). "Since there is some overhead
   associated with refined grids, we prefer a refinement ratio of 4 over
   the ratio of 2 typically used with multigrid methods". One level of
   ratio $r_{\mathrm{ref}}$ is cheaper than two of ratio
   $\sqrt{r_{\mathrm{ref}}}$ when one region needs refinement. The runs
   use $r_{\mathrm{ref}}$ = 10, 4 and 10 (§6).
6. **Integration order** (§3, p. 489; Fig. 3.3, p. 494). Before a grid
   advances, all its subgrids are integrated to its time. The recursive
   procedure `Integrate(level)` repeats, per call: optional regridding with
   error estimation for the level and finer; one step on all grids of the
   level; `Integrate(level+1)` and `Update(level, level+1)` if a finer
   level exists. The repeat count is printed as $(h_f/h_c)^{level}$ (see
   Citations). The Fortran implementation is iterative.
7. **Different integrators per grid** (§3, p. 490): e.g. a first-order
   scheme on a refined grid around a shock and higher order elsewhere,
   artificial viscosity only on fine grids, or boundary-layer equations on
   a separate grid. The integrators are user modules separated from the
   AMR routines.
8. **Regridding frequency and buffer** (§3, pp. 490–491). A buffer zone
   lengthens the interval between regrids at the cost of extra points;
   "Typical calculations give an optimal regridding frequency of
   approximately every 3–4 steps", per level.
9. **Richardson error estimator** (§3, pp. 491–492, eqs. 3.1–3.2). In the
   paper's notation ($Q$ the one-step operator on $h$, $Q_{2h}$ one step
   on the grid coarsened by 2, $\tau$ the leading local truncation error,
   $q$ the common order in space and time):
   $$\frac{Q^2u(x,t) - Q_{2h}u(x,t)}{2^{q+1}-2} = \tau + O(h^{q+2}).$$
   It is independent of the PDE and of the scheme, but needs equal order
   in space and time (Lax–Wendroff, MacCormack, leapfrog, upstream);
   otherwise the spatial and temporal errors are estimated separately. For
   non-smooth solutions it is no longer accurate but "still a good
   criterion"; for piecewise-constant data it is proportional to the jump.
   The motivation is Gustafsson's result that the convergence rate is set
   by the local truncation error when initial and boundary errors are of
   no lower order.
10. **Fine-grid boundary values** (§3, p. 493). From the interior of an
    intersecting same-level grid if one exists, else from coarser grids by
    Ciment's coarse-mesh approximation or by interpolation. Berger's thesis
    proves that with Lax–Wendroff and either interface equation, refinement
    in space and time "by any integer is stable in the sense of Kreiss".
    "Stable boundary conditions have been derived which maintain the
    conservation form of the difference scheme at the interface between
    the fine and coarse grid. These will also be reported elsewhere."
11. **Updating by injection** (§3, p. 493). When fine and coarse grids
    reach the same time, coarse values are replaced by injected fine
    values (interpolated where points do not coincide). For explicit
    schemes only as many coarse points along the fine-grid perimeter as the
    coarse stencil width need it. The stated reasons: otherwise the coarse
    solution disperses so much that refinement seems unnecessary, and bad
    coarse values contaminate the buffer and the fine boundary data. **No
    flux correction is used**; conservation across interfaces is deferred.
12. **Overlap averaging** (§3, p. 493): only for overlapping same-level
    grids, at most a few coarse cells wide; "so far ... only for graphical
    output".
13. **Regridding** (§4, pp. 494–499). Points with an estimate above a
    tolerance are flagged; level-$l$ points interior to level-$(l+2)$ grids
    are also flagged to keep the nesting; regridding runs from finest to
    coarsest. Four steps: flag, cluster, fit a grid per cluster, evaluate.
    At most one new level per regrid, except at $t = 0$ and at boundaries
    with time-dependent data.
14. **Clustering and fitting** (§4, pp. 495–498). 1D: intervals split at
    long gaps; points closer than twice the buffer width share a grid. 2D:
    nearest-neighbour clustering (tolerance "usually ... two mesh widths"),
    then minimal spanning trees and relative-neighbour graphs; a merge is
    rejected when the ratio of flagged to new fine-grid points falls below
    a cutoff "typically between 1/2 and 3/4". Each rectangle's orientation
    is that of the eigenvectors of the second-moment matrix of its flagged
    points; clustering is "still an open problem".
15. **Data structures** (§5, pp. 499–502). A 1D ordered tree with
    offspring, sibling and parent pointers and a same-level thread; in 2D a
    forest with one root per base component, with linked lists of parents
    and of intersecting same-level grids. Solution storage is one large
    array managed by first-fit allocation without compaction.
16. **Overhead** (§6, p. 505). On the rotating cone, about 9 s "are spent
    on other things besides integrating the grids. This is roughly 12% of
    the computing time, most of which is spent estimating the error and
    generating the subgrids" (9/86.6 s is about 10 % of the AMR run time,
    computed here).
17. **Open problems** (§7, p. 511). 3D "immediately"; steady states,
    implicit methods with diffusion, grids in different coordinate systems
    and "the best grid generation procedure" remain open.

# Tests

Error norm (§6, p. 502): a discrete $L_2$ norm evaluated only at
coarse-grid points. 1D runs on an IBM 370/168, 2D on an IBM 370/3081. No
convergence order is measured.

1. **[Sod shock tube](/benchmarks/sod-shock-tube.md)** (§6, Example 1,
   pp. 502–505, Table I). $\gamma = 1.4$; $\rho$ = 1 | 0.125, $p$ = 1 | 0.1,
   at rest; $0 \le t \le 0.15$; two-step Lax–Wendroff with artificial
   viscosity, reflecting walls; buffer 4, regrid every 5 steps, tolerance
   0.0005, $r_{\mathrm{ref}} = 10$, $\Delta t_l/h_l = 0.1$; 20–70 % of the
   coarse grid refined.

   | Run | $h$ | $L_2$ at coarse points | Time (s) |
   |---|---|---|---|
   | coarse | 0.01 | 2.14E−2 | 7.36 |
   | fine | 0.001 | 1.15E−2 | 347.0 |
   | AMR, 2 levels | finest 0.001 | 1.15E−2 | 79.9 |
   | AMR, 3 levels | finest 0.0001 | 6.53E−3 | 591.0 |

   Fine-grid accuracy "in less than one fourth the time" (79.9/347.0 =
   0.23, computed here). Errors are dominated by smearing at the
   rarefaction corners and the contact. Floating-point underflow interrupts
   skew the timings.
2. **Rotating cone** (§6, Example 2, pp. 505–507, Table II). Solid-body
   rotation of a cone on $[-1,1]^2$ for about half a revolution, after
   Gottlieb & Orszag; Lax–Wendroff without artificial viscosity; buffer 2,
   regrid every 8 steps, tolerance 0.001, $r_{\mathrm{ref}} = 4$,
   $\Delta t_l/h_l = 0.25$; one moving subgrid, about 12 % refined.

   | Run | $h$ | $L_2$ at coarse points | Time (s) |
   |---|---|---|---|
   | coarse | 1/20 | 5.21E−2 | 6.86 |
   | fine | 1/80 | 9.34E−3 | 588.0 |
   | AMR | finest 1/80 | 9.78E−3 | 86.6 |

   About the fine-grid error in "about one sixth the time"; the text says
   the run "costs only 16%" of the uniform fine run (86.6/588.0 = 14.7 %,
   computed here). The coarse-grid wake behind the cone is much reduced
   with AMR, "why the coarse grid solution must be updated by the fine
   grid".
3. **2D inviscid Burgers** (§6, Example 3, pp. 507–510, Table III), from
   Gropp: piecewise-constant data on the unit square; MacCormack; buffer
   1, regrid every 4 steps, tolerance 0.001, $r_{\mathrm{ref}} = 10$,
   $\Delta t_l/h_l = 0.5$.

   | Run | $h$ | $L_2$ at coarse points | Time (s) |
   |---|---|---|---|
   | coarse | 1/20 | 8.0E−2 | 0.18 |
   | fine | 1/200 | 3.86E−2 | 155.0 |
   | AMR | finest 1/200 | 2.75E−2 | 109.0 |

   "The most difficult example for the clustering and grid generation
   algorithms": much of the domain is refined, and AMR still runs in 0.70
   of the uniform-fine time (computed here). The AMR error is *smaller*
   than the uniform fine error, attributed to the linear interpolation
   that injects rotated-grid values onto the coarse grid and smooths the
   discontinuities.

# Notation map

| Paper | Canonical | Note |
|---|---|---|
| $u$, $f(u)$, $g(u)$ | $u$, components of $\mathbf f(u)$ | the paper writes $u_t = f(u)_x + g(u)_y$ |
| $G$, $G_l$, $G_{l,j}$ | in words | grid hierarchy, level-$l$ union, component grid |
| level $l$, level 0 coarsest | $l$ | agrees |
| $h_l$ | $h_l$ | agrees |
| $k_l$ | $\Delta t_l$ | time step |
| $r$ | $r_{\mathrm{ref}}$ | refinement ratio; **collision**: $r$ is also a rotated coordinate |
| $\lambda = k/h$ | $\Delta t_l/h_l$ | **collision**: registry $\lambda^{(p)}$ are eigenvalues |
| $Q$, $Q^2$, $Q_{2h}$ | in words | one-step operator, two steps, one step on the grid coarsened by 2 |
| $\tau$ | in words | leading local truncation error; **collision**: Valencia energy and optical depth |
| $q$, $q_1$, $q_2$ | in words | orders in time and space |
| $e(x)$, $\varepsilon$ (§4) | in words | error estimate and tolerance; **collision**: registry $e$ |
| $e$, $\varepsilon$, $m$ (Example 1) | $E$, $e$, $\rho\mathbf v$ | **collision**: the paper's $e$ is the total energy density, its $\varepsilon$ the specific internal energy |
| $u$ (velocity, Example 1) | $\mathbf v$ | **collision** with the state $u$ |
| $\Vert\mathrm{error}\Vert_{2_c}$ | $L_2$ | evaluated at coarse-grid points only |
| $r, s$, $J$ | in words | rotated coordinates and Jacobian; **collision**: $s(u)$, $\mathbf J$, $r_{\mathrm{ref}}$ |
| $A$, $A_m$, $M^{\mathrm t}M$ | in words | flagged-point coordinates, their mean, second-moment matrix; **collision**: Jacobian $A$ |

# Pages created or updated

* Created this Source page.
* Updated [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
  (batch-10 section: the original hierarchy, rotated overlaid grids, time
  refinement, Richardson estimator, injection without flux correction,
  clustering, data structures and cost; the attributions to Berger &
  Oliger checked; the refinement-ratio recommendation as a qualification;
  evidence added to the Open subcycling entry).
* Updated
  [Sod shock tube](/benchmarks/sod-shock-tube.md).

# Citations

1. Berger M.J., Oliger J. (1984), "Adaptive mesh refinement for hyperbolic
   partial differential equations", J. Comput. Phys. 53(3):484–512,
   doi:10.1016/0021-9991(84)90073-1. Local file:
   `/home/stefano/papers/mosaic/astrophysical-simulation-codes/1984-JCP-Berger-1010160021-99918490073-1.pdf`.
   * **Version read.** The published journal version (29-page scan of the
     Academic Press print with an OCR text layer; received March 8, 1983,
     revised August 24, 1983). Not a preprint.
   * **Identity.** Checked on Crossref: title, the two authors, vol. 53,
     issue 3, pp. 484–512, issued 1984-03; agrees with page 1.
   * **How it was read.** Text layer for the prose; all equations, the
     algorithm of Fig. 3.3, the parameter blocks, Tables I–III and the
     reference list were checked on rendered pages (pp. 489–492, 494,
     497–498, 502–505, 507, 510–512). Figs. 4.2, 5.2 and 6.3–6.6 are
     images; only captions and visible labels were used.
   * **Recorded as printed.** (a) Fig. 3.3 prints the repeat count of
     `Integrate(level)` as $(h_f/h_c)^{level}$; the intended per-call
     repetition (by the refinement ratio) is not stated. (b) Below eq. 3.1
     the two-step remainder is printed $k\,O(k^{q_1+1} + k^{q_2+1})$
     (reader's reading: the second $k$ is an $h$). (c) The second-moment
     matrix entries are printed $\sum_i x_i^2 - x_m^2$ etc., without the
     factor $n$ on the mean terms. (d) Example 1 prints the initial states
     for $x < 0$ and $x > 0$ on the domain $0 \le x \le 1$; the diaphragm
     position is ambiguous as printed. (e) Example 3's coarse time 0.18 s
     was checked at 250 dpi. The convergence result of Oliger and the
     conservative interface conditions are cited, not given.
   * **Reference list:** 31 printed entries, all merged. Gropp (1980),
     printed SIAM J. Sci. Statist. Comput. 1:191, agrees with Crossref
     (the existing `gropp-1980` entry stores 4:191; the note records the
     discrepancy). Harten & Hyman (J. Comput. Phys. 50:235) is
     `harten-1983-c`, not `harten-1983` (Harten, Lax & van Leer). Miller &
     Miller, SIAM J. Numer. Anal. 18:1019, is the new `miller-1981-b`,
     kept apart from `miller-1981` (18:1033, cited by Berger & Colella).
     Gottlieb & Orszag is printed "Gotlieb" (`gotlieb-1977`; the text spells
     Gottlieb). Oliger's "to appear" is `oliger-1984`, keyed with the
     citing year. Winkler's thesis (Max Planck Institute, 1977, title
     printed) is `winkler-1977`, kept apart from `winkler-1976`
     (Göttingen, no title; identity not verified). Bibliography: 2522
     entries.

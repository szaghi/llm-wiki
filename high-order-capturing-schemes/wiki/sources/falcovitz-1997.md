---
type: Source
title: "Falcovitz, Alfandary & Hanoch (1997) — A two-dimensional conservation laws scheme for compressible flows with moving boundaries"
description: "Moving boundary tracking (MBT): a dimensionally split GRP scheme on a fixed Cartesian grid with conservative, time-changing cut cells whose old and new volumes, time-averaged face apertures and projected boundary areas come from a trapezoid decomposition rule, so that uniform flow moving with the body is exact; first order in boundary cells, small cells merged; origin of the shock-driven cylinder lift-off test."
resource: "doi:10.1006/jcph.1997.5808"
source_kind: paper
authors: [Falcovitz J., Alfandary G., Hanoch G.]
year: 1997
venue: "J. Comput. Phys. 138:83–102"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1997-JCP-Falcovitz-101006jcph19975808.pdf"
tags: [embedded-boundary, moving-boundary, boundary-treatment, euler]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The second-order generalized Riemann problem (GRP) scheme of Ben-Artzi
and Falcovitz, applied dimension by dimension, is extended to
impermeable boundaries that move across a fixed Cartesian grid ("moving
boundary tracking", MBT). The body is a set of closed polygons. Boundary
cells are time-changing finite volumes with an old and a new fluid volume,
time-averaged exposed face areas, and a time-averaged projected boundary
area that carries the boundary pressure and work. The node motion is
split too, each split phase moving the polygon in one direction only.
All geometry comes from a "decomposition rule" that writes polygon areas
as signed sums of trapezoids. The design requirement is that a uniform
flow with the boundary moving at the fluid velocity is reproduced
exactly. Small, newly exposed and newly covered cells are merged with a
wet neighbour. The only computation shown is a Mach 3 shock lifting a
light cylinder off the floor, without error or convergence data. Merged
into [cut-cell finite volume](/methods/cut-cell-finite-volume.md) and the
[shock-driven cylinder lift-off](/benchmarks/shock-cylinder-lift-off.md).

# Key claims

1. **Equations** (§2, eq. 1): 2D plane Euler, perfect gas. Cylindrical
   symmetry is called a "fairly straightforward" extension, not shown.
2. **Splitting** (§2, eqs. 3–4). Strang splitting is second order; the
   authors normally use the plain sequence of an $x$ step then a $y$ step,
   found "virtually indistinguishable" in shock computations. Their
   argument merges adjacent half-steps over many steps, and they state
   that it "do[es] not constitute a proof"; no convergence test is given.
   *Compiler's note (hypothesis):* the argument leaves a half-step
   conjugation at the two ends, an $O(\Delta t)$ change of the final state,
   so by itself it gives first order for the plain sequence.
3. **1D building block** (§2, eq. 5): conservative update with
   piecewise-linear cell data and time-centred fluxes from analytic
   solutions of generalized Riemann problems.
4. **Boundary-cell finite volume** (§3, eqs. 6–9, $x$ phase). With old and
   new fluid volumes $\kappa_i^n h^2$, $\kappa_i^{n+1}h^2$ and time-averaged
   exposed face areas, mass, momentum and energy balance over the step. No
   mass or advective flux crosses the boundary: it adds only a pressure
   term to the normal momentum and a work term to the energy, each through
   the time-averaged projected boundary area, averaged as products over the
   step and the polygon segments in the cell.
5. **Boundary pressure** (§3, pp. 90–91) from a one-sided (piston) Riemann
   problem normal to each segment, with the known normal boundary speed and
   the cell state at $t^n$. Boundary cells carry piecewise-constant data,
   so MBT is first order in boundary cells (stated, p. 91).
6. **Cell merging** (§3, p. 91). The CFL condition is assumed to keep a
   cell from going between fully exposed and fully covered in one step. A
   cell becoming fully covered, a covered cell becoming partly exposed, and
   a cell whose partial length is below a user fraction, "typically about
   0.3" of a cell, are merged with an adjacent wet cell; the merged state is
   assigned to every member, so no unmerging is needed.
7. **Decomposition rule** (§4.1, eq. 11). A polygon's area is the signed
   sum of the trapezoids its sides subtend on a reference line outside the
   polygon's height range (credited to Mason's TOOREZ rezoning); it avoids
   constructing intersection polygons. Covered cell volumes follow from
   differences of trapezoid–half-column intersections (§4.3, eqs. 23–26).
8. **Time-averaged apertures** (§4.3, eqs. 27–33). The covered length of
   a face is a space–time integral of a cover function, built so that
   uniform flow is exact. Lemma 4.1 (eq. 29, proved, p. 98): the polygon's
   cover function is the signed sum of its trapezoids', so the covered
   lengths add over sides. For a monotonically moving side, the time-cover
   fraction is a rational function of $x$, integrated in closed form;
   non-monotonic motion is reduced to it by time reversal and a pivot point.
9. **Projected boundary area** (§4.3, eq. 34): the difference of the
   covered lengths of a cell's two faces in the split direction, summed over
   sides and polygons — the same quantities as the apertures, so the
   boundary term is geometrically consistent with the face fluxes.
10. **Consistency and conservation** (§§1, 3, 4.3). Exact uniform flow is
    satisfied "by construction" under node motion linear in time; no
    numerical demonstration is given. MBT "maintains an exact integration
    of the conservation laws in boundary cells", unlike Forrer's mirroring
    scheme (§1, p. 85).
11. **Coupling** (§1, pp. 85–86): the boundary motion is prescribed; a
    rigid body's motion can follow from the integrated pressure force
    ("inertial coupling").

**Tests** (§5). A double-wedge shock diffraction with a stationary
boundary is only mentioned, as validated against experiment in an
earlier paper (no set-up or figure here). The
[cylinder lift-off](/benchmarks/shock-cylinder-lift-off.md) (Fig. 5):
domain $100\times20$, $200\times40$ cells (mesh $R/10$); a 50-sided
polygon of radius $R = 5$, centre $(15, 5)$, resting on the floor, density
0.01; gas at rest with $\rho = 0.0013$, $p = 10^{-6}$, $\gamma = 1.40$;
$M_s = 3.0$ shock starting 8 from the left; post-shock inflow on the left,
non-reflecting on the right, rigid walls top and bottom; CFL "about 0.5";
plots at $T = 0$, 500, 1000 (time units not stated). The caption gives a
density ratio of 8 and the text "roughly eight"; $0.01/0.0013 = 7.69$.
Initial lift comes from the asymmetric shock reflection at the floor.
Results are qualitative only.

# Notation map

| Falcovitz et al. (1997) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U = (\rho, \rho u, \rho v, \rho E)$ | $u$ | paper's $u$ is the $x$-velocity |
| $u$, $v$ | $\mathbf v = (v_1, v_2)$ | |
| $E$ (specific total energy) | $E/\rho$ | registry $E$ is the energy density, the paper's $\rho E$ |
| $F(U)$, $G(U)$ | $\mathbf f$ | |
| $F(U)^{n+1/2}_{i+1/2}$ | $\hat f_{i+1/2}$ | time-centred GRP flux |
| $U_i^n$ | $\bar u_i$ | |
| $\Delta x$, $\Delta y$; $t_n$ | $h_x$, $h_y$; $t^n$ | |
| $V_i^n$, $V_i^{n+1}$ | $\kappa_i^n h^2$, $\kappa_i^{n+1}h^2$ | old and new fluid volume |
| $L_x$, $L_y$, $L$ | words | registry $L$ is the left eigenvector matrix |
| $A^{n+1/2}_{i\pm1/2}$, $A_{b_i}$, $P_{b_i}$, $U_{b_i}$ | words | registry $A$ is the flux Jacobian |
| $\theta$, $\Theta_{k,j+1/2}$, $H$, $Q$, $B$, $S$ | words | collide with $\theta$, $\Theta_{i+1/2}$, $\mathbf B$, $M$ |
| $M_s$; CFL coefficient | $M_s$; $\nu$ | |

# Pages created or updated

* Updated [Shock-driven cylinder lift-off](/benchmarks/shock-cylinder-lift-off.md): this paper is the origin; the Tan–Shu set-up is its rescaling.
* Updated [Cut-cell finite volume](/methods/cut-cell-finite-volume.md): moving boundary tracking.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/1997-JCP-Falcovitz-101006jcph19975808.pdf`.
   * **Version.** Publisher's version of record (Academic Press), 20 pages.
   * **Identity.** doi:10.1006/jcph.1997.5808, checked on Crossref: J.
     Comput. Phys. 138(1):83–102, November 1997, authors Falcovitz,
     Alfandary and Hanoch.
   * **How it was read.** Text extraction, all sections; Symbol-font
     glyphs are garbled in the text layer, so every equation quoted was
     checked on the page images (pp. 88, 90, 93, 97, 99, 100). Eqs. 12–22,
     24 and 31 were read in the text layer only and are not reproduced.
   * **Recorded as printed.** Eq. 28 integrates the fractional time from
     $t_n$ to $t_{n+1}$ where eq. 30b, the operative form, uses 0 to 1; the
     density ratio 8 against $0.01/0.0013 = 7.69$.
   * **Reference list:** 20 entries; van Leer 1979 (entry 19) is never
     cited in the text. Quirk's final report is merged into
     `quirk-1994-b`; Ben-Artzi & Falcovitz is `benartzi-1984`. Noh's CEL
     chapter (Methods in Computational Physics, vol. 3) is `noh-1964`,
     kept distinct from the Livermore report `noh-1963`.

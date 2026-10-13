---
type: Source
title: "Berger & Oliger (1984) — Adaptive Mesh Refinement for Hyperbolic Partial Differential Equations"
description: "The original AMR algorithm for hyperbolic systems: a recursive hierarchy of rotated, overlaid subgrids refined in space and time by the same ratio, flagged by a Richardson truncation-error estimate, coupled by interpolated boundary values and coarse updating by injection, with no flux correction."
resource: "doi:10.1016/0021-9991(84)90073-1"
source_kind: paper
authors: [Berger M.J., Oliger J.]
year: 1984
venue: "J. Comput. Phys. 53:484-512"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1984-JCP-Berger-1010160021-99918490073-1.pdf"
tags: [amr, hierarchy, subcycling, error-estimation, regridding]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

An adaptive finite-difference method for hyperbolic systems. A fixed base
grid is overlaid by a recursive hierarchy of finer subgrids. The subgrids
are **rectangles of arbitrary orientation**, each an independent grid with
its own storage, that *overlay* the coarse grid rather than being patched
into it (§§1–2). The refinement ratio $r$ applies in time as well as in
space, so $\Delta t/h$ is the same on every level (§3). The refinement
criterion is a Richardson-extrapolation estimate of the local truncation
error (eq. 3.2). Fine-grid boundary values come from overlapping
same-level grids or from the coarser grid, and coarse values under a fine
grid are **updated by injection** (§3). Flagged points are clustered, and
each cluster gets a rectangle oriented along the principal axes of its
points (§4). A tree/forest data structure manages the hierarchy (§5).
Three tests (Sod shock tube, rotating cone, 2D inviscid Burgers) reach
uniform-fine accuracy at a fraction of the cost (§6). The paper has no
divergence content and no flux correction; this is the "earlier
rotated-grid approach" that
[Berger & Colella (1989)](/sources/berger-colella-1989.md) refined into
grid-aligned patches ([block-structured AMR](/definitions/block-structured-amr.md)).

# Key claims

1. **Hierarchy and nesting** (§2, pp. 486–488, Fig. 2.1).
   * The base grid is fixed for the run and may consist of several
     overlapping component grids, each locally uniform in its own
     coordinates. Level-$l$ mesh widths are $1/r$ of level $l-1$'s.
   * **Nesting:** every point of a level-$l$ grid must lie in the
     *interior* of a level-$(l-1)$ grid, unless it lies on the physical
     boundary, with all intermediate grids kept (p. 487). A fine grid need
     only lie inside the *union* of level-$(l-1)$ grids (p. 488).
   * Same-level grids may overlap in 2D; in 1D they are disjoint or merged.
   * The solution at a point is "defined by interpolation from the finest
     grid to which that point is interior" (p. 487).
2. **Refinement ratio** (p. 487). The authors "prefer a refinement ratio of
   4 over the ratio of 2 typically used with multigrid methods", because
   each refined grid carries overhead. The tests use $r = 10$, 4 and 10.
3. **Rotated, overlaid subgrids** (§§1–2, pp. 484–487). Orientation aligns
   grids with singular surfaces such as shocks and reduces the refined
   point count. Grids are not merged into the coarse grid: in the authors'
   account Simpson's merging "destroys the local uniformity of each grid"
   and prevents vectorization. Independent grids make the method a form of
   domain decomposition suited to multiprocessors (p. 487).
4. **Time refinement** (§3, p. 489, Figs. 3.1, 3.3). The time step of
   level $l$ is $1/r$ of level $l-1$'s, so the mesh ratio is constant; the
   paper names this as a main source of efficiency. A grid's subgrids are
   integrated to its time before it advances. The recursive procedure of
   Fig. 3.3 regrids if due, steps all grids of the level, recurses to the
   next level and then updates the coarser level.
5. **Integration on rotated grids** (§3, pp. 489–490). The equations are
   transformed to each grid's rotated coordinates, which for standard
   schemes "can be done conservatively" (Viviand). Different integrators,
   or even different equations, may run on different grids.
6. **Regridding frequency and buffer** (§3, pp. 490–491). A buffer zone
   around fine grids lengthens the safe interval between regriddings
   (finite propagation speed). "Typical calculations give an optimal
   regridding frequency of approximately every 3–4 steps", per level.
7. **Richardson error estimator** (eqs. 3.1–3.2, pp. 491–492, Fig. 3.2).
   For a two-level explicit scheme of equal order $q$ in time and space,
   two regular steps are compared with one step of the same scheme on a
   mesh coarsened by 2 in space and time; their difference divided by
   $2^{q+1}-2$ estimates the local truncation error to
   $O(h^{q+2})$. The estimator is independent of the PDE and the
   difference method and reuses the user's integrator. Unequal orders need
   separate space and time estimates at extra cost (p. 492). For
   non-smooth solutions the estimate "still provide[s] a good criterion
   for refinement"; for piecewise-constant data it is proportional to the
   jump (pp. 492–493).
8. **Intergrid communication** (§3, p. 493).
   * *Fine boundary values* come from an intersecting same-level grid if
     there is one, else from the coarse grid by interpolation or Ciment's
     coarse-mesh approximation. Berger's thesis is cited for stability, in
     the sense of Kreiss, of Lax–Wendroff with either treatment under
     space–time refinement by any integer. Interpolation orders and time
     interpolation are not specified.
   * *Conservation:* "stable boundary conditions have been derived which
     maintain the conservation form of the difference scheme at the
     interface between the fine and coarse grid. These will also be
     reported elsewhere." No conservative interface treatment is given.
   * *Updating:* when coarse and fine grids reach the same time, coarse
     values are replaced by **injection** of fine values (interpolation
     where points do not coincide). Implicit schemes might want "some sort
     of averaging … before injecting". Without updating, the coarse
     solution disperses and contaminates the buffer zone.
9. **Regridding** (§4, pp. 494–499).
   * Points whose error estimate exceeds the tolerance are flagged; level-$l$
     points interior to level-$(l+2)$ grids are also flagged, so nesting is
     kept. Regridding runs from finest to coarsest.
   * Clustering: trivial in 1D; in 2D nearest-neighbour with a tolerance of
     usually two mesh widths, falling back to minimal spanning trees or
     relative-neighbour graphs (Fig. 4.2). A merge is kept only if the
     fraction of flagged points stays above a cutoff "typically between ½
     and ¾" (p. 497).
   * Orientation: the eigenvectors of the second-moment matrix of the
     flagged points about their mean (translation- and rotation-invariant);
     extent from projections on those axes, plus a buffer (pp. 498–499).
   * New fine grids are initialized by interpolation from the finest
     existing grids (p. 490), or from the initial data at $t = 0$.
10. **Data structures** (§5, pp. 499–502). In 1D an ordered tree with
    offspring, sibling, parent and same-level "neighbor" links; in 2D a
    forest with one root per base component, parent lists (partial nesting
    in several coarse grids) and intersection lists. Solution storage is
    one array managed by first-fit allocation without compaction.
11. **Open problems** (§7, p. 511): steady states, implicit methods on
    this grid structure, component grids in different coordinate systems,
    and the best subgrid-generation procedure.
12. **Divergence constraints: none.** The equations are 1D Euler, 2D
    linear advection by rotation and 2D scalar Burgers. Conservation enters
    only through the conservative rotated-coordinate transformation and the
    announced interface conditions; coarse updating is injection, not a
    conservative average, and there is no flux correction.

# Tests

The error is measured on coarse-grid points only, as a root-mean-square
norm (p. 502). Each adaptive run (MR) is compared with uniform coarse and
uniform fine runs; times are IBM 370 seconds.

1. **Sod shock tube** (§6, pp. 502–505, Table I;
   [Sod shock tube](/benchmarks/sod-shock-tube.md)). 1D Euler, $\gamma = 1.4$,
   two-step Lax–Wendroff with artificial viscosity, buffer 4, regrid every 5
   steps, tolerance 0.0005, $r = 10$, mesh ratio 0.1.

   | Run | $h$ | error | s |
   |---|---|---|---|
   | Coarse | 0.01 | 2.14E-2 | 7.36 |
   | Fine | 0.001 | 1.15E-2 | 347.0 |
   | MR 2 levels | fine 0.001 | 1.15E-2 | 79.9 |
   | MR 3 levels | fine 0.0001 | 6.53E-3 | 591.0 |

   MR matches uniform-fine accuracy "in less than one fourth the time".
   The error is dominated by smearing at the rarefaction corners and the
   contact.
2. **Rotating cone** (pp. 505–507, Table II). Linear rotation on
   $[-1,1]^2$ to $t = 3.375$, Lax–Wendroff without viscosity, buffer 2,
   regrid every 8 steps, tolerance 0.001, $r = 4$, one rotated subgrid
   following the cone.

   | Run | $h$ | error | s |
   |---|---|---|---|
   | Coarse | 1/20 | 5.27E-2 | 6.86 |
   | Fine | 1/80 | 9.34E-3 | 588.0 |
   | MR | fine 1/80 | 9.78E-3 | 86.6 |

   About the uniform-fine error in about 1/6 of the time; roughly 12% of
   the grid refined; about 9 s (12%) of the MR run is overhead, mostly
   error estimation and grid generation. The reduced wake behind the cone
   is taken as showing that coarse updating is necessary.
3. **2D inviscid Burgers** (pp. 507–510, Table III). Piecewise-constant
   data on the unit square (from Gropp), MacCormack, buffer 1, regrid every
   4 steps, tolerance 0.001, $r = 10$.

   | Run | $h$ | error | s |
   |---|---|---|---|
   | Coarse | 1/20 | 8.0E-2 | 0.18 |
   | Fine | 1/200 | 3.86E-2 | 155.0 |
   | MR | fine 1/200 | 2.75E-2 | 109.0 |

   MR is faster than uniform fine and has a lower error, which the authors
   attribute to the linear interpolation used when the rotated grid is
   injected onto the coarse grid, smoothing the discontinuities.

# Notation map

| Berger & Oliger | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $h_l$; $h_c$, $h_f$ | $h$, $H$ | $H = rh$ here; $H = 2h$ only at a 2:1 interface |
| $r$ (refinement ratio) | $r$ | same; **collision inside the paper:** $r(x,y)$, $s(x,y)$ are also the rotated coordinates |
| $l$ (level) | $l$ | same, 0 = coarsest |
| $k$, $k_l$ | $\Delta t$ | time step |
| $\lambda = k/h$ | words (mesh ratio) | **collision:** registry $\lambda_k$ is a characteristic speed |
| $G$, $G_l$, $G_{l,j}$ (grids) | $\Omega_h$ | **collision:** registry $G_h$ is the discrete gradient |
| $Q$, $Q_{2h}$ (scheme, coarsened scheme) | words | |
| $\tau$ (local truncation error); $q$, $q_1$, $q_2$ | words | **collision:** $\tau$ is the SBP boundary order |
| $\epsilon$ (flag tolerance), $e(x)$ (error estimate) | words | $e$ is also the Euler total energy in Example 1 |
| $M^tM$, $A$, $A_m$ (moment matrix) | words | |
| injection onto the coarse grid | $R$, by injection | not the conservative average of Berger–Colella-derived pages |
| fine boundary values from the coarse grid | $\Gamma$ | interpolation or Ciment's approximation; order unspecified |
| new-grid initialization | $P$ | interpolation; order unspecified |

# Pages created or updated

* Created this Source page.
* Updated [Block-structured AMR](/definitions/block-structured-amr.md): the rotated-grid predecessor, by name.
* Updated [Refluxing](/methods/refluxing.md): the non-conservative predecessor (injection, no flux correction).
* Updated [Berger & Colella (1989)](/sources/berger-colella-1989.md).

# Citations

1. `/home/stefano/papers/mosaic/div-free-amr/1984-JCP-Berger-1010160021-99918490073-1.pdf`.
   * **Version read.** The published journal version (Academic Press scan,
     29 pp.). Received 8 March 1983, revised 24 August 1983. Supported by
     ONR and NSF (p. 484 footnote).
   * **Identity.** doi:10.1016/0021-9991(84)90073-1, not printed on the
     paper (the PDF metadata gives the PII); checked on Crossref: title and
     authors match; J. Comput. Phys. vol. 53, issue 3, pp. 484–512, issued
     March 1984.
   * **How it was read.** Text layer by pdftotext; every equation and table
     cited was checked on page renders (pp. 490–492, 494, 497, 502–507,
     510–512). Table II's coarse error is 5.27E-2 on the 250-dpi render
     (the text layer reads 5.21). Figures (space–time mesh, subgrid
     snapshots, solution and error surfaces, data-structure schematics)
     are described qualitatively only.
   * **Recorded as printed.**
     * The two-step Richardson line prints $k^{q_2+1}$ where eq. 3.1
       implies $h^{q_2+1}$ (p. 491).
     * The moment-matrix entries print the mean terms without the factor
       $n$ (p. 498).
     * Example 1 puts the jump at $x = 0$ on the printed domain
       $0 \le x \le 1$ (pp. 502–503); Fig. 6.1 shows it near $x \approx 0.5$.
     * The internal energy $e - \tfrac12\rho u^2$ is called "per unit mass"
       (p. 503).
     * Fig. 3.3 prints the repeat count as $(h_f/h_c)^{\text{level}}$,
       which is below 1 as written; $r$ substeps per level is the evident
       intent.
     * Gottlieb is printed "Gotlieb" in the reference list, Sager "Saeger"
       (the body text has "Sager", p. 485).
   * **Reference list.** 31 entries, all merged. Harten & Hyman (J.
     Comput. Phys. 50:235) is `harten-1983-c`, not the ingested
     [Harten (1983)](/sources/harten-1983.md). Gropp is printed SIAM J. Sci.
     Statist. Comput. 1:191; the bibliography's earlier 4:191 is wrong
     (Crossref doi:10.1137/0901012 is vol. 1). Miller & Miller, SIAM J.
     Numer. Anal. 18:1019, is the new `miller-1981-b`. Gottlieb & Orszag is
     printed "Gotlieb". Oliger "to appear" is keyed `oliger-1984` (no year
     printed). Sod is the ingested [Sod (1978)](/sources/sod-1978.md).
     Key renamed `berger-1984` → `berger-oliger-1984`; the entry's note
     records that balsara-2001 prints the year 1989 and page 64 (the
     Berger–Colella citation data). The bibliography holds 3834 entries
     after this batch.

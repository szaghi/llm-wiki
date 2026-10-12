---
type: Software
title: "CASTRO"
description: "Compressible astrophysical hydrodynamics code on BoxLib/AMReX: unsplit PPM on subcycled block-structured AMR with refluxing, and a multilevel self-gravity synchronization (level solves, lagged composite correction, flux-register-driven correction solve); no divergence constraint."
status: established
aliases: [Castro]
tags: [amr, block-structured, subcycling, self-gravity, astrophysics]
timestamp: 2026-10-12T00:00:00Z
---

# CASTRO

A compressible, multicomponent Eulerian code with a general equation of
state, nuclear reactions and self-gravity, built on BoxLib, the
predecessor of [AMReX](/software/amrex.md)
([Almgren et al. (2010)](/sources/almgren-2010.md)).
* **Hydrodynamics.** Unsplit PPM with characteristic tracing and full
  corner coupling, using a limiter that keeps accuracy at smooth extrema.
  It is "formally second-order in both space and time" (§5).
* **Hierarchy.**
  * Arbitrary-size, logically rectangular grids with refinement ratio 2
    or 4.
  * Proper nesting of unions of grids, with no parent–child relation and
    a buffer of 2 cells ($r = 2$) or 1 cell ($r = 4$).
  * Subcycling in time, synchronized by volume averaging and Berger–Colella
    [refluxing](/methods/refluxing.md) (§§6.1–6.2.1).
  * The interpolation orders for ghost cells and new grids are not stated.
* **Self-gravity across levels** (§6.2.3). Subcycled level Poisson solves
  leave a mismatch in the normal gradient of $\phi_{\mathrm g}$ at
  coarse–fine boundaries. The code repairs it in two ways:
  * a lagged composite correction, exact when the density does not change;
  * at synchronization, a two-level composite correction solve driven by
    a flux register of that mismatch and by the density change from
    refluxing, followed by momentum and energy sync sources.

  This is the gravity analog of the elliptic synchronization of the
  [AMR projection method](/methods/amr-projection-method.md). No test in
  the paper exercises it with refinement (§8).
* **Parallelism** (§7). MPI and MPI+OpenMP. Grids are distributed by a
  knapsack heuristic or a Morton [space-filling curve](/definitions/space-filling-curve.md).
  * Weak scaling without gravity holds from 8 to 64 000 processors, and the
    Poisson solve scales well up to 13 824.
  * One level of refinement costs about 5–19 % over its ideal factor of 3,
    against a factor of 16 for a uniform fine grid.
* **Tests.** Sod, double rarefaction, a strong shock, Sedov–Taylor,
  Rayleigh–Taylor (split schemes show spurious secondary instabilities),
  a hydrostatic white dwarf, dust collapse and reacting bubbles (§8).

The code has no MHD and no divergence constraint. It enters this bundle
for its AMR synchronization of an elliptically coupled field.

# Citations

1. [Almgren et al. (2010)](/sources/almgren-2010.md), §§1, 5–8 (arXiv:1005.0114v1).

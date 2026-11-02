---
type: Definition
title: "Orphan points"
description: "Receptor points that need interpolation but have no valid donor: the definition, the causes the founding sources identify (insufficient overlap, hole-cutting failure, curved-surface discretization mismatch, donor qualification near boundaries), the treatments (elimination, averaging, projection, reduced stencils) and the measured counts."
status: established
aliases: [orphan, orphans, orphaned point]
tags: [domain-connectivity, donor-search, interpolation]
timestamp: 2026-11-02T11:29:00Z
---

# Orphan points

An **orphan point** is a receptor $(\mathbf i,k)\in\mathcal R_k$ that requires
interpolation but for which no suitable donor stencil exists in any
overlapping grid; the orphans of $G_k$ form the subset
$\mathcal O_k\subset\mathcal R_k$ ([point
classification](/definitions/point-classification.md)).
[Rogers et al. (2003)](/sources/rogers-2003.md), "Automation of the Oversetting
Process", define the term in exactly this way ("If a suitable donor cell
cannot be found for an interpolation point, the point is termed an
'orphan'") as part of the output of
[domain connectivity](/definitions/domain-connectivity.md);
[Lee & Baeder (2003)](/sources/lee-2003.md) use it in the same sense. A donor is
"suitable" when it lies in an overlapping grid, contains the receptor in its
donor cell, and its stencil consists of usable (non-hole, and for explicit
interpolation non-receptor) points ([donor search](/methods/donor-search.md),
[fringe points](/definitions/fringe-point.md)).

## Causes

- **Insufficient overlap.** When the overlap is too narrow for the donor
  stencil, a receptor has no donor. Lee & Baeder (2003), p. 3, note that
  implicit hole cutting removes orphans caused by hole-cutting failures but
  not those caused by insufficient overlap, which must still be checked. The
  overlap requirement itself is discussed on
  [fringe points](/definitions/fringe-point.md).
- **Hole-cutting failures.** With walls as cutters, thin bodies, mismatched or
  open surfaces produce holes that are wrong in size or leak, leaving receptors
  next to holes without valid donors; Lee & Baeder (2003), p. 3, claim that
  [implicit hole cutting](/methods/implicit-hole-cutting.md) eliminates the
  orphans "because of the failure", since walls do not cut. Rogers et al. (2003),
  Boeing 777 section and Conclusions, list the remaining failure modes of their
  automatic cutting — holes not cut inside very thin trailing edges (fixed by the
  OFFSET hole enlargement or a finer Cartesian hole map), and improper holes where
  overlapping surface grids define a curved wall ambiguously (fixed by a grid
  subset in which no holes may be cut).
- **Curved-surface discretization mismatch.** Rogers et al. (2003), "Projection
  for Viscous Grids", Figs. 6–7: overlapping surface grids on a curved wall are
  each linearly discretized and do not coincide. On a **concave** surface the
  near-wall receptors fall outside the donor grid and become orphans; on a
  **convex** surface donors are found but lie much farther from the wall than the
  receptors, feeding near-wall points outer-boundary-layer data. PEGASUS 5
  projects the receptor surface onto the donor surface and uses the shifted
  coordinates only to compute donor indices and weights
  ([PEGASUS 5](/software/pegasus-5.md)).
- **Donor qualification near boundaries.** Wide stencils disqualify donors
  near grid boundaries: with a 6-point stencil per direction the first two cells
  from each boundary cannot be donors (Lee & Baeder 2003, p. 10). Lee & Baeder
  accept reduced 4- or 2-point stencils near walls (flagged when the wall-normal
  index is below a user value, e.g. 4) rather than reject the receptor (p. 11,
  Fig. 13).

## Treatments

Rogers et al. (2003) state the PEGASUS policy: orphans "need to be
eliminated"; any left after a PEGASUS run must be investigated by the user, who
then modifies the input or the volume grids. A small number in a noncritical
region has "only a negligible effect on the solution accuracy", some flow
solvers update orphans by an averaging process because in certain situations
they cannot be eliminated, but "the best standard is to eliminate orphan points
entirely". PEGASUS 5 reduces them by surface projection and by OFFSET; in the
777 case a large number of orphans came from a too restrictive default limit on
the surface-to-surface projection distance, cured by raising it 50%.
Noack (2005) describes no orphan treatment in SUGGAR; its fallback to
zeroth-order weights when all Laplacian weights vanish next to a boundary
(§VI) concerns degenerate donors, not missing ones.

In the CMPGRD algorithm ([Chesshire & Henshaw (1990)](/sources/chesshire-1990.md),
§3.2, Step 3) a point that can be neither a valid discretization point nor
interpolated is set exterior and the classification is iterated, so there is
no orphan list; a failure shows up as further points becoming unused, in the
limit the null grid that the authors avoid by enough overlap *(compiler
check, not in the sources)*.

## Measured counts

For the Boeing 777-200 landing configuration (79 grids, 22.4 million points)
the final PEGASUS 5 system has just under 1200 orphan points against just under
5600 with PEGASUS 4 (Rogers et al. 2003, Boeing 777 section); reaching it took
eight automatic hole cutters, OFFSET 1 or 2 on nearly half the grids, a 50%
larger maximum projection distance and manual unblanking in two regions. The
OVERFLOW lift on this grid system matches the PEGASUS 4 result and is within
1.5% of experiment at approach conditions (Fig. 12); the paper does not
relate the agreement to the remaining orphans.

## Qualifications

- The founding Chimera papers have no orphan concept
  ([Benek et al. (1983)](/sources/benek-1983.md)); Benek et al. (1985), p. 324,
  only require "care ... to ensure" that the receptor lies inside its trilinear
  donor cell.
- A hole point that becomes a field point without being interpolated, on a
  moving grid, is a different failure: its value is undefined rather than
  missing a donor ([Meakin & Suhs (1989)](/sources/meakin-1989.md), §II, Fig. 3;
  [moving overset grids](/methods/moving-overset-grid.md)).

# Citations

- [Rogers et al. (2003)](/sources/rogers-2003.md) — "Automation of the Oversetting Process" (definition, elimination, averaging); "Projection for Viscous Grids", Figs. 6–7; Boeing 777 section (counts, failure modes); Conclusions.
- [Lee & Baeder (2003)](/sources/lee-2003.md) — p. 3 (orphans from failure vs insufficient overlap); pp. 10–11, Fig. 13 (stencil size, low-order stencils near walls).
- [Noack (2005)](/sources/noack-2005.md) — §VI (zeroth-order fallback for degenerate donors).
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §3.2, Step 3 (failed points set exterior; null grid).
- [Benek et al. (1985)](/sources/benek-1985.md) — p. 324 (receptor inside the donor cell).
- [Meakin & Suhs (1989)](/sources/meakin-1989.md) — §II, Fig. 3 (undefined values on uncovered points).

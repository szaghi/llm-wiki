---
type: Definition
title: "Explicit and implicit interpolation"
description: "Two kinds of receptor coupling. In explicit interpolation every donor stencil holds discretization points only, so receptors update directly but need more overlap; in implicit interpolation stencils may hold other receptors and the coupled equations are solved as a system. The page gives the costs and separates the term from compact interpolation and from single-system versus Schwarz solves."
status: established
aliases: [explicit interpolation, implicit interpolation, coupled interpolation, CGINTE, CGINT, circular interpolation]
tags: [interpolation, composite-grid, overset-grid, domain-connectivity]
timestamp: 2026-11-02T14:53:00Z
---

# Explicit and implicit interpolation

Let $(\mathbf i,k)\in\mathcal R_k$ be a receptor with donor stencil $\mathcal S_{\mathbf i}\subset G_{k'}$
and interpolation equation
$u^k_{\mathbf i}=\sum_{\mathbf j\in\mathcal S_{\mathbf i}}\alpha_{\mathbf j}u^{k'}_{\mathbf j}$
(see [inter-grid interpolation](/methods/inter-grid-interpolation.md)). The
two kinds differ only in which points the stencil may contain:

- **Explicit interpolation:** every stencil lies in the donor's discretization
  points, $\mathcal S_{\mathbf i}\subset\mathcal D_{k'}$. No interpolation
  point uses another interpolation point. Each receptor value is a direct
  weighted sum of already-updated values.
- **Implicit interpolation:** stencils may contain receptors of the donor
  grid, $\mathcal S_{\mathbf i}\cap\mathcal R_{k'}\neq\emptyset$. The
  interpolation equations are then coupled to each other and must be solved
  together as a linear system.

The distinction and the names are [Chesshire & Henshaw's (1990)](/sources/chesshire-1990.md)
(§5.2, p. 28). It is decided at grid-generation time: the
[point classification](/definitions/point-classification.md) of CMPGRD
validates a receptor only if its stencil holds points of the admissible kind
(§3.2). The two choices therefore yield different composite grids for the same
component grids.

## Trade-off

Chesshire & Henshaw (§5.2) state the trade-off as follows:

| | explicit (CMPGRD routine CGINTE) | implicit (CMPGRD routine CGINT) |
|---|---|---|
| stencil points | discretization points only | discretization and interpolation points |
| overlap | more overlap needed | less overlap, fewer grid points |
| update | direct evaluation; vectorizes easily; more efficient per update | sparse system, factored once (Yale Sparse Matrix Package), one back-substitution per update |

The overlap cost of the explicit choice follows from the classification rule:
the donor stencil must fit inside the donor's discretization region, past its
receptor lines. With implicit interpolation the stencil may reach into the
donor's receptor rows, so the grids may overlap less. See
[fringe points and overlap width](/definitions/fringe-point.md) and the overlap
measure $d$ of the
[interpolation-order requirement](/results/interpolation-order-requirement.md).

## Measured costs

- [Henshaw (1994)](/sources/henshaw-1994.md) labels the interpolation of
  the two timing runs of the fourth-order incompressible solver CGINS
  "explicit" and "implicit". Henshaw does not define the terms; the definitions above are
  Chesshire & Henshaw's. All runs
  used $5\times5(\times5)$ quartic stencils on an IBM RS/6000-530:
  - Cylinder at $Re=100$, 14,581 points, explicit interpolation: 0.024 s of
    1.5 s per step (2%) (Table V).
  - Sphere in a channel, three component grids with 10,728 interpolation
    points, implicit interpolation: 7.7 s of 45.0 s per step (17%) (Table VIII).

  Henshaw attributes the sphere's interpolation cost to the high fraction of
  interpolation points (§5.2).
- Chesshire & Henshaw (Table X, p. 56) report that in the explicit run of the
  compressible solver CGNVT, interpolation plus boundary conditions took
  longer than the interior update, because of the sparse back-solve. As
  recalled there, D. Brown reports explicit interpolation at 11% of the
  interior update in a finite-volume code on a Cray X-MP (private
  communication).

## Avoiding the coupled system by ordering

[Lee & Baeder (2003)](/sources/lee-2003.md) (p. 11, Fig. 12) use 6-point
Hermite stencils with minimum overlap, so two outer-boundary receptors of
facing grids can fall in each other's stencils. They state that implicit
(mutually coupled) interpolation is not needed, because the first and last
stencil points contribute little. Their assembler removes the coupling between
outer-boundary and hole-fringe receptors by interpolating all grid-boundary
receptors before the hole-fringe receptors. This is a sequential (ordered)
evaluation, neither the implicit solve nor a strictly explicit stencil
restriction.

## Explicit conditions in later assemblers

Later sources enforce the explicit kind at assembly time, in their own words:

- [Picard et al. (2021)](/sources/picard-2021.md) (§3.2.2, Eq. (12), after a
  report they cite) require the substrate ghost cells $\widetilde{\mathcal W}$
  and the patch ghost cells $\widetilde{\mathcal V}$ (page-local names of the
  two receptor sets) to be disjoint, $\widetilde{\mathcal W}\cap\widetilde{\mathcal V}=\emptyset$,
  while the substrate ghost cells still overlap the patch. No receptor then
  takes its value from a receptor of the other grid.
- [Sharma et al. (2021)](/sources/sharma-2021.md) (Eq. (10)) interpolate
  each fringe point from donor *field* points only. TIOGA keeps a preset
  number of field points between the two meshes' fringes, because a zero
  fringe gap "would otherwise result in a singular system of equations"
  (Fig. 4).
- [Sherer & Scott (2005)](/sources/sherer-2005.md) (§5.3) size the overlap
  as the minimum that, with a two-point fringe, prevents "circular
  interpolation, whereby interpolation donor points are also receiver points
  obtaining their data from the grid that they themselves are trying to
  update".
- [Roget & Sitaraman (2014)](/sources/roget-2014.md) (§3.5) call a donor cell
  whose vertices or centre are receptors a "low-quality donor" and resolve
  the conflict by turning those vertices into field points, or, when they are
  mandatory receptors, the served receptor into a field point.

## Other uses of the words

**Compact ("implicit") interpolation within one donor grid.** Sherer & Scott
(2005) (§2, Eq. (1)) call an interpolation formula *implicit* or *compact*
when it couples several receptors lying along one donor grid line in a
tridiagonal system, as a Padé scheme couples derivatives. The coupling is
within one donor grid; the authors explicitly exclude Chesshire & Henshaw's
cross-grid implicit interpolation by assuming adequate overlap. They found
compact interpolation the most accurate in 1-D but ill-conditioned for
general receptor distributions in several dimensions, and abandoned it (§4.2,
§6); see [high-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md).

**Single system versus overset Schwarz.** Sharma et al. (2021) (§3.2,
Algorithms 1–2) distinguish how the interpolation equations enter the
*solver*, not which points a stencil may hold. In the overset single system
(OSS) the interpolation equations of all fringe points are constraint rows of
one global linear system over all meshes, solved together with the field
equations. In overset Schwarz coupling each mesh's system is solved
separately and the fringe values are updated afterwards, in Jacobi
(additive) or Gauss–Seidel (alternating) fashion, over a number of "overset
corrector" iterations. With explicit stencils, OSS corresponds to Chesshire &
Henshaw's implicit *time stepping* with interpolation equations in the
system (§5.6), and the Schwarz variant to a lagged explicit update
*(compiler check, not in the sources)*; Sharma et al. do not use these terms.
[Horne & Mahesh (2021)](/sources/horne-2021.md) (§3.2) likewise inject the
reconstructed fringe values into the implicit velocity and pressure systems.
The accuracy and cost of the two solves are on
[incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md).

## Qualifications

- The Chimera sources do not use the terms. The tree hierarchy of
  [Benek et al. (1983)](/sources/benek-1983.md) and
  [Benek et al. (1985)](/sources/benek-1985.md) makes each embedded grid's
  outer boundary interpolate from its parent and each hole fringe from its
  child. Whether a stencil may contain a fringe point of the donor is not
  stated in either paper.
- The interpolation kind is distinct from the time-stepping kind. In explicit
  time stepping, Chesshire & Henshaw advance the interior points and then
  update the boundary and interpolation points. In implicit time stepping,
  they solve the stepping equations coupled with the interpolation equations
  through the sparse solver CGEL (§5.6, Eq. (5.9)).

# Citations

- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §3.2 (classification of interpolation points), §5.2 p. 28 (definitions, CGINTE/CGINT, trade-off), §5.6 (method of lines, Eq. (5.9)), Table X and p. 56 (costs; Brown as recalled).
- [Henshaw (1994)](/sources/henshaw-1994.md) — §4.1, §5.1.2 Table V, §5.2 Table VIII.
- [Lee & Baeder (2003)](/sources/lee-2003.md) — p. 11, Fig. 12.
- [Benek et al. (1983)](/sources/benek-1983.md) — p. 374–375, Fig. 7.
- [Benek et al. (1985)](/sources/benek-1985.md) — p. 324.
- [Sherer & Scott (2005)](/sources/sherer-2005.md) — §2, Eq. (1) (compact interpolation), §4.2, §5.3 (circular interpolation), §6.
- [Roget & Sitaraman (2014)](/sources/roget-2014.md) — §3.5 (low-quality donors).
- [Picard et al. (2021)](/sources/picard-2021.md) — §3.2.2, Eq. (12).
- [Sharma et al. (2021)](/sources/sharma-2021.md) — Eq. (10), Fig. 4, §3.2, Algorithms 1–2.
- [Horne & Mahesh (2021)](/sources/horne-2021.md) — §3.2.

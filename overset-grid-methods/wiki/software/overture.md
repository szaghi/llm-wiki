---
type: Software
title: "Overture (and its grid generator Ogen)"
description: "Henshaw's C++ framework for PDEs on composite overlapping grids and its overlapping grid generator Ogen: inputs and point classification, the per-step incremental connectivity update for moving and deforming grids with its measured cost, the P++ parallel arrays and donor-side parallel interpolation, the solvers built on it, and how other assembly papers place it."
status: established
aliases: [Overture framework, Ogen, Overture class library]
tags: [software, composite-grid, domain-connectivity, moving-grid, parallel]
timestamp: 2026-11-02T15:09:00Z
---

# Overture (and Ogen)

Overture is a C++ class library for solving partial differential equations
on [composite overlapping grids](/definitions/composite-overlapping-grid.md);
**Ogen** is its overlapping grid generator, the component that computes the
[domain connectivity](/definitions/domain-connectivity.md). The two names
are distinct: Overture is the framework that hosts mappings, grid
functions, solvers, adaptive refinement and moving grids; Ogen is one tool
in it (Henshaw's LLNL report "Ogen: an overlapping grid generator for
Overture", 1998, cited by all the papers below). The composite-grid
concepts Ogen works with are those of [CMPGRD](/software/cmpgrd.md): grids
$G_k$ given by mappings $\mathbf x=\mathbf d_k(\mathbf r)$ of the unit
square or cube, three point classes, Lagrange interpolation in the donor's
parameter coordinates. The 1990–1994 papers run CMPGRD and its Fortran
solvers; the 2006 and later papers read here run Overture and Ogen for the
same task. The ingested sources do not describe the code relation between
the two beyond this.

## Ogen: inputs and output

[Henshaw & Schwendeman (2006, §3.1)](/sources/henshaw-2006.md) state what
Ogen takes and returns:

- **Input:** a set of overlapping component grids, each boundary side
  labelled as a physical boundary, an interpolation boundary or a periodic
  boundary.
- **Hole cutting:** unused points ($\mathcal H_k$) are found by a
  "hole-cutting algorithm" that uses the physical boundaries to mark points
  exterior to the domain (see [hole cutting](/methods/hole-cutting.md)).
- **Classification:** the remaining points become discretization points
  ($\mathcal D_k$) or interpolation points ($\mathcal R_k$), with
  interpolation "generally determined by a tensor-product Lagrange
  interpolant in the parameter space of the donor grid"; ghost points carry
  the boundary conditions. The 2006 paper does not state the width $q$ it
  uses; the same author's Maxwell paper uses $q=p+1$ for a $p$th-order
  scheme for the second-order wave equation
  ([Henshaw 2006](/sources/henshaw-2006-b.md), §4).

The classification is defined on
[point classification](/definitions/point-classification.md). Two other
groups recall Ogen's overlap handling:
[Rogers et al. (2003)](/sources/rogers-2003.md) cite Ogen (1998), with Chiu
& Meakin (1995), as earlier attempts to "resize the holes and optimize the
grid overlap automatically", against which they call the
[PEGASUS 5](/software/pegasus-5.md) overlap optimization "unique" (see
[overlap optimization](/methods/overlap-optimization.md)); and
[Picard et al. (2021, §3.2.2, Eq. 12)](/sources/picard-2021.md) take their
condition for explicit interpolation (the substrate's ghost cells must not
overlap the patch's ghost cells, yet must overlap the patch) "from" the Ogen
report (see
[explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md)).

## Ogen for moving and deforming grids

**Rigid motion (Henshaw & Schwendeman 2006, §3.1, §3.4, Table 6).** During
a moving-grid computation Ogen is called at every time step after the grids
move. An optimized algorithm considers only the component grids affected by
the motion, assumes the new structure resembles the previous one, finds the
interpolation points that are no longer valid and makes a local search for
new donor candidates; if the local search fails, the full algorithm is
called. Ogen runs once per step, on the predicted grid: after the corrector
of the rigid-body integrator moves the grids slightly, the connectivity is
not recomputed, because it "is already known to second-order accuracy from
the predictor step". Points uncovered by the motion are handled outside Ogen
(see [exposed points](/definitions/exposed-point.md)). On a 2.2 GHz Xeon
desktop with 2 GB, for a Mach 1.5 shock driving a free cylinder:

| Run | Ogen update per step | Share of the step |
|---|---|---|
| moving grids, no AMR, $\approx1.56\times10^6$ points | 0.66 s | 3.7% |
| moving grids with one AMR level | 0.164 s | 4.3% |

The authors summarize the moving-grid generation as below 5% of the total
in both cases. Refinement patches are restrictions of the base-grid
mapping, so they move with their base grid and need no new connectivity
among themselves; only interpolation to grids of other base grids is
updated (§3.3; see [AMR on overlapping grids](/methods/amr-on-overset-grids.md)
and [moving overset grids](/methods/moving-overset-grid.md)).

**Deforming grids (Banks et al. 2016, §4.1, §4.3, Procedure 1).**
[Banks et al. (2016)](/sources/banks-2016.md) solve fluid–structure
interaction on deforming composite grids: after the interface points move,
Overture's hyperbolic grid generator re-marches the boundary-fitted grids
next to the interface (6, 9 or 10 normal lines in their tests), then Ogen
regenerates the connectivity ("cut holes, determine interpolation points");
Ogen also builds the initial grids in pre-processing. No timing of this
step is given. See
[fluid–structure interaction on overlapping grids](/methods/fluid-structure-interaction-on-overset-grids.md).

## The framework: parallel arrays and solvers

**Data and parallelism (Henshaw 2006, §9.4).** The Maxwell solver mx "is
implemented at a high level in C++" and "based upon the Overture class
library", with "most of the numerically intensive kernels" in Fortran 77;
the C++ overhead is "found to be negligible for any reasonable size
problem". Grid functions are P++ distributed arrays (Quinlan's A++/P++
library): each array is distributed independently as one serial array per
processor with ghost lines copied from neighbours, and P++ uses the
Multiblock PARTI library for ghost updates and block copies. Inter-grid
interpolation in parallel evaluates the Lagrange sum on the processor that
owns the donor stencil and sends the sums to the owner of the receptors,
so "there is at most one message that needs to be sent between any two
processors". Strong scaling up to 32 processors is called very good in
2-D and reasonable in 3-D, the overlapping grids scaling comparably to a
single box (Fig. 5). Memory for a 3-D pill-box grid of $10.2\times10^6$
points: 980 MB, 12.6 reals per point, of which the overlapping grid itself
takes 2.3 (17.8%); storing $\partial\mathbf x/\partial\mathbf r$ on all
grids would alone take 9 (Table 7). Interpolation takes 0.46% of a 2-D step
and 6.8% of a 3-D step (Table 6). Henshaw (2006, §11) adds that Overture
"has support for adaptive mesh refinement, moving grids and fast multigrid
solvers for elliptic equations".

**Solvers and tools named in the sources.**

| Name | Role | Source |
|---|---|---|
| Ogen | overlapping grid generator (connectivity) | Henshaw & Schwendeman (2006), Banks et al. (2016) |
| hyperbolic grid generator | regenerates boundary-fitted grids by marching from a surface | Banks et al. (2016), §4.1 |
| SmoothedPolygon mapping | smooth boundary curves (the rounded beam tip) | Banks et al. (2016), §7 |
| mx | fourth-order Maxwell solver, serial and distributed | Henshaw (2006), §9.4 |
| Cgcns | compressible-flow domain solver, one instance per fluid domain | Banks et al. (2016), §4.1 |
| Cgsm | solid-mechanics domain solver, one instance per solid domain | Banks et al. (2016), §4.1 |
| Cgmp | multi-physics controller: time stepping, interface exchange and conditions | Banks et al. (2016), §4.1 |

Banks et al. (2016, §7) state that the grids and run scripts of their
computations "are available with the Overture software". The physics of mx
is on [Maxwell's equations on overlapping grids](/methods/maxwell-equations-on-overset-grids.md);
the shock-capturing solver of Henshaw & Schwendeman is on
[shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md).

## How other sources place it

- [Lee & Baeder (2003, "Existing Connectivity Method")](/sources/lee-2003.md)
  list Overture among codes that follow the two-step explicit procedure,
  hole cutting then donor search.
- [Rogers et al. (2003, Introduction)](/sources/rogers-2003.md) list it with
  DCF3D, Beggar and FASTRAN as codes performing the functions of PEGASUS.
- [Noack (2005, §I)](/sources/noack-2005.md) describes "the Overture
  library" as supporting static and dynamic overset grids.
- [Roget & Sitaraman (2014, §1)](/sources/roget-2014.md) class Overture with
  OVERFLOW, BEGGAR, FASTRAN and elsA as solver-integrated assembly, and
  assert of the existing codes as a group a lack of modularity, mixed-mesh
  support or parallelism; Henshaw (2006, §9.4) documents distributed-memory
  operation of Overture's grid functions and interpolation, so the group
  statement does not fit Overture on parallelism *(compiler check, not in
  the sources)*.
- [Sharma et al. (2021, §3)](/sources/sharma-2021.md) cite Ogen with other
  assembly tools as approaches to which their interpolation results apply.

## Later mentions

[Kopriva et al. (2022)](/sources/kopriva-2022.md) cite Overture among the overset software that motivates their analysis of the continuous problem (§1).

## Qualifications

- Roget & Sitaraman print the authors of their Overture reference (ref.
  [11], AIAA 1999) as "L. David, W.D.H. Brown, D.J. Quinlan"; the
  bibliography records it as Brown, Henshaw & Quinlan, AIAA Paper 99-3130
  (DOI 10.2514/6.1999-3130, checked on Crossref), the Overture paper that
  Lee & Baeder, Rogers et al. and Noack also cite.
- Picard et al. print the Ogen report as a LANL report "96-3466", while
  Henshaw & Schwendeman and Banks et al. give LLNL research report
  UCRL-MA-132237; the bibliography records each as printed.
- Henshaw (2006) prints the processor type as "Zeon" (Xeon) in §9.4 and the
  Table 6 caption.

# Citations

- [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) — §1 (composite-grid lineage); §3.1 (Ogen input, hole cutting, classification, per-step optimized update with local search and fallback); §3.3 (refinement grids as restriction mappings); §3.4, Fig. 6 (one Ogen call per step, none after the corrector); Table 6 (grid-generation cost per step); ref. [45].
- [Henshaw (2006)](/sources/henshaw-2006-b.md) — §4 (width $q=p+1$); §9.4, Fig. 5 (mx on Overture, C++ and Fortran 77, P++ over Multiblock PARTI, donor-side parallel interpolation, strong scaling); §10.5, Tables 6–7 (time shares, memory); §11 (Overture's AMR, moving grids, multigrid).
- [Banks et al. (2016)](/sources/banks-2016.md) — §4.1 (hyperbolic grid generator, Ogen per step, Cgcns, Cgsm, Cgmp); §4.3, Procedure 1 (Ogen in pre-processing and in the time loop); §7 (SmoothedPolygon mapping, scripts distributed with Overture); refs. [37], [38], [44].
- [Rogers et al. (2003)](/sources/rogers-2003.md) — Introduction (Overture among connectivity codes); "Overlap Optimization" (Ogen 1998 as an earlier automatic hole-resizing attempt).
- [Noack (2005)](/sources/noack-2005.md) — §I (Overture library, static and dynamic overset grids).
- [Lee & Baeder (2003)](/sources/lee-2003.md) — "Existing Connectivity Method" (Overture among two-step codes).
- [Roget & Sitaraman (2014)](/sources/roget-2014.md) — §1 (Overture among solver-integrated assembly codes, ref. [11]).
- [Picard et al. (2021)](/sources/picard-2021.md) — §3.2.2, Eq. 12 (explicit-interpolation condition after the Ogen report, ref. [18]).
- [Sharma et al. (2021)](/sources/sharma-2021.md) — §3 (Ogen among assembly tools, ref. [63]).
- [Kopriva et al. (2022)](/sources/kopriva-2022.md) — §1.

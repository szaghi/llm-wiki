---
type: Definition
title: "Overset (Chimera) grid"
description: "A covering of the domain by independently generated, mutually overlapping component grids coupled by interpolation at receptor points, with hole points excluded; the hub page tracing the idea from Benek's Chimera and Chesshire and Henshaw's composite grids through moving and adaptive grids, NASA's production tool chain, partitioned and GPU assembly, and Chimera without hole cutting."
status: established
aliases: [Chimera grid, chimera grid scheme, chimera grid-embedding scheme, grid embedding, overlapped grid, overlaid grid, overset composite grid, composite overlapping grid, overset mesh, overlapping meshes, dynamic overset grid, synthesized grid]
tags: [overset-grid, chimera, composite-grid, domain-connectivity, interpolation]
timestamp: 2026-11-02T15:07:00Z
---

# Overset (Chimera) grid

An **overset grid** is a set $\mathcal G=\{G_k\}_{k=1}^{n_g}$ of component grids,
each generated independently and covering a subdomain $\Omega_k$, such that
$\Omega=\bigcup_k\Omega_k$ and neighbouring subdomains overlap
($\Omega_{kk'}=\Omega_k\cap\Omega_{k'}\neq\emptyset$) instead of meeting along
common boundaries. The discrete solutions on the components are coupled only
through **receptor points** $\mathcal R_k$, whose values are interpolated,
$u^k_{\mathbf i}=\sum_{\mathbf j\in\mathcal S_{\mathbf i}}\alpha_{\mathbf j}u^{k'}_{\mathbf j}$,
from a donor stencil $\mathcal S_{\mathbf i}$ of an overlapping grid $G_{k'}$;
points that lie outside $\Omega$ (inside a body) or that another grid
represents better are **hole points** $\mathcal H_k$ and are excluded. The
Chimera papers ([Benek et al. (1983)](/sources/benek-1983.md);
[Benek et al. (1985)](/sources/benek-1985.md)) call the construction *grid
embedding* or the *chimera grid scheme*; the Kreiss-school papers
([Chesshire & Henshaw (1990)](/sources/chesshire-1990.md);
[Henshaw (1994)](/sources/henshaw-1994.md)) call it a
[composite overlapping grid](/definitions/composite-overlapping-grid.md);
[Wang (1995)](/sources/wang-1995.md) writes *overlapped grids* and
[Noack (2005)](/sources/noack-2005.md) *overset composite grid*.
[Kageyama & Sato (2004)](/sources/kageyama-2004.md), §I, list the synonyms
explicitly: an overset grid "is also called overlaid grid, or composite
overlapping grid, or Chimera grid". Later sources add their own names:
[Chan (2009)](/sources/chan-2009.md), §1, calls a complex configuration "an
unstructured collection of overlapping structured grids";
[Roget & Sitaraman (2014)](/sources/roget-2014.md) and
[Horne & Mahesh (2021)](/sources/horne-2021.md) speak of overlapping
(unstructured) meshes; [Wang et al. (2021)](/sources/wang-2021.md), §III A,
of a "synthesized grid" made of component grids, used as a *dynamic* overset
grid around a rotating propeller; [Picard et al. (2021)](/sources/picard-2021.md),
§3.2.1, of a fine local **patch** superposed on an unmodified global
**substrate**.

## The name

Benek et al. (1983), p. 374, name the approach a **chimera method**, after the
composite creature of Greek mythology, because each region may carry its own
simple body-fitted grid and, in principle, its own fluid-dynamic model
(Navier–Stokes on element grids near bodies and wakes, Euler or potential flow
on the background grid; their Fig. 1). Benek et al. (1985), pp. 322–323, repeat
the etymology ("compounded of incongruous parts"). Only the Euler equations are
solved on all grids in both papers; the multi-model coupling is a stated
possibility, not a demonstration.

## Ingredients

An overset method has two parts, kept in separate codes by the Chimera
lineage (PEGASUS / PEGSUS for the grids, XMERA / XMER3D for the flow;
Benek et al. 1983, p. 376; Benek et al. 1985, p. 323) and in one code family by
CMPGRD and its solvers (Chesshire & Henshaw 1990, §§3–6):

1. **Domain connectivity** ([domain connectivity and overset grid
   assembly](/definitions/domain-connectivity.md)): classify every point
   ([point classification](/definitions/point-classification.md)) by
   [hole cutting](/methods/hole-cutting.md) or
   [implicit hole cutting](/methods/implicit-hole-cutting.md), mark the
   [fringe (receptor) points](/definitions/fringe-point.md), find their donors
   by [donor search](/methods/donor-search.md), flag
   [orphan points](/definitions/orphan-point.md), and, in the automated codes,
   apply [overlap optimization](/methods/overlap-optimization.md). Which grid
   may cut or serve which is fixed by a
   [grid hierarchy or priority](/definitions/grid-hierarchy.md). Chan (2009),
   §7, defines domain connectivity as two tasks, hole cutting plus the search
   and storage of interpolation stencils for the fringe points; Roget &
   Sitaraman (2014), §2.2, split *overset grid assembly* into six steps run
   on the flow solver's own partitions
   ([parallel and GPU overset grid assembly](/methods/parallel-overset-grid-assembly.md)).
   When grids move, assembly is repeated every step and the points uncovered
   by the motion need values
   ([exposed points](/definitions/exposed-point.md)).
2. **Inter-grid communication** in the flow solver:
   [inter-grid interpolation](/methods/inter-grid-interpolation.md), explicit or
   implicit ([explicit and implicit
   interpolation](/definitions/explicit-and-implicit-interpolation.md)), whose
   order and the overlap it needs are governed by the
   [interpolation-order requirement](/results/interpolation-order-requirement.md);
   or a flux coupling that restores conservation
   ([conservative overset interface](/methods/conservative-overset-interface.md)).
   With implicit time stepping the coupled systems are solved either as one
   system with the interpolation equations as constraint rows or grid by grid
   with lagged receptor values (Sharma et al. 2021, §3.2; see
   [incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md)).

Not every overset method removes points. Picard et al. (2021), §3.2.2, cut no
hole and deactivate no cell: the substrate cells covered by the patch keep
being integrated, the geometric detail (a cylinder, a ramp) exists only in
the patch, and the two grids exchange values only through two layers of
receptor ("ghost") cells on each side.

## Position among grid strategies

Benek et al. (1983), Introduction, p. 373, and Benek et al. (1985), p. 322,
divide the methods that reduce grid-generation effort into **grid patching**,
**grid embedding** and **grid adapting**: patched subdomains share common
boundaries ([patched grids](/definitions/patched-grid.md)), embedded ones need a
common overlap region instead. Chesshire & Henshaw (1990), §2, p. 8, regard a
patched grid as "an overlapping grid with exactly zero overlap" and argue that
overlap makes the method more flexible. They motivate composite grids by the
limits of a single mapping (§2, p. 7): forced non-uniform density, global
effect of local changes, and a necessary singularity of the mapping for
regions that are not simply the image of a square (the Jacobian of any map of
the unit square onto a disc is singular at some corners). Henshaw (1994),
§1.2, adds that overlapping grids avoid coordinate singularities (a sphere's
poles covered by two or more patches) and the metric discontinuities of
multiblock patched grids, which makes high-order accuracy easier to obtain.
Kageyama & Sato (2004), §I, reach the same dichotomy on the sphere: no single
grid is orthogonal on the whole sphere and free of both the pole singularity
and grid convergence, so the sphere is decomposed either by patched grids (no
overlap) or by overset grids (partial overlap); their
[Yin–Yang grid](/definitions/yin-yang-grid.md) is the overset choice.

Chan (2009), §2, gives the NASA Ames motivation: the general six-degree-of-freedom
relative motion of several bodies, which the abutting (patched) approach
"clearly could not satisfy"; independent generation of each grid for cell
quality (orthogonality, clustering), "typically" better than abutting grids;
and local changes (adding or removing a component) without regenerating the
whole system. Wang et al. (2021), §III A, repeat that components can be added
independently and connectivity updated locally.
[Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md), §1, place
overlapping grids between fixed-grid methods (embedded boundary, immersed
boundary and interface, fictitious domain) and boundary-conforming ones (ALE,
moving unstructured grids): most points lie on Cartesian grids, and "the
irregular boundary associated with standard Cartesian grid methods takes the
form of the interpolation boundary between overlapping grids"; they claim a
cost similar to a Cartesian embedded-boundary method, stated without a
comparison run. [Henshaw (2006)](/sources/henshaw-2006-b.md) measures
the Cartesian share: in a 2-D cylinder run with 3.8 million points, 71.4% of
the step time goes to Cartesian grids (§10.5, Table 6), and the composite grid
costs 2.3 of 12.6 stored reals per point in a 3-D run (Table 7).

[Meakin & Suhs (1989)](/sources/meakin-1989.md), §I, place Chimera in the
family of overlapping domain decompositions descended, as they recall, from
Schwarz's alternating method (cited as 1869): subdomain problems solved in
sequence, each taking its inter-subdomain boundary values from the
overlapping neighbour, iterated to convergence. What distinguishes Chimera,
they argue, is that bodies **cut holes** in neighbouring subdomains, creating
artificial hole boundaries that receive interpolated data; this two-way link
between a primary grid and a fully embedded subordinate grid is what makes
moving multi-body computation possible (their Figs. 1–2). Chesshire & Henshaw
(1990), §1, recall the parallel Kreiss-school lineage: Starius (1977) applied
the Schwarz alternating procedure to elliptic problems on two overlapping
meshes, Starius (1980) analysed Lax–Wendroff stability on an overlapping 1-D
mesh, and B. Kreiss (1983) built the grid-construction program from which
CMPGRD descends. Henshaw & Schwendeman (2006), §1, recall the two lines as
independent: the Volkov–Starius–Kreiss composite-grid line and the "Chimera
grids" that Steger and associates conceived separately. Chan (2009), §2, dates
the official start of overset development at NASA Ames to 1983, with the
Chimera framework of Steger, Dougherty & Benek (as recalled there), and notes
that overlapping meshes had been used before (e.g. wing–nacelle) without the
general framework.

## History in the founding papers

- **Two-dimensional Chimera (1983).** Benek et al. (1983) organize the grids
  in a strict [hierarchy](/definitions/grid-hierarchy.md), cut holes bounded by
  a level curve $\mathcal C$ of the embedded grid, flag hole points with a 0/1
  IBLANK array multiplied into the rows of a Beam–Warming approximate-factorization
  solver, and interpolate boundary values by the linear ($q=2$) Taylor formula
  $u^k_{\mathbf i}=u^{k'}_{\mathbf j_0}+(\partial_xu)^{k'}_{\mathbf j_0}\Delta x+(\partial_yu)^{k'}_{\mathbf j_0}\Delta y$,
  with $\mathbf j_0$ the donor point and $(\Delta x,\Delta y)=\mathbf x^k_{\mathbf i}-\mathbf x^{k'}_{\mathbf j_0}$
  the receptor's offset (their Eq. 1, which they call "first-order accurate"). Tests: Euler flow past a
  [circular cylinder](/benchmarks/flow-past-circular-cylinder.md) at
  $M_\infty=0.25$ and $0.5$, and the SKF 1.1 airfoil with and without a
  maneuver flap ([multi-element airfoils](/benchmarks/multi-element-airfoil.md)).
  The Chimera run converged three times faster than the single grid (p. 376,
  no history shown); a shock crossing the overlap boundary produced a
  mismatch that the authors provisionally blame on the non-conservative
  interpolation (pp. 376–377).
- **Three-dimensional Chimera (1985).** Benek et al. (1985) keep the hierarchy,
  switch to trilinear interpolation in the donor cell, and run transonic Euler
  flows with the [PEGSUS](/software/pegasus.md) and XMER3D codes on a Cray
  X-MP/12: a wing/body (3 grids, 65,813 points), a wing/body/tail (4 grids,
  157,540 points) and three ellipsoids (3 grids, 57,750 points).
- **Composite overlapping grids (1990).** Chesshire & Henshaw (1990) formalize
  component grids as images $\mathbf x=\mathbf d_k(\mathbf r)$ of the unit square,
  replace the hierarchy by a priority ordering of the grids, classify points
  with a signed flag that stores the donor grid, interpolate with tensor-product
  Lagrange formulas of any width $q$ in donor parameter coordinates, and prove
  how wide $q$ must be. Their generator is [CMPGRD](/software/cmpgrd.md); they
  call their overlap algorithm "fundamentally different" from those of
  B. Kreiss and Benek et al. (§3.2, p. 14).
- **Moving bodies (1989).** Meakin & Suhs (1989) run a modified PEGASUS, the
  domain connectivity function, at every time step, couple it cyclically with
  the flow solver and a (not yet implemented) body-dynamics function, and
  demonstrate [store separation](/benchmarks/store-separation.md) and Space
  Shuttle booster separation ([moving overset grids](/methods/moving-overset-grid.md);
  [DCF3D](/software/dcf3d.md) is the later code of the same function).
- **High order (1994).** Henshaw (1994) solves the incompressible
  Navier–Stokes equations to fourth order on overlapping grids with $q=5$
  interpolation and two receptor layers
  ([incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md),
  verified by [twilight-zone flow](/methods/twilight-zone-flow.md)).
- **Conservation (1995).** Wang (1995) makes the overlapped interface fully
  conservative by turning the overlap into a patched interface.
- **Automation (2003).** [Rogers et al. (2003)](/sources/rogers-2003.md)
  rewrite PEGASUS as [PEGASUS 5](/software/pegasus-5.md): hole cutting driven by
  the flow-solver boundary conditions, exhaustive donor search, donor choice by
  a cell-difference parameter, automatic overlap optimization, MPI
  parallelism; they date the approach at "over 15 years" (Introduction).
  [Lee & Baeder (2003)](/sources/lee-2003.md) drop explicit hole cutting
  altogether ([implicit hole cutting](/methods/implicit-hole-cutting.md)).
- **Spherical geometry (2004).** Kageyama & Sato (2004) cover a spherical shell
  with two identical overlapping latitude–longitude patches.
- **Unstructured and moving assembly (2005).** Noack (2005) assembles
  structured, unstructured and general polyhedral grids for node- and
  cell-centred solvers with [SUGGAR](/software/suggar.md), for moving bodies,
  and calls overset grids "a mature technology that has been used for over 20
  years" (§I), traditionally with structured grids.

## Later developments in the ingested sources

- **High-order compact schemes (2005).** [Sherer & Scott (2005)](/sources/sherer-2005.md)
  run sixth-order compact differencing with Padé filters on general overset
  grids with holes, and show that second-order interpolation caps the whole
  computation at second order
  ([high-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md)).
- **Moving grids with AMR (2006).** Henshaw & Schwendeman (2006) regenerate the
  composite-grid connectivity with Ogen at every step, give the uncovered points
  old-time values ([exposed points](/definitions/exposed-point.md)) and refine
  any component grid adaptively ([AMR on overlapping
  grids](/methods/amr-on-overset-grids.md); [shock capturing on overlapping
  grids](/methods/shock-capturing-on-overset-grids.md)).
- **Maxwell's equations (2006).** Henshaw (2006) solves the second-order form
  of Maxwell's equations to fourth order on overlapping grids in parallel
  ([Maxwell's equations on overlapping grids](/methods/maxwell-equations-on-overset-grids.md)).
- **Production tool chain (2009).** Chan (2009) reviews the NASA Ames tools:
  PLOT3D, hyperbolic surface and volume grid generators, collar grids, off-body
  Cartesian grids, PEGASUS and object X-rays, zipper grids, Chimera Grid Tools
  and [OVERFLOW](/software/overflow.md); applications range from a first Space
  Shuttle grid of a quarter-million points to one of 96 million points in 619
  zones (§11).
- **Partitioned unstructured assembly (2014).** Roget & Sitaraman (2014) assemble
  overlapping unstructured meshes on the flow solver's own partitions with local
  data only ([parallel and GPU overset grid
  assembly](/methods/parallel-overset-grid-assembly.md)).
- **Fluid–structure interaction (2016).** [Banks et al. (2016)](/sources/banks-2016.md)
  discretize both the fluid and the solid on overlapping grids whose interface
  components are regenerated every step
  ([fluid–structure interaction on overlapping grids](/methods/fluid-structure-interaction-on-overset-grids.md)).
- **2021.** Picard et al. build a finite-volume Chimera for fast transient
  compressible two-component flow without hole cutting; Horne & Mahesh move
  unstructured assembly (cutting and donor search) to GPUs; [Sharma et al.
  (2021)](/sources/sharma-2021.md) measure how interpolation order and the
  coupling of the linear systems affect incompressible accuracy; Wang et al.
  use a rotating overset grid as the ingredient of a propeller-wake study.

## Uses beyond moving bodies

Later sources also use overset grids where one grid alone cannot be well behaved: [Teschner & Mundt (2022)](/sources/teschner-2022.md) cover the symmetry axis of a blunt-body mesh, where the metric is singular, with a small overset mesh whose points coincide with the body mesh ([interpolation-free overset coupling](/methods/interpolation-free-overset-coupling.md)); [Zhao et al. (2022)](/sources/zhao-2022.md) and [Hedayat et al. (2022)](/sources/hedayat-2022.md) carry an immersed boundary on a body-attached grid ([immersed boundaries on overlapping grids](/methods/immersed-boundary-on-overset-grids.md)); [Li & Wang (2022)](/sources/li-2022.md) give each component of an array its own solver instance ([parallel overset grid assembly](/methods/parallel-overset-grid-assembly.md)). [Kopriva et al. (2022)](/sources/kopriva-2022.md) analyse the continuous problem behind every overset discretization ([well-posedness](/results/overset-well-posedness.md)).

## Grid generation for overset systems

Chan (2009), §§4–6, describes the generation side of the NASA structured
tool chain, as background work recalled by the review:

- **Hyperbolic grid generation.** Surface grids are marched from an initial
  curve on a reference surface and projected back after each step; volume grids
  are marched from the surface by hyperbolic equations (two orthogonality
  conditions and a cell-volume constraint in 3-D; Steger and co-workers, as
  recalled). The method is "one to two orders of magnitude faster than elliptic
  methods" and needs one prescribed boundary of six, but cannot place the outer
  boundary exactly, which makes it unsuitable for abutting grids and natural for
  overset ones. Surface grid generation is called "the most difficult grid
  generation step" (§5). Banks et al. (2016), §4.1, regenerate the
  interface-adjacent component grids with a hyperbolic generator at every step.
- **Collar grids.** At an intersection of two components (wing and fuselage) the
  independently generated grids blank a region in each other; a collar grid,
  whose surface grid joins two half-grids meeting at the intersection line,
  covers the junction with a single viscous-spacing direction (Steger's concept,
  as recalled, §4).
- **Off-body Cartesian grids.** Either one Cartesian grid embedding all
  near-body grids, with a uniform core spacing matched to them and stretched
  outer layers, or Meakin's multiple Cartesian blocks with refinement levels set
  by body proximity, adaptable to flow features and re-adapted as bodies move
  (§6).
- **Zipper grids.** To integrate forces and moments on overlapping surface
  grids, overlapping surface quadrilaterals are blanked until none overlap and
  the gaps filled by one layer of triangles; the integration is exact for
  constant and linear integrands. The tool (FOMOCO) handled about 10 million
  points and at most about 50 grids, with robustness degrading for very
  different overlapping resolutions (§8).

## Codes named in passing

Rogers et al. (2003) name the flow solvers that consume PEGASUS output
(OVERFLOW, NXAIR, INS3D, DXEAGLE) and the grid tools around it (Chimera Grid
Tools, with OVERGRID detecting boundary conditions and PROGRD projecting
surface grids); they and Lee & Baeder (2003) list other connectivity codes:
DCF3D, BEGGAR, FASTRAN, Overture and (Lee & Baeder) ChalMesh/Xcog. Noack (2005),
§I, distinguishes codes where assembly is integral to the solver (BEGGAR,
DCF3D) from stand-alone assemblers (PEGASUS, SUGGAR) and describes Overture as
an object-oriented library with static and dynamic overset grids. Wang (1995)
compares against the interpolation-based Chimera implemented in CFL3D.
Chan (2009), §§9–10, describes Chimera Grid Tools (library, batch utilities,
the OVERGRID interface and a Tcl script library, distributed to 500 user
organizations by March 2008) and the OVERFLOW lineage. Roget & Sitaraman
(2014), §1, list dedicated assembly codes (PEGASUS 5, SUGGAR++ with DiRTlib,
CHIMPS, PUNDIT) and solver-integrated ones (OVERFLOW, OVERFLOW-D, BEGGAR,
FASTRAN, [Overture](/software/overture.md), elsA); their own code PUNDIT is the
connectivity module of the Helios rotorcraft code. Sharma et al. (2021) assemble
with TIOGA inside the ExaWind stack (Nalu-Wind); Henshaw & Schwendeman (2006)
and Banks et al. (2016) with Ogen, the grid generator of Overture; Wang et al.
(2021) run OpenFOAM without naming its overset module.

## Collar grids and untrimmed grids

Lee & Baeder (2003), pp. 8–9 (Figs. 8–9), treat *untrimmed near-body grids*
(collar grids at junctions, grids of secondary surface features, surface
refinement grids) that cut through a body surface: under implicit hole
cutting such a grid is given `jHoleImmune` $=1$ when its interior points are
tested against partner grids, and the untrimmed grids and their partners are
identified manually.

## Qualifications

- **Order naming.** Benek et al. (1983) call their linear Taylor interpolation
  "first-order accurate"; it is exact for linear functions and is $q=2$
  (second order) in this bundle's convention (see the
  [notation registry](/notation.md)).
- **Mask conventions.** The 0/1 IBLANK of the Chimera papers and the signed
  flag of CMPGRD encode different information; the bundle writes the signed
  mask $\iota_k$ throughout
  ([point classification](/definitions/point-classification.md)).
- **Hierarchy.** The strict hierarchy of the 1983–1985 papers (each grid inside
  a single parent, siblings disjoint) was lifted in PEGASUS version 2 (Benek,
  Donegan & Suhs 1987, as recalled by Rogers et al. 2003); later tools use
  priority orderings, donor-quality criteria or body hierarchies instead
  ([grid hierarchy](/definitions/grid-hierarchy.md)).
- **Who introduced the iblank.** Chan (2009), §2, credits the 0/1 iblank array,
  "a new innovation" that turns a single-grid solver into an overset solver
  with no special logic, to Steger, Dougherty & Benek (1983), a work not
  ingested here; the pages of this bundle describe it from Benek et al. (1983) of the
  same year and group. The two attributions do not conflict.
- **Accuracy of non-conservative interpolation.** Chan (2009), §7, reports that
  early concern over non-conservative fringe interpolation "was resolved by
  Meakin", who showed (as recalled) that tri-linear interpolation keeps formal
  accuracy provided the solution is smoothly resolved by all grids in the
  overlap. The condition of smooth resolution leaves out discontinuities
  crossing the overlap, the case taken up by the
  [conservative overset interface](/methods/conservative-overset-interface.md),
  and the statement names no order of the flow scheme, whereas the
  [interpolation-order requirement](/results/interpolation-order-requirement.md)
  ties the interpolation order to it.
- Chan (2009), §12, asserts without evidence that structured grids "enjoy better
  accuracy and speed" than unstructured methods; Chan's §7 verdict that no
  connectivity software yet combined "full automation, robustness, and speed"
  dates from 2008, before Roget & Sitaraman (2014) claimed an automated,
  robust parallel assembler.

# Citations

- [Benek et al. (1983)](/sources/benek-1983.md) — Introduction, p. 373; p. 374 (chimera name, Fig. 1, hierarchy, Eq. 1); pp. 375–377 (holes, IBLANK, tests).
- [Benek et al. (1985)](/sources/benek-1985.md) — pp. 322–323 (three categories, etymology, PEGSUS/XMER3D); pp. 325–330 (grids and tests).
- [Meakin & Suhs (1989)](/sources/meakin-1989.md) — §I, Figs. 1–2 (Schwarz lineage, hole cutting as the distinguishing feature); §II (ADF/BDF/DCF).
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §1 (lineage); §2, pp. 7–8 (single-mapping limits, patched grid as zero overlap); §3.2, p. 14 (algorithm "fundamentally different").
- [Henshaw (1994)](/sources/henshaw-1994.md) — §1.2 (singularities and metric discontinuities avoided); §§4–5 (fourth-order method, $q=5$).
- [Wang (1995)](/sources/wang-1995.md) — §1 (overlapped vs patched grids); §3 (conservative interface).
- [Lee & Baeder (2003)](/sources/lee-2003.md) — pp. 2–3 (existing connectivity codes); pp. 8–9, Figs. 8–9 (untrimmed and collar grids).
- [Rogers et al. (2003)](/sources/rogers-2003.md) — Introduction (chimera grid-embedding scheme, history, codes); PEGASUS version history, pp. 1037–1038.
- [Kageyama & Sato (2004)](/sources/kageyama-2004.md) — §I (synonyms; patched vs overset on the sphere).
- [Noack (2005)](/sources/noack-2005.md) — §I (definition of the overset composite grid, maturity, codes).
- [Sherer & Scott (2005)](/sources/sherer-2005.md) — §1, §5.2 (high-order compact schemes on overset grids).
- [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) — §1 (lineage, position among moving-boundary methods); §3 (Ogen, exposed points, AMR).
- [Henshaw (2006)](/sources/henshaw-2006-b.md) — §4; §10.5, Tables 6–7 (Cartesian share of cost, storage).
- [Chan (2009)](/sources/chan-2009.md) — §1–2 (history, motivation, iblank); §§4–6 (hyperbolic, collar, off-body grids); §7 (connectivity, Meakin's result); §8 (zipper grids); §§9–12 (tools, OVERFLOW, applications, outlook).
- [Roget & Sitaraman (2014)](/sources/roget-2014.md) — §1 (codes); §2.2 (six-step assembly).
- [Banks et al. (2016)](/sources/banks-2016.md) — §4.1 (deforming composite grids, hyperbolic regeneration).
- [Picard et al. (2021)](/sources/picard-2021.md) — §3.2.1–3.2.2 (substrate and patch, no hole cutting).
- [Horne & Mahesh (2021)](/sources/horne-2021.md) — §1–2 (unstructured overset meshes, GPU assembly).
- [Sharma et al. (2021)](/sources/sharma-2021.md) — §1 (TIOGA, ExaWind); §3.2 (single-system and Schwarz coupling).
- [Wang et al. (2021)](/sources/wang-2021.md) — §III A (synthesized grid, dynamic overset grid).
- [Teschner & Mundt (2022)](/sources/teschner-2022.md) — §1, §3.
- [Zhao et al. (2022)](/sources/zhao-2022.md) — §II.
- [Hedayat et al. (2022)](/sources/hedayat-2022.md) — §1.
- [Li & Wang (2022)](/sources/li-2022.md) — §2.
- [Kopriva et al. (2022)](/sources/kopriva-2022.md) — §1.

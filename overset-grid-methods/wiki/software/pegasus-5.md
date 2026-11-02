---
type: Software
title: "PEGASUS 5"
description: "The 2003 from-scratch Fortran 90 rewrite of the PEGASUS overset connectivity preprocessor: boundary-condition-driven automation, Cartesian hole map with line-of-sight test, exhaustive ADT plus stencil-jumping donor search, cell-difference-parameter donor choice, overlap optimization, surface projection for viscous grids, restart and master–worker MPI, with its measured costs and labour savings."
status: established
aliases: [PEGASUS5, Pegasus 5]
tags: [software, chimera, domain-connectivity, hole-cutting, donor-search, parallel]
timestamp: 2026-11-02T15:09:00Z
---

# PEGASUS 5

PEGASUS 5 is a domain-connectivity preprocessor for structured
[overset grids](/definitions/overset-grid.md), written from scratch in
Fortran 90 (dynamic memory, pointers) rather than derived from
[PEGASUS 1–4](/software/pegasus.md), with automation as its design goal
([Rogers et al. 2003](/sources/rogers-2003.md), "Motivation for PEGASUS
Version 5"). For a set of $n_g$ component grids it outputs the hole points
$\mathcal H_k$, the receptor points $\mathcal R_k$ (hole-fringe and
outer-boundary points), their donor cells and interpolation coefficients,
read by flow solvers such as OVERFLOW (Introduction). Rogers et al. split
connectivity into three operations: hole cutting, identification of
interpolation points, identification of donor cells; a receptor without a
suitable donor is an [orphan](/definitions/orphan-point.md), which should
ideally be eliminated ("Automation of the Oversetting Process").

## Components

1. **Boundary-condition-driven input.** PEGASUS 5 reads the flow-solver
   boundary conditions (OVERFLOW format): solid-wall conditions define the
   hole-cutting surfaces $\mathcal C$; minimum/maximum index surfaces with no
   flow-solver condition become outer boundaries whose points need donors.
   The OVERGRID tool of Chimera Grid Tools can detect boundary conditions
   and write both inputs; a script (printed "peg setup") builds all
   PEGASUS 5 input from an OVERFLOW input file and a composite grid
   (pp. 1038–1039, 1042).
2. **Automatic hole cutting: Cartesian hole map plus line of sight.** A
   Cartesian mesh enclosing the solid surfaces is classified into fringe
   elements (cut by the surface), outside elements (painted inward from the
   corners) and inside elements (the rest). A grid point in an outside or
   inside element becomes a field or hole point; a point in a fringe element
   takes the status of a neighbouring non-fringe element it can "see"
   without crossing the surface. The test does not use surface normals and
   so tolerates surface discontinuities, but needs an air-tight surface
   (pp. 1038–1039, Figs. 2–3). Parts come from J. Steger (private
   communication) and from Chiu & Meakin (1995), as cited. Several hole
   maps ("cutters") with their own extent and resolution may be defined;
   manual hole cutting is kept for backward compatibility. Details are on
   [hole cutting](/methods/hole-cutting.md).
3. **OFFSET.** An input (default 0, global or per mesh) that also blanks
   every point within OFFSET cells of a hole point (pp. 1042–1043).
4. **Exhaustive donor search.** For each of the $n_g(n_g-1)$ ordered
   donor/receptor grid pairs, PEGASUS 5 searches donors for **every** point,
   not only fringe and boundary points, because the later overlap
   optimization may turn interior points into receptors (p. 1039). Steps:
   Cartesian and rotated bounding boxes reject disjoint pairs and points; an
   alternating digital tree (ADT), built once per mesh, gives a nearby cell;
   **stencil jumping** then inverts trilinear interpolation by Newton
   iteration for the local coordinates $\mathbf s$ relative to the current
   cell and jumps by the indicated amount until $\mathbf s\in[0,1]^3$.
   Typically 3–5 Newton inversions and 2–3 jumps are needed; a jump is
   limited to 5 cells per direction and may cross C-grid cuts and periodic
   O-grid boundaries. Interpolation is trilinear on the 8-vertex donor cell
   ($q=2$ per direction), implied by the inversion; the paper prints no
   interpolation formula. Rogers et al. call stencil jumping and its
   variants "the most commonly used approaches for finding donor cells".
   See [donor search](/methods/donor-search.md).
5. **Cell-difference parameter (CDP).** Among several candidate donors the
   one with the smallest CDP, a "qualitative measure" of the difference in
   size and orientation between receptor and donor cells, is kept; it
   replaces the prioritized link lists of earlier versions (p. 1040). The
   formula and its printed range are discussed on
   [overlap optimization](/methods/overlap-optimization.md).
6. **Overlap optimization.** After hole cutting and outer-boundary donor
   search, each grid pair interpolates its points mutually; only the
   coarser points (those interpolated from finer regions) are kept as
   receptors, receptors that are members of a donor cell are released, and
   with multiple candidates the smallest-CDP donor wins (pp. 1040–1041,
   Figs. 4–5). The principle is that the finest mesh points are kept.
   Rogers et al. call it "unique" relative to the automatic hole-resizing
   attempts of Chiu & Meakin (1995) and of Henshaw's Ogen (1998). See
   [overlap optimization](/methods/overlap-optimization.md).
7. **Surface projection for viscous grids.** Overlapping surface grids on a
   curved wall, each linearly discretized, do not coincide. On concave
   walls near-wall points find no legal donor (orphans); on convex walls
   donors are found too far from the wall, so near-wall receptors receive
   outer-boundary-layer data and the boundary-layer profile is wrong.
   PEGASUS 5 shifts the receptor grid so that its surface lies on the donor
   surface (the PROGRD method of Chimera Grid Tools), uses the shifted
   coordinates only to compute donor indices and coefficients, then
   discards them; it repeats with roles reversed for every pair of grids
   with overlapping surfaces, up to a maximum allowable projection distance
   (pp. 1041–1042, Figs. 6–7).
8. **Restart.** Only the operations depending on modified input are
   repeated, determined automatically (p. 1042).
9. **Parallelization.** Coarse-grained MPI master–worker: projections per
   grid pair, ADT construction per mesh, donor searches per grid pair, hole
   cutting and boundary-point identification per mesh are dealt out
   dynamically by the master; ordering constraints (all projections before
   all interpolations) create idle phases; the final gather and write of
   all stencils (XINTOUT) is serial. The parallel version reproduces the
   serial results (p. 1042, Fig. 8; Conclusions).

## Fringe level

Rogers et al. (2003, p. 1039) call the number of receptor layers the
"fringe level", $n_f$ in the registry; Fig. 1 shows $n_f=2$, which "has
certain advantages within the flow solver and can produce more accurate
solutions" (stated without data). One $n_f$ may be set for holes and outer
boundaries jointly or separately; not all flow solvers accept mixed values.
See [fringe points](/definitions/fringe-point.md).

## Measured performance

| Quantity | Value | Hardware, case |
|---|---|---|
| 30P30N three-element airfoil, 7 zones, 313,000 points | 65 s | one SGI R10K 250 MHz |
| 52-mesh case, 2429 operations | just under 13× on 15 processors (14 workers); speedup saturates near 14 beyond about 16 processors | — |
| Boeing 777-200 landing configuration, 79 meshes, $22.4\times10^6$ points, first run | 40 min on 16 SGI Origin processors, just over 9 CPU h, 85% parallel efficiency | SGI Origin 2000 |
| same, 48 processors | speedup 33, under 13 min | SGI Origin |
| cost shares (average of the two cases) | interpolation ~50%, hole cutting ~30%, projection 10%, overlap optimization ~5% | — |
| hole cutting | 5–15% of points blanked in a typical 3-D case; 100–200 blanked points per CPU second | SGI R10K 250 MHz |
| donor search | 2–3 donor cells found per point on average, ~10,000 donor cells per CPU second; about 5% of those found are kept | SGI R10K 250 MHz |

(Rogers et al. 2003, "Multi-Element Airfoil", "Parallelization", "Boeing
777", "Performance".) The abstract states a speedup "up to a factor of 30";
the body and Conclusions give 33 on 48 processors.

**Labour and quality.** For the 777, connectivity took 3 labour days
against 32 with PEGASUS 4, and left just under 1200 orphan points against
just under 5600 (Boeing 777 section). The case needed 8 automatic hole
cutters, OFFSET 1 or 2 on about half of the meshes, a 50% larger maximum
projection distance and manual unblanking in two regions. In general Rogers
et al. estimate about one labour day per complex 3-D case, against 10–20
days with PEGASUS 4 ("Performance"). OVERFLOW solutions on PEGASUS 4 and
PEGASUS 5 connectivity agree: no visible $C_p$ difference on the 30P30N
airfoil, and matching lift curves on the 777 with the computed lift within
1.5% of experiment at approach conditions (Figs. 10, 12). The validation
cases are on [multi-element airfoils](/benchmarks/multi-element-airfoil.md).

## Remaining failure modes

Rogers et al. (2003, 777 section; Conclusions) report two: (a) the hole map
lacks the resolution to cut points inside very thin bodies such as trailing
edges, so the hole ends too close to the edge, fixed by OFFSET or a finer
hole map (Fig. 9 shows this at the 30P30N slat trailing edge); (b) where
overlapping surface grids define a curved surface ambiguously, tiny gaps
fool the line-of-sight test and improper holes result, fixed by declaring a
grid subset in which no hole may be cut.

## Positions of other sources

- [Lee & Baeder (2003)](/sources/lee-2003.md) list PEGASUS (the conference
  version of PEGASUS 5, AIAA 2002-3186) among the codes that follow the
  two-step explicit procedure, hole cutting then donor search
  ("Existing Connectivity Method"). Their
  [implicit hole cutting](/methods/implicit-hole-cutting.md) selects donors
  by smallest cell volume and explicitly does not use the CDP (sub-item 1,
  p. 5); their user parameter that makes near-wall cells forced donors is
  stated to be "not the PEGASUS 5 OFFSET variable", since hole expansion is
  irrelevant in their method (p. 8).
- [Noack (2005, §I)](/sources/noack-2005.md) calls PEGASUS 5 "a more
  modern and automated version of the venerable Pegsus4 code" that "has not
  been applied to moving body problems"; [SUGGAR](/software/suggar.md) is
  presented against that background.
- [Chan (2009, §7)](/sources/chan-2009.md), reviewing the NASA Ames tool
  chain, summarizes the same rewrite as a "major re-engineering effort" of
  the late 1990s: hole cutting "mostly automated using uniform Cartesian
  maps", a scheme to "optimize the interpolation stencils based on cell
  size compatibility" (the CDP and overlap optimization above) and MPI
  parallelism. Chan reports that version 5.1 "is used routinely in highly
  complex configurations such as the Space Shuttle in steady-state mode",
  which agrees with Noack's remark that it was not used for moving bodies
  *(compiler check, not in the sources)*; moving-body runs of [OVERFLOW](/software/overflow.md) 2 cut holes with
  Meakin's object X-rays instead (§7). Chan names two weaknesses:
  "occasional robustness issues at component junctions with fairings", and
  a memory requirement of the uniform Cartesian maps that "can also become
  significant" when feature sizes span a large range. The second matches the
  map-resolution limit that Rogers et al. meet at thin trailing edges
  (Remaining failure modes, item a) *(compiler check, not in the sources)*. Chan states that, as of 2008, "there
  is currently still no approach and software that satisfies the combined
  requirements of full automation, robustness, and speed" for domain
  connectivity.
- [Roget & Sitaraman (2014, §1)](/sources/roget-2014.md) list PEGASUS5 among
  the dedicated assembly codes (with SUGGAR++/DiRTlib, CHIMPS and PUNDIT) and
  attribute to the existing codes as a group a lack of modularity, of mixed
  structured/unstructured support or of fine-grained parallelism, or hole
  cutting that needs user input; the statement is made for the group, not
  shown code by code. Their partitioned, solver-side assembly is on
  [parallel overset grid assembly](/methods/parallel-overset-grid-assembly.md).
  Against the group statement, Rogers et al. (2003) describe PEGASUS 5 as a
  coarse-grained MPI code, i.e. parallel over whole meshes and mesh pairs,
  the "coarse-grain parallelism" Roget & Sitaraman name *(compiler check,
  not in the sources)*.

## Later mentions

[Wang & Stern (2022)](/sources/wang-2022.md) name PEGASUS 5 with Suggar++ as the assembly packages of structured overset solvers (§1).

## Qualifications

- The CDP rule ("donor and receptor cells should be of similar size") and
  the finest-points-kept principle are stated from experience; Rogers et
  al. give no accuracy analysis of either.
- The conference version (Suhs, Rogers & Dietz, AIAA Paper 2002-3186),
  cited by Lee & Baeder and by Noack, is a distinct earlier record of the
  same code; this page cites the journal paper read.

# Citations

- [Rogers et al. (2003)](/sources/rogers-2003.md) — Introduction; "Motivation for PEGASUS Version 5"; "Automation of the Oversetting Process"; "Hole Cutting" pp. 1038–1039, Figs. 2–3; "Outer-Boundary Specification" p. 1039; "Boundary Point Interpolation" p. 1039; "Cell Difference Parameter" p. 1040; "Overlap Optimization" pp. 1040–1041, Figs. 4–5; "Projection for Viscous Grids" pp. 1041–1042, Figs. 6–7; "Restarting", "Parallelization" p. 1042, Fig. 8; "Multi-Element Airfoil", "Boeing 777", "Performance", Conclusions.
- [Lee & Baeder (2003)](/sources/lee-2003.md) — "Existing Connectivity Method"; sub-item 1 p. 5 (CDP not used); p. 8 (jHoleImmune versus OFFSET).
- [Noack (2005)](/sources/noack-2005.md) — §I.
- [Chan (2009)](/sources/chan-2009.md) — §7 (late-1990s re-engineering, Cartesian maps, stencil optimization, MPI, version 5.1 on the Space Shuttle in steady state, weaknesses, state of domain connectivity), ref. [18].
- [Roget & Sitaraman (2014)](/sources/roget-2014.md) — §1 (PEGASUS5 among dedicated assembly codes, ref. [3]; stated limitations of existing codes).
- [Wang & Stern (2022)](/sources/wang-2022.md) — §1.

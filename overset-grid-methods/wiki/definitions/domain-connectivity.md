---
type: Definition
title: "Domain connectivity and overset grid assembly"
description: "The preprocessing that turns independent component grids into a usable overset grid: the domain connectivity information it produces (hole points, receptors, donors, weights), its phases, the algorithm families of the founding codes, and the measured costs of assembly for static and moving grids."
status: established
aliases: [overset grid assembly, grid assembly, domain connectivity information, DCI, domain connectivity function, DCF, oversetting process, connectivity]
tags: [domain-connectivity, hole-cutting, donor-search, moving-grid, parallel]
timestamp: 2026-11-02T11:29:00Z
---

# Domain connectivity and overset grid assembly

**Domain connectivity** is the information that couples the component grids of
an [overset grid](/definitions/overset-grid.md): which points are hole points
$\mathcal H_k$, which are receptor (fringe) points $\mathcal R_k$, and, for each
receptor, its donor grid $k'$, donor stencil $\mathcal S_{\mathbf i}$ and
interpolation weights $\alpha_{\mathbf j}$. **Overset grid assembly** is the
process that computes it. [Noack (2005)](/sources/noack-2005.md), §I, defines the
domain connectivity information (DCI) exactly as "which points are receptor
points along with their corresponding donor members and which are hole
points"; [Rogers et al. (2003)](/sources/rogers-2003.md) name three primary
operations — hole cutting, identification of interpolation points (hole-fringe
and outer-boundary points), identification of donor cells — and call a receptor
without a donor an [orphan](/definitions/orphan-point.md);
[Meakin & Suhs (1989)](/sources/meakin-1989.md) name the module the **Domain
Connectivity Function** (DCF).

## Output

The founding codes agree on the content of the output, not on its form.
PEGSUS writes two files, the composite grid and the interpolation data
([Benek et al. (1985)](/sources/benek-1985.md), p. 325); PEGASUS 5 writes the
interpolated points with their coefficients and donor cells and the blanked
points (Rogers et al. 2003); [Lee & Baeder (2003)](/sources/lee-2003.md), p. 1,
list the receptor points (indices, grid numbers) and donor cells (one corner's
indices, grid number, and the receptor's local coordinates $\mathbf s$ in the
cell); CMPGRD's output adds the mapping derivatives $\partial r_m/\partial x_n$
and the interpolation and discretization widths
([Chesshire & Henshaw (1990)](/sources/chesshire-1990.md), §4). The flow solver
reads the point classification as a mask
([point classification](/definitions/point-classification.md)) and applies the
interpolation at each step ([inter-grid
interpolation](/methods/inter-grid-interpolation.md)).

## Phases

Noack (2005), §§II–VI, orders assembly in four phases, which the other sources
share with variations:

1. **[Hole cutting](/methods/hole-cutting.md)** — mark points inside bodies or
   superseded by another grid as $\mathcal H_k$.
2. **Fringe identification** — mark the receptor layers around holes and on
   overlap (outer) boundaries ([fringe points](/definitions/fringe-point.md)).
3. **[Donor search](/methods/donor-search.md)** — locate, for each receptor, a
   donor cell in an overlapping grid and its local coordinates $\mathbf s$.
4. **Donor stencil and weights** — choose the stencil members and compute
   $\alpha_{\mathbf j}$.

Automated codes add donor selection among several candidates and
[overlap optimization](/methods/overlap-optimization.md) (Rogers et al. 2003),
and projection of overlapping viscous surface grids before the donor search
([PEGASUS 5](/software/pegasus-5.md)).

## Algorithm families in the founding papers

- **Hierarchy-driven explicit cutting** (Benek et al. 1983, 1985;
  [PEGASUS / PEGSUS](/software/pegasus.md)): a strict
  [grid hierarchy](/definitions/grid-hierarchy.md) fixes who cuts whom and
  restricts the donor search to parent–child pairs; holes are bounded by a
  constant-index surface $\mathcal C$ of the embedded grid.
- **Priority-ordered classification** (Chesshire & Henshaw 1990, §3.2;
  [CMPGRD](/software/cmpgrd.md)): every point is assigned a status by a
  six-step iteration to a fixed point over a signed flag; exterior points are
  seeded next to physical boundaries and grow; unneeded interpolation points
  are deleted and interpolation points that can be discretized are converted;
  the authors estimate the cost at $O(n_g^2N_{\mathrm{pts}})$ operations.
- **Boundary-condition-driven automation** (Rogers et al. 2003; PEGASUS 5): the
  solid-wall boundary conditions of the flow-solver input define the hole
  cutters, a Cartesian hole map with a line-of-sight test cuts the holes,
  every point of every grid is searched against all $n_g(n_g-1)$ ordered grid
  pairs, a cell-difference parameter chooses among donors, and overlap
  optimization keeps the finest points.
- **Cell selection** (Lee & Baeder 2003;
  [implicit hole cutting](/methods/implicit-hole-cutting.md)): the two-step
  "cut, then search" procedure is replaced by a donor search for every point,
  keeping the smallest-volume cell; holes appear as a by-product, and no
  hierarchy, priority, hole optimization or tree data structure is used.
- **Tree-based cutting of general grids** (Noack 2005;
  [SUGGAR](/software/suggar.md)): octree or binary-tree Cartesian
  approximations of each body's cutting surface, a body hierarchy in which
  "siblings cut each other", node- and cell-centred fringe rules, and a
  neighbour-walk donor search through general polyhedra.

Lee & Baeder (2003), pp. 2–3, describe the common two-step procedure of DCF3D,
Overture, PEGASUS, BEGGAR, ChalMesh/Xcog and FASTRAN as: cut holes into a mask
array, extract the list of inter-grid boundary points (outer-boundary and
hole-fringe points), then search donors for that list; they identify the mask
as the main difficulty.

## Assembly as a separate code or inside the solver

PEGASUS and SUGGAR are stand-alone preprocessors; the flow-solution algorithm
is "hidden" from PEGASUS/XMERA management so almost any solver can be
substituted (Benek et al. 1983, p. 376). Noack (2005), §I, contrasts codes where
assembly is integral to the solver (BEGGAR, DCF3D); Lee & Baeder (2003) say
their implicit hole cutting can be integrated in the flow solver or run
stand-alone, and that the solver then needs only one more array dimension
(`P(i,j,k)` → `P(i,j,k,ngrid)`, p. 3).

## Static and moving grids

For a static configuration assembly runs once and is cheap relative to a
converged solution, especially when one grid system serves many flow
conditions (Meakin & Suhs 1989, §II). For bodies in relative motion it runs
every time step, coupled cyclically with the flow solver (which needs the mask
and interpolation data) and the body dynamics (which needs the loads and
supplies the positions) (Meakin & Suhs 1989, §II; Noack 2005, §VII); see
[moving overset grids](/methods/moving-overset-grid.md). Meakin & Suhs limit
the level-$(n+1)$ hole search to the points on either side of the level-$n$ hole
boundaries; Noack builds the hole-cutting and donor-search trees once in each
body's own frame and transforms query points instead of grids, and couples
SUGGAR, the flow solver and a motion controller through blocking Unix FIFOs.
Noack (2005), §I, states that PEGASUS 5 "has not been applied to moving body
problems".

## Measured cost

| Source | Case | Hardware | Cost |
|---|---|---|---|
| Meakin & Suhs (1989), Table 1 | wing/store, 2 grids, 243,906 points | NAS CRAY-2 | connectivity/flow-solver CPU time per iteration: PEGASUS 1.96, restricted DCF 0.64 |
| Meakin & Suhs (1989), Table 1 | Shuttle SRB separation, 3 grids, 357,330 points | NAS CRAY-2 | same ratio: PEGASUS 5.27, restricted DCF 2.02 |
| Chesshire & Henshaw (1990), §6.4, §6.5 | cylinder in channel, three resolutions; two-flap airfoil | IBM 3090VF | 1.6, 3.1, 7.2 s; 9.3 s |
| Lee & Baeder (2003), Example | quad tilt rotor half model, 39 grids, ≈2.5 M points | Alpha 21264, 667 MHz | ≈45 s; linear instead of cubic interpolation saves ≈20–25% |
| Rogers et al. (2003) | 30P30N airfoil, 7 zones, 313,000 points | one SGI R10K, 250 MHz | 65 s |
| Rogers et al. (2003) | Boeing 777-200, 79 grids, 22.4 M points | SGI Origin, 16 / 48 processors | 40 min (just over 9 CPU h, 85% efficiency) / under 13 min (speedup 33) |
| Noack (2005), Table 2 | wing/pylon/store, structured, 3.64 M points | Pentium 4, 2.6 GHz | setup 283 s; per step ≈15 s holes + 39 s donors + 10 s output |
| Noack (2005), Table 3 | C130 + parachute + cargo, 2 unstructured + 15 structured, 4.85 M points | same | per step ≈81 s holes + 53 s donors + 71 s output |

Rogers et al. (2003) split PEGASUS 5's time, averaged over their two cases, as
interpolation ≈50%, hole cutting ≈30%, projection 10%, overlap optimization
≈5%; a typical 3-D case blanks 5–15% of the points, at 100–200 blanked points
per CPU second, and finds 2–3 donor cells per point at ≈10,000 donor cells per
CPU second, of which ≈5% are kept. The labour cost dominated before
automation: PEGASUS 4 needed over 17,000 lines of input for a 153-grid,
33-million-point high-lift case, and the 777 connectivity took 32 labour days
with PEGASUS 4 against 3 with PEGASUS 5. Meakin & Suhs (1989) attribute the
remaining DCF cost to problem-dependent configurations and to DCF routines
that do not vectorize; in static PEGASUS runs, hole definition is typically
the most expensive task (§II).

Chesshire & Henshaw's $O(n_g^2N_{\mathrm{pts}})$ estimate and Rogers et al.'s
$n_g(n_g-1)$ grid pairs both grow quadratically in the number of grids
*(compiler check, not in the sources)*; Rogers et al. answer it with bounding-box rejection of non-intersecting
pairs and Lee & Baeder with a symmetric overlap matrix built from boundary
points first ([donor search](/methods/donor-search.md)).

## Parallel assembly

PEGASUS 5 distributes per-grid and per-grid-pair operations (projections,
tree builds, donor searches, hole cutting, boundary-point identification) from
an MPI master to workers with dynamic load balancing; the final gather of all
stencils is serial, and speedup saturates (a 52-grid case with 2429 operations:
just under 13 on 15 processors, asymptote ≈14 beyond ≈16 processors; the 777:
33 on 48 processors) (Rogers et al. 2003, Parallelization, Fig. 8). The parallel
version always reproduces the serial result (Conclusions). SUGGAR has a parallel
option for hole cutting and donor search that Noack (2005) did not use in the
reported runs.

## Qualifications

- Rogers et al. (2003) print a speedup "up to a factor of 30 for very large"
  problems in the abstract, and "a factor of 33" (body) / "over a factor of 33"
  (Conclusions) for the 777 run on 48 processors.
- Noack (2005), §VIII, prints a C130 setup total of 335 s for components of
  256, 14 and 79 s, which sum to 349 s *(compiler check, not in the sources)*.
  Its Table 2 totals (26 structured grids, 3,639,804 points, 3,411,400 cells)
  exceed the sums of the 25 listed rows (3,108,363 points, 2,899,400 cells) by
  531,441 $=81^3$ points and 512,000 $=80^3$ cells, the size of one
  $81\times81\times81$ grid not listed *(compiler check, not in the sources)*.

# Citations

- [Benek et al. (1983)](/sources/benek-1983.md) — p. 376 (PEGASUS/XMERA roles, solver hidden from management).
- [Benek et al. (1985)](/sources/benek-1985.md) — pp. 323–325 (PEGSUS input, hierarchy-restricted search, two output files).
- [Meakin & Suhs (1989)](/sources/meakin-1989.md) — §II (DCF, cyclic ADF/BDF/DCF coupling, restricted search, Table 1).
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §3.2, pp. 14–21 (composite grid algorithm, cost estimate); §4 (output); §6.4–6.5 (construction times).
- [Lee & Baeder (2003)](/sources/lee-2003.md) — pp. 1–3 (output, existing two-step procedure, solver integration); Example, p. 12 (timing).
- [Rogers et al. (2003)](/sources/rogers-2003.md) — "Automation of the Oversetting Process", "Boundary Point Interpolation", "Parallelization", "Performance", Boeing 777 section, Conclusions.
- [Noack (2005)](/sources/noack-2005.md) — §I (DCI definition, codes); §§II–VII (phases, moving bodies, FIFOs); §VIII, Tables 2–3 (timings).

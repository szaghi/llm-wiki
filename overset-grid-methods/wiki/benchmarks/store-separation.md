---
type: Benchmark
title: "Wing–pylon–store separation and related moving-body cases"
description: "The store released from a wing (with or without pylon) as the reference moving-body overset problem: Meakin and Suhs's AFATL wing and store at Mach 1.05 with steady validation and a prescribed fall, their Space Shuttle booster separation, Noack's 3.6-million-point wing/pylon/finned-store assembly with per-step timings, and Roget and Sitaraman's 15-million-cell parallel assembly scaling."
status: established
aliases: [store separation, wing/pylon/store, wing/pylon/finned-store, AFATL wing and store, SRB separation]
tags: [benchmark, moving-grid, chimera, domain-connectivity, parallel]
timestamp: 2026-11-02T15:26:00Z
---

# Wing–pylon–store separation

A store (bomb, missile, fuel tank) released from a wing, often hanging from a
pylon, is the problem for which moving [overset grids](/definitions/overset-grid.md)
were built: the store grid moves through the wing and background grids, so
holes, receptors and donors change every step and the
[domain connectivity](/definitions/domain-connectivity.md) must be
recomputed each time ([moving overset grids](/methods/moving-overset-grid.md)).
In these sources the case serves three purposes: steady validation of an
overset solver against wind-tunnel pressures, a demonstration of per-step
assembly under prescribed motion, and a scaling test of parallel assembly.
No ingested source computes a six-degree-of-freedom trajectory or compares a
trajectory with experiment.

## Meakin & Suhs (1989): AFATL wing and ogive-cylinder store

[Meakin & Suhs (1989)](/sources/meakin-1989.md), §III, Figs. 6–10,
Plate 1, Table 1:

- **Geometry.** The AFATL generic wing with NACA 64A010 section, symmetric
  about the root chord, and an ogive-cylinder store (body of revolution);
  pylon and stings are omitted.
- **Flow.** Thin-layer Navier–Stokes, $M_\infty=1.05$, $\alpha=2^\circ$,
  $Re=2.4\times10^6$ per foot; free stream at the wing grid's outer
  boundary, 10 chords away; symmetry at the root.
- **Grids.** Two overset grids, the wing grid as primary and the store
  grid as subordinate: 243,906 points, 2,090 receptors. The decomposition
  has three inter-grid boundaries: the wing's hole in the store grid, the
  store's hole in the wing grid, and the store grid's outer boundary.
- **Steady validation.** Wing alone: computed $C_p$ at three span stations
  agrees well with AEDC Tunnel 4T data. Wing with store: good agreement on
  the wing upper surface; the differences on the lower surface and on the
  store are attributed to the missing pylon and sting.
- **Prescribed separation.** From the converged steady solution, the store
  is pinned at the tail while its nose sweeps one body diameter of arc
  downward in 500 steps (150 ms); Mach contours at 0, 45 and 90 ms. No
  reference data.
- **Assembly cost.** PEGASUS run unmodified each step costs 1.96 flow-solver
  iterations; the band-restricted DCF costs 0.64 (NAS CRAY-2). See
  [DCF and DCF3D](/software/dcf3d.md).

## Noack (2005): wing/pylon/finned store

[Noack (2005)](/sources/noack-2005.md), §VIII, Figs. 3, 11–13, Table 2:

- **Geometry and grids.** Wing, pylon and a store with four fins, all on
  structured grids supplied by R. Nichols: wing (inboard, mid-span,
  outboard, two tip grids, sting, sting cap, three root grids), two pylon
  grids, store (forebody, aftbody, base, sting, root and tip grids for each
  fin) and a farfield grid; the totals row prints 26 grids, 3,639,804
  points, 3,411,400 cells. A body hierarchy (Aircraft → Wing+Pylon,
  Store) decides which grids each body cuts. No Mach or Reynolds number is
  given; no flow solution is computed.
- **Hole cutting.** Binary-tree Cartesian approximation with variable
  resolution: coarse on the wing far from the store, fine on the store and
  on the pylon bottom to resolve the small pylon–store gap (Figs. 11–12).
- **Assembly cost (prescribed store motion).** On a 2.6 GHz Pentium 4 with
  3 GB: setup 283 s (6 s grid read, 261 s binary trees, 16 s donor-search
  octree); per step about 15 s hole cutting, 39 s donor search and 10 s
  output; maximum memory about 1.0 GB.
- A static unstructured tetrahedral assembly of the same configuration is
  in Noack's earlier paper (ref. 19), as recalled in §VIII.

See [SUGGAR](/software/suggar.md) for the assembler.

## Roget & Sitaraman (2014): parallel static assembly of a wing–pylon–store

[Roget & Sitaraman (2014)](/sources/roget-2014.md), §6.2, Figs. 22–23, use
a generic wing–pylon–store configuration (their ref. [20]) only to time
their partitioned [parallel overset grid assembly](/methods/parallel-overset-grid-assembly.md),
implemented in the PUNDIT module:

- **Grids.** Three unstructured grids (the wing and two stores), 15 million
  cells, partitioned by the flow solver.
- **Runs.** 64, 128, 256 and 512 processors (Wyoming "Vortex" cluster,
  2.3 GHz AMD Opteron 6134, the hardware of their §6.1). Static assembly, no
  motion and no flow solution is reported.
- **Result.** Adaptive load re-balancing reduces the total assembly time by
  up to 80% (at 256 processors); the speed-up at 256 processors rises from
  117 without re-balancing to 213 with it, "still well below" linear. The
  speed-up is measured from total assembly time, re-balancing overhead
  included, assuming linear speed-up from a serial run to the smallest
  processor count.

The case thus measures parallel scalability of the assembly, the
complement of Noack's serial per-step timings above.

## Related moving-body demonstrations

- **Space Shuttle solid-rocket-booster separation** (Meakin & Suhs 1989,
  §III, Fig. 11, Plate 2). Orbiter, external tank and boosters without
  attach hardware, a sting modelling the orbiter plume, boosters closed with
  a spherical cap. Three grids (the tank grid primary), 357,330 points,
  10,408 receptors, eight inter-grid boundaries (two outer, six hole).
  $M_\infty=4.5$, $\alpha=2^\circ$, $Re=6.95\times10^6$ on the full-scale
  orbiter length. Prescribed booster path over the separation-motor burn
  (about 2/3 s), $\Delta t=1.36\times10^{-3}$ s, the first characteristic
  interval "resolved with 500 points"; the booster bow
  shocks interact with the orbiter bow shock and impinge on tank and
  orbiter. PEGASUS / flow solver 5.27 per step, DCF / flow solver 2.02. No
  reference data.
- **C130 cargo air drop** (Noack 2005, §VIII, Table 3, Figs. 14–15). C130
  with open doors, a parachute and a cargo box in prescribed motion: 2
  unstructured (prism/tetrahedral) and 15 structured grids, 4,846,230 points
  and 10,687,568 cells; per step about 81 s hole cutting, 53 s donor search,
  71 s ASCII output; memory about 1.8 GB.

## What the cases measure

| Source | Measured | Not measured |
|---|---|---|
| Meakin & Suhs (1989) | steady $C_p$ vs wind tunnel; assembly cost relative to the flow solver | trajectory, time accuracy of the inter-grid updates (stated as not addressed, §IV) |
| Noack (2005) | assembly time and memory per step | any flow quantity |
| Roget & Sitaraman (2014) | parallel assembly time and speed-up, 64–512 processors | any flow quantity; motion |

## Place in the literature

Meakin & Suhs (1989, refs. [2,3]) cite earlier Chimera store-separation
work by Dougherty and co-workers; it is not ingested here.
[Banks et al. (2016, §1)](/sources/banks-2016.md) name store separation
(citing Dougherty & Kuan, AIAA Paper 89-0637) as the application for which
overlapping grids were early "recognized" as useful with rigid moving
bodies. [Chan (2009)](/sources/chan-2009.md) recalls that until the late
1980s overset multi-body computations involved "very simple geometries
where each body could be described by a single structured grid", citing
the booster separation of Meakin & Suhs (1989) and Meakin's 1992
wing/pylon/finned-store computation (AIAA Paper 92-4568, not ingested)
(§4); Chan lists a "controlled store separation" from a cavity among the
1990s applications (§11, Chan's ref. [36]) and states that the
relative-motion version OVERFLOW-D, with six-degree-of-freedom dynamics,
contact detection and impact dynamics, has been used by DoD projects
involving store separation (§10; see [OVERFLOW](/software/overflow.md)).
Chan gives no case data. No ingested source compares a computed store
trajectory with experiment.

## Unstructured assembly in later work

[Xiao et al. (2023)](/sources/xiao-2023.md) compute a store separation, a helicopter and a component deployment with a parallel unstructured overset assembly embedded in a URANS solver (§4).

## Qualifications

- Noack's Table 2 lists 25 grid rows whose dimensions sum to 3,108,363
  points and 2,899,400 cells; the printed totals exceed these by exactly
  one $81\times81\times81$ grid *(compiler check, not in the sources)*.
- Meakin & Suhs do not give the grid sizes of the single-grid wing-alone
  case or the time step of the store-separation run beyond the 500 steps in
  150 ms.

# Citations

- [Meakin & Suhs (1989)](/sources/meakin-1989.md) — §II DCF and Table 1 (assembly cost); §III, Figs. 6–11, Plates 1–2 (AFATL wing and store, Space Shuttle SRB separation); §IV (time accuracy not addressed).
- [Noack (2005)](/sources/noack-2005.md) — §II, Figs. 3–4 (body hierarchy); §VIII, Figs. 11–15, Tables 2–3 (wing/pylon/finned store, C130 air drop, timings).
- [Roget & Sitaraman (2014)](/sources/roget-2014.md) — §6.1 (hardware); §6.2, Figs. 22–23 (wing–pylon–store, 15 M cells, speed-up 117 → 213 at 256 processors, up to 80% time reduction).
- [Chan (2009)](/sources/chan-2009.md) — §4 (early single-grid-per-body moving cases, refs. [3], [4]); §10 (OVERFLOW-D in store separation); §11 (controlled store separation from a cavity, ref. [36]).
- [Banks et al. (2016)](/sources/banks-2016.md) — §1 (store separation as early motivation, ref. [29]).
- [Xiao et al. (2023)](/sources/xiao-2023.md) — §4.

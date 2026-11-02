---
type: Software
title: "DCF and DCF3D (Meakin's domain connectivity function and code)"
description: "Meakin's domain-connectivity line: the 1989 Domain Connectivity Function, a modified PEGASUS run every time step and coupled cyclically to flow solver and body dynamics with a band-restricted search, and the later DCF3D code that the 2003–2005 sources list among connectivity tools, with assembly integral to the solver and object X-ray hole cutting."
status: established
aliases: [DCF, DCF3D, Domain Connectivity Function, unsteady PEGASUS]
tags: [software, domain-connectivity, moving-grid, hole-cutting, chimera]
timestamp: 2026-11-02T11:28:00Z
---

# DCF and DCF3D

**DCF** is the Domain Connectivity Function of the moving-body Chimera
method of [Meakin & Suhs (1989)](/sources/meakin-1989.md); **DCF3D** is the
domain-connectivity code that later sources ingested here attribute to Meakin and
list beside [PEGASUS](/software/pegasus.md), Beggar, FASTRAN and Overture.
The sources ingested here describe the 1989 function in detail; they describe
DCF3D only through citations, so this page records the function and what
those citations say. No source ingested here states whether the later code
descends from the 1989 function.

## The 1989 Domain Connectivity Function

Meakin & Suhs (1989, §II) build their method for "multiple bodies in
relative motion" from three functions in a cycle: the Aerodynamic Function
(the flow solver) needs hole and interpolation data from the DCF; the DCF
needs body positions from the Body Dynamics Function; the Body Dynamics
Function needs loads from the flow solver. With moving bodies the hole and
inter-grid boundary positions change in time, so the mask
$\iota_k$ (their $i_b$, 1 on field points, 0 on hole points) and the
interpolation coefficients must be recomputed every step (§II). In the
paper the Body Dynamics Function is not implemented and trajectories are
prescribed.

- **Base.** The DCF is a modified PEGASUS (the 1987 version of Benek,
  Donegan & Suhs, ref. [13]), named the "unsteady PEGASUS" (§II DCF).
- **Band-restricted search.** The hole and inter-grid boundary positions
  at level $n$ limit the search at level $n+1$: hole points are sought only
  "on either side of the time level $n$ hole boundaries" (§II DCF).
- **Hole-motion rule.** The restriction is valid only if no hole point
  becomes a field point without first having been an interpolated
  hole-boundary point; otherwise undefined values enter the field
  computation. A hole may therefore move by at most one point per step
  (Fig. 3, a 1-D illustration). The authors state that in all
  time-accurate moving-body cases examined, the time step needed by the
  physics was much smaller than this limit. The rule and later treatments
  are on [moving overset grids](/methods/moving-overset-grid.md).
- **Cost.** Per iteration, relative to one flow-solver iteration on the
  NAS CRAY-2 (Table 1):

| Case | Grids | Points | Receptors | PEGASUS / flow solver | DCF / flow solver |
|---|---|---|---|---|---|
| AFATL wing + store | 2 | 243,906 | 2,090 | 1.96 | 0.64 |
| Space Shuttle SRB separation | 3 | 357,330 | 10,408 | 5.27 | 2.02 |

  The text calls the gain "a factor of ∼3" and attributes the remaining,
  problem-dependent cost to the grid configuration and to DCF subroutines
  that do not vectorize (§II DCF). The cases are on
  [store separation](/benchmarks/store-separation.md).
- **Not addressed.** No interpolation formula, stencil or donor-search
  algorithm is given (delegated to PEGASUS), and the authors state that the
  effect of the inter-grid boundary updates on time accuracy has not been
  addressed (§IV).

## DCF3D in the later sources

- [Lee & Baeder (2003)](/sources/lee-2003.md), "Existing Connectivity
  Method": DCF3D (cited through Meakin's 2001 paper "Object X-Rays for
  Cutting Holes in Composite Overset Structured Grids") is one of the codes
  that follow the two-step procedure: an explicit hole cut producing the
  mask, hole resizing for optimum overlap, extraction of the inter-grid
  boundary point list, then donor search. As recalled by Lee & Baeder,
  Meakin's paper summarizes the hole-cutting alternatives (mark-and-fill,
  surface normal vectors, ray casting, hole map) and its object X-rays
  combine a hole map with ray casting. See
  [hole cutting](/methods/hole-cutting.md).
- [Rogers et al. (2003)](/sources/rogers-2003.md), Introduction: DCF3D
  (cited through the same 2001 paper) is among the codes that "perform the
  same basic functions as PEGASUS", each producing interpolation data with
  "some level of automation". Rogers et al. also credit part of the PEGASUS
  5 Cartesian hole map to Chiu & Meakin (1995) and name Chiu & Meakin among
  earlier attempts to resize holes and optimize overlap automatically
  ("Hole Cutting", "Overlap Optimization"); see
  [PEGASUS 5](/software/pegasus-5.md) and
  [overlap optimization](/methods/overlap-optimization.md).
- [Noack (2005)](/sources/noack-2005.md), §I: Beggar and DCF3D (cited
  through Meakin's 1991 paper "A New Method for Establishing Intergrid
  Communication Among Systems of Overset Grids") are structured-grid codes
  suitable for moving bodies "where the overset assembly process is
  integral to the CFD solver", in contrast with the separate-process
  [SUGGAR](/software/suggar.md).

## Qualifications

- The the sources give no algorithm, timing or version information for
  DCF3D itself; every statement above about DCF3D is a citing source's
  characterization.
- Meakin & Suhs (1989, p. 646) state the time-step comparison twice. The
  first sentence reads "the time-step sizes required to accurately resolve
  the physical processes being simulated are generally much smaller than
  the time-step limits imposed by the DCF search restriction"; the second
  reads "the time-step size limitation imposed by the DCF search limits are
  generally much less than those required to accurately resolve the
  physical processes being simulated". Read literally, the two say
  opposite things. This page reports the first, which the paper follows
  with "This has been the case for all of the time-accurate moving body
  cases examined to date".

# Citations

- [Meakin & Suhs (1989)](/sources/meakin-1989.md) — §I; §II (ADF/BDF/DCF cycle, $i_b$, DCF modification, Fig. 3 hole-motion rule, Table 1); §IV (time accuracy not addressed); ref. [13].
- [Lee & Baeder (2003)](/sources/lee-2003.md) — "Existing Connectivity Method" pp. 2–3; ref. [2].
- [Rogers et al. (2003)](/sources/rogers-2003.md) — Introduction; "Hole Cutting"; "Overlap Optimization"; Refs. 3, 17.
- [Noack (2005)](/sources/noack-2005.md) — §I; ref. 13.

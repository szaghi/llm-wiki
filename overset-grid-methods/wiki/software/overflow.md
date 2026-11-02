---
type: Software
title: "OVERFLOW (OVERFLOW-D, OVERFLOW 2)"
description: "NASA's structured overset compressible Navier–Stokes solver: its 1989 origin as Buning's iblank rewrite of Steger's F3D scheme, the relative-motion branch OVERFLOW-D with six-degree-of-freedom dynamics and contact detection, their 2001 merger as OVERFLOW 2, and its use as the consumer of PEGASUS connectivity and of object X-ray hole cutting."
status: established
aliases: [OVERFLOW-D, OVERFLOW 2, OVERFLOWD]
tags: [software, chimera, compressible, moving-grid, parallel]
timestamp: 2026-11-02T14:54:00Z
---

# OVERFLOW

OVERFLOW is the structured [overset grid](/definitions/overset-grid.md) flow
solver of the NASA Ames line: a two- and three-dimensional compressible
viscous solver that works on a set of overlapping curvilinear grids $G_k$
with the 0/1 IBLANK mask (the registry's $\iota_k$ restricted to hole and
non-hole) and receptor lists supplied by a
[domain-connectivity](/definitions/domain-connectivity.md) step. The only
ingested account of its history is the review of
[Chan (2009, §10)](/sources/chan-2009.md); the PEGASUS 5 paper of
[Rogers et al. (2003)](/sources/rogers-2003.md) uses it as the solver
behind its validation cases. No ingested source prints its equations,
discretization or convergence data; this page records lineage,
capabilities as stated, and its role in the tool chain.

## Lineage (Chan 2009, §10)

| Version | Date | Change, as Chan recalls it |
|---|---|---|
| OVERFLOW | 1989 | Buning rewrites Steger's two-factored flux-split F3D scheme "with the overset grid framework (implementing iblank arrays)"; the Pulliam–Chaussee diagonal scheme "was quickly added" for faster turnaround |
| OVERFLOW | "subsequent development years", continuing in 2009 | boundary conditions applicable in any of the three coordinate directions; further numerical schemes, turbulence models, species-convection schemes, diagnostics and error checks; code optimization and MPI parallelization |
| OVERFLOW-D | early 1990s | Meakin adds prescribed motion, six-degree-of-freedom dynamics, body contact detection and impact dynamics, for DoD moving-body problems (rotorcraft, store separation, missiles) |
| OVERFLOW 2 | 2001 | Buning merges OVERFLOW and OVERFLOW-D into one code |

Chan dates the start of OVERFLOW to the Space Shuttle ascent analysis that
followed the 1986 Challenger accident, the program that also produced the
hyperbolic grid generators HYPGEN and SURGRD and that Chan calls the first
application of the structured overset method to a real engineering problem
(§11). The incompressible counterpart at Ames is the INS series, which Chan
mentions but leaves to another review (§10). Chan reports that OVERFLOW, like
Chimera Grid Tools, "has also been distributed to hundreds of organizations"
under non-disclosure agreements, and calls it "one of the most efficient flow
solvers in use by the CFD community today" (§10); no measurement is given
for the latter.

**The iblank mechanism.** The overset framework of the 1989 rewrite is the
iblank array: an integer per grid point, 0 for a blanked (hole) point and 1
for a field point, "introduced into the differencing stencils" so that a
single-grid solver becomes an overset solver "with no special logic" to
avoid computing on blanked points (Chan 2009, §2). How the early Chimera
solvers used the mask in their implicit operators is on
[point classification](/definitions/point-classification.md).

## Role in the tool chain

- **Consumer of PEGASUS connectivity.** Rogers et al. (2003, Introduction)
  list OVERFLOW first among the solvers that read
  [PEGASUS](/software/pegasus.md) output, and
  [PEGASUS 5](/software/pegasus-5.md) takes the flow-solver boundary
  conditions in OVERFLOW's format as its own input: solid walls define the
  hole-cutting surfaces, index surfaces without a boundary condition become
  outer boundaries needing donors (pp. 1038–1039). Chan (2009, §11) names
  OVERFLOW, Chimera Grid Tools and PEGASUS 5 as the Ames suite in use for
  NASA programs (Constellation, Space Shuttle operations).
- **Integrated connectivity for moving bodies.** In OVERFLOW 2 moving-body
  computations, holes are cut with Meakin's object X-rays: a fine 2-D
  Cartesian map over the body with rays cast normal to it, whose stored
  surface pierce points decide inside/outside by one comparison per point;
  Chan reports the method "routinely used" there, with the drawbacks that
  X-rays are generated manually and the user lists the grids each X-ray cuts
  (§7; see [hole cutting](/methods/hole-cutting.md) and
  [DCF and DCF3D](/software/dcf3d.md)). Accordingly,
  [Roget & Sitaraman (2014, §1)](/sources/roget-2014.md) class OVERFLOW and
  OVERFLOW-D among codes with assembly integrated in the solver, as
  distinct from dedicated assemblers such as PEGASUS5 and SUGGAR++.
- **Moving bodies.** OVERFLOW-D's dynamics and contact capabilities are
  illustrated in a dart-dispenser problem (Chan 2009, §11, Fig. 8); see
  [moving overset grids](/methods/moving-overset-grid.md) and
  [store separation](/benchmarks/store-separation.md).

## Computations reported with it

| Case | What is reported | Source |
|---|---|---|
| 30P30N three-element airfoil, 7 zones, 313,000 points | $M_\infty=0.2$, $Re=9\times10^6$, $\alpha=8.1^\circ$; no visible $C_p$ difference between PEGASUS 4 and PEGASUS 5 connectivity; suction peaks above experiment | Rogers et al. (2003), Figs. 9–10 |
| Boeing 777-200 landing configuration, 79 meshes, $22.4\times10^6$ points | $M_\infty=0.2$; lift curves on PEGASUS 4 and 5 connectivity agree; lift within 1.5% of experiment at approach conditions; maximum lift not predicted | Rogers et al. (2003), Fig. 12 |
| Space Shuttle launch vehicle | grids grew from about $0.25\times10^6$ points to $16\times10^6$ and then $96\times10^6$ points in 619 zones | Chan (2009), §11, Fig. 2 |
| CH-47 tandem-rotor helicopter, forward flight | OVERFLOW 2 coupled with a rotorcraft comprehensive analysis code; pictures only | Chan (2009), §11, Fig. 9 |

The airfoil case is on
[multi-element airfoils](/benchmarks/multi-element-airfoil.md). Chan's
further applications (SOFIA, Harrier in ground effect, F/A-18 tail buffet,
V-22 tiltrotor, turbopumps, the Columbia debris analysis, the Apollo launch
escape vehicle) are listed without data and are not attributed to a
specific solver version in every case.

## Future work as stated (Chan 2009, §12)

Chan expects the search for "faster and more robust numerical algorithms"
to continue in a code that has grown large, and names the scaling of the
current load-balancing scheme with processor count, and its effect on
convergence, as an issue "to be examined carefully"; software maintenance
and automatic regression testing are the other items.

## Qualifications

- Every statement on this page about OVERFLOW's algorithms is a recalled
  history in a review without equations; scheme details (F3D flux
  splitting, the diagonal scheme, turbulence models) are not read here from
  primary sources.
- Chan's reference list prints the F3D co-author once as "Shiff LB"
  (ref. [27]) and once as "Schiff LB" (ref. [39]).

# Citations

- [Chan (2009)](/sources/chan-2009.md) — §2 (iblank in the differencing stencils); §7 (object X-rays in OVERFLOW 2 moving-body runs); §10 (OVERFLOW lineage, F3D, diagonal scheme, OVERFLOW-D, OVERFLOW 2, distribution, INS series), refs. [25]–[30]; §11, Figs. 2, 8, 9 (Space Shuttle, dart dispenser, CH-47; Ames suite in NASA programs); §12 (future work).
- [Rogers et al. (2003)](/sources/rogers-2003.md) — Introduction (solvers fed by PEGASUS); pp. 1038–1039 (OVERFLOW boundary-condition format as PEGASUS 5 input); "Multi-Element Airfoil", "Boeing 777", Figs. 9–12 (OVERFLOW solutions).
- [Roget & Sitaraman (2014)](/sources/roget-2014.md) — §1 (OVERFLOW and OVERFLOW-D among solver-integrated assembly codes, refs. [7], [8]).

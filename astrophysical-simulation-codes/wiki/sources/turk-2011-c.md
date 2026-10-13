---
type: Source
title: "Turk et al. (2011) — yt: A Multi-Code Analysis Toolkit for Astrophysical Simulation Data"
description: "Software paper of yt, a Python and C toolkit that reads the output of several AMR codes through per-code frontends into one data model (lazy hierarchy, data containers, derived fields), with adaptive projections, slicing, volume rendering, profiles and analysis modules, MPI parallelism through mpi4py, and in-line embedding in Enzo."
resource: "doi:10.1088/0067-0049/192/1/9"
source_kind: paper
authors: [Turk M.J., Smith B.D., Oishi J.S., Skory S., Skillman S.W., Abel T., Norman M.L.]
year: 2011
venue: "Astrophys. J. Suppl. 192:9"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2011-ApJS-Turk-1010880067-004919219.pdf"
tags: [software, analysis, amr, scaling, performance]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper presents yt, an open-source Python toolkit with core routines in
C for analysing and visualizing astrophysical simulation output. It was
built first for [Enzo](/software/enzo.md) and generalized to other codes
through per-code "frontends" (§1, §4). Its data model opens a data set
cheaply, builds the AMR hierarchy of grid patches lazily, and lets the
user address physical regions through "data containers" (spheres, prisms,
disks, rays, slices, clumps) and recursively defined "derived fields",
hiding grid patches, files and refinement overlap (§2.1–§2.2). On top sit
adaptive projections, slices, oblique cutting planes, CPU ray-casting
volume rendering (§3), weighted profiles (§2.5) and analysis modules
(halo finding and profiling, merger trees, two-point functions, light
cones, level-set clump finding; §7). Parallelism is MPI through mpi4py,
the same serial script running unchanged in parallel; profiles scale to
128 processors and adaptive projections to 64 on a
$5.5\times10^8$-cell Enzo data set (§5). An embedding interface runs yt
in-line inside Enzo (§6). The paper is analysis software: it describes no
solver, and its only measurements are two strong-scaling studies.

# Key claims

1. **Codes supported** (§1, §4, §8). yt was "originally designed
   exclusively for analyzing data from the AMR code Enzo"; at publication
   it works "natively" with Orion, [FLASH](/software/flash.md), Chombo and
   [RAMSES](/software/ramses.md); ART and Gadget support is in progress
   (§4); Pluto and ZEUS-MP are stated future targets (§8).
2. **Frontend contract** (§4.1). A code is "supported" when (1) its fluid
   quantities and domain information map to the common yt format
   "(typically cgs)", (2) its on-disk data are mapped and localized (for
   AMR codes, grid patches or blocks), and (3) readers exist for whole
   patches or subsets. Code-specific parts are subclasses in
   `yt.frontends.<code>`; analysis then becomes "agnostic to the
   simulation code", so different codes can be compared with identical
   analysis implementations (§1, §4.1, §9).
3. **Octree data coalesced into patches** (§4.1). For RAMSES and other
   octree codes yt coalesces cells into patches with "the mechanism used
   by Enzo to create subgrid patches": cell-count histograms along each
   axis, cuts at zeros and then at the strongest zero crossings of the
   second derivative, recursively until the fraction of fine cells
   exceeds an efficiency factor "typically set to be 0.2".
4. **Data model** (§1, §2.1). The hierarchy is built only on first access;
   data containers load on demand and return the finest available values,
   with covered coarser cells masked; grid patches obey the same protocol.
5. **Derived fields** (§2.2, eq. 1). Fields are NumPy functions of other
   fields with unit metadata; a field may request ghost cells from
   neighbouring grids through covering grids, which enables
   finite-difference fields such as the velocity divergence.
6. **Covering grids** (§2.4). Fixed-resolution arrays filled coarsest to
   finest; a "smoothed" variant interpolates each level trilinearly before
   overwriting with the next and "does not explicitly perform the
   crack-fixing method" of Kaehler et al. (2005).
7. **Adaptive projections** (§3.2, eqs. 4–5). Line integrals are stored as
   a flat list of finest-resolution image-plane points, computed level by
   level with child masks, two levels at a time; for the Santa Fe Light
   Cone data set this needs "less than 1%" of the storage of a
   full-resolution image of $2^{30}$ values.
8. **Volume rendering** (§3.5). CPU ray casting over non-overlapping
   bricks (the homogenization step being the most expensive),
   vertex-centred data, five samples per cell by default, trilinear
   interpolation and an emission–absorption update per colour channel
   without scattering.
9. **Particles and generic format** (§4.2–§4.3). Enzo and FLASH store
   particles with the finest grid patch containing them; Orion stores
   sink and star particles in a separate file; cloud-in-cell deposit and
   interpolation are provided. An HDF5-based generic gridded format lets
   unsupported codes be converted.
10. **Parallelism** (§5). MPI through mpi4py; unordered tasks iterate over
    grids assigned to minimize file overhead; spatial tasks (projections)
    decompose the image plane into prisms along the full line of sight.
    Serial scripts run unchanged in parallel.
11. **In-line analysis** (§6). An embedded Python interpreter per MPI task
    wraps simulation memory, with no inter-task data movement and so no
    spatial decomposition; available only for Enzo at publication.
    Motivation: Population III data dumps of "as much as 10 gigabytes per
    time step".
12. **Clump finding** (§7.7). Recursive grid-by-grid level-set labelling
    with a one-cell buffer and a join tree across grids; a boundedness
    test compares kinetic with pairwise gravitational energy (optionally
    adding thermal energy), run in C or on the GPU through PyCUDA.

# Tests

The only quantitative measurements are two strong-scaling studies on the
Triton Resource (SDSC), on the Santa Fe Light Cone data set at redshift 0
($512^3$ root grid, six refinement levels, $5.5\times10^8$ computational
elements):
1. **Profiles** (§5.1, Fig. 5): 1D and 2D profiles show "nearly ideal
   strong scaling up to 128 processors, at which point overhead
   dominates", against ideal lines calibrated at 16 processors; 1D
   profiles are slower because 1D histogramming is pure Python and 2D a
   hand-coded C routine.
2. **Adaptive projections** (§5.2, Fig. 6), with and without disk input
   (a density field and a field of 1.0): algorithmic overhead dominates
   input; strong scaling from 4 to 64 processors, deviation at 128. Enzo
   and Orion write one file per processor with load-balanced, not
   spatially local, grids, so image-plane decomposition makes each
   processor read many files.

Timings are plotted only; no numeric times are printed. Figs. 2–4 and the
halo-profiler table (§7.2) are illustrations without verification content.

# Notation map

| Paper | Canonical | Note |
|---|---|---|
| $v_x$, $v_y$, $v_z$; $V$ (eq. 1) | components of $\mathbf v$; $\vert\mathbf v\vert$ | **collision**: $V$ is also a bin average (eq. 3) and a projected sum (eq. 4) |
| $v_i$, $w_i$, $V_j$ (eqs. 2–3) | in words | generic field value and weight, not velocity |
| $r$ (§3.2) | $r_{\mathrm{ref}}$ | refinement factor |
| $l$, $L$ (§2.4) | $l$ | refinement level; $L$ the target level |
| $dx$, $dy$, $dz$ | $h_l$ per direction | cell widths |
| $\alpha$ (eq. 6), $j_i$, $\alpha_i$ (§3.5) | in words | area ratio; emission and absorption; **collision** with $\alpha_{\mathrm L}$, $\alpha_{\mathrm c}$ |
| $\mathbf n$, $\mathbf c$, $d$ (eqs. 8–14) | in words | cutting-plane geometry; **collision**: $d$ is the number of dimensions |
| $N$ (§7.7) | in words | cells in a level set; **collision** with $N$ |
| $G$, $k$, $T$, $\gamma$ | $G$, $k_{\mathrm B}$, $T$, $\gamma$ | |
| $D_C$, $D_H$, $D_A$, $\Omega_M$, $H_0$, $z$ (eqs. 15–17) | in words | cosmological distances; not used in concept pages |

# Pages created or updated

* Created this Source page.
* Updated [Enzo](/software/enzo.md) (batch-10 section: yt's origin in Enzo,
  in-line analysis, the shared patch-clustering mechanism, particle
  storage and output layout).
* Updated [FLASH](/software/flash.md) (batch-10 section: one line on yt
  support).
* Updated[RAMSES](/software/ramses.md),
  [IDEFIX](/software/idefix.md).
* No Software page for yt: the bundle's scope (bundle law) covers
  simulation codes and their physics modules, not analysis tooling.

# Citations

1. Turk M.J., Smith B.D., Oishi J.S., Skory S., Skillman S.W., Abel T.,
   Norman M.L. (2011), "yt: A Multi-Code Analysis Toolkit for Astrophysical
   Simulation Data", Astrophys. J. Suppl. 192(1):9,
   doi:10.1088/0067-0049/192/1/9. Local file:
   `/home/stefano/papers/mosaic/astrophysical-simulation-codes/2011-ApJS-Turk-1010880067-004919219.pdf`.
   * **Version read.** The typeset publisher PDF (IOP, © 2011 AAS,
     16 pages); received 2010 October 6, accepted 2010 November 17,
     published 2010 December 28. Not a preprint. The preprint is
     arXiv:1011.3514 (posted 2010-11-15, seven authors; checked on the
     arXiv API, not printed in the PDF). No yt version number is printed.
   * **Identity.** Checked on Crossref: title, the seven authors in order,
     vol. 192, issue 1, article 9, online 2010-12-28, print 2011-01. The
     slug follows the issue year.
   * **How it was read.** Text extraction of all sections; eqs. 4–14 and
     the unnumbered volume-rendering and boundedness formulas checked on
     rendered pages 6–8 and 14. Eqs. 15–17 read from the text layer only
     and not reproduced.
   * **Recorded as printed.** Eq. 11 has a misplaced parenthesis; §7.7
     says "$n$ is the number of cells" while the inequality uses $N$; the
     text cites Pascucci & Cole-McLaughlin (2002) while the reference list
     prints 2003.
   * **Reference list:** 54 printed entries (Crossref also 54). The
     arXiv:1008.2801 entry is the SciDAC 2010 MAESTRO, CASTRO and SEDONA
     paper, `almgren-2010-b`; Collins et al., arXiv:1008.2402, is
     `collins-2010-b`, "distinct from collins-2010 (ApJS 186:308)";
     Agarwal & Feldman is "printed as "MNRAS, 1530" with no volume
     number"; Pascucci & Cole-McLaughlin is kept as printed, 2003
     (`pascucci-2003`); Norman et al.'s Petascale Computing chapter is
     merged into `norman-2007`. `turk-2011-b` (Turk & Smith, "ArXiv
     e-prints", cited by Bryan et al. 2014) is not this paper's preprint;
     its note is revised accordingly. [Hunter (2007)](/sources/hunter-2007.md) is cited
     (`hunter-2007`). Bibliography: 2522 entries.

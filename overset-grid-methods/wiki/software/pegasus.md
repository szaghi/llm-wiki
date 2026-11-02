---
type: Software
title: "PEGASUS (PEGSUS) versions 1–4"
description: "The AEDC Chimera domain-connectivity preprocessor from its 2-D origin with the XMERA solver (1983) through the 3-D PEGSUS with XMER3D (1985) to PEGASUS 4 (1991): what it computes, the hierarchy restriction of the early versions, its per-step cost in moving-body use, and the manual effort that motivated PEGASUS 5."
status: established
aliases: [PEGASUS, PEGSUS, PEGASUS 4, Pegsus4, PEGSUS 4.0]
tags: [software, chimera, domain-connectivity, hole-cutting]
timestamp: 2026-11-02T11:28:00Z
---

# PEGASUS (PEGSUS) versions 1–4

PEGASUS is the preprocessor of the Chimera method: it takes independently
generated structured component grids $G_k$ and the information on how they
are embedded, and computes the hole points $\mathcal H_k$, the receptor
points $\mathcal R_k$ with their donor stencils $\mathcal S_{\mathbf i}$ and
interpolation coefficients, i.e. the
[domain connectivity](/definitions/domain-connectivity.md) of the
[overset grid](/definitions/overset-grid.md). A separate flow solver then
reads this data. The code was introduced with the 2-D Chimera method by
[Benek et al. (1983)](/sources/benek-1983.md), extended to 3-D as PEGSUS by
[Benek et al. (1985)](/sources/benek-1985.md), made to run every time step for
moving bodies by [Meakin & Suhs (1989)](/sources/meakin-1989.md), and
rewritten from scratch as [PEGASUS 5](/software/pegasus-5.md) (Rogers et
al. 2003). This page covers versions 1–4; the rewrite has its own page.

**Name as printed.** Benek et al. (1983, p. 376) print PEGASUS, "named after
the winged horse that was critical in managing the chimera". Benek et al.
(1985, p. 323) print PEGSUS; the user's manuals of versions 3.0 and 4.0 are
cited as "PEGSUS 3.0/4.0" by [Rogers et al. (2003)](/sources/rogers-2003.md)
(Refs. 13–14) and [Noack (2005)](/sources/noack-2005.md) (ref. 7, "PEGSUS 4.0
User's Manual", and "the venerable Pegsus4 code" in §I). Meakin & Suhs (1989)
and Rogers et al. (2003) write PEGASUS. All denote the same code family.

## Code family and division of labour

- **2-D origin: PEGASUS + XMERA.** Benek et al. (1983, "Computer Codes",
  p. 376): PEGASUS takes the separately generated grids and the hierarchy
  data, combines the grids and computes the interpolation and hole-flag
  data; its output is the input of XMERA, which manages the grid and
  solution data on each mesh and directs the solution through the grid
  hierarchy. The flow algorithm is "hidden" from these management
  functions, so almost any solution algorithm can be substituted with
  minimal code change.
- **3-D: PEGSUS + XMER3D.** Benek et al. (1985, "Implementation",
  p. 323) split the procedure the same way: PEGSUS takes the grids plus the
  embedding hierarchy and writes two files, the composite grid and the
  interpolation data (p. 325); XMER3D solves the Euler equations on the
  composite mesh.
- **Moving bodies: unsteady PEGASUS (DCF).** Meakin & Suhs (1989, §II) run a
  modified PEGASUS every time step as the Domain Connectivity Function of
  their moving-body method (see [DCF3D](/software/dcf3d.md) and
  [moving overset grids](/methods/moving-overset-grid.md)). Noack (2005,
  §I) states that the PEGASUS codes, separate from the flow solver, have been
  used for static and, "by using scripts", moving-body simulations, citing
  Meakin & Suhs among the latter.
- **Flow solvers fed.** Rogers et al. (2003, Introduction) list OVERFLOW,
  NXAIR, INS3D and the cell-centred DXEAGLE as solvers that have used
  PEGASUS output.

## What the early versions compute

**Grid hierarchy.** The 1983 and 1985 codes impose the embedding hierarchy
of [grid hierarchy and priority](/definitions/grid-hierarchy.md): every grid
of level $\ell$ lies wholly inside a single grid of level $\ell-1$, and grids
of the same level are disjoint (Benek et al. 1983, p. 374, Fig. 3; Benek et
al. 1985, p. 323, Fig. 1). The hierarchy is stored as a graph (a tree) whose
edges are the only communication lines, and its stated main advantage is that
it restricts the donor search to parent–child pairs (Benek et al. 1985,
p. 323). Benek et al. (1983) already call the general graph, in which a grid
may connect to several grids of the previous level, "an important
generalization" for future versions.

**Holes and fringe.** A level surface $\mathcal C$ of the embedded grid
$G_{k'}$ ($\ell(k')=\ell(k)+1$) is the hole boundary in the enclosing grid
$G_k$; points of $G_k$ inside $\mathcal C$ are found by a bounding-radius
pre-test followed by the sign of the outward normal at the closest point of
$\mathcal C$ (Benek et al. 1983, p. 375, Figs. 5–6; Benek et al. 1985,
p. 324, six steps). Non-hole nearest neighbours of hole points form one
fringe layer ($n_f=1$) interpolated from $G_{k'}$; the outer boundary of
$G_{k'}$ is interpolated from $G_k$. The algorithms are on
[hole cutting](/methods/hole-cutting.md) and
[fringe points](/definitions/fringe-point.md).

**Mask.** PEGASUS writes the 0/1 IBLANK array: in the registry's mask,
$\iota_k=0$ on $\mathcal H_k$ and $\iota_k=1$ elsewhere, with receptors kept
in separate lists rather than in the mask (Benek et al. 1983, p. 375). In the
3-D version fringe points are also given IBLANK $=0$ "to simplify XMER3D's
logic" and are told apart only by their presence in the interpolation list
(Benek et al. 1985, p. 324). How XMERA and XMER3D use the mask in the
block-tridiagonal solver is on
[point classification](/definitions/point-classification.md).

**Interpolation.** The 1983 code stores, for each receptor, the offsets
$(\Delta x,\Delta y)=\mathbf x^k_{\mathbf i}-\mathbf x^{k'}_{\mathbf j_0}$ of the receptor
from the donor point $\mathbf j_0$ and applies the linear Taylor formula
$u^k_{\mathbf i}=u^{k'}_{\mathbf j_0}+(\partial_xu)^{k'}_{\mathbf j_0}\Delta x+(\partial_yu)^{k'}_{\mathbf j_0}\Delta y$ (Eq. 1; symbols as on
[inter-grid interpolation](/methods/inter-grid-interpolation.md)),
which the paper calls "first-order accurate"; it is exact for linear
functions, i.e. linear ($q=2$) in the registry's naming (Benek et al. 1983,
p. 374). The 1985 code switches to trilinear interpolation on the
$2\times2\times2$ donor cell, $q=2$ in each direction, in the donor cell's
local coordinates $\mathbf s\in(0,1)^3$ (Benek et al. 1985, p. 324).
Both are non-conservative; see
[inter-grid interpolation](/methods/inter-grid-interpolation.md).

**Data structures.** Benek et al. (1983, pp. 375–376) store the hierarchy as
a graph whose nodes hold, per grid, its storage location, size, level,
precursor and descendants, and the locations of interpolation points,
coefficients, interpolated data and flagged points; all solution data sit in
one large array addressed by per-grid pointers and linked lists. They remark
that "implementing these techniques in Fortran is not always
straightforward". PEGSUS keeps the same single-array, pointer-list layout
(Benek et al. 1985, pp. 324–325).

## Version history (as recalled by Rogers et al. 2003)

Rogers et al. (2003, "Motivation for PEGASUS Version 5", pp. 1037–1038)
recall the versions as follows:

| Version | Year | Capability added, as recalled |
|---|---|---|
| 1 | 1985 | hierarchy imposed: a grid may cut a hole only in a larger grid and connect only to it; hole cutters restricted to specific topologies |
| 2 | 1987 | no restriction on interconnectivity: a grid may cut holes in any number of grids; hole cutters still topology-specific |
| 3 | 1989 | generalized hole cutting: a hole may be defined by any number of surfaces of a single grid; improved NAMELIST input |
| 4 | 1991 | surfaces from several grids may define one hole; restart capability, used for moving bodies |

Meakin & Suhs (1989, ref. [13]) base their moving-body DCF on the 1987 code
of Benek, Donegan & Suhs, which "establishes all inter-grid linkages" on
arbitrary 3-D grid systems.

## Cost and effort

- **Per-step cost in moving-body use.** Unmodified PEGASUS costs 1.96 times
  one flow-solver iteration for a two-grid wing/store case (243,906 points)
  and 5.27 times for the three-grid Space Shuttle SRB separation (357,330
  points); restricting the search to a band around the previous hole
  boundaries lowers this to 0.64 and 2.02 (Meakin & Suhs 1989, Table 1, NAS
  CRAY-2). In static use, hole definition is "typically the most
  time-consuming task" (§II). The restriction and its one-cell-per-step
  hole-motion rule are on
  [moving overset grids](/methods/moving-overset-grid.md).
- **Input and labour.** A PEGASUS 4 high-lift case with 153 meshes and
  $33\times10^6$ points needed over 17,000 lines of input and many weeks of
  expert work (Rogers et al. 2003, Motivation). For the Boeing 777-200
  landing configuration, PEGASUS 4 connectivity took 32 labour days and left
  just under 5600 orphan points, against 3 days and just under 1200 orphans
  with PEGASUS 5 (Rogers et al. 2003, Boeing 777 section; see
  [multi-element airfoils](/benchmarks/multi-element-airfoil.md) for the
  2-D case).
- **Limitations recalled by its successor.** Rogers et al. (2003) state that
  hole cutting by surface normals in earlier versions "exhibited many
  situations that had to be dealt with as special cases", and that the
  user-supplied prioritized link lists for donor choice "unnecessarily
  constrained the choices for the donor interpolation cells".

## Qualifications

- The 1983 and 1985 papers state the hole-cutting tests without hypotheses
  on the shape of $\mathcal C$, and neither paper describes how the donor
  cell and its local coordinates are found (Benek et al. 1985 says only that
  the hierarchy limits the search; Benek et al. 1983 describes a closest
  point plus "nearest neighbor" search and refers to its Ref. 13 for details).
- Benek et al. (1985, p. 323) use "lower level" in two opposite senses
  (embedded grids "occupy a lower level" than their enveloping grid, yet
  level $\ell-1$ is "the next lower level"); their Fig. 1 makes the
  hierarchy unambiguous: embedded grids have larger $\ell$.
- No timings of PEGASUS itself are given in the 1983 and 1985 papers.

# Citations

- [Benek et al. (1983)](/sources/benek-1983.md) — "Computer Codes" p. 376 (PEGASUS, XMERA, name); hierarchy p. 374, Figs. 2–3; Eq. (1) p. 374; holes and fringe p. 375, Figs. 4–7; IBLANK p. 375; data structures pp. 375–376.
- [Benek et al. (1985)](/sources/benek-1985.md) — "Implementation" and "PEGSUS" pp. 323–325 (two-code split, hierarchy, hole generation, fringe with IBLANK 0, trilinear interpolation, data structures, output files).
- [Meakin & Suhs (1989)](/sources/meakin-1989.md) — §II DCF, Table 1 (PEGASUS cost relative to the flow solver), ref. [13].
- [Rogers et al. (2003)](/sources/rogers-2003.md) — Introduction (codes and solvers), "Motivation for PEGASUS Version 5" pp. 1037–1038 (version history, 17,000 input lines), Boeing 777 section (labour days, orphans).
- [Noack (2005)](/sources/noack-2005.md) — §I (PEGASUS family as the mainstay of structured assembly, scripts for moving bodies, "Pegsus4"), ref. 7.

---
type: Definition
title: "Point classification and the iblank mask"
description: "The partition of every component grid into discretization, receptor and hole points (with orphans among the receptors), the signed mask that records it, the 0/1 IBLANK of the Chimera codes and how blanking enters implicit solvers, and the vocabularies of the founding sources translated into one."
status: established
aliases: [iblank, IBLANK, i_b, kr flag, point status, blanking, hole point, field point, discretization point, unused point, active point, solver point, blanked-out point, masking variable]
tags: [domain-connectivity, hole-cutting, overset-grid]
timestamp: 2026-11-02T11:39:00Z
---

# Point classification and the iblank mask

Every point of a component grid $G_k$ of an
[overset grid](/definitions/overset-grid.md) belongs to exactly one of three
disjoint sets, $G_k=\mathcal D_k\cup\mathcal R_k\cup\mathcal H_k$: the
**discretization points** $\mathcal D_k$, updated by the flow solver; the
**receptor points** $\mathcal R_k$, whose values are interpolated from a donor
grid $k'$ ([fringe points](/definitions/fringe-point.md)); and the **hole
points** $\mathcal H_k$, excluded from the solution. Receptors without a valid
donor form the [orphan](/definitions/orphan-point.md) subset
$\mathcal O_k\subset\mathcal R_k$. The bundle records the classification in
the signed mask

$$
\iota_k(\mathbf i)=\begin{cases}1,&(\mathbf i,k)\in\mathcal D_k,\\ -k',&(\mathbf i,k)\in\mathcal R_k\text{ with donor grid }k',\\ 0,&(\mathbf i,k)\in\mathcal H_k,\end{cases}
$$

which carries the donor grid in its sign as CMPGRD's flag does, because the
0/1 IBLANK of the Chimera codes cannot tell a receptor from a hole or a field
point (see the [notation registry](/notation.md)). Computing the classification
is the first task of [domain connectivity](/definitions/domain-connectivity.md).

## The sources' vocabularies

| Source | $\mathcal D_k$ | $\mathcal R_k$ | $\mathcal H_k$ | stored as |
|---|---|---|---|---|
| [Benek et al. (1983)](/sources/benek-1983.md), p. 375 | (computed) points | hole-boundary points; outer-boundary points of embedded grids | hole points | IBLANK 1 / 0; receptors not given a distinct value, kept in flagged lists |
| [Benek et al. (1985)](/sources/benek-1985.md), p. 324 | active points | fringe points; outer boundary of the embedded grid | hole points | IBLANK 1 / 0, fringe points **also set to 0** |
| [Meakin & Suhs (1989)](/sources/meakin-1989.md), §I–II | conventional field points | interpolated (hole-)boundary points | hole points | $i_b$ 1 / 0 |
| [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md), §3.2 | discretization points (interior, boundary) | interpolation points | exterior or unused points | `kr` $=k$ / $-k'$ / $0$ |
| [Henshaw (1994)](/sources/henshaw-1994.md), §2, §4 | interior and boundary points (plus ghost points) | interpolation points | — | no mask stated |
| [Wang (1995)](/sources/wang-1995.md), §3.1 | normal cells; cut cells (clipped) | — (no interpolation) | hole cells | cell classes of the major grid |
| [Rogers et al. (2003)](/sources/rogers-2003.md), Fig. 1 | field points | hole-fringe points; outer-boundary points | hole (blanked) points | iblank-type data, values not printed |
| [Lee & Baeder (2003)](/sources/lee-2003.md), pp. 2–3 | field points | hole-fringe points; interpolated boundary points | hole points | $i_b$, values not printed |
| [Kageyama & Sato (2004)](/sources/kageyama-2004.md), §§II–III | grid points | border points ("internal boundary condition") | masked points (minimum-overlap variants) | no convention |
| [Noack (2005)](/sources/noack-2005.md), §IV | FIELD | INNER FRINGE 1, 2; OUTER FRINGE 1, 2 | OUT | labels, no integers |
| [Sherer & Scott (2005)](/sources/sherer-2005.md), §4.4 | (computed) points | interpolation (fringe) points, two levels | hole points, "blanked out" | rows of the implicit operators |
| [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md), §3.1; [Henshaw (2006)](/sources/henshaw-2006-b.md), §4 | discretization points (plus ghost points) | interpolation points | unused points | no mask values printed |
| [Chan (2009)](/sources/chan-2009.md), §2, Fig. 1 | field points | hole-boundary and outer-boundary fringe points | blanked (hole) points | iblank 1 / 0; no fringe value stated |
| [Roget & Sitaraman (2014)](/sources/roget-2014.md), §2.1 | field (active, solver) points | receptor points, mandatory or by resolution | hole (blanked-out) points | types, no integers |
| [Banks et al. (2016)](/sources/banks-2016.md), §4.1 | discretization points | interpolation points | unused (hole) points | Ogen classification |
| [Picard et al. (2021)](/sources/picard-2021.md), §3.2.1 | integrated cells, incl. covered substrate cells | ghost cells, two layers per grid | — (none) | cell sets |
| [Horne & Mahesh (2021)](/sources/horne-2021.md), §2 | unmasked cells | reconstruction cells | cut (masked) cells | binary masking variable |
| [Sharma et al. (2021)](/sources/sharma-2021.md), §1, Fig. 1 | field points | fringe points (donors: "donor points") | hole points | no values |
| [Wang et al. (2021)](/sources/wang-2021.md), §III A, Figs. 4–5 | interior and boundary points; active cells | interpolation points; acceptor cells | exterior and unused points | figure legend also has "ghost" points |

Hence $\iota_k=1\Leftrightarrow$ IBLANK $=1$ and $\iota_k=0\Leftrightarrow$ a
hole, but a Chimera IBLANK of 0 can also be a receptor (Benek et al. 1985) and
an IBLANK of 1 can also be a receptor (Benek et al. 1983). Chesshire & Henshaw's
`kr` stores $k$ rather than 1 on $\mathcal D_k$; the information is the same as
$\iota_k$. Noack's classification is attached to nodes or to cell centres
according to where the solver stores its unknowns, and a cell-centred solver
gets a different fringe from a node-centred one
([fringe points](/definitions/fringe-point.md)). Wang classifies cells, not
points, and uses no interpolation at all: the minor grid's boundary becomes a
patch boundary inside the major grid
([conservative overset interface](/methods/conservative-overset-interface.md)).
Picard et al. (2021) likewise remove nothing: the substrate cells under the
patch keep being integrated, and the authors state that they have "no impact
on the solution inside the patch" because the patch receives only through its
own receptor layers (§3.2.3).

Roget & Sitaraman (2014), §2.1, give automatable definitions that make the
classification a decision rule. A *candidate donor* of a query point is any
cell of another mesh that contains it (in their implementation, a mesh of
another body, §3.2); the *donor* is the candidate of finest resolution
(nominally the cell volume; for nodes the average volume of the adjacent
cells); a point is a **hole** point if it lies inside a solid body, a
**receptor** if it is a *mandatory receptor* (within a stencil-dependent number
of cells of an outer boundary node or of a hole point) or has a donor finer than
itself, and a **field** point otherwise. The rule selects field points so that
the overlap is minimal ([implicit hole cutting](/methods/implicit-hole-cutting.md);
[overlap optimization](/methods/overlap-optimization.md)); an orphan is a
mandatory receptor without donor ([orphan points](/definitions/orphan-point.md)).

## Validity conditions

Chesshire & Henshaw (1990), §3.2, p. 16, make membership conditional on
stencils. A point is a valid discretization point if the centred stencil of
width $q_{\mathrm d}$ around it contains only points of $\mathcal D_k\cup\mathcal R_k$;
it is a valid receptor if its donor stencil $\mathcal S_{\mathbf i}$ of width
$q$ in $G_{k'}$ is "sufficiently centred" and consists of points of
$\mathcal D_{k'}\cup\mathcal R_{k'}$ — or of $\mathcal D_{k'}$ only, when
interpolation is explicit
([explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md)).
Since validity depends on the neighbours' status, CMPGRD iterates the
classification to a fixed point (§3.2, Step 3). The categories overlap before
the choice is made: a discretization point may also be interpolable, and the
algorithm prefers the classification with the fewest receptors. The Chimera
papers state the same condition informally: the points used by the
interpolation must be defined on the donor grid and must not be hole points
(Benek et al. 1983, p. 375; Benek et al. 1985, p. 324).

## Blanking in implicit solvers

Benek et al. (1983), p. 375, Eqs. (2)–(3), show how holes enter an implicit
approximate-factorization solver. For a line system $\mathsf A\boldsymbol\phi=\mathbf F$
with hole unknowns $\phi_3,\phi_4,\phi_5$ of specified values, the off-diagonal
couplings of the hole rows are zeroed, their diagonal entries set to the
identity and their right sides set to the specified values; the neighbours'
couplings to the now-known hole values ($a_{23}$, $a_{65}$) are kept, and a
standard tridiagonal algorithm still applies. Operationally each row of the
coefficient matrix is multiplied by the point's IBLANK and the diagonal of a
zeroed row is reset to unity, "a simple matter". Benek et al. (1985), p. 325,
apply the same partition in "the standard tri-diagonal algorithm" of XMER3D, where
fringe points, also blanked, thus keep their interpolated values through the
implicit sweep. Meakin & Suhs (1989), §II, Eq. (2), place $i_b$ on every term
of the factored thin-layer scheme that carries $h$, $\Delta t$ or dissipation,

$$
\bigl[\mathsf I+i_b\,h\,(\cdots)\bigr]\bigl[\mathsf I+i_b\,h\,(\cdots)\bigr]\Delta\hat{\mathbf q}^n=-i_b\,\Delta t\,\{\cdots\}-i_b\,(\cdots)\,\hat{\mathbf q}^n,
$$

so that $i_b=0$ gives $\Delta\hat{\mathbf q}^n=\mathbf 0$ and
$\hat{\mathbf q}^{n+1}=\hat{\mathbf q}^n$ at hole points; they stress that $i_b$
is the only dependence of their solver on the Chimera machinery. Chan (2009),
§2, presents the same device as the reason a single-grid solver becomes an
overset solver "with no special logic" for blanked points, the iblank being
multiplied into the differencing stencils.

Sherer & Scott (2005), §4.4, Fig. 10, carry the device to compact
(tridiagonal) difference and filter operators, where a hole couples the whole
line. Along every grid line crossed by a hole the points within two points of
the hole boundary take one-sided boundary difference formulas (five-point
interior stencil) and those within five points take boundary filters
(eleven-point filter); each hole point gets the row $\{0,1,0\}$ with zero right
side, so the system stays tridiagonal and splits into the hole and the two
sides. Hole-boundary points are classified per coordinate direction, since a
point may border a hole along one line and not along the other.

Lee & Baeder (2003), p. 3, obtain the same protection without blanking for
their cell-selection assembly: the solver need not blank hole points for the update, and $i_b$ is
kept only for contour plotting, for blanking holes in steady-state residual
checks, and for the residuals of implicit Newton subiterations; unsteady
explicit computations use it only for plotting. Their argument is
hyperbolicity: invalid values cannot cross a receptor layer that is thicker
than the distance information travels in one $\Delta t$, provided the layers
completely enclose the body and the values at invalid points are not very
large (pp. 7–9; see [implicit hole cutting](/methods/implicit-hole-cutting.md)).

## Frequencies

Rogers et al. (2003), Performance, report that a typical 3-D problem blanks
about 5–15% of the grid points. Henshaw (2006), §10.5, counts about
$4.2\times10^5$ interpolation points in a 10.2-million-point 3-D grid. Chesshire & Henshaw's coarsest cylinder grid
has 4221 stored and 3580 active points (Tables IX–X); Henshaw (1994) counts
10,728 interpolation points in the three-grid sphere case, a large fraction of
the total (§5.2, Table VIII).

## Qualifications

- **Must hole points be excluded from the solution update?** (Reclassified
  from a contradiction at the first deep lint: a difference of setting and of
  mechanism, not a conflict between sources.) Benek et al. (1983), p. 374, require
  "some mechanism … to remove such points from the solution process", because
  points of the parent grid inside the embedded grid fall "outside the
  computational domain" or "violate the constraints on the grid hierarchy";
  "the solution algorithm must also be modified to exclude these points".
  Benek et al. (1985), p. 323, give the same ground (such points "lie outside
  the computational domain and must be excluded"), and they and Meakin & Suhs
  (1989), §II, build the exclusion into an implicit approximate-factorization
  operator with a single fringe layer (Benek et al. 1985, p. 324, Fig. 4).
  Lee & Baeder (2003), pp. 3, 7–9, agree that invalid values must not reach the
  field points, but obtain this by insulation instead of blanking: hole points
  may be updated like any other point provided the hole fringe completely
  encloses the body, is thicker than the distance information travels in one
  $\Delta t$, and the values at invalid points are not very large; they extend
  the argument to implicit methods with Newton subiterations and still blank
  hole points in residuals. The two positions rest on different hypotheses —
  a one-layer fringe and no thickness condition in the Chimera papers, a thick
  fringe in Lee & Baeder's — and no source tests an unblanked update under the
  Chimera papers' hypotheses or a blanked one under Lee & Baeder's. Lee &
  Baeder's claim is an argument with "first order checks of many cases", no
  proof and no measurement. Meakin & Suhs's warning that a hole point turning
  into a field point without first being interpolated brings in undefined
  values (§II, Fig. 3) concerns hole motion, not the update, and Lee & Baeder
  do not address it. The same reading is recorded on
  [implicit hole cutting](/methods/implicit-hole-cutting.md).

- Benek et al. (1983) call the receptors of the hole boundary "also flagged";
  the paper gives them no separate IBLANK value, so their status lives in the
  interpolation lists, not in the mask.
- Lee & Baeder's unblanked update has two later analogues of different scope:
  Picard et al. (2021) integrate the covered substrate cells, which are valid
  flow cells, not points inside a body; Horne & Mahesh (2021) mask cut cells.
  Neither tests the thickness condition of Lee & Baeder.
- Chan (2009) states only the values 0 and 1 of the iblank; the fringe points of
  its Fig. 1 are not given a value of their own.
- Kageyama & Sato (2004) give no masking convention; masking appears only in
  their minimum-overlap Yin–Yang variants
  ([Yin–Yang grid](/definitions/yin-yang-grid.md)).

# Citations

- [Benek et al. (1983)](/sources/benek-1983.md) — p. 374 (holes must be excluded); p. 375, Eqs. (2)–(3) (IBLANK in the implicit solver; hole-boundary points).
- [Benek et al. (1985)](/sources/benek-1985.md) — pp. 323–325 (hole and fringe points, IBLANK = 0 for both, partitioned tridiagonal solve).
- [Meakin & Suhs (1989)](/sources/meakin-1989.md) — §I (point types); §II, Eq. (2), Fig. 3 ($i_b$ in the factored scheme; hole-to-field transitions).
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §3.2, pp. 16–21 (point types, validity, `kr` convention); Tables IX–X.
- [Henshaw (1994)](/sources/henshaw-1994.md) — §2, §4.1 (interpolation and ghost points); §5.2, Table VIII.
- [Wang (1995)](/sources/wang-1995.md) — §3.1, Fig. 3 (cut, normal and hole cells).
- [Lee & Baeder (2003)](/sources/lee-2003.md) — pp. 2–3 ($i_b$ uses); pp. 7–9 (contamination argument).
- [Rogers et al. (2003)](/sources/rogers-2003.md) — Fig. 1 and "Automation of the Oversetting Process" (point types); Performance (5–15% blanked).
- [Kageyama & Sato (2004)](/sources/kageyama-2004.md) — §II (border points); §III (masked points).
- [Noack (2005)](/sources/noack-2005.md) — §I (hole and receptor points); §IV (OUT, INNER/OUTER FRINGE labels).
- [Sherer & Scott (2005)](/sources/sherer-2005.md) — §4.4, Fig. 10 (holes in compact operators).
- [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) — §3.1, Fig. 2 (point classes, ghost points).
- [Henshaw (2006)](/sources/henshaw-2006-b.md) — §4 (point classes); §10.5 (interpolation-point count).
- [Chan (2009)](/sources/chan-2009.md) — §2, Fig. 1 (iblank, field, hole and fringe points).
- [Roget & Sitaraman (2014)](/sources/roget-2014.md) — §2.1 (automated definitions), §3.2, §3.5.
- [Banks et al. (2016)](/sources/banks-2016.md) — §4.1.
- [Picard et al. (2021)](/sources/picard-2021.md) — §3.2.1–3.2.3 (ghost and sending cells, no deactivation).
- [Horne & Mahesh (2021)](/sources/horne-2021.md) — §2 (masking variable, reconstruction cells).
- [Sharma et al. (2021)](/sources/sharma-2021.md) — §1, Fig. 1.
- [Wang et al. (2021)](/sources/wang-2021.md) — §III A, Figs. 4–5.

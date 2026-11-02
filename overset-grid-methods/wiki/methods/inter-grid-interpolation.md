---
type: Method
title: "Inter-grid interpolation"
description: "How overset grids exchange data: each receptor takes a weighted sum of donor values. Covers linear Taylor, trilinear, tensor-product Lagrange, Hermite, compact, intersection-volume, radial-basis-function and unstructured cell weights, their order and width with measured effects, cell-size ratio, geometry consistency, monotonicity at shocks, parallel evaluation and cost."
status: established
aliases: [intergrid communication, intergrid interpolation, chimera interpolation, overset interpolation, donor interpolation, intergrid boundary conditions, fringe interpolation, Chimera transfer, overset reconstruction]
tags: [interpolation, overset-grid, chimera, composite-grid, high-order, domain-connectivity]
timestamp: 2026-11-02T14:53:00Z
---

# Inter-grid interpolation

In an [overset grid](/definitions/overset-grid.md) the component grids are
coupled only through their receptor points $\mathcal R_k$ (see
[fringe points](/definitions/fringe-point.md)). Each receptor $(\mathbf i,k)$
takes its value from a donor stencil $\mathcal S_{\mathbf i}$ on another grid
$G_{k'}$:
$$u^k_{\mathbf i}=\sum_{\mathbf j\in\mathcal S_{\mathbf i}}\alpha_{\mathbf j}\,u^{k'}_{\mathbf j},\qquad \sum_{\mathbf j}\alpha_{\mathbf j}=1 .$$
This is the form written by [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md)
(Eq. (5.3)). The Taylor formula of [Benek et al. (1983)](/sources/benek-1983.md)
also takes this form once the donor gradient is written as a difference
*(compiler check, not in the sources)*. The sources that describe the
coupling compute the weights $\alpha_{\mathbf j}$ once per grid configuration, during
[domain connectivity](/definitions/domain-connectivity.md), and the flow
solver applies them at every update. The interpolation equations act as
boundary conditions on the receptors: at the outer boundaries of embedded
grids and at the fringes of holes (Benek et al. 1983, Fig. 7). The values at
these receptors are not computed by the solver
([Meakin & Suhs (1989)](/sources/meakin-1989.md), §I). Later sources name the
receptors differently: "fringe points" whose "donor points" are field points
([Sharma et al. (2021)](/sources/sharma-2021.md), Eq. (10)), "ghost cells"
in two layers fed from "sending cells"
([Picard et al. (2021)](/sources/picard-2021.md), §3.2.1), "acceptor" cells
([Wang et al. (2021)](/sources/wang-2021.md), §III A), and "reconstruction"
cells with "partners" ([Horne & Mahesh (2021)](/sources/horne-2021.md), §2).
[Chan (2009)](/sources/chan-2009.md) (§7) defines the storage of the
"interpolation stencils" of fringe points as half of domain connectivity,
with hole cutting the other half.

## Donor coordinates

Every weight formula needs the receptor's position inside the donor cell. On
mapped grids [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) (§3.2,
§5.2) compute
$\mathbf r'=\mathbf d_{k'}^{-1}(\mathbf x^k_{\mathbf i})$ by Newton iteration on
the mapping. They interpolate in the donor's unit-square coordinates, which
they say makes arbitrary-order interpolation easy and less error-prone (p. 28).
CMPGRD stores, for each receptor, the donor grid $k'$, $\mathbf r'$, the
lower-left corner of the stencil and the widths $q$ in each direction.

The Chimera assemblers have only the grid points, not a mapping. They invert
the trilinear map of a candidate cell for the local coordinates
$\mathbf s\in[0,1]^{n_d}$ by Newton iteration, then walk or jump to a
neighbouring cell when $\mathbf s$ falls outside the unit cube
([Rogers et al. (2003)](/sources/rogers-2003.md), "Boundary Point
Interpolation"; [Lee & Baeder (2003)](/sources/lee-2003.md), pp. 9–11). On
general polyhedra, barycentric or parametric coordinates are unavailable, and
[Noack (2005)](/sources/noack-2005.md) (§V) uses a neighbour walk with
approximate face planes. [Roget & Sitaraman (2014)](/sources/roget-2014.md)
(§3.4, §3.6) compute tri-linear weights in tetrahedra, prisms, pyramids and
hexahedra by Newton–Raphson, converging to machine precision in 3–4
iterations; when the weights of the identified donor fall out of tolerance
(e.g. a concave cell) all neighbour cells are tested before the point is
declared donorless. High-order formulas need high-order offsets:
[Sherer & Scott (2005)](/sources/sherer-2005.md) (§4.2, Eqs. (11)–(12)) start
from the second-order offsets of a grid-assembly code and iterate Newton on
the tensor-product Lagrange representation of the donor coordinates. These
searches are described in [donor search](/methods/donor-search.md).

## Weight formulas in the sources

**Linear Taylor formula.** [Benek et al. (1983)](/sources/benek-1983.md)
(Eq. (1), p. 374) use, in 2-D,
$$u^k_{\mathbf i}=u^{k'}_{\mathbf j_0}+(\partial_xu)^{k'}_{\mathbf j_0}\,\Delta x+(\partial_yu)^{k'}_{\mathbf j_0}\,\Delta y,\qquad (\Delta x,\Delta y)=\mathbf x^k_{\mathbf i}-\mathbf x^{k'}_{\mathbf j_0},$$
where $\mathbf j_0$ (page-local) is the donor point found by the nearest-point
search. The stored "interpolation coefficients" are $\Delta x$ and $\Delta y$
(p. 376). The paper does not say how the donor derivatives are differenced. The
formula is exact for linear data, with error $O(h^2)$: it is linear ($q=2$)
interpolation in this bundle's naming. The authors call it "first-order
accurate".

**Bilinear and trilinear interpolation in the donor cell.**
[Benek et al. (1985)](/sources/benek-1985.md) (p. 324) replace the Taylor
formula in 3-D by
$u=a_1+a_2s_1+a_3s_2+a_4s_3+a_5s_1s_2+a_6s_1s_3+a_7s_2s_3+a_8s_1s_2s_3$
in the local coordinates of the $2\times2\times2$ donor cell. The eight
coefficients are fixed by the eight vertex values. This is the tensor-product
Lagrange form below with $q=2$, $L_0(s)=1-s$, $L_1(s)=s$ *(compiler check, not
in the sources)*. Their reasons, as recalled from Mastin and from simple
experiments reported by private communication: in 2-D, bilinear interpolation is better than the Taylor series
when higher derivatives of the solution are unimportant, and it is also better
on a rectangular mesh containing a discontinuity. The stencil is more compact,
but the receptor must lie inside its cell, and "trouble may be encountered
with shock–grid boundary interactions". PEGASUS 5 inverts trilinear
interpolation to locate donor cells and outputs the donor cells with their
coefficients. The interpolation formula itself is not printed
([Rogers et al. (2003)](/sources/rogers-2003.md)). For node-centred grids
SUGGAR takes the weights from the parametric coordinates of the search
([Noack (2005)](/sources/noack-2005.md), §VI). Trilinear interpolation remains
the common choice in later production use: [Chan (2009)](/sources/chan-2009.md)
(§7) calls it "the commonly adopted" fringe scheme; Roget & Sitaraman (2014)
use tri-linear basis functions on all unstructured cell types (§3.6); and
[Wang et al. (2021)](/sources/wang-2021.md) (Eq. (10)) interpolate
$u^k_{\mathbf i}=\sum_{l=1}^{8}\alpha_l\,u^{k'}_l$ from the eight values of the donor
cell of a rotating propeller grid, recomputing the weights at every
rotation step. Neither Roget & Sitaraman nor Wang et al. discuss the order
or conservation of the formula.

**Tensor-product Lagrange interpolation in parameter space.**
[Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) (§5.2) use
$\alpha_{\mathbf j}=\prod_{m}L_{j_m}(s_m)$ with $q$ points per direction,
covering bilinear, biquadratic and higher formulas. The width $q$ may differ
per direction and per grid pair (`iw(m,k1,k2)`). [Henshaw (1994)](/sources/henshaw-1994.md)
(§4.1) writes the quartic case ($q=5$) explicitly:
$$\mathbf u^{k}_{\mathbf i}=\sum_{j_1=0}^{4}\sum_{j_2=0}^{4}\sum_{j_3=0}^{4}L_{j_1}(\bar s_1)L_{j_2}(\bar s_2)L_{j_3}(\bar s_3)\,\mathbf u^{k'}_{\mathbf i_0+(j_1,j_2,j_3)},\qquad L_j(\bar s)=\prod_{l=0,\,l\neq j}^{4}\frac{\bar s-l}{j-l}.$$
Here $\mathbf i_0$ is the lower corner of the $5\times5\times5$ stencil and
$\bar s_m=(r'_m-r_m(\mathbf i_0))/\Delta r_m$ is the receptor's offset from
that corner in units of the donor spacing (page-local; $\bar s_m=s_m+$ the
index offset of the donor cell inside the stencil). The coefficients are
stored and applied by gather–scatter, which vectorizes (§4.1). The Overture
solvers keep the same form: a tensor-product Lagrange interpolant in the
donor's parameter space ([Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md),
§3), of width $q=p+1$ for an order-$p$ wave-equation solver
([Henshaw (2006)](/sources/henshaw-2006-b.md), §4).
[Sharma et al. (2021)](/sources/sharma-2021.md) (§3.1.1, Eq. (11), Fig. 5)
write the same product in physical coordinates on Cartesian donors, with a
cell-based stencil for linear and a neighbour (tensor-grid) stencil for
quadratic interpolation; they note that on curvilinear donors a nonlinear
problem must first be solved for the parameter coordinates.
Sherer & Scott (2005) (§4.2, Fig. 9) apply 1-D Lagrange formulas dimension by
dimension: first to "extended interpolation points" along donor grid lines,
then across them to the receptors.

**Compact, optimized and B-spline formulas.** Sherer & Scott (2005) (§2–3,
§5.1) also test compact formulas that couple three receptors along a donor
line, wavenumber-optimized weights and B-splines. Compact interpolation is
the most accurate in 1-D but ill-conditioned for general receptor
distributions; optimized weights lose under refinement; B-splines need
centred stencils. Their conclusion favours explicit non-optimized Lagrange
interpolation; the analysis is on
[high-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md).

**Hermite cubic interpolation.** [Lee & Baeder (2003)](/sources/lee-2003.md)
(pp. 4, 10) interpolate the solution with a Hermite cubic monotone formula
along each direction. It needs a 6-point stencil per direction: values at the
two cell ends, plus first derivatives there from 5-point fourth-order
differences (at least third order is needed; five points are used for
symmetry). The first two cells from each grid boundary therefore cannot be
donors. A $4^3$ Hermite tricubic interpolant of the *coordinates* supplies the
donor-cell geometry (see below). No interpolation formula is printed. The
importance of monotone interpolation is credited to the authors' 2-D work
(p. 4).

**Cell-centred weights on unstructured and polyhedral grids.**
[Noack (2005)](/sources/noack-2005.md) (§VI, Fig. 8) takes the donor members to
be the donor cell plus its face neighbours, roughly twice the footprint of a
node-centred stencil. The weights are linear and normalized to sum to one,
with three options:
- *zeroth order*: weight 1 on the donor cell, the least accurate option and
  the one needing the least overlap;
- *Laplacian weights* of USM3D, optionally clipped to $[0,2]$ before
  normalization, falling back to zeroth order when all weights vanish next to
  a boundary;
- *unweighted least squares* of HYB3D, which degenerates when the member
  centres are coplanar or collinear, e.g. donor cells sharing a
  Cartesian-aligned boundary face (Fig. 9).

A barycentric option on a Delaunay dual of the cell centres is planned. The
member count drops at boundaries; in the worst case, a tetrahedron in a mesh
corner with all but one face on a boundary, interpolation accuracy can suffer.

**Intersection-volume-weighted reconstruction.** For cell-centred finite
volumes [Picard et al. (2021)](/sources/picard-2021.md) (§3.2.4, Eqs. (14)–(15))
start from a "local conservation" hypothesis: the integral of the receptor
state over a receptor cell equals the integral of the donor solution over the
same region. With $V_c$ a receptor cell, $V'_{c'}$ the donor cells it
intersects, $\mathbf x_{cc'}$ the barycentre of $V_c\cap V'_{c'}$, and
$\Phi_{c'}\nabla\mathbf q_{c'}$ the limited least-squares gradient of the
conserved variables in donor cell $c'$ (page-local notation),
$$\mathbf q_c=\sum_{c'}\frac{\lvert V_c\cap V'_{c'}\rvert}{\lvert V_c\rvert}\Big(\mathbf q_{c'}+\Phi_{c'}\nabla\mathbf q_{c'}\cdot(\mathbf x_{cc'}-\mathbf x_{c'})\Big).$$
The weights are the intersection-volume fractions; the stencil is every donor
cell that geometrically intersects the receptor, plus the least-squares
neighbours of each. The formula is claimed second order on structured or
unstructured meshes without mesh constraints, and the authors state that it
is not globally conservative, because it interpolates states and not fluxes.
The intersection barycentre can lie farther from the donor centre than any
face centre, increasingly so as the cell-size ratio grows, so the authors
widen the limiter's search radius from face centres to cell corners
(Eq. (19)); see
[shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md).

**Radial-basis-function point clouds.** For unstructured donors,
[Sharma et al. (2021)](/sources/sharma-2021.md) (§3.1.2, Eqs. (12)–(22))
interpolate from a cloud of donor field points, all those within $2.5h$ of
the receptor (20 points on their Cartesian test meshes), by radial basis
functions $g_l$ augmented with monomials $P_j$ up to a degree $m_{\mathrm p}$
(page-local symbols):
$$u(\mathbf x)=\sum_l g_l(\mathbf x)\,a_l+\sum_jP_j(\mathbf x)\,b_j,\qquad \begin{bmatrix}\mathsf G&\mathsf P\\ \mathsf P^T&0\end{bmatrix}\begin{bmatrix}\mathbf a\\ \mathbf b\end{bmatrix}=\begin{bmatrix}\mathbf u^{k'}\\ \mathbf 0\end{bmatrix},$$
with the Gaussian $g_l(\mathbf x)=e^{-\epsilon_{\mathrm g}\lvert\mathbf x-\mathbf x_l\rvert^2}$,
$\epsilon_{\mathrm g}=1$. Eliminating $\mathbf a$ and $\mathbf b$ in the
element-free-Galerkin manner (Eqs. (20)–(21)) turns the interpolant into
explicit weights $\alpha_l(\mathbf x)$ on the donor values, so it can enter an
implicit system as constraint rows; Sharma et al. state that the earlier
point-cloud form of Quon & Smith (as recalled there) is "only first-order
consistent" and could not. Invertibility needs many more cloud points than
monomials. Augmentation to degree $m_{\mathrm p}\ge2$ (the paper's
"$C^2$") is needed to keep second order for an elliptic equation, and degree
1 is not (§4.1.1, Fig. 13). Constructing the weights costs about five times
Lagrange interpolation on the finest mesh, and the cost of one receptor grows
quadratically with the cloud size (§4.1.4, Fig. 17; in-house MATLAB, hardware
not stated). The authors list moving least squares, kriging, RKPM and Hermite
interpolants as alternatives.

**Supercell reconstruction by injection.** Horne & Mahesh (2021) (§3.2) keep
the supercell interpolant of their earlier unstructured method (not
restated in this paper) but inject the reconstructed values directly into
the implicit equations for all variables, pressure included; see
[incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md).

**Symmetric stencils on the Yin–Yang grid.** On the
[Yin–Yang grid](/definitions/yin-yang-grid.md) the two component grids are
congruent. [Kageyama & Sato (2004)](/sources/kageyama-2004.md) (§II) show that
the stencil and coefficients for the Yin border point $(i,j)$ are identical to
those for the Yang border point $(i,j)$, so one routine serves both borders.
The interpolation order is not specified. Vector fields must also be rotated
into the receiving grid's components by the matrix $\mathsf P$ (§III).

## Order, width and overlap

In this bundle a $q$-point formula has error $O(h^q)$ and is called order
$q$. On that scale, the linear and trilinear formulas of Benek et al.
(1983, 1985) and PEGASUS 5 are second order ($q=2$),
Henshaw's quartic is fifth order ($q=5$), and Noack's zeroth-order option is
first order ($q=1$, error $O(h)$) *(compiler check, not in the sources)*.
[Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) prove that, for
elliptic problems, the required $q$ depends on the overlap scaling. When the
overlap shrinks with $h$, a second-order discretization of a second-order
equation needs quadratic ($q=3$) interpolation; their heuristic extension
asks $q=5$ for a fourth-order one. When the overlap stays fixed, $q=2$
suffices at second order. Their
2-D Poisson tests lose one order of convergence when the interpolation is
one order short. The statements, proofs and tests are on
[interpolation order and overlap requirements](/results/interpolation-order-requirement.md).
Henshaw (1994) applies the rule: quartic interpolation with two receptor lines
keeps the fourth-order incompressible solver at measured rates 4.0–4.3 on
overlapping grids (Tables III, VII). Later sources add measurements:
- With fringe gap $d=3h$, linear ($q=2$) interpolation degrades a
  second-order diffusion solution and quadratic ($q=3$) keeps it; with a
  constant gap linear suffices; for linear advection linear suffices
  (Sharma et al. 2021, §4.1, Figs. 10–15).
- A sixth-order compact scheme with second-order interpolation converges at
  order 2.01; with sixth-order interpolation at 5.33 (Sherer & Scott 2005,
  §5.2, Fig. 16a).
- Fourth-order Maxwell with $q=5$ converges at 3.9–4.4 in twilight-zone
  tests ([Henshaw (2006)](/sources/henshaw-2006-b.md), Tables 1–2).
- Second-order intersection-volume interpolation keeps a second-order
  finite-volume scheme second order (orders 2.026 and 2.108 against 2.022 and
  2.119 on a single grid; Picard et al. 2021, §4.1, Table 1).

The width also sets how many receptor rows a grid needs and how far the grids
must overlap:
- A centred 3-point discretization needs one line of interpolation points, a
  5-point one two lines (Chesshire & Henshaw, p. 14).
- Benek et al. (1983) state only that the donor stencil must lie in the donor
  grid, and that the overlap must keep its boundaries' influence small
  (p. 375).
- [Rogers et al. (2003)](/sources/rogers-2003.md) call the number of receptor
  layers the "fringe level". They state that a fringe level of 2 "has certain
  advantages within the flow solver and can produce more accurate solutions"
  (p. 1039).
- Lee & Baeder (2003) recommend a *single* layer of interpolated
  outer-boundary points instead of the usual two, for cost. Biased stencils
  are then needed at the first interior points if 5-point interior stencils
  are kept, but not with a fourth-order compact scheme. At hole fringes they
  recommend as many layers as possible (p. 12).
- Sherer & Scott (2005) (§4.2) use a two-point fringe at all interpolation
  boundaries with a compact sixth-order scheme, and size the cylinder overlap
  as the minimum that avoids donors being receptors of the grid they update
  (§5.3).
- Picard et al. (2021) (§3.2.3) use two ghost-cell layers because a
  second-order flux at a face needs two cells on each side, which makes the
  first computed flux independent of the patch boundary. They then add ghost
  cells to shrink the gap between the two grids' ghost layers (Eq. (13)).
- Sharma et al. (2021) (Fig. 4) use TIOGA's implicit hole cutting, which marks
  a preset number of cells from each outer boundary as receptors and keeps a
  preset number of field points beyond them, so the fringe gap is nonzero
  (a zero gap gives a singular system) but shrinks with $h$.

Whether stencils may contain other receptors is the distinction between
[explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md).

## Geometry consistency and near-wall interpolation

- **Coordinate consistency.** Lee & Baeder (2003) (p. 4) represent the donor
  grid by a piecewise Hermite tricubic interpolant of the coordinates. They
  describe it as $C^1$, exact, and "the lowest order interpolant consistent
  with the grid metrics used by the solver". A decoupled cubic is not $C^1$,
  and the trilinear map is only $C^0$ and inconsistent with the metrics. They
  also state that cubic interpolation tolerates a larger spacing jump between
  two grids, "usually about 2:1".
- **Near walls.** The 6-point stencil does not fit next to a wall, so Lee &
  Baeder accept and flag low-order 4- or 2-point stencils there (p. 11,
  Fig. 13). In multigrid, the stencil shrinks to 4 and 2 points on the first
  and second coarser levels.
- **Curved viscous walls.** Rogers et al. (2003) ("Projection for Viscous
  Grids", Figs. 6–7) show what goes wrong when overlapping surface grids
  discretize a curved wall linearly. On concave walls near-wall receptors
  become orphans. On convex walls the donors lie much farther from the wall
  than the receptors, and boundary-layer profiles are corrupted. PEGASUS 5
  projects the receptor surface onto the donor surface and uses the shifted
  coordinates only to compute indices and coefficients. See
  [PEGASUS 5](/software/pegasus-5.md).
- **Donor quality.** Among several candidate donors, Lee & Baeder keep the
  smallest cell (p. 5). Rogers et al. keep the donor of most similar size and
  orientation, by the cell-difference parameter. They state that accuracy
  degrades when donor and receptor cells differ much in size. Roget &
  Sitaraman (2014) (§3.5) keep the candidate donor of finest resolution
  (smallest cell volume). See
  [overlap optimization](/methods/overlap-optimization.md) and
  [implicit hole cutting](/methods/implicit-hole-cutting.md).
- **Cell-size ratio, measured.** The tolerated ratio depends on the test.
  Sherer & Scott (2005) (§5.2, Fig. 18) find no degradation of a convected
  vortex at cell-volume ratios of 4 and 16, with a filter removing the
  waves generated by the jump. Picard et al. (2021) find the error of a
  convected sine wave dominated by the coarse grid for patch refinement
  ratios up to 16 (§4.1, Table 2), but see slip lines perturbed in the
  double Mach reflection at ratio 8 and recommend ratios of at most 4 (§4.5,
  §5). Lee & Baeder's "about 2:1" (above) is a guideline for their cubic
  formula, not a measurement.

## Discontinuities, monotonicity and conservation

None of the formulas above is conservative. Benek et al. (1983) (pp. 374, 377,
Figs. 13–14) flag the loss of conservation form as a possible deficiency
across shocks. On the SKF 1.1 airfoil at $M_\infty=0.76$, a shock crossing the
overlap boundary produced a mismatch and "hash" that "indicates that the
nonconservative interpolations are likely to be at fault", although the
matter was "still under study". [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md)
(Fig. 19a) see a Mach 2 bow shock have "some difficulty crossing the
interpolation boundary" on their coarsest grid only. As recalled by
[Chan (2009)](/sources/chan-2009.md) (§7), the early concern that
non-conservative fringe interpolation degrades accuracy "was resolved by
Meakin", who showed formal accuracy kept with trilinear interpolation
"provided the flow solution is smoothly resolved by all participant grids in
the overlapped zones". [Sharma et al. (2021)](/sources/sharma-2021.md) (§1)
likewise state that the lack of conservation does not degrade the solution
when the overlap is away from shocks. Picard et al. (2021) measure the
defect for a shock sitting on the patch boundary: conservation errors equal
to the single grid's when the two grids' interfaces coincide, at most 0.635%
when they do not (§4.2, Tables 3–4).

Monotonicity is a separate issue:
- Lee & Baeder choose a *monotone* Hermite cubic.
- Noack (2005) (§VI) reports that least-squares weights can be non-monotone
  with respect to the donor values, as found in HYB3D and USM3D results. This
  must be handled in the flow solver or in DiRTlib.
- Sharma et al. (2021) (§3.1.2) state that non-monotone interpolation can
  create or amplify extrema that grow cycle after cycle and drive exponential
  instability at high Reynolds number when grids overlap in chaotic,
  high-gradient regions.
- Picard et al. (2021) (§3.2.5) limit the donor reconstruction and extend
  the limiter's search radius so that the transfer creates no new extrema at
  large cell-size ratios.
- [Henshaw (1994)](/sources/henshaw-1994.md) (§4.4) notes that, in
  incompressible flow, the interpolation equations act as a source of discrete
  divergence.

Flux-based alternatives that avoid interpolation are on
[conservative overset interface](/methods/conservative-overset-interface.md).

## Cost

- **Assembly.** PEGASUS 5's interpolation phase (donor search and
  coefficients) takes about 50% of its run time, against about 30% for hole
  cutting. It finds 2–3 donor cells per grid point, at about 10,000 donor
  cells per CPU second on an SGI R10K at 250 MHz, and keeps about 5% of the
  donors found (Rogers et al. 2003, "Performance").
- **Order of the formula.** Lee & Baeder's connectivity for a 39-grid,
  2.5-million-point tiltrotor model took about 45 s on an Alpha 21264 at
  667 MHz. Linear instead of cubic interpolation saved 20–25% (p. 12).
- **Curse of dimensionality.** Lee & Baeder (p. 12) count the cost per
  receptor and variable. From 2-D to 3-D, an interior point costs 50% more,
  but a receptor of a decoupled $n$-point formula grows from $n+1$ to
  $n^2+n+1$ operations. A 3-D tricubic needs $4^3-2^3=56$ derivative
  evaluations, 32 of them cross derivatives. A decoupled cubic needs
  $2(n^2+n+1)$: 14, 42 and 86 for $n=2,4,6$. For steady problems they suggest
  switching to high order only near convergence.
- **Solver.** In Henshaw's fourth-order code, interpolation took 2% of a time
  step with explicit interpolation and 17% with implicit interpolation and
  many receptors (Tables V, VIII). In the fourth-order Maxwell code it took
  0.46% of a 2-D step and 6.8% of a 3-D step (Henshaw 2006, Table 6); in a
  moving-grid run with adaptive refinement, 14.5% (Henshaw & Schwendeman
  2006, Table 6).
- **Weight construction.** Radial-basis-function weights cost about five
  times Lagrange weights on the finest mesh (Sharma et al. 2021, Fig. 17a).
- **Parallel evaluation.** In mx the Lagrange sums are formed on the
  processor that owns the donor stencil and sent to the receptor's owner, so
  at most one message passes between any two processors (Henshaw 2006,
  §9.4). Point-cloud stencils can cross processor boundaries and add
  communication (Sharma et al. 2021, §4.1.4). See
  [parallel and GPU overset grid assembly](/methods/parallel-overset-grid-assembly.md).
- **Moving bodies.** Hole positions and receptors change with time, so the
  interpolation coefficients are recomputed every time step together with the
  hole mask ([Meakin & Suhs (1989)](/sources/meakin-1989.md), §II; Noack 2005,
  §VII). Meakin & Suhs's cases have 2,090 receptors among 243,906 points
  (wing–store) and 10,408 among 357,330 (Space Shuttle) (Table 1). Wang et
  al. (2021) recompute the trilinear weights at every 1° rotation of a
  propeller grid (§III A). Henshaw & Schwendeman (2006) solve on each grid in
  a frame moving with it, so no interpolation transfers the solution from old
  to new grid positions (§1, §4.1); only receptors are re-interpolated, and
  points uncovered by the motion receive old-time values by interpolation
  (§3.2; see [exposed points](/definitions/exposed-point.md)).
  [Banks et al. (2016)](/sources/banks-2016.md) (§4.3, Procedure 1)
  regenerate the deforming interface grids and recompute all interpolation
  points with Ogen at every step; they do not state the interpolation width.
  See
  [moving overset grids](/methods/moving-overset-grid.md).

## Qualifications

- **Order naming.** Benek et al. (1983) call their linear Taylor formula
  "first-order accurate" (p. 374). Benek et al. (1985) and Rogers et al.
  (2003) state no order for trilinear interpolation. Chesshire & Henshaw name
  orders by the error exponent. This page uses the latter throughout, so the
  Chimera formulas are "linear ($q=2$)".
- **Width versus degree.** The equivalence "width $q$ = order $q$" holds for
  Lagrange formulas. Lee & Baeder's Hermite cubic has degree 3 on a 6-point
  stencil. Its order is not stated in the source and is not inferred here.
- **Evidence.** The accuracy claims of the Chimera and assembly papers (Benek
  et al. 1985; Lee & Baeder 2003; Rogers et al. 2003; Noack 2005) are
  qualitative or rest on figures. Measured convergence rates through
  interpolation boundaries come from Chesshire & Henshaw (1990), Henshaw
  (1994), Sherer & Scott (2005), Henshaw (2006), Sharma et al. (2021) and
  Picard et al. (2021). Roget & Sitaraman (2014), Chan (2009) and Wang et al.
  (2021) state no order for their trilinear formulas.
- **Order naming in Sharma et al.** They write $O(\psi)$ for the polynomial
  degree of the interpolating function, so their "linear" ($O(\psi)=1$) is
  $q=2$ and "quadratic" is $q=3$ here.
- **Printed slip in Sharma et al. (2021):** the third factor of the
  tensor-product formula (Eq. (11)) has denominator $z_j-z_n$; by the
  pattern of the other factors and the donor index $(i,j,k)$ it is
  $z_k-z_n$.
- **Fringe-layer advice.** Rogers et al. (2003) favour two receptor layers for
  accuracy. Lee & Baeder (2003) recommend one layer at outer boundaries for
  cost, with a compact interior scheme. These are recommendations under
  different scheme assumptions, neither supported by a measurement in its
  source, so they are not recorded as a contradiction.

# Citations

- [Benek et al. (1983)](/sources/benek-1983.md) — p. 374, Eq. (1); p. 375 (overlap rule, donor location); p. 376 (stored coefficients); pp. 376–377, Figs. 13–14 (shock crossing).
- [Benek et al. (1985)](/sources/benek-1985.md) — p. 324 (trilinear interpolation; Mastin, Rai and Berger as recalled).
- [Meakin & Suhs (1989)](/sources/meakin-1989.md) — §I (interpolated boundary points), §II (per-step recomputation), Table 1.
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §3.2 (stencil validity, donor inversion), §5.2 (Eq. (5.3), Lagrange interpolation in parameter space), §5.3 (order convention and requirement), Fig. 19a.
- [Henshaw (1994)](/sources/henshaw-1994.md) — §4.1 (quartic Lagrange formula), §4.4 (interpolation as divergence source), Tables III, V, VII, VIII.
- [Wang (1995)](/sources/wang-1995.md) — §1, §3 (interpolation as the source of non-conservation; interpolation-free alternative).
- [Lee & Baeder (2003)](/sources/lee-2003.md) — p. 4 (Hermite coordinate interpolation, 2:1 ratio), pp. 9–11 (Newton for $\mathbf s$, stencil size, low order near walls), p. 12 (cost, layers, timing).
- [Rogers et al. (2003)](/sources/rogers-2003.md) — p. 1039 (fringe level), "Boundary Point Interpolation", "Cell Difference Parameter", "Projection for Viscous Grids", "Performance".
- [Kageyama & Sato (2004)](/sources/kageyama-2004.md) — §II (symmetric stencils), §III (vector rotation).
- [Noack (2005)](/sources/noack-2005.md) — §V (polyhedral donor search), §VI (cell-centred stencils and weights, non-monotonicity), §VII.
- [Sherer & Scott (2005)](/sources/sherer-2005.md) — §2–3 (compact, optimized, B-spline formulas), §4.2 (dimension-by-dimension interpolation, Newton offsets, Eqs. (11)–(12), two-point fringe), §5.2 (Figs. 16a, 18), §5.3, §6.
- [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) — §1, §3, §3.2, §4.1, Table 6.
- [Henshaw (2006)](/sources/henshaw-2006-b.md) — §4 ($q=p+1$), §9.4 (parallel interpolation), Tables 1–2, 6.
- [Chan (2009)](/sources/chan-2009.md) — §7 (stencil storage, trilinear interpolation, Meakin's accuracy result as recalled).
- [Roget & Sitaraman (2014)](/sources/roget-2014.md) — §3.4–3.6 (weight tolerance, finest-resolution donor, tri-linear weights by Newton–Raphson).
- [Picard et al. (2021)](/sources/picard-2021.md) — §3.2.1–3.2.5 (Eqs. (13)–(15), (19)), §4.1 (Tables 1–2), §4.2 (Tables 3–4), §4.5, §5.
- [Horne & Mahesh (2021)](/sources/horne-2021.md) — §2 (reconstruction cells and partners), §3.2 (injection of the supercell reconstruction).
- [Sharma et al. (2021)](/sources/sharma-2021.md) — §1, §3.1 (Eqs. (10)–(22), Figs. 4–5), §4.1 (Figs. 10–17).
- [Wang et al. (2021)](/sources/wang-2021.md) — §III A, Eq. (10).
- [Banks et al. (2016)](/sources/banks-2016.md) — §4.3, Procedure 1.

---
type: Method
title: "High-order discretizations on overlapping grids"
description: "How fourth- to sixth-order finite-difference schemes are run on overset grids: interpolation of matching order and width, compact Padé schemes and filters with holes and two-point fringes, Fourier error analysis of interpolation formulas, symmetric operators, and high-order dissipation against the weak instability that interpolation causes."
status: established
aliases: [high-order overset methods, high-order Chimera, compact schemes on overset grids, high-order composite-grid discretization]
tags: [high-order, finite-difference, interpolation, stability, overset-grid, composite-grid]
timestamp: 2026-11-02T14:53:00Z
---

# High-order discretizations on overlapping grids

A high-order discretization on an [overset grid](/definitions/overset-grid.md)
runs an order-$p$ interior scheme, $p\ge4$, on every component grid $G_k$ and
couples the grids through [inter-grid interpolation](/methods/inter-grid-interpolation.md).
Three things the second-order Chimera practice can neglect then decide the
global order: the interpolation must have order and width matched to $p$; the
wide or implicit interior operators must be closed at hole and fringe
boundaries; and the coupled discrete operator, which interpolation makes
non-symmetric, must be kept stable. The sources treat three solver
families: Henshaw's fourth-order explicit differences for incompressible flow
([Henshaw (1994)](/sources/henshaw-1994.md)), Henshaw's fourth-order
second-order-form Maxwell solver ([Henshaw (2006)](/sources/henshaw-2006-b.md)),
and Sherer & Scott's compact Padé schemes with high-order filters
([Sherer & Scott (2005)](/sources/sherer-2005.md)).

## Interpolation order and width

All three sources tie the interpolation to the interior order.

- **Chesshire–Henshaw rule.** For a second-order PDE ($s=1$) and an overlap
  that shrinks with $h$, the width is $q=p+1$ with $p/2$ receptor lines
  (see [interpolation order and overlap requirements](/results/interpolation-order-requirement.md)).
  Henshaw (1994) uses quartic ($q=5$) Lagrange interpolation with two
  receptor lines for the fourth-order incompressible solver, and Henshaw
  (2006, §4) states $q=p+1$ for a $p$th-order approximation of the
  second-order wave equation, "following" Chesshire & Henshaw.
- **Measured loss with low-order interpolation.** Sherer & Scott (§5.2,
  Fig. 16a) advect an inviscid vortex through a curvilinear overset system
  with a hole, using the sixth-order compact scheme. With second-order
  interpolation the whole computation converges at order 2.01; with
  sixth-order interpolation at 5.33, against 6.36 for the same grids joined
  by direct injection and 7.47 on a single grid (orders printed on the
  figure). As recalled by Sherer & Scott (§1), Delfs found that linear
  interpolation eventually corrupts the whole domain of a high-order
  computation.
- **Preferred formula.** Sherer & Scott (§6) conclude that explicit,
  non-optimized Lagrange interpolation in the donor's parameter space,
  applied dimension by dimension (§4.2), is the best combination of accuracy,
  robustness and simplicity. Fourth- and sixth-order explicit interpolation
  reproduce the direct-injection drag history of a cylinder at $Re_D=100$,
  $M_\infty=0.1$; second-order interpolation is worst (§5.3, Fig. 19).
- **High-order donor coordinates.** The donor offsets must themselves be
  accurate to high order. Sherer & Scott (§4.2, Eqs. (11)–(12)) take the
  second-order offsets and stencils from a grid-assembly code, widen the
  stencil symmetrically (one-sided when a candidate donor is unusable), and
  solve for the receptor's position by Newton iteration on the tensor-product
  Lagrange (isoparametric) representation of the donor grid's coordinates,
  starting from the second-order offsets. The coefficients are computed once
  and stored, since the grids are static. Henshaw (2006, §4) requires the
  mappings $\mathbf d_k$ themselves to be smooth enough for high order, or
  spurious reflections appear.

## Compact schemes with holes and fringes

Sherer & Scott (§4) extend the compact (Padé) finite-difference solver of
Visbal and Gaitonde (as recalled there) to general overset grids. The
interior operators are tridiagonal: compact sixth-order differences and a
low-pass Padé filter of up to tenth order on an 11-point stencil, with
one-sided boundary closures. A scheme label such as 45654 gives the order at
the boundary, at the next point and so on to the interior (sixth order
inside, fourth on the boundary); "C6" denotes this scheme.

- **Holes inside implicit operators** (§4.4, Fig. 10). Along each grid line
  that crosses a hole, points within two of the hole boundary use the
  boundary difference formulas and points within five use the boundary
  filters. The rows of hole points are replaced by $\{0,1,0\}$ with zero right
  side, so the system stays tridiagonal and splits into decoupled pieces.
  Hole-boundary points are classified per direction, and each direction must
  keep enough support for the solver and the filter.
- **Fringe and overlaps** (§4.2). A two-point fringe ($n_f=2$) is used at all
  interpolation boundaries; overlapping blocks of one grid (the MPI
  decomposition) share five coincident points, enough to recover interior
  differencing and filtering. Interpolation is applied $T+1$ times per step,
  where $T$ (page-local) is the number of Runge–Kutta stages or implicit
  subiterations, the extra application following the filter.
- **Boundary-filter order** (§5.2, Fig. 15). In the vortex test, a
  second-order boundary filter limits accuracy for all solvers; the uniformly
  sixth-order scheme 66666 is unstable with an eighth-order boundary filter,
  and 45654 is stable with it and matches the single-block sixth-order
  result. In acoustic scattering from a cylinder the second-order boundary
  filter gives spikes at block boundaries, while all one-sided filters of
  order at least four perform well (§5.4, Fig. 24).
- **Cell-size jumps.** Inner-to-outer cell-volume ratios of 4 and 16 in the
  overlap do not degrade the vortex; the filter removes the spurious waves
  generated by the volume jump (§5.2, Fig. 18).
- **Solver comparison.** On scattering from three cylinders, C6 with
  sixth-order interpolation is "nearly indistinguishable" from the analytic
  solution, while an explicit fourth-order scheme on the same five-point
  stencil with fourth-order interpolation shows considerable error (§5.4,
  Fig. 26). Two side-by-side cylinders with centres 1.3 diameters apart at $Re_D=100$
  (seven grids, 32 blocks, sixth-order interpolation) give a fundamental
  Strouhal number of about 0.09, as in experiment (§5.3).

Henshaw (1994) and Henshaw (2006) use explicit centred differences instead,
with two ghost lines carrying numerical boundary conditions; see
[incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md)
and [Maxwell's equations on overlapping grids](/methods/maxwell-equations-on-overset-grids.md).

## Fourier error analysis of interpolation formulas

Sherer & Scott (§2–3, App. A–B) compare interpolation families on one
donor line with unit spacing. Let $q$ donor points carry weights
$\alpha_j$, $j=0,\dots,q-1$, and let $b$ receptors with offsets $\bar s_l$
(in donor spacings from the first stencil point) and coefficients $\varpi_l$
be coupled in one equation ($b$, $\bar s_l$, $\varpi_l$ page-local):
$$\sum_{l=1}^{b}\varpi_l\,u^k_{(l)}=\sum_{j=0}^{q-1}\alpha_j\,u^{k'}_{j}.$$
$b=1$ is ordinary explicit interpolation; $b=3$ couples three receptors in a
tridiagonal ("compact") system. The maximum formal order on a $q$-point
stencil is $q+b-1$ (Eq. (4)); for $b=1$ the weights are the Lagrange weights
(Eqs. (A.9)–(A.10)). With $u=e^{\mathrm i\theta x}$ ($\theta$ the wavenumber in
donor-spacing units, page-local) the local error is
$$E_{\mathrm{loc}}(\theta)=\Big|\sum_l\varpi_le^{\mathrm i\theta\bar s_l}-\sum_j\alpha_je^{\mathrm i\theta j}\Big|^2,$$
($E_{\mathrm{loc}}$ page-local, not the total energy $E$), and its integral over $0\le\theta\le\theta_{\max}$ is the integrated error
(Eqs. (2)–(3)). The findings:

- **Compact versus explicit.** Compact interpolation has local error more
  than an order of magnitude lower at low wavenumbers than explicit
  interpolation on the same stencil (§3.1, Fig. 2), and 0.5–1 decade lower in
  2-D grid-to-grid tests, where measured orders match the formal ones
  (§5.1, Fig. 12). It was nevertheless judged unsuited to overset grids:
  clustered, stacked or too few receptors along a donor line, and receptors
  nearly coincident with donors, make the coupled systems singular or
  ill-conditioned (§4.2). The compact coupling is within one donor grid and
  is not the cross-grid implicit interpolation of Chesshire & Henshaw; see
  [explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md).
- **Stencil position.** The integrated error vanishes when the receptor
  coincides with a donor and peaks near subinterval midpoints; for a 6-point
  stencil the peak rises by an order of magnitude from the central to the
  outermost subinterval (§3.2, Fig. 4a). Adding points on one side to raise
  the order still lowers the integrated error, up to very high wavenumbers
  (§3.2, Fig. 4b). Larger overlap gives more centred stencils.
- **Wavenumber-optimized weights** (Tam–Kurbatskii type, as recalled there):
  minimizing the integrated error over $0\le\theta\le r_{\mathrm o}\pi$
  ($r_{\mathrm o}$ page-local) under order constraints lowers the error at
  high wavenumbers but opens non-monotone error pockets at low wavenumbers
  (§3.1). For explicit 6-point interpolation the gain over non-optimized
  weights reverses below the fitted breakeven line
  $\theta_{\max}/\pi=1.504\,r_{\mathrm o}+0.005$ (Eq. (9), Fig. 6). In
  grid-to-grid tests the optimized weights win on the coarsest grid and lose
  under refinement (§5.1, Fig. 13), so the authors dropped optimization: with
  a low-pass filter there is no point in improving high-wavenumber content.
- **B-splines** with natural-spline end conditions are accurate at the
  stencil centre but poor in outer subintervals, where the error saturates
  independently of the stencil size; they do not converge at a consistent
  rate in the grid-to-grid tests and need a larger overlap (§3.2, §5.1,
  Figs. 7, 12, 19).

## Symmetric operators, energy and dissipation

Henshaw (2006, §5) builds the stability argument for wave equations on the
symmetry of the discrete operator. A three-level scheme
$D_{+t}D_{-t}\mathbf U^n=\mathsf L\mathbf U^n$ ($\mathsf L$ the spatial matrix
with the boundary conditions eliminated, page-local) is stable if and only if
$\mathsf L$ has a complete set of eigenvectors with real negative eigenvalues
$\lambda$ satisfying $-4<\lambda\Delta t^2<0$ (Lemma 5.1); when $\mathsf L$ is
symmetric a discrete energy is conserved. Henshaw therefore writes the
generalized Laplacian in conservation (self-adjoint) form on each curvilinear
grid and approximates it to orders 2, 4, 6 and 8 by operators that are
symmetric in the Jacobian-weighted inner product; these keep the energy
constant to relative $10^{-10}$ over $t\in[0,100]$ on randomly perturbed
grids, where the standard mapping-method operators are unstable without
dissipation (Fig. 2). Details are on
[Maxwell's equations on overlapping grids](/methods/maxwell-equations-on-overset-grids.md).

**Weak instability from interpolation.** On a general overlapping grid the
interpolation equations and the curvilinear boundary conditions make
$\mathsf L$ non-symmetric, so some eigenvalues acquire imaginary parts and the
non-dissipative scheme is weakly unstable at high frequencies (Henshaw 2006,
§3, §9.2, following Reyna's analysis as recalled there). The cure is a
high-order dissipation; for the fourth-order scheme Henshaw adds
$-\alpha_{\mathrm d}(c\Delta t)^2\sum_m\Delta r_m^4(D_{+m}D_{-m})^2(\mathbf U^n-\mathbf U^{n-1})/\Delta t$
with $c$ the wave speed and $\alpha_{\mathrm d}\approx1$ (both page-local), which keeps fourth order when
$\alpha_{\mathrm d}=O(1)$ and can be applied only near boundaries and
interpolation points (Eq. (9.9)); a sixth-order dissipation gave no
significant advantage. The mechanism is argued, not proved.
[Banks et al. (2016)](/sources/banks-2016.md) (§4.2, Eqs. (38)–(40)) meet
the same problem in a second-order upwind solid solver: upwinding does not
damp the zero-speed characteristic variables, which can become weakly
unstable at grid overlaps, and a fourth-order dissipation on those variables
suppresses it. Sherer & Scott's high-order filter plays the same damping
role in the compact solver, though the paper does not frame it as a cure for
an interpolation instability.

## Cost

- Henshaw (2006, §10.5, Table 6): per time step on a 2.2 GHz Xeon, a 2-D
  cylinder grid of 3.8 million points spends 71.4% on the Cartesian grids,
  14.0% on the curvilinear grids, 10.6% on boundary conditions and 0.46% on
  interpolation; a 3-D pill-box of 10.2 million points spends 28.2%, 47.8%,
  14.8% and 6.8%. A fourth-order curvilinear point costs about ten times a
  Cartesian point in 3-D, which is the efficiency argument for overlapping
  grids with Cartesian backgrounds.
- In Henshaw (1994), interpolation takes 2% of a step on a 2-D cylinder grid
  with explicit interpolation and 17% on a 3-D sphere grid with implicit
  interpolation and a high fraction of interpolation points (see
  [explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md)).

## Qualifications

- **Sixth versus fourth order.** In the acoustic-scattering tests fourth-order
  interpolation was slightly better than sixth order; Sherer & Scott attribute
  this to the minimal overlap, which forces more one-sided stencils on the
  higher-order formula (§5.4, §6). The paper does not reconcile it with its
  §3.2 finding that one-sided points still lower the integrated error.
- **Stability evidence.** Henshaw's weak-instability argument and Sherer &
  Scott's filter choices rest on reasoning and numerical tests, not on a
  stability proof for the coupled overlapping-grid scheme.
- **Single-grid order above the formal order.** The single-grid vortex rate
  7.47 exceeds the formal sixth order; Sherer & Scott do not comment.
- **Printed slips in Sherer & Scott (2005):** the convecting-vortex pressure
  (Eq. (17)) is printed with $\exp(-r_2)$; the radial momentum balance of the
  printed velocity field gives $\exp(-r^2)$ *(compiler check, not in the
  sources)*. Eq. (14) is labelled "F1" but is the function F2 of Fig. 12(b).

# Citations

- [Sherer & Scott (2005)](/sources/sherer-2005.md) — §1 (Delfs as recalled), §2, Eqs. (1)–(4); §3.1–3.2, Figs. 2, 4, 6–8, Eq. (9); §4.2 (dimension-by-dimension interpolation, two-point fringe, five-point overlaps, Newton offsets, Eqs. (11)–(12)); §4.4, Fig. 10 (holes in implicit operators); §5.1–5.4, Figs. 12–13, 15–16, 18–19, 24–26; §6; App. A–B.
- [Henshaw (2006)](/sources/henshaw-2006-b.md) — §3, §4 ($q=p+1$, smooth mappings), §5 (Lemma 5.1, symmetric operators, Fig. 2), §9.2 (Eq. (9.9)), §10.5 (Table 6).
- [Henshaw (1994)](/sources/henshaw-1994.md) — §4.1 (quartic interpolation, two receptor lines), Tables V, VIII.
- [Banks et al. (2016)](/sources/banks-2016.md) — §4.2, Eqs. (38)–(40) (dissipation of zero-speed characteristics at overlaps).

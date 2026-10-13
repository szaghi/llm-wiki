---
type: Method
title: "Projection method (divergence cleaning by Poisson solve)"
description: "Removes the divergence of the updated field by solving a Poisson problem and subtracting a gradient; constraint held to solver tolerance."
status: established
aliases: [Hodge projection, divergence cleaning (elliptic)]
tags: [projection, poisson, divergence-constraint]
timestamp: 2026-10-13T00:00:00Z
---

# Projection method

After the base scheme produces a provisional field $B_h^*$, solve
$$D_h^{\mathrm{c}} G_h\, \phi_h = D_h^{\mathrm{c}} B_h^{*},$$
then correct $B_h = B_h^* - G_h \phi_h$, removing the cell-centered discrete
divergence ([notation](/notation.md)) to the tolerance of the Poisson solver.

## Origin

The method is [Chorin (1968)](/sources/chorin-1968.md)'s scheme for
incompressible Navier–Stokes, transplanted to the induction equation:
advance an auxiliary field without the constraint-enforcing gradient, then
perform the **discrete Hodge decomposition**
$u_h^{\mathrm{aux}} = u_h^{n+1} + b^{-1} G_h \phi_h$ with
$D_h u_h^{n+1} = 0$ — keep the divergence-free part, discard the gradient
part into the pressure. Chorin works *collocated* with central $D_h$ and
$G_h$, so his composite Laplacian $D_h^{\mathrm{c}} G_h$ is a five-point
stencil of spacing $2\Delta x$ (the compact staggered alternative is the
[MAC](/methods/mac-method.md) pressure equation, which enforces the same
constraint family through the momentum update rather than as a separate
projection). The existence and uniqueness of the decomposition is inherited
from the well-posedness of the continuous problem. The MHD adaptation
(Brackbill & Barnes) is ingested as
[Brackbill & Barnes (1980)](/sources/brackbill-barnes-1980.md), with the
qualification below; its modern
assessment is [Tóth (2000)](/sources/toth-2000.md). Within the
[GLM framework](/methods/glm-divergence-cleaning.md) the projection is the
elliptic member of the cleaning family — the limit $\mathcal{D}(\psi) = 0$
of the generalized-Lagrange-multiplier coupling
([Dedner et al. (2002)](/sources/dedner-2002.md)). Its subcycled AMR
realization, with the attendant interface synchronization solves, is the
[AMR projection method](/methods/amr-projection-method.md).

**What Brackbill & Barnes actually propose: a qualification.** The
primary source states the correction in one sentence, in continuous form
only (p. 428): solve a Poisson problem for a potential with the divergence
as source and add its gradient to the field. In registry terms this is
$B_h = B_h^* - G_h\phi_h$ with the opposite sign convention for the
potential. The paper gives no discrete operators, boundary conditions,
solver or test, and sets the idea aside: "one can eliminate the parallel
force without having to solve a potential problem". Its adopted cure is a
nonconservative momentum equation that removes the force component along
$\mathbf B$ without reducing the divergence
([exact discrete divergence](/properties/exact-discrete-divergence.md)).
"The MHD adaptation" is therefore an attribution made by later sources,
not a method the paper develops. The bundle's reading of
[Dedner et al. (2002)](/sources/dedner-2002.md) §2 identifies their
elliptic member with the Brackbill–Barnes projection, and
[Jiang & Wu (1999)](/sources/jiang-1999.md) solve the same equation, with
the same sign convention, following Brackbill–Barnes. The discrete MHD
projection as practiced is documented by [Tóth (2000)](/sources/toth-2000.md),
Jiang & Wu and [Balsara & Kim (2004)](/sources/balsara-kim-2004.md).

**What removing it bought one code.** Ryu, Miniati, Jones & Frank replaced
their code's explicit Poisson cleaning with constrained transport. The new
code ran "about 20% faster", which they attribute to "the absence of an
explicit divergence-cleaning step". By their account the cleaning
worked only where boundary effects are negligible or the domain is
periodic on a "more or less regular" grid, and an oblique-field
cloud problem was "difficult to simulate with the old code because of its
lack of a suitable periodic space for solving Poisson's equation"
([Ryu et al. (1998)](/sources/ryu-1998.md) §§1, 2, 3.3).
*Compiler reading:* this sits beside Tóth's ≈6% overhead below without
contradicting it; the two are different codes and Poisson solvers, and the
cost of the elliptic step is implementation-dependent.

## Properties, per [Tóth (2000)](/sources/toth-2000.md)

* **Accuracy is preserved:** the projection scheme is consistent and retains
  the base scheme's order of accuracy *even for discontinuous solutions* —
  proved in the paper against the folklore objection that projecting across
  shocks degrades the solution.
* **Tolerance-, not roundoff-level:** the constraint is enforced to the
  (iterative) Poisson solver's accuracy each time it is applied — a weaker
  guarantee than CT's algebraic invariant, but applied in the more natural
  cell-centered stencil $D_h^{\mathrm{c}}$, and it *removes* initial-condition
  divergence rather than merely preserving it
  ([exact discrete divergence](/properties/exact-discrete-divergence.md)).
* **Global, grid-flexible:** requires a global elliptic solve (CG-type
  iterative methods; parallelizable), and is the only scheme in Tóth's
  comparison applicable to unstructured grids.
* **Cheap in practice:** ≈6% CPU overhead in 2D relative to the base scheme;
  identical to the base scheme whenever $D_h^{\mathrm{c}} B_h^* = 0$ already.
* **Top-ranked:** among the most accurate and reliable schemes across the
  ten-problem comparison (Table IX).

## High-order finite-difference use

[Jiang & Wu (1999)](/sources/jiang-1999.md) pair a fifth-order point-value WENO finite-difference scheme for MHD,
with dimension-by-dimension Lax–Friedrichs flux splitting, with a Poisson
correction of the updated field, solved by relaxation. The paper does not
specify the discrete divergence and gradient stencils, or whether the
correction is applied per Runge–Kutta stage.
* **Without it the scheme fails.** Orszag–Tang on $192^2$ loses pressure
  positivity and blows up, at $t \approx 3.9$ with Powell's $8\times8$
  eigensystem and at $t \approx 2.5$ with the $7\times7$ one. With the
  correction both run to $t = 8$ and agree.
* **Without it the waves are wrong.** On a Brio–Wu shock tube rotated by
  $45°$ on a $600^2$ grid, the uncorrected run shows spurious oscillations
  at the slow rarefaction inside the compound wave. The corrected run
  matches the 1D solution.

This is the elliptic route to divergence control above second order, which
[GLM](/methods/glm-divergence-cleaning.md)'s high-order finite-difference
realization was later designed to avoid.

## Variants and the non-locality failure mode

[Balsara & Kim (2004)](/sources/balsara-kim-2004.md) separate three variants
and test them against a staggered-mesh CT scheme on supernova-driven,
radiatively cooling MHD turbulence:

| Variant | Operator | Exact? | Defect |
|---|---|---|---|
| wide-stencil scalar (Chorin's $D_h^{\mathrm{c}} G_h$) | $2\Delta x$ Laplacian | $D_h^{\mathrm{c}} B_h = 0$ exactly | even–odd decoupling into $2^3$ sub-lattices |
| compact-stencil scalar | 7-point Laplacian | no (a different residue after each pass) | not exact |
| spectral vector | $\delta_{ij} - k_ik_j/k^2$ per mode | in Fourier space only | periodic uniform boxes only; no AMR |

All three share the elliptic step's **non-locality**. A localized divergence
source corrects the field everywhere, with a $1/r^2$ fall-off that is slower
still for sheet-like sources. Applied every step, the correction
accumulates. Persistent converging flows, such as colliding cooling shells,
build divergence locally, and the projection spreads the defect across the
box. The measured result: magnetic-energy spikes (the scalar variants
saturate about 10× too high), polluted shell interiors, shifted field
histograms and excess small-scale power. Only the local CT scheme was clean.
The spectral variant fluctuates but eventually returns to the CT energy
level.

## The iterated collocated projection

When the velocity and the potential share the same nodes, the composite
Laplacian is not the composition of the nodal divergence and gradient, so
$I - G\,L^{-1}D$ is not a projection: one pass leaves a residual
divergence. [Blomquist, West, Binswanger & Theillard (2024)](/sources/blomquist-2024.md) turn this into a convergent procedure on non-graded
quadtrees and octrees.
* **The limit is exact.** The operator leaves discretely divergence-free
  fields unchanged, and its eigenvalue-1 eigenspace is exactly the
  incompressible space. If the iteration converges, its limit is the
  canonical projection onto that space.
* **Stability through the staggered complex.** On periodic uniform grids
  the nodal divergence and gradient are the staggered $D_h$ and $G_h$
  ([notation](/notation.md)) composed with linear node–edge
  interpolations that are transposes of each other, while the nodal
  Laplacian equals the staggered $D_h G_h$. Since averaging has norm at
  most one, the operator is a contraction, and its spectrum lies in
  $[0, 1]$.
* **On adaptive grids** a sufficient condition for convergence is a
  spectral-radius bound below 1 on a product of the interpolations. The
  only free ingredient is the ghost-value rule used by the divergence at
  hanging nodes (see the
  [AMR projection method](/methods/amr-projection-method.md)). The
  condition is not proved for the rule used, and boundary effects are
  outside the analysis; stability is verified numerically.
* **In practice** one to three passes reach a tolerance of $10^{-3}$, and
  a single pass already gives second order in velocity and potential. The
  constraint class is therefore tolerance-level.

*Compiler reading:* this answers the "different residue after each pass"
of the compact-stencil variant in the table above. The residue is not
noise: under the contraction condition, repeated passes converge to the
exact projection.

## Contradictions

**Is projection as good as an exactly divergence-free local scheme?**

* [Tóth (2000)](/sources/toth-2000.md): the projection scheme is consistent
  and order-preserving even for discontinuous flows, and ranks among the most
  accurate and reliable in a ten-problem 2D comparison (above).
* [Balsara & Kim (2004)](/sources/balsara-kim-2004.md): on a stringent 3D
  turbulence problem every projection variant gives spurious energetics,
  structures, statistics and spectra. They judge the scalar variants
  unsuitable for turbulence and dynamo studies.

**Scoped reading (compiled, open).** The two claims are measured on
different problem classes:
* Tóth's tests are standard 2D problems in which divergence is created and
  advected.
* Balsara & Kim's failure needs *persistent, converging* flows that keep
  regenerating divergence in one place for many steps. There the
  non-locality of a per-step global correction accumulates.

Neither result refutes the other, and no supersession is recorded. The
open question is whether a projection error is benign when it is created
locally once, or damaging when it is re-created in place. That is the same
distinction met at
[GLM's `Contradictions`](/methods/glm-divergence-cleaning.md) for interface
sources.

# Citations

1. [Chorin (1968)](/sources/chorin-1968.md), eqs. (3)–(5), (20)–(22).
2. [Tóth (2000)](/sources/toth-2000.md), §5, §7, Table IX.
3. [Dedner et al. (2002)](/sources/dedner-2002.md), §2.
4. [Balsara & Kim (2004)](/sources/balsara-kim-2004.md), §§II.a–c, III.b, Table I.
5. [Jiang & Wu (1999)](/sources/jiang-1999.md), §§1, 3.1, 3.4.
6. [Blomquist, West, Binswanger & Theillard (2024)](/sources/blomquist-2024.md), §§1, 3, 4.2.
7. [Brackbill & Barnes (1980)](/sources/brackbill-barnes-1980.md), pp. 428–429.
8. [Ryu, Miniati, Jones & Frank (1998)](/sources/ryu-1998.md), §§1, 2, 3.3.

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
$u_h^{\mathrm{aux}} = u_h^{n+1} + G_h \phi_h$ (the gradient scaled by the
inverse of the coefficient of the new time level in Chorin's time
discretization) with $D_h u_h^{n+1} = 0$ — keep the divergence-free part, discard the gradient
part into the pressure. Chorin works *collocated* with central $D_h$ and
$G_h$, so his composite Laplacian $D_h^{\mathrm{c}} G_h$ is a five-point
stencil of spacing $2h$ (the compact staggered alternative is the
[MAC](/methods/mac-method.md) pressure equation, which enforces the same
constraint family through the momentum update rather than as a separate
projection). The existence and uniqueness of the decomposition is inherited
from the well-posedness of the continuous problem. The MHD adaptation
is attributed to
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

**Two early MHD implementations.** Before those, two Godunov-type MHD
codes stated discrete operators for the collocated projection, both
citing Brackbill & Barnes.
* [Zachary, Malagoli & Colella (1994)](/sources/zachary-malagoli-colella-1994.md)
  §2.4 "follow the prescription in [4]" and apply a Hodge projection at the
  end of each step, with second-order central gradient and divergence
  ($G_h$ and $D_h^{\mathrm{c}}$), which "leads to nonstandard
  discretizations of the Laplacian" solvable by multigrid. The projection
  is optional (§4). Eq. 34 as printed (a Poisson equation whose source is
  the divergence with the sign of Brackbill & Barnes, then *subtraction*
  of the potential's gradient) doubles the divergence if taken literally
  (checked on the page images); one sign must be flipped, and the intent
  is unambiguous.
* [Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md) §2.4,
  eqs. 2.23–2.24, project after every time step of a Strang-split TVD
  code. The printed operator is the wide $2h$ Laplacian with the
  central divergence of the provisional field as source, i.e.
  $D_h^{\mathrm{c}} G_h\,\phi_h = D_h^{\mathrm{c}} B_h^*$ with
  $\phi_h$ the negative of their potential (their correction adds the
  gradient).
  The gradient stencil of the correction is not printed; the factored
  Laplacian implies the central one. The solve is by FFT, on a box doubled
  with "an appropriate symmetry" (unspecified) when the boundaries are not
  periodic.

Both are instances of the wide-stencil row of the variants table below.
Neither reports a residual divergence.
*Accounts differ, a qualification.* Ryu, Jones & Frank (§2.4) say that
Zachary et al. used the Brackbill–Barnes modified equations, found "no
discernible differences with and without the correction", and "abandoned
the correction". Zachary et al. present the projection as an option they
keep; [Ryu et al. (1998)](/sources/ryu-1998.md) §1 group them with
explicit cleaning.

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

**An early objection, untested.** Dai & Woodward object that the
"clean-up" needs global information, "not favored in the existing parallel
computers", and that it evaluates the divergence by derivatives, so the
cleaned field is divergence-free "only to the accuracy of a numerical
scheme" ([Dai & Woodward (1998, ApJ)](/sources/dai-woodward-1998-b.md) §1;
[Dai & Woodward (1998, JCP)](/sources/dai-woodward-1998.md) §1). Neither
paper runs a projection; their own remedy is a staggered CT update
([flux-CT](/methods/flux-ct.md)).

**The cleaning step's cost in its own paper.** The cleaning that Ryu et al.
(1998) removed is the FFT projection of
[Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md) §2.4. It
cost "≲5% of the total CPU time" with periodic boundaries and "≲30%" with
reflecting or continuous boundaries, which need the doubled box.
*Compiler reading:* the 1998 saving of about 20% is compatible only with
the non-periodic cost; the 1998 timing does not state its boundary type.

**A third early implementation: the modified wavenumber.**
[Balsara (1998)](/sources/balsara-1998-b.md) §5 projects the collocated
field of a TVD Godunov code by FFT on periodic boxes.
* He calls "traditional" the solve with the inverse squared continuous
  wavenumber (eqs. 5.2–5.4, citing Zachary et al.), and reports that on a
  random vector field it leaves the central divergence $D_h^{\mathrm c}$
  of eq. 5.1 "not exactly zero".
* His fix writes the projection as the tensor $\delta_{ij} - k_ik_j/\lvert\mathbf k\rvert^2$
  and replaces each wavenumber component by the central-difference symbol
  $\sin(k_ih)/h$ (eqs. 5.5–5.6). This "makes equation (5.1) exactly zero".
  No residual value is printed.
* The printed signs of eqs. 5.2–5.3 repeat the inconsistency of Zachary et
  al.'s eq. 34 noted above.
* Cost: "no more than 2% of the total computational cost" (§6.2.2).

*Compiler reading:* with the central-difference symbol the tensor is the
Fourier form of $B_h = B_h^* - G_h\phi_h$ with
$D_h^{\mathrm c} G_h\,\phi_h = D_h^{\mathrm c} B_h^*$ and central $G_h$,
so it is the wide-stencil row of the variants table below, not the
spectral-vector row, which is his "traditional" version. The modes where
the symbol vanishes ($\mathbf k = 0$ and the grid-scale mode) are not discussed
in the paper; the existing note on the Ryu–Jones–Frank FFT solve below
covers them. Balsara's characterization of the earlier projections is
the subject of an Open entry under `Contradictions`.

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

**Round-off with a direct solve: a qualification.** The tolerance
limitation above belongs to iterative Poisson solvers, not to projection
as such. [Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md)
solve the wide-stencil equation by FFT, which "can provide an exact
solution … if the field structure is periodic" (§2.4). With the central
gradient that matches $D_h^{\mathrm{c}} G_h$, the corrected field then has
$D_h^{\mathrm{c}} B_h = 0$ to round-off, the level the variants table
below calls "exactly". The paper calls the constraint "enforced exactly"
but measures no residual.
*Compiler reading:* the Fourier symbol of the wide Laplacian also vanishes
at the two-cell-period (grid-scale) mode, not only at the constant mode. The symbol of
$D_h^{\mathrm{c}}$ vanishes there too, so the FFT solve is consistent; the
undetermined $\phi_h$ component has zero central gradient and does not
change the correction.

## High-order finite-difference use

[Jiang & Wu (1999)](/sources/jiang-1999.md) pair a fifth-order point-value WENO finite-difference scheme for MHD,
with dimension-by-dimension Lax–Friedrichs flux splitting, with a Poisson
correction of the updated field, solved by relaxation. The paper does not
specify the discrete divergence and gradient stencils, or whether the
correction is applied per Runge–Kutta stage.
* **Without it the scheme fails.** [Orszag–Tang](/benchmarks/orszag-tang-vortex.md) on $192^2$ loses pressure
  positivity and blows up, at $t \approx 3.9$ with Powell's $8\times8$
  eigensystem and at $t \approx 2.5$ with the $7\times7$ one. With the
  correction both run to $t = 8$ and agree.
* **Without it the waves are wrong.** On a Brio–Wu shock tube rotated by
  $45°$ on a $600^2$ grid, the uncorrected run shows spurious oscillations
  at the slow rarefaction inside the compound wave. The corrected run
  matches the 1D solution.

**At second order, one code saw no effect: a qualification.** Zachary,
Malagoli & Colella report for their 2D problems, including Orszag–Tang on
$192^2$ for 300 steps ("approximately 2 Alfven transit times"), that they
"did not find any noticeable difference regardless of whether or not we
applied a projection" (§2.4). This does not contradict Jiang & Wu. The
base schemes differ (second-order Strang-split Godunov on a nonconservative
momentum form against fifth-order WENO on the conservative form), and so do
the time windows: Jiang & Wu's uncorrected runs fail at $t \approx 2.5$–$3.9$
and the corrected ones run to $t = 8$. Neither paper reports a divergence
value on the test
([Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)).

This is the elliptic route to divergence control above second order, which
[GLM](/methods/glm-divergence-cleaning.md)'s high-order finite-difference
realization was later designed to avoid.

## Variants and the non-locality failure mode

[Balsara & Kim (2004)](/sources/balsara-kim-2004.md) separate three variants
and test them against a staggered-mesh CT scheme on supernova-driven,
radiatively cooling MHD turbulence:

| Variant | Operator | Exact? | Defect |
|---|---|---|---|
| wide-stencil scalar (Chorin's $D_h^{\mathrm{c}} G_h$) | $2h$ Laplacian | $D_h^{\mathrm{c}} B_h = 0$ exactly | even–odd decoupling into $2^3$ sub-lattices |
| compact-stencil scalar | 7-point Laplacian | no (a different residue after each pass) | not exact |
| spectral vector | $\delta_{ij} - k_ik_j/\lvert\mathbf k\rvert^2$ per mode | in Fourier space only | periodic uniform boxes only; no AMR |

All three share the elliptic step's **non-locality**. A localized divergence
source corrects the field everywhere, with a fall-off inverse-square in distance that is slower
still for sheet-like sources. Applied every step, the correction
accumulates. Persistent converging flows, such as colliding cooling shells,
build divergence locally, and the projection spreads the defect across the
box. The measured result: magnetic-energy spikes (the scalar variants
saturate about 10× too high), polluted shell interiors, shifted field
histograms and excess small-scale power. Only the local CT scheme was clean.
The spectral variant fluctuates but eventually returns to the CT energy
level.

**Does the stencil matter? The same author, six years apart: a
qualification.** [Balsara (1998)](/sources/balsara-1998-b.md) §6.2.2
(p. 149) states that "the discretized formulation in which this
divergence-free condition for the magnetic field is imposed is not as
important in obtaining good results as the fact that it is indeed
imposed". The comparison above finds an order of magnitude between
variants, with the wide-stencil scalar variant (the 1998 modified-symbol
projection, per the compiler reading above) saturating about 10× too
high. The regimes differ: short 2D shock and vortex tests against long 3D
turbulence with persistent converging flows, and the 1998 paper compares
no two formulations directly. The two statements do not meet.

## The iterated collocated projection

When the velocity and the potential share the same nodes, the composite
Laplacian is not the composition of the nodal divergence and gradient, so
subtracting the nodal gradient of the potential obtained by inverting that
Laplacian on the nodal divergence is not a projection: one pass leaves a
residual divergence. [Blomquist, West, Binswanger & Theillard (2024)](/sources/blomquist-2024.md) turn this into a convergent procedure on non-graded
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
  accurate and reliable in a ten-problem 2D comparison (§7, Table IX).
* [Balsara & Kim (2004)](/sources/balsara-kim-2004.md) (§III.b, Figs. 2–6): on a stringent 3D
  turbulence problem every projection variant gives spurious energetics,
  structures, statistics and spectra. They judge the scalar variants
  unsuitable for turbulence and dynamo studies.

**Status: Open.** Scoped reading (compiled): the two claims are measured on
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

**Does the loss of local conservation after projection corrupt jump conditions at discontinuities?**

* [Tóth (2000)](/sources/toth-2000.md) §5.3 (pp. 621–622, eqs. 41–44), the
  source of "Accuracy is preserved … *even for discontinuous solutions* —
  proved in the paper against the folklore objection that projecting across
  shocks degrades the solution" above. Magnetic flux is conserved globally,
  but local flux conservation "is a more delicate problem", "especially
  next to discontinuities, where the correctness of the jump conditions
  relies on the conservation properties of the scheme" (p. 621). That "the
  discontinuities are correctly represented" is stated as what "numerical
  experience shows" (p. 621), not as a consequence of the proof: eqs. 41–44
  show that the projected scheme is consistent, with an order no worse than
  that of the base scheme or of any CT/CD scheme (eq. 44). Its "Green
  function" changes the field by more than 5% only within 4 cells
  (Fig. 7).
* [Dai & Woodward (1998, ApJ)](/sources/dai-woodward-1998-b.md) §1 (p. 317):
  "the clean-up may destroy the conservative property of a Godunov scheme";
  afterwards the conservation laws for the three field components (and for
  total energy; see the scoped note below) hold only to truncation
  accuracy, "and truncation errors may be O(1) near MHD discontinuities".
  The companion [Dai & Woodward (1998, JCP)](/sources/dai-woodward-1998.md)
  §1 (p. 332) says the same of the field alone. Asserted; no projection is
  run.

**Status: Open.** Both claims concern the same thing: local conservation
of the field after projection, at discontinuities. Tóth cites
[Dai & Woodward (1998, ApJ)](/sources/dai-woodward-1998-b.md) (his
ref. 11) but names no source for the "quite widely believed" objection, so
the entry is not answered explicitly. Scope note (compiler): Tóth's proof
bounds an error norm, which does not exclude O(1) pointwise errors in a few
cells at a front, while Dai & Woodward's claim is that such errors spoil
the jump conditions. Neither paper measures the jump conditions of a
projected scheme on an oblique strong shock, the test Dai & Woodward name.

*Visual evidence at 45° only, not a jump-condition measurement.*
[Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md) §3.1
projected after every step on strong-shock tubes rotated by 45° ($256^2$
cells): the capture of the shocks and the contact is "virtually the same
as with the one-dimensional code".
[Jiang & Wu (1999)](/sources/jiang-1999.md) §3.1 projected the Brio–Wu
tube rotated by 45° on a $600^2$ grid; the corrected run agrees with their
1D solution on 800 points. Both runs use the 45° angle, which the
[rotated shock tube](/benchmarks/rotated-shock-tube.md) page qualifies as
a special case, and neither reports post-shock states against the exact
jump conditions.

**Scoped note: energy.** For Tóth, total energy is an independent
variable, so a projection "does not affect the total energy at all"
(p. 621); exact total-energy conservation is given up only by the optional
eq. 40, which keeps the thermal energy of the base scheme. Dai & Woodward's
energy claim holds only for that variant (compiler reading).

**Which projection did Ryu, Jones & Frank (1995) use?**

* [Balsara (1998)](/sources/balsara-1998-b.md) §6.2.1 (p. 147): Dai &
  Woodward (1994b), Zachary et al. (1994) and Ryu, Jones & Frank
  ("1996" in the text; the list gives ApJ 452:785, 1995) "experimented
  with only the less accurate version of the divergence cleaning step",
  the version he defines in §5 as the FFT solve with the continuous
  wavenumber, which does not zero the central divergence (eqs. 5.2–5.4; the accurate version is eqs. 5.5–5.6).
  No equation of theirs is quoted.
* [Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md) §2.4,
  eqs. 2.23–2.24, as the bundle reads them (above): the printed Poisson
  operator is the wide $2h$ Laplacian with the central divergence
  as source, solved by FFT. Its Fourier symbol is the square of the
  central-difference symbol, i.e. Balsara's own "accurate" operator, not
  the continuous-wavenumber one. The gradient stencil of the correction
  is not printed; with the central one implied by the factored
  Laplacian, $D_h^{\mathrm c}B_h = 0$ to round-off.

**Status: Open.** Both are claims about the same RJF projection, and they
are incompatible on the printed Laplacian. Scope notes (compiler): the
bundle read the arXiv preprint of RJF, so a change in the refereed ApJ
version cannot be excluded; and if RJF's unprinted gradient were not the
central one, their corrected field would not zero $D_h^{\mathrm c}$ either,
which would make "less accurate" true in effect though not in Balsara's
definition. For Zachary et al. the characterization is also inexact
without being incompatible: they use central operators with a
"nonstandard" Laplacian solved by multigrid, i.e. the wide-stencil row to
solver tolerance, not the continuous-wavenumber FFT. Dai & Woodward
(1994b) is not ingested.

# Citations

1. [Chorin (1968)](/sources/chorin-1968.md), eqs. (3)–(5), (20)–(22).
2. [Tóth (2000)](/sources/toth-2000.md), §5 (§5.3, pp. 621–622, eqs. 40–44), §7, Table IX.
3. [Dedner et al. (2002)](/sources/dedner-2002.md), §2.
4. [Balsara & Kim (2004)](/sources/balsara-kim-2004.md), §§II.a–c, III.b, Table I.
5. [Jiang & Wu (1999)](/sources/jiang-1999.md), §§1, 3.1, 3.4.
6. [Blomquist, West, Binswanger & Theillard (2024)](/sources/blomquist-2024.md), §§1, 3, 4.2.
7. [Brackbill & Barnes (1980)](/sources/brackbill-barnes-1980.md), pp. 428–429.
8. [Ryu, Miniati, Jones & Frank (1998)](/sources/ryu-1998.md), §§1, 2, 3.3.
9. [Zachary, Malagoli & Colella (1994)](/sources/zachary-malagoli-colella-1994.md), §§2.4, 3.2.2, 4, eq. 34.
10. [Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md), §§1, 2.4, 3.1, eqs. 2.23–2.24.
11. [Dai & Woodward (1998, ApJ)](/sources/dai-woodward-1998-b.md), §1.
12. [Dai & Woodward (1998, JCP)](/sources/dai-woodward-1998.md), §1.
13. [Balsara (1998)](/sources/balsara-1998-b.md), §§5, 6.2.1–6.2.2, eqs. 5.1–5.6.

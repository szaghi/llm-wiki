---
type: Property
title: "Exact discrete divergence"
description: "The algebraic invariant $D_h B_h = 0$: a specific discrete divergence of the evolved field vanishes identically, up to machine roundoff."
status: established
tags: [divergence-constraint, invariant, mhd]
timestamp: 2026-10-13T00:00:00Z
---

# Exact discrete divergence

The property that a scheme's evolved magnetic field satisfies
$$D_h B_h = 0$$
*algebraically* — the discrete divergence operator
$D_h : V_h^2 \to V_h^3$ ([notation](/notation.md)) annihilates the evolved
field by construction of the update, so the constraint holds to machine
roundoff at every step, independent of resolution, time step, or solution
smoothness. The velocity analog $D_h u_h = 0$ (incompressibility) is the
older sibling: the [MAC method](/methods/mac-method.md)
([Harlow & Welch (1965)](/sources/harlow-welch-1965.md)) already enforced
the face-difference stencil $D_h^{\mathrm{f}} u_h = 0$ cell-by-cell — though
by elliptic solve (tolerance-level), not algebraically.

Key structural facts, per [Evans & Hawley (1988)](/sources/evans-hawley-1988.md):

* **The constraint is initial data, not dynamics.** Analytically,
  $\nabla\cdot\mathbf{B}=0$ is preserved by the induction equation but not
  enforced by it; discretely the same holds — a scheme with this property
  preserves divergence *changes* at zero, so initial data must satisfy the
  constraint (edge-differencing a vector potential yields exactly
  divergence-free initial fields in the matching discrete sense), and
  boundary inflow can still inject violation.

**The invariant lives on the evolved field only.** In [DeVore (1991)](/sources/devore-1991.md)'s staggered FCT every stage is an edge-flux update and keeps $D_h^{\mathrm f}B_h$, while the single-component low-order fields used to size the limiter "are not divergence-free, but they are used solely to correct their associated partial antidiffusive fluxes" (Appendix, p. 157).

* **The operator is scheme-specific.** "Exact" is always relative to one
  particular $D_h$ — for [constrained transport](/methods/constrained-transport.md)
  it is the face-flux difference over a cell, $D_h^{\mathrm{f}}$
  (Evans & Hawley eq. 4.9, the discrete Gauss theorem). A field exactly
  solenoidal in one discretization is generally not solenoidal in another.
  [Tóth (2000)](/sources/toth-2000.md) makes the stencil-dependence
  systematic: the collocated recast of the CT variants conserves the
  corner-centered $D_h^{\mathrm{k}}$ but *not* the natural cell-centered
  $D_h^{\mathrm{c}}$
  ([CT–finite-volume equivalence](/results/ct-finite-volume-equivalence.md));
  central-difference schemes conserve $D_h^{\mathrm{c}}$ to roundoff; the
  [projection method](/methods/projection-method.md) enforces
  $D_h^{\mathrm{c}}$ to solver tolerance;
  [eight-wave](/methods/eight-wave.md) bounds it by truncation error only.
* **No stencil choice is physically privileged.** For conservative
  shock-capturing schemes, no discrete divergence constraint eliminates all
  unphysical Lorentz-force effects — exact orthogonality of the discrete
  acceleration to $B_h$ in every cell is incompatible with momentum
  conservation
  ([conservation–orthogonality incompatibility](/results/conservation-orthogonality-incompatibility.md));
  Tóth: the choice of discretization "is always somewhat arbitrary."
* **Roundoff behavior.** The invariant is exact in exact arithmetic; in
  floating point it accumulates roundoff at a problem-dependent rate
  (Evans & Hawley observe drift from $10^{-15}$ to $10^{-10}$ in single
  precision over one run; double-precision field evolution holds
  $10^{-15}$–$10^{-14}$).
* **Flux-CT's primary source asserts the property; it neither proves nor
  measures it.** [Balsara & Spicer (1999)](/sources/balsara-spicer-1999.md)
  derive the invariant from "a discrete version of Stokes' theorem" and the
  earlier CT literature, without writing the divergence out, and report no
  divergence diagnostic for their scheme in any test. Their wording is also
  inconsistent: "up to the computer's round-off error" (abstract), "to
  machine accuracy" (§2.2), but "strictly solenoidal up to discretization
  error" (§4). *Compiler reading:* their face update (eqs. 13–15) is
  $B_h^{n+1} = B_h^n - \Delta t\, C_h E_h^{n+1/2}$ with one $E_h$ per edge,
  so $D_h^{\mathrm{f}} B_h$ is conserved by $D_h C_h = 0$; the update
  supports the round-off reading, and the §4 phrase is best read as loose
  wording ([flux-CT](/methods/flux-ct.md)).

* **Field-CT's primary sources assert the face invariant and measure
  another.** [Dai & Woodward (1998, JCP)](/sources/dai-woodward-1998.md)
  define exactness as a zero area-weighted net face flux in every cell,
  $D_h^{\mathrm f} B_h = 0$ (eqs. 15–16), and state that it stays "exactly
  the same as its initial value all the time in all these simulations"
  (§4), without printing a value. Their split-updated cell field $B_h^{*}$
  is not held: its divergence is "interpolation-dependent" and "O(1) if
  strong shocks are involved" (§5).
  [Dai & Woodward (1998, ApJ)](/sources/dai-woodward-1998-b.md) give the
  only numbers: the net cell flux computed from the cell-centred field
  spans $-4.75\cdot10^{-3}$ to $2.75\cdot10^{-3}$ with the face update and
  $-2.84\cdot10^{-2}$ to $1.74\cdot10^{-2}$ without it, on one shock–cloud
  run (Figs. 18–19; colour-bar ranges, units and interpolation not stated).
  The pattern is the one Londrillo & Del Zanna measure below: one stencil
  exact, another $O(1)$ at fronts.

* **"Local" exactness is a distinct, weaker class.** Locally
  divergence-free DG ([Li & Shu (2005)](/sources/li-shu-2005.md)) builds
  the constraint into element-local polynomial bases — exactly solenoidal
  *inside* each element, at *reduced* cost (a smaller space) — but the
  normal-component jumps across element interfaces are uncontrolled, so no
  global discrete divergence is held. Basis-level exactness within cells
  plus unconstrained interfaces is precisely the pattern the AMR
  transfer problem exhibits at coarse–fine boundaries.
* **Stencil consistency is testable.** The 3D
  [field-loop advection](/benchmarks/field-loop-advection.md) test
  ($(x,y)$-plane loop, $u_z \ne 0$) detects mismatch operationally: if the
  constraint is held on a stencil different from the one used to build the
  $B_z$ fluxes, $B_z$ grows unphysically; round-off-constant $B_z$
  certifies preservation on the *consistent* stencil
  ([Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md)).
* **The same field on two stencils, measured.** On rotated shock tubes an
  upwind-CT scheme holds its staggered $D_h^{\mathrm{f}} B_h$ at
  $10^{-13}$–$10^{-12}$. The central $D_h^{\mathrm{c}}$ of the *same field*,
  interpolated to cell centers, is $O(10$–$100)$ at the fronts. The
  consequence is that a scheme's exactness certifies nothing about a
  divergence computed on another stencil. Monopoles appear wherever the
  momentum fluxes see such a stencil. Cancellation also needs every flux at
  the same stage: time splitting breaks it
  ([Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md)
  §§2.4, 4.2;
  [upwind constrained transport](/methods/upwind-constrained-transport.md)).
* **Exactness is not adequacy without locality.** A wide-stencil
  projection makes $D_h^{\mathrm{c}} B_h$ exactly zero after every pass, yet
  on persistent converging flows it gives spurious energy spikes and
  small-scale power. The causes are even–odd decoupling and the non-local
  elliptic correction. A local exact update of the same field (flux-CT) was
  clean on the same problem
  ([Balsara & Kim (2004)](/sources/balsara-kim-2004.md);
  [projection](/methods/projection-method.md) `Contradictions`). How the
  invariant is enforced matters as much as which stencil holds it.
* **Collocated exactness is a uniform-grid property.** A collocated scheme
  whose curl and divergence share one antisymmetric derivative primitive
  holds $D_h^{\mathrm{c}} C_h^{\mathrm{c}} = 0$ identically. The identity is
  published at fourth order:
  [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md) define $B_h$ as the
  fourth-order central curl of a collocated potential, and the
  commutativity of the central differences gives $D_h^{\mathrm{c}} B_h = 0$
  (their eqs. 6.2, 6.8). The second-order versions are those of Tóth and
  Rossmanith. For tensor-product SBP operators the identity holds through
  the boundary closures too. The kernel of $D_h^{\mathrm{c}}$ is, however,
  larger than the image of $C_h^{\mathrm{c}}$ by grid-oscillation modes
  ([Ranocha, Ostaszewski & Heinisch (2020)](/sources/ranocha-2020.md);
  [exactness theorems](/results/discrete-exactness-theorems.md)). Zaghi's record
  measures $2\cdot10^{-19}$, and exactly 0.0 on a source-free pulse. The
  identity rests on derivatives commuting on a tensor-product grid. A 2:1
  refinement seam breaks that commutation, so the invariant drops to a
  truncation-order seam source
  ([seam divergence source](/results/collocated-seam-divergence-source.md);
  [Zaghi (2026)](/sources/zaghi-2026.md), hypothesis).
* **Time coupling is part of the claim too.** At a 1:1 seam between
  independently stepped blocks, the invariant holds exactly (0.0 for 100
  steps) only if the seam ghosts are refreshed at every Runge–Kutta stage.
  With end-of-step coupling the stage buffers read stale or empty ghosts and
  the divergence leaks ($4.56\cdot10^{2}$ in the negative control). An
  exactness claim is relative to a stencil and to a stage-coupling
  schedule. Value-exact ghost copies are not enough if they arrive at the
  wrong stage ([Zaghi (2026)](/sources/zaghi-2026.md), hypothesis).
  A published motive points the same way for accuracy:
  [Christlieb, Feng, Seal & Tang (2016)](/sources/christlieb-2016.md) choose a single-stage, single-step integrator for AMR because
  multistage Runge–Kutta needs intermediate-stage ghost values that
  time-interpolated ghosts cannot provide to high order.
  *Compiler reading:* the two are distinct claims, one on the invariant and
  one on accuracy, with the same cause: stage-level coupling across a
  seam.
* **Boundary data need not be solenoidal.** In cut-cell CT, ghost fields
  behind an embedded wall are extrapolated and are not divergence-free.
  The invariant still holds on the active faces, because those faces are
  updated only by $-C_h E_h$; the ghost data affect accuracy and boundary
  flux, not $D_h^{\mathrm{f}}B_h$. The converse also holds: evolving one
  field per side of a material interface and joining them by a
  normal–tangential split is accurate only to truncation error, and creates
  monopoles. The fix is one field with one $E_h$ per edge. Measured
  divergence is about $10^{-18}$ on a curved two-material interface
  ([embedded-boundary CT](/methods/embedded-boundary-constrained-transport.md);
  [Jones, McNally & Reynolds (2026)](/sources/jones-2026.md)).

## Why it matters

**Positivity.** For Lax–Friedrichs-type conservative schemes in 2D and 3D,
provable positivity of density and pressure requires a discrete
divergence-free condition on the scheme's own flux stencil. Admissible data
alone do not suffice, at any CFL number or viscosity. The first-order LF
scheme in fact preserves $D_h^{\mathrm{c}}\bar B_h = 0$ exactly
([positivity–divergence coupling](/results/positivity-divergence-coupling.md);
[Wu (2018)](/sources/wu-2018.md)).

**Dynamics.** Nonzero numerical divergence produces an anomalous force component parallel
to the magnetic field, corrupting dynamics ([Brackbill & Barnes (1980)](/sources/brackbill-barnes-1980.md) eq. 8, as
reviewed in [Evans & Hawley (1988)](/sources/evans-hawley-1988.md) §III). At production scale the stakes are
documented: in GRMHD black-hole accretion, "the choice of the
divergence-control method can produce qualitative differences in the
simulation results for scientifically relevant … problems"
([Olivares et al. (2019)](/sources/olivares-2019.md)) — the constraint
class is not a numerical nicety but a physics-level decision.

**The parallel force in its primary source.** Brackbill & Barnes write
the magnetic force in conservation form as the divergence of the Maxwell
stress (eq. 7). Its component along the field is
$$\mathbf B\cdot\nabla\cdot\left(\mathbf B\mathbf B - \tfrac12(\mathbf B\cdot\mathbf B)\,I\right) = (\mathbf B\cdot\mathbf B)\,\nabla\cdot\mathbf B$$
(eq. 8), nonzero whenever $\nabla\cdot\mathbf B \ne 0$. The error is a force
proportional to $\mathbf B$; it matters more the smaller the flow speed is
relative to the Alfvén speed, so it dominates low-β equilibria and
instabilities integrated over many transit times (p. 427). On a uniform
equilibrium in an implicit Lagrangian code, the conservative form drives
field-aligned flows that invert cells, while the nonconservative form
leaves a kinetic energy 1/4000 as large (Figs. 1–2). No divergence value
is reported. Two qualifications:
* The identity holds for the conservative (Maxwell-stress) momentum
  equation only. With the nonconservative force
  $-\mathbf B\times(\nabla\times\mathbf B)$ the parallel component is zero
  for any divergence (p. 429).
* The paper's cure is that nonconservative momentum equation, not the
  enforcement of $D_h B_h = 0$: it removes the parallel force without
  reducing the divergence, at the price of momentum conservation to
  truncation error only. A Poisson correction is named and set aside
  ([projection](/methods/projection-method.md)). Citing it as the case
  for enforcing $D_h B_h = 0$, as
  [positivity–divergence coupling](/results/positivity-divergence-coupling.md)
  does, follows the later literature's reading, not the paper's own
  conclusion.

Later sources repeat the attribution.
[Ryu, Miniati, Jones & Frank (1998)](/sources/ryu-1998.md) §1 add that the
divergence "usually grows exponentially", which they assert without
evidence, and object that the nonconservative momentum form risks
"unphysical results because of the nonconservation of momentum". Their
remedy is a face-centred CT field whose net face flux per cell stays
exactly zero (eq. 18), $D_h^{\mathrm f}B_h^{n+1} = D_h^{\mathrm f}B_h^n$;
they report no measured divergence.

**The earlier statement of the growth claim.** [Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md) §2.4 make the same assertion for their split TVD code: the error "usually grows exponentially during the computations, causing an artificial force parallel to the magnetic field", citing Schmidt-Voigt (1987) "e.g."; it is asserted there too, with no demonstration. [Zachary, Malagoli & Colella (1994)](/sources/zachary-malagoli-colella-1994.md) §2.4 place their own scheme in the truncation-error class: it preserves the constraint "only to the truncation error of the method. In principle, that truncation error could be $O(1)$" at discontinuities.

**Conservation without the constraint, in one test.**
[Dai & Woodward (1998, ApJ)](/sources/dai-woodward-1998-b.md) run one
fully conservative scheme with and without its CT field update on a
Mach-15 shock–cloud problem. The uncontrolled run does not fail, and the
two solutions are "not significantly different, although some differences
exist in small scales", located where the uncontrolled run has its largest
net cell flux (§3, Figs. 12–18). The authors conclude that "it is the
conservation laws which play the crucial role" for supersonic flows (§4),
while the companion paper states that whether divergence errors matter
when conservation is exact "remains unknown"
([Dai & Woodward (1998, JCP)](/sources/dai-woodward-1998.md) §5).
*Compiler reading:* one problem and a visual comparison; it sits beside
the failures without divergence control reported elsewhere in the bundle
for other problems and schemes, and contradicts none of them.

**A regime where it did not matter (preprint).** In driven subsonic
turbulence with a weak seed field, [Pakmor et al. (2026)](/sources/pakmor-2026.md) find no difference that separates
the exact-divergence CT codes from the Powell and Dedner codes. This
holds for dynamo growth, saturation, field-structure statistics and
spectra. The residual differences track numerical dissipation and other
scheme details, and the authors stress the idealized setting.
*Compiler reading:* this scopes the Olivares claim rather than
contradicting it. "Can produce qualitative differences" is not refuted by
one regime where none appear. Nor does it contradict
[Balsara & Kim (2004)](/sources/balsara-kim-2004.md), whose spurious
turbulence statistics came from elliptic projection, a cleaning method
this comparison does not test.
Within CT the same holds for the order of the constraint step: in driven
ISM- and ICM-like turbulence, fifth-order WENO runs with sixth-, fourth-
and second-order CT give identical spectra. The upwind scheme's order is
what extends them, compared with a second-order TVD code ([Seo & Ryu (2023)](/sources/seo-2023.md)).
The regime matters, and a same-code comparison shows where it ends
([Tomida, Sadanari, Takasao & Iwasaki (2026)](/sources/tomida-2026.md)). With weak, space-filling fields, CT and GLM with fixed parameters
agree, CT being less diffusive. With strongly localized fields, GLM carries
divergence error into weakly magnetized regions and creates field there;
with time-varying cleaning speed, a sudden time-step drop produces
spurious amplification by orders of magnitude in a collapsing-cloud run.
*Compiler reading:* this, not a contradiction, is how the
no-difference result of Pakmor et al. should be scoped: their regime is
the one where both papers find agreement.

# Citations

1. [Evans & Hawley (1988)](/sources/evans-hawley-1988.md), §III–IV, eq. (4.7)–(4.9), (5.6).
2. [Tóth (2000)](/sources/toth-2000.md), §1.1, §4.4, §7, Appendix A.
3. [Harlow & Welch (1965)](/sources/harlow-welch-1965.md), eqs. (6)–(10).
4. [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md), §1, §6.
5. [Olivares et al. (2019)](/sources/olivares-2019.md), abstract, §5.
6. [Li & Shu (2005)](/sources/li-shu-2005.md), §1.
7. [Zampa (2024)](/sources/zampa-2024.md) — the 2024 frontier: exact
   face-based invariants now coexist with well-balancing and unstructured
   mixed-element grids in hybrid FV/FE form; collocated high-order FD at
   2:1 AMR interfaces remains outside even the newest synthesis.
8. [Zaghi (2026)](/sources/zaghi-2026.md): issues #21 (§2, E1a), #29, #31; `prism-regression.md` (inter-realm 1:1 anchor).
9. [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md), §§2.4, 4.2, Table 3.
10. [Balsara & Kim (2004)](/sources/balsara-kim-2004.md), §§II, III.b.
11. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §6.
12. [Wu (2018)](/sources/wu-2018.md), Theorems 4.1, 4.3, 4.5.
13. [Ranocha, Ostaszewski & Heinisch (2020)](/sources/ranocha-2020.md), Remark 2.8, Theorems 3.8, 3.19.
14. [Jones, McNally & Reynolds (2026)](/sources/jones-2026.md), §§4.1–4.2, 7.9.
15. [Pakmor et al. (2026)](/sources/pakmor-2026.md), §§6.2, 7 (preprint).
16. [Christlieb, Feng, Seal & Tang (2016)](/sources/christlieb-2016.md), §1.
17. [Seo & Ryu (2023)](/sources/seo-2023.md), §3.9.
18. [Tomida, Sadanari, Takasao & Iwasaki (2026)](/sources/tomida-2026.md), §§3–5.
19. [Balsara & Spicer (1999)](/sources/balsara-spicer-1999.md), abstract, §§2.1–2.2, 4, eqs. 13–15.
20. [Brackbill & Barnes (1980)](/sources/brackbill-barnes-1980.md), pp. 426–430, eqs. 4, 7–8, Figs. 1–2.
21. [Ryu, Miniati, Jones & Frank (1998)](/sources/ryu-1998.md), §1, eqs. 16–18.
22. [Dai & Woodward (1998, JCP)](/sources/dai-woodward-1998.md), §§2, 4, 5, eqs. 15–16.
23. [Dai & Woodward (1998, ApJ)](/sources/dai-woodward-1998-b.md), §§3–4, Figs. 12–19.
24. [Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md), §2.4.
25. [Zachary, Malagoli & Colella (1994)](/sources/zachary-malagoli-colella-1994.md), §2.4.
26. [DeVore (1991)](/sources/devore-1991.md), §2, Appendix.

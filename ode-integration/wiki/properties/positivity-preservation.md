---
type: Property
title: "Positivity preservation in time integration"
description: "A time integrator is positivity preserving if nonnegative data give nonnegative numerical solutions; within SSP theory it holds under $h\\le\\mathcal C h_{\\mathrm{FE}}$, unconditional positivity is limited to first order for linear methods, and nonlinear routes (Patankar-type schemes, adaptive weights, flux limiting, multiderivative, splitting and exponential reformulations) obtain higher order."
status: established
aliases: [positivity-preserving time stepping, positivity preserving coefficient, nonnegativity preservation, unconditional positivity, monotone linear scheme, bound preservation, invariant domain preservation, admissibility preservation]
tags: [positivity, structure-preserving, ssp, stiff, asymptotic-preserving, kinetic]
timestamp: 2026-10-20T10:00:00Z
---

# Positivity preservation in time integration

A time integrator is **positivity preserving** for $y'=f(y)$ if $y_n\ge0$ (or $>0$)
componentwise implies $y_{n+1}\ge0$, either for all $h>0$ (*unconditional*) or under a
step restriction. Densities, concentrations and kinetic distribution functions need
it: a negative value can make the semi-discrete problem ill-posed (for instance a
negative temperature in a Maxwellian) and stops a computation even when the error is
small. In the SSP framework positivity is the special case of a convex functional
(the indicator of the nonnegative cone), so every
[SSP method](/methods/strong-stability-preserving-runge-kutta.md) preserves it under
$h\le\mathcal Ch_{\mathrm{FE}}$ whenever forward Euler preserves it under $h\le
h_{\mathrm{FE}}$ ([Gottlieb et al. 2022](/sources/gottlieb-2022.md), §1, §3.4).

## The first-order barrier

Runge–Kutta and linear multistep methods that preserve positivity **unconditionally**
are at most first order (Bolley & Crouzeix 1978), as recalled by
[Blanes et al. (2024)](/sources/blanes-2024.md) (§9.2.1); the same holds for every general
linear method that is unconditionally positive on all positive ODEs
([Nüßlein et al. 2021](/sources/nusslein-2021.md), §1;
[Torlo et al. 2022](/sources/torlo-2022.md), §1, "general linear methods of order $\ge2$ are
only conditionally positive"). The barrier concerns positivity *in all stages* for all
positive problems: Torlo et al. recall that only first-order linear schemes have
$(I+hA)^{-1}\ge0$ for every $h$ (positive stages on linear problems), while the fifth-order
Radau IIA method is unconditionally positive in its final update on linear problems
(Remark 4.5). The SSP form of the same
fact: implicit methods preserving the forward Euler condition for every $h$ cannot
exceed order 1, backward Euler being the first-order example, as recalled by Gottlieb
et al. (2022, §1, App. A, restating Gottlieb–Shu–Tadmor). For stiff problems this is
the obstacle: the stiff part fixes a small $h_{\mathrm{FE}}$, and a higher-order
implicit method inherits only a bounded multiple of it. Gottlieb et al. illustrate it
on $y'=-10y^2$, $y(0)=10$: the forward Euler bound is $h\le0.1/y_n$, and the second-
and third-order stiffly accurate DIRKs of Kennedy & Carpenter lose positivity for
$h>\frac1{50}$ and $h>\frac1{75}$ and converge to qualitatively wrong solutions (§2.4,
Fig. 1).

## Ways around the barrier

Every route changes the class of methods or adds hypotheses on $f$:

- **Multiderivative methods with a backward derivative condition.** If in addition
  $\lVert y-h^2\dot f(y)\rVert\le\lVert y\rVert$ for $h^2\le\dot kh_{\mathrm{FE}}^2$
  (page-local constant $\dot k>0$), implicit two-derivative methods with nonnegative
  coefficients on $f$ and nonpositive coefficients on $\dot f$ preserve the functional
  for every $h>0$; methods of orders 2, 3 and 4 exist (Gottlieb et al. 2022, Thm. 1,
  §2.3). On $y'=-10y^2$ they stay positive for all steps tested, where the DIRKs fail
  (Fig. 1). See [multiderivative Runge–Kutta methods](/methods/multiderivative-runge-kutta.md).
- **Splitting of a doubled system.** For a problem written as $y'=A(y)y$ (page-local matrix function $A$), the doubled
  system $y'=A(z)y$, $z'=A(y)z$ is split so that each sub-step is a linear problem
  with frozen matrix, solved exactly; the Strang composition yields second-order
  approximations that preserve positivity and mass for every $h>0$, and fail for
  $h<0$ (Blanes et al. 2024, §9.2.1, Eqs. (9.14)–(9.15)). The structural hypothesis on
  $A$ that makes the frozen flows positive is not recorded in the reading notes. See
  [operator splitting](/methods/operator-splitting.md).
- **Exponential reformulation of stiff relaxation.** For a kinetic equation
  $\partial_tF=\frac1\varepsilon\mathcal Q(F)$ penalized by a BGK operator
  $\beta(\mathcal M-F)$, the change of variable
  $\partial_t[(F-\mathcal M)e^{\beta t/\varepsilon}]=\frac{\mathcal Q-\beta(\mathcal M-F)}{\varepsilon}e^{\beta t/\varepsilon}$
  lets any explicit Runge–Kutta method be applied; $\beta$ is chosen as the smallest
  value that keeps $F$ positive, and the inhomogeneous version of Li & Pareschi is
  stated to preserve positivity, high order and the AP property (Dimarco & Pareschi;
  Li & Pareschi; as recalled by [Jin 2022](/sources/jin-2022.md), §5.2, Eqs.
  (5.7)–(5.8); page-local: $F$ distribution, $\mathcal Q$ collision operator,
  $\mathcal M$ local Maxwellian). See
  [exponential integrators](/methods/exponential-integrators.md) and
  [BGK penalization](/methods/bgk-penalization.md).
- **Positive coefficients in splitting.** For parabolic problems splitting
  coefficients must themselves be nonnegative (a negative sub-step runs a diffusion
  backwards); real splittings of order $\ge3$ need negative coefficients, so real
  positive splittings stop at order 2 unless commutators or complex coefficients are
  used (Blanes et al. 2024, §2.6, §6.4). This is positivity of the *method
  coefficients*, a precondition for well-posed sub-steps, not positivity of the
  solution; see the [negative-coefficient barrier](/results/negative-coefficient-barrier.md).

- **First-order linearly implicit diffusion with an inverse-positive matrix.**
  [Liu & Zhang (2023)](/sources/liu-2023.md) keep density and internal energy positive
  in compressible Navier–Stokes under a hyperbolic step $h=O(\Delta x)$, instead of the
  $h=O(\mathrm{Re}\,\Delta x^2)$ of fully explicit positivity-preserving schemes (§1.2),
  with a Strang splitting: the Euler half-steps use SSPRK(3,3) with a positivity limiter
  (the SSP route above), and the viscous step is linearly implicit, Crank–Nicolson for
  the velocity and backward Euler in the internal energy with the viscous heating frozen
  at the midpoint velocity (§2.1, Eqs. (6a)–(6b)). Positivity of that step rests on a
  matrix property rather than on the time integrator: if $(M_{\mathrm d}+hL_{\mathrm d})x=r$
  with $M_{\mathrm d}$ diagonal positive, $L_{\mathrm d}\mathbf 1=0$ and
  $M_{\mathrm d}+hL_{\mathrm d}$ monotone (entrywise nonnegative inverse), then
  $M_{\mathrm d}^{-1}r\ge\epsilon$ implies $x\ge\epsilon$, because the rows of the inverse
  of $I+hM_{\mathrm d}^{-1}L_{\mathrm d}$ are convex weights (§3.3; page-local
  $M_{\mathrm d}$, $L_{\mathrm d}$, $r$, $\epsilon$). Backward Euler on the three-point
  heat stencil gives an M-matrix for every $h$, whereas forward Euler is monotone only
  for $h/\Delta x^2\le\tfrac12$ (§1.3). The authors prove the M-matrix property for every
  $h$ for $Q^1$ interior-penalty DG in two dimensions, given a penalty above
  $\sqrt2/2$ (App. A). For $Q^2$ and $Q^3$ spectral elements the matrix is a product of
  M-matrices, monotone only under a **lower** bound $h\gtrsim C\,\mathrm{Re}\,\Delta x^2$
  ($Q^2$ from Li & Zhang, $Q^3$ "in principle"; Eqs. (16a)–(16b)). The adaptive step
  therefore halves the explicit step when a cell average leaves the admissible set and
  *doubles* the implicit step when a negative internal energy appears (§3.4,
  Algorithms H and CNS); the doubling was triggered only in the first steps of the
  $Q^2$/$Q^3$ Sedov runs (Remark 2). The construction is consistent with the barrier: the
  implicit step is first order, the scheme is at most first order in time, and no
  temporal convergence is reported (§1.4); a lower step bound of this kind is a
  property of the spatial matrix, not of an ODE method. See
  [step-size control](/methods/step-size-control.md) and
  [operator splitting](/methods/operator-splitting.md).

## Patankar-type schemes, adaptive weights and flux limiting

Three further routes escape the barrier by giving up linearity of the method, each with a
different meaning of "unconditional".

- **Patankar-type schemes** for [production–destruction systems](/definitions/production-destruction-system.md).
  Multiplying each production term $p_{ij}$ by $y^{n+1}_j/\varpi_j$ and each destruction
  term $d_{ij}$ by $y^{n+1}_i/\varpi_i$, with positive denominators $\varpi$ computed from
  known values, turns every stage into a linear system with an M-matrix, so the scheme is
  positive and conservative for every $h$ ([modified Patankar methods](/methods/modified-patankar-methods.md)).
  The schemes are nonlinear in the data, so the first-order barrier for linear methods does
  not bind them: [Izzo et al. (2025)](/sources/izzo-2025.md) prove unconditional positivity
  and conservation for multistep schemes of orders up to 6 (Lemmas 2.2–2.3, Table 1), and
  modified Patankar deferred correction reaches arbitrary order
  ([Ciallella et al. 2022](/sources/ciallella-2022.md), §4.3, recalled). Positivity for
  every $h$ is not freedom from step restrictions: Torlo et al. (2022) show that these
  schemes oscillate around steady states above step bounds of order one (for instance $h\le2$
  for MPRK(2,2,1), Thm. 4.7) and fall to order 1 or 2 when a constituent vanishes initially
  (Thm. 5.4, Table 2). [Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) apply a
  Patankar-type correction after an SDIRK step, proving positivity for every $h$ when the
  weights are nonnegative and order $\min(p,q+1)$ (Prop. 3.23).
- **Adaptive Runge–Kutta weights.** Nüßlein et al. (2021) re-choose the weights of each step
  by a linear program that keeps the update nonnegative and the order conditions up to a
  possibly reduced order; every linear invariant is kept because each step is a Runge–Kutta
  step. Positivity is obtained per problem and per step, so it is "unconditional" in a
  data-dependent sense only, and the authors keep the two senses distinct (§1); see
  [adaptive-weight Runge–Kutta methods](/methods/adaptive-weight-runge-kutta.md).
- **Flux limiting of the Runge–Kutta update.** For finite-volume schemes,
  [Kuzmin et al. (2022)](/sources/kuzmin-2022.md) limit antidiffusive fluxes of the final
  update (and, where needed, of the stages) against step-independent bounds; explicit methods
  of any order then preserve bounds, positivity included, under a forward-Euler-type step
  restriction (§3, Eq. (28)). Their Theorem 1 gives a semi-discrete maximum principle: an
  ODE $y_i'=a_i(y)(g_i(y)-y_i)$ with $g$ mapping a box into itself and $0\le a_i\le C$ keeps
  its solution in the box. Bound preservation, invariant-domain preservation and positivity
  preservation are the same notion for different admissible sets (Def. 2). See
  [bound-preserving flux limiting](/methods/bound-preserving-flux-limiting.md).

**Positivity limiters and the CFL price.** With a Zhang–Shu positivity limiter on a WENO5
reconstruction, forward Euler is positive for CFL numbers up to the first Gauss–Lobatto
weight, $\tfrac1{12}$, and SSPRK(5,4) up to about $1.508\cdot\tfrac1{12}$; explicit SSP methods
stop at order 4, and high-order deferred correction cannot be written as a convex
combination of Euler steps, so it has no positivity proof under that bound
(Ciallella et al. 2022, Remark 3.1, Remark 5.4, §6.6). Replacing the time integrator of the
water height by modified Patankar deferred correction removes the positivity restriction:
a dry dam break runs positively at CFL 1.5, at about 18% extra cost (§6.6).
[Babbar & Chandrashekar (2025)](/sources/babbar-2025.md) keep a Lax–Wendroff flux
reconstruction scheme admissible (positive density and pressure) by blending a high-order
and a first-order subcell flux and a Zhang–Shu scaling, which relies on a CFL restriction
of the first-order scheme (Defs. 4–5, Thm. 1, App. A); their error-based step-size
controller also rejects and repeats any step that produces an inadmissible state (§5.2,
Algorithm 3). Rejecting steps is not a general remedy: enforcing positivity of SDIRK steps by
rejection and halving drives the step to its floor on a stiff chemistry problem
(Nurkhametova et al. 2026, Fig. 8).

**Monotone approach versus positivity.** On the linear two-species exchange
$y_1'=-\theta y_1+(1-\theta)y_2$, $y_2'=\theta y_1-(1-\theta)y_2$ (page-local $\theta$), a
Runge–Kutta method neither overshoots the steady state nor moves away from it iff
$0<R(-h)<1$, i.e. iff the Dahlquist mode stays positive (Torlo et al. 2022, Props.
4.3–4.6). A-stable methods always move in the right direction; whether they overshoot
depends on the sign of $R(-h)$, positive for every $h$ for Radau IIA5, Gauss–Legendre 4 or
implicit Euler, and only for $h<2$ for implicit midpoint and trapezoid (Table 1; see
[stability function](/definitions/stability-function.md)).

## Linear positivity of many-stage explicit methods: the role of boundaries

For a linear semi-discretization $y'=Ly$ a one-step method gives
$y_{n+1}=P(hL)y_n$, and the step preserves nonnegativity of all data iff every entry
of the matrix $P(hL)$ is nonnegative; [Dawes (2021)](/sources/dawes-2021.md) (§5–6,
Eqs. (13)–(17), after Hirsch) calls such a scheme monotone and uses the two words
interchangeably for linear schemes. He computes the entries in closed form for
Runge–Kutta–Legendre (RKL) super-time-stepping with up to four stages (App. D) and
numerically beyond, for the 1D cell-centred heat equation written as
$X=I+d_{\mathrm e}\mathbb M$, where $d_{\mathrm e}$ is the mesh
Fourier number of one forward Euler sub-step and $\mathbb M$ the scaled Laplacian with
its boundary closure (page-local symbols); see
[stabilized explicit Runge–Kutta methods](/methods/stabilized-explicit-runge-kutta.md).

- **Neumann and periodic boundaries:** all entries are nonnegative whenever forward
  Euler is, $d_{\mathrm e}\le\frac12$, for first- and second-order RKL with any
  stage count (§6.2–6.3, §7.2, Figs. 13–24). This extends the monotonicity of RKL
  for $s<64$ shown by Meyer et al. through the convex monotone property, an analysis
  that "did not include boundary conditions" (§5).
- **Dirichlet boundaries** (ghost value zero at the ghost-cell centre): every scheme
  except one-stage RKL1 (forward Euler) and two-stage RKL2 has negative entries next
  to the boundary, in up to $s-1$ cells per boundary (§7.1, Fig. 25). The largest safe
  Fourier number falls quickly with $s$: $\frac1{15}(6-\sqrt6)\approx0.24$,
  $\frac1{35}(10-\sqrt{30})\approx0.13$ and $\approx0.08$ for RKL1 with 2, 3, 4 stages,
  $\frac1{35}(15-\sqrt{15})\approx0.32$ and $\frac1{21}(7-\sqrt7)\approx0.21$ (printed
  "$\sim0.18$", a slip; see Qualifications) for RKL2
  with 3 and 4 stages, against $\frac12$ for forward Euler (§6.1.2–6.1.3). With some
  negative entries, nonnegativity of the update depends on the data, through
  $\sum_ja^+_{ij}y_{n,j}\ge\sum_ja^-_{ij}y_{n,j}$ for the positive and negative parts of
  the entries (page-local; Eq. (23)).
- **Remedies on a fixed mesh:** refining near the boundary (positivity then holds
  independently of the mesh width only below the critical Fourier number, §6.1.5), or
  coarsening the boundary cells by grouping $g$ cells (page-local), with $g$ = 4, 5,
  7, 12, 17, 26, 50, 85, 205 for RKL1 and 1, 5, 7, 9, 17, 26, 35, 85, 196 for RKL2 with
  $s=2,\dots,10$, at a visible loss of accuracy (§6.1.6, Table 3, Fig. 12). Skaras et
  al.'s Gegenbauer super-time-stepping is named as a possible alternative (§6.1.4).

The threshold depends on the closure: the face-based Dirichlet closure needs
$d_{\mathrm e}\le\frac13$ already for forward Euler, the ghost-centre closure
adopted by Dawes $\frac12$ (§6.1, Eqs. (18)–(19)). Positivity here is a property of
the method together with the discrete operator and its boundary rows, not of the
stability polynomial alone.

## Positivity uniformly in a stiffness parameter

For the stiff relaxation form $y'=T(y)+\frac1\varepsilon Q(y)$ (page-local: $T$
transport, $Q$ collision or relaxation), a scheme should stay positive under a step
restriction independent of $\varepsilon$ and be
[asymptotic preserving](/definitions/asymptotic-preserving-scheme.md). Ordinary
higher-order IMEX schemes generally violate positivity unless $h$ is restricted in
terms of $\varepsilon$ (Higueras et al., as recalled by Gottlieb et al. 2022, §3.4).
Gottlieb et al. assume (§3.4.1): forward Euler on $T$ preserves positivity for
$h\le h_{\mathrm{FE}}$; backward Euler on $Q$ preserves it for every $h\ge0$ (which
forward Euler positivity does not imply, Remark 1); conservation $\mathcal RQ=0$ for
a linear map $\mathcal R$; equilibria $Q(y)=0\iff y=E(\mathcal Ry)$; and the key,
non-generic property $Q'(y)Q(y)=-C_{\mathcal Ry}Q(y)$ with $C_{\mathcal Ry}>0$
(page-local symbols). Under these, their multiderivative IMEX scheme preserves
positivity for $h\le rh_{\mathrm{FE}}$, $r$ the SSP coefficient of the explicit part,
for **every** $\varepsilon$, because each implicit stage collapses to a backward Euler
step on $Q$ with the nonnegative effective step
$\frac h\varepsilon d_{ii}-\frac{h^2}{\varepsilon^2}\dot d_{ii}C_{\mathcal RY_i}$,
where $d_{ii}\ge0$ and $\dot d_{ii}\le0$ are the stage's diagonal coefficients on the
stiff term and on its time derivative (Prop. 1, Eq. (51)). BGK, Broadwell and hyperbolic relaxation systems satisfy the
property ($C=1$, $\rho$, $1$). In a mixed-regime BGK test ($\varepsilon$ from $10^{-5}$
to $O(1)$) no negative cell average appeared at $h=\frac1{24}\Delta x/v_{\max}$
(§3.5.3, Fig. 8). They present the third-order scheme as the first positivity- and
AP-preserving IMEX method of order three, earlier final-stage derivative corrections
of Hu, Shu & Zhang having stopped at order 2 (§3.4). Hu & Shu (2019) give a
second-order AP and positivity-preserving exponential Runge–Kutta method, as recalled
by Jin (2022, §6.1).

## Positivity failures of IMEX schemes in applications

Outside the structural setting above, the sources report positivity as the practical limit
of higher-order IMEX schemes:

- In gray radiation hydrodynamics, most third-order IMEX pairs that
  [Southworth et al. (2024)](/sources/southworth-2024.md) tried were unstable at the
  hydrodynamic CFL step; they attribute this to higher-order methods producing nonphysical
  negative temperatures at shocks, which their code clips, and report only the one robust
  third-order pair, I-IMEX(3,4,3) (§5.1). They conjecture that pairs without explicit
  evaluations of the implicit operator are less prone to such negativities, and choose all
  their pairs that way.
- [Boscheri & Thomann (2024)](/sources/boscheri-2024.md) state that their second-order
  semi-implicit MHD scheme "is not naturally positivity preserving" (§4.1), although it
  performs well at small densities on their accuracy test.

See [semi-implicit IMEX Runge–Kutta](/methods/semi-implicit-imex-runge-kutta.md) and
[IMEX Runge–Kutta methods](/methods/imex-runge-kutta.md).

## Qualifications

- **Liu & Zhang (2023), App. A.** Their Lemma 4 states that a matrix with positive
  diagonal, nonpositive off-diagonal entries, nonnegative row sums and at least one
  positive row sum is a nonsingular M-matrix; without irreducibility this is false (a
  reducible block with zero row sums is singular), but in their application every row sum
  is strictly positive, so the conclusion stands *(compiler remark, not in the
  sources)*. They also attribute the penalty condition to the positivity of the
  diagonal entries, which are positive for every penalty; the condition makes the
  off-diagonal entries nonpositive.

- The multiderivative route needs $\dot f=f'f$ and a structural condition on it; the
  condition $Q'Q=-CQ$ is special to relaxation-type operators (Gottlieb et al. 2022,
  §3.4.1, "non-generic").
- The exponential-RK claims are recalled by Jin without proof; whether high order
  holds *uniformly* in $\varepsilon$ is not claimed there.
- Positivity of a fully discrete scheme also depends on the spatial discretization
  (limiters, as in the WENO positivity limiter used in Gottlieb et al. 2022, §3.5.3).
- **Patankar-type methods** are positive for every $h$ on production–destruction systems
  at any order, because they are nonlinear schemes; the price is a linear solve per stage,
  oscillation-free step bounds of order one and order loss for vanishing constituents (Torlo
  et al. 2022; summary above, details on
  [modified Patankar methods](/methods/modified-patankar-methods.md)).
- **Hypotheses of the Patankar predictor–corrector.** Nurkhametova et al. (2026, §3.3)
  require nonnegative weights for their positivity proof, while two of the three SDIRK
  methods they test have negative weights, so their positivity guarantee covers only the
  second-order base *(compiler check of the printed tableaux; see the method page)*.
- Deferred-correction variants with Patankar weights and relaxation are cited, not
  analysed, by [Micalizzi & Torlo (2024)](/sources/micalizzi-2024.md) (§1).
- **Dawes's notion and the SSP notion differ.** Dawes's "monotone" is nonnegativity of
  the entries of the one-step matrix for a specific operator; no SSP coefficient is
  computed. The two-stage RKL1 polynomial
  $1+z+z^2/6$ is absolutely monotonic only on about $[-1.27,0]$, against a real
  stability interval of length 6, so the interior monotonicity at
  $d_{\mathrm e}\le\frac12$ comes from the structure of the Laplacian, not from an
  SSP property *(compiler check, not in the sources: $1+z+z^2/6$ and its
  first derivative are nonnegative on $[-(3-\sqrt3),0]$)*. The ghost-centre closure places the boundary value half a cell
  outside the domain, so the thresholds are closure-specific. All results are for 1D
  constant-coefficient diffusion.
- **Printed slips in Dawes (2021).** Dawes prints the four-stage RKL2 Dirichlet
  threshold as "$\frac1{21}(7-\sqrt7)\sim0.18$" (§6.1.3). The closed form equals
  0.2073, the smallest root of the
  boundary entry $2-18d_{\mathrm e}+49d_{\mathrm e}^2-42d_{\mathrm e}^3$ (roots 0.2073, 0.4594, 0.5) so the printed decimal is a slip of the source, not a disagreement,
  and the closed form is used above *(compiler check, not in the
  sources)*. The qualitative statement that the threshold is lower than the three-stage
  one (0.32) holds either way. Several closed-form
  entries in App. D carry coefficient slips (D.8, D.18, D.20) and the analytic heat
  solutions (35)–(36) are printed with the exponential multiplying the constant;
  none changes a sign or a threshold.

# Citations

- [Gottlieb et al. (2022)](/sources/gottlieb-2022.md) — §1, Thm. 1, §2.3–2.4 (Fig. 1), §3.4 (Properties 1–5, Prop. 1, Eq. 51, Remark 1), §3.5.3 (Fig. 8), App. A.
- [Blanes et al. (2024)](/sources/blanes-2024.md) — §2.6, §6.4, §9.2.1 (Bolley–Crouzeix barrier, doubled-system splitting, Eqs. 9.14–9.15).
- [Jin (2022)](/sources/jin-2022.md) — §5.2 (Eqs. 5.7–5.8, exponential reformulation and positivity), §6.1 (Hu & Shu 2019).
- [Dawes (2021)](/sources/dawes-2021.md) — §5 (Eqs. 13–17), §6.1–6.3 (Eqs. 18–30, Table 3, Figs. 1–24), §7 (Fig. 25), App. D.
- [Southworth et al. (2024)](/sources/southworth-2024.md) — §5.1 (negative temperatures, choice of pairs).
- [Boscheri & Thomann (2024)](/sources/boscheri-2024.md) — §4.1 (no positivity guarantee); arXiv v1.
- [Liu & Zhang (2023)](/sources/liu-2023.md) — §1.2–1.4, §2.1 (Eqs. (6a)–(6b)), §3.3 (Eqs. (13)–(16)), §3.4 (Algorithms H, CNS, Remark 2), App. A.
- [Nüßlein et al. (2021)](/sources/nusslein-2021.md) — §1 (barrier for general linear methods, senses of unconditional positivity); arXiv v2.
- [Torlo et al. (2022)](/sources/torlo-2022.md) — §1, Remark 4.5, Props. 4.3–4.6, Table 1, Thm. 4.7, Thm. 5.4 (Table 2); arXiv v5.
- [Ciallella et al. (2022)](/sources/ciallella-2022.md) — Remark 3.1, §4.3, Remark 5.4, §6.6; arXiv v3.
- [Kuzmin et al. (2022)](/sources/kuzmin-2022.md) — Def. 2, Thm. 1, §3 (Eq. (28)); arXiv v2.
- [Izzo et al. (2025)](/sources/izzo-2025.md) — Lemmas 2.2–2.3, Table 1; arXiv v1.
- [Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) — §3.3, Prop. 3.23, Fig. 8.
- [Babbar & Chandrashekar (2025)](/sources/babbar-2025.md) — §5.2 (Algorithm 3), App. A (Defs. 4–5, Thm. 1); arXiv v4.
- [Micalizzi & Torlo (2024)](/sources/micalizzi-2024.md) — §1 (structure-preserving DeC variants cited); arXiv v4.

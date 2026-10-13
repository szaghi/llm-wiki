---
type: Method
title: "Hyperbolic (GLM) divergence cleaning"
description: "Dedner's generalized-Lagrange-multiplier treatment of ∇·B: an extra scalar couples to the induction equation so that divergence errors propagate away at a cleaning speed and are damped, keeping all variables cell-centred; second-order CTU and high-order finite-difference forms, the non-conservative EGLM and entropy-consistent variants, and the consistency conditions on the cleaning speed and damping that time-step changes and AMR violate."
status: established
aliases: [GLM, GLM-MHD, divergence cleaning, mixed hyperbolic–parabolic cleaning, Dedner cleaning, EGLM, ideal GLM-MHD]
tags: [mhd, divergence-free, finite-difference, amr, glm]
timestamp: 2026-10-13T00:00:00Z
---

# Hyperbolic (GLM) divergence cleaning

**System** ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md),
§2, eqs. 4–9; [Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md),
§2, eqs. 1–3). Gauss's law is replaced by
$c_h^{-2}\partial_t\psi_{\mathrm{GLM}} + c_p^{-2}\psi_{\mathrm{GLM}} + \nabla\cdot\mathbf B = 0$.
The induction flux gains the gradient of $\psi_{\mathrm{GLM}}$, and
$$\partial_t\psi_{\mathrm{GLM}} + c_h^2\,\nabla\cdot\mathbf B = -\frac{c_h^2}{c_p^2}\psi_{\mathrm{GLM}}.$$
Both $\psi_{\mathrm{GLM}}$ and $\nabla\cdot\mathbf B$ then obey the telegraph
equation $\partial_t^2\psi_{\mathrm{GLM}} + (c_h^2/c_p^2)\,\partial_t\psi_{\mathrm{GLM}} = c_h^2\nabla^2\psi_{\mathrm{GLM}}$
(Mignone & Tzeferacos eq. 2). Divergence errors travel at the cleaning
speed $c_h$, independently of the flow, so they do not pile up at
stagnation points, and they decay at rate $c_h^2/c_p^2$. Everything is
conservative except the source of $\psi_{\mathrm{GLM}}$, and no staggering
or Poisson solve is needed.
* **Speeds.** The system has nine waves: the seven MHD waves and
  $\pm c_h$. The $\pm c_h$ modes carry jumps only in $B_x$ and
  $\psi_{\mathrm{GLM}}$ (Mignone et al. eqs. 6–7). Both Mignone papers take
  $c_h$ as the largest speed the time step allows, the domain maximum of
  $|v_d| + c_{f,d}$ over directions $d$, recomputed each step (FD eq. 8;
  CTU eq. 15). That choice is disputed (see Contradictions).
* **Damping** is a separate exact step,
  $\psi_{\mathrm{GLM}} \leftarrow \psi_{\mathrm{GLM}}\exp\left(-\alpha_p\,c_h\,\Delta t/\min_d h_d\right)$
  with $\alpha_p = c_h\min_d h_d/c_p^2$ (FD eq. 9). With $c_h$ tied to the
  step the exponent is simply $-\nu\alpha_p$. The dimensionless
  $\alpha_p$ was introduced in the second-order CTU-GLM paper, which calls
  Dedner's recommended $c_p^2/c_h = 0.18$ incomplete because that ratio has
  the dimension of a length (Mignone & Tzeferacos, §3.3, eqs. 26–27).
  * The best value is problem-dependent. Values $\alpha_p \in [0, 1]$
    minimize the divergence; the fifth-order FD scheme uses 0.8 for shock
    tubes and 0.4 for vortices.
  * At second order the optima spread much further: about 0.5 for a 2D
    oblique shock tube, 0.005–0.01 for a 3D one, 0 for the Alfvén wave,
    $\gtrsim 0.01$ and $\gtrsim 0.03$ for 2D and 3D field loops (CTU-GLM,
    §4). "0.8 for shock tubes" is therefore an FD fifth-order value, not a
    general rule.
  * A length-based form writes $c_p^2 = C_r c_h L_{\mathrm{GLM}}$ with a
    fixed $C_r$ (0.18 in Dedner's spirit), so $\alpha_p = \min_d h_d/(C_r L_{\mathrm{GLM}})$
    ([Tomida et al. (2026)](/sources/tomida-2026.md), eq. 20; the $\alpha_p$
    relation is a compiler's conversion). $L_{\mathrm{GLM}} = \min_d h_d$, the
    PLUTO choice, gives $\alpha_p \approx 5.6$, well outside $[0, 1]$.
    $L_{\mathrm{GLM}} = 1$ gives $\alpha_p \approx 0.04$ at $h = 1/128$.
    The two studies optimize different things: Mignone and Tzeferacos the
    divergence norm, Tomida et al. the fidelity of the solution.

**Second order: CTU-GLM** ([Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md),
§3). Colella's corner-transport-upwind integrator with all variables,
$\mathbf B$ included, at cell centres. It is unsplit and single-step,
with 6 Riemann solves per zone and Courant number below 1 in 2D and 1/2
in 3D. The damping source is Strang-split around the advection step
(eq. 6). At each face the linear $(B_x, \psi_{\mathrm{GLM}})$ system is first
solved exactly,
$$B_x^* = \tfrac12(B_{x,L} + B_{x,R}) - \tfrac{1}{2c_h}(\psi_{\mathrm{GLM},R} - \psi_{\mathrm{GLM},L}),\qquad \psi^*_{\mathrm{GLM}} = \tfrac12(\psi_{\mathrm{GLM},L} + \psi_{\mathrm{GLM},R}) - \tfrac{c_h}{2}(B_{x,R} - B_{x,L}),$$
and a seven-wave Roe solver then runs with $B_x^*$ as the normal field
(eqs. 23–25; the same face states appear in [Tomida et al. (2026)](/sources/tomida-2026.md),
eqs. 13–16).

**In a high-order finite-difference scheme** ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md),
§3.1, eqs. 21–24). The $(B_x, \psi_{\mathrm{GLM}})$ pair decouples into a
$2\times2$ linear system with constant eigenvectors. Its two
characteristic fields are reconstructed grid-wide, with no local
projection, and give the interface $B_x$. That value then enters the
usual $7\times7$ MHD eigensystem as a parameter. This makes 16
reconstructions per interface
([characteristic decomposition](/methods/characteristic-decomposition.md);
[conservative finite difference](/methods/conservative-finite-difference.md)).
* Divergence errors stay at $10^{-2}$ or below with shocks, bounded under
  refinement, and saturate for $\alpha_p \gtrsim 0.4$. On smooth 3D
  problems they fall below $10^{-8}$ at $128^3$ (§§4.2–4.3).
* For field-loop advection the best $\alpha_p$ depends on the order:
  above about 0.4 at fifth order, below about 0.2 at third
  ([field-loop advection](/benchmarks/field-loop-advection.md)).

## Energy and entropy: EGLM and ideal GLM-MHD

**EGLM.** Dedner's extended GLM adds the non-conservative sources
$-(\nabla\cdot\mathbf B)\mathbf B$ to the momentum and
$-\mathbf B\cdot\nabla\psi_{\mathrm{GLM}}$ to the energy. It gives up exact
momentum and energy conservation. Mignone and Tzeferacos find it more
robust for strongly magnetized oblique shocks. On a 3D blast at plasma
beta $2\times10^{-4}$, only CTU-EGLM ran: constrained transport failed even
with a minmod limiter (§§2, 4.7, Test 2). The energy of the cleaning
field, $\psi_{\mathrm{GLM}}^2/(2c_h^2)$, is missing from plain GLM. On a
circularly polarized Alfvén wave at plasma beta $1.98\times10^{-4}$, GLM
and CT both make thermal-energy errors of about 30%, and EGLM does not.
Tomida et al. recommend the energy source, and call the momentum source
optional ([Tomida et al. (2026)](/sources/tomida-2026.md), App. B).
This bears on the [positivity](/properties/positivity-preserving.md)
of low-β runs.

**Ideal GLM-MHD, entropy-consistent** ([Derigs et al. (2018)](/sources/derigs-2018.md),
§§2–4). The non-conservative Godunov–Powell terms proportional to
$\nabla\cdot\mathbf B$ are derived as physics: they follow from Maxwell's
equations once monopoles are allowed, and without them the Lorentz force
has a component along $\mathbf B$ of size $-(\nabla\cdot\mathbf B)|\mathbf B|$
(eqs. 2.16, 2.21). The cleaning field enters through a convective
(Lagrangian) ansatz. In field units,
$\partial_t\hat\psi_{\mathrm{GLM}} + c_h\nabla\cdot\mathbf B + \mathbf v\cdot\nabla\hat\psi_{\mathrm{GLM}} = 0$,
the induction flux gains $c_h\hat\psi_{\mathrm{GLM}}\mathsf I$, and the total
energy contains $\tfrac12\hat\psi_{\mathrm{GLM}}^2$ (eqs. 3.16–3.18).
* The system is Galilean invariant: its cleaning waves move at
  $v_x \pm c_h$ instead of $\pm c_h$ (eq. 3.28). The cleaning speed is
  therefore reduced to $c_h = \lambda_{\max} - \max|v|$, so that the time
  step is unaffected; $c_h = \lambda_{\max}$ "may lead to a violation of the
  CFL criterion" (eq. 3.30). That differs from Mignone's rule only because
  the wave speeds differ.
* It satisfies an entropy conservation law (eq. 4.12). Dedner's
  conservative GLM (the system above), EGLM, its Galilean-invariant form,
  and the Mackey–Lim and Tricco–Price variants do not admit
  entropy-conservative or entropy-stable schemes: they leave terms of
  indefinite sign, or a zero entropy variable for the cleaning field
  (§4.1).
* The paper builds an entropy-conservative, kinetic-energy-preserving
  flux $\hat f^{\mathrm{EC}}$ from arithmetic and logarithmic means, and
  entropy-stable fluxes $\hat f^{\mathrm{ES}}$ with Lax–Friedrichs or matrix
  dissipation in entropy variables. Damping stays entropy-stable
  (§§4.2–4.5; [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)).
* In FLASH with block AMR, the scheme gives rotor and Orszag–Tang results
  close to the staggered CT solver. Its cell-centred divergence is
  comparable to that of the CT run, whose face divergence is at machine
  precision (§§5.3–5.4).

## Consistency conditions on the parameters

([Tomida et al. (2026)](/sources/tomida-2026.md), §§2.3, 3, 4.)
$\psi_{\mathrm{GLM}}$ and $\nabla\cdot\mathbf B$ obey the same telegraph
equation only if the fields are smooth and the cleaning operator
commutes with $\partial_t$ and $\nabla$. So $c_h$, $c_p$ and
$L_{\mathrm{GLM}}$ must be constant in time and uniform in space.
* **A time-step-tied $c_h$ breaks this.** In a magnetized Kelvin–Helmholtz
  run, dividing $\Delta t$ by 40 for 100 steps raises $\max|\psi_{\mathrm{GLM}}|$
  about 40 times within 10 steps. When the step recovers, the excess is
  converted into spurious, non-solenoidal ripple fields that dominate the
  weak-field region and do not recover with $L_{\mathrm{GLM}} = 1$ (§3.3).
  A constant $c_h$ is immune.
* **Localized fields leak.** Divergence errors made in a strongly
  magnetized layer travel isotropically at $c_h$ into weakly magnetized
  gas: $|\mathbf B|$ reaches $10^{-4}$ ($L_{\mathrm{GLM}} = 1$) or $10^{-2}$
  ($L_{\mathrm{GLM}} = h$), against $10^{-30}$ initially, at any resolution and
  even with a constant $c_h$ (§3.2). Stronger damping shrinks the region
  but adds artifacts.
* **Stability.** With a constant $c_h$ the KHI run is unstable for
  $c_h \lesssim 1.0$, the maximum flow speed. Exceeding the sound or
  Alfvén speed is not what matters. The authors still recommend
  $c_h \ge \max\sqrt{|\mathbf v|^2 + c_f^2}$ (§§3.1.2, 4.1.2).
* **Recommendations** (§§4.1, 5). Keep $L_{\mathrm{GLM}}$, $c_p$ and $c_h$
  fixed in time and space, with $L_{\mathrm{GLM}}$ larger than the scale of
  interest. If $c_h$ must change, first project the field
  (Brackbill–Barnes) and reset $\psi_{\mathrm{GLM}} = 0$. "The conventional
  implementation with variable transport speed is strongly discouraged."
  Their overall verdict: constrained transport is less arbitrary and more
  robust, and cleaning should be "used with caution".

## On adaptive meshes

* Third-order ADER-WENO and ADER-DG with subcell limiting use GLM on
  cell-by-cell AMR, with time-accurate local time stepping and a constant
  $c_h$ (2 and 4), instead of a staggered field. The
  [MHD rotor](/benchmarks/mhd-rotor.md) then shows none of the spurious
  density and magnetic-pressure oscillations reported for Godunov schemes
  without divergence treatment
  ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4;
  [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.2;
  [high-order AMR](/methods/high-order-amr.md)).
* AMR breaks the consistency conditions in three ways
  ([Tomida et al. (2026)](/sources/tomida-2026.md), §§2.3.3, 3.4):
  * $L_{\mathrm{GLM}} = \min_d h_d$ changes the damping time whenever the
    finest level appears or disappears;
  * each new level halves $\Delta t$, which doubles a time-step-tied $c_h$;
  * level-local time steps make $c_h$ non-uniform in space.
* In AMR collapse of a primordial cloud, a time-step-tied $c_h$ gives a peak
  field of $7.1\times10^{-4}$ G against $6.8\times10^{-9}$ G with CT, five
  orders of magnitude more. A constant $c_h$ with $L_{\mathrm{GLM}} = 1$
  ($4.2\times10^{-9}$ G) agrees with CT (§3.4, Fig. 9). The authors judge
  some published field amplification in such collapses "likely
  artifacts" of the cleaning (§4.3.1).

## Against the alternatives

GLM is not exactly divergence-free, unlike
[constrained transport](/methods/constrained-transport.md), but it keeps
every variable at cell centres.
* **At second order, GLM matches CT** in one code (PLUTO). The
  normal-field errors on 2D and 3D oblique shock tubes are equal
  (0.4 vs 0.4 $\times10^{-2}$; 0.5 vs 0.5 $\times10^{-4}$). Alfvén-wave errors
  are second order and comparable. The eight-wave scheme gives wrong
  normal-field jumps ([Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md),
  Tables 1–3; [grid-oblique shock tubes](/benchmarks/oblique-mhd-shock-tubes.md)).
  This is the earlier work the high-order paper cites for comparable
  accuracy ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §1).
* **In a controlled comparison in Athena++**, CT is the least diffusive,
  and GLM agrees with it only for a large damping length, a large $c_h$
  and fields that are not localized ([Tomida et al. (2026)](/sources/tomida-2026.md),
  §§3, 5).
* For curl involutions, GLM-type curl cleaning needs fast cleaning
  speeds and many extra fields ([Balsara et al. (2023)](/sources/balsara-2023.md), §5;
  [curl-preserving reconstruction](/methods/curl-preserving-reconstruction.md)).

**Later uses (batch 15).** *What "Brackbill–Barnes" refers to*
([Brackbill & Barnes (1980)](/sources/brackbill-1980.md), pp. 426–430;
details on [constrained transport](/methods/constrained-transport.md)).
* *The projection of Tomida et al.'s recommendation.* The note states it
  as $\nabla^2\Phi + \nabla\cdot\mathbf B = 0$, $\mathbf B \leftarrow \mathbf B + \nabla\Phi$,
  in one sentence (p. 428), with no discrete operators, solver or test;
  the name used above is consistent with that formula. The note's own
  remedy is the nonconservative momentum equation, which avoids the
  potential problem.
* *The parallel force.* The note gives the dot product of the conservative
  magnetic force with $\mathbf B$ as $\vert\mathbf B\vert^2\,\nabla\cdot\mathbf B$
  (eq. 8), that is, a component $\vert\mathbf B\vert\,\nabla\cdot\mathbf B$
  along $\mathbf B$; Derigs et al. are quoted above with
  $-(\nabla\cdot\mathbf B)\vert\mathbf B\vert$. Both describe a force along
  $\mathbf B$ proportional to the divergence, with opposite signs; see
  the `Contradictions` entry on the sign of the parallel force below.
* *A precursor of the non-conservative sources.* The note's
  nonconservative momentum equation differs from the conservative one by
  exactly the momentum source $-(\nabla\cdot\mathbf B)\mathbf B$ that EGLM
  and the Godunov–Powell terms add, since
  $(\nabla\times\mathbf B)\times\mathbf B = \nabla\cdot\left(\mathbf B\mathbf B - \tfrac12\vert\mathbf B\vert^2\mathsf I\right) - \mathbf B(\nabla\cdot\mathbf B)$
  (compiler's identity). The choices differ elsewhere: the note's flux
  statement carries the induction term $\mathbf v(\nabla\cdot\mathbf B)$
  (eq. 3), but its scheme drops it and keeps induction and energy
  conservative (eq. 9), where the Godunov–Powell system has sources in
  momentum, induction and energy.

**Later uses (batch 17).** *The origin*
([Dedner et al. (2002)](/sources/dedner-2002.md), §§2–6).
* *A family of cleanings.* $\psi_{\mathrm{GLM}}$ enters the induction flux
  as $\psi_{\mathrm{GLM}}\mathsf I$ and is tied to Gauss's law by a linear
  operator. Setting it to zero gives the Brackbill–Barnes projection;
  $\psi_{\mathrm{GLM}}/c_p^2$ gives parabolic cleaning, rejected because an
  explicit scheme limits $c_p$ by stability;
  $c_h^{-2}\partial_t\psi_{\mathrm{GLM}}$ gives purely hyperbolic cleaning;
  their sum is the mixed form above (eqs. 12–19). The system above, the
  telegraph equation, the conservation of $\rho$, $\rho\mathbf v$,
  $\mathbf B$ and $E$, the nine waves and the $\pm c_h$ modes that alone
  carry jumps in $B_x$ and $\psi_{\mathrm{GLM}}$ are all in the 2002 paper
  (eqs. 17–19, §3, p. 653). The face states $B_x^*$, $\psi^*_{\mathrm{GLM}}$
  of the CTU-GLM paragraph are its eq. 42, with the flux
  $(\psi^*_{\mathrm{GLM}}, c_h^2B_x^*)$ added to any MHD flux that takes
  $B_x^*$ as its normal field (eq. 43), on unstructured triangles.
* *The time-step-tied $c_h$ originates here.* $c_h$ is $\nu$ times the
  smallest triangle height over $\Delta t$, uniform over the grid, "the
  maximal value which is compatible with" the time step, so it is
  recomputed every step (§4, eq. 40, p. 656). The rule the Mignone papers
  use is therefore Dedner's.
* *Damping and the value 0.18.* The exact split step
  $\psi_{\mathrm{GLM}} \leftarrow \psi_{\mathrm{GLM}}\,e^{-\Delta t\,c_h^2/c_p^2}$,
  "unconditionally stable", is eqs. 44–45. Three ways to set $c_p$ are
  offered: a constant $c_p$, whose optimum "significantly depends on the
  grid size and the scheme used"; a fixed per-step factor
  $e^{-\Delta t\,c_h^2/c_p^2}$ (eq. 46); and a fixed $c_p^2/c_h$, with
  which the results are "quite independent of the grid resolution and the
  scheme used". Only the last is run. Its value "about 0.18" is the
  optimum for one test, an advected peak in $B_x$ on $[-0.5, 1.5]^2$ with
  the Dai–Woodward flux, "independent of the grid resolution and the order
  of the scheme" (§5, p. 661, Fig. 2). No unit is discussed. In the
  registry's terms the paper fixes $C_rL_{\mathrm{GLM}} = 0.18$ in the
  problem's length unit, not $L_{\mathrm{GLM}} = \min_d h_d$ (compiler's
  reading).
* *EGLM, as printed.* The two sources quoted above are eqs. 24b and 24d;
  the induction equation has none (eq. 24c). They come from writing the
  Lorentz force of the GLM–Maxwell system as
  $(\nabla\times\mathbf B)\times\mathbf B = \nabla\cdot\left(\mathbf B\mathbf B - \tfrac12\vert\mathbf B\vert^2\mathsf I\right) - (\nabla\cdot\mathbf B)\mathbf B$
  (eq. 22, p. 651) and keeping the second term, which "usually … is
  dropped". A Galilean-invariant variant (eq. 38) adds
  $-(\nabla\cdot\mathbf B)\mathbf v$ to the induction,
  $-(\nabla\cdot\mathbf B)\,\mathbf v\cdot\mathbf B$ to the energy and
  $-\mathbf v\cdot\nabla\psi_{\mathrm{GLM}}$ to the cleaning equation, and
  moves the cleaning waves to $v_x \mp c_h$; it "is no longer
  conservative". The EGLM model of [Zaghi (2026)](/sources/zaghi-2026.md)
  has the $\nabla\cdot\mathbf B$ sources of eq. 38, not of eq. 24
  (compiler's comparison), so "EGLM" names different source sets.
* *Mixed GLM is recommended over EGLM.* "We have observed a significant
  loss of conservation caused by hyperbolic source terms, which are not
  present in the mixed GLM formulation. Thus we recommend using the mixed
  GLM scheme" (§6). EGLM also shows "some problems with the intermediate
  states, which are not present in the GLM case" (p. 664). This qualifies
  the robustness of EGLM reported above: Dedner's tests are on adaptive
  triangles and include no strongly magnetized low-β case (the
  Kelvin–Helmholtz run has $p = 50$, $B_x = 1$), the regime where Mignone
  and Tzeferacos and Tomida et al. found the sources useful.
* *Orders* (Table II, colliding-flow Riemann problem, first-order
  Dai–Woodward flux, $L^1$ errors on a cut): mixed GLM falls from 6.455 on
  1,024 to 0.228 on 1,048,576 elements, with EOC 1.061, 0.875, 0.804,
  1.069, 1.014; mixed EGLM is within 6% of it (5.3% on the finest grid); Powell's source terms give
  EOC 0.880, 0.622, 0.432 and no solution on the two finest grids
  ([grid-oblique shock tubes](/benchmarks/oblique-mhd-shock-tubes.md)).
* *Divergence.* Across the tests, mixed GLM and mixed EGLM have the smallest
  maximum face-jump divergence; on a 2D Riemann problem the GLM variants'
  errors are "at least 50% smaller" than without correction or with
  source terms, and the uncorrected and source-term runs need at least 50%
  more time on the adaptive grid (§5).

* *The counts in the CTU-GLM paragraph.* The 6-solve count is Colella's reduced 3D variant without corner coupling, and the 3D limit of 1/2 is Mignone and Tzeferacos's: [Colella (1990)](/sources/colella-1990.md) (§6) states no 3D Courant limit; his full 3D CTU needs 12 solves ([corner transport upwind](/methods/corner-transport-upwind.md)).

**Later uses (batch 18).** *Powell's source terms at their origin*
([Powell (1994)](/sources/powell-1994.md), §§1–2, eqs. 5–17, ICASE
report).
* *Where they come from.* A Roe-type solver for the full eight-equation
  system, with the normal field not held constant. The primitive-variable
  Jacobian then has a zero row for $B_x$, a "clearly non-physical" zero
  eigenvalue whose mode "will be undamped" (eqs. 6–8). Powell zeroes the
  $\partial_xB_x$ column except for $v_x$ on the diagonal (eq. 9): the seven
  usual waves are unchanged, and an eighth, moving at $v_x$, carries only
  jumps in $B_x$ (eqs. 10–13).
* *The sources as printed* (eq. 14, sign checked on the page image). The
  conservative system, with momentum flux
  $\rho\mathbf v\mathbf v + \mathsf I\left(p + \tfrac12\vert\mathbf B\vert^2\right) - \mathbf B\mathbf B$,
  gets the right-hand side $-\mathbf B\,\nabla\cdot\mathbf B$ in momentum,
  $-\mathbf v\,\nabla\cdot\mathbf B$ in induction,
  $-(\mathbf v\cdot\mathbf B)\,\nabla\cdot\mathbf B$ in energy and none in
  continuity. These are the terms the ideal GLM-MHD paragraph calls
  Godunov–Powell; the report never uses the name "Godunov".
* *Why they remove something* (eq. 15). Expanding the conservative
  equations exposes terms proportional to $\nabla\cdot\mathbf B$
  (for momentum, $-\mathbf B\,\nabla\cdot\mathbf B$ beside
  $\nabla(p + \tfrac12\vert\mathbf B\vert^2) - (\mathbf B\cdot\nabla)\mathbf B$);
  the source "simply acts to remove the terms proportional to ∇·B that
  appear in Equation 2". It vanishes at the PDE level, so "the deviations
  from conservation will be very small".
* *What happens to the divergence* (eqs. 16–17). The original system
  freezes it, $\partial_t(\nabla\cdot\mathbf B) = 0$; with the sources,
  $\partial_t(\nabla\cdot\mathbf B) + \nabla\cdot(\mathbf v\,\nabla\cdot\mathbf B) = 0$,
  so "the quantity ∇·B/ρ is treated as a passive scalar" and "any local
  ∇·B that is created is convected away". Errors thus move with the flow,
  not at a cleaning speed $c_h$. Powell presents the advection as the
  stabilizing feature; Derigs et al. describe the same mechanism as
  accumulation at stagnation points: a difference of evaluation, not of
  mechanism.
* *Attribution.* Powell cites Brackbill & Barnes only for the
  nonconservative momentum equation ("[1]", pp. 6–7); the induction and
  energy sources come from his Jacobian modification. This qualifies
  Tóth's statement that Brackbill & Barnes already contain all the source
  terms, and agrees with the batch-15 block: the 1980 note keeps induction
  and energy conservative.
* *Scope of the report.* First order in space and time, an arithmetic-mean
  interface state, the source evaluated per cell with an unstated discrete
  divergence, one test (a Brio–Wu tube rotated by 45°, normal field off by
  a few percent on the coarse grid and better on the fine one; no norms).
  The EOC of "Powell's source terms" in Dedner et al.'s Table II above
  belong to a later implementation, not to this report
  ([grid-oblique shock tubes](/benchmarks/oblique-mhd-shock-tubes.md)).

On tetrahedra with PNPM schemes up to sixth order, "We did not obtain the correct convergence rates without the use of the divergence cleaning approach … high order schemes alone are not able to resolve the problem of the divergence-free condition". With GLM cleaning, design order is reached. Pure DG is the most efficient for the field components, and intermediate PNPM schemes for $\rho$, $\mathbf v$, $p$ ([Dumbser et al. (2008)](/sources/dumbser-2008.md), §5.2.2, pp. 8227–8228).

## Contradictions

**Should the cleaning speed follow the time step?** *Open.*
* [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md) eq. 8 and
  [Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md) eq. 15: $c_h$ is
  the maximum signal speed compatible with the time step, recomputed each
  step. This is the method as described above, used on all their tests.
* [Tomida et al. (2026)](/sources/tomida-2026.md) §§2.3.3, 3.3, 5: that
  choice violates the assumption under which the cleaning is derived,
  makes spurious divergent fields whenever $\Delta t$ drops abruptly, and is
  "strongly discouraged". Use a constant $c_h$ above the fastest speed of
  the whole run, or project and reset before changing it.
* *Further evidence (added at the 2026-10-13 deep lint).*
  [Derigs et al. (2018)](/sources/derigs-2018.md), §3.7, eq. 3.30, also tie
  $c_h$ to the time step: $c_h$ is the largest eigenvalue minus the
  largest fluid speed in the whole domain, global, chosen so that the
  cleaning waves $v_x \pm c_h$ never shrink the step. The paper does not
  say how often it is updated; since it is built from the current
  largest eigenvalue, it varies in time as the step does (compiler's
  reading). A local $c_h$ is named as future work. On the other side,
  [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4, and
  [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.2, run GLM with a
  *constant* $c_h$ (2 for the Orszag–Tang vortex and the MHD rotor in
  the 2013 paper; 4 for the rotor in the 2015 paper) on cell-by-cell AMR
  with time-accurate local time stepping, and report no spurious density
  or magnetic-pressure oscillations on the rotor (see "On adaptive
  meshes" above). That fits Tomida et al.'s recommendation of a constant
  $c_h$, although neither paper reports a divergence norm or tests a
  time-step-tied $c_h$, so it supports the constant choice without
  refuting the other.
* *Compiler's note on scope, not a resolution:* Mignone's tests have no
  abrupt change of $\Delta t$. Tomida et al.'s failures need one: an
  imposed drop, a new AMR level, or a transient near a discontinuity. Each
  side is supported on its own tests. Whether the time-step-tied choice is
  acceptable for runs with a smooth time-step history is not settled by
  either.
* *Batch 17, the originator (a qualification, not a resolution).*
  [Dedner et al. (2002)](/sources/dedner-2002.md), §4, eq. 40, p. 656,
  define $c_h$ as the largest value the time step allows, recomputed every
  step, and run it on dynamically adapted triangular grids (shock
  reflection, 2D Riemann problem, Kelvin–Helmholtz) with smaller
  divergence errors than without cleaning and no failure. The time step
  is a global minimum over the grid. The paper reports no abrupt drop of
  $\Delta t$, no constant-$c_h$ run and no comparison with constrained
  transport, so it is evidence of the same scope as Mignone's and does
  not test Tomida et al.'s failure case.

**Is constrained transport or cleaning the more robust?** *Open* (recorded
at the batch-8 deep lint; both sides were already in the text).
* [Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md) §4.7: on a 3D blast at plasma beta $2\times10^{-4}$,
  constrained transport "failed even with a minmod limiter" while CTU-EGLM
  ran.
* [Tomida et al. (2026)](/sources/tomida-2026.md) §5: in Athena++, constrained transport is the less
  diffusive and the more robust choice, and cleaning should be "used with
  caution".
* *Scope:* the comparisons differ in the cleaning variant (EGLM with
  non-conservative sources against plain or mixed GLM), the code and the
  tests (an extreme low-β blast against Kelvin–Helmholtz, AMR and wave
  tests). Neither tests the other's failure case. See also
  [constrained transport](/methods/constrained-transport.md).
* *Batch 11 evidence, not decisive.*
  [Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §5.4, run
  staggered constrained transport with multidimensional (MuSIC) edge
  fields on a third-order 3D blast at plasma beta $1.117\times10^{-4}$
  ($257^3$) and report positive density and pressure; they do not say
  which positivity safeguards were active.
  [Balsara & Spicer (1999)](/sources/balsara-1999.md), §3.2, find 2D
  staggered constrained transport at plasma beta about $2.5\times10^{-4}$
  as robust as a zone-centred scheme with projection cleaning (not GLM),
  without saying whether their energy correction (eq. 16) was used.
* *Batch 18, not decisive.* [Balsara (2012)](/sources/balsara-2012.md)
  §3.3: a 3D MHD blast at plasma beta $1.005\times10^{-3}$ run with the
  positivity fix, whose MHD pressure step acts on a divergence-free
  reconstruction of face-centred fields (§2.2), at third order (floors
  alone: pressure "totally corrupted"); §3.3 itself does not name the
  divergence treatment, and no cleaning run is shown.

**What is the sign of the parallel force of the conservative magnetic force?** *Open*
(recorded at batch 15).
* [Brackbill & Barnes (1980)](/sources/brackbill-1980.md), eqs. 7–8 (p. 427):
  for the conservative force
  $\nabla\cdot\left(\mathbf B\mathbf B - \tfrac12\vert\mathbf B\vert^2\mathsf I\right)$,
  its dot product with $\mathbf B$ is $+\vert\mathbf B\vert^2\,\nabla\cdot\mathbf B$.
* [Derigs et al. (2018)](/sources/derigs-2018.md), eqs. 2.20–2.21 (arXiv v3, p. 6): for the same
  force, written $-\nabla\cdot\left(\tfrac12\vert\mathbf B\vert^2\mathsf I - \mathbf B\otimes\mathbf B\right)$,
  its projection on $\mathbf B/\vert\mathbf B\vert$ is $-(\nabla\cdot\mathbf B)\vert\mathbf B\vert$.
* *Compiler's note, not a resolution:* expanding the divergence gives
  $(\nabla\cdot\mathbf B)\mathbf B + (\mathbf B\cdot\nabla)\mathbf B - \tfrac12\nabla\vert\mathbf B\vert^2$,
  whose last two terms have no component along $\mathbf B$, so the
  projection is $+(\nabla\cdot\mathbf B)\vert\mathbf B\vert$, as Brackbill &
  Barnes print. Both papers agree that the force is along $\mathbf B$,
  proportional to the divergence, and unphysical; only the printed sign
  differs. A derivation is not a source.
* *Compiler's reading of Derigs et al.'s eqs. 2.18–2.20 (derivation, not printed):* their eq. 2.18
  writes the Lorentz force with the non-conservative term as
  $-\nabla\cdot\left(\tfrac12\vert\mathbf B\vert^2\mathsf I - \mathbf B\otimes\mathbf B\right) - (\nabla\cdot\mathbf B)\mathbf B$,
  and eq. 2.19 states that its projection on $\mathbf B/\vert\mathbf B\vert$
  is zero; the force of eq. 2.20 is that force plus
  $(\nabla\cdot\mathbf B)\mathbf B$, so its projection is
  $+(\nabla\cdot\mathbf B)\vert\mathbf B\vert$, against their eq. 2.21
  (compiler's reading of eqs. 2.18–2.21, arXiv v3, pp. 5–6). A printed-sign
  erratum in Derigs et al. is the likely reading.
* *Implicit evidence from a production code, for the plus sign
  (hypothesis-grade).* The EGLM model of
  [Zaghi (2026)](/sources/zaghi-2026.md) keeps the conservative
  Maxwell-stress momentum flux and adds the momentum source
  $-(\nabla\cdot\mathbf B)\,\mathbf B$, citing Derigs et al. eqs.
  3.16–3.18; flux and source together give
  $(\nabla\times\mathbf B)\times\mathbf B$, with no component along
  $\mathbf B$. That removal works only if the conservative force has the
  component $+(\nabla\cdot\mathbf B)\vert\mathbf B\vert$ along
  $\mathbf B$, the sign Brackbill & Barnes print. The code never states the
  sign (compiler's reading of its flux and source); its plain GLM model
  adds no momentum source and keeps the parallel force.
* *Batch 17, two peer-reviewed sources for the plus sign (Dedner: printed
  identity; Tóth: printed equation said to come from the Lorentz force;
  projection not printed in either).*
  [Dedner et al. (2002)](/sources/dedner-2002.md) print, as eq. 22
  (p. 651, checked on the page image),
  $(\nabla\times\mathbf B)\times\mathbf B = \nabla\cdot\left(\mathbf B\mathbf B - \tfrac12\vert\mathbf B\vert^2\mathsf I\right) - (\nabla\cdot\mathbf B)\mathbf B$,
  and their EGLM momentum equation (eq. 24b) keeps the conservative
  Maxwell-stress flux with the source $-(\nabla\cdot\mathbf B)\mathbf B$.
  Since $(\nabla\times\mathbf B)\times\mathbf B$ is orthogonal to
  $\mathbf B$, the conservative force has the component
  $+(\nabla\cdot\mathbf B)\vert\mathbf B\vert$ along $\mathbf B$, the sign
  Brackbill & Barnes print; the one-line projection is the compiler's,
  Dedner et al. do not write it. [Tóth (2000)](/sources/toth-2000.md)
  prints the eight-wave momentum equation the same way, conservative flux
  with the source $-(\nabla\cdot\mathbf B)\mathbf B$ (eq. 11, read from
  the text layer), credits all the source terms to Brackbill & Barnes,
  and names acceleration "parallel to the field lines" as the usual
  unphysical effect (§1.1); he states that this form is derived from the
  Lorentz force (§3, ref. [47]), so flux plus source is
  $(\nabla\times\mathbf B)\times\mathbf B$, and the conservative force
  then has the component $+(\nabla\cdot\mathbf B)\vert\mathbf B\vert$
  along $\mathbf B$ (projection by the compiler; Tóth states neither the
  sign nor the cancellation). Appendix A proves that no conservative scheme
  keeps the discrete Lorentz acceleration exactly orthogonal to
  $\mathbf B$ in every cell.
* *Batch 18, the eight-wave origin, for the plus sign (printed expansion,
  projection not printed).* [Powell (1994)](/sources/powell-1994.md), eq. 14,
  keeps the conservative Maxwell-stress momentum flux and adds the source
  $-\mathbf B\,\nabla\cdot\mathbf B$; eq. 15 (page image p. 7) writes the
  conservative momentum equation expanded as
  $\partial_t(\rho\mathbf v) + \nabla\cdot(\rho\mathbf v\mathbf v) + \nabla\left(p + \tfrac12\vert\mathbf B\vert^2\right) - (\mathbf B\cdot\nabla)\mathbf B - \mathbf B\,\nabla\cdot\mathbf B = 0$,
  the last term underlined as one of "the terms proportional to ∇·B that
  appear in Equation 2". The conservative magnetic force is then
  $-\nabla\left(\tfrac12\vert\mathbf B\vert^2\right) + (\mathbf B\cdot\nabla)\mathbf B + (\nabla\cdot\mathbf B)\mathbf B$,
  whose first two terms sum to $(\nabla\times\mathbf B)\times\mathbf B$,
  orthogonal to $\mathbf B$, so its component along $\mathbf B$ is
  $+(\nabla\cdot\mathbf B)\vert\mathbf B\vert$, the sign Brackbill & Barnes
  print. Powell never projects on $\mathbf B$ and never speaks of a force
  along the field: the projection is the compiler's. Powell credits the
  non-conservative momentum equation to Brackbill & Barnes (his ref. [1],
  pp. 6–7).
* *State of the evidence for the human's fiat (compiler's summary, not a
  resolution).* Printed projections: plus, Brackbill & Barnes eq. 8;
  minus, Derigs et al. eq. 2.21 only. Printed identities or forms that
  entail plus by a one-line projection (the compiler's): Derigs et al.
  eq. 2.18 with 2.19–2.20, Dedner et al. eqs. 22 and 24b, Tóth eq. 11,
  Powell eqs. 14–15; code record (hypothesis-grade): Zaghi (2026). No
  source other than eq. 2.21 prints the minus sign, and none addresses
  eq. 2.21; every peer-reviewed plus-side source predates it, so none
  supersedes it, and Powell and Tóth both credit the non-conservative form
  to Brackbill & Barnes. Closing needs a source that supersedes eq. 2.21,
  or the human's fiat.

# Citations

1. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §§1–4 (arXiv v2).
2. [Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md), §§2–5 (arXiv v1).
3. [Derigs et al. (2018)](/sources/derigs-2018.md), §§2–5, incl. §3.7 (arXiv v3).
4. [Tomida et al. (2026)](/sources/tomida-2026.md), §§2–5, App. B (arXiv v2).
5. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4.
6. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.2.
7. [Balsara et al. (2023)](/sources/balsara-2023.md), §5.
8. [Balsara & Spicer (1999)](/sources/balsara-1999.md), §3.2.
9. [Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §5.4.
10. [Brackbill & Barnes (1980)](/sources/brackbill-1980.md), pp. 426–430 (read from page images).
11. [Zaghi (2026)](/sources/zaghi-2026.md), key claims 1–4 (frozen capture at commit 4a3a0815).
12. [Dedner et al. (2002)](/sources/dedner-2002.md), §§2–6, eqs. 12–24, 38, 40–46, Table II (eqs. 22 and 24 checked on the page image).
13. [Tóth (2000)](/sources/toth-2000.md), §§1.1, 3, Appendix A.
14. [Colella (1990)](/sources/colella-1990.md), §6.
15. [Powell (1994)](/sources/powell-1994.md), §§1–4, eqs. 5–17 (ICASE Report 94-24; eqs. 14–15 checked on the page images).
16. [Dumbser et al. (2008)](/sources/dumbser-2008.md), §5.2.2.

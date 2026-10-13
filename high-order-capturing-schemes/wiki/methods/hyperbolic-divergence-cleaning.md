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

**What is the sign of the parallel force of the conservative magnetic force?** *Open*
(recorded at batch 15).
* [Brackbill & Barnes (1980)](/sources/brackbill-1980.md), eqs. 7–8 (p. 427):
  for the conservative force
  $\nabla\cdot\left(\mathbf B\mathbf B - \tfrac12\vert\mathbf B\vert^2\mathsf I\right)$,
  its dot product with $\mathbf B$ is $+\vert\mathbf B\vert^2\,\nabla\cdot\mathbf B$.
* [Derigs et al. (2018)](/sources/derigs-2018.md), eqs. 2.20–2.21: for the same
  force, written $-\nabla\cdot\left(\tfrac12\vert\mathbf B\vert^2\mathsf I - \mathbf B\otimes\mathbf B\right)$,
  its projection on $\mathbf B/\vert\mathbf B\vert$ is $-(\nabla\cdot\mathbf B)\vert\mathbf B\vert$.
* *Compiler's note, not a resolution:* expanding the divergence gives
  $(\nabla\cdot\mathbf B)\mathbf B + (\mathbf B\cdot\nabla)\mathbf B - \tfrac12\nabla\vert\mathbf B\vert^2$,
  whose last two terms have no component along $\mathbf B$, so the
  projection is $+(\nabla\cdot\mathbf B)\vert\mathbf B\vert$, as Brackbill &
  Barnes print. Both papers agree that the force is along $\mathbf B$,
  proportional to the divergence, and unphysical; only the printed sign
  differs. A derivation is not a source: the entry stays open until a
  source settles it or the human closes it.
* *Derigs et al.'s own equations entail the plus sign.* Their eq. 2.18
  writes the Lorentz force with the non-conservative term as
  $-\nabla\cdot\left(\tfrac12\vert\mathbf B\vert^2\mathsf I - \mathbf B\otimes\mathbf B\right) - (\nabla\cdot\mathbf B)\mathbf B$,
  and eq. 2.19 states that its projection on $\mathbf B/\vert\mathbf B\vert$
  is zero; the force of eq. 2.20 is that force plus
  $(\nabla\cdot\mathbf B)\mathbf B$, so its projection is
  $+(\nabla\cdot\mathbf B)\vert\mathbf B\vert$, against their eq. 2.21
  (compiler's reading of eqs. 2.18–2.21, arXiv v3, p. 5). A printed-sign
  erratum in Derigs et al. is the likely reading; closing needs the
  human's fiat.

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

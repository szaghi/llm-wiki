---
type: Source
title: "Godunov (1959) — A difference method for numerical calculation of discontinuous solutions of the equations of hydrodynamics"
description: "Proves that a linear two-level scheme keeps monotone data monotone iff all its coefficients are nonnegative and that no such scheme for linear advection is second order unless the Courant number is an integer; then builds the first-order Lagrangian gas-dynamics scheme on exact interface Riemann problems (solved by fixed-point iteration on the contact pressure) and conservative layer averages, with proofs that limits are weak solutions satisfying the entropy inequality."
resource: "https://www.mathnet.ru/eng/msb4873"
source_kind: paper
authors: [Godunov S.K.]
year: 1959
venue: "Mat. Sb. 47:271–306"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1959-MatSb-Godunov-msb4873.pdf"
tags: [godunov, riemann-problem, monotonicity, impossibility, euler, first-order]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

Godunov looks, for linear hyperbolic equations, for the best difference
scheme among those that map monotone data to monotone data, and then
carries it over by analogy to the Lagrangian equations of gas dynamics.
Chapter I proves that a linear two-level scheme preserves monotonicity
iff all its coefficients are nonnegative (§2), and that for
$\partial_t u = \partial_x u$ no such scheme is second order, explicit or
implicit, on any stencil, unless $\nu$ is an integer (§3): the result the
literature calls Godunov's theorem
([Godunov's order barrier](/results/godunov-order-barrier.md)). The best
monotone three-point scheme is first-order upwind. For the acoustic
system it is reinterpreted physically: its interface values are the
state produced by the decay of the discontinuity (the Riemann problem)
between neighbouring constant layers, and the update is a conservation
balance of these interface fluxes (§5). Chapter II builds the nonlinear
scheme on this picture: piecewise-constant layers, the exact gas-dynamic
Riemann problem at every interface, solved by a fixed-point iteration on
the contact pressure, and a conservative update of the layer averages.
It proves that convergent limits are weak solutions and satisfy the
entropy inequality, gives a Courant-type step rule, and analyses an
accuracy defect at material contacts
([Godunov's method](/methods/godunov-method.md)).

The paper is the Russian original. All quotations and paraphrases below
are the reader's translations; the English translation was not
consulted.

# Key claims

1. **Monotonicity as the requirement** (Ch. I §1, pp. 272–274). A
   difference solution should behave qualitatively like the exact one:
   monotone data should stay monotone. Counterexamples: Crank–Nicolson for
   the heat equation, stable for every ratio $\Delta t/h^2$, always
   destroys the monotonicity of a step when that ratio exceeds $3/2$. For
   $\partial_t u = \partial_x u$ (left-running waves) Lax's first-order
   "triangle" scheme (Lax–Friedrichs) keeps a step monotone for
   $\nu \le 1$; the second-order "tripod" scheme
   $u^{n+1}_i = u^n_i + \tfrac{\nu}{2}(u^n_{i+1} - u^n_{i-1}) + \tfrac{\nu^2}{2}(u^n_{i+1} - 2u^n_i + u^n_{i-1})$
   (Lax–Wendroff form, stable for $\nu \le 1$) produces the value
   $1 + \tfrac12(\nu - \nu^2) > 1$ on a unit step: an overshoot. It is
   the unique second-order scheme on these three points, so no
   three-point second-order scheme is monotone (p. 274).
2. **Monotonicity criterion** (Ch. I §2, pp. 275–276). An implicit
   two-level scheme whose implicit symbol has no roots of modulus 1 is
   uniquely solvable in bounded sequences and can be written in explicit,
   possibly infinite, form: each new value is a fixed linear combination
   of old values. Theorem: the scheme maps every monotone function to a
   monotone function with the same direction of growth iff all
   coefficients of that combination are nonnegative. Proof: the new
   differences are the same combination of the old differences; necessity
   by a unit step placed at a negative coefficient. Corollary: nonnegative
   coefficients summing to 1 (constants reproduced) give max-norm
   stability.
3. **The best first-order monotone scheme** (Ch. I §2, pp. 276–277). The
   first-order three-point schemes for $\partial_t u = \partial_x u$ form
   a one-parameter family in a numerical-diffusion coefficient, second
   order for one value of it, with truncation error proportional to the
   distance from that value times $h^2\partial_x^2 u$. The member closest
   to second order with all coefficients nonnegative is
   $u^{n+1}_i = \nu u^n_{i+1} + (1 - \nu)u^n_i$, stable for $\nu \le 1$:
   upwind differencing, equivalently linear interpolation at the foot of
   the characteristic followed by transport along it.
4. **The order barrier** (Ch. I §3, title and pp. 277–278). "For this
   equation, when $\nu \neq 0, 1, 2, \dots$, there are in general no
   second-order schemes, explicit or implicit, connecting any number of
   points on two successive time levels, that map all monotone functions
   into monotone functions." Second order is *defined* as exactness on
   quadratic data. Proof: the datum $u(x) = (x/h - \tfrac12)^2 - \tfrac14$
   has nonnegative samples $(j - \tfrac12)^2 - \tfrac14$ at every integer
   $j$; exactness gives the new value $(l + \nu - \tfrac12)^2 - \tfrac14$
   at node $l$; nonnegative coefficients (claim 2) would make every new
   value nonnegative, but it is negative at the integer $l$ with
   $l - 1 < -\nu < l$. Scope: linear, constant-coefficient, two-level
   schemes for scalar advection. The test datum is not itself monotone;
   the proof goes through the coefficient criterion
   ([Godunov's order barrier](/results/godunov-order-barrier.md)).
5. **The acoustic system** (Ch. I §4, eqs. 1–4). For a linear $2\times2$
   system with constant coefficients, requiring each Riemann invariant to
   stay monotone and taking the most accurate monotone three-point scheme
   for each gives the first-order scheme (4). Stencils wider than three
   points are excluded on purpose, because boundaries would then need
   special handling, "inconvenient for standardised machine computation"
   (p. 279).
6. **The Riemann-problem reading** (Ch. I §5, eqs. 5–8, pp. 281–283). For
   Lagrangian acoustics, scheme (4) becomes a conservative update (8)
   whose interface pressure and velocity (7) are exactly the state
   between the two acoustic waves of the decay of the discontinuity
   («распад разрыва») between neighbouring constant layers. These values
   stay constant at an interface until waves from the neighbouring
   interfaces arrive, which requires the time step to be below the
   interface spacing over the acoustic speed; "curiously, this inequality
   coincides with the stability condition for scheme (4)" (p. 283). After
   the step a layer is no longer constant, and the new values are its
   averages, obtained from conservation of momentum and volume.
7. **The nonlinear scheme** (Ch. II §2, eq. 4, pp. 285–286). Lagrangian
   1D gas dynamics in velocity, specific volume and specific internal
   energy, with a mass-type Lagrangian coordinate. The gas is split into
   layers (half-integer indices), constant at the start of a step; the
   decay of the discontinuity at every integer point gives an interface
   pressure and velocity; velocity, specific volume and total specific
   energy of each layer are then updated by the differences of the
   interface pressures, interface velocities and interface
   pressure–velocity products. The computed values are layer averages
   that replace the true distribution (p. 286). There is no Eulerian
   fixed-grid version in the paper.
8. **Limits are weak solutions** (Ch. II §3, eq. 5, Fig. 1). If the grid
   functions converge, as the steps are refined, to piecewise smooth
   limits, the limits satisfy the integral conservation laws on every
   contour, i.e. are generalized solutions. Proof: discrete conservation
   (5a) on rectangular contours, plus the fact (§4) that the interface
   values converge to the same limits as the layer values.
9. **Exact Riemann solver by iteration** (Ch. II §4, eqs. 6–8,
   pp. 287–292). Ideal gas. With the left and right mass fluxes through
   the two waves (the paper's $a_0$, $b_0$, its Lagrangian wave speeds
   divided by the scaling constant), the shock relations give
   $$p_* = \frac{b_0\,p^- + a_0\,p^+ + a_0 b_0\,(v^- - v^+)}{a_0 + b_0}, \qquad v_{n*} = \frac{a_0\,v^- + b_0\,v^+ + p^- - p^+}{a_0 + b_0}$$
   (registry symbols, $v^\mp$ the layer velocities). For a shock,
   $a_0 = \sqrt{\left((\gamma+1)p_* + (\gamma-1)p^-\right)\rho^-/2}$; for a
   rarefaction ($p_* < p^-$) the same linear relations hold with
   $a_0 = \frac{\gamma-1}{2\gamma}\sqrt{\gamma p^-\rho^-}\,\dfrac{1 - p_*/p^-}{1 - (p_*/p^-)^{(\gamma-1)/(2\gamma)}}$;
   $b_0$ likewise from the $+$ data. Iteration (8): evaluate $a_0$, $b_0$
   at the previous $p_*$, update $p_*$, then $v_{n*}$. It "converges if
   the decay does not produce very strong rarefaction waves"; for all
   cases a relaxed iteration averages the new and old iterates with the
   weight $\frac{\gamma-1}{3\gamma}\cdot\frac{1 - z}{z^{(\gamma+1)/(2\gamma)}\left(1 - z^{(\gamma-1)/(2\gamma)}\right)} - 1$
   on the old iterate if positive, else 0, with $z$ the previous $p_*$
   over $p^- + p^+$ (p. 292). The convergence analysis is omitted as
   "standard". With $a_0 = b_0$ equal to the constant $\sqrt{A/B}$ of the
   linear model of Ch. I (paper symbols) the formulas reduce to the acoustic (7) of Ch. I
   ([exact Riemann solver](/methods/exact-riemann-solver.md)).
10. **Time step** (Ch. II §4, p. 292). The step is bounded by the
    interface spacing over the largest Lagrangian wave speed of the
    interface problems: a Courant number of 1 with respect to the
    interface-to-interface distance. Godunov states that this is only
    approximately the time for waves from one interface to reach the
    next, but that "a large number of varied computations convincingly
    show" stability under it. If the step is also below the time for
    waves of neighbouring interfaces to *meet* (half of it), the in-layer
    solution is analytically simple (p. 293).
11. **Entropy** (Ch. II §4, eq. 9, pp. 292–294). The exact in-layer
    evolution does not lower entropy, and the convexity of the logarithm
    and of the kinetic energy (Jensen-type inequalities) give the cell
    entropy inequality (9): the specific entropy of the averaged state at
    $t^{n+1}$ is not below that at $t^n$. Hence limits satisfy the
    entropy condition that singles out the physical solution. A footnote
    (p. 294) credits the observation to L. I. Sedov.
12. **Eulerian positions** (Ch. II §5, eq. 10, p. 294). Particle
    positions at integer points move with the interface velocity; the
    specific volume of a layer is then the scaled position difference,
    preserved if it holds initially, and may replace the volume update
    (saving memory). This is position tracking, not a moving-mesh
    formulation.
13. **Material contacts** (Ch. II §§7–8, eqs. 11–16). The material
    interface sits at an integer point, with the left gas's constants for
    the left wave and the right gas's for the right wave. This is
    admissible but costs accuracy: on a linearized model the discrete
    solution near the contact has linear profiles whose extrapolations to
    the contact disagree in velocity and pressure by amounts proportional
    to the difference of the two sides' stable time steps (eq. 16). Cure:
    choose the steps on both sides so that the maximal stable time steps
    agree (pp. 299–300). §8 proves max-norm stability of the contact
    scheme for the linear system (stability in Filippov's sense).
14. **Nonmonotone schemes on shocks** (Ch. II §1, p. 285). Schemes
    without the monotonicity property give "humped" shock profiles with
    humps pulsating from step to step (Appendix I).

# Tests

All tests are graphs; no error tables and no grid-convergence study.

* **Appendix I, Fig. 2 (p. 303).** A travelling shock for a Lagrangian
  $2\times2$ system computed with a second-order (Lax–Wendroff-type)
  scheme: pressure profiles at successive steps show large post-shock
  overshoots (peak above 6 against a plateau of about 4.5–5, read from
  the plot) that pulsate in time. Purpose: show why a nonmonotone scheme
  is unacceptable.
* **Appendix II, Figs. 3–5 (pp. 303–305); §6.** A steady shock,
  $\gamma = 5/3$, computed by the scheme of Ch. II from an exact step at
  point 0, steps 0–18. A stationary profile forms within a few steps and
  travels at the shock speed with the correct jumps, without overshoot
  (a small bump in velocity near the start). A permanent mark in the
  specific volume remains near point 0: the scheme "erred" in entropy
  while the profile formed, and the smooth region conserves the error
  (pp. 294–295) — a start-up entropy error.
* **Appendix III, Figs. 6–7 (pp. 305–306); §6.** A cold gas
  ($\gamma = 5/3$, zero pressure, unit specific volume) hitting a wall,
  with zero interface velocity imposed at the wall in the boundary
  Riemann problem; steps 2–12; a right-running shock forms (pressure
  rises to 4, specific volume drops to about 0.25). The same kind of
  entropy trace appears near the wall; such traces "usually occupy
  two–three computational points" and at fine steps do not affect the
  results (p. 295).
* **Contact error (§7).** Experiments settle near the contact on the
  linear discrete solution of the model; the linearized estimate "gave
  the size of the effect coinciding with that observed in gas-dynamic
  computations" (pp. 295, 299). No figure.
* **Introduction.** "A large number of calculations", some compared with
  the method of characteristics in "quite satisfactory" agreement; no
  data shown.

# Notation map

| Godunov (1959) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$ (Ch. I §§1–3) | $u$ | scalar unknown |
| $u$ (Ch. II) | $v$ (1D $v_x$, $v_n$) | velocity; **collision**: the registry $u$ is the conserved state |
| $v$ | $1/\rho$ | specific volume; **collision**: the registry $v$ is velocity |
| $E$ | words (specific internal energy) | **collision**: the registry $E$ is the total energy density; the registry has only $\rho e(u)$ |
| $p$, $\gamma$ | $p$, $\gamma$ | |
| $P_m$, $U_m$ (Ch. II); $P_{m+1/2}$, $U_{m+1/2}$ (Ch. I) | $p_*$, $v_{n*}$ at the interface | Ch. I numbers interfaces half-integer, Ch. II integer (p. 285) |
| $P_0^{(i)}$ | $p_*$ at iteration $i$ | |
| $a_0$, $b_0$ | words (left and right mass fluxes); kept as $a_0$, $b_0$ on this page only | no registry symbol (proposal: $W_L$, $W_R$); not the Eulerian $S_L$, $S_R$ |
| $p_{\mp1/2}$, $u_{\mp1/2}$, $v_{\mp1/2}$ (decay data) | $p^\mp$, $v^\mp$, $1/\rho^\mp$ | the two layers adjacent to the interface |
| $B$ | words (Lagrangian scaling constant) | **collision**: TVB bound $B$, magnetic field $\mathbf B$ |
| $A$, $B$ (Ch. I linear system) | words | not the flux Jacobian; the Jacobian eigenvalues are $\pm\sqrt{AB}$ |
| $\tau$ | $\Delta t$ | **collision**: WENO-Z $\tau$ |
| $h$ | $h$ | a Lagrangian step in Ch. II |
| $r = \tau/h$ (advection, unit speed) | $\nu$ | **collision**: registry $r$ is the stencil count |
| $r = \tau/h^2$ (heat equation) | words | |
| $c_m$, $c_{n-k}$ | words (coefficients of a linear scheme) | **collision**: sound speed $c$ (proposal: $a^{\mathrm{lin}}_k$) |
| $k$ (Ch. I §2) | words (numerical-diffusion coefficient) | |
| $u^0$; $u_0$, $u_{\pm1}$ | $u^{n+1}_i$; $u^n_i$, $u^n_{i\pm1}$ | the paper puts the new level as a superscript, the old as a subscript (footnote p. 273) |
| $u_{m+1/2}$ (layer) | $\bar u_i$ | layer averages at half-integer indices |
| $S$ | words (specific entropy) | the registry $U(u)$ is the mathematical entropy, of opposite sign; **collision** with the Rusanov $S$ |
| $\alpha^{(i)}$, $z_{i-1}$ | words; $z$ on this page only | relaxation weight; **collision** with the Lax–Friedrichs $\alpha$ |
| $\alpha$, $\beta$, $\delta$, $\theta$ (§7) | words | gradients and offsets of the linear model solution |
| $r_m$ | words (particle position) | **collision** with $r$ |

# Pages created or updated

* Created [Godunov's order barrier for monotone linear schemes](/results/godunov-order-barrier.md) and [Godunov's method](/methods/godunov-method.md).
* Updated [Total variation diminishing](/properties/total-variation-diminishing.md) (batch-14 block: the linear barrier behind the TVD programme).
* Updated [Monotone numerical flux](/definitions/monotone-flux.md) (batch-14 block: origin of the monotone-scheme criterion; the scalar min/max formula is not in this paper).
* Updated [Exact Riemann solver for the Euler equations](/methods/exact-riemann-solver.md) (batch-14 block: Godunov's own iteration and relaxation, the Lagrangian setting, the step rule and the entropy proof).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/1959-MatSb-Godunov-msb4873.pdf`.
   * **Version read.** The published journal pages in Russian
     (Математический сборник, т. 47(89), № 3, 1959, pp. 271–306, 36 PDF
     pages), an OCR'd scan from the Math-Net.ru archive (PDF produced
     2007-08-17). Received 20 March 1956 (p. 306). Not the English
     translation, which the bundle does not hold; every translation on
     this page is the reader's.
   * **Identity.** No DOI exists, so no Crossref check is possible. The
     Math-Net.ru record, fetched 2026-10-13 at
     https://www.mathnet.ru/eng/sm4873, reads "S. K. Godunov, A difference
     method for numerical calculation of discontinuous solutions of the
     equations of hydrodynamics, Mat. Sb. (N.S.), 47(89):3 (1959),
     271–306", received 20.03.1956; every field agrees with page 1 and
     p. 306. The reader recorded the record id as `sm4873`, while the
     archive filename and this page's `resource` use `msb4873`. "89" is
     the old-series continuation number of volume 47.
   * **How it was read.** The OCR text layer for prose; every formula
     reported here read from rendered page images (120 dpi; the
     rarefaction mass-flux formula at 250 dpi). Ch. II §7 eqs. 12–15
     (pp. 296–299) read only in part (poor OCR, pages not rendered in
     full) and not reproduced, except eq. 16, read cleanly from p. 299;
     the §8 recurrences (pp. 301–302) not reproduced, only their
     conclusion. Figure values are read from plots and approximate.
   * **Recorded as printed.**
     - The right-side rarefaction mass flux on p. 290 is printed with
       $(1 - p_*/p^+)^{(\gamma-1)/(2\gamma)}$ in the denominator, while the
       left-side version just below and both entries of system (8) on
       p. 291 have $1 - (p_*/p)^{(\gamma-1)/(2\gamma)}$; the latter follows
       from the stated rarefaction relations (reader's check), so the
       p. 290 form is a misprint.
     - The acoustic step bound on p. 292 is printed
       $\tau \le h/\sqrt{AB} = h/(B\sqrt{B/A})$; the second form equals the
       first only as $h/(B\sqrt{A/B})$.
     - In §5 (p. 294) the energy equation is reprinted with
       $(E + u^2/2)^2$ under the time derivative, a misprint of eq. (1).
     - First page 271, confirmed on page 1. Several citing sources print
       357.
   * **Reference list:** 4 entries (von Neumann & Richtmyer 1950; Lax
     1954; Landau & Lifshitz 1955; Filippov 1955), all merged. Von Neumann
     is printed "J. Neumann", without "von", and lands on the existing
     `vonneumann-1950` (J. Appl. Phys. 21:232). Landau & Lifshitz is the
     1955 Russian edition of *Mechanics of Continuous Media*, kept apart
     from the bundle's English editions. The bibliography note of
     `godunov-1959` now records the first page 271 as confirmed on page 1
     (citing sources print 271 or 357). Bibliography: 3104 entries.

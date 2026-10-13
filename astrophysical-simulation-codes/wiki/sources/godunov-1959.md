---
type: Source
title: "Godunov (1959) — Разностный метод численного расчета разрывных решений уравнений гидродинамики"
description: "Origin of Godunov's method: the best monotone two-level scheme for linear advection and acoustics, reinterpreted as the decay of the discontinuity (Riemann problem) at each cell interface followed by a conservative cell-average update, extended to 1D Lagrangian gas dynamics with an exact iterative ideal-gas Riemann solver; proves the monotonicity criterion, the absence of monotone linear second-order two-level schemes, consistency of convergent limits with the conservation laws, and a cell-average entropy inequality."
resource: "https://www.mathnet.ru/eng/msb4873"
source_kind: paper
authors: [Godunov S.K.]
year: 1959
venue: "Mat. Sb. 47(89):271–306"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/1959-MatSb-Godunov-msb4873.pdf"
tags: [hydro, riemann-solver]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper is in Russian; its title translates as "A difference method for
the numerical calculation of discontinuous solutions of the equations of
hydrodynamics" (every English rendering on this page is the reader's
translation). Godunov looks for the "best" two-level difference scheme
that maps monotone data to monotone data, first for linear advection and
the linear acoustic system (Ch. I), then carries it over to the nonlinear
Lagrangian gas-dynamics equations (Ch. II). He proves that a linear scheme
is monotonicity-preserving iff all its coefficients are non-negative
(Ch. I §2), and that no linear two-level scheme of second order is
monotone for a non-integer Courant number (Ch. I §3). The best monotone
first-order scheme for acoustics turns out to be: solve, at each
interface, the decay of the discontinuity between the two adjacent
constant states («распад разрыва», the Riemann problem), and update the
cell averages conservatively with the interface values (Ch. I §§4–5).
Ch. II applies this to 1D Lagrangian gas dynamics with an exact ideal-gas
Riemann solver iterated for the interface pressure, proves that convergent
solutions are weak solutions and satisfy the entropy inequality, gives the
time-step condition, and analyses an error at contacts between two gases.
Three appendices show a stationary shock and a wall-impact test. This is
[Godunov's method](/methods/godunov-method.md).

# Key claims

Equations are in the [registry](/notation.md) notation where it has the
symbols, otherwise in words (see the Notation map). The paper's model
equation $\partial_t u = \partial_x u$ has wave speed $-1$; $\nu$ below is
its Courant number $\Delta t/h$.

1. **Monotonicity is the requirement** (Ch. I §1, pp. 272–274). A
   Crank–Nicolson-type scheme for the heat equation, stable for every
   step, is non-monotone in its first step on step data when the
   diffusion number exceeds $3/2$. For advection, Lax's first-order
   "triangle" scheme is monotone for $\nu \le 1$ but turns data into
   linear functions at small $\Delta t$ and smears contacts (p. 271); the
   second-order "tripod" scheme is stable for $\nu \le 1$ but overshoots
   a step to $1 + (\nu - \nu^2)/2 > 1$ for $\nu < 1$.
2. **Monotonicity criterion** (Ch. I §2, pp. 274–276). An explicit linear
   scheme, each new value a weighted sum of old ones, maps every monotone
   grid function to a monotone one of the same direction iff all weights
   are non-negative (sufficiency from the differences of consecutive new
   values, necessity from a step). Implicit schemes whose characteristic
   equation has no root of modulus 1 reduce to explicit form and are
   covered. If the weights also sum to 1, the scheme is stable in the
   maximum norm (p. 276).
3. **Best monotone first-order scheme** (Ch. I §2, pp. 276–277). Among the
   three-point first-order schemes, the one with non-negative weights
   closest to second order is upwind,
   $u^{n+1}_i = \nu\,u^n_{i+1} + (1 - \nu)\,u^n_i$, stable for $\nu \le 1$:
   linear interpolation at the foot of the characteristic.
4. **Order barrier** (Ch. I §3, pp. 277–278). "For this equation, at
   $\nu \ne 0, 1, 2, \dots$, there are no second-order schemes at all,
   explicit or implicit, connecting any number of points at two
   successive time levels, that map all monotone functions into monotone
   ones" (reader's translation). Second order means exact on quadratics;
   the proof uses a quadratic that is non-negative at the nodes but whose
   exact translate is not. Schemes with more than two time levels are
   excluded explicitly (p. 275).
5. **Acoustics: the interface Riemann problem** (Ch. I §§4–5,
   pp. 278–283, eqs. 4–8). For the linear acoustic system, requiring each
   Riemann invariant to stay monotone and taking the most accurate
   monotone three-point scheme for each gives eq. 4. Rewritten in
   Lagrangian pressure–velocity form (eqs. 7–8), its interface pressure is
   the mean of the two cell pressures minus half the acoustic impedance
   times the velocity jump, and its interface velocity the mean of the two
   velocities minus the pressure jump over twice the impedance: exactly the
   state between the two acoustic waves that the discontinuity at the
   interface decays into (p. 282). The new cell values are averages, from
   momentum and volume conservation. The interface values stay constant
   until waves from the neighbouring interfaces arrive, a time that
   "coincides with the stability condition of scheme (4)" (p. 283). Wider
   stencils were rejected because they need "significant modifications
   near boundaries, inconvenient for standardized machine computation"
   (p. 279).
6. **Nonlinear scheme** (Ch. II §§1–2, pp. 283–286, eq. 4). For the 1D
   Lagrangian Euler equations (velocity, specific volume $1/\rho$,
   specific internal energy $e$), cells carry piecewise-constant data;
   the Riemann problem at each interface gives an interface pressure and
   velocity; momentum, volume and total energy are updated conservatively
   from their differences across the cell. The new values are only the
   cell averages of a no longer constant distribution (p. 286).
7. **Convergent limits are weak solutions** (Ch. II §3, pp. 286–287,
   Fig. 1). If the scheme converges under refinement to a piecewise-smooth
   limit, that limit satisfies the integral conservation laws, by the
   discrete conservation law on rectangular contours.
8. **Exact ideal-gas Riemann solver** (Ch. II §4, pp. 287–292). For an
   ideal gas the interface pressure is the mean of the two pressures
   weighted by the opposite side's Lagrangian wave speed (mass flux
   through the wave), plus the product of the two speeds times the
   left-minus-right velocity jump, all over the sum of the speeds; the interface velocity
   follows likewise. Each wave speed has a shock branch, the square root
   of $\rho\,[(\gamma + 1)\,\text{interface pressure} + (\gamma - 1)\,p]/2$
   of its side (from the Hugoniot adiabat), and a rarefaction branch (from
   the Riemann invariant and the adiabat), chosen by whether the current
   interface-pressure iterate exceeds that side's pressure (eq. 8, p. 291).
   The iteration is fixed-point, said to converge "if very strong
   rarefaction waves do not result"; a relaxed iteration with a printed
   relaxation weight is given for convergence in all cases, with the
   convergence analysis omitted (p. 292). In the acoustic limit the
   formulas reduce to item 5.
9. **Time step** (Ch. II §4, p. 292). The linear condition is the
   wave-interaction time; for the nonlinear scheme Godunov takes $\Delta t$
   at most $h$ over the largest Lagrangian wave speed of the step's
   Riemann problems, admitted to be only approximately that time and
   justified by "a large number of diverse runs" that were stable.
10. **Entropy inequality** (Ch. II §4, p. 293, eq. 9). By the convexity of
    the logarithm and of the squared velocity, the cell-average entropy
    after a step is not below its value before (for $\Delta t$ below the
    wave-interaction time), so the limit satisfies the entropy
    inequality. A footnote (p. 294) credits L. I. Sedov with first noticing
    the fact.
11. **Eulerian positions** (Ch. II §5, p. 294). Interface positions advance
    with the interface velocity; the specific volume is then the
    position difference over the mass interval (eq. 10), which can replace
    the volume update.
12. **Contact between two gases** (Ch. II §7, pp. 295–300, eqs. 11–16). A
    linearized analysis gives a stationary discrete solution whose
    velocity and pressure, extrapolated to the interface, jump by amounts
    proportional to the difference between the two sides' cell sizes over
    their acoustic speeds, i.e. between their maximal stable time steps
    (eq. 16). Remedy: choose the cell sizes so that the two stable time
    steps nearly agree; the effect "was almost not observed" and agreement
    with the method of characteristics improved (p. 300).
13. **Stability at contacts** (Ch. II §8, pp. 300–302). For the linear
    two-medium system with Courant number below 1 on each side, each
    update has coefficients whose absolute values sum to 1, so the maximum
    norm does not grow: stability in Filippov's sense is proved.

# Tests

No error tables; validation is stated: many runs on Soviet computers,
some compared with the method of characteristics, with "quite
satisfactory" agreement (Introduction, p. 271). Figure values below are
read off the plots, not printed.

1. **Analytic first steps** (Ch. I §1). Heat-equation step data
   (non-monotone above a diffusion number of $3/2$); advection step data
   with the triangle (monotone) and tripod (overshoot) schemes.
2. **Stationary shock, second-order scheme** (Appendix I, Fig. 2, p. 303):
   pressure profiles with large overshoots (peak about 6 against a
   post-shock level about 4.7), the "humped" shocks with pulsating humps
   that p. 285 attributes to non-monotone schemes.
3. **Stationary shock, this scheme** (Appendix II, Figs. 3–5,
   pp. 303–305). $\gamma = 5/3$, started from a step satisfying the shock
   conditions; pressure 0 to about 4, velocity 0 to about $-1.75$,
   specific volume 1 to 0.25, plotted at steps 0–18. A stationary profile
   forms within a few steps and moves with the correct speed and jumps
   (§6, p. 294). An **entropy trace**, a mark in the specific volume near
   the starting point, remains because the start-up "erred in entropy";
   such traces "usually cover two–three computational points" and do not
   matter at fine steps.
4. **Cold gas against a wall** (Appendix III, Figs. 6–7, pp. 305–306).
   $\gamma = 5/3$, zero pressure, unit specific volume; the wall condition
   is zero interface velocity in its Riemann problems. A right-moving
   shock forms (pressure to about 4, specific volume to about 0.25), with
   an entropy dip near the wall. The initial gas velocity is not printed.

# Notation map

| Paper | Registry | Note |
|---|---|---|
| $u$ (Ch. I, scalar model) | $u$ | conserved scalar |
| $u$ (Ch. II) | $v_x$ | **collision**: the registry $u$ is the conserved state; the paper's $u$ is velocity |
| $v$ | $1/\rho$ | **collision**: the paper's $v$ is specific volume, not velocity |
| $E$ | $e$ | **collision**: the paper's $E$ is specific internal energy; the registry $E$ is total energy density |
| $E + u^2/2$ | $E/\rho$ | specific total energy |
| $p$, $\gamma$ | $p$, $\gamma$ | |
| $c = \sqrt{\gamma p v}$ | $c_s$ | |
| $\tau$ | $\Delta t$ | **collision**: registry $\tau$ is the Valencia energy or an optical depth |
| $h$ | $h$ | spacing in the Lagrangian coordinate |
| $r = \tau/h$ | $\nu$ | Courant number for unit wave speed; the heat-equation $r = \tau/h^2$ is a diffusion number, in words |
| $\sqrt{AB}$, $\sqrt{A/B}$ | in words | acoustic speed and impedance of the linear Lagrangian system |
| $a_0$, $b_0$ (also $a_m$, $b_m$) | in words | left and right Lagrangian wave speeds (mass fluxes through the waves) |
| $P_m$, $U_m$ | in words | interface (star) pressure and velocity; **collision**: $P^*$ is the registry total pressure |
| cells $m + \tfrac12$, interfaces $m$ | $I_i$, $x_{i+1/2}$ | **index shift**: the paper's cells are half-integer, the opposite of the registry |
| $B$ | in words | constant in the Lagrangian equations, not defined in the text |
| $S$ | in words | specific entropy; **collision** risk with $s(u)$ and Valencia $S_i$ |
| $c_m$ | in words | scheme weights, local to the theorem |

# Pages created or updated

* Created this Source page.
* Created [Godunov's method](/methods/godunov-method.md).
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md)
  (batch-9 section: Godunov's original solver is exact and iterative).

# Citations

1. Godunov S.K. (1959), «Разностный метод численного расчета разрывных
   решений уравнений гидродинамики», Mat. Sb. 47(89), no. 3, 271–306.
   Local file:
   `/home/stefano/papers/mosaic/astrophysical-simulation-codes/1959-MatSb-Godunov-msb4873.pdf`.
   * **Version read.** The published journal pages: an OCR'd scan (ABBYY,
     2007) distributed by Math-Net.ru (id msb4873), 36 PDF pages = journal
     pp. 271–306. Received 20 March 1956 (p. 306). Not a preprint.
   * **Identity.** No DOI: none is printed and a Crossref bibliographic
     query returns no record of the paper. Year, volume and pages are from
     the scan's running header and pagination; `resource` is the
     Math-Net.ru page, the best stable identifier found.
   * **How it was read.** The OCR layer is garbled for all mathematics;
     every equation was read from rendered pages (110 dpi). English
     renderings are the reader's translations. The long index expressions
     of the stability proof (eqs. 12–13, pp. 301–302) were read for
     structure and conclusion only.
   * **Recorded as printed.** (a) p. 294 prints the energy equation with
     the time derivative of the squared specific total energy, unlike Ch. II
     eq. 1 (p. 283) (reader's reading: a printing error). (b) The constant
     $B$ of the Lagrangian equations is not defined in the text read.
   * **Reference list:** 4 printed entries (p. 306): von Neumann &
     Richtmyer (1950, printed "J. Neumann", merged into `vonneumann-1950`),
     Lax (1954), Landau & Lifshitz (1955, Russian edition) and Filippov
     (1955, Dokl. Akad. Nauk SSSR 100:1045). Bibliography: 2407 entries.

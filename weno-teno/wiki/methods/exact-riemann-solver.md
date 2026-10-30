---
type: Method
title: "Exact Riemann solver"
description: "The exact Riemann solver resolves a jump between two states into its waves by solving the nonlinear wave relations for the resolved pressure; the page gives van Leer's pressure equation, acoustic start, Godunov's chord and Bedijn's tangent iterations with the cavitation floor, the scalar Osher formula, and where later sources use or avoid it."
status: established
aliases: [exact Riemann solution, exact Riemann flux, Godunov flux (exact), iterative Riemann solver, pressure iteration, Godunov's iteration]
tags: [riemann-solver, numerical-flux, finite-volume, characteristic, multiphase]
timestamp: 2026-10-30T08:39:00Z
---

# Exact Riemann solver

The **Riemann problem** for $\partial_tu+\partial_xf(u)=0$ is the initial-value problem with data
$u^-$ for $x<0$ and $u^+$ for $x>0$; its solution is self-similar,
$u^{\mathrm{RP}}(x/t;u^-,u^+)$ (page-local). An **exact Riemann solver** computes this solution, or
at least its value at $x/t=0$, without linearizing or truncating the wave structure; the
[Godunov flux](/methods/godunov-scheme.md) is then $h^{\mathrm G}(u^-,u^+)=f\big(u^{\mathrm{RP}}(0;u^-,u^+)\big)$
([Harten et al. (1987a)](/sources/harten-1987.md), §4, Eqs. (4.4)–(4.5)). For a scalar law it is a
closed formula; for the Euler equations the wave relations are nonlinear and the solution is found
by iteration on the pressure between the waves. Approximate solvers
([Roe](/methods/roe-riemann-solver.md), the [HLL family](/methods/hll-riemann-solvers.md)) replace it,
and the sources weigh the replacement against cost and order.

## Scalar conservation laws

Harten et al. (1987a) (§4, Eq. (4.6a)), after Osher, evaluate the exact Riemann flux without
constructing the fan:

$$h^{\mathrm G}(u^-,u^+)=\begin{cases}\min_{u^-\le u\le u^+}f(u),&u^-\le u^+,\\ \max_{u^+\le u\le u^-}f(u),&u^->u^+,\end{cases}$$

with the convex case written through the sonic point (Eq. (4.6b)). The formula covers nonconvex
fluxes, where the fan contains compound waves; on the
[nonconvex scalar Riemann problems](/benchmarks/nonconvex-scalar-riemann-problem.md) their ENO
schemes with this flux develop the solution "at the correct rate" with the shocks at the right places,
whereas the Roe flux with a crude entropy correction lags by 8, 3 and 1 cells at $r=1$, 2, 4 (§7 A2,
Figs. 5–8). They also print a correction of the Roe flux for nonconvex $f$ (Eqs. (7.8c)–(7.8d)) with
which it "becomes computationally equivalent to the exact" flux.

## Euler equations: van Leer's pressure iteration

[Van Leer (1979)](/sources/vanleer-1979.md) resolves each interface discontinuity "as in Godunov's
method" and prints the procedure in a Lagrangean (mass-coordinate) setting (§2.3, Eqs. (57)–(63);
App. A, Eqs. (A1)–(A3), Figs. A1–A4). Page-local symbols: $p^*$, $v^*$ the resolved pressure and
velocity between the two waves, $\mathsf W^\mp>0$ the mass fluxes through the left and right waves
(the source's Lagrangean wave speeds $W_{i\mp}$), and $\rho^\pm c^\pm$ the Lagrangean sound speeds
(acoustic impedances) of the two initial states.

**Wave relations.** Across the left and right waves (Eq. (25))

$$\mathsf W^-(v^*-v^-)+(p^*-p^-)=0,\qquad \mathsf W^+(v^*-v^+)-(p^*-p^+)=0 \qquad\text{(57)–(58)},$$

and for an ideal gas the mass flux of each wave depends on $p^*$ and its own initial state: a shock
($p^*\ge p$) has

$$\mathsf W=\rho c\Big[1+\frac{\gamma+1}{2\gamma}\,\frac{p^*-p}{p}\Big]^{1/2}\qquad(31\gamma),$$

a centred rarefaction ($p^*<p$) the effective value

$$\mathsf W=\Big\lvert\frac{p^*-p}{v^*-v}\Big\rvert=\frac{\gamma-1}{2\gamma}\,\frac{1-p^*/p}{1-(p^*/p)^{(\gamma-1)/(2\gamma)}}\,\rho c\qquad(34\gamma).$$

**Pressure equation and start.** Eliminating $v^*$ from (57)–(58),

$$p^*=\frac{\mathsf W^+p^-+\mathsf W^-p^+-\mathsf W^-\mathsf W^+(v^+-v^-)}{\mathsf W^-+\mathsf W^+}\qquad(59),$$

an implicit equation since $\mathsf W^\pm$ depend on $p^*$; "in practice, $p^*$ is obtained through an
iterative procedure", started from the acoustic (linear-wave) estimate

$$p^{*(1)}=\frac{\rho^+c^+\,p^-+\rho^-c^-\,p^+-\rho^-c^-\rho^+c^+(v^+-v^-)}{\rho^-c^-+\rho^+c^+}\qquad(60),$$

and after convergence $v^*=\big[\mathsf W^-v^-+\mathsf W^+v^+-(p^+-p^-)\big]/(\mathsf W^-+\mathsf W^+)$
(Eq. (61)). The densities on the two sides of the contact then follow from the jump or adiabatic
relations, which completes the resolved state (§2.3).

**Chord against tangent iteration.** In the $(v,p)$ plane each initial state lies on a curve of
states reachable through a rarefaction (Poisson adiabat) or a shock (Hugoniot), and the resolved
state is their intersection (App. A, Fig. A1). Godunov's iteration intersects the chords of slopes
$\mp\mathsf W^\mp$ evaluated at the current $p^{*(n)}$, i.e. iterates Eq. (59), and gains a factor
$O(\lvert v^+-v^-\rvert,\lvert p^+-p^-\rvert)$ per cycle (Fig. A2). The tangent iteration "suggested by
P. J. Bedijn" intersects the tangents instead,

$$p^{*(n+1)}=p^{*(n)}-\frac{\mathsf Z^{-(n)}\mathsf Z^{+(n)}\big(v^{*(n)}_+-v^{*(n)}_-\big)}{\mathsf Z^{-(n)}+\mathsf Z^{+(n)}}\qquad(\mathrm{A1}),$$

with $v^{*(n)}_\mp$ the velocities on the two curves at $p^{*(n)}$ and $\mathsf Z^\mp$ (page-local) the
absolute tangent slopes,

$$\Big\lvert\frac{dp^*}{dv^*}\Big\rvert=\begin{cases}\dfrac{2\mathsf W^2}{\mathsf W^2+(\rho c)^2}\,\mathsf W,&p^*\ge p,\\ \rho c\,(p^*/p)^{1-(\gamma-1)/(2\gamma)},&p^*<p,\end{cases}\qquad(\mathrm{A2}\gamma)$$

and gains a factor $O\big((v^+-v^-)^2,(p^+-p^-)^2\big)$ per cycle "at a minor extra expense", the
slopes being a by-product of the wave-speed computation with no extra square root or
exponentiation; then $v^*=(\mathsf Z^-v^*_-+\mathsf Z^+v^*_+)/(\mathsf Z^-+\mathsf Z^+)$ (Eq. (A3); Fig. A3).
The two branches of (A2γ) follow from differentiating (25) with (31γ) and from the isentropic
relation (33γ) with $\rho c\propto p^{(\gamma+1)/(2\gamma)}$ *(compiler check, not in the sources)*.

**Cavitation.** An iterate, $p^{*(1)}$ in particular, can be negative when $v^+\gg v^-$; van Leer
clips it from below by "the smallest value $p_{\min}$ that is significant for the flow", and if
$p^{*(2)}$ is negative again "the exact solution would involve cavitation": $p^*$ is left at $p_{\min}$
and $v^*=v^{*(2)}$ (App. A, Fig. A4).

**How much exactness is needed.** In smooth flow the interface jumps of the second-order scheme are
$O(\Delta\zeta^2)$ ($\Delta\zeta$ the mass-coordinate cell size, page-local), so the acoustic estimate (60),
with error $O(\Delta\zeta^6)$, "is more than adequate" in the smooth part of the flow; inside a shock
structure the linear-wave approximation breaks down, and a bad estimate there enhances "numerical
oscillations in the post-shock region, an effect also known for Godunov's method". MUSCL therefore
iterates only where $p^{*(1)}$ differs by more than 1 % from the adjacent pressures, until successive
iterates differ by less than 1.5 %; in the Sod run the extra iterations took 2–3 % of the Lagrangean
step (§2.3, p. 110). Van Leer adds that using the exact wave-speed formulas inside the iterations
"even seems wasteful" and that one approximate formula not distinguishing shock from rarefaction
is "presently in study" (p. 110). The first time derivatives of the resolved state, which make the
scheme second order in time, come from the characteristic equations after the resolution
([generalized Riemann problem](/methods/generalized-riemann-problem.md), Eqs. (64)–(66)).

## Exact against approximate solvers

- **The Riemann solver as a pointer.** Harten et al. (1987a) argue that in their ENO schemes the
  Riemann flux only selects which one-sided Taylor expansion is valid at the interface, so the Roe
  flux replaces the exact one without loss of order (§4, pp. 252–253), and that "the importance of
  the Riemann solver decreases with increasing order" (§7 A2, p. 274; argued from figures). For the
  Euler equations they cite iterative algorithms for the exact flux and use the Roe flux in all runs
  (§6, §7 B). [Shu (2009a)](/sources/shu-2009.md) (§3.5.3) states that for systems "a monotone flux
  is replaced by an exact or approximate Riemann solver".
- **Cost.** [Bielawski et al. (2023)](/sources/bielawski-2023.md) (§3) choose an approximate solver,
  HLLC, because of "a significant reduction in computational cost compared to an exact Riemann
  solution with only a small increase in dissipation". [Cernetic et al. (2023)](/sources/cernetic-2023.md)
  (§2.2, §7.1) have an exact Riemann solver for an isothermal equation of state but emulate
  isothermality in their turbulence runs, resetting the temperature of an ideal gas each step, so
  that the "approximate, fast HLLC" solver replaces the "exact, but slower" one. For the liquid–vapour
  Riemann problem with phase change, [Long et al. (2023)](/sources/long-2023.md) state that the exact
  solver needs an eight-dimensional root finding and is "computationally expensive and not robust";
  their approximate solver runs a droplet with evaporation in 86.99 s against 318.17 s and a bubble
  with condensation in 106.93 s against 325.82 s (§4.2.1–§4.2.2;
  [phase-change Riemann solver](/methods/phase-change-riemann-solver.md)).
- **Availability.** [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) (§2.2, §4.1) offer exact,
  HLL and HLLC solvers in [MFC](/software/mfc.md), HLLC the default.
- **Source terms and equilibria.** [Yu, Liu & Feng (2023)](/sources/yu-2023.md) (§1) state, citing
  others, that the Godunov scheme built on the exact Riemann solution is well-balanced for
  conservation laws with singular sources, but that the complete Riemann solution of their Euler
  system with a singular source "is generally not available", and build an approximate solver
  instead. [Kurganov et al. (2023)](/sources/kurganov-2023.md) (§1) describe upwind well-balanced
  nozzle schemes as accurate but complicated because they need exact or sophisticated approximate
  Riemann solvers ([quasi-one-dimensional nozzle flow](/benchmarks/quasi-one-dimensional-nozzle-flow.md)).
- **Positivity.** [Ding & Wu (2024a)](/sources/ding-2024.md) (§1) recall that the one-dimensional
  positivity proofs of Cheng et al. for MHD hold under assumptions on exact Riemann solutions.

## Uses inside high-order schemes

- **Entropy-stable DG flux.** [Alberti et al. (2025)](/sources/alberti-2025.md) use a Godunov flux with
  the exact solver of Gottlieb & Groth (as they cite it) as their entropy-stable surface flux. On the
  [isentropic vortex](/benchmarks/isentropic-vortex.md) at $N=3,4$ it converges at order $N+1$, against
  $N$ for the Ismail–Roe [entropy-conservative flux](/methods/entropy-conservative-flux.md), and its
  entropy-conservation error converges at rate $2N+1$ (§3.1.1, Figs. 1–2).
- **Boundary states.** [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) impose slip walls through the
  exact Riemann solution of van der Vegt & van der Ven, which is not provably positivity preserving
  but "greatly improves robustness" near walls (§8).
- **Interfaces of multiphase flows.** [Bai & Li (2022)](/sources/bai-2022.md) obtain the normal
  velocity and pressure on cut faces from an exact two-phase Riemann solver, which sets the ghost
  states and the level-set velocity, while the cell-face fluxes use HLLC and HLL
  ([level-set method](/methods/level-set-method.md)).
- **Interface states of generalized Riemann problems.** The leading term of the Toro–Titarev
  solver is a classical Riemann problem solved "by any exact or approximate Riemann solver", as
  recalled by [Yajaman, Toro & Demattè (2025)](/sources/yajaman-2025.md) (§2.1, Eqs. (8)–(9);
  [generalized Riemann problem](/methods/generalized-riemann-problem.md)).
- **Reference solutions.** Exact Riemann solutions are the references of the shock-tube benchmarks:
  van Leer (1979, §4, Fig. 6) on Sod's tube, Harten et al. (1987a, §7 A2, Eq. (7.9)) on the nonconvex
  scalar problems, and among later sources [Fu (2021)](/sources/fu-2021.md) (§5.3),
  [Chamarthi (2023a)](/sources/chamarthi-2023.md) (Ex. 4.10, Leblanc) and
  [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) (Ex. 3.2)
  ([Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md),
  [Leblanc shock tube](/benchmarks/leblanc-shock-tube.md)).

## Qualifications

- Van Leer's relations are written in the Lagrangean mass coordinate with the Lagrangean wave speeds
  $\mathsf W$ (mass fluxes); the page keeps that form and does not translate it to Eulerian wave speeds.
- The convergence factors of the two iterations are stated, not proved or measured, in the source.
- Harten et al.'s claim that the Riemann solver matters less at higher order is argued from
  figures on scalar and Euler problems.
- The cost figures of Long et al. concern a phase-change solver, not the single-gas Euler solver of
  van Leer.

# Citations

- [Van Leer (1979)](/sources/vanleer-1979.md) — §2.1 (Eqs. (25), (31γ), (33γ), (34γ)), §2.3 (Eqs. (57)–(63), p. 110), §4 (Fig. 6), App. A (Eqs. (A1)–(A3), Figs. A1–A4).
- [Harten et al. (1987a)](/sources/harten-1987.md) — §4 (Eqs. (4.4)–(4.6), pp. 252–253), §6, §7 A2 (Eqs. (7.8)–(7.9), Figs. 5–8, p. 274), §7 B.
- [Shu (2009a)](/sources/shu-2009.md) — §3.5.3.
- [Bielawski et al. (2023)](/sources/bielawski-2023.md) — §3.
- [Cernetic et al. (2023)](/sources/cernetic-2023.md) — §2.2, §7.1.
- [Long et al. (2023)](/sources/long-2023.md) — §1, §3.2, §4.2.1–§4.2.2.
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §2.2, §4.1.
- [Yu, Liu & Feng (2023)](/sources/yu-2023.md) — §1.
- [Kurganov et al. (2023)](/sources/kurganov-2023.md) — §1.
- [Ding & Wu (2024a)](/sources/ding-2024.md) — §1.
- [Alberti et al. (2025)](/sources/alberti-2025.md) — §3.1.1, Figs. 1–2.
- [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) — §8.
- [Bai & Li (2022)](/sources/bai-2022.md) — solution algorithm (step 2), level-set velocity (Eqs. (21)–(22)).
- [Yajaman, Toro & Demattè (2025)](/sources/yajaman-2025.md) — §2.1, Eqs. (8)–(9).
- [Fu (2021)](/sources/fu-2021.md) — §5.3.
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — Ex. 4.10.
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — Ex. 3.2 (arXiv v1).

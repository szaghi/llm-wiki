---
type: Benchmark
title: "Buckley–Leverett problem"
description: "Scalar conservation law with the non-convex S-shaped flux used to model porous-media flow, run as Riemann or step data against fine reference solutions; the founding ENO and WENO papers use its step data to show convergence to the entropy solution, later sources to test subcell-limited DG, implicit CWENO, a multi-block WCNS and a bound-preserving PAMPA scheme."
status: established
aliases: [Buckley–Leverett equation, Buckley–Leverett test]
tags: [benchmark, limiting, cweno, dg]
timestamp: 2026-10-30T07:58:00Z
---

# Buckley–Leverett problem

The Buckley–Leverett equation $\partial_tu+\partial_xf(u)=0$ is used to
model porous-media flow (Pazner 2021, §5.3); the sources plot its
solution in $[0,1]$. Its flux

$$
f(u)=\frac{u^2}{u^2+M_{\mathrm{BL}}(1-u)^2},
$$

with a positive constant $M_{\mathrm{BL}}$ (page-local symbol), is
non-convex. Pazner and Puppo et al. describe it so, and Qin et al. call it a
benchmark "for two-phase Darcy flows"; the S shape follows from
$f(0)=0$, $f(1)=1$ and $f'(0)=f'(1)=0$, which force $f'$ to have an
interior maximum and $f''$ to change sign on $(0,1)$. The entropy
solution of a Riemann problem can then contain a shock attached to a
rarefaction in one compound wave, by the convex-hull construction
*(compiler check and remark, not in the sources)*. A scheme that
converges to a non-entropic or overshooting solution is exposed against
a fine reference solution.

## Setups

| Source | $M_{\mathrm{BL}}$ | Initial data | Domain | Grid | Final time |
|---|---|---|---|---|---|
| [Shu & Osher (1988)](/sources/shu-1988.md) §IV, Ex. 4, Eq. (4.5) | $1/4$ (printed as $4u^2/(4u^2+(1-u)^2)$) | $u_0=1$ on $[-\tfrac12,0]$, $0$ elsewhere | not printed (plots on $[-1,1]$) | $\Delta x=1/10,1/20,1/40$; 3-3-LF-ENO and 3-3-EO-ENO | not printed |
| [Liu et al. (1994)](/sources/liu-1994.md) Example 3(b) | $1/4$ | $u_0=1$ on $[-\tfrac12,0]$, $0$ elsewhere | $[-1,1]$, periodic | 80 cells ($\Delta x=0.025$), $\Delta t/\Delta x=0.4$, WENO $r=3$; reference Lax–Friedrichs on a very fine grid | 0.4 |
| [Jiang & Shu (1996)](/sources/jiang-1996.md) §8.1 Ex. 2, Eq. (8.1) | $1/4$ | $u_0=1$ on $[-\tfrac12,0]$, $0$ elsewhere | not printed in the text (plots on $[-1,1]$) | 81 points, CFL 0.8 (figure headers); WENO-RF-3 with RK-3, WENO-RF-5 with RK-4 | 0.4 (figure headers) |
| [Pazner (2021)](/sources/pazner-2021.md) §5.3, Eq. (75) | $1/4$ (printed as $4u^2/(4u^2+(1-u)^2)$) | Riemann data, printed $u_0=-3$ for $x<0$, $3$ for $x\ge0$ | not stated (plots on $[-1,1]$) | 256 DOFs, $N=0,1,3,7$; reference $N=0$ on 10,000 elements | 0.25 |
| [Puppo, Semplice & Visconti (2023)](/sources/puppo-2023.md) §4.4, Eqs. (38)–(39) | $1/3$ | $u_0=0.5$ on $-0.25\le x\le0.25$, $0$ otherwise | "periodic domain $\Omega=[0,1]$" | 100 cells, $\Delta t=1.1h$ and $4.4h$ | 0.085 |
| [Abgrall et al. (2026)](/sources/abgrall-2026.md) Ex. 3 | $1/4$ (printed as $4u^2/(4u^2+(1-u)^2)$) | $u_0=1$ on $[-\tfrac12,0]$, $0$ otherwise | $[-1,1]$, periodic | 200 cells, SSP-RK3, CFL 0.2 | 0.4 |
| [Qin et al. (2023)](/sources/qin-2023.md) §3.3, Eqs. (30)–(31) | $1/4$ (printed as $4u^2/(4u^2+(1-u)^2)$) | $u_0=1$ on $[-0.5,1]$, $0$ elsewhere | $[-1,1]$, two blocks with interface at $x=0.5$ | 160 points on $[-1,0.5]$, 80 on $[0.5,1]$; reference: 4000 points, single block | 0.31, 0.4 |

Puppo et al. take the setup from Arbogast et al. ("the same setup as
in [3]"); $h$ is their cell width. With $M_{\mathrm{BL}}=1/3$ the largest
characteristic speed is $\max f'\approx2.21$ (at $u\approx0.33$), so the
two time steps correspond to Courant numbers of about 2.4 and 9.7
*(compiler check, not in the sources)*.

## Findings

**The founding runs.** [Shu & Osher (1988)](/sources/shu-1988.md) call
it "the well known Buckley-Leverett example" and describe its exact
solution as "a shock-rarefaction-contact discontinuity mixture"; their
finite-difference [ENO](/methods/eno-reconstruction.md) schemes "resolve
the correct solution well", but with the
[Lax–Friedrichs](/methods/lax-friedrichs-flux.md) building block the
third-order scheme smears more than with the Engquist–Osher one
(Figs. 33–38). Liu et al.'s WENO converges "with good resolution" to the
entropy solution against the fine Lax–Friedrichs reference (Fig. 8).
Jiang & Shu print the same description of the exact solution and find
their fifth-order [WENO](/methods/weno-js-reconstruction.md) and its
third-order counterpart converging to the entropy solution with sharp
shock profiles. Since near discontinuities WENO behaves like its base
ENO scheme, they expect the shock to be only as sharp as with that base
scheme, yet the third-order WENO is "comparable to the 3rd order ENO
scheme instead of the base 2nd ENO scheme", and the fifth-order one to
fourth-order ENO (§8.1 Ex. 2, Fig. 3). The quartic-flux Riemann problems
that the same papers run are on
[Riemann problems with nonconvex scalar fluxes](/benchmarks/nonconvex-scalar-riemann-problem.md).

**Explicit DG with subcell convex limiting.** Pazner's sparse
invariant-domain-preserving DG with subcell
[convex limiting](/methods/convex-limiting.md) at fixed 256 degrees of
freedom "compare[s] well" with the fine first-order reference for every
degree $N=0,1,3,7$ (Fig. 9).

**Implicit CWENO at large time steps.** Puppo et al. compare implicit
Euler, the unlimited third-order DIRK–CWENO scheme D3P1 and the
time-limited [Quinpi](/methods/quinpi.md) scheme Q3P1, with the
time-limiter regularization set to $\Delta t^3$ for this test. At the
smaller time step the schemes are similar; at $\Delta t=4.4h$ Q3P1 avoids
the overshoots of D3P1 (Fig. 10).

**A multi-block finite-difference WCNS.** Qin et al. call the solution "a
shock-rarefaction-contact discontinuity mixture", the words of Shu &
Osher (1988) and Jiang & Shu (1996), and recall that "some
high-order method may converge to fake solution" on it (§3.3). They run it on
two blocks with a jump in grid spacing, to test their
[shock-capturing boundary closures](/methods/shock-capturing-boundary-closure.md)
for a fifth-order multi-resolution
[WCNS](/methods/weighted-compact-nonlinear-scheme.md) at the block interface.
*(Compiler check, not in the sources: 160 points on $[-1,0.5]$ and 80 on
$[0.5,1]$ give spacings $1.5/160$ and $0.5/80$, a ratio of 1.5, the left
block coarser.)* The solution converges to the single-block reference on 4000 points. At
$t=0.31$, just after the shock has crossed the interface, the transition is
smooth, and the discontinuities are "well captured" at $t=0.4$ (Fig. 5). The
scalar runs use Lax–Friedrichs flux splitting and SSP-RK3 (Eq. (23)) at
CFL 0.4.

**A bound-preserving point–average scheme.** Abgrall et al. (2026) run
the problem with their bound-preserving
[PAMPA scheme](/methods/pampa-scheme.md), which evolves cell averages
and point values and blends high- and low-order fluxes and
residuals so that both stay within the global bounds $[0,1]$ (strict
or slightly relaxed); the result agrees with that of Zhang & Shu, as
they cite it (Fig. 3). Their step data, like Qin et al.'s, lie in
$[0,1]$, with the flux of Pazner and Qin et al.; data, domain and final
time are those of Liu et al. (1994).

## Qualifications

- Pazner's printed Riemann data, $\mp3$, lie outside the range $[0,1]$
  shown on the vertical axis of Pazner's Fig. 9; the data run cannot be
  recovered from the paper.
- Puppo et al.'s step occupies $[-0.25,0.25]$, outside their stated
  domain $[0,1]$; on a periodic $[0,1]$ it is the step on
  $[0,0.25]\cup[0.75,1]$, and their Fig. 10 is plotted on $[0,1]$.
- Qin et al. use the same flux as Pazner ($M_{\mathrm{BL}}=1/4$) but data
  in $[0,1]$, so their run, unlike Pazner's, can be read from the paper.
- Evidence in all seven papers is visual. Abgrall et al.'s Fig. 3
  caption writes "restrict GMP" for the strict global maximum
  principle.

# Citations

- [Shu & Osher (1988)](/sources/shu-1988.md) — §IV, Ex. 4, Eq. (4.5), Figs. 33–38 (ICASE Report 87-33).
- [Liu et al. (1994)](/sources/liu-1994.md) — §4, Example 3(b), Fig. 8.
- [Jiang & Shu (1996)](/sources/jiang-1996.md) — §8.1, Ex. 2, Eq. (8.1), Fig. 3 (author preprint).
- [Pazner (2021)](/sources/pazner-2021.md) — §5.3, Eq. (75), Fig. 9 (arXiv v1).
- [Puppo, Semplice & Visconti (2023)](/sources/puppo-2023.md) — §4.4, Eqs. (38)–(39), Fig. 10 (arXiv v2).
- [Qin et al. (2023)](/sources/qin-2023.md) — §3.3, Eqs. (30)–(31), Fig. 5: two-block WCNS run.
- [Abgrall et al. (2026)](/sources/abgrall-2026.md) — §3, §4, Ex. 3, Fig. 3.

---
type: Benchmark
title: "Quasi-one-dimensional nozzle flow"
description: "Euler flow through a duct of variable cross-section with a standing shock, marched or solved to steady state: the page gives the forms of the equations, the nozzle shapes and boundary data of Harten, Jiang & Shu, Huang & Zahr and the Chou–Shu run, the isentropic discontinuous-nozzle relatives, and what the runs show about steady convergence and downstream order."
status: established
aliases: [quasi-1D nozzle, quasi-1-D nozzle flow, nozzle flow problem, steady nozzle flow, quasi-one-dimensional Euler equations, converging-diverging nozzle, divergent nozzle]
tags: [benchmark, finite-volume, finite-difference, weno, well-balanced, shock-tracking]
timestamp: 2026-10-30T08:38:00Z
---

# Quasi-one-dimensional nozzle flow

In the **quasi-one-dimensional nozzle problem** the gas moves along a duct whose cross-section
$\Sigma(x)$ varies slowly (page-local symbol, the sources' $A$ or $a$; the registry's $A$ is the flux
Jacobian), and the flow is described by cross-section-averaged states that obey the one-dimensional
Euler equations with a geometric source. The steady solution is known exactly: for given inflow and
outflow conditions the area–Mach relation fixes the flow on each side, and a standing shock sits at
the position where the back pressure is matched. The sources run it to test steady-state
convergence of a shock-capturing scheme, the order of accuracy upstream and downstream of a shock,
and, with a discontinuous cross-section, the preservation of equilibria. The problem is also
listed among the [steady shock problems](/benchmarks/steady-shock-problems.md), which compare it
with the planar steady shocks; this page gives the full treatment.

## Equations

The sources write the model in three forms.

- **Conservation form in area-weighted variables.** [Huang & Zahr (2022)](/sources/huang-2022.md)
  (§6.3, Eqs. (83)–(86)) solve the steady equations
  $$\begin{aligned}
  \partial_x(\Sigma\rho v)&=0,\\
  \partial_x\big(\Sigma(\rho v^2+p)\big)&=p\,\frac{d\Sigma}{dx},\\
  \partial_x\big(\Sigma(E+p)v\big)&=0,
  \end{aligned}$$
  with the ideal-gas law, and call them "a conservation law of the form (1)" in the variables
  $\Sigma(\rho,\rho v,E)$ (their Eq. (86); $E$ is written here per unit volume, the source writes
  $\rho E$ with $E$ specific). $\gamma$ is not printed.
- **Euler variables with a source proportional to $\Sigma'/\Sigma$.**
  [Jiang & Shu (1996)](/sources/jiang-1996.md) (§8.2, Ex. 4) add to the 1D Euler equations
  $\partial_tu+\partial_xf(u)=S(u,x)$ the forcing term
  $$S(u,x)=-\frac{\Sigma'(x)}{\Sigma(x)}\big(\rho v,\ \rho v^2,\ v(E+p)\big)^\top .$$
  Dividing the three equations of Huang & Zahr by $\Sigma$ gives exactly the steady form of this
  source: $\partial_x(\rho v^2+p)=-(\Sigma'/\Sigma)\rho v^2$, the pressure terms
  $p\Sigma'$ cancelling *(compiler check, not in the sources)*.
- **Cross-section averages with a momentum source.** [Harten (1983a)](/sources/harten-1983.md)
  (§8 (II), Eq. (8.7a)) considers "an axisymmetric nozzle", writes "the cross-section average of the
  flow" as $\partial_tw+\partial_xf(w)=-s(w,x)$ with $s=\big(0,\ p\,\tfrac{d\Sigma}{dx},\ 0\big)^\top$,
  "where $w$, $f(w)$ and $p$ are given in (7.1)", the Euler variables of the report, and does not
  relate $w$ to $\Sigma$ further.

Neither source relates its form to another source's. A fourth, **isentropic** model with a possibly
discontinuous cross-section is the system of [Kurganov et al. (2023)](/sources/kurganov-2023.md) (§5,
Eqs. (5.1)–(5.5)): unknowns $(\Sigma\rho,\Sigma\rho v,\Sigma)$, $p=\kappa_{\mathrm p}\rho^\gamma$
(page-local constant), no energy equation, and the non-conservative product $p\,\partial_x\Sigma$ in
the momentum equation; its steady states have constant discharge $q_{\mathrm n}=\Sigma\rho v$ and
constant Bernoulli energy $\tfrac12v^2+\frac{\kappa_{\mathrm p}\gamma}{\gamma-1}\rho^{\gamma-1}$, and a
jump of $\Sigma$ makes them discontinuous ([flux globalization](/methods/flux-globalization.md),
[well-balancing](/properties/well-balancing.md)).

## Configurations

| Source | Cross-section $\Sigma(x)$ | Flow and boundary data | Grid and scheme |
|---|---|---|---|
| Harten (1983a) §8 (II), Eq. (8.7b), Figs. 4–5 | divergent, $1.398+0.347\tanh(0.8x-4)$ | supersonic at the entrance, subsonic at the exit | "crude mesh" with Roe's first-order scheme (Fig. 4a) and ULT1 (Fig. 4b); ULT1 on a finer mesh (Fig. 5) |
| Harten (1983a) §8 (II), Eq. (8.7c), Fig. 6 | convergent–divergent, $1+(\Sigma_0-1)(1-x/5)^2$ for $x\le5$, $1+(\Sigma_E-1)\big[(x-5)/(x_E-5)\big]^2$ for $x>5$ | subsonic at entrance and exit | ULT1 |
| Jiang & Shu (1996) §8.2 Ex. 4, Fig. 8 | unit length, shape fixed by "a linear, isentropic Mach number distribution, which is 0.8 at $x=0$ (the entrance) and 1.8 at $x=1$ (the exit)" | exit condition set by the prescribed shock position $x=0.5$ | 34 points, WENO-Roe-4 and WENO-Roe-5, third-order TVD Runge–Kutta |
| Huang & Zahr (2022) §6.3, Eq. (85) | $\mu_1+(\mu_2-\mu_1)(10-x)x/25$ on $(0,10)$, $\mu_1=3$ at inlet and exit, throat $\mu_2=1$ at $x=5$ | $\rho(0)=1$, $\rho(10)=0.7$, "which will lead to a shock at $x_s=7.94$" | 12 elements, $N=1$–$5$, [implicit shock tracking](/methods/implicit-shock-tracking.md) (HOIST) against artificial viscosity |
| Chou & Shu, as reproduced by [Shu (2009a)](/sources/shu-2009.md) §3.5.2, Fig. 3.1, Table 3.1 | not printed in the review | not printed | fourth-order residual-distribution WENO on nonsmooth meshes, $N=21$–$641$ cells (Fig. 3.1: 81 cells) |

Harten's figures are credited to H. C. Yee; the report prints neither $\Sigma_0$, $\Sigma_E$, $x_E$ nor the
meshes, shows the exact steady solutions as solid curves, and hopes that "a detailed report of these
calculations and the particular approach to steady state will be published elsewhere" (pp. 46–47);
all its runs use the Roe linearization (§8). ULT1 is
[Harten's TVD scheme](/methods/harten-tvd-scheme.md) with the numerical-viscosity function
$\mathfrak Q(x)=\lvert x\rvert$ (Eq. (8.3a); page-local, the source writes $Q$). Huang & Zahr's flux is "a smoothed variant of Roe's flux" with the
Harten–Hyman entropy fix ([Roe solver](/methods/roe-riemann-solver.md)). $\gamma$ is printed by none
of Harten (1983a), Jiang & Shu (1996) and Huang & Zahr (2022) for this problem.

Harten's divergent nozzle and the smooth nozzles of Kurganov et al. (2023) (§7, Ex. 3, Eq. (7.3):
$\Sigma=0.976\pm0.748\tanh(0.8x-4)$ on $[0,10]$, isentropic, $\gamma=1.4$, inflow discharge $8$) share
the profile $\tanh(0.8x-4)$ with different constants; neither paper cites the other for it.

## Findings

**Steady convergence of WENO.** Jiang & Shu (1996) report that WENO-Roe-4 and WENO-Roe-5 "converge
nicely to the exact solution" on 34 points and that the residue "settles down to $10^{-7}$ for this
grid, and to a smaller number for a finer grid"; they conclude that "WENO has its advantage for
steady state calculations" and attribute it (§1) to the WENO flux being smoother than the ENO flux,
which also enables their convergence proof for smooth solutions. Residual histories are not shown.

**Second-order TVD against first order.** Harten (1983a) shows the steady standing shock of the
divergent nozzle with Roe's first-order scheme and with ULT1 on the same crude mesh, and ULT1 on a
finer one (Figs. 4–5); the report compares them only through the figures.

**Order downstream of the shock.** The run of Chou & Shu that Shu (2009a, §3.5.2, Table 3.1)
reproduces measures the density error outside three cells around the shock. Upstream, the $L^1$
orders rise from 3.23 to 4.60 on refinement from 41 to 641 cells. Downstream they depend on the
treatment of the shock cell: with "subcell separate integrations" in the cell containing the shock
the $L^1$ orders are 3.90, 4.93, 4.43, 4.40, 4.38, with regular integration 1.99, 1.98, 2.25, 2.01,
2.83, the $L^1$ error on 641 cells being $1.75\times10^{-12}$ against $8.15\times10^{-9}$. Shu explains
the loss by characteristics of other fields crossing the shock and carrying its error downstream,
which a subcell resolution technique in shock cells prevents, and adds that even when the
downstream order degenerates, "the magnitude of the errors is typically still much smaller than
that of a lower order scheme on the same mesh".

**Tracking against capturing.** Huang & Zahr (2022, §6.3) find their tracking solution at $N=2$ on
12 elements "indistinguishable from the exact solution", whereas the
[artificial-viscosity](/methods/artificial-viscosity.md) shock-capturing method they compare with
needs 50 elements at $N=4$ for a similar solution, with a steep gradient in place of the jump
(Fig. 24); the optimizer converges in about 20 iterations (Fig. 25). With the $L^1$ density error
$E_\rho$ and the shock-position error $E_{x_s}$ (Eq. (87)), the observed rates are about $N+1$ for
$N=1$–$5$ and artificial viscosity at $N=2$ converges "sub-first-order", which the authors attribute
to the smoothed discontinuity and to "downstream corruption" (Fig. 26, Table 3). Their Table 3, on
the finest pairs of meshes:

| $N$ | elements | $E_\rho$ | rate | $E_{x_s}$ | rate |
|---|---|---|---|---|---|
| 1 | 448 → 896 | $4.18\times10^{-5}$ → $1.04\times10^{-5}$ | 2.00 | $3.74\times10^{-5}$ → $9.31\times10^{-6}$ | 2.00 |
| 2 | 192 → 384 | $2.97\times10^{-7}$ → $6.19\times10^{-8}$ | 2.26 | $1.84\times10^{-7}$ → $2.42\times10^{-8}$ | 2.92 |
| 3 | 96 → 192 | $2.11\times10^{-8}$ → $1.29\times10^{-9}$ | 4.03 | $1.00\times10^{-8}$ → $6.72\times10^{-10}$ | 3.90 |
| 4 | 96 → 192 | $2.67\times10^{-10}$ → $8.28\times10^{-12}$ | 5.01 | $5.50\times10^{-11}$ → $2.44\times10^{-12}$ | 4.50 |
| 5 | 40 → 80 | $3.29\times10^{-10}$ → $4.82\times10^{-12}$ | 6.09 | $4.50\times10^{-11}$ → $6.22\times10^{-14}$ | 9.50 |

The caption states that the segment-wise slopes tend "to at least the optimal rate ($p+1$)"; the
$N=2$ density slopes 3.00, 2.84, 2.26 and the final $N=4$ shock-position slope 4.50 stay below it.

**Discontinuous cross-sections.** For the isentropic model, Kurganov et al. (2023, §7) keep a steady
state across a jump of $\Sigma$ from 1.5 to 2.5 with errors $0$ in $q_{\mathrm n}$ and
$8.88\times10^{-16}$ in the Bernoulli energy (Table 7.1), reach a discontinuous steady state from
Riemann data with discharge $-13.583$ against the exact $\approx-13.446$ of Cuong & Thanh as they cite
it, run six nozzle Riemann problems of Kröner & Thanh, and on a piecewise-constant
convergent–divergent nozzle ($\Sigma=2$, 1, 2 on $[0,7.5]$, $[7.5,12.5]$, $[12.5,20]$) find that their
§3 scheme produces spikes near $x=7.5$ and $12.5$ and converges to a state with non-constant energy
(Ex. 4). They describe the upwind well-balanced nozzle methods they compare against as accurate but
complicated, needing exact or sophisticated approximate Riemann solvers (§1;
[exact Riemann solver](/methods/exact-riemann-solver.md)).
[Yu, Liu & Feng (2023)](/sources/yu-2023.md) (§1, §4) list nozzles with discontinuous cross-section
among the motivations of Euler equations with singular sources and transpose the Kröner–Thanh
nozzle flux to that setting, where it is well-balanced (Theorem 4.1) but can become unavailable
(Theorem 4.2).

## Qualifications

- None of the capturing runs on this page prints the residual history or the steady-state
  iteration; Jiang & Shu's $10^{-7}$ is stated in the text, Harten's comparison is graphical.
- The Chou–Shu data are reproduced in a review; the nozzle geometry, $\gamma$ and boundary data of
  that run are not in the ingested source. Shu (2009a) prints identical before-shock errors in the
  two halves of Table 3.1 with orders that differ in the last digit (e.g. 3.23 and 3.24 at 41 cells).
- Huang & Zahr's equations (83) are steady only; their HOIST method solves them as an optimization
  problem, not by time marching. Their mesh-size column equals $10/\lvert\mathcal E_h\rvert$, the
  domain length over the number of elements, in every row *(compiler check, not in the sources:
  e.g. $10/112=8.93\times10^{-2}$)*; the $N=5$ rows start at 10 elements.
- The isentropic nozzle of Kurganov et al. has no energy equation and no standing shock of the
  Euler type; it belongs to this family through the geometry and the source $p\,\partial_x\Sigma$.

# Citations

- [Harten (1983a)](/sources/harten-1983.md) — §8 (Eqs. (8.3a), (8.5)), §8 (II) (Eqs. (8.7a)–(8.7c), Figs. 4–6, pp. 46–47) (NYU report DOE/ER/03077-175, March 1982).
- [Jiang & Shu (1996)](/sources/jiang-1996.md) — §1, §8.2 Ex. 4, Fig. 8 (author preprint).
- [Huang & Zahr (2022)](/sources/huang-2022.md) — §6.3, Eqs. (83)–(87), Figs. 24–26, Table 3 (arXiv v2).
- [Shu (2009a)](/sources/shu-2009.md) — §3.5.2, Fig. 3.1, Table 3.1 (reproduced from Chou & Shu).
- [Kurganov et al. (2023)](/sources/kurganov-2023.md) — §1, §5 (Eqs. (5.1)–(5.5)), §7 Exs. 1–4, Eq. (7.3), Table 7.1.
- [Yu, Liu & Feng (2023)](/sources/yu-2023.md) — §1, §4 (Theorems 4.1–4.2).

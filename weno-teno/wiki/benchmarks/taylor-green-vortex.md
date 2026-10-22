---
type: Benchmark
title: "Taylor–Green vortex"
description: "Three-dimensional periodic vortex flow that transitions to turbulence, run inviscid at low Mach number to compare the kinetic-energy loss and enstrophy growth of shock-capturing schemes, and viscous at Re=1600 to compare their dissipation rate with DNS; the bundle's smooth-turbulence resolution test for TENO-type schemes."
status: established
aliases: [TGV, inviscid Taylor–Green vortex, Taylor–Green vortex at Re 1600]
tags: [benchmark, turbulence, low-dissipation, teno, weno]
timestamp: 2026-10-21T12:00:00Z
---

# Taylor–Green vortex

The Taylor–Green vortex is a smooth, triply periodic initial velocity
field on $[0,2\pi]^3$ that stretches its vorticity, breaks down into
small scales and, if the flow is viscous, decays as turbulence. The sources use it as
the smooth-turbulence test of shock-capturing schemes: there is no
shock, and in the inviscid low-Mach runs the loss of
kinetic energy is read as [numerical dissipation](/definitions/numerical-dissipation.md), and the
volume-averaged kinetic energy $\langle\kappa\rangle$ and enstrophy (the
volume average of half the squared vorticity, in words) are the
measures.

## Setups

**Inviscid, low Mach number.** [Li et al. (2022)](/sources/li-2022-b.md)
§4.5, Eqs. (47)–(49) and [Takagi et al. (2022)](/sources/takagi-2022.md)
§4.10 print

$$
\begin{aligned}
\rho&=1,\qquad v_1=\sin x\cos y\cos z,\qquad v_2=-\cos x\sin y\cos z,\qquad v_3=0,\\
p&=100+\tfrac1{16}\big[(\cos2x+\cos2y)(2+\cos2z)-2\big],
\end{aligned}
$$

on periodic $[0,2\pi]^3$. The background pressure $100$ makes the
maximum Mach number about $0.08$ for $\gamma=5/3$
($c=\sqrt{\gamma p/\rho}\approx12.9$ with $\lvert v\rvert\le1$;
*compiler check, not in the sources*), so the flow is nearly
incompressible. Li et al. use $\gamma=5/3$ and grids $64^3$, $128^3$ up
to $t=6$; Takagi et al. do not print $\gamma$ and use $64^3$ to $t=10$.
Li et al. write the pressure as $100+([\cos(2z)+2][\cos(2x)+\cos(2y)]-2)/16$,
the same expression.

**Viscous, $\mathrm{Re}=1600$.** [Ye et al. (2022)](/sources/ye-2022.md)
§4.9, Eqs. (49)–(52): a cube of side $2\pi L$, reference Mach number
$M=0.1$,

$$
v_1=M\sin\tfrac xL\cos\tfrac yL\cos\tfrac zL,\quad
v_2=-M\cos\tfrac xL\sin\tfrac yL\cos\tfrac zL,\quad v_3=0,\quad
p=\frac1\gamma+\frac{M^2}{16}\Big(\cos\tfrac{2x}L+\cos\tfrac{2y}L\Big)\Big(\cos\tfrac{2z}L+2\Big),
$$

$\mathrm{Re}=1600$, $\mathrm{Pr}=0.71$, $\gamma=1.4$, $256^3$ points,
$t\in[0,20]$; diagnostics are the kinetic energy, the dissipation rate
split into solenoidal and dilatational parts, and $Q$-criterion
iso-surfaces ($Q=2.5$ at $t=10$).

**Reviewed results.** [Fu (2023)](/sources/fu-2023.md) reproduces an
inviscid TGV at $t=10$ (iso-surface $Q=3$, resolution not printed;
WENO-CU6, TENO6, TENO8, TENO8-opt, Fig. 4) and an incompressible viscous
TGV dissipation rate on $64^3$ against DNS on $256^3$ (TENO8-A against
the ALDM and dynamic Smagorinsky models, Fig. 14).

## Findings across sources

**Kinetic-energy loss ranks the schemes; WENO-JS loses most.** Li et
al. find that WENO-JS dissipates the most kinetic energy of the WENO
variants, that at $128^3$ it still dissipates more than the
seventh-order linear upwind scheme at $64^3$, yet its enstrophy grows
faster than that upwind run; [WENO-ZN](/methods/weno-zn.md) has the
least dissipation of the three WENO schemes (Fig. 11). Takagi et al.
find that [TENO-THINC](/methods/teno-thinc.md) preserves kinetic energy
better and gives larger enstrophy growth than WENO5-Z and TENO5 on
$64^3$ (Fig. 21). Fu (2023) shows TENO6 and TENO8 less dissipative than
WENO-CU6.

**TENO beats WENO on the viscous dissipation rate.** Ye et al. find
the kinetic energy nearly scheme-independent at $256^3$, but the
dissipation rate discriminates: all TENO-type schemes beat the
WENO-type ones, the WENO-type schemes underestimate the peak (more so
with a dissipative flux), [AFTENO5](/methods/afteno.md) with HLLC is
best, and HLLC beats Steger–Warming splitting in both alternative-flux
schemes (Figs. 10–12). Fu (2023) reports that
[TENO8-A](/methods/adaptive-teno.md) on $64^3$ beats the dynamic
Smagorinsky model and ALDM for the dissipation rate (§4.2).

The sources agree that WENO-JS-type weights are the most dissipative
of the schemes compared, and no source reports a newer scheme
dissipating more than its WENO-JS baseline.

## Qualifications

- Takagi et al. head §4.10 "incompressible" Taylor–Green vortex, but
  solve the compressible Euler equations with the background pressure
  $100$; the flow is low-Mach, not incompressible.
- Li et al.'s Fig. 10 caption says the contours are "given by velocity
  from 0 to 1", while the panels are labelled with vorticity-magnitude
  levels $\Omega=1.5$ and $3.0$.
- In the inviscid runs there is no converged reference: the sources
  compare schemes with each other (Li et al. also with a linear upwind
  scheme), not with an exact energy history.

# Citations

- [Li et al. (2022)](/sources/li-2022-b.md) — §4.5, Eqs. (47)–(49), Figs. 10–11.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.10, Fig. 21.
- [Ye et al. (2022)](/sources/ye-2022.md) — §4.9, Eqs. (49)–(52), Figs. 10–12.
- [Fu (2023)](/sources/fu-2023.md) — Figs. 4 and 14; §4.2 (reproduced).

---
type: Benchmark
title: "Linear acoustics tests"
description: "Smooth and stationary solutions of the two-dimensional linear acoustic equations (standing sine wave, non-irrotational wave, high-frequency radial pulse, stationary vortex) verifying order, adaptive-mesh behaviour and stationarity preservation of Active Flux methods, with small-amplitude sound and MHD eigenmode convergence tests of nonlinear solvers as relatives."
status: established
aliases: [acoustics sine wave, Lukáčová acoustics test, acoustic convergence test, linear acoustics sine wave, stationary acoustic vortex]
tags: [benchmark, active-flux, finite-volume, well-balanced]
timestamp: 2026-10-24T05:33:00Z
---

# Linear acoustics tests

The linear acoustic equations in symmetric scaling,

$$
\partial_tp+c\,\nabla\cdot v=0,\qquad \partial_tv+c\,\nabla p=0,
$$

with acoustic pressure $p$, velocity $v=(v_1,v_2)$ and constant sound speed $c$, are the
simplest hyperbolic system with genuinely multi-dimensional wave propagation. They have exact
evolution operators, which is why [Active Flux](/methods/active-flux.md) methods are first built
and tested on them, and they have a large set of stationary states: every field with
$\nabla p=0$ and $\nabla\cdot v=0$ *(compiler check, not in the sources)*. The sources use
them for three things: a convergence test on a smooth periodic wave whose exact solution is
known in closed form, a test of adaptive meshes on a high-frequency pulse, and a test of
[stationarity preservation](/properties/well-balancing.md) on a stationary vortex.

## Periodic standing sine wave

**Data.** [Calhoun, Chudzik & Helzel (2023)](/sources/calhoun-2023.md) §4.5.1, Eq. (31), take
the test from Lukáčová-Medvid'ová et al.: on the periodic $[-1,1]^2$ with $c=1$,

$$
\begin{aligned}
p(x,y,t)&=-\tfrac1c\cos(2\pi ct)\,\big(\sin2\pi x+\sin2\pi y\big),\\
v(x,y,t)&=\tfrac1c\sin(2\pi ct)\,\big(\cos2\pi x,\ \cos2\pi y\big),
\end{aligned}
$$

so $p_0=-\tfrac1c(\sin2\pi x+\sin2\pi y)$ and $v_0=0$. The two plane standing waves along $x$
and $y$ are exact solutions: $\partial_tp=2\pi\sin(2\pi ct)(\sin2\pi x+\sin2\pi y)=-c\nabla\cdot v$
and $\partial_tv=2\pi\cos(2\pi ct)(\cos2\pi x,\cos2\pi y)=-c\nabla p$ *(compiler check, not in
the sources)*. The solution has period $1/c$ in time.

[Barsukow et al. (2026)](/sources/barsukow-2026.md) §5.2 (arXiv v2) take the same wave on the
same domain from Eymann & Roe, after Lukáčová-Medvid'ová et al., with the opposite sign of the
pressure: $p_0=\tfrac1c(\sin2\pi x+\sin2\pi y)$, $v_0=0$, and print the exact solution
$p=\tfrac1c\cos(2\pi ct)(\sin2\pi x+\sin2\pi y)$,
$v=\tfrac1c\sin(2\pi ct)(\cos2\pi x,\cos2\pi y)$. With that sign of $p$ the velocity must carry
the opposite sign, $v=-\tfrac1c\sin(2\pi ct)(\cos2\pi x,\cos2\pi y)$: as printed,
$\partial_tp+c\nabla\cdot v=-4\pi\sin(2\pi ct)(\sin2\pi x+\sin2\pi y)\neq0$ *(compiler check, not
in the sources)*. Calhoun et al.'s printed pair is consistent. The slip does not touch Barsukow
et al.'s comparison, which is made at $t=5$, a whole number of periods, where $v=0$ and $p=p_0$.

| Source | Final time | Grid | Time step | Measured |
|---|---|---|---|---|
| Calhoun et al. (2023) §4.5.1 | $t=1$ | $16\times16$ patches, uniform levels 2 and 3, AMR levels 2–3 and 3–4 with refinement forced along the diagonal | CFL $\le0.4$ | $L^1$ errors and EOC of $p$ and $v$ (Table 4) |
| Barsukow et al. (2026) §5.2 | $t=5$ | $60\times60$ | $\Delta t=\mathrm{cfl}\,\min(\Delta x,\Delta y)/c$, cfl their maximal $C_{\mathrm{cfl}}$ (0.085 at order 7) | cross-section of $p$ at $y=0.25$, orders 3–7 (Figs. 12–13) |

**Third order on adaptive grids.** Calhoun et al. run the third-order Cartesian Active Flux
method in [ForestClaw](/software/forestclaw.md), with the Eymann–Roe acoustic evolution
operator for the point values and coarse–fine transfer of averages and point values (see
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)). Their $L^1$ errors
(Table 4):

| Grid pair | $p$ errors | EOC | $v$ errors | EOC |
|---|---|---|---|---|
| uniform 2 → 3 | $2.23\times10^{-4}$, $2.79\times10^{-5}$ | 2.9975 | $2.52\times10^{-5}$, $2.65\times10^{-6}$ | 3.2509 |
| AMR 2–3 → 3–4 | $1.64\times10^{-4}$, $2.06\times10^{-5}$ | 3.1045 (printed) | $3.33\times10^{-5}$, $3.87\times10^{-6}$ | 2.8564 (printed) |

They conclude that the accuracy on the adaptive grid is comparable with that of the coarser
uniform grid. The uniform-row EOCs follow from the printed errors; the AMR-row EOCs do not:
$\log_2(1.64\times10^{-4}/2.06\times10^{-5})=2.99$ and $\log_2(3.33\times10^{-5}/3.87\times10^{-6})=3.11$,
so the printed 3.1045 matches the velocity errors and no pairing of the printed errors gives 2.8564
*(compiler check, not in the sources)*.

**Orders 3 to 7 of a generalized Active Flux.** Barsukow et al.'s semi-discrete Active Flux
method of arbitrarily high order in two dimensions, with edge point values at Gauss–Legendre
positions between the cell vertices (the placement their stability analysis requires) and
SSP-RK3 in time, approximates the exact solution better as the
order rises from 3 to 7 on the same $60\times60$ grid (Figs. 12–13). The comparison is
qualitative; their error tables are for scalar advection. Their maximal CFL numbers come from a
numerical eigenvalue analysis of two-dimensional advection, $C_{\mathrm{cfl}}=0.27$, 0.20,
0.17, 0.12, 0.088 for orders 3–7 (Table 3), defined with the common component $a_x=a_y$ of the
advection velocity at $45^\circ$; they also quote 0.28 for acoustics from another work of
theirs.

## Non-irrotational periodic wave

[Chudzik, Helzel & Lukáčová-Medvid'ová (2024)](/sources/chudzik-2024.md) Ex. 5.1 build a
periodic test on $[-1,1]^2$, $c=1$, whose velocity is not curl-free: $p_0=0$,
$v_0=\tfrac1c\big(-(\sin2\pi x+\sin2\pi y),\ \sin2\pi x+\sin2\pi y\big)$, with exact solution
$p=\tfrac1c(\cos2\pi x-\cos2\pi y)\sin(2\pi ct)$,
$v_1=-\tfrac1c(\sin2\pi x\cos(2\pi ct)+\sin2\pi y)$,
$v_2=\tfrac1c(\sin2\pi x+\sin2\pi y\cos(2\pi ct))$: the parts $\sin2\pi y$ of $v_1$ and
$\sin2\pi x$ of $v_2$ are a stationary divergence-free field, the others a standing wave
*(compiler check, not in the sources)*.
Their bicharacteristic EG2 operator for the point values, at $\nu=0.267$, gives $L^1$ orders
2.92 in $p$ and 2.97 in the velocity at $t=0.1$ on $64^2$–$256^2$; the Eymann–Roe operator,
exact only for constant vorticity, gives 2.99 in $p$ but 2.00 in the velocity, and the exact
operator 2.99 and 2.44, its velocity order depending on the final time (Tables 3–5). The test
separates operators that the sine wave above, which has zero vorticity, cannot.

## High-frequency radial pulse

Calhoun et al. §4.5.2, Eq. (32), start from $p_0=2+\exp\big(-100(r-0.5)^2\big)\sin(100r)$,
$v_0=0$, on the periodic $[-1.5,1.5]^2$ ($r$ the distance from the origin, page-local), with
adaptive levels 3 to 6 and refinement where $\lvert p_{\max}-p_{\min}\rvert\ge0.001$ on a
patch. At $t=0.3$, 0.6 and 0.9 the wave packet crosses the coarse–fine interfaces without
visible spurious grid effects, apart from a smearing they attribute to the domain boundary
(Figs. 14–15). The test is qualitative.

## Stationary vortex

The velocity of the [Gresho vortex](/benchmarks/gresho-vortex.md) with $p=0$,
$v=v_\theta(r)(-\sin\theta,\cos\theta)$ with $v_\theta=5r$ on $r\le0.2$, $2-5r$ on
$0.2<r\le0.4$ and $0$ beyond ($\theta$ the polar angle, page-local), is divergence-free and
therefore a stationary state of linear acoustics. Chudzik et al. (Ex. 5.2, on the periodic
$[-0.75,0.75]^2$, $t=100$ on $128^2$) find that the exact acoustic operator keeps the discrete
steady state, while EG2 does not but stays closer to the exact vorticity profile than the
Eymann–Roe operator (Figs. 8–10). Calhoun et al. (§4.6) run it with the Eymann–Roe operator,
which is not stationarity preserving, and find accurate results at $t=100$ with third order and
adaptive refinement (Fig. 16); with the stationarity-preserving operator of Barsukow et al.
the steady state is kept on a regular grid but their adaptive solver becomes unstable, an
observation without a figure. As recalled by both papers, Barsukow showed that the Cartesian
Active Flux method with the exact operator adds no dissipation to discrete representations of
all stationary states.

## Linear-wave eigenmodes of the nonlinear equations

A relative of these tests runs the full Euler or ideal-MHD equations
with a small-amplitude exact eigenmode on a uniform state, one wave
period, and measures the $L_1$ error against the initial data under
refinement. [Stone et al. (2026)](/sources/stone-2026.md) §§3.1–3.2
verify the reconstructions of [AthenaK](/software/athenak.md) this way,
in one dimension and always on primitive variables (amplitudes and
background states not printed):

- *Hydrodynamics* (sound and entropy waves): fourth order for RK3 with
  PPM under the extremum-preserving limiters of McCorquodale et al.
  ("PPMX") and for RK3 with [WENO-Z](/methods/weno-z.md), until
  nonlinear effects or round-off dominate; second order for RK2 with
  PLM and for RK3 with PPM under the original Colella–Woodward limiters
  ("PPM4"); the same as the corresponding figure of the earlier Athena
  code (Fig. 1).
- *Ideal MHD* (fast, slow and Alfvén waves): fourth order for RK3 with
  PPMX or WENO-Z on the slow and Alfvén waves, while the fast wave
  converges only at second order "even in one dimension", a result they
  report as reproducing the Athena++ paper without giving a cause;
  second order for PPM4 and PLM on all waves (Fig. 3).

The entropy wave is also recorded on
[density-wave advection](/benchmarks/density-wave-advection.md), PPM on
[piecewise parabolic method](/methods/piecewise-parabolic-method.md).

## Qualifications

- All the convergence data are third order; the arbitrary-order comparison of Barsukow et al.
  on this system is visual. No source compares two discretization families (Active Flux against
  finite volumes or DG) on these data.
- Calhoun et al.'s and Barsukow et al.'s sine waves differ only by the sign of $p$, which is a
  symmetry of the linear system together with $v\mapsto-v$; Barsukow et al.'s printed velocity
  is the one that breaks it (above).
- Barsukow et al. are read as the arXiv v2 preprint, Calhoun et al. as the arXiv v2 preprint,
  Chudzik et al. as the version of record (see their Source pages).
- A nonlinear relative: [Zampa & Dumbser (2025)](/sources/zampa-2025.md) §4.2 run a smooth
  acoustic pulse of the Euler equations, $p=1+e^{-40r^2}$, $\rho=1$, $v=0$ on the periodic
  $[-2,2]^2$, to $t=1$ on $120\times120$ unstructured triangles, against a radial
  finite-volume reference (Figs. 1–2); it is not a linear-acoustics test.

# Citations

- [Calhoun, Chudzik & Helzel (2023)](/sources/calhoun-2023.md) — §1, §4.5.1–4.5.2, §4.6, Eqs. (31)–(32), Table 4, Figs. 13–16 (arXiv v2).
- [Barsukow et al. (2026)](/sources/barsukow-2026.md) — §4, §5.2, Eq. (42), Table 3, Figs. 12–13 (arXiv v2).
- [Chudzik, Helzel & Lukáčová-Medvid'ová (2024)](/sources/chudzik-2024.md) — §2.1, Ex. 5.1–5.2, Tables 3–5, Figs. 8–10.
- [Zampa & Dumbser (2025)](/sources/zampa-2025.md) — §4.2, Figs. 1–2 (arXiv v1; nonlinear relative).
- [Stone et al. (2026)](/sources/stone-2026.md) — §§3.1–3.2, Figs. 1 and 3 (eigenmode relatives).

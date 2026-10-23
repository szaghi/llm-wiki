---
type: Benchmark
title: "Burgers equation tests"
description: "The inviscid Burgers equation as test bed: sine data for accuracy before the shock and shock capturing after, energy and entropy tests of split forms, discontinuous data, a slow shock across a block interface, 2D Riemann and sine data, the latter on adaptive Active Flux grids, and gamma = 3 Euler data reducing to Burgers; setups, breaking times, orders."
status: established
aliases: [Burgers equation, inviscid Burgers test, Burgers sine wave, two-dimensional Burgers Riemann problem]
tags: [benchmark, weno, cweno, dg]
timestamp: 2026-10-23T23:00:00Z
---

# Burgers equation tests

The inviscid Burgers equation $\partial_tu+\partial_x(u^2/2)=0$, and its
two-dimensional form $\partial_tu+\partial_x(u^2/2)+\partial_y(u^2/2)=0$,
is the simplest genuinely nonlinear conservation law. Smooth data
steepen and form a shock at the breaking time
$t_{\mathrm b}=-1/\min_xu_0'(x)$ (page-local symbol), so a single
initial profile serves two tests: an accuracy test at $t<t_{\mathrm b}$,
where the exact solution follows from characteristics, and a
shock-capturing test at $t>t_{\mathrm b}$. The sources also use
discontinuous data, a slow shock across a block interface, a two-dimensional Riemann problem, and Euler data
that reduce exactly to Burgers.

## Sine data: accuracy and shock formation

| Source | Data | Domain | Accuracy time | Shock time |
|---|---|---|---|---|
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.1 | $u_0=0.5+\sin(\pi x)$ | $[0,2]$, periodic | $0.5/\pi$, 10–320 cells | $1.5/\pi$, 200 cells |
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.2 | $u_0=0.5+\sin(\pi(x+y)/2)$ | $[0,4]^2$, periodic | $0.5/\pi$, $10^2$–$320^2$ | $1.5/\pi$, $200^2$, cut along $x=y$ |
| [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) Ex. 3.1 | $u_0=0.5+\sin(\pi x)$; 2D $u_0=0.5+\sin(\pi(x+y)/2)$ | $[0,2]$; $[0,4]^2$, periodic | $0.5/\pi$, 10–320 cells; $10^2$–$320^2$ | — |
| [Puppo, Semplice & Visconti (2023)](/sources/puppo-2023.md) §4.1, §4.3.1 | $u_0=0.5-0.25\sin(\pi x)$ | $[0,2]$, periodic | $1$, $\Delta t=h,10h,50h$ | $2$, 256 cells, $\Delta t=3h,5h$ |
| [Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md) §4.1 | $u_0=\sin(\pi x)+0.01$ | $[0,2]$, periodic | — | $3$, 8 elements, $N=4,5$, RK4, $\Delta t=10^{-4}$ |
| [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) §5.1.1 | $u_0=\sin(2\pi x)+2$ | $[0,1]$, periodic | — | $0.5$, $\mathbb P_4$ on 15 and $\mathbb P_{14}$ on 5 elements |
| [Yu & Hesthaven (2022)](/sources/yu-2022.md) §5.2 | $u_0=\sin(2\pi x)$, flux printed $u^2$ | $[0,1]$ | — | $0.3$, 80 elements |
| [Sousa & Scalo (2022)](/sources/sousa-2022.md) §2.3 | $u_0=1+\tfrac12\sin(\pi x)$ | $[-1,1]$, periodic | — | $1$, Fourier pseudo-spectral, 128 points, RK4 |
| [Zhong et al. (2023)](/sources/zhong-2023.md) Ex. 5 | $u_0=0.5+\sin(\pi x)$ | $[0,2]$, periodic | $0.15$, 20–320 cells | $0.5$, 20 and 40 cells, reference WENO-JS on 10000 |
| [Calhoun, Chudzik & Helzel (2023)](/sources/calhoun-2023.md) §4.4 | $u_0=\sin(2\pi x)\sin(2\pi y)+0.1$, 2D flux $(u^2/2,u^2/2)$ | $[0,1]^2$, boundary conditions not stated | $0.05$, AMR | $0.2$, $0.6$, $1.0$, AMR levels 3–5 |
| [Qin et al. (2023)](/sources/qin-2023.md) §3.2 | $u_0=0.25+0.5\sin(\pi x)$ | $[-1,1]$, periodic, boundary closures kept active | $0.3$, 40–640 points | $4$, $7.9$, $8.1$, 200 points |

For $u_0=0.5+\sin(\pi x)$, $t_{\mathrm b}=1/\pi$ (stated by Zhong et
al.); along the diagonal the
two-dimensional data have the same breaking time (the data of Li, Shu
& Qiu, also run by Fan et al.); for Calhoun et al.'s two-dimensional
data, whose characteristics carry the Jacobian
$1+t\,(\partial_xu_0+\partial_yu_0)$ and
$\partial_xu_0+\partial_yu_0=2\pi\sin(2\pi(x+y))$,
$t_{\mathrm b}=1/(2\pi)\approx0.16$ *(compiler check, not in the
sources)*; for
$u_0=0.5-0.25\sin(\pi x)$, $t_{\mathrm b}=4/\pi\approx1.27$ *(compiler
check, not in the sources)*. The accuracy times thus lie before and
the shock times after breaking. Likewise $t_{\mathrm b}=1/\pi$ for
Cicchino et al., $1/(2\pi)\approx0.16$ for Dzanic et al., $2/\pi\approx0.64$
for Sousa & Scalo and for Qin et al. (who print $t=2/\pi$ themselves), and, with Yu & Hesthaven's flux $u^2$ (characteristic
speed $2u$), $1/(4\pi)\approx0.08$ *(compiler check, not in the
sources)*: all four run past breaking.

**Orders.** Li, Shu & Qiu's sixth-order moment-based
[multi-resolution HWENO](/methods/hermite-weno.md), with the first
moments modified only in cells flagged by their indicator (M5-I),
reaches $L^1$ error $3.95\times10^{-13}$ at 320 cells (order 5.96) in
1D and $6.83\times10^{-12}$ at $320^2$ (order 6.36) in 2D; modifying the
moments in every cell (M5-NI) drops the order to five, as they expect
(4.97 and 4.88; Tables 3.1–3.2). Fan, Zhao, Xiong & Qiu's fifth-order finite-difference
[Hermite WENO](/methods/hermite-weno.md) with restricted derivatives
(HWENO-R) gives $L^1$ errors $3.69\times10^{-10}$ at 320 cells and
$3.64\times10^{-10}$ at $320^2$, against $3.24\times10^{-10}$ and
$3.20\times10^{-10}$ for HWENO-L and $2.12\times10^{-9}$ and
$2.10\times10^{-9}$ for WENO-ZQ (Table 3.1). On meshes of at least 160
cells HWENO-R costs about 1.2 times the CPU time of WENO-ZQ (1.45 in
2D) for an error about 5.3 times smaller, so it is the more efficient at
equal error (Fig. 3.1). Its observed 1D orders oscillate, 2.98, 4.61,
6.99, 6.15, 5.32, which the authors explain only qualitatively
(Remark 3.1); $\log_2(1.32\times10^{-4}/1.04\times10^{-6})=6.99$
reproduces the printed order at 80 cells *(compiler check, not in the
sources)*. Back to Li, Shu & Qiu: on the shocked data the unmodified and
modified schemes both match the exact solution with "not much
difference" (Figs. 3.1–3.2). Puppo et al.'s time-limited implicit
[Quinpi](/methods/quinpi.md) scheme Q3P1 converges at third order even
at time steps of 10 and 50 cell widths: $L^1$ errors
$3.66\times10^{-7}$ ($\Delta t=h$, 2560 cells), $1.29\times10^{-7}$
($\Delta t=10h$, 5120 cells) and $1.41\times10^{-5}$ ($\Delta t=50h$,
5120 cells), with finest-grid rates 2.99, 2.99 and 2.79 (Table 1);
implicit Euler is first order and the unlimited DIRK–CWENO scheme D3P1
third order on the same data (Fig. 1). After the shock forms, Q3P1 is
slightly more diffusive than D3P1 but much less than implicit Euler,
and at $\Delta t=5h$ it reduces D3P1's oscillations (Figs. 4–5).

**Symmetric smoothness indicators.** Zhong et al.'s fifth-order
finite-volume IMWENO-P, whose smoothness indicators satisfy their
mirror-symmetry condition (see
[smoothness indicator](/definitions/smoothness-indicator.md)), reaches
fifth order on the smooth data with $L_1$ error $3.30\times10^{-9}$ at
320 cells, against $1.63\times10^{-8}$ for
[WENO-JS](/methods/weno-js-reconstruction.md) (Table 6; SSP-RK3, global
Lax–Friedrichs flux, CFL number $(\Delta x)^{2/3}$); the shocked solutions at $t=0.5$ on 20 and 40 cells are
compared with the WENO-JS reference (Fig. 3).

**Boundary closures.** Qin et al. run the sine with their fifth-order
multi-resolution [WCNS](/methods/weighted-compact-nonlinear-scheme.md)
and one-sided nonlinear [boundary closures](/methods/shock-capturing-boundary-closure.md)
used at the ends of a periodic domain, with global Lax–Friedrichs
splitting. At $t=0.3$ the $L_2$ order is 5.16 and the $L_\infty$ order
4.97 at 640 points; their scaled smoothness indicators (scaling
parameter $\lambda=2$, page-local)
give larger errors than $\lambda=1$ on coarse grids ($L_2$
$6.92\times10^{-5}$ against $4.37\times10^{-5}$ at 40 points) and the
same from 160 points (Table 11). After breaking, the shock reaches $x=0$
at $t=4$ and crosses the periodic boundary between $t=7.9$ and $8.1$
with correct profile and location (Fig. 3); the shock moves at speed
$0.25$, and its positions $0$, $\approx0.975$ and $\approx-0.975$ at the
three times follow from the characteristic through $x=1$ *(compiler
check, not in the sources)*.

**Shock capturing in element methods.** Dzanic, Trojak & Witherden
use the shocked sine to show that their residual-based
[artificial viscosity](/methods/artificial-viscosity.md) with $c_\mu=1$
resolves the shock over 4–5 solution points without spurious
oscillations at $\mathbb P_{14}$ on 5 elements, at a width similar to
$\mathbb P_4$ on 15 elements, with the viscosity localized at the shock:
"the proposed approach does not suffer with increasing approximation
order" (§5.1.1, Fig. 1). Yu & Hesthaven capture the discontinuity
without spurious oscillations on 80 elements with ANN-predicted
viscosity, whose peak decreases with the degree; a slight asymmetry of
the viscosity is attributed to the randomness of the training samples
(§5.2, Figs. 5–6).

**Spectral make-up of added dissipation.** Sousa & Scalo filter the
shocked sine with a sharp spectral filter and compute the exact
sub-filter flux from the characteristic solution: its energy spectrum
spans all resolved wavenumbers with a plateau and a cusp near the
cut-off, the shape of the Kraichnan and Chollet–Lesieur turbulence
spectra, here produced by shock formation (§2.3, Fig. 1b). A
posteriori, dynamic Smagorinsky dissipates uniformly across the
spectrum, over-damps large scales, under-damps near the cut-off and
lets oscillations pile up, and spectral vanishing viscosity with an
inviscid low range under-damps low wavenumbers; their
[quasi-spectral viscosity](/methods/quasi-spectral-viscosity.md), tuned
on this test, matches the exact spectrum best (Fig. 1).

**Active Flux on adaptive grids.** Calhoun, Chudzik & Helzel run the
two-dimensional sine data with their Cartesian
[Active Flux](/methods/active-flux.md) method in ForestClaw
([adaptive mesh refinement](/methods/adaptive-mesh-refinement.md) with
subcycling and a conservative fix at coarse–fine interfaces). The
point values are evolved by a fixed-point iteration of the implicit
characteristic relation $u(x,y,t)=u_0(x-ut,\,y-ut)$, each iteration
gaining one order, two iterations from a first-order guess giving the
third order of the biquadratic reconstruction (§2.2). At $t=0.05$, with
refinement fixed along the diagonal and CFL at most 0.5, they state
third order, with the result "not shown here". At $t=0.2$, $0.6$ and
$1.0$ on levels 3–5, unlimited Active Flux shows unphysical oscillations
along the curve where the characteristic speed changes sign; the
bound-preserving limiter of their earlier work, applied where the
refinement criterion flags steep gradients, avoids them (Fig. 12).

## Space–time Burgers: accelerating shock and shock merger

[Huang & Zahr (2022)](/sources/huang-2022.md) (arXiv v2) solve
Burgers' equation as a steady problem in the space–time slab with their
high-order [implicit shock tracking](/methods/implicit-shock-tracking.md)
method, which moves the mesh so that element faces fit the
discontinuity:

- *Accelerating shock* (§6.2.1, iburg-acc): $(z,t)\in(-0.2,1)\times(0,1.2)$,
  inflow value $\mu_1=4$ at $z=-0.2$, $\mu_2=3$. The exact solution
  (79) is $u=\mu_1$ left of the shock and $u=\mu_2(z-1)/(1+\mu_2t)$
  right of it, and the shock path (80) starts at $z=0$ and accelerates.
  On 72 right triangles whose hypotenuses cross the shock, with
  $p=q=1,2,3$, the discontinuity is mostly tracked after 20 iterations;
  re-initializing oscillatory elements is needed for $p=3$, without
  which the solver stalls (Figs. 17–19). Under refinement (Table 2) the
  solution error $E_\phi$ along $z=0.8$ decreases with segment slopes
  5.88, 3.92, 2.88 for $p=2$ and 6.60, 5.21, 3.73 for $p=3$, and the
  shock-position error $E_{z_s}$ with slopes of at least $p+1$ except
  the first $p=1$ segment (1.09).
- *Shock formation and merger* (§6.2.2, iburg-form): $(z,t)\in(-1,1)\times(0,1)$,
  $u_0=1.2\exp(-(z+0.5)^2/0.025)-\exp(-(z-0.5)^2/0.025)$, Dirichlet
  data $u_0(\pm1)$, 400 right triangles, $p=q=2,3$. Two shocks form and
  merge in a space–time triple point that the method tracks from a mesh
  carrying no knowledge of them; where the formation is under-resolved
  the steep continuous profile is represented by a growing
  discontinuity (Figs. 21–22).

The printed exact solution satisfies Burgers' equation
($u_t+uu_z=0$ for $u=\mu_2(z-1)/(1+\mu_2t)$), and with
$s=\sqrt{1+\mu_2t}$ the path $z_s=1+(\mu_1/\mu_2)s(s-1)-s$ starts at
$z_s(0)=0$ and moves at the Rankine–Hugoniot speed
$\tfrac12\big(\mu_1+\mu_2(z_s-1)/(1+\mu_2t)\big)$ *(compiler check,
not in the sources)*.

## Energy and entropy tests

Burgers' equation with the square entropy $\eta=u^2/2$ serves as the
scalar test of discrete energy (entropy) conservation in the sources below.
[Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md)
§4 (arXiv v1) split the volume term as
$\tfrac23\partial_x(u^2/2)+\tfrac13u\partial_xu$ in energy-stable
[flux reconstruction](/methods/flux-reconstruction.md) and run the
shocked sine above on Gauss–Lobatto nodes (collocated), on $N+1$ Gauss
nodes (uncollocated) and on $N+3$ Gauss nodes (overintegrated), with
an energy-conservative or a local Lax–Friedrichs interface flux. With
their split form, in which the flux-reconstruction filter also acts on
the non-conservative volume term, the energy is conserved to
$O(10^{-12})$ with the conservative flux and decreases monotonically
with Lax–Friedrichs, for $c_{\mathrm{DG}}$, $c_+$ and $c=10^4$ (their
correction parameters); the conservative DG scheme and the classical
split forms, filtered on the surface only, do neither, except Huynh's
lumped-Lobatto $g_2$ scheme (Tables 1–3). A manufactured solution
$u=\cos(\pi(x-t))$ with source term
$\pi\sin(\pi(x-t))\big(1-\cos(\pi(x-t))\big)$ to $t=1$ gives orders
near $N+1$ for $N=4$ and about 5.7 for $c_+$ at $N=5$ (Tables 4–7). See
[split convective forms](/methods/split-convective-forms.md) and
[entropy stability](/properties/entropy-stability.md).

[Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) (arXiv v4)
use two Burgers-type tests of their
[entropy correction term](/methods/entropy-correction-term.md):

- Example 2.12, $\partial_tu+\partial_x(u^2/2)=0$ on periodic $[0,3]$
  with $u_0=-1$ on $(1,2)$ and $+1$ elsewhere, whose entropy solution
  has a stationary shock at $x=1$ and a rarefaction at $x=2$. Central
  finite-difference and Fourier collocation schemes, with or without
  the correction, keep the initial data stationary, so a global entropy
  equality does not make a scheme converge to the entropy solution (no
  numbers given). The shock at $x=1$ is stationary because the
  Rankine–Hugoniot speed is $\tfrac12(1+(-1))=0$, and the jump at $x=2$
  from $-1$ to $+1$ is an expansion shock in the initial data
  *(compiler check, not in the sources)*.
- §4.1, a two-dimensional Burgers-type equation
  $\partial_tu+\partial_x(\cos u)+\partial_yu=0$ on the unit disk with
  $u_0=\exp(-40(x^2+y^2))$, outflow, to $t=0.2$ before shock formation,
  third-order continuous Galerkin residual distribution, SSPRK(3,3),
  CFL 0.1. The non-polynomial flux makes the quadrature inexact. The
  entropy changes at $t=0.2$ are $1.6819\times10^{-15}$ and
  $1.6822\times10^{-15}$ for the two weightings of the correction, so
  the weighting makes no significant difference on smooth data.

## Discontinuous data and interacting shocks

[Puppo et al.](/sources/puppo-2023.md) §4.3.2–4.3.3 run, on periodic
$[-1,1]$:

- the top hat $u_0=1$ on $|x|\le0.25$, $0$ otherwise, to $t=0.5$ on 400
  cells with $\Delta t=3h,5h$, which develops a rarefaction and a moving
  shock (Fig. 6). Without their conservative correction Q3P1 loses mass
  and misplaces the shock; with it mass is conserved at all times and
  the shock is correctly placed (Fig. 7). An explicit first-order
  predictor, even at each Runge–Kutta abscissa, does not prevent
  spurious oscillations at $\Delta t=5h$ (Fig. 8);
- $u_0=0.2-\sin(\pi x)+\sin(2\pi x)$ on 256 cells with $\Delta t=5h$,
  shown at $t=1/(2\pi)$ (shock formation), $0.6$ (before the shocks
  interact) and $1$ (after): Q3P1 is non-oscillatory and sharper than
  implicit Euler (Fig. 9).

**Slow shock across a block interface.** [Qin et al.](/sources/qin-2023.md)
§3.2 start from $u_0=1.02$ for $x<0.1$ and $u_0=-1$ otherwise, a shock
of speed $0.01$, on $[0,1]$ split at $x=0.5$ into two blocks of 160 and
80 points (a 2:1 jump of grid spacing). The shock crosses the interface
"with invisible oscillation and phase lag" at $t=40$ and $80$ (Fig. 4);
they cite Pärt-Enander & Sjögreen and Sebastian & Shu for the
stagnation and oscillation of slow shocks at non-conservative
interfaces. A two-dimensional Euler version (shock speed $0.015$) is
recorded on [shock-capturing boundary closures](/methods/shock-capturing-boundary-closure.md).

## Two-dimensional Riemann problem

[Pazner (2021)](/sources/pazner-2021.md) §5.5 solves
$\partial_tu+\nabla\cdot(\tfrac12u^2(1,1))=0$ on $[0,1]^2$ with quadrant
values $-1$ ($x>0.5$, $y>0.5$), $-0.2$ ($x\le0.5$, $y>0.5$), $0.5$
($x\le0.5$, $y\le0.5$) and $0.8$ ($x>0.5$, $y\le0.5$), the exact solution
imposed on the boundary, to $t=0.5$. With $120^2$ degrees of freedom as
$N=2$, $5$, $11$ on $40^2$, $20^2$, $10^2$ elements, and a reference with
$N=1$ on $512^2$ elements, Pazner's subcell
[convex-limited](/methods/convex-limiting.md) DG resolves the solution
well even on the coarsest mesh and captures discontinuities that are
not aligned with element boundaries (Fig. 11). The same quadrant values
and final time are run by [Peng, Sun & Wu (2024)](/sources/peng-2024.md)
Ex. 5.11 on $256^2$ cells, recorded with the Euler configurations on
[two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md).

## Euler data that reduce to Burgers

For $\gamma=3$ the isentropic data $p=\rho^\gamma$, $v=\sqrt\gamma\,\rho$
make the sound speed $c=\sqrt{\gamma p/\rho}=\sqrt3\,\rho$ equal to $v$.
The Riemann invariant $v-c$ is then identically zero, and the other,
$v+c=2\sqrt3\,\rho$, is transported at its own speed $v+c$, so it obeys
Burgers' equation *(compiler check, not in the sources)*. The sources
use this to obtain exact smooth Euler solutions:

- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) Ex. 1: $\gamma=3$,
  $\rho=(1+0.2\sin x)/(2\sqrt\gamma)$, $v=\sqrt\gamma\rho$, $p=\rho^\gamma$
  on periodic $[0,2\pi]$; $2\sqrt\gamma\rho$ solves Burgers with data
  $1+0.2\sin x$, smooth until $t=5$, and the run stops at $t=3$. An
  artificial material interface between identical fluids starts at
  $x=\pi$ with their full interface algorithm active; the density
  converges at fifth order, $L^1$ error $1.05\times10^{-5}$ at 80 points to
  $1.07\times10^{-8}$ at 320 (order 5.14; Table 2). Ex. 8 is the 2D
  analogue, $\rho=(1+0.2\sin((x+y)/2))/\sqrt{2\gamma}$,
  $v_1=v_2=\sqrt{\gamma/2}\,\rho$ on $[0,4\pi]^2$ with an artificial
  circular interface, $t=3$: $9.57\times10^{-6}$ at $80^2$ to
  $1.24\times10^{-8}$ at $320^2$ (order 5.06; Table 4).
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.3–3.4 use the
  same data with the factors printed as $2\sqrt3$ and $\sqrt6$, which
  equal $2\sqrt\gamma$ and $\sqrt{2\gamma}$ only for $\gamma=3$, a value they
  do not state *(compiler check, not in the sources)*; exact solution taken from their
  earlier paper; $t=3$. M5-I reaches $1.69\times10^{-12}$ at 320 cells
  (order 6.03) and $4.67\times10^{-11}$ at $320^2$ (6.49), M5-NI again
  about fifth order (Tables 3.3–3.4).

The breaking time of $1+0.2\sin x$ is $1/0.2=5$ *(compiler check, not
in the sources)*, matching Zheng et al.'s statement.

## Qualifications

- Li, Shu & Qiu caption the Burgers figures "density" and call the
  unknown $\mu$, the letter of the velocity in their Euler examples.
- Their M5-I orders 8.85 and 8.72 at 40 and 80 cells (Table 3.1)
  exceed the design order six and are not commented on.
- Puppo et al.'s Table 1 prints a rate on the first row of each
  sub-table, against a coarser grid that is not listed; their Fig. 7
  caption gives $t=5$ for a test that ends at $t=0.5$.
- Cicchino et al. write that "all schemes yield the expected
  convergence rates of $p+1$", while their split form with $c_+$ at
  $N=5$ gives 5.70–5.76 (Tables 5, 7); they define $c_+$ as the value at
  which an order is about to be lost, which explains the rates but not
  the sentence.
- Yu & Hesthaven print the flux as $f=u^2$, not $u^2/2$, a scaling that
  doubles the wave speeds against the other sources.
- Huang & Zahr print the initial condition (78) as
  $\mu_1H(-z)-\mu_2H(z)$, a constant right state $-3$, which would move
  the shock at the constant speed $(4-3)/2=1/2$; their exact solution
  (79) and shock path (80), consistent with each other, start instead
  from $\mu_2(z-1)$ for $z>0$ *(compiler check, not in the sources)*.
  Their Table 2 caption says the slopes "tend to at least the optimal
  rate ($p+1$)", while the final $E_\phi$ slopes for $p=2,3$ are 2.88
  and 3.73; the printed slopes agree with the printed errors and mesh
  sizes ($\ln(6.36/0.866)/\ln(3.63/1.81)=2.87$) *(compiler check, not
  in the sources)*.
- Calhoun et al. print the refinement criterion as
  $(q_{i,j+1}-q_{i,j+1})/(2\Delta y)\ge15$ (their $q$ is $u$), which is
  identically zero, next to the centred
  $(q_{i+1,j}-q_{i-1,j})/(2\Delta x)\ge15$ for $x$, so the $y$-criterion
  read as the centred difference $q_{i,j+1}-q_{i,j-1}$ is the
  non-trivial one; both are printed without absolute values. They are
  read in the arXiv v2 preprint.
- The accuracy tests of Zheng et al. use $\Delta t=O(\Delta x^{5/3})$;
  the other sources' accuracy runs state CFL 0.6 with a reduced time
  step (Li, Shu & Qiu) or prescribed multiples of $h$ (Puppo et al.).

# Citations

- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — Ex. 3.1–3.4, Tables 3.1–3.4, Figs. 3.1–3.2 (arXiv v1).
- [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) — Ex. 3.1, Table 3.1, Fig. 3.1, Remark 3.1.
- [Huang & Zahr (2022)](/sources/huang-2022.md) — §6.2.1–6.2.2, Eqs. (78)–(80), Table 2, Figs. 17–22 (arXiv v2).
- [Puppo, Semplice & Visconti (2023)](/sources/puppo-2023.md) — §4.1, §4.3, Table 1, Figs. 1, 4–9 (arXiv v2).
- [Pazner (2021)](/sources/pazner-2021.md) — §5.5, Fig. 11 (arXiv v1).
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — Ex. 5.11 (arXiv v1).
- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) — §4, Ex. 1 and Ex. 8, Tables 2 and 4.
- [Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md) — §4.1–4.2, Tables 1–7 (arXiv v1).
- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — §5.1.1, Fig. 1 (arXiv v2).
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §5.2, Figs. 5–6.
- [Sousa & Scalo (2022)](/sources/sousa-2022.md) — §2.3, Fig. 1 (arXiv v2).
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — Example 2.12; §4.1, Eq. (44) (arXiv v4).
- [Qin et al. (2023)](/sources/qin-2023.md) — §3.2, Table 11, Figs. 3–4.
- [Zhong et al. (2023)](/sources/zhong-2023.md) — §4.1, Ex. 5, Table 6, Fig. 3.
- [Calhoun, Chudzik & Helzel (2023)](/sources/calhoun-2023.md) — §2.2, §4.4, Eqs. (7)–(10), (30), Fig. 12 (arXiv v2).

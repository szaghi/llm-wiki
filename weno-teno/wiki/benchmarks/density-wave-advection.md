---
type: Benchmark
title: "Density-wave advection"
description: "Smooth density (entropy) wave carried at uniform velocity and pressure, the exact Euler solution being pure translation; used as a 1D and 2D order-of-accuracy test of Euler and Navier–Stokes schemes, as a long-time dissipation test, and as a probe of pressure-equilibrium and entropy conservation of kinetic-energy-preserving fluxes."
status: established
aliases: [density wave, entropy wave advection, sine density wave, advection of an entropy wave, density perturbation advection]
tags: [benchmark, kinetic-energy-preserving, entropy-stable, low-dissipation, weno]
timestamp: 2026-10-23T20:00:00Z
---

# Density-wave advection

With uniform velocity $v_0$ and pressure $p_0$, any density profile
$\rho_0(x)$ is carried unchanged: $\rho(x,t)=\rho_0(x-v_0t)$, $v=v_0$,
$p=p_0$ is an exact solution of the Euler equations, a pure entropy
(contact) wave *(compiler check, not in the sources: the momentum and
energy equations reduce to the mass equation when $v$ and $p$ are
uniform)*. On a periodic domain the solution returns to the initial
data after each period, so errors are measured against the initial or
translated profile. The sources use the wave three ways: as the
simplest order-of-accuracy test of a scheme for the Euler (and, with
small viscosity, Navier–Stokes) equations; as a long-time test of
dissipation and dispersion; and as a test of whether a discretization
keeps the uniform pressure and velocity exactly, the discrete
[pressure-equilibrium](/properties/pressure-equilibrium-preservation.md)
property, and conserves entropy.

## Setups

| Source | Profile $\rho_0$ | $v_0$, $p_0$ | Domain, boundaries | Grid, time | Use |
|---|---|---|---|---|---|
| [Wang et al. (2023c)](/sources/wang-2023-c.md) Example 4.1 | $1+0.2\sin(\pi x)$ | 1, 1 | period 2 | 10–320 points (Euler), 20–320 (Navier–Stokes); $t=2$ | fifth-order accuracy, CFL 0.6 |
| Wang et al. (2023c) Example 4.2 | $1+0.2\sin(\pi(x+y))$ | $(1,1)$, 1 | $[0,2]^2$, periodic | $10^2$–$320^2$ (Euler), $20^2$–$320^2$ (Navier–Stokes); $t=2$ | 2D accuracy |
| [Zhao, Ji, Shyy & Xu (2023)](/sources/zhao-2023.md) §4.1 | $1+0.2\sin(\pi x)$ | 1, 1 | $[0,2]$, periodic | $h=1/10$–$1/80$, $\Delta t=0.5\Delta x^2$; final time not printed | eighth-order accuracy |
| Zhao et al. §4.4 | $1+0.5\,e^{-\ln2\,x^2/b^2}$, $b=2$ and $1.5$ | 1, 1 | $[-800,1000]$, free-flow | $h=1$, $t=400$, CFL 0.4 and 0.8 | long-time propagation |
| [De Michele & Coppola (2023b)](/sources/demichele-2023-b.md) §5 | $1+\exp(\sin(2\pi x/L))$, $L=1$ | 1, 1 | $[0,1]$, periodic | 61 points, RK4 at CFL 0.01, to $t=100$ | pressure equilibrium and entropy |
| [Peyvan et al. (2023)](/sources/peyvan-2023.md) §4.4 | temperature $9000+200\sin(2\pi x)$ K, equilibrium five-species composition | 11450 m/s, 195256 Pa | $[0,1]$, periodic | 170 elements, $P=3$, $t=0.1$ | entropy conservation of two-point fluxes |

All with $\gamma=1.4$, except Wang et al.'s Navier–Stokes cases
($\gamma=5/3$, $\mu=0.0005$, $\mathrm{Pr}=2/3$, $\mathrm{Re}=1000$, after
earlier work) and Peyvan et al.'s reacting air (five species, with the
reaction sources switched off). Zhao et al.'s Gaussian has half-width
$b$ at half height: $e^{-\ln2\,x^2/b^2}=\tfrac12$ at $x=b$ *(compiler
check, not in the sources)*. De Michele & Coppola choose a
non-sinusoidal profile because with a pure sine wave they observed a
fortuitous global entropy conservation, from symmetry, despite the lack
of local conservation. Peyvan et al.'s Table 1 prints constant $p$,
$\rho=0.03805$ kg m$^{-3}$ and $u$, with the temperature and composition
varying, so their wave is one of temperature and composition at
printed constant density.

## Findings across sources

**Design order of WCNS and gas-kinetic schemes.** Wang et al. (2023c)
find fifth order for WENO-JS, the original multi-resolution WCNS and
their hybrid multi-resolution
[WCNS](/methods/weighted-compact-nonlinear-scheme.md) in all four
cases, with errors of the two WCNS about one order of magnitude below
WENO-JS (Tables 4.1–4.4, $L^1$ density errors):

| Case, finest grid | WENO-JS | MR-WCNS | hybrid MR-WCNS |
|---|---|---|---|
| 1D Euler, 320 | $1.93\times10^{-10}$ | $2.07\times10^{-11}$ | $1.10\times10^{-11}$ |
| 1D Navier–Stokes, 320 | $7.68\times10^{-9}$ | $7.45\times10^{-10}$ | $7.31\times10^{-10}$ |
| 2D Euler, $320^2$ | $4.28\times10^{-10}$ | $4.95\times10^{-11}$ | $4.65\times10^{-11}$ |
| 2D Navier–Stokes, $320^2$ | $1.44\times10^{-8}$ | $1.52\times10^{-9}$ | $1.50\times10^{-9}$ |

The Navier–Stokes errors are measured against an asymptotic
convergence error, as in the work they follow. Their CPU-time-against-error plots for
three sets of linear weights, $(100,10,1)/111$, equal weights and
$(1,10,100)/111$, show their scheme at fifth order for all three and
the most efficient of the three schemes (Figs. 4.1–4.4); see
[multi-resolution WENO](/methods/multi-resolution-weno.md).

Zhao et al.'s eighth-order compact
[gas-kinetic scheme](/methods/gas-kinetic-scheme.md) with nonlinear
reconstruction gives $L_1$ errors $2.7627\times10^{-4}$,
$3.5968\times10^{-6}$, $1.2672\times10^{-8}$, $5.9689\times10^{-11}$ on
$h=1/10$ to $1/80$ (orders 6.26, 8.15, 7.73) and $L_\infty$ errors
$5.6985\times10^{-4}$ to $1.5194\times10^{-10}$ (orders 6.13, 7.00,
8.71) (Table 1).

**Long-time propagation at large CFL.** On the Gaussian wave to
$t=400$, Zhao et al. run the nonlinear and the linear eighth-order
compact scheme at CFL 0.4 and 0.8 and compare with a sixth-order
DG-$P^5$ result of the literature at $h=6$ and CFL $1/30$, which solved
the linear advection equation without background flow; they state that
their scheme "works very well even for the linear wave propagation"
(Fig. 7).

**Pressure equilibrium of kinetic-energy-preserving fluxes.** De
Michele & Coppola (2023b) compare second-order split fluxes for $\rho$,
$\rho v$ and the internal energy, with a central pressure term: the
arithmetic-mean $\rho$ and internal-energy flux (Aρ-Ae) is not
pressure-equilibrium preserving and blows up at $t\approx22$; the
KEEP(1) truncation of Tamaki, Kuya & Kawai shows spurious pressure and
velocity oscillations of order $10^{-7}$, while their asymptotically
entropy-conservative AEC(1) flux shows none; both have the best entropy
conservation, AEC(1) slightly better, and densities indistinguishable
from Ranocha's entropy-conservative flux, whose entropy production they
report "always equal to machine zero" (Fig. 1). At $t=30$ the
normalized entropy error is $7\times10^{-3}$ for Aρ-He and Aρ-Ap, which
have identical entropy production because for constant $v$ and $p$
their internal-energy fluxes coincide, and $-2\times10^{-3}$ for the
geometric-mean Gρ-Ge. See
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md),
[split convective forms](/methods/split-convective-forms.md) and
[entropy-conservative flux](/methods/entropy-conservative-flux.md).

**Entropy conservation of two-point fluxes for reacting air.** Peyvan
et al. replace every volume and interface flux of their DGSEM by their
new entropy-conservative two-point fluxes for the five-species
rigid-rotor–harmonic-oscillator model, with no stabilization,
positivity limiter or sources. The global entropy rate stays at order
$10^{-5}$ up to $t=0.1$, not at machine zero, which they attribute to
the tolerance of about $10^{-7}$ of the Newton inversion from energy to
temperature (Figs. 4–5); the attribution is not tested, for example by
varying the tolerance.

## Qualifications

- Wang et al. (2023c) state that the original multi-resolution WCNS
  reaches fifth order only with the first weight set,
  $(100,10,1)/111$, and fails with the other two (Remark 2, Ex. 4.1),
  against the claim of the multi-resolution literature they cite that
  any positive linear weights keep the design order. The evidence is
  their Figs. 4.1–4.4 only, with no tabulated errors for the other
  weight sets, so it is recorded here as their finding, not as an
  established property; no bundle source states the opposite for
  MR-WCNS.
- Zhao et al. do not print the final time of their accuracy test and
  are read as arXiv v1; Peyvan et al. and De Michele & Coppola (2023b)
  as arXiv v1 and v2.
- De Michele & Coppola's claim of exactly zero entropy production for
  Ranocha's flux with RK4 concerns their observed diagnostic at
  CFL 0.01; entropy conservation is a semi-discrete property, and RK4
  adds a time-integration error *(compiler check, not in the
  sources)*.
- Smooth Navier–Stokes cases are not exact translations: heat
  conduction acts on the temperature gradient of the wave *(compiler
  check, not in the sources)*; Wang et al. (2023c) measure them against
  an asymptotic convergence error, not against the initial data.

# Citations

- [Wang et al. (2023c)](/sources/wang-2023-c.md) — Examples 4.1–4.2, Remark 2, Tables 4.1–4.4, Figs. 4.1–4.4.
- [Zhao, Ji, Shyy & Xu (2023)](/sources/zhao-2023.md) — §4.1, §4.4, Table 1, Fig. 7 (arXiv v1).
- [De Michele & Coppola (2023b)](/sources/demichele-2023-b.md) — §5, Fig. 1 (arXiv v2).
- [Peyvan et al. (2023)](/sources/peyvan-2023.md) — §4.4, Table 1, Eq. (97), Figs. 4–5 (arXiv v1).

---
type: Benchmark
title: "Density-wave advection"
description: "Smooth density (entropy) wave carried at uniform velocity and pressure, the exact Euler solution being pure translation; used as a 1D and 2D order-of-accuracy test of Euler and Navier–Stokes schemes, as a long-time dissipation test, and as a probe of pressure-equilibrium and entropy conservation of kinetic-energy-preserving fluxes."
status: established
aliases: [density wave, entropy wave advection, sine density wave, advection of an entropy wave, density perturbation advection]
tags: [benchmark, kinetic-energy-preserving, entropy-stable, low-dissipation, weno]
timestamp: 2026-10-23T23:45:00Z
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
| [Jiang et al. (2024)](/sources/jiang-2024.md) §4.1.1 | $1+0.2\sin(\pi x)$ | 1, 1 | $[0,2]$, periodic | $N=100$, 200, 400 particles, fixed; $t=2$ | accuracy of a Lagrangian particle scheme |
| Jiang et al. §4.1.2 | $1+0.2\sin(x+y)$ | $(1,1)$, 1 | $[0,2\pi]^2$, periodic | $51^2$, $101^2$, $201^2$ particles (and a non-uniform set); $t=1$ | 2D accuracy |
| [Rueda-Ramírez et al. (2024)](/sources/ruedaramirez-2024.md) §3.1 | $2+0.98\sin(2\pi(x+y))$ | $(0.1,0.2)$, 20 | $[-1,1]^2$ | $N_e=4$–$32$ elements per direction, $N=3,4$, CFL 0.9; final time not printed | accuracy under convex limiting with global and local bounds |
| [Trojak & Dzanic (2024)](/sources/trojak-2024.md) §5.1.1 | two species, $\rho=e^{-500x^2}+4\epsilon_{\mathrm v}$, species fraction $\tfrac12(\sin(2\pi x)+1)$ | 1, $2\epsilon_{\mathrm v}$ | $[-0.5,0.5]\times[-0.05,0.05]$, periodic | $N_x=8$–512 elements, $\mathbb P_1$–$\mathbb P_5$; $t=1$ | accuracy and positivity near vacuum |

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

Jiang et al. hold the particles fixed in their accuracy tests, so
these measure the weighted-least-squares approximation with WENO-Z-type
left and right states, not the Lagrangian motion. Rueda-Ramírez et al.'s
amplitude $0.98$ about a mean of 2 brings the minimum density to $1.02$
and is used with a pressure of 20. Trojak & Dzanic's wave is a
near-vacuum test: $\epsilon_{\mathrm v}=10^{-12}$ (page-local; their
$\epsilon$), each species density has minimum $2\times10^{-12}$, and the
two species have $c_p=1.4$, $c_v=1$ and $c_p=4.21$, $c_v=2.52$; the
Gaussian of width parameter 500 is the density, the sine the composition.

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

**Order of a Lagrangian particle scheme.** Jiang et al.'s
Lagrangian weighted-least-squares method converges at order about 2.00
with Roe-type intermediate states between particle pairs (LWLS-RR) and
at 2.22–2.35 with WENO-Z-type reconstruction of the pair states
(LWLS-WENO-Z), with lower errors, in 1D and 2D and for smoothing lengths
$h/\Delta x_0=1.2$–$1.9$ (Tables 1–2); on a non-uniform particle set the
2D errors are "slightly larger" but of the same order of magnitude
(Table 2c). The fifth order of the WENO-Z-type reconstruction does
not show in these rates, and the paper does not discuss why; see
[WENO-Z](/methods/weno-z.md).

**Bounds and order under convex limiting.** Rueda-Ramírez et al.'s
monolithic convex limiting of LGL-DGSEM with global (positivity) bounds
only keeps the design order: mean experimental orders 4.16 for $N=3$
($L^2$ density errors $1.29\times10^{-1}$ to $2.25\times10^{-5}$ on
$N_e=4$ to 32) and 4.75 for $N=4$ ($1.75\times10^{-2}$ to
$8.97\times10^{-7}$) (Tables 1–2). With tight local bounds on density,
velocity and specific total energy the order falls to at most about
two, independent of $N$: mean 1.82 for $N=3$ and 1.61 for $N=4$ (Tables
3–4); the bounds must be relaxed, for instance by a smoothness sensor,
to recover high order. See [convex limiting](/methods/convex-limiting.md).

**Positivity at near vacuum.** Trojak & Dzanic's positivity-preserving
entropy filter for two-species DG (flux reconstruction in PyFR)
converges at fitted rates 2.28, 3.16, 3.93, 5.17 and 6.61 in $L^\infty$
for $\mathbb P_1$–$\mathbb P_5$ with their pressure-jump entropy switch,
and at 2.28, 3.16, 3.93, 5.22 and 6.47 with the entropy constraint
active everywhere, with nearly identical errors (Tables 1–2): the
authors observe $p+1$ convergence "even at smooth extrema" and conclude
that the scheme keeps its high-order accuracy with the entropy
constraints active. See [entropy filtering](/methods/entropy-filtering.md)
and [bound preservation](/properties/bound-preservation.md).

## Qualifications

- Trojak & Dzanic's printed rates are least-squares slopes over all
  grids; pairwise rates are irregular (for example 5.85 for $\mathbb P_3$
  from 32 to 64 elements), so the data are pre-asymptotic *(compiler
  check, not in the sources)*. The paper is read as arXiv v1.
- Jiang et al.'s Table 2b prints the $L_2$ error $3.95\times10^{-4}$ on
  $201^2$ particles at $h/\Delta x_0=1.5$ with a rate 2.347, which holds
  only for $3.95\times10^{-5}$, the value of the $L_{\mathrm{RMS}}$
  error on the same row *(compiler check, not in the sources)*.
- Rueda-Ramírez et al. are read as arXiv v1 and do not print the final
  time of their convergence test.

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
- [Jiang et al. (2024)](/sources/jiang-2024.md) — §4.1, Tables 1–2.
- [Rueda-Ramírez et al. (2024)](/sources/ruedaramirez-2024.md) — §3.1, Eq. (46), Tables 1–4 (arXiv v1).
- [Trojak & Dzanic (2024)](/sources/trojak-2024.md) — §5.1.1, Eqs. (36a)–(36e), Tables 1–2 (arXiv v1).

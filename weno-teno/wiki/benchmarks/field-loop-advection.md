---
type: Benchmark
title: "Magnetic field-loop advection"
description: "Two-dimensional ideal-MHD test in which a weak cylindrical magnetic loop, defined by a vector potential, is advected diagonally across a periodic box; with the magnetic field nearly passive, the loop shape and magnetic-energy decay measure the dissipation of constrained-transport schemes, here at fourth order and at low Mach number."
status: established
aliases: [field loop advection, advection of a magnetic field loop, current loop advection, Gardiner–Stone field loop]
tags: [benchmark, mhd, relativistic, low-dissipation]
timestamp: 2026-10-23T23:45:00Z
---

# Magnetic field-loop advection

A weakly magnetized cylindrical loop of field lines is carried by a
uniform flow across a doubly periodic box and, after an integer number
of periods, should return unchanged. The field is set from the out-of-plane
vector potential $\mathsf A_3$ (page-local), $B_1=\partial_y\mathsf A_3$,
$B_2=-\partial_x\mathsf A_3$, with $\mathsf A_3$ proportional to the
distance from the loop's edge, so $\lvert B\rvert$ is uniform inside the
loop and zero outside: the loop boundary is a tangential discontinuity
of $B$. Because the thermal pressure dominates, the field behaves almost
as a passive scalar, and the smearing of the loop and the decay of the
magnetic energy measure the numerical dissipation of the
[constrained-transport](/properties/divergence-free-magnetic-field.md)
discretization ([Berta et al. (2024)](/sources/berta-2024.md) §5.4,
after Gardiner & Stone and Mignone as they cite them;
[Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) Ex. 5.8, which call
it a test of "capturing a tangential discontinuity for a
multidimensional flow").

## Setup as printed

Both sources use $[-1,1]\times[-0.5,0.5]$, doubly periodic, on
$256\times128$ cells, $\rho=1$, and a loop of radius $0.3$ centred at
the origin with amplitude $10^{-3}$; with $r=\sqrt{x^2+y^2}$:

| | Berta et al. (2024) §5.4, Eqs. (53)–(54) | Chen, Wu & Xiong (2023) Ex. 5.8 |
|---|---|---|
| equations | ideal MHD and relativistic MHD | ideal MHD in an all-Mach scaling, sonic Mach parameter $\varepsilon$ |
| pressure | $p=1$ (MHD), $p=3$ (RMHD, after Beckwith & Stone) | $p=1$ |
| velocity | $V_0(\cos\vartheta_{\mathrm a},\sin\vartheta_{\mathrm a})$, $\sin\vartheta_{\mathrm a}=1/\sqrt5$, $\cos\vartheta_{\mathrm a}=2/\sqrt5$; $V_0=\sqrt5$ (MHD), $\sqrt5/10$ (RMHD) | $v_0(\cos\vartheta_{\mathrm a},\sin\vartheta_{\mathrm a},0)$, $v_0=1$, $\cos\vartheta_{\mathrm a}=-2/\sqrt5$, $\sin\vartheta_{\mathrm a}=1/\sqrt5$ |
| potential | $\mathsf A_3=10^{-3}(0.3-r)$ for $0.06<r\le0.3$, $0$ "elsewhere" ($R_1=0.2R$) | $\mathsf A_3=10^{-3}(0.3-r)$ for $r\le0.3$, $0$ otherwise |
| final time | $t=2$ (MHD), $t=20$ (RMHD): two periods | $T=\sqrt5$: one period |
| time step | CFL 0.4 | third-order IMEX, CFL 0.25 (paper-wide) |

($\vartheta_{\mathrm a}$ is the page-local advection angle.) The
velocities give displacements $(4,2)$ in Berta et al.'s runs and
$(-2,1)$ in Chen, Wu & Xiong's, integer multiples of the box *(compiler
check, not in the sources)*. Inside the loop
$\lvert B\rvert=10^{-3}$, so the ambient plasma beta
$\beta_{\mathrm p}=2p/\lvert B\rvert^2$ is $2\times10^6$ for $p=1$
*(compiler check, not in the sources)*.

## Runs and findings

**Order and dissipation in fourth-order finite volumes.** Berta et al.
compare the second-order LINEAR scheme, WENO3 (with RK3), and their
fourth-order finite-volume scheme with pointwise
[MP5](/methods/monotonicity-preserving-limiter.md) and pointwise
[WENO-Z](/methods/weno-z.md) reconstructions, with HLL or HLLD fluxes
and the matching upwind constrained-transport averages in MHD, HLL or
GFORCE in RMHD (see [HLL-family solvers](/methods/hll-riemann-solvers.md)):

- the smearing and diffusion of the loop fall markedly from second to
  fourth order, in MHD and RMHD alike (Fig. 6, normalized magnetic
  energy density after two periods);
- WENO-Z "performs the best"; MP5 shows small overshoots at the loop
  tail and undershoots at its head, which they ascribe to "a small
  clipping of its limiting procedure";
- the magnetic energy decays considerably faster at second order than
  at third and fourth order, fourth order being best (Fig. 7); the
  Riemann solver affects the energy conservation only marginally, with
  GFORCE best in RMHD.

They recall that the fifth-order finite-difference WENO-Z and MP5
schemes of Mignone dissipate about 5 % of the total magnetic energy at
the end of the same run, results "very similar" to theirs.

**Low Mach number and cost.** Chen, Wu & Xiong run the loop with their
semi-implicit [IMEX](/methods/imex-runge-kutta.md) fifth-order
finite-difference WENO scheme with constrained transport
([semi-implicit all-Mach scheme](/methods/semi-implicit-all-mach-scheme.md))
at $\varepsilon=0.1$, against an explicit Runge–Kutta WENO scheme with
constrained transport (ERKC) on $256\times128$ and $384\times192$ (Fig.
5.6). The IMEX scheme keeps the symmetric structure of the density
deviation better than ERKC on the same mesh, comparably to ERKC on the
finer one; the magnetic-pressure profiles are nearly identical, and
both schemes slightly distort the profile at $y=0.15$. CPU seconds on
$256\times128$ to $T=\sqrt5$ (Table 5.5, hardware not stated):

| $\varepsilon$ | 0.5 | 0.1 | 0.05 |
|---|---|---|---|
| IMEX | 7634.880 | 5687.467 | 8015.959 |
| ERKC | 4736.466 | 19719.964 | 38666.192 |

ERKC is cheaper at $\varepsilon=0.5$; IMEX is 3.47 times faster at
$\varepsilon=0.1$ and 4.82 times at $\varepsilon=0.05$ *(compiler
check, not in the sources)*.

## Qualifications

- As printed, Berta et al.'s Eq. (54) sets $\mathsf A_3=0$ also for
  $r\le0.06$, so $\mathsf A_3$ jumps by $2.4\times10^{-4}$ at $r=0.06$,
  which would put a singular azimuthal field on that circle
  *(compiler check, not in the sources)*; a constant
  $\mathsf A_3=10^{-3}(0.3-0.06)$ inside $r=0.06$ would give a field-free
  core without that singularity *(compiler check, not in the sources)*.
  Chen, Wu & Xiong's potential has no inner radius.
- The two sources differ in direction, speed, number of periods and
  measured quantity (loop shape and magnetic energy against density
  deviation, magnetic pressure and cost); neither reports an error norm.
- Chen, Wu & Xiong do not state which wave speed sets the explicit
  ERKC time step at $\varepsilon<1$, nor the hardware or the linear
  solver behind Table 5.5.
- Berta et al. are read as the arXiv v4 preprint, Chen, Wu & Xiong as
  arXiv v1.

# Citations

- [Berta et al. (2024)](/sources/berta-2024.md) — §5.4, Eqs. (53)–(54), Figs. 6–7 (arXiv v4).
- [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) — Ex. 5.8, Fig. 5.6, Table 5.5 (arXiv v1).

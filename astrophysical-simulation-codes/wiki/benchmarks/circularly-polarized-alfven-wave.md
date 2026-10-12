---
type: Benchmark
title: "Circularly polarized Alfvén wave"
description: "A finite-amplitude, circularly polarized Alfvén wave, an exact nonlinear solution of ideal MHD, propagated (or held standing) obliquely to a periodic grid; its convergence measures the order of multidimensional MHD schemes, and its regular 3D set-up also serves as a scaling workload."
status: established
aliases: [CPAW, circularly polarised Alfvén wave, Tóth Alfvén wave, nonlinear Alfvén wave]
tags: [benchmark, mhd, verification, constrained-transport, divergence-cleaning, scaling]
timestamp: 2026-10-12T00:00:00Z
---

# Circularly polarized Alfvén wave

**Set-up.** A circularly polarized Alfvén wave of finite amplitude in a
uniform gas with a uniform field along the wavevector is an exact nonlinear
solution of ideal MHD ([Rossazza et al. (2026)](/sources/rossazza-2026.md),
§4.2). The wave is laid obliquely across a periodic grid and run for one
or more periods; it travels when the gas is at rest and stands in a uniform
counter-flow (Cholla's set-up below). The error after whole periods
against the initial state measures the convergence order. Unlike
[linear wave convergence](/benchmarks/linear-wave-convergence.md), the
amplitude is not small. The sources cite different origins: Tóth (2000)
([Stone et al. (2008)](/sources/stone-2008.md)), Tóth (1996)
([Caddy & Schneider (2024)](/sources/caddy-2024.md)) and Mignone,
Tzeferacos & Bodo (2010) ([Rossazza et al. (2026)](/sources/rossazza-2026.md)).

**Runs.**

* *2D, Athena* ([Stone et al. (2008)](/sources/stone-2008.md), §8.4,
  Figs. 19–20). Parameters of Tóth (2000), oblique initialization after
  Gardiner & Stone (2005), $2N\times N$ cells with $N = 4$ to 64, PPM with
  the Colella–Sekora limiters, Roe, CTU with
  [constrained transport](/methods/constrained-transport.md); travelling
  and standing waves, five periods. The amplitude keeps at least 0.8 of its
  initial value at 8 cells per wavelength and more than 0.95 at 16 or more.
  L1 errors of the travelling wave (one wavelength, isothermal; Fig. 20)
  converge at **second order** with PLM and PPM; 2D errors are about twice
  the 1D errors.
* *3D, Athena* ([Stone et al. (2008)](/sources/stone-2008.md), §8.6,
  Fig. 33). Oblique wave in a $(3, 3/2, 3/2)$ domain, $N$ up to 64, PPM
  with Colella–Sekora limiters, HLLD. With an adiabatic equation of state
  the L1 errors with PLM and PPM are nearly identical to the 2D ones.
* *3D, Cholla* ([Caddy & Schneider (2024)](/sources/caddy-2024.md),
  §3.1.2, Fig. 3). Domain $3.0\times1.5\times1.5$ with $2N\times N\times N$
  cells, $N = 8$ to 256, periodic; $\rho = 1$, $p = 0.1$, along-wave field
  1, amplitude 0.1, wavelength 1; along-wave velocity 0 (travelling) or $-1$
  (standing). The wave is rotated by two angles whose sines are $2/3$ and
  $1/\sqrt5$, with $\mathbf B$ initialized from a vector potential. VL+CT,
  HLLD, PLM or PPM; one period; error is the L2 norm over variables of the
  per-variable L1 norms. **Second order** for travelling and standing waves.
  "The accuracy improvement of PPM versus PLM seen for the linear waves is
  absent in this non-linear test." The paper mentions compressions driven
  by truncation error (citing Stone et al. 2008), not the parametric
  instability. The CFL number is not stated.
* *3D, gPLUTO, as a scaling workload* ([Rossazza et al. (2026)](/sources/rossazza-2026.md),
  §4.2, eq. 10, Figs. 8–9, Table 5). Unit periodic cube, $\rho = 1$,
  $p = 0.1$, $\gamma = 5/3$; a rotated 1D configuration whose eq. 10
  prints the field as a unit $x$ component plus $y$ and $z$ components of
  amplitude 0.1 in quadrature, with phase $2\pi$ times the sum of the
  coordinates divided by the domain lengths (the velocity line prints the
  $y$ unit vector twice). SSP-RK3, WENOZ, HLLD, FP64; CT for weak
  scaling, [GLM cleaning](/methods/glm-divergence-cleaning.md) for strong
  scaling. Weak-scaling efficiency 0.97 at 256 nodes on Leonardo Booster and
  0.95 on MareNostrum 5. **No error or convergence order is reported**,
  although the paper states that the test has an exact nonlinear solution.
  See [gPLUTO](/software/gpluto.md).

**What it shows.** CT codes converge at second order on this nonlinear
test in 2D and 3D ([Stone et al. (2008)](/sources/stone-2008.md), §8.4,
§8.6; [Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.1.2). In
Cholla's VL+CT, PPM gives no accuracy gain over PLM here, unlike on the
small-amplitude linear waves (§3.1.1–§3.1.2). Its regular, smooth 3D
set-up also makes it a scaling workload
([Rossazza et al. (2026)](/sources/rossazza-2026.md), §4.2).

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §8.4, §8.6.
2. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.1.1–§3.1.2.
3. [Rossazza et al. (2026)](/sources/rossazza-2026.md), §4.2.

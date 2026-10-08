---
type: Benchmark
title: "Isentropic vortex advection (smooth accuracy test)"
description: "A smooth isentropic vortex advected diagonally through a periodic box and back to its start; the standard multi-dimensional convergence test for Euler, with low-density, relativistic and MHD variants."
status: established
aliases: [vortex evolution problem, isentropic vortex, Shu vortex]
tags: [benchmark, euler, accuracy, 2d]
timestamp: 2026-10-08T00:00:00Z
---

# Isentropic vortex advection

**Set-up.** Uniform flow of unit density, velocity and pressure, plus an
isentropic vortex perturbation in velocity and
temperature with no entropy perturbation. It is advected at 45° on a
periodic box and returns to its start after one period
(the set-up of Balsara–Shu and of Pao–Salas, as cited).
* $[-5,5]^2$, vortex strength 5, $t = 10$ (one period), fixed CFL 0.45
  ([Titarev & Toro (2004)](/sources/titarev-2004.md), §5.2); a 3D run
  places the vortex in the $y$–$z$ plane.
* Low-density version: $[0,10]^2$, vortex strength 10.0828, so the minimum
  density and pressure are $7.8\times10^{-15}$ and $1.7\times10^{-20}$
  ([Zhang & Shu (2012)](/sources/zhang-2012.md), Example 5.1).
* The domain and run time are doubled for seventh and ninth order, to
  reduce the effect of small velocity jumps at the periodic boundary
  ([Balsara et al. (2025)](/sources/balsara-2025.md), §VI.a).
  Relativistic and ten-moment analogues are in §§VI.b–c, and an MHD
  vortex in [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §6.2.

**Results.**
* FV-WENO with HLLC or MUSTA, dimension by dimension with two Gauss
  points per face, reaches about fifth order with $r = 3$, despite RK3
  at a fixed Courant number: at this output time the error is
  space-dominated. $r = 4$ is about 10 times more accurate and exceeds
  the fourth order the two-point rule nominally allows. The Rusanov-based
  scheme of Shi, Hu and Shu, with a sixth-order face quadrature, is
  twice less accurate ([Titarev & Toro (2004)](/sources/titarev-2004.md), §5.2).
* FD WENO5 with the [positivity scaling limiter](/methods/positivity-preserving-scaling-limiter.md)
  keeps fifth order at near-vacuum densities
  ([Zhang & Shu (2012)](/sources/zhang-2012.md), Table 5.1).
* AFD-WENO at orders 3, 5, 7, 9 (WENO-AO or multiresolution
  interpolation) meets design accuracy for Euler, RHD and the ten-moment
  model ([Balsara et al. (2025)](/sources/balsara-2025.md), Tables I–III),
  and for MHD with constrained transport
  ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), Table 2).

**Later uses (batch 4).**
* ADER-WENO of second to fourth order with vortex strength 5. For
  fourth order the domain is enlarged to $[-10, 10]^2$ and the run to
  $t = 20$, because the exponential tails at the periodic boundary are
  felt on $[-5, 5]^2$. Third order on $128^2$ matches second order on
  $256^2$ ([Balsara et al. (2009)](/sources/balsara-2009.md), §5.1). A magnetized isodensity vortex is the MHD
  analogue (§5.2).
* Third- and fourth-order ADER-WENO with AMR, $r_{\mathrm{AMR}} = 3$, on $[0, 10]^2$
  ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4, Table 2). ADER-DG with subcell limiting, $K = 2$–$9$,
  never activates the limiter ([Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.2, Table 2). With AMR,
  $K = 2$–$8$, refinement is triggered by a density threshold of 0.75
  ([Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.1, Table 1).
* Energy-stable WENO with SAT boundaries on a bounded domain reaches
  third order (diagonal norm) and fourth order (block norm). It is less
  accurate than the linear target on coarse grids and equal to it once
  the critical regions are resolved ([Fisher et al. (2011)](/sources/fisher-2011.md), §6.3).

# Citations

1. [Titarev & Toro (2004)](/sources/titarev-2004.md), §5.2.
2. [Zhang & Shu (2012)](/sources/zhang-2012.md), Example 5.1.
3. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §VI.
4. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §6.2.
5. [Balsara et al. (2009)](/sources/balsara-2009.md), §§5.1–5.2.
6. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4.
7. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.2.
8. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.1.
9. [Fisher et al. (2011)](/sources/fisher-2011.md), §6.3.

---
type: Benchmark
title: "Isentropic vortex advection (smooth accuracy test)"
description: "A smooth isentropic vortex advected diagonally through a periodic box and back to its start; the standard multi-dimensional convergence test for Euler, with low-density, relativistic and MHD variants."
status: established
aliases: [vortex evolution problem, isentropic vortex, Shu vortex]
tags: [benchmark, euler, accuracy, 2d]
timestamp: 2026-10-13T00:00:00Z
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

**Later uses (batch 5).**
* With boundary data from the exact solution on $(-0.5, 1)^2$, where the
  normal velocity changes sign along the boundary, flux-based ILW keeps
  $L^1$ order near 5 (4.80 on the finest grid; $L^\infty$ 4.11)
  ([Lu et al. (2021)](/sources/lu-2021.md), Example 3.9).
* *A different variant:* a stationary *viscous* vortex with thermally
  perfect multispecies properties, measured by Richardson extrapolation
  rather than against an exact solution. Fourth-order finite volume
  converges at order 3.96–3.99 on the two finest pairs
  ([Owen, Guzik & Gao (2018)](/sources/owen-2018.md), §4.5, Table 3).

**Later uses (batch 6): MHD and relativistic vortices.**
* *The MHD vortex* was introduced at second order on $[-5, 5]^2$, with
  background $(\rho, p, v_x, v_y) = (1, 1, 1, 1)$, $\gamma = 5/3$, and
  velocity and field perturbations of the same Gaussian form, balanced by
  a pressure perturbation (eqs. 6.1–6.5). With $r = 3$ WENO slopes it needs
  a little more than half the zones per direction of $r = 2$ for the same
  error, at $L^1$ order 2.0 ([Balsara (2004)](/sources/balsara-2004.md),
  §6, Tables 1–7). At third and fourth order with divergence-free
  reconstruction it reaches orders 2.99 and 4.41
  ([Balsara (2009b)](/sources/balsara-2009-b.md), §4.1, Table I).
* With GLM finite differences, $L^1(B_x)$ orders reach 2.9 and 4.9 in 2D.
  A new 3D version reaches 4.8–4.9, with divergence below $10^{-8}$ at
  $128^3$. The authors warn that $L^2$ errors sit systematically below
  $L^1$ ones, so comparisons across norms "may be deceitful"
  ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.3).
* Fourth-order finite volume with upwind CT converges at rates above 4.
  An iso-enthalpy relativistic vortex, a new exact equilibrium, does the
  same ([Berta et al. (2024)](/sources/berta-2024.md), §5.2, Table 1).
* *Lorentz-boosted vortices* for relativistic hydrodynamics and MHD,
  boosted at $(0.5, 0.5)$ so that they are contracted on the mesh,
  converge at orders 2.2, 2.9 and 4.4–4.5. The third-order hydro and MHD
  tables are numerically identical, which looks like a duplicated table
  ([Balsara & Kim (2016)](/sources/balsara-2016-b.md), §5, Tables 1–6).
* *A low-pressure vortex* with minimum pressure about $5.3\times10^{-12}$,
  so that the positivity limiter acts, converges at fifth order
  ([Ding & Wu (2024)](/sources/ding-2024.md), Example 4.1, Table 4.1).

**Later uses (batch 7).**
* *A strong, low-density vortex* (strength 9.5 on $[0, 10]^2$, minimum
  density $4.22\times10^{-3}$ and pressure $4.74\times10^{-4}$, $t = 0.1$) tests
  the accuracy of the efficient positivity limiter in DG: orders near
  $K + 1$ for $K = 2$–5 on rectangles and triangles ([Zhang (2017)](/sources/zhang-2017.md),
  Example 4, Tables 2–3).
* Third-order cell averages need more than the centre value: the review
  uses the centre and the four face midpoints ([Balsara (2017)](/sources/balsara-2017-d.md), §VIII.1).

**Later uses (batch 9).**
* *3D version for time integrators.* $[-5, 5]^3$, free-stream Mach
  number 0.5, strength 5, flow at 45°, $t = 10$. Entropy-conservative
  flux-differencing SBP–SAT with relaxation Runge–Kutta reaches $L^2$
  rates 4.21, 5.17 and 6.15 for polynomial degrees 3, 4 and 5, and
  conserves the total entropy to quadruple precision on nonconforming
  grids ([Ranocha et al. (2020)](/sources/ranocha-2020.md), §4.1, Table 1, Fig. 7; [relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md)).
* *For step-size control*, with the axis along $(1, 1, 0)$, Mach 0.5 and
  strength 5: the error is dominated by space (about
  $5.78\times10^{-4}$ for all methods at degree 2), and the step is
  accuracy-limited only for tolerances below about $10^{-6}$
  ([Ranocha et al. (2022)](/sources/ranocha-2022.md), §5.2; [step-size control](/methods/runge-kutta-step-size-control.md)).

**Later uses (batch 11, merged at the 2026-10-13 deep lint).**
* *ADER–WENO with a multidimensional HLLI solver*, vortex advected at
  45°, $64^2$ to $512^2$ cells: on $[-5, 5]^2$ to $t = 10$ at orders 2
  and 3, and on $[-10, 10]^2$ to $t = 20$ at order 4, because the
  exponential tail of the vortex is felt at the boundary of the smaller
  box. $L^1$ orders on $512^2$ are 2.10, 2.98 and 3.76 ($L^\infty$ 2.12,
  2.97, 4.24). The printed third-order $256^2$ $L^1$ error (1.0361E−6) is
  inconsistent with the printed orders on either side, which imply
  1.0361E−5 ([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §4.1,
  Table 1; [multidimensional Riemann solvers](/methods/multidimensional-riemann-solvers.md)).
* *The MHD vortex* in the same runs: $B_x$ $L^1$ orders 2.00, 2.97 and
  4.11. The third-order $L^\infty$ order falls across refinements (2.69,
  2.60, 2.41) without comment, while the paper says all runs "meet the
  expected order" (§4.2, Table 2).

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
10. [Lu et al. (2021)](/sources/lu-2021.md), Example 3.9.
11. [Owen, Guzik & Gao (2018)](/sources/owen-2018.md), §4.5 (accepted manuscript).
12. [Balsara (2004)](/sources/balsara-2004.md), §6.
13. [Balsara (2009b)](/sources/balsara-2009-b.md), §4.1 (author manuscript).
14. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.3 (arXiv v2).
15. [Berta et al. (2024)](/sources/berta-2024.md), §5.2 (arXiv v4).
16. [Balsara & Kim (2016)](/sources/balsara-2016-b.md), §5.
17. [Ding & Wu (2024)](/sources/ding-2024.md), Example 4.1 (arXiv v1).
18. [Zhang (2017)](/sources/zhang-2017.md), Example 4.
19. [Balsara (2017)](/sources/balsara-2017-d.md), §VIII.1.
20. [Ranocha et al. (2020)](/sources/ranocha-2020.md), §4.1 (arXiv v4).
21. [Ranocha et al. (2022)](/sources/ranocha-2022.md), §5.2.
22. [Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §§4.1–4.2, Tables 1–2.

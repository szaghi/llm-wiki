---
type: Benchmark
title: "Sedov point-blast wave (low-density positivity test)"
description: "A point release of energy into a cold gas of near-zero pressure; the strong shock and the near-vacuum interior make it the standard low-density test for positivity-preserving schemes, in a planar 1D version, a 2D corner (quarter-plane) version and a full-domain centred 2D version, the last also a carbuncle test for Riemann solvers."
status: established
aliases: [Sedov blast, planar Sedov problem, point-blast wave]
tags: [benchmark, euler, positivity, low-density, blast-wave]
timestamp: 2026-10-13T00:00:00Z
---

# Sedov point-blast wave

**Set-up.** Density 1, zero velocity, and a tiny background energy
everywhere, except one cell that carries the point energy. Zhang & Shu
use total energy $10^{-12}$ with $E_0/h$, $E_0 = 3.2\times10^6$, in the
centre cell, $\gamma = 1.4$, $t = 0.001$
([Zhang & Shu (2010)](/sources/zhang-2010.md), §4.2;
[Zhang & Shu (2012)](/sources/zhang-2012.md), Example 5.2). Hu et al. and
Guo et al. use $(\rho, v_x, p) = (1, 0, 4\times10^{-13})$ with
$p = 2.56\times10^{8}$ in the centre cell on $[0, 4]$, $h = 0.005$,
$t = 0.001$ ([Hu, Adams & Shu (2013)](/sources/hu-2013.md), §3.1;
[Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 9). The 2D
version puts the energy in the lower-left corner cell of a square with
reflecting (symmetry) left and bottom boundaries; the exact solution is
self-similar (Sedov; Korobeinikov).

**Results.**
* Third-order RKDG with the [scaling limiter](/methods/positivity-preserving-scaling-limiter.md)
  and a TVB limiter captures the shock in 1D ($N = 800$) and 2D
  ($160^2$, $t = 1$). Without the TVB limiter it blows up even with the
  positivity limiter ([Zhang & Shu (2010)](/sources/zhang-2010.md), §4.2).
* FD WENO5 with the limiter ($h = 1/200$ in 1D; $h = 1.1/320$ in 2D)
  matches the DG results ([Zhang & Shu (2012)](/sources/zhang-2012.md), Examples 5.2–5.3).
* The [cut-off flux limiter](/methods/positivity-preserving-flux-limiter.md)
  with WENO5 gives a slightly sharper blast than Zhang–Shu, attributed
  to Zhang–Shu's single global signal speed in the Lax–Friedrichs flux
  ([Hu, Adams & Shu (2013)](/sources/hu-2013.md), §§3.1–3.2).
* The positivity-preserving [compact-reconstruction WENO](/methods/compact-reconstruction-weno.md)
  with HLLC is also slightly sharper than Zhang–Shu; minimum density and
  internal energy $4.7\times10^{-3}$ and $10^{-12}$
  ([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 9).

**Later uses (batch 7).**
* *DG with only the positivity limiter.* On $160^2$ over $[0, 1.1]^2$ with
  background pressure $10^{-5}$ and corner-cell energy $0.244816/h^2$, Euler
  and Navier–Stokes ($\mathrm{Re} = 200$) DG of degree 2–4 run to completion
  with no TVB or WENO limiter ([Zhang (2017)](/sources/zhang-2017.md), Example 6). *Compiler's
  note, flagged for human review:* this sits uneasily with the statement
  above that RKDG "blows up" without the TVB limiter even with the
  positivity limiter. The set-ups differ (background state, a step rule
  with $\max\{\cdot, 2h^2\}$ and restarts), so the two may not be
  comparable, and neither paper addresses the other.

**Later uses (batch 11, merged at the 2026-10-13 deep lint).** *A
third variant: the full-domain centred blast as a carbuncle test.* On
$[-1.1, 1.1]^2$ with $160^2$ cells, $(\rho, v_x, v_y, p) = (1, 0, 0, 10^{-6})$,
and the energy $0.244816$ deposited as pressure in "the central cell" (as
printed; with an even cell count no single cell contains the origin), to
$t = 1$ when the shock reaches radius 1. At second order (MUSCL), HLLC
shows carbuncle-type oscillations of the shock front along the $x$- and
$y$-axes, where the front is aligned with the grid, and the largest
radial density error; HLL and HLL-BVD keep a stable front
([Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §III G, eq. 26,
Figs. 12–13; [numerical shock instability](/definitions/numerical-shock-instability.md)).
Unlike the positivity uses above, this one tests the Riemann solver at a
strong shock in all orientations to the grid.

## Contradictions

* **Does positivity-limited DG survive the Sedov problem without a TVB or
  WENO limiter?** *Open* (recorded at the batch-8 deep lint, from the
  compiler's note above; evidence added at the 2026-10-13 deep lint).
  * *Against:* "The DG scheme without the TVB limiter will produce
    blow-ups for the Sedov blast waves even if we use the positivity
    limiter", stated in general for the problem, not for one run
    ([Zhang & Shu (2010)](/sources/zhang-2010.md), §4.2). Their 2D run
    puts total energy $10^{-12}$ in the background and $0.244816/h^2$ in
    the corner cell, $160^2$ cells on a square of side 1.1, $t = 1$.
  * *For:* DG of degree 2–4 with the positivity limiter alone runs to
    completion for Euler and for Navier–Stokes ($\mathrm{Re} = 200$) on
    the same domain, mesh and corner energy, but with background pressure
    $10^{-5}$ and a time step floored at $2h^2$ (to avoid the "artificial
    stiffness" of near-vacuum sound speeds), with a restart whenever a cell
    average leaves the admissible set
    ([Zhang (2017)](/sources/zhang-2017.md), Example 6, Fig. 8).
  * *Scope.* The two runs differ in the background state and the
    step rule, and neither paper tests the other's set-up, so they are not
    shown to be compatible; the entry stays open. Zhang (2017) itself
    reports that Euler RKDG with only the positivity limiter "may produce
    excessive oscillations affecting the shock locations" on finer meshes
    or higher degree in a shock-diffraction problem (§1.7), which bears on
    the "against" side for Euler without deciding it.

# Citations

1. [Zhang & Shu (2010)](/sources/zhang-2010.md), §4.2.
2. [Zhang & Shu (2012)](/sources/zhang-2012.md), Examples 5.2–5.3.
3. [Hu, Adams & Shu (2013)](/sources/hu-2013.md), §§3.1–3.2.
4. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 9.
5. [Zhang (2017)](/sources/zhang-2017.md), Example 6.
6. [Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §III G, Figs. 12–13.

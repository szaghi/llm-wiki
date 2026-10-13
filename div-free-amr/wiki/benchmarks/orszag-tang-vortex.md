---
type: Benchmark
title: "Orszag–Tang vortex"
description: "Compressible 2D MHD vortex on a periodic box that steepens into interacting shocks; the standard robustness test of divergence control, where uncontrolled high-order schemes lose pressure positivity."
status: established
aliases: [Orszag-Tang, OT vortex]
tags: [benchmark, divergence-constraint, mhd, positivity]
timestamp: 2026-10-13T00:00:00Z
---

# Orszag–Tang vortex

A smooth, doubly periodic velocity and magnetic field whose field has
twice the velocity's wavenumber in one direction. The flow steepens into
shocks that cross and interact, and the field reconnects into current
sheets and islands. There is no exact solution: the test is judged by
comparison with other codes, by robustness (no negative pressure, no
blow-up) and, in some papers, by the visible monopole damage of schemes
without divergence control.

## Set-up

The compressible form used in this bundle's sources has plasma
$\beta = 10/3$, sonic Mach number 1 and $\gamma = 5/3$. Two scalings are
in use.

* **Unit wavenumbers** ([Zachary, Malagoli & Colella (1994)](/sources/zachary-malagoli-colella-1994.md) §3.2.2):
  $\mathbf u = -\sin y\,\hat{\mathbf x} + \sin x\,\hat{\mathbf y}$,
  $\mathbf B = -\sin y\,\hat{\mathbf x} + \sin 2x\,\hat{\mathbf y}$
  (Gaussian units), uniform density and pressure, periodic, $192^2$
  cells, after Dahlburg & Picone.
* **On the unit box** ([Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md) §3.4):
  $\mathbf u = -\sin(2\pi y)\,\hat{\mathbf x} + \sin(2\pi x)\,\hat{\mathbf y}$,
  $\mathbf B = B_0[-\sin(2\pi y)\,\hat{\mathbf x} + \sin(4\pi x)\,\hat{\mathbf y}]$
  with $B_0 = 1/\sqrt{4\pi}$ (units absorbing $4\pi$), density
  $25/(36\pi)$ and pressure $5/(12\pi)$ (caption, read as such), $256^2$
  cells, shown at $t = 0.48$.
  [Ryu et al. (1998)](/sources/ryu-1998.md) §3.2 repeat it unchanged.
  Both papers print the Mach-number definition without the square on the
  velocity.

* **Dai & Woodward's form, as printed:** [Dai & Woodward (1998, JCP)](/sources/dai-woodward-1998.md) §4.2 (Figs.
14–15) and [Dai & Woodward (1998, ApJ)](/sources/dai-woodward-1998-b.md) §3
(Figs. 6–7): velocity $(-\sin 2\pi y, \sin 2\pi x)$, field
$(-\sin 2\pi y, \sin 4\pi x)$, uniform density and pressure,
$\beta_0 = 8\pi p_0 = 10/3$, $M_0 = \rho_0/(\gamma p_0) = 1$ (Gaussian
units), unit periodic box, $128^2$–$512^2$, density and field lines at
$t = 0.5$; qualitative only. The face divergence is stated exact; the net
cell flux of the cell-centred field is one order lower than without the
CT update for Orszag–Tang among other problems (ApJ §4).

*Compiler reading:* the forms have the same dimensionless parameters.
Their times are in different units, so failure times quoted below are
comparable only within one paper.

## What it tests

**Second order, one code: projection made no visible difference.**
Zachary et al. hold the divergence only to truncation error, with an
optional collocated central projection. On this test, run for 300 steps
("approximately 2 Alfven transit times"), they "did not find any
noticeable difference regardless of whether or not we applied a
projection" (§2.4). No divergence value is reported, and the paper does not
say which run its figure shows. Their base scheme is a Strang-split
Godunov scheme on a nonconservative momentum form
([eight-wave](/methods/eight-wave.md), Brackbill–Barnes lineage). Ryu,
Jones & Frank (projected every step) and Ryu et al. (1998)
([CT](/methods/flux-ct.md)) compare structures with earlier runs
visually and report no divergence either.

**High order, uncontrolled: loss of positivity.**
* Fifth-order FD-WENO without correction loses pressure positivity and
  blows up on $192^2$, at $t \approx 3.9$ with Powell's $8\times8$
  eigensystem and $t \approx 2.5$ with the $7\times7$ one. With a Poisson
  [projection](/methods/projection-method.md) both run to $t = 8$
  ([Jiang & Wu (1999)](/sources/jiang-1999.md) §3.4).
* Fifth-order FD-WENO goes negative near $t = 4$ without CT; with
  potential-based CT it runs to $t = 30$
  ([Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md)).
* Its single-step successor crashes at $t = 1.67$ without CT
  ([Christlieb, Feng, Seal & Tang (2016)](/sources/christlieb-2016.md)).
* Fifth-order FV-WENO without the trace projection and the limiter breaks
  down at $t = 3.11$; with the projection the monitored cell-local
  condition stays near $10^{-13}$
  ([Ding & Wu (2024)](/sources/ding-2024.md);
  [divergence-free reconstruction](/methods/divergence-free-reconstruction.md)).
* The coupling behind these failures is recorded at
  [positivity–divergence coupling](/results/positivity-divergence-coupling.md).

**A qualification, not a contradiction.** Zachary et al.'s "no noticeable
difference" and Jiang & Wu's "projection needed" are about different
schemes (second-order split Godunov on a nonconservative form against
fifth-order WENO on the conservative form) and different time windows:
about two Alfvén transit times against failures at $t \approx 2.5$–$3.9$
in Jiang & Wu's units, with corrected runs to $t = 8$. Neither paper
measures a divergence on this test. *Compiler reading:* the claims do not
meet; a same-scheme run past two transit times with and without the
projection would decide whether Zachary et al.'s observation persists.

**Monopole damage and EMF dissipation.**
* Collocated base schemes show "structured filaments", while their
  [UCT](/methods/upwind-constrained-transport.md) counterparts do not
  ([Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md)).
* Run to $t = 2\pi$: with a third-order Roe base scheme, arithmetic EMF
  averaging and CT-Flux fail outright; UCT-HLL resolves the central island
  only at the higher resolution
  ([Mignone & Del Zanna (2021)](/sources/mignone-2021.md);
  [flux-CT](/methods/flux-ct.md)).
* With GLM cleaning the divergence error peaks at the discontinuities
  ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md)).
* EGLM's nonconservative sources move the total energy by
  $3.0$–$4.4\cdot10^{-4}$ ([Zaghi (2026)](/sources/zaghi-2026.md),
  hypothesis; [GLM](/methods/glm-divergence-cleaning.md)).

**Robustness runs.** The test is part of the suites of
[Balsara & Spicer (1999)](/sources/balsara-spicer-1999.md) (run,
"comparable" to cleaned runs, not shown),
[Stone, Gardiner, Teuben, Hawley & Simon (2008)](/sources/stone-2008.md),
[Felker & Stone (2018)](/sources/felker-2018.md) (robust at $500^2$),
[Berta, Mignone, Bugli & Mattia (2024)](/sources/berta-2024.md) (MHD and relativistic MHD)
and the face-based scheme summarized in
[Zampa (2024)](/sources/zampa-2024.md).

# Citations

1. [Zachary, Malagoli & Colella (1994)](/sources/zachary-malagoli-colella-1994.md), §§2.4, 3.2.2, Fig. 9.
2. [Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md), §3.4, eqs. 3.20–3.23, Fig. 8 caption.
3. [Ryu, Miniati, Jones & Frank (1998)](/sources/ryu-1998.md), §3.2, Fig. 3.
4. [Jiang & Wu (1999)](/sources/jiang-1999.md), §3.4.
5. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §7.
6. [Christlieb, Feng, Seal & Tang (2016)](/sources/christlieb-2016.md), §6.
7. [Ding & Wu (2024)](/sources/ding-2024.md), §4.
8. [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md), §4.
9. [Mignone & Del Zanna (2021)](/sources/mignone-2021.md), §§6.1–6.6.
10. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md), §§4.2–4.4.
11. [Zaghi (2026)](/sources/zaghi-2026.md): FLUME verification record.
12. [Balsara & Spicer (1999)](/sources/balsara-spicer-1999.md), §3.1.
13. [Stone, Gardiner, Teuben, Hawley & Simon (2008)](/sources/stone-2008.md), §8.
14. [Felker & Stone (2018)](/sources/felker-2018.md), §5.
15. [Berta, Mignone, Bugli & Mattia (2024)](/sources/berta-2024.md), §§5.4–5.8.
16. [Zampa (2024)](/sources/zampa-2024.md), Chapter 4 (claim level).
17. [Dai & Woodward (1998, JCP)](/sources/dai-woodward-1998.md), §4.2, Figs. 14–15.
18. [Dai & Woodward (1998, ApJ)](/sources/dai-woodward-1998-b.md), §§3–4, Figs. 6–7.

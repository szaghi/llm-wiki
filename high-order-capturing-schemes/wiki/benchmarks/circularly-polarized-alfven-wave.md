---
type: Benchmark
title: "Circularly polarized (torsional) Alfvén waves"
description: "An exact nonlinear MHD wave, oblique to the mesh: run for a few periods it measures the convergence order of a multi-D MHD scheme and its divergence control; run for many crossings at a small angle to the mesh, its decaying amplitude measures numerical dissipation."
status: established
aliases: [circularly polarized Alfvén wave, torsional Alfvén wave, smooth Alfvén wave, Alfvén-wave decay]
tags: [benchmark, mhd, accuracy, dissipation, 2d, 3d]
timestamp: 2026-10-09T00:00:00Z
---

# Circularly polarized (torsional) Alfvén waves

**The wave.** With uniform density and pressure and a uniform guide
field, a transverse velocity and field of equal amplitude and opposite
sign, rotating in phase along the propagation direction, is an exact
nonlinear solution of ideal MHD. Rotating the propagation direction off
the grid axes makes it a multidimensional test. Two uses appear.

## Convergence

* **1D and oblique 3D** ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.1).
  In 1D on 16–256 points, the four finite-difference schemes reach exactly
  3.00 (WENO+3, LimO3) and 5.00 (WENO-Z, MP5); 64 points at fifth order
  match 256 at third. In 3D, rotated by $\tan^{-1}2$ in a
  $[0,1]\times[0,\tfrac12]^2$ box to $t = 1/3$, the orders hold and errors
  are about 4 times the 1D ones. All beat a second-order CT-PPM scheme.
* **Rotated along the cube diagonal**, with $p = 1000$, amplitude 0.02 and
  one crossing: the RK-WENO divergence-free scheme reaches orders 2.48,
  2.94 and 4.48 ([Balsara (2009b)](/sources/balsara-2009-b.md), §4.2,
  Table II). Fourth order on $16^3$ beats second order on $48^3$
  ([Balsara et al. (2009)](/sources/balsara-2009.md), §5).
* **2D and 3D smooth Alfvén waves** (Helzel et al.'s set-up): unstaggered
  CT FD-WENO converges at fourth order, $L^2$ orders 4.01–4.46 in 2D and
  4.34–4.42 in 3D, limited by the curl and SSP-RK4
  ([Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md),
  §7.1, Tables 1–4); also fourth order in space and third in time in the
  single-step sequel ([Christlieb et al. (2016)](/sources/christlieb-2016.md), §6).
* **The role of CT.** With the original second-order CT, a WENO5 code
  converges at second order. With fourth- or sixth-order staggered CT it
  converges at fifth (3D, $N = 16$–256, $t = 5$;
  [Seo & Ryu (2023)](/sources/seo-2023.md), §3.2;
  [constrained transport](/methods/constrained-transport.md)).
* **Fourth-order FV with CT**, rotated 45° (2D) and 45° plus 45° (3D): all
  orders converge to 4.00, with smaller errors than fifth-order FD below
  $256^3$ ([Berta et al. (2024)](/sources/berta-2024.md), §5.3, Table 2).

## Long-term decay

At a small angle to the mesh ($\tan^{-1}(1/6) = 9.462°$, $120^2$ zones),
the wave crosses the domain many times, and the decay of $\max|v_z|$ and
$\max|B_z|$ measures numerical dissipation.
* At second order, a dimensionally swept scheme is the most dissipative,
  then an unsplit TVD scheme, then $r = 2$ and $r = 3$ WENO slopes, with
  HLLE almost as good as Roe ([Balsara (2004)](/sources/balsara-2004.md),
  §7.1, to $t = 129$).
* The decay falls sharply with order whatever the Riemann solver, and the
  linearized solver's advantage over HLL shrinks with order
  ([Balsara (2009b)](/sources/balsara-2009-b.md), §5.1;
  [Balsara et al. (2009)](/sources/balsara-2009.md), §7.2;
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)).
* After about 100 crossings ($\tan\alpha = 6$, $120\times20$ cells,
  $t = 16.5$), about 94% of the amplitude remains at fifth order, 20% at
  third and 3% for second-order TVD with the MC limiter
  ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.1.3).
* A relativistic MHD version to $t = 130$ shows decay "almost
  imperceptible" at fourth order ([Balsara & Kim (2016)](/sources/balsara-2016-b.md), §6.5).
* Measured as a decay rate, fourth-order dissipation is more than an order
  of magnitude below second order already at 8 cells, and scales as about
  $N^{-5}$ against $N^{-3}$ ([Berta et al. (2024)](/sources/berta-2024.md), §5.3).

**A tension on instability.** Torsional waves are parametrically
unstable. One paper runs at very high plasma beta, stating that this
suppresses the instability ([Balsara et al. (2009)](/sources/balsara-2009.md), §5.3).
Its RK sibling, with the same $p = 1000$, says the instabilities exist
also at high beta and that the set-up is designed to ameliorate them
([Balsara (2009b)](/sources/balsara-2009-b.md), §4.2). Neither reports
an instability in its runs.

**Later uses (batch 7).**
* *Second-order convergence of four schemes* in 2D ($\tan\alpha = 2$) and 3D:
  at $N_x = 256$ and Courant number 0.8 in 2D, GLM $8.48\times10^{-5}$, CT
  $6.73\times10^{-5}$, eight-wave $7.29\times10^{-5}$, all about second order
  ([Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md), §4.1, Table 1).
* *A thermal-energy diagnostic at very low β* ($p_0 = 10^{-4}$, plasma beta
  $1.98\times10^{-4}$, $256\times128$, five periods): CT and GLM make errors
  of about 30% of both signs, EGLM a nearly uniform slow increase
  ([Tomida et al. (2026)](/sources/tomida-2026.md), App. B.3).
* *Long-term decay, quantified.* An incomplete solver dissipates about 6
  times more than a complete one at second order, 3 times at third, and
  almost no more at fourth; second order with the complete solver beats
  third order with the incomplete one ([Balsara (2017)](/sources/balsara-2017-d.md), §§IX.5, IX.8).

# Citations

1. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.1 (arXiv v2).
2. [Balsara (2009b)](/sources/balsara-2009-b.md), §§4.2, 5.1 (author manuscript).
3. [Balsara et al. (2009)](/sources/balsara-2009.md), §§5, 7.2.
4. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §7.1 (arXiv v2).
5. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.
6. [Seo & Ryu (2023)](/sources/seo-2023.md), §3.2.
7. [Berta et al. (2024)](/sources/berta-2024.md), §5.3 (arXiv v4).
8. [Balsara (2004)](/sources/balsara-2004.md), §7.1.
9. [Balsara & Kim (2016)](/sources/balsara-2016-b.md), §6.5.
10. [Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md), §4.1.
11. [Tomida et al. (2026)](/sources/tomida-2026.md), App. B.3.
12. [Balsara (2017)](/sources/balsara-2017-d.md), §§IX.5, IX.8.

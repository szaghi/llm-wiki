---
type: Benchmark
title: "Linear wave convergence test"
description: "A small-amplitude eigenmode of the (magneto)hydrodynamic or radiation equations is propagated on a periodic grid, often oblique to it, most commonly for one period with the L1 error against the initial state measuring the order of accuracy of each wave family; radiation and damped-wave variants compare against dispersion relations or decay rates instead."
status: established
aliases: [linear wave test, linear wave convergence, oblique linear wave]
tags: [benchmark, verification, mhd, hydro, radiation, amr]
timestamp: 2026-10-12T00:00:00Z
---

# Linear wave convergence test

**Set-up.** A single eigenmode (sound, shear, entropy; or fast, Alfvén,
slow and entropy in MHD) of amplitude $10^{-6}$ relative to a uniform
background is laid on a periodic domain and propagated for one period.
The exact solution then equals the initial state, so the L1 norm of the
difference between the final and initial cell values, per variable,
measures the error with no reference solution. In multi-dimensional
versions the wavevector is oblique to the grid (Gardiner–Stone geometry),
so that no grid direction is favoured. The amplitude is tiny so that the
wave stays linear; [Stone et al. (2008)](/sources/stone-2008.md), §8.1,
report that double precision and the tiny amplitude are both needed to
see convergence out to 1024 cells, reading this as round-off able to
dominate truncation error.

**Runs.**

* *1D hydro* ([Stone et al. (2008)](/sources/stone-2008.md), §8.1, Fig. 7).
  Sound, two shear and entropy waves; $\rho = 1$, $p = 3/5$,
  $\gamma = 5/3$, domain length 1. Sound waves start from rest, the others
  with background $v_x = 1$. Run to $t = 1$, up to 1024 zones, PPM. HLLC
  and Roe errors are nearly identical and second order; HLLE errors are
  slightly larger, with a slightly lower rate. Errors are dominated by
  diffusion; dispersion is nearly absent at 16 or more points per
  wavelength. Suggested code checks: L1 errors identical to every digit for
  left- and right-moving waves, and a standing-wave variant with
  background $v_x = -c_s$.
* *1D MHD* ([Stone et al. (2008)](/sources/stone-2008.md), §8.2, Fig. 12).
  $\rho = 1$, $p = 3/5$, $\mathbf B = (1, \sqrt2, 1/2)$, $\gamma = 5/3$,
  giving $c_f = 2$, an Alfvén speed along $x$ of 1 and a slow speed of
  1/2; up to 1024 zones, PPM. Roe and HLLD are nearly identical and second
  order, slightly lower than HLLE.
* *3D MHD, oblique* ([Stone et al. (2008)](/sources/stone-2008.md), §8.6,
  Fig. 32). Domain $(3, 3/2, 3/2)$, grid $2N\times N\times N$ with
  $N = 4, 8, 16, 32, 64, 128$, wavevector not along a cell diagonal;
  HLLD, PLM and PPM. Second order in all wave families; fast-wave errors
  are about twice the 1D errors, the other families comparable to 1D.
* *3D MHD, integrator comparison* ([Stone et al. (2020)](/sources/stone-2020.md),
  §3.3.1, Fig. 11). Domain $(3.0, 1.5, 1.5)$, grid $2N\times N\times N$,
  $N = 16$–256, wavelength 1, wave along the grid diagonal, HLLD; error is
  the rms over variables of volume-weighted L1 norms (eq. 21). Strictly
  second order whenever VL2 or PLM is used. RK3+PPM errors are at least
  10 times lower than VL2+PLM, and for some families convergence is near
  third order (the entropy-wave panel approaches a fourth-order guide
  line); the authors attribute this to temporal errors dominating, since
  there is no formal third-order spatial accuracy in multi-D. The CFL
  number is not printed.
* *3D MHD, with AMR* ([Stone et al. (2020)](/sources/stone-2020.md),
  §3.4.1, Fig. 19). As above, with one finer level wherever the density
  is within 90% of its peak; blocks from $4^3$ to $64^3$; VL2 with PLM and
  PPM. Globally second order with [AMR](/methods/adaptive-mesh-refinement.md);
  the AMR error is slightly below that of the unrefined root grid; at the
  largest resolution the second-order prolongation and restriction errors
  dominate PPM; the $L_\infty$ error is sensitive to faulty boundary
  communication; AMR overhead is about 20%. The text calls this test
  "identical to that already presented in Section 3.3.2", which is the
  non-ideal test; the ideal one is §3.3.1.
* *3D MHD on a GPU AMR code, uniform grids* ([Zhang et al. (2018)](/sources/zhang-2018.md),
  §5.1(i), Fig. 4). Slow, Alfvén and fast waves along the 3D box diagonal,
  relative amplitude $1.0\times10^{-6}$, one period, uniform grids, CTU
  with PLM, Roe, double precision, $\gamma = 5/3$, Courant factor 1/2;
  error is the mean absolute deviation over primitive variables. All
  errors scale as $N^{-2}$. Grid sizes and error values appear only on
  the log plot (N from about $10^1$ to $10^3$).
* *Damped (non-ideal) fast wave* ([Stone et al. (2020)](/sources/stone-2020.md),
  §3.3.2, Figs. 12–13). 2D, domain $(2/\sqrt5)\times(1/\sqrt5)$,
  wavelength 1 at $\tan^{-1}2 \approx 63.43^\circ$, amplitude $10^{-4}$,
  CFL 0.4, $c_f = 2$, $t = 0.75$; viscosity $10^{-2}$ to $10^{-4}$ with
  Prandtl and magnetic Prandtl numbers 1/2. The measured decay rate
  converges to the analytic rate of Ryu et al. (1995) for Reynolds numbers
  134, 269, 2690 and 13,452; the decay-rate error converges at second
  order at Re = 13,452, much faster with RK3+PPM, with a floor below about
  $10^{-4}$ from the ideal-MHD initial data.
* *Radiation-only wave* ([Skinner & Ostriker (2013)](/sources/skinner-2013.md),
  §4.1.2, Fig. 4). A free-streaming, absorbing radiation wave in 1D, 2D
  ($2L\times L$, inclined at $\tan^{-1}2 \approx 63.4^\circ$) and 3D
  (inclined at $\tan^{-1}(2/\sqrt5) \approx 41.8^\circ$), after Gardiner
  & Stone; amplitude $10^{-6}$, optical depth per wavelength
  $\tau_\lambda = 0.1$, periodic, one period, $\hat c = c$. The paper
  reports "nearly second-order" convergence in 1D, 2D and 3D against a
  slope −2 guide line; no rate or error table is printed. The source step
  is exact here, so there is no splitting error.
* *Radiation-hydrodynamic waves* ([Skinner & Ostriker (2013)](/sources/skinner-2013.md),
  §4.3.4, Figs. 17–20). A different use of the linear wave: a 1D standing
  wave, $N = 512$, $\gamma = 5/3$, amplitude $10^{-6}$, ten periods, over
  a range of radiation-to-gas pressure ratios and $\tau_\lambda = 10^{-2}$
  to $10^2$. Phase speed and damping rate match the roots of the linear
  dispersion relation (eq. 93), and match the full-$c$ solution provided
  the reduced speed of light, in the paper's dimensionless units, is at
  least about $\tau_\lambda$; see [reduced speed of light](/definitions/reduced-speed-of-light.md).
  There is some discrepancy for the smallest damping rates (about
  $10^{-4}$). No convergence order is measured.

The self-gravitating analogue, with a Jeans dispersion relation, is the
[Jeans wave](/benchmarks/jeans-wave.md) test.

**What it shows.** The second-order MHD codes measured here converge at
second order in all wave families, including on grids oblique in 3D
([Stone et al. (2008)](/sources/stone-2008.md), §8.6;
[Zhang et al. (2018)](/sources/zhang-2018.md), §5.1(i)); with
higher-order options the test separates integrators and reconstructions
mainly by error constant ([Stone et al. (2020)](/sources/stone-2020.md),
§3.3.1), and it probes [AMR](/methods/adaptive-mesh-refinement.md) boundary communication
through $L_\infty$ (§3.4.1).

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §8.1, §8.2, §8.6.
2. [Stone et al. (2020)](/sources/stone-2020.md), §3.3.1, §3.3.2, §3.4.1.
3. [Zhang et al. (2018)](/sources/zhang-2018.md), §5.1(i) (arXiv v4).
4. [Skinner & Ostriker (2013)](/sources/skinner-2013.md), §4.1.2, §4.3.4 (arXiv v1).

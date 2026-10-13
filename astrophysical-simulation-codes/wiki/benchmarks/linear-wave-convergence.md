---
type: Benchmark
title: "Linear wave convergence test"
description: "A small-amplitude eigenmode of the (magneto)hydrodynamic or radiation equations is propagated on a periodic grid, often oblique to it, most commonly for one period with the L1 error against the initial state measuring the order of accuracy of each wave family; radiation and damped-wave variants compare against dispersion relations or decay rates instead."
status: established
aliases: [linear wave test, linear wave convergence, oblique linear wave]
tags: [benchmark, verification, mhd, hydro, radiation, amr]
timestamp: 2026-10-13T00:00:00Z
---

# Linear wave convergence test

**Set-up.** A single eigenmode (sound, shear, entropy; or fast, Alfvén,
slow and entropy in MHD) of amplitude $10^{-6}$ relative to a uniform
background is laid on a periodic domain and propagated for one period.
The exact solution then equals the initial state, so the $L_1$ norm of the
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
  wavelength. Suggested code checks: $L_1$ errors identical to every digit for
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
  the rms over variables of volume-weighted $L_1$ norms (eq. 21). Strictly
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

## Later uses (batch 3)

* *1D hydro and MHD with fourth-order reconstructions*
  ([Stone et al. (2026)](/sources/stone-2026.md), §3.1–§3.2, Figs. 1 and 3;
  [AthenaK](/software/athenak.md), one CPU core). Exact eigenmode after
  Stone et al. (2020), one period, $N$ from about 8 to about 1000 (read
  from the plot axis); RK2+PLM, RK3+PPM4, RK3+PPMX and RK3+WENOZ, all
  reconstructing primitive variables; amplitude and CFL number not
  printed. Hydro (sound and entropy waves): fourth order for the
  extremum-preserving PPMX and WENOZ "until either non-linear effects or
  round-off error becomes important", second order for PPM4 and PLM; the
  errors bottom out near $10^{-11}$–$10^{-12}$ at $N \approx 128$ (plot).
  MHD: fourth order for RK3+PPMX and RK3+WENOZ on the slow and Alfvén
  waves, but "the fast wave only converges at second-order even in
  one-dimension"; PPM4 and PLM are second order for all waves. The paper
  does not explain the fast-wave order loss. No error values are printed.
* *3D MHD, oblique, solver and reconstruction comparison*
  ([Lesur et al. (2023)](/sources/lesur-2023.md), §4.2, eq. 14, Figs. 7–8;
  [IDEFIX](/software/idefix.md)). The Gardiner–Stone geometry of Stone et
  al. (2008): domain $(3.0, 1.5, 1.5)$, grid $2N\times N\times N$,
  periodic; $\rho = 1$, $p = 1/\gamma = 3/5$; in the frame of the
  wavevector a field of 1 along it and 3/2 across it, and a background
  velocity of 1 along it for the entropy mode only (fast, Alfvén and slow
  speeds 2, 1 and 0.5); amplitude $10^{-6}$; one domain-crossing time.
  The error (eq. 14) is the square root of the sum over variables of the
  squared $L_1$ errors, each normalized by the amplitude and the number of
  cells and components. With PLM+RK2, the Rusanov (Lax–Friedrichs), HLL,
  HLLD and Roe solvers all converge at second order (Fig. 7). With HLLD
  (Fig. 8), LimO3+RK3 and PPM+RK3 are less diffusive than PLM+RK2,
  notably for the entropy mode, but PPM "stops converging" at high
  resolution, worst for the slow mode; the same stall appears with HLL
  and in an [Athena++](/software/athena-plus-plus.md) PPM run with primitive-variable reconstruction
  (dashed curve); the stalled PPM curves rise back to about $10^{-2}$ at
  the finest grid. The authors recommend LimO3. Recorded as printed: the
  text says LimO3
  "shows proper second order convergence", the Fig. 8 caption "slightly
  larger than second order".
* *3D MHD, grid-aligned* ([Caddy & Schneider (2024)](/sources/caddy-2024.md),
  §3.1.1, eqs. 33–35, Fig. 2; [Cholla](/software/cholla.md)). Periodic
  unit cube, $N\times16\times16$ cells with $N = 16$ to 512 in powers of
  2, the wave along $x$ (not oblique), wavelength 1, amplitude $10^{-6}$,
  $\gamma = 5/3$; $\rho = 1$, $\mathbf v = 0$ (background $v_x = 1$ for
  the contact wave), $p = 1/\gamma$, $\mathbf B = (1, 1.5, 0)$;
  eigenvectors of Gardiner & Stone (2008); one period; VL+CT with HLLD.
  The error is the $L_2$ norm over variables of the per-variable $L_1$ norms.
  Slow, fast, Alfvén and entropy waves all converge at second order. PPM
  with characteristic limiting is "approximately an order of magnitude"
  more accurate than PLM with characteristic limiting at every
  resolution, still at second order (PPM is "formally second order"
  inside this integrator, §2.2.6), and "comparable to" Stone & Gardiner
  (2009). Runs along all three axes and in both directions give
  "identical results". The CFL number is not stated.
* *1D hydro sound wave on a GPU AMR code*
  ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3.1.1, eq. 45,
  Fig. 1; [Quokka](/software/quokka.md)). After Stone et al. (2008):
  $\rho = 1$, $\mathbf v = 0$, $p = 1/\gamma$, $\gamma = 5/3$, amplitude
  $10^{-6}$, periodic $[0, 1]$, one period, PPM, CFL 0.1, $N = 16$ to
  1024. The error, the rms over components of the $L_1$ error (eq. 45), is
  $1.0\times10^{-7}$ at $N = 16$, $1.6\times10^{-9}$ at $N = 128$ and
  $1.7\times10^{-11}$ at $N = 1024$, scaling as $N^{-2}$ (Fig. 1), in
  "excellent agreement" with [Athena](/software/athena.md) (Stone et al. 2008, Fig. 7). Recorded
  as printed: the eigenvector $(1, -1, 1, 1, 1.5)$ has nonzero transverse
  velocity components, unusual for a pure sound wave from rest.
* *Radiation-modified wave, discrete-angle transport*
  ([Stone et al. (2026)](/sources/stone-2026.md), §3.7, Fig. 15). A
  gas-dominated wave in Minkowski spacetime after White et al. (2023),
  with one angle per octant so that the Eddington tensor is exact; RK2+PLM;
  run until the perturbation has decayed by a factor 2. Convergence is
  better than first order (the plot carries an $N^{-2}$ guide line); the
  authors call the expected rate "non-trivial" because the operator-split
  backward-Euler source is first order in time. 1D is shown; 3D inclined
  waves are "confirmed" but not shown. This is specific-intensity
  transport on an angular grid, not the moment method of the
  Skinner & Ostriker runs above.
* *As a performance workload.* A 3D linear wave on a uniform mesh is
  AthenaK's single-device throughput and weak-scaling problem, and a 3D
  sound wave along the mesh diagonal with one refinement level its AMR
  weak-scaling problem ([Stone et al. (2026)](/sources/stone-2026.md),
  §5.1–§5.2, Tables 1–2, Figs. 21–22). Cholla's weak and strong scaling
  use the slow magnetosonic wave of its convergence set-up, $459^3$ cells
  per MI250X GCD for weak scaling, double precision, PLM with
  characteristic limiting ([Caddy & Schneider (2024)](/sources/caddy-2024.md),
  §3.2, Figs. 13–14). The numbers are on
  [cell-update throughput](/definitions/cell-updates-per-second.md) and
  [parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md).

Three further codes (IDEFIX, Cholla, Quokka) find second order in every
family with second-order configurations, and Cholla confirms that PPM
lowers the error constant without raising the order inside a
second-order integrator. Two results qualify the higher-order runs above.
(i) IDEFIX's PPM+RK3 stalls at high resolution, and so does an Athena++
PPM run with primitive reconstruction
([Lesur et al. (2023)](/sources/lesur-2023.md), §4.2); the Stone et al.
(2020) entry above reports RK3+PPM errors at least 10 times below VL2+PLM
and some families near third order for $N \le 256$; see Contradictions. (ii) With fourth-order
reconstructions in 1D, AthenaK reaches fourth order except for the MHD
fast wave, which stays second order
([Stone et al. (2026)](/sources/stone-2026.md), §3.2).

## Later uses (batch 6)

* *2D MHD, oblique: the origin of the Gardiner–Stone geometry*
  ([Gardiner & Stone (2005)](/sources/gardiner-2005.md), §5.4, eqs. 79–81,
  Fig. 11, App. A; arXiv v1). Domain $[0, 2/\sqrt5]\times[0, 1/\sqrt5]$ on
  $2N\times N$ cells, periodic, wavevector at $\tan^{-1}2$; amplitude
  $10^{-6}$; $\rho = 1$, $p = 1/\gamma = 3/5$, $\gamma = 5/3$; field
  $(1, \sqrt2, 1/2)$ in the frame of the wavevector, background velocity 1
  along it for the entropy mode only; slow, Alfvén and fast speeds 1/2, 1
  and 2; right eigenvectors printed (App. A); one wavelength of travel.
  Error: the per-component $L_1$ norm of the final minus initial cell values
  (cell-centred field), combined as the square root of the sum of squares
  (eqs. 80–81). 2D CTU+CT with PPM and the Roe solver: fitted orders **fast
  2.0, Alfvén 2.26, slow 2.29, entropy 2.11**, errors between about
  $10^{-7}$ and $10^{-10}$ for $N$ from about 8 to 128 (plot axes); with PLM
  every mode scales as $N^{-2}$ with a slightly larger error. The 1D MHD
  background of Stone et al. (2008) above and IDEFIX's field of 1 along and
  3/2 across the wavevector ($\sqrt{2 + 1/4} = 3/2$) are this background.
  The 3D geometry above (domain $(3, 3/2, 3/2)$) is not in this paper,
  which is 2D only.
* *Wavelength as printed.* Gardiner & Stone state the wavelength as 2/5
  (read from the rendered page), while their eq. 79 prints the phase as
  $\cos(2\pi x_1)$, i.e. wavelength 1, with $x_1$ along the wavevector. In
  this domain and angle the projections of the domain sides on the
  wavevector are both 2/5, so only wavelengths 2/5, 1/5, … are periodic
  (computed at ingestion): the stated 2/5 is the consistent value, and eq.
  79 omits the division by the wavelength. The damped-wave entry above
  records "wavelength 1 at $\tan^{-1}2$" in the same domain for Stone et
  al. (2020). Stone et al. (2020, §3.3.2) print λ = 1 and k = 2π
  explicitly, so they repeat the original's printed inconsistency; this is
  not a transcription slip (checked on the Stone et al. (2020) PDF at deep
  lint #4). It is recorded here as a printed inconsistency, not a
  contradiction.

The original adds a 2D CTU+CT data point to "What it shows": second order
in all four MHD families in 2D, with PPM changing the error constant and
slightly raising the fitted rates, PLM giving exactly second order.

## Later uses (batch 9)

* *The damping rate attributed to "Ryu et al. (1995)".* The damped fast-wave
  entry above says the measured decay rate of Stone et al. (2020)
  converges to "the analytic rate of Ryu et al. (1995)". That rate is not
  in [Ryu & Jones (1995)](/sources/ryu-1995.md), the bundle's `ryu-1995`:
  that paper is two-author, strictly 1D and ideal (no viscosity or
  resistivity), and its tests are Riemann problems, not damped waves
  (§§2, 4). "Ryu et al." names three or more authors, and the reference
  list of Stone et al. (2020), as merged into the bibliography, holds
  Ryu, Jones & Frank (1995, Astrophys. J. 452:785, `ryu-1995-b`, not
  ingested) and not `ryu-1995`. Which paper derives the rate is not
  settled here; the attribution is recorded as a qualification of the
  entry above, not as a contradiction.

* *3D MHD, both CTU variants* ([Gardiner & Stone (2008)](/sources/gardiner-2008.md), §5.2, eqs. 53–56, Fig. 3, App. A). Amplitude $10^{-6}$; background $\rho = 1$, $p = 3/5$, $\mathbf B = (1, 3/2, 0)$, velocity 1 along the wave for the entropy mode and 0 otherwise (slow, Alfvén, fast speeds 1/2, 1, 2); domain $[0,3]\times[0,1.5]^2$ on $2N\times N\times N$, periodic; rotation sines $2/3$ and $2/\sqrt5$, wavelength 1; one crossing time; per-component $L_1$ errors combined in quadrature. Second order for all four families with the 6- and 12-solve CTU+CT; the 6-solve errors are lower except for the slow wave. This is the primary source of the 3D geometry and background attributed above to "Gardiner & Stone"; App. A prints the eigenvectors.

## Contradictions

* **Does Athena++ RK3+PPM keep converging on 3D linear waves up to
  $N = 256$?** *Open.* [Stone et al. (2020)](/sources/stone-2020.md):
  RK3+PPM errors at least 10 times below VL2+PLM, some wave families near
  third order, for $N$ from 16 to 256 (entry above).
  [Lesur et al. (2023)](/sources/lesur-2023.md), §4.2, Fig. 8: an Athena++
  run with PPM and primitive-variable reconstruction on the oblique 3D
  wave stalls from about $N = 64$–$128$ (128–256 cells along $x_1$) and
  its error rises back to about $10^{-2}$, like IDEFIX's PPM. Same code,
  test family and resolution range. Neither source prints the full
  configuration (Stone et al. not the reconstruction variables, Lesur et
  al. not the Athena++ version or options), so the difference may lie in
  the set-up; the entry closes when a source identifies it.

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §8.1, §8.2, §8.6.
2. [Stone et al. (2020)](/sources/stone-2020.md), §3.3.1, §3.3.2, §3.4.1.
3. [Zhang et al. (2018)](/sources/zhang-2018.md), §5.1(i) (arXiv v4).
4. [Skinner & Ostriker (2013)](/sources/skinner-2013.md), §4.1.2, §4.3.4 (arXiv v1).
5. [Stone et al. (2026)](/sources/stone-2026.md), §3.1, §3.2, §3.7, §5.1, §5.2 (arXiv v1).
6. [Lesur et al. (2023)](/sources/lesur-2023.md), §4.2 (arXiv v1).
7. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.1.1, §3.2 (arXiv v2).
8. [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3.1.1 (arXiv v2).
9. [Gardiner & Stone (2005)](/sources/gardiner-2005.md), §5.4, eqs. 79–81, Fig. 11, App. A (arXiv v1).
10. [Ryu & Jones (1995)](/sources/ryu-1995.md), §§2, 4 (arXiv preprint).
11. [Gardiner & Stone (2008)](/sources/gardiner-2008.md), §5.2, App. A.

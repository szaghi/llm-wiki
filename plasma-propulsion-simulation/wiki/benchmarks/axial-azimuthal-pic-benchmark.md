---
type: Benchmark
title: "Axial–azimuthal Hall-thruster PIC benchmark (Charoy et al. 2019)"
description: "Collisionless 2D axial–azimuthal PIC test case of a Hall-thruster discharge with imposed radial magnetic field and imposed ionization source, reproduced by seven codes in 2019 and later used to test GPU, semi-implicit and reduced-order PIC and kinetic transport theory."
status: established
aliases: [Charoy benchmark, LPPic, LANDMARK axial-azimuthal benchmark, LANDMARK Case 2a, 2D axial-azimuthal benchmark]
tags: [benchmark, verification, pic, hall-thruster, anomalous-transport, instability]
timestamp: 2026-10-14T00:00:00Z
---

# Axial–azimuthal Hall-thruster PIC benchmark (Charoy et al. 2019)

The benchmark of Charoy et al. (2019), part of the LANDMARK
low-temperature magnetized plasma benchmarks (Case 2a), is a fully kinetic
2D test of a Hall-thruster discharge in the axial–azimuthal plane. It
removes the radial direction, walls, neutrals and collisions, so that
[anomalous electron transport](/definitions/anomalous-electron-transport.md)
can arise only from the azimuthal
[electron drift instability](/definitions/electron-drift-instability.md).
The 2019 paper itself is not ingested in this bundle; the set-up below is
as its users restate it.

## Set-up

Planar Cartesian domain, axial $x$ ($\leftrightarrow z$) and azimuthal $y$
($\leftrightarrow\theta$), periodic in $y$, no curvature
([Marks & Gorodetsky (2025)](/sources/marks-2025.md), Methods, Table 1;
[Charoy et al. (2020)](/sources/charoy-2020.md), §II A):
* $L_x=2.5$ cm, $L_y=1.28$ cm (the real circumference is about 18 cm).
* Radial magnetic field, function of $x$ only, peak 0.01 T (printed as 100 G) at
  $x=0.75$ cm (about 2.5 cm in a real SPT-100).
* Anode at $x=0$ (200 V); cathode (electron emission) plane at $x=2.4$ cm
  (0 V). Electrons are injected there uniformly in $y$ to balance the
  current, and the potential is corrected so that its azimuthal average is
  zero at that plane.
* Ionization: an imposed cosine-shaped source of electron–ion pairs,
  nonzero for $0.25\le x\le1$ cm with its peak, $5.23\times10^{23}$ m⁻³ s⁻¹,
  at $x=0.625$ cm ([Marks & Gorodetsky (2025)](/sources/marks-2025.md),
  Eq. 2); the source integrated over the ionization zone, times $e$, gives
  an extracted ion current density of 400 A m⁻²
  ([Reza et al. (2022)](/sources/reza-2022.md), §3.1;
  [Charoy et al. (2020)](/sources/charoy-2020.md), §II).
* Initial plasma $n_0=5\times10^{16}$ m⁻³, $T_e=10$ eV, $T_i=0.5$ eV;
  injected particles at the same temperatures; singly charged xenon ions.
* Grid 512×256 ($\Delta x=4.88\times10^{-5}$ m, $\Delta y=5\times10^{-5}$ m),
  $\Delta t=5\times10^{-12}$ s, 20 µs simulated (4,000,000 steps), averages
  over 16–20 µs ([Marks & Gorodetsky (2025)](/sources/marks-2025.md);
  [Reza et al. (2022)](/sources/reza-2022.md), §3.1).
  [Charoy et al. (2020)](/sources/charoy-2020.md), §II B, derive these values
  from $\Delta t\le0.2/\omega_{pe}$ and $\Delta x\le\lambda_D$ at the maximum
  density ≈$5\times10^{17}$ m⁻³ and $T_e\approx50$ eV (see
  [resolution constraints](/definitions/explicit-pic-resolution-constraints.md)).
* Three particle-count cases: 75 (Case 2), 150 (Case 1) and 300 (Case 3)
  initial particles per cell, growing to about 290, 590 and 1200 at steady
  state in WarpX ([Marks & Gorodetsky (2025)](/sources/marks-2025.md),
  Table 4). [Charoy et al. (2020)](/sources/charoy-2020.md), §II B, report
  75 initial and about 250 at steady state, converged according to the
  2019 paper. The two steady-state counts come from different codes and
  are given as approximate; they are not in conflict.
* No [permittivity or mass scaling](/methods/pic-acceleration-scaling.md)
  ([Charoy et al. (2020)](/sources/charoy-2020.md), §II B).

The imposed ionization source precludes the
[breathing mode](/definitions/breathing-mode.md) and probably ion
transit-time oscillations ([Charoy et al. (2020)](/sources/charoy-2020.md),
p. 10).

## Runs

* **2019 participants** (as reported). Seven groups reproduced the case
  ([Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. III A d);
  LPPic was verified against six other codes
  ([Charoy et al. (2020)](/sources/charoy-2020.md), §II A). Typical wall
  times were 3–11 days; the fastest, a PPPL code, took 2.5 days on 112 CPUs
  for Case 2 (224 CPUs for Case 1, 448 for Case 3)
  ([Marks & Gorodetsky (2025)](/sources/marks-2025.md), Results, Table 4).
  The RUB implicit code ECCOPIC2S-M ran on GPUs (CUDA) at the explicit
  codes' $\Delta t$ and $\Delta x$, so the benefit of its GPU
  parallelization did not show here; it became visible only in a
  different benchmark
  ([Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. V B, V C b);
  Marks & Gorodetsky report the only GPU code as taking 9 days for Case 2
  on an Nvidia A100 with an implicit pusher, "not directly comparable".
* **LPPic, parametric extension** ([Charoy et al. (2020)](/sources/charoy-2020.md),
  §II–§V). The benchmark is case 0 of ten: peak field 0.005, 0.01, 0.015,
  0.02 T (printed as 50–200 G) at 400 A m⁻², current density 50, 100, 200,
  400 A m⁻² at 0.01 T, and three collisional variants (backscattering,
  isotropic ion–neutral scattering, all collisions) at 0.01 T and
  400 A m⁻². At 0.01 T the azimuthal wavelength
  changes sharply between a short-wavelength near-anode region and a
  long-wavelength plume, as in the 2019 paper; a higher field extends the
  long wavelengths toward the anode, 0.005 T extends the short ones into the
  plume, and lower current density gives longer wavelengths. The
  [instability-enhanced friction force](/results/instability-enhanced-friction-force.md)
  is the main contributor to axial electron transport (peak about
  11 N m⁻³ at the field maximum, read from Fig. 5a); density fluctuations
  are about 10% in the channel, a few percent just downstream of the exit
  and about 10% further out (§IV B).
* **WarpX on one GPU** ([Marks & Gorodetsky (2025)](/sources/marks-2025.md),
  Results, Fig. 3, Tables 4–5). Explicit [WarpX](/software/warpx.md): Case 2
  in 1.81 days on an H100 and 3.81 days on a V100; Case 1 in 2.86 days and
  Case 3 in 5.06 days on the H100; 1.52 days with tuned solver tolerance,
  sorting and resampling. Time-averaged $E_x$, $n_i$ and $T_e$ lie "well
  within" the band of the 2019 codes, with no error metric printed. Both
  azimuthal modes (short wavelength near the anode, long wavelength
  downstream) are reproduced. See [GPU acceleration](/methods/gpu-acceleration-of-pic.md).
* **Semi-implicit WarpX** ([Marks & Gorodetsky (2025)](/sources/marks-2025.md),
  Table 5, Figs. 8–14). Grids and steps coarsened 2×, 4×, 8× run in 11.5,
  4 and 2 h; deviation ≤10% at 2× and <25% at 4× and 8×, with the
  azimuthal spectrum altered at 4× and 8×. See
  [implicit and energy-conserving PIC](/methods/implicit-and-energy-conserving-pic.md).
* **Reduced-order PIC** ([Reza et al. (2022)](/sources/reza-2022.md), §3,
  Figs. 3–6). Single-region [pseudo-2D PIC](/methods/reduced-order-pic.md),
  150 particles per cell along $x$ (75,000 in total), real scale:
  time-averaged $E_x$, $n_i$, $\phi$, $T_e$ "consistent with" the 2D
  benchmark, no error metric. A 1D axial PIC needs a tuned three-zone
  Bohm-type collision frequency to match, and collapses without one. The
  azimuthal waves (≈3 MHz, ≈2 mm) follow the ion-acoustic dispersion
  relation.
* **Accelerated 1D tuning run** ([Reza et al. (2022)](/sources/reza-2022.md),
  §3.2, Fig. 4). A 1D axial run with $f_m=100$ and $f_\varepsilon=20$
  (about 300,000 steps for 20 µs) tuned to the benchmark potential shows
  "clear discrepancies" against it, while a real-scale 1D run with the same
  Bohm coefficients matches it.

## The code used by Charoy et al. (2020)

LPPic is the explicit, electrostatic 2D-3V PIC-MCC code of the
Laboratoire de Physique des Plasmas (CNRS–Ecole polytechnique), on a
structured Cartesian mesh in the axial–azimuthal plane with electrons and
singly charged xenon ions as macroparticles; its language and
parallelization are not stated, and HPC resources of CINES/GENCI and
CERFACS are acknowledged. The cathode emission plane sits 1 mm from the
right boundary. In the collisional variants (§V),
[Monte Carlo collisions](/methods/monte-carlo-collisions.md) after Vahedi
& Surendra act against a neutral background computed separately from 1D
Euler equations: electron–xenon elastic scattering and four excitations,
ion–neutral isotropic scattering and backscattering (charge exchange),
with LXCat (Phelps) cross sections
([Charoy et al. (2020)](/sources/charoy-2020.md), §II, §V,
acknowledgements).

## Radial–azimuthal benchmark (Villafana et al. 2021)

A companion LANDMARK case in the radial–azimuthal plane was reproduced by
seven codes; the 1D azimuthal FFTs of the azimuthal field show the
modified two-stream and electron cyclotron drift resonances "with a
minimal difference" between codes. In that case an explicit GPU code
performed "comparable to the best CPU-based code"
([Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. III A d, Fig. 4;
Sec. V B).

# Citations

1. [Charoy et al. (2020)](/sources/charoy-2020.md) — §II A–B, §III–§V, Figs. 3–5, acknowledgements.
2. [Marks & Gorodetsky (2025)](/sources/marks-2025.md) — Methods (Table 1, Eq. 2), Results (Fig. 3, Tables 4–5), semi-implicit section.
3. [Reza et al. (2022)](/sources/reza-2022.md) — §3.1–§3.2, Figs. 3–6.
4. [Taccogna et al. (2023)](/sources/taccogna-2023.md) — Sec. III A d (Fig. 4), Sec. V B, Sec. V C b.

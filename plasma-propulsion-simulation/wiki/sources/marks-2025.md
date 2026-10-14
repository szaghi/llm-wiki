---
type: Source
title: "Marks & Gorodetsky (2025) — GPU-accelerated kinetic Hall thruster simulations in WarpX"
description: "Runs the axial–azimuthal Hall-thruster PIC benchmark in WarpX on one GPU (1.81 days on an H100 against 2.5 days on 112 CPUs for the fastest 2019 code), shows that resampling below the steady-state particle count heats electrons, that semi-implicit coarsening by 2× stays within 10% in 11.5 h, and that the multigrid electrostatic solver is MPI-communication-bound on multiple GPUs."
resource: "doi:10.1007/s44205-025-00133-1"
source_kind: paper
authors: [Marks T.A., Gorodetsky A.A.]
year: 2025
venue: "J. Electr. Propuls. 4:34"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2025_Crossref_Journal_of_Electric_Propulsion_Marks_GPU-accelerated_kinetic_Hall_thruster_simulations_in_WarpX.pdf"
tags: [pic, gpu, performance, hall-thruster, benchmark, verification, software, instability]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The authors run the 2D axial–azimuthal Hall-thruster PIC benchmark of
Charoy et al. (2019) (LANDMARK Case 2a) with the open-source GPU-native
PIC code WarpX, extended through Python callbacks for ionization-source
injection, cathode re-injection and a potential correction. On one Nvidia
H100 the explicit baseline completes 20 µs in 1.81 days (3.81 days on a
V100), against 2.5 days on 112 CPUs for the fastest 2019 code. A parameter
study finds that multigrid tolerance and resampling threshold dominate wall
time, and that leveling-thinning resampling below the steady-state particle
count widens electron VDFs. Barnes' semi-implicit electrostatic scheme
allows 2×, 4× and 8× coarser grids and steps (11.5, 4 and 2 h) at growing
deviation and altered instability spectra. A 3D strong-scaling test on up
to 32 H100s shows the multigrid electrostatic solver spending up to 95% of
its time in MPI communication. The paper is an expanded version of the
authors' IEPC-2024-409 paper, which also studied shape functions and
electron–ion collision checks.

# Key claims

1. **Single-GPU wall time** (Abstract; Results; Table 4). Case 2 (75
   initial particles per cell): 1.81 days on an H100 (80 GB), 3.81 days on a
   V100. Shown.
2. **Comparison with 2019** (Results; Table 4). Typical 2019 wall times
   were 3–11 days; fastest the PPPL code, 2.5 days on 112 CPUs (Case 2), on
   224 CPUs (Case 1) and 448 CPUs (Case 3). The only 2019 GPU code took 9
   days for Case 2 on an Nvidia A100 with an implicit pusher, "not directly
   comparable". Attributed to Charoy et al. (2019).
3. **Architecture and hardware** ("Role of GPU hardware"). The V100 run
   beats all but two 2019 codes, so part of the gain is code architecture;
   the H100 is nearly 2× faster than the V100 with no algorithm change.
   Inference from their timings.
4. **Accuracy** (Fig. 3). Time-averaged $E_x$, $n_i$, $T_e$ lie "well
   within" the band of the 2019 Case 2 results. No metric for the explicit
   baseline.
5. **Solver tolerance** (Table 5). Multigrid relative tolerance $10^{-2}$,
   $10^{-3}$, $10^{-5}$, $10^{-6}$ needs on average 2, 2, 3, 4 iterations and
   gives 1.59, 1.59, 1.81, 1.93 days; loosening $10^{-5}\to10^{-3}$ saves
   about 13% (5 h) "with no visible impact". Shown.
6. **Resampling** (Table 5; Figs. 5–7). Leveling-thinning (Muraviev et al.
   2021) cuts wall time by up to 25% (1.39 days at a 200 threshold) but
   raises $T_e$ at the right boundary by 7 eV and widens axial and azimuthal
   VDFs; radial VDFs stay Maxwellian. The baseline steady state is 290
   particles per cell per species, so a 300 threshold acts only at start-up
   (1.76 days). Shown; the mechanism (insufficient particle resolution in
   high-density regions of the long-wavelength mode downstream of the field
   peak) is the authors' hypothesis.
7. **Sorting** (Table 5; Methods). Intervals 5–100 steps give 1.76 days, 500
   gives 1.81, 1000 gives 1.80; sorting costs about 80% of a particle push.
   Shown.
8. **Semi-implicit coarsening** (Table 5; Figs. 8–9). 2× ($\Delta t=10^{-11}$
   s, 256×128, constant 8): 11.5 h, deviation ≤10%; 4× ($2\times10^{-11}$ s,
   128×64, constant 16): 4 h; 8× ($4\times10^{-11}$ s, 64×32, constant 8):
   2 h; deviation <25% at 4× and 8×. Peaks drop baseline → 8×: $E_x$ 50 → 43
   (printed "kV"), density $3.6\times10^{17}\to3\times10^{17}$ m⁻³, $T_e$
   52 → 44 eV. Shown.
9. **Instability spectra** (Figs. 11–13). Two azimuthal modes (short
   wavelength near the anode, long wavelength downstream) are reproduced;
   dominant frequencies and wavelengths match at 1× and 2×; the distinction
   fades at 4× and disappears at 8×; maximum azimuthal field −40% (4×),
   −70% (8×). The time-averaged axial field stays consistent, read by the
   authors as transport being "relatively insensitive" to some spectral
   characteristics (hypothesis).
10. **Numerical heating** (Fig. 14). Cathode current fraction agrees with
    the benchmark at 1×, 2×, 4×, falls by a factor of 3 at 8×.
    Domain-averaged $T_e$ exceeds the benchmark by 2, 2.5, 1 eV at 2×, 4×,
    8×. A larger constant improves $T_e$ at the cost of $n$ and $E_x$; more
    particles reduce heating at 2× (Fig. 9). Shown.
11. **Strong scaling** (Fig. 15; Tables 2–3). 3D uniform periodic plasma,
    1 particle per cell, 1–32 GPUs. At workload $2^{13}$ (1024×512×512, the
    largest fitting one H100) the multi-GPU speed-up is only 1.75; the MPI
    fraction of the multigrid electrostatic solver reaches 95% at 32 GPUs.
    Particle routines and the EM solver scale "excellently" (consistent with
    Myers et al. 2021). Shown; cluster-specific.
12. **CHAOS** (Jambunathan & Levin 2018) is reported to scale well up to
    128 GPUs with a GPU conjugate-gradient Poisson solver. Attributed.
13. **Roofline** (Fig. 4b). Gather-and-push and deposition kernels are
    memory-bound on the H100; the field solver is far from the streaming
    limit. Ceilings printed: L1 33.0 TB/s, L2 12.0 TB/s, DRAM 3.4 TB/s;
    single 67 TFLOPs, double 34 TFLOPs. Shown.
14. **Engineering outlook** ("Kinetic simulations in an engineering
    context"). Real ionization brings ~10 kHz breathing oscillations,
    hence ~1 ms runs, about 50× this benchmark; 3D PIC (Villafana et al.
    2023) shows that 2D axial–azimuthal runs under-resolve the
    instabilities; whole-device kinetic runs "may still require wall times
    measuring in the months". Stated.

# Models and numerics

* Fully kinetic, explicit, electrostatic PIC; electrons and singly charged
  ions; no neutrals or collisions (benchmark); ionization replaced by a
  prescribed cosine source of electron–ion pairs (Eq. 2) with injected count
  from Eqs. 3–4 and stochastic rounding, positions by inverse-transform
  sampling (Eqs. 5–6). Ion species not restated.
* Domain $L_x=2.5$ cm (axial) × $L_y=1.28$ cm (azimuthal), periodic in
  $y$; radial field, peak 10 mT at $x=0.75$ cm; anode at $x=0$, cathode
  plane at $x=2.4$ cm, 200 V. 512×256 cells, $\Delta t=5\times10^{-12}$ s;
  $n_0=5\times10^{16}$ m⁻³, $T_e=10$ eV, $T_i=0.5$ eV; 20 µs, averages over
  16–20 µs.
* Cathode re-injection of the anode-plane ion-minus-electron count each
  step, at the base weight, 10 eV Maxwellian. Potential correction (Eqs.
  7–8): a linear ramp removes the azimuthal mean of the potential at the
  cathode plane, with the corresponding constant added to $E_x$.
* Geometric multigrid Poisson (Eq. 1), warm-started, double precision;
  energy-conserving gather (Lewis 1970), staggered grid, linear shapes;
  relativistic Boris push, single precision; gather+push fused.
* Semi-implicit scheme of Barnes as implemented by Groenewald et al.
  (Eq. 9), resembling the direct-implicit method of Langdon et al. (1983).
* Resampling: leveling-thinning, target ratio 1.5, minimum 75 per cell,
  trigger 200–300. Sorting every 5–1000 steps. Diagnostics every 5000
  steps; TinyProfiler.
* No anomalous-transport model. Hardware: one H100 80 GB (one run on a
  V100); scaling cluster with 8 GPUs per node, one MPI rank per GPU.
* WarpX v24.05–25.02; scripts at `https://github.com/archermarx/warpx-hall`.

# Tests and results

* Axial–azimuthal benchmark, Cases 1/2/3 (150/75/300 initial particles per
  cell; final 590/290/1200): H100 2.86/1.81/5.06 days. Time fractions
  (Case 2/1/3): gather+push 48.81/63.79/73.11%, field solve
  40.86/24.21/16.63%, deposition 8.43/10.72/9.63%, Python 1.9/1.28/0.63%.
* Parameter study (Table 5): resampling none/300/275/250/200 →
  1.81/1.76/1.66/1.54/1.39 days; optimized explicit (resampling 300, sort
  100, tolerance $10^{-3}$) 1.52 days (38 h).
* Semi-implicit 2×/4×/8× as in Key claims 8–10. The reader's visual
  readings of Fig. 9 (approximate): 2× ≈5% $E_x$, ≈5–6% $n_i$, ≈9% $T_e$;
  4× ≈12%, ≈15%, ≈13%; 8× ≈23%, ≈15%, ≈9–10%. At 8× the anode sheath
  widens (Fig. 10).
* Strong scaling (Eq. 11): efficiency is the one-GPU time divided by the
  GPU count times the time on that many GPUs; workload $2^{14}$ is measured
  relative to 2 GPUs.

# Notation map

| Marks & Gorodetsky (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$ (axial), $y$ (azimuthal) | $x$, $y$ with $x\leftrightarrow z$, $y\leftrightarrow\theta$ | planar domain |
| $B_z(x)$ | radial field as a function of $z$ | **collision:** the paper's $z$ is radial, the registry's $z$ is axial |
| $U$; $U_0$ | uncorrected potential; $V_d$ | **collision:** $U$ is both the solved potential and, subscripted, the discharge voltage |
| $\phi$ | $\phi$ | corrected potential (Eq. 7) |
| $\overline U_e$, $\mathcal E_x$ | words | cathode-plane mean potential; uncorrected $E_x$ |
| $\rho$, $\epsilon_0$ | $\rho_c$, $\varepsilon_0$ | |
| $n_0$, $T_{e,0}$, $T_{i,0}$ | $n_0$, $T_e$, $T_i$ | |
| $W_0$ | $W$ | base macroparticle weight |
| $N_{ppc,ini}$ | $N_{\mathrm{ppc}}$ | initial value |
| $N_x$, $N_y$, $N_z$ | words (cell counts) | not in the registry |
| $S(x)$, $S_0$ | words (ionization source rate) | **collision:** registry $S(\mathbf x)$ is the particle shape function |
| $C$ (semi-implicit constant) | words | not in the registry; proposed $C_{\mathrm{SI}}$ |
| $J_M$ | words (extracted ion current) | |
| $y$, $y_b$ in Eq. 10 | words | **collision** with the azimuthal $y$; local use |

# Pages created or updated

Chunk 1 (2026-10-14) created every page of the bundle. This source is cited on:

* [Anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md)
* [Axial–azimuthal Hall-thruster PIC benchmark (Charoy et al. 2019)](/benchmarks/axial-azimuthal-pic-benchmark.md)
* [Breathing mode](/definitions/breathing-mode.md)
* [Electron drift instability (ECDI)](/definitions/electron-drift-instability.md)
* [GPU acceleration of particle codes](/methods/gpu-acceleration-of-pic.md)
* [Instability-enhanced electron–ion friction and effective mobility](/results/instability-enhanced-friction-force.md)
* [One-dimensional fluid model of the Hall-thruster discharge](/methods/one-dimensional-fluid-hall-model.md)
* [Particle pushers: leapfrog, Boris and Runge–Kutta](/methods/particle-pushers.md)
* [Particle-in-cell with Monte Carlo collisions (PIC-MCC)](/methods/pic-mcc.md)
* [Resolution constraints of explicit PIC](/definitions/explicit-pic-resolution-constraints.md)
* [Semi-implicit, implicit and energy-conserving PIC](/methods/implicit-and-energy-conserving-pic.md)
* [WarpX](/software/warpx.md)

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2025_Crossref_Journal_of_Electric_Propulsion_Marks_GPU-accelerated_kinetic_Hall_thruster_simulations_in_WarpX.pdf`.
   * **Version.** Publisher's final version (Open Access, CC BY 4.0), 25
     pages; received 20 December 2024, accepted 28 April 2025.
   * **Identity.** doi:10.1007/s44205-025-00133-1, printed on page 1 and
     checked on Crossref (title, both authors): J. Electr. Propuls. 4(1),
     article 34; issued and published online 2025-05-09, no print date.
   * **How it was read.** Full text; Tables 4 and 5 (images) read from
     rendered pages 13–14; Fig. 9 bars read visually; Figs. 3, 5–8, 10–15
     only through the numbers the text quotes.
   * **Recorded as printed.**
     * Table 1 gives the maximum field as $10^{-12}$ T; the text gives 10 mT.
     * Results: "downstream of the peak magnetic field (x > 0.75 m)"; the
       domain is 2.5 cm, so cm is meant.
     * Scaling: the text says runs with 16 and 32 GPUs used two and three
       nodes; Table 3 gives 2 and 4 nodes, and 3 nodes of 8 GPUs cannot hold
       32. Table 3's 32-GPU rank layout (4×4×4 = 64) contradicts one rank per
       GPU.
     * Table 1 lists sort intervals 10–1000 and resampling thresholds
       200/250/300; the text and Table 5 include 5 and 275.
     * The 2× speed-up is printed as "3.5x"; 43.4 h / 11.5 h = 3.78 against
       the baseline, 38 h / 11.5 h = 3.3 against the optimized run.
     * Peak fields printed as "50 kV" and "43 kV": a field unit is meant.
     * "Decreasing the tolerance" for $10^{-5}\to10^{-3}$ is a loosening;
       the same paragraph later says "increasing".
     * H100 FP16 printed as "1513 FLOPS" (tera missing).
     * The 2019 GPU code is said to have run on an A100, which was released
       after the 2019 benchmark publication: a later re-run or a slip.
     * The Conclusion speaks of "good agreement" up to 4×, while the
       semi-implicit section calls 4× and 8× runs "difficult to trust for
       predictive simulations".
   * **Reference list.** 30 printed entries (Crossref reference-count 30).


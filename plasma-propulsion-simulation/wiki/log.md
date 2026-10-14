# Directory Update Log

## 2026-10-14

* **Scaffolding and chunk 1 (the core, 20 sources)** (D22). Read by 20 reader
  agents into scratch notes (each paper read fully; equations checked on rendered
  pages where the text layer failed), drafted by six drafters from the notes only,
  installed by the compiler, then audited read-only before staging (counts as deep
  lint #1) and fixed: six attribution or fidelity errors corrected, paper-native
  symbols removed from concept pages, SI units enforced, one missed contradiction
  opened, and three pages below the granularity bar merged (LANDMARK test case 3
  into the one-dimensional fluid model, LPPic into the axial–azimuthal benchmark,
  EP2PLUS into the hybrid-model page).
  * **Identity:** the archive file named for Bird et al. (2009) is Mungiguerra et
    al. (2018), Acta Astronaut. 151:456, ingested as
    [mungiguerra-2018](/sources/mungiguerra-2018.md); Bird et al. (2009) is not in
    the archive. charoy-2020 and taccogna-2019 were read as HAL accepted
    manuscripts, taccogna-2023 as the accepted manuscript, reza-2022 as the
    Research Square preprint (recorded on each Source page).
  * **Notation registry seeded** ([notation](/notation.md)): coordinates and
    conventions (comma component subscripts, reference subscript 0, averages and
    fluctuations), species and kinetic quantities, fields, plasma parameters (Bohm
    coefficient $\alpha_{\mathrm B}$ with $\nu_{\mathrm{ano}}=\alpha_{\mathrm B}\omega_{ce}/16$,
    $\Omega_e$, $\mu_\perp$, $\phi^*$, $\gamma$, $\delta_{\mathrm{SEE}}$,
    $\mathbf R_{sk}$), particle methods ($W$, $N_{\mathrm{ppc}}$, $P_c$, scaling
    factors $f_\varepsilon$, $f_m$, $f_g$), waves, inference ($\boldsymbol\vartheta$,
    Sobol' indices), surfaces, thruster performance and magnetic-nozzle thrust
    components.
  * **Definitions (17):** [Anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md), [Breathing mode](/definitions/breathing-mode.md), [Charge-exchange ions](/definitions/charge-exchange-ions.md), [Current-free double layer](/definitions/current-free-double-layer.md), [Electron drift instability (ECDI)](/definitions/electron-drift-instability.md), [Cross-field electron mobility and the Hall parameter](/definitions/electron-mobility-and-hall-parameter.md), [Resolution constraints of explicit PIC](/definitions/explicit-pic-resolution-constraints.md), [Hall-effect thruster](/definitions/hall-effect-thruster.md), [Helicon plasma thruster](/definitions/helicon-plasma-thruster.md), [Magnetic nozzle](/definitions/magnetic-nozzle.md), [Magnetic shielding](/definitions/magnetic-shielding.md), [Near-wall conductivity](/definitions/near-wall-conductivity.md), [Polytropic electron closure and plume cooling](/definitions/polytropic-electron-closure.md), [Pulsed plasma thruster](/definitions/pulsed-plasma-thruster.md), [Rotating spoke](/definitions/rotating-spoke.md), [Secondary electron emission and sheath regimes](/definitions/secondary-electron-emission.md), [Thermalized potential](/definitions/thermalized-potential.md).
  * **Methods (18):** [Bayesian calibration of thruster models](/methods/bayesian-calibration.md), [Boltzmann-relation electrons](/methods/boltzmann-electron-model.md), [Direct simulation Monte Carlo (DSMC)](/methods/dsmc.md), [Electron fluid models (drift-diffusion)](/methods/electron-fluid-model.md), [Five-moment electron fluid model](/methods/five-moment-fluid-model.md), [Gas–surface interaction models](/methods/gas-surface-interaction.md), [GPU acceleration of particle codes](/methods/gpu-acceleration-of-pic.md), [Hybrid PIC–fluid models](/methods/hybrid-pic-fluid-model.md), [Semi-implicit, implicit and energy-conserving PIC](/methods/implicit-and-energy-conserving-pic.md), [Laser-ablation plume model](/methods/laser-ablation-plume-model.md), [Magnetic-field-aligned meshes](/methods/magnetic-field-aligned-mesh.md), [Monte Carlo collisions and the null-collision method](/methods/monte-carlo-collisions.md), [One-dimensional fluid model of the Hall-thruster discharge](/methods/one-dimensional-fluid-hall-model.md), [Particle pushers: leapfrog, Boris and Runge–Kutta](/methods/particle-pushers.md), [Permittivity, ion-mass and geometric scaling in PIC](/methods/pic-acceleration-scaling.md), [Particle-in-cell with Monte Carlo collisions (PIC-MCC)](/methods/pic-mcc.md), [Reduced-order (pseudo-2D) PIC](/methods/reduced-order-pic.md), [Spectral entropy of plasma oscillations](/methods/spectral-entropy.md).
  * **Results (2):** [Instability-enhanced electron–ion friction and effective mobility](/results/instability-enhanced-friction-force.md), [Thrust decomposition of a magnetic nozzle](/results/magnetic-nozzle-thrust-decomposition.md).
  * **Benchmarks (2):** [Axial–azimuthal Hall-thruster PIC benchmark (Charoy et al. 2019)](/benchmarks/axial-azimuthal-pic-benchmark.md), [SPT-100 as a validation case](/benchmarks/spt-100.md).
  * **Software (3):** [EX-PWS](/software/ex-pws.md), [HYPHEN](/software/hyphen.md), [WarpX](/software/warpx.md).
  * **Sources (20):** [Adamovich et al. (2017) — The 2017 Plasma Roadmap: Low temperature plasma science and technology](/sources/adamovich-2017.md), [Ahedo (2023) — Using electron fluid models to analyze plasma thruster discharges](/sources/ahedo-2023.md), [Boyd (2005) — Numerical modeling of spacecraft electric propulsion thrusters](/sources/boyd-2005.md), [Cai et al. (2018) — Three-dimensional particle simulation of ion thruster plume impingement](/sources/cai-2018.md), [Charoy et al. (2020) — A comparison between kinetic theory and particle-in-cell simulations of anomalous electron transport in E × B plasma discharges](/sources/charoy-2020.md), [Eckels et al. (2024) — Hall thruster model improvement by multidisciplinary uncertainty quantification](/sources/eckels-2024.md), [Gallo et al. (2021) — Numerical Aspects of Particle-in-Cell Simulations for Plasma-Motion Modeling of Electric Thrusters](/sources/gallo-2021.md), [Giannetti et al. (2021) — Numerical and experimental investigation of longitudinal oscillations in Hall thrusters](/sources/giannetti-2021.md), [Marks & Gorodetsky (2025) — GPU-accelerated kinetic Hall thruster simulations in WarpX](/sources/marks-2025.md), [Miranda et al. (2026) — Spectral entropy of plasma oscillations in numerical simulations of a Hall thruster during start-up transients](/sources/miranda-2026.md), [Mungiguerra et al. (2018) — Effects of solar panels on Aerodynamics of a small satellite with deployable aero-brake](/sources/mungiguerra-2018.md), [Muñoz Tejeda, Perales-Díaz & Knoll (2025) — Computational modelling of water-fuelled Hall Effect Thrusters](/sources/munoz-2025.md), [Reza, Faraji & Knoll (2022) — Resolving multi-dimensional plasma phenomena in Hall thrusters using the reduced-order particle-in-cell scheme](/sources/reza-2022.md), [Saravia et al. (2026) — Calibration of a Hall thruster numerical model using a Bayesian approach](/sources/saravia-2026.md), [Sun & Wu (2018) — Ignition mechanism in ablative pulsed plasma thrusters with coaxial semiconductor spark plugs](/sources/sun-2018.md), [Taccogna & Garrigues (2019) — Latest progress in Hall thrusters plasma modelling](/sources/taccogna-2019.md), [Taccogna et al. (2023) — Plasma propulsion modeling with particle-based algorithms](/sources/taccogna-2023.md), [Takahashi (2019) — Helicon-type radiofrequency plasma thrusters and magnetic plasma nozzles](/sources/takahashi-2019.md), [Troyetsky, Bögel & Hara (2026) — Comparison of two-dimensional five-moment fluid and kinetic simulations for the discharge plasma in a Hall effect thruster](/sources/troyetsky-2026.md), [Zhang et al. (2018) — Investigation on plume expansion and ionization in a laser ablation plasma thruster](/sources/zhang-2018.md).
  * **Contradictions opened (3, all Open):** the form of the Jorns (2018)
    anomalous collision frequency as two reviews print it
    ([anomalous transport](/definitions/anomalous-electron-transport.md)); the
    priority claim for the first GPU PIC of a thruster
    ([GPU acceleration](/methods/gpu-acceleration-of-pic.md), recommended for the
    human's closure); noise or physics as the cause of the ion-acoustic character
    of azimuthal PIC below about 1000 particles per cell
    ([electron drift instability](/definitions/electron-drift-instability.md)).
  * **Bibliography:** [bibliography](/bibliography.md) created from the 20
    reference lists, 1798 printed references merged into 1437 entries with
    `tools/bib_merge.py` (FLAGS 0; `--dupes` and a fuzzy-title sweep clean).
    The cited PSST 2019 paper of Taccogna et al. is `taccogna-2019-b`, distinct
    from the ingested review; undated web resources take the earliest citing year.
  * Digest of contradictions, printed slips, identity problems and open
    bibliography decisions: `INGESTION-ISSUES.md` at the bundle root.

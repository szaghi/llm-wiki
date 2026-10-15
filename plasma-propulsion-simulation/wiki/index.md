---
okf_version: "0.1"
---

# plasma-propulsion-simulation — Knowledge Bundle

Numerical modelling of electric and plasma thrusters: Hall, gridded-ion,
helicon, pulsed and laser-ablation thrusters; particle-in-cell, DSMC,
hybrid and fluid models of their discharges and plumes; anomalous electron
transport, oscillations and instabilities; verification, uncertainty
quantification and calibration; GPU particle codes.

**Start here:** the [Notation registry](/notation.md), which is normative
for every page, and the [update log](/log.md).

**Corpus:** 41 of the archive's 108 files ingested. Chunk 1, the core (20):
three reviews of plasma-propulsion modelling
([Boyd 2005](/sources/boyd-2005.md), [Taccogna & Garrigues 2019](/sources/taccogna-2019.md),
[Taccogna et al. 2023](/sources/taccogna-2023.md)), a review of helicon thrusters and
magnetic nozzles ([Takahashi 2019](/sources/takahashi-2019.md)), a review of electron
fluid models ([Ahedo 2023](/sources/ahedo-2023.md)), the 2017 Plasma Roadmap
([Adamovich et al. 2017](/sources/adamovich-2017.md)), and fourteen research papers.
The other 88 files are the rest of *Acta Astronautica* vol. 151 (2018), compiled
as context (bundle law, D22, D23): chunk 2 added 21 of them as Source-only
pages (high-speed aerothermodynamics and chemical propulsion papers,
outside this bundle's domain); they are listed in the
[sources catalog](/sources/index.md) with the tag `context`. The
[bibliography](/bibliography.md) lists the 2130 works the 41 sources cite.

## Reading guide

1. **The devices.** [Hall-effect thruster](/definitions/hall-effect-thruster.md)
   (SPT and TAL, operating ranges, what a model must capture), then
   [helicon plasma thruster](/definitions/helicon-plasma-thruster.md) with the
   [magnetic nozzle](/definitions/magnetic-nozzle.md), the
   [current-free double layer](/definitions/current-free-double-layer.md) and the
   [thrust decomposition](/results/magnetic-nozzle-thrust-decomposition.md), and the
   [pulsed plasma thruster](/definitions/pulsed-plasma-thruster.md).
2. **The central open problem.**
   [Anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md)
   (with its table of Bohm-type coefficients), built on
   [cross-field mobility and the Hall parameter](/definitions/electron-mobility-and-hall-parameter.md);
   the candidate mechanisms [near-wall conductivity](/definitions/near-wall-conductivity.md)
   and the [electron drift instability](/definitions/electron-drift-instability.md),
   whose saturated state gives the
   [instability-enhanced friction](/results/instability-enhanced-friction-force.md);
   the oscillations [breathing mode](/definitions/breathing-mode.md) and
   [rotating spoke](/definitions/rotating-spoke.md).
3. **Kinetic models.** [PIC-MCC](/methods/pic-mcc.md), its
   [resolution constraints](/definitions/explicit-pic-resolution-constraints.md) and the
   [scaling tricks](/methods/pic-acceleration-scaling.md) that relax them;
   [Monte Carlo collisions](/methods/monte-carlo-collisions.md),
   [particle pushers](/methods/particle-pushers.md); cost reductions:
   [reduced-order PIC](/methods/reduced-order-pic.md),
   [implicit and energy-conserving PIC](/methods/implicit-and-energy-conserving-pic.md),
   [GPU acceleration](/methods/gpu-acceleration-of-pic.md) and the code
   [WarpX](/software/warpx.md); the verification case
   [axial–azimuthal PIC benchmark](/benchmarks/axial-azimuthal-pic-benchmark.md)
   (with the code LPPic used on it).
4. **Fluid and hybrid models.** [Electron fluid models](/methods/electron-fluid-model.md),
   the [thermalized potential](/definitions/thermalized-potential.md) and
   [magnetic-field-aligned meshes](/methods/magnetic-field-aligned-mesh.md);
   [hybrid PIC–fluid models](/methods/hybrid-pic-fluid-model.md) with
   [Boltzmann-relation electrons](/methods/boltzmann-electron-model.md) and the codes
   [HYPHEN](/software/hyphen.md) and EP2PLUS; the
   [five-moment model](/methods/five-moment-fluid-model.md) and its comparison with
   PIC; the [polytropic closure](/definitions/polytropic-electron-closure.md).
5. **Walls and sheaths.** [Secondary electron emission and sheath regimes](/definitions/secondary-electron-emission.md),
   [magnetic shielding](/definitions/magnetic-shielding.md).
6. **Reduced models, calibration and uncertainty.**
   [One-dimensional fluid model](/methods/one-dimensional-fluid-hall-model.md),
   [Bayesian calibration](/methods/bayesian-calibration.md) (identifiability,
   model-form error, Sobol' analysis), the validation cases
   [SPT-100](/benchmarks/spt-100.md) and LANDMARK test case 3 (on the
   one-dimensional fluid model page); the diagnostic
   [spectral entropy](/methods/spectral-entropy.md).
7. **Plumes and rarefied flow.** [DSMC](/methods/dsmc.md),
   [charge-exchange ions](/definitions/charge-exchange-ions.md),
   [gas–surface interaction](/methods/gas-surface-interaction.md), the plume code
   [EX-PWS](/software/ex-pws.md), and the
   [laser-ablation plume model](/methods/laser-ablation-plume-model.md).

## Open contradictions

* The form of the Jorns (2018) data-driven anomalous collision frequency, as two
  reviews print it ([anomalous transport](/definitions/anomalous-electron-transport.md)).
* The priority claim for the first GPU PIC simulation of a plasma thruster
  ([GPU acceleration](/methods/gpu-acceleration-of-pic.md)), recommended for
  closure by the human.
* Numerical noise or physics as the cause of the ion-acoustic character of
  azimuthal PIC below about 1000 particles per cell
  ([electron drift instability](/definitions/electron-drift-instability.md)).

---
type: Source
title: "Adamovich et al. (2017) — The 2017 Plasma Roadmap: Low temperature plasma science and technology"
description: "Nineteen two-author perspective sections on low-temperature plasma science; for this bundle, the 2017 state of electric propulsion (Hall and gridded-ion thrusters, magnetic shielding, nested channels, priorities on electron transport and predictive 3D codes), anomalous transport in E×B discharges as instability-driven, and the modelling ecosystem (GPU, Poisson parallelization, verification and validation, data uncertainty)."
resource: "doi:10.1088/1361-6463/aa76f5"
source_kind: paper
authors: [Adamovich I., Baalrud S.D., Bogaerts A., Bruggeman P.J., Cappelli M., Colombo V., Czarnetzki U., Ebert U., Eden J.G., Favia P., Graves D.B., Hamaguchi S., Hieftje G., Hori M., Kaganovich I.D., Kortshagen U., Kushner M.J., Mason N.J., Mazouffre S., Mededovic Thagard S., Metelmann H.-R., Mizuno A., Moreau E., Murphy A.B., Niemira B.A., Oehrlein G.S., Petrovic Z.Lj., Pitchford L.C., Pu Y.-K., Rauf S., Sakai O., Samukawa S., Starikovskaia S., Tennyson J., Terashima K., Turner M.M., van de Sanden M.C.M., Vardelle A.]
year: 2017
venue: "J. Phys. D: Appl. Phys. 50:323001"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2017_Crossref_Journal_of_Physics_D_Applied_Physics_Adamovich_The_2017_Plasma_Roadmap_Low_temperature_plasma_science_and_t.pdf"
tags: [review, hall-thruster, anomalous-transport, instability, pic, gpu, verification]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The second edition of the *J. Phys. D* Plasma Roadmap: 19 two-author
perspective sections covering low-temperature plasma (LTP) science and
technology, each with the same structure (status, challenges, advances,
concluding remarks), edited by Bruggeman, Czarnetzki and Kushner. It
presents no new simulation, proof or experiment; every figure is
reproduced from cited work. Sections read fully, as relevant to this
bundle: §12 (aerospace: propulsion and flow control; Mazouffre & Moreau),
§16 (plasma theory; Baalrud & Kaganovich), §17 (modelling and simulation;
Ebert & Kushner), §§4, 18, 19 (particle transport, atomic and molecular
data, plasma chemistry). The other sections (sources, metamaterials,
multiphase, materials processing, agriculture, medicine, environment,
combustion, thermal plasmas, diagnostics, analytical chemistry) were
skimmed and are outside the domain.

# Key claims

All stated or attributed.

1. **Electric propulsion status** (§12): gridded ion engines and Hall
   thrusters are the most advanced technologies (attributed to the 2012
   Roadmap); ion engines give high exhaust velocity but limited thrust,
   Hall thrusters a larger thrust-to-power ratio.
2. **Magnetic shielding** (§12): has "led to a drastic improvement in
   thruster lifetimes" (Mazouffre 2016; Hofer et al. 2014); the wall-less
   configuration "may potentially" reduce wear.
3. **Power classes** (§12, Fig. 22): high-power (above 20 kW) long-life
   thrusters are needed; the 10 kW-class nested-channel X2 in magnetic
   shielding was "validated at 20 kW", with research above 100 kW; MPD and
   VASIMR for MW; 1–100 W systems through miniaturisation and
   cathode-less concepts (PEGASES, ECR, vacuum-arc, liquid-fed PPT);
   alternatives to xenon are needed.
4. **EP research priorities** (§12): electron transport, turbulence and
   confinement in magnetized discharges first; plasma–wall interaction
   with accurate SEE and sputtering data; "The development of powerful 3D
   codes with predictive capabilities has become a necessity"; facility
   effects critical.
5. **Anomalous transport as instability-driven** (§16, Fig. 31): anomalous
   transport in $\mathbf E\times\mathbf B$ discharges "may be associated
   with fluctuations amplified by the differential flow between electrons
   and ions" (Lafleur, Baalrud & Chabert 2016) or between ion populations
   (Tsikata et al. 2014), or with the drift between wall-emitted and plasma
   electrons (Campanell & Umansky 2016); Fig. 31 reproduces MHz-scale
   fluctuations from a Hall-thruster PIC run.
6. **Rotating spokes** (§16, Fig. 30): large-scale coherent structures in
   Hall thrusters, magnetrons, Penning discharges and magnetic filters.
7. **Theory–simulation hierarchy** (§16): reduced-dimension kinetic or PIC
   simulations should test theory and then inform fluid models efficient
   enough for whole devices; the LTP community "would benefit from
   adapting" fusion turbulence methods.
8. **Modelling ecosystem** (§17): hybrid models and AMR enable
   time-dependent 3D simulations (Fig. 32, AMR PIC of breakdown in argon);
   progress in GPUs (Eremin et al. 2016); "implementation of Poisson's
   equation, due to its nonlocal nature, makes it still a major challenge
   to code parallelization"; verification and validation "becomes even more
   important"; the number of groups developing new algorithms is
   shrinking.
9. **Transport data and verification** (§4): Boltzmann-equation and Monte
   Carlo transport; plasma models "should be tested on transport based
   benchmarks as a necessary part of the verification of the model"; 3D
   MC/PIC with adaptive mesh is "required for high-fidelity modeling
   predictions".
10. **Data and mechanisms** (§§18–19): semi-empirical electron cross
    sections reach "accuracies of some 10%"; theoretical uncertainty
    estimates are rare; LXCat (2010) and VAMDC; validated reaction
    mechanisms are lacking, with model reduction and sensitivity analysis
    with error bars as tools.

# Models and numerics

None of its own. Named: two-term and multi-term Boltzmann solvers, Monte
Carlo swarm simulation, fluid, hybrid and global models, 3D MC/PIC with
adaptive mesh, molecular dynamics and DFT for surfaces. No mesh, time
step, weight, scaling or code detail is given; a GPU code (Eremin et al.
2016) and a free two-term Boltzmann solver (Hagelaar & Pitchford 2005)
are cited without names.

# Tests and results

None of its own. Reproduced: Fig. 7 (multi-term Boltzmann drift
velocities), Fig. 22 (X2 thruster photo), Fig. 30 (spokes, magnetron PIC),
Fig. 31 (Hall-thruster PIC fluctuations), Fig. 32 (AMR PIC breakdown),
Figs. 33–36 (other topics).

# Notation map

Almost no mathematics.

| Adamovich et al. (2017) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $T_e$, $T_g$ | $T_e$, $T_n$ | |
| $n_0$ (gas density in $E/n_0$, $B/n_0$) | $n_n$ | **collision:** registry $n_0$ is a reference density |
| $E/n_0$ (Td), $B/n_0$ (Hx) | words | 1 Td = $10^{-21}$ V m², 1 Hx = $10^{-27}$ T m³ |
| $\varepsilon_p$, $\mu_{\mathrm{eff}}$ (§2) | words | **collision** with $\varepsilon_0$, $\mu_0$, $\mu_\perp$; outside the domain |

# Pages created or updated

Chunk 1 (2026-10-14) created every page of the bundle. This source is cited on:

* [Anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md)
* [Bayesian calibration of thruster models](/methods/bayesian-calibration.md)
* [Electron drift instability (ECDI)](/definitions/electron-drift-instability.md)
* [GPU acceleration of particle codes](/methods/gpu-acceleration-of-pic.md)
* [Hall-effect thruster](/definitions/hall-effect-thruster.md)
* [Magnetic shielding](/definitions/magnetic-shielding.md)
* [Particle-in-cell with Monte Carlo collisions (PIC-MCC)](/methods/pic-mcc.md)
* [Pulsed plasma thruster](/definitions/pulsed-plasma-thruster.md)
* [Rotating spoke](/definitions/rotating-spoke.md)

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2017_Crossref_Journal_of_Physics_D_Applied_Physics_Adamovich_The_2017_Plasma_Roadmap_Low_temperature_plasma_science_and_t.pdf`.
   * **Version.** Publisher's version of record (IOP typeset, CC BY 3.0,
     46 pages) as deposited on HAL (hal-01895583v1); the 48-page file adds a
     HAL cover and an IOP download cover. Not a preprint.
   * **Identity.** doi:10.1088/1361-6463/aa76f5, checked on Crossref
     (J. Phys. D: Appl. Phys. 50(32), article 323001): received 13 January
     2017, revised 27 May 2017, accepted 5 June 2017, online 14 July 2017,
     print 16 August 2017.
   * **How it was read.** Introduction and §§4, 12, 16–19 in full; the
     other sections skimmed. No equations. Reference titles are not printed
     (IOP style).
   * **Recorded as printed.**
     - §12 attributes "the most advanced technologies are the gridded ion
       engine and the Hall thruster" to the 2012 Roadmap, not to an
       electric-propulsion source.
     - Refs. [175] and [185] are the same work (Pitchford et al. 2017,
       Plasma Process. Polym. 14:1600098) under two journal spellings.
     - Refs. [138] and [182] share Plasma Sources Sci. Technol. 25:054003;
       not resolved.
     - Volume–year mismatches as printed (keys follow the printed year):
       [111], [183], [176], [103], [151], [162].
     - Probable misspellings: [60] "Kenarik" (Kanarik), [94] "Dozlas"
       (Dozias), [139] "Lempert W A" against "Lempert W R" in [45].
   * **Reference list:** 189 entries, one numbering across the paper
     (Crossref count 189). Suffixed keys in printed order: chen-2015/-b,
     wang-2016/-b, bruggeman-2016/-b, white-2009/-b, lafleur-2016/-b,
     pitchford-2017/-b; corporate keys itrs-2015 and grimech-2017.

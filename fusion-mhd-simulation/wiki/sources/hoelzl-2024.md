---
type: Source
title: "Hoelzl et al. (2024) — Non-linear MHD modelling of transients in tokamaks: a review of recent advances with the JOREK code"
description: "Review of 2021–2024 advances with the non-linear extended-MHD code JOREK: ELM-free regimes and RMP ELM control, pellets, kinetic neutrals and impurities, VDEs and JOREK-CARIDDI wall coupling, SPI disruption mitigation, the vertical-force-mitigation mechanism, the current spike, runaway-electron beams, stellarators, energetic particles, particle-in-cell turbulence, flux pumping, and numerical and infrastructure developments."
resource: "doi:10.1088/1741-4326/ad5a21"
source_kind: paper
authors: [Hoelzl M., Huijsmans G.T.A., Artola F.J., Nardon E., Becoulet M., Schwarz N., Cathey A., Pamela S.J.P., Aleynikova K., Antlitz F., Bandaru V., Bergström H., Bhole A., Bogaarts T., Bonfiglio D., Cipolletta F., Driessen T., Edes L., Futatani S., Hao G., Hindenlang F., Holod I., Hu D., Hu S., Isernia N., Isliker H., Kim S.K., Kong M., Korving S., Kos L., Krebs I., Lee S.J., Liang Y.C., Liang Z., Liu S.J., Lu Z.X., Meier L., Messfeldt L., Mitterauer V., Nikulsin N., Nkonga B., Ramasamy R., Reinking J., Rogge C., Rubinacci G., Särkimäki K., Smits T., Sommariva C., Sparago R., Strien K., Szucs M., Tang W., van Tongeren J., Vannini F., Ventre S., Villone F., Wang C., Wang L., Wieschollek F., Wouters F., Zielinski J., Zhang H.]
year: 2024
venue: "Nucl. Fusion 64:112016"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2024_Crossref_Nuclear_Fusion_Hoelzl_Non-linear_MHD_modelling_of_transients_in_tokamaks_a_review.pdf"
tags: [review, mhd, reduced-mhd, full-mhd, extended-mhd, tokamak, stellarator, disruption, vde, runaway-electrons, impurities, neutrals, wall, free-boundary, elm, pedestal, energetic-particles, hybrid-kinetic, finite-elements, gpu, code]
timestamp: 2026-10-16T00:00:00Z
---

# Summary

A concise community review of research with the non-linear extended-MHD
code [JOREK](/software/jorek.md) over roughly 2021–2024, designed as "a
complete overview" that defers all detail to about 89 original
publications. It prints **no equations**. Section 2 covers pedestal,
scrape-off-layer and divertor physics: regimes without large ELMs (ASDEX
Upgrade small ELMs and quasi-continuous exhaust, EDA H-mode, QH-mode with
$q_{95}$ windows, HL-3 predictions), RMP ELM control (free-boundary RMP
response through JOREK–STARWALL, pedestal-top island penetration, KSTAR
density pump-out, ITER predictions), pellet ELM triggering, and kinetic
neutrals and impurities (ITER high-field-side high-density region,
tungsten transport, X-point radiator). Section 3 covers disruptions:
unmitigated [VDEs](/definitions/vertical-displacement-event.md) (the 3D VDE
benchmark, ASDEX Upgrade hot-VDE validation, COMPASS sheath boundary
conditions, an ITER unmitigated thermal quench of about 20 ms), two-way
JOREK–CARIDDI coupling to 3D volumetric walls, shattered pellet and
massive material injection with
[collisional-radiative impurities](/methods/collisional-radiative-impurity-model.md),
current-quench forces and the
[vertical-force-mitigation mechanism](/results/vertical-force-mitigation.md),
the $I_p$ spike, and [runaway-electron](/definitions/runaway-electrons.md)
beams. Section 4 covers stellarators (virtual-current model, JOREK3D,
VMEC comparisons), energetic particles (full-$f$ pressure coupling,
fishbones), electrostatic particle-in-cell ITG/TEM turbulence and flux
pumping. Section 5 lists numerics and infrastructure: a preconditioner
that keeps toroidal-harmonic coupling, BiCGSTAB besides GMRES,
arbitrary-order Bézier elements, axis regularization, shock capturing,
solver spectral analysis, wall-matrix compression, an OpenACC GPU port of
the particle module, IMAS and MUSCLE3.

# Key claims

The paper is a review: every claim rests on a cited original work.
"Shown" below means a figure reproduced in the review carries the
evidence; "Attributed" means the claim is asserted with a citation only.

1. **Small ELMs / QCE** (§2.1). ASDEX Upgrade low-triangularity small-ELM
   simulations "agree qualitatively with the quasi-continuous exhaust
   regime", with transitions to large ELMs at higher heating and at
   sufficiently low separatrix density. Attributed.
2. **EDA H-mode** (§2.1, Fig. 1). Fluctuating MHD dominated by $n=1$–3 with
   pedestal fluctuation frequencies in the experimental range. Shown.
3. **QH-mode** (§2.1, Fig. 2). Simulations recover the edge harmonic
   oscillation and the loss of the regime to large ELMs at higher pedestal
   density; "$q_{95}$ windows are found within which QH-mode can exist".
   A non-linear drop of $q_{95}$ (current redistribution including the
   self-consistent bootstrap current) reduces growth rates and acts as a
   saturation mechanism. Shown (Fig. 2) / Attributed (mechanism).
4. **Free-boundary RMP response** (§2.2). The JOREK–STARWALL RMP model
   "was shown to recover experimental flux surface corrugation
   accurately". Attributed.
5. **Pedestal-top island** (§2.2). Experimental evidence of a pedestal-top
   island in ELM-suppressed ASDEX Upgrade plasmas, with simulations
   reproducing the local bump in flux-surface corrugation (cited work
   "submitted"). Attributed.
6. **Tungsten transport with RMPs** (§2.2). Hybrid kinetic–fluid
   simulations show a substantial increase of radial tungsten transport
   for sufficiently high RMP coil currents. Attributed.
7. **KSTAR pump-out and suppression** (§2.2, Fig. 3). An electron
   polarization-drift and neoclassical-toroidal-viscosity extension
   recovers the density pump-out, explained by step-wise growth of the 5/1
   and 6/1 islands; island-mediated mode coupling reproduces RMP ELM
   suppression. Shown.
8. **HL-2A and ITER RMPs** (§2.2). HL-2A simulations agree with the
   experimental mitigation threshold (private communication); ITER
   predictions indicate suppression within coil-current limits.
   Attributed.
9. **Pellet triggering** (§2.3). A lag time after an ELM, during which
   triggering fails, is recovered; peak heat-flux reduction is limited
   because a smaller wetted area cancels part of the smaller-ELM benefit,
   as seen experimentally (Wenninger et al.). Attributed.
10. **Kinetic neutrals** (§2.4, Fig. 4). ITER 5 MA H-mode (PFPO-1,
    detached) shows a high-field-side high-density structure, with a role
    for $\mathbf E\times\mathbf B$ drifts in the scrape-off layer. Shown.
11. **3D VDE benchmark** (§3.1). JOREK–STARWALL has been benchmarked for 3D
    VDEs against other codes ([Artola et al. (2021)](/sources/artola-2021.md));
    no agreement figures are restated. Attributed.
12. **ASDEX Upgrade hot VDE** (§3.1, Fig. 5). With vertical control off,
    simulations reproduce the vertical motion, the halo-current magnitude,
    the vertical-force magnitude and the thermal-quench onset; $I_p$,
    $I_{\mathrm{halo}}$ and TPF match the experiment for suitable values of
    the temperature below which the $T$-dependence of $\kappa_\parallel$ is
    cut off, which strongly affects the evolution. Shown.
13. **COMPASS halo region** (§3.1, Fig. 6). The ion saturation current in
    the boundary conditions controls the poloidal extent of the halo
    region. Shown.
14. **ITER unmitigated thermal quench** (§3.1). Predicted "to the range of
    20 ms". Attributed.
15. **ITER β-limit disruptions** (§3.1). A dominant $n=1$ internal kink
    evolves into a disruptive state (MSc thesis). Attributed.
16. **JOREK–CARIDDI** (§3.1, Fig. 7). Two-way coupling to the volumetric
    eddy-current code CARIDDI is implemented and benchmarked for eddy
    currents; a non-axisymmetric wall induces mode coupling; halo-current
    and full-MHD coupling are ongoing. Shown.
17. **Collisional-radiative SPI** (§3.2, Fig. 8). The collisional-radiative
    treatment that replaces coronal equilibrium is benchmarked
    ([Hu et al. (2021b)](/sources/hu-2021-b.md)); in ITER Ne–D SPI, shards
    can reach the core before the edge radiative collapse, stochastic field
    lines outside $q=1$ form a transient transport barrier early in the
    thermal quench, and core density transport depends on the deposition
    relative to $q=1$ and $q=2$. Shown.
18. **Pre-existing islands** (§3.2). The response to massive D injection
    depends on the injection phase relative to the island. Attributed.
19. **JET, ASDEX Upgrade, KSTAR SPI** (§3.2). JET D and mixed SPI
    simulations reproduce key radiation observations, with plasmoid drifts
    essential for assimilation; ASDEX Upgrade SPI reproduces the double
    radiation peak qualitatively; KSTAR runs, with a deposition area
    enlarged "for numerical reasons", agree on density and qualitatively
    on bolometry. Attributed.
20. **ITER current quench** (§3.3, Fig. 9). At realistic post-quench
    parameters, mitigation reduces global wall forces; MHD activity
    persists through the current quench; runaway losses and trapping are
    analysed. Shown (Fig. 9) / Attributed.
21. **Vertical-force mitigation mechanism** (§3.3, Fig. 10). Massive
    impurity injection makes temperatures inside and outside the
    separatrix comparable, so substantial current flows in the
    scrape-off layer; because $q_{95}$ has increased, these currents are
    mainly toroidal; the current centroid decouples from the axis motion
    and its smaller excursion "is responsible for the vertical force
    reduction", consistent with only moderate poloidal halo currents;
    broadened halo patterns are seen in simulations and experiments
    (ASDEX Upgrade, JET, ITER). Shown.
22. **Current spike** (§3.4, Fig. 11). The $I_p$ spike comes from
    current-profile relaxation driven partly by shear-Alfvén-wave
    propagation in the stochastic field (Boozer's mechanism, flattening
    $j_\parallel/B$) and partly by a macroscopic $\mathbf E\times\mathbf B$
    flow mixing the core; the results "seem quantitatively consistent with
    Boozer's theory", but the second mechanism complicates the picture.
    Shown.
23. **Runaway avalanche and vertical motion** (§3.5). Vertical motion in the
    ITER current quench substantially reduces the avalanche gain relative
    to simulations without it, "although the avalanche gain remains very
    large". Attributed.
24. **Double tearing mode** (§3.5, Fig. 12). Lower resistivity gives faster
    growth of secondary modes and earlier stochasticity at the same
    main-mode amplitude ($\eta=10^{-5}$ vs $10^{-6}$ in JOREK units, main
    mode $m/n=4/1$). Shown.
25. **Stellarators** (§4.1). A virtual-current model (axisymmetric geometry
    with an approximated external rotational transform); JOREK3D's
    stellarator reduced MHD benchmarked linearly for classical
    stellarators ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md)); VMEC
    and JOREK agree qualitatively on saturated external modes with the same
    dominant $n$, but magnetic-energy spectra and topology can differ
    through coupling to internal modes and non-ideal effects. Attributed.
26. **Energetic particles** (§4.2). A full-$f$ energetic-particle model
    coupled through anisotropic pressure is benchmarked linearly
    ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md)) and compared with
    the ASDEX Upgrade NLED scenario. Attributed.
27. **Particle-in-cell turbulence** (§4.3). Gyrokinetic and fully kinetic
    electrostatic models agree closely for the Cyclone base case and a
    COMPASS-like pedestal; in some regimes the gyrokinetic model and the
    Padé approximation "differ substantially from the fully kinetic
    model"; RMPs enhance turbulence in ITER and HL-2A. Attributed.
28. **Flux pumping** (§4.4). A 1/1 quasi-interchange keeps $q_0\ge1$ for
    sufficiently peaked pressure, preventing sawteeth and hence an NTM
    seed; a quasi-linear expression for the current redistribution is
    derived in the cited work. Attributed.
29. **Numerics** (§5). Retaining non-linear toroidal-harmonic couplings in
    the preconditioner speeds up convergence; arbitrary-order Bézier
    elements give "speed-up or better stability depending on the
    application"; shock capturing enables highly non-linear mitigated
    disruption studies in full MHD "which were previously not possible"
    ([Bhole et al. (2023)](/sources/bhole-2023.md)). Attributed.

# Models and numerics

No governing equations are printed (checked on the rendered pages). The
review states:

* **Model hierarchy.** Reduced and full MHD, each with "model families"
  that toggle extensions (neutrals, impurities, runaway electrons);
  extended-MHD effects for pedestal work with a self-consistently evolved
  bootstrap current; an electron-polarization-drift and
  neoclassical-toroidal-viscosity extension for RMP pump-out;
  temperature-dependent anisotropic heat conduction with a scrape-off-layer
  cut-off temperature below which the $T$-dependence of $\kappa_\parallel$
  is frozen.
* **Impurities.** Coronal equilibrium replaced by a collisional-radiative
  non-equilibrium treatment; particle-in-cell injected impurities
  (axisymmetric tests so far); kinetic tungsten in a hybrid kinetic–fluid
  approach.
* **Neutrals.** Kinetic neutral extension for scrape-off layer and
  divertor ([Korving et al. (2023)](/sources/korving-2023.md)).
* **Runaway electrons.** Fluid model coupled self-consistently to MHD;
  equilibria with a runaway beam; full-$f$ kinetic runaways with two-way
  pressure or current coupling in development; synthetic synchrotron
  diagnostic.
* **Energetic particles.** Full-$f$ model with anisotropic pressure
  coupling; kinetic thermal ions in progress.
* **Turbulence.** Electrostatic particle-in-cell with fully kinetic or
  gyrokinetic ions (Padé approximation mentioned) in X-point geometry.
* **Stellarators.** Virtual-current model in axisymmetric geometry;
  JOREK3D with an adapted reduced MHD model.
* **Space discretization.** Finite elements generalized from bi-cubic
  Hermite–Bézier to arbitrary-order $G$-continuous Bézier elements;
  regularization of the grid at the magnetic axis; stabilized,
  shock-capturing Hermite–Bézier FEM for reduced and full MHD. Toroidal
  harmonics are implied, not described. Time integration is not
  described.
* **Solvers.** GMRES plus a new BiCGSTAB option; a preconditioner that
  keeps some non-linear couplings of toroidal harmonics; spectral analysis
  of the original and preconditioned systems.
* **Walls and boundaries.** Free boundary through JOREK–STARWALL (thin wall)
  for RMPs and VDEs; two-way JOREK–CARIDDI coupling to volumetric 3D
  conductors (integral eddy-current formulation;
  [Isernia et al. (2023)](/sources/isernia-2023.md)); compression of the
  wall-coupling matrices; sheath conditions including the ion saturation
  current for halo currents.
* **Parallelism and infrastructure.** Kinetic and gyrokinetic particles
  ported to GPUs with OpenACC; an OpenMP offload approach under study;
  IMAS adaptation with lossless storage of the finite-element
  representation; JOREK–RaySect radiation workflow; MUSCLE3 coupling;
  expanded regression tests. Marconi-Fusion and JFRS-1.
* No resolutions or run costs are given.

# Tests and results

* **Benchmarks cited:** the 3D VDE benchmark with M3D-C1 and NIMROD; the
  JOREK–CARIDDI eddy-current benchmark on an ASDEX-Upgrade-like artificial
  vessel with one hole (Fig. 7); the collisional-radiative impurity
  benchmark; full-$f$ energetic-particle linear benchmarks; the Cyclone
  base case (gyrokinetic vs fully kinetic); JOREK3D linear benchmarks for
  classical stellarators and in the tokamak limit.
* **Validation cases:** ASDEX Upgrade hot VDE ($I_p$, $I_{\mathrm{halo}}$,
  TPF; Fig. 5); COMPASS VDE halo currents (Fig. 6, at axis height
  $Z=-0.27$ m); KSTAR pump-out versus coil current (Fig. 3); ASDEX Upgrade
  EDA (Fig. 1) and QH-mode (Fig. 2); JET argon gas-injection current spike
  (Fig. 11, snapshots at 5.26, 5.72, 5.99, 6.69 ms); JET, KSTAR and ASDEX
  Upgrade SPI; JET benign runaway termination; ASDEX Upgrade NLED.
* **Numbers:** ITER unmitigated thermal quench of about 20 ms; ITER
  PFPO-1 electron-temperature contours at 1, 10, 50 eV (Fig. 4); Fig. 9
  field lines traced for 1000 poloidal turns; double tearing at
  $\eta=10^{-5}$ and $10^{-6}$ (JOREK units). No tables, growth rates or
  tabulated quantities.

# Notation map

The review prints no equations; the symbols below come from prose and
figure captions.

| Hoelzl et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $m$, $n$, $m/n$ | $m$, $n$, $m/n$ | |
| $q$, $q_{95}$, $q_0$ | $q$, $q_{95}$, $q_0$ | |
| $I_p$ | $I_p$ | |
| $I_h$ | $I_{\mathrm{halo}}$ | poloidal halo current |
| TPF | $\mathrm{TPF}$ | |
| $T_{e,\chi_\parallel}$ | words (cut-off temperature of the $T$-dependence of $\kappa_\parallel$) | value not given |
| $j_\phi$, $j_\parallel/B$ | $j_\phi$, $j_\parallel/B$ | normalization not stated |
| $E\times B$ | $\mathbf E\times\mathbf B$ drift | |
| $\eta$ | $\eta$ | JOREK normalized units, not defined in the review |
| $\psi_n^{1/2}$ | $\sqrt{\psi_N}$ | $2\pi$ convention not given |
| $\theta$ | $\theta$ | poloidal angle of Fig. 12 |
| $Z_{\rm axis}$ | words (axis height) | |
| $l$ | words (poloidal period number of an $l=2$ stellarator) | |

# Pages created or updated

Chunk 1 (2026-10-16) created every page of the bundle. This source is cited on:

* [Bootstrap current and its MHD implementation](/definitions/bootstrap-current.md)
* [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md)
* [CARIDDI](/software/cariddi.md)
* [Collisional-radiative (non-equilibrium) impurity model](/methods/collisional-radiative-impurity-model.md)
* [Coronal-equilibrium impurity model](/methods/coronal-equilibrium-impurity-model.md)
* [Disruption: phases, current quench and current spike](/definitions/disruption.md)
* [Edge-localized mode (ELM) and ELM-free regimes](/definitions/edge-localized-mode.md)
* [Electromagnetic wall forces (vertical and sideways)](/definitions/wall-forces.md)
* [Fishbone instability](/definitions/fishbone.md)
* [Free-boundary and resistive-wall coupling](/methods/resistive-wall-coupling.md)
* [Halo current](/definitions/halo-current.md)
* [High-field-side high-density region](/results/high-field-side-high-density-region.md)
* [Hybrid kinetic-MHD models](/methods/hybrid-kinetic-mhd.md)
* [Implicit time integration and preconditioned Krylov solvers for nonlinear MHD](/methods/implicit-time-integration.md)
* [JOREK](/software/jorek.md)
* [JOREK3D](/software/jorek3d.md)
* [Kinetic (Monte Carlo) neutral model coupled to MHD](/methods/kinetic-neutral-model.md)
* [NSTX VDE benchmarks of JOREK, M3D-C1 and NIMROD (axisymmetric and 3D)](/benchmarks/nstx-vde-benchmarks.md)
* [Reduced MHD for stellarators](/methods/stellarator-reduced-mhd.md)
* [Reduced-MHD boundary condition suppresses the toroidal asymmetry of the plasma current](/results/reduced-mhd-current-asymmetry.md)
* [Resistive internal kink (m/n = 1/1)](/definitions/resistive-internal-kink.md)
* [Resistive tearing mode](/definitions/tearing-mode.md)
* [Runaway electrons and their generation mechanisms](/definitions/runaway-electrons.md)
* [Runaway-electron fluid model coupled to MHD](/methods/runaway-electron-fluid-model.md)
* [Shattered pellet injection and massive material injection](/definitions/shattered-pellet-injection.md)
* [Sheath (Bohm) boundary conditions](/methods/sheath-boundary-conditions.md)
* [Shock-capturing artificial viscosity for MHD finite elements](/methods/shock-capturing-artificial-viscosity.md)
* [STARWALL](/software/starwall.md)
* [Thermal quench](/definitions/thermal-quench.md)
* [Three-dimensional inverse equilibrium solvers](/methods/inverse-equilibrium-solvers.md)
* [Variational multiscale (VMS) stabilization for MHD finite elements](/methods/variational-multiscale-stabilization.md)
* [Vertical displacement event (hot and cold VDE)](/definitions/vertical-displacement-event.md)
* [Vertical-force mitigation by massive material injection](/results/vertical-force-mitigation.md)
* [VMEC](/software/vmec.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2024_Crossref_Nuclear_Fusion_Hoelzl_Non-linear_MHD_modelling_of_transients_in_tokamaks_a_review.pdf`
   * **Version.** Publisher version of record (IOP, open access, CC BY
     4.0), 14 article pages plus an IOP cover sheet (15 PDF pages); received
     26 January 2024, accepted 20 June 2024, online 11 September 2024.
   * **Identity.** doi:10.1088/1741-4326/ad5a21, checked on Crossref:
     Nucl. Fusion 64(11), article 112016, issue 1 November 2024; 62
     authors, first author Hoelzl M.; 89 references; all match the PDF.
   * **How read.** Full text and all figure captions; the absence of
     displayed equations was checked on the rendered pages.
   * **Recorded as printed.**
     * Fig. 5 caption: "Reproduced from [32]" (an IAEA FEC 2023
       contribution), while the text describing the same ASDEX Upgrade
       hot-VDE validation cites [35] (PPCF 65:054003); possible citation
       mismatch.
     * Refs. [38] (EPS 2023) and [39] (PPCF 2024) share the title
       "Modelling of vertical displacement events in tokamaks: status and
       challenges ahead" with slightly different author lists; they are
       distinct works.
     * Ref. [80] (EPS 2023, linear ITG stability) is cited both for the
       particle-in-cell turbulence benchmark (§4.3) and for the OpenACC GPU
       port (§5), which its title does not cover.
     * The abstract mentions ongoing predictive "JT60-SA" simulations
       (ref. [6] title: "JT-60SA"); the body does not discuss them.
     * Name variants in the reference list: Huysmans/Huijsmans,
       Bergström/Bergstroem, Särkimäki/Saerkimaeki, Artola J./Artola F.J.
     * Formatting glitches in refs. [5], [16], [18] (unclosed team
       parenthesis containing the year), [42], [43], [49] ("and et al"),
       [53], [80]; typos "connection lenghts" (§3.3); redundant wording in
       §3.1 and §4.3; affiliation numbering out of order (7 before 6).
     * Ref. [17] is "submitted"; refs. [13], [20], [48], [60] are private
       communications; ref. [40] is a Master thesis without URL.
   * **Reference list.** 89 printed entries, no DOIs printed, merged into
     the bibliography under `hoelzl-2024`. Key decisions: its
     "Artola et al. 2021" COMPASS paper (PPCF 63:064004, ref. [33]) is
     `artola-2021-b`, while the 3D VDE benchmark (ref. [34]) is the ingested
     `artola-2021`; its citation of the collisional-radiative impurity
     paper (PPCF 63:125003, ref. [42]) is the ingested `hu-2021-b`;
     Bandaru et al. NF 64:076053 (ref. [63]) is `bandaru-2024-b`, not the
     ingested `bandaru-2024`; Cathey's thesis (ref. [9]) is `cathey-2021-c`
     and the PPCF paper is `cathey-2021`; Schwarz FEC 2023 (ref. [32]) is
     `schwarz-2023-b`, the PPCF paper (ref. [35]) `schwarz-2023`; the
     private communications of Wang L. (ref. [20]) and Wang C. (ref. [60])
     are `wang-2024-c` and `wang-2024-d`. Other ingested works it cites:
     `hoelzl-2021`, `isernia-2023`, `korving-2023`, `bhole-2023`,
     `bogaarts-2022`, `nikulsin-2022`.

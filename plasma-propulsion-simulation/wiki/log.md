# Directory Update Log

## 2026-10-15

* **Human rulings (2026-10-15)** on decisions recorded in `INGESTION-ISSUES.md`:
  * `voland-2005` → `voland-2006` (Crossref doi:10.1016/j.actaastro.2006.02.021,
    print July 2006), also in the two bundles that share the key.
  * Preprints are kept as distinct bibliography entries, not folded into
    their published versions: `hippke-2017-f` (the arXiv form of
    [hippke-2018-b](/sources/hippke-2018-b.md), cited by hippke-2018),
    `learned-2008` (arXiv form of `learned-2012`) and `lubin-2016-b` (the
    JBIS version cited by semyonov-2018; `lubin-2016` stays the arXiv
    preprint). The bibliography entry `hippke-2018-b`, which existed only
    through the fold, is gone (nothing cites the published paper).
    4084 → 4086 entries.
  * The contradiction "first GPU PIC simulation of a plasma thruster"
    ([GPU acceleration](/methods/gpu-acceleration-of-pic.md)) is closed by
    human fiat against Gallo et al.'s priority claim; the closure is
    hypothesis-grade. Two contradictions remain Open.
  * Orphan warnings: the lint now exempts Source pages tagged `context`
    (DECISIONS.md D24); the bundle's 85 orphan warnings drop to 3
    (gomezjenkins-2018, garciagarrido-2018, yang-2018, full ingestions
    awaiting a second source).

* **Deep lint #2** (all 43 concept pages, the notation registry and the root
  index; 2026-10-15), applied with chunk 6:
  * **Error fixed:** [cross-field mobility](/definitions/electron-mobility-and-hall-parameter.md)
    misstated Reza et al.'s Hall parameter (it is $\omega_{ce}/\nu_{\mathrm{ano}}$,
    not $\Omega_e$); [reza-2022](/sources/reza-2022.md) aligned.
  * **Notation:** unregistered $U$, $Q$ and paper-native $C$, $c_k$ removed
    from concept pages; the §1 comma rule now exempts registered multi-index
    symbols; $\mathrm{Re}_m$ (magnetic Reynolds number) added to §7.
  * **Fidelity and wording:** ten smaller fixes (SEE and near-wall energy
    units, ECCOPIC2S-M, the EX-PWS over-prediction, the anomalous-transport
    median label, axis labels, compiler notes on two qualifications).
  * **Tags:** `review` and `software` dropped from concept pages; 11 Source-page
    tags merged into canonical forms (e.g. `uq`, `small-satellite`,
    `deployable-structure`); cross-tags added to the two chunk-3 pages.
  * The three Open contradictions re-verified; the GPU-priority entry still
    awaits the human's closure.
  * Pages touched: notation, electron-mobility-and-hall-parameter,
    secondary-electron-emission, near-wall-conductivity,
    anomalous-electron-transport, electron-drift-instability,
    current-free-double-layer, hall-effect-thruster,
    polytropic-electron-closure, ion-beam-shepherd, monte-carlo-collisions,
    implicit-and-energy-conserving-pic, hybrid-pic-fluid-model,
    electron-fluid-model, five-moment-fluid-model, boltzmann-electron-model,
    gpu-acceleration-of-pic, pic-mcc, instability-enhanced-friction-force,
    magnetized-body-plasma-drag, reza-2022, and the tags of 12 Source pages.

* **Chunk 6: the last 7 Source-only pages** (D23): yamaguchi-2018,
  yang-2018-b, yu-2018, yuan-2018, zhang-2018-b, zhang-2018-c, zhao-2018-b,
  outside this bundle's domain (yamaguchi-2018 reports Hayabusa2 ion-engine
  operating figures as mission context only). No concept page created. The
  archive is complete: 108 of 108 ingested.
  * **Bibliography:** 7 reference lists merged with `tools/bib_merge.py`
    (FLAGS 0), 3899 → 4084 entries. Closing sweeps over the whole
    bibliography: `--dupes` 0 groups, cross-year fuzzy-title sweep 51
    candidate pairs all distinct works, no shared DOI across keys; no
    corpus-wide merge needed.

* **Chunk 5: 20 Source-only pages** (D23): meng-2018-b, miller-2018, mu-2018,
  nies-2018, pallone-2018, perez-2018, pestrenin-2018, sabatini-2018,
  semyonov-2018, unknown-2018, verspieren-2018, volpe-2018, wang-2018,
  wang-2018-b, wang-2018-e, wang-2018-f, wu-2018, wu-2018-b, wu-2018-c,
  xu-2018, all outside this bundle's domain: each has a Source page tagged
  `context` and its reference list. No concept page created or changed.
  * **Front matter:** [unknown-2018](/sources/unknown-2018.md) is the issue's
    inside front cover (publication information, editorial board), recorded
    as a `report` with no reference list; it stays in `--pending` by design.
  * **Bibliography:** before the merge, the cited-work entry `wu-2018` (Acta
    Astronaut. 149:11) was re-keyed to `wu-2018-d`, freeing the slug of a
    chunk-5 paper. 19 reference lists merged with `tools/bib_merge.py`
    (FLAGS 0, `--dupes` clean), 3360 → 3899 entries.

* **Chunk 4: 20 Source-only pages** (D23): ghassabian-2018, haley-2018,
  helman-2018, hippke-2018, hippke-2018-b, hou-2018, huang-2018, huang-2018-b,
  huang-2018-c, joffre-2018, ke-2018, kim-2018, kumar-2018, lemay-2018,
  li-2018-b, li-2018-c, liu-2018, liu-2018-b, loureiro-2018, mcdowell-2018,
  all outside this bundle's domain: each has a Source page tagged `context`
  and its reference list. No concept page created or changed (scope rule).
  * **Identity:** the file filed under "Hady" is by Ghassabian et al. (page 1
    prints every name surname-first; Crossref swaps given and family names
    for all six authors), slug `ghassabian-2018`; the file filed under "Le" is by Le May et
    al. (Crossref family name), slug `lemay-2018`.
  * **Bibliography:** before the merge, the cited-work entries `kim-2018`
    (New J. Phys. 20:063033) and `liu-2018` (Rev. Sci. Instrum. 89:043502)
    were re-keyed to `kim-2018-b` and `liu-2018-e`, freeing the slugs of two
    chunk-4 papers. 20 reference lists merged with `tools/bib_merge.py`
    (FLAGS 0, `--dupes` clean), 2738 → 3360 entries. hippke-2018's citation of
    a different 2018 arXiv paper is `hippke-2018-c`; its citation of the arXiv
    preprint of hippke-2018-b is merged into that ingested paper.

* **Chunk 3: five plasma-related papers in full, 15 Source-only pages** (D23).
  Read by 20 reader agents into scratch notes, drafted by five drafters from
  the notes only, installed by the compiler, audited read-only before staging.
  * **In full:** [alpatov-2018](/sources/alpatov-2018.md) and
    [shuvalov-2018](/sources/shuvalov-2018.md) seed two concept pages:
    [ion-beam shepherd](/definitions/ion-beam-shepherd.md) (also citing
    takahashi-2019 and cai-2018) and
    [plasma drag augmentation of a magnetized body](/results/magnetized-body-plasma-drag.md).
    [gomezjenkins-2018](/sources/gomezjenkins-2018.md),
    [garciagarrido-2018](/sources/garciagarrido-2018.md) and
    [yang-2018](/sources/yang-2018.md) are full Source pages that no concept
    page cites yet: none of their contributions meets the granularity rule
    (each page says why).
  * **Source-only (tag `context`):** ahmad-2018, an-2018, antoni-2018, bu-2018,
    cai-2018-b, cerf-2018, conte-2018, crusan-2018, delchambre-2018,
    dhara-2018, dong-2018, gagg-2018, grieve-2018, guo-2018,
    gomezsanjuan-2018.
  * **Identity:** the archive file filed under "Gomez" is by Gomez Jenkins,
    Krejci & Lozano (Crossref family name "Gomez Jenkins"); slug
    `gomezjenkins-2018`, not the planned `gomez-2018`.
  * **Notation registry extended** ([notation](/notation.md) §7, plasma–body
    interaction): $C_D$, $C_{D0}$, $p_{\mathrm{dyn}}$, $p_{Bw}$, $B_w$,
    $r_w$, $L_{\mathrm{so}}$, $F_{\mathrm{IT}}$, $F_{\mathrm{CT}}$.
  * **Bibliography:** 20 reference lists merged with `tools/bib_merge.py`
    (FLAGS 0, `--dupes` clean), 2130 → 2738 entries. Citations keyed with
    their citing paper's own slug were re-keyed (`bu-2018-d`, `an-2018-b`,
    `conte-2018-b`); cai-2018-b's IAC 2017 conference version is a separate
    entry (`cai-2017-c`); the existing key `voland-2005` carries a wrong year
    (Crossref: 2006), merged under it pending the human's re-key.
  * Source pages whose audit list changed: [cai-2018](/sources/cai-2018.md),
    [takahashi-2019](/sources/takahashi-2019.md).

## 2026-10-14

* **Chunk 2: 21 Source-only pages** (D23): knight-2018, liu-2018-c, liu-2018-d,
  meng-2018, moradi-2018, wang-2018-d, zhao-2018, zuo-2018, fedele-2018,
  cheng-2018 (high-speed aerothermodynamics) and armbruster-2018, bai-2018,
  peng-2018, zhou-2018, song-2018, wang-2018-c, yan-2018, ye-2018, veale-2018,
  li-2018, greer-2018 (chemical and air-breathing propulsion), all outside this
  bundle's domain: each has a Source page tagged `context` and its reference
  list. No concept page created or changed (scope rule).
  * **Bibliography:** 21 reference lists merged with `tools/bib_merge.py`
    (FLAGS 0, `--dupes` clean), 1437 → 2130 entries. Cited works whose natural
    key equals a slug reserved for another Acta vol. 151 file were re-keyed past
    it (e.g. `zhang-2018-d`…`-i`, `li-2018-d`…`-f`); zhao-2018's citation of
    "Mosavat 2018" is the ingested moradi-2018 (Crossref).

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

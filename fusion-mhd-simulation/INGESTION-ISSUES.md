# Ingestion issues — fusion-mhd-simulation

Reviewer's digest, one section per chunk, newest first: contradictions
opened (the normative record is the `## Contradictions` section of the
named page), printed inconsistencies, identity and metadata problems,
bundle-fit suggestions, and questions left to the human. Not part of the
OKF wiki; maintained by the compiler at every chunk.

## Chunk 1 — scaffold (D25) and the 20 code, method, benchmark and review papers (2026-10-16)

Sources: artola-2021, bandaru-2024, bhole-2023, bogaarts-2022,
hoelzl-2021, hoelzl-2024, hu-2021-b, isernia-2023, jiang-2024,
korving-2023, liu-2022, liu-2024, ma-2022, nikulsin-2022, panici-2023,
saxena-2025, seto-2023, taheri-2022, vlad-2025, zhang-2021.
75 concept pages, 20 Source pages, 905 bibliography entries.

### Decisions for the human

1. **Close by fiat as printed slips** (recommended):
   * *Order of JOREK's Gear scheme* ([implicit time integration](wiki/methods/implicit-time-integration.md)):
     artola-2021 (arXiv v1, §2 and Table 1) prints "BDF5 Gears"; hoelzl-2021,
     bhole-2023 (Eq. 40) and korving-2023 give BDF2, and the three-level
     scheme is BDF2 by construction.
   * *Sign of the resistive term in the JOREK flux equation*
     ([reduced MHD](wiki/methods/reduced-mhd.md)): hoelzl-2021 Eq. 28 and
     nikulsin-2022 Eq. 3d print an anti-diffusive sign; hu-2021-b Eq. 8,
     bandaru-2024 Eq. 2.3 and the compiler's derivation give the diffusive one.
2. **Keep open or rule** (two sources disagree on a description):
   * *Sideways-force agreement in the 3D NSTX VDE benchmark*: artola-2021
     says "good agreement in magnitude" (peaks 2.5–3.5 kN; the compiler's
     Fig. 8 readings give NIMROD ≈0.74 of JOREK); hoelzl-2021 §4.8 summarizes
     the same benchmark as "factor 2 smaller in NIMROD". hoelzl-2021 also
     writes the wall condition as $\Phi=0$ where artola-2021 has $\Phi=$ const.
   * *Continuity class of the JOREK element* ($G^1$ in hoelzl-2021,
     artola-2021, nikulsin-2022; $C^1$ in bhole-2023): on regular nodes the
     two describe the same continuity in different coordinates; the real
     difference is at the axis and at X-point nodes, where hoelzl-2021 says
     continuity is not enforced and bhole-2023 is silent.
3. **Version caveats** to be aware of when citing: 8 of the 20 files are
   preprints, not versions of record: artola-2021, bhole-2023 (HAL
   pre-review, 66 of the published 75 references), bogaarts-2022,
   hoelzl-2021, hu-2021-b, liu-2022, nikulsin-2022 (an unseen Publisher's
   Note, doi:10.1063/5.0124567, postdates it) and taheri-2022 (whose Eq. 34
   is identically zero as typeset). Equation and figure numbers on their
   Source pages are those of the preprint.

### Contradictions opened (all Open)

| Name | Page(s) |
|---|---|
| Continuity class of the JOREK element | methods/bezier-finite-elements, software/jorek |
| Order of JOREK's Gear scheme | methods/implicit-time-integration, software/jorek |
| Sign of the resistive term in the JOREK flux equation | methods/reduced-mhd |
| Sideways-force agreement, 3D NSTX VDE | definitions/wall-forces, benchmarks/nstx-vde-benchmarks, software/nimrod |
| $I_p$ toroidal asymmetry in the full-MHD codes (factor ≈3 between M3D-C1 and NIMROD; 10–20 % in experiment) | results/reduced-mhd-current-asymmetry, benchmarks/nstx-vde-benchmarks |
| Pressure vs current coupling: analytic equivalence (liu-2022 Eq. 25) vs observed behaviour (bogaarts-2022 "too noisy", vlad-2025 MEGA discrepancy) | methods/pressure-and-current-coupling |
| EPM vs TAE labelling of the AUG-NLED $n=1$ mode; TAE vs EPM and RSAE vs EPM inside bogaarts-2022 (Table I vs Fig. 16) | definitions/energetic-particle-mode, definitions/reversed-shear-alfven-eigenmode, definitions/toroidal-alfven-eigenmode |
| Chirping direction (down in HYMAGYC/MEGA, up in ORB5); frequency trend with EP gradient (JOREK vs HYMAGYC/MEGA) | benchmarks/nled-aug-benchmark |
| Coronal-equilibrium thermal-collapse delay: size and attribution | methods/coronal-equilibrium-impurity-model, benchmarks/diii-d-mgi-impurity-benchmark |
| Dreicer source in the JOREK runaway-electron model (described in hoelzl-2021 §4.7, absent per bandaru-2024; model versions) | methods/runaway-electron-fluid-model |
| JOREK–DINA seed discrepancy (0.1–1 A vs 3.8 kA, same plateau) | benchmarks/iter-runaway-electron-benchmarks |
| Sign of the fourth-order regularization in particle projection (hoelzl-2021 Eq. 48 vs korving-2023 Eq. 23) | methods/particle-to-mesh-projection |
| JOREK kinetic neutrals vs SOLPS-ITER (power within 10 %, peak heat flux ≈2×) | methods/kinetic-neutral-model |
| Low-$n$ ballooning overestimate of flute-ordered BOUT++ (indirect evidence) | benchmarks/cbm18-ballooning-benchmark, software/bout-plus-plus |
| JOREK3D vs CASTOR3D (13.2 %, 26.2 % tearing; 6.4 % ballooning) | software/jorek3d |

Qualifications (not contradictions): the tearing and kink scaling
exponents printed by zhang-2021 are low-$\eta$ fits (the compiler's
log–log fits of its tables: 0.54/0.51 over all points, 0.60–0.65 over
the lowest three or four; kink 0.285/0.281 vs 0.313/0.301); its "about
10 %" agreement hides 24 % at $\eta=10^{-7}$; the current-spike mechanism
in hoelzl-2024 (Boozer's shear-Alfvén relaxation plus an $\mathbf E\times\mathbf B$
mixing flow).

### Printed inconsistencies (selection; full lists on the Source pages)

* hoelzl-2021: §4.4 "m=n=1 tearing mode" vs Fig. 18 caption 2/1; p. 19
  $j=FF'+R^2p'$ with the sign that defeats the claimed cancellation; three
  references printed twice; bad DOIs in [104], [119], [158].
* artola-2021: NIMROD resolution $n\le20$ vs $n\le21$; Table 2 units
  "(ms)⁻¹" meaning (m s)⁻¹; ref. [6] carries an OSTI report DOI.
* zhang-2021: Fig. 7 linear-phase $\gamma$ ≈1.45×10⁻³ vs Table 1 0.00165/0.00178;
  undefined $q_0'$, $q_e'$.
* bhole-2023: Eq. 1 sign of $\mathbf v\times\mathbf B$; VMS $\tau$ with 8 coefficients
  for 9 unknowns; Ohmic heating in the source but absent from the model;
  Grad–Shafranov without $R^2$ on $p'$; thermal energy without 3/2.
* taheri-2022: Eq. 34 identically zero; Eq. 38 cancelling terms; "2×10¹² s".
* liu-2022: 16 M vs 4 M particles; $\mathbf E^\dagger$ without $1/q$; sign of the
  magnetization vs Eq. 27.
* jiang-2024: Eq. 60 $q_l$ inverted against Fig. 24.
* liu-2024: Eq. 9 twist-shift sign opposite to its definition of $z$;
  Figs. 3–5 "PF3D".
* korving-2023: Eq. 21 radiation as heat gain; Eqs. 26–27 weights swapped;
  Eq. 29 without mass; 0.8984 vs 8.984 ms.
* isernia-2023: Eq. 3 volume term $1/r^2$ (compiler: $1/r$); 0.2 % accuracy
  claim stronger than Figs. 2–3.
* saxena-2025: abstract credits the isomorphism to the wrong Landreman
  paper; sign mismatch A1/A2 vs 2.3; Eq. C5 heat-flux sign; $\ln\Lambda$
  printed $\Lambda$.
* seto-2023: Eq. A.12 $B_{t0}$ for $B_{p0}$; Eq. A.20 missing $\nu$; Eq. 37
  factor 2.
* panici-2023: Zernike index order swapped between Eqs. 3.17 and 3.18; force
  sign flips between (1.2) and (A8a).
* hu-2021-b: Eq. 4 loss term quadratic.
* bandaru-2024: $\beta$ defined as $p^2/(1+p^2)$; Eq. 2.8 $v_\parallel B^2$.
* nikulsin-2022: Eqs. 6–7 and $\Delta^*$ truncated in arXiv v3; Fig. 3 $\iota$
  values incompatible with the reported (2,1) surface.
* vlad-2025: FLR claim of §7 vs the HYMAGYC row of Table 2.

### Bibliography (0 → 905 entries, FLAGS 0)

* 1166 printed references from 20 fragments. Citations of ingested works
  under other keys mapped onto the Source slugs: the VDE benchmark
  (printed "submitted" in hoelzl-2021, `artola-2021-b` in hoelzl-2024) →
  `artola-2021`; the CR impurity paper (`hu-2021` in bandaru-2024 and
  hoelzl-2024) → `hu-2021-b`.
* Same key, different work: `bandaru-2024-b` (NF 64:076053), `artola-2021-b`
  (COMPASS PPCF), `artola-2020-b` (COMPASS Varenna 2020), `artola-2018-c`
  (thesis), `liu-2022-c` (P. Liu PRL), `cathey-2021-c` (thesis), and about
  twenty more in the merge's resolutions table.
* Folded: Hölzl/Hoelzl and Huijsmans/Huysmans spelling variants (three
  groups); "submitted" citations into their published entries
  (`nikulsin-2021`, `pamela-2022`, `holod-2021`, `cathey-2021`); a year
  variant (`strumberger-2017`). Kept distinct: conference and journal
  versions with the same title (artola-2023-b/artola-2024,
  konies-2012/konies-2018, dvornova-2018/2020, artola-2020-b/2021-b).
  **Question for the human:** the plasma-propulsion ruling keeps
  preprints distinct from their published versions; here "submitted"
  citations (not separate artefacts) were folded. Confirm, or ask for them
  to be split.
* Undated web resource: `adas-2023` (earliest citing year).
* `meier-2016`: korving-2023 prints the title of `sytova-2019`; kept with a note.

### Bundle-fit suggestions (the user's request)

Every one of the 50 files belongs in this bundle; none is misfiled. Some
would also serve another bundle as a D17 copy (copy the PDF into that
archive, ingest it there for that bundle's scope). None is made without
your decision.

**Existing bundles — D17 copies worth considering:**

| Paper | Candidate bundle | Why |
|---|---|---|
| bhole-2023 (stabilized Hermite–Bézier FEM: VMS + shock capturing) | `high-order-capturing-schemes` | a residual-based stabilization and pressure-sensor shock capturing for a high-order continuous FEM — that bundle's subject, outside finite volumes |
| jiang-2024, seto-2023, liu-2024 (field-aligned coordinates, twist-shift, shifted metric) | `curvilinear-metric-discretization` | metric tensors and coordinate shifts for strongly anisotropic transport; the integrated-shear cell deformation is a metric-discretization problem |
| panici-2023 (DESC, Fourier–Zernike basis, spectral convergence) | `orthogonal-polynomials-and-quadrature` | Zernike polynomials as a global basis with axis regularity; exponential vs algebraic convergence |
| liu-2022, zhang-2021 (OpenACC GPU ports) | `astrophysical-simulation-codes` | weak: that bundle's GPU scope is compressible flow; only the GPU sections overlap |

**New bundles worth considering:**

1. **`neural-operator-surrogates`** (scientific machine learning for PDE
   solvers): gopakumar-2024 (FNO surrogates of JOREK and MAST) and
   rahman-2024 (sparsified time-dependent FNOs for fusion simulations),
   both in chunk 3. Their method (Fourier neural operators trained on
   simulation data, error growth in rollouts) is a field with its own
   literature that this bundle's registry should not have to carry. Ingest
   them here for their fusion content, and found the new bundle on them if
   you plan further SciML reading.
2. **`stiff-time-integration`** (implicit, semi-implicit, IMEX and
   splitting schemes for stiff multiphysics PDEs): taheri-2022, the
   time-integration parts of hoelzl-2021 and bhole-2023, and the
   semi-implicit literature in this bibliography (Schnack 1987, Sovinec &
   King 2010, Knoll & Keyes 2004, Jardin 2012). Worth it only if you read
   time integration beyond MHD; otherwise the method pages here suffice.
3. **Not recommended:** splitting the ~10 energetic-particle / Alfvén
   papers (bogaarts-2022, liu-2022, liu-2022-b, liu-2024, jiang-2024,
   hezaveh-2022, sato-2024, sato-2026, vlad-2025) into a separate bundle.
   They are hybrid extensions of MHD codes; pressure/current coupling and
   the code families live in the MHD code literature, and a split would
   sever them from JOREK, M3D-C1 and the reduced-MHD pages. Likewise the
   stellarator cluster (nikulsin-2022, panici-2023, saxena-2025,
   zhou-2023, ramasamy-2024, wright-2024, sato-2026) stays here.

### Chunks 2 and 3 (planned)

Chunk 2 (20): the disruption, SPI, runaway-electron, ELM, tearing and
energetic-particle application papers — strauss-2022, hu-2021, liu-2021,
liu-2022-b (JPP fishbone), artola-2022, becoulet-2022, hezaveh-2022,
zeng-2022, howell-2022, cathey-2023, ebrahimi-2023, hu-2023,
mcdevitt-2023, nardon-2023, zhou-2023, cathey-2024, hu-2024, kong-2024,
ramasamy-2024, sato-2024. Chunk 3 (10): gopakumar-2024, rahman-2024,
seto-2024, wright-2024, tang-2025, vannini-2025, zhang-2025, izzo-2025,
liang-2025, sato-2026. Provisional slugs; identities are verified at
ingestion.

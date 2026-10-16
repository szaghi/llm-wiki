# Ingestion issues — fusion-mhd-simulation

Reviewer's digest, one section per chunk, newest first: contradictions
opened (the normative record is the `## Contradictions` section of the
named page), printed inconsistencies, identity and metadata problems,
bundle-fit suggestions, and questions left to the human. Not part of the
OKF wiki; maintained by the compiler at every chunk.

## Chunk 3 — the last 10 papers, closing sweeps and deep lint #1 (2026-10-16)

Sources: gopakumar-2024, rahman-2024, seto-2024, wright-2024, tang-2025,
vannini-2025, zhang-2025, izzo-2025, liang-2025, sato-2026 (no slug
changes). 10 new concept pages (110 in all, 160 with the Source pages),
about 40 pages extended, 1552 bibliography entries. 50 of 50 files
ingested.

### Decisions for the human

1. **Closures recommended as printed slips.** *Both closed by human fiat
   (2026-10-16) as printed slips, with `status: hypothesis` attribution on
   the pages.*
   - Resistive-term sign in the JOREK flux equation
     ([reduced MHD](wiki/methods/reduced-mhd.md)): now 8 sources print the
     diffusive sign against 3 (hoelzl-2021, nikulsin-2022, and liang-2025, which
     is internally mixed). Recommended: close as a printed slip.
   - Gear scheme order, "BDF5" in artola-2021 against BDF2 in four sources
     ([implicit time integration](wiki/methods/implicit-time-integration.md)).
     zhang-2025 gives no order and does not help. Recommended: close as a
     printed slip, or check the published version first.
2. **Fiat candidates raised by the deep lint:**
   - Bézier element continuity ([Bézier elements](wiki/methods/bezier-finite-elements.md)):
     four sources say $G^1$ (hoelzl-2021, artola-2021, zhang-2025,
     liang-2025) against one $C^1$ (bhole-2023). Most likely a difference of
     terminology. *Closed by human fiat (2026-10-16) as a difference of
     terminology; canonical label $G^1$.*
   - JOREK3D–CASTOR3D tearing gap: ramasamy-2024 re-attributes it to
     CASTOR3D resolution, with authors shared with the 2022 paper but no
     data. Supersede, or keep Open. *Kept Open by human decision
     (2026-10-16).*
3. **Reclassification candidates** (contradiction → qualification or
   compatible; the pages already say so). *All five downgraded to
   qualifications by human decision (2026-10-16); moved to the pages'
   `## Qualifications` sections.* EHO frequency
   ([EHO](wiki/definitions/edge-harmonic-oscillation.md)); the
   phase-space invariant $C$ vs $P_2$ during chirping
   ([EPM](wiki/definitions/energetic-particle-mode.md),
   [chirping diagnostic](wiki/methods/chirping-phase-space-diagnostic.md));
   complete RE loss vs trapped survivors after vannini-2025
   ([runaway electrons](wiki/definitions/runaway-electrons.md)); the SPI
   trigger surface, where tang-2025 supports the restricted reading, and the
   ITER TQ duration, an attributed contrast
   ([thermal quench](wiki/definitions/thermal-quench.md)).
4. **Tag vocabulary** (not changed, your call): `benchmark` (39) and
   `verification` (38) overlap heavily. The auditors split between merging
   them and keeping `benchmark` for Benchmark pages only. `code` (57)
   duplicates `type: Software`. `mhd` (69) sits alongside
   `full-mhd`/`reduced-mhd`. Applied: `surrogate` → `machine-learning`.
   *Decided (2026-10-16): `benchmark` only on Benchmark pages; the other
   31 pages carry `verification`. `code` dropped (57 pages); `mhd` removed
   where `full-mhd`, `reduced-mhd` or `extended-mhd` is present (33 pages).*
5. **Version caveats:** gopakumar-2024 is arXiv v2; seto-2024, tang-2025,
   vannini-2025 and zhang-2025 are preprints or accepted manuscripts. Claims
   are those of the versions read.

### Contradictions opened (all Open)

| Name | Page(s) |
|---|---|
| Tungsten melt limit in energy-impact units: 50 vs 38 MJ m⁻² s⁻¹ᐟ² | definitions/radiation-asymmetry |
| Double radiation peak in AUG SPI (tang-2025) | definitions/shattered-pellet-injection |
| Terms of the JOREK RE fluid model: vannini-2025 vs bandaru-2024 | methods/runaway-electron-fluid-model |
| Flux pumping with $q_0\approx0.99$ (zhang-2025) vs $q_0\ge1$ | definitions/magnetic-flux-pumping (pointers from interchange-mode, resistive-internal-kink, tearing-mode, neoclassical-tearing-mode) |
| Resistivity model of the QA reactor stellarator: saxena-2025 vs wright-2024 | definitions/quasi-symmetry, definitions/bootstrap-current |
| Interchange-like instability despite a magnetic well (wright-2024) | definitions/interchange-mode |

Qualifications recorded: SPI fragment speed (hu-2023 vs tang-2025);
vertical-force mitigation fails once a runaway beam carries the current
(vannini-2025); the fluid RE beam re-forms after the flush; EHO frequency,
liang-2025 vs cathey-2023/2024; the different context of sato-2026 and
ramasamy-2024 for stellarator β limits. Updated tallies on
[reduced MHD](wiki/methods/reduced-mhd.md): resistive sign 8 against 3,
viscous term 5 $R$ against 2 $R^3$.

### Printed inconsistencies and metadata

- The slips each reader found are recorded under "Recorded as printed" on
  the Source page.
- izzo-2025 cites "[Hu 2024]", which is not in its printed reference list.
  The link to hu-2024 is the compiler's inference.
- hoelzl-2024 claims 8 (ITER RMP predictions, probably becoulet-2022) and 25
  (VMEC–JOREK, probably ramasamy-2024) are left unlinked: the cited original
  cannot be confirmed.
- liu-2022-b: it remains open whether particles are pushed with $\mathbf E$
  or $\mathbf E^*$.
- nikulsin-2022 Fig. 3: the ι range is inconsistent with the (2,1) and
  (3,2) surfaces named in the text. Recorded as printed.
- tang-2025's 50 eV floor on $\chi_\parallel$ could be a temperature floor
  or a diffusivity floor. Recorded as ambiguous.

### Bibliography

- 1312 → 1552 entries, FLAGS 0.
- Aliases: `li-2020-c` (FNO), `li-2022-b` (PINO; rahman-2024 prints 2021),
  `kirk-2006-b`, `siccinio-2022-b`, `shi-2015-b`.
- `bergstroem-2023-b` is kept distinct from `bergstroem-2023`: different
  printed titles at the same workshop, possibly the same contribution.
- **Chunk-1 repair:** hoelzl-2021's citation of Zohm PPCF 38:1213, together
  with its DOI, moved from `zohm-1996` (the 38:105 review) to
  `zohm-1996-b`.
- Closing sweeps:
  - `--dupes` leaves only `kim-2023`/`kim-2023-b` (same printed title,
    different author and article; kept distinct).
  - The whole-corpus fuzzy-title sweep found every pair distinct.
- Rule question, carried over: "submitted" citations had been folded into
  the published entries. *Decided (2026-10-16): preprints are kept
  distinct, as in plasma-propulsion. 23 entries split (1552 → 1572); the
  repair also separated a wrong merge, `rosofsky-2023` vs
  `rosofsky-2023-b`.*

### Deep lint #1

- Notation, consistency, stale-statement and link fixes on about 110 pages.
  Summary in `wiki/log.md`.
- Real errors found and fixed: tang-2025 refs [32]/[33] swapped;
  artola-2022's TPF attribution (fast-CQ, not VDE); rahman-2024 on
  gopakumar's loss; MEGA dissipation per run; cbm18 DWRBM reference length.
- None closed: no contradiction was closed and no tag changed beyond
  `surrogate`.

### Bundle fit (final recommendation)

- **New bundle `neural-operator-surrogates`** for gopakumar-2024 and
  rahman-2024. They are ML-method papers whose MHD content is the training
  data (JOREK and NIMROD/GTC runs). They stay here as the "data-driven
  surrogates" entry of the reading guide. A dedicated bundle would hold
  their FNO/PINO lineage (`li-2020-c`, `li-2022-b`) properly.
- Earlier suggestions stand:
  - D17 copies: bhole-2023 → high-order-capturing-schemes; jiang-2024,
    seto-2023 and liu-2024 → curvilinear-metric-discretization;
    panici-2023 → orthogonal-polynomials-and-quadrature. *Done 2026-10-16:
    PDFs copied into each archive and ingested separately in each bundle.*
  - Possible new bundle `stiff-time-integration`.
  - Not recommended: splitting off the energetic-particle or stellarator
    clusters.

## Chunk 2 — the 20 application papers (2026-10-16)

Sources: strauss-2022, hu-2021, liu-2021, liu-2022-b, artola-2022,
becoulet-2022, hezaveh-2022, zeng-2023, howell-2022, cathey-2023,
ebrahimi-2023, hu-2023, mcdevitt-2023, nardon-2023-b, zhou-2023,
cathey-2024, hu-2024, kong-2025, ramasamy-2024, sato-2024.
25 new concept pages (100 in all), about 50 chunk-1 pages extended,
1312 bibliography entries. 40 of 50 files ingested.

### Decisions for the human

1. **Resistive-term sign in the JOREK flux equation** (open since chunk 1,
   [reduced MHD](wiki/methods/reduced-mhd.md)): chunk 2 adds four sources
   with the diffusive sign (nardon-2023-b Eq. 1, hu-2021 Eq. 3, hu-2023
   Eq. 5, ramasamy-2024 Eq. 7, the last also for the hyper-resistive term);
   the count is six against two. The closure as a printed slip is now
   strongly supported.
2. **Cause of the JOREK3D–CASTOR3D tearing gap**: ramasamy-2024 (same author
   group) attributes nikulsin-2022's 13.2 %/26.2 % gap to insufficient
   CASTOR3D poloidal resolution, without showing the re-run; nikulsin-2022
   attributed it to $v_\parallel=0$. Rule whether the later statement
   supersedes, or keep Open (current state).
3. **Slug decisions from Crossref** (applied): zeng-2022 → `zeng-2023`
   (NF 63:016026, January 2023 issue); the Kong plasmoid-drift paper →
   `kong-2025` (NF 65:016042, January 2025; the JET SPI paper keeps
   `kong-2024`); the double-tearing-mode paper is `nardon-2023-b`
   (NF current-spike paper `nardon-2023` came first).
4. **Version caveats**: becoulet-2022 is the IAEA FEC 2020 manuscript (15
   references) rather than the NF article (57); ebrahimi-2023 is arXiv v1,
   single-author, while the published paper adds Bhattacharjee; artola-2022
   is arXiv v1 under its earlier title; zeng-2023, kong-2025, liu-2021,
   liu-2022-b, hezaveh-2022, hu-2021, hu-2024, howell-2022, cathey-2023,
   ramasamy-2024 and zhou-2023 are preprints or accepted manuscripts.

### Contradictions opened (Open unless stated)

| Name | Page(s) |
|---|---|
| ITER wall time: 250 ms (strauss-2022) vs 0.5 s / ≈500 ms (hoelzl-2021, artola-2022); definitions not stated | definitions/disruption |
| ITER TQ duration: 75–125 ms for a locked-mode RWTM TQ (strauss-2022) vs ≈20 ms VDE TQ (hoelzl-2024) — attributed contrast | definitions/thermal-quench |
| TQ trigger surface of impurity SPI: q=2 (hoelzl-2021) vs q=1 in ITER Ne/H SPI (hu-2021, hu-2023) — qualification | definitions/thermal-quench |
| Fast-CQ sideways force: <1 MN (artola-2022) vs ≈4 MN (Strauss 2018 as cited by artola-2022) | definitions/wall-forces |
| Radiation scaling with toroidal source width (hu-2023, kong-2025 vs hoelzl-2021 §2.8) | definitions/shattered-pellet-injection |
| Plasmoid drift aids (hoelzl-2024, JET D) or hinders (hu-2024, ITER Ne H-mode) assimilation — context-dependent | definitions/plasmoid-drift, definitions/shattered-pellet-injection |
| EDA H-mode dominant harmonics: n=1–3 (hoelzl-2024) vs n=6–9 linear, low n nonlinear (cathey-2023, cathey-2024) | definitions/edge-localized-mode |
| Complete RE loss vs trapped survivors at beam termination (hoelzl-2021, liu-2021 vs mcdevitt-2023) | definitions/runaway-electrons |
| Artificial parallel diffusion as a surrogate for RE streaming (bandaru-2024 vs liu-2021's judgement) | methods/runaway-electron-fluid-model |
| Viscous term of the JOREK vorticity equation: $R$ (hu-2021-b, hu-2021) vs $R^3$ (hu-2023, hu-2024) | methods/reduced-mhd |
| Ohmic heating with a source current in M3D-C1: $\eta J^2$ (zhou-2023) vs $\eta\mathbf J\cdot(\mathbf J-\mathbf J_x)$ (saxena-2025) | methods/visco-resistive-mhd-model, software/m3d-c1 |
| Cause of the JOREK3D–CASTOR3D tearing gap (nikulsin-2022 vs ramasamy-2024) | software/jorek3d, software/castor3d, definitions/tearing-mode |
| Analytic Dommaschk vs finite-element vacuum potential (nikulsin-2022 vs ramasamy-2024) | methods/dommaschk-potentials |
| BAE-like $n=1$ growth at $q_{\min}>1.1$: zero in M3D-C1-K vs constant in NIMROD (liu-2022-b citing Brennan 2012) | definitions/fishbone |
| Phase-space invariant during chirping: $C=\omega P_\phi-n\mathcal E$ (White 2020, not ingested) not conserved (hezaveh-2022) | definitions/energetic-particle-mode, methods/chirping-phase-space-diagnostic |

Qualifications, not contradictions: "ELM cycles" in single-fluid NIMROD
(ebrahimi-2023) vs the diamagnetic requirement for repetitive cycles; the
hybrid kinetic-MHD definition widened from a minority population to bulk
kinetic thermal ions (liu-2022-b, sato-2024); the "none computes $\Delta'$"
sentence on the tearing page replaced (zeng-2023 measures it); the chunk-1
"axisymmetric-only PiC impurities" claim of hoelzl-2024 refers to a
different model than hu-2023's 3D CR markers (no conflict).

### Printed inconsistencies (selection; full lists on the Source pages)

* strauss-2022: the 75–125 ms ITER range combines two TQ/wall-time ratios.
* artola-2022: Eq. 1 has $1/\mu_0$ on the wrong integral; "0.8 µΩ".
* hu-2021: γ−1 factor only in Eq. 12; "100 ms" for ≈100 µs.
* hu-2024: "10⁸ MJ s^-1/2 m^-2" for 10⁸ J.
* liu-2021: pseudo-particle count off by 10; Eq. 9 anti-diffusive heat flux.
* zeng-2023: Eq. 4 signs; "16^-32" for 10^-32.
* hezaveh-2022: Eq. 16 sign of $P_2$ (confirmed wrong by the paper's numbers); "ε = 3.2".
* howell-2022: Eq. A30 missing $d\rho$; viscous-term sign A23/A28 vs Eq. 2.
* cathey-2023: Fig. 6 caption vs legend m/n; E_r minimum stated two ways.
* cathey-2024: diamagnetic-velocity mass factor.
* nardon-2023-b: Eq. A3 missing a factor $R$.
* ramasamy-2024: Table 1 η 1.93e-6 vs text 1.93e-5; Eq. 5 extra ρ.
* sato-2024: §1 vs §2 credit for the equilibrium; "Phys. Plasma B".
* mcdevitt-2023: seed fraction text vs Fig. 3b; missing square root in $\xi_{\mathrm{trap}}$.
* becoulet-2022: "~40 m" for 40 cm; displacement formula gives a flux.

### Bibliography (905 → 1312 entries, FLAGS 0)

* Same key, different work: `gerasimov-2020-b`, `xu-2019-b`, `hu-2018-c`,
  `pazsoldan-2021-b`, `maget-2007-b`, `zhang-2020-c`, `matsuyama-2022-c`,
  `matsuyama-2022-d`, `kim-2020-d` (missed by the merge, caught by the
  Source writer of ebrahimi-2023 and fixed), `liu-2021-b`, `dimits-1993-b`.
* Folded: `carl-2021` → `sovinec-2021` (NIMSTELL abstract, given names
  printed as surnames in saxena-2025); White's book printed 2014 →
  `white-2013`; Beidler PPCF 59 printed 2017 → `beidler-2016`.
* Kept distinct with a note: `kim-2023` / `kim-2023-b` (same printed title,
  different first author and article number).
* `liu-2021` upgraded from the arXiv `@misc` to the PPCF article.

### Bundle-fit suggestions (chunk 2)

All 20 belong here. No new D17 candidates beyond chunk 1's list; the
stellarator papers (ramasamy-2024, zhou-2023) and energetic-particle papers
(liu-2022-b, hezaveh-2022, sato-2024) stay with their clusters as
recommended before.

### Chunk 3 (planned)

gopakumar-2024, rahman-2024, seto-2024, wright-2024, tang-2025,
vannini-2025, zhang-2025, izzo-2025, liang-2025, sato-2026 (10 files).

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
     *Kept Open by human decision (2026-10-16).*
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

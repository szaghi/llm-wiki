# Update log

## 2026-11-08

**Chunk 6 ingested (night protocol, D32); archive complete.** Sources:
boscheri-2025, liu-2025, taylor-2025, zeng-2025, jones-2026, yang-2026,
okafor-2026 (57 of 57).

- Concept pages updated (11): methods/shifted-boundary-method (compressible
  Euler with shocks; polynomial correction), methods/inverse-lax-wendroff
  (deformable solids), methods/fluid-structure-coupling (added mass,
  compressible), methods/state-redistribution (energy stability),
  definitions/small-cell-problem (remedies; Forrer–Jeltsch), methods/cut-cell-method
  (constrained-transport MHD), methods/ghost-fluid-method (Riemann-based
  variants, MHD), methods/high-order-immersed-boundary (shock-adaptive
  blending), methods/ghost-cell-method, benchmarks/shock-obstacle-interaction,
  properties/discrete-conservation.
- Source pages created (7); audit lists regenerated, no older list changed.
- Bibliography: 2608 entries after the chunk merge (FLAGS 0; karatzas-2020-b
  kept distinct from the 2019 pre-publication citation), 2598 after the closing
  sweep.
- **Closing bibliography sweep:** `bib_merge --dupes` (3 cross-stem groups),
  plus a scratch sweep for DOI duplicates, identical titles across years,
  journal+volume+page collisions and fuzzy titles. Merged (citedby union):
  ye-1993 → ye-1999, leveque-1019 → leveque-1994, yusof-1996 →
  mohdyusof-1996 (rekeyed from jmohdyusof-1996), mos-1999 → moes-1999,
  scicomput-2020 → sticko-2020, computphys-2007 → parvizian-2007,
  jhbramble-1972 → bramble-1972, barlev-1997 → barlev-1975, boiveau-2014 →
  boiveau-2016, deconinck-2007 → deconinck-2004; d-1991 rekeyed
  dezeeuw-1991. Kept distinct after review: editions (ferziger, leveque
  1990/1992, saad, toro), thesis vs paper (berger-1982, givelberg, zhu-2001),
  conference vs journal (dezeeuw-1991/1993), report vs chapter (noh-1963/1964),
  pre-publication citations (khadra-1999, karatzas-2019-b, burman-2019), series
  parts (coutanceau, shu, saye, zhu, borazjani, bungartz). `--dupes` reports 0
  afterwards.
- **Whole-bundle deep lint:** registry extended with $k$ (polynomial degree),
  which removes drift between $p$, $m$ and $k$ (state-redistribution,
  shifted-boundary-method); bound summation indices renamed where they
  collided with $k$ ($S^m_h$ in the registry and shifted-boundary-method, the
  ILW Taylor formula); tag synonyms merged (small-cell-problem → small-cell,
  volume-penalization → penalization, multi-material → multimaterial,
  adaptive-mesh-refinement → amr); every concept page reachable from the
  reading guide and linked from at least two other pages; no forbidden math
  delimiters; no contradiction open.

**Chunk 5 ingested (night protocol, D32).** Sources: mittal-2023,
agrawal-2024, liu-2024, turner-2024, munschy-2024, huang-2024, qi-2024,
berger-2024, burman-2025, marashi-2025 (50 of 57).

- Concept page created (1): methods/high-order-immersed-boundary (seven
  routes to third or higher order at an immersed boundary, compared).
- Concept pages updated (10): definitions/sharp-and-diffuse-interface
  (five-condition definition), definitions/immersed-boundary-method (second
  history), methods/inverse-lax-wendroff (auxiliary-point simplified ILW),
  methods/state-redistribution (provable stability), methods/volume-penalization
  (kinetic plasma walls), methods/fluid-structure-coupling (isogeometric
  rods), methods/cutfem (2025 review), methods/ghost-cell-method (high order),
  benchmarks/shock-obstacle-interaction, benchmarks/flow-past-circular-cylinder.
- Registry: no extension; native symbols kept page-local in the notation maps.
- Source pages created (10); audit lists regenerated, two older lists changed
  (sharan-2022, tan-2010).
- Bibliography: 2287 entries (from 1780); FLAGS 0. burman-2025 has no Crossref
  deposit: its 224 printed references were parsed from the text, and the
  parser's split of "Part I/II" titles into the venue was corrected before the
  merge. Resolution: autoresolve (now reserving every fragment key as taken, to
  avoid alias shadowing), plus hand corrections: leveque-1985-b (cochlea
  model), glowinski-1994-b (same-key venue check), munschy-2024-b (companion
  paper), burman-2011 (cut elements II), seo-2011-b.
- Deep lint (self-audit of the 11 touched concept pages): quotations checked
  against the text layers (Turner, Mittal & Seo, Liu, Marashi, Munschy);
  canonical notation only; reading guide renumbered (it had run 1–4, 7, 8, 5, 6).

**Chunk 4 ingested (night protocol, D32).** Sources: sharan-2022,
xie-2022, boustani-2022, reiss-2022, giuliani-2022, verzicco-2023,
deprenter-2023, collins-2023, menez-2023, raj-2023 (40 of 57).

- Concept pages created (2): definitions/spurious-force-oscillations,
  methods/wall-models-for-immersed-boundaries.
- Concept pages updated (17): definitions/immersed-boundary-method (history
  before 1972), definitions/sharp-and-diffuse-interface,
  definitions/small-cell-problem (finite-element stability vs conditioning),
  definitions/fresh-cell-problem, methods/cut-cell-method (SBP embedded
  boundaries, implicit moving cut cells), methods/volume-penalization
  (compressible), methods/state-redistribution (DG), methods/immersed-interface-method
  (thin porous membranes), methods/fluid-structure-coupling,
  methods/shifted-boundary-method (penalty-free), methods/cutfem,
  methods/ghost-cell-method (GPU, thin and sharp-edged bodies),
  properties/discrete-conservation, results/first-order-accuracy-of-regularized-delta-forcing,
  benchmarks/shock-obstacle-interaction, benchmarks/flow-past-sphere.
- Registry: subscripted $\phi_v$, $\phi_p$ (penalization volume fraction and
  porosity) recorded as a clash kept on purpose with the level set.
- Source pages created (10); audit lists of all 40 regenerated.
- Bibliography: 1780 entries (from 1186); FLAGS 0 after mechanical resolution
  (scratch tool autoresolve: aliases by DOI or title to the right member of a
  key family, else the next free suffix) plus ten hand corrections; a duplicate
  of Burman's "cut elements II" under two keys (burman-2011, burman-2012-b) is
  left for the closing duplicate sweep.
- Deep lint (self-audit of the 19 touched concept pages): notation of
  compressible penalization translated; no contradiction opened.

**Chunk 3 ingested (night protocol, D32).** Sources: sotiropoulos-2014,
main-2018, griffith-2020, berger-2021, atallah-2022, giuliani-2022-b,
nair-2022, natarajan-2022, ni-2022, ou-2022 (30 of 57).

- Concept pages created (3): methods/shifted-boundary-method,
  methods/state-redistribution, methods/fluid-structure-coupling.
- Concept pages updated (15): definitions/immersed-boundary-method
  (terminology, later families), definitions/sharp-and-diffuse-interface,
  definitions/small-cell-problem, definitions/fresh-cell-problem,
  methods/redistribution, methods/cut-cell-method (moving embedded boundaries),
  methods/ghost-cell-method (directional ghost values, CURVIB),
  methods/classical-immersed-boundary-method (immersed finite elements),
  methods/immersed-interface-method, methods/cutfem,
  operators/regularized-delta-function (B-spline kernels),
  results/first-order-accuracy-of-regularized-delta-forcing,
  properties/discrete-conservation, benchmarks/flow-past-circular-cylinder,
  benchmarks/shock-obstacle-interaction.
- Registry extended: surrogate domain and boundary, map $\mathcal M$, distance
  vector $\mathbf d$, shift operator $S^m_h$, redistribution neighbourhoods.
- Source pages created (10); audit lists of all 30 Source pages regenerated.
- Bibliography: 1186 entries (from 609); FLAGS 0 after 37 aliases (30 same-key
  different works, 7 same work under a second key) and 18 verified silences.
- Deep lint (self-audit of the 18 touched concept pages): timestamps from the
  real clock; no contradiction opened (Griffith & Patankar's claim that
  immersed formulations escape added-mass instability is recorded beside
  Uhlmann's measured density-ratio limit as a qualified statement, not as a
  contradiction: the former concerns elastic-structure formulations, the
  latter explicit rigid-particle coupling).

**Chunk 2 ingested (night protocol, D32).** Sources: tseng-2003,
mittal-2005, uhlmann-2005, colella-2006, ghias-2007, taira-2007,
mittal-2008, tan-2010, chaudhuri-2011, burman-2015 (20 of 57).

- Concept pages created (6): methods/ghost-cell-method,
  definitions/fresh-cell-problem, methods/immersed-boundary-projection-method,
  methods/inverse-lax-wendroff, methods/cutfem,
  benchmarks/shock-obstacle-interaction.
- Concept pages updated (15): definitions/immersed-boundary-method (formal
  continuous/discrete forcing dichotomy, grid scaling, later families),
  definitions/sharp-and-diffuse-interface, definitions/small-cell-problem,
  operators/regularized-delta-function, operators/spreading-and-interpolation,
  methods/direct-forcing (Lagrangian direct forcing), methods/feedback-forcing,
  methods/volume-penalization, methods/classical-immersed-boundary-method,
  methods/cut-cell-method (formally consistent EB), methods/redistribution
  (hybrid update), methods/ghost-fluid-method, properties/discrete-conservation
  (accuracy–conservation trade-off), results/first-order-accuracy-of-regularized-delta-forcing,
  benchmarks/flow-past-circular-cylinder, benchmarks/flow-past-sphere.
- Registry extended: rigid-body velocity $\mathbf u_c$, $\boldsymbol\omega_c$,
  $\mathbf x_c$; ghost-cell points $\mathbf x_{BI}$, $\mathbf x_{IP}$, $\Delta l$;
  classification symbols $\mathbf f_b$, $[L]$, $[L']$.
- Source pages created (10); audit lists of all 20 Source pages regenerated.
- Bibliography: 609 entries (from 312), all ten lists from Crossref deposits;
  `bib_merge.py` FLAGS 0 after 18 aliases (same key, different works:
  verzicco-2000-b, verzicco-1996-b, liu-1998-b, quirk-1994-b, beyer-1992-b,
  lee-2003-b, mittal-1999-b, mittal-2002-c, fedkiw-2002-b, iaccarino-2003-b,
  peskin-1972-b for the thesis, the swapped Mittal 1997 pair, GetFEM++/LifeV)
  and 12 verified silences; same-key venue check clean.
- Deep lint (compiler self-audit of the 21 touched concept pages): paper
  symbols translated (Taira's $q$ → $\mathbf u$, his pressure $\phi$ → $\mathbf p$),
  section references without a printed heading replaced by part names
  (Mittal & Iaccarino 2005), Colella's redistribution formula marked as
  reconstructed from the prose; no contradiction opened.

**Chunk 1 ingested (night protocol, D32): the founding papers.** Sources:
peskin-1972, goldstein-1993, leveque-1994, pember-1995, fedkiw-1999,
ye-1999, angot-1999, fadlun-2000, kim-2001, peskin-2002 (10 of 57).

- Bundle scaffolded: `bundle.toml`, `CLAUDE.md`, `raw/`, `wiki/index.md`,
  `wiki/log.md`, `wiki/notation.md`.
- Registry created from chunk 1 (domain, fluid, Lagrangian description,
  coupling operators, forcing and penalization, cut cells, interfaces and
  level sets); conventions fixed: normal out of the body, $\varphi$ for the
  delta kernel because $\phi$ is the level set, $\kappa$ for the volume
  fraction, $\mathbf q$ for conserved variables, order of accuracy $r$.
- Concept pages created (18): definitions/immersed-boundary-method,
  definitions/sharp-and-diffuse-interface, definitions/small-cell-problem,
  operators/regularized-delta-function, operators/spreading-and-interpolation,
  methods/classical-immersed-boundary-method, methods/feedback-forcing,
  methods/direct-forcing, methods/volume-penalization,
  methods/immersed-interface-method, methods/ghost-fluid-method,
  methods/cut-cell-method, methods/redistribution,
  results/first-order-accuracy-of-regularized-delta-forcing,
  results/convergence-of-volume-penalization,
  properties/discrete-conservation, benchmarks/flow-past-circular-cylinder,
  benchmarks/flow-past-sphere.
- Source pages created (10), one per source above.
- Bibliography: 312 entries from the ten reference lists (six from Crossref
  deposits, four transcribed from the printed lists: goldstein-1993 and
  pember-1995 through OCR, angot-1999, peskin-2002); `bib_merge.py` FLAGS 0
  after 2 aliases and 11 verified silences; undated in-press citations keyed
  by the citing paper's year.
- Deep lint (compiler self-audit of the 18 concept pages against the
  registry): section references the OCR texts cannot support replaced by
  part names; paper-native symbols removed (Ye's $\phi$ → $w$, Pember's
  update formula described in words because the OCR does not show it);
  no contradiction opened.

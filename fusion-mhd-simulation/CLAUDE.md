# Bundle law — fusion-mhd-simulation

Domain (user decision, 2026-10-16, `DECISIONS.md` D25): the numerical
simulation of magnetically confined fusion plasmas with
magnetohydrodynamic models and their kinetic extensions.

* models: resistive, visco-resistive and extended (two-fluid,
  diamagnetic, neoclassical) MHD; reduced MHD for tokamaks and
  stellarators; hybrid kinetic-MHD models for energetic particles, with
  their pressure or current coupling; the physics modules attached to MHD
  codes (impurities in coronal or collisional-radiative treatment,
  neutrals, runaway electrons, bootstrap current, sheath conditions);
* numerics: finite elements (Bézier/Hermite $G^1$/$C^1$, Bell, spectral
  elements), finite differences in field-aligned coordinates, toroidal
  Fourier representations, implicit, semi-implicit and leapfrog time
  integration, operator splitting, stabilization, linear solvers and
  preconditioners, free-boundary and resistive-wall coupling,
  particle-to-mesh projection, GPU ports, symbolic code generation;
* equilibria as initial states: Grad–Shafranov, 3D inverse equilibrium
  solvers;
* the physics these models are used for: disruptions (thermal and current
  quench, vertical displacement events, halo currents, wall forces,
  runaway electrons, shattered pellet and massive material injection),
  edge-localized modes and ELM-free regimes, tearing, kink, ballooning and
  infernal modes, energetic-particle-driven Alfvén modes and fishbones,
  edge and divertor plasmas, stellarator MHD;
* verification and validation: code-to-code benchmarks, analytic scalings,
  and data-driven surrogates of MHD codes (neural operators).

It is a standalone second brain, independent of every other bundle and
agnostic of every other repository (`DECISIONS.md` D12, D17, D25).

## Corpus

- Primary archive: `~/papers/mosaic/fusion-mhd-simulation/*.pdf`
  (read-only; Layer 1), 50 PDFs (2026-10-16). Most filenames follow
  `year_Crossref_Journal_Surname_Title-prefix.pdf`; three are
  `0000_manual_no_journal_Unknown_<doi-digits>title….pdf` and carry no
  metadata (their page 1 identifies them). Many files are arXiv or HAL
  preprints despite the "Crossref" in their name. Treat the filename as a
  hint and verify identity against page 1 and Crossref.
- **Version rule:** the Source page records the version read (arXiv vN,
  HAL, accepted manuscript, version of record); its metadata is the
  published identity from Crossref. Claims and equations are those of the
  version read; a known later correction (publisher's note, erratum) is
  recorded, not silently applied.
- Chunks (user decision): 20 sources each. Chunk 1 is the code, method,
  benchmark and review papers, so that the registry and the reading guide
  are built from them; chunks 2 and 3 are the application papers.

## Bundle specifics

- Notation registry: [`wiki/notation.md`](wiki/notation.md) is normative
  for every concept page. Extend it, and log the extension, before
  writing math that needs a symbol it lacks. Equations are written in SI
  with $\mu_0$ explicit; a source in normalized units (JOREK, M3D-C1,
  CLT units) is translated on its Source page, and its numbers are quoted
  with the normalization stated.
- Keys and slugs: `firstauthor-year[-b, …]`, the first author's surname
  in lowercase ASCII, the year that of the published issue. Same-author
  same-year papers take suffixes in publication order when known,
  otherwise in archive-filename order.
- Chunks are read by parallel subagents into scratch notes, compiled by
  the main session, staged as one unit with one commit message; the human
  reviews and commits before the next chunk starts. Reference lists are
  merged with `tools/bib_merge.py` (D16); `--dupes` and a fuzzy-title
  sweep after the final chunk.
- Issues file: [`INGESTION-ISSUES.md`](INGESTION-ISSUES.md) (bundle root,
  outside the wiki) records per chunk every contradiction opened, every
  printed inconsistency, identity or metadata problem, every paper that
  would fit another bundle better, and every decision left to the human.
  The `## Contradictions` sections of concept pages stay the normative
  record; the file is the reviewer's digest.
- Worklist: `tools/worklist.sh fusion-mhd-simulation`.
- Bibliography: `wiki/bibliography.bib` plus the generated
  `wiki/bibliography.md` (D15); pending reference lists:
  `python3 tools/bib_to_md.py fusion-mhd-simulation/wiki --pending`.
- Lint: `python3 tools/lint_okf.py fusion-mhd-simulation/wiki`.
  It must pass before commit.
- Commits: `docs(fusion-mhd-simulation): ingest chunk N: <slugs>`.

## Status

**Chunk 3 committed 2026-10-16:** the last 10 papers; corpus complete
(50 of 50 ingested), 110 concept pages, 1552 bibliography entries.
Closing `--dupes` and fuzzy-title sweeps done; deep lint #1 (50
ingestions) applied; committed (123a28a). Fiat closures (2026-10-16):
JOREK resistive sign and Gear order, both printed slips. Next: the
remaining human decisions listed in
`INGESTION-ISSUES.md` (closures, tag vocabulary, bundle-fit); the next
deep lint is due after 50 further ingestions.

**Chunk 2 committed 2026-10-16 (0b8f975):** the 20 application papers;
40 of 50 ingested, 100 concept pages, 1312 bibliography entries.

**Chunk 1 committed 2026-10-16 (e579f32):** scaffold (D25) and the 20 code, method,
benchmark and review papers; 20 of 50 ingested. Next: chunk 2, 20
application papers.

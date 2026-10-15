# Bundle law — plasma-propulsion-simulation

Domain (user decision, 2026-10-14, `DECISIONS.md` D22): the numerical
modelling of electric and plasma thrusters and of the plasmas they make.

* thruster families as simulation targets: Hall-effect, gridded-ion,
  helicon and magnetic-nozzle, pulsed (ablative) and laser-ablation
  plasma thrusters, with their propellants (xenon, krypton, water,
  PTFE);
* kinetic models: particle-in-cell with Monte Carlo collisions
  (PIC-MCC), DSMC for neutral and plume flows, their numerical
  constraints (Debye length, plasma frequency, particle weighting,
  noise), permittivity and geometry scaling, and GPU implementations;
* fluid and hybrid models: electron fluid (drift-diffusion, five-moment)
  models, hybrid fluid-kinetic models, quasi-neutral and sheath
  treatments;
* the physics these models must reproduce: anomalous electron
  cross-field transport, the breathing mode and other oscillations,
  azimuthal (electron drift) instabilities, wall interaction, plume
  expansion and backflow;
* verification, benchmarks, uncertainty quantification and Bayesian
  calibration of thruster models.

**Context material (user decision, 2026-10-14):** the archive also holds
the complete *Acta Astronautica* vol. 151 (October 2018), 92 files
including the issue's front matter (one of them misfiled under a Bird 2009
filename; see Corpus). Most of them (attitude control,
launch and trajectory design, structures, combustion, mission studies)
are outside the domain above. The user chose to ingest all of them. Each
gets a Source page and its reference list in the bibliography; it earns
concept pages only where it touches the domain above (plasma, electric
propulsion, plasma–spacecraft interaction, particle simulation). An
off-domain paper presenting its own named method (an attitude
controller, a trajectory scheme) does not seed a concept page here: the
bundle's registry and reading guide are for plasma propulsion. This is a
scope rule of this bundle, not a granularity exception, and the Source
page says why no concept page was created.

It is a standalone second brain, independent of every other bundle and
agnostic of every other repository (`DECISIONS.md` D12, D17, D22).

## Corpus

- Primary archive: `~/papers/mosaic/plasma-propulsion-simulation/*.pdf`
  (read-only; Layer 1), 108 PDFs (2026-10-14). Filenames follow
  `year_Crossref_Journal_Surname_Title-prefix.pdf`; the year is the one
  the collection recorded, not necessarily the issue year. Treat the
  filename as a hint and verify identity against page 1 and Crossref.
- The 16 papers outside *Acta Astronautica*, 3 on-domain papers from
  Acta vol. 151 (cai-2018, sun-2018, zhang-2018) and the file
  `2009_Crossref_Physics_of_Fluids_Bird_Accuracy_and_efficiency_of_the_sophisticated_direct_simulati.pdf`
  form chunk 1. That file is **not** Bird et al. (2009): page 1 is
  Mungiguerra et al., Acta Astronaut. 151:456 (2018), ingested as
  `mungiguerra-2018`; Bird et al. (2009, doi:10.1063/1.3067865) is not in
  the archive.
- The other 88 Acta files (D23): chunk 2 is the 21 papers copied to the
  new bundles `high-speed-aerothermodynamics` (10) and
  `chemical-airbreathing-propulsion` (11), ingested in full there and as
  Source-only pages here; chunks 3–6 (20, 20, 20, 7) are the rest, the
  five plasma-related papers first (gomezjenkins-2018, alpatov-2018,
  shuvalov-2018, garciagarrido-2018, yang-2018, ingested in full here),
  then the others as Source-only pages, in archive-filename order.
- **Source-only page:** verified metadata, summary, key claims, notation
  map, an audit list stating that no concept page cites it and why (the
  scope rule; other bundles are never named in wiki content, D12, even
  for the D23 copies compiled in full elsewhere), and the reference list
  merged into the
  bibliography. It is an ingestion in the protocol's sense. Source-only
  pages carry the tag `context` and have no incoming links from concept
  pages, so the lint reports each as an orphan warning; these warnings
  are expected. The only other accepted orphan warning is a Source page
  of a paper ingested in full that earns no concept page under the
  granularity rule; its audit list says why, it carries no `context`
  tag, and the warning clears when a later source makes a concept page
  cite it (amendment 2026-10-15, chunk 3: gomezjenkins-2018,
  garciagarrido-2018, yang-2018).

## Bundle specifics

- Notation registry: [`wiki/notation.md`](wiki/notation.md) is normative
  for every concept page. Extend it, and log the extension, before
  writing math that needs a symbol it lacks. Units are SI; temperatures
  in energy units (eV) are written $T_s$ with the unit stated.
- Keys and slugs: `firstauthor-year[-b, …]`, the first author's surname
  in lowercase ASCII, the year that of the published issue. Same-author
  same-year Acta papers take suffixes in archive-filename order, after
  the core paper (cai-2018, zhang-2018 are the core papers).
- Chunks: 20 sources each (user decision), read by parallel subagents
  into scratch notes, compiled by the main session, staged as one unit
  with one commit message; the human reviews and commits before the next
  chunk starts. Reference lists are merged with `tools/bib_merge.py`
  (D16), with the venue check, the same-key vol:page check and the
  per-fragment final-key collision check before `--write`, then
  `--dupes` and a fuzzy-title sweep after the final chunk.
- Issues file: [`INGESTION-ISSUES.md`](INGESTION-ISSUES.md) (bundle root,
  outside the wiki, user request 2026-10-14) records per chunk every
  contradiction opened, every printed inconsistency, identity or
  metadata problem, and every decision left to the human. The
  `## Contradictions` sections of concept pages stay the normative
  record; the file is the reviewer's digest.
- Worklist: `tools/worklist.sh plasma-propulsion-simulation`.
- Bibliography: `wiki/bibliography.bib` plus the generated
  `wiki/bibliography.md` (D15); pending reference lists:
  `python3 tools/bib_to_md.py plasma-propulsion-simulation/wiki --pending`.
- Lint: `python3 tools/lint_okf.py plasma-propulsion-simulation/wiki`.
  It must pass before commit.
- Commits: `docs(plasma-propulsion-simulation): ingest chunk N: <slugs>`.

## Status

**Chunk 6 staged 2026-10-15 — the archive is complete:** the last 7
Source-only pages; 108 of 108 ingested (`tools/worklist.sh`: pending 0),
4084 bibliography entries, the front matter `unknown-2018` the only
`--pending` entry (by design). Closing sweeps after the final chunk:
`--dupes` 0 groups, cross-year fuzzy-title sweep 51 pairs all distinct,
no corpus-wide merge. Deep lint #2 (all concept pages, registry, root
index) applied with this chunk: 1 error fixed, unregistered symbols
removed, `$\mathrm{Re}_m$` registered, 13 tag merges.

**Chunk 5 committed 2026-10-15 (cd72295):** 20 Source-only pages, including the
front matter `unknown-2018` (no reference list: a permanent `--pending`
entry); 101 of 108 ingested, 3899 bibliography entries; no concept page
changed. The old cited-work entry `wu-2018` was re-keyed to `wu-2018-d`
first. Next: chunk 6, the last 7 Source-only pages, then the whole-corpus
`--dupes` and fuzzy-title sweeps and a deep lint.

**Chunk 4 committed 2026-10-15 (8a867fb):** 20 Source-only pages; 81 of 108 ingested,
3360 bibliography entries; no concept page changed. Two re-slugs
(hady-2018 → `ghassabian-2018`, le-2018 → `lemay-2018`); the old cited-work
entries `kim-2018` and `liu-2018` were re-keyed to `kim-2018-b` and
`liu-2018-e` first. Next: chunk 5, 20 Source-only pages including the
front matter `unknown-2018`; first re-key the existing `wu-2018` entry.

**Chunk 3 committed 2026-10-15 (20de74d):** the five plasma-related Acta papers in full
(alpatov-2018, shuvalov-2018, gomezjenkins-2018, garciagarrido-2018,
yang-2018) and 15 Source-only pages; 61 of 108 ingested, 2738 bibliography
entries; two new concept pages (ion-beam shepherd, magnetized-body plasma
drag), notation §7 added; no contradiction opened. gomez-2018 was re-slugged
`gomezjenkins-2018` (Crossref family name). Next: chunk 4, 20 Source-only
pages; first re-key the existing `kim-2018` and `liu-2018` entries.

**Chunk 2 committed 2026-10-14 (4c3b34e):** 21 *Acta Astronautica* papers as Source-only
pages (their full compilation is in high-speed-aerothermodynamics and
chemical-airbreathing-propulsion, D23); 41 of 108 ingested, 2130
bibliography entries; no concept page changed. Next: chunk 3, the five
plasma-related Acta papers in full plus 15 Source-only pages.

**Chunk 1 committed 2026-10-14 (37602e6):** the 20 core papers; 20 of 108 ingested,
1437 bibliography entries, 42 concept pages after merges. Three Open
contradictions (see `INGESTION-ISSUES.md`). Deep lint: the chunk was audited
before staging (counts as deep lint #1).

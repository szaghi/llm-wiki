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
  the archive. The other 88 Acta files follow in chunks 2–6
  (20, 20, 20, 20, 8) in archive-filename order.

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

**Chunk 1 staged 2026-10-14:** the 20 core papers; 20 of 108 ingested,
1437 bibliography entries, 42 concept pages after merges. Three Open
contradictions (see `INGESTION-ISSUES.md`). Deep lint: the chunk was audited
before staging (counts as deep lint #1); the next is due after 10 more
ingestions. Next: chunk 2 (Acta files 1–20 in filename order).

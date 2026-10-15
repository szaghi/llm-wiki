# Bundle law — chemical-airbreathing-propulsion

Domain (user decision, 2026-10-14, `DECISIONS.md` D23):

* liquid rocket engines: combustion instability and thermoacoustic
  coupling, injector dynamics (swirl coaxial injectors, self-pulsation);
* detonation-based propulsion: rotating and continuous detonation
  combustors and their coupling to nozzles and turbines;
* air-breathing high-speed propulsion: scramjet combustors, cavity
  flameholding and lean blowoff, rocket-based combined-cycle engines
  (heat release, thermal choking, variable geometry, skin friction);
* hybrid and solid propellants: paraffin and HTPB fuels and binders,
  their structural and aging behaviour; combustion-based power systems;
* the experimental and numerical methods these use (reacting CFD,
  acoustic analysis, constitutive models).

It is a standalone second brain, independent of every other bundle and
agnostic of every other repository (`DECISIONS.md` D12, D17, D23).

## Corpus

- Primary archive: `~/papers/mosaic/chemical-airbreathing-propulsion/*.pdf` (read-only; Layer 1),
  self-contained per D17. Founded 2026-10-14 with papers of *Acta
  Astronautica* vol. 151 (2018), copied from the plasma-propulsion
  archive where they had been filed (D23); the files keep the
  collection's names (`year_Crossref_Journal_Surname_Title-prefix.pdf`).
  Treat the filename as a hint and verify identity against page 1 and
  Crossref.

## Bundle specifics

- Notation registry: [`wiki/notation.md`](wiki/notation.md) is normative
  for every concept page. Extend it, and log the extension, before
  writing math that needs a symbol it lacks. Units are SI.
- Keys and slugs: `firstauthor-year[-b, …]`, the first author's surname
  in lowercase ASCII, the year that of the published issue. The founding
  slugs keep the suffixes they received in the plasma-propulsion archive
  plan (e.g. `liu-2018-c`), so one paper has one slug in every bundle.
- Ingestion: reader agents into scratch notes, compiled by the main
  session, staged with the chunk of the plasma-propulsion ingestion they
  belong to (user's chunk discipline, D22); contradictions and issues go
  to [`INGESTION-ISSUES.md`](INGESTION-ISSUES.md). Reference lists are
  merged with `tools/bib_merge.py` (D16) with the venue, same-key and
  per-fragment collision checks.
- Worklist: `tools/worklist.sh chemical-airbreathing-propulsion`.
- Bibliography: `wiki/bibliography.bib` plus the generated
  `wiki/bibliography.md` (D15).
- Lint: `python3 tools/lint_okf.py chemical-airbreathing-propulsion/wiki`. It must pass before commit.
- Commits: `docs(chemical-airbreathing-propulsion): ingest <slugs>`.

## Status

**Founding chunk staged 2026-10-14** (with plasma-propulsion chunk 2): 11 sources, 13 concept pages; audited before staging (counts as deep lint #1). No open contradiction.

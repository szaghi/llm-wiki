# Bundle law — structured-mesh-methods

Domain (user decision, 2026-11-08, `DECISIONS.md` D33): structured and
curvilinear mesh generation and its numerical consequences, as collected in
the user's structured-mesh bibliography (papers of 1966–2026).

* boundary-fitted (curvilinear) coordinate systems: algebraic generation by
  transfinite interpolation, elliptic generators (Winslow, Thompson) with
  control functions and clustering, hyperbolic generators, variational
  generators, conformal and orthogonal systems;
* adaptive and moving meshes: the equidistribution principle, moving mesh
  PDEs, r- and hr-adaptivity, anisotropic metric-based adaptation;
* mesh quality: algebraic quality metrics, target-matrix optimization,
  validity, untangling and morphing of high-order curvilinear meshes,
  curving third-party meshes, hexahedral meshing;
* the discretization on curvilinear and moving grids: metric terms and
  metric identities, the geometric conservation law, free-stream
  preservation of finite-difference, WENO, DG and flux-reconstruction
  schemes, grid-induced truncation error;
* applications: shock fitting on structured grids, MHD and plasma
  coordinates, detonation, turbomachinery, machine-learning and
  reinforcement-learning mesh generation.

The bundle is a standalone second brain, independent of every other bundle
and agnostic of every other repository (`DECISIONS.md` D12, D17, D33):
metric identities and the geometric conservation law also live in
`curvilinear-metric-discretization`, overlapping grids in
`overset-grid-methods`, WENO schemes in `weno-teno`; a shared work is read
again here, in this bundle's notation.

## Corpus

- Primary archive: `~/papers/mosaic/structured-mesh/*.pdf` (read-only;
  Layer 1), 56 PDFs at founding (2026-11-08), named
  `year_Crossref_Venue_Surname_Title-prefix.pdf`. Papers added later are
  ingested in further chunks, found with
  `tools/worklist.sh structured-mesh-methods`.
- The page-1 and checksum check of 2026-11-08 found 56 distinct works and
  no byte copies; all identities were confirmed on Crossref, most of them by
  bibliographic search because page 1 carries no DOI. No file is an
  image-only scan; the papers of 1966–1982 are scans with a text layer. No
  work is a Source page of another bundle. The year in the filename is the
  online year; the slug uses the year of the published issue (xie-2013 is
  filed as 2012, dobrev-2022 as 2021, pietroni-2023 as 2022). Treat the
  filename as a hint and verify identity against page 1 and Crossref.
- **Version rule:** the Source page records the version read; its metadata
  is the published identity from Crossref, corrected from page 1 where
  Crossref misspells.
- Chunks (user decision): 10 sources each, in archive (chronological)
  order; chunk 1 holds the founding papers of 1966–2001 from which the
  registry and the reading guide are built; chunk 6 holds the last six
  papers with the whole-bundle deep lint and the closing bibliography sweeps.

## Bundle specifics

- Notation registry: [`wiki/notation.md`](wiki/notation.md) is normative for
  every concept page. Extend it, and log the extension, before writing math
  that needs a symbol it lacks.
- Keys and slugs: `firstauthor-year[-b, …]`, the first author's surname in
  lowercase ASCII with spaces, hyphens and particles joined (El Aouad →
  `elaouad`), the year that of the published issue. Same-author same-year
  papers take suffixes in publication order (su-2023 is the Computers &
  Fluids paper of March 2023, su-2023-b the J. Sci. Comput. paper of
  September 2023).
- Chunks are compiled inline by the main session, without subagents (the
  owner's standing instruction), and handed to the human as one unit with
  one commit message (D26). The founding ingestion runs under the night
  protocol (D33): each chunk is one snapshot step, committed by the human
  in order. Reference lists come from the Crossref deposited records; they
  are merged with `tools/bib_merge.py` (D16); `--dupes` and a fuzzy-title
  sweep after the final chunk.
- Issues file: [`INGESTION-ISSUES.md`](INGESTION-ISSUES.md) (bundle root,
  outside the wiki) records per chunk every contradiction opened, every
  printed inconsistency, identity or metadata problem, every paper that
  would fit another bundle better, and every decision left to the human.
  The `## Contradictions` sections of concept pages stay the normative
  record; the file is the reviewer's digest.
- Bibliography preprints: a citation printed in pre-publication form
  (submitted, accepted, in preparation, to appear, arXiv) is its own entry,
  keyed by the year of that form — the citing paper's year when none is
  printed — and is never folded into the published entry.
- Timestamps come from the real clock (`date -u`), never planned times.
- Worklist: `tools/worklist.sh structured-mesh-methods`.
- Bibliography: `wiki/bibliography.bib` plus the generated
  `wiki/bibliography.md` (D15); pending reference lists:
  `python3 tools/bib_to_md.py structured-mesh-methods/wiki --pending`.
- Lint: `python3 tools/lint_okf.py structured-mesh-methods/wiki`. It must
  pass before commit.
- Commits: `docs(structured-mesh-methods): ingest chunk N: <slugs>`.

## Status

**Chunk 2 compiled 2026-11-08 (night step 02, awaiting the human's
commit):** 10 papers of 2002–2019; 20 of 56 ingested, 14 concept pages plus
the registry, 678 bibliography entries, compiler self-audit done, no
contradiction open.

**Chunk 1 compiled 2026-11-08 (night step 01, awaiting the human's
commit):** the 10 founding papers of 1966–2001; 10 of 56 ingested, 11
concept pages plus the registry, 470 bibliography entries, compiler
self-audit done, no contradiction open.

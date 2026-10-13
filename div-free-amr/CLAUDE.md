# Bundle law — div-free-amr

Domain: numerical preservation of divergence constraints (∇·B = 0 in MHD,
incompressibility in CFD) across discretizations — finite-difference,
finite-volume, mimetic/compatible/structure-preserving operators, SBP,
constrained transport, projection and cleaning methods — with particular depth
on block-structured AMR hierarchies and refinement interfaces.

This bundle is a standalone second brain on this field. It is agnostic of every
other repository (see `DECISIONS.md` D12).

## Corpus

- Primary archive: `~/papers/mosaic/div-free-amr/*.pdf` (read-only; Layer 1).
  Filenames follow `year-journal-firstauthorsurname[-doi].pdf`; the embedded DOI
  is punctuation-stripped — treat it as a hint, always verify identity and
  metadata against page 1 of the PDF itself.
- Several PDFs are image-only scans (e.g. Strand 1994, Evans & Hawley 1988):
  `pdftotext` yields ~0 chars. Read these visually page-by-page; do not OCR by
  default, and never guess equations — record illegible ranges on the Source page.
- Future sources of any kind land per repo law (capture to `raw/` if undurable).

## Bundle specifics

- Notation registry: [`wiki/notation.md`](wiki/notation.md) — normative for
  every concept page. Extend it (and log the extension) before writing math
  that needs a symbol it lacks.
- Ingestion order for the initial corpus: foundations first, roughly
  chronological (Yee/Harlow/Chorin/Evans–Hawley → CT variants, projection,
  cleaning → SBP/mimetic/DEC machinery → AMR-interface papers → recent sweep).
  Early papers define concepts; later papers exercise the merge path.
- Worklist: `tools/worklist.sh div-free-amr` (corpus minus existing Source pages).
- Bibliography: `wiki/bibliography.bib` (canonical) + generated `wiki/bibliography.md`
  per repo law (D15). Pending reference-list extractions:
  `python3 tools/bib_to_md.py div-free-amr/wiki --pending`.
- Lint: `python3 tools/lint_okf.py div-free-amr/wiki` — must pass before commit.
- Commits: `docs(div-free-amr): ingest <source-slug>`.

## Status

**Frontier batch 3a staged 2026-10-13:** jiang-shu-1996 and
colella-woodward-1984, copied from a sibling archive (D17); 103 sources.
New pages methods/weno and methods/ppm; registry section *Reconstruction
(WENO, PPM)*. Key colella-1984 renamed to the slug. No contradiction
opened. Deep lint: 7 ingestions since #9.

**Frontier batch 2 staged 2026-10-13:** brackbill-barnes-1980,
powell-1994 (ICASE report) and ryu-1998, from the user's downloads (101
sources). Key brackbill-1980 renamed to the slug. No contradiction opened.
Deep lint: 5 ingestions since #9.

**Frontier batch staged 2026-10-13:** the bundle's two most-cited works
not yet ingested whose PDFs sat in a sibling archive, copied into this
bundle's archive (D17): balsara-spicer-1999 and brio-wu-1988 (98 sources).
Their bibliography keys were renamed to the slugs (balsara-1999,
brio-1988). No contradiction opened. Deep lint: 2 ingestions since #9.

**AMR-frameworks batch staged 2026-10-12:** 93 archived sources plus one
frozen code record, all ingested. The user assigned the AMR-framework and
octree class of the ADAM paper collection to this bundle (2026-10-12). It
covers AMR infrastructure (frameworks, trees, space-filling curves, GPU
AMR) as context for the interface problem, even where a source has no
divergence content. Deep lint #9 ran on 2026-10-13 with hoppe-2022 and irsalinda-2026 (96
sources); the next is due after 10 more ingestions.

**Corpus complete (2026-07-08): 61/61 sources ingested**, 97 conformant
pages, six deep-lint passes. Books and long reviews were scoped reads with
coverage recorded on their Source pages (Bossavit, Shashkov, Hiptmair
§§4–6, AFW 2006 §§2–11, Christiansen §§2–4, Crane body) — those are the
known re-ingestion targets if deeper coverage is ever needed. New sources
append per repo law; the worklist stays authoritative.

**Bibliography backfill complete (2026-07-21): 61/61 reference lists
merged.** The corpus predated D15; its reference lists were merged in six
staged batches (2026-07-10 → 07-21), growing `bibliography.bib` from the
61 seeded ingested sources to **2700 works** (2639 cited but not ingested).
`tools/bib_to_md.py div-free-amr/wiki --pending` is empty and the sync
linter is warning-free. The three scoped-read sources' consolidated
bibliographies were extracted whole with scope recorded on each fragment
(Bossavit = 12 per-chapter lists deduplicated; Shashkov = end-of-book;
Crane = single p.163 list). The derived ingestion frontier (heavily-cited
non-ingested works) tops out at Balsara–Spicer 1999, Brackbill–Barnes 1980,
Kreiss–Scherer 1974, Whitney 1957 — candidates if the corpus is extended.
New sources append per repo law (ingestion now includes reference-list
merge per D15, step 5); the worklist and `--pending` stay authoritative.

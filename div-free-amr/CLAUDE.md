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
- Lint: `python3 tools/lint_okf.py div-free-amr/wiki` — must pass before commit.
- Commits: `docs(div-free-amr): ingest <source-slug>`.

## Status

**Corpus complete (2026-07-08): 61/61 sources ingested**, 97 conformant
pages, six deep-lint passes. Books and long reviews were scoped reads with
coverage recorded on their Source pages (Bossavit, Shashkov, Hiptmair
§§4–6, AFW 2006 §§2–11, Christiansen §§2–4, Crane body) — those are the
known re-ingestion targets if deeper coverage is ever needed. New sources
append per repo law; the worklist stays authoritative.

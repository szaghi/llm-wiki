# Bundle law — curvilinear-metric-discretization

Domain (user decision, 2026-10-13, `DECISIONS.md` D20):

* vector calculus and the integral theorems (divergence, Stokes,
  Green) that finite-volume and finite-difference forms rest on;
* curvilinear coordinates: scale factors, the metric tensor, the
  Jacobian, Christoffel symbols, covariant differentiation, vector
  operators in tensor form, conservative and non-conservative forms of
  the equations in general coordinates;
* the discretization of metrics: metric identities, the geometric
  conservation law, free-stream preservation, metric evaluation on
  curvilinear, overset and moving or deforming grids.

Out of scope: discrete divergence constraints (∇·B = 0) as such, and the
design of capturing schemes, except where a source ties them to the
metric terms.

It is a standalone second brain, independent of every other bundle and
agnostic of every other repository (`DECISIONS.md` D12, D17, D20).

## Corpus

- Primary archive: `~/papers/mosaic/curvilinear-metric-discretization/*.pdf` (read-only; Layer 1),
  self-contained per D17. Filenames follow
  `year-venue-firstauthorsurname-doi.pdf` with the DOI stripped of
  punctuation; treat the filename as a hint and verify identity against
  page 1 and Crossref.
- Founding source (2026-10-13): Riley, Hobson & Bence, *Mathematical
  Methods for Physics and Engineering*, 3rd ed. (Cambridge University
  Press, 2006; doi:10.1017/CBO9780511810763, verified on Crossref),
  filed as `2006-CUP-Riley-101017CBO9780511810763.pdf`, slug
  `riley-2006`. The same book founds four bundles; each reads only its
  own chapters: here Chs. 10 (vector calculus), 11 (line, surface and volume integrals), 26 (tensors). PDF page = printed page + 30.
- Further sources arrive as the user files them (their own database or
  `~/papers/re-download/`).

## Bundle specifics

- Notation registry: [`wiki/notation.md`](wiki/notation.md) is normative
  for every concept page. Extend it, and log the extension, before
  writing math that needs a symbol it lacks.
- Keys and slugs: `firstauthor-year[-b, …]`, the first author's surname
  in lowercase ASCII, the year that of the published issue.
- `status`: results proved or stated as standard in a textbook or a
  peer-reviewed source are `established`; the compiler's own
  derivations are marked as such and stay `hypothesis`.
- Bibliography: `wiki/bibliography.bib` plus the generated
  `wiki/bibliography.md` (D15). Riley et al. print no reference list:
  the works they cite in footnotes and the text of the chapters read are
  its reference list.
- Worklist: `tools/worklist.sh curvilinear-metric-discretization`.
- Lint: `python3 tools/lint_okf.py curvilinear-metric-discretization/wiki`. It must pass before
  commit.
- Commits: `docs(curvilinear-metric-discretization): ingest <source-slug>`.

## Status

**Scaffolded 2026-10-13** with the founding source `riley-2006`
(scoped read: Chs. 10 (vector calculus), 11 (line, surface and volume integrals), 26 (tensors)).

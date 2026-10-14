# Bundle law — fourier-analysis-of-schemes

Domain (user decision, 2026-10-13, `DECISIONS.md` D20):

* Fourier series and transforms as analysis tools: convergence
  (Dirichlet conditions), Gibbs phenomenon, Parseval's theorem,
  convolution, the discrete Fourier transform, and the Laplace transform
  as used for initial-value and stability problems;
* Fourier analysis of discretizations: von Neumann stability and the
  amplification factor, modified wavenumber, numerical dispersion and
  dissipation, spectral resolution and resolving efficiency of
  finite-difference and finite-volume schemes.

Out of scope: the design of particular schemes, except for the
Fourier-analysis results a source states about them.

It is a standalone second brain, independent of every other bundle and
agnostic of every other repository (`DECISIONS.md` D12, D17, D20).

## Corpus

- Primary archive: `~/papers/mosaic/fourier-analysis-of-schemes/*.pdf` (read-only; Layer 1),
  self-contained per D17. Filenames follow
  `year-venue-firstauthorsurname-doi.pdf` with the DOI stripped of
  punctuation; treat the filename as a hint and verify identity against
  page 1 and Crossref.
- Founding source (2026-10-13): Riley, Hobson & Bence, *Mathematical
  Methods for Physics and Engineering*, 3rd ed. (Cambridge University
  Press, 2006; doi:10.1017/CBO9780511810763, verified on Crossref),
  filed as `2006-CUP-Riley-101017CBO9780511810763.pdf`, slug
  `riley-2006`. The same book founds four bundles; each reads only its
  own chapters: here Chs. 12 (Fourier series), 13 (integral transforms), 27.5–27.6 (finite differences; differential equations). PDF page = printed page + 30.
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
- Worklist: `tools/worklist.sh fourier-analysis-of-schemes`.
- Lint: `python3 tools/lint_okf.py fourier-analysis-of-schemes/wiki`. It must pass before
  commit.
- Commits: `docs(fourier-analysis-of-schemes): ingest <source-slug>`.

## Status

**Scaffolded 2026-10-13** with the founding source `riley-2006`
(scoped read: Chs. 12 (Fourier series), 13 (integral transforms), 27.5–27.6 (finite differences; differential equations)).

# Bundle law — linear-elliptic-solvers

Domain (user decision, 2026-10-13, `DECISIONS.md` D20):

* linear algebra as used by discretized PDEs: vector spaces, linear
  operators, matrices, eigenproblems, similarity and diagonalisation,
  quadratic and Hermitian forms, conditioning;
* operator theory for boundary-value problems: adjoint and self-adjoint
  operators, Sturm–Liouville problems, eigenfunction expansions, Green's
  functions;
* elliptic problems (Poisson, Helmholtz, Laplace) and their boundary
  conditions, including isolated (free-space) boundaries;
* solvers for the resulting linear systems: direct methods, relaxation
  (Jacobi, Gauss–Seidel, SOR), Krylov methods, multigrid,
  preconditioning, FFT-based and Green's-function solvers, with their
  convergence theory.

Out of scope: time-dependent hyperbolic problems (bundle
`hyperbolic-pde-theory`), Fourier stability analysis of schemes
(`fourier-analysis-of-schemes`), and how a particular code couples a
solver to its mesh, except where a source presents that coupling as a
solver result.

It is a standalone second brain, independent of every other bundle and
agnostic of every other repository (`DECISIONS.md` D12, D17, D20).

## Corpus

- Primary archive: `~/papers/mosaic/linear-elliptic-solvers/*.pdf` (read-only; Layer 1),
  self-contained per D17. Filenames follow
  `year-venue-firstauthorsurname-doi.pdf` with the DOI stripped of
  punctuation; treat the filename as a hint and verify identity against
  page 1 and Crossref.
- Founding source (2026-10-13): Riley, Hobson & Bence, *Mathematical
  Methods for Physics and Engineering*, 3rd ed. (Cambridge University
  Press, 2006; doi:10.1017/CBO9780511810763, verified on Crossref),
  filed as `2006-CUP-Riley-101017CBO9780511810763.pdf`, slug
  `riley-2006`. The same book founds four bundles; each reads only its
  own chapters: here Chs. 8 (matrices and vector spaces), 17 (eigenfunction methods), 21.5 (Green's functions for inhomogeneous PDEs), 27.1–27.3 and 27.8 (numerical: equations, iteration, simultaneous linear equations, PDEs). PDF page = printed page + 30.
- Second source (2026-10-14, D21): Arfken, Weber & Harris, *Mathematical
  Methods for Physicists*, 7th ed. (Academic Press, 2013;
  doi:10.1016/C2009-0-30629-7, ISBN 978-0-12-384654-9, verified on
  Crossref), slug `arfken-2013`, filed as
  `2013-AcademicPress-Arfken-101016C20090306297.pdf`. Read here: Chs. 2 (determinants and matrices), 5 (vector spaces), 6 (eigenvalue problems), 8 (Sturm–Liouville theory), 10 (Green's functions).
  An ebook conversion: the PDF-to-printed page offset drifts, so cite
  printed page numbers. Its chapter-end "Additional Readings" are its
  reference list.
- Further sources: see `~/papers/mosaic/llm-wiki-planned-ingestions.md`
  (a plan outside the repository; ingested-ness is derived from Source
  pages).

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
- Worklist: `tools/worklist.sh linear-elliptic-solvers`.
- Lint: `python3 tools/lint_okf.py linear-elliptic-solvers/wiki`. It must pass before
  commit.
- Commits: `docs(linear-elliptic-solvers): ingest <source-slug>`.

## Status

**arfken-2013 staged 2026-10-14** (D21, scoped read): 1 new page (methods/variation-method), 15 updated; one Open contradiction (is a non-unitary similarity a change of basis? Riley §8.15 vs Arfken §5.6); bibliography 36 entries.

**Scaffolded 2026-10-13** with the founding source `riley-2006`
(scoped read: Chs. 8 (matrices and vector spaces), 17 (eigenfunction methods), 21.5 (Green's functions for inhomogeneous PDEs), 27.1–27.3 and 27.8 (numerical: equations, iteration, simultaneous linear equations, PDEs)).

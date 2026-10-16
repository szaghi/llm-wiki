# Bundle law — orthogonal-polynomials-and-quadrature

Domain (user decision, 2026-10-14, `DECISIONS.md` D21):

* orthogonal polynomials: weight functions and intervals, orthogonality
  and normalization, three-term recurrences, Rodrigues formulae,
  generating functions, zeros, the classical families (Legendre,
  Chebyshev, Jacobi, Gegenbauer, Hermite, Laguerre);
* the special functions built on them that numerical methods use:
  associated Legendre functions, spherical harmonics and their addition
  theorem, Bessel and spherical Bessel functions;
* quadrature: Gauss, Gauss–Radau and Gauss–Lobatto rules, nodes and
  weights, exactness and error, and the classical Newton–Cotes rules as
  contrast;
* their use as bases and quadratures of numerical methods: modal and
  nodal polynomial bases (spectral, DG, flux reconstruction),
  interpolation and Lebesgue constants, aliasing, multipole expansions.

Out of scope: special functions for their own sake (gamma, zeta,
hypergeometric, elliptic integrals) except where a page needs them, and
the design of particular DG or spectral schemes beyond their basis and
quadrature.

It is a standalone second brain, independent of every other bundle and
agnostic of every other repository (`DECISIONS.md` D12, D17, D21).

## Corpus

- Primary archive: `~/papers/mosaic/orthogonal-polynomials-and-quadrature/*.pdf` (read-only; Layer 1),
  self-contained per D17. Filenames follow
  `year-venue-firstauthorsurname-doi.pdf` with the DOI stripped of
  punctuation; treat the filename as a hint and verify identity against
  page 1 and Crossref.
- Founding sources (2026-10-14), two textbooks read in scope:
  - Riley, Hobson & Bence, *Mathematical Methods for Physics and
    Engineering*, 3rd ed. (Cambridge University Press, 2006;
    doi:10.1017/CBO9780511810763), `riley-2006`, file
    `2006-CUP-Riley-101017CBO9780511810763.pdf`: Ch. 18 (special
    functions) and §27.4 (numerical integration, Gaussian integration).
    PDF page = printed page + 30.
  - Arfken, Weber & Harris, *Mathematical Methods for Physicists*, 7th
    ed. (Academic Press, 2013; doi:10.1016/C2009-0-30629-7, ISBN
    978-0-12-384654-9, verified on Crossref), `arfken-2013`, file
    `2013-AcademicPress-Arfken-101016C20090306297.pdf`: §12.1
    (orthogonal polynomials), Ch. 14 (Bessel functions), Ch. 15
    (Legendre functions), §§18.1, 18.3, 18.4 (Hermite, Laguerre,
    Chebyshev). An ebook conversion: the PDF-to-printed page offset
    drifts, so cite printed page numbers.
- Further sources: see `~/papers/mosaic/llm-wiki-planned-ingestions.md`.

## Bundle specifics

- Notation registry: [`wiki/notation.md`](wiki/notation.md) is normative
  for every concept page. Extend it, and log the extension, before
  writing math that needs a symbol it lacks.
- Keys and slugs: `firstauthor-year[-b, …]`, the first author's surname
  in lowercase ASCII, the year that of the published issue.
- `status`: results proved or stated as standard in a textbook or a
  peer-reviewed source are `established`; the compiler's own
  derivations are labelled hypothesis-grade where they appear.
- Bibliography: `wiki/bibliography.bib` plus the generated
  `wiki/bibliography.md` (D15). Riley prints no reference list (works
  cited in the text are its list); Arfken's chapter-end "Additional
  Readings" are its reference list, for the chapters read.
- Worklist: `tools/worklist.sh orthogonal-polynomials-and-quadrature`.
- Lint: `python3 tools/lint_okf.py orthogonal-polynomials-and-quadrature/wiki`. It must pass before
  commit.
- Commits: `docs(orthogonal-polynomials-and-quadrature): ingest <source-slug>`.

## Status

**Scaffolded 2026-10-14** with the founding sources `riley-2006` and
`arfken-2013` (scoped reads above).

**2026-10-16:** `panici-2023` ingested (bundle-fit copy, D17; read in
full, extracted for the Zernike basis, axis regularity and radial
convergence). 3 sources, 24 OKF pages (20 concept pages, the registry, 3 Source pages), 89 bibliography entries.
Registry section 8 added (unit disc, Fourier–Zernike bases). Open: no
source yet defines Jacobi polynomials, Gauss–Jacobi rules, collocation
grids on the disc, or the ANSI/Fringe Zernike indexing schemes.

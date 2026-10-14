# Bundle law — hyperbolic-pde-theory

Domain (user decision, 2026-10-13, `DECISIONS.md` D20):

* classification of second-order and first-order PDEs, characteristics
  and the existence and uniqueness of solutions, boundary and initial
  data that make a problem well posed;
* solution methods for the model equations (wave, diffusion, Laplace):
  general solutions, separation of variables, transform methods;
* the ODE theory these rely on (characteristic ODEs, linear equations);
* hyperbolic systems and conservation laws as continuum objects: weak
  solutions, Rankine–Hugoniot conditions, entropy conditions, Riemann
  problems, characteristic boundary conditions.

Out of scope: discrete schemes (the high-order-capturing-schemes
bundle compiles those independently); continuum results are compiled
here even when a scheme paper states them.

It is a standalone second brain, independent of every other bundle and
agnostic of every other repository (`DECISIONS.md` D12, D17, D20).

## Corpus

- Primary archive: `~/papers/mosaic/hyperbolic-pde-theory/*.pdf` (read-only; Layer 1),
  self-contained per D17. Filenames follow
  `year-venue-firstauthorsurname-doi.pdf` with the DOI stripped of
  punctuation; treat the filename as a hint and verify identity against
  page 1 and Crossref.
- Founding source (2026-10-13): Riley, Hobson & Bence, *Mathematical
  Methods for Physics and Engineering*, 3rd ed. (Cambridge University
  Press, 2006; doi:10.1017/CBO9780511810763, verified on Crossref),
  filed as `2006-CUP-Riley-101017CBO9780511810763.pdf`, slug
  `riley-2006`. The same book founds four bundles; each reads only its
  own chapters: here Chs. 14–15 (first- and higher-order ODEs), 20 (PDEs: general and particular solutions), 21 (separation of variables, transform methods, Green's functions). PDF page = printed page + 30.
- Second source (2026-10-14, D21): Arfken, Weber & Harris, *Mathematical
  Methods for Physicists*, 7th ed. (Academic Press, 2013;
  doi:10.1016/C2009-0-30629-7, ISBN 978-0-12-384654-9, verified on
  Crossref), slug `arfken-2013`, filed as
  `2013-AcademicPress-Arfken-101016C20090306297.pdf`. Read here: Chs. 7 (ordinary differential equations) and 9 (partial differential equations).
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
- Worklist: `tools/worklist.sh hyperbolic-pde-theory`.
- Lint: `python3 tools/lint_okf.py hyperbolic-pde-theory/wiki`. It must pass before
  commit.
- Commits: `docs(hyperbolic-pde-theory): ingest <source-slug>`.

## Status

**arfken-2013 staged 2026-10-14** (D21, scoped read): 2 new pages (Helmholtz equation, Frobenius series solutions); one Open contradiction (Helmholtz Dirichlet eigenvalues for the minus sign: Arfken p. 413 vs Riley Ex. 20.25); bibliography 27 entries.

**Scaffolded 2026-10-13** with the founding source `riley-2006`
(scoped read: Chs. 14–15 (first- and higher-order ODEs), 20 (PDEs: general and particular solutions), 21 (separation of variables, transform methods, Green's functions)).

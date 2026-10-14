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
- Worklist: `tools/worklist.sh hyperbolic-pde-theory`.
- Lint: `python3 tools/lint_okf.py hyperbolic-pde-theory/wiki`. It must pass before
  commit.
- Commits: `docs(hyperbolic-pde-theory): ingest <source-slug>`.

## Status

**Scaffolded 2026-10-13** with the founding source `riley-2006`
(scoped read: Chs. 14–15 (first- and higher-order ODEs), 20 (PDEs: general and particular solutions), 21 (separation of variables, transform methods, Green's functions)).

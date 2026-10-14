# Directory Update Log

## 2026-10-14

* **Ingestion of [arfken-2013](/sources/arfken-2013.md)** (Arfken, Weber &
  Harris, *Mathematical Methods for Physicists*, 7th ed., 2013; D21), scoped
  read: preface, Chs. 3 (vector analysis) and 4 (tensors and differential
  forms) with exercises and Additional Readings; other chapters not read.
  Printed page numbers cited (ebook offset +12 in Ch. 3, +11 in Ch. 4);
  equations checked against page images where ambiguous; four misprints
  recorded on the Source page; no illegible range. Merge path against
  riley-2006.
  * Notation registry extended (marked "added 2026-10-14, arfken-2013"): a
    differential-forms section ($p$, $D$, $\Lambda^p$, $\alpha,\beta,\gamma$,
    basis 1-forms $dx^i$, $\wedge$, $d$, $\star$, $\Omega$/$\partial\Omega$,
    $\int_\Omega\alpha$) and the auxiliary $\mathbf y$, $\nabla_{\mathbf y}$,
    $x_0,y_0$.
  * Created 4 definitions: differential-form, wedge-product, hodge-star,
    exterior-derivative (continuum operators in `definitions/`).
  * Created 2 results: generalized-stokes-theorem, helmholtz-theorem.
  * Updated, with Arfken citations next to Riley's and Arfken's extensions:
    all 17 previous definitions, all 8 previous results, and the registry.
  * Contradictions: none opened. Qualifications recorded (both sides
    cited): connectivity hypothesis of the integral theorems (divergence
    theorem, Stokes' theorem, Green's theorem in the plane, Stokes' theorem
    for forms); continuity hypothesis of curl grad = 0 and div curl = 0
    (vector operator identities); sign of the metric's diagonal elements
    outside Euclidean space (metric tensor); naming of Green's identities;
    Arfken's reversed Jacobian labelling in Example 4.4.2 (Jacobian);
    Arfken's use of "Poincaré's lemma" for $d\circ d=0$ (exterior derivative).
  * riley-2006 Source page: one audit line (cited on the new
    generalized-stokes-theorem page).
  * Bibliography: 29 entries (was 4); 25 added — arfken-2013 itself and the
    24 works of its Chs. 3–4 Additional Readings (10 + 15 listed, 2 shared,
    plus the 1970 second edition named in an annotation); no DOI printed or
    added. Pending reference lists: 0 / 2.
  * Folder indexes, sources index and root reading guide (new section 5,
    *Differential forms*) updated.

## 2026-10-13

* **Scaffolding and ingestion of [riley-2006](/sources/riley-2006.md)**
  (Riley, Hobson & Bence, *Mathematical Methods for Physics and Engineering*,
  3rd ed., 2006), scoped read: prefaces, contents, Chs. 10 (vector calculus),
  11 (line, surface and volume integrals) and 26 (tensors), with exercises;
  other chapters not read. Equations checked against rendered page images
  where the text layer was garbled; no illegible range.
  * Notation registry seeded: [notation.md](/notation.md) (index conventions;
    coordinates $x^i$, $\xi^i$, $\bar\xi^i$ and reserved moving-grid symbols;
    bases $\mathbf e_k$, $\mathbf a_i$, $\mathbf a^i$; metric $g_{ij}$, $g$,
    $J=\det[\partial x^i/\partial\xi^j]$; fields and components; operators;
    curves, surfaces and volumes; auxiliary symbols).
  * Created 12 definitions: curvilinear-coordinates, scale-factors,
    covariant-and-contravariant-bases, metric-tensor, jacobian,
    christoffel-symbols, cartesian-tensor, general-tensor, relative-tensor,
    levi-civita-symbol, conservative-vector-field, vector-area-element.
  * Created 5 continuum-operator definitions: gradient, divergence, curl,
    laplacian, covariant-derivative (`definitions/`: `operators/` is
    reserved for discrete operators by repo law; it is empty for now).
  * Created 8 results: divergence-theorem, greens-identities, stokes-theorem,
    greens-theorem-in-the-plane, integral-definitions-of-grad-div-curl,
    closed-surface-vector-area, vector-operator-identities, quotient-law.
  * Created source page sources/riley-2006.md; folder indexes and the root
    reading guide.
  * Bibliography: 4 entries (riley-2006 and the 3 works of the Ch. 26
    opening footnote: dinverno-1992, foster-2006, schutz-1985); Chs. 10–11
    cite none.

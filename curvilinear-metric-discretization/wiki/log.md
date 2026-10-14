# Directory Update Log

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

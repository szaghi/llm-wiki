# Directory Update Log

## 2026-10-16

Three application papers ingested as D17 bundle-fit copies (the human's
instruction "do the bundle-fit copies"): overlapping works read for this
bundle's subject, in this bundle's notation, with no link to any other
bundle. Scoped reads (D21 practice): coordinates, metrics, Jacobians,
operators and their discretization only; reference lists merged complete.
Ingestion order jiang-2024, liu-2024, seto-2023.

* **Ingestion of [seto-2023](/sources/seto-2023.md)** (Seto, Dudson, Xu &
  Yagi, *Comput. Phys. Commun.* 283:108568, 2023), scoped read: §§1–3, the
  flute-ordering comparison of §4, eq. (38), summary, App. A, references.
  * Notation registry: $\nabla_\parallel^2$, $\nabla_\perp^2$,
    $h_\Psi,h_\vartheta,h_\varphi$, $B_{\mathrm p}$, $B_{\mathrm t}$,
    $\mathrm i$ (marked "added 2026-10-16, seto-2023").
  * Created software/bout-plus-plus.
  * Updated field-aligned-coordinates, magnetic-flux-coordinates,
    shifted-metric (quasi-ballooning coordinates), laplacian (perpendicular
    and parallel Laplacians, expanded form), scale-factors (orthogonal flux
    row), metric-tensor, jacobian, covariant-and-contravariant-bases,
    gradient, divergence, curvilinear-coordinates.
  * Contradictions: none opened; it sides with jiang-2024 on the
    twist-shift sign. Misprints recorded on the Source page (eqs. (A.12),
    (A.20)).
  * Bibliography: 55 references, 52 new entries and 3 merged
    (dudson-2009, scott-2001, beer-1995), plus the source's own entry;
    Hazeltine–Meiss 1985 is keyed `hazeltine-1985-b` against Jiang's
    `hazeltine-1985`; DOIs as printed.
* **Ingestion of [liu-2024](/sources/liu-2024.md)** (Liu, Jiang, Liu, Zhang
  & Fu, *Phys. Plasmas* 31:073905, 2024), scoped read: §I, §II, App. C
  (convergence), references.
  * Updated field-aligned-coordinates (full field-aligned metric, normalised
    $\xi^1$, flux-tube contrast, flute-ordering order estimate),
    magnetic-flux-coordinates (PEST; metric from $R(\Psi,\vartheta)$,
    $z(\Psi,\vartheta)$), shifted-metric (dissipation alternative,
    qualification of Jiang's 7% bias), gmec, metric-tensor (inverse by
    cofactors), jacobian, covariant-and-contravariant-bases, curl,
    curvilinear-coordinates.
  * **Contradiction opened** on field-aligned-coordinates: the sign of the
    twist-shift (Liu eq. (9) against Jiang eq. (26) and Seto eq. (9)); the
    compiler's check from the shared definition supports Jiang and Seto;
    left open for the human.
  * Recorded on the Source page: eq. (27) is four times the inverse metric
    with the printed unrestricted sums.
  * Bibliography: 41 references, 35 new entries plus the source's own entry,
    5 merged with jiang-2024's references (dudson-2009, scott-2001,
    pheatt-2008, hirshman-1983, dudt-2020). Ref. 29, printed as
    arXiv:2402.09324, is the preprint of the ingested jiang-2024 and is kept
    distinct as `jiang-2024-c` (human preprint ruling, 2026-10-16). Ref. 19 (Fu et
    al. 2006, M3D-K) re-keyed `fu-2006-b` against Jiang's `fu-2006`.
* **Ingestion of [jiang-2024](/sources/jiang-2024.md)** (Jiang, Liu, Liu,
  Bao & Fu, *Phys. Plasmas* 31:073904, 2024), scoped read: §I, §III, §IV A–C
  and F, §V A, §VI C, §VII, §VIII, §X, App. A, C, D, references.
  * Notation registry extended with a section *Magnetic geometry: flux and
    field-aligned coordinates* ($\mathbf B$, $B$, $\hat{\mathbf b}$,
    $\nabla_\parallel$, $\nabla_\perp$, $k_\parallel,k_\perp$,
    $(\Psi,\vartheta,\varphi)$, $\varphi_{\mathrm B}$,
    $\mathbf a_\Psi,\mathbf a_\vartheta,\mathbf a_\varphi$, $q$, $q'$,
    $q_{\mathrm{loc}}$, $\chi$, $\Psi_0,\vartheta_0$, $I$, $\sigma_{[k]}$,
    grid subscripts $(\cdot)_{[k]}$, $\mathcal C_\ell$, $n_\varphi$,
    $m_\vartheta$); field-aligned coordinates are written $\xi^i$.
  * Created definitions/field-aligned-coordinates,
    definitions/magnetic-flux-coordinates, methods/shifted-metric,
    software/gmec.
  * Updated metric-tensor, jacobian, covariant-and-contravariant-bases,
    curvilinear-coordinates, divergence, curl, laplacian (agreeing
    citations; non-orthogonal example; expanded form for discretization).
  * Contradictions: none opened. Recorded on the Source page: eq. (38) states
    a stronger condition than needed; eq. (43) prefactor and symbol
    inconsistent with eq. (42); eq. (52) against eq. (48).
  * Bibliography: 22 references, all new entries, plus the source's own
    entry. Its text announces Part II
    but its reference list does not cite it, so liu-2024 has no `citedby`.
* Bibliography after the three: 142 entries (was 29; Liu's arXiv citation of Part I kept distinct as `jiang-2024-c`). Pending reference
  lists: 0 / 5.
* Folder indexes (definitions, methods, software, sources) and the root
  reading guide (new section 6) updated; bundle status in CLAUDE.md
  updated.

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

# Directory Update Log

## 2026-07-08

* **Ingestion**: [Hiptmair (2002)](/sources/hiptmair-2002.md) — **scoped
  read**: §§1–3 of 104 pp. compiled; §§4–6 (eigenvalue/source problems,
  regularization) explicitly not read, flagged on the Source page for a
  follow-up pass. Created [Whitney forms](/definitions/whitney-forms.md).
  Merged the cohomology-aware FE counterpart into
  [Discrete exactness theorems](/results/discrete-exactness-theorems.md).

* **Ingestion**: [Tóth & Roe (2002)](/sources/toth-roe-2002.md) — text
  extraction. Created
  [Locality limits of divergence-preserving transfer](/results/transfer-operator-locality-limits.md).
  Merged into [$P_D$](/operators/divergence-free-prolongation.md) (second,
  independent construction) and
  [Divergence-free reconstruction](/methods/divergence-free-reconstruction.md).
  **Contradictions development**: the Balsara-vs-Tóth AMR-nesting dispute at
  [CT–finite-volume equivalence](/results/ct-finite-volume-equivalence.md)
  is effectively settled by convergence — Tóth's own 2002 conclusion
  recommends face-centered storage for divergence-free AMR.

* **Ingestion**: [Hyman & Shashkov (1997)](/sources/hyman-shashkov-1997.md)
  — text extraction. Created
  [Discrete exactness theorems](/results/discrete-exactness-theorems.md)
  (the discrete Poincaré lemma with converses) and
  [Support-operator method](/definitions/support-operator-method.md).
  Opens the mimetic branch of the bundle.

* **Deep lint #1** (after 11 ingestions). Findings and fixes: (1) notation
  drift — [flux-CT](/methods/flux-ct.md) used base-scheme flux symbols
  $f^{x,*}$ without registry backing; fixed by extending
  [notation](/notation.md) with the starred base-scheme-quantity
  convention. (2) $\psi_h$/$\psi$ inconsistency on
  [GLM cleaning](/methods/glm-divergence-cleaning.md); unified. (3) Tag
  synonyms consolidated: `divergence-free` → `divergence-constraint`
  (3 pages), `collocated` → `collocation` (1 page). No stale
  contradictions (both blocks current, no supersession available in
  ingested corpus); no orphan pages.

* **Ingestion**: [Dedner et al. (2002)](/sources/dedner-2002.md) — text
  extraction. Created
  [GLM divergence cleaning](/methods/glm-divergence-cleaning.md). Merged
  into [Eight-wave](/methods/eight-wave.md) (conservation contrast) and
  [Projection method](/methods/projection-method.md) (elliptic limit of the
  GLM family). Completes the constraint-method taxonomy: exact-algebraic
  (CT), tolerance (projection), truncation (eight-wave), controlled (GLM).

* **Ingestion**: [Balsara (2001)](/sources/balsara-2001.md) — text
  extraction. Created
  [Divergence-space prolongation $P_D$](/operators/divergence-free-prolongation.md)
  (first Operator page) and
  [Electric-field correction](/methods/electric-field-correction.md).
  Merged into [Divergence-free reconstruction](/methods/divergence-free-reconstruction.md)
  (now multi-source), [Refluxing](/methods/refluxing.md), and
  [CT–finite-volume equivalence](/results/ct-finite-volume-equivalence.md)
  — **second `Contradictions` block**: Balsara's nesting claim against the
  zone-centered formulation on AMR hierarchies (open, no supersession).

* **Ingestion**: [Londrillo & Del Zanna (2000)](/sources/londrillo-delzanna-2000.md)
  — text extraction. Created
  [Divergence-free reconstruction](/methods/divergence-free-reconstruction.md).
  Merged into [Constrained transport](/methods/constrained-transport.md)
  (high-order extension) and [Staggered grid](/definitions/staggered-grid.md).
  **First `Contradictions` block** recorded (Tóth vs Londrillo–Del Zanna on
  the necessity of staggering), with scoped resolution, no supersession.

* **Ingestion**: [Powell et al. (1999)](/sources/powell-1999.md) — text
  extraction. No new pages; grounded
  [Eight-wave formulation](/methods/eight-wave.md) in its primary source
  (symmetrizable form, divergence wave, discrete source term) and layered
  it against Tóth's assessment.

* **Ingestion**: [Berger & Colella (1989)](/sources/berger-colella-1989.md) —
  text extraction; DOI absent from the scan, Crossref-verified. Created
  [Block-structured AMR](/definitions/block-structured-amr.md) and
  [Refluxing](/methods/refluxing.md). First concrete instances of registry
  operators $R$ (conservative averaging) and $\Gamma$ (bilinear +
  linear-in-time ghost fill). Opens the AMR branch of the bundle.

* **Ingestion**: [Strand (1994)](/sources/strand-1994.md) — fully image-only
  scan, read visually (21/21 pages). Created
  [Summation by parts (SBP)](/definitions/summation-by-parts.md) and
  [SBP operator existence and families](/results/sbp-operator-existence.md).
  **Registry extension**: SBP block ($\mathsf{H}, \mathsf{Q}, \mathsf{D}_1$)
  — literature's $H$ renamed to avoid collision with coarse spacing $H$.
  Opens the SBP branch of the bundle.

* **Ingestion**: [Chorin (1968)](/sources/chorin-1968.md) — text extraction.
  Merged into [Projection method](/methods/projection-method.md) (origin:
  discrete Hodge decomposition; collocated central operators with
  $2\Delta x$-spaced composite Laplacian). No new pages — the method page
  already existed from the Tóth ingestion; this run grounded it in its
  primary source.

* **Ingestion**: [Yee (1966)](/sources/yee-1966.md) — read visually (6/6
  pages). Created [Yee scheme (FDTD)](/methods/yee-scheme.md). Merged into
  [Staggered grid](/definitions/staggered-grid.md) (EM instance; time
  staggering). Integrity note: divergence preservation is *implicit* in
  Yee (1966) — recorded as unstated, not attributed to the paper.

* **Ingestion**: [Harlow & Welch (1965)](/sources/harlow-welch-1965.md) —
  text-poor scan, read visually (8/8 article pages). Created
  [MAC method](/methods/mac-method.md). Merged into
  [Staggered grid](/definitions/staggered-grid.md) (origin of staggering) and
  [Exact discrete divergence](/properties/exact-discrete-divergence.md)
  (velocity/incompressibility ancestry).

* **Ingestion**: [Tóth (2000)](/sources/toth-2000.md) — clean text extraction.
  Created [Flux-CT and the Godunov CT variants](/methods/flux-ct.md),
  [Projection method](/methods/projection-method.md),
  [Eight-wave formulation](/methods/eight-wave.md),
  [CT–finite-volume equivalence](/results/ct-finite-volume-equivalence.md),
  [Conservation–orthogonality incompatibility](/results/conservation-orthogonality-incompatibility.md).
  Merged into [Constrained transport](/methods/constrained-transport.md),
  [Exact discrete divergence](/properties/exact-discrete-divergence.md),
  [Staggered grid](/definitions/staggered-grid.md).
  **Registry extension**: $D_h^{\mathrm{f}}/D_h^{\mathrm{c}}/D_h^{\mathrm{k}}$
  divergence-stencil superscripts added to [notation](/notation.md).
  Pilot ingestion #2 (merge path).

* **Ingestion**: [Evans & Hawley (1988)](/sources/evans-hawley-1988.md) —
  image-only scan, read visually (19/19 pages). Created
  [Constrained transport](/methods/constrained-transport.md),
  [Exact discrete divergence](/properties/exact-discrete-divergence.md),
  [Staggered grid](/definitions/staggered-grid.md). Pilot ingestion #1
  (visual-read path).

* **Creation**: Bundle scaffolded — constitution, taxonomy folders, linter,
  derived worklist, and the [Notation registry](/notation.md) seeded as
  wiki-native law.

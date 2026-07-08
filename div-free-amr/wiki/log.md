# Directory Update Log

## 2026-07-08

* **Ingestion**: [Etienne, Liu & Shapiro (2010)](/sources/etienne-2010.md)
  — text extraction. Created
  [Vector-potential evolution](/methods/vector-potential-evolution.md):
  the third AMR strategy — transfer the unconstrained potential, take the
  curl; the $P_D$ problem dissolved by the exactness converse, at the
  price of derivative count and gauge control.

* **Ingestion**: [Mignone et al. (2012)](/sources/mignone-2012.md) — text
  extraction. No new pages; merged the AMR realization (no dedicated
  magnetic transfer operators under collocated+GLM) into
  [GLM divergence cleaning](/methods/glm-divergence-cleaning.md).

* **Ingestion**: [Miniati & Martin (2011)](/sources/miniati-martin-2011.md)
  — text extraction. No new pages; merged reflux-curl production naming
  into [Electric-field correction](/methods/electric-field-correction.md)
  and the **subcycling caveat** (time interpolation breaks the
  divergence-free premise for ghost fills) into
  [$P_D$](/operators/divergence-free-prolongation.md).

* **Ingestion**: [Wang & Petersson (2019)](/sources/wang-petersson-2019.md)
  — text extraction. No new pages; merged the strong-imposition (SBP-GP)
  alternative and the SAT time-step trade into
  [SBP-SAT](/methods/sbp-sat.md).

* **Ingestion**: [Almquist, Wang & Werpers (2019)](/sources/almquist-2018.md)
  — text extraction; authorship Crossref-verified. No new pages; merged the
  interpolation accuracy bound ($q_{C2F}+q_{F2C} \le 2p+1$) and the
  order-preserving two-pair remedy into
  [SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md).

* **Deep lint #3** (after 30 ingestions). Findings and fixes: (1) tag
  synonym `2-1-interface` consolidated into `coarse-fine-interface`
  (2 pages); (2) FEEC element families
  ($\mathcal{P}_r\Lambda^k, \mathcal{P}_r^-\Lambda^k$) recur across three
  concept pages — registered in [notation](/notation.md). Both
  `Contradictions` blocks current; timestamps uniform; no orphans.

* **Ingestion**: [Nissen et al. (2014)](/sources/nissen-2014.md) — text
  extraction. No new pages; merged junction/corner treatment into
  [SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md)
  (resolving the pending pointer) and the block-oriented SAMR variant into
  [Block-structured AMR](/definitions/block-structured-amr.md).

* **Ingestion**: [Christiansen et al. (2011)](/sources/christiansen-2011.md)
  — **scoped read** (§5 at claim level; §§2–4 out of domain, not
  compiled). No new pages; merged the finite-element-systems
  generalization into [FEEC](/definitions/finite-element-exterior-calculus.md).

* **Ingestion**: [Arnold, Falk & Winther (2009)](/sources/arnold-falk-winther-2009.md)
  — **scoped read** (§§1, 3 closely). No new pages; merged the two-hypothesis
  master stability criterion into
  [FEEC](/definitions/finite-element-exterior-calculus.md).

* **Ingestion**: [Arnold, Falk & Winther (2006)](/sources/arnold-falk-winther-2006.md)
  — **scoped read** (§1 of 155 pp.; technical sections flagged unread).
  Created [FEEC](/definitions/finite-element-exterior-calculus.md). Merged
  into [Whitney forms](/definitions/whitney-forms.md) (two-family
  hierarchy).

* **Ingestion**: [Mignone & Tzeferacos (2010)](/sources/mignone-tzeferacos-2010.md)
  — text extraction. No new pages; merged CTU-GLM production realization,
  EGLM trade, and the same-code three-way comparison into
  [GLM divergence cleaning](/methods/glm-divergence-cleaning.md).

* **Ingestion**: [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md)
  — text extraction. No new pages; merged into
  [Constrained transport](/methods/constrained-transport.md) (unsplit CTU,
  upwind $\mathcal{E}^c$) and
  [Exact discrete divergence](/properties/exact-discrete-divergence.md)
  (field-loop test as stencil-consistency detector).

* **Ingestion**: [Fromang et al. (2006)](/sources/fromang-2006.md) — text
  extraction. No new pages; merged into
  [Block-structured AMR](/definitions/block-structured-amr.md)
  (tree-based/octree variant distinguished) and
  [Constrained transport](/methods/constrained-transport.md) (production
  deployment). Interface-prolongation details deferred to Teyssier et al.
  2006, not in corpus — recorded as a gap.

* **Ingestion**: [Brezzi, Lipnikov & Shashkov (2005)](/sources/brezzi-lipnikov-shashkov-2005.md)
  — text extraction. Created
  [MFD convergence on polyhedral meshes](/results/mfd-convergence.md)
  (2:1 interfaces enter the proven class as degenerate polyhedra). Merged
  into [Support-operator method](/definitions/support-operator-method.md).

* **Ingestion**: [Desbrun et al. (2005)](/sources/desbrun-hirani-2005.md) —
  text extraction. Created
  [Discrete exterior calculus](/definitions/discrete-exterior-calculus.md).
  Merged the DEC Poincaré lemma into
  [Discrete exactness theorems](/results/discrete-exactness-theorems.md)
  (third independent derivation). Formality caveat recorded (convergence
  mostly unproved, per the authors). Hirani (2003) thesis to be a scoped
  supplement later.

* **Ingestion**: [Clemens & Weiland (2001)](/sources/clemens-weiland-2001.md)
  — text extraction. Created
  [Finite integration technique](/methods/finite-integration-technique.md).
  Merged into [Whitney forms](/definitions/whitney-forms.md) (Hodge/mass
  matrix identity).

* **Deep lint #2** (after 20 ingestions). Findings and fixes: (1) registry
  gap — $\mathsf{D}_2$ used on the [SBP page](/definitions/summation-by-parts.md)
  but unregistered; added to [notation](/notation.md). (2) Redundant tag
  `summation-by-parts` removed from the Strand source (duplicate of `sbp`).
  (3) The [staggered-grid Contradictions block](/definitions/staggered-grid.md)
  now cross-references the Tóth–Roe 2002 development recorded at the
  equivalence page. $D_h$ stencil superscripts fully consistent (f/c/k);
  no orphans; $\mathcal{D}$ and glue-space remain deliberately inline-named.

* **Ingestion**: [Kozdon & Wilcox (2015)](/sources/kozdon-wilcox-2015.md) —
  text extraction. No new pages; merged the glue-space generalization into
  [SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md).

* **Ingestion**: [Mattsson & Carpenter (2010)](/sources/mattsson-carpenter-2010.md)
  — text extraction. Created
  [SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md)
  (second Operator page). Merged into [SBP-SAT](/methods/sbp-sat.md)
  (nonconforming extension). **Registry extension**: interface
  interpolation block ($I_{C2F}, I_{F2C}$, adjoint condition).

* **Ingestion**: [Mattsson & Nordström (2004)](/sources/mattsson-nordstrom-2004.md)
  — text extraction. No new pages; merged second-derivative SBP operators
  into [SBP](/definitions/summation-by-parts.md).

* **Ingestion**: [Balsara (2004)](/sources/balsara-2004.md) — text
  extraction; **filename DOI tag found wrong**, identity Crossref-verified
  (10.1086/381377). Consolidation source: no new pages; merged into
  [Divergence-free reconstruction](/methods/divergence-free-reconstruction.md)
  (face-variable limiting, WENO, curvilinear/unstructured),
  [Flux-CT](/methods/flux-ct.md) (direct edge EMFs supersede averaging),
  [Eight-wave](/methods/eight-wave.md) (Issue-3 critique: C0 normal
  continuity removes the motivating premise).

* **Ingestion**: [Nordström & Carpenter (1999)](/sources/nordstrom-carpenter-1999.md)
  — text extraction; report number as permanent identifier (no DOI exists).
  Created [SBP-SAT technique](/methods/sbp-sat.md). Merged into
  [SBP](/definitions/summation-by-parts.md). Scope note recorded: this is
  the *conforming*-interface baseline; nonconforming 2:1 SBP interfaces are
  later corpus papers.

* **Ingestion**: [Almgren et al. (1998)](/sources/almgren-1998.md) — text
  extraction. Created [AMR projection method](/methods/amr-projection-method.md)
  and [Free-stream preservation](/properties/free-stream-preservation.md).
  Merged into [MAC method](/methods/mac-method.md) (afterlife as MAC
  projection), [Refluxing](/methods/refluxing.md) (elliptic
  generalization), [Projection method](/methods/projection-method.md).

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

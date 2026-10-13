# Directory Update Log

## 2026-10-13

* **Frontier batch: ingested [Balsara & Spicer (1999)](/sources/balsara-spicer-1999.md)
  and [Brio & Wu (1988)](/sources/brio-wu-1988.md)**, the two most-cited
  works the bundle had not ingested (cited by 37 and 19 of its sources),
  from PDFs copied out of a sibling archive into this bundle's (98 sources).
  * Balsara & Spicer, the primary source of flux-CT: extended
    [flux-CT](/methods/flux-ct.md) (eqs. 7–9 and 13–15, the separately
    evolved cell-centred field and the optional energy correction, the
    switched variant eq. 26; their "no significant numerical diffusion"
    written as a qualification beside Gardiner & Stone's halved viscosity,
    not as a contradiction: the claims point in opposite directions),
    [constrained transport](/methods/constrained-transport.md) (the history
    they give), [exact discrete divergence](/properties/exact-discrete-divergence.md)
    (no proof or diagnostic in the primary source; round-off vs
    discretization-error wording), [positivity–divergence coupling](/results/positivity-divergence-coupling.md),
    [CT–finite-volume equivalence](/results/ct-finite-volume-equivalence.md)
    and [staggered grid](/definitions/staggered-grid.md) (evidence neither
    way on the open necessity entry).
  * Brio & Wu: extended [eight-wave](/methods/eight-wave.md) (the seven-wave
    system and its renormalized eigenvectors) and the
    [rotated shock tube](/benchmarks/rotated-shock-tube.md) (the unrotated
    problem); no separate benchmark page.
  * **Notation:** registered $\Delta t$ and the time-level superscripts
    $n$, $n+1/2$, $n+1$ in the [registry](/notation.md); several concept
    pages already used them unregistered.
  * **Compiler correction** on [Tóth (2000)](/sources/toth-2000.md): the
    table remark "primary sources not yet ingested" now says the
    Balsara–Spicer primary source is ingested.
  * **Bibliography** (3639 entries): 52 references merged; keys
    balsara-1999 and brio-1988 renamed to the slugs; Evans & Hawley printed
    as 1989 and Brackbill & Barnes as 35:462 by Balsara & Spicer (noted);
    three Harten 1983 works resolved by venue; Osher & Chakravarthy (1983)
    kept apart from Osher & Sanders (Crossref).

* **Ingested [Hoppe et al. (2022)](/sources/hoppe-2022.md) and
  [Irsalinda et al. (2026)](/sources/irsalinda-2026.md)**, the user's manual
  downloads for the AMR-framework class (96 sources).
  * Hoppe et al. (ALPACA): block octree with multiresolution refinement,
    halos advanced with predicted right-hand sides, local time stepping,
    a resolution-jump flux correction stated by citation only; no
    divergence content. Extended [block-structured AMR](/definitions/block-structured-amr.md)
    and [refluxing](/methods/refluxing.md).
  * Irsalinda et al.: "mesh refinement" means adaptive resampling of PINN
    collocation points, outside the bundle's AMR sense; no divergence
    content; its comparative claims are not supported by its own tables.
    Source page only (orphan by design).
  * Bibliography: 149 references merged (3618 entries); LeVeque's 2nd
    edition is `leveque-1992`; Munz, Ommes & Schneider is `munz-2000-b`;
    Cohen, Kaber, Müller & Postel is `cohen-2001-b`; Wang et al. (2023,
    curriculum learning) is `wang-2023-b`.
* **Deep lint #9** (10 ingestions since #8: couch-2021, balsara-kim-2016,
  the AMR-frameworks batch, hoppe-2022, irsalinda-2026). Fixed:
  * Bibliography: own entries added for `knapp-2026`,
    `jaber-essel-sullivan-2025` and `irsalinda-2026`; the ingested Aftosmis
    paper, cited as `aftosmis-2004`, rekeyed `aftosmis-berger-murman-2004`
    with its DOI; `almgren-2010` given its ten authors, title and DOI;
    `colella-woodward-1985` corrected to Colella & Glaz and rekeyed
    `colella-glaz-1985-b`; DOIs added to `balsara-kim-2016` and
    `zaghi-2023`; `kutta-1901` venue corrected to Z. Math. Phys.
  * Notation: the flux-CT edge-field formula in paper symbols rewritten in
    words with $E_h$; two unregistered time-step symbols on the
    block-structured-AMR page written out; the Morton bit count renamed
    $b$ (it reused the SFC index $m$).
  * Claims: Zaghi et al. (2023) no longer called independent support on
    the ADAM page (same first author); CASTRO's synchronization "applies",
    not "confirms", the elliptic-interface lesson; the coarsening ratio
    "> 7" marked as the authors' unquantified statement beside their own
    example (about 5.6); Knapp's scaling described as near-ideal to 2^15
    (about 63% efficiency to 2^17); ALPACA's weak scaling given with the
    figure reading.
  * Scope: the block-structured-AMR "Defining discipline" heading scoped
    to the Berger–Colella formulation, and the "same object in both
    flavors" sentence scoped to 2:1-balanced trees, since Knapp and
    ALPACA depart from both.
  * Staleness: the staggering contradiction's lead sentence; timestamps.
  * Tags: `relativistic-mhd` merged into `relativistic`, `octree` into
    `tree-amr` (also added to ADAM), `load-balancing` dropped beside
    `partitioning`.
  * Audit list: couch-2021 now records its citation by AMReX.

* **Source-page paths made absolute** on user instruction, as the repo
  schema asks: `local_file` in all 94 Source pages now reads
  `/home/stefano/...` instead of `~/...`. Every path was checked to exist.
  Citation lines in page bodies are unchanged.

## 2026-10-12

* **Batch: AMR frameworks and octrees from the ADAM paper collection** (6
  sources, staged as one unit). The user assigned this class to the bundle
  (2026-10-12); the scope note in bundle law records it.
  * **Readers.** Papers were read by parallel subagents into scratch notes
    and reference fragments. The compiler wrote every page from those
    notes.
  * **Archive copies.** Three were copied from the collection: AMReX,
    Aftosmis et al. and Knapp et al. Three repository copies were moved
    in from a fresh download: Zaghi et al., Jaber et al. and CASTRO.
  * **Left out.** Baert et al. (2013), on out-of-core voxel octrees, is
    computer graphics and outside the scope.
  * Ingested:
    * [Zhang et al. (2019)](/sources/zhang-2019.md), the AMReX software
      paper;
    * [Aftosmis, Berger & Murman (2004)](/sources/aftosmis-berger-murman-2004.md),
      the extended abstract, not the final paper;
    * [Knapp et al. (2026)](/sources/knapp-2026.md), an arXiv preprint;
      the collection's key "david-2026" used the first author's given
      name;
    * [Zaghi et al. (2023)](/sources/zaghi-2023.md), the published
      version;
    * [Jaber, Essel & Sullivan (2025)](/sources/jaber-essel-sullivan-2025.md),
      arXiv v3;
    * [Almgren et al. (2010)](/sources/almgren-2010.md), CASTRO, arXiv v1.

    None of the six has divergence-constraint content.
  * Created:
    * [Space-filling curve](/definitions/space-filling-curve.md) (Morton
      and Peano–Hilbert; four sources plus one counterexample);
    * [AMReX](/software/amrex.md) and [CASTRO](/software/castro.md).
  * Updated:
    * [Block-structured AMR](/definitions/block-structured-amr.md): the
      CASTRO nesting rules and code taxonomy; subcycling as a choice
      (AMReX, ADAM); subcycling without time interpolation (Jaber et al.);
      four more tree variants.
    * [Refluxing](/methods/refluxing.md): CASTRO's second flux register
      for the gravitational potential, and codes without a register.
    * [AMR projection method](/methods/amr-projection-method.md): the
      self-gravity synchronization as an elliptic analog.
    * [Point-value restriction bound](/results/point-value-restriction-compatibility.md):
      two data points from Jaber et al. Cubic ghost fill is more accurate
      than linear, and a cubic restriction was unstable.
    * [ADAM](/software/adam.md): a published-record section. Zaghi et al.
      (2023) support the octree, 2:1 balance, Morton-keyed tree, GPU-resident
      field and WENO lineage. At its 2023 state the code differs in two
      respects (CUDA Fortran rather than OpenACC; second-order rather than
      tricubic ghost fill), recorded as version differences. The paper is
      silent on every divergence claim, so the page keeps
      `status: hypothesis`.
  * [Notation registry](/notation.md): $l$, $r$, $m(E)$, $\phi_{\mathrm g}$.
  * **Bibliography.** 316 references merged with `tools/bib_merge.py`.
    * The resolver's aliases were reviewed, with overrides for
      multi-author keys (`berger-colella-1989`, `jiang-shu-1996`,
      `harten-lax-1983`).
    * `aftosmis-1998` was sent to the wrong key by the resolver and
      corrected.
    * Venue identities were settled with Crossref:
      * JCP 59:264 is Colella & Glaz (1985). It merges onto
        `colella-woodward-1985`, whose citing source had misattributed
        it; a note records this.
      * Berger & Rigoutsos: the report and the IEEE journal version.
      * Taylor (1950), printed as 201:192, matches neither part on
        Crossref and is kept apart as `taylor-1950-b`.
    * 10 reviewed silences (FLAGS 0). A per-fragment collision check and a
      cross-fragment venue sweep were clean, and so was `--dupes`.
    * The malformed AMReX self-entry (author list "et, al.") was corrected
      to the 17 Crossref authors.
    * 3227 → 3487 entries.

## 2026-10-09

* **Ingested [Balsara & Kim (2016)](/sources/balsara-kim-2016.md)** (J. Comput. Phys.
  312:357–384, Version of Record; archive copy added from the high-order bundle's
  archive per D17). Gap found by cross-checking the ADAM paper collection against
  this bundle.
  * Updated [Staggered grid](/definitions/staggered-grid.md): the unscoped
    "any divergence-free formulation requires a Yee-type mesh" premise, attributed
    to the necessity side as a citation, not as evidence. The scoped resolution
    is unchanged.
  * Updated [Flux-CT](/methods/flux-ct.md),
    [Upwind constrained transport](/methods/upwind-constrained-transport.md) and
    [Constrained transport](/methods/constrained-transport.md): edge fields from a
    two-dimensional MuSIC Riemann solver, the RMHD finite-volume realization, and
    the unverified no-doubled-dissipation claim.
  * Bibliography: the existing entry `balsara-2016-d` was re-keyed to
    `balsara-kim-2016` (the bundle's two-author slug convention), and the 73-entry
    reference list was merged: 19 new works, 54 existing, 7 placeholder titles
    upgraded. Merged with `tools/bib_merge.py` for its collision checks. The
    resolver's aliases were reviewed by vol:page, and the fragment's first-author
    keys of ingested sources were mapped onto their multi-author keys
    (`gardiner-stone-2005`, `gardiner-stone-2008`, `jiang-shu-1996`,
    `mccorquodale-colella-2011`). `komissarov-2006-b` (AIP Conf. Proc. 856:129) was
    split from `komissarov-2006` (MNRAS 368:993). 3208 → 3227 entries.

## 2026-10-08

* **Layer-1 renames (user-authorized):** three archive filenames now embed
  the Crossref-verified DOIs found by the DOI audit below.
  * `2013-JCP-Kreeft-101016jjcp201212028.pdf` →
    `2013-JCP-Kreeft-101016jjcp201210043.pdf`
  * `1994-JCP-Strand-101006jcph19941023.pdf` (and its `.ocr.txt` sidecar) →
    `1994-JCP-Strand-101006jcph19941005.pdf`
  * `2020-JCP-Trask-101016jjcp2020109187.pdf` →
    `2020-JCP-Trask-101016jjcp2019109187.pdf`

  `local_file` and the Citations paths were updated on
  [Kreeft & Gerritsma (2013)](/sources/kreeft-gerritsma-2013.md),
  [Strand (1994)](/sources/strand-1994.md) and
  [Trask et al. (2020)](/sources/trask-2020.md).

* **Maintenance on user instruction:** the Gardiner filename fix, the eymard
  fold, and a DOI audit.
  * **Layer-1 rename** (user-authorized):
    `2008-JCP-Gardiner-101016jjcp200712003.pdf` was renamed to
    `2008-JCP-Gardiner-101016jjcp200712017.pdf`, and `local_file` on
    [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md) was updated.
  * **Fold by user decision:** `eymard-2008` (lipnikov-2014, no venue) was
    folded into `eymard-2010` (IMA J. Numer. Anal. 30:1009). The record goes
    from 3209 to 3208.
  * **DOI audit of all 87 Source pages** against Crossref, and DataCite for
    arXiv/Zenodo.
    * 72 are correct, 10 have no DOI by nature (books, theses, URLs, arXiv
      records), and 2 flags were wording differences (balsara-kim-2004,
      londrillo-delzanna-2004).
    * **Corrected, on both the Source page and the bibliography:**
      * [Kreeft & Gerritsma (2013)](/sources/kreeft-gerritsma-2013.md):
        `10.1016/j.jcp.2012.12.028` (an Innocenti et al. PIC paper) to
        `10.1016/j.jcp.2012.10.043`;
      * [Strand (1994)](/sources/strand-1994.md): `10.1006/jcph.1994.1023`
        (Andreassen et al.) to `10.1006/jcph.1994.1005`. This reverses an
        earlier bibliography note that had called kozdon-2021's printed
        `.1005` a typo. That note was wrong.
      * [Trask et al. (2020)](/sources/trask-2020.md):
        `10.1016/j.jcp.2020.109187` (does not resolve) to
        `10.1016/j.jcp.2019.109187`.
    * **Venue corrected:**
      [Wang, Nissen & Kreiss (2017)](/sources/wang-nissen-kreiss-2017.md) is
      published in Math. Comp. 87:2737-2763, doi:10.1090/mcom/3319. The
      earlier "SINUM 56(5):3016-3048" was unsupported by page 1.
    * **Published DOI added** to the venue of
      [Arnold, Falk & Winther (2009)](/sources/arnold-falk-winther-2009.md)
      (verified).
    * **Not renamed:** the archive files for Kreeft, Strand and Trask still
      embed the wrong DOIs. Renaming them awaits the user's authorization.
    * **Scope:** the audit covered Source-page identifiers only. The DOIs of
      the roughly 3,100 cited-only bibliography entries were not
      re-verified.

* **Ingested [Couch et al. (2021)](/sources/couch-2021.md)** (Flash-X Spark), a
  tier-C source added at the user's request.
  * **Corpus:** the PDF was moved to
    `~/papers/mosaic/div-free-amr/2021-ParCo-Couch-101016jparco2021102830.pdf`.
    `~/papers/re-download` is now empty.
  * **Divergence content is thin:** the paper names a "cell-centered
    approach" without specifying it, and none is inferred.
  * **Updated** [refluxing](/methods/refluxing.md): flux registers holding
    Runge–Kutta stage combinations. A compiler reading links this to the
    stage-coupling requirement for the invariant.
  * **Bibliography:** 22 references; the record goes from 3196 to 3209.
    * 10 existing entries gained the citer; 12 works are new, plus the self
      entry.
    * Titles were filled for `fryxell-2000` (FLASH), `lee-2013-b` (USM)
      and `grete-2009` (K-Athena).
    * `zhang-2019` gained its printed DOI.

* **Duplicate sweep and deep lint #8** after the 23 ingestions of this
  session (counter since #7 was past the every-10 cadence).
  * **`--dupes`** (`tools/bib_merge.py --dupes`): one identical-title+year
    group, `powell-1995` / `powell-1995-b`. It was reviewed earlier as two
    distinct works (book chapter versus AIAA conference paper) and is left
    alone.
  * **Supplementary sweeps.** Placeholder titles are invisible to
    `--dupes`, so two more sweeps were run: a journal-volume-page collision
    sweep and a fuzzy cross-year title sweep.
    * **Folded** four same-work pairs, each with a citedby union and a note:
      * `godunov-1972-b` into `godunov-1961` (Dokl. 139:521);
      * `yee-1969` into `yee-1966` (IEEE Trans. AP vol. 14);
      * `samarski-1983` into `samarskii-1982` (Diff. Eqns. 18:881, where
        1983 is the translation year);
      * `mirzaei-2011` into `mirzaei-2012` (online-first versus print).
    * **Flagged, not folded:** `eymard-2008` / `eymard-2010` (no venue on
      the 2008 entry).
    * **Kept distinct:** editions, parts I/II, and report-versus-journal
      forms, per earlier convention.
    * The record goes from 3200 to 3196.
  * **Parse repair:** `losasso-2004` had absorbed a page footer during the
    blomquist-2024 merge. Its booktitle was restored to
    "ACM SIGGRAPH 2004 Papers, pp. 457–462", and no other entry carries the
    footer.
  * **Notation drift.** These symbols were in use on concept pages but
    unregistered:
    * $\mathcal{E}^{\circ}$, $\mathcal{E}^{\alpha}$ and $\mathcal{E}^{c}$
      (CT pages, since the gardiner-stone-2005 ingestion), now in a new
      "Edge-EMF constructions" section;
    * Dedner's $\mathcal{D}$ (GLM and projection pages).

    Both are now in [notation](/notation.md). No paper-native symbols were
    found in the concept pages touched this session.
  * **Tag synonyms** introduced this session were normalized to the older
    vocabulary:
    * `code-comparison` to `comparison` (pakmor-2026, tomida-2026);
    * `relativistic-mhd` to `relativistic` (berta-2024, balsara-2026);
    * `helmholtz-hodge` to `hodge-decomposition` (ranocha-2020).
  * **Contradictions review.** The five `## Contradictions` sections were
    re-read.
    * The GLM entry's scoped reading gained the Tomida et al.
      commutativity precondition, noting that it does not explain the
      ADAM seam growth, which was observed at fixed $c_h$.
    * The positivity entries were already updated this session.
    * No other entry is stale.

* **Ingested [Stone et al. (2008)](/sources/stone-2008.md)** (Athena), a tier-C
  source added at the user's request.
  * **Corpus:** the PDF was moved to
    `~/papers/mosaic/div-free-amr/2008-ApJS-Stone-101086588755.pdf`.
  * **Scope:** the algorithm sections and the divergence-relevant tests
    were read in full. The steps that repeat GS05 and GS08 were read in
    outline, as recorded on the Source page.
  * **Updated** three pages:
    * [CT](/methods/constrained-transport.md);
    * [field loop](/benchmarks/field-loop-advection.md): aligned loops hold
      to round-off, inclined loops to truncation;
    * [positivity–divergence coupling](/results/positivity-divergence-coupling.md):
      the HLL-family statement, added to the scoped reading of the open
      entry.
  * **Bibliography:** 81 references; the record goes from 3177 to 3200.
    * The cited-only self entry gained its title.
    * 58 existing entries gained the citer; 23 works are new.
    * Eight mis-printed or forward citations carry notes, among them
      SG08 "in press", which maps to `stone-2009`, and Colella & Sekora
      "submitted", which maps to `colella-2008`.
    * The AIP proceedings paper Gardiner & Stone 2005b is keyed
      `gardiner-2005`. Its relation to the existing e-print
      `gardiner-2005-b` is unestablished, and it is left for the dupes
      sweep.

* **Ingested [Tomida et al. (2026)](/sources/tomida-2026.md)**, re-downloaded
  source 7 of 7. This completes the re-download batch.
  * **Corpus:** the arXiv v2 was moved to
    `~/papers/mosaic/div-free-amr/2026-ApJS-Tomida-1038471538-4365ae8785.pdf`.
    The published ApJS 285(2):64 version was found on Crossref, so this is
    a published work and not a preprint.
  * **Updated** four pages:
    * [GLM](/methods/glm-divergence-cleaning.md): the failure modes of the
      conventional implementation. A compiler reading notes that Pakmor
      et al. use the time-varying $c_h$ warned against here, but in the
      regime where both papers agree.
    * [exact discrete divergence](/properties/exact-discrete-divergence.md):
      the "no difference" result is scoped, not contradicted;
    * [positivity–divergence coupling](/results/positivity-divergence-coupling.md):
      CT's low-$\beta$ face-to-centre weakness;
    * [eight-wave](/methods/eight-wave.md).
  * **Bibliography:** 63 references; the record goes from 3141 to 3177.
    * The cited-only preprint entry `tomida-2026` (from pakmor-2026) was
      upgraded in place to the published article, keeping its eprint.
    * 27 existing entries gained the citer; 36 works are new.
    * The citation of Mocz, Vogelsberger & Hernquist (2014) is a different
      paper from the existing `mocz-2014`, so it is keyed `mocz-2014-b`.

* **Ingested [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md)**,
  re-downloaded source 6 of 7.
  * **Corpus:** the PDF was moved to
    `~/papers/mosaic/div-free-amr/2026-CAMC-Balsara-101007s42967-025-00517-y.pdf`.
    The slug follows the printed volume year (2026).
  * **Updated** two pages:
    * [UCT](/methods/upwind-constrained-transport.md): the
      finite-difference realization up to ninth order;
    * [positivity–divergence coupling](/results/positivity-divergence-coupling.md):
      the staggered positivity repair.
  * **New `Contradictions` entry, open**, on the positivity page: the
    paper calls the first-order HLL/LLF zone update positive (citing
    Gurski 2004), against Wu (2018) and Wu & Shu (2019). A scoped reading
    notes that the cited proof is 1D as far as the citing text shows, and
    that the scheme's energy repair makes its own guarantee independent of
    the claim.
  * **Bibliography:** 91 references; the record goes from 3109 to 3141.
    * 59 existing entries gained the citer; 32 works are new, plus the self
      entry.
    * Titles were filled for `donnert-2019`, `vanderholst-2008` and
      `komissarov-1999`.
    * **Duplicate fold:** `balsara-2009-b`, created at the christlieb-2016
      ingestion, is the published form of the existing `balsara-2008-a`.
      It was folded into that entry and its citers were merged.
    * A malformed printed DOI for Bhoriya et al. (2024) was not recorded.

* **Ingested [Blomquist et al. (2024)](/sources/blomquist-2024.md)**,
  re-downloaded source 5 of 7.
  * **Corpus:** the PDF was moved to
    `~/papers/mosaic/div-free-amr/2024-JCP-Blomquist-101016jjcp2023112695.pdf`.
  * **Updated** two pages:
    * [projection](/methods/projection-method.md): the iterated collocated
      projection, with a compiler reading on the compact-stencil variant of
      Balsara & Kim;
    * [AMR projection](/methods/amr-projection-method.md): the tree-based
      variant. A compiler reading links its hanging-node divergence rule
      to the bundle's seam-operator theme.
  * **Bibliography:** 74 references; the record goes from 3042 to 3109.
    * 8 existing entries gained the citer; 66 works are new, plus the self
      entry.
    * The `zhang-2019` (AMReX) placeholder title was filled.
    * Temam (1969) parts I and II are printed with identical pages, which
      is recorded in a note.

* **Ingested [Seo & Ryu (2023)](/sources/seo-2023.md)**, re-downloaded source
  4 of 7.
  * **Corpus:** the PDF was moved to
    `~/papers/mosaic/div-free-amr/2023-ApJ-Seo-1038471538-4357acdf4b.pdf`.
  * **Updated** three pages:
    * [constrained transport](/methods/constrained-transport.md): the
      high-order staggered FD CT. A compiler reading notes that its
      commuting one-axis differences imply an identity-level invariant,
      while the paper words it as "up to truncation error"; the text does
      not settle which.
    * [field loop](/benchmarks/field-loop-advection.md);
    * [exact discrete divergence](/properties/exact-discrete-divergence.md):
      turbulence spectra are independent of the CT order.
  * **Bibliography:** 71 references; the record goes from 3013 to 3042.
    * 43 existing entries gained the citer; 28 works are new, plus the self
      entry.
    * The CANS+ PASJ 2019 citation maps to `matsumoto-2016`, which already
      notes that publication.

* **Ingested [Balsara, Käppeli, Boscheri & Dumbser (2023)](/sources/balsara-2023.md)**,
  re-downloaded source 3 of 7.
  * **Corpus:** the PDF was moved to
    `~/papers/mosaic/div-free-amr/2023-CAMC-Balsara-101007s42967-021-00160-3.pdf`.
    The slug follows the printed volume year (2023), not the 2021 online
    date that Crossref reports.
  * **Updated** two pages:
    * [divergence-free reconstruction](/methods/divergence-free-reconstruction.md):
      a section on curl-constrained reconstruction, one degree down the
      complex;
    * [exactness theorems](/results/discrete-exactness-theorems.md):
      $C_h G_h = 0$ as a design principle.

    No page was created. The bundle's scope is divergence constraints,
    and the paper enters as the mirror construction.
  * **Bibliography:** 55 references; the record goes from 2987 to 3013.
    * 30 existing entries gained the citer; 25 works are new, plus the self
      entry.
    * `balsara-2017` (Part III) and `balsara-2014-b` gained notes on the
      printed volume and year.

* **Ingested [Christlieb, Feng, Seal & Tang (2016)](/sources/christlieb-2016.md)**,
  re-downloaded source 2 of 7.
  * **Corpus:** the PDF was moved to
    `~/papers/mosaic/div-free-amr/2016-JCP-Christlieb-101016jjcp201604016.pdf`.
  * **Updated** three pages:
    * [vector-potential evolution](/methods/vector-potential-evolution.md):
      the single-stage, single-step variant;
    * [positivity–divergence coupling](/results/positivity-divergence-coupling.md):
      the energy adjustment after the curl reset;
    * [exact discrete divergence](/properties/exact-discrete-divergence.md):
      the published AMR stage-coupling motive, linked to Zaghi's
      stage-refresh finding by a compiler reading.
  * **New `Contradictions` entry, closed** on the positivity page. The
    paper's limiter assumes Claim 1 (LF positivity for admissible data);
    [Wu (2018)](/sources/wu-2018.md), Theorem 4.1, refutes that conjecture
    explicitly. It is closed by explicit supersession. A compiler reading
    notes that the scheme's fourth-order curl does not meet the theorem's
    second-order divergence condition.
  * **Bibliography:** 63 references; the record goes from 2973 to 2987.
    * The cited-only self entry gained its DOI.
    * 49 existing entries gained the citer; 14 works are new.
    * The 1997 SHASTA reprint maps to `boris-1973`; the online-first
      Seal et al. maps to `seal-2016`; both carry notes.

* **Ingested [Jiang & Wu (1999)](/sources/jiang-1999.md)**, re-downloaded
  source 1 of 7.
  * **Corpus:** the re-downloaded PDF was moved from `~/papers/re-download/`
    to `~/papers/mosaic/div-free-amr/1999-JCP-Jiang-101006jcph19996207.pdf`.
  * **Updated** three pages:
    * [projection](/methods/projection-method.md): its high-order
      finite-difference use, which is necessary for stability there;
    * [eight-wave](/methods/eight-wave.md): the $8\times8$ eigensystem's
      normal-field dissipation, used without source terms (compiler
      reading);
    * [positivity–divergence coupling](/results/positivity-divergence-coupling.md):
      the early observation, with a compiler reading on why the theorem
      does not cover it.
  * **Bibliography:** 36 references; the record goes from 2962 to 2973.
    * The cited-only `jiang-1999` entry was upgraded in place with its
      DOI and pages.
    * 25 existing entries gained the citer; 11 works are new.
    * Titles were filled for `clarke-1986`, `harten-1987`, `liu-lax-1996`,
      `liu-1994`, `shu-1997` and `wu-1987`.
    * The printed AIAA 1995 Powell et al. paper (p. 661) was folded into
      `powell-1995-b`, with a note.

* **Ingested [Pakmor et al. (2026)](/sources/pakmor-2026.md)**, source 16 of 16.
  This completes the A + B ingestion list.
  * **Corpus:** the arXiv v1 preprint was moved to
    `~/papers/mosaic/div-free-amr/2026-arXiv-Pakmor-1048550arXiv260706660.pdf`.
    No journal version was found on Crossref. It is the corpus's first
    non-peer-reviewed paper, so each claim it adds to a concept page is
    marked "preprint"; no page status changed. The root index now counts
    it separately.
  * **Updated** four pages:
    * [GLM](/methods/glm-divergence-cleaning.md): cleaning as effective
      resistivity, with a compiler reading linking it to the
      solenoidal-data damping;
    * [eight-wave](/methods/eight-wave.md): measured low dissipation;
    * [vector-potential evolution](/methods/vector-potential-evolution.md):
      the Arepo-CT moving-mesh instability;
    * [exact discrete divergence](/properties/exact-discrete-divergence.md):
      a regime with no systematic class difference. A compiler reading
      scopes it against Olivares (2019) and Balsara & Kim (2004); no
      Contradictions entry is opened.
  * **Bibliography:** 48 references; the record goes from 2926 to 2962.
    * 13 existing entries gained the citer; 35 works are new, plus the self
      entry.
    * `teyssier-2006` ("in press") gained its published volume and page.
    * The DOI printed for `feldmann-2026` is malformed
      (`214394`); the hyphenated form was verified on Crossref and the
      title filled from there.

* **Ingested [Jones, McNally & Reynolds (2026)](/sources/jones-2026.md)**, source 15 of 16.
  * **Corpus:** the arXiv v1 preprint (which prints the JCP DOI) was moved to
    `~/papers/mosaic/div-free-amr/2026-JCP-Jones-101016jjcp2025114641.pdf`.
    Volume and article number were verified on Crossref.
  * **Created**
    [embedded-boundary CT](/methods/embedded-boundary-constrained-transport.md).
    It is a single-source page, earned as the paper's named contribution.
    It carries one compiler reading, which relates the edge-EMF mechanism
    to the [electric-field correction](/methods/electric-field-correction.md).
  * **Updated** three pages:
    * [constrained transport](/methods/constrained-transport.md):
      embedded boundaries;
    * [exact discrete divergence](/properties/exact-discrete-divergence.md):
      boundary ghost data need not be solenoidal, and one field per
      interface is required;
    * [positivity–divergence coupling](/results/positivity-divergence-coupling.md):
      the reported low-$\beta$ positivity limit.
  * **Bibliography:** 47 references; the record goes from 2886 to 2926.
    * 8 existing entries gained the citer; 39 works are new, plus the self
      entry.
    * The Clarke, Salas & Hassan AIAA paper is keyed `clarke-1986-b`, to
      keep it distinct from the existing `clarke-1986` (an ApJ Letters
      paper).
    * `toro-1997` gained its printed DOI.
    * The printed Osher, Fedkiw & Piechor (2004) DOI belongs to an Applied
      Mechanics Reviews item, which is recorded in a note.

* **Ingested [Berta et al. (2024)](/sources/berta-2024.md)**, source 14 of 16.
  * **Corpus:** the arXiv v4 preprint was moved to
    `~/papers/mosaic/div-free-amr/2024-JCP-Berta-101016jjcp2023112701.pdf`.
    The published JCP version was identified on Crossref.
  * **Updated** three pages:
    * [UCT](/methods/upwind-constrained-transport.md): a second fourth-order
      FV realization, with point-value reconstruction and the composition
      formula;
    * [positivity–divergence coupling](/results/positivity-divergence-coupling.md):
      the energy correction is still required at fourth order;
    * [field loop](/benchmarks/field-loop-advection.md).
  * **Bibliography:** 85 references; the record goes from 2871 to 2886.
    * 71 existing entries gained the citer; 14 works are new, plus the self
      entry.
    * Placeholder titles were filled for `falle-1998`, `meyer-2012` and
      `beckwith-2011`.
    * `matsumoto-2016` (CANS+, "submitted") gained a note on its PASJ 2019
      publication.
    * `jameson-1981` is printed with no authors; the authors were taken
      from Crossref via the printed DOI.

* **Ingested [Ding & Wu (2024)](/sources/ding-2024.md)**, source 13 of 16.
  * **Corpus:** the arXiv v1 preprint was moved to
    `~/papers/mosaic/div-free-amr/2024-SISC-Ding-10113723m1562081.pdf`.
    The published SISC version was identified on Crossref by title, and the
    slug follows the published year.
  * **Updated** two pages:
    * [positivity–divergence coupling](/results/positivity-divergence-coupling.md):
      the FV point-value version. A projection of the traces replaces the
      locally divergence-free DG basis. The page states that the
      condition is cell-local and enforced on the reconstruction, not an
      evolved invariant;
    * [divergence-free reconstruction](/methods/divergence-free-reconstruction.md):
      projecting point values instead of building polynomials, contrasted
      with Balsara's continuous construction.
  * **Scoped read:** the proof was read in outline only.
  * **Bibliography:** 59 references; the record goes from 2860 to 2871.
    * 49 existing entries gained the citer; 10 works are new, plus the self
      entry.
    * `fu-2018` gained its volume and pages.
    * `powell-1994` gained a note on its 1997 Springer reprint, which is the
      form cited here.

* **Ingested [Mignone & Del Zanna (2021)](/sources/mignone-2021.md)**, source
  12 of 16.
  * **Corpus:** the arXiv v2 preprint was moved to
    `~/papers/mosaic/div-free-amr/2021-JCP-Mignone-101016jjcp2020109748.pdf`;
    venue verified on Crossref.
  * **Updated** four pages:
    * [UCT](/methods/upwind-constrained-transport.md): the composition
      formula for Jacobian-free solvers, UCT-HLLD and UCT-GFORCE, and the
      measured ranking;
    * [flux-CT](/methods/flux-ct.md): the averaging-family comparison, and
      CT-Contact dissipation inherited from the base solver;
    * [field loop](/benchmarks/field-loop-advection.md): the rotated 3D
      loop, at truncation level and distinct from Felker & Stone's
      round-off geometry;
    * [positivity–divergence coupling](/results/positivity-divergence-coupling.md):
      exact $D_h^{\mathrm{f}}$ CT schemes still need an energy fix at
      $\beta \approx 2.5\cdot10^{-4}$.
  * **DOI correction (record error, fixed with visibility):**
    [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md) carried
    `doi:10.1016/j.jcp.2007.12.003` as its resource. That DOI is Artebrant
    & Torrilhon's (Crossref). The correct DOI, 10.1016/j.jcp.2007.12.017,
    is printed in this reference list and verified on Crossref.
    * The Source page and the bib entry were corrected.
    * The Layer-1 archive filename `2008-JCP-Gardiner-101016jjcp200712003.pdf`
      also embeds the wrong DOI. It was left unchanged and flagged to the
      human.
  * **Bibliography:** 62 references; the record goes from 2845 to 2860.
    * 48 existing entries gained the citer; 14 works are new, plus the self
      entry.
    * Placeholder titles were filled for `mignone-2006`, `mignone-2009`,
      `mignone-2012-c`, `porth-2019` and `suresh-1997`.
    * A second DOI swap was found and fixed: `balsara-1998` carried
      10.1086/313093, which is the TVD paper `balsara-1998-b`. Its own DOI
      is 10.1086/313092 (both verified on Crossref).

* **Ingested [Ranocha, Ostaszewski & Heinisch (2020)](/sources/ranocha-2020.md)**,
  source 11 of 16.
  * **Corpus:** the arXiv v2 preprint was moved to
    `~/papers/mosaic/div-free-amr/2020-CAMC-Ranocha-101007s42967-019-00057-2.pdf`;
    venue verified on Crossref.
  * **Registry:** $\mathsf{D}_1^*$, the SBP adjoint whose kernel holds the
    grid-oscillation mode, was added to [notation](/notation.md).
  * **Updated** six pages:
    * [exactness theorems](/results/discrete-exactness-theorems.md): a new
      section on the collocated SBP failure. The description now scopes the
      converses to staggered operators, and the index line follows;
    * [exact discrete divergence](/properties/exact-discrete-divergence.md);
    * [vector-potential evolution](/methods/vector-potential-evolution.md):
      the converse is a staggered-complex property;
    * [collocated seam source](/results/collocated-seam-divergence-source.md):
      the grid-oscillation modes are characterised, with a compiler
      reading marked as such;
    * [SBP](/definitions/summation-by-parts.md): nullspace consistency.
  * **Bibliography:** 60 references; the record goes from 2809 to 2845.
    * 24 existing entries gained the citer, and 36 works are new.
    * The cited-only `ranocha-2019` (cited by zaghi-2026 for Remark 2.8 and
      eq. 55, both matched in this paper) was folded into `ranocha-2020`.
    * The tech-report entries `linders-2017` and `mattsson-2013-b` gained
      notes recording their published versions, which are the ones cited
      here.

* **Ingested [Wu & Shu (2019)](/sources/wu-shu-2019.md)**, source 10 of 16.
  * **Corpus:** the arXiv v1 preprint was moved to
    `~/papers/mosaic/div-free-amr/2019-NumerMath-Wu-101007s00211-019-01042-w.pdf`;
    venue verified on Crossref.
  * **Updated**
    [positivity–divergence coupling](/results/positivity-divergence-coupling.md):
    * HLL fluxes on polytopal meshes;
    * the conservative scheme preserves its DDF condition only on
      Cartesian meshes with the global LF flux;
    * smooth solutions of the symmetrizable system are now a theorem
      (positive for any $\nabla\cdot B$); the conservative side is still
      evidence only;
    * the scope is rewritten, with a compiler reading, marked as such, that
      a 2:1 seam is formally a polytopal case and untested.
  * **Updated** [eight-wave](/methods/eight-wave.md): PDE-level positivity of
    the symmetrizable system.
  * **Scoped read:** proofs were read in outline only.
  * **Bibliography:** 66 references; the record goes from 2799 to 2809.
    * 57 existing entries gained the citer; 9 works are new, plus the self
      entry.
    * `dumbser-2014-a`, whose authors came from a garbled string, was renamed
      `balsara-2014-c`. Crossref confirms Balsara, Dumbser, Abgrall as the
      authors, and the DOI was added.

* **Ingested [Wu & Shu (2018)](/sources/wu-shu-2018.md)**, source 9 of 16.
  * **Corpus:** the arXiv v1 preprint was moved to
    `~/papers/mosaic/div-free-amr/2018-SISC-Wu-10113718m1168042.pdf`. The
    published title differs from the preprint's ("A provably positive …
    method"); verified on Crossref.
  * **Updated** two pages:
    * [positivity–divergence coupling](/results/positivity-divergence-coupling.md):
      it is now scoped to conservative schemes, and has a section on the
      non-conservative escape. The symmetrizable form with penalty terms is
      provably positive without a DDF condition, at the cost of exact
      conservation;
    * [eight-wave](/methods/eight-wave.md): positivity as a second argument
      for the source term. It is weighed against Tóth's wrong-jump result,
      not offered as closing it.
  * **Scoped read:** proofs were read in outline only, and the Source page
    says so.
  * **Bibliography:** 58 references; the record goes from 2793 to 2799.
    * 51 existing entries gained the citer, and 7 works are new.
    * `wu-shu-2018` was upgraded to its published metadata.
    * The duplicate `godunov-1972-a` was folded into `godunov-1972` (same
      title, year and start page; the printed volume differs, and a note
      records it).
    * `powell-1995-b` (AIAA 12th CFD conference) is kept distinct from
      `powell-1995` (a book chapter with the same title).

* **Ingested [Wu (2018)](/sources/wu-2018.md)**, source 8 of 16.
  * **Corpus:** the arXiv v2 preprint was moved to
    `~/papers/mosaic/div-free-amr/2018-SINUM-Wu-10113718m1168017.pdf`;
    venue verified on Crossref.
  * **Created**
    [positivity–divergence coupling](/results/positivity-divergence-coupling.md),
    a Result with status established. For LF-type schemes in 2D and 3D,
    provable positivity needs a discrete divergence-free condition on the
    scheme's own stencil, and the first-order LF scheme preserves
    $D_h^{\mathrm{c}}\bar B_h = 0$ exactly.
  * **Registry:** $\mathcal{G}$ (admissible set) and $\alpha^{\mathrm{LF}}$
    were added to [notation](/notation.md).
  * **Updated**
    [exact discrete divergence](/properties/exact-discrete-divergence.md)
    (positivity as a second reason the constraint matters) and
    [GLM](/methods/glm-divergence-cleaning.md) (no guarantee in the
    controlled class). A compiler reading, marked as such, links this to the
    low-$\beta$ GLM failure in the Zaghi (2026) record without claiming it
    as the cause.
  * **Scoped read:** proofs were read in outline only, and the Source page
    says so.
  * **Bibliography:** 54 references; the record goes from 2769 to 2793.
    * 30 existing entries gained the citer, and 24 works are new.
    * `wu-2018` (cited by zaghi-2026) was upgraded in place.
    * `wu-shu-2018` gained the printed title. It is source 10 of this batch.
    * The venue-less `zhang-shu-2010` was **not** folded into either new
      JCP 229 Zhang–Shu entry. Identity is unverified, and a note records
      this.

* **Ingested [Felker & Stone (2018)](/sources/felker-2018.md)**, source 7
  of 16.
  * **Corpus:** the arXiv v2 preprint was moved to
    `~/papers/mosaic/div-free-amr/2018-JCP-Felker-101016jjcp201808025.pdf`.
    The DOI was found by a Crossref title search, which also verified
    volume and pages.
  * **Updated** three pages:
    * [UCT](/methods/upwind-constrained-transport.md): the fourth-order FV
      realization, and the Appendix-A relation to $\mathcal{E}^c$. The
      limiting-case agreement at second order complements GS05's
      first-order identity with $\mathcal{E}^\circ$. It is scoped, not a
      contradiction;
    * [flux-CT](/methods/flux-ct.md): the structural second-order ceiling
      of $\mathcal{E}^c$;
    * [field loop](/benchmarks/field-loop-advection.md): the 3D
      fourth-order run with $B_z$ below machine epsilon.
  * **Bibliography:** 64 references; the record goes from 2753 to 2769.
    * 48 existing entries gained the citer, and 16 works are new.
    * The pre-existing cited-only `felker-2018` (cited by stone-2020) was
      upgraded in place.
    * Placeholder titles were filled for 13 existing entries, including
      `mccorquodale-colella-2011`, `stone-2009`, `delzanna-2007` and
      `miyoshi-2005`. DOIs printed in this list were added where entries
      lacked them.

* **Ingested [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md)**,
  source 6 of 16.
  * **Corpus:** the arXiv v2 preprint was moved to
    `~/papers/mosaic/div-free-amr/2014-JCP-Christlieb-101016jjcp201403001.pdf`;
    volume and pages were verified on Crossref.
  * **Updated** five pages:
    * [exact discrete divergence](/properties/exact-discrete-divergence.md):
      the collocated $D_h^{\mathrm{c}} C_h^{\mathrm{c}} = 0$ identity, until
      now supported only by the hypothesis-grade Zaghi (2026) record, gains
      a published fourth-order source on uniform grids. The seam claim stays
      hypothesis;
    * [vector-potential evolution](/methods/vector-potential-evolution.md):
      the collocated high-order realization (Weyl gauge, weak hyperbolicity,
      WENO-HJ limiting of the field, artificial resistivity), plus a
      compiler reading, marked as such, on the untested AMR gauge
      behavior;
    * [constrained transport](/methods/constrained-transport.md): the
      unstaggered potential-based line;
    * [rotated shock tube](/benchmarks/rotated-shock-tube.md): base scheme
      against CT;
    * [collocated seam source](/results/collocated-seam-divergence-source.md):
      no published exact collocated scheme has been run across a 2:1 seam.
  * **Bibliography:** 47 references; the record goes from 2734 to 2753.
    * 29 existing entries gained the citer; 18 works are new, plus the self
      entry.
    * `gottlieb-2009` was upgraded with the title and venue printed here.
    * Misprinted venues were checked on Crossref and recorded in notes:
      Helzel et al. 2011 (printed 227:9527, actually 230:3803), Cheng et
      al. 2013 (no volume printed) and Seal et al. ("to appear").
    * The MHDCLAW software page has no printed year. It is keyed
      `rossmanith-2014` by its citation date, and the note says so.

* **Ingested [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md)**,
  source 5 of 16.
  * **Corpus:** the arXiv v2 preprint was moved to
    `~/papers/mosaic/div-free-amr/2010-JCP-Mignone-101016jjcp201004013.pdf`;
    volume, issue and pages were verified on Crossref.
  * **Updated** four pages:
    * [GLM](/methods/glm-divergence-cleaning.md): a high-order
      finite-difference section. It covers the separate upwinding of the
      $(B_n, \psi_h)$ pair, which is the construction behind the Zaghi (2026)
      solenoidal-damping observation; the scheme-dependent divergence
      monitor; and the order-dependent optimum of $\alpha_p$;
    * [divergence-free reconstruction](/methods/divergence-free-reconstruction.md):
      the controlled-class alternative;
    * [rotated shock tube](/benchmarks/rotated-shock-tube.md) and
      [field-loop advection](/benchmarks/field-loop-advection.md): the
      high-order cleaning runs in 2D and 3D.
  * Record inconsistencies are noted on the Source page: CTU-GLM is cited
    as "ApJS 229", and Colella–Sekora as volume "277".
  * **Bibliography:** 54 references; the record goes from 2729 to 2734.
    * 47 existing entries gained the citer, and 7 works are new.
    * The pre-existing cited-only `mignone-2010-c` (3 citers) is this work.
      It was renamed to the slug and upgraded to verified metadata.
    * Two duplicates surfaced and were folded:
      * `dumbser-2008` into `dumbser-2008-b` (same JCP 227:8209);
      * `woodward-1998` into `dai-woodward-1998` (same JCP 142:331,
        authors reversed by powell-1999).
    * DOIs were added from Crossref to `artebrant-2008` (printed
      "Arterant") and to `balsara-2008-a` (now published, JCP 228:2480).

* **Ingested [Balsara (2009)](/sources/balsara-2009.md)**, source 4 of 16.
  * **Corpus:** the author preprint was moved to
    `~/papers/mosaic/div-free-amr/2009-JCP-Balsara-101016jjcp200903038.pdf`;
    venue and pages were verified on Crossref.
  * **Updated** two pages:
    * [divergence-free reconstruction](/methods/divergence-free-reconstruction.md):
      third and fourth order in a Legendre-moment basis; the face moments
      fix the interior; energy minimization closes the free constraints;
      compared with UCT's point-value invariant;
    * [$P_D$](/operators/divergence-free-prolongation.md): refinement ratio
      3 and recursive 2·3 ratios, claimed but not demonstrated.
  * A record inconsistency is noted on the Source page: the tables label
    the runs "ADER" while the text describes RK-WENO.
  * **Bibliography:** 35 references (two are numbered [26]); the record
    goes from 2725 to 2729.
    * 31 existing entries gained the citer, and 4 works are new, including
      the "submitted" Balsara–Rumpf–Dumbser–Munz ADER-WENO paper as
      `balsara-2008-a`.
    * The pre-existing cited-only `balsara-2009` (3 citers) is this work;
      it was upgraded in place to verified metadata.

* **Ingested [Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md)**,
  source 3 of 16.
  * **Corpus:** the arXiv preprint was moved to
    `~/papers/mosaic/div-free-amr/2005-JCP-Gardiner-101016jjcp200411016.pdf`;
    venue and pages were verified on Crossref.
  * **Updated** four pages:
    * [flux-CT](/methods/flux-ct.md): the FV–CT consistency relations; the
      proof that the arithmetic EMF average halves numerical viscosity on
      grid-aligned flow; the $\mathcal{E}^\alpha/\mathcal{E}^\circ/\mathcal{E}^c$
      family;
    * [UCT](/methods/upwind-constrained-transport.md): at first order the
      UCT EMF equals $\mathcal{E}^\circ$, the oscillatory member;
    * [rotated shock tube](/benchmarks/rotated-shock-tube.md): the
      macro-cell diagnostic;
    * [field-loop advection](/benchmarks/field-loop-advection.md): the 2D
      origin of the test.
  * **Bibliography:** 33 references; the record goes from 2720 to 2725.
    * 28 existing entries gained the citer, and 5 works are new.
    * The pre-existing cited-only `gardiner-2005-a` (8 citers) is this work;
      it was folded into the ingested key `gardiner-stone-2005`.
      `gardiner-2005-b`, a separate 2005 e-print cited by Fromang, is left
      as is.
    * Crockett et al. "in press" was mapped onto `crockett-2005`, and the
      Evans–Hawley "ApJ 322" typo onto 332.

* **Ingested [Balsara & Kim (2004)](/sources/balsara-kim-2004.md)**, source 2
  of 16.
  * **Corpus:** the arXiv preprint was moved to
    `~/papers/mosaic/div-free-amr/2004-ApJ-Balsara-101086381051.pdf`.
    Venue, pages and published title were verified on Crossref; the
    published title differs from the preprint's.
  * **Updated** three pages:
    * [projection](/methods/projection-method.md): the three variants (the
      wide-stencil SDC1 is Chorin's $D_h^{\mathrm{c}} G_h$), the
      non-locality failure mode, and a new `## Contradictions` against
      Tóth's top ranking. It is scoped to problems with persistent,
      re-created divergence and left open.
    * [exact discrete divergence](/properties/exact-discrete-divergence.md):
      exactness is not adequacy without locality.
    * [staggered grid](/definitions/staggered-grid.md): a compiler note
      that this comparison tests constraint mechanism, not placement, since
      the "staggered" scheme is flux-CT, which Tóth proved collocated-equivalent.
  * No new page: the supernova-turbulence test has a single source and is
    under-specified (heating and cooling are delegated to other papers), so
    it stays inline.
  * **Bibliography:** 33 references; the record goes from 2715 to 2720.
    * 27 existing entries gained the citer, and 6 works are new.
    * The pre-existing cited-only `balsara-kim-2004` was upgraded in place
      to verified metadata, keeping its 4 citers.
    * Balsara 2003 "submitted" was mapped onto `balsara-2004`, the published
      form.
    * Printed typos were kept off the merge: Brackbill–Barnes "35, 462"
      maps onto 35:426, and Evans–Hawley "1989" onto 1988.
    * **A pre-existing duplicate was found and folded:** `dai-1994` and
      `dai-woodward-1994` are both Dai & Woodward JCP 111:354. They now sit
      under `dai-woodward-1994`, with citers balsara-2001 and toth-2000
      added. The title+year sweep missed it because one entry is title-less.

* **Ingested [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md)**,
  source 1 of 16 in the ADAM-bibliography div-free batch. The batch covers
  tiers A and B of the reviewed `~/papers/adam` list, real PDFs only.
  * **Corpus:** the PDF was moved, as the human asked, from `~/papers/adam`
    to `~/papers/mosaic/div-free-amr/2004-JCP-Londrillo-101016jjcp200309016.pdf`.
    The worklist now counts 62.
  * **Created** two pages:
    * [Upwind constrained transport](/methods/upwind-constrained-transport.md):
      the paper's named contribution; Mignone & Del Zanna (2021), later in
      the batch, merges here.
    * [Rotated shock tube](/benchmarks/rotated-shock-tube.md): it now meets
      the ≥2-sources rule (Tóth 2000, this paper, the ADAM record).
  * **Updated** six pages:
    * [flux-CT](/methods/flux-ct.md): the monopole objection to feeding
      cell-centered averages into fluxes, reconciled with Tóth's
      equivalence as two different stencils;
    * [CT](/methods/constrained-transport.md): the point-value high-order
      form;
    * [divergence-free reconstruction](/methods/divergence-free-reconstruction.md);
    * [exact discrete divergence](/properties/exact-discrete-divergence.md):
      the same field on two stencils, and time splitting;
    * [conservation–orthogonality](/results/conservation-orthogonality-incompatibility.md):
      the truncation-order loophole, with two compiler cautions on its
      discontinuity remainder;
    * [staggered grid](/definitions/staggered-grid.md): further support for
      the Londrillo–Del Zanna side of the `Contradictions`; still open.
  * **Bibliography:** all 35 references were merged; the record grows from
    2707 to 2715.
    * 27 existing entries gained the citer; 8 works are new.
    * The pre-existing cited-only key `londrillo-2004` is the same work. It
      was folded into the ingested key `londrillo-delzanna-2004`, and its 4
      citers carried over.
    * `toth-2002` (JCP 182:346, Lorentz-force discretization) is new and
      carries a note: it is a different work from `toth-roe-2002`, which an
      earlier backfill resolution had aliased to first-author "toth-2002"
      citations.
    * Two printed venue typos were mapped onto existing entries: Komissarov
      "343 (1999) 366" (which reads as pages 343–366 of MNRAS 303) and
      Del Zanna et al. "A&A 307" (vol. 367).

* **Ingested [Zaghi (2026)](/sources/zaghi-2026.md), the ADAM verification
  record.** It is the first non-corpus source and the first `source_kind: code`.
  * **Capture (Layer 1, frozen):** `raw/docs/zaghi-2026/` holds 8 doc
    snapshots at commit `d99e61f0`, the divb-peak oracle, issue threads #21,
    #29, #30 and #31 (full, with comments) and 6 FLUME div(B) run histories.
    Only the snapshots are read, so the bundle has no live dependency on the
    code repository (D12). #13 was fetched and then dropped unread, so it is
    not claimed as read.
  * **Status:** every claim compiled from this source is `hypothesis` (D3:
    the human's own record).
  * **Created** three pages:
    * [Divergence source at collocated 2:1 seams](/results/collocated-seam-divergence-source.md)
    * [Restriction-compatibility bound for point-value prolongation](/results/point-value-restriction-compatibility.md)
    * [ADAM](/software/adam.md), the first Software page
  * **Updated** seven pages:
    * [transfer locality limits](/results/transfer-operator-locality-limits.md):
      evidence on the cell-collocated row;
    * [SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md):
      a partial answer to its open structural question;
    * [GLM](/methods/glm-divergence-cleaning.md): a new `## Contradictions`
      on boundedness under a growing seam source, scoped and left open; the
      accuracy cost on solenoidal data; EGLM evidence;
    * [exact discrete divergence](/properties/exact-discrete-divergence.md):
      collocated exactness as a uniform-grid property; time coupling as part
      of the claim;
    * [refluxing](/methods/refluxing.md);
    * [field-loop advection](/benchmarks/field-loop-advection.md);
    * [staggered grid](/definitions/staggered-grid.md): a further
      development of its `Contradictions`.
  * **Registry extension** ([notation](/notation.md)): $C_h^{\mathrm{c}}$ (the
    collocated curl), $R P = I$ round-trip compatibility, and a new
    "Cleaning and verification quantities" table ($c_h$ and $c_p$, already in
    use on the GLM page but unregistered until now, plus $q$ and
    $p_{\mathrm{obs}}$).
  * **Bibliography:** the reference list was merged with a recorded scope:
    the References sections of FLUME `numerics.md` and `models.md`, inline
    author-year citations in the captured docs, and every citation in the
    four issue threads.
    * 26 existing entries gained `zaghi-2026` in `citedby`.
    * 17 new entries, plus the source's own entry: 2689 → 2707.
    * Metadata is as printed. Author initials not printed by the citing text
      were deliberately left out.
    * Four citations with no year or title stay unresolved, listed on the
      Source page: Mishra–Svärd, Cheng, the Guzik dissertation, Wang 2018.
  * **Compiler analysis recorded separately from the source's claims:**
    * the FLUME/PRISM "bounded vs unbounded" seam verdicts are explained by
      constraint class, not by a contradiction;
    * the FLUME divb-peak seam oracle has no boundedness assertion;
    * the field-loop seam peak occurs at the seam crossing, not at the first
      step.
  * **Corrections caught during compilation:** an EGLM robustness claim was
    narrowed (the benefit is not isolated from the HLLD base scheme). An
    earlier verbal claim that the "+2" convergence figure was only a
    prediction was withdrawn: it is measured on step-1 ladders.
  * Deep-lint counter: 1 ingestion since deep lint #7.

## 2026-07-22

* **Deep lint #7 / closing audit — bibliography citation graph.** First audit
  of the completed 2700-entry citation record (D15 backfill). **Structural
  checks (deterministic):** 0 dangling `citedby` slugs, 0 self-citations,
  61/61 ingested slugs present as entries, every source's reference list
  non-empty; the 16 `citedby=0` entries are all recent/peripheral ingested
  sources nothing else cites (correct). **Duplicate sweep found 9 same-work
  entries under distinct keys that per-batch dedup missed** — all merged
  (2700 → 2691): two placeholder-title duplicates a batch-6 silence wrongly
  admitted (`stone-1992-c` = `stone-1992` ZEUS-2D II, both ApJS 80:791;
  `harten-1978-b` = `harten-1978`, shashkov's "part II" label but identical
  Math. Comp. 32:363-389); and seven cross-source surname-spelling variants
  the stem-year grouping couldn't catch (`chiuekwanyu`→`chiu`, `detain`→
  `demin`, `casilov`→`gasilov`, `ganhga`→`solovov`, `tishkin`→`favorskii`
  author-order, `schewchuck`→`shewchuck`, and `hu-1999-a`→`jiang-1999` — a
  wrong-author transcription in zampa's list, same JCP 150:561 Jiang–Wu
  WENO-MHD paper). **LLM edge verification:** five agents re-read the PDFs
  of the six sources contributing the most disambiguation keys (zampa,
  lipnikov, delreyfernandez, olivares, stone, shashkov) and checked 194
  disambiguated `citedby` edges against the printed reference lists —
  **193 confirmed correct, 1 misattribution found and fixed**
  (olivares-2019's Hawley–Smarr–Wilson edge pointed at `hawley-1984-b`
  [ApJS 55:211] but olivares prints ApJ 277:296, a page variant of HSWa
  [`hawley-1984-a`]; edge moved). One metadata inconsistency corrected
  (`svard-2008-b` venue: the mattsson-carpenter-2010 misprint "JCP 225"
  fixed to the real JCP 227:4805-4824, confirmed by delreyfernandez-2014).
  Benign preprint-vs-published year labels (kreeft-gerritsma-2013 cited as
  2012 arXiv, arnold-falk-winther-2009 as 2010 Bull. AMS) left as-is with
  their existing notes; the two key-stem/year-field mismatches
  (almquist-2018 slug, balsara-2014-b Part-II series sibling) are
  intentional. Final state: **2691 entries, 3889 citation edges**, graph
  invariant-clean.

* **Backfill merger promoted to `tools/bib_merge.py` (D16).** The throwaway
  batch harness was generalized into a documented, bundle-agnostic tool
  (CLI-parameterized master/frags/resolutions; refuses `--write` while flags
  are open) and its whole-corpus duplicate sweep made a first-class `--dupes`
  subcommand. Regression-tested: it reproduces the batch-6 merge exactly
  (FLAGS: 0, same entry count). Running `--dupes` on the audited master
  immediately found **2 more cross-spelling duplicates the hand sweep missed**
  (`bossavit-1991c`→`bossavit-1991-a`, same Eur. J. Mech. B/Fluids 10(5):474;
  `nordstrom-2015`→`lundquist-2015`, same LiTH report, author order swapped) —
  merged (2691 → **2689 entries**); the sweep is now clean at 0 groups.

## 2026-07-21

* **Bibliography backfill batch 6 — FINAL; citation record complete
  (61/61 reference lists merged).** Reference lists of the last 11 sources
  merged (almquist-2018, bossavit-1998, crane-2025, degoes-2020,
  kozdon-2021, lundquist-2018, olivares-2019, shashkov-1996, stone-2020,
  wang-petersson-2019, zampa-2024): 1195 printed references,
  [bibliography](/bibliography.md) grows 1804 → 2700 entries. **All 61
  ingested sources' reference lists are now merged; the `--pending`
  worklist is empty and the sync linter is warning-free.** The three
  scoped-read sources contributed their consolidated bibliographies whole,
  scope recorded on each fragment: crane-2025 (single p.163 list, 17 refs),
  shashkov-1996 (end-of-book Bibliography pp.341-354, 154 refs), and
  bossavit-1998 — which has **no single bibliography**: references are 12
  per-chapter lists, extracted and deduplicated to 273 distinct works
  (28 cross-chapter duplicates collapsed). zampa-2024's thesis bibliography
  (346 works) is the largest single list in the corpus. Identity
  resolutions closed the graph on itself: the SBP cluster's four papers
  cite each other and the earlier SBP corpus almost entirely into existing
  keys (almquist: 15 of 29 refs already present), with published-form
  merges onto ingested slugs (almquist-2019 → the ingested almquist-2018
  SISC form; wang-2018 "2D wave" → wang-nissen-kreiss-2017's Math. Comp.
  publication; friedrich-2017 → friedrich-2016; svard-2014 → svard-2013-a).
  Same-key different-work collisions split by second-author or letter key
  (berg-2012-b, nordstrom-2003-b, liu-2008-b, zhang-2006-b, mignone-2005-b,
  jiang-2012-b, several Bossavit-book works at -g/-b, balsara-1999-d for
  the pressure-positivity paper). **Data correction**: kozdon-2021 prints
  Strand 1994's DOI suffix as .1994.1005 — a citing-list typo; the
  authoritative .1994.1023 (from the ingested Source page) was kept, the
  typo recorded in a note. The venue-number cross-check again earned its
  keep, catching placeholder-title collisions the title check is blind to
  (harten-lax vs harten, jiang Y.-F. vs R.-L., the six EHT companion
  papers). Twenty-plus references excluded as un-citable across the batch
  (no printed year: two Dumbser/Hu thesis-list items, code-website URLs,
  in-press entries without year). **Final frontier**: balsara-1999 leads
  at 17 of 61 processed sources, brackbill-1980 (16), then kreiss-1974 and
  whitney-1957 (13), brio-1988 / carpenter-gottlieb-1994 / nedelec-1980
  (11), raviart-1977 / ryu-1998 (10) — the ranking spans the full corpus:
  MHD divergence control (Balsara, Brackbill, Brio), SBP (Kreiss,
  Carpenter), and FEEC/mimetic (Whitney, Nédélec, Raviart) all in the top
  tier. These heavily-cited non-ingested works are the derived ingestion
  frontier if the corpus is ever extended.

* **Bibliography backfill batch 5** — reference lists of 10 sources merged
  (bonelle-ern-2014, lipnikov-2014, nissen-2014, palha-2014, etienne-2015,
  kozdon-wilcox-2015, wang-kreiss-2017, wang-nissen-kreiss-2017, derigs-2018,
  friedrich-2018): 621 printed references, [bibliography](/bibliography.md)
  grows 1504 → 1804 entries (50/61 lists merged). Lipnikov–Manzini–Shashkov's
  mimetic review contributed a complete 276-item list (one verbatim in-list
  duplicate collapsed). The citation graph is closing on itself: the SBP
  cluster's lists land mostly on existing keys (kozdon-wilcox-2015: 16 of 19
  refs already present), and five sources cite other ingested sources in
  preprint/published year-variants, all merged with notes
  (kreeft-gerritsma-2013 cited as arXiv 2012 by lipnikov-2014 and palha-2014;
  kozdon-wilcox-2015 cited as SISC 2016; nissen-2014 as JSC 2015;
  wang-kreiss-2017 cited by its twin; shashkov-1996 under a short book
  title). Identity resolutions: a batch-3 informational silence
  (bossavit-1998 short-title variant) was found masking a genuinely
  different work — bonelle-ern-2014 and palha-2014 cite the four-part JSAEM
  "On the geometry of electromagnetism" series collectively under the
  book's key; the silence is removed, the collective citation now lives at
  bossavit-1998-f, and the five-part "Computational electromagnetism and
  geometry" series is reconciled across three citing sources
  (bossavit-2000 collective + bossavit-1999-c part 2). Same-title
  same-year pairs from three sources' own lists trusted as distinct
  (gyrya-2012 square/rectangular, lipnikov-2011 monotonicity pair,
  aavatsmark-1998 I/II). Notable merges: lipnikov's Castillo-first
  "High-order mimetic FDM on nonuniform grids" identified as hyman-1995
  (ICOSAHOM 95 = Houston J. Math. special issue); Svärd–Nordström SBP
  review (svard-2013-a) united with its JCP 268 published form;
  duez-2005/shibata-2006 GRMHD placeholder pairs disambiguated by venue
  against etienne-2015's titled citations (20 placeholder titles upgraded,
  the largest single-source enrichment so far); Derigs' DOI-rich list
  filled 20 missing identifiers. Nine references excluded as un-citable
  (no printed year): five in derigs-2018 (incl. an arXiv-only lecture-notes
  set and a DOI-only in-press item), the Kranc code URL, plus the two
  "submitted" Kreeft preprints now entering via palha-2014's dated
  citations. **Frontier update**: brackbill-1980 (16 of 50), balsara-1999
  (15), whitney-1957 (12), brio-1988 and ryu-1998 (10), kreiss-1974 and
  nedelec-1980 and zachary-1994 (9) — Kreiss–Scherer 1974 (SBP origin)
  enters the top tier.

* **Bibliography backfill batch 4** — reference lists of 10 sources merged
  (etienne-2010, mignone-tzeferacos-2010, perot-2011, miniati-martin-2011,
  christiansen-2011, mignone-2012, etienne-2012, teixeira-2013,
  kreeft-gerritsma-2013, delreyfernandez-2014): 859 printed references,
  [bibliography](/bibliography.md) grows 907 → 1504 entries (40/61 lists
  merged). Christiansen's Acta Numerica review (145 refs) and Teixeira's
  CEM review (162 printed, 2 in-list duplicates collapsed) contributed
  complete consolidated lists. **New safeguard**: a venue-number cross-check
  now guards placeholder-title merges — it caught six same-key different-work
  collisions the title check cannot see (Harten–Lax–van Leer SIAM Rev. 25 vs
  Harten JCP 49; Jiang–Shu WENO vs Jiang–Wu–Povinelli; two De Villiers–Hawley
  2003, two J.D. Brown 2009, two Tadmor 1984, two De Rango–Zingg 2001).
  Identity resolutions: two sources cite a **different work carrying the
  citing source's own slug key** (Christiansen & Scheid 2011 →
  christiansen-scheid-2011; Del Rey Fernández, Boom & Zingg JCP 266 →
  delreyfernandez-boom-2014); first-author citations of ingested sources
  mapped to slugs (harlow-welch, evans-hawley, berger-colella, toth-roe,
  gardiner-stone, mignone-tzeferacos, mattsson-carpenter, balsara-2004,
  arnold-falk-winther-2009 cited as its 2010 Bull. AMS form,
  desbrun-kanso-tong-2008 cited as its 2005 SIGGRAPH course-notes form);
  letter-swap untangled vs master for mattsson-2008-a/-b; year-variant
  merges with notes (svard-2007→svard-2008-a, yee-2000→yee-1999-b,
  mattsson-2007→mattsson-2006-b, flanders-1989→flanders-1990,
  deschamps-1982→deschamps-1981, subramanian-2007→subramanian-2006,
  berger-1991 report/IEEE-journal forms). **Pre-batch repair**: master
  desbrun-2003 ("Discrete exterior calculus (in preparation)", cited by
  hirani-2003) merged into desbrun-hirani-2005 as its early form — freeing
  the key for Teixeira's distinct CDC-2003 DEC paper. Volume misprints
  recorded in notes (mattsson-carpenter-2010 prints JCP 225 + wrong third
  author for the no-slip Svärd–Nordström paper; JCP 111:354 venue belongs
  to dai-woodward-1994). Nine references excluded as un-citable (no printed
  year): Cactus/HARM code URLs, a private communication, two Lorenz-gauge
  editorial footnotes in etienne-2012, two "submitted" Kreeft preprints, an
  ICCFD7 paper, one duplicate-only). Seven placeholder titles upgraded;
  three arXiv ids filled. **Frontier update**: brackbill-1980 (15 of 40),
  balsara-1999 (13), ryu-1998 and whitney-1957 (10 each), brio-1988 (9),
  nedelec-1980, powell-1994, zachary-1994 (8 each) — the FEEC/DEC/mimetic
  cluster (whitney, nedelec) now rivals the MHD core.

* **Bibliography backfill batch 3** — reference lists of 10 sources merged
  (mattsson-nordstrom-2004, brezzi-lipnikov-shashkov-2005, desbrun-hirani-2005,
  li-shu-2005, arnold-falk-winther-2006, fromang-2006, desbrun-kanso-tong-2008,
  gardiner-stone-2008, arnold-falk-winther-2009, mattsson-carpenter-2010):
  464 printed references, [bibliography](/bibliography.md) grows 662 → 907
  entries (30/61 lists merged). The two FEEC reviews contributed complete
  consolidated lists (100 + 90 refs) per the complete-and-unfiltered rule.
  Identity resolutions, all recorded in entry notes where they carry
  information: preprint/submitted forms merged into published entries
  (arnold-2005→arnold-2007, christiansen-2005→christiansen-2007,
  boffi-2002→boffi-2001 [M2AN publication of the "submitted" form],
  monk-2003-b→monk-2001, desbrun-2003→desbrun-2004 [Discrete Poincaré lemma],
  Bossavit's Extrusion/contraction preprint→bossavit-2003 [COMPEL]);
  first-author-only citations of ingested sources mapped to their slugs
  (evans-1988, londrillo-2000, berger-1989, toth-2002, brezzi-2005,
  desbrun-2005, mattsson-2004, hyman-1997, arnold-2006-c = the ingested
  Acta Numerica review); the two Mattsson fragments assigned opposite
  -a/-b letters to Gustafsson 1995 (GKO book vs Gustafsson–Olsson JCP 117) —
  untangled, book kept at gustafsson-1996 with year-variant note; colliding
  distinct works split per house convention (second-author key when
  authorship differs: bochev-gunzburger-2005, marsden-pekarsky-1999,
  marsden-west-2001, dodziuk-patodi-1976, mattsson-nordstrom-2003; letter
  suffix otherwise: boffi-2001-b, monk-1992-b, hiptmair-2001-c). Six
  placeholder titles upgraded from titled citations; eprint filled for
  desbrun-hirani-2005. **Pre-batch defect repaired**: duplicate dodziuk-1973
  (year misprint in hyman-shashkov-1997's list; Amer. J. Math. 98 appeared
  1976) merged into dodziuk-1976. Nine references excluded as un-citable
  (no printed year): seven software-website citations in
  arnold-falk-winther-2009, Qiu & Shu "to appear" in li-shu-2005,
  mattsson-carpenter-2010's own URL-only arXiv preprint. **Frontier update**:
  brackbill-1980 leads at 11 of 30 processed sources, then balsara-1999 (9),
  ryu-1998 (8), brio-1988 and powell-1994 and stone-1992 (7 each) —
  whitney-1957 (6) is the first non-MHD entry, pushed up by the FEEC/DEC
  cluster.

## 2026-07-10

* **Bibliography backfill batch 2** — reference lists of 10 sources merged
  (powell-1999, londrillo-delzanna-2000, toth-2000, balsara-2001,
  clemens-weiland-2001, dedner-2002, hiptmair-2002, toth-roe-2002,
  hirani-2003, balsara-2004): 541 printed references,
  [bibliography](/bibliography.md) grows 299 → 662 entries (20/61 lists
  merged). Hiptmair's scoped-read Acta Numerica review contributed its full
  consolidated list (161 refs) per the complete-and-unfiltered rule. Identity
  resolutions, all recorded in entry notes: Berger–Oliger and Evans–Hawley
  cited with year 1989 by balsara-2001 (merged into berger-1984 /
  evans-hawley-1988); Colella JCP 87:171 cited under two different titles;
  Ryu et al. ApJ volume misprint 504→509; "Harlow & Welsch, The MAC
  method…" identified as harlow-welch-1965 by venue 8:2182; Schuhmann &
  Weiland cited as "this volume" (= PIER 32) by its companion paper;
  Dai–Woodward 1994 venue conflict between citing sources recorded, not
  resolved. A transcription-format defect (space-separated initials) briefly
  produced nine duplicate entries — all found and merged; the merge tool is
  fixed. Ten references excluded as un-citable (no printed year: in press /
  to appear / no year on book). **Frontier signal now live**: most-cited
  non-ingested work is Brackbill & Barnes 1980 (8 of 20 processed sources),
  then Balsara & Spicer 1999, Brio & Wu 1988, DeVore 1991, Powell's ICASE
  report 94-24 (6 each).

* **Bibliography backfill batch 1** — reference lists of 10 sources merged
  (harlow-welch-1965, yee-1966, chorin-1968, evans-hawley-1988,
  berger-colella-1989, strand-1994, hyman-shashkov-1997, almgren-1998,
  nordstrom-carpenter-1999, trask-2020): 263 printed references,
  [bibliography](/bibliography.md) grows 61 → 299 entries (238 cited but not
  ingested; 10/61 lists merged). Image-only scans (Evans & Hawley, Strand,
  Harlow & Welch body) read visually. Identity resolutions: "Shashkov 1995,
  *Conservative Finite-Difference Schemes on General Grids*" merged into
  shashkov-1996 (variant year/title recorded in the entry note);
  Hawley–Smarr–Wilson "1984a/1984b" → hawley-1984-a / hawley-1984-b. Nine
  printed references excluded as un-citable, all lacking a printed year:
  Rabinowitz (to appear; chorin-1968), Hyman–Scovel (personal communication)
  and Hyman–Shashkov (in preparation) (hyman-shashkov-1997), Adjerid–Flaherty,
  Chern–Colella, Colella LBL-17023, Dwyer AIAA 83-0449 (berger-colella-1989),
  Harlow–Welch (to be published; harlow-welch-1965), Masud–Hughes (entry
  truncated in the citing paper's printed list; trask-2020). ApJ/JCP-footnote
  reference styles print no titles — those entries carry the explicit
  placeholder "[title not printed in citing reference]" rather than
  reconstructed titles.

* **Bundle bibliography introduced (D15).** Canonical
  [`bibliography.bib`](/bibliography.bib) — every work cited by any ingested
  source, complete and unfiltered, with the `citedby` citation graph — plus
  the generated view [Bibliography](/bibliography.md)
  (`tools/bib_to_md.py`; sync linter-enforced). Seeded with the 61 ingested
  sources from Source-page frontmatter; the `citedby` graph is empty pending
  the reference-list backfill (batches of ~10 sources;
  `tools/bib_to_md.py div-free-amr/wiki --pending` is the derived worklist).
  Root [index](/index.md) catalog gained the Bibliography entry.

## 2026-07-08

* **Deep lint #6 + closing audit** (corpus complete, 61/61). Corrective
  action: created [Field-loop advection](/benchmarks/field-loop-advection.md)
  — the multi-source admission criterion had been met (4 sources) while
  `benchmarks/` sat empty; granularity debt repaid. `software/` left
  deliberately empty: production evidence lives on Source pages and no
  code earned a standalone page. **Root [index](/index.md) recurated**
  into a six-step reading guide reflecting the completed bundle; bundle
  `CLAUDE.md` status updated with the scoped-read re-ingestion targets.
  Final state: 97 conformant pages, 2 `Contradictions` blocks (one
  resolved by convergence, one live), 5 registry extensions, 0 orphans.

* **Ingestions**: [Bossavit (1998)](/sources/bossavit-1998.md) and
  [Shashkov (1996)](/sources/shashkov-1996.md) — both **scoped** (front
  matter/positioning; bodies deferred to the research-grade article
  sources). Lineage anchors for the edge-element and support-operator
  schools. **Filename error caught**: the Shashkov PDF is CRC Press 1996,
  not "2009-Wiley" as the filename claims. **Corpus complete: 61/61
  sources ingested.**

* **Ingestions**: [Desbrun, Kanso & Tong (2008)](/sources/desbrun-kanso-tong-2008.md)
  (Whitney bridge) and [Crane (2025)](/sources/crane-2025.md) (**scoped**:
  TOC/framing; pedagogical consolidation, no-free-lunch principle). No new
  pages; both merged into [DEC](/definitions/discrete-exterior-calculus.md).

* **Ingestion**: [Zampa (2024)](/sources/zampa-2024.md) — **scoped read**
  (abstract, framing, Ch. 4 divergence machinery at claim level). No new
  pages; merged the 2024-frontier note into
  [Exact discrete divergence](/properties/exact-discrete-divergence.md).

* **Ingestion**: [Hirani (2003)](/sources/hirani-2003.md) — **scoped
  supplement** (front matter/abstract; body deferred to the 2005 paper).
  No new pages; merged discrete-first philosophy and operator
  proliferation into [DEC](/definitions/discrete-exterior-calculus.md).
  Integrity note: a pattern-guessed thesis DOI was caught before staging
  and replaced by the CaltechTHESIS repository pointer — no verifiable
  DOI exists for this record.

* **Ingestion**: [de Goes, Butts & Desbrun (2020)](/sources/degoes-2020.md)
  — text extraction. No new pages; merged the industrial-deployment note
  into [DEC](/definitions/discrete-exterior-calculus.md).

* **Ingestion**: [Teixeira (2013)](/sources/teixeira-2013.md) — text
  extraction. Created [Orientation (inner/outer)](/definitions/orientation.md)
  — promoted to a page on multi-source convergence: three communities
  (CDO, Delft, lattice field theory), three vocabularies, one distinction.

* **Ingestion**: [Trask, Bochev & Perego (2020)](/sources/trask-2020.md) —
  text extraction. No new pages; merged the meshfree frontier (virtual
  faces, structure-attaches-to-operators) into
  [Support-operator method](/definitions/support-operator-method.md).

* **Ingestion**: [Palha et al. (2014)](/sources/palha-2014.md) — text
  extraction. No new pages; merged the forms/pseudo-forms framework and
  single/dual-grid equivalence into
  [Mimetic spectral elements](/methods/mimetic-spectral-elements.md).

* **Ingestion**: [Bonelle & Ern (2014)](/sources/bonelle-ern-2014.md) —
  text extraction. No new pages; merged the CDO analysis (Hodge design
  properties, orientation) into
  [Finite integration technique](/methods/finite-integration-technique.md).

* **Deep lint #5** (after 50 ingestions). Clean pass: no notation drift,
  no orphans, both `Contradictions` blocks current. Singleton tags
  reviewed — `hybrid` (FD–FV mesh hybrid) and `hybridization` (static
  condensation) deliberately kept distinct: different concepts despite
  similar names.

* **Ingestion**: [Kozdon, Erickson & Wilcox (2021)](/sources/kozdon-2021.md)
  — text extraction. No new pages; merged the hybridized trace-variable
  formulation into [SBP-SAT](/methods/sbp-sat.md).

* **Ingestion**: [Wang, Nissen & Kreiss (2017)](/sources/wang-nissen-kreiss-2017.md)
  — text extraction. No new pages; merged the 2D/corner extension of the
  convergence theory into [SBP](/definitions/summation-by-parts.md).

* **Ingestion**: [Wang & Kreiss (2017)](/sources/wang-kreiss-2017.md) —
  text extraction. No new pages; merged the convergence-gain /
  determinant-condition theory into
  [SBP](/definitions/summation-by-parts.md).

* **Ingestion**: [Friedrich et al. (2018)](/sources/friedrich-2018.md) —
  text extraction. No new pages; merged the nonlinear caveat
  (energy-stable interface coupling ≠ entropy-stable; mortar
  modification) into
  [SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md).

* **Ingestion**: [Derigs et al. (2018)](/sources/derigs-2018.md) — text
  extraction. No new pages; merged the entropy-consistent nine-wave
  synthesis into [GLM cleaning](/methods/glm-divergence-cleaning.md) and
  the thermodynamic rederivation of the source terms into
  [Eight-wave](/methods/eight-wave.md).

* **Ingestion**: [Li & Shu (2005)](/sources/li-shu-2005.md) — text
  extraction. No new pages; merged the locally-divergence-free class
  (basis-level exactness, uncontrolled interelement jumps) into
  [Exact discrete divergence](/properties/exact-discrete-divergence.md).

* **Ingestion**: [Kreeft & Gerritsma (2013)](/sources/kreeft-gerritsma-2013.md)
  — text extraction. Created
  [Mimetic spectral elements](/methods/mimetic-spectral-elements.md):
  the corpus's constructive proof that high order and pointwise exactness
  coexist (FE/spectral family, conforming curvilinear meshes; 2:1
  interfaces untouched).

* **Ingestion**: [Lipnikov, Manzini & Shashkov (2014)](/sources/lipnikov-2014.md)
  — **scoped read** (§1 closely, remainder at claim level). No new pages;
  merged the S1/S2 architecture, scheme families, and hanging-node inner
  products into
  [Support-operator method](/definitions/support-operator-method.md).

* **Ingestion**: [Perot (2011)](/sources/perot-2011.md) — text extraction.
  Created [Secondary conservation](/properties/secondary-conservation.md)
  (taxonomy; the divergence constraint positioned as the corpus's
  archetypal secondary invariant).

* **Ingestion**: [Lundquist, Malan & Nordström (2018)](/sources/lundquist-2018.md)
  — text extraction. No new pages; merged the general-mesh hybrid
  extension into
  [SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md).

* **Deep lint #4** (after 40 ingestions). One registry gap: the vector
  potential $A_h$ recurred across four pages unregistered — added to
  [notation](/notation.md). Tag vocabulary healthy (no new synonyms);
  both `Contradictions` blocks current; recurring math symbols otherwise
  all registered.

* **Ingestion**: [Del Rey Fernández et al. (2014)](/sources/delreyfernandez-2014.md)
  — text extraction. No new pages; merged the quadrature identity of
  $\mathsf{H}$, dual consistency/superconvergence, and generalized SBP
  into [SBP](/definitions/summation-by-parts.md).

* **Ingestion**: [Stone et al. (2020)](/sources/stone-2020.md) — text
  extraction. No new pages; merged the line-weighted EMF matching and the
  same-level bitwise-determinism requirement into
  [Electric-field correction](/methods/electric-field-correction.md).
  Closes the astro production line.

* **Ingestion**: [Olivares et al. (2019)](/sources/olivares-2019.md) —
  text extraction. No new pages; merged the coordinate-independent $P_D$
  generalization into
  [$P_D$](/operators/divergence-free-prolongation.md) and the
  qualitative-differences production finding into
  [Exact discrete divergence](/properties/exact-discrete-divergence.md).

* **Ingestion**: [Etienne et al. (2015)](/sources/etienne-2015.md) — text
  extraction. No new pages; merged the damped generalized Lorenz gauge
  into [Vector-potential evolution](/methods/vector-potential-evolution.md).

* **Ingestion**: [Etienne et al. (2012)](/sources/etienne-2012.md) — text
  extraction. No new pages; merged the gauge-mode diagnosis (static modes
  + interface interpolation → spurious constraint-consistent fields) and
  Lorenz-gauge cure into
  [Vector-potential evolution](/methods/vector-potential-evolution.md).

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

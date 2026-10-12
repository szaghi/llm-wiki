# Directory Update Log

## 2026-10-12

* **Batch 9: time integration from the ADAM paper collection** (6
  sources). The user assigned this class to the bundle (2026-10-12).
  Ingested [Ranocha et al. (2020)](/sources/ranocha-2020.md),
  [Ranocha et al. (2022)](/sources/ranocha-2022.md),
  [Nüßlein, Ranocha & Ketcheson (2021)](/sources/nusslein-2021.md),
  [Hadjimichael et al. (2016)](/sources/hadjimichael-2016.md),
  [Higueras & Roldán (2019)](/sources/higueras-2019.md) and
  [Runge (1895)](/sources/runge-1895.md). Three files were copied from the
  collection (all arXiv preprints) and three came from fresh downloads
  (the Springer publisher PDF of Ranocha et al. 2022, arXiv for Higueras &
  Roldán, the Zenodo scan of Runge).
  * **Deferred, not ingested:** Williams (2011, the RAW filter) and Robert
    (1966), leapfrog filters for semi-implicit weather models, outside the
    capturing-scheme scope. They can be added on request.
  * **Created:** [explicit Runge–Kutta methods](/methods/explicit-runge-kutta.md),
    [low-storage Runge–Kutta](/methods/low-storage-runge-kutta.md),
    [step-size control](/methods/runge-kutta-step-size-control.md),
    [relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md),
    [SSP linear multistep methods](/methods/ssp-linear-multistep.md) and
    [positivity-preserving adaptive Runge–Kutta](/methods/positivity-preserving-adaptive-runge-kutta.md).
  * **Updated:** [SSP Runge–Kutta](/methods/ssp-runge-kutta.md),
    [SSP order barriers](/results/ssp-order-barriers.md),
    [positivity preservation](/properties/positivity-preserving.md),
    [TVD](/properties/total-variation-diminishing.md),
    [isentropic vortex](/benchmarks/isentropic-vortex.md),
    [Sod](/benchmarks/sod-shock-tube.md),
    [Shu–Osher problem](/benchmarks/shu-osher-problem.md) and
    [interacting blast waves](/benchmarks/interacting-blast-waves.md), plus the
    root index.
  * **Clarifications, not contradictions.**
    * The SSP page's "the methods preserve … entropy inequalities" holds
      only when forward Euler satisfies the inequality; for an
      entropy-conservative semi-discretization it does not, and Ranocha et
      al. show SSP methods changing the entropy. Recorded as a qualifier.
    * The barrier page's "best two-register third-order method found has
      $\mathcal C = 0.32$" was re-read in Gottlieb, Shu & Tadmor §4.2. It
      concerns the Williamson 2N form; SSP(4,3) reaches $\mathcal C = 2$ in
      two registers in the 2N\* Shu–Osher form (Higueras & Roldán).
    * The barrier page's two-step second-order SSP value $1/2$ needs a
      negative coefficient ($b_2 = -2/5$, checked against Gottlieb, Shu &
      Tadmor's Proposition 5.2), consistent with Lenferink's bound.
    * Two reasons for multistep methods with positivity limiters (unknown
      stage wave speeds; order reduction of Runge–Kutta with the limiter)
      are recorded side by side.
  * **Notation:** new registry section "Butcher form, step-size control,
    relaxation and multistep methods" ($\mathsf a_{ij}$, $\mathsf b_j$,
    $\mathsf c_i$, $Y_i$, $p_{\mathrm t}$, $R_{\mathrm{st}}$,
    $\mathcal C_{\mathrm{eff}}$, $\mathcal C_{\mathrm{obs}}$,
    $\mathrm{err}^{n+1}$, $\beta^{\mathrm c}$, $U$, $\mathcal S$,
    $\gamma^n_{\mathrm R}$, $\Psi^n$, $\Omega_{\Delta t}$).
  * **Bibliography:** 216 references merged (1957 → 2114 entries, 157
    new). Resolutions:
    * the ingested SISC paper owns `ranocha-2020`, and the other Ranocha
      2020 works take `-b` (Numer. Math.), `-c` (J. Sci. Comput.) and `-d`
      (Comput. Math. Appl.);
    * Del Rey Fernández, printed "Fernández", is keyed
      `delreyfernandez-*`;
    * Kennedy & Carpenter's NASA TM 109112, printed with the authors
      reversed, folds into `carpenter-1994`;
    * Titarev & Toro printed 2014 is `titarev-2004`;
    * Shu's ICASE report is `shu-1998`, with a note;
    * Tadmor (1987) has two DOIs, of which the JSTOR one redirects to the
      AMS one (doi.org, checked);
    * a PETSc manual revision (`balay-2020`) and Lenferink's 1991 implicit
      paper are kept distinct from their near-namesakes.
    `--dupes` and the fuzzy-title sweep show only edition pairs (Butcher
    2008/2016, Hairer 1993/2008), which are kept.
  * **Runge (1895) has no reference list** (no bibliography, no
    footnotes), so nothing was merged for it. The linter's pending
    warning for `runge-1895` is expected. It cannot be cleared without
    inventing a citation; a tool-level "no references" marker is a
    decision for the human.

* **Deep lint (77 ingestions; the pages of batches 7 and 8).** Two
  read-only auditors re-read 46 concept pages and 15 Source pages against
  [notation](/notation.md); the compiler applied the fixes.
  * **Corrections to batch-8 text.**
    * The HLLE `Contradictions` entry on
      [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)
      said Xie et al. give no 2D HLLE run. They do (a flat plate and
      Elling's test), with smearing and no carbuncle. The entry now says so
      and adds Navas-Montilla & Murillo's HLLS evidence; the status stays
      open.
    * [Numerical shock instability](/definitions/numerical-shock-instability.md)
      no longer cites Xie et al. §6 for HLLE's robustness.
    * [HLLEM](/methods/hllem-riemann-solver.md) now writes the clipped
      speeds as $S_L^-$, $S_R^+$ and states the condition under which
      $\delta_p$ reduces to Einfeldt's form.
  * **A false gloss fixed** on [Zhang (2017)](/sources/zhang-2017.md): the
    Lemma 6 root is $(\gamma-1)\sqrt{e/2}$, below $c$, not equal to it.
  * **Three contradictions recorded that were stated only in prose**, all
    open:
    * CT against cleaning robustness, on [GLM cleaning](/methods/hyperbolic-divergence-cleaning.md)
      (pointer from [CT](/methods/constrained-transport.md));
    * positivity-limited DG on [Sedov](/benchmarks/sedov-blast-wave.md);
    * the Picard iteration count on [ADER](/methods/ader.md).
  * **Notation drift fixed:**
    * rotation angles were written as $\alpha$, $\gamma$ and $\theta$ (now
      $\theta_{\mathrm{rot}}$, $\phi_{\mathrm{rot}}$), and radii as $r$
      (now $\varrho$);
    * $u$ was used as a velocity on seven pages (now $v_x$ or
      $\vert\mathbf v\vert$);
    * $M$ and $m$ were used as lower bounds;
    * a bare source $s(u)$, a triangle written $K$, $e_i$, and the modal
      derivatives of ADER;
    * the PPM parabola variable ($\xi$ is now the cell coordinate
      $\zeta$) and the MC slope.
    * Registry section "Deep-lint additions".
  * **Batch-7 audit lists completed** on four Source pages (balsara-2017-d,
    derigs-2018, balsara-2001, mignone-2010-b).
  * **Tags merged:** steady-state→steady, spectral-analysis→spectral-resolution,
    shock-tube→riemann-problem, nonlinear-stability→stability,
    entropy-stable→entropy, balance-law→source-terms,
    preconditioning→low-mach. Missing tags added (glm, hllem,
    shock-instability).
  * **Left for later, flagged for human review:**
    * whether Harten et al. (1987) put Lax's problem in Figs. 11–15 or
      12–16;
    * two pages give the label "Ryu–Jones 1a/2a" to different problems;
    * the angle conventions on the Alfvén-wave page;
    * whether Derigs et al.'s cleaning speed bears on the open cleaning-speed
      entry (needs a PDF check);
    * candidate pages: a flat-plate boundary-layer benchmark (3 sources), a
      Kelvin–Helmholtz benchmark and an AUSM-family page;
    * prose Unicode ε and plasma β, and the remaining unregistered set-up
      constants.

* **Batch 8: Riemann solvers and shock anomalies from the ADAM paper
  collection** (8 sources). The user assigned this class of the ADAM
  collection to this bundle (2026-10-12). The bundle scope gains
  Riemann-solver design as it bears on capturing schemes: shock
  instabilities and their cures, HLLEM, low-Mach fluxes and
  well-balancing (bundle law). Five of the files came from fresh downloads
  (the collection held HTML error pages): arXiv for Xie et al.,
  institutional repositories for Dumbser & Balsara, Navas-Montilla &
  Murillo and Kitamura & Shima, and arXiv for Simon & Mandal (2019). The
  other three were copied from the collection.
  * **Two identity corrections.** The collection's "simon-2019" file
    (arXiv:1806.03187) is Simon & Mandal's HLLEM paper (IJNMF 89:533), not
    the JCP 378:477 HLLC paper its DOI names; the arXiv record carries the
    wrong DOI. Both are ingested: the HLLC preprint (arXiv:1803.04922),
    fetched separately, as `simon-2019`, and the HLLEM paper as
    `simon-2019-b`. The collection's "samala-2016" is arXiv:1611.06755,
    already ingested as [Rathan & Naga Raju (2017)](/sources/rathan-2017.md),
    so it was dropped.
  * Ingested [Simon & Mandal (2019)](/sources/simon-2019.md),
    [Simon & Mandal (2019b)](/sources/simon-2019-b.md),
    [Miczek et al. (2015)](/sources/miczek-2015.md),
    [Edelmann et al. (2021)](/sources/edelmann-2021.md),
    [Xie et al. (2021)](/sources/xie-2021.md),
    [Dumbser & Balsara (2016)](/sources/dumbser-2016.md),
    [Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md) and
    [Kitamura & Shima (2019)](/sources/kitamura-2019.md). Every one is a
    preprint or author manuscript; each Source page records which. None
    uses a reconstruction above second order. Edelmann et al. contains no
    shocks at all, and its link to this bundle is flux design.
  * Created:
    * [Numerical shock instability](/definitions/numerical-shock-instability.md)
      and the [slowly moving shock anomaly](/definitions/slowly-moving-shock-anomaly.md);
    * [Cures for numerical shock instability](/methods/shock-instability-cures.md),
      [HLLEM (HLLI) Riemann solver](/methods/hllem-riemann-solver.md) and
      [low-Mach-number fluxes](/methods/low-mach-number-fluxes.md);
    * [Well-balanced schemes](/properties/well-balanced.md);
    * benchmarks: [Quirk's odd–even test](/benchmarks/quirk-odd-even-test.md),
      [hypersonic blunt body](/benchmarks/hypersonic-blunt-body.md) and
      [stationary normal shock](/benchmarks/stationary-normal-shock.md).
  * [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md):
    a batch-8 block, and a **new open `Contradictions` entry** on whether
    HLLE is carbuncle-free. Balsara (2004) and Simon & Mandal say yes;
    Kitamura & Shima, and Xie et al.'s 1D steady shock, say no. The block
    records that Dumbser & Balsara (2016) name the solver HLLEM, with HLLI
    as an alias, and do not mention LLFI. The bundle's "HLLI / LLFI
    (Dumbser–Balsara)" bullet therefore rests on Balsara et al. (2025) for
    LLFI.
  * Batch-8 blocks on [double Mach reflection](/benchmarks/double-mach-reflection.md),
    [forward step](/benchmarks/forward-facing-step.md),
    [shock diffraction](/benchmarks/shock-diffraction.md) (description
    widened to the instability use), [double rarefaction](/benchmarks/double-rarefaction.md),
    [Sod](/benchmarks/sod-shock-tube.md), [Brio–Wu](/benchmarks/brio-wu-shock-tube.md)
    and [supersonic cylinder](/benchmarks/supersonic-cylinder-flow.md)
    (a pointer to the different Mach 20 test).
  * Both Simon & Mandal papers print the double Mach reflection end time as
    $t = 0.02$. It is recorded as printed and flagged, not corrected.
  * [Notation registry](/notation.md): new section "Riemann-solver design,
    shock instability, low Mach and well-balancing":
    * $u^{\mathrm{HLL}}_*$, $u^{\mathrm{HLLC}}_{*L,R}$, $S_L^-$, $S_R^+$,
      $\mathbf d^{\mathrm{HLL}}$, $\delta_p$, $\mathcal I$, $v_n$, $v_t$,
      $\Theta_{i+1/2}$;
    * $S^{\mathrm w}_{L,R}$, $\alpha_{\mathrm{SWM}}$, $\epsilon_{\mathrm{SWM}}$,
      $\omega_{\mathrm p}$, $\varphi_{\mathrm p}$, $\nu_y$;
    * $\mathrm{Ma}$, $\mathrm{Ma}_r$, $\mathrm{Ma}_{\mathrm{cut}}$,
      $M_{\mathrm{prop}}$, $M_{\mathrm{sig}}$, $\epsilon_{\mathrm{sh}}$,
      $\epsilon_{\mathrm g}$, $P_{\mathrm{pc}}$, $\mu_{\mathrm{pc}}$,
      $\delta_{\mathrm{pc}}$;
    * $\mathbf s(u)$, $u^{\mathrm{eq}}$, $\varphi_{\mathrm g}$, $\mathbf g$.
  * **Bibliography.** 436 references merged with `tools/bib_merge.py`,
    using the vol:page resolver and reviewed overrides:
    * `kappeli-2016` (A&A 587:A94 = 587:94) and `toro-2009` (3rd ed.) kept
      on their existing keys;
    * `zhang-2016-b` (Comput. Fluids 134:11) and `zhang-2017-b` (IJNMF
      84:135), so neither lands on an unrelated key, `zhang-2017` being the
      ingested source;
    * Edelmann et al.'s "accepted in CiCP" Berberich 2020 onto
      `berberich-2021` (Crossref, same four authors), with the thesis as
      `berberich-2021-b` and the Comput. Fluids paper as `berberich-2021-c`;
    * this last one was first wrongly merged into the thesis, caught by a
      per-fragment collision check and redone from the pre-batch file;
    * 15 reviewed silences of distinct pairs (FLAGS 0); `xie-2021` merged
      first so that `simon-2019` lands in its published form.
    * **Closing sweeps.** `--dupes` folded two first-author spelling
      variants (`pandolfini-2001` into `pandolfi-2001`, `gressiera-2000`
      into `gressier-2000`). The fuzzy-title sweep left distinct editions,
      a reprint and a conference/journal pair apart.
    * 1707 → 1957 entries.

## 2026-10-09

* **Batch 7: gap closure against the ADAM paper collection** (7 sources).
  A cross-check of the ADAM bibliography's numerics and MHD papers against
  this bundle found these missing. Archive copies were added: four from the
  div-free-amr archive (D17), Ryu & Jones from the ADAM collection, and two
  downloaded because the collection held HTML error pages in their place
  (Zhang 2017 from the author's page; Balsara 2017 from NSF PAR).
  * Ingested [Ryu & Jones (1995)](/sources/ryu-1995.md),
    [Balsara (2001)](/sources/balsara-2001.md),
    [Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md),
    [Zhang (2017)](/sources/zhang-2017.md),
    [Balsara (2017)](/sources/balsara-2017-d.md) (213-page review, whole
    text read), [Derigs et al. (2018)](/sources/derigs-2018.md) and
    [Tomida et al. (2026)](/sources/tomida-2026.md). Two other "missing"
    papers were already ingested under their journal DOIs
    ([Guo et al. (2014)](/sources/guo-2014.md), [Rathan & Naga Raju (2017)](/sources/rathan-2017.md)).
  * Created [Ryu–Jones and Dai–Woodward MHD shock tubes](/benchmarks/ryu-jones-shock-tubes.md).
  * Rewrote [Hyperbolic (GLM) divergence cleaning](/methods/hyperbolic-divergence-cleaning.md):
    CTU-GLM and the origin of $\alpha_p$, EGLM, the entropy-consistent
    system, the consistency conditions on the cleaning parameters, AMR, and a
    **new open `Contradictions` entry**: should the cleaning speed follow the
    time step (Mignone et al. against Tomida et al.)?
  * Corrected the attribution of the second-order divergence-free
    reconstruction formulas on
    [divergence-free reconstruction](/methods/divergence-free-reconstruction.md):
    they first appear in Balsara (2001), not (2004); added its AMR section.
  * Added "Later uses (batch 7)" blocks to 31 pages: CT, high-order AMR,
    positivity, scaling limiter, WENO-limited DG, characteristic
    decomposition, Riemann solvers, ADER, PPM, WENO, SSP-RK, subcell
    limiting, TVD, PLUTO and 17 benchmarks. Flagged for human review:
    [Sedov](/benchmarks/sedov-blast-wave.md), where Zhang (2017) runs DG
    with only the positivity limiter to completion against an earlier
    "blows up" statement; and an attribution tension on the ADER-CG
    iteration count ([ADER](/methods/ader.md)).
  * [Notation registry](/notation.md): new section "Cleaning parameters,
    MHD eigensystems and viscous positivity" ($L_{\mathrm{GLM}}$, $C_r$,
    $\hat\psi_{\mathrm{GLM}}$, $\alpha_f$, $\alpha_s$, $B_\perp$,
    $\mathbf f^{\mathrm v}$, $\boldsymbol\tau$, $\mathbf q$, $\beta^{\mathrm v}_{i+1/2}$,
    $\theta_e$, $\hat f^{\mathrm{EC}}$, $\hat f^{\mathrm{ES}}$).
  * Bibliography: 585 references merged with `tools/bib_merge.py`, using
    the vol:page resolver, nine manual overrides and 11 reviewed silences of
    distinct pairs, plus one temporary silence for the Kurganov fold (FLAGS 0); seed entries for derigs-2018 and tomida-2026. Folds:
    `harten-1983-b` into `harten-1983` (balsara-2001 prints the same
    misprinted venue with the title, which settles the open identity), the
    UCLA report `kurganov-2001` into `kurganov-2000`, and, from the closing
    `--dupes` and fuzzy-title sweeps, five spelling or author-order variants
    and `deng-2005` into `deng-2000`. Crossref-checked: Antón et al. 2010
    (ApJS 188:1, printed 187:1) and Ha et al. 2005 (J. Sci. Comput. 24:29).
    `dai-1994` keeps ryu-1995's title-less "in press" citation by inference,
    recorded in its note. 1494 → 1707 entries.

## 2026-10-08

* **Human review of batch 6** (fiat decisions, recorded with
  `status: hypothesis` attribution):
  * [Constrained transport](/methods/constrained-transport.md): the Yee-mesh
    contradiction (Balsara & Kim against Christlieb et al.) is *closed by
    human fiat*. Both are reasonable, for different discrete divergences,
    and both designs are kept.
  * [Self-similarity](/properties/self-similarity.md): human note that ε is
    not a non-dimensional parameter and that its mesh and flow dependences
    are a real concern.

* **Batch 6 (12 sources, the last of the archive), ingested autonomously on
  user instruction** and staged as one unit:
  [Balsara (2004)](/sources/balsara-2004.md),
  [Balsara (2009b)](/sources/balsara-2009-b.md),
  [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md),
  [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md),
  [Balsara & Kim (2016)](/sources/balsara-2016-b.md),
  [Balsara et al. (2023)](/sources/balsara-2023.md),
  [Seo & Ryu (2023)](/sources/seo-2023.md),
  [Berta et al. (2024)](/sources/berta-2024.md),
  [Ding & Wu (2024)](/sources/ding-2024.md),
  [Bernardini et al. (2021)](/sources/bernardini-2021.md),
  [Shu (2009)](/sources/shu-2009.md),
  [Shu (2020)](/sources/shu-2020.md).
  All 62 archived PDFs are now ingested. Papers were read by parallel
  subagents into scratch notes and reference fragments; the compiler wrote
  every page from those notes.
  * **Created** 11 concept pages:
    * methods: divergence-free reconstruction, hyperbolic (GLM) divergence
      cleaning, edge-centred curl-preserving reconstruction, negative
      linear weights;
    * property: self-similarity;
    * benchmarks: circularly polarized Alfvén waves, field-loop
      advection, grid-oblique MHD shock tubes;
    * software (the folder's first pages): STREAmS, HOW-MHD, PLUTO.
  * **Updated**:
    * methods: constrained transport (primary source for the unstaggered
      design, new sections on fourth-order upwind CT, staggered FD-CT from
      WENO fluxes and projection of reconstructed traces), fourth-order
      finite volume (pointwise reconstruction), WENO, ENO, WENO-AO,
      WENO-Z, mapped WENO, central WENO, WENO-limited DG, MP limiting,
      energy-stable WENO, hybrid compact-WENO, PPM, ADER, Lax–Wendroff,
      Riemann solvers, characteristic decomposition, SSP Runge–Kutta,
      conservative FD, FV reconstruction, alternative FD-WENO,
      polynomial WENO, inverse Lax–Wendroff, scaling limiter;
    * definition: smoothness indicator; result: weight accuracy
      conditions;
    * properties: positivity preservation, accuracy at critical points;
    * benchmarks: Orszag–Tang, rotor, blast, shock–cloud, Brio–Wu,
      high-Mach jet, shock–vortex, isentropic vortex (MHD and relativistic
      variants);
    * the root reading guide: items 3, 9, a new item 12 (codes), 13.
  * **Contradictions.**
    * *Opened* on constrained transport: Balsara and Kim state that
      divergence-free MHD "requires" a Yee mesh; Christlieb et al.'s
      unstaggered CT keeps its central discrete divergence exactly zero.
      The compiler notes that the two use different discrete divergences.
    * *Open, new evidence:* first-order Lax–Friedrichs MHD positivity.
      Ding and Wu report a proof by Wu (2018), conditional on a discrete
      divergence-free property. This is secondhand; Wu (2018) is the
      decisive ingestion target.
    * *Closed, later position recorded:* critical points. Shu (2020) still
      calls the Jiang–Shu proof valid but concedes the degeneracy for some
      extrema, which he says needs ε of $10^{-10}$ or smaller; the closure
      stands.
    * *Open, unchanged:* WENO-ZQ non-oscillation (Shu 2020 runs no tests).
  * **Kept inline**: $K$ against $K + 1$ ADER predictor iterations; the
    CT resistivity coefficient (about 0.01 in 2016, 0.02–0.2 in 2014, with
    different integrators); global against local Lax–Friedrichs for MHD
    (2014 found no difference); Shu's view that $\varepsilon = 10^{-6}$ is
    legitimate design, against Henrick et al.'s "masking"; Shu's
    self-similarity principle against mesh-dependent ε (a design-principle
    conflict); the parametric-instability statements of the two
    torsional-wave papers.
  * **Recorded as printed**: Balsara (2004) labels the explicit midpoint
    rule "TVD … Heun"; Balsara and Kim's Tables 3 and 4 are identical;
    Balsara (2009b) labels RK tables "ADER"; Seo and Ryu's eq. 47 swaps the
    blast pressures; Shu (2020) calls $10^{-12}$ "close to machine zero".
  * **Registry extensions** ([notation](/notation.md)): $\psi$ (in use since
    batch 3, now registered), $\psi_{\mathrm{GLM}}$, $c_h$, $c_p$,
    $\alpha_p$, $c_f$, $c_A$, $c_s$, $\hat B_{x,\mathbf m}$, $f^{**}_x$,
    $A^{\mathrm{DDF}}_x$, $\rho e(u)$, $\mathbf J$, $\boldsymbol\Omega$.
  * **Bibliography**: 1086 printed references merged with 0 flags under
    155 scoped aliases, 41 checked silences, 21 notes and 3 field fixes;
    1003 → 1494 entries. Many citing lists number same-author-year works in
    printed order, so their `-b`/`-c` suffixes swap against the master; a
    resolver matched each fragment entry to an existing work by printed
    vol:page or near-identical title (same surname stem), allocated fresh
    suffixes otherwise, and every match and allocation was reviewed. Twelve
    manual overrides fix resolver errors or settle identities (e.g. chou-2006/2007 and
    xing-2006-b/-c are distinct works).
    * Same-key venue check: all mismatches explained (Brackbill & Barnes
      35:462 for 426; Colella–Sekora vol. 277 for 227; Helzel et al.
      227:9527 for 230:3803, Crossref; SIAM page B1302).
    * Field fixes: Stone & Norman 80:791 is ApJS (Crossref); Wu & Shu's
      SIAM page B1302; MHDCLAW's year is the citing date.
  * **Closing sweeps (final batch, whole corpus).** `--dupes` found three
    spelling variants (Del Zanna printed "Zanna", Merriman printed
    "Merryman", Friedrich printed "Friedrichs"), folded. The fuzzy-title
    and venue sweeps found two misprinted citations (Roe's 1981 paper with
    Sod's venue, now on roe-1981; Mock & Lax with reversed authors) and
    three report or submitted versions of published papers, folded into
    them: jiang-1997-b into jiang-2000, powell-2009 into powell-1994,
    xiong-2013 into xiong-2016. One citation stays undecided (pao-1981-b
    carries Meadows et al.'s title). Edition pairs (Toro 1997/2009) and
    conference/journal pairs (Aftosmis 1997/1998) stay separate.
  * **Deep lint (62 ingestions, corpus complete)**: four registry
    collisions in the new text fixed ($\gamma$ for the Lorentz factor,
    $\eta$ and $\nu$ for a flattener and a resistivity coefficient); tag
    `curvilinear` merged into `mapped-grid`; the unregistered gauge scalar
    $\psi$ registered; contradiction entries reviewed as above.

* **Batch 5 (10 sources), ingested autonomously on user instruction** and
  staged as one unit: [Jiang & Wu (1999)](/sources/jiang-1999.md),
  [McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md),
  [Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md),
  [Owen, Guzik & Gao (2018)](/sources/owen-2018.md),
  [Wang et al. (2025)](/sources/wang-2025.md),
  [Ding, Shu & Zhang (2020)](/sources/ding-2020.md),
  [Lu et al. (2021)](/sources/lu-2021.md),
  [Liu et al. (2022)](/sources/liu-2022.md),
  [Liu et al. (2023)](/sources/liu-2023.md),
  [Liu et al. (2025)](/sources/liu-2025.md).
  Papers were read by parallel subagents into scratch notes and reference
  fragments; every page was written by the compiler from those notes.
  * **Created** 5 concept pages:
    * method: fourth-order finite volume with average–point conversions;
    * property: free-stream preservation on curvilinear grids;
    * benchmarks: Brio–Wu MHD shock tube, supersonic flow past a
      cylinder, shock-driven cylinder lift-off.
  * **Updated**:
    * methods: inverse Lax–Wendroff (new sections on sign-changing wind,
      conservation, moving boundaries, interfaces between two media),
      high-order AMR (new section on block-structured hierarchies with
      Runge–Kutta subcycling; the $r_{\mathrm{AMR}} \ge K$ rule now
      attributed to the tree design), weighted extrapolation (new section
      on multi-resolution WENO extrapolation), constrained transport (new
      section on projection), WENO, characteristic decomposition,
      conservative finite difference, alternative FD-WENO, MP limiting,
      PPM, finite-volume reconstruction (the Gauss-quadrature sentence
      qualified at fourth order), SSP Runge–Kutta;
    * property: accuracy at critical points;
    * benchmarks: Orszag–Tang, double Mach reflection, interacting blast
      waves, isentropic vortex, Sod, Lax, Shu–Osher, 2D Riemann problems;
    * the root reading guide: items 8, 9, 11 and 12.
  * **Contradictions**: none opened. Kept inline as design trade-offs or
    scope differences:
    * Chen et al. omit refluxing because it costs FD its order, and Wang
      et al. reflux anyway for robustness and accept second-order
      conservation error. Both report the same order effect (AMR page).
    * Lu et al. (2021) take only $u^{*(0)}$ from the data, below the SILW
      threshold; the authors flag stability above fifth order (ILW page).
    * Liu et al. (2025) analyse stability only at the DG solid's Courant
      number, far below the fluid scheme's limit (ILW page).
    * Owen et al. and Chen et al. run fourth and fifth order with
      $r_{\mathrm{AMR}} = 2$, outside the tree rule $r_{\mathrm{AMR}} \ge K$
      (AMR page).
  * **Recorded as printed** (internal inconsistencies of single sources):
    Ding et al.'s Example 5 exact solution does not satisfy its PDE; Wang
    et al. call their prolongation fourth order and their restriction fifth
    order, where the coefficients give sixth (compiler's check), and print
    12/32 for 21/32; Liu et al. (2025) eq. 4.1 has a sign that their own
    eigenvectors contradict; Jiang and Wu write $B_x^2 + B_y^2$ for
    $B_y^2 + B_z^2$ once.
  * **Registry extensions** ([notation](/notation.md)): $c$, $T$, $T_b$,
    $\Phi$, $f^{*(k)}$, $f_{-\varsigma}$, $\varpi_j$, $\tilde{\mathcal M}$,
    $\hat f^{\mathrm{tot}}_{i+1/2}$, $\hat f^{\mathrm R}_{i+1/2}$, $\dot a$,
    $\epsilon_{\mathrm{ILW}}$, $\mathbf X$, $\mathcal J$, $\tilde m^a_b$,
    $\tilde f^a$, $\mathbf e_d$, $\Delta_h$, $\Delta^\perp_h$, $\mathbf W$,
    $\langle w\rangle_i$, $\langle w\rangle_{i+1/2}$, $C_2$, $C_3$, $\chi$,
    $k_m$, $M_s$, $\mathrm{Re}$, $\mathrm{Pr}$. Collisions avoided: Ding
    et al.'s quadrature weights $\omega_j$ (now $\varpi_j$), Liu et al.'s
    swapped $\epsilon$/$\mu$, the computational coordinates $\xi, \eta, \zeta$
    (now $X^a$), McCorquodale and Colella's flattening coefficient (1 means
    none, the opposite of $\phi_i$).
  * **Bibliography**: 351 printed references (348 fragment entries, after
    three repeats within Wang et al.'s list) merged with 0 flags, under 21
    scoped aliases, 3 checked silences, 14 notes and 4 field fixes;
    845 → 1003 entries.
    * Same-key venue check: all mismatches explained. Two master entries
      were wrong and are fixed against Crossref: Roe & Balsara (1996) is in
      SIAM J. Appl. Math., not SIAM J. Numer. Anal.; Peskin (2002) starts
      at Acta Numer. 11:479, not 11:1. Berger & Colella's first page
      printed as 67 by Chen et al. is a misprint (Crossref: 64).
      Jeffrey & Taniuti's second author is T., not A.
    * Identities settled: Jiang, Shu & Zhang's free-stream report is the
      published jiang-2014; Zhang, Johansen & Colella's preprint is
      SISC 34:B179 (zhang-2012-c); the Brown preprint cited by Liu et al.
      (2022) is liu-2023; "Vanna" is De Vanna (devanna-2020); JCAM 400 is
      the 2022 issue (li-2022).
    * Closing sweeps: `--dupes` found one cross-stem pair (the De Vanna
      spelling, folded); the fuzzy-title sweep found the two editions of the
      Chombo design document (2009 and 2014, kept separate with notes);
      the venue sweep found no duplicates.
  * **Deep lint (50 ingestions)**: no notation drift in the batch-5 pages
    and no paper-native symbols in concept pages. Tag synonyms normalized:
    `viscous` → `navier-stokes`, `runge-kutta` → `time-discretization`
    (including gottlieb-2001 from batch 3), `characteristic-decomposition`
    → `eigenvectors`, `monotonicity-preserving` → `monotonicity`. The four
    `Contradictions` entries (two open, two closed) have no new evidence.

* **Batch 4 (10 sources), ingested autonomously on user instruction** and
  staged as one unit: [Qiu & Shu (2005)](/sources/qiu-2005.md),
  [Dumbser & Käser (2007)](/sources/dumbser-2007.md),
  [Balsara et al. (2009)](/sources/balsara-2009.md),
  [Dumbser et al. (2013)](/sources/dumbser-2013.md),
  [Dumbser et al. (2014)](/sources/dumbser-2014.md),
  [Zanotti et al. (2015)](/sources/zanotti-2015.md),
  [Fisher et al. (2011)](/sources/fisher-2011.md),
  [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md),
  [Li, Shu & Zhang (2016)](/sources/li-2016.md),
  [Lu et al. (2016)](/sources/lu-2016.md).
  * **Created** 10 concept pages:
    * methods: ADER, polynomial WENO, WENO limiters for DG, a posteriori
      subcell limiting (MOOD), high-order AMR, inverse Lax–Wendroff,
      weighted extrapolation, energy-stable WENO;
    * benchmarks: 2D Riemann problems, cylindrical and spherical explosion.
  * **Updated**:
    * methods: WENO, finite-volume reconstruction, Lax–Wendroff (Taylor),
      SSP Runge–Kutta, constrained transport (new section on staggered
      divergence-free reconstruction with ADER, and on GLM cleaning),
      approximate Riemann solvers, WENO-Z, conservative finite difference,
      characteristic decomposition;
    * definition: smoothness indicator;
    * result: SSP order barriers;
    * properties: positivity preservation, accuracy at critical points;
    * benchmarks: interacting blast waves, Shu–Osher, DMR (including a
      triangle-ramp variant), forward step, Lax, Sod, isentropic vortex,
      Orszag–Tang, rotor, MHD blast, shock–vortex, composite profile;
    * the root reading guide: new items 10 (limiting high-order DG) and
      11 (boundaries and adaptive meshes).
  * **Contradictions**: none opened. Kept inline as scope, parameter or
    attribution differences:
    * Li et al.'s 1D stability of outflow Lagrange extrapolation, against
      Baeza et al.'s mild instability of Lagrange extrapolation on complex
      2D domains (ILW page);
    * Zanotti et al. attribute $\delta_{\mathrm{DMP}} = \max(\delta_0, \dots)$
      to Dumbser et al. (2014), whose arXiv version read here has no
      $\delta_0$ (subcell-limiting page);
    * different polynomial-WENO parameters across papers
      ($d_{\mathrm c} = 10^3$, 100 or $10^5$; $q = 4$ or 8);
    * different rotor variants (taper, $\gamma$).
  * **Flagged inside one source**: Fisher et al. require
    $O(h^3) \le \varepsilon \le O(h^2)$ for design order at critical points
    but prescribe $\varepsilon \propto h^4$ in the implementation recipe
    (energy-stable WENO page). Also recorded as printed:
    * Dumbser et al. (2014) print the Shu–Osher data as $\sin(5\pi x)$ and
      $t = 0.18$;
    * Zanotti et al. give the 3D explosion degree as 3 in the text and 5
      in the caption.
  * **Agreement noted**: Li et al.'s SSP-RK3 limits for orders 5–13
    (1.43 to 0.99) match Balsara and Shu's range.
  * **Registry extensions** ([notation](/notation.md)):
    * modal and DG: $\zeta$, $P_l(\zeta)$, $\hat u^{(l)}_i$;
    * polynomial WENO: $d_{\mathrm c}$, $\mathsf B$;
    * one-step schemes: $u^{\mathrm p}_i$;
    * DG limiting: $\mathcal{B}_i$, $N_{\mathrm s}$, $\bar v_{i,m}$, $\Pi$,
      $\mathcal R$, $\delta_{\mathrm{DMP}}$ (with $\delta_0$,
      $\epsilon_{\mathrm{DMP}}$), $V_i$, $M$, $\operatorname{minmod}_M$,
      $x_G$, $w_G$;
    * boundaries: $g(t)$, $C_a$, $u^{*(k)}$, $n_{\mathrm b}$,
      $k_{\mathrm{ILW}}$, $\mu$, $\theta_{\mathrm{ILW}}$, $\varsigma$,
      $x_N$, $e_j$, $\omega^{\mathrm{ext}}_k$, $x^{\mathrm g}$,
      $\breve u_k$, $\lambda_{\mathrm{UW}}$;
    * summation by parts: $\mathsf P$, $\mathsf Q$, $\mathsf D$;
    * time stepping: $\nu_{\max}$;
    * AMR: $r_{\mathrm{AMR}}$, $N_{\mathrm{lev}}$;
    * the GP amplitude $\Sigma^2$, which was used on the GP-WENO page but
      unregistered.
  * **Bibliography**: 10 fragments (575 printed references) merged with
    `tools/bib_merge.py`. The resolutions module had 63 scoped aliases, 10
    verified silences and 13 notes; the merge ran to FLAGS: 0. The record
    grew from 597 to 845 works. The alias families: Qiu & Shu 2004–2005,
    Dumbser 2005–2014, the Balsara pairs, and the Cockburn and Carpenter
    pairs.
  * **Master renames**, done before the merge (pre-merge copy kept in the
    session scratchpad):
    * `qiu-2005` → `qiu-2005-b` (the CMAME Lax–Wendroff DG paper), so the
      ingested SISC paper takes the bare key;
    * `friedrichs-1998` → `friedrich-1998` (Crossref: Oliver Friedrich);
    * `berger-1990` → `berger-1989` (Crossref: JCP 82 is the May 1989 issue).
  * **Identity checks on Crossref**:
    * Hermite WENO I is JCP 193 (2004): `qiu-2004`;
    * JCP 248:200 is Zhu, Zhong, Shu & Qiu, printed with scrambled authors:
      `zhu-2013-b`;
    * Abgrall is JCP 114:45; the citing lists misprint 144.
  * **New check — same-key venue comparison.** `bib_merge` flags a same-key
    conflict only for *dissimilar* titles, so near-identical titles merge
    silently. Comparing the printed vol:page of every same-key merge found:
    * in batch 4, swapped Cockburn & Shu 1989 parts II/III in three lists,
      a second van Leer 1979 print landing on the TICOM proceedings entry,
      and Schulz-Rinne's two 1993 papers;
    * run retroactively over batches 1–3, two citations attached to the
      wrong work: castro-2011's Yamaleev & Carpenter JCP 228:3025, from
      batch 2; and zhang-2012's Cockburn et al. JCP 84:90 (part III), from
      batch 3. Both are moved, with notes;
    * three printed misprints, now noted.

    The check is not part of `bib_merge` yet.
  * **Closing sweeps**:
    * `--dupes`: one same-stem group, `yang-2009` / `yang-2009-b` (AIAA
      paper vs journal paper, distinct);
    * venue sweep: one real duplicate, `filbert-2013` folded into
      `filbet-2013`;
    * fuzzy-title sweep: only known distinct works.
  * **Versions read**:
    * `dumbser-2013` as arXiv:1212.3585v3;
    * `dumbser-2014` as arXiv:1406.7416v3 and `zanotti-2015` as
      arXiv:1412.0081v2, despite their journal-style filenames;
    * `baeza-2016` as the accepted manuscript (arXiv:2501.17106v1).

    All are checked on Crossref against the published versions.
  * **Deep lint** (due at 40 ingestions; whole bundle):
    * no $\Delta x$ or $\epsilon$ drift left in concept pages;
    * the new ghost index (was $p$, now $\varsigma$), the plasma beta, the
      CFL symbols and the extrapolation recurrence (was $u^{(k)}$, which
      collides with RK stages) were rewritten into registry notation;
    * a GP amplitude clash was resolved: the oscillation-indicator matrix
      became $\mathsf B$;
    * tags: no synonyms found (`spectral-analysis` and
      `spectral-resolution` are distinct);
    * contradictions: the two closed entries still hold; the open WENO-ZQ
      and MHD-positivity entries have no new evidence;
    * the retroactive bibliography venue check above.

* **Batch 3 (10 sources), ingested autonomously on user instruction** and
  staged as one unit: [Gottlieb, Shu & Tadmor (2001)](/sources/gottlieb-2001.md),
  [Titarev & Toro (2004)](/sources/titarev-2004.md),
  [Zhang & Shu (2010)](/sources/zhang-2010.md),
  [Zhang & Shu (2012)](/sources/zhang-2012.md),
  [Hu, Adams & Shu (2013)](/sources/hu-2013.md),
  [Guo, Xiong & Shi (2014)](/sources/guo-2014.md),
  [Christlieb et al. (2016)](/sources/christlieb-2016.md),
  [Reyes et al. (2018)](/sources/reyes-2018.md),
  [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md),
  [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md).
  * **Created** 20 concept pages:
    * result: SSP order barriers;
    * property: positivity preservation;
    * methods: scaling and flux positivity limiters, compact-reconstruction
      WENO, GP-WENO, alternative finite-difference WENO, Lax–Wendroff
      (Taylor) time discretization, constrained transport, approximate
      Riemann solvers;
    * benchmarks: Sedov, double rarefaction, Leblanc, Mach 2000 jet, shock
      diffraction, isentropic vortex, Orszag–Tang, MHD rotor, MHD blast,
      shock–cloud.
  * **Updated** SSP Runge–Kutta, WENO, finite-volume reconstruction,
    conservative finite difference, characteristic decomposition, WENO-Z,
    WENO-AO (new section on WENO-AO interpolation), smoothness indicator,
    hybrid compact-WENO, monotone flux, central WENO, accuracy at critical
    points, and the DMR, forward-step, blast-wave, Lax, Sod and Shu–Osher
    benchmarks.
  * **Contradictions**: **opened** on
    [positivity preservation](/properties/positivity-preserving.md): is the
    first-order Lax–Friedrichs MHD update provably positive? Christlieb et
    al. say it is conjectured and unproven; Balsara et al. say Gurski proved
    it. The scopes may differ, and Gurski is not in the corpus.
  * **Not recorded as contradictions**, kept inline: Titarev & Toro's
    1D RK3 stability condition (CFL $\le 1$, called "optimal" without
    derivation) against Balsara & Shu's linear-stability 1.43
    (SSP Runge–Kutta page); and Balsara et al.'s "FD cannot draw on ADER"
    against the existence of FD single-step Taylor schemes (Taylor
    time-discretization page). Both are scope or definition differences.
  * **Registry extensions** ([notation](/notation.md)):
    * positivity: $\rho(u)$, $p(u)$, $\epsilon_{\mathcal G}$, $\nu_0$,
      $\mathcal P_i$, $K$, the Gauss–Lobatto points and weights,
      $\theta_\rho$, $\theta_p$, $\hat f^{\mathrm{LO}}$/$\hat f^{\mathrm{HO}}$
      and $\sigma$;
    * Riemann solvers: $S_L$, $S_R$, $S_M$ (and $S_D$, $S_U$);
    * time stepping: $\eta$, $K_{\mathrm L}$, $\mathcal F^n_i$;
    * MHD: $\boldsymbol{\mathcal E}$, $\mathbf A$, the face and edge
      averages;
    * GP symbols;
    * the directional spacings $h_x$, $h_y$, $h_z$.
  * **Bibliography**: 10 fragments (455 printed references) merged with
    `tools/bib_merge.py`. The resolutions module had 51 scoped aliases, 13
    verified silences and 11 notes; the merge ran to FLAGS: 0. The record
    grew from 342 to 597 works. The alias families:
    * Shu (SISC 1988) printed before Shu & Osher (JCP 1988);
    * the Zhang–Shu positivity and maximum-principle papers;
    * the Balsara papers. Bare keys stay free for archived works awaiting
      ingestion: `balsara-2009-b`, `balsara-2016-b`, `balsara-2023`,
      `mignone-2010`, `chen-2016` (see bundle law).
  * **Master renames**, done before the merge to follow the
    published-year key rule (pre-merge copy kept in the session scratchpad):
    * `balsara-1997` → `balsara-1999`;
    * `balsara-2000-b` → `balsara-2001-b`, identified with ApJS 132:83;
    * `gottlieb-1997` → `gottlieb-1998`;
    * `tadmor-1997` → `tadmor-1998`, the report form of the LNM 1697 chapter;
    * **correction of batch 2**: `kim-2006` → `kim-2005-b`. Kim & Kwon is
      J. Comput. Phys. 210:554 (2005), verified on Crossref; martin-2006
      had printed 215:417 (2006), and batch 2 had followed it.
  * **Closing sweeps**:
    * `--dupes` found two spelling duplicates, both folded: `loubcre-2005`
      into `loubere-2005`, and `tao-1999` into `tang-1999`;
    * the venue sweep found no real collisions;
    * the fuzzy-title sweep found only distinct works and the known JCP
      republications. `roe-1997` is noted as the JCP 135 republication of
      `roe-1981` (verified on Crossref).
  * **Versions read**:
    * `hu-2013` as arXiv:1203.1540v5, although its filename says JCP;
    * `guo-2014` as arXiv:1402.5618v2;
    * `balsara-2025` as the author manuscript. Its slug takes the issue
      year 2025 (online 2024); the bundle law now says the year is the
      issue year.
  * **Deep lint** (first one, due since 10 ingestions; whole bundle):
    * tag synonyms fixed: `three-dimensional` → `3d`, `weno-ao` →
      `adaptive-order`; `smooth` dropped;
    * notation drift fixed in older pages: $\Delta x$ → $h$ in SSP
      Runge–Kutta, MP limiting and Sod;
    * notation drift fixed in new pages: GP indices and eigenpairs (the
      Jacobian eigenvalue $\lambda$ and the weights $d_k$ were clashing),
      $\lambda = \Delta t/h$ and the partition weights $\alpha_x$,
      $\alpha_y$ in the flux-limiter page, the floors
      $\epsilon_\rho$/$\epsilon_p$, and the vortex strength $\epsilon$;
    * contradictions: two closed entries (MP fiat, Henrick supersession)
      still hold; the WENO-ZQ entry is still open, with no new evidence in
      batch 3.

* **Batch 2 (10 sources), ingested autonomously on user instruction** and
  staged as one unit: [Pirozzoli (2002)](/sources/pirozzoli-2002.md),
  [Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md),
  [Martín et al. (2006)](/sources/martin-2006.md),
  [Borges et al. (2008)](/sources/borges-2008.md),
  [Hu, Wang & Adams (2010)](/sources/hu-2010.md),
  [Castro, Costa & Don (2011)](/sources/castro-2011.md),
  [Fu, Hu & Adams (2016)](/sources/fu-2016.md),
  [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md),
  [Zhu & Qiu (2016)](/sources/zhu-2016.md),
  [Rathan & Naga Raju (2017)](/sources/rathan-2017.md).
  * **Created** 9 concept pages: methods (mapped WENO, WENO-Z,
    central-upwind WENO, TENO, WENO-AO/ZQ, bandwidth-optimized WENO,
    hybrid compact-WENO); definition (modified wavenumber); result (WENO
    weight accuracy conditions). **Updated** WENO, central WENO,
    smoothness indicator, accuracy at critical points, MP limiting, SSP
    Runge–Kutta, conservative finite difference, characteristic
    decomposition and all eight benchmarks.
  * **Contradictions**: the MP-limiting entry (batch 1) **closed by human
    fiat in favour of Balsara & Shu** (recorded on the page with
    `status: hypothesis` attribution). The critical-point entry on
    [accuracy at critical points](/properties/accuracy-at-critical-points.md)
    **closed by explicit supersession**: Henrick et al. show WENO-JS loses
    order at first-order critical points, confirmed by Borges et al. and
    Castro et al. **Opened** on [WENO-AO](/methods/weno-ao.md): Zhu–Qiu's
    non-oscillation claim for WENO-ZQ vs Balsara et al.'s composite-advection
    overshoots.
  * **Registry extended**: $n_{\mathrm{cp}}$, mapping $g_k(\omega)$,
    $\tau_{2r-1}$, $\tau_6$, $C_w$, TENO $\gamma_k$, $\chi_k$, $\delta_k$,
    $C_T$; AO $\gamma_{\mathrm{Hi}}, \gamma_{\mathrm{Lo}}$; hybrid switch
    threshold $\vartheta$; wavenumber $\xi$ and modified wavenumber
    $\tilde\xi$.
  * **Bibliography**: 10 fragments, 295 references merged with
    `tools/bib_merge.py` (FLAGS: 0); 190 → 342 works. 15 scoped key
    aliases (Harten report/proceedings variants, misprinted years for
    Henrick 2005 and Kim & Kwon 2006, same-key different-work splits
    `martin-2006-b`, `fedkiw-2000-b`, `hu-2011-b`, `hu-2016-b`), three
    silenced pairs (Levy 2000 vs Levy 1999 ×2, Harten 1983 self-pair).
    Closing sweeps (`--dupes`, venue collisions, fuzzy titles): folded
    `deng-2005` into `deng-2000`, renamed Liu & Osher's convex ENO to
    `liu-1998-b`, and added a republication note to `harten-1997`.
  * **Versions read**: rathan-2017 as arXiv:1611.06755v1 (slug and metadata
    follow the Comput. Fluids version, verified on Crossref).

* **Batch 1 (10 sources), ingested autonomously on user instruction** and
  staged as one unit: [Colella & Woodward (1984)](/sources/colella-1984.md),
  [Harten et al. (1987)](/sources/harten-1987.md),
  [Shu & Osher (1988)](/sources/shu-1988.md),
  [Shu & Osher (1989)](/sources/shu-1989.md),
  [Liu, Osher & Chan (1994)](/sources/liu-1994.md),
  [Jiang & Shu (1996)](/sources/jiang-1996.md),
  [Suresh & Huynh (1997)](/sources/suresh-1997.md),
  [Shu (1998)](/sources/shu-1998.md),
  [Levy, Puppo & Russo (1999)](/sources/levy-1999.md),
  [Balsara & Shu (2000)](/sources/balsara-2000.md).
  * **Created** 23 concept pages: methods (PPM, finite-volume
    reconstruction, ENO, WENO, conservative finite difference, SSP
    Runge–Kutta, characteristic decomposition, MP limiting, central WENO,
    contact sharpening); definitions (essentially non-oscillatory,
    monotone flux, smoothness indicator); properties (TVD/TVB, accuracy at
    critical points); eight benchmarks.
  * **Registry extended**: primitive $\mathcal{U}$ and divided
    differences; monotone flux $\hat f(a,b)$, Roe speed, local LF speed,
    eigenvectors $\ell^{(p)}, r^{(p)}$; Shu–Osher RK coefficients
    $a_{ik}, b_{ik}$ and $\tilde{\mathcal{L}}$; minmod, median,
    $\delta^2$, $\kappa$, MP values $u^{\mathrm{or}}, u^{\mathrm{MD}},
    u^{\mathrm{LC}}, u^{\min}, u^{\max}$, $\mathcal{D}^{\mathrm{M4}}$; PPM
    $\Delta u_i, u_{6,i}, \phi_i$. Wording of $\mathcal{H}$ corrected (it
    is the function whose sliding average is $f$, not a primitive).
  * **Contradictions**: opened on
    [monotonicity-preserving limiting](/methods/monotonicity-preserving-limiter.md)
    (Suresh–Huynh accuracy claim vs Balsara–Shu's $\sin^4$ results).
    Jiang–Shu's critical-point claim (also asserted by Balsara–Shu for
    $r = 4$–$7$) recorded on
    [accuracy at critical points](/properties/accuracy-at-critical-points.md)
    with a compiler reading.
  * **Versions read**: shu-1988 as ICASE Report 87-33; jiang-1996 as the
    40-page preprint; shu-1998 as ICASE Report 97-65. Slugs follow the
    published versions (bundle law); the earlier plan to identify Shu's
    notes as the report is reversed for consistency with that rule.
    liu-1994 is an image-only scan, read visually.
  * **Bibliography**: reference lists extracted to fragments and merged
    with `tools/bib_merge.py` (10 fragments, 302 printed references;
    resolutions: 19 aliases, 27 silenced pairs, all distinct works
    verified by venue). Supplementary sweeps folded three duplicates (roe-1978 into
    roe-1981, cockburn-nd-b into cockburn-1998, harten-1985-b into
    harten-1987-b). 22 undated keys renamed to the citing date per the
    div-free-amr precedent. Record: 190 works, 10 ingested.

* **Bundle scaffolded** on user instruction: broad scope (all high-order
  capturing schemes), independent of every other bundle. Created the
  folder indexes, an empty `bibliography.bib`, and the
  [notation registry](/notation.md), seeded once (D12) with the
  reconstruction, weight, flux-splitting, time-stepping and positivity
  symbols the ingestion order needs first. Corpus archive:
  `~/papers/mosaic/high-order-capturing-schemes/` (62 PDFs).

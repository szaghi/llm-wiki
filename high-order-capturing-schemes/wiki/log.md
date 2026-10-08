# Directory Update Log

## 2026-10-08

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

# Directory Update Log

## 2026-10-08

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

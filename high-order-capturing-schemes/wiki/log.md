# Directory Update Log

## 2026-10-08

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

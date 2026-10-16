# Directory Update Log

## 2026-10-16

* **Ingestion: [Panici et al. (2023)](/sources/panici-2023.md)**, *J. Plasma Phys.*
  89:955890303 (bundle-fit copy, D17: the PDF copied into this bundle's archive and
  read for this bundle's subject only). Read in full; extracted: the Zernike basis
  (§3.2, eqs. 3.17–3.21), the regularity diagnostic (§5.1, Fig. 4), indexing and
  truncation (Table 2, App. C) and the expected and measured radial convergence
  (§5.2, Table 1, Figs. 7–8). The equilibrium physics is out of scope. The paper
  describes no collocation node set and no quadrature rule, so no quadrature page
  cites it. Printed slip recorded: eq. 3.19 has $+s$ where the radial Zernike
  polynomial has $-s$. No `Contradictions` entry opened: no existing page makes a
  claim about the same objects.
  * **Notation registry extended** ([notation](/notation.md), section 8): $R_n^m$,
    $Z_n^m$, $f_m$, $b_{m,j}$, $\zeta$, $\mathcal F_k$, $c_{nm}$, $c_{nmk}$, $L$, $M$, $K$;
    disc coordinates $(r,\phi)$; the $P_n^{(\alpha,\beta)}$ note updated.
  * **Definitions (1 created):** [Zernike polynomials and the Fourier–Zernike basis](/definitions/zernike-polynomials.md)
    (granularity rule 1: the basis whose axis regularity and radial convergence the
    paper tests). Its Jacobi relation and orthogonality are compiler-supplied,
    hypothesis-grade, checked symbolically for $n\le8$.
  * **Definitions (1 updated):** [orthogonal polynomials](/definitions/orthogonal-polynomials.md)
    (pointer to the Zernike polynomials; the first stated convergence rate of an
    orthogonal expansion).
  * **Bibliography:** 35 → 89 entries: the ingested paper and its 53 references,
    none shared with the two founding books; four DOIs verified on Crossref
    (Genberg 2002, Lewis & Bellan 1990, Sakai & Redekopp 2009, Zernike & Stratton
    1934). `bib_merge.py --dupes`: 0 groups.

## 2026-10-14

* **Scaffolding and founding ingestion: [Riley et al. (2006)](/sources/riley-2006.md)
  and [Arfken et al. (2013)](/sources/arfken-2013.md)**, both scoped reads (D21).
  Riley: preface, contents, Ch. 18 (with exercises) and §27.4; Arfken: front matter,
  §12.1, Chs. 14–15, §§18.1, 18.3, 18.4, and the Additional Readings of Chs. 12, 14,
  15, 18. Riley was read and drafted first, then Arfken merged per the ingestion
  protocol: agreements gained a second citation, extensions were integrated, and
  differences of convention were recorded as qualifications on the pages and in
  both notation maps (Condon–Shortley phase of $P_\ell^m$; the two $T_n$ generating
  functions; $n_\ell$ vs $y_n$; $L_n^m$ vs $L_n^k$; Riley's $k_n$ as a norm). No
  incompatible claim about the same object was found, so no `Contradictions` entry
  was opened. A printed slip, Riley's $H_3=8x^2-12x$ (p. 625), is recorded on the
  Hermite page and the Source page.
  * **Notation registry seeded** ([notation](/notation.md), sections 1–7): variables
    and indices; orthogonality ($\omega$, $h_n$, $k_n$); classical families with
    Jacobi $P_n^{(\alpha,\beta)}$ and $\mathit{He}_n$ reserved; sphere ($P_\ell^m$ with
    the Condon–Shortley phase, $Y_\ell^m$); Bessel ($\alpha_{\nu,k}$ for zeros, $y_\ell$
    not $n_\ell$); quadrature and bases ($\mathcal Q_n$, $x_j$, $w_j$, $\ell_j(x)$,
    reserved $\mathcal V$ and $\Lambda_n$); derived and physical symbols.
  * **Definitions (9):** [orthogonal polynomials](/definitions/orthogonal-polynomials.md),
    [Legendre](/definitions/legendre-polynomials.md),
    [associated Legendre](/definitions/associated-legendre-functions.md),
    [spherical harmonics](/definitions/spherical-harmonics.md),
    [Chebyshev](/definitions/chebyshev-polynomials.md),
    [Hermite](/definitions/hermite-polynomials.md),
    [Laguerre](/definitions/laguerre-polynomials.md),
    [Bessel](/definitions/bessel-functions.md),
    [spherical Bessel](/definitions/spherical-bessel-functions.md).
  * **Results (6):** [Rodrigues formula](/results/rodrigues-formula.md),
    [generating functions](/results/generating-functions.md),
    [three-term recurrences](/results/three-term-recurrences.md),
    [addition theorem](/results/spherical-harmonic-addition-theorem.md) (Riley only;
    Arfken defers it to Ch. 16, unread),
    [inverse-distance expansion](/results/legendre-expansion-of-inverse-distance.md),
    [Fourier–Bessel series](/results/fourier-bessel-series.md).
  * **Methods (4):** [Gaussian quadrature](/methods/gaussian-quadrature.md),
    [Gauss–Legendre](/methods/gauss-legendre-quadrature.md),
    [Gauss–Chebyshev](/methods/gauss-chebyshev-quadrature.md),
    [trapezium and Simpson rules](/methods/trapezium-and-simpson-rules.md), all from
    Riley alone (Arfken does not treat quadrature in the sections read).
  * **Bibliography:** 35 entries — the 2 ingested books and 33 cited works: Riley's
    3 in-text citations, Arfken's Additional Readings (36 entries, 29 distinct works)
    and 2 footnoted works with DOIs verified on Crossref (Beattie 1958, Weber 2007).
    Abramowitz–Stegun is shared by both books (`abramowitz-1964`).

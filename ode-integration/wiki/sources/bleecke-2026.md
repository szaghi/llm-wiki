---
type: Source
title: "Bleecke & Ranocha (2026) — Relaxation Runge-Kutta Methods with First-Same-as-Last Structure"
description: "Technical note removing the extra right-hand-side evaluation per step that relaxation costs with FSAL embedded pairs: FSAL-R interpolates the relaxed first stage, R-FSAL relaxes before the error estimate; both keep the local orders and match the naive scheme's accuracy at baseline cost on the BBM equation."
resource: "doi:10.1007/s10915-025-03130-6"
source_kind: paper
authors: [Bleecke S., Ranocha H.]
year: 2026
venue: "J. Sci. Comput. 106:18"
local_file: "/home/stefano/papers/mosaic/ode-integration/2025_Crossref_Journal_of_Scientific_Computing_Bleecke_Relaxation_Runge-Kutta_Methods_with_First-Same-as-Last_Struc.pdf"
tags: [relaxation, embedded-pair, step-size-control, structure-preserving, explicit]
timestamp: 2026-10-19T20:00:00Z
---

# Summary

[Relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md) (RRK) methods
replace the baseline step $y_{n+1}$ by
$y^\gamma_{n+1}=y_n+\gamma_n(y_{n+1}-y_n)$. The scalar $\gamma_n$ makes an
invariant conserved, $\eta(y^\gamma_{n+1})=\eta(y_n)$, and the result is
assigned to $t_n+\gamma_nh_n$. Explicit methods are normally run with
[step-size control](/methods/step-size-control.md) and an FSAL
[embedded pair](/methods/embedded-runge-kutta-pair.md), whose last stage
$f(y_{n+1})$ is reused as the first stage of the next step. Relaxation breaks
this reuse, because the next first stage is $f(y^\gamma_{n+1})$. The "naive"
combination therefore costs one extra right-hand-side evaluation per step;
this is the structure of OrdinaryDiffEq.jl
([DifferentialEquations.jl](/software/differentialequations-jl.md)) and of
SUNDIALS.

The note removes the extra evaluation by exploiting the linear form of the
relaxed update:

- **FSAL-R** (relax after step-size control) approximates the next first stage
  by $f(y_n)+\gamma_n(f(y_{n+1})-f(y_n))$. Lemma 1 bounds the interpolation
  error by $\mathcal O(h_n^{p+1})$, and Theorem 1 shows that the main and
  embedded local errors keep the orders $p+1$ and $p$.
- **R-FSAL** (relax before step-size control) relaxes first, approximates the
  FSAL value by $f(y_n)+\gamma_n^{-1}(f(y^\gamma_{n+1})-f(y_n))$, and compares
  the relaxed solution with a relaxed embedded solution at $t_n+\gamma_nh_n$
  (Lemma 2, Theorem 2).

Both proofs are short Taylor arguments built on $\gamma_n=1+\mathcal O(h_n^{p-1})$.
The only test is the [Benjamin–Bona–Mahony equation](/benchmarks/benjamin-bona-mahony-equation.md)
(traveling wave, Fourier collocation that conserves a quadratic invariant),
with the BS3 and DP5 pairs in four variants. Work-precision diagrams show both
new variants reaching the naive method's accuracy at about the baseline's
cost, "roughly 25%" more accurate than the baseline. For conservative problems
neither variant is clearly superior. FSAL-R is recommended for general-purpose
libraries because it keeps their structure; R-FSAL is preferred for
dissipative problems, where the entropy estimates relaxation needs cannot be
used directly with FSAL-R.

# Version read

The file is the version of record (Springer typeset, Open Access CC BY 4.0,
article type "Technical note"), 7 pages, with the DOI printed on page 1.
Received 20 Aug 2025, accepted 4 Nov 2025, online 4 Dec 2025; the issue year
is 2026, which gives the slug. Title, authors and venue match Crossref. The
note is the short journal version of the authors' technical report
arXiv:2311.14050 (its ref. [14]), a distinct document not read here.

# Key claims

Notation: $y_n$ the current (relaxed) solution, $y_{n+1}$ the baseline
update, $y^\gamma_{n+1}=y_n+\gamma_n(y_{n+1}-y_n)$, $\hat y_{n+1}$ the
embedded solution with FSAL weight $\hat b_{s+1}$, $p$ the order of the main
method.

1. Combining relaxation with an FSAL pair naively needs one extra right-hand-side evaluation per step, because $f(y^\gamma_{n+1})$ must be computed instead of reusing $f(y_{n+1})$ (§1, after Eq. 7). **Derived**
2. The naive combination follows OrdinaryDiffEq.jl and SUNDIALS: stages (4), main solution (5), embedded solution (6) with $\hat b_{s+1}f(y_{n+1})$, PID control, and relaxation only after acceptance. Relaxation is available in recent ARKODE versions (§1, Eqs. 4–7, footnote 1). **Stated**
3. Under "some technical assumptions" the relaxation equation $\eta(y^\gamma_{n+1})=\eta(y_n)$ has a unique solution $\gamma_n=1+\mathcal O(h_n^{p-1})$, and the RRK method has order at least $p$ and preserves $\eta$ (§1, Eq. 3). **Stated** (from earlier work)
4. Lemma 1: for $g\in C^2$, $g(y^\gamma_{n+1})=g(y_n)+\gamma_n(g(y_{n+1})-g(y_n))+\mathcal O(h_n^{p+1})$ (§2.1, Eq. 9, proof Eqs. 10–13). **Proved**
5. Theorem 1 (FSAL-R): with $f(y_n)+\gamma_n(f(y_{n+1})-f(y_n))$ as the first stage, $y(t_{n+1})-y_{n+1}=\mathcal O(h_n^{p+1})$ and $y(t_{n+1})-\hat y_{n+1}=\mathcal O(h_n^{p})$. The first-stage error is $\mathcal O(h_{n-1}^{p+1})$ and is multiplied by $h_n$ (§2.1, Eq. 14). **Proved**
6. FSAL-R keeps the structure of existing libraries, relaxes only accepted steps, and obtains the first stage as a combination of values already computed, saving one evaluation per step (§2.1). **Derived**
7. FSAL-R can have trouble approximating the first stage for dissipative problems, because the entropy estimates relaxation then needs cannot be used directly (§2.1, §4). **Stated**
8. R-FSAL relaxes before the error estimate and approximates $f(y_{n+1})$ by $f(y_n)+\gamma_n^{-1}(f(y^\gamma_{n+1})-f(y_n))$ (§2.2, Eq. 15). **Derived**
9. Lemma 2: for $g\in C^2$, $g(y_{n+1})=g(y_n)+\gamma_n^{-1}(g(y^\gamma_{n+1})-g(y_n))+\mathcal O(h_n^{p+1})$, by rearranging Lemma 1 with $\gamma_n=1+\mathcal O(h_n^{p-1})$ (§2.2, Eq. 16). **Proved**
10. In R-FSAL the error estimate compares $y^\gamma_{n+1}$ with the relaxed embedded solution $\hat y^\gamma_{n+1}=y_n+\gamma_nh_n\big(\sum_i\hat b_if(Y_i)+\hat b_{s+1}[f(y_n)+\gamma_n^{-1}(f(y^\gamma_{n+1})-f(y_n))]\big)$, both read at $t_n+\gamma_nh_n$ (§2.2, Eq. 17). **Derived**
11. Theorem 2 (R-FSAL): $y(t_n+\gamma_nh_n)-\hat y^\gamma_{n+1}=\mathcal O(h_n^{p})$ (§2.2, Eq. 18); the proof is "similar to Theorem 1". **Proved** (sketched)
12. The implementation is in Julia, checked against OrdinaryDiffEq.jl; $\gamma_n$ is computed with the Alefeld–Potra–Shi bracketing Algorithm 748 in Roots.jl; code is in a reproducibility repository (§3). **Stated**
13. Test: BBM equation with periodic boundaries, a traveling-wave solution, and a Fourier collocation semi-discretization conserving a discrete quadratic invariant (§3, Eqs. 19–22). **Stated**
14. On BBM the naive method is more accurate than the baseline at a given tolerance but uses more evaluations (§3, Fig. 1). **Shown**
15. FSAL-R and R-FSAL reach the naive method's accuracy "without increasing the number of RHS evaluations visibly", about 25% more accurate than the baseline at about equal work, for BS3 and DP5 (§3, Fig. 1, §4). Final time and tolerances are not printed, and "25%" is not defined as an error or a work ratio. **Shown**
16. For entropy-conservative problems no clear evidence favors one variant (§4). **Shown** (one test)
17. FSAL-R "appears to be preferable" for general-purpose implementations; R-FSAL "can be advantageous" for dissipative problems (§4). **Stated**
18. Step-size-control stability and a broader set of problems are deferred to the technical report (§3). **Stated**

# Printed slips

- Eqs. (1)–(2), p. 1: the ODE is autonomous, $u'(t)=f(u(t))$, but the invariant condition is printed "$\forall t,u:\ \eta'(u)f(t,u)=0$".
- p. 2 and Eq. (11): the relaxed solution and the relaxation equation are written with base point $u^n$, while Eq. (7) uses $u^n_\gamma$ (notational, not mathematical).
- p. 2: "we follow take an approach that is common in software packages".
- Theorem 1 proof, p. 3: "the difference between the approximated and the exact first stage is of order $\Delta t_{n-1}^{p+1}\Delta t_n$" describes the scaled contribution, not the stage difference itself.
- Eq. (21), p. 5: $x_{\min}=0$, $x_{\max}=2$ with $c=1.2$ gives $K\approx0.204$, a solitary wave of width $\sim5$ on a periodic domain of length 2. A misprinted domain is suspected; it is not verifiable from the note.
- Front matter: received and revised dates are both "20 August 2025".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $u'=f(u)$ | $y$, $y'=f(y)$ | autonomous |
| $\Delta t_n$ | $h_n$ | |
| $t^n$, $t^{n+1}=t^n+\Delta t_n$ | $t_n$, $t_{n+1}$ | |
| $u^n_\gamma$ | $y_n$ | current (relaxed) solution, base point of the stages |
| $u^{n+1}$ | $y_{n+1}$ | baseline (unrelaxed) update |
| $u^{n+1}_\gamma$ | $y^\gamma_{n+1}$ | relaxed solution |
| $t^{n+1}_\gamma=t^n+\gamma\Delta t_n$ | $t_n+\gamma_nh_n$ | relaxed time |
| $\gamma$ | $\gamma_n$ | relaxation parameter |
| $\eta$, $\eta'(u)$ | $\eta$, $\eta'(y)$ | invariant ("entropy") |
| $y^i$ | $Y_i$ | stage values, superscript index in the source |
| $\widehat u^{n+1}$, $\widehat b_i$, $\widehat b_{s+1}$ | $\hat y_{n+1}$, $\hat b_i$, $\hat b_{s+1}$ | embedded solution and weights; $s+1$ is the FSAL stage |
| $\widehat u^{n+1}_\gamma$ | $\hat y^\gamma_{n+1}$ | relaxed embedded solution (R-FSAL) |
| $p$ | $p$ | order of the main method; the embedded method has order $p-1$ |
| $g$ | same (page-local) | generic $C^2$ function of Lemmas 1–2 |
| $A$, $K$, $c$ (BBM) | same (page-local) | **collision**: wave amplitude, wavenumber and speed, not the Butcher matrix and abscissae |
| $\mathrm I$ | $I$ | identity in $(\mathrm I-\partial_x^2)$ |

# Reference list

The note prints 24 references in numbered style ([1]–[24]), all with DOIs
except [17] (Roots.jl, GitHub URL only). The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` this slug. Ref. [14], the
authors' technical report (arXiv:2311.14050), prints no year; it is keyed by
the arXiv year 2023 (`bleecke-2023`), so it is not mistaken for this
ingested source, and the reproducibility repository [19] (2023, GitHub and
Zenodo DOI) takes the next suffix (`bleecke-2023-b`). [5], [6] and [8]
print no volume or pages. Three items are ingested sources:
[6] [Al Jahdali, Dalcin & Parsani (2022)](/sources/aljahdali-2022.md),
[8] [Gardner et al. (2022)](/sources/gardner-2022.md) and
[10] [Reynolds et al. (2023)](/sources/reynolds-2023.md). No printed
duplicates.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [ARKODE](/software/arkode.md)
* [Benjamin–Bona–Mahony equation](/benchmarks/benjamin-bona-mahony-equation.md)
* [DifferentialEquations.jl](/software/differentialequations-jl.md)
* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [Relaxation Runge–Kutta methods](/methods/relaxation-runge-kutta.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)

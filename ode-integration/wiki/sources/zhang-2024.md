---
type: Source
title: "Zhang (2024) — An explicit 16-stage Runge–Kutta method of order 10 discovered by numerical search"
description: "Reports an explicit 16-stage Runge–Kutta method that satisfies all 1205 order-10 conditions to more than 3000 digits, found by BFGS minimization of the squared order-condition residuals without simplifying assumptions, conjecturally lowering the known stage count for explicit order 10 from 17 to 16."
resource: "doi:10.1007/s11075-024-01783-2"
source_kind: paper
authors: [Zhang D.K.]
year: 2024
venue: "Numer. Algorithms 96:1243-1267"
local_file: "/home/stefano/papers/mosaic/ode-integration/2024_Crossref_Numerical_Algorithms_Zhang_An_explicit_16-stage_RungeKutta_method_of_order_10_discovere.pdf"
tags: [runge-kutta, explicit, order-conditions, b-series, software]
timestamp: 2026-10-19T00:00:00Z
---

# Summary

The paper reports an explicit [Runge–Kutta method](/definitions/runge-kutta-method.md)
with $s=16$ stages that satisfies the Butcher
[order conditions](/results/runge-kutta-order-conditions.md) to order
$p=10$ numerically: the coefficients posted online to more than 3000
digits make the sum of squared residuals smaller than $10^{-6000}$. The
best published explicit order-10 methods, Hairer (1978) and Feagin, use 17
stages, so the method conjecturally lowers the known stage count from 17 to
16. The minimum stage count for explicit order $p>8$ is unknown; this is an
upper bound, not a barrier, and no proof of order is given.

No simplifying assumptions are imposed. All 136 free parameters (strictly
lower-triangular $A$ and $b$, with $c=A\mathbf 1$) enter the full system of
1205 conditions $\Phi(\tau)=1/\gamma(\tau)$ over the rooted trees with at most
10 vertices (the trees of [B-series](/definitions/b-series.md) theory). The
search minimizes the sum of squared residuals by BFGS from random starts.
Four ingredients make it feasible, all in the author's Julia package
RungeKuttaToolKit: amortized-constant-time tree enumeration (Beyer–Hedetniemi
level sequences), "instruction tables" that compute all elementary weights
in one pass reusing shared subtrees, bespoke reverse-mode automatic
differentiation, and a "Hessian reset" heuristic for BFGS combined with
adaptive extended precision (the author's MultiFloats library). Timings
against Mathematica, NodePy, MPFR and Arb show one to two orders of
magnitude gains; the tree enumeration matches RootedTrees.jl (see
[BSeries.jl and RootedTrees.jl](/software/bseries-jl.md)).

After several weeks of 64-bit search (8000 candidates) and refinement of
the 8 best at higher precision, one point reached a residual below
$10^{-200}$; it is printed to 120 digits. Certification tools do not apply:
Gröbner bases and cylindrical algebraic decomposition are doubly
exponential, and Smale's α-theory needs isolated roots of square systems,
whereas the solutions are expected to lie on positive-dimensional
varieties. PSLQ finds no low-height integer relations among the
coefficients. The paper has no ODE tests.

# Version read

Version of record: Numer. Algorithms 96:1243–1267, Springer typeset
"Original Paper", received 16 September 2023, accepted 12 February 2024,
published online 1 March 2024; 25 pages, the appendix Table 2
(pp. 1260–1265) printed rotated. Title, author and journal agree with
Crossref; no identity problem. The paper expands the author's 2019
undergraduate thesis (ref. [12], arXiv:1911.00318), which is cited as a
separate work. The archive also holds this paper under a second, duplicate
filename (a former "Maurya 2021" download error), since overwritten by the
correct Maurya paper; the file named in `local_file` is the one read.

# Key claims

Registry notation: $s$ stages, $p$ order, $(A,b,c)$ the tableau with
$c=A\mathbf 1$, $\tau$ a rooted tree, $\bullet$ the one-vertex tree,
$\gamma(\tau)$, $\sigma(\tau)$ density and symmetry, $\Phi(\tau)$ the
elementary weight. Page-local: $T_{\le p}=\{\tau\in T:\lvert\tau\rvert\le p\}$
(the source's $T_p$), $\Phi_\tau(A)\in\mathbb R^s$ the weight vector with
$\Phi(\tau)=b^\top\Phi_\tau(A)$, and $R_{p,s}$ the residual objective.

1. An explicit 16-stage method satisfies the order-10 conditions
   numerically, conjecturally improving the best known explicit order-10
   stage count from 17 to 16 (Abstract, §1, §5). **Shown** (numerical
   residual, no proof)
2. The previous best explicit order-10 constructions, Hairer [7] (1978) and
   Feagin [8], use 17 stages; this is "the first improvement on this bound
   in over 40 years" (§1). **Stated**
3. The minimum stage count of an explicit method of any order $p>8$ is
   unknown; orders 1–5 are "straightforward", 6–8 "difficult, though
   tractable" (§1). **Stated**
4. For $s=16$ there are $s(s+1)/2=136$ free parameters, and order 10
   imposes $\lvert T_{\le10}\rvert=1205$ polynomial equations, a heavily
   overdetermined system (§2). **Stated** (reader-checked:
   $1205=1+1+2+4+9+20+48+115+286+719$)
5. Order $p$ holds iff $b^\top\Phi_\tau(A)=1/\gamma(\tau)$ for all
   $\tau\in T_{\le p}$, with $c=A\mathbf 1$ assumed "without loss of
   generality" (Proposition 1, attributed to Butcher [13], §2). **Stated**
6. Unlike Hairer's and Feagin's constructions, no simplifying assumptions
   are imposed; the search works on the full Butcher system "avoiding any
   potential loss of generality" (§1). **Stated**
7. RungeKuttaToolKit enumerates $T_{\le p}$ in $O(\lvert T_{\le p}\rvert)$
   time and is 16.3×–170.4× faster than Mathematica and NodePy for
   $p=1,\dots,15$; Butcher's Algorithm 3 is similar at low $p$ and up to
   2.9× slower at high $p$; NodePy stops at 10 vertices (§3.1, Fig. 1).
   **Shown**
8. Evaluating $R_{p,s}$ with instruction tables (Algorithm 1), $p=1..12$,
   $s=16$: on average 47.7× faster than NodePy, 33.4× faster than
   interpreted and 4.5× faster than compiled Mathematica (§3.2, Fig. 2).
   **Shown**
9. Reverse-mode differentiation of $R_{p,s}$ is on average 76.4× faster
   than forward mode and only 25.9% slower than evaluating $R_{p,s}$
   (§3.3, Fig. 3). **Shown**
10. Levenberg–Marquardt needs the Jacobian of all elementary weights, which
    "can only be effectively computed using forward-mode" differentiation,
    and Newton needs the Hessian; both are rejected for gradient-only
    quasi-Newton methods (Remark 1, §3.3). **Stated** (a cost argument,
    not a theorem)
11. From the same random start in $[0,1]^{136}$, gradient descent fails to
    decrease $R_{10,16}$ significantly, plain BFGS stalls near $0.1$, and
    BFGS with Hessian reset reaches about $10^{-6}$ within 30,000
    iterations (§4.1, Fig. 4). **Shown** (one trajectory, called typical)
12. Hessian reset: each BFGS iteration runs line searches along the raw
    gradient and along the quasi-Newton direction; if the raw one decreases
    the objective more, the inverse-Hessian approximation is reset to the
    identity (§4.1). **Stated** (algorithm definition)
13. In 64-bit arithmetic the number of correct bits of $\nabla R_{p,s}$
    falls from 53 to about 10 along a typical trajectory, at times below 0,
    when the computed gradient is no longer a descent direction (§4.2,
    Fig. 5). **Shown**
14. MultiFloats is on average 3.4× faster than MPFR at evaluating
    $R_{10,16}$ at 128–256 bits, MPFR being fastest at high precision
    (Fig. 6); for $\nabla R_{10,16}$ MultiFloats beats Arb and MPFR at all
    precisions from 64 to 512 bits (Fig. 7) (§4.2). **Shown**
15. Search protocol: random starts, 64-bit BFGS with reset until no descent
    direction remains, points with Euclidean norm above 1000 rejected;
    several weeks gave 8000 candidates (footnote 3: misreported as 800 in
    the thesis); the 8 best ($R_{10,16}<10^{-14}$ in 128-bit) were refined
    at 128–256 bits, and after several more weeks one reached
    $R_{10,16}<10^{-200}$ (§5). **Shown**
16. The coefficients are printed to 120 digits (Table 2), every digit
    "confirmed to be correct" in that changing the last one increases
    $R_{10,16}$; a 3000+-digit version gives $R_{10,16}<10^{-6000}$ (§5).
    **Shown**
17. Preliminary evidence places the method on a positive-dimensional
    solution manifold rather than at an isolated root; embedded lower-order
    methods are left for future work (Remark 6). **Stated** (preliminary)
18. The author holds it "inconceivable" that the coefficients are not near
    a genuine root, but has no formal proof (§5.1). **Stated**
19. PSLQ at 3000 digits finds no nonzero coefficient that is a root of a
    univariate integer polynomial with coefficients bounded by $10!$, and no
    such bivariate relation between pairs; algebraic coefficients are
    "extremely unlikely" (§5.1). **Shown** (negative search result)
20. Many high-order Runge–Kutta methods are known only approximately
    [8, 25, 26]; this blocks theory, not practice (§5.1). **Stated**
21. Khashin [25] found a 13-stage explicit order-9 method by numerical
    search with "filtrated simplifying assumptions" and finite-difference
    Levenberg–Marquardt; the author infers his tools are "roughly two to
    three orders of magnitude faster" and calls Khashin's the only other
    numerically conjectured stage-count improvement (§6). **Stated** (speed
    inferred, not measured)
22. Gröbner bases and CAD are at least doubly exponential; verifying even
    the $p=s=5$ explicit barrier mechanically is "completely out of reach"
    (§6). **Stated**
23. Smale's α-theory certifies only isolated solutions of square systems;
    the Butcher equations are overdetermined with positive-dimensional
    solution sets, so it does not apply (§6). **Stated**
24. Minimizing the $\sigma(\tau)^{-2}$-weighted residual $E_{p,s}$ instead of
    $R_{p,s}$ makes no significant difference, and $R_{p,s}$ is marginally
    cheaper (Remark 2). **Stated** (experiments not shown)

*(Compiler check by the reader, not in the source.)* Parsing the 136
printed coefficients at 130 digits and enumerating the 1205 trees gives
$R_{10,16}\approx3.6\times10^{-236}$ and a maximum residual
$\approx6.9\times10^{-119}$, consistent with 120-digit truncation. The
abscissae $c=A\mathbf 1$ show emergent structure that the paper does not
mention: $c_2=c_4$; $c_3=c_{10}=c_{11}=c_{14}=c_{15}$ to all digits;
$c_{16}=1$; 11 distinct abscissae; and $b_2=b_4=b_5=0$. "No simplifying
assumptions" describes the search, not the result.

# Printed slips

- Ref. [16]: DOI printed "DOIurlhttps://doi.org/10.1137/0209055" (LaTeX
  macro residue).
- Ref. [21]: DOI printed "https://doi.org/10.1145/35733842111.11680",
  apparently a DOI run together with an arXiv identifier (2111.11680); not
  used as a DOI.
- Ref. [20]: author printed "Ranocha H (2019) contributors:" (garbled
  "Ranocha H and contributors").
- Ref. [23]: URL printed ".../dzhang314/MultiFloat"; the package is
  MultiFloats.jl.
- Ref. [9]: the printed DOI 10.1007/978-3-540-78862-1_2 is a chapter DOI of
  Hairer–Nørsett–Wanner I, not the book's.
- Ref. [15] (Ruskey & Hu, binary trees) is cited for the level-sequence
  representation of rooted trees, usually attributed to Beyer–Hedetniemi
  [16]; possibly a mis-citation (not verified).
- Remark 2 calls the $\sigma^{-2}$-weighted sum over all
  $\lvert\tau\rvert\le p$ the norm of the "principal error coefficients",
  a term usually reserved for the trees of order $p+1$.
- Self-correction in the source: footnote 3 corrects the thesis's "800"
  candidates to 8000.

# Notation map

| Zhang (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $s$, $p$ | $s$, $p$ | agrees |
| $(A,b)$, $A_{i,j}$, $b_i$ | $A$, $b$ | agrees; $c$ never written, $c=A\mathbf 1$ |
| $\mathbf 1$ | $\mathbf 1$ | agrees |
| $t$, $t_i$ | $\tau$ | rooted tree |
| **$\tau$** | $\bullet$ | **collision with the registry's generic tree $\tau$**: the source's trivial one-vertex tree |
| **$T_p$** | $T_{\le p}$ (page-local) | trees with **at most** $p$ vertices, $\lvert T_{\le10}\rvert=1205$ |
| $[t]$, $t_1\#t_2$ | — | extension (graft onto a new root) and rooted sum (merge roots) |
| $\gamma(t)$, $\sigma(t)$ | $\gamma(\tau)$, $\sigma(\tau)$ | agrees |
| $\Phi_t(A)\in\mathbb R^s$ | $\Phi_\tau(A)$ (page-local) | weight vector; elementary weight $\Phi(\tau)=b^\top\Phi_\tau(A)$ |
| $b\cdot\Phi_t(A)$ | $\Phi(\tau)$ | elementary weight |
| $\odot$ | — | componentwise product |
| $R_{p,s}$, $E_{p,s}$ | — | unweighted and $\sigma^{-2}$-weighted squared residual sums |
| **$I$** | — | **collision with the identity matrix**: instruction table |
| $y\in\mathbb R^n$ | $y\in\mathbb R^d$ | dimension |

# Reference list

The paper prints 29 references, numbered [1]–[29], mixing two Springer
styles. All 29 are merged complete into the [bibliography](/bibliography.md)
with `citedby` zhang-2024. Same-author same-year items take suffixes in
printed order: `zhang-2019` (RungeKuttaToolKit software, [11]),
`zhang-2019-b` (undergraduate thesis, arXiv:1911.00318, [12]) and
`zhang-2019-c` (MultiFloats.jl, [23]). Ref. [21] has a garbled DOI, kept in
a note only. Refs. [19] and [27] are book chapters with no book title
printed; [25] prints no pages; [8], [11], [17], [20] and [23] are web or
software items. No printed duplicates.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [B-series, composition and substitution laws](/definitions/b-series.md)
* [BSeries.jl and RootedTrees.jl](/software/bseries-jl.md)
* [DifferentialEquations.jl](/software/differentialequations-jl.md)
* [Runge–Kutta method](/definitions/runge-kutta-method.md)
* [Runge–Kutta order conditions and simplifying assumptions](/results/runge-kutta-order-conditions.md)

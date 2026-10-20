---
type: Source
title: "Ketcheson & Ranocha (2023) — Computing with B-series"
description: "Presents the Julia package BSeries.jl, built on RootedTrees.jl, for symbolic computation with truncated B-series: composition and substitution laws, order conditions, effective order, modified equations and modifying integrators, with worked examples and a 70-fold speed-up over pybs."
resource: "doi:10.1145/3573384"
source_kind: paper
authors: [Ketcheson D.I., Ranocha H.]
year: 2023
venue: "ACM Trans. Math. Softw. 49:1-23"
local_file: "/home/stefano/papers/mosaic/ode-integration/2023_Crossref_ACM_Transactions_on_Mathematical_Software_Ketcheson_Computing_with_B-series.pdf"
tags: [order-conditions, geometric-integration, runge-kutta, software, structure-preserving]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper presents [BSeries.jl](/software/bseries-jl.md), a Julia package for computing with and manipulating [B-series](/definitions/b-series.md) truncated at an arbitrary fixed order, built on the authors' RootedTrees.jl. It is part tutorial, part software paper, and contains no new theorems.

It recalls rooted trees (order $\lvert\tau\rvert$, symmetry $\sigma(\tau)$, density $\gamma(\tau)$, level sequences), elementary differentials $F(\tau)$ and the elementary weights $\Phi(\tau)$ of a [Runge–Kutta method](/definitions/runge-kutta-method.md). It also recalls the B-series $B(a,y)$, the [order conditions](/results/runge-kutta-order-conditions.md) $\Phi(\tau)=1/\gamma(\tau)$, the composition law (ordered subtrees) and the substitution law (partitions and skeletons).

The worked computations are:

- the B-series of the two-stage second-order explicit family and of the composition of two such methods, which stays of order 2;
- Butcher's effective-order-5 method ([processing and effective order](/methods/processing-and-effective-order.md));
- [modified equations and modifying integrators](/methods/backward-error-analysis.md) for explicit Euler on Lotka–Volterra;
- the explicit midpoint rule on a nonlinear oscillator, which it integrates with exact energy conservation at any step size;
- Störmer–Verlet on the Kepler problem as an additive Runge–Kutta method, whose modified equation has no odd powers of $h$, consistent with [symplecticity](/properties/symplecticity.md);
- the average-vector-field method.

The package also covers [Rosenbrock–Wanner](/methods/rosenbrock-wanner-method.md) B-series, but only as a listed feature without an example. The implementation stores trees as canonical level sequences, uses lazy iterators over splittings and partitions, skips zero skeleton coefficients, and offers three symbolic back ends. Summing the modified-equation coefficients of the explicit midpoint rule to order 9 takes about 53 ms against 3.7 s in pybs.

# Version read

arXiv:2111.11680v2 [math.NA], 15 Nov 2022, in the ACM TOMS author template: an accepted manuscript, not the typeset version of record. 23 pages, all read; tree glyphs and tableaux on pp. 3–7, 9–10 and 16–18 were checked visually. Page 1 prints the ACM reference line "2022. Computing with B-series. 1, 1 (November 2022), 23 pages" with the template placeholder DOI `10.1145/nnnnnnn.nnnnnnn`; the resource above is the Crossref DOI. Title and authors match Crossref. Numbering cited here is that of the arXiv v2.

# Key claims

Notation: $B(a,y)=a(\varnothing)y+\sum_\tau\frac{h^{\lvert\tau\rvert}}{\sigma(\tau)}a(\tau)F(\tau)(y)$; $e(\tau)=1/\gamma(\tau)$ the exact-flow coefficients; $\psi_h$ the numerical one-step map; $\tilde f$ the modified vector field; trees written by level sequence (see the notation map).

1. BSeries.jl computes B-series of Runge–Kutta, additive Runge–Kutta and Rosenbrock–Wanner methods, composition and substitution laws, modified equations and modifying integrators, for generic $f$ or a specific ODE, with symbolic coefficients, on series truncated at a fixed but arbitrary order. (§1) **Stated**
2. The only similar library known to the authors (computing B-series themselves, not only Runge–Kutta order conditions) is the Python code pybs; other tools use B-series only implicitly for order conditions. (§1) **Stated**
3. The test suite covers 99% of the code, with continuous integration, under the MIT license. (§1) **Stated**
4. For the explicit two-stage second-order family (17), $c=(0,\tfrac1{2\alpha})$, $a_{21}=\tfrac1{2\alpha}$, $b=(1-\alpha,\alpha)$, the solution map is $y_{n+1}=y_n+hF([1])+\tfrac12h^2F([1,2])+\tfrac1{8\alpha}h^3F([1,2,2])+\tfrac1{48\alpha^2}h^4F([1,2,2,2])+\tfrac1{384\alpha^3}h^5F([1,2,2,2,2])+O(h^6)$. (Eq. 18) **Derived** (computed by the package; the $\alpha$ coefficients were checked by hand by the compiler, not in the sources)
5. Order $p$ iff $\Phi(\tau)=e(\tau)=1/\gamma(\tau)$ for all $\lvert\tau\rvert\le p$. (§2.2, Eq. 20) **Stated**
6. Composing two methods of form (17) (same step, normalized) gives a series whose coefficient of the tall tree $[1,2,3]$ is $1/8$, independent of $\alpha_1,\alpha_2$ and different from the exact $1/6$; any such composition has order exactly two. (§2.3.1) **Derived** (computed)
7. Butcher's effective-order-5 method: the main five-stage method (24) has order 4, the starting and finishing methods (25) have order 3, and their composition has order 5. (§2.3.2, Eqs. 24–25) **Shown** (computed)
8. The original motivation for BSeries.jl was to automate backward error analysis of nonlinear ODE integrators, which is "less well-known" for nonlinear ODEs because it is much more tedious. (§2.4) **Stated**
9. The substitution law (26) lets $(b\star e)(\tau)=a(\tau)$ be solved recursively for the modified-equation coefficients $b$, because $(b\star e)(\tau)=b(\tau)+$ lower-order terms. (§2.4, Eq. 26) **Stated**
10. Modified equation of the family (17): $\tilde f=F([1])-\tfrac{h^2}6F([1,2,3])+h^2(-\tfrac16+\tfrac1{8\alpha})F([1,2,2])+\tfrac{h^3}8F([1,2,3,4])+h^3(\tfrac18-\tfrac1{16\alpha})F(\cdot)+h^3(\tfrac18-\tfrac1{8\alpha})F(\cdot)+h^3(\tfrac1{24}-\tfrac1{16\alpha}+\tfrac1{48\alpha^2})F([1,2,2,2])+O(h^4)$, the two unlabelled order-4 trees being printed as glyphs. (Eq. 27) **Derived** (computed)
11. Explicit Euler on Lotka–Volterra (28): the $O(h)$ modified equation (30)–(31) agrees with Hairer–Lubich–Wanner; higher-order modified equations (up to $O(h^5)$) are needed for larger $h$ or longer $T$ to match the Euler solution ($h=0.1,0.11,0.12$ to $T=10$; $h=0.1$ to $T=66.4$). (§2.4.2, Fig. 1) **Shown**
12. Modifying integrators for explicit Euler on Lotka–Volterra ($h=0.35$): order 1 still grows (much less than Euler), order 2 is dissipative, order 3 is indistinguishable from the exact solution and nearly periodic. (§2.5, Fig. 2) **Shown**
13. The explicit midpoint rule (32) on the nonlinear oscillator (33) has the exact closed form $y_n=\beta(\cos n\theta(h/\beta^2),\sin n\theta(h/\beta^2))$, $\theta(\mu)=\arccos\frac{1-\mu^2/4}{1+\mu^2/4}$, $\beta=\lVert y(0)\rVert$, and so conserves energy exactly for any step size. (§2.6, Eq. 35) **Derived**
14. "As far as we are aware, this behavior is unique among explicit discretizations of initial value ODEs." (§2.6) **Stated**
15. The modified equation for this pair is $\tilde f(y)=f(y)g(h/\lVert y\rVert^2)$ with $g(z)=1-\tfrac{z^2}{12}+\tfrac{z^4}{80}-\tfrac{z^6}{448}+\tfrac{z^8}{2304}+O(z^{10})$ (computed to order 8); a closed form attributed to Hairer is printed as (38). (Eqs. 36–38) **Derived** — the printed closed form is inconsistent with the series (printed slips).
16. The explicit midpoint rule is symmetric for this problem (its adjoint (39) reproduces (34)) but not for general ODEs; at order $h^5$, 16 of 20 modified-equation coefficients are nonzero, yet their sum with this problem's elementary differentials vanishes. (§2.6.1) **Derived**
17. Modifying integrator for this pair: $\hat f=f\,\hat g_4(h/\lVert y\rVert^2)$ with $\hat g_4(z)=1+z^2/12+z^4/20$ up to $h^4$; through $h^7$ (40) adds the non-Hamiltonian term $y\big(\frac{h^5}{48\lVert y\rVert^{12}}+\frac{31h^7}{640\lVert y\rVert^{16}}\big)$, with $\hat g_6=\hat g_4+\tfrac{127}{2016}z^6$; its truncations are not Hamiltonian from order $h^5$. (§2.6.2, Eq. 40) **Derived**
18. The order-8 modifying integrator is initially much more accurate than the energy-conserving explicit midpoint rule, but its error grows faster because energy is not conserved; for $h=0.6$ the midpoint rule wins at large times, for $h=0.3$ the modifying integrator stays better until both reach about 100% error. (§2.6.2, Fig. 3) **Shown**
19. Partitioned Runge–Kutta, Runge–Kutta–Nyström and additive Runge–Kutta methods are covered by generalized B-series on colored rooted trees (NB-series, P-series); additive Runge–Kutta is a superset of partitioned Runge–Kutta. (§3.1) **Stated**
20. Störmer–Verlet (45) is an additive Runge–Kutta method with two parts, coefficients $A^{[1]}=\begin{pmatrix}0&0\\1/2&1/2\end{pmatrix}$, $b^{[1]}=(1/2,1/2)$, $A^{[2]}=\begin{pmatrix}1/2&0\\1/2&0\end{pmatrix}$, $b^{[2]}=(1/2,1/2)$ (46); its modified equation through $h^7$ has no odd powers of $h$, consistent with symplecticity. (§3.1.2) **Shown** (computed)
21. The order-4 modifying integrator of Störmer–Verlet on Kepler has no third-order terms, but $q$ appears on the right-hand side of $\dot q_1$ (47), so the scheme is no longer explicit; "this does not appear to be an appealing approach." (§3.1.2, Eq. 47) **Derived**
22. The average-vector-field method (48) is a B-series method with coefficients $a([1])=1$, $a([\tau_1,\dots,\tau_n])=a(\tau_1)\cdots a(\tau_n)/(n+1)$; its modified equation to $h^4$ reproduces the formula of Celledoni et al. (2010, top of p. 679), showing energy preservation up to $h^4$ terms. (§3.2, Eqs. 49–50) **Shown** (computed)
23. Summing the modified-equation coefficients of the explicit midpoint rule (51) up to order nine takes about 53 ms with BSeries.jl and 3.7 s with pybs on an Intel Core i7-8700K (2017), about 70 times faster. (§4) **Shown**
24. Modifying-integrator coefficients of the explicit midpoint rule to order nine take about 23 ms against about 52 ms for the modified equation, because zero skeleton coefficients (many, for explicit Runge–Kutta) let the partition-forest loop be skipped. (§4.2) **Shown**
25. Symbolic back ends (Table 4; modifying-integrator B-series of the explicit midpoint rule on the oscillator to order 8, then substitution of the initial condition $(0,1)$): SymPy.jl $1.811\pm20.118\times10^{-3}$ s / $212.317\pm9.885$ ms; Symbolics.jl $710.232\pm21.727$ ms / $2.565\pm2.848\times10^{-3}$ s; SymEngine.jl $15.768\pm7.733$ ms / $3.353\pm0.271$ ms; SymEngine is "several orders of magnitude faster". (§4.3, Table 4) **Shown**
26. Julia "can be at least as fast as" Fortran, C or C++ code. (§4) **Stated**
27. Renormalization in quantum field theory relies on the same Hopf-algebra structure, so the package may be useful there. (§5) **Stated**
28. Listed future extensions: B-series for partitioned, multistep, multiderivative, exponential and Rosenbrock methods. (§5) **Stated** — Rosenbrock (ROW) methods already appear in the §1 feature list (internal inconsistency).

# Printed slips

- Eq. (38) against (37): printed "$g(z)=\frac{d}{dz}\arccos\left(\frac{1-z^2/4}{1+z^2/4}\right)=2\arctan(z/2)$". But $\arccos\frac{1-z^2/4}{1+z^2/4}=\theta(z)=2\arctan(z/2)$ itself, which tends to 0 as $z\to0$, whereas (37) has $g(0)=1$. The function matching (37) term by term is $g(z)=\theta(z)/z=\frac2z\arctan(z/2)$ *(compiler check)*; $\theta'(z)=1/(1+z^2/4)$ does not match either. The derivation before (38) differentiates in $h$, which gives $\theta'$, while the modified flow over time $h$ must rotate by $\theta$. The package output (37) appears correct.
- Eq. (29): explicit Euler printed "$y_{n+1}=y_n+f(y)$", missing $h$ and with argument $y$ for $y_n$.
- Algorithm 1: loops over "all binary sequences of length $m$" with $m\leftarrow\lvert\tau\rvert$, but a tree has $\lvert\tau\rvert-1$ edges (Def. 2.2 counts $2^{\lvert\tau\rvert-1}$ partitions); it also initializes `partitions ← []` but appends to `skeletons`.
- Def. 2.1: "used in the definition of the composition law (22)" — the subtree sum is (23).
- §4.2: "additional checks in the composition law: If the coefficient of the partition skeleton is zero … see (26)" — skeletons and (26) belong to the substitution law; also "modified integrator" for "modifying integrator".
- Def. 2.2 against Algorithms 2–3: the definition removes "the edges of $p$" to form the forest, while §4.2 marks kept edges 1 and removed edges 0; which edges belong to $p$ is ambiguous.
- §4: "which which could increase".
- §2.3.2 code: `series_b` and `series_c` are used but never defined; which tableau of (25) is starter and which finisher is implicit.
- Table 1 heads the weight column $\Phi_j(t)$ while trees are $\tau$ elsewhere (cosmetic).
- Kepler problem (43) printed as $\dot p=q/\lvert q\rvert^3$ (repulsive); the attractive problem has $-q/\lvert q\rvert^3$. Possibly a sign slip; flagged, not corrected.
- Page 1: template DOI placeholder.

# Notation map

| Ketcheson & Ranocha | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\dot y=f(y)$ | $y'=f(y)$ | autonomous throughout; $c_i=\sum_ja_{ij}$ assumed |
| $h$; figures "dt" | $h$ | |
| $A=(a_{ij})$, $b$, $c$, $s$, $Y_i$ | same | stage values; **$s$ also names an ordered subtree in (23)** |
| $T$, $T_k$, $\tau=[\tau_1,\dots,\tau_m]$, $\lvert\tau\rvert$ | same | Butcher bracket |
| $\sigma(\tau)$, $\gamma(\tau)$ | same | |
| $F_f(\tau)$, $F(\tau)$; $f^j_{kl}$ | $F(\tau)$ | Einstein summation in the source |
| $\Phi_j(\tau)$, $\Phi(\tau)$ | same | internal and full elementary weights |
| $B(u,hf,y)$ | $B(a,y)$ | same normalization $h^{\lvert\tau\rvert}/\sigma(\tau)$; $a(\varnothing)=1$ for maps, $0$ for vector fields |
| $e(\tau)=1/\gamma(\tau)$ | kept | exact-flow coefficients |
| $v\cdot u$, $B(u,hf,B(v,hf,y))=B(v\cdot u,hf,y)$ | $a\cdot b$, $B(b,B(a,y))=B(a\cdot b,y)$ | same convention: the left factor is applied first |
| $v\star u$ | $b\star a$ | substitution of $B(b,\cdot)$ into $B(a,\cdot)$ |
| $S(\tau)$, $s_\tau$, $\tau\setminus s$; $P(\tau)$, $p_\tau$, $\tau\setminus p$ | kept | ordered subtrees; partitions and skeletons |
| $b(\tau)$ (AVF coefficients, (49)–(50)) | $a(\tau)$ | coefficient map of a B-series method; $\bullet$ written $[1]$ |
| $\phi_h$ | $\psi_h$ | numerical one-step map |
| $f_h$ | $\tilde f$ | modified vector field |
| $\hat f_h$, $\hat g_4$, $\hat g_6$ | $\hat f$, kept | modifying-integrator field (not in the registry) |
| $g(z)$, $z=h/\lVert y\rVert^2$ | kept | **$g$ also denotes the Kepler force and the second additive part in the source** |
| $\alpha$ (family (17)) | kept | $b_2=\alpha$; **collides with the Shu–Osher $\alpha$ of the registry** |
| $\beta=\lVert y(0)\rVert$, $\theta(\mu)$ | kept | oscillator amplitude; rotation per step |
| $f^\nu$, $A^\nu$, $b^\nu$, $N$ | $f^{[\nu]}$, $A^{[\nu]}$, $b^{[\nu]}$ | additive parts and coefficients |
| $p,q$ | kept locally | Lotka–Volterra populations, Kepler momentum/position; **$p$ and $q$ are order and stage order in the registry** |

# Reference list

38 printed references, numbered [1]–[38] in the ACM style. The list is merged complete into the [bibliography](/bibliography.md) with `citedby` ketcheson-2023. Two Ketcheson 2021 items (BSeries.py [25]; the reproducibility repository [26]) take same-key suffixes in printed order. [10] and [21] print series volumes without the series name; [27] (NodePy) has no venue; [16] is a JuliaCon talk; [38] is a master's thesis. No unparseable item and no preprint/published duplicate pair.

# Pages created or updated

Chunk 1 (2026-10-19); updated in later chunks. This source is cited on:

* [B-series, composition and substitution laws](/definitions/b-series.md)
* [Backward error analysis, modified equations and modifying integrators](/methods/backward-error-analysis.md)
* [BSeries.jl and RootedTrees.jl](/software/bseries-jl.md)
* [DifferentialEquations.jl](/software/differentialequations-jl.md)
* [Kepler problem](/benchmarks/kepler-problem.md)
* [Operator splitting: Lie–Trotter, Strang and dimensional splitting](/methods/operator-splitting.md)
* [Processing and effective order](/methods/processing-and-effective-order.md)
* [Rosenbrock–Wanner (ROW) and W-methods](/methods/rosenbrock-wanner-method.md)
* [Runge–Kutta method](/definitions/runge-kutta-method.md)
* [Runge–Kutta order conditions and simplifying assumptions](/results/runge-kutta-order-conditions.md)
* [Symplecticity and quadratic-invariant preservation](/properties/symplecticity.md)

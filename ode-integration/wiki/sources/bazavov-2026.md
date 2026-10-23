---
type: Source
title: "Bazavov (2026) — 2N-storage Runge-Kutta methods: Order conditions, general properties and some analytic solutions"
description: "Characterizes Williamson 2N-storage explicit Runge–Kutta methods exactly by quadratic constraints on the Butcher coefficients, gives closed maps between the Butcher and 2N coefficients, corrects Williamson's 1980 special-case conversion formula, and derives the general third-order four- and five-stage families with new rational schemes."
resource: "doi:10.1007/s10543-026-01139-3"
source_kind: paper
authors: [Bazavov A.]
year: 2026
venue: "BIT Numer. Math. 66:38"
local_file: "/home/stefano/papers/mosaic/ode-integration/2026_Crossref_BIT_Numerical_Mathematics_Bazavov_2N-storage_Runge-Kutta_methods_Order_conditions_general_prop.pdf"
tags: [runge-kutta, explicit, low-storage, order-conditions, embedded-pair]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

The paper studies the structure of Williamson's 2N-storage explicit
Runge–Kutta methods, the two-register class of
[low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md):
a register $\Delta Y_i=A^{\mathrm W}_i\Delta Y_{i-1}+hf$ and the solution
register $Y_i=Y_{i-1}+B^{\mathrm W}_i\Delta Y_i$. The usual construction
substitutes the Butcher coefficients, expressed through
$A^{\mathrm W}_i,B^{\mathrm W}_i$, into the classical
[order conditions](/results/runge-kutta-order-conditions.md), which gives
high-degree polynomial systems. The author instead introduces an
intermediate "α-form" of an explicit
[Runge–Kutta method](/definitions/runge-kutta-method.md), in which each
stage is an increment of the previous stage, and shows that the 2N property
is equivalent to a chain of ratio equalities among its coefficients. In
Butcher form these become $(s-1)(s-2)/2$ independent constraints, quadratic
in $(A,b)$ whatever the order, matching the drop from $s(s+1)/2$ explicit
coefficients to $2s-1$ free 2N coefficients.

Consequences follow. Closed, non-recursive maps between
$(A^{\mathrm W},B^{\mathrm W})$ and $(A,b)$ expose an error in Williamson's
1980 conversion formula for the case $b_i=0$, $i>2$, shown by exact
counterexamples. In general all $a_{ij}$, $A^{\mathrm W}_i$ and
$B^{\mathrm W}_i$ are determined by $b$ and $c$, so $b,c$ can be taken as
the free parameters. The special case $A^{\mathrm W}_i=-1$ gives
$a_{ij}=b_j+(-1)^{i-j+1}b_i$. The complete third-order families with four
and five stages reduce to one quadratic equation for $b_2$. A grid search
yields new rational schemes, among them four-stage ones that are fourth
order on linear problems and a five-stage scheme whose fourth stage is a
second-order solution, giving a free
[embedded pair](/methods/embedded-runge-kutta-pair.md) 3(2). The six-stage
fourth-order scheme of Berland, Bogey and Bailly is recomputed to 42
digits. The motivation is the author's earlier evidence that 2N-storage
schemes are automatically commutator-free Lie-group integrators, proved
only for a three-stage third-order scheme.

# Version read

arXiv:2506.07359v1 [math.NA], 9 June 2025 (footer date 10 June 2025), a
33-page elsarticle preprint including Appendices A–E, not the BIT version
of record (article 38 of vol. 66). Title and author agree with Crossref;
the published text may differ, and some printed slips below may be
corrected there. The DOI is not printed in the file. Equation, table,
theorem and section numbers on this page are those of arXiv v1.

# Key claims

Registry notation: $h$ step, $y_n$ the solution, $Y_i$ stage values,
$(A,b,c)$ the Butcher tableau with $c=A\mathbf 1$, $s$ stages, $p$ order.
Page-local: $A^{\mathrm W}_i$, $B^{\mathrm W}_i$ the Williamson 2N
coefficients (the source's scalar $A_i$, $B_i$), $\Delta Y_i$ the second
register, $d_{ij}$ the α-form coefficients (the source's $\alpha_{ij}$,
with $d_{s+1,j}$ the source's $\beta_j$), $(s,p)$ a method label. The
source assumes $A^{\mathrm W}_i\ne0$ for $i\ge2$ throughout.

1. Williamson's A-form (Eqs. 7–9), $A^{\mathrm W}_1=0$, relates to the
   Butcher form by Eqs. (10)–(14); the special case (12),
   $A^{\mathrm W}_i=(a_{i+1,i-1}-c_i)/B^{\mathrm W}_i$ for $b_i=0$, holds
   only for $i=2$ and is wrong for $b_i=0$, $i>2$ (§2, §5.1). **Proved**
   (derivation and exact counterexamples, Tables 1–4)
2. Lemma 1: $\Delta Y_i=h\sum_{m=1}^{i-1}\big(\prod_{l=m+1}^{i-1}A^{\mathrm W}_l\big)k_m$
   with $k_m$ the stage derivatives (Eq. 33). **Proved**
3. Lemma 2: $d_{ij}=B^{\mathrm W}_{i-1}\prod_{k=j+1}^{i-1}A^{\mathrm W}_k$
   and $d_{s+1,i}=B^{\mathrm W}_s\prod_{k=i+1}^{s}A^{\mathrm W}_k$
   (Eqs. 39–40). **Proved**
4. All $B^{\mathrm W}_i\ne0$; with all $A^{\mathrm W}_i\ne0$ every $d_{ij}$
   is nonzero; $B^{\mathrm W}_i=a_{i+1,i}$ and $B^{\mathrm W}_s=b_s$.
   Almost all published 2N methods have $A^{\mathrm W}_i\ne0$, Ruuth (2006)
   being a rare exception (Remark 2). **Proved** / exception **Stated**
5. Theorem 1: a method is 2N-storage iff
   $\frac{d_{j+2,j}}{d_{j+2,j+1}}=\dots=\frac{d_{s,j}}{d_{s,j+1}}=\frac{d_{s+1,j}}{d_{s+1,j+1}}\;(=A^{\mathrm W}_{j+1})$,
   $j=1,\dots,s-2$ (Eq. 42). **Proved**
6. Of the $s(s-1)(s-2)/6$ relations in (42) only $(s-1)(s-2)/2$ are
   independent (§4). **Stated** (counting argument)
7. Theorem 2: in Butcher form the 2N constraints are
   $a_{ij}(b_{j-1}-a_{j,j-1})=(a_{i,j-1}-a_{j,j-1})b_j$, $i=3,\dots,s$,
   $j=2,\dots,i-1$ (Eq. 47, form II), or equivalently Eqs. (45)–(46)
   (form I); they are quadratic in $(A,b)$ independently of the order, and
   their number $(s-1)(s-2)/2=s(s+1)/2-(2s-1)$. **Proved** (count
   **Derived**)
8. The polynomial forms admit spurious zero solutions, so solutions must be
   checked against the ratios (42) (Remark 3); some $a_{ij}$, $b_i$ may
   vanish, e.g. $b_3=0$ in a four-stage method forces $b_2=a_{32}$
   (Remark 4). **Derived**
9. Theorem 3: $a_{ij}=\sum_{k=j+1}^{i}B^{\mathrm W}_{k-1}\prod_{l=j+1}^{k-1}A^{\mathrm W}_l$,
   $b_i=\sum_{k=i+1}^{s+1}B^{\mathrm W}_{k-1}\prod_{l=i+1}^{k-1}A^{\mathrm W}_l$
   (Eqs. 59–60); inversely
   $A^{\mathrm W}_i=\frac{a_{k,i-1}-a_{k-1,i-1}}{a_{ki}-a_{k-1,i}}$ for any
   $i<k\le s$, or $\frac{b_{i-1}-a_{s,i-1}}{b_i-a_{s,i}}$, and
   $B^{\mathrm W}_i=a_{i+1,i}$, $B^{\mathrm W}_s=b_s$ (Eqs. 61–63), with
   no special cases. Earlier such relations existed only for $s=5$
   (Carpenter–Kennedy) and $s=7$ (Allampalli et al.). **Proved** /
   history **Stated**
10. The correct special case is
    $A^{\mathrm W}_i=(a_{i+1,i-1}-a_{i,i-1})/B^{\mathrm W}_i$, $i\ne1$
    (Eq. 70), valid for all $b_i$; Williamson's has $c_i$ in place of
    $a_{i,i-1}$, which coincide only for $i=2$. **Proved**
11. Six reasons are given why the error went unnoticed since 1980, among
    them that the Butcher-to-2N conversion is almost never used and that
    $b_i=0$, $i\ge3$, must be imposed deliberately (§5.1). **Stated**
12. A (4,3) method with $b_3=0$ and a (5,3) method with $b_4=0$ (rational,
    Tables 1–2) round-trip exactly through Eqs. (62)–(63), whereas
    Williamson's (12) gives $A^{\mathrm W}_3=38/243$ instead of $130/81$,
    resp. $A^{\mathrm W}_4=-862/729$ instead of $-452/729$, and the
    reconstructed tableaux (Tables 3–4) are no longer third order.
    **Shown** (exact arithmetic; compiler re-verified, not in the sources, also on a third
    (5,3) scheme with $b_3=0$ from App. E)
13. Theorem 4: in the general case
    $a_{ij}=\frac{b_j}{\sum_{k=1}^{j}b_k-c_j}\big[c_i-c_j-\sum_{k=j+1}^{i-1}a_{ik}\big]$
    (Eq. 71); a non-recursive form is Eq. (80). **Proved** (Eq. 71) /
    **Stated** (Eq. 80, proof omitted)
14. Theorem 5: with $b_0=0$, $c_{s+1}=1$,
    $A^{\mathrm W}_i=\frac{b_{i-1}}{b_i}\frac{\sum_{k<i}b_k-c_i}{\sum_{k<i}b_k-c_{i-1}}$,
    $B^{\mathrm W}_i=\frac{b_i}{\sum_{k\le i}b_k-c_i}(c_{i+1}-c_i)$
    (Eqs. 81–82); the $2s-1$ free parameters may be taken as $b,c$.
    **Proved**
15. With $A^{\mathrm W}_i=-1$ for all $i>1$: $a_{ij}+a_{i,j+1}=b_j+b_{j+1}$
    (Eq. 87), $a_{ij}=b_j+(-1)^{i-j+1}b_i$ (Eq. 90) and
    $c_i=\sum_{j<i}b_j+\tfrac12(1+(-1)^i)b_i$ (Eq. 91), so $c_2=c_3$,
    $c_4=c_5$, … and $c_s=1$ for even $s$; (91) matches Bernardini–Pirozzoli
    in recursive form (§6.1). **Proved**
16. General (4,3) solution: with distinct free $c_2,c_3,c_4$, $b_1,b_3,b_4$
    are linear in $b_2$ (Eqs. 92–94) and the last third-order condition
    reduces to a quadratic in $b_2c_2$ (Eq. 95) (§7). **Derived** (the
    printed linear coefficient is wrong; see slips)
17. General (5,3) solution: with free $c_2,\dots,c_5,b_5$ a chain of
    intermediates (Eqs. 103–114) gives a cubic in $b_2$ whose leading
    coefficient vanishes identically, so again a quadratic, then
    $b_1,b_3,b_4$ (Eqs. 115–118) (§8). **Derived** (compiler check, not in the sources: verified exactly
    on Tables 7, 9, 10 and the corrected Table 8)
18. Conjecture: for any $s$, third-order 2N methods lead to a final
    equation of degree at most 3 for $b_2$, since $2s-1$ parameters face
    four conditions after (71) (§8). **Stated** (heuristic)
19. Imposing Carpenter–Kennedy's extra condition
    $b^\top A^2c=1/24$ (Eq. 102) makes a (4,3) method fourth order on
    linear problems; a Gröbner elimination with it gives a sixth-degree
    equation, so rational solutions of (95) are searched and filtered (§7).
    **Stated** / **Shown** (Tables 5–6)
20. Four new rational (4,3) schemes satisfy (102), with increasing $c$ and
    $b_i\ge-3/8$ (Tables 5–6). **Shown** (compiler check, not in the sources: verified exactly)
21. "A simple grid search relatively quickly revealed over two million of
    (5,3) methods with rational coefficients" (§9). **Stated**
22. New (5,3) schemes: the lowest error over the tests (Table 7); one of
    the largest stability regions (Table 8); fourth order on linear
    problems (Table 9); and one whose stage 5 is second order
    ($\sum_ja_{5j}=1$, $\sum_ja_{5j}c_j=1/2$), giving an embedded 3(2) pair
    at no extra cost (Table 10) (§9). **Shown**
23. On three scalar ODEs over $[0,20]$ all new methods converge at third
    order; (4,3)$_1$ is "slightly better" than the five Carpenter–Kennedy
    (4,3) schemes, a by-product of the search, and (5,3)$_1$ has the lowest
    error (§9, Figs. 1–2). **Shown**
24. All (4,3) methods satisfying (102) share one stability region (Fig. 2
    caption), since their $P(z)$ is the degree-4 Taylor polynomial.
    **Shown**
25. The (6,4) scheme of Berland, Bogey and Bailly (12 digits originally)
    is recomputed to 42 digits by Newton with backtracking on the 8
    fourth-order conditions, the 2N constraints and the two extra
    constraints of the original, with $B^{\mathrm W}_6=0.27$ fixed, in
    1000-bit MPFR; residual $10^{-300}$ in four iterations (§10, App. D).
    **Shown** (compiler check, not in the sources: order conditions hold to $10^{-16}$)
26. To design 2N methods of order $\ge4$, solve the standard order
    conditions plus (45)–(46) or (47) numerically in $(A,b)$, not in
    $(A^{\mathrm W},B^{\mathrm W})$ (§§9–10). **Stated**
27. Earlier numerical evidence (Bazavov 2021 [13]) suggests that
    Williamson 2N schemes are automatically commutator-free Lie-group
    integrators of the same order via
    $Y_i=\exp(B^{\mathrm W}_i\Delta Y_i)Y_{i-1}$ (Eqs. 120–123), proved
    only for (3,3); the (6,4) scheme works "remarkably well" for SU(3)
    gradient flow (§1, §10). **Stated** (cited; a hypothesis beyond (3,3))

# Printed slips

- **Eq. (95), linear coefficient:** printed
  $\tfrac16(z_2-z_1)(c_3-c_2)$; it must be $\tfrac16(z_2+z_1)(c_3-c_2)$.
  With the printed sign the four schemes of Tables 5–6 leave residuals
  $1/25920$, $-8/28125$, $4/84375$, $169/268912$; with $+$ all vanish
  (compiler symbolic and exact check, not in the sources).
- **Table 8, $a_{51}$:** printed $\tfrac{12053}{11172}$; it must be
  $\tfrac{2053}{11172}$, which makes the row sum $c_5=\tfrac{13}{14}$ (the
  printed node) and satisfies the third-order conditions; the
  $(A^{\mathrm W},B^{\mathrm W})$ column of Table 8 is correct.
- **Table 9, $A_5$:** printed $-\tfrac8{25}$; it must be
  $-\tfrac{261}{625}$ to reproduce $b_4=\tfrac{17}{64}$ through Eq. (14);
  the Butcher tableau of Table 9 is correct.
- **Eq. (46):** the right side prints $(a_{i,i-2}-a_{j-1,i-2})b_{i-1}$,
  where $j$ is not an index of (46); by (47) with $j=i-1$ it is
  $(a_{i,i-2}-a_{i-1,i-2})b_{i-1}$. The range "$j=2,\dots,i-2$" is printed
  jointly for (45)–(46).
- **Eq. (41):** the summand prints $\prod_{l=i+1}^{i-1}A_lk_i$; it should
  be $\prod_{l=j+1}^{i-1}A_lk_j$ (as in Eq. 33).
- **Eq. (84):** the denominator prints $\sum_{k=1}^{i-1}b_k-c_i$;
  substitution of (82) gives $\sum_{k=1}^{i-1}b_k-c_{i-1}$, which is what
  yields the (correct) Eq. (81).
- Ref. [13] is printed as BIT 62(3) (2021) 745–771; volume 62 is the 2022
  volume (online 2021). Ref. [16] (AIAA paper 2004-2814) is printed with
  year 2012 and a malformed "arXiv:https://arc.aiaa.org/…" field.
- Typos: "auxilliary" (§3), "Butcher tableu" (§4).

# Notation map

| Bazavov (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $h$ | $h$ | agrees |
| $y_t$, $y_{t+h}$ (also $y_0$, $y_{s+1}$) | $y_n$, $y_{n+1}$ | step indexed by time; the stage index is reused for the endpoints |
| $y_i$, $k_i$ | $Y_i$, $f(t_n+c_ih,Y_i)$ | stage values and stage derivatives |
| $a_{ij}$, $b_i$, $c_i$ ("a-form") | $A$, $b$, $c$ | agrees; $c=A\mathbf 1$; modified form $a_{s+1,i}\equiv b_i$, $c_{s+1}\equiv1$ |
| **$A_i$, $B_i$** | $A^{\mathrm W}_i$, $B^{\mathrm W}_i$ (page-local) | **collision with the Butcher matrix $A$ and with $B(\xi)$**: scalar Williamson 2N coefficients |
| $\Delta y_i$ | $\Delta Y_i$ (page-local) | second register |
| **$\alpha_{ij}$, $\beta_i$ ("α-form")** | $d_{ij}$, $d_{s+1,i}$ (page-local) | **collision with the Shu–Osher $\alpha_{ij}$, $\beta_{ij}$**; the source's $\alpha_{ij}$ plays the role of a Shu–Osher $\beta_{ij}$ with all weight on the previous stage (Remark 1) |
| $(s,p)$ | $s$, $p$ | method label, e.g. (4,3) |
| $z_1,\dots,z_5$; $\omega_k,\rho_k,\zeta_7,\chi_{kn},\mathcal C_k$ | — | intermediates of the (4,3) and (5,3) solutions |
| $x=b_2c_2$ | — | unknown of Eq. (95) |
| $d(h)$ | — | absolute error at the end of the test interval |
| **$Y$, $A(t,Y)$ (Eqs. 120–123)** | — | **collision with the stage values $Y_i$ and the Butcher $A$**: Lie-group ODE $Y'=A(t,Y)Y$ |
| "fourth order for linear problems" | — | tall-tree (linear) order conditions to order 4, not classical order 4 |

# Reference list

The paper prints 19 references, numbered [1]–[19]. All 19 are merged
complete into the [bibliography](/bibliography.md) with `citedby`
bazavov-2026. Ref. [16] prints year 2012 with the AIAA DOI
10.2514/6.2004-2814 of a 2004 conference paper and is recorded as printed
(key `berland-2012`), distinct from `berland-2006` ([6]). Ref. [12] prints
an author as "Y. an Yan" (surname Yan). Ref. [17] is an arXiv preprint and
kept as its own entry. No printed duplicates or unparseable items.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [Low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md)
* [Runge–Kutta method](/definitions/runge-kutta-method.md)
* [Runge–Kutta order conditions and simplifying assumptions](/results/runge-kutta-order-conditions.md)

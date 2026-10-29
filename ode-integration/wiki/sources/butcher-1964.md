---
type: Source
title: "Butcher (1964) — Implicit Runge-Kutta processes"
description: "Introduces general implicit Runge–Kutta processes and the coefficient array, proves the implications among the conditions B, C, D, E that reduce the order conditions, builds the s-stage order-2s processes on Gauss–Legendre nodes for s ≤ 5 with their principal error coefficients, and proves convergence of a fixed-point iteration for the stages."
resource: "doi:10.1090/S0025-5718-1964-0159424-9"
source_kind: paper
authors: [Butcher J.C.]
year: 1964
venue: "Math. Comp. 18(85):50-64"
local_file: "/home/stefano/papers/mosaic/ode-integration/1964_Crossref_Mathematics_of_Computation_Butcher_Implicit_Runge-Kutta_processes.pdf"
tags: [runge-kutta, implicit, order-conditions, fully-implicit, implicit-stage-solvers]
timestamp: 2026-10-29T18:13:00Z
---

# Summary

Butcher drops the tradition, traced to Runge, Kutta, Nyström, Gill and
Huťa, of considering only explicit
[Runge–Kutta methods](/definitions/runge-kutta-method.md), and studies the
general implicit $s$-stage process, whose stage derivatives are coupled
through a full matrix $A$. He names three classes, implicit (general),
semi-explicit ($a_{ij}=0$ for $i<j$) and explicit ($a_{ij}=0$ for $i\le j$),
writes the coefficients as an array (with $c$ to the right of $A$), and
gives two three-stage order-4 examples: an implicit one he credits to
Clippinger and Dimsdale (via Kunz) and a semi-explicit one that "appears to
have been previously overlooked".

A count of free coefficients against the number of
[order conditions](/results/runge-kutta-order-conditions.md) (Table 1)
suggests that implicitness gains at most one power of $h$; Butcher points
out that the count ignores the relations among the conditions. Section 2
defines the statements $A(\xi)$ (order $\xi$), $B(\xi)$, $C(\xi)$, $D(\xi)$
and $E(\xi,\eta)$ on the coefficients and proves seven implications among
them. The key one, Theorem 7, gives order $\zeta$ from $B(\zeta)$, $C(\eta)$
and $D(\xi)$ when $\zeta\le\xi+\eta+1$ and $\zeta\le2\eta+2$. The paper
does not use the term "simplifying assumptions", nor stage order; the
bundle defines [stage order](/definitions/stage-order.md) through $B$ and
$C$.

Section 3 applies these results to processes whose abscissae are the
Gauss–Legendre nodes: order $2s$ implies $C(s)$ and $D(s)$, and with $B(2s)$
either of them implies the other and order $2s$, with $A$ uniquely
determined (Theorems 8–10). Table 2 prints the tableaux for $s=1,\dots,5$ in
closed form, the [Gauss methods](/methods/fully-implicit-runge-kutta.md) of
orders 2 to 10; the $s=2$ process is Hammer and Hollingsworth's. Section 4
gives closed forms for the error coefficient of every elementary
differential of order $2s+1$ (Theorems 11–13) and tabulates two of them
(Table 3). Section 5 checks the $s=3$ process on $y'=y$. The Appendix
(Theorem 14) proves existence, uniqueness and convergence of a
fixed-point iteration, sweeping the stages in order and using the new
iterates of earlier stages, for the
[stage equations](/methods/implicit-stage-solvers.md) when $\lvert h\rvert<1/(La)$.
The paper says nothing about stability functions, A-stability,
symplecticity or collocation.

# Version read

Version of record, the AMS scan of Math. Comp. pp. 50–64 (15 pages),
"Received November 1, 1962. Revised April 22, 1963"; the author's
affiliation is the University of Canterbury, Christchurch. The OCR layer is
unreliable in every equation and tableau, so all formulas were read
visually. Title and author agree with the Crossref record; the DOI, volume
and issue are not printed on the pages. Equation, theorem and table numbers
are those of the paper.

# Key claims

Registry notation: $s$ for the paper's $\nu$ (stages), $p$ for its $\rho$
(order), $t$ for its $x$, stage derivatives $f(Y_i)$ for its $g^{(i)}$,
$y_1$ for its numerical value $\hat y$ at $t_0+h$. The paper's $A(\xi)$ is
written "order $\xi$" (notation map).

1. The process is $f(Y_i)$ with $Y_i=y_0+h\sum_{j=1}^sa_{ij}f(Y_j)$,
   $y_1=y_0+h\sum_ib_if(Y_i)$, for an autonomous system $y'=f(y)$, with
   $c_i=\sum_ja_{ij}$ by definition (§1, pp. 50–51). It is "implicit" in
   general, "semi-explicit" when $a_{ij}=0$ for $i<j$, and "explicit" when
   also $a_{ii}=0$; refs. [2]–[7] considered only explicit processes (§1,
   p. 50). **Stated**
2. The numerical and exact solutions agree to terms in $h^p$ iff
   $\Phi=1/\gamma$, $\gamma=r\beta/\alpha$, for every elementary
   differential of order $r\le p$ (Eq. (3), recalled from Butcher 1963,
   ref. [1]). **Stated**
3. The implicit process with $c=(0,\frac12,1)^\top$, rows of $A$ $(0,0,0)$,
   $(\frac5{24},\frac13,-\frac1{24})$, $(\frac16,\frac23,\frac16)$ and
   $b=(\frac16,\frac23,\frac16)^\top$ has order 4 and "is equivalent to a
   process due to R. F. Clippinger and B. Dimsdale and quoted by Kunz [8]"
   (§1, p. 51). **Stated** (order "easy to verify")
4. The semi-explicit process with $c=(0,\frac12,1)^\top$, rows $(0,0,0)$,
   $(\frac14,\frac14,0)$, $(0,1,0)$ and $b=(\frac16,\frac23,\frac16)^\top$
   has order 4, "appears to have been previously overlooked even though it
   is of comparable accuracy and more convenient for practical use" (§1,
   p. 51). **Stated**
5. Free coefficients: $s(s+1)/2$ explicit, $s(s+3)/2$ semi-explicit,
   $s(s+1)$ implicit; the number of order conditions is
   $M=1,2,4,8,17,37,85$ for $p=1,\dots,7$ (Table 1). On counting alone "the
   gain in accuracy that can be achieved by the use of implicit rather than
   explicit processes is not more than one power of $h$ and in some cases
   semi-explicit processes do not give even this gain" (§1, pp. 51–52).
   **Stated**
6. The counting argument "ignores the relationships between them. In fact,
   it happens that the $M$ restrictions of Table 1 can often be satisfied
   with considerably fewer than $M$ variables" (p. 52). **Stated**, then
   shown by §3
7. Under the standing restriction of distinct $c_i$ and non-zero $b_i$, the
   statements are: order $\xi$; $B(\xi)$: $b^\top c^{k-1}=1/k$, $k\le\xi$;
   $C(\xi)$: $\sum_ja_{ij}c_j^{k-1}=c_i^k/k$, all $i$, $k\le\xi$;
   $D(\xi)$: $\sum_ib_ic_i^{k-1}a_{ij}=b_j(1-c_j^k)/k$, all $j$, $k\le\xi$;
   $E(\xi,\eta)$: $\sum_{i,j}b_ic_i^{k-1}a_{ij}c_j^{l-1}=1/(l(k+l))$,
   $k\le\xi$, $l\le\eta$ (§2, p. 52). **Stated** (definitions)
8. Theorems 1–6: order $\xi$ implies $B(\xi)$; order $\xi+\eta$ implies
   $E(\xi,\eta)$; $B(\xi+\eta)$ with $C(\eta)$, or with $D(\xi)$, implies
   $E(\xi,\eta)$; $B(s+\eta)$ with $E(s,\eta)$ implies $C(\eta)$;
   $B(\xi+s)$ with $E(\xi,s)$ implies $D(\xi)$ (pp. 52–53). **Proved**
9. Theorem 7: $B(\zeta)$, $C(\eta)$, $D(\xi)$ with $\zeta\le\xi+\eta+1$ and
   $\zeta\le2\eta+2$ imply order $\zeta$ (p. 53; proof pp. 53–55 by
   induction on tree order). **Proved**
10. For each Gauss–Legendre quadrature formula, nodes the roots of
    $P_s(2c-1)=0$, "there corresponds a unique Runge-Kutta process with the
    same order of accuracy" (§3, p. 55). Theorem 8: order $2s$ implies
    $B(2s)$, $C(s)$, $D(s)$. Theorem 9: given $B(2s)$, either of $C(s)$,
    $D(s)$ implies the other and order $2s$. Theorem 10: given $b$, $c$,
    either $C(s)$ or $D(s)$ determines $A$ uniquely (p. 57). **Proved**
11. Construction: $c$ from $P_s(2c-1)=0$, $A$ from $C(s)$ and $b$ from
    $B(s)$, $C(s)$ being "slightly simpler" than $D(s)$ (pp. 57–58).
    Table 2 prints the processes for $s=1,\dots,5$; "for the case $\nu=2$
    the process is the same as one suggested by Hammer and Hollingsworth
    [11]" (p. 58). **Derived**
12. Principal error function (Henrici's term): for order $p$,
    $y_1-y(t_0+h)\approx h^{p+1}\sum_{r=p+1}\epsilon F$ with
    $\delta=\Phi-1/\gamma$ and $\epsilon=\beta\delta/p!$ (§4, p. 58).
    **Derived**
13. Theorems 11–13, for order $2s$: the bushy differential $\{f^{2s}\}$ has
    $\delta=-(s!)^4/\{(2s)!(2s+1)!\}$; a "central" differential (no subtree
    of order above $s$) has $\delta=-(s!)^4/\{[(2s)!]^2\gamma\}$; a
    non-central one has $\delta=-\delta'$ for the differential $F'$ of
    Eq. (12), so every $\delta$ of order $2s+1$ is $\pm\delta_*$ of a
    central $F_*$ (pp. 59–61). **Proved**
14. The two extreme differentials $F_1=\{f^{2s}\}$ and
    $F_2=(\partial f/\partial y)^{2s}f$ have
    $\epsilon_1=-(s!)^4/\{[(2s)!]^3(2s+1)\}$ and
    $\epsilon_2=\mp(s!)^2/\{(2s)!(2s+1)!\}=\pm\binom{2s}{s}\epsilon_1$, upper
    sign for $s$ even (p. 61). Table 3: $1/\epsilon_1=-24$, $-4320$,
    $-2\,016\,000$, $-1\,778\,112\,000$, $-2\,534\,876\,467\,200$ and
    $1/\epsilon_2=+12$, $-720$, $+100\,800$, $-25\,401\,600$,
    $+10\,059\,033\,600$ for $s=1,\dots,5$ (p. 62). **Derived**
15. Against the quadrature-based processes of Stoller and Morrison (ref.
    [14]), "no coefficient $\epsilon_1\alpha$ exceeds the corresponding
    $\epsilon$" of the present processes, suggesting "a tendency for the
    methods of this paper to be the less accurate"; the lack of suitable
    high-accuracy estimators of the stage values for $s\ge3$ "is a
    disadvantage of the other method" (pp. 61–62). **Stated**
16. $s=3$ on $y'=y$, $y(0)=1$, $h=0.3$: the principal error function is
    $yh^7/100800$, estimated as $22\times10^{-10}$; starting from
    $f(Y_i)=1$ and working to 10 decimals, 8 iterations give
    $y(0.3)\approx1.3498588105$, which exceeds $\exp(0.3)=1.3498588076$ by
    $29\times10^{-10}$, "in reasonable agreement with our error estimate"
    (§5, p. 62). **Shown**
17. Theorem 14: if $\lVert f(y)-f(z)\rVert\le L\lVert y-z\rVert$ and
    $\lvert h\rvert<1/(La)$, with $a=l+u$, $l$ the largest strictly-lower row
    sum and $u$ the largest upper (diagonal included) row sum of
    $\lvert a_{ij}\rvert$, the stage equations have a unique solution and
    the iteration (13), which uses the new iterates of the earlier stages,
    converges to it; the map is a
    contraction in the max norm (Appendix, pp. 62–64). **Proved**

*(Compiler check, not in the sources.)* Table 3, $s=2$:
$\epsilon_1=-(2!)^4/(24^3\cdot5)=-1/4320$ and
$\epsilon_2=-(2!)^2/(24\cdot120)=-1/720$, as printed; the differences of
$M$ in Table 1, $1,1,2,4,9,20,48$, are the per-order tree counts of the
[order-conditions page](/results/runge-kutta-order-conditions.md).

# Printed slips

- p. 54: "Using $C(\eta)$ and that fact that none of $r_1,r_2\cdots,r_s$ can
  exceed $\eta$" ("that fact" for "the fact").
- Ref. [3] (Kutta 1901) prints "naherungsweisen" without the umlaut.

No coefficient or numerical slip was found in Tables 1–3 or in §5.

# Notation map

| Butcher (1964) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$, $x_0$ | $t$, $t_0$ | |
| $y$, $y_0$ | $y(t)$, $y_0$ | exact solution and initial value |
| $\hat y$ | $y_1$ | numerical value at $t_0+h$; **the hat is not the registry embedded solution** |
| $dy/dx=f(y)$ | $y'=f(y)$ | autonomous form throughout; $n$ is the dimension (registry $d$) |
| $\nu$ | $s$ | number of stages |
| $g^{(i)}$ | $f(Y_i)$ | stage derivatives; the paper has no stage values |
| $a_{ij}$, $b_i$, $c_i$ | $A$, $b$, $c$ | agree; $c=A\mathbf 1$ by definition; $c$ printed in a column to the **right** of $A$ |
| implicit / semi-explicit / explicit | — | full $A$ / $a_{ij}=0$ for $i<j$ / $a_{ij}=0$ for $i\le j$; printed names, kept as printed |
| $\rho$ | $p$ | order |
| $F$, $r$ | $F(\tau)$, $\lvert\tau\rvert$ | elementary differential and its order |
| $\Phi$, $\gamma=r\beta/\alpha$ | $\Phi(\tau)$, $\gamma(\tau)$ | elementary weight and density (the paper does not say "density") |
| $\alpha$, $\beta$ | — | coefficients of the series (1)–(2) from ref. [1]; the numerical series uses $h^r/(r-1)!$, a normalization different from the registry B-series |
| $\{F_1\cdots F_s\}$, $\{f^k\}$, $\{_kf\}_k$ | — | tree with subtrees $F_i$; bushy tree; tall tree ($k$-fold nesting) |
| $[\phi^{k-1}]$, $[\Phi_1\cdots\Phi_s]$ | $b^\top c^{k-1}$; $\Phi$ of $\{F_1\cdots F_s\}$ | bracket notation for weights |
| **$A(\xi)$** | "order $\xi$" | **collision with the Butcher matrix $A$ and with A-stability** |
| $B(\xi)$, $C(\xi)$, $D(\xi)$ | $B(\xi)$, $C(\eta)$, $D(\zeta)$ | agree (argument letters vary) |
| $E(\xi,\eta)$ | — | $\sum b_ic_i^{k-1}a_{ij}c_j^{l-1}=1/(l(k+l))$, page-local |
| $P_\nu$ | $P_s$ | Legendre polynomial; **collision with the stability polynomial $P(z)$** |
| $N_E$, $N_S$, $N_I$, $M$ | — | free-coefficient counts and number of order conditions (Table 1); **$M$ collides with the mass matrix** |
| $\delta=\Phi-1/\gamma$, $\epsilon=\beta\delta/\rho!$ | — | error coefficients, sign numerical minus exact; $\epsilon_1$, $\epsilon_2$ for $F_1$, $F_2$; **$\epsilon$ is not the registry $\varepsilon$** |
| central / non-central | — | order-$(2s+1)$ tree with no / one subtree of order above $s$ |
| $\omega_k$, $\omega_k'$ | — | auxiliary constants of Table 2, defined differently for $\nu=4$ and $\nu=5$ |
| $L$, $l$, $u$, $a$, $k$ (Appendix) | — | Lipschitz constant, row-sum bounds, $a=l+u$, contraction factor $\lvert h\rvert La$; **$L$ collides with the registry linear operator, $k$ with the step count** |
| $g_N^{(i)}$ | — | $N$-th iterate of stage derivative $i$ |

# Reference list

The paper prints 15 references, numbered [1]–[15] in order of citation.
All 15 are merged complete into the [bibliography](/bibliography.md) with
`citedby` butcher-1964. Ref. [1] (Butcher 1963, J. Austral. Math. Soc.) is
the source of the elementary-differential expansions; ref. [9] (Merson
1957) is a conference paper printed as "paper No. 110"; refs. [8], [10],
[12], [13] and [15] are books cited with a page. No DOIs are printed. No
printed duplicates or unparseable items.

# Pages created or updated

Chunk 7 (2026-10-29). This source is cited on:

* [B-series, composition and substitution laws](/definitions/b-series.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [Fully implicit collocation Runge–Kutta methods (Gauss, Radau IIA, Lobatto IIIC)](/methods/fully-implicit-runge-kutta.md)
* [Runge–Kutta method](/definitions/runge-kutta-method.md)
* [Runge–Kutta order conditions and simplifying assumptions](/results/runge-kutta-order-conditions.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Stage order](/definitions/stage-order.md)

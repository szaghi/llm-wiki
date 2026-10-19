---
type: Source
title: "de León et al. (2025) — Pseudo-energy-preserving explicit Runge–Kutta methods"
description: "Defines the pseudo-energy-preserving order of a Runge–Kutta method, derives its conditions from the energy-preserving B-series characterization through order 6, and finds explicit methods whose energy error on canonical Hamiltonian systems is of higher order than the solution error, with better long-time behaviour than classical methods."
resource: "doi:10.1051/m2an/2025002"
source_kind: paper
authors: [Barrios de León G.A., Ketcheson D.I., Ranocha H.]
year: 2025
venue: "ESAIM Math. Model. Numer. Anal. 59:729-748"
local_file: "/home/stefano/papers/mosaic/ode-integration/2025_Crossref_ESAIM_Mathematical_Modelling_and_Numerical_Analysis_de_Pseudo-energy-preserving_explicit_RungeKutta_methods.pdf"
tags: [runge-kutta, explicit, structure-preserving, order-conditions, b-series, hamiltonian]
timestamp: 2026-10-19T20:00:00Z
---

# Summary

A Runge–Kutta method of classical order $p$ is
[pseudo-energy-preserving](/methods/pseudo-energy-preserving-runge-kutta.md)
(PEP) of order $q_{\mathrm E}\ge p$ if on every canonical Hamiltonian
system $y'=\mathbb J\nabla\eta(y)$ (constant skew-symmetric $\mathbb J$) the
one-step energy error is $\eta(y_{n+1})-\eta(y_n)=O(h^{q_{\mathrm E}+1})$. It
is the energy analogue of the pseudo-symplectic methods of Aubry and
Chartier, which satisfy the [symplecticity](/properties/symplecticity.md)
conditions to an order above $p$.

The conditions come from the characterization of energy-preserving
[B-series](/definitions/b-series.md) by Celledoni, McLachlan, Owren and
Quispel: the modified vector field $\tilde f$ of
[backward error analysis](/methods/backward-error-analysis.md) preserves
energy to order $q_{\mathrm E}$ iff it is a combination of
$F(\tau)\pm F(\tau^*(\ell))$ over each tree and its energy-preserving
conjugates. Conjugacy classes give one linear condition each on the
coefficients of $\tilde f$; the substitution law, computed with
[BSeries.jl](/software/bseries-jl.md) and SymPy, turns them into conditions
on the elementary weights and on $(A,b,c)$ through PEP order 5. The
cumulative condition counts are 1, 2, 3, 6, 10, 21 for orders 1–6, fewer
than the 12 and 28 of pseudo-symplecticity at orders 5 and 6. PEP order 2
equals classical order 2; PEP order 3 needs only $b^\top c^2=1/3$ beyond
it, a subset of the classical [order conditions](/results/runge-kutta-order-conditions.md).

A local optimizer finds the maximal $q_{\mathrm E}$ for $s\le5$, $p\le5$:
$q_{\mathrm E}=s+1$ for $p=2$, and extra stages are needed for
$q_{\mathrm E}>p$ except $s=p=2$ (Ralston's method). Tests on canonical
problems (exponential entropy system, Duffing, Hénon–Heiles, a
Benjamin–Bona–Mahony semi-discretization) confirm energy convergence at
rate $q_{\mathrm E}$ and show smaller long-time errors, longer linear error
growth and larger usable steps than classical methods at equal cost per
unit time. On non-canonical systems the energy rate falls to $p$, but the
long-time benefit persists. The paper sets PEP beside exact preservation by
AVF and continuous-stage methods, projection, discrete gradients and
[relaxation](/methods/relaxation-runge-kutta.md).

# Version read

arXiv:2407.15365v2 [math.NA], 23 January 2025, a 24-page preprint (text,
tables and appendix pp. 1–21, references pp. 22–24), not the ESAIM: M2AN
version of record; the DOI and journal pagination are not printed in the
file. Title and authors agree with the published version (page 1 prints a
plain hyphen in "Runge-Kutta"). **Surname:** page 1 prints the first
author as "Gabriel A. Barrios de León", a Spanish double surname; Crossref
splits the family name as "de León", which gives the slug `deleon-2025`
and the title form "de León et al."; the authors field keeps the printed
name. Equation, table, figure and section numbers on this page are those
of arXiv v2. Code: the reproducibility repository cited as [3].

# Key claims

Registry notation: $h$ step, $(A,b,c)$ the tableau with $c=A\mathbf 1$,
$p$ classical order, $F(\tau)$ elementary differential, $\Phi(\tau)$
elementary weight, $\tilde f$ modified vector field, $\eta$ the
Hamiltonian (energy). Page-local: $q_{\mathrm E}$ the PEP order (the
source's $q$, which collides with the stage order), $\mathbb J$ the
constant skew-symmetric structure matrix (the source's $J$, which collides
with the Jacobian), $\tilde a(\tau)$ the B-series coefficients of
$\tilde f$ (the source's $v(\tau)$).

1. A Runge–Kutta method is energy preserving if $\eta(y_{n+1})=\eta(y_n)$
   for every Hamiltonian system (4), and pseudo-energy-preserving of order
   $(p,q_{\mathrm E})$ if it has classical order $p$ and
   $\eta(y_{n+1})=\eta(y_n)+O(h^{q_{\mathrm E}+1})$ for every such system
   (Defs. 1–2, §2). **Stated** (definition)
2. Runge–Kutta methods cannot be exactly energy preserving for all
   Hamiltonian systems (citing Celledoni et al. 2009 [13]), though explicit
   methods can be for a specific system ([38, §5.1]) (§1). **Stated**
3. A B-series flow for the canonical system (4) is PEP of order
   $q_{\mathrm E}$ iff it equals
   $\sum_{\lvert\tau\rvert\le q_{\mathrm E}}h^{\lvert\tau\rvert}\sum_{\ell_j\in L(\tau)}\mu_{j,\tau}\big(F(\tau)+(-1)^{m_j(\tau)}F(\tau^*(\ell_j))\big)+O(h^{q_{\mathrm E}+1})$
   (Theorem 1, Eq. 5, quoting [14, Thms. 2–3]); the condition is necessary
   and sufficient (Remark 1). **Stated** (proof in [14])
4. Bushy trees and tall trees with an even number of vertices cannot
   appear in an energy-preserving flow; tall trees with an odd number of
   vertices and self-conjugate trees carry free coefficients (Examples 1–3,
   Eqs. 6–7). **Derived**
5. Energy-preserving conjugacy partitions the trees of each order into
   classes, each giving one condition; up to order 5 classes have one or
   two trees, from order 6 there are triplets whose three equations are
   dependent and give one constraint (§2.1–2.2, Eq. 8). **Derived**
6. PEP order 2 is equivalent to classical order 2, so every consistent
   method with $q_{\mathrm E}\ge2$ has $p\ge2$ and every
   $q_{\mathrm E}=2$ method has $p=2$ (§2.2, §2.3, §3). **Derived**
7. PEP order 3 adds one condition to order 2, $b^\top c^2=1/3$ (Eq. 14),
   weaker than classical order 3, which also needs $b^\top Ac=1/6$
   (§2.2, Eqs. 10, 14). **Derived**
8. The conditions on $(A,b,c)$ for PEP orders 4 (three new) and 5 (four
   new) are Eqs. (15) and (16); the eleven order-6 conditions are given only
   on the elementary weights (Eq. 13, one of them quadratic) (§2.4).
   **Derived**
9. Cumulative condition counts for PEP orders 1–6: 1, 2, 3, 6, 10, 21,
   against 1, 2, 3, 6, 12, 28 for pseudo-symplectic methods (Table 4).
   **Derived** (counts from the authors' code)
10. The unique two-stage second-order explicit method with
    $q_{\mathrm E}=3$ is $\alpha=2/3$ in family (17), $c=(0,2/3)$,
    $b=(1/4,3/4)$ (Ralston's method), citing [13] (§3). **Derived**
11. Exactly one three-stage second-order explicit method has
    $q_{\mathrm E}=4$: $c=(0,1/3,5/6)$, $a_{21}=1/3$, $a_{31}=-5/48$,
    $a_{32}=15/16$, $b=(1/10,1/2,2/5)$ (§3, citing [13]). **Stated**
    (uniqueness by citation)
12. Maximal $q_{\mathrm E}$ found for $(s,p)$: (2,2)→3; (3,2)→4, (3,3)→3;
    (4,2)→5, (4,3)→4, (4,4)→4; (5,2)→6, (5,3)→5, (5,4)→5 (Table 5); except
    for $s=p=2$, $q_{\mathrm E}>p$ needs extra stages. **Shown** (numerical
    search, optimality not proved)
13. The search is local and non-convex (fmincon via RK-Opt [24]), with
    many thousands of random starts minimizing the norm of the leading
    truncation-error coefficients; it stopped at $s=5$ because the optimizer
    struggles beyond, although $q_{\mathrm E}=6$ methods with
    $(s,p)=(6,3)$ and $(7,4)$ were also found (§3). **Stated**
14. Exactly energy-preserving methods often give linear instead of
    quadratic global error growth ([17, 18, 37]); PEP methods are expected
    to do so for moderately long times because their dominant error terms
    do not change the energy (§4). **Stated** (tested in §4)
15. Fair comparison uses $h=sh_0$ with a common advance per stage $h_0$
    for all methods (Eq. 18, §4). **Stated** (methodology)
16. Exponential entropy system, $T=160$: PEP(6,3,6) gives solution rate
    3.00 and energy rate 5.96 at $h=1/32$, with round-off at $h=1/64$
    (Table 6); PEP(7,4,6) gives energy rates up to 8.13 before round-off,
    "roughly consistent with the theory" (Table 7, §4.1.1). **Shown**
17. Undamped Duffing oscillator from $(1.4142,0)$: the largest step
    keeping the orbit in the right half-plane is $h=0.004$ for RK(2,2) and
    $h=0.152$ for PEP(5,2,6); second- and third-order methods typically
    increase the energy, fourth-order ones decrease it, PEP(7,4,6) more
    slowly than RK(4,4) (§4.1.2, Fig. 1). **Shown**
18. Hénon–Heiles ($\lambda=1$ in the source's potential): PEP methods
    conserve energy significantly better than pseudo-symplectic methods of
    matching orders, PS(3,2,4) against PEP(3,2,4) and PS(5,3,6) against
    PEP(6,3,6), up to $t=10^3$ (§4.1.3, Fig. 2). **Shown**
19. Benjamin–Bona–Mahony solitary wave on $[-90,90]$, Fourier collocation
    with a conservative semi-discretization (Eq. 27): PEP(4,2,5) gives
    smaller long-time errors than the midpoint method, $h_0=0.05$, to
    $t=10^3$ (§4.1.4, Fig. 3). **Shown**
20. Theorem 1 holds only for canonical (constant $\mathbb J$) Hamiltonian
    systems (§4, §4.2). **Stated**
21. Non-canonical nonlinear oscillator (Eq. 29): error growth is linear,
    then superlinear, then saturates; PEP(4,2,5) keeps linear growth longest
    among second-order methods, and PEP(7,4,6) has a larger initial but
    smaller long-time error than RK(4,4); PEP and pseudo-symplectic methods
    of matching orders behave very similarly (§4.2.1, Figs. 4–5). **Shown**
22. Lotka–Volterra (non-canonical): the energy rate of PEP(6,3,6) tends to
    the classical order 3 (3.05 at $h=1/64$), not 6 (Table 8), yet higher
    PEP order still gives smaller long-time errors and orbits closer to the
    periodic one; pseudo-symplectic methods give a similar benefit
    (§4.2.2, Figs. 6–8). **Shown**
23. Exact energy preservation is available from AVF and continuous-stage
    methods (implicit), projection (oblique projection along the step also
    preserves linear invariants), discrete gradients and relaxation; since
    floating-point arithmetic breaks even exact conservation, numerical
    energy conservation "is effectively a matter of making the energy error
    small in any case" (§1, §1.1). **Stated**

*(Compiler check by the reader, not in the source.)* With $c=A\mathbf 1$,
PEP(4,2,5) satisfies $b^\top\mathbf 1=1$, $b^\top c=1/2$, $b^\top c^2=1/3$,
$b^\top Ac\ne1/6$ (so $p=2$) and all of (15)–(16) in exact arithmetic;
PEP(5,2,6), PEP(6,3,6), PEP(7,4,6) and PEP(7,5,6) satisfy their stated
orders to $10^{-14}$–$10^{-16}$, PEP(6,3,6) fails order 4 and PEP(7,4,6)
fails order 5, as their labels say.

# Printed slips

- **Eq. (31), PEP(4,2,5):** the abscissae column prints
  $(0,\tfrac1{10},\tfrac{19}{20},\tfrac{37}{63})$, but the row sums are
  $(0,\tfrac1{10},\tfrac{37}{63},\tfrac{19}{20})$: $c_3$ and $c_4$ are
  swapped. With $c=A\mathbf 1$ the method satisfies all its conditions.
- **Eq. (9):** the constants of $u([[\bullet,\bullet]])$ and
  $u([\bullet,[\bullet]])$ are printed as $\tfrac7{12}$ and $\tfrac16$; the
  exact flow requires $1/\gamma(\tau)$, that is $\tfrac1{12}$ and
  $\tfrac18$, and the downstream conditions (11) and (15) are consistent
  only with the latter.
- **Eq. (16), second condition:** printed $\sum_{i,j}b_i(a_{ij}c_j)^2$;
  the tree $[[\bullet],[\bullet]]$ and a numerical check on the printed
  methods require $\sum_ib_i\big(\sum_ja_{ij}c_j\big)^2$.
- **Eq. (21):** "$\log(e_{i+1}/e_i)/\log(h_{i+1}/h_i)=\log(e_{i+1}/e_i)/\log(2)$";
  with halving, $\log(h_{i+1}/h_i)=-\log2$, so the second equality has the
  wrong sign.
- Tables 6–7 print a convergence rate in the first row ($h=1/2$), where no
  coarser step exists in the table.
- §4.1.2: "the correct solution is shown in red in Figure 6(a)"; Fig. 6(a)
  is the Lotka–Volterra phase portrait, the Duffing results are Fig. 1.
- §4.2.2 calls Lotka–Volterra "two competing biological species"; system
  (30) is predator–prey.
- Fig. 4a labels family (17) with $\alpha=10,1.5,1$ as "RK(2,2)", which §4
  defines as the midpoint method ($\alpha=1/2$).
- **Refs. [41] and [42] are the same paper** (Ranocha, Sayyari, Dalcin,
  Parsani, Ketcheson, SIAM J. Sci. Comput. 42(2):A612–A638, 2020), printed
  twice with minor differences.
- Table 12, PEP(7,5,6): $c_4$ differs from the row sum of the printed
  $a_{4j}$ by $3.9\times10^{-11}$, and $b_2$, $b_4$ are $O(10^{-13})$; the
  method appears only in the appendix and is not tested.
- Typos: "ilustrative" (§4.1.3); "duffing" (Fig. 1 caption); "with with"
  (Fig. 3 caption).

# Notation map

| de León et al. (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $h$, $y_n$ | $h$, $y_n$ | agrees; autonomous $y'=f(y)$ |
| $h_0$ | — | advance per stage, $h=sh_0$ |
| $H$ | $\eta$ | Hamiltonian (energy) |
| **$J$** | $\mathbb J$ (page-local) | **collision with the Jacobian $J$**: constant non-singular skew-symmetric matrix |
| **$q$ (PEP or pseudo-symplectic order)** | $q_{\mathrm E}$ (page-local) | **collision with the stage order $q$** |
| $s$, $p$ | $s$, $p$ | agrees; labels PEP$(s,p,q_{\mathrm E})$, PS$(s,p,q)$, RK$(s,p)$ |
| $A$, $b$, $c$ | $A$, $b$, $c$ | agrees; $c=A\mathbf 1$ assumed |
| $T$, $T_q$, $\lvert\tau\rvert$, $\sigma(\tau)$ | $T$, $\lvert\tau\rvert\le q$, $\lvert\tau\rvert$, $\sigma(\tau)$ | agrees |
| $F_f(\tau)$ | $F(\tau)$ | elementary differential |
| $B(u,hf,y)$ | $B(a,y)$ | B-series, same $h^{\lvert\tau\rvert}/\sigma(\tau)$ normalization, without the $\varnothing$ term |
| **$u(\tau)$** | $\Phi(\tau)$ | elementary weights of the map $y_{n+1}=y_n+B(u,hf,y_n)$; **collision with the state $u$ of §4** |
| $v(\tau)$ | $\tilde a(\tau)$ (page-local) | coefficients of the modified field $\tilde f$ |
| $L(\tau)$, $S(\ell)$, $\tau^*(\ell)$, $m_j(\tau)$ | — | leaves, trunk, energy-preserving conjugate, root-to-leaf distance |
| $\mu_{j,\tau}$ | — | free coefficients of the energy-preserving basis |
| $\alpha$ (family (17)) | — | two-stage parameter; **collision with Shu–Osher $\alpha_{ij}$** in letter only |
| $u$, $u_1$, $u_2$ (§4) | $y$ | state of the test problems |
| **$\lambda$ (Hénon–Heiles)** | — | **collision with the Dahlquist $\lambda$**: coupling parameter |
| EOC | — | experimental order of convergence |

# Reference list

The paper prints 44 references, numbered [1]–[44] in alphabetical order.
All 44 are merged complete into the [bibliography](/bibliography.md) with
`citedby` deleon-2025. Refs. [41] and [42] are the same work printed twice
(Ranocha et al., SIAM J. Sci. Comput. 2020) and are folded into one entry,
`ranocha-2020-c`, so the 44 printed items give 43 entries. Ref. [3] is the authors' reproducibility
repository (2024), keyed `deleon-2024` to follow the Crossref surname
split. Ref. [44] is an arXiv preprint printed as a DOI URL
(10.48550/arXiv.2301.09335) and kept as its own entry. Several entries
print an issue month instead of pages ([16], [20], [22], [25], [28],
[39]); [28] prints no volume or pages. No unparseable items.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [B-series, composition and substitution laws](/definitions/b-series.md)
* [Backward error analysis, modified equations and modifying integrators](/methods/backward-error-analysis.md)
* [Benjamin–Bona–Mahony equation](/benchmarks/benjamin-bona-mahony-equation.md)
* [BSeries.jl and RootedTrees.jl](/software/bseries-jl.md)
* [Entropy stability and conservation of the fully discrete scheme](/properties/entropy-stability.md)
* [Pseudo-energy-preserving explicit Runge–Kutta methods](/methods/pseudo-energy-preserving-runge-kutta.md)
* [Relaxation Runge–Kutta methods](/methods/relaxation-runge-kutta.md)
* [Runge–Kutta order conditions and simplifying assumptions](/results/runge-kutta-order-conditions.md)
* [Symplecticity and quadratic-invariant preservation](/properties/symplecticity.md)

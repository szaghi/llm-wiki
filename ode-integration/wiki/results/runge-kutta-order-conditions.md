---
type: Result
title: "Runge–Kutta order conditions and simplifying assumptions"
description: "A Runge–Kutta method has order p iff its elementary weights equal 1/γ(τ) for every rooted tree of at most p vertices; the page gives the conditions to order five in matrix form, their growth with p, simplifying assumptions B and C, related condition families, numerical constructions, stage-count barriers and records, and the extensions to partitioned, additive and multiderivative methods."
status: established
aliases: [order conditions, Butcher order conditions, rooted-tree order conditions, simplifying assumptions, B(ξ), C(η)]
tags: [runge-kutta, order-conditions]
timestamp: 2026-10-20T06:18:00Z
---

# Runge–Kutta order conditions and simplifying assumptions

**Theorem (as recalled by Ketcheson & Ranocha (2023) from Hairer–Nørsett–Wanner,
Thm. II.2.6).** A [Runge–Kutta method](/definitions/runge-kutta-method.md)
$(A,b,c)$ with $c=A\mathbf 1$ has order $p$ if and only if

$$\Phi(\tau)=\frac{1}{\gamma(\tau)}\qquad\text{for every rooted tree }\tau\text{ with }\lvert\tau\rvert\le p,$$

where $\Phi(\tau)$ is the elementary weight of the method and $\gamma(\tau)$
the tree density. The proof compares the [B-series](/definitions/b-series.md)
of one step, $B(\Phi,y_n)$, with that of the exact flow, whose coefficients
are $1/\gamma(\tau)$ ([Ketcheson & Ranocha (2023)](/sources/ketcheson-2023.md),
§2.2, Eqs. (13)–(20)).

## Trees, densities and elementary weights

For $\tau=[\tau_1,\dots,\tau_m]$ (the root joined to the roots of the subtrees
$\tau_k$): $\lvert\tau\rvert$ counts vertices;
$\gamma(\bullet)=1$, $\gamma(\tau)=\lvert\tau\rvert\,\gamma(\tau_1)\cdots\gamma(\tau_m)$;
$\sigma(\bullet)=1$, $\sigma(\tau)=\sigma(\tau_1)\cdots\sigma(\tau_m)\,\mu_1!\mu_2!\cdots$
with $\mu_k$ the multiplicities of identical subtrees. The internal weights
are $\Phi_j(\bullet)=1$, $\Phi_j(\tau)=\prod_{k=1}^m\sum_{l}a_{jl}\Phi_l(\tau_k)$,
and $\Phi(\tau)=\sum_jb_j\Phi_j(\tau)$ (Ketcheson & Ranocha (2023), Eqs. (5),
(14)–(16)). There are 1, 1, 2, 4 trees of orders 1–4 (Eqs. (1)–(4)), and 9 of
order 5, so order 4 needs 8 conditions and order 5 needs 17
([Biswas et al. (2023)](/sources/biswas-2023.md), Table 1). Writing
$\operatorname{diag}(c)$ for the diagonal matrix of abscissae and powers of
$c$ componentwise, the conditions read:

| order | conditions |
|---|---|
| 1 | $b^\top\mathbf 1=1$ |
| 2 | $b^\top c=\frac12$ |
| 3 | $b^\top c^2=\frac13$, $b^\top Ac=\frac16$ |
| 4 | $b^\top c^3=\frac14$, $b^\top\operatorname{diag}(c)Ac=\frac18$, $b^\top Ac^2=\frac1{12}$, $b^\top A^2c=\frac1{24}$ |
| 5 | $b^\top c^4=\frac15$, $b^\top\operatorname{diag}(c)^2Ac=\frac1{10}$, $b^\top\operatorname{diag}(c)Ac^2=\frac1{15}$, $b^\top\operatorname{diag}(Ac)Ac=\frac1{20}$, $b^\top\operatorname{diag}(c)A^2c=\frac1{30}$, $b^\top Ac^3=\frac1{20}$, $b^\top A\operatorname{diag}(c)Ac=\frac1{40}$, $b^\top A^2c^2=\frac1{60}$, $b^\top A^3c=\frac1{120}$ |

The table is Biswas et al. (2023, Table 1) rewritten with $A\mathbf 1=c$
(they list $b^\top A^{k-1}\mathbf 1=1/k!$ for the tall trees). Ketcheson &
Ranocha (2023, Table 1) give the same order-4 data tree by tree, with
$\sigma$, $\gamma$, $F(\tau)$ and $\Phi(\tau)$ for each.
[Fekete et al. (2022)](/sources/fekete-2022.md) (Eq. (8)) write the order-3
and order-4 conditions in residual form, $b^\top(\tfrac12c^2-Ac)=0$,
$b^\top A(\tfrac12c^2-Ac)=0$, $b^\top(\tfrac16c^3-\tfrac12Ac^2)=0$ and
$b^\top\operatorname{diag}(c)(\tfrac12c^2-Ac)=0$: since
$\tfrac12c^2-Ac=-\tau^{(2)}$ and $\tfrac16c^3-\tfrac12Ac^2=-\tfrac12\tau^{(3)}$
*(compiler check, not in the sources)*, these are conditions on the
[stage-order residuals](/definitions/stage-order.md).
[Belardo et al. (2026)](/sources/belardo-2026.md) (Table 1) and
[Bazavov (2026)](/sources/bazavov-2026.md) (App. B) print the same conditions to orders 4 and 3.

**Growth with $p$.** [Zhang (2024)](/sources/zhang-2024.md) writes the theorem in
weight-vector form, $b^\top\Phi_\cdot(\tau)=1/\gamma(\tau)$ for all trees with at most $p$
vertices, where the vector of internal weights obeys $\Phi_\cdot([\tau])=A\,\Phi_\cdot(\tau)$ when
$\tau$ is attached to a new root and is the componentwise product of the vectors of the subtrees
when roots are merged (Proposition 1, Eqs. (5)–(6), attributed to Butcher). The number of trees
with exactly $k$ vertices is 1, 1, 2, 4, 9, 20, 48, 115, 286, 719 for $k=1,\dots,10$, so order 10
imposes 1205 conditions (§2). An explicit 16-stage method has $s(s+1)/2=136$ free coefficients,
so the order-10 system is heavily overdetermined. For fixed $A$ and $c$ the conditions are linear
in $b$ (Belardo et al. 2026, §2, Eq. (1)), which is the basis of the null-rule description of
[embedded pairs](/methods/embedded-runge-kutta-pair.md).

## Simplifying assumptions and related families

* $B(\xi)$: $b^\top c^{k-1}=1/k$ for $k=1,\dots,\xi$ (quadrature or bushy-tree
  conditions).
* $C(\eta)$: $\tau^{(k)}=Ac^{k-1}-c^k/k=0$ for $k=1,\dots,\eta$.

These are Butcher's assumptions as restated by Biswas et al. (2023, Eqs.
(10)–(11)) and [Biswas et al. (2024)](/sources/biswas-2024.md) (Eqs.
(6)–(7)); $C(\eta)$ together with $B$ defines [stage order](/definitions/stage-order.md).
Biswas et al. (2023, Eqs. (12)–(13)) name two further families:

* $T(\xi)$: $b^\top A^{k-1}\mathbf 1=1/k!$, $k=1,\dots,\xi$ — the tall-tree
  conditions, which are exactly the order conditions for linear constant-
  coefficient problems and fix the leading coefficients of the
  [stability function](/definitions/stability-function.md); Bazavov (2026, §7, Eq. (102))
  imposes $b^\top A^2c=\tfrac1{24}$ on third-order four-stage methods, Carpenter and Kennedy's
  "nearly optimal" condition as he recalls it, which makes them fourth order on linear problems;
* an Albrecht-type family $b^\top A^j\tau^{(k)}=0$ for $k\ge1$, $j+k<\xi$.

$B(p)$, $T(p)$ and the Albrecht family at $\xi=p$ are necessary but not
sufficient for order $p$ (Biswas et al. (2023), §2). The quantities
$b^\top A^j\tau^{(k)}$ are linear combinations of the order-condition
residuals: with the page-local residual
$\varrho_{i,k}=b^\top A^{i-k}c^k-k!/(i+1)!$,
$b^\top A^j\tau^{(k)}=\varrho_{j+k,k-1}-\tfrac1k\varrho_{j+k,k}$ (Biswas et al. (2023),
§3). Imposing [weak stage order](/definitions/weak-stage-order.md) $q_{\mathrm w}$
therefore makes $(p-1)(p-2)/2$ order conditions redundant for
$(p,q_{\mathrm w})\in\{(3,2),(3,3),(4,3),(4,4),(5,4),(5,5)\}$ (Table 2: 1 of 4,
3 of 8, 6 of 17).

[Biswas et al. (2025)](/sources/biswas-2025.md) (Eq. (3.2)) name the
**palm-tree conditions** $b^\top A^kc^j=1/\big((k+j+1)\cdots(j+1)\big)$,
$0\le j+k\le p-1$ (a bushy tree attached at the leaf of a tall tree), and
state that weak stage order $q_{\mathrm w}\ge p-1$ together with $B(p)$ implies
all of them; for $p\le3$ every order condition is a palm-tree condition, so
only $b^\top\operatorname{diag}(c)Ac=\tfrac18$ remains at order 4 (§3.1,
App. A.1). The implication is stated without proof.

## Stage-count barriers recalled by the sources

* Explicit methods reach $p=s$ only for $p\le4$
  ([Hedayati Nasab et al. (2021)](/sources/hedayatinasab-2021.md), §2, citing
  Butcher); the minimum explicit stage counts for orders 2–5 are 2, 3, 4, 6
  (Biswas et al. (2025), Table 3.1, row $q_{\mathrm w}=1$).
* No explicit method of order $\ge5$ has a positive SSP coefficient
  (Fekete et al. (2022), §1.1); see
  [SSP methods](/methods/strong-stability-preserving-runge-kutta.md).
* A DIRK has $p\le s+1$ (Biswas et al. (2023), §4, citing Hairer–Wanner
  Thm. IV.4.18; Biswas et al. (2024), Thm. 3.2 at $q_{\mathrm w}=0$).
* A fully implicit method has $p\le2s$, attained by Gauss–Legendre methods
  (Biswas et al. (2024), Example 7.4, Cor. 4.5).
* **Explicit order 10 with 16 stages (numerical record, not a barrier).** The
  minimum stage count of an explicit method of order $p>8$ is unknown; orders
  1–5 are "straightforward" and 6–8 "difficult, though tractable" (Zhang (2024),
  §1). The best published explicit order-10 methods, Hairer's (1978) and
  Feagin's, have 17 stages, and Khashin (2009) found a 13-stage order-9 method by
  numerical search, as recalled by Zhang (§1, §6). Zhang (2024) reports a
  16-stage explicit method whose 136 coefficients, given to 3000+ digits, make the
  sum of squared order-10 residuals smaller than $10^{-6000}$; it is printed to 120
  digits (§5, Table 2). *Hypothesis-grade:* that an exact order-10 method with 16
  stages exists near these coefficients is not proved (no exact form; Gröbner/CAD
  certification is out of reach and Smale's α-theory does not apply to this
  overdetermined system, §5.1, §6), and whether 16 stages is minimal for order 10
  is open.

The weak-stage-order analogues of these barriers are on
[weak-stage-order barriers](/results/weak-stage-order-barriers.md). Biswas et
al. (2024, Remark 3.6) and Biswas et al. (2025, Remark 1) note that their
barriers use only the order of the stability function, i.e. $T(p)$.

## Error constants

The leading local error is measured by the **principal error norm** (page-local
$\mathcal E_{p+1}$)

$$\mathcal E_{p+1}=\Big(\sum_{\lvert\tau\rvert=p+1}\Big(\frac{1}{\sigma(\tau)}\Big(\frac{1}{\gamma(\tau)}-\Phi(\tau)\Big)\Big)^2\Big)^{1/2},$$

the primary objective of Biswas et al. (2025, Eq. (3.3)). Biswas et al. (2023,
§5) minimize the squared norm of the order-$(p+1)$ residuals instead. Fekete
et al. (2022, §2) use the Kennedy–Carpenter–Lewis measurements (2- and
$\infty$-norms of the order-$(p+1)$ and order-$p$ error vectors of main and
embedded method, and their ratios) to design
[embedded pairs](/methods/embedded-runge-kutta-pair.md). Zhang (2024, Remark 2)
considers the analogous sum $\sum_{\lvert\tau\rvert\le p}\sigma(\tau)^{-2}(\Phi(\tau)-1/\gamma(\tau))^2$
over the order conditions themselves as a search objective and finds no difference in
difficulty from the unweighted sum.

## Solving the conditions

* **Numerical search without simplifying assumptions.** Zhang (2024, §2–5)
  minimizes the unweighted sum of squared residuals
  $\sum_{\lvert\tau\rvert\le p}(\Phi(\tau)-1/\gamma(\tau))^2$ over all entries of a strictly
  lower-triangular $A$ and $b$, by BFGS with a "Hessian reset" heuristic (reset to the identity
  when the plain gradient step does better), reverse-mode differentiation through a shared-subtree
  evaluation of all internal weights, and adaptive 128–256-bit arithmetic, since in double
  precision the gradient loses almost all correct bits along the descent (§3–4, Figs. 4–5).
  Several weeks of random starts gave 8000 candidates, of which one was refined to the
  order-10 method above (§5). No structure was imposed, yet the printed coefficients have
  $b_2=b_4=b_5=0$, and $c=A\mathbf 1$ gives five stages with the same abscissa
  $0.41558\ldots$, $c_2=c_4$ and $c_{16}=1$, the structure of classical high-order
  constructions; the paper does not comment *(compiler check of Table 2, not in the source)*. Zhang states that the solutions lie on a positive-dimensional set, on
  preliminary evidence (Remark 6).
* **Butcher variables for constrained classes.** For
  [2N-storage methods](/methods/low-storage-runge-kutta.md), Bazavov (2026) turns the storage
  restriction into $(s-1)(s-2)/2$ quadratic constraints on $(A,b)$ and recommends solving them
  together with the order conditions in the Butcher variables, where the systems have low
  degree; all four- and five-stage third-order 2N methods then follow from one quadratic
  equation (§4, §7–8, §10).
* **Weights for fixed stages.** Because the conditions are linear in $b$ for fixed $(A,c)$, all
  weight vectors of a given order sharing the stages form an affine set (Belardo et al. 2026,
  §2–3).

## Composition and order

Composing two steps of one method does not raise its order unless the
coefficients are tuned: any composition of two second-order explicit
two-stage methods has coefficient $\tfrac18$ on the tall tree of order 3
instead of $\tfrac16$, so it has order exactly two (Ketcheson & Ranocha
(2023), §2.3.1). Composition with suitable starting and finishing methods can
raise the order: Butcher's 5-stage order-4 method has effective order 5 with
order-3 starter and finisher (§2.3.2); see
[processing and effective order](/methods/processing-and-effective-order.md).

## Extensions

* **Additive and partitioned methods.** Trees get colored vertices, one color
  per partition; elementary differentials use $f^{[\nu]}$ and elementary
  weights use the tableau of the vertex's color (Ketcheson & Ranocha (2023),
  §3.1; N-trees and P-trees). See [IMEX and additive RK](/methods/imex-runge-kutta.md)
  and [GARK](/methods/generalized-additive-runge-kutta.md).
* **Partitioned methods with shared weights and abscissae.** When every
  partition $r$ uses its own matrix $A^{\{r\}}$ but all share $b$ and $c$, the
  conditions up to order 3 reduce to the classical ones, with
  $b^\top A^{\{r\}}c=\tfrac16$ for every $r$
  ([Hedayati Nasab & Vermeire (2022)](/sources/hedayatinasab-2022.md), §3.2,
  Eqs. (31)–(39); [Doehring et al. (2025)](/sources/doehring-2025.md), §2.1,
  Eq. (2.3)). At order 4 the per-partition conditions $b^\top c^3=\tfrac14$,
  $b^\top\operatorname{diag}(c)A^{\{r\}}c=\tfrac18$, $b^\top A^{\{r\}}c^2=\tfrac1{12}$
  are joined by the coupling conditions $b^\top A^{\{r_1\}}A^{\{r_2\}}c=\tfrac1{24}$
  for all pairs $r_1,r_2$ (Doehring et al. 2025, Eq. (2.4)), which the fourth-order
  [paired explicit methods](/methods/paired-explicit-runge-kutta.md) satisfy by
  sharing the last three subdiagonal entries (§3.2).
* **Nonlinearly partitioned methods.** For $y'=F(y,y)$ with a two-argument
  partition, an [NPRK method](/methods/nonlinearly-partitioned-runge-kutta.md)
  with coefficient tensor $a_{ijk}$ and weight matrix $b_{ij}$ (page-local,
  defined on that page) has two underlying Runge–Kutta methods,
  $a^{\{1\}}_{ij}=\sum_ka_{ijk}$, $b^{\{1\}}_i=\sum_jb_{ij}$ and
  $a^{\{2\}}_{ik}=\sum_ja_{ijk}$, $b^{\{2\}}_j=\sum_ib_{ij}$, with equal abscissae. On an
  additive $F(u,v)=f^{\{1\}}(u)+f^{\{2\}}(v)$ the method is the additive method
  built from them, so order $p$ requires the additive (colored-tree) conditions to
  order $p$; the shared abscissae remove none of the NPRK conditions, which must hold
  for nonlinear partitions ([Buvoli & Southworth (2025)](/sources/buvoli-2025.md),
  §4.1, Def. 4.1, Eqs. (4.3)–(4.5)). For a diagonally implicit subclass Buvoli &
  Southworth avoid a new tree theory: every such method equals a larger
  *sequentially coupled* method, which is an $(s-1)$-stage partitioned method
  with equal weights $b=\hat b$ applied to $z'=F(z,w)$, $w'=F(z,w)$ (Props. 4.3–4.4,
  proved in App. A), so the partitioned conditions apply. With the page-local
  tableaux $(A,c)$, $(\hat A,\hat c)$ of that partitioned method, order 2 needs only
  $b^\top\mathbf 1=1$ and $b^\top c=b^\top\hat c=\tfrac12$, and order 3 adds
  $b^\top c^2=b^\top\operatorname{diag}(c)\hat c=b^\top\hat c^2=\tfrac13$,
  $b^\top Ac=b^\top A\hat c=b^\top\hat Ac=b^\top\hat A\hat c=\tfrac16$: per tableau the
  classical conditions, plus three coupling conditions (Table 4.3, Eqs. (4.13)–(4.15)).
  The general conditions use edge-colored rooted trees, from a companion paper
  that the bundle has not ingested, as recalled by
  [Buvoli et al. (2026)](/sources/buvoli-2026.md) (§2.2, Table 2, App. B): up to
  order 3 they are the additive conditions plus a single *nonlinear coupling
  condition* $\sum b_{ij}a_{ikl}a_{juv}=\tfrac13$ on the tree whose root carries the
  mixed derivative $\partial_u\partial_vF$, a condition that cannot be written in
  terms of the underlying methods; second order holds iff both underlying methods
  are second order (SM C.1, recalled). Sparsity patterns of multirate NPRK methods
  restrict the summation sets of these conditions without changing them (Table 2).
* **Two-derivative methods.** With weights $b$, $\dot b$ on $f$ and $\dot f$
  and abscissae $c=A\mathbf 1$, $\dot c$ the row sums of $(\dot a_{ij})$, the
  conditions to order 3 are $b^\top\mathbf 1=1$; $b^\top c+\dot b^\top\mathbf 1=\tfrac12$;
  $b^\top c^2+2\dot b^\top c=\tfrac13$ and $b^\top Ac+b^\top\dot c+\dot b^\top c=\tfrac16$
  ([Gottlieb et al. (2022)](/sources/gottlieb-2022.md), §2.1, recalling
  their ref. [6], with four more at order 4). For the IMEX two-derivative class
  with an additional explicit tableau the paper derives 22 conditions through
  order 3, new in that paper (§3.2). See
  [multiderivative RK](/methods/multiderivative-runge-kutta.md).
* **Splitting and Rosenbrock methods** have their own order theories:
  [splitting order conditions](/results/splitting-order-conditions.md) and
  [ROW methods](/methods/rosenbrock-wanner-method.md).

The conditions are generated automatically by RootedTrees.jl and
BSeries.jl ([BSeries.jl](/software/bseries-jl.md); Ketcheson & Ranocha (2023),
§1).

## Qualifications

* The symbol $S(\xi)$ is used for two different families: Biswas et al. (2023,
  Eq. (12)) for the Albrecht-type family above ($j+k<\xi$), and Biswas et al.
  (2024, Eq. (4)) for the weak-stage-order conditions
  ($0\le j\le s-1$, $1\le k\le\xi$). This page uses neither symbol.
* "Order" here is classical order on smooth non-stiff problems. On stiff
  problems the observed order can drop to about the
  [stage order](/definitions/stage-order.md); see
  [order reduction](/definitions/order-reduction.md).
* Hedayati Nasab & Vermeire (2022, §2.1) state that order $p$ requires $2^{p-1}$
  conditions; this matches the counts 1, 2, 4, 8 only up to $p=4$, while order 5
  needs 17 (Biswas et al. 2023, Table 1; Zhang 2024, §2). It is a misstatement,
  not a disagreement about the conditions, which they apply only to order 3.
* Zhang (2024, Remark 2) calls the $\sigma^{-2}$-weighted sum over all trees with
  at most $p$ vertices the norm of the "principal error coefficients"; elsewhere
  on this page that name is reserved for the trees with $p+1$ vertices.
* Related condition families with their own pages:
  [pseudo-energy-preserving order](/methods/pseudo-energy-preserving-runge-kutta.md),
  whose order 2 coincides with classical order 2 and whose order 3 needs only
  $b^\top c^2=\tfrac13$ beyond it ([de León et al. (2025)](/sources/deleon-2025.md),
  §2.2, Eq. (14)).

# Citations

- [Ketcheson & Ranocha (2023)](/sources/ketcheson-2023.md) — §2.2, Eqs. (1)–(5), (13)–(20), Table 1 (theorem as recalled, trees, weights); §2.3 (composition, effective order); §3.1 (colored trees).
- [Biswas et al. (2023)](/sources/biswas-2023.md) — Eqs. (10)–(13), §3, Tables 1–2 (conditions to order 5; $B$, $C$, $T$, Albrecht family; redundancy under weak stage order); §4 (DIRK bound $p\le s+1$); §5 (objective).
- [Biswas et al. (2024)](/sources/biswas-2024.md) — Eqs. (4), (6)–(7); Remark 3.6; Thm. 3.2; Example 7.4; Cor. 4.5.
- [Biswas et al. (2025)](/sources/biswas-2025.md) — Eq. (3.2) (palm-tree conditions), Eq. (3.3) (principal error norm), Table 3.1, Remark 1.
- [Fekete et al. (2022)](/sources/fekete-2022.md) — Eq. (8) (residual form to order 4); §1.1 (no explicit SSP method of order $\ge5$); §2 (error measurements).
- [Gottlieb et al. (2022)](/sources/gottlieb-2022.md) — §2.1 (two-derivative conditions), §3.2 (IMEX two-derivative conditions to order 3).
- [Hedayati Nasab et al. (2021)](/sources/hedayatinasab-2021.md) — §2 ($p=s$ possible only to order 4).
- [Zhang (2024)](/sources/zhang-2024.md) — §1 (records for orders 9–10, minimum unknown for $p>8$), §2 (Proposition 1, Eqs. (2)–(6), condition count), §3–4 (search machinery, Figs. 4–5), §5 (Table 2, residual), §5.1, §6 (certification), Remarks 2 and 6.
- [Bazavov (2026)](/sources/bazavov-2026.md) — App. B (conditions to order 3), §4, §7 (Eq. (102)), §8, §10.
- [Belardo et al. (2026)](/sources/belardo-2026.md) — §2 (Table 1, Eq. (1)), §3.
- [Doehring et al. (2025)](/sources/doehring-2025.md) — §2.1 (Eqs. (2.3)–(2.4)), §3.2.
- [Hedayati Nasab & Vermeire (2022)](/sources/hedayatinasab-2022.md) — §2.1, §3.2 (Eqs. (31)–(39)).
- [de León et al. (2025)](/sources/deleon-2025.md) — §2.2 (Eq. (14)).
- [Buvoli & Southworth (2025)](/sources/buvoli-2025.md) — §4.1 (Def. 4.1, Eqs. (4.3)–(4.5)), Props. 4.3–4.4 and App. A, Table 4.3, Eqs. (4.13)–(4.15).
- [Buvoli et al. (2026)](/sources/buvoli-2026.md) — §2.2, Table 2, App. B, SM C.1.

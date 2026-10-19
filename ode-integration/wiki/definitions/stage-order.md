---
type: Definition
title: "Stage order"
description: "Stage order q is the largest integer for which the quadrature conditions B(q) and the stage conditions C(q) hold, i.e. the stage-order residuals τ^(k) vanish for k ≤ q; it bounds the observed order on stiff problems, is at most 2 for DIRKs and 1 for explicit methods, and equals s for Gauss and Radau IIA."
status: established
aliases: [classical stage order, stage-order residual, C(η) condition, stiff order]
tags: [runge-kutta, order-reduction, stiff, order-conditions]
timestamp: 2026-10-19T12:00:00Z
---

# Stage order

For a [Runge–Kutta method](/definitions/runge-kutta-method.md) $(A,b,c)$ with
$c=A\mathbf 1$, the **$k$-th stage-order residual** is

$$\tau^{(k)}=Ac^{k-1}-\frac{c^k}{k},\qquad k\ge1,$$

with powers of $c$ componentwise; $\tau^{(1)}=A\mathbf 1-c=0$ under the
row-sum convention. The **stage order** is $q=\min\{q_1,q_2\}$, where $q_1$ is
the largest integer with $B(q_1)$ ($b^\top c^{k-1}=1/k$, $k\le q_1$) and $q_2$
the largest with $C(q_2)$ ($\tau^{(k)}=0$, $k\le q_2$)
([Biswas et al. (2023)](/sources/biswas-2023.md), §2, Def. 2.1;
[Biswas et al. (2024)](/sources/biswas-2024.md), Eq. (3), §2.1).

The residual $\tau^{(k)}$ measures how well the internal stages integrate
$t^{k-1}$: the $i$-th entry of $Ac^{k-1}$ is the stage-$i$ quadrature of
$\int_0^{c_i}t^{k-1}\,dt=c_i^k/k$. Stage order $q$ therefore means each stage
value is itself an approximation of $y(t_n+c_ih)$ with local error
$O(h^{q+1})$, and Biswas et al. (2023, §2) note that this bound holds also in
the stiff regime. Biswas et al. (2024, §1.1) recall from Hairer–Wanner
(Thm. IV.15.3) that $\tau^{(k)}=0$ for $k\le\xi$ is necessary for order-$\xi$
convergence on general stiff problems.

## Why it matters: order reduction

On the Prothero–Robinson problem $y'=\lambda(y-g(t))+g'(t)$ (smooth solution $g$, page-local) the stage
local truncation errors are $\sum_k\frac{h^k}{(k-1)!}\tau^{(k)}g^{(k)}(t_n)$
and enter the global error through $zb^\top(I-zA)^{-1}$; in the stiff limit
$z\to-\infty$ the Neumann expansion produces terms $b^\top A^{-j}\tau^{(k)}$
with $j\ge1$ that the order conditions do not annihilate (Biswas et al.
(2023), Eqs. (5)–(8), §2). Methods with $C(q)$ remove these terms up to
$k=q$. The observed behaviour reported by the sources:

* stiff ODEs (Prothero–Robinson): weak-stage-order-1 DIRKs converge at about
  rate $q$ for large $\lvert\lambda\rvert h$ and at $p$ for small $h$ (Biswas
  et al. (2023), §6.1, Fig. 2);
* stiff PDEs: observed accuracy limited to about $\min\{p,q+1\}$
  ([Southworth et al. (2022)](/sources/southworth-2022.md), §2.1;
  [Biswas et al. (2025)](/sources/biswas-2025.md), §1.3, both citing
  Hundsdorfer–Verwer); collocation methods fall to the per-stage truncation
  order, e.g. $s$ for $s$-stage Gauss–Legendre
  ([Farrell et al. (2021)](/sources/farrell-2021.md), §4.1); for Gauss methods the
  two statements disagree, an open contradiction recorded on
  [order reduction](/definitions/order-reduction.md);
* index-2 DAEs: order formally limited to $q$ (Southworth et al. (2022), §2.1).

Farrell et al. (2021, §4.1, Figs. 1–2) observe on a manufactured-solution heat
equation that two-stage Gauss–Legendre degrades from order 4 to "stiff order"
2 while three-stage Radau IIA keeps full accuracy in $L^2$ and $H^1$. The
mechanism and its PDE manifestation (numerical boundary layers) are on
[order reduction](/definitions/order-reduction.md); the
[Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md) is the
model.

## Bounds by method class

| class | stage order | source |
|---|---|---|
| explicit | $\le1$ | Biswas et al. (2025), §1.3 |
| DIRK, irreducible | $\le2$ | Biswas et al. (2023), Thm. 2.2 (proof in its ref. [20]) |
| DIRK with nonsingular $A$ | $\le1$ | Biswas et al. (2023), Thm. 2.2 |
| ESDIRK (one explicit stage) | $\le2$ | Southworth et al. (2022), §2.1; Biswas et al. (2024), Example 7.3 |
| Gauss–Legendre, Radau IIA ($s$ stages) | $s$ | Southworth et al. (2022), §2.1; Farrell et al. (2021), §3.2 |

Biswas et al. (2024, Example 7.3) recover the DIRK and EDIRK bounds from
their weak-stage-order theory: stage order $q$ means $\mathcal K_q=\{0\}$, the Krylov space of
the residuals $\tau^{(1)},\dots,\tau^{(q)}$, and their Lemma 3.13 then gives the bound.
Southworth et al. (2022, §2.1) and Farrell et al. (2021, §1) use the gap
between DIRK ($q\le2$) and fully implicit collocation ($q=s$) as the main
reason to solve the coupled stage systems of
[fully implicit methods](/methods/fully-implicit-runge-kutta.md).

## Relaxation to weak stage order

**Weak stage order** $q_{\mathrm w}$ replaces $\tau^{(k)}=0$ by
$b^\top A^j\tau^{(k)}=0$ for all $j$ and $k\le q_{\mathrm w}$, i.e. the
residuals need only lie in an $A$-invariant subspace orthogonal to $b$; then
$q\le q_{\mathrm w}$ for every method (Biswas et al. (2024), Def. 1.1, §2.2).
For linear problems with time-independent operators this suffices to avoid
order reduction, and DIRKs and explicit methods can have $q_{\mathrm w}$ well
above their stage order (Biswas et al. (2023), §§3–5; Biswas et al. (2025),
Thm. 3.1). See [weak stage order](/definitions/weak-stage-order.md) and
[weak-stage-order barriers](/results/weak-stage-order-barriers.md).

## Qualifications

* Statements that DIRKs are "limited to stage order 1 or 2" (Southworth et
  al. (2022), §2.1) concern classical stage order only; weak stage order up to
  5 is attained by DIRKs (Biswas et al. (2023), App. A).
* The observed-rate rules ($q$, $\min\{p,q+1\}$, $\min\{p,q\}$) mostly refer
  to different problem classes (stiff ODEs, PDEs with boundary data, the "ODE
  problems" of Biswas et al. (2025), §3) and to different norms, and none of the
  sources proves them in general. The exception is Gauss methods on stiff PDEs,
  where $s$ (Farrell et al.) and $s+1$ (Southworth et al.; Biswas et al. 2025)
  are stated for the same class; see the contradiction on
  [order reduction](/definitions/order-reduction.md).
* Biswas et al. (2023, 2025) use $q$ both for stage order and for weak stage
  order; this page writes $q$ for stage order and $q_{\mathrm w}$ for weak
  stage order, as the registry does.
* Farrell et al. (2021, §4.1) state that the $H^1$ error of three-stage Lobatto
  IIIC "stays at order three (which is both the stage order and the spatial
  order in this norm)". The standard classification gives $s$-stage Lobatto
  IIIC only $C(s-1)$, i.e. stage order 2 for $s=3$ *(compiler check, not in the
  sources; the reader of the paper flags the statement as a likely error)*.
* Multirate methods that drop internal consistency have stage order zero
  ([Roberts et al. (2021)](/sources/roberts-2021.md), §7).

# Citations

- [Biswas et al. (2023)](/sources/biswas-2023.md) — §2, Eqs. (5)–(8), Def. 2.1, Thm. 2.2; §6.1, Fig. 2; App. A.
- [Biswas et al. (2024)](/sources/biswas-2024.md) — Eq. (3), §1.1, §2.1–2.2, Def. 1.1, Example 7.3.
- [Biswas et al. (2025)](/sources/biswas-2025.md) — §1.3, §3, Thm. 3.1.
- [Southworth et al. (2022)](/sources/southworth-2022.md) — §2.1 (observed accuracy $\min\{p,q+1\}$; DIRK and IRK stage orders; index-2 DAEs).
- [Farrell et al. (2021)](/sources/farrell-2021.md) — §1, §3.2, §4.1, Figs. 1–2 (stiff order of Gauss–Legendre and Radau IIA).
- [Roberts et al. (2021)](/sources/roberts-2021.md) — §7 (internally inconsistent multirate methods).

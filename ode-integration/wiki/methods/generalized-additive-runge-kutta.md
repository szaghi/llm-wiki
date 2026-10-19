---
type: Method
title: "Generalized additive Runge–Kutta (GARK) methods and internal consistency"
description: "GARK methods give each additive partition of the right-hand side its own stages and coupling matrices; the page states the scheme, internal consistency, the order-condition and stability machinery the sources use, and how IMEX, multirate and explicit methods embed in it."
status: established
aliases: [GARK, generalized-structure additive Runge–Kutta, generalized additively partitioned Runge–Kutta, internal consistency]
tags: [runge-kutta, imex, multirate, order-conditions, stability, gark]
timestamp: 2026-10-19T12:00:00Z
---

# Generalized additive Runge–Kutta (GARK) methods and internal consistency

A generalized additive Runge–Kutta (GARK) method integrates an additively
partitioned problem $y'=f(y)=\sum_q f^{\{q\}}(y)$ by giving every partition $q$
its own set of stage values $Y^{\{q\}}_i$ and coupling every pair of partitions
through its own matrix $A^{\{q,r\}}$. It is the framework of Sandu & Günther, as
recalled by [Roberts et al. (2021)](/sources/roberts-2021.md) (§2, eqs. 2.1–2.3)
and [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md) (§2.1); both use it
to derive the order conditions and the linear stability of
[multirate](/methods/multirate-gark.md) and
[multirate-infinitesimal](/methods/multirate-infinitesimal-methods.md) methods by
writing those methods as GARK schemes. Additive (IMEX) Runge–Kutta methods are
the special case in which all partitions share their stages.

## The scheme

For $P$ partitions with $s^{\{q\}}$ stages each, one step of size $h$ reads

$$\begin{aligned}
Y^{\{q\}}_i&=y_n+h\sum_{r=1}^{P}\sum_{j=1}^{s^{\{r\}}}a^{\{q,r\}}_{ij}\,f^{\{r\}}\big(Y^{\{r\}}_j\big),\qquad i=1,\dots,s^{\{q\}},\\
y_{n+1}&=y_n+h\sum_{q=1}^{P}\sum_{i=1}^{s^{\{q\}}}b^{\{q\}}_i\,f^{\{q\}}\big(Y^{\{q\}}_i\big).
\end{aligned}$$

The diagonal blocks $A^{\{q,q\}}$ are the base methods of the partitions; the
off-diagonal blocks $A^{\{q,r\}}$, $q\ne r$, are the **coupling** coefficients.
The tableau is the block matrix $\mathbf A=(A^{\{q,r\}})$ with weights
$\mathbf b=(b^{\{1\}};\dots;b^{\{P\}})$, of total size
$\mathbf s=\sum_q s^{\{q\}}$ (Roberts et al. 2021, eq. 2.2, two partitions).

**Embedded methods.** An [IMEX or additive Runge–Kutta method](/methods/imex-runge-kutta.md)
is the GARK method whose coupling blocks repeat the tableau of the partition
being evaluated: $A^{\{\mathrm I,\mathrm E\}}=A^{\{\mathrm E,\mathrm E\}}=A^{\mathrm E}$ and
$A^{\{\mathrm E,\mathrm I\}}=A^{\{\mathrm I,\mathrm I\}}=A^{\mathrm I}$, so the two
stage sets coincide (Chinomona & Reynolds 2021, §2.1, citing Sandu & Günther).
Multirate GARK (MrGARK) methods are GARK methods whose fast block repeats a base
method over $m$ micro-steps ([Multirate GARK](/methods/multirate-gark.md)), and
Chinomona & Reynolds (2021, §2.1, eqs. 2.5–2.26) prove that every IMEX-MRI-GARK
method is a GARK method with explicitly given tables
([IMEX-MRI-GARK](/methods/imex-mri-gark.md)). A partitioned Runge–Kutta method is
recovered when $A^{\{\mathrm f,\mathrm f\}}=A^{\{\mathrm s,\mathrm f\}}$,
$A^{\{\mathrm f,\mathrm s\}}=A^{\{\mathrm s,\mathrm s\}}$ and
$b^{\{\mathrm f\}}=b^{\{\mathrm s\}}$ (Roberts et al. 2021, App. C, eq. C.3).

## Internal consistency

A GARK method is **internally consistent** when every row sum of a coupling
block equals the abscissa of the partition being computed:

$$c^{\{q\}}:=A^{\{q,q\}}\mathbf 1=A^{\{q,r\}}\mathbf 1\qquad\text{for all }r$$

(Roberts et al. 2021, eq. 2.3). The condition makes every partition be
evaluated at consistent times. The sources draw three consequences.

- **Fewer order conditions.** Internal consistency collapses many coupling
  conditions onto base-method conditions. Roberts et al. (2021, Thm. 2.1) use it
  to reduce the fourth-order GARK coupling conditions of a compound-fast MrGARK
  method to six (eqs. 2.7a–f); Chinomona & Reynolds (2021, Thms. 2.3–2.4) use it
  to reduce the 26 fourth-order coupling conditions of a three-partition GARK
  scheme to the families (2.41a–e).
- **Stage order.** Dropping internal consistency increases the number of order
  conditions and "limits the stage order to zero" (Roberts et al. 2021, §7).
- **Stability.** Roberts et al. (2021, §5.2) find that "internal consistency
  negatively affects the stability" of the low-order multirate methods they
  construct, and prove that internally consistent multirate methods of order
  exactly one are scalar A-stable for only finitely many multirate ratios
  ([multirate A-stability barriers](/results/multirate-a-stability-barriers.md)).
  The internally inconsistent multirate backward Euler methods, by contrast,
  are scalar L- and algebraically stable for every ratio.

For IMEX-MRI-GARK methods internal consistency is an explicit row-sum condition
on the coupling matrices (Chinomona & Reynolds 2021, Thm. 2.2;
[IMEX-MRI-GARK](/methods/imex-mri-gark.md)).

## Order conditions

GARK order conditions are the Runge–Kutta
[order conditions](/results/runge-kutta-order-conditions.md) written with the
coefficients of the partitions along each path of the rooted tree; an order-$p$
GARK method needs every base method to have order $p$ plus the coupling
conditions. The third-order coupling conditions take the form
$b^{\{q\}\top}A^{\{q,r\}}c^{\{r\}}=\tfrac16$ and the fourth-order ones the
families "3a–4j" of Sandu & Günther, as recalled by Roberts et al. (2021, proof of
Thm. 2.1), who show that for compound-fast methods conditions 3b, 4b, 4d and
4h–4j reduce to base-method conditions and 4g coincides with 4f. Chinomona &
Reynolds (2021, Thm. 2.4) count 26 fourth-order coupling conditions for their
three-partition structure, of which 10 hold automatically by structure (2.48) and
16 reduce to (2.41).

## Linear stability

Two partitions with the scalar test problem
$y'=\lambda^{\{\mathrm f\}}y+\lambda^{\{\mathrm s\}}y$ give the stability function

$$R_{\mathrm{mr}}\big(z^{\{\mathrm f\}},z^{\{\mathrm s\}}\big)=1+\mathbf b^\top Z\big(I-\mathbf AZ\big)^{-1}\mathbf 1,\qquad Z=\operatorname{diag}\big(z^{\{\mathrm f\}}I_{\mathbf s^{\{\mathrm f\}}},\,z^{\{\mathrm s\}}I_{\mathbf s^{\{\mathrm s\}}}\big),$$

with both $z$'s scaled by the full step (Roberts et al. 2021, eq. 3.4, from
Sandu & Günther). Because partitioned stability depends on the basis, a scalar
test is not enough, and Roberts et al. add a $2\times2$ test matrix; the
definitions, the hierarchy between the notions and the joint stability region of
Chinomona & Reynolds are on
[linear stability of multirate methods](/definitions/multirate-linear-stability.md).
Every result there is stated for general GARK methods, not only for multirate
ones; in particular no consistent **decoupled** GARK method is A-stable for the
real 2D test problem (Roberts et al. 2021, Thm. 3.4;
[barriers](/results/multirate-a-stability-barriers.md)).

## Implementation structure

- **Coupled and decoupled.** A decoupled GARK method has implicitness only in its
  base methods, so every coupling stage is available before it is needed; a
  coupled method defines stages of different partitions implicitly in terms of
  each other (Roberts et al. 2021, §2.1, classification after Sarshar et al.).
- **Stacked Newton system.** Writing all stages as
  $\hat Y=\mathbf 1_{\mathbf s}\otimes y_n+h(\mathbf A\otimes I_d)\hat f(\hat Y)$
  gives the Newton matrix $I-h(\mathbf A\otimes I_d)\hat J$ with block-diagonal
  partition Jacobians $\hat J$ (Roberts et al. 2021, §4, eqs. 4.1–4.4).
- **Stage reducibility.** When a coefficient row repeats across partitions the
  unknowns merge: for the ARK tableau with rows $(\tfrac12\,|\,1)$,
  $(\tfrac12\,|\,1)$, $(1\,|\,1)$ the coupled system collapses to dimension $d$
  with matrix $I-\tfrac h2J^{\{1\}}-hJ^{\{2\}}$ (Roberts et al. 2021, §4.3,
  eq. 4.5). A Woodbury identity reduces low-rank couplings in the same way
  (§4.4). The cost model for multirate stage solves is on
  [Multirate GARK](/methods/multirate-gark.md).
- **Linear invariants.** A GARK method does not preserve a linear invariant
  $\zeta^\top y$ in general (let $\zeta$ denote the invariant's weight vector,
  page-local). It does when every partition is conservative on its own,
  $\zeta^\top f^{\{q\}}=0$, or when (C.3) holds (Roberts et al. 2021, App. C).

## Explicit methods written as GARK methods

[Biswas et al. (2025)](/sources/biswas-2025.md) (Thm. 4.1, eq. 4.2) use GARK as
an implementation device. For $y'=Ly+g(t)$, with $g$ a forcing (page-local), an
explicit Runge–Kutta method $(A,b)$ of order $p\ge1$ equals a two-partition GARK
method that evaluates $L$ only $\dim\mathcal Y$ times and $g$ $s$ times per step,
where $\mathcal Y=\operatorname{span}\{b,A^\top b,\dots,(A^\top)^{s-1}b\}$ is the
registry's smallest $A^\top$-invariant subspace containing $b$. The $g$-partition reuses
$(A,b,c)$ with weights $b$; the $L$-partition has weights $e_{\dim\mathcal Y}$ (the source
writes $\hat b$, which the registry reserves for embedded weights) and a tableau built from
$b^\top A^k$. The proof expands
$y_{n+1}=R(hL)y_n+h(b^\top\otimes I)(I-A\otimes hL)^{-1}g(t_n+ch)$. Stage-optimal
[explicit methods with high weak stage order](/methods/explicit-runge-kutta-high-weak-stage-order.md)
have $\dim\mathcal Y=p$, so in $L$-evaluations they cost as much as a $p$-stage
method even though $s=p+q_{\mathrm w}-1$.

## Qualifications

- The order of every GARK-based multirate-infinitesimal method assumes the inner
  (fast) problem is solved exactly or with at least the target order (Chinomona
  & Reynolds 2021, §2.1); the GARK tables are a formal device that represents the
  inner solver as one step of an $s^{\{\mathrm f\}}$-stage Runge–Kutta method.
- Notation differs between the sources: Roberts et al. print bold full-GARK
  coefficients and plain base coefficients, label partitions $\{f\},\{s\}$ and
  scale both stability arguments by the macro step; Chinomona & Reynolds use
  $\{I\},\{E\},\{F\},\{S\}$ and Kronecker-product tables. This page writes both
  in the registry symbols.

# Citations

- [Roberts et al. (2021)](/sources/roberts-2021.md) — §2 (eqs. 2.1–2.3, Thm. 2.1), §3 (eq. 3.4, Thms. 3.1–3.4), §4 (eqs. 4.1–4.5), §5.2, §7, App. C.
- [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md) — §2.1 (eqs. 2.5–2.26), Thms. 2.2–2.4, eqs. 2.41, 2.48–2.49.
- [Biswas et al. (2025)](/sources/biswas-2025.md) — §4, Thm. 4.1, eq. 4.2.

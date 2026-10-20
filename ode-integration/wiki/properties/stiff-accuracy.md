---
type: Property
title: "Stiff accuracy"
description: "A Runge–Kutta method is stiffly accurate when the last row of A equals b, so the step result is the last stage; with invertible A this gives R(∞) = 0 and turns A-stability into L-stability, tightens weak-stage-order barriers, and is imposed on DIRK, Rosenbrock, IMEX, asymptotic-preserving and multirate constructions, though it does not by itself prevent order reduction."
status: established
aliases: [stiffly accurate, SA, stiffly accurate form, globally stiffly accurate, GSA, implicitly stiffly accurate, ISA]
tags: [stiff, runge-kutta, stability, dae, asymptotic-preserving]
timestamp: 2026-10-20T16:00:00Z
---

# Stiff accuracy

A [Runge–Kutta method](/definitions/runge-kutta-method.md) is **stiffly
accurate** if the last row of $A$ equals the weights,

$$a_{sj}=b_j,\qquad j=1,\dots,s,$$

so that $y_{n+1}=Y_s$ and, with $c=A\mathbf 1$, $c_s=1$
([Biswas et al. (2024)](/sources/biswas-2024.md), §2.1;
[Biswas et al. (2023)](/sources/biswas-2023.md), constraint (C.3)). The step
result then satisfies the same stage equation as an internal stage; for a
problem with an algebraic constraint, the result inherits whatever the stage
equation enforces *(compiler remark, not stated in the sources)*. Taddei et al. use it
this way: Radau IIA is stiffly accurate with $c_s=1$, so for their fluid–structure DAE
the step value is the last stage and the separate update (projection) step is dropped
([Taddei et al. (2026)](/sources/taddei-2026.md), §1.1, §3.1 after Eq. (15)).
[Kirby & MacLachlan (2025)](/sources/kirby-2025.md) (§2.1–2.2) use it twice in Irksome: with
Dirichlet data imposed on the stage values, a stiffly accurate method (Radau IIA, Lobatto
IIIC) returns a step value that matches the data at $t_{n+1}$, which other methods do not
guarantee, and the stage-value formulation then skips the final mass-matrix solve; see
[boundary conditions for Runge–Kutta stages](/methods/runge-kutta-stage-boundary-treatment.md).

## Consequence for the stability function

If $A$ is invertible, stiff accuracy gives $b^\top A^{-1}=e_s^\top$, hence
$b^\top A^{-1}\mathbf 1=1$ and $\lim_{z\to\infty}R(z)=1-b^\top A^{-1}\mathbf 1=0$
(Biswas et al. (2024), §2.1; the limit formula is the standard consequence of
$R(z)=1+zb^\top(I-zA)^{-1}\mathbf 1$, *compiler check*). An A-stable stiffly
accurate method with invertible $A$ is therefore L-stable; the
weak-stage-order DIRKs of Biswas et al. (2023, §5.1) and the Rosenbrock method
Rodas5P ([Steinebach (2023)](/sources/steinebach-2023.md), §3) obtain
L-stability this way. See [A- and L-stability](/properties/a-stability.md).

In the rational structure $R=N/D$, stiff accuracy with invertible $A$ gives
$\deg N\le\deg D-1$, which sharpens the order bounds through the parameter
$\delta_{\mathrm{SA}}$ ($=1$ for such methods, $0$ otherwise; page-local):
$\lfloor(p+1+\delta_{\mathrm{SA}})/2\rfloor\le\dim\mathcal Y$ and, for DIRKs,
$p\le\dim\mathcal Y+1-\delta_{\mathrm{SA}}$, with $\mathcal Y$ the smallest
$A^\top$-invariant subspace containing $b$ (Biswas et al. (2024), Thm. 3.9;
see [stability function](/definitions/stability-function.md)).

## Singular $A$: type-II tableaux

The implication fails when $A$ is singular, as for tableaux with an explicit first stage.
Write $A=\begin{pmatrix}0&0\\ \hat a&\hat A\end{pmatrix}$ with $\hat A$ invertible
("type II", or "type CK"; $\hat a$, $\hat A$ page-local). For a stiffly accurate
tableau of this form
$R(\infty)=-\hat e^\top\hat A^{-1}\hat a$, $\hat e$ the last unit vector of
$\mathbb R^{s-1}$ *(compiler derivation from $R(z)=e_s^\top(I-zA)^{-1}\mathbf 1$, valid
under stiff accuracy)*, so L-stability needs the extra condition
$\hat e^\top\hat A^{-1}\hat a=0$; a stiffly accurate tableau of type ARS ($\hat a=0$) is
L-stable ([Orlando & Bonaventura (2025)](/sources/orlando-2025.md), §3.1, Eq. (68);
[Orlando et al. (2025b)](/sources/orlando-2025-b.md), §3.1, Eq. (32); both citing
Boscarino–Russo). The Kennedy–Carpenter ESDIRK used by Orlando & Bonaventura satisfies it
(§5; it holds only with the minus sign that their Table 1 omits, see
[IMEX Runge–Kutta methods](/methods/imex-runge-kutta.md)). The same expression is the
"condition (A)" of [Hu & Shu (2025)](/sources/hu-2025.md): the null vector of $A$ has zero
last component, which they show equivalent to $\hat e^\top\hat A^{-1}\hat a=0$ (Remark 4.2)
and which makes the last stage reach equilibrium as $\varepsilon\to0$ (App. 7.3); that it
coincides with the L-stability condition is a *compiler observation, not in the sources*.

## Effect on weak-stage-order barriers

The same $\delta_{\mathrm{SA}}$ enters the stage-count barriers for
[weak stage order](/definitions/weak-stage-order.md): for a DIRK with $n_c$
distinct abscissae and weak stage order $q_{\mathrm w}\le2n_c-1$,
$s-p+1-\delta_{\mathrm{SA}}\ge\dim\mathcal K_{q_{\mathrm w}}\ge\lfloor q_{\mathrm w}/2\rfloor$ (Biswas
et al. (2023), Thm. 4.2, from Biswas et al. (2024)), and
$\lfloor q_{\mathrm w}/2\rfloor+p\le s+1-\delta_{\mathrm{SA}}$ for non-GEDIRK
DIRKs (Biswas et al. (2024), Thm. 3.2). Stiff accuracy thus costs a stage:
Biswas et al. (2023, §5.1) quote 5 stages as the lower bound for a DIRK with
$p=q_{\mathrm w}=4$, which is the $\delta_{\mathrm{SA}}=0$ value; with stiff
accuracy, imposed in their search, the bound is 6
*(compiler arithmetic from their Thm. 4.2)*. See
[weak-stage-order barriers](/results/weak-stage-order-barriers.md).

## Rosenbrock–Wanner methods

For a [ROW method](/methods/rosenbrock-wanner-method.md) with coefficients
$\alpha_{ij}$, $\gamma_{ij}$ and diagonal $\gamma$, stiff accuracy means
$b_i=\alpha_{si}+\gamma_{si}$ for $i<s$, $b_s=\gamma$ and
$\sum_j\alpha_{sj}=1$ (Steinebach (2023), Eqs. (3.1)–(3.3)). Rodas5P makes both
the 8-stage main method and its 7-stage embedded method stiffly accurate,
and chains the structure so that the argument of the last stage equals the
embedded solution and that of stage 7 equals the solution after stage 6
(§3). See [Rodas5P](/methods/rodas5p.md).

## Stiffly accurate form of IMEX and multirate methods

* **Padding.** Any tableau can be written in stiffly accurate form by
  appending a stage, $c\to(c,1)$, $A\to\begin{pmatrix}A&0\\b^\top&0\end{pmatrix}$,
  which leaves the order conditions unchanged
  ([Chinomona & Reynolds (2021)](/sources/chinomona-2021.md), §2.1). They
  require the base IMEX-ARK of an [IMEX-MRI-GARK method](/methods/imex-mri-gark.md)
  in this form, so that the step result is the last slow stage. The padded
  $A$ is singular, so padding does not give $R(\infty)=0$; the padded method is the
  original one, with the same $R$ *(compiler check, not in the source)*. (Padding appends an explicit *last* stage; the type-II
  condition above concerns an explicit *first* stage and does not apply.)
* **Multirate GARK.** Requiring stiff accuracy in both partitions, together
  with internal consistency and the standard multirate form, determines the
  lightly coupled SDIRK2-based method uniquely; it is only L($69.2^\circ$)-stable
  at $m=2$ and not L($0^\circ$)-stable at $m=6$
  ([Roberts et al. (2021)](/sources/roberts-2021.md), §5.2, Eq. (5.5)). For the
  compound-fast methods of orders 3–4 their design rules include a stiffly
  accurate, L-stable base and the coupling condition
  $A^{\{\mathrm f,\mathrm s,\ell\}}A^{-1}\mathbf 1=\mathbf 1$ for each micro-step $\ell=0,\dots,m-1$ (the source counts $1,\dots,M$),
  which makes the stability function vanish as the slow eigenvalue tends to
  $-\infty$ (§3.4, Eq. (3.18), §5.3). The bases are the L-stable stiffly
  accurate SDIRK2 of Alexander, $A=\begin{pmatrix}\gamma&0\\1-\gamma&\gamma\end{pmatrix}$,
  $b=(1-\gamma,\gamma)$, $\gamma=1-1/\sqrt2$ (Eq. (5.4)), Alexander's 3-stage
  SDIRK3 (App. A) and a new 5-stage stiffly accurate L-stable SDIRK4 with
  $\gamma=\tfrac14$, $c=(\tfrac14,1,\tfrac25,\tfrac7{11},1)$ (App. B, Eq. (B.1)).
  See [multirate GARK methods](/methods/multirate-gark.md).

## Stiff accuracy in IMEX and asymptotic-preserving schemes

For an IMEX pair $(A^{\mathrm E},b^{\mathrm E})$, $(A^{\mathrm I},b^{\mathrm I})$ the AP
literature distinguishes **implicitly stiffly accurate** (ISA), $a^{\mathrm I}_{sj}=b^{\mathrm I}_j$,
from **globally stiffly accurate** (GSA), which adds $a^{\mathrm E}_{sj}=b^{\mathrm E}_j$
and gives $Y_s=y_{n+1}$ (Hu & Shu 2025, footnote 1). The sources use the two levels for
different purposes:

* **Stability.** In Hu & Shu's uniform-stability proof for hyperbolic relaxation, ISA
  removes the stiff term from the passage between the last stage and $y_{n+1}$, so a
  non-GSA pair needs only one extra nonstiff energy estimate (§3, Eq. (3.15)).
* **AP limit.** For initial data in equilibrium to $O(\varepsilon)$, a type-CK ISA pair that
  is GSA is AP with full order in the limit (recalled from Dimarco–Pareschi; ARS(2,2,2) and
  ARS(4,4,3) qualify); without GSA, condition (A) plus order conditions on
  $b^{\mathrm E}-A^{\mathrm E}_{s\cdot}$ suffice (Hu & Shu 2025, Thm. 7.4, formal).
  BHR(5,5,3)\* is ISA, not GSA, and AP.
* **Practice.** [Boscheri & Pareschi (2021)](/sources/boscheri-2021.md) (§3.4.1) and
  [Boscheri & Thomann (2024)](/sources/boscheri-2024.md) (§3.3) call a stiffly accurate
  implicit part "crucial for assuring asymptotic consistency and accuracy"; the former use
  their non-stiffly-accurate SSP3(4,3,3) pair only at high Mach number. With
  $b^{\mathrm E}=b^{\mathrm I}$ and a stiffly accurate implicit part, the
  [semi-implicit IMEX](/methods/semi-implicit-imex-runge-kutta.md) update is the last
  implicit stage (Boscheri & Thomann 2024, §3.3). Boscheri & Thomann call their LSDIRK2
  pair stiffly accurate, but its explicit last row differs from $b$, so it is ISA and not
  GSA. Orlando et al. (2025b, Def. 3.2) define an IMEX pair as stiffly accurate when its
  implicit part is, and use only such pairs.
* **Accuracy.** Orlando & Bonaventura (2025, §3.1) link asymptotic accuracy to L-stability
  and obtain L-stability through stiff accuracy (type I and ARS) or through the extra
  condition above (type II).

## Homonym: "stiffly accurate" exponential integrators

In the exponential-integrator literature "stiffly accurate" names a different property.
[Luan (2021)](/sources/luan-2021.md) (§1, §2.1) and
[Dallerit & Tokman (2025)](/sources/dallerit-2025.md) (§1, §7) call an exponential
Runge–Kutta or Rosenbrock method stiffly accurate when it satisfies the **stiff order
conditions** of Hochbruck and Ostermann. Those conditions give error bounds independent of
the norm of the stiff operator; see
[stiff order conditions of exponential Runge–Kutta methods](/results/exponential-runge-kutta-stiff-order-conditions.md).
Neither source uses the tableau property $a_{sj}=b_j$ of this page, and the coefficients of an
exponential method are matrix functions, for which that property is not defined in these
sources. The two meanings are unrelated, not two views of one property, and the sources are
cited here only for the name.

## What stiff accuracy does not do

Stiff accuracy is not sufficient to avoid [order reduction](/definitions/order-reduction.md).
Rodas5 is stiffly accurate, yet drops to order 1 on the stiff
[Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md), to order 2
on a semi-discretized parabolic problem and to order 1 on index-2 DAEs, while
Rodas5P, with the same structure, reaches order 3, about 3.9 and 2 because it
additionally satisfies Scholz's Prothero–Robinson conditions and the index-2
condition (Steinebach (2023), Table 1, Tables 6–8). Among DIRKs, the
Hairer–Wanner DIRK-(5,4,1) is stiffly accurate and the Kennedy–Carpenter
DIRK-(5,5,1) is not; both have weak stage order 1 and both show order
reduction (Biswas et al. (2023), §6, Fig. 2). The remedy is
[weak stage order](/definitions/weak-stage-order.md), imposed together with
stiff accuracy in the DIRK-(7,4,4), DIRK-(12,5,4) and DIRK-(12,5,5) schemes
(Biswas et al. (2023), App. A).

Fully implicit Radau IIA methods, stiffly accurate and of formal order $2s-1$, give
least-squares temporal rates of only about 2.1, 2.4 and 3.5 for $s=2,3,4$ on an
incompressible fluid–structure DAE; the authors attribute the shortfall to the DAE
structure and the interaction with the spatial discretization, mesh motion and interface
coupling (Taddei et al. 2026, §5.1.1, Table 1). Hu & Shu (2025, §6) show the IMEX analogue:
ARS(4,4,3), globally stiffly accurate, is only uniformly second order on a relaxation
system, because it does not meet the conditions of their uniform-third-order theorem, which
include [stage order](/definitions/stage-order.md) 2 on the stages after the second
(Thm. 5.1).

# Citations

- [Biswas et al. (2024)](/sources/biswas-2024.md) — §2.1 (definition, $R(\infty)=0$), Thm. 3.2, Thm. 3.9.
- [Biswas et al. (2023)](/sources/biswas-2023.md) — constraint (C.3), Thm. 4.2, §5.1, §6, Fig. 2, App. A.
- [Steinebach (2023)](/sources/steinebach-2023.md) — Eqs. (3.1)–(3.3), §3, Table 1, Tables 6–8.
- [Roberts et al. (2021)](/sources/roberts-2021.md) — Eq. (3.18), §3.4, Eqs. (5.4)–(5.5), §5.2–5.3, Apps. A–B.
- [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md) — §2.1 (stiffly accurate padding of the base IMEX-ARK).
- [Hu & Shu (2025)](/sources/hu-2025.md) — §2 footnote 1 (ISA, GSA), §3 (Eq. (3.15)), Remark 4.2 (condition (A)), Thm. 5.1, §6, App. 7.3 (Thm. 7.4); arXiv v1.
- [Orlando & Bonaventura (2025)](/sources/orlando-2025.md) — §3.1 (Eq. (68)), §5 (Tables 1–2); HAL v2.
- [Orlando et al. (2025b)](/sources/orlando-2025-b.md) — §3.1 (Def. 3.2, Eq. (32)); arXiv v5.
- [Boscheri & Pareschi (2021)](/sources/boscheri-2021.md) — §3.4.1 (Eqs. (79)–(81)); arXiv v1.
- [Boscheri & Thomann (2024)](/sources/boscheri-2024.md) — §3.3 (Eq. (39)); arXiv v1.
- [Taddei et al. (2026)](/sources/taddei-2026.md) — §1.1, §3.1 (Eq. (15)), §5.1.1 (Table 1); arXiv v1.
- [Luan (2021)](/sources/luan-2021.md) — §1, §2.1 (homonym: "stiffly accurate" for exponential methods satisfying the stiff order conditions); arXiv v1.
- [Dallerit & Tokman (2025)](/sources/dallerit-2025.md) — §1, §7 (the same homonym).
- [Kirby & MacLachlan (2025)](/sources/kirby-2025.md) — §2.1–2.2 (step value matches stage-value boundary data; mass-matrix solve skipped).

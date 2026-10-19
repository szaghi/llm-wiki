---
type: Property
title: "Stiff accuracy"
description: "A Runge–Kutta method is stiffly accurate when the last row of A equals b, so the step result is the last stage; with invertible A this gives R(∞) = 0 and turns A-stability into L-stability, tightens weak-stage-order barriers, and is imposed on DIRK, Rosenbrock, IMEX and multirate constructions, though it does not by itself prevent order reduction."
status: established
aliases: [stiffly accurate, SA, stiffly accurate form, globally stiffly accurate]
tags: [stiff, runge-kutta, stability, dae]
timestamp: 2026-10-19T12:00:00Z
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
equation enforces *(compiler remark, not stated in the sources)*.

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
  $A$ is singular, so padding does not give $R(\infty)=0$
  *(compiler remark)*.
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

# Citations

- [Biswas et al. (2024)](/sources/biswas-2024.md) — §2.1 (definition, $R(\infty)=0$), Thm. 3.2, Thm. 3.9.
- [Biswas et al. (2023)](/sources/biswas-2023.md) — constraint (C.3), Thm. 4.2, §5.1, §6, Fig. 2, App. A.
- [Steinebach (2023)](/sources/steinebach-2023.md) — Eqs. (3.1)–(3.3), §3, Table 1, Tables 6–8.
- [Roberts et al. (2021)](/sources/roberts-2021.md) — Eq. (3.18), §3.4, Eqs. (5.4)–(5.5), §5.2–5.3, Apps. A–B.
- [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md) — §2.1 (stiffly accurate padding of the base IMEX-ARK).

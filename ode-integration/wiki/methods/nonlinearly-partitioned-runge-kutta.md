---
type: Method
title: "Nonlinearly partitioned Runge–Kutta (NPRK) methods"
description: "NPRK methods integrate y' = F(y,y) for any two-argument splitting F of the right-hand side, giving each argument its own implicitness through a rank-3 coefficient tensor; the page gives the scheme, its reductions to RK, ARK, PRK and SIRK, the order-condition route, IMEX and IMIM stability notions, the named IMEX-NPRK methods, and the multirate extension MR-NPRK with its L-stability theorem."
status: established
aliases: [NPRK, IMEX-NPRK, IMIM-NPRK, MR-NPRK, multirate NPRK, nonlinearly partitioned IMEX, sequentially coupled NPRK, implicitly wrapped MR-NPRK]
tags: [runge-kutta, imex, multirate, order-conditions, stability, stiff]
timestamp: 2026-10-20T06:18:00Z
---

# Nonlinearly partitioned Runge–Kutta (NPRK) methods

A **nonlinear partition** of $y'=f(y)$ is any function $F(u,v)$ with $F(y,y)=f(y)$
for all $y$ (registry notation; the sources write $G$ for $f$). Examples: $F(u,v)=uv$
for $f(y)=y^2$; for viscous Burgers', $F(u,v)=\varepsilon Du+\operatorname{diag}(v)Au$
with $D$, $A$ the discrete diffusion and advection matrices (page-local). A
nonlinearly partitioned Runge–Kutta (NPRK) method, introduced by
[Buvoli & Southworth (2025)](/sources/buvoli-2025.md), evaluates $F$ at pairs of
stage values:

$$Y_i=y_n+h\sum_{j=1}^s\sum_{k=1}^sa_{ijk}F(Y_j,Y_k),\qquad y_{n+1}=y_n+h\sum_{i=1}^s\sum_{j=1}^sb_{ij}F(Y_i,Y_j),$$

with a rank-3 coefficient tensor $a_{ijk}$ and a weight matrix $b_{ij}$ (page-local
symbols; $j$ indexes the first argument, $k$ the second). Each argument can then
receive its own degree of implicitness: implicit in $u$ and explicit in $v$ makes the
stage solve linear whenever $F$ is linear in $u$, which lifts the classical
"lagged-coefficient" (Picard) linearization to high order (Buvoli & Southworth 2025,
§1, §4, eq. 4.2).

## Underlying methods and reductions

Every NPRK method has two **underlying** Runge–Kutta methods, obtained when $F$
depends on one argument only (Def. 4.1, eqs. 4.3–4.4; also
[Buvoli et al. (2026)](/sources/buvoli-2026.md), Def. 1.1):

$$a^{\{1\}}_{ij}=\sum_ka_{ijk},\quad b^{\{1\}}_i=\sum_jb_{ij};\qquad a^{\{2\}}_{ik}=\sum_ja_{ijk},\quad b^{\{2\}}_j=\sum_ib_{ij};\qquad c^{\{1\}}=c^{\{2\}}.$$

- A diagonal tensor ($a_{ijk}=0$ for $j\ne k$, $b_{ij}=0$ for $i\ne j$) gives a classical
  Runge–Kutta method.
- An additive partition $F(u,v)=f^{\{1\}}(u)+f^{\{2\}}(v)$ gives the
  [ARK/IMEX method](/methods/imex-runge-kutta.md) built from the underlying methods, with
  shared abscissae; a component partition gives a partitioned Runge–Kutta (PRK) method
  (Buvoli et al. 2026, §1.2). An order-$p$ NPRK method therefore needs order-$p$ ARK
  conditions on its underlying methods, plus conditions for the nonlinear coupling.
- Every $s$-stage [semi-implicit (linearly implicit) IMEX method](/methods/semi-implicit-imex-runge-kutta.md)
  of Boscarino et al., with tables $(A^{\mathrm I},b)$, $(A^{\mathrm E},b)$, is a
  $2s$-stage NPRK method with $a_{2i-1,2j,2j-1}=a^{\mathrm E}_{ij}$,
  $a_{2i,2j,2j-1}=a^{\mathrm I}_{ij}$, $b_{2i,2i-1}=b_i$ (eq. 4.6). NPRK needs no
  alternation of explicit and implicit stages and reaches high order with fewer stages.
  Buvoli & Southworth call SIRK "to our knowledge the only general class of methods in
  the literature" applicable to $y'=F(y,y)$ before NPRK (§2.2); GARK "does not address"
  nonlinear partitions (§2.1.4).
- Nonlinearly partitioned IMEX Euler, $y_{n+1}=y_n+hF(y_{n+1},y_n)$, is the standard
  first-order time lagging of opacities in thermal radiation transport (Larsen), as both
  papers recall (Buvoli & Southworth 2025, §7.2; Buvoli et al. 2026, eq. 1.4).
- Rosenbrock methods linearize the whole problem uniformly; they cannot mix explicit,
  implicit and linearly implicit treatment inside one nonlinear term (2025, §2.3; see
  [Rosenbrock–Wanner methods](/methods/rosenbrock-wanner-method.md)).

The **implicitness classes** follow from the sparsity of $a_{ijk}$ (Table 4.1): IMEX
(DIRK in $u$, explicit in $v$) has $a_{ijk}=0$ for $j>i$ or $k\ge i$; IMIM (implicit
in both arguments, **decoupled**: the unknown of a stage appears in one argument only)
is the other class pursued.

## Order conditions

Buvoli & Southworth (2025) derive conditions for the restricted diagonally implicit
ansatz (4.7) by two equivalences:

- **Proposition 4.3** (proved, App. A): every such $s$-stage method equals a
  **sequentially coupled** method with $\hat s\ge s$ stages, which uses only
  $F(Y_j,Y_{j-1})$.
- **Proposition 4.4** (proved): an $s$-stage sequentially coupled method is an
  $(s-1)$-stage PRK method with equal weights applied to $z'=F(z,w)$, $w'=F(z,w)$,
  $z_n=w_n=y_n$, with $a_{ij}=a_{i+1,j+1,j}$, $\hat a_{ij}=a_{i,j+1,j}$,
  $b_i=\hat b_i=b_{i+1,i}$ (page-local hats for the second PRK tableau).

PRK theory then gives second order iff both PRK tableaux have order 2, and three extra
coupling conditions at order 3 (Table 4.3); the third-order residual vector $r^{(3)}$ of
the seven order-3 conditions serves as error constant (page-local). The general
conditions, by edge-coloured rooted trees, are in a companion paper of Tran, Southworth
& Buvoli, as recalled by Buvoli et al. (2026, §2.2, App. B): up to order 3 they are the
ARK conditions on the underlying methods plus **one** nonlinear-coupling condition, for
the tree with elementary differential $F_{12}[F,F]$ (mixed second derivative),
$\sum b_{ij}a_{ikl}a_{juv}=\tfrac13$, which cannot be written through the underlying
methods; second order holds iff both underlying methods are second order. See
[Runge–Kutta order conditions](/results/runge-kutta-order-conditions.md).

## Linear stability

On the **partitioned Dahlquist problem** $y'=F(y,y)$, $F(u,v)=\lambda_1u+\lambda_2v$,
$z_r=h\lambda_r$, an NPRK method has the ARK stability function

$$R(z_1,z_2)=\frac{\det\big(I-z_1A^{\{1\}}-z_2A^{\{2\}}+\mathbf 1(z_1b^{\{1\}}+z_2b^{\{2\}})^\top\big)}{\det\big(I-z_1A^{\{1\}}-z_2A^{\{2\}}\big)}$$

(2025, eq. 4.18; 2026, eq. 2.7; page-local $R(z_1,z_2)$). It models a nonlinear system
whose two partial Jacobians are simultaneously diagonalizable (2025, SM2). Real
semi-discretizations have conjugate-symmetric spectra, so the sources plot
$\mathcal P=\{(z_1,z_2):\max(|R(z_1,z_2)|,|R(\bar z_1,z_2)|)\le1\}$ in slices
$\mathcal P(z_1)$; $\arg z_1=\pi/2$ models skew-symmetric advection, $\arg z_1=\pi$
symmetric positive definite diffusion. Notions (page-local names):

- **IMIM A-stable**: $\{(z_1,z_2):\lvert R(z_1,z_2)\rvert\le1\}\supseteq\mathbb C^-\times\mathbb C^-$; L-stable if also
  $R\to0$ as $|z_1|\to\infty$ and as $|z_2|\to\infty$ (2025, eqs. 4.20–4.21). An NPRK
  method implicit in only one argument cannot be A-stable, since $R(0,z_2)$ is an
  explicit Runge–Kutta stability polynomial (2025, §4.5.2; 2026, §3.1).
- **IMEX A-/L-stable in the stiff $z_j$ limit**: $\lim_{|z_j|\to\infty}|R(z_1,z_2)|\le1$
  (respectively $=0$) (2025, eqs. 4.22–4.23).
- **Stable in the coupled stiff $z_2$ limit** (new in 2025, eqs. 4.24–4.27): with
  $R_\infty(\kappa)=\lim_{|z_1|\to\infty}R(z_1,\kappa z_1)$ (page-local), require
  $|R_\infty(\kappa)|\le1$ for $|\kappa|\le1$, i.e. stability when the explicitly treated
  argument is as stiff as a fraction of the implicit one. For a diagonally implicit IMEX
  ARK with nonzero implicit diagonal, $R_\infty$ is a polynomial, so by the maximum
  modulus principle the condition is $\Upsilon(\theta)=|R_\infty(e^{i\theta})|^2\le1$ on
  $[0,2\pi)$, and $\Upsilon$ is a cosine series (Props. SM3.1–SM3.2, Remark 2; page-local
  $\Upsilon$, the source's $\gamma(\theta)$).

These notions use a different test problem and different limits from the joint regions
of [linear stability of multirate methods](/definitions/multirate-linear-stability.md);
the two families of definitions are not interchangeable.

## Named single-rate methods (Buvoli & Southworth 2025, §5, SM4–SM5)

Names IMEX-NPRK$p[sq]$: order $p$, $s$ stages, $q$ implicit solves; Si singly implicit
(diagonal $\gamma$, page-local), Sa stiffly accurate ($b_{i,i-1}=a_{s,i,i-1}$).

| Method | Notes |
|---|---|
| IMEX-NPRK1[21] (Euler) | $R=(1+z_2)/(1-z_1)$; L-stable in $z_1$, stable in the coupled stiff $z_2$ limit |
| IMEX-NPRK2[31] (midpoint) | implicit/explicit midpoint underlying; $\lim_{|z_1|\to\infty}R=-(z_2+1)$, not L-stable; only for $F$ nonstiff in $v$ |
| IMEX-NPRK2[32]a / b | one-parameter L-stable family, $b_{32}=1\mp1/\sqrt2$; (a) stable in the coupled limit, $\lVert r^{(3)}\rVert_2\approx4.159$; (b) not, $\approx0.302$ |
| IMEX-NPRK2[42]a / b | same stability regions as [32]a/b, $\lVert r^{(3)}\rVert_2\approx1.696$ and $0.191$, one more stored stage |
| IMEX-NPRK2[43]-Si, -SiSa | SiSa: $\gamma=0.386585$, $\lVert r^{(3)}\rVert_2=0.500$, $R_\infty(\kappa)=-\kappa^3$ for the stiffly accurate family |
| IMEX-NPRK3[54]-Sa | rational coefficients, stable in the coupled limit; at least five stages needed for order 3 in this ansatz (stated, not proved) |
| IMEX-NPRK3[54]-Si | $\gamma=0.54$, not stable in the coupled limit |
| IMIM midpoint, IMIM midpoint/Crank–Nicolson | $b_{23}\in\{1,\tfrac12\}$; $R$ separates as $g(z_1)g(z_2)$ with the implicit-midpoint factor, so A-stable in both variables |

Algorithm 6.1 implements a sequentially coupled IMEX-NPRK step for
$F(u,v)=F_{\mathrm E}(v)+F_{\mathrm I}(u,v)$ in stage-value form: the implicit operator's
action is recovered after each solve as $(Y-r_j)/a_{j,j,j-1}$, so codes that can solve
but not apply the operator (transport sweeps) need no assembly.

## Multirate NPRK (Buvoli et al. 2026)

An NPRK method is **multirate** (MR-NPRK) when its two *reduced* underlying methods
(redundant stages removed, Butcher's reducibility) have different stage counts
$s^{\{1\}}\ne s^{\{2\}}$ (Defs. 2.3, 2.6); no new method class is needed, and every
MR-NPRK method is also a multirate ARK and a multirate PRK method. Buvoli et al. argue
that existing [multirate GARK](/methods/multirate-gark.md) and
[multirate infinitesimal](/methods/multirate-infinitesimal-methods.md) methods assume a
linear (additive or component) separation of scales, which fails in radiation transport,
where material coefficients of stiff processes depend on nonstiff variables (§1).

- **Timescale coupling** (§2.1, Table 1, Fig. 1): fully decoupled, $1\to2$, $2\to1$ or
  fully coupled, according to which irreducible stages may enter which argument; each
  class fixes zero patterns of $a_{ijk}$, and overlapping stage sets force full coupling
  (Prop. SM A.2).
- **Theorem 3.2 (L-stability in the stiff $z_1$ limit).** An IMEX MR-NPRK method with
  $\lim_{|z_1|\to\infty}R(z_1,z_2)=0$ results if it is (i) fully decoupled or $1\to2$
  coupled, (ii) stiffly accurate, (iii) its reduced implicit method is a DIRK with nonzero
  diagonal. The proof shows the denominator has degree $s^{\{1\}}$ and the numerator
  degree at most $s^{\{1\}}-1$ in $z_1$ (App. A). Its practical value decays as $s^{\{2\}}$
  grows: damping needs $|z_1|\gg|z_2|^{s^{\{2\}}/s^{\{1\}}}$, and the step must still lie in
  the explicit region, which grows only linearly in $s^{\{2\}}$ (§3.1.1, Fig. 2).
- **Implicitly wrapped methods** (§3.2): all implicit stages placed before and after an
  arbitrary user-chosen explicit Runge–Kutta method; excluding the solves, the step is one
  explicit step of the modified ODE $w'=F(Y_2,w)$. MR-NPRK2 ($s=s^{\{2\}}+2$, fully
  decoupled, any explicit method of order $\ge2$) needs the SDIRK coefficient
  $(2\pm\sqrt2)/2$; MR-NPRK3 ($s=s^{\{2\}}+3$, $1\to2$ coupled, explicit order $\ge3$) uses
  Butcher's three-stage L-stable stiffly accurate SDIRK with diagonal
  $0.43586652150845899941\ldots$ and three remaining conditions, each fixed by one free
  coefficient (App. C.2). One coupling coefficient grows without bound as $s^{\{2\}}\to\infty$;
  an alternative with bounded coefficients doubles the explicit cost (Remark 3.3, C.46).
  The fast explicit method is an $m$-fold composition of SSP2 or SSP3 (same storage as the
  base method; see [SSP RK](/methods/strong-stability-preserving-runge-kutta.md)).

## Numerical evidence

- **Viscous [Burgers](/benchmarks/burgers-equation.md)** (2025, §3, §7.1): nonlinearly
  partitioned IMEX Euler matches implicit and Rosenbrock Euler in accuracy and stability
  with one linear solve and no exact Jacobian, while additive IMEX Euler degrades to
  explicit Euler as $\varepsilon\to0$. On the non-conservative partition all seven
  IMEX-NPRK methods are stable at all steps; on the conservative partition only those
  stable in the coupled stiff $z_2$ limit (1[21], 2[42]a, 2[43]-SiSa, 3[54]-Sa) survive large
  steps, and all converge at design order.
- **Gray thermal radiation transport, Marshak wave** (2025, §7.2): on the fine mesh every
  second-order NPRK method is stable at much larger steps than H-LDIRK2(2,2,2) and
  SSP-LDIRK2(3,3,2) in Boscarino form; on the coarse mesh the IMEX partition suffers
  complete [order reduction](/definitions/order-reduction.md) to first order and
  NPRK2[43]-SiSa keeps second order at the largest steps; NPRK3[54]-Si mostly fails from
  temperature negativities.
- **Burgers with nonlinear diffusion** $|u|^{1/2}$, WENO5 advection (2026, §4): the
  partition $F(u,v)=a(x)(k(v)u_x)_x+b(x)(v^2)_x$ needs only linear solves; MR-NPRK2/3 reach
  orders 2 and 3, are more accurate than single-rate IMEX-NPRK at fixed step, stable at
  larger steps than explicit SSP, and about 4× faster than single-rate NPRK at moderate
  precision (an implicit solve costing four function evaluations).

## Qualifications

- Order conditions in Buvoli & Southworth (2025) cover only the restricted ansatz (4.7);
  minimum stage counts are stated from Mathematica solves, not proved.
- Printed slips (arXiv versions read): 2025 prints the Euler limit as $R_\infty=\kappa$
  where $R(z_1,\kappa z_1)\to-\kappa$, swaps the global/local labels in the Fig. SM4.1
  caption (the equations (5.6), SM4.21 are right), and Algorithm 6.1 adds the weights
  inside the wrong loop; 2026 prints the SDIRK choice as $(\sqrt2\pm2)/2$ in a pseudocode
  line against $(2\pm\sqrt2)/2$ in (3.7). Details are on the Source pages.

# Citations

- [Buvoli & Southworth (2025)](/sources/buvoli-2025.md) — §1, §2.2–2.3, §3, §4 (eqs. 4.2–4.27, Def. 4.1, Props. 4.3–4.4, Table 4.1, Table 4.3), §5 (eqs. 5.2–5.19), §6 (Algorithm 6.1), §7, SM2–SM5, App. A.
- [Buvoli et al. (2026)](/sources/buvoli-2026.md) — §1 (eqs. 1.2–1.9, Def. 1.1), §2 (Defs. 2.3–2.6, Tables 1–2, eq. 2.7), §3 (Thm. 3.2, eqs. 3.3–3.13, Table 3, Remark 3.3), §4, Apps. A–C.

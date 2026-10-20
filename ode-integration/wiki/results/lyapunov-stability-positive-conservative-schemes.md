---
type: Result
title: "Lyapunov stability of steady states of positive, conservative time integrators"
description: "Izgin, Kopecz and Meister prove that a positive, conservative map on two-component systems with a line of fixed points has a stable fixed point when the non-unit Jacobian eigenvalue has modulus below one, and use it to show MPRK22(α) stable for every step and MPRK22ncs(α) stable for every step only when α ≥ 1."
status: established
aliases: [Lyapunov stability of MPRK, centre manifold stability of Patankar schemes, stability function of MPRK22, unconditional stability of MPRK22, Izgin–Kopecz–Meister theorem]
tags: [stability, positivity, structure-preserving, stiff]
timestamp: 2026-10-20T14:00:00Z
---

# Lyapunov stability of steady states of positive, conservative time integrators

[Modified Patankar methods](/methods/modified-patankar-methods.md) cannot be tested on
the Dahlquist equation $y'=\lambda y$, because a complex term $\lambda y$ has no
production–destruction reading, and they are nonlinear even on linear problems, so the
[stability function](/definitions/stability-function.md) of linear stability theory does
not exist for them ([Izgin et al. 2022](/sources/izgin-2022.md), §1, Eq. (1)). Izgin,
Kopecz and Meister replace the test equation by the most general positive and
conservative linear $2\times2$
[production–destruction system](/definitions/production-destruction-system.md)

$$y'=\begin{pmatrix}-a&b\\a&-b\end{pmatrix}y,\qquad a,b\ge0,\quad a+b>0$$

(page-local $a$, $b$; Eq. (3)), with eigenvalues $\lambda=-(a+b)$ and $0$, and study
the **Lyapunov stability of its steady states** as fixed points of the numerical map. The
result is a general criterion for positive and conservative maps (Thm. 2.9) and its
application to the second-order MPRK22 families.

## Why the steady states are non-hyperbolic

The steady states of the test system fill the ray $y^*=\theta(b,a)^\top$, $\theta>0$
(page-local $\theta$); each is Lyapunov stable but not asymptotically stable, since every
neighbourhood contains other steady states, and the exact solution approaches
$\frac{y_1(0)+y_2(0)}{a+b}(b,a)^\top$ monotonically along the conserved line
$y_1+y_2=\text{const}$ (§2, Eq. (5)). A fixed point $y^*$ of a map $y_{n+1}=g(y_n)$ is
Lyapunov stable if iterates starting close stay close, asymptotically stable if they also
converge, and unstable otherwise (Defs. 2.1–2.2). Linearization decides only
hyperbolic fixed points, those without Jacobian eigenvalues of modulus one; a positive,
conservative scheme with a line of fixed points always has the eigenvalue 1, so the
nonlinear terms must be controlled (Thm. 2.3, Def. 2.4, as recalled from Stuart &
Humphries).

## The theorem

**Theorem** (Izgin et al. 2022, Thm. 2.9). Let $g\in C^2(\mathbb R^2_{>0})$ map positive
states to positive states, let $y^*>0$ be a fixed point such that every $ry^*$, $r>0$, is
a fixed point, and let $g$ conserve the 1-norm, $\lVert g(y)\rVert_1=\lVert y\rVert_1$.
Then the Jacobian has spectrum $\{1,R\}$, $R\in\mathbb R$ (page-local), with
$Dg(y^*)y^*=y^*$ and $Dg(y^*)(1,-1)^\top=R\,(1,-1)^\top$, and

- (a) if $\lvert R\rvert<1$, $y^*$ is Lyapunov stable;
- (b) if $y^*$ is stable, there is $\delta>0$ such that every start with
  $\lVert y_0\rVert_1=\lVert y^*\rVert_1$ and $\lVert y_0-y^*\rVert<\delta$ gives
  $y_n\to y^*$.

The proof changes variables to the eigenbasis $\{y^*,(1,-1)^\top\}$, in which the map has
the normal form of the centre manifold theorem for maps with centre eigenvalue 1 and
stable eigenvalue $R$. Conservation makes the first new coordinate invariant, so the map
restricted to the centre manifold is the identity, which is stable, and the centre
manifold reduction carries stability back to $g$; for (b) the centre manifold is the line
of fixed points itself (§2, Thms. 2.5–2.7, Eqs. (11)–(20)). If $\lvert R\rvert>1$ the
fixed point is unstable by linearization (Thm. 2.3). Nothing is claimed for
$\lvert R\rvert=1$. The theorem applies to any positive and conservative scheme, not only
to Patankar methods; the authors present it as the first stability criterion for such
schemes on this test (§2, §5).

For a Runge–Kutta method the same construction gives the eigenvalues $1$ and
$R(z_a+z_b)$, with $R$ the ordinary stability function and $z_a=-ha$, $z_b=-hb$
(page-local), so the non-unit eigenvalue plays the role of the stability function (Remark
3.7). For a nonlinear scheme it can depend on $z_a$ and $z_b$ separately.

## Application to MPRK22

The second-order family of Kopecz and Meister, written by Izgin et al. with a switch
$\gamma\in\{0,1\}$ (page-local; distinct from the registry's Rosenbrock $\gamma$), has
stages

$$Y_{2,i}=y^n_i+\alpha h\sum_j\Bigl((1-\gamma)p_{ij}(y_n)+\gamma\,p_{ij}(y_n)\frac{Y_{2,j}}{y^n_j}-d_{ij}(y_n)\frac{Y_{2,i}}{y^n_i}\Bigr),$$

and the update of MPRK(2,2,α) on the
[modified Patankar page](/methods/modified-patankar-methods.md) with denominators
$\varpi_i=Y_{2,i}^{1/\alpha}(y^n_i)^{1-1/\alpha}$, $\alpha\ge\tfrac12$ (Eq. (6); registry
§8 notation). $\gamma=1$ gives **MPRK22(α)**, whose stage is itself conservative;
$\gamma=0$ gives **MPRK22ncs(α)** ("non-conservative stages"), whose stage leaves the
production unweighted. On the test system the scheme is a closed-form map
(Prop. 3.1, by a rank-one inverse formula), every positive steady state is a fixed point
and the map is $C^\infty$ (Lemmas 3.3–3.4), and the Jacobian at $y^*$ is
$I+\frac{h}{1+h(a+b)}A\bigl(I+\frac1{2\alpha}(I-B_\gamma)\bigr)$ with $B_\gamma$ the linear
stage map (page-local; Lemma 3.5, Eq. (41)). The non-unit eigenvalues are (Lemma 3.6,
Eqs. (43a)–(43b)), with $z=z_a+z_b=h\lambda$:

$$R_1(z)=\frac{2-2\alpha z-z^2}{2(1-z)(1-\alpha z)},\qquad R_0(z_a,z_b)=\frac{2-z\bigl(\frac{z_a}{1-\alpha z_a}+\frac{z_b}{1-\alpha z_b}\bigr)}{2(1-z)}$$

(page-local $R_1$, $R_0$ for $\gamma=1,0$). $R_1$ depends only on $z$, $R_0$ on both
arguments.

- **MPRK22(α) is unconditionally stable** for $\alpha\ge\tfrac12$: $\lvert R_1(z)\rvert<1$
  for every $z<0$ (Lemma 3.8), so every positive steady state is a stable fixed point and
  attracts nearby starts on its 1-norm level for every $h>0$ (Cor. 3.9).
- **MPRK22ncs(α)**: $R_0$ is symmetric, increasing in each argument, and
  $-\frac1\alpha<R_0<1$, with limit $-\frac1\alpha$ as both arguments tend to $-\infty$
  (Lemma 3.10). Hence it is unconditionally stable for $\alpha\ge1$. For
  $\tfrac12\le\alpha<1$ it is stable only inside a region $S(\alpha)$ of the
  $(z_a,z_b)$ quadrant bounded by an explicit curve $z_b=f(z_a)$, unstable outside, and
  the region grows as $\alpha\to1$ (Eqs. (44)–(45), Cor. 3.11, Fig. 2).
- **The degenerate test does not distinguish them.** For $b=0$ ($y_1'=-ay_1$,
  $y_2'=ay_1$, the production–destruction analogue of Dahlquist's equation) both families
  reduce to $y^{n+1}_1=R(-ha)y^n_1$ with
  $R(z)=\frac{(1-\alpha z)^{1-1/\alpha}}{(1-\alpha z)^{1-1/\alpha}-z(1-(\alpha-\frac12)z)}\in(0,1)$
  for $z<0$, and converge monotonically. Since the families differ on the full test
  system, the authors conclude that this one-directional test is insufficient for schemes
  outside the class of general linear methods (§3.1, Eqs. (47)–(48)).

**Numbers** (§4, Figs. 3–8). With $a=b=25$ ($\lambda=-50$), $y_0=(0.998,0.002)^\top$ and
steady state $(\tfrac12,\tfrac12)^\top$, MPRK22(α) and MPRK22ncs(α) with $\alpha=1$ at
$h=4$ and with $\alpha=2$ at $h=20$ all converge, the ncs variants with more oscillation
and more slowly. For $a=b$ the critical steps of MPRK22ncs are
$h^*_{0.5}=(\sqrt{17}+3)/50\approx0.14$ and $h^*_{0.8}=(\sqrt{101}+9)/50\approx0.38$;
just below them MPRK22ncs is stable, just above them it diverges from a start perturbed by
$10^{-3}$, while MPRK22(α) stays stable. Both values follow from $R_0(w,w)=-1$ with
$w=z_a=z_b=-25h$, which reduces to $(1-w)(1-\alpha w)=w^2$, i.e. $w^2+3w-2=0$ for
$\alpha=\tfrac12$ and $w^2+9w-5=0$ for $\alpha=0.8$ *(compiler check, not in the
sources; page-local $w$)*.

## What "unconditionally stable" means here

The statement is Lyapunov stability of the steady states of the $2\times2$ linear test, for
every $h>0$: perturbations of a steady state stay small and, on the conserved level,
decay. It is not A-stability, which the scheme does not have as a notion, and it is not
absence of oscillations: MPRK22(1) oscillates at $h=4$ in Fig. 4 while being stable. This
is consistent with [Torlo et al. (2022)](/sources/torlo-2022.md), who find MPRK(2,2,α)
oscillation-free only below a step bound (1 for $\alpha<1$, 2 for $\alpha=1$) and present
the Izgin–Kopecz–Meister result as a different notion, stability of the fixed point rather
than monotone approach, not as a conflict (Remark 1.4); the two results answer different
questions. [Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) (§2.1) recall the
same result among the MPRK theory.

The stiff damping of $R_1$ also depends on $\alpha$: $R_1(z)\to-\frac1{2\alpha}$ as
$z\to-\infty$, so at $\alpha=\tfrac12$ the modulus tends to 1 although it stays below 1
for every finite $z$, an analogue of A- without L-stability *(compiler remark, from the
printed $R_1$)*.

## Qualifications

- **Scope.** The criterion is local (a neighbourhood of $y^*$, the same 1-norm level),
  for $2\times2$ linear test systems with positive steady states; the authors name
  higher dimensions, nonlinear systems and global stability as open, and list third-order
  MPRK, MPRKSO, mPDeC, GeCo and BBKS schemes as candidates (§5). The case $b=0$, whose
  steady states lie on the boundary of the positive quadrant, is outside Thm. 2.9 and is
  treated directly.
- **Printed slips** (arXiv v1). Remark 3.2 writes $A_D=\mathrm{diag}(A)$ against
  $A_D=-\mathrm{diag}(A)$ in Eq. (21); Eq. (47) omits the prime on $y_2'$; the proof of
  Lemma 3.10 writes the limit point $(-\infty,\infty)$ for $(-\infty,-\infty)$; the proof of
  Thm. 2.9 calls the eigenvector $(1,-1)^\top$ an "eigenvalue"; Thm. 2.5 asserts a $C^1$
  centre manifold while the proof of Thm. 2.9 speaks of a $C^2$ one. None affects the
  results.
- **Version.** Read as arXiv:2202.01099v1; the published M2AN version may number
  equations differently.

# Citations

- [Izgin et al. (2022)](/sources/izgin-2022.md) — §1 (Eqs. (1), (3)), §2 (Defs. 2.1–2.4, Thms. 2.3, 2.5–2.7, Lemma 2.8, Thm. 2.9, Eqs. (5), (11)–(20)), §3 (Eq. (6), Prop. 3.1, Remark 3.2, Lemmas 3.3–3.6, Remark 3.7, Lemmas 3.8, 3.10, Cors. 3.9, 3.11, Eqs. (41)–(48), Fig. 2), §4 (Eq. (49), Figs. 3–8), §5; arXiv v1.
- [Torlo et al. (2022)](/sources/torlo-2022.md) — Remark 1.4, Thm. 4.7, Fig. 5b; arXiv v5.
- [Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) — §2.1.

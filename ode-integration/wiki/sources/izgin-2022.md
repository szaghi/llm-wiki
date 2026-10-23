---
type: Source
title: "Izgin et al. (2022) — On Lyapunov stability of positive and conservative time integrators and application to second order modified Patankar–Runge–Kutta schemes"
description: "Replaces the Dahlquist equation by the general positive conservative linear 2x2 production–destruction system and proves, by centre manifold theory, that the non-unit Jacobian eigenvalue at a steady state decides Lyapunov stability of any positive conservative scheme, then derives the stability regions of MPRK22."
resource: "doi:10.1051/m2an/2022031"
source_kind: paper
authors: [Izgin T., Kopecz S., Meister A.]
year: 2022
venue: "ESAIM: Math. Model. Numer. Anal. 56:1053-1080"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_ESAIM_Mathematical_Modelling_and_Numerical_Analysis_Izgin_On_Lyapunov_stability_of_positive_and_conservative_time_integrators.pdf"
tags: [positivity, structure-preserving, stability, stiff]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

[Modified Patankar–Runge–Kutta](/methods/modified-patankar-methods.md) (MPRK)
schemes are unconditionally positive and conservative for
[production–destruction systems](/definitions/production-destruction-system.md),
the core of [positivity preservation](/properties/positivity-preservation.md)
in time integration. They are nonlinear even on linear problems and cannot be
applied to the Dahlquist equation $y'=\lambda y$, $\lambda\in\mathbb C^-$,
because $\lambda y$ has no production–destruction meaning. No stability
theory for them existed. The paper replaces the Dahlquist equation by the most
general positive and conservative linear $2\times2$ system $y'=Ly$,
$L=\begin{pmatrix}-a&b\\a&-b\end{pmatrix}$, $a,b\ge0$, $a+b>0$. Its steady
states form a line $\theta(b,a)^\top$; they are Lyapunov stable and never
asymptotically stable.

The main theorem ([Lyapunov stability of positive conservative schemes](/results/lyapunov-stability-positive-conservative-schemes.md),
Thm. 2.9) uses centre manifold theory for maps. Let a $C^2$ map $\psi_h$ on the
positive quadrant have the ray through a steady state $y^*$ as fixed points
and conserve the 1-norm. Then the Jacobian $D\psi_h(y^*)$ has eigenvalues
$1$ and $R$. If $\lvert R\rvert<1$, $y^*$ is Lyapunov stable, and stability
gives local convergence for starting values on the same 1-norm level. The
result holds for any positive and conservative scheme, not only MPRK.

Applied to the two-parameter MPRK22 family of Kopecz & Meister, the scheme is
written as a closed-form map, and the non-unit eigenvalue
$R_\gamma(z_a,z_b)$, $z_a=-ha$, $z_b=-hb$, is called the
[stability function](/definitions/stability-function.md) of MPRK22. MPRK22($\alpha$)
is unconditionally stable for all $\alpha\ge\tfrac12$. MPRK22ncs($\alpha$),
with non-conservative stages, is unconditionally stable for $\alpha\ge1$; for
$\tfrac12\le\alpha<1$ it is stable only inside an explicit region and
unstable outside it. On the degenerate case $b=0$ both families behave alike,
so that test cannot tell them apart. Experiments with $a=b=25$ confirm the
critical steps. "Stable" here means Lyapunov stability of steady states, not
the absence of oscillations; the [Brusselator](/benchmarks/brusselator.md)
appears only as earlier work on Patankar-type integrators.

# Version read

arXiv:2202.01099v1 [math.NA], 2 February 2022, 28 pages, all read. This is
the preprint, not the ESAIM: M2AN version of record; the file prints no DOI.
Title and authors match Crossref. The bibliography keeps this preprint as its
own entry, izgin-2022-b. Section, equation and page numbers on this page are
those of arXiv v1. The archive also holds a short-titled
"..._Izgin_On_Lyapunov_stability_of_positive_and_conservative_time_inte.pdf",
which contains Belardo et al. (2026), not this paper; the file read here is
the full-title one.

# Key claims

Registry notation: $h$ is the step (source $\Delta t$), $L$ the $2\times2$
test matrix (source $A$), $\psi_h$ the one-step map (source $g$), $\varpi_i$
the Patankar denominators (source $\sigma_i$), $z=z_a+z_b=h\lambda$ with
$\lambda=-(a+b)$. The MPRK22 parameter $\alpha$, the selector
$\gamma\in\{0,1\}$ and the matrices $B_\gamma$, $C_\gamma$ are page-local (see
Notation map).

1. MPRK schemes cannot be applied to the Dahlquist equation $y'=\lambda y$,
   $\lambda\in\mathbb C^-$, since $\lambda y$ cannot be treated as production
   and destruction; the usual linear stability analysis is not feasible (§1,
   Eq. (1)). **Stated**
2. On $y_1'=\lambda y_1$, $y_2'=-\lambda y_1$ ($\lambda<0$) the modified
   Patankar–Euler scheme is equivalent to the L-stable backward Euler method
   (§1). **Stated**
3. Even on a linear PDS the second-order MPRK of Burchard et al. gives
   $y^{n+1}=R^ny^n$ with
   $R^n=(I-\frac h2L(W^n+I))^{-1}$, $W^n=\mathrm{diag}(y^n_i/y^{(2)}_i)$, so
   $y^{n+1}$ depends nonlinearly on $y^n$ (after Ortleb & Hundsdorfer) (§1).
   **Derived**
4. A positive and conservative linear PDS matrix has $l_{ii}\le0$,
   $l_{ij}\ge0$ ($i\ne j$) and zero column sums, so the matrix $L$ above covers
   all positive and conservative linear $2\times2$ PDS except $a=b=0$ (§1,
   Eq. (3)). **Stated**
5. The steady states $y^*=\theta(b,a)^\top$ are Lyapunov stable but not
   asymptotically stable; the solution approaches
   $\frac{y^0_1+y^0_2}{a+b}(b,a)^\top$ monotonically along
   $y_1+y_2=\mathrm{const}$ (§2 after Def. 2.1). **Stated**
6. Main theorem: let $\psi_h\in C^2(\mathbb R^2_{>0})$ have the fixed point
   $y^*>0$ with every $ry^*$ ($r>0$) a fixed point, and let
   $\lVert y^{n+1}\rVert_1=\lVert y^n\rVert_1$. Then the spectrum of
   $D\psi_h(y^*)$ is $\{1,R\}$, $R\in\mathbb R$; (a) $\lvert R\rvert<1$ implies
   that $y^*$ is stable; (b) if $y^*$ is stable, there is $\delta>0$ such that
   $\lVert y^0\rVert_1=\lVert y^*\rVert_1$ and $\lVert y^0-y^*\rVert<\delta$
   imply $y^n\to y^*$ (Thm. 2.9). **Proved**
7. Thm. 2.9 holds for general positive and conservative schemes and gives
   "for the first time" a stability criterion for them on (3) (§2 intro,
   remark after the proof, §5). **Proved** (the novelty is **Stated**)
8. In the proof the centre manifold is the $w_1$-axis: the line of fixed
   points maps to it, the conserved 1-norm lines map to lines parallel to the
   $w_2$-axis, and the first component of the transformed map is the identity
   (Eq. (20)). **Proved**
9. On (3), MPRK22 (Eq. (6)) is the map
   $\psi_h(y)=\bigl(I+\frac{h}{1+h(a\tau_1(y)+b\tau_2(y))}L\,\mathrm{diag}(\tau(y))\bigr)y$,
   derived with Miller's rank-one inverse formula (Prop. 3.1, Eq. (26)).
   **Proved**
10. The representation $y^{n+1}=M(y^n)^{-1}y^n$,
    $M(y)=I-hL\,\mathrm{diag}(C_\gamma y)\,\mathrm{diag}(\varpi(y))^{-1}$
    (Eq. (34)), holds for any linear positive and conservative PDS of size
    $N$; the closed-form inverse (36) needs $L$ of rank one (Rem. 3.2).
    **Stated**
11. Every positive steady state of (3) is a fixed point of MPRK22, with
    $B_\gamma y^*=C_\gamma y^*=\varpi(y^*)=y^*$ and $\tau(y^*)=(1,1)$ (Lemma
    3.3); the map is $C^\infty$ on the open quadrant (Lemma 3.4). **Proved**
12. $D\psi_h(y^*)=I+\frac{h}{1+h(a+b)}L\bigl(I+\frac1{2\alpha}(I-B_\gamma)\bigr)$
    (Lemma 3.5, Eq. (41)). **Proved**
13. Every steady state $y^*>0$ is a non-hyperbolic fixed point of MPRK22 with
    $D\psi_h(y^*)y^*=y^*$ and $D\psi_h(y^*)(1,-1)^\top=R_\gamma(z_a,z_b)(1,-1)^\top$,
    $$R_1=\frac{2-2\alpha z-z^2}{2(1-z)(1-\alpha z)},\qquad R_0=\frac{2-z\bigl(\frac{z_a}{1-\alpha z_a}+\frac{z_b}{1-\alpha z_b}\bigr)}{2(1-z)},$$
    $z=z_a+z_b$ (Lemma 3.6, Eqs. (43a)–(43b)). **Proved**
14. For a Runge–Kutta scheme the same analysis gives the eigenvalues 1 and
    $R(z_a+z_b)$, with $R$ the RK stability function, so $R_\gamma$ is called
    the stability function of MPRK22 (Rem. 3.7). **Stated**.
    $R_1(z)=1+z+\tfrac12z^2+O(z^3)$ and $R_1(-\infty)=-\frac1{2\alpha}$, so the
    stiff-limit damping vanishes at $\alpha=\tfrac12$ *(compiler check)*; the
    paper does not comment.
15. $\lvert R_1(z)\rvert<1$ for all $z<0$ and $\alpha\ge\tfrac12$; $R_1$
    depends only on $z=z_a+z_b$ (Lemma 3.8). **Proved**
16. MPRK22($\alpha$) is unconditionally stable: every $y^*>0$ is a stable fixed
    point for every $h$, with local convergence on its 1-norm level (Cor.
    3.9). **Proved**
17. $R_0$ is symmetric and strictly increasing in each argument, with
    $-\frac1\alpha<R_0<1$ for $z_a,z_b<0$ and limit $-\frac1\alpha$ as
    $(z_a,z_b)\to(-\infty,-\infty)$; hence $\lvert R_0\rvert<1$ for
    $\alpha\ge1$ (Lemma 3.10). **Proved**
18. For $\tfrac12\le\alpha<1$: $\lvert R_0\rvert<1$ iff $f(z_a)<z_b<0$ and
    $\lvert R_0\rvert>1$ iff $z_b<f(z_a)$, with $f$ explicit (Eqs.
    (44)–(45)) (Lemma 3.10). **Proved**
19. MPRK22ncs($\alpha$) is stable if $\alpha\ge1$ or $h<h^*_\alpha$, and
    unstable (every steady state an unstable fixed point) if $h>h^*_\alpha$
    and $\tfrac12\le\alpha<1$, where $h^*_\alpha$ solves
    $f(-h^*_\alpha a)=-h^*_\alpha b$ (Cor. 3.11). The stability region lies
    above the graph of $f$ and grows as $\alpha\to1$ (Fig. 2, $\alpha=0.5$,
    0.8, 0.9, 0.95). **Proved** (figure **Shown**)
20. Degenerate case $b=0$: both families reduce to
    $y_1^{n+1}=R(-ha)y_1^n$ with
    $R(z)=\frac{(1-\alpha z)^{1-1/\alpha}}{(1-\alpha z)^{1-1/\alpha}-z(1-(\alpha-\frac12)z)}$
    and $0<R(z)<1$ for $z<0$, $\alpha\ge\tfrac12$, converging monotonically to
    $(0,y^0_1+y^0_2)$ (§3.1, Eqs. (47)–(48)). **Proved**
21. Since both families agree on $b=0$ but differ on (3), this PDS analogue of
    the Dahlquist equation is insufficient to assess the stability of schemes
    that are not general linear methods (end of §3.1). **Derived**
22. Second-order MPRK schemes behave very well on
    $y_1'=\lambda y_1$, $y_2'=-\lambda y_1$, but "only for specific MPRK
    schemes in more general cases" (§1). **Stated**
23. With $a=b=25$, $y^0=(0.998,0.002)^\top$ (Eq. (49)), the exact solution
    reaches $(\frac12,\frac12)^\top$ by about $t=0.1$. MPRK22(1) and
    MPRK22ncs(1) with $h=4$, and MPRK22(2) and MPRK22ncs(2) with $h=20$, all
    converge; the ncs variants oscillate more and converge more slowly (§4,
    Fig. 4). **Shown**
24. For $a=b$ the critical steps are $h^*_{0.5}=(\sqrt{17}+3)/50\approx0.14$
    and $h^*_{0.8}=(\sqrt{101}+9)/50\approx0.38$ (§4, Fig. 5). With
    $h^*_\alpha-0.1$ MPRK22ncs is stable (Fig. 6); with $h^*_\alpha+0.1$
    MPRK22($\alpha$) stays stable (Fig. 7) while MPRK22ncs($\alpha$), started at
    $(0.501,0.499)^\top$, diverges from $y^*$ (Fig. 8). **Shown**. Both values
    give $R_0(z,z)=-1$ with $z=-25h^*_\alpha$ *(compiler check)*.
25. Extending Thm. 2.9 to higher-dimensional and nonlinear systems and to
    global stability is open; the theorem makes possible the analysis of
    third-order MPRK, MPRKSO, mPDeC, GeCo, BBKS and nonautonomous MPRK schemes
    (§5). **Stated**

The result is local (a neighbourhood of $y^*$ on its 1-norm level) and
restricted to linear $2\times2$ systems. "Unconditionally stable" does not
mean oscillation-free: Fig. 4 shows oscillating MPRK22(1) iterates at $h=4$.

# Printed slips

- Rem. 3.2 (p. 13): "$A_D=\mathrm{diag}(A)$" contradicts Eq. (21),
  $A_D=-\mathrm{diag}(A)$ (checked visually).
- Eq. (47) (p. 19): "$y_2=ay_1$" lacks the prime; the next sentence says
  "This system (3)" for (47) (checked visually).
- Proof of Lemma 3.10 (p. 19): the limit is taken as
  "$(z_a,z_b)\to(-\infty,\infty)$" instead of $(-\infty,-\infty)$ (checked
  visually).
- Proof of Thm. 2.9 (p. 8): "$\bar y$ is an eigenvalue ... with corresponding
  eigenvalue $R$"; the first should be "eigenvector".
- Thm. 2.5(a) asserts a $C^1$ centre manifold, while the proof of Thm. 2.9(a)
  speaks of "a $C^2$ function h"; the argument is unaffected.
- Proof of Lemma 3.5 (pp. 14–15): "$d(y)^2$" for $d(y^*)^2$, and
  "$D\tau(y)=\dots$" for $D\tau(y^*)$.
- Typos: "non conservaitve" (p. 3), "Defintion" (p. 4), "provides for the
  first time a criteria" (p. 4), "strictly in increasing" (p. 18),
  "montonically" (p. 21), "larger then" (p. 22). Ref. [20] prints "Meister A."
  surname-first.

# Notation map

| Izgin et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$ | $h$ | constant step |
| $A=\begin{pmatrix}-a&b\\a&-b\end{pmatrix}$ | $L$ | linear test matrix; **$A$ is the registry Butcher matrix** |
| $A_P$, $A_D$ | — | off-diagonal production part and destruction diagonal of $L$ |
| $p_{ij}$, $d_{ij}$ | $p_{ij}$, $d_{ij}$ | PDS rates, $p_{ij}=d_{ji}$ |
| $g$, $Dg$ | $\psi_h$, $D\psi_h$ | one-step map and its Jacobian |
| $\lambda=-(a+b)$; $z_a=-\Delta ta$, $z_b=-\Delta tb$ | $\lambda$; $z=z_a+z_b=h\lambda$ | $z_a$, $z_b$ page-local |
| $\sigma(y)$ | $\varpi(y)$ | Patankar denominators; **$\sigma$ is the registry tree symmetry** |
| $\tau(y)$ | — | ratios $(C_\gamma y)_i/\varpi_i(y)$; **not a tree** |
| $\alpha$ | — | MPRK22 parameter, $\alpha\ge\tfrac12$ (the node $c_2$ of the underlying two-stage method); **not a Shu–Osher or Rosenbrock coefficient** |
| $\gamma\in\{0,1\}$ | — | selects MPRK22($\alpha$) (1) or MPRK22ncs($\alpha$) (0); **not the Rosenbrock or relaxation $\gamma$** |
| $B_\gamma$, $C_\gamma$ | — | stage map and averaged map on linear PDS; **$C_\gamma$ is not a simplifying assumption $C(\eta)$** |
| $M(y)$ | — | matrix of the final linear solve; **$M$ is the registry mass matrix** |
| $R_\gamma(z_a,z_b)$ | — | non-unit Jacobian eigenvalue, the "stability function" of MPRK22; reduces to $R(z)$ for RK methods |
| $\Delta t^*_\alpha$, $S(\alpha)$ | $h^*_\alpha$, — | critical step and stability region of MPRK22ncs($\alpha$); **$S(\alpha)$ is not the registry region $\mathcal S$** |
| $G$, $U$, $V$, $u$, $v$, $h$, $w_1$, $w_2$ | — | centre-manifold normal form; **the source's $h$ is the centre-manifold graph, not the step** |

# Reference list

The paper prints 37 references in numbered, alphabetical style. All are merged
complete into the [bibliography](/bibliography.md) with `citedby` izgin-2022.
No DOIs or arXiv identifiers are printed. Refs. [5] (Blanes, Iserles &
Macnamara 2021), [11] (Ciallella et al. 2021) and [29] (Nüßlein, Ranocha &
Ketcheson 2021) print no venue and are kept as preprint entries, distinct
from any published version. Ref. [6] prints "pages 1–37" without volume;
ref. [20] (PAMM 2021) prints no volume or pages; refs. [27] and [32] are book
chapters whose book titles are not printed; ref. [34] prints pages
"n/a–n/a"; ref. [35] prints a series "volume 2". Three same-author,
same-year pairs need suffixes (Kopecz & Meister 2018 [22], [23]; Hense 2010
[15], [16]; Huang 2019 [17], [18]); their identities are matched to existing
entries by volume and page, not by printed order.

# Pages created or updated

Chunk 6 (2026-10-20). This source is cited on:

* [Lyapunov stability of steady states of positive, conservative time integrators](/results/lyapunov-stability-positive-conservative-schemes.md)
* [Modified Patankar methods (MPRK, MPDeC, MP linear multistep, Patankar predictor–corrector)](/methods/modified-patankar-methods.md)
* [Positivity preservation in time integration](/properties/positivity-preservation.md)
* [Production–destruction systems](/definitions/production-destruction-system.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)

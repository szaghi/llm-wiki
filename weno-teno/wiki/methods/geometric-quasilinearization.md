---
type: Method
title: "Geometric quasilinearization (GQL)"
description: "Geometric quasilinearization rewrites every nonlinear constraint of a convex admissible set as a family of constraints affine in the conservative variables, indexed by free auxiliary variables; the page gives the representation theorems, the three construction methods, the explicit representations and the bound-preservation proofs built on them."
status: established
aliases: [GQL, geometric quasi-linearization, GQL representation]
tags: [bound-preserving, positivity, mhd, relativistic]
timestamp: 2026-10-23T14:51:00Z
---

# Geometric quasilinearization (GQL)

Geometric quasilinearization, introduced by
[Wu & Shu (2023)](/sources/wu-2023-b.md), is an analysis and design tool
for [bound-preserving](/properties/bound-preservation.md) schemes when the
admissible set $G$ is cut out by **nonlinear** constraints $g_i(u)\succ0$
(here and below $\succ$ means $>$ for strict constraints and $\ge$ for
non-strict ones, as in the source, Eq. (3.1)). Its observation is
geometric: a convex set is the intersection of its supporting halfspaces.
Introducing auxiliary variables that are independent of $u$ and
parametrize the boundary points of $G$, every nonlinear constraint becomes
a family of constraints **affine in $u$**. Affine constraints commute with
convex combinations and with the flux-difference structure of a
conservative update, which is what bound-preservation proofs need.

## Definitions

Let $\zeta_{i*}\in\Theta_i$ denote the free auxiliary variables of
constraint $i$ and their range (page-local symbols; the source writes
$\boldsymbol\theta_{i*}$). Let $\varphi_i(u;\zeta_{i*})$ denote a function
affine in $u$ (page-local). Following
[Wu & Shu (2023)](/sources/wu-2023-b.md), Def. 3.1, the set
$$G_*=\{u:\ \varphi_i(u;\zeta_{i*})\succ0\ \ \forall\zeta_{i*}\in\Theta_i,\ 1\le i\le I\}$$
is a **GQL representation** of $G$ if $G_*=G$. Constraints already linear in
$u$ (such as $\rho>0$) are kept as they are (Rem. 3.3). "Linear" means
affine throughout (footnote 2). Let $G_L$ denote the set cut out by the
linear constraints alone ($G_L=\mathbb R^m$ if there are none).

## Representation theorems

- **Constructive criterion** (Thm 3.2). If each $\varphi_i$ is affine in
  $u$ and $\min_{\zeta_{i*}\in\Theta_i}\varphi_i(u;\zeta_{i*})=\lambda_i(u)\,g_i(u)$
  with a scalar $\lambda_i(u)>0$ on $G_L$ (page-local), then $G_*=G$. The
  source states it follows immediately from the definition; no separate
  proof is printed.
- **Necessity of convexity** (§3, Assumption 3.4). An intersection of
  halfspaces is convex, so a GQL representation exists only for convex $G$.
  The minimal hypothesis is "$G$ convex, $\mathrm{int}(G)\neq\emptyset$".
  The $g_i$ themselves need not be concave.
- **Smooth case** (Thm 3.9, proof in App. A). If $G$ is convex, open or
  closed, with differentiable boundary, then
  $$G=\{u:\ (u-u_*)\cdot n_*\succ0\ \ \forall u_*\in\partial G\},$$
  with $n_*$ the inward normal at $u_*$, ">" for open and "≥" for closed $G$.
- **General case** (Thm 3.10). Let $G$ satisfy Assumption 3.4, with
  boundary pieces $\mathcal S_i=\partial G\cap\partial\{g_i\succ0\}$ on
  which $g_i$ is $C^1$ (page-local $\mathcal S_i$), and, when strict
  constraints exist, condition (3.7) (implied by convexity of the open
  region of the strict constraints). Then
  $$G=\{u:\ (u-u_*)\cdot n_{i*}\succ0\ \ \forall u_*\in\mathcal S_i,\ 1\le i\le I\}.$$
  $G$ need not be open or closed. The proof projects an exterior point
  onto $\mathrm{cl}(G)$ and uses the Karush–Kuhn–Tucker conditions, with
  Slater's condition guaranteed by $\mathrm{int}(G)\ne\emptyset$ (Eqs.
  (3.12)–(3.15)). At a non-smooth junction at most $m$ supporting
  halfspaces are needed, instead of all of them (Rem. 3.12).

## Construction methods

1. **Gradient method** (Thm 4.1). If $\nabla g_i(u_*)\neq0$ on $\mathcal S_i$,
   then $\varphi_i(u;u_*)=(u-u_*)\cdot\nabla g_i(u_*)$, the auxiliary
   variable being the boundary point itself.
2. **Cross-product method** (Thm 4.2). Parametrize $\mathcal S_i$ by
   $u_*=U_i(\zeta_{i*})$, $\zeta_{i*}\in\mathbb R^{m-1}$; the normal is
   a nonzero multiple of the $(m-1)$-ary cross product of the tangents
   $\partial U_i/\partial\zeta^{(k)}_{i*}$ (Eq. (4.6)). This handles
   constraints that are only implicit in $u$, such as $p(u)$ in
   relativistic hydrodynamics. A physics-based parametrization in
   primitive variables reduces the number of auxiliary variables
   (Rems. 4.3, 4.5).
3. **Constructive method** (§4.1.3). Propose $\varphi_i$ by method 1 or 2,
   then verify the criterion of Thm 3.2, which bypasses the hypotheses of
   Thms 4.1–4.2.

## Explicit representations

Wu & Shu derive (§4.2):

- **Euler / Navier–Stokes**, $G=\{\rho>0,\ \rho e>0\}$ (Thm 4.4): $\rho>0$ and
  $$\varphi(u;v_*)=E-\rho v\,v_*+\tfrac12\rho v_*^2>0\quad\forall v_*\in\mathbb R .$$
  Its physical reading is $\varphi=\tfrac12\rho(v-v_*)^2+\rho e$, the total
  energy seen from a frame moving at velocity $v_*$ (Rem. 4.6). Minimizing
  over $v_*$ (at $v_*=v$) returns $\rho e$, so the constructive criterion
  holds with $\lambda=1$ *(compiler check, not in the sources: expand
  $E=\rho e+\tfrac12\rho v^2$)*. All three construction methods give this
  representation.
- **Euler with Tadmor's minimum entropy principle** (Thm 4.7): two
  auxiliary variables $(\rho_*,v_*)$, a non-strict family affine in $u$
  plus a term in $\rho_*^\gamma$.
- **M1 radiative transfer** (Thm 4.8): radiation energy minus the radiation
  flux projected on any unit vector is non-negative.
- **Special relativistic hydrodynamics** (Thm 4.9): with $D>0$,
  $E-m\,v_*-D\sqrt{1-v_*^2}>0$ for all $v_*\in(-1,1)$ in 1D ($m$ the
  momentum, $D$ the relativistic mass density); with the entropy principle
  a single family also implies the energy constraint (Thm 4.10).
  [Chen & Wu (2022)](/sources/chen-2022-b.md) state and prove the 2D form,
  $D>0$ and $u\cdot n_*>0$ with
  $n_*=\big(-\sqrt{1-\lvert v_*\rvert^2},\,-v_*,\,1\big)^\top$ for all
  $\lvert v_*\rvert<1$ in the ordering $u=(D,m,E)$ (Lemma 3.4, Eq. (48)):
  the choice $v_*=m/\sqrt{D^2+\lvert m\rvert^2}$ gives one inclusion and
  Cauchy–Schwarz the other. The model is on
  [relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md).
- **Ten-moment Gaussian closure** (Thm 4.11): positive definiteness of the
  pressure tensor becomes $z^\top(\mathcal E-m\otimes v_*+\tfrac12\rho\,v_*\otimes v_*)z>0$
  for all $v_*\in\mathbb R^2$, $z\ne0$, with $\mathcal E$ the energy tensor
  (page-local).
- **Ideal MHD** (Thm 4.12): $\rho>0$ and
  $u\cdot n_*+\tfrac12\lvert B_*\rvert^2>0$ for all $v_*,B_*\in\mathbb R^3$,
  with $n_*=(\tfrac12\lvert v_*\rvert^2,-v_*,-B_*,1)^\top$ in the ordering
  $u=(\rho,\rho v,B,E)$. The gradient method recovers a representation
  first found algebraically by Wu in 2018.
- **Relativistic MHD** (Thm 4.13): an explicit family linear in $u$ and
  indexed by $(v_*,B_*)$, although $p(u)$ and $v(u)$ are implicit.
  [Ding & Wu (2024b)](/sources/ding-2024-b.md) (Lemma 2.2, as recalled from
  Wu & Tang and Wu & Shu) write it, for a general equation of state with
  a Taub-type inequality and causality, in the ordering $u=(D,m,B,E)$, as
  $u\cdot n_1>0$ and
  $$u\cdot n_*+p^*_{\mathrm m}>0\quad\forall\,\lvert v_*\rvert<1,\ B_*\in\mathbb R^3,\qquad
  n_*=\big(-\sqrt{1-\lvert v_*\rvert^2},\,-v_*,\,-(1-\lvert v_*\rvert^2)B_*,\,1\big)^\top,\quad
  p^*_{\mathrm m}=\tfrac12\big((1-\lvert v_*\rvert^2)\lvert B_*\rvert^2+(v_*\cdot B_*)^2\big),$$
  with $n_1=(1,0,\dots,0)^\top$ (page-local $n_1$, $p^*_{\mathrm m}$, the
  auxiliary magnetic pressure).
- **Multicomponent MHD** (Eqs. (6.4)–(6.5)): the ideal-MHD family plus
  linear constraints on the partial densities.
- **Kapila five-equation two-phase model.** [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md)
  (Lemma 2.10, 2D Lemma 3.8, via Thm 4.1 of Wu & Shu) write the admissible
  set $\{\phi_1\rho_1\ge0,\ \phi_2\rho_2\ge0,\ \rho e>0,\ 0\le\phi_1\le1\}$ of the
  [five-equation model](/definitions/five-equation-model.md), in the ordering
  $u=(\phi_1\rho_1,\phi_2\rho_2,\rho v,E,\phi_1)$, as the linear constraints
  $u\cdot n_1\ge0$, $u\cdot n_2\ge0$, $0\le\phi_1\le1$ and $u\cdot n_*>0$ for all
  $v_*\in\mathbb R$, with $n_*=(v_*^2/2,\,v_*^2/2,\,-v_*,\,1,\,0)^\top$ and $n_1$,
  $n_2$ the first two unit vectors (page-local); in 2D $v_*\in\mathbb R^2$ and
  $\lvert v_*\rvert^2$. It is the Euler family above with the density split
  into the two partial densities.

## Bound-preservation proofs built on GQL

Because $\varphi(\cdot\,;\zeta_*)$ is affine, it suffices to bound
$\pm f(u)\cdot n_*$ by a multiple of $u\cdot n_*$:

- **First-order Lax–Friedrichs for Euler.** With $f(u)=v\,u+p\,(0,1,v)^\top$,
  $\pm f(u)\cdot n_*\le\big(\lvert v\rvert+p/(\rho\sqrt{2e})\big)\,u\cdot n_*<(\lvert v\rvert+c)\,u\cdot n_*$,
  hence the scheme is BP under $\nu\le1$ with the global wave speed $a$
  ([Wu & Shu (2023)](/sources/wu-2023-b.md), §5.1, Ex. 1.1; flux on
  [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)).
- **Gas-kinetic (kinetic flux-vector splitting) scheme.** BP under the same
  condition. The proof is much shorter than the classical one, because
  $v_*$ commutes with the velocity integrals (§5.1, Ex. 1.2, Rem. 5.2).
- **Navier–Stokes with central diffusion.** BP under
  $a\frac{\Delta t}{\Delta x}+\frac{\Delta t}{\Delta x^2}\frac{2}{\bar\rho_i\mathrm{Re}}\max\{\eta_v,\gamma/\mathrm{Pr}\}\le1$,
  $\eta_v$ the viscosity constant (page-local), with no convex
  decomposition of convection and diffusion. The authors say the
  decomposition approach gives stricter time-step limits (§5.2, Eq. (5.11),
  Rem. 5.3), an assertion they do not quantify.
- **HLL for special relativistic hydrodynamics on triangles.**
  [Chen & Wu (2022)](/sources/chen-2022-b.md) (§3.5) bound the normal flux
  against the 2D form above: for $a\ge\lambda_4(u)$, the largest
  eigenvalue along the normal $n$,
  $-\big(f(u)\cdot n\big)\cdot n_*>-a\,u\cdot n_*$ (Lemma 3.6, Eq. (52); the
  proof uses $\gamma\le2$), and the HLL flux with wave-speed bounds clipped
  at zero satisfies the corresponding bounds for $D$ and $u\cdot n_*$ with
  the spectral radius of the normal Jacobian (Lemma 3.7). With the
  triangle cell-average decomposition of Zhang, Xia & Shu this proves the
  third-order finite-volume WENO scheme physical-constraint-preserving
  under $\Delta t\,\hat a\,\lvert e\rvert/\lvert K\rvert\le\frac23\mathsf w^{\mathrm{GL}}_0$
  on every edge $e$ of every triangle $K$ (Thm 3.1, Eq. (57); $\hat a$ the
  edge spectral radius, page-local; $\mathsf w^{\mathrm{GL}}_0=1/6$ for their
  quadratic reconstruction). The auxiliary variable never appears in the
  scheme: it is used only in the proof, which checks $D>0$ and
  $u\cdot n_*>0$ for all $v_*$ at once.
- **Ten-moment Lax–Friedrichs in 2D.** BP under
  $\frac{\Delta t}{\Delta x}a^{(1)}+\frac{\Delta t}{\Delta y}a^{(2)}<1$, via an
  AM–GM bound on the GQL form (§5.3, Eqs. (5.16)–(5.18)).
- **Multicomponent MHD.** The first-order update satisfies the GQL
  constraint only up to a term $-\Delta t\,(v_*\cdot B_*)\,\mathrm{div}_{ij}\bar B$,
  which ties bound preservation to a discrete divergence-free condition
  (Thms 6.1–6.4); see
  [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md).

- **Ideal MHD, finite volumes with a discretely divergence-free field.**
  [Ding & Wu (2024a)](/sources/ding-2024.md) (arXiv v1, §3, Lemmas 3.1–3.4,
  Thm 2.1) prove a high-order finite-volume WENO scheme for the
  Godunov–Powell form of ideal MHD positivity preserving with the
  Thm 4.12 representation. Recalled lemmas bound the Lax–Friedrichs flux
  difference of two admissible states with the extra term
  $(B_\ell-\tilde B_\ell)(v_*\cdot B_*)$ for a Lax–Friedrichs coefficient above Wu's wave-speed bound
  (Lemma 3.2, Cor. 3.3), and the source term by
  $-\xi\,S(u)\cdot n_*\ge\xi(v_*\cdot B_*)-\frac{\lvert\xi\rvert}{\sqrt\rho}\big(u\cdot n_*+\tfrac12\lvert B_*\rvert^2\big)$
  (Lemma 3.4; $S(u)=(0,B,v,v\cdot B)^\top$ the Powell source vector, $\xi$
  page-local). Summed over the cell, the divergence terms leave
  $\Delta t\,(v_*\cdot B_*)\big(\tfrac12\widehat{[\![B]\!]}-\nabla_h\cdot\{\!\{B\}\!\}\big)=-\Delta t\,(v_*\cdot B_*)\nabla_h\cdot B_{ij}$,
  which vanishes when the discrete divergence of the cell's own interface
  traces is zero (§3.2; page-local $\nabla_h\cdot$, $\widehat{[\![B]\!]}$; the
  identity checks term by term, *compiler check, not in the sources*). The
  authors use GQL because the divergence condition couples the point values
  and, they state, invalidates the classical convex-decomposition argument of
  Zhang & Shu (§3); see
  [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md).
- **Kapila model with HLL fluxes on DG.** Yan et al. (2024) (Lemma 2.11, 2D
  Lemma 3.9) show $f(u)\cdot n>\sigma^-\,u\cdot n$ and $-f(u)\cdot n>-\sigma^+\,u\cdot n$
  for $n=n_1,n_2,n_*$ with $\sigma^-=\min\{v-c,0\}$, $\sigma^+=\max\{v+c,0\}$
  ($c$ the Wood sound speed; page-local $\sigma^\pm$), through
  $\tfrac12\rho(v-v_*)^2+\rho e\ge\lvert v-v_*\rvert\rho\sqrt{2e}$; the step
  $p/(\rho\sqrt{2e})<c$ is not shown, and holds because
  $\big(p/(\rho\sqrt{2e})\big)^2=(\gamma-1)p/(2\rho)$ with the mixture $\gamma$ while
  $c^2=p/\big(\rho\sum_k\phi_k/\gamma_k\big)$ and $(\gamma-1)\sum_k\phi_k/\gamma_k<1$
  *(compiler check, not in the sources)*. With these bounds the cell averages of
  their [OEDG](/methods/oedg.md) scheme stay admissible under explicit CFL
  conditions (Thms 2.12, 3.10, App. A).
- **Relativistic MHD with central DG.** [Ding & Wu (2024b)](/sources/ding-2024-b.md)
  (§2, Lemmas 2.3–2.4, Cors. 2.1–2.2; Thms 3.1, 4.1–4.2) derive from the
  recalled flux bound
  $(u+\vartheta_{\mathrm s}f_\ell(u))\cdot n_*+p^*_{\mathrm m}+\vartheta_{\mathrm s}\big(v_{*\ell}p^*_{\mathrm m}-B_\ell(v_*\cdot B_*)\big)\ge0$,
  $\vartheta_{\mathrm s}\in[-1,1]$ (page-local), a two-state bound in which
  the difference of fluxes of two admissible states leaves the term
  $-(B_\ell-\tilde B_\ell)(v_*\cdot B_*)$ (Eq. (15)): the jump of the normal
  field enters linearly, which is how a discrete divergence enters the
  bound-preservation proof. A recalled source bound (Lemma 2.4) shows that
  a symmetrization source proportional to $\nabla\cdot B$ produces the
  opposite term, so the two cancel for a locally divergence-free field;
  without the source the proof needs globally coupled discrete
  divergence-free conditions (Thm 4.2). The authors call GQL "essential"
  here, because the locally divergence-free constraint couples the
  interface states and prevents the usual splitting into formally 1D
  bound-preserving schemes (§4.4;
  [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md),
  [bound preservation](/properties/bound-preservation.md)). Their limiter
  uses instead the explicit equivalent form
  $G=\{D>0,\ q(u)>0,\ \Phi(u)>0\}$ with
  $q=E-\sqrt{D^2+\lvert m\rvert^2}$ and a closed-form $\Phi$ (Lemma 3.2,
  recalled; [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)).

## Closed-form blending coefficients

In convex limiting the GQL form turns the internal-energy constraint on an
intermediate state $u^*+\mathsf e\,\Delta u$ into a family of linear inequalities in
the blending coefficient $\mathsf e$ (page-local), so the largest admissible
coefficient is $\min_{v_*}u^*\cdot n_*/\lvert\Delta u\cdot n_*\rvert$.
[Abgrall et al. (2026)](/sources/abgrall-2026.md) (§3.4, Appendix A) evaluate it
in closed form for the 1D Euler family above: numerator and denominator are
quadratics in $v_*$, and with $v_*=p/q$ the minimum is a ratio of quadratic forms
in $(p,q)$, equal to the inverse spectral radius of $\mathsf B^{-1/2}\mathsf A\mathsf B^{-1/2}$,
$\mathsf A$, $\mathsf B$ the $2\times2$ matrices of the two quadratics ($\mathsf B$
positive definite; page-local). They use it for the flux and residual coefficients
of the bound-preserving [PAMPA scheme](/methods/pampa-scheme.md) and state that the
analysis extends to several dimensions (§1).

## Relation to cell-average decompositions

[Cui, Ding & Wu (2024)](/sources/cui-2024.md) relate the tangent lines of
the critical polynomials of their optimal-decomposition problem, which
touch the boundary of the feasible boundary-weight set, to geometric
quasilinearization (§3.7, Fig. 4); see
[optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md).

## Qualifications

- Wu & Shu (2023) was read in its 28-page arXiv v1; the SIAM Review version
  of record is 43 pages, and its numbering may differ.
- The extension of bound preservation to SSP time stepping is stated
  without a stage-wise argument: the point-value hypothesis (6.12) and the
  locally divergence-free property must hold at every stage (§6.2).
- The arXiv v1 prints the bound of Eq. (6.21) as $\le\lvert b\rvert\rho^{1/2}\varphi$
  and the jump coefficient of Thm 6.4 with $(\rho^{\pm})^{1/2}$; text layer
  and page image agree. The bound that holds has the exponent $-1/2$:
  with $\varphi=\rho e+\tfrac12\rho\lvert v-v_*\rvert^2+\tfrac12\lvert B-B_*\rvert^2$
  (Thm 4.12's $n_*$ expanded),
  $(v-v_*)\cdot(B-B_*)\le\rho^{-1/2}\varphi$, while the printed bound fails
  for $\rho<1$ when $\lvert B-B_*\rvert=\rho^{1/2}\lvert v-v_*\rvert$ and
  $\rho e$ is small *(compiler check, not in the sources: Cauchy–Schwarz and
  AM–GM)*. Whether the version of record corrects it is not known.

- Chen & Wu (2022, arXiv v1) print "$-U^\pm\cdot\xi_*>0$" in the proof of
  Lemma 3.7, where their own Lemma 3.4 and the proof of Lemma 3.6 give
  $u^\pm\cdot n_*>0$; the inequalities that follow use the positive sign.

- Ding & Wu (2024b) print the auxiliary magnetic pressure of Lemma 2.2 as
  $\tfrac12\big((1-\lvert v_*\rvert^2)B_*+(v_*\cdot B_*)^2\big)$, with the
  vector $B_*$ where the scalar $\lvert B_*\rvert^2$ is needed, by analogy
  with their $p_{\mathrm m}=\tfrac12\big((1-\lvert v\rvert^2)\lvert B\rvert^2+(v\cdot B)^2\big)$
  (p. 2), since the printed form adds a vector to a scalar; the form above
  uses $\lvert B_*\rvert^2$ *(compiler check, not in the sources)*.

# Citations

- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: Def. 3.1; Thm 3.2; Assumption 3.4; Thms 3.9, 3.10 (App. A, Eqs. (3.12)–(3.15)); Rems. 3.3, 3.12; Thms 4.1, 4.2 (Eq. (4.6)); §4.1.3; Thms 4.4, 4.7–4.13 and Rem. 4.6; §5 (Eqs. (5.11), (5.16)–(5.18)); §6 (Thms 6.1–6.4).
- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — arXiv v1: §3.7, Fig. 4 (link to GQL).
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — arXiv v1: §3.5 (Lemmas 3.4–3.7, Eqs. (48), (52), Thm 3.1, Eq. (57)).
- [Ding & Wu (2024b)](/sources/ding-2024-b.md) — §1; §2 (Eqs. (7)–(16), Lemmas 2.1–2.4, Cors. 2.1–2.2); §3.2–3.3 (Thm 3.1, Lemma 3.2); §4.4 (Thm 4.1, Eqs. (70)–(74)); §4.7 (Thm 4.2).
- [Ding & Wu (2024a)](/sources/ding-2024.md) — arXiv v1: §2.1 (Thm 2.1); §3.1 (Lemmas 3.1–3.4); §3.2 (proof of Thm 2.1).
- [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) — Lemmas 2.10–2.11, 3.8–3.9; Thms 2.12, 3.10; App. A.
- [Abgrall et al. (2026)](/sources/abgrall-2026.md) — §1; §3.4, Eq. (3.19); Appendix A.

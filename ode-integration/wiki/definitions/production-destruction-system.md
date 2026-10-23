---
type: Definition
title: "Production–destruction systems"
description: "A production–destruction system writes each component's right-hand side as nonnegative production minus nonnegative destruction rates; it is conservative when every destruction of one constituent is a production of another, and it is the class on which Patankar-type schemes are positive and conservative for every step size."
status: established
aliases: [PDS, production–destruction–rest system, PDRS, conservative production–destruction system, fully conservative PDS, graph Laplacian system]
tags: [positivity, structure-preserving, stiff, verification]
timestamp: 2026-10-20T06:18:00Z
---

# Production–destruction systems

A **production–destruction system** (PDS) is an ODE whose right-hand side is
split, component by component, into nonnegative transfer rates between constituents:

$$y_i'=\sum_{j=1}^d\bigl(p_{ij}(y)-d_{ij}(y)\bigr),\qquad p_{ij},d_{ij}\ge0,\quad p_{ii}=d_{ii}=0,\qquad i=1,\dots,d,$$

where $p_{ij}$ is the rate at which constituent $j$ feeds constituent $i$ and $d_{ij}$ the
rate at which $i$ is converted into $j$ (registry §8). The form goes back to Burchard,
Deleersnijder and Meister (2003), as recalled by
[Torlo et al. (2022)](/sources/torlo-2022.md) (Eq. (2)),
[Ciallella et al. (2022)](/sources/ciallella-2022.md) (§4.2, Eq. (26)),
[Izzo et al. (2025)](/sources/izzo-2025.md) (Eqs. (1.1)–(1.3), matrix form
$y'=(P(y)-D(y))\mathbf 1$ with page-local matrices $P=(p_{ij})$, $D=(d_{ij})$) and
[Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) (§2.1, Eq. (1)), and is
restated by [Zhu et al. (2024)](/sources/zhu-2024.md) (Eqs. (1.4), (2.1)) and
[Izgin et al. (2022)](/sources/izgin-2022.md) (§1). Torlo et al.
also allow a **rest term** $\rho_i(y)\ge0$ (page-local), $y_i'=\rho_i+\sum_j(p_{ij}-d_{ij})$,
a production–destruction–rest system (PDRS) whose source can break conservation (Eq. (3)).
The splitting into $p$ and $d$ is a modelling choice, not a property of $f$: the same
$f$ admits several splittings, and the Patankar schemes built on them differ.

## Conservation and positivity

- **Conservative PDS.** The system is *conservative* if $p_{ij}(y)=d_{ji}(y)$ for all
  $i,j,y$; then $\sum_iy_i'=0$ and $\mathbf 1^\top y$ is a linear invariant (Torlo et al.
  2022, Def. 1.1; Ciallella et al. 2022, Def. 4.1; Izzo et al. 2025, Eqs. (1.5)–(1.6),
  "fully conservative"; Nurkhametova et al. 2026, Eq. (1b)).
- **Positive ODE.** The ODE is *positive* if $y(0)>0$ componentwise implies $y(t)>0$ for
  all $t$ (Torlo et al. 2022, Def. 1.1; Ciallella et al. 2022, Def. 4.1; Izzo et al. 2025,
  Eq. (1.4)). Nurkhametova et al. use the nonnegative version and the structural condition
  $y_i=0\Rightarrow D_i(y)=0$, with $D_i=\sum_jd_{ij}$, which makes the nonnegative orthant
  invariant (Eq. (1a)).
- **Existence and positivity theorem** (Formaggia–Scotti, as recalled by Torlo et al.
  2022, Thm. 1.2): a PDS with $y(0)\ge0$ has a unique $C^1$ solution with $y_i(t)>0$
  whenever $y_i(0)>0$, if every $d_{ij}$ is locally Lipschitz, $d_{ij}(0)=0$ and
  $d_{ij}(y)=\tilde d_{ij}(y)y_i$ with $\tilde d_{ij}$ continuous, positive for $y>0$ and
  zero at $y=0$. The weaker hypothesis of Burchard et al., $d_{ij}\to0$ as $y_i\to0$ plus
  Lipschitz continuity, bounds $d_{ij}/y_i$ without making it continuous at $y_i=0$
  (Eqs. (4)–(5)). Izzo et al. (2025, §1) state the condition as a unique solution together
  with $D(y)\to0$ as $y\to0$.
- **Linear PDS.** The matrix $L$ of a positive and conservative linear system $y'=Ly$
  must have nonpositive diagonal, nonnegative off-diagonal entries and zero column sums;
  for $d=2$ every such system except $L=0$ is
  $y_1'=-ay_1+by_2$, $y_2'=ay_1-by_2$, $a,b\ge0$, $a+b>0$ (page-local), with
  $p_{12}=d_{21}=by_2$ and $p_{21}=d_{12}=ay_1$ (Izgin et al. 2022, §1, Eqs. (3)–(4)). Its
  eigenvalues are $0$ and $-(a+b)$ and its steady states form the ray $\theta(b,a)^\top$,
  each Lyapunov stable but not asymptotically stable (§2). Izgin et al. use it in place
  of the Dahlquist equation, which has no production–destruction form for complex
  $\lambda$ (§1); see
  [Lyapunov stability of positive, conservative schemes](/results/lyapunov-stability-positive-conservative-schemes.md).
  On the degenerate case $b=0$ the modified Patankar–Euler scheme coincides with backward
  Euler (§1), as Torlo et al. note for linear conservative PDS in general.
- **A general sufficient condition.** For an arbitrary ODE, $y_i=0\Rightarrow f_i(t,y)\ge0$
  for all $y\ge0$ makes the nonnegative orthant invariant; under it backward Euler
  preserves nonnegativity for every $h$ and forward Euler for $h$ small enough
  ([Nüßlein et al. 2021](/sources/nusslein-2021.md), §1, Eq. (1.4), recalled). A PDS with
  $d_{ij}\to0$ as $y_i\to0$ satisfies it *(compiler check, not in the sources)*.

## Properties of a method on a PDS

A one-step or multistep method is **conservative** if $\sum_iy^{n+1}_i=\sum_iy^n_i$ for a
conservative PDS, and **unconditionally positive** if $y_n>0$ implies $y_{n+1}>0$ for
every $h>0$ (Torlo et al. 2022, Def. 1.3; Ciallella et al. 2022, Def. 4.2; Izzo et al.
2025, §1). Here and on [modified Patankar methods](/methods/modified-patankar-methods.md)
$y^n_i$ is component $i$ of $y_n$ (registry §8). Implicit Euler is conservative and
unconditionally positive on a conservative PDS; explicit Euler is only conservative
(Ciallella et al. 2022, §4.2, after Burchard et al.). Every Runge–Kutta method is
conservative, since it preserves all linear invariants (Nüßlein et al. 2021, §1–2), and
so is every linear multistep method *(compiler check, not in the sources)*, but none of
order above one is unconditionally positive (the barrier on
[positivity preservation](/properties/positivity-preservation.md)). In the
shallow-water literature "unconditionally positivity preserving" means a provably positive
water height with no step restriction from positivity (Ciallella et al. 2022, §4).

## Graph Laplacian form

Nurkhametova et al. (2026, §3.1) write a positive system as $y'=\mathbb G(t,y)\,y$, with
$\mathbb G$ (page-local, distinct from the registry's G-norm matrix) satisfying:

- **sign structure:** $\mathbb G_{ii}\le0$ and $\mathbb G_{ij}\ge0$ for $i\ne j$, for all
  $y\ge0$ (Assumption 3.2), or for all $y\in\mathbb R^d$ (the *strong sign* Assumption
  3.3);
- **stability:** the eigenvalues of $\mathbb G$ have nonpositive real parts (Assumption 3.1);
- **linear invariants:** left null vectors $w_1,\dots,w_M$ (page-local) with
  $w_l^\top\mathbb G(t,y)=0$, so that $w_l^\top y$ is constant (Assumption 3.4).

A *graph Laplacian* is the case with sign structure and $w_1=\mathbf 1$ (zero column
sums, mass conservation; Remark 3.5). A conservative PDS with $d_{ij}=\ell_{ij}(y)\,y_i$,
$\ell_{ij}\ge0$ (page-local transition rates) has this form with
$\mathbb G_{ii}=-\sum_{j\ne i}\ell_{ij}$ and $\mathbb G_{ij}=\ell_{ji}$ (§3.2, Eqs.
(11)–(14)). Two structural facts carry the positivity proofs of the Patankar
predictor–corrector: right-multiplying a graph Laplacian by a nonnegative diagonal matrix
keeps its sign structure and left kernel, and nonnegative combinations of such scaled
matrices are again graph Laplacians with the same left kernel (Remarks 3.7–3.9, Eqs.
(8)–(10)). Then $I-h\mathbb G$ is an M-matrix with $(I-h\mathbb G)^{-1}\ge0$ for every
$h\ge0$ (Remark 3.6, recalled from Blanes, Iserles and Macnamara).

The factorization $f=\mathbb G(y)y$ is not unique, and different factorizations preserve
different invariants. Not every linear invariant of the ODE is a left null vector of
$\mathbb G$; those that are not need not be preserved by methods built on $\mathbb G$
(Remark 3.11, §4). In the [stratospheric reaction problem](/benchmarks/stratospheric-reaction-problem.md)
the nitrogen count is a left null vector of the printed factorization and the oxygen count
is not; in the six-species MAPK cascade a factorization parameter decides which of two
invariants is a left null vector (§4.1.2–4.1.3).

## Examples in the sources

- **Linear exchange tests.** Two species with $y_1'=-\kappa_1y_1+\kappa_2y_2$,
  $y_2'=\kappa_1y_1-\kappa_2y_2$ (page-local rates): Torlo et al. (2022, Eqs. (11)–(14))
  rescale time so that $\kappa_1=\theta$, $\kappa_2=1-\theta$ and start from
  $(1-\varepsilon,\varepsilon)$, which isolates the Dahlquist mode
  $\theta y_1-(1-\theta)y_2$ and the conserved sum; Izzo et al. (2025, Eq. (4.22)) use
  $\kappa_1=5$, $\kappa_2=1$ from $(0.9,0.1)$; Nüßlein et al. (2021, Eq. (2.8)) use the
  same structure with rates 5 and 1 from $(1,0)$.
- **Chemical kinetics.** The [Robertson problem](/benchmarks/robertson-problem.md) (Torlo
  et al. 2022, Eq. (69); Nurkhametova et al. 2026, Eqs. (35)–(37)), the
  [stratospheric reaction problem](/benchmarks/stratospheric-reaction-problem.md), the
  nine-species HIRES problem written with one rest term (Torlo et al. 2022, Eqs.
  (70)–(71)), the six-species MAPK cascade (Nurkhametova et al. 2026, Eq. (39)), the
  original six-species [Brusselator](/benchmarks/brusselator.md) (Izzo et al. 2025, Eq.
  (4.25)), the three-species algal-bloom test (Izzo et al. 2025, Eq. (4.24)) and the
  four-species Kopecz–Meister system (Nüßlein et al. 2021, Eq. (2.14)).
- **Reacting flows.** The reaction source of the multispecies reacting Euler equations,
  written for the partial densities $\rho z_i$ (page-local mass fractions $z_i$), is a
  conservative PDS; Zhu et al. (2024, §1, §4.2–4.3) split a reversible reaction rate
  into its nonnegative forward and backward parts to obtain $p_{ij}$ and $d_{ij}$, and
  conservation of $\sum_i\rho z_i=\rho$ is what keeps every $z_i\le1$. Their accuracy tests
  are a linear two-species exchange ($y_1'=y_2-2.7y_1$) and the three-species nonlinear
  system of Huang and Shu with added non-conservative terms (§4.1).
- **Epidemiology.** The eight-compartment SACEIRQD COVID-19 model (Izzo et al. 2025,
  Eq. (4.26)).
- **Finite-volume updates.** A conservative finite-volume semi-discretization of a scalar
  density is a conservative PDS once the positive and negative parts of each face flux
  are read as production and destruction terms between neighbouring cells: for the water
  height of the shallow-water equations, $p$ and $d$ are the positive and negative parts
  of the well-balanced face fluxes divided by the cell size, with at most four nonzeros
  per row in two dimensions (Ciallella et al. 2022, §5.1, Eq. (33)); for heterogeneous
  diffusion with zero-flux boundaries Izzo et al. (2025, Thm. 4.1, Eq. (4.38)) obtain a
  fully conservative PDS with $D=P^\top$. Nurkhametova et al. (2026, §4.1.4) write a
  positivity-shifted finite-volume [KdV equation](/benchmarks/korteweg-de-vries-equation.md)
  in production–destruction form.

## Qualifications

- **"Positive" means two things.** Nüßlein et al. (2021, §1) use "positive" for
  nonnegative; Torlo et al., Ciallella et al. and Izzo et al. use strict positivity, which
  Patankar weights need (they divide by the old values). Zero initial components are
  therefore replaced by tiny values in the Patankar literature: $10^{-180}$ on Robertson
  and $10^{-35}$ on HIRES (Torlo et al. 2022, §7), and the smallest normalized double,
  about $2.2\times10^{-308}$, by Izzo et al. (2025, §3, Tests 3–4).
- **Printed slip in the Kopecz–Meister system.** Nüßlein et al. (2021) print the fourth
  equation as $y_4'=0.05y_2+0.02y_3+0.003y_4$ in Eq. (2.14) and with $-0.003y_4$ in the
  convection–diffusion version (5.5); since $y_1'$ contains $+0.003y_4$, conservation
  requires the minus sign, so (2.14) carries the slip *(compiler check of the printed
  equations, PDF p. 5)*.

# Citations

- [Torlo et al. (2022)](/sources/torlo-2022.md) — Eqs. (2)–(5), Defs. 1.1, 1.3, Thm. 1.2, Eqs. (11)–(14), §7 (Eqs. (69)–(71)); arXiv v5.
- [Ciallella et al. (2022)](/sources/ciallella-2022.md) — §4, §4.2 (Eq. (26), Defs. 4.1–4.2), §5.1 (Eq. (33)); arXiv v3.
- [Izzo et al. (2025)](/sources/izzo-2025.md) — §1 (Eqs. (1.1)–(1.6)), §3, §4 (Eqs. (4.22)–(4.26)), Thm. 4.1 (Eq. (4.38)); arXiv v1.
- [Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) — §2.1 (Eq. (1)), §3.1–3.2 (Assumptions 3.1–3.4, Remarks 3.5–3.12, Eqs. (2)–(16)), §4.1.
- [Nüßlein et al. (2021)](/sources/nusslein-2021.md) — §1 (Eq. (1.4)), §2 (Eqs. (2.8), (2.14)), §5.3 (Eq. (5.5)); arXiv v2.
- [Zhu et al. (2024)](/sources/zhu-2024.md) — §1 (Eqs. (1.3)–(1.4)), §2 (Eq. (2.1)), §4.1–4.3; arXiv v1.
- [Izgin et al. (2022)](/sources/izgin-2022.md) — §1 (Eqs. (3)–(4)), §2; arXiv v1.

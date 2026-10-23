---
type: Definition
title: "Special relativistic hydrodynamics and MHD"
description: "The special relativistic (magneto)hydrodynamics equations in lab-frame conservation form, whose primitive variables and fluxes are implicit functions of the conserved ones; the page fixes the variables, the implicit pressure equation and its provably convergent solvers, the convex admissible set and its linear GQL form, homogeneity, wave speeds, the entropy pair, and the two-fluid plasma and radiation-moment extensions."
status: established
aliases: [RHD, RMHD, relativistic hydrodynamics, relativistic MHD, special relativistic hydrodynamics, special relativistic magnetohydrodynamics, physical-constraint-preserving, PCP, two-fluid relativistic plasma, relativistic radiation MHD, Rad-RMHD, M1 closure]
tags: [relativistic, mhd, bound-preserving, positivity, entropy-stable]
timestamp: 2026-10-23T23:45:00Z
---

# Special relativistic hydrodynamics and MHD

The special relativistic hydrodynamics (RHD) equations express conservation
of rest mass and of the energy–momentum tensor
$T^{\alpha\beta}=\rho h_{\mathrm R}u^\alpha u^\beta+p\,g^{\alpha\beta}$ of a
perfect fluid in Minkowski space-time, with the speed of light $c=1$, the
four-velocity $u^\alpha=W(1,v)$ and the Lorentz factor
$W=(1-\lvert v\rvert^2)^{-1/2}$ (registry §5). Relativistic MHD (RMHD) adds
the electromagnetic part of the stress tensor and the induction equation
([Chen & Wu (2022)](/sources/chen-2022-b.md), §2;
[Duan & Tang (2022)](/sources/duan-2022.md), Eqs. (1.1)–(1.4)). On this page
let $h_{\mathrm R}=1+e+p/\rho$ denote the relativistic specific enthalpy
(page-local; it includes the rest-mass energy and is not the registry's
classical $H$), and let $E$ denote the relativistic lab-frame energy defined
below, which replaces the classical total energy of registry §5. The
ideal equation of state is $p=(\gamma-1)\rho e$ with $\gamma\in(1,2]$, the
upper bound being required for causality (Chen & Wu, Eq. (2), citing Wu &
Tang; Duan & Tang, Eq. (1.7)); the sources write $\Gamma$ for $\gamma$, and
Chen & Wu write $\gamma$ for $W$.

What sets RHD apart from the Euler equations, for a numerical scheme, is
that the primitive variables $(\rho,v,p)$, and therefore the fluxes, are
**implicit** functions of the conserved variables: each flux evaluation
needs the root of a nonlinear equation, and the constraints that define the
admissible states are nonlinear in the conserved variables.

## Conservation form

**RHD** (Chen & Wu, Eqs. (6), (9), 2D). Let $D=\rho W$ denote the lab-frame
mass density and $m=\rho h_{\mathrm R}W^2v$ the momentum (page-local; also
used on the [bound-preservation](/properties/bound-preservation.md) and
[GQL](/methods/geometric-quasilinearization.md) pages). The conserved
variables are $u=(D,m,E)$ with $E=\rho h_{\mathrm R}W^2-p$, and the flux in
direction $d$ is
$$f^{(d)}(u)=\big(D\,v_d,\ m\,v_d+p\,e_d,\ m_d\big),$$
$e_d$ the unit vector. The energy $E$ includes the rest-mass energy.

**RMHD** (Duan & Tang, Eqs. (1.8)–(1.10), 3D). With the lab-frame field $B$,
$\lvert b\rvert^2=\lvert B\rvert^2/W^2+(v\cdot B)^2$ the squared comoving
field and $p_{\mathrm{tot}}=p+\tfrac12\lvert b\rvert^2$ the total pressure
(page-local), $u=(D,m,E,B)$ with
$$m=\big(\rho h_{\mathrm R}W^2+\lvert B\rvert^2\big)v-(v\cdot B)B,\qquad E=D h_{\mathrm R}W-p_{\mathrm{tot}}+\lvert B\rvert^2,$$
$$f^{(d)}=\Big(D v_d,\ m\,v_d-B_d\big(B/W^2+(v\cdot B)v\big)+p_{\mathrm{tot}}e_d,\ m_d,\ v_dB-B_dv\Big),$$
subject to $\nabla\cdot B=0$. RHD is the case $B\equiv0$.

[Berta et al. (2024)](/sources/berta-2024.md) (§2, Eq. (7)) print the RMHD system with the
energy $E=\rho h_{\mathrm R}W^2-p+\tfrac12\lvert B\rvert^2+\tfrac12\big(\lvert v\rvert^2\lvert B\rvert^2-(v\cdot B)^2\big)$
and the momentum flux $w_{\mathrm t}W^2v\,v_d-\mathsf b\,\mathsf b_d+p_{\mathrm{tot}}e_d$, with
$w_{\mathrm t}=\rho h_{\mathrm R}+\lvert B\rvert^2/W^2+(v\cdot B)^2=\rho h_{\mathrm R}+\lvert b\rvert^2$
(the comoving $\lvert b\rvert^2$ above) and the spatial part of the magnetic four-vector
$\mathsf b=B/W+W(v\cdot B)v$ (page-local; its Euclidean norm is not $\lvert b\rvert$). *(compiler check, not in the sources: with
$1/W^2=1-\lvert v\rvert^2$ both expressions equal Duan & Tang's above, so the two sources use the
same system.)* They evolve it with a fourth-order finite-volume scheme with constrained
transport in PLUTO and do not describe their primitive recovery
([divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).

## Primitive recovery

For RHD the pressure is the root on $[0,\infty)$ of (Chen & Wu, Eqs. (7)–(8);
page-local $\mathcal P_u$)
$$\mathcal P_u(p)=\frac{p}{\gamma-1}-E+\frac{\lvert m\rvert^2}{E+p}+D\sqrt{1-\frac{\lvert m\rvert^2}{(E+p)^2}}=0,$$
after which $v=m/(E+p)$ and $\rho=D\sqrt{1-\lvert v\rvert^2}$. For RMHD Duan &
Tang state only that a nonlinear solve is needed (§1). Chen & Wu prove
(§3.4, Lemma 3.3):

- For $u$ in the admissible set below, $\mathcal P_u$ is strictly increasing
  on $[0,\infty)$, with
  $\mathcal P_u'(p)\ge1-\lvert m\rvert^2/(E+p)^2>0$, $\mathcal P_u(0)<0$ and
  $\mathcal P_u\to+\infty$. The positive root exists and is unique, and the
  map from conserved to primitive admissible states is a bijection.
- **Bisection** on $(0,p_{\mathrm R})$,
  $p_{\mathrm R}=(\gamma-1)\big(E-D\sqrt{1-\lvert m\rvert^2/E^2}\big)$, has
  error at most $p_{\mathrm R}/2^{n+1}$ after $n$ steps (Alg. 3.1).
- **Fixed point** $p^{(n)}=p^{(n-1)}-(\gamma-1)\mathcal P_u(p^{(n-1)})$ from
  $p^{(0)}=p_{\mathrm R}/2$ stays positive and contracts with rate
  $\delta_{\mathrm R}=(\gamma-1)\lvert m\rvert^2/E^2<1$ (Alg. 3.2, Eqs.
  (46)–(47); page-local $\delta_{\mathrm R}$, motivated by Marquina et al.).
- A **hybrid** takes bisection when $\delta_{\mathrm R}\ge\tfrac12$ and the
  fixed point otherwise, so it converges at rate
  $\min\{\tfrac12,\delta_{\mathrm R}\}$ (Alg. 3.3); tolerance $10^{-15}$.
- **Newton's method**, the common choice, is not convergence-guaranteed: an
  iterate can turn negative even for an admissible $u$ (Rem. 3.6), and the
  authors restart it from zero when that happens (Rem. 4.1).

On one core (Intel i7-8700K) the hybrid takes 8.7–13.9% of the total CPU
time on four tests, against 15.4–23.0% for Newton, 14.6–17.1% for bisection
and 14.0–27.4% for the fixed point; none of the three provable solvers
failed (Table 3, Rem. 4.1).

**Provably convergent Newton iterations.** [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) (§2)
call a recovery algorithm PCP if every iterate is positive and *convergent* if the iterates
tend to the physical pressure $p(u)$ (Defs. 2.1–2.2), and give three Newton variants, PCP,
convergent for every $u\in G$ and quadratically convergent (Thms. 2.5–2.6, 2.10):

- **NR-I** applies Newton to the monic quartic $\phi(p)=(\gamma-1)^2(h_1-h_2)$ obtained by
  squaring the pressure equation, with $h_1(p)=\big(\lvert m\rvert^2+(E+p)(\tfrac{p}{\gamma-1}-E)\big)^2$
  and $h_2(p)=D^2\big((E+p)^2-\lvert m\rvert^2\big)$ (page-local; Eqs. (2.5)–(2.8)). The quartic has
  two positive roots and either two negative or two complex ones, and $p(u)$ is the smaller
  positive root (Thms. 2.1–2.2). Started from $p_0=0$ if its $p^2$ coefficient $c_2$ is positive,
  and otherwise from the largest root of $\phi''$, the iteration increases monotonically to $p(u)$
  (Alg. 2.1, Thms. 2.3–2.5; page-local $c_2$).
- **NR-II** applies Newton to $\psi(p)=(E+p)\,\mathcal P_u(p)$, whose first and third
  derivatives are positive on $p\ge0$; started from $0$ when $D\ge(E^2-\lvert m\rvert^2)/E$ and
  otherwise from a closed-form guess above $p(u)$, it is always PCP and convergent (Alg. 2.3,
  Lemma 2.6, Thms. 2.7–2.10). It needs one square root per iteration.
- **Hybrid NR** uses NR-I unless $\gamma<1.01$ or $D^2/(E^2-\lvert m\rvert^2)<10^{-4}$, where the
  two positive roots of the quartic cluster (as $D\to0^+$ and as $\gamma\to1^+$, Lemmas 2.7–2.8)
  and NR-I is ill-conditioned; NR-II is used there (Alg. 2.4, Eq. (2.22)).

A closed-form Ferrari root of the quartic exists but is "very costly and sometimes of low
accuracy" (Alg. 2.2). In $10^8$ random samples per set (C++, one core of an i5-7300HQ;
tolerance $10^{-14}$) no algorithm produced a negative pressure. On the first set the hybrid
took 38.775 s against 120.152 s for the Chen & Wu hybrid and 62.906 s for the velocity-proxy
Newton method of Riccardi and Durante, with maximum error $1.15\times10^{-9}$ against
$1.81\times10^{-4}$ for NR-I; on an extreme low-density set NR-I needs 13.19 iterations on average,
NR-II and the hybrid about 3.2; on a large-density, low-velocity set the Chen & Wu hybrid is
fastest, 33.876 s against 37.629 s (§5.1, Tables 1–3). Cai et al. call the Chen & Wu algorithms
only linearly convergent (§1). Because the recovery converges only for $u\in G$, they require
the admissible set at every point where a flux is evaluated, inner quadrature points included,
which they say "differs from the Euler equations" (Remark 3.4).

## Admissible set

The physically admissible states are $\{\rho>0,\ p>0,\ \lvert v\rvert<1\}$ in
primitive variables. In conserved variables (Chen & Wu, Eqs. (10)–(12),
Lemmas 2.1–2.2, recalled from Wu & Tang 2015;
[Wu & Shu (2023)](/sources/wu-2023-b.md), Thm 4.9 with the same
equivalence)
$$G=\{u:\ \rho(u)>0,\ p(u)>0,\ \lvert v(u)\rvert<1\}=\Big\{u:\ D>0,\ g(u)=E-\sqrt{D^2+\lvert m\rvert^2}>0\Big\},$$
with $g$ concave, so $G$ is convex. Although $p(u)$ is implicit, $G$ has a
representation linear in $u$, the
[geometric quasilinearization](/methods/geometric-quasilinearization.md)
(GQL) form
$$G=\Big\{u:\ D>0,\ E-m\cdot v_*-D\sqrt{1-\lvert v_*\rvert^2}>0\ \ \forall\,\lvert v_*\rvert<1\Big\},$$
stated in 1D by Wu & Shu (Thm 4.9) and in 2D by Chen & Wu (Lemma 3.4,
Eq. (48)), who prove it with $v_*=m/\sqrt{D^2+\lvert m\rvert^2}$ for one
inclusion and Cauchy–Schwarz for the other. Wu & Shu add the minimum
principle on the specific entropy, which a single affine family of the same
kind also represents (Thm 4.10), and for RMHD the equivalent set
$\{D>0,\ E-\sqrt{D^2+\lvert m\rvert^2}>0,\ p(u)>0\}$ (Eq. (4.22), from Wu &
Tang 2017) with an explicit GQL family indexed by $(v_*,B_*)$ (Thm 4.13).
Schemes that keep $G$ are called **physical-constraint-preserving** (PCP)
by Chen & Wu; it is [bound preservation](/properties/bound-preservation.md)
for this $G$. [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) (§3–§4) prove a
finite-volume [Hermite WENO](/methods/hermite-weno.md) scheme PCP with the global
[Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md), a two-stage scaling limiter (first on
$D$, then on the concave $g$) at all Gauss–Lobatto points, and the step
$\Delta t\le\tfrac1{12}\Delta x/a$ (Thm. 3.1); the axisymmetric version adds a step restriction
from the geometric source (§4.3).

## Homogeneity

For every $\sigma>0$ (registry §10 scaling), $f^{(d)}(\sigma u)=\sigma f^{(d)}(u)$,
$g(\sigma u)=\sigma g(u)$, and the eigenvalues and eigenvector matrices are
unchanged, so $\sigma u\in G$ for $u\in G$ and the exact evolution operator
is homogeneous of degree one: if $u(x,t)$ solves the problem with data
$u_0$, then $\sigma u(x,t)$ solves it with data $\sigma u_0$ (Chen & Wu,
Eqs. (13)–(14), Lemma 2.3, Prop. 2.1). The density and pressure scale and
the velocity does not, which is why scaled RHD Riemann problems test
[scale invariance](/properties/scale-invariance.md): Chen & Wu make their
WENO weights, limiter and HLL flux homogeneous so that the one-step
operator satisfies $S_h(\sigma u)=\sigma S_h(u)$ (Thm 3.2; the limiter's
floors $10^{-13}$ excepted). With the original Zhu–Qiu weights the deviation
$\rho_h^{(\sigma)}-\sigma\rho_h$ on a scaled Riemann problem is $O(10^{-1})$
for $\sigma=10^{-2}$, with the new weights $O(10^{-12})$ (Ex. 4.4).

## Wave speeds

Along a unit normal $n$, with normal velocity $v_n$ and relativistic sound
speed $c=\sqrt{\gamma p/(\rho h_{\mathrm R})}$ (here not the classical sound
speed of registry §5), the eigenvalues are (Chen & Wu, App. A, after Zhao,
He & Tang)
$$\lambda_{1,4}=\frac{v_n(1-c^2)\mp c\,W^{-1}\sqrt{1-v_n^2-(\lvert v\rvert^2-v_n^2)c^2}}{1-\lvert v\rvert^2c^2},\qquad\lambda_2=\lambda_3=v_n,$$
and for $u\in G$: $0<c<\sqrt{\gamma-1}$ and $v_n<\lambda_4<1$ (Lemma 3.5).
All signal speeds are subluminal. With these speeds as bounds, the HLL flux
with $s^-=\min\{\lambda_1(u^-),\lambda_1(u^+),0\}$,
$s^+=\max\{\lambda_4(u^-),\lambda_4(u^+),0\}$ satisfies GQL-type bounds
(Lemmas 3.6–3.7; the proof uses $\gamma\le2$), from which the third-order
finite-volume WENO scheme on triangles is PCP under
$\Delta t\,\hat a_K^{(j)}\lvert e_K^j\rvert/\lvert K\rvert\le\frac23\mathsf w^{\mathrm{GL}}_0$
(Thm 3.1, Eq. (57); $e_K^j$ the edges of triangle $K$, $\hat a_K^{(j)}$ the
spectral radius on edge $e_K^j$, page-local; $\mathsf w^{\mathrm{GL}}_0=1/(L(L-1))$
the first Gauss–Lobatto weight, $L=\lceil(N+3)/2\rceil$, $1/6$ for their
quadratic reconstruction); see [HLL solvers](/methods/hll-riemann-solvers.md) and the
[cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
on triangles.

## Entropy pair and symmetrization

[Duan & Tang (2022)](/sources/duan-2022.md) (§2, Eq. (2.3), recalled from
Duan & Tang and Wu & Shu) use the convex entropy pair
$$\eta=-\frac{\rho W s}{\gamma-1}=-\frac{D\,s}{\gamma-1},\qquad F^{(d)}_\eta=\eta\,v_d,\qquad s=\ln(p\rho^{-\gamma}),$$
the relativistic form of registry §6, with entropy variables
$w=\big(\frac{\gamma-s}{\gamma-1}+\frac\rho p,\ \frac{\rho W v}{p},\ -\frac{\rho W}{p},\ \frac{\rho(B+W^2v(v\cdot B))}{pW}\big)$.
For $B\not\equiv0$ the pair does not satisfy the compatibility condition and
the RMHD system is not symmetrizable. Adding the Godunov–Powell-type source
$-\Phi'(w)^\top\nabla\cdot B$, with $\Phi=\rho W(v\cdot B)/p$ homogeneous of
degree one in $w$ (page-local $\Phi$), makes $(\eta,F_\eta)$ an entropy pair
of the modified system (Eqs. (2.4)–(2.5), after Wu & Shu); the source
vanishes for divergence-free fields
([divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).
On this form Duan & Tang build sixth-order entropy-conservative and
fifth-order entropy-stable finite-difference schemes on adaptive moving
meshes ([entropy-conservative flux](/methods/entropy-conservative-flux.md),
[TeCNO schemes](/methods/tecno-scheme.md),
[adaptive moving mesh](/methods/adaptive-moving-mesh.md)).

## Two-fluid relativistic plasma

[Bhoriya et al. (2023)](/sources/bhoriya-2023.md) (§2, Eqs. (1)–(3)) treat ions and electrons
as two relativistic fluids, each with a 3D velocity and its own RHD block (page-local species
index $\mathsf s\in\{\mathrm i,\mathrm e\}$, with $D_{\mathsf s}$, $m_{\mathsf s}$, $E_{\mathsf s}$ as
above), coupled to Maxwell's equations in the perfectly hyperbolic divergence-cleaning form of
Munz et al. The 18 conserved variables are the two fluid blocks plus the magnetic field $B$,
the electric field $\mathfrak E$ and two cleaning potentials (page-local $\mathfrak E$,
$\phi_{\mathrm{GLM}}$ for the electric constraint; $\psi_{\mathrm{GLM}}$ of registry §5 for the
magnetic one; cleaning speeds set to 1). With charge-to-mass ratios $\mathsf r_{\mathsf s}$
(page-local), the fluids are coupled only through the Lorentz-force sources
$\big(0,\ \mathsf r_{\mathsf s}D_{\mathsf s}(\mathfrak E+v_{\mathsf s}\times B),\ \mathsf r_{\mathsf s}D_{\mathsf s}\,v_{\mathsf s}\cdot\mathfrak E\big)$,
and Maxwell's equations receive the current and charge densities of both species. The flux
therefore splits into three independent blocks (ion, electron, linear Maxwell), coupled only
by sources; a resistive extension after Amano adds further implicit source terms
(Eqs. (27)–(28)). The ratios $\mathsf r_{\mathsf s}$ set the skin depth and the stiffness of the
sources, which is why the paper integrates them with [IMEX Runge–Kutta](/methods/imex-runge-kutta.md)
schemes.

- **Hyperbolicity** (Lemma 3.1, App. B.1). On
  $\{\rho_{\mathsf s}>0,\ p_{\mathsf s}>0,\ \lvert v_{\mathsf s}\rvert<1\}$ the system has real
  eigenvalues and a complete set of eigenvectors, and $\gamma\in(1,2]$ gives $c<1$; the
  Maxwell eigenvalues are $\pm1$ and the cleaning speeds. *(compiler check, not in the
  sources: the printed fluid eigenvalues in $x$ are the wave-speed formula above with
  $v_n=v_1$.)*
- **Entropy** (Prop. 3.1, App. A; the contraction below in the proof of Thm. 4.2). Smooth solutions satisfy
  $\partial_ts_{\mathsf s}+v_{1,\mathsf s}\partial_xs_{\mathsf s}=0$ for each species, *with* the Lorentz
  sources present, because their contraction with the entropy variables vanishes,
  $w_{\mathsf s}^\top S_{\mathsf s}=0$ (it reduces to
  $v_{\mathsf s}\cdot\big(\mathsf r_{\mathsf s}D_{\mathsf s}(\mathfrak E+v_{\mathsf s}\times B)\big)-\mathsf r_{\mathsf s}D_{\mathsf s}v_{\mathsf s}\cdot\mathfrak E=0$).
  Each fluid carries the entropy pair of the previous section, and entropy stability of the
  whole scheme reduces to that of the two fluid blocks, for any discretization of the Maxwell
  block (Remark 4.3; [entropy stability](/properties/entropy-stability.md)).
- **Entropy variables and scaling.** The entropy variables of each fluid are those of the
  previous section without the magnetic part, with $\rho/p$ as inverse temperature; App. B.2
  gives Barth's eigenvector scaling for the 3D-velocity RHD block in closed form, with a coupled
  $2\times2$ block in the transverse velocities. On this basis the paper builds closed-form
  two-point [entropy-conservative fluxes](/methods/entropy-conservative-flux.md) and
  [TeCNO-type](/methods/tecno-scheme.md) entropy-stable finite-difference schemes of orders 2–4.
- **Tests.** A forced smooth solution, a relativistic two-fluid
  [Brio–Wu tube](/benchmarks/brio-wu-shock-tube.md) with finite skin depth (dispersive two-fluid
  waves appear at 1600 and 6400 cells; at charge-to-mass ratio $10^5/\sqrt{4\pi}$ the solution is
  close to the single-fluid RMHD one), a resistive self-similar current sheet, the relativistic
  [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), a two-fluid
  [blast wave](/benchmarks/mhd-blast-wave.md) and relativistic magnetic reconnection (§6).
  The magnetic divergence is cleaned hyperbolically and monitored, not kept zero
  ([divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).

## Radiation moments (M1 closure)

[López-Miralles et al. (2023)](/sources/lopezmiralles-2023.md) (§2, Eqs. (1)–(17)) extend
relativistic MHD with the grey two-moment radiation transport: the radiation energy density
and flux are added as conserved variables, the radiation pressure tensor is closed by the M1
Eddington tensor, which tends to the Eddington approximation for vanishing reduced flux and to
free streaming as it tends to one, and radiation and matter exchange energy and momentum only
through the radiation four-force (absorption and scattering), a stiff source in optically thick
media. The radiation Jacobian depends only on the radiation variables, so its eigenvalues are
available in closed form and independent of the fluid block (§3.2.1). The paper integrates the
sources with an IMEX Runge–Kutta step and compares radiative
[HLL](/methods/hll-riemann-solvers.md) with a [PVM flux](/methods/polynomial-viscosity-matrix-solver.md);
it bounds the reduced flux by one after reconstruction and falls back to first order when a
reconstructed velocity is superluminal (§3.2).

## Test problems in the sources

Relativistic variants of the bundle's benchmarks:
[isentropic vortex](/benchmarks/isentropic-vortex.md) (RHD, Chen & Wu Ex.
4.1, down to minimum pressure $1.78\times10^{-20}$; RMHD in 2D and 3D, Duan &
Tang Exs. 6.1, 6.7),
[2D Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
(Chen & Wu Exs. 4.6–4.7; Duan & Tang Exs. 6.2–6.4;
[Cui, Ding & Wu (2024)](/sources/cui-2024.md) Ex. 4),
[double Mach reflection](/benchmarks/double-mach-reflection.md) and
[forward-facing step](/benchmarks/forward-facing-step.md) with inflow
$v_1$ up to 0.999 (Chen & Wu Exs. 4.8–4.9),
[shock–vortex interaction](/benchmarks/shock-vortex-interaction.md) and
[shock diffraction](/benchmarks/shock-diffraction.md) (Chen & Wu Exs.
4.10–4.11), the axisymmetric
[relativistic jet](/benchmarks/high-mach-astrophysical-jet.md) at
relativistic Mach number about 41.95 (Chen & Wu Ex. 4.12; Cui et al. Ex. 5),
the [MHD blast wave](/benchmarks/mhd-blast-wave.md) with $\gamma=4/3$ (also Berta et al.'s
relativistic case R1) and
RMHD shock–cloud interactions in 2D and 3D, and a 3D
[shock–bubble interaction](/benchmarks/shock-bubble-interaction.md) (Duan
& Tang Exs. 6.5–6.10). Chen & Wu's code fails without the PCP limiter on
most of these (Exs. 4.3, 4.6, 4.7, 4.9, 4.10, 4.12).
[Cai, Qiu & Wu (2024)](/sources/cai-2024.md) (§5) run sixth-order (1D) and fifth-order (2D)
smooth ultra-relativistic accuracy tests, a 1D Riemann problem, the shock-heating (wall) problem
with inflow speed $1-10^{-10}$, two 2D Riemann problems, the shock–vortex interaction with a
mild and the demanding vortex, and an axisymmetric jet with beam speed 0.99; without the PCP
limiter the code fails after one step on the shock-heating problem and cannot take one step on
the demanding vortex (Exs. 5.4, 5.8). [Berta et al. (2024)](/sources/berta-2024.md) (§5) run
relativistic MHD versions of the 3D rotated shock tube, a new iso-enthalpy vortex, the
[circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md) (observed
$L_1$ order $4.00$ at 512 cells), [field-loop advection](/benchmarks/field-loop-advection.md), the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), a 3D blast wave and a 3D
[shock–cloud interaction](/benchmarks/mhd-shock-cloud-interaction.md).

## Qualifications

- Chen & Wu state, without proof, that Lax–Friedrichs and HLLC fluxes also
  fit their PCP framework (§3.1, KI-4); only HLL is proved.
- The admissible-set equivalence and its convexity are recalled from Wu &
  Tang (2015, 2017), not proved in the ingested sources.
- In the axisymmetric extension Chen & Wu print the geometric source as
  $+\frac1r(Dv_1,m_1v_1,m_2v_1,m_1)$ for
  $\partial_tu+\partial_rf^{(1)}+\partial_zf^{(2)}=S$ (§3.7, Eq. (60)).
  Writing $\frac1r\partial_r(rf^{(1)})=\partial_rf^{(1)}+\frac1rf^{(1)}$ and
  keeping the pressure gradient gives
  $S=-\frac1r(Dv_1,m_1v_1,m_2v_1,m_1)$, and their time-step restriction,
  active only where $v_1>0$, is consistent with the negative sign
  *(compiler check, not in the sources)*. [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) (§4.3)
  print the negative sign, $S=-\frac1r(Dv_1,m_1v_1,m_2v_1,m_1)$.
- Chen & Wu state $\gamma=5/3$ as default and no other value for the
  strong vortex of Ex. 4.1 (vortex strength $\mathcal E=10.0828$, registry
  §10; the source writes $\varepsilon$). With $\gamma=5/3$ the printed
  density $(1-a_{\mathcal E}e^{1-r^2})^{1/(\gamma-1)}$,
  $a_{\mathcal E}=\frac{(\gamma-1)/\gamma}{8\pi^2}\mathcal E^2=0.515$
  (page-local), is undefined at the centre ($1-a_{\mathcal E}e\approx-0.40$); with $\gamma=1.4$ it gives
  $\rho_{\min}=7.83\times10^{-15}$ and $p_{\min}=1.78\times10^{-20}$, the
  printed minima, and $\gamma=1.4$ is the value Ex. 4.10 states for the
  same vortex *(compiler check, not in the sources)*. The paper does not
  print the $\gamma$ of Ex. 4.1. Cai, Qiu & Wu (2024) run the same vortex "as in" Chen & Wu with
  $\gamma=1.4$ stated and print $\rho_{\min}=7.8337\times10^{-15}$, $p_{\min}=1.7847\times10^{-20}$
  (Ex. 5.8).
- **Newton on the pressure equation.** Chen & Wu's statement that Newton's method is not
  convergence-guaranteed concerns plain Newton on $\mathcal P_u$ from an arbitrary start; Cai et
  al. apply Newton to other functions ($\phi$, $\psi$) from designed starting values, so the two
  results do not conflict. Cai et al. call their hybrid superior "in terms of speed ... across
  all tests" (§5.1), but in their own Table 3 the Chen & Wu hybrid and NR-I are faster, and in
  Table 2 NR-II is marginally faster (49.493 s against 49.734 s).
- Cai et al.'s tests run at "CFL number 0.6", whose definition is not printed, while the PCP
  proof needs $\Delta t\le\tfrac1{12}\Delta x/a$ (§5; see
  [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)).

# Citations

- [Chen & Wu (2022)](/sources/chen-2022-b.md) — arXiv v1: §2 (Eqs. (2), (6)–(14), Lemmas 2.1–2.3, Prop. 2.1); §3.1; §3.4 (Algs. 3.1–3.3, Lemma 3.3, Rem. 3.6); §3.5 (Lemmas 3.4–3.7, Thm 3.1); §3.6 (Thm 3.2); §3.7 (Eq. (60)); §4 (Exs. 4.1–4.12, Table 3, Rem. 4.1); App. A.
- [Duan & Tang (2022)](/sources/duan-2022.md) — arXiv v1: §1 (Eqs. (1.1)–(1.10)); §2 (Eqs. (2.3)–(2.6)); §6 (Exs. 6.1–6.10).
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: Thms 4.9, 4.10, 4.13 (Eq. (4.22)).
- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — arXiv v1: §8, Exs. 4–5 (relativistic Riemann problem and jet).
- [Bhoriya et al. (2023)](/sources/bhoriya-2023.md) — arXiv v2: §2 (Eqs. (1)–(3), (27)–(29)); §3 (Lemma 3.1, Prop. 3.1); §4.1 (Remark 4.3); §6; Apps. A, B.
- [López-Miralles et al. (2023)](/sources/lopezmiralles-2023.md) — arXiv v1: §2 (Eqs. (1)–(17)); §3.2 (Eqs. (23)–(31)).
- [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) — arXiv v1: §1; §2 (Eqs. (2.3)–(2.22), Defs. 2.1–2.2, Lemmas 2.1–2.8, Thms. 2.1–2.10, Algs. 2.1–2.4); §3 (Thm. 3.1, Remark 3.4); §4.3; §5 (Tables 1–3, Exs. 5.2–5.9).
- [Berta et al. (2024)](/sources/berta-2024.md) — arXiv v4: §2 (Eq. (7)); §5.

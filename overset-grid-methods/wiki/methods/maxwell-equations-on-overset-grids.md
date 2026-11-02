---
type: Method
title: "Maxwell's equations on overlapping grids"
description: "Henshaw's fourth-order time-domain Maxwell solver on composite overlapping grids: the second-order (vector wave equation) form, modified-equation time stepping, symmetric curvilinear operators, compatibility boundary and dielectric interface conditions with their stability lemmas, Lagrange interpolation of width p+1, dissipation against interpolation-induced weak instability, and measured fourth-order convergence."
status: established
aliases: [time-domain electromagnetics on overlapping grids, Maxwell solver on composite grids, mx, second-order Maxwell formulation, FDTD on overlapping grids]
tags: [maxwell, wave-equation, high-order, composite-grid, stability, parallel]
timestamp: 2026-11-02T15:27:00Z
---

# Maxwell's equations on overlapping grids

[Henshaw (2006)](/sources/henshaw-2006-b.md) solves the time-domain Maxwell
equations for linear, isotropic, non-dispersive media to fourth order on
[composite overlapping grids](/definitions/composite-overlapping-grid.md):
boundary-fitted curvilinear grids at bodies and material interfaces,
Cartesian grids elsewhere, coupled by tensor-product Lagrange
[interpolation](/methods/inter-grid-interpolation.md). Instead of the
first-order curl system and the staggered Yee grid, each field is advanced as
a vector wave equation on collocated grids, so the principal part is a
Laplacian. Four ingredients make the method: three-level modified-equation
time stepping, symmetric high-order approximations of the Laplacian on
curvilinear grids, centred numerical boundary and interface conditions
derived from compatibility conditions, and high-order dissipation against
the weak instability that interpolation introduces. The implementation is
the parallel code mx, built on [Overture](/software/overture.md).

Page-local symbols: $\mathbf E$, $\mathbf H$ the electric and magnetic fields
(bold; the scalar $E$ of the registry is total energy), $\epsilon$ the
permittivity, $\mu_{\mathrm m}$ the permeability (renamed, since $\mu$ is
viscosity), $c=1/\sqrt{\epsilon\mu_{\mathrm m}}$ the wave speed,
$\rho_{\mathrm q}$, $\mathbf J_{\mathrm q}$ the charge and current densities
(renamed from Henshaw's $\rho$, $\mathbf J$), $\mathbf t_\mu$ unit tangents,
$[\cdot]$ the jump across a material interface.

## Second-order formulation

From the curl equations and the constraints
$\nabla\cdot(\epsilon\mathbf E)=\rho_{\mathrm q}$,
$\nabla\cdot(\mu_{\mathrm m}\mathbf H)=0$, Henshaw (§1, Eqs. (1.4)–(1.5))
derives decoupled equations for $\mathbf E$ and $\mathbf H$:
$$\epsilon\mu_{\mathrm m}\,\partial_t^2\mathbf E=\nabla^2\mathbf E+\nabla(\nabla\ln\epsilon\cdot\mathbf E)+\nabla\ln\mu_{\mathrm m}\times(\nabla\times\mathbf E)-\nabla\Big(\frac{\rho_{\mathrm q}}{\epsilon}\Big)-\mu_{\mathrm m}\partial_t\mathbf J_{\mathrm q},$$
and the analogous equation for $\mathbf H$; with constant coefficients and no
sources, $\partial_t^2\mathbf E=c^2\nabla^2\mathbf E$ (Eq. (1.6)). The
second-order form needs one extra boundary condition. On a perfect electrical
conductor (PEC) the conditions are $\mathbf n\times\mathbf E=0$ and
$\nabla\cdot\mathbf E=0$ (Eqs. (2.2)–(2.3)); Gauss's law then holds
everywhere, because $\nabla\cdot\mathbf E$ satisfies the wave equation with zero
initial and boundary data. In 2-D the TE$_z$ unknowns are $(E_x,E_y,H_z)$,
with $\partial_nH_z=0$ on a PEC wall. Far-field (radiation) conditions are
left to later work (§11).

Henshaw (§1, §6.1) argues against the first-order staggered approach on
overlapping grids, citing the large null space of $\nabla\times\nabla\times$, and
shows that away from boundaries the Yee scheme is equivalent to the
second-order version of the present scheme: each staggered component
satisfies the standard centred wave equation. As recalled there, earlier
overlapping-grid Maxwell solvers were second-order FDTD (Yee, Chen & Chang) and
block pseudospectral methods for the first-order system (Driscoll &
Fornberg).

## Time stepping

The three-level Taylor (modified-equation) expansion
$u(t+\Delta t)-2u(t)+u(t-\Delta t)=\Delta t^2\partial_t^2u+\tfrac{\Delta t^4}{12}\partial_t^4u+\dots$,
with time derivatives replaced through $\partial_t^2u=c^2\nabla^2u+f$, gives
schemes of any even order (§3). The fourth-order scheme is (Eq. (3.2))
$$\mathbf U^{n+1}-2\mathbf U^n+\mathbf U^{n-1}=\Delta t^2\big(c^2\nabla^2_4\mathbf U^n+\mathbf f\big)+\frac{\Delta t^4}{12}\Big(c^4(\nabla^4)_2\mathbf U^n+c^2\nabla^2_2\mathbf f+\partial_t^2\mathbf f\Big),$$
where $(\nabla^4)_2$ (page-local) is a second-order biharmonic, so the
stencil is no wider than that of the fourth-order Laplacian. For the PEC
strip model (periodic in $y$, PEC at $x=0,1$), Lemma 6.1 proves stability for
$$\Delta t<c^{-1}\big(\Delta x^{-2}+\Delta y^{-2}\big)^{-1/2},$$
the same limit as the second-order scheme; the 3-D analogue is stated by "an
argument similar". The discrete amplification factors approximate the exact ones to
fourth order, so the model problem is fourth-order accurate (§6). The method is related, as recalled by Henshaw, to the
Numerov and Störmer methods and to Dablain and Shubin & Bell; method-of-lines
Störmer schemes also work but need smaller $\Delta t$ as the order grows (§3).

## Symmetric operators on curvilinear grids

Lemma 5.1 (§5): the scheme $D_{+t}D_{-t}\mathbf U^n=\mathsf L\mathbf U^n$
($\mathsf L$ the spatial matrix with eliminated boundary conditions and
$\lambda$ its eigenvalues, both page-local; $\lambda$ is not the second
viscosity here) is stable if and only if $\mathsf L$ has a complete set of
eigenvectors and real eigenvalues $\lambda$ with $-4<\lambda\Delta t^2<0$. A
double root at $\lambda\Delta t^2=0$ or $-4$, or a Jordan block, gives linear
growth. If $\mathsf L$ is symmetric negative definite the discrete energy
(Eqs. (5.6)–(5.7)) is constant and positive under the step condition.

To obtain symmetric operators on curvilinear grids, Henshaw writes the
generalized Laplacian in conservation form,
$$\nabla\cdot(\kappa\nabla w)=\frac1{\mathcal J}\sum_{m,n}\partial_{r_m}\Big(a^{mn}\partial_{r_n}w\Big),\qquad a^{mn}=\kappa\,\mathcal J\sum_\nu\frac{\partial r_m}{\partial x_\nu}\frac{\partial r_n}{\partial x_\nu},$$
with $\mathcal J=\det(\partial\mathbf x/\partial\mathbf r)$ and a coefficient
$\kappa$ (both page-local; note that $\mathcal J$ is the inverse of the
registry's $J$). Each term $\mathcal J^{-1}\partial_r(a\,\partial_r)$ is
approximated by $\mathcal J^{-1}D_+(a_{i-1/2}D_-)$ plus high-order
corrections, symmetric in the inner product weighted by $\mathcal J$
(Eq. (5.11)). The fourth-order version is
$$\mathcal J^{-1}\Big\{D_+\big(a^{(4)}_{i-1/2}D_-\big)-\frac{\Delta r^2}{24}\Big[D_+\big(a^{(2)}_{i-1/2}D_+D_-^2\big)+D_+^2D_-\big(a^{(2)}_{i-1/2}D_-\big)\Big]\Big\}w,$$
with $a^{(2)}_{i-1/2}=\tfrac12(a_i+a_{i-1})$ and
$a^{(4)}_{i-1/2}=\tfrac9{16}(a_i+a_{i-1})-\tfrac1{16}(a_{i+1}+a_{i-2})$; the
mixed terms are symmetric only in the pair $rs+sr$. Operators of orders 2, 4,
6 and 8 (named SD2–SD8) were implemented in 2-D and 3-D, with stencils at most
$p+1$ points wide (Eq. (5.12)). On a smooth non-orthogonal grid their
Laplacian errors match those of the standard mapping-method operators (FD$p$):
the measured 2-D rates are 2.7, 4.0, 5.8 and 7.5 for SD2–SD8 against 2.7, 4.0,
5.3 and 6.9 (Fig. 1 legend). On randomly perturbed periodic grids the SD
schemes keep the energy constant to relative $10^{-10}$ for $t\in[0,100]$,
while the FD schemes are not energy preserving and are unstable without
dissipation (Fig. 2).

## Compatibility boundary conditions

Ghost values are fixed by centred numerical boundary conditions obtained by
taking even time derivatives of the boundary conditions and replacing them
with space derivatives through the PDE: on a PEC wall
$\mathbf n\times(\nabla^2)^m\mathbf E=0$ and $\nabla\cdot(\nabla^2)^m\mathbf E=0$,
$m=0,1,2,\dots$ (Eqs. (3.3)–(3.4)). Henshaw states that centred conditions are
"in general" more stable and accurate than one-sided extrapolation (§3). In
the PEC model with $(U_1,U_2)\approx(E_x,E_y)$ and two ghost lines, the
fourth-order conditions at $x=0$ are (Eqs. (6.2)–(6.6))
$$\begin{aligned}&U_2=0, && D_{0x}\big(1-\tfrac{\Delta x^2}{6}D_{+x}D_{-x}\big)U_1=0, && D_{+x}D_{-x}\big(1-\tfrac{\Delta x^2}{12}D_{+x}D_{-x}\big)U_2=0,\\ &D_{0x}D_{+x}D_{-x}U_1=0, && (D_{+x}D_{-x})^2U_2=0,\end{aligned}$$
fourth-order approximations of $E_y=0$, $\nabla\cdot\mathbf E=0$ and
$\nabla^2E_y=0$, and second-order approximations of
$\nabla\cdot\nabla^2\mathbf E=0$ and $\nabla^4E_y=0$. On curvilinear grids
(§9.1, Eqs. (9.4)–(9.8)) the divergence condition is written with the scaled
contravariant vectors $\mathcal J\nabla_{\mathbf x}r_m$, and two of the
conditions couple neighbouring boundary points; they are solved by
iteration, normally in 1–2 iterations.

## Material interfaces

Each dielectric subdomain has its own overlapping grid, with boundary-fitted
grids aligned with the interface on both sides and ghost points on both
sides (§7, Fig. 3). The basic jump conditions are
$[\epsilon\,\mathbf n\cdot\mathbf E]=0$, $[\mathbf t_\mu\cdot\mathbf E]=0$, and
for the first derivatives $[\nabla\cdot\mathbf E]=0$,
$[\mu_{\mathrm m}^{-1}\mathbf t_\mu\cdot\nabla\times\mathbf E]=0$, with the
analogous conditions for $\mathbf H$ (Eqs. (7.3)–(7.6)). Compatibility gives
the hierarchy for $n=0,1,2,\dots$ (Eqs. (7.7)–(7.10))
$$\Big[\epsilon\,\mathbf n\cdot\frac{(\nabla^2)^n\mathbf E}{(\epsilon\mu_{\mathrm m})^n}\Big]=0,\quad \Big[\mathbf t_\mu\cdot\frac{(\nabla^2)^n\mathbf E}{(\epsilon\mu_{\mathrm m})^n}\Big]=0,\quad \big[\nabla\cdot(\nabla^2)^n\mathbf E\big]=0,\quad \Big[\mu_{\mathrm m}^{-1}\mathbf t_\mu\cdot\frac{\nabla\times(\nabla^2)^n\mathbf E}{(\epsilon\mu_{\mathrm m})^n}\Big]=0 .$$
The second-order scheme imposes the $n\le1$ conditions with one ghost line
per side; the fourth-order scheme imposes the first- and second-derivative
conditions to fourth order and the third- and fourth-derivative ones to
second order, with two ghost lines (Eqs. (7.11)–(7.18)). Interface values are
set by overwriting the side with the larger $\epsilon$ (Eqs. (7.13)–(7.14)).
When $\epsilon$ is equal on both sides, the discrete conditions reproduce the
no-interface solution (§8). The ghost values couple along the interface: each
iteration solves an $8\times8$ local system per interface point in 2-D
($12\times12$ in 3-D) with neighbours frozen. About 30 iterations were needed
without dissipation for long runs, 1–2 with a small fourth-order dissipation
(§9.3). The implementation is 2-D only and needs matching grid points across
the interface.

**Stability of the interface conditions** (§8). On the 1-D model
$\epsilon u_{tt}=u_{xx}$ with normal and tangential components:
- Lemma 8.1: the second-order interface approximation satisfies the
  Godunov–Ryabenkii condition (no $\ell^2$-bounded eigensolutions with
  growing time dependence) and is second-order accurate.
- Lemma 8.2: the fourth-order approximation satisfies the Godunov–Ryabenkii
  condition in the resolved limit $sh\ll1$, $s$ being the Laplace dual
  variable (page-local); the proof rests on the leading-order asymptotics of
  a $4\times4$ determinant, which is nonzero. General $sh$ is "difficult to
  prove" and is not covered.
- A plane wave through a straight interface ($\epsilon_2=4$, and a 45°
  rotated case with $\epsilon_2=16$; two $80\times80$-cell grids, no
  dissipation) runs stably to $t=500$, about 60,000 steps, with maximum
  errors 0.01 and 0.05 (Fig. 4).

## Overlapping-grid coupling

- **Interpolation width.** Tensor-product Lagrange interpolation in the
  donor's parameter space, width $q=p+1$ for a $p$th-order approximation of
  the second-order wave equation, following Chesshire & Henshaw (§4); see
  [interpolation order and overlap requirements](/results/interpolation-order-requirement.md).
  Points are classified as discretization, interpolation and unused points
  ([point classification](/definitions/point-classification.md)).
- **Weak instability and dissipation.** Interpolation and curvilinear
  boundary conditions make the discrete operator non-symmetric, so some
  eigenvalues are complex and the scheme is weakly unstable at high
  frequencies, by Lemma 5.1 and following Reyna (as recalled by Henshaw).
  The fourth-order dissipation
  $-\alpha_{\mathrm d}(c\Delta t)^2\sum_m\Delta r_m^4(D_{+m}D_{-m})^2(\mathbf U^n-\mathbf U^{n-1})/\Delta t$,
  $\alpha_{\mathrm d}\approx1$ (page-local), keeps fourth order and is on by
  default (Eq. (9.9)); see
  [high-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md).
- **Parallel interpolation** (§9.4). Grid functions are P++ distributed
  arrays (built on Multiblock PARTI). The Lagrange sums are evaluated on the
  processor that owns the donor stencil and shipped to the owner of the
  interpolation points, so at most one message passes between any two
  processors. Strong scaling on a 2.4 GHz Xeon cluster is very good in 2-D (a
  $1024^2$ square; a 3.8-million-point cylinder in a channel) and reasonable
  in 3-D, up to about 32 processors, with the overlapping grid scaling like
  the single box (Fig. 5).

## Verification

Max-norm errors on three grids $\mathcal G_1$, $\mathcal G_2$, $\mathcal G_4$
(refined 2× and 4×), rates $\sigma$ by least squares (§10). The normalized
divergence is $\lVert\nabla\cdot\mathbf E\rVert_\infty/\lVert\nabla\mathbf E\rVert_\infty$.

| test | grids ($\mathcal G_1$) | $\sigma$ (field components) | $\sigma$ (divergence) |
|---|---|---|---|
| [twilight zone](/methods/twilight-zone-flow.md), 2-D cylinder in a channel, PEC, $t=1$ (Table 1) | Cartesian $[-2,2]^2$, $61\times61$, plus annulus radii 1/2 to 3/4, $81\times5$ | 4.40, 3.93, 4.02 | 3.94 |
| twilight zone, 3-D sphere in a box, PEC, $t=1$ (Table 2) | $41^3$ Cartesian $[-2,2]^3$ plus two orthographic patches $33\times33\times13$ on a sphere of radius 1/2 | 4.12, 4.26, 4.11 | 3.47 |
| plane-wave scattering by a PEC sphere vs the Mie series, $t=3$ (Table 3) | as above | 3.86, 3.86, 3.85 | 3.09 |
| scattering by a dielectric cylinder, $ka=4\pi$, $c=1$ outside and 2 inside, radius 1/2, $t=1$ (Table 4) | four grids: Cartesian $[-1,1]^2$ $81\times81$, two annuli matching at the interface, inner Cartesian | 3.86, 3.87, 3.88 | 3.92 |

The finest 2-D twilight-zone errors are $2.2\times10^{-7}$–$5.1\times10^{-7}$.
The dielectric case verifies the fourth-order interface conditions; it was
run with a small fourth-order dissipation and 1–2 interface iterations.

**Eigenvalues** (§10.4). The regularized problem $-\nabla^2\mathbf E=\lambda\mathbf E$,
$\mathbf n\times\mathbf E=0$, $\nabla\cdot\mathbf E=0$ is discretized with the
same operators and solved with ARPACK; spurious eigenvalues with nonzero
divergence are removed afterwards. The first five eigenvalues of the unit
disk converge at close to fourth order. On an L-shaped domain whose
re-entrant corner is rounded by a boundary-fitted grid, they converge at
rates between 1 and 2 to the sharp-corner benchmark values (Table 5;
relative errors on $\mathcal G_1$ from $9.93\times10^{-3}$ for $\lambda_1$ to
$2.53\times10^{-5}$), and the computed eigenvalues are real to double
precision. Henshaw recommends rounding re-entrant corners of large opening
angle with smooth boundary-fitted grids.

**Cost and memory** (§10.5, Tables 6–7). The 3-D pill-box of 10.2 million
points (about $4.2\times10^5$ interpolation points) took 15.0 s per step on a
2.2 GHz Xeon, 6.8% of it interpolation, and 980 MB, or 12.6 reals per point
with only $\mathbf E$ computed; the overlapping grid itself took 2.3 reals per
point. Storing $\partial\mathbf x/\partial\mathbf r$ on all grids would alone
take 9 reals per point.

## Upwind and implicit schemes in later work

[Angel et al. (2023)](/sources/angel-2023.md) solve Maxwell's equations in second-order form to second and fourth order on overset grids with upwind dissipation added as a corrector stage, ten or more times faster than their earlier upwind formulation; [Carson et al. (2025)](/sources/carson-2025.md) add implicit and spatially partitioned implicit–explicit modified-equation time stepping for geometrically stiff wave problems ([upwind schemes for wave equations](/methods/upwind-wave-equation-overset.md), [IMEX time stepping](/methods/imex-time-stepping-on-overset-grids.md)).

## Qualifications

- **Stability on general overlapping grids is not proved.** Lemmas 5.1, 6.1,
  8.1 and 8.2 cover model problems; on general overlapping grids stability
  rests on the added dissipation and the weak-instability argument.
- **Second-order form.** The extra condition $\nabla\cdot\mathbf E=0$ is
  needed at PEC and far-field boundaries, and the regularized eigenproblem
  admits spurious divergent eigenvalues that are filtered afterwards.
- **Printed slips in Henshaw (2006)** *(compiler checks, not in the sources)*:
  - Lemma 8.1 proof: $s_1+s_2=-4$ with $s_k=\epsilon_ks^2h^2$ gives
    $s=\pm2\mathrm i/(h\sqrt{\epsilon_1+\epsilon_2})$, not the printed
    $\pm\mathrm i/(h\sqrt{\epsilon_1+\epsilon_2})$; the conclusion ($s$
    imaginary) stands.
  - §5 (p. 1738) prints the first coefficient of the midpoint-derivative
    series $\partial_rw(r+\Delta r/2)=D_+[1+\sum_n\alpha_n\Delta r^{2n}(D_+D_-)^n]w$
    as $\alpha_1=-\tfrac16$. Since $D_+w=\partial_rw(r+\Delta r/2)+\tfrac{\Delta r^2}{24}\partial_r^3w+O(\Delta r^4)$,
    the coefficient is $-\tfrac1{24}$, which is the $\Delta r^2/24$ printed in
    Eq. (5.12) and in the fourth-order operator above; the printed
    $\alpha_2=\tfrac3{640}$, $\alpha_3=-\tfrac5{7168}$, $\alpha_4=\tfrac{35}{294912}$
    belong to the same series ($\alpha_n$ page-local, not the interpolation weights).
  - §9.1 defines the fourth-order first derivative as
    $D_{0,r_m}(1-\tfrac1{12}\Delta r_1^2D_{+,r_m}D_{-,r_m})$. Since
    $D_0=\partial+\tfrac{h^2}6\partial^3+O(h^4)$, fourth order needs the factor
    $\tfrac16$ (as in the paper's own Eq. (6.3)) and $\Delta r_m$.
  - §6.1 prints the Yee wave operator as $D_{+x}D_{+x}+D_{+y}D_{-y}$; the
    text's "standard central difference operators" is $D_{+x}D_{-x}$.
  - §10.1 defines $s_y=\sin(\pi x)$; the exact fields are divergence-free
    only with $s_y=\sin(\pi y)$.
  - The 3-D scaling box is "$256^3$ (1.78e7)" points; $256^3=1.68\times10^7$.
  - Table 1's $E_x$ rate 4.40: for three grids equally spaced in $\log h$ the
    least-squares slope is $\log_2(e_1/e_3)/2=4.35$ from the printed errors,
    and 4.33–4.37 over their rounding intervals. The other rates of
    Tables 1–4 reproduce within 0.06. The fitting details are not stated, so
    this is recorded as an unexplained discrepancy.

# Citations

- [Henshaw (2006)](/sources/henshaw-2006-b.md) — §1 (Eqs. (1.1)–(1.6); earlier work as recalled), §2 (Eqs. (2.1)–(2.9)), §3 (Eqs. (3.1)–(3.4)), §4 (overlapping grid, $q=p+1$), §5 (Lemma 5.1, Eqs. (5.6)–(5.13), Figs. 1–2), §6 (Lemma 6.1, Eqs. (6.1)–(6.9)), §6.1 (Yee), §7 (Eqs. (7.3)–(7.18)), §8 (Lemmas 8.1–8.2, Fig. 4), §9.1–9.4 (Eqs. (9.1)–(9.9), Fig. 5), §10 (Tables 1–7, Figs. 8–9), §11.
- [Angel et al. (2023)](/sources/angel-2023.md) — Abstract.
- [Carson et al. (2025)](/sources/carson-2025.md) — Abstract.

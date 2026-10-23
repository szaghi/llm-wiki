---
type: Property
title: "Divergence-free magnetic field"
description: "The magnetic field of MHD obeys div B = 0; discretizations enforce it exactly, locally, by cleaning or not at all. Wu and Shu show that bound-preserving high-order MHD needs a discrete divergence-free condition, recovered by a Godunov-symmetrization source; the page adds Powell-type sources, locally divergence-free reconstruction, constrained transport, projection and GLM cleaning, and divergence-preserving prolongation on adaptive meshes."
status: established
aliases: [div B = 0, solenoidal constraint, discrete divergence-free condition, DDF, divergence cleaning, GLM-MHD, constrained transport, CTM, upwind constrained transport, UCT, locally divergence-free DG, locally divergence-free reconstruction, Powell source term, Godunov–Powell source term, projection cleaning, vector-potential formulation, divergence-preserving prolongation]
tags: [mhd, bound-preserving, positivity, dg, finite-volume, relativistic]
timestamp: 2026-10-23T11:06:00Z
---

# Divergence-free magnetic field

The ideal MHD equations carry the involution $\nabla\cdot B=0$: it holds for
all time if it holds initially, but the conservative flux form does not
enforce it, and discretizations generally do not preserve any discrete
version of it. The sources of this bundle meet the constraint in seven ways:
as a hypothesis that [bound preservation](/properties/bound-preservation.md)
needs ([Wu & Shu (2023)](/sources/wu-2023-b.md)); as a constraint built
into the reconstruction polynomial, cell by cell
([Liu et al. (2021)](/sources/liu-2021.md)); as a quantity controlled by
generalized-Lagrange-multiplier (GLM) divergence cleaning
([Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md);
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md));
through constrained transport in an unstaggered central scheme
([Kanbar, Touma & Klingenberg (2022)](/sources/kanbar-2022.md)), through a
vector potential in a semi-implicit all-Mach finite-difference WENO scheme
([Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md)) and in
finite-difference TENO codes ([Fu (2023)](/sources/fu-2023.md)), and on
face-centred staggered fields in a GPU Godunov code
([Lesur et al. (2023)](/sources/lesur-2023.md)) and in a fourth-order
finite-volume scheme for classical and relativistic MHD
([Berta et al. (2024)](/sources/berta-2024.md)); by projection or GLM
cleaning in continuous finite elements
([Dao & Nazarov (2022)](/sources/dao-2022.md)); as a constraint that
prolongation onto refined meshes must keep
([Balsara, Samantaray & Subramanian (2023)](/sources/balsara-2023.md)); and,
without cleaning or transport, through a Powell-type source alone, in
flux reconstruction ([Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md);
[Dzanic & Witherden (2023)](/sources/dzanic-2023.md)) and in entropy-stable
relativistic MHD
([Duan & Tang (2022)](/sources/duan-2022.md)). Three further sources add
locally divergence-free central DG with a symmetrization source for
relativistic MHD ([Ding & Wu (2024)](/sources/ding-2024-b.md)), tenth-order
constrained transport ([Teissier et al. (2024)](/sources/teissier-2024.md))
and constrained transport inside a semi-implicit all-Mach scheme
([Dematté et al. (2024)](/sources/dematte-2024.md)); the construction of
staggered schemes is collected on
[constrained transport](/methods/constrained-transport.md).

## The Powell source term

Three sources add to the conservative MHD system the non-conservative
Godunov–Powell term, proportional to the divergence,
$$\partial_tu+\nabla\cdot f(u)+(\nabla\cdot B)\,S_B(u)=0,\qquad S_B=(0,\ B,\ v,\ v\cdot B)^\top$$
for the ordering $u=(\rho,\rho v,B,E)$ ($S_B$ page-local): Wu & Shu as the
Godunov symmetrization (§6.2, as recalled from Godunov 1972), Liu et al.
after Powell et al. (Eq. (1)), and Rueda-Ramírez et al. (2021) as the
Powell part $\Upsilon^{\mathrm{MHD}}$ of the resistive GLM-MHD system, whose
coefficient vector $(0,B,v\cdot B,v,0)$ for the ordering
$(\rho,\rho v,E,B,\psi_{\mathrm{GLM}})$ is the same vector, with $\mu_0=1$
(Eqs. (13)–(15)) *(compiler check, not in the sources: the components
agree after reordering)*. Rueda-Ramírez et al. (2021) state that these terms, together
with a GLM term required by Galilean invariance, are needed for the
continuous entropy analysis to hold, and they enter the entropy flux
potential through an extra term proportional to $(v\cdot B)B$ (§2.2,
Eqs. (21)–(22)).

**Flux reconstruction.** [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md)
(§5.3, Eq. (48)) add the eight-wave Powell source
$-(0,\ B,\ v,\ v\cdot B)^\top\,\nabla\cdot B$, the same vector, with
$\nabla\cdot B$ the corrected divergence of their
[flux-reconstruction](/methods/flux-reconstruction.md) scheme built from
centred common interface values, and run the MHD rotor and the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) with their
time-reversibility [artificial viscosity](/methods/artificial-viscosity.md);
no further divergence control is used.

[Dzanic & Witherden (2023)](/sources/dzanic-2023.md) use the same
eight-wave source with nodal DG and flux reconstruction stabilized by
[entropy filtering](/methods/entropy-filtering.md) (§2.3, Eq. (17)). They
distinguish a *local* discrete divergence, the collocated derivative of the
element's nodal $B$ (Eq. (18)), from a *global* one that adds the
interface correction built from the centred common value of $B$
(Eq. (19)), and use the global one, which they call "correct" because its
space is consistent with the solution space, the local one being "usually
sufficient in practice". They state, after Wu & Shu, that only the
Powell-modified system is symmetrizable and Galilean invariant for a $B$
that is not exactly solenoidal and that the source suppresses
$\nabla\cdot B$ to the order of the approximation error, and, after Tóth,
that the non-conservative form can be inaccurate near discontinuities
(§2.3); the last point is not tested. The filter interacts with the
constraint: only the linear kernel, which recovers the
[Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md), is
guaranteed not to increase the divergence; the nonlinear exponential
filter may add small divergence errors, which the source treats at the
next update and whose effect was "found to be negligible" (§3.2). On the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)
$\lvert\nabla\cdot B\rvert$ concentrates at strong gradients and decreases
with resolution from $64^2$ to $256^2$ elements at degree 3 (§5.3,
Fig. 4).

**Relativistic MHD.** For special relativistic MHD
([relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md))
[Duan & Tang (2022)](/sources/duan-2022.md) (§2, Eqs. (2.4)–(2.5), after
Wu & Shu) use the symmetrizing source $-\Phi'(w)^\top\sum_d\partial_{x_d}B_d$,
with $w$ the entropy variables and $\Phi=\rho W(v\cdot B)/p$ homogeneous of
degree one in $w$ (page-local), so that
$\Phi'(w)=\big(0,\ B/W^2+v(v\cdot B),\ v\cdot B,\ v\big)$ in the ordering
$(D,m,E,B)$. Without it the thermodynamic entropy pair does not symmetrize
the system for $B\not\equiv0$. On moving curvilinear meshes they discretize
it by the same $2p$th-order linear combination of two-point fluxes as the
entropy-conservative flux, with a two-point "source flux" built from the
averaged metrics and the averaged $B_d$ (Eqs. (3.4), (3.9)), and add no
dissipation to it; the entropy-conservation proof uses this compatibility
(Thm 3.2; [entropy-conservative flux](/methods/entropy-conservative-flux.md),
[TeCNO schemes](/methods/tecno-scheme.md)). No cleaning or constrained
transport is used.

## Divergence and bound preservation

[Wu & Shu (2023)](/sources/wu-2023-b.md) (§6) study multicomponent ideal MHD,
whose admissible set requires $0\le Y_k\le1$, $\rho>0$ and $p>0$ (Eq. (6.4)).
Its [geometric quasilinearization](/methods/geometric-quasilinearization.md)
writes the pressure constraint as
$\varphi(u;v_*,B_*)=u\cdot n_*+\tfrac12\lvert B_*\rvert^2>0$ for all auxiliary
velocities $v_*$ and fields $B_*$ (Eq. (6.5); page-local $\varphi$). With it:

- **First order** (Thm 6.1). Under
  $\Delta t\big(a^{(1)}/\Delta x+a^{(2)}/\Delta y\big)\le1$, the 2D
  Lax–Friedrichs update keeps the species and density constraints and
  satisfies
  $$\varphi(\bar u^{n+1}_{ij};v_*,B_*)>-\Delta t\,(v_*\cdot B_*)\,\mathrm{div}_{ij}\bar B,\qquad
  \mathrm{div}_{ij}\bar B=\frac{\bar B_{1,i+1,j}-\bar B_{1,i-1,j}}{2\Delta x}+\frac{\bar B_{2,i,j+1}-\bar B_{2,i,j-1}}{2\Delta y}.$$
  The update is therefore bound-preserving if the discrete divergence
  vanishes, the **discrete divergence-free (DDF) condition**; since
  $v_*\cdot B_*$ takes either sign, a nonzero divergence leaves the
  right-hand side negative for some auxiliary states.
- **High order** (Thm 6.2, proof omitted by analogy with Wu's 2018
  analysis). For finite-volume or DG cell-average schemes of degree $N\ge1$
  with Gauss-quadrature Lax–Friedrichs fluxes, if the point values at the
  mixed Gauss / Gauss–Lobatto points lie in $G$, then under the CFL bound
  with the first Gauss–Lobatto weight the same estimate holds with
  $\mathrm{div}_{ij}B=\tfrac12\big(\mathrm{div}^-_{ij}B+\mathrm{div}^+_{ij}B\big)$,
  built from the interior ($-$) and exterior ($+$) interface traces.
- **Standard schemes do not preserve the DDF condition** (Rem. 6.3).
  Globally divergence-free DG techniques are incompatible with the local
  [scaling limiter](/methods/zhang-shu-scaling-limiter.md), and a locally
  divergence-free DG basis gives only $\mathrm{div}^-_{ij}B=0$. The
  convex-decomposition analyses of the classical Zhang–Shu framework are
  therefore "inapplicable" to multidimensional MHD.

**The remedy: a discretized Godunov-symmetrization source** (§6.2). The
symmetrizable form above is discretized by a source built only from the
jumps of the normal magnetic field at the interface Gauss points
(Eq. (6.22)). With a locally divergence-free DG basis, $\mathrm{div}_{ij}B$
reduces to those jumps (Eq. (6.19)), the source cancels the offending term,
and the scheme is provably bound-preserving under $(1+\varepsilon_B)\nu\le\varpi$
(Thm 6.4), where $\nu=\Delta t(a^{(1)}/\Delta x+a^{(2)}/\Delta y)$ is the 2D
CFL number of this page, $\varpi=\mathsf w^{\mathrm{GL}}_0$ the first
Gauss–Lobatto weight (the source writes $\lambda$ and $\widehat\omega_1$) and $\varepsilon_B$ a
correction proportional to the normal-field jumps divided by the wave speeds
(page-local; the source's $\varepsilon$). The CFL penalty vanishes when the
normal field is continuous.

**Evidence** (§7). A third-order locally divergence-free DG method with the
source term, a locally divergence-free WENO limiter in KXRCF-flagged cells,
the scaling limiter and SSP-RK3 at CFL 0.15 keeps the admissible set
throughout a two-species MHD blast ($400^2$ cells, $t=0.01$, Fig. 5), and
computes a two-species MHD jet with inflow speed 800 and
$B=(0,\sqrt{4000},0)$ (Fig. 6). On the jet the run "fails quickly" without
any one of the three ingredients — scaling limiter, locally divergence-free
basis, source term — even with the WENO limiter; this is stated, no failure
figure is shown.

For nodal DG with a Powell source, Dzanic & Witherden (2023) state the
gap from the other side: Wu & Shu's positivity of the element mean needs
a locally divergence-free $B$, which their scheme does not have, so
positivity of the mean "remains to be proven" and their positivity is
observed; they split the source from the flux update so that the
entropy filter acts on the source-free part
([bound preservation](/properties/bound-preservation.md), Route 5;
§3.2, Eqs. (29)–(33)).

**Central DG for relativistic MHD.** [Ding & Wu (2024)](/sources/ding-2024-b.md)
(§3–§4, §5) carry the same mechanism to central DG on overlapping primal
and dual meshes, for special relativistic MHD with a general equation of
state. In 1D the flux of $B_1$ vanishes, so $B_1$ stays constant and the
discrete condition holds automatically (Remark 3). In 2D they discretize
the symmetrizable form $\partial_tu+\nabla\cdot f(u)=-(\nabla\cdot B)S(u)$,
$S=\big(0,(1-\lvert v\rvert^2)B+(v\cdot B)v,\,v,\,v\cdot B\big)^\top$ in the
ordering $(D,m,B,E)$ (Eq. (7), the relativistic analogue of the Godunov
form; $S$ page-local), with $(B_1,B_2)$ in the locally divergence-free
polynomial space of Li and Shu and a source on the interior lines of the
target cell, where the other mesh's solution jumps: the normal-field jump
times $S$ of the averaged traces (Eqs. (37)–(38), (51)). In the
bound-preservation proof the flux term and the source term leave
divergence terms of opposite sign whose difference is the divergence
integrated over the four quarter cells, which vanishes for the locally
divergence-free field by Gauss exactness and the divergence theorem
(Thm 4.1, Eqs. (70)–(74)). They call this discrete condition on
overlapping meshes "distinct" from the one Wu and coworkers derived for
non-central DG (§1). Without the source, bound preservation needs
globally coupled discrete divergence-free conditions (Thm 4.2), which hold
for a globally divergence-free field but which the local scaling limiter
destroys; enforcing both "remains unresolved" (§4.7). The limiter itself
keeps the locally divergence-free property (Remark 8). They measure a
relative global divergence, which includes the normal-field jumps on the
edges, and a local one, the integral of $\lvert\nabla\cdot B_h\rvert$ over the
cells (Eqs. (90)–(91)): the local one is zero and the global one about
$10^{-4}$ on the relativistic Orszag–Tang vortex and $10^{-5}$ on the
shock–cloud interaction (Figs. 7, 9). On Mach 50 jets with plasma beta
0.001 the code "would quickly break down" without the limiter, without the
source, or with a conventional (not locally divergence-free) central DG
(Ex. 5.9; runs described, not shown).

## Locally divergence-free reconstruction (finite volumes)

[Liu et al. (2021)](/sources/liu-2021.md) (§3.1–§3.3) carry the
locally divergence-free idea from DG bases to finite-volume reconstruction.
Their [WLS-ENO](/methods/wls-eno.md) polynomials $B^{\mathrm R}_1$,
$B^{\mathrm R}_2$ of degree $k$ in each cell are constrained so that
$\partial_xB^{\mathrm R}_1+\partial_yB^{\mathrm R}_2\equiv0$ in the cell
(Eqs. (15)–(16); $B^{\mathrm R}$ page-local):

1. $B^{\mathrm R}_2$ is reconstructed by the conservative weighted least
   squares, with its cell average imposed exactly;
2. the coefficients of $B^{\mathrm R}_1$ that appear in
   $\partial_xB^{\mathrm R}_1$ follow from matching the monomial
   coefficients of the identity, a square upper-triangular system with
   diagonal $1/((p_1-1)!\,p_2!)$ and therefore a unique solution for every
   degree (Eqs. (17), (24)–(26));
3. the remaining coefficients of $B^{\mathrm R}_1$ (pure $y$-derivatives)
   come from a reduced weighted least-squares fit (Eq. (18));
4. the procedure is repeated with the roles of the two components swapped
   and the two results averaged (Eqs. (19)–(20)), which removes the bias of
   the one-sided version, slightly larger errors in $B_1$ than in $B_2$
   (stated, no data). Both rounds are divergence-free in the cell and
   conservative, so the average is too.

**Discrete divergence.** The Powell term is discretized upwind with the
HLL wave speeds, after Wu & Shu (2019, as recalled; Eqs. (3), (32)). The
resulting discrete divergence splits into an interior term, the integral of
$\nabla\cdot B^{\mathrm R}$ over the cell, which vanishes for a locally
divergence-free reconstruction when the edge quadrature is exact
($2N_g-1\ge k$, $N_g$ Gauss points per edge, Eq. (34)), and a term of
normal-field jumps across the edges (Eqs. (33), (35)). The same reduction
to normal-field jumps is what Wu & Shu's DG analysis uses (Eq. (6.19)).
Because the interior term is not zero in floating point and "may lead to a
failed simulation", the code omits it and evaluates only the jump term,
which is also the divergence diagnostic (§3.3.3); the remaining jumps are
"globally controlled by the Godunov–Powell source term". On the rotor the
divergence norm is "controlled below $10^{-3}$" for linear and quadratic
reconstruction at $200^2$ cells and for linear at $600^2$ (§4.3, Fig. 12). The authors stress
that local is not global: a globally divergence-free scheme would also make
the normal component continuous, so that the Powell term vanishes (§5).

**One-step time-centred form.** [Liu, Feng & Wang (2023a)](/sources/liu-2023.md)
use the same ingredients with linear reconstruction of the primitive
variables inside a one-step HLL generalized-Riemann-problem scheme
([generalized Riemann problem](/methods/generalized-riemann-problem.md);
§3.1.1, §3.2.2). The gradients of $B_2$ come from the weighted least
squares, $\partial_xB_1=-\partial_yB_2$ is imposed in the cell, and
$\partial_yB_1$ follows from a one-unknown least-squares fit; constraining
$\partial_yB_2$ instead, or both and averaging, "didn't make much
difference" (stated, no data). The Godunov–Powell source keeps Wu and
Shu's upwind discretization by normal-field jumps but is evaluated at the
half step $t^n+\Delta t/2$, with the interface states predicted by a
Cauchy–Kowalewski step (Eqs. 67–70); the generalized Riemann problem at
the edge is posed without the source, "following the usual rotation
schemes", because adding it "may affect the stability and accuracy"
(§3.1.3). They monitor the normalized divergence
$\Delta x\,\lvert\nabla\cdot B\rvert_i/\lvert B\rvert_i$, computed from
the normal-field jumps (Eqs. 86–87). Its global norm is comparable to or
lower than that of forward-Euler and two-stage Runge–Kutta HLL schemes
with the same reconstruction on the [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)
(run to $t=100$ without negative pressure), concentrates at the shock
front of the low-$\beta_{\mathrm p}$ [blast wave](/benchmarks/mhd-blast-wave.md),
and stays at the $10^{-3}$ level on a 3D blast wave at $200^3$
(§4.3–4.6, Figs. 7–11, 16–20).

## Constrained transport

**Unstaggered central scheme.** [Kanbar, Touma & Klingenberg (2022)](/sources/kanbar-2022.md)
(§4, Eqs. (18)–(21)) correct the magnetic field of their
[unstaggered central scheme](/methods/unstaggered-central-scheme.md) at the
end of each step, after Touma's constrained-transport method (CTM). With
$\Omega=-v_1B_2+v_2B_1$ (page-local) the 2D induction equation is
$\partial_t(B_1,B_2)-\partial_x(0,\Omega)+\partial_y(\Omega,0)=0$; the field
on the dual (staggered) nodes is re-updated with centred differences of
$\Omega^{n+1/2}$, the time average of $\Omega$ at the dual node, and averaged
back to the primary nodes. If the centred divergence
$$\nabla\cdot B^n_{i,j}=\frac{B^n_{1,i+1,j}-B^n_{1,i-1,j}}{2\Delta x}+\frac{B^n_{2,i,j+1}-B^n_{2,i,j-1}}{2\Delta y}$$
vanishes at every primary node, the divergence on the dual nodes is the
average of four such values and vanishes, and so does the divergence at the
primary nodes after averaging back (Eqs. (20)–(21); the substitution is
sketched, not written out). This is the same centred, $2\Delta$-wide
discrete divergence that appears in Wu & Shu's Thm 6.1 above *(compiler
check, not in the sources: the two printed formulas coincide)*. Numerically
(§5): on a four-state MHD Riemann problem ($400^2$, $t=0.8$) the divergence
is of order $10^{-14}$ with CTM and of order one without, with visually
alike densities (Figs. 4–5); in a magnetized stratified atmosphere it is
clearly nonzero without CTM and zero "up to machine precision" with it
(Figs. 10–11); CTM adds "a small smearing out effect" on the Brio–Wu tube
(Fig. 3). The authors apply CTM "whenever needed" and give no criterion
(§6).

**Staggered constrained transport in IDEFIX.**
[Lesur et al. (2023)](/sources/lesur-2023.md) (§2.4, Eqs. (6)–(8))
evolve face-averaged $B$ by $\partial_tB=-\nabla\times\mathcal E$ with
the electric field $\mathcal E$ (page-local) on cell edges, after Evans
and Hawley, so that the discrete Stokes theorem keeps the face-based
divergence of each cell "in principle" at machine precision; the
cell-centred $B$ in the conserved vector is reconstructed from the faces
([IDEFIX](/software/idefix.md)). The edge field comes from the
face-centred Riemann fluxes, by arithmetic averaging, by Gardiner and
Stone's $\mathcal E^0$ or $\mathcal E^c$ (the default, "a good trade-off
between accuracy, stability and computing time"), or from 2D HLL and
HLLD Riemann solvers at the edges after Mignone and Del Zanna, all
selectable at run time; no formulas are printed. Round-off can still
accumulate over billions of steps: with second-order Runge–Kutta–Legendre
super time-stepping for Ohmic and ambipolar diffusion the round-off
divergence grows like $O(n)$ in the number of cycles, against
$O(\sqrt n)$ with the explicit integrator (§2.8; stated from their
tests). An optional vector-potential form, $\partial_tA=-\mathcal E$ with
$A$ on edges and $B=\nabla\times A$, "mathematically equivalent to the
original CT algorithm", stops the accumulation at the cost of memory, an
initial condition written for $A$, and possible overflow of $A$ under a
large-scale constant electric field (§2.4). On the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)
$\lvert\nabla\cdot B\rvert\ll10^{-12}$ in all runs (§4.2, Fig. 11). For
the Hall effect the edge field is the arithmetic average, because a
Hall-modified $\mathcal E^c$ "led to numerical instabilities" (§2.5).

**Vector potential in a semi-implicit finite-difference WENO scheme.**
[Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) (§2.4, Eqs.
(2.15)–(2.17), after Christlieb, Rossmanith & Tang) write
$B=\nabla\times A$ with a page-local vector potential $A$ in the Weyl
gauge, evolve $\partial_tA+(\nabla\times A)\times v=0$ in place of the
induction equation, and recover $B$ from $A$ at every stage, so that the
continuous $\nabla\cdot B$ vanishes identically. In 2D only $A_3$ is
evolved, by the Hamilton–Jacobi equation
$\partial_tA_3+v_1\partial_xA_3+v_2\partial_yA_3=0$, discretized by the
fifth-order WENO scheme for Hamilton–Jacobi equations of Jiang & Peng with
a Lax–Friedrichs Hamiltonian, and $B_1=\partial_yA_3$, $B_2=-\partial_xA_3$
are computed by fourth-order central differences (§3.3–3.4, Eq. (3.14)).
The explicit part of their
[semi-implicit all-Mach scheme](/methods/semi-implicit-all-mach-scheme.md)
carries the transport step, and their asymptotic-accuracy theorem includes
$\nabla\cdot B=0$ in the low sonic Mach limit (Thm 4.2;
[asymptotic preservation](/properties/asymptotic-preservation.md)). In 1D
the divergence vanishes automatically and the conservative $B$ equation is
used instead (§3.1). Numerically, the maximum discrete divergence on the
[MHD blast wave](/benchmarks/mhd-blast-wave.md) ($200^2$, sonic Mach
number $M=0.9$) is $2.87\times10^{-11}$, against $2.77\times10^{-11}$ for
an explicit WENO scheme with the same transport (§5.2); the other 2D runs
keep it "up to machine round off errors", unquantified. The price is
accuracy in $B$: on the rotated Alfvén wave the momentum converges at
fifth order and $B_1$ at about fourth ($L^1$ order 4.13 at $128^2$), which
they attribute to the central-difference curl (Table 5.3).

**Fourth-order upwind constrained transport.**
[Berta et al. (2024)](/sources/berta-2024.md) (§2, §4, App. B, arXiv v4)
build a fourth-order finite-volume scheme for classical and special
relativistic MHD on Cartesian grids in the PLUTO code. The staggered,
face-averaged normal field is advanced by the discrete Stokes theorem
with edge-averaged electric fields, so the face-based discrete divergence
of each cell has zero time derivative exactly (Eqs. 11–15). Fourth order
needs conversions between averages and point values, all built from
undivided Laplacians with the factor $1/24$: the face point value of the
normal field is the face average minus $1/24$ of its transverse
Laplacian (Eq. 21); the cell-centred field is an unlimited fourth-order
interpolation of the face point values,
$B_{1,i}=\tfrac9{16}\big(B_{1,i+1/2}+B_{1,i-1/2}\big)-\tfrac1{16}\big(B_{1,i+3/2}+B_{1,i-3/2}\big)$
(Eq. 22, in 1D notation); and the edge-centred electric field from the
upwind constrained-transport (UCT) average of Mignone and Del Zanna,
built from the transverse velocities and normal fields reconstructed
from face centres to edges with flux and diffusion coefficients of the
HLL, HLLD or GFORCE solver (Eq. 39,
[HLL-family solvers](/methods/hll-riemann-solvers.md)), is turned into an
edge average by adding $1/24$ of its Laplacian along the edge (Eq. 40).
The relativistic extension of UCT-GFORCE is new (App. B). Because the
reconstruction acts on point values, the electric field needs three
layers of transverse ghost zones rather than four (§4). Appendix B also
corrects Mignone and Del Zanna's GFORCE transverse-velocity formula,
whose Eq. 51 "contains 'y' instead of 't'".

The evidence is on divergence-sensitive benchmarks (§5). On rotated 3D
shock tubes the oscillations of the normal field are of the same order as
with Mignone's fifth-order finite-difference scheme and smaller than with
an earlier scheme they cite (Figs. 2–3). On
[field-loop advection](/benchmarks/field-loop-advection.md) ($256\times128$,
two periods) the loop is smeared less at fourth than at second order,
pointwise WENO-Z "performs the best", pointwise MP5 leaves small over- and
undershoots at the tail and head of the loop, the magnetic energy decays
fastest at second order, and the Riemann solver matters "only
marginally", with GFORCE better (Figs. 6–7). On circularly polarized
Alfvén waves the damping rate, their measure of dissipation, falls as
about $N_x^{-5}$ at fourth order against $N_x^{-3}$ at second order (§5.3,
Fig. 5; [circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)).

**Tenth-order constrained transport.** [Teissier et al. (2024)](/sources/teissier-2024.md)
(§2.3, §3.1.1, §3.2.3, arXiv v2) build finite-volume MHD schemes of orders
2–10 with staggered constrained transport: face averages of the normal
field, an edge field from a multidimensional Lax–Friedrichs average with
WENO-reconstructed corner states, and a face-to-cell interpolation by
explicit formulas up to tenth order, with one reconstructed value per face
at any order. The face-based discrete divergence is preserved to machine
precision (Eq. (17)), and the electromotive forcing of their turbulence
runs is built as a staggered face average in Fourier space so that it adds
no divergence (§3.5). In their diffusion test the magnetic-field error
stays near $5\times10^{-15}$ while the velocity error decreases, which they
attribute to floating-point arithmetic without investigating it (§4.2).
Formulas and orders are on [constrained transport](/methods/constrained-transport.md).

**Constrained transport inside an implicit iteration.**
[Dematté et al. (2024)](/sources/dematte-2024.md) (§3.3, Eqs. (39)–(51))
keep $\nabla\cdot B$ at round-off in a cell-centred semi-implicit all-Mach
finite-volume scheme, where the magnetic field is first predicted by a
linear solve that does not respect the constraint. In each inner Picard
iteration the predictor is corrected either by a staggered adaptation of
Gardiner and Stone's constrained transport, whose corner electric field
includes the implicit pressure-subsystem flux and whose cell field is the
face average, or by an unstaggered adaptation of Rossmanith's
vector-potential method, which advects the out-of-plane potential at cell
centres and keeps the central divergence zero. Both keep
$\lVert\nabla\cdot B\rVert_{L^2}$ near machine precision through the MHD
rotor (§4.1.4, Fig. 8); magnetic and cross helicity are not conserved
exactly, with errors comparable to those of an explicit second-order
divergence-free Godunov scheme (§4.3.2, Fig. 16;
[semi-implicit all-Mach scheme](/methods/semi-implicit-all-mach-scheme.md)).

**Prolongation onto refined meshes.** On a block-structured
[adaptive mesh](/methods/adaptive-mesh-refinement.md) the face-collocated
field of a newly refined coarse zone must be filled so that every new fine
zone satisfies the constraint. Balsara, Samantaray & Subramanian (2023)
treat $\nabla\cdot B=0$ and the electrodynamic $\nabla\cdot D=\rho_{\mathrm q}$
together ($D$ the electric displacement, $\rho_{\mathrm q}$ the charge
density, page-local), recalling Yee's staggering and constrained-transport
MHD as the face-collocated setting (§1). Fine faces that overlie coarse
faces keep the coarse data, so the normal component stays continuous;
only the internal fine faces are new. Their high-order constructions,
an analytically exact fourth-order reconstruction and a WENO-type face
interpolation with a least-squares touch-up, give fine-zone divergences
of $10^{-15}$–$10^{-12}$ (Tables 2–11); details on
[divergence-preserving prolongation](/methods/divergence-preserving-prolongation.md).
Their sub-cycled two-level step adds edge-field defect correction, without
which, they state, divergence builds up at fine–coarse interfaces (§7).

**TENO-A with unstaggered constrained transport.**
[Fu (2023)](/sources/fu-2023.md) reviews TENO-A for MHD with unstaggered
constrained transport (§5.3, recalled from earlier work): in 1D the cost of
TENO5-A is similar to WENO5-JS and WENO5-Z, and even the eight-point TENO8-A
adds a "negligible" cost; Orszag–Tang results at $200^2$ are compared with a
WENO5-JS reference at $512^2$ (Fig. 19). The review gives no formulas for
the transport step.

**Reference solutions.** [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md)
compare their GLM-MHD DG results on the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) with the
second-order constrained-transport code Athena at $1024^2$ and $2048^2$
(§6.2, Figs. 9–10).

## Divergence cleaning (GLM-MHD)

GLM-MHD adds a field $\psi_{\mathrm{GLM}}$ that transports divergence
errors away at a cleaning speed $c_h$; $\nabla\cdot B=0$ is not enforced
exactly. Both GLM sources recompute $c_h$ every step as the largest value
compatible with the CFL condition
([Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md), §6;
[Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md), §5.3, Eqs.
(51)–(52)). They differ in the form of the equations:

- Rueda-Ramírez et al. (2021) keep the **non-conservative** Powell and GLM
  terms, which the entropy analysis needs, discretize them with two-point
  volume and surface terms in the DGSEM and by central differences of
  interface means in the subcell finite volumes, and prove entropy
  stability of the element-wise blend (§3; see
  [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).
- Rueda-Ramírez et al. (2022) solve the **conservative** form, although the
  non-conservative form is needed to prove entropy stability, because the
  conservative form fits their subcell-wise limiting framework (§5.3). On
  the Orszag–Tang vortex ($N=3$, $256^2$ elements, $t=1$) subcell-wise
  density limiting with second-order subcell finite volumes limits less and
  develops more turbulent structure than with first-order ones (§5.3.1).

The earlier paper carries the non-conservative terms with an entropy proof
for element-wise blending; the later one gives them up for subcell-wise
blending, for which the entropy proof is "still missing"
(Rueda-Ramírez et al. 2022, §4 item (2)).

## Projection and cleaning in continuous finite elements

[Dao & Nazarov (2022)](/sources/dao-2022.md) (§3.2, Eqs. (3.6)–(3.7);
§5.3) compare three divergence controls for their residual-viscosity
continuous Galerkin MHD solver:

- **Projection** (Brackbill–Barnes, as recalled): $B\leftarrow B-\nabla\Psi_{\mathrm p}$
  with $\nabla^2\Psi_{\mathrm p}=\nabla\cdot B$ (page-local
  $\Psi_{\mathrm p}$), after which pressure, total energy and entropy
  functions are updated; one Poisson solve per step.
- **Pseudo-time stepping** (Hayashi, as recalled): the same correction
  reached by iterating
  $\partial_{\tilde t}\Psi_{\mathrm p}-\nabla^2\Psi_{\mathrm p}+\nabla\cdot B=0$,
  ten pseudo-iterations per step.
- **Hyperbolic GLM cleaning** (Dedner et al.):
  $\partial_t\psi_{\mathrm{GLM}}+c_h\nabla\cdot B=-\frac{c_rc_h}{h}\psi_{\mathrm{GLM}}$
  with $c_r=0.3$ in 2D and 1 in 3D, $c_h$ the largest modulus of the
  extreme (fast-wave) eigenvalues $\lambda_1$, $\lambda_8$ over the nodes
  and $h$ the local mesh function (page-local $c_r$, $h$), coupled to the
  system by a source term.

On a $40\times40$ $\mathbb P^1$ Orszag–Tang run all three keep
$\int\lvert\nabla\cdot B_h\rvert$ small; pseudo-time stepping is best and
most expensive, projection costs more than GLM cleaning (Fig. 5; cost
stated, no timings). Without any control, Orszag–Tang breaks down around
$t\approx0.7$ on a sufficiently fine mesh (stated; the figure shows only
the coarse run), while up to $t=0.5$ cleaning makes no visible
difference, as Balsara also observed (as recalled). Their production runs
to $t=1$ in 2D and the 3D extension use projection.

## Qualifications

- The Godunov-symmetrization source is non-conservative; Wu & Shu do not
  discuss the resulting conservation error. The source vanishes only where
  the normal field is continuous.
- The extension of Thm 6.4 to SSP time stepping requires the point-value
  hypothesis and the locally divergence-free property at every stage; it is
  stated without a stage-wise argument (§6.2).
- arXiv v1 of Wu & Shu prints the jump coefficient of $\varepsilon_B$ with
  $(\rho^\pm)^{1/2}$ where a Cauchy–Schwarz and AM–GM bound of Eq. (6.21)
  gives $(\rho^\pm)^{-1/2}$ *(compiler check, not in the sources; worked out
  on [geometric quasilinearization](/methods/geometric-quasilinearization.md))*;
  the version of record should decide.
- Liu et al. place their scheme in Wu & Shu's provably positivity-preserving
  framework, but the implemented scheme drops the interior divergence term
  and the paper prints no CFL number, so the guarantee is not established
  for the code; a degree-2 run of the Mach 800 jet fails with negative
  pressure unless the SVD truncation of the least-squares solve is loosened
  (§3.3.3, §4.5).
- Liu et al. (2023a) do not state which discrete divergence enters the
  Cauchy–Kowalewski predictor of the source (Eq. 70); with the locally
  divergence-free reconstruction the in-cell divergence is zero. Their
  divergence comparisons are relative to their own two baseline schemes.
- Lesur et al.'s round-off growth rates ($O(n)$ with super
  time-stepping, $O(\sqrt n)$ without) are stated from their tests with no
  figure; Dao & Nazarov's ranking of cleaning methods rests on one coarse
  $\mathbb P^1$ run without timings.
- Balsara et al.'s constructions preserve the constraint for prolonged
  data; the evolution between regrids relies on the face-centred update
  and on defect correction, whose effect is shown on one 2D linear
  electrodynamics test (§9).
- Chen et al. quantify the divergence on one test only and do not state
  which discrete divergence they measure (§5.2).
- Dzanic & Witherden (2023) do not quantify the divergence added by the
  nonlinear filter; "negligible" is stated (§3.2).
- Berta et al. define the field-loop vector potential as $A_3=A_0(R-r)$
  for $R_1<r\le R$ and zero "elsewhere" (Eq. 54), which makes $A_3$ jump
  by $A_0(R-R_1)$ at $r=R_1$ and would put a singular azimuthal field
  there; a constant $A_3=A_0(R-R_1)$ for $r\le R_1$ gives a field-free
  core without the singular sheet *(compiler check, not in the sources)*.
- Kanbar et al.'s CTM preserves the centred discrete divergence at the
  nodes, not a face-centred divergence *(compiler check, not in the
  sources: the divergence of Eqs. (20)–(21) is the centred nodal one)*, and only in the steps where it is applied; it is applied "whenever needed" without a stated criterion.

- Ding & Wu (2024) apply a locally divergence-free WENO limiter in
  troubled cells before the scaling limiter in their shock tests without
  naming the troubled-cell indicator (§5); their claim that the scaling
  limiter keeps the locally divergence-free space is stated, not proved
  (Remark 8).
- Dematté et al.'s printed signs of the staggered update (Eq. (39)) and
  of $B_2$ from the potential (Eqs. (49), (51)) are reversed; see
  [constrained transport](/methods/constrained-transport.md).

# Citations

- [Berta et al. (2024)](/sources/berta-2024.md) — arXiv v4: §2 (Eqs. (11)–(15)); §3.1 (Eqs. (21)–(22)); §4 (Eqs. (38)–(40)); App. B; §5.1, §5.3–5.4 (Figs. 2–3, 5–7).
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: §6 (Eqs. (6.3)–(6.5), (6.17)–(6.22); Thms 6.1, 6.2, 6.4; Rem. 6.3); §7 (Ex. 7.1–7.2, Figs. 5–6).
- [Liu, Feng & Wang (2023a)](/sources/liu-2023.md) — §2.1–2.2, Eqs. (1)–(7); §3.1.1, Eqs. (19)–(24); §3.1.3; §3.2.2, Eqs. (67)–(70); §4.3–4.6, Eqs. (86)–(87), Figs. 7–11, 16–20.
- [Liu et al. (2021)](/sources/liu-2021.md) — Eq. (1); §3.1–§3.2 (Eqs. (15)–(26)); §3.3.3 (Eqs. (32)–(35)); §4.3 (Fig. 12); §4.5; §5.
- [Kanbar, Touma & Klingenberg (2022)](/sources/kanbar-2022.md) — arXiv v1: §4 (Eqs. (18)–(21)); §5.1–§5.2, §5.5 (Figs. 3–5, 10–11); §6.
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — arXiv v1: §2.2 (Eqs. (13)–(15), (21)–(22)); §3; §6; §6.2 (Figs. 9–10).
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — arXiv v2: §5.3 (Eqs. (51)–(52)); §5.3.1 (Figs. 10–11).
- [Fu (2023)](/sources/fu-2023.md) — §5.3, Fig. 19.
- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — arXiv v2: §5.3 (Eq. (48)).
- [Duan & Tang (2022)](/sources/duan-2022.md) — arXiv v1: §2 (Eqs. (2.4)–(2.5)); §3 (Eqs. (3.4), (3.9), Thm 3.2).
- [Lesur et al. (2023)](/sources/lesur-2023.md) — arXiv v1: §2.4, Eqs. (6)–(8); §2.5; §2.8; §4.2, Fig. 11.
- [Dao & Nazarov (2022)](/sources/dao-2022.md) — arXiv v1: §3.2, Eqs. (3.6)–(3.7); §5.3, Fig. 5; §5.4.
- [Balsara, Samantaray & Subramanian (2023)](/sources/balsara-2023.md) — §1; §2–§5; §7; Tables 2–11.
- [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) — arXiv v1: §2.4, Eqs. (2.15)–(2.17); §3.1; §3.3–3.4, Eq. (3.14); Thm 4.2; §5.1, Table 5.3; §5.2.
- [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) — arXiv v2: §2.3, Eqs. (17)–(19); §3.2, Eqs. (29)–(33); §5.3, Fig. 4.
- [Ding & Wu (2024)](/sources/ding-2024-b.md) — §1; Remark 3; §4.1–4.2 (Eqs. (7), (37)–(51)); §4.4 (Thm 4.1, Eqs. (70)–(74), Remarks 7–8); §4.7 (Thm 4.2); §5, Eqs. (90)–(91), Ex. 5.5, 5.7, 5.9, Figs. 7, 9.
- [Teissier et al. (2024)](/sources/teissier-2024.md) — arXiv v2: §2.3, Eq. (17); §3.1.1; §3.2.3; §3.5, Eq. (55); §4.2.
- [Dematté et al. (2024)](/sources/dematte-2024.md) — §3.3, Eqs. (39)–(51); §4.1.4, Fig. 8; §4.3.2, Fig. 16.

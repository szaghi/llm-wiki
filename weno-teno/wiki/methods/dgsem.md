---
type: Method
title: "Discontinuous Galerkin spectral element method (DGSEM)"
description: "The DGSEM is nodal collocation DG on tensor-product Legendre–Gauss–Lobatto nodes with a diagonal mass matrix and an SBP derivative matrix; the page gives its strong, weak and split (flux-differencing) forms, the curvilinear metric treatment, non-conservative and viscous terms, the subcell flux form used for limiting, positivity of its cell averages, and the codes that implement it."
status: established
aliases: [LGL-DGSEM, DG spectral element method, nodal DGSEM, split-form DGSEM, collocation DG on Gauss–Lobatto nodes]
tags: [dg, entropy-stable, kinetic-energy-preserving, limiting, software]
timestamp: 2026-10-23T10:00:00Z
---

# Discontinuous Galerkin spectral element method (DGSEM)

The DGSEM is the nodal [discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
on quadrilateral or hexahedral elements in which the solution of degree $N$
is a tensor-product Lagrange interpolant at the $N+1$ Legendre–Gauss–Lobatto
(LGL) nodes $\xi_j$ per direction. The integrals are approximated by the
collocated LGL quadrature with weights $\mathsf w_j$. As a result the mass
matrix $M=\mathrm{diag}(\mathsf w_j)$ is diagonal and includes the boundary
nodes. The nodal derivative matrix $D$, with $Q=MD$, is a
[summation-by-parts operator](/operators/summation-by-parts-operator.md),
$Q+Q^\top=B$ ([Ranocha et al. (2023)](/sources/ranocha-2023.md), Ex. 2.3;
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md),
§2.1, Eq. (4)).

## Strong, weak and split forms

On the reference element in 1D, with nodal flux vector $\mathbf f$ and
surface numerical fluxes $h_L$, $h_R$ collected in $\mathbf h$ at the
boundary nodes, the three forms are as follows.

- **Strong form** (Ranocha et al. (2023), Eq. (2.3)):

  $$\frac{d}{dt}\mathbf u+D\mathbf f+M^{-1}B(\mathbf h-\mathbf f)=0.$$

- **Weak form** (Eq. (2.6)):
  $\frac{d}{dt}\mathbf u-M^{-1}D^\top M\mathbf f+M^{-1}B\mathbf h=0$. It is
  algebraically identical to the strong form by the SBP property.
- **Split (flux-differencing) form** (Eq. (2.5)): $D\mathbf f$ is replaced by
  $\sum_m2D_{im}f^{\mathrm{vol}}(u_i,u_m)$, with a symmetric consistent two-point
  volume flux. See [flux differencing](/methods/flux-differencing.md).

Rueda-Ramírez et al. (2022), Eqs. (2)–(4), write the same three forms on a
curvilinear element as a nodal balance:

$$J_i\mathsf w_i\frac{d}{dt}u_i=F^{\mathrm{vol}}_i+\delta_{i0}\hat f_L-\delta_{iN}\hat f_R .$$

The volume term takes one of two forms:

- standard: $F^{\mathrm{vol}}_i=-\sum_m(Q-B)_{im}\tilde f_m$;
- split: $F^{\mathrm{vol}}_i=-\sum_m(2Q-B)_{im}\tilde f^{\mathrm{vol}}_{(i,m)}$.

Here $\tilde f_m=\sum_d(Ja^{(1)}_d)_mf^{(d)}(u_m)$ is the contravariant flux
and $\tilde f^{\mathrm{vol}}_{(i,m)}=f^{\mathrm{vol}}(u_i,u_m)\cdot\{\!\{Ja^{(1)}\}\!\}_{(i,m)}$
the two-point flux with averaged metrics (Eqs. (5)–(6)). The 2D balance has
one such term per direction, weighted by the other direction's quadrature
weight. The standard volume matrix $Q-B=-Q^\top$ is the weak form, and the
split matrix $2Q-B$ is $M\widetilde D$ of Ranocha et al. *(compiler check,
not in the sources: use $Q+Q^\top=B$)*.

The choice of the volume flux decides what the DGSEM preserves:

| volume flux | property | as stated by |
|---|---|---|
| central $\{\!\{f\cdot Ja\}\!\}$ | standard DGSEM | Rueda-Ramírez et al. (2022), Eq. (7) |
| Shima et al. | kinetic energy and pressure equilibrium, not entropy | Ranocha et al. (2023), Eq. (3.7) |
| Ranocha | entropy, kinetic energy and pressure equilibrium | Ranocha et al. (2023), Eq. (3.10) |
| Chandrashekar | entropy and kinetic energy | Rueda-Ramírez et al. (2022), §4–5 |
| Chandrashekar–Klingenberg | entropy (GLM-MHD) | Rueda-Ramírez et al. (2022), §5.3 |

See [entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md),
[entropy stability](/properties/entropy-stability.md) and
[kinetic energy preservation](/properties/kinetic-energy-preservation.md).

A central (standard) volume term can instead be made entropy conservative,
kinetic-energy preserving or both by an element-wise
[entropy correction term](/methods/entropy-correction-term.md) added to
the semi-discretization, without changing the volume flux
([Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md), §2.2, §3.3).
On the inviscid 2D Taylor–Green vortex the two routes behave differently;
see *Variants and evidence* below.

**Collocation removes the face splitting.** On the LGL nodes the face
value of the interpolated flux equals the flux of the face value of the
solution. [Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md)
note that this is why the split form of collocated DG needs no splitting
of the face term, while uncollocated volume nodes (Gauss, or
overintegration) do (§3.1). They also state that Huynh's $g_2$
lumped-Lobatto flux-reconstruction scheme is the collocated LGL DG scheme
in disguise (Remark 3.1); see
[flux reconstruction](/methods/flux-reconstruction.md).

## Curvilinear meshes

The element map gives the Jacobian $J$ and the contravariant metric terms
$Ja^{(n)}_d$, computed at the nodes by applying the SBP derivative to the
node coordinates (Ranocha et al. (2023), Eqs. (2.12)–(2.14)).
Free-stream preservation needs metric terms that satisfy discrete metric
identities; Ranocha et al. refer to the literature for that treatment (§2.3).
Rueda-Ramírez et al. carry the identities over to the subcell level
([free-stream preservation](/properties/free-stream-preservation.md)). The
directional-flux reordering of Ranocha et al. keeps the tensor-product
sparsity on curved meshes (Eq. (2.19)).

[Pazner (2021)](/sources/pazner-2021.md) proves that the strong form with
the discrete metric identity preserves constants, while the weak form in
general does not on curved meshes, and takes the strong form as the
high-order target of his limiter (Prop. 3, §2.4.2). The two forms are
algebraically identical when the face normals are the volume metric terms
at the boundary nodes, so the difference lies in how the normals are
computed *(compiler check, not in the sources; see the qualification on
the free-stream page)*.
[Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) show that on
3D curvilinear hexahedra the entropy-balance residual of the split form
vanishes under the same identities, e.g. for metrics computed as a
discrete curl (App. C.1, Lemma 4).

## Non-conservative and viscous terms

Rueda-Ramírez et al. (2021) discretize the resistive GLM-MHD equations
(nine variables: $\rho$, $\rho v$, $E$, $B$, $\psi_{\mathrm{GLM}}$) with the
split-form DGSEM (§2–3, after Bohm et al.):

- **Non-conservative terms.** The Powell term and the GLM
  Galilean-invariance term enter through a surface two-point term and a
  non-symmetric volume two-point term
  ([flux differencing](/methods/flux-differencing.md), Eqs. (32)–(37)).
- **Visco-resistive terms.** These use the standard DGSEM with BR1 lifting
  applied to the *entropy variables*, $J\mathsf w_kg_k=\sum_nQ_{kn}w_n+$
  boundary corrections, page-local $g$ the lifted gradient (Eqs. (38)–(39)).
  With entropy-variable gradients BR1 keeps entropy stability, as they
  recall from earlier work.
- **Time step.** Five-stage fourth-order SSP-RK of Spiteri–Ruuth, with
  $\Delta t$ the minimum of an advective bound $\propto\Delta x/(2N+1)$ and a
  diffusive one $\propto\Delta x^2/(2N+1)^2$, with empirical factors and CFL
  numbers 0.5 (Eq. (89)).

## Positivity of the cell averages

[Renac (2021)](/sources/renac-2021.md) proves a Zhang–Shu-type result for
an entropy-stable DGSEM on *unstructured* straight-sided quadrilaterals
(Theorem 6.1). The scheme uses his multicomponent EC volume flux and an
entropy-stable, positive relaxation flux at the interfaces. If every nodal
value is admissible, the forward-Euler cell averages stay admissible under

$$\Delta t\,\max_{K}\max_{e}\frac{\lvert\partial K_e\rvert}{\lvert e\rvert}\max_{k}\frac{\lvert\partial K\rvert}{\tilde J^k_K}\,\big\lvert\lambda\big(u_h^\pm(x^k_e)\big)\big\rvert<\frac1{2N(N+1)},$$

with element $K$, page-local faces $e$, sub-triangles $K_e$, wave speed
$\lvert\lambda\rvert=\lvert v\cdot n\rvert+a_{\mathrm L}/\rho$ with the Lagrangian sound speed
$a_{\mathrm L}$ of the relaxation solver, and
$\tilde J^k_K=\min_{e\subset\partial K}J_K(x^k_e)$ the smallest element Jacobian
at the $k$th node of the faces (Eq. (66)). The proof sums the nodal updates and writes the cell average
as a convex combination of interior nodal values and of positive
first-order finite-volume schemes on the boundary traces. It uses the LGL
boundary weight $\mathsf w_0=\mathsf w_N=2/(N(N+1))$, which separates (66) from
the first-order condition, and extends the Cartesian result of Zhang & Shu
through a quadrilateral version of a Perthame–Shu lemma (Lemma 3.2, App. A;
[optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)).
A sequential [scaling limiter](/methods/zhang-shu-scaling-limiter.md) on
density, partial densities and internal energy then restores the nodal
values after each Runge–Kutta stage (Eq. (67)). Renac states that (66) is
not optimal (Remark 6.1). In practice a simpler bound of 0.4 on a
mesh-based CFL number kept positivity in all runs, without a proof (§7).

## Subcell flux form and limiting

Because the LGL mass matrix is diagonal, the whole DGSEM can be written as
differences of high-order inter-node fluxes. The nodal values then act as
subcell values with subcell widths $\mathsf w_i$ in reference space
(Rueda-Ramírez et al. (2022), Eqs. (8)–(11)). A compatible first- or
second-order finite-volume scheme on the same subcells shares the degrees
of freedom. Its subcell normals are derived from the DGSEM metrics. The
DGSEM is made robust by convex blending with that scheme, either one
coefficient $\alpha$ per element or one per subcell interface, with $\alpha$
from a modal-energy indicator or from a posteriori bounds
([subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md),
[convex limiting](/methods/convex-limiting.md),
[troubled-cell indicator](/definitions/troubled-cell-indicator.md)).

[Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) extend the
element-wise blend to systems with non-conservative terms. Only the
advective and non-conservative terms are blended,
$J\mathsf w_j\frac{d}{dt}u_j=(1-\alpha)F^{\mathrm{DG}}_j+\alpha F^{\mathrm{FV}}_j-F^{\nu,\mathrm{DG}}_j$,
and the visco-resistive part $F^{\nu,\mathrm{DG}}$ (page-local) stays pure
DGSEM (Eq. (28)). Their blending lemma keeps the scheme entropy stable for
any element-wise $\alpha$, and their second-order subcell scheme reconstructs
scaled entropy variables with minmod
([TeCNO schemes](/methods/tecno-scheme.md)).

Rueda-Ramírez et al. (2022) prove two results about this construction:

- **Prop. 1.** With first-order reconstruction and the Rusanov flux, the
  subcell scheme *is* Pazner's sparse invariant-domain-preserving low-order
  scheme.
- **Prop. 2.** The subcell metrics solve Pazner's conservation condition for
  the modified metric terms exactly, so the singular-value-decomposition
  step of that construction is unnecessary.

**Whole-element switching on equidistant subcells.** FLEXI's
finite-volume subcell scheme, as described by Mossier et al. (2022),
uses neither the LGL subcells nor a blend. A troubled element is replaced
as a whole ($\alpha\in\{0,1\}$) by a second-order minmod-TVD
finite-volume scheme on $N_{\mathrm{FV}}^d$ subcells that are equidistant
in reference space (page-local $N_{\mathrm{FV}}$ per direction). The DG
data go to the subcells as subcell integral means; the way back is a
least-squares pseudo-inverse constrained by conservation of the element
integral, and DG/FV faces are evaluated on the subcell face distribution
(§4, Eqs. (19)–(30), Fig. 2). The switch is a priori, decided by a
modal-decay indicator before the step and after each stage, which Mossier
et al. contrast with the a posteriori MOOD-type detection of Dumbser et
al. (§1, §7.2; [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).

## Variants and evidence

- **Legendre–Gauss nodes.** Collocation at Gauss nodes needs generalized SBP
  operators, a hybridized operator and an entropy projection to be entropy
  stable. It is 1.5× to 5× more expensive than the LGL-DGSEM at equal $N$
  (Ranocha et al. (2023), §6, Fig. 4).
  Without an entropy-stability requirement, Gauss collocation is the
  baseline of [FLEXI](/software/flexi.md): [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md)
  run a standard (not split-form) Gauss-node DGSEM on curved hexahedra,
  $J\partial_tu+\nabla_\xi\cdot\tilde f=0$ with contravariant fluxes
  $\tilde f^{(d)}=Ja^{(d)}\cdot f$, an explicit four-stage Runge–Kutta
  method and a step proportional to $\Delta x/\big((2N+1)a\big)$
  (maximum signal speed $a$; §3, Eqs. (5)–(18)).
- **Variable degree.** Mossier et al. let the degree vary from element to
  element. A face between degrees $N<M$ (page-local $M$) is evaluated at
  the $M+1$ nodes of the higher degree, after interpolating the lower
  trace, and the flux is returned to degree $N$ by Legendre modal
  truncation; the mixed-degree scheme converges at the order of the lowest
  degree present (§3.3, Eqs. (14)–(17), §8.2 Table 2;
  [h- and hp-adaptation](/methods/hp-adaptation.md)).
- **KPP problem.** With element-wise shock capturing, the standard DGSEM
  converges to a non-entropic solution of the
  [KPP rotating wave](/benchmarks/kpp-rotating-wave.md). The entropy-stable
  split-form DGSEM converges to the entropy solution (Rueda-Ramírez et al.
  (2022), §5.1, $N=3$, up to $256^2$ elements).
- **Further tests.** The split-form DGSEM with the Chandrashekar volume flux
  and subcell limiting runs four further problems (Rueda-Ramírez et al.
  (2022), §5.2–5.3):
  - an under-resolved [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
    at $N=7$;
  - a Mach 4 bow shock on third-order curved elements at $N=5$;
  - the Mach $\approx2000$
    [astrophysical jet](/benchmarks/high-mach-astrophysical-jet.md) at $N=3$;
  - the GLM-MHD [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) at
    $N=3$, with the Chandrashekar–Klingenberg flux.
- **Multicomponent flows.** Renac (2021) runs $N=3$ with SSP-RK(4,3) in the
  ONERA code Aghora. Smooth convection reaches the design order $N+1$
  ($L^1$ errors $9.28\times10^{-5}$, $3.05\times10^{-6}$, $3.03\times10^{-7}$ at
  $h=1/16,1/32,1/64$, observed orders 4.96 and 3.33; Table 1). The
  convergence is irregular on coarse meshes, but Renac states that the
  order $N+1$ is recovered. Two-component Riemann problems, a
  shock–helium bubble on 238 673 unstructured elements, a Richtmyer–Meshkov
  instability with re-shock on $1601\times118$ elements and a Mach 2
  shock–hydrogen bubble on 74 504 unstructured elements run with the
  positivity limiter (§7;
  [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)).
- **Resistive MHD.** Rueda-Ramírez et al. (2021) run the blended scheme in
  FLUXO on the [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)
  ($N=3$ and $7$, up to $1024^2$ degrees of freedom, against Athena), the
  GEM reconnection challenge, where the ES DGSEM alone crashes, and Io's
  interaction with the Jovian plasma torus (165 888 curved hexahedra,
  $N=4$, 20.7 M degrees of freedom) (§6.2–6.4).
- **Invariant-domain limiting.** Pazner (2021) uses the strong-form DGSEM,
  in MFEM, as the target of subcell convex limiting, up to a
  [double Mach reflection](/benchmarks/double-mach-reflection.md) on
  $2400\times600$ elements at $N=3$; at fixed degrees of freedom the results
  improve with $N$ (§5; [convex limiting](/methods/convex-limiting.md)).
- **Correction terms versus flux differencing.** Abgrall, Öffner &
  Ranocha (2022) run nodal DG on LGL nodes with $N=5$ on $16^2$ elements
  on the inviscid 2D [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md),
  with SSP-RK(10,4) and $\Delta t=\frac{\Delta x}{10}\frac1{N^2+1}$
  (§4.2.2). The central DGSEM blows up at $t\approx3.8$. Entropy and
  kinetic-energy correction terms control the two quantities until blow-up
  but do not prevent it ($t\approx4.3$ with both). The split form with an
  entropy-conservative and kinetic-energy-preserving volume flux runs to
  $t\approx35$. The authors attribute the blow-up of the corrected central
  scheme to negative nodal densities or pressures, after which entropy
  variables cannot be formed (§4.2.2, §6). The split form of Ducros et
  al. plus both corrections behaves like flux differencing up to $t=30$
  (Fig. 8).
- **Codes.** The method is implemented in [Trixi.jl](/software/trixi-jl.md)
  (Julia) and [FLUXO](/software/fluxo.md) (Fortran). Their serial
  performance is similar (Ranocha et al. (2023), §4, Fig. 1). The Gauss
  variant is the basis of [FLEXI](/software/flexi.md) (Mossier et al.
  (2022)). Renac (2021) uses Aghora and Pazner (2021) MFEM.

## Qualifications

- "High order" in Rueda-Ramírez et al. (2022) is the formal order of the
  DGSEM of degree $N$. Their §5 reports no convergence study.
- Ranocha et al., Pazner and Renac write the degree $p$; Rueda-Ramírez et
  al. write $N$. Pazner's reference element is $[0,1]^d$, the others' is
  $[-1,1]^d$. Renac prints the sums of his cell average (59)–(60) from
  $1$ instead of $0$; the nodes run from $0$ to $N$.
  Abgrall et al. and Cicchino et al. also write the degree $p$.
  Rueda-Ramírez et al. write the quadrature weights $\omega$, which this
  bundle writes $\mathsf w$ to keep $\omega_k$ for WENO weights; Ranocha et
  al. name no weight symbol and work with the mass matrix $M$.
- Mossier et al. (2022) call their Legendre–Gauss collocation scheme
  "DGSEM" as well; the definition in the lead of this page (LGL nodes,
  boundary nodes in the quadrature) is the convention of the other
  sources.

# Citations

- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — Ex. 2.3, Eqs. (2.3), (2.5), (2.6), (2.12)–(2.19), (3.7), (3.10), §4 Fig. 1, §6 Fig. 4.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.1 Eqs. (2)–(11), §2.2–2.4, §3 Props. 1–2, §5.
- [Pazner (2021)](/sources/pazner-2021.md) — §2 Eqs. (3)–(15), Props. 1–3, §5 (arXiv v1).
- [Renac (2021)](/sources/renac-2021.md) — §5 Eqs. (57)–(64), §6 Theorem 6.1 Eqs. (65)–(67), Remark 6.1, Lemma 3.2, App. A, §7 Table 1 (arXiv v3).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §2–3 Eqs. (28), (31)–(39), §5 Eq. (89), §6, App. C.1 Lemma 4 (arXiv v1).
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — §2.2 Eqs. (20)–(26), §3.3, §4.2.2 Figs. 7–8, §6 (arXiv v4).
- [Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md) — §3.1, Remark 3.1 (arXiv v1).
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — §1, §3 Eqs. (5)–(18), §4 Eqs. (19)–(30) Fig. 2, §7.2, §8.2 Table 2, §9.

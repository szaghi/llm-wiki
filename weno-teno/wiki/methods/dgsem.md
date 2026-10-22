---
type: Method
title: "Discontinuous Galerkin spectral element method (DGSEM)"
description: "The DGSEM is nodal collocation DG on tensor-product Legendre–Gauss–Lobatto nodes with a diagonal mass matrix and an SBP derivative matrix; the page gives its strong, weak and split (flux-differencing) forms, the curvilinear metric treatment, the subcell flux form used for limiting, and the codes that implement it."
status: established
aliases: [LGL-DGSEM, DG spectral element method, nodal DGSEM, split-form DGSEM, collocation DG on Gauss–Lobatto nodes]
tags: [dg, entropy-stable, kinetic-energy-preserving, limiting, software]
timestamp: 2026-10-21T12:00:00Z
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

## Curvilinear meshes

The element map gives the Jacobian $J$ and the contravariant metric terms
$Ja^{(n)}_d$, computed at the nodes by applying the SBP derivative to the
node coordinates (Ranocha et al. (2023), Eqs. (2.12)–(2.14)).
Free-stream preservation needs metric terms that satisfy discrete metric
identities. Ranocha et al. note the usual care with metric terms (§2.3).
Rueda-Ramírez et al. carry the identities over to the subcell level
([free-stream preservation](/properties/free-stream-preservation.md)). The
directional-flux reordering of Ranocha et al. keeps the tensor-product
sparsity on curved meshes (Eq. (2.19)).

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

Rueda-Ramírez et al. (2022) prove two results about this construction:

- **Prop. 1.** With first-order reconstruction and the Rusanov flux, the
  subcell scheme *is* Pazner's sparse invariant-domain-preserving low-order
  scheme.
- **Prop. 2.** The subcell metrics solve Pazner's conservation condition for
  the modified metric terms exactly, so the singular-value-decomposition
  step of that construction is unnecessary.

## Variants and evidence

- **Legendre–Gauss nodes.** Collocation at Gauss nodes needs generalized SBP
  operators, a hybridized operator and an entropy projection to be entropy
  stable. It is 1.5× to 5× more expensive than the LGL-DGSEM at equal $N$
  (Ranocha et al. (2023), §6, Fig. 4).
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
- **Codes.** The method is implemented in [Trixi.jl](/software/trixi-jl.md)
  (Julia) and [FLUXO](/software/fluxo.md) (Fortran). Their serial
  performance is similar (Ranocha et al. (2023), §4, Fig. 1).

## Qualifications

- "High order" in Rueda-Ramírez et al. (2022) is the formal order of the
  DGSEM of degree $N$. Their §5 reports no convergence study.
- Ranocha et al. write the degree $p$ and Rueda-Ramírez et al. write $N$.
  Rueda-Ramírez et al. write the quadrature weights $\omega$, which this
  bundle writes $\mathsf w$ to keep $\omega_k$ for WENO weights; Ranocha et
  al. name no weight symbol and work with the mass matrix $M$.

# Citations

- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — Ex. 2.3, Eqs. (2.3), (2.5), (2.6), (2.12)–(2.19), (3.7), (3.10), §4 Fig. 1, §6 Fig. 4.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.1 Eqs. (2)–(11), §2.2–2.4, §3 Props. 1–2, §5.

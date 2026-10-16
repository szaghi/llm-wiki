---
type: Method
title: "Reduced MHD for stellarators"
description: "Generalization of tokamak reduced MHD in which the fixed toroidal field is replaced by the curl-free coil field ∇χ: the field is ∇χ plus field-line bending ∇ψχ×∇χ and the flow is ∇u×∇χ/|∇χ|²; a full-MHD stellarator equilibrium leaves a residual force of fourth order in the ordering parameter; implemented in JOREK3D with v∥ = 0 and verified on Wendelstein 7-A."
status: established
aliases: [stellarator RMHD, Nikulsin reduced MHD, JOREK3D reduced MHD]
tags: [mhd, reduced-mhd, stellarator, code]
timestamp: 2026-10-16T00:00:00Z
---

# Reduced MHD for stellarators

Tokamak [reduced MHD](/methods/reduced-mhd.md) fixes the toroidal field
$F_0\nabla\phi$ and evolves only the poloidal flux. In a stellarator the
coils produce a three-dimensional vacuum field, so the reduced model fixes
that whole field instead, $\mathbf B_{\rm vac}=\nabla\chi$, and evolves the
plasma-current-induced part. The model was derived by Nikulsin et al.
(2019, 2021) and implemented in JOREK as
[JOREK3D](/software/jorek3d.md)
([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §I–II;
[Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §4.1). In the tokamak
limit $\chi=F_0\phi$ it reduces to the existing JOREK tokamak model, and the
reduction preserves Grad–Shafranov equilibria
([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §II).

## Ansatz

The exact (full-MHD) representation is

$$\mathbf B=\nabla\chi+\nabla\psi_\chi\times\nabla\chi+(\text{compressional term}),\qquad
\mathbf v=\frac{\nabla u\times\nabla\chi}{|\nabla\chi|^2}+(\text{parallel flow along }\mathbf B)+(\text{fast-wave potential term}),$$

where the three velocity terms carry, approximately, the Alfvén, slow and
fast waves, and the compressional field term is the gradient of a second
potential crossed with a Clebsch potential of $\nabla\chi$
([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), Eqs. 1–2). The
reduced model drops the compressional and fast-wave terms and the current
component perpendicular to $\nabla\chi$ in Ohm's law; the JOREK3D paper
further sets $v_\parallel=0$:

$$\mathbf B=\nabla\chi+\nabla\psi_\chi\times\nabla\chi,\qquad \mathbf v=\frac{\nabla u\times\nabla\chi}{|\nabla\chi|^2}$$

([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), Eq. 4). On this page
$\psi_\chi$ is the field-line-bending potential (a length; its tokamak limit
is $\psi/F_0$, and in a stellarator it is not constant on flux surfaces)
and $u$ the stream function of this ansatz; in the tokamak limit
$\mathbf v=(R^2/F_0)\nabla u\times\nabla\phi$, so this $u$ is $F_0$ times
the tokamak stream function up to a sign that depends on orientation
conventions the source does not state (the source writes "$\Phi\to F_0u$").

## Operators

Operators with a superscript refer to the direction of $\nabla\chi$, those
with a subscript to $\mathbf B$
([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §II):

$$\begin{aligned}
\partial^\parallel&=|\nabla\chi|^{-1}\,\nabla\chi\cdot\nabla,\qquad \nabla^\perp=\nabla-|\nabla\chi|^{-1}\nabla\chi\,\partial^\parallel,\qquad \Delta^\perp=\nabla\cdot\nabla^\perp,\\
\Delta^*f&=|\nabla\chi|^{-2}\,\nabla\cdot\big(|\nabla\chi|^2\nabla^\perp f\big),\qquad [f,g]=|\nabla\chi|^{-1}\,\nabla\chi\cdot(\nabla f\times\nabla g).
\end{aligned}$$

For $\chi=F_0\phi$ these reduce to $R^{-1}\partial_\phi$, the $(R,Z)$-plane
gradient, the tokamak $\Delta^*$ and the tokamak bracket
$\mathbf e_\phi\cdot(\nabla f\times\nabla g)$.

## Equations

The source evolves $u$, $\rho$, $p$, $\psi_\chi$ and two auxiliary fields,
the current along $\nabla\chi$ and the contravariant $\chi$ vorticity, both
taken with the opposite sign,

$$j=-\frac{\nabla\chi\cdot\mathbf J}{|\nabla\chi|^2},\qquad \varpi=-\nabla\chi\cdot\nabla\times\mathbf v.$$

The system ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), Eqs. 3a–f,
with the source term of the density written out) is

$$\begin{aligned}
\nabla\cdot\Big(\frac{\rho}{|\nabla\chi|^2}\nabla^\perp\partial_tu\Big)&=\frac{|\nabla\chi|}{2}\Big[\frac{\rho}{|\nabla\chi|^2},\frac{|\nabla^\perp u|^2}{|\nabla\chi|^2}\Big]+|\nabla\chi|\Big[\frac{\rho\varpi}{|\nabla\chi|^4},u\Big]-\nabla\cdot\Big(\frac{\sigma_\rho}{|\nabla\chi|^2}\nabla^\perp u\Big)\\
&\quad+\nabla\cdot(j\mathbf B)+|\nabla\chi|\Big[\frac1{|\nabla\chi|^2},p\Big]+\nabla\cdot(\nu_\perp\nabla^\perp\varpi)-\Delta^\perp(\nu_h\Delta^\perp\varpi),\\
\partial_t\rho&=-|\nabla\chi|\Big[\frac{\rho}{|\nabla\chi|^2},u\Big]+\sigma_\rho,\qquad \sigma_\rho\equiv\nabla\cdot(D_\perp\nabla_\perp\rho+D_\parallel\nabla_\parallel\rho)+S_\rho,\\
\partial_tp&=-\frac{1}{|\nabla\chi|}[p,u]-\Gamma p\,|\nabla\chi|\Big[\frac1{|\nabla\chi|^2},u\Big]+\nabla\cdot\Big[(\Gamma-1)(\kappa_\perp\nabla_\perp T+\kappa_\parallel\nabla_\parallel T)+\frac{pD_\perp}{\rho}\nabla_\perp\rho+\frac{pD_\parallel}{\rho}\nabla_\parallel\rho\Big]\\
&\quad+(\Gamma-1)\big(S_p+\eta_{\rm Ohm}|\nabla\chi|^2j^2\big),\\
\partial_t\psi_\chi&=\frac{\partial^\parallel u-[\psi_\chi,u]}{|\nabla\chi|}-\eta\,(j-j_{\rm eq})+\nabla\cdot(\eta_h\nabla^\perp j),\\
\mu_0\,j&=\Delta^*\psi_\chi,\qquad \varpi=\Delta^\perp u.
\end{aligned}$$

$\sigma_\rho$ is a page-local shorthand for the mass source, $\nu_\perp$ a
"viscosity-like" coefficient (not the physical dynamic viscosity), $\nu_h$
a hyperviscosity, $\eta_h$ a hyper-resistivity, $\eta_{\rm Ohm}$ a separate
resistivity for Ohmic heating (so that an artificially high $\eta$ need not
heat the plasma) and $j_{\rm eq}$ the initial current
([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §II). The source
prints $\tilde j=\Delta^*\Psi$ in JOREK normalization; $\mu_0$ is restored
here from its SI definition of $\tilde j$, which carries $1/\mu_0$. With
that definition the other equations are dimensionally consistent in SI
as printed (compiler's check). The resistive term of the
$\psi_\chi$ equation is reproduced with its printed sign, which is
anti-diffusive given $\mu_0j=\Delta^*\psi_\chi$; the open entry on
[reduced MHD](/methods/reduced-mhd.md) (*Contradictions*) records it. The
vorticity equation is obtained by
applying $\nabla\chi\cdot\nabla\times(|\nabla\chi|^{-2}\,\cdot\,)$ to the
momentum equation; viscous terms are added after the projection. The
auxiliary fields are separate finite-element unknowns, which avoids
second derivatives in the weak form on the $G^1$ elements, except in the
hyperviscous term (same section; see
[Bézier finite elements](/methods/bezier-finite-elements.md)).

## Equilibrium compatibility: the residual force

With the ordering $\lambda_{\rm o}=L_\perp/L_\parallel$,
$|\partial^\parallel|\sim\lambda_{\rm o}|\nabla^\perp|$,
$\psi_\chi=O(\lambda_{\rm o})$, $u,v_\parallel=O(\lambda_{\rm o})$,
$\partial_t=O(\lambda_{\rm o})$, $\rho=O(1)$ and $p=O(\lambda_{\rm o}^2)$, a
full-MHD stellarator equilibrium is not an exact equilibrium of the reduced
equations. The residual force, the difference of the full and reduced
Lorentz forces, enters the vorticity and parallel-velocity equations at
$O(\lambda_{\rm o}^4)$, against leading terms of $O(\lambda_{\rm o}^2)$,
and is present even at zero β
([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §II, Eqs. 8–12). In
the W7-A runs an initial transient, attributed to the neglected
fourth-order terms and to the different JOREK and GVEC discretizations,
has a kinetic energy of about $10^{-7}$ J that decays to about
$2\times10^{-11}$ J within about 0.02 ms; it is damped by implicit-Euler
steps before the run switches to Crank–Nicolson (§V, Fig. 4).

## Vacuum field and initial state

$\chi$ is represented analytically by
[Dommaschk potentials](/methods/dommaschk-potentials.md), so that
$\Delta\chi=0$ and $\nabla\cdot\mathbf B=0$ hold to machine precision; a
finite-element $\chi$ would make the advective terms discontinuous on $G^1$
elements ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §II–III;
see [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).
The initial current comes from the GVEC equilibrium,
$j_{\rm eq}=-\nabla\chi\cdot\nabla\times\mathbf B_{\rm GVEC}/(\mu_0|\nabla\chi|^2)$,
dropping an $O(\lambda_{\rm o}^3)$ term; $\psi_\chi$ follows from
$\mu_0j_{\rm eq}=\Delta^*\psi_\chi$, with a non-homogeneous Dirichlet
condition obtained from $\mathbf n\cdot\mathbf B=0$ on the boundary,
$\mathbf n\cdot(\nabla\psi_\chi\times\nabla\chi)=-\mathbf n\cdot\nabla\chi$,
solved by a Fourier–Galerkin method that excludes the $m=0$ kernel
(§IV, Eqs. 32–35). The grid is flux-surface aligned and its $(R,Z)$
geometry has its own toroidal Fourier expansion (App. A); see
[three-dimensional inverse equilibrium solvers](/methods/inverse-equilibrium-solvers.md)
for GVEC.

## Results and limits

* The linearized ideal reduced operator is self-adjoint, so ideal
  perturbations have real $\omega^2$
  ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), App. B).
* Four stable W7-A equilibria (β up to 0.022%) keep the magnetic axis and
  the flux surfaces fixed for about 7 ms, with an axis offset from GVEC of
  at most about $10^{-4}$ m attributed to the reduced ansatz (§V,
  Figs. 5–6).
* Linear growth rates agree with the full-MHD code CASTOR3D within 13.2%
  (β scan) and 26.2% (η scan) for the $(2,1)$ tearing mode and within 6.4%
  for ballooning modes, JOREK3D being higher; the tearing gap is attributed
  to $v_\parallel=0$ and the ballooning gap mostly to spectral blocking
  (§VI–VII; numbers on [JOREK3D](/software/jorek3d.md)).
* In a five-period stellarator, toroidal harmonics couple linearly in
  families $n\pm5k$, e.g. $\{1,4,6,9\}$, $\{2,3,7,8\}$, $\{0,5,10\}$
  (§V–VI).
* The reduced family "cannot accurately reproduce kink modes at higher β",
  and whether it holds at β of 3–5% "remains to be seen" (§VIII); the
  tokamak counterpart of the kink limitation is derived in
  [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.3.3 (see
  [reduced MHD](/methods/reduced-mhd.md)).
* JOREK3D has since been benchmarked linearly for classical stellarators
  and in the tokamak limit; JOREK also has an axisymmetric "virtual
  current" model that approximates the external rotational transform, and
  saturated external modes in JOREK agree qualitatively with VMEC
  free-boundary equilibria with the same dominant $n$, with differences in
  the magnetic-energy spectrum and topology
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §4.1;
  [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §7, where the
  quasi-axisymmetric stellarator is treated with "virtual coil currents").
  [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.15, list stellarator
  reduced and full MHD formulations, then not implemented, as an outlook.

# Citations

* [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — model, residual-force ordering, implementation and W7-A verification.
* [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — later JOREK3D benchmarks, virtual-current model, VMEC comparisons.
* [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — stellarator outlook and the kink limitation of the reduced family.

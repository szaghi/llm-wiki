---
type: Definition
title: "Quasi-symmetry"
description: "Property of a stellarator field whose strength, in Boozer coordinates, depends on the flux label and on a single helical angle combination only, B = B(ψ, Mθ − Nζ); it gives guiding-centre conservation analogous to axisymmetry and lets tokamak neoclassical results, such as bootstrap-current fits, be mapped to the stellarator."
status: established
aliases: [QS, quasisymmetry, quasi-axisymmetry, QA, quasi-helical symmetry, QH]
tags: [stellarator, equilibrium, bootstrap-current]
timestamp: 2026-10-16T00:00:00Z
---

# Quasi-symmetry

A magnetic field is quasi-symmetric when, in Boozer coordinates
$(\psi,\theta,\zeta)$, its strength depends only on the flux label and on
one combination of the angles,

$$B=B(\psi,\,M\theta-N\zeta),$$

with integers $M$ and $N$ (page-local helicity numbers). The vector field
itself need not be symmetric; the symmetry of $B$ is enough to give the
guiding-centre motion a conserved quantity, as in a tokamak
([Saxena et al. (2025)](/sources/saxena-2025.md), §1). The cases are:

* **quasi-axisymmetry (QA)**, $M=1$, $N=0$: $B=B(\psi,\theta)$, a tokamak-like
  dependence in a three-dimensional geometry;
* **quasi-helical symmetry (QH)**, $N\ne0$: $B$ depends on a helical angle
  ([Panici et al. (2023)](/sources/panici-2023.md), §5.4).

Saxena et al. (2025) write the helical angle as $\theta-N\zeta$ for their
QA cases, with $N=0$ (Eq. 2.3, App. B); the general $(M,N)$ form appears in
their quasi-symmetry error (Eq. 3.3).

## Measuring the departure from quasi-symmetry

A computed field is never exactly quasi-symmetric. The two-term error used
as a diagnostic is

$$F_{\rm QS}=\Big\langle\Big\{\frac{1}{B^3}\Big[(N-\iota M)\,\mathbf B\times\nabla B\cdot\nabla\psi-(MG+NI)\,\mathbf B\cdot\nabla B\Big]\Big\}^2\Big\rangle,$$

with $\langle\cdot\rangle$ the flux-surface average and $G$, $I$ the Boozer
covariant field components: $\mu_0/2\pi$ times the poloidal current outside
and the toroidal current inside the surface
([Saxena et al. (2025)](/sources/saxena-2025.md), Eq. 3.3, citing Helander
& Simakov 2008 and Paul et al. 2020). In nonlinear M3D-C1 runs of a QA
stellarator at $\beta=2.5\%$, $F_{\rm QS}$ evaluated on temperature
isotherms rises from about $10^{-5}$ to $10^{-3}$ across the radius and
does not change appreciably over $0<t<250\,\tau_A$; quasi-symmetry is
therefore kept until the surfaces break (§3.3, Fig. 8). The
$F_{\rm QS}$ computed by SFINCS at $t=0$ is lower by a factor of about 2–3,
which the paper does not discuss (Fig. 8).

## Why it matters for MHD codes

* **Bootstrap current.** In a quasi-symmetric field the tokamak
  bootstrap-current fits map to the stellarator through an isomorphism
  (Landreman, Buller & Drevlak 2022): $F\to G+NI$,
  $\partial/\partial\psi\to\partial/\partial\psi_t$ divided by $(\iota-N)$,
  and the inverse aspect ratio
  $\to(B_{\max}-B_{\min})/(B_{\max}+B_{\min})$ on the surface. M3D-C1 uses
  this "Sauter–Redl–Landreman" form, which is valid only in quasi-symmetric
  geometry ([Saxena et al. (2025)](/sources/saxena-2025.md), Eq. 2.3,
  App. B, §2; see [bootstrap current](/definitions/bootstrap-current.md)).
  The QA verification against SFINCS is "in close agreement" (§3.2,
  Fig. 4).
* **Equilibrium accuracy near the axis.** For a finite-β QH equilibrium
  (aspect ratio about 20, zero net toroidal current, $\iota\approx-1.14$),
  near-axis expansions for quasi-symmetric fields (Landreman & Jorge 2020)
  give asymptotic Mercier coefficients. DESC reproduces them down to the
  axis; VMEC deviates near the axis even with 801 radial surfaces
  ([Panici et al. (2023)](/sources/panici-2023.md), §5.4, Eqs. 5.9–5.10,
  Fig. 15; see
  [inverse equilibrium solvers](/methods/inverse-equilibrium-solvers.md)).
  The configuration is Mercier-unstable.
* **Optimization targets.** The QA configurations simulated nonlinearly in
  M3D-C1 come from bootstrap-consistent QA optimization (SIMSOPT); they
  remain MHD-unstable with and without the bootstrap current, and higher
  resistivity raises the instability growth
  ([Saxena et al. (2025)](/sources/saxena-2025.md), §3.3, Figs. 5–7).

# Citations

* [Saxena et al. (2025)](/sources/saxena-2025.md) — definition, QA cases, $F_{\rm QS}$ diagnostic, bootstrap isomorphism.
* [Panici et al. (2023)](/sources/panici-2023.md) — quasi-helically symmetric equilibrium and near-axis Mercier verification.

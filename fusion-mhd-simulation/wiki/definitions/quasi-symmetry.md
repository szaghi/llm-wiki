---
type: Definition
title: "Quasi-symmetry"
description: "Property of a stellarator field whose strength, in Boozer coordinates, depends on the flux label and on a single helical angle combination only, B = B(ψ, Mθ − Nζ); it gives guiding-centre conservation analogous to axisymmetry and lets tokamak neoclassical results, such as bootstrap-current fits, be mapped to the stellarator, but a quasi-axisymmetric reactor configuration optimized without a stability target is violently MHD-unstable at its edge."
status: established
aliases: [QS, quasisymmetry, quasi-axisymmetry, QA, quasi-helical symmetry, QH]
tags: [stellarator, equilibrium, bootstrap-current, mhd]
timestamp: 2026-10-16T20:00:00Z
---

# Quasi-symmetry

A magnetic field is quasi-symmetric when, in Boozer coordinates
$(\psi_t,\theta,\zeta)$, its strength depends only on the flux label and on
one combination of the angles,

$$B=B(\psi_t,\,M\theta-N\zeta),$$

with integers $M$ and $N$ (the registry's helicity integers, §9; the
source writes the flux label as $\psi$, here the toroidal flux $\psi_t$ of
the stellarator pages). The vector field
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

$$F_{\rm QS}=\Big\langle\Big\{\frac{1}{B^3}\Big[(N-\iota M)\,\mathbf B\times\nabla B\cdot\nabla\psi_t-(MG+NI)\,\mathbf B\cdot\nabla B\Big]\Big\}^2\Big\rangle,$$

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
  ([Saxena et al. (2025)](/sources/saxena-2025.md), §3.3, Figs. 5–7; but
  see *Contradictions* for how this relates to Wright & Ferraro 2024).
  The reactor-scale $N_{\rm fp}=2$ QA of Landreman, Buller & Drevlak (2022,
  as cited), optimized at $\beta=2.5\,\%$ for quasi-symmetry,
  energetic-particle confinement and a self-consistent bootstrap current
  but not for MHD stability, is "highly unstable to multiple MHD modes
  that grow on Alfvénic timescales": edge high-$n$ modes make 5–10 % of
  the minor radius chaotic within about $500\tau_A$ and engulf the core by
  about $1500\tau_A$ in full-torus M3D-C1 runs, for every resistivity
  model tried ([Wright & Ferraro (2024)](/sources/wright-2024.md), §II–III;
  details on
  [edge instabilities of an optimized QA reactor stellarator](/results/stellarator-edge-instability-qa.md)).
  The authors conclude that MHD stability is "at least as important a
  target for optimization" as the neoclassical ones and that linear
  stability predictions should be used with caution (§I, §IV).

## Contradictions

* **Does the QA instability grow faster with resistivity?** *Open.*
  [Saxena et al. (2025)](/sources/saxena-2025.md) (§3.3, Fig. 7) find, in
  their own QA runs with Spitzer multipliers 1, 10, $10^3$ and $10^4$, that
  kinetic energy grows faster with larger resistivity with the bootstrap
  current on or off, and state that "instability growth still increases
  with resistivity, supporting Wright & Ferraro (2024a)".
  [Wright & Ferraro (2024)](/sources/wright-2024.md) state the opposite
  emphasis for their runs: the evolution is "qualitatively identical,
  regardless of resistivity model", which "is indicative of an ideally
  unstable plasma" (§III–IV). Their maximum kinetic-energy growth rates
  (Fig. 3, constant $\eta$ and Spitzer multipliers 1, 10, 100) are not
  monotonic in the multiplier: the $1\times$ Spitzer case lies above the
  $10\times$ case for most $n$, the $100\times$ case is highest at high
  $n$, and the constant-$\eta$ case is lowest at low $n$; at $n=30$ the
  higher multipliers peak earlier (Fig. 5). Saxena et al.'s own trend over
  a wider multiplier range is not in question; what conflicts is the
  characterization of Wright & Ferraro's result as resistivity-driven
  growth. The two runs also differ in resolution (36 against 72 toroidal
  planes) and multiplier range, so neither paper's data decide the
  question for the other's runs.

# Citations

* [Saxena et al. (2025)](/sources/saxena-2025.md) — definition, QA cases, $F_{\rm QS}$ diagnostic, bootstrap isomorphism.
* [Panici et al. (2023)](/sources/panici-2023.md) — quasi-helically symmetric equilibrium and near-axis Mercier verification.
* [Wright & Ferraro (2024)](/sources/wright-2024.md) — nonlinear instability of a stability-unoptimized QA reactor configuration; stability as an optimization target.

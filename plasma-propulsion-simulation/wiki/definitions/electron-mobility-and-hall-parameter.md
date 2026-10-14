---
type: Definition
title: "Cross-field electron mobility and the Hall parameter"
description: "The electron mobility tensor of a magnetized drift-diffusion model, whose perpendicular component is the parallel mobility divided by one plus the square of the Hall parameter omega_ce/nu_e; Hall-thruster values of the Hall parameter make the tensor strongly anisotropic and ill-conditioned for numerics."
status: established
aliases: [Hall parameter, electron mobility tensor, cross-field mobility, perpendicular mobility, classical mobility, electron magnetization]
tags: [anomalous-transport, fluid, hall-thruster, numerics]
timestamp: 2026-10-14T00:00:00Z
---

# Cross-field electron mobility and the Hall parameter

## Definitions

In the inertialess (drift-diffusion) electron momentum balance used by
[electron fluid models](/methods/electron-fluid-model.md), the electron
flux responds to the electric field and the pressure gradient through a
mobility tensor
([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.1,
eqs. 11–13, attributed to Hagelaar et al. 2011;
[Ahedo (2023)](/sources/ahedo-2023.md), Eqs. 13–16). Its components are

$$\mu_\parallel=\frac{e}{m_e\nu_e},\qquad \mu_\perp=\frac{\mu_\parallel}{1+\Omega_e^2},\qquad \Omega_e=\frac{\omega_{ce}}{\nu_e},$$

along and across $\mathbf B$, and the off-diagonal (Hall, $\mathbf E\times\mathbf B$)
component is $\pm\mu_\parallel\Omega_e/(1+\Omega_e^2)$ (Taccogna & Garrigues
2019, eq. 12). The Hall parameter $\Omega_e$ is the number of electron
gyrations per momentum-transfer collision. The same perpendicular mobility
appears in the 1D axial fluid models of
[Giannetti et al. (2021)](/sources/giannetti-2021.md) (eqs. 12–13) and
[Saravia et al. (2026)](/sources/saravia-2026.md) (eq. 5). In the 2D
[five-moment model](/methods/five-moment-fluid-model.md), the same factor
$1/(1+\Omega_e^2)$ relates the perpendicular to the field-aligned electron
thermal conductivity
([Troyetsky et al. (2026)](/sources/troyetsky-2026.md), Eqs. 10–13).

**Momentum-transfer frequency.** $\nu_e$ sums the collision processes the
model keeps, and the anomalous term is added to it:
* electron–neutral elastic, ionization and excitation collisions, plus an
  electron–wall term and the anomalous term
  ([Giannetti et al. (2021)](/sources/giannetti-2021.md), eq. 10);
* $n_n$ times a constant electron–neutral momentum-transfer rate
  coefficient, plus a constant wall term
  $10^7$ s⁻¹ inside the channel, plus the anomalous term
  ([Saravia et al. (2026)](/sources/saravia-2026.md), eq. 6)¹;
* electron–neutral elastic $2.5\times10^{-13}n_n$ s⁻¹ (with $n_n$ in m⁻³,
  after Boeuf & Garrigues), inelastic scattering and the anomalous term,
  with excitation and Coulomb collisions neglected
  ([Troyetsky et al. (2026)](/sources/troyetsky-2026.md), Eqs. 6–9).

With a Bohm-type anomalous closure (see
[Anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md)),
the effective Hall parameter is $\omega_{ce}/(\nu_e+\nu_{\mathrm{ano}})$.
Ahedo (2023, Eqs. 26–29) shows that when the anomalous force acts only on
the azimuthal equation, the in-meridian perpendicular current is set by
the denominator $1+\Omega_e\,\omega_{ce}/(\nu_e+\nu_{\mathrm{ano}})$, the
product of the classical and the effective Hall parameters; with an
isotropic anomalous force both factors become effective.

Reza et al. (2022, §3.1) call the ratio $\omega_{ce}/\nu_e$ the Hall
parameter and specify their zone-wise Bohm closure through it
([Reza et al. (2022)](/sources/reza-2022.md)).

## Magnitudes and consequences

* Hall thrusters use a field of about 0.01 T (SPT-100: about 0.02 T peak;
  printed as 100 G and 200 G) to
  magnetize the electrons but not the ions
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §1;
  [Boyd (2005)](/sources/boyd-2005.md), §3.4), which is why electrons are
  modelled as a fluid and ions kinetically in the hybrid codes Boyd
  reviews.
* Parallel and perpendicular derivatives in the electron equations differ
  by a factor of order $\Omega_e$ times the effective Hall parameter, "say
  $O(10^5)$ in conventional HETs"
  ([Ahedo (2023)](/sources/ahedo-2023.md), Eqs. 33–35). In the
  acceleration region the ratio of the parallel to the perpendicular
  electric force is about 1/10 and the ratio of perpendicular to azimuthal
  electron current is about 1/100 (Eq. 25).
* For $\Omega_e\gg1$ the mobility tensor is ill-conditioned, "the key
  difficulty" for accurate numerics (Ahedo 2023, Eqs. 15–17). Written in
  $r$–$z$ components, the current-continuity equation becomes a strongly
  anisotropic five-point elliptic problem whose flux is a sum of large
  opposite-sign terms, so that numerical error can dominate cross-field
  transport (Taccogna & Garrigues 2019, §2.2, eq. 20, attributed to
  Hagelaar 2016). Both reviews present the
  [magnetic-field-aligned mesh](/methods/magnetic-field-aligned-mesh.md)
  and the [thermalized potential](/definitions/thermalized-potential.md)
  as the remedy. On a 3D Cartesian mesh, the EP2PLUS code is reliable only
  for an effective Hall parameter up to 50–100 (Ahedo 2023, §EP2PLUS,
  attributed to his ref. 87).
* The measured electron current exceeds what the classical mobility with
  electron–atom collisions allows ([Boyd (2005)](/sources/boyd-2005.md),
  §3.4, Fig. 16): this excess is
  [anomalous transport](/definitions/anomalous-electron-transport.md). A
  2D hybrid model whose $\mu_\perp$ profile is adjusted to laser-induced
  fluorescence ion velocities reproduces a shorter acceleration region
  than one fitted to discharge current and performance (Taccogna &
  Garrigues 2019, §2.5, Fig. 5, attributed to Garrigues et al. 2009).
* An effective cross-field mobility from correlated azimuthal fluctuations
  is on
  [Instability-enhanced electron–ion friction](/results/instability-enhanced-friction-force.md).

¹ Saravia et al. (2026, §2.1) print the electron–neutral
momentum-transfer rate coefficient as $2.5\times10^{13}$ m³/s; the
positive exponent is not physical, and the value
$2.5\times10^{-13}$ m³/s used by Troyetsky et al. (2026) after the same
Boeuf & Garrigues model is the likely intent (compiler note).

# Citations

1. [Boyd (2005)](/sources/boyd-2005.md), §3.4, Fig. 16.
2. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §§1, 2.1, 2.2, 2.5, eqs. 11–13, 20, Fig. 5 (accepted manuscript).
3. [Giannetti et al. (2021)](/sources/giannetti-2021.md), §2.3, eqs. 10, 12–13.
4. [Reza et al. (2022)](/sources/reza-2022.md), §3.1 (preprint).
5. [Ahedo (2023)](/sources/ahedo-2023.md), §3D, Eqs. 13–17, 25–29, 33–35; EP2PLUS section.
6. [Troyetsky et al. (2026)](/sources/troyetsky-2026.md), Eqs. 6–13.
7. [Saravia et al. (2026)](/sources/saravia-2026.md), §2.1, eqs. 5–6.

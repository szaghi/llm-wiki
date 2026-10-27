---
type: Definition
title: "Reduced MHD and Elsasser variables"
description: "Reduced MHD is the strong-guide-field, anisotropic limit of MHD written in Elsasser variables; it conserves each Elsasser energy, couples only counter-propagating fields, and has a rescaling symmetry that any scaling theory of MHD turbulence must respect."
status: established
aliases: [RMHD, reduced magnetohydrodynamics, Strauss equations, Elsasser fields, Elsasser variables]
tags: [mhd, plasma, astrophysics, dns]
timestamp: 2026-10-27T15:46:00Z
---

# Reduced MHD and Elsasser variables

**Reduced MHD (RMHD)** is the limit of magnetohydrodynamics in which a strong
mean (guide) field $\boldsymbol B_0=B_0\hat{\boldsymbol z}$ makes the
fluctuations anisotropic, $k_\parallel/k_\perp\ll1$, small,
$\boldsymbol b_\perp/v_A\sim k_\parallel/k_\perp$, and slow, with rates of
order $k_\parallel v_A$. Written in the **Elsasser fields**
$\boldsymbol Z^\pm_\perp=\boldsymbol u_\perp\pm\boldsymbol b_\perp$ (with
$\boldsymbol b_\perp$ in velocity units, $v_A=B_0/\sqrt{4\pi\rho}$), it is the
model system on which the scaling theories of strong MHD turbulence reviewed
by [Schekochihin (2022)](/sources/schekochihin-2022.md) are built: the
[critically balanced cascade](/properties/critical-balance.md), [dynamic
alignment](/properties/dynamic-alignment.md) and [tearing-mediated
turbulence](/results/tearing-mediated-mhd-turbulence.md). Schekochihin
(2022, §3) credits RMHD to Kadomtsev & Pogutse (1974) and Strauss (1976),
and the Elsasser variables to Elsasser (1950).

## Equations

In the notation of the registry (Schekochihin 2022, Eqs. 3.1–3.2, written
there with equal viscosity and magnetic diffusivity, $\nu=\eta_m$, until §6.4):

$$\begin{aligned}
&\partial_t\boldsymbol Z^\pm_\perp\mp v_A\nabla_\parallel\boldsymbol Z^\pm_\perp+\boldsymbol Z^\mp_\perp\cdot\nabla_\perp\boldsymbol Z^\pm_\perp=-\nabla_\perp p+\eta_m\nabla_\perp^2\boldsymbol Z^\pm_\perp+\boldsymbol f^\pm,\\
&\nabla_\perp^2p=-\nabla_\perp\nabla_\perp:\boldsymbol Z^+_\perp\boldsymbol Z^-_\perp,
\end{aligned}$$

where $p$ is the total (thermal plus magnetic) pressure divided by $\rho$,
fixed by $\nabla_\perp\cdot\boldsymbol Z^\pm_\perp=0$, and $\boldsymbol f^\pm$
are Elsasser forcings. $\boldsymbol Z^+$ propagates along $+\boldsymbol B_0$
(the sign convention of the registry).

**Derivation and validity.** Schekochihin (2022, §3) recalls that RMHD follows
from compressible MHD with all perturbations ordered like the Mach number and
like $k_\parallel/k_\perp\ll1$, with frequencies $\sim k_\parallel v_A$; it
also describes the Alfvénic part of low-frequency collisionless plasma
dynamics near a gyrotropic equilibrium (the review cites Schekochihin et al.
2009 and Kunz et al. 2015). Section 13 of the review argues that even MHD
turbulence without an imposed mean field "turns itself into" RMHD below the
fold scale of the [small-scale dynamo](/results/small-scale-dynamo.md).

**Scalar (potential) form.** With Elsasser potentials,
$\boldsymbol Z^\pm_\perp=\hat{\boldsymbol z}\times\nabla_\perp\zeta^\pm$, and
Elsasser vorticities $\varpi^\pm=\nabla_\perp^2\zeta^\pm$ (both page-local
symbols; the source writes $\omega^\pm$), Schekochihin (2022, App. A.1,
Eq. A2) writes

$$\partial_t\varpi^\pm\mp v_A\nabla_\parallel\varpi^\pm=-\{\zeta^\mp,\varpi^\pm\}+\{\partial_j\zeta^\pm,\partial_j\zeta^\mp\},$$

with the Poisson bracket $\{f,g\}=\hat{\boldsymbol z}\cdot(\nabla_\perp f\times\nabla_\perp g)$
(page-local). The first term is advection of one Elsasser vorticity by the
other field; the second is a "vortex-stretching" term of opposite sign for the
two fields. In Fourier space the nonlinearity couples triads
$\boldsymbol k=\boldsymbol p+\boldsymbol q$ with the coefficient
$q_\perp^2\sin\phi\cos\phi$, $\phi$ the angle between
$\boldsymbol k_\perp$ and $\boldsymbol q_\perp$ (Eqs. A4–A5).

**Strauss form.** With a stream function $\Phi$ and a flux function $\Psi$
(page-local), $\boldsymbol u_\perp=\hat{\boldsymbol z}\times\nabla_\perp\Phi$,
$\boldsymbol b_\perp=\hat{\boldsymbol z}\times\nabla_\perp\Psi$, so
$\zeta^\pm=\Phi\pm\Psi$, and with separate $\nu$ and $\eta_m$
(Schekochihin 2022, App. D, Eqs. D2–D3):

$$\begin{aligned}
&\partial_t\nabla_\perp^2\Phi+\{\Phi,\nabla_\perp^2\Phi\}=v_A\nabla_\parallel\nabla_\perp^2\Psi+\{\Psi,\nabla_\perp^2\Psi\}+\nu\nabla_\perp^4\Phi,\\
&\partial_t\Psi+\{\Phi,\Psi\}=v_A\nabla_\parallel\Phi+\eta_m\nabla_\perp^2\Psi.
\end{aligned}$$

This is the form in which the review derives the tearing instability (see
[tearing-mediated MHD turbulence](/results/tearing-mediated-mhd-turbulence.md)).

## Properties

Schekochihin (2022, §3, items (i)–(v)) lists the properties every scaling
theory uses.

1. **Decoupling.** Alfvénic perturbations decouple from compressive and
   kinetic ones; the latter are passively advected.
2. **Only counter-propagating fields interact.** The nonlinearity is
   $\boldsymbol Z^\mp_\perp\cdot\nabla_\perp\boldsymbol Z^\pm_\perp$, so a
   state with $\boldsymbol Z^-_\perp=0$ (that is,
   $\boldsymbol u_\perp=\boldsymbol b_\perp$, or the reverse) is an exact
   nonlinear solution — an **Elsasser state**, a finite-amplitude Alfvén wave
   travelling in one direction.
3. **Two conserved energies.** Each Elsasser energy obeys
   $$\frac{\partial}{\partial t}\frac{\langle|\boldsymbol Z^\pm_\perp|^2\rangle}{2}=\varepsilon^\pm-\eta_m\langle|\nabla_\perp\boldsymbol Z^\pm_\perp|^2\rangle,\qquad\varepsilon^\pm=\langle\boldsymbol Z^\pm_\perp\cdot\boldsymbol f^\pm\rangle$$
   (Eq. 3.3), where $\langle\cdot\rangle$ is a volume average and
   $\varepsilon^\pm$ are the Elsasser energy injection rates (equal to the
   cascade fluxes in a steady state). Equivalently, the total energy
   $\langle|\boldsymbol u_\perp|^2+|\boldsymbol b_\perp|^2\rangle/2$ and the
   cross-helicity $\langle\boldsymbol u_\perp\cdot\boldsymbol b_\perp\rangle$
   are ideal invariants (Eq. 3.4). Turbulence with
   $\varepsilon^+\ne\varepsilon^-$ is called **imbalanced** (see [critical
   balance](/properties/critical-balance.md)).
4. **Rescaling symmetry.** For any amplitude factor $c$ and length factor $a$
   (page-local), the equations are invariant under (Eq. 3.5)
   $$\boldsymbol Z^\pm_\perp\to c\,\boldsymbol Z^\pm_\perp,\quad \boldsymbol f^\pm\to\frac{c^2}{a}\boldsymbol f^\pm,\quad \nabla_\perp\to\frac{\nabla_\perp}{a},\quad \nabla_\parallel\to\frac{c}{a}\nabla_\parallel,\quad t\to\frac{a}{c}\,t,\quad \eta_m\to a\,c\,\eta_m .$$
   $v_A$ is unchanged, so $\boldsymbol Z^\pm_\perp$ and $\nabla_\parallel$ are
   formally infinitesimal next to $v_A$ and $\nabla_\perp$: parallel and
   perpendicular distances are measured "in different units". Two corollaries
   are drawn (§3, §5.2, §6.3, crediting Beresnyak 2011, 2012a):
   the parallel-to-perpendicular aspect ratio of an RMHD simulation box is an
   arbitrary parameter, and any scaling law containing $v_A$ and a parallel
   length must contain them only through the combination $l_\parallel/v_A$.
   This symmetry is the argument that rules out the original form of
   [dynamic alignment](/properties/dynamic-alignment.md).
5. **Exact third-order law.** For longitudinal increments $\delta Z_L$ and
   perpendicular increments $\delta\boldsymbol Z^\pm_\lambda$ at separation
   $\lambda$,
   $$\langle\delta Z^\mp_L\,|\delta\boldsymbol Z^\pm_\lambda|^2\rangle=-2\varepsilon^\pm\lambda$$
   (Eq. 3.7); the review (§3) cites it as derived for isotropic MHD by
   Politano & Pouquet (1998) and adapted to RMHD by Boldyrev et al. (2009); the derivation is
   sketched in the review's footnote 9.

## Alignment and residual-energy diagnostics

Schekochihin (2022, App. B) defines the quantities used to describe Elsasser
fields statistically (page-local symbols): the Elsasser ratio
$R_E=|\delta\boldsymbol Z^+|^2/|\delta\boldsymbol Z^-|^2$, the Alfvén ratio
$R_A=|\delta\boldsymbol u|^2/|\delta\boldsymbol b|^2$, the normalized
cross-helicity $\sigma_c=(R_E-1)/(R_E+1)$ and the normalized residual energy
$\sigma_r=(R_A-1)/(R_A+1)$ (Eqs. B2, B4). With $\theta$ the angle between
$\delta\boldsymbol Z^+$ and $\delta\boldsymbol Z^-$ and $\theta_{ub}$ the
angle between $\delta\boldsymbol u$ and $\delta\boldsymbol b$,

$$\cos\theta=\frac{\sigma_r}{\sqrt{1-\sigma_c^2}},\qquad \cos\theta_{ub}=\frac{\sigma_c}{\sqrt{1-\sigma_r^2}}$$

(Eq. B5; App. B cites Wicks et al. 2013 for it). The **residual energy**
$\langle\boldsymbol Z^+\cdot\boldsymbol Z^-\rangle=\langle|\boldsymbol u_\perp|^2\rangle-\langle|\boldsymbol b_\perp|^2\rangle$
(Eq. 10.4) is therefore non-zero whenever the Elsasser increments are
aligned; the review prefers the Elsasser angle $\theta$ over $\theta_{ub}$
because it is the one that reduces the nonlinearity under imbalance (App. B,
Eq. B10). The scale-dependent version is $\theta_\lambda$ of the registry.

## Outside the reduced limit

Four sources work with systems that RMHD does not describe.

- **Compressive modes in full MHD.** [Gan et al.
  (2022)](/sources/gan-2022.md) drive isothermal compressible MHD with a
  strong guide field ($v_A=8$, plasma beta $\beta_p=0.4$, turbulent Mach
  number 0.12–0.18) and separate the fluctuation power into Alfvén, slow and
  fast modes. Even there, outside the injection range, most of the power lies
  on none of the linear dispersion branches (73–79% by the
  spatio-temporal filter); among the wave-like part the Alfvén
  mode dominates, with fast modes negligible under incompressible driving
  and about 2% under compressible driving (§3); details on [compressible MHD
  turbulence](/results/compressible-mhd-turbulence.md). They solve the
  full compressible equations, so the decoupling of property 1 above is not
  assumed there.
- **Elsasser fields in an inhomogeneous, high-beta wind.** [Adhikari et
  al. (2023)](/sources/adhikari-2023.md) (§2, Eqs. 4–7) use Elsasser
  variables $\boldsymbol Z^\pm=\boldsymbol u\pm\boldsymbol B/\sqrt{\mu_0\rho(\boldsymbol x)}$
  (SI units, a position-dependent background density, $\boldsymbol Z^+$
  directed outward from the Sun) at the leading order of nearly
  incompressible MHD for plasma beta $\beta_p\gg1$. That leading order is
  fully three-dimensional incompressible MHD holding both two-dimensional
  structures and slab Alfvén waves at the same order, with the Alfvén
  velocity present, and its velocity is not solenoidal in the stratified
  background, so the Elsasser equation gains density-gradient and
  background-shear terms. Adhikari et al. (§1–§2), citing Zank et al. (2017), state that for $\beta_p\ll1$ or
  $\beta_p\sim1$ the leading order is instead two-dimensional and the slab
  part a higher-order correction. Their Elsasser energies carry no factor
  $\tfrac12$, and the residual energy is
  $\langle\boldsymbol Z^+\cdot\boldsymbol Z^-\rangle$. The resulting
  turbulence transport model is on [compressible MHD
  turbulence](/results/compressible-mhd-turbulence.md).
- **A different reduced plasma model.** [Coelho et al.
  (2022)](/sources/coelho-2022.md) simulate stellarator edge turbulence with
  the drift-reduced Braginskii two-fluid equations (electrostatic, with
  density, electron and ion temperatures, parallel velocities, vorticity and
  potential), not with RMHD; they apply what they call the Boussinesq
  approximation (p. 3, Eqs. 1–7, not defined further), a plasma-fluid
  approximation unrelated to the eddy-viscosity hypothesis.
- **An Alfvén-like analogue.** On a ferrofluid surface in a horizontal field
  the magnetic surface wave is dispersionless along the field with an
  "Alfvén-like" speed, and its weak turbulence reproduces the spectrum of
  anisotropic shear-Alfvén wave turbulence without any Elsasser formalism
  ([Kochurin et al. 2022](/sources/kochurin-2022.md), Eqs. 1, 3, 6; see
  [weak wave turbulence](/results/weak-wave-turbulence.md)).

The exact third-order law of property 5 has compressible and Hall-MHD
counterparts, tested on DNS by [Ferrand et al.
(2022)](/sources/ferrand-2022.md); see [exact laws](/results/turbulence-exact-laws.md).

## Qualifications

- RMHD is incompressible in the perpendicular plane and assumes
  $\delta B/B_0\ll1$; the review states no turbulence closure in the CFD sense
  (no Reynolds averaging, no LES filter): $\langle\cdot\rangle$ is a volume or
  ensemble average and $\delta\boldsymbol Z_\lambda$ is a two-point increment.
- The registry writes $\boldsymbol b=\delta\boldsymbol B/\sqrt{4\pi\rho}$ and
  $\eta_m$ for the magnetic diffusivity; the source writes $\eta$ for it, and
  for the common value of $\nu$ and $\eta_m$ before §6.4.

# Citations

- [Schekochihin (2022)](/sources/schekochihin-2022.md) — §3, Eqs. (3.1)–(3.7); App. A.1, Eqs. (A1)–(A5); App. B, Eqs. (B1)–(B10); App. D, Eqs. (D1)–(D3); §10.4, Eq. (10.4); §13.3.3.
- [Gan et al. (2022)](/sources/gan-2022.md) — §2.1; §3 (mode fractions with a strong guide field).
- [Coelho et al. (2022)](/sources/coelho-2022.md) — p. 3, Eqs. (1)–(7) (drift-reduced Braginskii model, plasma Boussinesq approximation).
- [Kochurin et al. (2022)](/sources/kochurin-2022.md) — Eqs. (1), (3), (6).
- [Ferrand et al. (2022)](/sources/ferrand-2022.md) — §2 (compressible Hall-MHD exact laws).
- [Adhikari et al. (2023)](/sources/adhikari-2023.md) — §1; §2, Eqs. (4)–(9) (Elsasser fields at the leading order of high-beta nearly incompressible MHD; contrast with the reduced limit).

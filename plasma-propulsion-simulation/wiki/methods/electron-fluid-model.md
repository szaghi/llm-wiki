---
type: Method
title: "Electron fluid models (drift-diffusion)"
description: "Moment models of the electrons in thruster discharges, reduced in the slow-dynamics limit to a quasi-neutral drift-diffusion model with a generalized Ohm's law, a Fourier heat-flux law and empirical anomalous terms; the closure that hybrid and fully fluid Hall-thruster codes share, and whose heat-flux and transport terms kinetic comparisons show to be inadequate."
status: established
aliases: [drift-diffusion electron model, drift-diffusive electrons, slow-dynamics electron fluid model, generalized Ohm's law, fluid electrons, 8-moment electron model]
tags: [fluid, hybrid, hall-thruster, anomalous-transport, numerics]
timestamp: 2026-10-15T00:00:00Z
---

# Electron fluid models (drift-diffusion)

Fluid models describe the electrons by velocity moments of their kinetic
equation instead of by particles. In thruster codes they serve two roles: as
the electron half of [hybrid PIC–fluid models](/methods/hybrid-pic-fluid-model.md),
with particle ions and neutrals, and as one species of fully fluid models such as the
[one-dimensional fluid Hall model](/methods/one-dimensional-fluid-hall-model.md).
The form used almost everywhere is the inertialess, quasi-neutral
*drift-diffusion* model below
([Ahedo (2023)](/sources/ahedo-2023.md), §3;
[Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.1).

## Moment hierarchy

* The general moment equations are continuity, momentum with inertia and
  total energy. With an isotropic pressure tensor and a negligible heat flux
  they form the closed isotropic adiabatic *5-moment* model; adding a Fourier
  law for $\mathbf q_e(n_e,T_e)$ gives the *8-moment* isotropic model, "the
  main one being used in the literature to describe electrons in HET and EPT
  discharges" ([Ahedo (2023)](/sources/ahedo-2023.md), eqs. 1–3).
* The Chew–Goldberger–Low model splits the pressure tensor into parallel and
  perpendicular parts and adds a parallel-energy equation; Grad 13-, Levermore
  14- and Ramos 20-moment models are called "currently too ambitious" for
  these discharges ([Ahedo (2023)](/sources/ahedo-2023.md), eq. 4).
* Terminology differs between sources: the 2D model that
  [Troyetsky et al. (2026)](/sources/troyetsky-2026.md) call *five-moment*
  carries a Fourier heat flux, which Ahedo's count would make 8-moment. See
  [five-moment electron fluid model](/methods/five-moment-fluid-model.md).

## Drift-diffusion limit

When the electron drift is small against the electron thermal speed and the
distribution is near-Maxwellian, electron inertia drops out and the momentum
equation becomes a force balance
([Ahedo (2023)](/sources/ahedo-2023.md), eqs. 5–9):
$$\mathbf 0=-en_e\mathbf E+\mathbf j_e\times\mathbf B-\nabla p_e+(\text{collisional force})+(\text{anomalous force}),$$
with $\mathbf j_e=-en_e\mathbf u_e$. The anomalous terms are secular averages
of high-frequency dynamics; their consistent determination is "the main
weakness of slow-dynamics fluid models". A five-moment model with inertia
returns to drift-diffusion at steady state when the inertial term is dropped
([Troyetsky et al. (2026)](/sources/troyetsky-2026.md), p. 4).

**Generalized Ohm's law.** With the collisional force written through
$\nu_e$ and the drag current of the heavy species dropped, the electron
current in a frame aligned with $\mathbf B$ is
([Ahedo (2023)](/sources/ahedo-2023.md), eqs. 13–16, 27–29)
$$j_{e,\parallel}=\mu_\parallel\left(\nabla_\parallel p_e-en_e\nabla_\parallel\phi\right),\qquad j_{e,\perp}=\mu_\perp\left(\nabla_\perp p_e-en_e\nabla_\perp\phi\right),\qquad j_{e,\theta}=\Omega_e\,j_{e,\perp},$$
where $\perp$ is the direction normal to $\mathbf B$ in the meridian plane,
$\theta$ the azimuthal ($\mathbf E\times\mathbf B$) direction,
$\mu_\parallel=e/(m_e\nu_e)$, $\mu_\perp=\mu_\parallel/(1+\Omega_e^2)$ and
$\Omega_e=\omega_{ce}/\nu_e$ (see
[electron mobility and the Hall parameter](/definitions/electron-mobility-and-hall-parameter.md)).
[Taccogna & Garrigues (2019)](/sources/taccogna-2019.md) (§2.1, eqs. 11–13,
after Hagelaar et al. 2011) write the same law for the electron particle flux,
with a mobility tensor holding $\mu_\parallel$, $\mu_\perp$ and an
$\mathbf E\times\mathbf B$ term $\pm\mu_\parallel\Omega_e/(1+\Omega_e^2)$. The
1D axial models of [Giannetti et al. (2021)](/sources/giannetti-2021.md)
(eqs. 12–13) and [Saravia et al. (2026)](/sources/saravia-2026.md) (eqs. 4–5)
keep only the axial component with the cross-field mobility $\mu_\perp$.

**Anomalous transport.** The empirical turbulence model of Ahedo's group adds
an anomalous force proportional to the electron current, which replaces
$\nu_e$ by $\nu_e+\nu_{\mathrm{ano}}$ with
$\nu_{\mathrm{ano}}=\alpha_{\mathrm B}\,\omega_{ce}/16$ (the paper's
coefficient is $\alpha_{\mathrm B}/16$). Ahedo states that "there is no
evidence supporting" its isotropy and proposes an alternative that acts on the
azimuthal equations only and adds no anomalous parallel transport
([Ahedo (2023)](/sources/ahedo-2023.md), eqs. 18–21, 26). The coefficient
profiles in use are collected on
[anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md).

**Electron energy and heat flux.** The energy equation is closed by a Fourier
law with the same tensor structure as Ohm's law: along $\mathbf B$ the
conductivity is set by $\mu_\parallel$, across it by $\mu_\perp$
([Ahedo (2023)](/sources/ahedo-2023.md), eqs. 7–9, 17, 30–32). In this
form the parallel heat flux is
$$q_{e,\parallel}=-\frac{5}{2}\,\frac{\mu_\parallel}{e}\,p_e\nabla_\parallel T_e .$$
The same coefficient $5/2$ appears in the axial energy equation of
[Giannetti et al. (2021)](/sources/giannetti-2021.md) (eq. 16) and, written
with the mean energy $\tfrac32T_e$, in the closure of
[Taccogna & Garrigues (2019)](/sources/taccogna-2019.md) (eq. 15, after
Bittencourt 2004). [Troyetsky et al. (2026)](/sources/troyetsky-2026.md)
(eqs. 10–13) use instead the Mitchner–Kruger conductivity, whose parallel
value is $2.4/(1+\nu_{ei}/(\sqrt2\nu_e))$ times $n_eT_e/(m_e\nu_e)$, with
$\nu_{ei}=0$, and the perpendicular value divided by $1+\Omega_e^2$. This is a
different choice of closure coefficient, not a disagreement about a measured
quantity. Taccogna & Garrigues (§2.1) report that Boeuf & Garrigues (1998)
solved the energy equation stationary without the thermal flux, that Barral et
al. (2003) used separate parallel and perpendicular energy equations, and that
only 2D models solve the complete form.

## Quasi-neutral potential solve

Under quasi-neutrality the electron continuity equation is replaced by current
conservation, $\nabla\cdot\mathbf j_e=-\nabla\cdot\mathbf j_i$ plus sources,
and Ohm's law then gives an elliptic equation for $\phi$
([Ahedo (2023)](/sources/ahedo-2023.md), eqs. 11–12;
[Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), eqs. 17–19).

* **Anisotropy.** For $\Omega_e\gg1$ the mobility tensor is ill-conditioned,
  "the key difficulty" for accurate numerics; parallel and perpendicular
  derivatives differ by a factor of order $\Omega_e$ times its anomalous
  counterpart, "say $O(10^5)$ in conventional HETs"
  ([Ahedo (2023)](/sources/ahedo-2023.md), eqs. 16, 33). In $r$–$z$
  components the flux is a sum of large terms of opposite sign, and numerical
  error can dominate cross-field transport
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), eqs. 20a,b, after
  Hagelaar 2016). The remedies are the
  [magnetic-field-aligned mesh](/methods/magnetic-field-aligned-mesh.md) and the
  [thermalized potential](/definitions/thermalized-potential.md).
* **One dimension.** In 1D axial models the current density is uniform in $z$
  and follows from an integral of Ohm's law over the domain, with $\phi$
  recovered afterwards ([Giannetti et al. (2021)](/sources/giannetti-2021.md),
  eq. 19; [Saravia et al. (2026)](/sources/saravia-2026.md), eq. 13). See
  [one-dimensional fluid Hall model](/methods/one-dimensional-fluid-hall-model.md).
* **Non-neutral fluid models** solve Poisson's equation instead and keep
  electron inertia ([Troyetsky et al. (2026)](/sources/troyetsky-2026.md),
  eq. 40).

## Cost

* Replacing electron particles by a fluid removes the PIC time-step ordering
  $\Delta t_n\sim10^2\Delta t_i\sim10^4\Delta t_e$, allows electron steps of
  the order of the ion step and larger cells, and cuts cost by "about two
  orders of magnitude … say from 3 months to 1 day"
  ([Ahedo (2023)](/sources/ahedo-2023.md), Introduction).
* A 1D axial electron model takes minutes where the 2D $(z,r)$ one takes tens
  of hours ([Ahedo (2023)](/sources/ahedo-2023.md), p. 14). One evaluation of
  a 1D multi-fluid model takes O(1 min)
  ([Eckels et al. (2024)](/sources/eckels-2024.md), p. 9); a serial 1D fluid
  code needs about 1310 s per ms of plasma time
  ([Giannetti et al. (2021)](/sources/giannetti-2021.md), §2.4).
* Boyd (2005, §3.4) reports that the 2D steady multi-fluid models of Keidar
  et al. run in minutes against many hours for unsteady hybrid fluid–particle
  codes ([Boyd (2005)](/sources/boyd-2005.md)).

## Limits shown against kinetic models and experiment

* **Heat flux and pressure.** A 1D radial PIC solution shows a radially
  depleted electron distribution, a gyroviscous pressure term that can exceed
  azimuthal inertia, and a radial heat flux proportional to the enthalpy flux
  rather than to $\nabla T_e$: convective, not diffusive
  ([Ahedo (2023)](/sources/ahedo-2023.md), eqs. 44–46, Fig. 4).
  In a 2D axial–radial comparison with PIC-MCC on the same set-up, the
  fluid model gives isothermal field lines and a peak $T_e$ about 2.7 times
  lower, while PIC-MCC is strongly non-isothermal; the authors conclude that a
  Fourier-law heat flux is insufficient
  ([Troyetsky et al. (2026)](/sources/troyetsky-2026.md), pp. 18–19, 26–29).
  The convective closure leads to the
  [polytropic electron closure](/definitions/polytropic-electron-closure.md).
* **Anomalous terms.** Fluid models need ad-hoc parameters
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §4). A 1D fluid
  model calibrated across operating points keeps errors far above the
  experimental noise with negligible parametric uncertainty, which its authors
  attribute to model-form error
  ([Eckels et al. (2024)](/sources/eckels-2024.md), Discussion); see
  [Bayesian calibration](/methods/bayesian-calibration.md).
* **Accuracy (2005).** Fluid and hybrid schemes predicted Hall-thruster thrust
  and power only within about 10 %, limited by the electron mobility
  ([Boyd (2005)](/sources/boyd-2005.md), §3.4).

Wall terms (sheath losses, secondary emission, wall collisionality) enter the
electron equations as sources: see
[secondary electron emission](/definitions/secondary-electron-emission.md) and
[near-wall conductivity](/definitions/near-wall-conductivity.md).

# Citations

1. [Ahedo (2023)](/sources/ahedo-2023.md), Introduction, §3, eqs. 1–36, 44–46, Fig. 4, p. 14.
2. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §§2.1–2.2, 4, eqs. 11–20.
3. [Troyetsky et al. (2026)](/sources/troyetsky-2026.md), eqs. 3–13, 40, pp. 4, 18–19, 26–29.
4. [Giannetti et al. (2021)](/sources/giannetti-2021.md), §2.4, eqs. 12–16, 19.
5. [Saravia et al. (2026)](/sources/saravia-2026.md), §2, eqs. 4–5, 13.
6. [Eckels et al. (2024)](/sources/eckels-2024.md), p. 9, Discussion.
7. [Boyd (2005)](/sources/boyd-2005.md), §3.4.

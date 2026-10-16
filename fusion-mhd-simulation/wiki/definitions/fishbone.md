---
type: Definition
title: "Fishbone instability"
description: "Energetic-particle-modified n = 1 internal kink that acquires a finite real frequency through resonance with trapped energetic particles; benchmarked linearly in this bundle by M3D-C1-K against M3D-K and NIMROD."
status: established
aliases: [fishbone, fishbone mode, energetic-particle-driven internal kink]
tags: [energetic-particles, hybrid-kinetic, kink, tokamak]
timestamp: 2026-10-16T00:00:00Z
---

# Fishbone instability

The fishbone is the $n=1$ internal kink modified by energetic particles
(EPs). Without EPs the $m/n=1/1$ mode is an ideal or
[resistive internal kink](/definitions/resistive-internal-kink.md) with zero
real frequency. As the EP share of the pressure grows, the mode changes
character. It acquires a finite real frequency $\omega$, and its growth is
driven by resonance with trapped EPs
([Liu et al. (2022)](/sources/liu-2022.md), §6.1).

## The linear transition from kink to fishbone

The M3D-C1-K benchmark follows the setup of Fu et al. (2006) for M3D-K, also
used by Kim et al. (2008) for NIMROD
([Liu et al. (2022)](/sources/liu-2022.md), §6.1):

- **Geometry and plasma.** Circular tokamak with $R_0=1$ m,
  $a=0.361925$ m, $B=1$ T and hydrogen at uniform
  $n_i=2.489\times10^{20}$ m$^{-3}$. The pressure is
  $p=p_0\exp(-\psi_N/0.25)$ with $p_0=16335$ Pa, which gives a central
  $\beta=8\%$.
- **Safety factor.** $q_0=0.6$, so the $q=1$ surface lies inside the plasma.
- **EPs.** The EP density has the same shape as $p$. The distribution is an
  isotropic slowing-down $f_0\propto H(v_0-v)/(v^3+v_c^3)$ with
  $v_0=3.9\times10^6$ m/s and $v_c=0.58v_0$. The EP mass is reduced to
  $0.11m_{\mathrm H}$ to match $\rho_L/a=0.0125$.
- **Physics options.** No FLR. Markers are loaded on the local $\psi$, not
  the orbit-averaged $\psi$ of Fu et al.

The scan holds the total pressure fixed and raises the EP share
$\beta_h/\beta$ from 0 to 0.75 (Fig. 3):

- the mode changes from an ideal kink at $\beta_h/\beta=0$ to a fishbone
  with finite real frequency;
- $\gamma\tau_A$ falls from about 0.025 to a minimum of about 0.021 near
  $\beta_h/\beta=0.25$, then rises to about 0.028 at 0.75;
- $\omega\tau_A$ rises roughly linearly with $\beta_h/\beta$, to about 0.030
  at 0.75 (values read off the plot; $\tau_A$ is not defined in the paper).

The non-adiabatic EP response $\delta p_{\perp h}-\delta p_{\parallel h}$ is
localized on the low-field side. The paper reads this as evidence of
trapped-particle resonance, and the mode structure is "consistent with" the
NIMROD result (§6.1, Fig. 4). Pressure coupling and current coupling give
nearly identical $\gamma$ and $\omega$ (Fig. 3; see
[pressure and current coupling](/methods/pressure-and-current-coupling.md)).

## Nonlinear studies

JOREK's full-$f$ EP model, coupled through anisotropic pressure, has so far
been verified only linearly. Nonlinear applications "to fishbone
instabilities and other phenomena" are listed as in progress
([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §4.2). Liu et al. name
long-time nonlinear EP physics as the intended use of M3D-C1-K, including
"kink/tearing with EPs" ([Liu et al. (2022)](/sources/liu-2022.md), §7).

## Code-to-code spread

M3D-C1-K's growth rates agree with M3D-K and NIMROD over the whole scan.
Its real frequency does not at large $\beta_h/\beta$. The paper states the
exception ("except for the mode real frequency at large
$\beta_h/\beta_{total}$"). Read off Fig. 3b, M3D-C1-K's $\omega\tau_A$ is
15–20% below the other two codes at $\beta_h/\beta=0.5$–0.75: about 0.022
against 0.026–0.028 at 0.5, and about 0.030 against 0.035–0.036 at 0.75
([Liu et al. (2022)](/sources/liu-2022.md), §6.1). The paper does not
attribute the gap. The one setup difference it records is the local-$\psi$
loading of markers in place of Fu et al.'s orbit-averaged $\psi$. Repeating
the scan with orbit-averaged loading would test that candidate.

# Citations

- [Liu et al. (2022)](/sources/liu-2022.md): the linear kink-to-fishbone benchmark against M3D-K and NIMROD.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md): nonlinear JOREK fishbone studies in progress.

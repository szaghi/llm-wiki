---
type: Definition
title: "Plasmoid drift of ablation clouds"
description: "Plasmoid drift is the major-radius-outward E×B motion of a dense, over-pressured pellet-ablation cloud, polarized vertically by the ∇B drift current and braked by shear Alfvén waves and parallel return currents; in MHD simulations of shattered pellet injection it helps assimilation in some cases and expels material and heats the wall in others, and artificially elongated toroidal sources under-predict it."
status: established
aliases: [plasmoid drift, ablation cloud drift, pellet cloud drift, E×B drift of plasmoids, LFS drift]
tags: [disruption, impurities, neutrals, mhd, tokamak]
timestamp: 2026-10-16T12:00:00Z
---

# Plasmoid drift of ablation clouds

A **plasmoid** is the dense, ionized cloud that forms around an ablating
pellet or pellet fragment. Its pressure exceeds the background pressure by
a large factor, so the $\nabla B$ (and curvature) drift current inside it is
not closed locally; charge separates vertically, the resulting vertical
electric field drives an $\mathbf E\times\mathbf B$ motion of the whole cloud
toward larger $R$, the low-field side (LFS)
([Kong et al. (2025)](/sources/kong-2025.md), §1, Fig. 1;
[Hu et al. (2024)](/sources/hu-2024.md), §3). The drift moves injected
material away from where the fragments ablate, so it bears on the
assimilation of [shattered pellet injection](/definitions/shattered-pellet-injection.md)
and on the heat loads of the mitigated [thermal quench](/definitions/thermal-quench.md).

## Theory used by the sources

Page-local symbols: $v_{\mathrm D}$ is the major-radius component of the
cloud's $\mathbf E\times\mathbf B$ velocity at its centre; $n_{\mathrm c}$,
$p_{\mathrm c}$ the cloud density and total pressure, $p_\infty$ the
background pressure; $\ell_0$ the half-length of the cloud along the field;
$L_{\mathrm{con}}$ the connection length between neighbouring passages of the
cloud's flux tube; $v_A$ is evaluated with the **background** density.

The acceleration of the cloud is the $\nabla B$ drive minus the braking by
shear Alfvén waves launched from both ends of the cloud, which carry the
polarization charge away along the field:

$$\frac{dv_{\mathrm D}}{dt}=\frac{2(p_{\mathrm c}-p_\infty)}{n_{\mathrm c}m_iR}-v_{\mathrm D}\,\frac{2B_\phi^2}{\mu_0v_An_{\mathrm c}m_i\ell_0},$$

and for $p_{\mathrm c}\gg p_\infty$ the velocity saturates at

$$v_{\mathrm D,\lim}\approx\frac{\mu_0v_Ap_{\mathrm c}\ell_0}{RB_\phi^2},\qquad p_{\mathrm c}=2n_eT_e\ \text{(equal temperatures)}$$

([Kong et al. (2025)](/sources/kong-2025.md), §1, Eqs. 1–3, attributing
the theory to Parks 2000, Rozhansky 2004 and Pégourié 2007). Three braking
stages follow each other: a polarization current on the shortest times;
**shear-Alfvén-wave (SAW) braking**, which sets $v_{\mathrm D,\lim}$; and,
once the wave packets have travelled $L_{\mathrm{con}}$ and reached the
cloud's other passages, **Pégourié braking** by purely parallel resistive
return currents, which sets in earlier for larger toroidal extent (§1, §3).

In the JOREK reduced-MHD vorticity equation the drive is the term
$[p,R^2]$, with the bracket $[f,g]=R\,(\nabla f\times\nabla g)\cdot\nabla\phi$:
a local pressure peak polarizes the cloud through it
([Hu et al. (2024)](/sources/hu-2024.md), §3, Eq. 5, reading the mechanism
of Rozhansky et al. into that term).

## Mechanism study: JET H-mode, transient deuterium source

[Kong et al. (2025)](/sources/kong-2025.md) place a 0.05 µs Gaussian
deuterium neutral source at the LFS midplane of a JET H-mode (#96874) in
JOREK reduced MHD with a [fluid neutral model](/methods/fluid-neutral-models.md)
and $n\le10$, and compare the drift with the theory "for the first time"
(§1):

- **SAW braking at moderate amplitude.** For $2\times10^{26}$ to
  $1.4\times10^{27}$ atoms/s, $v_{\mathrm D}$ saturates within a few µs and
  scales linearly with the source amplitude, as $v_{\mathrm D,\lim}$
  predicts: 2.7, 15 and 20 km/s (§3.1, Fig. 3).
- **Departure at large amplitude.** At $10^{28}$ atoms/s the drift saturates
  at ≈65 km/s, about half the linear extrapolation (≈130 km/s); the authors
  propose stronger Pégourié braking aided by stochastization of the outer
  region as a "possible explanation" (§3.1, Fig. 12).
- **Toroidal extent.** Raising the toroidal source half-width from 0.5 to
  2 rad brings the fast drop of $v_{\mathrm D}$ forward, i.e. earlier
  Pégourié braking through a shorter $L_{\mathrm{con}}$, as the theory
  predicts (§3.2, Fig. 5).
- **Magnitude.** The saturation formula with the central cloud pressure
  overestimates the JOREK velocity by a factor 2.8–3.8 (75 against 20,
  42.5 against 15, 8.4 against 2.7 km/s; the source says "3–4") (§3.3,
  Table 1). The $\mathbf E\times\mathbf B$ flow region is near-circular in the
  poloidal plane, because the dipole electric field has a pole separation set
  by the toroidal size of the source, and it is larger than the poloidally
  elongated cloud; more field lines are bent, so SAW braking is stronger.
  The field-line-integrated pressure averaged over ≈1600 field lines of that
  region is 3.6 times below the central value and closes the gap (§3.4,
  Figs. 7–9).
- **Toroidal field.** $v_{\mathrm D}$ grows with $F_0$ over 0.5–3 times the
  nominal value, against the $B_\phi^{-2}$ of the formula; the authors
  attribute it to the shrinking flow region (§3.4, Figs. 10–11).
- **Shear Alfvén waves are resolved.** The flow-potential perturbation
  propagates along the field at ≈$4.7\times10^6$ m/s against
  $v_A\approx4.5\times10^6$ m/s, and the wave energy $\int|\delta\mathbf B_\perp|^2dV$
  peaks at ≈5.5 µs (§4, Figs. 13–16).

Their practical conclusion: the toroidally elongated sources that 3D MHD
codes use for resolution reasons strengthen all three braking effects and
under-predict the drift, which makes it "difficult to reach drift levels
inferred from experiments" (§3.2, §5).

## Drift in ITER H-mode dual SPI

[Hu et al. (2024)](/sources/hu-2024.md) find the drift in JOREK runs of
neon-doped dual SPI into ITER H-modes (two temperatures,
[collisional-radiative impurities](/methods/collisional-radiative-impurity-model.md),
$n=0$–11):

- In the 370 MJ baseline H-mode with 1% neon pellets, vanguard fragments
  reaching the pedestal create a strong local over-pressure; the plasmoid
  drifts outward along $R$, expels injected material beyond the last closed
  flux surface, stochastizes the edge and collapses the pedestal by 0.46 ms
  (§3, Figs. 3–5).
- More than 100 MJ of thermal energy are lost "before the fragments
  penetrate deep into the core"; the radiated fraction is 49.4% and only
  ≈20% of the neon is assimilated (compiler's arithmetic from Table 2)
  (§3, Fig. 7). Conductive and convective wall heat fluxes peak at about
  $3\times10^{11}$ W/m² (read from Fig. 6), dominated by the perpendicular
  part.
- A higher neon fraction (5% "quarter pellets") lowers the over-pressure
  by local radiation, and a degraded 190 MJ H-mode lowers the thermal
  reservoir; both suppress the drift and raise the radiated fraction to
  86–90% (§3, Table 2; the radiative suppression is attributed to Matsuyama
  et al. 2022). With full pellets the degraded H-mode still drifts, including
  a second drift driven by heat leaving the X-point of the 1/1 island during
  core relaxation (§3, Figs. 8–9).

[Hu et al. (2023)](/sources/hu-2023.md) (§5) anticipated that at low neon
fraction plasmoid drift can reduce assimilation in ITER H-mode.

## Qualifications

**Helpful or harmful.** The JOREK review states that "plasmoid drifts are
essential for assimilation" in JET deuterium and mixed SPI simulations
([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.2), while
[Hu et al. (2024)](/sources/hu-2024.md) find that in an ITER baseline
H-mode with LFS injection of 1%-neon pellets the drift expels material,
cuts the assimilated neon to ≈20% and loses over 100 MJ before the TQ.
The statements are compatible: they concern different machines (JET
against ITER), pellet compositions (deuterium or mixed against 1% neon),
and targets (a JET plasma against a 370 MJ pedestal). The review gives no
mechanism for "essential", and Hu et al. do not cite it; which conditions
turn the drift from beneficial to harmful has not been isolated by a
single scan in the sources.

**Resolution.** All drift results of this page use toroidally elongated
sources (0.3 rad in Hu et al. 2024; 0.5–2 rad in Kong et al. 2025); by Kong
et al.'s analysis the simulated drift is a lower bound. Hu et al. (2024,
§5) state that the effect of the elongation on their drift is undetermined.

## Citations

- [Kong et al. (2025)](/sources/kong-2025.md), §1–5, Eqs. 1–3, Table 1, Figs. 1–16.
- [Hu et al. (2024)](/sources/hu-2024.md), §3, §5, Eq. 5, Table 2, Figs. 3–9.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.2.
- [Hu et al. (2023)](/sources/hu-2023.md), §5.

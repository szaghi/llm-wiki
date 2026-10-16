---
type: Result
title: "Edge instabilities of an optimized quasi-axisymmetric reactor stellarator"
description: "First nonlinear M3D-C1 simulations of a reactor-scale two-field-period quasi-axisymmetric stellarator optimized at β = 2.5 % without a stability target: edge pressure-driven high-n modes destroy the flux surfaces within about 1500 Alfvén times for every resistivity model, only even toroidal harmonics are destabilized, temperature gradients survive in the chaotic field, and Spitzer resistivity gives a secondary nonlinear growth acceleration; the authors conclude that MHD stability must enter stellarator optimization."
status: established
aliases: [QA reactor stellarator nonlinear MHD, Wright–Ferraro QA instability, optimized QA edge instability]
tags: [stellarator, full-mhd, equilibrium, bootstrap-current]
timestamp: 2026-10-16T23:45:00Z
---

# Edge instabilities of an optimized quasi-axisymmetric reactor stellarator

[Wright & Ferraro (2024)](/sources/wright-2024.md) run the first
nonlinear MHD simulations of a reactor-scale
[quasi-axisymmetric](/definitions/quasi-symmetry.md) (QA) stellarator: the
$N_{\rm fp}=2$ equilibrium of Landreman, Buller & Drevlak (2022, §VI C, as
cited), optimized with SIMSOPT for $\beta=2.5\,\%$, quasi-symmetry,
energetic-particle confinement and a self-consistent bootstrap current, but
not for MHD stability (§II). The result is a rapid loss of confinement
from the edge inward, which the authors take as evidence that MHD stability
must be an optimization target.

## Setup

* **Code and model.** [M3D-C1](/software/m3d-c1.md) in stellarator
  geometry, single-fluid
  [visco-resistive MHD](/methods/visco-resistive-mhd-model.md) with
  continuity, anisotropic heat conduction ($\kappa_\perp/\kappa_\parallel=10^{-6}$,
  $\chi_\perp=2.18$ m²/s), dynamic viscosity $\nu=3.65\times10^{-4}$
  kg m⁻¹ s⁻¹ (about 100 times experimental values), no hyper-diffusion, no
  source current and no two-fluid terms (§II, App. A).
* **Resistivity.** Four models, $\eta=\eta_{\rm u}[\eta_c+\eta_0T_e^{-3/2}]$
  with $\eta_{\rm u}=2.74\ \Omega$ m the M3D-C1 resistivity unit
  (page-local symbols): constant ($\eta_c=10^{-6}$, $\eta_0=0$, i.e.
  $2.74\times10^{-6}\ \Omega$ m) and Spitzer-like with $\eta_0=1,10,100$
  ($\eta_c=0$); the unit of $T_e$ in this formula is not stated (Eq. 2).
* **Geometry.** Limited plasma, the conducting wall on the initial plasma
  boundary, no vacuum region, $T$ and $J$ zero at the wall, density held at
  its initial wall value; full torus with no imposed symmetry, so harmonics
  of every toroidal [mode family](/definitions/toroidal-mode-family.md) are
  allowed; 72 toroidal planes, $8.64\times10^5$ 3D elements; minor radius
  $a=1.704$ m (§II).
* **Cost.** About $4\times10^5$ CPU-hours, 14 days wall clock per run;
  no GPU (§II).

## Findings

* **Alfvénic edge instability.** High-$(m,n)$ modes appear "almost
  immediately near the plasma edge"; many modes develop from about
  $200\tau_A$; a chaotic layer of 5–10 % of the minor radius forms within
  about $500\tau_A$, reaches "nearly 25 %" by about $800\tau_A$ and then
  spreads until "the core is enveloped by a sea of chaotic magnetic
  fields", at about $1500\tau_A$, printed as $\sim700\,\mu$s for constant
  $\eta$ (§III, Figs. 1, 2, 6). Two core modes, $m=5$ and $m=3$, grow much
  more slowly and stay small (§III; not shown).
* **Insensitivity to the resistivity model.** The evolution is
  "qualitatively identical, regardless of resistivity model", which the
  authors read as an ideally unstable plasma (§III–IV). No ideal linear
  stability calculation is reported.
* **Classification.** The abstract calls the modes "interchange-like
  pressure-driven", although an a posteriori analysis finds a magnetic
  well on all surfaces (§II); no Mercier or ballooning evaluation is shown.
  The tension is recorded on
  [interchange modes](/definitions/interchange-mode.md).
* **Even harmonics only.** The kinetic-energy growth rates
  $d\ln W_{\rm kin}^{(n)}/dt$ (twice $\gamma$ during exponential growth;
  the paper does not say so) of the even harmonics $6\le n\le30$ are all
  positive, largest for $20\le n\le28$, about
  $(0.1$–$1.1)\times10^{-2}\tau_A^{-1}$ at their maxima (§III, Figs. 3–4).
  The authors explain the even-only spectrum by $N_{\rm fp}=2$ coupling, a
  single unstable eigenmode composed of many even harmonics (§III–IV);
  that a single eigenmode is responsible is asserted, not shown.
* **Temperature gradients in chaotic field.** The pressure-relaxation time
  $a^2/\chi_\perp=1.33$ s exceeds the breakup time by more than three
  orders of magnitude, so $T_e$ gradients persist inside the chaotic
  region, consistent with Reiman (2021, as cited); the authors call the
  instability-driven breakup "mechanistically distinct" from equilibrium
  pressure-driven stochastization (§III, Fig. 1).
* **Secondary acceleration with Spitzer resistivity.** At $n=30$, with
  constant $\eta$ the growth rate rises, plateaus near $500\tau_A$ and
  decays toward saturation; with the three Spitzer models it shows no
  plateau but a slowing and then "a significant increase" before peaking,
  read as "strong nonlinear interactions, which are accelerating the
  growth"; an energy-transfer analysis is left to future work (§III,
  Fig. 5). The higher the Spitzer multiplier, the earlier the peak (figure
  reading on the Source page).

## Conclusions drawn by the authors

* "Field-periodicity plays an important role in nonlinear MHD stability,
  especially if there is a linearly unstable mode" (§IV).
* MHD stability is "at least as important a target for optimization" as
  the neoclassical targets for finite-β QA configurations, which motivates
  better stability metrics (§I, §IV).
* One should "proceed with caution when using linear approximations to
  predict nonlinear MHD behavior in stellarators" (§III).
* The result runs against the view, which the authors attribute to LHD
  experiments exceeding linear thresholds without confinement loss
  (Sakakibara et al. 2010, as cited), that stellarators are robust to
  MHD (§I); see the contrast on [soft β limit](/definitions/soft-beta-limit.md).

## Caveats recorded by the compiler

* The modes are called "internal in character" and "unaffected by the
  boundary conditions", although they arise at the edge and the wall sits
  on the plasma boundary; no boundary-condition variation is run (§III).
* The viscosity is stated not to affect the result because it damps the
  high-$(m,n)$ modes; no viscosity scan is shown. Convergence studies are
  stated, not shown (§II).
* $\tau_A$ is not defined in the paper; the printed $1500\tau_A\approx700\,\mu$s
  implies $\tau_A\approx0.46\,\mu$s, consistent with a 1 m length and the
  M3D-C1 reference field and density (inference on the Source page).

## Follow-up with the bootstrap current

[Saxena et al. (2025)](/sources/saxena-2025.md) (§3.3, Figs. 5–8) evolve
a QA case of the same family (bootstrap-consistent, $\langle\beta\rangle=2.5\,\%$,
$a=1.70$ m, the same $\eta$ unit and viscosity) with a
[bootstrap current](/definitions/bootstrap-current.md) closure, at lower
resolution (36 planes, $1.88\times10^5$ elements) and Spitzer multipliers
1, 10, $10^3$, $10^4$. The plasma stays MHD-unstable with and without the
bootstrap current; the bootstrap current sustains the toroidal current and
slows the breakup of the edge surfaces; and kinetic energy grows faster
with larger resistivity, a finding they present as "supporting Wright &
Ferraro (2024a)".

## Contradictions

* **Does growth increase with resistivity?** *Open.* Saxena et al. (2025)
  attribute to Wright & Ferraro (2024) a growth that increases with
  resistivity; Wright & Ferraro state that the behaviour is qualitatively
  unchanged across resistivity models, and their maximum growth rates are
  not monotonic in the multiplier. Recorded in full on
  [quasi-symmetry](/definitions/quasi-symmetry.md).

# Citations

* [Wright & Ferraro (2024)](/sources/wright-2024.md) — the simulations, findings and conclusions.
* [Saxena et al. (2025)](/sources/saxena-2025.md) — the bootstrap-current follow-up and its reading of the resistivity dependence.

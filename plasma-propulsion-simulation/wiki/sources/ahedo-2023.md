---
type: Source
title: "Ahedo (2023) — Using electron fluid models to analyze plasma thruster discharges"
description: "Review of slow-dynamics electron fluid models for Hall and electrodeless thrusters: the drift-diffusive quasi-neutral model with generalized Ohm's and Fourier laws and empirical anomalous terms, field-aligned meshes and the thermalized potential, an extended 1D axial model, kinetically consistent closures (anisotropic pressure, gyroviscosity, convective heat flux, polytropic laws), plume boundary conditions and a Debye-sheath/SEE wall model."
resource: "doi:10.1007/s44205-022-00035-6"
source_kind: paper
authors: [Ahedo E.]
year: 2023
venue: "J. Electr. Propuls. 2:2"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2023_Crossref_Journal_of_Electric_Propulsion_Ahedo_Using_electron_fluid_models_to_analyze_plasma_thruster_disch.pdf"
tags: [review, fluid, hybrid, hall-thruster, helicon, magnetic-nozzle, plume, anomalous-transport, sheath, wall-interaction, numerics, software]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

A review by the head of the UC3M EP2 group of the slow-dynamics electron fluid
models used in hybrid codes for Hall-effect thrusters and electrodeless
thrusters (helicon, ECR). It sets out the general 5- and 8-moment electron
equations, reduces them to the one-temperature, drift-diffusive,
quasi-neutral model with a generalized Ohm's law, a Fourier heat-flux law and
empirical anomalous terms, and discusses why the anisotropic mobility tensor
calls for magnetic-field-aligned meshes and a thermalized potential. It
presents an extended 1D axial Hall model with azimuthal electron inertia, an
internal volumetric cathode and the far plume. Two 1D kinetic solutions (a
radial PIC model of a Hall-thruster cross-section and a paraxial
magnetic-nozzle Vlasov model) are used to derive kinetically consistent
closures: anisotropic pressure, gyroviscosity and a convective parallel heat
flux. It closes with plume models (2D collisionless magnetic nozzle,
EP2PLUS), global current-free plume boundary conditions and an appendix on the
Debye-sheath and SEE wall model. Most figures come from the group's codes
(HYPHEN, EP2PLUS) and earlier group papers; no new simulation is documented in
reproducible detail.

# Key claims

1. **Moment models** (§3, eqs. 1–4). Isotropic pressure with negligible heat
   flux gives the closed 5-moment model; a Fourier law gives the 8-moment
   model, "the main one being used in the literature" for these discharges.
   Grad 13-, Levermore 14- and Ramos 20-moment models are "currently too
   ambitious".
2. **Drift-diffusive model** (eqs. 5–10). With negligible electron inertia
   and a near-Maxwellian distribution, momentum and heat-flux equations become
   algebraic. The anomalous (secular) terms are "the main weakness of
   slow-dynamics fluid models".
3. **Quasi-neutral form** (eqs. 11–17). Current conservation replaces
   continuity; Ohm's law and the Fourier law share a mobility tensor that is
   ill-conditioned for large Hall parameter, "the key difficulty" for accurate
   numerics.
4. **Turbulence models** (eqs. 18–21, 26). An isotropic Bohm-type force
   (anomalous collision frequency $\alpha_{\mathrm B}\omega_{ce}/16$ added to
   $\nu_e$) for which "there is no evidence supporting" the isotropy; an
   alternative acting on the azimuthal equations only. A "certain consensus"
   (refs. 31–34) holds that the coefficient is smaller in the channel than in
   the near plume, with a minimum near the peak axial field; electrodeless
   thrusters use a constant coefficient. No numerical coefficient values are
   given.
5. **Field-aligned meshes and the thermalized potential** (eqs. 33–36).
   Parallel and perpendicular derivatives differ by about $O(10^5)$; on a
   cylindrical mesh this produces numerical diffusion, avoided by an MFAM
   (HALL2De, HYPHEN), whose drawbacks are irregular cells, non-aligned
   boundaries and boundary derivative errors. The Morozov limit of infinite
   parallel mobility makes lines isothermal and equipotential in
   $\phi^*$ but leaves the parallel current undetermined by Ohm's law.
6. **1D axial model** (eqs. 37–43, Fig. 3). Azimuthal inertia matters near the
   anode, around the cathode and in the near plume, where it bounds the
   azimuthal electron velocity; $\phi$ and $T_e$ change little. The model runs
   in minutes against tens of hours for the 2D $(z,r)$ electron model.
7. **Kinetic closures** (eqs. 44–53, Figs. 4–5). The 1D radial PIC solution
   shows radial tail depletion, a gyroviscous term that can exceed azimuthal
   inertia, and a convective (not diffusive) radial heat flux; the replenishment
   factor is 0.05–0.20 for $\mathbf B$ normal to the wall. The paraxial nozzle
   model gives a convective far-plume parallel heat flux and a $B$-dependent
   polytropic law, fitted with $\gamma-1=0.23$.
8. **Plume models** (eqs. 54–63, Fig. 6). In a 2D collisionless nozzle with
   polytropic electrons the electron equations are algebraic; a global
   current-free boundary condition is "more robust" than the local zero-current
   condition, whose plume current loops depend on plume size (HYPHEN, shown).
9. **Parallel cooling** (eq. 64). An anomalous parallel collisionality of
   10–100 times the collisional one recovers the observed parallel cooling in
   an electrodeless thruster (ref. 41).
10. **EP2PLUS** (eqs. 68–72, Fig. 7). 3D hybrid with 4-moment polytropic
    electrons on a Cartesian mesh, reliable up to effective Hall parameters of
    50–100; ref. 29 showed the polytropic law inadequate in the near region of a
    Hall thruster; an 8-moment upgrade is described.
11. **Wall model** (Appendix, eqs. 73–78). Thin collisionless Debye sheaths
    with reflected and true-secondary electrons; the dielectric-wall drop
    (eq. 75), whose first logarithm argument is about 200 for xenon; the
    charge-saturation limit "is very unstable numerically"; the Hobbs–Wesson
    result holds only for a fully replenished semi-Maxwellian; a "certain
    consensus" that wave turbulence matters more than wall collisionality for
    anomalous transport; the normal–inverse anode-sheath transition.

# Models and numerics

Review; no model of its own is run in reproducible detail. The electron
equations are those of the drift-diffusive model (eqs. 6–17), in magnetic
coordinates for axisymmetric problems (eqs. 22–35). No discretization
formulas, mesh sizes, time steps, particle counts, collision sets or run times
are given, except: the PIC step ordering $\Delta t_n\sim10^2\Delta t_i\sim10^4\Delta t_e$;
fluid electrons allow electron steps of the order of the ion step and cut cost
by about two orders of magnitude ("from 3 months to 1 day"); the 1D axial
model takes minutes against tens of hours for 2D. The 1D radial PIC models
turbulence as isotropic collisions at $0.01\,\omega_{ce}$ (Fig. 4 caption).
Language, GPU and MPI are not stated.

# Tests and results

All illustrative, from the group's codes and earlier papers; none is a
quantitative comparison with experiment in this paper. Figure values are read
from plots.

* Fig. 1: HYPHEN, magnetically shielded Hall thruster (MFAM with a null point;
  maps of $n_e$, $T_e$, $\phi$, currents).
* Fig. 2: HYPHEN, ECR thruster (absorbed power $10^5$–$10^9$ W m$^{-3}$; $T_e$
  nearly constant along lines).
* Fig. 3: 1D axial fluid model with and without azimuthal inertia: anode-side
  $\phi\approx300$ V; plume $\phi$ about 65 V (inertialess) against 55 V
  (inertia); $T_e$ peak about 35 eV near the exit; plume axial electron
  velocity about 17–18 km/s, equal to the ion velocity.
* Fig. 4: 1D radial PIC of a Hall-thruster cross-section: depleted tail,
  sheath edges at 2 % non-neutrality coinciding with ion Mach about 1, mean
  axial electron current density about 560 A/m$^2$ with Larmor-scale
  undulations.
* Fig. 5: paraxial kinetic magnetic nozzle: $e\phi/T_e$ falls to about −3,
  polytropic fit $\gamma-1=0.23$, parallel heat flux over enthalpy flux about
  0.6 downstream.
* Fig. 6: HYPHEN plume boundary conditions, local against global.
* Fig. 7: EP2PLUS near plume of a gridded ion thruster, 3 × 5 holes.

# Notation map

| Ahedo (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $n_e$, $\boldsymbol u_e$, $T_e$, $p_e$, $\boldsymbol q_e$ | $n_e$, $\mathbf u_e$, $T_e$, $p_e$, $\mathbf q_e$ | $T_e$ in energy units |
| $\bar{\bar p}_e$ | $\mathsf P_e$ | |
| $p_{\parallel e}$, $p_{\perp e}$, $T_{\parallel e}$, $T_{\perp e}$ | words | not in the registry |
| $\boldsymbol j_e=-en_e\boldsymbol u_e$, $\boldsymbol j_i$ | $\mathbf j_e$, $\mathbf j_i$ | |
| $\boldsymbol j_c$ | words (heavy-species drag current) | **collision:** subscript $c$ also marks the cathode source $S_c$ |
| $\boldsymbol F_c$, $\boldsymbol F_a$, $Q_a$, $\boldsymbol Y_a$ | words | collisional and anomalous force, heating, heat-flux terms |
| $\nu_e$, $\nu_{es}$ | $\nu_e$, $\nu_{es}$ | |
| $\alpha_a$ | $\alpha_{\mathrm B}/16$ | the paper's $\nu_e^*=\nu_e+\alpha_a\omega_{ce}$, so $\alpha_{\mathrm B}=16\alpha_a$ |
| $\mu_e=e/(m_e\nu_e)$, $\bar{\bar\mu}_e$ | $\mu_\parallel$; words for the tensor | |
| $\chi=\omega_{ce}/\nu_e$, $\chi^*$ | $\Omega_e$; words (effective Hall parameter) | **collision:** the paper's $\chi$ is the Hall parameter |
| $\Phi$ | $\phi^*$ | thermalized potential |
| $\Phi_p$ | words | polytropic analogue |
| $\mathbf 1_\parallel$, $\mathbf 1_\top$, $\mathbf 1_\theta$ | $\parallel$, $\perp$, $\theta$ | $\top$ is in-meridian perpendicular |
| $\psi$ | words | magnetic stream function |
| $\gamma$ | $\gamma$ | polytropic index |
| $c_e=\sqrt{T_e/m_e}$ | words | **collision:** the registry's $c_s$ is the ion sound speed |
| $\delta_s$ | $\delta_{\mathrm{SEE}}$ | true-SEE yield |
| $\delta_r$, $\sigma_{rp}$, $\phi_{WQ}$ | words; $\Delta\phi_{\mathrm{sh}}$ | reflected fraction, replenishment factor, sheath fall |
| $\eta=\lvert I_i/I_e\rvert\sqrt{m_i/m_e}$ | words | **collision:** the registry's $\eta$ is thrust efficiency |
| $\rho_{el}$, $\epsilon_0$ | $\rho_c$, $\varepsilon_0$ | |
| $I_d$, $V_d$ | $I_d$, $V_d$ | |

# Pages created or updated

Chunk 1 (2026-10-14) created every page of the bundle. This source is cited on:

* [Anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md)
* [Boltzmann-relation electrons](/methods/boltzmann-electron-model.md)
* [Cross-field electron mobility and the Hall parameter](/definitions/electron-mobility-and-hall-parameter.md)
* [Electron fluid models (drift-diffusion)](/methods/electron-fluid-model.md)
* [Five-moment electron fluid model](/methods/five-moment-fluid-model.md)
* [Hall-effect thruster](/definitions/hall-effect-thruster.md)
* [Helicon plasma thruster](/definitions/helicon-plasma-thruster.md)
* [Hybrid PIC–fluid models](/methods/hybrid-pic-fluid-model.md)
* [HYPHEN](/software/hyphen.md)
* [Magnetic nozzle](/definitions/magnetic-nozzle.md)
* [Magnetic shielding](/definitions/magnetic-shielding.md)
* [Magnetic-field-aligned meshes](/methods/magnetic-field-aligned-mesh.md)
* [Near-wall conductivity](/definitions/near-wall-conductivity.md)
* [One-dimensional fluid model of the Hall-thruster discharge](/methods/one-dimensional-fluid-hall-model.md)
* [Polytropic electron closure and plume cooling](/definitions/polytropic-electron-closure.md)
* [Secondary electron emission and sheath regimes](/definitions/secondary-electron-emission.md)
* [Thermalized potential](/definitions/thermalized-potential.md)

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2023_Crossref_Journal_of_Electric_Propulsion_Ahedo_Using_electron_fluid_models_to_analyze_plasma_thruster_disch.pdf`.
   * **Version.** Publisher's final typeset version (Springer, "© The
     Author(s) 2023", CC BY 4.0), 31 pages. Article type: review. Received
     25 May 2022, accepted 29 Nov 2022.
   * **Identity.** doi:10.1007/s44205-022-00035-6, checked on Crossref (title
     matches): J. Electr. Propuls. 2(1), article 2; online and issued
     2023-01-25; no print date (online-only journal).
   * **How it was read.** All 31 pages; every equation checked on rendered
     pages 4–28. Figure values for Figs. 3–5 read from the plots (approximate);
     colour-bar ranges of Figs. 1, 2 and 7 approximate.
   * **Recorded as printed.** p. 19 refers to "Eq. (46) in the 1Dz HET kinetic
     model", but eq. 46 belongs to the 1D radial model; p. 21 attributes the
     $T_\perp/B$ behaviour and eq. 53 to "the 1Dr kinetic solution", although
     they come from the paraxial magnetic-nozzle solution, and the same page
     calls that one "the 1Dz kinetic model". Refs. 8 (Inchingolo et al.) and 83
     (Domínguez-Vázquez et al.) both carry the paper number IEPC-2022-338. Ref.
     41's authors are printed garbled ("Domínguez-Vazquez Zhou A J"; Crossref
     lists Zhou J first). Ref. 21 prints year 2017 with PSST vol. 27:015003
     (the 2018 volume). Ref. 1 prints "55(373):001" for article 373001. Eqs. 63
     and 76 omit the reflected-fraction factor of eq. 73, consistent for
     metallic surfaces where it is said to be marginal.
   * **Reference list:** 98 printed entries; Crossref reference-count 98.

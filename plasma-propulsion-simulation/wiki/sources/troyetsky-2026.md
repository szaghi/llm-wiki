---
type: Source
title: "Troyetsky, Bögel & Hara (2026) — Comparison of two-dimensional five-moment fluid and kinetic simulations for the discharge plasma in a Hall effect thruster"
description: "Builds a 2D axial–radial, non-neutral five-moment fluid model of a Hall thruster with electron inertia, two ion fluids and a new energy-limited kinetic flux wall condition, and benchmarks it against an in-house 2D3V PIC-MCC code on an identical set-up: discharge current 10.1 A against 14.7 A, isothermal against non-isothermal field lines, the anisotropic electron pressure the fluid model lacks named as the probable cause of the gap."
resource: "doi:10.1007/s44205-026-00210-z"
source_kind: paper
authors: [Troyetsky D.E., Bögel E., Hara K.]
year: 2026
venue: "J. Electr. Propuls. 5:34"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2026_Crossref_Journal_of_Electric_Propulsion_Troyetsky_Comparison_of_two-dimensional_five-moment_fluid_and_kinetic.pdf"
tags: [fluid, pic, mcc, kinetic, hall-thruster, sheath, wall-interaction, anomalous-transport, numerics, verification]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper develops a 2D Cartesian axial–radial (3V) five-moment (5M) fluid
model of a Hall-thruster discharge: non-neutral (Poisson-coupled), with
electron inertia and two ion fluids. It benchmarks the model against an
in-house 2D3V PIC-MCC code that shares the geometry, magnetic field,
anomalous-collision profile, cross sections, neutral model and Poisson solver.
Two methodological contributions: an electron wall boundary condition, the
energy-limited kinetic flux (ELKF), which truncates a drifting Maxwellian at
the speed needed to cross the boundary-cell potential drop and which the
authors find necessary for a steady state; and a two-population ion fluid
split by local potential. The codes agree qualitatively on many profiles, but
the discharge current is 14.7 A (PIC-MCC) against 10.1 A (5M), and 5M field
lines are isothermal where PIC-MCC's are not. In a term-by-term momentum analysis the
PIC-MCC axial momentum structure correlates most closely with the radial
gradient of the off-diagonal electron pressure, which 5M lacks; the authors
name this anisotropic pressure, together with sheath kinetics, as the
probable cause of the gap, and note that 5M numerical diffusion could
enhance its cross-field transport. Reducing the field-aligned conductivity ad hoc restores
non-isothermality but degrades electron velocity and current fields and
changes the current by only 0.1 A. Neither code is named.

# Key claims

1. **5M system** (eqs. 3–5): per-species continuity, momentum and energy with
   isotropic pressure; steady state without inertia recovers drift-diffusion
   (p. 4).
2. **Electron collisions and anomalous transport** (eqs. 6–9): Krook
   momentum exchange; $\nu_{en}=2.5\times10^{-13}n_n$; excitation and Coulomb
   collisions neglected; Bohm-type anomalous frequency $\alpha\,\omega_{ce}$
   with $\alpha$ = 0.01 for $x<2.25$ cm, a linear ramp, 0.25 for
   $x\ge2.75$ cm ($\alpha_{\mathrm B}$ = 0.16 and 4), isotropic in both codes.
3. **Heat flux** (eqs. 10–13): Fourier law with a field-aligned
   Mitchner–Kruger conductivity tensor.
4. **Two ion populations** (eqs. 14–26): high- and low-energy fluids split by
   a potential-dependent fraction (0 below 30 V, 0.999 above 60 V).
5. **ELKF** (eqs. 31–36, new): closed-form one-sided moments of a drifting
   Maxwellian integrated from a threshold speed; reduces to the kinetic flux
   method at zero threshold; "plays a critical role in obtaining a
   steady-state solution"; without it the 5M model "eventually faced runaway
   electron emission" (p. 21).
6. **Discharge current** (Fig. 4): 10.1 A (5M) against 14.7 A (PIC-MCC), in
   contrast with an earlier 1D comparison that agreed within 0.5 % (Yamashita
   et al., ref. 13).
7. **Electron temperature** (Figs. 5e–f, 6d): 5M peak about 2.7 times lower;
   5M field lines isothermal, PIC-MCC strongly non-isothermal; a Fourier-law
   heat flux is insufficient (pp. 18–19).
8. **Momentum analysis** (eqs. 48–49, Figs. 10–11): in PIC-MCC, between
   $x=1.25$ and 2.25 cm, the axial momentum structure correlates most with the
   radial gradient of the off-diagonal pressure component; inertia matters only
   at the anode–wall corners.
9. **Conductivity study** (Figs. 12–15): scaling the parallel conductivity by
   1 to 0.005 raises the current by 0.1 A and degrades the electron fields;
   ad-hoc tuning is insufficient; a Dufour term from higher-moment closures
   (unshown) reduces the field-aligned heat flux (p. 29).
10. **Heat flux direction** (Fig. 12, p. 26): the peak PIC-MCC conductive heat
    flux is about twice the 5M one and follows Fourier's direction only for
    $x\le1.5$ cm and outside the channel.

# Models and numerics

* **Shared set-up** (Fig. 1, eqs. 1, 40–43): $x$ axial, $y$ radial, $z$
  azimuthal; channel 2.5 × 1.5 cm, plume 2.5 × 3.5 cm; anode 300 V, cathode
  boundary 0 V; dielectric channel walls and pole pieces; $B_y$ Gaussian, peak
  150 G at $L_{ch}=2.5$ cm, widths 1.35 cm inside and 1.0 cm outside;
  permittivity scaled by $f_\varepsilon=10$; Xe at 5 mg/s; quasi-steady 1D
  neutral law in the channel plus a rescaled plume profile, which suppresses
  the 10–30 kHz breathing mode; Poisson by HYPRE GMRES with PFMG, Neumann
  conditions from wall surface charge; linear SEE yield with 51.1 eV for BN,
  secondaries half-Maxwellian at 2 eV; cathode injection at 3 eV with cathode
  current equal to anode current. The channel radii needed by the neutral law
  are not stated.
* **5M**: finite volume, $\Delta x=\Delta y=0.1$ mm, MUSCL with van Leer
  limiter, Steger–Warming flux-vector splitting with entropy fix; SSP-RK2 for
  all equations except the electron energy, which is semi-implicit (θ = 0.5,
  implicit mean-energy diffusion with lagged conductivity); adaptive step with
  CFL 0.4 and $\Delta t<0.4\cdot2\pi/\omega_{pe}$, average about 8 ps; ELKF
  fluxes at all boundaries; MPI, about 3 days on 50 cores for 50 µs.
* **PIC-MCC** (developed by E. Bögel): leap-frog with Boris push,
  $\Delta t=10$ ps; $\Delta x=\Delta y=0.2$ mm; cloud-in-cell weighting; 40
  particles per cell per species initially (20 and 80 gave similar trends),
  $W=1.068\times10^8$; null-collision MCC for ionization, elastic plus
  anomalous scattering (isotropic) and charge exchange (neutral sampled at
  0.1 eV, velocities swapped); absorbing walls with probabilistic SEE; MPI
  particle decomposition, about 5 weeks on 100 cores for 50 µs; averages over
  30–50 µs.
* Not stated: total cell counts, implementation language, GPU use, code names.

# Tests and results

Single case, 300 V, 5 mg/s Xe, run to 50 µs (steady for about 20 µs).

* Discharge current 10.1 A against 14.7 A (Fig. 4).
* PIC-MCC peak plasma density about 70 % higher, at $x=1.1$ cm against 0.8 cm
  (Figs. 5a–d, 6a); 5M ion density higher near the anode.
* Maximum scalar temperature 16 eV (5M) against 25 eV (PIC-MCC), in the ion
  paragraph (p. 17); PIC-MCC axial ion temperature peaks at 74 eV near the
  exit.
* Peak potential 319 V at $x\approx0.9$ cm (5M) against 310 V at $x=1.1$ cm;
  anode-region field about twice as large in 5M (Figs. 5g–h, 6e–f).
* PIC-MCC forms a space-charge-limited sheath with trapped secondaries near
  $x\approx2.1$ cm; 5M does not, with yields of 0.92–0.983 there (Fig. 9).
* Ion current more centred and less divergent in 5M; electron current agrees
  upstream of $x=1.2$ cm and in the plume (Fig. 7).

# Notation map

| Troyetsky et al. (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$, $y$, $z$ | $z$ (axial), $r$ (radial), $\theta$ (azimuthal) | **collision:** the paper's $z$ is azimuthal, the registry's $z$ axial; planar $x,y$ kept with this mapping |
| $n_s$, $\vec u_s$, $p_s$, $\vec q_s$ | $n_s$, $\mathbf u_s$, $p_s$, $\mathbf q_s$ | |
| $k_BT_s$ | $T_s$ | registry temperatures in energy units |
| $\epsilon_s$ | $\tfrac32T_s+\tfrac12m_s|\mathbf u_s|^2$ | mean energy per particle; not a registry symbol |
| $\epsilon_0'=f_\epsilon^2\epsilon_0$, $f_\epsilon$ | $f_\varepsilon^2\varepsilon_0$, $f_\varepsilon$ | same convention |
| $\nu_a$, $\alpha_\nu$ | $\nu_{\mathrm{ano}}$, $\alpha_{\mathrm B}/16$ | $\nu_a=\alpha_\nu\omega_{ce}$, so $\alpha_{\mathrm B}=16\alpha_\nu$ |
| $\Omega_H$ | $\Omega_e$ | |
| $\kappa_{e\parallel}$, $\kappa_{e\perp}$, $\alpha_q$ | words | conductivity and its scaling factor |
| $\alpha$ (eq. 22) | words | ion population split; the paper uses $\alpha$ three ways |
| $\delta_{SEE}$, $\epsilon^*$ | $\delta_{\mathrm{SEE}}$; words | |
| $\sigma$ (surface charge) | words | **collision** with the cross section $\sigma_{sk}$ |
| $\sigma_{CEX}$ | $\sigma_{sk}$ (charge exchange) | |
| $w_p$, ppc | $W$, $N_{\mathrm{ppc}}$ | |
| $I_a$, $I_c$ | $I_d$ | anode and cathode currents, equal by construction |
| $c_m=\sqrt{2k_BT/m}$ | $v_{th,s}$ with the $\sqrt2$ convention | |

# Pages created or updated

Chunk 1 (2026-10-14) created every page of the bundle. This source is cited on:

* [Anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md)
* [Breathing mode](/definitions/breathing-mode.md)
* [Charge-exchange ions](/definitions/charge-exchange-ions.md)
* [Cross-field electron mobility and the Hall parameter](/definitions/electron-mobility-and-hall-parameter.md)
* [Electron fluid models (drift-diffusion)](/methods/electron-fluid-model.md)
* [Five-moment electron fluid model](/methods/five-moment-fluid-model.md)
* [Gas–surface interaction models](/methods/gas-surface-interaction.md)
* [Monte Carlo collisions and the null-collision method](/methods/monte-carlo-collisions.md)
* [Particle pushers: leapfrog, Boris and Runge–Kutta](/methods/particle-pushers.md)
* [Particle-in-cell with Monte Carlo collisions (PIC-MCC)](/methods/pic-mcc.md)
* [Permittivity, ion-mass and geometric scaling in PIC](/methods/pic-acceleration-scaling.md)
* [Resolution constraints of explicit PIC](/definitions/explicit-pic-resolution-constraints.md)
* [Secondary electron emission and sheath regimes](/definitions/secondary-electron-emission.md)

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2026_Crossref_Journal_of_Electric_Propulsion_Troyetsky_Comparison_of_two-dimensional_five-moment_fluid_and_kinetic.pdf`.
   * **Version.** Final published version of record (journal typeset, "(2026)
     5:34", 32 pp.), CC BY-NC-ND 4.0. Received 2 April 2026, accepted 2 July
     2026. Code availability: "In-house code".
   * **Identity.** doi:10.1007/s44205-026-00210-z, checked on Crossref (title,
     authors, volume 5, issue 1, article 34 match): J. Electr. Propuls. 5:34;
     online and issued 2026-07-28; no print date (online-only journal).
   * **How it was read.** All pages; equations from rendered pages 3, 4, 6, 7,
     10, 11 or a clean text layer (eqs. 6–9, 27–30, 40–49). Colour-map figures
     not extracted beyond the numbers in the text.
   * **Recorded as printed.**
     - p. 3: $\lambda_D$ printed with $e$ instead of $e^2$ in the denominator
       (dimensionally wrong).
     - Eq. 38: the right-hand side $-(\dot n_{iz}-\mathcal C_e)/n_e$ is
       dimensionally inconsistent; the intended term is unclear.
     - p. 7 against eq. 21: the charge-exchange rate contains $n_n$ twice.
     - The location where the anomalous frequency "begins to increase" is
       given as $x\approx2.0$ cm (p. 18) and 2.25 cm (pp. 17, 24, eq. 8);
       p. 20 says it "sharply decreases" at 2.25 cm.
     - p. 22: the higher PIC-MCC SEE yield is "explained by the higher electron
       energy near the walls in the latter result", where "former" is meant.
     - p. 28: panel references to Fig. 14 are offset from the caption ((d) for
       (e), (f) for (g), (g) for (h)); p. 27 "the dip at cm" lacks its number.
     - p. 17: the 16 eV / 25 eV maxima are not explicitly labelled as ion
       temperatures.
   * **Reference list:** 55 printed entries; Crossref reference-count 55.

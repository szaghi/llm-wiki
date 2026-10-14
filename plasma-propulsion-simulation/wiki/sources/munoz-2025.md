---
type: Source
title: "Muñoz Tejeda, Perales-Díaz & Knoll (2025) — Computational modelling of water-fuelled Hall Effect Thrusters"
description: "Extends the fully kinetic PIC code PlasmaSim to oxygen- and water-fed Hall thrusters with a two-stage electron-impact reaction set (parent molecule, then dissociation products), a 0D screening model and a partially coupled pseudo-2D axial–radial Poisson solver, and compares thrust, specific impulse and plume ion fractions with WET-HET experiments."
resource: "doi:10.1007/s44205-025-00124-2"
source_kind: paper
authors: [Muñoz Tejeda J.M., Perales-Díaz J., Knoll A.]
year: 2025
venue: "J. Electr. Propuls. 4:27"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2025_Crossref_Journal_of_Electric_Propulsion_Muñoz_Computational_modelling_of_water-fuelled_Hall_Effect_Thruste.pdf"
tags: [pic, mcc, kinetic, hall-thruster, anomalous-transport, wall-interaction, software]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper presents the water-propellant extension of PlasmaSim, the
in-house fully kinetic electrostatic PIC code of the Imperial Plasma
Propulsion Laboratory (C++ and Unreal Engine), for two concepts of the
WET-HET Hall thruster: oxygen fed through the anode (water electrolysis
propulsion) and direct water vapour. A 0D one-cell model with a uniform
field screens the chemistry and supplies initial densities to a pseudo-2D
axial–radial PIC whose Poisson equation uses a separable potential. The
main contribution is a "double-stage" electron-impact reaction model: the
first stage holds the reactions of the parent molecule (O₂ or H₂O), the
second those of the dissociation products. The 0D model shows that the
second stage is indispensable and that ionization fractions follow power
laws in $T_e$. The 2D model gives axial profiles, species fractions and
inelastic-loss budgets; thrust, $I_{sp}$ and anode efficiency at 300 V and
1 mg/s are compared with WET-HET experiments, and the plume O₂⁺/O⁺
fractions with a plume measurement.

# Key claims

1. **0D + 2D framework** (§"Materials and methods", Fig. 3). The 0D steady
   state initializes the 2D run; species about two orders of magnitude
   below the others are dropped with the reactions producing them. 2D costs
   about $10^6$ times 0D per simulated µs (stated, no timing table).
2. **Partially coupled pseudo-2D Poisson** (§"PlasmaSim 2D", Eqs. 1–5).
   Potential = function of axial $x$ + function of radial $y$; integrating
   Poisson's equation once along each direction gives two ODEs that keep the
   other potential's boundary derivatives; $N+N$ equations instead of
   $N\times N$. Stated to be more accurate than the fully decoupled version,
   with no test here. Dirichlet at cathode (0) and anode ($V_d$);
   surface-charge Neumann conditions with a dimensionless wall capacitance
   (5) at the walls. Method attributed to A. Knoll, developed in Faraji,
   Reza et al.
3. **Anomalous collisions** (Eq. 7). $\nu_{\mathrm{ano}}=\alpha_{\mathrm B}\omega_{ce}/16$
   with $\alpha_{\mathrm B}=0.01$, uniform, electrons only, elastic isotropic
   scattering without energy loss, collision probability $\nu_{\mathrm{ano}}\Delta t$.
   A tenfold larger value extinguishes the plasma by demagnetizing the
   electrons (stated sensitivity, not shown).
4. **Double-stage reaction model** (Tables 3–4). Oxygen: 10 first-stage and
   8 second-stage reactions (18 stated and counted). Water: 45 stated (25 +
   20), with 17 + 20 rows printed. Per-electron collision frequency (Eq. 8):
   target density times the cross section at the electron energy times the
   square root of the electron speed squared plus the target species' mean
   speed squared, against a target built from local cell properties; the
   whole energy loss is taken
   from the incident electron and the remainder shared equally among
   outgoing electrons (Eq. 9), directions by Marsaglia's method. The
   reaction model takes about 34% of run time, half per stage.
5. **First stage alone is insufficient** (Fig. 4, 0D, injected $T_e$ = 20 eV).
   Oxygen: atomic O dominates the neutrals, O₂⁺ is 80% of the ions. Water:
   neutrals OH and H, ions mainly H₂O⁺. Shown.
6. **Ion ratios vs injected $T_e$** (Tables 5–6, 0D). O⁺/O₂⁺ = 158, 150,
   143, 132, 120 per 100 at 5, 10, 15, 20, 35 eV. Water at the same
   temperatures: OH⁺/H₂O⁺ 150–167, H⁺/H₂O⁺ 19–65, O⁺/H₂O⁺ 50–33, H₂⁺/H₂O⁺
   0.1–100 per 100. Shown.
7. **Power-law ionization fractions** (Fig. 6). Ion-to-neutral density
   ratios fit $A\,T_e^{B}$ over 3–35 eV with exponents 1.394–1.8785 and
   $R^2$ 0.9876–0.9966. Shown (0D).
8. **2D oxygen** (Fig. 7, Table 7). Removing reactions found negligible in
   0D speeds the run by about ×1.5; potential drops mainly inside the
   channel; anode sheath 20–50 V (about 3–4 local $T_e$), decreasing with
   flow; O₂/O and O₂⁺/O⁺ split about 40–60%. Inelastic loss fractions: O₂
   ionization 0.27, dissociation 0.12, excitation 0.09; O ionization 0.32,
   excitation 0.21. Agreement with Taccogna et al. (2022) that atomic O
   ionization is the largest sink (stated).
9. **2D water vapour** (Figs. 9–10, Table 8). Speed-up about ×2 from
   pruning; H excitation 0.44 and H ionization 0.25 of inelastic losses;
   light ions concentrate at the channel centre, molecular ions near the
   walls (attributed to wall recombination). H⁺ dominates the ions in 2D,
   unlike 0D.
10. **Performance vs experiment** (Eqs. 10–14). At 300 V, 1.0 mg/s, peak
    field 0.025 T: O₂ simulation 520 W, 1.6 A, 7.8 mN, 720 s, 5.85%
    (experiment 696 W, 272 V, 2.56 A, 7.7 mN, 696 s, 4.3%); H₂O simulation
    1200 W, 4.0 A, 12.4 mN, 933 s, 6.41% (experiment 1148 W, 287 V, 4.0 A,
    11.2 mN, 1142 s, 5.46%). Inelastic losses are about 13% (O₂) and 16%
    (H₂O) of discharge power. Agreement called "reasonable".
11. **Plume composition** (end of §"Performance evaluation"). Measured O₂⁺
    39%, O⁺ 61% at 400 W; simulated 43% and 55% at 520 W.

# Models and numerics

* Fully kinetic electrostatic PIC: electrons, ions and neutrals as
  macroparticles, Boris push (Eq. 6). Annulus unwrapped into a Cartesian box
  ($x$ axial, $y$ radial, $z$ azimuthal, periodic), no curvature; axial
  extent channel length + 25%; WET-HET channel 35 mm long, 5 mm wide, mean
  diameter 20 mm, cathode at 44 mm.
* No permittivity, mass or geometric scaling.
* $\Delta t$ = minimum of plasma-frequency, gyro-frequency and CFL steps
  with safety factor 25, adapted dynamically; $\Delta x$ below the smallest
  local $\lambda_D$ (safety factor 6), uniform, adapted dynamically; about
  40,000 cells; population control targets at least 25 (text) or more than
  50 (Table 1) particles per cell per species; constant initial weights
  (values not stated); Box–Muller sampling.
* Monte Carlo electron-impact collisions (no null-collision method stated);
  no heavy–heavy collisions stated; metastables, O₂ vibrational/rotational
  modes and dissociative recombination not modelled.
* Boundaries (Table 2): anode removes electrons, recombines ions, reflects
  neutrals; cathode quasineutrality injection at 5 eV; dielectric walls with
  linear SEE after Croes (Maxwellian emission at 1 eV, reflection yield 0.5);
  neutrals injected at 300 K with 750 m/s drift.
* Inputs (Table 1): anode flow 0.8, 1.0, 1.3 mg/s; 300 V; Gaussian field
  peak 0.025 T; initial $n_i=2\times10^{20}$ m⁻³; injected $T_e$ 5 eV,
  $T_i$ 0.1 eV, $T_n$ 300 K.
* PlasmaSim: C++ and Unreal Engine (a pure C++ parallel version exists);
  shared memory (OpenMP, Unreal ParallelFor); no GPU or MPI stated; one 2D
  run "can still require several weeks" for 10 µs.

# Tests and results

* 0D: first stage only (Fig. 4); full model at 35 eV (Fig. 5); injected-$T_e$
  scan 5–35 eV (Tables 5–6); power-law fits (Fig. 6).
* 2D oxygen and water vapour at 0.8, 1.0, 1.3 mg/s (Figs. 7–10, Tables
  7–8).
* Performance against WET-HET (Key claim 10), with SPT-100 xenon reference
  values quoted (598 W: 40 mN, 1050 s, 34.5%; 1130 W: 64.9 mN, 1270 s,
  35.8%) and a high-power O₂ experiment (2232 W, 0.60 mg/s: 21.5 mN,
  3617 s, 17.1%).
* Plume composition against measurement (Key claim 11).

# Notation map

| Muñoz Tejeda et al. (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$, $y$, $z$ | $z$, $r$, $\theta$ | **collision:** the paper's $z$ is azimuthal, the registry's $z$ is axial |
| $\phi_1(x)$, $\phi_2(y)$ | words | 1D components of $\phi$ |
| $\rho$, $\rho^x$, $\rho^y$ | $\rho_c$; averages in words | |
| $\sigma_{inner}$, $\sigma_{outer}$ | words (wall surface charge) | **collision:** registry $\sigma_{sk}$ is a cross section |
| $C$ | words (dimensionless wall capacitance) | |
| $W$ (channel width), $L$ | words; $L$ | **collision:** registry $W$ is the macroparticle weight |
| $\phi_m$ (mean diameter) | words | not a potential |
| $T$ (thrust) | $F$ | **collision:** registry $T_s$ is temperature |
| $g$ | $g_0$ | |
| $\eta_A$ | $\eta$ (anode) | Eq. 13 uses an ion-velocity $I_{sp}$ |
| $\nu_t$, $k$ | $\nu_{\mathrm{ano}}$, $\alpha_{\mathrm B}$ | $\nu_t=k\omega_{ce}/16$: same convention, $\alpha_{\mathrm B}=k=0.01$ |
| $\nu_k$, $\sigma_k$, $c_k$ | $\nu_{ek}$, $\sigma_{ek}$, words | $c_k$: mean speed of the target species |
| $E_{reac}$, $E_{lost}$ | words | |
| $P_t$, $t_{step}$ | $P_c$, $\Delta t$ | linearized: $P_t=\nu_t\,t_{step}$ |
| $\pi$ | words (ion-to-neutral density ratio) | |
| $\epsilon_0$ / $\varepsilon_0$ | $\varepsilon_0$ | |

# Pages created or updated

Chunk 1 (2026-10-14) created every page of the bundle. This source is cited on:

* [Anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md)
* [Hall-effect thruster](/definitions/hall-effect-thruster.md)
* [Monte Carlo collisions and the null-collision method](/methods/monte-carlo-collisions.md)
* [Particle pushers: leapfrog, Boris and Runge–Kutta](/methods/particle-pushers.md)
* [Particle-in-cell with Monte Carlo collisions (PIC-MCC)](/methods/pic-mcc.md)
* [Permittivity, ion-mass and geometric scaling in PIC](/methods/pic-acceleration-scaling.md)
* [Reduced-order (pseudo-2D) PIC](/methods/reduced-order-pic.md)
* [Resolution constraints of explicit PIC](/definitions/explicit-pic-resolution-constraints.md)
* [Secondary electron emission and sheath regimes](/definitions/secondary-electron-emission.md)
* [SPT-100 as a validation case](/benchmarks/spt-100.md)

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2025_Crossref_Journal_of_Electric_Propulsion_Muñoz_Computational_modelling_of_water-fuelled_Hall_Effect_Thruste.pdf`.
   * **Version.** Publisher's version of record (Springer, 30 pp., Open
     Access CC BY 4.0), marked "corrected publication 2025"; no correction
     notice found on Crossref. Received 7 August 2024, accepted 25 March
     2025, published 24 April 2025. A Research Square preprint
     (doi:10.21203/rs.3.rs-4874324/v1) exists and was not read.
   * **Identity.** doi:10.1007/s44205-025-00124-2, printed on page 1 and
     checked on Crossref (title, venue, authors Muñoz Tejeda J.M.,
     Perales-Díaz J., Knoll A.): J. Electr. Propuls. 4(1), article 27;
     issued and published online 2025-04-24, no print date.
   * **How it was read.** Full text; Tables 3–4 (vector graphics) read from
     a 200–300 dpi render; Fig. 6 fit coefficients read from the panels
     (the $R^2$ of the H fit not legible); Eq. 8 read from the render
     (garbled text layer).
   * **Recorded as printed.**
     * Water reaction count: 45 stated (25 + 20), but Table 4 prints 17
       first-stage and 20 second-stage rows; the four H₂O rotational modes
       the text mentions are absent from the table.
     * Table 1 footnote marks the wall capacitance "Not applicable to the
       2D simulations", while the 2D wall conditions use it.
     * Particles per cell: "at least 25" in the text, "> 50" in Table 1.
     * Injected $T_e$: 5 eV in Table 1, 15 eV as an example in the text,
       20 and 35 eV in the 0D figures.
     * The ionization-fraction fit is written $AT_e^{-B}$ and called
       "exponential"; the panels show positive exponents of a power law.
     * Oxygen performance: 300 V × 1.6 A = 480 W, not 520 W; Eq. 13 with
       the printed thrust and $I_{sp}$ gives 5.3% (520 W) or 5.7% (480 W),
       not 5.85%. Water: Eq. 13 gives about 4.7%, not 6.41%. O₂ experiment:
       3.8%, not 4.3%; $\eta_A$ is also called an "anode specific impulse".
     * Eq. 12 sums mean axial velocities over species, which overcounts for
       several species (reader's judgment); $F/(\dot m g_0)$ would give
       795 s (O₂) and 1264 s (H₂O).
     * "Total ionisation losses are approximately 15.52 eV" is not
       derivable from the printed values.
     * Loss fractions sum to 1.01 (Table 7) and 1.06 (Table 8).
     * Azimuthal extent described as both "the mean radius of curvature" and
       "the perimeter of the chamber".
     * p. 18 names O₂⁺ twice for two different ion species; "Fig. 9e" should
       read Fig. 7e; further cross-reference slips (Fig. 5 caption, section
       pointer, "Table 2" for Table 1).
     * 2D water ions: H⁺ predominant, against OH⁺ > H₂O⁺ > H⁺ in 0D (a model
       difference the conclusions acknowledge).
   * **Reference list.** 83 printed entries (Crossref reference-count 83).


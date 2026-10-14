---
type: Source
title: "Taccogna & Garrigues (2019) — Latest progress in Hall thrusters plasma modelling"
description: "Review of Hall-thruster plasma modelling: quasi-neutral fluid and hybrid models (drift-diffusion electrons, field-aligned meshes, thermalized potential, analytical SEE sheaths, the catalogue of anomalous collision models) and kinetic models (Boltzmann solvers, 1D radial, 2D r–z, azimuthal and 3D PIC-MCC of the electron drift instability and sheaths, plume kinetics, global models)."
resource: "doi:10.1007/s41614-019-0033-1"
source_kind: paper
authors: [Taccogna F., Garrigues L.]
year: 2019
venue: "Rev. Mod. Plasma Phys. 3:12"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2019_Crossref_Reviews_of_Modern_Plasma_Physics_Taccogna_Latest_progress_in_Hall_thrusters_plasma_modelling.pdf"
tags: [review, hall-thruster, fluid, hybrid, pic, anomalous-transport, instability, sheath, wall-interaction]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

A review of Hall-thruster plasma modelling in two parts. Part 1 (Sect. 2)
covers quasi-neutral fluid and hybrid models: the moment hierarchy, the
drift-diffusion electron closure and the generalized-Ohm potential solve
with its anisotropy problem, magnetic-field-aligned meshes and Morozov's
thermalized potential, analytical sheaths with secondary-electron emission
(SEE) and space-charge saturation, and the catalogue of anomalous
collision-frequency models (Tab. II). Illustrations cover nominal
operation, operating regimes, the breathing mode, erosion and lifetime, and
magnetic shielding. Part 2 (Sect. 3) covers kinetic models: Boltzmann
solvers for the electron distribution; 1D radial PIC-MCC of SEE sheaths; 2D
r–z PIC with a Bohm-type anomalous collision; azimuthal PIC (1D-θ, 2D r–θ,
2D θ–z) of the electron drift instability; 3D PIC; plume kinetics; and 0D
global and collisional-radiative models. Appendices give SEE yield models,
the sputtering erosion model and Poisson solvers. Almost every claim is
attributed to cited work; Figs. 16, 19 and 20 carry no attribution and no
set-up beyond their captions.

# Key claims

All claims are attributed to cited work unless marked as the review's own.

1. **Typical parameters** (§1, §2.2; review). Discharge current about 4 A
   for a kW-class thruster; about 20% of the cathode current enters the
   channel; field about 100 G; about 90% of the injected neutrals ionized.
   With $n_e\sim10^{18}$ m⁻³ and $T_e\sim50$ eV, $\lambda_D\approx50$ µm
   against a 2 cm device, so resolving $\lambda_D$ needs more than 400
   cells per direction.
2. **Drift-diffusion electrons and mobility tensor** (§2.1, eqs. 11–16;
   Hagelaar et al. 2011). Parallel, perpendicular and Hall mobilities
   $\mu_\parallel$, $\mu_\parallel/(1+\Omega_e^2)$, $\pm\mu_\parallel\Omega_e/(1+\Omega_e^2)$;
   heat-flux closure eq. 15. Hybrid PIC needs about 100 particles per cell
   for heavy-species properties (review).
3. **Anisotropy of the potential solve** (§2.2, eqs. 18–23). In $r$–$z$
   components the current-continuity flux is a sum of large opposite-sign
   terms, and numerical error can dominate cross-field transport (Hagelaar
   2016); a magnetic-field-aligned mesh removes the problem (Mikellides &
   Katz 2012). Thermalized potential, eqs. 24–25 (Morozov & Savelyev 2000).
4. **Sheaths with SEE** (§2.3, eqs. 26–30). Zero-net-current dielectric
   wall, sheath drop eq. 27; space-charge saturation at
   $\delta^*_{\mathrm{SEE}}=1-8.3\sqrt{m_e/m_i}\approx0.983$ for xenon
   (Hobbs & Wesson 1967), where the drop is about $T_e/e$; electron–wall
   momentum frequency eq. 28; wall power loss eq. 29; empirical wall loss
   eq. 30.
5. **Anomalous transport** (§2.4, Tab. II, after Jorns 2018). Five forms:
   near-wall conductivity, Bohm-like, shear-flow, small-scale turbulence,
   wave trapping. Classical Bohm is $\alpha_{\mathrm B}=1$; fitted
   coefficients are $\alpha_{\mathrm B}\sim0.16$; near-wall conductivity
   alone is insufficient (Ahedo et al. 2003). Self-consistent route through
   a wave-energy equation; data-driven route through laser-induced
   fluorescence; a genetic-algorithm fit (Jorns 2018) printed as
   $\nu_{\mathrm{ano}}\propto\omega_{ce}(c_s/u_{e,\theta})^2$.
6. **Nominal operation** (§2.5, Figs. 4–5). About 50% of the potential drop
   occurs outside the channel (a general trend; Bareilles et al. 2003). A
   hybrid model whose $\mu_\perp$ profile is fitted to measured ion velocity
   shortens the acceleration region (Garrigues et al. 2009).
7. **Operating regimes and the breathing mode** (§2.6, Figs. 6–7). Three
   SPT-100 regimes against wall material; the low-voltage regime shows a
   rotating $m=1$ structure; the breathing mode at about 20 kHz is neutral
   depletion and refilling (Boeuf & Garrigues 1998; Darnon et al. 1999).
8. **Erosion and magnetic shielding** (§2.7–2.8). Tuning anomalous
   coefficients to erosion does not guarantee current or performance;
   magnetic shielding reduces computed erosion by 3 orders of magnitude,
   confirmed experimentally (Mikellides et al. 2014).
9. **Explicit PIC-MCC constraints** (§3; review). $\Delta x<\lambda_D$,
   $\Delta t<1/\omega_{pe}$, CFL, $N_{\mathrm{ppc}}>50$–100; typical
   $\Delta x<30$ µm and $\Delta t<5\times10^{-12}$ s.
10. **Boltzmann solvers with walls** (§3.1). Depleted high-energy tail,
    no space-charge saturation, minor near-wall conductivity (Latocha 2002;
    Meezan & Cappelli 2002).
11. **1D radial PIC** (§3.2, eqs. 31–33, Figs. 13–14). Floating-wall
    boundary conditions; relaxation sheath oscillations switching between
    saturated and unsaturated sheaths (Sydorenko et al. 2009).
12. **2D r–z PIC** (§3.3, Fig. 15). Speed-up tricks (reduced mass ratio,
    enlarged $\varepsilon_0$, geometric scaling) break similarity and
    affect sheaths and instabilities (review). Anomalous collision
    $\omega_{ce}/\beta$, fitted $\beta=50$–500 ($\alpha_{\mathrm B}=0.32$–0.032);
    global performance within 20% in thrust and discharge current
    (review).
13. **Azimuthal PIC and the ECDI** (§3.4, eqs. 34–35, Figs. 16–18).
    Mobility from correlated fluctuations (eq. 34, Lafleur et al. 2016);
    cyclotron resonances and maximum growth at $\omega_{pi}/\sqrt3$; 1D-θ
    models give mobility about ten times too large; nonlinear-regime
    disagreement between ion-sound transition and persistent cyclotron
    modes, attributed to the missing axial dimension; MTSI in 2D r–θ;
    SEE–ECDI coupling (bulk mobility −20%, near-wall mobility ×2); θ–z
    scalings $\lambda_w\sim\lambda_D$, $\omega\sim\omega_{pi}$.
14. **Noise** (§3.4; review). Noise destroys the cyclotron resonances and
    "facilitates the transition to an ion acoustic instability"; "it seems"
    that more than 1000 particles per cell are needed. Charoy et al. (2020)
    read the ion-acoustic character as physical: see the Open entry on the
    [electron drift instability](/definitions/electron-drift-instability.md)
    page. LANDMARK defines benchmark cases for PIC,
    hybrid and fluid models of $\mathbf E\times\mathbf B$ plasmas.
15. **3D PIC and spokes** (§3.5). First 3D attempt on an SPT-50 with small
    ion mass and large $\varepsilon_0$ (Hirakawa & Arakawa); current 3D
    models handle miniaturized thrusters; rotating spoke: kHz, cm,
    phase velocity about $0.2E_z/B_r$ (Ellison 2012).
16. **Plume** (§3.6). "One third of the potential drop occurs in the
    plume" (review; see Recorded as printed); polytropic index 1.2–1.5 for
    the SPT-100 plume (Giono et al.).
17. **Outlook** (§4; review opinion). Kinetic methods are the most
    effective; larger 3D domains with lower noise, data-intensive
    modelling and machine learning, a community "virtual laboratory".

# Models and numerics

A review: no model of its own is documented. Fluid/hybrid models are
quasi-neutral with drift-diffusion electrons, an anisotropic mobility
tensor and an energy equation; heavy species as fluids, direct-kinetic or
PIC with about 100 particles per cell; potential from current continuity
on Cartesian or field-aligned meshes; analytical sheaths. Kinetic models
are explicit electrostatic PIC-MCC (Taccogna 2015) with the constraints of
claim 9, floating-wall conditions eqs. 31–33, linear, modified-Vaughan or
Furman–Pivi SEE, mass-ratio, permittivity and geometric scaling, and
direct-implicit PIC in Sydorenko's code. Not stated: code names (except
titles of cited works), languages, parallelism, run times, particle
weights, scaling factors. Fig. 16: $N_{\mathrm{ppc}}=2.5\times10^4$, azimuthal
length 5 cm, nothing else.

# Tests and results

No simulation of the review's own is documented in its text. Reproduced
cases (all attributed): wall loss models against SEE theory (Fig. 3);
2D r–z hybrid nominal operation at 300 V, 5 mg/s (Fig. 4); PPS X000-ML at
500 V, 6 mg/s (Fig. 5); SPT-100 current–voltage curves for three wall
materials (Fig. 6); breathing mode at 280 V, 5 mg/s, period 30 µs
(Fig. 7); wall erosion histories (Fig. 8); H6 unshielded against shielded
(Fig. 10); 1D radial PIC distributions and relaxation sheath oscillations
(Figs. 13–14); 2D r–z PIC with and without anomalous collision at 750 V,
2 mg/s (Fig. 15); 1D-θ PIC (Fig. 16, unattributed); 2D r–θ spectra with
MTSI (Fig. 17); 2D θ–z PIC, $E_\theta$ within $\pm5\times10^4$ V/m, $n_i$ up to
$5\times10^{17}$ m⁻³ (Fig. 18); 3D sector PIC (Fig. 19, unattributed); 3D
near-plume PIC (Fig. 20, unattributed); SEE yields and BN sputtering fits
(Figs. 21–22, Tabs. III–IV).

# Notation map

| Taccogna & Garrigues (2019) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $z,r,\theta$; $x$ (axial in Figs. 4, 18, 20; radial in Fig. 13); $y$ azimuthal | $z,r,\theta$; $x,y$ | the paper reuses $x$ for axial and radial |
| subscripts $e,i,a$ | $s\in\{e,i,n\}$ | **collision:** $a$ (atoms) → $n$ |
| $\mathbf r$, $f(\mathbf r,\mathbf v,t)$ | $\mathbf x$, $f_s(\mathbf x,\mathbf v,t)$ | |
| $\varepsilon_e$ (mean energy, eV) | words | $T_e=2\varepsilon_e/3$ |
| $\mu_0=e/(m_e\nu_e)$ | $\mu_\parallel$ | **collision:** $\mu_0$ is the vacuum permeability in the registry |
| $\boldsymbol\Omega_e$, $\Omega$ | $\Omega_e$ | vector form in the paper |
| $\omega_e$ (Tab. II) | $\omega_{ce}$ | the paper's $\omega_e$ is the cyclotron frequency |
| $k_{ano}$ | $\alpha_{\mathrm B}=16k_{ano}$ | classical Bohm $k_{ano}=1/16$ is $\alpha_{\mathrm B}=1$ |
| $\beta$ (§3.3, $\nu=\omega_{ce}/\beta$) | $\alpha_{\mathrm B}=16/\beta$ | $\beta=16$ is $\alpha_{\mathrm B}=1$ |
| $\nu_{e,coll}$, $\nu_{e,ano}$, $\nu_{e,w}$ | $\nu_e$ (classical part), $\nu_{\mathrm{ano}}$, $\nu_w$ | |
| $\sigma$, $\bar\sigma$, $\sigma_{SCS}$ (SEE yield) | $\delta_{\mathrm{SEE}}$, Maxwellian average in words, $\delta^*_{\mathrm{SEE}}$ | **collision:** $\sigma$ is a cross section in the registry; the paper also uses $\sigma_w$ for surface charge |
| $\phi_s$ | $\Delta\phi_{\mathrm{sh}}$ | sheath drop |
| $h=R_2-R_1$ | words (channel width) | **collision:** eq. 34 reuses $h$ for the Hall parameter |
| $v_{i,w}$, $c_s$, $c_{si}$ | $c_s$ | |
| $v_{de}$ | $\vert u_{e,\theta}\vert$ | $\mathbf E\times\mathbf B$ drift speed |
| $\rho_e$ (Larmor radius); $\rho$ (eq. 44) | $r_L$; $\rho_c$ | **collision:** registry $\rho_c$ is charge density |
| $\epsilon$, $\epsilon_0$ | $\varepsilon_0$ | |
| $\lambda_{De}$, $\omega_{pi}$, $k_{\theta,n}$ | $\lambda_D$, $\omega_{pi}$, $k_\theta$ | |
| $\gamma$ (plume polytropic index) | $\gamma$ | |
| $Y$, $Y_\varepsilon$, $Y_\theta$ | $Y$ | sputtering yield |
| $n_p$ | $n_e$ | quasi-neutral plasma density |

# Pages created or updated

Chunk 1 (2026-10-14) created every page of the bundle. This source is cited on:

* [Anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md)
* [Bayesian calibration of thruster models](/methods/bayesian-calibration.md)
* [Boltzmann-relation electrons](/methods/boltzmann-electron-model.md)
* [Breathing mode](/definitions/breathing-mode.md)
* [Cross-field electron mobility and the Hall parameter](/definitions/electron-mobility-and-hall-parameter.md)
* [Electron drift instability (ECDI)](/definitions/electron-drift-instability.md)
* [Electron fluid models (drift-diffusion)](/methods/electron-fluid-model.md)
* [Hall-effect thruster](/definitions/hall-effect-thruster.md)
* [Hybrid PIC–fluid models](/methods/hybrid-pic-fluid-model.md)
* [Instability-enhanced electron–ion friction and effective mobility](/results/instability-enhanced-friction-force.md)
* [Magnetic shielding](/definitions/magnetic-shielding.md)
* [Magnetic-field-aligned meshes](/methods/magnetic-field-aligned-mesh.md)
* [Monte Carlo collisions and the null-collision method](/methods/monte-carlo-collisions.md)
* [Near-wall conductivity](/definitions/near-wall-conductivity.md)
* [One-dimensional fluid model of the Hall-thruster discharge](/methods/one-dimensional-fluid-hall-model.md)
* [Particle-in-cell with Monte Carlo collisions (PIC-MCC)](/methods/pic-mcc.md)
* [Permittivity, ion-mass and geometric scaling in PIC](/methods/pic-acceleration-scaling.md)
* [Polytropic electron closure and plume cooling](/definitions/polytropic-electron-closure.md)
* [Resolution constraints of explicit PIC](/definitions/explicit-pic-resolution-constraints.md)
* [Rotating spoke](/definitions/rotating-spoke.md)
* [Secondary electron emission and sheath regimes](/definitions/secondary-electron-emission.md)
* [Semi-implicit, implicit and energy-conserving PIC](/methods/implicit-and-energy-conserving-pic.md)
* [SPT-100 as a validation case](/benchmarks/spt-100.md)
* [Thermalized potential](/definitions/thermalized-potential.md)

# Citations

1. `~/papers/mosaic/plasma-propulsion-simulation/2019_Crossref_Reviews_of_Modern_Plasma_Physics_Taccogna_Latest_progress_in_Hall_thrusters_plasma_modelling.pdf`.
   * **Version.** The HAL accepted manuscript (hal-02326278, deposited
     22 Oct 2019), 51 pages, title-cased "Latest Progress in Hall Thrusters
     Plasma Modelling", with an unfilled header ("Received: ? / Accepted:
     ?", "Published online: ?"). Not the typeset article; no publisher page
     numbers.
   * **Identity.** doi:10.1007/s41614-019-0033-1, checked on Crossref (title
     and authors match): Rev. Mod. Plasma Phys. 3(1), article 12, issue
     2019-12, online 2019-07-18. Review paper.
   * **How it was read.** Text extraction of all sections; eqs. 1–43,
     Tabs. I–IV, the θ–z scalings of §3.4 and the Jorns fit checked on
     rendered pages 6–15, 24–26, 28–29, 31–33 and 37–39. Eqs. 44–45 from
     the text layer. The parameters of the Fig. 14 raster (embedded from
     Sydorenko et al. 2009) leak into the text layer and are not used.
   * **Recorded as printed.**
     * Plume share of the potential drop: "typically 50%" outside the
       channel (§2.5) against "one third … in the plume" (§3.6).
     * Eq. 34 uses $h$, defined in §2.3 as the channel width, where the Hall
       parameter is meant ($\mu_0h/(1+h^2)$ matches the Hall mobility of
       §2.1).
     * "n = 1 [Eq. (1)]" in §3.4 refers to the cyclotron resonance, eq. 35.
     * "$\Omega_i\gg L$" in §2.1 compares a Hall parameter with a length; the
       ion Larmor radius is meant.
     * Eq. 1 is printed with total derivatives where partials are meant;
       §2.1 says Boeuf & Garrigues "solved Eq. (15)" where the energy
       equation (14)/(16) is meant; $\mathbf Q_e$ is called "the electron
       flux vector" but is the heat flux.
     * Modified Vaughan model: eq. 38 uses one $k$ for two parameters
       (exponent 0.62/0.25 and a smoothness factor; Tab. IV "k = 1"); Tab.
       IV has $r_i$ where eq. 39b has $r_r$.
     * Furman–Pivi eq. 40b lacks a multiplicative amplitude on the bracket,
       and eq. 40c puts $(1-\sigma_e-\sigma_r)$ in the denominator; not
       reproduced as authoritative.
     * App. 1 says Fig. 21(b) shows BN yields at 0–100 eV; the caption
       makes (b) a zoom near the crossover and (c) the Al₂O₃ components.
     * Fig. 14 caption writes $\gamma_{SCS}=0.983$, the text
       $\bar\sigma_{SCS}$.
     * Eq. 44 cites "Poisson Eq. ()" with an empty number.
     * Citation slips: Cho et al. 2013, 2015 and Tang et al. 2012 are cited
       but missing from the list; year mismatches Cheng & Martinez-Sanchez
       2007 (list 2008), Hara et al. 2015 (2014), Touzeau et al. 2001
       (2000), Giono et al. 2017 (2018), Garrigues et al. 2018 (2019 "to
       appear"); the graphite-wall result is attributed to Grimaud &
       Mazouffre 2017a but matches 2017b; spellings Jahnunen, Quing,
       Sidorenko, Ashkenazy, Tarawa for Janhunen, Qing, Sydorenko,
       Askenazy, Tawara. The Bareilles et al. (2003) entry prints the
       vol:page of Garrigues et al. 2003 and a DOI resolving to Phys.
       Plasmas 11:3035 (2004); the Hu & Wang (2015) entry prints a DOI
       resolving to Phys. Plasmas 24:033510 (2017).
     * Tab. II's "small-scale turbulence" form and the Jorns (2018) best fit
       printed in the same section are inverse ratios; not commented on.
   * **Reference list:** 199 printed entries in the manuscript; Crossref
     lists 239 for the published version (not reconciled). The printed
     entry Taccogna, Minelli, Asadi & Bogopolsky (2019), "Numerical studies
     of the ExB electron drift instability in Hall thrusters" (PSST, to
     appear) would take the key `taccogna-2019`, this source's slug; it was
     merged as `taccogna-2019-b` (PSST 28:064002), and every citation of Rev.
     Mod. Plasma Phys. 3:12 in other reference lists goes to `taccogna-2019`.
     Merge corrections recorded in the `.bib` notes: the printed Bareilles
     (2003) entry goes to `bareilles-2004` (its printed DOI resolves there);
     year misprints were re-keyed only where Crossref proves the true year.

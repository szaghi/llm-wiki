---
type: Source
title: "Charoy et al. (2020) — A comparison between kinetic theory and particle-in-cell simulations of anomalous electron transport in E × B plasma discharges"
description: "Uses 2D axial–azimuthal PIC-MCC (LPPic) runs of the 2019 Hall-thruster benchmark and nine variants to show that the instability-enhanced electron–ion friction force drives axial electron transport without wall or neutral collisions, and that a simplified quasi-linear closure fed with PIC velocity distributions and wave energies reproduces it while Maxwellian, ion-trapping-saturation and Bohm/wall models do not."
resource: "doi:10.1063/5.0003978"
source_kind: paper
authors: [Charoy T., Lafleur T., Tavant A., Chabert P., Bourdon A.]
year: 2020
venue: "Phys. Plasmas 27:063510"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2020_Crossref_Physics_of_Plasmas_Charoy_A_comparison_between_kinetic_theory_and_particle-in-cell_sim.pdf"
tags: [pic, mcc, kinetic, hall-thruster, anomalous-transport, instability, benchmark]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper tests the quasi-linear kinetic model of the instability-enhanced
electron–ion friction force (Lafleur et al. 2018) against 2D
axial–azimuthal PIC-MCC simulations with the code LPPic, in the
configuration of the Charoy et al. (2019) benchmark and nine variants
(peak radial field 50–200 G, discharge current density 50–400 A m⁻², with
and without ion– and electron–neutral collisions). A term-by-term
evaluation of the azimuthal electron momentum equation shows that the
azimuthal electron–ion friction force is the main contributor to axial
electron transport, without wall or neutral collisions. The model is
re-derived with further simplification to a closed form which, evaluated
with the PIC velocity distributions and wave energies, reproduces the PIC
friction force in all cases; a Bohm/wall empirical model, the
ion-trapping saturation model and a Maxwellian closure do not. Momentum
conservation between electron–ion and ion–electron friction is verified
directly in the PIC, and ion–neutral backscattering is found to enhance
the friction. Because the force depends sensitively on the strongly
non-Maxwellian electron distribution, the authors conclude that a
self-consistent fluid closure for anomalous transport remains out of
reach.

# Key claims

1. **Friction dominates transport** (§III A, Figs. 5a, 6). In the
   azimuthal electron momentum balance, the instability-enhanced friction
   $\mathbf R_{ei}$ is the main contributor to axial transport in all seven
   collisionless cases, "even in the absence of electron-wall or
   electron-neutral collisions". Shown.
2. **Classical friction is negligible** (§III A, Eq. 6). The
   Lenard–Balescu Coulomb friction is smaller than the instability-enhanced
   force by "of the order of a factor of 500". Shown.
3. **Axial balance** (§III A, Fig. 5b). Only the pressure (diamagnetic) and
   electric terms drive the azimuthal drift, pressure dominant near the
   anode and electric near the exit plane. Shown.
4. **Dependence on current density and field** (§III B, Fig. 6). Lower
   current density (hence plasma density) lowers friction and transport
   ("when the current density is divided by 2, the electron-ion friction
   force is also divided by 2"); friction seems to increase with the field,
   with a distinct plume peak at 50 G. Shown.
5. **Quasi-linear closure** (§IV A, Eqs. 12–24). From a single-mode,
   electrostatic, unmagnetized-electron linear response, with the wavenumber
   of maximum growth of the simplified ion-acoustic dispersion relation,
   $k_\theta\lambda_D=1/\sqrt2$ (Eqs. 18–19, attributed), and a phase speed
   $\sim c_s$ much smaller than the electron thermal speed, the friction
   reduces to $2\sqrt2\pi\,\omega_{pe}^2\lambda_D$ times the wave energy
   density times the slope at zero velocity of the normalized azimuthal
   reduced electron distribution (Eq. 24). Derived. No full
   cyclotron-resonant ECDI dispersion relation is written; nonlinear
   smearing of the cyclotron resonances (Lampe et al. 1972) is invoked to
   leave an unmagnetized ion-acoustic instability.
6. **Maxwellian closure** (§IV A, Eqs. 25–27; §IV B, Fig. 7). For a
   drifting Maxwellian the formula has a similar shape to the PIC force but
   overestimates it by a factor of about 3 and changes sign between
   $x=1.25$ and 1.75 cm. Shown.
7. **Other models fail** (§IV B, Fig. 7). The ion-trapping saturation
   model (Eq. 10) behaves differently near the exit; the empirical model
   (Eq. 9) with best-fit wall coefficient 0.4 (times $10^7$ s⁻¹) inside and
   $\alpha_{\mathrm B}=0.17$ outside matches for $x<1$ cm but goes to zero
   in the plume and is not predictive. Shown.
8. **Non-Maxwellian distributions** (§IV B, Fig. 8). PIC electron
   distributions (azimuthally averaged, time-averaged over 5000 steps) are
   strongly non-Maxwellian in the axial and azimuthal velocities,
   especially near the anode. Shown.
9. **Wave energy below trapping saturation** (§IV B, Eqs. 28–29, Fig. 9).
   Ion-wave trapping implies a wave-to-thermal energy ratio of at most
   1/432; except at 50 G the PIC ratio is below it, which explains why the
   saturation model overestimates the force. Quasi-linear validity
   (potential fluctuation small compared with $T_e$) holds everywhere.
   Shown.
10. **Fluctuation level** (§IV B, p. 23). Density fluctuations are about
    10% inside the thruster, a few percent just downstream of the exit
    (close to the ~1% measured by Tsikata et al. 2009) and about 10%
    further downstream, against 15–20% in other (non-axial) PIC
    simulations. Shown and compared.
11. **Closure reproduces PIC** (§IV C, Fig. 10). With local PIC
    distributions and wave energies, Eq. 24 agrees "very well" with the PIC
    friction in all seven cases, over 0.5–20 N m⁻³. Shown; the inputs come
    from the PIC, so this tests the closure physics, not a predictive model.
12. **Momentum conservation** (§IV D, Fig. 11). The friction computed from
    electron density–field and ion density–field correlations satisfies
    $\mathbf R_{ie}=-\mathbf R_{ei}$ in all cases. Shown.
13. **Collisions** (§V, Fig. 12). Eq. 24 still holds; all collisions
    together enhance the friction by "almost a factor 2"; ion–neutral
    isotropic scattering has no significant effect; backscattering (charge
    exchange) enhances it (hypothesis: modified ion distribution, reduced
    Landau damping); electron–neutral drag is negligible against
    $\mathbf R_{ei}$; the electron–neutral enhancement mechanism "remains
    unclear". Shown.
14. **Wavelength trends** (§II B, Figs. 3–4). At 100 G a sharp change from
    short wavelengths near the anode to long wavelengths in the plume;
    higher field extends long wavelengths to the anode, 50 G extends short
    ones into the plume; lower current density gives longer wavelengths, as
    "expected" from $k_\theta\lambda_D=1/\sqrt2$. Qualitative; no growth
    rates, frequencies or wavelengths are measured.

# Models and numerics

* LPPic: explicit electrostatic 2D-3V PIC-MCC; electrons and Xe⁺ as
  macroparticles; neutral Xe (§V only) as an imposed background from a 1D
  Euler solution (Eq. 30; 1.5 mg/s, channel radii 2 and 4 cm). Verified in
  the 2019 benchmark against six other codes.
* Domain $L_x=2.5$ cm axial × $L_y=1.28$ cm azimuthal, periodic in $y$;
  anode at $x=0$ (200 V), cathode/emission plane near the right boundary
  (0 V); peak radial field at 0.75 cm. No walls, no SEE.
* Cathode: electrons injected uniformly in $y$ at the emission plane, 1 mm
  from the right boundary, to balance current; potential rescaled to zero
  there.
* Ionization: imposed cosine-shaped source (also in §V); no breathing mode.
* Collisions (§V): MCC after Vahedi & Surendra; e–Xe elastic and four
  excitations (8.315, 9.447, 9.917, 11.7 eV), Xe⁺–Xe isotropic and
  backscattering, LXCat (Phelps) cross sections; no ionization energy loss.
* $\Delta t\le0.2/\omega_{pe}$, $\Delta x\le\lambda_D$; at $n\approx5\times10^{17}$
  m⁻³ and $T_e\approx50$ eV this gives $\Delta t\approx5\times10^{-12}$ s and
  $\Delta x\approx5\times10^{-5}$ m. 75 initial particles per cell at
  $5\times10^{16}$ m⁻³, about 250 at steady state (converged per the 2019
  paper). No artificial scaling. Weight, cell counts and run time not
  stated. Snapshots at 15 µs.
* No anomalous-transport model in the PIC. Models compared: Bohm
  $\nu_{\mathrm{ano}}=\alpha_{\mathrm B}\omega_{ce}/16$ (Eq. 7), wall
  collisions (Eq. 8, Hagelaar et al.), their force form (Eq. 9),
  ion-trapping saturation (Eq. 10), quasi-linear (Eq. 24), Maxwellian
  (Eq. 27).

# Tests and results

| Case | Peak field [G] | Current density [A m⁻²] | Collisions |
|---|---|---|---|
| 0 (benchmark) | 100 | 400 | none |
| 1, 2, 3 | 50, 150, 200 | 400 | none |
| 4, 5, 6 | 100 | 50, 100, 200 | none |
| 7 | 100 | 400 | backscattering only |
| 8 | 100 | 400 | isotropic scattering only |
| 9 | 100 | 400 | all |

* Nominal friction peaks at about 11 N m⁻³ at the field maximum (read from
  Fig. 5a); axial force terms of order 10³ N m⁻³ (Fig. 5b).
* Friction magnitudes 0.5–20 N m⁻³ across cases; Eq. 24 agrees in all
  (Fig. 10); all-collision case about twice the nominal (Fig. 12).
* Wave-to-thermal energy ratio between about $10^{-3}$% and $10^{-1}$%
  (Fig. 9 axis), limit 1/432 ≈ 0.23%.

# Notation map

| Charoy et al. (2020) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$ (axial), $y$ (azimuthal) | $x$, $y$ with $x\leftrightarrow z$, $y\leftrightarrow\theta$ | Eq. 30 slips to $z$ |
| $q$, $e$ | $q_e=-e$, $e$ | |
| $m$, $M$ | $m_e$, $m_i$ | |
| $n_g$ | $n_n$ | |
| $\mathbf v_e$, $v_{e,x}$, $v_{e,y}$ | $\mathbf u_e$ | **collision:** the paper's $\mathbf v_e$ is the mean velocity; registry $\mathbf v$ is the phase-space velocity |
| $\mathbf w$ (§III), $\mathbf v$ (§IV) | $\mathbf v$ | |
| $\mathbf v_{de}$, $\mathbf v_{di}$ | words (azimuthal drift speeds) | |
| $\Pi_e$ | $\mathsf P_e$ | |
| $f_e$, $f_{e0}$, $F_{e0}(v_y)$ | $f_e$; words | equilibrium and reduced distributions |
| $\mathbf R_{ei}$, $\mathbf R_{ie}$, $\mathbf R_{en}$ | $\mathbf R_{ei}$, $\mathbf R_{ie}$, $\mathbf R_{en}$ | force-term label $F_{ei}=-R_{ei}$ in Eqs. 1–2 |
| $\mathbf k$, $k_y$, $\omega_R$, $\gamma$ | $\mathbf k$, $k_\theta$, $\omega_r$, $\omega_i$ | **collision:** registry $\gamma$ is the polytropic index |
| $\zeta=\omega/k_y$ | words (phase velocity) | |
| $\varepsilon_{wave}$, $\varepsilon_{th}$ | words | **collision risk** with $\varepsilon_0$ and excitation energies |
| $\omega_p$, $\omega_{pe}$ | $\omega_{pe}$ | |
| $\lambda_d$, $\lambda_{De}$ | $\lambda_D$ | |
| $c_s=\sqrt{eT_e/M}$ | $c_s$ | $T_e$ in eV |
| $v_{Te}=\sqrt{2eT_e/m}$ | $v_{th,e}$ | with the $\sqrt2$ |
| $\nu_{bohm}=\frac{K}{16}\omega_{ce}$ | $\nu_{\mathrm{ano}}=\alpha_{\mathrm B}\omega_{ce}/16$ | same convention, $\alpha_{\mathrm B}=K$ |
| $\alpha$, $\nu_{ref}$ (wall model) | words | best fit $\alpha=0.4$; $\nu_{ref}=10^7$ s⁻¹ |
| $\sigma_m$ | $\sigma_{en}$ | |
| $J$ | words (discharge current density) | |
| $u_g$/$v_g$, $p_g$, $E_g$ | $\mathbf u_n$, $p_n$, words | **collision:** $E_g$ (total energy) vs $\mathbf E$ |

# Pages created or updated

Chunk 1 (2026-10-14) created every page of the bundle. This source is cited on:

* [Anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md)
* [Axial–azimuthal Hall-thruster PIC benchmark (Charoy et al. 2019)](/benchmarks/axial-azimuthal-pic-benchmark.md)
* [Breathing mode](/definitions/breathing-mode.md)
* [Electron drift instability (ECDI)](/definitions/electron-drift-instability.md)
* [Instability-enhanced electron–ion friction and effective mobility](/results/instability-enhanced-friction-force.md)
* [Monte Carlo collisions and the null-collision method](/methods/monte-carlo-collisions.md)
* [Near-wall conductivity](/definitions/near-wall-conductivity.md)
* [Particle-in-cell with Monte Carlo collisions (PIC-MCC)](/methods/pic-mcc.md)
* [Permittivity, ion-mass and geometric scaling in PIC](/methods/pic-acceleration-scaling.md)
* [Resolution constraints of explicit PIC](/definitions/explicit-pic-resolution-constraints.md)
* [SPT-100 as a validation case](/benchmarks/spt-100.md)

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2020_Crossref_Physics_of_Plasmas_Charoy_A_comparison_between_kinetic_theory_and_particle-in-cell_sim.pdf`.
   * **Version.** HAL accepted manuscript (hal-02877468v1, deposited 22
     June 2020), AIP preprint template dated 14 May 2020, 36 PDF pages (HAL
     cover + 35 manuscript pages); not the typeset version of record. Page
     numbers above are manuscript pages.
   * **Identity.** doi:10.1063/5.0003978, printed on the HAL cover and
     checked on Crossref: Phys. Plasmas 27(6), article 063510; issue
     2020-06-01, online 2020-06-04.
   * **How it was read.** Full text; all equations read from rendered pages
     (PDF pp. 6, 11–13, 17–21, 23, 29), none illegible; plot values are the
     reader's approximate readings. The exact magnetic-field and ionization
     profiles are deferred to the 2019 paper.
   * **Recorded as printed.**
     * The Fig. 7 legend labels the Maxwellian curve "Eq. 26"; the text says
       Eq. 27 is plotted.
     * Eq. 9 defines $R_{an,empirical}$; text and legend use
       $R_{ei,empirical}$.
     * "Divided by 2" (p. 14): peak friction read from Fig. 10 gives ratios
       of about 2.6, 2.1 and 5 per doubling of current density, not a clean
       factor 2 (plot reading, soft flag).
     * Fig. 9 description (p. 22) reads as both below and reaching the
       saturation limit.
     * Fig. 12d: electron–neutral drag reaches about 3 N m⁻³ near
       $x\approx0.3$ cm, comparable to $\mathbf R_{ei}$ there, although
       called "negligible" (p. 29).
     * The text places the cathode at $x=2.4$ cm with the emission plane
       1 mm from the right boundary; Fig. 1 labels 2.4 cm as the emission
       plane and the boundary at 2.5 cm.
     * Eq. 30 mixes $v_g$ and $u_g$ and uses $z$ for $x$.
     * The emitted-electron count, $\Delta t\times(I_{a,e}-I_{a,i})$, lacks
       the division by $e$ and by the macroparticle weight.
     * Eq. 15 uses $\langle|\delta\mathbf E|\rangle_{rms}$, Eq. 16 defines
       $\langle\delta E\rangle_{rms}$.
   * **Reference list.** 65 printed entries. Three Vienna 2019 IEPC papers
     (refs. 57, 60, 65) are printed as the "29th" IEPC (it was the 36th).
     In the bibliography this source is `charoy-2020`; Charoy's 2020 PhD
     thesis, which reza-2022 cites, is the separate entry `charoy-2020-b`.


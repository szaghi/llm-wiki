---
type: Source
title: "Takahashi (2019) — Helicon-type radiofrequency plasma thrusters and magnetic plasma nozzles"
description: "Single-author review of electrodeless rf magnetic-nozzle thrusters centred on the thrust decomposition F = F_s + F_B + F_w (source electron pressure, diamagnetic Lorentz force on the nozzle, wall momentum loss) and its direct measurement, with current-free double layers, neutral depletion, electron polytropic behaviour, plasma detachment and a table of 18 thrust measurements; simulations appear only as citations."
resource: "doi:10.1007/s41614-019-0024-2"
source_kind: paper
authors: [Takahashi K.]
year: 2019
venue: "Rev. Mod. Plasma Phys. 3:3"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2019_Crossref_Reviews_of_Modern_Plasma_Physics_Takahashi_Helicon-type_radiofrequency_plasma_thrusters_and_magnetic_pl.pdf"
tags: [helicon, magnetic-nozzle, review, plume]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

A review of electrodeless radiofrequency thrusters with
[magnetic nozzles](/definitions/magnetic-nozzle.md), mostly
[helicon thrusters](/definitions/helicon-plasma-thruster.md), with VASIMR,
ICP and ECR thrusters covered briefly. It centres on how thrust arises, as
shown by direct thrust and momentum-flux measurements combined with plasma
diagnostics. Its model (§4) splits the thrust into the source
electron-pressure force on the back wall, the Lorentz force of the
azimuthal electron-diamagnetic current with the radial nozzle field, and
the axial momentum lost to the radial wall; the measurements of each are
reviewed (§5.5). It also covers the
[current-free double layer](/definitions/current-free-double-layer.md),
neutral depletion, electron thermodynamics, detachment, 18 performance
results (§6) and engineering topics. The review runs no simulation;
numerical work (PIC, PIC/DSMC, 2D fluid, wave–plasma models) appears only
through citations, without numerical parameters. Merged into
[thrust decomposition of a magnetic nozzle](/results/magnetic-nozzle-thrust-decomposition.md).

# Key claims

1. **Performance figures** (§1, Eqs. 1–2): $I_{sp}=F/(\dot mg_0)$,
   $\eta=F^2/(2\dot mP)$, with $P$ the rf power. Thrust is the exhausted
   momentum flux, static plus dynamic pressure. Rf thrusters are
   current-free and need no neutralizer.
2. **Wave physics** (§2, Eqs. 3–6, Fig. 3): helicon and ECR waves are
   whistler (R) modes; the helicon has no strict resonance. Helicon sources
   reach $10^{12}$–$10^{13}$ cm$^{-3}$ at a few mTorr with $T_e\gg T_i$.
   VASIMR exceeded about 50% efficiency at about 200 kW (attributed).
3. **Thrust model** (§4, Eqs. 8–23): from a steady axisymmetric two-fluid
   balance with cold ions, inertialess electrons and quasi-neutrality,
   neglecting radial ion inertia (kept by Ahedo & Merino 2010):
   $T=T_s+T_B+T_w$ (registry $F=F_s+F_B+F_w$); the 1D reduction of
   Fruchtman et al. (2012) differs from the 2D integral by 15–25%.
4. **Prior models** (§4; attributed): Ahedo & Merino (2010) conclude that
   the main nozzle force comes from the electron Hall current; Fruchtman
   (2006) shows that spontaneous electric fields impart no net momentum;
   models of the wave and the plasma flow "have not been compared with the
   experiments yet".
5. **CFDL** (§5.2–5.4, Figs. 7–10, Eq. 24): formation threshold set by the
   ion Larmor radius against the tube radius; depleted-tail electron
   distributions instead of beam electrons; potential drop
   $\frac12[1+\ln(m_i/2\pi m_e)]T_e/e\approx5.18\,T_e/e$ in argon (the
   reader checked 5.18 numerically).
6. **Thrust measurements** (§5.5, Figs. 12–16): $F_s$ dominates the first
   measurements; $F_B$ measured alone and computed from measured pressure
   profiles agree within 20–30%; all three components measured separately
   in HPT-I; negative $F_w$ in Kr and Xe with neutral depletion; the
   measured azimuthal current is dominated by the diamagnetic term.
7. **Neutrals** (§5.6, Fig. 17): about 80% depletion near the exit; exit gas
   injection +25–40% in thrust and density; PIC coupled with DSMC (Takase
   et al. 2018) qualitatively consistent; CEX conserves momentum and raises
   the momentum gain when its mean free path is shorter than the
   potential-drop scale.
8. **Electron thermodynamics** (§5.7, Eqs. 27–30, Figs. 18–19): measured
   $\gamma\sim1$–1.2 and $\sim1.17$; trapped electrons isothermal, free
   electrons nearly adiabatic ($\gamma\to5/3$); effective $\gamma$ open.
9. **Detachment** (§5.8, Eqs. 31–36, Figs. 20–21): ion, electron and MHD
   mechanisms; observed field-line stretching at $M_A\sim0.2$–0.25 against
   0.3–0.4 from the review's dimensional analysis and $M_A>1$ in Arefiev &
   Breizman (2005); "still in argument".
10. **Performance table** (§6, Table 1, Figs. 22–23): 18 results, 0.07–6 kW,
    0.85–67 mN, efficiency 0.25–17.8%; best 67 mN at 6 kW, $I_{sp}=3256$ s,
    17.8% (private communication). The reader recomputed all 18 rows from
    Eqs. 1–2; they are internally consistent.
11. **Engineering** (§6.2–6.4): permanent-magnet nozzles of about 120–500 G;
    rf amplifiers (class AB, 75% at $40\pm3$ MHz, VSWR minimized within about
    10 ms); a bidirectional thruster with zero net force for debris
    removal.

# Models and numerics

* Analytic: cold-plasma dispersion (Eqs. 3–6), Bohm ion saturation current
  (Eq. 7), two-fluid momentum balance and thrust integrals (Eqs. 10–23)
  evaluated with **measured** electron-pressure profiles and $F_w=0$,
  CFDL potential (Eq. 24), polytropic law (Eqs. 27–30), Hooper drift
  (Eq. 31), ideal-MHD dimensional analysis (Eqs. 32–36).
* Cited numerical work, none performed here: 1D PIC of CFDL formation
  (Meige et al. 2005) and electron distributions (Meige & Boswell 2006); 2D
  PIC of the CFDL (Rao & Singh 2012); PIC of a nozzle-surface instability
  (Singh et al. 2013); PIC of probe sheaths (Sheridan 2000); PIC with
  depleted neutrals (Takao & Takahashi 2015); PIC/DSMC (Takase et al.
  2018); 2D fluid models (Ahedo & Merino 2010, 2011; Ahedo &
  Navarro-Cavallé 2013; Merino & Ahedo 2014, 2016); a global model (Lafleur
  2014); 2D wave–plasma modelling (Tian et al. 2018). Field solvers,
  collision models, grids, steps, weights, codes and run times are not
  stated for any of them.

# Tests and results

Experiments reviewed, mostly the author's: Figs. 6c, 7–21 and Table 1, as
in Key claims 5–10, and on the concept pages listed below.

# Notation map

| Takahashi (2019) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $F$, $T$, $T_{total}$ | $F$ | **collision**: $T$ is a temperature in the registry |
| $T_s$, $T_B$, $T_w$ | $F_s$, $F_B$, $F_w$ | **collision**: registry $T_s$ is a species temperature |
| $\tau$ | words (axial momentum flux density) | |
| $g$ | $g_0$ | |
| $P$, $P_{rf}$ | $P$ | rf generator power |
| $\eta$, $\eta_{rf}$ | $\eta$ | with $P$ the rf power |
| $n_p$ | $n_e\approx n_i$ | quasi-neutral density |
| $(u_r,u_\theta,u_z)$ | components of $\mathbf u_i$ | |
| $(v_r,v_\theta,v_z)$ | components of $\mathbf u_e$ | **collision**: registry $\mathbf v$ is the phase-space velocity |
| $u_B$, $C_s$ | $c_s$ | |
| $T_e$, $T_{eff}$ | $T_e$; words for the effective temperature | the paper writes $k_BT_e$ |
| $\omega_{pj}$, $\omega_{cj}$ | $\omega_{pe}$, $\omega_{ce}$ (and ion analogues) | |
| $\gamma$ (Eq. 27) | $\gamma$ | **collision inside the paper**: $\gamma\equiv k_\parallel^2-\kappa_1$ in Eq. 4 |
| $\mu$ | $\mu_0$ | **collision**: registry $\mu_\perp$ is a mobility |
| $V_A$ | words (Alfvén speed) | **collision inside the paper**: $V_A$ is also the source bias voltage (Figs. 18–19) |
| $M_A$ | $M_A$ | |
| $J_\theta$, $j_\theta$ | $j_\theta$ | |
| $\phi_{DL}$, $\Delta V$ | words (double-layer potential drop) | |
| $I_B$ | words (solenoid current) | **collision** with $I_b$ |
| $\rho$ (Eq. 32) | words (mass density) | not $\rho_c$ |

# Pages created or updated

Chunk 1 (2026-10-14) created every page of the bundle. This source is cited on:

* [Breathing mode](/definitions/breathing-mode.md)
* [Charge-exchange ions](/definitions/charge-exchange-ions.md)
* [Current-free double layer](/definitions/current-free-double-layer.md)
* [Direct simulation Monte Carlo (DSMC)](/methods/dsmc.md)
* [Helicon plasma thruster](/definitions/helicon-plasma-thruster.md)
* [Magnetic nozzle](/definitions/magnetic-nozzle.md)
* [Polytropic electron closure and plume cooling](/definitions/polytropic-electron-closure.md)
* [Thrust decomposition of a magnetic nozzle](/results/magnetic-nozzle-thrust-decomposition.md)

# Citations

1. `~/papers/mosaic/plasma-propulsion-simulation/2019_Crossref_Reviews_of_Modern_Plasma_Physics_Takahashi_Helicon-type_radiofrequency_plasma_thrusters_and_magnetic_pl.pdf`.
   * **Version.** Publisher's version of record (Springer, © The Author(s)
     2019, CC BY 4.0), 61 pages.
   * **Identity.** doi:10.1007/s41614-019-0024-2, checked on Crossref (title,
     author): Rev. Mod. Plasma Phys. 3(1), article 3, issue 2019-12; online
     2019-05-22. Received 6 Jan 2019, accepted 28 Apr 2019.
   * **How it was read.** Full text layer; pages 6, 13, 15, 39 and 43 checked
     visually for Eqs. 3–6, 11–23, 31 and 35–36. Eq. 3 is garbled in the text
     layer and was read on the rendered page. Values given as "about" were
     read from figures. Many in-text "Takahashi et al. YYYY" citations are
     ambiguous because the list holds several works per year (2008–2018);
     they were attributed by content, e.g. the §5.6 exit-injection result
     most likely to APL 109:194101.
   * **Recorded as printed.**
     - Fig. 22's axis is labelled "Prf (W)" but runs 0–6, i.e. kW.
     - In-text "Plihon et al. 2017" is 2007 in the reference list.
     - $V_A$ is both the Alfvén speed (Eqs. 35–36) and the bias voltage
       (Figs. 18–19); $\gamma$ is both $k_\parallel^2-\kappa_1$ (Eq. 4) and the
       polytropic index (Eq. 27).
     - §5.5.1 "a few mN … for several hundreds of W" against §6 "only a few mN
       for about 1 kW" for the same 2011 experiments (Table 1: 0.9 and
       0.65 kW); wording, not a numerical conflict.
     - Eq. 18 prints only $\int_{r_s}$; integration from 0 to the source
       radius is implied.
     - The measured MHD-stretching threshold ($M_A\sim0.2$–0.25) and the
       Eq. 36 estimate (0.3–0.4) differ; the review calls the agreement
       "qualitative".
   * **Reference list:** 236 printed entries (Crossref reference-count 236);
     six entries print no title (Charles et al. 2008, IEEE TPS 36:1196;
     Cohen et al. 2006; Longmier et al. 2011, PSST; Tonooka et al. 2015;
     Ziemba et al. 2006; Takahashi & Ando 2018, private communication).
     Printed a/b suffixes are recorded in the fragment's `note` fields.

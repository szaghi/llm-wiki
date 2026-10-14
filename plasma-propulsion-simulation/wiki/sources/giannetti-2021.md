---
type: Source
title: "Giannetti et al. (2021) — Numerical and experimental investigation of longitudinal oscillations in Hall thrusters"
description: "Calibrates three physical parameters of a 1D quasi-neutral fluid Hall-thruster model (neutral speed, wall-loss scaling, two-level Bohm coefficient) by hand on the breathing-mode discharge current of the 5 kW-class HT5k, reproducing its mean, extremes, RMS and 25 kHz frequency, then validates it against fast-diving triple-probe profiles, which it matches only in order of magnitude and trend."
resource: "doi:10.3390/aerospace8060148"
source_kind: paper
authors: [Giannetti V., Saravia M.M., Leporini L., Camarri S., Andreussi T.]
year: 2021
venue: "Aerospace 8:148"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2021_Crossref_Aerospace_Giannetti_Numerical_and_Experimental_Investigation_of_Longitudinal_Osc.pdf"
tags: [hall-thruster, fluid, oscillation, anomalous-transport, calibration, sheath, wall-interaction]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper couples an unsteady, quasi-neutral, fully fluid 1D axial model
of a Hall-thruster discharge (neutrals, singly charged ions,
drift-diffusion electrons with an internal-energy equation) with
measurements on SITAEL's HT5k DM2 (5 kW class) in its chamfered
"end-of-life" M1 configuration at 300 V and 8.4 mg/s xenon. Three
physically motivated parameters are calibrated by hand on the
discharge-current signal alone: the constant neutral speed, a coefficient
that scales every plasma–wall term, and a two-level Bohm coefficient. The
calibrated model reproduces the [breathing-mode](/definitions/breathing-mode.md)
current and is then validated, without retuning, against time-resolved
near-plume density, potential and $T_e$ from a fast-diving triple
Langmuir probe with Bayesian reconstruction. It captures orders of
magnitude and trends but not local values. The authors present the model
as an "extrapolator" of partial data rather than a predictive tool.

# Key claims

1. **Calibrated current** (shown; §4, Fig. 5, Table 2). Measured against
   simulated: mean $I_d$ 8.65 / 8.67 A; maximum 13.9–17.3 / 16.4 A;
   minimum 3.3–5 / 4.5 A; RMS 4.1 / 3.9 A; $f_{\mathrm{BM}}$ 25.4 /
   25.3 kHz. Both spectra share the fundamental and a second harmonic near
   50 kHz; the simulation adds a sharp peak near 100 kHz.
2. **Best-fit parameters** (§4, p. 14): neutral speed 395 m/s, wall
   coefficient 0.115, Bohm coefficient 0.075 in the channel and 7.5 in the
   plume (ratio 100), joined by a smooth transition of tunable steepness
   (§2.5). The paper's $\nu_a=\beta\,eB_r/(16m_e)$ (eq. 11) gives
   $\alpha_{\mathrm B}=\beta$ directly.
3. **Calibrated anomalous frequency** (Fig. 6, values read off a log
   plot): about $1.5\times10^6$ Hz at the anode, about $10^7$ Hz near
   $0.8L_{\mathrm{ch}}$, about $6\times10^7$ Hz at the exit, peaking at
   about $1.5\times10^9$ Hz near $1.5L_{\mathrm{ch}}$. The authors state the
   profile is close to profiles other authors calibrated on experiments
   (stated, not shown).
4. **Sensitivities** (shown qualitatively; §4, pp. 14–15): the neutral
   speed directly controls $f_{\mathrm{BM}}$ (faster neutrals, more
   frequent surges), consistent with an ionization-instability picture;
   395 m/s is "relatively high" against the 100–300 m/s the authors infer
   from Reid. The wall coefficient mainly controls the amplitude; its
   strong reduction is attributed to unresolved radial gradients, fluid
   sheath models that overestimate wall losses (Sydorenko et al. 2006;
   Kaganovich et al. 2007) and the chamfered channel shielding the walls
   magnetically. The in-channel Bohm coefficient strongly affects mean
   current and amplitude, consistent with Hara et al.; the steepness of the
   transition also matters.
5. **Mechanism** (shown in simulation; §4, Figs. 7–8): neutral advection
   into the hot region, a density surge, near-anode phase opposition of
   plasma and neutral densities, plasma pushed both downstream and
   upstream through a weak reversed field near the anode, and refuelling
   by recombined ion backflow. All quantities oscillate at one frequency
   over the whole domain, read as a "global self-sustained instability".
6. **Validation against the probe** (shown; §4, Fig. 9): orders of
   magnitude, trends and the breathing motion of the acceleration region
   are reproduced. The model underestimates near-plume density (mean and
   amplitude), puts the density peak inside the channel, overestimates
   peak $T_e$ (about 29 eV against about 18 eV, read off the figure; the
   measured peak lies in the probe-perturbed region) and places the
   acceleration region too far upstream. Suggested causes: neutral
   back-ingestion, section-averaged against centreline values, the
   unmodelled plume expansion, the calibration choices and the 1D
   treatment of an end-of-life magnetic topology.
7. **Numerical stabilization** (stated, attributed to Hara 2018; §2.4,
   eqs. 17–18): eliminating $\partial_z\phi$ from the ion momentum
   equation through Ohm's law gives the ion system the acoustic speed
   $\sqrt{(T_i+T_e)/m_i}$.
8. **Discharge current** (eqs. 19–22): an integral of Ohm's law over the
   domain, with an anode-sheath drop added to $V_d$ (checked at
   ingestion: eq. 19 follows from eqs. 7, 12 and 22 with consistent signs).
9. **Outlook** (stated; §§4–5): the Bohm coefficient should depend on $z$
   and $t$; Dale & Jorns measured it varying strongly over the breathing
   cycle.
10. **Cost** (§2.4): about 1310 s per 1 ms simulated on an i7-8750H
    (6 cores, 16 GB); code "not optimized".

# Models and numerics

See [one-dimensional fluid model](/methods/one-dimensional-fluid-hall-model.md).
Neutrals: continuity at constant speed, ionization rate from LXCat
(Biagi) cross sections processed by BOLSIG+ for a Maxwellian EEDF.
Ions: continuity and momentum, unmagnetized, collisionless, $T_i=0$; no
charge exchange, no plume expansion. Electrons: drift-diffusion in $z$
and $\theta$ with purely radial $\mathbf B$, total frequency
$\nu_e=\nu_{en}+\nu_w+\nu_{\mathrm{ano}}$, internal-energy equation after
Hara et al. Wall model (App. A): Hobbs–Wesson sheath with cold ions and
SEE, inside the channel only, every term scaled by the wall coefficient;
BN-SiO$_2$ yield after Goebel & Katz capped at 0.983 (xenon
space-charge saturation); secondaries thermalize. Domain: anode to a
virtual cathode line at $2L_{\mathrm{ch}}$; $T_e=2$ eV at the cathode line;
characteristic ion boundary conditions with ions entering the anode
sheath edge at or above the acoustic speed. Discretization: finite
volume, first-order Lie splitting into five sub-steps; upwind neutrals,
Steger–Warming ions, implicit second-order electron energy, explicit
Euler otherwise. Not printed: $L_{\mathrm{ch}}$, channel radii, $B_r(z)$,
the transition function, $\Delta t$, cell count, code name and language.
Serial PC run, no MPI or GPU.

Experiment (§3): SITAEL IV4 facility (2 m × 4.2 m, 70,000 L/s xenon,
below $10^{-4}$ mbar in operation); HC20 cathode; current probe sampled at
5 MHz. Triple probe: W–25 %Re electrodes, arm radius 350 mm, 200 ms
stroke, data from 15 mm upstream to 70 mm downstream of the exit plane,
only $z>L_{\mathrm{ch}}+2$ mm counted as unperturbed; reconstruction by
nested-sampling Bayesian inference on Laframboise probe theory.

# Tests and results

Calibration (Key claim 1), space–time fields over 0.2 ms (Figs. 7–8), and
the probe comparison (Fig. 9, Key claim 6). Simulated $\phi$ is about
310–320 V near the anode and falls mostly around $z\approx L_{\mathrm{ch}}$;
measured $\phi$ is plasma-to-ground and simulated $\phi$ is relative to
the cathode, so the comparison holds only if the cathode reference
potential is neglected (read off Fig. 9, approximate). No convergence
study.

# Notation map

| Giannetti et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $z$ | $z$ | |
| $n$, $n_e$, $n_i$, $n_n$ | $n_e=n_i$, $n_n$ | |
| $u_n$, $u_i$, $u_e$ | axial components of $\mathbf u_n$, $\mathbf u_i$, $\mathbf u_e$ | |
| $k_BT_e$, $k_BT_i$ ($T$ in K) | $T_e$, $T_i$ (energy units) | |
| $\Phi$ | $\phi$ | **collision:** the paper's lowercase $\phi_a$, $\phi_w$ are sheath drops |
| $\phi_a$, $\phi_w$ | $\Delta\phi_{\mathrm{sh}}$ (anode, wall) | |
| $\omega_e$ | $\omega_{ce}$ | **collision** risk with $\omega_{pe}$ |
| $\nu_e$, $\nu_c$, $\nu_{ew}$, $\nu_a$ | $\nu_e$, $\nu_{en}$, $\nu_w$, $\nu_{\mathrm{ano}}$ | $\nu_c$ lumps elastic, ionization and excitation |
| $\beta$ | $\alpha_{\mathrm B}$ | $\nu_a=\beta\,\omega_{ce}/16$, so $\alpha_{\mathrm B}=\beta$ |
| $\alpha$ | words (wall-interaction scaling coefficient) | **collision** with $\alpha_{\mathrm B}$ |
| $\mu$, $\mu_0$ | $\mu_\perp$, $\mu_\parallel$ | **collision:** registry $\mu_0$ is the vacuum permeability |
| $\Omega$ | $\Omega_e$ | |
| $J$, $I$ | $j_z$, $I_d$ | |
| $k_I$ | $k_{\mathrm{ion}}$ | |
| $K$, $W$ | words (collisional energy-loss coefficient, wall power loss) | **collision:** registry $W$ is the macroparticle weight |
| $\sigma$ | $\delta_{\mathrm{SEE}}$ | **collision:** registry $\sigma_{sk}$ is a cross section |
| $c_i$ | $\sqrt{(T_i+T_e)/m_i}$, $=c_s$ for $T_i=0$ | |
| $f_{BM}$ | $f_{\mathrm{BM}}$ | |
| $\varepsilon$ | words (mean electron energy) | close to $\varepsilon_0$ |

# Pages created or updated

Chunk 1 (2026-10-14) created every page of the bundle. This source is cited on:

* [Anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md)
* [Bayesian calibration of thruster models](/methods/bayesian-calibration.md)
* [Breathing mode](/definitions/breathing-mode.md)
* [Cross-field electron mobility and the Hall parameter](/definitions/electron-mobility-and-hall-parameter.md)
* [Electron fluid models (drift-diffusion)](/methods/electron-fluid-model.md)
* [Magnetic shielding](/definitions/magnetic-shielding.md)
* [Near-wall conductivity](/definitions/near-wall-conductivity.md)
* [One-dimensional fluid model of the Hall-thruster discharge](/methods/one-dimensional-fluid-hall-model.md)
* [Secondary electron emission and sheath regimes](/definitions/secondary-electron-emission.md)

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2021_Crossref_Aerospace_Giannetti_Numerical_and_Experimental_Investigation_of_Longitudinal_Osc.pdf`.
   * **Version.** Published version (MDPI typeset, CC BY 4.0), 23 pages.
   * **Identity.** doi:10.3390/aerospace8060148, checked on Crossref (title,
     five authors, Aerospace 8(6), article 148): received 15 April 2021,
     accepted 22 May 2021, published (online and issue) 26 May 2021.
   * **How it was read.** All 23 pages; equations checked on rendered pages
     7, 8, 19 and 20, none unreadable. Values from Figs. 5, 6 and 9 are read
     off plots and approximate; only Table 2 is exact. Figs. 3–4 (probe
     signals) not used quantitatively.
   * **Recorded as printed.**
     - Eq. 3 carries a wall sink on the ion momentum, which the reformulated
       eq. 17 (stated to be eq. 3 with $\partial_z\phi$ eliminated) drops
       without comment.
     - "Lafambroise" for Laframboise (§3.3).
     - Below eq. 16, $K$ is a function of the electron energy and then
       "calculated as a function of the electron temperature" (equivalent
       for a Maxwellian EEDF).
     - Fig. 9's probe axis extends to about $3.8L_{\mathrm{ch}}$ while §4
       gives 15 mm upstream to 70 mm downstream of the exit; with
       $L_{\mathrm{ch}}$ unprinted the mapping cannot be checked.
   * **Reference list:** 75 entries (Crossref count 75). No DOIs printed.
     Printed oddities kept: ref 38 "Leporini, A.", ref 66 "Sivia, J.S.D.",
     ref 61 "Ortega, A.L.".

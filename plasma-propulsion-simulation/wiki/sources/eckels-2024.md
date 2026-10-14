---
type: Source
title: "Eckels et al. (2024) — Hall thruster model improvement by multidisciplinary uncertainty quantification"
description: "Couples semi-empirical cathode and plume models with a 1D multi-fluid thruster code, replaces the thruster by a multifidelity MISC surrogate with SVD-reduced field outputs, and calibrates 17 parameters on SPT-100 background-pressure data by DRAM MCMC; residual errors far exceed noise and parametric uncertainty, which the authors attribute to model-form error, and Sobol' analysis shows the anomalous-transport coefficients dominate."
resource: "doi:10.1007/s44205-024-00079-w"
source_kind: paper
authors: [Eckels J.D., Marks T.A., Allen M.G., Jorns B.A., Gorodetsky A.A.]
year: 2024
venue: "J. Electr. Propuls. 3:19"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2024_Crossref_Journal_of_Electric_Propulsion_Eckels_Hall_thruster_model_improvement_by_multidisciplinary_uncerta.pdf"
tags: [uq, calibration, hall-thruster, fluid, anomalous-transport, plume, verification]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper builds a feed-forward multidisciplinary "predictive engineering
model" of a Hall-thruster system: a semi-empirical cathode coupling-voltage
model (Jorns & Byrne 2021), a 1D axial multi-fluid discharge model
(HallThruster.jl) and a semi-empirical far-field plume model (Allen et
al. 2022), with the facility background pressure entering in four places.
The thruster component is replaced by a multifidelity multi-index
stochastic collocation (MISC) surrogate, extended with SVD dimension
reduction for field outputs. With it the authors calibrate all component
parameters on SPT-100 literature data (DRAM MCMC, 17 parameters), propagate
uncertainty, extrapolate to an independent SPT-100 dataset, and compute
Sobol' indices over background pressure. The paper states explicitly that
it proposes no new Hall-thruster physics; its contribution is the UQ
workflow and what it reveals about the model. Merged into
[Bayesian calibration](/methods/bayesian-calibration.md).

# Key claims

1. **Scope** (Introduction, pp. 2–3): "We do not propose a new Hall
   thruster model nor any new insight into anomalous transport or facility
   effects." Priority claim (stated): "first attempt at global calibration
   of a fluid Hall thruster model on system-level data with uncertainty
   quantification of both anomalous transport and facility effects". A
   "predictive" model is one that predicts key outputs over a broad range
   of operating conditions with a single set of global parameters,
   including where no data exist (p. 2).
2. **Anomalous transport** (eqs. 5–6): $\nu_{\mathrm{ano}}=a_1\omega_{ce}$
   upstream of a transition point and $a_2a_1\omega_{ce}$ downstream (after
   Hofer et al. 2008), so $\alpha_{\mathrm B}=16a_1$ and $16a_1a_2$; the
   transition moves with background pressure along a logistic law with a
   fixed steepness parameter 14 ("shifted Bohm").
3. **Background pressure** (eqs. 3–4, 20, 22): cathode coupling voltage
   rises with background pressure; thermal ingestion of background neutrals
   adds to the anode neutral flux.
4. **Surrogate** (eq. 9, Fig. 3, pp. 10–13): model fidelity = cells
   (100, 150, 200) and charge states (1–3); many outputs reach 10 % or less
   relative $L_2$ test error (500 samples) for about 200 high-fidelity
   evaluations over 12 inputs; multifidelity beats single high fidelity at
   equal cost.
5. **Calibration** (Table 3, p. 13): 100,000 DRAM iterations, 10 % burn-in,
   acceptance 22 %, 17 dimensions. Medians include cathode $T_e$ 1.33 eV,
   vacuum coupling voltage 31.6 V, neutral speed 141.2 m/s, transition
   length 1.88 mm, $\log_{10}a_1=-2.167$ ($\alpha_{\mathrm B}\approx0.11$,
   computed here), $a_2=14.6$ (downstream $\alpha_{\mathrm B}\approx1.6$),
   transition displacement 0.4 (at its prior bound). Four parameters are
   pushed to prior bounds.
6. **Wrong thrust trend** (Obs. 1, Fig. 5): the model predicts thrust
   falling with background pressure, the experiment (Diamant et al. 2014)
   rising; the model's current utilization falls from 66 % to 51 %.
7. **Discharge current** (Obs. 4): posterior $I_d$ still more than 50 %
   above the 4.5 A experiment; the authors suspect a three-zone transport
   model would fix it (not shown).
8. **Surrogate-induced error** (Obs. 3, Table 4): below $\log_{10}a_1=-2$ the
   model's thrust is "discontinuous, unstable"; the posterior lies there,
   so the surrogate thrust error rises from 1 % to 23 % and the true
   model's thrust error at the median worsens from 22 % to 29 %.
9. **Ion velocity** (Fig. 7): the shifted transition moves the acceleration
   region upstream with pressure but too little, and profiles are not steep
   enough; under this parameterization the 1D model is "unlikely" to
   capture location, steepness and far-field asymptote together (stated).
10. **Plume** (Figs. 8–9): wings above 50° match, but the centreline
    current density falls with pressure in the model and rises in the
    experiment; the inflection angle is about 50° measured and 40° modelled.
11. **Training summary** (Table 4): posterior s.d. of the error at most
    0.3 % for all outputs; surrogate mean error prior → posterior:
    coupling voltage 54 → 1.3 %, thrust 19 → 2.6 %, $I_d$ 290 → 45 %, ion
    velocity 35 → 21 %, plume current density 79 → 33 %; true model at the
    median: thrust 22 → 29 %, $I_d$ 230 → 63 %, ion velocity 50 → 17 %,
    current density 80 → 49 %.
12. **Extrapolation** (Table 5, Figs. 10–11; Sankovic et al. 1993):
    surrogate thrust 20 → 7 %, $I_d$ 270 → 40 %; true model thrust 22 →
    30 % (worse), $I_d$ 193 → 53 %.
13. **Sensitivity** (Fig. 12, App. E Fig. 17): the anomalous coefficients
    dominate thrust and exit ion velocity (total index above 0.8 for the
    in-channel one, growing with pressure); the shifted-transition
    parameters matter little (over-parameterization); pressure and flow
    uncertainties are negligible; the neutral speed is "surprisingly"
    important for thrust.
14. **Conclusion** (pp. 26–28): model-form error is the dominant accuracy
    limit. Suggested: a 2D thruster model, a physics-based plume model, a
    background-flow ingestion model (thermal ingestion found
    insufficient), three-region anomalous transport, nonlinear dimension
    reduction, time-resolved analysis, and accounting for model-form and
    surrogate error (e.g. Gaussian processes).

# Models and numerics

System: cathode → thruster → plume, coupled through the cathode coupling
voltage (potential boundary condition of the 1D domain) and the beam
current (Fig. 1, eqs. 1–2); 22 inputs (Table 1), 7 outputs (Table 2).
Thruster: HallThruster.jl (Julia; Marks et al. 2023), 1D axial
multi-fluid, all species fluid, 1–3 ion charge states, 100–200 cells; the
governing equations, field solver, collision model and the role of the
transition length are not given in this paper; boron-nitride–silica wall
properties; neutral injection speed calibrated; centreline $B_r(z)$ after
Sahu et al. 2020, peak 0.016 T. SPT-100 geometry (Table 6): channel length
0.025 m, radii 0.035 and 0.05 m, xenon, external cathode. One thruster
evaluation takes about 1 min. Plume (App. A): Gaussian-in-angle beam and
scattered components plus isotropic charge-exchange ions, xenon
charge-exchange cross section about 55 Å$^2$ (prior 51–58 Å$^2$), radius
1 m. UQ: MISC with adaptive index sets and Lagrange interpolants, Leja
sequences, SVD to 4 (ion velocity, 200 points) and 2 (current density,
100 points) coefficients at 95 % variance from 500 offline runs; DRAM
MCMC; Gaussian likelihood with experimental error bars read as s.d. = 1/4
of the error range ($I_d$ ±10 % assumed); Monte Carlo forward propagation
with 1000 samples; Sobol' indices with 5000 samples. Code:
github.com/JANUS-Institute/HallThrusterPEM and github.com/eckelsjd/amisc
(p. 39). Computed on the University of Michigan Advanced Research
Computing cluster; GPU or MPI use not stated.

# Tests and results

Five SPT-100 datasets: (1) cathode coupling voltage, 31.12–33.11 V for
background pressures $1.67\times10^{-6}$ to $7.37\times10^{-5}$ Torr at
300 V (Jorns & Byrne 2021); (2) thrust, 80.05–83.11 mN at constant
$I_d=4.5$ A (Diamant et al. 2014); (3) plume ion current density (Diamant
et al. 2014); (4) LIF axial ion velocity (Macdonald et al. 2019); (5)
thrust and $I_d$ off-nominal (Sankovic et al. 1993), held out. Results in
Key claims 6–13. The cathode model fits well but asymptotes to 31.6 V at
zero pressure while the data keep falling (Fig. 4).

# Notation map

| Eckels et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\nu_{\mathrm{AN}}$ | $\nu_{\mathrm{ano}}$ | |
| $a_1$, $a_2$ | $\alpha_{\mathrm B}=16a_1$ (upstream), $16a_1a_2$ (downstream) | $a_2$ is a ratio, not the downstream coefficient |
| $z^*$, $\Delta z$, $z_0$, $p_0$, $b$, $l_t$ | words | transition location and its parameters |
| $L_{ch}$ | $L_{\mathrm{ch}}$ | |
| $P_B$, $P^*$, $P_T$ | words (background pressure, fit pressures) | **collision:** registry $P$ is electric power |
| $V_{cc}$, $V_{vac}$ | words (cathode coupling voltage, its vacuum value) | |
| $V_a$, $\dot m_a$ | $V_d$, $\dot m$ | |
| $I_d$, $I_b$, $\eta_c$ | $I_d$, $I_b$, $\eta_c$ | |
| $T$ (thrust) | $F$ | **collision** with $T_s$ |
| $T_e$ | $T_e$ | here the cathode electron temperature |
| $u_{\mathrm{ion}}(z)$, $u_n$ | axial components of $\mathbf u_i$, $\mathbf u_n$ | |
| $j_{\mathrm{ion}}$ | words (plume ion current density) | |
| $\gamma$ | words (plume angle) | **collision** with the polytropic $\gamma$ |
| $\sigma_{cex}$ | $\sigma_{sk}$, charge exchange in words | |
| $\theta$ (parameters) | $\boldsymbol\vartheta$ | **collision** with the azimuthal $\theta$ |
| $\xi$ | words | overloaded: coupling variables (eq. 2), noise (eq. 10), relative noise (Table 4) |
| $\Gamma$ | words | overloaded: input domain (eq. 1), particle flux (eq. 4) |
| $\alpha$, $\beta$ (MISC indices) | words | **collision** with $\alpha_{\mathrm B}$ |
| $S_{1i}$, $S_{Ti}$ | $S_j$, $S_{T,j}$ | |

# Pages created or updated

Chunk 1 (2026-10-14) created every page of the bundle. This source is cited on:

* [Anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md)
* [Bayesian calibration of thruster models](/methods/bayesian-calibration.md)
* [Electron fluid models (drift-diffusion)](/methods/electron-fluid-model.md)
* [Hall-effect thruster](/definitions/hall-effect-thruster.md)
* [One-dimensional fluid model of the Hall-thruster discharge](/methods/one-dimensional-fluid-hall-model.md)
* [SPT-100 as a validation case](/benchmarks/spt-100.md)

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2024_Crossref_Journal_of_Electric_Propulsion_Eckels_Hall_thruster_model_improvement_by_multidisciplinary_uncerta.pdf`.
   * **Version.** Publisher's version of record (Springer Nature, CC BY 4.0),
     40 pages.
   * **Identity.** doi:10.1007/s44205-024-00079-w, checked on Crossref
     (title, five authors, J. Electr. Propuls. 3(1), article 19): received
     20 May 2024, accepted 30 Aug 2024, online and issued 27 Sep 2024 (no
     separate print date).
   * **How it was read.** Whole paper; Fig. 12 rendered; other figures
     through captions and text, curve values not extracted. Eqs. 31–32
     (plume normalizations, with erfi terms) read from the rendered page 30
     because the text layer is garbled.
   * **Recorded as printed.**
     - p. 17 (Obs. 2) calls the uncertainty bounds overconfident because
       they omit model-form and surrogate error; p. 28 calls them "overly
       conservative" for the same reason. Omitting an uncertainty source
       narrows bounds, so p. 17 is the consistent statement.
     - The text calls the transition displacement "the total displacement
       from zero to infinite pressure"; with the fixed steepness 14, eq. 6
       gives $14/15$ of it.
     - Remark 3 reads the displacement's collapse onto its prior bound as
       over-parameterization ("further data … will likely not reduce
       epistemic uncertainty"), while Remark 4 and p. 18 show the
       likelihood pushing against the bound.
     - The abstract's "more accurate, sometimes by an order of magnitude"
       applies to the surrogate; the true model's thrust error worsens
       (Tables 4–5).
     - "below 0.3 %" (p. 22) against Table 4, where two values equal 0.3;
       "over 30 %" for thrust (pp. 24, 27) against Table 5's 30 %.
     - Table 1 describes one fit pressure as a "plasma density ratio" but
       gives it in µTorr.
   * **Reference list:** 44 entries (Crossref count 44). Ref 42 (Gascon,
     Dudeck & Barral) is printed with year 2023, Phys. Plasmas vol. 10 and
     a DOI of 2003, journal "hys Plasmas"; kept as printed. Ref 21's page
     range "35:1–10" looks like an online-first placeholder.

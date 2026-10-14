---
type: Source
title: "Saravia et al. (2026) — Calibration of a Hall thruster numerical model using a Bayesian approach"
description: "Bayesian calibration, by nested sampling, of four parameters of a 1D fluid Hall-thruster model (the LANDMARK test case 3) on synthetic data, with a Wasserstein likelihood for the time-resolved discharge current; current-only data leave the plume anomalous coefficient unidentified, while adding thrust and plume electron temperature recovers it within 57 %."
resource: "doi:10.1007/s11071-026-12217-0"
source_kind: paper
authors: [Saravia M.M., Giannetti V., Guidi C., Paganucci F., Camarri S.]
year: 2026
venue: "Nonlinear Dyn. 114:350"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2026_Crossref_Nonlinear_Dynamics_Saravia_Calibration_of_a_Hall_Thruster_numerical_model_using_a_Bayes.pdf"
tags: [calibration, uq, hall-thruster, fluid, anomalous-transport, oscillation, verification, benchmark]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper proposes an automated Bayesian procedure for the free
parameters of a 1D axial quasi-neutral fluid Hall-thruster model, the
authors' implementation of [LANDMARK test case 3](/methods/one-dimensional-fluid-hall-model.md).
Four parameters are calibrated: the neutral injection speed, the
anomalous energy-loss coefficient, and the in-channel and plume Bohm
coefficients. The data are synthetic, from a reference run with noise: a
time-resolved discharge current, a thrust value and a plume electron
temperature. The current enters through a likelihood built on the
quadratic Wasserstein distance between time-lagged phase-portrait
densities (after Greve et al. 2019), the scalars through Gaussian
likelihoods; the posterior is sampled by nested sampling (UltraNest). The
method is first verified on the Lorenz system. The main result is limited
identifiability: current-only calibration does not identify the plume
coefficient and leaves the neutral speed multimodal, and adding thrust and
plume $T_e$ sharpens every posterior. Merged into
[Bayesian calibration](/methods/bayesian-calibration.md).

# Key claims

1. **Data fusion** (§4.1, eqs. 19–27, Fig. 4): the joint likelihood is the
   product of independent per-datum likelihoods, three data, all from one
   model run per sample.
2. **Time-signal likelihood** (§4.1.2, eq. 27): "analog to the Normal
   distribution", with the Euclidean norm replaced by the squared
   Wasserstein distance between 2D phase-portrait densities on 50×50 bins.
3. **Lorenz verification** (§5, Tables 3–4, Figs. 5–6): all three Lorenz
   parameters recovered from a noisy reference (noise s.d. 0.05):
   $10.36^{+1.07}_{-1.25}$ (reference 10), $2.67^{+0.28}_{-0.33}$ (2.67),
   $27.97^{+1.07}_{-1.05}$ (28); the first marginal is nearly flat, which
   the paper attributes to the attractor's critical points depending only
   on the other two.
4. **Marginalizing the current-likelihood width is harmful** (§6.1,
   Table 5, Fig. 7, App. B): with a Jeffreys prior on $[10^{-3},10^2]$ the
   posteriors are nearly flat; the width is fixed to 1, and its
   prescription is called an open problem.
5. **Current-only calibration is not identifiable** (§§6.2, 6.3.3,
   Tables 5, 7, Figs. 8, 11–12): plume coefficient
   $3.50^{+1.74}_{-1.68}$ against 1.0, neutral speed multimodal; two
   samples (A: plume coefficient 4.86, thrust 96.7 mN, $T_e$ 8.56 eV; B:
   neutral speed 230.3 m/s, plume coefficient 3.01, 86.8 mN, 11.0 eV) both
   fit the current by "typical fitting criteria".
6. **Data fusion restores identifiability** (§§6.2–6.3, Tables 5–6,
   Fig. 9): plume coefficient $1.57^{+1.78}_{-0.67}$ (57 % error against
   250 %); thrust $101.36^{+2.22}_{-3.27}$ mN (reference 103); plume $T_e$
   $12.14^{+2.84}_{-2.91}$ eV (14.2); a positive correlation between the
   energy-loss coefficient and the in-channel Bohm coefficient.
7. **Inferred profile** (§6.3.1, Fig. 9): in-channel $\alpha_{\mathrm B}(z)$
   recovered in all cases, the plume value only with plume data.
8. **Code verification on LANDMARK TC3** (App. A, Figs. 13–14): mean
   current 8.03 A (benchmark) against 7.96 A (under 1 %); peak plasma
   density $1.04\times10^{19}$ m$^{-3}$ (5.4 %), peak neutral density
   $7.87\times10^{19}$ m$^{-3}$ (2.8 %); residual attributed to numerical
   viscosity.
9. **Contrast with Eckels et al. (2024)** (§7): their steady data,
   Gaussian likelihoods and MCMC are contrasted with this paper's
   time-resolved likelihood and nested sampling, "reducing the reliance on
   surrogate models"; agreement with Marks & Jorns (2023) on the need for
   time-dependent data. A methodological contrast, not a disagreement on
   results.

Table 5 (median and central 68 %):

| Parameter | Reference | Case 1, width marginalized | Case 1, width 1 | Case 2, width marginalized | Case 2, width 1 |
|---|---|---|---|---|---|
| neutral speed [m/s] | 150 | $239.72^{+72.11}_{-107.56}$ | $155.24^{+153.08}_{-26.84}$ | $168.41^{+90.75}_{-59.40}$ | $137.74^{+15.73}_{-12.40}$ |
| energy-loss coefficient | 0.4 | $0.40^{+0.20}_{-0.19}$ | $0.43^{+0.12}_{-0.10}$ | $0.53^{+0.13}_{-0.17}$ | $0.44^{+0.09}_{-0.10}$ |
| in-channel $\alpha_{\mathrm B}$ | 0.1 | $0.15^{+0.10}_{-0.09}$ | $0.11^{+0.05}_{-0.04}$ | $0.10^{+0.05}_{-0.04}$ | $0.10^{+0.03}_{-0.03}$ |
| plume $\alpha_{\mathrm B}$ | 1.0 | $3.44^{+1.83}_{-1.80}$ | $3.50^{+1.74}_{-1.68}$ | $1.51^{+1.67}_{-0.70}$ | $1.57^{+1.78}_{-0.67}$ |

Case 1: current only. Case 2: current, thrust and plume $T_e$. Table 6
(width 1): thrust $94.92^{+7.15}_{-18.71}$ mN (Case 1) and
$101.36^{+2.22}_{-3.27}$ mN (Case 2); plume $T_e$ $10.11^{+2.69}_{-1.64}$ eV
and $12.14^{+2.84}_{-2.91}$ eV.

# Models and numerics

**Calibration set-up.** Parameters: neutral injection speed (stated
typical range 100–250 m/s), anomalous energy-loss coefficient (stated
typical 0.1–0.5 in the channel, 1 outside), in-channel and plume Bohm
coefficients joined by a two-error-function profile of width
$L_{\mathrm{ch}}/50$ (eq. 21). Priors: independent uniforms, 75–350 m/s,
0.1–0.7, 0.01–0.3, 0.3–6.0, with in-channel < plume. Likelihoods: thrust
Gaussian with s.d. 5 mN; plume $T_e$ at $z=\tfrac32L_{\mathrm{ch}}$
Gaussian with 20 %; current by eq. 27 with a constant lag (value for the
Hall case not stated), Wasserstein distance from the Python "Wasserstein"
library. Data: current $I_d(t)$ with Gaussian noise of s.d. 0.1 A, thrust
103 mN (time-averaged ion momentum flux at the outlet, eq. 16), plume $T_e$
14.2 eV. Sampler: nested sampling, UltraNest 4.3.3, 120 live points, stop
at 1 % remaining posterior volume, up to 280 cores, "tens of thousands of
evaluations in less than 100 hours". App. B filters samples below 0.2 of
the maximum normalized likelihood, by analogy with burn-in.

**Physical model** (§§2.1–2.2, after the first author's group, ref. 44):
see [one-dimensional fluid model](/methods/one-dimensional-fluid-hall-model.md)
and [LANDMARK test case 3](/methods/one-dimensional-fluid-hall-model.md). Xenon;
$R_{\mathrm{in}}=3.5$ cm, $R_{\mathrm{out}}=5.0$ cm, $L_{\mathrm{ch}}=2.5$ cm,
domain 5.0 cm, 5 mg/s, 300 V (Table 1, "based on the SPT-100"); Gaussian
$B$ with peak 0.015 T at the exit plane (eq. 15); constant
$\nu_w=10^7$ s$^{-1}$ in the channel; no SEE, no radial losses; LANDMARK
viscosity dropped (footnote 1). Finite volume, five-step Lie splitting,
upwind neutrals, Steger–Warming ions, implicit electron energy, 1000
cells, CFL 0.8. Robustness (§4.2): divergence from current blow-up or anode
detachment; each sample starts from one stored state and ramps its
parameters over 0.5 ms; output is stored only once the current is
stationary. Code: FORTRAN 95, shared memory, Python 3 driver through f2py,
unnamed, no GPU.

# Tests and results

LANDMARK TC3 verification (App. A), Lorenz verification (§5), and the
four Hall-thruster calibrations (Cases 1–2, width marginalized or fixed;
§6, Tables 5–7, Figs. 7–12, 15–16). Predicted currents are shown only at
the posterior median, because prediction bands are meaningless for
out-of-phase oscillations (§6.3). Lorenz set-up: SciPy odeint, step
$5\times10^{-3}$, $10^5$ steps, 60 bins, lag 40 steps, 120 live points.

# Notation map

| Saravia et al. (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $n$ | $n_e=n_i$ | |
| $u_n$, $u_{inj}$, $u_i$, $u_e$ | axial components of $\mathbf u_n$, $\mathbf u_i$, $\mathbf u_e$ | $u_{inj}$ is the calibrated neutral speed |
| $\Phi$ | $\phi$ | |
| $\mu$ | $\mu_\perp$ | |
| $\nu_e$, $n_nk_m$, $\nu_w$, $\nu_{anom}$ | $\nu_e$, $\nu_{en}$, $\nu_w$, $\nu_{\mathrm{ano}}$ | |
| $\omega_c$, $\omega_e$ | $\omega_{ce}$ | both spellings in the paper |
| $\beta$, $\beta_{in}$, $\beta_{out}$ | $\alpha_{\mathrm B}$ (in-channel, plume) | $\nu_{anom}=\beta\,\omega_{ce}/16$, so $\alpha_{\mathrm B}=\beta$; **collision** with the Lorenz $\beta$ and the profile width $\beta_L$ |
| $k_I$ | $k_{\mathrm{ion}}$ | |
| $K$, $W$, $\nu_\varepsilon$, $U$ | words (collisional loss, anomalous energy loss, its coefficient, 20 eV) | **collision:** registry $W$ is the macroparticle weight |
| $J$, $I_d$, $V_d$, $\dot m$ | $j_z$, $I_d$, $V_d$, $\dot m$ | |
| $T$ (thrust) | $F$ | **collision** with $T_s$ |
| $\theta$ (parameter vector) | $\boldsymbol\vartheta$ | **collision** with the azimuthal $\theta$ |
| $D$, $I$ | $\mathbf d$, words (background information) | |
| $p(\theta\mid D,I)$, $p(D\mid\theta,I)$ | $\pi(\boldsymbol\vartheta\mid\mathbf d)$, $\mathcal L(\boldsymbol\vartheta)$ | |
| $W_2$ | words (quadratic Wasserstein distance) | close to $W$ |
| $\sigma_T$, $\sigma_{I_d}$, $S_{EMD}$ | words (likelihood widths) | **collision** with $\sigma_{sk}$ |
| $\sigma$, $\rho$, $\beta$ (Lorenz) | words | Source page only |

# Pages created or updated

Chunk 1 (2026-10-14) created every page of the bundle. This source is cited on:

* [Anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md)
* [Bayesian calibration of thruster models](/methods/bayesian-calibration.md)
* [Breathing mode](/definitions/breathing-mode.md)
* [Cross-field electron mobility and the Hall parameter](/definitions/electron-mobility-and-hall-parameter.md)
* [Electron fluid models (drift-diffusion)](/methods/electron-fluid-model.md)
* [Near-wall conductivity](/definitions/near-wall-conductivity.md)
* [One-dimensional fluid model of the Hall-thruster discharge](/methods/one-dimensional-fluid-hall-model.md)
* [Secondary electron emission and sheath regimes](/definitions/secondary-electron-emission.md)
* [SPT-100 as a validation case](/benchmarks/spt-100.md)

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2026_Crossref_Nonlinear_Dynamics_Saravia_Calibration_of_a_Hall_Thruster_numerical_model_using_a_Bayes.pdf`.
   * **Version.** Publisher's version of record (Springer, CC BY 4.0), 22
     pages.
   * **Identity.** doi:10.1007/s11071-026-12217-0, checked on Crossref
     (title, five authors, Nonlinear Dyn. 114(5), article 350): received
     6 Feb 2025, revised 30 Dec 2025, accepted 3 Jan 2026, online
     10 Mar 2026, issue March 2026.
   * **How it was read.** Whole paper; eqs. 1–16, 21–27 and Table 5 checked
     on rendered pages 3–6, 8, 10, 14 and 16. Corner plots (Figs. 6–10,
     15–16) not reproduced numerically. The $k_I$ and $K$ tables come from
     the benchmark and are not reproduced.
   * **Recorded as printed.**
     - The electron–neutral rate coefficient is printed
       $k_m=2.5\times10^{13}$ m³/s (§2.1); a positive exponent is not
       physical for this quantity, $2.5\times10^{-13}$ is the likely value.
       Not corrected.
     - The energy-loss coefficient is dimensionless in eq. 9, Table 1, §4.1
       and Table 2 (0.4; prior 0.1–0.7), but App. A writes
       "$\nu_\varepsilon>0.5\times10^7$ s⁻¹" and "$0.4\times10^7$ s⁻¹".
     - §6.1 says marginalized Case 2 gives the neutral speed within 10 %;
       Table 5 gives 168.41 against 150 (12.3 %).
     - "($m_{Xe}=131.3$) AMU" garbled (§2.1); §6 refers to "Section 2.2.3"
       for the test case of §2.3.
     - The Fig. 14 caption says "HALLIS benchmark", elsewhere LANDMARK; App.
       A calls the authors' own run the "reference simulation", so which of
       8.03 and 7.96 A belongs to which run rests on one sentence.
     - §6 calls the nested-sampling output "MCMC chains".
     - §1 spells "Troyestky"; §4.1 describes the anomalous term as the
       product of $\beta(z)$ and $\omega_e$, omitting the 1/16 of eq. 7.
   * **Reference list:** 62 entries. Refs [22] and [45] are the same work
     (Hara 2018, Phys. Plasmas 25(12)); [43] (LANDMARK website) and [61]
     (UltraNest website) carry no year; [46] (Steger & Warming 1981) has a
     garbled author field; [40] (Marks & Jorns 2023) has no title.

---
type: Source
title: "Gómez-San-Juan, Pérez-Grande & Sanz-Andrés (2018) — Uncertainty calculation for spacecraft thermal models using a generalized SEA method"
description: "Proposes the one-dimensional generalized statistical error analysis (OGS), which screens parameters by linear sensitivity, fits one-dimensional non-linear surrogates, maps parameter PDFs by change of variables and convolves them, and shows on the Solar Orbiter EPD-STEP thermal model that it stays within 1.2 °C of Monte Carlo limits at under 3% of its cost."
resource: "doi:10.1016/j.actaastro.2018.05.045"
source_kind: paper
authors: [Gómez-San-Juan A., Pérez-Grande I., Sanz-Andrés A.]
year: 2018
venue: "Acta Astronaut. 151:691–702"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Gómez-San-Juan_Uncertainty_calculation_for_spacecraft_thermal_models_using.pdf"
tags: [context, thermal-control, uq, monte-carlo, surrogate-model]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper compares the two standard methods for temperature uncertainty
in spacecraft thermal models: Statistical Error Analysis (SEA: linear
sensitivities combined by root-sum-square, Eq. 4) and Monte Carlo
Simulation (MCS). It identifies two sources of SEA error, model
non-linearity (§3.3.1.1) and the restriction to normal, independent
parameter distributions (§3.3.1.2), and proposes the One-dimensional
Generalized SEA (OGS) method (§4). SEA screening keeps the parameters that
account for 99% of the uncertainty; each retained parameter gets a
one-dimensional non-linear surrogate of its temperature contribution
(linear, quadratic or exponential, fitted to $R^2\ge0.99$); the parameter
PDF is mapped through the surrogate by change of variables (Eq. 10); the
node-temperature PDF is the convolution of the contribution PDFs
(Eq. 12). On the 1378-node ESATAN-TMS model of the EPD-STEP instrument of
Solar Orbiter (steady hot case at 0.28 AU, 76 parameters), OGS costs
13.7 h against 10.7 h for SEA and 578.9 h for MCS (Table 2) and stays
within 1.2 °C of the MCS temperature limits at 99.7% confidence, while SEA
errs by up to 3.8 °C on the lower limit (Table 5). Joint (cross-parameter)
non-linearity is neglected and left to future work. The paper has no
plasma or propulsion content.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Classical SEA** (§1.2, attributed to [6,10] after Kline &
   McClintock [9]): $w_{T_i}=\sqrt{\sum_{k=1}^{N_P}\left(\frac{\partial T_i}{\partial p_k}w_{p_k}\right)^2}$.
2. **Linear propagation theorem** (§3.2, Eq. 4, cited [26]): if $T$ is
   linear in $\nu$ independent normal variables, $T$ is normal with
   $w_T=\left[\sum_j\left(\frac{\partial f(\mu_1,\dots,\mu_\nu)}{\partial x_j}w_j\right)^2\right]^{1/2}$.
3. **MCS sample size** (§3.1, Eqs. 2–3, attributed to [25]):
   $N_{\min1}=(2N_\sigma s/\Delta x)^2$ for the mean and
   $N_{\min2}=P(1-P)(N_\sigma/\Delta P)^2$ for a percentile; worked
   examples give 2500 ($s=5$ °C, $\Delta x=0.4$ °C, $N_\sigma=2$) and 1900
   ($P=0.95$, $\Delta P=0.01$, $N_\sigma=2$).
4. **Cost models** (§3.3.2, Eqs. 6–7; §4.3, Eq. 13):
   $t_{MCS}=N_s(t_R+t_T)$; $t_{SEA}=(N_{PR}+1)(t_R+t_T)+N_{PT}t_T$,
   dominated by the first term since $t_R\gg t_T$;
   $t_{OGS}=4N_{PRS}(t_R+t_T)+4N_{PTS}t_T+t_{SEA}$, a first estimate
   without the extra runs of exponential fits.
5. **SEA as a special case** (§4.1): SEA is OGS with linear surrogates,
   normal PDFs and independent parameters. The Taylor linearisation
   (Eq. 8) holds if $|f'|\gg|f''|\sigma$ and $|x-\mu|<\sigma$ [26], but in
   practice $|x-\mu|\sim N_\sigma\sigma$ with $N_\sigma$ between 1 and 4,
   which motivates non-linear fits. Stated.
6. **OGS** (§4.2, Eqs. 9–12): $T_i\simeq\mu_{T_i}+\sum_{k=1}^{N_{PS}}u_{ik}(p_k)$;
   change of variable for a one-to-one $u_{ik}$ with inverse $v_{ik}$
   (Eq. 10, printed form in Recorded as printed); $h_i=g_{i1}*g_{i2}*\dots*g_{iN_{PS}}$
   (Eq. 12). Quadratic surrogates need the extremum outside the parameter
   range, otherwise a singular point changes the transformed PDF.
7. **Cost on the test case** (§5.4.1, Table 2; i7-7700K 4.20 GHz, 32 GB):
   SEA 34 radiative and 77 thermal runs, 10.7 h; OGS 42 and 159, 13.7 h;
   MCS 1900 and 1900, 578.9 h. OGS costs under 3% of MCS (§6). Shown.
8. **Accuracy on the test case** (§5.4.2, Tables 4–5): at 99.7%
   confidence, OGS−MCS differences in the temperature limits are at most
   1.2 °C; SEA−MCS lower-limit differences are −2.0 to −3.8 °C (SEA
   predicts colder minima, suggesting overdesign). OGS−MCS differences stay
   about 1 °C across confidence levels, SEA−MCS differences grow with it.
   SEA margins are symmetric by construction, OGS and MCS margins
   asymmetric. Shown for this single model.
9. **Dominant parameters** (§5.4.2, Fig. 5): about 90% of the uncertainty
   comes from a few parameters; the instrument-to-spacecraft conductive
   coupling (lognormal, the main source of PDF asymmetry) dominates for all
   parts, the IR emittance of the optical solar reflectors is second.
   Shown for nodes T3 and T4.
10. **Generality** (§6): cross-influence non-linearities "do not seem to
    contribute in a relevant way" here, and the method "has given accurate
    results for most of the thermal models analyzed by the authors".
    Stated; no data shown for other models.

# Methods

* Thermal model (§2.1, Eq. 1): lumped-node balance
  $C_i\,dT_i/dt=Q_{S-i}+Q_{a-i}+Q_{IRp-i}+Q_i+\sum_jGL_{ij}(T_j-T_i)+\sigma_{SB}\sum_jGR_{ij}(T_j^4-T_i^4)$;
  a geometrical model (Monte Carlo ray tracing) supplies radiative loads
  and exchange factors, a thermal model solves the network; only steady
  cases are computed.
* Parameter classes (§2.2): radiative parameters (solar absorptance, IR
  emittance, planetary or Sun temperature) need a ray-tracing plus thermal
  rerun; thermal parameters only a thermal rerun.
* SEA derivatives by one-sided difference quotients, one run per parameter
  plus the nominal (§5.4.1).
* OGS steps (§4.2): (1) SEA screening to 99% of the uncertainty,
  $N_{PS}<N_P$; (2) per-parameter regression on 5 points (nominal plus 4
  evenly spaced over the expected range), linear, then quadratic, then
  exponential until $R^2=0.99$, with extra runs if needed; (3) PDF change
  of variables (Eq. 10); (4) convolution (Eq. 12), CDF by integration,
  analytically or via the characteristic function, margins at any
  confidence level.
* Test model (§5.1–5.3): EPD-STEP on Solar Orbiter; ESATAN-TMS model with
  1378 diffusive and 86 boundary nodes; steady hot case at 0.28 AU (solar
  flux ≈17500 W/m², "13 more times than at 1 AU"); high-gain antenna as a
  400 °C boundary node; $10^6$ rays for antenna couplings and solar fluxes,
  $10^4$ elsewhere; run times 1070 s radiative, 20 s thermal solver, 7 s
  pre-processing.
* Parameters (§5.3): 76 = 33 radiative (absorptance and emittance of 16
  finishes plus the Sun temperature) + 43 thermal. Optical properties
  normal, 5% standard deviation; Sun temperature normal, σ = 11 °C;
  internal dissipations triangular, coefficient of variation 0.1;
  conductivities normal, 0.0625; MLI effective emittance uniform, 0.2;
  contact conductances and couplings lognormal with 90% of the CDF between
  −50% and +100%, 0.43. For SEA all PDFs are replaced by equal-variance
  normals (the lognormal then gives about 1% negative values).
* Screening result: $N_{PS}=13$ (2 radiative, 11 thermal); 5 of the 11
  thermal parameters needed exponential fits (10 extra points each), the
  others 4 extra points.
* MCS: $N_s=1900$ from Eq. 3 (95% confidence that the 95th percentile lies
  between the 94th and 96th; 99.7% margins within ±0.25% at 95%
  confidence); 2400 runs performed, convergence shown over the last 500
  (Table 3).

# Tests and results

* Nodes (Table 1): T1 power PCB, T2 digital PCB, T3 analog PCB, T4 IT
  detector, T5 PT detector (hottest node of each element).
* Computing cost (Table 2, SEA/OGS/MCS): radiative analyses 34/42/1900;
  thermal analyses 77/159/1900; radiative time 10.1/12.5/564.7 h; thermal
  time 0.6/1.2/14.2 h; total 10.7/13.7/578.9 h.
* MCS convergence (Table 3, last 500 shots, 95% confidence): mean
  temperatures T1 [−2.8, −2.7], T2 [−5.0, −4.9], T3 [−9.6, −9.5], T4
  [−21.4, −21.3], T5 [−22.3, −22.2] °C; lower margins about [−11.4, −8.6]
  °C, upper margins about [9.1, 12.2] °C.
* Margins (Table 4, lower / mean / upper, °C): T1 at 95.4%: SEA
  −12.5/−3.2/+12.5, MCS −11.4/−2.7/+12.2, OGS −10.1/−2.9/+12.7; T1 at
  99.7%: SEA −18.8/−3.2/+18.8, MCS −16.2/−2.7/+19.1, OGS −14.8/−2.9/+20.3;
  T4 at 99.7%: SEA ±14.5 around −21.2, MCS −12.3/−21.3/+14.7, OGS
  −12.0/−21.4/+15.3.
* Differences to MCS (Table 5, °C): at 95.4%, SEA lower limit −0.8 to
  −1.7, OGS +0.6 to +1.1; at 99.7%, SEA lower limit −2.0 to −3.8 and upper
  limit −1.9 to +0.1, OGS lower limit +0.2 to +1.2 and upper limit −0.7 to
  +1.0; mean: SEA −0.6 to +0.2, OGS −0.4 to 0.0.
* Fig. 3: for T1 and T5 the OGS PDF follows the MCS histogram tail (T1
  left tail −10 to −20 °C), the SEA normal deviates.
* Figs. 5–7: contribution PDFs; the conductive coupling to the spacecraft
  dominant and asymmetric; the reflector emittance normal; dissipations
  triangular (linear response); the uniform MLI emittance through a
  quadratic surrogate gives a near-trapezoidal PDF; the E-Box-to-TCP
  coupling matters for the detectors (second for negative margins at T4),
  negligible for the E-Box.

# Notation map

The paper is spacecraft thermal analysis; none of its quantities has a
registry counterpart.

| Gómez-San-Juan et al. (2018) | Registry | Note |
|---|---|---|
| $T_i$ | words (node temperature, °C or K) | **collision:** $T_s$ is a species temperature in energy units |
| $C_i$ | words (thermal capacity, J/°C) | |
| $GL_{ij}$, $GR_{ij}$ | words (conductive coupling, W/°C; radiative exchange factor, m²) | |
| $Q_i$, $Q_{S-i}$, $Q_{a-i}$, $Q_{IRp-i}$ | words (heat loads, W) | |
| $\sigma_{SB}$ | words (Stefan–Boltzmann constant) | **collision risk** with $\sigma_{sk}$ |
| $\sigma$, $s^2$, $\mu$, $V=\sigma/\mu$ | words (standard deviation, variance, mean, coefficient of variation) | **collisions** with $\sigma_{sk}$, $\mu_0$, $\mu_\perp$ |
| $\alpha_S$, $\varepsilon_{IR}$ | words (solar absorptance, IR emittance) | **collisions** with $\alpha_E$, $\alpha_{\mathrm B}$, $\varepsilon_0$ |
| $P$ | words (percentile) | **collision:** $P$ is electric power |
| $f_k$, $g_{ik}$, $h_i$ | words (PDFs) | **collisions** with $f_s$, relative speed $g$ |
| $N_P$, $N_N$, $N_s$, $N_\sigma$, $N_{PR}$, $N_{PT}$, $N_{PS}$, $N_{PRS}$, $N_{PTS}$ | words (counts of parameters, nodes, shots, standard deviations) | |
| $w$, $w_{T_i}$, $w_{p_k}$ | words (uncertainty) | |
| $a_{ik}$, $u_{ik}$, $v_{ik}$ | words (linear sensitivity, surrogate, its inverse) | **collision:** $\mathbf u_s$ is a mean velocity |
| $t_R$, $t_T$ | words (radiative and thermal solve times) | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Gómez-San-Juan_Uncertainty_calculation_for_spacecraft_thermal_models_using.pdf`.
   * **Version.** Publisher's typeset version of record (Elsevier, © 2018
     IAA), 12 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.05.045, printed on page 1
     and checked on Crossref: title, three authors, Acta Astronaut.
     151:691–702 match; issue October 2018 (no published-online field on
     Crossref); page 1 gives received 12 Feb 2018, revised 20 Apr 2018,
     accepted 23 May 2018, online 25 May 2018. Page 1 matches the filename
     title.
   * **How it was read.** Full text layer, all equations legible. Figs. 1–7
     (instrument views, PDFs, histograms, pie charts) not digitised:
     values from text and tables only. No surrogate coefficients are
     given for the test case.
   * **Recorded as printed.**
     * §4.3, below Eq. 13: "$N_{PRS}$ and $N_{PRT}$", where Eq. 13 and the
       nomenclature have $N_{PTS}$.
     * Eq. 10 prints the PDF as $f_{ik}$ (elsewhere $f_k$) and the Jacobian
       as $1/|d\Delta T_{ik}/dv_{ik}|$, a derivative with respect to the
       inverse function; the standard factor is
       $|dv_{ik}/d\Delta T_{ik}|=1/|du_{ik}/dp_k|$. Recorded as printed,
       not corrected.
     * §5.4.1 states 578 h ("about 24 days") for 1900 MCS runs, while 2400
       were performed; Table 2 reports the minimum, not the executed,
       cost, and the "<3%" ratio of §6 uses the 1900-run figure.
     * Rounding between Tables 4 and 5: T1 95.4% SEA lower-limit
       difference −1.6 from Table 4 against −1.7 printed; T3 99.7% SEA
       upper −2.0 against −1.9; T2 99.7% OGS lower 0.6 against 0.5.
     * The text cites "Chacko et al. (1987) [18]", the list prints 1986
       (J. Spacecr. Rockets vol. 24 is 1987, so the list year is the
       likely slip; not checked on Crossref).
     * Ref. [19] prints SAE paper "2001-01-2484", year 2000 and DOI
       10.4271/2000-01-2484: internal mismatch.
     * Ref. [23] prints the malformed DOI
       "10.1016/0021-9991(78)90097–90099" (the SICI-style DOI would end
       "90097-9"); kept verbatim.
     * Ref. [9] prints "McKlintock" (Kline & McClintock, 1953).
     * Reader's check: Eqs. 2–3 give the stated 2500 and 1900; Table 2
       times follow from the run counts (34 × 1070 s = 10.1 h,
       1900 × 1070 s = 564.7 h, 159 × 27 s = 1.2 h); the §6 SEA lower-limit
       error range 2.0–3.8 °C agrees with Table 5.
   * **Reference list.** 32 printed entries ([1]–[32]), matching the
     Crossref reference count.

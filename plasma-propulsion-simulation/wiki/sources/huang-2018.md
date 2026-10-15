---
type: Source
title: "Huang et al. (2018) — A new explorer mission for soft X-ray timing - Observation of the Crab pulsar"
description: "Crab pulsar timing from 162 observations by the soft X-ray spectrometer on China's XPNAV-1 satellite: data-reduction rules, epoch folding, FFT cross-correlation phase delays and a weighted least-squares ephemeris correction giving a 55.94 microsecond post-fit RMS residual; no propulsion or plasma content."
resource: "doi:10.1016/j.actaastro.2018.05.060"
source_kind: paper
authors: [Huang L., Shuai P., Zhang X., Chen S.]
year: 2018
venue: "Acta Astronaut. 151:63–67"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Huang_A_new_explorer_mission_for_soft_X-ray_timing_-_Observation_o.pdf"
tags: [context, x-ray-pulsar-navigation, pulsar-timing, space-instrumentation]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper reports timing of the Crab pulsar (PSR B0531+21) with the
Time-resolved Soft X-ray Spectrometer (TSXS) on China's XPNAV-1 satellite,
launched 10 Nov 2016, from 162 observations over MJD 57709–57872. It gives
two data-reduction rules (drop photons within 1 s of a GPS-service failure;
drop photons above 9 keV because of an energy-recorder artefact), folds one
profile per observation with Jodrell Bank radio ephemerides, obtains phase
delays by FFT cross-correlation against a standard profile, resolves integer
cycle ambiguities from continuity, and corrects the initial phase and the
spin frequency and its first three derivatives by weighted least squares.
The post-fit RMS time residual is 55.94 μs and the 1σ error of the spin
frequency $1.76\times10^{-10}$ s⁻¹; the authors take this as verification
of the TSXS. Pulsar navigation is the application; there is nothing on
propulsion or plasma.

# Key claims

Symbols are the paper's (see the notation map).

1. **Spacecraft and instruments** (§1): XPNAV-1, 270 kg, 500 km LEO,
   launched on Long March 11 from Jiuquan; three-axis stabilized, 2 arcmin
   pointing, up to 90 min per target. TSXS: Wolter-I optic of 4 nested
   shells, about 10 cm² effective area, 15 arcmin field of view, silicon
   drift detector, GPS-calibrated Rb clock, 1.5 μs time resolution, 180 eV
   at 5.9 keV, 0.5–10 keV. The second instrument (collimated MCP detector,
   2° field of view, 1–10 keV, 100 ns, 1200 cm²) is not used here.
2. **Observations** (§2, Fig. 1): 162 missions, each about 3000 s, about six
   per day before 28 Dec 2016 (test and calibration) and about one per day
   after; pointing excludes the South Atlantic Anomaly (ref. [7]) and
   requires Sun and Moon angles above 45°; slewing starts 7 min before each
   observation.
3. **Data reduction** (§3, Fig. 2): photons within 1 s of a GPS failure
   (orbit-determination flag 0) are excluded; photons above 10 keV trigger
   events but are not energy-tagged, so the normalized spectrum rises above
   9 keV, and events above 9 keV are excluded. Shown and recommended.
4. **Frequency model** (Eq. 1):
   $f(t)=\sum_{i=0}^{2}F_i(t-T_{\mathrm{EFRQ}})^i/i!$, prefit parameters from
   Jodrell Bank (Table 1); 512 phase bins; arrival times transformed to the
   solar-system barycentre by standard procedures (refs. [8,9]).
5. **Folding** (§4.1): the epoch is placed at mid-observation to reduce the
   effect of spin-parameter error (ref. [12]); initial phase zero assumed at
   MJD 57715.
6. **Phase delay** (§4.2, Eqs. 2–6): cross-correlation
   $R_D(\phi)=\frac{1}{N_b}\sum_{j=1}^{N_b}h_j\tilde h_{j+\phi}$, maximised
   over $\phi\in[0,1)$ and evaluated by FFT; time residual
   $\delta\tilde t=(\tilde\phi_0+n)/f(t_0)$ with the integer $n$ fixed by
   continuity of neighbouring epochs. The pre-fit residual is at the
   $10^4$ μs level (Fig. 5), attributed to the assumed initial phase and the
   extrapolated ephemeris error.
7. **Ephemeris correction** (§4.3, Eqs. 7–11): the residual is linearized
   (neglecting the effect of the corrections on $f$) into
   $\mathbf Y=\mathbf H\mathbf X$ with
   $\mathbf X=[\Delta\phi_0,\Delta F_0,\Delta F_1,\Delta F_2,\Delta F_3]'$
   and rows of $\mathbf H$ equal to
   $[1/f,\ \Delta t_k/f,\ \Delta t_k^2/2f,\ \Delta t_k^3/6f,\ \Delta t_k^4/24f]$;
   weighted least squares with a diagonal $\mathbf W$ of phase-delay error
   variances from the Emadzadeh–Speyer formula (Eq. 11, ref. [14]), which
   the paper attributes and calls "proved" there.
8. **Result** (Table 2, Fig. 5, §5): $F_0=29.64726102428$ s⁻¹ (1σ
   $1.76\times10^{-10}$), $F_1=-3.6894800\times10^{-10}$ s⁻² (1σ
   $1.52\times10^{-16}$), $F_2=1.358\times10^{-20}$ s⁻³ (1σ
   $2.25\times10^{-22}$), $F_3=-2.48\times10^{-28}$ s⁻⁴ (1σ
   $9.65\times10^{-29}$), $\phi_0=-8.4\times10^{-4}$ (1σ
   $1.35\times10^{-4}$), reference epoch MJD 57733.610873554011; post-fit
   RMS residual 55.94 μs. Shown.
9. **Refolding** (§4.4, Fig. 6, attributed to ref. [15]): over the 163-day
   span a spin-frequency error above $10^{-9}$ s⁻¹ would smear the
   all-photon profile; the refolded profile is cleaner than the
   single-observation ones, from which the authors infer that the true
   ephemeris error is "better than" the estimation errors. A qualitative
   inference with no metric.

# Methods

TSXS data reduced with the DASS software (ref. [1]); barycentring by
standard procedures (refs. [8,9]); epoch folding (refs. [2,11]) with 512
bins and the extrapolated Jodrell Bank monthly Crab ephemeris (ref. [10]);
standard profile from the EPN database (ref. [13]); FFT cross-correlation
for phase delays; cycle ambiguity by continuity; five-parameter weighted
least squares with Eq. 11 weights, background and source photon rates chosen
"based on observation result", and the observation time reduced by the
GPS-failure skips. Energy band 0.5–9.0 keV.

# Tests and results

One case: the Crab, 162 TSXS observations, MJD 57709–57872. Figs. 3–4 show
flux and folded profiles for MJD 57809.515, 57810.635, 57811.555 and
57812.541 (about 13–21 counts/s); Fig. 5 the pre-fit (about $10^4$ μs) and
post-fit (RMS 55.94 μs) residuals; Table 2 the corrected ephemeris; Fig. 6
the refolded profile. No comparison with other X-ray missions' Crab timing,
no independent validation of the fitted ephemeris.

# Notation map

Pulsar-timing symbols; none has a registry counterpart.

| Huang et al. (2018) | Registry | Note |
|---|---|---|
| $f(t)$ | words (pulse frequency) | **collision:** registry $f_s$ is the distribution function, $f_\varepsilon$, $f_m$, $f_g$ scaling factors |
| $F_0$–$F_3$ | words (spin frequency and derivatives) | **collision:** registry $F$ is thrust |
| $T_{\mathrm{EFRQ}}$, $T_{\mathrm{obs}}$ | words (ephemeris epoch, observation interval) | not a temperature $T_s$ |
| $\phi$, $\phi_0$, $\Delta\phi_0$ | words (pulse phase, initial phase, its correction) | **collision:** registry $\phi$ is the electrostatic potential, $\Delta\phi_{\mathrm{sh}}$ the sheath drop |
| $h(\phi)$, $h_j$, $\tilde h_{j+\phi}$, $N_b$, $R_D$ | words (standard and folded profiles, bin count, cross-correlation) | |
| $n$ | words (integer cycle ambiguity) | **collision:** registry $n_s$ is number density |
| $\delta\tilde t$, $\Delta t$ | words (time residual, time from epoch) | **collision:** registry $\Delta t$ is the time step |
| $\mathbf H$, $\mathbf X$, $\mathbf Y$, $\mathbf W$ | words (least-squares matrix, unknowns, residuals, variance matrix) | **collision:** registry $H$ spectral entropy, $Y$ sputtering yield, $W$ macroparticle weight |
| $\lambda_b$, $\lambda_s$ | words (background and source photon rates) | **collision:** registry $\lambda$-family symbols are lengths |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Huang_A_new_explorer_mission_for_soft_X-ray_timing_-_Observation_o.pdf`.
   * **Version.** Publisher's version of record (Elsevier), 5 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.05.060, printed on page 1
     and checked on Crossref: title, all four authors, Acta Astronaut.
     151:63–67 match; issued 2018-10, no published-online field. Page 1:
     received 23 Mar 2017, revised 19 Jan 2018, accepted 30 May 2018, online
     31 May 2018. Page 1 matches the filename title. First of the three
     Huang 2018 files in archive-filename order, hence `huang-2018`.
   * **How it was read.** Full text layer; Eqs. 4–11 read on the rendered
     page 3. Figure data are not tabulated; only values quoted in the text
     are recorded.
   * **Recorded as printed.**
     * Eq. 10 is printed
       $\tilde{\mathbf X}=(\mathbf H'\mathbf W^{-1}\mathbf H)^{-1}\mathbf W^{-1}\mathbf H'\mathbf Y$,
       in which $\mathbf W^{-1}\mathbf H'$ (162 × 162 times 5 × 162) is
       undefined; the standard form is
       $(\mathbf H'\mathbf W^{-1}\mathbf H)^{-1}\mathbf H'\mathbf W^{-1}\mathbf Y$.
     * The text calls $\mathbf Y$ a vector of 162 residuals but writes it
       with index running to 139, as does the inline $\mathbf H$, while
       Eq. 8 runs to 162; the discrepancy is unexplained.
     * The text says $\mathbf Y$ is "calculated by Eq. (5)" (the residuals
       are Eq. 6) and defines $\Delta t$ "in Eq. (6)" (it appears in
       Eq. 7).
     * Eq. 3 defines the folded profile with the untilded standard profile
       $h$, which read literally makes the folded profile a shifted
       standard profile.
     * §4.4's "163 days of observation" against 162 observations over
       MJD 57709–57872: consistent (163 days inclusive, 162 missions).
     * $F_2$ changes sign from the prefit $-3.89\times10^{-20}$ (Table 1)
       to the fitted $+1.358\times10^{-20}$ (Table 2) with a 1σ of
       $2.25\times10^{-22}$, without comment. Reader's check: Table 1's
       $F_0$ propagated with $F_1$ from MJD 57715 to 57733.61 gives about
       29.647262 s⁻¹, consistent with Table 2.
     * Ref. [15] is printed "Atca Astronautica 12 (2016) 179–185"; volume
       12 is implausible for 2016, kept as printed. §4.4's fragment "[15].
       have proved" suggests a lost author name.
     * The abstract's apposition "Time-resolved soft X-ray spectrometer,
       X-ray pulsar navigation 1 satellite" is garbled; the affiliation
       prints "Space Technolog".
   * **Reference list.** 16 printed entries ([1]–[16]), matching the
     Crossref reference count. Entries without a printed year ([1], [6],
     [10], [13], [16]) are keyed with `-nd`; same-author-year pairs take
     suffixes in printed order (Edwards 2006, refs. [8], [9]; Emadzadeh
     2011, refs. [11], [14]).

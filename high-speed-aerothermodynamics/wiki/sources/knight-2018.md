---
type: Source
title: "Knight & Mortazavi (2018) — Hypersonic shock wave transitional boundary layer interactions - A review"
description: "Reviews hypersonic shock-wave/transitional-boundary-layer interaction research since 1993 over fourteen canonical configurations, proposes a four-class categorisation of interactions, shows that transitional interactions can exceed laminar and turbulent peak heating by factors up to about 3.7 over the Holden turbulent correlation, and names the tuned inflow forcing of DNS as the open problem."
resource: "doi:10.1016/j.actaastro.2018.06.019"
source_kind: paper
authors: [Knight D., Mortazavi M.]
year: 2018
venue: "Acta Astronaut. 151:296–317"
local_file: "/home/stefano/papers/mosaic/high-speed-aerothermodynamics/2018_Crossref_Acta_Astronautica_Knight_Hypersonic_shock_wave_transitional_boundary_layer_interactio.pdf"
tags: [swbli, transition, aeroheating, review, correlation, dns, benchmark]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

A review of research since 1993 on hypersonic shock-wave/transitional
boundary-layer interactions (SWTBLI). Fourteen groups of studies
(§§2.1–2.14), each with a freestream-condition table, cover the canonical
configurations: hollow-cylinder flare, compression ramp or corner, oblique
shock impinging on a flat plate, cylinder normal to a flat plate,
hemisphere-cylinder flare, sliced cone with ramp, and Edney III/IV
shock/shock interactions, in facilities including RWG, H2K, HEG, the
Boeing/AFOSR Mach-6 Quiet Tunnel and T-325. The paper reports no
experiment or simulation of its own. Its message: a transitional
interaction can produce a peak heat transfer well above both the laminar
and turbulent interactions of the same strength; interactions fall into
four classes by steadiness, dimensionality and spectrum; DNS is the most
promising prediction method but matched experiment only after *a
posteriori* tuning of an ad hoc inflow-disturbance amplitude, because
time-dependent inflow data for five variables cannot be measured. It
calls for collaborative work on dynamic inflow boundary conditions and on
transitional interactions at transonic and low supersonic Mach numbers.

# Key claims

1. **Four-class categorisation** (§1, Table 1, Figs. 1–4), "the general
   consensus": laminar steady (2-D/axisymmetric or 3-D); laminar unsteady
   (2-D or 3-D, discrete frequencies); transitional (unsteady, 3-D,
   discrete frequencies with a developing cascade to higher frequency);
   turbulent (unsteady, 3-D, broad spectrum). Stated.
2. **Roberts separation length** (§2.1, Eq. 1, attributed). Heffner et
   al.'s data at flare angles 10°, 20°, 30° "generally overpredict the
   correlation but show the same trend" (Fig. 5).
3. **Hung–Barnett peak heating** (§2.1, Eqs. 2–4, attributed): laminar,
   transitional and turbulent forms; against the Heffner data the
   transitional form underpredicts and the turbulent one agrees more
   closely (Fig. 6).
4. **Holden turbulent peak heating** (§2.5, Eq. 5, attributed), the
   baseline of Tables 6 and 9.
5. **Hollow-cylinder flare transitional peak** (§2.5, Table 6, Benay et
   al. / Bur & Chanetz): natural-transition peaks average 3.4 times the
   Holden value (ratios 3.2–3.7 over $\mathrm{Re}_L=0.405$–$2.031\times10^6$;
   peak ratio 12.4–14.5 against 3.9); a trip gives agreement with Holden;
   excess attributed by the original authors to Görtler vortices
   (Fig. 16); laminar axisymmetric Navier–Stokes underpredicts (Fig. 17);
   maximum N-factor 1.0 against 2–4 for transition in that tunnel.
6. **Shock/shock heating** (§2.3, Fig. 11, attributed to Holden et al.):
   peak ratio below 10 for $\mathrm{Re}_D<10^4$, rising rapidly above, sharp
   increase at shear-layer Reynolds number about 2000.
7. **Mach-6 impinging shock** (§2.7, Table 9, Willems et al.): at
   impingement Reynolds numbers 1, 2, $4\times10^6$ the peak ratios 8.1,
   5.4, 2.8 are 3.2, 2.2, 1.1 times Holden (2.5): transitional, then
   turbulent. Wall pressure not measured.
8. **Sandham et al. DNS and experiment** (§2.9, Figs. 27–28): peak
   Stanton number reached when the boundary layer is transitional at
   impingement; DNS matched RWG only with the high forcing amplitude,
   tuned *a posteriori*.
9. **Schülein intermittency correlation** (§2.10, Eqs. 9–10, Fig. 30):
   peak at intermittency about 0.1, nearly three times the fully turbulent
   peak.
10. **Quiet vs noisy freestream** (§2.11, Fig. 32, Table 13): noisy flow
    moves transition onto the cone (x ≈ 0.28 m) and halves the peak ramp
    heat transfer; the quiet case shows a curved reattachment line at
    x ≈ 0.4 m.
11. **Shock-foot unsteadiness** (§2.12, Figs. 35–37, Mach 2.01): position
    PDFs significantly broader for transitional than turbulent inflow;
    skewness −1.88 and kurtosis 6.99 at x/D = 8.5.
12. **Cylinder-induced separation distance** (§2.6, Fig. 20): decreases
    monotonically from laminar through transitional to turbulent; about
    two diameters for turbulent inflow.
13. **Turbulent spots** (§2.8, Mach 8.9): spot heat transfer 4–5 times
    laminar, convection speed 0.66–0.69 of the edge velocity, spots remove
    flare-induced separation over their azimuthal extent.
14. **Leading-edge bluntness** (§2.13, Mach 2.5): a weak N-wave shock
    raises the peak mass-flow fluctuation from 1.4% to 2.5% (sharp) and to
    9.3% (blunt, 2.5 mm radius).
15. **Protuberance** (§2.14, Fig. 41, Mach 6): the no-protuberance peak
    rises then falls with unit Reynolds number (laminar → transitional →
    turbulent); a protuberance of height $0.6\delta$ and width $2\delta$
    raises the peak at the highest Reynolds number.
16. **Conclusion** (§3): DNS is the most promising method; dynamic inflow
    conditions for five variables are presently infeasible to measure; the
    tuned ad hoc disturbance is the open problem. The paper's own
    assessment.

# Methods

Review; no facility or computation of its own. Each section tabulates the
cited study's model, diagnostics and freestream conditions (Tables 2–15):
Heffner et al. 1993 ($\mathrm{Ma}_\infty=4.96$, 150 mm hollow cylinder,
flares 10°/20°/30°); Holden & Chadwick 1995 (curved ramp, Mach 10–11.94;
GASP with Baldwin–Lomax and imposed transition); Balakumar et al. 2005
(computational 5.5° corner, Mach 5.373, fifth-order WENO on 1001×301 and
1701×301 grids plus linear stability); Benay et al. 2006 / Bur & Chanetz
2009 (hollow cylinder + 15° flare, Mach 5, 52 pressure taps and 52
thermocouples); Murphree et al. 2006/07 (cylinder on plate, Mach 5);
Willems et al. (4° wedge on flat plate, Mach 6, IR thermography and
gauges); Estruch-Samper et al. / Vanstone et al. (hemisphere-cylinder +
8° flare, N₂, Mach 8.9); Sandham et al. 2014 (RWG, H2K, HEG; DNS of 8 runs
on $2401\times232\times360$ points with a random inflow density
perturbation); Schülein 2014 (Mach 5.96, QIRT); Edelman et al. / Gray et
al. (BAM6QT, quiet and noisy); Lash et al. / Combs et al. (Mach 2.01);
Vaganov et al. 2016 (T-325, Mach 2.5); Leidy et al. 2017 (Mach 6 and 7).
Only Balakumar's two successive grids constitute a grid study; no
uncertainties are quoted.

# Tests and results

The numbers of the reviewed cases are collected on
[Peak heating of transitional shock/boundary-layer interactions](/results/transitional-swbli-peak-heating.md)
and
[Shock-wave/boundary-layer interaction](/definitions/shock-wave-boundary-layer-interaction.md).
Further items: on a 7° cone at Mach 7.95 the peak mass-flux fluctuation
grows and broadens around 100 kHz downstream (§1, Fig. 2); on the curved
ramp transition onset moves upstream with Reynolds number, and GASP with
Baldwin–Lomax is accurate in the laminar region but only modest in the
turbulent region (§2.2, Figs. 8–9); in the computational corner flow
high-frequency disturbances grow uniformly outside the separation and in
a narrow region inside it (§2.4, Figs. 12–14).

# Notation map

| Knight & Mortazavi (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $M_\infty$ | $\mathrm{Ma}_\infty$ | |
| $Re_\infty$ (per metre), $Re_L$, $Re_D$, $Re_\delta$, $Re_x$ | $\mathrm{Re}$ with stated length scale | |
| $p_{t\infty}$, $T_{t\infty}$ | $p_{0,\infty}$, $T_{0,\infty}$ | paper subscript $t$ = total |
| $T_w$, $q_w$ | $T_w$, $q_w$ | |
| $q_{w\,max}$, $q_{max}$; $q_{w\infty}$, $q_{ref,lam}$, $q_{ref,turb}$ | $q_{w,\max}$; $q_{w,\mathrm{ref}}$ | peak and undisturbed wall heat flux; not yet in the registry |
| $p_2/p_1$, $p_{max}/p_\infty$ | words / $p_2/p_1$, $p_{\max}/p_\infty$ | inviscid pressure ratio across the interaction; peak pressure |
| $St$ | $\mathrm{St}$ | referenced to $\rho_\infty u_\infty$, specific heat and recovery-temperature difference (Eq. 7) |
| $T_r$, $r$, $c_p$ | words | recovery temperature, recovery factor, specific heat; **collision:** registry $C_p$ is the pressure coefficient |
| $\gamma_{imp}$ | words (intermittency) | **collision** with $\gamma$ |
| $\gamma_1$, $\gamma_2$; $\mu$, $\sigma$ of the PDFs | words | **collisions** with $\gamma$, $\mu$, $\sigma_0$ |
| $L_{sep}$, $\ell_{sep}$ | $L_{\mathrm{sep}}$ | |
| $\Delta x_{tr}$, $x_{trans}$ | words | transition length, end-of-transition station |
| $U_\infty$, $U_e$, $U_s$ | $u_\infty$; words | edge and spot velocity |
| $a$ (DNS forcing amplitude, Eq. 6) | words | **collision** with the speed of sound $a$ |
| $F=2\pi\nu_\infty f/U_\infty^2$, $N$ | words | non-dimensional frequency, amplification factor |

# Pages created or updated

* [Shock-wave/boundary-layer interaction](/definitions/shock-wave-boundary-layer-interaction.md)
* [Peak heating of transitional shock/boundary-layer interactions](/results/transitional-swbli-peak-heating.md)

# Citations

1. `/home/stefano/papers/mosaic/high-speed-aerothermodynamics/2018_Crossref_Acta_Astronautica_Knight_Hypersonic_shock_wave_transitional_boundary_layer_interactio.pdf`.
   * **Version.** Publisher's final typeset PDF, 22 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.019, printed on page 1
     and checked on Crossref: title, authors, Acta Astronaut. 151:296–317;
     issue October 2018 (issued and published-print 2018-10, no
     published-online field); page 1 prints received 14 Jan 2018,
     revised 1 Jun 2018, accepted 5 Jun 2018, online 15 Jun 2018. Page 1
     title matches the filename. The file was first filed in the
     plasma-propulsion archive; the paper has no plasma content.
   * **How it was read.** Full text layer; PDF pages 2, 4, 11, 12 and 13
     rendered for Table 1 and Eqs. 1–10, all read cleanly (the text layer
     drops the square root in the laminar recovery factor
     $r=\sqrt{\mathrm{Pr}}$ of Eq. 8, restored from the rendered page).
     Figure contents are images; only numbers stated in the text were
     taken, and Fig. 20 was read only for its axis label and range.
   * **Recorded as printed.**
     * Fig. 20: text and caption give the ordinate as separation distance
       over boundary-layer thickness; the plotted axis label normalises by
       cylinder diameter, and §2.6 speaks of "two diameters".
     * Footnote 4 gives the transition location as 10.414 mm, which
       cannot match the cylinder positions (69.85–127 mm) and the 0–2
       range of Fig. 20; possibly 104.14 mm, not verifiable.
     * §2.9 defines $St_{lam}$ a second time as the Stanton number at the
       impingement location without shock, apparently meaning $St_{tr}$.
     * Footnote 2 cites "Potter and Whitfield [8] and Michel [9]"; ref. [8]
       is Potter alone and ref. [9] is Gilly, Rosenthal & Sémézis.
     * Ref. [10] Hung & Barnett is printed "AIAA Paper 72-237 … January
       1973"; the DOI 10.2514/6.1973-237 (Crossref issued 1973-01-10)
       shows the paper number is the slip.
     * Ref. [46] Davidson & Babinsky is printed "AIAA Paper 2015-1975 …
       January 2014"; Crossref gives 2015-01-02 and a slightly different
       title.
     * Table 11 cites Schülein for its RWG values ($\mathrm{Ma}_\infty=5.98$,
       unit Reynolds number from 2.8) while Table 12 (Schülein) prints
       5.96 and 2.83.
     * Table 3 gives Mach up to 11.94 and unit Reynolds number from
       $1.04\times10^6$ m⁻¹; the §2.2 text and Fig. 9 give 11.85 and 11.92
       and $1.87\times10^6$ m⁻¹ at Mach 10.
     * Table 11 wall-to-freestream temperature ratio 0.7 for HEG against
       4.5 and 4.7 for RWG and H2K, uncommented.
     * Fig. 40 caption "Impinging Shock [34]" for the Leidy et al. [44]
       geometry.
     * Typos: "Holden and Chadwich" (§2.2 heading), "Murphree et al., 2006
       and 207" (Table 7), "s/D = 25" (Fig. 35(b)), "Layes" (ref. [31]).
   * **Reference list.** 54 printed entries ([1]–[54]), equal to the
     Crossref reference-count. Refs. [29] (Willems et al.) and [48]
     (Giepman et al.) print no year.

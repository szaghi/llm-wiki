---
type: Source
title: "Knight & Mortazavi (2018) — Hypersonic shock wave transitional boundary layer interactions - A review"
description: "Reviews hypersonic shock-wave/transitional-boundary-layer interaction research since 1993 in 14 groups of studies, proposes a four-class categorisation of interactions, documents that transitional interactions can exceed laminar and turbulent peak heating, and judges DNS the most promising predictor, limited by ad hoc inflow forcing."
resource: "doi:10.1016/j.actaastro.2018.06.019"
source_kind: paper
authors: [Knight D., Mortazavi M.]
year: 2018
venue: "Acta Astronaut. 151:296–317"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Knight_Hypersonic_shock_wave_transitional_boundary_layer_interactio.pdf"
tags: [context, review, hypersonic, shock-boundary-layer-interaction, aeroheating]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

A review of research since 1993 on hypersonic shock-wave/transitional
boundary-layer interactions (SWTBLI), organised as 14 groups of cited
studies (§§2.1–2.14), each with a freestream-conditions table. The
configurations are the canonical ones: hollow-cylinder flare,
compression ramp or corner, impinging oblique shock on a flat plate,
cylinder normal to a flat plate, hemisphere-cylinder flare, sliced cone
with ramp, and Edney III/IV shock/shock interactions. The review reports
no experiment or simulation of its own. Its message: a transitional
interaction can produce a peak surface heat flux well above both the
laminar and the turbulent interaction of the same strength; interactions
fall into four classes by steadiness, dimensionality and spectrum
(Table 1); DNS is the most promising prediction method, but it matched
experiment only after an *a posteriori* tuning of an ad hoc inflow
disturbance amplitude, because time-dependent inflow data for five
variables cannot be measured. It calls for collaborative work on dynamic
inflow boundary conditions and for SWTBLI studies at transonic and low
supersonic Mach numbers.

# Key claims

Symbols below are the paper's own (see the notation map). Everything
except claim 1 and claim 16 is attributed to the cited works.

1. **Four-class categorisation** (§1, Table 1), presented as "the general
   consensus": laminar steady (2-D/axisymmetric or 3-D); laminar unsteady
   (2-D or 3-D; discrete frequencies); transitional (unsteady, 3-D;
   discrete frequencies with a developing cascade to higher frequency,
   typically with downstream distance); turbulent (unsteady, 3-D; broad
   spectrum). Illustrated by Figs. 1–4.
2. **Roberts separation-length correlation** (§2.1, Eq. 1, attributed):
   $L_{sep}M_\infty^{3/2}/\Delta x_{tr}\approx\sqrt{p_2/p_1}$, with
   $\Delta x_{tr}$ the flat-plate transition length. Heffner et al.'s data
   (flares of 10°, 20°, 30°) "generally overpredict the correlation but
   show the same trend" (Fig. 5).
3. **Hung & Barnett peak-heating correlations** (§2.1, Eqs. 2–4,
   attributed): laminar $q_{max}/q_{ref,lam}=0.13(p_2/p_1)^{1.13}$;
   transitional $q_{max}/q_{ref,lam}=0.468(Re_L\times10^{-6})(p_2/p_1)^{1.13}$;
   turbulent $q_{max}/q_{ref,turb}=(p_2/p_1)^{0.80}$, with $p_2/p_1$ the
   inviscid surface pressure ratio across the shock. Against the Heffner
   data (Fig. 6) the transitional correlation underpredicts the peak; the
   turbulent one agrees more closely.
4. **Holden turbulent peak-heating correlation** (§2.5, Eq. 5,
   attributed): $q_{w\,max}/q_{w\infty}=(p_{max}/p_\infty)^{0.85}$.
5. **Transitional peak on the hollow-cylinder flare** (§2.5, Table 6,
   Benay et al. / Bur & Chanetz): "natural"-transition peaks average 3.4
   times the Holden value; Table 6 ratios 3.2–3.7 over
   $Re_L=0.405$–$2.031\times10^6$, with $q_{w\,max}/q_{w\infty}=12.4$–14.5
   against 3.9 from Holden. A trip forcing a turbulent inflow gives a peak
   close to Holden. The excess is attributed by the original authors to
   Görtler vortices (Fig. 16); laminar axisymmetric Navier–Stokes runs
   substantially underpredict the peak (Fig. 17); the maximum
   linear-stability N-factor was 1.0, against N = 2–4 for transition in
   that tunnel.
6. **Edney III/IV shock/shock heating** (§2.3, Fig. 11, Holden et al.):
   $q_{max}/q_{ref}<10$ for $Re_D<10^4$, rising rapidly above it
   (presumably transition of the shear layer and/or attaching jet); a sharp
   increase at shear-layer Reynolds number $Re_\delta\approx2000$.
7. **Incident shock on a flat plate at Mach 6** (§2.7, Table 9, Willems et
   al.): with $x_{shock}=331$ mm and $Re_{shock}=1$, 2, 4 ×10⁶,
   $q_{w\,max}/q_{w\infty}=8.1$, 5.4, 2.8 against Holden's 2.5
   ($p_{max}/p_\infty=2.96$, inviscid): factors 3.2, 2.2, 1.1, i.e.
   transitional at the two lower and turbulent at the highest Reynolds
   number. Wall pressure was not measured (footnote 5).
8. **Peak Stanton number at transitional impingement** (§2.9, Fig. 28b,
   Sandham et al. DNS and experiment): $St_{max}/St_{lam}$ peaks when the
   boundary layer is transitional at impingement; the abscissa
   $(St_{tr}-St_{lam})/(St_{tur}-St_{lam})$ is an intermittency factor,
   $St_{tur}$ from Van Driest II.
9. **Schülein intermittency correlation** (§2.10, Eqs. 9–10, Fig. 30,
   attributed): $\gamma_{imp}=(St_{imp}-St_{lam})/(St_{tr}-St_{lam})$ with
   $St_{tr}=5.5\,St_{lam}$; the peak $St_{max}/St_{w/o}$ occurs at
   $\gamma_{imp}\approx0.1$ (early transition) and is nearly three times the
   fully turbulent value ($\gamma_{imp}\approx1$).
10. **Quiet vs noisy freestream** (§2.11, Fig. 32, Table 13; 7° sliced cone
    with 30° ramp in the BAM6QT): under noisy flow transition occurs on the
    cone (x ≈ 0.28 m) and the peak ramp heat transfer is about half the
    quiet-flow level; the quiet case shows a curved reattachment line at
    x ≈ 0.4 m.
11. **Shock-foot unsteadiness** (§2.12, Figs. 35–37, Mach 2.01): the PDFs of
    forward-shock and upstream-influence-shock position are significantly
    broader for transitional inflow (x/D = 6, 8, 12) than for turbulent
    inflow (x/D = 25); at x/D = 8.5 the separation-location PDF has the
    largest skewness (−1.88) and kurtosis (6.99), implying upstream
    excursions.
12. **Cylinder-induced separation distance** (§2.6, Fig. 20): the
    normalised upstream separation distance decreases monotonically from
    laminar through transitional to turbulent inflow; about two diameters
    for turbulent inflow, the transitional case midway.
13. **Turbulent spots** (§2.8, Figs. 24–25, Mach 8.9 hemisphere-cylinder
    with 8° flare): spot heat transfer typically 4–5 times laminar;
    convection speed $U_s\approx0.66$–$0.69\,U_e$; spots eliminate
    flare-induced separation over their azimuthal extent; without
    roughness the whole flow is laminar.
14. **Leading-edge bluntness** (§2.13, Figs. 38–39, Mach 2.5,
    $Re=4.9\times10^6$ m⁻¹): a weak N-wave shock raises the peak mass-flow
    fluctuation from 1.4% (no shock) to 2.5% with the sharp and to 9.3%
    with the blunt (2.5 mm radius) leading edge.
15. **Protuberance-perturbed interactions** (§2.14, Fig. 41, Mach 6): the
    no-protuberance peak heat flux rises from $Re=2.9$ to $4.3\times10^6$
    m⁻¹ and falls at $6.5\times10^6$ m⁻¹ (laminar → transitional →
    turbulent inflow); a protuberance of height 0.6δ and width 2δ
    significantly increases the peak at the highest Reynolds number.
16. **Assessment** (§3, abstract), the authors' own: DNS is the most
    promising methodology and "has successfully reproduced experimental
    surface heat transfer distributions"; it needs dynamic inflow boundary
    conditions for five variables (three velocity components, two
    thermodynamic variables), presently infeasible to measure; the ad hoc
    disturbance with a free parameter tuned to experiment is the open
    problem. Stated.

# Methods

A review: no facility and no computation of its own. Summarised from the
cited works (conditions as printed in Tables 2–15):

* Heffner et al. 1993 (Table 2): hollow-cylinder flare, $M_\infty=4.96$,
  $T_{t\infty}=453$ K, $p_{t\infty}=0.86$ MPa, $Re_\infty=12.8\times10^6$
  m⁻¹, $T_w=293$ K.
* Holden & Chadwick 1995 (Table 3): curved compression surface,
  $M_\infty=10.0$–11.94; computations with GASP and Baldwin–Lomax eddy
  viscosity, transition imposed at the measured location.
* Balakumar et al. 2005 (Table 4): numerical 5.5° compression corner,
  $M_\infty=5.373$, $Re_\infty=17.9\times10^6$ m⁻¹; fifth-order WENO steady
  flow on 1001×301 and 1701×301 grids, then parallel-flow linear stability.
* Benay et al. 2006 / Bur & Chanetz 2009 (Table 5): hollow cylinder with
  15° flare, $M_\infty=5$, $Re_\infty=1.1$–$8.8\times10^6$ m⁻¹, 52 pressure
  taps and 52 thermocouples; laminar axisymmetric Navier–Stokes and
  N-factor analysis.
* Murphree et al. (Table 7), Lash et al. / Combs et al. (Table 14), Leidy
  et al. (Table 15): cylinder-induced interactions at Mach 5, 2.01, 6 and 7.
* Willems et al. (Table 8), Sandham et al. (Table 11), Schülein (Table 12):
  impinging shock from a 4° generator on a flat plate at Mach ≈ 6 (RWG,
  H2K, HEG). Sandham's DNS: 8 runs on a 2401×232×360 grid (200 M points),
  laminar similarity inflow plus the random density forcing of Eq. 6
  ($J=16$, $K=20$, $f_k=0.02k$, random phases), amplitude tuned
  *a posteriori* and different for RWG and H2K; scheme and code not stated
  in the review.
* Estruch-Samper / Vanstone (Table 10): hemisphere-cylinder flare in N₂ at
  $M_\infty=8.9$, $p_{t\infty}=60.8$ MPa.
* Edelman / Gray (Table 13): sliced cone with ramp, quiet and noisy runs in
  the BAM6QT. Vaganov et al. (§2.13): T-325, Mach 2.5.
* Stanton number (Eq. 7) $St=q_w/(\rho_\infty U_\infty c_p(T_r-T_w))$;
  recovery temperature (Eq. 8) $T_r=T_\infty(1+\frac{\gamma-1}{2}rM_\infty^2)$
  with $r=\sqrt{Pr}$ (laminar).

No grid-independence study beyond Balakumar's two grids; no uncertainties
quoted.

# Tests and results

All cases are those of the cited works; their numbers are in Key claims
2–15. Additional: §1, Fig. 2 (7° cone at $M_\infty=7.95$; mass-flux
fluctuation peak grows around 100 kHz downstream); §2.2, Figs. 8–9
(transition onset moves upstream with Reynolds number; GASP with imposed
transition accurate in the laminar region, modest in the turbulent one);
§2.4, Figs. 12–14 (separated corner flow; high-frequency disturbances
$F=0.8\cdot10^{-4}$ grow outside the separation, inside it only in a
narrow region); §2.9, Figs. 27–28 (high-amplitude DNS agrees with RWG at
$4\times10^6$ m⁻¹, lower amplitudes underpredict); §3 (pointers to
transonic and low-supersonic studies at Mach 1.2, 1.47, 1.7).

# Notation map

The paper's symbols are those of compressible aerodynamics; few have a
counterpart in this bundle's notation registry.

| Knight & Mortazavi (2018) | Registry | Note |
|---|---|---|
| $M_\infty$ | words (freestream Mach number) | |
| $Re_\infty$, $Re_L$, $Re_D$, $Re_\delta$, $Re_x$, $Re_{imp}$, $Re_{shock}$ | words (Reynolds number, length scale stated) | |
| $p_{t\infty}$, $T_{t\infty}$ | words (stagnation pressure and temperature) | |
| $T_w$ | $T_w$ | wall temperature |
| $q_w$, $q_{w\,max}$, $q_{w\infty}$, $q_{ref,lam}$, $q_{ref,turb}$ | words (wall heat flux, peak, reference) | not the heat-flux vector $\mathbf q_s$ |
| $p_2/p_1$, $p_{max}/p_\infty$ | words (interaction pressure ratios) | |
| $St$, $c_p$, $Pr$ | words | |
| $T_r$, $r$ | words (recovery temperature and factor) | **collision:** registry $r$ is the radial coordinate |
| $\gamma$ (Eq. 8) | $\gamma$ | ratio of specific heats |
| $\gamma_{imp}$ | words (intermittency) | **collision** with $\gamma$ |
| $\gamma_1$, $\gamma_2$, $\mu$, $\sigma$ (PDF moments) | words | **collisions** with $\gamma$ and $\mu_\perp$ |
| $\nu_\infty$ | words (kinematic viscosity) | **collision** with collision frequencies $\nu_{sk}$ |
| $F=2\pi\nu_\infty f/U_\infty^2$ | words (non-dimensional frequency) | **collision:** registry $F$ is thrust |
| $k_w$ | words (wall thermal conductivity) | **collision:** registry $k$ is a wavenumber |
| $\delta$, $L_{sep}$, $\Delta x_{tr}$, $N$ | words | |
| $U_\infty$, $U_e$, $U_s$ | words | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Knight_Hypersonic_shock_wave_transitional_boundary_layer_interactio.pdf`.
   * **Version.** Publisher's final typeset PDF, 22 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.019, printed on page 1
     and checked on Crossref: title, authors, Acta Astronaut. 151:296–317
     match; issue October 2018 (no published-online field on Crossref);
     page 1 gives received 14 Jan 2018, revised 1 Jun 2018, accepted 5 Jun
     2018, online 15 Jun 2018. Page 1 matches the filename title.
   * **How it was read.** Full text layer; Table 1 and Eqs. 1–10 checked
     on rendered pages 2, 4, 11–13, all legible (the text layer drops the
     root in $r=\sqrt{Pr}$, restored from the rendered page). Figure
     contents (spectra, heat-flux curves, PDFs) were not digitised; only
     numbers stated in the text are recorded.
   * **Recorded as printed.**
     * Fig. 20: text and caption give the ordinate as $\ell_{sep}/\delta$,
       the plotted axis reads $\lambda_{sep}/d$ (cylinder diameter), and
       §2.6 speaks of "two diameters".
     * Footnote 4 gives $x_{trans}=10.414$ mm, which with cylinder
       positions 69.85–127 mm is incompatible with Fig. 20's abscissa
       range 0–2 (104.14 mm would fit; not verifiable).
     * §2.9 defines $St_{lam}$ a second time as the Stanton number "at the
       impinging shock location in the absence of the shock", evidently
       meaning $St_{tr}$.
     * Footnote 2 cites "Potter and Whitfield [8] and Michel [9]", but
       ref. [8] is Potter alone and ref. [9] is Gilly, Rosenthal & Sémézis.
     * Ref. [10] (Hung & Barnett) is printed "AIAA Paper 72-237 … January
       1973"; Crossref gives 1973-01-10 for doi:10.2514/6.1973-237, so the
       paper number is the slip.
     * Ref. [46] (Davidson & Babinsky) is printed "AIAA Paper 2015-1975 …
       January 2014"; Crossref gives 2015-01-02 and a different title
       wording ("Transition location effects on …").
     * Table 11 credits the RWG values to Schülein, yet prints
       $M_\infty=5.98$ and $Re_\infty$ from 2.8, against 5.96 and 2.83 in
       Table 12.
     * Table 3 prints $M_\infty$ up to 11.94 and $Re_\infty$ from
       $1.04\times10^6$ m⁻¹; the text gives 11.85 and 11.92, and
       $1.87\times10^6$ m⁻¹ at Mach 10.
     * Table 11 prints $T_w/T_\infty=0.7$ for HEG against 4.5 and 4.7 for
       RWG and H2K, without comment (plausible, not a slip).
     * The Fig. 40 caption reads "Impinging Shock [34]" for the Leidy et al.
       [44] protuberance geometry.
     * Typos: "Holden and Chadwich" (§2.2 heading), "2006 and 207"
       (Table 7), "s/D = 25" (Fig. 35b), "Layes" (ref. [31]).
   * **Reference list.** 54 printed entries ([1]–[54]), matching the
     Crossref reference count. Refs. [29] (Willems et al.) and [48]
     (Giepman et al.) print no year; Crossref gives 2015 for both.

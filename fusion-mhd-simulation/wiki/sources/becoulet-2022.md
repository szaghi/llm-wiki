---
type: Source
title: "Becoulet et al. (2022) — Non-linear MHD modelling of edge localized modes suppression by resonant magnetic perturbations in ITER"
description: "First nonlinear JOREK simulations of ELM suppression by N = 2, 3, 4 RMPs in ITER 15, 12.5 and 10 MA H-mode scenarios with MARS-F-optimized coil phasing: suppression threshold of about 45–60 kAt (coil limit 90 kAt), QH-like locking at 10 MA, linear/nonlinear X-point displacement comparison, and split 3D divertor footprints."
resource: "doi:10.1088/1741-4326/ac47af"
source_kind: paper
authors: [Becoulet M., Huijsmans G.T.A., Passeron C., Liu Y.Q., Evans T.E., Lao L.L., Li L., Loarte A., Pinches S., Polevoi A., Hosokawa M., Kim S.K., Pamela S.J.P., Futatani S., JOREK Team]
year: 2022
venue: "Nucl. Fusion 62:066022"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2022_Crossref_Nuclear_Fusion_Becoulet_Non-linear_MHD_modelling_of_edge_localized_modes_suppression.pdf"
tags: [mhd, reduced-mhd, extended-mhd, elm, pedestal, tokamak, divertor, edge, code]
timestamp: 2026-10-16T00:00:00Z
---

# Summary

The paper presents the first nonlinear MHD simulations of
[ELM](/definitions/edge-localized-mode.md) suppression by resonant magnetic
perturbations (RMPs) for ITER, run with [JOREK](/software/jorek.md), on
three ASTRA-modelled H-mode scenarios at $B_\phi=5.3$ T: 15 MA, 12.5 MA and
10 MA (high-$\beta_p$ steady state), with toroidal rotation from NBI
momentum input. The two-fluid JOREK model is used with $T_i=T_e$, toroidal
rotation, diamagnetic effects and neoclassical poloidal friction, in a
domain extending to the ITER wall with Bohm
[sheath conditions](/methods/sheath-boundary-conditions.md) at the divertor
targets. Vacuum RMP fields of the 3×9 ITER in-vessel coils are computed with
ERGOS, imposed at the wall boundary and ramped over a few ms; the coil
phasing is the MARS-F optimum that maximizes the linear-response
displacement near the X-point. Natural ELMs (harmonics $n=1$–9 from noise)
lose 4 MJ (15 MA) and 2 MJ (12.5 MA); the 10 MA case shows a rotating
$n=3$ QH-mode-like state without ELM crash. With $n=3$ RMPs at 15 MA,
suppression needs a peak coil current above about 45 kAt (coil maximum
90 kAt); above it the RMP harmonic and its side harmonics $n\cdot k$
dominate and the other harmonics saturate into "edge MHD turbulence".
$n=2$, 3 and 4 RMPs at 60 kAt all avoid crashes. At 10 MA the $n=3$ mode
locks to the static RMP. The JOREK X-point displacement is about 6–8 mm in
the early single-harmonic phase, close to MARS-F (about 7 mm), and about
60 mm later in the multi-harmonic phase. Divertor footprints show $n$-fold
splitting extending about 20 cm (inner) and 40 cm (outer), with heat fluxes
of about 5 to 1 MW m⁻² once normalized to 50 MW into the divertor; about
1 MW m⁻² at the outer baffle/first-wall junction is flagged as a concern
during the RMP switch-on transient. The local file is the IAEA FEC 2020
manuscript, not the published article (see Citations).

# Key claims

1. **Suppression threshold, 15 MA, $n=3$** (§4, Fig. 5; Abstract; §8). "For
   an RMP coil current larger than 45kAt" the RMP harmonic $n=3$ and the
   most strongly coupled $n=6,9$ dominate and the others stay at noise
   level; Abstract and §8 give "45kAt-60kAt" against a 90 kAt coil maximum.
   Shown.
2. **Below threshold** (§4). RMPs "usually decrease" the growth rates, but
   the ELM harmonics keep growing and "eventually produce an ELM crash".
   Shown.
3. **$n=2,3,4$ at 60 kAt** (§4, Fig. 7). All mitigate strongly and avoid
   crashes; side harmonics $n\cdot k$ couple most strongly; other harmonics
   are driven nonlinearly and saturate, "providing edge MHD turbulence
   instead of ELM crashes", at a higher level for $n=2$ and 4 than for
   $n=3$. Shown.
4. **Ergodization falls with $n$** (§4, Fig. 8). At fixed coil current the
   main-harmonic magnetic energy and the edge ergodization decrease with
   $n$, explained by higher-$m$ resonances at the edge ($q=m/n$) and a
   perturbation decaying from the coils as $\sim1/d^m$ ($d$ the distance
   from the coils). Energies Shown; explanation Stated.
5. **Profiles with RMPs** (§4, Figs. 9–10). Energy transport "slightly
   decreases with increased" $n$; density transport is "almost the same";
   density transport is convective ($E\times B$), energy transport
   conductive. Shown.
6. **Faster rotation** (§4, Fig. 6). With the faster 15 MA rotation profile
   and an $n=3,6$ spectrum at 60 kAt, suppression is "very similar"; without
   RMPs $n=6,7,8$ are most unstable. Shown.
7. **Natural ELMs** (§3, Figs. 2–3). 15 MA: low $n=2,3,4$ most unstable,
   4 MJ loss; 12.5 MA: $n=5$ precursor then $n=7,9$, 2 MJ loss; 10 MA: $n=3$
   stays most unstable, "QH-mode like behavior without ELM crashes". Shown.
8. **Mode rotation** (§3, Fig. 4). Two-fluid diamagnetic effects and toroidal
   rotation are "the most important factors" for the observed rotation of
   [ballooning modes](/definitions/ballooning-mode.md) before the crash and
   between ELMs; the 10 MA $n=3$ structure rotates in the electron
   diamagnetic (or $E\times B$) direction. Rotation Shown; importance
   Attributed (refs. [6, 14]).
9. **Locking at 10 MA** (§5, Figs. 11–13). With $n=3$ RMPs at 20 and 40 kAt
   the plasma behaves QH-like and the main $n=3$ harmonic locks to the
   static RMP "after few ms", later at smaller amplitude; strong density
   transport, almost unchanged $T_e$, "typical for QH-modes". Shown.
10. **12.5 MA, $n=3$, 60 kAt** (§5, Figs. 14, 16). Suppression; density
    transport exceeds energy transport, "observed also in many RMP
    experiments". Shown.
11. **X-point displacement, linear vs nonlinear** (§6, Figs. 17–18). MARS-F
    with optimum phasing: about 7 mm at $\psi_N\approx0.99$ near the X-point
    at 60 kAt (figure drawn at 30 kAt); non-optimum phasing reaches the same
    at about 80 kAt. JOREK early single-$n=3$ phase (<6.2 ms): about 6 mm
    (optimum, 60 kAt) and 8 mm (non-optimum, 80 kAt), "very similar";
    later multi-harmonic phase (>17 ms): about 60 mm ("not shown here").
    Shown, except the 60 mm value (Stated).
12. **Displacement criterion** (§1, §6). "The maximum perpendicular magnetic
    surface displacement near X-point with linear MHD plasma response gives
    better predictions for ELM suppression in experiment" than the vacuum
    island-overlap (Chirikov) criterion. Attributed (Liu et al. 2016).
13. **Minimum model** (§1). Realistic X-point and SOL geometry, realistic RMP
    coils and spectrum, toroidal rotation, two-fluid diamagnetic effects and
    neoclassical poloidal friction; the external kink-peeling response is
    "an important factor for ELM suppression". Stated, on earlier AUG and
    KSTAR validation (refs. [5–7]).
14. **Divertor footprints, 15 MA** (Abstract, §7, Figs. 10, 19–20). $n$-fold
    splitting; radial extension about 20 cm (inner) and 40 cm (outer);
    normalized heat flux from about 5 MW m⁻² at the strike point (5–6 in §8)
    to about 1 MW m⁻² at the outer baffle/first-wall junction; particle
    fluxes rise with RMPs but are not stationary. Shown, under the 50 MW
    normalization.
15. **Other scenarios** (§7, Figs. 21–22). At 10 MA no clear inner-divertor
    splitting; at 12.5 and 10 MA about 1 MW m⁻² at the outer
    baffle/first-wall junction. Shown.
16. **Design limits** (§7–8). Stationary LFS RMP heat fluxes are within
    target <10, baffle <5 and first-wall about 1 MW m⁻²; during switch-on
    they "can be much larger" since confinement loss reaches 20% in
    experiments. Limits and transient Stated; stationary values Shown.
17. **Simulated time** (§7). "~few tens of ms" against >3 s confinement time,
    because of "the small Alfven-like time steps needed … even with a fully
    implicit scheme". Stated.
18. **Resistivity** (§2). $\eta_0=10^{-7}$ (JOREK units) is "about of two
    orders higher" than the realistic central ITER value at 15 MA "because
    of state-of-art numerical limitations"; other dissipation parameters are
    "rather close to realistic". Stated.

# Models and numerics

* **Model.** No governing equations are printed; the model is "described in
  detail" in refs. [5–7] (Orain 2013, 2019; Kim 2020, all
  [reduced MHD](/methods/reduced-mhd.md)). Two-fluid JOREK with $T_i=T_e$,
  source-sustained toroidal rotation (ASTRA/NBI), diamagnetic effects and
  neoclassical poloidal friction; reduced vs full MHD is not stated.
* **Closures** (§2, checked on the rendered page 3), JOREK normalized units:
  $$\eta=\eta_0\Big(\frac{T_e}{T_{e,0}}\Big)^{-3/2},\qquad \nu_\perp=\nu_{\perp0}\Big(\frac{T_e}{T_{e,0}}\Big)^{-3/2},\qquad \kappa_\parallel=\kappa_{\parallel,0}\Big(\frac{T_e}{T_{e,0}}\Big)^{5/2},$$
  with $\eta_0=10^{-7}$; $\nu_\perp$ called a "poloidal viscosity";
  $\kappa_{\parallel,0}\sim8\times10^5$ (printed as about $4\times10^5$
  "kg/m/s" in SI), capped by a kinetic flux limit of 10 (normalized, form
  not given). Central perpendicular heat and particle diffusivity about
  $10^{-6}$ (≈1.3 m² s⁻¹), lowered in the pedestal to hold H-mode profiles;
  parallel particle diffusivity $D_\parallel=10^{-5}$ (≈13 m² s⁻¹). The
  [bootstrap current](/definitions/bootstrap-current.md) evolves with the
  profiles as in Pamela et al. (2017).
* **Initialization.** Stationary equilibrium with flows from an $n=0$-only
  run of a few ms; then $n=1$–9 at noise level. In RMP runs the RMP is
  ramped first and $n=1$–9 are seeded once it is established.
* **Domain and BCs.** Closed surfaces, X-point and SOL up to the ITER wall;
  Bohm sheath BCs for velocity and normal heat flux at the targets. The
  ERGOS vacuum RMP field is imposed at the wall boundary, ramped over "a few
  ms" to avoid transient currents in the vacuum region; no STARWALL coupling
  is mentioned (fixed-boundary RMP, unlike the free-boundary model in
  [resistive-wall coupling](/methods/resistive-wall-coupling.md)).
* **RMP coils** (§2). Three rows of 9 coils, horizontal parts as curves and
  vertical parts as straight lines in ERGOS. Corners (m): upper
  $(7.73,3.38)$–$(8.26,2.62)$; middle $(8.62,1.79)$–$(8.66,-0.55)$; lower
  $(8.23,-1.55)$–$(7.77,-2.38)$. Toroidal widths 29.4°, 20.9°, 30.5° and
  centre shifts 30°, 26.7°, 30° (upper, middle, lower). Coil currents
  $$I_i=I_C\cos\!\big[-n(\phi_i-\Delta\phi_{\mathrm c})\,\pi/180\big],\qquad \phi_i=\phi_{\mathrm{shift}}+40(i-1),\quad i=1,\dots,9\ \text{(degrees)},$$
  with $I_C$ the peak current and $\Delta\phi_{\mathrm c}$ the row phase.
  MARS-F phases are converted to the ERGOS convention by printed formulas;
  the middle-row phase is zero in both. ERGOS and MARS-F were benchmarked
  in vacuum (not shown).
* **Displacement diagnostic** (§6): $\xi_\perp\approx\delta T_e/(\partial T_e/\partial\psi)$,
  as in Park et al. (APS 2020).
* **Divertor heat flux** (§7): $(Tn_e\mathbf v)\cdot\mathbf n$ with
  $T=T_e+T_i$, rescaled to a stationary 50 MW into the divertor (about 66%
  of the total heating, including fusion power, assumed radiated); kinetic
  neutrals, recycling and pumping are absent. This is a diagnostic, not the
  sheath BC.
* **Coupling.** ASTRA scenarios via the ITER IMAS database (Table 1:
  131025_24, 131025_23, 131039_0, 131036_21), ERGOS vacuum field, MARS-F
  phasing; one-way and offline.
* **Discretization, solver, cost.** Not described; a "fully implicit scheme"
  is mentioned (§7; see [implicit time integration](/methods/implicit-time-integration.md)).
  No resolution, element count or time step. Marconi-Fusion (CINECA).

# Tests and results

* **Scenarios** (Fig. 1; readings): pedestal $n_e$ about
  $1.1\times10^{20}$ m⁻³ (15 MA) and $0.7\times10^{20}$ (12.5, 10 MA); central
  $T_e$ about 25, 37, 47 keV (15, 12.5, 10 MA); central rotation about
  400 km/s (12.5, 10 MA), 130 and 200 km/s (15 MA slow and fast profiles).
* **Table 1, coil phasing** (degrees, upper/middle/lower):

  | Scenario | $n$ | MARS-F | ERGOS |
  |---|---|---|---|
  | 15 MA, slow rotation | 2 | 145/0/195 | 110.8/0/85.8 |
  | 15 MA, slow rotation | 3 | 200/0/140 | 56.63/0/76.63 |
  | 15 MA, slow rotation | 4 | 250/0/95 | 30.8/0/69.55 |
  | 15 MA, fast rotation | 3 | 200/0/140 | 56.63/0/76.63 |
  | 12.5 MA optimum | 3 | 215/0/120 | 51.63/0/83.3 |
  | 12.5 MA non-optimum | 3 | 135/0/25 | 78.3/0/114.97 |
  | 10 MA | 3 | 240/0/110 | 43.3/0/86.63 |

  Every ERGOS entry recomputed from the conversion formulas matches to the
  printed precision; the middle value comes out as $360°/n$, equivalent to
  0° (compiler's check).
* **Natural ELMs:** 15 MA crash at about 4.5 ms; 12.5 MA $n=5$ precursor at
  about 7.5 ms and crash at about 10 ms; 10 MA $n=3$ saturated from about
  4 ms. Fig. 3 peak divertor heat flux colour bars (not normalized)
  $5.9\times10^8$ and $2.5\times10^7$ W m⁻².
* **Threshold scan, 15 MA, $n=3$:** 0, 6, 20, 45, 60 kAt; suppression at 45
  and 60 kAt; runs about 12 ms.
* **Locking, 10 MA:** at about 12 ms (40 kAt) and 25 ms (20 kAt); runs about
  40 ms.
* **Footprints** (Figs. 19–20): heat-flux colour scales to about
  4–6 MW m⁻²; particle fluxes about $(1$–$2)\times10^{23}$ m⁻² s⁻¹.
* No code-to-code or experimental benchmark; the only quantitative
  comparison is the MARS-F vs JOREK X-point displacement.

# Notation map

| Becoulet et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $B_{tor}$ | $B_\phi$ at $R_0$ | |
| $N$, $M$ | $n$, $m$ | toroidal, poloidal mode numbers |
| $q_{res}=M/N$ | $q=m/n$ | |
| $\psi$, $\psi_n$ | $\psi$, $\psi_N$ | $2\pi$ convention not stated |
| $n_e$, $T_e$, $T_i$, $T=T_e+T_i$ | same | $T$ total in the heat-flux formula only |
| $V_{tor}$, $\vec V$ | $\mathbf v\cdot\mathbf e_\phi$, $\mathbf v$ | |
| $\vec n$ | $\mathbf n$ | |
| $\eta$, $\eta_0$ | $\eta$, $\eta_0$ | JOREK units |
| $\nu_\perp$, $\nu_{\perp0}$ | $\nu$ (perpendicular) | |
| $K_\parallel$, $K_{\parallel,0}$, $K_{\parallel,\max}$ | $\kappa_\parallel$, $\kappa_{\parallel,0}$, words (flux limit) | |
| $\nu_\parallel$ | $D_\parallel$ | **collision:** native $\nu$ used for a particle diffusivity |
| $\xi_\perp$ | $\xi_\perp$ (page-local) | perpendicular displacement; not registered |
| $\delta T_e$ | $\delta T_e$ | |
| $I_C$, $I_i$ | same (page-local) | coil currents, kAt |
| $\varphi_i^{coil}$, $\Delta\varphi^{center,coil}_{shift}$ | $\phi_i$, $\phi_{\mathrm{shift}}$ | degrees |
| $\Delta\Phi^{coil}_{MARS}$, $\Delta\Phi^{coil}_{ERGOS}$ | $\Delta\phi_{\mathrm c}$ (page-local) | **collision:** registry $\Phi$ is the electrostatic potential |
| $P_{div,nst}$, $P_{div,st}$, $L_{div}$ | words | |
| $W_{th}$, $W_{mag}$ | $W_{\mathrm{th}}$, $W_{\mathrm{mag}}^{(n)}$ | |
| $r$ (in $\sim1/r^M$) | $d$ (words: distance from the coils) | **collision:** registry $r$ is the minor radius |

The orientation of $\phi$ is not stated; MARS-F and ERGOS differ by a
starting-angle offset, hence the conversion formulas.

# Pages created or updated

Chunk 2 (2026-10-16) created or updated the pages below. This source is cited on:

* [Ballooning mode](/definitions/ballooning-mode.md)
* [Edge-localized mode (ELM) and ELM-free regimes](/definitions/edge-localized-mode.md)
* [Implicit time integration and preconditioned Krylov solvers for nonlinear MHD](/methods/implicit-time-integration.md)
* [JOREK](/software/jorek.md)
* [MARS-F](/software/mars-f.md)
* [Resonant magnetic perturbations and plasma response](/definitions/resonant-magnetic-perturbation.md)
* [Sheath (Bohm) boundary conditions](/methods/sheath-boundary-conditions.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2022_Crossref_Nuclear_Fusion_Becoulet_Non-linear_MHD_modelling_of_edge_localized_modes_suppression.pdf`.
   * **Version.** The PDF is the authors' IAEA FEC 2020 (28th IAEA Fusion
     Energy Conference) manuscript, 8 A4 pages, Word-generated (created
     2021-03-31), no page numbers, 15 printed references, ref. [10] "Y Liu
     et al this conference". It is **not** the Nucl. Fusion article, which
     Crossref lists with 57 references: the published paper is a longer,
     revised version, and every claim and number on this page refers to the
     conference manuscript. Section and figure numbers are those of the
     manuscript.
   * **Identity.** doi:10.1088/1741-4326/ac47af, checked on Crossref: Nucl.
     Fusion 62(6), article 066022, online 2022-04-05; title and the author
     order (14 names plus "the JOREK Team") match the manuscript; T.E. Evans
     is marked deceased. Year and venue are the published identity.
   * **How read.** Full text; the coil formulas and closures (pp. 2–3)
     checked on the rendered pages; plot values are the reader's
     approximate readings; the axis multiplier of the Fig. 5 linear panel is
     illegible.
   * **Recorded as printed.**
     * §7 "~40 m in the outer divertor"; the Abstract and §8 give "~40 cm".
     * §2 prints $\varphi_i^{(2)}=\varphi_i^{(2)}+\Delta\varphi^{coil}_{width}$
       (self-referential; intended $\varphi_i^{(1)}+\dots$), and the corner
       formula spaces coils by one coil width while the centre formula
       spaces them by 40° (compiler's check).
     * §6 $\xi_\perp\approx\delta T_e/(\partial T_e/\partial\psi)$ has units
       of flux, yet values are quoted in mm; a factor $|\nabla\psi|$ is not
       printed (compiler's dimensional check).
     * §6 quotes "~7mm at 60kAt" for MARS-F while Fig. 17 is "done for
       30kAt", implying linear scaling.
     * §5 cites a Fig. 15 that does not exist (captions jump from 14 to 16);
       the text calls Fig. 16 "experiments", its caption a 12.5 MA modelling
       plot.
     * §4 "increased toroidal rotation (Fig.1 left)": rotation is the right
       panel.
     * Peak strike-point heat flux "~5MW/m2" (Abstract) vs "~5-6MW/m2" (§8).
     * Threshold "45kAt-60kAt" (Abstract, §8) vs ">45kAt" sufficient with
       45 kAt shown suppressed (§4, Fig. 5).
     * §7 "the lowest point of the outer divertor is at $L_{div}=0.411$ m",
       while the Fig. 19 outer panels span about 0.6–1 m and the inner
       0–0.4 m.
     * $K_{\parallel,0}\approx4\times10^5$ "kg/m/s" is not a heat-conductivity
       unit.
     * $\nu_\perp$ is called a "poloidal viscosity".
     * The 10 MA case is called "high beta poloidal steady-state" with no
       $\beta$, $q_{95}$ or $\beta_p$ given; no scenario parameters beyond
       $I_p$, $B$ and the IMAS identifiers.
     * Typos: "Transotion", "diveror-wall", "were take", "access" for
       "assess".
   * **Reference list.** 15 printed entries (the manuscript's, not the
     published 57), merged into the bibliography under `becoulet-2022`; no
     titles are printed in any entry. Liu Y.Q. et al., PPCF 58:114005
     (2016), is `liu-2016-b` (`liu-2016` is a different Liu C. paper); J.-K.
     Park's APS-DPP 2020 abstract [15] is `park-2020-b`; ref. [10], "this
     conference", is recorded as the 28th IAEA FEC (2020). Existing keys
     reused: `loarte-2003`, `huysmans-2009` (printed "Huysmans" in [4]),
     `orain-2013`, `orain-2019`, `kim-2020`, `pamela-2017`, `becoulet-2017`;
     [12] misprints the surname "Becouet". The author block cites the JOREK
     team paper as "Hoelzl et al 2020 Nucl. Fus. sub, arXiv:2011.09120",
     i.e. the ingested [Hoelzl et al. (2021)](/sources/hoelzl-2021.md);
     being outside the reference list, it is not merged.

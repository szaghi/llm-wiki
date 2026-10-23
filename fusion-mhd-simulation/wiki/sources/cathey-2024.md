---
type: Source
title: "Cathey et al. (2024) — Non-linear MHD investigations of high-confinement regimes without type-I ELMs in ASDEX Upgrade and JT-60SA"
description: "Comparative review of JOREK reduced-MHD simulations of three ASDEX Upgrade regimes without type-I ELMs (QH-mode, low-triangularity small ELMs/QCE, EDA H-mode), plus preliminary JT-60SA linear pedestal-stability scans showing that diamagnetic and E×B flows cut the unstable spectrum from n = 1–30 to n = 3–9 as the resistivity falls to its realistic value."
resource: "doi:10.1088/1741-4326/ad5e97"
source_kind: paper
authors: [Cathey A., Hoelzl M., Meier L., Dunne M.G., Huijsmans G.T.A., Gil L., Harrer G.F., Aiba N., Cruz-Zabala D.J., Lackner K., Pamela S.J.P., Viezzer E., Wolfrum E., Günter S., JOREK Team, ASDEX Upgrade Team, EUROfusion WPTE Team]
year: 2024
venue: "Nucl. Fusion 64:096003"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2024_Crossref_Nuclear_Fusion_Cathey_Non-linear_MHD_investigations_of_high-confinement_regimes_wi.pdf"
tags: [reduced-mhd, extended-mhd, elm, pedestal, ballooning, kink, edge, tokamak, review]
timestamp: 2026-10-16T18:35:00Z
---

# Summary

A comparative review, mostly of the authors' earlier work, of
[JOREK](/software/jorek.md) [reduced-MHD](/methods/reduced-mhd.md)
simulations with diamagnetic and bootstrap extensions of three ASDEX
Upgrade (AUG) H-mode regimes without type-I
[ELMs](/definitions/edge-localized-mode.md), followed by new preliminary
linear-stability runs for JT-60SA. The regimes are QH-mode (AUG #39279,
detailed in Meier et al. 2023), small ELMs at low triangularity as a
stand-in for the quasi-continuous-exhaust (QCE) regime (Cathey et al. 2022)
and EDA H-mode (AUG #36330, Cathey et al. 2023). In QH-mode an
$n=1$-dominated saturated kink-peeling mode, with harmonic energies falling
steeply with $n$, is identified with the edge harmonic oscillation (EHO);
raising the particle source turns it into a type-I ELM at the experimental
pedestal-density threshold of about $2.3\times10^{19}$ m⁻³. In the
small-ELM and EDA cases resistive peeling–ballooning modes at medium-to-high
$n$ dominate the linear phase and low $n$ are excited non-linearly; the
pedestal fluctuation frequencies (20–40 kHz for small ELMs, about 13 kHz
late in EDA) are compared with experiment. For JT-60SA (scenario 4-1,
4.6 MA, 2.26 T, GOTRESS+ with EPED1) JOREK re-solves the
[Grad–Shafranov equation](/definitions/grad-shafranov-equation.md) on a
double-X-point grid and runs single-$n$ linear simulations on established
diamagnetic and $E\times B$ flows: at about 10 times the realistic
resistivity all probed $n=1$–30 are unstable ($n=17$ fastest); at realistic
resistivity only $n=3$, 6, 9. Without the flows, $n\ge9$ are unstable at
realistic resistivity and $n=3,6$ are stable: the flows stabilize high-$n$
[ballooning modes](/definitions/ballooning-mode.md) and destabilize low-$n$
modes. No equation is numbered; the model is only sketched.

# Key claims

1. **EHO = saturated $n=1$ kink-peeling mode** (§3.2, Fig. 3). AUG #39279
   with $n=0$–6: only $n=1,2$ linearly unstable, $n=2$ faster, but $n=1$
   dominates and saturates with all higher harmonics; outboard-midplane
   density fluctuations peak at about 27 kHz with harmonics, above the
   experimental EHO at about 10 kHz (§2.1). Shown; the gap "likely" due to
   the omitted NBI torque and $T_e\ne T_i$ separation (Stated).
2. **QH → type-I transition** (§3.2). Raising the particle source from
   $t=20$ ms gives a type-I ELM once the pedestal density exceeds about
   $2.3\times10^{19}$ m⁻³, "at the same density threshold as seen in AUG
   discharge #39279"; the ELM is under-resolved with $n\le6$ (fn. 10). Shown.
3. **$q_{95}$ windows** (§3.2). From rigidly raising $q$ by a larger
   toroidal field at fixed shear, consistent with carbon-wall AUG
   experiments; the non-linear evolution of $q_{95}$ "contributes to the kink
   mode saturation". Stated (detailed in Meier et al. 2023).
4. **Toroidal-resolution check** (fn. 10). Doubling the harmonics leaves the
   EHO and the ELM onset unchanged; the ELM dynamics could change. Stated
   (no data).
5. **Small ELMs at low triangularity** (§3.3). A type-I ELMy discharge with
   artificially raised separatrix density develops quasi-continuous activity
   that prevents type-I ELMs; even $n=0$–12, with runs to $n=20$ showing the
   same dynamics; 20–40 kHz at the outboard steep-gradient region,
   "qualitatively similar" to QCE observations; dominant $n=8,10$ near the
   separatrix, identified as resistive peeling–ballooning modes by their
   resistivity sensitivity and phase velocity. Shown (in Cathey et al. 2022;
   summarized).
6. **Access control** (§3.3, Fig. 4). Lowering the separatrix density
   suppresses the small ELMs and leads to a type-I ELM, consistent with the
   experimental threshold of about 0.3 of the Greenwald density; raising the
   heating power also suppresses them within a few ms, a type-I ELM
   following at about 20 ms. Reasons: higher $T$ lowers
   $\eta\propto T^{-3/2}$ and removes resistive drive; steeper $\nabla p$
   raises the diamagnetic and $E\times B$ flows that stabilize medium/high-$n$
   ballooning modes. Shown (Fig. 4 reproduced); mechanism Stated.
7. **EDA: resistive peeling–ballooning modes** (§3.4, Fig. 5; from Cathey et
   al. 2023). $n=0$–13; linear phase dominated by $n=6$–9; linearly stable
   $n<4$ and $n>11$ driven non-linearly by three-wave interaction with
   $\gamma_{n_1\pm n_2}=\gamma_{n_1}+\gamma_{n_2}$; fluctuations 8–18 kHz,
   shifting from about 40 to 13 kHz as $E_r$ is modified, 13 kHz being
   "approximately … the lower end" of AUG QCM frequencies (15–40 kHz);
   poloidal wavenumber 0.1–0.5 cm⁻¹ ($k_\theta\rho_s\sim0.01$–0.05) against
   about 0.6 cm⁻¹ measured; mode velocity about 1 km/s in the ion
   diamagnetic direction; filaments at about 2.3 kHz; outer-divertor heat
   peaks 3.2–12 MW m⁻². Shown (in the earlier paper).
8. **Regime comparison** (§3.5, Fig. 6). Small-ELM and EDA linear phases are
   dominated by medium-to-high-$n$, LFS-localized resistive modes; in QH the
   linearly dominant $n=2$ kink-peeling mode grows more slowly and is
   overtaken by $n=1$. Non-linearly, QH energy flows from $n=1$ to higher
   $n$ and $W_{\mathrm{mag}}^{(n)}$ falls steeply (exponentially, §5) with
   $n$; small-ELM and EDA spectra are flat with active exchange; in EDA,
   pedestal depletion shifts the dominant modes to lower $n$. Shown.
9. **JT-60SA resistivity scan** (§4.1, Figs. 8–9). Single-$n$ runs for
   $n=1,3,6,9,13,17,21,25,30$ on an established $n=0$ with Mach-1 parallel
   flow and diamagnetic flows. At about $10\eta$ all unstable, $n=17$
   fastest (about $2.6\times10^4$ s⁻¹, figure reading); lowering $\eta$
   narrows the spectrum; at realistic $\eta$ (Spitzer with neoclassical
   corrections, $Z_{\mathrm{eff}}=2.5$ in the pedestal) only $n=3,6,9$ are
   unstable, $n=3$ "mostly peeling", $n=6,9$ coupled peeling–ballooning.
   Shown.
10. **Flows stabilize high $n$, destabilize low $n$** (§4.2, Figs. 10–11).
    Without diamagnetic and $E\times B$ flows at realistic $\eta$ the
    unstable modes are $n\ge9$ with $\gamma$ rising monotonically to $n=30$;
    at $10\eta$ zero-flow growth rates are much larger at high $n$ (about
    $1.1\times10^5$ against $4\times10^3$ s⁻¹ at $n=30$, readings); $n=3,6$
    at realistic $\eta$ and $n=1$ at $10\eta$ are unstable only with flows,
    attributed to "the destabilising effect that ExB and its shear have on
    low-n modes" (Xu et al. 2017; Chen et al. 2017). Without flows the
    $n=9$ structure is "much more ballooning". Shown; mechanism Attributed.
11. **JT-60SA harder than AUG** (§4.1) because of the larger size and higher
    Lundquist number. Stated.
12. **Single-temperature limitation** (§2.3, §3.2). With one temperature and
    no NBI torque source the simulated $E_r$ differs from the CXRS fit (Fig.
    2), affecting intermediate/high-$n$ stability; the MISHKA-1 point of
    #36330 lies near the $n\sim14$ ideal ballooning boundary, but ideal
    analysis neglects diamagnetic and $E\times B$ stabilization. Stated.

# Models and numerics

* **Model** (§3.1, unnumbered; "rigorously described" in
  [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) and Huysmans & Czarny
  2007). JOREK visco-resistive reduced MHD with diamagnetic extension and
  bootstrap source. Eight unknowns (continuity, adiabatic pressure, three
  vector-potential and three ion-momentum components) are reduced to five
  (continuity, pressure, $\psi$, $\Phi$, $v_\parallel$) by a stationary
  toroidal field (removing the fast magnetosonic wave) and an $E\times B$
  velocity in the poloidal plane. Ansatz (checked on the rendered page 5),
  in physical form:
  $$\mathbf B=F_0\nabla\phi+\nabla\psi\times\nabla\phi,\qquad
  \mathbf v=v_\parallel\mathbf b+\mathbf v_E+\mathbf v_{\mathrm{dia},i},\qquad
  \mathbf v_{\mathrm{dia},i}=-\frac{R}{eF_0n_e}\nabla p_i\times\mathbf e_\phi .$$
  The printed forms carry inconsistent mass factors (Recorded as printed).
* **Closures.** Spitzer $\eta\propto T^{-3/2}$; Spitzer–Härm
  $\kappa_\parallel\propto T^{5/2}$ "at realistic parallel-to-perpendicular
  heat asymmetry"; ad-hoc perpendicular particle and heat diffusivity
  profiles, stationary and tuned per scenario to prescribe the axisymmetric
  pedestal evolution (extra transport after the harmonics are switched on is
  attributed to the modes); viscosity mentioned, no value; no higher-order
  FLR (gyroviscous) terms. Single temperature $T=T_e=T_i$.
* **Bootstrap current** (Sauter formula). Enters Ohm's law through
  $\eta(\mathbf J-\mathbf J_x)$, with $\mathbf J_x$ holding both the bootstrap
  and the Ohmic source parts, so the current relaxes on the resistive time
  scale (see [bootstrap current](/definitions/bootstrap-current.md)).
* **Parallel flow.** Set only by Mach-1 conditions at the simplified
  divertor targets ([sheath BCs](/methods/sheath-boundary-conditions.md));
  no parallel momentum source (fn. 9).
* **Discretization.** Not described (JOREK
  [Bézier finite elements](/methods/bezier-finite-elements.md) with toroidal
  Fourier harmonics, by reference); flux-aligned grid, double-X-point grid
  for JT-60SA (Fig. 7); for JT-60SA the core current profile is smoothed "to
  avoid … numerical instabilities" at a fixed 4.6 MA. Toroidal resolution:
  QH $n=0$–6 (doubled as a check); small ELMs even $n=0$–12 (check to 20);
  EDA $n=0$–13; JT-60SA $n=0$ plus one $n$.
* **Workflow (JT-60SA).** Axisymmetric phase until the boundary-driven
  parallel flow and the diamagnetic poloidal flow are established, then
  harmonics at noise level; pedestal build-up as in Cathey et al. 2020.
* **Time integration, solvers, parallelism, costs.** Not given;
  Marconi-Fusion (project FUA37_MHD).

# Tests and results

* **Table 1 (AUG discharges, values at $\psi_N=0.95$):**

  | Regime | Triangularity (up/down) | $q_{95}$ | $\beta_p$ | Electron collisionality | $n_e$ [m⁻³] | $T_e$ [eV] |
  |---|---|---|---|---|---|---|
  | QH-mode | 0.38 (0.31/0.44) | 6.8 | 1.50 | 0.43 | $1.74\times10^{19}$ | 831 |
  | Small ELMs | 0.24 (0.08/0.40) | 5.4 | 0.69 | 6.42 | $4.52\times10^{19}$ | 281 |
  | EDA H-mode | 0.41 (0.32/0.49) | 5.3 | 0.91 | 6.64 | $6.70\times10^{19}$ | 328 |

* **AUG #39279 (QH):** upper single null, unfavourable $\nabla B$ drift,
  co-current NBI, $I_p=+0.6$ MA, $B_\phi=-2.5$ T, elongation 1.83; QH phase
  3.44–3.59 s; EHO $n=1$ plus harmonics at about 10 kHz (simulated about
  27 kHz); $\log_{10}W_{\mathrm{mag}}^{(n)}$ saturates by about 7 ms with $n=1$
  highest (Fig. 3).
* **Small ELMs:** dominant $n=8,10$ (§3.3) or $n=7$–10 (§3.5); 20–40 kHz;
  after a heating-power increase at about 5.5 ms the oscillations stop and a
  type-I ELM follows at about 20 ms with an outer-divertor power peak of
  about 30 MW (reading, Fig. 4).
* **AUG #36330 (EDA):** $-2.5$ T, 0.8 MA, 5 MW NBI+ECRH, argon seeding
  feedback at 1.5 MW crossing the separatrix, lower single null, favourable
  drift, elongation 1.6; QCM about 30 kHz; MISHKA-1 point near the
  $n\sim14$ boundary ($\alpha_{\mathrm b}\approx3.5$, edge current about
  0.4 MA m⁻²); simulated $E_r$ well about $-25$ kV/m (Fig. 2); simulation
  8–18 kHz settling at about 13 kHz.
* **JT-60SA scenario 4-1:** 4.6 MA, $B_0=2.26$ T, EPED1 width coefficient
  0.076, high shaping, low separatrix density. Fig. 8 growth rates
  ($10^3$ s⁻¹, readings):

  | $n$ | 1 | 3 | 6 | 9 | 13 | 17 | 21 | 25 | 30 |
  |---|---|---|---|---|---|---|---|---|---|
  | $\sim10\eta$ | 4 | 13 | 18 | 22 | 25.5 | 26.5 | 20 | 11 | 4 |
  | $\sim8\eta$ | 3 | 9.5 | 14 | 16 | 19 | 19.5 | 15.5 | – | – |
  | $\sim6\eta$ | 1 | 5 | 9 | 9.3 | 11 | 13 | 9.3 | – | – |
  | $\sim1\eta$ | – | 3.3 | 8 | 8 | – | – | – | – | – |

  Fig. 10 without flows (readings): at $10\eta$ from about 1.5 ($n=1$) to
  115 ($n=30$); at $1\eta$ from about 8 ($n=9$) to 17 ($n=25$–30).

# Notation map

| Cathey et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $R$, $\hat{\boldsymbol\varphi}$ | $R$, $\mathbf e_\phi$ | positive $I_p$ counter-clockwise from above |
| $\hat{\boldsymbol\vartheta}$, $B_{\mathrm{pol}}$ | words; $\nabla\psi\times\nabla\phi$ | poloidal direction and field |
| $F_0$, $\psi$, $\psi_{\mathrm{norm}}$ | $F_0$, $\psi$, $\psi_N$ | $\psi$ per radian |
| $v_\parallel$, $v_{\mathrm{ExB}}$ | $v_\parallel$, $\mathbf v_E$ | |
| $\mathbf v_{\mathrm{dia},i}$ | $\mathbf v_{\mathrm{dia},i}$ | |
| $p_i$, $n_e$, $e$, $m_{\mathrm{ion}}$, $m_e$ | $p_i$, $n_e$, $e$, $m_i$, $m_e$ | |
| $\delta^*$ | words (JOREK diamagnetic parameter) | undefined here; **collision** with $\delta(\cdot)$ |
| $\eta$, $\eta_{\mathrm{realistic}}$ | $\eta$, words | |
| $\chi_\parallel$ | $\kappa_\parallel$ | |
| $j$, $j_{\mathrm{src}}$ | $J_\phi$, $\mathbf J_x$ | source holds bootstrap and Ohmic parts |
| $T$ | $T$ | each species temperature, not the sum |
| $E_r$ | $E_r$ | |
| $n$, $m$ | $n$, $m$ | |
| $\gamma$, $\gamma_{k\pm m}$ | $\gamma$, $\gamma_{n_1\pm n_2}$ | **collision:** native $k$, $m$ are toroidal indices, not the poloidal $m$ |
| $f$ | $\omega/2\pi$, words | registry: $f$ is never a frequency |
| $E_{\mathrm{mag},n}$ | $W_{\mathrm{mag}}^{(n)}$ | |
| $k_\theta$, $\rho_s$ | words (poloidal wavenumber, ion sound Larmor radius) | not registered; **collision:** registry $\rho$ is mass density |
| $q_{95}$, $\beta_{\mathrm{pol}}$ | $q_{95}$, $\beta_p$ | |
| $\nu^*_{e,95}$ | words (electron collisionality) | **collision:** registry $\nu$ is viscosity |
| $\delta$, $\kappa$ | words (triangularity, elongation) | **collision** with $\delta(\cdot)$, $\kappa_\parallel$ |
| $n_{\mathrm{GW}}$, $n_{e,\mathrm{sep}}$, $n_{e,\mathrm{ped}}$ | words | |
| $P_{\mathrm{heat}}$, $P_{\mathrm{sep}}$, $P_{\mathrm{rad}}$ | words (powers) | **collision:** registry $P_{\mathrm{rad}}$ is a power density |
| $\alpha_{\max}$, $\langle j_{\max}\rangle$ | $\alpha_{\mathrm b}$, words | |
| $Z_{\mathrm{eff}}$ | $Z_{\mathrm{eff}}$ | |

# Pages created or updated

Chunk 2 (2026-10-16) created or updated the pages below; chunk 3 extended some. This source is cited on:

* [Ballooning mode](/definitions/ballooning-mode.md)
* [Bootstrap current and its MHD implementation](/definitions/bootstrap-current.md)
* [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md)
* [Edge harmonic oscillation and QH-mode](/definitions/edge-harmonic-oscillation.md)
* [Edge-localized mode (ELM) and ELM-free regimes](/definitions/edge-localized-mode.md)
* [JOREK](/software/jorek.md)
* [Reduced MHD for tokamaks](/methods/reduced-mhd.md)
* [Sheath (Bohm) boundary conditions](/methods/sheath-boundary-conditions.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2024_Crossref_Nuclear_Fusion_Cathey_Non-linear_MHD_investigations_of_high-confinement_regimes_wi.pdf`.
   * **Version.** Publisher version of record (IOP, open access, CC BY 4.0),
     12 printed pages plus the IOP download cover (13 PDF pages); received
     25 Jan 2024, revised 6 Jun 2024, accepted 3 Jul 2024.
   * **Identity.** doi:10.1088/1741-4326/ad5e97, checked on Crossref: Nucl.
     Fusion 64(9), article 096003, online 18 July 2024; title, first author
     and journal match; 53 references, as printed.
   * **How read.** Full text; the ansatz (p. 5) checked on the rendered
     page; growth rates, frequencies and powers from figures are the
     reader's approximate readings.
   * **Recorded as printed.**
     * $\mathbf v_{\mathrm{dia},i}$ is printed as
       $-R\nabla p_i\times\hat{\boldsymbol\varphi}/(e\,m_{\mathrm{ion}}F_0n_e)$,
       with a dimensionally wrong extra $m_{\mathrm{ion}}$, and as
       $-\delta^*R\nabla p_i\times\hat{\boldsymbol\varphi}/(m_en_e)$, with the
       electron mass where the JOREK normalized form has the ion mass;
       $\delta^*$ is undefined (compiler's check).
     * The ansatz writes $B_{\mathrm{pol}}\hat{\boldsymbol\vartheta}$ as a
       scalar times a unit vector but defines $B_{\mathrm{pol}}$ as a
       vector, and writes the $E\times B$ velocity along
       $\hat{\boldsymbol\vartheta}$ only.
     * QH triangularity: Table 1 "(up/down)" 0.31/0.44, text upper 0.44,
       lower 0.31; EDA upper triangularity 0.32 (Table 1) vs 0.31 (§2.3).
     * Small ELMs: "all even toroidal mode numbers between $n=0$ and 12"
       with dominant $n=8,10$ (§3.3), but dominant "$n=7\ldots10$" (§3.5),
       and the Fig. 6 small-ELM curve shows every integer $n$ from 1 to 12.
     * EDA: linear growth "dominated by $n=\{6\ldots9\}$" and linearly
       stable "$n<4$ and $n>11$", leaving $n=4,5,10,11$ unclassified.
     * 13 kHz is called "approximately … the lower end" of AUG QCM
       frequencies while §2.3 gives 15–40 kHz; the discharge's own QCM is
       about 30 kHz, not compared.
     * The experimental QCM propagates in the electron diamagnetic
       direction (lab frame, §2.3), the simulated mode at about 1 km/s in
       the ion diamagnetic direction (§3.4); frames are not stated here.
       The original EDA paper, [Cathey et al. (2023)](/sources/cathey-2023.md),
       resolves it: about $+1$ km/s is the plasma-frame velocity at the mode
       maximum, the lab-frame velocity is about $-15$ km/s (electron
       diamagnetic), so the two directions are not in conflict.
     * EDA numbers differ slightly from [Cathey et al. (2023)](/sources/cathey-2023.md):
       linear-phase frequency "about 40" here vs about 35 kHz (30–45) there;
       MISHKA-1 boundary $n\sim14$ here vs $n\approx15$ there; simulated $E_r$
       well about $-25$ kV/m (Fig. 2) here vs $-29$ (linear) and about $-15$
       kV/m (non-linear) there; measured QCM $k_\theta$ about 0.6 here vs
       0.6–0.9 cm⁻¹ there.
     * Fig. 7 caption: the imported separatrix is "below" the JOREK one;
       §4: they "overlap".
     * Fig. 8 shows four resistivities (about 10, 8, 6, 1 × realistic)
       while caption and text describe a scan between "nominal" and "high";
       "nominal", "realistic" and "anticipated" are used interchangeably.
     * "Low edge safety factor" (Abstract), "high shaping and low"
       separatrix density (§5): no values given.
     * Fn. 10's statement on the ELM onset reads as either a prediction or
       a result.
     * No simulation parameters (JOREK-unit resistivity, diffusivities,
       time step, grid size) are given.
     * Language: "complimentary", "opaqued", "acts an indicator", two
       sentence fragments (§4, §5).
   * **Reference list.** 53 printed entries, merged into the bibliography
     under `cathey-2024`. Ref. [41] is the EDA paper `cathey-2023`; [14] is
     the published PPCF 63:075016 of `cathey-2021`; [18] is the ingested
     [Hoelzl et al. (2021)](/sources/hoelzl-2021.md); the Sauter erratum
     [46], page range printed "5140–2839", is `sauter-2002-b`. New keys
     avoiding collisions: `burrell-2009-b` (`burrell-2009` is PRL
     102:155003), `kim-2023-b` (Kim S.K. et al., NF 63:106013, which shares
     its printed title with the existing `kim-2023`, Kim D. et al., NF
     63:124001; to be checked), `li-2022` (BOUT++ QH-mode FLR study).
     Printed defects: [9] private communication without title; [12] title
     in the collaboration slot; [22], [31] titles not printed; [38]
     "submitted"; [51] stray "a)"; [27], [39], [40] printed years one less
     than the volume years. Existing keys reused include `meier-2023`,
     `cathey-2020`, `cathey-2022`, `krebs-2013`, `liu-2015`, `liu-2017`,
     `pamela-2017`, `huysmans-2007`, `sauter-1999`. Footnote a cites the
     ingested [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (doi
     10.1088/1741-4326/ad5a21) for the JOREK Team list; as a footnote, not a
     numbered reference, it is not in the merged list.

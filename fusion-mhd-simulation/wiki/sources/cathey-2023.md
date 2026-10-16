---
type: Source
title: "Cathey et al. (2023) — Probing non-linear MHD stability of the EDA H-mode in ASDEX Upgrade"
description: "First non-linear JOREK reduced-MHD simulations of an ASDEX Upgrade EDA H-mode: ideally stable resistive peeling–ballooning modes (n = 6–9) rotate at the E×B plus projected parallel velocity, couple non-linearly down to n = 2–3, erode the pedestal continuously, and chirp from about 35 to 13 kHz, overlapping the measured 20–40 kHz quasi-coherent mode."
resource: "doi:10.1088/1741-4326/acc818"
source_kind: paper
authors: [Cathey A., Hoelzl M., Gil L., Dunne M.G., Harrer G.F., Huijsmans G.T.A., Kalis J., Lackner K., Pamela S.J.P., Wolfrum E., Günter S., JOREK Team, ASDEX Upgrade Team, EUROfusion MST1 Team]
year: 2023
venue: "Nucl. Fusion 63:062001"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2023_Crossref_Nuclear_Fusion_Cathey_Probing_non-linear_MHD_stability_of_the_EDA_H-mode_in_ASDEX.pdf"
tags: [mhd, reduced-mhd, extended-mhd, elm, pedestal, ballooning, edge, tokamak]
timestamp: 2026-10-16T00:00:00Z
---

# Summary

The paper (a Nucl. Fusion Letter) reports the first non-linear MHD
simulations started from an experimental enhanced D-alpha (EDA) H-mode
equilibrium: ASDEX Upgrade #36330, argon-seeded and ELM-free, CLISTE
reconstruction at 6.165 s. Linear ideal MHD (MISHKA) puts the operational
point just inside the ideal $n\approx15$ ballooning boundary. The
[JOREK](/software/jorek.md) runs use single-temperature visco-resistive
[reduced MHD](/methods/reduced-mhd.md) with diamagnetic drift and a Sauter
[bootstrap](/definitions/bootstrap-current.md) source, keep $n=0,\dots,13$,
and find the equilibrium unstable to resistive peeling–ballooning modes:
$n=5,\dots,11$ are linearly unstable, $n=6,\dots,9$ most unstable, peaking at
the maximum of $\nabla T_e$ ($\psi_N\approx0.98$). Their lab-frame poloidal
velocity, about $-15$ km/s (electron diamagnetic direction), matches the
$E\times B$ velocity plus the poloidal projection of the parallel flow, the
expected velocity of a resistive [ballooning mode](/definitions/ballooning-mode.md);
this is the basis of the identification. Three-wave coupling then drives
the linearly stable $n$; non-linearly the dominant $n$ shifts to 2–3, an
ergodic layer forms outside $\psi_N\approx0.965$, and the pedestal erodes
continuously (about 2.5 MJ/s and $6.9\times10^{21}$ ions/s), unlike the
transient losses of type-I [ELMs](/definitions/edge-localized-mode.md).
Fluctuations are large ($\delta T_e/T_e\sim50\%$, $\delta n_e/n_e\sim40\%$).
The frequency chirps from about 35 kHz (linear phase), within the measured
20–40 kHz quasi-coherent mode (QCM) band, to 8–18 kHz as the $E_r$ well
becomes shallower. The simulated poloidal wavenumber, 0.1–0.5 cm⁻¹, is below
the QCM values and closer to the quasi-continuous-exhaust (QCE) regime. The
paper states only that the simulated modes "could be related" to the QCM.

# Key claims

1. **Ideally stable operational point** (§2.1, Fig. 2). MISHKA puts it "just
   inside" the ideal ballooning boundary at $n\approx15$. Shown. EDA points
   generally lie slightly inside the peeling–ballooning boundary for
   $n=10$–30 (§1, refs. [19–22]). Attributed.
2. **Resistively unstable** (§2.1, §3). At realistic resistivity JOREK finds
   resistive peeling–ballooning modes; resistivity moves the ballooning
   boundary to lower pressure gradients (refs. [28–30]). Shown; the general
   statement Attributed.
3. **Linear spectrum** (§3.1, Fig. 5). Unstable $n=5,\dots,11$; linearly
   stable $n=1,\dots,4,12,13$ are excited non-linearly; "most unstable"
   $n=6,\dots,9$. Shown (reader's readings: peak $\gamma\approx2.7\times10^4$ s⁻¹
   at $n=7$–8, about $1.5\times10^4$ at $n=5$, $0.5\times10^4$ at $n=11$).
4. **Three-wave rule** (§3.1). $n_3=n_1\pm n_2$ with
   $\gamma_{n_3}=\gamma_{n_1}+\gamma_{n_2}$ (Krebs et al. 2013); the
   dominant pair mostly sets the growth rate. Attributed; consistent with
   early non-linear growth rates of about $(4$–$6)\times10^4$ s⁻¹ for
   $n=1,2,3,12,13$ in Fig. 5.
5. **Localization** (§3.2, Fig. 6). The mode peaks at $\psi_N=0.983$,
   "almost exactly" at the maximum of $\partial_RT_e$ ($\psi_N=0.980$);
   maxima of $\nabla p_e$ and $\nabla n_e$ at 0.977 and 0.995; dominant
   $m=35,\dots,56$, resonant at $q=6$ ($m/n=36/6,42/7,48/8$). Shown; agreement
   with C-Mod GPI and AUG helium-beam observations Attributed.
6. **Mode velocity** (§3.2, Fig. 7). Lab frame about $-15$ km/s at the
   outboard midplane for $\psi_N=0.929$–0.987, electron diamagnetic at all
   radii; plasma frame about $+1$ km/s (ion diamagnetic) only where the
   amplitude peaks ($\psi_N\approx0.970$–0.982), electron direction elsewhere
   ($-9$ km/s at 0.934, $-4.5$ km/s at 0.997), "rigid body rotation". Shown.
7. **Identification as resistive (peeling-)ballooning** (§3.2, §5). The
   velocity "match[es] best" $(\mathbf v_E+v_\parallel\mathbf b)\cdot\hat{\boldsymbol\theta}$,
   the resistive-ballooning result of Morales et al. 2016, not the ideal
   one, which adds half the poloidal ion diamagnetic velocity. Shown
   (comparison) on an Attributed theory basis, together with the
   low-field-side structure.
8. **Cross-phases** (§3.2, Fig. 8). Linear phase: $n_e$ and $T_e$
   "'perfectly' in-phase", about 10° to $\Phi$; non-linear phase: all three
   roughly in phase. Shown.
9. **$E_r$ well** (§2.2, §3.2, §4.3, Fig. 4). Axisymmetric minimum about
   $-29$ kV/m in the linear phase against the measured $-20\pm4$ kV/m, too
   deep because there is no NBI torque source and the single temperature
   cannot give $\nabla p_i<\nabla p_e$; in the non-linear run the minimum
   "matches" experiment (§2.2) and averages about $-15$ kV/m (§4.3). Shown;
   the two statements conflict (Recorded as printed).
10. **Down-shift of dominant $n$** (§4.1, Fig. 9). From $n=6$–9 to 2–5
    (§4), with $n=2,3$ dominant in time-averaged spectra centred at 4 ms;
    causes: non-linear transfer to linearly stable low $n$ and pedestal
    depletion. Shift Shown; causes Stated.
11. **Ergodization and continuous losses** (§4, §4.2, Fig. 10). Ergodic
    layer outside $\psi_N\approx0.965$; about 2.5 MJ/s and
    $6.9\times10^{21}$ ions/s, continuous, "in opposition to" transient type-I
    ELM transport in JOREK (Cathey et al. 2020); the pedestal density drops
    more than $T_e$. Shown.
12. **Fluctuation amplitude** (§4.3, Fig. 11). $\delta T_e/\langle T_e\rangle\sim50\%$,
    $\delta n_e/\langle n_e\rangle\sim40\%$ at $\psi_N\approx0.98$
    (toroidal averages), consistent with C-Mod and AUG QCM observations.
    Shown; comparison Attributed.
13. **Frequency chirp** (§3.2, §4.3, Fig. 11). About 35 kHz in the linear
    and early non-linear phase, then 8–18 kHz (Abstract: 13 kHz), attributed
    to the shallowing $E_r$ well; the linear value overlaps the QCM band
    20–40 kHz, the non-linear one "sits at the lower end" of AUG QCM values.
    Frequencies Shown; cause Stated.
14. **Wavenumber mismatch** (§4.3). Simulated poloidal wavenumber 0.1–0.5
    cm⁻¹ at the outer midplane against C-Mod QCM about 1.5, AUG QCM 0.6–0.9
    and AUG QCE 0.4–0.9 cm⁻¹: "closer resemblance to … the QCE regime than
    the quasi-coherent mode". Shown, against Attributed experimental values.
15. **Pick-up coils** (§2.1, Fig. 3). Bands $n=3,\dots,7$ at frequencies
    $n\times32.9$ kHz; their relation to the QCM is "unclear as of yet". Shown
    (experimental).
16. **Hedged conclusion** (§4.3, §5). The modes "could be related to the
    QCM", with "several quantitative and qualitative similarities". Stated.

# Models and numerics

* **Model.** No governing equations are printed; the model is that of
  [Hoelzl et al. (2021)](/sources/hoelzl-2021.md): JOREK single-temperature
  ($T_e=T_i=T$) visco-resistive reduced MHD with the diamagnetic-drift and
  bootstrap-source extensions. Reduced MHD is justified by "excellent
  agreement of reduced and full MHD models for pedestal applications"
  (Pamela et al. 2020). The bootstrap fraction follows the Sauter model as
  profiles change; with the diamagnetic extension this makes an $E_r$ well
  ($\propto\nabla p/n_e$) appear self-consistently. Dissipation coefficients
  are not given, except $\kappa_\parallel/\kappa_\perp\sim10^9$ and a
  "realistic" resistivity.
* **Experimental $E_r$** (CXRS force balance on N⁷⁺, §2.2):
  $E_r=\partial_rp_{\mathrm{imp}}/(eZn_{\mathrm{imp}})-(\mathbf v_{\mathrm{imp}}\times\mathbf B)_r$.
* **Ballooning-mode velocities** (from Morales et al. 2016, §3.2): ideal,
  $(\mathbf v_E+v_\parallel\mathbf b)\cdot\hat{\boldsymbol\theta}+\tfrac12$(poloidal
  ion diamagnetic velocity); resistive,
  $(\mathbf v_E+v_\parallel\mathbf b)\cdot\hat{\boldsymbol\theta}$, with
  $\hat{\boldsymbol\theta}$ the poloidal unit vector; in JOREK reduced MHD
  $\mathbf v_E$ is purely poloidal.
* **Sources and transport.** Ad-hoc diffusivities and particle and heat
  sources keep $T$, $n_e$ and $j_\phi$ stationary in axisymmetric runs (Fig.
  4: profiles at 0 and 10 ms overlap), standing for neoclassical and
  turbulent transport. No toroidal-rotation source; parallel and poloidal
  flows saturate after about 1 ms of axisymmetric run.
* **Equilibrium.** CLISTE, with a bootstrap constraint, from data in
  6.115–6.190 s, at 6.165 s.
* **BCs.** Ideal (perfectly conducting) wall; simplified SOL and divertor
  targets; the SOL $E_r$ is "unrealistic".
* **Discretization.** JOREK [Bézier finite elements](/methods/bezier-finite-elements.md)
  (not restated): 214 radial (axis to wall) × 354 poloidal elements, packed
  so that one radial element spans 1.28 mm in the pedestal; 64 toroidal
  planes for $n=0,\dots,13$. This allows the realistic anisotropy $10^9$.
* **Time integration.** Implicit
  ([implicit time integration](/methods/implicit-time-integration.md));
  $\Delta t$ one JOREK time unit, $\sqrt{\mu_0\rho_0}=0.6687\,\mu$s ($\rho_0$
  the central mass density), halved at times in the non-linear phase "to
  improve convergence of the iterative solver". MHD validity requires
  $\omega\ll\Omega_i\sim10^8$ s⁻¹; a smaller step would not make faster
  physics valid.
* **Initialization.** $n=1,\dots,13$ at noise amplitude after 1 ms of
  axisymmetric run. Marconi-Fusion (project FUA36 MHD); no cost given.

# Tests and results

* **Discharge AUG #36330** (§2.1): lower single null, elongation 1.6,
  triangularity 0.49 lower, 0.31 upper (0.40 average), favourable
  $\nabla B$ drift; $B_\phi=-2.5$ T, $I_p=0.8$ MA, $q_{95}=4.86$; ECRH and NBI
  2.5 MW each (5.9–6.3 s), argon seeding; divertor peak heat flux 5–10 MW m⁻²;
  helium-beam QCM about 30 kHz (20–40 kHz).
* **Comparison** (simulation vs experiment):

  | Quantity | JOREK | Experiment | Location |
  |---|---|---|---|
  | Ideal stability | MISHKA: just stable, $n\approx15$ | ELM-free | Fig. 2 |
  | Dominant $n$, linear | 6–9 (7 dominant) | pick-up coils $n=3$–7 | §3.1, Fig. 3 |
  | Dominant $n$, non-linear | 2–3 | pick-up coils $n=3$–7 | Fig. 9 |
  | Mode location | $\psi_N\approx0.98$, max $\nabla T_e$ | max $\nabla T_e$ (C-Mod GPI) | §3.2 |
  | Plasma-frame velocity at mode maximum | about $+1$ km/s | $+15$ to $+7$ km/s (C-Mod) | §3.2 |
  | Lab-frame velocity | about $-15$ km/s | electron diamagnetic (C-Mod) | §3.2 |
  | $E_r$ minimum | $-29$ kV/m (linear), about $-15$ (non-linear) | $-20\pm4$ kV/m | §3.2, §4.3 |
  | Frequency | about 35 kHz (linear), 8–18 kHz (non-linear) | 20–40 kHz | §4.3, Fig. 11 |
  | Poloidal wavenumber | 0.1–0.5 cm⁻¹ | AUG QCM 0.6–0.9; C-Mod 1.5; AUG QCE 0.4–0.9 | §4.3 |
  | $\delta T_e/T_e$, $\delta n_e/n_e$ | about 50%, 40% | large | §4.3 |
  | Losses | 2.5 MJ/s, $6.9\times10^{21}$ ions/s, continuous | ELM-free | §4.2 |

* **Phases:** linear to about 1.5 ms, early non-linear to about 2.2 ms,
  non-linear 2–6 ms. Time-averaged spectra (1, 2, 3 ms windows at 4 ms)
  order $n=3>2>1\approx4$ by eye, insensitive to the window.
* No code benchmark; a validation-type comparison with experiment. The
  GENE study of the same equilibrium (Stimmel et al. 2022) "did not find
  clear indications of the QCM", attributed to separatrix resolution.

# Notation map

| Cathey et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\psi_{\rm norm}$ | $\psi_N$ | |
| $n$, $m$ | $n$, $m$ | |
| $n_e$ | $n_e$ | **collision:** the paper writes $\nabla p/n$ with $n$ a density |
| $T=T_e=T_i$ | $T$ | each species temperature, not the sum |
| $p_e$, $p_\alpha$ | $p_e$, $p_s$ | |
| $E_r$ | $E_r$ (page-local radial component of $\mathbf E$) | |
| $Z_\alpha$, $n_\alpha$, $\mathbf v_\alpha$ | $Z$, $n_{\mathrm{imp}}$, $\mathbf v_{\mathrm{imp}}$ (page-local) | N⁷⁺ |
| $\mathbf B$, $B_t$ | $\mathbf B$, $B_\phi$ | sign convention not stated |
| $j_\varphi$, $\varphi$ | $j_\phi$, $\phi$ | |
| $q$, $q_{95}$ | same | |
| $\kappa$, $\delta$ (shape) | words (elongation, triangularity) | **collision:** registry $\kappa$ is heat conductivity, $\delta$ a perturbation |
| $\chi_\parallel/\chi_\perp$ | $\kappa_\parallel/\kappa_\perp$ | |
| $\gamma_n$ | $\gamma$ | s⁻¹ |
| $E_{{\rm mag},n}$ | $W_{\mathrm{mag}}^{(n)}$ | |
| $v_{\rm ExB}$ | $\mathbf v_E$ | |
| $\mathbf v_\parallel$ | $v_\parallel\mathbf b$ | |
| $\mathbf b_\theta$ | $\hat{\boldsymbol\theta}$ (page-local) | poloidal projection direction |
| $v^*_{i,\theta}$ | words (poloidal ion diamagnetic velocity) | not registered |
| $f_{\rm QCM}$, $f_n$ | $\omega/2\pi$, words | registry: $f$ is never a frequency |
| $k_\theta$ | words (poloidal wavenumber) | not registered |
| $\Phi$ | $\Phi$ | |
| $\Omega_i=eB/m$ | $\Omega_i$ | |
| $\sqrt{\mu_0\rho_0}$, $\delta t$ | JOREK time unit, $\Delta t$ | **collision:** native $\delta t$ vs registry $\delta(\cdot)$ |
| $\delta T_e/\langle T_e\rangle$ | $\delta T_e/\langle T_e\rangle$ | $\langle\cdot\rangle$ is the **toroidal** average here |
| $\langle n_e,T_e\rangle$ | words (cross-phase) | **collision:** registry $\langle\cdot\rangle$ is an average |
| $\nabla_R$ | $\partial_R$ | outer midplane |
| $\alpha_{\max}$, $\langle j_{\max}\rangle$ | $\alpha_{\mathrm b}$, words | MISHKA diagram axes, undefined in the paper |

# Pages created or updated

Chunk 2 (2026-10-16) created or updated the pages below. This source is cited on:

* [Ballooning mode](/definitions/ballooning-mode.md)
* [Bootstrap current and its MHD implementation](/definitions/bootstrap-current.md)
* [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md)
* [Edge-localized mode (ELM) and ELM-free regimes](/definitions/edge-localized-mode.md)
* [Implicit time integration and preconditioned Krylov solvers for nonlinear MHD](/methods/implicit-time-integration.md)
* [JOREK](/software/jorek.md)
* [Sheath (Bohm) boundary conditions](/methods/sheath-boundary-conditions.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2023_Crossref_Nuclear_Fusion_Cathey_Probing_non-linear_MHD_stability_of_the_EDA_H-mode_in_ASDEX.pdf`.
   * **Version.** arXiv:2301.09066v1 [physics.plasm-ph], 22 Jan 2023,
     "Submitted to: Nucl. Fusion", 12 pages; not the publisher version, so
     the published Letter may differ in wording, figures or numbers.
   * **Identity.** doi:10.1088/1741-4326/acc818, checked on Crossref by
     title: Nucl. Fusion 63(6), article 062001 (Letter), online 2023-04-11;
     the first 11 authors match, followed by the team names; title
     identical.
   * **How read.** Full text; no equations to check beyond the $E_r$ force
     balance and the velocity expressions; growth rates and spectra are the
     reader's approximate figure readings.
   * **Recorded as printed.**
     * Fig. 6 caption "m/n = 36/6, 42/6, and 48/6"; the legend shows 36/6,
       42/7, 48/8, all on $q=6$.
     * Fig. 4 labels the temperature "(eV)" with values 0–0.8; Fig. 10 gives
       the same profile in keV.
     * §3.2 points to "fig. 1 (d)" for the QCM frequency; the spectrogram is
       panel (c), (d) the heating power.
     * $E_r$: §2.2 and Fig. 4 say the non-linear minimum "matches" the
       experimental $-20\pm4$ kV/m; §4.3 says it is about $-15$ kV/m,
       "shallower than the experimental measurement"; the time of the Fig. 4
       profile is not stated. Unit typo "kv/m" (§3.2).
     * AUG QCM wavenumber 0.5–0.6 cm⁻¹ (§1) vs 0.6–0.9 cm⁻¹ (§4.3).
     * Frequencies: linear phase about 35 kHz, "{30…45}" (§4.3) and
       "{30…40}" (§5); non-linear "13 kHz" (Abstract, Fig. 11) and
       "{8…18}" kHz (§4.3, §5).
     * Dominant non-linear $n$: "{2…5}" (§4), "2 and 3" (§4.1), "from n = 7
       to n = 3" (§5).
     * "δTe/⟨Te⟩ ∼ 50 %" while the Fig. 11 traces span 0.2–1.8 (±80%
       peaks); 50% is typical, not maximal (reader's reading).
     * Fig. 2 axes $\alpha_{\max}$, $\langle j_{\max}\rangle$ are never
       defined.
     * "The time step … corresponds to $\sqrt{\mu_0\rho_0}$" reads as if the
       step defined the unit.
     * §2.2 "Using the former means that the radial electric field well …"
       has an unclear referent.
     * Footnote cites Labit et al. 2019 Nucl. Fusion 59 "0860020" (extra
       digit; 086020).
     * Typos: "advance SOL model", "wavenumers", "Alfvèn", "fig, 6".
   * **Reference list.** 39 printed entries, merged into the bibliography
     under `cathey-2023`, which also fills the stub of this paper cited by
     [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (adding the DOI). Ref.
     [37], "Physics of Plasmas (submitted), 2023", is the ingested
     [Korving et al. (2023)](/sources/korving-2023.md); [24] is the ingested
     [Hoelzl et al. (2021)](/sources/hoelzl-2021.md); `cathey-2021` is the
     published PPCF 63:075016 printed here. The Sauter erratum [33], page
     range printed "5140–2839" and only Sauter and Angioni as authors, is
     `sauter-2002-b`; [36], a personal communication without year, is
     `kalis-2023`; [16] Kallenbach, printed "nov 2020" for NF 61, is
     `kallenbach-2020`; [26] "Mc Carthy" is `mccarthy-1999`. Other printed
     defects: [15] authors end "and and."; [7] Viezzer 2022 has only a page
     number; [23] "and et al.". Existing keys reused include `zohm-1996`,
     `eich-2017`, `pamela-2020`, `sauter-1999`, `krebs-2013`,
     `morales-2016`, `cathey-2020`, `cathey-2022`. No DOIs are printed.

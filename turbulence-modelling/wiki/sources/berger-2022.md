---
type: Source
title: "Berger et al. (2022) — Synergistic interactions of thermodiffusive instabilities and turbulence in lean hydrogen flames"
description: "Detailed-chemistry DNS of lean hydrogen–air slot-burner jet flames at equal Reynolds and Karlovitz numbers, with and without thermodiffusive instability: turbulence amplifies the instability, the stretch factor rising to about 4, and an optimal-estimator analysis shows that the reaction rate needs mixture fraction as a second manifold coordinate."
resource: "doi:10.1016/j.combustflame.2022.112254"
source_kind: paper
authors: [Berger L., Attili A., Pitsch H.]
year: 2022
venue: "Combust. Flame 244:112254"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Combustion_and_Flame_Berger_Synergistic_interactions_of_thermodiffusive_instabilities_an.pdf"
tags: [combustion, dns, tabulated-chemistry]
timestamp: 2026-10-27T15:52:00Z
---

# Summary

Berger et al. (2022) run three-dimensional
[direct numerical simulations](/definitions/direct-numerical-simulation.md)
of lean ($\phi_{\mathrm{eq}}=0.4$, 298 K, 1 bar) premixed hydrogen–air
slot-burner jet flames with a burned-gas coflow, a 9-species 46-reaction
mechanism, low-Mach equations and fifth-order
[WENO](/methods/weno-scheme.md) convection of species and temperature. Case
TurbUnstable uses realistic constant Lewis numbers and the Soret effect;
case TurbStable uses unity Lewis numbers and no Soret effect, which
suppresses the thermodiffusive instability; half the slot width and twice
the bulk velocity keep both at $Re=11{,}000$ and $Ka\approx15$. A laminar
three-dimensional initially planar flame (LamUnstable) at the same
thermochemical state separates the effect of turbulence from that of the
instability.

The consumption speed is decomposed as $s_c=s_L(A/A_0)I_0$. TurbStable
reaches $s_c/s_L\approx5$ with $I_0\approx1$, a gain from flame area
alone; TurbUnstable peaks at $s_c/s_L\approx15$ with $I_0\approx4$, above
the laminar unstable flame's 2.6, a synergy of turbulence and instability.
In the flame-surface-density budget the surface-averaged tangential strain
scales with the Kolmogorov time in both flames,
$\langle K_{\mathrm t}\rangle_S\tau_\eta\approx0.28$, while the curvature
term differs: the unstable flame produces area in convex segments
propagating into the fresh gas, forming tongue-like structures.

For modelling, an optimal-estimator (irreducible-error) analysis of the DNS
shows that the progress-variable source term is not parametrized by the
progress variable alone, nor by adding stretch, strain or curvature, but is
by adding the mixture fraction $Z$: a manifold of
[flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
for these flames needs $Z$ as a coordinate. The analysis is made on the
DNS fields; no simulation with a tabulated manifold is run. Mixture-fraction fluctuations follow curvature, not strain;
the shift of the conditional mean of $Z$ above the flamelet is reproduced
by strained laminar counterflow flames at the mean tangential strain.

# Version read

Version of record (Elsevier typeset, Combust. Flame 244:112254; received
6 December 2021, available online 24 June 2022), 20 pages, all read; the
equations on pp. 6–8, 13 and 14 were read on the page images because the
text extraction garbles them. Page 1 matches the published title, authors
and DOI. The supplementary material (Tables A1–A2, Figs. A1–A13) is cited
but is not in the file; claims resting on it are marked.

# Key claims

1. Two DNS of lean ($\phi_{\mathrm{eq}}=0.4$) premixed hydrogen–air slot-burner flames at $Re=11{,}000$ and $Ka\approx15$ with detailed chemistry were run, one with realistic transport (TurbUnstable), one with unity Lewis numbers and no Soret effect (TurbStable) (Abstract, §2.1, Table 1). **Shown**
2. The flame without thermodiffusive instability burns locally like an unstretched laminar flame ($I_0\approx1$); its flame-speed gain comes from area alone, with maximum $s_c/s_L\approx5$ (§3.2, Fig. 7c). **Shown**
3. The unstable turbulent flame reaches a peak $s_c/s_L\approx15$ and $I_0\approx4$, while the maximum area ratio $A/A_0\approx4$–5 is similar in both flames (§3.2, Fig. 7). **Shown**
4. The stretch factor of the unstable turbulent flame ($I_0\approx4$) exceeds that of the unstable laminar flame ($I_0=2.6$): turbulence enhances the reactivity effect of the instability, a "synergistic effect" (§3.2, §3.5, §4). **Shown**
5. The surface-averaged tangential strain normalized by the Kolmogorov time is nearly constant along the flame, $\langle K_{\mathrm t}\rangle_S\tau_\eta\approx0.28$ in both flames, consistent with Rutland & Trouvé (0.28) and Luca et al. (0.24) (§3.3.1, Fig. 9). **Shown**
6. The PDFs of $K_{\mathrm t}$ in TurbUnstable are self-similar only when normalized by $\tau_\eta$, not by the flame time $\tau_{\mathrm F}$: area generation by strain is set by the small turbulent scales, not by flame-intrinsic mechanisms (§3.3.1, Fig. 10). **Shown**
7. The curvature term $\kappa_{\mathrm f}s_d$ is mostly negative (area destruction) in both flames; normalized by $\tau_\eta$ it is constant up to half the flame height in TurbStable, and constant under neither normalization in TurbUnstable (§3.3, §3.3.2, Figs. 8–9). **Shown**
8. TurbUnstable forms finger- or tongue-like structures convex towards the fresh gas with large positive stretch at their tips; TurbStable destroys its convex leading edges (§3.3.2, Figs. 11–12). **Shown**
9. In the quadrant split of $\langle\kappa_{\mathrm f}s_d\rangle_S$ over the joint PDF of curvature and displacement speed, quadrant $Q_2$ (concave, positive $s_d$; cusps) destroys area similarly in both flames; $Q_1$ (convex, positive $s_d$) gives a large positive contribution only in the unstable flames, absent in TurbStable and in the methane flames of Luca et al.; TurbStable has a small $Q_4$ contribution (§3.3.2, Figs. 13–14). **Shown**
10. The $Q_1$ and $Q_2$ contributions are larger in TurbUnstable than in LamUnstable, because turbulence enhances curvature fluctuations and the flame responds through $s_d$ (§3.3.2). **Shown**
11. The progress-variable source term of TurbStable follows the unstretched laminar flamelet closely; TurbUnstable scatters strongly through local equivalence-ratio variations (§3.4.1, Fig. 15). **Shown**
12. Optimal-estimator analysis: parametrizing the source term by $C_{\mathrm{H_2}}$ alone leaves large irreducible errors; adding $Z$ reduces them strongly; adding stretch, tangential strain or curvature, singly or together, helps much less; $(C_{\mathrm{H_2}},T)$ is about as good as $(C_{\mathrm{H_2}},Z)$ (§3.4.1, Fig. 16). **Shown**
13. The authors read claim 12 as the source term not being set by the instantaneous stretch, strain and curvature but possibly by their time history, whereas $Z$ results from differential diffusion (§3.4.1). **Stated**
14. Mixture-fraction fluctuations and the deviation of the conditional mean $\langle Z\mid C_{\mathrm{H_2}}\rangle$ above the flamelet are much larger in TurbUnstable than in LamUnstable (§3.4.1, Fig. 17). **Shown**
15. Super-adiabatic temperatures up to 400 K above the adiabatic 1418 K appear in TurbUnstable, over a broader range than in LamUnstable; TurbStable is narrow (§3.4.1, Fig. 18). **Shown**
16. Mixture-fraction fluctuations are caused by curvature, not by strain fluctuations: the irreducible error of $Z$ with $(C_{\mathrm{H_2}},K_{\mathrm t})$ is close to that with $C_{\mathrm{H_2}}$ alone, while $(C_{\mathrm{H_2}},\kappa_{\mathrm f})$ reduces it strongly (§3.4.2, Figs. 21–22). **Shown**
17. An irreducible-error analysis measures only the correlation of fluctuations and is blind to a shift of the mean, such as a larger mean strain (§3.4.3). **Stated**
18. The mean positive strain steepens scalar gradients; laminar counterflow flames at the same tangential strain reproduce the gradient at zero curvature; the mean strain is $\langle K_{\mathrm t}\rangle_S\tau_\eta\approx0.28$, or $\langle K_{\mathrm t}\rangle_S\tau_{\mathrm F}\approx6.5$, in the turbulent flames and $\langle K_{\mathrm t}\rangle_S\tau_{\mathrm F}\approx0.4$ in LamUnstable (§3.4.3, Figs. 23–26). **Shown**
19. With the TurbUnstable diffusivity model a counterflow flame at the matching strain has $s_c=0.49$ m/s against 0.17 m/s unstretched; with the TurbStable model 0.32 against 0.34 m/s (§3.4.4, Figs. 27–28). **Shown**
20. The conditional means $\langle Z\mid C_{\mathrm{H_2}}\rangle$ of TurbUnstable and LamUnstable agree with counterflow flamelets at $K_{\mathrm t}\tau_{\mathrm F}\approx6.5$ and 0.4: the shift to richer mixture is caused by the mean strain of the turbulence (§3.4.4, Fig. 29). **Shown**
21. In TurbUnstable reaction rates on the flame sheet reach 40 times the unstretched-flamelet value; the thinning of the front is overcompensated by the reaction rate, giving $I_0>1$; in TurbStable small changes of thickness and reactivity compensate to $I_0\approx1$ (§3.5, Figs. 24–25). **Shown**
22. Halving the lateral domain of LamUnstable changes the consumption speed but not the local flame state or the stretch factor (§2.1). **Stated** (evidence in the supplementary material, not read)
23. A TurbUnstable run at half resolution showed no significant effect on the statistics and conclusions (§2.2). **Stated** (evidence in the supplementary material, not read)
24. Coflow entrainment is negligible where the flames sit: the jet scalar $\xi_{\mathrm p}\approx1$ for all $C_{\mathrm{H_2}}<1$ at three heights, apart from minor near-inlet interaction in TurbStable (§3.1, Fig. 6). **Shown**
25. Theory expects intrinsic instabilities to matter mainly at low Karlovitz numbers, but Aspden et al. found thermodiffusive effects still at $Ka=100$ (§1). **Stated**

DNS set-up (§2.1–2.2, Table 1): TurbUnstable/TurbStable slot width 8/4 mm, bulk velocity 24/48 m/s, $s_L=0.17/0.34$ m/s, $l_{\mathrm F}=714/374$ µm, $\eta=180/90$ µm at half flame height, uniform spacing $h=70/35$ µm, $1792\times1024\times512$ and $3300\times1062\times512$ points; $\eta$ resolved at all times and $l_{\mathrm F}$ by ten points; semi-implicit finite differences, Crank–Nicolson, second-order momentum, fifth-order WENO for species and temperature, Strang splitting with CVODE chemistry, maximum CFL 0.5; statistics over at least one jet flow-through time, averaged in time and span.

# Printed slips

- §3.5: "As reaction rates are significantly larger in the TurbStable compared to the LamUnstable case due to the larger fluctuations of curvature and the mean positive strain rate and only a maximum increase of gradients by a factor of two is seen in the TurbStable case, a larger overcompensation occurs in the turbulent flame", while two sentences earlier "almost no effect on the flame reactivity is seen in the TurbStable case" and the comparison concerns the unstable flames.
- §3.4: "the stretch factor $I_0$ in Eq. (7)"; $I_0$ is introduced in Eq. (9).
- Table 1 prints $Ka=20$ and 16, and §2.1 says $\eta$ and $Ka$ are taken at half the jet height, while Eq. (2) with the Table 1 values gives $(714/180)^2\approx15.7$ and $(374/90)^2\approx17.3$; the ratio $6.5/0.28$ of §3.4.3 gives $\tau_{\mathrm F}/\tau_\eta\approx23$ *(compiler check, not in the sources)*.
- The Table 1 caption places $Ka$ "in the plateau region of Fig. 2", while §2.1 says "The value of Ka in Table 1 is taken at half of the jet height".
- Fig. 20 caption "PDF of curvature, strain rate, and stretch", panels in the order stretch, strain rate, curvature.
- "consumption seeds" (§2.1), "initialzied", "suﬃcienlty", "LamUnstbale" (§3.4.1, §3.4.3); Fig. 18 caption "or all cases"; §3.4.2 "or the source term".
- Ref. [29] (Zhou et al.) prints no title; names printed "C. Patano" [33], "S.S. Grimaji" [59] and "S. Stefano" (second author of [53]).

# Notation map

The registry holds only the thickened-flame symbols of combustion (§11);
the page-local symbols follow
[flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md).

| Berger et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\phi$ | $\phi_{\mathrm{eq}}$ (page-local equivalence ratio) | |
| $Re=UH/\nu_u$ | $Re$ on slot width and bulk velocity | |
| $Ka=(l_F/\eta)^2=\tau_F/\tau_\eta$ | $Ka$ (page-local) | |
| $l_F=(T_b-T_u)/\max\lvert\nabla T\rvert$, $\tau_F=l_F/s_L$, $s_L$ | $l_{\mathrm F}$, $\tau_{\mathrm F}$, $s_L$ (page-local) | thermal thickness, flame time, laminar burning velocity |
| $\eta$, $\tau_\eta$ | $\eta$, $\tau_\eta$ | from the Favre-averaged dissipation on the mean flame sheet |
| $\tilde C_{H_2}$, $\tilde\varepsilon$ | $\langle C_{\mathrm{H_2}}\rangle_\rho$, $\langle\varepsilon\rangle_\rho$ | **collision:** the tilde is a Favre (Reynolds-type) average, not an LES filter |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle$ | average over time and span |
| $\Delta$ | $h$ | **collision:** grid spacing, not a filter width |
| $C_{H_2}=1-Y_{H_2}/Y_{H_2,u}$, $C_0=0.8$ | $C_{\mathrm{H_2}}$, $C_0$ (page-local progress variable and iso-value) | |
| $Z$ (Bilger), $Z_{eq}$, $Z_{st}$ | $Z$, $Z_{\mathrm{eq}}$, $Z_{\mathrm{st}}$ (page-local) | 0.012 and 0.028 |
| $\xi$ | $\xi_{\mathrm p}$ (page-local passive jet scalar) | **collision:** not the reference coordinate $\xi$ |
| $s_c$, $A$, $A_0$, $I_0$ | consumption speed, flame areas, stretch factor (page-local) | $s_c=s_L(A/A_0)I_0$ |
| $\Sigma$, $\langle\cdot\rangle_S$ | flame surface density, surface average (page-local) | |
| $K=\kappa s_d+K_S$ | $K_{\mathrm{st}}=\kappa_{\mathrm f}s_d+K_{\mathrm t}$ (page-local stretch) | **collision** with $K$ |
| $K_S=\nabla\cdot\boldsymbol u-\boldsymbol n\cdot\nabla\boldsymbol u\cdot\boldsymbol n$ | $K_{\mathrm t}$ (page-local tangential strain) | without the curvature term, unlike the $K_{\mathrm f}$ of the flamelet page |
| $\kappa=\nabla\cdot\boldsymbol n$, $\boldsymbol n=-\nabla C/\lvert\nabla C\rvert$ | $\kappa_{\mathrm f}$, $\boldsymbol n_{\mathrm f}$ (page-local) | **collision:** not the von Kármán constant; positive convex towards the fresh gas |
| $s_d$, $s_d^*$, $a_N$ | displacement speed, density-weighted form, normal strain (page-local) | |
| $\dot\omega_C=-\dot\omega_{H_2}/Y_{H_2,u}$ | progress-variable source term (page-local) | **collision:** not the specific dissipation rate $\omega$ |
| $\boldsymbol\psi$, $\epsilon_{irr}$ | parameter set and irreducible error of the optimal estimator (page-local) | $\psi$ elsewhere the tabulated state |
| $Q_1$–$Q_4$ | quadrants of the curvature–displacement-speed PDF | |
| $D_i=\lambda/(\rho c_pLe_i)$ | species diffusivity (page-local) | **collision:** not the differentiation matrix |

# Reference list

66 printed references, numbered Elsevier style ([1]–[66]). The list is
merged complete into the [bibliography](/bibliography.md) with `citedby`
berger-2022. Ref. [1] is a report; ref. [29] prints no title and is entered
from its authors, venue and locator; refs. [44] (HYPRE) and [48]
(FlameMaster) are software items. Misspelled names are kept as printed in
notes. No printed duplicates or unparseable items.

# Pages created or updated

Chunk 9 (2026-10-27). This source is cited on:

- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)

---
type: Source
title: "Coulon et al. (2023) — Direct numerical simulations of methane, ammonia-hydrogen and hydrogen turbulent premixed flames"
description: "Three DNS of slot-burner premixed flames sharing laminar flame speed, thickness and synthetic inlet turbulence but differing in fuel Lewis number show that methane and stoichiometric ammonia–hydrogen burn by wrinkling alone, while lean hydrogen has a stretch factor up to 2.5, reproduced by strained counterflow flamelets."
resource: "doi:10.1016/j.combustflame.2023.112933"
source_kind: paper
authors: [Coulon V., Gaucherand J., Xing V., Laera D., Lapeyre C., Poinsot T.]
year: 2023
venue: "Combust. Flame 256:112933"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Combustion_and_Flame_Coulon_Direct_numerical_simulations_of_methane_ammonia-hydrogen_and.pdf"
tags: [combustion, dns, tabulated-chemistry, isotropic-turbulence]
timestamp: 2026-10-27T21:11:00Z
---

# Summary

Coulon et al. (2023) compare three 3-D [DNS](/definitions/direct-numerical-simulation.md)
of turbulent premixed slot-burner flames at 300 K and 1 bar: CH4/air at
equivalence ratio 1, NH3–H2/air (46% vol. H2 in the fuel) at 1, and H2/air
at 0.45. The mixtures share the unstretched laminar flame speed
($\approx0.38$ m/s) and thermal thickness ($\approx450\,\mu$m) of
stoichiometric methane, and the same synthetic
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
is injected at the inlet (random Fourier modes with a Passot–Pouquet
spectrum, [inflow turbulence generation](/methods/inflow-turbulence-generation.md)),
so all three sit in the thin-reaction-zones regime with $Ka\approx7.8$;
by design the mixtures differ in the fuel Lewis number (1, $\approx0.6$,
$\approx0.3$). The solver is AVBP (third-order Taylor–Galerkin
convection), with single-step, skeletal and analytically reduced chemistry.

The CH4 and NH3–H2 flames have nearly the same flame surface and brush
length and a stretch factor $I_0\to1$: the turbulent flame speed increase
comes from wrinkling (Damköhler's first hypothesis). The lean H2 flame is
about half as long, has less surface and $I_0>1$, rising from about 1 at
the foot to about 2.5 at the tip, with thin intensely burning flamelets at
positive curvature (thermo-diffusive instability) and near-extinction at
negative curvature. Flame–flame interactions in cusps raise the
displacement speed in all three flames ("kinematic restoration"), carried
in H2 by diffusion. Laminar counterflow flamelets over equivalence ratios
0.3–0.7 and strain rates up to twice the DNS mean give stretch factors
between 1 and 3, matching the DNS, and the authors propose them, together
with flame-surface-density wrinkling, as a model of stretch effects on
lean H2 propagation — a direction for
[flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md),
whose assumption $I_0\approx1$ the lean H2 flame breaks. A reference
surface for local statistics is built by Gaussian filtering to a
resolution of 5 points per thermal thickness, "a typical number of points
in the thermal thickness of a LES calculation" (the paper names no LES
combustion closure; the figure is recorded on the
[thickened flame model](/methods/thickened-flame-model.md) page). Evidence
is numerical; the paper has no turbulence closure.

# Version read

Version of record (Elsevier; received 7 December 2022, accepted 30 June
2023, online 14 July 2023), 14 pages, all read (pp. 3–4 also visually for
the equations and Table 1). Page 1 matches the metadata; no identity
issue. The supplementary material (Sections A–K: viscosity parameters,
mechanism validation, mesh convergence, spectral analysis of the shear
turbulence, 2-D laminar runs, definitions of the displacement speed and
stretch, diffusive-flux decomposition) is not in the file; claims resting
on it are marked **Stated**.

# Key claims

Page-local symbols: $\phi_{\mathrm{eq}}$ the equivalence ratio (global or
local); $Le_f$ the fuel Lewis number; $S_L^0$, $\delta_L^0=(T_b-T_u)/\max|\nabla T|$
the unstretched laminar flame speed and thermal thickness; $Ka$, $Re_t=(L/\eta)^{4/3}$
the Karlovitz and turbulent Reynolds numbers; $N_c=\delta_L^0/\Delta x$
points per thermal thickness; $c$, $c^*$ the progress variable and its
value at peak heat release of the unstretched flame; $\Sigma$ the flame
surface density; $S_d$, $S_d^{\mathrm{diff}}$, $S_d^{\mathrm{reac}}$,
$S_d^*=S_d\rho/\rho_u$ the displacement speed, its diffusive and reactive
parts, and its density-weighted form; $\kappa_{\mathrm f}=\nabla\cdot\boldsymbol n$
the flame curvature ($\boldsymbol n=-\nabla c/|\nabla c|$, toward the
fresh gas); $K_{\mathrm f}$, $K_s$, $K_c$ the total stretch, tangential
strain and curvature term; $S_T$, $A_T$, $A_0$ the turbulent consumption
speed, flame surface and reference surface; $I_0$, $I_0^*$, $I_0^{1D}$ the
stretch factor (global, from $S_d^*$, from counterflow flamelets);
$S_c^{1D}$ the counterflow consumption speed; $t_{\mathrm{ft}}=L_x/U_{\mathrm{bulk}}$
the flow-through time; HRR the heat release rate.

1. The three mixtures share $S_L^0\approx0.38$ m/s and $\delta_L^0\approx450\,\mu$m at $T_u=300$ K, $P=1$ bar (§2.2, Table 1). **Stated** (laminar values from Cantera)
2. All three flames are in the thin-reaction-zones regime of the Borghi–Peters diagram, $Ka=7.8$, 7.8, 7.7 and $Re_t=355$, 313, 271; the classification "should be interpreted with care" (Table 1, Fig. 2). **Stated**
3. The CH4 and NH3–H2 flames have the same flame surface $A_T$ over time; the H2 flame is significantly shorter with less surface ("twice as short", abstract) (Fig. 4). **Shown**
4. Once stationary, $I_0$ (computed as Attili et al.) tends to one for CH4 and NH3–H2 and exceeds one for H2 (Fig. 5). **Shown**
5. For H2, $I_0$ grows from about 1 at the flame foot to about 2.5 at the tip, "more than the flame wrinkling factor" (§3.3, Fig. 13c). **Shown**
6. $I_0^*=\langle S_d^*\rangle_S/S_L^0$ on the $c=c^*$ isosurface is close to the global $I_0$ in all three cases (§3.2, Fig. 12). **Shown**
7. CH4: for $x/H\le7$ positive and negative curvatures balance and surface production is strain-controlled; beyond, negative curvature (cusps, detachments) dominates and the curvature term drives surface destruction (§3.2, Figs. 6–7). **Shown**
8. Flame–flame interactions in cusps strongly increase $S_d$ ("kinematic restoration") in all three flames by modifying the heat and species diffusive fluxes (§3.2, Figs. 7a, 8, 11). **Shown** (attribution **Stated**, citing Lagrangian studies)
9. NH3–H2: weaker flame–flame interactions at trailing edges, and negative displacement speeds where small negative curvature lets diffusion outweigh a small reactivity (§3.2, Figs. 8b–c, 9c). **Shown**
10. H2: the total stretch is a positive source of flame surface density up to $x/H\approx3.5$, with $K_c\approx0$ there; the switch of stretch contributions occurs further upstream than in the other flames (§3.2, Figs. 10a, 11c). **Shown**
11. H2: in extreme cusps $S_d^{\mathrm{diff}}$ is strongly positive where the heat release almost vanishes ("tip-opening"); kinematic restoration is carried mainly by diffusive fluxes (§3.2, Figs. 10–11). **Shown**
12. CH4: the normalized $|\nabla c|$ is below one at large $|\kappa_{\mathrm f}|$ (thickening) and largest near zero curvature; large positive strain steepens gradients; heat release is not enhanced by curvature and decreases slightly with $K_s$ (§3.3, Fig. 14). **Shown**
13. NH3–H2 behaves like CH4 with slight thinning at positive curvature; its normalized heat release varies more but stays below one; the blend is thermo-diffusively stable at these conditions, "specific to the stoichiometric conditions and mixture proportions used in this study" (§3.3, Figs. 15, 19b). **Shown**
14. H2: thickened at negative curvature, steep at zero and positive curvature, asymmetric about zero; heat-release deviations from the laminar flame exceed a factor three at positive curvature (§3.3, Fig. 16a, c). **Shown**
15. H2: super-unity normalized heat release already for $x/H\le3.5$, with strong overconsumption on flat elements; heat release rises with positive $K_s$ before extinction "due to blow off" (§3.3, Fig. 16d). **Shown**
16. H2: the local equivalence ratio spans a wide range; hydrogen depletion near trailing edges goes with positive strain and local extinction; the curved tips of long-tail structures are "unconditionally" richer (§3.3, Fig. 17). **Shown**
17. Conditional mean gradients $\langle|\nabla c|\,|\,c\rangle$: CH4 nearly unaltered in the preheat zone and slightly steeper in the reaction zone; NH3–H2 the same; H2 significantly steeper from preheat to oxidation zone (Fig. 18). **Shown**
18. Conditional heat release: CH4 never exceeds the flamelet maximum; NH3–H2 lower in the reaction zone; H2 widely scattered and deviating in the preheat zone, while $c^*=0.85$ almost matches the maximum of its conditional mean, explaining $I_0^*\approx I_0$ (§3.3, Fig. 19). **Shown**
19. The stable stoichiometric NH3–H2 flame contrasts with the thermo-diffusively unstable lean ($\phi_{\mathrm{eq}}=0.45$), preheated (750 K) NH3–H2–N2 flame of Wiseman et al. and Rieth et al. ($I_0\approx2$); the authors attribute the difference to fuel proportions and operating conditions (§3.3). **Stated**
20. The strong stretch effect of lean H2 at $\phi_{\mathrm{eq}}=0.45$ was "not observed in calculations performed at richer conditions with $\phi=0.7$" (Song et al.); Berger et al. report even higher $I_0$ in leaner conditions ([berger-2022](/sources/berger-2022.md)) (§3.1, §3.3). **Stated**
21. Counterflow flamelets ($0.3<\phi_{\mathrm{eq}}<0.7$, strain $a_{\mathrm{cf}}$ from 0 to twice the isosurface mean $\langle K_s\rangle|_{c^*}=2436$ s$^{-1}$) give $1<S_c^{1D}/S_L^0<3$ for points sampled on the DNS isosurface, matching the DNS stretch factors (§3.4, Fig. 20). **Shown**
22. Near-flat DNS elements ($|\kappa_{\mathrm f}\delta_L^0|<0.01$) map to $S_c^{1D}/S_L^0\approx2$ except near the inlet: strain controls consumption where preferential diffusion is weak; positively curved rich elements give 2–3 irrespective of strain (§3.4, Fig. 20). **Shown**
23. As $\phi_{\mathrm{eq}}$ decreases, strain affects the counterflow consumption much less, so highly strained cusps are less affected than leading edges (§3.4). **Shown** (1-D flamelets)
24. Counterflow flamelets in strain–equivalence-ratio space can approximate stretch effects on lean H2 propagation in addition to wrinkling modelled by a flame-surface-density approach (§3.4, Conclusion). **Stated** (proposal, not implemented in LES)
25. Shear turbulence from the jet and coflow has no time to develop because the flames add viscous dissipation; the flames are controlled by the injected isotropic turbulence (§2.2; supplementary Section D). **Stated**
26. Resolution: $N_c\approx7$ (CH4), $\approx11$ (NH3–H2, H2); $\eta/\Delta x\approx0.5$, 0.7, 0.8; CFL 0.7; mesh convergence checked on H2 (Table 1, footnote 4; supplementary Section C). **Stated**

Inlet turbulence (Eqs. 2–3): $N=200$ random Fourier modes reproducing
$E(k)=16\frac{u'^2}{k_e}\sqrt{\frac2\pi}\big(\frac{k}{k_e}\big)^4\exp\big[-2\big(\frac{k}{k_e}\big)^2\big]$
with $u'=2.5$ m/s $=U_{\mathrm{bulk}}/10$ and $L=\sqrt{2\pi}/k_e=2.1$ mm
$=H/4$, injected in a central jet of width $H=8.53$ mm at
$U_{\mathrm{bulk}}=25$ m/s with burnt-gas coflows at 0.1 m/s. Meshes:
$1601\times401\times201$ ($\Delta x=64\,\mu$m, CH4),
$2191\times627\times314$ (41 μm, NH3–H2), $1281\times641\times321$
(40 μm, H2). The turbulent consumption speed and surface
(Eqs. 7–9): $S_T/S_L^0=I_0A_T/A_0$, $S_T=-(\rho_uY_{f,u}A_0)^{-1}\int_\Omega\dot\omega_f\,dV$,
$A_T=\int_\Omega|\nabla c|\,dV$; the flame surface density
$\Sigma=\langle|\nabla c|\,\delta(c-c^*)\rangle$ obeys
$\partial_t\Sigma+\nabla\cdot(\langle\boldsymbol u+S_d\boldsymbol n\rangle_S\Sigma)=\langle K_{\mathrm f}\rangle_S\Sigma$.

# Printed slips

- **§2.2:** "fuel Lewis number $Le_f=\lambda\rho C_pD$" and "Reynolds numbers $Re=U_{bulk}H\nu$" are printed as products, without division.
- **Table 1:** the time-step row is labelled "Δt [μm]" (values ≈ 0.062, 0.040, 0.043).
- **§3 against Table 1:** the density fields are "very similar so that $u'$ and $l_t$, as well as $Re_t$, are the same", while Table 1 prints $Re_t=355$, 313, 271.
- **Eq. (4):** $X_i$ are called "the molar mass fractions". *(Compiler check, not in the sources: with $X_{\mathrm{H_2}}=0.46$, $X_{\mathrm{NH_3}}=0.54$ and the printed $Le_{\mathrm{NH_3}}\approx0.9$, $Le_{\mathrm{H_2}}\approx0.3$, Eq. (4) gives 0.62, the printed $\approx0.6$.)*
- **Typos:** "stretch fator" (§3.1), "an arbitraly downsampling factor" (§3.3).
- **References:** [41], [42], [61], [62], [64] print no volume; [26], [27], [30] print article numbers without volume.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\phi$ | $\phi_{\mathrm{eq}}$ (page-local) | equivalence ratio |
| $S_L^0$, $\delta_L^0$ | $S_L^0$, $\delta_L^0$ (page-local) | **collision:** the registry's $S_L$ is the Lundquist number; concept pages write $s_{\mathrm L}$ |
| $u'$, $l_t$, $k_e$ | $u'$ (rms), $L$, $k_e$ | integral length $L=\sqrt{2\pi}/k_e$ |
| $\eta_k$ | $\eta$ | Kolmogorov length |
| $E(k)$ | $E(k)$ | Passot–Pouquet spectrum |
| $\omega^n$ (Eq. 2) | (mode frequencies) | **collision** with the specific dissipation rate |
| $\lambda$, $D$, $D_k$ | $\lambda_{\mathrm{th}}$ (page-local), $D_{\mathrm m}$ | **collision:** $\lambda$ is not the Taylor microscale |
| $\kappa$, $\kappa^\pm$ | $\kappa_{\mathrm f}$, $\kappa_{\mathrm f}^\pm$ (page-local) | **collision** with the von Kármán constant |
| $K$, $K_s$, $K_c$ | $K_{\mathrm f}$, $K_s$, $K_c$ (page-local) | **collision:** $K$ is the kinetic energy on spectral pages |
| $K_s^{1D}$ | $a_{\mathrm{cf}}$ | counterflow strain rate |
| $\Delta$, $\Delta x$ | $\Delta$, $\Delta x$ | Gaussian filter width of the reference-surface procedure; grid spacing |
| $\tau$ | $t_{\mathrm{ft}}$ (page-local) | flow-through time |
| $Re$, $Re_t$, $Ka$, $Le$, $Pr$ | $Re$ (jet, on $H$), $Re_t$, $Ka$, $Le$, $Pr$ | |
| $c$, $c^*$, $\Sigma$, $S_d$, $S_T$, $I_0$ | same (page-local) | |

# Reference list

77 printed references, numbered style. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug. Ref. [25]
is the ingested [berger-2022](/sources/berger-2022.md); same-author
same-year works are keyed in printed order (Aspden 2011, Berger 2022,
Pfitzner 2021, Song 2022) and matched by venue against works the
bibliography already holds under the same names. Ref. [43] is the Cantera
software (version 2.6.0). No item is unparseable.

# Pages created or updated

Chunk 11 (2026-10-27). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [Thickened flame model](/methods/thickened-flame-model.md)

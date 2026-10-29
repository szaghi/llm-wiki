---
type: Source
title: "Rahatgaonkar & Ghosh (2025) — Large eddy simulation of high Reynolds number compressible round jets: Insights into compressibility effects"
description: "Explicit-filtering approximate-deconvolution LES of isothermal, perfectly expanded round jets at Re 5e5 and jet Mach numbers 0.45, 0.9 and 1.8: longer potential core, lower spreading and decay rates, transitional anisotropy explained by the axial Reynolds-stress budget, and near-field noise rising with Mach number."
resource: "doi:10.1063/5.0293785"
source_kind: paper
authors: [Rahatgaonkar A.M., Ghosh S.]
year: 2025
venue: "Phys. Fluids 37:116106"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Physics_of_Fluids_Rahatgaonkar_Large_eddy_simulation_of_high_Reynolds_number_compressible_r.pdf"
tags: [les, compressible, approximate-deconvolution, filtering, aeroacoustics, anisotropy]
timestamp: 2026-10-29T05:14:00Z
---

# Summary

Rahatgaonkar & Ghosh (2025) study compressibility effects on spatially
developing, isothermal, perfectly expanded
[round jets](/benchmarks/turbulent-round-jet.md) at $Re_D=5\times10^5$
by [LES](/definitions/large-eddy-simulation.md) of three jets that differ
only in inflow centreline Mach number, $M_j=0.45$, $0.9$, $1.8$; earlier
LES of Mach effects (Maidi & Lesieur 2005; Bellan 2016; Bonelli et al.
2021) were at Reynolds numbers up to $3.6\times10^4$ by the paper's
account. The solver integrates the characteristic form of the
compressible Navier–Stokes equations (Sesterhenn 2000) in cylindrical
coordinates with Lele's sixth-order
[compact scheme](/methods/compact-finite-difference-scheme.md), low-storage
RK3 and the Mohseni–Colonius axis treatment. The LES model is the
single-step explicit-filtering variant of
[approximate deconvolution](/methods/scale-similarity-model.md) (Mathew et
al. 2003): every step the solution is filtered with $(Q_N*G)^2$, $Q_N$ the
van Cittert inverse with $N_{\mathrm{AD}}=6$ and $G$ a Padé filter, the
second filtering replacing ADM's relaxation term as regularization (the
[dissipation](/properties/numerical-dissipation.md) role of the unresolved
scales); no eddy viscosity is used and bulk viscosity is neglected. The
inflow is a tanh profile with vortex-ring forcing up to 3.3% of $u_0$
([inflow turbulence generation](/methods/inflow-turbulence-generation.md)),
with characteristic inflow, partially nonreflecting radial and sponge
outflow conditions, on $512\times128\times120$ points.

The $M_j=0.9$ jet is validated against LES and experiments, with
near-field OASPL within 1.5 dB of Bogey et al. (2007), taken directly from
the LES pressure (no [acoustic analogy](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)).
Raising $M_j$ elongates the transitional structures, lengthens the
potential core (+4.65% at 0.9, about +55% at 1.8, against 0.45; fit
$x_c/D=4.925+0.915M_j^2$ proposed against Lau et al.'s
$4.2+1.1M_j^2$), and lowers spreading and decay rates. All jets are
self-similar beyond $x=35r_0$. The supersonic jet has higher
Reynolds-stress anisotropy in the transitional region only, which the
authors attribute, from the Favre axial Reynolds-stress budget, to reduced
pressure–strain; reduced axial production they attribute to reduced mean
shear (transitional) and reduced Reynolds shear stress (fully turbulent).
Near-field pressure fluctuations rise with $M_j$ (OASPL above 135 dB at
$M_j=1.8$), and the authors propose Mach-wave radiation as an additional
source for the supersonic jet.
Statistics are of resolved scales only.

# Version read

Version of record (AIP; submitted 30 July 2025, accepted 14 October 2025,
published online 5 November 2025), 29 PDF pages (AIP cover plus article
pages 116106-1 to -28), all read; equation pages read visually. Page 1
matches the metadata. Numbering on this page is that of the version read.

# Key claims

Page-local symbols: $M_j$ the inflow centreline jet Mach number; $r_0$,
$D=2r_0$ the inflow jet radius and diameter; $u_0$, $\rho_0$ the inflow
centreline velocity and density; $u_{cl}$, $\rho_{cl}$ the mean
centreline velocity and density; $r_{0.5}$ the jet half-width; $x_c$ the
potential-core length ($\langle u\rangle_{cl}(x_c)=0.95u_0$); $A$, $B$
the spreading rate and centreline decay constant; $\alpha_{\mathrm f}$
the Padé filter parameter; cylindrical coordinates $(x,r,\theta)$.

1. The LES approach is a single-step explicit-filtering ADM: deconvolution and regularization are combined in one filtering with $(Q_N*G)^2$ every step, $N_{\mathrm{AD}}=6$, Padé filter $\alpha_{\mathrm f}=0.2$ in the azimuthal (periodic) direction and a physical-space filter of similar spectral behaviour elsewhere. §II B, Fig. 1. **Stated** (method from Mathew et al. 2003 and Stolz 2000)
2. The transfer functions of $Q_N*G$ and $(Q_N*G)^2$ both decay smoothly to zero at high wavenumber. §II B, Fig. 1. **Shown**
3. Azimuthal spectra of axial-velocity fluctuations at $r=r_0$, $x/r_0=30,40,50$ decay properly at the highest resolved wavenumbers, the Nyquist wavenumber lies in the inertial subrange, and a short segment follows $k^{-5/3}$ for all jets; taken as evidence that grid and LES approach are appropriate. §II D, Fig. 3. **Shown**
4. No spurious acoustic reflections from the boundaries are observed. §II C, Fig. 2. **Shown** (qualitative)
5. For $M_j=0.9$ the centreline decay matches reference LES and the experiment of Lau et al. (1979), with faster decay than Arakeri et al. (2003); the half-width agrees "excellently" with Bogey & Bailly (2005) and Thaker & Ghosh (2021); reference profiles are shifted axially to match the core length. §III A, Fig. 4. **Shown**
6. Self-similar intensities and shear stress for $M_j=0.9$, averaged over $35r_0\le x\le50r_0$ and scaled by $u_{cl}$ and $r_{0.5}$, agree with the LES of Bogey & Bailly (2009) and the experiment of Panchapakesan & Lumley (1993). §III A, Fig. 7. **Shown**
7. Near-field OASPL at $r=15r_0$ for $M_j=0.9$ is within 1.5 dB of Bogey et al. (2007), slightly overpredicted, partly attributed to the inflow momentum thickness ($\sim10^{-2}r_0$ here, $\sim10^{-3}r_0$ in experiments); it lies between the jetH and jetL cases of Bogey et al. (2008). §III A, Fig. 8. **Shown**
8. Raising $M_j$ suppresses the early breakdown of vortical structures: axisymmetric structures breaking down from $x\approx6r_0$ at $M_j=0.45$, elongated structures to $x\approx7.5r_0$ at 0.9, highly stretched structures, three-dimensional beyond $x\approx12r_0$, at 1.8; the radial extent of vortical activity shrinks. §III B 1, Fig. 9 ($Q_A=0.02u_0^2/r_0$). **Shown** (visualization)
9. $x_c$ grows by 4.65% at $M_j=0.9$ and about 55% at $M_j=1.8$ relative to $M_j=0.45$. §III B 1, Fig. 12. **Shown**
10. The fit $x_c/D=4.925+0.915M_j^2$ (Eq. 18) predicts $x_c$ up to $M_j=1.8$ better than Lau et al.'s $x_c/D=4.2+1.1M_j^2$ (Eq. 17) for isothermal perfectly expanded jets. §III B 1. **Shown** (fit to three LES points)
11. Decay and spreading start further downstream as $M_j$ rises; beyond $x=35r_0$ all jets spread linearly and decay as $x^{-1}$, with $A=0.108$, $0.086$, $0.060$ and $B=5.28$, $6.59$, $8.57$ for $M_j=0.45$, $0.9$, $1.8$. §III B 1, Table II, Figs. 13–14. **Shown**
12. The systematic reduction of both decay and spreading rates with $M_j$ was not distinctly identified by earlier lower-Reynolds-number studies; the present results "provide clear evidence of this trend". §III B 1, §IV. **Shown**
13. Mean axial-velocity profiles are self-similar at $x/r_0=35,40,45$ for all jets. §III B 1, Fig. 16. **Shown**
14. In the self-similar region the centreline Mach number of the subsonic jets drops to low subsonic values, while the supersonic jet stays high subsonic. §III B 1, Fig. 15. **Shown**
15. Compressibility damps the initial transition but allows larger peak axial RMS fluctuations in the transitional shear layer of the supersonic jet; the azimuthal peaks are lower and the radial peak decreases with $M_j$. §III B 2, Figs. 17–18. **Shown**
16. Peak turbulent kinetic energy along the shear layer decreases with $M_j$ and moves downstream, close to where large coherent structures begin to disintegrate. §III B 2, Fig. 19. **Shown**
17. At the station of maximum $k$, the radial stress exceeds the axial one at $M_j=0.45$, they are comparable at 0.9, and the axial stress is much larger at 1.8. §III B 3, Figs. 20–21. **Shown**
18. Peak Reynolds shear stress in the transitional region is comparable for all jets, "in contrast to the findings of Bellan", who reported an increase with compressibility for low-Re supersonic jets. §III B 3, Fig. 21(d). **Shown**
19. In the fully turbulent region ($35\le x/r_0\le50$) all stress components drop considerably from $M_j=0.45$ to 0.9 and less from 0.9 to 1.8, with no distinct change in anisotropy. §III B 3, Figs. 22–23. **Shown**
20. In the transitional region the peaks of axial production $\mathcal P_{xx}$ and pressure–strain $\phi_{xx}$ decrease with $M_j$ and move downstream; "the increased turbulence anisotropy in the transitional region is due to the reduced pressure-strain correlations". §III B 4, Fig. 24. **Shown** (the causal attribution is the authors')
21. In the fully turbulent region $\mathcal P_{xx}$ and $\phi_{xx}$ both decrease with $M_j$, without noticeable change in anisotropy. §III B 4, Fig. 25. **Shown**
22. Of the three parts of $\mathcal P_{xx}$ (Eq. 20), mean shear dominates in the transitional region, where mean-dilatation and extra-strain parts are small but grow with $M_j$; in the fully turbulent region the extra-strain part is comparable to the mean-shear part, the dilatation part small but not negligible, and all three decrease with $M_j$. §III B 4, Figs. 26–29. **Shown**
23. The reduction of $\mathcal P_{xx}$ with $M_j$ comes from reduced mean shear $\partial\langle u_x\rangle_\rho/\partial r$ in the transitional region and reduced Reynolds shear stress in the fully turbulent region. §III B 4, Figs. 21(d), 23(d), 30. **Shown**
24. To the authors' knowledge this is the first detailed analysis of production and pressure–strain explaining compressibility effects on round-jet turbulence intensities. §IV. **Stated**
25. RMS pressure along the shear layer peaks near $x\approx5r_0$, $8r_0$, $13r_0$ for $M_j=0.45$, $0.9$, $1.8$, strongly amplified at higher $M_j$, near the peak-$k$ location, in line with Bellan, who however reported a slight reduction of peak RMS pressure with $M_j$ at low Re. §III B 5, Fig. 32. **Shown**
26. Near-field OASPL at $r=15r_0$ peaks at $x\approx13r_0$, $21r_0$, $32r_0$; the supersonic peak exceeds 135 dB; Mach-wave radiation is suggested as an additional mechanism for the supersonic, shock-free jet. §III B 5, Figs. 31, 33; §IV. **Shown** (mechanism **Stated**)
27. The OASPL directivity at $r=15r_0$ moves to larger angles with $M_j$, in qualitative agreement with Brès & Lele (2019) at $28.6r_0$. §III B 5, Fig. 34. **Shown**
28. The changes with $M_j$ are associated with changes of the transitional large-scale structures rather than with the jet density ratio, though density-ratio effects in variable-density jets (Charonko & Prestridge 2017: $A=0.068$ at density ratio 1.2, $0.052$ at 4.2) follow the same trend. §III B 1. **Stated**

Eq. (18) gives $x_c/D=5.110$, $5.666$, $7.890$ at $M_j=0.45$, $0.9$, $1.8$, i.e. +10.9% and +54.4% relative to $M_j=0.45$, against the +4.65% and about +55% stated from the LES *(compiler check, not in the sources)*.

# Printed slips

- **Eq. (19) vs Eq. (20):** the second production term of Eq. (19) is printed $+2\bar\rho\widetilde{u''_xu''_x}\,\partial\tilde u_x/\partial x$, while Eq. (20) writes the corresponding part of $P_{xx}$ with a minus sign. The three parts of Eq. (20) sum to $-\overline{\rho u''_xu''_r}\,\partial\tilde u/\partial r-\overline{\rho u''_xu''_x}\,\partial\tilde u_x/\partial x$, half the "Production" group of Eq. (19) taken with that minus sign *(compiler check, not in the sources)*; which normalization the plotted $P_{xx}$ uses is not stated.
- **Eq. (20):** the mean-shear term writes $\partial\tilde u/\partial r$ without the subscript $x$ used in the text; the label reads "mean dialatation".
- **Eq. (5)** writes $X_s$, $Y_s$, $Z_s$ where Eq. (1) and the text write $X^s$, $Y^s$, $Z^s$.
- **Maidi & Lesieur:** the introduction gives "a Reynolds number of $3.6\times10^4$" and "The highest Reynolds number involved in the aforementioned studies was $3.6\times10^4$"; §III B 1 gives "$Re=7\times10^4$".
- **Overbar:** the LES filter $\bar u=G*u$ in §II B, the Reynolds average from §II D on.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar u=G*u$ (§II B) | $\bar u=G*u$ | LES filter |
| $\overline{(\cdot)}$ (§II D on) | $\langle\cdot\rangle$ | Reynolds average; **collision** with the §II B filter overbar |
| $\widetilde{(\cdot)}=\overline{\rho\,\cdot}/\bar\rho$ | $\langle\cdot\rangle_\rho$ | Favre average, not a Favre filter |
| $x'$, $x''$ | $\phi'$, $\phi''$ | Reynolds and Favre fluctuations |
| $R_{uu}$, $R_{vv}$, $R_{ww}$, $R_{uw}$ | $\langle\rho u_x''u_x''\rangle$, $\langle\rho u_\theta''u_\theta''\rangle$, $\langle\rho u_r''u_r''\rangle$, $\langle\rho u_x''u_r''\rangle$ | positive convention; the paper's $v$ is azimuthal, $w$ radial |
| $P_{xx}$, $\Pi_{xx}$ | $\mathcal P_{xx}$, $\phi_{xx}$ | production and pressure–strain of the axial Favre stress; $\phi_{xx}=2\langle p'\partial u_x''/\partial x\rangle$ |
| TKE | $k$ | definition not printed |
| $Q_N$, $N$ | $Q_N$, $N_{\mathrm{AD}}$ | van Cittert inverse, 6 terms; $N$ is not a polynomial degree |
| $u^*$ | deconvolved field | page-local |
| $\chi$ | $\chi_f$ | ADM relaxation strength, not used in this variant |
| $G$, $\hat G(\omega)$, $\alpha$ | $G$, $\hat G(k)$, $\alpha_{\mathrm f}$ | Padé filter, $\alpha_{\mathrm f}=0.2$ (page-local); **collision** with the DG blending $\alpha$ |
| $\tau_{ij}$, $s_{ij}$, $\Psi$ | $\sigma_{ij}$, $S_{ij}$, $\sigma_{ij}S_{ij}$ | viscous stress, strain rate, viscous dissipation; $\tau_{ij}$ is not the SGS stress |
| $\lambda$ | thermal conductivity | **collision** with the Taylor microscale |
| $C_p$, $C_v$ | $c_p$, $c_v$ | |
| $\theta_0$, $\theta$ | $\theta$ (momentum thickness), azimuth, observation angle | **collision** of the three uses of $\theta$ |
| $Q$ | $Q_A$ | isosurface $0.02u_0^2/r_0$ |
| $Re$ | $Re_D$ | on $D$ and $u_0$ |
| $u^l$, $\xi^l$, $g^{lm}$; $X^\pm$, $X^s$, $X^{v,w}$, … | page-local | curvilinear and characteristic-wave variables of the Sesterhenn form |
| $\eta_{1..4}$, $\sigma_1$, $\sigma_2$, $K$, $L_x$ | boundary-condition constants (3.58; 2.8 or 28) | page-local |

# Reference list

45 printed references, numbered AIP style, no DOIs printed, all parsed.
The list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Ref. 23 is Stolz's ETH thesis and ref. 37 Pope's
book; ref. 40 prints the article number "15-00496". The two Bogey 2006
works (refs. 1 and 18) are suffixed in printed order. No key falls on a
bundle source of a different work, and no item is printed twice.

# Pages created or updated

Chunk 15 (2026-10-28). This source is cited on:

- [Turbulent round jets](/benchmarks/turbulent-round-jet.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Vortex identification criteria](/definitions/vortex-identification-criterion.md)
- [Compact finite-difference schemes](/methods/compact-finite-difference-scheme.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)

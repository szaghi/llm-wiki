---
type: Source
title: "Aiello et al. (2026) — Impact of Structure-Preserving Discretizations on Compressible Wall-Bounded Turbulence of Thermally Perfect Gases"
description: "DNS of supersonic and hypersonic channel flow of thermally perfect CO2 in STREAmS comparing kinetic-energy-preserving convective schemes with and without exact entropy conservation: non-entropy-conservative schemes overpredict and drift in thermodynamic fluctuations, and the pressure-term discretization also matters at high Mach number."
resource: "doi:10.1007/s10494-026-00768-6"
source_kind: paper
authors: [Aiello A., Palumbo A., De Michele C., Coppola G.]
year: 2026
venue: "Flow Turbul. Combust. 117:8"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_Flow_Turbulence_and_Combustion_Aiello_Impact_of_Structure-Preserving_Discretizations_on_Compressib.pdf"
tags: [dns, compressible, hypersonic, kinetic-energy-preserving, entropy-stable, gpu]
timestamp: 2026-10-29T07:41:00Z
---

# Summary

Aiello et al. (2026) run [direct numerical simulations](/definitions/direct-numerical-simulation.md)
of compressible [turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
of CO$_2$ treated as a non-reacting thermally perfect gas (specific heats
$c_v(T)$, $c_p(T)$ from the NASA 7-coefficient polynomials), at wall-based bulk
Mach numbers 3, 4 and 5 and $Re_\tau\approx470$, 630 and 800. They measure
how the convective discretization, through its
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md),
its [entropy conservation](/properties/entropy-conservation.md) and its
consistency with the equation of state, affects robustness and statistics.

All schemes share a kinetic-energy-preserving mass and momentum flux and
differ in the density interpolant, the internal-energy flux and the pressure
term. The authors' EC-TP scheme (derived in a companion J. Comput. Phys.
paper) is entropy conserving for thermally perfect gases; Gouasmi et al.
(2020) is also entropy conserving but discretizes the pressure as
$R\{\!\{\rho\}\!\}/\{\!\{1/T\}\!\}$; Ranocha (2018) is entropy conserving only
for a calorically perfect gas and also
[pressure-equilibrium preserving](/properties/pressure-equilibrium-preservation.md);
KEEP (Kuya et al. 2018) is the [STREAmS](/software/streams.md) baseline. The
runs use STREAmS 2.1 on GPUs, sixth-order central differences and a WENO5
start-up transient ([WENO](/methods/weno-scheme.md)).

The schemes differ most in thermodynamic fluctuations: non-entropy-conservative
schemes overpredict pressure and density rms, which drift after long times,
while both entropy-conservative schemes stay stationary. As the Mach number
grows the differences reach velocity statistics: KEEP overpredicts the
Trettel–Larsson [transformed velocity](/definitions/compressible-velocity-transformation.md)
in the log region and the streamwise Reynolds stress (10.98% from EC-TP at
Mach 5), Gouasmi et al. less (5.25%). The authors conclude that entropy
consistency with the equation of state decides long-time robustness, that
entropy conservation of the convective terms is necessary but not sufficient,
and that EC-TP gives the best results.

# Version read

Version of record (Springer, open access CC BY 4.0; received 18 February 2026,
accepted 15 June 2026, online 26 June 2026), 23 pages, all read; the rotated
Table 1 (p. 11) and the EC-TP flux (p. 10) checked visually. Page 1 matches
Crossref. Locators are those of the published article.

# Key claims

1. To the authors' knowledge these are the first high-enthalpy channel-flow simulations of a thermally perfect gas with exactly entropy-conservative convective schemes (§5). **Stated**
2. Second-order kinetic-energy preservation requires the momentum flux $\mathcal F_{\rho u}=\mathcal F_\rho\{\!\{u\}\!\}$ (Jameson 2008b; Veldman 2019); the mass flux and the momentum pressure term stay free (§3.2). **Stated**
3. With the fluxes of Eq. 7, kinetic-energy preservation holds whatever the internal-energy flux; that flux and the density interpolant are degrees of freedom that can enforce entropy conservation (§3.2, Eq. 7). **Derived** (by reference to De Michele & Coppola 2023b)
4. For gases that are not calorically perfect, entropy-conservative fluxes designed for calorically perfect gases (Chandrashekar, Ranocha, asymptotic EC) lose entropy conservation but keep kinetic-energy preservation, which depends only on mass and momentum (§3.2). **Stated**
5. Entropy conservation for an arbitrary equation of state follows from discrete consistency with the Gibbs relation $\partial_t(\rho e)=T\partial_t(\rho s)+g\,\partial_t\rho$ (Aiello et al. 2025); the formulation is singular at uniform temperature, treated by the Ismail–Roe fix or an asymptotic expansion (§3.2). **Stated**
6. The EC-TP flux (p. 10) is entropy conserving and kinetic-energy preserving for thermally perfect gases with $c_v(T)=\sum_{m=-\ell}^{r}c_{v,m}T^m$ (§3.2, Table 1). **Stated** (derivation in Aiello et al. 2026, J. Comput. Phys.)
7. Gouasmi et al. (2020) is entropy conserving for thermally perfect gases and kinetic-energy preserving "according to our definition", but its pressure discretization spoils the kinetic-energy balance in isotropic turbulence (Aiello et al. 2026, J. Comput. Phys.; Gassner et al. 2016); it reduces to Chandrashekar (2013) for a calorically perfect gas (§4). **Stated**
8. Removing ghost nodes and using second-order boundary formulae improved robustness at hypersonic Mach numbers (negative temperatures appeared at ghost nodes in transients); preliminary Mach-3 runs showed a negligible effect of the boundary order reduction (§3.3). **Stated** (not shown)
9. Viscous terms in conservative form were more robust than the non-conservative form often used against odd–even decoupling (§3.3). **Stated**
10. All Trettel–Larsson profiles collapse on $u^+_{TL}=y^*$ in the viscous sublayer for every scheme and Mach number; a narrow log region appears for $y^*\ge40$, fitted with $\kappa=0.41$, $B=6.0$ on the entropy-conservative results (§4.1, Fig. 1). **Shown**
11. The large intercept $B=6.0$ is attributed to the low semi-local Reynolds number $Re^*_\tau$ (160 to 190), consistent with low-$Re_\tau$ incompressible flow and earlier calorically perfect supersonic channel DNS (§4.1). **Stated**
12. As the Mach number grows, KEEP overpredicts the transformed velocity in the log region; Gouasmi et al. departs from EC-TP more slowly, visibly at Mach 5 (§4.1, Fig. 1, Table 3). **Shown**
13. Max-norm relative differences from EC-TP of $u^+_{TL}$: KEEP 0.23% (Mach 3), 1.05% (Mach 4), 1.98% (Mach 5); Gouasmi 0.57%, 0.23%, 0.78%; Ranocha 0.55% (Mach 5) (Table 3). **Shown**
14. KEEP raises the peak of $R^+_{11}=\langle\rho u''u''\rangle/\tau_w$ in all cases, "abnormally high" at Mach 5; differences from EC-TP: KEEP 0.60%, 1.59%, 10.98%; Gouasmi 1.38%, 1.21%, 5.25%; Ranocha 1.32% (Mach 5) (§4.2, Fig. 2, Table 3). **Shown**
15. Isolating scheme features (EC-TP against Gouasmi: same convective part, different pressure term; EC-TP against KEEP: same pressure term, non-entropy-conservative convection) shows that both the lack of entropy-conservative convection and the pressure term $R\{\!\{\rho\}\!\}/\{\!\{1/T\}\!\}$ lead to inaccurate trends (§4.2). **Shown** (controlled comparison)
16. The turbulent shear stress $R^+_{12}$ shows no relevant scheme differences (§4.2, Fig. 2d–f). **Shown**
17. Non-entropy-conservative schemes overpredict thermodynamic fluctuations, especially pressure and density, which begin to drift after a long time in the stationary state; both entropy-conservative schemes stay statistically stationary over a run extended by 50% (§4.2, Fig. 3). **Shown**
18. Entropy conservation of the convective terms is the main factor for robustness; the pressure-term discretization matters less, mostly in the buffer layer at high Mach number (§4.2). **Shown**
19. Ranocha's scheme lies between the entropy-conservative and the non-conservative formulations, since it reproduces more structural properties than KEEP in the calorically perfect framework (§4.2, Table 3). **Shown** (Mach 5 only)
20. Wall-pressure rms $p'^+_w$: EC-TP 1.97, 2.33, 2.57; KEEP 2.89, 3.23, 3.55; Gouasmi 1.97, 2.31, 2.55; Ranocha 2.78 (Mach 5) for Mach 3, 4, 5 (Table 3). **Shown**
21. $C_f\times10^3$: EC-TP 6.78, 6.79, 6.96; KEEP 6.79, 6.67, 6.71; Gouasmi 6.84, 6.81, 6.89; Ranocha 6.97 (Mach 5); for EC-TP, $-B_q$ = 0.111, 0.172, 0.241 and $M_\tau$ = 0.126, 0.147, 0.164 (Table 3). **Shown**
22. The Trettel–Larsson transformation does not change the scheme differences appreciably (relative differences of $\langle u\rangle_\rho^+$ and $u^+_{TL}$ are close) (§4.2, Table 3). **Shown**
23. At Mach 5 the centreline temperature reaches about 1000 K, which amplifies the differences between calorically and thermally perfect models (§4.1). **Shown**
24. With entropy-conservative schemes no shock capturing was needed in a fully central framework here; strong shocks would still need it, and KEEP or Ranocha would in practice be hybridized with WENO, mitigating the issues at the price of dissipation (§4.2). **Stated**
25. Time integration may add entropy errors, "typically less significant in practice" than spatial ones (§3.3). **Stated**
26. Entropy consistency with the equation of state decides long-time robustness; entropy-conservative convection is necessary but not sufficient for accuracy; both entropy consistency and an appropriate thermodynamic coupling in the pressure term are essential (§5). **Shown** (as conclusion of §4)

# Printed slips

- §3.3: sample spacing "$\Delta t_s=1.5U_b/h$"; $U_b/h$ is an inverse time, so a time spacing reads $1.5\,h/U_b$ *(compiler check, not in the sources)*.
- §4.1: "for all the numerical tests reported in Table 1"; Table 1 includes the asymptotic AEC$^{(N)}$-TP scheme, which its caption says is not reported; the tests are those of Table 3.
- Table 2 caption: "supersonic channel flow at $M_b=3,4$", while the cases are labelled by $M_{bw}$, a different quantity defined in §2.1.
- Fig. 1 caption writes the log law in $y^+$ ("$u^+=6.0+1/0.41\log y^+$"), the text in $y^*$.
- The AEC row of Table 1 uses $\hat\rho$, $\hat T$, $\overline T^H$, not defined in the paper; $\hat\rho$ is also the generic density interpolant of Eq. 7.
- $c_f$ and the sign of $B_q$ are not defined; Table 3 lists "$-B_q$" with positive values.
- Reference list: Coleman et al. (1995) authors printed "Coleman, G.N., Kim, J., Moser, Moser, R.D.: R.D.:"; Moser et al. (1999) printed with the title of Lee & Moser (2015); Spina et al. pages "287–3191"; Kawai & Kawai (2025) with both authors "Kawai, S."; Wray (1991) without venue; Chase (1998) publisher city "???".

# Notation map

| Aiello et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\overline\phi=(\phi^i+\phi^{i+1})/2$ | $\{\!\{\phi\}\!\}$ | **collision:** the overbar is a two-point mean, not the LES filter |
| $\overline\phi^{\log}$ | $\phi^{\ln}$ (logarithmic mean, registry §11) | |
| $\overline{\overline{(u,p)}}$ | (product mean $(u^ip^{i+1}+u^{i+1}p^i)/2$) | page-local |
| $\overline{\overline T}^m$, $\widetilde{\widetilde T}^m$ | $\mathcal T_m$ (generalized two-point averages, page-local as on [entropy conservation](/properties/entropy-conservation.md)) | at equal states both reduce to $T^{m+1}$, not $T^m$ *(compiler check, not in the sources)*; **collision:** the tildes are not Favre filters |
| $\mathcal F^c_{\rho\phi}$, $\mathcal P_{\rho\phi}$ | $\mathcal F_{\rho\phi}$ (convective face flux, page-local as on [entropy conservation](/properties/entropy-conservation.md)), (pressure term) | |
| $\hat\rho$ | (density interpolant at $x_{i+1/2}$) | **collision:** not a test filter |
| $e$, $k=u_iu_i/2$, $E$, $H$ | (internal, kinetic, total energy and total enthalpy per unit mass) | **collision:** $k$ is not the turbulent kinetic energy |
| $s$, $g$ | (specific entropy, Gibbs free energy) | |
| $\tau_{ij}$ | $\sigma_{ij}$ | viscous stress |
| $\tau^+_{ij}=\langle\rho\rangle\widetilde{u''_iu''_j}/\tau_w$ | $R^+_{ij}=\langle\rho u_i''u_j''\rangle/\tau_w$ | positive convention; **collision:** $\tau$ is the SGS stress in the registry |
| $\tilde\phi$, $\phi''$ | $\langle\phi\rangle_\rho$, $\phi''$ | Favre average; **collision** with the registry tilde |
| $c_v(T)=\sum c_mT^m$, $c_m$, $\ell$, $r$ | $c_{v,m}$, $\ell$, $r$ (polynomial specific heat and its coefficients, page-local) | |
| $M_{bw}$, $M_b$, $M_\tau$ | (bulk Mach on the wall sound speed), $M_b$, (friction Mach) | |
| $Re_b$, $Re_\tau$, $Re^*_\tau$ | $Re_b$, $Re_\tau$, (semi-local $Re_\tau$) | half-width $h=\delta$, wall viscosity |
| $y^*$ | $y^*$ | semi-local wall distance, agrees |
| $u^+_{TL}$ | $u^+_{TL}$ | Trettel–Larsson velocity |
| $\kappa=0.41$, $B=6.0$ | $\kappa$, $B$ | |
| $c_f$, $B_q$ | $C_f$, (wall heat-flux coefficient) | |
| $N$ | (truncation order of the asymptotic expansion) | **collision:** not a polynomial degree |

# Reference list

72 printed references, author–year style, alphabetical. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
The cited Aiello, De Michele & Coppola (2026), J. Comput. Phys. 563:115053, is
a different work from this source and takes the key `aiello-2026-b`. No printed
duplicates; Moser et al. (1999) carries the title of Lee & Moser (2015), as
printed; Wray (1991) has no venue; Chase (1998) a garbled publisher city.

# Pages created or updated

Chunk 7 (2026-10-26). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Morkovin's hypothesis and Reynolds analogies](/definitions/morkovin-hypothesis.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Entropy conservation and entropy stability](/properties/entropy-conservation.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
- [STREAmS](/software/streams.md)

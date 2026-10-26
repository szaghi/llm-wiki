---
type: Source
title: "Löhrer & Fröhlich (2025) — Large-eddy simulation of the fluid–structure interaction in aquatic canopies consisting of highly flexible blades"
description: "Wall-resolved Smagorinsky LES with a direct-forcing immersed boundary method of open-channel flow over 672 two-way-coupled, highly flexible Cosserat-rod blades at Cauchy number 25 000, reporting a 12.4-fold drag increase, a displaced log law, sweep-dominated exchange and hull-triggered coherent structures."
resource: "doi:10.1017/jfm.2025.407"
source_kind: paper
authors: [Löhrer B., Fröhlich J.]
year: 2025
venue: "J. Fluid Mech. 1016:A4"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Journal_of_Fluid_Mechanics_Löhrer_Large-eddy_simulation_of_the_fluidstructure_interaction_in_a.pdf"
tags: [les, immersed-boundary, fluid-structure-interaction, eddy-viscosity, boundary-layer]
timestamp: 2026-10-26T15:49:00Z
---

# Summary

Löhrer & Fröhlich (2025) run a wall-resolved, high-resolution
[LES](/definitions/large-eddy-simulation.md) of turbulent open-channel flow over
and through a submerged aquatic canopy of 672 long, thin, highly flexible
ribbons. The configuration is a periodic, sidewall-free version of a flume
experiment, at $Re_H=20\,000$ and nominal Cauchy number $Ca=25\,000$, which the
authors say exceeds every earlier blade-resolved canopy simulation. Each blade
is a geometrically exact Cosserat rod, two-way coupled to the fluid by a
direct-forcing [immersed boundary method](/methods/immersed-boundary-method.md)
with zero-thickness marker sheets. A constraint-based collision model and a
lubrication model handle blade contact. The fluid solver is second-order finite
volume on a staggered Cartesian grid with the [Smagorinsky model](/methods/smagorinsky-model.md)
at $C_s=0.15$, damped near the blades with the immersed-boundary kernel.
Turbulence modelling is a tool here, not the subject: the paper is about canopy
fluid–structure interaction and coherent structures, and its fit to the bundle
is peripheral.

The canopy raises the drag 12.4 times over a smooth [channel](/benchmarks/turbulent-channel-flow.md)
at the same bulk Reynolds number. Above the canopy the mean velocity follows a
displaced form of the [law of the wall](/definitions/law-of-the-wall.md), whose
displacement height depends on the chosen $\kappa$. Quadrant analysis shows
sweeps dominating below about $1.5$ hull heights and ejections above. Hull
fluctuations correlate with the streamwise velocity, and conditional averages on
hull troughs and ridges recover sweeps and ejections flanked by counter-rotating
streamwise vortices. The LES quality is assessed with the Geurts–Fröhlich
activity parameter, the fraction of dissipation carried by the SGS model (mean
0.11), from which the authors call the run "close to a DNS". Their
[DNS](/definitions/direct-numerical-simulation.md) of the problem is declared
infeasible.

# Version read

Version of record (J. Fluid Mech., Cambridge University Press, open access CC
BY 4.0; received 1 August 2024, revised 25 January 2025, accepted 21 March
2025), 61 pages (A4-1 to A4-61), all read; Table 3 and Eq. (A2) checked
visually. Page 1 matches Crossref; no identity problem. Locators are the
journal's sections, equations, figures and tables.

# Key claims

Page-local symbols: $H$ flow depth, $U_b$ bulk velocity, $Re_H=U_bH/\nu$;
$h_c$ mean canopy-hull height (the source's $h$), $h^*$ mean tip height, $y_h$
the instantaneous hull height (the source's $\bar y$); $y_{vo}$ displacement
height, $u_{\tau,vo}$ its friction velocity, $\Delta U^+$ the roughness
function; $\lambda_f$ frontal-area density; $Q_\varepsilon$ the SGS activity
parameter.

1. The canopy raises the drag by $C_f/C_{f0}=12.4$ over a smooth channel at the same bulk Reynolds number, with $C_f\approx0.063$ from the driving force and $C_{f0}\approx0.0051$ from $C_{f0}\approx0.0549\,Re_H^{-0.24}$ (Pope 2000) (§5.3, Eqs. 5.12–5.14). **Shown**
2. The configuration has $Re_H=20\,000$, $Ca=25\,000$, buoyancy number 140, blade-to-ground area ratio 2.8, blade length $1.6H$, thickness-to-width ratio 0.0042, $Re_{\tau,vo}=2638$, $\lambda_f=0.56$, $h_c/H=0.20$, $y_{vo}/h_c=0.91$ and nominal reduced velocity 395 (Table 3). **Shown** (the independent numbers are set a priori, the others come from the simulation)
3. This Cauchy number exceeds those of all earlier simulations of canopies with resolved flexible blades (§1.2–1.3, Table 1). **Stated**
4. Above the canopy the mean velocity obeys the displaced log law (5.7), $u^+=\kappa^{-1}\ln[(y-y_{vo})u_{\tau,vo}/\nu]+B-\Delta U^+$ with $B=5.5$. A fit over $2.5h_c\le y\le0.8H$ with $\kappa=0.41$ gives $y_{vo}=0.18H$, $\Delta U^+=15.4$, $u_{\tau,vo}=0.16U_b$; fitting $\kappa$ too gives $\kappa=0.38$, $y_{vo}=0.13H$, $\Delta U^+=17.4$, $u_{\tau,vo}=0.17U_b$, so the displacement height is sensitive to $\kappa$ (§5.2). **Shown**
5. $y_{vo}=0.18H<h_c=0.20H$, consistent with the heuristic of Nicholas et al. (2023) that the canopy height bounds $y_{vo}$ from above, which may therefore extend to very flexible, slightly buoyant canopies (§5.2). **Shown**
6. $\Delta U^+$ equals that of case DE of Monti et al. (2020), a rigid upright canopy with the same $\lambda_f=0.56$, supporting a monotonic growth of $\Delta U^+$ with $\lambda_f$ (§5.3, Fig. 6b). **Shown** (comparison)
7. $-\langle u'v'\rangle$ peaks at $y=0.34H$, above $h^*=0.25H$, whereas lower-Cauchy flows peak at $y\approx h^*$; normalized, $-\langle u'v'\rangle_{\max}/\Delta U^2=0.010$ with $\Delta U=1.34U_b$, within the literature range 0.017 (rigid) to 0.008 (flexible with monami) (§5.2). **Shown**
8. The $\langle v'v'\rangle$ and $\langle w'w'\rangle$ maxima lie at $y/h^*=1.36$, inside the range $0.98\le y/h^*\le1.83$ measured by Ghisalberti & Nepf (2002) (§5.2). **Shown**
9. Vegetation drag is the dominant force up to $y\approx2h_c\approx0.4H$; between the lower and upper inflection points of $\langle u\rangle$ the viscous term changes sign; canopy drag equals turbulent shear stress at $y=y_{vo}$ (§5.3, Figs. 7–8). **Shown**
10. With the immersed boundary method the double-averaged canopy force equals the averaged coupling force (Eq. 5.5), checked numerically, so the form/viscous drag split of classical double averaging is unavailable; the frontal-area and drag profiles suggest viscous forces carry more of the drag in the upper canopy (§5.1, §5.3, Fig. 9). **Shown** / **Derived**
11. Blade-shape fluctuations are smallest in $x$ and largest in $z$; the spanwise fluctuation grows almost linearly with arc length, exceeds the vertical one beyond $s=0.28L$, and is about 1.56 times the vertical one at the tip (the abstract states 1.5) (§6.1, Fig. 11). **Shown**
12. The first cantilever Euler–Bernoulli mode dominates vertical and spanwise deflection; modal amplitudes decrease monotonically with mode number; ten modes reconstruct the shape well (§6.2, App. E). **Shown**
13. The added fluid mass is 99.5% of the effective blade mass; the natural period is $139H/U_b$, far longer than the fluid time scales, so blade elasticity is "not physically relevant" for the dynamics (§3.1). **Derived**
14. The nominal reduced velocity is 395; read from the tip spectra the effective reduced velocity is $\lesssim28$ (§3.1, §6.3, App. F). **Shown** / **Derived**
15. Dense blade–blade interaction gives the canopy the effective stiffness of a blade of length $h_c/2\lesssim l\lesssim h_c$, "an increase of stiffness ... by a factor of about 8", to be accounted for in modelling (§6.3, App. F, Fig. 37). **Derived** (lumped model fitted to spectra)
16. Tip-velocity spectra peak at $(0.6,0.4,0.3)\,U_b/H$ in $(x,y,z)$, independent of the in-vacuo natural frequency, and fall to zero near $f\approx10U_b/H\approx U_b/W$ ($W$ blade width), attributed to low-pass filtering by the blade width (App. F, Figs. 34–35). **Shown**
17. At low frequency the tip-velocity spectrum scales as $f^2$, from the transfer function of a forced oscillator for $\omega\ll\omega_n$; at high frequency it should scale as $f^{-5/3-2}$ (App. F, Eqs. F2–F6). **Derived**
18. The canopy hull, the smoothed height of the uppermost blade point, has mean $h_c=0.20H$ and a PDF reaching $0.6H$; the authors prefer it to a threshold on the smoothed solid volume fraction (§6.4, App. G, Fig. 14). **Stated** (definition) / **Shown**
19. Quadrant analysis: sweeps dominate momentum exchange below $y\approx0.3H\approx1.5h_c$, ejections above; the sweep-dominated layer spans about 386 units of $\nu/u_{\tau,vo}$, much thicker than the $y^+<15$ layer over smooth walls; quadrants 1 and 3 peak near $y=h_c$, 2.7 times weaker than sweeps (§7.1, Fig. 15). **Shown**
20. The correlation coefficient $-\langle u'v'\rangle/(\langle u'u'\rangle\langle v'v'\rangle)^{1/2}$ peaks near $y\approx0.5H$, well above the $-\langle u'v'\rangle$ peak at $0.34H$ (§7.1, Fig. 15a). **Shown**
21. Two-point correlations at $y=h_c$ give a streak spacing of about $0.75H$ and structures inclined about 6:1, as in smooth- and rough-wall open channels; streamwise correlations have no negative lobe (§7.2, Figs. 18–19). **Shown**
22. The hull height correlates negatively with $u'$ (coefficient $\approx-0.6$ at $y=h_c$): high-speed streaks press the hull down, low-speed streaks go with ridges (Fig. 20). **Shown**
23. Premultiplied spectra of $u'$ at $y=h_c$ and of the hull height peak at $\lambda_x\approx2.5H$, $\lambda_z\approx1H$; the hull's $\lambda_z\approx1.25H$ (plain spectrum) exceeds the $0.6H$ of Monti et al. (2023) (§7.2, App. J, Figs. 21–22, 44). **Shown**
24. Conditional averages: troughs (hull $0.06H$ at the centre) are sweeps flanked by counter-rotating streamwise vortices that push blades apart, trough width $1.04H$; ridges ($0.44H$) are ejections with the opposite rotation, width $0.92H$, with a shear-stress maximum near $y\approx2h_c$; streak spacing $\approx0.55H$ in both (§7.3, Figs. 23–25). **Shown**
25. The trough structure resembles the head-down structure linked to monami by Tschisgale et al. (2021), although no monami occurs here; their combined Kelvin–Helmholtz/head-up structures are not seen (§4.2, §7.3, §8). **Shown** (qualitative)
26. LES quality: $Q_\varepsilon\approx\nu_t/(\nu_t+\nu)$ has mean 0.11, 95% of values below 0.23 and a local maximum about 0.3; the SGS contribution to the mean drag is smaller than the viscous one everywhere and vanishes above the canopy edge; the authors call the run "a high-resolution LES ... close to a DNS" (App. C, Figs. 28–29). **Shown**
27. Grid study on the half-size domain: medium ($W/\Delta z=24.4$) to fine (48.8) changes the mean velocity by at most $\approx0.05U_b$, the resolved shear stress by about 18% and the kinetic energy by about 9%; the fine run used a doubled CFL number, so its fluctuation profiles are "likely to be underestimated"; halving the horizontal domain changes little (App. B, Table 6, Fig. 27). **Shown**
28. Inside the canopy the spectra show weak traces of the spectral shortcut; at $y=h_c$ and $0.75H$ they follow $k^{-5/3}$ for $2\pi/H\lesssim k\lesssim10\pi/H$; at $0.75H$ the $v'$ and $w'$ spectra collapse at high $k_x$, which the authors say is not observed in a flat-plate boundary layer (App. I, Figs. 41–43). **Shown**
29. In Tschisgale et al. (2021) halving and doubling $C_s$ had practically no effect, and the present runs use the same SGS model and constant (§3.3). **Stated** (cited)
30. DNS of this problem is "not feasible due to excessive computational resources"; the production run cost 1.3 Mcore-h on CPU clusters (§3.2–3.3). **Stated**

The activity parameter (App. C, Eqs. C1–C3) in registry notation:
$$Q_\varepsilon=\frac{\varepsilon_{\mathrm{sgs}}}{\varepsilon_{\mathrm{res}}+\varepsilon_{\mathrm{sgs}}},\qquad \varepsilon_{\mathrm{res}}=\nu\,\bar S_{ij}\partial_j\bar u_i,\quad \varepsilon_{\mathrm{sgs}}=\nu_t\,\bar S_{ij}\partial_j\bar u_i,\qquad Q_\varepsilon\approx\frac{\nu_t}{\nu_t+\nu},$$
$Q_\varepsilon=0$ for DNS and 1 for LES at infinite Reynolds number (Geurts &
Fröhlich 2002; Celik et al. 2005). The source prints neither the formula for
$\nu_t$ nor the filter width.

# Printed slips

- **§3.1:** "$T_f^{-1}=0.075\,u_\tau^2/(2\pi\nu)=0.2\,H/U$": the right-hand side has the dimension of a time, so the printed value is that of $T_f$, not $T_f^{-1}$ *(compiler check, not in the sources)*.
- **App. A, Eq. (A2) context, p. A4-37:** "$u_\tau^0/U_b^0=\sqrt{c_f^0/2}=15.66$": a ratio $u_\tau/U_b$ is below 1; 15.66 is the inverse ratio, $1/15.66\approx0.064$ *(compiler check, not in the sources)*.
- **App. B:** "maximum absolute difference ... $0.0034\,U^2\approx(0.0058\,U)^2$"; $\sqrt{0.0034}=0.058$ *(compiler check, not in the sources)*.
- **§6.1:** "Streamwise and spanwise deflections are overall well correlated, with ... $-\rho_{c_xc_y}\gtrsim0.5$ in figure 11(b)": the coefficient and the Fig. 11(b) caption concern streamwise and **vertical** deflections, and the next sentence says the streamwise–spanwise coefficient vanishes by symmetry.
- **§6.3:** "an increase of stiffness ... by a factor of about 8" when $L$ is replaced by $l$ with $h_c/2\lesssim l\lesssim h_c$: with the paper's own $k(l)=3EI/l^3$ (Eq. F7c) the stiffness scales as $(L/l)^3$, while 8 is the length ratio $L/h_c$ *(compiler check, not in the sources)*.
- **Okamoto & Nezu citations:** the text cites "2009", "2010a" and "2010b"; the reference list has entries labelled "2010", "2010a" and "2010", with no 2009 and no 2010b.
- **Domain extent:** $9.22H\times H\times4.03H$ in §3.2 against $9.23\times1\times4.04$ for case Coarse in Table 6, described as identical apart from the grid.
- **App. G:** the hull grid is said to use "24" points per blade width $W$, while Eq. (G2), $N_{it}=\sigma^2(1/\Delta_x^2+1/\Delta_z^2)$ with $\sigma=W/2$, gives $2\cdot12^2=288$ iterations at that spacing, not the printed $N_{it}=66$ *(compiler check, not in the sources)*.
- **Fig. 3 caption:** "(a) streamwise, (b) vertical, (b) spanwise"; **Table 4:** "Makers per blade element"; reference list: "Nezu & Sanjou 2008 Turburence structure", and the Guiot De La Rochère et al. (2022) author list printed with given names as surnames.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf u=(u,v,w)$, $x,y,z$ | $u_i$, $x,y,z$ | $y$ vertical (wall-normal), as in the registry |
| $\langle\cdot\rangle$, $\langle\cdot\rangle_t$, $\langle\cdot\rangle_{xz}$ | $\langle\cdot\rangle$ | space–time (double), time and plane averages of the resolved field; no filter bar printed |
| $\tilde u$ | page-local | dispersive (spatial) deviation of the time average; **collision** with the Favre tilde |
| $\boldsymbol\tau_{sgs}=-\rho\nu_{sgs}2\mathbf S+\tfrac13\mathrm{tr}(\boldsymbol\tau_{sgs})\mathbf I$ | $\bar\rho\,\tau_{ij}$, $\tau^d_{ij}=-2\nu_t\bar S^d_{ij}$ | dynamic form, enters as $\boldsymbol\sigma_h-\boldsymbol\tau_{sgs}$; same sign as the registry |
| $\nu_{sgs}$, $C_S$ | $\nu_t$, $C_s$ | $C_s=0.15$; filter width not printed |
| $\Delta_g=\sqrt[3]{\Delta x\Delta y\Delta z}$ | page-local | immersed-boundary marker spacing |
| $K$ | $k$ | resolved turbulent kinetic energy |
| $\kappa$, $A$, $\Delta U^+_{vo}$ | $\kappa$, $B$, $\Delta U^+$ | $B=5.5$; $\Delta U^+$ page-local roughness function |
| $B$ (buoyancy number) | page-local | **collision** with the log-law intercept $B$ |
| $u_{\tau,i}$, $\ell_\tau$ | $u_\tau$, $\delta_\nu$ | in-canopy wall friction velocity, $u_\tau=0.026U_b$ |
| $u_{\tau,vo}$, $\ell_{\tau,vo}$, $y_{vo}$ | page-local | friction velocity, length and displacement height of the displaced log law |
| $Re_{\tau,vo}=u_{\tau,vo}(H-y_{vo})/\nu$, $Re_\tau$ (§5.3) | page-local, $Re_\tau$ | two different friction Reynolds numbers |
| $U$, $H$, $Re_H$ | $U_b$, $H$, $Re_H$ | page-local bulk velocity and flow depth |
| $h$, $h^*$ | $h_c$, $h^*$ | **collision:** $h$ is the registry's cell size |
| $\bar y(x,z;t)$ | $y_h$ | **collision:** the overbar is not a filter here |
| $\lambda$, $\lambda_L$ | $\lambda_f$, page-local | **collision** with the Taylor microscale; also wavelengths $\lambda_x,\lambda_z$ and the $\lambda_2$ criterion |
| $\kappa_x$, $\kappa_z$ | $k_x$, $k_z$ | **collision** with the von Kármán constant |
| $\alpha$ | page-local | $2\pi/1.875^2$, solid volume fraction and modal coefficient; **collision** with the DG blending factor |
| $\rho_{u'v'}$ | page-local | correlation coefficient |
| $Q_\varepsilon$, $\varepsilon_{res}$, $\varepsilon_{sgs}$ | page-local | activity parameter, App. C |
| $Ca$, $U_r$, $Ga$ | page-local | Cauchy, reduced-velocity and Galilei numbers |

# Reference list

143 printed references in JFM author–year style, alphabetical, unnumbered, no
DOIs printed; merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. The cited Löhrer, Krause & Fröhlich (2025,
arXiv:2503.19741, collision model) is a different work whose rule key equals
this slug; it is a distinct preprint entry, keyed `lohrer-2025-b`.
Same-author same-year works keyed in printed order (Foggi Rota 2024a/b, Löhrer
& Fröhlich 2023a/b, Nepf 2012a/b, Tschisgale 2020 thesis and Tschisgale &
Fröhlich 2020, Vowinckel 2017a/b, the three Okamoto & Nezu 2010 entries; see
the printed slips for their labels). Recorded as printed: the garbled
Guiot De La Rochère et al. (2022) author list, Bartlett (1950) "Biometrika 1
(2)", Ghisalberti & Nepf (2002) "107 (C2), 3", a web page (Hadley 2024), an
edited volume (Salvetti et al. 2011) and a report (Dong 1978).

# Pages created or updated

Chunk 6 (2026-10-26). This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)

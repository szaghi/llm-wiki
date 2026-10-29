---
type: Source
title: "Smagorinsky (1963) — General circulation experiments with the primitive equations: I. The basic experiment"
description: "A 60-day two-level hemispheric primitive-equation general-circulation experiment whose subgrid motions are represented by a nonlinear lateral diffusion with an exchange coefficient set by the grid size and the local horizontal deformation: the founding source of the Smagorinsky subgrid model, with its constant 0.28 and an inertial-subrange justification."
resource: "doi:10.1175/1520-0493(1963)091<0099:GCEWTP>2.3.CO;2"
source_kind: paper
authors: [Smagorinsky J.]
year: 1963
venue: "Mon. Weather Rev. 91:99-164"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/1963_Crossref_Monthly_Weather_Review_SMAGORINSKY_GENERAL_CIRCULATION_EXPERIMENTS_WITH_THE_PRIMITIVE_EQUATIONS.pdf"
tags: [les, sgs-model, eddy-viscosity, atmospheric-flows]
timestamp: 2026-10-29T16:19:00Z
---

# Summary

Smagorinsky (1963) integrates a two-level, hemispheric, baroclinic
primitive-equation model of the atmosphere for 60 days ("EXP-8") and
diagnoses its energetics, heat and angular-momentum balances, mean zonal
wind and meridional circulation against observations. The paper is a
meteorology paper; the bundle cites it for one ingredient, the closure of
the motions smaller than the grid, which is the origin of the
[Smagorinsky model](/methods/smagorinsky-model.md).

The model's lateral (horizontal) friction is a nonlinear diffusion of
momentum and heat whose exchange coefficient is $(k_H\Delta)^2|D|$: $\Delta$
is the grid increment (555 km), $|D|$ the magnitude of the horizontal
deformation built from the tension and shearing strains, and $k_H\approx0.28$
(§4, Eqs. 4.22–4.26). It is a down-gradient eddy-viscosity closure in the
sense of the [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md),
applied on constant-pressure surfaces, and the same factor
$(k_H\Delta)^2$ is used for heat with half the deformation magnitude, with no
[turbulent Prandtl number](/definitions/turbulent-prandtl-number.md) named.
The justification (§14), without the term
[large-eddy simulation](/definitions/large-eddy-simulation.md): if the grid
scale lies in an inertial subrange and energy does not accumulate in the
subgrid scales, the energy removed at grid scale must equal the implied
molecular dissipation; without the term, energy piles up at the highest
resolved wavenumber (Phillips' "non-linear computational instability"), and
an energy-conserving difference scheme does not remove the need for it (see
[numerical dissipation](/properties/numerical-dissipation.md)). The
derivation from "Heisenberg similarity theory" is deferred to a separate
paper in preparation.

The general-circulation results: from random temperature disturbances the
model selects zonal wave numbers 5–6 and an index cycle of 11–12 days,
lengthening to 17 days after day 40; the mean jet (40 m s⁻¹) is too
intense; the lateral subgrid diffusion carries a large share of the eddy
transfer of heat and momentum, which the author judges intuitively too
large, and the model's dissipation is called "naturally suspect" against
observational estimates.

# Version read

Version of record: a scan of the typeset issue (Monthly Weather Review 91,
No. 3, March 1963; manuscript received 5 October 1962, revised 18 January
1963), 66 pages (pp. 99–164), all read. The OCR layer garbles every
equation, so equations and constants were read visually from the page
images. Page 1 matches the Crossref metadata; no DOI is printed on the
scan. Numbering cited on this page is that of the paper.

# Key claims

Page-local symbols: $k_H$ the lateral-diffusion constant; $D_T$, $D_S$ the
horizontal tension and shearing strains and $|D|$ their magnitude; $m$ the
Mercator map factor; $F^{\mathrm H}_x$, $F^{\mathrm H}_y$ the lateral
friction force; $H$ the lateral heat-diffusion term; $\Phi_{\mathrm{th}}$
the 250–750 mb thickness departure (the source's $\hat\Phi$); $|D|_\Sigma$
the source's $|\bar D|$, the overbar marking the sum of the two levels;
$\gamma^2_{\mathrm{st}}$ the effective static-stability measure (the
source's $\gamma^2$). Here $x$ is eastward and $y$ northward on the map;
the smooth lateral walls are at $y=0$ and $y=Y$.

1. The subgrid motions are represented by a nonlinear lateral diffusion of momentum and heat "through an exchange coefficient which depends on the local horizontal rate of strain—a horizontal length scale entering as the governing parameter" (Abstract; §4, Eqs. 4.22–4.26). **Stated** (form), used in the model.
2. Lateral friction (Eq. 4.22): $F^{\mathrm H}_x=(k_H\Delta)^2m^3\big[\partial_x(|D|D_T/m^2)+\partial_y(|D|D_S/m^2)\big]$, $F^{\mathrm H}_y=(k_H\Delta)^2m^3\big[\partial_x(|D|D_S/m^2)-\partial_y(|D|D_T/m^2)\big]$, with $D_T=\partial_xu-\partial_yv$, $D_S=\partial_xv+\partial_yu$ (4.23), $|D|=\sqrt{D_T^2+D_S^2}$ (4.24) and $k_H\approx0.28$ (§4, p. 105; parameter list p. 164, "Lateral $k_H=0.28$"). **Stated**
3. Lateral heat diffusion (Eq. 4.26): $H=(k_H\Delta)^2m^2\big[\partial_x(\tfrac12|D|_\Sigma\,\partial_x\Phi_{\mathrm{th}})+\partial_y(\tfrac12|D|_\Sigma\,\partial_y\Phi_{\mathrm{th}})\big]$, "if we assume the lateral heat diffusion to be forced" (§4, p. 105). **Stated**
4. The nonlinear lateral diffusion "may be formulated on the basis of the Heisenberg similarity theory", shown separately in ref. [55] (in preparation); the forms are taken to apply within constant-pressure surfaces with density variations ignored (§4, p. 105). **Stated** (derivation not in this paper)
5. The lateral diffusion simulates "the physically real net cascade of energy from the larger than grid-size scale to the smaller scales which have been truncated by the discrete differencing"; with no net accumulation of energy in the subgrid scales, "the energy removed at grid scale must be taken as identical to the implied dissipation which must occur by molecular viscosity"; with the grid scale in an inertial subrange, "we may express the exchange coefficient in the form $(k_H\Delta)^2|D|$, where $k_H\sim0.1$–$1.0$" (§14, p. 150). **Stated** (argument, no derivation)
6. The same formulation "was used successfully for numerical integrations on the convective scale [22]" (Lilly 1962), with a grid more than 1000 times smaller, which "suggests an element of validity in the approach" (§14, p. 150). **Stated**
7. Without (or with too small) $k_H$, "a systematic accumulation of available potential and kinetic energy by the non-linear cascade would occur in the highest allowable spectral component", Phillips' "non-linear computational instability" (§14, pp. 149–150). **Stated**
8. An energy-conserving (Arakawa) scheme does not remove the need for the subgrid transfer: the energy "may still be trapped in the highest wave numbers admissible by the finite grid" (§14, p. 150). **Stated**
9. Boundary conditions: no flux of zonal angular momentum through, and no kinetic-energy effect of, the smooth walls give "the weakest possible condition" $D_S\equiv0$ on $y=0,Y$ (4.25), hence $\partial_yu=0$ there; for heat $\partial_y\Phi_{\mathrm{th}}=0$ (4.27) (§4, pp. 105–106). **Derived**
10. The change of domain-mean relative zonal angular momentum due to the lateral friction is proportional to $[|D|D_S/m^2]_{y=0}^{y=Y}$, and its kinetic-energy dissipation to the domain mean of $|D|^3$ minus $[u|D|D_S/m^2]_{y=0}^{y=Y}$, internal and boundary lateral stresses respectively (§4, p. 105). **Derived**
11. The nonlinear diffusion terms are differenced forward (lagged) in time (Eq. 2.13) and the linear vertical diffusion implicitly (2.15); central differencing of $\partial_t\xi=\nu\xi$ (2.12) "is computationally unstable for $\nu<0$ for all $\Delta t$" (§2, p. 102; §4, p. 106). **Stated**
12. In the energy transformations the lateral-diffusion terms carry the factor $(k_H\Delta)^2/2$ for momentum and $(k_H\Delta)^2/(4\gamma^2_{\mathrm{st}})$ for heat (Eqs. 8.64, 8.102, §8b). **Derived**
13. From "white noise" temperature disturbances (variance about 2.5 °C) wave numbers 5 and 6 grow; after about 10 days the flow cycles with a period of 11–12 days, lengthening to 17 days with smaller amplitude after day 40 (§7; Abstract; §8f). **Shown**
14. Means over days 17–39: generation of zonal-mean available potential energy 29.8 and of eddy available potential energy −0.70 ($10^{-3}$ J g⁻¹ day⁻¹), against 42 and −29 of Wiin-Nielsen & Brown for January 1959 (§8f, p. 130). **Shown**
15. "In our model the lateral heat diffusion plays the role of dissipating available potential energy that is done in the atmosphere by diabatic processes"; a printed ratio of −0.44 against the observed −0.69 (§8f, p. 130). **Shown**
16. Total mean dissipation (36.3) exceeds net generation (29.1); the surface-stress dissipation (6.8) is, as a fraction of the total, a third of Brunt's estimated fraction 0.6; kinetic-energy dissipations 10.8 (zonal mean) and 13.0 (eddy) against Saltzman's 2.0 and 29.1; "The dissipation formulation of our model is naturally suspect" (§8f, p. 130). **Shown**
17. Dissipation partition as printed: "32 percent is dissipated in $\mathcal P$, 21 percent in $\hat K$, and 47 percent in $\bar K$" (available potential, vertical-shear kinetic and vertical-mean kinetic energy), against Wiin-Nielsen's 71/21/8 (§8f, p. 130). **Shown**
18. Logarithmic decrements over days 17–39: available potential energy $(100\ \text{days})^{-1}$, shear and mean kinetic energy $(15.8)^{-1}$ and $(14.8)^{-1}$, total energy $(42\ \text{days})^{-1}$ (§8f, Eq. 8.127). **Shown**
19. The scheme conserves the domain integral of zonal angular momentum (up to surface stresses) and thermal equilibrium but is not energy-conserving; the energy gain from truncation error is largest in the perturbation partitions (14.0 % and 4.9 % per day for two kinetic-energy partitions, 0.18 % per day for the total) (§8g, Table 8.5). **Shown**
20. The small-scale lateral eddy heat-flux divergence is of order 0.1 °C day⁻¹ except near the northern wall; "the small-scale eddies seem to contribute too heavily to the northward transfer" (§9, pp. 132–133). **Shown**
21. "If the small-scale diffusion mechanism were adjusted to give a smaller flux, the large-scale eddies would have to increase in intensity … just a small reduction in the small-scale eddy transfer could give rise to a much larger increase in the large-scale eddy transfer" (§9, pp. 133, 137). **Stated**
22. Small-scale lateral diffusion raises the angular momentum at high and low latitudes at the expense of the jet, much less than the large-scale flux divergence (§10, p. 138). **Shown**
23. Total zonal angular momentum rises for 20 days, then stays within ±2 % of its mean, controlled by the surface-wind distribution (§10; Abstract). **Shown**
24. Mean zonal-wind maximum 40 m s⁻¹, against Mintz's 27, Buch's 19 and Phillips' model 50 m s⁻¹; a double jet "may have been wiped out by too great a small-scale lateral diffusion coefficient" (§11, p. 143). **Shown** / **Stated**
25. The zonal flow is super-geostrophic poleward of the angular-momentum maximum and sub-geostrophic equatorward (Abstract; §12); the printed magnitudes are listed under Printed slips. **Shown**
26. "Our model requires a significant transfer by sub-grid scale motions. No comparison with the corresponding transfer in the real atmosphere is available … subject to some adjustment through the coefficient $k_H$" (§14, p. 149). **Stated**
27. Forecast code about 5000 instructions, 0.4 model days per hour on the IBM 704 and 3 days per hour on the 7090; 95 % of computer time in the forecast code (§13). **Stated**
28. Corrections to the author's earlier paper [53] (Smagorinsky 1958): its Eq. (75) left sides should have been multiplied by $m$, $G_x$ (not $G_y$) is needed on the walls, and its boundary reconstruction of the geopotential (Section 4c) is corrected (footnote p. 101; §5, p. 106). **Stated**

For the horizontal velocity $(u,v)$ with Cartesian derivatives,
$2S_{ij}S_{ij}=D_T^2+D_S^2+(\partial_xu+\partial_yv)^2$ ($i,j$ over $x,y$),
so $|D|$ equals the registry's $|S|$ of the horizontal motion only where the
horizontal divergence vanishes, and the exchange coefficient
$(k_H\Delta)^2|D|$ has the form $(C_s\Delta)^2|S|$ of the
[Smagorinsky model](/methods/smagorinsky-model.md) under that condition
*(compiler check, not in the sources)*.

# Printed slips

- **Super-geostrophic departure, Abstract against §12:** the Abstract says the zonal profile is "no more than 5 percent super-geostrophic poleward of the angular momentum maximum" (and 2 % sub-geostrophic equatorward); §12 says super-geostrophic departures "are at a maximum (7 to 8 percent) before and during low index", 1–2 % before and during high index.
- **Ratio of the two nonconservative transformations, §8 against §14:** §8e gives the theoretical value $\gamma^2/(\gamma_s^2\,2^{1/2})$, "0.57 as large", and §8f states that the ratio from Fig. 8.7 "=0.57 in (8.116)"; §14 (p. 149) gives "their ratio being approximately 0.7". With the printed $\gamma^2=0.8\gamma_s^2$, $0.8/\sqrt2=0.566$ *(compiler check, not in the sources)*.
- **Names of $D_T$, $D_S$:** "tension and shearing strains" (§4) against "tension stress", "shearing stress" (Appendix C).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $(k_H\Delta)^2\lvert D\rvert$ | $\nu_t=(C_s\Delta)^2\lvert S\rvert$ form | the source's lateral exchange coefficient (eddy viscosity) |
| $k_H$ | $k_H$ (page-local) | plays the role of $C_s$; 0.28 used, 0.1–1.0 stated |
| $D_T=u_x-v_y$, $D_S=v_x+u_y$, $\lvert D\rvert$ | $D_T$, $D_S$, $\lvert D\rvert$ (page-local) | horizontal, Mercator map derivatives; **not** $\lvert S\rvert$ (no divergence, no vertical shear) |
| $\Delta$ | $\Delta$ | grid increment, 555 km (5° longitude) |
| ${}_H\mathbf F$ | $F^{\mathrm H}_x$, $F^{\mathrm H}_y$ (page-local) | lateral friction force; not the registry forcing $f_i$ |
| $\bar\xi=\xi_1+\xi_3$, $\hat\xi=\xi_1-\xi_3$ | (two-level sum and difference) | **collision**: neither is the LES filter nor the test filter |
| $\hat\Phi$ | $\Phi_{\mathrm{th}}$ (page-local) | thickness departure |
| $\lvert\bar D\rvert$ | $\lvert D\rvert_\Sigma$ (page-local) | deformation magnitude with the two-level sum notation |
| $\tilde\xi$ | (time mean) | **collision** with the Favre tilde |
| $[\xi]$, $\{\xi\}$ | (zonal and meridional means) | averages, not filters |
| $\gamma_s^2$, $\gamma^2$ | $\gamma^2_{\mathrm{st}}$ (page-local) | static stability; **collision** with the ratio of specific heats $\gamma$ |
| $K$ | (kinetic energy; also eddy viscosity of vertical stresses) | overloaded in the source; not $k$ |
| $k_0=0.4$ | $\kappa$ | von Kármán constant of the surface layer |
| $m=\sec\theta$ | $m$ (page-local) | Mercator map factor |
| $x$, $y$ | $x$ eastward, $y$ northward | $y$ is normal to the lateral walls |

# Reference list

64 printed references, numbered [1]–[64], alphabetical by first author,
cited by number, no DOIs. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Ref. [55]
(Smagorinsky, "The formulation of eddy transport processes for the
quasi-static inertial subrange of atmospheric motions", in preparation, no
year printed), the promised derivation of the subgrid formulation, would take this source's own key and is keyed `smagorinsky-1963-b`. Fultz et al. (1959),
Mintz (1955) and Wiin-Nielsen (1962) each appear twice and take suffixes in
printed order; refs. [16] and [45] print "et al.". No item is unparseable.

# Pages created or updated

Chunk 17 (2026-10-29). This source is cited on:

- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Turbulent Prandtl number and turbulent heat-flux models](/definitions/turbulent-prandtl-number.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)

---
type: Source
title: "Slaughter et al. (2023) — Large Eddy Simulation of an Inverted Multi-element Wing in Ground Effect"
description: "Wall-resolved implicit LES with Nektar++, stabilized by gradient-jump penalisation and spectral vanishing viscosity, of a spanwise-periodic slice of the Imperial Front Wing in ground effect, characterizing its laminar separation bubbles, wake-induced transition, lift spectra and wake, as a first open motorsport benchmark."
resource: "doi:10.1007/s10494-023-00404-7"
source_kind: paper
authors: [Slaughter J., Moxey D., Sherwin S.]
year: 2023
venue: "Flow Turbul. Combust. 110:917-944"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Flow_Turbulence_and_Combustion_Slaughter_Large_Eddy_Simulation_of_an_Inverted_Multi-element_Wing_in_G.pdf"
tags: [implicit-les, transition, high-order, benchmark, spectral-vanishing-viscosity]
timestamp: 2026-10-28T07:11:00Z
---

# Summary

Slaughter et al. (2023) run a wall-resolved
[implicit LES](/definitions/implicit-les.md) of a spanwise-extruded slice
of the [Imperial Front Wing](/benchmarks/imperial-front-wing.md), a
three-element inverted wing (mainplane, two flaps) derived from a McLaren
MP4-17D specification, in ground effect at ride height $0.36c$ and
$Re=2.2\times10^5$ on the mainplane chord $c=0.25$ m. The motivation is the
lack of open motorsport benchmarks; the case is the first step of a
hierarchical benchmark set meant to calibrate lower-fidelity models: RANS,
reduced-order and transition models (the paper names no specific transition
model; one family is the
[local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)).

The solver is [Nektar++](/software/nektar-plus-plus.md): incompressible
Navier–Stokes, two-dimensional spectral/hp elements in the $x$–$y$ plane
with 64 Fourier modes over a span of $0.16c$, velocity-correction
splitting, second-order implicit–explicit time stepping, polynomial orders
6 (velocity) and 5 (pressure). There is no subgrid model
([large-eddy simulation](/definitions/large-eddy-simulation.md) in its
implicit form): the in-plane discretization is stabilized by
gradient-jump penalisation, a form of
[jump-penalty stabilization](/methods/jump-penalty-stabilization.md)
(Moura et al. 2022), the Fourier direction by
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
with an exponential kernel, so all dissipation beyond the viscous one is
[numerical dissipation](/properties/numerical-dissipation.md). The paper
relays that SVV can be overly diffusive at low polynomial order and states
that gradient-jump penalisation had not been applied to complex geometries
before. Wall resolution is judged at the first quadrature point against
the limits of Georgiadis et al. (2010)
([grid-point requirements](/results/les-grid-point-requirements.md)).

The mean lift and drag coefficients are $C_L=-8.33$ and $C_D=0.17$.
[Laminar separation bubbles](/definitions/laminar-separation-bubble.md) sit
on the suction sides of the mainplane and first flap, on the floor and on
the pressure side of the second flap; the second flap's suction side has
none, which the authors attribute to wake-induced bypass ("wake")
transition. Lift spectra show narrowband peaks at $St=40$, 60, 140, 200; the
surface-pressure spectrum inside the mainplane bubble coincides with them,
from which the authors infer that the bubble causes these frequencies. The
wake meanders and breaks down through a Kelvin–Helmholtz-type instability.
All evidence comes from one simulation, without a grid-convergence study
or an experimental comparison.

# Version read

Research Square preprint v1 (doi:10.21203/rs.3.rs-2068909/v1, posted 20
September 2022, CC BY 4.0, Springer Nature LaTeX template), not the version
of record: 27 PDF pages (a cover sheet and 26 manuscript pages), all read.
Title (up to capitalization: "Multi-Element") and authors match the
published article, which spans 28 journal pages. Claims, numbers and
references here are those of the preprint. Section, equation and figure numbers and
manuscript pages on this page are those of the preprint.

# Key claims

Page-local symbols: $c$ the mainplane chord; $\boldsymbol u_m(x,y)$
the $m$-th spanwise Fourier mode of the velocity and $E_m$ its modal
kinetic energy (the source's $\hat{\mathbf u}_k$, $E_k$); $t^*=tU_\infty/L_c$.

1. The simulations are implicit LES: no subgrid model; the stabilizations "fill a similar role" but their dissipation "is a pure characteristic of the numerical scheme", the iLES assumption being that the subgrid stresses are of the order of the truncation error (§3). **Stated**
2. SVV-type approaches at lower polynomial orders "can be overly diffusive, resulting in a significant loss in resolution" (citing Moura et al. 2022), which "disproportionately impacts industrial type approaches limited to lower polynomial orders" (§3.1). **Stated**
3. Gradient-jump penalisation, which adds a penalty on the gradient discontinuity at element boundaries, "has out-performed the SVV approach on canonical cases but has yet to be applied to more complex geometries"; it is applied here to the wing slice (§3.1). **Stated** (application **Shown**); no operator or penalty parameter is printed
4. Polynomial orders 3–8 are typical for industrial problems in Nektar++; velocity one order above pressure (Taylor–Hood type); here $N=6$ and 5 (§3.1, §3.3). **Stated**
5. The exponential SVV kernel in the Fourier direction "activates purely on expansion modes greater than the product of the cut-off ratio and the polynomial order" (§3.1). **Stated** (cut-off ratio not printed)
6. A two-dimensional linear mesh (triangles, quadrilaterals, one inflation layer, three wake-refinement regions) is projected to curvilinear high order and the layer split isoparametrically into 10 layers at growth rate 1.4 on the wing and 5 on the floor (§3.2). **Stated**
7. Lift varies "only by approximately 5% over a large range of spanwise lengths", and the smaller span $0.16c$ is chosen (§3.3). **Shown** (data not plotted)
8. Wall resolution is judged at the first quadrature point inside the element; the planar spacings are below the Georgiadis et al. (2010) limits except two small mainplane sections where $y^+$ is "slightly above one"; spacings are estimates from the mesher's specified spacings (§3.6, Fig. 4). **Shown**
9. The spanwise modal energy $E_m$ "quickly decays to $10^{-7}$" before the SVV filter width, "suggesting the irrelevance of additional high-frequency modes" (§3.6, Fig. 5). **Shown**
10. Mean $C_L=-8.33$, $C_D=0.17$ (Abstract, §4.2, §6). **Shown**
11. Peak suction $C_p\sim-11$ close to the mainplane leading edge; pressure decreases monotonically along the suction sides except on the mainplane for $0.50\le x/c\le0.65$; the second flap is "seemingly misaligned" with the local flow, its stagnation point lying away from the leading edge (§4.1, Fig. 7). **Shown**
12. Laminar separation bubbles lie on the mainplane and first-flap suction sides, "thinned" by the strong adverse pressure gradient, a larger and thicker one on the floor, and one on the second-flap pressure side; two bifurcation lines bound each in surface line-integral convolution (§4.1, Figs. 6, 9, 10). **Shown**
13. The second flap's suction side shows no bubble; wake and shear-layer interaction from the upstream elements causes a bypass-like "wake transition" (§4.1, Fig. 11). **Shown** (qualitative)
14. Mainplane suction-side boundary layer: inflection point near $x/c=0.4$, reversed flow until about $x/c=0.5$, reversed region extending to $y/c\sim0.001$ (§4.1, Fig. 12). **Shown**
15. Lift spectra (Welch's method): a dominant narrowband mode at $St=60$ on all three elements; $St=140$ and 200 on the mainplane; $St=40$ on all elements, strongest on the first flap; $St=30$ on the second flap only (§4.2, Fig. 13). **Shown**
16. Surface-pressure variance is largest within and around the bubbles; the maximum of $\mathrm{RMS}(C_p)-\overline{C_p}$ lies at $x/c\sim0.55$ (mainplane) and $\sim0.61$ (first flap) (§4.3, Fig. 14). **Shown**
17. The spectrum at the mainplane maximum-RMS point "coincides perfectly" with the lift peaks at $St=60$, 140, 200; with almost no upstream pressure fluctuation, "the LSB is causal of these pressure fluctuations - on the mainplane"; for the first flap causality cannot be asserted, but the frequencies are "locked" for both bubbles (§4.3, Fig. 15). **Shown** (causality argued from coincident spectral peaks)
18. The cross-spectral phase of mainplane and first-flap lift is in phase at $St=40$ and out of phase at $St=60$ (§4.3, Fig. 16; Abstract; §6). **Shown**
19. The mainplane bubble shows Kelvin–Helmholtz roll-up, bursting and ejection of low-momentum fluid; quasi-periodic streaky structures leave the transition location (§4.3, Figs. 17, 18). **Shown**
20. On the second-flap pressure side, $St=60$, 140, 200 appear at the leading edge, transition peak ($x/c\sim0.35$) and trailing edge, "probably convected or caused by the changes in blockage/downwash on the upstream elements"; energy at $St=10$–20 at the transition location is attributed to the pressure-side bubble (§4.3, Figs. 19, 20). **Shown**
21. Q-criterion iso-surfaces show two-dimensional Tollmien–Schlichting waves from the start of the mainplane bubble breaking down quickly to turbulence; the breakdown route is unclear (§4.3, Fig. 22b). **Shown** (qualitative)
22. The wake meanders about $1c$ downstream of the second flap and breaks up a few chords downstream, with Kelvin–Helmholtz-type shedding about $1.5c$ downstream of the trailing edge; the floor shear layer shows a 15% velocity deficit over less than 1 cm at $x/c=2$ (§4.3, Figs. 21, 23). **Shown**
23. Turbulent kinetic energy $k$: three near-field wake peaks at $y/c=0.75$, 0.8, 1.0 ($x/c=2$); maximum 0.012 at $x/c=2.5$, 0.008 at $x/c=4$; at $x/c=6$ the maximum is 50% larger than $2c$ upstream, attributed to production by the Kelvin–Helmholtz mode (Fig. 24). **Shown** (the production reading is **Stated**; no budget computed)
24. The fields, statistics, mesh and session files "will" be released for calibration of lower-fidelity and reduced-order models (§5). **Stated**

# Printed slips

- **Pressure coefficient** (§4.1, p. 9): printed "$C_p=\frac12\rho V^2$", the dynamic pressure, not a pressure coefficient.
- **Turbulent kinetic energy** (§4.3, p. 21): printed "$TKE=1/2(\overline{u'}+\overline{v'}+\overline{w'})$", fluctuations unsquared; the adjacent text says "half the sum of the variances".
- **Range** (§4.1, p. 11): "Between $0.45\le\frac{x}{c}\le-0.50$ on the mainplane".
- **Elements** (§4.1, p. 11): "The LSBs on the suction side are evident in the pressure distribution on the suction side of both the first and second flaps", while the paper places them on the mainplane and first flap and finds none on the second-flap suction side.
- **Q-criterion description** (§4.3, p. 19): "the LSB on the upper surface of the second flap with no visible transition on the pressure surfaces of the mainplane and first flap"; §4.1 places that bubble on the second-flap pressure side.
- **Conclusions against §4.3:** §6 says "a lower frequency mode at $St=30$ exists only on the second flap which likely corresponds to the LSB on the pressure surface", while §4.3 attributes the "$St=10-20$" energy at the transition location to that bubble; §6 says $St=40$, 60, 140, 200 were found "on all flaps", while §4.2 says $St=140$, 200 "are not as visible on the other elements".
- **Sample counts** *(compiler check, not in the sources)*: averaging over $8t^*$ at the printed $dt^*=1.6\times10^{-6}$, sampled every 10 steps, gives $8/(10\times1.6\times10^{-6})=5.0\times10^5$ samples, while the cross-spectral phase uses "a vector of roughly 35,000 samples long (again sampled every 10 timesteps)", i.e. $0.56t^*$; the transient of about $40t^*$ would be $2.5\times10^7$ steps. The paper does not reconcile these values ($L_c$ in $t^*$ is not specified).
- **Fig. 19** panel title "Mainplane Average $C_p$" in a figure captioned "Flap 2 Pressure Fluctuation".
- **Frequency axes:** Figs. 13, 16 use $St$, Figs. 15, 20 "Frequency [1/CTU]", compared in the text as the same $St$ values; $St$ is never defined.
- **Minor:** "laminar separation bubbles (LSC)" (p. 11); "Tollmein-Schlichting" (p. 19); "28 behind" without unit (p. 7); wall units printed as "$\Delta(x^+,y^+,z^+)=\frac{u_\tau(x,y,z)}{\nu}$" without the spacing factor (p. 7).
- **References:** Karniadakis & Orszag (1991) pages "414443"; Hambli et al. (2022) DOI truncated to "10.3390/fluids"; Moxey et al. (2020) DOI printed with a Mendeley Data prefix ("10.17632/9drxd9d8nx.1"); Serdar et al. (2012) author names garbled.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u,v,w$; $x,y,z$ | $u,v,w$; $x$ streamwise, $y$ vertical (normal to the floor), $z$ spanwise | agrees |
| $c$, $C$ | $c$ (page-local mainplane chord) | both printed in figure axes |
| $h/c$ | (ride height over chord, 0.36) | **collision:** not the element size $h$ |
| $Re$ | $Re_c$ | mainplane chord and far-field velocity |
| polynomial order 6, 5 | $N=6$ (velocity), 5 (pressure) | |
| $\hat{\mathbf u}_k$, $E_k(t)$ | $\boldsymbol u_m$, $E_m$ (page-local) | Fourier coefficient written with a subscript, never a hat (registry §2); $E_k$ is not the spectrum $E(k)$ |
| $L_z$ | (span, $0.16c$) | |
| $t^*=tU/L_c$, $dt^*$ | $t^*$, (time step) | $L_c$ not specified |
| $St$ | $St$ | definition not printed |
| $C_L$, $C_D$, $C_p$, $C_f=2\tau_w/(\rho U^2)$ | $C_L$, $C_D$, $C_p$, $C_f$ | $C_L<0$ is downforce |
| $x^+$, $y^+$, $z^+$ | $\Delta x^+$, $\Delta y^+$, $\Delta z^+$ | first quadrature point for the wall-normal spacing |
| $TKE$, $k$; $\overline{(\cdot)}$, $u'$ | $k$; $\langle\cdot\rangle$, $u'$ | **collision:** overbar = time average, not the filter |
| $Q$ | (Q-criterion, iso-value 100) | |
| LSB | (laminar separation bubble) | |

# Reference list

20 printed references, author–year style (Springer Nature template). The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Buscariolo et al. (2019), Lombard (2017), Pegrum
(2006) and Cabral & Leedom (1993) print no venue or document type;
Serdar et al. (2012) is transcribed with its garbled author names, and the
truncated DOI of Hambli et al. (2022) is kept as printed. No cited key
equals an ingested Source.

# Pages created or updated

Chunk 4 (2026-10-26). This source is cited on:

- [Imperial Front Wing](/benchmarks/imperial-front-wing.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Laminar separation bubble](/definitions/laminar-separation-bubble.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Jump-penalty stabilization of high-order methods](/methods/jump-penalty-stabilization.md)
- [Local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)
- [Spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [Nektar++](/software/nektar-plus-plus.md)

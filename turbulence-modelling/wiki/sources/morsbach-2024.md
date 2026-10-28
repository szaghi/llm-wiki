---
type: Source
title: "Morsbach et al. (2024) — Large Eddy Simulation of a Low-Pressure Turbine Cascade with Turbulent End Wall Boundary Layers"
description: "Wall-resolved sixth-order DGSEM implicit LES of the T161 low-pressure turbine cascade with synthetic turbulent end-wall boundary layers and free-stream turbulence, matching experiment, and used as reference for SST and SSG/LRR-ω RANS with γ-Re_θ transition, which miss the midspan separation bubble and overpredict secondary losses."
resource: "doi:10.1007/s10494-023-00502-6"
source_kind: paper
authors: [Morsbach C., Bergmann M., Tosun A., Klose B.F., Kügeler E., Franke M.]
year: 2024
venue: "Flow Turbul. Combust. 112:165–190"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Flow_Turbulence_and_Combustion_Morsbach_Large_Eddy_Simulation_of_a_Low-Pressure_Turbine_Cascade_with.pdf"
tags: [implicit-les, dg, rans, transition, turbomachinery, anisotropy]
timestamp: 2026-10-28T07:09:00Z
---

# Summary

Morsbach et al. (2024) present a wall-resolved
[implicit LES](/definitions/implicit-les.md) of the MTU T161 low-pressure
turbine linear cascade, a high-lift blade between diverging end walls, at an
isentropic exit Reynolds number of $9\times10^4$ (chord) and exit Mach number
0.6. They compare it with two RANS closures run on a consistent setup. The
LES uses the sixth-order
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) solver of
DLR's TRACE code ($N=5$, Legendre–Gauss–Lobatto collocation, Roe interface
flux, BR1 viscous terms without penalty, SSP-RK3). It is stabilized by the
Kennedy–Gruber [kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
split form and has no explicit subgrid model. The unresolved scales are left to
the [numerical dissipation](/properties/numerical-dissipation.md) of the
scheme. The RANS runs use TRACE's second-order finite-volume solver with the
[$k$-$\omega$ SST model](/methods/k-omega-sst-model.md) (2003, Kato–Launder
production) and with the SSG/LRR-$\omega$ differential Reynolds-stress model.
Both are coupled to the $\gamma$-$Re_\theta$
[transition model](/methods/local-correlation-based-transition-model.md).

A central part is the [inflow](/methods/inflow-turbulence-generation.md). A
Fourier-mode synthetic turbulence generator (Shur et al. 2014) is fed with
spanwise profiles of total pressure and temperature, Reynolds stresses and
length scale. The profiles are scaled from the $Re_\theta=670$
[boundary-layer](/benchmarks/turbulent-boundary-layer.md) DNS of Schlatter &
Örlü and merged with free-stream turbulence of the measured anisotropy. A
precursor finite-length [channel](/benchmarks/turbulent-channel-flow.md) LES
calibrates the inlet distance, and the RANS inflows are tuned to reproduce the
LES decay. The fine LES (189.4M degrees of freedom, 100 convective times)
matches the measured blade loading, including the plateau of the
[laminar separation bubble](/definitions/laminar-separation-bubble.md). It
also matches the midspan wake loss and the secondary-flow loss cores. Both
RANS models miss the bubble and underestimate the midspan loss by 35% (SST)
and 29% (SSG/LRR-$\omega$). Reducing the inflow length scale, a common
practice, brings the SST loss within 2.7% by error cancellation, with an open
separation. In the end-wall region both RANS models overpredict the peak loss
(+34%, +48%). The Reynolds-stress model reproduces the free-stream anisotropy,
which a [Boussinesq](/definitions/boussinesq-hypothesis.md) model cannot, but
it underpredicts $k$ in the passage vortex. The introduction recalls the
[grid-point scaling](/results/les-grid-point-requirements.md) of
[DNS](/definitions/direct-numerical-simulation.md) and
[LES](/definitions/large-eddy-simulation.md).

# Version read

Version of record (Springer, open access CC BY 4.0; received 28 April 2023,
accepted 6 October 2023), 26 pages, all read; Eqs. 1–15 and Table 2 were
checked visually. The extracted text prints no running page numbers, so
locations are given by section, equation, figure and table. Page 1 matches the
metadata. The archive filename carries the online year 2023; the issue year is
2024.

# Key claims

1. Cost scaling cited from Choi & Moin (2012): DNS cost grows roughly as $Re^{3.5}$ and wall-resolved LES as $Re^{2.5}$ (§1). **Stated** (cited)
2. The LES uses a sixth-order DGSEM on collocated Legendre–Gauss–Lobatto nodes, with a Roe flux, the Kennedy–Gruber kinetic-energy-preserving split-form volume flux, BR1 viscous terms with a central flux and no penalty, SSP-RK3 time integration and no explicit SGS model (§2). **Stated**
3. The synthetic turbulence is superimposed on a mean state from a Riemann boundary condition and imposed weakly through a central flux on the inflow faces; the outflow uses one-dimensional non-reflecting conditions with a global static pressure; RANS uses the same inflow and outflow formulation (§2). **Stated**
4. Fine mesh: 876 960 hexahedra, geometry degree 4, $N=5$, 189.4M degrees of freedom; blade midspan average cell sizes in wall units divided by $N$ of $(23.1, 0.742, 15.0)$ (streamwise, wall-normal, spanwise), end-wall averages $(23.2, 0.809, 18.8)$ and maxima $(65.2, 1.71, 60.3)$; the ratio of the average solution-point distance to the estimated Kolmogorov length stays below 6 in the free stream (§3.1, Fig. 2). **Shown**
5. Coarse mesh: 312 424 elements, 67.9M degrees of freedom, much coarser spanwise; channel precursor: 83 790 elements, $(32.6, 2.0, 33.1)$ (§3.1, Table 2). **Shown** (see Printed slips)
6. Operating point: inflow angle 41°, upstream total pressure 11 636 Pa and total temperature 303.25 K, exit static pressure 9122.7 Pa, $Re=9\times10^4$, $M=0.6$ (isentropic exit values) (§3.2, Table 1, Eqs. 1–4). **Stated**
7. Specifying the inflow through total pressure makes end-wall boundary-layer profiles harder to impose than specifying velocity, since the near-wall velocity follows from the total and the simulated static pressure; the chosen centre-line Mach number (0.362) must keep the total pressure above the static pressure to avoid backflow and may need iteration (§3.2–3.3). **Stated**
8. Matching the measured free-stream decay would need a length scale of the order of the pitch; the length scale is instead reduced and the Reynolds stresses rescaled to match $Tu$ at the leading-edge plane, at the cost of a steeper decay (§3.3, Fig. 4). **Shown**
9. Boundary-layer shape factors at $x/c_{ax}=-0.99$: 1.447 (fine LES), 1.405 (channel LES), 1.440 (SST), 1.396 (SSG/LRR-$\omega$) (§3.3, Fig. 3). **Shown**
10. Both RANS models reproduce the upstream LES decay of $Tu$; in the passage SST underestimates $Tu$ shortly behind the leading edge while SSG/LRR-$\omega$ follows it nearly to the trailing edge, which required the correct inflow anisotropy (§3.3, Fig. 4). **Shown** (sensitivity to anisotropy **Stated**, not shown)
11. The injected turbulence is two-component at the inlet and returns toward isotropy in the channel; with the blade, flow acceleration stretches the vortices and drives the anisotropy toward the two-component axisymmetric corner from leading to trailing edge, then back toward isotropy; SSG/LRR-$\omega$ reproduces this qualitatively (§3.3, Fig. 4). **Shown**
12. The integral length scale, from frozen turbulence (Eqs. 13–14), drops quickly to about half the generator's value, as in the authors' earlier tests on decaying isotropic turbulence; spectra at $x/c_{ax}=-0.99$ show large-scale anisotropy and an inertial range $\propto f^{-5/3}$ (§3.3, Fig. 5). **Shown**
13. At the peak wake-loss point the mean velocity reaches 1% relative sampling error after 46 convective times and 0.58% after 100, while $R_{11}$ still carries 3.0% after 100 (68% confidence intervals) (§4.1, Fig. 6). **Shown**
14. Fine and coarse LES give the same blade loading; skin friction differs downstream of the transition peak of the separation bubble, "indicating that the resolution on the coarse mesh is not entirely sufficient" (§4.1, Fig. 7). **Shown**
15. LES against experiment: very good on the pressure side; a suction-side pressure offset for $0.1<x/c_{ax}<0.6$, similar to earlier studies; the separation-bubble plateau between 0.7 and 0.9 and the base-pressure recovery captured very well (§4.1, Fig. 7). **Shown**
16. Both RANS models with properly configured inflow turbulence miss the pressure plateau: separation slightly delayed, premature reattachment, a very thin bubble (§4.1, Figs. 7–8). **Shown**
17. Reducing the RANS inflow length scale ($L_{T,0}/16.7$, SST), "common practice", strongly reduces $Tu$; the flow separates early and does not reattach before the trailing edge, the transition model keeping a larger laminar portion through $\gamma\ll1$ (§4.1, Figs. 4, 7, 8). **Shown**
18. Midspan mixed-out wake losses are underestimated by 35% (SST) and 29% (SSG/LRR-$\omega$) with the appropriate turbulence decay; the reduced-length-scale SST is off by 2.7% through "a lucky cancellation of errors"; LES and experiment agree within the confidence intervals (§4.1, Fig. 9). **Shown**
19. The fine LES reproduces the measured secondary-flow loss cores at $x/c_{ax}=1.4$, with the passage-vortex core slightly closer to the end wall than measured; coarse and fine LES agree (§4.2, Fig. 10). **Shown**
20. The reduced free-stream length scale barely changes the secondary losses (§4.2, Fig. 10). **Shown**
21. RANS overpredicts the maximum loss in the passage-vortex and trailing-shed-vortex region by 34% (SST) and 48% (SSG/LRR-$\omega$); unlike in Marconcini et al. (2019), the losses are too large "even in a pitch-averaged sense" (§4.2, Fig. 10). **Shown**
22. In both RANS models the corner vortex persists further downstream and the vortex system is stronger, further from the end wall and offset toward the suction side; the Reynolds-stress model strongly exaggerates the compactness and strength of the vortices, contrary to the expectation that such models are less diffusive for vortices (§4.2, Fig. 11). **Shown**
23. In the LES, turbulence over the separation bubble dominates the wake near midspan; two vortex cores above the passage vortex co-rotate with it (Cui et al. 2017 report opposite rotation, Gross et al. 2018 co-rotation); the incoming turbulent end-wall boundary layer is lifted off by the passage vortex, leaving a calmed region (§4.2, Fig. 12). **Shown**
24. The RANS models reproduce the overall secondary-flow topology; SSG/LRR-$\omega$ shows a second saddle point upstream of the first; both place the horseshoe vortex at nearly the same position with a straight pressure-side leg, whereas the LES has it closer to the leading edge with a curved leg (§4.2, Fig. 13). **Shown**
25. SST qualitatively reproduces the elevated $k$ in the passage-vortex core, while SSG/LRR-$\omega$ produces too little $k$ there, a possible explanation of its slower vortex decay (§4.2, Fig. 14). **Shown**
26. A linear eddy-viscosity model cannot reproduce the free-stream anisotropy, since through the Boussinesq approximation the turbulence anisotropy equals the strain-rate anisotropy (§4.2). **Stated**
27. The LES shows near-one-component turbulence in the transitional separated shear layer and near-isotropic turbulence after transition; SSG/LRR-$\omega$, a high-Reynolds-number model with the LRR pressure–strain near walls and no near-wall pressure–strain or dissipation terms, misses this, and the authors question that choice here (§4.2, Fig. 15). **Shown** / **Stated**
28. Downstream of the passage vortex the LES fills the region with two-component free-stream turbulence by down-wash, where the Reynolds-stress model gives a large rod-like region (§4.2, Fig. 15). **Shown**
29. Neither RANS model predicts the separation-induced transition at midspan; tuned transition models or laminar-kinetic-energy models may be needed; the midspan errors weakly affect the secondary flow; the Reynolds-stress model represents anisotropy better but underpredicts turbulence in large vortices (§5). **Shown** (suggestions **Stated**)

The inflow profiles (Eqs. 5–11), with $y$ the wall distance of the end wall:
$$\begin{aligned}
M(y_i)&=u^+_{i,\mathrm{DNS}}\,u_\tau/a_1,\qquad y_i=y^+_{i,\mathrm{DNS}}\,\nu_1/u_\tau,\qquad u_\tau=a_1M_{1,c}/u^+_{\infty,\mathrm{DNS}},\\
R_{jk}(y_i)&=R^+_{jk}\big|_{i,\mathrm{DNS}}\,u_\tau^2,\qquad L_{T,\mathrm{BL}}(y_i)=\frac{(k^+_{i,\mathrm{DNS}})^{3/2}}{\varepsilon^+_{i,\mathrm{DNS}}}\frac{\nu_1}{u_\tau},\qquad L_T=\max(L_{T,\mathrm{BL}},L_{T,\mathrm{fs}}),
\end{aligned}$$
with constant static temperature and pressure across the layer, related to the total quantities by isentropic relations (Eq. 5), and the free-stream length scale taking over beyond $\delta_{99}$ (§3.3). **Stated**

# Printed slips

- **Coarse-mesh degrees of freedom.** Table 2 defines nDoF $=n_{xy}n_z(N+1)^3$; for the coarse mesh $3188\times98\times6^3=67\,483\,584$, whereas Table 2 and §3.1 print 67.9M; the channel (18.10M) and fine (189.42M) entries reproduce *(compiler check, not in the sources)*.
- **Citations against the list.** The text cites "Bergmann and Morsbach 2018", the list's 2018 entry is Bergmann, Gölden and Morsbach; the text cites "Morsbach and Mare 2012", the list prints "Morsbach, C., di Mare, F."; "Afshar et al. (2022)" is cited twice (§1, §4.1) while the list holds only Afshar et al. 2023; "Moura et al. 2017, 2017" is cited without a/b.
- **Fig. 12 caption.** "$QC_{ax}^2/\|u_2\|^2=100$ over the end wall (left)", while the text places the end-wall top view on the right ("in the top view (right)"); both sub-views are labelled "(left)".
- **§3.3.** "a fit of an exponential function proportional to $x^{4/5}$", a power law.
- **Reference list.** Kato & Launder (1993) pages printed "10–411046".
- **Symbol reuse.** $\gamma$ is the ratio of specific heats and the intermittency; $\omega$ is the total-pressure loss coefficient (Eq. 16) and the specific dissipation rate.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $z$, $z^+$ (inflow profiles, Eqs. 6–11) | $y$, $y^+$ | **collision:** wall-normal to the end wall is the source's $z$ (the cascade's spanwise direction) |
| $\Delta\xi^+$, $\Delta\eta^+$, $\Delta\zeta^+$ | $\Delta x^+$, $\Delta y^+$, $\Delta z^+$ divided by $N$ | **collision:** $\xi$ is not the reference coordinate |
| $N$, $q$ | $N$, (geometry polynomial degree) | sixth order $=N+1$ |
| overbar | $\langle\cdot\rangle$ (time average) | **collision:** not an LES filter |
| $\overline{u'_iu'_j}$ | $R_{ij}$ | positive, kinematic |
| $k$, $\epsilon$ | $k$, $\varepsilon$ | DNS values in wall units |
| $\gamma$ | $\gamma$ | **collision:** ratio of specific heats and intermittency on the same page |
| $\omega$ (Eq. 16) | (total-pressure loss coefficient, page-local) | **collision** with the specific dissipation rate $\omega$ |
| $\omega_{sw}$ | (streamwise vorticity $\boldsymbol u\cdot\boldsymbol\omega/\lVert\boldsymbol u\rVert$) | |
| $L_T$, $L_{T,0}$ | $L$ (integral length scale), its generator input | |
| $Tu$ | $Tu$ | |
| $\delta_{99}$, $\theta$, $H_{12}$, $Re_\theta$ | $\delta_{99}$, $\theta$, (shape factor), $Re_\theta$ | $Re_\theta$ with $\nu$ at the wall |
| $u_\tau$, $u^+$ | $u_\tau$, $u^+$ | |
| $Ma_{2,th}$, $Re_{2,th}$, $Ma_{1,c}$ | $M$, $Re$ (isentropic exit values, chord-based), (profile centre-line Mach number) | |
| $T_1$, $p_1$, $a_1$, $\nu_1$ | (static inflow temperature, pressure, sound speed, viscosity) | |
| $p_{t1,ref}$, $T_{t1,ref}$, $p_{2,ref}$ | (upstream total pressure and temperature, exit static pressure) | |
| $C$, $C_{ax}$, $l_{pitch}$, $\beta_s$, $\alpha_1$ | (chord), $c_{ax}$ (axial chord, registry §11), (pitch, stagger angle, inflow angle) | **collision:** $\alpha_1$ is not the DG/FV blending factor |
| $H$, $h$ | (upstream channel height, local channel height) | **collision:** $h$ is not an element size |
| $\overline{c_f}$ | $C_f$ normalized by $p_{t1,ref}-p_{2,ref}$ | not by the dynamic pressure |
| $t_c$ | (convective time: chord over exit velocity) | |
| $Q$ | Q-criterion normalized by $c_{ax}^2/\lVert\boldsymbol u_2\rVert^2$ | |
| LEVM, DRSM | linear eddy-viscosity model, differential Reynolds-stress model | |
| PV, TSV, HSV, LSB | passage vortex, trailing shed vortex, horseshoe vortex, laminar separation bubble | |
| 1C, 2C, 3C | one-, two-, three-component limiting states of the anisotropy (barycentric map) | expressed through $b_{ij}$ |

# Reference list

64 printed references, author–year style, alphabetical. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
The two Moura et al. 2017 works take suffixes in printed order. Kato & Launder
(1993), Müller-Schindewolffs et al. (2017) and Sandberg et al. (2015) print
irregular page fields, recorded as printed. Afshar et al. (2022), cited twice
in the text, is not in the list. No printed duplicates.

# Pages created or updated

Chunk 4 (2026-10-26), cited further in chunks 5, 6, 12. This source is cited on:

- [Turbine cascades (T106, T161, VKI LS89)](/benchmarks/turbine-cascade.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Barycentric anisotropy map](/definitions/barycentric-anisotropy-map.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Laminar separation bubble](/definitions/laminar-separation-bubble.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Model-form uncertainty in turbulence closures](/definitions/model-form-uncertainty.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Laminar kinetic energy transition models](/methods/laminar-kinetic-energy-transition-model.md)
- [Local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)
- [Differential Reynolds-stress models](/methods/reynolds-stress-model.md)
- [Geometric conservation law and free-stream preservation](/properties/geometric-conservation-law.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [TRACE](/software/trace.md)

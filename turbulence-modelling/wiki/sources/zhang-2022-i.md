---
type: Source
title: "Zhang et al. (2022e) — Large-eddy simulation of wind-turbine wakes over two-dimensional hills"
description: "Wall-modelled LES (LESGO, Smagorinsky with wall damping, log-law wall stress, immersed-boundary terrain, filtered actuator disk) of a wind-turbine wake over steep and gentle two-dimensional hills: wake trajectory, Gaussian self-similarity, power by turbine position and a disk-integrated mean-kinetic-energy budget."
resource: "doi:10.1063/5.0095348"
source_kind: paper
authors: [Zhang Z., Huang P., Bitsuamlak G., Cao S.]
year: 2022
venue: "Phys. Fluids 34:065123"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Physics_of_Fluids_Zhang_Large-eddy_simulation_of_wind-turbine_wakes_over_two-dimensi.pdf"
tags: [les, wmles, wall-model, immersed-boundary, wind-energy, separated-flow]
timestamp: 2026-10-29T07:41:00Z
---

# Summary

Zhang et al. (2022e) study the wake of a single
wind turbine placed upstream of, on and behind an isolated
spanwise-uniform $\cos^2$ hill in a neutral, pressure-gradient-driven
atmospheric boundary layer at wind-tunnel scale. The tool is
[wall-modelled LES](/methods/wall-modelled-les.md) with a modified
[LESGO](/software/lesgo.md) (pseudo-spectral in the two horizontal
directions, second-order central differences in the vertical, second-order
Adams–Bashforth, 3/2-rule dealiasing). The viscous term is dropped; the
subgrid stress is the [Smagorinsky model](/methods/smagorinsky-model.md)
with the Mason–Thomson wall damping; the wall stress is the rough-wall
[log law](/definitions/law-of-the-wall.md) applied as an
[equilibrium wall model](/methods/equilibrium-wall-model.md) with
test-filtered velocity; the terrain is an
[immersed boundary](/methods/immersed-boundary-method.md) (Chester et al.
2007); the rotor is the filtered
[actuator disk](/methods/actuator-line-model.md); the inflow comes from a
concurrent precursor ([inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
The [LES](/definitions/large-eddy-simulation.md) is validated on the bare
steep hill against the Cao & Tamura (2006) wind-tunnel data: mean
velocity agrees, streamwise turbulence intensity is underpredicted in the
recirculating lower hill wake, which the authors attribute to the
equilibrium log-law wall model.

The wind-energy results stay on this page. On the steep hill the
wake-centre trajectory of a turbine at or behind the crest deflects
downward, against the constant-elevation assumption of Shamsoddin &
Porté-Agel (2018). The velocity deficit is not Gaussian in the steep-hill
wake until $x/D\ge7.5$, yet the Shamsoddin–Porté-Agel pressure-gradient
model still predicts the maximum deficit. Power peaks at the crest
(1.8 times the flat-ground value on the gentle hill, 2.6 on the steep
hill) and collapses behind the steep hill. A resolved mean-kinetic-energy
budget integrated over a wake-following disk shows pressure transport and
mean convection dominating wake recovery over hills, turbulent transport
over flat ground.

# Version read

Version of record (AIP; received 9 April 2022, accepted 27 May 2022,
published online 10 June 2022), 22 PDF pages: an AIP cover page plus
article pages 065123-1 to 065123-21, all read; the equations of pp. 3, 4,
8, 10, 15, 16 and Appendix B were read visually. Page 1 matches the
metadata; no identity issue. Equation and figure numbers are those of
this version.

# Key claims

Page-local symbols: $D$ rotor diameter, $h_{\mathrm{hub}}$ hub height
($h_{\mathrm{hub}}=D=40$ mm), $x_t$ turbine streamwise position, $H$ hill
height, $L_{\mathrm h}$ hill half-length, $s_{\mathrm h}=H/L_{\mathrm h}$
hill slope, $y_{0,\mathrm r}$ roughness length, $\ell_s=C_s\Delta$ the Smagorinsky
length and $\ell_0=C_{\mathrm{MT}}\Delta$ its far-wall value ($C_{\mathrm{MT}}$ the Mason–Thomson far-wall coefficient, printed $C_0$), $C_{\mathrm{Th}}$ and
$C'_{\mathrm{Th}}$ the rotor thrust coefficient and its local-velocity
form, $a_{\mathrm i}$ the axial induction factor, $H_{\mathrm{dom}}$ the
domain height, $C_{\mathrm{def}}(x)$ the maximum normalized deficit,
$\sigma_{\mathrm w}$ the Gaussian wake width, $k_{\mathrm w}$ the wake
growth rate. $y$ is vertical (wall-normal), $z$ spanwise; $\langle\cdot\rangle$ is the time average.

1. The filtered incompressible continuity and momentum equations are solved for neutral conditions without the viscous term, driven by a constant pressure gradient $F_p=u_\tau^2/H_{\mathrm{dom}}$ (§II A, Eqs. 1–2). **Stated**
2. The deviatoric subgrid stress is $\tau^d_{ij}=-2\nu_t\bar S_{ij}$, $\nu_t=\ell_s^2|\bar S|$, with the Mason–Thomson damping $1/\ell_s^n=1/\ell_0^n+1/[\kappa(y+y_{0,\mathrm r})]^n$, $C_{\mathrm{MT}}=0.16$, $n=2$ (§II A, Eqs. 4–6; §II B). **Stated**
3. The wall stress is the log law with test-filtered ($\hat\Delta=2\Delta$) velocity at the first grid point, $\tau_{w,i}=-[\kappa/\ln(y/y_{0,\mathrm r})]^2\sqrt{\hat{\bar u}^2+\hat{\bar w}^2}\,\hat{\bar u}_i$ for the two horizontal components; zero vertical velocity and stress-free top (§II A, Eq. 3). **Stated**
4. The rotor is a filtered actuator disk with local disk velocity and $C'_{\mathrm{Th}}=C_{\mathrm{Th}}/(1-a_{\mathrm i})^2$; with $a_{\mathrm i}=1/4$, $C_{\mathrm{Th}}=3/4$ and $C'_{\mathrm{Th}}=4/3$ (§II A–B, Eqs. 7–11). **Stated** *(compiler check, not in the sources: $(1-a_{\mathrm i})^2=0.75^2$ and $0.75/0.75^2=4/3$, consistent.)*
5. Domain $30D\times6D\times6D$, grid $192\times64\times97$ uniform (streamwise × spanwise × vertical, as printed), CFL 0.08, statistics over about 25 time units $D/u_\tau$ (§II B). **Stated**
6. The precursor total shear stress, resolved plus subgrid, is linear, $1-y/H_{\mathrm{dom}}$ when normalized by $u_\tau^2$, taken as evidence of stationarity; inflow profiles reproduce the wind-tunnel data (§II B, Eq. 13, Fig. 3). **Shown**
7. The bare steep-hill LES agrees overall with the Cao & Tamura mean streamwise velocity; reverse flow appears because $s_{\mathrm h}=0.4$ exceeds the 0.3 limit of Mason & King (§III A, Fig. 4). **Shown**
8. Streamwise turbulence intensity is underpredicted in the lower hill wake at $x/D=2.5$, attributed to the classical wall model in recirculating flow, as Yang et al. (2015) also report (§III A, Fig. 4b). **Shown** (attribution **Stated**, not tested)
9. With a turbine present, the mean velocity below the turbine wake increases in the hill wake (negative deficit), explained by mass-flux conservation (§III B, Figs. 5, 7). **Shown**
10. At $x/D=-2.5$ the maximum deficit is about the same for flat and hill cases, justifying identical boundary conditions in pressure-gradient wake models; the favourable pressure gradient then accelerates recovery on the windward side (§III B, Fig. 6). **Shown**
11. For $x_t/D=-5$ the wake centre follows the terrain windward and stays at about constant elevation behind the crest, as in Shamsoddin & Porté-Agel (2018); for $x_t/D=0$ and $1.25$ on the steep hill it deflects downward behind the hilltop (§III B, Fig. 7). **Shown**
12. For $x_t/D=-5$ the steep-hill wake recovers faster windward ($(x-x_t)/D\le5$) and slower leeward ($5\le(x-x_t)/D\le10$) than the gentle-hill wake; for $x_t/D=1.25$ the relative deficit first recovers slower, then faster than over flat ground (§III B, Fig. 8). **Shown**
13. $\sigma_{\mathrm w}$ grows linearly with $x$ over flat ground and, after $x/D=2.5$, on the gentle hill; it drops on the windward side (§III B, Fig. 9a). **Shown**
14. The Gaussian deficit fits flat and gentle cases except at the wake edges, but not the steep-hill wake for $2.5\le x/D\le6.25$ (significantly negative normalized deficit in the lower wake) until $x/D\ge7.5$ (§III B, Fig. 9b–d). **Shown**
15. Wake growth rate $k_{\mathrm w}=\mathrm d\sigma_{\mathrm w}/\mathrm dx$ at $x/D\ge7.5$: steep 0.0667, flat 0.0188, gentle 0.0146 (§III B). **Shown**
16. $C_{\mathrm{def}}(x)$ from LES agrees reasonably with the Bastankhah–Porté-Agel model (flat) and the Shamsoddin–Porté-Agel model (hills); the asymptotic Shamsoddin solution underestimates it for the gentle hill until the very far wake (§III B, Fig. 10). **Shown**
17. Since $C'_{\mathrm{Th}}$ is constant, power relative to flat ground is estimated without a turbine as the cube of the ratio of disk-integrated no-turbine velocities; the actuator-disk results collapse on this estimate (§III C, Eq. 19, Fig. 11a). **Shown**
18. Normalized power peaks at the crest, 1.8 (gentle) and 2.6 (steep); at $x_t/D=-5,-2.5$ the steep case gives less than flat ground, at $x_t/D=2.5$ power drops drastically (rotor partly in reverse flow), and $x_t/D=5,7.5,10$ remain severely affected; the gentle hill has no adverse effect behind it (§III C, Fig. 11). **Shown**
19. The hilltop is argued to be the best site (more energy, lower turbulence, hence less fatigue); turbines should not sit in the wake of steep hills (§III C, §IV). **Stated** (fatigue not computed)
20. Turbulence intensity in the turbine wake is non-axisymmetric with an upper-edge enhancement; on windward slopes it falls below flat-ground levels with the peak shifted downward; behind the hill the wake reduces turbulence below its lower half (§III D1, Figs. 12–16). **Shown**
21. The reduction below the wake behind the hill comes from a weaker shear layer and reduced $\langle u'v'\rangle$, i.e. reduced production $-\langle u'v'\rangle\partial_y\langle\bar u\rangle$ (§III D1, Fig. 17). **Shown**
22. The vertical turbulent flux decreases with slope on the windward side; behind hills it increases around the upper half of the wake and drops below the lower half (§III D2, Figs. 18–19). **Shown**
23. Flat-ground budget: mean convection is balanced by pressure transport in the near wake ($(x-x_t)/D\le2$), then by turbulent transport; production term much smaller; subgrid diffusion and dissipation negligible (§III E, Fig. 20a). **Shown**
24. Over hills pressure transport is the main contributor to mean-kinetic-energy restoration windward; pressure transport and mean convection mainly balance each other; turbulent transport is always a source (§III E, Fig. 20b–c). **Shown**
25. Pressure transport splits into streamwise, spanwise (zero by symmetry) and vertical parts; the streamwise part dominates for the gentle hill, the vertical part is non-negligible near the steep-hill crest (§III E, Eq. 23, Fig. 21). **Shown**
26. Grid study on four grids (GR1–GR4): GR1 underpredicts turbulence intensity at $x/D=1.25$, 2.5, 3.75; GR2–GR4 agree for the bare hill and GR3–GR4 for turbine wakes; GR3 is used (App. A, Table I, Fig. 22). **Shown**

The resolved mean-kinetic-energy budget (Eqs. 20–22), in registry
notation with $R_{ij}$ the time-averaged resolved stress:
$0=-\tfrac12\partial_j(\langle\bar u_j\rangle\langle\bar u_i\rangle^2)-\langle\bar u_i\rangle\partial_i\langle\bar p^*\rangle-\partial_j(\langle\bar u_i\rangle R_{ij})+R_{ij}\partial_j\langle\bar u_i\rangle-\partial_j(\langle\bar u_i\rangle\langle\tau^d_{ij}\rangle)+\langle\tau^d_{ij}\rangle\partial_j\langle\bar u_i\rangle$
(mean convection, pressure transport, turbulent transport, production
term, subgrid diffusion, dissipation), each integrated over a disk of
diameter $D$ centred on the wake centre and divided by its area. As
printed, the production term carries $+R_{ij}\partial_j\langle\bar u_i\rangle$,
so it is negative where the production of turbulent kinetic energy is
positive (the paper's "loss in MKE").

# Printed slips

- **Fig. 8 legend against §III B:** the legend reads "$x_t=3.5$", "$x_t=8.5$", "$x_t=9.75$" (no $/D$), while the text discusses turbines at $x_t/D=-5$, 0, 1.25.
- §III C writes the turbine positions with lowercase $d$ ("$x_t/d=1.25$", "$x_t/d=-1.25$"), $D$ being the rotor diameter everywhere else.
- Typos: "inhabit the wake recovery" (§III B), "much more smaller" (§III E), "the project method" for the projection method (§II A).
- Reference 12 lists "W. Yuan" twice among its authors.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$, $y$, $z$ | $x$, $z$, $y$ | **source $z$ is vertical (wall-normal), $y$ spanwise** |
| $\tilde{(\cdot)}$, $\tilde\Delta$ | $\bar{(\cdot)}$, $\Delta$ | LES filter; the source drops the tilde later |
| $\hat{\tilde u}_i$ (filter $2\tilde\Delta$) | $\hat{\bar u}_i$, $\hat\Delta=2\Delta$ | test filter in the wall model |
| $\bar{(\cdot)}$ | $\langle\cdot\rangle$ | **collision:** the source's overbar is the time average |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle_{\mathrm h}$ (page-local) | horizontal average in the precursor |
| $\tau^d_{ij}=-2\nu_t\tilde S_{ij}$ | $\tau^d_{ij}=-2\nu_t\bar S_{ij}$ | same sign convention |
| $\lvert\tilde S\rvert=\sqrt{2\tilde S_{ij}\tilde S_{ij}}$ | $\lvert\bar S\rvert$ | factor two present |
| $\tilde p^*=\tilde p/\rho+\tfrac13\tau_{kk}$ | $\bar p^*$ (page-local) | kinematic modified pressure |
| $\lambda=C_s\Delta$, $\lambda_0=C_0\Delta$ | $\ell_s$, $\ell_0$ (page-local), $\ell_0=C_{\mathrm{MT}}\Delta$ with $C_{\mathrm{MT}}$ of registry §11 | **collision** with the Taylor microscale $\lambda$; $\lambda_0(x)$ of App. B (B4) is another quantity |
| $z_0$ | $y_{0,\mathrm r}$ (registry §11) | roughness length |
| $u_*$, $L_z$ | $u_\tau$, $H_{\mathrm{dom}}$ (page-local) | |
| $\overline{u'w'}$ | $\langle u'v'\rangle$ | vertical turbulent flux |
| $\overline{u_i'u_j'}$ | $R_{ij}$ (resolved) | positive convention |
| $C_T$, $C_T'$, $a$ | $C_{\mathrm{Th}}$, $C'_{\mathrm{Th}}$, $a_{\mathrm i}$ | **collision:** $C_T$ is the TENO cut-off in the registry |
| $h$ | $h_{\mathrm{hub}}$ (page-local) | **collision** with the cell size $h$ |
| $H$, $L$, $S$ | $H$, $L_{\mathrm h}$, $s_{\mathrm h}$ (page-local) | **collisions:** $L$ integral scale, $S$ strain rate |
| $k=\mathrm d\sigma/\mathrm dx$, $\sigma$, $C(x)$ | $k_{\mathrm w}$, $\sigma_{\mathrm w}$, $C_{\mathrm{def}}$ (page-local) | **collision:** $k$ is not the TKE |
| TKE $=0.5(\sigma_u^2+\sigma_v^2+\sigma_w^2)/U_\infty^2$ | $k/U_\infty^2$ (resolved) | |
| $\kappa$ | $\kappa$ | value not printed |
| MC, PT, TT, TP, DF, DP | (budget terms, page-local) | Eq. 22 |

# Reference list

70 printed references, numbered AIP style, one with a DOI (ref 36). The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug; same-author same-year works (Shamsoddin 2017, 2018;
Ge 2021) are keyed in printed order, and the printed years of refs 11 and
56 are kept as printed. Ref [18] (Gao et al., Appl. Energy 307:118182,
2022) is another work than the ingested [gao-2022](/sources/gao-2022.md) and is keyed `gao-2022-b`. Ref 44 prints "A. Thomas, Jr. et al."; ref 65 is a
thesis, refs 52 and 57 are books. No item is unparseable.

# Pages created or updated

Chunk 11 (2026-10-27). This source is cited on:

- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Actuator line and actuator disk models](/methods/actuator-line-model.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [LESGO](/software/lesgo.md)

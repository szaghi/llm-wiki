---
type: Benchmark
title: "Turbulent round jets"
description: "Free round jets issuing into quiescent or co-flowing surroundings: their potential core, transition, spreading and centreline decay test compressible LES and its Reynolds-stress budgets from Mach 0.45 to 1.8 at Re 500,000, DNS and LES mesh-adaptation criteria at Re 4000, hp-adaptive hybrid RANS/LES, jet-noise chains and real-fluid DNS."
status: established
aliases: [round jet, free round jet, circular jet, axisymmetric jet, compressible round jet, forced round jet, PPRIME jet, potential core]
tags: [benchmark, les, dns, compressible, aeroacoustics, mesh-adaptation]
timestamp: 2026-10-29T05:14:00Z
---

# Turbulent round jets

A round jet of radius $r_0$ and diameter $D=2r_0$ issues with centreline
velocity $u_0$ into fluid at rest or into a slower co-flow. The annular
shear layer that separates the jet from its surroundings rolls up into
vortex rings close to the exit, the rings pair, break down and become
three-dimensional, and the layer thickens until it reaches the axis at the
end of the **potential core**, where the centreline velocity begins to
fall. Further downstream the jet becomes self-similar: the centreline mean
velocity $\langle u\rangle_{\mathrm{cl}}$ decays as $x^{-1}$ and the
half-width $r_{1/2}$, the radius where the mean velocity is half its
centreline value, grows linearly. On this page $x$ is the axial and $r$
the radial coordinate, $M_j$ the jet Mach number on $u_0$, $x_c$ the
potential-core length, $A$ the spreading rate and $B$ the decay constant
of the self-similar laws below (all page-local). In this bundle the round
jet tests large-eddy simulation of a free shear flow without walls, serves
as a test of mesh criteria for DNS and LES, and is the flow-noise source
of jet-noise computations.

## Self-similar laws and the potential core

[Rahatgaonkar & Ghosh (2025)](/sources/rahatgaonkar-2025.md), §III B 1,
fit the far field with the self-similar laws they take from Pope,
$$\frac{\langle u\rangle_{\mathrm{cl}}}{u_0}=B\,\frac{D}{x-x_0},\qquad
\frac{r_{1/2}}{D}=A\,\frac{x-x_0}{D},$$
$x_0$ a virtual origin, and define the potential-core length by
$\langle u\rangle_{\mathrm{cl}}(x_c)=0.95\,u_0$. For its dependence on the
Mach number of isothermal, perfectly expanded jets they print the
correlation of Lau et al. (1979), $x_c/D=4.2+1.1M_j^2$ (their Eq. 17;
Lau (1981), as they cite, found that it underestimates $x_c$ for
$M_j>1.37$), and propose the fit $x_c/D=4.925+0.915M_j^2$ through their
three LES (Eq. 18), claimed to predict $x_c$ better up to $M_j=1.8$.

## Compressibility effects at high Reynolds number

[Rahatgaonkar & Ghosh (2025)](/sources/rahatgaonkar-2025.md) simulate
three perfectly expanded, isothermal jets that differ only in $M_j=0.45$,
0.9 and 1.8, at $Re=5\times10^5$ on $D$ and $u_0$, which they set against
the highest Reynolds number of the earlier LES studies of Mach-number
effects they review, $3.6\times10^4$ (§I).

**Set-up.** The compressible Navier–Stokes equations are integrated in a
characteristic form in cylindrical coordinates with sixth-order
[compact central differences](/methods/compact-finite-difference-scheme.md),
a low-storage third-order Runge–Kutta scheme and the Mohseni–Colonius
axis treatment. The LES is a single-step explicit-filtering variant of
[approximate deconvolution](/methods/scale-similarity-model.md): at every
step the solution is filtered with $(Q_N*G)^2$, $Q_N$ the van Cittert
approximate inverse truncated at $N_{\mathrm{AD}}=6$ terms and $G$ a Padé
filter of parameter 0.2 in the azimuthal direction; there is no
eddy-viscosity subgrid model (§II B). The inflow is a tanh profile of
momentum thickness $0.05r_0$ with vortex-ring forcing of at most 3.3% of
$u_0$ and no nozzle (see
[inflow turbulence generation](/methods/inflow-turbulence-generation.md)),
with characteristic inflow conditions, partially non-reflecting radial
boundaries and an axial sponge over $55\le x/r_0\le60$. The grid is
$N_x\times N_\theta\times N_r=512\times128\times120$ on
$60r_0\times20r_0$, uniform in $x$ and $\theta$ and stretched radially
from $\Delta r/r_0\approx0.05$ on the axis to about 0.5 at the boundary;
runs last $800r_0/u_0$ with statistics over the last 300 (§II). Azimuthal
spectra at $r=r_0$ decay at the highest resolved wavenumbers, with a short
$k^{-5/3}$ range and the Nyquist wavenumber inside the inertial range,
which the authors take as evidence that grid and LES approach are adequate
(Fig. 3). Statistics are of resolved scales only.

**Validation at $M_j=0.9$.** The centreline decay matches reference LES and
the experiment of Lau et al., the half-width agrees "excellent[ly]" with
Bogey & Bailly and with Thaker & Ghosh after an axial shift of the
reference profiles to the same core length, the self-similar intensities
and shear stress averaged over $35\le x/r_0\le50$ agree with the LES of
Bogey & Bailly and the incompressible experiment of Panchapakesan & Lumley
(both at $Re=1.1\times10^4$), and the near-field overall sound pressure
level at $r=15r_0$ lies within 1.5 dB of the experiment of Bogey et al.
(2007), slightly above it, which the authors relate partly to an inflow
momentum thickness of order $10^{-2}r_0$ against $10^{-3}r_0$ in
experiments (§III A, Figs. 4–8).

**Mach-number trends** (§III B, Table II, Figs. 9–34):

| $M_j$ | core length relative to $M_j=0.45$ | spreading rate $A$ | decay constant $B$ | near-field noise peak at $r=15r_0$ |
|---|---|---|---|---|
| 0.45 | — | 0.108 | 5.28 | $x/r_0\approx13$ |
| 0.9 | +4.65% | 0.086 | 6.59 | $x/r_0\approx21$ |
| 1.8 | about +55% | 0.060 | 8.57 | $x/r_0\approx32$, above 135 dB |

- Increasing $M_j$ suppresses the early breakdown of the vortical
  structures: axisymmetric structures break down from $x/r_0\approx6$ at
  $M_j=0.45$, streamwise-elongated ones persist to $x/r_0\approx7.5$ at
  0.9, and highly stretched ones become three-dimensional only beyond
  $x/r_0\approx12$ at 1.8 (Fig. 9). All three jets are self-similar beyond
  $x=35r_0$, where they spread linearly and decay as $x^{-1}$; the
  authors find that the systematic fall of both $A$ and the decay rate
  with $M_j$ had not been distinctly identified at lower Reynolds numbers,
  and associate it with the changed large-scale structures of the
  transitional region rather than with the jet density ratio.
- In the self-similar region the centreline Mach number of the subsonic
  jets drops to low subsonic values, which is why their $M_j=0.9$ profiles
  match incompressible data, while that of the supersonic jet stays high
  subsonic (Fig. 15).
- In the transitional region, at the station of peak turbulent kinetic
  energy, the radial normal stress exceeds the axial one at $M_j=0.45$,
  the two are comparable at 0.9, and the axial stress is much larger at
  1.8; the peak Reynolds shear stress is comparable for the three jets,
  "in contrast to the findings of Bellan", who reported an increase with
  compressibility in low-Reynolds-number supersonic jets (Figs. 20–21). In
  the fully turbulent region all stress components fall from $M_j=0.45$ to
  0.9, less from 0.9 to 1.8, with no distinct change of anisotropy (Figs.
  22–23).

**Reynolds-stress budget.** From the budget of the Favre axial stress
$\langle\rho u''_xu''_x\rangle$ (their Eq. 19), the authors analyse the
production $\mathcal P_{xx}$ and the pressure–strain term $\phi_{xx}$
(registry §11). In the transitional region both peaks decrease with $M_j$
and move downstream, and they attribute the higher anisotropy of the
supersonic jet to the reduced pressure–strain correlation; in the fully
turbulent region both decrease with no change in anisotropy (Figs.
24–25). Splitting $\mathcal P_{xx}$ into mean-shear, mean-dilatation and
extra-strain parts (Eq. 20), the mean-shear part dominates the
transitional region, where the other two are small but grow with $M_j$,
while in the fully turbulent region the extra-strain part is comparable
to the mean-shear part (Figs. 26–29). The fall of $\mathcal P_{xx}$ with
$M_j$ comes from the reduced mean shear in the transitional region and
from the reduced Reynolds shear stress in the fully turbulent region
(Fig. 30). The authors present this as the first detailed analysis of
production and pressure–strain explaining compressibility effects on the
turbulence intensities of round jets (§IV).

**Near-field pressure.** The rms pressure along the shear layer peaks near
$x/r_0\approx5$, 8 and 13 for the three jets, close to the peak of the
turbulent kinetic energy, and grows strongly with $M_j$, whereas Bellan
reported a slight decrease at low Reynolds number (Fig. 32); the
directivity at $r=15r_0$ moves to larger angles with $M_j$, in
qualitative agreement with Brès & Lele, and the authors propose Mach-wave
radiation as an additional source for the supersonic jet (Figs. 33–34).

## A forced jet for DNS and LES mesh criteria

[Barbera et al. (2026)](/sources/barbera-2026.md), §3 and §5.1, use a
forced round jet in co-flow as the main test of mesh-adaptation criteria
for DNS and LES in the incompressible finite-volume solver YALES2 with
MMG3D remeshing (see [mesh adaptation](/methods/mesh-adaptation.md)): a
tanh inlet profile, $Re=(U_{\mathrm{in}}-U_{\mathrm{co}})R/\nu=4000$ on the
jet radius $R$ and the velocity difference between jet and co-flow, a
domain of $30R\times28R\times28R$, isotropic turbulence at 3% of the
velocity difference injected in the shear layer plus an axisymmetric
excitation at the linear-stability Strouhal number 0.033 and amplitude
2.5%, an initial uniform mesh of 307,806 elements, and statistics over
$170R/(U_{\mathrm{in}}-U_{\mathrm{co}})$ during adaptation and 600 such
units at the end (§3, Eqs. 21–22). The co-flow ratio and the inlet momentum
thickness are not printed.

- **DNS.** The DNS criterion targets a cell Reynolds number built on a
  subgrid velocity estimated from the filtered second derivatives of the
  instantaneous velocity. Targets from 0.5 down to 0.05 give final meshes
  of 75,093,339 to 920,442,715 elements, with mean and rms axial velocity
  at $x/D=1$, 5 and 10 the same for all targets; at 0.5 the $x/D=10$
  spectrum shows weak high-frequency ripples, attributed to under-resolved
  dissipative scales together with the implicit filtering of the
  finite-volume method (Figs. 2–4). With the target 0.125 the mesh size is
  $\Delta/\eta\approx1.5$ in the fully turbulent region and the subgrid
  part of the dissipation is below 5% of the total (Fig. 5), which the
  authors read as the criterion scaling the mesh to the Kolmogorov scale a
  priori (see
  [direct numerical simulation](/definitions/direct-numerical-simulation.md)).
- **LES.** With the [σ model](/methods/sigma-model.md) and a target ratio
  of integral length to filter width $L/\Delta_c$ from 5 to 25, the
  transition region near the inlet and the turbulent/non-turbulent
  interface stay meshed by the DNS criterion whatever $L/\Delta_c$, which
  acts after the potential core; the element count grows with $L/\Delta_c$
  from very-large-eddy to quasi-DNS resolution, mean and rms profiles agree
  with the DNS even at small $L/\Delta_c$, and the spectra approach the DNS
  for $L/\Delta_c>20$ (Figs. 7–9). Anisotropic meshes give very similar
  statistics with 2 to 3 times fewer elements, the anisotropy developing in
  the transition regions while the fully turbulent region stays isotropic
  (§5.1, Figs. 8, 10–11). The criteria are discussed on
  [grid-point requirements of LES](/results/les-grid-point-requirements.md).

## Jets as noise sources and in other solvers

- [Basile et al. (2023)](/sources/basile-2023.md) compute the isothermal
  PPRIME jet ($M_j=0.9$, $Re_D\simeq10^6$) with an hp-adaptive modal DG
  hybrid RANS/LES (ZDES mode 0+1) on 11.6, 18.9 and 31.7 million degrees
  of freedom: refinement lengthens the potential core, the intermediate
  mesh is closest to experiment on the centreline and the finest
  overpredicts the core length, agreeing with finer ZDES and implicit-LES
  references; the far-field noise from a Ffowcs Williams–Hawkings
  integral lies within about 1–2 dB of experiment (see
  [hybrid RANS/LES](/definitions/hybrid-rans-les.md) and the
  [Ffowcs Williams–Hawkings analogy](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)).
  Among the causes of the overlong core they list implicit LES and the
  missing nozzle–jet feedback, the missing turbulent tripping in the
  nozzle, and insufficient resolution, without a formal answer.
- [Moratilla-Vega et al. (2024)](/sources/moratillavega-2024.md) couple a
  second-order σ-model LES of a cold jet at acoustic Mach number 0.75 and
  $Re\approx7\times10^5$, isolated and below a flat plate, to a DG solver
  of the acoustic perturbation equations: the velocity-decay constants are
  7.5 (isolated) and 7.4 (installed) and the far-field spectra at 90° lie
  within 1–2 dB of experiment for $0.05<St<0.7$; no inflow turbulence is
  imposed.
- [Monteiro et al. (2026)](/sources/monteiro-2026.md), §4.5, validate the
  real-fluid thermodynamics of the GPU DNS solver RHEA-X on the
  supercritical nitrogen jet of Mayer et al. (case 4: injection at about
  133 K and 5.4 m/s through $D=2.2$ mm into nitrogen at 298 K and 3.98 MPa,
  above the critical pressure 3.39 MPa): the centreline density decay,
  with a potential core, a mixing region $5\lesssim x/D\lesssim25$ and
  self-similarity beyond, agrees closely with Raman data and is "a modest
  improvement" over the Favre-averaged RANS of the original study, and the
  spectra show a $k^{-5/3}$ range at $x/D=5$ and 30 (Figs. 7–8). The grid
  is not printed.

## What the case shows

- The potential-core length moves with the set-up: it lengthens with $M_j$ (about 55% from $M_j=0.45$ to 1.8 at
  $Re=5\times10^5$; Rahatgaonkar & Ghosh (2025)), and with mesh refinement
  of a hybrid RANS/LES at fixed $M_j=0.9$ (Basile et al. (2023)), and both
  sources compare their core with references only after accounting for the
  inflow: Rahatgaonkar & Ghosh shift the reference profiles axially to the
  same core length, and Basile et al. name the untripped nozzle among the
  causes of their overlong core.
- In the forced low-Reynolds-number jet of
  [Barbera et al. (2026)](/sources/barbera-2026.md) the transitional
  shear layer near the inlet needs DNS resolution whatever LES target is
  set, and the LES filter acts only downstream of the core.

## Qualifications

- [Rahatgaonkar & Ghosh (2025)](/sources/rahatgaonkar-2025.md) print two
  Reynolds numbers for the study of Maidi & Lesieur, $3.6\times10^4$ (§I,
  also stated as the highest of the earlier studies) and $7\times10^4$
  (§III B 1), without saying whether one is based on the radius. Their fit
  $x_c/D=4.925+0.915M_j^2$ gives $x_c/D=5.110$, 5.666 and 7.890 at
  $M_j=0.45$, 0.9 and 1.8, increases of 10.9% and 54.4% over the
  $M_j=0.45$ value, against the +4.65% and about +55% they print from the
  LES *(compiler check, not in the sources)*.
- In their budget, Eq. 19 prints the second production term with a plus
  sign, $+2\langle\rho u''_xu''_x\rangle\,\partial\langle u_x\rangle_\rho/\partial x$
  in registry notation, while Eq. 20 writes the corresponding part
  of $\mathcal P_{xx}$ with a minus sign. The three parts of Eq. 20 sum to
  $-\langle\rho u''_xu''_r\rangle\,\partial\langle u_x\rangle_\rho/\partial r-\langle\rho u''_xu''_x\rangle\,\partial\langle u_x\rangle_\rho/\partial x$,
  half of the production group of Eq. 19 apart from the sign of its second
  term *(compiler check, not in the sources)*; the paper does not say which
  normalization the plotted $\mathcal P_{xx}$ uses. Their overbar is the
  LES filter in §II B and a Reynolds average from §II D on, and their
  statistics and budgets are of resolved scales only.
- [Barbera et al. (2026)](/sources/barbera-2026.md) call their LES
  "implicitly filtered": the filter size is the local mesh size and the
  subgrid stress comes from the [σ model](/methods/sigma-model.md) (§3).
  Their mesh size $\Delta$ is the radius of the equivalent sphere of a
  cell, not an edge length.
- The inflow treatments differ: no nozzle and a forced tanh profile (Rahatgaonkar & Ghosh; Barbera et al., with
  co-flow), an untripped nozzle (Basile et al.), a nozzle whose contraction
  the authors expect to relaminarize the boundary layer (Moratilla-Vega et
  al.),
  and a sharp circular initial condition of a dense supercritical jet
  (Monteiro et al.). No source of this page compares its jet with that of
  another source of this page.

# Citations

- [Rahatgaonkar & Ghosh (2025)](/sources/rahatgaonkar-2025.md) — §I; §II A–D, Eqs. 6–16, Figs. 1–3; §III A, Table I, Figs. 4–8; §III B 1–5, Eqs. 17–20, Table II, Figs. 9–34; §IV.
- [Barbera et al. (2026)](/sources/barbera-2026.md) — §2.1–2.3; §3, Eqs. 21–22, Figs. 2–9; §4.1; §5.1, Figs. 10–11.
- [Basile et al. (2023)](/sources/basile-2023.md) — §4.1–4.4, Table 1, Figs. 9–14 (PPRIME jet, as its Source page records).
- [Moratilla-Vega et al. (2024)](/sources/moratillavega-2024.md) — §3; §4.2–4.3, Figs. 7–8, 15 (as its Source page records).
- [Monteiro et al. (2026)](/sources/monteiro-2026.md) — §4.5, Figs. 7–8.

---
type: Method
title: "Vreman model"
description: "Vreman's static eddy-viscosity model builds the subgrid viscosity from an invariant of the resolved velocity-gradient tensor that vanishes in many laminar flows; the sources print it in two index orders with constants from 0.08 to 0.17, use it in aircraft, channel, lattice Boltzmann, DG and shock-interaction LES, and recommend it with a recalibrated filter width for high-order wall-modelled LES."
status: established
aliases: [Vreman eddy-viscosity model, Vreman (2004) model, static-coefficient Vreman model]
tags: [les, sgs-model, eddy-viscosity, wmles]
timestamp: 2026-10-26T15:49:00Z
---

# Vreman model

The **Vreman model** is an eddy-viscosity closure of the deviatoric
[subgrid stress](/definitions/large-eddy-simulation.md),
$\tau^d_{ij}=-2\nu_t\bar S_{ij}$, with a static coefficient and a viscosity
built from an invariant of the resolved velocity-gradient tensor. The
sources cite Vreman (2004). Only
[Agrawal et al. (2022)](/sources/agrawal-2022.md) print it (§II.C, Eqs. 9–10):

$$\nu_t=2.5\,C_s^2\sqrt{\frac{B_\beta}{\alpha_{ij}\alpha_{ij}}},\qquad
\alpha_{ij}=\partial_j\bar u_i,\qquad
\beta_{ij}=\Delta^2\alpha_{mi}\alpha_{mj},$$

$$B_\beta=\beta_{11}\beta_{22}-\beta_{12}^2+\beta_{11}\beta_{33}-\beta_{13}^2+\beta_{22}\beta_{33}-\beta_{23}^2 ,$$

with $C_s\approx0.17$, the Smagorinsky coefficient (so the prefactor is
$2.5C_s^2\approx0.072$, *compiler check, not in the sources*). The symbols
$\alpha_{ij}$, $\beta_{ij}$, $B_\beta$ are page-local, and the index order
of $\alpha_{ij}$ and of the contraction in $\beta_{ij}$ is that printed by
Agrawal et al. Agrawal et al. state that the model gives zero dissipation
in laminar base flows with two velocity components and does not
overpredict dissipation in transitional flows. Unlike the
[dynamic procedure](/methods/dynamic-procedure.md), it needs no test
filter and no averaging; Agrawal et al. (§II.A) recall that the plain
[Smagorinsky model](/methods/smagorinsky-model.md), by contrast, does not
vanish at walls without damping.

## Other printed forms and constants

[Kim et al. (2022)](/sources/kim-2022.md) (§II, §III C) and
[Cai et al. (2022)](/sources/cai-2022.md) (§II.A, Eqs. 11–15) print the
model with the opposite index order, $\alpha_{ij}=\partial_i\bar u_j$, and
$\beta_{ij}=\alpha_{mi}\alpha_{mj}$ weighted by the grid spacing. Kim et
al. use a direction-dependent spacing,
$\beta_{ij}=\Delta_m^2\alpha_{mi}\alpha_{mj}$ (summed over $m$, $\Delta_m$
the grid size in direction $m$, page-local), and Cai et al. a single
$\Delta$ equal to the grid size; Cai et al. also write
$B_\beta=\tfrac12[(\mathrm{tr}\,\beta)^2-\mathrm{tr}(\beta^2)]$, the second
invariant of $\beta$. For a single $\Delta$ the two index orders give the
same viscosity: one $\beta$ is $\Delta^2G^TG$ and the other $\Delta^2GG^T$
for the velocity-gradient matrix $G$, which share their invariants, and
$\alpha_{ij}\alpha_{ij}$ is the same *(compiler check, not in the
sources)*. With direction-dependent $\Delta_m$ only the form of Kim et al.
is defined.
[Duan & Wang (2024)](/sources/duan-2024.md) (§2.4, Eq. 15) assume an
isotropic filter width and take it out of $\beta_{ij}$:
$\nu_t=(C_v\Delta)^2\sqrt{B_\beta/(\alpha_{ij}\alpha_{ij})}$ with
$\beta_{ij}=\alpha_{mi}\alpha_{mj}$ in the index order of Kim et al.
($\alpha_{ij}=\partial_i\bar u_j$), and relate the Vreman coefficient to the
Smagorinsky one by $C_v\approx\sqrt{2.5}\,C_s$ ($C_v$ page-local). This is
the form of Agrawal et al.: $B_\beta$ is quadratic in $\beta$, so a
$\Delta^2$ inside $\beta$ comes out of the square root as $\Delta^2$, and
$C_v^2=2.5C_s^2$ *(compiler check, not in the sources)*. Duan & Wang do
not print the value of $C_v$ used in their runs.

| $C_s$ in $\nu_t=2.5C_s^2\sqrt{B_\beta/(\alpha_{ij}\alpha_{ij})}$ | Context | Source |
|---|---|---|
| about 0.17 | the Smagorinsky coefficient | Agrawal et al. (2022), §II.C |
| 0.08 | static baseline and pretraining target in wall-resolved channel LES | Kim et al. (2022), §III C |
| about 0.1, "the Smagorinsky constant" | lattice Boltzmann LES of the Ahmed body | Cai et al. (2022), §II.A |

[Blind et al. (2023)](/sources/blind-2023.md) (§2.3, §3, §3.3) use "the
Vreman model constant" 0.03 for wall-resolved channels, the value of
Toosi & Larsson (cited), and 0.11 for the wall-modelled channel,
"from previous experience". The paper does not print the model formula,
so it cannot be decided whether these values are $C_s$ or the prefactor
$2.5C_s^2$ of the table. Their length scale is the DG one,
$\Delta=\mathrm{Vol}^{1/3}/(N+1)$ for an element of volume Vol and degree
$N$ (the paper's $P$), with $N=5$.

## Use in the sources

- **High-lift aircraft.** [Goc et al. (2021)](/sources/goc-2021.md)
  (§2.1, §3.1–3.2) use the static-coefficient Vreman model with an
  equilibrium wall model for the free-air computations of the JAXA Standard
  Model at $Re_c=1.96\times10^6$, $M_\infty=0.172$, in two low-dissipation
  codes (charLES, Alya). At baseline resolution (charLES 32 million cells,
  $\delta_{99}/\Delta\approx10$ at the main-element trailing edge) the lift
  curve, $C_{L,\max}$ and stall onset are captured reasonably; the in-tunnel
  cases switch to the dynamic Smagorinsky model. See
  [JAXA Standard Model](/benchmarks/jaxa-standard-model.md).
- **Burner LES.** In the LES zones around the embedded DNS box of a premixed
  Bunsen jet, the SGS momentum fluxes "are modeled" with a citation of
  Vreman's paper, the model not being named in the text
  ([Domingo & Vervisch 2023](/sources/domingo-2023.md), §3.1).
- **Cavity noise.** [Krais et al. (2021)](/sources/krais-2021.md) (§7.3)
  run a zonal wall-modelled LES of an open cavity in FLEXI ($N=7$, 30
  million degrees of freedom per variable, $Re_\theta=6300$) with the
  Kawai–Larsson wall model and the Vreman model, which "helps to reduce
  artificial pressure fluctuations caused by the wall-model". Vreman is
  also listed among FLEXI's eddy-viscosity models (§2.2.3).
- **Gaussian bump.** Agrawal et al. (2022, §VIII) compare Vreman with the
  dynamic Smagorinsky and the
  [tensor-coefficient](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
  models in charLES wall-modelled LES. On the spanwise-periodic bump
  ($Re_L=2\times10^6$) Vreman converges non-monotonically in $C_f$ (as DSM
  does) and predicts a smaller separation bubble than the quasi-DNS
  (Figs. 13–14). On the 3D bump ($Re_L=3.41\times10^6$, up to 452 million
  cells) it misses the separation, the apex pressure peak and the
  counter-rotating vortex pair even on the finest grid (Figs. 15–19),
  agreeing with Iyer & Malik, who are recalled to find no separation with
  Vreman up to 450 million control volumes.

- **Shock/boundary-layer interaction over a flexible panel.**
  [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) (§3) use the Vreman
  model in a compressible finite-volume wall-modelled LES on unstructured
  hexahedra in arbitrary Lagrangian–Eulerian form, with the Kawai–Larsson
  equilibrium wall model, hybrid ENO/central second-order numerics and a
  digital-filter inflow, coupled to a finite-element panel solver for a
  Mach 3 oblique-shock interaction ($Re_\infty=49.4\times10^6$ m$^{-1}$,
  $\delta_0=4$ mm, about 20 million cells spanwise-periodic). No formula or
  constant of the model is printed. See [wall-modelled LES](/methods/wall-modelled-les.md).
- **Jet reference LES.** Among the reference simulations of the PPRIME
  $M_j=0.9$ round jet listed by [Basile et al. (2023)](/sources/basile-2023.md)
  (Table 1), the LES of Brès et al. uses the Vreman model with a
  second-order finite-volume scheme on 16 and 69 million cells, with
  turbulent injection in the nozzle; Basile et al. note that dof
  comparisons with it are not like-for-like, because it uses a wall model
  and turbulent injection (§4.2.3).

- **Wall-resolved channel, learned-model baseline.** Kim et al. (2022, §II,
  §III C, Fig. 7) use the static Vreman model ($C_s=0.08$) as a baseline
  and as the pretraining target of their
  [reinforcement-learning SGS model](/methods/reinforcement-learning-closure.md),
  noting that it needs only first derivatives and no ad hoc averaging. At
  $Re_\tau=180$ on $(\Delta x^+,\Delta z^+)=(70.7,35.3)$ it predicts the
  mean velocity reasonably but over-estimates the Reynolds shear stress and
  under-predicts the mean subgrid transport $\langle\partial_j(\tau_{ij}\bar u_i)\rangle$
  compared with filtered DNS. Pretraining on Vreman converges slightly
  faster than on the dynamic Smagorinsky model (§II D, no results shown).
- **Lattice Boltzmann LES with an immersed boundary.** Cai et al. (2022,
  §II.A, §II.C.1) use the model in the lattice Boltzmann solver ProLB on
  octree Cartesian grids for the Ahmed body with a 35° slant; near the wall
  a constrained-LES eddy viscosity built on it imposes the total shear
  stress of a mixing-length RANS model (see
  [hybrid RANS/LES](/definitions/hybrid-rans-les.md) and
  [immersed boundary methods](/methods/immersed-boundary-method.md)).
- **DG grid adaptation.** Blind et al. (2023, §2.2–2.3) use the model in
  [FLEXI](/software/flexi.md) to estimate the LES modelling residual that
  drives [mesh adaptation](/methods/mesh-adaptation.md): the residual is
  evaluated on a test-filtered field with only the Vreman length scale
  changed, to $\hat\Delta=[(N+1)/(N_f+1)]^{1/3}\Delta$ for a modal test
  filter that keeps degrees up to $N_f=3$ ($N_f$ page-local, as on the
  mesh-adaptation page; the paper's $M$). In the
  wall-modelled channel at $Re_\tau=2000$ the constant 0.11 is used with a
  Spalding wall law at $h_{\mathrm{wm}}=0.1\delta$ (§3.3). See
  [wall-modelled LES](/methods/wall-modelled-les.md).
- **HORSES3D.** The model is one of the explicit LES models of the
  [HORSES3D](/software/horses3d.md) DG code, with Smagorinsky and WALE
  ([Ferrer et al. 2023](/sources/ferrer-2023.md), §4.1; no formula printed).

- **Building-block-flow wall model.** [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md)
  (§3.2, §4.2–4.5) run their machine-learned
  [building-block-flow wall model](/methods/building-block-flow-wall-model.md)
  and the [equilibrium wall model](/methods/equilibrium-wall-model.md)
  with the Vreman and the dynamic Smagorinsky models in charLES (no
  equations printed). In the laminar Blasius boundary layer all four
  combinations give the mean velocity within 5%, the equilibrium model
  benefiting from cancellation between its own and the SGS-model errors;
  across the cases, the SGS-model errors at the matching location limit
  the accuracy of the learned wall model (§4.2, §6). See
  [wall-modelled LES](/methods/wall-modelled-les.md).
- **DG Taylor–Green vortex.** [Kou et al. (2023)](/sources/kou-2023.md)
  (§4.2, Fig. 12) adapt the Vreman and Smagorinsky models to the DG code
  [HORSES3D](/software/horses3d.md) and find both inferior to
  [jump-penalty stabilization](/methods/jump-penalty-stabilization.md) at
  $Re=1600$ ($32^3$ elements, $N=3$): lower peak dissipation rate, higher
  dissipation before the peak and significant dissipation at mid
  wavenumbers. No constant or filter width is printed.

## Spectral-element LES

Two sources use the model in continuous-Galerkin
[spectral-element](/methods/spectral-element-method.md) codes.

- **Form and constant in NUMA.**
  [Reddy et al. (2026)](/sources/reddy-2026.md) (§3.2, Eqs. 9a–b) print
  the model in the index order of Kim et al.:
  $\beta_{ij}=\Delta_k^2\,\partial_k\bar u_i\,\partial_k\bar u_j$ (summed
  over $k$), with a direction-dependent effective resolution $\Delta_k$,
  equal in all directions in their runs. The prefactor is
  $c\approx2.5C_s^2$, with the Smagorinsky value $C_s=0.14$, raised to 0.21
  for a Burgers test. The prefactor is therefore about 0.049
  *(compiler check, not in the sources)*. To the authors' knowledge the
  model "has not been previously studied within the spectral element
  framework or in the context of atmospheric flows" (§3.2).
- **Results in NUMA ($N=4$, filter width $\min(h_x,h_y,h_z)/(N+1)$).**
  Reddy et al. compare Vreman with Smagorinsky and the
  [residual-based dynamic model](/methods/residual-based-dynamic-sgs-model.md):
  - In passive-tracer transport, the errors in the extrema are about
    0.05 kg/kg, against 0.12–0.15 kg/kg for Smagorinsky (§5.2).
  - In a two-dimensional inviscid Burgers system with discontinuities,
    Vreman oscillates and diverges at $t=0.7$ s, while the residual-based
    model, with one coefficient per equation, stays stable. The authors
    attribute the divergence to the single coefficient shared by both
    equations (§6.2).
  - In the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
    ($32^3$ elements), Vreman conserves more kinetic energy than
    Smagorinsky (§7.2).
  - In the Straka density current, Vreman and Smagorinsky resolve
    Kelvin–Helmholtz rotors already at 50 m spacing, with similar enstrophy
    and the largest tracer overshoots (§8.2).
- **Wall-modelled LES in Nek5000.**
  [Mukha et al. (2025)](/sources/mukha-2025.md) (§II.D, §III) use Vreman in
  [Nek5000](/software/nek5000.md) ($N=7$) for
  [wall-modelled LES](/methods/wall-modelled-les.md) of channel flow at
  $Re_\tau\approx8000$ and of a flat-plate boundary layer.
  - The constant is $2.5C_s^2$ with $C_s=0.16$, which the authors call
    "slightly below the theoretical value for homogeneous isotropic
    turbulence".
  - The length scale is the maximum GLL spacing in the element, assigned to
    the whole element.
  - $\nu_t$ is not forced to zero at the wall. Its asymptote is linear in
    $y$, but no decrease toward the wall is discernible, whereas the Sigma
    model, with a cubic asymptote, visibly reduces $\nu_t$. The authors
    conclude that "not only the asymptotic behavior … but also how fast the
    model transitions towards the asymptote" matters (§III.C).
  - Of the closures tested on the finest channel mesh (Vreman, Sigma and a
    high-pass relaxation filter), Vreman stabilizes best and gives the
    smoothest derivatives.
  - The wall stress computed from the mean wall gradient deviates from the
    modelled one by 8.07% with Vreman, against −25.72% with Sigma and
    −84.85% with the filter.
  - With Vreman, the mean velocity is within 1% of DNS for $y>0.1\delta$ on
    all three meshes, and the boundary-layer skin friction is within 2% of
    wall-resolved LES on the finest mesh (§III.B, §IV.B).

## Filter width for high-order wall-modelled LES

Duan & Wang (2024) keep the model coefficients and recalibrate the filter
width instead, in the flux-reconstruction (FR/CPR) solver hpMusic with an
element-averaged eddy viscosity and zero interface flux of the subgrid
stress (§3, Eqs. 26–27; see
[flux reconstruction](/methods/flux-reconstruction.md)). For an element of
volume $V$ and polynomial degree $N$ (the paper's $P$) they test three
widths (Eqs. 28–30):

$$\text{d1: }\Delta=V^{1/3},\qquad\text{d2: }\Delta=\frac{V^{1/3}}{\sqrt{N+1}},\qquad\text{d3: }\Delta=\frac{V^{1/3}}{N+1}.$$

d1 is the finite-volume convention, d3 the per-degree-of-freedom choice
the paper calls natural (it is also the length scale
$\mathrm{Vol}^{1/3}/(N+1)$ of [Blind et al.](/sources/blind-2023.md)
above), and d2 their new intermediate value,
introduced because subgrid models were calibrated on second-order schemes
and high-order schemes carry less numerical dissipation, so d3 is expected
to under-dissipate (§3).

- In the wall-modelled [channel](/benchmarks/turbulent-channel-flow.md) at
  $Re_\tau=5200$ ($60\times16\times40$ elements, $\Delta x^+=1088$,
  $\Delta y^+=650$, $\Delta z^+=544$ element sizes, $N=2$ to 5, equilibrium
  wall model with the exchange point at the first element interface), the
  Vreman results are consistent across degrees: d1 always too dissipative,
  d3 too little, d2 best in the mean velocity (§5.4, Figs. 11–14). The same
  holds at $Re_\tau=544$ on the same mesh at $N=3$ (Fig. 15). No-model
  implicit LES was not stable on this mesh (§5.4).
- In the dissipation ranking of the three models tested, Vreman sits
  between [WALE](/methods/wale-model.md) (least dissipative) and
  [Smagorinsky](/methods/smagorinsky-model.md) (§5.1–5.2, §6); in decaying
  isotropic turbulence WALE and Vreman give similar spectra, Vreman
  slightly more damped.
- In the wall-resolved channel at $Re_\tau=180$ ($N=3$), Vreman and WALE
  match DNS in the viscous sublayer $y^+<10$; with d1 both are poor in the
  buffer and log regions, with d2 and d3 they agree well (§5.3, Figs.
  9–10).

The authors recommend Vreman with d2 for high-order wall-modelled LES
(§6); the recommendation rests on visual comparison of profiles with DNS,
no error norm being tabulated. It was obtained with their element-averaged
viscosity and zero interface subgrid flux (§3).

## Fluctuating viscosity and the mean stress

[Haering et al. (2022)](/sources/haering-2022.md) (§V D) list Vreman with
Smagorinsky and WALE as fluctuating-viscosity models: used as the
energy-transfer part of their model-split hybrid, their correlation with
the strain gives a contribution to the mean stress that would have to be
computed and subtracted from the mean-stress model.

## Qualifications

- Blind et al. (2023, §2.3) state that the test-level eddy viscosity is "a
  factor of $[(P+1)/(M+1)]^{2/3}\approx1.59$ larger"; with the printed
  $P=5$ (the registry's $N$) and $M=3$ (here $N_f$), $(6/4)^{2/3}\approx1.31$ *(compiler
  check, not in the sources)*, so the printed number or the printed
  exponent is wrong. The page records the version read (arXiv
  2301.03199v1).
- The constants in the table belong to different flows, filter-width
  definitions and codes; none of the sources calibrates the constant.

# Citations

- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §II.C, Eqs. (9)–(10); §VIII.A–B, Figs. 13–19.
- [Goc et al. (2021)](/sources/goc-2021.md) — §2.1; §3.1–3.2.
- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — §3.1.
- [Krais et al. (2021)](/sources/krais-2021.md) — §2.2.3; §7.3, Fig. 27.
- [Haering et al. (2022)](/sources/haering-2022.md) — §V D.
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) — §3.
- [Basile et al. (2023)](/sources/basile-2023.md) — §4.2.3, Table 1.
- [Kim et al. (2022)](/sources/kim-2022.md) — §II; §II D; §III C, Fig. 7.
- [Cai et al. (2022)](/sources/cai-2022.md) — §II.A, Eqs. (11)–(15); §II.C.1.
- [Blind et al. (2023)](/sources/blind-2023.md) — §2.2–2.3; §3; §3.3.
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §4.1.
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §3.2; §4.2–4.5; §6.
- [Kou et al. (2023)](/sources/kou-2023.md) — §4.2, Fig. 12.
- [Duan & Wang (2024)](/sources/duan-2024.md) — §2.4, Eq. (15); §3, Eqs. (26)–(30); §5.1–5.4, Figs. 5–15; §6.
- [Reddy et al. (2026)](/sources/reddy-2026.md) — preprint of 4 March 2021: §3.2, Eqs. (9a)–(9b); §5.2; §6.2; §7.2; §8.2.
- [Mukha et al. (2025)](/sources/mukha-2025.md) — arXiv v1: §II.D; §III.B–III.C, Figs. 1–8, Table II; §IV.B.

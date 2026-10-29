---
type: Method
title: "Vreman model"
description: "Vreman's static eddy-viscosity model builds the subgrid viscosity from an invariant of the resolved velocity gradient that vanishes in many laminar flows; the sources print it in two index orders with coefficients from 0.06 to 0.17 and use it from aircraft to detonation LES, with a recalibrated width for high-order WMLES and a small constant best for bump separation."
status: established
aliases: [Vreman eddy-viscosity model, Vreman (2004) model, static-coefficient Vreman model]
tags: [les, sgs-model, eddy-viscosity, wmles]
timestamp: 2026-10-29T10:10:00Z
---

# Vreman model

The **Vreman model** is an eddy-viscosity closure of the deviatoric
[subgrid stress](/definitions/large-eddy-simulation.md),
$\tau^d_{ij}=-2\nu_t\bar S_{ij}$, with a static coefficient and a viscosity
built from an invariant of the resolved velocity-gradient tensor. The
sources cite Vreman (2004).
[Agrawal et al. (2022)](/sources/agrawal-2022.md) print it as (§II.C, Eqs. 9–10)

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
the grid size in direction $m$, the registry-§11 $\Delta_k$), and Cai et al. a single
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
| 0.1 | compact-difference LES of the transitional Taylor–Green vortex | [Caban et al. (2026)](/sources/caban-2026.md), §2, Eq. (7) |
| $\approx0.063$ ($c=2.5C_s^2=0.01$) and $\approx0.167$ ($c=0.07$) | gas-kinetic channel LES at $Re_\tau=180$ (best of $c=0.01$–0.1) and 395 (after Vreman 2004) | [Zhao et al. (2021)](/sources/zhao-2021-c.md), §III.B, §IV |
| 0.1 ($c=2.5C_s^2=0.025$) | gas-kinetic implicit-versus-explicit LES of the compressible Taylor–Green vortex | [Cao et al. (2022b)](/sources/cao-2022-c.md), §III, Eqs. (10)–(11) |
| 0.1 ($c=2.5C_s^2=0.025$) | the same comparison on $64^3$, $128^3$ and $256^3$ | [Wang et al. (2026)](/sources/wang-2026.md), §II B, Eqs. (14)–(15) |
| 0.1 (prefactor $c=0.025$; printed $C_V$) | finite-volume LES of a sinusoidally forced periodic shear flow on $16^3$ | [Hausmann et al. (2022)](/sources/hausmann-2022.md), §III B, Eqs. (42)–(45) |
| 0.1 (prefactor printed as $2.5C_s^2$, with $C_s=0.1$ after Sayadi & Moin and Yu et al., cited) | sixth-order finite-difference LES of compressible channels and a supersonic boundary layer, baseline against a learned model | [Xu et al. (2023)](/sources/xu-2023.md), §2.2 |
| constant $c=0.025$ and $c=0.07$ printed, formula not printed | incompressible second-order finite-volume wall-modelled LES of the Gaussian bump | [Zhou & Bae (2024)](/sources/zhou-2024-b.md), §2.1 |
| constant $C=0.07$ printed, "as specified in the original paper", formula not printed | compressible reacting LES of a rotating detonation rocket engine | [Vignat et al. (2024)](/sources/vignat-2024.md), §3.3 |
| prefactor $c_v=0.07$ printed in $\mu_t=\bar\rho\,c_v\sqrt{B_\beta/(\alpha_{ij}\alpha_{ij})}$, with an isotropic filter width | flux-reconstruction wall-modelled LES of channels and the periodic hill | [Gao et al. (2025b)](/sources/gao-2025-b.md), §II B, Eqs. (11)–(16) |
| not printed | high-order finite-difference (aeroacoustic) wall-modelled LES of channels and a boundary layer | [Gao et al. (2025)](/sources/gao-2025.md), §II.A |

Cao et al. (2022b, Eqs. 10–11) print the dynamic viscosity
$\mu_t=\bar\rho\,c\sqrt{B_\beta/(\alpha_{ij}\alpha_{ij})}$ in the index
order of Kim et al. ($\alpha_{ij}=\partial_i\bar u_j$,
$\beta_{ij}=\Delta_m^2\alpha_{mi}\alpha_{mj}$) with $c=2.5C_s^2=0.025$.
Hausmann et al. (2022, Eqs. 42–45) print a third index pattern,
$\beta_{ij}=\Delta^2\alpha_{ik}\alpha_{jk}$ with $\alpha_{ij}=\partial_j\bar u_i$,
and the prefactor $c=0.025$ (the source's $C_V$); this $\beta$ is the same
matrix $\Delta^2GG^T$ as the single-$\Delta$ form of Kim et al., so it gives
the same viscosity as the other orders, and the $C_s$ of the table is
$\sqrt{0.025/2.5}=0.1$ *(compiler check, not in the sources)*.

[Zhao et al. (2021)](/sources/zhao-2021-c.md) (§III.B, Eq. 17) print the
dynamic viscosity $\mu_t=\bar\rho\,c\sqrt{B_\beta/(\alpha_{ij}\alpha_{ij})}$
in the index order of Kim et al. ($\alpha_{ij}=\partial_i\bar u_j$) with
directional cell widths, $\beta_{ij}=\Delta_m^2\alpha_{mi}\alpha_{mj}$,
and $c=2.5C_s^2$; "the grids themselves act as the filter". They print the
constant $c$, not $C_s$; the $C_s$ values of the table are $\sqrt{c/2.5}$
*(compiler check, not in the sources)*.

Caban et al. (2026, §2, Eq. 7) print the model in the index order of
Agrawal et al. ($\alpha_{lm}=\partial_m\bar u_l$,
$\beta_{lm}=\Delta^2\alpha_{kl}\alpha_{km}$) and write the stress as
$-2c\sqrt{B_\beta/(\alpha_{lm}\alpha_{lm})}\,\bar S_{ij}$ with the
prefactor $c=2.5C_s^2$ (the source's $C_v$, not the $C_v$ of Duan & Wang
above), i.e. $c=0.025$ for their $C_s=0.1$ *(compiler check, not in the
sources)*.

[Xu et al. (2023)](/sources/xu-2023.md) (§2.2) print the form of Kim et
al., $\alpha_{ij}=\partial_i\tilde u_j$ and
$\beta_{ij}=\sum_m\Delta_m^2\alpha_{mi}\alpha_{mj}$ with the local grid
widths, for the compressible (Favre-filtered) velocity, and complete it
with an isotropic part $\tau_{kk}=2C_I\sqrt{B_\beta/(\alpha_{ij}\alpha_{ij})}\,\lvert\tilde S\rvert$
whose coefficient they set to $C_I=0$, and a subgrid heat flux with
$Pr_t=0.9$, both after Sayadi & Moin (cited).

[Blind et al. (2023)](/sources/blind-2023.md) (§2.3, §3, §3.3) use "the
Vreman model constant" 0.03 for wall-resolved channels, the value of
Toosi & Larsson (cited), and 0.11 for the wall-modelled channel,
"from previous experience". The paper does not print the model formula
and does not state whether these values are $C_s$ or the prefactor
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
  In the wall-modelled LES technology focus group of the fourth AIAA
  High-Lift Prediction Workshop, summarized by
  [Kiris et al. (2023)](/sources/kiris-2023.md) (§II.4, Table 2), four of
  the nine submissions on the
  [CRM high-lift configuration](/benchmarks/nasa-crm-high-lift.md)
  (NASA LAVA, Boeing BCFD, Alya, NASA FUN3D) close the subgrid stress with
  the constant-coefficient Vreman model and an equilibrium wall model; the
  charLES team, which uses the dynamic Smagorinsky model, "reported little
  sensitivity" between the two on its intermediate grids. No constant is
  printed.
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
  agreeing with Iyer & Malik, whom Agrawal et al. cite as finding no
  separation with Vreman up to 450 million control volumes.

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

- **Compact-difference Taylor–Green vortex.** [Caban et al. (2026)](/sources/caban-2026.md)
  (§5.3.1, Figs. 18, 20, 22, Table 4) find Vreman "very similar" to
  [Smagorinsky](/methods/smagorinsky-model.md) at $Re=1600$ on $64^3$ in a
  sixth-order compact-difference code. Without numerical filtering both are
  unstable at $\Delta=2h$ and stable but inaccurate at $\Delta=4h$. With
  an explicit regularization filter, Vreman at $\Delta=2h$ gives the best
  eddy-viscosity result of the paper, an energy error at $t=20$ of
  $4.33\times10^{-2}$ against $4.76\times10^{-2}$ for Smagorinsky, but
  about twice the $2.23\times10^{-2}$ of [implicit LES](/definitions/implicit-les.md)
  with the same filter, because the total dissipation is too large. Their
  scale-similarity and deconvolution models do better (see
  [scale-similarity models](/methods/scale-similarity-model.md)).

- **Gas-kinetic channel LES.** In wall-resolved channel flow with the
  [high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md),
  where the viscosity enters the BGK collision time, Zhao et al. (2021,
  §IV–V, Tables III, V–VII) scan $c$ from 0.01 to 0.1 at $Re_\tau=180$
  and keep the best, $c=0.01$ (results of the scan not shown), and take
  $c=0.07$ at 395 from Vreman (2004). The realized $Re_\tau$ is 174.99
  at 180 ($96^3$; DNS 178.12) and 351.36 and 370.13 at 395 ($96^3$,
  $128^3$; DNS 392.24), below the dynamic Smagorinsky model and the
  no-model run; the Vreman model is the cheapest explicit model (0.534 s
  per step against 0.520 s without model; see
  [implicit LES](/definitions/implicit-les.md)).
- **Wall-model-integrated DG LES.** [Lv et al. (2021)](/sources/lv-2021.md)
  (§III A, Eq. 15) close the compressible LES of their solver (discontinuous
  Galerkin in the wall-adjacent cells, finite volume elsewhere) with the
  Vreman model (Vreman 2004; You & Moin, cited) and an
  eddy diffusivity with $Pr_t=0.9$, for channel flow up to
  $Re_\tau=50\,000$ and the periodic hill at $Re_h=10\,595$; no constant
  or formula is printed, and the paper does not define the strain in its
  stress $\mu_t\tilde S$ (factor two, trace). The subgrid model is not
  varied; the subject is the wall treatment (see
  [non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)).
- **Implicit against explicit LES with a gas-kinetic scheme.** Cao et
  al. (2022b, §IV A, §IV C, Figs. 2–3, 8, Table II) compare the Vreman,
  static [Smagorinsky](/methods/smagorinsky-model.md) and
  [dynamic](/methods/dynamic-procedure.md) models with no-model
  [implicit LES](/definitions/implicit-les.md) on the compressible
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) ($M=0.1$,
  $Re=1600$, $256^3$) with the fourth-order
  [gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md), the
  eddy viscosity entering through the collision time. Vreman behaves like
  static Smagorinsky: both are farther from the $1024^3$ DNS than implicit
  LES in the enstrophy dissipation, and their total subgrid dissipation,
  measured a posteriori as $-\mathrm dE_k/\mathrm dt$ minus the resolved
  physical dissipation, is about twice that of implicit LES at $t=2.5$–10
  (Vreman $2.6\times10^{-5}$, $3.2\times10^{-4}$, $1.3\times10^{-3}$
  against $1.5\times10^{-5}$, $1.4\times10^{-4}$, $6.7\times10^{-4}$, Table
  II). The same ordering holds on $128^3$ and $384^3$ (App. B).
  The sequel, [Wang et al. (2026)](/sources/wang-2026.md) (§II B,
  Eqs. 14–15), prints the same form,
  $\mu_t=\bar\rho\,c\sqrt{B_\beta/(\alpha_{ij}\alpha_{ij})}$ with
  $\alpha_{ij}=\partial_i\bar u_j$ and $\beta_{ij}=\Delta_m^2\alpha_{mi}\alpha_{mj}$
  (one width on their uniform grids), and runs it on $64^3$, $128^3$ and
  $256^3$ against a $512^3$ DNS. Vreman and Smagorinsky give nearly
  identical modelled dissipation, higher than the dynamic model on every
  grid, and a modelled share that rises to most of the subgrid dissipation
  on $256^3$ (§III B, Figs. 3, 6). Judged by PDFs of the resolved velocity
  gradients, Vreman is farther from DNS than implicit LES on $64^3$ and
  $128^3$ (time-averaged Jensen–Shannon divergence against filtered DNS
  $4.77\times10^{-3}$ and $9.39\times10^{-4}$, against $4.16\times10^{-3}$ and
  $8.01\times10^{-4}$) and closest of all on $256^3$ ($1.95\times10^{-4}$,
  Wasserstein-1 $6.94\times10^{-3}$), mainly from late decay (§IV B,
  Table I); against unfiltered DNS on $256^3$ it has the largest
  Wasserstein-1 distance of the four runs, $1.45\times10^{-2}$ (Table II).
  Details on [implicit LES](/definitions/implicit-les.md).
- **Transitional shear flow.** Hausmann et al. (2022, §III A–B) choose
  Vreman over Smagorinsky for a sinusoidally forced periodic shear flow
  ($Re_{\mathrm{shear}}=3115$, LES on $16^3$ against a $128^3$ DNS),
  citing Smagorinsky's inaccuracy in shear-dominated flows and calling
  Vreman "known to produce more physical results in transitional shear
  flows". At that resolution the Vreman LES over-predicts the amplitude of
  the mean velocity, hence the mean kinetic energy, and its velocity
  correlations deviate from the DNS, most in the normal components
  (§IV B, Figs. 6, 12a). The LES is the carrier of their
  [subgrid velocity enrichment](/methods/subgrid-velocity-enrichment.md).
- **Compressible wall-bounded LES against a learned model.** Xu et al.
  (2023) test Vreman beside the dynamic Smagorinsky and
  [WALE](/methods/wale-model.md) models against filtered DNS of a
  compressible channel at $Re=3000$, $M=1.5$: a priori, the correlation
  coefficients of all three with the true subgrid stress are "almost lower
  than 0.6" and the relative errors near 1.0 (§2.2, Figs. 1–3). A
  posteriori (sixth-order central differences, untrained grid
  $64\times65\times64$) Vreman overpredicts the van Driest log-region
  velocity and the r.m.s. peaks, transfers energy only forward, and
  underestimates the mean subgrid fluxes of kinetic energy and temperature
  variance (§4.1, Figs. 13–20); it is the cheapest of the explicit models,
  0.28 of the dynamic Smagorinsky cost per step (Table 4). See
  [neural-network SGS models](/methods/neural-network-sgs-model.md).
- **Listed only.** [Qi et al. (2022)](/sources/qi-2022-b.md) (§1) list the
  Vreman model as "a low dissipation eddy-viscosity model … for turbulent
  shear flows" that "can also predict transitional flow well", among
  eddy-viscosity models that they call purely dissipative and poorly
  correlated with the real subgrid stress; they do not test it.

- **Separated flow on the Gaussian bump.** [Zhou & Bae (2024)](/sources/zhou-2024-b.md)
  run Vreman with two constants in wall-modelled LES of the
  spanwise-periodic [Gaussian bump](/benchmarks/gaussian-bump.md),
  $Re_L=2\times10^6$, with the reference mean wall stress imposed: $c=0.07$,
  "derived theoretically for homogeneous isotropic turbulence", and
  $c=0.025$, "recommended for more complicated cases" (§2.1, as printed).
  - On the baseline isotropic mesh $c=0.025$ separates with a bubble
    "similar to the DNS" and gives the best $C_p$, while $c=0.07$ stays
    attached; $c=0.025$ gives the smallest mean eddy viscosity in the
    boundary layer of the eddy-viscosity models, and its subgrid
    dissipation is comparable to the viscous one (§3.1, Figs. 4–6, 11).
  - The separation length converges monotonically to the reference
    $L_s/L=0.32$ with $c=0.025$ and non-monotonically with $c=0.07$, on
    four isotropic meshes of 1.94 to 993 million cells (§3.1, Fig. 8).
  - The two constants respond differently to the wall boundary condition:
    for $c=0.07$ the three conditions agree, for $c=0.025$ the two
    eddy-viscosity conditions give a longer bubble; the authors conclude
    that the model "is sensitive to its constant" (§3.2, Figs. 15–16).
  - On cells of aspect ratio $4:1:2$ at the same volume, $c=0.025$
    degrades most: the separated boundary layer at $x/L=0.2$ becomes
    attached or nearly so. The authors attribute this to the cube-root
    filter width and call the model "comparatively robust" on isotropic
    meshes, with caution for anisotropic ones (§3.3, §4, Figs. 17–20; see
    the [anisotropic minimum-dissipation model](/methods/anisotropic-minimum-dissipation-model.md),
    which is insensitive there).
- **Grid-convergence study of wall-modelled LES.** [Hu et al. (2024)](/sources/hu-2024.md)
  (§4) close the subgrid stress and heat flux with the Vreman model in
  [CharLES](/software/charles.md) (second-order central finite volume,
  RK3) for their matching-height convergence study in channel and
  three-dimensional boundary layers; the constant is not printed, and the
  study varies the grid and the matching height, not the model (see
  [wall-modelled LES](/methods/wall-modelled-les.md)).
- **Rotating detonation engine.** [Vignat et al. (2024)](/sources/vignat-2024.md)
  (§3.3) use Vreman with $C=0.07$ and turbulent Prandtl and Schmidt
  numbers of 0.7 in the LES of the AFRL rotating detonation rocket engine
  (54 million cells, 50–100 μm in the detonation region) in a
  compressible unstructured finite-volume code that their Table 1 calls
  CharlesX (see [CharLES](/software/charles.md)); earlier LES of the same engine used one-equation,
  dynamic Smagorinsky or no subgrid closure. The authors state that the
  adequacy of subgrid models for highly compressible, turbulent, reacting
  flows is open, and they do not vary the model (§3.3, §3.8).
- **Wall-modelled LES with flux reconstruction.** [Gao et al. (2025b)](/sources/gao-2025-b.md)
  (§II B, Eqs. 11–16) close the compressible FR/CPR wall-modelled LES of
  channels at $Re_\tau=2000$, 5200 and 10 000 and of the
  [periodic hill](/benchmarks/periodic-hill.md) with the Vreman model in
  the index order of Kim et al. ($\alpha_{ij}=\partial_i\bar u_j$,
  $\beta_{ij}=\Delta_m^2\alpha_{mi}\alpha_{mj}$), $c_v=0.07$ ($c_v$
  page-local) and the filter width "simplif[ied]" to an isotropic one,
  whose definition on an FR element is not stated. They print the stress
  as $2\mu_t S_{ij}$, the opposite-sign convention, without a trace term.
  The subgrid model is not varied; the paper's subject is the wall-model
  input point and a hybrid inviscid wall flux (see
  [wall-modelled LES](/methods/wall-modelled-les.md) and
  [flux reconstruction](/methods/flux-reconstruction.md)); the
  filter-width study of Duan & Wang is below.
- **Aeroacoustic finite-difference WMLES.** [Gao et al. (2025)](/sources/gao-2025.md)
  (§II.A) use the model in a high-order computational-aeroacoustics
  finite-difference solver with a [slip-wall model](/methods/slip-wall-model.md),
  stating that it improves on the Smagorinsky model "by
  significantly reducing numerical dissipation and providing improved
  accuracy for inhomogeneous turbulent flows" and "achieves an accuracy
  comparable to that of the Dynamic Smagorinsky model, while avoiding the
  need for computationally intensive spatial averaging and filtering
  procedures"; these are stated with a citation of Vreman (2004), not
  tested in the paper, and the constant is not printed.
- **Named, not run, in a GPU channel solver.** [Xiao et al. (2025)](/sources/xiao-2025.md)
  do not implement the model in [CaLES](/software/cales.md): they name it
  as one the solver "can easily incorporate" (§5), and cite Vreman's
  paper for the over-estimated peak of the streamwise normal stress that
  their own wall-resolved channel LES with the static and dynamic
  [Smagorinsky](/methods/smagorinsky-model.md) models also show at
  $Re_\tau\approx544$ (§4.2, Fig. 8).

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
- **Results in NUMA ($N=4$, filter width printed as $\min(\Delta x,\Delta y,\Delta z)/(N+1)$; see the [residual-based dynamic model](/methods/residual-based-dynamic-sgs-model.md) for the grid spacings).**
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
(§6), from profiles compared with DNS (Figs. 9–15); the paper tabulates no
error norm. The runs use their element-averaged viscosity and zero
interface subgrid flux (§3).

## Fluctuating viscosity and the mean stress

[Haering et al. (2022)](/sources/haering-2022.md) (§V D) list Vreman with
Smagorinsky and WALE as fluctuating-viscosity models: used as the
energy-transfer part of their model-split hybrid, their correlation with
the strain gives a contribution to the mean stress that would have to be
computed and subtracted from the mean-stress model.

## Qualifications

- Blind et al. (2023, §2.3) state that the test-level eddy viscosity is "a
  factor of $[(P+1)/(M+1)]^{2/3}\approx1.59$ larger"; with the printed
  $P=5$ (the registry's $N$) and $M=3$ (here $N_f$) the printed formula
  gives $(6/4)^{2/3}\approx1.31$, not 1.59 *(compiler check, not in the
  sources)*. The Source page records the version read (arXiv
  2301.03199v1).
- The constants in the table belong to different flows, filter-width
  definitions and codes; none of the sources calibrates the constant.
- Zhou & Bae (2024) and Vignat et al. (2024) print the constant but not
  the formula, so whether their $c$ or $C$ is the prefactor $2.5C_s^2$ of
  the table is not stated; Vignat et al.'s "as specified in the original
  paper" and Zhou & Bae's "derived theoretically" for 0.07 match the
  prefactor $c=0.07$ that Zhao et al. (2021) attribute to Vreman (2004)
  *(compiler check, not in the sources)*.

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
- [Caban et al. (2026)](/sources/caban-2026.md) — §2, Eq. (7); §5.3.1, Figs. 18, 20, 22, Table 4.
- [Zhao et al. (2021)](/sources/zhao-2021-c.md) — §III.B, Eq. (17); §IV; §V, Tables III, V–VII.
- [Lv et al. (2021)](/sources/lv-2021.md) — §III A, Eqs. (13)–(15).
- [Qi et al. (2022)](/sources/qi-2022-b.md) — §1.
- [Cao et al. (2022b)](/sources/cao-2022-c.md) — §III, Eqs. (10)–(11); §IV A, §IV C, Figs. 2–3, 8, Table II; App. B.
- [Hausmann et al. (2022)](/sources/hausmann-2022.md) — §III A–B, Eqs. (42)–(45); §IV B, Figs. 6, 12a.
- [Kiris et al. (2023)](/sources/kiris-2023.md) — §II.4, Table 2.
- [Xu et al. (2023)](/sources/xu-2023.md) — §2.2, Eqs. (2.15)–(2.31), Figs. 1–3; §4.1, Figs. 13–20, Table 4.
- [Zhou & Bae (2024)](/sources/zhou-2024-b.md) — §2.1; §3.1, Figs. 4–6, 8, 11; §3.2, Figs. 15–16; §3.3, Figs. 17–20; §4.
- [Hu et al. (2024)](/sources/hu-2024.md) — §4.
- [Vignat et al. (2024)](/sources/vignat-2024.md) — §3.3, Table 1; §3.8.
- [Xiao et al. (2025)](/sources/xiao-2025.md) — §4.2, Fig. 8 (streamwise-stress peak over-estimate, Vreman cited); §5 (model named for future inclusion). Not run.
- [Gao et al. (2025b)](/sources/gao-2025-b.md) — §II B, Eqs. (11)–(16) (form, $c_v=0.07$, isotropic filter width).
- [Gao et al. (2025)](/sources/gao-2025.md) — §II.A (model choice and stated advantages; constant not printed).
- [Wang et al. (2026)](/sources/wang-2026.md) — §II B, Eqs. (14)–(15); §III B, Figs. 3, 6; §IV B, Tables I–II.

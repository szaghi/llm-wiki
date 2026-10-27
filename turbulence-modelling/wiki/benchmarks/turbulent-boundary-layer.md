---
type: Benchmark
title: "Turbulent boundary layers: zero and adverse pressure gradient, compressible"
description: "Spatially developing turbulent boundary layers on flat walls: zero- and adverse-pressure-gradient layers test wall models, RANS wall functions, high-order RANS discretizations, hybrid RANS/LES shielding, the log law, physics-informed networks and data-driven corrections; supersonic and hypersonic layers are DNS databases for compressibility transformations, LES validation and algebraic RANS, and feed shock interactions."
status: established
aliases: [TBL, flat-plate boundary layer, ZPG boundary layer, APG boundary layer, Wieghardt flat plate, Samuel–Joubert boundary layer, DLR/UniBw APG boundary layer, compressible turbulent boundary layer, hypersonic boundary layer, shock/boundary-layer interaction, STBLI]
tags: [benchmark, boundary-layer, compressible, hypersonic, dns, wmles, data-driven, rans, dg, flux-reconstruction, des, lattice-boltzmann]
timestamp: 2026-10-27T06:07:00Z
---

# Turbulent boundary layers: zero and adverse pressure gradient, compressible

A turbulent boundary layer grows along a wall under a free stream of
velocity $U_\infty$; $x$ is streamwise, $y$ wall-normal, $z$ spanwise. Unlike
the [channel](/benchmarks/turbulent-channel-flow.md) it is not homogeneous in
$x$: its thickness $\delta$ (the 99% thickness unless a page says
otherwise), displacement and momentum thickness $\delta^*$, $\theta$, and
$Re_\tau$ grow downstream, an inflow condition must supply turbulence, and
the outer layer meets a non-turbulent free stream. The pressure gradient
along the wall classifies it: zero (ZPG), adverse (APG, decelerating) or
favourable. At high Mach number the wall temperature becomes a parameter,
measured by the ratio $T_w/T_r$ of wall to recovery temperature
$T_r=T_\infty(1+r\frac{\gamma-1}2M_\infty^2)$ (recovery factor $r=0.89$ in
both compressible sources). In this bundle the case serves as a
generalization test for wall models trained in channels, as the data base of
wall laws under pressure gradient, and as a DNS database for compressible
wall scalings.

## Zero-pressure-gradient layer as a wall-model test

[Bae & Koumoutsakos (2022)](/sources/bae-2022.md) (preprint v1, Methods p.
14, Fig. 5) apply a log-law-based
[reinforcement-learning wall model](/methods/machine-learning-wall-model.md),
trained only in channel flow, to a flat-plate ZPG layer at
$Re_\theta=1000$–7000 without retraining. The WMLES domain is
$3570\theta_0\times100\theta_0\times200\theta_0$ ($\theta_0$ the inlet
momentum thickness) with recycling of the inflow at $890\theta_0$ (Lund et
al.), a top condition from the experimental displacement-thickness growth, a
convective outlet, and spanwise periodicity; at $Re_\theta=6500$ the spacing
is $\Delta x^+=128$, $\Delta z^+=105$, $\Delta y^+=64$, with about 10 points
per $\delta$ at the inlet and the matching height at the third point. The
predicted skin friction $C_f(Re_\theta)$ is comparable to the empirical
correlation of Schlichting & Kestin.

[Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md), §4.2–4.3,
Figs. 8–9, test their
[building-block-flow wall model](/methods/building-block-flow-wall-model.md)
against the algebraic [equilibrium wall model](/methods/equilibrium-wall-model.md)
on two flat-plate layers in CharLES, with the dynamic Smagorinsky or the
Vreman SGS model. The ZPG layer spans $Re_\theta=800$–2000 in a box of
$1060\times18\times35$ average momentum thicknesses, with Lund–Wu–Squires
recycling at $890\theta_i$ (the recycling distance of Bae & Koumoutsakos above), a top
condition from the displacement-thickness growth, a uniform grid from
$\Delta\approx\delta/5$ at the inlet to $\delta/20$ at the outlet, and the
DNS of Towne et al. on the same set-up as reference. Mean profiles deviate
about 10–30% from DNS; the averaged wall-stress error of the wall model
alone (its "internal" error, isolated by forcing the LES mean to the DNS) is
below 0.5% for the learned model and about 2% for the equilibrium model,
while the total error is 5–15% for both, dominated by the SGS model at the
matching point. The model classifies the flow as ZPG with almost 100%
confidence except near the inlet. A laminar Blasius layer
($Re_x=10^4$–$10^6$) is also run: all combinations give the mean velocity
within 5%, the learned model's internal error falls below 1% against more
than 20% for the equilibrium model, and the equilibrium runs benefit from
cancellation of internal and external errors.

[Mukha et al. (2025)](/sources/mukha-2025.md) (read in arXiv v1), §IV,
run wall-modelled LES of a ZPG layer in the
[continuous-Galerkin spectral-element](/methods/spectral-element-method.md)
code [Nek5000](/software/nek5000.md) ($N=7$), with the
[Vreman model](/methods/vreman-model.md) and the
[equilibrium wall model](/methods/equilibrium-wall-model.md) in the form of
Spalding's law imposed as a weak Neumann condition on the wall-parallel
velocity, matching height $h_{\mathrm{wm}}=0.2\delta_{99}(x)$ and a time
average of the input over 10 time steps. The domain is
$450\times20\times27.395$ inlet thicknesses $\delta_{99}$, with SIMSON
inflow at $Re_\theta=790$; $\delta_{99}$ grows about eightfold and results
reach $Re_\theta\approx6000$. Three meshes of $519\times15$ elements in $x$
and $y$ and 28, 56, 112 spanwise (1, 2, 4 elements per inlet $\delta_{99}$;
75, 149, 299 million nodes) cover the layer with about 4 elements in $x$
and $y$, since a structured mesh cannot follow the growth in $z$ (Table V,
Fig. 12):

- the shape factor agrees with the references after the inflow adapts, with
  no clear gain from refinement (Fig. 13);
- the outer-scaled mean velocity is slightly over-predicted and improves
  with spanwise refinement, the finest mesh being "virtually
  indistinguishable" from the references at $Re_\theta=4000$ (Fig. 14);
  the authors note that a dependence on $\Delta z^+$ "would violate" the
  premise that WMLES is independent of inner-scale resolution;
- Reynolds stresses are more accurate than in their channel runs (Fig. 15),
  and $C_f$ from the modelled wall stress is within 2% of the wall-resolved
  LES of Eitel-Amor et al. on the finest mesh (Fig. 16).

They place the results "on par with the state of the art, possibly
outperforming it" for $\langle u'u'\rangle$, recalling the 10–30% velocity
and 5–15% wall-stress deviations of Lozano-Durán & Bae (above) on coarser
meshes and an OpenFOAM WMLES with about 2 cells per $\delta_{99}$ (§IV.B).
A priori, Spalding's law with $\kappa=0.41$ and the classical intercept
gives a wall-stress error of about ±1% with reference input, an order of
magnitude more than with the constants tuned for their channel; it reaches
its logarithmic limit near $y^+=150$, close to the wake at low Reynolds
number (App. A, Figs. 20–21). The channel runs are on
[turbulent channel flow](/benchmarks/turbulent-channel-flow.md).

## Turbulent flat plate in RANS

[Zhao et al. (2023b)](/sources/zhao-2023-b.md), §5.1, Fig. 5-2, run a ZPG
flat plate at Mach 0.2 and $Re_L=1.12\times10^7$ on the plate length,
first cell at $y^+=1$, with the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md)
discretized by first-order finite volumes under an interior-penalty DG mean
flow. The velocity profile agrees with the reference of Georgiadis et al.
in the log layer and the turbulent kinetic energy with that of Yoder &
Georgiadis; grid size and polynomial degree are not printed.

**High-order RANS of the $k$-$\omega$ family.**
[Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md), §5.3 and §6,
run the NASA TMR plate at $Re_L=10^7$ with a hybridizable DG discretization
of degree $N=3$ and four [$k$-$\omega$ models](/methods/k-omega-model.md)
(Wilcox 1998, Kok's TNT, BSL and [SST](/methods/k-omega-sst-model.md)),
with $y^+<3$ at the wall and $x^+<3$ at the leading edge:

- With TNT and inlet $\nu_t/\nu=0.1$, the velocity profile at
  $Re_\theta=10{,}000$ lies very close to Coles' law, and $C_f$ is about 2%
  above an SST finite-volume solution, which the authors attribute to the
  leading-edge singularity and the lower dissipation of the finer HDG
  leading-edge mesh (Figs. 18–20).
- $k$ and $\omega$ oscillate at the boundary-layer edge; BSL and SST are
  less robust than TNT and Wilcox 1998 at low inlet eddy viscosity, and an
  inlet ratio of 100 is "one of the simplest remedies", at the price of an
  over-estimated $C_f$ (SST: 1.6% above the reference). Wilcox 1998 is the
  most sensitive to the inlet condition (Figs. 21–27).
- On four grids ($228\times72$ to $380\times120$ elements) the observed
  order of $C_f$ is 1.84 computed from the velocity gradient and 3.33
  from the HDG auxiliary strain variable, with extrapolated values
  $2.919602\times10^{-3}$ and $2.918802\times10^{-3}$ (Table 4).
- Against 26 grids of the finite-volume code ReFRESCO, the HDG solution
  gives the same extrapolated drag and a "significantly smaller" numerical
  error at equal degrees of freedom, for integral, surface and local
  quantities (§6, Figs. 37–45).

**Wall functions on a high-order discretization.**
[Ghidoni et al. (2026)](/sources/ghidoni-2026.md), §4.1, run the
Wieghardt–Tillmann plate ($Re_L=11.1\times10^6$, $M_\infty=0.096$; the
same experiment as Wu et al. below) with an explicit
[RANS wall function](/methods/rans-wall-function.md) for the Wilcox
$k$-$\omega$ model on a modal DG discretization, $N=1$ to 6, on meshes
whose first element has height $y_1^+=1$ to 320, obtained by removing
wall layers from the wall-resolved mesh. $C_f$ agrees with the reference
for all $y_1^+$ and degrees (Figs. 2–4). Relative $C_f$ errors at
$x/L=0.923$ against the wall-resolved $N=6$ run (Table 1) are below 1%
from $N=3$ up to $y_1^+=10$; at $y_1^+=20$ they are non-monotone in $N$
(0.04% at $N=2$, 5.5% at $N=6$), because the feeding points of the wall
function fall in the buffer layer where the wall law blends its viscous
and power-law branches. The computing time falls with $y_1^+$, on average
over the degrees by 29.8%, 34.1%, 45.9%, 59.5% and 69.0% at $y_1^+=20$, 40,
80, 160 and 320; at 320 the implicit Spalding law saves 63.7% (Table 2).

**Spalart–Allmaras on the NASA TMR plate at high order.** Two sources
run the TMR plate at $Re=5\times10^6$ (reference length not printed) and
$M=0.2$ with the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md)
and compare with the finite-volume TMR solutions on the $545\times385$
grid:

- [Huang et al. (2022b)](/sources/huang-2022-d.md), §3.1, Figs. 20–23, on
  $137\times97$ quadrilaterals with first cell $5\times10^{-6}$
  ($y^+\approx0.5$–1): the fourth-order variational-reconstruction finite
  volumes match the CFL3D skin friction "very well", the second-order
  scheme differs slightly and under-predicts the log-region velocity, and
  the fourth-order scheme gives a higher peak eddy viscosity; both reach
  density increments of about $10^{-10}$.
- [Lodares et al. (2022)](/sources/lodares-2022.md), §7.3, Figs. 7–8, on
  the coarsest TMR mesh (816 elements) with the entropy-stable split-form
  [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) at
  $N=4$, 7 and 10 (residual histories to $N=10$): $C_f$, the eddy-viscosity
  profile and the [law of the wall](/definitions/law-of-the-wall.md) at
  $x=0.97008$ agree with FUN3D.

Huang et al. also reconstruct a manufactured composite wall-law profile
on meshes of aspect ratio $5\times10^2$ and about $10^3$ to choose the
weights of their reconstruction (§2.4.3, Table 3); see
[boundary-layer-conforming grids](/methods/boundary-layer-conforming-grid.md).

**$k$-$\omega$ SST and $k$-$\sqrt kL$ in high-order discretizations.**
[Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md), §4.1, verify
their [$k$-$\omega$ SST](/methods/k-omega-sst-model.md) model with
$\ln\omega$ as transported variable in
[flux reconstruction](/methods/flux-reconstruction.md) on the Wieghardt
plate, $Re_L=1.03\times10^7$, free-stream Mach raised to 0.2 for
convergence: mesh A has 784 quadrilaterals and first-element
$y_1^+\simeq10$ (degrees 0–4), mesh B 392 and $y_1^+\simeq25$ (degrees
5–6). The higher-degree velocity profiles at $Re_x=1.02\times10^7$
coincide and agree with experiment, Spalding's law and a degree-2 DG
reference on 8800 elements; the degree-4 $C_f$ lies considerably closer to
the experiment than lower degrees and the DG reference. On mesh B
discontinuities at degree 5 disappear at degree 6, and the degree-4
(mesh A), 5 and 6 (mesh B) solutions coincide, so the authors claim
accurate results at $y_1^+\simeq25$ without wall functions, a first-element
height larger than state-of-the-art second-order finite-volume solvers
tolerate without them (stated, not shown; Figs. 9–10).
[Ghidoni et al. (2026)](/sources/ghidoni-2026.md), above, reach coarser
first elements with a wall function instead.
[Jiang et al. (2025)](/sources/jiang-2025.md), §4.1, run the
$k$-$\sqrt kL$ model of [scale-adaptive simulation](/methods/scale-adaptive-simulation.md)
in a modal DG solver on an adiabatic plate at $M=0.3$, $Re=3\times10^6$
(on the 1 m plate length), on $45\times35$, $45\times75$ and $90\times120$
quadrilaterals (first-cell $y^+\approx1$, 0.6, 0.4) at degrees 1–3: the
velocity profiles agree in the viscous sublayer and log layer on the two
finer meshes and are almost identical across degrees; $C_f$ improves with
mesh and degree. For $x<0.1$ the finest mesh and the highest degree give a
later apparent transition, which the authors, following Rumsey as cited,
call numerical and not physical (Figs. 3–4). Their positivity treatment
of the length-scale variable and limiting of $k$ make the implicit solver
converge by 5–6 orders where it otherwise diverges (Fig. 1).

**Shielding of a hybrid RANS/LES on a fine Cartesian grid.**
[Husson et al. (2024)](/sources/husson-2024.md), §4.1, run the TMR plate
($Re_L=5\times10^6$, $M=0.2$, $T=300$ K, plate half-length $L=1$ m) on the isotropic octree
grid of a [lattice Boltzmann](/methods/lattice-boltzmann-method.md) solver
with a linearized Spalart–Allmaras wall law at an
[immersed boundary](/methods/immersed-boundary-method.md): six refinement
levels down to $1.6\times10^{-4}$ m, so that $\Delta y^+\approx30$ at
$x/L=1$ and the streamwise spacing is about $0.01\delta$ at mid-plate, far
below the $0.3\delta$ at and under which, as they cite, typical DES-type
methods give insufficient protection (§4.1.2). ZDES mode 2 (2020) reproduces RANS exactly ($C_f$, velocity
and eddy-viscosity profiles at $x/L=1$), also with $C_{DES}=0$ and on a
plate inclined to the grid, while DDES (2006) on the same grid suffers
severe modelled-stress depletion: the layer tends to laminarize while the
wall law still imposes a turbulent profile, and $C_f$ oscillates
"unexploitably" (Figs. 4–5). See
[detached-eddy simulation](/methods/detached-eddy-simulation.md) and
[hybrid RANS/LES](/definitions/hybrid-rans-les.md).

**Non-regression of data-driven corrections.** Two sources use the
incompressible ZPG plate to check that a RANS correction trained on
separated flows does not spoil an attached layer, the "L2" level of the
generalizability scale of [Wu et al. (2025)](/sources/wu-2025.md), Table 1.

- [Wu et al. (2025)](/sources/wu-2025.md), §4.5, run the plate at
  $Re_L=10^7$ on about $2\times10^5$ cells with $\Delta y^+\le0.05$
  (OpenFOAM simpleFoam) against the data of Wieghardt & Tillmann. SST and
  SR-CND, a [symbolic-regression](/methods/symbolic-regression-closure.md)
  correction of the SST $\omega$ destruction trained on
  [field inversion](/methods/field-inversion-machine-learning.md) gated by
  the DDES shielding function, both match the measured $C_f$ and the
  viscous and log layers; SR-CLS, trained by ungated inversion, gives a
  multiplier $\beta\approx1.06$ inside the layer, overestimates $C_f$ and
  gives a wrong log layer and a thicker layer (Figs. 47–48). The authors
  derive the cause: the log-layer calibration of the $\omega$ equation,
  written, citing Wilcox, as $\beta_\omega-\beta^*\gamma_\omega=\kappa^2\sqrt{\beta^*}\sigma_\omega$
  (page-local names $\beta_\omega$, $\gamma_\omega$ for the destruction and
  production coefficients of the $\omega$ equation), holds only if the
  multiplier equals 1 in the log layer (§2.1, Eqs. 3–4); see
  [law of the wall](/definitions/law-of-the-wall.md).
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md), §5.1.1, run the
  plate at $Re=5\times10^6$ per unit length on a $545\times385$ grid against
  Wieghardt's data and the Coles profile, with three expert models (SST, a
  separated-flow correction, a jet correction) and a learned
  [blend](/methods/turbulence-model-aggregation.md) of them (Table 9):

| Model | mean abs. error of $C_f$ | mean abs. error of $u^+$ |
|---|---|---|
| SST | $8.4\times10^{-5}$ | 0.42 |
| separated-flow expert | $3.7\times10^{-4}$ | 1.45 |
| jet expert | $1.1\times10^{-3}$ | 6.27 |
| blend | $1.7\times10^{-4}$ | 0.7 |

  The blend beats the two corrected experts but not SST. "Contrary to
  expectations", SST does not dominate the weights across the layer; the
  jet expert gains significant weight in the log region, which the authors
  read as weight shifts there having "little impact" on accuracy
  (Fig. 11c).

**Boundary layers on an airfoil.** The turbulent part of the
suction-side layer of the [Eppler 387 airfoil](/benchmarks/eppler-387-airfoil.md)
tests the near-wall numerical dissipation of a high-order implicit LES
([Lederer et al. (2026)](/sources/lederer-2026.md), §4.2): its mean
velocity in wall units, against $\kappa=0.41$ and an intercept of 5.2, is
over-predicted for $y^+>10$ on coarse meshes, less so with
projection-based upwinding (Figs. 7–10).

## Mean-flow reconstruction with physics-informed networks

[Eivazi et al. (2022)](/sources/eivazi-2022.md), §3, Table 1, Figs. 3–5, solve
the RANS equations of boundary layers with a
[physics-informed neural network](/methods/physics-informed-neural-network.md)
that outputs the mean velocity, pressure and Reynolds stresses, with no
turbulence model, from the RANS residuals and data on the domain boundaries.
On the ZPG layer of the DNS of Eitel-Amor et al. ($1000<Re_\theta<7000$;
continuity and streamwise momentum only) the relative $\ell_2$ errors are
1.02% for the streamwise velocity, 4.25% for the wall-normal velocity and
6.46% for $\langle u'v'\rangle$; on the APG layer of Bobke et al. at constant
Clauser parameter about 1 ($910<Re_\theta<3360$) they are 0.28% to 7.96%; on
the suction-side layer of a NACA4412 airfoil at $Re_c=200{,}000$ (LES of
Vinuesa et al., $0.5<x/c<1$) they are 1.56% to 11.36%. The authors report
agreement of shape factor, skin friction and inner-scaled profiles with the
references (Figs. 3–5). The method needs the reference Reynolds stresses on the boundaries.

## Adverse pressure gradient: the extent of the log law

[Knopp (2022)](/sources/knopp-2022.md) analyses wind-tunnel mean-velocity
profiles of 2D incompressible smooth-wall APG layers at $Re_\theta>8000$:
the 1968 Stanford collection (Bradshaw, Clauser, Ludwieg & Tillmann, Perry,
Schubauer & Klebanoff, Schubauer & Spangenberg), Samuel & Joubert, Skare &
Krogstad, Marusic & Perry, a UNH experiment and two DLR/UniBw experiments,
plus a low-Reynolds-number experiment (Nagano et al., $481\le Re_\tau\le639$)
and a DNS with a separation bubble (Coleman et al., $Re_\tau$ up to 880) for
validation (§3, Table 1). The local parameter is the pressure gradient in
inner units, $\Delta p_s^+=\nu\,(dP/ds)/(\rho u_\tau^3)$ (page-local, $s$
the wall-tangential direction). The log law is robust in APG, but its outer
edge moves down relative to $\delta$ as $\Delta p_s^+$ grows: below
$0.11\delta$ for $\Delta p_s^+>0.005$ and below $0.08\delta$ for
$\Delta p_s^+>0.015$, never reaching $0.15\delta$ except in the mild
equilibrium flows (§5.2). Above it the profile turns upward and follows a
half-power law. The calibrated correlation and the half-power slope are on
[the wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md).
Only a few experiments reach $\Delta p_s^+>0.02$, and few exceed
$Re_\theta=30{,}000$ (Fig. 2).

**A ZPG wall function in adverse pressure gradient.**
[Ghidoni et al. (2026)](/sources/ghidoni-2026.md), §4.2, run two of the
experiments of Knopp's collection with their power-law wall function
(Figs. 6–8). On the weak-APG layer of Samuel & Joubert
($Re_L=5.95\times10^6$, $M_\infty=0.07$, Clauser-type parameter 1.5 to 4.5,
the upper wall of the channel shaped to match the measured outer flow)
$C_f$ agrees for all $y_1^+$ and degrees, though every mesh needs one
degree more than on the ZPG plate. On the strong-APG DLR/UniBw layers DM2
and DM3 ($Re_L=3.4$ and $5.2\times10^7$, parameter 25 to 45) the agreement
deteriorates for $y_1^+>80$, and at $N=6$ the $C_f$ difference grows for
$y_1^+=160$ and 320 near the end of the APG region, $0.8<x/L<0.85$; the
authors attribute this to a wall law that holds only for ZPG layers,
consistent with the shrinking log layer above (see
[wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)).

## Supersonic and hypersonic layers on cooled walls (DNS)

| Case | Source | $M_\infty$ | $T_w/T_r$ | $Re_\tau$ range | Grid ($N_x\times N_y\times N_z$) |
|---|---|---|---|---|---|
| M2 low/high | [Cogo et al. (2022)](/sources/cogo-2022.md) | 2.00 | 0.76 | 340–620; 1240–2300 | $4096\times320\times512$; $16384\times832\times2048$ |
| M6 low/high | [Cogo et al. (2022)](/sources/cogo-2022.md) | 5.86 | 0.76 | 290–520; 1080–1953 | as M2 |
| M2p5HighRe | [Huang et al. (2022)](/sources/huang-2022.md) | 2.5 | 1.0 (adiabatic) | 395–1199 | three boxes, up to $5200\times680\times800$ |
| M5Tw091 | [Huang et al. (2022)](/sources/huang-2022.md) | 4.9 | 0.91 | 726–1244 | three boxes, up to $5000\times550\times600$ |
| M11Tw020 | [Huang et al. (2022)](/sources/huang-2022.md) | 10.9 | 0.20 | 672–1193 | three boxes, up to $6300\times690\times600$ |

The two databases join: the low-Reynolds-number Mach 5.86 case of Cogo et al.
matches case M6Tw076 of Zhang, Duan & Choudhari (2018), one of the five
earlier cases (Mach 2.5 to 14, $Re_\tau\le686$) that
[Huang et al. (2022)](/sources/huang-2022.md) reuse. Grid spacings are
$\Delta x^+\le7.9$, $\Delta z^+\le4.8$, $\Delta y^+_{\min}\le0.7$ with the
mean spacing below $4\eta$ ([Cogo et al. (2022)](/sources/cogo-2022.md),
Table 1) and $\Delta x^+\approx6.5$–7.8, $\Delta z^+\approx4.7$–6.6
([Huang et al. (2022)](/sources/huang-2022.md), Table 2; their grid counts
are reordered in the table above to $x\times y\times z$ with $y$
wall-normal). Cogo et al. use the GPU code STREAmS
(energy-preserving central schemes with WENO switched by a shock sensor);
Huang et al. a limiter-optimized seventh-order WENO scheme, or an
eighth-order split central scheme for the Mach 2.5 case. Wall temperature
alone does not fix the cooling effect: at equal $T_w/T_r=0.76$ the Mach 2
layers behave as more strongly cooled, which
[Cogo et al. (2022)](/sources/cogo-2022.md) relate to the lower Eckert
number (3.9 against 8.0; §3.1).

**LES of supersonic and hypersonic layers.**
[Helm & Martín (2022)](/sources/helm-2022.md), §III B, Tables I–II, compare
LES with a dynamic mixed subgrid model against DNS of the same group at three
Mach numbers (values at the rescaling plane; $T_w/T_r$ with recovery factor
0.9):

| Case | $M_e$ | $T_w/T_r$ | $Re_\theta$ (DNS / LES) | $Re_\tau$ (DNS / LES) | Points (DNS / LES) |
|---|---|---|---|---|---|
| Mach 3 (narrow box) | 2.9 | 1.1 | 2809 / 3030 | 336 / 359 | 7.3M / 0.5M |
| Mach 7 | 7.2 | 0.52 | 3342 / 3254 | 202 / 197 | 96.7M / 3.0M |
| Mach 10 (nitrogen) | 9.0 | 0.33 | 7486 / 8038 | 495 / 503 | 361.3M / 14.8M |

The LES mean velocity and temperature are within 3% of the DNS (5% at
Mach 10), van Driest-transformed profiles within 3%, and the peak turbulent
kinetic energy within 2% of the top-hat filtered DNS; the unresolved kinetic
energy is 14% to 25% at Mach 7 and 10% to 15% at Mach 3 and 10 (Figs. 2–5).
The inflow is generated by recycling–rescaling in an auxiliary box with a
long rescaling length; the authors attribute a slight log-law overshoot of
their Mach 3 DNS to the recycling forcing of its shorter rescaling length
(§II, §III B). Spectra of top-hat filtered DNS are essentially unaffected
below $f\delta/U_e\approx0.4$, which makes the filtered DNS an acceptable LES
reference (Fig. 6). These layers feed the
[shock–turbulent boundary layer interactions](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
of the same paper.

**Supersonic layer generated by blowing and suction.**
[Dang et al. (2022)](/sources/dang-2022.md), §5.1, §6.1, generate the
Mach 2.9 layer upstream of a compression ramp by blowing and suction on the
wall between 350 and 200 mm upstream of the corner, instead of recycling,
and validate the van Driest-transformed mean velocity against the DNS of
Martín et al. (Fig. 17); at the reference station 35 mm upstream of the
corner their wide-span DNS has $\Delta x^+=1.2$, $\Delta y^+=0.41$,
$\Delta z^+=1.2$.

**A Mach 2 layer for high-order implicit LES.**
[Gao et al. (2022)](/sources/gao-2022.md), §5.2, run the undisturbed
Mach 2 layer upstream of their impinging-shock interaction
($Re_{\theta_0}=1628$ at the inlet) as split-form DGSEM
[implicit LES](/definitions/implicit-les.md) at $N=6$ in
[FLEXI](/software/flexi.md), on the interaction mesh ($\Delta x^+=30$,
$\Delta y^+_{\min}=1.6$, $\Delta z^+=16$), with a reformulated
synthetic-eddy inflow and anisotropic linear forcing over
$5\delta_r$–$10\delta_r$ ([inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
At $11\delta_r$, one $\delta_r$ after the forcing zone, the van
Driest-transformed mean velocity and the density-scaled Reynolds stresses
agree with the DNS of Wenzel et al.
([compressible velocity transformations](/definitions/compressible-velocity-transformation.md),
[Morkovin's hypothesis](/definitions/morkovin-hypothesis.md)), and the
transformed skin friction approaches the DNS and the correlation
$C_{f,i}=0.024Re_{\theta,i}^{-0.25}$ quickly after the forcing zone
(Figs. 16–17). The run took about 46,173 CPU hours on 16,384 cores, at a
performance index 94% above the code's baseline, which the authors
attribute to load imbalance of the synthetic-eddy method, the forcing
(5–10%) and statistics collection.

**Transition on a supersonic plate.**
[Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md), §IV C, use the
spatially developing Mach 2.25 DNS of Pirozzoli et al. ($Tu_\infty=0.04\%$)
as transitional $C_f$ reference for their compressibility-corrected
[laminar kinetic energy model](/methods/laminar-kinetic-energy-transition-model.md):
$C_f$ error 10.91% and onset error 6.96%, against 39.70% and 32.40% without
the compressibility correction of the onset correlation and 64.42% and
46.78% without both corrections (Fig. 23).

**Inflow and domain length.** Both use recycling–rescaling inflow, at
$80\delta_{\mathrm{in}}$ from the inlet in Cogo et al. Huang et al. measure
the induction length, the distance after which the momentum-integral
relation $C_f=2\,d\theta/dx$ holds to 5%: it grows from $20\delta_i$ at Mach
2.5 to $80\delta_i$ at Mach 14 ($\delta_i$ the inflow thickness), is one to
three eddy-turnover lengths $U_\infty\delta_i/u_{\tau,i}$, and is 15 to
$20\delta_i$ longer with digital-filter than with recycling inflow; the outer
layer recovers more slowly than the near-wall region (§3.1, Table 3, Fig.
2).

**Compressible velocity transformations.** The two sources agree on the
ranking of [compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
at $Re_\tau$ up to about 2000 and 1200: the transformation of Volpiani et
al. and the total-stress transformation of Griffin, Fu & Moin collapse the
mean velocity onto the incompressible law through the viscous sublayer and
the log layer; van Driest and, more, Trettel–Larsson leave a scatter of the
log-law intercept in the hypersonic cases
([Cogo et al. (2022)](/sources/cogo-2022.md), §4, Fig. 8;
[Huang et al. (2022)](/sources/huang-2022.md), §4.1, Figs. 10–11). Huang et
al. rank the total-stress transformation best across the inner layer; Cogo
et al. find the two equivalent except in the wake and say their database
cannot decide between them. Both note that Trettel–Larsson collapses
cooled-wall channels, so the scatter is particular to boundary layers. For
the Mach 11 cold wall no clear log region appears up to $Re_\tau=1172$,
which Huang et al. attribute to reduced scale separation under strong
cooling (Fig. 11).

**Temperature–velocity relations and Reynolds analogies.** Both find the
generalized Reynolds analogy of Zhang et al. (2014) accurate: Walz's
relation stays within 3% at $T_w/T_r=0.76$
([Cogo et al. (2022)](/sources/cogo-2022.md), Fig. 9), and only the Zhang
et al. and Duan & Martin relations fit the Mach 11 cold wall
([Huang et al. (2022)](/sources/huang-2022.md), §4.3.1, Table 5). Huang et
al. also find the strong Reynolds analogy of Morkovin violated, with
velocity–temperature correlation about $-0.55$ for $y/\delta\gtrsim0.2$,
the modified analogy of Huang, Coleman & Bradshaw collapsing all cases, and
the Reynolds analogy factor $2C_h/C_f$ between 1.1 and 1.2 in the
hypersonic cold-wall cases (§3.2, §4.3.2).
See [Morkovin's hypothesis](/definitions/morkovin-hypothesis.md).

**Skin friction and shape factor.** [Huang et al. (2022)](/sources/huang-2022.md),
§3.2, Fig. 3, find that for $T_w/T_r\lesssim0.3$ the van Driest II
transformation over-predicts $C_f$ by up to 10–20% and Spalding–Chi
under-predicts it by 20–40%; van Driest II with the Smits et al. power law
is the best combination (within ±5% supersonic adiabatic, $-15\%$ to $-6\%$
hypersonic cold wall). The shape factor $\delta^*/\theta$ grows strongly
with Mach number and is best correlated by Hopkins et al. (§3.2, Fig. 5).

**Reynolds stresses and structure.** In Morkovin's density-weighted scaling
the Mach 2 stresses of [Cogo et al. (2022)](/sources/cogo-2022.md) agree
with incompressible DNS at matching $Re_\tau$, the streamwise peak rising with
Mach number, and the outer wall-normal and spanwise intensities fall at high
Mach and Reynolds number (§5.1). [Huang et al. (2022)](/sources/huang-2022.md)
find the peak locations collapse in semi-local units $y^*$, a logarithmic
decay of the normal stresses in the quasi-adiabatic cases (slope 1.03 and
intercept 2.39 for the streamwise one), and no such region for the Mach 11
cold wall (§4.2; see [attached-eddy hypothesis](/definitions/attached-eddy-hypothesis.md)).
Both find outer superstructures of length $O(10\delta)$ at all Mach numbers
([Cogo et al. (2022)](/sources/cogo-2022.md), §3.1;
[Huang et al. (2022)](/sources/huang-2022.md), §5). Strong cooling enlarges
near-wall streaks in wall units (semi-local spacing $\lambda_z^*\approx120$
at all Mach numbers) and removes the outer spectral peak and the outer
footprint on the wall stress (Huang et al., §5). At $T_w/T_r=0.76$ the
near-wall temperature streaks are hardly detectable at Mach 2 but strong at
Mach 6 (Cogo et al., §3.1, §5.4). Cogo et al. detect the
turbulent/non-turbulent interface with a density-weighted momentum defect
and find uniform momentum zones, 3.6 and 2.5 on average at Mach 2 and 6, and
for the first time uniform temperature zones, 5.9 and 4.9 (§3.2).

**Fluctuating wall quantities and budgets.** In
[Cogo et al. (2022)](/sources/cogo-2022.md) the pressure rms normalized by
$\tau_w$ is controlled by $Re_\tau$ and nearly independent of Mach number at
$T_w/T_r=0.76$ except very near the wall and in the free stream; the
semi-locally scaled dissipation is independent of Mach and Reynolds number
while production and transport keep a Mach dependence (§5.2–5.3). In
[Huang et al. (2022)](/sources/huang-2022.md) the wall-pressure rms over
$\tau_w$ is 2.6–2.8 for (nearly) adiabatic walls and about 3.6 and 4.5 for
the cold walls of Mach 6–8 and 11–14, and the wall shear-stress rms reaches
0.45–0.5 of its mean on cold walls (§3.2, Figs. 8–9). The two statements
concern different cooling levels.

**Algebraic RANS calibrated against the DNS databases.**
[Chen et al. (2024)](/sources/chen-2024.md) use twelve published DNS
datasets of zero-pressure-gradient layers (Mach 2 to 14, $T_w/T_r=0.18$
to 1.9, $Re_\tau$ from 100 to 1272, plus the incompressible layer of
Schlatter & Örlü), among them case M6Tw076R17 of Zhang, Duan & Choudhari
that the Mach 5.86 low-Reynolds-number case of
[Cogo et al. (2022)](/sources/cogo-2022.md) matches, to modify the
[Baldwin–Lomax model](/methods/baldwin-lomax-model.md). The paper calls this
model a "wall model", but it is an algebraic RANS eddy-viscosity closure
of the whole boundary layer, solved here by marching the boundary-layer
equations, not a wall-stress model for LES (§1, §2.2). Three established
relations replace the semilocal inner scaling of the baseline:

- the inner eddy viscosity of the baseline is shown to be equivalent to the
  Trettel–Larsson transformation inside a van Driest mixing length, and is
  replaced by the total-stress transformation of Griffin, Fu & Moin, whose
  semilocal eddy viscosity follows the incompressible curve into the log
  region for diabatic cases (§3.1, Fig. 3); see
  [compressible velocity transformations](/definitions/compressible-velocity-transformation.md);
- the outer eddy viscosity is rescaled with the van Driest defect scaling
  (§3.2);
- below $y^*=100$ the temperature follows the quadratic
  temperature–velocity relation of Duan & Martín and Zhang et al. instead of
  the energy equation with constant $Pr_t=0.9$, because the DNS turbulent
  Prandtl number is non-monotonic and singular near the temperature peak of
  cold-wall layers (§3.3, Fig. 6); see
  [Morkovin's hypothesis](/definitions/morkovin-hypothesis.md).

Mean relative errors over all cases fall from 1.2% to 0.7% (velocity, log
coordinate), 2.5% to 1.3% (velocity, outer coordinate), 1.4% to 0.4% and
8.8% to 3.4% (temperature) (§4, Fig. 13); for walls with
$T_w/T_r\le0.5$ modifying the eddy viscosity alone is insufficient, and
the temperature–velocity relation is required (§4, Fig. 11). Wall and
integral quantities (Table 2):

| Case | $C_f\times10^3$ DNS / baseline / modified | $\delta^*/\theta$ DNS / baseline / modified |
|---|---|---|
| M2p5Tw10R17 | 2.31 / 2.07 / 2.13 | 4.1 / 4.29 / 4.17 |
| M6Tw025R11 | 1.70 / 1.55 / 1.52 | 8.4 / 8.96 / 8.35 |
| M6Tw076R17 | 1.00 / 0.85 / 0.97 | 13.6 / 14.4 / 13.7 |
| M8Tw048R20 | 0.77 / 0.66 / 0.76 | 17.4 / 20.1 / 19.0 |
| M14Tw018R24 | 0.40 / 0.35 / 0.39 | 37.6 / 43.8 / 40.9 |

(The DNS $C_f$ is inferred by the authors from $\rho_w$ and $u_\tau$.) The
model choices coincide with DNS findings recorded above: the total-stress
transformation, which [Huang et al. (2022)](/sources/huang-2022.md) rank
best across the inner layer and [Cogo et al. (2022)](/sources/cogo-2022.md)
find equivalent to that of Volpiani et al., and the temperature–velocity
relation of Zhang et al., which both databases find accurate. The
modifications are restricted to attached thin layers; extension to pressure
gradients and separation is left open (§5.1).

## End-wall boundary layers built from a DNS template

[Morsbach et al. (2024)](/sources/morsbach-2024.md), §3.3, Eqs. (5)–(11),
Fig. 3, feed the turbulent end-wall boundary layers of a turbine-cascade LES
by scaling the $Re_\theta=670$ ZPG DNS of Schlatter & Örlü to the operating
point: the DNS velocity, Reynolds stresses and a length scale $k^{3/2}/\varepsilon$
in wall units are mapped to total pressure, Reynolds stress and length-scale
profiles that drive a synthetic turbulence generator (see
[inflow turbulence generation](/methods/inflow-turbulence-generation.md)). A
precursor LES of a finite-length channel with parallel end walls fixes the
inlet distance at which the layer meets the measured momentum-thickness
growth (a fit $\propto x^{4/5}$). At $x/C_{ax}=-0.99$ upstream of the blades
the shape factor $\delta^*/\theta$ is 1.447 in the cascade LES, 1.405 in the
precursor, 1.440 with SST and 1.396 with the SSG/LRR-$\omega$
Reynolds-stress model fed with the same profile.

## Shock/boundary-layer interaction

The interaction has its own page,
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md),
which also covers the compression ramps of Helm & Martín and Dang et al.
[Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) simulate a Mach 3
boundary layer ($\delta_0=4$ mm at the reference station, unit Reynolds
number $49.4\times10^6$ m$^{-1}$) hit by the oblique shock of a wedge that
rotates to 17.5°, over a rigid wall and over a flexible steel panel,
replicating the experiment of Daub et al. The
[wall-modelled LES](/methods/wall-modelled-les.md) uses the Vreman SGS model,
the equilibrium wall model of Kawai & Larsson matched at $0.1\delta_0$ with
four cells below it, digital-filter inflow, $\Delta x\approx0.08\delta_0$,
$\Delta z=0.05\delta_0$, about $2\times10^7$ cells for a $5\delta_0$
periodic span and $2\times10^8$ for the full span (§3). The full-span run
shows wall pressure and skin friction nearly two-dimensional (§4.1). Panel
flexibility moves separation about $3\delta_0$ upstream and lengthens the
separation from $7.8\delta_0$ to $12.6\delta_0$ (+60%), lowers the peak wall
pressure, shifts the dominant frequencies down, and lengthens the recovery
of the downstream boundary layer from $47\delta_0$ to $61\delta_0$ (§4.3).
At the separation shock the low-frequency band ($f\delta_0/U_\infty<0.05$)
carries about 70% of the wall-pressure power, against over 80% in the band
above 0.5 upstream (Fig. 10). The authors state that RANS cannot predict the
strong separation and low-frequency dynamics of such interactions and that
DNS and wall-resolved LES are too costly at the experimental Reynolds number
(§1).

## Qualifications

- Coordinate translation: [Huang et al. (2022)](/sources/huang-2022.md)
  write $y$ spanwise and $z$ wall-normal; this page uses $y$ wall-normal.
- Semi-local friction Reynolds number: [Cogo et al. (2022)](/sources/cogo-2022.md)
  evaluate it with free-stream properties, [Huang et al. (2022)](/sources/huang-2022.md)
  with boundary-layer-edge properties; the two agree where the edge state
  equals the free stream *(compiler check, not in the sources)*.
- The sources print the total-stress transformation in different but
  algebraically equivalent forms ([Cogo et al. (2022)](/sources/cogo-2022.md),
  Eq. 4.2, writes the mean shears as derivatives of transformed velocities;
  [Huang et al. (2022)](/sources/huang-2022.md), Eq. 4.4, with viscosity-ratio
  factors); the mapping is on
  [compressible velocity transformations](/definitions/compressible-velocity-transformation.md).
- [Cogo et al. (2022)](/sources/cogo-2022.md), Table 2, print for the low-Reynolds
  Mach 6 station $\delta^*/\delta=0.43$ and $\theta/\delta=3.2\times10^{-2}$
  with shape factor 10.9, while the ratio is 13.4; the other three rows
  agree with their printed shape factors within rounding *(compiler check,
  not in the sources)*.
- [Huang et al. (2022)](/sources/huang-2022.md) give $Re_\tau^*$ at the
  $Re_\tau=1172$ stations as 2626, 9178 and 6213 in §4.1 and 2761, 9114 and
  6149 in Table 4, and print "$Re_\tau=744$" in two figure legends for the
  774 station.
- [Helm & Martín (2022)](/sources/helm-2022.md) write $z$ wall-normal, use
  the edge density in $u_\tau=(\tau_w/\rho_e)^{1/2}$ and a recovery factor 0.9;
  the Mach 3 wall is slightly heated ($T_w/T_r=1.1$). For the unresolved
  energy at the wall of the Mach 7 layer §III B prints both 25% and "a
  maximum of 18%", and §V gives 12% (against about 14% in §III B) above
  $y/\delta=0.2$. Their §III B gives the
  rescaling lengths as "29δ compared to 7δ for the LES" while calling the DNS
  length "much shorter".
- [Eivazi et al. (2022)](/sources/eivazi-2022.md) were read in arXiv v1;
  their ZPG case uses only two of the three equations of their general loss.
- [Knopp (2022)](/sources/knopp-2022.md) analyses measured mean profiles
  only; no turbulence model is run on these layers.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) compare their skin
  friction with an empirical correlation, although the Reynolds-number range
  was chosen to match the DNS of Sillero et al.
- The wall-model errors of [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md)
  split into an internal part (the wall model given the exact mean input)
  and an external part (SGS error at the matching point); their equilibrium
  model takes its input at the second off-wall grid point (Eq. 3.1).
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) write $z$ for the
  wall-normal coordinate of the end-wall layer; their momentum-thickness
  data are given only as a fit, the absolute values being confidential.
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) place the reference
  station at $x=210$ mm in §2 and at $x=200$ mm in the Table 1 caption and
  later in §2. Their structural-damping coefficient is fitted to the measured
  panel displacement of the same experiment (§3).

- [Mukha et al. (2025)](/sources/mukha-2025.md) print the Spalding
  intercept for the boundary layer as $B=5.2$ in §IV.A and $B=5.5$ in
  App. A, so the value used in the simulations is not certain; their node
  counts are $N^3$ per element in Table V but $(N+1)^3$ in Table I
  *(compiler check, not in the sources)*. Their Fig. 20 caption says DNS
  input where the text uses the wall-resolved LES.
- [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) define their $C_f$
  error as an average over 1000 wall points (Eq. 20), while Table 1 is
  captioned "at $x/L=0.923$"; its printed $C_f$ values reproduce its
  errors as pointwise relative differences at that station (at
  $y_1^+=1$: $|2.479-2.431|/2.431=1.97\%$ for $N=1$, $0.41\%$ for $N=2$,
  $0.21\%$ for $N=3$) *(compiler check, not in the sources)*. Their text
  states errors "below 0.5%" at $y_1^+=1$ from $N=1$, where Table 1 prints
  1.970%, and "<3%" at $y_1^+=40$ from $N=3$, where it prints 3.833%
  (§4.1). Their Table 2 savings are not monotone in $N$ at fixed mesh,
  although the text says they increase with it.
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) compare
  $C_f(Re_\theta)$ with a "K-S correlation" whose reference entry [40] is
  titled as a paper on the Kolmogorov–Smirnov test, and their
  finite-volume reference ISIS-CFD with an entry [41] titled as a fire
  simulation code; the Table 4 caption prints "Re = ×10^7".
- [Wu et al. (2025)](/sources/wu-2025.md) give the $\beta$ distribution of
  Fig. 48 "at $Re_x=1.5\times10^6$" while the text says $x=0.3$; the plate
  length is not printed, so the two cannot be checked against each other.

- The Wieghardt plate is run at $Re_L=1.03\times10^7$ (Mach raised from
  0.096 to 0.2) by [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md)
  and at $Re_L=11.1\times10^6$, $M_\infty=0.096$ by
  [Ghidoni et al. (2026)](/sources/ghidoni-2026.md); neither comments on
  the other value, and the two are recorded side by side.
  Vandenhoeck et al. print the free-stream intensity as "$10^{-2}$" while
  defining $Tu$ in percent, so the unit of the value is ambiguous (§3.3.2,
  §4.1).
- [Huang et al. (2022b)](/sources/huang-2022-d.md) write the friction
  velocity of their manufactured profile in one equation as
  $\sqrt{\rho_0u_0^2C_f/\rho}=\sqrt{a\rho_0u_0^2x^b/2\rho}$, with the fit
  $C_f=ax^b$ (p. 19): the two printed forms differ by a factor $\tfrac12$
  under the root.
- [Husson et al. (2024)](/sources/husson-2024.md) show no profiles for the
  DDES run on the plate, only eddy-viscosity fields (Fig. 5).
- [Jiang et al. (2025)](/sources/jiang-2025.md) compare their plate with
  laws and correlations ("Turbulent theory", Blasius), not with a
  reference solution.

# Citations

- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Results pp. 6–8, Fig. 5; Methods p. 14 (preprint v1).
- [Knopp (2022)](/sources/knopp-2022.md) — §3, Table 1; §5.1–5.2, Figs. 2, 4, 7–9.
- [Cogo et al. (2022)](/sources/cogo-2022.md) — §2, Tables 1–3; §3.1–3.2; §4, Figs. 8–9; §5.1–5.4.
- [Huang et al. (2022)](/sources/huang-2022.md) — §2, Tables 1–4; §3.1–3.2, Figs. 2–9; §4.1–4.3, Figs. 10–18; §5, Figs. 20–26.
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) — §1–3, Tables 1–2; §4.1, §4.3, Figs. 4, 8–10.
- [Eivazi et al. (2022)](/sources/eivazi-2022.md) — §3, Table 1, Figs. 3–5.
- [Helm & Martín (2022)](/sources/helm-2022.md) — §II, Fig. 1; §III B, Tables I–II, Figs. 2–6.
- [Dang et al. (2022)](/sources/dang-2022.md) — §5.1, Fig. 17; §6.1.
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §4.1–4.3, Figs. 8–9.
- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §5.1, Fig. 5-2.
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §3.1, §3.3, Eqs. (5)–(12), Fig. 3.
- [Chen et al. (2024)](/sources/chen-2024.md) — §1; §2.1–2.3, Table 1; §3.1–3.3, Figs. 3–6; §4, Table 2, Figs. 7–13; §5.1; App. A–B.
- [Mukha et al. (2025)](/sources/mukha-2025.md) — arXiv v1: §IV.A–B, Table V, Figs. 12–17; App. A, Figs. 19–21.
- [Wu et al. (2025)](/sources/wu-2025.md) — author manuscript: §2.1, Eqs. 3–4; Table 1; §4.5, Figs. 47–48.
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — arXiv v2: §5.1.1, Table 9, Fig. 11.
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §5.3, Table 4, Figs. 18–27; §6, Figs. 37–45.
- [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) — §4.1, Eq. 20, Tables 1–2, Figs. 2–5; §4.2, Figs. 6–8.
- [Lederer et al. (2026)](/sources/lederer-2026.md) — arXiv v1: §4.2, Figs. 7–10.
- [Huang et al. (2022b)](/sources/huang-2022-d.md) — §2.4.3, Table 3; §3.1, Figs. 20–23.
- [Lodares et al. (2022)](/sources/lodares-2022.md) — §7.3, Figs. 7–8.
- [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md) — §3.3.2; §4.1, Figs. 8–10.
- [Jiang et al. (2025)](/sources/jiang-2025.md) — §4.1, Figs. 1–4.
- [Husson et al. (2024)](/sources/husson-2024.md) — §2.2; §4.1.1–4.1.2, Figs. 3–5.
- [Gao et al. (2022)](/sources/gao-2022.md) — §5.2, Eq. 19, Figs. 16–17.
- [Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md) — §IV C, Table VIII, Fig. 23.

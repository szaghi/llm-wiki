---
type: Benchmark
title: "NASA CRM high-lift configuration"
description: "The NASA High-Lift Common Research Model (CRM-HL), a half-span transport in landing configuration at Mach 0.2: at mean-chord Reynolds number about 5.5 million nine HLPW-4 codes test wall-modelled LES of maximum lift and stall, IDDES resolves its vortex system, a learned wall model and immersed-boundary RANS are tested, and its wing-body form tests DG mesh adaptation."
status: established
aliases: [CRM-HL, HL-CRM, NASA High-Lift Common Research Model, NASA CRM-HL, HLPW-4 CRM-HL, CRM-HL wing-body, HLPW-5 CRM-HL, HLPW-4 case 2]
tags: [benchmark, wmles, wall-model, rans, des, immersed-boundary, data-driven, mesh-adaptation, dg]
timestamp: 2026-10-28T07:04:00Z
---

# NASA CRM high-lift configuration

The NASA High-Lift Common Research Model (CRM-HL) is the half model of a
civil transport with deployed slats and flaps, a nacelle and pylon,
used as the test case of the Fourth AIAA High-Lift Prediction Workshop
(HLPW-4), and in a wing-body form without nacelle and pylon in the fifth
workshop (HLPW-5). The HLPW-4 sources run it at freestream Mach number
$M_\infty=0.20$ and $Re=5.49\times10^6$ based on the mean aerodynamic
chord ($5.5\times10^6$ as printed by
[Kiris et al. (2023)](/sources/kiris-2023.md)); the HLPW-5 source runs the wing-body at $M_\infty=0.2$ and
$Re=5.6\times10^6$ based on the root chord. The flow combines
thin leading-edge boundary layers on slats, main wing and flaps, wakes
merging over the flaps, and separation that spreads with incidence until
maximum lift. The quantities compared are the lift, drag and pitching-moment
coefficients $C_L$, $C_D$ and $C_M$ against incidence $\alpha$ (page-local:
angle of attack), and $C_p$ and $C_f$ on spanwise sections. In this bundle
it tests near-wall modelling at aircraft scale: a nine-code comparison of
[wall-modelled LES](/methods/wall-modelled-les.md) of maximum lift and
stall, a learned wall model in WMLES and a wall function at an
[immersed boundary](/methods/immersed-boundary-method.md) in RANS, and
[mesh adaptation](/methods/mesh-adaptation.md) for high-order
discontinuous Galerkin RANS. A
second high-lift workshop configuration is the
[JAXA Standard Model](/benchmarks/jaxa-standard-model.md).

## Configurations in the sources

| Item | [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md), §4.7 | [Constant et al. (2024)](/sources/constant-2024.md), §6.3 |
|---|---|---|
| Model | wall-modelled LES (CharLES), dynamic Smagorinsky SGS model, [building-block-flow wall model](/methods/building-block-flow-wall-model.md) against the algebraic [equilibrium wall model](/methods/equilibrium-wall-model.md) | steady RANS with the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md) and Musker's wall function at a ghost-cell immersed boundary |
| Set-up | semi-span in free air; free-slip symmetry plane, plug inflow, non-reflecting outlet | HLPW-4 nominal configuration (slat 30°/30°, flap 40°/37° inboard/outboard), half span 29.4 m, mean aerodynamic chord 7.005 m; viscosity modified to reach the Reynolds number |
| Incidence | $7^\circ$ and $19^\circ$ for the learned wall model | $17.05^\circ$, below maximum lift "to avoid massive separation" |
| Grid | 30 million points, 0 to 20 points per boundary-layer thickness | octree Cartesian, $h_{\min}=3.5$ mm on slats, flaps and pylon, $2h_{\min}$ on the rest of the wing and nacelle, $8h_{\min}$ on the fuselage, target $y^+=500$, $2.4\times10^9$ cells |
| Reference | wind-tunnel data corrected to free air | body-fitted RANS of the LAVA structured solver on grid D ($5.5\times10^8$ cells, target $y^+=0.75$) |

The wing-body case of [Schotte et al. (2026)](/sources/schotte-2026.md),
§4.4: HLPW-5 CRM-HL wing-body, $M_\infty=0.2$, $\alpha=11^\circ$,
$Re=5.6\times10^6$ on the root chord; steady RANS with the negative
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md); modal
discontinuous Galerkin of degree $N=1$ and 2 in the ONERA–DLR–Airbus
solver CODA, remeshed by the Tucanos library from an initial mesh of
244,561 cells; target complexities $3\times10^5$ to $2.4\times10^6$ at
$N=1$ and $1.2\times10^5$ to $4.8\times10^5$ at $N=2$ (Table 5);
references are the finite-volume solvers FUN3D, USM3D, CHAMPS and CODA FV
under uniform refinement.

## The HLPW-4 wall-modelled LES focus group

[Kiris et al. (2023)](/sources/kiris-2023.md) summarize the Wall-Modeled
LES and Lattice–Boltzmann Technology Focus Group of HLPW-4: nine
participants simulated the NASA 10%-scale semispan CRM-HL of the
experiment of Evans et al. in the QinetiQ 5 m low-speed wind tunnel
(Farnborough), at $Re=5.5\times10^6$ on the mean aerodynamic chord and
$M=0.2$ (§I). Workshop case 2a is the model in free air, compared with
loads corrected to free air at five angles of attack (7.05°, 11.29°,
17.05°, 19.57°, 21.47°); case 2b, run by three participants (W-020,
W-021, W-032), is the model inside the tunnel, compared with uncorrected
data, the reference Mach number held between 0.195 and 0.205 by the
tunnel back-pressure (§I, §V). All submissions used $y^+\gg1$ grids with a
wall model. Every participant but two used an
[equilibrium wall model](/methods/equilibrium-wall-model.md) with an
adiabatic wall; PowerFLOW used a proprietary pressure-aware
[nonequilibrium wall model](/methods/nonequilibrium-wall-model.md), and
W-030 an inviscid slip wall without viscous terms (§II.5, Fig. 2). The
paper prints no model equations or constants. The submissions (Tables 1–2;
$\Delta t$ non-dimensional, the exchange location in multiples of the
wall-normal spacing $h$, the source's $\Delta$):

| ID | Code | Discretization, time integration | SGS closure | Wall-model exchange | $\Delta t$ | Grid |
|---|---|---|---|---|---|---|
| W-020 | LAVA | 4th/2nd-order finite differences, structured overset, RK3 | [Vreman](/methods/vreman-model.md) | 2nd off-wall point | $3.3\times10^{-5}$ | 360 M |
| W-021 | [CharLES](/software/charles.md) | 2nd-order finite volume, Voronoi, RK3 | dynamic Smagorinsky ([dynamic procedure](/methods/dynamic-procedure.md)) | 1st off-wall point, $0.5h$ | $5.7\times10^{-5}$ | 362 M |
| W-030 | Real Flight Simulator | adaptive finite elements, implicit | none (Euler, [implicit LES](/definitions/implicit-les.md)) | not applicable | $2.1\times10^{-2}$ | 3 M |
| W-031 | BCFD | blended 2nd-order finite volume, BDF2 | Vreman | 4th off-wall cell, $3.5h$ | $5.8\times10^{-4}$ | 296 M |
| W-032 | PowerFLOW | [lattice Boltzmann](/methods/lattice-boltzmann-method.md), Cartesian, explicit | VLES ($k$-$\varepsilon$ based) | $0.5h$ | $3.7\times10^{-5}$ | 475 M |
| W-034 | Alya | 2nd-order finite elements, RK3 convection, Crank–Nicolson viscous terms | Vreman | 2nd (Voronoi) or 3rd (hexahedra) off-wall point | $2.9\times10^{-5}$ | 273 M |
| W-047 | [hpMusic](/software/hpmusic.md) | [flux reconstruction](/methods/flux-reconstruction.md) $N=2$, BDF2 | none (implicit LES) | interface of 1st and 2nd elements | $9.7\times10^{-5}$ | 13 M |
| W-049 | FFVHC-ACE | 2nd-order kinetic-energy- and entropy-preserving, Cartesian, RK3 | CSM | $3.5h$ | $3.6\times10^{-5}$ | 11.2 B |
| W-050 | FUN3D | 2nd-order finite volume, BDF2 | Vreman | 1st off-wall point, $1h$ | $5\times10^{-4}$ | 419 M |

PowerFLOW's closure is a RANS-based model switched to an LES-type closure
by an indicator function, a [hybrid RANS/LES](/definitions/hybrid-rans-les.md)
philosophy that the authors group with WMLES because of its $y^+\gg1$ grid
(§II.4). The Cartesian codes W-032 and W-049 use immersed boundaries
(§II). The wall-normal spacings at the 7 m full-scale mean aerodynamic
chord range from 0.8 mm (W-034 hexahedra) to about 10 mm (W-032) (Table 2).

**Loads.** Except for W-030 and W-031, the participants predict
$C_{L,\max}$ between 2.48 and 2.57; at $C_{L,\max}$ the pitching-moment
scatter is small, which the authors read as a correct prediction of the
flow topology, and it is large at the extreme angles 7° and 21.4° (§III,
Fig. 4). RANS submissions of the other focus groups that obtain
$C_{L,\max}$ "invariably predict far-too-high nose-up pitching moments",
which the authors read as error cancellation between inboard excess lift
and outboard loss of lift (§III, citing the LAVA comparison of their
ref. [5]). Scale-resolving simulations (WMLES and hybrid RANS/LES)
under-predict the suction peak on the outboard flap (stations E and F)
against steady RANS at 21.47°, which the authors take to explain the
excessive nose-up pitching moment of all WMLES above $\alpha=17^\circ$ in
free air; the cause is left open (§VI 1e, Fig. 37).

**Resolution.** The submissions are down-selected by three criteria:
best practice; $C_{L,\max}$ within 2% at 17.05° or 19.57°; and outboard
suction peaks (stations G and H, spanwise fractions 0.82 and 0.91) at
19.57° above the measured peaks at 17.05° (§IV, Figs. 4, 9, 12). Only
submissions with more than 250 M spatial degrees of freedom pass the
third criterion, and the authors conclude that this many are needed for
the outboard slat and main-element loading, and so for the pitching moment
above $\alpha=17^\circ$ (Abstract; §IV; §VI 1a). They attribute the
requirement to inviscid, curvature-induced acceleration, not to the wall
layer: W-021's refinement from 12 M to 362 M Voronoi cells converges
largely monotonically with that kinematic effect at leading order (§III,
Fig. 6). W-020's off-wall refinement from 275 M to 360 M improves the
chine vortex and delays the onset of corner-flow separation by more than
1.5° (§III, Fig. 7); its refinement toward about 1.2 B degrees of freedom
changes the outboard skin friction and wedge-shaped separations while the
static pressure changes little (§VI 1a). Anisotropic grids with finer
near-wall spacing (W-034) give more accurate outboard $C_p$ on coarser
grids than unit-aspect-ratio Voronoi grids with larger wall-normal
spacing (§III, Figs. 8, 16, 21), while W-020 shows the need to resolve
off-body vorticity above 19°, which favours isotropic grids; the
authors give no answer to the isotropic-versus-anisotropic question
(§VI 2). W-047, the high-order run with 13 M degrees of freedom, obtains
reasonably accurate integrated loads at $C_{L,\max}$ but no outboard
separation from the slat-bracket wakes (§VI 1a). Grid convergence is
judged on time-averaged static pressure only, because the convergence of
wall-bounded LES in mean velocity profiles is non-monotonic and
numerically induced transition shifts the virtual origins of the boundary
layers with the grid (§I.1a). Further grid requirements are on
[grid-point requirements](/results/les-grid-point-requirements.md).

**Stall topologies.** Among the submissions above 250 M, most of the
pitching-moment scatter at 21.47° comes from the predicted onset of
inboard stall, which falls into two surface-flow topologies (§IV,
Figs. 23–25): A, a corner separation growing from the wing–body
juncture, with a pitch break between 20.5° and 21.47° (or $21.47^\circ$
plus less than 0.3°); and B, a separation from the inboard side of the
wing–pylon juncture, with no pitch break near 21.47°. The two resemble the
two stall mechanisms that Evans et al. observed in the QinetiQ 5 m and
the Langley 14×22 tunnels; because both appear in free-air WMLES, the
authors doubt that the tunnel-floor boundary layer explains them and
propose separation at the nacelle lip instead (§IV). All WMLES
predict nacelle-lip separation above 17.05° near $C_{L,\max}$, absent in
the experiment; trip dots twice the experimental size (W-020) do not
remove it, and the authors attribute it to under-resolution combined with
a non-optimal cowl design (§IV; §VI 1d). WMLES does not show the excess
outboard separation of steady RANS, and most submissions predict
wedge-shaped outboard separations consistent with the oil flow (Abstract;
§IV; Fig. 33).

**In the tunnel.** No team reproduces the thick floor boundary layer
measured by the rake ahead of the model, despite artificial roughness and
tripping (§V, Fig. 27). W-021 predicts the pitch break between 18.9° and
19.9°, "in perfect agreement with the experiment", and all three teams
show wedge-shaped outboard separation and a massive wing-root separation
at 19.9° that RANS does not capture (§V, Figs. 27–33). With slip tunnel
walls (W-020) the onset of the pitch break is sensitive to the floor
boundary layer but the stalled state at 19.9° is largely invariant to it,
verified by W-020 and W-021 (§V.4, Figs. 35–36).

**Inviscid implicit LES rejected.** W-030 runs implicit LES at
$Re\to\infty$ with slip walls on 3 M adaptive degrees of freedom. The
authors reject it: the experiments show more than 5% lift sensitivity
between the lowest and highest two Reynolds numbers, skin-friction drag
is about 10% of the total drag at 7.05° (by RANS and WMLES), and the
corner separation is a viscous effect (§II). The participant "emphatically
argued the validity of its approach" (§II).

**Time step and cost.** The authors argue that explicit time stepping
suits near-unit-aspect-ratio grids for compressible solvers at
$M\ge0.2$, since the decorrelation time of inertial-range eddies scales as
$k^{-2/3}$ and the acoustic CFL limit as $k^{-1}$, with $k$ (page-local)
the Nyquist wavenumber of the grid (§II.3). A hybrid RANS/LES time-step
study they cite finds large errors in the wing-root separation at 21.47°
from the dissipation of the large time steps allowed by A-stable BDF2
(§VI 1c). Best-practice WMLES cost about 5–10 times a representative
steady RANS at this Reynolds number, W-021 and W-047 report a substantial
reduction of wall time on GPUs, and no cost scaling of WMLES with
Reynolds number exists for such a configuration (§VI 4; cost details
withheld).

## What the case tests

**A learned wall model on an aircraft it has not seen.**
[Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) deliberately
leave airfoils, wings and bumps out of the building blocks of their
[machine-learning wall model](/methods/machine-learning-wall-model.md), so
the CRM-HL is an out-of-sample test (§2.3, §4.7). The building-block model
gives moderate improvements over the equilibrium model, especially near
stall and most clearly in the pitching moment; the exception is $C_L$ at low
incidence, where the equilibrium model's better prediction is attributed to
error cancellation ("it has been reported", without citation) (§4.7,
Fig. 15). The model's confidence falls below 20% at the leading edges of
nacelle, slats and flaps, where the grid has no points across the boundary
layer, and in the separated regions at the wing tip and near the root
(Fig. 16; see [model-form uncertainty](/definitions/model-form-uncertainty.md)).
The authors find the external error of the SGS model, not the wall model,
the main limit of accuracy, and cite Ling et al. (2022), who extended
the building blocks to the SGS model, as having "greatly improved" $C_L$,
$C_D$ and $C_M$ on this configuration (§5(4), §6). The grid resolution, with 0 to 20
points per boundary-layer thickness, is recorded on
[grid-point requirements](/results/les-grid-point-requirements.md).

**Immersed-boundary RANS with a wall function.**
[Constant et al. (2024)](/sources/constant-2024.md) (read in the HAL
author manuscript) apply their modelling-height adaptation and their
higher-order reconstruction of the wall pressure, developed on the
[NACA 0012](/benchmarks/naca-0012-airfoil.md), to the CRM-HL (§6.3,
Table 9):

| Solution | $C_D$ | error | $C_L$ | error |
|---|---|---|---|---|
| IBM, single modelling height, zeroth-order wall pressure | 0.3767 | 9.1% | 2.2118 | 13% |
| IBM, adapted height, zeroth-order | 0.3783 | 9.5% | 2.2940 | 9.5% |
| IBM, adapted height, second-order | 0.3405 | 1.5% | 2.3205 | 8.4% |
| LAVA body-fitted (reference) | 0.3455 | — | 2.5341 | — |

The higher-order reconstruction "divides the error made on the drag
coefficient by six". Pre-processing of the Cartesian grid took under seven
hours in a massively parallel environment from the surface mesh alone,
which the authors set against weeks for a curvilinear grid of comparable
resolution and months to calibrate one for WMLES (§6.3, Table 8; stated,
without a breakdown). The run used "20×28" Intel Broadwell CPUs (as printed),
five runs of 15,000 iterations, the adaptation after the third (§6.3). The
$C_p$ and $C_f$ on sections D, E and F and the off-body vorticity are
compared in Figs. 37–39.

**Anisotropic mesh adaptation for high-order RANS.**
[Schotte et al. (2026)](/sources/schotte-2026.md) adapt the mesh with a
metric built from the Hessian of the Mach number, which sets the
orientations and anisotropy, scaled at $N\ge2$ by an isotropic DG
spectral error estimator that sets the element size (§3.2). On the
wing-body (§4.4, Figs. 18–22):

- all adapted DG strategies "clearly outperform FUN3D, CHAMPS and CODA FV
  solutions" in drag and lift at equal degrees of freedom; the $N=1$ drag
  is slightly less accurate, except at the finest complexity, and is
  equivalent to USM3D;
- at $N=2$ the scaling by the small-scale lifted estimator captures the
  wing-tip vortex better than the unscaled Hessian, a change of "+2 drag
  counts and +0.1 lift counts", and $N=2$ needs about $8\times10^6$ fewer
  degrees of freedom than $N=1$ for similar integrated values;
- the unscaled Mach Hessian "still performs well" at $N=2$, which the
  authors call "surprising", since the Hessian does not describe the
  interpolation error above second order;
- adaptation reaches a near-wall $y^+$ close to 1 at $N=1$, with
  anisotropic ratios up to $10^5$ near the wall (Fig. 22).

The authors present the case as the first published high-order DG
metric-based adaptation for "a full high-lift aircraft configuration"
(§1); the configuration run is the wing-body.

**Two-dimensional multi-element airfoils.** The three-element airfoils
that the sources run are separate configurations, not sections of the
CRM-HL; the 30P30N now has its own page,
[30P30N three-element high-lift airfoil](/benchmarks/30p30n-high-lift-airfoil.md),
which collects the results below with those of later sources. [Huang et al. (2022b)](/sources/huang-2022-d.md), §3.3, run the
30P-30N at $\alpha=16^\circ$, $Re=9\times10^6$, $M=0.2$ with steady
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) RANS on a hybrid
mesh of 53,870 cells (non-dimensional first-layer height $10^{-6}$,
growth 1.25): their
optimized fourth-order variational-reconstruction finite-volume scheme
predicts lift and drag closer to the DLR reference than the fourth-order
scheme with the earlier weights of Pan et al. that they cite, both beat the
second-order scheme (lower lift, higher drag), and its skin friction is
closer to a degree-4 DG solution of 1,119,530 degrees of freedom (the FV
grid has 4.8% of that), though all schemes miss some peaks (Figs. 33–34).
The fourth-order scheme carries the slat-wake eddy viscosity to the
outlet, where the second-order one dissipates it, which the authors link
to the better skin friction (Fig. 35); a WBAP limiter with a shock detector
stabilizes only the start-up iterations. The LEISA2 three-element airfoil
run in ZDES on a lattice Boltzmann solver is recorded on
[detached-eddy simulation](/methods/detached-eddy-simulation.md) and
[lattice Boltzmann method](/methods/lattice-boltzmann-method.md).
The 30P-30N conditions of Huang et al. are those that
[Wang et al. (2013)](/sources/wang-2013.md), §4.11, specify as case C3.1 of
the first High-Order CFD Workshop: two-dimensional RANS with the
Spalart–Allmaras or $k$-$\omega$ model, $M=0.2$, $\alpha=16^\circ$,
$Re=9\times10^6$, fully turbulent, reference chord 0.5588 m; no workshop
results are shown for it. [Bose & Park (2018)](/sources/bose-2018.md),
§4.3, cite the wall-modelled LES of the 30P/30N at $Re_c=9\times10^6$ with
an equilibrium wall model by Bodart et al. (2013): the lift polar is
"qualitatively similar" to the measurements and the maximal lift "well
captured", but the stall angle is about $23^\circ$ against about $21^\circ$
in the experiment, a discrepancy they attribute "potentially" to blockage
corrections of the data, limited spanwise domains or statistical
convergence; their Fig. 7b compares $C_p$ at $19^\circ$ without and with an
equilibrium wall model (Bodart & Larsson 2011) against the experiment.
The same review also cites a wall-modelled LES of the NASA Common
Research Model at $M=0.85$, $\alpha=4^\circ$, $Re_c=5\times10^6$ (Lehmkuhl
et al. 2016, algebraic Werner–Wengle wall-stress closure), which is not
the high-lift configuration of this page and is not a high-lift result.

**Mesh adaptation on a section of the CRM-HL wing.**
[Mani & Dorgan (2023)](/sources/mani-2023.md), §4.3, Figs. 8 and 10,
reproduce the study of Michal et al. (2021) on a two-dimensional cross
section of the CRM-HL wing over a range of angles of attack, with four
flow solvers, four mesh-mechanics methods and four error estimates
(GGNS, SANS with MOESS, SFE and Wolf, with Hessian-based, multiscale and
lift-output-based metrics). Carried to sufficient mesh convergence, all
adaptive methods give nearly the same lift coefficient at $8^\circ$,
"regardless of flow solver, mesh mechanics method, or error estimate",
but their convergence trajectories differ, and the output-error-based
methods reach a prescribed error on coarser meshes. The review reads this
as the case for adjoint-based adaptation in industry (see
[mesh adaptation](/methods/mesh-adaptation.md)). In §4.5.2 the same
review cites Goc et al. (2020, 2021, 2022), the last titled in its
reference list as a large-eddy simulation of the CRM-HL, together for a
wall-modelled LES that "predicted the abrupt lift break near the stall",
and shows only the JSM result (see
[JAXA Standard Model](/benchmarks/jaxa-standard-model.md)).

**IDDES of the vortex system at the landing incidence.**
[Li et al. (2024b)](/sources/li-2024-f.md) run Spalart–Allmaras-based
IDDES ([detached-eddy simulation](/methods/detached-eddy-simulation.md),
$C_w=0.15$) and steady SA-RANS in the HLPW-4 nominal landing configuration
(inboard flap 40°, outboard 37°) at $M_\infty=0.2$, $Re=5.49\times10^6$ and
$\alpha=7.05^\circ$, the highest-priority workshop case, with the in-house
cell-centred finite-volume solver HUNS3D (second-order Roe flux with
low-Mach preconditioning, dual time stepping) on level C of the
HLPW-4 "103-ANSA-Unstructured" grids, $276\times10^6$ cells for the half
model, first-layer $y^+\le1$, on 6000 MPI partitions (§II–III.C); the
time step and averaging window are not printed, and there is no grid
or time-step study. Against the QinetiQ data corrected for incidence:

| | $C_D$ | pressure part | friction part |
|---|---|---|---|
| experiment | 0.1868 | — | — |
| SA-RANS | 0.1867 | 0.1701 | 0.0165 |
| SA-IDDES | 0.1843 | 0.1691 | 0.0151 |

(§III.D.2). The mean $C_p$ of the two models is "basically consistent" with
the data on the spanwise sections, except that SA-RANS underestimates
$C_p$ on the flap leading edge at the inboard flap-bracket station
$\eta=0.33$, where it overpredicts the separation behind the bracket, and
IDDES deviates slightly more than RANS at $\eta=0.42$ (Fig. 5); the IDDES
friction patterns agree with the oil flow at the wing root and tip (Fig. 6).
They cite a smaller DDES than RANS drag also in Probst et al. (0.1793).
The authors compare three vortex identifications on the IDDES field
(§III.D.3, Eqs. 5–7, Fig. 7), the vorticity magnitude, the $Q$-criterion
$Q=\tfrac12(\Omega_{ij}\Omega_{ij}-S_{ij}S_{ij})$ (of Hunt et al., in their
norm notation) and the Rortex rotation strength of Liu et al., at
thresholds 0.05 to 10 made dimensionless by the free-stream sound speed
and the mean aerodynamic chord: vorticity and $Q$ are contaminated by
shear in the boundary layers, raising the $Q$ threshold removes weak
vortices with the contamination, and Rortex at 0.5 removes the shear
contamination while keeping weak vortices, so it is used for the rest.
With it, IDDES resolves a hairpin-like vortex "forest" on the rear half
of the inboard upper surface, grown from slat vortices stretched in the
slat gap, hairpins in slat-bracket wakes, the nacelle-strake vortex
persisting over almost the whole upper surface at this incidence (breaking
down at the wing leading edge at 19.57°, as they cite Probst et al.),
wing-tip and flap-tip vortices, a horseshoe vortex at the lower
wing–fuselage junction only, and Kelvin–Helmholtz wake vortices behind
the nacelle and flap trailing edges; SA-RANS captures only the strong tip
vortices (Figs. 8–14). They attribute the larger RANS flap separation to
the flap-bracket tip vortex, which in RANS persists without breakdown and
rolls up the flap flow (§III.D.3), and conclude that IDDES "basically
satisfies the engineering simulation requirements of aerodynamic load and
complex vortex system" for this case (§IV).

**Wall-model robustness.** [Nuca et al. (2025)](/sources/nuca-2025.md), §I,
cite CRM-HL wall-modelled LES among the complex applications that motivate
their explicit, iteration-free forms of the algebraic and ODE
[equilibrium wall models](/methods/equilibrium-wall-model.md), but do not
run the configuration.

**What the two HLPW-4 studies share.** Both locate the weak point at the leading
edges of the high-lift elements, where the boundary layers are thinnest
relative to the grid: the low confidence of the learned wall model there in
[Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md), and the
leading-edge wall-function error that the modelling-height adaptation
addresses in [Constant et al. (2024)](/sources/constant-2024.md).
[Kiris et al. (2023)](/sources/kiris-2023.md) also find the outboard
slat and main-element leading edges decisive, but trace the grid demand
there to inviscid curvature-induced acceleration, not to the wall layer
(§IV; §VI 1a). Lozano-Durán & Bae run CharLES, the code of W-021, on
30 million points against W-021's 12 M to 362 M; no source compares the
two runs.

## Qualifications

- The two studies differ in modelling level (WMLES against steady RANS),
  incidence ($7^\circ$ and $19^\circ$ against $17.05^\circ$) and reference
  (wind-tunnel data corrected to free air against a body-fitted RANS);
  neither compares its errors with the other's.
- The immersed-boundary errors of [Constant et al. (2024)](/sources/constant-2024.md)
  are relative to another RANS solution ($5.5\times10^8$ cells against
  their $2.4\times10^9$), not to experiment; their lift error stays at 8.4% after both corrections.
  Their Table 9 drag error of 9.1% for the first row is 9.0% by the table's
  own coefficients *(compiler check, not in the sources)*.
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) give their
  force comparison only in figures (Fig. 15); no coefficients are printed.
- The Reynolds numbers $5.49\times10^6$ (HLPW-4, on the mean aerodynamic
  chord) and $5.6\times10^6$ ([Schotte et al. (2026)](/sources/schotte-2026.md),
  HLPW-5 wing-body, on the root chord) refer to different reference
  lengths and different configurations of the same model; they are not
  competing values for one case. [Schotte et al. (2026)](/sources/schotte-2026.md)
  print no force coefficients for the case (Figs. 20–21 only) and compare
  with other RANS solutions, not with experiment.
- The 30P/30N and Common Research Model results of
  [Bose & Park (2018)](/sources/bose-2018.md) are cited from the works
  they review; the review prints no force coefficients for them.
- [Kiris et al. (2023)](/sources/kiris-2023.md) is the journal version
  of the focus-group summary presented as AIAA Paper 2022-3294; it
  prints $Re=5.5\times10^6$, the other HLPW-4 sources $5.49\times10^6$,
  for the same mean-chord Reynolds number. Its printed slips: W-032 is
  listed in both stall topologies in §IV and then placed in topology B;
  §II.3 counts six explicit and three implicit participants, while
  Table 1 shows five explicit (counting W-034, with implicit viscous
  terms) and four implicit (W-030, W-031, W-047, W-050) *(compiler check,
  not in the sources)*; the implicit time steps "only about 10× larger"
  (§VI 1c) are 9–20 times the explicit ones of Table 2 for W-031 and
  W-050 but 1.7–3.3 times for W-047 *(compiler check, not in the
  sources)*; W-020's finest grid is "1.2B" in the text and "1100M" in the
  Fig. 3 legend; the high angle is printed 21.4° and 21.47°, the in-tunnel
  angles 17.9°, 18.9°, 19.9° and 17.98°, 19.98°, 19.99°; and "spatial
  degrees of freedom", "grid cells" and "points" are used for the 250 M
  threshold interchangeably, though they differ for $N=2$ flux
  reconstruction and nodal finite elements.
- [Li et al. (2024b)](/sources/li-2024-f.md) write the turbulent stress
  as $\bar\rho\tilde R_{ij}=2\bar\rho\nu_t\tilde S^*_{ij}$ (their Eq. 2;
  $\tilde S^*$ the traceless strain) and subtract it from the laminar
  stress in the total stress; taken together the two printed signs make
  the eddy viscosity enter with the sign of a negative viscosity
  *(compiler check, not in the sources)*. They call the trailing-edge
  wake vortices a source of airframe noise "in the cruising stage" for a
  landing configuration, and the thresholds "dimensionalized" where they
  are made dimensionless. Their conclusion rests on one grid and one
  incidence below maximum lift. [Lv & Ekaterinaris (2023)](/sources/lv-2023.md),
  §4.2, cite a limiter-assisted flux-reconstruction implicit LES of a
  NASA CRM near stall by Wang & Rahmani in which "only 0.3% of elements
  have the limiter activated"; the review does not say which CRM
  configuration it is.
- The focus-group findings rest on the submitted data; the RANS and
  hybrid RANS/LES comparisons come from other focus groups and from the
  LAVA study that Kiris et al. cite (their ref. [5]).

# Citations

- [Kiris et al. (2023)](/sources/kiris-2023.md) — §I; §II.2–II.5, Tables 1–2, Fig. 2; §III, Figs. 4–8; §IV, Figs. 9, 12, 23–25, 33; §V, Figs. 27–36; §VI 1a–1e, 2, 4, Fig. 37.
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §2.3; §4.7, Figs. 14–16; §5(4); §6.
- [Constant et al. (2024)](/sources/constant-2024.md) — §6.3, Tables 7–9, Figs. 35–39; §7.
- [Schotte et al. (2026)](/sources/schotte-2026.md) — §1; §3.2; §4.4, Table 5, Figs. 18–22.
- [Huang et al. (2022b)](/sources/huang-2022-d.md) — §3.3, Figs. 33–35 (30P-30N, a separate configuration).
- [Nuca et al. (2025)](/sources/nuca-2025.md) — §I (cited application only).
- [Bose & Park (2018)](/sources/bose-2018.md) — §4.3, Fig. 7b (cited results: 30P/30N; the $M=0.85$ Common Research Model, not CRM-HL).
- [Wang et al. (2013)](/sources/wang-2013.md) — §4.11 (case C3.1; specification only).
- [Mani & Dorgan (2023)](/sources/mani-2023.md) — §4.3, Figs. 8, 10 (reproduced adaptation study of Michal et al. 2021 on a CRM-HL wing section); §4.5.2 (cited WMLES).
- [Li et al. (2024b)](/sources/li-2024-f.md) — §I; §II.A–B, Eqs. 1–4; §III.A–D, Table I, Figs. 4–14; §IV.
- [Lv & Ekaterinaris (2023)](/sources/lv-2023.md) — §4.2 (cited flux-reconstruction LES of a CRM; passing mention).

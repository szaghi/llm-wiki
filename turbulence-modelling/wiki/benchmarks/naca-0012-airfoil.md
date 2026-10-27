---
type: Benchmark
title: "NACA 0012 airfoil"
description: "The symmetric NACA 0012 airfoil: static RANS at chord Reynolds numbers of 1 to 6 million up to 45° and transonic, high-order workshop cases, pitching in dynamic stall and transonic hysteresis, and a rod–airfoil noise case: it validates high-order RANS discretizations, near-wall and immersed-boundary treatments, data-driven corrections, and LES and DDES of dynamic stall."
status: established
aliases: [NACA0012, NACA 0012, NACA-0012]
tags: [benchmark, rans, hybrid-rans-les, les, data-driven, immersed-boundary, dg, separated-flow, des, transition, aeroacoustics]
timestamp: 2026-10-27T11:00:00Z
---

# NACA 0012 airfoil

The NACA 0012 is a symmetric airfoil of 12% thickness. At low Mach number
and chord Reynolds numbers $Re_c$ of a few million its boundary layers are
attached at small incidence $\alpha$ (page-local: angle of attack), lift
grows linearly with $\alpha$, and near stall the suction peak and the thin
leading-edge boundary layer dominate the forces; at very high incidence the
flow separates massively from the leading edge. The quantities compared are
the lift and drag coefficients $C_L$ and $C_D$, the pressure coefficient
$C_p$ and the skin friction $C_f$ along the chord $c$. Reference data
recalled by the sources are the measurements of Ladson (forces and $C_p$) and
the compilation of McCroskey. In this bundle the static airfoil validates
discretizations and near-wall treatments of RANS and hybrid RANS/LES, and
is a non-regression test of data-driven RANS corrections: an attached flow
that a correction trained on separated flows must not spoil. The pitching
airfoil tests wall-resolved LES and its spanwise domain size in deep
[dynamic stall](/definitions/dynamic-stall.md), and DDES with transition
closures in the onset of dynamic stall under a constant-rate pitch-up.
The airfoil also defines inviscid and laminar order-of-accuracy cases of
the first High-Order CFD Workshop, a transonic pitching case for moving
immersed-boundary grids, and the downstream body of the rod–airfoil noise
configuration.

## Configurations in the sources

| Item | [Zhao et al. (2023b)](/sources/zhao-2023-b.md) | [Constant et al. (2024)](/sources/constant-2024.md) | [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) |
|---|---|---|---|
| Flow | $M=0.15$, $Re_c\approx6\times10^6$, $\alpha=0^\circ$, $10^\circ$; transonic $M=0.804$, $Re_c=4.09\times10^6$, $\alpha=0.05^\circ$ | $M=0.15$, $Re_c=6\times10^6$, $\alpha=0^\circ$ to $15^\circ$ | $Re_c=3\times10^6$, $\alpha=2^\circ$, $6^\circ$, $10^\circ$, $15^\circ$ and $45^\circ$; Mach number not stated |
| Model | [$k$-$\omega$ SST](/methods/k-omega-sst-model.md) RANS, wall-resolved | [Spalart–Allmaras](/methods/spalart-allmaras-model.md) RANS with Musker's wall function | SST RANS, SST-IDDES and SST-based [continuous eddy simulation](/methods/continuous-eddy-simulation.md) |
| Discretization | interior-penalty DG of degree $N=2$ for the mean flow, first-order finite volumes for SST | ghost-cell [immersed boundary](/methods/immersed-boundary-method.md) on octree Cartesian grids, second-order finite volumes (FastS) | [lattice Boltzmann](/methods/lattice-boltzmann-method.md) D3Q19 on octree Cartesian grids with immersed boundaries ([ProLB](/software/prolb.md)) |
| Grid | 5883 elements (grid independence on 6834, 8844, 10854); 8954 cells transonic | IBM6: $h_{\min}/c=10^{-4}$, target $y^+=100$, $3.8\times10^6$ cells; body-fitted wall-resolved reference with $h_{\min}/c=10^{-6}$, $y^+=1$, $8\times10^6$ cells | 7 refinement levels to $\Delta_{\min}\approx0.18\%c$; span equal to chord, periodic |
| Reference | Ladson ($C_p$), McCroskey (forces), ONERA data (transonic) | the body-fitted wall-resolved solution | Ladson (forces, $C_p$); for $45^\circ$ the data of Shur et al. as cited |

Data-driven RANS corrections ([Wu et al. (2025)](/sources/wu-2025.md),
§4.5; [Oulghelou et al. (2025)](/sources/oulghelou-2025.md), §5.1.3) and
deep dynamic stall ([Baldan & Guardone (2025)](/sources/baldan-2025.md)):

| Item | Wu et al. (2025) | Oulghelou et al. (2025) | Baldan & Guardone (2025) |
|---|---|---|---|
| Flow | $Re_c=6\times10^6$, $M\approx0.15$, $\alpha=0^\circ$ | $Re_c=6\times10^6$, chord 1 m, $\alpha=0^\circ$–$18^\circ$, NASA TMR set-up | pitching $\alpha(t)=10^\circ+15^\circ\sin(\varpi_{\mathrm p}t)$ ($\varpi_{\mathrm p}$ page-local: angular pitching frequency; the source's $\omega$), reduced frequency 0.1, $Re_c=1.35\times10^5$, $U_\infty=14$ m/s, incompressible |
| Model | $k$-$\omega$ SST and two symbolic-regression corrections of it (SR-CLS, SR-CND) | SST, two expert corrections and their learned blend | wall-resolved LES with the [WALE model](/methods/wale-model.md); 2D URANS and 3D SBES of the authors' earlier work |
| Discretization | OpenFOAM simpleFoam; C-grid of 640 surface, 120 wake and 136 wall-normal cells, $\Delta y^+\approx0.6$ | OpenFOAM (modified), $225\times65$ grid of the NASA TMR | ANSYS Fluent, second-order finite volume, SIMPLEC, rigidly rotating O-grid of $934\times334$ nodes, first cell $10^{-4}c$, far field $50c$ |
| Reference | SST itself (NASA TMR) for $C_f$ | Ladson; Gregory & O'Reilly; Abbott & von Doenhoff | experiment of Lee & Gerontakos (loads) |

High-order RANS discretizations of the $k$-$\omega$ family
([Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md), §5.4;
[Ghidoni et al. (2026)](/sources/ghidoni-2026.md), §4.4):

| Item | Elzaabalawy et al. (2023) | Ghidoni et al. (2026) |
|---|---|---|
| Flow | $Re_c=6\times10^6$, $\alpha=0^\circ$, steady incompressible; inlet eddy-viscosity ratio 6 | $Re_c=6\times10^6$, $M=0.15$, $-15^\circ\le\alpha\le15^\circ$, steady |
| Model | two-equation [$k$-$\omega$ models](/methods/k-omega-model.md) (the model of this case is not named in §5.4), wall-resolved | Wilcox $k$-$\omega$ (2006/2007 version) in log-$\omega$ form, with an explicit [wall function](/methods/rans-wall-function.md) |
| Discretization | hybridizable DG, degree $N=3$ triangles | modal DG, $N=1$ to 6 |
| Grid | first element at $y^+=2$, clustered at leading and trailing edges, $x^+<3$ at the trailing edge | hybrid meshes (hexahedra in the boundary layer, prisms outside), far field at $50c$; wall-resolved reference of 6535 elements with 200 on the airfoil; meshes with first-element height $y_1^+$ up to 320 |
| Reference | Ladson ($C_p$); NASA TMR SST ($C_f$) | the wall-resolved $N=6$ solution; FUN3D $k$-$\omega$ (NASA TMR); Ladson, Gregory & O'Reilly, Abbott & von Doenhoff |

High-order Spalart–Allmaras and $k$-$\tau$ discretizations
([Huang et al. (2022b)](/sources/huang-2022-d.md), §2.5, §3.2;
[Lodares et al. (2022)](/sources/lodares-2022.md), §7.4;
[Tomboulides et al. (2025)](/sources/tomboulides-2025.md), §3.4):

| Item | Huang et al. (2022b) | Lodares et al. (2022) | Tomboulides et al. (2025) |
|---|---|---|---|
| Flow | $Re_c=2.88\times10^6$, $M=0.15$, $\alpha=15^\circ$, steady | $Re_c=6\times10^6$, $M=0.15$, $\alpha=0^\circ$, $10^\circ$, $15^\circ$, steady | $Re_c=6\times10^6$, $M=0.15$ (Ladson), $\alpha=0^\circ$, $10^\circ$ |
| Model | standard [Spalart–Allmaras](/methods/spalart-allmaras-model.md) with the exponential-decay positivity treatment of $\tilde\nu$ | Spalart–Allmaras with a negative-$\tilde\nu$ variant and clipped diffusion coefficient | [$k$-$\tau$ model](/methods/k-tau-model.md) and the authors' regularized $k$-$\omega$ |
| Discretization | cell-centred finite volumes with compact variational reconstruction, second order (O2) and fourth order (O4), implicit LU-SGS | entropy-stable split-form [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) (Pirozzoli flux), $N=2$–6, implicit pseudo-transient solver | [spectral elements](/methods/spectral-element-method.md) in [Nek5000](/software/nek5000.md), $p=5$ and 7 |
| Grid | C-meshes of 11,880, 20,816 and 33,150 cells, first layer $5\times10^{-6}c$ (O2 also on 143,700 cells) | coarsest NASA TMR family-II grid ($113\times33$, 65 points on the airfoil) with quadratic edges | 5974 elements, average $y^+<1$ |
| Reference | Gregory & O'Reilly, $C_L=1.526$ | finite-volume solution of the NASA TMR on the $897\times257$ grid | Ladson (forces), Gregory & O'Reilly and Ladson ($C_p$), CFL3D and FUN3D with SA, SST and $k$-$\omega$ |

Dynamic stall under a constant-rate pitch-up
([Batther & Lee (2022)](/sources/batther-2022.md), §2, §4): $Re_c=2\times10^5$,
$M=0.10$, blunt trailing edge, span $0.1c$, periodic; DDES with four RANS
and transition closures in OVERFLOW 2.3 on an $811\times200\times100$ O-grid
(16 million points), upper-surface $y^+\approx0.4$; the reference is the
wall-resolved LES of Visbal and Garmann (74 million points) as cited, with
no experimental dynamic data. A static 2D RANS at $Re_c=10^6$, $M=0.10$
on the same point count validates the grid against the measurements of
Hristov and Ansell that they cite (§4.1, Fig. 3).

Workshop, moving-grid and aeroacoustic configurations
([Wang et al. (2013)](/sources/wang-2013.md), §4.3, §5.2;
[Sugaya & Imamura (2021)](/sources/sugaya-2021.md), §3;
[Monfaredi et al. (2021)](/sources/monfaredi-2021.md), §4.2):

| Item | Wang et al. (2013) | Sugaya & Imamura (2021) | Monfaredi et al. (2021) |
|---|---|---|---|
| Flow | case C1.3, closed trailing edge $y=\pm0.6(0.2969\sqrt x-0.1260x-0.3516x^2+0.2843x^3-0.1036x^4)$: inviscid $M=0.5$, $\alpha=2^\circ$; inviscid transonic $M=0.8$, $\alpha=1.25^\circ$; laminar $M=0.5$, $\alpha=1^\circ$, $Re_c=5000$, adiabatic wall | steady $M=0.15$ (relative to the grid), $\alpha=10^\circ$, $Re_c=6\times10^6$, the NASA TMR set-up, with the airfoil fixed in a free stream or moving through still air; AGARD Case 3: $M_\infty=0.6$, $Re_c=4.8\times10^6$, $\alpha=4.86^\circ+2.44^\circ\sin\varpi_{\mathrm p}t$, reduced frequency 0.081, pivot at $c/4$ | rod–airfoil: a rod of diameter $c/10$ one chord upstream of the airfoil, $c=0.1$ m, $M_\infty=0.2$, $Re_c=4.8\times10^5$ |
| Model | Euler and laminar Navier–Stokes (no turbulence model) | [Spalart–Allmaras](/methods/spalart-allmaras-model.md) RANS, Spalart–Allmaras wall function at an [immersed boundary](/methods/immersed-boundary-method.md) | 2D URANS with Spalart–Allmaras; permeable [Ffowcs Williams–Hawkings](/methods/ffowcs-williams-hawkings-acoustic-analogy.md) surface; continuous adjoint |
| Discretization | participants' DG, [flux-reconstruction](/methods/flux-reconstruction.md) (CPR), high-order FV and FD codes at $N=1$ to 4, against the second-order finite-volume TAU code | hierarchical Cartesian grid moving rigidly with the body, SLAU finite volumes; about 45,000 cells with $h_{\min}/c=5\times10^{-4}$ (steady) and 85,000 with $2.5\times10^{-4}$ (AGARD) | quadrilateral grid of 161,906 nodes (414 on the airfoil), first node $10^{-5}c$, $y^+<1$ |
| Reference | each participant's own reference solution; force errors against hp-independent values | the body-fitted code FaSTAR on the TMR grid (steady); the experiment of Landon and body-fitted FUN3D (AGARD) | the experiment and LES of Jacob et al., other LES and URANS, as cited |

The airfoil appears with less weight in three further roles: as the
subject, cited by [Bose & Park (2018)](/sources/bose-2018.md), §4.5, of a wall-modelled LES
of its trailing-edge noise at $Re_c=1.5\times10^6$; as the laminar
energy-harvesting foil of [Liu et al. (2022b)](/sources/liu-2022-g.md),
§3.3 ($Re_c=1000$, $M=0.1$, prescribed pitch and flow-driven plunge,
efficiencies of 20% to 34%; see
[geometric conservation law](/properties/geometric-conservation-law.md));
and as the blade section of the
[Caradonna–Tung rotor](/benchmarks/caradonna-tung-rotor.md) of
[Sugaya & Imamura (2021)](/sources/sugaya-2021.md) and
[Han et al. (2022)](/sources/han-2022-c.md).

## What the case tests

**Attached and moderate incidence.** [Zhao et al. (2023b)](/sources/zhao-2023-b.md),
§5.2, obtain $C_p$ coinciding with Ladson's experiment at $0^\circ$ for
polynomial degrees 1 to 3, and agreement with experiment at $10^\circ$ (Figs.
5-4, 5-6). Their forces (Table 5-1) are:

| $\alpha$ | $C_L$ IPDG / McCroskey | $C_D$ IPDG / McCroskey |
|---|---|---|
| $0^\circ$ | 0.00 / 0.00 | 0.0084 / 0.0083 |
| $10^\circ$ | 0.93 / 1.05 | 0.011 / 0.012 |

The authors attribute the $10^\circ$ lift deficit "probably" to the RANS
assumption; it is 11.4% *(compiler check, not in the sources)*. On the
lattice Boltzmann solver, [Mozaffari et al. (2024)](/sources/mozaffari-2024.md),
§3.2, find $C_L$ and $C_D$ close to Ladson's data at $2^\circ$, $6^\circ$ and
$10^\circ$ for all three models, with a slight RANS discrepancy at $15^\circ$
(Fig. 12). IDDES, CES and RANS give identical mean $C_p$ at $10^\circ$; at
$15^\circ$ the hybrids differ slightly downstream of the leading edge
because the fine leading-edge grid lets them run as LES in the outer
boundary layer with only the first few nodes in RANS (Figs. 10–11); see
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) and
[detached-eddy simulation](/methods/detached-eddy-simulation.md).

**Near stall with an immersed boundary and a wall function.**
[Constant et al. (2024)](/sources/constant-2024.md) (read in the HAL
author manuscript) use the airfoil at $15^\circ$ as the "critical flow
incidence" for wall-function boundary conditions on Cartesian grids:

- A modelling height estimated from a flat-plate skin-friction correlation
  places the first computed point at a $y^+$ far above the target near the
  leading edge: the relative error is "close to 300%" for a target of 300
  at $15^\circ$ (§4.1, Fig. 10). After their one-pass adaptation, the
  largest suction-side $y^+$ falls from 435 to 243 for a target of 100
  (§6.1, Fig. 18).
- Over the first 10% of the chord the equilibrium wall function cannot
  represent the velocity profile; beyond it the log region is established
  (§6.1, Figs. 19–21); see
  [equilibrium wall model](/methods/equilibrium-wall-model.md) and
  [wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md).
- Extrapolating the wall pressure from the image point with zero normal
  gradient misplaces the suction peak; a first- or second-order
  reconstruction from a second layer of image points corrects it (§6.1,
  Figs. 23–24).

Forces at $15^\circ$ (Table 3):

| Solution | $C_D\times10^3$ | error | $C_L$ |
|---|---|---|---|
| body-fitted, wall-resolved | 20.85 | — | 1.516 |
| IBM, single modelling height, zeroth-order pressure | 40.44 | 94% | 1.416 |
| IBM, adapted height, zeroth-order pressure | 30.57 | 47% | — |
| IBM, adapted height, second-order pressure | 24.51 | 17% | 1.476 |

Only the adapted solution keeps the lift error below 3% at every incidence
(Fig. 25). The authors relate the remaining drag error of about 20% at
$15^\circ$ to the sensitivity of this test case reported by others, and to
the equilibrium wall model at the leading edge (§6.1).

**High-order RANS of the $k$-$\omega$ family.**
[Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md), §5.4, use the
airfoil to show that their hybridizable DG treatment of the
$\omega$ equation (interpolation of $1/\omega$, removal of the
wall-touching elements from the $\omega$ problem) works on curved geometry.
$C_f$ is over-estimated against the NASA TMR SST solution, which they
attribute to the raised inlet eddy viscosity; $C_p$ lies slightly below
the TMR reference but closer to Ladson's experiment. $\omega$ oscillates in
the wake, and at lower inlet eddy-viscosity ratios the oscillations
"obstruct the convergence of the solver", "one of the drawbacks of using
high-order methods while using the $k-\omega$ model" (Figs. 28–36).

[Ghidoni et al. (2026)](/sources/ghidoni-2026.md), §4.4, test the
first-element height that a wall function tolerates on a modal DG
discretization: $C_p$, $C_f$, $C_D$ and $C_L$ agree with the wall-resolved
reference for all $y_1^+$ and degrees (Figs. 13–14). At $N=6$ the $C_f$
difference grows for $y_1^+>80$ near the leading edge; at $y_1^+=320$ the
$C_f$ peak is under-estimated and recovers from $x/c=0.15$, so the effect on
$C_D$ and $C_L$ is negligible. At $\alpha=15^\circ$ the suction side shows
incipient separation from $x/c=0.72$ that reattaches only at the trailing
edge; the wall function avoids the $C_f$ under-estimation it shows in the
recirculation of the [backward-facing step](/benchmarks/backward-facing-step.md),
which the authors attribute to the smaller recirculation.

**High-order Spalart–Allmaras at $15^\circ$.** [Huang et al. (2022b)](/sources/huang-2022-d.md),
§3.2, run the airfoil at $15^\circ$ to compare their fourth-order
finite-volume scheme with the second-order one on three C-meshes. The
second-order scheme predicts a trailing-edge separation bubble on all
meshes, only slightly smaller on finer grids, and does not converge in lift
and drag on mesh 3; the fourth-order scheme gives a small bubble on mesh 1
and none on meshes 2–3, and its $C_p$ curves overlap across grids
(Figs. 25–29). Lift against the Gregory & O'Reilly value 1.526 (Table 6):

| Scheme, mesh (cells) | $C_L$ | error | relative CPU time |
|---|---|---|---|
| O2, 1 (11,880) | 1.183 | 22.48% | 1 |
| O2, 2 (20,816) | 1.277 | 16.32% | 1.82 |
| O2, 3 (33,150) | 1.299 | 14.88% | 3.01 |
| O2, 4 (143,700) | 1.437 | 5.74% | 22.02 |
| O4, 1 | 1.393 | 8.72% | 1.43 |
| O4, 2 | 1.499 | 1.77% | 2.75 |
| O4, 3 | 1.523 | 0.19% | 4.50 |

With the efficiency measure $1/(\text{error}\times\text{CPU time})$ the
fourth-order scheme gains on refinement (8.0 to 117.0) while the
second-order one loses (4.4 to 0.79); the finest second-order mesh costs
eight times the CPU time of fourth-order mesh 2 for a larger error
(§3.2, Fig. 30). The same case, at CFL 20, shows where their exponential-decay
procedure acts: cells where the predicted $\tilde\nu$ would turn negative
lie near the outer edge of the boundary layer and move downstream as the
solution converges, and none remain near convergence (§2.5, Figs. 15–18);
see [Spalart–Allmaras model](/methods/spalart-allmaras-model.md).

**Entropy-stable DG with Spalart–Allmaras.** [Lodares et al. (2022)](/sources/lodares-2022.md),
§7.4, Table 2, run the TMR case on the coarsest grid with polynomial
degrees $N=2$ to 6 and find lift and drag converging toward the reference
as $N$ rises; at $N=6$:

| $\alpha$ | $C_L$ DGSEM / reference | $C_D$ DGSEM / reference |
|---|---|---|
| $0^\circ$ | — | 0.00813 / 0.00819 (for all $N$) |
| $10^\circ$ | 1.0894 / 1.0909 | 0.01250 / 0.01231 |
| $15^\circ$ | 1.5502 / 1.5461 | 0.02144 / 0.02124 |

The implicit solver reaches CFL numbers near $10^{12}$ by switched
evolution relaxation (§6, Fig. 1); see
[entropy conservation](/properties/entropy-conservation.md).

**The $k$-$\tau$ model in spectral elements.** [Tomboulides et al. (2025)](/sources/tomboulides-2025.md),
§3.4, Tables 3–4, set $k=\tau_t=0$ at the inlet ($\tau_t=1/\omega$, page-local: the turbulent time scale) and use the free-stream
limiter of their [$k$-$\tau$ model](/methods/k-tau-model.md), which they call
"imperative" for external flows; $p=5$ and $p=7$ differ by less than 0.1%
in every reported value.

| Solution | $C_D$, $0^\circ$ | $C_D$, $10^\circ$ | $C_L$, $10^\circ$ |
|---|---|---|---|
| $k$-$\tau$ (Nek5000) | 0.00831 | 0.01381 | 1.0618 |
| regularized $k$-$\omega$ (Nek5000) | 0.00835 | — | — |
| CFL3D SA / SST / $k$-$\omega$ | 0.008190 / 0.008090 / 0.00854 | 0.01231 / 0.01236 / 0.01259 | 1.0909 / 1.0778 / 1.0958 |
| FUN3D SA / SST / $k$-$\omega$ | 0.008120 / 0.008160 / 0.00837 | 0.01242 / 0.01253 / 0.01297 | 1.0983 / 1.0840 / 1.1012 |
| experiment | 0.0081 | 0.012 | 1.075 |

At $10^\circ$ the $k$-$\tau$ model over-predicts drag and under-predicts lift,
whereas the NASA codes over-predict both; its lift error is smaller than
that of the standard $k$-$\omega$ in either NASA code. $C_p$ agrees with
Gregory & O'Reilly and Ladson at both angles (Fig. 16).

**Dynamic-stall onset in DDES.** In the constant-rate pitch-up of
[Batther & Lee (2022)](/sources/batther-2022.md), DDES with
SST Langtry–Menter, SA Medida–Baeder, SA amplification-factor-transport
and fully turbulent SA closures reproduces the LES sequence of
leading-edge laminar separation bubble, its bursting near $16.9^\circ$ and
the formation of the dynamic-stall vortex, but stalls slightly earlier
with a slightly lower peak lift; the amplification-factor-transport model
is closest to the LES (§4.2–§4.5, Figs. 14–22). Grids 2 and 3 give similar
loads and stall inception, grid 1 stalls early, and all three underpredict
the LES peak lift (§4.2.1, Fig. 4). The stages and the stall type are on
[dynamic stall](/definitions/dynamic-stall.md).

**Massive separation at $45^\circ$.** [Mozaffari et al. (2024)](/sources/mozaffari-2024.md),
§3.2, Table 2, after 234 flow-through times with 110 averaged:

| Model | $C_L$ | $C_D$ |
|---|---|---|
| SST RANS | 2.238 | 2.053 |
| SST-IDDES | 1.231 | 1.038 |
| SST-CES | 1.192 | 0.993 |
| reference (Shur et al., as cited) | 1.097 | 1.180 |

The RANS lift and drag exceed the reference by factors of about 2.0 and
1.7 *(compiler check, not in the sources)*; the two hybrids "perform
almost the same without any superiority" (§3.2).

**Transonic shock.** At $M=0.804$, [Zhao et al. (2023b)](/sources/zhao-2023-b.md),
§5.3, place the shock at $x\approx0.47c$ with $C_p$ extrema consistent with
ONERA data, but "the ending position of the shock wave slightly lags
behind", attributed to an overestimated shock–boundary-layer interaction
(Figs. 5-9–5-11); see
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).

**Implicit LES polars.** As recalled by [Ferrer et al. (2023)](/sources/ferrer-2023.md),
§4.1, Fig. 7, from the group's earlier paper, a DG implicit LES at
$Re_c=10^6$ on 18,000 hexahedra with $N=4$ (2.2 million degrees of freedom)
gives lift and drag polars in "very good agreement" with experimental data
not named in that paper; see [implicit LES](/definitions/implicit-les.md)
and [HORSES3D](/software/horses3d.md).

**Non-regression of data-driven RANS corrections.** Both data-driven
sources use the static airfoil as a flow their corrections were not
trained on.

- [Wu et al. (2025)](/sources/wu-2025.md), §4.5, Fig. 50, take SST as
  accurate for the attached $C_f$ at $\alpha=0^\circ$ and test whether two
  [symbolic-regression](/methods/symbolic-regression-closure.md) corrections
  of the SST $\omega$-destruction term, fitted to
  [field-inversion](/methods/field-inversion-machine-learning.md) data of
  separated flows, leave it unchanged ("L2 generalizability" in their
  four-level scale, Table 1). SR-CND, whose correction is gated by the DDES
  shielding function so that it vanishes in attached boundary layers, gives
  nearly the same $C_f$ as SST; SR-CLS, trained by classic ungated
  inversion, overpredicts it. The same pair behaves the same way on the
  zero-pressure-gradient [flat plate](/benchmarks/turbulent-boundary-layer.md).
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md), §5.1.3, run the
  polar from $0^\circ$ to $18^\circ$ with three experts (baseline SST; a
  separated-flow correction; a jet correction) and a random-forest
  [blend of the experts](/methods/turbulence-model-aggregation.md). The jet
  expert gives the largest $C_L$ and $C_D$ discrepancies; SST "performs
  better than" the separated-flow expert "for most of the present flows,
  the latter model being too dissipative", so that expert "should be
  replaced or supplemented"; the blend reproduces the lift-curve slope,
  drag and surface pressure near SST, giving the separated-flow expert
  weight in moderately separated suction-side regions and SST in attached
  ones (Figs. 15–16). No error table is printed for this case. Projected in
  latent feature spaces (PCA, t-SNE, autoencoder), the airfoil features
  lie mostly inside the training region, with outliers "especially at
  higher angles of attack" (§5.1, Fig. 10).

**Deep dynamic stall and the spanwise domain.**
[Baldan & Guardone (2025)](/sources/baldan-2025.md) (read in arXiv v2)
simulate the Lee & Gerontakos pitching airfoil, $-5^\circ\le\alpha\le25^\circ$,
with wall-resolved LES on four spanwise-periodic extrusions,
$L_z/c=0.2$, 0.4, 0.8 and 1.2, at the same $\Delta z=10^{-3}c$ (62.7 to
374.7 million nodes). The wall resolution satisfies $\Delta x^+<40$,
$\Delta y^+<5$, $\Delta z^+<20$ on all grids, including the instant when
the near-wall velocity exceeds twice the free stream (§2.1, Fig. 7). The
cycle takes 144,000 time steps of $2.337\times10^{-6}$ s
($2.181\times10^{-4}$ convective times, CFL about 1); one cycle is recorded
after a quarter cycle is discarded, without phase averaging (§1.2).

- *Upstroke.* With the flow attached and a
  [laminar separation bubble](/definitions/laminar-separation-bubble.md)
  near the leading edge, the span does not matter: from $-5^\circ$ to about
  $22^\circ$ the four spans differ by at most 0.05 in $C_L$ (Fig. 3).
  Transition starts near the trailing edge around $\alpha=2^\circ$ and moves
  towards the bubble by $10^\circ$; the dynamic-stall vortex forms beyond
  $15^\circ$ and reaches the trailing edge at $22^\circ$ (Fig. 6).
- *Downstroke.* Once the bubble bursts and the dynamic-stall vortex forms,
  the two short spans force a quasi-two-dimensional vortex with a more
  coherent core and higher peak velocity, and the trailing-edge-vortex
  interaction produces spurious lift peaks exceeding the upstroke $C_L$ by
  0.5 and $C_D$ by 0.3. The two long spans develop three-dimensional
  structures and follow the experimental downstroke trend with a $C_L$
  offset of about 0.25 (Figs. 3–4). At $10^\circ$ in the downstroke the
  1.2$c$ span is fully stalled while 0.8$c$ still shows oscillatory wake
  patterns (Fig. 4).
- *Recommendation.* A span of at least one chord is needed to capture the
  dynamic-stall vortex in the downstroke; the 0.05$c$–0.2$c$ spans common in
  the LES literature are adequate only for the attached upstroke, the part
  that ramp-up studies simulate (§3).
- *Model comparison.* The 1.2$c$ LES, 2D URANS ($k$-$\omega$ SST with an
  intermittency transition model) and 3D SBES agree within 0.1 in $C_L$ in
  attached flow, all put peak lift at $22^\circ$ against $24^\circ$
  measured, diverge in the early stalled downstroke ($24^\circ$–$18^\circ$)
  and reconverge later; a $C_L$ offset of 0.2 from experiment persists
  (§2.2, Fig. 9). The authors infer that the experiment–simulation
  discrepancies usually blamed on turbulence models come instead from other
  factors, such as wind-tunnel effects or the model's surface roughness
  (§3). The span requirement belongs also to
  [grid-point requirements of LES](/results/les-grid-point-requirements.md).

**Order of accuracy at the trailing-edge singularity.** In the first
High-Order CFD Workshop, [Wang et al. (2013)](/sources/wang-2013.md), §5.2,
Figs. 16–21, compare error against degrees of freedom and work units
(their TauBench-based cost unit):

- inviscid subcritical: $N=3$ is more efficient than $N=1$ in degrees of
  freedom and work units "even at moderate error", but no scheme reaches
  its asymptotic rate under uniform refinement, because of the
  trailing-edge singularity; output-based fixed-DOF mesh optimisation (MIT)
  gives the highest rates, at least for drag;
- transonic: the gain of $N=2$ over $N=1$ is smaller than for smooth
  problems, but $N=2$ "does not fare worse"; adaptive refinement generally
  beats uniform refinement, including an hp-adaptive run with $N=1$ to 4;
- laminar, $Re_c=5000$: $N=1$ is comparable with TAU and $N=3$ generally
  better, especially at high accuracy, after the residual criterion was
  relaxed from ten to eight orders of magnitude.

The authors call these results "qualitative in nature": the participants
generated their own reference solutions without common standards, and the
scatter of those references is similar to the errors under refinement
(§5.2). See [mesh adaptation](/methods/mesh-adaptation.md).

**An immersed boundary on a moving Cartesian grid.**
[Sugaya & Imamura (2021)](/sources/sugaya-2021.md), §3.1, run the steady
TMR case twice, the airfoil fixed in a free stream and the grid moving
with the airfoil through still air, to verify the Galilean invariance of
their moving-grid formulation: the density residuals are
$4.85717\times10^{-11}$ and $4.85718\times10^{-11}$ after 15,000 steps and
$4.20906\times10^{-16}$ and $4.49798\times10^{-16}$ after 30,000, differences
"in the order of machine zero" (Table 3, Fig. 5); the $C_p$, $C_f$,
velocity and eddy-viscosity profiles of the two runs coincide and agree
with the body-fitted FaSTAR solution (Figs. 6–8). The first image point
lies at $y^+\approx230$ at $x/c=0.5$; citing earlier studies, the authors
state that immersed boundaries with wall functions agree with body-fitted
grids for surface pressure when $y^+$ is "approximately 500 or less"
(Fig. 4). See [immersed boundary method](/methods/immersed-boundary-method.md)
and [RANS wall functions](/methods/rans-wall-function.md).

**Transonic pitching.** On AGARD Case 3, with 800 steps per cycle, three
cycles and $y^+\sim100$ at $x/c=0.5$, the same method places the shock and
the suction peak at $5.92^\circ$ in the upstroke as FUN3D on a body-fitted
grid and the experiment, reproduces the $C_L$–$\alpha$ hysteresis loop and
the inversion of the lift trajectory near $6^\circ$, and differs from the
measured pitching moment by "around 0.005, which is almost the same" as
the body-fitted simulation (§3.2, Figs. 10–13). Since the immersed
boundary is not strictly conservative, the authors offer this agreement as
evidence that the non-conservation does not spoil unsteady aerodynamics.
Its incidence stays between $2.42^\circ$ and $7.30^\circ$
*(compiler check, not in the sources)*; the paper does not present it as
[dynamic stall](/definitions/dynamic-stall.md).

**Rod–airfoil noise and its adjoint.**
[Monfaredi et al. (2021)](/sources/monfaredi-2021.md), §4.2, use the
airfoil behind a rod as the turbulent case of an aeroacoustic shape
optimization. The 2D Spalart–Allmaras URANS sheds from the rod at
$St=0.24$, as an earlier 2D URANS they cite, against about 0.19 measured,
an over-prediction they call expected of URANS; the mean $C_p$ on the
pressure side agrees with a 3D LES, both above the experiment (Figs. 7–8,
10). Adjoint sensitivities with respect to 50 free-form-deformation
variables agree with central finite differences (Fig. 14); 12 optimization
cycles reduce the noise objective by 30% and the main spectral peak by
about 3.7 dB to 90.7 dB, at the price of a mean drag increase of 0.011 and
a lift change of $-0.018$ (§4.2, Fig. 16). The acoustic method is on
[Ffowcs Williams–Hawkings acoustic analogy](/methods/ffowcs-williams-hawkings-acoustic-analogy.md).

**Wall-modelled LES of trailing-edge noise.**
[Bose & Park (2018)](/sources/bose-2018.md), §4.5, cite a wall-modelled LES of
the airfoil's trailing-edge noise at $Re_c=1.5\times10^6$ (Kocheemoolayil &
Lele) is within 3 dB of the measurements, but on a grid with
$\Delta y^+\lesssim10$ and $\Delta x_i^+\sim40$, close to wall-resolved
resolution; see [wall-modelled LES](/methods/wall-modelled-les.md).

**What the sources share.** Away from stall the RANS solutions of all
three discretizations match the reference forces; the discrepancies
gather at the leading edge at high incidence: the $10^\circ$ lift deficit
in [Zhao et al. (2023b)](/sources/zhao-2023-b.md), the wall-function
leading-edge error at $15^\circ$ in
[Constant et al. (2024)](/sources/constant-2024.md), the $15^\circ$ RANS
discrepancy in [Mozaffari et al. (2024)](/sources/mozaffari-2024.md).
The two high-order $k$-$\omega$ studies place their difficulty at the
leading edge as well (the $C_f$ peak at $y_1^+=320$ in
[Ghidoni et al. (2026)](/sources/ghidoni-2026.md)) and, for the
discretization itself, in the wake (the $\omega$ oscillations of
[Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md)).
Of the three Spalart–Allmaras and $k$-$\tau$ studies, only
[Huang et al. (2022b)](/sources/huang-2022-d.md) compare a high-order with
a second-order scheme on this airfoil: a fourth-order lift error of 0.19%
on 33,150 cells against 5.74% for the second-order scheme on 143,700
(Table 6). [Lodares et al. (2022)](/sources/lodares-2022.md) report forces
converging toward the reference on the coarsest TMR grid as $N$ rises
(Table 2), and [Tomboulides et al. (2025)](/sources/tomboulides-2025.md)
forces that change by less than 0.1% between $p=5$ and 7 (§3.4). Each
treats the sign of its turbulence variable: Huang et al. by their
exponential-decay procedure for negative $\tilde\nu$, which they observe
at the outer edge of the boundary layer (§2.5), Lodares et al. by a
negative-$\tilde\nu$ model variant (§2), and Tomboulides et al. by
transporting $\tau_t=1/\omega$ to avoid the near-wall singularity of
$\omega$ (§1–§2).

## Qualifications

- The configurations differ in Reynolds number ($1.35\times10^5$,
  $2\times10^5$, $10^6$, $2.88\times10^6$, $3\times10^6$,
  $4.09\times10^6$, $6\times10^6$) and reference ($C_p$ and forces of experiments, a
  body-fitted computation); no source compares its errors with another's.
- [Constant et al. (2024)](/sources/constant-2024.md) print a lift error
  of 5.6% for the non-adapted solution in Table 3, while the table's own
  coefficients give 6.6%, and call the non-adapted lift error at $15^\circ$
  "almost 10%" in the text *(compiler check, not in the sources)*.
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) head the
  $45^\circ$ reference column "Exp." while citing Shur et al.'s
  detached-eddy simulation of an airfoil at high incidence; they mention
  $60^\circ$ without reporting results. The chord is not stated.

- [Baldan & Guardone (2025)](/sources/baldan-2025.md) print the angular
  frequency of the pitching motion as "18.67 [Hz]"; their own step count
  and step size give a period of 0.3365 s, so 18.67 is in rad/s
  *(compiler check, not in the sources)*. They say transition starts at the
  trailing edge "progressing downstream" (Introduction), while §2.1 has it
  progressing towards the bubble, i.e. upstream. Their Table 1 quad count
  (311,622) does not match the hexahedra of Table 2, which correspond to
  $933\times333$ quads per layer *(compiler check, not in the sources)*.
  The $C_L$ offset from experiment is printed as about 0.25 (§2.1) and 0.2
  (§2.2).
- Their inference that turbulence modelling is not the main source of
  discrepancy rests on one recorded cycle per model without phase
  averaging (§1.2, §2.2); the URANS and SBES come from the authors' earlier
  work with the same solver, and the 0.8$c$ and 1.2$c$ spans still differ
  at $10^\circ$ in the downstroke (Fig. 4).
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) caption their
  Fig. 33 with $Re=6.6\times10^6$, while the text and the other figures of
  the case give $6\times10^6$. [Ghidoni et al. (2026)](/sources/ghidoni-2026.md)
  print the element counts of their coarser meshes as
  "$5\,929<n_e<2\,899$" (§4.4), an inverted inequality.
- [Wu et al. (2025)](/sources/wu-2025.md) refer to "Figure 45" for the
  airfoil C-grid, which is their Fig. 49. The NACA 0012 claims of
  [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) ("accurate
  predictions of lift, drag", §6) rest on plots without error metrics.

- [Huang et al. (2022b)](/sources/huang-2022-d.md) print an O2 mesh-4
  lift error of 5.74% (Table 6), while their $C_L=1.437$ and 1.526 give
  5.83%; the printed efficiency 0.791 follows from 5.74% *(compiler check,
  not in the sources)*. They call mesh 4 "an even smaller mesh", though it
  has the most cells.
- [Lodares et al. (2022)](/sources/lodares-2022.md) label their reference
  "FUN3D, 897×257" in Table 2 and "CFL3D, 897 x 257 grid" in the Fig. 10
  legends. Their $\alpha=0^\circ$ and $10^\circ$ reference values
  (0.00819; 1.0909, 0.01231) coincide with the CFL3D Spalart–Allmaras values
  that [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) list
  (Tables 3–4), not with their FUN3D ones *(compiler check, not in the
  sources)*.
- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) call their
  $10^\circ$ drag a slight over-prediction; 0.01381 against the
  measured 0.012 is 15.1% high, against at most 8.1% for the NASA-code
  values (FUN3D $k$-$\omega$, 0.01297) *(compiler check, not in the
  sources)*. They cite Freeman and Roy (2014)
  for the CFL3D and FUN3D values in Table 3 and Jespersen et al. (2016) in
  Table 4.
- [Batther & Lee (2022)](/sources/batther-2022.md) do not name the
  turbulence model of their static validation run (§4.1).
- [Wang et al. (2013)](/sources/wang-2013.md) print the laminar incidence
  as "$\alpha = 1$" without the degree sign used for the other conditions
  (§4.3).
- [Sugaya & Imamura (2021)](/sources/sugaya-2021.md) report a "small
  improvement" from taking the face-centre pressure from the fluid cell
  instead of the image point without showing it (§2.2, Table 1), and give
  their Reynolds number on the velocity relative to the grid.
- [Monfaredi et al. (2021)](/sources/monfaredi-2021.md) give the peak
  reduction as about 3.7 dB in §4.2 and 3.6 dB in the Conclusions, and call
  3456 Hz the "third harmonic" of the 1728 Hz tone, whose frequency it
  doubles, $3456=2\times1728$ *(compiler check, not in the sources)*.
  Their URANS is two-dimensional.

# Citations

- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §5.2, Table 5-1, Figs. 5-4–5-6; §5.3, Figs. 5-9–5-11.
- [Constant et al. (2024)](/sources/constant-2024.md) — §4.1, Fig. 10; §5.1, Figs. 12–13; §6.1, Tables 1–3, Figs. 18–25.
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §3.2, Table 2, Figs. 9–12.
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §4.1, Fig. 7 (recalled result).
- [Wu et al. (2025)](/sources/wu-2025.md) — author manuscript: Table 1; §4.5, Figs. 49–50.
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — arXiv v2: §5.1, Fig. 10; §5.1.3, Figs. 15–16; §6.
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §5.4, Figs. 28–36.
- [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) — §4.4, Figs. 13–14.
- [Baldan & Guardone (2025)](/sources/baldan-2025.md) — arXiv v2: Introduction; §1.1–1.2, Eq. 1, Tables 1–2; §2.1, Figs. 3–8; §2.2, Fig. 9; §3.
- [Huang et al. (2022b)](/sources/huang-2022-d.md) — §2.5, Table 4, Figs. 15–18; §3.2, Tables 5–6, Figs. 25–30.
- [Lodares et al. (2022)](/sources/lodares-2022.md) — §6, Fig. 1; §7.4, Table 2, Figs. 9–10.
- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) — §3.4, Tables 3–4, Figs. 13–16.
- [Batther & Lee (2022)](/sources/batther-2022.md) — §2.1–2.2, Tables 1–2; §4.1, Fig. 3; §4.2–§4.5, Figs. 4–22.
- [Wang et al. (2013)](/sources/wang-2013.md) — §3.2; §4.3 (case C1.3); §5.2, Table III, Figs. 16–21.
- [Sugaya & Imamura (2021)](/sources/sugaya-2021.md) — §2.2, Table 1; §3.1, Tables 2–3, Figs. 4–8; §3.2, Figs. 9–13.
- [Monfaredi et al. (2021)](/sources/monfaredi-2021.md) — §4.2, Figs. 6–18; Conclusions.
- [Bose & Park (2018)](/sources/bose-2018.md) — §4.5 (cited result).
- [Liu et al. (2022b)](/sources/liu-2022-g.md) — §3.3, Table 4 (laminar harvester).
- [Han et al. (2022)](/sources/han-2022-c.md) — §4 (blade section of the Caradonna–Tung rotor).

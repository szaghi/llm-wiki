---
type: Software
title: "TRACE"
description: "TRACE is DLR's turbomachinery flow solver, with a second-order finite-volume solver for RANS, URANS and DDES and a high-order DGSEM solver for implicit LES; this page records the configurations, transition and Reynolds-stress closures, inflow generation, flux blending and costs reported by the cascade studies of the bundle."
status: established
aliases: [DLR TRACE, TRACE DG, TRACE solver]
tags: [software, turbomachinery, dg, implicit-les, des, transition]
timestamp: 2026-10-26T15:52:00Z
---

# TRACE

**TRACE** is the turbomachinery flow solver of the German Aerospace Center
(DLR). Three sources of the bundle use it, all on linear compressor or
turbine cascades. It contains two solvers. The first is a density-based,
cell-centred, second-order **finite-volume** solver for RANS, URANS and
hybrid RANS/LES. The second is a high-order
**[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md)**
solver used for wall-resolved [implicit LES](/definitions/implicit-les.md)
([Morsbach et al. (2024)](/sources/morsbach-2024.md), §2;
[Klose et al. (2025)](/sources/klose-2025.md), §2;
[Möller et al. (2024)](/sources/moller-2024.md), §III.A). The sources cite
DLR's "Numerical Test Rig" papers for the solver descriptions and print no
code-level details such as language or parallel model.

## DGSEM solver for implicit LES

Both DG studies use nodal collocation on Legendre–Gauss–Lobatto nodes, which
gives a diagonal mass matrix. Neither adds an explicit subgrid model: "the
numerical dissipation of the Riemann solver" supplies the subgrid
dissipation (Klose et al. 2025, §2). The two studies stabilize the scheme with
different split forms:

| Item | Morsbach et al. (2024), T161 turbine cascade | Klose et al. (2025), TCTA compressor cascade |
|---|---|---|
| Degree | $N=5$ (sixth order) | $N=3$ (fourth order) |
| Volume flux | Kennedy–Gruber [kinetic-energy-preserving](/properties/kinetic-energy-preservation.md) split form | Chandrashekar entropy-conserving split form with its matching Riemann solver |
| Interface flux | Roe | "the corresponding Riemann solver" of the Chandrashekar flux (as printed) |
| Viscous terms | BR1, central flux, no penalty | BR1 with a central interface flux |
| Time | SSP-RK3 | explicit third-order Runge–Kutta (Shu–Osher) |
| Shocks | none (exit Mach number 0.6) | [subcell finite-volume blend](/methods/subcell-finite-volume-shock-capturing.md) of Hennemann et al., first-order FV residual, Fernandez dilatation–vorticity sensor with relaxation factors 0.7 |
| Largest run | 876 960 elements, geometry degree 4, 189.4M degrees of freedom | 375.2M degrees of freedom on 16 384 MPI ranks |

(Morsbach et al. 2024, §2, §3.1; Klose et al. 2025, §2–§3, Table 1.) The
blending factor $\alpha$ is the registry's DG/FV factor. Klose et al. scale
the wall-unit spacings by $N$ "to aid the comparability to FV simulations".
Morsbach et al. report $(23.1,0.742,15.0)$ in streamwise, wall-normal and
spanwise wall units at midspan. Klose et al. report averages of
$(25.5,1.39,21.4)$ on their refined grid.

Synthetic inflow turbulence is imposed weakly in the DG solver. Fourier-mode
fluctuations after Shur et al. (2014) are added to a mean state from a
Riemann boundary condition and enter through a central flux on the inflow
faces. Outflow uses one-dimensional non-reflecting conditions (Morsbach et
al. 2024, §2; see
[inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
Klose et al. impose no inflow turbulence, since the measured level is below
1% (§3).

## Finite-volume solver: RANS, URANS and DDES

- **Discretization.** Second order. Klose et al. (2025, §2) give Green–Gauss
  gradients, the Venkatakrishnan limiter and Roe's approximate Riemann solver
  for their URANS. Möller et al. (2024, §III.A) describe a density-based,
  cell-centred scheme with explicit third-order Runge–Kutta.
- **Closures used.** The [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md)
  with Kato–Launder production (Morsbach et al.; Klose et al.). The
  SSG/LRR-$\omega$ [Reynolds-stress model](/methods/reynolds-stress-model.md)
  (Morsbach et al.). The $\gamma$-$Re_\theta$
  [transition model](/methods/local-correlation-based-transition-model.md)
  coupled to both closures (Morsbach et al.; Klose et al.). Menter's
  one-equation $\gamma$ model coupled to SST-based delayed
  [detached-eddy simulation](/methods/detached-eddy-simulation.md), the
  "DDES-$\gamma$" of Möller et al. (§II.B).
- **Inviscid-flux blending for DDES.** Möller et al. (2024, §II.C, Eq. 26)
  blend a central and a Roe upwind flux, $F=(1-\sigma_b)F_{\mathrm{central}}+\sigma_bF_{\mathrm{upwind}}$,
  with $\sigma_b$ (page-local) the upwind fraction. In transitional DDES the
  dynamic blending of Travin et al. is fully upwind in the boundary layers
  and damps the synthetic turbulence there. A constant $\sigma_b$ of 5% gives
  the best skin friction on both sides of the V103
  [compressor cascade](/benchmarks/compressor-cascade.md). With 0% the
  solution oscillates and the bubble is suppressed; 25%, the value of Yin &
  Durbin, over-damps the synthetic turbulence in this solver (§III.B.3). The
  authors call the 5% value case- and mesh-dependent. Details are on
  [numerical dissipation](/properties/numerical-dissipation.md).
- **Synthetic turbulence.** The generator of Shur et al. (2014) is
  "implemented in TRACE by Morsbach & Franke" and fed from a RANS precursor
  (Möller et al. 2024, §II.E).
- **Calibration.** Möller et al. checked $C_{DES}=0.65$ in TRACE on decaying
  isotropic turbulence (results not shown, §II.B.1).

## Studies run with it

| Study | Solver | Case | Resolution | Cost |
|---|---|---|---|---|
| Morsbach et al. (2024) | DGSEM $N=5$, implicit LES; FV SST and SSG/LRR-$\omega$ with $\gamma$-$Re_\theta$ | MTU T161 low-pressure [turbine cascade](/benchmarks/turbine-cascade.md), exit $Re=9\times10^4$, $M=0.6$, turbulent end-wall boundary layers | 189.4M degrees of freedom (fine), 67.9M (coarse) | not printed |
| Möller et al. (2024) | FV, DDES-$\gamma$ and WALE LES | V103 [compressor cascade](/benchmarks/compressor-cascade.md), $Re=138\,500$ on axial chord, $M=0.1$, inflow $Tu=3.25\%$ | DDES 0.68M, 1.08M (chosen), 4.32M cells; LES 10.86M cells; 40 spanwise cells; $y^+<1$ | not printed |
| Klose et al. (2025) | DGSEM $N=3$ with FV subcells, implicit LES; FV URANS SST + $\gamma$-$Re_\theta$ | TCTA transonic compressor cascade, $M_{\mathrm{in}}=1.21$, $Re_c=1.35\times10^6$, shock buffet | 54.6M–375.2M degrees of freedom; URANS 0.12M | 15 583–152 850 CPU-hours per convective time on 4096–16 384 ranks (HAWK); URANS 74.6 |

(Morsbach et al. 2024, §3.1–3.2, Table 2; Möller et al. 2024, §III.A,
Tables 2–3; Klose et al. 2025, §3, Table 1.)

**Findings that bear on the code's closures.**

- In the turbine cascade both FV RANS models miss the midspan
  [separation bubble](/definitions/laminar-separation-bubble.md) that the DG
  LES and the experiment show. They underestimate the midspan loss by 35%
  (SST) and 29% (SSG/LRR-$\omega$), and overpredict the end-wall peak loss
  by 34% and 48% (Morsbach et al. 2024, §4).
- In the transonic cascade the FV URANS reproduces the buffet Strouhal
  number of the LES (0.161 against about 0.16; experiment about 0.14). It
  puts the mean shock upstream, gives less than half the LES amplitude and
  a mostly laminar suction side. It needs a time step of
  $2.8\times10^{-5}$ convective times to get the oscillation right (Klose et
  al. 2025, §6, Table 2; see
  [shock–boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).
- In the V103 cascade DDES-$\gamma$ beats fully turbulent DDES on
  suction-side separation-induced transition. Bypass transition on the
  pressure side improves only with synthetic inflow turbulence and constant
  5% blending, and the authors doubt the model is then still a DDES rather
  than "more like an LES model" (Möller et al. 2024, §III.B).

## Qualifications

- The sources use TRACE's DG and FV solvers side by side as high- and
  low-fidelity tools on the same cascade. None compares the two solvers at
  equal cost.
- Klose et al. (2025) print the BR1 scheme as "Bassy-Rebay-1"; the version
  read is the ASME accepted manuscript. Möller et al. (2024) is read as the
  author-typeset accepted manuscript (pages 2–30).

# Citations

- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §2 (DG and FV solvers, inflow and outflow conditions, closures); §3.1–3.3, Table 2 (meshes, inflow); §4 (LES against RANS).
- [Möller et al. (2024)](/sources/moller-2024.md) — accepted manuscript: §II.B–II.E, Eq. 26 (DDES-$\gamma$, flux blending, STG in TRACE); §III.A, Tables 2–3 (solver, meshes); §III.B (results, 5% blending).
- [Klose et al. (2025)](/sources/klose-2025.md) — ASME accepted manuscript: §2, Eq. 1 (DG solver, subcell blending, FV URANS); §3, Table 1 (grids, costs); §6, Table 2 (URANS against LES).

---
type: Software
title: "ProLB"
description: "ProLB is a lattice Boltzmann solver on octree Cartesian grids with a regularized collision, eddy-viscosity closures and immersed boundaries; in the sources it runs wall-modelled LES of the Ahmed body, turbulent fluid–structure interaction, k-ω SST RANS and hybrids, and Spalart–Allmaras-based ZDES mode 2 on a flat plate, a step and a high-lift airfoil."
status: established
aliases: [ProLB solver]
tags: [software, lattice-boltzmann, les, hybrid-rans-les, immersed-boundary, wall-model]
timestamp: 2026-10-27T15:51:00Z
---

# ProLB

**ProLB** is a [lattice Boltzmann](/methods/lattice-boltzmann-method.md)
solver used by four ingested sources, three of which share an author
(Jacob; Cheylan et al. and Mozaffari et al. are at the M2P2 laboratory,
Aix-Marseille University):
[Cai et al. (2022)](/sources/cai-2022.md), for
[wall-modelled LES](/methods/wall-modelled-les.md) of the
[Ahmed body](/benchmarks/ahmed-body.md), and
[Cheylan et al. (2023)](/sources/cheylan-2023.md), for an
[immersed-boundary](/methods/immersed-boundary-method.md) analysis and
turbulent fluid–structure interaction, and
[Mozaffari et al. (2024)](/sources/mozaffari-2024.md), for
[$k$-$\omega$ SST](/methods/k-omega-sst-model.md) RANS and SST-based
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) in a research version
of the code. The fourth,
[Husson et al. (2024)](/sources/husson-2024.md) (ONERA), runs a development
branch of "the commercial solver ProLB" (§2.1) for Spalart–Allmaras RANS
and [zonal detached-eddy simulation](/methods/detached-eddy-simulation.md)
mode 2 (2020), which they call ZDES-LBM. None is a code description: ProLB is named and its components
are summarized, with validation referred to the group's earlier papers (Cai
et al. 2022, §II.A, citing their Refs. 17–19, 23, 24). Mozaffari et al.
(2024) use a research version of what they call a commercial solver.

## Components

| Component | Cai et al. (2022) | Cheylan et al. (2023) | Mozaffari et al. (2024) | Husson et al. (2024) |
|---|---|---|---|---|
| Lattice | D3Q19 | D3Q19 | D3Q19, trapezoidal shifted populations (§2.1, Eqs. 1–4) | D3Q19 (§2.1, Eq. 2) |
| Collision | hybrid recursive regularized (HRR-$\rho$), hyper-viscosity weight "as close to unity as possible" (§II.A, Eq. 7) | hybrid recursive regularized, traceless non-equilibrium tensor (§2.1) | hybrid recursive regularized, weight 0.98 (§2.1, Eq. 5) | hybrid recursive regularized BGK, blending weight 0.98 "as in" Soni et al.; recursive third-order off-equilibrium coefficients and an improved D3Q19 equilibrium (§2.1, Eqs. 7–14) |
| Forcing | — | Guo forcing of the immersed-boundary body force (§2.1, Eqs. 3–4) | — | — |
| Turbulence model | [Vreman](/methods/vreman-model.md) SGS, $C_s\approx0.1$, filter width the grid size (§II.A) | shear-improved [Smagorinsky](/methods/smagorinsky-model.md) SGS of Lévêque et al. (§2.7) | Spalart–Allmaras and $k$-$\omega$ SST RANS; SST-IDDES and SST continuous eddy simulation; SST equations by finite differences inside the collision step (§2.3) | [Spalart–Allmaras](/methods/spalart-allmaras-model.md) RANS and ZDES mode 2 (2020), $C_{DES}=0.65$; the $\chi=\tilde\nu/\nu$ equation by finite differences (second-order centred, hybrid upwind–centred advection), independent of the distributions (§2.2, Eqs. 18–35) |
| Grid | octree (hierarchical) Cartesian (§III) | uniform Cartesian (§3) | octree Cartesian, isotropic refinement, multi-tree (§2.2, §3) | isotropic octree Cartesian with factor-two level transitions, 5–6 levels (§4) |
| Walls | reconstruction at boundary points, explicit Lambert-W [equilibrium wall model](/methods/equilibrium-wall-model.md), constrained-LES near-wall viscosity (§II.B–II.C) | direct-forcing immersed boundary with Lagrangian markers and weight (§2.2–2.4) | reference-point reconstruction; Cai & Sagaut explicit equilibrium wall model, or a zero-velocity Dirichlet condition; $k$, $\omega$ wall functions (§2.2, Eqs. 9–15, 22–25) | sharp-interface direct forcing on fluid-side nodes, all distributions overwritten by equilibrium plus off-equilibrium parts; interpolation point at $2.5\Delta y$ by weighted least squares from eight nodes; Allmaras–Johnson analytical SA [wall law](/methods/rans-wall-function.md), linearized below the interpolation-point distance, inverted by Newton–Raphson (§3, Eqs. 36–43) |
| Coupling | — | explicit staggered coupling with the finite-element solver Calculix (§2.6) | — | — |

In all four, the eddy viscosity (subgrid or RANS) enters through the relaxation time,
$\nu+\nu_t=c_s^2(\tau_{\mathrm{LB}}-\Delta t/2)$ ($\tau_{\mathrm{LB}}$ the
relaxation time, registry §11; $c_s$ the lattice sound speed, page-local), and the
weakly compressible flow is valid for Mach numbers below about 0.3. The time
step is tied to the finest grid spacing, $\Delta t=(c_s/c_0)\Delta x_{\min}$
($c_0$ the physical sound speed), so Cai et al. (2022, §III) raise the Mach
number from 0.12 to 0.24 to double the time step. Husson et al. (2024,
§2.1, Eq. 15) print the same relation in the form
$\tau_{\mathrm{LB}}=(\nu+\nu_t)/c_0^2+\Delta t/2$, with $\rho=p/c_0^2$,
from a Chapman–Enskog expansion to second order.

## Studies run with it

- **Ahmed body, 35° slant** (Cai et al. 2022, §III–§IV): $Re_H=7.68\times10^5$,
  octree grids of $1.36\times10^7$ and $4.03\times10^7$ cells (finest
  spacing $9.0\times10^{-3}H$ and $4.5\times10^{-3}H$), 200 flow-through times
  of which 150 averaged. With the wall model on the whole body the flow stays
  attached on the slant on the coarse grid and separates massively on the
  fine one; drag coefficients 0.2347 to 0.2912 against 0.279 measured by
  Meile et al. Details on [Ahmed body](/benchmarks/ahmed-body.md) and
  [immersed boundary methods](/methods/immersed-boundary-method.md).
- **Immersed-boundary verification** (Cheylan et al. 2023, §3.1–3.3):
  laminar cylinder at $Re=100$ (finest drag error 0.035 at a spacing of
  $0.005$ with $D=0.4$), Poiseuille channel, and a three-dimensional flapping
  flag at $Re=200$ coupled to Calculix.
- **Turbulent fluid–structure interaction** (Cheylan et al. 2023, §3.4): an
  elastic beam behind a fixed cylinder at $Re=10^4$, density ratio 1, with
  LES; Strouhal numbers 0.185 and 0.101 against 0.175 and 0.103 of Breuer
  et al. (Table 13).
- **RANS and hybrid RANS/LES** (Mozaffari et al. 2024, §3): NACA 23012 at
  $Re_c=1.88\times10^6$ ($3.8\times10^6$ nodes, SST against SA RANS);
  [NACA 0012](/benchmarks/naca-0012-airfoil.md) at $Re_c=3\times10^6$ up to
  $45^\circ$ incidence, where IDDES and continuous eddy simulation give
  $C_L=1.231$ and 1.192 against 2.238 for RANS and 1.097 for the reference
  (Table 2); the Ahmed body at $25^\circ$ and $35^\circ$ on
  $45.8\times10^6$ nodes, where the equilibrium wall model suppresses slant
  separation and IDDES with a no-slip condition gives $C_D=0.2819$ at
  $35^\circ$ (Table 3). Details on
  [lattice Boltzmann methods](/methods/lattice-boltzmann-method.md) and
  [immersed boundary methods](/methods/immersed-boundary-method.md).
- **ZDES mode 2 (2020) on lattice Boltzmann grids** (Husson et al. 2024,
  §4): the NASA zero-pressure-gradient
  [flat plate](/benchmarks/turbulent-boundary-layer.md) at
  $Re_L=5\times10^6$, $M=0.2$, with $\Delta y^+\approx30$ and
  $\Delta x\approx0.01\delta$ at mid-plate, where ZDES gives the same $C_f$
  and eddy-viscosity profile as RANS (also with $C_{DES}=0$ and on an inclined
  plate) while DDES (2006) suffers severe modelled-stress depletion (§4.1.2,
  Figs. 4–5); the A3C
  [backward-facing step](/benchmarks/backward-facing-step.md) at
  $Re_h=40\,000$ on $44.7\times10^6$ nodes against the body-fitted
  Navier–Stokes ZDES of Deck & Renard on $3.9\times10^6$ (Table 1), with
  matching vorticity-thickness growth and mean profiles (§4.2.2, Figs. 9–11);
  and the LEISA2 three-element high-lift airfoil at $Re_c\approx1.23\times10^6$
  on $77\times10^6$ nodes against a wall-resolved LES of $2.6\times10^9$
  points, with attached layers kept in RANS, no grid-induced separation and
  $C_p$ in very good agreement with the experiment (§4.3.2, Figs. 13–14).
  The isotropy of the lattice makes the grid locally much finer than the
  Navier–Stokes one: $\Delta z_{NS}\approx10\Delta z_{LBM}$ behind the step
  (§4.2.1). Details on
  [detached-eddy simulation](/methods/detached-eddy-simulation.md) and
  [lattice Boltzmann methods](/methods/lattice-boltzmann-method.md).

## Qualifications

- Cai et al. describe the HRR variant as density-based ("HRR-$\rho$");
  Cheylan et al. describe the regularization as removing the trace of the
  non-equilibrium tensor. Neither prints the collision parameters.
- No source reports run times, core counts or hardware for ProLB;
  Mozaffari et al. (2024) name only the Aix-Marseille computing centre.
- Cai et al. (2022), Cheylan et al. (2023) and Mozaffari et al. (2024)
  share the author Jacob; Husson et al. (2024) are from ONERA and are the
  only ProLB users in the bundle outside that group. They use a development
  branch of the code.
- Husson et al. (2024) print the wall-resolved LES point count of the
  three-element airfoil as $2.6\cdot10^9$ (p. 15) and $2700\cdot10^6$
  (p. 18), and the D3Q19 sum of Eq. (10) over $i=1,\dots,19$ where Eqs.
  (2)–(3) index $i=0,\dots,18$.
- On the $35^\circ$ Ahmed body the two ProLB studies reach different
  verdicts on the wall model (Cai et al. 2022 favour it with their
  constrained-LES enhancement; Mozaffari et al. 2024 find it suppresses
  separation under SST-based hybrids); the turbulence treatments differ,
  see [immersed boundary methods](/methods/immersed-boundary-method.md).

# Citations

- [Cai et al. (2022)](/sources/cai-2022.md) — §II.A, Eqs. (1)–(15) (lattice Boltzmann, HRR, Vreman); §II.B–II.C (immersed boundary, wall model); §III, Tables I–II, Eq. (28) (grids, Mach number); §IV, Table III (results).
- [Cheylan et al. (2023)](/sources/cheylan-2023.md) — §2.1–2.7 (lattice, collision, forcing, immersed boundary, coupling, LES); §3.1–3.4, Tables 9, 13 (verification, turbulent beam).
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — HAL accepted manuscript hal-04921212v1: §1; §2.1–2.3, Eqs. (1)–(34) (lattice, HRR, relaxation time, wall model, SST, IDDES, CES); §3.1–3.3, Tables 1–3 (airfoils, Ahmed body).
- [Husson et al. (2024)](/sources/husson-2024.md) — §2.1, Eqs. (1)–(17) (D3Q19 HRR-BGK, relaxation time); §2.2, Eqs. (18)–(35) (SA, ZDES mode 2 (2020)); §3, Eqs. (36)–(43) (wall law, immersed boundary); §4, Table 1, Figs. 4–19 (flat plate, A3C step, LEISA2 airfoil).

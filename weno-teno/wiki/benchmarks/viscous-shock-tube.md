---
type: Benchmark
title: "Viscous shock tube (Daru–Tenaud)"
description: "Two-dimensional Navier–Stokes shock tube of Daru and Tenaud in a closed box [0,1]×[0,0.5] with a 100:1 density and pressure jump at Reynolds number 1000 and above; the Mach 2.37 shock reflects from the end wall, interacts with the boundary layer and forms a lambda-shock and a primary vortex, a test of viscous discretizations, shock capturing and resolution."
status: established
aliases: [Daru–Tenaud viscous shock tube, viscous shock-tube problem, shock–boundary-layer interaction in a shock tube]
tags: [benchmark, low-dissipation, finite-difference, dg]
timestamp: 2026-10-23T16:00:00Z
---

# Viscous shock tube (Daru–Tenaud)

A closed two-dimensional shock tube is filled with a gas at rest, with
a diaphragm at $x=0.5$ separating a high state on the left from a state
with one hundredth of its density and pressure (equal temperature) on
the right. The shock runs to the right wall, reflects, and meets the
boundary layer that the contact and the shock have left on the bottom
wall. The interaction separates the boundary layer, forms a
lambda-shaped shock foot and rolls the separated layer into a primary
vortex near $x\approx0.75$, with a smaller vortex system near the right
wall. Because the flow is viscous, a grid-converged solution exists at
finite Reynolds number, so schemes can be compared against a fine
reference rather than only against each other. Only the lower half of
the tube is computed, with a symmetry condition on top.

## Data

| | [Chamarthi (2023a)](/sources/chamarthi-2023.md) Ex. 4.1; [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) Ex. 3.10 | [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) §5.2.2 |
|---|---|---|
| domain | $[0,1]\times[0,0.5]$ | $[0,1]\times[0,0.5]$ |
| left state ($x<0.5$), $(\rho,v_1,v_2,p)$ | $(120,0,0,120/\gamma)$ | $(120,0,0,120/\gamma)$ |
| right state | $(1.2,0,0,1.2/\gamma)$ | $(1.2,0,0,1.2/\gamma)$ |
| $\gamma$, viscosity | $\gamma=7/5$, $\mu=1/1000$, $\mathrm{Re}=1000$ | $\mu=10^{-3},\,5\cdot10^{-4},\,2\cdot10^{-4},\,10^{-4}$ |
| boundaries | walls, symmetry on top | no-slip adiabatic walls, slip adiabatic top |
| final time | $t=1$ (also $t=0.5$ in Chamarthi 2023a) | $t=1$ |
| discretization | $1280\times640$ points, conservative finite differences | $\mathbb P_4$ flux reconstruction, $800\times400$ elements |
| reference | grid-converged $4000\times2000$ solution of the cited study | Guermond et al., qualitative |

Chamarthi (2023a) states the shock Mach number as 2.37; the shock-tube
relation for a pressure ratio of 100 between equal-temperature states
of one gas with $\gamma=1.4$ gives a shock pressure ratio of 6.39 and
$M=2.371$ *(compiler check, not in the sources)*.

## Runs and findings

**Viscous fluxes and odd–even decoupling.** Chamarthi (2023a) uses the
case to test the [α-damping viscous flux](/methods/alpha-damping-viscous-flux.md):
with Shen & Zha's sixth-order viscous scheme, which does not damp the
highest wavenumbers, the TENO5 run shows saw-tooth oscillations at
$t=0.5$, while every α-damping run is free of odd–even decoupling
(Figs. 4–5).

**Resolution of the gradient-based schemes.** Among TENO5, MEG6 and MIG4
([gradient-based reconstruction](/methods/gradient-based-reconstruction.md)),
MIG4 comes closest to the fine-grid primary vortex (Chamarthi 2023a,
Fig. 5). Chamarthi (2023b) repeats the case with the seventh-order MEG7:
the seventh-order mapped explicit [WCNS](/methods/weighted-compact-nonlinear-scheme.md)
baseline (WCNS7M) deviates significantly at the primary vortex near
$x=0.75$ and at the right-wall vortex system, and MEG7 is much closer to
the $4000\times2000$ reference (Fig. 13).

**Cost.** This is the most expensive case of both papers. Chamarthi
(2023a, Table 1) prints wall-clock times of 58680 s for TENO5 with
compact viscous gradients (ratio 1.147 to MIG4), 50880 s for TENO5 with
explicit gradients (0.994), 48506 s for MEG6 (0.948) and 51146 s for
MIG4 (1). Chamarthi (2023b, Table 2) prints 35455 s for MEG7-prim,
38062 s for MEG7-cons and 70082 s for WCNS7M, and calls MEG7 "twice as
fast" here because the gradients are shared between the inviscid and
viscous fluxes. Neither paper names the hardware.

**Positivity filtering at higher Reynolds number.** Dzanic & Witherden
run four viscosities with [entropy filtering](/methods/entropy-filtering.md)
in [flux reconstruction](/methods/flux-reconstruction.md): agreement with
Guermond et al. is good, small-scale features are more pronounced at
high Reynolds number, the filter acts sporadically, and about 16
elements need the positivity re-filter after the viscous step, with
filter strength about $10^{-4}$ (Figs. 8–9).

## Qualifications

- All comparisons are visual (density contours, vortex position); no
  error norm is given.
- Chamarthi (2023a) and (2023b) are read as arXiv preprints. In
  Chamarthi (2023a) the text attributes the tridiagonal solve to the
  TENO5/explicit-gradient run, whereas the compact (tridiagonal)
  gradients belong to MIG4; Chamarthi (2023b) prints a normalized
  WCNS7M time of 1.97 for the ratio $70082/35455=1.977$
  *(compiler check, not in the sources)*.
- Dzanic & Witherden compare with a different reference
  (Guermond et al.) at the same and higher Reynolds numbers; their
  results and Chamarthi's are not compared with each other.

# Citations

- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — Ex. 4.1, Table 1, Figs. 4–5 (arXiv v2).
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — Ex. 3.10, Table 2, Fig. 13 (arXiv v1).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §5.2.2, Figs. 8–9.

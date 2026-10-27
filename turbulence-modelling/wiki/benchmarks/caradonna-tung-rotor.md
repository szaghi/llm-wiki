---
type: Benchmark
title: "Caradonna–Tung rotor"
description: "The two-bladed untwisted NACA 0012 model rotor of Caradonna and Tung in hover, collective 8°, tip Mach 0.439 and 0.877: a test of how long a scheme preserves the tip-vortex wake, run with immersed-boundary DDES on moving Cartesian grids and with WENO-type URANS on overset grids."
status: established
aliases: [C-T rotor, Caradonna-Tung rotor, Caradonna and Tung rotor, hovering model rotor]
tags: [benchmark, hybrid-rans-les, des, immersed-boundary, numerical-dissipation, rans]
timestamp: 2026-10-27T11:00:00Z
---

# Caradonna–Tung rotor

The Caradonna–Tung rotor is the two-bladed model helicopter rotor of the
1981 experiment of Caradonna and Tung, run in hover: rectangular,
untwisted blades of [NACA 0012](/benchmarks/naca-0012-airfoil.md) section
and aspect ratio 6, at a collective pitch of $8^\circ$, with surface
pressures measured at five spanwise stations and the trajectory of the
tip vortex measured against its wake age. In hover the blade sheds a tip
vortex that winds into a helix under the rotor disk and must survive
several revolutions in the computation; the integrated loads (thrust,
torque) and the wake structure respond differently to the scheme in
both ingested sources, which use the case to compare inviscid-flux
schemes by the wake they preserve, and Han et al. (2022) attribute the
longer-lived tip vortex to the lowest
[numerical dissipation](/properties/numerical-dissipation.md) (§4.2).
Page-local symbols: $R_{\mathrm r}$
rotor radius, $r$ radial position, $\psi$ wake age (azimuth since the
vortex left the blade), $M_{\mathrm{tip}}$ tip Mach number, $C_{\mathrm{Th}}$ thrust
coefficient, $T_{\mathrm r}$ thrust, $a_\infty$ free-stream sound speed.

## Configuration

| Item | [Sugaya & Imamura (2021)](/sources/sugaya-2021.md), §4 | [Han et al. (2022)](/sources/han-2022-c.md), §2, §4 |
|---|---|---|
| Geometry | 2 blades, $R_{\mathrm r}=45$ in, chord 7.5 in (aspect ratio 6), NACA 0012 | 2 blades, NACA 0012, rectangular, zero twist, aspect ratio 6 |
| Operating point | collective $8^\circ$, 1250 rpm, $M_{\mathrm{tip}}=0.439$, $T=288$ K | collective $8^\circ$, flapping and shaft angles $0^\circ$; $M_{\mathrm{tip}}=0.439$ (subsonic) and 0.877 (transonic) |
| Reynolds number | $4.44\times10^6$ on the chord and the **sonic** speed | $1.92\times10^6$ (subsonic), $3.93\times10^6$ (transonic), basis not printed |
| Closure | DDES-p, a delayed [detached-eddy simulation](/methods/detached-eddy-simulation.md) on the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md) with a modified shielding function for Cartesian grids (not printed); fully turbulent | URANS with the Spalart–Allmaras model (variant not printed) |
| Grid | hierarchical Cartesian grid moving rigidly with the rotor, [immersed boundaries](/methods/immersed-boundary-method.md) with a Spalart–Allmaras wall function; Grid 1 75 M cells (blade root/mid/tip cells $6.0$, $3.0$, $1.5\times10^{-2}$ in), Grid 2 149 M (halved); wake cells 0.24 in on both; first image point at $y^+$ up to about 500 (Grid 1) | dynamic overset grid: static Cartesian background with a uniform orthogonal wake region plus two rotating body-fitted C–H blade grids; 18,057,216 cells ($240\times256\times240$ background, $176\times56\times168$ per blade), first cell $y^+<1$, tip spacing $<0.2\%$ chord, wake cells $<5\%$ chord |
| Inviscid flux | SLAU; MUSCL or the fourth-order (on uniform patches) Tamaki–Imamura quadrature-modification finite-volume scheme extended to moving grids | Roe flux with Harten's entropy fix; third-order MUSCL, fifth-order WENO-JS or WENO-K reconstruction ([WENO scheme](/methods/weno-scheme.md)) |
| Time | dual time stepping, 3600 steps per revolution; 10 revolutions MUSCL with 2 sub-iterations, then 12 with 10 sub-iterations; last 4 averaged | dual time stepping with LU-SGS, $1^\circ$ per step (360 per revolution), 20 sub-iterations, 10 revolutions |
| Reference | the experiment ($C_p$ at $r/R_{\mathrm r}=0.50$, 0.68, 0.80, 0.89, 0.96; tip-vortex trajectory) | the experiment ($C_{\mathrm{Th}}$, $C_p$ at 0.50, 0.68, 0.80, 0.96, trajectory); a 100-million-cell simulation for the vortex-pairing age |

Sugaya & Imamura print
$C_{\mathrm{Th}}=T_{\mathrm r}/(\pi R_{\mathrm r}^2\rho_\infty a_\infty^2M_{\mathrm{tip}}^2)$
and the Figure of Merit $C_{\mathrm{Th}}^{3/2}/(\sqrt2C_Q)$ with $C_Q$ the torque
coefficient and $M_{\mathrm{tip}}=\Omega_{\mathrm{rot}}R_{\mathrm r}/a_\infty$
(§4.5); Han et al. print no definition.

## What the case tests

**Loads are insensitive, the wake is not.** Both sources find the
integrated thrust nearly independent of the scheme and grid in the
subsonic case, while the wake differs strongly.

- [Sugaya & Imamura (2021)](/sources/sugaya-2021.md), Table 7: $C_{\mathrm{Th}}$ and
  Figure of Merit 0.00514 and 0.594 (MUSCL, Grid 1), 0.00518 and 0.611
  (MUSCL, Grid 2), 0.00519 and 0.606 (high-order, Grid 1), 0.00521 and
  0.618 (high-order, Grid 2); grid and scheme "have a small effect" on the
  coefficients, and the time-averaged $C_p$ at the five stations agrees
  with the experiment, almost independent of the grid (§4.5, Figs. 16–17).
- [Han et al. (2022)](/sources/han-2022-c.md), Tables 6–7, against the
  measured $C_{\mathrm{Th}}=0.00459$ (subsonic) and 0.00473 (transonic):

| Scheme | $C_{\mathrm{Th}}$, $M_{\mathrm{tip}}=0.439$ (error) | $C_{\mathrm{Th}}$, $M_{\mathrm{tip}}=0.877$ (error) |
|---|---|---|
| third-order MUSCL | 0.00443 (3.5%) | 0.00512 (8.2%) |
| WENO-JS | 0.00452 (1.5%) | 0.00497 (5.1%) |
| WENO-K | 0.00455 (0.9%) | 0.00487 (3.0%) |

  A MUSCL grid study on 5, 10, 18 and 36 million cells gives $C_{\mathrm{Th}}=0.00410$,
  0.00431, 0.00443 and 0.00447, the last two within 1%, so the 18-million
  grid is retained (§2.5, Table 3). All three schemes match the subsonic
  $C_p$; the WENO suction peaks are closer than MUSCL's, and WENO-K is
  "obviously better" than WENO-JS at $r/R_{\mathrm r}=0.80$ and 0.96
  (Fig. 16).

**How long the tip vortex survives.** [Han et al. (2022)](/sources/han-2022-c.md)
measure it by the wake age up to which a Q-criterion iso-surface tracks
the vortex: subsonic $\psi=900^\circ$ (WENO-K), $630^\circ$ (WENO-JS),
$150^\circ$ (MUSCL); transonic $1000^\circ$, $720^\circ$, $250^\circ$
(§4.1–4.2, Figs. 13, 17). Subsonic "vortex pairing" appears at
$\psi=930^\circ$ with WENO-K and $700^\circ$ with WENO-JS, against
$950^\circ$ in a 100-million-cell simulation they cite (Fig. 15); in the
transonic case no pairing occurs within the visible revolution, which they
explain by the faster descent of the stronger vortices (§4.2, Fig. 19).
WENO-K reproduces the measured trajectory best, "along circumferential
direction" (as printed) after $\psi=200^\circ$ and axially after
$180^\circ$, which Han et al. ascribe to vortex preservation "due to lowest
numerical dissipation" (transonic, §4.2, Fig. 24).
[Sugaya & Imamura (2021)](/sources/sugaya-2021.md) track the vortex core as
the peak of vorticity magnitude: the trajectories of all runs agree with
the experiment "both qualitatively and quantitatively", including the
radial contraction from $0^\circ$ to $300^\circ$ and the steepening of the
vertical descent at $180^\circ$; between $300^\circ$
and $400^\circ$ the radial position changes rapidly with MUSCL and stays
almost constant with the high-order scheme (§4.5, Fig. 18). Their
high-order scheme resolves finer wake vortices than MUSCL and secondary
braid structures entangling two helical vortices, which they note were
reported before in simulations and experiments; "the numerical scheme
greatly affects the prediction of the wake structure" (Fig. 19).

**Cost of the low-dissipation scheme.** The two sources price the gain
differently. [Sugaya & Imamura (2021)](/sources/sugaya-2021.md), Table 6,
report 11 h for the first 10 MUSCL revolutions and 63 h (MUSCL) against
99 h (high-order scheme) for the remaining ones, on 896 (Grid 1) and 1792
(Grid 2) cores of Oakbridge-CX. [Han et al. (2022)](/sources/han-2022-c.md),
Table 5, report 12.5, 14.6 and 15.2 h per revolution for MUSCL, WENO-JS and
WENO-K on 157 processes of TianHe-1(A), and print the increments: WENO-K
costs 4.1% more than WENO-JS and 21.6% more than MUSCL; they summarize the gain as about 40%
less thrust error than WENO-JS and a tip vortex resolved about $270^\circ$
of wake age longer.

**Transonic tip.** At $M_{\mathrm{tip}}=0.877$ a strong shock and unsteady
separation near the blade tip make the tip-vortex strength and position
vary with azimuth and its iso-surface irregular; Han et al. state that
the smooth, regular iso-surfaces of quasi-steady or coarse-grid hover
simulations are "not actually consistent with the reality", without
naming those studies (§4.2, Figs. 20–22). For capturing the shock itself
WENO-K is "only slightly better" than WENO-JS, its advantage being lower
dissipation in smooth regions (Fig. 23); see
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
for the shock–boundary-layer interactions of the bundle.

**Moving bodies on Cartesian grids.** For
[Sugaya & Imamura (2021)](/sources/sugaya-2021.md) the rotor is the
three-dimensional demonstration of an
[immersed boundary method](/methods/immersed-boundary-method.md) on a grid
that moves rigidly with the body: the wall-cell classification and the
image points are computed once, there is no fresh-cell problem, and the
turbulent boundary layer stays in the same cells, so the
[wall function](/methods/rans-wall-function.md) of the stationary solver
carries over (§2.2, Conclusion). Their 2D validations of the same
machinery are on [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md).
[Han et al. (2022)](/sources/han-2022-c.md) instead use body-fitted blade
grids that move through an overset background, with three-layer fringes so
that the five-point WENO stencil keeps its width at overset boundaries
(§2.2, Fig. 5).

**Where the sources agree.** Both report that the thrust coefficient barely
distinguishes the schemes while the wake does. Han et al. attribute the
longer-lived vortex to the lower dissipation of WENO-K (§4.2); Sugaya &
Imamura state that "the numerical scheme greatly affects the prediction of
the wake structure" (Fig. 19). The wall-time price is 4.1% (WENO-K against
WENO-JS, printed) and 57% (the high-order scheme against MUSCL, 99 h
against 63 h *(compiler check, not in the sources)*).

## Qualifications

- The Reynolds numbers are on different bases. Sugaya & Imamura state the
  chord and the sonic speed; Han et al. state no basis, but
  $4.44\times10^6\times0.439=1.95\times10^6$ against their subsonic
  $1.92\times10^6$, and $3.93/1.92=2.05$ against $0.877/0.439=2.00$
  *(compiler check, not in the sources)*.
- The two sources' computed thrust coefficients at $M_{\mathrm{tip}}=0.439$
  differ: 0.00514–0.00521 ([Sugaya & Imamura (2021)](/sources/sugaya-2021.md))
  against 0.00443–0.00455 ([Han et al. (2022)](/sources/han-2022-c.md)),
  about 12% to 14% above the measured 0.00459 that Han et al. print
  *(compiler check, not in the sources)*. Sugaya & Imamura print no
  measured $C_{\mathrm{Th}}$ and compare with the experiment only through $C_p$ and the
  trajectory; Han et al. print no definition of $C_{\mathrm{Th}}$, so whether the two
  normalizations coincide is not established. The numbers are recorded
  side by side, not as a contradiction.
- [Han et al. (2022)](/sources/han-2022-c.md) print the per-revolution
  times of Table 5 2.0 h above 360 times their per-step times (105, 126,
  132 s give 10.5, 12.6, 13.2 h) without explaining the difference
  *(compiler check, not in the sources)*; their percentages follow the
  per-revolution values. Their turbulence closure is SA URANS, and no
  rotation or curvature correction is mentioned.
- [Sugaya & Imamura (2021)](/sources/sugaya-2021.md) do not print the
  DDES-p shielding function, and their "high-order" scheme is fourth order
  only on uniform patches and second order at refinement interfaces, with
  second-order viscous fluxes (§2.3). They state that the conservation
  laws are not strictly satisfied with immersed boundaries (§3.2).

# Citations

- [Sugaya & Imamura (2021)](/sources/sugaya-2021.md) — §1; §2.1–2.3; §4.1–4.5, Tables 5–7, Figs. 14–19; Conclusion.
- [Han et al. (2022)](/sources/han-2022-c.md) — §2.1–2.5, Tables 2–3, Figs. 5, 11; §3.2; §4.1–4.2, Tables 5–7, Figs. 13–24; §5.

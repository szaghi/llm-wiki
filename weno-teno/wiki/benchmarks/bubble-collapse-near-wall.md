---
type: Benchmark
title: "Bubble collapse near a wall"
description: "A gas or vapour bubble in high-pressure liquid next to a rigid wall collapses asymmetrically and forms a wall-directed micro-jet; with pressure ratios of about 350 to 4300 and density ratios of 1000 and above it tests interface sharpness, tensile stability and conservation of compressible multiphase schemes."
status: established
aliases: [cavitation bubble collapse near a wall, CBNW, near-wall bubble collapse, vapour bubble collapse near a wall, gas bubble collapse near a wall, Lauer bubble collapse]
tags: [benchmark, multiphase, interface-capturing, cavitation]
timestamp: 2026-10-23T19:51:00Z
---

# Bubble collapse near a wall

A spherical (in 2D, circular or axisymmetric) bubble of gas or vapour at low pressure sits in
liquid at much higher pressure at a distance $H$ of its centre from a rigid wall, both at rest.
The pressure difference drives a collapse which is asymmetric because the wall slows the
liquid on its side: the far side of the bubble flattens and then inverts into a
**micro-jet** directed at the wall, followed by a vortex ring, rebound and a pressure peak on
the wall. The radius $R$ and the stand-off ratio $H/R$ (page-local) set the regime. No
interface or shock is present initially, so the test isolates the capture of a strongly
compressed, large-density-ratio material interface and of the waves it emits, rather than
shock–interface interaction (for the shock-driven case see
[shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)).

## Setups

| Source | Bubble | Liquid | $R$, $H$ | Domain, grid | Method |
|---|---|---|---|---|---|
| [Jiang et al. (2024)](/sources/jiang-2024.md) §5.2.3 | gas, $(\rho,p)=(1\ \mathrm{kg\,m^{-3}},10^5\ \mathrm{Pa})$, $\gamma=1.43$ | water, $(10^3,3.53\times10^7)$, stiffened gas $\gamma=2.35$, $p_\infty=10^9$ Pa | $R=0.01$ m, $H/R=1.25$ and $2$ | $[-0.25,0.25]\times[0,0.25]$ m, wall at the bottom; about $2.09\times10^6$ particles, $R/\Delta x_0=20$ with $\Delta x_0/8$, or $R/\Delta x_0=40$ with $\Delta x_0/5$, in the local-refinement region | Lagrangian WLS particles with WENO-Z-type reconstruction, GPU |
| [Jiao et al. (2024)](/sources/jiao-2024.md) §4.9 | gas at 3000 Pa, or vapour at 1342 Pa | barotropic liquid (setup after Trummler et al.) | $R=400$ μm, $H=440$ μm | 4 μm cells near the bubble | finite-volume four-equation model, MUSCL-TVD vs THINC with thermodynamic update |
| [Long et al. (2023)](/sources/long-2023.md) §4.5, Eq. (41) | vapour, $(0.0173\ \mathrm{kg\,m^{-3}},0.0234\ \mathrm{bar},293\ \mathrm K)$ | water, $(1004.13,100\ \mathrm{bar},293\ \mathrm K)$ | $R=0.4$ mm, centre at $y=0.416$, $0.140$, $-0.140$ mm (Lauer et al. cases A, B, C) | axisymmetric $10\times10$ mm, wall at the bottom; wavelet multiresolution up to $8192^2$ effective | conservative cut-cell level set with phase change, fifth-order WENO |

The pressure ratio liquid/bubble is $3.53\times10^7/10^5=353$ in Jiang et al. (their
$P_{l0}/P_{b0}$) and $100\ \mathrm{bar}/0.0234\ \mathrm{bar}\approx4270$ in Long et al.
*(compiler check, not in the sources, for the second ratio)*. Jiao et al. print only the
bubble pressures and state that the initial pressure distribution and bubble position are
"similar to" Trummler et al.; they call $H=440$ μm "the distance between the gas or vapor
bubble and the wall" without saying whether it is measured from the centre.
Long et al.'s case C places the bubble centre below the wall ($y=-0.140$ mm with $R=0.4$ mm),
so the bubble is cut by the wall, which is the attached-bubble case of Lauer et al. Jiang et
al. time their results in $t_{\mathrm d}=t/(R/c_{\mathrm L})$ with $c_{\mathrm L}$ the liquid
sound speed.

## Findings across sources

**Micro-jet and asymmetry require low dissipation.** Jiang et al. reproduce, with their
WENO-Z-type reconstruction, the depression of the bubble at $t_{\mathrm d}\approx15.3$ and 17
and a micro-jet faster than 500 m/s at $H/R=1.25$; their Riemann-solver variant without reconstruction
(LWLS-RR) is too dissipative to produce either (Fig. 14). Pressure histories at
$H/R=2$ and $1.25$ agree with SPH-ALE results of the literature, with small differences after
$t_{\mathrm d}>15$ when the jet exceeds 500 m/s; a vortex ring, "apple" and concave-ring shapes
appear, and the asymmetry grows as $H/R$ decreases (Figs. 15–19).

**Interface sharpness under compression.** Jiao et al. compare a second-order MUSCL-TVD
reconstruction with THINC on the gas mass fraction (gas bubble) and on the density (vapour
bubble), both followed by their equation-of-state update of the interface density; the
interfaces stay sharp for both liquid–gas and liquid–vapour collapse with THINC, at 2.06% extra
cost over the original scheme in the gas case (§4.9, §5, Figs. 4.20–4.23; see
[THINC](/methods/thinc-reconstruction.md)). Jiang et al. need an acceleration-based particle
shifting (CPP-II) with local refinement to suppress the tensile instability of the fast
compression; their default shifting (CPP-I), adequate for expanding interfaces, fails here
(Fig. 13).

**Conservation and phase change.** Long et al. run Lauer et al.'s three cases with
evaporation and condensation coefficients 0.01 in a method whose mass, momentum and energy are
conserved through interfacial fluxes of a phase-change Riemann solver
([phase-change Riemann solver](/methods/phase-change-riemann-solver.md),
[level-set method](/methods/level-set-method.md)); they attribute their differences from
Lauer et al. to the thermal non-equilibrium assumption of the latter (§4.5).

## Related tests without a wall

[Wilfong et al. (2026)](/sources/wilfong-2026.md) run two bubble-collapse cases in
[MFC](/software/mfc.md) 5.0 that are not this benchmark, because no wall is present. A
spatially homogeneous ("0D") collapse of monodisperse sub-grid air bubbles of equilibrium
radius 5 mm at liquid-to-bubble pressure ratio $p_\infty/p_{\mathrm b}=1427$ (page-local
symbols) tests time stepping, not interface capture: the unsplit scheme needs
$\Delta t=0.008$ μs and fails at $0.8$ μs with a negative radius, while
[Strang splitting](/methods/operator-splitting.md) with an adaptive embedded third-order
Runge–Kutta sub-step runs at $0.8$ μs (§4.2.3, Fig. 13). A shock-driven collapse of a cloud of
75 resolved 3 mm air bubbles in water on about $2\times10^9$ points is a capability
demonstration, without comparison data (§5.1, Fig. 19; the authors state in §5.5 that
validation rests on earlier work).

## Qualifications

- The three setups differ in the bubble content (non-condensable gas, vapour without and with
  phase change), the liquid model (stiffened gas, barotropic, stiffened gas with phase change)
  and the dimension, so no cross-source comparison of jet speed or wall pressure is possible
  from the printed data.
- Jiang et al.'s local-refinement region for $H/R=1.25$ is centred at $y=0.0135$ m while
  $H=1.25\times0.01=0.0125$ m; the paper does not explain the offset *(compiler check, not in
  the sources: the value of $H$)*.
- Jiang et al. use "CBNW" and "CNBW" for the same test.

# Citations

- [Jiang et al. (2024)](/sources/jiang-2024.md) — §3.3.1, §5.2.3, Figs. 13–19.
- [Jiao et al. (2024)](/sources/jiao-2024.md) — §4.9, §5, Figs. 4.20–4.23.
- [Long et al. (2023)](/sources/long-2023.md) — §4.5, Eq. (41).
- [Wilfong et al. (2026)](/sources/wilfong-2026.md) — §4.2.3, §5.1, §5.5, Figs. 13, 19 (free-field collapses, for contrast).

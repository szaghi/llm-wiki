---
type: Benchmark
title: "Shock–mixing-layer interaction"
description: "Viscous two-dimensional (and three-dimensional) benchmark after Yee, Sandham & Djomehri in which an oblique shock impinges on a spatially developing, periodically forced mixing layer at Re 500, producing vortices, shocklets and acoustic waves; used to test shock detectors and the resolution of low-dissipation schemes."
status: established
aliases: [shock/mixing-layer interaction, shock–shear layer interaction, Yee–Sandham–Djomehri mixing layer, viscous shock–mixing layer]
tags: [benchmark, low-dissipation, turbulence, weno]
timestamp: 2026-10-23T10:00:00Z
---

# Shock–mixing-layer interaction

A spatially developing mixing layer between two parallel streams of
different speed and density is forced at the inlet by two transverse
velocity modes, so that it rolls up into a row of vortices. An oblique
shock enters through the upper boundary, crosses the layer, reflects
from the lower slip wall and interacts with the vortices, which in
turn emit shocklets and acoustic waves. The flow combines a shock,
vortical structures and weak waves in one field, so it tests both the
resolution of a low-dissipation scheme and whether a shock detector
fires on shocklets and stays silent on smooth acoustic waves.

## Data

[Li, Chen & Ren (2022)](/sources/li-2022.md) §4.3.4 and
[Wang et al. (2021)](/sources/wang-2021.md) Ex. 5.10 print the same
setup, attributed by Li et al. to Yee et al. (1999): domain
$[0,200]\times[-20,20]$, Navier–Stokes with $\mathrm{Re}=500$,
$\mathrm{Pr}=0.72$, $t=120$;

- inlet velocity $v_1=2.5+0.5\tanh(2y)$, upper stream
  $(\rho,p)=(1.6374,\,0.3327)$, lower stream $(0.3626,\,0.3327)$;
- post-shock state $(\rho,v_1,v_2,p)=(2.1101,\,2.9709,\,-0.1367,\,0.4754)$
  imposed on the upper boundary;
- inlet forcing $v_2'=\sum_{k=1}^2a_k\cos(2\pi kt/T_{\mathrm f}+\varphi_k)\,e^{-y^2/b}$
  with $a_1=a_2=0.05$, $\varphi_1=0$, $\varphi_2=\pi/2$, $b=10$,
  $T_{\mathrm f}=\lambda_{\mathrm f}/u_c$, $\lambda_{\mathrm f}=30$, $u_c=2.68$
  (page-local forcing period, phases and wavelength);
- inflow on the left, slip wall at the bottom, outflow on the right
  (zero gradient in Li et al.).

The data are consistent *(compiler check, not in the sources)*: with
$\gamma=1.4$ the two streams have sound speeds $0.5334$ and $1.1334$,
the convective velocity $(3c_{\mathrm{low}}+2c_{\mathrm{up}})/(c_{\mathrm{up}}+c_{\mathrm{low}})$
is $2.680$, the printed $u_c$, and the convective Mach number
$(3-2)/(c_{\mathrm{up}}+c_{\mathrm{low}})$ is $0.600$. The post-shock
state is the Rankine–Hugoniot state of an oblique shock with normal Mach
number $1.169$ in the upper stream: the printed pressure ratio $1.4289$
gives a density ratio $1.28868$ against the printed $1.28869$, a shock
angle of $12.0^\circ$ to the stream $(3,0)$, and behind it the velocity
$(2.9709,-0.1367)$, the printed one.

**Three-dimensional extension.** Wang et al. Ex. 5.12 extend the domain
to $[0,200]\times[-20,20]^2$ with symmetric boundaries in $z$ and the
forcing $v_2'=\sum_ka_k\cos\big(2\pi k(t/T_{\mathrm f}+z/L_z)+\varphi_k\big)e^{-y^2/b}$,
$L_z=40$, on $600\times120\times120$ points to $t=120$.

## Runs and findings

| Source | Scheme | Grid | Reference |
|---|---|---|---|
| Li et al. (2022) | MDAD-HY: [minimized-dispersion, adaptive-dissipation](/methods/mdcd-scheme.md) linear scheme hybridized with WENO by their shock detector | $1600\times320$, non-uniform, refined near $y=0$ | none |
| Wang et al. (2021) | [multi-resolution WENO](/methods/multi-resolution-weno.md) (New WENO5) against WENO-JS5, [WENO-AO](/methods/weno-ao.md)5, WENO-ZS5; sixth-order central viscous fluxes | $500\times100$ | seventh-order WENO-JS on $2000\times400$ |

**Detector behaviour.** Li et al. use the case as the robustness test
of their [hybrid](/methods/hybrid-weno.md) detector: it flags the
oblique shock and the vortex-induced shocklets and does not flag the
acoustic waves (Fig. 26).

**Resolution and cost.** Wang et al. compare the schemes on density
contours and a cut at $y=0$ against the fine reference (Figs. 5.16–5.17);
they rank WENO-AO5 below the multi-resolution schemes on this case. In
their cost table New WENO5 takes 1.60 times the time of WENO-JS5 on this
example, and 0.87 times that of WENO-ZS5 (Table 5.8), above the
"9 %–30 %" overhead their text gives for all examples. The 3D extension
is shown in Figs. 5.20–5.21.

## Qualifications

- No source gives an error norm; the comparisons are visual (Wang et al.
  against a finer computation, Li et al. without reference).
- The two runs differ by a factor of about 3 in grid spacing
  ($1600\times320$ against $500\times100$) *(compiler check, not in the sources)* and in grid
  type (uniform against refined near the layer), so their figures
  cannot be compared directly.
- Wang et al. call the 3D case an "extension of the previous Example
  4.10"; the 2D case is their Example 5.10.

# Citations

- [Li, Chen & Ren (2022)](/sources/li-2022.md) — §4.3.4, Fig. 26.
- [Wang et al. (2021)](/sources/wang-2021.md) — Exs. 5.10, 5.12, Table 5.8, Figs. 5.16–5.17, 5.20–5.21.

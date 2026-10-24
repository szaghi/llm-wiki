---
type: Benchmark
title: "Shock–mixing-layer interaction"
description: "Viscous two-dimensional (and three-dimensional) benchmark after Yee, Sandham & Djomehri (also run inviscid) in which an oblique shock impinges on a spatially developing, periodically forced mixing layer at Re 500, producing vortices, shocklets and acoustic waves; used to test shock detectors and low-dissipation schemes; a reacting hydrogen variant tests positivity-preserving DG."
status: established
aliases: [shock/mixing-layer interaction, shock–shear layer interaction, Yee–Sandham–Djomehri mixing layer, viscous shock–mixing layer]
tags: [benchmark, low-dissipation, turbulence, weno]
timestamp: 2026-10-24T05:58:00Z
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
setup, attributed by Li et al. (2022a) to Yee et al. (1999): domain
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
  (zero gradient in Li et al. (2022a)).

[Chamarthi (2023a)](/sources/chamarthi-2023.md) Ex. 4.2 and
[Chamarthi (2023b)](/sources/chamarthi-2023-b.md) Ex. 3.11 print the
same domain, inlet profile, forcing ($a_k$, $\varphi_k$, $b$,
$\lambda_{\mathrm f}$, $u_c$), $\mathrm{Pr}=0.72$, a $12^\circ$ oblique
shock, convective Mach number 0.6 and $t=120$, slip wall at the bottom
and supersonic outlet, without reprinting the stream states;
Chamarthi (2023b) states $\mathrm{Re}=500$ and Chamarthi (2023a)
$\mathrm{Re}=1000$.

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

**Inviscid version.** [Tang (2024)](/sources/tang-2024.md) §4.4.6,
Eq. (38) runs the setup with the Euler equations: the same domain,
inlet profile, upper stream $(1.6374,\,0.3327)$, forcing with
$a_1=a_2=0.05$, $b=10$ and period $30/2.68$, but without printing the
phases $\varphi_k$ or the post-shock state ("the rear shock wave" on
the upper boundary), with a slip wall below and outflow on the right,
and the lower-stream density printed as $0.3636$. With $\gamma=1.4$ the
other sources' $0.3626$ gives $u_c=2.6800$ and a convective Mach number
$0.59998$, Tang's $0.3636$ gives $2.6797$ and $0.6005$: both agree with
$u_c=2.68$ and $0.6$ to the printed digits, the former more closely
*(compiler check, not in the sources)*.

**Three-dimensional extension.** Wang et al. (2021) Ex. 5.12 extend the domain
to $[0,200]\times[-20,20]^2$ with symmetric boundaries in $z$ and the
forcing $v_2'=\sum_ka_k\cos\big(2\pi k(t/T_{\mathrm f}+z/L_z)+\varphi_k\big)e^{-y^2/b}$,
$L_z=40$, on $600\times120\times120$ points to $t=120$.

**Reacting three-dimensional variant.** [Ching et al. (2025)](/sources/ching-2025.md)
§5.5, after an NRL report and Ferrer et al., run a different, reacting
configuration: a vitiated-air stream ($v_1=1634$ m/s, 1475 K,
$Y_{\mathrm O_2}=0.278$, $Y_{\mathrm N_2}=0.552$, $Y_{\mathrm H_2\mathrm O}=0.17$
and radical traces) over a fuel stream ($973$ m/s, 545 K,
$Y_{\mathrm N_2}=0.95$, $Y_{\mathrm H_2}=0.05$) at $94232.25$ Pa, joined by
tanh profiles whose centre and thickness are forced in time and in
$x_3$ (their Eqs. (5.6)–(5.8)); supersonic inflow on the left,
extrapolation on the right, slip walls top and bottom, periodic in
$x_3$ over $1.44$ mm; unstructured tetrahedra, SSPRK3 at CFL 0.5,
detailed hydrogen chemistry. The reacting
[Navier–Stokes](/definitions/multicomponent-euler-equations.md) DG
scheme with positivity and entropy bounds runs on the tetrahedra; the
evidence is qualitative: OH isosurfaces and schlieren show roll-up
upstream of the shock and smaller-scale compression waves (Fig. 5.15).

## Runs and findings

| Source | Scheme | Grid | Reference |
|---|---|---|---|
| Li et al. (2022a) | MDAD-HY: [minimized-dispersion, adaptive-dissipation](/methods/mdcd-scheme.md) linear scheme hybridized with WENO by their shock detector | $1600\times320$, non-uniform, refined near $y=0$ | none |
| Chamarthi (2023a) | [gradient-based](/methods/gradient-based-reconstruction.md) MEG6, MIG4 vs TENO5, all with [α-damping](/methods/alpha-damping-viscous-flux.md) compact viscous gradients | $320\times80$ | none |
| Chamarthi (2023b) | seventh-order MEG7 vs seventh-order mapped [WCNS](/methods/weighted-compact-nonlinear-scheme.md) WCNS7M | $320\times80$ | none |
| Tang (2024) | [TENO-AZ](/methods/adaptive-teno.md) vs TENO-Z, TENO-A, TENO-LAD; finite difference, global LF splitting, TVD-RK3 | $500\times100$; $1000\times200$ at CFL 0.3, 0.5, 0.8 | none |
| Wang et al. (2021) | [multi-resolution WENO](/methods/multi-resolution-weno.md) (New WENO5) against WENO-JS5, [WENO-AO](/methods/weno-ao.md)5, WENO-ZS5; sixth-order central viscous fluxes | $500\times100$ | seventh-order WENO-JS on $2000\times400$ |

**Detector behaviour.** Li et al. (2022a) use the case as the robustness test
of their [hybrid](/methods/hybrid-weno.md) detector: it flags the
oblique shock and the vortex-induced shocklets and does not flag the
acoustic waves (Fig. 26).

**Shear-layer thickness in gradient-based schemes.** Chamarthi (2023a)
finds MIG4 giving the thinnest shear layer of MEG6, MIG4 and TENO5
(Ex. 4.2). In Chamarthi (2023b) all schemes capture the oblique shock
without oscillation and MEG7 resolves the shear-layer vortices better
than WCNS7M (Fig. 14).

**Resolution and cost.** Wang et al. (2021) compare the schemes on density
contours and a cut at $y=0$ against the fine reference (Figs. 5.16–5.17);
they rank WENO-AO5 below the multi-resolution schemes on this case. In
their cost table New WENO5 takes 1.60 times the time of WENO-JS5 on this
example, and 0.87 times that of WENO-ZS5 (Table 5.8), above the
"9 %–30 %" overhead their text gives for all examples. The 3D extension
is shown in Figs. 5.20–5.21.

**Stability margin of adaptive TENO.** Tang finds that the TENO-AZ
resolves "much finer unstable vortices" than the other TENO schemes on
$500\times100$, with 12 density levels in $[0.4,2.4]$ (Fig. 15). On
$1000\times200$, TENO-Z and TENO-LAD fail at CFL 0.3, 0.5 and 0.8,
TENO-A runs at 0.3 and fails at 0.5 and 0.8, and TENO-AZ runs at all
three (Fig. 16). Tang attributes this to the continuity of the new
cut-off threshold against the "jump breaks" of the others' floor-based
thresholds, without testing the attribution; the 0/1 cut-off flag
$\delta_k$ is discontinuous in all four schemes, only the threshold
$C_T$ varies continuously in TENO-AZ *(compiler check, not in the
sources)*. Tang's CPU times on $500\times100$ are 0.821 (TENO-Z), 1.095
(TENO-A), 0.912 (TENO-LAD) and 0.807 (TENO-AZ), hardware an Intel
i7-9700 (Table 6).

## Qualifications

- No source gives an error norm; the comparisons are visual (Wang et al. (2021)
  against a finer computation, Li et al. (2022a) and the Chamarthi papers
  without reference).
- Chamarthi (2023a) prints $\mathrm{Re}=1000$ for a setup the other three
  sources, Chamarthi's companion paper included, run at $\mathrm{Re}=500$; the
  paper does not say whether the value is deliberate. Both are read as
  arXiv preprints.
- Li et al. (2022a)'s and Wang et al. (2021)'s runs differ by a factor of about 3 in grid spacing
  ($1600\times320$ against $500\times100$) *(compiler check, not in the sources)* and in grid
  type (uniform against refined near the layer), so their figures
  cannot be compared directly.
- Tang's run is inviscid, while the setup of Yee et al. that the paper cites
  is viscous ($\mathrm{Re}=500$ in the other sources), so Tang's run is
  not the same problem as theirs; the introduction says
  TENO-Z, TENO-A and TENO-LAD "fail at $CFL\ge0.3$" on $1000\times200$,
  while §4.4.6 has TENO-A running at 0.3.
- Ching et al. print the temperature profile as
  $\tfrac12\big((T_F+Y_O)+(T_F-T_O)\tanh(\cdot)\big)$; by the pattern of
  their velocity and mass-fraction profiles the first term is
  $T_F+T_O$ *(compiler check, not in the sources)*.
- Wang et al. (2021) call the 3D case an "extension of the previous Example
  4.10"; the 2D case is their Example 5.10.

# Citations

- [Li, Chen & Ren (2022)](/sources/li-2022.md) — §4.3.4, Fig. 26.
- [Wang et al. (2021)](/sources/wang-2021.md) — Exs. 5.10, 5.12, Table 5.8, Figs. 5.16–5.17, 5.20–5.21.
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — Ex. 4.2 (arXiv v2).
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — Ex. 3.11, Fig. 14 (arXiv v1).
- [Tang (2024)](/sources/tang-2024.md) — §1, §4.4.6, Eq. (38), Figs. 15–16; §4.4.8, Table 6.
- [Ching et al. (2025)](/sources/ching-2025.md) — §5.5, Table 1, Eqs. (5.6)–(5.8), Fig. 5.15.

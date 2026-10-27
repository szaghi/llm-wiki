---
type: Benchmark
title: "Compressor cascades"
description: "Linear compressor cascades as turbomachinery benchmarks: the low-speed V103 and PVD cascades for laminar separation, bypass transition and corner separation, the NACA65 K48 at Mach 0.67, and the transonic TCTA with an oscillating bow shock, run by transitional DDES, RANS transition and Reynolds-stress models and implicit DG LES."
status: established
aliases: [compressor cascade, linear compressor cascade, V103 cascade, PVD cascade, NACA65 K48 cascade, TCTA, Transonic Cascade TEAMAero, compressor corner separation]
tags: [benchmark, turbomachinery, transition, des, rans, implicit-les]
timestamp: 2026-10-26T20:47:00Z
---

# Compressor cascades

A linear compressor cascade is a row of identical blades in a wind tunnel,
computed over one blade passage with pitchwise periodicity (and spanwise
periodicity when the end walls are left out). Compressor blades turn and
decelerate the flow, so the suction-side boundary layer meets an adverse
pressure gradient: at low free-stream turbulence it separates laminar and
reattaches turbulent (a
[laminar separation bubble](/definitions/laminar-separation-bubble.md)),
under higher free-stream turbulence the pressure side can undergo bypass
transition, and where the blade meets the end wall a three-dimensional
**corner separation** forms. At transonic inlet Mach numbers a bow shock
stands in the passage and interacts with the suction-side layer. The
quantities compared are the blade pressure coefficient $C_p$ (or the
isentropic Mach number), $C_f$ along both sides, transition onset, the
size and topology of the corner separation (against oil-flow images), the
wake total-pressure loss and exit flow angle, and for transonic cascades
the position, amplitude and frequency of the shock oscillation. The
intermittency $\gamma$ of transition models follows the registry
(transition pages only). See
[turbine cascades](/benchmarks/turbine-cascade.md) for the
accelerating-flow counterpart.

## Configurations in the sources

| Item | V103 | PVD | NACA65 K48 | TCTA |
|---|---|---|---|---|
| Sources | [Möller et al. (2024)](/sources/moller-2024.md) | [Li & Liu (2022)](/sources/li-2022.md); [Liu et al. (2024)](/sources/liu-2024.md) | [Liu et al. (2024)](/sources/liu-2024.md) | [Klose et al. (2025)](/sources/klose-2025.md) |
| Profile, origin | NACA-65-based, DLR; experiment Hilgenfeld & Pfitzner at $M=0.67$, $Re=4.5\times10^5$, here at the scaled DNS point of Zaki et al. | prescribed velocity distribution, Cambridge/Rolls-Royce (Gbadebo et al.) | DLR (Liesner & Meyer; Hergt et al.) | DLR, TEAMAero programme |
| Inlet Mach number | 0.1 | about 0.07 | 0.67 | 1.21 |
| Reynolds number | $1.385\times10^5$ on axial chord | $2.3\times10^5$ | $5.6\times10^5$ | $1.35\times10^6$ on chord |
| Inflow | angle 42°, $Tu=3.25\%$ | incidence $-7^\circ$ and $0^\circ$ (Liu et al.), $0^\circ$ (Li & Liu) | design point | angle 145.7°; no inflow turbulence (measured below 1%) |
| Span in the computation | $0.1c_{ax}$ ($c_{ax}$ page-local: axial chord), periodic | half span with end wall | mid-span symmetry with end wall | 5%, 10%, 20% chord, periodic |
| Physics | separation-induced transition (suction side), bypass transition (pressure side) | corner separation; mid-chord laminar bubbles | corner separation; mid-chord bubbles | bow shock oscillating at mid-chord over a laminar or transitional layer with shock-induced separation |
| Methods | DDES-$\gamma$ in [TRACE](/software/trace.md) (second-order finite volume); own WALE LES; DNS of Zaki et al. | steady RANS, [Spalart–Allmaras](/methods/spalart-allmaras-model.md) variants (CFL3D); time-averaged URANS, [Reynolds-stress model](/methods/reynolds-stress-model.md) with and without $\gamma$ ([OpenFOAM](/software/openfoam.md)) | as PVD (Liu et al.) | implicit LES, DGSEM $N=3$ in TRACE; URANS SST with $\gamma$-$Re_\theta$ |
| Grids | DDES 0.68, 1.08, 4.32 M cells, 40 spanwise cells, $y^+<1$; LES 10.86 M | about 1.5 M points in half span, $y^+\approx0.7$ (Li & Liu) | — | 47,319 or 108,564 elements per plane; 54.6 M to 375.2 M degrees of freedom |

The PVD cascade has stagger 14.7°, inlet flow angle 41°, camber 42°, chord
0.1515 m, solidity 0.926 and aspect ratio 1.32; the K48 stagger 112.5°,
inlet angle 132°, camber 48°, chord 0.04 m, solidity 1.82 and aspect ratio
1.0 (Liu et al. 2024, Tables 4–5). The TCTA has pitch 0.065 m, chord 0.1 m
and stagger 135.8° (Klose et al. 2025, §3).

## What the case tests

**Transitional hybrid RANS/LES on the V103.**
[Möller et al. (2024)](/sources/moller-2024.md) (read in the accepted
manuscript) assess DDES-$\gamma$: SST-based
[delayed DES](/methods/detached-eddy-simulation.md) coupled with Menter's
one-equation [$\gamma$ model](/methods/local-correlation-based-transition-model.md),
the $k$ production multiplied by $\gamma$, the DDES destruction by
$\max(0.1,\gamma)$, and the separation-induced extra production of the
RANS $\gamma$ model dropped (§II.B.3, Eqs. 24–25).

- *Fully turbulent DDES* misses the suction-side bubble, produces modelled
  turbulent kinetic energy too early, ends in an open separation near the
  trailing edge, and "transitions" on the pressure side just behind the
  leading edge (§III.B.1, Figs. 5–8).
- *DDES-$\gamma$* agrees with LES and DNS in $C_p$ and the suction-side
  bubble, and $C_f$ is almost the DNS value before transition near
  $x/c_{ax}\approx0.65$, but too low after reattachment. On the pressure
  side it follows RANS-$\gamma$, not the DNS, because the attached layer
  stays in RANS mode (Fig. 10).
- *Free-stream turbulence.* Without inflow turbulence both DDES variants
  let the modelled free-stream intensity collapse ahead of the leading
  edge: the shielding function is 1 in the free stream and the
  shear-layer-adapted length is small, so LES-mode destruction acts there
  (Figs. 11–12). Shur et al.'s synthetic turbulence generator restores it,
  closes the bubble slightly earlier, and carries bypass transition by
  resolved scales ($x=0.3$–$0.55c_{ax}$), although pressure-side $C_f$
  barely changes; the authors warn that judging transition "by surface
  values such as $c_f$ only may lead to wrong conclusions" (§III.B.2,
  Figs. 13–16). See [inflow turbulence generation](/methods/inflow-turbulence-generation.md).
- *Convective-flux blending.* Travin et al.'s dynamic central/upwind
  blending goes fully upwind in both boundary layers; a constant 5% upwind
  share gives the best $C_f$ on both sides, 0% oscillates and suppresses
  the bubble, and 25% (Yin & Durbin's value) damps the synthetic
  turbulence (§III.B.3, Figs. 19–22). The authors caution that bypass
  transition then rests on resolved scales, so the model may act "more
  like an LES model", and that the 5% is another adjustable parameter that
  may need re-tuning for other cases or meshes (pp. 25–26); see
  [numerical dissipation](/properties/numerical-dissipation.md).

**Corner separation in RANS: PVD and K48.**
[Li & Liu (2022)](/sources/li-2022.md) compare Spalart–Allmaras
variants on the PVD cascade at $0^\circ$: SA "largely overpredicts" the
corner separation with a peak $\mu_t/\mu$ above 1100; the helicity
correction is the most accurate and has the lowest peak, about 400;
rotation–curvature and strain-based production variants barely change it;
quadratic constitutive relations improve SA but still overpredict, and
blends inherit both behaviours (§3–4; details on the
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) page).
[Liu et al. (2024)](/sources/liu-2024.md) find that
[$k$-$\omega$ SST](/methods/k-omega-sst-model.md) overpredicts the PVD
corner separation at both incidences, and the fully turbulent SSG/LRR-$\omega$
Reynolds-stress model is "only slightly more accurate". Coupled with the
$\gamma$ model, it resolves the mid-chord laminar bubbles, with $C_p$
plateaus near 45% ($-7^\circ$) and 35% ($0^\circ$) of the axial chord,
gives a corner separation closer to the oil flow and better loss and exit
angle, but still overpredicts it under strong adverse pressure gradient;
on K48 it captures mid-chord bubbles and a better corner topology while
still overpredicting the separation near the trailing edge (Figs. 8–17).
The 3D Reynolds-stress runs do not reach a steady state and are
time-averaged URANS. The two RANS sources agree that linear eddy-viscosity
models overpredict compressor corner separation.

**Transonic buffet in the TCTA.**
[Klose et al. (2025)](/sources/klose-2025.md) (read in the ASME accepted
manuscript) run an [implicit LES](/definitions/implicit-les.md) with
nodal [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md)
($N=3$, entropy-conserving split form, BR1 viscous fluxes) and the
[subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)
of Hennemann et al. in TRACE. The suction-side boundary layer is laminar
up to the bow shock at mid-chord; shocklets running upstream in the
passage intermittently transition the pressure side; the mean flow has a
slender bubble under the shock and an open separation toward the trailing
edge (§4, Figs. 3–4). The shock oscillates at $fc/U_{\mathrm{in}}\approx0.16$
in every run, LES and URANS, against about 0.14 measured, while its
amplitude depends on span and resolution and is under-predicted by more
than half by URANS. Numbers, the span study and the SPOD mechanism are on
the [shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
page. Costs (Table 1): the coarse LES at 10% span used 30,933 CPU hours per
convective time on 8192 ranks, the fine one 152,850 on 16,384 ranks,
against 74.6 for URANS.

**What the sources share.** In every cascade the decisive quantity is
where and how the suction-side layer transitions or separates, and every
source finds that the treatment of the laminar or transitional state
changes the outcome: the $\gamma$ coupling and the inflow turbulence of
the hybrid in Möller et al., the $\gamma$ coupling of the
Reynolds-stress model in Liu et al., and the mostly laminar suction side
that makes the URANS of Klose et al. miss the shock position and
amplitude. Möller et al. and Liu et al. both couple the same
one-equation $\gamma$ model, of Menter et al. (2015), to different hosts.

## Qualifications

- The four configurations differ in Mach number (0.07 to 1.21), Reynolds
  number ($1.4\times10^5$ to $1.35\times10^6$), end-wall treatment and
  modelling level, so their errors are not comparable across sources.
- [Möller et al. (2024)](/sources/moller-2024.md) state "Values of
  $l_{\mathrm{ratio}}<0$ are not possible" (§II.B.1, p. 7). With
  $l_{\mathrm{ratio}}=l_{\mathrm{RANS}}/l_{\mathrm{DDES}}$ (their Eq. 22),
  their Eq. 18 and a shielding function $0<f_d\le1$ (Eq. 19) give
  $\min(l_{\mathrm{RANS}},C_{\mathrm{DES}}\Delta_{\mathrm{SLS}})\le l_{\mathrm{DDES}}\le l_{\mathrm{RANS}}$,
  so the bound is $l_{\mathrm{ratio}}\ge1$ *(compiler check, not in the
  sources)*; they use
  $\kappa$ both for the ratio of specific heats (1.4) and for the von
  Kármán constant, whose value they do not print. Their T3C5 check is on
  the [ERCOFTAC T3 page](/benchmarks/ercoftac-t3-flat-plate.md).
- The TCTA amplitude is not grid-converged in
  [Klose et al. (2025)](/sources/klose-2025.md) (0.172 to 0.231 under
  refinement at fixed span), and they print the frequency as
  $St\approx0.16$ against 0.14 without further explanation than the finite
  span (the tunnel span is $1.68c$).

# Citations

- [Möller et al. (2024)](/sources/moller-2024.md) — accepted manuscript: §II.B.1–3, Eqs. 18–25; §II.D, Fig. 1; §III.A, Tables 2–3, Fig. 3; §III.B.1–3, Figs. 5–22; §IV.
- [Li & Liu (2022)](/sources/li-2022.md) — §2.1, Table 1; §3–4, Table 3, Figs. 3–15.
- [Liu et al. (2024)](/sources/liu-2024.md) — Introduction; Flow solvers; Tables 4–5; Figs. 1, 8–18; Discussion; Conclusions.
- [Klose et al. (2025)](/sources/klose-2025.md) — accepted manuscript: §2–4, Table 1, Figs. 2–4; §5–7, Table 2, Figs. 5–14; §8.

---
type: Benchmark
title: "JAXA Standard Model high-lift configuration"
description: "The JAXA Standard Model, a half-span civil transport in landing configuration from the Third AIAA High-Lift Prediction Workshop at chord Reynolds number 1.96 million and Mach 0.172, on which wall-modelled LES predicts maximum lift within five lift counts on grids of 32 to 185 million cells."
status: established
aliases: [JSM, JAXA high-lift model, HLPW3 JSM]
tags: [benchmark, wmles, separated-flow, gpu, software]
timestamp: 2026-10-25T13:45:00Z
---

# JAXA Standard Model high-lift configuration

The JAXA Standard Model (JSM) is a half-model of a civil transport aircraft
in landing configuration (slat, main element and flap, with slat brackets
and flap-support fairings) tested in the JAXA $6.5\,\mathrm m\times5.5\,\mathrm m$
low-speed wind tunnel and used as the test case of the Third AIAA High-Lift
Prediction Workshop (HLPW3). Near maximum lift the flow combines strong
leading-edge acceleration, laminar-to-turbulent transition close to the
leading edges, and separation at the wing–body juncture, which makes the
lift curve, the maximum lift coefficient $C_{L,\max}$ and the stall
behaviour hard to predict with steady RANS. On this page $\alpha$ denotes the angle of attack (page-local; the registry's $\alpha$ is the DG/FV blending factor). In this bundle the case
documents what [wall-modelled LES](/methods/wall-modelled-les.md) of a
realistic aircraft costs and achieves.

## Configuration

From [Goc et al. (2021)](/sources/goc-2021.md), §2, §3:

- semispan 2.3 m, mean aerodynamic chord $c_{\mathrm{mac}}$ about 530 mm (page-local symbol), free-stream velocity
  about 60 m/s;
- $M_\infty=0.172$, $Re_c=1.96\times10^6$ on the mean aerodynamic chord,
  calorically perfect gas, $Pr=0.70$, $\gamma=1.4$;
- peak local Mach number about 0.75 on the slat near maximum lift;
  $Re_\tau\approx5000$ from the peak skin friction and the 99% boundary-layer
  thickness of the LES;
- two variants: **free air** without nacelle and pylon, and **in tunnel**,
  with tunnel walls (wall-modelled), the 70 mm peniche offset and a
  flow-through nacelle, the tunnel extruded about five fuselage lengths
  upstream and downstream, plug inflow and non-reflecting outflow;
- reference data: JAXA experiments (Yokokawa et al. 2006, 2008, 2010):
  corrected integrated forces, uncorrected surface pressures at five
  semispan stations (semispan fractions 0.16 to 0.77) and oil-flow visualizations.
  The experimental repeatability at maximum lift is $C_L=0.03$, $C_D=0.0015$.

Statistics are averaged over 30 flow-through times $c_{\mathrm{mac}}/U_\infty$
(40 after stall, because of low-frequency load oscillations).

## Runs

[Goc et al. (2021)](/sources/goc-2021.md) use two low-dissipation codes with
the [equilibrium wall model](/methods/equilibrium-wall-model.md):
[CharLES](/software/charles.md) (compressible finite volume on Voronoi
grids) and Alya (incompressible Galerkin finite elements). The SGS model is
the [Vreman model](/methods/vreman-model.md) in free air and the dynamic
Smagorinsky model ([dynamic procedure](/methods/dynamic-procedure.md)) in the
tunnel. Grids:

| Code | Variant | Grids | Resolution measure |
|---|---|---|---|
| CharLES | free air | 9, 32, 157 M cells | about 10 cells across $\delta_{99}$ at the trailing edge of the main element on the 32 M baseline, isotropic |
| Alya | free air | 30 M, 180 M; 2 B at $\alpha=21.57^\circ$ | about 5 and 10 elements across the boundary layer |
| CharLES | in tunnel, nacelle on | 10, 42, 185 M cells | isotropic refinement near wing and fuselage |

Results (§3, Figs. 5–14):

- *Free air.* Both codes agree before stall ($\alpha<19^\circ$). CharLES
  approximately predicts $C_{L,\max}$ and stall onset; Alya shows a deeper
  stall at baseline resolution, and its 180 M grid lies within experimental
  repeatability at all angles. Sectional $C_p$ at $\alpha=18.58^\circ$
  agrees with experiment on the finer grids, so the lift agreement is not
  error cancellation. Drag shows a persistent shift $\Delta C_D\approx0.03$
  against corrected tunnel data, also present in all HLPW3 submissions, and
  the pitching moment misses the post-stall "kink" caused by inboard
  separation.
- *In tunnel.* With tunnel walls, peniche and nacelle, the medium and fine
  grids converge $C_L$ to within repeatability at maximum lift, the fine grid
  converges drag to the uncorrected experiment, and the pitching-moment
  kickback and the inboard separation at $21^\circ$ appear, with an angle
  shift of about $1^\circ$. The authors attribute the free-air drag shift to
  the uncertainty of the wind-tunnel corrections.
- *Open problem.* On the finest in-tunnel grid a flap separation bubble,
  present in the experiment and on coarser grids, collapses and lift is
  over-predicted in the linear range; the authors leave cause and remedy
  open and note a similar collapse under refinement reported by Iyer & Malik
  for a Gaussian bump.
- Friction drag is at most about 10% of total drag (about 5% at the highest
  angle).

The headline claim is $C_{L,\max}$ "consistently being predicted to within
five lift counts", with $\Delta C_L\le0.03$ and $\Delta C_D\le0.0010$ at
maximum lift (Abstract, §1). The authors contrast this with the scatter of
the HLPW3 RANS submissions (35 participants, 79 data sets, mostly
Spalart–Allmaras or $k$-$\omega$ SST) near maximum lift, as recalled from
Rumsey et al. (2019).

## Cost

From [Goc et al. (2021)](/sources/goc-2021.md), §4, Tables 1–2,
$\alpha=18.58^\circ$, 30 flow passes:

| Code | Cells | Core-hours per flow pass | Wall-clock |
|---|---|---|---|
| CharLES | 32 M | 1.4k | 21 h on 2000 Ivy Bridge cores; 48 min on 96 V100 GPUs |
| CharLES | 157 M | 12.3k | 7.5 days on 2000 cores; 7 h on 96 GPUs |
| Alya | 30 M | 0.22k | 9 h on 720 CPUs |
| Alya | 180 M | 4.26k | 63 h on 2016 CPUs |
| Alya | 2000 M | 111.11k | 35 h on 96,000 CPUs |

A medium-grid LES (about $40\times10^3$ core-hours) costs about as much as an
HLPW3 steady RANS run in OpenFOAM with Spalart–Allmaras on 109 M cells (about
$60\times10^3$); the fine grid costs about six times more. Voronoi grid
generation is negligible (157 M cells in about two minutes on $10^3$ cores).
The authors scale the WMLES grid count as $N\propto Re_c$ (after Choi &
Moin 2012) and, accounting for the reduction of the time step, the cost as
$Re_c^{4/3}$, and conclude that WMLES of
high-lift aircraft is "on the threshold of readiness for industrial use"
(§4–5). See [grid-point requirements](/results/les-grid-point-requirements.md).

## Qualifications

- The caption of Table 2 places the Alya grid sequence, including the
  2000 M row, at $\alpha=18.58^\circ$, while §3.2 and the Fig. 6 and 10
  captions place the 2 B refinement after stall, at $\alpha=21.57^\circ$.
- 12.3k core-hours per pass over 30 passes on 2000 cores is 184.5 h, about
  7.7 days, against the printed 7.5 days; and ideal linear scaling of the
  157 M case to the stated strong-scaling limit ("nearly $80\times10^3$
  cores and 160 GPUs") gives about 4.6 h from 184.5 h on 2000 cores and
  about 4.2 h from the printed 7 h on 96 GPUs, both above the printed "<4 h"
  *(compiler check, not in the sources)*.
- §4 attributes the WMLES grid scaling $N\propto Re_c$ to "Choi and Moin
  (1994)", the time-step paper, and later in the same section to Choi &
  Moin (2012).
- The case is wind-tunnel-specific: the free-air and in-tunnel results
  differ in drag, pitching moment and inboard separation, so comparisons
  must say which variant and which (corrected or uncorrected) data they use.

# Citations

- [Goc et al. (2021)](/sources/goc-2021.md) — §1–5, Eqs. (2.1)–(2.6), Tables 1–2, Figs. 1–15.

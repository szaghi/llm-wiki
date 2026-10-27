---
type: Benchmark
title: "ACAT1 fan stage"
description: "The ACAT1 fan and outlet-guide-vane stage of the TurboNoiseBB project, run at approach (tip relative Mach 0.57) with hot-wire wake data between rotor and stator: a test of zonal DES and of wall-modelled LES on 95 to 380 million cells for the rotor wakes that drive broadband interaction noise."
status: established
aliases: [ACAT1, ACAT1 fan-OGV stage, TurboNoiseBB fan stage, AneCom UFFA fan rig]
tags: [benchmark, turbomachinery, aeroacoustics, wmles, des, hybrid-rans-les]
timestamp: 2026-10-27T15:50:00Z
---

# ACAT1 fan stage

The ACAT1 stage is a modern turbofan fan with 20 rotor blades followed by
44 outlet guide vanes (OGV) in the bypass duct, tested in the AneCom UFFA
rig at Wildau within the EU project TurboNoiseBB. At the approach operating
point the rotor turns at about 3828 rpm with a tip relative Mach number of
0.57, close to surge, with a short rotor–stator gap (about one fan chord in
François et al., about 1.3 rotor mid-span chords in Lewis et al.).
The case is used to predict the turbulent rotor wakes that impinge on the
vanes, the source of rotor–stator interaction (RSI) broadband noise, so the
quantities a simulation must reproduce are the mean and rms velocity in the
wakes at the interstage hot-wire plane (called HW1 in both sources), their
spectra, the global performance, and the separations on rotor and vanes. In
this bundle two sources run it: a zonal
[detached-eddy simulation](/methods/detached-eddy-simulation.md) and two
[wall-modelled LES](/methods/wall-modelled-les.md), both against the same
measurements and against $k$-$\omega$ SST RANS.

## Configuration

| Item | [François et al. (2022)](/sources/francois-2022.md) | [Lewis et al. (2023)](/sources/lewis-2023.md) |
|---|---|---|
| Rotational speed | 3828.4 rpm | 3828.2 rpm |
| Tip Mach number | $M_{tip}=0.57$ (not defined) | tip relative Mach 0.57 |
| Fan radius | outer radius 0.42 m | tip radius 0.435 m; hub radius at rotor leading edge 0.138 m |
| Chords | – | rotor 0.136 m, stator 0.066 m at mid-span; tip gap 0.78 mm; gap about $1.3$ rotor chords |
| Bypass ratio | "about six" | 7.6 (total mass flow 55.156 kg/s) |
| Blade-count reduction | OGV 44 → 40 at constant solidity (chord +10%) | OGV 44 → 40, rescaled after Rai & Madavan (about +9% axial and azimuthal), solidity, thickness-to-chord and camber kept |
| Domain | 1 fan + 2 OGV channels, periodic; inlet 4 fan chords upstream, outlet 3 vane chords downstream | 18° sector (1 blade, 2 vanes); 4 fan axial chords upstream to 6 vane axial chords downstream |
| Solver | elsA, cell-centred finite volume, AUSM with third-order limiter, implicit second order with 5 Newton sub-iterations | AVBP, cell-vertex finite volume, Lax–Wendroff second order, CFL 0.7 |
| Model | ZDES mode 2 with Spalart–Allmaras (URANS in the core flow and upstream, ZDES in the bypass) | WALE SGS model; linear/log wall law switching at $y^+=11$ |
| Rotor–stator coupling | sliding mesh | overset grids coupled through CWIPI |
| Inlet | radially non-uniform stagnation pressure fitted to hot-wire data, sponge layers | measured total pressure and temperature, axial flow, no turbulence injection, NSCBC |
| Grid | structured, 380 M cells, first cell $y^+=1$, 0.5 mm free-shear cells | LES1 95 M and LES2 210 M cells (prisms and tetrahedra), 8 and 14 prism layers |
| Time step | $3.2\times10^{-7}$ s (2400 per blade passage) | $3.7\times10^{-8}$ s (LES1), $2.75\times10^{-8}$ s (LES2) |
| Statistics | 36 blade passages (about 1.8 revolutions) after a two-revolution transient | about three rotations (LES2) |
| Cost | about 2 million CPU hours on 672 cores | not printed |

Both sources reduce the OGV count from 44 to 40 so that the domain becomes
periodic over an 18° sector; François et al. reject Fourier phase-lag
conditions as "unadapted for the convection of broadband structures", and
both rely on an earlier RANS study showing little effect of the rescaling
([François et al. (2022)](/sources/francois-2022.md), §3.2.2;
[Lewis et al. (2023)](/sources/lewis-2023.md), §3.1).

The measurements, from the rig campaign of Meyer et al. that both sources
cite, are hot-wire velocity at HW1 (360° phase-averaged maps split into
the 20 fan channels), global mass flows and pressure ratio, and acoustic
arrays in the inlet, interstage and bypass and on a far-field arc. The hot
wires cut off at about 8.5 kHz (François et al., §5.2) or about 8 kHz
(Lewis et al., §4.3.2). François et al. multiply the measured rms by 1.5 to
correct for it; Lewis et al. (§4.3.2) cite Polacsek et al.'s estimate that the
measured rms is underestimated by a factor of about 1.5, warn that the
factor was estimated at only two radial positions, and plot the corrected
data separately (Fig. 25).

## What the case tests

**Global performance.** [François et al. (2022)](/sources/francois-2022.md),
Table 1, match core and bypass mass flows and the bypass pressure ratio
within 0.4%, after raising the bypass back-pressure and adding the inlet
stagnation-pressure profile (their earlier run had a 1% mass-flow error).
[Lewis et al. (2023)](/sources/lewis-2023.md), Tables 9–10, find RANS and
the coarser LES1 close to the measured performance (LES1: total mass flow
+0.05%, total fan pressure ratio −0.36%), while the finer LES2 over-predicts
the mass flow by 2.7%,
which they attribute to its changed stator flow topology.

**Separation and its sensitivity to the wall mesh.**
[Lewis et al. (2023)](/sources/lewis-2023.md), §3.3 and §4.2, give a
quantitative warning for wall-modelled LES of turbomachinery. Both of their
meshes are said to meet the wall-mesh requirements of WMLES (streamwise
$100<\Delta x^+<600$, spanwise $100<\Delta z^+<300$, wall-normal
$30<y^+<150$, from Piomelli and Wagner et al.; Table 5), yet LES1 shows a
large separation from about 65% of the stator chord over almost the whole
span, with a radial vortex, that disappears on LES2. The authors conclude
that "wall laws should be used with caution since wall-mesh requirements for
WMLES are actually quite broad", and that even a WMLES able to predict large
detachments may misplace the detachment and reattachment points. Both LES
and RANS show a rotor leading-edge separation with an intermittent radial
vortex, over about 80% of the span in the LES and from 40% of the span to
the tip in RANS (Figs. 12, 16); RANS misses the radial secondary flows of
the LES. See [LES grid-point requirements](/results/les-grid-point-requirements.md).

**Hybrid RANS/LES shielding.** In the ZDES of
[François et al. (2022)](/sources/francois-2022.md), §4.2, the shielding
function keeps both blade boundary layers in RANS mode and switches quickly
to LES at the trailing edges, and the fan wakes cross the sliding interface
and the periodic boundaries "without noticeable attenuation or numerical
artefact". Placing the URANS/ZDES border so that every streamline from the
fan into the bypass is in ZDES is required, otherwise part of the wakes
reaching the OGV stays RANS-like (§3.2.1). The authors state, without a cost
comparison, that the 0.5 mm free-shear cells they need would cost more cells
in a WMLES.

**Wake profiles at the interstage plane.**
[François et al. (2022)](/sources/francois-2022.md), §5.3–5.4, Figs. 12–15:
the ZDES over-predicts the mean axial and tangential velocity by less than
3% and the radial velocity by 5–10 m/s; the three rms components and the
turbulent kinetic energy lie within the measurement band, notably in the tip
gap; the wake width is "very consistent" with measurement, the
velocity-deficit depth over-predicted by 10–15% and the rms peak by 15% on
average. RANS ($k$-$\omega$ SST and Smith $k$-$l$, with rms rebuilt through
the [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)) gives
narrower wakes and doubles the main dip in the tip gap.
[Lewis et al. (2023)](/sources/lewis-2023.md), §4.3, Figs. 19–24: the
mean and rms wake profiles improve from LES1 to LES2; at 95% span only LES2
recovers the measured rms; LES profile shapes reproduce the measured rms
shapes better than RANS. The axial-velocity spectrum at 50% span is too high
by 5–10 dB between 1 and 5 kHz on LES1 and by less than 5 dB, falling to
2 dB above 4 kHz, on LES2. On LES1 the wakes widen abruptly at the
rotor–stator domain interface, where the mesh coarsens (§4.4.1, Fig. 26).

**Comparison of the two approaches.** [Lewis et al. (2023)](/sources/lewis-2023.md),
§4.1 and §4.3.2, compare their LES with the ZDES of François et al.: the
ZDES, with a total-pressure inlet profile, adjusted outlet pressure,
reflective boundaries with sponges, recovers the mass flow better and the rms
levels better, but shows a secondary peak of the streamwise rms absent from
the experiment. [François et al. (2022)](/sources/francois-2022.md), §5.2,
report measured background turbulence outside the wakes that no simulation
of the project reproduces, and Lewis et al.
judge the common trends of the simulations "more consistent than the
experimental values" (§4.3.1).

**Noise sources.** [Lewis et al. (2023)](/sources/lewis-2023.md), §5,
feed the LES wall pressure to Ffowcs Williams–Hawkings and Goldstein
analogies; with an indicative rotor-shielding correction LES2 agrees with
the measured sound power, and rotor self-noise above 8 kHz is comparable to
stator noise, which questions the assumption that RSI alone dominates fan
broadband noise at approach. The authors state that a mesh as fine as LES2
is "mandatory" for reliable results with this approach. The acoustic part of
the work is outside this bundle and is recorded on the Source page.

## Qualifications

- The two sources print slightly different values for the same rig and
  operating point: 3828.4 rpm against 3828.2 rpm, a fan outer radius of
  0.42 m against a tip radius of 0.435 m, and a bypass ratio of "about six"
  against 7.6. The measured mass flows agree within rounding (bypass 48.76
  against 48.745 kg/s, core 6.41 against 6.411 kg/s), and the ratio of
  François et al.'s measured bypass and core mass flows, $48.76/6.41=7.6$,
  equals Lewis et al.'s bypass ratio *(compiler check, not in the sources)*.
  The interstage gap is "about one fan chord" in François et al. and
  $\approx1.3$ rotor mid-span chords in Lewis et al. (Table 1). Neither
  source comments on the other's values or states the definitions behind
  its own.
- [François et al. (2022)](/sources/francois-2022.md) were read in an ASME
  accepted manuscript; their $M_{tip}=0.57$ is not defined. The blade tip
  speed from their rotational speed and radius is
  $2\pi\cdot0.42\cdot3828.4/60\approx168$ m/s, and divided by the
  normalization velocity $V_{adim}=343.0$ m/s they print for Fig. 8 it gives
  about 0.49 *(compiler check, not in the sources)*; Lewis et al. name the
  same 0.57 a "tip relative Mach number".
- [Lewis et al. (2023)](/sources/lewis-2023.md) were read in a HAL accepted
  manuscript. The mean wall spacings they print (mean $y^+$ 25 and 17,
  mean wall-parallel spacing 80 and 64 for LES1 and LES2, Table 6) lie below
  the lower bounds of the WMLES ranges of their Table 5, although the text
  says the meshes satisfy them; the paper does not reconcile the two. Their
  Table 9 prints the LES2 total mass flow as
  56.647 kg/s while bypass plus core gives 56.608 *(compiler check, not in
  the sources)*.
- Neither source gives a Reynolds number for the case beyond "around one
  million" ([François et al. (2022)](/sources/francois-2022.md), §1).

# Citations

- [François et al. (2022)](/sources/francois-2022.md) — §2; §3.1–3.6, Figs. 2–7; §4.1–4.2, Figs. 8–9; §5.1–5.4, Table 1, Figs. 10–15; Appendix.
- [Lewis et al. (2023)](/sources/lewis-2023.md) — §3.1–3.4, Tables 1–8; §4.1–4.4, Tables 9–10, Figs. 12–26; §5.1, §5.3, Figs. 27–43; §6.

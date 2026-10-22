---
type: Benchmark
title: "Shock-induced combustion and detonation"
description: "Reacting-flow validation cases with detailed hydrogen chemistry: Lehr's ballistic blunt-body experiments, where the oscillation frequency of the shock-induced combustion front is measured; a one-dimensional reflected-shock detonation; and two-dimensional cellular H2–O2–Ar detonations judged by front speed and cell size."
status: established
aliases: [shock-induced combustion, Lehr blunt-body experiment, blunt-body shock-induced combustion, cellular detonation, H2–O2–Ar detonation, reflected-shock detonation]
tags: [benchmark, reacting-flows, bound-preserving, immersed-boundary]
timestamp: 2026-10-22T20:00:00Z
---

# Shock-induced combustion and detonation

These cases solve the reacting
[multicomponent Euler or Navier–Stokes equations](/definitions/multicomponent-euler-equations.md)
for hydrogen mixtures with detailed finite-rate chemistry. Unlike most
benchmarks of the bundle, two of them have experimental data behind
them: the oscillation frequency of the combustion front ahead of a blunt
projectile (Lehr's ballistic-range experiments) and the cell size of a
gaseous detonation. They test the coupling of a shock-capturing scheme
with stiff chemistry, the preservation of positive densities, pressures
and mass fractions, and, for geometry, the treatment of a curved wall
on a Cartesian or a body-fitted mesh.

## Blunt-body shock-induced combustion (Lehr)

A projectile with a hemispherical nose flies into a combustible
hydrogen mixture; the bow shock ignites it, and at subdetonative speeds
the reaction front behind the shock oscillates periodically, at a
frequency Lehr measured. Two sources compute it:

| | [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) §4 | [Wang et al. (2022)](/sources/wang-2022.md) §3.6 |
|---|---|---|
| Mixture | stoichiometric H$_2$–air, 293 K, 42 663.04 Pa | H$_2$:O$_2$:N$_2$ = 2:1:3.76, 298 K, 42.663 kPa |
| Speed | Mach 4.18, 4.48 (subdetonative), 5.04 (superdetonative) | 1931 m/s, stated to equal the Chapman–Jouguet speed |
| Geometry | axisymmetric half domain, polar body-fitted mesh, nose radius 7.5 mm | Cartesian $18\times12$ mm, nose radius 7.5 mm, wall by a ghost-cell [immersed boundary](/methods/immersed-boundary-method.md); planar or axisymmetric not stated |
| Chemistry | modified Jachimowski (9 species, 19 reactions) and UCSD 2016 | 12 species, 42 reactions |
| Scheme | MUSCL–Hancock, AUSM or hybrid Roe/HLL, three adaptive levels in [AMROC](/software/amroc.md), finest 3.5 µm × 4.375 µm | MUSCL–Hancock, HLL, uniform $1920\times2880$ cells (6.25 µm) |
| Measured frequency | 148, 425, 1040 kHz | 725 kHz |

**Frequencies.** Peng et al. measure the oscillation of the H$_2$O mass
fraction at the stagnation point (FFT resolution 5 kHz) and obtain, at
Mach 4.18 and 4.48, 160 and 425 kHz (Jachimowski, AUSM), 165 and
430 kHz (Jachimowski, Roe/HLL), 145 and 395 kHz (UCSD, AUSM) and 155 and
395 kHz (UCSD, Roe/HLL), against 148 and 425 kHz measured (Table 5). The
UCSD mechanism fits Mach 4.18 better and Jachimowski Mach 4.48, where
UCSD couples a high- and a low-frequency mode. At Mach 5.04 they obtain
1155 kHz against 1040 kHz, and refining the mesh destabilizes the run
(the reaction front couples with the bow shock and a detonation forms),
which they attribute to the missing physical viscosity and to errors of
detailed chemistry (Fig. 21). Wang et al. measure the pressure
oscillation and obtain 707.2 kHz with the baseline ghost-cell wall and
714.8 kHz with their hybrid reconstruction, errors of 2.5 % and 1.4 %
against 725 kHz; only the hybrid wall treatment reproduces the
alternating entropy and compression waves between bow shock and
combustion front (Fig. 19).

**Resolution.** Peng et al. find that without refinement (14 µm) the
front oscillates at a wrong 40 kHz and the bow-shock oscillation is
lost; two or three levels give 160 kHz and four levels 155 kHz, so three
are used (Figs. 13–15). The bow-shock stand-off distance is "nearly the
same" as in Lehr's schlieren images (Fig. 16). The cost of refinement
is on the [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
page.

## Detonations

**One-dimensional reflected-shock detonation.**
[Du & Yang (2022)](/sources/du-2022-b.md) Ex. 6.4, after Fedkiw et al.:
a shock in an H$_2$/O$_2$/Ar mixture (molar 2:1:7) reflects from a wall;
after an induction delay a reaction wave starts at the wall, catches the
shock and splits into a rarefaction, a contact and a shock. States
$(\rho,v,p)=(0.072\ \mathrm{kg/m^3},0,7173\ \mathrm{Pa})$ for $x\le6$ cm
and $(0.18075\ \mathrm{kg/m^3},-487.34\ \mathrm{m/s},35594\ \mathrm{Pa})$
otherwise, 12 cm, $t=190\,\mu$s; 9 species, 37 irreversible reactions,
calorically perfect gases; DG of degree 2 on 400 cells. The bounds are
preserved, with "some numerical oscillations" because only the
bound-preserving limiter is applied (Figs. 6.4–6.5).

**Two-dimensional cellular H$_2$–O$_2$–Ar detonation.** Both Du & Yang
(Ex. 6.6) and Peng et al. (§3.4) run the Westbrook mechanism (9 species,
34 reactions) in a 2:1:7 mixture:

- Du & Yang: a channel 0.06 m high with walls on all sides; burnt gas at
  $5.5\times10^5$ Pa and 3500 K for $x<0.015$ m, a layer at 350 K, fresh
  mixture at 298 K and $6.67\times10^3$ Pa ahead, and two hot spots of
  radius 2.5 mm; DG of degree 1 on 1 mm squares, outputs to
  $150\,\mu$s. Transverse waves and a cellular front form
  (Figs. 6.6–6.7). Higher degrees need a further oscillation limiter,
  left to future work.
- Peng et al.: a channel $1000\times32$ mm at 298 K and 10 kPa, a ZND
  profile with its front at $x=46$ mm, base mesh $2000\times128$ with
  five levels (Table 1). The detonation speed is 1645.24 m/s on a
  Cartesian and 1641.82 m/s on a stretched mapped mesh, against a
  Chapman–Jouguet speed of 1629.34 m/s; the cells are 8–10 mm wide,
  against 11.4 mm from a correlation and about 40 mm in experiments, a
  gap they attribute, after others, to wall heat losses in the
  experiments (Fig. 11).

**Reconstruction on detonations.** As reproduced in
[Fu (2023)](/sources/fu-2023.md) §5.2 (Fig. 18), fifth-order
[TENO](/methods/targeted-eno.md) captures the cellular structure of a
two-dimensional self-sustained detonation on coarse meshes better than
WENO5-JS and [mapped WENO](/methods/mapped-weno.md), and WENO5-JS gives
incorrect cellular structures.

## Qualifications

- Peng et al.'s Lehr cases are run on the inviscid model; at Mach 5.04
  their run becomes unstable when the mesh is refined, so that case has
  no converged frequency. Wang et al. run one mesh.
- The two blunt-body sources measure different signals (H$_2$O mass
  fraction at the stagnation point; pressure) at different flight
  conditions; their frequencies are not comparable with each other.
  Peng et al.'s conclusion speaks of pressure oscillation frequencies,
  while their §4.1 and Table 5 are for the H$_2$O mass fraction.
- Peng et al.'s figure of 56.2 points per induction length (0.878 mm)
  holds for the finest cells in the cross-stream direction; along the
  channel their base cells are twice as long, which gives about 28
  points *(compiler check, not in the sources)*.
- Du & Yang give the 2D composition as ratios of mass fractions
  ($Y_{\mathrm{Ar}}:Y_{\mathrm O_2}:Y_{\mathrm H_2}=7:1:2$), while the 1D
  cases state a 2:1:7 molar ratio of H$_2$/O$_2$/Ar; the paper does not
  say whether the 2D mixture differs. They also print the hot spots as
  circles (equalities) rather than discs.
- Du & Yang's proven time-step condition is not the one run: the runs
  restart a step with stronger damping and a halved step when a cell
  average leaves the admissible set (see
  [multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)).

# Citations

- [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) — §3.4, Table 1, Figs. 9–11; §4, Tables 2–5, Figs. 12–21 (accepted manuscript).
- [Wang et al. (2022)](/sources/wang-2022.md) — §3.6, Fig. 19.
- [Du & Yang (2022)](/sources/du-2022-b.md) — §6, Ex. 6.4, 6.6, Figs. 6.4–6.7.
- [Fu (2023)](/sources/fu-2023.md) — §5.2, Fig. 18 (reproduced result).

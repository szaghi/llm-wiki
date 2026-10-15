---
type: Method
title: "Boundary-layer bleed for intake control"
description: "Removes low-momentum boundary-layer fluid through a wall slot at a shock impingement to suppress interaction-induced separation in an intake; on a Mach-4 inward-turning intake a 20 mm slot bleeding about 2.5% of the captured mass removed a throat normal shock and raised the sustainable back-pressure ratio from 73.4 to 76.7."
status: established
aliases: [bleed control, slot bleed, boundary-layer suction, bleeding control]
tags: [inlet, bleed, swbli, flow-control, unstart]
timestamp: 2026-10-14T00:00:00Z
---

# Boundary-layer bleed for intake control

Bleed removes part of the boundary layer through a slot or porous wall
section, so that a
[shock-wave/boundary-layer interaction](/definitions/shock-wave-boundary-layer-interaction.md)
at that station meets a thinner, fuller layer and separates less. In an
intake the aim is a cleaner throat flow, a higher total-pressure recovery
$\sigma_0$ and a larger back-pressure margin before
[unstart](/definitions/inlet-start-and-unstart.md).

## Sizing and placement rules (attributed)

Stated by [Zuo & Huang (2018)](/sources/zuo-2018.md), §3.3, with
attribution:

* slot streamwise length between $\delta$ and $2\delta$ of the local
  turbulent boundary layer (Schulte et al.);
* a slot width at least equal to the incoming boundary-layer thickness,
  removing 20–30% of the incoming boundary-layer mass flow, eliminates
  turbulent boundary-layer separation (Hamed et al.);
* place the slot where the Prandtl–Meyer turning angle is below 45°, so
  that the main stream does not spill through it (stated, no attribution).

## Application to an inward-turning intake

[Zuo & Huang (2018)](/sources/zuo-2018.md), §3, apply a single
streamwise slot to a section-controllable inward-turning intake (design
and geometry in
[Inward-turning intake design](/methods/inward-turning-intake-design.md))
at $\mathrm{Ma}_\infty=4.0$, $p_\infty=2930.7$ Pa, $T_\infty=220.6$ K,
by steady 3-D RANS with the standard k–ε model and wall functions
($y^+\approx30$–60), on the fine grid of a three-grid study (5.21 million
cells). The slot is on the upper wall at the impingement of the reflected
cowl shock, where the undisturbed $\delta\approx18.1$ mm, and is 20 mm
long (§3.3, Fig. 15). The bleed fraction is an outcome, not an input: 2.528%
of the captured mass flow (2.579% at the highest back pressure). The
bleed-exit boundary condition is not stated.

**Flow structure** (§3.3, Figs. 14, 16–17; shown). Without bleed the
reflected shock hits the upper wall at the shoulder, re-reflects to the
lower surface and induces a weak normal shock near the throat, with
low-energy flow in the corners. With bleed the boundary layer at the
reflected-shock station thins, the weak normal shock disappears, and the
spanwise vortices near the upper throat surface (identified with the
Q-criterion) are removed through the slot. Throat Mach number rises from
1.461 to 1.622 and throat $\sigma_0$ from 0.740 to 0.764 (Tables 4–5).

**Back pressure** (§3.4, Tables 4–5, Figs. 18–20; shown). The largest
back-pressure ratio $p_b/p_\infty$ sustained rises from 73.4 to 76.7, and
the exit $\sigma_0$ at that limit from 0.509 to 0.528, which the paper
reports as a 3.73% improvement. At equal back pressure the exit recovery
with and without bleed is practically the same (0.508 against 0.509 at
73.4; 0.484 against 0.486 at 69.6), and the terminal-shock position is
unchanged (Fig. 18): the 3.73% compares the two configurations at their
different maximum back pressures, not at one operating point.

The authors state that their numerical approach was validated against
wind-tunnel data on a wavecatcher intake in an earlier paper (Huang, Zuo &
Qiao 2018); no validation is shown in this one.

# Citations

1. [Zuo & Huang (2018)](/sources/zuo-2018.md), §3.1–3.4 (Tables 3–5, Figs. 12–20).

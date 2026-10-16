---
type: Definition
title: "Vertical displacement event (hot and cold VDE)"
description: "A vertical displacement event is the axisymmetric vertical instability of an elongated plasma after loss of position control, slowed to the wall time by eddy currents; in a hot VDE the thermal quench is caused by the displacement itself and low-n external kinks ($0<nq_a<m$) make the late phase 3D, in a cold VDE the displacement follows the thermal quench."
status: established
aliases: [VDE, hot VDE, cold VDE, asymmetric VDE, vertical instability]
tags: [disruption, vde, wall, free-boundary, kink, tokamak]
timestamp: 2026-10-16T00:00:00Z
---

# Vertical displacement event (hot and cold VDE)

A **vertical displacement event (VDE)** is the axisymmetric instability of
an elongated plasma that sets in when control of its vertical position is
lost, whether by a large MHD perturbation or by a failure of the vertical
control system ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.3;
[Artola et al. (2021)](/sources/artola-2021.md), §1). The plasma column
drifts into the wall and deposits heat and electromagnetic loads on plasma-facing
components and the vessel. In ITER every major
[disruption](/definitions/disruption.md) is expected to end in loss of
control and hence in a VDE ([Artola et al. (2021)](/sources/artola-2021.md), §1).

Simulating a VDE requires free-boundary conditions for the magnetic field
and a self-consistent evolution of the currents in the surrounding
structures ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.3), i.e.
[resistive-wall coupling](/methods/resistive-wall-coupling.md).

## Growth rate and the role of the wall

Eddy currents induced in the wall and in passive conductors by the moving
plasma oppose the motion and slow it towards the wall time $\tau_w$. For a multi-conductor system the growth rate is $1/\tau_w$
divided by (Leuer's stabilization parameter minus one), the stabilization
parameter being larger than one and decreasing with $I_p$
([Bandaru et al. (2024)](/sources/bandaru-2024.md), §IV.B, after Leuer
1989). This explains why the ITER cold VDE of the JOREK–DINA runaway
benchmark moves on ≈$2\times10^{-2}$ s although the vessel time is 0.5 s
(same section). The passive stabilizing loop (PSL) of ASDEX Upgrade shows
both limits: at low PSL conductivity the growth rate is limited by plasma
inertia, at high conductivity by the PSL resistance
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.8, Fig. 30). The PSL
eddy currents dominate the slowing of the motion relative to the no-wall
limit in an AUG-like axisymmetric VDE, whose growth rate is ≈40 s$^{-1}$
([Isernia et al. (2023)](/sources/isernia-2023.md), §IV, Fig. 4). Reducing
the ITER vessel resistivity by a factor 10 or more removes the fast vertical
motion of the cold VDE and makes halo currents negligible
([Bandaru et al. (2024)](/sources/bandaru-2024.md), §IV.B, Fig. 9b). Wall
ports raise the vertical growth rate slightly
([Isernia et al. (2023)](/sources/isernia-2023.md), §VI).

## Hot and cold VDE

The two classes differ by the order of thermal quench and displacement.

- **Hot VDE.** The plasma keeps its thermal energy while it drifts; the
  [thermal quench](/definitions/thermal-quench.md) "is induced by the
  vertical displacement" and occurs after the plasma has become limited and
  its volume has shrunk (to 26% of the initial volume at 1.16 ms after
  limitation in the JOREK run of the NSTX benchmark). Hot VDEs "feature the largest wall forces observed in
  experiments" ([Artola et al. (2021)](/sources/artola-2021.md), §4.1.1).
- **Cold VDE.** The vertical motion takes place after the thermal quench,
  during the current quench. In the ITER JOREK–DINA benchmark an upward cold
  VDE starts after an artificial TQ and continues into the runaway-electron
  plateau until full termination; a runaway beam slows the current decay
  and the VDE, which is faster without it
  ([Bandaru et al. (2024)](/sources/bandaru-2024.md), §IV.B).

## Edge safety factor and the 3D phase of a hot VDE

During a hot VDE the plasma current decays slowly while the minor radius
shrinks, so the edge safety factor falls strongly ($q_a\propto a^2/I_p$);
axisymmetric codes can keep $q_a\ge1$ only by forcing the current profile.
When $q_a$ falls below about 2 the configuration no longer stays
axisymmetric: non-axisymmetric modes grow, produce horizontal forces and
stochastic field lines ([Artola et al. (2021)](/sources/artola-2021.md), §1).

The modes are low-$n$ external kinks. In the NSTX benchmark they appear
when the $q=2$ surface moves into the open-field-line region
($q_{95}\approx2$), with dominant 2/1, 4/2 and 6/3 structures, consistent
with the external-kink condition

$$0<n\,q_a<m,$$

satisfied with $q_a\approx1.8<m/n=2$ ([Artola et al. (2021)](/sources/artola-2021.md),
§4.1.2, Eq. 7, citing Freidberg). Before that, a weakly growing $n=1$ mode
mixing a 3/1 external kink and a resistive 2/1 mode is present. All three
codes find the plasma unstable 0.85–1.10 ms after limitation
([Artola et al. (2021)](/sources/artola-2021.md), §4.1.2;
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.8). Artola et al.
use the cylindrical $q_a$ in the criterion and $q_{95}$ in the figures
interchangeably as "edge safety factor" (Fig. 3 caption); the criterion is
the cylindrical one. The kinks cause the stochastic TQ and the 3D
[halo currents](/definitions/halo-current.md) that carry the sideways
[wall force](/definitions/wall-forces.md).

The edge current lost by scrape-off during a VDE is partly re-induced in
the hot edge of the remaining plasma; analytical theory and JOREK agree on
this ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.3).

## Modelling requirements in the SOL

The SOL energy balance (parallel and perpendicular transport, Ohmic
heating, radiation, ionization) sets the temperature, hence the
resistivity, hence the current distribution and the VDE dynamics. It is
essential to limit the current density at the boundary to the ion
saturation current; otherwise large currents are induced in regions of very
low density ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.3; see
[sheath boundary conditions](/methods/sheath-boundary-conditions.md)). In
COMPASS, including the ion saturation current changes the poloidal extent of
the halo region, and in ASDEX Upgrade the SOL heat-transport parameter
changes the whole evolution ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md),
§3.1, Figs. 5–6).

## Verification and validation

- Code-to-code: the axisymmetric and 3D NSTX benchmarks of JOREK, M3D-C1
  and NIMROD ([NSTX VDE benchmarks](/benchmarks/nstx-vde-benchmarks.md));
  JOREK–CEDRES++ VDE growth rates within 10–20% over a wide range of wall
  resistivities; JOREK–DINA ITER 15 MA VDE with the last closed flux surface
  within a few cm, and a vertical oscillation driven by the VS3 coils;
  JOREK–CASTOR3D PSL growth rates within ≈20%
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.8, §6.3); JOREK
  coupled to CARIDDI and to STARWALL within 2%, and both within ≈11% of the
  mass-less CarMa0NL ([Isernia et al. (2023)](/sources/isernia-2023.md),
  §IV, Fig. 4); the cold VDE with runaway beam against DINA
  ([ITER runaway-electron benchmarks](/benchmarks/iter-runaway-electron-benchmarks.md)).
- Experiment: dedicated ASDEX Upgrade VDEs with vertical control switched
  off, where JOREK reproduces the vertical motion, the halo-current and
  vertical-force magnitudes and the TQ onset point
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.1, Fig. 5).

## Citations

- [Artola et al. (2021)](/sources/artola-2021.md), §1, §4.1.1–4.1.2, Eq. 7.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.8, §6.3.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.1.
- [Isernia et al. (2023)](/sources/isernia-2023.md), §IV, §VI.
- [Bandaru et al. (2024)](/sources/bandaru-2024.md), §IV.

---
type: Method
title: "Inward-turning intake design"
description: "Designs a three-dimensional inward-turning intake by streamline tracing in an axisymmetric internal parent flow (internal conical flow A, Busemann, or their coupling ICFC) over osculating planes, trading higher recovery and shorter, less wetted compression than planar wedges for a harder shock/boundary-layer interaction."
status: established
aliases: [wavecatcher intake, streamline-traced intake, osculating-axisymmetric intake design, section-controllable intake]
tags: [inlet, design-method, streamline-tracing, parent-flow]
timestamp: 2026-10-14T00:00:00Z
---

# Inward-turning intake design

An inward-turning intake is carved out of a chosen axisymmetric internal
parent flow: the compression surfaces are streamlines traced in that flow,
so the intake inherits its inviscid compression. The geometric route that
blends prescribed cross-sections of an isolator and optimises its
centreline with CFD is a separate method,
[Shape-transition isolator design](/methods/shape-transition-isolator-design.md).

## Osculating-axisymmetric streamline tracing

[Zuo & Huang (2018)](/sources/zuo-2018.md), §2.1, Fig. 2, design a
"section-controllable wavecatcher" intake as follows (stated; details
deferred to You & Liang 2007):

1. **Osculating planes.** Osculating-axisymmetric theory (attributed to
   Sobieczky 1990) reduces the 3-D design with prescribed capture and
   throat shapes to a series of 2-D designs, one in each osculating plane.
2. **Parent flow.** In each plane the wall is a streamline traced in an
   axisymmetric internal parent flow. The authors' parent flow, "Internal
   Conical Flow C", couples an internal conical flow of type A with a
   truncated Busemann flow; the truncated-Busemann generatrix is adjusted
   until the entrance and exit points lie on the same reflected shock.
   They credit Mölder (1967) with proving that only four types of
   parallel, uniform, straight-shock internal axisymmetric conical flows
   exist.
3. **Corrections.** The shoulder is smoothed and a displacement-thickness
   viscous correction is applied (§3.1.1).

The design is the intake counterpart of the parent-flow and
osculating-plane construction used for waveriders; see
[Osculating-cone waverider design](/methods/osculating-cone-waverider-design.md).

### Parent-flow comparison

Inviscid comparison at $\mathrm{Ma}_\infty=4.0$, mean exit Mach 1.4, same
capture area ([Zuo & Huang (2018)](/sources/zuo-2018.md), §2.3, Tables
1–2, Fig. 5; shown by the authors' inviscid computation, method not
stated):

| Parent flow | $\sigma_0$ | static pressure ratio | $\mathrm{CR}$ | length / capture height | exit height / capture height | length / exit height | wetted / capture area | pressure-drag coefficient |
|---|---|---|---|---|---|---|---|---|
| 2-D multi-wedge | 0.683 | 32.6 | 6.58 | 3.10 | 0.152 | 20.4 | 4.72 | 0.430 |
| 2-D isentropic | 0.740 | 34.5 | 6.99 | 4.17 | 0.143 | 29.3 | 5.73 | 0.423 |
| Busemann | 0.984 | 44.7 | 9.10 | 4.38 | 0.331 | 13.2 | 5.34 | 0.401 |
| Internal Conical Flow C | 0.874 | 40.5 | 7.39 | 2.94 | 0.368 | 8.0 | 3.98 | 0.378 |

Against the multi-wedge compression the inward-turning parent flow gains
28.0% in $\sigma_0$ and needs 5% less length, 15.7% less wetted area
(width-to-height ratio set to π for the planar ducts) and 12.1% less
pressure drag; the Busemann flow has the highest $\sigma_0$ of all four.
Pressure drag is stated to be 70–80% of total intake drag (attributed).
The price claimed by the authors is a harder
[shock-wave/boundary-layer interaction](/definitions/shock-wave-boundary-layer-interaction.md):
continuously rising wall pressure, larger adverse-gradient regions and a
thinned boundary-layer profile at the shoulder (§2.4, Figs. 7–8,
qualitative).

### Example and limitation

The section-controllable intake at design Mach 4 is 2920 mm long, with
$\mathrm{CR}\approx5.96$ and $\mathrm{CR}_i\approx2.18$, an elliptic and
straight-sided capture section of 88460 mm² and a two-ellipse throat of
14851 mm², followed by an 1800 mm divergent duct (13.1 throat equivalent
diameters, equivalent expansion angle 1.6°) (§3.1.1, Figs. 9–10). Because
the osculating planes cannot all keep the same $\mathrm{CR}$, the throat
Mach number is non-uniform; for ramjet intakes, whose throat Mach number
approaches 1, some planes then near Mach 1 and risk unstart, so a slightly
higher throat Mach number has to be accepted at the price of
terminal-shock loss (§2.2, stated). See
[Inlet start, unstart and hysteresis](/definitions/inlet-start-and-unstart.md)
and, for the control used on this intake,
[Boundary-layer bleed for intake control](/methods/boundary-layer-bleed.md).

# Citations

1. [Zuo & Huang (2018)](/sources/zuo-2018.md), §2.1 (Fig. 2), §2.2, §2.3 (Tables 1–2, Figs. 5–6), §2.4 (Figs. 7–8), §3.1.1 (Figs. 9–10).

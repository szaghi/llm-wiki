---
type: Definition
title: "Waverider"
description: "A hypersonic lifting body whose leading edge lies on a known shock surface, so that at its design condition the shock stays attached along the leading edge and the high-pressure gas is contained below the lower surface; its design inputs are capture curves in the base plane."
status: established
aliases: [waverider vehicle, wave rider, osculating-cone waverider]
tags: [waverider, hypersonic-vehicle, inverse-design, wide-speed-range, vortex-lift]
timestamp: 2026-10-14T00:00:00Z
---

# Waverider

A waverider is a lifting body derived from a known supersonic parent flow:
its leading edge lies on the parent flow's shock surface, so that at the
design condition the shock is attached along the whole leading edge and the
compressed gas stays below the lower surface without spilling around it.
[Zhao et al. (2018)](/sources/zhao-2018.md), §4, Figs. 9–11, show this
property on their own designs: in inviscid simulation at the design Mach
number the base-plane shock coincides with the designed shock curve and the
high pressure is confined below the lower surface; in viscous simulation the
boundary layer deflects the shock downward from its design position. The
osculating-cone family of design methods is described in
[osculating-cone waverider design](/methods/osculating-cone-waverider-design.md).

## Capture curves

The design inputs are curves in the base plane, named differently by the two
sources:

| Curve | [Wang et al. (2018)](/sources/wang-2018-d.md) | [Zhao et al. (2018)](/sources/zhao-2018.md) |
|---|---|---|
| Trace of the shock in the base plane | inlet capture curve (ICC) | inlet capture curve (ICC), also "shock profile curve" |
| Curve whose streamlines traced upstream define the leading edge | flow capture curve (FCC) | flow capture tube (FCT) |
| Planform (top view of the leading edge) | planar shape curve (PSC), a design input | an output, except for the straight constant-sweep segment |

In the conventional method the ICC and FCC are prescribed and the planform
follows; Wang et al. derive a relation among the three curves so that any
two determine the third ([Wang et al. (2018)](/sources/wang-2018-d.md), §2.1,
Eqs. 1–4). [Zhao et al. (2018)](/sources/zhao-2018.md), §2, state, citing
Sobieczky et al., that the osculating-cone method is an inverse design
approach whose main purpose is airframe–inlet integration;
[Wang et al. (2018)](/sources/wang-2018-d.md), §4, state that a concave ICC
segment can host an inward-turning inlet (not shown).

## Volumetric efficiency

[Zhao et al. (2018)](/sources/zhao-2018.md), §3.2, Eq. 16, use $\eta_V$ as
the figure of merit for volume. For their general and cuspidal
osculating-cone waveriders, $\eta_V$ rises monotonically with the design
Mach number and flattens at high Mach number (Fig. 6, approximate readings:
about 0.111 at Mach 4 to 0.132 at Mach 14 for the general one, about 0.102
at Mach 3 to 0.122 at Mach 5 for the cuspidal one). They compare three
waveriders at matched $\eta_V$ and report CFD-measured deviations of 4.6%
and 7.3% from the reference body. [Wang et al. (2018)](/sources/wang-2018-d.md),
Table 2, report a "volume index" (0.113–0.152) that the paper does not
define (it cites its ref. [20]); it is therefore not
identified with $\eta_V$ here.

## Wide-speed-range waveriders

A waverider is optimized for one design Mach number; the two sources pursue
better low-speed or off-design behaviour by changing the planform.

* **Low-sweep planforms.** [Wang et al. (2018)](/sources/wang-2018-d.md),
  §3.3, Table 2, design three Mach 6 waveriders with planforms whose sweep
  falls from 70° near the nose to 20° outboard, and a constant 70°-sweep
  reference. The design-point $L/D$ stays at 6.21–6.32 against 6.33 for the
  reference, while $L/D$ at $\mathrm{Ma}_\infty=0.4$, sea level, rises from
  12.1 to 18.3–20.1 (+51% to +66%; the paper says "about fifty percent").
  The volume index falls for the low-speed planforms (0.113–0.134 against
  0.152).
* **Constant-sweep segments.** [Zhao et al. (2018)](/sources/zhao-2018.md),
  §5, compare at equal $\eta_V$ a delta-winged waverider (design Mach 8), a
  cuspidal waverider (design Mach 3.86) and a general osculating-cone
  waverider (design Mach 4.4) at Mach 3.0–10.0 and $\alpha$ from −2° to 10°
  (25 km). The ordering of $L/D$, cuspidal > general > delta-winged, holds at
  every condition; the cuspidal gain over the general body reaches 18.5%
  (§7) and is larger at higher Mach number and lower $\alpha$ (Fig. 13a); at
  Mach 8 the cuspidal $L/D$ falls from 3.4976 at −2° to 2.1805 at 10°
  (Tables 4–6). The authors explain the ordering by body thickness (tangent of
  the symmetry-plane surface angle 0.2471, 0.2626, 0.3046) and by the
  lower-surface pressure, hence wave drag (§6). All three bodies have low
  absolute $L/D$ because the basic cone half-angle is 20° (§5).

## Nonlinear lift ("vortex lift")

* [Zhao et al. (2018)](/sources/zhao-2018.md), §6.1, Figs. 18–19, 22: at
  Mach 8 the cuspidal waverider's $C_L(\alpha)$ departs from linear above
  about 6°, reaching "almost 8%" above the linear function at 10°; the
  general and delta-winged waveriders are almost linear. The upper-surface
  pressure of the cuspidal body shows a low-pressure region that grows with
  $\alpha$ (0–12°), which the authors attribute to a vortex or separation
  bubble, following Miller & Wood and Rodi. Shown for the $C_L$ curves and
  surface pressure; the mechanism is attributed, and the authors state that
  hypersonic upper-surface separation needs further study.
* [Wang et al. (2018)](/sources/wang-2018-d.md), §3.3, Fig. 7: at the Mach 6
  design point, $C_L$ against $\alpha$ (0–10°) of their low-sweep planforms
  is nonlinear, more so for the two planforms with a 70°-to-20° sweep
  change than for the cubic-planform one; the authors attribute it to
  leading-edge vortex lift, following Rodi. No vortex or surface-pressure
  evidence is shown, and the $C_L$ magnitudes (about 0.66 at 0°, about
  2.5–2.7 at 10°, approximate readings) imply an undeclared reference area.

These two reports are a qualification, not a contradiction: they concern
different bodies (cuspidal against general and delta-winged planforms at
Mach 8; low-sweep outboard planforms at Mach 6), neither source claims
nonlinear lift for every waverider or its absence for every waverider, and
both attribute the mechanism to the same literature. What the bundle holds
is that nonlinear lift growth has been computed for some planforms, with
surface-pressure support in one source only; the vortex mechanism itself is
not demonstrated by either.

# Citations

1. [Wang et al. (2018)](/sources/wang-2018-d.md) — §2.1 (Eqs. 1–4), §3.3 (Table 2, Fig. 7), §4.
2. [Zhao et al. (2018)](/sources/zhao-2018.md) — §2, §3.2 (Eq. 16, Fig. 6), §4 (Figs. 9–11), §5 (Fig. 13, Tables 4–6), §6 (Figs. 14–22), §7.

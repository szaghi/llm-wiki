---
type: Method
title: "Osculating-cone waverider design"
description: "Inverse design of waveriders and inward-turning intakes that splits a three-dimensional shock surface into osculating planes, assigns each a local conical (or wedge) parent flow with a common shock angle, and builds the surface by streamline tracing from prescribed base-plane capture curves."
status: established
aliases: [osculating cones, osculating-cone method, osculating flowfield method, osculating-axisymmetric design]
tags: [waverider, osculating-cone, inverse-design, streamline-tracing, parent-flow]
timestamp: 2026-10-14T00:00:00Z
---

# Osculating-cone waverider design

The osculating-cone method designs a [waverider](/definitions/waverider.md)
(or an intake) from a prescribed shock shape instead of from a single
axisymmetric parent flow. [Zhao et al. (2018)](/sources/zhao-2018.md), §2,
call it an inverse design approach and credit it to Sobieczky et al.;
[Zuo & Huang (2018)](/sources/zuo-2018.md), §2.1, use the same idea under the
name *osculating-axisymmetric theory*, which reduces a three-dimensional
design to a series of two-dimensional designs in osculating planes.

## Procedure

1. **Base-plane curves.** Prescribe the inlet capture curve (ICC, the shock
   trace in the base plane) and the flow capture curve or tube (FCC/FCT)
   ([Wang et al. (2018)](/sources/wang-2018-d.md), §2.1;
   [Zhao et al. (2018)](/sources/zhao-2018.md), §2, Eqs. 1–2).
2. **Osculating planes.** At each point of the ICC, the osculating plane is
   normal to the ICC; the FCC point of that plane lies on the same normal
   ([Wang et al. (2018)](/sources/wang-2018-d.md), §2.1, Eq. 1).
3. **Local parent flow.** In each plane a local parent flow is used, sized
   by the local curvature radius of the ICC; all planes share one shock
   angle $\beta_s$ ([Wang et al. (2018)](/sources/wang-2018-d.md), §2.2).
4. **Streamline tracing.** Streamline tracing in each plane's parent flow
   builds the leading edge and the compression surface ([Wang et al. (2018)](/sources/wang-2018-d.md),
   §2.3, Table 1; [Zhao et al. (2018)](/sources/zhao-2018.md), Fig. 3).

## Parent flows

* **External cone flow (Taylor–Maccoll).** Gives convex ICC segments
  ([Wang et al. (2018)](/sources/wang-2018-d.md), §2.2).
  [Zhao et al. (2018)](/sources/zhao-2018.md), §3.1, §5, use a basic cone of
  20° half-angle for all their designs, which they say produces a large shock
  angle and low $L/D$.
* **Internal Conical Flow A (ICFA).** An internal axisymmetric conical flow
  with the same straight shock, after Mölder; it gives concave ICC segments
  ([Wang et al. (2018)](/sources/wang-2018-d.md), §2.2).
  [Zuo & Huang (2018)](/sources/zuo-2018.md), §2.1, credit Mölder (1967) with
  proving that only four types of parallel, uniform, straight-shock internal
  axisymmetric conical flows exist (stated, attributed).
* **Wedge flow.** For near-straight ICC segments (very large curvature radius)
  ([Wang et al. (2018)](/sources/wang-2018-d.md), §2.2).
* **Mixed parent flows.** Wang et al. combine external cone, ICFA and wedge
  flows in one design, all with one effective shock angle (14.35° at
  $\mathrm{Ma}_\infty=6$, 30 km), because a prescribed planform forces an ICC
  that cannot stay convex (§2.2, §3). Curved internal and external cone
  flows are stated to be admissible (not shown).
* **ICFC, for intakes.** [Zuo & Huang (2018)](/sources/zuo-2018.md), §2.1,
  §2.3, design each osculating plane of an
  [inward-turning intake](/methods/inward-turning-intake-design.md) in their
  Internal Conical Flow C, an ICFA coupled with a truncated Busemann flow,
  adjusting the Busemann generatrix until the entrance and exit points lie on
  the same reflected shock (details deferred to You & Liang 2007).

## Variants that control the planform

* **Planform as input.** [Wang et al. (2018)](/sources/wang-2018-d.md),
  §2.1–2.3, Eqs. 1–4, derive a relation among ICC, FCC and planform: each
  osculating plane is a sub-waverider of constant local sweep, and with a
  straight effective shock the local distance from FCC to shock equals the
  tangent of $\beta_s$ times the local length. Any two curves then give the
  third, solved by a predictor-corrector Euler march from the FCC–planform
  intersection. Design rules (stated): a smooth (preferably C2) planform; a
  maximum local sweep not exceeding the complement of the freestream Mach
  angle (attributed); nonzero sweep except at boundary points; a sharp nose
  forces an ICC completed by a circular arc so that the streamlines converge
  at the nose. The extra cost is stated to be "far less" than streamline
  tracing. CFD (Fluent, AUSM, RNG k–ε) reproduces the prescribed planforms,
  with shock-ICC mismatch only where the arc joins the computed curve
  (§3.3, Figs. 4–6).
* **Straight constant-sweep segments.** [Zhao et al. (2018)](/sources/zhao-2018.md),
  §2.1–2.2, Eqs. 3–15, build ICC and FCT from straight, power-law and
  parabolic pieces with tangency, intersection and perpendicularity
  constraints so that part of the leading edge is straight with a chosen
  sweep: outboard for a delta-winged waverider, near the symmetry plane for
  a cuspidal one. For the cuspidal design the tangent of the sweep equals
  the tangent of the FCT segment's inclination divided by $\tan\beta_s$
  (Eq. 13), and the parameters follow explicitly; the delta-winged design
  needs an iterative search (Fig. 3). They contrast this with earlier
  constant-swept designs (Rodi; Duan et al.; Liu et al.) restricted to a
  circular-arc ICC and a straight FCT (§1, stated). Several of their printed
  constraint equations carry slips (see the Source page).

# Citations

1. [Wang et al. (2018)](/sources/wang-2018-d.md) — §2.1 (Eqs. 1–4), §2.2, §2.3 (Table 1), §3, §3.3 (Figs. 4–6).
2. [Zhao et al. (2018)](/sources/zhao-2018.md) — §1, §2 (Eqs. 1–15, Figs. 1–4), §3.1, §5.
3. [Zuo & Huang (2018)](/sources/zuo-2018.md) — §2.1 (Fig. 2), §2.3.

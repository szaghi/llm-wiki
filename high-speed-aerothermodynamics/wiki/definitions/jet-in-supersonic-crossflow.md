---
type: Definition
title: "Transverse jet in supersonic crossflow"
description: "A jet injected normal to a wall into a supersonic stream, the canonical fuel-injection flow of scramjets, whose structure (bow shock, barrel shock and Mach disk, upstream and leeward separation, near-wall wake) is organized by the jet-to-crossflow momentum flux ratio J."
status: established
aliases: [JISC, jet in supersonic crossflow, transverse injection, sonic transverse jet]
tags: [jet-in-crossflow, injection, separation, shock-structure, experiment, npls]
timestamp: 2026-10-14T00:00:00Z
---

# Transverse jet in supersonic crossflow

A transverse jet in supersonic crossflow (JISC) is a jet issued normal to a
wall into a supersonic boundary-layer flow. Its controlling parameter is the
momentum flux ratio $J=(\rho u^2)_j/(\rho u^2)_\infty$, and lengths are
scaled by the orifice diameter $d_j$.
[Liu Y. et al. (2018)](/sources/liu-2018-c.md), Fig. 1, reproduce the canonical
structure after Gruber: a bow shock ahead of the jet, an upstream separation
with a horseshoe vortex, the barrel shock closed by a Mach disk, a
counter-rotating vortex pair, and a wake.

## Near-wall wake

[Liu Y. et al. (2018)](/sources/liu-2018-c.md) study the wake on the wall behind
a sonic nitrogen jet ($d_j$ = 2 mm) at $\mathrm{Ma}_\infty=2.95$, for $J$ =
2.3–28.9, with NPLS slices and surface oil flow (§3).

* **Collision shocks.** The flows wrapping around the barrel collide on the
  leeward side and form V-shaped "collision shocks". At $J$ = 20.6 and 28.9
  they are visible on slices 2 mm and 4 mm above the wall, which the authors
  read as evidence that the flow lateral to the jet is supersonic even 2 mm
  from the wall; at $J$ = 7.7 (and 2.3, 5.5) they are too weak to identify
  (Figs. 4–6). Their footprint is much larger at 2 mm than at 4 mm, so the
  structure is strongly three-dimensional (Fig. 7). Shown (visualization);
  interpretation stated.
* **Reflected shock.** The collision shock intersects a reflected shock that
  forms when the barrel shock is reflected by the Mach disk (attributed to the
  same group's earlier study); a half-cone shock surface forms because the
  flow behind the collision is blocked by the leeward separation bubble
  (Fig. 8b, schematic interpretation).
* **Three regions** (Fig. 8a, $J$ = 20.6, the paper's own classification):
  (I) a V-shaped separation zone induced by the collision shocks; (II) a
  reattachment region bounded by an outer slip line along the collision
  shock and an inner slip line between the reattached wake and the lateral
  flow; (III) a mixing and recovery region in which the reflected shock
  generates a second outer slip line.
* **Relation to the upstream separation.** The authors distinguish the
  V-shaped leeward separation, by mechanism and position, from the
  parabolic separation zone of Glagolev et al., which they identify with the
  horseshoe separation under the bow shock (§3, stated).
* **Effect of $J$.** At lower $J$ the collision and reflected shocks are
  weaker, the slip lines decay sooner, and the collision/reflected-shock
  intersection moves closer to the orifice; the separation is largest at
  $J$ = 28.9 (Fig. 9). Shown qualitatively.

## Separation geometry and correlation

* **Included angle.** The angle between the two separation lines of the
  V-shaped zone is 34.50° at $J$ = 28.9, 33.20° at 20.6 and 34.20° at 7.7
  (Figs. 8a, 9; the text cites "Fig. 4(b)" for the last, an evident slip for
  Fig. 9b). The authors state it is independent of $J$, because the
  collision-shock angle "is only dependent upon the free-stream Mach number"
  (stated justification; single Mach number tested).
* **Power laws** (§3, Eqs. 1–3, Fig. 11b), least-squares fitted over eight
  conditions including $J=0$: the separation start lies at
  $x/d_j=0.3167\,J^{0.7697}$, and the leeward separation length is
  $$\frac{L_{\mathrm{sep}}}{d_j}=4.582\,J^{0.4135}.$$
  The form follows jet-penetration correlations (Rothstein–Wantuck, Gruber).
  Stated uncertainties of the extraction: 3% on angles, 5% on lengths. No
  width correlation is printed, although the abstract claims one; the
  authors argue width follows from length because the angle is constant.
  The correlation is fitted to one facility, one Mach number and one
  injectant, and including $J=0$ adds a constraint rather than a
  measurement.
* **Use.** Fuel and crossflow do not mix completely in the separation zone,
  so the correlation is offered for placing injectors and combustion
  organization away from it, and as validation data (§3, stated).

## Conditions of the data set

Mach 2.95 suction tunnel, $p_0$ = 101325 Pa, $T_0$ = 300 K, $u_\infty$ about
605 m/s; flat plate with a trip; turbulent boundary layer with
$\delta$ = 6.0 mm and $\mathrm{Re}_\delta=3.5\times10^4$ at 5 mm upstream of
the orifice; sonic nitrogen jet at $T_0$ = 300 K, jet total pressure
110–1354 kPa for $J$ = 2.3–28.9 (§2, Table 1).

# Citations

1. [Liu Y. et al. (2018)](/sources/liu-2018-c.md) — §2 (Table 1, Fig. 3), §3 (Figs. 1, 4–11, Eqs. 1–3).

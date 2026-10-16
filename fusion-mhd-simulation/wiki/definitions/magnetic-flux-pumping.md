---
type: Definition
title: "Magnetic flux pumping"
description: "A saturated (1,1) helical core mode that redistributes current so as to clamp the central safety factor at about 1, replacing the sawtooth cycle; found in JOREK for sufficiently peaked pressure (1/1 quasi-interchange) and in M3D-C1 simulations of W7-X after an ECCD-driven crash."
status: established
aliases: [flux pumping, saturated (1,1) core, sawtooth-free helical core]
tags: [kink, mhd, tokamak, stellarator]
timestamp: 2026-10-16T12:00:00Z
---

# Magnetic flux pumping

Magnetic flux pumping is the redistribution of current by a saturated,
non-crashing $(1,1)$ helical core mode that keeps the central safety factor
$q_0$ at or slightly above 1. Where current drive or peaking would push $q_0$
below 1 and start a [sawtooth](/definitions/sawtooth-crash.md) cycle, the mode
instead removes the excess central current continuously, so the plasma stays
sawtooth-free.

## Sources

* **JOREK (tokamak).** A $1/1$ quasi-interchange mode keeps $q_0\ge1$ if the
  pressure is peaked enough, which prevents sawteeth and thereby removes a
  seed of [neoclassical tearing modes](/definitions/neoclassical-tearing-mode.md).
  An analytical quasi-linear expression for the normalized current
  redistribution has been derived and a reduced model is in development
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §4.4, refs. [82, 83];
  stated in the review, details in the cited works).
* **M3D-C1 (W7-X).** After the ECCD-driven outer $(1,1)$ crash, a saturated
  $(1,1)$ helical core forms and "the plasma does not tend to restore the
  initial equilibrium", so the crash cycle does not repeat
  ([Zhou et al. (2023)](/sources/zhou-2023.md), §IV, Fig. 7). The authors relate
  the structure to flux pumping and note that such post-crash saturated
  $(1,1)$ structures are "fairly common in tokamak simulations" and sensitive
  to transport parameters (their refs. [10–13]). The structure is robust to a
  temperature-dependent resistivity (Fig. 8) but does not form if the ECCD is
  switched off during the crash (not shown). The authors suggest that an
  ECCD model following the evolving field could recover cyclic behaviour.

## Relation to other core dynamics

The two sources reach the saturated state from different directions: in
JOREK the mode prevents the first crash; in the W7-X runs it appears after
one. In both, the controlling ingredients are the central current source
(ECCD in W7-X) and the pressure peaking (JOREK quasi-interchange). A related
observation without the name: after a runaway-beam loss in DIII-D a persisting
$n=1$ keeps $q_0\approx1$ in the core
([Liu et al. (2021)](/sources/liu-2021.md), §5.4, Fig. 16). The internal
kink background is on
[resistive internal kink](/definitions/resistive-internal-kink.md).

## Contradictions

None open. Neither source quantifies the clamped $q_0$ or the pumping rate in
the material ingested here.

# Citations

- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §4.4.
- [Zhou et al. (2023)](/sources/zhou-2023.md) — §IV, Figs. 7–8.
- [Liu et al. (2021)](/sources/liu-2021.md) — §5.4, Fig. 16 (related observation).

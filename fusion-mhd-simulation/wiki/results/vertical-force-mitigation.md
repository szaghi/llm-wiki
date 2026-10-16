---
type: Result
title: "Vertical-force mitigation by massive material injection"
description: "Massive impurity injection during a VDE reduces the vertical wall force because the cooled plasma carries a large, predominantly toroidal current in a broad scrape-off layer, which decouples the current centroid from the magnetic-axis motion and reduces its vertical excursion; the poloidal halo current stays moderate."
status: established
aliases: [force mitigation, vertical force reduction, current-centroid decoupling]
tags: [disruption, vde, wall, impurities]
timestamp: 2026-10-16T00:00:00Z
---

# Vertical-force mitigation by massive material injection

**Statement.** Massive impurity injection, applied at different stages of a
[VDE](/definitions/vertical-displacement-event.md), reduces the vertical
[wall force](/definitions/wall-forces.md) because the current centroid stops
following the magnetic axis: "it is this reduced excursion of the current
centroid from the midplane that is responsible for the vertical force
reduction" ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.3, Fig. 10).
The review names this among its main results: "The mechanism of vertical
force mitigation by impurity injection was identified" (Abstract). The
underlying study (Schwarz et al. 2023, reference [54] of the review) covers
JOREK simulations of ASDEX Upgrade, JET and ITER.

## Mechanism

[Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (§3.3) give the chain:

1. The injected impurities cool the plasma inside and outside the
   separatrix to comparable temperatures, such that a substantial fraction
   of $I_p$ flows in the scrape-off layer.
2. The injection raises $q_{95}$ substantially, and at large $q_{95}$ the
   SOL currents are predominantly toroidal.
3. As the plasma moves, the current centroid becomes dominated by these
   broad SOL currents and decouples from the motion of the magnetic axis,
   "as seen in simulations as well as experiments".
4. The reduced vertical excursion of the current centroid from the
   midplane is what reduces the vertical force; the source attributes the
   reduction to this excursion without giving a quantitative force law.

The halo current is consistent with this picture although the SOL current
is large: since the SOL currents are mostly toroidal, their poloidal
component, the [halo current](/definitions/halo-current.md) proper, is
reduced compared with hot VDEs at much lower $q_{95}$. Both simulations and
experiments show a broadening of the halo-current pattern in mitigated
cases, which is direct evidence of the broader SOL current distribution
([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.3).

## Context

- In an unmitigated hot VDE the maximum vertical force is carried by halo
  currents induced in the open-field-line region after the thermal quench
  ([Artola et al. (2021)](/sources/artola-2021.md), §4.3.1, Fig. 12), and
  hot VDEs "feature the largest wall forces observed in experiments"
  (§4.1.1). The mitigation mechanism acts by changing the current
  distribution that produces this force, not by removing the VDE.
- A complementary route works through the current-quench time: JOREK scans
  of an ITER VDE give a poloidal halo fraction that grows from ≈10% for fast
  to ≈50% for slow current quench relative to the wall time, so the 50–150 ms
  CQs targeted by the ITER mitigation system halve the halo loads with
  respect to their maximum ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md),
  §6.3). See [disruption](/definitions/disruption.md).
- Predictive ITER current-quench simulations at realistic post-TQ
  parameters show that mitigation reduces the global wall forces
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.3).
- The injection itself is described on
  [shattered pellet injection and massive material injection](/definitions/shattered-pellet-injection.md).

## Limits of the evidence

The review states the mechanism and reproduces one figure; force values,
injection timings and the experimental comparison are in the cited
original, which is not ingested in this bundle. The result concerns the
vertical force; the sideways force of 3D kinks in mitigated disruptions is
not addressed in this statement.

## Citations

- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md), Abstract, §3.3, Fig. 10.
- [Artola et al. (2021)](/sources/artola-2021.md), §4.1.1, §4.3.1.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.3.

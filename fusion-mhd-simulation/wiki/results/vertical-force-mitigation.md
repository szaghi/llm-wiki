---
type: Result
title: "Vertical-force mitigation by massive material injection"
description: "Massive impurity injection during a VDE reduces the vertical wall force because the cooled plasma carries a large, predominantly toroidal current in a broad scrape-off layer, which decouples the current centroid from the magnetic-axis motion and reduces its vertical excursion; the poloidal halo current stays moderate, and the mechanism fails when a runaway beam keeps the current inside the last closed surface."
status: established
aliases: [force mitigation, vertical force reduction, current-centroid decoupling]
tags: [disruption, vde, wall, impurities]
timestamp: 2026-10-16T16:51:00Z
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
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.3). The primary
  study gives numbers: in two 3D JOREK–STARWALL runs of ITER 15 MA
  mitigated CQs ($\tau_{\mathrm{CQ}}\approx46$ ms, cold post-TQ states mimicking
  neon SPI) the vertical force peaks at 11–14 MN, a factor ≈6 below the
  ≈80 MN of earlier estimates, and the sideways force stays below 1 MN
  ([Artola et al. (2022)](/sources/artola-2022.md), §4.3, §5, Fig. 9).
- **EU-DEMO without runaways.** In a 2D JOREK–STARWALL run of an upward
  hot VDE of EU-DEMO mitigated by neon, $q_{95}$ rises above 8 because
  $I_p$ decays faster than the square of the minor radius, a large fraction
  of the current is induced in the halo region outside the last closed
  surface, the current centroid stagnates near the midplane, and the
  vertical current moment and the vertical force saturate at about 13 MN,
  "in agreement with" Schwarz et al. (2023) and Miyamoto (2011), as cited
  ([Vannini et al. (2025)](/sources/vannini-2025.md), §4, Fig. 3). This is
  an independent instance of steps 2–4 above.
- The injection itself is described on
  [shattered pellet injection and massive material injection](/definitions/shattered-pellet-injection.md).

## Qualifications

**A second mechanism in the fast-CQ limit — complementary.**
[Artola et al. (2022)](/sources/artola-2022.md) (§4.3) attribute the
residual vertical force of their mitigated ITER CQs not to the current
centroid but to the diffusion of the net toroidal wall current along the
up-down asymmetric vessel after $I_p$ has vanished; the force peaks on the
wall time and does not depend on the direction of the displacement. The
two explanations answer different questions. The centroid decoupling of
[Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (§3.3) explains why
injection during a VDE lowers the force that the moving plasma current
exerts; Artola et al. explain what force remains when the CQ is so fast
that the plasma current is gone before the wall currents have redistributed.
Artola et al. do not analyse the current centroid, and their injection is
represented only by the cold initial state, so neither study tests the
other's mechanism. Together they say that a fast, strongly mitigated CQ
moves the peak vertical load from the plasma to the vessel's own current
redistribution.

**Failure with a runaway beam — qualification.** The same EU-DEMO VDE
with a runaway seed forms a beam of about 13 MA that slows the $I_p$ decay.
The plasma then shrinks faster than its current falls, so $q_{95}$
*decreases*; "a large portion of the current remains inside the LCMFS", the
centroid follows the axis, and the vertical current moment and force keep
growing, to about 43 MA m and 60 MN at 570 ms in 2D, with only a flattening
that "could indicate" the maximum
([Vannini et al. (2025)](/sources/vannini-2025.md), §4, Fig. 3; values read
from the figure). Step 2 of the mechanism therefore fails when a runaway
beam carries the current. The authors note that $q_{95}$ falls to
unphysically low values because 2D allows no MHD; in 3D the beam
termination raises $q_{95}$ from about 2.2 to 2.55, "slightly reduces" the
force and makes it grow more slowly than in 2D (§5, Fig. 6). The 60 MN is
therefore an axisymmetric upper estimate, not a 3D prediction.

## Limits of the evidence

The review states the mechanism and reproduces one figure; force values,
injection timings and the experimental comparison are in the cited
original, which is not ingested in this bundle. The only ITER force values
in the bundle are those of Artola et al. (2022), which concern the
fast-CQ, post-CQ mechanism above rather than the centroid mechanism; the
EU-DEMO values of Vannini et al. (2025) are the bundle's only force numbers
for the centroid mechanism, and they are axisymmetric. The
result concerns the vertical force; the sideways force of 3D kinks in
mitigated disruptions is not addressed in this statement (Artola et al.
2022 find it at noise level for their cases).

## Citations

- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md), Abstract, §3.3, Fig. 10.
- [Artola et al. (2021)](/sources/artola-2021.md), §4.1.1, §4.3.1.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.3.
- [Artola et al. (2022)](/sources/artola-2022.md), §4.3, §5, Fig. 9.
- [Vannini et al. (2025)](/sources/vannini-2025.md), §4–5, Figs. 3, 6.

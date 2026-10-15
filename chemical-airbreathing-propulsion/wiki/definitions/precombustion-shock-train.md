---
type: Definition
title: "Pre-combustion shock train"
description: "The shock train that combustion back pressure drives into the isolator of a ramjet or dual-mode combustor, whose strength and position balance the combustor pressure against the inlet flow and which, pushed too far upstream, enters the inlet and cuts air capture."
status: established
aliases: [precombustion shock train, pre-combustion shock, combustion shock]
tags: [isolator, shock-train, ramjet, scramjet, rbcc, inlet-unstart]
timestamp: 2026-10-14T00:00:00Z
---

# Pre-combustion shock train

The pre-combustion shock train is the shock system that forms in the
isolator, upstream of the fuel injection, when combustion raises the
combustor pressure above what the incoming supersonic flow can enter
against. In the direct-connect tests of
[Ye et al. (2018)](/sources/ye-2018.md), §4.1, Fig. 6, combustion
produced boundary-layer separation and a normal shock train in the
isolator, so the combustor inflow was subsonic. Its position responds to
the fuel distribution and to the rocket state, and the sources below
treat the isolator entrance as the upstream limit of acceptable
operation.

## Strength and self-balancing

[Yan et al. (2018)](/sources/yan-2018.md) measure its strength by the
static-pressure ratio across a normal shock at the upstream Mach number,
$\frac{2\gamma}{\gamma+1}\mathrm{Ma}^2-\frac{\gamma-1}{\gamma+1}$ (Eq. 4,
attributed to Emanuel, ref. 37), with $\mathrm{Ma}$ the Mach number ahead
of the shock. In their unsteady RANS of an RBCC flow path at
$\mathrm{Ma}_\infty=5$ (§4.1, Fig. 7, Case 3):

* combustion grows behind the pylon for 5.7 ms after ignition;
* from 5.7 to 9.7 ms it pushes the shock upstream; during the motion the
  shock angles and the pre-shock velocity rise, so the pressure ratio
  rises until it balances the combustion pressure;
* the shock then stabilises in the forepart of the isolator, with
  [thermal choking](/definitions/thermal-choking.md) at the exit of the
  frontal cavity.

Yan et al. state this self-balancing as the paper's main mechanism. They
also attribute to the literature (§1) that in HyShot II a combustion shock
forms and propagates upstream only for $\phi>0.38$ (Laurence, ref. 11),
that shock-train strength falls as fuel flux falls (Fotia, ref. 12), that
the shock changes from a λ to an X shape as mainstream velocity rises
(Tamaki, ref. 13), and that direct-connect and freejet tests differ in
shock-train length and ignition (Thomas, ref. 18).

## Position and the inlet limit

* **Pushed into the inlet.** In [Yan et al. (2018)](/sources/yan-2018.md),
  §4.2, Fig. 9, front-loaded fuel at $\mathrm{Ma}_\infty=3$ raised the
  pressure to 4.5 times the reference pressure and pushed the shock into
  the inlet throat; more air spilled through the bleed and capture fell by
  17%. At $\mathrm{Ma}_\infty=4$ with all fuel at one station the shock sat
  at the isolator entrance, "the limit" of inlet operation (§4.2, Fig. 8).
  Moving fuel downstream returned the shock to the isolator in both cases.
* **Freejet test.** In the shock-tunnel freejet test at
  $\mathrm{Ma}_\infty=4$ (§4.3, Fig. 12) the shock train stabilised "at
  the isolator entrance", with the flow stable 30 ms after the reference
  time of the record (ignition at 2.7 ms), at a station ($x$ = 22 inlet-throat heights) that Fig. 2
  places upstream of the isolator start (see the Source page).
* **Rocket shut-off.** In [Ye et al. (2018)](/sources/ye-2018.md), §4.1,
  Fig. 6c–d, switching the pilot rocket off at simulated Mach 4 and 6 moved
  the shock train toward the combustor; it stayed in the isolator.
* **Throat type.** At Mach 6, Ye et al. compute that the
  [variable-geometry combustor](/methods/variable-geometry-combustor.md)
  forms a pre-combustion shock train in the isolator and runs in ramjet
  mode, while the fixed-geometry one does not and keeps supersonic flow
  outside the pylons (§4.2.2, Figs. 11–13).

## Total-pressure cost

The shock train costs total pressure. [Ye et al. (2018)](/sources/ye-2018.md),
§4.3, Fig. 14, find that the variable-geometry combustor loses more total
pressure in the isolator (stronger shock train) and less in combustion
(lower combustor Mach number), ending with higher recovery at the
combustor exit: 0.63 against 0.58 at Mach 3, 0.32 against 0.24 at Mach 6
(recovery taken as the mass-weighted $p_0$ over the isolator-inlet $p_0$).

# Citations

1. [Yan et al. (2018)](/sources/yan-2018.md) — §1 (refs. 11–13, 18), §4.1 (Eq. 4, Fig. 7), §4.2 (Figs. 8–9), §4.3 (Figs. 2, 12).
2. [Ye et al. (2018)](/sources/ye-2018.md) — §4.1 (Fig. 6), §4.2.2 (Figs. 11–13), §4.3 (Fig. 14).

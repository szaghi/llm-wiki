---
type: Method
title: "Boundary-layer combustion for skin-friction reduction"
description: "Injecting and burning hydrogen inside the wall boundary layer of a supersonic combustor to lower near-wall density and Reynolds stress, which cut the mean wall shear stress of a step duct at Mach-6 combustor conditions by 57.5% in RANS at the cost of a local wall heat-flux peak."
status: established
aliases: [boundary layer combustion, BL combustion, film combustion for drag reduction]
tags: [skin-friction, drag-reduction, hydrogen, scramjet, rbcc, heat-flux, rans]
timestamp: 2026-10-14T00:00:00Z
---

# Boundary-layer combustion for skin-friction reduction

Boundary-layer combustion injects fuel (here hydrogen) along a wall of a
supersonic duct and burns it inside the boundary layer. The mechanism
stated by [Wang et al. (2018)](/sources/wang-2018-c.md), §1 and §3.4,
after Stalker and Goyne (their refs. 11–15), is that heat release lowers
the near-wall density and with it the Reynolds stress, and so the wall
shear stress. Wang et al. study it as the remedy for the skin friction of
a [rocket-based combined-cycle engine](/definitions/rbcc-engine.md),
which their computations put at 40.3% of thrust at Mach 6.

## Computation of Wang et al.

Simplified duct (§3.4, Fig. 8), steady RANS in ANSYS Fluent with SST k–ω:

* 3-D rectangular duct, 900 mm long; entry 250 mm long, 54 mm × 29 mm;
  a 3 mm rearward-facing step with three 3 mm × 3 mm hydrogen holes on the
  step.
* Inflow at Mach-6 combustor-entry conditions: $\mathrm{Ma}=2.3$,
  $T_0=1850$ K, $p_0=2.4$ MPa. Hydrogen at $p_0=1$ MPa and $T_0=300$ K,
  overall $\phi=0.2$.
* Three cases: no injection, injection without combustion, injection with
  combustion. The reaction step used for hydrogen is not stated.

Results (Figs. 9–11):

| Case | Mean upper-wall shear stress |
|---|---|
| air only | 1234 Pa |
| hydrogen injection, no combustion | 1214 Pa |
| hydrogen injection with combustion | 525 Pa |

The reduction with combustion is 57.5% (the abstract prints 57.7%; the
shear values give 57.46%). Along the duct (figure readings, Fig. 9a) the
burning case has near-zero shear just behind the step, a peak of about
730 Pa near $x\approx0.4$ m, a minimum of about 270 Pa at
$x\approx0.57$ m and about 850 Pa at the exit: downstream mixing raises
the density and the shear recovers. Wall shear is negative behind the step
(recirculation, Fig. 11) and larger mid-span than near the side walls.
Injection without combustion can raise the shear downstream (stronger
turbulence). The Conclusions call the result a 57.5% cut in "total drag";
the computed quantity is the mean upper-wall shear stress of the duct.

## Heat-flux penalty

The burning case produces a strong exothermic region near
$x\approx350$ mm, where the upper-wall total heat flux peaks at about
−4.9 MW/m² against about −2 MW/m² for air only (figure reading, Fig. 10;
sign convention not stated); cold hydrogen lowers the flux near the step.
Wang et al. conclude that thermal management is part of using the method.

## Reported effectiveness of skin-friction reduction

Wang et al. (§1) attribute to the literature: boundary-layer combustion
above 70% reduction (ref. 11); about 50% with hydrogen and negligible
effect with JP-10 (ref. 20); passive methods such as riblets at most about
10% (ref. 16); arc discharge 18.5% in air and 27.4% in argon (ref. 18).
They also cite skin friction above 50% of total drag on hypersonic
vehicles (ref. 9).

## Validation basis

The skin-friction prediction of the same numerical setup was checked
against the direct skin-friction measurement of Tsuru et al. (their
ref. 44) in a Mach 2.5 vitiated-air duct: 950 Pa computed against
1072 Pa ± 5% and 1060 Pa ± 10% measured (validation, Fig. 2), about 11% low and
outside both stated uncertainties, which the authors call "acceptable in
engineering calculations". The boundary-layer-combustion case itself has
no experimental comparison.

# Citations

1. [Wang et al. (2018)](/sources/wang-2018-c.md) — §1 (refs. 9, 11–16, 18, 20), validation section (Fig. 2), §3.2, §3.4 (Figs. 8–11), Conclusions.

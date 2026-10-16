---
type: Result
title: "High-field-side high-density region"
description: "In JOREK simulations of the ITER PFPO-1 H-mode with kinetic neutrals, poloidal E×B drifts trap a dense, cold, low-pressure region in a dominant high-field-side E×B vortex near the X-point; it forms dynamically over 10–20 ms, only when drifts are included, with a phase-like transition of the upstream density and full inner-target detachment."
status: established
aliases: [HFSHD, HFSHD region, high-field-side high-density front]
tags: [edge, divertor, neutrals, tokamak]
timestamp: 2026-10-16T00:00:00Z
---

# High-field-side high-density region

**Statement.** In [JOREK](/software/jorek.md) reduced-MHD simulations of the
ITER PFPO-1 H-mode (1.85 T, 5 MA, 20 MW heating, no impurities) with
[kinetic neutrals](/methods/kinetic-neutral-model.md), a high-field-side
high-density (HFSHD) region forms near the X-point when the poloidal
$E\times B$ drifts are included. It is a dense, cold, low-pressure region,
reaching electron densities of order $10^{21}$ m$^{-3}$, trapped in a
high-field-side $E\times B$ vortex. It forms dynamically, and its formation
coincides with full detachment of the inner target
([Korving et al. (2023)](/sources/korving-2023.md), §VI D, §VIII, Figs.
11, 15, 18–20). [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (§2.4,
Fig. 4) list it among the JOREK edge results of 2021–2024.

## Conditions of the simulations

- Standard JOREK reduced MHD with $\psi$ and $u$ evolved, so that the
  $E\times B$ velocity $-R^2\nabla u\times\nabla\phi$ is self-consistent;
  diamagnetic and neoclassical flows off; one temperature; Bohm
  [sheath conditions](/methods/sheath-boundary-conditions.md) with a
  grounded wall ([Korving et al. (2023)](/sources/korving-2023.md), §II B,
  §V E).
- Kinetic neutrals without molecules or neutral–neutral collisions; gas
  puff in the divertor and pumping at the private-region boundary; the
  sub-dome region is not gridded (§IV, §V).
- Steady states need 11–55 ms of simulated time, dynamic puff ramps at
  least 40 ms; some runs reach 150 ms (§V, §VII A).
- The orientation of $\phi$ and the signs of $B_\phi$ and $I_p$, which set
  the direction of the $E\times B$ drift, are not stated in the paper
  (Source page).

## Mechanism

1. With drifts, the $E\times B$ flow from the outer to the inner target
   through the private flux region moves power to the outer target. The
   inner target then detaches (target $T_e<5$ eV) at an upstream
   separatrix density of about $2\times10^{19}$ m$^{-3}$, much lower than
   without drifts ([Korving et al. (2023)](/sources/korving-2023.md),
   §VI A, Figs. 7, 11).
2. Three $E\times B$ vortices form near the X-point: on the low-field side,
   on the high-field side and in the private region. When the
   high-field-side vortex dominates the poloidal flow, i.e. the $E\times B$
   speed is comparable to or larger than the remaining poloidal speed, it
   traps density (§VI D, §VIII D, Figs. 11, 18).
3. Formation proceeds by a slow build-up of density at the wall, then a
   density front that moves toward the X-point and builds up to
   $n_e\sim10\times10^{20}$ m$^{-3}$, then a jump away from the X-point to a
   stable position that shifts horizontally with the fuelling rate. It
   takes 10–20 ms (Fig. 19, §IX).
4. The region is "not a passive structure": it changes the flows in the
   whole SOL. Ionization concentrates at its edge. In the detached case
   the inner strike point is at about 1 eV and the outer at about 10 eV
   (outer target attached) (§VIII D, Fig. 21).

## Signatures

- **Phase-like transition.** Near an upstream density of
  $2.4\times10^{19}$ m$^{-3}$ the upstream density stagnates, drops and
  recovers at nearly constant power over about 6 ms. This occurs "only
  with drifts" (§VIII A, Fig. 15). The quoted transition density varies
  between runs: about 2–2.2 (§VI A), 2.28–2.3 (§VI B), 2.4 (§VIII) and 2.2
  (§IX) $\times10^{19}$ m$^{-3}$, from steady-state and dynamic runs with
  different ramp rates.
- **Two states at nearly equal upstream density.** Two distinct target
  profiles at 2.28 and $2.3\times10^{19}$ m$^{-3}$ bracket the HFSHD
  formation (§VI B).
- **Detachment link.** In the 20 MW scenario full inner-target detachment
  always comes with HFSHD formation (§VIII C, a single scenario).

## Relation to other findings

- ASDEX Upgrade measurements identify $E\times B$ drifts as fundamental to
  the HFSHD region (Reimold et al. 2017, Manz et al. 2017, cited in §I):
  agreement in mechanism.
- SOLPS-ITER finds an HFSHD region with drifts at high SOL power and with
  impurities (Kaveeva et al. 2020, Rozhansky et al. 2021, cited in §VIII B).
  In JOREK it is driven by the drifts and the main-plasma flow and does
  "not specifically requir[e] high power operation and the injection of
  impurities". The two results differ in conditions, not in mechanism, and
  the JOREK result rests on one scenario.
- The diamagnetic drift is not expected to matter because the region has
  low pressure (§VIII D 1, §IX, stated, not tested).
- An HFSHD region with radiating impurities is named as a possible
  precursor of the X-point radiator (§I).
- For ITER $Q=10$ (100 MW) neutrals alone will not detach the plasma, and
  impurity seeding is needed (§VIII D 3, stated).

## Qualifications

The result comes from one code and one scenario. Molecules, neutral–neutral
collisions, two temperatures and diamagnetic flows are absent. In the
driftless comparison, the same model gives about 2× higher peak target heat
flux than SOLPS-ITER and detaches at about 10% higher upstream density
([kinetic neutral model](/methods/kinetic-neutral-model.md), Contradictions).
The existence and dynamics of the HFSHD region in the full model have not
been checked against another code.

# Citations

- [Korving et al. (2023)](/sources/korving-2023.md) — §I, §II B, §V E, §VI, §VII A, §VIII, §IX, Figs. 7, 11, 15, 18–21.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §2.4, Fig. 4.

---
type: Method
title: "Global kinetic mechanisms for kerosene"
description: "Reduced finite-rate mechanisms of a few irreversible Arrhenius steps on a single-component kerosene surrogate (C12H23, C10H16 or C10H20), used without turbulence–chemistry interaction in the RANS of scramjet and RBCC combustors."
status: established
aliases: [global kerosene mechanism, quasi-global kerosene mechanism, reduced kerosene kinetics, three-step kerosene mechanism, Westbrook–Dryer mechanism]
tags: [kinetics, kerosene, reacting-cfd, rans, rbcc, scramjet]
timestamp: 2026-10-14T00:00:00Z
---

# Global kinetic mechanisms for kerosene

A global (or quasi-global) mechanism represents kerosene oxidation by a
handful of irreversible steps on a one-component surrogate, each with a
modified Arrhenius rate: pre-exponential factor, temperature exponent and
activation energy $E_a$, with empirical fuel and oxidizer reaction orders
where given. The three RBCC sources of this bundle all use one in steady
3-D RANS of liquid-kerosene combustors, each with a different surrogate
and none with a turbulence–chemistry interaction model.

## Mechanisms as printed

**[Wang et al. (2018)](/sources/wang-2018-c.md), Table 2** — surrogate
C₁₂H₂₃, three irreversible steps, laminar finite-rate closure (Eq. 4-1),
mechanism cited to their refs. 38–39 in the text and refs. 35–36 in the
table caption. Pre-exponential units printed as
"(kmol/m3)^{1−η_F−η_O}/S"; $E_a$ in J/kmol.

| Reaction | Pre-exponential factor | Temperature exponent | $E_a$ (J/kmol) | Fuel order | Oxidizer order |
|---|---|---|---|---|---|
| 4 C₁₂H₂₃ + 47 O₂ → 48 CO + 46 H₂O | 1.60e+15 | 0 | 2.20e+08 | 0.5 | 1.0 |
| 2 CO + O₂ → 2 CO₂ | 1.92e+10 | 0 | 1.03e+08 | 1.0 | 1.0 |
| H₂ + 0.5 O₂ → H₂O | 9.87e+08 | 0 | 3.10e+07 | 1.0 | 1.0 |

**[Yan et al. (2018)](/sources/yan-2018.md), Table 2** — surrogate
C₁₀H₁₆, three irreversible steps, laminar finite-rate closure, cited to
their refs. 22 and 27. Units as printed: pre-exponential factor in
cm³/(mol s), $E_a$ in J/(kg mol).

| Reaction | Pre-exponential factor | Temperature exponent | $E_a$ (J/(kg mol)) |
|---|---|---|---|
| C₁₀H₁₆ + 5 O₂ → 10 CO + 8 H₂ | 2.35e+04 | 1 | 1.633e+08 |
| 2 CO + O₂ → 2 CO₂ | 3.48e+08 | 2 | 8.42e+07 |
| 2 H₂ + O₂ → 2 H₂O | 3.01e+17 | −1 | 0 |

**[Ye et al. (2018)](/sources/ye-2018.md), Table 3** — surrogate C₁₀H₂₀
(ref. 30), Westbrook–Dryer quasi-global mechanism (ref. 31) with 10
species and 12 finite-rate reactions; turbulence–chemistry interaction
neglected. The fuel step:

| Reaction | Pre-exponential factor | Temperature exponent | $E_a$ (J/kmol) | Fuel order | Oxidizer order |
|---|---|---|---|---|---|
| C₁₀H₂₀ + 5 O₂ → 10 CO + 10 H₂ | 4.50e+09 | 0 | 1.256e+08 | 0.25 | 1.5 |

The other eleven reactions of Ye et al.'s Table 3 are not reproduced in
the reading notes behind this page.

## How the sources use them

* **Spray coupling.** Wang et al. and Yan et al. feed the gas-phase
  mechanism from Lagrangian droplets with non-equilibrium evaporation and a
  boiling law in ANSYS Fluent (Wang et al., Eqs. 3-1 to 3-9; Yan et al.,
  §3); Ye et al. use an Eulerian dispersed-phase spray in CFD++ (§3).
* **No turbulence–chemistry interaction.** All three use the mean
  temperature and composition in the Arrhenius rates. Ye et al. (§3)
  acknowledge that this can misplace ignition delay and argue that it
  matters little in a steady computation.
* **Rocket exhaust.** Yan et al. and Ye et al. do not compute the
  embedded rocket's combustion; they impose its exhaust with a CEA
  composition dominated by CO (mass fraction 0.941) and H₂ (0.057), the
  species of the mechanisms' second and third steps (Yan et al., §3;
  Ye et al., Table 4).
* **Hydrogen.** Wang et al. also burn hydrogen in their
  [boundary-layer combustion](/methods/boundary-layer-combustion.md) duct;
  which step they use is not stated (§3.4).

Wang et al. and Yan et al. come from the same laboratory and use
different surrogates, step sets and rate constants for the same purpose.
Neither paper compares mechanisms or tests sensitivity to the choice, so
the differences are not a disagreement about kerosene chemistry; the
mechanisms are modelling choices with no validation of their own in these
sources beyond the wall-pressure agreement of the whole computation.

# Citations

1. [Wang et al. (2018)](/sources/wang-2018-c.md) — §2.2, Eqs. 3-1 to 3-9, 4-1, 4-2, Table 2, §3.4.
2. [Yan et al. (2018)](/sources/yan-2018.md) — §3 (Table 2), rocket boundary condition.
3. [Ye et al. (2018)](/sources/ye-2018.md) — §3 (Table 3), Table 4.

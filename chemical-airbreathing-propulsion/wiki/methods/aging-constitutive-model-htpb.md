---
type: Method
title: "Thermo-oxidative aging model of HTPB coatings"
description: "Phenomenological constitutive model of an aged HTPB solid-motor coating that takes the NMR crosslink density as the aging variable, advances it with a power law in time whose rate follows a modified Arrhenius law, and multiplies an equilibrium polynomial hyperelastic stress by an aging function of strain and crosslink density."
status: established
aliases: [aging constitutive model, HTPB coating aging model, crosslink-density aging model]
tags: [solid-rocket-motor, htpb, aging, constitutive-model, hyperelasticity, arrhenius, experiment]
timestamp: 2026-10-14T00:00:00Z
---

# Thermo-oxidative aging model of HTPB coatings

The coating of a solid rocket motor, the buffer and thermal-insulation layer
between propellant and case, is in the case of
[Li et al. (2018)](/sources/li-2018.md) a hydroxyl-terminated polybutadiene
(HTPB) rubber filled with corrosion-resistant and anti-abrasive fillers. The
paper builds a constitutive model of the aged coating in which the aging state
is the crosslink density $\nu_e$, measured by NMR, instead of aging time and
temperature. The authors state that such a model for HTPB coatings "has not
been reported" (§1).

The model has three parts. Each is a least-squares fit to one material batch,
so the fitted constants are not shown to transfer to other batches.

## 1. Crosslink-density kinetics

* **Data.** Thermo-oxidative aging at 323.15, 333.15, 343.15 and 353.15 K
  (±1 K, humidity below 30 %) for 50 days, sampled every 5 days. $\nu_e$
  rises monotonically, fast at first and then slower, with a similar shape at
  every temperature, which the authors read as a single aging mechanism
  ([Li et al. (2018)](/sources/li-2018.md), §2.1, §2.4, Fig. 7). Read from
  Fig. 7, $\nu_e$ starts at about 300 mol m⁻³ (3.0×10⁻⁴ mol cm⁻³) and reaches
  about 485, 520, 610 and 655 mol m⁻³ after 50 days at the four temperatures.
  The early rise is attributed to post-curing and oxidative crosslinking, the
  later one to oxidation slightly outweighing chain scission (stated,
  attributed).
* **Model selection.** Of three empirical laws for $\nu_e$ against aging
  time, the best is a **power law**: $\nu_e$ equals its initial value plus a
  rate constant times $t^{0.3}$, with $t$ in days (§3, Eq. 2, Table 1;
  correlation coefficient 0.9684–0.9828). A logarithmic law gives
  0.8397–0.8887; a third law, called exponential, is misprinted and cannot be
  reproduced (see the source page). The exponent 0.3 is stated to be the best
  of a scan that is not tabulated.
* **Modified Arrhenius law.** The logarithm of the rate constant is fitted as
  a constant, plus an exponent times the logarithm of $T$, minus
  $E_a$ divided by the product of the universal gas constant
  (8.314 J mol⁻¹ K⁻¹) and $T$ (§3, Eq. 4,
  Table 2, form attributed). Fitted values: constant 213.5, temperature
  exponent −30.21, $E_a$ = 1.062×10⁵ (unit not printed; J mol⁻¹ implied),
  correlation coefficient 0.9971.

## 2. Equilibrium hyperelastic stress

* **Equilibrium curve.** The equilibrium stress–strain curve is obtained by
  multi-step relaxation: 10 % strain steps at 100 mm/min, each held 600 s, to
  fracture. The hold length is justified by a single-step test in which the
  stress falls from 0.23 MPa to 0.12 MPa in 600 s and is 0.11 MPa at 1800 s,
  so 91.67 % of the drop occurs in the first 600 s
  ([Li et al. (2018)](/sources/li-2018.md), §2.2, Fig. 3).
* **Law.** Incompressible uniaxial tension with stretch $1+\varepsilon$, and a
  second-order polynomial (Rivlin) strain-energy density in the first two
  invariants with five coefficients, the order chosen from "application
  experience" (§4.1, Eqs. 12, 14, 15). The fitted coefficients (Table 3; units
  not printed, MPa implied) are 0.4001 and −0.1957 for the linear first- and
  second-invariant terms, −0.005041 and −0.1390 for their squares, and 0.0333
  for the cross term, with correlation coefficient 0.9999 over strains 0–3
  (Fig. 8).

## 3. Aging function

* **Definition.** The stress $\sigma$ of the aged material is the
  equilibrium hyperelastic stress multiplied by an aging function of $\nu_e$
  and $\varepsilon$, measured as
  the ratio of the tensile-test stress (100 mm/min) to the equilibrium stress
  at the same strain ([Li et al. (2018)](/sources/li-2018.md), §4.2, Eqs. 5,
  16).
* **Fit.** The aging function is a sum of two exponentials in $\varepsilon$, each with an
  amplitude and a rate coefficient (Eq. 17); the four coefficients are fitted
  as functions of $\nu_e$ expressed in units of 100 mol m⁻³ (10⁻⁴ mol cm⁻³),
  written X below (a local abbreviation, not a coordinate) (Table 4, Figs. 9–10):

  | Coefficient | Fit in X | Correlation coefficient (as printed) |
  |---|---|---|
  | first amplitude | −0.009045 X² + 0.01206 X + 0.9628 | −0.9417 |
  | first rate | −0.8583 X + 0.4713 | −0.9023 |
  | second amplitude | 0.5303 X − 0.5374 | 0.9147 |
  | second rate | −0.02202 X + 0.1428 | −0.8971 |

  The aging function ranges from about 1.2 for unaged material to about 3.5 after 50 days at
  small strain (read from Fig. 9). Because it differs from 1 for the unaged material,
  it combines the rate (viscoelastic) effect of comparing a tensile test with
  a relaxed curve with the aging effect; the model does not separate them.
* **Aging effect on the tensile curve.** Longer or hotter aging lowers the
  maximum elongation and raises the modulus and the strength (§2.3,
  Figs. 4–5). Read from Fig. 5, the unaged coating fractures at an elongation
  of about 4.3 and a stress of about 1.9 MPa; after 50 days at 353.15 K, at
  about 2.3 and 2.7 MPa.

## Verification

A held-out aging test at 313.15 K ([Li et al. (2018)](/sources/li-2018.md),
§5, Table 5, Fig. 11):

| Aging time (days) | $\nu_e$ measured (mol m⁻³) | $\nu_e$ predicted (mol m⁻³) | Error |
|---|---|---|---|
| 10 | 377.1 | 379.3 | 0.58 % |
| 20 | 399.7 | 398.1 | 0.40 % |
| 30 | 408.9 | 411.0 | 0.51 % |
| 40 | 423.1 | 421.2 | 0.45 % |
| 50 | 428.9 | 429.7 | 0.19 % |

The tensile curves are said to be predicted "accurately", without an error
metric; the 10-day case is somewhat worse, and the model is "not very good"
near fracture because damage is neglected. The initial crosslink density used
for the 313.15 K prediction is not printed; the power-law intercepts of
Table 1 (258–284 mol m⁻³) differ from the measured day-0 value of about
300 mol m⁻³, so the procedure for choosing it at a new temperature is not
stated.

# Citations

1. [Li et al. (2018)](/sources/li-2018.md) — §1, §2.1–2.4 (Figs. 3–7), §3 (Eqs. 1–4, Tables 1–2), §4.1–4.2 (Eqs. 5, 12–18, Tables 3–4, Figs. 8–10), §5 (Table 5, Fig. 11).

---
type: Definition
title: "Spectral gap"
description: "Separation in frequency between deterministic unsteadiness (rotor–stator interaction, wake passing, vortex shedding) and the turbulence spectrum; its presence is what makes Reynolds averaging and URANS legitimate, and its absence decides how data-driven URANS closures must be trained (phase-locked against triple-decomposed data)."
status: established
aliases: [spectral gap between deterministic and stochastic unsteadiness, scale separation of URANS]
tags: [rans, turbomachinery, hybrid-rans-les, data-driven, symbolic-regression]
timestamp: 2026-10-27T15:55:00Z
---

# Spectral gap

A flow with deterministic (periodic or organized) unsteadiness has a
**spectral gap** when the frequencies of that unsteadiness do not overlap
the energy spectrum of the stochastic turbulence. Sandberg & Michelassi
(2022), after Tucker (2011), define it as "the scenario in which the
low-frequency deterministic unsteadiness does not overlap with the
turbulence energy spectrum" ([Sandberg & Michelassi (2022)](/sources/sandberg-2022.md),
§3.1.2, Fig. 1). The gap is the condition under which an unsteady
Reynolds average is meaningful: the averaging removes the turbulence and
keeps the deterministic motion, which the URANS equations then resolve
in time while the closure carries only the turbulence.

## Why the gap decides Reynolds averaging

- **URANS assumption.** URANS assumes that the time scales of the blade
  motion exceed the averaged turbulence scales (Sandberg & Michelassi 2022,
  §2.2.2.1). Their Fig. 1 places RANS, URANS, hybrid URANS–LES, LES and
  DNS along the frequency axis of a turbulence spectrum on which
  deterministic unsteadiness is superimposed, with and without a gap.
- **Failure without a gap.** When the deterministic frequencies overlap
  the turbulence spectrum, "any model based on Reynolds averaging will
  fail", because it "cannot account for the stochastic–deterministic
  interaction and the associated energy transfer between the two
  frequency ranges"; scale-resolving simulation is then required
  (Sandberg & Michelassi 2022, §3.1.2, §3.2.3). Sandberg & Zhao (2022)
  state the same in their review of machine-learnt closures, with a
  schematic of the two spectra (Fig. 8)
  ([Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md), §2.5).
- **Where the gap closes in turbomachinery.** Higher rotation speeds of
  modern engines move the rotor–stator frequencies into the turbulence
  range, and trailing-edge vortex shedding (thin trailing edges, high exit
  Mach numbers) adds deterministic content at frequencies close to the
  turbulence (Sandberg & Michelassi 2022, §3.1.2, §3.2.3; see
  [turbine cascades](/benchmarks/turbine-cascade.md) and
  [compressor cascades](/benchmarks/compressor-cascade.md)).
- **Double counting.** In URANS of shedding wakes and trailing-edge
  cooling slots the shedding is accounted for twice, resolved by the
  unsteady solution and again in the closure calibrated on time-averaged
  data, which gives excessive turbulent diffusion, wrong shedding
  frequencies and wake decay; with a constant turbulent Prandtl number
  the gradient-diffusion heat flux then overpredicts the wall temperature
  (Sandberg & Michelassi 2022, §3.2.3; Sandberg & Zhao 2022, §2.3, citing
  Medic & Durbin and Sandberg et al. 2018).

The alternative to URANS when the deterministic motion is not resolved
is the deterministic-stress approach: an additional average over the
rotor–stator interaction time scales produces deterministic stresses
that need their own closure, with the benefit that no unsteady
computation is needed (Sandberg & Michelassi 2022, §2.2.2.1, after van de
Wall et al. 2000). Without a gap, the remedy is a scale-resolving or
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) simulation
(Sandberg & Michelassi 2022, Fig. 1).

## Training data-driven URANS closures

The gap also decides how a learned closure for URANS is trained, because
the training target must contain only what the closure is meant to
model. Sandberg & Zhao (2022, §4.4) review two routes, both with
[gene-expression programming](/methods/symbolic-regression-closure.md) of
[explicit algebraic stress models](/methods/explicit-algebraic-reynolds-stress-model.md):

- **Gap present: phase-locked averaging.** Akolekar et al. (2019) trained
  models on phase-lock-averaged DNS of a low-pressure turbine with
  incoming wakes, 20 phases per wake-passing cycle. A model trained on one
  phase performs well on that phase and on some others (trained on phase
  13, it works on phase 5) but fails on others (trained on phase 10, it
  fails on phase 18); the trends of the linear coefficient and of the
  non-linear contribution follow the wake–wake interaction, so two models
  trained on two representative phases suffice (Sandberg & Zhao 2022,
  §4.4.1, Fig. 10; Sandberg & Michelassi 2022, §4.3, Fig. 7). The error
  measure is the percentage reduction of the normalized mean-square error
  of the learned model relative to the linear baseline.
- **Gap absent: exclude or decompose.** One option is to omit the
  coherent near-wake region from training (Akolekar et al. 2019). The
  other is a triple decomposition of each field into its time average, a
  periodic part and a stochastic part, $\phi=\langle\phi\rangle+\phi_{\mathrm p}+\phi_{\mathrm s}$
  (page-local subscripts; the sources write $\tilde\phi$ and $\phi''$, which
  are the registry's Favre symbols), with the closure trained on the
  stochastic anisotropy only (Lav et al. 2019). The stochastic anisotropy
  was insensitive to whether Fourier, POD or DMD separated the periodic
  part; the learned closure sharply reduces the modelled diffusion, its
  non-linear coefficients are small, and URANS then resolves more scales
  and improves the near and far wake (Sandberg & Zhao 2022, §4.4.2;
  Sandberg & Michelassi 2022, §3.2.3).
- **Heat flux without a gap.** Lav & Sandberg (2020) trained
  gene-expression closures for both the stochastic stress and the
  stochastic heat flux of a trailing-edge cooling slot in URANS, the heat
  flux as a scalar diffusivity function of the invariants multiplying the
  mean temperature gradient. Trained at blowing ratio 1.26 (slot lip
  thickness 1.14 in units of the slot height), the mean learned turbulent Prandtl number
  is 0.471; the adiabatic wall effectiveness at the training blowing ratio
  is "nearly perfect", which the reviewers say "might be fortuitous" since
  the velocity profiles do not match closely; at blowing ratio 0.86 the
  improvement holds up to a streamwise distance of 20 in the source's
  normalization ($x/s=20$) and weakens downstream, attributed to frozen rather than
  [model-consistent](/methods/model-consistent-training.md) training
  (Sandberg & Zhao 2022, §4.4.2, Fig. 11).

## Qualifications

- Both reviews summarize published work; the statements above are the
  reviews' accounts of the cited studies, not new demonstrations.
- In the steady wake-mixing closures of Zhao et al. (2020) the
  improvement came "predominantly" from *more* turbulent diffusion
  (Sandberg & Zhao 2022, §4.1), while the stochastic URANS closure of Lav
  et al. (2019) improves the wake by *less* modelled diffusion (§4.4.2).
  The two statements concern different settings (steady RANS of the
  time-averaged wake against URANS resolving the shedding), and Sandberg &
  Zhao state each in its own context.
- Neither review gives a quantitative measure of the gap (a spectral
  overlap criterion or a frequency ratio); the definition is qualitative
  in both.

# Citations

- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §2.2.2.1, §3.1.2, §3.2.3, §4.3, Figs. 1, 7.
- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) — §2.3, §2.5 Fig. 8, §4.1, §4.4.1 Fig. 10, §4.4.2 Fig. 11.

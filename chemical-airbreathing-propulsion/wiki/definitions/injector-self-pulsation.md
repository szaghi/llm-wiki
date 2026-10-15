---
type: Definition
title: "Self-pulsation of gas–liquid swirl coaxial injectors"
description: "Pressure and flow-rate oscillation of a gas–liquid swirl coaxial injector sustained by time-delayed feedback between the liquid sheet and the gas flow; in a recessed liquid-centered injector it is attributed to periodic blocking of the annular gas by the conical liquid sheet, with a kHz frequency rising linearly with liquid Reynolds number and a jump to an 8–9 kHz band at high gas flow."
status: established
aliases: [self-pulsation, self-oscillation of coaxial injectors, spray self-pulsation, ultra-high frequency pulsation]
tags: [injector-dynamics, swirl-coaxial-injector, two-phase-flow, cold-flow, vof, experiment, liquid-rocket-engine]
timestamp: 2026-10-14T00:00:00Z
---

# Self-pulsation of gas–liquid swirl coaxial injectors

Self-pulsation is "a pressure and flow rate oscillation by a time-delayed
feedback between liquid and gas phases", the definition
[Bai et al. (2018)](/sources/bai-2018.md), §1, attribute to the literature.
It occurs in gas–liquid swirl coaxial injectors, in which a swirling liquid
sheet and a coaxial gas stream meet; the variant studied here is the
liquid-centered swirl coaxial (LCSC) injector, where the liquid issues from a
central swirl stage whose post is recessed behind the injector exit, so that
liquid and gas first interact inside a recess chamber. Bai et al. study it
as a liquid-rocket injector phenomenon in cold flow (water and air), without
combustion; coupling with chamber acoustics, the subject of
[combustion instability](/definitions/combustion-instability.md), is not
tested.

## Competing mechanisms (attributed)

[Bai et al. (2018)](/sources/bai-2018.md), §1, review mechanisms from earlier
work:

| Account | Mechanism | Attributed to |
|---|---|---|
| Recess and acoustic impedance | the LOX-post recess length is the most significant parameter; a "petal-valve" acoustic-impedance model | Bazarov |
| Gas-passage resonance | resonance between the annular gas passage and the gas core | Huang et al. |
| Dominant sheet wave | the dominant wave of the liquid sheet is the excitation; $f$ linear in the liquid and gas Reynolds numbers, more dependent on the liquid one; ambient pressure suppresses self-pulsation | Im et al. |
| Kelvin–Helmholtz excitation | strong self-pulsation without recess, Kelvin–Helmholtz excitation identified by POD | Eberhart et al. |
| Mixing regime | outer, critical and inner mixing, strongest pulsation near critical mixing | Kang et al. |

Bai et al. propose the blocking mechanism below specifically for recessed
LCSC injectors and do not adjudicate against the other accounts.

## Liquid-sheet blocking mechanism

[Bai et al. (2018)](/sources/bai-2018.md), §3.2, Figs. 5, 7, 8, Conclusion 1,
describe one cycle in the recess chamber:

1. the conical liquid sheet moves out to the recess wall and blocks the
   annular gas;
2. the pressure in the confined region rises to a peak;
3. the sheet is pushed toward the centerline and thins;
4. the high-speed gas tears the sheet open;
5. the gas channel opens and the pressure drops rapidly.

The evidence is simulation contours together with high-speed imaging inside a
quartz recess; no causal test is made.

## Frequency

* **Spray frequency equals pressure frequency.** The image-derived spray
  oscillation frequency matches the recess-pressure frequency "in most
  conditions", so the pressure frequency is used as the characteristic
  self-pulsation frequency (§3.3.1, Fig. 10a).
* **Linear law in the liquid Reynolds number (empirical fit).** At a gas mass
  flow of 5 g/s (gas Reynolds number 35700),
  $f = 890 + 0.089\,\mathrm{Re}_l$ (with $f$ in Hz) for
  $6800<\mathrm{Re}_l<39000$, where $\mathrm{Re}_l$ is the liquid Reynolds
  number; self-pulsation disappears outside this range (§3.3.1). The paper
  does not define the Reynolds numbers (length or velocity scale), so the fit
  is not transferable as printed. Read from Fig. 10a, $f$ rises from about
  1700 Hz at $\mathrm{Re}_l\approx7000$ to about 4100 Hz at
  $\mathrm{Re}_l\approx38000$ (the fit gives about 1.5 kHz and 4.3 kHz at
  the same points).
* **Effect of gas flow.** At liquid flows of 40 and 80 g/s, $f$ rises
  slightly with the gas Reynolds number, then falls, and the pulsation
  disappears. At larger liquid flows $f$ stays roughly constant (about
  3–3.7 kHz, read from Fig. 10b), then jumps to an **ultra-high frequency
  (UHF) pulsation** of 8000–9000 Hz (§3.3.1, Fig. 10b). The UHF window is a
  gas flow of 11.67–16.01 g/s at a liquid flow of 160 g/s and 12.55–16.97 g/s
  at 200 g/s.

## High-frequency and ultra-high-frequency waveforms

[Bai et al. (2018)](/sources/bai-2018.md), §3.3.2, Figs. 9, 11:

* **High-frequency (HF) pulsation.** The positive half-wave is much larger
  than the negative one, with a positive peak of about 0.21 MPa absolute.
* **UHF pulsation.** The half-waves are roughly symmetric, with a positive
  peak of about 0.13 MPa; 8332 Hz at liquid 160 g/s and gas 14.5 g/s
  (Fig. 11b).
* **Stated, not shown.** The annular gas reaches sonic speed when UHF occurs;
  a qualitative force balance (lower exterior pressure peaks give a shorter
  cycle) explains the higher frequency. The authors call the two-stage force
  argument "based on the qualitative analysis".

## Flow patterns in the recess

At small liquid flows (40 and 80 g/s) the whole sheet in the recess
oscillates; at large liquid flows the spray angle inside the recess stays
nearly constant and only the downstream sheet oscillates. Stable,
non-pulsating sprays at small or large gas-to-liquid mass ratio are solid
cones whose spray angle decreases with gas flow
([Bai et al. (2018)](/sources/bai-2018.md), §3.1, Figs. 5–6).

## Self-pulsation boundaries

[Bai et al. (2018)](/sources/bai-2018.md), §3.4, Fig. 12, Conclusion 3, map
the boundaries in the plane of liquid momentum flux against gas momentum flux
(each a density times a velocity squared, kg m⁻¹ s⁻²) for liquid flows of 40,
80, 120, 160, 180 and 200 g/s, and claim this is the first such map:

* the **lower (onset) threshold** rises with liquid flow, with a "skewed
  parabola or exponential-like" shape, which they call consistent with Bazarov
  and Im et al.;
* the **upper (vanishing) threshold** falls quickly, "downward
  parabola-like", at small liquid flow and rises slightly, roughly linearly,
  at large liquid flow;
* the **UHF band** has nearly parallel lower and upper boundaries, and no
  spray oscillation occurs between the HF and UHF states.

## Experiment and simulation

[Bai et al. (2018)](/sources/bai-2018.md), §2:

* **Injector.** LCSC with a 5 mm recess, 0.5 mm annular gas gap, swirl stage
  with four tangential 2 mm entries (geometry in Table 1).
* **Experiment.** Water and air into atmospheric ambient; a quartz outer
  injector for backlit high-speed imaging at 30000 frames/s; a miniature
  pressure transducer 3.5 mm upstream of the exit sampled at 1 MHz for 2 s.
  Liquid flow 43.1–285.3 g/s, gas flow 0.545–31.732 g/s (Table 2).
* **Simulation.** 2D axisymmetric-swirl unsteady volume-of-fluid model with
  continuum surface force, RNG k–epsilon turbulence and
  non-equilibrium wall functions; compressible ideal-gas air, incompressible
  water; time step 0.1 µs; intermediate grid of 193360 cells chosen from a
  three-grid study. The solver is not named.
* **Agreement (baseline only).** At liquid 160 g/s and gas 5.0 g/s the
  simulation gives 3246 Hz and 0.12 MPa, the experiment 3165 Hz and about
  0.13 MPa (§3.2, Figs. 8–9). Only the baseline is simulated; the UHF regime
  is not.

# Citations

1. [Bai et al. (2018)](/sources/bai-2018.md) — §1 (definition, literature), §2 (Tables 1–2, numerical model), §3.1–3.4 (Figs. 5–12), Conclusions 1–3.

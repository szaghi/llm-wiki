---
type: Definition
title: "Rotating detonation engine"
description: "Combustor in which one or more detonation waves travel continuously around an annular or hollow cylindrical chamber fed with fresh mixture at its head, characterized by its propagation mode, the wave speed relative to the Chapman–Jouguet speed, its formation transient and its coupling to exit nozzles and turbines."
status: established
aliases: [RDE, rotating detonation combustor, RDC, continuous rotating detonation, CRD, continuous detonation wave engine, continuous spin detonation]
tags: [detonation, rotating-detonation, propagation-mode, velocity-deficit, nozzle, turbine, experiment]
timestamp: 2026-10-14T00:00:00Z
---

# Rotating detonation engine

A rotating detonation engine (RDE) burns a continuously injected mixture in
one or more detonation waves that travel around the circumference of the
combustor, near its injection plane, while the products expand axially to the
exit. The literature uses several names for it: continuous rotating
detonation (CRD), continuous detonation wave engine and "continuous spin
detonation" ([Peng et al. (2018)](/sources/peng-2018.md), §1); Zhou et al.
use rotating detonation combustor (RDC).

## Configurations

| Source | Chamber | Mixture and injection | Exit |
|---|---|---|---|
| [Peng et al. (2018)](/sources/peng-2018.md), §2, Fig. 2 | **hollow** (no centerbody) cylinder, $d_c$ = 100 mm, length 90 mm, with a sudden enlargement downstream of the injector | ethylene–air, non-premixed; air through a convergent–divergent radial slit (0.7 mm throat), ethylene through 90 orifices | 200 mm Laval nozzle, seven interchangeable nozzles with $\varepsilon_c$ = 1, 2, 4, 6, 8, 10, 12 ($\varepsilon_c$ = 1 a straight cylinder) |
| [Zhou et al. (2018)](/sources/zhou-2018.md), §2, Fig. 1 | **annular**, inner diameter 94 mm, $d_c$ = 106 mm (6 mm gap) | hydrogen–air, slot–orifice: hydrogen through 120 orifices of 0.8 mm, air through a 1.5 mm annular slot; both at 282 K | convergent section, turbine guide vane and an axial-flow turbine of 66 mm outer diameter (open cycle) |

Peng et al. attribute the easy initiation of their hollow chamber to two
mechanisms they do not measure (§3.1): the hollow chamber satisfies the
empirical criterion that the channel width exceed half the detonation cell
size (attributed to Bykovskii et al.), and a recirculation zone at the sudden
enlargement holds a deflagration flame that acts as an ignition source.

## Wave speed from frequency

The mean wave speed follows from the measured frequency $f$ of the pressure
peaks at a fixed sensor:

$$D = \frac{\pi d_c f}{n_w},$$

with $f$ the mean of the instantaneous frequencies, each the inverse of a
peak-to-peak interval ([Peng et al. (2018)](/sources/peng-2018.md), §3.2,
Eqs. 1–2, with $d_c$ the chamber diameter), or the dominant FFT frequency
with $d_c$ the outer annulus diameter
([Zhou et al. (2018)](/sources/zhou-2018.md), §3.1, Eq. 1).

* **Critical frequency.** A single wave travelling at $D_{\mathrm{CJ}}$ has
  the frequency $D_{\mathrm{CJ}}/(\pi d_c)$, doubled for two waves; Peng et
  al. use it to bound the mode (§3.1, Fig. 5).
* **Wave count from two sensors.** With two sensors at the same axial station
  separated by an angle of $2\pi/3$, the ratio of the inter-sensor delay to
  the period fixes $n_w$: $n_w$ equals $2\pi$ divided by the separation angle,
  times that ratio ([Peng et al. (2018)](/sources/peng-2018.md), §3.2.2,
  Eqs. 3–5). In their two-wave test the ratio is about 2/3, giving
  $n_w$ = 2. The paper does not discuss the ambiguity that sensor spacing
  introduces into this count (a remark of the reader, not a claim of the
  paper).

## Propagation modes

* **Single wave.** One wave co-rotating around the chamber; the stable state
  of both studies ([Peng et al. (2018)](/sources/peng-2018.md), §3.2.1;
  [Zhou et al. (2018)](/sources/zhou-2018.md), §3.1–3.2).
* **Two co-rotating waves.** In Peng et al. only at $\varepsilon_c$ = 12 and
  $\phi\ge$ 0.99, where the frequency steps from below the single-wave
  critical frequency to between the single- and two-wave values (§3.1,
  Fig. 5b; §3.2.2). In Zhou et al. as the first phase of the formation
  transient (below).
* **Sawtooth wave.** Near the lean limit at $\varepsilon_c$ = 1, 2, 4, Peng
  et al. observe a wave with a very low pressure rise and no steep front
  (§3.2.3, Figs. 10–13). They state, without demonstrating it, that it is "a
  manifestation of high-frequency tangential instability in rocket
  combustor" (see [combustion instability](/definitions/combustion-instability.md))
  and a critical condition of rotating detonation, with too little heat
  release or pressure to couple the inducing shock to the flame: adverse
  factors quench it, favourable ones turn it into a detonation.
* **Two-peak wave and strong–weak alternation.** Transient modes of the
  formation process in Zhou et al. (§3.3).

## Wave speed relative to the Chapman–Jouguet speed

| Source and case | Mode | $\phi$ | $f$ | $D$ | $D/D_{\mathrm{CJ}}$ |
|---|---|---|---|---|---|
| [Peng et al. (2018)](/sources/peng-2018.md), test 1, $\varepsilon_c$ = 4 | single wave | 1.09 | 6.10 kHz | 1915.40 m/s | about 1.038 (computed here from $D_{\mathrm{CJ}}$ = 1845.91 m/s at 1 atm, 300 K) |
| Peng et al., test 2, $\varepsilon_c$ = 12 | two waves | 1.00 | 8.84 kHz | 1387.88 m/s per wave | 0.7462 |
| Peng et al., test 3, $\varepsilon_c$ = 2 | sawtooth | 0.43 | 4.32 kHz | 1356.48 m/s | 0.9297 ($D_{\mathrm{CJ}}$ = 1459.11 m/s) |
| [Zhou et al. (2018)](/sources/zhou-2018.md), $\phi$ = 1, spark plug | single wave | 1 | 4.73 kHz | 1.57 km/s | — |
| Zhou et al., $\phi$ = 1.17 | single wave | 1.17 | 4.79 kHz | 1.59 km/s | — |
| Zhou et al., $\phi$ = 0.6–1.4 (Fig. 11) | single wave (stable above $\phi$ = 0.6) | 0.6–1.4 (Fig. 11 plots $\phi$ = 0.6 although §3.2 states it never stabilised) | — | about 1.32 to 1.65 km/s (read from figure) | stated deficit of about 20 % against CEA $D_{\mathrm{CJ}}$ of about 1.70 to 2.07 km/s (read from figure) |

Peng et al. call test 1 the highest ethylene–air rotating-detonation speed
reported to date, contrast it with velocity deficits above 50 % and sawtooth
waveforms in earlier ethylene–air annular RDEs (attributed), and attribute the
difference to configuration (hollow against annular). They note the super-CJ
reading and refer to the literature for "correction methods" without applying
one; their $D_{\mathrm{CJ}}$ is evaluated at 1 atm and 300 K, and the code is
not stated (§3.2.1). Zhou et al. attribute their deficit, without proof,
mainly to the engine structure and reactant mixing (§3.4); nine runs at
$\phi$ = 0.85 give 1.5–1.55 km/s (Fig. 10).

**Qualification, not contradiction.** The near- or super-CJ ethylene–air
speed of Peng et al. and the 20 % hydrogen–air deficit of Zhou et al. are
not incompatible claims about the same thing. The two measure different
mixtures, in different configurations (hollow chamber with a Laval nozzle
against an annulus feeding a turbine), against $D_{\mathrm{CJ}}$ values
computed at different or unstated reference states, and Peng et al.
themselves report deficits of 7–25 % in their other modes. Neither source
claims a general law that the other's measurement refutes, and both explain
their speed by configuration.

## Operating domain and exit-nozzle contraction ratio

[Peng et al. (2018)](/sources/peng-2018.md), §3.1, §3.3, Figs. 4, 14, 15,
with air at 0.540–0.560 kg/s (540–560 g/s) and $\phi$ = 0.33–1.35:

* **Lean limit.** It rises, and the operating domain shrinks, as
  $\varepsilon_c$ increases: 0.4 at $\varepsilon_c$ = 1, about 0.7 at
  $\varepsilon_c$ = 12 (read from Fig. 4). The rich limit was not sought. The
  trend is inferred, not measured: higher $\varepsilon_c$ lowers the main
  stream velocity and the wave height, so a smaller cell size, hence a higher
  $\phi$, is required.
* **Propagation stability.** Measured by the relative standard deviation of
  the instantaneous frequency (Eqs. 6–7). For $\varepsilon_c$ = 1, 2, 4, 6 it
  decreases with $\phi$, which the authors attribute to the nozzle isolating
  the back pressure; for $\varepsilon_c$ = 8, 10, 12 it increases with
  $\phi$, attributed to a stronger oblique shock reflected from the nozzle
  contraction (a secondary peak behind each main peak, §3.2.2). The two-wave
  mode is the least stable.
* **Best choice.** Around stoichiometric, $\varepsilon_c$ = 2 and 4 give the
  most stable propagation and super-CJ speeds, and the authors conclude that
  $\varepsilon_c$ = 2–4 is the best choice (§3.3, Fig. 15).

## Formation process and ignition

[Zhou et al. (2018)](/sources/zhou-2018.md), §3.2–3.3, Figs. 4–9, at air
0.170 kg/s (170 g/s) and $\phi$ = 0.6–1.4, compare an automotive spark plug
(test 1) and a hydrogen–oxygen pre-detonator (test 2) at the same location:

* **Formation time.** The time to a stable single wave is about 0.15 s with
  the spark plug and 0.02 s with the pre-detonator at $\phi$ = 1; the means
  over $\phi$ are 0.159 s and 0.022 s. It falls as $\phi$ rises; $\phi$ = 0.6
  never stabilised (Fig. 6).
* **Final state.** It does not depend on the igniter: 4.73 kHz and 1.57 km/s
  with the spark plug, 4.7 kHz and 1.56 km/s with the pre-detonator, in
  agreement with the literature (attributed).
* **Mode sequence with spark ignition.** Two co-rotating waves (7.76 kHz in
  the text, 7.67 kHz on the figure label); after about 20 ms a "two-peak"
  wave, still two-wave, at 7.53 kHz; strong–weak alternation (one strong
  wave followed by two weaker ones) for about 0.1 s at 4.91 kHz; a stable
  single wave at 0.148 s. Just before the stable state the authors interpret
  a 5 ms interval in which the downstream sensor reads higher than the
  upstream one as a backward displacement of the reaction zone (Fig. 8).

[Peng et al. (2018)](/sources/peng-2018.md), §2, initiate with a
tangentially connected, spark-ignited hydrogen–oxygen pre-detonator.

## Turbine integration

[Zhou et al. (2018)](/sources/zhou-2018.md) drive a real axial-flow turbine
with the RDE exhaust:

* **Shown.** A stable single hydrogen–air wave forms at every tested
  $\phi$ except 0.6, with either igniter (§3.1–3.2, Conclusion 1). The
  turbine runs at 12000 rpm (200 Hz) at steady state, far below the wave
  frequency of about 4.5 kHz. Shocks are present in front of the guide vane,
  part of the oblique shock reflecting back into the combustor from the
  concave blade surfaces (incidence about 25°); the authors state that the
  reflection has a minor influence (§3.1, Fig. 3d).
* **Hypothesis.** The authors compare their 0.15 s formation time with
  2.23 ms in their earlier turbine-free combustor and infer "relatively large
  effects of turbine": the dependence of the formation time on $\phi$ and on
  the igniter is attributed to how fast the turbine spins up. No
  turbine-free control and no turbine-speed history are given, and they
  concede that a rule linking turbine speed to wave behaviour is hard to
  extract (§3.2).

# Citations

1. [Peng et al. (2018)](/sources/peng-2018.md) — §1, §2 (Fig. 2), §3.1 (Figs. 4–5), §3.2.1–3.2.3 (Eqs. 1–5, Figs. 6–13, Table 1), §3.3 (Eqs. 6–7, Figs. 14–15).
2. [Zhou et al. (2018)](/sources/zhou-2018.md) — §1, §2 (Fig. 1), §3.1 (Eq. 1, Fig. 3), §3.2 (Figs. 4–6), §3.3 (Figs. 7–9), §3.4 (Figs. 10–11), Conclusion 1.

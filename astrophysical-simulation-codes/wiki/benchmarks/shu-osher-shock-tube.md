---
type: Benchmark
title: "Shu–Osher shock tube"
description: "A shock running into a sinusoidal density field, which leaves a train of short-wavelength entropy oscillations behind it; a qualitative check of how much small-scale structure a shock-capturing scheme keeps at a given resolution, run by Athena, Athena++, Quokka and AthenaK against fine-grid references."
status: established
aliases: [Shu-Osher problem, shock–entropy interaction, shock-entropy wave interaction]
tags: [benchmark, hydro, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Shu–Osher shock tube

**Set-up.** A shock moves into gas at rest whose density varies
sinusoidally; behind the shock the density perturbation becomes a train of
short-wavelength oscillations that low-order or diffusive schemes smear.
There is no exact solution, so every run below compares with a
fine-grid reference. The states are printed only by
[Wibking & Krumholz (2022)](/sources/wibking-2022.md) (§3.1.5,
eqs. 46–51): on the left $\rho = 3.857143$, $v_x = 2.629369$,
$p = 10.33333$; on the right $\rho = 1 + 0.2\sin(5x)$, $v_x = 0$, $p = 1$.
[Stone et al. (2008)](/sources/stone-2008.md) (§8.1) give the domain
$-1 \le x \le 1$, the shock at $x = -0.8$, $\gamma = 1.4$ and
$t = 0.47$; the domain, shock position and final time of the Quokka run
are not in the evidence read.

**Runs.**

* [Stone et al. (2008)](/sources/stone-2008.md), §8.1, Fig. 10.
  [Athena](/software/athena.md), 200 and 800 cells, PPM with the
  Colella–Sekora extremum-preserving limiters, HLLC. The solution is
  "similar" to third-order WENO (Balsara & Shu 2000, Fig. 5), and the
  Colella–Sekora limiters improve it significantly.
* [Stone et al. (2020)](/sources/stone-2020.md), §3.3.3, Fig. 14.
  [Athena++](/software/athena-plus-plus.md), $t = 0.47$, $N = 200$, HLLC,
  VL2+PPM against RK3+PPM, reference RK3+PPM at $N = 8192$. RK3+PPM
  captures the short-wavelength oscillations and outperforms the VL2 run.
  Recorded as printed: the text names the compared run both VL2+PPM and
  VL2+PLM.
* [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3.1.5, Fig. 4.
  [Quokka](/software/quokka.md), 400 cells, PPM on primitive variables,
  RK2-SSP, HLLC, against an Athena++ reference of 1600 cells (VL2,
  characteristic PPM, HLLC). Agreement is "very good", comparable to
  third-order ENO; with PLM at 400 cells the high-frequency features
  alias (not shown).
* [Stone et al. (2026)](/sources/stone-2026.md), §3.1, Fig. 1 (right).
  [AthenaK](/software/athenak.md), 200 cells, PLM+RK2 against WENOZ+RK3,
  reference 2000 cells with RK3+WENOZ, at $t = 0.047$ as printed (the
  Athena and Athena++ runs end at $0.47$). WENOZ "captures small scales
  ... more accurately than PLM". Precision is not stated.

**What it shows.** All four comparisons are visual; none reports an
error norm. They agree in direction: at fixed resolution, higher-order
or less dissipative reconstruction (extremum-preserving PPM limiters,
RK3+PPM, PPM rather than PLM, WENOZ rather than PLM) keeps more of the
post-shock oscillation train. The test is the bundle's standard 1D check
of small-scale fidelity behind a shock, complementary to the
[Sod shock tube](/benchmarks/sod-shock-tube.md), which Stone et al. (2008)
no longer regard as discriminating.

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §8.1.
2. [Stone et al. (2020)](/sources/stone-2020.md), §3.3.3.
3. [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3.1.5 (arXiv v2).
4. [Stone et al. (2026)](/sources/stone-2026.md), §3.1 (arXiv v1).

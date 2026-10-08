---
type: Benchmark
title: "Shu–Osher shock/entropy-wave interaction"
description: "A Mach 3 shock running into a sinusoidal density (entropy) field: smooth structure behind a shock, where high-order capturing schemes show their largest advantage over TVD schemes."
status: established
aliases: [Shu-Osher problem, shock-entropy wave interaction, Shu's problem]
tags: [benchmark, euler, shock-turbulence, high-order]
timestamp: 2026-10-08T00:00:00Z
---

# Shu–Osher shock/entropy-wave interaction

**Set-up** ([Shu & Osher (1989)](/sources/shu-1989.md), Example 8). The
1D Euler equations with a right-moving Mach 3 shock entering a state
whose density carries a sine perturbation of amplitude $\varepsilon$
($\varepsilon = 0.2$; $\varepsilon = 0$ is a pure shock). The post-shock
state printed in later uses is
$(\rho, v, p) = (3.857143,\ 2.629369,\ 10.3333)$
([Jiang & Shu (1996)](/sources/jiang-1996.md);
[Suresh & Huynh (1997)](/sources/suresh-1997.md)). The interaction
generates a band of fine density oscillations behind the shock.

**What it measures.** Accuracy of smooth structure behind a shock: the
whole difficulty is resolving the oscillations without shock-generated
noise. Results in this corpus:
* third-order ENO-RF with 200 points matches a second-order MUSCL TVD
  scheme with 800 in density; velocity and pressure, lacking structure,
  gain less ([Shu & Osher (1989)](/sources/shu-1989.md));
* $r = 5$ MPWENO with 200 zones converges to an 800-zone reference, every
  extremum matched with no more than 11 points between extrema; $r = 3$
  WENO needs 400 ([Balsara & Shu (2000)](/sources/balsara-2000.md), §VI.d);
* MP5 and WENO5 compared by [Suresh & Huynh (1997)](/sources/suresh-1997.md).

**Weak-wave variant** ([Jiang & Shu (1996)](/sources/jiang-1996.md),
§8.2 Example 2). Amplitude $\varepsilon = 0.01$, wave number $k = 13$ on
$[0, 5]$; the shock is run to $x = 4.5$ and shuffled back to remove the
start-up transient. The amplified entropy wave is compared with the
linear-theory amplitude 0.08690716. At 800 points (about 20 per
wavelength) the fourth-order Liu–Osher–Chan WENO is best and WENO5
second; at 1200 they are equal, and WENO5 wins on finer grids. A
second-order TVD scheme with 2000 points is clearly worse.

**2D variant** (Example 4 of §8.3): a normal Mach 3 shock and an oblique
weak entropy wave; linear-theory amplitude 0.08744786. ENO-LF-4/5 lose
accuracy unless biased; WENO works without modification, and the biased
"WENO2" variants are better still; the pressure–entropy weights fail.

# Citations

1. [Shu & Osher (1989)](/sources/shu-1989.md), §V Example 8.
2. [Jiang & Shu (1996)](/sources/jiang-1996.md), §§8.2–8.3.
3. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §4.2 Example 3.
4. [Balsara & Shu (2000)](/sources/balsara-2000.md), §VI.d.

---
type: Benchmark
title: "DIII-D reversed-shear Alfvén eigenmode benchmark"
description: "Linear multi-code verification and validation case of n = 3–6 reversed-shear Alfvén eigenmodes in DIII-D discharge #159243 at 805 ms (Taimourzadeh et al. 2019), with a kinetic-EFIT equilibrium and Maxwellian energetic particles; run by M3D-C1-K and GMEC, whose growth rates sit with the lower group of codes."
status: established
aliases: [DIII-D RSAE benchmark, Taimourzadeh RSAE benchmark, DIII-D 159243 benchmark]
tags: [benchmark, verification, alfven-eigenmode, energetic-particles, hybrid-kinetic]
timestamp: 2026-10-16T00:00:00Z
---

# DIII-D reversed-shear Alfvén eigenmode benchmark

This benchmark tests the linear drive of
[RSAEs](/definitions/reversed-shear-alfven-eigenmode.md) in a real
reversed-shear discharge, DIII-D #159243 at 805 ms. The case is the
multi-code V&V exercise of Taimourzadeh et al. (2019), built on the
discharge of Collins et al. (2016). Neither paper is ingested; the case is
known here through two hybrid codes
([Liu et al. (2022)](/sources/liu-2022.md), §6.3;
[Liu et al. (2024)](/sources/liu-2024.md), §III D).

## Setup

- **Equilibrium.** A kinetic-EFIT reconstruction with $q_{\min}=2.94$ at
  $\sqrt{\psi_{t,N}}=0.4$ (both sources). GMEC uses a VMEC equilibrium built
  from $q$ and the total pressure. Its boundary is
  $R=R_0+r\cos[\theta+\arcsin(0.0528165)\sin\theta]$, $Z=1.49557\,r\sin\theta$
  (elongation 1.49557, triangularity 0.0528165)
  ([Liu et al. (2024)](/sources/liu-2024.md), §III D).
- **EPs.** Isotropic Maxwellian, with density and temperature profiles from
  kinetic EFIT (both sources).
- **Modes.** $n=3$–6, with FLR.

## Results (values read off the figures unless printed)

| $n$ | M3D-C1-K $\omega/2\pi$ [kHz] | M3D-C1-K $\gamma$ [$10^4$ s$^{-1}$] | GMEC $\omega/2\pi$ [kHz] | GMEC $\gamma$ [$10^4$ s$^{-1}$] |
|---|---|---|---|---|
| 3 | ≈ 62 | low end of 1.2–2.5 | ≈ 65 | ≈ 1.0 |
| 4 | — | peak range | ≈ 68 | ≈ 2.1 |
| 5 | — | ≈ 2.3 | ≈ 72 | ≈ 2.6 |
| 6 | ≈ 82 | ≈ 1.7 | ≈ 77 | ≈ 1.6 |

The values come from [Liu et al. (2022)](/sources/liu-2022.md) (§6.3,
Fig. 7) and [Liu et al. (2024)](/sources/liu-2024.md) (§III D, Fig. 17).

- **M3D-C1-K.** The frequency rises from about 62 to 82 kHz over $n=3$–6.
  $\gamma$ spans about 1.2–2.5 $\times10^4$ s$^{-1}$ and is largest at
  $n=4$–5. The $n=4$ mode is localized at $q_{\min}$ and dominated by $m=12$
  (Fig. 8).
- **GMEC.** For $n=4$ the paper prints $\omega\tau_A=0.092972$ and
  $\gamma\tau_A=0.004593$ ($\tau_A=R_0/v_A$ on axis). That mode is dominated
  by $m=12$ with weak $m=11,13$, and its structure agrees with EUTERPE and
  GTC. GMEC's most unstable mode is $n=5$. The Fig. 17 caption swaps the
  panel labels.

## Code-to-code spread

- **M3D-C1-K.** Liu et al. (2022, §6.3) state that the results "agree well"
  with the other initial-value MHD and gyrokinetic codes. Read off Fig. 7,
  M3D-C1-K's $\gamma$ at $n=5$–6 (about 2.3 and 1.7 $\times10^4$ s$^{-1}$)
  sits with the lower group (GTC, GYRO, ORB5, EUTERPE). It is well below
  NOVA (about 4.3 and 4.9) and FAR3D (about 3.9 and 4.2). The paper does
  not discuss this spread
  ([Liu et al. (2022)](/sources/liu-2022.md)).
- **GMEC.** Liu et al. (2024) word the agreement three ways: "agrees
  reasonably" (§I), "agrees well" (§III D) and "close to" (§IV). The
  other-code curves of its Fig. 17 (MEGA, GEM, GTC, EUTERPE, M3D-C1) are
  copied from Fig. 7 of Liu et al. (2022). GMEC's $\gamma$ at $n=3$ is at
  the low side of the spread. GMEC peaks at $n=5$, like MEGA, but MEGA's
  $\gamma$ is higher ([Liu et al. (2024)](/sources/liu-2024.md)).
- **M3D-C1-K against GMEC.** The two hybrid codes agree on
  the rise of frequency with $n$ and on the $m=12$ structure. GMEC's
  frequencies cover a narrower range (65 to 77 kHz against 62 to 82 kHz,
  compiler's reading of the two figures).

## Contradictions

None between the two sources. Both report agreement and neither discusses
the NOVA/FAR3D outliers. The spread with those eigenvalue codes is open
inside the multi-code benchmark itself, which is not ingested.

# Citations

- [Liu et al. (2022)](/sources/liu-2022.md): M3D-C1-K RSAE runs, $n=3$–6, with FLR.
- [Liu et al. (2024)](/sources/liu-2024.md): GMEC RSAE runs, VMEC boundary, the $n=4$ eigenvalues.

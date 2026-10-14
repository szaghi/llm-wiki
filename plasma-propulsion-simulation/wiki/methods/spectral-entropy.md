---
type: Method
title: "Spectral entropy of plasma oscillations"
description: "The normalized Shannon entropy of the Fourier power spectrum of a field, in one or two dimensions, used as a scalar measure of how organized the azimuthal electric-field fluctuations of a Hall-thruster PIC simulation are; 0 means one mode holds all the power, 1 means power spread uniformly."
status: established
aliases: [normalized spectral entropy, Fourier power spectral entropy, power spectral entropy]
tags: [instability, oscillation, pic, hall-thruster, anomalous-transport]
timestamp: 2026-10-14T00:00:00Z
---

# Spectral entropy of plasma oscillations

## Definition

For a signal with Fourier coefficients indexed by the wavenumber $k$, let the normalized power of mode $k$ be the squared modulus
of its coefficient divided by the sum of the squared moduli over all
modes. The spectral entropy is the Shannon entropy of this distribution,
$-\sum_k(\text{normalized power})\ln(\text{normalized power})$, and the
normalized spectral entropy $H$ divides it by the logarithm of the number
of modes, so that $0\le H\le1$. The 2D version sums over both wavenumber
components of a 2D field and divides by the logarithm of the number of 2D
modes ([Miranda et al. (2026)](/sources/miranda-2026.md), §2.2,
eqs. 5–11).

* $H=0$: one mode holds all the power, a fully ordered field.
* $H=1$: the power is spread uniformly over all modes.

The authors had applied it before to drift-wave models, mean-field dynamos
and a Keplerian shear flow (§2.2).

## Application to Hall-thruster PIC

Miranda et al. (2026) apply it to the azimuthal electric field $E_\theta$
of 2D axial–azimuthal [PIC-MCC](/methods/pic-mcc.md) simulations of an
SPT-100-like thruster (XOOPIC, xenon and argon, no permittivity or
mass scaling), averaging over the last 10 snapshots:

| Gas | $H$ (1D, azimuthal line) | $H$ (2D, axial–azimuthal field) | mean electron axial velocity (m/s) |
|---|---|---|---|
| Xe | $0.57\pm0.05$ | $0.79\pm0.003$ | $-3488.2\pm1592.9$ |
| Ar | $0.44\pm0.12$ | $0.65\pm0.119$ | $-6328.4\pm2346.6$ |

(§3, Table 1; the axial velocity is averaged over $0.015<z<0.030$.) The
argon field carries a ~10 mm wave superposed on the ~1 mm
[electron drift instability](/definitions/electron-drift-instability.md),
which the authors give as the reason for its lower entropy (§3–4).

**Claims and their status.**
* Shown, on the means only: the argon azimuthal field is more organized
  than the xenon one by this measure, and argon has the larger mean
  electron axial velocity (§3). The 1D-$H$ and velocity differences lie
  within about one standard deviation ($H$ 0.44 ± 0.12 against
  0.57 ± 0.05; velocity −6328 ± 2347 against −3488 ± 1593 m/s), and the
  2D-$H$ difference within about 1.2 standard deviations of the argon
  value; the paper reports no significance test.
* Stated interpretation: the waves act as coherent structures, so the
  instability-driven microturbulence "is not a completely random process"
  (§4–5).
* Conjecture: "a link between ordered patterns due to the presence of
  plasma waves and an increase of anomalous transport, which must be
  verified carefully" (§4–5). Unpublished neon runs (no instability, low
  axial velocity, high entropy) are said to "appear to confirm" it; no data
  are shown. See [anomalous electron transport](/definitions/anomalous-electron-transport.md).
* Open: $H$ in 2D exceeds $H$ in 1D, which the authors attribute to random
  field fluctuations in different regions that may be physical or may be
  noise from low-density regions; a particles-per-cell study was under way
  (§4). They cite work on the robustness of spectral entropy to noise.

**Limits of the evidence.** The runs do not reach a steady state (start-up
transients). Two gases, one geometry, no convergence or particle-count
study, no benchmark comparison and no experiment (§3–4).

# Citations

1. [Miranda et al. (2026)](/sources/miranda-2026.md), §§2.2, 3, 4, 5, eqs. 5–11, Table 1.

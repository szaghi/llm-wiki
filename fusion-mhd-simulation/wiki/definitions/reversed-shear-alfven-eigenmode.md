---
type: Definition
title: "Reversed-shear Alfvén eigenmode (RSAE)"
description: "Shear-Alfvén eigenmode localized at the minimum of a non-monotonic safety-factor profile, dominated by the single harmonic m ≈ n q_min, whose frequency rises with toroidal mode number and follows q_min in time; benchmarked in this bundle on DIII-D #159243."
status: established
aliases: [RSAE, Alfvén cascade, reversed shear Alfvén eigenmode]
tags: [alfven-eigenmode, energetic-particles, hybrid-kinetic, tokamak]
timestamp: 2026-10-16T00:00:00Z
---

# Reversed-shear Alfvén eigenmode (RSAE)

A reversed-shear Alfvén eigenmode lives in a plasma whose safety factor is
non-monotonic, with a minimum $q_{\min}$ off axis. The mode is localized
radially at $q_{\min}$ and dominated by the single poloidal harmonic with
$m\approx nq_{\min}$. Energetic particles (EPs) drive it
([Liu et al. (2022)](/sources/liu-2022.md), §6.3;
[Liu et al. (2024)](/sources/liu-2024.md), §III D). The local shear vanishes
at $q_{\min}$, so the mode sits near the extremum of a single continuum
rather than in a gap between two coupled harmonics. This single-harmonic
structure separates it from a
[TAE](/definitions/toroidal-alfven-eigenmode.md). Its frequency increases
with $n$ ([Liu et al. (2022)](/sources/liu-2022.md), Fig. 7;
[Liu et al. (2024)](/sources/liu-2024.md), Fig. 17).

## Examples in the sources

- **DIII-D #159243 at 805 ms**, with $q_{\min}=2.94$ at $\sqrt{\psi_{t,N}}=0.4$
  ([DIII-D RSAE benchmark](/benchmarks/diii-d-rsae-benchmark.md)).
  - M3D-C1-K: the $n=4$ mode is localized at $q_{\min}$ and dominated by
    $m=12$ ([Liu et al. (2022)](/sources/liu-2022.md), Fig. 8).
  - GMEC: $m=12$ with weak $m=11,13$ sidebands, with
    $\omega\tau_A=0.092972$ and $\gamma\tau_A=0.004593$
    ($\tau_A=R_0/v_A$ on axis). Its structure agrees with EUTERPE and GTC
    ([Liu et al. (2024)](/sources/liu-2024.md), §III D, Figs. 15–16).
  - In both codes the frequency rises across $n=3$–6, and the most unstable
    modes are $n=4$–5.
- **ASDEX Upgrade #31213, JOREK.** The core $q$ profile becomes flat
  ($s<0.4$) for $t\ge0.75$ s. JOREK then finds $n=1$, $m=2$ modes at
  85–60 kHz ($\omega/2\pi$), classified as RSAEs in Table I
  ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §V).
  - The modes at 0.75–0.84 s are absent from the Mirnov spectrogram. The
    authors attribute the mismatch to the uncertainty of the core $q$
    profile, which strongly perturbs the core continuum (Figs. 16–17).
  - The Fig. 16 caption calls the $t\ge0.75$ s modes "m=2 EPMs or low-shear
    modes", while Table I says RSAE. The label is uncertain within the
    paper.
- **NLED-AUG on-axis case.** In the linear benchmark of Vlad et al. (2021),
  as restated by [Vlad et al. (2025)](/sources/vlad-2025.md) (§1), HYMAGYC
  and MEGA found an RSAE near $q_{\min}$ and ORB5 an external TAE. Scans of
  EP density or temperature reconciled the two results by showing different
  thresholds, "likely" due to different damping.

## Contradictions

**RSAE versus EPM/low-shear labelling in AUG #31213.** Open, within one
source. [Bogaarts et al. (2022)](/sources/bogaarts-2022.md) classify the
$t\ge0.75$ s modes as RSAE in Table I. Their Fig. 16 caption calls them
"m=2 EPMs or low-shear modes". Settling it needs a continuum-resolved
classification of the modes, with an uncertainty band on the core $q$
profile.

# Citations

- [Liu et al. (2022)](/sources/liu-2022.md): the DIII-D RSAE in M3D-C1-K.
- [Liu et al. (2024)](/sources/liu-2024.md): the DIII-D RSAE in GMEC.
- [Bogaarts et al. (2022)](/sources/bogaarts-2022.md): RSAEs in AUG #31213 and the $q$-profile sensitivity.
- [Vlad et al. (2025)](/sources/vlad-2025.md): the RSAE/TAE divergence in the NLED-AUG on-axis linear benchmark.

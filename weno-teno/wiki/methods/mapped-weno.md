---
type: Method
title: "Mapped WENO"
description: "Mapped WENO (WENO-M, Henrick, Aslam & Powers) passes the Jiang–Shu nonlinear weights through a mapping function, restoring the fifth-order condition at first-order critical points at a higher cost than WENO-JS; the bundle's sources recall it, without printing the mapping, as the first remedy for critical-point order loss."
status: established
aliases: [WENO-M, mapped weights, Henrick mapping, mapping-function-free WENO-M]
tags: [weno, reconstruction, finite-difference]
timestamp: 2026-10-22T00:00:00Z
---

# Mapped WENO

Mapped WENO (WENO-M) of Henrick, Aslam & Powers corrects the [WENO-JS](/methods/weno-js-reconstruction.md)
weights $\omega_k$ through a mapping function $g(\omega)$ (Luo & Wu 2021, §1: "a mapping function to
correct the WENO-JS weights"; Deng 2023, §1: "modifies the non-linear weights through a mapping
function"; Takagi et al. 2022, §1: "remapping the WENO5-JS nonlinear weights"). None of the ingested
sources prints the mapping function itself, so its form is not recorded here.

## What the sources record

- **Purpose: critical points.** WENO-M was designed because WENO-JS fails to recover the optimal
  order at critical points (Deng 2023, §1; Fu 2021, §1; Takagi et al. 2022, §1; Balsara et al. 2024,
  §I). Li et al. (2022, §2) recall that it satisfies the fifth-order condition at first-order
  critical points ([critical-point accuracy](/properties/critical-point-accuracy.md)). Wang et al.
  (2021, §1) describe it as one of "two important variants" for "achieving optimal order near critical
  points", whose "nonlinear weights are pushed smoothly to the optimal values by a regularization
  process", the other being [WENO-Z](/methods/weno-z.md). Deng (2023,
  §1) adds that Henrick et al. also pointed out the sensitivity of WENO schemes to the regularization
  $\epsilon$.
- **Cost.** Luo & Wu (2021, §1) state that the mapping functions "dramatically" increase the
  computational expense, and recall Hong's mapping-function-free WENO-M, which uses a pre-discrete
  mapping to reduce that cost. Deng (2023, §1) and Luo & Wu (2021, §1) recall that
  [WENO-Z](/methods/weno-z.md) is more accurate than WENO-JS and cheaper than WENO-M, and Deng
  (2023, §4.3) that WENO-Z3 gives sharper solutions than mapped WENO.
- **Resolution.** Luo & Wu (2021, §1) recall that WENO-M "achieves significantly better results than
  WENO-JS for both discontinuities and smooth structures"; Fu (2023, §2.3) that WENO-M and WENO-Z
  "show better spectral resolution" than WENO-JS.
- **Comparisons.** In Fu's review (2023, §5.2, Fig. 18, reproduced from earlier work) TENO5 captures
  the cellular structure of a two-dimensional self-sustained detonation on coarse meshes better than
  WENO5-JS and WENO-M, and WENO5-JS gives incorrect cellular structures
  ([targeted ENO](/methods/targeted-eno.md)).

- **In codes.** Bryngelson et al. (2021, §4.1) cite Henrick, Aslam & Powers among the WENO
  references of the MFC solver, but do not state whether MFC uses mapped weights
  ([MFC](/software/mfc.md)).

## Place in the family

Mapped weights, WENO-Z and its descendants ([WENO-Z+](/methods/weno-z-plus.md),
[WENO-ZN](/methods/weno-zn.md)) all act only on the nonlinear weights of the same candidate
stencils. Fu (2023, §1) groups WENO-M and WENO-Z as the improvements for the order-degeneration
problem, distinct from the strategies that target dissipation (freezing the nonlinear adaptation,
raising the weights of non-smooth stencils, hybridization, spectral optimization).

## Qualifications

- The page records only what the ingested sources state about WENO-M; the mapping function, its
  parameters and the proofs belong to Henrick et al., which is not ingested.

# Citations

- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §1.
- [Deng (2023)](/sources/deng-2023.md) — §1; §4.3.
- [Li et al. (2022)](/sources/li-2022-b.md) — §2.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §1.
- [Fu (2021)](/sources/fu-2021.md) — §1.
- [Fu (2023)](/sources/fu-2023.md) — §1; §2.3; §5.2, Fig. 18.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §I.
- [Wang et al. (2021)](/sources/wang-2021.md) — §1.
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §4.1.

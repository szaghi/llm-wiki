---
type: Source
title: "Wang & Kreiss (2017) — Convergence of summation-by-parts finite difference methods for the wave equation"
description: "Normal-mode convergence theory: the two-order gain from localized boundary truncation error requires the determinant condition, which many common SBP-SAT discretizations fail at s = 0."
resource: "doi:10.1007/s10915-016-0297-3"
source_kind: paper
authors: [Wang S., Kreiss G.]
year: 2017
venue: "J. Sci. Comput. 71:219-245"
local_file: "~/papers/mosaic/div-free-amr/2017-JSC-Wang-101007s10915-016-0297-3.pdf"
tags: [sbp, sat, convergence, normal-mode-analysis, accuracy, wave-equation]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The convergence-rate theory behind the SBP interface accuracy story: for
the second-order wave equation with
[SBP-SAT](/methods/sbp-sat.md) boundary/interface treatment, the observed
rate exceeds the order of the (localized) boundary truncation error — the
"gain in convergence." Laplace-transforming the error equation gives the
*boundary system*; if it is nonsingular for all $\mathrm{Re}(s)\ge 0$ (the
**determinant condition**), two orders are gained. The paper's central
finding: **many common discretizations fail the determinant condition at
$s = 0$**, and then careful analysis of the error equation shows the true
gain "can be lower than, equal to or higher than two orders, depending on
the boundary condition and numerical boundary treatment." Verified
numerically with very good agreement.

# Key claims

1. **Stability ≠ accuracy gain**: an energy estimate guarantees only a
   $1/2$-order gain (and is "often not sharp"); pointwise stability does
   *not* imply the determinant condition for the wave equation
   (counterexample in their appendix) — the rate question is genuinely
   separate from the stability question.
2. **The $s=0$ failure is generic**: the marginal mode at zero frequency
   is where common SBP-SAT closures lose the determinant condition — the
   analytical root of the interface order-loss phenomena later
   catalogued and repaired
   ([SBP-preserving interpolation, accuracy bound](/operators/sbp-preserving-interpolation.md)).
3. **Rule-of-thumb calibrated**: the folklore "gain = order of the
   spatial derivative" is neither guaranteed nor an upper bound — the
   machinery to compute the actual gain per closure is provided.

# Notation map

| Wang & Kreiss | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| SBP-SAT wave discretization | $\mathsf{D}_2$-based semi-discretization | second-order form |
| determinant condition | boundary-system nonsingularity, $\mathrm{Re}(s)\ge 0$ | optimal-gain criterion |
| gain in convergence | rate minus boundary truncation order | localized-error effect |

# Pages created or updated

* Updated [Summation by parts (SBP)](/definitions/summation-by-parts.md) (convergence-gain theory; determinant condition).

# Citations

1. `~/papers/mosaic/div-free-amr/2017-JSC-Wang-101007s10915-016-0297-3.pdf` (doi:10.1007/s10915-016-0297-3) — text extraction, pp. 219–245.

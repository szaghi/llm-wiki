---
type: Result
title: "SBP operator existence and families"
description: "SBP first-derivative operators exist at every interior order; the achievable boundary orders and parameter families are catalogued per norm class."
status: established
tags: [sbp, existence, boundary-closure, high-order]
timestamp: 2026-07-08T00:00:00Z
---

# SBP operator existence and families

Results of [Strand (1994)](/sources/strand-1994.md) for
[SBP](/definitions/summation-by-parts.md) approximations of $d/dx$.

**Existence** (his Theorem 2.2): for every $\tau + 1 = 2s$ there exist a
norm $\mathsf{H}$ of full form and an operator accurate of order $\tau$ at
the boundary points and $\tau+1$ in the interior satisfying the SBP rule —
high-order SBP closures exist at every order; the question is only their
class and cost.

**The catalogue:**

| Norm class | Boundary order $\tau$ | Interior order | Family |
|---|---|---|---|
| diagonal | $1, 2$ | $2\tau$ | unique |
| diagonal | $3$ | $6$ | one-parameter |
| diagonal | $4$ | $8$ | three-parameter |
| full | $3, 5$ | $\tau+1$ | two-/three-parameter |
| restricted full | $3$ | $4$ | three-parameter |

Free parameters are spent minimizing operator bandwidth (memory/work on
parallel machines): e.g. diagonal-norm $\tau=3$ reduces to nine nonzero
diagonals, $\tau=4$ to eleven.

**Two load-bearing caveats:**

1. **Only diagonal norms are safe for systems.** For first-order hyperbolic
   *systems*, stability proofs exist only for the diagonal-norm class; full
   and restricted-full norms lack them and "should not be used" there.
   Since diagonal norms also give interior order $2\tau$ at the same
   boundary bandwidth, they dominate in practice — at the price that
   boundary accuracy is capped ($\tau \le 4$ evaluated) and globally one
   expects order $\tau+1$.
2. **Finite-precision fragility.** The exact rational coefficients of
   higher-order closures involve very large integers; whether the SBP
   energy identity survives floating-point round-off is doubted explicitly
   — an early flag of the exactness-vs-arithmetic gap that matters for any
   "exact algebraic invariant" claim.

# Citations

1. [Strand (1994)](/sources/strand-1994.md), Theorems 2.1–2.3, §4–6, Appendices A–B.

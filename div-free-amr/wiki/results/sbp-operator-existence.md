---
type: Result
title: "SBP operator existence and families"
description: "SBP first-derivative operators exist at every interior order; the achievable boundary orders and parameter families are catalogued per norm class."
status: established
tags: [sbp, existence, boundary-closure, high-order]
timestamp: 2026-10-13T00:00:00Z
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

**Origin and the locus of the free parameters.** The diagonal-norm rows ($\tau = 1$–$4$, interior $2\tau$) and the full-norm rows ($\tau = 3, 5$) were first constructed by [Kreiss & Scherer (1974)](/sources/kreiss-scherer-1974.md) (Theorem 2.1, Table 1; Lemma 2.3, Table 2). They prove no SBP operator exists in the unweighted norm (Lemma 2.1). When the diagonal norm carries weights on the first $2\tau$ points, these weights are uniquely determined by their eq. 2.24. Strand's one- and three-parameter diagonal families at $\tau = 3, 4$ therefore live in the operator's boundary block, not in $\mathsf{H}$. For the full norm, Kreiss–Scherer additionally state interior order $\tau+2$ for even $\tau$ (Lemma 2.3, $\tau \le 8$). Caveat 1 is Strand's: Kreiss–Scherer apply their operators to symmetric systems without distinguishing norm classes (§3). Caveat 2 has a precursor in their "single precision only" eigenvalues (Table 2) and their doubt about $\tau > 4$ (p. 207).

# Citations

1. [Strand (1994)](/sources/strand-1994.md), Theorems 2.1–2.3, §4–6, Appendices A–B.
2. [Kreiss & Scherer (1974)](/sources/kreiss-scherer-1974.md), §2, Lemmas 2.1–2.3, Theorem 2.1, Tables 1–2.

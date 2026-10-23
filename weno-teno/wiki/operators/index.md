# Operators

Discrete operators with an algebraic identity.

* [Cell-average to point-value conversion](/operators/cell-average-point-value-conversion.md) — Explicit symmetric-stencil formulas that turn line, face or cell averages into centre point values and back to a prescribed even order; with them a finite-volume scheme reconstructs one value per face and evaluates the flux pointwise, and without them it is second order in multi-D.
* [Logarithmic mean](/operators/logarithmic-mean.md) — The logarithmic mean of two positive numbers, the jump of a quantity divided by the jump of its logarithm, makes two-point fluxes entropy-conservative for entropies with logarithmic terms; the page gives its identity and mean inequalities, its stable, division-reduced and truncated evaluations, its cost, an exponential variant, and the fluxes that use it.
* [Summation-by-parts operator](/operators/summation-by-parts-operator.md) — A first-derivative matrix D with a symmetric positive-definite norm M is summation-by-parts when MD + DᵀM equals the boundary operator; LGL collocation (DGSEM) has this property with diagonal norm, which yields the strong–weak equivalence, the skew-symmetric flux-differencing operator, the flux form of nodal DG and its entropy proofs, and sparse low-order SBP operators on quadrilaterals and triangles.

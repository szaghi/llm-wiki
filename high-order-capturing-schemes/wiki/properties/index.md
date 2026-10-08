# Properties

Constraints and invariants a method can hold.

* [Accuracy at critical points](/properties/accuracy-at-critical-points.md) — Whether a nonlinear capturing scheme keeps its design order where derivatives of the solution vanish (smooth extrema, flat extrema, sonic points); limiters, stencil switches and smoothness indicators can each cost order there.
* [Total variation diminishing (TVD) and bounded (TVB)](/properties/total-variation-diminishing.md) — TVD: the discrete total variation does not grow; TVB: it stays uniformly bounded. TVD yields convergent subsequences but forces first-order accuracy at smooth extrema, which is why high-order capturing schemes give it up.

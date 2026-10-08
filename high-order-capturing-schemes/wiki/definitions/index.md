# Definitions

Precise domain terms.

* [Essentially non-oscillatory (ENO property)](/definitions/essentially-non-oscillatory.md) — A reconstruction or scheme is essentially non-oscillatory if it produces no Gibbs-like O(1) oscillations at discontinuities, while oscillations at the level of the truncation error are allowed.
* [Modified wavenumber (dispersion and dissipation analysis)](/definitions/modified-wavenumber.md) — The Fourier symbol of a discrete first-derivative operator: applied to e^{ikx} it returns i·ξ̃(ξ)/h; Re ξ̃ against ξ = kh measures dispersion and Im ξ̃ dissipation, the standard tool for judging capturing schemes for turbulence.
* [Monotone numerical flux](/definitions/monotone-flux.md) — A two-argument interface flux that is Lipschitz, nondecreasing in its left and nonincreasing in its right argument, and consistent; the first-order building block that high-order capturing schemes evaluate on reconstructed states.
* [Smoothness indicator](/definitions/smoothness-indicator.md) — The per-stencil measure β_k that drives WENO weights: O(h²) on smooth data, O(1) across a jump; its form (undivided differences vs. L² norms of derivatives) decides the achievable order, including at critical points.

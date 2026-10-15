---
type: Method
title: "Non-intrusive polynomial chaos and Sobol' indices"
description: "Uncertainty propagation that fits a polynomial-chaos surrogate to a set of deterministic CFD runs at collocation points of the uncertain inputs and reads means, variances and variance-based Sobol' sensitivity indices directly from the expansion coefficients; applied to a started and unstarted hypersonic inlet."
status: established
aliases: [NIPC, point-collocation polynomial chaos, polynomial chaos expansion, PCE, Sobol indices, variance-based sensitivity analysis]
tags: [uncertainty-quantification, sensitivity-analysis, polynomial-chaos, surrogate, inlet]
timestamp: 2026-10-14T00:00:00Z
---

# Non-intrusive polynomial chaos and Sobol' indices

Non-intrusive polynomial chaos (NIPC) treats the CFD solver as a black box:
each output is expanded in orthogonal polynomials $\Psi_k$ of the uncertain
inputs $\boldsymbol\xi$, and the expansion coefficients are fitted to
deterministic runs at sampled input values. Statistics and sensitivities then
follow from the coefficients without further runs.
[Liu H. et al. (2018)](/sources/liu-2018-d.md), §3, use the point-collocation
variant of Hosder et al.

## Formulation

As written by [Liu H. et al. (2018)](/sources/liu-2018-d.md), §3, Eqs. 13–19:

* **Expansion.** The output is a sum of coefficient × $\Psi_k(\boldsymbol\xi)$,
  truncated at a total polynomial order; for that order and the number of
  inputs, the number of terms is the binomial coefficient (inputs + order)
  choose order (Eqs. 13–14).
* **Basis.** Multidimensional Legendre polynomials, because the inputs are
  bounded and treated as uniform.
* **Collocation.** Points by optimal Latin hypercube sampling; the number of
  runs is the oversampling ratio (here 2) times the number of terms; the
  coefficients are obtained by least squares (Eq. 15).
* **Moments.** The mean is the zeroth coefficient; the variance is the sum,
  over the other terms, of squared coefficient times the norm
  $\langle\Psi_k^2\rangle$ (Eq. 16).
* **Sobol' indices.** The partial variance of a set of inputs is the same
  sum restricted to the terms that depend on exactly that set; the index is
  its ratio to the total variance (Eqs. 17–19). $S_j$ is the first-order
  index of input $j$.
* **Intervals and correlations.** The 95% interval width is taken as 3.92
  standard deviations, after the paper's ref. [39]; linear correlation
  coefficients between inputs and outputs come from linear regression.

The paper does not state the polynomial order or the number of CFD runs;
the reader's count of about 40 points per flow state in Fig. 20 is
consistent with order 2 in five inputs with oversampling 2 (42 runs), an
inference only. The 3.92-standard-deviation interval assumes Gaussian
outputs, while the inputs are uniform.

## Application to a hypersonic inlet

[Liu H. et al. (2018)](/sources/liu-2018-d.md) propagate five uncertain inputs
through 3D RANS ([SST k–ω](/methods/sst-k-omega-model.md)) of a two-ramp
inlet/isolator at $\mathrm{Ma}_\infty=5.9$, a condition inside the inlet's
hysteresis loop, so that both the started and the unstarted flow exist
([inlet start, unstart and hysteresis](/definitions/inlet-start-and-unstart.md)).

| Input | Baseline | Range |
|---|---|---|
| $\alpha$ | 0.0° | ±0.2° |
| $\mathrm{Ma}_\infty$ | 5.9 | ±1.5% |
| $\mathrm{Re}_\infty$ (per metre) | $5.2\times10^6$ | ±15% |
| $T_\infty$ | 101.7 K | ±10% |
| $T_w$ | 283.0 K | ±10% |

Table 5, bounds based on shock-tunnel conditions of Sriram et al.; the
authors note that the chosen ranges drive the sensitivities.

* **Pressure-coefficient field** (§5.2–5.3, Figs. 14–18). $\mathrm{Ma}_\infty$
  and $\alpha$ dominate the $C_p$ uncertainty in "nearly complementary"
  regions: in the started flow $\alpha$ dominates behind the shocks and
  $\mathrm{Ma}_\infty$ ahead of and under them. $T_w$ is negligible. Near
  the separation bubble all five inputs have comparable indices. Shown.
* **Performance parameters at the isolator station** (Table 6, Fig. 19). The
  95% interval widths of exit Mach number and $\sigma_0$ are about twice as
  large in the started flow as in the unstarted flow (exit Mach number 0.536
  against 0.205; $\sigma_0$ 0.111 against 0.053); the normalized mass
  capture is the exception ($1.06\times10^{-3}$ against
  $1.00\times10^{-3}$). $\mathrm{Ma}_\infty$ dominates the $\sigma_0$
  uncertainty; $\mathrm{Ma}_\infty$ and $\alpha$ dominate the mass-capture
  uncertainty. Shown.
* **Correlations** (Fig. 20). $\mathrm{Ma}_\infty$ correlates positively with
  mass capture (0.8180 started, 0.9005 unstarted) and exit Mach number
  (0.8594, 0.6817) and negatively with $\sigma_0$ (−0.9117, −0.9665).
  The authors conclude that maximum mass flow and maximum $\sigma_0$ cannot
  both be reached by varying $\mathrm{Ma}_\infty$ alone. Shown.
* **Interpretation.** The authors explain the dominance of $\alpha$ behind
  shocks by an oblique-shock derivative ratio, $\mathrm{Ma}_\infty$ times the
  cotangent of the shock angle, much greater than 1 (Eqs. 24–26). The
  printed derivatives carry a spurious constant term, and the argument
  ignores the input ranges: Sobol' indices scale with the squared derivative
  times the input variance, and with ±0.2° against ±0.0885 in Mach number
  the reader's estimate gives comparable contributions (see the Source page).
* **Unresolved.** The sample spreads plotted in Fig. 20 are 5–10 times
  smaller than the Table 6 interval widths (reader's reading).

# Citations

1. [Liu H. et al. (2018)](/sources/liu-2018-d.md) — §3 (Eqs. 13–19), §4.6 (Table 5), §5.2–5.3 (Table 6, Figs. 14–21, Eqs. 24–26).

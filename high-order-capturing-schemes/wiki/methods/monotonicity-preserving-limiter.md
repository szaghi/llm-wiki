---
type: Method
title: "Monotonicity-preserving (MP) limiting"
description: "Suresh–Huynh bound on a high-order interface value: keep it unless it leaves an interval built from the data, an interval enlarged near smooth extrema so that accuracy is kept there; monotone data stay monotone under RK3. Applied to WENO it gives MPWENO."
status: established
aliases: [MP limiter, MP5, MPWENO, monotonicity-preserving bounds]
tags: [limiter, monotonicity, high-order, weno]
timestamp: 2026-10-08T00:00:00Z
---

# Monotonicity-preserving (MP) limiting

[Suresh & Huynh (1997)](/sources/suresh-1997.md) follow the limiting
approach of PPM and Leonard but design the limiter to (a) preserve both
monotonicity and accuracy, (b) suit Runge–Kutta stepping, (c) skip work
when not needed, and (d) be presented geometrically with the
$\operatorname{median}$ function.

## MP5

**Original value.** The quartic through five cell averages gives the
fifth-order left interface value
$$u^{\mathrm{or}}_{i+1/2} = \tfrac{1}{60}\left(2\bar u_{i-2} - 13\bar u_{i-1} + 47\bar u_i + 27\bar u_{i+1} - 3\bar u_{i+2}\right),$$
the same stencil as third-order ENO and fifth-order WENO; five points is
the minimum to tell an extremum from a jump. (Fourth-order low-phase-error
and implicit fifth-order alternatives are also given; larger stencils
give orders $2m-1$.)

**First-order constraint.** If the interface value lies in
$I[\bar u_i, u^{\mathrm{MP}}_{i+1/2}]$ with
$u^{\mathrm{MP}}_{i+1/2} = \bar u_i + \operatorname{minmod}(\bar u_{i+1} - \bar u_i,\ \kappa(\bar u_i - \bar u_{i-1}))$,
monotone data stay monotone after one forward-Euler stage for CFL
$\le 1/(1+\kappa)$, hence after the full RK3 step, whose stages are
positive combinations ([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).
$\kappa = 4$ works well with RK ($\kappa = 2$, the parabolic-scheme value,
may staircase); the bound gives CFL $\le 0.2$, but 0.4 stays
non-oscillatory in practice. Enforced alone, this constraint is first
order at extrema (the interval collapses to $\bar u_i$).

**Accuracy-preserving constraint.** The two intervals are enlarged by
adjoining a median value $u^{\mathrm{MD}}$ (from linear extrapolation
from both sides and a curvature measure) and a large-curvature value
$u^{\mathrm{LC}}$, using the curvature
$\mathcal{D}^{\mathrm{M4}}_{i+1/2} = \operatorname{minmod}(4\delta^2\bar u_i - \delta^2\bar u_{i+1},\ 4\delta^2\bar u_{i+1} - \delta^2\bar u_i,\ \delta^2\bar u_i,\ \delta^2\bar u_{i+1})$,
which switches the enlargement off when neighbouring curvatures differ
by more than a factor 4. The final value is
$\operatorname{median}(u^{\mathrm{or}}_{i+1/2}, u^{\min}, u^{\max})$, with
$[u^{\min}, u^{\max}]$ the intersection of the enlarged intervals. On
monotone data the enlarged interval reduces to the first-order one, so
monotonicity is proved. **Economy:** the limiter is skipped when
$(u^{\mathrm{or}} - \bar u_i)(u^{\mathrm{or}} - u^{\mathrm{MP}}) \le 10^{-10}$
(a round-off tolerance), which holds in most smooth cells. The result
depends continuously on the data.

**Claims and results.** For linear advection the scheme is shown to be
monotonicity preserving and "uniformly high-order accurate". In Euler
tests MP5 resolves shocks and contacts sharply, compares favourably with
WENO5 in accuracy and cost, and needs no steepening
([Suresh & Huynh (1997)](/sources/suresh-1997.md), §4).

## MPWENO

[Balsara & Shu (2000)](/sources/balsara-2000.md) apply the bound to
[WENO](/methods/weno.md) of $r = 3$–$7$, with $\kappa = 2$ (CFL 0.6
safely; about 0.33 for the best advected pulses), a large-curvature
factor of 4 (their $\beta$; 2 works as well), and three curvature choices (minmod, M4, and an
extended M4X over six differences that filters extrema supported on four
zones, useful for MHD). The bounded schemes are robust at normal CFL,
almost spectrally accurate for $r \ge 5$ on smooth problems, and the
results depend little on the heuristic choices.

**Later.** [Fu, Hu & Adams (2016)](/sources/fu-2016.md) list the MP
technique among the robustness devices for very-high-order WENO and state
that "it fails to maintain the formal order of the original WENO scheme"
(citing Gerolymos et al.). [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md)
report that their adaptive-order WENO needs no MP step at all
([adaptive-order WENO](/methods/weno-ao.md)).

## Contradictions

**Does the MP bound degrade accuracy at smooth extrema?**
* [Suresh & Huynh (1997)](/sources/suresh-1997.md): the
  accuracy-preserving constraint "preserves accuracy near extrema"; for
  advection the schemes are "uniformly high-order accurate", and the MP5
  errors on $\sin^4(\pi x)$ are "basically identical" to the unlimited
  quartic's at CFL 0.05 (Table I).
* [Balsara & Shu (2000)](/sources/balsara-2000.md), §IV.a, Table V: on
  $\sin^4(\pi x)$, whose maxima are flat (first three derivatives zero),
  "even the imposition of the least restrictive monotonicity preserving
  bounds strongly degrades the order of accuracy", the error building up
  within $t \le 0.1$; "the monotonicity preserving bounds do not live up
  to the full extent of the claim made in Suresh and Huynh". On
  $\sin(\pi x)$ and on Burgers before shock formation the bounds have no
  effect.
* *Compiler reading:* the two tests differ in time step (CFL 0.05 versus
  Balsara–Shu's $\Delta t \propto h^{(2r-1)/3}$) and in the base
  interface value ($r = 3$ quartic versus $r = 5$ WENO), so the evidence
  is not one-to-one; the claim in dispute is the general one ("does not
  damage the order property"), which Balsara and Shu restrict to
  solutions without very flat extrema.
* **Closed by human fiat (2026-10-08) in favour of Balsara & Shu:** the
  MP bounds do degrade the order of accuracy at flat extrema; Suresh and
  Huynh's "uniformly high-order" claim holds only for solutions without
  such extrema. *Fiat closure — `status: hypothesis` attribution: the
  closure is the human's judgment, not a source superseding a source; a
  later source can reopen it.*

# Citations

1. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §§2–4 and Appendix.
2. [Balsara & Shu (2000)](/sources/balsara-2000.md), §§I, III.d, IV.
3. [Fu, Hu & Adams (2016)](/sources/fu-2016.md), §1.
4. [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §3.1.

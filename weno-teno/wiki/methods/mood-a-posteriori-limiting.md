---
type: Method
title: "MOOD a posteriori limiting"
description: "MOOD-type limiting computes a candidate high-order update first, checks it for admissibility (positivity, NaN), and recomputes only the flagged cells or elements with a robust low-order scheme; the page records the detection and recomputation of Abgrall and Nassajian Mojarrad's kinetic scheme, its use with deferred correction, and its contrast with a priori limiting."
status: established
aliases: [MOOD, multi-dimensional optimal order detection, a posteriori limiting, a posteriori stabilization, a posteriori subcell limiting]
tags: [limiting, positivity, bound-preserving, finite-difference]
timestamp: 2026-10-23T10:00:00Z
---

# MOOD a posteriori limiting

MOOD (multi-dimensional optimal order detection) reverses the order of
a priori non-oscillatory limiting. Instead of deciding before the
step where the high-order scheme must be limited, it computes a
candidate update $\tilde u^{n+1}$ with the unlimited high-order scheme,
tests the candidate cell by cell against admissibility criteria, and
recomputes the update only in the cells that fail, with a lower-order
scheme that is robust there; the high-order result is kept everywhere
else. The two sources of this bundle that apply it use only physical
admissibility (positivity of density and pressure, finite values) as
criterion, and fall back directly to first order.
[Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) present
their version as inspired by two earlier a posteriori methods (their
refs. [14] and [25], §3.2.2).

## Detection and recomputation in a kinetic scheme

Abgrall & Nassajian Mojarrad (2024) (§3.2.2) use MOOD as one of two
stabilizations of their arbitrarily high-order, explicit
[discrete kinetic relaxation scheme](/methods/discrete-kinetic-relaxation-scheme.md),
the other being a flux limiter blending first- and high-order
differences (§3.2.1). From the kinetic state at $t^n$:

1. compute the candidate update with the full-order method (fourth
   order in space and time in their tests);
2. at every grid point recover $(\tilde\rho,\tilde v,\tilde p)$ from the
   projected kinetic state and flag the point if $\tilde\rho\le0$,
   $\tilde p\le0$, or any component is NaN (tested as $x\ne x$);
3. flag a quadrilateral if any of its four vertices is flagged;
4. on flagged quadrilaterals, recompute for every sub-time step the four
   vertex residuals with the first-order scheme.

The recomputation is local because the update of each grid point is
written as the sum of four residuals, one from each quadrilateral sharing
it, and the four residuals of one quadrilateral sum to an approximation
of the flux through its boundary (Eqs. (15)–(16)); this guarantees local
conservation when some quadrilaterals use first-order residuals and their
neighbours high-order ones ([local conservation](/results/local-conservation-flux-form.md)).
No local-extremum detection (as in their ref. [14]) and no
discrimination of smooth extrema (as in their ref. [25]) are used
(§3.2.2). The first-order
scheme "amounts to global Lax–Friedrichs" ([Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)).
Applying the procedure at each cycle of the
[deferred-correction](/methods/deferred-correction.md) iteration would
make the scheme domain-invariant preserving, they state; in the tests it
is applied once per time step, not per cycle.

**Evidence** (§5.2). On a radial Sod problem ($[-1,1]^2$, $200^2$ points,
CFL 1, $T=0.16$) MOOD never activates the first-order scheme, so the
results are fourth order everywhere, with over- and undershoots at the
shock; the flux limiter removes the overshoot and reduces the undershoot
(Figs. 8–9; [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)).
On a radial shock with pressure ratio 1000 ($[-1.5,1.5]^2$, $200^2$,
$T=0.025$) MOOD is required; the flagged first-order elements are few and
localized around the discontinuities (Fig. 10). The authors give no
CPU cost of the recomputation.

## With deferred correction and residual distribution

[Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) use MOOD
(their ref. [12]) as the positivity enforcement of a fourth-order
deferred-correction residual-distribution scheme, DeC(4,4) with cubic
Bernstein elements, on the radial Sod problem with
[entropy correction terms](/methods/entropy-correction-term.md); with it
the computation works (§4.1, Fig. 5). The paper does not describe the
detection criteria or the fallback scheme.

## A posteriori against a priori

[Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) take the subcell
resolution $N_{\mathrm{FV}}=2N+1$ of their DG finite-volume subcell
scheme from the "a posteriori FV sub-cell limiting" of Dumbser et al.,
and call their own switching, decided by a modal-decay indicator before
the step and after each Runge–Kutta stage, "a priori" (§1, §4.3, §7.2;
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md),
[troubled-cell indicator](/definitions/troubled-cell-indicator.md)). In
the a priori route the indicator decides; in MOOD the candidate solution
itself does, so no smoothness threshold has to be tuned for the
admissibility part, at the cost of computing every step twice in the
flagged cells *(compiler check, not in the sources)*.

## Qualifications

- With only positivity and NaN checks, MOOD as used here is a robustness
  fallback, not an oscillation control: Abgrall & Nassajian Mojarrad's
  radial Sod results keep over- and undershoots because no cell is
  flagged (§5.2.2). A [bound-preserving](/properties/bound-preservation.md)
  guarantee requires the first-order fallback itself to be invariant-domain
  preserving and the check to be applied wherever a convex combination is
  formed; the authors state the first part and do not do the second.
- Abgrall & Nassajian Mojarrad print the residual of Eq. (15b) with
  $\Delta y$ multiplying both the $x$- and $y$-direction terms, and
  Eq. (16) with the mesh sizes swapped; the quadrilateral sum that gives
  the boundary flux needs $\Delta y$ on the $x$-part and $\Delta x$ on the
  $y$-part *(compiler check, not in the sources)*.

# Citations

- [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) — §2.1, Eqs. (15)–(16); §3.2.1–3.2.2; §5.2.2–5.2.3, Figs. 8–10.
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — arXiv v4: §4.1, Fig. 5.
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — §1; §4.3; §7.2 (a priori contrast).

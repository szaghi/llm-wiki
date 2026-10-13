---
type: Result
title: "Order barriers and optimal coefficients of SSP time discretizations"
description: "What strong-stability-preserving Runge–Kutta and multistep methods can and cannot reach: SSP coefficient at most 1 for s-stage order-s methods, no four-stage fourth-order method without the downwind operator, multistep step-count barriers, and no implicit SSP method above first order."
status: established
aliases: [SSP barriers, SSP order barrier, optimal SSP methods]
tags: [time-discretization, ssp, impossibility]
timestamp: 2026-10-13T00:00:00Z
---

# Order barriers and optimal coefficients of SSP time discretizations

The setting is the [SSP Runge–Kutta](/methods/ssp-runge-kutta.md)
framework: forward Euler is strongly stable in some norm or convex
functional for $\Delta t \le \Delta t_{\mathrm{FE}}$, and a higher-order
method in Shu–Osher form inherits the property for
$\Delta t \le \mathcal{C}\,\Delta t_{\mathrm{FE}}$, where
$\min a_{ik}/\vert b_{ik}\vert$ (using $\tilde{\mathcal{L}}$ where
$b_{ik} < 0$) is a lower bound on $\mathcal{C}$, equal to it for an
optimal Shu–Osher representation (the coefficient belongs to the method,
not to one representation; see [notation](/notation.md)). "SSP" replaces the earlier name "TVD time
discretization", because nothing in the argument is specific to total
variation ([Gottlieb, Shu & Tadmor (2001)](/sources/gottlieb-2001.md), §1).
The results below are all from Gottlieb, Shu & Tadmor unless stated.

## Runge–Kutta

* **$\mathcal{C} \le 1$ for $s$ stages and order $s$** (Proposition 3.1):
  with nonnegative coefficients, no $s$-stage method of order $s$ beats
  forward Euler's step, already for linear $\mathcal{L}$. Dropping the
  order requirement lifts the bound: an $s$-stage first-order method
  reaches $\mathcal{C} = s$ (suitable for steady states).
* **Linear problems, any order** (Proposition 3.2): for linear
  $\mathcal{L}$ the unique $s$-stage order-$s$ method is SSP with
  $\mathcal{C} = 1$. It is built as $s-1$ forward-Euler stages followed by
  $$u^{(s)} = \sum_{k=0}^{s-2} a_{s,k}\,u^{(k)} + a_{s,s-1}\left(u^{(s-1)} + \Delta t\,\mathcal{L}u^{(s-1)}\right),$$
  with $a_{s,k} = a_{s-1,k-1}/k$, $a_{s,s-1} = 1/s!$,
  $a_{s,0} = 1 - \sum_{k\ge1} a_{s,k}$, all nonnegative. Examples are the
  convex decompositions
  $\sum_{k=0}^{3}\frac{(\Delta t\mathcal{L})^k}{k!} = \frac13 + \frac12(I+\Delta t\mathcal{L}) + \frac16(I+\Delta t\mathcal{L})^3$
  and
  $\sum_{k=0}^{4}\frac{(\Delta t\mathcal{L})^k}{k!} = \frac38 + \frac13(I+\Delta t\mathcal{L}) + \frac14(I+\Delta t\mathcal{L})^2 + \frac1{24}(I+\Delta t\mathcal{L})^4$.
  For nonlinear $\mathcal{L}$ the same schemes stay SSP but lose order $s$.
* **Fourth order needs $\tilde{\mathcal{L}}$** (Proposition 4.2; proved
  in Gottlieb & Shu 1998): every four-stage fourth-order method with
  $\mathcal{C} > 0$ has a negative $b_{ik}$. The best method found has
  $\mathcal{C} = 0.936$ but needs two extra $\tilde{\mathcal{L}}$ evaluations,
  so relative to an ideal four-evaluation method it gives
  $0.936 \times 4/6 = 0.624$ (not $\mathcal C_{\mathrm{eff}}$ in the registry
  sense); its optimality is not claimed.
  This agrees with [Shu (1998)](/sources/shu-1998.md), §4.2.2, and with
  [Shu & Osher (1988)](/sources/shu-1988.md), whose search for fourth
  order could not avoid negative $b_{ik}$.
* **Low storage**: the best three-stage third-order method found in the
  Williamson low-storage form has $\mathcal{C} = 0.32$ (§4.2; two
  registers do not by themselves cap $\mathcal{C}$ there: SSP(4,3) reaches
  $\mathcal{C} = 2$ in two registers, see *Later uses (batch 9)* below;
  corrected at the 2026-10-13 deep lint); no SSP five-stage fourth-order member of the
  Carpenter–Kennedy low-storage class with positive coefficients was
  found, and a low-storage method with a negative $b_{ik}$ cannot use
  $\tilde{\mathcal{L}}$ and so cannot be made SSP.
* **Two-step two-stage hybrids**: third order reaches $\mathcal{C} \approx 0.473$;
  fourth order with nonnegative coefficients is impossible (Proposition 4.3).

**Consequences drawn in later sources.** Authors of one-step schemes
cite the barriers as the reason to leave Runge–Kutta at high order. The
number of stages exceeds the order beyond four (Butcher), and the
fourth-order SSP method is complex enough that RKDG is used up to third
order in practice ([Dumbser & Käser (2007)](/sources/dumbser-2007.md), §3.1.1; [Zanotti et al. (2015)](/sources/zanotti-2015.md), §1; [ADER](/methods/ader.md)).

## Multistep

For $u^{n+1} = \sum_{i=1}^{m}\left(a_i u^{n+1-i} + \Delta t\, b_i\,\mathcal{L}(u^{n+1-i})\right)$:

* no $m$-step method of order $m$ ($m \ge 2$) has all $b_i \ge 0$, and no
  $m$-step SSP method has order $m+1$ (Proposition 5.1);
* optimal $\mathcal{C}$: two-step second order $1/2$; three-step second
  order with $b_i \ge 0$, $1/2$; four-step third order with $b_i \ge 0$,
  $1/3$ (Propositions 5.2–5.4). With one evaluation per step these match
  the efficiency of the optimal two- and three-stage Runge–Kutta
  methods, at higher storage;
* more steps help: four-step second order $2/3$; five- and six-step
  third order $1/2$ and $0.567$; four-step fourth order $\approx 0.159$
  ($0.245$ with six steps); five-step fifth order $\approx 0.085$
  ($0.130$ with six steps);
* a five-step fourth-order method with all $b_i \ge 0$ exists
  ($\mathcal{C} = 0.021$), which disproves the belief that SSP order four
  forces negative coefficients — though the coefficient is too small to
  be useful.

## Implicit methods

Backward Euler is unconditionally TVD (Harten's lemma for implicit
schemes), but no implicit Runge–Kutta (Proposition 6.2) or multistep
(Proposition 6.3) method of the form with only implicit $\mathcal{L}$
terms is SSP above first order. A non-SSP second-order implicit
Runge–Kutta method destroys the monotonicity of a first-order upwind
solution at CFL 1.4 (Fig. 6.1).

## Linear coercive operators

For a linear, coercive, Lipschitz-in-time $\mathcal{L}(t)$, forward
Euler is strongly stable iff $\Delta t \le 2\eta$, and classical RK4 is
then stable under the same condition, with growth $\vert u^n\vert \le e^{3K_{\mathrm{L}}t^n}\vert u^0\vert$
for a Lipschitz constant $K_{\mathrm{L}}$ of $\mathcal{L}(t)$ (Proposition 3.3), improving the Levy–Tadmor bound
$\Delta t \le \eta/31$ to $\Delta t \le 2\eta$.

**Later uses (batch 9).**
* *The low-storage line, read in context.* Gottlieb, Shu and Tadmor's
  $\mathcal C = 0.32$ is the best three-stage method found in the
  Williamson 2N form (their eq. 4.4; four free coefficients), which they compare with the three-stage optimum
  $\mathcal C = 1$ (§4.2, read from the text layer). In the 2N\* Shu–Osher
  form SSP(4,3) reaches $\mathcal C = 2$ in two registers, and the
  optimal SSP($n^2$,3) reach $n^2 - n$ in 2N ([Higueras & Roldán (2019)](/sources/higueras-2019.md), §§2.2, 3;
  [low-storage Runge–Kutta](/methods/low-storage-runge-kutta.md)). The bullet above is therefore a statement about the
  three-stage Williamson form, not about two registers; five-stage
  Williamson methods reach 1.40 (Higueras & Roldán, Table 1).
* *More optimal Runge–Kutta coefficients* ([Higueras & Roldán (2019)](/sources/higueras-2019.md), §§2.2, 4.1,
  citing Kraaijevanger and Ketcheson): SSP($s$,1) $\mathcal C = s$
  (agrees with the bullet above), SSP($s$,2) $s - 1$, SSP($n^2$,3)
  $n^2 - n$, and SSP(5,3) the real root of $x^3 - 5x^2 + 10x - 10$,
  $\approx 2.6506$.
* *A storage barrier with an empirical premise.* No optimal SSP(5,3)
  method has the 2N\* form (Proposition 1). The proof assumes a
  coefficient structure that RK-Opt runs exhibit but that is not proved,
  and the abstract states the result more broadly than the proposition
  ([Higueras & Roldán (2019)](/sources/higueras-2019.md), §4).
* *The multistep values follow from one bound.* For $m \ge p_{\mathrm t}$,
  $\mathcal C \le (m - p_{\mathrm t})/(m - 1)$ (Lenferink), with variable
  steps $\mathcal C \le (\Omega_{\Delta t} - p_{\mathrm t})/(\Omega_{\Delta t} - 1)$,
  sharp at second order and at third order for four and five steps
  ([Hadjimichael et al. (2016)](/sources/hadjimichael-2016.md), Theorem 2, Proposition 1). It reproduces $1/2$, $2/3$,
  $1/3$ and $1/2$ above. The two-step second-order value $1/2$ is not
  covered: that method has a negative coefficient ($b_2 = -2/5$) and
  needs $\tilde{\mathcal L}$ ([SSP linear multistep methods](/methods/ssp-linear-multistep.md)).
* *A positivity barrier, second-hand.* No Runge–Kutta or general linear
  method that is unconditionally positive for all positive ODEs exceeds
  first order (Bolley and Crouzeix, as cited by [Nüßlein, Ranocha & Ketcheson (2021)](/sources/nusslein-2021.md), §1; not
  in the corpus). It is the positivity counterpart of the implicit-method
  barrier above.

**Later uses (batch 14).**

* *"Harten's lemma" is explicit in its source.* Lemma 2.2 of
  [Harten (1983)](/sources/harten-1983.md) (§2, eqs. 2.9–2.12) gives
  sufficient conditions for TVD on an explicit scheme in incremental
  form, $u^{n+1}$ computed from $u^n$ alone: nonnegative incremental
  coefficients whose sum at each interface is at most 1. The paper states
  no implicit version. The statement under *Implicit methods* above, that
  backward Euler is unconditionally TVD by "Harten's lemma for implicit
  schemes", therefore does not rest on the 1983 paper; which work it
  rests on is not recorded in this bundle
  ([TVD](/properties/total-variation-diminishing.md)).

**Later uses (batch 16).**
* *The first-order bullet, at its origin.* The earliest form of "an
  $s$-stage first-order method reaches $\mathcal C = s$" in the corpus is
  Shu's steady-state scheme: stage coefficients $i/(s(s-i+1))$, one cycle
  equal to the $s$-th power of a forward-Euler-type operator of step
  $\Delta t/s$, TVD under CFL number $s$
  ([Shu (1988b)](/sources/shu-1988-b.md), Proposition 2.1, eqs. 2.4–2.10).
  Its nonlinear coefficients are frozen at the start of each cycle, so it
  is a linear iteration, not a Runge–Kutta method applied to a nonlinear
  $\mathcal L$. The bullet above is Gottlieb, Shu and Tadmor's.
* *The multistep values come from Shu (1988b), Table 1.* Two-step second
  order $0.5$, three-step $0.5$, four-step second order $0.67$, four-step
  third order $0.33$, five- and six-step third order $0.5$ and $0.57$,
  six-step fourth order $0.245$ and six-step fifth order $0.1298$ are all
  rows of that table ([SSP linear multistep methods](/methods/ssp-linear-multistep.md)).
  For four-step fourth order and five-step fifth order Shu's methods have
  $0.15$ and $0.077$, below the $0.159$ and $0.085$ above; Shu calls his
  table "by no means exhaustive, nor … the optimal of the corresponding
  order". A four-step second-order method with a negative coefficient
  reaches $0.75$, above the $2/3$ quoted here, at the cost of
  $\tilde{\mathcal L}$, whose avoidance "will reduce the work of each
  timestep by one half" (Remark 3.1).
* *The barrier, seen in the table.* Every $m$-step method of order $m$
  in Table 1 has a negative coefficient, consistent with Proposition 5.1
  above; Shu states no such theorem. He never asserts the belief that
  fourth order forces negative coefficients, which the five-step bullet
  above disproves; his table merely contains no fourth-order method with
  all $b_i \ge 0$.
* *Existence at every order* (Corollary 3.1). For any TVD space
  discretization of a given order there are $m$-step TVD multistep
  methods of the same order, $p_{\mathrm t} = m$, with positive CFL number; the coefficients solve a nonsingular
  (Vandermonde-type) linear system, and may be negative, so
  $\tilde{\mathcal L}$ is then needed. The four-step third-order row of
  Table 1 is misprinted (see the multistep page).
* *A spatial barrier, quoted.* No local-stencil scheme of order above one
  was proven TVD in two or more dimensions, and Goodman and LeVeque proved
  that in 2D a TVD scheme, for the total variation summed over both
  directions, is at most first order; Shu notes that this does not exclude
  high-order TVB schemes and that this 2D total variation "may not be the
  best choice" (p. 1082; [TVD](/properties/total-variation-diminishing.md)).

# Citations

1. [Gottlieb, Shu & Tadmor (2001)](/sources/gottlieb-2001.md), §§2–6 (Propositions 3.1–6.3, Table 3.1).
2. [Shu (1998)](/sources/shu-1998.md), §4.2.
3. [Shu & Osher (1988)](/sources/shu-1988.md), §II.
4. [Dumbser & Käser (2007)](/sources/dumbser-2007.md), §3.1.1.
5. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §1.
6. [Higueras & Roldán (2019)](/sources/higueras-2019.md), §§2–4 (arXiv v1).
7. [Hadjimichael et al. (2016)](/sources/hadjimichael-2016.md), §§3.1–3.2 (arXiv v2).
8. [Nüßlein, Ranocha & Ketcheson (2021)](/sources/nusslein-2021.md), §1 (arXiv v2).
9. [Harten (1983)](/sources/harten-1983.md), §2 (Lemma 2.2).
10. [Shu (1988b)](/sources/shu-1988-b.md), §§2–3, Proposition 2.1, Corollary 3.1, Remark 3.1, Table 1, p. 1082.

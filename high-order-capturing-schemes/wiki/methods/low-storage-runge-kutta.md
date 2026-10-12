---
type: Method
title: "Low-storage Runge–Kutta methods"
description: "Runge–Kutta methods arranged to run in two or three solution-sized registers instead of s+1: the Williamson 2N form, the 2N* form that keeps u^n, and the 3S*-type forms with an error-estimate register; which SSP coefficients survive the storage constraint, and the optimized low-storage pairs for compressible CFD."
status: established
aliases: [2N-storage Runge-Kutta, 2N*, 3S*, low-storage RK, Williamson form]
tags: [time-discretization, runge-kutta, low-storage, ssp]
timestamp: 2026-10-12T00:00:00Z
---

# Low-storage Runge–Kutta methods

A naive explicit $s$-stage [Runge–Kutta method](/methods/explicit-runge-kutta.md)
keeps $s + 1$ arrays of the size of the solution ("registers"). For
large 3D computations storage is often the binding constraint, so
methods are sought that need a fixed small number of registers
regardless of $s$ ([Gottlieb, Shu & Tadmor (2001)](/sources/gottlieb-2001.md), §4.2;
[Higueras & Roldán (2019)](/sources/higueras-2019.md), §§1, 3).

## Storage classes

* **2N (Williamson).** Only the solution and one increment register are
  kept: each stage scales the increment by a constant, adds
  $\Delta t\,\mathcal L$ of the current stage, and adds a multiple of the
  increment to the solution
  ([Gottlieb, Shu & Tadmor (2001)](/sources/gottlieb-2001.md), eq. 4.4). Van der Houwen's
  construction is the other classical 2N route
  ([Higueras & Roldán (2019)](/sources/higueras-2019.md), §3).
* **2N\*.** A 2N method that also keeps $u^n$ for the whole step, which a
  variable-step code needs to reject a step without a third register
  (Def. 3, after Gottlieb, Ketcheson & Shu 2011). In Shu–Osher form the
  sparse pattern is: $a_{ik}$ nonzero only on the first subdiagonal and in
  the column of $u^n$, $b_{ik}$ only on the first subdiagonal (eq. 24,
  Algorithm 1).
* **3S\*, 3S\*₊, 2R.** Ketcheson's counting, used for pairs: 3S\* is three
  registers including an error estimate, valid when overwriting a
  register with itself plus $\mathcal L$ of itself costs one register
  plus lower-order memory; the subscript ₊ adds one register for the embedded solution.
  Three registers is the minimum when an error estimate and step
  rejection are required ([Ranocha et al. (2022)](/sources/ranocha-2022.md), §2.1, Algorithms 1–2).

## Which SSP coefficients survive

* **Williamson form, three stages, third order:** the best SSP method
  found in that class (a one-parameter family; four free coefficients)
  has $\mathcal C = 0.32$, against $\mathcal C = 1$ for the optimal
  three-stage method in the usual form; no SSP member of the Carpenter–Kennedy five-stage
  fourth-order 2N class with positive coefficients was found, and a
  low-storage method with a negative $b_{ik}$ cannot use
  $\tilde{\mathcal L}$ without losing its storage property
  ([Gottlieb, Shu & Tadmor (2001)](/sources/gottlieb-2001.md), §4.2;
  [SSP order barriers](/results/ssp-order-barriers.md)).
* **2N\* in Shu–Osher form keeps the optimal methods** SSP($s$,2)
  ($\mathcal C = s-1$), SSP(3,3) ($\mathcal C = 1$) and SSP(4,3)
  ($\mathcal C = 2$). The optimal SSP($n^2$,3), $\mathcal C = n^2 - n$
  (Ketcheson 2008), are 2N but not 2N\*
  ([Higueras & Roldán (2019)](/sources/higueras-2019.md), §§2.2, 3).
  So the 0.32 figure is a property of the three-stage Williamson form,
  not of two registers; five-stage Williamson methods reach
  $\mathcal C = 1.40$ (Higueras & Roldán, Table 1).
* **Five stages, third order.** The optimal SSP(5,3) has
  $\mathcal C \approx 2.6506$, the real root of $x^3 - 5x^2 + 10x - 10$.
  Under a structure that RK-Opt runs show and the paper then assumes, no
  optimal SSP(5,3) method has the 2N\* form (24) (Proposition 1); some
  run in 3N (Proposition 2). Optimizing inside 2N\* gives
  SSP53_2N\*₁ with $\mathcal C = 2.18075$ and SSP53_2N\*₂ with
  $\mathcal C = 2.14874$, the latter with the smaller error constant and
  the longer real stability interval (to $-7.26$) (§5, eqs. 49–53, 60–61).
  Per evaluation that is $\mathcal C_{\mathrm{eff}} \approx 0.436$ and
  $0.430$, below SSP(4,3)'s $0.5$ (compiler's arithmetic; the paper
  reports none).
* **Observed coefficients.** On one Buckley–Leverett test with a Koren
  limiter, the new methods stay TVD up to $\mathcal C_{\mathrm{obs}} = 2.29$
  and $2.45$; SSP(4,3) is sharp at $2.04$; the five-stage Williamson and
  van der Houwen methods ($\mathcal C$ between 1 and 1.48) reach 1.96–2.20
  (§6.1, Table 1). One grid, one problem, one limiter.
* **Ten stages, fourth order.** Ketcheson's SSP-RK(10,4) is low-storage
  ([Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §3;
  [SSP page](/methods/ssp-runge-kutta.md)).
* **Not SSP:** the Spalart–Moser–Rogers low-storage RK3 of a production
  WENO code ([Bernardini et al. (2021)](/sources/bernardini-2021.md), §2.2).

## Low-storage embedded pairs for CFD

[Ranocha et al. (2022)](/sources/ranocha-2022.md) (§6, Tables 6, 11, B1–B6)
add optimized embedded methods to the 3S\*₊ main methods of Parsani,
Ketcheson and Deconinck (2013), giving RK3(2)5, RK4(3)9 and RK5(4)10, each
also as a FSAL variant, with a PID controller tuned for each
([step-size control](/methods/runge-kutta-step-size-control.md)). The
embedded methods are designed so that their stability region contains
the main method's. None is claimed SSP. With stability-limited steps the
third-order pairs are up to 18 % cheaper than BS3(2)3F, in proportion to
their real stability intervals (§6.2). The 2R pairs of Kennedy,
Carpenter and Lewis lose to BS3(2)3F almost everywhere; the paper blames
the stricter storage constraints, the missing FSAL, and an embedded
stability region smaller than the main one in places (§5.5.4).
* **SSP3(2)4 in 3S\*₊.** Kraaijevanger's four-stage third-order SSP
  method with the Conde–Fekete–Shadid embedded method runs in three
  registers (the old solution, the current stage and the embedded solution): three forward-Euler half steps, the
  combination $\tfrac23 u^n + \tfrac13 u$, and a fourth half step
  (App. A, eqs. A1–A2). It was the most efficient method on several
  stability-limited flows (§§5.5.2, 7).

**Relaxation needs no extra storage.** The direction and the entropy
estimate of a [relaxation step](/methods/relaxation-runge-kutta.md) are
accumulated during the stages, so existing low-storage implementations
run unchanged ([Ranocha et al. (2020)](/sources/ranocha-2020.md), p. 4).

# Citations

1. [Gottlieb, Shu & Tadmor (2001)](/sources/gottlieb-2001.md), §4.2 (eq. 4.4; the coefficient system of the Williamson-form method is illegible in the text layer and not reproduced).
2. [Higueras & Roldán (2019)](/sources/higueras-2019.md), §§2–6, Table 1 (arXiv v1).
3. [Ranocha et al. (2022)](/sources/ranocha-2022.md), §§2.1, 5.5, 6, App. A.
4. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §3.
5. [Bernardini et al. (2021)](/sources/bernardini-2021.md), §2.2.
6. [Ranocha et al. (2020)](/sources/ranocha-2020.md), §2.

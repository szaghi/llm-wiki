---
type: Property
title: "Total variation diminishing (TVD) and bounded (TVB)"
description: "TVD: the discrete total variation does not grow; TVB: it stays uniformly bounded. TVD yields convergent subsequences but forces first-order accuracy at smooth extrema, which is why high-order capturing schemes give it up."
status: established
aliases: [TVD, TVB, total variation diminishing, total variation bounded]
tags: [stability, tvd]
timestamp: 2026-10-13T00:00:00Z
---

# Total variation diminishing (TVD) and bounded (TVB)

With $TV(u) = \sum_i \vert u_{i+1} - u_i\vert$, a scheme is **TVD** if
$TV(u^{n+1}) \le TV(u^n)$, and **TVB** if $TV(u^n) \le B$ for a bound $B$
depending only on $TV(u^0)$, for all $n$ and $\Delta t$ with $t^n$ up
to a fixed final time. Uniform boundedness of the total variation gives a
subsequence converging in $L^1_{\mathrm{loc}}$ to a weak solution
(with a conservative scheme, by the Lax–Wendroff theorem); an entropy
condition then identifies the limit
([Harten et al. (1987)](/sources/harten-1987.md), Remark 1.3;
[Shu & Osher (1988)](/sources/shu-1988.md), §I).

**First order at extrema.** TVD schemes, of any form, are necessarily
only first-order accurate at local extrema
([Harten et al. (1987)](/sources/harten-1987.md), §2;
[Shu & Osher (1988)](/sources/shu-1988.md), §I: even the TVD schemes of
very high order — up to 15th, on a 17-point stencil — degenerate at
extrema). The limiter that enforces TVD makes the leading error
coefficient discontinuous there. [Suresh & Huynh (1997)](/sources/suresh-1997.md)
add a geometric reason: over a three-point stencil an extremum and a
discontinuity look the same, so a TVD limiter cannot tell them apart;
five points are the minimum to distinguish them. In the $L^1$ norm the
loss shows as second order: Colella and Woodward's PPM uses third-order
interpolants but, being TVD, is "restricted to being second-order
accurate in the $L^1$ norm even for smooth problems with extrema", and
so is Chakravarthy and Osher's class of TVD schemes of increasing order
for monotone data; the TVD limiters are "highly non-linear", which makes
their effect hard to remove after the fact
([Balsara & Shu (2000)](/sources/balsara-2000.md), §I).

**Examples.** Godunov's scheme and the MUSCL scheme are TVD in the
scalar case ([Harten et al. (1987)](/sources/harten-1987.md)). Second
order ENO is TVD ([Shu (1998)](/sources/shu-1998.md), §2.3.4). The
fixed wide stencils of very high order TVD/TVB schemes smear
discontinuities and pollute a large region near them
([Shu & Osher (1988)](/sources/shu-1988.md)).

**What replaced it.** High-order schemes in this bundle weaken the
requirement:
* [essentially non-oscillatory](/definitions/essentially-non-oscillatory.md)
  reconstruction, which admits oscillations at the truncation-error level;
* TVB modifications that recover high order at extrema (Shu);
* [monotonicity-preserving limiting](/methods/monotonicity-preserving-limiter.md),
  which keeps monotone data monotone but enlarges the admissible interval
  near smooth extrema.

TVD survives as a property of the *time* discretization: the
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) methods preserve
whatever forward-Euler stability (TVD, TVB, maximum norm, entropy
inequality) the spatial operator has
([Shu & Osher (1988)](/sources/shu-1988.md);
[Shu (1998)](/sources/shu-1998.md), §4.2).

**Later uses (batch 7).**
* *Applied field by field to MHD.* Harten's (1983) second-order TVD scheme
  on the seven characteristic fields of ideal MHD, with a Roe-type
  linearization and steepening of the Alfvén families; in 1D the
  divergence-free reconstruction of face fields reduces to the same MUSCL
  profile. No TVD property is proved for the system
  ([Ryu & Jones (1995)](/sources/ryu-1995.md), §2.3; [Balsara (2001)](/sources/balsara-2001.md), eq. 3.40).

**Later uses (batch 9).** *Observed SSP coefficient.* The largest step
at which a scheme stays TVD on a test, divided by the forward-Euler TVD
step on the same test, $\mathcal C_{\mathrm{obs}}$. On Buckley–Leverett
with a Koren limiter, SSP(4,3) is sharp ($2.04$ against $\mathcal C = 2$);
every other third-order method tested exceeds its $\mathcal C$, the two
new 2N\* methods by 5 % and 14 % ([Higueras & Roldán (2019)](/sources/higueras-2019.md), §6.1, Table 1;
[low-storage Runge–Kutta](/methods/low-storage-runge-kutta.md)).

**Later uses (batch 14).**

**The primary source.** [Harten (1983)](/sources/harten-1983.md) defines
the property, under the name TVNI ("total variation nonincreasing"), as
$TV(u^{n+1}) \le TV(u^n)$ for *all* data of bounded total variation
(eq. 2.4), motivated by the exact scalar solution, which creates no new
extrema (eq. 2.2). The definition above agrees with it.

**Where TVD sits** (§2, Theorem 2.1). Monotone ⇒ TVD ⇒ monotonicity
preserving. A linear scheme is monotonicity preserving iff its
coefficients are nonnegative (citing Godunov), so a linear TVD scheme is
monotone and first order; a second-order TVD scheme must be nonlinear.
The root of this is Godunov's barrier for linear monotone schemes
([Godunov's order barrier](/results/godunov-order-barrier.md);
[Godunov (1959)](/sources/godunov-1959.md), Ch. I §3). It is a different
result from the first-order-at-extrema statement above, which concerns
nonlinear TVD schemes.

**Harten's lemma** (Lemma 2.2, eqs. 2.9–2.12). Write an explicit scheme
in incremental form: $u^{n+1}_i$ is $u^n_i$ plus a coefficient times
$\Delta^1 u^n_i$ minus a coefficient times $\Delta^1 u^n_{i-1}$, each
coefficient a function of the four values around its interface. If both
coefficients are nonnegative at every interface and their sum at each
interface is at most 1, the scheme is TVD: each new difference is then a
combination of three old differences with nonnegative coefficients. Any
three-point conservative scheme with a differentiable numerical flux has
this form, by the mean value theorem. The lemma is stated for explicit
schemes only (see [SSP order barriers](/results/ssp-order-barriers.md)).

**The first second-order TVD construction** (§3). Start from the
three-point flux
$\hat f_{i+1/2} = \tfrac12\left[f(u_i) + f(u_{i+1})\right] - \tfrac12\Theta_{i+1/2}\Delta^1 u_i$,
with $\Theta_{i+1/2}$ a function of the local Courant number
$\hat a_{i+1/2}\Delta t/h$. It is TVD if
$\vert\hat a_{i+1/2}\vert \le \Theta_{i+1/2} \le h/\Delta t$ for local
Courant numbers up to a bound at most 1, and the Courant number of the
Roe speeds stays below that bound (Lemma 3.1); then it is only first
order. Applying the same scheme to $f$ plus a limited correction, at
node $i$ the $\operatorname{minmod}$ of the two neighbouring interface
values of
$\tfrac12\left[\Theta_{i+1/2}\Delta t/h - (\hat a_{i+1/2}\Delta t/h)^2\right]\Delta^1 u_i$
(up to the factor $h/\Delta t$, the antidiffusive flux that turns the
first-order flux into Lax–Wendroff's), gives a five-point scheme that is
second order (Lemmas 3.2–3.3) and TVD under the *same* CFL condition
(Lemma 3.4). It "may degenerate locally" where the sign of the
antidiffusive term jumps, at extrema (Remark 2): agreement in mechanism
with the paragraph on extrema above, without the general theorem.
A simplified version uses a three-argument $\operatorname{minmod}$
(Remark 4).

**Systems and convergence.** The scheme is applied field by field with
any symmetric average state; for constant $A$ it is TVD in the functional
$\sum_i\sum_p\vert\ell^{(p)}\Delta^1 u_i\vert$, motivated by Glimm's
(Lemma 4.2), and convergent and second order (Corollary 4.3). For
nonlinear scalar laws convergence to the entropy solution needs an
entropy consistency the paper does not prove (Remark 1), and for
nonlinear systems Harten "cannot prove convergence" (Remark 3). This
qualifies the convergence paragraph above: the TVD argument identifies
the limit only where an entropy condition is available. It agrees with
the batch-7 note that no TVD property is proved for the MHD system.
Harten allows any average and finds that the arithmetic mean "will do
just as well" as Roe's in many applications (§6), the choice Ryu & Jones
make; his entropy-fix parameter, 0.1 on genuinely nonlinear and 0 on
linearly degenerate fields (§5), matches their fast, slow and entropy
values ([Ryu & Jones (1995)](/sources/ryu-1995.md), Key claims 7–8).

**On the examples.** Harten (1983) cites van Leer's (1974) second-order
scheme only as monotonicity preserving, "at least in the constant coefficient
case" (§2, p. 361); this does not conflict with the scalar TVD statement
of Harten et al. (1987) above.

**Later uses (batch 14).** *MUSCL at the source* ([van Leer (1979)](/sources/vanleer-1979.md), §§3.3, 4;
[MUSCL](/methods/muscl.md)). Van Leer makes no TVD claim. For the
gas-dynamics system his monotonicity algorithms do not guarantee
monotonicity: "the nonlinearity of slab interactions makes it impossible
to fully guarantee monotonicity, especially for the largest allowed time
steps" (p. 118), and in the remap "positivity is guaranteed only for the
zone averages" (p. 119). This qualifies by scope, and does not
contradict, the scalar statement under **Examples**. He is the earliest
source of this bundle for the loss at extrema: his limiters "will clip
real peaks to the same degree as a first-order method would do"
(p. 119), and the coarse-grid Mach stem of his step test is "an artifact
due to the monotonicity algorithms" (p. 123). The limiter factors 2 may
be lowered, but not below 1 plus a term of the order of the data jump,
"lest the scheme lose its second-order accuracy" (p. 118). His remedy is
a narrow-base limiter built on saved interface values, which limits less
near peaks (eq. 104). *Compiler reading:* it anticipates the enlarged
admissible interval of [monotonicity-preserving limiting](/methods/monotonicity-preserving-limiter.md).

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), §§1–2, Remark 1.3.
2. [Shu & Osher (1988)](/sources/shu-1988.md), §§I–II.
3. [Shu (1998)](/sources/shu-1998.md), §§1, 2.3.4, 4.2.
4. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §2.
5. [Balsara & Shu (2000)](/sources/balsara-2000.md), §I.
6. [Ryu & Jones (1995)](/sources/ryu-1995.md), §2.3.
7. [Balsara (2001)](/sources/balsara-2001.md), §III.
8. [Higueras & Roldán (2019)](/sources/higueras-2019.md), §6.1 (arXiv v1).
9. [Godunov (1959)](/sources/godunov-1959.md), Ch. I §§2–3 (reader's translation of the Russian original).
10. [Harten (1983)](/sources/harten-1983.md), §§2–6 (Theorem 2.1, Lemmas 2.2, 3.1–3.4, 4.2, Corollary 4.3).
11. [van Leer (1979)](/sources/vanleer-1979.md), §§3.3, 4.

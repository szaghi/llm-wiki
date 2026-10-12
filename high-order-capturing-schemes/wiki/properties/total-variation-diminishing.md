---
type: Property
title: "Total variation diminishing (TVD) and bounded (TVB)"
description: "TVD: the discrete total variation does not grow; TVB: it stays uniformly bounded. TVD yields convergent subsequences but forces first-order accuracy at smooth extrema, which is why high-order capturing schemes give it up."
status: established
aliases: [TVD, TVB, total variation diminishing, total variation bounded]
tags: [stability, tvd]
timestamp: 2026-10-12T00:00:00Z
---

# Total variation diminishing (TVD) and bounded (TVB)

With $TV(u) = \sum_i \vert u_{i+1} - u_i\vert$, a scheme is **TVD** if
$TV(u^{n+1}) \le TV(u^n)$, and **TVB** if $TV(u^n) \le B$ for a bound $B$
depending only on $TV(u^0)$, for all $n$ and $\Delta t$ with
$n\Delta t \le T$. Uniform boundedness of the total variation gives a
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
five points are the minimum to distinguish them.

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

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), §§1–2, Remark 1.3.
2. [Shu & Osher (1988)](/sources/shu-1988.md), §§I–II.
3. [Shu (1998)](/sources/shu-1998.md), §§1, 2.3.4, 4.2.
4. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §2.
5. [Balsara & Shu (2000)](/sources/balsara-2000.md), §I.
6. [Ryu & Jones (1995)](/sources/ryu-1995.md), §2.3.
7. [Balsara (2001)](/sources/balsara-2001.md), §III.
8. [Higueras & Roldán (2019)](/sources/higueras-2019.md), §6.1 (arXiv v1).

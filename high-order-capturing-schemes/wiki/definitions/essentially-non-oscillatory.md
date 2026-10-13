---
type: Definition
title: "Essentially non-oscillatory (ENO property)"
description: "A reconstruction or scheme is essentially non-oscillatory if it produces no Gibbs-like O(1) oscillations at discontinuities, while oscillations at the level of the truncation error are allowed."
status: established
aliases: [ENO property, essentially non-oscillatory]
tags: [eno, stability]
timestamp: 2026-10-13T00:00:00Z
---

# Essentially non-oscillatory (ENO property)

**Harten et al.** ([Harten et al. (1987)](/sources/harten-1987.md)):
a piecewise-polynomial reconstruction $\mathcal P$ from the cell
averages of a piecewise smooth $w$, of degree $K$ in each cell and so of
order $K + 1$, is essentially non-oscillatory when
$$TV\left(\mathcal P\right) \le TV(w) + O(h^{K+1})$$
(their eq. 1.9c, in registry symbols) — it does not generate $O(1)$
oscillations proportional to the jump at a discontinuity, though it may
generate spurious oscillations of the size of the truncation error,
$O(h^{K+1})$, in smooth regions. In the scalar case the abstract ENO scheme inherits this
property because the exact evolution and the cell averaging are both
monotone.

The notion sits in a hierarchy that each step weakens:
* **TVD**: $TV(u^{n+1}) \le TV(u^n)$ — forces first order at extrema
  ([total variation diminishing](/properties/total-variation-diminishing.md));
* **non-oscillatory**: the number of local extrema does not increase —
  limits the order to 2 (the second paper of the series, cited in
  [Harten et al. (1987)](/sources/harten-1987.md));
* **essentially non-oscillatory**: the condition above, which admits
  arbitrary order.

**Shu's reading** ([Shu (1998)](/sources/shu-1998.md)): an
interpolation is essentially non-oscillatory when "the magnitude of the
oscillations decays as" $h$ to the power of the order of accuracy, for
piecewise smooth functions; and the ENO reconstruction is TVB
([ENO](/methods/eno-reconstruction.md)).

**Weight form** ([Liu, Osher & Chan (1994)](/sources/liu-1994.md),
Definition 1): a convex combination $R_i = \sum_k \omega_k p_k$ has the
ENO property when $\omega_k = O(1)$ for candidate stencils in smooth
regions and $\omega_k \le O(h^r)$ for stencils containing a
discontinuity. [Jiang & Shu (1996)](/sources/jiang-1996.md) note that
with several smooth candidates each gets an $O(1)$ weight, so WENO does
not reproduce the "ENO digital weights" exactly; the WENO
weight of a stencil crossing a discontinuity is $O(h^{2q})$ for power
$q$ ([WENO](/methods/weno.md)).

The property is a design target, not a theorem: no proof exists that
ENO or WENO schemes of order above two are TVB as time evolves
([Shu & Osher (1988)](/sources/shu-1988.md), §III;
[Shu (1998)](/sources/shu-1998.md), §2.3.4).

**Later uses (batch 18).** *The nonoscillatory rung at its source*
([Harten & Osher (1987)](/sources/harten-1987-b.md), §§1–2), now ingested.
* *Where the notion is introduced* (a correction of the attribution in the
  hierarchy above). The requirement that the solution operator "diminish
  the number of local extrema in the numerical solution" ("diminishing"
  meaning nonincreasing) is defined in Harten & Osher's paper, which calls
  itself "the first" of the series (§1, p. 280), not in the second paper.
  Every essentially 3-point TVD scheme that is an average of monotone
  Riemann solvers has the property; unlike TVD, a nonoscillatory scheme
  may "occasionally accentuate a local extremum", and it is monotonicity
  preserving.
* *"Limits the order to 2" is not stated there.* Harten & Osher prove no
  order limit. They present their second-order scheme as the first step of
  a programme: "we show how to construct nonoscillatory schemes that are
  uniformly high-order accurate … In this first paper we describe a
  second-order accurate scheme of this type" (p. 280). The order-2 limit
  of the hierarchy is the later statement of
  [Harten et al. (1987)](/sources/harten-1987.md) (§2), to which it stays
  attributed.
* *The same argument, first for extrema* (§2, p. 281). Cell averaging is
  nonoscillatory and exact evolution is TVD, so a reconstruct–evolve–average
  scheme is nonoscillatory if the reconstruction has no more local extrema
  than the data: "the design of nonoscillatory high-order accurate schemes
  essentially boils down to a problem on the level of approximation of
  functions". The ENO III argument above repeats it for the total
  variation.
* *What is given up* (§§2, 5). The paper's second-order scheme keeps
  second order at extrema but loses TVD: its TV can grow, by an amount
  bounded per step (5.5b), and uniform TV boundedness is not proved, for
  "lack of theoretical tools to analyze pointwise regularity" (p. 291)
  ([ENO](/methods/eno-reconstruction.md)).

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), §§1–2.
2. [Shu & Osher (1988)](/sources/shu-1988.md), §§I, III.
3. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), §3.3, Definition 1.
4. [Jiang & Shu (1996)](/sources/jiang-1996.md), §2.
5. [Shu (1998)](/sources/shu-1998.md), §§1, 2.2.1, 2.3.4.
6. [Harten & Osher (1987)](/sources/harten-1987-b.md), §§1–2, 5, pp. 280–291.

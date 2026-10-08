---
type: Definition
title: "Essentially non-oscillatory (ENO property)"
description: "A reconstruction or scheme is essentially non-oscillatory if it produces no Gibbs-like O(1) oscillations at discontinuities, while oscillations at the level of the truncation error are allowed."
status: established
aliases: [ENO property, essentially non-oscillatory]
tags: [eno, definition, stability]
timestamp: 2026-10-08T00:00:00Z
---

# Essentially non-oscillatory (ENO property)

**Harten et al.** ([Harten et al. (1987)](/sources/harten-1987.md)):
a reconstruction $R(x; \bar w)$ of a piecewise smooth $w$ is
essentially non-oscillatory when
$$TV\left(R(\cdot; \bar w)\right) \le TV(w) + O(h^r)$$
(their eq. 1.9c, with $r$ the order) — it does not generate $O(1)$ oscillations
proportional to the jump at a discontinuity, though it may generate
spurious oscillations of the size of the truncation error, $O(h^r)$, in
smooth regions. In the scalar case the abstract ENO scheme inherits this
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
oscillations decays as $O(h^k)$ where $k$ is the order of accuracy", for
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

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), §§1–2.
2. [Shu & Osher (1988)](/sources/shu-1988.md), §§I, III.
3. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), §3.3, Definition 1.
4. [Jiang & Shu (1996)](/sources/jiang-1996.md), §2.
5. [Shu (1998)](/sources/shu-1998.md), §§1, 2.2.1, 2.3.4.

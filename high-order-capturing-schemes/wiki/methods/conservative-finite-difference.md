---
type: Method
title: "Conservative finite-difference (flux) formulation"
description: "Shu–Osher point-value formulation: the numerical flux approximates a function whose sliding average is the physical flux, so ENO/WENO reconstruction of flux point values gives high-order conservative differences, dimension by dimension, on uniform or smoothly mapped grids."
status: established
aliases: [flux ENO, finite-difference ENO/WENO, Shu-Osher formulation]
tags: [finite-difference, flux-splitting, eno, weno]
timestamp: 2026-10-08T00:00:00Z
---

# Conservative finite-difference (flux) formulation

The unknowns are point values $u_i$, and the scheme is conservative,
$\frac{d}{dt}u_i = -\frac{1}{h}\left(\hat f_{i+1/2} - \hat f_{i-1/2}\right)$,
so the Lax–Wendroff theorem applies.

**The lemma** ([Shu & Osher (1989)](/sources/shu-1989.md), Lemma 2.1).
If $\mathcal{H}$ is defined implicitly by
$f(u(x)) = \frac{1}{h}\int_{x-h/2}^{x+h/2}\mathcal{H}(\xi)\,d\xi$, then
$\partial_x f(u(x_i)) = \left(\mathcal{H}(x_{i+1/2}) - \mathcal{H}(x_{i-1/2})\right)/h$
exactly. A numerical flux that approximates $\mathcal{H}(x_{i+1/2})$ to
order $r$ therefore gives an $r$-th order conservative difference. The
point values $f(u_j)$ are the cell averages of $\mathcal{H}$, so the
[reconstruction from cell averages](/methods/finite-volume-reconstruction.md)
applies verbatim with $f$ in place of $\bar u$: the primitive of
$\mathcal{H}$ is $h\sum_{j\le i} f(u_j)$ at interfaces, and the
divided differences of that primitive come from those of $f$
([Shu & Osher (1989)](/sources/shu-1989.md); [Shu (1998)](/sources/shu-1998.md),
Problem 2.2). [Shu & Osher (1988)](/sources/shu-1988.md) had obtained
the same accuracy with correction terms,
$\hat f_{i+1/2} = f_{i+1/2} + \sum_k a_{2k} h^{2k}\,\partial_x^{2k} f\big\vert_{i+1/2}$
with $a_2 = -\tfrac{1}{24}$, $a_4 = \tfrac{7}{5760}$; the 1989 form is a
simpler equivalent.

## Upwinding

ENO and WENO reconstruction of the flux must be upwind-biased; the bias
is set by the first stencil point or by the linear weights.
* **Flux splitting** $f = f^+ + f^-$, $df^+/du \ge 0$, $df^-/du \le 0$:
  reconstruct $f^+$ from the left and $f^-$ from the right and add. The
  splitting must be as smooth as the order of the scheme, which rules
  out van Leer and Osher splittings at high order; Lax–Friedrichs,
  $f^\pm = \tfrac12(f \pm \alpha u)$, is the standard choice
  ([Shu (1998)](/sources/shu-1998.md), §2.3.2;
  [Jiang & Shu (1996)](/sources/jiang-1996.md)). Any splitting yields a
  [monotone flux](/definitions/monotone-flux.md)
  $\hat f(a,b) = f^+(a) + f^-(b)$, but not every monotone flux splits
  (Godunov's does not).
* **ENO-Roe**: upwind by the sign of the Roe speed $\hat a_{i+1/2}$
  (a single difference table, half the cost); it admits stationary
  entropy-violating expansion shocks.
* **ENO-LLF**: a local Lax–Friedrichs splitting with $\alpha_{i+1/2}$
  the maximum of $\vert f'\vert$ between $u_i$ and $u_{i+1}$; uniformly
  high order, sonic points included.
* **ENO-RF** (Roe with entropy fix): Roe where $f'$ keeps its sign
  between $u_i$ and $u_{i+1}$, LLF otherwise; always converged to the
  entropy solution in their tests and is the recommended variant.
  Numerical viscosity decreases from LF to LLF to Roe
  ([Shu & Osher (1989)](/sources/shu-1989.md), §II).
* Using a general E-flux as the building block costs accuracy at sonic
  points, where most E-fluxes are only Lipschitz
  ([Shu & Osher (1988)](/sources/shu-1988.md), §III).
* [Balsara & Shu (2000)](/sources/balsara-2000.md) take the LLF speed as
  $\chi$ times the maximum over the whole stencil, $\chi \approx 1.1$–$1.3$
  (more robust at reflecting walls), use LLF in linearly degenerate
  fields and RF in genuinely nonlinear ones, and cure a mild carbuncle
  at a grid-aligned shock by switching to LLF near shocks.

Systems are split in [local characteristic fields](/methods/characteristic-decomposition.md).

## Multi-D, grids and cost

* The difference is applied dimension by dimension with all other
  indices fixed; no multi-D reconstruction and no flux quadrature are
  needed, and the order is kept ([Shu & Osher (1988)](/sources/shu-1988.md),
  [(1989)](/sources/shu-1989.md)). The CFL condition becomes
  $\Delta t\sum_d \max\vert f_d'\vert/h_d \le$ const.
* **Uniform grids only.** Third- and higher-order conservative
  differences of point values exist only on uniform or smoothly varying
  (mapped) grids: on a general non-uniform grid no choice of constants
  depending on the local spacings gives more than second order
  ([Shu (1998)](/sources/shu-1998.md), §2.1.2, "a simple exercise of
  Taylor expansions"). Smooth mappings keep the scheme conservative.
* For linear constant-coefficient problems in 1D the finite-difference
  and finite-volume schemes coincide except for their initial data; not
  for nonlinear problems ([Shu (1998)](/sources/shu-1998.md)). In 2D the
  finite-difference version costs about a quarter of the finite-volume
  one, and Shu recommends it whenever possible
  ([Shu (1998)](/sources/shu-1998.md), §3.3.2;
  [Balsara & Shu (2000)](/sources/balsara-2000.md), §I).
* [Suresh & Huynh (1997)](/sources/suresh-1997.md) build their 2D MP5
  scheme in this framework (ENO-LLF with the MP5 reconstruction).

**Later remarks (batch 2).** $\mathcal{H} = f + O(h^2)$ but is not the
exact flux for finite $h$; the same stencil for $\hat f_{i\pm1/2}$ makes
the leading $O(h^5)$ flux errors cancel in the difference
([Henrick et al. (2005)](/sources/henrick-2005.md), §2). A compact
(implicit) flux keeps conservation and the Lax–Wendroff property though
it is not local in the data ([Pirozzoli (2002)](/sources/pirozzoli-2002.md);
[hybrid compact-WENO](/methods/hybrid-compact-weno.md)).

# Citations

1. [Shu & Osher (1988)](/sources/shu-1988.md), §§III–IV.
2. [Shu & Osher (1989)](/sources/shu-1989.md), §§I–II, IV.
3. [Shu (1998)](/sources/shu-1998.md), §§2.1.2, 2.3.2, 3.1.2, 3.3.2.
4. [Jiang & Shu (1996)](/sources/jiang-1996.md), §2.
5. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §3.
6. [Balsara & Shu (2000)](/sources/balsara-2000.md), §§I–II, VII.b.
7. [Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md), §2.
8. [Pirozzoli (2002)](/sources/pirozzoli-2002.md), §2.

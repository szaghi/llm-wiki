---
type: Operator
title: "Central first difference $D_0$"
description: "The central difference (f_{j+1} - f_{j-1})/(2h) approximating f' at x_j, second-order accurate with leading error (h^2/6) f'''_j, more accurate than either one-sided difference."
status: established
symbol: "$D_0$"
aliases: [central difference, centred difference, central difference approximation]
tags: [finite-difference, truncation-error]
timestamp: 2026-10-13T00:00:00Z
---

# Central first difference $D_0$

On a uniform grid of spacing $h$,
$$D_0 f_j = \frac{f_{j+1} - f_{j-1}}{2h}.$$
Subtracting the Taylor expansions
$f_{j\pm1} = f_j \pm hf^{(1)}_j + \frac{h^2}{2!}f^{(2)}_j \pm \frac{h^3}{3!}f^{(3)}_j + \cdots$
(eq. 27.56) gives
([Riley et al. (2006)](/sources/riley-2006.md), eq. 27.57)
$$f^{(1)}_j = D_0 f_j - \frac{h^2}{3!}f^{(3)}_j - \cdots,$$
so $D_0$ "is in error by approximately $(h^2/6)f^{(3)}_j$" (§27.5, p. 1019).
It is the better of the three first-difference approximations derived there;
the [one-sided differences](/operators/one-sided-differences.md) err at
$O(h)$.

## Remarks

* The source uses $D_0$ to diagnose the forward-Euler step: its forward
  difference $D_+$ approximates the derivative at $x_j + h/2$ better than at
  $x_j$ (§27.6.1, p. 1021). Milne's method is "based on central differences"
  (see [Milne's method](/methods/milne-central-difference-method.md)).
* The error statements are truncation errors of Taylor series for smooth $f$.
  The chapters read contain no Fourier (wavenumber) analysis of $D_0$.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §27.5 (eqs. 27.56–27.57, p. 1019), §27.6.1 (pp. 1021–1022).

---
type: Operator
title: "One-sided first differences $D_+$, $D_-$"
description: "The forward difference (f_{j+1} - f_j)/h and backward difference (f_j - f_{j-1})/h approximating f' at x_j, first-order accurate with leading errors of opposite sign, -(h/2) f''_j and +(h/2) f''_j, poorer than the central difference."
status: established
symbol: "$D_+$, $D_-$"
aliases: [forward difference, backward difference, one-sided difference]
tags: [finite-difference, truncation-error]
timestamp: 2026-10-13T00:00:00Z
---

# One-sided first differences $D_+$, $D_-$

$$D_+ f_j = \frac{f_{j+1} - f_j}{h},\qquad D_- f_j = \frac{f_j - f_{j-1}}{h}.$$
From the Taylor expansion of $f_{j+1}$ alone
([Riley et al. (2006)](/sources/riley-2006.md), eq. 27.58):
$$f^{(1)}_j = D_+ f_j - \frac{h}{2!}f^{(2)}_j - \cdots,$$
so the forward difference "is clearly a poorer approximation, since it is in
error by approximately $(h/2)f^{(2)}_j$ as compared with $(h^2/6)f^{(3)}_j$"
for the [central difference](/operators/central-difference.md). The backward
difference, from $f_{j-1}$, "is not as good as the central difference; the sign
of the error is reversed in this case" (§27.5, p. 1019). Then
$f^{(1)}_j = D_- f_j + \frac{h}{2}f^{(2)}_j + \cdots$; this sign form is the
compiler's reading of that sentence.

## Remarks

* $D_+$ in time is the forward [Euler method](/methods/forward-euler-method.md).
  The source notes that $D_+ f_j$ is "a closer approximation to $\mathrm df/\mathrm dx$
  evaluated at $x = x_j + h/2$ than ... at $x = x_j$" (p. 1021).
* No Fourier analysis of these operators appears in the chapters read.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §27.5 (eq. 27.58, p. 1019), §27.6.1 (pp. 1021–1022).

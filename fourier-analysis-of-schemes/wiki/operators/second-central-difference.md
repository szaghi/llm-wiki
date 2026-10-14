---
type: Operator
title: "Second central difference $D_+D_-$"
description: "The second difference (f_{j+1} - 2 f_j + f_{j-1})/h^2 approximating f'' at x_j, obtained by adding the two Taylor expansions, with error about (h^2/12) f''''_j; exact when f is a polynomial of low enough degree, so constant second differences detect a quadratic and locate tabulation errors."
status: established
symbol: "$D_+D_-$"
aliases: [second difference, three-point second difference, central second difference]
tags: [finite-difference, truncation-error]
timestamp: 2026-10-13T00:00:00Z
---

# Second central difference $D_+D_-$

$$D_+D_- f_j = \frac{f_{j+1} - 2f_j + f_{j-1}}{h^2} \approx f^{(2)}_j$$
([Riley et al. (2006)](/sources/riley-2006.md), eq. 27.59), obtained by adding
the expansions (27.56) of $f_{j\pm1}$. The error, "also known as the second
difference of $f$", is "easily shown to be about $(h^2/12)f^{(4)}_j$"
(§27.5, p. 1019). The source gives no sign. A compiler remark, from the same
expansion: $D_+D_- f_j = f^{(2)}_j + \frac{h^2}{12}f^{(4)}_j + O(h^4)$.

## Exactness on polynomials

"If the function $f(x)$ is a sufficiently simple polynomial in $x$, all
derivatives beyond a particular one will vanish and there is no error in
taking the differences to obtain the derivatives" (pp. 1019–1020). The worked
example uses this to repair a table of a quadratic at unit spacing. The
undivided second differences $f_{j+1} - 2f_j + f_{j-1}$ must all equal the
same constant ($2$ there). That fixes two illegible entries and one
transcription error, $46 \to 44$. The procedure would fail if the error sat
where no two computable second differences agree (p. 1020).

## Remarks

The chapters read contain no Fourier analysis of $D_+D_-$.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §27.5 (eq. 27.59 and worked example, pp. 1019–1020).

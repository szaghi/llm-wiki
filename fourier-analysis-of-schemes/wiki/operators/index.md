# Operators

Discrete operators and their algebraic identities.

* [Central first difference $D_0$](/operators/central-difference.md) — The central difference (f_{j+1} - f_{j-1})/(2h) approximating f' at x_j, second-order accurate with leading error (h^2/6) f'''_j, more accurate than either one-sided difference.
* [One-sided first differences $D_+$, $D_-$](/operators/one-sided-differences.md) — The forward difference (f_{j+1} - f_j)/h and backward difference (f_j - f_{j-1})/h approximating f' at x_j, first-order accurate with leading errors of opposite sign, -(h/2) f''_j and +(h/2) f''_j, poorer than the central difference.
* [Second central difference $D_+D_-$](/operators/second-central-difference.md) — The second difference (f_{j+1} - 2 f_j + f_{j-1})/h^2 approximating f'' at x_j, obtained by adding the two Taylor expansions, with error about (h^2/12) f''''_j; exact when f is a polynomial of low enough degree, so constant second differences detect a quadratic and locate tabulation errors.

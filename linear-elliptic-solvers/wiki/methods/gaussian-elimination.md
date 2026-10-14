---
type: Method
title: "Gaussian elimination with interchange"
description: "Direct solution of a square system by successive elimination of unknowns and back substitution, with rows reordered before each elimination so that the largest remaining coefficient in modulus is on the leading diagonal (partial pivoting) to limit rounding-error growth."
status: established
aliases: [Gaussian elimination, Gauss elimination, partial pivoting, pivoting, row interchange, elimination with interchange, Gauss-Jordan elimination, Gauss-Jordan inversion]
tags: [linear-algebra, direct-solver, rounding-error]
timestamp: 2026-10-14T00:00:00Z
---

# Gaussian elimination with interchange

**Method.** For square $A\mathbf x=\mathbf b$, each equation in turn is used
to eliminate one unknown from all the remaining ones until a single
equation in one unknown is left; the unknowns are then recovered by
substitution in reverse order
([Riley et al. (2006)](/sources/riley-2006.md), §27.3.1, p. 995).
[Arfken et al. (2013)](/sources/arfken-2013.md) describe the same procedure,
dividing each equation by its leading coefficient before subtracting, and
call it "well adapted to computers and ... far faster than" Cramer's rule
(§2.1, Example 2.1.4, pp. 91–92). They cite Press et al. (1992) for
production codes (footnote 1, p. 91).

**Interchange (partial pivoting).** Before eliminating $x_i$, the remaining
equations are reordered to bring the coefficient of $x_i$ largest in
modulus onto the leading diagonal; row $j$ is then replaced by
$\text{row}_j-(a_{ji}/a_{ii})\,\text{row}_i$. This is "the only, but
essential, difference from straightforward elimination". The stated
motivation, given without analysis ("we will merely state this"): rounding
errors can become excessive when $N$ is large and particularly when the
diagonal entries are small compared with the off-diagonal ones — for
example "unforeseeable zeros or very small numbers appearing on the leading
diagonal" in a 1000-unknown program (pp. 995–996).

*Qualification (when the reordering is done), Arfken et al.* Arfken et al.
also reorder for accuracy, but once, before elimination starts: "For
convenience and for the optimum numerical accuracy, the equations are
rearranged so that, to the extent possible, the largest coefficients run
along the main diagonal" (p. 91). Riley et al. reorder before every
elimination step, which is partial pivoting proper. Neither book analyses
the error.

**Worked case.** The $3\times3$ system of eq. 27.22 is solved with one
interchange, giving $\mathbf x=(10,1,2)^{\mathsf T}$; the same system is
the [Gauss–Seidel](/methods/gauss-seidel-iteration.md) test (pp. 996–998).

**Determinant as a by-product.** Without the right-hand side, the
elimination reduces $\det A$ to triangular form, so the determinant is the
product of the pivots, corrected for the rows divided out (Arfken et al.,
eq. 2.24, p. 93).

**Gauss–Jordan inversion** (Arfken et al., Example 2.2.3, pp. 100–102).
Each elementary row operation — scaling a row, subtracting a multiple of
another row, interchanging two rows — is left multiplication by a matrix
(exercise 2.2.21); applying to $I$ the same sequence of operations that
reduces a non-singular $A$ to $I$ produces $A^{-1}$. The book calls it
"computationally more efficient" than the cofactor formula of the
[determinant](/definitions/determinant.md) page and works a $3\times3$
example.

**Scope of the sources.** No operation count, error bound or growth-factor
discussion is given in either; the relation of elimination to the
[LU decomposition](/methods/lu-decomposition.md) of §8.18.2 is not stated
by Riley et al.,
the two being presented in different chapters, and Arfken et al. do not
treat LU at all. The general remark that
the work for most matrix equations grows roughly as $N^3$ is in §27.3.3
(p. 998).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §27.3.1 (pp. 995–996),
  §8.18.2 (p. 295).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §2.1 (pp. 91–93), §2.2
  (pp. 100–102, 118).

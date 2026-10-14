---
type: Method
title: "Gaussian elimination with interchange"
description: "Direct solution of a square system by successive elimination of unknowns and back substitution, with rows reordered before each elimination so that the largest remaining coefficient in modulus is on the leading diagonal (partial pivoting) to limit rounding-error growth."
status: established
aliases: [Gaussian elimination, partial pivoting, pivoting, row interchange, elimination with interchange]
tags: [linear-algebra, direct-solver, rounding-error]
timestamp: 2026-10-13T00:00:00Z
---

# Gaussian elimination with interchange

**Method.** For square $A\mathbf x=\mathbf b$, each equation in turn is used
to eliminate one unknown from all the remaining ones until a single
equation in one unknown is left; the unknowns are then recovered by
substitution in reverse order
([Riley et al. (2006)](/sources/riley-2006.md), §27.3.1, p. 995).

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

**Worked case.** The $3\times3$ system of eq. 27.22 is solved with one
interchange, giving $\mathbf x=(10,1,2)^{\mathsf T}$; the same system is
the [Gauss–Seidel](/methods/gauss-seidel-iteration.md) test (pp. 996–998).

**Scope of the source.** No operation count, error bound or growth-factor
discussion is given; the relation of elimination to the
[LU decomposition](/methods/lu-decomposition.md) of §8.18.2 is not stated,
the two being presented in different chapters. The general remark that
the work for most matrix equations grows roughly as $N^3$ is in §27.3.3
(p. 998).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §27.3.1 (pp. 995–996),
  §8.18.2 (p. 295).

---
type: Result
title: "Quotient law"
description: "If a set of quantities A, contracted with an arbitrary tensor B, gives a tensor C in every coordinate frame, then A is itself a tensor; the practical test for tensor character, proved in the source for Cartesian second-order tensors."
status: established
aliases: [quotient theorem, quotient rule for tensors]
tags: [tensor-calculus, cartesian-tensors]
timestamp: 2026-10-14T00:00:00Z
---

# Quotient law

**Statement** ([Riley et al. (2006)](/sources/riley-2006.md), §26.7,
eq. (26.25), pp. 939–940). If $B$ and $C$ are tensors of orders $N$ and
$M+N-2$ and

$$A_{pq\cdots k\cdots m}B_{ij\cdots k\cdots n}=C_{pq\cdots mij\cdots n}$$

holds in all rotated coordinate frames, with $B$ arbitrary, then the
$A_{pq\cdots k\cdots m}$ are the components of an $M$th-order tensor. The
contracted index may sit anywhere in $A$ and $B$.

**Second statement and proof.** [Arfken et al. (2013)](/sources/arfken-2013.md) (§4.1,
eqs. (4.20)–(4.24), pp. 211–213) state the rule for general coordinates: if
an equation such as $A^j{}_iB_j=C_i$, with $B$ arbitrary and $C$ a known
tensor, "holds in all transformed coordinate systems", then $A$ "is a tensor of
the indicated rank and covariant/contravariant character". They prove this
mixed case under general (not only rotational) coordinate
changes, using the inverse transformation law of $B$ and the arbitrariness
of $B$ (eq. (4.24)), and note a pitfall: the rule "does not necessarily
apply if" the right-hand side "is zero", since the transformation properties of zero are
indeterminate (p. 213). "The quotient rule is a substitute for the illegal
division of tensors" (p. 213). Exercises: the metric tensor from the
invariance of $g_{ij}d\xi^id\xi^j$ (4.1.10), $A^{ij}B_{jk}=C^i{}_k$ (4.1.11),
and the dual pseudovector (4.2.1).

**Scope of Riley's proof.** Proved for $M=N=2$, Cartesian tensors under
rotations ($A_{pk}B_{ik}=C_{pi}$ gives $(A'_{pk}-L_{pq}L_{kl}A_{ql})B'_{ik}=0$
for arbitrary $B'$, p. 940); the general case is asserted to follow on the
same lines. The book then applies the law without further proof to general
tensors: $\partial\phi/\partial\xi^i$ is a covariant vector because
$d\phi=(\partial\phi/\partial\xi^i)d\xi^i$ is a scalar for the contravariant
vector $d\xi^i$ (p. 968), and $v^i{}_{;j}$ is a tensor because
$\partial_j\mathbf v=v^i{}_{;j}\mathbf a_i$ (p. 969;
[covariant derivative](/definitions/covariant-derivative.md)).

**Use.** Contracting a candidate set with an arbitrary tensor (e.g. an
outer product $x_ix_j$) and checking that the result is a scalar is
"generally much more convenient than making a direct substitution"
(pp. 940–941). Examples: the inertia tensor, conductivity and
susceptibility are second-order tensors because they map vectors to vectors
(§26.12, pp. 950–952). See [Cartesian tensor](/definitions/cartesian-tensor.md)
and [general tensor](/definitions/general-tensor.md).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §26.7, pp. 939–941; §26.12, pp. 950–952; §26.19, pp. 968–969.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §4.1, pp. 211–213; §4.3, p. 219; exercises 4.1.10, 4.1.11, 4.2.1, pp. 215, 217.

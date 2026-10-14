---
type: Result
title: "Quotient law"
description: "If a set of quantities A, contracted with an arbitrary tensor B, gives a tensor C in every coordinate frame, then A is itself a tensor; the practical test for tensor character, proved in the source for Cartesian second-order tensors."
status: established
aliases: [quotient theorem, quotient rule for tensors]
tags: [tensor-calculus, cartesian-tensors]
timestamp: 2026-10-13T00:00:00Z
---

# Quotient law

**Statement** ([Riley et al. (2006)](/sources/riley-2006.md), §26.7,
eq. (26.25), pp. 939–940). If $B$ and $C$ are tensors of orders $N$ and
$M+N-2$ and

$$A_{pq\cdots k\cdots m}B_{ij\cdots k\cdots n}=C_{pq\cdots mij\cdots n}$$

holds in all rotated coordinate frames, with $B$ arbitrary, then the
$A_{pq\cdots k\cdots m}$ are the components of an $M$th-order tensor. The
contracted index may sit anywhere in $A$ and $B$.

**Scope of the proof.** Proved for $M=N=2$, Cartesian tensors under
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

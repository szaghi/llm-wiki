---
type: Definition
title: "Relative tensor"
description: "A set of components that transforms like a general tensor times the w-th power of the Jacobian determinant |∂ξ/∂ξ̄|; weight 1 is a tensor density, weight −1 a general pseudotensor, so the metric determinant g has weight 2, √g weight 1 and the permutation symbols ε_ijk, ε^ijk weights −1 and +1."
status: established
aliases: [tensor density, weight of a tensor, pseudotensor, scalar density, relative scalar, pseudovector, dual tensor]
tags: [tensor-calculus, coordinate-transformation, jacobian]
timestamp: 2026-10-14T00:00:00Z
---

# Relative tensor

Under a change of coordinates $\xi\mapsto\bar\xi$, a **relative tensor of
weight $w$** transforms as a [general tensor](/definitions/general-tensor.md)
times the $w$-th power of the determinant $\lvert\partial\xi/\partial\bar\xi\rvert$
([Riley et al. (2006)](/sources/riley-2006.md), §26.17, eq. (26.74), p. 964):

$$\bar T^{ij\cdots k}{}_{lm\cdots n}=\frac{\partial\bar\xi^i}{\partial\xi^a}\cdots\frac{\partial\bar\xi^k}{\partial\xi^c}\,\frac{\partial\xi^d}{\partial\bar\xi^l}\cdots\frac{\partial\xi^f}{\partial\bar\xi^n}\;T^{a\cdots c}{}_{d\cdots f}\;\left\lvert\frac{\partial\xi}{\partial\bar\xi}\right\rvert^{w}.$$

* $w=0$: an absolute (true) tensor. $w=-1$: a **general pseudotensor**.
  $w=1$: a **tensor density** (p. 964).
* **Weight convention.** The power is taken of $\lvert\partial\xi/\partial\bar\xi\rvert$,
  the determinant of old with respect to new coordinates. Sources that define
  weight with the reciprocal determinant have the opposite sign of $w$;
  compare weights only after checking which determinant is meant.
* The metric determinant $g$ is a relative scalar of weight 2:
  $\bar g=\lvert\partial\xi/\partial\bar\xi\rvert^2g$ (worked example, p. 964,
  from $\bar G=U^{\mathsf T}GU$ with $U=[\partial\xi^i/\partial\bar\xi^j]$).
  Hence $\sqrt g$ — the [Jacobian](/definitions/jacobian.md) magnitude —
  is a scalar density of weight 1 (consequence of the stated weight-2 law).
* The [Levi-Civita symbol](/definitions/levi-civita-symbol.md) $\varepsilon_{ijk}$
  is a covariant relative tensor of weight $-1$; $\varepsilon^{ijk}$,
  numerically equal, has weight $+1$ (p. 964).
* Outer products and contractions add weights, $w_1+w_2$ (pp. 964–965). So
  for an antisymmetric absolute tensor $A^{jk}$, $p_i=\tfrac12\varepsilon_{ijk}A^{jk}$
  is a pseudovector of weight $-1$, and $A^{ij}=\varepsilon^{ijk}p_k$ (p. 965).
  The same counting shows that $\varepsilon^{ijk}/\sqrt g$, which appears in
  the general-coordinate [curl](/definitions/curl.md), is an absolute tensor
  (compiler's remark from the stated weights).

## Cartesian special case

For rotations of Cartesian axes the Jacobian is $\pm1$. Components that
transform with an extra factor $\det L$,
$T'_{ij\cdots k}=\det L\;L_{il}L_{jm}\cdots L_{kn}T_{lm\cdots n}$, are
**Cartesian pseudotensors** (eq. (26.39), p. 947): they behave as tensors
under proper rotations and change sign under improper ones (reflections,
inversion). Relative tensors of weight $\pm1$ both satisfy this definition
(p. 964). [Arfken et al. (2013)](/sources/arfken-2013.md) give the same Cartesian definition,
$\mathbf v'=\det L\;L\mathbf v$ for pseudovectors (eqs. (3.30), (4.26),
pp. 136, 215) and its extension to pseudotensors of any rank (p. 216), with
the multiplication rule tensor $\otimes$ pseudotensor = pseudotensor,
pseudotensor $\otimes$ pseudotensor = tensor (eq. (4.27)); the scalar triple
product is a pseudoscalar (p. 137). They treat pseudotensors in Cartesian
systems only, "for practical reasons" (§4.2, p. 215), and do not introduce
weights or densities for general coordinates. The vector product $\varepsilon_{ijk}b_jc_k$ of two vectors is a
pseudovector: it gives the components of $\mathbf b\times\mathbf c$ only in a
right-handed frame (§26.10, p. 948). The **dual** of an antisymmetric
second-order tensor, $p_i=\tfrac12\varepsilon_{ijk}A_{jk}$, is a pseudovector
with $A_{ij}=\varepsilon_{ijk}p_k$ (§26.11, eq. (26.40), pp. 949–950;
Arfken et al., eqs. (4.31)–(4.33), pp. 216–217, and exercise 4.2.7, which
call the pair "dual tensors ... simply different representations of the
same information"). The
book stresses that physical quantities (velocity, magnetic field, angular
momentum) are vectors, not pseudovectors; pseudovectors are a property of a
component representation under passive improper transformations
(§26.10, pp. 948–949).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §26.10, pp. 946–949; §26.11, pp. 949–950; §26.17, pp. 963–965.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §3.3, pp. 136–137; §4.2, pp. 215–218 (Cartesian pseudotensors and duals only).

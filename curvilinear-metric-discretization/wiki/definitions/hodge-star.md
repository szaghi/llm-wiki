---
type: Definition
title: "Hodge star operator"
description: "The operator ⋆ mapping a p-form to its complementary (D−p)-form, defined from a metric and an orientation: in Euclidean three-space ⋆1 = dx^1∧dx^2∧dx^3, ⋆dx^1 = dx^2∧dx^3 (cyclically), ⋆(dx^1∧dx^2) = dx^3, ⋆(dx^1∧dx^2∧dx^3) = 1, with ⋆⋆ = identity there but not in Minkowski space."
status: established
aliases: [Hodge operator, star operator, Hodge dual, complementary form, dual form]
symbol: "$\\star$"
tags: [differential-forms, exterior-calculus, metric]
timestamp: 2026-10-14T00:00:00Z
---

# Hodge star operator

**Definition** ([Arfken et al. (2013)](/sources/arfken-2013.md), §4.5,
pp. 235–236). In a space of dimension $D$ every $p$-form has a
**complementary** (dual) $(D-p)$-form containing the differentials it lacks.
The Hodge star $\star$ produces it. Its definition requires a **metric** and
an **orientation** (a standard order of the basis 1-forms). For an
orthogonal basis of 1-forms, with a metric whose diagonal elements are
$\pm1$, the rule for a monomial $\alpha$ is:

1. write the wedge product $\alpha'$ of the basis 1-forms absent from
   $\alpha$, with the sign of the permutation that brings (indices of
   $\alpha$, indices of $\alpha'$) to the standard order;
2. multiply by $(-1)^\mu$, $\mu$ being the number of differentials *in
   $\alpha$* whose metric diagonal element is $-1$.

"If the 1-form basis is not orthogonal there result complications we shall
not discuss" (p. 235): the book gives no Hodge star for a non-orthogonal
basis or a non-unit metric, and so none for general curvilinear coordinates.

**Euclidean three-dimensional space** (eq. (4.81), p. 236), with the indices
in cyclic order:

$$\begin{aligned}
\star1&=dx^1\wedge dx^2\wedge dx^3,\\
\star dx^1&=dx^2\wedge dx^3,\quad \star dx^2=dx^3\wedge dx^1,\quad \star dx^3=dx^1\wedge dx^2,\\
\star(dx^2\wedge dx^3)&=dx^1,\quad \star(dx^3\wedge dx^1)=dx^2,\quad \star(dx^1\wedge dx^2)=dx^3,\\
\star(dx^1\wedge dx^2\wedge dx^3)&=1,
\end{aligned}$$

all consistent with $\star\star\alpha=\alpha$. Other cases follow by
permuting the differentials and tracking signs.

**Minkowski space** (Example 4.5.2, eq. (4.82), pp. 236–237; outside this
bundle's Euclidean scope): with the oriented basis $(dt,dx^1,dx^2,dx^3)$ and
metric $\operatorname{diag}(1,-1,-1,-1)$, the forms of even degree satisfy
$\star\star\alpha=-\alpha$, so "complementing twice does not always restore
the original form with its original sign" (p. 237).

## Use

* With the [wedge product](/definitions/wedge-product.md) it gives the cross
  product, $\star(\alpha\wedge\beta)\leftrightarrow\mathbf v\times\mathbf w$,
  and the triple product, $\star(\alpha\wedge\beta\wedge\gamma)=\mathbf v\cdot(\mathbf w\times\mathbf b)$
  (eqs. (4.83)–(4.84), pp. 237–238).
* With the [exterior derivative](/definitions/exterior-derivative.md) it
  gives the curl as a 1-form, $\star d(v_k\,dx^k)=(\nabla\times\mathbf v)_k\,dx^k$,
  and the divergence as a 0-form, $\star d(b_1\,dx^2\wedge dx^3+b_2\,dx^3\wedge dx^1+b_3\,dx^1\wedge dx^2)=\nabla\cdot\mathbf b$
  (eqs. (4.88), (4.90), p. 240), in Cartesian coordinates.
* Maxwell's equations take the two-line form "$d$ of the field 2-form
  vanishes; $d$ of its star equals the source 3-form" in Minkowski space
  (Example 4.6.2, eq. (4.99), pp. 241–243; Arfken's symbols are not
  registered here, since the bundle's $J$ is the Jacobian).

*Compiler's remark.* Every metric dependence of the vector operators sits in
$\star$: $d$ is metric-free. For curvilinear coordinates the book stops at
orthonormal bases, so this bundle has, as yet, no source for $\star$ written
with $g_{ij}$ and $\sqrt g$; the relation to the tensor forms of the
[divergence](/definitions/divergence.md) and [curl](/definitions/curl.md)
remains to be sourced.

# Citations

* [Arfken et al. (2013)](/sources/arfken-2013.md), §4.5, pp. 235–238; §4.6, pp. 240–243.

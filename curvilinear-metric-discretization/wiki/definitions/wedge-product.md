---
type: Definition
title: "Wedge product"
description: "The exterior product ∧ of differential forms: distributive, associative and antisymmetric on 1-forms (dx^i∧dx^j = −dx^j∧dx^i, so dx^i∧dx^i = 0); it builds p-forms, makes the signed Jacobian appear under a change of variables, and with the Hodge star reproduces the cross and triple products in three dimensions."
status: established
aliases: [exterior product, exterior algebra, Grassmann algebra, wedge]
symbol: "$\\wedge$"
tags: [differential-forms, exterior-calculus, jacobian]
timestamp: 2026-10-14T00:00:00Z
---

# Wedge product

**Axioms** ([Arfken et al. (2013)](/sources/arfken-2013.md), §4.5,
eq. (4.80), p. 234). For forms $\alpha_1,\alpha_2$ of equal degree, any forms
$\alpha_3$, functions $a,b$, and basis 1-forms $dx^i$:

$$\begin{aligned}
(a\alpha_1+b\alpha_2)\wedge\alpha_3&=a\,\alpha_1\wedge\alpha_3+b\,\alpha_2\wedge\alpha_3,\\
(\alpha_1\wedge\alpha_2)\wedge\alpha_3&=\alpha_1\wedge(\alpha_2\wedge\alpha_3),\qquad a(\alpha_1\wedge\alpha_2)=(a\alpha_1)\wedge\alpha_2,\\
dx^i\wedge dx^j&=-dx^j\wedge dx^i .
\end{aligned}$$

The operations are "designed to create permutational antisymmetry" (p. 234).
Consequences stated in the source:

* Coefficient functions can be collected in front, so no parentheses are
  needed: $a\,dx^1\wedge b\,dx^2=ab\,dx^1\wedge dx^2$ (p. 234).
* $dx^i\wedge dx^i=0$; a product with a repeated (or linearly dependent)
  differential vanishes, hence only $p\le D$ survives
  ([differential form](/definitions/differential-form.md)).
* Any product of distinct differentials equals $\varepsilon_P$ times the
  product in ascending index order, $\varepsilon_P$ being the sign of the
  sorting permutation — the sign rule of the terms of a determinant (p. 234).
* Worked example (p. 235):
  $(3dx+4dy-dz)\wedge(dx-dy+2dz)=7(dy\wedge dz-dz\wedge dx-dx\wedge dy)$; in
  three dimensions the book prefers the **cyclic** order
  $dy\wedge dz$, $dz\wedge dx$, $dx\wedge dy$, which makes the duals of the
  [Hodge star](/definitions/hodge-star.md) all positive.

## Change of variables

For the linear map $x=au+bv$, $y=eu+fv$ (with $a,b,e,f$ constants),

$$dx\wedge dy=(af-be)\,du\wedge dv,$$

and $af-be$ is the determinant of $[\partial(x,y)/\partial(u,v)]$, the
[Jacobian](/definitions/jacobian.md) (eqs. (4.103)–(4.104), §4.7, p. 244).
"The Jacobian occurred as a natural consequence of the transformation; we
did not have to take additional steps to insert it" (p. 245). Because
$dx\wedge dy=-dy\wedge dx$, areas carry signs and the sign of the Jacobian
must be **retained**; the same holds for $p>2$, where
$dx\wedge dy\wedge\cdots$ becomes $J\,du\wedge dv\wedge\cdots$ with the
signed $J$ (p. 245; exercise 4.7.1 for the 3-form). The source states the
rule for $p>2$ and for general (non-linear) changes of variables without
further proof.

## Vector products in three dimensions

For 1-forms $\alpha=v_k\,dx^k$, $\beta=w_k\,dx^k$ and $\gamma=b_k\,dx^k$ in
Euclidean three-dimensional space (Example 4.5.3, eqs. (4.83)–(4.84),
pp. 237–238):

$$\star(\alpha\wedge\beta)=(\mathbf v\times\mathbf w)_1\,dx^1+(\mathbf v\times\mathbf w)_2\,dx^2+(\mathbf v\times\mathbf w)_3\,dx^3,\qquad \star(\alpha\wedge\beta\wedge\gamma)=\mathbf v\cdot(\mathbf w\times\mathbf b),$$

the second because $\alpha\wedge\beta\wedge\gamma=\det[\mathbf v;\mathbf w;\mathbf b]\;dx^1\wedge dx^2\wedge dx^3$.
The sign of $\star(\alpha\wedge\beta)$ follows from the chosen standard
order $(dx,dy,dz)$. The book stresses that these relations generalise to
any dimension and metric, while the cross product is specific to
three-dimensional space (p. 238; §3.2, p. 128).

# Citations

* [Arfken et al. (2013)](/sources/arfken-2013.md), §4.5, pp. 233–238; §4.7, pp. 244–245; exercise 4.7.1, p. 248.

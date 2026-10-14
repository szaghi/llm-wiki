---
type: Result
title: "Vector operator identities"
description: "The product rules of grad, div and curl (Table 10.1), the identities curl grad φ = 0 and div curl v = 0, ∇·(∇φ×∇ψ) = 0, and curl curl v = grad div v − ∇²v; coordinate-independent, provable compactly with the ε–δ identity."
status: established
aliases: [vector identities, product rules, curl of gradient, divergence of curl, BAC-CAB for operators]
tags: [vector-calculus, identities, operators]
timestamp: 2026-10-14T00:00:00Z
---

# Vector operator identities

For differentiable scalar fields $\phi,\psi$ and vector fields $\mathbf v,\mathbf w$
([Riley et al. (2006)](/sources/riley-2006.md), §10.8, Table 10.1, p. 354):

$$\begin{aligned}
\nabla(\phi\psi)&=\phi\nabla\psi+\psi\nabla\phi,\\
\nabla(\mathbf v\cdot\mathbf w)&=\mathbf v\times(\nabla\times\mathbf w)+\mathbf w\times(\nabla\times\mathbf v)+(\mathbf v\cdot\nabla)\mathbf w+(\mathbf w\cdot\nabla)\mathbf v,\\
\nabla\cdot(\phi\mathbf v)&=\phi\nabla\cdot\mathbf v+\mathbf v\cdot\nabla\phi,\\
\nabla\cdot(\mathbf v\times\mathbf w)&=\mathbf w\cdot(\nabla\times\mathbf v)-\mathbf v\cdot(\nabla\times\mathbf w),\\
\nabla\times(\phi\mathbf v)&=\nabla\phi\times\mathbf v+\phi\nabla\times\mathbf v,\\
\nabla\times(\mathbf v\times\mathbf w)&=\mathbf v(\nabla\cdot\mathbf w)-\mathbf w(\nabla\cdot\mathbf v)+(\mathbf w\cdot\nabla)\mathbf v-(\mathbf v\cdot\nabla)\mathbf w,
\end{aligned}$$

plus linearity of all three operators. [Arfken et al. (2013)](/sources/arfken-2013.md) prove
the product rules for $\nabla\cdot(\phi\mathbf v)$, $\nabla\times(\phi\mathbf v)$
and $\nabla(\mathbf v\cdot\mathbf w)$ (eqs. (3.72)–(3.74), pp. 156–157, the
last via the BAC–CAB rule with $\nabla$ acting on one factor at a time) and
set $\nabla(\phi\psi)$, $\nabla\cdot(\mathbf v\times\mathbf w)$ and
$\nabla\times(\mathbf v\times\mathbf w)$ as exercises 3.5.5, 3.5.9, 3.6.5
(pp. 152–153, 157), in agreement with the table. Second-order combinations
(§10.8.2, eqs. (10.37)–(10.43), pp. 356–357):

$$\nabla\times\nabla\phi=\mathbf 0,\qquad \nabla\cdot(\nabla\times\mathbf v)=0,\qquad \nabla\times(\nabla\times\mathbf v)=\nabla(\nabla\cdot\mathbf v)-\nabla^2\mathbf v,\qquad \nabla\cdot(\nabla\phi\times\nabla\psi)=0.$$

Arfken et al. state the first three identically (eqs. (3.64), (3.65),
(3.70), p. 155), with the double-curl identity taken as the *definition* of
the vector Laplacian, and the fourth as exercise 3.6.13 ($\nabla\phi\times\nabla\psi$
is solenoidal, p. 158).

* **Coordinate independence**: "although some of the following vector
  relations are expressed in Cartesian coordinates, it may be proved that
  they are all independent of the choice of coordinate system", because grad,
  div and curl have coordinate-free definitions
  ([integral definitions](/results/integral-definitions-of-grad-div-curl.md))
  (p. 354).
* **Proof route**: direct calculation, or "a quick method ... using tensor
  notation" with the [Levi-Civita symbol](/definitions/levi-civita-symbol.md)
  (p. 354; exercise 26.6 lists five of them). Arfken et al. prove
  $\nabla\times\nabla\phi=\mathbf 0$ and $\nabla\cdot(\nabla\times\mathbf v)=0$
  as determinants with two equal rows (pp. 154–155), and again as instances
  of $d\circ d=0$ for forms (eqs. (4.91)–(4.92), p. 241;
  [exterior derivative](/definitions/exterior-derivative.md)), "merely the
  first members of hierarchies of identities" in higher dimensions.
* **Qualification: smoothness.** Riley states the identities for
  differentiable fields. Arfken et al. state the hypothesis the two
  second-order identities actually use: the order of the mixed partial
  derivatives can be reversed, "which is true so long as these second
  derivatives of $\phi$ are continuous", and $\nabla\cdot(\nabla\times\mathbf v)=0$
  "if $\mathbf v$ has sufficient continuity" (pp. 154–155). A difference in
  stated conditions, not in conclusion.
* **Use in curvilinear coordinates**: the last identity applied to
  $\phi=\xi^2$, $\psi=\xi^3$ gives $\nabla\cdot(\nabla\xi^2\times\nabla\xi^3)=0$,
  the step that yields the orthogonal-coordinate
  [divergence](/definitions/divergence.md); $\nabla\times\nabla\xi^1=\mathbf 0$
  does the same for the [curl](/definitions/curl.md) (pp. 368–369).
* **Vector Laplacian caveat**: the double-curl identity holds in all
  coordinates, but only in Cartesians may it be split component-wise
  ([Laplacian](/definitions/laplacian.md); p. 357; Arfken et al., p. 155).
* **Consequences**: a gradient is irrotational, a curl solenoidal; adding
  $\nabla\phi+\mathbf c$ to an irrotational field, or a constant to a
  solenoidal one, preserves the property (p. 356;
  [conservative vector field](/definitions/conservative-vector-field.md)).

Special cases for $r=\lvert\mathbf x\rvert$ (p. 355): $\nabla\phi(r)=(d\phi/dr)\hat{\mathbf x}$,
$\nabla\cdot[\phi(r)\mathbf x]=3\phi+r\,d\phi/dr$, $\nabla\times[\phi(r)\mathbf x]=\mathbf 0$,
$\nabla\cdot\mathbf x=3$, $\nabla\cdot(\hat{\mathbf x}/r^2)=-\nabla^2(1/r)=4\pi\delta(\mathbf x)$,
with $\hat{\mathbf x}=\mathbf x/r$. Arfken et al. derive the same
special cases in Cartesian and in spherical coordinates, adding
$\nabla r^n=nr^{n-1}\hat{\mathbf x}$, $\nabla\cdot(r^n\hat{\mathbf x})=(n+2)r^{n-1}$
and $\nabla^2r^n=n(n+1)r^{n-2}$ (eqs. (3.50), (3.54), (3.161)–(3.164),
pp. 146–147, 154, 192–193).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §10.8, pp. 354–357; §10.10, pp. 368–369; §26.8, pp. 943–944; exercise 26.6, p. 978.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §3.5, pp. 145–147; §3.6, pp. 153–158; §3.10, pp. 192–193; §4.6, p. 241; exercises 3.5.5, 3.5.9, 3.6.5, 3.6.13, pp. 152–158.

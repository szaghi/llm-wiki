---
type: Result
title: "Vector operator identities"
description: "The product rules of grad, div and curl (Table 10.1), the identities curl grad φ = 0 and div curl v = 0, ∇·(∇φ×∇ψ) = 0, and curl curl v = grad div v − ∇²v; coordinate-independent, provable compactly with the ε–δ identity."
status: established
aliases: [vector identities, product rules, curl of gradient, divergence of curl, BAC-CAB for operators]
tags: [vector-calculus, identities, operators]
timestamp: 2026-10-13T00:00:00Z
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

plus linearity of all three operators. Second-order combinations
(§10.8.2, eqs. (10.37)–(10.43), pp. 356–357):

$$\nabla\times\nabla\phi=\mathbf 0,\qquad \nabla\cdot(\nabla\times\mathbf v)=0,\qquad \nabla\times(\nabla\times\mathbf v)=\nabla(\nabla\cdot\mathbf v)-\nabla^2\mathbf v,\qquad \nabla\cdot(\nabla\phi\times\nabla\psi)=0.$$

* **Coordinate independence**: "although some of the following vector
  relations are expressed in Cartesian coordinates, it may be proved that
  they are all independent of the choice of coordinate system", because grad,
  div and curl have coordinate-free definitions
  ([integral definitions](/results/integral-definitions-of-grad-div-curl.md))
  (p. 354).
* **Proof route**: direct calculation, or "a quick method ... using tensor
  notation" with the [Levi-Civita symbol](/definitions/levi-civita-symbol.md)
  (p. 354; exercise 26.6 lists five of them).
* **Use in curvilinear coordinates**: the last identity applied to
  $\phi=\xi^2$, $\psi=\xi^3$ gives $\nabla\cdot(\nabla\xi^2\times\nabla\xi^3)=0$,
  the step that yields the orthogonal-coordinate
  [divergence](/definitions/divergence.md); $\nabla\times\nabla\xi^1=\mathbf 0$
  does the same for the [curl](/definitions/curl.md) (pp. 368–369).
* **Vector Laplacian caveat**: the double-curl identity holds in all
  coordinates, but only in Cartesians may it be split component-wise
  ([Laplacian](/definitions/laplacian.md); p. 357).
* **Consequences**: a gradient is irrotational, a curl solenoidal; adding
  $\nabla\phi+\mathbf c$ to an irrotational field, or a constant to a
  solenoidal one, preserves the property (p. 356;
  [conservative vector field](/definitions/conservative-vector-field.md)).

Special cases for $r=\lvert\mathbf x\rvert$ (p. 355): $\nabla\phi(r)=(d\phi/dr)\hat{\mathbf x}$,
$\nabla\cdot[\phi(r)\mathbf x]=3\phi+r\,d\phi/dr$, $\nabla\times[\phi(r)\mathbf x]=\mathbf 0$,
$\nabla\cdot\mathbf x=3$, $\nabla\cdot(\hat{\mathbf x}/r^2)=-\nabla^2(1/r)=4\pi\delta(\mathbf x)$,
with $\hat{\mathbf x}=\mathbf x/r$.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §10.8, pp. 354–357; §10.10, pp. 368–369; §26.8, pp. 943–944; exercise 26.6, p. 978.

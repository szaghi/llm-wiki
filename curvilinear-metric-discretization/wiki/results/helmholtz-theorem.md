---
type: Result
title: "Helmholtz theorem"
description: "A vector field is uniquely determined in a simply connected region by its divergence, its curl and its normal component on the boundary; and a field whose divergence and curl vanish at infinity is the sum of an irrotational part −∇φ and a solenoidal part ∇×w, with φ and w the Newtonian potentials of ∇·v/4π and ∇×v/4π."
status: established
aliases: [Helmholtz decomposition, Helmholtz-Hodge decomposition, fundamental theorem of vector calculus, uniqueness theorem for vector fields]
tags: [vector-calculus, potential-theory, integral-theorems]
timestamp: 2026-10-14T00:00:00Z
---

# Helmholtz theorem

[Arfken et al. (2013)](/sources/arfken-2013.md) (§3.9, pp. 177–180) proves
two theorems that "establish conditions for the existence and uniqueness of
solutions to time-independent problems in electromagnetic theory".

## 1. Uniqueness

"A vector field is uniquely specified by giving its divergence and its curl
within a simply connected region and its normal component on the boundary"
(p. 177). Points where the divergence or curl exist only as delta functions
are not removed from the region (p. 178).

**Proof given** (pp. 177–178). Two fields with the same $\nabla\cdot\mathbf v$,
$\nabla\times\mathbf v$ and $\hat{\mathbf n}\cdot\mathbf v$ on the boundary
differ by a field $\mathbf w$ that is irrotational, solenoidal and has zero
normal component. Irrotational in a simply connected region,
$\mathbf w=-\nabla\phi$ ([conservative vector field](/definitions/conservative-vector-field.md));
solenoidal, so $\nabla^2\phi=0$. Green's first identity with both functions
equal to $\phi$ ([Green's identities](/results/greens-identities.md),
Arfken's eq. (3.86)) and $\partial\phi/\partial n=0$ on the boundary give
$\int_V\mathbf w\cdot\mathbf w\,dV=0$, hence $\mathbf w=\mathbf 0$.

## 2. Decomposition

"A vector P with both source and circulation densities vanishing at infinity
may be written as the sum of two parts, one of which is irrotational, the
other of which is solenoidal" (p. 178): with $\mathbf v$ for the field,

$$\mathbf v=-\nabla\phi+\nabla\times\mathbf w,\qquad \phi(\mathbf x)=\frac{1}{4\pi}\int\frac{\nabla_{\mathbf y}\cdot\mathbf v(\mathbf y)}{\lvert\mathbf x-\mathbf y\rvert}\,dV_{\mathbf y},\qquad \mathbf w(\mathbf x)=\frac{1}{4\pi}\int\frac{\nabla_{\mathbf y}\times\mathbf v(\mathbf y)}{\lvert\mathbf x-\mathbf y\rvert}\,dV_{\mathbf y}$$

(eqs. (3.123)–(3.125)). **Proof given** (pp. 178–179): with
$\nabla^2(1/\lvert\mathbf x-\mathbf y\rvert)=-4\pi\delta(\mathbf x-\mathbf y)$
(eq. (3.121); [Laplacian](/definitions/laplacian.md)) one checks
$-\nabla^2\phi=\nabla\cdot\mathbf v$; for the curl,
$\nabla\times(\nabla\times\mathbf w)=\nabla(\nabla\cdot\mathbf w)-\nabla^2\mathbf w$
([vector operator identities](/results/vector-operator-identities.md)), the
first term vanishes after an integration by parts because the divergence of
a curl is zero, and the Cartesian components of $-\nabla^2\mathbf w$ return
$\nabla\times\mathbf v$. Since $\mathbf v$ and the reconstructed field share
divergence and curl and vanish at infinity, uniqueness (part 1) identifies
them.

The book uses the theorem to legitimise splitting electromagnetic fields
into an irrotational and a solenoidal part represented by scalar and vector
potentials (pp. 179–180). The representation is in all space with fields
vanishing at infinity; the source does not treat the bounded-domain
decomposition with boundary terms.

*Compiler's remark.* Part 1 is the continuum reason why a discretisation
that controls a field's divergence, curl and boundary normal flux controls
the field; no source of this bundle yet makes that argument for a discrete
operator.

# Citations

* [Arfken et al. (2013)](/sources/arfken-2013.md), §3.9, pp. 177–180; eq. (3.121), p. 177.

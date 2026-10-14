---
type: Definition
title: "Conservative vector field"
description: "A vector field whose line integral between two points is path-independent; in a simply connected region this is equivalent to being a gradient of a single-valued scalar potential, to being irrotational, and to v·dx being an exact differential. Solenoidal fields are, dually, curls of a vector potential."
status: established
aliases: [irrotational field, scalar potential, solenoidal field, vector potential, exact differential, path independence]
tags: [vector-calculus, integral-theorems]
timestamp: 2026-10-13T00:00:00Z
---

# Conservative vector field

A vector field $\mathbf v$ with continuous partial derivatives in a **simply
connected** region is **conservative** if, and only if, any one of the
following holds; each implies the other three
([Riley et al. (2006)](/sources/riley-2006.md), §11.4, pp. 387–389):

1. $\int_A^B\mathbf v\cdot d\mathbf x$ is independent of the path between
   $A$ and $B$; hence $\oint_C\mathbf v\cdot d\mathbf x=0$ around every closed
   loop in the region.
2. There is a single-valued scalar function $\phi$ with $\mathbf v=\nabla\phi$.
3. $\nabla\times\mathbf v=\mathbf 0$ (the field is **irrotational**).
4. $\mathbf v\cdot d\mathbf x$ is an exact differential.

The chain (1)⇒(4)⇒(2)⇒(3) uses $d\phi=\nabla\phi\cdot d\mathbf x$; (3)⇒(1)
uses [Stokes' theorem](/results/stokes-theorem.md), which is why simple
connectivity is required. The **scalar potential** $\phi$ is unique up to an
additive constant (p. 389). In the plane the test reduces to
$\partial P/\partial y=\partial Q/\partial x$, from
[Green's theorem in the plane](/results/greens-theorem-in-the-plane.md)
(eq. (11.5), p. 386).

**Connectivity matters.** A region is simply connected if every simple closed
curve in it can be shrunk to a point without leaving it; a plane region with
$n-1$ holes is $n$-fold connected (§11.2, p. 383). In a multiply connected
region an irrotational field can have a multivalued potential: the vortex
$\mathbf u=\hat{\mathbf a}_\varphi/R$ is irrotational except on the axis,
$\phi=\varphi$, and $\oint_C\mathbf u\cdot d\mathbf x=2\pi n$ for a loop
winding $n$ times round the axis (§11.9.2, pp. 408–409); the book writes
$\nabla\times\mathbf u=2\pi\delta(R)$ to keep Stokes' theorem valid.

**Solenoidal fields.** A field with $\nabla\cdot\mathbf b=0$ is
**solenoidal**; then a **vector potential** $\mathbf v$ with
$\mathbf b=\nabla\times\mathbf v$ exists ("it may be shown", p. 389), and
$\mathbf v+\nabla\psi+\mathbf c$ is another one for any scalar $\psi$ and
constant $\mathbf c$ (pp. 356, 389). Conversely, every gradient is
irrotational and every curl is solenoidal
([vector operator identities](/results/vector-operator-identities.md)).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §10.7, pp. 352–353; §10.8.2, p. 356; §§11.2–11.4, pp. 383–389; §11.9.2, pp. 408–409.

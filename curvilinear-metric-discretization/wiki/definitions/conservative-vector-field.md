---
type: Definition
title: "Conservative vector field"
description: "A vector field whose line integral between two points is path-independent; in a simply connected region this is equivalent to being a gradient of a single-valued scalar potential, to being irrotational, and to v·dx being an exact differential. Solenoidal fields are, dually, curls of a vector potential."
status: established
aliases: [irrotational field, scalar potential, solenoidal field, vector potential, exact differential, path independence]
tags: [vector-calculus, integral-theorems]
timestamp: 2026-10-14T00:00:00Z
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

[Arfken et al. (2013)](/sources/arfken-2013.md) (§3.9, eqs. (3.96)–(3.100), pp. 171–172)
state the equivalence of (1), (2), (3) "over a given simply connected region
of space (one with no holes)", proving (2)⇒(1) by $\nabla\phi\cdot d\mathbf x=d\phi$,
(2)⇒(3) by $\nabla\times\nabla\phi=\mathbf 0$, (1)⇔(3) by
[Stokes' theorem](/results/stokes-theorem.md) on a differential loop, and
(1)⇒(2) from the vanishing of $\int(\mathbf v-\nabla\phi)\cdot d\mathbf x$
for all endpoints. (Arfken's sign convention for forces, $\mathbf F=-\nabla\phi$,
only flips the sign of the potential.) In the language of
[differential forms](/definitions/differential-form.md), (4) says that the
1-form $v_k\,dx^k$ is exact (Arfken et al., eqs. (4.100)–(4.101), p. 244).

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
constant $\mathbf c$ (pp. 356, 389). Arfken et al. prove existence by
construction (eq. (3.102), pp. 172–173): for $\nabla\cdot\mathbf b=0$,

$$\mathbf v=\mathbf e_2\int_{x_0}^{x}b_3(x,y,z)\,dx+\mathbf e_3\left[\int_{y_0}^{y}b_1(x_0,y,z)\,dy-\int_{x_0}^{x}b_2(x,y,z)\,dx\right]$$

satisfies $\nabla\times\mathbf v=\mathbf b$, the $\mathbf e_1$ component using
$\nabla\cdot\mathbf b=0$; $x_0,y_0$ are arbitrary and a second formula follows
with the roles of $x$ and $y$ exchanged (eq. (3.103)). They stress that the
vector potential is "far from unique" (any gradient may be added) and
reconcile three different potentials of a uniform field by such gauge
terms (Example 3.9.2, p. 174). Conversely, every gradient is
irrotational and every curl is solenoidal
([vector operator identities](/results/vector-operator-identities.md)).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §10.7, pp. 352–353; §10.8.2, p. 356; §§11.2–11.4, pp. 383–389; §11.9.2, pp. 408–409.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §3.9, pp. 170–174; §4.7, p. 244; exercises 3.6.11, 3.9.12, 3.10.16, 4.7.3, pp. 158, 182, 199, 248.

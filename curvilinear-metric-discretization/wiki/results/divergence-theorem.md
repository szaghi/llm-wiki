---
type: Result
title: "Divergence theorem"
description: "For a vector field continuous and differentiable in a volume V bounded by a closed surface S, ∫_V ∇·v dV = ∮_S v·dS; with its corollaries ∫_V ∇φ dV = ∮_S φ dS and ∫_V ∇×v dV = ∮_S dS×v, its tensor form, and its use to turn integral conservation laws into differential ones."
status: established
aliases: [Gauss's theorem, Gauss-Ostrogradsky theorem, Green's theorem in space, divergence theorem for tensors]
tags: [integral-theorems, conservation-form, vector-calculus]
timestamp: 2026-10-14T00:00:00Z
---

# Divergence theorem

**Statement** ([Riley et al. (2006)](/sources/riley-2006.md), §11.8,
eq. (11.18), p. 401). If $\mathbf v$ is continuous and differentiable in a
volume $V$ bounded by the closed surface $S$, with outward
[vector area element](/definitions/vector-area-element.md) $d\mathbf S$,

$$\int_V\nabla\cdot\mathbf v\,dV=\oint_S\mathbf v\cdot d\mathbf S.$$

It holds for simply and multiply connected closed surfaces enclosing a
non-zero volume (p. 401). [Arfken et al. (2013)](/sources/arfken-2013.md) state the same
equation as **Gauss' theorem**, $\oint_{\partial V}\mathbf v\cdot d\mathbf S=\int_V\nabla\cdot\mathbf v\,dV$,
for $\mathbf v$ and its first derivatives continuous over a simply connected
region (§3.8, eq. (3.81), p. 164), and check it on a tetrahedron
(Example 3.8.1, p. 165).

**Argument given.** Divide $V$ into small volumes $V_i$, apply the integral
definition $(\nabla\cdot\mathbf v)V_i\approx\oint_{S_i}\mathbf v\cdot d\mathbf S$
([integral definitions](/results/integral-definitions-of-grad-div-curl.md)),
and sum: every interior face appears twice with opposite outward normals and
cancels, leaving only the faces on $S$; let $V_i\to0$ (p. 401). The book
presents this as a heuristic derivation, not a rigorous proof; the telescoping
cancellation of shared faces is the same bookkeeping that makes a
finite-volume sum over cells conservative (compiler's remark). Arfken et al.
give the same argument with parallelepipeds: "outflow from one
parallelepiped is inflow to its neighbor; in a summation of all the
outflows, all the contributions of interior boundaries cancel" (pp. 164–165,
fig. 3.15), and the alternative reading that both sides sum the same
outflow, by elements of volume or by elements of the boundary (p. 165).
They recover the theorem a second time as the 3-form case of
[Stokes' theorem for differential forms](/results/generalized-stokes-theorem.md)
(Example 4.7.3, eq. (4.117), p. 248).

**Qualification: connectivity.** Riley states the theorem for simply and
multiply connected closed surfaces (p. 401); Arfken et al. assume a simply
connected region, "regions that contain holes, like a donut, are not simply
connected" (p. 164), and to apply it to a region containing a point charge
they excise a small sphere and join it to the outer boundary by a thin tube
"thereby creating a simply connected region" (Gauss's law, pp. 175–176,
fig. 3.18). The result they then obtain — the outer-surface integral equals
minus the inner-sphere integral with the inward-pointing normal — is
Riley's multiply connected statement with all boundary components included.
The books differ in the hypothesis stated, not in any conclusion; recorded
as a qualification. (Arfken's "no holes" usage also differs from Riley's
definition of simple connectivity by shrinking closed curves, §11.2,
p. 383, under which a ball with a spherical cavity is simply connected;
compiler's remark.)

**Corollaries.**
* With $\mathbf v=\mathbf x$: $V=\frac13\oint_S\mathbf x\cdot d\mathbf S$ (p. 401;
  Arfken et al., exercise 3.8.2, p. 169;
  [closed-surface vector area](/results/closed-surface-vector-area.md)).
* With $\mathbf v=\phi\mathbf c$ and $\mathbf v=\mathbf b\times\mathbf c$,
  $\mathbf c$ constant and arbitrary (eqs. (11.21)–(11.22), p. 403):
  $$\int_V\nabla\phi\,dV=\oint_S\phi\,d\mathbf S,\qquad \int_V\nabla\times\mathbf b\,dV=\oint_S d\mathbf S\times\mathbf b.$$
  Arfken et al. derive both by the same arbitrary-constant-vector device
  (eqs. (3.87)–(3.90), p. 166; "this exploitation of the arbitrary nature of
  a part of a problem is a valuable and widely used technique").
* Over all space, if the volume integral converges,
  $\int\nabla\cdot\mathbf v\,dV=0$ (Arfken et al., eq. (3.82), p. 165); the
  integration-by-parts rules $\int\phi\,\nabla\cdot\mathbf v\,dV=-\int\mathbf v\cdot\nabla\phi\,dV$
  and $\int\mathbf w\cdot\nabla\times\mathbf v\,dV=\int\mathbf v\cdot\nabla\times\mathbf w\,dV$
  hold when the integrated terms vanish at infinity (eqs. (3.78)–(3.80),
  p. 163).
* In two dimensions, with outward normal $\hat{\mathbf n}\,ds=dy\,\mathbf e_1-dx\,\mathbf e_2$:
  $\iint_R(\partial_xv_x+\partial_yv_y)\,dx\,dy=\oint_C(v_x\,dy-v_y\,dx)$,
  which is [Green's theorem in the plane](/results/greens-theorem-in-the-plane.md)
  (p. 402).
* [Green's identities](/results/greens-identities.md) follow with
  $\mathbf v=\phi\nabla\psi$ (§11.8.1).

**Tensor form** (§26.13, p. 954; stated, "we shall not prove it
rigorously"): for Cartesian tensor components,
$\int_V\partial T_{ij\cdots k\cdots m}/\partial x_k\,dV=\oint_ST_{ij\cdots k\cdots m}\hat n_k\,dS$.
Worked example: with $T_{ij}=x_ia_j$, a solenoidal field with
$\mathbf a\cdot\hat{\mathbf n}=0$ on $S$ has $\int_V\mathbf a\,dV=\mathbf 0$
(p. 954).

**Conservation laws** (§11.8.3, pp. 404–405). For an arbitrary fixed volume,
$\frac{d}{dt}\int_V\rho\,dV+\oint_S\rho\mathbf u\cdot d\mathbf S=0$ becomes
$\int_V[\partial_t\rho+\nabla\cdot(\rho\mathbf u)]\,dV=0$, and since $V$ is
arbitrary and the integrand continuous, the **continuity equation**
$\partial_t\rho+\nabla\cdot(\rho\mathbf u)=0$ follows. Point sources are
admitted by writing $\nabla\cdot\mathbf u=Q\,\delta(\mathbf x)$ (p. 405). The
derivation uses a volume fixed in space; volumes moving with a grid are not
treated in the source. Arfken et al. derive the same continuity equation
from the flux balance of a parallelepiped (eqs. (3.55)–(3.56), p. 148) and turn
Gauss's law of electrostatics (outward flux of the electric field equals the
enclosed charge divided by the permittivity) into its differential form by
the same arbitrary-volume argument (eqs. (3.115)–(3.116), p. 176), also for
a fixed volume.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §11.8, pp. 401–405; §26.13, p. 954.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §3.5, p. 148; §3.7, p. 163; §3.8, pp. 164–166; §3.9, pp. 175–176; §4.7, p. 248; exercises 3.8.1–3.8.5, p. 169.

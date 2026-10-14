---
type: Result
title: "Divergence theorem"
description: "For a vector field continuous and differentiable in a volume V bounded by a closed surface S, ∫_V ∇·v dV = ∮_S v·dS; with its corollaries ∫_V ∇φ dV = ∮_S φ dS and ∫_V ∇×v dV = ∮_S dS×v, its tensor form, and its use to turn integral conservation laws into differential ones."
status: established
aliases: [Gauss's theorem, Gauss-Ostrogradsky theorem, Green's theorem in space, divergence theorem for tensors]
tags: [integral-theorems, conservation-form, vector-calculus]
timestamp: 2026-10-13T00:00:00Z
---

# Divergence theorem

**Statement** ([Riley et al. (2006)](/sources/riley-2006.md), §11.8,
eq. (11.18), p. 401). If $\mathbf v$ is continuous and differentiable in a
volume $V$ bounded by the closed surface $S$, with outward
[vector area element](/definitions/vector-area-element.md) $d\mathbf S$,

$$\int_V\nabla\cdot\mathbf v\,dV=\oint_S\mathbf v\cdot d\mathbf S.$$

It holds for simply and multiply connected closed surfaces enclosing a
non-zero volume (p. 401).

**Argument given.** Divide $V$ into small volumes $V_i$, apply the integral
definition $(\nabla\cdot\mathbf v)V_i\approx\oint_{S_i}\mathbf v\cdot d\mathbf S$
([integral definitions](/results/integral-definitions-of-grad-div-curl.md)),
and sum: every interior face appears twice with opposite outward normals and
cancels, leaving only the faces on $S$; let $V_i\to0$ (p. 401). The book
presents this as a heuristic derivation, not a rigorous proof; the telescoping
cancellation of shared faces is the same bookkeeping that makes a
finite-volume sum over cells conservative (compiler's remark).

**Corollaries.**
* With $\mathbf v=\mathbf x$: $V=\frac13\oint_S\mathbf x\cdot d\mathbf S$ (p. 401;
  [closed-surface vector area](/results/closed-surface-vector-area.md)).
* With $\mathbf v=\phi\mathbf c$ and $\mathbf v=\mathbf b\times\mathbf c$,
  $\mathbf c$ constant and arbitrary (eqs. (11.21)–(11.22), p. 403):
  $$\int_V\nabla\phi\,dV=\oint_S\phi\,d\mathbf S,\qquad \int_V\nabla\times\mathbf b\,dV=\oint_S d\mathbf S\times\mathbf b.$$
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
treated in the source.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §11.8, pp. 401–405; §26.13, p. 954.

---
type: Definition
title: "Validity of high-order curvilinear elements"
description: "A curved polynomial element is geometrically valid when its Jacobian determinant is strictly positive everywhere on the reference element; because that determinant is itself a polynomial, its expansion in a Bézier basis gives provable bounds (refined by subdivision), whereas sampling gives only a necessary condition; the distortion J/J0 relative to the straight-sided element measures quality."
status: established
aliases: [geometrical validity, curved element validity, scaled Jacobian, Jacobian bounds, Bézier bounds]
tags: [high-order-mesh, validity, element-jacobian, mesh-quality]
timestamp: 2026-11-08T21:01:00Z
---

# Validity of high-order curvilinear elements

A curved element of degree $k$ maps the reference element through Lagrange
shape functions; it is **valid** if the mapping is bijective, i.e. if its
Jacobian determinant $J(\boldsymbol\xi)$ is strictly positive everywhere on
the reference element ([Johnen, Remacle & Geuzaine 2013](/sources/johnen-2013.md)).
Unlike a straight-sided simplex, $J$ varies over the element, so its
minimum must be found.

## Distortion

With $J_0$ the Jacobian of the straight-sided element the curved one was
built from, the distortion (scaled Jacobian) $\mathcal D=J/J_0$ should stay
close to 1 ([notation](/notation.md)); a negative value means an invalid
element. [Xie et al. (2013)](/sources/xie-2013.md) use the ratio of the
minimum to the maximum of $|J|$ over the element as distortion measure,
modified to $\min J/\max|J|$ so that the sign reveals invalidity.

## Provable bounds

Checking $J$ at sample points (Xie et al. use the points of a quadrature of
order $2k$) is only a necessary condition, and more points need not mean a
better prediction. Johnen et al. use the fact that $J$ of a polynomial
element is a polynomial of higher degree: expanded in the Bézier (Bernstein)
basis, which is positive and a partition of unity, $J$ lies within the range
of its control values (convex-hull property). If the bound does not decide
the sign, the element is subdivided and new control values computed on each
part, with quadratic convergence, until it does; elements still undecided
after a limit are declared invalid. The method covers triangles,
quadrangles, tetrahedra, prisms and hexahedra and is fast: 8,112 invalid
elements among 82,009 sixth-order triangles were found in about 2 s, seven
times faster than brute-force sampling. Bounds of this kind drive the
untangling of [high-order mesh curving](/methods/high-order-mesh-curving.md),
and they are the curved-element counterpart of the
[mesh quality metrics](/definitions/mesh-quality-metric.md) of linear
elements.

## Optimizing the bound itself

Since the Bézier coefficients bound the Jacobian, the smallest coefficient
can be maximized directly; with one control point free this is a linear
program solved exactly by the simplex method
([Rochery & Loseille 2023](/sources/rochery-2023.md)).

## Validity, quality and fidelity

[Hu & Chen (2026)](/sources/hu-2026.md) organize the evaluation of curved
meshes in three parts: validity (positivity of the Jacobian), shape
quality (distortion) and fidelity of the curved boundary to the geometry.

# Citations

- [Johnen, Remacle & Geuzaine (2013)](/sources/johnen-2013.md) — whole paper.
- [Xie et al. (2013)](/sources/xie-2013.md) — validity and distortion measure.
- [Rochery & Loseille (2023)](/sources/rochery-2023.md) — method.
- [Hu & Chen (2026)](/sources/hu-2026.md) — §2.

---
type: Result
title: "Vector area of a closed surface"
description: "The vector area ∮_S dS of every closed surface is zero; hence the vector area of an open surface depends only on its perimeter, S = ½∮_C x×dx, and the enclosed volume is V = ⅓∮_S x·dS."
status: established
aliases: [closed surface vector area vanishes, vector area of a surface, surface closure, volume from surface integral]
tags: [integral-theorems, surfaces, geometry]
timestamp: 2026-10-14T00:00:00Z
---

# Vector area of a closed surface

The **vector area** of a surface is $\mathbf S=\int_Sd\mathbf S$
([vector area element](/definitions/vector-area-element.md))
([Riley et al. (2006)](/sources/riley-2006.md), §11.5.2, p. 393).

1. **Closed surfaces** (p. 394; [Arfken et al. (2013)](/sources/arfken-2013.md), exercise 3.8.1,
   p. 169, "using Gauss' theorem"): $\oint_Sd\mathbf S=\mathbf 0$. Argument given:
   project the surface on each Cartesian coordinate plane; each positive
   projected element of the upper part cancels a negative one of the lower
   part. (It also follows from $\int_V\nabla\phi\,dV=\oint_S\phi\,d\mathbf S$
   with $\phi=1$, eq. (11.21) of the [divergence theorem](/results/divergence-theorem.md);
   compiler's remark.)
2. **Open surfaces** (p. 394): two surfaces $S_1,S_2$ with the same perimeter
   $C$ form a closed surface $S_1-S_2$, so $\mathbf S_1=\mathbf S_2$: the vector
   area depends only on $C$. Taking a cone with vertex at the origin,
   $$\mathbf S=\frac12\oint_C\mathbf x\times d\mathbf x,$$
   which for a plane curve in the $xy$-plane gives $A=\frac12\oint_C(x\,dy-y\,dx)$
   ([Green's theorem in the plane](/results/greens-theorem-in-the-plane.md)).
   The same formula follows from the second corollary of
   [Stokes' theorem](/results/stokes-theorem.md) with $\mathbf b=\mathbf x$ (p. 408;
   Arfken et al., exercises 3.8.7–3.8.8, p. 170: $\lvert\oint_C\mathbf x\times d\mathbf x\rvert$
   is twice the enclosed area of a plane loop, and an ellipse gives $\pi ab$
   with $a,b$ its semi-axes). Arfken et al. also ask for the total vector area
   of the four faces of a tetrahedron (exercise 3.7.1, p. 163), zero by
   statement 1.
   The magnitude of $\mathbf S$ is a projected area, not the surface area:
   a hemisphere of radius $a$ has $\mathbf S=\pi a^2\mathbf e_3$ (p. 393).
3. **Volume** (§11.6.1, p. 397): $V=\frac13\oint_S\mathbf x\cdot d\mathbf S$,
   from cones with vertex at an interior origin; "it may be shown" to hold
   also when the origin is outside $V$; it is the divergence theorem with
   $\mathbf v=\mathbf x$ (p. 401; Arfken et al., exercise 3.8.2, p. 169,
   generalising exercise 3.7.5 on the unit cube).

The book notes that in practice the direct volume integral is usually
simpler (p. 397). Statements 1–3 are the continuum facts behind computing
face-area vectors and cell volumes of a hexahedral cell from its vertices;
the source does not discuss that use, and no source of this bundle yet does
(compiler's remark).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §11.5.2, pp. 393–395; §11.6.1, p. 397; §11.8, p. 401; §11.9.1, p. 408.
* [Arfken et al. (2013)](/sources/arfken-2013.md), exercises 3.7.1, 3.7.5, pp. 163–164; exercises 3.8.1, 3.8.2, 3.8.7, 3.8.8, pp. 169–170.

---
okf_version: "0.1"
---

# curvilinear-metric-discretization — Knowledge Bundle

Vector and tensor calculus in general coordinates and its discretization: integral theorems, curvilinear coordinates, metric tensor and Christoffel symbols, covariant derivatives, metric identities, the geometric conservation law, free-stream preservation, finite differences and finite volumes on curvilinear and moving grids.

**Start here:** the [Notation registry](/notation.md), which is normative
for every page, and the [update log](/log.md).

**Corpus:** 1 source, a scoped read —
[Riley et al. (2006)](/sources/riley-2006.md), Chs. 10, 11 and 26 (continuum
vector and tensor calculus). No source on metric discretization, the geometric
conservation law or free-stream preservation is ingested yet; those topics
have no pages. Citation record: [bibliography](/bibliography.md).

## Reading guide

**1. Coordinates and geometry of the mapping.** What a curvilinear system is,
and the objects it induces at every point.

* [General curvilinear coordinates](/definitions/curvilinear-coordinates.md) — the mapping $\mathbf x(\xi)$, coordinate surfaces and curves, orthogonality.
* [Covariant and contravariant bases](/definitions/covariant-and-contravariant-bases.md) — $\mathbf a_i=\partial\mathbf x/\partial\xi^i$, $\mathbf a^i=\nabla\xi^i$, reciprocity, components.
* [Metric tensor](/definitions/metric-tensor.md) — $g_{ij}$, $g^{ij}$, arc length, volume element, index raising.
* [Jacobian of the coordinate mapping](/definitions/jacobian.md) — $J$, $\lvert J\rvert=\sqrt g$, and the naming hazard.
* [Scale factors](/definitions/scale-factors.md) — the orthogonal special case.

**2. Integral theorems and the finite-volume viewpoint.**

* [Integral definitions of grad, div and curl](/results/integral-definitions-of-grad-div-curl.md) — operators as limits of surface and contour integrals.
* [Divergence theorem](/results/divergence-theorem.md), [Stokes' theorem](/results/stokes-theorem.md), [Green's theorem in the plane](/results/greens-theorem-in-the-plane.md), [Green's identities](/results/greens-identities.md).
* [Vector area element](/definitions/vector-area-element.md) and [vector area of a closed surface](/results/closed-surface-vector-area.md) — orientation, face area vectors, $\oint_S d\mathbf S=\mathbf 0$.

**3. Vector operators in any coordinates.**

* [Divergence](/definitions/divergence.md) — including the conservative form $(1/\sqrt g)\partial_j(\sqrt g\,v^j)$.
* [Gradient](/definitions/gradient.md), [Curl](/definitions/curl.md), [Laplacian](/definitions/laplacian.md).
* [Vector operator identities](/results/vector-operator-identities.md) and [conservative vector field](/definitions/conservative-vector-field.md).

**4. Tensor calculus.**

* [Christoffel symbols](/definitions/christoffel-symbols.md) and the [covariant derivative](/definitions/covariant-derivative.md).
* [General tensor](/definitions/general-tensor.md), [relative tensor](/definitions/relative-tensor.md) (weights, densities), [Cartesian tensor](/definitions/cartesian-tensor.md), [quotient law](/results/quotient-law.md), [Levi-Civita symbol](/definitions/levi-civita-symbol.md).

Folder catalogs: [definitions](/definitions/index.md),
[operators](/operators/index.md), [results](/results/index.md),
[sources](/sources/index.md).

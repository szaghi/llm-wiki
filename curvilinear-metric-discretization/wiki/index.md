---
okf_version: "0.1"
---

# curvilinear-metric-discretization — Knowledge Bundle

Vector and tensor calculus in general coordinates and its discretization: integral theorems, curvilinear coordinates, metric tensor and Christoffel symbols, covariant derivatives, metric identities, the geometric conservation law, free-stream preservation, finite differences and finite volumes on curvilinear and moving grids.

**Start here:** the [Notation registry](/notation.md), which is normative
for every page, and the [update log](/log.md).

**Corpus:** 5 sources. Two are scoped reads of textbooks —
[Riley et al. (2006)](/sources/riley-2006.md), Chs. 10, 11 and 26, and
[Arfken et al. (2013)](/sources/arfken-2013.md), Chs. 3 and 4 (continuum
vector and tensor calculus; Arfken adds Jacobians and differential forms).
Three are scoped reads of magnetic-confinement code papers that compute in
non-orthogonal, field-aligned coordinates —
[Jiang et al. (2024)](/sources/jiang-2024.md) and
[Liu et al. (2024)](/sources/liu-2024.md) (the GMEC code) and
[Seto et al. (2023)](/sources/seto-2023.md) (BOUT++) — read for their
coordinates, metrics, operators and finite-difference treatment only.
Shared claims carry every citation; one contradiction is open (the sign of
the twist-shift condition, on
[field-aligned coordinates](/definitions/field-aligned-coordinates.md)).
No source on the geometric conservation law or free-stream preservation is
ingested yet; the plasma codes evaluate their metrics from the equilibrium
and do not address discrete metric identities. Citation record:
[bibliography](/bibliography.md).

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
* [Helmholtz theorem](/results/helmholtz-theorem.md) — a field is fixed by its divergence, curl and boundary normal component; irrotational plus solenoidal decomposition.

**3. Vector operators in any coordinates.**

* [Divergence](/definitions/divergence.md) — including the conservative form $(1/\sqrt g)\partial_j(\sqrt g\,v^j)$.
* [Gradient](/definitions/gradient.md), [Curl](/definitions/curl.md), [Laplacian](/definitions/laplacian.md).
* [Vector operator identities](/results/vector-operator-identities.md) and [conservative vector field](/definitions/conservative-vector-field.md).

**4. Tensor calculus.**

* [Christoffel symbols](/definitions/christoffel-symbols.md) and the [covariant derivative](/definitions/covariant-derivative.md).
* [General tensor](/definitions/general-tensor.md), [relative tensor](/definitions/relative-tensor.md) (weights, densities), [Cartesian tensor](/definitions/cartesian-tensor.md), [quotient law](/results/quotient-law.md), [Levi-Civita symbol](/definitions/levi-civita-symbol.md).

**5. Differential forms.** The metric-free calculus of oriented integrands,
the continuum layer onto which discrete exterior calculus maps.

* [Differential form](/definitions/differential-form.md) — $p$-forms as oriented integrands of lines, surfaces, volumes; closed and exact forms.
* [Wedge product](/definitions/wedge-product.md) — exterior algebra; the signed Jacobian appears by itself under a change of variables.
* [Exterior derivative](/definitions/exterior-derivative.md) — $d$, with $d\circ d=0$; grad, curl, div as $d$ on 0-, 1-, 2-forms.
* [Hodge star operator](/definitions/hodge-star.md) — $\star$, where the metric enters.
* [Stokes' theorem for differential forms](/results/generalized-stokes-theorem.md) — $\int_\Omega d\alpha=\int_{\partial\Omega}\alpha$, uniting Green, Stokes and the divergence theorem.

**6. Coordinates adapted to a magnetic field.** Non-orthogonal coordinates
in use, with their metric, operators and discretization.

* [Magnetic flux coordinates](/definitions/magnetic-flux-coordinates.md) — $(\Psi,\vartheta,\varphi)$: orthogonal, PEST and Boozer variants; metric from the poloidal-plane mapping.
* [Field-aligned coordinates](/definitions/field-aligned-coordinates.md) — $\xi^3=\varphi-\chi$, $\mathbf B=\mathbf a_2/J$, sheared metric, twist-shift condition (open contradiction), flute-ordering error.
* [Shifted metric](/methods/shifted-metric.md) — Scott's, the simple and the quasi-ballooning variants; the boundary instability they remove.
* [GMEC](/software/gmec.md) and [BOUT++](/software/bout-plus-plus.md) — how two codes store metrics and difference the expanded operators.

Folder catalogs: [definitions](/definitions/index.md),
[methods](/methods/index.md), [operators](/operators/index.md),
[results](/results/index.md), [software](/software/index.md),
[sources](/sources/index.md).

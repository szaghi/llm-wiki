# Definitions

Precise domain terms.

* [Boundary-fitted coordinate system](/definitions/boundary-fitted-coordinate-system.md) — A structured (curvilinear) grid viewed as a one-to-one mapping from a rectangular computational domain onto the physical domain, with coordinate lines coincident with every boundary; the equations are transformed so that all computation runs on a uniform square mesh, and the generation methods divide into conformal, orthogonal, algebraic (interpolation), elliptic, hyperbolic and variational families.
* [Equidistribution principle](/definitions/equidistribution-principle.md) — Choose mesh points so that a positive monitor function, a measure of the solution error, is equalized over every cell: in one dimension the integral of the monitor up to x(ξ) is a fixed fraction ξ of its total; the principle underlies most adaptive and moving mesh equations.
* [Mesh quality metric](/definitions/mesh-quality-metric.md) — A scalar function of an element's node positions that measures a geometric property — volume, shape, skew, length ratio, orientation — defined algebraically from the element Jacobian relative to an ideal (target) element; the condition number shape metric measures the distance to degenerate elements and is equivalent to the mean ratio.

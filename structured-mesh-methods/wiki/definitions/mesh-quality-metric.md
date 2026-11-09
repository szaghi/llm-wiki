---
type: Definition
title: "Mesh quality metric"
description: "A scalar function of an element's node positions that measures a geometric property — volume, shape, skew, length ratio, orientation — defined algebraically from the element Jacobian relative to an ideal (target) element; the condition number shape metric measures the distance to degenerate elements and is equivalent to the mean ratio."
status: established
aliases: [element quality metric, algebraic quality metric, shape metric, condition number metric, mean ratio]
tags: [mesh-quality, element-jacobian, target-matrix]
timestamp: 2026-11-08T20:46:00Z
---

# Mesh quality metric

An **element quality metric** is a scalar function of an element's node
positions that measures one of its geometric properties
([Knupp 2001](/sources/knupp-2001.md)). Metrics serve as mesh specifications
before meshing, as objective functions of smoothing and optimization, and as
quality control of a finished mesh; h-refinement rarely improves the quality
of an initial mesh, and node-moving (r-type) adaptation can use them
directly.

## The algebraic framework

Knupp builds metrics from the element Jacobian $\mathsf A$ (corner or edge
vectors) and a key idea: a metric is **referenced** to an ideal element with
Jacobian $\mathsf W$, and measures the deviation $\mathsf T=\mathsf A\mathsf W^{-1}$
from it ([notation](/notation.md)). The ideal may be isotropic or anisotropic
with a preferred orientation. $\mathsf A$ factors into orientation (a
rotation), volume ($\det$), and shape, the shape splitting into length ratio
and skew — the complete list of element properties the Jacobian carries.
Desirable properties of a metric are listed: dimension-free, element-free,
domain-general, versatile, scale-free, orientation-free, unitless.

An **algebraic shape metric** $\mu(\mathsf T)$ is scale- and
orientation-invariant, equals 1 exactly when $\mathsf T$ is a scaled rotation
and 0 exactly when $\mathsf T$ is degenerate (singular but nonzero).
$\mu=d/\kappa(\mathsf T)$, with the condition number
$\kappa(\mathsf T)=|\mathsf T||\mathsf T^{-1}|$ in the Frobenius norm, is one;
$1/\kappa$ is the relative distance from $\mathsf T$ to the singular matrices,
so $\kappa$ measures how far the element is from degeneracy. Knupp proves the
condition number and mean-ratio metrics equivalent (the mean ratio being
conjugate to a modified Winslow functional), and recalls that radius ratio,
mean ratio and the sine of the solid angle are equivalent; skew,
length-ratio, volume, orientation and combined shape–volume(–orientation)
metrics are defined, and nonsimplicial elements are treated through corner
Jacobians at the price of homogeneity for volume metrics.

Knupp names, as future work, high-order elements with midside nodes, links
between metrics and analysis error, and metrics as objective functions of
mesh optimization. The structured-grid counterparts of these measures —
spacing variation, skewness, aspect ratio — enter the truncation error
directly ([grid-induced truncation error](/results/grid-induced-truncation-error.md)).

## Curved elements

For high-order curved elements the Jacobian varies inside the element, and
quality and validity are measured by the distortion relative to the
straight-sided element, bounded from its Bézier expansion
([validity of high-order curvilinear elements](/definitions/high-order-mesh-validity.md);
[Johnen, Remacle & Geuzaine 2013](/sources/johnen-2013.md)).

## Optimizing with the metrics

Knupp's referenced metrics became the objective functions of
[target-matrix optimization](/methods/target-matrix-optimization.md), with
targets at sub-element points for high-order elements
([Dobrev et al. 2019](/sources/dobrev-2019.md)).

# Citations

- [Knupp (2001)](/sources/knupp-2001.md) — §1–§9, conclusions.
- [Johnen, Remacle & Geuzaine (2013)](/sources/johnen-2013.md) — distortion.
- [Dobrev et al. (2019)](/sources/dobrev-2019.md) — §2.

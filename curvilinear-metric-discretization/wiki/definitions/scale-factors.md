---
type: Definition
title: "Scale factors"
description: "The lengths h_i = |∂x/∂ξ^i| of the covariant base vectors, which convert coordinate increments into distances; for orthogonal coordinates they fix arc length, volume element and the metric g_ij = h_i² δ_ij."
status: established
aliases: [Lamé coefficients, metric scale factors]
tags: [curvilinear-coordinates, metric]
timestamp: 2026-10-13T00:00:00Z
---

# Scale factors

For [general curvilinear coordinates](/definitions/curvilinear-coordinates.md)
$\xi^i$, the **scale factors** are the lengths of the covariant base vectors,

$$h_i=\left\lvert\frac{\partial\mathbf x}{\partial\xi^i}\right\rvert=\lvert\mathbf a_i\rvert,\qquad \hat{\mathbf a}_i=\frac{1}{h_i}\frac{\partial\mathbf x}{\partial\xi^i},$$

so that the distance moved when only $\xi^i$ changes by $d\xi^i$ is
$h_i\,d\xi^i$ (no sum) ([Riley et al. (2006)](/sources/riley-2006.md),
§10.10, p. 364). The general displacement is
$d\mathbf x=\sum_i h_i\,d\xi^i\,\hat{\mathbf a}_i$ (eq. (10.57)).

**Orthogonal systems only.** When the $\hat{\mathbf a}_i$ are mutually
perpendicular (§10.10, eq. (10.58), pp. 365–366):

$$(ds)^2=h_1^2(d\xi^1)^2+h_2^2(d\xi^2)^2+h_3^2(d\xi^3)^2,\qquad dV=h_1h_2h_3\,d\xi^1d\xi^2d\xi^3,$$

the [metric tensor](/definitions/metric-tensor.md) is diagonal,
$g_{ij}=h_i^2\delta_{ij}$, $g^{ij}=h_i^{-2}\delta_{ij}$, and
$g=h_1^2h_2^2h_3^2$ (§26.15, p. 957; §26.20, p. 972). For a non-orthogonal
system the scale factors do not determine $(ds)^2$ or $dV$: the off-diagonal
$g_{ij}$ enter (exercise 10.22 shows the extra $(ds)^2$ term and a $dV$
smaller than $h_1h_2h_3\,d\xi^1d\xi^2d\xi^3$, p. 374).

The scale factors give the orthogonal-coordinate forms of the
[gradient](/definitions/gradient.md), [divergence](/definitions/divergence.md),
[curl](/definitions/curl.md) and [Laplacian](/definitions/laplacian.md)
(Table 10.4, p. 369), and they relate contravariant to physical components:
$v^i=\hat v_i/h_i$ (no sum) (§26.20, p. 972).

| System | $h_1$ | $h_2$ | $h_3$ |
|---|---|---|---|
| cylindrical $(R,\varphi,z)$ | $1$ | $R$ | $1$ |
| spherical $(r,\theta,\varphi)$ | $1$ | $r$ | $r\sin\theta$ |

(§10.10, p. 365.)

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§10.9–10.10, pp. 358–369; §26.15, p. 957; §26.20, p. 972.

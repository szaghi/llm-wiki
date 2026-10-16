---
type: Definition
title: "Scale factors"
description: "The lengths h_i = |∂x/∂ξ^i| of the covariant base vectors, which convert coordinate increments into distances; for orthogonal coordinates they fix arc length, volume element and the metric g_ij = h_i² δ_ij."
status: established
aliases: [Lamé coefficients, metric scale factors]
tags: [curvilinear-coordinates, metric]
timestamp: 2026-10-16T00:00:00Z
---

# Scale factors

For [general curvilinear coordinates](/definitions/curvilinear-coordinates.md)
$\xi^i$, the **scale factors** are the lengths of the covariant base vectors,

$$h_i=\left\lvert\frac{\partial\mathbf x}{\partial\xi^i}\right\rvert=\lvert\mathbf a_i\rvert,\qquad \hat{\mathbf a}_i=\frac{1}{h_i}\frac{\partial\mathbf x}{\partial\xi^i},$$

so that the distance moved when only $\xi^i$ changes by $d\xi^i$ is
$h_i\,d\xi^i$ (no sum) ([Riley et al. (2006)](/sources/riley-2006.md),
§10.10, p. 364). The general displacement is
$d\mathbf x=\sum_i h_i\,d\xi^i\,\hat{\mathbf a}_i$ (eq. (10.57)).
[Arfken et al. (2013)](/sources/arfken-2013.md) give the same definitions,
$h_i^2=\sum_k(\partial x^k/\partial\xi^i)^2$, $\partial\mathbf x/\partial\xi^i=h_i\hat{\mathbf a}_i$,
$d\mathbf x=\sum_ih_i\,d\xi^i\,\hat{\mathbf a}_i$ (eqs. (3.131)–(3.133),
p. 184; the printed (3.131) repeats the $y$ term for the $z$ term, a
misprint), and note that $h_i$ "may be position-dependent and must have the
dimension needed to cause $h_i\,d\xi^i$ to be a length" (p. 184).

**Orthogonal systems only.** When the $\hat{\mathbf a}_i$ are mutually
perpendicular (§10.10, eq. (10.58), pp. 365–366):

$$(ds)^2=h_1^2(d\xi^1)^2+h_2^2(d\xi^2)^2+h_3^2(d\xi^3)^2,\qquad dV=h_1h_2h_3\,d\xi^1d\xi^2d\xi^3,$$

(Arfken et al., eqs. (3.130), (3.136), pp. 184–185) the
[metric tensor](/definitions/metric-tensor.md) is diagonal,
$g_{ij}=h_i^2\delta_{ij}$, $g^{ij}=h_i^{-2}\delta_{ij}$, and
$g=h_1^2h_2^2h_3^2$ (§26.15, p. 957; §26.20, p. 972; Arfken et al.,
p. 225 and exercise 4.3.2, where also $\lvert\mathbf a^i\rvert=1/h_i$). The
scale factors also convert integrals: $\int_C\mathbf v\cdot d\mathbf x=\sum_i\int_C\hat v_ih_i\,d\xi^i$
and $\int_S\mathbf v\cdot d\mathbf S=\int\hat v_1h_2h_3\,d\xi^2d\xi^3+\int\hat v_2h_3h_1\,d\xi^3d\xi^1+\int\hat v_3h_1h_2\,d\xi^1d\xi^2$
(Arfken et al., eqs. (3.134)–(3.135), pp. 184–185). In two dimensions the
Jacobian of an orthogonal system is $h_1h_2$ (exercise 4.4.2, p. 231). For a non-orthogonal
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
| orthogonal flux $(\Psi,\vartheta,\varphi)$ | $1/(RB_{\mathrm p})$ | $\sqrt{(\partial_\vartheta R)^2+(\partial_\vartheta z)^2}$ | $R$ |

(§10.10, p. 365; Arfken et al., eqs. (3.145), (3.153), pp. 188, 191; the
last row from [Seto et al. (2023)](/sources/seto-2023.md), eqs. (1)–(3),
p. 2, with $\Psi$ the poloidal flux per radian, so that $h_\Psi=1/\lvert\nabla\Psi\rvert$
and $h_1h_2h_3=h_\vartheta/B_{\mathrm p}$ is their Jacobian $\sqrt g$, p. 9;
see [magnetic flux coordinates](/definitions/magnetic-flux-coordinates.md).)

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §§10.9–10.10, pp. 358–369; §26.15, p. 957; §26.20, p. 972.
* [Arfken et al. (2013)](/sources/arfken-2013.md), §3.10, pp. 184–191; §4.3, p. 225; exercises 4.3.2, 4.4.2, pp. 226, 231.
* [Seto et al. (2023)](/sources/seto-2023.md), §2, p. 2; §5.1, p. 9.

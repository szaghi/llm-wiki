---
type: Definition
title: "Field-aligned coordinates"
description: "Computational coordinates ξ^1 = Ψ − Ψ_0, ξ^2 = ϑ, ξ^3 = φ − χ(Ψ,ϑ) obtained from magnetic flux coordinates by shifting the toroidal angle along the field lines, so that B = ∇ξ^3×∇ξ^1 = a_2/J and the parallel derivative is ∂_2 alone; the price is a non-orthogonal metric that carries the integrated shear I and a twist-shift periodicity condition in ξ^2."
status: established
aliases: [magnetic-field-aligned coordinates, Clebsch coordinates, flux-tube coordinates, twist-shift boundary condition, twist-shift condition, flute-ordering approximation]
tags: [curvilinear-coordinates, field-aligned-coordinates, metric, plasma-geometry, finite-difference]
timestamp: 2026-10-16T00:00:00Z
---

# Field-aligned coordinates

## Definition

Starting from [magnetic flux coordinates](/definitions/magnetic-flux-coordinates.md)
$(\Psi,\vartheta,\varphi)$, the **field-aligned coordinates** are the
computational coordinates

$$\xi^1=\Psi-\Psi_0,\qquad \xi^2=\vartheta,\qquad \xi^3=\varphi-\chi(\Psi,\vartheta),\qquad \chi(\Psi,\vartheta)=\int_{\vartheta_0}^{\vartheta}q_{\mathrm{loc}}(\Psi,\vartheta')\,d\vartheta',$$

where $q_{\mathrm{loc}}=\mathbf B\cdot\nabla\varphi/\mathbf B\cdot\nabla\vartheta$
is the local field-line pitch
([Jiang et al. (2024)](/sources/jiang-2024.md), eqs. (13)–(15), p. 3;
[Seto et al. (2023)](/sources/seto-2023.md), eqs. (5)–(6), p. 3;
[Liu et al. (2024)](/sources/liu-2024.md), eq. (8), p. 3, who normalise
$\xi^1=(\Psi-\Psi_1)/\Delta\Psi$ over the radial extent of the domain, so that
$\xi^1\in[0,1]$). A field line is a curve $\xi^1=$ const, $\xi^3=$ const, and
$\xi^2$ runs along it. In straight-field-line coordinates
$q_{\mathrm{loc}}\to q(\Psi)$, $\chi\to q(\vartheta-\vartheta_0)$ and
$I\to q'(\vartheta-\vartheta_0)$ (Jiang et al., eqs. (23)–(25); Seto et al.,
p. 3).

The **integrated local shear** is $I(\Psi,\vartheta)=\partial\chi/\partial\Psi$
(Jiang et al., eq. (19); Seto et al., eq. (7)).

## Bases, field and Jacobian

The [contravariant and covariant bases](/definitions/covariant-and-contravariant-bases.md)
of the new system, in terms of those of the flux system (Jiang et al.,
eqs. (16)–(22), p. 3; Seto et al., eq. (7), p. 3):

$$\mathbf a^1=\nabla\Psi,\quad \mathbf a^2=\nabla\vartheta,\quad \mathbf a^3=\nabla\varphi-I\,\nabla\Psi-q_{\mathrm{loc}}\nabla\vartheta;\qquad \mathbf a_1=\mathbf a_\Psi+I\,\mathbf a_\varphi,\quad \mathbf a_2=\mathbf a_\vartheta+q_{\mathrm{loc}}\mathbf a_\varphi,\quad \mathbf a_3=\mathbf a_\varphi.$$

Reciprocity $\mathbf a_i\cdot\mathbf a^j=\delta^j_i$ holds term by term (e.g.
$\mathbf a_1\cdot\mathbf a^3=I-I=0$; compiler's check). Consequences:

* **The field is a coordinate direction.** $\mathbf B=\nabla\xi^3\times\nabla\xi^1$
  (Seto et al., p. 3), equivalently $\mathbf B=\mathbf a_2/J$ with $J$ the
  [Jacobian](/definitions/jacobian.md) (Jiang et al., eq. (39), p. 4). Hence
  $\hat{\mathbf b}=\mathbf a_2/\sqrt{g_{22}}$ (Seto et al., p. 15) and
  $$\nabla_\parallel\phi=\hat{\mathbf b}\cdot\nabla\phi=\frac{1}{JB}\frac{\partial\phi}{\partial\xi^2}$$
  (Jiang et al., eq. (40)): only derivatives along $\xi^2$ enter, "so that
  the number of grid points in the parallel direction can be reduced
  especially for high-$n$ modes" whose structure has $k_\parallel\ll k_\perp$
  (Seto et al., p. 3; Jiang et al., p. 3; Liu et al., p. 3).
* **The Jacobian is unchanged.** Both GMEC papers define
  $J=(\nabla\xi^1\times\nabla\xi^2\cdot\nabla\xi^3)^{-1}$ (Jiang et al.,
  Table I, p. 16; Liu et al., p. 3), the registry's $J$. The shift of
  $\varphi$ does not change the triple product: Seto et al. state
  $\mathbf a_\Psi\times\mathbf a_\vartheta\cdot\mathbf a_\varphi=\mathbf a_1\times\mathbf a_2\cdot\mathbf a_3$
  (p. 9), and Liu et al. obtain $J=\Delta\Psi\,(\nabla\Psi\times\nabla\vartheta\cdot\nabla\varphi)^{-1}$
  for their normalised $\xi^1$ (p. 5).
* **The radial derivative is sheared.** From $\mathbf a_1$,
  $\partial_1\phi=\partial_\Psi\phi+I\,\partial_\varphi\phi$ (Seto et al.,
  eq. (8), p. 3), and $\partial_2\phi=\partial_\vartheta\phi+q_{\mathrm{loc}}\partial_\varphi\phi$
  (eq. (A.18), p. 16). In straight-field-line coordinates $I$ grows linearly
  with $\vartheta-\vartheta_0$: a "secular poloidal cell deformation" that
  "degrades the numerical accuracy of radial derivatives" (Seto et al.,
  p. 3), the problem the [shifted metric](/methods/shifted-metric.md)
  removes.

## Metric

The [metric](/definitions/metric-tensor.md) of the field-aligned system is
non-orthogonal even when the parent flux system is orthogonal. From the
contravariant basis above (Jiang et al., eq. (27), p. 3):

$$g^{13}=\nabla\Psi\cdot\nabla\varphi-I\,\lvert\nabla\Psi\rvert^2-q_{\mathrm{loc}}\,\nabla\Psi\cdot\nabla\vartheta .$$

For axisymmetric straight-field-line (PEST) coordinates with
$\nabla\Psi\cdot\nabla\varphi=\nabla\vartheta\cdot\nabla\varphi=0$, $\vartheta_0=0$
and the normalised $\xi^1=(\Psi-\Psi_1)/\Delta\Psi$, Liu et al. (eq. (26),
p. 5) list all six components:

$$\begin{aligned}
g^{11}&=\frac{\lvert\nabla\Psi\rvert^2}{\Delta\Psi^2},\qquad g^{22}=\lvert\nabla\vartheta\rvert^2,\qquad g^{12}=\frac{\nabla\Psi\cdot\nabla\vartheta}{\Delta\Psi},\\
g^{33}&=q'^2\vartheta^2\lvert\nabla\Psi\rvert^2+q^2\lvert\nabla\vartheta\rvert^2+\lvert\nabla\varphi\rvert^2+2qq'\vartheta\,\nabla\Psi\cdot\nabla\vartheta,\\
g^{23}&=-q'\vartheta\,\nabla\Psi\cdot\nabla\vartheta-q\lvert\nabla\vartheta\rvert^2,\qquad g^{13}=-\frac{1}{\Delta\Psi}\left(q'\vartheta\lvert\nabla\Psi\rvert^2+q\,\nabla\Psi\cdot\nabla\vartheta\right),
\end{aligned}$$

and obtain the covariant components by inversion (their eq. (27); see the
[metric tensor](/definitions/metric-tensor.md) for the cofactor formula and a
normalisation remark). The terms in $q'\vartheta$ are the integrated shear: they
grow with the distance from $\vartheta_0$ and are discontinuous across the
$\xi^2$ boundary (below). Both GMEC papers precompute $J$, $g^{ij}$, $g_{ij}$
and their first derivatives (second derivatives of $B$) from the equilibrium
and store them (Jiang et al., Table I, p. 16; Liu et al., §II C, p. 3); the
metric is evaluated from the equilibrium representation, not by differencing
grid coordinates.

## Vector operators

With $\mathbf B=\mathbf a_2/J$ the operators of reduced MHD take compact
component forms (Jiang et al., eqs. (40)–(44), p. 4), consistent with the
general-coordinate [divergence](/definitions/divergence.md),
[curl](/definitions/curl.md) and [Laplacian](/definitions/laplacian.md) for
$J>0$ (compiler's check):

$$\hat{\mathbf b}\times\nabla\phi\cdot\nabla\psi=\frac{1}{J^2B}\,g_{2i}\,\varepsilon^{ijk}\,\partial_j\phi\,\partial_k\psi,\qquad \nabla\times(\phi\,\hat{\mathbf b})\cdot\nabla\psi=\frac1J\,\varepsilon^{ijk}\,\partial_i\psi\;\partial_j\!\left(\frac{\phi\,g_{2k}}{JB}\right).$$

The second is the general curl applied to the covariant components
$\phi\,\hat{\mathbf b}\cdot\mathbf a_k=\phi g_{2k}/(JB)$. Liu et al. use the same
form for the curl of $\hat{\mathbf b}$ in the guiding-centre equations
(p. 4). A misprinted prefactor in Jiang et al.'s curvature form, eq. (43), is
recorded on the [Source page](/sources/jiang-2024.md).

## Twist-shift periodicity

Field-aligned coordinates break the $2\pi$ periodicity in $\vartheta$: the
points $(\xi^1,\xi^2+2\pi,\xi^3)$ and $(\xi^1,\xi^2,\xi^3+2\pi q)$ are the same
point of space, because $\chi$ increases by $2\pi q$ over one poloidal turn.
Every field therefore satisfies the **twist-shift condition**

$$\phi(\xi^1,\xi^2+2\pi,\xi^3)=\phi(\xi^1,\xi^2,\xi^3+2\pi q)$$

(Jiang et al., eq. (26), p. 3), written equivalently
$\phi(\xi^1,\xi^2+2\pi,\xi^3-2\pi q)=\phi(\xi^1,\xi^2,\xi^3)$ by Seto et al.
(eq. (9), p. 3; with $\phi(\xi^1,\xi^2,\xi^3+2\pi/N)=\phi$ on a $1/N$ wedge).
Ghost points across the $\xi^2$ boundary are therefore interpolated in
$\xi^3$ from the other side (Jiang et al., p. 3; §IV C, p. 5). The condition
is a property of the coordinates only; the metric does not satisfy it,
because $I$ contains $\vartheta$ explicitly: at $\xi^2=0$ and $2\pi$ the
integrated shear is $0$ and $2\pi q'$, so $\mathbf a_1$ and $\partial_1$ jump
across the boundary, which "may cause the numerical instability at the $y$
boundary" (Jiang et al., p. 3). That instability and its cures are on the
[shifted metric](/methods/shifted-metric.md) page. Liu et al. state the
condition with the opposite sign of the shift (Contradictions, below).

Liu et al. contrast these global field-aligned coordinates, whose field lines
cover the whole flux surface, with flux-tube coordinates, in which "only one
magnetic field line is followed and the simulation is limited to a band
region" (p. 3, figs. 1–2).

## Transform to flux coordinates

Because $\xi^3=\varphi-\chi(\Psi,\vartheta)$ is a shift at fixed
$(\Psi,\vartheta)$, a toroidal Fourier mode $n_\varphi$ only changes phase:
Seto et al. (eqs. (10)–(11), p. 3) pass between the two systems by an FFT in
$\xi^3$ or $\varphi$ and the factor $e^{\mp\mathrm i n_\varphi\chi}$, using the
same grid points for the $(\Psi,\vartheta)$ and $(\xi^1,\xi^2)$ planes, which
axisymmetry permits. For a field independent of $\varphi$ ($n_\varphi=0$) the
two systems coincide, $\partial_2=\partial_\vartheta$ (Seto et al., p. 4,
from eq. (7)).

## Flute-ordering approximation in elliptic operators

The perpendicular operators $\nabla_\perp^2$ and $\nabla\cdot(\phi\nabla_\perp\psi)$
contain $\partial_2$ terms. All three sources drop them when inverting the
vorticity–potential relation, which turns a 3D elliptic problem into a 2D one
in $(\xi^1,\xi^3)$ (Jiang et al., eq. (41), p. 4, "$\partial_yh\to0$"; Liu
et al., p. 3, who estimate the dropped term "on the order of $k_\parallel/k_\perp$
as compared to the 2D terms") or, per toroidal mode, into a 1D radial problem
(Seto et al., eq. (17), p. 4). Seto et al. show its limits:

* it is "not valid for $n=0$ mode and may not be valid for low-$n$ modes"
  (p. 2); in the $n_\varphi=0$ case the 1D solver produces "a disruptive
  numerical noise along the equilibrium magnetic field line" (p. 4);
* inverting the full operator for each mode in the flux plane $(\Psi,\vartheta)$
  instead (eq. (19), p. 5; [BOUT++](/software/bout-plus-plus.md)), the
  ideal-ballooning growth rates of the two solvers differ by about 1% at
  $n_\varphi=20$ and about 36% at $n_\varphi=5$ (§4, p. 7, fig. 3), an error
  the authors relate to an $O(1/n_\varphi)$ correction;
* the flux-plane grid is not field-aligned, so it must resolve
  $m_\vartheta\sim n_\varphi q$ poloidally, which limits the 2D solver to low
  $n_\varphi$ (p. 5).

## Contradictions

* **Sign of the twist-shift.** [Jiang et al. (2024)](/sources/jiang-2024.md)
  (eq. (26), p. 3) give $\phi(\xi^1,\xi^2+2\pi,\xi^3)=\phi(\xi^1,\xi^2,\xi^3+2\pi q)$,
  and [Seto et al. (2023)](/sources/seto-2023.md) (eq. (9), p. 3) the
  equivalent $\phi(\xi^1,\xi^2+2\pi,\xi^3-2\pi q)=\phi(\xi^1,\xi^2,\xi^3)$.
  [Liu et al. (2024)](/sources/liu-2024.md) (eq. (9), p. 3) give
  $\phi(\xi^1,\xi^2+2\pi,\xi^3)=\phi(\xi^1,\xi^2,\xi^3-2\pi q)$, with the same
  definition $\xi^3=\varphi-\int_0^\vartheta q_{\mathrm{loc}}\,d\vartheta'$
  (eq. (8)). The two statements differ by the sign of the shift. *Compiler's
  check (hypothesis):* from the shared definition, the point
  $(\xi^2+2\pi,\xi^3)$ has toroidal angle $\xi^3+q(\vartheta+2\pi)$, which is
  the angle of $(\xi^2,\xi^3+2\pi q)$, so the definition implies the form of
  Jiang et al. and Seto et al. Open: neither source supersedes the other, and
  the check does not close the entry by itself.

# Citations

* [Jiang et al. (2024)](/sources/jiang-2024.md), §I, p. 1; §III A, p. 3; §IV A, p. 4; §IV C, p. 5; Table I, p. 16.
* [Liu et al. (2024)](/sources/liu-2024.md), §II B–C, p. 3; p. 4; §II D, p. 5.
* [Seto et al. (2023)](/sources/seto-2023.md), §1, p. 2; §2, p. 3; §3, pp. 4–5; §4, p. 7; p. 9; App. A, pp. 15–16.

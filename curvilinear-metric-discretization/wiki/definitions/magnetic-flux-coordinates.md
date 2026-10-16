---
type: Definition
title: "Magnetic flux coordinates"
description: "Curvilinear coordinates (Ψ, ϑ, φ) adapted to a magnetic field with nested flux surfaces: a flux-surface label Ψ with B·∇Ψ = 0, a poloidal angle ϑ and a toroidal angle φ; orthogonal variants make ∇Ψ normal to the other two directions, straight-field-line variants (Boozer, PEST) make the field-line pitch a flux function q(Ψ)."
status: established
aliases: [flux coordinates, flux-surface coordinates, toroidal flux coordinates, straight-field-line coordinates, Boozer coordinates, PEST coordinates, orthogonal flux-surface coordinates]
tags: [curvilinear-coordinates, flux-coordinates, metric, plasma-geometry]
timestamp: 2026-10-16T00:00:00Z
---

# Magnetic flux coordinates

**Magnetic flux coordinates** are a system of
[general curvilinear coordinates](/definitions/curvilinear-coordinates.md)
$(\Psi,\vartheta,\varphi)$ built on a magnetic field $\mathbf B$ whose field
lines lie on nested toroidal surfaces: $\Psi$ labels the surfaces
($\mathbf B\cdot\nabla\Psi=0$), and the poloidal angle $\vartheta$ and the
toroidal angle $\varphi$ run from $0$ to $2\pi$ on each surface. In the three
sources of this bundle that use them, $2\pi\Psi$ is the poloidal flux, or
$\Psi$ is that flux normalised to its edge value
([Jiang et al. (2024)](/sources/jiang-2024.md), §III A, p. 3;
[Liu et al. (2024)](/sources/liu-2024.md), §II B, p. 3;
[Seto et al. (2023)](/sources/seto-2023.md), §2, p. 2). The domain is a
torus: every field is periodic in $\vartheta$ and $\varphi$, and Seto et al.
also allow a $1/N$ toroidal wedge, $\phi(\Psi,\vartheta,\varphi+2\pi/N)=\phi$
(eq. (4), p. 3). The magnetic axis is a coordinate singularity, excluded from
the domain by Liu et al. ($\Psi\ge\Psi_1>0$, p. 3).

The local field-line pitch on a surface is
$q_{\mathrm{loc}}(\Psi,\vartheta)=\mathbf B\cdot\nabla\varphi/\mathbf B\cdot\nabla\vartheta$,
and its average over a poloidal turn is the safety factor,
$\oint q_{\mathrm{loc}}\,d\vartheta=2\pi q(\Psi)$ (Seto et al., eq. (6),
p. 3; Jiang et al., eq. (15), p. 3; Liu et al., p. 3).

## Variants

* **Orthogonal flux-surface coordinates** (Seto et al., eqs. (1)–(3),
  p. 2): $\vartheta$ is chosen so that $\nabla\vartheta\perp\nabla\Psi$, and
  $\varphi$ is the geometric toroidal angle, the azimuth of cylindrical polars
  $(R,\varphi,z)$. The [metric](/definitions/metric-tensor.md) is diagonal,
  with [scale factors](/definitions/scale-factors.md)
  $$h_\Psi^2=g_{\Psi\Psi}=\frac{1}{\lvert\nabla\Psi\rvert^2}=\frac{1}{B_{\mathrm p}^2R^2},\qquad h_\vartheta^2=\left(\frac{\partial R}{\partial\vartheta}\right)^2+\left(\frac{\partial z}{\partial\vartheta}\right)^2,\qquad h_\varphi^2=R^2,$$
  so that $\sqrt g=h_\vartheta/B_{\mathrm p}$ (eq. (38), p. 9), and the pitch
  is $q_{\mathrm{loc}}=B_{\mathrm t}h_\vartheta/(B_{\mathrm p}R)$
  (eq. (6)). The first identity requires $\lvert\nabla\Psi\rvert=RB_{\mathrm p}$,
  i.e. $\Psi$ the poloidal flux per radian. Seto et al. assume
  $B_{\mathrm p}>0$; BOUT++ handles the other sign through a sign factor in
  the radial label (pp. 2–3). Here $q_{\mathrm{loc}}$ depends on $\vartheta$.
* **Straight-field-line coordinates**: $\vartheta$ (and, in general,
  $\varphi$) are chosen so that the field lines are straight in the
  $(\vartheta,\varphi)$ plane, $q_{\mathrm{loc}}=q(\Psi)$ (Jiang et al.,
  eq. (23), p. 3; Liu et al., p. 3). Liu et al. write the field as
  $\mathbf B=\nabla\Psi\times\nabla(q\vartheta-\varphi)$ (p. 5). Two choices
  are used:
  * **PEST coordinates** (Liu et al., §II D, p. 5): the toroidal angle is the
    geometric one and $\vartheta$ is fixed by requiring the Jacobian of
    $(\Psi,\vartheta,\varphi)$ divided by $R^2$ to be a flux function; for a
    circular equilibrium they solve for $\vartheta$ to $O(\varepsilon^2)$ in
    the inverse aspect ratio (eq. (24)).
  * **Boozer coordinates** (Jiang et al., §III A, p. 3; App. C, pp. 16–17):
    the coordinates GMEC "usually" chooses "considering the particle
    equations"; the toroidal angle $\varphi_{\mathrm B}$ differs from the
    geometric one. Jiang et al. obtain them from VMEC's flux coordinates by
    the angle shifts $\vartheta_{\mathrm B}=\vartheta_{\mathrm V}+\lambda+p$,
    $\varphi_{\mathrm B}=\varphi+q\,p$ (in their symbols), with the
    covariant representation $\mathbf B=\delta\nabla\Psi+I_{\mathrm B}(\Psi)\nabla\vartheta_{\mathrm B}+g_{\mathrm B}(\Psi)\nabla\varphi_{\mathrm B}$
    and $JB^2=I_{\mathrm B}+g_{\mathrm B}q$ (eqs. (C7)–(C15)). These
    symbols are local to this paragraph; the registry does not carry them.

## Metric from the poloidal-plane mapping

For an axisymmetric system given by $R(\Psi,\vartheta)$, $z(\Psi,\vartheta)$
and the geometric $\varphi$, Liu et al. (eq. (28), p. 5) compute the
contravariant metric from the two in-plane derivatives,

$$\lvert\nabla\Psi\rvert^2=\frac{R^2}{J^2}\left(R_\vartheta^2+z_\vartheta^2\right),\qquad \lvert\nabla\vartheta\rvert^2=\frac{R^2}{J^2}\left(R_\Psi^2+z_\Psi^2\right),\qquad \nabla\Psi\cdot\nabla\vartheta=-\frac{R^2}{J^2}\left(R_\Psi R_\vartheta+z_\Psi z_\vartheta\right),\qquad \lvert\nabla\varphi\rvert^2=\frac{1}{R^2},$$

with $R_\Psi=\partial R/\partial\Psi$ and so on, and
$\lvert J\rvert=\lvert R_\Psi z_\vartheta-R_\vartheta z_\Psi\rvert R$. These
are the cross-product formula $\mathbf a^i=(\mathbf a_j\times\mathbf a_k)/J$
of the [covariant and contravariant bases](/definitions/covariant-and-contravariant-bases.md)
applied to $\mathbf a_\Psi=(R_\Psi,0,z_\Psi)$, $\mathbf a_\vartheta=(R_\vartheta,0,z_\vartheta)$,
$\mathbf a_\varphi=R\,\hat{\mathbf a}_\varphi$ (compiler's identification).
Liu et al. print the Jacobian with the sign of their ordering
$(R,z,\varphi)\to(\Psi,\vartheta,\varphi)$; the sign drops out of these
formulas.

## Use

Flux coordinates are the parent system from which
[field-aligned coordinates](/definitions/field-aligned-coordinates.md) are
built by shifting the toroidal angle along the field lines, and they are the
system in which the [shifted-metric](/methods/shifted-metric.md) and
quasi-ballooning constructions evaluate radial derivatives (Seto et al.,
p. 3). In both GMEC and BOUT++ the metric of the flux system is computed once
from an equilibrium code and stored, not differenced on the simulation grid
([GMEC](/software/gmec.md), [BOUT++](/software/bout-plus-plus.md)).

# Citations

* [Jiang et al. (2024)](/sources/jiang-2024.md), §III A, p. 3; App. C, pp. 16–17.
* [Liu et al. (2024)](/sources/liu-2024.md), §II B, p. 3; §II D, p. 5.
* [Seto et al. (2023)](/sources/seto-2023.md), §2, pp. 2–3; §5.1, eq. (38), p. 9.

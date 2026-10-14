---
type: Definition
title: "Green's function"
description: "Response G(r, r') of a linear operator to a unit point source, L G = delta(r - r'), obeying the problem's homogeneous boundary conditions, so that u = integral of G f solves L u = f; symmetry G(r,r') = conj G(r',r), the free-space fundamental solutions of the Laplacian in two and three dimensions, and the split G = G_0 + H."
status: established
aliases: [Green function, fundamental solution, free-space Green's function, point-source solution, isolated boundary conditions]
tags: [greens-function, poisson, operator-theory]
timestamp: 2026-10-13T00:00:00Z
---

# Green's function

**Definition.** For a linear operator $\mathcal L$ and homogeneous boundary
conditions on $\partial\Omega$, the Green's function solves
$$\mathcal L_{\mathbf r}G(\mathbf r,\mathbf r')=\delta(\mathbf r-\mathbf r'),\qquad\mathbf r'\in\Omega\quad\text{(eq. 21.77)},$$
with $\mathcal L$ acting on $\mathbf r$, and obeys the same boundary
conditions. It is the response to a unit point source at $\mathbf r'$, and
$$u(\mathbf r)=\int_\Omega G(\mathbf r,\mathbf r')f(\mathbf r')\,\mathrm dV(\mathbf r')\quad\text{(eq. 21.78)}$$
solves $\mathcal Lu=f$ under those conditions
([Riley et al. (2006)](/sources/riley-2006.md), §21.5.1, pp. 752–753; the
one-dimensional form is §17.5). Inhomogeneous boundary conditions are
handled either by a change of variable that moves them into the equation,
or directly by the [representation formula](/results/greens-representation-formula.md).

**Symmetry.** For Hermitian $\mathcal L$ the
[eigenfunction series](/methods/eigenfunction-expansion.md) gives
$G(\mathbf r,\mathbf r')=\overline{G(\mathbf r',\mathbf r)}$, a real $G$
being symmetric; the book states that this holds "irrespective of how it is
found" (p. 753).

## Fundamental solutions of the Laplacian

With $\nabla^2G_0=\delta(\mathbf r-\mathbf r')$ (registry sign convention):

* $d=3$, decaying at infinity:
  $$G_0(\mathbf r,\mathbf r')=-\frac{1}{4\pi\lvert\mathbf r-\mathbf r'\rvert}\quad\text{(eq. 21.90)},$$
  derived from spherical symmetry and the divergence theorem on a sphere
  about $\mathbf r'$. It is the full Green's function for the condition
  $u\to0$ as $\lvert\mathbf r\rvert\to\infty$ — the free-space (isolated)
  problem — and yields $u(\mathbf r')=-\frac{1}{4\pi}\int f(\mathbf r)\lvert\mathbf r-\mathbf r'\rvert^{-1}\,\mathrm dV(\mathbf r)$
  over all space, which for an electrostatic charge distribution is the
  familiar Coulomb potential (eq. 21.91, pp. 757–758).
* $d=2$:
  $$G_0(\mathbf r,\mathbf r')=\frac{1}{2\pi}\ln\lvert\mathbf r-\mathbf r'\rvert+\text{const}\quad\text{(eq. 21.93)};$$
  it cannot be made to vanish at infinity, so the constant is not
  necessarily zero (p. 758).

**Split.** A Green's function for a bounded region is sought as
$G=G_0+H$, $G_0$ carrying the singularity at $\mathbf r'$ and $H$ harmonic
($\nabla^2H=0$) in $\Omega$ and chosen to meet the boundary condition
(pp. 756–757). The [method of images](/methods/method-of-images.md)
constructs $H$ from sources outside $\Omega$.

The free-space Green's function as the kernel of a fast convolution solver
(FFT or multipole) is not treated in the source.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §17.5 (pp. 569–570),
  §21.5.1 (pp. 752–753), §21.5.3 (pp. 756–758).

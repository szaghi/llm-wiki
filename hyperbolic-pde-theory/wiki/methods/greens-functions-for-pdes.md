---
type: Method
title: "Green's functions for linear PDEs"
description: "Solve L u = psi by the response G to a unit point source: with homogeneous boundary conditions u is the integral of G times the source; Green's second theorem gives a representation formula carrying boundary data, which a Dirichlet Green's function (zero on the boundary) or a Neumann one (constant normal derivative, by the compatibility condition) reduces to known data; images build G for planes, spheres and discs."
status: established
aliases: [Green's function, Dirichlet Green's function, Neumann Green's function, method of images, Green's representation formula, Poisson integral]
tags: [greens-function, elliptic, boundary-conditions, method-of-images]
timestamp: 2026-10-14T00:00:00Z
---

# Green's functions for linear PDEs

For $\mathcal Lu = \psi$ in $\Omega$ with homogeneous boundary conditions,
the Green's function solves
$$\mathcal L\,G(\mathbf x,\mathbf x') = \delta(\mathbf x - \mathbf x'), \qquad \mathbf x' \in \Omega,$$
with $\mathcal L$ acting on $\mathbf x$ and $G$ obeying the same
homogeneous boundary conditions. Then
$u(\mathbf x) = \int G(\mathbf x,\mathbf x')\psi(\mathbf x')\,\mathrm dV(\mathbf x')$
([Riley et al. (2006)](/sources/riley-2006.md), eqs. 21.76–21.78,
pp. 751–753). $G$ is the response to a unit point source, as for ODEs
([Green's functions for linear ODEs](/methods/greens-functions-for-linear-odes.md)).
Time dependence is omitted but "can be generalised" (p. 752).

**Eigenfunction form.** If $\mathcal L$ is Hermitian, with real
eigenvalues $\lambda_n$ and eigenfunctions $\varphi_n$ satisfying the
homogeneous conditions,
$$G(\mathbf x,\mathbf x') = \sum_n \frac{\varphi_n(\mathbf x)\varphi_n^*(\mathbf x')}{\lambda_n}$$
(eq. 21.79, p. 753). Hence $G(\mathbf x,\mathbf x') = G^*(\mathbf x',\mathbf x)$,
symmetric when real. The argument is referred to Ch. 17 (not read). The
expansion silently needs $\lambda_n \ne 0$ (compiler's remark). The book
calls the approach cumbersome for PDEs and does not pursue it (p. 753).

## Representation formula (Poisson's equation)

For $\nabla^2u = \psi$, Green's second theorem with $u$ and $G$ (no
boundary condition yet imposed on $G$) gives
$$u(\mathbf x') = \int_\Omega G(\mathbf x,\mathbf x')\psi(\mathbf x)\,\mathrm dV(\mathbf x) + \oint_{\partial\Omega}\left[u\,\partial_nG - G\,\partial_nu\right]\mathrm dS(\mathbf x)$$
(eqs. 21.81–21.84, pp. 754–756). $\hat{\mathbf n}$ points out of
$\Omega$, which may be bounded by several disconnected surfaces, one of
them a sphere at infinity (p. 754). For
$\mathcal L = \nabla\cdot(\alpha\nabla) + c_0$ the surface term carries a
factor $\alpha$ (Exercise 21.28, p. 773, posed as an exercise).

* **Dirichlet problem**, $u = g$ on $\partial\Omega$: choose $G = 0$ on
  $\partial\Omega$. Then
  $u(\mathbf x') = \int_\Omega G\psi\,\mathrm dV + \oint_{\partial\Omega} g\,\partial_nG\,\mathrm dS$
  (eqs. 21.85–21.86, p. 756).
* **Neumann problem**, $\partial_nu = h$: a solution exists only if
  $\oint_{\partial\Omega}h\,\mathrm dS = \int_\Omega\psi\,\mathrm dV$
  (compatibility, eq. 21.105, p. 765). Since
  $\oint\partial_nG\,\mathrm dS = 1$, the condition $\partial_nG = 0$ is
  not allowed; the simplest choice is $\partial_nG = 1/|\partial\Omega|$,
  which gives
  $u(\mathbf x') = \int_\Omega G\psi\,\mathrm dV + \langle u\rangle_{\partial\Omega} - \oint_{\partial\Omega}Gh\,\mathrm dS$
  with $\langle u\rangle_{\partial\Omega}$ a free constant. The constant is
  absent when the boundary is at infinity and $u \to 0$ there (eq. 21.106,
  p. 766). [Arfken et al. (2013)](/sources/arfken-2013.md) state the same
  compatibility requirement for Laplace's equation in a sphere, as Gauss's
  law: the surface integral of the normal derivative measures the enclosed
  charge, so it must vanish (Example 9.4.4, pp. 428–429).

## Method of images

Write $G = E(\mathbf x - \mathbf x') + H$, with $E$ the [fundamental
solution](/definitions/fundamental-solution.md) and $H$ harmonic in
$\Omega$. Build $H$ from image sources $q_j\delta(\mathbf x - \mathbf x_j)$
placed outside $\Omega$, $G = E(\mathbf x - \mathbf x') + \sum_j q_jE(\mathbf x - \mathbf x_j)$,
and adjust positions and strengths until the boundary condition holds
(pp. 756–759). Plane boundaries act as mirrors. Curved ones need more work,
and in general the images are "very difficult" to find (p. 759).

* **Half-space** $z > 0$, Dirichlet: one image of strength $-1$ at the
  mirror point. The solution of $\nabla^2u = 0$ with $u = g$ on $z = 0$ is
  $u(\mathbf x') = \frac{z'}{2\pi}\iint g(x,y)\left[(x - x')^2 + (y - y')^2 + z'^2\right]^{-3/2}\mathrm dx\,\mathrm dy$
  (eqs. 21.94–21.95, pp. 759–760). A quarter-plane needs three images;
  a strip needs infinitely many (pp. 761–762).
* **Sphere** of radius $R_0$, exterior: image at $(R_0^2/|\mathbf x'|^2)\mathbf x'$,
  strength $-R_0/|\mathbf x'|$ (pp. 762–764). The same image point serves
  the interior.
* **Disc** $r \le R_0$, Dirichlet ($u = g(\phi)$ on the rim): image strength
  $-1$ plus a constant. This gives the Poisson integral
  $$u(r',\phi') = \frac{1}{2\pi}\int_0^{2\pi}\frac{(R_0^2 - r'^2)\,g(\phi)\,\mathrm d\phi}{R_0^2 + r'^2 - 2R_0r'\cos(\phi - \phi')}$$
  (eq. 21.104, p. 765). The Neumann version takes the image with strength
  $+1$, giving $\partial_nG = 1/(2\pi R_0)$ (pp. 766–767).

The [uniqueness theorem](/results/uniqueness-theorem-poisson.md) justifies
the method: any function meeting the equation and the data is the
solution (p. 706). Arfken et al. give the same justification with the
grounded plane and its mirror charge (§9.5, p. 434). Their
Green's-function chapter (Ch. 10) is not part of this ingestion, so the
representation formula and the image constructions above rest on Riley et
al. alone.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §21.5 (pp. 751–767),
  Exercise 21.28 (p. 773).
* [Arfken et al. (2013)](/sources/arfken-2013.md), Example 9.4.4
  (pp. 428–429), §9.5 (p. 434).

---
type: Result
title: "Green's representation formula"
description: "From Green's second theorem, u(r') = integral of G f over the volume plus the boundary integral of (u dG/dn - G du/dn); a Dirichlet Green's function (G = 0 on the boundary) or a Neumann Green's function (dG/dn = 1/|boundary area|) reduces it to data the problem prescribes."
status: established
aliases: [Green's second identity, Green's theorem, Dirichlet Green's function, Neumann Green's function, boundary integral representation]
tags: [greens-function, poisson, boundary-conditions]
timestamp: 2026-10-13T00:00:00Z
---

# Green's representation formula

**Statement.** Let $\nabla^2u=f$ in $\Omega$ and
$\nabla^2_{\mathbf r}G(\mathbf r,\mathbf r')=\delta(\mathbf r-\mathbf r')$
with $\mathbf r'\in\Omega$ and no boundary condition yet imposed on $G$.
Green's second theorem,
$\int_\Omega(\phi\nabla^2\psi-\psi\nabla^2\phi)\,\mathrm dV=\oint_{\partial\Omega}(\phi\nabla\psi-\psi\nabla\phi)\cdot\hat{\mathbf n}\,\mathrm dS$
(eq. 21.81, for any scalar functions $\phi$, $\psi$), with
$\phi=u$, $\psi=G$, gives
$$u(\mathbf r')=\int_\Omega G(\mathbf r,\mathbf r')f(\mathbf r)\,\mathrm dV(\mathbf r)+\oint_{\partial\Omega}\left[u(\mathbf r)\,\partial_nG(\mathbf r,\mathbf r')-G(\mathbf r,\mathbf r')\,\partial_nu(\mathbf r)\right]\mathrm dS(\mathbf r)$$
([Riley et al. (2006)](/sources/riley-2006.md), §21.5.2, eqs. 21.83–21.84,
pp. 755–756). The roles of $\mathbf r$ and $\mathbf r'$ may be exchanged,
using $G(\mathbf r,\mathbf r')=G(\mathbf r',\mathbf r)$ for real $G$. For
homogeneous conditions on $u$, giving $G$ the same condition removes the
surface integral and recovers the [Green's function](/definitions/greens-function.md)
solution. The book states the extension to other operators as exercise
21.28 (not read).

## Dirichlet problem (§21.5.3)

Choosing $G=0$ on $\partial\Omega$ (eq. 21.85) removes the unknown
$\partial_nu$:
$$u(\mathbf r')=\int_\Omega Gf\,\mathrm dV+\oint_{\partial\Omega}g_{\mathrm D}\,\partial_nG\,\mathrm dS\quad\text{(eq. 21.86)}.$$

## Neumann problem (§21.5.4)

$\partial_nG=0$ is not admissible, because the divergence theorem forces
$\oint\partial_nG\,\mathrm dS=\int\nabla^2G\,\mathrm dV=1$. The simplest
admissible choice is $\partial_nG=1/\lvert\partial\Omega\rvert$ on
$\partial\Omega$, which defines the Neumann Green's function and gives
$$u(\mathbf r')=\int_\Omega Gf\,\mathrm dV+\langle u\rangle_{\partial\Omega}-\oint_{\partial\Omega}G\,g_{\mathrm N}\,\mathrm dS\quad\text{(eq. 21.106)},$$
with the boundary mean $\langle u\rangle_{\partial\Omega}$ a freely
specifiable constant (pp. 765–766). For a region bounded by a surface at
infinity with $u\to0$ there, the mean term is not needed. The data must
satisfy the [Neumann consistency condition](/definitions/poisson-boundary-value-problem.md).

Explicit Dirichlet and Neumann Green's functions for half-spaces, spheres
and discs are on the [method of images](/methods/method-of-images.md)
page.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §21.5.2 (pp. 753–756),
  §21.5.3 (p. 756), §21.5.4 (pp. 765–766).

---
type: Method
title: "Method of images"
description: "Construction of Dirichlet and Neumann Green's functions for the Laplacian by adding fundamental solutions of image sources placed outside the region: mirror images for planes and lines, the inversion point R^2 r'/|r'|^2 for spheres and discs, and the resulting half-space and Poisson integral formulas."
status: established
aliases: [image charges, image sources, Kelvin inversion, Poisson integral formula, Poisson kernel]
tags: [greens-function, poisson, boundary-conditions]
timestamp: 2026-10-13T00:00:00Z
---

# Method of images

**Procedure** for a Dirichlet [Green's function](/definitions/greens-function.md)
([Riley et al. (2006)](/sources/riley-2006.md), §21.5.3, pp. 758–759):

1. Add image sources $\sum_m\alpha_m\delta(\mathbf r-\mathbf r_m)$ with all
   $\mathbf r_m$ outside $\Omega$.
2. Their fundamental solutions are harmonic in $\Omega$, so
   $G(\mathbf r,\mathbf r')=G_0(\mathbf r,\mathbf r')+\sum_m\alpha_mG_0(\mathbf r,\mathbf r_m)$
   still satisfies $\nabla^2G=\delta(\mathbf r-\mathbf r')$ in $\Omega$.
3. Choose $\mathbf r_m$, $\alpha_m$ so that $G=0$ on $\partial\Omega$.
4. Insert $G$ in the [representation formula](/results/greens-representation-formula.md).

Finding the images is "in general very difficult"; for plane (3D) or
straight (2D) boundaries they are mirror reflections of $\mathbf r'$.

## Cases worked in the source

| Region | Images | Result |
|---|---|---|
| half-space $z>0$, 3D | one, $\alpha_1=-1$ at the reflection of $\mathbf r'$ in $z=0$ (eq. 21.94) | $u(\mathbf r')=\frac{z'}{2\pi}\int\!\!\int\frac{g_{\mathrm D}(x,y)\,\mathrm dx\,\mathrm dy}{[(x-x')^2+(y-y')^2+z'^2]^{3/2}}$ for Laplace (p. 760) |
| half-plane $x>0$, 2D | one, $\alpha_1=-1$; additive constant zero | $G=\frac{1}{2\pi}(\ln\lvert\mathbf r-\mathbf r'\rvert-\ln\lvert\mathbf r-\mathbf r_1\rvert)$ (p. 761) |
| quarter-plane, 2D | three, alternating signs (fig. 21.13) | worked as a line-charge force problem (pp. 761–762) |
| strip, 2D | infinite series of images (stated, p. 762) | — |
| exterior of sphere radius $R$, 3D | one at $\mathbf r_1=(R^2/\lvert\mathbf r'\rvert^2)\mathbf r'$, $\alpha_1=-R/\lvert\mathbf r'\rvert$ | $G=-\frac{1}{4\pi\lvert\mathbf r-\mathbf r'\rvert}+\frac{R/\lvert\mathbf r'\rvert}{4\pi\lvert\mathbf r-\mathbf r_1\rvert}$; the interior case is the same with roles swapped (pp. 762–764) |
| disc $r\le R$, 2D, Dirichlet | one at the inverse point, $\alpha_1=-1$, plus a constant | eq. 21.101 and the Poisson integral below |
| disc $r\le R$, 2D, Neumann | one at the inverse point, $\alpha_1=+1$ | $\partial_nG=1/(2\pi R)$ on the circle; eq. 21.109 and the formula below |

The sphere construction rests on the identity
$\lvert\mathbf r-\mathbf r_1\rvert=(R/\lvert\mathbf r'\rvert)\lvert\mathbf r-\mathbf r'\rvert$
for $\lvert\mathbf r\rvert=R$ (eqs. 21.98–21.99); in 2D "it is usually
necessary to take the image strength as $-1$" and absorb the rest in the
additive constant (p. 764).

**Disc, Dirichlet** (eqs. 21.101–21.104):
$$G=\frac{1}{2\pi}\left(\ln\lvert\mathbf r-\mathbf r'\rvert-\ln\left\lvert\mathbf r-\frac{R^2}{\lvert\mathbf r'\rvert^2}\mathbf r'\right\rvert-\ln\frac{\lvert\mathbf r'\rvert}{R}\right),$$
$$u(r',\varphi')=\frac{1}{2\pi}\int_0^{2\pi}\frac{(R^2-r'^2)\,g_{\mathrm D}(\varphi)\,\mathrm d\varphi}{R^2+r'^2-2Rr'\cos(\varphi-\varphi')}$$
for Laplace's equation — the Poisson integral formula (name not used by the
book) (pp. 764–765).

**Disc, Neumann** (eqs. 21.107–21.109), with
$\int_0^{2\pi}g_{\mathrm N}\,\mathrm d\varphi=0$:
$$u(r',\varphi')=\langle u\rangle_{\partial\Omega}-\frac{R}{2\pi}\int_0^{2\pi}g_{\mathrm N}(\varphi)\ln\left[R^2+r'^2-2Rr'\cos(\varphi-\varphi')\right]\mathrm d\varphi$$
(pp. 766–767).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §21.5.3 (pp. 758–765),
  §21.5.4 (pp. 766–767).

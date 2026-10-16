---
type: Method
title: "Dommaschk potentials for the vacuum field"
description: "Analytic toroidal-harmonic solutions of Laplace's equation in cylindrical coordinates used to represent the stellarator coil field as ∇χ; the coefficients are fitted to a computed vacuum field by Fourier and Legendre projections on a cylinder, giving triangular linear systems, so that ∇·B = 0 holds to machine precision in JOREK3D."
status: established
aliases: [Dommaschk representation, Dommaschk harmonics]
tags: [stellarator, reduced-mhd, numerics]
timestamp: 2026-10-16T00:00:00Z
---

# Dommaschk potentials for the vacuum field

The [reduced MHD model for stellarators](/methods/stellarator-reduced-mhd.md)
needs the vacuum (coil) field as the gradient of a scalar potential,
$\mathbf B_{\rm vac}=\nabla\chi$. JOREK3D represents $\chi$ by Dommaschk
potentials (Dommaschk 1986): closed-form solutions of $\Delta\chi=0$ in
cylindrical coordinates. The coefficients are fitted to a vacuum field
computed by a coil code, and $\chi$ is then evaluated analytically at
every quadrature point ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md),
§III).

## Representation

With $R_0$ the toroidally averaged major radius of the vacuum magnetic
axis, $\hat R=R/R_0$ and $\hat Z=Z/R_0$ (page-local scaled coordinates),

$$\frac{\chi}{F_0}=\phi+\sum_{n,m}\Big[\big(a_{nm}\cos n\phi+b_{nm}\sin n\phi\big)D_{nm}(\hat R,\hat Z)+\big(c_{nm}\cos n\phi+d_{nm}\sin n\phi\big)N_{n,m-1}(\hat R,\hat Z)\Big],$$

$$\{D,N\}_{nm}(\hat R,\hat Z)=\sum_{k=0}^{\lfloor m/2\rfloor}\frac{\hat Z^{\,m-2k}}{(m-2k)!}\,C^{\{D,N\}}_{nk}(\hat R)$$

([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), Eqs. 13–15). The
radial functions $C^{D}_{nk}$, $C^{N}_{nk}$ are finite sums with
coefficients built from Gamma functions and harmonic-number sums (Eqs.
16–17). The first term, $F_0\phi$, is the tokamak toroidal field; in the
tokamak limit $\chi=F_0\phi$. Every harmonic satisfies $\Delta\chi_{nm}=0$
exactly, so the represented field is curl-free and divergence-free
analytically.

The functions satisfy simple conditions on the cylinder $\hat R=1$:

$$D_{nm}\big|_{\hat R=1}=\frac{\hat Z^m}{m!},\quad N_{nm}\big|_{\hat R=1}=0,\quad \partial_{\hat R}D_{nm}\big|_{\hat R=1}=0,\quad \partial_{\hat R}N_{nm}\big|_{\hat R=1}=\frac{\hat Z^m}{m!},$$

which decouple the fit (same section).

## Fitting procedure

The vacuum field is first computed on an $(R,Z,\phi)$ grid by a coil code
(EXTENDER_P in the source). Then, on the cylinder $\hat R=1$,
$|Z|\le Z_{\max}$ ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md),
§III, Eqs. 20–31):

1. $F_0$ is the toroidal average of $R_0B_\phi$ at $\hat R=1$, $\hat Z=0$.
2. The coefficients $a_{nm}$, $b_{nm}$ follow from $B_\phi$, the
   $c_{nm}$, $d_{nm}$ from $B_R$, and the $n=0$ coefficients $a_{0m}$
   from $B_Z$.
3. Projecting on $\cos n\phi$, $\sin n\phi$ and on Legendre polynomials in
   $Z/Z_{\max}$ gives upper-triangular linear systems, solved in Python and
   passed to JOREK as a Fortran namelist.

The fit error $\langle(\nabla\chi-\mathbf B_{\rm vac})^2/B_{\rm vac}^2\rangle$
for the Wendelstein 7-A field at $\beta=2.3\times10^{-3}\%$ is smallest,
about $5\times10^{-11}$, at 9 poloidal modes; more modes overfit (about
$10^{-7}$ at 12) (§III, Fig. 1).

## Why an analytic potential

* $\Delta\chi=0$ exactly, so $\nabla\cdot\mathbf B=0$ "to machine
  precision" in the reduced field $\nabla\chi+\nabla\psi_\chi\times\nabla\chi$
  ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §II; see
  [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).
* $\chi$ is smooth. Represented on the finite elements, which are only
  $G^1$, $\chi$ would make the advective terms of the vorticity equation
  discontinuous even after integration by parts; in the authors' experience
  such discontinuities reduce accuracy or cause numerical instabilities
  (§II; see [Bézier finite elements](/methods/bezier-finite-elements.md)).

The fitting procedure, not the potentials themselves, is the source's
contribution; its Python implementation is based on a BOUT++ version of the
potentials (§III).

# Citations

* [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — representation, fitting procedure, W7-A fit error, motivation.

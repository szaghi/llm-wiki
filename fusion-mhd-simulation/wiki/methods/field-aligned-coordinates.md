---
type: Method
title: "Field-aligned coordinates, twist-shift condition and shifted metric"
description: "Coordinates in which one coordinate follows the equilibrium field line, so that few points resolve the parallel direction; their twist-shift periodicity, the phase-shift Fourier transform to flux coordinates, the integrated-shear boundary instability, and its cures by numerical diffusion, Scott's shifted metric, quasi-ballooning coordinates and a simple shifted metric aligned with the toroidal angle."
status: established
aliases: [field-aligned coordinates, twist-shift boundary condition, shifted metric, simple shifted metric, quasi-ballooning coordinates, flux-tube coordinates]
tags: [finite-differences, numerics, ballooning]
timestamp: 2026-10-16T18:35:00Z
---

# Field-aligned coordinates, twist-shift condition and shifted metric

Instabilities and turbulence in a magnetized plasma have
$k_\parallel\ll k_\perp$. Coordinates in which one direction follows the
equilibrium field line need far fewer grid points along $\mathbf B$ than
toroidal coordinates ([Jiang et al. (2024)](/sources/jiang-2024.md), §III A;
[Liu et al. (2024)](/sources/liu-2024.md), §II B). The finite-difference codes
[BOUT++](/software/bout-plus-plus.md) and [GMEC](/software/gmec.md) store
their fields in such coordinates
([Seto et al. (2023)](/sources/seto-2023.md), §2;
[Jiang et al. (2024)](/sources/jiang-2024.md), §III).

## Definition

Start from axisymmetric flux coordinates $(\psi,\theta,\varphi_{\mathrm c})$:
$\psi$ a poloidal-flux label, $\theta$ a poloidal angle and
$\varphi_{\mathrm c}$ the toroidal angle of the system. BOUT++ uses
orthogonal coordinates with the geometric angle, $\varphi_{\mathrm c}=\phi$
([Seto et al. (2023)](/sources/seto-2023.md), Eqs. 1–4); GMEC uses
straight-field-line coordinates, usually Boozer in Part I and PEST in Part II,
with $\varphi_{\mathrm c}=\zeta$ or $\phi$
([Jiang et al. (2024)](/sources/jiang-2024.md), §III A;
[Liu et al. (2024)](/sources/liu-2024.md), Eq. 8). With the local field-line
pitch $\hat q(\psi,\theta)=\mathbf B\cdot\nabla\varphi_{\mathrm c}/\mathbf B\cdot\nabla\theta$,
whose poloidal average is the safety factor, $2\pi q=\oint\hat q\,\mathrm d\theta$,
the field-line phase is
$\alpha(\psi,\theta)=\int_{\theta_0}^{\theta}\hat q\,\mathrm d\theta'$ and
$$x=\psi-\psi_0,\qquad y=\theta,\qquad z=\varphi_{\mathrm c}-\alpha(\psi,\theta)$$
([Seto et al. (2023)](/sources/seto-2023.md), Eqs. 5–6;
[Jiang et al. (2024)](/sources/jiang-2024.md), Eqs. 13–15; GMEC Part II
normalizes $x=(\psi-\psi_1)/\Delta\psi$,
[Liu et al. (2024)](/sources/liu-2024.md), Eq. 8; the later BOUT++ ELM runs
take the reference angle $\theta_0=\pi$, the inboard midplane,
[Seto et al. (2024)](/sources/seto-2024.md), §II). In straight-field-line
coordinates $\hat q=q(\psi)$, $\alpha=q(\theta-\theta_0)$. Then
$\mathbf B\propto\mathbf e_y$ and $\partial_y=\partial_\parallel$ up to a metric
factor, $\mathbf b\cdot\nabla f=(\mathcal J_{xyz}B)^{-1}\partial_yf$ with
$\mathcal J_{xyz}$ the Jacobian ([Jiang et al. (2024)](/sources/jiang-2024.md),
Eqs. 39–40). The covariant basis is
$$\mathbf e_x=\mathbf e_\psi+\mathcal I\,\mathbf e_{\varphi},\qquad \mathbf e_y=\mathbf e_\theta+\hat q\,\mathbf e_{\varphi},\qquad \mathbf e_z=\mathbf e_{\varphi},\qquad \nabla z=\nabla\varphi_{\mathrm c}-\mathcal I\nabla\psi-\hat q\nabla\theta,$$
with the integrated local shear $\mathcal I=\partial\alpha/\partial\psi$
([Seto et al. (2023)](/sources/seto-2023.md), Eq. 7;
[Jiang et al. (2024)](/sources/jiang-2024.md), Eqs. 16–22). The radial
derivative at fixed $(y,z)$ is $\partial_x=\partial_\psi+\mathcal I\,\partial_{\varphi}$;
in straight-field-line coordinates $\mathcal I=q'(\psi)(\theta-\theta_0)$
grows secularly along $\theta$, which deforms the cells
([Seto et al. (2023)](/sources/seto-2023.md), Eq. 8).

**Twist-shift periodicity.** Following $\theta\to\theta+2\pi$ at a fixed
physical point lowers $z$ by $2\pi q$, so every field obeys
$$f(x,\,y+2\pi,\,z-2\pi q)=f(x,y,z)\quad\Longleftrightarrow\quad f(x,\,y+2\pi,\,z)=f(x,\,y,\,z+2\pi q)$$
([Seto et al. (2023)](/sources/seto-2023.md), Eq. 9, left form;
[Jiang et al. (2024)](/sources/jiang-2024.md), Eq. 26, right form), plus
periodicity in $z$ over the toroidal domain ($2\pi/N$ for a wedge of $1/N$ of
the torus). Ghost points in $y$ are interpolated from the other end of the
field line ([Jiang et al. (2024)](/sources/jiang-2024.md), §III A).

**Fourier transform between the two systems.** Because $z$ and
$\varphi_{\mathrm c}$ differ by a function of $(\psi,\theta)$ only, a toroidal
harmonic $n$ transforms by a phase factor:
$\hat f_n(\psi,\theta)=\hat f^{(z)}_n(x,y)\,e^{-in\alpha}$ and back with
$e^{+in\alpha}$; for an axisymmetric equilibrium the $(\psi,\theta)$ and
$(x,y)$ planes share grid points
([Seto et al. (2023)](/sources/seto-2023.md), Eqs. 10–11). The two systems
coincide only for $n=0$ (Eq. 7, §3.1).

**Global, not flux-tube.** In GMEC the field lines of the grid cover the
whole flux surface, unlike a flux-tube code, which follows one field line and
covers only a band of the surface
([Liu et al. (2024)](/sources/liu-2024.md), §II B, Fig. 2).

## The integrated-shear boundary instability

$\mathcal I$ contains $\theta$ explicitly and does not satisfy the
twist-shift condition: $\mathcal I=0$ at $y=0$ and $2\pi q'(\psi)$ at
$y=2\pi$, two points that are the same point in space, so $\mathbf e_x$ and
the radial derivative are discontinuous at the $y$ boundary
([Jiang et al. (2024)](/sources/jiang-2024.md), §III A). For an $n=20$ ideal
ballooning mode in plain field-aligned coordinates this produces a numerical
instability localized at the $y$ boundary, growing at
$\gamma=0.21\,v_A/R_0$ within about $50\,R_0/v_A$ (§VIII, Figs. 10–11). The
metric component containing $\mathcal I$ also increases numerical dissipation
at large $\theta$ (§III A, after Scott).

**Cures.**

1. **Numerical vorticity diffusion** $D\,\nabla\cdot\nabla_\perp\delta\varpi$.
   It suppresses the instability only for a normalized $D\ge5\times10^{-8}$,
   and then lowers the physical growth rate by 7%, to $0.081$ from $0.087\,v_A/R_0$
   ([Jiang et al. (2024)](/sources/jiang-2024.md), §VIII, Fig. 12). GMEC
   Part II uses this route, with $D_{\delta\varpi}=10^{-6}$ and a smoothing of
   the energetic-particle pressure, both found to "affect little" the growth
   rate and frequency ([Liu et al. (2024)](/sources/liu-2024.md), §II A,
   App. C, Fig. 21).
2. **Shifted metric (Scott 2001).** At each grid line $y_i$ define local
   coordinates $x'=x$, $y'=y$, $z'=z-\alpha_{\mathrm{sm},i}(x)$ with
   $$\alpha'_{\mathrm{sm},i}(x)=\frac{g^{xz}}{g^{xx}}\Big|_{y=y_i},\qquad g^{xz}=-\mathcal I\,g^{\psi\psi}-\hat q\,g^{\psi\theta}+g^{\psi\varphi},$$
   so that $g^{x'z'}=0$ and $\partial_{x'}\approx\partial_\psi$; the parallel
   difference then needs interpolation in $z$ between neighbouring $y_i$,
   done with 1D B-splines of arbitrary order during the ghost update
   ([Jiang et al. (2024)](/sources/jiang-2024.md), Eqs. 27–35, §IV F).
3. **Quasi-ballooning coordinates (BOUT++).** Fields are stored in $(x,y,z)$
   but derivatives are taken in the dual system with
   $\mathbf e_u=\mathbf e_x-\mathcal I\mathbf e_z=\mathbf e_\psi$,
   $\mathbf e_v=\mathbf e_y$, $\mathbf e_w=\mathbf e_z$ and
   $\nabla w=\nabla\phi-\hat q\nabla\theta$, which combines the shifted radial
   derivative (Dimits 1993) with the shifted metric: the metric contains no
   $\mathcal I$ and no operator mixes $\psi$- and $y$-derivatives
   ([Seto et al. (2023)](/sources/seto-2023.md), Eqs. 12–14, App. A.1).
4. **Simple shifted metric (new in GMEC).** The choice
   $\alpha'_{\mathrm{sm},i}(x)=-\mathcal I(x,y_i)$ makes the local $z'$ the
   toroidal angle itself, with $\partial_{x'}=\partial_\psi$ exactly but
   $g^{x'z'}\ne0$; it coincides with Scott's shifted metric only if
   $g^{\psi\theta}=g^{\psi\varphi}=g^{\theta\varphi}=0$
   ([Jiang et al. (2024)](/sources/jiang-2024.md), Eqs. 36–38). Field grid
   points then coincide with the toroidal grid of the particle pusher, so a
   particle-in-cell hybrid needs no field-to-particle interpolation (§III C).
   Both shifted metrics remove the instability and give
   $\gamma\approx0.087\,v_A/R_0$ (§VIII).

## Elliptic solves and resolution limits

In field-aligned coordinates the perpendicular Poisson (vorticity) problem
reduces to independent 2D problems in $(x,z)$ by dropping the $\nabla_\parallel$
terms, an error of order $k_\parallel/k_\perp$
([Liu et al. (2024)](/sources/liu-2024.md), §II B;
[Jiang et al. (2024)](/sources/jiang-2024.md), §IV), the flute ordering
whose failure at low $n$ motivates the
[hybrid 2D/1D field solver](/methods/hybrid-2d-1d-field-solver.md) of
[Seto et al. (2023)](/sources/seto-2023.md). A grid in $(\psi,\theta)$, not
field-aligned, must resolve the resonant poloidal harmonics $m\sim nq$; the
FFT-and-phase-shift transform requires equal numbers of parallel and
poloidal points (Seto et al. 2023, §3.2). GMEC Part II's explicit RK4 advance becomes unstable
for $\Delta t/\tau_A\ge0.04$ ([Liu et al. (2024)](/sources/liu-2024.md),
App. C). GMEC decomposes the domain in $y$ only, because the Poisson solve
couples $x$ and $z$ ([Jiang et al. (2024)](/sources/jiang-2024.md), §IV E).

## Qualifications

- **Sign of the twist-shift condition in GMEC Part II.**
  [Liu et al. (2024)](/sources/liu-2024.md) (Eq. 9) print
  $\delta\Phi(x,y+2\pi,z)=\delta\Phi(x,y,z-2\pi q)$ (potential written
  $\delta\phi$ there) with
  $z=\phi-\int_0^\theta\hat q\,\mathrm d\theta'$ (Eq. 8). Under that definition
  the condition follows with $z+2\pi q$, as in Part I (Eq. 26) and in Seto et
  al. (Eq. 9) (compiler's check on the rendered page 3; the paper may rely on an
  orientation convention it does not state).
- **Printed instability growth rates.** Fig. 10 of Jiang et al. gives
  $\gamma=0.21\,v_A/R_0$ for the boundary instability, while Fig. 12 at
  vanishing diffusion shows about $0.10$; the cases are not distinguished
  (reader's note).
- **Metric of the quasi-ballooning system.** Seto et al. print
  $g^{ww}=B^2/(R^2B_\phi^2)$ (Eq. A.12). From $\nabla w=\nabla\phi-\hat q\nabla\theta$,
  $g^{ww}=1/R^2+\hat q^2/h_\theta^2=B^2/(R^2|\mathbf B_{\mathrm{pol}}|^2)$
  with $h_\theta=|\partial_\theta\mathbf X|$; only this form reproduces their
  printed flux-surface coefficient (Eq. A.28), so $B_\phi$ in Eq. A.12 is a
  typo for $|\mathbf B_{\mathrm{pol}}|$ (reader's check). Eq. A.20 also drops
  the factor $\hat q$ in
  $\partial_y\partial_z=\partial_\theta\partial_\phi+\hat q\,\partial_\phi^2$,
  which Eq. A.21 uses correctly (reader's note).
- In Jiang et al. the text states that both shifted metrics "need
  interpolation in y direction" and also that the simple one is better
  "because interpolation is not needed"; the second statement concerns
  field-to-particle interpolation (§III C; reader's note).

# Citations

- [Seto et al. (2023)](/sources/seto-2023.md) — §2, §3.1–3.2, Eqs. 1–14, App. A.
- [Jiang et al. (2024)](/sources/jiang-2024.md) — §III–IV, §VIII, Eqs. 13–40, Figs. 10–12.
- [Liu et al. (2024)](/sources/liu-2024.md) — §II A–B, Eqs. 8–9, App. C.
- [Seto et al. (2024)](/sources/seto-2024.md) — §II.

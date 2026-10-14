---
type: Definition
title: "Spherical harmonics"
description: "The functions Y_l^m(theta,phi) proportional to P_l^m(cos theta) e^{i m phi}, normalized to be orthonormal on the unit sphere; both founding sources give the same functions (Condon–Shortley phase), the Laplace series, rotation closure within each l, and recurrences in l and m."
status: established
aliases: [Laplace series, surface harmonics, Condon-Shortley phase]
tags: [sphere, spherical-harmonics, orthonormal-basis, expansion]
timestamp: 2026-10-14T00:00:00Z
---

# Spherical harmonics

## Definition

For integers $\ell\ge0$ and $-\ell\le m\le\ell$,
$$Y_\ell^m(\theta,\phi)=\sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell-m)!}{(\ell+m)!}}\;P_\ell^m(\cos\theta)\,e^{im\phi},$$
with $P_\ell^m$ the [associated Legendre function](/definitions/associated-legendre-functions.md)
carrying the Condon–Shortley factor $(-1)^m$ (registry convention). They are
the angular solutions, finite on the polar axis, of Laplace's, Helmholtz's
and Schrödinger's equations separated in spherical polar coordinates
([Riley et al. (2006)](/sources/riley-2006.md), §18.3, eq. 18.45, p. 593;
[Arfken et al. (2013)](/sources/arfken-2013.md), §15.5, eq. 15.137, p. 757).

**The two books give the same functions.** Arfken et al. write the formula
above with their $P_\ell^m$, which includes $(-1)^m$; Riley et al. write
$Y_\ell^m=(-1)^m\sqrt{\cdots}\,P_\ell^m(\cos\theta)e^{im\phi}$ with their
$P_\ell^m$, which does not. Their tables agree term by term, e.g.
$Y_1^{\pm1}=\mp\sqrt{3/8\pi}\,\sin\theta\,e^{\pm i\phi}$ and
$Y_2^{\pm1}=\mp\sqrt{15/8\pi}\,\sin\theta\cos\theta\,e^{\pm i\phi}$
(Riley et al., p. 593; Arfken et al., Table 15.4, p. 760, which also gives
Cartesian forms through $\ell=3$). Arfken et al. name the sign convention
the Condon–Shortley phase; its effect is a sign alternation with $m$ among
the positive-$m$ harmonics (p. 758). Both books state
$Y_\ell^{-m}=(-1)^m\big(Y_\ell^m\big)^*$ (Riley et al., p. 593, from
eq. 18.33).

## Orthonormality and completeness

$$\int_0^{2\pi}\!\!\int_0^\pi\big(Y_\ell^m\big)^*\,Y_{\ell'}^{m'}\,\sin\theta\,d\theta\,d\phi=\delta_{\ell\ell'}\delta_{mm'}$$
(Riley et al., eq. 18.46, p. 594; Arfken et al., eq. 15.138, p. 757). A
function on the sphere has the **Laplace series**
$$f(\theta,\phi)=\sum_{\ell=0}^\infty\sum_{m=-\ell}^{\ell}c_{\ell m}\,Y_\ell^m(\theta,\phi),\qquad c_{\ell m}=\int\big(Y_\ell^m\big)^*f\,d\Omega$$
(Riley et al., eqs. 18.47–18.48, p. 594, for "any reasonable function";
Arfken et al., eqs. 15.144–15.145, p. 761, who state that the double series
converges uniformly for $f$ "with sufficient continuity properties" and
cite Hobson, ch. VII, for the proof). The closure relation
$\sum_{\ell m}Y_\ell^m(\Omega)\big(Y_\ell^m(\Omega')\big)^*=\delta(\Omega-\Omega')$
is derived by Riley et al. from the expansion (eq. 18.51, p. 594) as the
first step of the
[addition theorem](/results/spherical-harmonic-addition-theorem.md).

## Rotations and degeneracy

Under a rigid rotation of the axes, each $Y_\ell^m$ in the new coordinates
is a linear combination of the $2\ell+1$ old $Y_\ell^{m'}$ with the same
$\ell$: the space of fixed $\ell$ is closed under rotation, which is the
reason for the $(2\ell+1)$-fold degeneracy of spherically symmetric
eigenproblems (Arfken et al., eq. 15.147, p. 763, and Example 15.5.3 for
$\ell=1$; Riley et al., p. 595, inside the proof of the addition theorem).
Neither book gives the rotation coefficients in the chapters read; Arfken
et al. defer them to their chapter 16.

## Special values and recurrences

$Y_\ell^m(0,\phi)=\sqrt{(2\ell+1)/4\pi}\,\delta_{m0}$ and
$Y_\ell^m(\pi,\phi)=(-1)^\ell\sqrt{(2\ell+1)/4\pi}\,\delta_{m0}$
(Arfken et al., eqs. 15.148–15.149, p. 764). The recurrences (eqs.
15.150–15.151, p. 764)
$$\begin{aligned}
\cos\theta\,Y_\ell^m&=\Big[\tfrac{(\ell-m+1)(\ell+m+1)}{(2\ell+1)(2\ell+3)}\Big]^{1/2}Y_{\ell+1}^m+\Big[\tfrac{(\ell-m)(\ell+m)}{(2\ell-1)(2\ell+1)}\Big]^{1/2}Y_{\ell-1}^m,\\
e^{\pm i\phi}\sin\theta\,Y_\ell^m&=\mp\Big[\tfrac{(\ell\pm m+1)(\ell\pm m+2)}{(2\ell+1)(2\ell+3)}\Big]^{1/2}Y_{\ell+1}^{m\pm1}\pm\Big[\tfrac{(\ell\mp m)(\ell\mp m-1)}{(2\ell-1)(2\ell+1)}\Big]^{1/2}Y_{\ell-1}^{m\pm1}
\end{aligned}$$
give the integrals $\int(Y_{\ell'}^{m'})^*\cos\theta\,Y_\ell^m\,d\Omega$ in
closed form (eq. 15.152). Riley et al. set as an exercise the identity
$\sum_m|Y_\ell^m|^2=(2\ell+1)/4\pi$, verified for $\ell\le2$ and stated
"true for any $\ell$" (Exercise 18.1, pp. 640–641); it is the coincident-direction
case of the addition theorem.

## Real forms

Arfken et al. note that geophysical gravity fields use real, unnormalized
harmonics $P_\ell^m(\cos\theta)\cos m\phi$ and $P_\ell^m(\cos\theta)\sin m\phi$
after Morse and Feshbach, with satellite coefficients for the Earth, Moon and
Mars (Example 15.5.2, Table 15.5, p. 762), and give real normalized azimuthal
functions $\cos m\phi/\sqrt\pi$, $\sin|m|\phi/\sqrt\pi$ (eq. 15.133, p. 757).
Riley et al. write the angular solution as
$P_\ell^m(\cos\theta)(C\cos m\phi+D\sin m\phi)$ (p. 593).

# Citations

1. [Riley et al. (2006)](/sources/riley-2006.md), §18.3, eqs. 18.45–18.53, pp. 593–595; Exercise 18.1, pp. 640–641.
2. [Arfken et al. (2013)](/sources/arfken-2013.md), §15.5, eqs. 15.132–15.152, pp. 756–765; Table 15.4, p. 760.

---
type: Method
title: "Shifted metric"
description: "Local re-coordinatisation of field-aligned grids: on each grid plane ξ^2 = const the binormal coordinate is shifted, ξ̄^3 = ξ^3 − σ_k(ξ^1) on plane k, so that the radial derivative no longer carries the integrated shear; Scott's choice makes ḡ^13 = 0, the simple variant makes ξ̄^3 the toroidal angle, and the quasi-ballooning form of BOUT++ pairs it with a shifted radial derivative. It removes the instability that the metric discontinuity at the twist-shift boundary drives."
status: established
aliases: [shifted metric method, shifted metric procedure, simple shifted metric, quasi-ballooning coordinates, shifted radial derivative]
tags: [field-aligned-coordinates, metric, finite-difference, plasma-geometry, shifted-metric]
timestamp: 2026-10-16T00:00:00Z
---

# Shifted metric

## Problem

In [field-aligned coordinates](/definitions/field-aligned-coordinates.md)
$\xi^3=\varphi-\chi(\Psi,\vartheta)$, the radial base vector
$\mathbf a_1=\mathbf a_\Psi+I\,\mathbf a_\varphi$ and the metric component
$g^{13}$ carry the integrated shear $I=\partial\chi/\partial\Psi$, which in
straight-field-line coordinates grows as $q'(\vartheta-\vartheta_0)$. Two
defects follow:

* **Grid deformation.** The computational cells shear secularly away from
  $\vartheta_0$, which "degrades the numerical accuracy of radial derivatives"
  ([Seto et al. (2023)](/sources/seto-2023.md), eq. (8), p. 3), and the
  $I$-containing metric component "may also cause increased numerical
  dissipation at large $\theta$" ([Jiang et al. (2024)](/sources/jiang-2024.md),
  p. 3, reporting Scott 2001).
* **Boundary instability.** $I$ does not satisfy the twist-shift periodicity
  of the fields: at $\xi^2=0$ and $\xi^2=2\pi$, which are the same points of
  space, $I=0$ and $I=2\pi q'$, so the derivative $\partial_1$ is
  discontinuous across the $\xi^2$ boundary (Jiang et al., p. 3). Jiang et
  al. show the consequence in GMEC (§VIII, pp. 10–11, with figs. 10–12 on
  pp. 8–9): for an
  $n_\varphi=20$ ideal ballooning mode in plain field-aligned coordinates, a
  numerical instability localised at the $\xi^2$ boundary appears within about
  $50R_0/v_A$, with growth rate $0.21\,v_A/R_0$ against the physical
  $0.087\,v_A/R_0$. A vorticity diffusion $D\,\nabla\cdot\nabla_\perp$ stabilises
  it only for a normalised $D\ge5\times10^{-8}$, and at that threshold the
  growth rate is still 7% below the physical one (fig. 12).

## Scott's shifted metric

On every grid plane $\xi^2=\xi^2_{[k]}$ introduce local coordinates
(Jiang et al., eqs. (28)–(33), pp. 3–4)

$$\bar\xi^1=\xi^1,\qquad \bar\xi^2=\xi^2,\qquad \bar\xi^3=\xi^3-\sigma_{[k]}(\xi^1),\qquad \sigma_{[k]}'(\xi^1)=\left.\frac{g^{13}}{g^{11}}\right|_{\xi^2=\xi^2_{[k]}}=\left.\left(-I-q_{\mathrm{loc}}\frac{\nabla\Psi\cdot\nabla\vartheta}{\lvert\nabla\Psi\rvert^2}+\frac{\nabla\Psi\cdot\nabla\varphi}{\lvert\nabla\Psi\rvert^2}\right)\right|_{\xi^2=\xi^2_{[k]}}.$$

Since $\nabla\bar\xi^3=\nabla\xi^3-\sigma_{[k]}'\nabla\xi^1$, the shifted metric has
$\bar g^{13}=g^{13}-\sigma_{[k]}'g^{11}=0$ on that plane. The shifted
binormal coordinate is the toroidal angle minus a small radial integral,
$\bar\xi^3=\varphi-\int^{\xi^1}M\,d\xi^1$ with
$M=-q_{\mathrm{loc}}\nabla\Psi\cdot\nabla\vartheta/\lvert\nabla\Psi\rvert^2+\nabla\Psi\cdot\nabla\varphi/\lvert\nabla\Psi\rvert^2$,
"usually small" because both ratios are (in the source's words) of order
$\epsilon$, a small parameter it does not define (eqs. (30)–(31)), so that
$\partial_{\bar 1}=\partial_\Psi+M\partial_\varphi\approx\partial_\Psi$ is
continuous (eqs. (32)–(33)). The price is in the parallel direction: the
neighbours $\xi^2_{[k+\ell]}$ of a stencil live in differently shifted
coordinates, so a parallel difference needs their values interpolated in
$\xi^3$,

$$\partial_2\phi\approx\frac{1}{\Delta\xi^2}\sum_\ell\mathcal C_\ell\,\phi_{[k+\ell]}\!\left(\bar\xi^1,\bar\xi^2_{[k]}+\ell\Delta\xi^2,\bar\xi^3+\sigma_{[k]}-\sigma_{[k+\ell]}\right)$$

(eqs. (34)–(35), (46), pp. 4, 6); GMEC uses 1D B-splines of arbitrary order
along $\xi^3$ at every $(\xi^1_{[i]},\xi^2_{[j]})$, computed during the ghost
update (§IV F, p. 6). With the shifted metric the $\xi^2$ boundary becomes
plainly periodic, without interpolation (§IV C, p. 5).

## Simple shifted metric (Jiang et al.)

Jiang et al. (§III C, eqs. (36)–(38), p. 4) choose instead
$\sigma_{[k]}'=-I(\xi^1,\xi^2_{[k]})$, which gives $\bar\xi^3=\varphi$ exactly,
$M=0$ and $\partial_{\bar 1}=\partial_\Psi$: the derivative is continuous as
in Scott's method, but $\bar g^{13}\ne0$. Its point is that the shifted grid
coincides with the grid of the toroidal flux coordinates, so a particle code
coupled to the field solver "advanced in the toroidal flux coordinates using
the same grids without interpolation from field grids to particles grids"
(p. 4). Both shifted metrics remove the boundary instability and give the same
growth rate, $0.087\,v_A/R_0$, with $D=0$ (§VIII, p. 11). Jiang et al. state
that the two coincide "only if the toroidal coordinates is orthogonal that
$g^{\psi\theta}=0$, $g^{\psi\xi}=0$ and $g^{\theta\xi}=0$" (eq. (38)).
*Compiler's remark (hypothesis):* from the formula for $\sigma_{[k]}'$ above,
$\nabla\Psi\cdot\nabla\vartheta=\nabla\Psi\cdot\nabla\varphi=0$ suffices;
$\nabla\vartheta\cdot\nabla\varphi$ does not enter.

## Quasi-ballooning coordinates (BOUT++)

Seto et al. (§2, eqs. (12)–(14), pp. 3–4) describe the dual system BOUT++
uses for derivatives, which combines the shifted radial derivative (Dimits
1993) with the shifted metric (Scott 2001). Fields are stored in field-aligned
coordinates, but derivatives use the bases

$$\mathbf a_1-I\,\mathbf a_3=\mathbf a_\Psi,\quad \mathbf a_2,\quad \mathbf a_3;\qquad \nabla\Psi,\quad \nabla\vartheta,\quad \mathbf a^3+I\,\mathbf a^1=\nabla\varphi-q_{\mathrm{loc}}\nabla\vartheta,$$

whose metric contains no $I$, and "there are no mixed derivatives including
both $\psi$-derivatives and $y$-derivatives in differential operators due to
the use of orthogonal flux surface coordinate system" (p. 3). A vector keeps
its first two contravariant components and has third component
$v^3+Iv^1$ on the new basis (eq. (14)). In this system the perpendicular
Laplacian becomes a sum of $\partial_\Psi$, $\partial_2$ and $\partial_3$
terms with $I$-free coefficients built from $\sqrt g$, $g^{\Psi\Psi}=\lvert\nabla\Psi\rvert^2$,
$g^{22}-1/g_{22}$, $g^{23}$ and $g^{33}$ (eqs. (A.2)–(A.12), pp. 14–15; see
[Laplacian](/definitions/laplacian.md)). Seto et al. record that BOUT++
v4.4.2 still takes derivatives in this system although it stores fields in
flux-surface coordinates (footnote 1, p. 2).

## Alternative without shifting

[Liu et al. (2024)](/sources/liu-2024.md) do not use the shifted metric in
GMEC's gyrokinetic version: they suppress the field-aligned instability with a
vorticity diffusion $D_{\delta\varpi}\nabla_\perp^2$ of normalised size
$10^{-6}$, chosen small enough "such that they affect little the physical
growth rate and real frequency" (§II A, p. 2), and they show that frequency
and growth rate hardly change as the coefficient is reduced (App. C, p. 12,
fig. 21). This is a qualification of Jiang et al.'s 7% bias, not a
contradiction: the problems (an $n_\varphi=3$ TAE against an $n_\varphi=20$
ballooning mode) and the normalisations differ, and neither source tests the
other's case.

# Citations

* [Jiang et al. (2024)](/sources/jiang-2024.md), §III A–C, pp. 3–4; §IV C, p. 5; §IV F, p. 6; figs. 10–12, pp. 8–9; §VIII, pp. 10–11.
* [Liu et al. (2024)](/sources/liu-2024.md), §II A, p. 2; App. C, p. 12.
* [Seto et al. (2023)](/sources/seto-2023.md), §1, p. 2; §2, pp. 3–4; App. A.1, pp. 14–15.

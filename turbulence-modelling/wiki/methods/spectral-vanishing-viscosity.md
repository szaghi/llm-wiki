---
type: Method
title: "Spectral vanishing viscosity"
description: "Implicit spectral vanishing viscosity boosts the modified wavenumber of the viscous-term discretization near the mesh cutoff, giving a scale-selective hyperviscous dissipation with one parameter; it serves as an implicit LES model that beats Smagorinsky on the Taylor–Green vortex and pipe flow but misses the spectral plateau."
status: established
aliases: [SVV, implicit SVV, ISVV, implicit spectral vanishing viscosity, spectral viscosity]
tags: [les, implicit-les, numerical-dissipation, sgs-model]
timestamp: 2026-10-25T13:42:00Z
---

# Spectral vanishing viscosity

**Spectral vanishing viscosity (SVV)** adds a viscosity that is zero at
large scales and grows near the mesh cutoff $k_c$. In the **implicit** form
used by [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md)
(§5.1), after Lamballais et al. and Dairay et al. (as recalled), no term is
added to the equations. Instead, the coefficients of the sixth-order
compact second-derivative scheme of the viscous term are chosen so that its
modified square wavenumber $k''_i(k_i)$ (page-local) exceeds $k_i^2$ near
$k_c$ while the scheme keeps sixth-order accuracy. The resulting
one-dimensional spectral viscosity is (Eq. 30)

$$\frac{\nu''(k_i)}{\nu}=\frac{k''_i(k_i)}{k_i^2}-1 ,$$

which vanishes for $k_i\ll k_c$ because $k''_i\approx k_i^2$ there. Its
main parameter is $\nu_0=\nu''(k_c)$ (page-local), quoted as $\nu_0/\nu$
and constant in space; the sharpness of the kernel is set by imposing its
value at $k=2k_c/3$. The dissipation is hyperviscous and linear, and comes
only from the discrete differentiation, which is why the authors classify
it as [implicit LES](/definitions/implicit-les.md).

## Choosing $\nu_0$

Following Dairay et al. (as recalled), $\nu_0$ is set by a Pao-like spectral
closure (§5.2, Eqs. 31–36). Pao's equilibrium $T(k)=\varepsilon(k)$ is
written with the modified wavenumber, a Pao-type ODE is integrated for the
kernel, and $\nu_0$ is chosen so that the LES spectrum at $k_c$ equals the
DNS spectrum at the DNS-mesh cutoff $k_d$. Vicente Cruz & Lamballais (§5.3,
Eqs. 37–42) show that the three-dimensional $k''=\sum_jk''_j$ depends on
the wavevector, not only on $|\boldsymbol k|$: it is largest along the mesh
axes and smallest along the diagonals (Fig. 1, $\nu_0/\nu=100$). Using the
shell average $\langle k''\rangle(k)$ instead of the one-dimensional kernel
roughly doubles the predicted value: $\nu_0/\nu=181$ and 700 for
$k_d/k_c=10$ and 25, against 92 and 355 from the isotropic version. The
authors argue that the anisotropy of the dissipation is an asset, because
convective differentiation errors are also largest along the axes. In the
simulations, kinetic energy and SVV anisotropies are anticorrelated, so the
effective viscosity is below the shell-average estimate for $k\gtrsim k_c/2$
(§6.4).

## Results

On the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at
$Re=40\,000$ (DNS $5400^3$; LES $216^3$ and $540^3$), §6.4:

- SVV damps the spectrum for $k_c/2\lesssim k\lesssim k_c$, prevents the
  thermalization of no-model LES, reduces the spectral error for
  $k\lesssim k_c/2$ compared with Smagorinsky and captures the dissipation
  peak of the breakdown (Figs. 13–14);
- at fixed filter scale, runs with $\Delta=\Delta x$ and $\Delta=2.5\Delta x$
  are "virtually identical" (data not shown), so SVV LES is numerically
  converged at standard resolution, unlike [Smagorinsky](/methods/smagorinsky-model.md);
- its effective filter is approximated by the super-Gaussian
  $\exp(-k^6\Delta^6/256)$, with a bump peaking near $k_c/4$: a
  **bottleneck**, i.e. a soft pile-up below $k_c/2$ that the authors call
  the main drawback of the method (Fig. 15, Eq. 50);
- its [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md)
  reproduces the a priori cusp but vanishes at low $k$, where the a priori
  plateau carries up to 24% of the dissipation (Figs. 16–18).

Adding Smagorinsky ($C_s=0.1$ or 0.18) to SVV restores a plateau and
reduces ($C_s=0.1$) or removes ($C_s=0.18$) the bottleneck, but does not
improve the total dissipation. As $C_s$ goes from 0.18 to 0, SVV takes over
the missing explicit dissipation automatically (§6.5, Figs. 20–22).

In turbulent pipe flow on a Cartesian mesh with an immersed boundary,
$\nu_0/\nu=234$ at $\Delta x^+=\Delta y^+\approx9$ gives $u_\tau$ within
1.8% at $Re_\tau=1000$ and about 1.9% at $Re_\tau=2000$, with realistic
mean and normal-stress profiles. The authors argue that, because $\nu_0$
is constant and scale-selective, the near-wall large scales are unaffected
without any wall correction, and call this an "augmented wall-resolving"
property.
At $\Delta x^+=18$ ($\nu_0/\nu=756$) $u_\tau$ is underpredicted by more
than 12%, so SVV "cannot be used alone in the context of WMLES"
(§7.2–7.4).

## Related constructions

- [Flad & Gassner (2017)](/sources/flad-2017.md) (App. C) build a modal
  cusp eddy viscosity in DG polynomial space, acting through a high-pass
  filter on the gradients: like SVV it is concentrated at the highest
  resolved modes.
- [Beck & Kurz (2023)](/sources/beck-2023.md) (§III B) relate their
  element-wise quadratic Smagorinsky coefficient (RL-Quad) to spectral
  vanishing viscosity, but defined in physical rather than wavenumber
  space.

## Qualifications

- Vicente Cruz & Lamballais (2023) print Eq. (38) without the shell factor
  $4\pi k^2$ in the numerator and Eq. (39) without the factor $\nu$ of
  Eq. (37) *(compiler check, not in the sources)*. Their Fig. 16 legend
  cites Eq. (40) where the caption and text cite Eq. (42).
- The SVV values for the two Taylor–Green resolutions are given in §5.3 and
  not restated in §6.

# Citations

- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §5.1, Eq. (30); §5.2, Eqs. (31)–(36); §5.3, Eqs. (37)–(42), Figs. 1–2; §6.4, Eq. (50), Figs. 13–18; §6.5, Figs. 20–22; §7.2–7.4, Figs. 25–28.
- [Flad & Gassner (2017)](/sources/flad-2017.md) — App. C.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §III B.

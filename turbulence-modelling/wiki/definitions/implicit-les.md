---
type: Definition
title: "Implicit large-eddy simulation"
description: "Implicit LES drops the explicit subgrid model and lets the discretization's own dissipation and filtering act as the closure; the sources use the term in at least three senses and report where it works, where it fails, and what it misses."
status: established
aliases: [ILES, iLES, implicitly filtered LES, no-model LES, under-resolved DNS, URDNS, MILES]
tags: [les, implicit-les, numerical-dissipation, sgs-model, dg]
timestamp: 2026-10-25T13:42:00Z
---

# Implicit large-eddy simulation

**Implicit LES (ILES)** solves the unfiltered Navier–Stokes equations on a
mesh too coarse to resolve the dissipative scales, with no explicit
subgrid-scale term: the [numerical dissipation](/properties/numerical-dissipation.md)
and the truncation of the discretization play the role of
$-\partial_j\tau_{ij}$ in the [filtered equations](/definitions/large-eddy-simulation.md).
In the form of [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md)
(§2.1, Eqs. 8–9), the LES equation with closure operator
$M_i=-\partial_j\tau_{ij}$ becomes formally identical to the Navier–Stokes
equation when $M_i$ is dropped, and the filter is whatever the numerics
apply. The sources agree on this core but use the name for different
things, and they disagree on how much of the subgrid physics the numerics
can carry.

## Three usages

1. **No-model LES.** The discretization is used as is and its truncation
   error is the only closure. [Dzanic et al. (2022)](/sources/dzanic-2022.md)
   (§1) equate ILES with under-resolved DNS (URDNS); [Lozano-Durán et al.
   (2022)](/sources/lozanoduran-2022.md) (App. B) run channel WMLES "without
   an explicit SGS model, i.e., the numerical truncation errors act as the
   SGS model". [Flad & Gassner (2017)](/sources/flad-2017.md) (§1, §3.1)
   describe the standard DG practice: no model, polynomial de-aliasing for
   stability, and the interface Riemann solver as the only source of
   subgrid dissipation.
2. **Designed numerical regularization.** The numerical dissipation is
   built to act as a model. Vicente Cruz & Lamballais (2023, §5.1) use the
   [implicit spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md),
   a viscous-term discretization tuned to dissipate near the mesh cutoff;
   [Beck & Kurz (2023)](/sources/beck-2023.md) (§III C, §V) distinguish
   such "true" implicit modelling from "no-model LES" (NoMo) and
   reinterpret the per-element blending factor $\alpha$ of a hybrid
   [DG/finite-volume subcell scheme](/methods/subcell-finite-volume-shock-capturing.md)
   as an implicit SGS model whose value a reinforcement-learning policy
   chooses (RL-Blend); [Haering et al. (2022)](/sources/haering-2022.md)
   (App. C) use an upwinding weight driven by a subgrid cell Reynolds
   number (iSGET) as the energy-transfer part of a hybrid model; MILES is
   recalled as the origin of the idea by Vicente Cruz & Lamballais (2023,
   §1) and Beck & Kurz (2023, §III C).
3. **Implicitly filtered LES.** The filter is the one induced by grid and
   discrete operator, whatever closure is added. Beck & Kurz (2023, §I)
   use the term in this sense: the filter width and shape are
   inhomogeneous, possibly nonlinear and unknown a priori, and the closure
   must be [discretization-consistent](/definitions/discretization-consistent-closure.md).
   [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) (§1) define
   implicit LES even more broadly, as any LES that uses the DNS equations
   in their original form with a closure added "regardless of whether the
   filter is known explicitly or not".
   [Krais et al. (2021)](/sources/krais-2021.md) (§2.2.3) state that LES in
   FLEXI uses implicitly filtered equations, with the implicit closure
   through the numerical flux recommended for well-resolved LES and
   explicit eddy-viscosity models available.

Usages 1 and 2 concern the closure (none, or numerical); usage 3 concerns
the filter. A page or claim about "ILES" should say which.

## What the closure terms are

Beck & Kurz (2023, §I, Eqs. 2–5) split the unclosed terms of implicitly
filtered LES into a commutation error, the classical subfilter term and a
discretization term (the "computational subgrid stress"). For
$\Delta\approx h$ the third can exceed the second, and for nonlinear schemes
it cannot be computed a priori. In this view ILES is the limit in which the
explicit closure is zero and the discretization term is the whole model.
The trained RL-Quad Smagorinsky coefficient of Beck & Kurz (§V B, Fig. 11)
peaks at the DG element centre and vanishes at the faces, which the authors
read as compensating the face-concentrated DG dissipation (an
interpretation they flag as needing further work).

## Evidence: when it works

- **High-order DG with enough resolution.** Flad & Gassner (2017, §1,
  Fig. 1a) obtain excellent spectra for decaying homogeneous isotropic
  turbulence (DHIT, $Re_\lambda$ from about 162 to 97) with DG ILES at
  $144^3$ degrees of freedom ($18^3$ elements, $N=7$), where about 43% of
  the dissipation is resolved at a 3-points-per-wavelength cutoff.
  Krais et al. (2021, §7.1) run a wall-resolved ILES of a NACA 64418
  airfoil at $Re_c=10^6$, $M=0.2$ with split-form DG and the Pirozzoli
  kinetic-energy-preserving flux ($N=7$, about 117 million degrees of
  freedom per variable); $C_p$ agrees with XFoil except near the suction-side
  trailing edge, where the LES separates (XFoil is the only reference).
- **Low order DG.** In forced HIT at $Re_\lambda\approx180$ with 24 or 36
  degrees of freedom per direction, NoMo is the best baseline for $N=3$,
  better than static and dynamic Smagorinsky and not reached by the RL
  models; its reward falls as $N$ grows to 5 and 8 (Beck & Kurz 2023, §V A,
  Fig. 8).
- **Designed SVV.** Implicit SVV beats constant-coefficient Smagorinsky in
  Taylor–Green-vortex spectra and dissipation at $Re=40\,000$ and is
  numerically converged at standard resolution (Vicente Cruz & Lamballais
  2023, §6.4). In pipe flow at $Re_\tau=1000$ with
  $\Delta x^+=\Delta y^+\approx9$ it predicts $u_\tau$ within 1.8%, against
  +9.6% for Smagorinsky with van Driest damping and +15.3% for no model
  (§7.2–7.4); the authors call this an "augmented wall-resolving" property.

## Evidence: when it fails

- **Applicability plateau.** At $48^3$ degrees of freedom ($6^3$ elements,
  $N=7$), where only about 0.9% of the dissipation is resolved, DG ILES
  piles energy up at mid wavenumbers and drops sharply near the cutoff;
  changing the Riemann solver (Roe, Lax–Friedrichs, low-dissipation Roe) or
  adding a Smagorinsky or small–small VMS model on top does not help.
  Flad & Gassner (2017, §1) conclude that roughly 40% of the total
  dissipation must be resolved for de-aliased upwind DG ILES to work, a
  threshold inferred from two resolutions of one case. The remedy they
  propose is a dissipation-free [kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
  split-form baseline plus an explicit [Smagorinsky model](/methods/smagorinsky-model.md)
  (§4).
- **Missing plateau of the spectral eddy viscosity.** The a priori
  [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md) of the
  Taylor–Green vortex has a nonzero low-wavenumber plateau (about 12, 2 and
  0.2 times $\nu$ at the three LES resolutions), which carries up to 24%,
  16% and 6% of the total dissipation through scales below $k_c/4$; scale-
  selective ILES vanishes there. Vicente Cruz & Lamballais (2023, §6.4,
  Figs. 16–18) call this "a fundamental limitation of any implicit LES",
  "making somewhat inconsistent the concept of implicit LES except when the
  mesh is close to DNS". Flad & Gassner (2017, §3.1) give the same
  explanation for the DG failure: interface dissipation is concentrated at
  the highest wavenumbers and lacks the Kraichnan plateau.
- **Bottleneck.** The scale-selective SVV dissipation produces a soft
  pile-up below $k_c/2$, a spurious defiltering that Vicente Cruz &
  Lamballais (2023, §6.4) call the main drawback of their implicit model;
  adding Smagorinsky ($C_s=0.18$) removes it but does not improve the total
  dissipation (§6.5).
- **No dissipation at all.** With kinetic-energy-conserving convection,
  no-model LES thermalizes towards a $k^2$ equipartition spectrum and,
  during the Taylor–Green breakdown, dramatically overestimates the total
  dissipation (Vicente Cruz & Lamballais 2023, §6.2); Flad & Gassner (2017,
  §3, Fig. 4) obtain the same $k^2$ spectrum from the dissipation-free
  split-form DG at $48^3$, stable but without a model. Agrawal et al. (2022,
  §VII.C) see $k^2$ equipartition in a no-model run of HIT at
  $Re_\lambda\to\infty$.
- **Aliasing.** On the periodic hill at $Re_b=10\,595$ with 64×64×32
  degrees of freedom, fourth-order URDNS shows large spurious oscillations
  in the $\langle v'v'\rangle$ and $\langle u'v'\rangle$ profiles that the
  authors attribute to aliasing, absent when the
  [PANS](/methods/partially-averaged-navier-stokes.md) eddy viscosity is
  added (Dzanic et al. 2022, §3.1, Fig. 5); the paper reports no
  de-aliased run.
- **Wall-modelled resolution.** Implicit SVV alone underestimates $u_\tau$
  by more than 12% at $Re_\tau=2000$ with $\Delta x^+=18$ (Vicente Cruz &
  Lamballais 2023, §7.4), so it "cannot be used alone in the context of
  WMLES".

## Flux reconstruction and PANS (inline)

Dzanic et al. (2022, §2.2–2.3) compare URDNS with
[partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
in the flux-reconstruction scheme of Huynh (PyFR), at equal degrees of
freedom with second-order ($\mathbb P_1$) and fourth-order ($\mathbb P_3$)
solution polynomials. Going to fourth order improves first-order statistics
of URDNS and PANS about equally, but second-order statistics (periodic hill)
and the shedding and Kelvin–Helmholtz spectral peaks of the circular
cylinder at $Re_D=3900$ (at $x/D=7$) much more for PANS than for URDNS
(§3.2, Figs. 11–13). The authors attribute the difference to the lower
numerical dissipation of the high-order scheme, which lets resolved small
scales respond to the model.

## Qualifications

- The plateau threshold of Flad & Gassner (2017) and the plateau-dissipation
  shares of Vicente Cruz & Lamballais (2023) come from one canonical flow
  each (DHIT, Taylor–Green vortex) and different schemes (DG, sixth-order
  compact differences); neither is a general bound.
- Krais et al. (2021) validate their ILES airfoil only against XFoil.
- Vicente Cruz & Lamballais (2023, §8) conclude that for
  $\Delta_{\mathrm{LES}}/\Delta x_{\mathrm{DNS}}\lesssim5$ the usefulness of
  explicit SGS modelling "cannot be evidenced", and invert the usual
  justification of ILES: explicit models such as Smagorinsky's "should be
  seen as an ersatz of regularization". Beck & Kurz (2023, §V A) reach a
  related conclusion from the other side: no reference model is best for
  all discretizations, so closure and discretization must be designed
  together.
- [Goc et al. (2021)](/sources/goc-2021.md) (§2.3), who run explicit SGS
  models, state that low-dissipation numerics are essential because
  numerical dissipation is "extremely detrimental" for coarse LES (Mittal &
  Moin 1997, as recalled): the opposite design choice to usage 2.

# Citations

- [Flad & Gassner (2017)](/sources/flad-2017.md) — §1, Figs. 1–3; §3, Fig. 4; §3.1; §4.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §I, Eqs. (2)–(5); §III C, Eq. (16); §V A–C, Figs. 8, 11–14.
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §1; §2.2–2.3; §3.1, Fig. 5; §3.2, Figs. 11–13.
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §2.1, Eqs. (8)–(9); §5.1; §6.2–6.5, Figs. 16–18; §7.2–7.4; §8.
- [Krais et al. (2021)](/sources/krais-2021.md) — §2.2.3; §7.1, Fig. 24.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §1.
- [Haering et al. (2022)](/sources/haering-2022.md) — §V D; App. C, Eqs. (C1)–(C2).
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — App. B.
- [Goc et al. (2021)](/sources/goc-2021.md) — §2.3 (low-dissipation numerics as a requirement of coarse LES).
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §VII.C, Fig. 6.

---
type: Definition
title: "Implicit large-eddy simulation (ILES)"
description: "Implicit LES adds no subgrid-scale term and lets the truncation error of the convective discretization act as the subgrid model; the page gives the definition, the Kolmogorov-scaling consistency test, the schemes the sources present as implicit models (adaptive TENO, ninth-order central dissipation, hybrid and multiphase schemes), and the case made against numerical dissipation as a subgrid model."
status: established
aliases: [ILES, implicit LES, under-resolved DNS, underresolved DNS, implicit subgrid-scale model, implicit subgrid regularization, MILES, monotone integrated LES]
tags: [turbulence, low-dissipation, numerical-dissipation, central-scheme, teno]
timestamp: 2026-11-17T08:43:53Z
---

# Implicit large-eddy simulation (ILES)

In **implicit LES** no subgrid-scale term is added to the equations: "the
discretization truncation error of the convective terms functions as a
subgrid-scale model" ([Fu et al. (2019d)](/sources/fu-2019-d.md), §V.F), and
the method is "also denoted as underresolved DNS, as no extra models are
involved" (same place). Explicit LES instead "employ[s] physically motivated
sub-grid scale (SGS) models by modifying the underlying conservation laws",
whose performance "strongly depends on the employment of a low-dissipation,
high-order scheme as the numerical truncation error, and the SGS model may
interact" (same place). In ILES the
[numerical dissipation](/definitions/numerical-dissipation.md) of the scheme
is therefore the model, and its distribution over wavenumbers
([approximate dispersion relation](/definitions/approximate-dispersion-relation.md))
decides whether it is a good one. The term classifies evidence: a scheme run
on a coarse turbulence grid without a model is being tested as an implicit
model, not as a DNS method. An older name, monotone-integrated LES (MILES,
printed "monotonic integrated LES"), is what
[Ducros et al. (1999)](/sources/ducros-1999.md) (§1) argue against (below).

## Consistency test

After the adaptive local deconvolution method (ALDM) of Hickel et al. and the
work of Schranner et al., as cited by [Fu et al. (2019d)](/sources/fu-2019-d.md)
(§V.F), "the physical consistency of the ILES method can be verified by
examining the performance in reproducing the Kolmogorov scaling of isotropic
turbulence decay for an infinite Reynolds number", the $k_w^{-5/3}$ inertial
range, for example in the inviscid
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) on a periodic grid
($k_w$ the wavenumber, page-local). TENO6-A on $64^3$ keeps the $-5/3$ range
"for almost all resolved wave numbers" at $t=10$ with a Roe flux, and up to
wavenumber 20 with a Rusanov flux, which is slightly more dissipative at high
wavenumbers; the scaling holds to $t=80$, "even at later times, this scaling is still
preserved (not shown here)", and no energy pile-up at high wavenumbers occurs (§V.F.1, Fig. 9). The paper
concludes that TENO6-A's "truncation error behaves physically consistently
for incompressible and compressible turbulence prediction" (§VI). The quantitative checks are the
kinetic-energy dissipation rate of the viscous Taylor–Green vortex at Re
100–3000 against DNS, and
[compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md)
statistics against filtered DNS (§§V.F.2, V.G). Fu (2023, §4.1) lists
Kolmogorov scaling for infinite-Re under-resolved turbulence among the design
constraints of adaptive TENO ([adaptive TENO](/methods/adaptive-teno.md)).

## Schemes presented as implicit models

- **Adaptive TENO.** On the viscous Taylor–Green vortex ALDM "fails to predict
  the kinetic energy dissipation rate between $t=8$ and $t=10$" at Re 400,
  where TENO6-A agrees with the DNS; at higher Re TENO6-A is better in the
  laminar phase ($t<4$) and "comparable to that of ALDM" overall
  ([Fu et al. (2019d)](/sources/fu-2019-d.md), §V.F.2, Fig. 10). On
  compressible isotropic turbulence (initial turbulent Mach number
  $M_{t,0}=0.6$, page-local; $64^3$ and $128^3$) TENO5-A
  and TENO6-A agree with filtered DNS and are comparable to localized
  artificial diffusivity (§V.G, §VI). [Fu (2023)](/sources/fu-2023.md) (§4.2)
  reports TENO8-A ahead of ALDM and the dynamic Smagorinsky model for the
  Taylor–Green dissipation rate on $64^3$.
- **Central scheme with high-order dissipation.**
  [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) (§3, §5) present
  the ninth-order Lerat–Corre dissipation of their central scheme, which acts
  only above $\vartheta\approx0.35\pi$, as an implicit subgrid regularization
  that converges to DNS under refinement. On the compressible Taylor–Green
  vortex they find no energy pile-up at $64^3$ and that the order of the
  dissipation matters more than that of the convective flux (§5.2;
  [artificial viscosity](/methods/artificial-viscosity.md)); on a Mach 2.25
  boundary layer their finer ILES is nearly identical to DNS, while one 64
  times coarser than DNS mispredicts transition (§5.3.1).
- **Hybrid schemes in wall turbulence.** In wall-resolved implicit LES of a
  Mach 2 boundary layer, [De Vanna et al. (2023a)](/sources/devanna-2023.md)
  (§4.2) find that upwind WENO and TENO schemes underestimate the friction,
  less so at higher order, while their sixth-order central
  kinetic-energy-preserving scheme fits the DNS
  ([supersonic turbulent boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md)).
- **Multiphase and jets.** [Jiao et al. (2024)](/sources/jiao-2024.md)
  (App. D, §4.6–4.8) build an implicit-LES variant of their multiphase scheme
  by blending central, MUSCL and THINC face values with a
  [Ducros sensor](/definitions/ducros-shock-sensor.md), and call a spray
  break-up run "under-resolved DNS" kept stable by inherent numerical
  dissipation. [Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md)
  (§8.3) run an implicit LES of a screeching Mach 1.35 jet with
  gradient-based schemes and WENO-Z. [Li et al. (2023b)](/sources/li-2023-b.md) (§4.7, §5)
  state that their optimized schemes provide "physically consistent
  dissipation and dispersion" for implicit LES. ALDM itself is an option of
  [JAX-Fluids](/software/jax-fluids.md) ([Bezgin et al. (2023)](/sources/bezgin-2023.md),
  §5.1.4: on $32^3$ ALDM agrees with DNS of decaying compressible turbulence,
  plain HLLC does not).
- **Selective filtering.** Bogey & Bailly (2004), as recalled by
  [Pirozzoli (2011a)](/sources/pirozzoli-2011.md) (§2.2), suggest using
  optimized explicit filters "to model the effects of the unresolved (subgrid)
  flow scales, replacing classical eddy-viscosity models".

## The case against numerical dissipation as the model

- [Ducros et al. (1999)](/sources/ducros-1999.md) (§1) recall encouraging
  results of the piecewise-parabolic method and MILES, but also studies in
  which numerical dissipation exceeds the subgrid dissipation, "may be due to
  the fact that classical shock-capturing schemes reduce to first order in
  the shock"; and "built-in numerical dissipation is unable to vanish in
  near-wall regions as SGS dissipation does, which can be seen as a major
  drawback of the MILES approach and may limit their applications to free
  shear flows". After Mittal & Moin, as recalled, an intrinsically dissipative
  shock-capturing scheme "may not be able to be generalized to the whole
  domain of calculation for LES", "even if such high-order schemes clearly
  exhibit some subgrid scale model behaviour".
- Their own test (§4.1, Figs. 1–3): second- and fourth-order
  Jameson–Schmidt–Turkel dissipation on inviscid decaying compressible
  turbulence "always brings a spurious dissipation, too large when the fourth
  order is employed and too weak when the second order alone is employed",
  and "is not able to mimic the dissipation of a true subgrid-scale model";
  with the second-order term and no model the spectrum settles to $k_w^2$
  equipartition ([numerical dissipation](/definitions/numerical-dissipation.md)).
  The dissipation orders are two and four, not the ninth order of
  Sciacovelli et al. or the adaptive dissipation of TENO-A, so these
  positions are opposed without testing the same scheme.
- [Pirozzoli (2011a)](/sources/pirozzoli-2011.md) (§2.1), after Park et al.
  (2004), as recalled: upwind dissipation "can be harmful for LES, for which
  proper resolution of marginally resolved wave numbers is crucial, as it may
  hamper the effect of subgrid-scale models".
- Inside a captured shock the distinction fades: Ducros et al. (§4.4,
  Fig. 24) find the numerical dissipation larger than the subgrid dissipation
  there even in their explicit LES, "leading to a weak influence of the
  subgrid scale modeling in such regions, at least for the numerical scheme
  used here" ([shock–turbulence interaction](/benchmarks/shock-turbulence-interaction.md)).

## Qualifications

- The consistency test is a statement about decaying, nearly incompressible
  turbulence at infinite Reynolds number; it says nothing about walls, where
  Ducros et al.'s objection applies, or about shocks.
- Fu et al. (2019d) take the test from Hickel et al. and Schranner et al.,
  which are not ingested; "physically consistent" is their word for passing
  it.
- The names are not used uniformly: Fu et al. equate ILES with under-resolved
  DNS; Jiao et al. use "iLES" for a sensor-blended scheme and "under-resolved
  DNS" for a run without a model; Ducros et al. use MILES for the approach
  they criticize. The page treats all three as the same practice: no explicit
  subgrid term.

# Citations

- [Fu et al. (2019d)](/sources/fu-2019-d.md) — §V.F (definition, explicit against implicit LES, consistency test), §V.F.1 (Fig. 9), §V.F.2 (Fig. 10), §V.G, §VI.
- [Ducros et al. (1999)](/sources/ducros-1999.md) — §1 (MILES critique); §4.1 (Figs. 1–3); §4.4 (Fig. 24).
- [Pirozzoli (2011a)](/sources/pirozzoli-2011.md) — §2.1–2.2: upwinding harmful for LES, selective filtering as a subgrid model (both as recalled).
- [Fu (2023)](/sources/fu-2023.md) — §4.1, §4.2: ILES design constraint of TENO-A, TENO8-A against ALDM and dynamic Smagorinsky.
- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — §3, §5.2, §5.3.1: ninth-order dissipation as implicit subgrid regularization (arXiv v1).
- [De Vanna et al. (2023a)](/sources/devanna-2023.md) — §4.2: wall-resolved implicit LES with upwind and central schemes.
- [Jiao et al. (2024)](/sources/jiao-2024.md) — App. D; §4.6–4.8: iLES variant, under-resolved DNS.
- [Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md) — §8.3: implicit LES of a screeching jet.
- [Li et al. (2023b)](/sources/li-2023-b.md) — §4.7, §5: physically consistent dissipation claimed for implicit LES.
- [Bezgin et al. (2023)](/sources/bezgin-2023.md) — §5.1.4, Fig. 12: ALDM in JAX-Fluids.

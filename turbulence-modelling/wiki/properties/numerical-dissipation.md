---
type: Property
title: "Numerical dissipation in scale-resolving simulation"
description: "Numerical dissipation is the kinetic-energy loss a discretization adds by itself; the sources show where in wavenumber and in the element it acts, that it competes with or replaces the subgrid model, and that both too much and too little of it degrade LES."
status: established
aliases: [artificial dissipation, scheme dissipation, upwind dissipation, Riemann-solver dissipation, numerical viscosity]
tags: [numerical-dissipation, implicit-les, les, dg, kinetic-energy-preserving]
timestamp: 2026-10-25T13:42:00Z
---

# Numerical dissipation in scale-resolving simulation

**Numerical dissipation** is the loss of resolved kinetic energy produced
by the discretization itself: upwind or Riemann-solver fluxes, interface
penalties, filters, limiters, hyperviscous derivative stencils and blended
low-order operators. In a scale-resolving simulation it acts on the same
scales as the [subgrid-scale model](/definitions/large-eddy-simulation.md).
It therefore either competes with the model or, in
[implicit LES](/definitions/implicit-les.md), replaces it. A
**low-dissipation** (kinetic-energy-preserving) discretization adds none
from the convective terms, so all dissipation comes from viscosity and the
model ([kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).

## Where it acts in wavenumber

- **Element methods with interface fluxes.** High-order element methods
  have very low dispersion errors over a broad range of scales and
  dissipation that is near zero for well-resolved scales and very high near
  the Nyquist cutoff. The interface dissipation thus acts like a
  high-frequency filter ([Flad & Gassner 2017](/sources/flad-2017.md),
  §1, §3.1, citing earlier DG studies). It is concentrated at the highest
  wavenumbers and lacks the low-wavenumber plateau of the Kraichnan
  [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md), which
  Flad & Gassner propose as the reason DG implicit LES fails when the cutoff
  lies in the inertial range.
- **Designed hyperviscosity.** The implicit
  [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
  of [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md)
  (§5.1, §5.3) puts the dissipation near $k_c$ by construction. It is
  strongly anisotropic, largest along the mesh axes and smallest along the
  diagonals; the authors argue that this is an asset, because the
  convective differentiation errors are also largest along the axes.
- **Discretization order at fixed degrees of freedom.** Going from a
  second- to a fourth-order flux-reconstruction scheme at equal degrees of
  freedom improves partially-averaged Navier–Stokes far more than
  under-resolved DNS. [Dzanic et al. (2022)](/sources/dzanic-2022.md)
  (§3.2, §4) attribute this to the lower numerical dissipation of the
  high-order scheme, which lets the small resolved scales respond to the
  model. At low order the shedding and Kelvin–Helmholtz peak frequencies of
  the cylinder at $Re_D=3900$ are overpredicted by about 10% and 6%
  (Fig. 11).

## Where it acts in the element

[Beck & Kurz (2023)](/sources/beck-2023.md) (§V A–C) contrast two DG-based
operators. DG dissipation enters only through the face fluxes, so it is
concentrated at element faces. The finite-volume subcell operator of the
hybrid [DG/FV scheme](/methods/subcell-finite-volume-shock-capturing.md),
whose subcells are sized by the LGL weights, dissipates most at the element
centre (Fig. 4; stated by the authors as an explanation, not tested). The no-model reward in forced HIT decreases as the degree $N$ grows from 3
to 8, which the authors relate to the localization of the numerical
dissipation at the element faces as $N$ grows. Pure DG ($\alpha=0$) is under-dissipative and pure FV ($\alpha=1$)
over-dissipative; an RL-chosen blend matches the DNS spectrum (Fig. 12). The
trained element-wise Smagorinsky coefficient peaks at the element centre and
vanishes at the faces, which the authors read as homogenizing the total
dissipation (Fig. 11).

## Interaction with the subgrid model

- **Detrimental excess.** [Goc et al. (2021)](/sources/goc-2021.md)
  (§2.3) state that low-dissipation discretization is essential and that
  numerical dissipation is "extremely detrimental" for coarse LES (Mittal &
  Moin 1997, as recalled); many unsteady solvers inherit dissipative RANS
  discretizations. Their aircraft LES use charLES, with entropy- and
  kinetic-energy-preserving fluxes, and Alya, with an energy-conserving
  Galerkin convective form and no upwinding. [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md)
  (§II.B) describe charLES as kinetic-energy conserving and approximately
  entropy preserving, "thereby limiting the amount of numerical
  dissipation".
- **Masking the model.** On de-aliased DG with Roe fluxes, adding
  Smagorinsky or VMS Smagorinsky does not improve coarse DHIT, which the
  authors attribute to the interaction of the artificial dissipation with
  the SGS viscosity. On a dissipation-free split-form baseline, which in
  their argument separates stability from model dissipation, Smagorinsky
  works (Flad & Gassner 2017, §1, §4). Of the three
  ways Flad & Gassner add small-scale damping (§5), only the low-dissipation
  L2Roe flux damps the pressure–dilatation oscillations left by the
  kinetic-energy-preserving scheme. It does so by scaling the interface
  velocity jump by the local Mach number, so that it dissipates density and
  pressure fluctuations without affecting the momentum dissipation. A BR2
  penalty reduces them somewhat, and the modal cusp viscosity leaves them
  unchanged (§5.1, Fig. 10).
- **Errors that look like a model.** With the Smagorinsky model at
  $\Delta x=\Delta$, differentiation errors dominate and the spectral eddy
  viscosity drops near the mesh cutoff, a numerical signature (Vicente Cruz
  & Lamballais 2023, §6.3). Numerical convergence needs $\Delta x=\Delta/5$.
  The authors propose the criterion that the effective transfer function at
  the mesh cutoff should be at most about 0.1.
- **Automatic compensation.** In a mixed Smagorinsky + SVV model, lowering
  $C_s$ from 0.18 to 0 shifts the dominant dissipation to the SVV term, which
  compensates the missing explicit dissipation; Vicente Cruz & Lamballais
  (2023, §6.5) relate this to the "convenient conspiracy" of Oran & Boris.
- **Uncounted dissipation.** The upwinding-based energy-transfer model iSGET
  of [Haering et al. (2022)](/sources/haering-2022.md) (App. C, §V D)
  works in their hybrid model, but its numerical dissipation is not counted
  in their resolution-adequacy parameter, an inconsistency the authors
  acknowledge.

## Too little dissipation

A scheme that conserves kinetic energy exactly and has no model does not
stay accurate:

- truncated-Euler and no-model runs thermalize towards a $k^2$
  equipartition spectrum. During the Taylor–Green breakdown the no-model LES
  overestimates the total dissipation: "a subdissipative operator leads
  eventually to an overdissipative behaviour" (Vicente Cruz & Lamballais
  2023, §6.2, Figs. 4–7);
- dissipation-free split-form DG is stable for severely under-resolved
  DHIT and gives a $k^2$ spectrum near the cutoff (Flad & Gassner 2017, §3,
  Fig. 4);
- high-order under-resolved DNS of the periodic hill shows spurious
  oscillations in second-order statistics, attributed by Dzanic et al.
  (2022, §3.1, Fig. 5) to aliasing and absent when an eddy viscosity is
  added;
- in the discretize-first LES of [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md)
  (§5.1.2, §5.2.4), the under-resolved second-order central scheme
  produces grainy high-wavenumber oscillations. The no-closure LES has too
  much energy at high wavenumbers; Smagorinsky corrects this, and the
  learned closure is trained to predict the oscillations as part of the
  discrete commutator error, instead of removing them by explicit
  filtering.

Polynomial de-aliasing (over-integration) and split forms are the two DG
remedies for aliasing. Flad & Gassner (2017, §3.1) find that with classic
Roe dissipation they give almost identical spectra. They conclude that the
failure of coarse DG ILES comes from the Riemann-solver dissipation, not
from the de-aliasing. [Krais et al. (2021)](/sources/krais-2021.md)
(§3.3) list both as stabilizations available in FLEXI. Split-form DG can be
made kinetic-energy-preserving or entropy-conserving by the choice of
two-point flux, with entropy-dissipative surface terms added.

## Qualifications

- The quantitative statements above come from canonical periodic flows
  (DHIT, forced HIT, Taylor–Green vortex), one bluff body (cylinder at
  $Re_D=3900$) and the periodic hill, each with one scheme family.
  [Duraisamy (2021)](/sources/duraisamy-2021.md) (§VII) states that
  disambiguating numerical from modelling errors in LES is hard, especially
  without explicit filtering, and recalls from Lund that even explicit
  filtering may not fully address it.

# Citations

- [Flad & Gassner (2017)](/sources/flad-2017.md) — §1; §3, Fig. 4; §3.1, Figs. 5–6; §4; §5, Figs. 8–9; §5.1, Fig. 10.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §V A–C, Figs. 4, 8, 11–12.
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §3.1, Fig. 5; §3.2, Fig. 11; §4.
- [Goc et al. (2021)](/sources/goc-2021.md) — §2.3.
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §5.1; §5.3, Fig. 1; §6.2–6.3; §6.5.
- [Krais et al. (2021)](/sources/krais-2021.md) — §3.3, Eqs. (52)–(54).
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §II.B.
- [Haering et al. (2022)](/sources/haering-2022.md) — §V D; App. C.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §5.1.2; §5.2.4.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §VII.

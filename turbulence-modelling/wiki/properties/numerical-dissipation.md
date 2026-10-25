---
type: Property
title: "Numerical dissipation in scale-resolving simulation"
description: "Numerical dissipation is the kinetic-energy loss a discretization adds by itself; the sources show where in wavenumber and in the element it acts, how it is measured, that it competes with or replaces the subgrid model, that grid-size changes alter it, and that both too much and too little of it degrade LES."
status: established
aliases: [artificial dissipation, scheme dissipation, upwind dissipation, Riemann-solver dissipation, numerical viscosity]
tags: [numerical-dissipation, implicit-les, les, dg, kinetic-energy-preserving]
timestamp: 2026-10-25T19:45:00Z
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

- **Filtered artificial viscosity versus Riemann-solver dissipation.**
  [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) (§5.2,
  Figs. 2–3) compare, by von Neumann (eigensolution) analysis of 1D
  advection–diffusion with DG at $N=7$ and an upwind flux, the dissipation
  of an artificial viscosity filtered by a modal
  [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
  kernel $(i/N)^{P}$ with that of the interface flux. The exponent $P$
  matters most at low wavenumbers, where the filtered viscosity supplies
  almost all the dissipation; at the other wavenumbers it is smaller than
  the Riemann-solver dissipation.

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

## Measuring it

- **Energy budget.** [Cao et al. (2022)](/sources/cao-2022.md) (§3.1,
  Fig. 5) estimate the numerical dissipation of a high-order gas-kinetic
  scheme in the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
  ($Re=1600$, $M_0=0.1$) as the residual of the volume-averaged
  kinetic-energy budget, with $E_k$ the volume-averaged kinetic energy per
  unit reference density and $\varepsilon_1$, $\varepsilon_2$,
  $\varepsilon_3$, $\varepsilon_{\mathrm{num}}$ page-local:
  $$\varepsilon_{\mathrm{num}}=-\frac{dE_k}{dt}-(\varepsilon_1+\varepsilon_2+\varepsilon_3),$$
  where $\varepsilon_1=\tfrac{2\mu}{\rho_0\lvert\Omega\rvert}\int_\Omega S^d_{ij}S^d_{ij}\,dV$
  is the solenoidal (deviatoric) part, $\varepsilon_2=\tfrac{\mu_b}{\rho_0\lvert\Omega\rvert}\int_\Omega(\nabla\cdot\boldsymbol u)^2dV$
  the bulk-viscosity part with the scheme's inherent bulk viscosity
  $\mu_b=\tfrac{2n}{3(n+3)}\mu$ ($n=2$ internal degrees of freedom for a
  diatomic gas, page-local), and $\varepsilon_3=-\tfrac1{\rho_0\lvert\Omega\rvert}\int_\Omega p\,\nabla\cdot\boldsymbol u\,dV$
  the pressure–dilatation. The resolved part is computed with sixth-order
  central differences. $\varepsilon_{\mathrm{num}}$ decreases with grid
  refinement from $128^3$ to $1024^3$ and is significant on the coarse
  grids, where $\varepsilon_1+\varepsilon_2+\varepsilon_3$ is well below the
  decay rate. The authors read the agreement of the decay rate with the
  reference as support for [implicit LES](/definitions/implicit-les.md).
- **Numerical Reynolds number.** [Seta & Federrath (2022)](/sources/seta-2022.md)
  (§2.4) take from earlier work (McKee et al. 2020, App. C) that the
  numerical Reynolds numbers of their finite-volume MHD code are
  approximately $2n_g^{4/3}$ for $n_g$ grid points per direction (about
  8000 at $n_g=512$), and choose explicit $Re=Rm=2000$ so that "the
  explicit diffusion is always significantly higher and at larger scales
  than the numerical diffusion".
- **Effective viscosity.** [Pereira et al. (2021)](/sources/pereira-2021.md)
  (§IV.3.1, Eqs. 22–23) include a numerical viscosity $\nu_n$ in the
  effective viscosity $\nu+\nu_t+\nu_n$ that sets an effective Reynolds
  number, but leave it out of their plots because it is not computed.

## Scheme design against excess dissipation

Several sources state how their scheme limits dissipation, without
measuring it:

- [Huang et al. (2022)](/sources/huang-2022.md) (§2.2) use for compressible
  boundary-layer DNS a seventh-order WENO scheme "optimized by means of
  limiters" to reduce numerical dissipation and, for the high-Reynolds
  Mach 2.5 case, an eighth-order split convective central scheme of
  Pirozzoli, "about twice as fast as the conventional WENO method".
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) (§3) combine an
  essentially non-oscillatory scheme near shocks with a centred scheme
  elsewhere, switched by a sensor based on dilatation, enstrophy and sound
  speed (no formula printed).
- Cao et al. (2022, §2.1, Remark 1) use linear WENO weights for smooth
  low-speed flows "to avoid the numerical dissipation from artificially
  created interface discontinuity", and WENO-Z with characteristic
  variables only for the compressible isotropic turbulence with shocklets.
- [Alauzet et al. (2022)](/sources/alauzet-2022.md) (§4.1.1) use a
  multi-slope MUSCL "β-scheme" that blends centred and upwind gradients for
  low dissipation, and note that the limiter choice "directly affects the
  numerical dissipation". In their RANS of NASA Rotor 37, globally refined
  structured meshes dissipate the induced tip vortex while adapted meshes
  keep it (Figs. 42–43), which they attribute to resolution.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) (§2) cite small
  dispersion and minimal dissipation as advantages of the spectral element
  code Nek5000; [Mozaffari et al. (2022)](/sources/mozaffari-2022.md)
  (§5.1) blend 20% second-order upwind into central convection for their
  delayed DES.
- [Basile et al. (2023)](/sources/basile-2023.md) (§1) state that pure
  p-adaptation of DG needs very high polynomial degrees, which can cause
  instabilities from aliasing "or too little numerical dissipation"; their
  DG uses a Roe flux with a Harten-type entropy fix (§2.1).
- In the stabilized finite-element LES of [Prakash et al. (2022)](/sources/prakash-2022.md)
  (§III.B.1), the authors state from experiments not shown that the
  SUPG/PSPG/grad-div stabilization dissipates "significantly" less than any
  of their explicit SGS models; their no-model run of forced isotropic
  turbulence at $\nu=10^{-12}$ piles energy up at the highest wavenumbers
  (Fig. 4).

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

## Grid-size changes

- **Refinement levels.** [Martin-Alvarez et al. (2022)](/sources/martinalvarez-2022.md)
  (§1, §2.1) argue that multi-level adaptive mesh refinement introduces
  numerical viscosity and resistivity at several scales, one per level, so
  that turbulent and magnetic energy is "dissipated significantly more than
  expected for the $\Delta x_{\max}$ employed" and small-scale structure is
  lost when gas moves to coarser levels. In cosmological zoom-in MHD with
  zero physical resistivity (RAMSES, constrained transport), their
  quasi-Eulerian refinement, which covers the galaxy with the finest level,
  gives faster [small-scale dynamo](/results/small-scale-dynamo.md) growth.
  Its growth rates "follow well" the reference scaling
  $\Gamma_E\propto Re^{1/2}\propto h_{\min}^{-1/2}$ drawn in Fig. 7 ($\Gamma_E$ the
  growth rate and $h_{\min}$ the finest cell size, as on the
  [small-scale dynamo](/results/small-scale-dynamo.md) page), the scaling for Kolmogorov turbulence with a
  numerical viscosity proportional to the cell size, whereas mass-based
  refinement follows about $h_{\min}^{-0.3}$ (§3.2, Fig. 7). They
  also state, citing other work, that constrained transport gives lower
  amplification than divergence cleaning because of "the high numerical
  diffusivity introduced by the numerical solver" (§1).
- **Resolution requirement.** With truncation-error dissipation, the
  critical Reynolds number of a turbulent dynamo becomes a grid requirement:
  [Liu et al. (2022)](/sources/liu-2022.md) (§1) estimate at least 30 pc
  for a 1 kpc thick galactic disc and about 3 pc for a 100 pc disc.
- **Fine-to-coarse interfaces.** Mozaffari et al. (2022, §1, Fig. 1, from an
  earlier thesis) show a detached-eddy simulation of decaying turbulence
  crossing a mesh-size doubling: the resolved kinetic energy drops at once,
  the modelled energy, whose dissipation term depends on the cell size,
  decays more slowly, and "the loss of resolved turbulence is never equal
  to the gain in modeled turbulence". They conclude that mesh-size changes
  should be avoided where possible, which motivates their averaged
  [mesh adaptation](/methods/mesh-adaptation.md). The mechanism they name is
  the cell-size-dependent dissipation term of the kinetic-energy equation
  of the [hybrid model](/definitions/hybrid-rans-les.md), which they call an
  "artificial dissipation term".

## Qualifications

- The quantitative statements above come from canonical periodic flows
  (DHIT, forced HIT, Taylor–Green vortex), one bluff body (cylinder at
  $Re_D=3900$) and the periodic hill, each with one scheme family. The
  astrophysical statements do not measure the numerical dissipation of
  their own runs: Martin-Alvarez et al. (2022) assume a numerical viscosity
  proportional to the cell size, Seta & Federrath (2022) take the numerical
  Reynolds number from earlier work, and Liu et al. (2022) give an
  order-of-magnitude estimate.
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
- [Cao et al. (2022)](/sources/cao-2022.md) — §2.1, Remark 1; §3.1, Fig. 5.
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §5.2, Figs. 2–3.
- [Seta & Federrath (2022)](/sources/seta-2022.md) — §2.4.
- [Pereira et al. (2021)](/sources/pereira-2021.md) — §IV.3.1, Eqs. (22)–(23).
- [Huang et al. (2022)](/sources/huang-2022.md) — §2.2.
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) — §3.
- [Alauzet et al. (2022)](/sources/alauzet-2022.md) — §4.1.1; Figs. 42–43.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §2.
- [Mozaffari et al. (2022)](/sources/mozaffari-2022.md) — §1, Fig. 1; §5.1.
- [Basile et al. (2023)](/sources/basile-2023.md) — §1; §2.1.
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §III.B.1, Fig. 4.
- [Martin-Alvarez et al. (2022)](/sources/martinalvarez-2022.md) — §1; §2.1; §3.2, Fig. 7.
- [Liu et al. (2022)](/sources/liu-2022.md) — §1.

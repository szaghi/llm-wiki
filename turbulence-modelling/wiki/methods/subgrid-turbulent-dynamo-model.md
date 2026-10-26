---
type: Method
title: "Subgrid turbulent dynamo model"
description: "A subgrid closure of the induction equation for cosmological MHD: an isotropic mean-field alpha effect whose coefficient is the subgrid turbulent velocity dispersion of a one-equation SGS kinetic-energy model, quenched when the magnetic energy reaches a tunable fraction q of the subgrid turbulent energy."
status: established
aliases: [subgrid dynamo, subgrid turbulent mean-field dynamo, alpha-effect subgrid dynamo, quenched alpha subgrid model]
tags: [sgs-model, dynamo, mhd, astrophysics, les]
timestamp: 2026-10-26T05:06:00Z
---

# Subgrid turbulent dynamo model

The **subgrid turbulent dynamo model** of [Liu et al. (2022)](/sources/liu-2022.md)
adds to the induction equation of a grid-resolved magnetic field an
electromotive force that represents the amplification by turbulent motions
the grid cannot resolve. The electromotive force is an isotropic
**$\alpha$ effect** of mean-field electrodynamics, and its coefficient is not
computed from the subgrid kinetic helicity but set equal to the subgrid
turbulent velocity dispersion supplied by a one-equation subgrid-scale
kinetic-energy model, multiplied by a quenching factor that switches the
term off once the magnetic energy reaches a fraction $q$ of the subgrid
turbulent kinetic energy (§2.2, Eq. 14). It is implemented in the
[RAMSES](/software/ramses.md) adaptive-mesh code and is meant to let
cosmological simulations of galaxy formation, which cannot resolve the
[small-scale dynamo](/results/small-scale-dynamo.md), grow realistic fields
from a weak seed.

Page-local notation: the overbar is the part of a field resolved by the grid
(the implicit grid filter of [LES](/definitions/large-eddy-simulation.md)),
the superscript $<$ the unresolved remainder (registry notation; the source
writes primes); $\boldsymbol{\mathcal E}$ is the
turbulent electromotive force; $\alpha_{\mathcal E}$ is the $\alpha$-effect
coefficient (velocity units; the registry's $\alpha$ is the DG blending
factor); $\sigma_{\mathrm{sgs}}$ is the one-dimensional subgrid velocity
dispersion, with $k_{\mathrm{sgs}}=\tfrac32\sigma_{\mathrm{sgs}}^2$;
$E_{\mathrm{mag}}$ is the magnetic energy density of the resolved field;
$q$ is the quenching parameter; $h$ is the cell size.

## Motivation: a resolution requirement the grid cannot meet

As recalled by Liu et al. (2022, §1, from Brandenburg & Subramanian 2005), a
turbulent dynamo operates only if the dissipation scale is at least about 30
times smaller than the injection scale, i.e. above a critical Reynolds number
estimated numerically at about 30–60. In a simulation whose dissipation comes
from truncation errors (an [implicit LES](/definitions/implicit-les.md) in
this bundle's terms; see [numerical dissipation](/properties/numerical-dissipation.md)),
this becomes a resolution requirement: with the disc thickness as injection
scale, a 1 kpc high-redshift disc needs $h\lesssim30$ pc and a 100 pc
low-redshift thin disc about 3 pc. Under-resolved galaxy and cluster
simulations therefore show a slow or absent dynamo, and the remedy the
authors describe, a strong initial seed field, needs fine tuning (§1). [Martin-Alvarez et al.
(2022)](/sources/martinalvarez-2022.md), who study how far resolution and
refinement strategy take the resolved dynamo, name this subgrid model (cited
as Liu, Kretschmer & Teyssier 2021) as the alternative way to model the
amplification a simulation does not resolve (§4).

## Mean-field background

Liu et al. (2022, §2.2, Eqs. 7–13) split velocity and field into resolved and
unresolved parts, $\boldsymbol u=\bar{\boldsymbol u}+\boldsymbol u^<$,
$\boldsymbol B=\bar{\boldsymbol B}+\boldsymbol B^<$, and write the induction
equation of the resolved field as

$$\frac{\partial\bar{\boldsymbol B}}{\partial t}=\nabla\times\big(\bar{\boldsymbol u}\times\bar{\boldsymbol B}+\boldsymbol{\mathcal E}\big),\qquad \boldsymbol{\mathcal E}=\overline{\boldsymbol u^<\times\boldsymbol B^<}$$

(Eqs. 8–9; ideal MHD, no explicit $\eta_m$). The two-scale expansion
(as recalled from Moffatt 1978)

$$\mathcal E_i=\alpha_{ij}\bar B_j+\beta_{ijk}\frac{\partial\bar B_j}{\partial x_k}+\dots$$

(Eq. 10; $\alpha_{ij}$, $\beta_{ijk}$ page-local transport coefficients) is
truncated to its first term (Eq. 11) and made isotropic,
$\alpha_{ij}=\alpha_{\mathcal E}\delta_{ij}$, so that
$\boldsymbol{\mathcal E}=\alpha_{\mathcal E}\bar{\boldsymbol B}$ (Eq. 12).
The truncation keeps no $\beta_{ijk}$ term: the closure carries no turbulent
magnetic diffusivity. The kinematic estimate recalled for the coefficient is
the subgrid kinetic helicity times a correlation time $\tau_{\mathrm c}$
(page-local),

$$\alpha_{\mathcal E}=-\frac{\tau_{\mathrm c}}{3}\,\overline{\boldsymbol u^<\cdot\boldsymbol\omega^<}$$

(Eq. 13, written with the unresolved parts as the text describes it; see
Qualifications).
The authors call the closure of $\alpha$ "highly controversial and heavily
debated" (§2.2, citing Cattaneo & Hughes, Rädler & Rheinhardt, Gressel et
al.).

## The closure

The model replaces Eq. (13) by (§2.2, Eq. 14)

$$\alpha_{\mathcal E}=\sigma_{\mathrm{sgs}}\max\!\left[1-\frac{E_{\mathrm{mag}}}{q\,\bar\rho\,k_{\mathrm{sgs}}},\,0\right],\qquad E_{\mathrm{mag}}=\frac{|\bar{\boldsymbol B}|^2}{8\pi},\qquad \bar\rho\,k_{\mathrm{sgs}}=\tfrac32\bar\rho\,\sigma_{\mathrm{sgs}}^2,$$

substituted in $\boldsymbol{\mathcal E}=\alpha_{\mathcal E}\bar{\boldsymbol B}$.
The source writes the subgrid turbulent energy per unit volume, $K_T$, which
is $\bar\rho k_{\mathrm{sgs}}$ in this bundle's notation; the modified
induction equation itself is implied by Eqs. (8), (12) and (14), not printed.
Properties stated by the authors:

- **One free parameter**, the quenching parameter $q$: the ratio of magnetic
  to subgrid turbulent energy at which the subgrid dynamo switches off;
  $\alpha_{\mathcal E}=0$ exactly once $E_{\mathrm{mag}}\ge q\bar\rho k_{\mathrm{sgs}}$
  (§2.2). It is interpreted as the saturation level of the subgrid dynamo,
  physically set by the back-reaction of the Lorentz force; saturated
  magnetic-to-turbulent energy ratios from 0.1% to 50% are quoted for
  context (Schober et al. 2015, as recalled).
- **Low $q$ by design.** The subgrid dynamo should only boost a marginally
  resolved dynamo; the resolved flow is expected to amplify the field
  further, up to equipartition. A larger $q$ would give "unrealistically large
  field strengths close to equipartition everywhere" (§2.2, §4.2).
- **Growth time.** The e-folding time of the subgrid amplification is
  $h/\sigma_{\mathrm{sgs}}$, about 3 Myr for $h=100$ pc and
  $\sigma_{\mathrm{sgs}}=30$ km s$^{-1}$ (§5.1.1).
- **A positive scalar.** $\alpha_{\mathcal E}$ carries no helicity sign, so
  the subgrid dynamo amplifies the field parallel to itself; the initial
  orientation survives except where resolved turbulence randomizes it, and
  the initial topology and coherence length of the seed therefore matter
  (§6).
- **Restricted to star-forming gas**, hydrogen number density above
  $10^{-2}$ cm$^{-3}$, the threshold also used for star formation and
  self-shielding; fields in the halo and the intergalactic medium come only
  from outflows or from the seed (§2.2, §6).

## The subgrid kinetic energy that drives it

$\sigma_{\mathrm{sgs}}$ comes from a transport equation for the subgrid
turbulent kinetic energy evolved with the conservative MHD variables, in the
lineage of Schmidt et al. (2006), Semenov et al. (2016) and Kretschmer &
Teyssier (2020), as recalled by Liu et al. (2022, §2.3): production by the
resolved shear, destruction modelling the cascade to viscous scales. The
paper prints neither the equation nor its constants. The same
$\sigma_{\mathrm{sgs}}$ sets the star-formation efficiency per free-fall time
(0–100%) through the cell virial parameter and turbulent Mach number of an
unresolved lognormal density distribution (§2.3). The dynamo closure thus
reuses an existing [SGS](/definitions/large-eddy-simulation.md) energy model
rather than adding a transport equation of its own.

## Calibration and application

- **Choice of $q$** (§4.2, Fig. 1). A series of lower-resolution zoom-in runs
  of the same galaxy (resolution not stated) with $q=10^{-5}$, $10^{-4}$,
  $10^{-3}$: at $z=0$ all gas inside the virial radius is magnetized above the
  subgrid saturation value $q$, and resolved motions then amplify the field
  by a further 3 to 4 orders of magnitude, "but not much more"; with
  $q=10^{-3}$ the magnetic-to-turbulent ratio reaches one or more. The
  fiducial value $q=10^{-3}$ was "determined by experimenting different
  values" (§7).
- **Fiducial run** (§4, §5). A cosmological zoom-in of a Milky Way-like halo
  in [RAMSES](/software/ramses.md), finest cells $h=55$ pc, uniform seed
  $10^{-20}$ G at $z=10$. At $z=4$ the field reaches about 100 μG in the
  galaxy, slightly below equipartition with the subgrid turbulence (ratio
  "close to 0.5"), and about 1 μG in the halo, carried there by outflows
  (§5.1.2). At $z=0.2$ the disc field is about 10 μG (100 μG in the nuclear
  region), in rough equipartition with the subgrid turbulent pressure, and
  the subgrid dynamo is "totally ineffective" at late times (§5.2). The disc
  field is mostly toroidal with one reversal at $r=0.5$ kpc and none at large
  radii, which the authors state disagrees with Pakmor et al. (2018) and
  attribute to the absence of resolved turbulence in the barely resolved
  thin disc (§5.2, §6). Halo fields follow the frozen-in compression scaling
  $|\boldsymbol B|\propto\rho^{2/3}$, normalized to the equipartition field
  of the dense interstellar medium (§5.1.1).
- **Comparisons** (§5, §6): Faraday depths systematically below the
  49-quasar sample of Kim et al. (2016) at high redshift, with the caveat of
  a single halo; fields a factor 2 to 4 weaker than the AURIGA simulations of
  Pakmor et al. (2020), "possibly a consequence of our less turbulent halo
  gas".

## A related induction-equation source term

Another "subgrid-scale model" acting through the induction equation, the [STITCH helicity-condensation
model](/methods/stitch-helicity-condensation-model.md) of [Dahlin et al.
(2022)](/sources/dahlin-2022.md), differs in kind. It is not a closure of a
filtered electromotive force in the volume: it injects, through the bottom
layer of cells of a coronal MHD simulation, the large-scale shear that
unresolved photospheric vortical cells would produce through reconnection
and an inverse helicity cascade, with one parameter set by the size and
rotation rate of those cells (§2, Eqs. 1–2). The authors read it as a
modification of Ohm's law at the base of the atmosphere (§7). Both models
have a single free parameter ($q$ here, the injection amplitude there).
Liu et al. calibrate $q$ on one halo (§4.2); Dahlin et al. compare STITCH
with one simulation that resolves the cells (§4).

## Qualifications

- **Tuned, resolution-dependent parameter.** The authors state that $q$ is
  likely resolution dependent, that many $\alpha$-dynamo models suggest $q$
  inversely proportional to the magnetic Reynolds number, and that $q$ "must
  be adjusted when changing the resolution" (§4.2, §7); this was not tested.
  There is no convergence study and no idealized test (such as a forced
  turbulent box): the evidence is one halo, one fiducial run and three
  low-resolution calibration runs.
- **Simplicity acknowledged.** The authors call the form "very simple
  (probably simplistic)" and propose two improvements: a pseudo-scalar
  $\alpha_{\mathcal E}$ from the local mean-field helicity, or a mean-field
  evolution equation for $\alpha$ with sources and sinks (§6). Eq. (14) is
  not derived from Eq. (13): the coefficient is independent of helicity.
- **Printed slips** (arXiv v2). Eq. (13) is printed
  $\alpha=-\frac{\tau_{\mathrm{corr}}}{3}\overline{\mathbf u\cdot(\nabla\times\mathbf u)}$
  without the primes that mark unresolved parts in Eq. (7), although the
  text calls it the average subgrid kinetic helicity; the form above
  follows the text. The Fig. 2 caption prints
  "$q=10^3$" while §2.2 and §4.2 give the fiducial $q=10^{-3}$. The sentence
  before Eq. (12) says "Eq. 9 becomes" where it is Eq. (11) that becomes
  Eq. (12).
- **Units.** $E_{\mathrm{mag}}=\bar B^2/8\pi$ is written in Gaussian units
  while the MHD system of §2.1 writes the magnetic energy as $\tfrac12B^2$
  (rationalized code units); the ratio in Eq. (14) depends on which is
  meant, and the paper does not say.
- **Resolution threshold quoted twice.** §1 gives about 30 pc for a resolved
  dynamo in a dwarf galaxy, "roughly what was observed" by Rieder & Teyssier
  (2016, 2017b), while §6 says the resolution "has to be better than
  $\Delta x\simeq10$ pc" citing the same works.

# Citations

- [Liu et al. (2022)](/sources/liu-2022.md) — §1; §2.2, Eqs. (7)–(14); §2.3; §4.2, Fig. 1; §5.1.1–§5.1.3; §5.2; §6; §7.
- [Martin-Alvarez et al. (2022)](/sources/martinalvarez-2022.md) — §4 (subgrid modelling as the alternative to resolved amplification).
- [Dahlin et al. (2022)](/sources/dahlin-2022.md) — §2, Eqs. (1)–(2); §4; §7 (contrast: boundary helicity-injection source term).

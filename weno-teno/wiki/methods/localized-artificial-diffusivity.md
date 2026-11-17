---
type: Method
title: "Localized artificial diffusivity (LAD)"
description: "Cook–Cabot localized artificial diffusivity adds artificial shear and bulk viscosities driven by a filtered polyharmonic derivative of the strain rate and a power of the mesh spacing, so that they act at the highest resolved wavenumbers; the page gives the formula and the common constants as recalled by Pirozzoli, the dilatation-based corrections of Mani et al. and Bhagatwala–Lele, and its record against hybrid WENO and quasi-spectral viscosity."
status: established
aliases: [LAD, local artificial diffusivity, Cook–Cabot artificial viscosity, high-wavenumber artificial viscosity, hyperviscosity, artificial bulk viscosity, Kawai–Lele LAD]
tags: [artificial-viscosity, compact-scheme, low-dissipation, turbulence, shock-capturing, central-scheme]
timestamp: 2026-11-17T08:44:05Z
---

# Localized artificial diffusivity (LAD)

**Localized artificial diffusivity** gives a high-order central (typically compact) scheme its shock
capturing by adding an artificial stress to the Navier–Stokes equations whose coefficients are large
only where the solution carries energy at the highest resolved wavenumbers. Cook & Cabot (2004, 2005)
"carried over the idea of selectively damping the highest-resolved wave numbers to physical space",
after the spectral vanishing viscosity of Tadmor; in the form recalled by the review of
[Pirozzoli (2011a)](/sources/pirozzoli-2011.md) (§3.3, Eqs. (33)–(34)),

$$\sigma^*_{ij}=2\mu^*S_{ij}+\big(\beta^*-\tfrac23\mu^*\big)(\nabla\cdot v)\,\delta_{ij},\qquad S_{ij}=\tfrac12\big(\partial_{x_j}v_i+\partial_{x_i}v_j\big),$$

$$\mu^*=c^{(r_{\mathrm L})}_\mu\,\mathcal H_{r_{\mathrm L}},\qquad
\beta^*=c^{(r_{\mathrm L})}_\beta\,\mathcal H_{r_{\mathrm L}},\qquad
\mathcal H_{r_{\mathrm L}}=\rho\,\Delta^{2(r_{\mathrm L}+1)}\,\big\lvert\widehat{\nabla^{2r_{\mathrm L}}\mathsf S}\big\rvert,\qquad
\mathsf S=(2S_{ij}S_{ij})^{1/2}.$$

Page-local symbols: $\sigma^*_{ij}$ the artificial stress, $\mu^*$ and $\beta^*$ the artificial shear
and bulk viscosities, $S_{ij}$ the strain-rate tensor (not the registry's source term $S(u)$),
$\mathsf S$ its magnitude, $\Delta$ "a measure of the local mesh spacing", $\nabla^{2r_{\mathrm L}}$ the
polyharmonic operator ("the $r$-th power of the Laplace operator"), the caret a truncated Gaussian
filter "designed to have smooth" $\mathcal H_{r_{\mathrm L}}$, and $c^{(r_{\mathrm L})}_\mu$,
$c^{(r_{\mathrm L})}_\beta$ user-specified constants; $c_\mu$ below is the von Neumann–Richtmyer constant, page-local. The source writes
$\eta_r$, $r$, $S$, $c^r_\mu$, $c^r_\beta$. "A set of coefficients used by most investigators" is
$r_{\mathrm L}=2$, $c^{(2)}_\beta=1$, $c^{(2)}_\mu=0.002$.

**Relation to the classical viscosities.** For $r_{\mathrm L}=0$ the driver is of the von
Neumann–Richtmyer type, whose viscosity $\mu^*=c_\mu\rho\Delta x^2\lvert\partial_xv\rvert$ spreads
shocks "to a thickness comparable to the local mesh spacing"; the polyharmonic driver "imparts on the
numerical viscosity a higher wave-number bias" (§3.3). The review assigns the two terms different roles:
"inclusion of the bulk viscosity term is the key to capturing shock waves without affecting the
vorticity field, whereas the shear viscosity has the effect of a Smagorinsky-like subgrid-scale model
for unresolved vortical fluctuations". The other artificial viscosities of the bundle (von
Neumann–Richtmyer, Jameson–Schmidt–Turkel, spectral vanishing viscosity, element-wise DG viscosities)
are on [artificial viscosity](/methods/artificial-viscosity.md).

## Corrections and extensions

As recalled by Pirozzoli (2011a, §3.3):

- **Dilatation-driven bulk viscosity.** Mani, Larsson & Moin (2009) observe that the strain-driven
  definition "introduces unnecessary damping into resolved dilatational motions (acoustic waves)". They
  replace $\mathsf S$ by the dilatation $\nabla\cdot v$ in the driver of the bulk viscosity and set it to
  zero where $\nabla\cdot v>0$ (expansions).
- **Further selectivity.** Bhagatwala & Lele (2009) make the bulk-viscosity coefficient "effectively
  zero in the presence of resolved acoustic motions".
- **Contacts and mixtures.** Fiorina & Lele (2007) and Cook (2007) add artificial terms for strong
  temperature gradients (contact discontinuities) and for species diffusion in multicomponent mixtures.
- **Curvilinear meshes.** Kawai & Lele (2008; printed 2007 in the review) extend the method to
  generalized curvilinear coordinates.

None of these papers is ingested; their formulas are not printed in the review beyond the sentences
above.

## Use and record

- **Jet in supersonic crossflow.** Kawai & Lele (2010, as recalled by Pirozzoli 2011a, §5, Fig. 7) run
  the method "in Kawai & Lele's (2007) version", with sixth-order compact derivatives and eighth-order
  low-pass filtering, for LES of an underexpanded sonic jet in supersonic crossflow; the bow shock, the
  upstream separation shock, the barrel shock and the Mach stem are captured "all without spurious
  wiggles", with a broad range of turbulence scales resolved.
- **Against quasi-spectral viscosity.** [Sousa & Scalo (2022)](/sources/sousa-2022.md) (§5, §7.1) take
  the LAD of Cook and Kawai–Lele, with an explicit Padé filter of strength 0.495
  ([compact low-pass filters](/methods/compact-low-pass-filter.md)), as the reference shock-capturing
  method for their [quasi-spectral viscosity](/methods/quasi-spectral-viscosity.md) (QSV) on a
  sixth-order compact central scheme. On Sod both converge, but LAD needs the explicit filter (§5.1). On
  the shock reflection off a sinusoidal wall at $M=1.5$ LAD gives a stronger spurious contact from the
  initial jump and oscillates near the primary vortex; at $M=5$, $\gamma=1.15$ it oscillates strongly
  and breaks symmetry early, while QSV keeps symmetry (§5.3;
  [symmetry preservation](/properties/symmetry-preservation.md)). On the supersonic Taylor–Green vortex
  ($M_t=1.2$, Re 5000, $96^3$) every LES model other than QSV blows up without shock capturing, and every LAD-aided run
  over-dissipates near the strongest shocklets, $tV_0/L\approx6.5$ (§7.1).

## Positions

The review of Pirozzoli (2011a, §6, Summary 9) calls nonlinear artificial viscosity methods,
"especially in their most recent variants (Mani et al. 2009)", "an attractive alternative to hybrid
shock-capturing methods" ([hybrid schemes](/methods/hybrid-weno.md)): they apply "in the same form
throughout the computational domain, without the need of hybridization", and their implementation in
existing Navier–Stokes solvers for shock-free flows is straightforward; but "applications of the method
are recent, and further testing is required to demonstrate comparable reliability to WENO for a range
of applications". Sousa & Scalo's evidence above is a later comparison against one alternative, QSV,
not against WENO.

## Qualifications

- The review prints the bulk-viscosity coefficient of Eq. (34) as $\beta$ while Eq. (33) calls it
  $\beta^*$, and says that Mani et al. replaced $S$ "in the definition of $c^r_\beta$" and set
  "$c^r_\beta$ to zero" in expansions; the change is to the driver of $\beta^*$ (equivalently,
  $\beta^*=0$ there), not to the constant. This page writes $\beta^*$ throughout.
- The review places the filter caret inside the modulus, $\lvert\widehat{\nabla^{2r_{\mathrm L}}\mathsf S}\rvert$ (Eq. (34)), while saying the filter is "designed to have smooth $\eta_r$"; the page writes the formula as printed.
- Neither source states the filter width of the caret, the definition of $\Delta$ on non-uniform
  meshes, or the artificial conductivity used with the method; Sousa & Scalo mention an artificial
  conductivity without writing it out.
- All evidence recorded here is numerical; no stability or accuracy result for the method is stated in
  the ingested sources.

# Citations

- [Pirozzoli (2011a)](/sources/pirozzoli-2011.md) — §3.3, Eqs. (33)–(34): the Cook–Cabot form, constants, von Neumann–Richtmyer limit, corrections and extensions as recalled; §5, Fig. 7: Kawai & Lele's jet in crossflow; §6, Summary 9: position against hybrid WENO (review).
- [Sousa & Scalo (2022)](/sources/sousa-2022.md) — arXiv v2: §5.1 (Fig. 4), §5.3 (Figs. 8–11), §7.1 (Figs. 16–19): LAD of Cook and Kawai–Lele as the reference shock capturing against QSV.

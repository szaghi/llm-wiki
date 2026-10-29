---
type: Definition
title: "Bottleneck effect in the energy spectrum"
description: "The bottleneck is a bump of excess energy just ahead of the range where a dissipation mechanism takes over. The sources find it in fully resolved DNS (viscous, near k·eta 0.1–0.2), in implicit LES and low-dissipation DG (numerical), and in compressible modes without bulk viscosity, and keep it apart from cutoff pile-up."
status: established
aliases: [bottleneck, spectral bottleneck, bottleneck bump, compressible-mode bottleneck, soft pile-up]
tags: [dns, implicit-les, numerical-dissipation, compressible, astrophysics]
timestamp: 2026-10-29T05:13:00Z
---

# Bottleneck effect in the energy spectrum

The **bottleneck effect** is a local excess of energy in the spectrum $E(k)$,
a bump, just ahead (at lower $k$) of the wavenumbers where a dissipation
mechanism starts to remove energy. The inertial-range power law therefore
flattens or rises before the spectrum falls into the dissipation range. In
the sources that use the term it has three distinct origins:

- **physical**, molecular viscosity in a fully resolved
  [DNS](/definitions/direct-numerical-simulation.md) of isotropic
  turbulence;
- **numerical**, the scale-selective dissipation of an
  [implicit LES](/definitions/implicit-les.md) operator or of a
  low-dissipation discretization;
- **missing physics**, the compressible velocity modes of a compressible
  simulation that has no [bulk viscosity](/definitions/bulk-viscosity.md).

The bottleneck is not the same thing as the **pile-up at the cutoff** of an
under-dissipative LES, and not the same as **thermalization** to $E(k)\propto
k^2$; the last section separates the three.

## Physical bottleneck in resolved DNS

[Yeung et al. (2025)](/sources/yeung-2025.md) (§3, Fig. 3b) plot the
compensated spectrum $E(k)\langle\varepsilon\rangle^{-2/3}k^{5/3}$ from
pseudo-spectral DNS of forced
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
at $Re_\lambda\approx390$–$2500$, on grids from $2048^3$ to $32\,768^3$. The
final resolution is $k_{\max}\eta\approx2.8$, with $k_{\max}$ the largest
resolved wavenumber (page-local). The data were produced with
[multi-resolution independent simulations](/methods/multi-resolution-independent-simulations.md).
The compensated spectrum shows no plateau. Instead the data support:

1. an inertial-range slope steeper than $-5/3$, which the authors relate to
   the intermittency correction of Kolmogorov (1962), which they cite;
2. "a bump, called the bottleneck, which is strongest at $k\eta$ between 0.1
   and 0.2".

On the mechanism, Yeung et al. state (§3) that, "because of the 5/3
exponent, the peak of the bottleneck is at a wavenumber slightly below that
for the dissipation spectrum $D(k)\propto k^2E(k)$, hence viscous effects
certainly play a role". $D(k)$ is page-local. The bump is also visible in
the one-dimensional longitudinal spectrum $E_{11}(k)$ (page-local), but it is
weaker there than in $E(k)$. The authors checked the two spectra against the
isotropy relation $E(k)=k^3\,\mathrm d[(1/k)\,\mathrm dE_{11}/\mathrm dk]$.

For the earlier literature they point to Donzis & Sreenivasan (2010) on the
bottleneck itself, and to the spectral fitting functions of Meyers &
Meneveau (2008), which carry both the intermittency correction and the
bottleneck (both cited by Yeung et al. 2025, §3). The conclusions (§5) list the
bottleneck among the scaling properties that the MRIS data "reproduced
well". The dashed reference lines of Fig. 3(b) sit at the "generally
accepted" values 1.62 (three-dimensional) and $(1.62)(18/55)=0.53$
(one-dimensional) (§3).

## Numerical bottleneck in implicit LES and low-dissipation schemes

When the dissipation that ends the resolved cascade comes from the
discretization, its spectral shape decides where energy accumulates.

**Implicit spectral vanishing viscosity.**
[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) (§6.4,
Fig. 15, Eq. 50) compute the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $Re=40\,000$
with a sixth-order compact scheme and implicit
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md).
They approximate the effective filter of the scheme by the super-Gaussian
$\hat G(k)=\exp(-k^6\Delta^6/256)$, but the filtered spectrum shows an
extended bump whose top is near $k\approx k_c/4$: a soft pile-up for
$k<k_c/2$. The authors read it as a spurious defiltering and call it "the
main drawback of present implicit modelling".

Adding the [Smagorinsky model](/methods/smagorinsky-model.md) to the
implicit operator affects the bump (§6.5, Figs. 20–21):

| $C_s$ added to implicit SVV | bottleneck | total dissipation |
|---|---|---|
| 0.1 | reduced | not improved |
| 0.18 | removed | not improved |

The explicit part also restores the low-$k$ plateau of the
[spectral eddy viscosity](/methods/spectral-eddy-viscosity.md). That plateau
is the non-local transfer which scale-selective implicit dissipation lacks.
In their conclusions (§8) the authors put the bottleneck and the missing
non-local transfer together. For strong reductions in degrees of freedom,
$\Delta/h_{\mathrm{DNS}}\gtrsim5$, these two defects motivate an explicit
model dedicated to non-local triad interactions. The mixed
explicit–implicit variant is also discussed on
[scale-similarity and mixed models](/methods/scale-similarity-model.md).

**High-order discontinuous Galerkin.**
[Cernetic et al. (2024)](/sources/cernetic-2024.md) run driven, isothermal,
solenoidally forced turbulence in a periodic box. They use a GPU **modal**
DG code with a Legendre total-degree basis and an HLLC flux, which is not
the nodal
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md), and
compare it with a second-order finite-volume scheme. The runs have no
explicit viscosity or SGS model, so the dissipation is numerical plus the
von Neumann–Richtmyer
[artificial viscosity](/methods/artificial-viscosity-shock-capturing.md) at
compressions.

The sources' scheme labels give the convergence order, so "DG-2" and "DG-3"
are degrees $N=1$ and $N=2$ in this bundle's notation.

- **$256^3$, subsonic runs (§5, Fig. 5).** Going from finite volume to DG
  extends the resolved range of the velocity spectrum. The extension is
  already clear at $N=1$ and larger at $N=2$, "with the latter showing also
  signs of a more pronounced bottleneck effect, which reflects the different
  and generally lower numerical dissipation in this scheme".
- **$1024^3$, $M=3.2$, $N=1$ (§6, Fig. 10).** The spectrum steepens to
  $k^{-2}$ just beyond the driving range, flattens towards $k^{-5/3}$ below
  the sonic scale, and then shows "a prominent bottleneck effect (as
  expected) with a small shoulder in the power spectrum before $E(k)$ drops
  rapidly in the dissipative regime".
- **Effect on the subsonic range (§6).** Cernetic et al. state that this
  subsonic range is short at the available resolution, "and thus the
  bottleneck effect from the onset of the dissipation range influences a good
  part of it". They state that the limited dynamic range and "the influence
  of the bottleneck effect are likely causes" of the fitted
  structure-function slope 0.43 on the subsonic side, against the expected
  $1/3$ (§6, Fig. 8).

The two studies report the bump with a numerical dissipation of their own
scheme: Cernetic et al. relate the stronger bump at $N=2$ to "generally lower
numerical dissipation" (§5), and Vicente Cruz & Lamballais find that adding
Smagorinsky dissipation to implicit SVV reduces or removes it (§6.5). See
[numerical dissipation](/properties/numerical-dissipation.md).

## Compressible-mode bottleneck without bulk viscosity

[Beattie et al. (2025)](/sources/beattie-2025.md) simulate the
[small-scale dynamo](/results/small-scale-dynamo.md) in isothermal,
visco-resistive compressible MHD at rms $M\approx1$. The code is a modified
FLASH: finite volume, second-order MUSCL–Hancock, a five-wave Riemann solver.
The runs use $Re=Rm=1000$ and grids of $128^3$–$1024^3$.

They add an explicit bulk viscosity, written here $\nu_b$ (the kinematic
bulk viscosity, registry §11), and vary the ratio $P_\nu=\nu/\nu_b$
(registry §11; the source's "viscous Prandtl number"). They split the
spectrum into compressible and solenoidal parts by a Helmholtz
decomposition, written $E_{\mathrm c}(k)$ (compressive part) and
$E_{\mathrm s}(k)$ (solenoidal part), registry §11 (the source's
$E_{\rm kin,\parallel}$, $E_{\rm kin,\perp}$; the subscripts $\parallel$,
$\perp$ are kept for the magnetic-field directions on the MHD pages).

- **$P_\nu=\infty$ ($\nu_b=0$) and $P_\nu=1$ (§6.1, Fig. 9).** "An excess
  amount of power piling up at high-$k$, which could be qualitatively
  described as a bottleneck effect". The authors identify it with their
  "sub-shear-viscous range": a range below the shear-viscous scale in which
  the compressible modes have not yet met any dissipation of their own.
- **Size of the excess (§6.2).** For $P_\nu>1$ the ratio
  $E_{\mathrm c}(k)/E_{\mathrm s}(k)$ goes from $\approx10^{-1}$ at large scales to
  $\approx10^{2}$ at small scales, so the compressible modes dominate the
  bump.
- **$P_\nu\le0.1$ (§6.1).** "The sub-shear-viscous range and bottleneck
  completely disappear", leaving "a smooth, rather featureless decay". Once
  $\nu_b$ is large enough, the physical dissipation removes the compressible
  modes faster than they can move down the (fast, $k^{-2}$) cascade, "and
  hence the bottleneck and sub-shear-viscous range is destroyed".
- **Effect on the magnetic field (§7, Figs. 10–11).** Suppressing the
  bottleneck through $\nu_b$ also suppresses high-$k$ magnetic modes, and the
  field becomes larger-scale.

The authors' resolution study (App. D) supports the reading that this
bottleneck is a resolution artefact of the missing dissipation:

- for $P_\nu=0.1$ the run is "converged on all scales at $512^3$";
- for $P_\nu=1$ the bulk-viscous scale is unresolved even at $1024^3$;
- for $P_\nu=\infty$ they state that $E_{\mathrm c}/E_{\mathrm s}$ at high $k$ should
  "grow unbounded" with resolution, "exactly what one expects for an ILES".

Hence their claim (§9.1) that a shear-viscous "DNS" without bulk viscosity
is "an implicit large eddy simulation for the compressible modes" (see
[implicit LES](/definitions/implicit-les.md),
[direct numerical simulation](/definitions/direct-numerical-simulation.md),
[compressible MHD turbulence](/results/compressible-mhd-turbulence.md)).

## Distinguishing the bottleneck from cutoff pile-up and thermalization

The sources describe three spectral symptoms of dissipation that is missing
or misplaced.

| symptom | where the excess sits | cause in the sources | examples |
|---|---|---|---|
| bottleneck | a bump inside the resolved range, ahead of where dissipation takes over ($k\eta\approx0.1$–$0.2$ in DNS; $k<k_c/2$, top near $k_c/4$, for implicit SVV) | a dissipation that switches on sharply in $k$ (viscous, scale-selective numerical, or shear-only in a compressible flow) | Yeung et al. (2025); Vicente Cruz & Lamballais (2023, §6.4); Cernetic et al. (2024); Beattie et al. (2025) |
| pile-up at the cutoff | the highest resolved wavenumbers, near $k_c$ | too little dissipation at the cutoff: no-model or under-dissipative LES | Prakash et al. (2022, §III.B.1, Fig. 4); Kurz et al. (2023, §4.2, Fig. 6); Vicente Cruz & Lamballais (2023, §6.2–6.3); Tsoutsanis & Nogueira (2025, §1, §4.1) |
| thermalization | most of the resolved range relaxes to $E(k)\propto k^2$ equipartition | no dissipation at all (truncated Euler, kinetic-energy-conserving no-model LES) | Vicente Cruz & Lamballais (2023, §6.2); Flad & Gassner (2017, §3, Fig. 4) |

The examples in the last two rows, with the cited sections:

- **Pile-up at the cutoff.** In forced isotropic turbulence,
  [Prakash et al. (2022)](/sources/prakash-2022.md) (§III.B.1, Fig. 4) find
  a large pile-up at the highest resolved wavenumbers for the no-model run
  and for the unclipped [gradient model](/methods/gradient-model.md), and
  none for [dynamic Smagorinsky](/methods/dynamic-procedure.md).
  [Kurz et al. (2023)](/sources/kurz-2023.md) (§4.2, Fig. 6) find the same
  build-up in no-model DG LES at $N=5$ and 7.
- **Build-up in the high modes of implicit LES, detected cell by cell.**
  [Tsoutsanis & Nogueira (2025)](/sources/tsoutsanis-2025.md) (§1) state
  that across finite-element, finite-difference and finite-volume
  frameworks a method with very low numerical dissipation "leads to an
  unphysical 'build-up' of energy in the high modes", which they relate
  also to dispersive effects on under-resolved grids, more pronounced in DG
  but present in finite volumes as the order rises; an
  [implicit LES](/definitions/implicit-les.md) must dissipate at the
  smallest grid scales the energy that the truncated cascade delivers
  there. They detect it locally, without a spectrum: an energy ratio of
  the residual momentum energies of the unlimited central reconstruction
  polynomial after a weak and after a strong modal filter (§4.1, Eq. 29;
  thresholds 0.95 and 1.2, Eq. 36). In the under-resolved inviscid
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) they read
  values far above one as "an unphysical 'build-up' of energy in the high
  modes associated with the high-order polynomial terms", with more such
  cells on tetrahedral and hybrid than on hexahedral meshes "even at
  early times" (§4.1, Fig. 6). Their scheme raises the dissipation of a
  CWENOZ reconstruction in those cells (see
  [WENO schemes](/methods/weno-scheme.md) and
  [numerical dissipation](/properties/numerical-dissipation.md)). The paper
  does not use the word bottleneck.
- **Cutoff pile-up with Smagorinsky.** Vicente Cruz & Lamballais (2023,
  §6.3) find that Smagorinsky with $h=\Delta$ "cannot control" the pile-up
  near $k_c$, which they attribute to differentiation errors.
- **Thermalization.** The same authors find that no-model LES thermalizes
  on more than 80% of the wavenumbers at their low resolution (§6.2).
  [Flad & Gassner (2017)](/sources/flad-2017.md) (§3, Fig. 4) obtain an
  approximate $k^2$ spectrum from dissipation-free split-form DG; see
  [kinetic-energy preservation](/properties/kinetic-energy-preservation.md).

A model or scheme can remove a cutoff pile-up and still produce a
bottleneck. Implicit SVV prevents thermalization and the cutoff pile-up, but
it creates the bump at $k_c/4$ (Vicente Cruz & Lamballais 2023, §6.4).

## Qualifications

- **No source models the bump quantitatively.** Yeung et al.
  give a qualitative viscous argument and defer to the literature. Cernetic
  et al. attribute the DG bump to lower numerical dissipation without a
  spectral analysis of the scheme. Beattie et al. call their pile-up one that
  "could be qualitatively described as" a bottleneck. No source gives a
  quantitative model of the bump's height or position. The three
  observations concern different dissipation operators (viscous, numerical,
  shear-only viscous in a compressible flow).
- **Beattie et al. (2025) print different thresholds for the disappearance
  of the compressible bottleneck.**
  - The abstract says it "disappears for $P_\nu\approx1$".
  - §6.1 shows it present at $P_\nu=1$ and gone "as $P_\nu$ decreases to
    $\le0.1$".
  - §6.2 says it disappears "once $P_\nu<1$".
  - The Fig. 10 discussion marks it as "only present in simulations with
    $P_\nu>0.1$".
  - §6.1 adds that the threshold "ought to be $P_\nu\approx1/3$ based on our
    definition" (footnote 5).

  The simulated values are $P_\nu\in\{\infty,1,0.1,0.01,0.001\}$ (§4,
  Table 1), with the bump present at 1 and absent at 0.1 (§6.1); the
  simulated set thus places the threshold between 1 and 0.1, which every
  printed statement except the abstract's "$\approx1$" accommodates
  *(compiler check, not in the sources)*.
- **Cernetic et al. (2024) label orders, not degrees.** Their "$p=2$, 3" (and
  in one place "$k=2$" for the order-2 runs, §5) are convergence orders, so
  the stronger bottleneck belongs to the degree-$N=2$ modal scheme, a
  modal, total-degree DG, not the nodal DGSEM.
- **Yeung et al. (2025) add a note in proof.** It points to Okamoto et al.
  (2025b, under review) for "new insights relevant to figure 3(b)" (the
  spectrum and bottleneck panel); its content is not given.

# Citations

- [Yeung et al. (2025)](/sources/yeung-2025.md) — §3, Fig. 3(b) (compensated $E(k)$ and $E_{11}(k)$, bottleneck strongest at $k\eta\in[0.1,0.2]$, viscous argument via $D(k)\propto k^2E(k)$, isotropy check); §2.2, Table 1 (MRIS, $k_{\max}\eta\approx2.8$); §5 (conclusions); note added in proof.
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §6.2–6.3 (thermalization, cutoff pile-up with Smagorinsky); §6.4, Fig. 15, Eq. (50) (implicit-SVV bottleneck near $k_c/4$); §6.5, Figs. 20–21 (Smagorinsky added to SVV reduces or removes it); §8 (conclusions).
- [Cernetic et al. (2024)](/sources/cernetic-2024.md) — arXiv v2: §5, Fig. 5 (more pronounced bottleneck at DG order 3); §6, Figs. 8 and 10 (prominent bottleneck at $1024^3$, $M=3.2$; slope 0.43 attributed in part to it); §2, §3.1 (modal DG, artificial viscosity).
- [Beattie et al. (2025)](/sources/beattie-2025.md) — arXiv v4: abstract; §6.1–6.2, Fig. 9 (compressible-mode bottleneck, sub-shear-viscous range, removal by bulk viscosity); §7, Figs. 10–11; App. D (resolution study); §9.1 (DNS as implicit LES of the compressible modes); §4 (numerical set-up).
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §III.B.1, Fig. 4 (cutoff pile-up of no-model and unclipped gradient runs).
- [Kurz et al. (2023)](/sources/kurz-2023.md) — §4.2, Fig. 6 (no-model DG pile-up).
- [Flad & Gassner (2017)](/sources/flad-2017.md) — §3, Fig. 4 ($k^2$ equipartition from dissipation-free split-form DG).
- [Tsoutsanis & Nogueira (2025)](/sources/tsoutsanis-2025.md) — §1 (build-up of energy in the high modes of low-dissipation implicit LES); §4.1, Eqs. (29), (36), Fig. 6 (energy-ratio detection of the build-up, hexahedral against tetrahedral meshes).

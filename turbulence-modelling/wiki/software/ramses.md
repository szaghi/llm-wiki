---
type: Software
title: "RAMSES"
description: "RAMSES is an octree adaptive-mesh-refinement code with a second-order Godunov MHD solver and constrained transport; in the sources it hosts cosmological galaxy-formation runs whose dissipation is purely numerical, a one-equation subgrid turbulence model, a subgrid dynamo, and a comparison of refinement strategies for the turbulent dynamo."
status: established
aliases: [ramses, RAMSES-MHD]
tags: [software, astrophysics, mhd, implicit-les, mesh-adaptation, dynamo]
timestamp: 2026-10-25T19:44:00Z
---

# RAMSES

**RAMSES** is an adaptive-mesh-refinement (AMR) code for self-gravitating
gas, dark matter and stars, introduced by Teyssier (2002) as recalled by both
sources: an octree mesh, a second-order Godunov solver for the gas and the
magnetic field, and N-body particles coupled through gravity. Two ingested
sources run it on cosmological zoom-in simulations of Milky Way-like galaxies
with magnetic fields: [Liu et al. (2022)](/sources/liu-2022.md), who add a
[subgrid turbulent dynamo model](/methods/subgrid-turbulent-dynamo-model.md),
and [Martin-Alvarez et al. (2022)](/sources/martinalvarez-2022.md), who use
a version modified by the authors to study how the refinement strategy
controls the resolved [small-scale dynamo](/results/small-scale-dynamo.md).
Both are peripheral to closure modelling; they bear on it through the
role of numerical dissipation and of subgrid models in astrophysical codes.

## Discretization

- **Solver.** Ideal MHD with gravity, heating and cooling, solved with the
  second-order unsplit Godunov scheme of Fromang et al. (2006) based on
  MUSCL–Hancock (Liu et al. 2022, §2.1, Eqs. 1–6, as recalled); "a second
  order Godunov scheme" (Martin-Alvarez et al. 2022, §2, §3.2). Ideal
  monatomic gas, $\gamma=5/3$ (Martin-Alvarez et al. 2022, §2).
- **Constrained transport.** The induction equation is advanced by
  constrained transport (Teyssier, Fromang & Dormy 2006, as recalled), with
  the magnetic field stored on cell faces, which keeps
  $\nabla\cdot\boldsymbol B=0$ to machine precision (Liu et al. 2022, §2.1)
  or "by construction" (Martin-Alvarez et al. 2022, §2). Martin-Alvarez et
  al. (App. A, Fig. A1) check it: the relative divergence
  $|\nabla\cdot\boldsymbol B|\,h/|\boldsymbol B|$, with $h$ the local cell
  size, stays almost always below the per-cent level for the face-centred
  field, and is negligible for cell-centred fields evaluated per oct.
- **No explicit diffusion.** Martin-Alvarez et al. (2022, §2, Eq. 1) set the
  magnetic diffusivity $\eta_m=0$ explicitly, so that "all diffusive effects
  in our simulations are of numerical nature"; they estimate the resulting
  numerical magnetic Prandtl number $Pm\sim2$ (§3.3.5). Liu et al. (2022, §1)
  likewise take the dissipation to be "provided by local truncation errors".
  The flow part is thus an [implicit LES](/definitions/implicit-les.md) in
  this bundle's sense, although neither source uses the term, and the
  effective Reynolds number is set by [numerical
  dissipation](/properties/numerical-dissipation.md) and the cell size.

## Mesh refinement

- **Quasi-Lagrangian refinement** (the standard criterion in both sources).
  A cell is refined when it holds more than the mass of eight dark-matter
  particles (Martin-Alvarez et al. 2022, §2.1), or more than eight
  dark-matter particles or a baryonic mass above eight baryonic particle
  masses (Liu et al. 2022, §4.1). Refinement levels are released with time to
  keep a quasi-constant physical resolution (Liu et al.: initial grid levels
  7 to 11, maximum level 19, finest cells 55 pc). RAMSES expands refinement $n_{\mathrm{expand}}$ times
  around flagged cells (default 1) and allows no level jump larger than one
  across a boundary (Martin-Alvarez et al. 2022, §2.1).
- **Quasi-Eulerian refinement** (Martin-Alvarez et al. 2022, §2.1, their
  contribution). Every cell with gas density above
  $\rho_{\mathrm{th}}=10^{-24}$ g cm$^{-3}$ (page-local) is refined to the
  maximum level, so the whole galaxy sits on an almost uniform grid, while
  the quasi-Lagrangian criterion still acts outside it. The aim is to reduce
  the number of distinct numerical viscous and resistive scales that
  multi-level AMR introduces, one per level: the authors argue that turbulent
  and magnetic energy is "dissipated significantly more than expected" for
  the finest cell size, and that small-scale structure is lost when gas
  crosses into coarser levels (§1, §2.1). Quasi-Lagrangian refinement
  concentrates resolution on the cold dense phase and under-resolves the
  warm and hot phases; the quasi-Eulerian criterion resolves the warm and
  cold phases at about the same resolution (§2.1, Fig. 2).
- **Cost** (Martin-Alvarez et al. 2022, §2.2, Table 1). The extra cost is
  stated to be minor below 80 pc resolution (printed wording); the run with
  20 pc quasi-Eulerian refinement costs about twice its quasi-Lagrangian
  counterpart, with $31\times10^6$ against $5\times10^6$ active cells finer
  than 320 pc at $z=9$ and $21\times10^6$ against $10\times10^6$ at $z=2$;
  the 10 pc quasi-Eulerian run, $127\times10^6$ cells at $z=9$, was stopped
  at $z\sim8.5$. No hardware or wall-clock times are given. The dynamo
  consequences are on the [small-scale dynamo](/results/small-scale-dynamo.md)
  page. General refinement and adaptation strategies for turbulent flows are
  on [mesh adaptation](/methods/mesh-adaptation.md).

## Subgrid models

- **Subgrid turbulent kinetic energy.** A transport equation for the subgrid
  turbulent kinetic energy, with production by resolved shear and
  destruction modelling the cascade to viscous scales, in the lineage of
  Schmidt et al. (2006), Semenov et al. (2016) and Kretschmer & Teyssier
  (2020), as recalled by Liu et al. (2022, §2.3); its equation is not printed
  there. It sets the star-formation efficiency per free-fall time through the
  cell virial parameter and turbulent Mach number.
- **Subgrid turbulent dynamo.** The [subgrid turbulent dynamo
  model](/methods/subgrid-turbulent-dynamo-model.md) of Liu et al. (2022,
  Eq. 14) drives an $\alpha$ effect with the velocity dispersion of that
  subgrid energy. The authors state that both models are in the public
  version of RAMSES (§7).
- **Galaxy-formation physics.** Supernova feedback, thermal or with the
  terminal momentum when the cooling radius is unresolved (Liu et al. 2022,
  §2.3), or mechanical with a fiducial or boosted specific energy of
  $10^{50}$ or $2\times10^{50}$ erg $M_\odot^{-1}$ (Martin-Alvarez et al.
  2022, §2); star formation where gravity exceeds the combined turbulent,
  magnetic and thermal support in the modified version of Martin-Alvarez et
  al. (§2); cooling, ultraviolet background and self-shielding in both.

## Divergence control and the dynamo

Martin-Alvarez et al. (2022, §1) report, from the galaxy-formation
literature, that Powell divergence cleaning yields fast amplification while
Dedner cleaning and constrained transport find lower growth rates, and that
constrained-transport methods have "significantly higher computational cost
and produce considerably lower amplification rates", which that literature
attributes to the numerical diffusivity of the solver. All their own runs use
constrained transport; their argument is that the quasi-Lagrangian
refinement, not only the induction scheme, is responsible for part of the
slow growth. This is a statement about un-ingested works, not tested here
across divergence treatments.

## Qualifications

- Liu et al. (2022, Eq. 2) print the total pressure $P_{\mathrm{tot}}$ inside
  the momentum flux without an identity tensor, and write the magnetic energy
  as $\tfrac12B^2$ (code units) in §2.1 but as $B^2/8\pi$ (Gaussian) in §2.2.
- Liu et al. (2022, §2) announce a list of model parameters that does not
  appear in the version read.

# Citations

- [Liu et al. (2022)](/sources/liu-2022.md) — §1; §2.1, Eqs. (1)–(6); §2.2, Eq. (14); §2.3; §4.1; §5.2; §7.
- [Martin-Alvarez et al. (2022)](/sources/martinalvarez-2022.md) — §1; §2, Eq. (1); §2.1, Fig. 2; §2.2, Table 1; §3.3.5; App. A, Fig. A1.

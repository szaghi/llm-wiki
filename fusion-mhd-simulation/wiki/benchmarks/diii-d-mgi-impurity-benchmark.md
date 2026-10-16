---
type: Benchmark
title: "DIII-D gas-injection impurity benchmark (Lyons et al. 2019)"
description: "Axisymmetric benchmark of impurity-driven radiative collapse on the DIII-D shot 137611 equilibrium with central argon or neon gas injection, defined by Lyons et al. (2019) for M3D-C1 and NIMROD and later run by JOREK with coronal-equilibrium and collisional-radiative impurity models."
status: established
aliases: [Lyons 2019 benchmark, DIII-D 137611 impurity benchmark, axisymmetric impurity benchmark]
tags: [benchmark, verification, impurities, disruption]
timestamp: 2026-10-16T00:00:00Z
---

# DIII-D gas-injection impurity benchmark (Lyons et al. 2019)

The benchmark tests how extended-MHD codes with impurity models reproduce
the radiative collapse of a tokamak plasma after massive gas injection,
without 3D MHD: all runs are axisymmetric ($n=0$). It was defined by Lyons
et al. (2019, PPCF 61:064001, not ingested here) for
[M3D-C1](/software/m3d-c1.md) and [NIMROD](/software/nimrod.md), which
track every impurity charge state with the KPRAD model and coronal-model
(ADPAK) rates. [JOREK](/software/jorek.md) ran it first with its
[coronal-equilibrium model](/methods/coronal-equilibrium-impurity-model.md)
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.7) and then with its
[collisional-radiative model](/methods/collisional-radiative-impurity-model.md)
([Hu et al. (2021b)](/sources/hu-2021-b.md), §3, §6).

## Setup

As run by [Hu et al. (2021b)](/sources/hu-2021-b.md) (§3, Eq. 18, Fig. 1):

- **Equilibrium**: DIII-D shot 137611 at 1950 ms, the equilibrium of Lyons
  et al.; initial pure deuterium with uniform $n_e=n_i=10^{20}$ m$^{-3}$.
- **Injection**: argon or neon, about $4.37\times10^{23}$ atoms/s, from a
  Gaussian source centred at $(R,Z)=(1.77037,\,0.01447)$ m on the axis,
  axisymmetric (toroidal width taken large). JOREK's source lacks the
  $R_0/R$ factor of the original definition.
- **Transport**: particle diffusivity $D=10$ m²/s (isotropic); heat
  diffusivities $\chi_\perp=100$ m²/s and $\chi_\parallel=10^8$ m²/s (the
  same for ions and electrons in two-temperature runs); momentum
  diffusivity 100 m²/s initially.
- **Resistivity**: either constant, $\eta=10^{-5}$ Ω m, or Spitzer-like with
  the Hirshman $Z_{\mathrm{eff}}$ factor, a 1 eV floor on $T_e$ and a
  coefficient 2.444 times the physical one, as in Lyons et al. (Eq. 7).
- **Setup differences**: JOREK gives the viscosity the temperature
  dependence of the resistivity (constant magnetic Prandtl number), while
  Lyons et al. used a constant momentum diffusivity; JOREK solves
  [reduced MHD](/methods/reduced-mhd.md) with one or two temperatures.

## Results

**M3D-C1 and NIMROD.** They "follow each other rather well", so Hu et al.
compare JOREK with NIMROD only, using data digitized from Lyons et al.
(§6.1). Lyons et al. already report a stronger final Ohmic burst in NIMROD
than in M3D-C1 (§6.2, as cited).

**JOREK with coronal equilibrium.** JOREK "predicts a roughly two times
slower thermal collapse than M3D-C1 and NIMROD"
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.7). No figure is given
in that paper.

**JOREK with collisional-radiative impurities** ([Hu et al. (2021b)](/sources/hu-2021-b.md),
§6, Figs. 10–17):

- *Constant $\eta$*: the increase in electron number agrees early and
  departs near the 100→10 eV turning points (Fig. 10). For argon the
  combined cooling power has the same shape and a similar peak, delayed by
  0.15 ms in JOREK, and the thermal energy is depleted at the same time
  (Fig. 11). Neon agrees until $t=1.2$ ms. After that JOREK has a higher
  radiation peak and a rapid drop, while NIMROD plateaus (Fig. 12).
- *Spitzer-like $\eta$*: the electron-number increase agrees better, but
  JOREK neon still recombines significantly below 100 eV at $t=1.2$ ms
  (Fig. 13). The argon cooling peak is slightly later, the Ohmic plateau
  is at the same level and the final burst comes at the same time, NIMROD's
  being stronger (Fig. 14). The neon termination comes at about 1.7 ms in
  both codes (Fig. 17).
- *2D evolution*: inside-out collapse, hollow $T_e$, a thin current and
  temperature halo, and final re-concentration of the current near a new
  axis follow Figs. 7–8 of Lyons et al.; JOREK's current halo is "not as
  steep" (§6.2, Figs. 15–16).

All comparisons are visual; no error metric is reported (§6).

## Spread and its attribution

- Hu et al. attribute the remaining JOREK–NIMROD differences to the atomic
  data: open-ADAS collisional-radiative rates against KPRAD-fitted ADPAK
  coronal-model rates. They support this with an argon rerun using
  a different ADAS line-radiation data set (labelled "1942" in the paper),
  which gives "much better" agreement (App. A, Fig. A1). For neon no ADAS
  version reproduces NIMROD and M3D-C1. ADAS recombination for Ne$^{4+}$ to
  Ne$^{8+}$ exceeds the fitted ADPAK values by up to an order of magnitude
  at $n_e=10^{21}$ m$^{-3}$, consistent with JOREK's faster recombination
  (Fig. A2; a data comparison, not a rerun).
- They call the agreement evidence of "the robustness of the radiative
  cooling dynamics" despite the different atomic models (§6.2, §7).

## Contradictions

**Coronal-equilibrium delay: model or atomic data** — Open. The factor-2
slower collapse of the JOREK CE run is attributed to the CE assumption by
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§2.7). The residual
differences of the JOREK CR run are attributed to atomic data by
[Hu et al. (2021b)](/sources/hu-2021-b.md) (§6, App. A), and Hu et al.
show that switching ADAS data sets alone moves the argon result toward
NIMROD. The share of the CE gap that comes from atomic data is therefore
not determined. The full entry is on the
[coronal-equilibrium page](/methods/coronal-equilibrium-impurity-model.md).

# Citations

- [Hu et al. (2021b)](/sources/hu-2021-b.md) — §3, §6, §7, Eq. 7, Eq. 18, Figs. 1, 10–17, App. A.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §2.7.

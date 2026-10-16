---
type: Method
title: "Collisional-radiative (non-equilibrium) impurity model"
description: "Impurity model that evolves the charge-state distribution in time with collisional-radiative ionization and recombination rates instead of assuming coronal equilibrium; in JOREK it is carried by fluid-advected super-particles whose radiation, ionization power, effective charge, mean charge and density are projected onto the finite-element fields, and in NIMROD by one fluid density per charge state with KPRAD rates."
status: established
aliases: [non-equilibrium impurity model, CR impurity model, charge-state-resolved impurity model]
tags: [impurities, particles, disruption, mhd, code]
timestamp: 2026-10-16T12:00:00Z
---

# Collisional-radiative (non-equilibrium) impurity model

A non-equilibrium impurity model evolves the density of every charge state
with ionization and recombination rate equations, so that the charge
distribution lags the electron temperature instead of jumping to the
[coronal-equilibrium](/methods/coronal-equilibrium-impurity-model.md) value
([Hu et al. (2021b)](/sources/hu-2021-b.md), §1–2). The rates are
collisional-radiative (CR) effective coefficients from open-ADAS, evaluated
at the local $n_e$ and $T_e$ (§2.2: argon 1989 and neon 1996 data sets).
[M3D-C1](/software/m3d-c1.md) and [NIMROD](/software/nimrod.md) track the
charge-state densities with the KPRAD model and coronal-model (ADPAK)
rates; JOREK adopted the CR treatment in 2021 and has since used it for
SPI studies ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.7;
[Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.2).

## Charge-state rate equation

For an impurity of atomic number $Z_{\mathrm{imp}}$, the densities
$n_{\mathrm{imp},z}$, $z=0,\dots,Z_{\mathrm{imp}}$, obey
$$\frac{d n_{\mathrm{imp},z}}{dt}=n_e\Big[\langle\sigma v\rangle_{\mathrm{ion},z-1}\,n_{\mathrm{imp},z-1}-\big(\langle\sigma v\rangle_{\mathrm{ion},z}+\langle\sigma v\rangle_{\mathrm{rec},z}\big)n_{\mathrm{imp},z}+\langle\sigma v\rangle_{\mathrm{rec},z+1}\,n_{\mathrm{imp},z+1}\Big],$$
with $\langle\sigma v\rangle_{\mathrm{ion},z}$ the ionization coefficient of
state $z\to z+1$ and $\langle\sigma v\rangle_{\mathrm{rec},z}$ the
recombination coefficient of $z\to z-1$
([Hu et al. (2021b)](/sources/hu-2021-b.md), Eq. 4). The printed Eq. 4
multiplies the ionization part of the loss term by the state density
twice, which would make it quadratic; the linear form above is the
intended one (recorded on the Source page). Here $d/dt$ is the time
derivative along the fluid motion. [Hu et al. (2023)](/sources/hu-2023.md)
(Eq. 16) repeat the equation in fractional abundances with the same doubled
factor in print.

## Particle realization in JOREK

[Hu et al. (2021b)](/sources/hu-2021-b.md) (§2) implement the rate
equation on marker particles of JOREK's particle framework:

- **Markers.** Equal-weight super-particles, each standing for
  $10^{14}$–$10^{15}$ atoms; $10^7$ particles represent $10^{21}$–$10^{22}$
  injected atoms (§2.2). New markers are born neutral at the end of each
  fluid step by rejection sampling of the impurity source.
- **Motion.** Markers are not pushed by the Lorentz force; they are
  advected with the local fluid velocity $\mathbf v$, justified by strong
  inter-species friction and charge exchange (§2.1). The pusher has no
  diffusion, a limitation the paper acknowledges. Several particle steps
  are taken per fluid step, with $\Delta t<10^{-8}$ s for the particles.
- **Charge-state array.** Each marker carries the full vector
  $n_{\mathrm{imp},z}$ instead of a single charge number. The authors state
  that this represents ionization and recombination more smoothly and
  allows massive injection with a moderate particle count (§2.2; no
  convergence study shown). This differs from the outlook of
  [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§2.15), which planned
  either one continuity equation per charge state (or bundle of states)
  or particles "the charge of each particle being evolved individually".

## Moments returned to the fluid

Five moments are projected onto the finite-element fields by the
[particle-to-mesh projection](/methods/particle-to-mesh-projection.md)
([Hu et al. (2021b)](/sources/hu-2021-b.md), §2.3):

1. **Ionization power**, accumulated per marker over each particle step
   and divided by the fluid step (Eq. 5):
   $$P_{\mathrm{ion}}=n_e\sum_{z=0}^{Z_{\mathrm{imp}}-1}\Big(\langle\sigma v\rangle_{\mathrm{ion},z}\,n_{\mathrm{imp},z}-\langle\sigma v\rangle_{\mathrm{rec},z+1}\,n_{\mathrm{imp},z+1}\Big)\varepsilon_{\mathrm{ion},z}.$$
   The recombination term returns the ionization energy to the electrons
   when an ion recombines, because the ADAS recombination radiation already
   counts that energy as radiated (§2.3).
2. **Radiated power** (Eq. 6):
   $P_{\mathrm{rad}}=n_e\sum_z n_{\mathrm{imp},z}\big(L_z^{\mathrm{line}}+L_z^{\mathrm{rec}}+L_z^{\mathrm{brems}}\big)(n_e,T_e)$,
   the line, recombination and bremsstrahlung coefficients of state $z$.
3. **Effective charge** $Z_{\mathrm{eff}}$, summed over all species and
   charge states, which enters the Spitzer–Hirshman resistivity (Eq. 7;
   see the [coronal-equilibrium page](/methods/coronal-equilibrium-impurity-model.md))
   and the ion–electron thermalization rate.
4. **Mean impurity charge** $\langle z\rangle$, which sets $n_e$ by
   quasi-neutrality: $n_e$ is the deuterium ion density plus
   $\langle z\rangle n_{\mathrm{imp}}$.
5. **Impurity density** $n_{\mathrm{imp}}$.

The fluid model is JOREK
[reduced MHD](/methods/reduced-mhd.md) with an impurity mass-density
equation (Eq. 11) and either one temperature,
$\partial_tp=\dots-(\Gamma-1)(P_{\mathrm{rad}}+P_{\mathrm{ion}})$
(Eq. 15), or separate ion and electron pressures, the electron equation
carrying the losses and the collisional exchange (Eqs. 16–17).

## Results

On the DIII-D gas-injection case
([benchmark page](/benchmarks/diii-d-mgi-impurity-benchmark.md);
[Hu et al. (2021b)](/sources/hu-2021-b.md), §4–6):

- Against CE (argon, Spitzer-like $\eta$, one temperature), the
  non-equilibrium model cools earlier through weakly ionized states and
  reaches the balance of radiative-plus-ionization cooling with Ohmic
  heating at $t\approx0.7$ ms, which the CE run reaches only very late;
  peak cooling powers are comparable (Fig. 2).
- The mean charge lags CE: low at $t=0.26$ ms, close to CE at $0.45$ ms,
  and higher than CE and less hollow at $0.78$ ms because of slow
  recombination (Fig. 4).
- The impurity density of the fluid equation and of the projected
  particles agree for most of the run; a local deviation at $t=1.10$ ms is
  attributed to the missing diffusion in the pusher (Fig. 5).
- Two temperatures cool the electrons faster than one temperature, much
  more so for neon (§5, Figs. 7–8); after $t\approx0.6$ ms the electron
  thermal energy exceeds the ion thermal energy because $n_e>n_i$ (Fig. 9).
- Compared with NIMROD, integrated cooling, Ohmic power and the 2D
  evolution of $T_e$ and $j_\phi$ agree in shape; the differences are
  attributed to atomic data (§6, App. A).

Cost: the particle part adds from negligible time to tens of seconds per
fluid step late in the run, against about 30 s per fluid step for an
axisymmetric run on 4 nodes of the Tianhe-3 prototype (§2.2). The paper
states that the model "is now ready for production" (§7). All its runs are
axisymmetric; the final current filament survives only because of
axisymmetry, and in 3D it would end by a kink (§6.2).

## KPRAD in NIMROD

The NIMROD runs of [Zeng et al. (2023)](/sources/zeng-2023.md) (§2, Eq. 3,
App. 7) carry one continuity equation per neon charge state ($z=0$–$10$).
Each has convection, a diffusion $\nabla\cdot(D\nabla n_{\mathrm{imp},z})$
and ionization and recombination sources from the KPRAD rates, updated every
time step. KPRAD writes its rates and powers as polynomial fits in
$\log_{10}T_e$:

- line radiation, proportional to $n_e\,n_{\mathrm{imp},z-1}$;
- ionization rates;
- radiative recombination with a Gaunt-like factor;
- bremsstrahlung, proportional to $n_e^2\sqrt{T_e}\,Z_{\mathrm{eff}}$;
- three-body recombination, significant only near $T_e\simeq1$ eV;
- background-impurity radiation from a coronal fit.

The formulas are printed in mixed cgs/eV units (Eqs. 10–21). One temperature
is shared by all species.

Zeng et al. say the KPRAD atomic data "originates from ADAS database"
(App. 7), whereas [Hu et al. (2021b)](/sources/hu-2021-b.md) describe the
NIMROD and M3D-C1 rates as KPRAD-fitted ADPAK coronal-model data. This
difference in attribution can reflect different data versions. It is a
qualification, not a contradiction of a printed equation.

## Later use

[Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (§3.2, Fig. 8) list the CR
treatment, "replacing coronal equilibrium", among the JOREK disruption
developments. The primary study behind the ITER statements below is
[Hu et al. (2023)](/sources/hu-2023.md). Applied to ITER neon–deuterium SPI it shows shards reaching
the core before the edge radiative collapse, a transient transport barrier
of stochastic field lines outside $q=1$ in the early
[thermal quench](/definitions/thermal-quench.md), and core density
transport that depends on where material is deposited relative to the
$q=1$ and $q=2$ surfaces. Particle-in-cell treatment of injected
impurities has been tested only axisymmetrically, and kinetic tungsten
impurities are treated in a hybrid kinetic-fluid approach (§2.2, §3.2).
The axisymmetric-only statement refers to "a further advanced model with a
particle in cell (PiC) treatment of the injected impurities", cited to a
2022 master thesis (Strien). It is not the fluid-advected CR marker model of
this page (compiler's check of the printed review, §3.2, ref. 44). The CR
marker model has run in 3D since 2023, as the next items show.

**3D production use.**

- [Hu et al. (2023)](/sources/hu-2023.md) run the CR model, with marker
  moments projected onto the fields, in 3D two-temperature reduced MHD for
  neon–deuterium SPI into ITER L-mode, with toroidal harmonics $n=0$–11
  (§2.1–2.2).
  - The fragments reach the core before the edge radiative collapse.
  - Assimilation is self-regulated. Non-local ablation, or removing the
    magnetic reduction factor, changes neon assimilation only mildly but
    raises the radiated power strongly (§4.1, Figs. 16, 18).
  - By the end of the 200 m/s run, 25 of 36 MJ are lost, with a radiated
    fraction of "about 80%" (§3.1). The definitions of the energy fractions
    are not stated (recorded on the Source page).
- [Hu et al. (2024)](/sources/hu-2024.md) (§2.1) reuse the same equations
  "without modifications" for dual SPI into ITER baseline and degraded
  H-modes. The radiated fractions range from 49.4% (baseline, full pellet)
  to 89.8% (degraded H-mode, quarter pellet, synchronized injectors)
  (Table 2). The radiation density is ray-traced onto the ITER first wall.
  These SPI dynamics are on [shattered pellet injection](/definitions/shattered-pellet-injection.md).

# Citations

- [Hu et al. (2021b)](/sources/hu-2021-b.md) — §1–7, Eqs. 4–7, 11, 15–17, Figs. 2–9, App. A.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §2.7, §2.15.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §2.2, §3.2, Fig. 8, ref. 44.
- [Hu et al. (2023)](/sources/hu-2023.md) — §2.1–2.2, §3.1, §4.1, Eq. 16.
- [Hu et al. (2024)](/sources/hu-2024.md) — §2.1, Table 2.
- [Zeng et al. (2023)](/sources/zeng-2023.md) — §2, Eq. 3, App. 7 (Eqs. 10–21).

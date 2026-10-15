---
type: Method
title: "Boltzmann-relation electrons"
description: "Electron model that sets the electron density from the potential by the isothermal Boltzmann relation, either inverted under quasi-neutrality for the potential (plume codes) or inserted into a nonlinear Poisson equation; the simplest fluid closure of hybrid plume, ion-thruster and helicon models, valid for collisionless, unmagnetized or field-aligned isothermal electrons."
status: established
aliases: [Boltzmann electrons, Boltzmann relation, isothermal electrons, Boltzmann electron fluid, nonlinear Poisson-Boltzmann]
tags: [hybrid, fluid, plume, ion-thruster, helicon, numerics]
timestamp: 2026-10-15T00:00:00Z
---

# Boltzmann-relation electrons

## Relation

For collisionless, unmagnetized electrons the quasi-neutral momentum balance
reduces to $en_e\mathbf E=-\nabla p_e$ with $p_e=n_eT_e$; at constant $T_e$
it integrates to
$$n_e=n_0\exp\left(\frac{e\phi}{T_e}\right),$$
with $n_0$ the density where $\phi=0$
([Cai et al. (2018)](/sources/cai-2018.md), §2.1, eqs. 7–9, attributed to
Boyd; [Gallo et al. (2021)](/sources/gallo-2021.md), eqs. 9–13). As printed,
Cai et al.'s eq. 9 has no $e$ in the exponent (consistent only with $T_e$ in
eV and $\phi$ in V), and Gallo et al.'s intermediate equations are
sign-inconsistent though their result is the relation above. Along a magnetic
line the same relation follows from the Morozov limit of infinite parallel
mobility ([Ahedo (2023)](/sources/ahedo-2023.md), p. 10; see
[thermalized potential](/definitions/thermalized-potential.md)). It is the
$\gamma=1$ case of the
[polytropic electron closure](/definitions/polytropic-electron-closure.md).

## Two ways to use it

**Quasi-neutral inversion.** With $n_e=n_i$ the potential follows from the
ion density by inverting the relation, and no Poisson equation is solved.
[EX-PWS](/software/ex-pws.md) does this for an ion-thruster plume with
$T_e=3.5$ eV and $n_0=10^{16}$ m$^{-3}$; the magnetic field is neglected, the
cells are required to be larger than $\lambda_D$ (about $10^{-5}$ m), and the
inversion itself is not printed ([Cai et al. (2018)](/sources/cai-2018.md),
§§2.1, 2.3). The resulting potential is negative everywhere relative to the
exit plane, with a maximum drop of tens of volts against beam ions of about
1000 eV (§4.2, Fig. 9).

**Nonlinear Poisson equation.** The relation replaces $n_e$ in Poisson's
equation. In the quasi-1D helicon double-layer model of
[Gallo et al. (2021)](/sources/gallo-2021.md) (§3, eqs. 13–18) the density
is further scaled by the square of the ratio of source radius to local duct
radius (after Chen), the equation is
$\mathrm d^2\phi/\mathrm dx^2=(e/\varepsilon_0)(n_e-n_i)$ with $\phi=0$ at both
ends, $x$ the coordinate along the field line, $n_0$ comes from a global electron balance, and a dedicated scheme
(citing Newton–Kantorovich papers) handles the exponential nonlinearity;
Poisson and particle steps are iterated to convergence of thrust and
specific impulse. In argon at $T_e=10$ eV the potential drop is 12 V; from 5 to
20 eV it rises from 6 to 23 V, and the ionization rate has no significant
effect on it (§4.4, Figs. 10–12). See
[current-free double layer](/definitions/current-free-double-layer.md).

## Applications

* Plume impingement of the LIPS-200 ion thruster on a plate (EX-PWS;
  [Cai et al. (2018)](/sources/cai-2018.md)).
* Quasi-1D helicon channel ([Gallo et al. (2021)](/sources/gallo-2021.md)).
* Gridded-ion extraction hybrids with Boltzmann electrons at fixed $T_e$,
  sometimes in two populations ([Taccogna et al. (2023)](/sources/taccogna-2023.md),
  §III A c, refs. 72, 80).
* Plume hybrids, as the isothermal limit of the polytropic potential law
  ([Taccogna et al. (2023)](/sources/taccogna-2023.md), §IV A, eq. 16).

## Limits

* The isothermal potential falls without bound as the plume density
  vanishes, unlike the finite polytropic limit
  ([Taccogna et al. (2023)](/sources/taccogna-2023.md), §IV A, eq. 16).
* Full-PIC plume runs show density errors of an isothermal-Boltzmann hybrid
  that are relevant in the plume periphery
  ([Taccogna et al. (2023)](/sources/taccogna-2023.md), Figs. 10–11, after
  Wang & Hu).
* In 1D radial PIC of Hall-thruster sheaths with SEE the Boltzmann relation
  breaks down ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.2).
* In the Morozov limit the parallel electron current cannot be computed from
  Ohm's law ([Ahedo (2023)](/sources/ahedo-2023.md), p. 10).

# Citations

1. [Cai et al. (2018)](/sources/cai-2018.md), §§2.1, 2.3, 4.2, eqs. 7–9, Fig. 9.
2. [Gallo et al. (2021)](/sources/gallo-2021.md), §§3, 4.4, eqs. 9–18, Figs. 10–12.
3. [Taccogna et al. (2023)](/sources/taccogna-2023.md), §§III A c, IV A, eq. 16, Figs. 10–11.
4. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.2.
5. [Ahedo (2023)](/sources/ahedo-2023.md), p. 10.

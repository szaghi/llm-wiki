---
type: Definition
title: "Thermalized potential"
description: "Morozov's combination of the electrostatic potential and the electron density, constant along each magnetic line when the electron temperature is uniform along the line and parallel mobility is large; used to reduce the 2D electron fluid problem to a problem across field lines."
status: established
aliases: [thermalized potential, Morozov thermalized potential, Morozov relation, thermalized-potential approximation]
tags: [fluid, hybrid, hall-thruster, numerics]
timestamp: 2026-10-14T00:00:00Z
---

# Thermalized potential

## Definition

With $T_e$ in energy units, the thermalized potential is
$$\phi^*=\phi-\frac{T_e}{e}\ln\frac{n_e}{n_0},$$
where $n_0$ is a reference density
([Ahedo (2023)](/sources/ahedo-2023.md), eq. 34, refs. 26, 27, 37). Taccogna
& Garrigues give the same relation, after Morozov & Savelyev (2000a), solved
for the potential and written with the mean electron energy, which is
$\tfrac32T_e$ ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md),
§2.2, eqs. 24–25):
$$\phi=\phi^*+\frac{T_e}{e}\ln\frac{n_e}{n_0},\qquad\phi^*\ \text{and}\ T_e\ \text{constant along each magnetic line}.$$

## Why it is constant along a line

The parallel electron force balance is dominated by the electric and pressure
terms, $en_e\nabla_\parallel\phi\approx T_e\nabla_\parallel n_e$, because
parallel and perpendicular derivatives differ by a factor of order
$O(10^5)$ in conventional Hall thrusters
([Ahedo (2023)](/sources/ahedo-2023.md), eq. 33). In terms of $\phi^*$
the parallel current is (heavy-species drag current dropped)
$$j_{e,\parallel}=-en_e\mu_\parallel\nabla_\parallel\phi^*+\left(1-\ln\frac{n_e}{n_0}\right)n_e\mu_\parallel\nabla_\parallel T_e$$
([Ahedo (2023)](/sources/ahedo-2023.md), eq. 35). In the Morozov
collisionless limit $\mu_\parallel\to\infty$ both $\nabla_\parallel\phi^*$ and
$\nabla_\parallel T_e$ vanish: field lines are isothermal and the electrons
follow a [Boltzmann relation](/methods/boltzmann-electron-model.md) along each
line (p. 10). The relation of Taccogna & Garrigues assumes the electron energy
is constant along field lines (§2.2).

## Uses and consequences

* It reduces the 2D electron problem to one across the magnetic lines and is
  used with [magnetic-field-aligned meshes](/methods/magnetic-field-aligned-mesh.md)
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.2;
  [Ahedo (2023)](/sources/ahedo-2023.md), §3).
* Equipotentials are not aligned with $\mathbf B$, because of the density
  term. In a 2D $r$–$z$ hybrid of a Hall thruster they follow the field lines
  in the plume but form a concave lens in the channel
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.5, Fig. 4,
  after Bareilles et al. 2003). In HYPHEN runs of a magnetically shielded
  thruster the lines are near-isothermal and $\nabla_\parallel\phi^*$ is
  small, while isopotentials are not aligned with the lines
  ([Ahedo (2023)](/sources/ahedo-2023.md), Fig. 1).
* 2D field-aligned calculations confirm that the potential is thermalized
  except in the near plume close to the cathode
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.2, after
  Mikellides & Katz 2012).

## Limitation

In the limit $\mu_\parallel\to\infty$ the parallel current cannot be computed
from Ohm's law. Ahedo states this drawback for the models that use the limit
([Ahedo (2023)](/sources/ahedo-2023.md), p. 10, refs. 13, 27, 34, 37).

## Polytropic variant

For collisionless polytropic electrons (index $\gamma$) in a 2D magnetic
nozzle the conserved quantity along each line is instead
$\phi-\frac{\gamma}{\gamma-1}\frac{T_e}{e}$, and the electron current is
determined without an Ohm's law
([Ahedo (2023)](/sources/ahedo-2023.md), eqs. 54–60; see
[polytropic electron closure](/definitions/polytropic-electron-closure.md)
and [magnetic nozzle](/definitions/magnetic-nozzle.md)). The
EP2PLUS code ([hybrid PIC–fluid model](/methods/hybrid-pic-fluid-model.md)) solves an elliptic equation for this
polytropic potential (eqs. 68–72).

# Citations

1. [Ahedo (2023)](/sources/ahedo-2023.md), §3, eqs. 33–35, 54–60, 68–72, p. 10, Fig. 1.
2. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §§2.2, 2.5, eqs. 24–25, Fig. 4.

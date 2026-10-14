---
type: Method
title: "Reduced-order (pseudo-2D) PIC"
description: "Particle-in-cell scheme that replaces the 2D Poisson problem by 1D Poisson problems on region-averaged charge densities and approximates the potential as a sum of one-dimensional potentials, cutting cell and particle counts toward those of a 1D run."
status: established
aliases: [pseudo-2D PIC, reduced-order particle-in-cell, quasi-3D PIC, Poisson-decomposition PIC]
tags: [pic, kinetic, numerics, hall-thruster, performance]
timestamp: 2026-10-14T00:00:00Z
---

# Reduced-order (pseudo-2D) PIC

Reduced-order PIC keeps the particle part of [PIC-MCC](/methods/pic-mcc.md)
(particles move in 3V, in the full plane or volume) and replaces the
multi-dimensional field solve by one-dimensional ones. The scheme was
introduced by Faraji, Reza & Knoll (2022) and developed by the Imperial
Plasma Propulsion Laboratory group; this bundle has not ingested that paper,
and the descriptions below come from its later users and from a review.

## Formulation

* **Decomposition.** At the intersection of a horizontal region and a
  vertical region, the 2D potential $\phi(x,y)$ is approximated as a weighted
  sum of a potential that depends on $x$ alone and one that depends on $y$
  alone, each weight constant in its region. Each 1D potential obeys a 1D
  Poisson equation whose source is the charge density averaged across the
  region, $\frac1{L_y}\int_0^{L_y}\rho_c(x,y)\,dy$ for the $x$-problem and
  $\frac1{L_x}\int_0^{L_x}\rho_c(x,y)\,dx$ for the $y$-problem, scaled by the
  region weight. The result is a decoupled pair of 1D ODEs, each solved with
  the Thomas tridiagonal algorithm on cells that span the full width of their
  region ([Reza et al. (2022)](/sources/reza-2022.md), §2.1, Eqs. 1–7, Fig. 1).
* **Single- and multi-region variants.** "Single-region" means one horizontal
  and one vertical region. It gives the largest cost reduction and amounts to
  capturing an *average* effect of the second direction in an otherwise 1D
  run. A "double-region" variant improved axial–azimuthal predictions in the
  original paper ([Reza et al. (2022)](/sources/reza-2022.md), §2.1, §6).
* **Weights.** Reza et al. use weight 0.5 for both 1D potentials in every
  run. They report that the original sensitivity study, done for the
  axial–azimuthal plane only, found predictions and stability "almost
  invariant" as long as the vertical weight is at least the horizontal one;
  for the azimuthal–radial and axial–radial planes equal weights were adopted
  by analogy, without a dedicated study
  ([Reza et al. (2022)](/sources/reza-2022.md), §2.1).
* **Partially coupled variant.** [Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md),
  "PlasmaSim 2D", Eqs. 1–5, insert the unweighted ansatz "potential = function
  of $x$ + function of $y$" into Poisson's equation and integrate once along
  each direction. Each resulting 1D equation keeps the boundary values of the
  other potential's first derivative, so the two ODEs are partially coupled;
  the system has $N+N$ algebraic equations instead of $N\times N$. Dielectric
  walls enter as a surface-charge Neumann condition scaled by a dimensionless
  wall capacitance (value 5, Table 1); second derivatives use centred
  differences and boundary first derivatives one-sided ones. The authors
  state that this is more accurate than the fully decoupled version, without
  an accuracy test in this paper, and attribute the method to A. Knoll.
* **Review description.** [Taccogna et al. (2023)](/sources/taccogna-2023.md),
  Sec. V C c, Eq. 21, Fig. 19, describe the potential as the sum of a
  function of $x$ and a function of $y$ per region of a coarse grid, solved
  as two 1D problems sharing the particles, with cells and particles reduced
  from $O(N^d)$ to $O(dN)$ for $N$ points per direction in $d$ dimensions.
* **Maturity.** Reza et al. call the formulation "preliminary", "not yet
  mature" and lacking "a rigorous mathematical framework", and announce a
  generalized formulation ([Reza et al. (2022)](/sources/reza-2022.md), §1, §6).

## Cost

* [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. V C c and
  Conclusions, report a speed-up of up to 50 over 2D PIC and an expected
  quasi-3D speed-up over full 3D of about 2500 ("order of $10^3$"), with an
  accuracy that depends on how fine the coarse grid is ("problem-dependant").
* [Reza et al. (2022)](/sources/reza-2022.md), §2.1, restate from the
  original paper "up to two orders of magnitude reduction in the
  computational cost, effectively to that equivalent of a 1D PIC simulation",
  and that full-size thrusters can be run "without any speed-up factor"
  (§3.2). They report no wall-clock time. The two figures (≤50 and ~100)
  are both attributed to the originators' work and are of the same order;
  neither source measures it.
* [Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md) report that a pseudo-2D
  axial–radial run takes about $10^6$ times the computing time of their 0D
  model per simulated µs, and that one 2D run "can still require several
  weeks" for 10 µs on a shared-memory (OpenMP) machine (§"Combining…",
  "Software").

## Accuracy in the three Hall-thruster planes

All from [Reza et al. (2022)](/sources/reza-2022.md), single-region,
real-scale (no [permittivity or mass scaling](/methods/pic-acceleration-scaling.md)).
In the axial–azimuthal and axial–radial runs $x$ is axial and $y$ azimuthal
or radial, so $E_x$ is the axial field.
* **Axial–azimuthal** (§3.2, Figs. 3, 5, 6). On the
  [axial–azimuthal benchmark](/benchmarks/axial-azimuthal-pic-benchmark.md),
  time-averaged $E_x$, $n_i$, $\phi$ and $T_e$ are "consistent with" the 2D
  reference without any [anomalous-transport](/definitions/anomalous-electron-transport.md)
  model; a 1D axial run without anomalous collisions cannot sustain the
  potential. No error metric is printed; the reader's plot readings put the
  peak $E_x$ slightly downstream of the 2D one and the plume $T_e$ at
  2.5 cm at about 18 eV against about 12 eV. The azimuthal spectrum follows
  the ion-acoustic dispersion relation (≈3 MHz, ≈2 mm; see
  [electron drift instability](/definitions/electron-drift-instability.md)),
  and the magnetic-force term of the azimuthal electron momentum budget is
  "remarkably similar" to the 2D one.
* **Azimuthal–radial** (§4.3, Figs. 8–11, images missing in the preprint
  read). Unlike a 1D radial run, the pseudo-2D run couples the azimuthal
  instability to the [secondary-electron-emission](/definitions/secondary-electron-emission.md)
  sheath: transition to space-charge saturation at about 1 µs, bursts of
  secondary electrons, [near-wall conductivity](/definitions/near-wall-conductivity.md),
  and lower wave energy and mobility than a 1D azimuthal run. The ≈0.7 µs
  oscillations in mobility and $T_e$ are flagged by the authors as an
  artefact of the finite virtual axial length and periodic reinjection.
* **Axial–radial** (§5.2, Figs. 12–14). Resolving the walls (Vaughan SEE)
  improves $T_e$, ionization-rate and $n_i$ profiles against a 2D hybrid
  reference, but the single-region run produces an "unrealistic anode sheath
  with high potential drop" and overpredicts $E_x$. The authors attribute
  this to radial wall physics driven by axially averaged bulk conditions,
  which overpredicts wall-induced electron mobility near the anode, and
  conclude that single-region is not the right choice for this plane. All
  axial–radial runs, pseudo-2D included, use the same Bohm-type mobility,
  so agreement was "expected" to be governed by it (§5); the claim that
  the scheme obviates ad-hoc transport models holds for the axial–azimuthal
  plane only.

## Applications

* Imperial Plasma Propulsion Laboratory PIC code (Julia), all three planes
  ([Reza et al. (2022)](/sources/reza-2022.md), §2).
* PlasmaSim (C++/Unreal Engine), axial–radial model of the water- and
  oxygen-fed WET-HET Hall thruster, with a Bohm-type anomalous collision
  frequency $\alpha_{\mathrm B}=0.01$ ([Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md),
  Eq. 7, Table 1).

# Citations

1. [Reza et al. (2022)](/sources/reza-2022.md) — §1, §2.1 (Eqs. 1–7), §3.2, §4.3, §5, §6.
2. [Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md) — "PlasmaSim 2D" (Eqs. 1–5, 7), Table 1, run-time statements.
3. [Taccogna et al. (2023)](/sources/taccogna-2023.md) — Sec. V C c (Eq. 21, Fig. 19), Conclusions.

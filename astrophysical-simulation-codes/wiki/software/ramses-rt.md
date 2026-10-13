---
type: Software
title: "RAMSES-RT (radiation hydrodynamics in RAMSES)"
description: "Multigroup radiative transfer of ionizing photons built into the cell-based oct-tree AMR code RAMSES: M1-closed photon-number moment equations advanced by an explicit first-order HLL or global Lax–Friedrichs scheme under a reduced speed of light, operator-split from a quasi-implicit non-equilibrium H/He thermochemistry, and multi-stepped across AMR levels with the hydrodynamics so that photons are conserved."
status: established
aliases: [RAMSES-RT, RAMSES RT]
tags: [software, radiation, reduced-speed-of-light, amr, hydro, cosmology, verification, chemistry, cooling]
timestamp: 2026-10-12T00:00:00Z
---

# RAMSES-RT

RAMSES-RT adds multigroup radiative transfer of hydrogen- and helium-ionizing
photons to the cell-based oct-tree AMR code RAMSES (Teyssier 2002), coupled to
the gas through non-equilibrium thermochemistry
([Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §1–§5).

## Code

* No repository URL, licence, version number or language is printed.
  Parallelism reuses "the MPI strategies already in place in RAMSES"; there is
  no threading or GPU in RAMSES-RT. The sibling code ATON is a CUDA GPU M1 code
  on Cartesian grids (§1.2, §5.2).

## Radiation equations

See [M1 radiation transport](/methods/m1-radiation-transport.md).
* The first two angular moments of the transfer equation, in photon number,
  integrated over frequency groups (§2, eqs. 3–7). For each group:

  $$\partial_t N_{\mathrm{ph}} + \nabla\cdot\mathbf F_{\mathrm{ph}} = -(\text{absorption}) + (\text{stellar injection}) + (\text{recombination emission}),\qquad
  \partial_t\mathbf F_{\mathrm{ph}} + c^2\nabla\cdot\left(\mathsf f_{\mathrm E}N_{\mathrm{ph}}\right) = -(\text{absorption}),$$

  with absorption by H I, He I and He II at group-averaged cross sections.
  Group cross sections and energies are global averages over an assumed source
  spectrum, set by hand or computed on the fly from spectral tables (eqs.
  9–11, App. B).
* **M1 closure** (§2, eqs. 12–14):
  $\mathsf f_{\mathrm E} = \tfrac{1-\chi_{\mathrm E}}{2}\mathsf I + \tfrac{3\chi_{\mathrm E}-1}{2}\hat{\mathbf n}\hat{\mathbf n}$,
  $\chi_{\mathrm E} = \frac{3+4f_{\mathrm r}^2}{5+2\sqrt{4-3f_{\mathrm r}^2}}$,
  with $f_{\mathrm r} = |\mathbf F_{\mathrm{ph}}|/(cN_{\mathrm{ph}})$ in $[0,1]$.
  The closure is local, so the system is hyperbolic with wave speeds at most
  $c$ (§1.1.2). Known failure: opposing beams cannot cross and produce a
  spurious perpendicular source (Fig. 1).

## Transport scheme

* Explicit conservative update with $u = (N_{\mathrm{ph}}, \mathbf F_{\mathrm{ph}})$,
  **first order in space and time**, without reconstruction (§3.2, eqs. 20–22;
  §7). See [approximate Riemann solvers](/methods/approximate-riemann-solvers.md).
* **HLL flux** (eq. 23), with the eigenvalues of the M1 flux Jacobian, which
  depend only on $f_{\mathrm r}$ and the angle of the flux to the interface,
  taken from the table of González, Audit & Huynh (2007).
* **Global Lax–Friedrichs flux** (eq. 24),
  $\hat f_{i+1/2} = \frac{\mathbf f(u_i) + \mathbf f(u_{i+1})}{2} - \frac{c}{2}(u_{i+1}-u_i)$,
  i.e. HLL with wave speeds $\pm c$. It is more diffusive and roughly isotropic
  around point sources; HLL keeps axis-aligned beams and shadows but makes
  isotropic sources anisotropic, and diagonal beams leak with both. The two
  cost the same; GLF is the default for cosmological and galactic runs.
* **Courant condition** (§4.1, eq. 31): $\Delta t < h/(3c)$ in 3D; tests use
  $\Delta t = 0.8\,h/(3\hat c)$ (§6, eq. 45). The light-speed limit is
  "typically 300 times shorter" than the hydro step. Implicit transport is
  rejected because accuracy still needs a trial-and-error global step and it
  requires iterative matrix solves.

## Reduced speed of light

See [reduced speed of light](/definitions/reduced-speed-of-light.md)
([Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §4.2, Table 1).
* From the Strömgren-sphere ionization-front solution with finite light speed
  (after Shapiro et al. 2006), the front follows the infinite-$c$ solution
  after one light-crossing time. Reducing $c$ by $f_c$ multiplies the effective
  crossing-to-recombination time ratio by $1/f_c$. The recipe: $f_c$ equal to 1
  or about ten light-crossing times divided by the simulated time, whichever is
  smaller.
* Minimum $f_c$ (Table 1): Milky Way ISM $3\times10^{-2}$, Milky Way cloud
  $6\times10^{-4}$, Iliev tests 1, 2, 5 $2\times10^{-2}$, Iliev test 4 (IGM
  reionization) 1. Galaxy-scale ISM work tolerates $f_c\simeq10^{-4}$–$10^{-3}$
  (§4.3); IGM reionization needs the true $c$, better done on GPUs with ATON.

## Coupling to the gas

* **Operator splitting** (§3): per group and step, injection, then transport,
  then thermochemistry; thermochemistry is likewise split from the Euler
  equations (§5).
* **Thermochemistry** (§3.3, App. A): photon densities and fluxes, thermal
  energy and the H II, He II and He III fractions are updated sequentially in a
  fixed order after Anninos et al. (1997), each semi-implicitly. A **10% rule**
  redoes a sub-step with half the step if any quantity changes by more than
  10% and doubles the next one below 5%. Photons are therefore conserved only
  "at the 10% level" in the thermochemistry; the transport step itself is
  photon-conserving.
* **On-the-spot approximation** (optional, §3.3.2): drops recombination
  emission and switches to case-B rates.
* **Smoothed RT** (§4.4, eqs. 34–37): the thermochemistry starts from the
  pre-injection, pre-transport state and receives the transport and injection
  increments as constant rates; in a cosmological zoom this cuts
  thermochemistry subcycles 6× and wall time 3.5×.
* **Hydro** (§5): a second-order Godunov (MUSCL) solver for the Euler
  equations with a gravity source and thermochemistry; the hydro Riemann solver
  is not specified. Super-comoving variables are extended to the radiation;
  redshift dilution of photon energy is not included, and with the RSLA
  photons are over-diluted (§5.4).

## Mesh and time stepping

See [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
([Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §5).
* The basic element is the oct ($2\times2\times2$ cells); the mesh is a
  cell-based recursive tree, uniformly refined to a minimum level and
  adaptively beyond, with $r_{\mathrm{ref}}=2$ and 2:1 grading ("the resolution
  must never change by more than one level across cell boundaries").
* **Multi-stepping** (§5.1, Fig. 5): two substeps on level $l+1$ per step on
  $l$; fluxes across a coarse–fine interface partially update the coarse
  neighbour, so the coarse state is ill-defined until its step completes
  (App. D).
* **RT on AMR** (§5.2, App. D): RT is **not** subcycled within the hydro step,
  because the partial coarse–fine updates leave states where thermochemistry is
  ill-defined; App. D argues conservative subcycling is "not possible (or at
  least nontrivial)". Each level instead runs injection, hydro, RT transport
  and thermochemistry over the same $\Delta t_l$, the minimum of the hydro and
  RT limits, so RT is multi-stepped across levels like the hydro and photons
  are conserved across levels. Newly refined cells take straight injection or
  linear interpolation; optional refinement acts on photon density, ion
  fractions and their gradients.
* **Memory** (§5.2): storage for the state grows by a factor of about 3.5 for
  3 groups.
* **Transport across levels** (§5.3, Figs. 7–8): beams crossing static
  refinement keep total flux constant to "about 1 in $10^4$" (oblique beam) and
  "to the number precision" (horizontal beam with HLL); with on-the-fly
  refinement on photon-density gradients the discrepancy is within 0.03%.

## Verification

From [Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §6; defaults are
hydrogen-only gas, smoothed RT, GLF, on-the-spot and $f_c=1/100$, with three
groups approximating a $10^5$ K blackbody. All comparisons are code-to-code
(against C²-Ray and the Iliev et al. codes) or against analytic front
positions; no convergence order or error norm is reported.
* Iliev et al. (2006) tests 0–4: single-zone photoionization and cooling, the
  isothermal Strömgren sphere (matches C²-Ray and the analytic solution; AMR
  run at 30% of the uniform time), the Strömgren sphere with heating, shadowing
  by a dense clump (reproduced with HLL; eroded with GLF or without the
  on-the-spot approximation), and multiple sources in a cosmological field
  (with $f_c=1$ the fronts lag C²-Ray).
* Iliev et al. (2009) tests 5–7: H II region expansion (front position and
  speed "virtually identical" to the reference), expansion in an
  inverse-square density profile, and a photo-evaporating clump (GLF loses the shadow after about
  40 Myr; a slight hexagonal grid artefact).
* Beam and point-source transport tests, including the crossing-beams failure
  of M1 (§3.2, Fig. 1).

## Limitations and open items

* Transport is first order; a second-order (MUSCL-type) solver, optional RT
  subcycling at the cost of strict photon conservation, coupling with ATON for
  full-$c$ coarse transport, radiation pressure on dust and further photon
  groups are listed as future work (§7).
* No strong- or weak-scaling numbers or parallel efficiencies are given.

# Citations

1. [Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §§1–7, App. A, D (arXiv v2).

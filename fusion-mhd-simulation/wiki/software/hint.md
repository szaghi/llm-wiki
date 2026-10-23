---
type: Software
title: "HINT"
description: "Three-dimensional MHD equilibrium code that does not assume nested flux surfaces, so it represents islands and stochastic regions; it supplies the high-beta LHD equilibria, with a stochastic layer outside the last closed surface, from which MIPS and MEGA start, VMEC being re-solved inside its last closed surface for Boozer coordinates and Mercier analysis."
status: established
aliases: [HINT2, HINT code]
tags: [equilibrium, stellarator]
timestamp: 2026-10-16T18:35:00Z
---

# HINT

HINT is a three-dimensional MHD equilibrium code for helical systems that,
unlike the [inverse equilibrium solvers](/methods/inverse-equilibrium-solvers.md)
VMEC, DESC and GVEC, does **not assume nested flux surfaces**
([Sato & Todo (2026)](/sources/sato-2026.md), p. 3, citing Suzuki et al.
2006 for HINT2). It can therefore represent magnetic islands and stochastic
field regions. [Panici et al. (2023)](/sources/panici-2023.md) (§2) list
HINT2, with PIES, SIESTA, SPEC and BETAS/NSTAB, among the codes that can
represent islands, in contrast to the nested-surface codes they compare
(VMEC and DESC). Neither source describes HINT's algorithm, discretization
or convergence; this page records only its role in the bundle's sources.

## Use for high-beta LHD equilibria

[Sato & Todo (2026)](/sources/sato-2026.md) (p. 3, Fig. 1) compute the
initial states of their [MIPS](/software/mips.md) and [MEGA](/software/mega.md)
simulations of inward-shifted LHD plasmas with HINT:

* **Profiles.** The pressure is $p=p_0(1-\psi_{t,N})$, linear in the
  normalized toroidal flux, with central beta $\beta_0=7.5\,\%$ and
  $9.2\,\%$.
* **Stochastic edge.** A stochastic region forms outside the last closed
  flux surface (LCFS); as β rises it grows and the nested core shrinks.
  The nested-surface assumption of an inverse solver would exclude this
  region by construction.
* **Cross-check with VMEC.** Inside the HINT LCFS the equilibrium is
  re-solved with [VMEC](/software/vmec.md); the $\iota$ and pressure
  profiles of the two codes overlap (Fig. 1). VMEC then provides what HINT
  does not: Boozer coordinates (via NEWBOZ) for the Fourier analysis of
  the cylindrical simulation data and the Mercier evaluation, which shows a
  Mercier-stable core (magnetic well from the large Shafranov shift) and a
  Mercier-unstable outer region (magnetic hill) (p. 3; see
  [interchange modes and the Mercier criterion](/definitions/interchange-mode.md)).
* **Kinetic loading.** For the runs with
  [kinetic thermal ions](/methods/kinetic-thermal-ions.md) the HINT pressure
  is split as $p_e=p_{\perp i}=p_{\parallel i}=p_{\rm HINT}/2$ with a
  Maxwellian ion distribution of uniform density; with energetic ions the
  energetic-particle pressure is first subtracted from $p_{\rm HINT}$ and
  the remainder split in the same way (p. 6, p. 8; $p_{\rm HINT}$
  page-local, the total HINT pressure).

The resulting simulations, in which conventional MHD collapses the core
and kinetic thermal ions do not, are summarized on
[kinetic thermal ions confine LHD pressure-driven activity to the periphery](/results/kinetic-ions-prevent-core-collapse-lhd.md).

## Limits of the record

* No HINT benchmark, resolution or run time is reported in the bundle's
  sources; the HINT–VMEC agreement of Fig. 1 of Sato & Todo (2026) is the
  only quantitative check, and it is restricted to the region inside the
  LCFS where both codes apply.
* Whether the stochastic layer outside the LCFS takes part in the
  simulated dynamics is not discussed (compiler's observation): the MIPS
  and MEGA perturbations of velocity, pressure and density are held at
  zero in the vacuum region surrounding the plasma, and the source does
  not say where that region begins relative to the LCFS (p. 2–3).

# Citations

* [Sato & Todo (2026)](/sources/sato-2026.md) — HINT equilibria of high-beta LHD, stochastic edge, VMEC re-solve and Boozer transformation, kinetic loading.
* [Panici et al. (2023)](/sources/panici-2023.md) — HINT2 among the equilibrium codes that can represent islands.

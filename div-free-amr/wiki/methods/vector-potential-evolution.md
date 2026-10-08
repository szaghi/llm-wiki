---
type: Method
title: "Vector-potential evolution"
description: "Evolves the magnetic vector potential instead of the field; B = curl A is exactly divergence-free on any grid, and AMR transfer acts on the unconstrained potential."
status: established
aliases: [A-method, potential-based CT]
tags: [vector-potential, constrained-transport, amr, grmhd]
timestamp: 2026-10-08T00:00:00Z
---

# Vector-potential evolution

Evolve $A_h \in V_h^1$ (edge-collocated) by the uncurled induction
equation and *define* the field as
$$B_h = C_h A_h,$$
so $D_h B_h = 0$ holds identically by $D_h C_h = 0$
([notation](/notation.md)) — on every grid, level, and interface, with no
constraint machinery at all. The modern AMR form is
[Etienne, Liu & Shapiro (2010)](/sources/etienne-2010.md) for GRMHD; on
uniform grids it is numerically equivalent to staggered
[constrained transport](/methods/constrained-transport.md), of which it is
the potential-level parametrization.

## Why it wins at AMR — and what it costs

* **Transfer without $P_D$**: the potential is unconstrained, so
  prolongation and restriction can use *any* interpolation — the entire
  divergence-preserving-transfer problem
  ([$P_D$](/operators/divergence-free-prolongation.md),
  [locality limits](/results/transfer-operator-locality-limits.md)) is
  dissolved rather than solved, by the exactness converse: every
  solenoidal field is a curl, so transfer the preimage. *The converse is a
  staggered-complex property.* On collocated tensor-product SBP grids,
  grid-oscillation modes are discretely solenoidal without being curls
  ([Ranocha, Ostaszewski & Heinisch (2020)](/sources/ranocha-2020.md)). A collocated field
  carrying them has no potential to transfer, although potential-evolved
  fields never contain them.
* **The historical costs return**: evolving $A$ was the *original* CT-era
  alternative, and [Evans & Hawley (1988)](/sources/evans-hawley-1988.md)
  rejected it on uniform grids because the Lorentz force needs *second*
  differences of $A$, generating anomalous currents under limited
  reconstruction. The modern HRSC formulations evolve $A$ with the same
  shock-capturing machinery as the fluid, mitigating but not erasing the
  extra-derivative concern.
* **Gauge dynamics is the new constraint — diagnosed and priced**: in the
  simple algebraic gauge the $A$-system carries a **static (zero-speed)
  gauge mode**; interpolation errors at refinement boundaries excite it in
  place, and the result is *spurious magnetic fields at interfaces* —
  divergence-free by construction, and wrong — that grow until the run
  fails. The cure is spectral, not accuracy: the **Lorenz gauge** has only
  propagating modes, so interface noise leaves the grid
  ([Etienne et al. (2012)](/sources/etienne-2012.md)). Note the moral for
  this bundle: exact constraint satisfaction does not certify a correct
  field — the constraint-consistent error channel simply moves elsewhere.

## Collocated high-order realization

[Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md) evolve the potential on the
*same* collocated mesh as all other variables. They build on the
unstaggered CT of Helzel et al. and Rossmanith, which this bundle has
not ingested.
* **Predictor–corrector per stage.** The base fifth-order FD-WENO scheme
  predicts $B^*$. The potential is advanced alongside it, with the velocity
  frozen at the stage. Then $B^*$ is replaced by
  $B_h = C_h^{\mathrm{c}} A_h$, built from fourth-order central differences.
  The total energy is kept, not the pressure.
  The constraint held is $D_h^{\mathrm{c}} B_h = 0$
  ([exact discrete divergence](/properties/exact-discrete-divergence.md)).
* **Gauge and hyperbolicity.** In the Weyl gauge (scalar potential zero),
  the 3D potential system is non-conservative and only *weakly*
  hyperbolic: eigenvectors are incomplete in four directions. In 2D it
  reduces to strongly hyperbolic advection of a scalar $A_z$.
* **The answer to the second-derivative objection.** The potential
  equation is treated as a Hamilton–Jacobi equation. WENO weights are
  computed from the *derivatives* of $A$, which are the field, so
  oscillations are limited where Evans and Hawley located the problem.
* **Missing dissipation is added by hand.** In 3D the upwinding supplies
  resistivity in only two of three directions. A smoothness-switched
  artificial resistivity fills the third. It is $O(\Delta x^6)$ on smooth
  data, and its coefficient $\nu \in [0.02, 0.2]$ is tuned.
* **Scope.** Fourth order in space and time (10-stage SSP-RK4, CFL 3) on
  uniform or smoothly mapped grids. AMR is future work. The authors flag
  that a many-stage integrator enlarges ghost regions and inter-patch
  communication.

The compiler's reading: the Weyl gauge, like the algebraic gauge diagnosed
by Etienne et al., leaves a non-propagating sector. Here it is controlled
by added resistivity on a uniform grid. Whether interface noise excites it
under AMR is untested.

## A moving-mesh failure (preprint evidence)

The Arepo-CT scheme of Mocz et al. (2016) evolves a cell-averaged
potential on a moving Voronoi mesh, in the Weyl gauge. Fluxes through
Delaunay faces are contour integrals of the potential, so every Delaunay
tetrahedron is exactly divergence-free. In driven subsonic turbulence it
is unstable at high resolution: granular artifacts at $128^3$, and at
$256^3$ excess tails in field, velocity and density that no other scheme
shows. The authors advise against production use. Their diagnosis:
* the potential is not a conserved quantity, and its advection term can
  dominate the electric-field source;
* cell averaging and the curl do not commute, so cell geometry injects
  local errors into $B$;
* Delaunay flips change the reconstructed field discontinuously;
* the electric-field source is cell-centred and not upwinded, which is
  known to destabilize CT even on fixed meshes;
* the formulation is not Galilean-invariant.

A stable, Galilean-invariant moving-mesh CT is stated as still open
([Pakmor et al. (2026)](/sources/pakmor-2026.md) §6.3, preprint).
*Compiler reading:* this is a second instance of the moral above. Exact
satisfaction of the constraint certified neither stability nor a correct
field.

The trade is precise: CT holds the invariant on the *field* and pays at
interfaces (EMF corrections, $P_D$); the potential route holds it by
*construction* and pays in derivative count and gauge control.

# Citations

1. [Etienne, Liu & Shapiro (2010)](/sources/etienne-2010.md), §§I–III.
2. [Evans & Hawley (1988)](/sources/evans-hawley-1988.md), §III (the second-derivative objection).
3. [Etienne et al. (2012)](/sources/etienne-2012.md), §§I–III, V.
4. [Etienne et al. (2015)](/sources/etienne-2015.md) — production form: damped generalized Lorenz gauge $\nabla_\mu A^\mu = \xi n_\mu A^\mu$ (transport *and* damping for the gauge sector, mirroring GLM's design).
5. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §§2–6.
6. [Ranocha, Ostaszewski & Heinisch (2020)](/sources/ranocha-2020.md), Theorems 3.8, 3.19.
7. [Pakmor et al. (2026)](/sources/pakmor-2026.md), §6.3 (preprint).

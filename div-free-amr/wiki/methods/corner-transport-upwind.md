---
type: Method
title: "Corner transport upwind (CTU)"
description: "Colella's single-step, dimensionally unsplit Godunov integrator: edge states carry a transverse correction for transport across zone corners, which raises the stability limit to a per-direction Courant number of 1; constraint-agnostic, so its MHD uses pair it with CT or GLM."
status: established
aliases: [CTU, corner-transport upwind, unsplit Godunov]
tags: [ctu, unsplit, godunov, shock-capturing]
timestamp: 2026-10-13T00:00:00Z
---

# Corner transport upwind (CTU)

A dimensionally unsplit, conservative, second-order Godunov method in
which every edge flux is computed from edge states that already account
for transverse transport. It is introduced, named and extended to systems
by [Colella (1990)](/sources/colella-1990.md). The primary source is pure
hydrodynamics: it contains no magnetic field and no divergence
constraint.

## Construction

**First order** (§1, eqs. 1.2–1.4, Figs. 1–2). For scalar advection the
new zone value is the area-weighted average of the four upstream zones
swept by the velocity, which includes the zone diagonally upstream. In
conservation form, each edge value is the upstream zone value corrected
by half a time step of transport in the *transverse* direction. Donor
cell is the same update without that correction. The name records that
"it takes into account the effect of information propagating across
corners of zones in calculating the flux" (p. 174). Edge values are
nonnegative-weight sums of zone values, so the scheme obeys a maximum
principle.

**Stability** (eqs. 1.5–1.6). CTU is stable when the Courant number in
each direction separately is at most 1 (eq. 1.5, sufficient); donor cell
needs the sum of the two directional Courant numbers to be at most 1
(eq. 1.6, necessary). Dropping the transverse correction "is always
destabilizing" (p. 175).

**Second order** (eqs. 1.7–1.9). A predictor–corrector: the edge state
adds a limited normal slope (van Leer's monotonized central difference)
to the transverse correction. The transverse derivative is an unlimited
upwind difference; full limiting of the normal slopes recovers
first-order CTU. Second order in smooth regions by a linear error
analysis, with no amplified Fourier mode under eq. 1.5 (p. 176).

**Systems** (§2). Four steps: limited slopes, time-centred left and right
edge states (componentwise, at each edge), a Riemann problem normal to the
edge, conservative differencing of the edge fluxes in both directions.
* Slopes are limited in characteristic variables (eqs. 2.5–2.6).
* The normal predictor is characteristic tracing: wave families that do
  not reach the edge in half a step are discarded by a projection onto
  the incoming characteristics (eqs. 2.10–2.12), "essentially" the 1D
  tracing of Colella & Woodward (p. 182;
  [PPM](/methods/ppm.md)).
* The transverse correction is a difference of Godunov fluxes from
  transverse Riemann problems (eq. 2.14). Zone values as their states
  (eq. 2.13) give second order; the predicted edge states (eq. 2.15) are
  needed at strong discontinuities oblique to the grid and are
  "essential" in the double Mach reflection (pp. 197–198).
* **CFL for systems** (eq. 2.17):
  $$\max_k \frac{|\lambda_k|\,\Delta t}{h} \le 1,$$
  taken in each direction with that direction's speeds and spacing. It is
  necessary and sufficient for Fourier stability only when the two flux
  Jacobians commute. Colella states that he has not proven it for any
  problem with non-commuting Jacobians, and uses it for all gas-dynamics
  runs with "no evidence of instability" (p. 183).

For 1D problems aligned with a grid direction the scheme reduces to the
1D second-order Godunov method (design criterion 1, p. 173). Mapped
quadrilateral grids (§3) and gas dynamics with multidimensional
flattening and reflecting walls (§4) are treated in the same paper; its
domain of dependence needs 4 ghost cells per side (p. 193).

## Cost and the 3D variants

* **2D.** Twice the Riemann solutions of operator splitting, about 50%
  more run time; resolution "essentially identical" to the split scheme
  on the double Mach reflection (§§5–6).
* **3D** (§6, p. 199). The analogue of the first-order scheme that keeps
  all three design criteria needs **12 Riemann solutions per zone per
  time step**, against 3 for operator splitting. Relaxing the maximum
  principle, with donor-cell-type transverse predictors that ignore
  transport from zones offset in all three directions (third-order
  truncation terms), needs **6**. Which is appropriate is "undoubtedly
  problem dependent".
* These are the **12-solve and 6-solve CTU** of the MHD codes below; both
  counts are printed first in Colella (1990).
  [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md) describe
  12-solve as "Saltzman-complete" and assess the two variants on a 3D
  MHD suite.

## Uses in this bundle

CTU is **constraint-agnostic**: divergence control in its MHD uses comes
from the paired mechanism, never from the integrator.
* **With staggered CT.** Athena: PPM interface states, CTU and the
  upwind-biased $\mathcal{E}^c$ edge EMF
  ([Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md), 2D;
  [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md), 3D;
  [Stone et al. (2008)](/sources/stone-2008.md), where CTU+CT is the
  default and less diffusive than VL+CT;
  [constrained transport](/methods/constrained-transport.md)). CHARM uses
  full 12-solve CTU with face-centred CT on Chombo AMR
  ([Miniati & Martin (2011)](/sources/miniati-martin-2011.md)).
* **MHD needs extra terms in the CTU steps.** In primitive variables the
  transverse-field induction equations keep normal-field derivative
  terms; they must enter the characteristic tracing and the CTU
  transverse update in a balance consistent with the divergence relation,
  or a field loop advected with a velocity component normal to its plane
  grows a spurious field component along that normal
  ([Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md) §§3.1,
  4.1.2; [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md);
  [field-loop advection](/benchmarks/field-loop-advection.md)). These
  terms are MHD-specific and not in Colella (1990).
  *Compiler reading:* Gardiner & Stone give dimensional splitting's
  failure to hold the constraint between sweeps as their reason for
  unsplit integration; Colella's own motives (front tracking, implicit
  coupling, existing unsplit codes; p. 172) have nothing to do with a
  divergence.
* **With GLM cleaning, all cell-centred.** CTU-GLM in PLUTO
  ([Mignone & Tzeferacos (2010)](/sources/mignone-tzeferacos-2010.md);
  [GLM](/methods/glm-divergence-cleaning.md)), and on Chombo AMR with
  linear, PPM or WENO tracing
  ([Mignone et al. (2012)](/sources/mignone-2012.md)).
* **Hydrodynamics on AMR.** CASTRO's unsplit PPM with full corner coupling
  ([Almgren et al. (2010)](/sources/almgren-2010.md);
  [CASTRO](/software/castro.md)).
* **Abandoned for generality.** Athena++ drops CTU because its
  characteristic projection is intractable for relativistic MHD, in
  favour of VL2 and Runge–Kutta integrators
  ([Stone et al. (2020)](/sources/stone-2020.md)). Colella's predictor
  rests on exactly that projection (eqs. 2.10–2.12) and on
  characteristic limiting (eqs. 2.5–2.6). Runge–Kutta time stepping also
  avoids the CTU interface-state source terms
  ([Mignone & Del Zanna (2021)](/sources/mignone-2021.md)).
* **An announced successor.** The split MHD Godunov scheme of
  [Zachary, Malagoli & Colella (1994)](/sources/zachary-malagoli-colella-1994.md)
  announces an unsplit method after Colella, expected to "improve the
  advection of the solenoidal magnetic field" (§§1, 4).

# Citations

1. [Colella (1990)](/sources/colella-1990.md), §§1–2, 5–6, eqs. 1.2–1.9, 2.5–2.17.
2. [Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md), §§1, 3.1, 4.1.2.
3. [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md).
4. [Stone, Gardiner, Teuben, Hawley & Simon (2008)](/sources/stone-2008.md).
5. [Miniati & Martin (2011)](/sources/miniati-martin-2011.md).
6. [Mignone & Tzeferacos (2010)](/sources/mignone-tzeferacos-2010.md).
7. [Mignone et al. (2012)](/sources/mignone-2012.md).
8. [Almgren et al. (2010)](/sources/almgren-2010.md), §5.
9. [Stone et al. (2020)](/sources/stone-2020.md).
10. [Mignone & Del Zanna (2021)](/sources/mignone-2021.md), §6.1.
11. [Zachary, Malagoli & Colella (1994)](/sources/zachary-malagoli-colella-1994.md), §§1, 4.

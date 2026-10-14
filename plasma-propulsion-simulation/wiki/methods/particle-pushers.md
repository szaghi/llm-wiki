---
type: Method
title: "Particle pushers: leapfrog, Boris and Runge–Kutta"
description: "Time integration of macroparticle trajectories in PIC codes for thrusters — the leapfrog scheme with the Boris rotation for magnetized electrons, used by the fully kinetic codes, and a fourth-order Runge–Kutta push with spline field interpolation, tested against leapfrog for unmagnetized heavy species."
status: established
aliases: [Boris pusher, Boris push, leapfrog, leap-frog, RK4 pusher, particle mover]
tags: [pic, numerics, kinetic]
timestamp: 2026-10-14T00:00:00Z
---

# Particle pushers: leapfrog, Boris and Runge–Kutta

The push step of [PIC-MCC](/methods/pic-mcc.md) advances each macroparticle
by the Newton–Lorentz equations
$$m_s\frac{d\mathbf v_p}{dt}=q_s(\mathbf E+\mathbf v_p\times\mathbf B),\qquad \frac{d\mathbf x_p}{dt}=\mathbf v_p,$$
with $\mathbf E$ (and $\mathbf B$) interpolated from the grid to the
particle ([Taccogna et al. (2023)](/sources/taccogna-2023.md), §II,
Eqs. 2–3). Taccogna et al. call leapfrog "the most diffuse" scheme.

## Leapfrog with the Boris rotation

The fully kinetic codes of this bundle use leapfrog with the Boris
treatment of the magnetic rotation:

- leapfrog with the Boris rotation for magnetized electrons, linear
  (cloud-in-cell) scatter and gather, in the Julia IPPL code
  ([Reza et al. (2022)](/sources/reza-2022.md), §2);
- leapfrog with a Boris push and cloud-in-cell weighting, face fields
  averaged to nodes and interpolated linearly, $\Delta t=10$ ps
  ([Troyetsky et al. (2026)](/sources/troyetsky-2026.md), PIC-MCC model
  section);
- the Boris pusher for electrons, ions and neutrals in PlasmaSim
  ([Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md), Eq. 6);
- the relativistic Boris pusher in [WarpX](/software/warpx.md), with the
  energy-conserving gather of Lewis (1970) on a staggered grid and gather
  and push fused into one GPU kernel
  ([Marks & Gorodetsky (2025)](/sources/marks-2025.md), Methods). In their
  baseline benchmark run the fused gather-and-push kernel takes 48.81 % of
  the wall time, rising to 73.11 % at four times the particle count
  (Table 4), and it is memory-bound on an H100 (Fig. 4b).

## Fourth-order Runge–Kutta for heavy species

[Gallo et al. (2021)](/sources/gallo-2021.md) replace leapfrog by a
fourth-order Runge–Kutta push (§2.1, Eqs. 2–4) in a code that pushes only
ions and neutrals, with no magnetic force on the ions. They state the
orders as second for leapfrog and fourth for RK4, without proof. As
printed, each velocity stage adds the acceleration at the start of the
step to the stage acceleration, and the stage positions use full rather
than half increments, so the scheme is not classical RK4; the reader judges this a typesetting slip rather than
the implemented scheme (recorded on the Source page).

**Test** (§4.2, Fig. 8a, Table 1). One particle starting at axial position 0
and radial position 0.0075 m with 150 m/s in the fixed potential of their Hall-thruster
case, cubic bi-spline field, cell size $4.16\times10^{-4}$ m,
$\Delta t\in\{2.5\times10^{-8},5\times10^{-8},10^{-7}\}$ s; the error in
the final velocity is measured against a Richardson-extrapolated reference.
The text gives the RK4 error falling "from $2.45\times10^{-2}$ to
$1.9\times10^{-3}$" and the leapfrog error from $1.64\times10^{-1}$ to
$6.31\times10^{-2}$; the values plotted span about 0.025 to 0.001 (RK4)
and 0.22 to 0.03 (leapfrog), so the text and the figure do not match at the
leapfrog end points. The paper reports no observed order; the slopes read
from the figure lie below the stated orders for both schemes (Source
page). The result is for a single particle in a fixed, unmagnetized
field.

## Field interpolation at the particle

Gallo et al. (2021, §2.1) interpolate the potential with cubic bi-splines
and differentiate the spline analytically, so that $\mathbf E$ is
continuous; they call bilinear interpolation of a finite-difference
$\mathbf E$ first-order and the spline "third order". On a smooth field the
two give nearly identical final-position errors (§4.2, Fig. 8b,
$\Delta x\in\{8.3,4.16,2.08\}\times10^{-4}$ m). In a test with a
discontinuous field (two concentric circular plates at 100 V and 0 V in a
2 × 1 m box with 100 × 50 nodes, Fig. 9), bilinear interpolation
accelerates particles outside the plates, where the field is zero, and the
spline does not. On one GPU the spline interpolation takes 19.80 min against 40.22 min on
the multicore CPU (§4.3, Table 2).
Marks & Gorodetsky (2025, Methods) use linear shape functions with an
energy-conserving gather.

# Citations

1. [Taccogna et al. (2023)](/sources/taccogna-2023.md), §II, Eqs. 2–3 (accepted manuscript).
2. [Reza et al. (2022)](/sources/reza-2022.md), §2 (preprint).
3. [Troyetsky et al. (2026)](/sources/troyetsky-2026.md), PIC-MCC model section.
4. [Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md), Eq. 6.
5. [Marks & Gorodetsky (2025)](/sources/marks-2025.md), Methods, Table 4, Fig. 4b.
6. [Gallo et al. (2021)](/sources/gallo-2021.md), §§2.1, 4.2, 4.3, Eqs. 2–4, Figs. 8–9, Tables 1–2.

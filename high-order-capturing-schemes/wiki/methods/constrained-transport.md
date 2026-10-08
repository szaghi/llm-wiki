---
type: Method
title: "Constrained transport for high-order capturing schemes (MHD)"
description: "Keeping the magnetic field discretely divergence-free alongside a high-order capturing scheme: the unstaggered vector-potential variant (evolve A on the cell mesh, set B as its discrete curl) and the Yee-staggered variant (face-averaged B updated by edge electric fields from a multidimensional Riemann solver)."
status: established
aliases: [CT, unstaggered constrained transport, vector-potential constrained transport, Yee mesh, divergence-preserving update]
tags: [mhd, divergence-free, constrained-transport, involution]
timestamp: 2026-10-08T00:00:00Z
---

# Constrained transport for high-order capturing schemes

$\nabla\cdot\mathbf B = 0$ is an involution: preserved by the exact
evolution, but discretizations of the transport equation alone
accumulate divergence errors. These produce an unphysical force along
$\mathbf B$ and often crash the code. The options are the eight-wave
method, projection, hyperbolic divergence cleaning and constrained
transport ([Christlieb et al. (2016)](/sources/christlieb-2016.md), §1).
Two constrained-transport designs appear in this corpus.

## Unstaggered, vector potential

([Christlieb et al. (2016)](/sources/christlieb-2016.md), §§2, 4; the
Rossmanith framework.) Faraday's law with ideal Ohm's law gives
$\partial_t\mathbf A + (\nabla\times\mathbf A)\times\mathbf v = -\nabla\psi$;
the Weyl gauge $\psi = 0$ is stable. $\mathbf A$ lives on the same
mesh as the conserved variables. Each step updates the MHD variables
(including a provisional $\mathbf B$), updates $\mathbf A$, overwrites
$\mathbf B$ with the discrete curl of $\mathbf A$, and — only when the
positivity limiter is on — corrects the energy so the pressure is
unchanged. The last step sacrifices energy conservation.
* In 2D only $A_z$ is needed:
  $\partial_t A_z + v_x\partial_x A_z + v_y\partial_y A_z = 0$, a strongly
  hyperbolic Hamilton–Jacobi equation. Treated with HJ technology
  (Lax–Friedrichs Hamiltonian, WENO5 one-sided derivatives), it gives
  $\mathbf B$ with non-oscillatory derivatives; the curl is fourth-order
  central.
* In 3D the $\mathbf A$ system is only weakly hyperbolic and needs
  artificial resistivity. A smoothness-indicator-gated term of size
  $O(h^6)$ in smooth regions and $O(h)$ at kinks, with coefficient
  $\nu \approx 0.01$, controls field oscillations.
* Without CT the rotated shock tube develops unphysical oscillations
  and the [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) run
  crashes at $t = 1.67$.

## Yee-staggered, multidimensional Riemann solver

([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §§1–4.)
Every divergence-preserving sub-system has the induction form
$\partial_t\mathbf B + \nabla\times\boldsymbol{\mathcal E} = 0$, with
anti-symmetric fluxes, and Stokes' theorem forces a Yee-type
collocation: face averages $\bar B_x$, $\bar B_y$, $\bar B_z$ updated by
edge averages of $\boldsymbol{\mathcal E}$,
$$\partial_t \bar B_{x;i+1/2,j,k} = -\frac{1}{h_y h_z}\left(h_z\,\bar{\mathcal E}_{z;i+1/2,j+1/2,k} - h_z\,\bar{\mathcal E}_{z;i+1/2,j-1/2,k} + h_y\,\bar{\mathcal E}_{y;i+1/2,j,k-1/2} - h_y\,\bar{\mathcal E}_{y;i+1/2,j,k+1/2}\right),$$
and cyclically (eqs. 3–5, checked on the page image). This preserves the discrete divergence exactly. Edge
fields need upwinding in both transverse directions, which is the role
of the multidimensional Riemann solver. In its 2D LLF limit (signal
speed $S$),
$$\mathcal E^{**}_z = \tfrac14\left(\mathcal E_{z,RU} + \mathcal E_{z,LU} + \mathcal E_{z,LD} + \mathcal E_{z,RD}\right) + \tfrac{S}{2}\left[B_{x,D} - B_{x,U} + B_{y,R} - B_{y,L}\right]$$
(eq. 12, checked on the page image). The four corner fields come from
2D WENO interpolation of cell-centred $\mathcal E_z$, and the jumps from
2D WENO reconstruction of the face fields evaluated at the edge. The
dissipation is thus proportional only to transverse jumps of the
normal field and vanishes as they converge. The HLL version (eqs.
16–20) adds a supersonic limit through a nine-case conditional; it is
preferred for strongly supersonic MHD.

**Mixed FD–FV scheme.** All cell-centred variables follow
[AFD-WENO](/methods/alternative-finite-difference-weno.md); only the
face fields are FV-updated. A pointwise 1D WENO interpolation along each
edge converts point values of $\mathcal E$ to edge averages. No
divergence-free volumetric reconstruction is built, which keeps the
cost low; high-order divergence-preserving AMR remains available. The
same algorithm, unchanged, solves electrodynamics, MHD and relativistic
MHD at orders up to 9.

**Comparison.** The vector-potential route needs no staggering, which
eases embedding in AMR, but it breaks energy conservation where the
positivity fix acts. The staggered route conserves exactly except in
rare cells, where the first-order PCP fallback adds an energy source
([positivity preservation](/properties/positivity-preserving.md)).

# Citations

1. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §§1, 2, 4, 6.
2. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §§1–5 (eq. 12 read from the page image).

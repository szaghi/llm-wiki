---
type: Method
title: "Cut-cell (embedded-boundary) finite volume"
description: "Finite volume on a Cartesian grid cut by the body: cut cells keep their fluid volume and face apertures so the scheme stays conservative, at the price of the small-cell problem — a time step set by the regular cells is unstable on tiny cut cells — which flux redistribution, cell merging, h-box and state redistribution remove; moving bodies and AMR add freshly cleared cells and coarse–fine synchronization."
status: established
aliases: [embedded boundary method, Cartesian cut-cell method, EB finite volume, cut-cell method, flux redistribution]
tags: [boundary-treatment, embedded-boundary, cartesian-grid, conservation, amr, cut-cell]
timestamp: 2026-10-13T00:00:00Z
---

# Cut-cell (embedded-boundary) finite volume

The body cuts the Cartesian cells. Each cut cell keeps its fluid volume
$\vert I_i\vert = \kappa_i h^d$, its face apertures and an
embedded-boundary (EB) face, and the finite-volume update is a flux
balance over that polygon. The wall condition enters only through the
flux on the EB face, so the scheme conserves exactly on a static body
([Berger & Giuliani (2021)](/sources/berger-2021.md), §3;
[Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §2).
The non-conservative alternative is the ghost-cell
[immersed-boundary method](/methods/immersed-boundary-method.md).

**The wall flux.** For an inviscid wall the EB-face flux carries only the
pressure, obtained by extrapolation to the face or from a Riemann problem
against the mirrored state with the wall's normal velocity
([Berger & Giuliani (2021)](/sources/berger-2021.md), §3;
[Natarajan et al. (2022)](/sources/natarajan-2022.md), eqs. 6–8). Viscous
wall gradients come from a least-squares fit about the EB-face centroid
(Natarajan et al., §2.2) or from a ray cast into the fluid
([Giuliani et al. (2022)](/sources/giuliani-2022.md), §5.1).

## The small-cell problem and its cures

An explicit update divides the flux balance by $\vert I_i\vert$, so a
stable step shrinks with $\kappa_i \to 0$. Every cure lets the step be set
by the regular cells ([Berger & Giuliani (2021)](/sources/berger-2021.md), §1):
* **Flux redistribution** (Pember et al. 1995; Colella et al. 2006, as
  cited), the most common. The cut cell takes the hybrid update
  $\kappa_i(\nabla\cdot\mathbf f)^{\mathrm c}_i + (1 - \kappa_i)(\nabla\cdot\mathbf f)^{\mathrm{nc}}_i$,
  where the non-conservative divergence is a volume-weighted average over
  the 3×3×3 neighbourhood, and the mass this loses is given to the
  neighbours with weights $\kappa_j/\sum_k\kappa_k^2$, which restore
  conservation ([Natarajan et al. (2022)](/sources/natarajan-2022.md), §2).
  It is first order at cut cells and does not preserve linear functions
  (Berger & Giuliani, §§1–2). In a reacting 3D run it produced mass
  fractions below 0 and above 1 where state redistribution did not
  ([Giuliani et al. (2022)](/sources/giuliani-2022.md), §6.1).
  The algorithm, its weights and its properties are on the
  [flux redistribution](/methods/flux-redistribution.md) page.
* **Cell merging**, stable but hard to do robustly in general 3D
  geometry; **h-box**, second order at cut cells but not extended to 3D;
  cell linking, and implicit updates on the cut cells only (Berger &
  Giuliani, §1).
* **State redistribution**, which post-processes the provisional states
  instead of the fluxes: [state redistribution](/methods/state-redistribution.md).

The threshold for "small" in state redistribution, half a regular cell,
rests on a 1D stability result for cell merging (Berger 2015); the 2D and
3D cases are not proved (Berger & Giuliani, §4.1).

**Accuracy.** On smooth flows the $L^1$ error is second order in the
volume and about 1.4–1.5 on the boundary cells, with local time
stepping as with redistribution, so the loss comes from the irregular
cut cells, not from the stabilization
([Berger & Giuliani (2021)](/sources/berger-2021.md), §5.1, Table 2;
[Giuliani et al. (2022)](/sources/giuliani-2022.md), §3.2;
[supersonic vortex](/benchmarks/supersonic-vortex-annulus.md)). The
base schemes are second order: MUSCL-type unsplit Godunov or a
two-stage method of lines, with least-squares gradients and a
Barth–Jespersen limiter evaluated at neighbour centroids at cut cells.

**Conservation is what matters at cold walls.** A strictly conservative
cut-element method (INCA) on a Mach 8.98 reacting cylinder matches the
body-fitted heat flux where the CHESS ghost-cell solver is low by a
factor of about 40. CHESS differs from INCA in other respects too, so
the isolating experiment is INCA with its conservative flux treatment
switched off, which differs from the cut-cell method in that treatment
only: its heat flux is closer than CHESS's but "clearly wrong", and on
an ablator its blowing rate is overpredicted much as CHESS's is. The
authors take this to consolidate conservation as the cause
([Başkaya et al. (2024)](/sources/baskaya-2024.md), §§4.5, 5, Fig. 18; see
the [IB page](/methods/immersed-boundary-method.md)). That solver keeps
every intersection of the grid with the surface triangulation, so one
cut cell can hold several cut elements, and it fills ghost cells as well
so that interior stencils are unchanged (§3.2).

## Moving bodies

[Natarajan et al. (2022)](/sources/natarajan-2022.md) move the EB in a
block-structured AMR code (AMReX), with flux redistribution:
* the cut-cell update divides by the old volume fraction $\kappa_i^n$ and
  has no term for the volume swept in the step (eq. 4);
* a freshly cleared cell is filled with the volume-weighted average of
  its fluid neighbours, which preserves a uniform flow moving with the
  body (§2.1; [free-stream preservation](/properties/free-stream-preservation.md));
  freshly covered cells are not discussed;
* the observed order on a receding piston drops to 1, which the authors
  attribute to the cleared-cell fill (Fig. 5c); the attribution is
  untested, and flux redistribution, which they use, is itself first
  order at cut cells (Berger & Giuliani, §1);
* a closed piston loses up to 0.92 % of its mass at $32^3$ and 0.31 % at
  $64^3$. The paper reads the decrease as proof of conservation; a
  conservative scheme would hold the mass to round-off, so these numbers
  show consistency, not conservation (§3.6).

## Cut cells and AMR

Redistribution done one level at a time moves conserved quantities into
covered coarse cells and fine ghost cells, which are not part of the
composite solution, and corrections added to tiny cut cells at the
coarse–fine boundary are unstable. Production codes either keep the
coarse–fine boundary away from cut cells
([Giuliani et al. (2022)](/sources/giuliani-2022.md), §4) or refine
every cut cell to the finest level
([Natarajan et al. (2022)](/sources/natarajan-2022.md), §3.1). The
repair, re-redistribution, is on the
[state-redistribution page](/methods/state-redistribution.md); see also
[high-order AMR](/methods/high-order-amr.md).

**Later uses (batch 11): moving boundary tracking.**
[Falcovitz, Alfandary & Hanoch (1997)](/sources/falcovitz-1997.md), a
moving-body Cartesian cut-cell scheme from the time of Pember et al.,
whom it cites:
* *Base scheme and splitting.* A dimensionally split second-order GRP
  scheme; the boundary-node motion is split too, so each split phase moves
  the polygonal body in one direction only (§§2–3). The base schemes above
  are unsplit or method-of-lines.
* *Swept volume.* Each boundary cell uses its old and new fluid volumes,
  $\kappa_i^n h^2$ and $\kappa_i^{n+1}h^2$, time-averaged exposed face
  areas, and a time-averaged projected boundary area that carries the wall
  pressure and work (eqs. 6–9, 27–34). These are built so that a uniform
  flow moving with the body is reproduced exactly (by construction, not
  demonstrated numerically), and the boundary term uses the same
  geometric quantities as the face apertures. This is a design contrast
  with the Natarajan et al. update above, which divides by $\kappa_i^n$
  and has no swept-volume term; the two papers do not contradict each
  other ([free-stream preservation](/properties/free-stream-preservation.md)).
* *Geometry.* All areas come from signed sums of trapezoids under the
  polygon sides, and a proved lemma (Lemma 4.1) makes the time-averaged
  covered lengths additive over sides, with closed-form integrals for each
  side (§4).
* *Cleared, covered and small cells.* A cell becoming fully covered, a
  covered cell becoming partly exposed, and a cell whose partial length is
  below a user fraction, "typically about 0.3" of a cell, are merged with
  an adjacent wet cell, and the merged state is given to every member
  (§3, p. 91). This answers the freshly covered cells that Natarajan et
  al. do not discuss. The 0.3 is a length fraction in the split direction,
  not the volume fraction of the half-cell threshold above, so the two are
  not comparable.
* *Wall flux and order.* The wall pressure comes from a one-sided piston
  Riemann problem normal to each segment, consistent with the wall flux
  above. Boundary cells carry piecewise-constant data, so the scheme is
  first order there (stated, p. 91), in line with the loss of order at
  cut cells reported above. No error or convergence data are given; the
  only computation is the [shock-driven cylinder lift-off](/benchmarks/shock-cylinder-lift-off.md),
  which this paper introduced.
* *Conservation.* MBT is called exactly conservative in boundary cells,
  unlike Forrer's mirroring scheme (§1).

**Later uses (batch 18): the h-box method in its primary source.**
[Berger et al. (2003)](/sources/berger-2003.md) is the systematic study of
h-box methods, one of the cures listed above. It treats grids with small
cells, not cut cells: the 1D grids have cells of length $\kappa_i h$
($0 < \kappa_i \le 1$, the 1D analogue of the volume fraction), and the 2D
grids are tensor grids with thin rows and columns of cells.
* *Principle* (§§1, 3). The fluxes at the two faces of a small cell come
  from Riemann problems between h-box values, averages over boxes of
  length $h$ next to each face, so the step obeys $\nu \le 1$ with $\nu$
  computed on $h$, not on $\kappa_i h$. The base scheme is LeVeque's
  wave-propagation algorithm.
* *The h-box values decide accuracy* (§3). Averaging the piecewise-constant
  data gives an inconsistent scheme that is still first order
  (Prop. 1, a supraconvergence proof). Linear interpolation, with the value
  seen from inside the small cell at its inflow face
  $$\frac{2\kappa_i\bar u_i + (1-\kappa_i)\bar u_{i+1}}{1+\kappa_i}$$
  (eq. 3.3, symmetric at the other face), is consistent and exact for
  linear data. With a second-order correction that uses $h$ (eq. 3.8; the
  natural correction with $(1+\kappa_i)h/2$, eq. 3.7, was unstable at
  $\nu \le 1$ on $h$), the scheme is **proved second order for 1D advection
  with one small cell** (Prop. 2), although its local truncation error in
  the small cell is first order. Stability is GKS, shown numerically for
  $0 < \nu \le 1$ (Appendix A).
* *Observed order* (§§5, 7). Second order on completely irregular 1D grids
  (advection, observed orders 2.03 and 2.01; smooth Euler with cells
  between $h/10$ and $h$, unlimited orders 1.67–1.94, Table 5.1) and on a
  2D tensor grid with rows and columns of width $0.1h$ and $0.9h$
  (2.19 and 2.09). The 2D method needs modified transverse propagation to
  be stable for $\nu \le 1$; without it, $\nu \le \tfrac12$.
* *Defects* (§6). With Godunov or Roe fluxes the h-box values produce
  unphysical oscillations at transonic rarefactions that standard Godunov
  schemes avoid; Lax–Friedrichs fluxes between h-box values cure them.
* *What it does not show* (§8). It has no cut cells and no embedded
  boundary, and states: "So far there is no Cartesian grid embedded
  boundary method that leads to a second order accurate approximation at
  boundary cells", announcing an h-box embedded-boundary scheme as
  forthcoming work. The line above, "**h-box**, second order at cut cells
  but not extended to 3D", is Berger & Giuliani's (2021, §1) summary; the
  "not extended to 3D" part agrees with this paper (1D and 2D only), but
  its "second order at cut cells" cannot rest on this paper, which proves
  second order only for small non-cut cells. The bundle holds no source
  for an h-box embedded-boundary scheme. This is a qualification, not a
  contradiction: Berger & Giuliani speak of the h-box family as of 2021.
* *Earlier small-cell methods* (§1). Pember et al. (1995) and Falcovitz et
  al. (1997) are listed among embedded-boundary methods stable with a
  regular-cell time step.

## Contradictions

**What order does flux redistribution give, and what limits it on moving
bodies?** *Open* (recorded at the 2026-10-12 deep lint).
* [Berger & Giuliani (2021)](/sources/berger-2021.md), §1: flux
  redistribution is "only first order accurate at the cut cells".
* [Natarajan et al. (2022)](/sources/natarajan-2022.md), §3.2.2: their
  flux-redistribution scheme "has an accuracy of 2 for smooth problems";
  the first order observed on a receding piston is attributed to the
  freshly-cleared-cell fill, without a test that separates the two causes.
* The scopes differ: Berger and Giuliani speak of the local error at cut
  cells, Natarajan et al. of a global entropy $L^2$ norm, where first-order
  cut cells on a codimension-one set need not cap the global order. A
  measurement for a different stabilization supports this scope reading:
  with weighted state redistribution on a static body,
  [Giuliani et al. (2022)](/sources/giuliani-2022.md), §3.2, Fig. 6b,
  find second order in the volume and about 1.4 on the boundary: the
  order at the cut cells falls below the order of a volume norm
  (evidence by analogy, not a flux-redistribution measurement). A static-body convergence test of
  the same scheme, or a moving test with state redistribution, would
  separate the causes.
* *Later evidence (batch 18), on a related distinction (truncation error
  against solution error), not the local/global scope reading.* A first-order (even
  inconsistent) local truncation error at small cells does not by itself
  cap the global order: [Berger et al. (2003)](/sources/berger-2003.md)
  prove first-order convergence of an inconsistent h-box scheme (Prop. 1)
  and second order of one whose small-cell truncation error is first order
  (Prop. 2), in 1D with one small (non-cut) cell. Its authors also state,
  in 2003, that no Cartesian embedded-boundary method was yet second order
  at boundary cells (§8), which, as of 2003, is consistent with Berger &
  Giuliani's local first-order statement. It measures no flux redistribution, so the entry
  stays Open.

# Citations

1. [Berger & Giuliani (2021)](/sources/berger-2021.md), §§1–5 (arXiv v1).
2. [Giuliani et al. (2022)](/sources/giuliani-2022.md), §§2–6, Fig. 6b (arXiv v2).
3. [Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §§2–3 (arXiv v1).
4. [Natarajan et al. (2022)](/sources/natarajan-2022.md), §§2–3 (arXiv v1).
5. [Başkaya et al. (2024)](/sources/baskaya-2024.md), §§3, 4.5, 5, Fig. 18 (arXiv v1).
6. [Falcovitz, Alfandary & Hanoch (1997)](/sources/falcovitz-1997.md), §§1–5.
7. [Berger et al. (2003)](/sources/berger-2003.md), §§1, 3–8, Props. 1–2, Appendix A.

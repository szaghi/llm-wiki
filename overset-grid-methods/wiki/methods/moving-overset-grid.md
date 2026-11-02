---
type: Method
title: "Moving overset grids"
description: "Moving overset grids let component grids follow bodies in relative motion, with domain connectivity recomputed every time step and coupled to the flow solver and body dynamics; the page covers Meakin and Suhs's unsteady Chimera cycle, time metrics and hole-motion limit, and SUGGAR's body-frame trees, hierarchical transforms and process coupling."
status: established
aliases: [moving-body overset, unsteady Chimera, dynamic overset grids, relative-motion Chimera, moving-body grid assembly]
tags: [moving-grid, domain-connectivity, overset-grid, chimera, store-separation]
timestamp: 2026-11-02T11:26:00Z
---

# Moving overset grids

On a **moving overset grid** the component grids $G_k$ attached to bodies move with them
while other grids (a background, the grid of a primary body) stay fixed or move differently.
In the chunk-1 sources each component grid moves rigidly, so its points keep their indices and the flow solver sees a
grid velocity $\mathbf u_g$; the [point classification](/definitions/point-classification.md),
the holes and the donors change with time and must be recomputed every time step. Meakin &
Suhs (1989) present a prototype method for three-dimensional viscous flow about several
bodies in relative motion and name its three functions: the flow solver (Aerodynamic
Function, ADF), the [domain connectivity](/definitions/domain-connectivity.md) (Domain
Connectivity Function, DCF) and the body motion (Body Dynamics Function, BDF). The functions
form a cycle: the flow solver needs hole and interpolation data from the connectivity, the
connectivity needs body positions from the dynamics, and the dynamics need loads from the
flow solver ([Meakin & Suhs (1989)](/sources/meakin-1989.md), §II). Noack (2005) builds the
connectivity side as a separate program, SUGGAR, for structured, unstructured and polyhedral
grids ([Noack (2005)](/sources/noack-2005.md), §VII).

## From static to moving assembly

In the static Chimera method the composite grid is assembled once: PEGSUS writes the
composite grid and the interpolation data to two files that the flow solver XMER3D reads
([Benek et al. (1985)](/sources/benek-1985.md), p. 323, p. 325). Meakin & Suhs measure what
this costs when repeated every step: unmodified PEGASUS took 1.96 times the CPU time of one
flow-solver iteration on a wing/store case and 5.27 times on the Space Shuttle SRB separation
case (NAS CRAY-2), and they judge it "simply not practical" for moving grids (Table 1). They
state that in static applications hole definition is typically the most time-consuming
connectivity task. Later tools keep the static design but reduce the redone work: Rogers et
al. (2003) recall that PEGASUS 4 had a restart capability useful for moving bodies, and
PEGASUS 5 repeats only the operations that depend on modified input
([Rogers et al. (2003)](/sources/rogers-2003.md), p. 1038, p. 1042). Noack (2005) states that
PEGASUS 5 "has not been applied to moving body problems" (§I). Wang (1995) notes that the cut
geometry of the conservative interface is computed once for grids that do not move and
expects it to be much more expensive in 3-D ([Wang (1995)](/sources/wang-1995.md), §6).

## Flow solver on moving component grids

Meakin & Suhs solve the thin-layer Navier–Stokes equations in strong conservation form with
an implicit, approximately factored, partially flux-split scheme (the VAPOR code of Steger,
Ying & Schiff, as cited) and add the time-metric terms $\xi_t,\eta_t,\zeta_t$, which the
original code neglected (§II ADF, §III). In registry form the inviscid flux in $\xi$ is
$\hat{\mathbf F}=J^{-1}(\xi_t\mathbf q+\xi_x\mathbf F_1+\xi_y\mathbf F_2+\xi_z\mathbf F_3)$,
with the contravariant velocity $U=\xi_t+\xi_xu+\xi_yv+\xi_zw$ carrying the grid motion; its
energy component is $J^{-1}\big((E+p)U-\xi_tp\big)$, which is the form Meakin & Suhs print
(Eq. (1)), since $\xi_tE+(E+p)(\xi_xu+\xi_yv+\xi_zw)=(E+p)U-\xi_tp$ *(compiler check, not
in the sources)*. For a grid
point moving with velocity $\mathbf u_g$ the time metrics are
$$\xi_t=-\mathbf u_g\cdot\nabla\xi,\qquad\eta_t=-\mathbf u_g\cdot\nabla\eta,\qquad\zeta_t=-\mathbf u_g\cdot\nabla\zeta .$$

The hole logic reaches the solver only through the 0/1 IBLANK: it multiplies the time step
and the dissipation terms of the factored scheme, so that at hole points the update vanishes
and the solution is frozen (Eq. (2)).

**Verification of the time metrics.** Before any overset run, Meakin & Suhs test the metrics
on a single grid: a NACA 64A010 airfoil at $M_\infty=0.8$ in constant plunge equivalent to
$1^\circ$ incidence, with $\xi_t=\eta_t=0$ and $\zeta_t=-M_\infty\sin(\pi/180)$, and in
sinusoidal plunge of amplitude equivalent to $\pm1^\circ$ with
$\zeta_t=-M_\infty\sin(\pi/180)\sin(2\pi\tilde t/\tilde t_p)$, $\tilde t_p=2\pi/(k_{\mathrm
r}M_\infty)$, $k_{\mathrm r}=0.4$ (dimensionless time $\tilde t$ and period $\tilde t_p$
page-local). Constant plunge agrees well with Magnus (1977) except for a weak lower-surface
shock smeared by the coarse grid; the lift coefficient over the fourth cycle of the sinusoidal
plunge shows "excellent agreement" (§III, Figs. 4–5).

## Connectivity every time step

**Restricted search and the hole-motion limit.** Meakin & Suhs's DCF is a modified PEGASUS
that uses the hole and inter-grid boundary locations at time level $n$ to restrict the search
at level $n+1$ to the points on either side of the level-$n$ hole boundaries ("unsteady
PEGASUS", §II DCF). The restriction is valid only if no hole point becomes a field point
without first having been an interpolated hole-boundary point. Writing the classification
sets at time level $n$ with a superscript (page-local), the rule is
$$\mathcal D_k^{n+1}\cap\mathcal H_k^{n}=\varnothing ,$$
so a hole may move by at most one point per step on its uncovering side. Their 1-D example
(Fig. 3): a hole moving one node is valid; a hole boundary jumping two nodes uncovers a point
that goes from hole to field "without ever being updated through interpolation as a hole
boundary point", introducing undefined flow values. The limit bounds the time step; the
authors state that in all moving-body cases examined the time step needed to resolve the
physics was much smaller. The restricted search lowered the connectivity cost from 1.96 to
0.64 and from 5.27 to 2.02 flow-solver iterations, "a factor of ∼3" (Table 1); the ratios
are 3.06 and 2.61 *(compiler check, not in the sources)*; the rest depends on the configuration and on connectivity routines that do
not vectorize.

| case | grids | points | interpolated boundary points | PEGASUS / ADF | DCF / ADF |
|---|---|---|---|---|---|
| wing/store separation | 2 | 243,906 | 2,090 | 1.96 | 0.64 |
| Space Shuttle SRB separation | 3 | 357,330 | 10,408 | 5.27 | 2.02 |

**Trees in body frames (SUGGAR).** Noack (2005) argues that hole cutting must be efficient
because it is repeated every step (§II, §VII). SUGGAR builds its hole-cutting and
donor-search trees once, at initialization, in each body's untransformed frame; the grids of
moving bodies stay in their original coordinates and are positioned by per-body transforms.
The transforms are **absolute** in time (not incremental) and **hierarchical**: a child body
moves relative to its parent, so a store can move relative to the aircraft and its fins
relative to the store. A query point is transformed from its local frame to the global frame
and then to the target body's frame, so every search runs in the target's coordinates (§VII).
In registry form a rigid transform maps body-frame coordinates $\mathbf X$ to
$\mathbf x=\mathbf x_{\mathrm{cg}}+\mathsf R(\mathbf X-\mathbf X_{\mathrm{cg}})$; Noack prints
no formula. The same body hierarchy decides which bodies cut which grids ("siblings cut each
other"; see [hole cutting](/methods/hole-cutting.md)).

**Implicit hole cutting.** Lee & Baeder (2003) do not blank hole points: the solver updates
them, and their contamination argument requires that information from invalid points cannot
cross the thinnest fringe in one time step $\Delta t$; their test-point sweeps alternate
direction with the time-step counter
([Lee & Baeder (2003)](/sources/lee-2003.md), sub-items 3–4, pp. 6–9; see
[implicit hole cutting](/methods/implicit-hole-cutting.md)). Lee & Baeder do not address
Meakin & Suhs's hole-motion rule, and neither source discusses the other's setting (see the
qualification on [point classification](/definitions/point-classification.md)).

## Coupling with body dynamics

Meakin & Suhs describe the BDF's role, computing loads and moments from the flow field and
predicting trajectories and attitudes, but do not implement it: all trajectories are
prescribed. They give the obstacle: the flow solver predicts lift and moments accurately, but
accurate drag for 3-D separated flow is beyond the memory and CPU available, so a trajectory
model must be built from what the flow solution can supply (§II BDF). They call the
prescribed-trajectory BDF the "weak link" (§IV).

Noack couples SUGGAR, the flow solver and a motion controller (for example a
six-degree-of-freedom integrator for the force $\boldsymbol{\mathcal F}$ and moment
$\boldsymbol{\mathcal M}$) as separate processes synchronized by blocking Unix FIFOs (named
pipes): the controller writes the transforms; SUGGAR assembles and signals; the solver reads
the new connectivity (and the composite grid when needed), advances one step and writes time,
forces and moments back to the controller. All processes must run on one shared-memory
machine, and only one parallel solver process can talk to a FIFO (§VII, Fig. 10). The
solver-side operations are in the companion library DiRTlib (Noack 2005, AIAA 2005-5116, as
cited).

## Demonstrations

All chunk-1 moving-grid demonstrations use prescribed motion (see
[store separation](/benchmarks/store-separation.md)):

- **Store separation from the AFATL wing** (Meakin & Suhs, §III, Plate 1): the converged
  steady wing + store solution ($M_\infty=1.05$, $\alpha=2^\circ$, $Re=2.4\times10^6$ per
  foot) is the initial condition; the store, pinned at the tail, sweeps its nose down by one
  body diameter of arc in 500 steps (150 ms).
- **Space Shuttle SRB separation** (Meakin & Suhs, §III, Fig. 11, Plate 2): orbiter, external
  tank and two SRBs on 3 grids (357,330 points) with 8 inter-grid boundaries (2 outer, 6 hole);
  $M_\infty=4.5$, $\alpha=2^\circ$, $Re=6.95\times10^6$ on the orbiter length;
  $\Delta t=1.36\times10^{-3}$ s, 500 steps over the booster-separation-motor burn of about
  2/3 s. No reference data.
- **Wing/pylon/finned store** (Noack, §VIII, Table 2): all structured grids, 3.64 million
  points, binary-tree hole cutting with variable resolution; about 15 s hole cutting, 39 s
  donor search and 10 s output per step on a 2.6 GHz Pentium 4, about 1.0 GB memory.
- **C130 air drop** (Noack, §VIII, Table 3): a C130 with open doors, a parachute and a cargo
  box on 2 unstructured (prism/tetrahedral) and 15 structured grids, 4.85 million points,
  10.7 million cells; parachute and cargo in prescribed motion; about 81 s hole cutting, 53 s
  donor search and 71 s ASCII output per step, about 1.8 GB memory. No flow solution is shown
  in either SUGGAR case.

## Qualifications

- Meakin & Suhs state that the effect of the inter-grid boundary updating on time accuracy
  "has not been addressed" (§IV); their time-accuracy evidence is the single-grid plunge tests,
  and the moving multi-grid cases have no reference data.
- The claim that the hole-motion limit is far weaker than the physics time step is stated for
  the cases examined, not shown. On p. 646 the claim is restated with the comparison inverted
  ("the time-step size limitation imposed by the DCF search limits are generally much less
  than those required"), which read literally says the opposite of the first statement.
- Meakin & Suhs print the constant-plunge metrics as
  $\xi_t=x_t\xi_x-y_t\xi_y-z_t\xi_z$ (and likewise for $\eta_t$, $\zeta_t$, p. 647), with a
  positive first term; the identity $\xi_t=-\mathbf u_g\cdot\nabla\xi$ gives the same sign for
  all three terms *(compiler check, not in the sources)*. Their right-hand sides, given
  directly, are unaffected.
  They also print the conserved vector without the factor $J^{-1}$ that their fluxes carry
  (p. 644).
- None of the chunk-1 sources discusses the discrete geometric conservation law for the moving
  component grids.
- Noack's C130 setup times (256 s reading and orienting cells, 14 s binary tree, 79 s
  donor-search octree) sum to 349 s, while the text prints a total of 335 s; the
  wing/pylon/store setup total (6 + 261 + 16 = 283 s) is consistent (§VIII) *(compiler check,
  not in the sources)*.

# Citations

- [Meakin & Suhs (1989)](/sources/meakin-1989.md) — §I; §II ADF (Eqs. (1)–(2)), BDF, DCF (Fig. 3, Table 1); §III (Figs. 4–5, 11, Plates 1–2); §IV.
- [Noack (2005)](/sources/noack-2005.md) — §I, §II, §VII (Fig. 10), §VIII (Tables 2–3).
- [Benek et al. (1985)](/sources/benek-1985.md) — pp. 323, 325 (static PEGSUS/XMER3D workflow).
- [Rogers et al. (2003)](/sources/rogers-2003.md) — p. 1038 (PEGASUS 4 restart), p. 1042 (PEGASUS 5 restart).
- [Wang (1995)](/sources/wang-1995.md) — §6.
- [Lee & Baeder (2003)](/sources/lee-2003.md) — sub-items 3–4, pp. 6–9.

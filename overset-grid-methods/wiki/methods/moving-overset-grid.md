---
type: Method
title: "Moving overset grids"
description: "Moving overset grids let component grids follow rigid, rotating or deforming bodies, with domain connectivity recomputed every time step and coupled to the flow solver and body dynamics: Meakin and Suhs's unsteady Chimera cycle and hole-motion limit, mapped equations with grid velocity, exposed points, Ogen's incremental update, SUGGAR's body-frame trees, parallel and GPU per-step assembly, and moving-body demonstrations."
status: established
aliases: [moving-body overset, unsteady Chimera, dynamic overset grids, dynamic overset technique, relative-motion Chimera, moving-body grid assembly, moving overlapping grids, deforming composite grids]
tags: [moving-grid, domain-connectivity, overset-grid, chimera]
timestamp: 2026-11-02T15:08:00Z
---

# Moving overset grids

On a **moving overset grid** the component grids $G_k$ attached to bodies move with them
while other grids (a background, the grid of a primary body) stay fixed or move differently.
In most sources each component grid moves rigidly, so its points keep their indices and the
flow solver sees a grid velocity $\mathbf u_g$; Banks et al. (2016) also let the grids next to
a fluid–solid interface deform and regenerate them every step. In every case the
[point classification](/definitions/point-classification.md), the holes and the donors change
with time and must be recomputed every time step. Meakin &
Suhs (1989) present a prototype method for three-dimensional viscous flow about several
bodies in relative motion and name its three functions: the flow solver (Aerodynamic
Function, ADF), the [domain connectivity](/definitions/domain-connectivity.md) (Domain
Connectivity Function, DCF) and the body motion (Body Dynamics Function, BDF). The functions
form a cycle: the flow solver needs hole and interpolation data from the connectivity, the
connectivity needs body positions from the dynamics, and the dynamics need loads from the
flow solver ([Meakin & Suhs (1989)](/sources/meakin-1989.md), §II). Noack (2005) builds the
connectivity side as a separate program, SUGGAR, for structured, unstructured and polyhedral
grids ([Noack (2005)](/sources/noack-2005.md), §VII). Henshaw & Schwendeman (2006) write the
same cycle as one PDE-independent time-stepping loop in which the grids are moved, the
connectivity updated and newly uncovered points filled before the solution is advanced
([Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md), §3.4, Fig. 6).

Relative motion was the original motivation of the Chimera scheme: Chan (2009) recalls that
simulating several bodies in relative motion with general six-degree-of-freedom (6-DOF)
motion was a main reason for overset rather than abutting grids, which "clearly could not
satisfy" it ([Chan (2009)](/sources/chan-2009.md), §2; see
[patched grids](/definitions/patched-grid.md)). Wang et al. (2021) choose a dynamic overset
technique for a rotating propeller because it is "used widely in problems that consider
moving geometries" ([Wang et al. (2021)](/sources/wang-2021.md), §III A).

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

Per-step assembly makes the speed of [hole cutting](/methods/hole-cutting.md) decisive. Chan
(2009, §7) recalls two hole-cutting methods of Meakin chosen for moving bodies: analytic
shapes (c. 1991), fast point-in-shape tests suited to hole cutting every time step but
"prohibitively difficult" to fit to complex bodies, and object X-rays (2001), "routinely used"
in OVERFLOW 2 moving-body computations, fast but with manually generated X-rays and
user-listed cut grids (see [OVERFLOW](/software/overflow.md)). Roget & Sitaraman (2014) state
that unsteady problems with relative motion and elasticity require the overset grid assembly
"at each time step", which is why it must be as efficient as possible
([Roget & Sitaraman (2014)](/sources/roget-2014.md), §1).

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

**Mapped equations in parameter space.** Henshaw & Schwendeman (2006, §4.1, Eqs. (7)–(8))
and Banks et al. (2016, §4.2, Eq. (31)) write the mapping of a moving component grid as
$\mathbf x=\mathbf d_k(\mathbf r,t)$, with grid velocity $\mathbf u_g=\partial_t\mathbf
d_k(\mathbf r,t)$, and transform the Euler equations exactly to the fixed parameter space.
With the page-local area (volume) factor $\mathcal J=\det(\partial\mathbf x/\partial\mathbf r)$
(not the registry's $J$, which is the inverse metric Jacobian of the computational
coordinates) and summation over $m,n=1,\dots,n_d$, Banks et al.'s form reads
$$\partial_t\mathbf q+\frac{1}{\mathcal J}\frac{\partial}{\partial r_m}\Big(\mathcal J\frac{\partial r_m}{\partial x_n}\big(\mathbf F_n-u_{g,n}\mathbf q\big)\Big)+\frac{\mathbf q}{\mathcal J}\frac{\partial}{\partial r_m}\Big(\mathcal J\frac{\partial r_m}{\partial x_n}u_{g,n}\Big)=\mathbf 0 ,$$
where $u_{g,n}$ are the components of $\mathbf u_g$; Henshaw & Schwendeman's 2-D Eq. (8) is
the same equation with the reactive source on the right, written with the face fluxes
$\mathcal J(\partial r_m/\partial x_n)(\mathbf F_n-u_{g,n}\mathbf q)$ across the curves
$r_m=$ const. The last term is the dilatation of the control volume caused by the divergence
of the grid velocity; Henshaw & Schwendeman state that it is identically zero for grids that
only translate and rotate (§4.1). The time derivative acts on $\mathbf q$, not on
$\mathcal J\mathbf q$, and the discretization built on it is the "semi-conservative"
Godunov scheme of [shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md).
Because the equations are solved in a frame moving with each grid, "no interpolation is
required to transfer the numerical solution from component grids at old times to those at
new times as a result of the motion" (Henshaw & Schwendeman, §1, §4.1). Banks et al. state
that the fluid scheme "is adjusted to ensure free-stream preservation, including the case of
deforming grids", and that the overall fluid–solid approximation is free-stream preserving
(§4.2).

Horne & Mahesh (2021) use the arbitrary Lagrangian–Eulerian integral form on unstructured
meshes attached to moving bodies: the convective flux through each face carries the relative
normal velocity $(\mathbf u-\mathbf u_g)\cdot\mathbf n$ ([Horne & Mahesh (2021)](/sources/horne-2021.md),
§3.1, Eq. (1)); see [incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md).

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

**Incremental update and exposed points (Ogen).** Henshaw & Schwendeman (2006, §3.1) call the
Overture grid generator Ogen after every move. The update considers only the grids affected
by the motion, starts from the previous classification, identifies the receptors that have
become invalid, searches locally for new donor candidates and completes the classification;
if the local search fails, the full overlapping-grid algorithm is called (see
[donor search](/methods/donor-search.md) and [Overture](/software/overture.md)). Where an
overlying grid moves away, points that were holes or receptors at the old time become
discretization points at the new time. Henshaw & Schwendeman call them
[exposed points](/definitions/exposed-point.md) and give them values at the *previous* time
level(s) by interpolation from other grids, before the step is taken; they reject assigning
values at the new time because that "involves an implicit coupling between unknown values at
the new time level" (§3.2, Figs. 3–4). Meakin & Suhs and Henshaw & Schwendeman thus treat the
same event in two ways: the first forbids a hole point from becoming a field point without an
intermediate step as an interpolated point, which limits how far a hole moves per step; the
second lets it happen and fills the exposed point's old-time values by interpolation, with
no hole-motion limit stated.

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

**Reuse under rigid motion on partitioned and GPU assemblies.** Two later assemblers reuse
geometric data that rigid motion does not change. Roget & Sitaraman (2014, §3.3) build the
cell-to-cell neighbour lists of their partitioned unstructured meshes once, at the first time
step, "since the neighbor information is unchanged by mesh motion or deformation"; cell and
nodal resolutions are recomputed only for elastically deforming meshes. Their adaptive load
re-balance estimates each processor's load from the previous assembly and updates it
continuously, which, they state, keeps it "applicable to moving and deforming grid problems"
(§5). Horne & Mahesh (2021, §2) assume rigid motion of the cells within each mesh partition,
so the Morton ordering and the node connectivity of their GPU bounding-volume hierarchy stay
fixed after initialization and only the object vertices and bounding boxes are updated. See
[parallel and GPU overset grid assembly](/methods/parallel-overset-grid-assembly.md).

**Implicit hole cutting.** Lee & Baeder (2003) do not blank hole points: the solver updates
them, and their contamination argument requires that information from invalid points cannot
cross the thinnest fringe in one time step $\Delta t$; their test-point sweeps alternate
direction with the time-step counter
([Lee & Baeder (2003)](/sources/lee-2003.md), sub-items 3–4, pp. 6–9; see
[implicit hole cutting](/methods/implicit-hole-cutting.md)). Lee & Baeder do not address
Meakin & Suhs's hole-motion rule, and neither source discusses the other's setting (see the
qualification on [point classification](/definitions/point-classification.md)).

**Deforming grids.** Banks et al. (2016, §4.1, §4.3) let the component grids next to a
fluid–solid interface deform with it. After the interface points are advanced, a hyperbolic
grid generator regenerates these grids by marching from the interface, and Ogen recomputes
the connectivity ("cut holes, determine interpolation points") every step; Banks et al. call
the construction *deforming composite grids*. The algorithm is on
[fluid–structure interaction on overlapping grids](/methods/fluid-structure-interaction-on-overset-grids.md).

## Time stepping with moving grids

Henshaw & Schwendeman's algorithm (§3.4, Fig. 6) orders one step as follows:

1. every $n_{\mathrm{regrid}}$ steps, rebuild the [AMR](/methods/amr-on-overset-grids.md)
   hierarchy and transfer the solution to it;
2. move the grids to a *predicted* state at $t+\Delta t$, computed "to full design accuracy
   (second-order accuracy for the present application)";
3. update the connectivity with Ogen;
4. fill the exposed points;
5. advance the solution from the old grid to the predicted grid;
6. interpolate the overlapping-grid and AMR receptors and apply the boundary conditions;
7. correct the grid positions (rigid-body corrector).

The connectivity is not recomputed after the corrector, since it "is already known to
second-order accuracy from the predictor step" (§3.4). A single global time step is used for
all component and refinement grids, $\Delta t=C_{\mathrm{CFL}}\min_k\Delta t_k$ with the
page-local safety factor $C_{\mathrm{CFL}}=0.9$ (§4.2, Eq. (13)). Banks et al.'s
fluid–structure procedure has the same predict–update–advance–project–correct structure
(§4.3, Procedure 1).

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

Free motion is integrated inside the solver in the later sources:
- Henshaw & Schwendeman (2006, §2, §4.3) integrate the Newton–Euler equations of rigid
  bodies loaded by the pressure force and torque, with a leap-frog predictor and a
  trapezoidal corrector, both second order.
- Chan (2009, §10) recalls that OVERFLOW-D (Meakin, early 1990s) added prescribed motion,
  6-DOF dynamics, body contact detection and impact dynamics, merged into OVERFLOW 2 in 2001.
- Horne & Mahesh (2021, §1) integrate 6-DOF rigid-body motion from the fluid forces and
  torques.

The coupling algorithms, rigid and deformable, are on
[fluid–structure interaction on overlapping grids](/methods/fluid-structure-interaction-on-overset-grids.md).

## Demonstrations

The moving-grid demonstrations of the founding papers all use prescribed motion (see
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

Later sources add verified moving-grid accuracy, free motion and timings:

- **Receding piston** (Henshaw & Schwendeman, §6.2, Tables 2–3): a 1-D piston with
  prescribed motion $-t^4/8$, computed on one translating grid and on a moving grid that cuts
  a hole in a fixed grid. The two constructions have nearly equal max-norm errors, with rates
  2.04–2.47 at $t=1$, so the overlapping moving-grid construction keeps second-order
  accuracy. The pressure-driven variant couples the piston's motion to the gas (see
  [fluid–structure interaction](/methods/fluid-structure-interaction-on-overset-grids.md)).
- **Smoothly accelerating cylinder** (Henshaw & Schwendeman, §6.3.1, Table 4): a cylinder of
  radius 1/2 moving through a channel on an annular grid over a Cartesian background, with
  self-convergence max-norm rates 2.03, 1.83 and 1.84 for $\rho$, $v$, $T$ at $t=6$ with the
  authors' slip-wall boundary condition (see
  [shock capturing](/methods/shock-capturing-on-overset-grids.md)).
- **Shock-driven cylinder and 26 cylinders in a detonation** (Henshaw & Schwendeman, §6.3.2,
  §7.2): free rigid bodies driven by shocks and detonations, with AMR; with one refinement
  level the number of component grids ranges from 28 to about 400 during the 26-cylinder run.
  See [shock–cylinder interaction](/benchmarks/shock-cylinder-interaction.md).
- **HART-II rotor–fuselage** (Roget & Sitaraman, §6.1, Fig. 19): five near-body unstructured
  meshes, 7 million nodes, 256 processors (2.3 GHz AMD Opteron 6134). One overset assembly
  takes 1.3 s, 7% of the total time-step time, with the exact-inverse-map donor search, and
  2.6 s (14%) with the alternating digital tree; the 62-million-node version reaches an
  assembly-to-solver time ratio of 21% at 8192 processors after load re-balance (Fig. 24).
- **Rotating cylinder** (Sharma et al., §4.3.4): a near-body mesh rotating at rate 3 (surface
  speed over free-stream speed) inside a Cartesian background, lift converged in space and
  time and in agreement with the literature values the authors cite
  ([Sharma et al. (2021)](/sources/sharma-2021.md); see
  [flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)).
- **Freely falling sphere** (Horne & Mahesh, §4.2.3, Fig. 20): a 6-DOF sphere (Galileo
  number 291, mass ratio 7.8) on 2 nodes with 2 NVIDIA V100 each; the GPU method is 12x–20x
  faster than the authors' earlier CPU method over 100 time steps, despite dynamic
  connectivity. Only timings are reported. See [flow past a sphere](/benchmarks/flow-past-sphere.md).
- **E779A propeller** (Wang et al. (2021), §III A): a rotating cylindrical overset region
  around the four-bladed propeller inside a stationary background, 48 million hexahedral
  cells in total, advance coefficient 0.38 at 25 rotations per second, one time step per
  $1^\circ$ of rotation, 30 rotations (statistics over the last 20, 7200 steps). The receptor
  ("acceptor") cells form a layer of a few cells on the outer surface of the rotating region
  and around a hole in the background; trilinear interpolation from an 8-point donor cell is
  used, and new interpolation coefficients are computed every time the propeller grid
  rotates.
- **Production applications** recalled by Chan (2009, §11): the V-22 tiltrotor in forward
  flight as one of the first overset applications with complex bodies in relative motion, SRB
  separation, wing–store and cavity store separation, a spinning missile with dithering
  canards, a dart dispenser with contact detection and impact dynamics (Fig. 8), and a CH-47
  dual-rotor helicopter with coupled CFD and structural dynamics (Fig. 9). No grid sizes or
  timings are given for these.

## Frames, rigid translation and deforming components

Three 2022 sources move component grids differently:

- [Hedayat et al. (2022)](/sources/hedayat-2022.md) solve each moving curvilinear grid in a non-inertial frame attached to its body, so its metrics are never recomputed, while the background stays inertial; interpolated velocities are rotated between frames (§2.1, §2.3).
- [Zhao et al. (2022)](/sources/zhao-2022.md) only translate a Cartesian overset grid with the body's centre-of-mass velocity; rotation and deformation are carried by the immersed-boundary points, so the grid is never regenerated (§II).
- [Delcour et al. (2022)](/sources/delcour-2022.md) deform a body-fitted component mesh as a fictitious linear-elastic solid with a free outer boundary around a flexible cylinder (§3.3).

[Chandar & Sitaraman (2022)](/sources/chandar-2022.md) show that on a rotating inner mesh the force oscillates in step with the number of receptors, as cells switch between field and receptor status; RBF interpolation lowers the force error by two orders of magnitude against inverse distance, and their conservation correction lowers the oscillation magnitude (§3.7.6). [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md) interpolate only when a hole cell becomes active as the foreground grid moves ([ADER schemes on overlapping grids](/methods/ader-on-overset-grids.md)). [Wang & Stern (2022)](/sources/wang-2022.md) and [Li & Wang (2022)](/sources/li-2022.md) run dynamic overset grids for planing hulls with two degrees of freedom and for rotating turbine and rotor blades. [Kochi & Ramakrishna (2022)](/sources/kochi-2022.md) use static grids only.

## Qualifications

- Meakin & Suhs state that the effect of the inter-grid boundary updating on time accuracy
  "has not been addressed" (§IV); their time-accuracy evidence is the single-grid plunge tests,
  and the moving multi-grid cases have no reference data. Henshaw & Schwendeman's piston and
  accelerating-cylinder tests (§6.2–6.3) measure convergence rates of time-dependent
  solutions on moving overlapping grids, against an exact solution and by self-convergence.
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
- **Geometric conservation.** None of the sources discusses a discrete geometric conservation
  law by name. Banks et al. (2016) state free-stream preservation on deforming grids (§4.2);
  Henshaw & Schwendeman evaluate the dilatation term with metrics and grid velocity averaged
  between $t$ and $t+\Delta t$ (§4.2) and rely on its vanishing for rigid motion.
- Henshaw & Schwendeman's exposed-point test is printed with a strict inequality that does not
  reproduce their own Fig. 4 example; the details are on
  [exposed points](/definitions/exposed-point.md).
- Henshaw & Schwendeman's claim that the total cost is "similar to that required for a
  Cartesian-grid embedded-boundary method" (§1) is asserted; Table 6 supports only the small
  share of the moving-grid update, 0.66 s of 17.8 s per step (3.7%) without AMR and 0.164 s of
  3.81 s (4.3%) with AMR, on a 2.2 GHz Xeon desktop.
- Wang et al. (2021) state no hole-cutting method, overlap width or interpolation accuracy for
  their rotating grid and do not discuss the tip vortices crossing the outer surface of the
  rotating region; the propeller case validates loads and wake topology against experiment
  without a grid-convergence study (§III B).
- Horne & Mahesh's falling-sphere case reports speed-ups only; trajectory accuracy is not
  shown in that paper (§4.2.3).
- Noack's C130 setup times (256 s reading and orienting cells, 14 s binary tree, 79 s
  donor-search octree) sum to 349 s, while the text prints a total of 335 s; the
  wing/pylon/store setup total (6 + 261 + 16 = 283 s) is consistent (§VIII) *(compiler check,
  not in the sources)*.

# Citations

- [Meakin & Suhs (1989)](/sources/meakin-1989.md) — §I; §II ADF (Eqs. (1)–(2)), BDF, DCF (Fig. 3, Table 1); §III (Figs. 4–5, 11, Plates 1–2); §IV.
- [Noack (2005)](/sources/noack-2005.md) — §I, §II, §VII (Fig. 10), §VIII (Tables 2–3).
- [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) — §1; §2 (Newton–Euler); §3.1 (Ogen update); §3.2 (exposed points, Figs. 3–4); §3.4 (Fig. 6); §4.1 (Eqs. (7)–(8)); §4.2 (Eq. (13)); §4.3; §6.2–6.3 (Tables 2–4, 6); §7.2.
- [Banks et al. (2016)](/sources/banks-2016.md) — §4.1 (deforming composite grids), §4.2 (Eq. (31), free-stream preservation), §4.3 (Procedure 1).
- [Chan (2009)](/sources/chan-2009.md) — §2 (relative motion as motivation), §7 (analytic shapes, object X-rays), §10 (OVERFLOW-D), §11 (applications, Figs. 4, 8, 9).
- [Roget & Sitaraman (2014)](/sources/roget-2014.md) — §1 (assembly at each time step), §3.3 (neighbour lists once, resolutions for deforming meshes), §5 (adaptive load estimate), §6.1–6.2 (Figs. 19, 24).
- [Horne & Mahesh (2021)](/sources/horne-2021.md) — §1 (6-DOF), §2 (rigid-motion reuse of the BVH), §3.1 (Eq. (1), ALE form), §4.2.3 (Fig. 20).
- [Sharma et al. (2021)](/sources/sharma-2021.md) — §4.3.4 (rotating cylinder).
- [Wang et al. (2021)](/sources/wang-2021.md) — §III A (dynamic overset grid, Fig. 5, Eq. (10), time step), §III B.
- [Benek et al. (1985)](/sources/benek-1985.md) — pp. 323, 325 (static PEGSUS/XMER3D workflow).
- [Rogers et al. (2003)](/sources/rogers-2003.md) — p. 1038 (PEGASUS 4 restart), p. 1042 (PEGASUS 5 restart).
- [Wang (1995)](/sources/wang-1995.md) — §6.
- [Lee & Baeder (2003)](/sources/lee-2003.md) — sub-items 3–4, pp. 6–9.
- [Hedayat et al. (2022)](/sources/hedayat-2022.md) — §2.1, §2.3.
- [Zhao et al. (2022)](/sources/zhao-2022.md) — §II.
- [Delcour et al. (2022)](/sources/delcour-2022.md) — §3.3.
- [Chandar & Sitaraman (2022)](/sources/chandar-2022.md) — §3.7.6.
- [Bergmann et al. (2022b)](/sources/bergmann-2022-b.md) — §4.4.
- [Wang & Stern (2022)](/sources/wang-2022.md) — §4.3.
- [Li & Wang (2022)](/sources/li-2022.md) — §5.

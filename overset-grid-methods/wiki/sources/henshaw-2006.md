---
type: Source
title: "Henshaw & Schwendeman (2006) — Moving overlapping grids with adaptive mesh refinement for high-speed reactive and non-reactive flow"
description: "Combines moving composite overlapping grids with block-structured adaptive mesh refinement on every component grid for the reactive Euler equations with rigid bodies, introducing exposed points, an incremental Ogen connectivity update, a predictor–corrector moving-grid algorithm and second-order slip-wall conditions, verified against exact and self-convergence solutions."
resource: "doi:10.1016/j.jcp.2006.01.005"
source_kind: paper
authors: [Henshaw W.D., Schwendeman D.W.]
year: 2006
venue: "J. Comput. Phys. 216:744-779"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2006_Crossref_Journal_of_Computational_Physics_Henshaw_Moving_overlapping_grids_with_adaptive_mesh_refinement_for_h.pdf"
tags: [composite-grid, moving-grid, shock-capturing, compressible, domain-connectivity]
timestamp: 2026-11-02T14:53:00Z
---

# Summary

Henshaw and Schwendeman solve the inviscid reactive and non-reactive Euler equations in
two-dimensional domains that change in time, on [moving](/methods/moving-overset-grid.md)
[composite overlapping grids](/definitions/composite-overlapping-grid.md) combined with
block-structured [adaptive mesh refinement](/methods/amr-on-overset-grids.md). Body-fitted
component grids follow moving boundaries or free rigid bodies and overlap fixed Cartesian
background grids. Refinement patches are built in the parameter space of every component grid, as
restrictions of its mapping, so they move with their base grid; earlier work by Meakin refined
only the Cartesian background grids.

The equations are transformed exactly to the fixed parameter space of each moving grid and solved
in a frame moving with it, so the motion needs no interpolation from old to new grids. Each step
follows one algorithm: predict the grids, rebuild the [domain connectivity](/definitions/domain-connectivity.md)
with Ogen (part of [Overture](/software/overture.md), successor of [CMPGRD](/software/cmpgrd.md)),
fill [exposed points](/definitions/exposed-point.md), advance, interpolate, apply boundary
conditions, correct the grids. Ogen's update reuses the previous
[point classification](/definitions/point-classification.md) and runs a local
[donor search](/methods/donor-search.md) for invalidated receptors. It falls back to the full
algorithm, [hole cutting](/methods/hole-cutting.md) included, when the local search fails.
Exposed points are uncovered by the motion; they receive old-time values by interpolation from
other grids.

The flow solver is a second-order slope-limited Godunov scheme with a Roe solver in
semi-conservative form, with Strang splitting for stiff chemistry (see
[shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md)). Rigid bodies
obey the Newton–Euler equations, integrated by a leap-frog predictor and trapezoidal corrector
([fluid–structure interaction](/methods/fluid-structure-interaction-on-overset-grids.md)). New
slip-wall conditions use a normal-pressure compatibility condition and limited extrapolation.
Verification uses exact solutions (supersonic expansion, receding pistons) and self-convergence
(accelerating cylinder, [shock-driven cylinder](/benchmarks/shock-cylinder-interaction.md), with and
without AMR); moving-grid generation costs under 5% of a step. Demonstrations show detonation
initiation by an impulsively moved cylinder and a detonation crossing 26 free cylinders. The
[inter-grid interpolation](/methods/inter-grid-interpolation.md) is tensor-product Lagrange in the
donor parameter space, its width not stated here.

# Version read

The Elsevier version of record (J. Comput. Phys. 216:744–779, received 9 September 2005, online
14 February 2006), 36 pages, all read; equations garbled in the text layer were read from the page
images. Page 1 matches the Crossref card. This is the JCP moving-grid and AMR paper, not the SISC
Maxwell paper [Henshaw (2006)](/sources/henshaw-2006-b.md).

# Key claims

1. Refinement grids are restrictions of the base-grid mapping in parameter space,
   $\mathbf d_{k_r}(\mathbf r,t)=\mathbf d_k(\mathbf R_{k_r}(\mathbf r),t)$ with
   $\mathbf R_{k_r}(\mathbf r)=(a_1+b_1r_1,a_2+b_2r_2)$, so they move with their base grid without
   moving in its parameter coordinates; only receptors whose donors lie on grids of *other* base
   grids need updating when grids move. (§3.3) **Derived**
2. The equations are solved in a frame moving with each grid, so "no interpolation is required to
   transfer the numerical solution from component grids at old times to those at new times as a
   result of the motion". (§1, §4.1) **Stated**
3. After the grids move, Ogen recomputes the point classification only for grids affected by the
   motion, starting from the previous classification and searching locally for new donors of
   invalidated receptors; it falls back to the full overlapping-grid algorithm when the local
   search fails. (§3.1) **Stated**
4. Exposed points (in $\mathcal H_k$ or $\mathcal R_k$ at the old time, needed by the discretization
   at the new time) receive values at *previous* time levels by interpolation from other grids;
   assigning values at the new time instead "involves an implicit coupling between unknown values at
   the new time level" and is judged harder. (§3.2) **Stated**
5. An old-time unused point $\mathbf i$ is exposed if some new-time discretization point $\mathbf j$
   of the same grid satisfies $\max_m|i_m-j_m|<(q_{\mathrm d}-1)/2$, $q_{\mathrm d}$ the
   discretization stencil width. (§3.2) **Stated** (see Printed slips)
6. The connectivity is not recomputed after the corrector step of the rigid-body integrator; it "is
   already known to second-order accuracy from the predictor step". (§3.4) **Stated**
7. For grids that only translate and rotate, the dilatation term of the mapped equation (8), from
   the divergence of the grid velocity $\mathbf u_g$, vanishes identically. (§4.1) **Derived**
8. One global time step $\Delta t=0.9\min_k\Delta t_k$ over all component grids, refinement grids
   included; no local time stepping on refinement levels. (§4.2, Eq. (13)) **Stated**
9. The leap-frog predictor and trapezoidal corrector for the Newton–Euler equations is second order;
   leap-frog is chosen for its low dissipation for purely imaginary eigenvalues, the corrector
   handles perturbations off the imaginary axis. (§4.3) **Stated**
10. The slip-wall condition SW-BC sets the ghost temperature from the normal-momentum compatibility
    condition $\rho^{-1}\partial_np=-\tilde u_2\,\mathbf n\cdot\partial_{r_2}\mathbf u-\mathbf n\cdot\partial_t\mathbf u_g$
    (Eq. (14)), $\tilde u_2=\nabla r_2\cdot(\mathbf u-\mathbf u_g)$, and the other variables by
    limited third-order extrapolation; it is second order for smooth solutions and drops to
    first-order extrapolation near discontinuities. (§5, Eqs. (17)–(20)) **Derived** (accuracy
    **Shown** in §6)
11. A density compatibility condition, valid only for isentropic flow, is avoided because entropy is
    not constant across shocks. (§5) **Stated**
12. Steady Mach 1.5 supersonic expansion over a smooth wall, single grid: max-norm rates $\sigma$ =
    1.84 ($\rho$), 1.77 ($u$), 1.95 ($v$), 1.88 ($T$). (§6.1, Table 1) **Shown**
13. Specified piston motion $g(t)=-t^4/8$: a single moving grid and a moving grid that cuts a hole in
    a fixed grid give nearly equal errors, with max-norm rates 2.04–2.47, so the moving overlapping
    construction keeps second order. (§6.2.1, Table 2) **Shown**
14. Pressure-driven piston ($m_b=2$, area 1): rates 0.71 (max norm), 1.32–1.34 (1-norm), about 1.05
    (2-norm), consistent with linear-advection theory for non-smooth solutions; piston position and
    velocity errors at $t=1$ fall by a factor 3.7 per halving of the spacing. (§6.2.2, Table 3,
    Fig. 13) **Shown**
15. Smoothly accelerating cylinder at $t=6$: estimated max-norm rates 2.03/1.83/1.84 ($\rho$, $v$,
    $T$) with SW-BC and 1.56/1.04/1.57 with the symmetry condition SW-SYM, whose errors are
    significantly larger and whose pressure contours are not smooth at the curved wall. (§6.3.1,
    Table 4, Fig. 15) **Shown**
16. Shock-driven cylinder (Mach 1.5 shock, cylinder mass 1/2): estimated 1-norm rates 1.47–1.49 at
    $t=1$. (§6.3.2, Table 5) **Shown**
17. AMR runs of equal effective resolution ($\mathcal G^{(2,2)}$, $\mathcal G^{(8,1)}$) and the uniform
    $\mathcal G^{(32,0)}$ give position, velocity and force curves "in excellent agreement". (§6.3.2,
    Fig. 18) **Shown**
18. CPU time per step on a 2.2 GHz Xeon: moving grids without AMR 17.8 s, of which 16.36 s (91.6%)
    is the flux update and 0.66 s (3.7%) moving-grid generation; with AMR 3.81 s, of which 2.43 s
    update, 0.552 s interpolation, 0.211 s regridding and 0.164 s (4.3%) grid generation. The AMR
    overhead is "about 20%" and the moving-grid update under 5% in both cases. (§6.3.2, Table 6)
    **Shown**
19. Because grid generation for moving overlapping grids is cheap, the total cost is similar to that
    of a Cartesian embedded-boundary method. (§1) **Stated** (Table 6 supports the grid-generation
    share only)
20. Detonation initiation by an impulsively moved cylinder: the shock position on the symmetry line
    converges with resolution, the von Neumann pressure peak is not fully converged on the finest
    grid, and the cylinder's position, velocity and force converge well. (§7.1, Fig. 21) **Shown**
21. A Chapman–Jouguet detonation crossing 26 free cylinders forms a local detonation in front of each
    impacted cylinder, which speeds the overall detonation beyond the steady CJ wave; with one AMR
    level the number of component grids ranges from 28 to about 400. (§7.2) **Shown** (qualitative)
22. Meakin combined moving overlapping grids and AMR but restricted refinement to the Cartesian
    background grids; refining any component grid is "more general". (§1) **Stated**
23. Overlapping grids are a synthesis of fixed-grid (embedded-boundary, immersed) and
    boundary-conforming (ALE, moving unstructured) approaches: most points lie on Cartesian grids, and
    "the irregular boundary associated with standard Cartesian grid methods takes the form of the
    interpolation boundary between overlapping grids". (§1) **Stated**

# Printed slips

- **Fig. 20 caption:** "at times t = 0.25 (left column) and t = 0.035 (right column)"; the text of
  §7.1 and the panel labels give $t=0.35$.
- **Fig. 19 caption:** "for the shock-driven cylinder calculation at t = 1"; §6.3.2 says the figure
  shows the AMR grids "at time t = 1.5", compared with the last frame of Fig. 16 ($t=1.5$).
- **Ref. [46]** prints "T. Poinsot, S. Lee", while §5 cites "Poinsot and Lele [46]".
- **Exposed-point test (§3.2).** With the 3-point stencil of the Fig. 4 example, the printed strict
  inequality $\max_m|i_m-j_m|<(q_{\mathrm d}-1)/2=1$ fails for $|1-2|=1$, yet the text declares
  $u_1^n$ exposed; a non-strict $\le$ would match the example *(compiler check, not in the
  sources)*.
- **§6.1 grid sequence.** The text defines $\Delta r_m^{(j)}=\Delta r_m^{(1)}/2^{j-1}$, but Table 1
  uses $j=1,2,4$. The printed density errors (1.2e-3, 3.3e-4, 9.6e-5) give rate 1.82 over a total
  spacing ratio 4 (printed 1.84) and 1.21 over ratio 8, so the table matches spacing $\propto1/j$,
  the convention of §6.2–6.3 *(compiler check, not in the sources)*.
- **§7.1 spacing.** The "representative grid spacing for both component grids is $h_j=2/(5j)$".
  The printed Cartesian ($2/(50j)$, $(3/2)/(75j/2)$) and radial ($0.24/(6j)$) definitions give
  $0.04/j$, and only the printed $N_\theta$ formula gives $2/(5j)$: a factor 10 that the paper does
  not let one assign to either side *(compiler check, not in the sources)*.
- **§6.3:** $N_R$, $N_\theta$, $N_x$, $N_y$ are called "the number of grid lines", while the grid
  constructors use $i_m=0,\dots,N_m$ (intervals); the constructors are written with $N_1,N_2$.
- **Table 6:** the listed rows sum to 17.152 s against the printed total 17.8 s (moving) and to
  3.4354 s against 3.81 s (moving + AMR) *(compiler check, not in the sources)*.
- Fig. 14 caption "smoothing accelerated cylinder"; §5 "taken to by zero"; ref. [36]
  "Sotiropolous" against "Sotiropoulos" in refs. [23]–[25].

# Notation map

| Henshaw & Schwendeman (2006) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathcal G(t)=\{G_g(t)\}$, $g=1,\dots,\mathcal N$ | $\mathcal G=\{G_k\}$, $n_g$ | $\mathcal N$ counts refinement grids too |
| $d$ | $n_d$ | |
| $\mathbf x=\mathbf G_g(\mathbf r,t)$ | $\mathbf x=\mathbf d_k(\mathbf r,t)$ | time-dependent mapping, fixed parameter space |
| $\mathbf G_{g_r}$, $\mathbf R_{g_r}$ | $\mathbf d_{k_r}$, $\mathbf R_{k_r}$ (page-local) | refinement-grid mapping and restriction map |
| $J=\lvert\partial(x_1,x_2)/\partial(r_1,r_2)\rvert$ | $\mathcal J=\det(\partial\mathbf x/\partial\mathbf r)$ (page-local, as on [moving overset grids](/methods/moving-overset-grid.md)) | **the inverse of the registry's Pulliam–Steger $J$ (up to the scaling $\Delta r_m$)** |
| $\dot{\mathbf G}$, $\ddot{\mathbf G}$ | $\mathbf u_g$, $\partial_t\mathbf u_g$ | grid velocity and acceleration |
| $\mathbf v=(v_1,v_2)$ | $\mathbf u=(u,v)$ | velocity |
| $\mathbf u=[\rho,\rho\mathbf v,E,\rho\mathbf Y]^T$, $\mathbf f_1,\mathbf f_2$ | $\mathbf q$ (with species), $\mathbf F_1,\mathbf F_2$ | **the source's $\mathbf u$ is the conserved vector, not the velocity** |
| $\tilde v_k=\nabla_{\mathbf x}r_k\cdot(\mathbf v-\dot{\mathbf G})$ | $\tilde u_k$ (page-local) | unnormalized relative normal velocity |
| $V_1$, $V_2$ | grid-velocity fluxes (page-local) | **not the registry's contravariant $V$** |
| discretization, interpolation, unused points | $\mathcal D_k$, $\mathcal R_k$, $\mathcal H_k$ | no mask values printed; ghost points separate |
| exposed point | exposed point | paper's term |
| $w$ | $q_{\mathrm d}$ | 5 for the Godunov scheme |
| $\Delta_{0k}$, $\Delta_{\pm k}$ | undivided $D_{0m}$, $D_{\pm m}$ | |
| $D_{0,r_k}$, $D_{0,n}$ | $D_{0m}$, discrete normal derivative | |
| $\mathcal G^{(j,\ell)}$, $l$, $n_r$, $n_{\rm regrid}$ | page-local | base resolution $j$, at most $\ell$ levels of ratio $n_r=4$ |
| $\sigma$ (§6) | $\sigma$ | observed rate; **also the Arrhenius rate constant in Eq. (24)** |
| $\sigma_{\rm CFL}$ | CFL safety factor 0.9 | |
| $M^b$, $\mathbf F^b$, $\mathbf T^b$, $\mathbf x^b$, $\mathbf v^b$, $\boldsymbol\omega$, $\mathcal I_k$ | $m_b$, $\boldsymbol{\mathcal F}$, $\boldsymbol{\mathcal M}$, $\mathbf x_{\mathrm{cg}}$, $\mathbf v_{\mathrm{cg}}$, $\boldsymbol\omega_b$, principal moments of $\mathsf I_b$ | **the source's $M$ is a mass, not the Mach number** |
| $E(t)E^{-1}(0)$ ($E$ the matrix of principal axes $\mathbf e_k$) | $\mathsf R(t)\,\mathsf R(0)^{-1}$ | **$E$ is the total energy in the registry** |
| $T=p/\rho$, $R$, $U$, $V$, $\mathcal T$, $\mathcal Y$ | temperature (gas constant absorbed), discrete $\rho,u,v,T,Y$ | page-local |
| $q$ (chemical heat), $Q$, $Y$, $\epsilon$ | page-local | **$q$ is the interpolation width in the registry**; $\epsilon$ also the limiter guard |
| $\kappa$, $\mathbf Q_{\mathbf i}$ | dilatation coefficient and term | page-local |

# Reference list

50 printed references, numbered [1]–[50], all merged complete into the
[bibliography](/bibliography.md) with `citedby` henshaw-2006. Two Starius works of 1977 take
suffixes in printed order (`starius-1977`, `starius-1977-b`). Ref. [35], Lee and LeVeque's immersed
interface method, is keyed `lee-2003-b` because `lee-2003` is the ingested Lee and Baeder paper.
Ref. [10] is [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) and ref. [21]
[Henshaw (1994)](/sources/henshaw-1994.md). Ref. [34] (Peskin, Acta Numer. 2002) prints no volume;
ref. [46] prints the second author as "S. Lee" (see Printed slips). No printed duplicates.

# Pages created or updated

Chunk 2 (2026-11-02). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Shock–cylinder interaction](/benchmarks/shock-cylinder-interaction.md)
- [Composite overlapping grid](/definitions/composite-overlapping-grid.md)
- [Domain connectivity and overset grid assembly](/definitions/domain-connectivity.md)
- [Exposed points](/definitions/exposed-point.md)
- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Point classification and the iblank mask](/definitions/point-classification.md)
- [Adaptive mesh refinement on overlapping grids](/methods/amr-on-overset-grids.md)
- [Conservative overset interface](/methods/conservative-overset-interface.md)
- [Donor search](/methods/donor-search.md)
- [Fluid–structure interaction on overlapping grids](/methods/fluid-structure-interaction-on-overset-grids.md)
- [Hole cutting](/methods/hole-cutting.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Moving overset grids](/methods/moving-overset-grid.md)
- [Shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md)
- [Twilight-zone flow (manufactured solutions)](/methods/twilight-zone-flow.md)
- [CMPGRD and its solver suite (CGINS, CGNVT, CGES, CGMG, DSK)](/software/cmpgrd.md)
- [Overture (and its grid generator Ogen)](/software/overture.md)

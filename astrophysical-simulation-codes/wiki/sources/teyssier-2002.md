---
type: Source
title: "Teyssier (2002) — Cosmological Hydrodynamics with Adaptive Mesh Refinement — A New High Resolution Code Called RAMSES"
description: "Code paper of RAMSES: cell-by-cell AMR on Khokhlov's fully threaded oct tree with a 3^d−1-neighbour grading rule and refinement-only criteria, ART-type particle-mesh N-body with a one-way-interface SOR Poisson solve per level, a second-order split or unsplit PLM Godunov scheme with an almost exact Riemann solver and refluxing, a single or a level-halving adaptive time step, and the claim that shocks leaving fine regions cause no detectable mesh artefact; tested on force accuracy, Sod, Sedov, a Mach 5000 level-jump shock, the Zel'dovich pancake and secondary infall."
resource: "doi:10.1051/0004-6361:20011817"
source_kind: paper
authors: [Teyssier R.]
year: 2002
venue: "Astron. Astrophys. 385:337–364"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2002-AA-Teyssier-1010510004-636120011817.pdf"
tags: [software, amr, cosmology, hydro, self-gravity, particles, riemann-solver, time-integration, verification]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper presents [RAMSES](/software/ramses.md), an N-body and
hydrodynamics code for cosmological structure formation built on
**cell-by-cell ("tree-based") AMR**: Khokhlov's (1998) fully threaded
tree, whose element is the oct of $2^d$ sibling cells over a regular
Cartesian coarse grid (§2.1). A grading rule requires every oct to be
surrounded by $3^d - 1$ neighbouring parent cells, and only refinement
criteria are needed, no derefinement criteria (§2.1.1). The N-body part
follows the ART code: cloud-in-cell deposit per level, an FFT Poisson
solve on the coarse grid and a "one-way interface" red–black SOR solve on
each finer level with Dirichlet data from the coarser one (§2.2). The
hydrodynamics is a second-order Godunov scheme (piecewise linear, MinMod
slopes, characteristic tracing), split or unsplit, with an "almost exact"
Riemann solver, refluxing at level boundaries and gravity as a
time-centred source (§2.3). Levels advance with one global step or with an
adaptive step that halves per level (§§2.1, 2.3.2). The tests support the
central claim that strong shocks moving from high to low resolution leave
no detectable mesh artefact, so cosmological runs may refine on density
only (§§3.5–3.7, 4). A $256^3$-particle ΛCDM run reaching a formal
resolution of $8192^3$ is analysed against the halo model (§4). The file
read is the arXiv preprint (see Citations).

# Key claims

Registry notation (level $l$, $l = 0$ the coarse grid; $h_l$, $d$,
$\Delta t_l$, $\Phi$, $\mathbf g$, $\nu$); see the Notation map.

1. **Fully threaded tree** (§2.1). The oct of $2^d$ cells at level $l$ is
   the basic element; the octs of a level form a doubly linked list; each
   oct points to its parent cell, to the $2d$ neighbouring parent cells at
   $l-1$ and to its $2^d$ child octs. Memory: "17 integers per oct for
   dim = 3, or equivalently 2.125 integers per cell". $d$ = 1, 2 or 3.
2. **Gather–scatter** (§2.1). Per level, a sub-sample of octs is gathered
   from the tree into arrays, updated "very efficiently on vector or
   parallel architectures", and scattered back.
3. **Grading rule** (§2.1.1). "any oct in the tree structure has to be
   surrounded by $3^{\mathrm{dim}}-1$ neighboring parent cells", which
   gives a smooth transition "even in the diagonal directions". The
   refinement map is built from $l_{\max}$ down to 0 in three passes: mark
   the parents of marked or refined children; mark their $3^d - 1$
   neighbours; apply the user criteria. Mesh smoothing expands the marked
   region by a cubic buffer $n_{\mathrm{expand}}$ times (twice in ART,
   "usually ... only once" in RAMSES, which uses buffer regions for level
   boundary data). **Only refinement criteria are needed; no derefinement
   criteria**, an "important difference" from ART and Khokhlov.
4. **Tree modification** (§2.1.2). Two passes from $l = 0$ up: create the
   child oct of a marked leaf; destroy the child oct of an unmarked split
   cell. The mesh is modified incrementally, never rebuilt. With adaptive
   steps a final check refuses refinements that would break the rule.
5. **Particles** (§2.2, eqs. 5–7). Particle-mesh steps on the AMR grid:
   per-oct particle lists; cloud-in-cell density per level, including
   clouds from particles in neighbouring parent cells, so the level-$l$
   density equals that of a uniform mesh of the same resolution (§2.2.2).
   A second-order midpoint (kick–drift–kick) integrator reduces to leapfrog
   for constant steps; with adaptive steps, particles crossing a refinement
   boundary see a factor-2 step jump and are only first order along those
   trajectories (§2.2.5).
6. **Poisson solver** (§2.2.3, eqs. 2–4). Coarse level: FFT with the Green
   function of the $(2d+1)$-point Laplacian. Finer levels: the "one-way
   interface" of Jessop et al. (1994) and Kravtsov et al. (1997): "the
   coarse grid solution never 'sees' the effect of the fine grids. The
   resulting accuracy is the same as if the coarse grid were alone", "it
   can not be better in any way"; "A better accuracy would be obtained
   using a two-way interface scheme", "left for future work". Dirichlet
   data in a buffer by linear reconstruction from level $l-1$; red–black
   Gauss–Seidel with over-relaxation, $\omega_{\mathrm{SOR}} \simeq
   2/(1+\pi/N)$ for Dirichlet and $2/(1+2\pi/N)$ for periodic boundaries,
   with $N$ replaced on AMR levels by the mean patch size in cells (eq. 4).
   Iterations stop when the residual 2-norm drops by $10^3$. Examples:
   $\omega_{\mathrm{SOR}} \simeq 1.9$ and 60 iterations for a $128^3$
   coarse grid fully refined to $256^3$; $\simeq 1.7$ and 20 iterations on
   a cosmological AMR level with mean patch size about 20; ART used 1.25.
7. **Acceleration** (§2.2.4). Symmetric 5-point gradient at cell centres
   (no self-force), interpolated back by inverse cloud-in-cell to particles
   whose cloud lies inside the level; otherwise from level $l-1$.
8. **Hydrodynamic equations** (§2.3, eqs. 8–11). Euler equations in
   conservative form with gravity sources in momentum and energy; total
   fluid energy conserved exactly without gravity; with gravity the total
   energy is conserved "at the percent level" (§4.3).
9. **Godunov scheme** (§2.3, eqs. 12–13; §2.3.1). Conservative update with
   time-centred fluxes from a second-order piecewise linear Godunov method,
   "with or without directional splitting (according to the user's
   choice)", after Colella (1990) and Saltzman (1994); gravity as a
   time-centred fractional step (eq. 13). Two ghost zones per side and
   direction, diagonals included: $3^d - 1$ neighbouring octs and a stencil
   of $6^d$ cells per oct. Characteristic tracing with gravity-corrected
   states, transverse terms in the unsplit option, MinMod slopes.
10. **Riemann solver** (§2.3.1). "Almost exact": the contact pressure by
    Newton–Raphson ("typically, for strong shocks 10 Newton-Raphson
    iterations are required for single-precision accuracy of $10^{-7}$"),
    the only approximation being a linear profile inside rarefactions.
11. **PPM rejected** (§2.3.1). PPM needs 4 ghost zones, "to expensive"
    [sic] with octs of $2^d$ cells; $4^d$-cell octs would cost flexibility;
    FLASH uses PPM with $8^d$ cells per tree element. The oct-wise stencil
    costs roughly 50 %, 100 % and 200 % extra CPU in 1, 2 and 3D on a full
    Cartesian grid (estimate; lower on real AMR meshes, not measured).
12. **AMR step** (§2.3.2), recursive in $l$: (1) new level-$(l+1)$ cells by
    conservative interpolation; (2) $\Delta t_l$ from the Courant condition
    with $\Delta t_l \le \Delta t_{l-1}$; (3) advance level $l+1$ once
    (single step) or twice (adaptive step); (4) reset $\Delta t_l$ to the
    fine step or to the sum of the two fine steps; (5) ghost data by
    conservative interpolation from level $l-1$ with "a 3D generalization
    of the Min-Mod limiter (De Zeeuw 1993)"; (6) fluxes; (7) coarse–fine
    fluxes replaced by averages of the level-$(l+1)$ fluxes; (8) update leaf
    cells; (9) split cells take the average of their updated children;
    (10) new refinement map.
13. **No temporal interpolation** (§2.3.2). "The coarse solution is assumed
    to remain constant in time during the advance of the fine solution":
    with the adaptive step the accuracy at coarse–fine boundaries drops
    "from second to first order in time, but the global solution remains
    second order (Khokhlov 1998)".
14. **Time stepping across levels** (§§2.1, 2.2.5, 2.3.2, 3.6, 4.2). Two
    schemes: one step for all levels, and an adaptive scheme "similar to a
    'W cycle'" (level 1 takes 2 steps, level 2 four, …). The single step is
    "more accurate (but time consuming)" (§2.2.5); for the 3D Sedov test it
    is "the fastest solution" (§3.6); the cosmological runs use the adaptive
    step (§4.2). No common-problem comparison is given.
15. **Time-step limits** (§2.4, eqs. 14–17). The minimum of: a safety
    factor times the smallest $t_{\mathrm{ff}}$ on the level; a safety
    factor times $h_l$ over the largest particle speed; about 10 % of
    $a/\dot a$ (early times only); and
    $\nu\,h_l/\max(\vert v_x\vert + c_s, \vert v_y\vert + c_s, \vert v_z\vert + c_s)$,
    $\nu < 1$.
16. **Refinement strategy** (§2.5, eqs. 18–21). Because the AMR overhead
    "can be as large as a factor of 2 to 3", "the maximum fraction of the
    grid that can be refined lies in between 30 % to 50 %" (an estimate).
    Quasi-Lagrangian criteria: refine where the dark-matter (or gas) density
    exceeds a mass per cell divided by $h_l^d$ (about 5–10 particles per
    cell for pure N-body, 40–80 for gas runs; the gas threshold scaled by
    the baryon fraction). Also a gradient criterion (relative jump to the
    $2d$ neighbours above a threshold), a second-derivative variant, and a
    purely spatial criterion (no refinement outside a sphere per level).
17. **Super-comoving coordinates** (§2.6, eqs. 22–25), after Martel &
    Shapiro (1998), with conformal time: for $\gamma = 5/3$ the equations
    keep their non-expanding form except the Poisson equation (eq. 25); for
    $\gamma \ne 5/3$ "a single additional source term" enters the energy
    equation. Boundaries: periodic, reflecting, inflow, outflow.
18. **Shocks across level jumps** (§3.5, Fig. 5; §§3.6–3.7, 4.2, 4.4). A
    Mach 5000 shock crossing from coarse to fine produces post-shock
    oscillations "of the order of 5 %"; from fine to coarse no visible
    oscillation. "if shock waves move from high- to low-resolution regions,
    spurious effects associated to the mesh structure are undetectable";
    weak shocks are undetectable either way (citing Berger & Colella 1989).
    Cosmological accretion shocks form in dense, highly refined regions and
    move outwards, so refining on density alone is "safe". The evidence is
    1D (§3.5) and spherically averaged 3D profiles (§3.6); oblique incidence
    is not tested separately.
19. **Effective resolution** (§§3.1, 3.8, 5). "the actual resolution limit
    of the code is equal to roughly twice the cell size of the maximum
    refinement level"; the point-mass force has resolution of about 1.5
    finest cells.
20. **Implementation** (§5). Fortran 90, optimized for the vector Fujitsu
    VPP 5000; a shared-memory OpenMP version; a distributed-memory
    domain-decomposition version "currently under construction". No scaling
    data. Planned: cooling, star formation, supernova feedback, zoom initial
    conditions.

# Tests

No convergence order or error norm is reported for any hydrodynamic test;
comparisons are visual or against analytic profiles. Figures were not seen
(placeholders in the file read); statements come from text and captions.

1. **Point-mass force** (§3.1, Fig. 1). $32^3$ coarse grid, 0–6 levels
   (formal $2048^3$), periodic images removed by Ewald summation. Force
   resolution about 1.5 finest cells; anisotropy "close to 1 %" at large
   radius; percent-level errors that do not decrease monotonically with
   level; percent-level force discontinuities between levels.
2. **ΛCDM particle force** (§3.2, Fig. 2). $64^3$ particles at $z = 0$,
   $32^3$ coarse grid, refinement above 40 particles; the AMR force against
   a PM force of equivalent resolution ($64^3$–$512^3$): strongly
   non-Gaussian errors "at the percent level in all cases", larger for
   small and intermediate forces, attributed to the level-boundary (tidal)
   conditions, "the main source of inaccuracy in the N-body scheme".
3. **[Sod shock tube](/benchmarks/sod-shock-tube.md)** (§3.3, Fig. 3).
   Standard states, $\gamma = 1.4$; 64 coarse cells, $l_{\max} = 6$ (formal
   4096); gradient criteria on $\rho$, $p$ and Mach number with threshold
   0.01; $\nu = 0.8$; $t = 0.245$. 560 cells (14 % of uniform); 69 coarse
   and 4416 finest steps; shocks over 2–3 zones, contacts over 6–10;
   pressure and velocity uniform across the contact; no artefacts from the
   refinement ratio.
4. **Planar [Sedov blast](/benchmarks/sedov-taylor-blast-wave.md)** (§3.4,
   Fig. 4). $\gamma = 1.4$, $\rho_0 = 1$, $p_0 = 10^{-5}$, energy 1/2 in the
   first cell, reflecting boundary, 32 coarse cells, 6 levels, $\nu = 0.8$.
   Correct shock speed, no visible post-shock oscillation; 239 coarse
   against 15296 finest steps; 130 cells against 2048 uniform (4.3 %).
5. **Strong shock through a level jump** (§3.5, Fig. 5; Khokhlov's test).
   Mach 5000, $\gamma = 5/3$, 256 cells, $\nu = 0.5$: uniform level 1;
   level 1 only left of cell 234 (fine-to-coarse crossing); level 2 right of
   cell 234 (coarse-to-fine). The first two show no visible oscillation; the
   third shows oscillations "of the order of 5 %".
6. **Spherical Sedov blast** (§3.6, Fig. 6). $32^3$ coarse, $l_{\max} = 6$,
   refinement confined to spheres of radius $2^{5-l}$ coarse cells
   (eq. 27), pressure-gradient threshold 0.5, energy 1 in the 8 central
   cells, $\gamma = 1.4$, $\nu = 0.8$, single time step; about $10^6$
   cells. "remarkable" agreement of spherically binned profiles; the main
   departure, in velocity near 60 % of the shock radius, is "Similar" to
   Fryxell et al. (2000); "Oscillations due to spurious mesh reflections
   are not visible in the radial profiles"; the only systematic effect is
   non-sphericity from the Cartesian mesh.
7. **[Zel'dovich pancake](/benchmarks/zeldovich-pancake.md)** (§3.7, Fig. 7,
   eqs. 28–30). Einstein–de Sitter, baryon fraction 0.1, collapse at
   $1+z = 10$, start at $1+z = 100$, cold gas, 32 coarse cells, 256
   particles, $l_{\max} = 6$ (formal 2048). Run A refines on density and
   pressure gradients (shocks refined), run B on density only; profiles
   "almost indistinguishable in the center", no oscillation in run B.
8. **Spherical secondary infall** (§3.8, Fig. 8, Bertschinger 1985).
   Self-similar baryonic infall, $\gamma = 5/3$, $32^3$ coarse,
   $l_{\max} = 6$, $\nu = 0.5$; about $10^5$ cells; 86 coarse against 5504
   finest steps; "very good agreement ... down to a radius of 2 fine cells,
   the actual resolution limit of the code".
9. **ΛCDM application** (§4, Tables 1–2, Figs. 9–13). $100\,h^{-1}$ Mpc
   box, six runs from $64^3$ to $256^3$ particles and 0–5 levels; the
   largest has $4.1\times10^7$ cells, finest cell $12.21\,h^{-1}$ kpc, 304
   coarse and 7281 finest steps; no shock refinement. Layzer–Irvine energy
   error at most 2 %, 1 % and 0.5 % for the three AMR runs compared; final
   cell count 2.5× the initial coarse count (mesh smoothing). The
   dark-matter power spectrum matches the halo model to the formal Nyquist
   frequency; the gas pressure spectrum agrees within a factor 2 and is not
   converged at small scales.

# Notation map

| Paper | Canonical | Note |
|---|---|---|
| $\ell$, $\ell_{\max}$ | $l$, $l_{\max}$ | $\ell = 0$ is the coarse Cartesian grid (Rosdahl et al. 2013 count the root oct as level 1) |
| dim | $d$ | |
| $\Delta x^\ell$ | $h_l$ | |
| oct ($2^{\mathrm{dim}}$ cells) | in words; $N_{\mathrm b} = 2$ | |
| refinement factor 2 | $r_{\mathrm{ref}} = 2$ | |
| 2 ghost zones | $n_{\mathrm g} = 2$ | |
| $\mathbf u$ | $\mathbf v$ | **collision**: registry $u$ is the state |
| $e$ (specific total energy), $\rho e$ | $E/\rho$, $E$ | **collision**: registry $e$ is the specific internal energy |
| $c$ (sound speed) | $c_s$ | **collision**: registry $c$ is the speed of light |
| $U_i^n$, $F^{n+1/2}_{i+1/2}$, $S_i^{n+1/2}$ | $u$, $\hat f_{i+1/2}$, $s(u)$ | |
| $\phi$, $-\nabla\phi$ | $\Phi$, $\mathbf g$ | |
| cfl | $\nu$ | |
| $\Delta t^\ell$ | $\Delta t_l$ | |
| $\omega$ | $\omega_{\mathrm{SOR}}$ | |
| $N$, $\langle L\rangle$ | $N$; in words | mean patch size; **collision**: $L$ is also the box size |
| $\alpha$ (eq. 4) | in words | boundary factor (1 Dirichlet, 2 periodic) |
| $t_{\mathrm{ff}}$, $a_{\mathrm{exp}}$ | $t_{\mathrm{ff}}$, $a$ | |
| $C_1$, $C_2$, $C_3$, $C_q$ | in words | safety factors and gradient threshold |
| $\rho_\ell$, $M_c$, $M_b$ | in words | refinement density threshold and mass per cell; **collision**: registry $\rho_{\mathrm{thr}}$ is the sink threshold |
| $n_{\mathrm{expand}}$, $R_\ell$ | in words | smoothing passes; refinement radius per level |
| $\mathbf x_p$, $\mathbf v_p$, $m_p$ | in words | particle position, velocity, mass |
| $H_0$, $\Omega_m$, $\Omega_b$, $\Omega_\Lambda$, $\rho_c$, $L$ | in words | cosmological parameters and box size |

# Pages created or updated

* Created this Source page.
* Created [RAMSES](/software/ramses.md).
* Updated [RAMSES-RT](/software/ramses-rt.md) (batch-10 section: the host
  code from its own paper; link to RAMSES).
* Updated [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
  (batch-10 section: the RAMSES row from the code paper, the grading rule,
  no temporal interpolation, refinement-only criteria, the level-jump shock
  test as a qualification of the general claim against FLASH's oblique
  case; evidence added to the Open subcycling entry).
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md)
  (batch-10 section: RAMSES's almost exact solver).
* Updated
  [Poisson solvers on adaptive meshes](/methods/multigrid-self-gravity.md),
  [particle-mesh gravity](/methods/particle-mesh-gravity.md),
  [Sod shock tube](/benchmarks/sod-shock-tube.md),
  [Sedov–Taylor blast wave](/benchmarks/sedov-taylor-blast-wave.md) and
  [Zel'dovich pancake](/benchmarks/zeldovich-pancake.md).

# Citations

1. Teyssier R. (2002), "Cosmological hydrodynamics with adaptive mesh
   refinement. A new high resolution code called RAMSES", Astron.
   Astrophys. 385(1):337–364, doi:10.1051/0004-6361:20011817. Local file:
   `/home/stefano/papers/mosaic/astrophysical-simulation-codes/2002-AA-Teyssier-1010510004-636120011817.pdf`.
   * **Version read.** The archive file is the **arXiv preprint
     astro-ph/0111367v1** (19 Nov 2001), the submitted A&A manuscript
     ("Accepted ??? / Received ???"): 21 text pages and 13 figure
     placeholder pages ("This figure ... is available in 'jpg' format from
     arxiv.org"). Section, equation and table numbers are those of v1 and
     may differ from the published pages; the published text may differ
     (the referee is already thanked in v1).
   * **Identity.** Checked on Crossref: "Cosmological hydrodynamics with
     adaptive mesh refinement" (Crossref drops the subtitle), single author
     R. Teyssier, Astronomy & Astrophysics vol. 385, issue 1, pp. 337–364,
     issued 2002-04. The slug follows the issue year.
   * **How it was read.** Text layer, with pages 5, 6 and 8 rendered for
     the equations. Figures 1–13 were not available. Eqs. 31 and 44–46
     (infall turn-around radius, halo gas profiles) were read from the text
     layer only and are not reproduced (outside the bundle's scope).
   * **Recorded as printed.** (a) Eq. 13 prints the gravity source without
     the minus sign of eqs. 9–10, and its energy component as
     $(\rho u)\nabla\phi$ without a dot product; not corrected. (b) Eq. 3
     puts $\omega$ on the old iterate and $(1-\omega)$ on the Gauss–Seidel
     value, which for $1 < \omega < 2$ is not standard over-relaxation
     (reader's reading: a probable typo; the published version not
     checked). (c) "to expensive" and "rouhly" as printed.
   * **Reference list:** 61 printed entries (A&A style, no article titles),
     all merged. The list prints "Collela" for Colella three times (Berger
     & Colella 1989, Colella 1990, Colella & Woodward 1984); the three land
     on `berger-1989`, `colella-1990` and `colella-1984` by venue. Bryan &
     Norman in the 12th Kingston Meeting (ASP Conf. Ser. 123) is
     `bryan-1997-b`, printed with pp. 363–364. De Zeeuw's PhD thesis
     (University of Michigan) is the new `dezeeuw-1993-b`, distinct from
     `dezeeuw-1993` (Dezeeuw & Powell, J. Comput. Phys. 104:56). Kravtsov &
     Klypin, Astrophys. J. 520:437, is `kravtsov-1999-b`, distinct from the
     thesis `kravtsov-1999`. Cooray (2001, Phys. Rev. D, in press),
     Refregier & Teyssier (2001, A&A, submitted) and Varnieres & Arnaud
     (2001, in preparation) carry status notes. Bibliography: 2522 entries.

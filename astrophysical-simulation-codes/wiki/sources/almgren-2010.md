---
type: Source
title: "Almgren et al. (2010) — CASTRO: A new compressible astrophysical solver. I. Hydrodynamics and self-gravity"
description: "Method paper of CASTRO, a BoxLib block-structured AMR code for multicomponent compressible Euler with a general EOS: unsplit PPM with characteristic tracing and full corner coupling, a two-shock-type Riemann solver, Strang-split reactions, time-centred gravity sources, subcycled Berger–Oliger AMR with refluxing, and a multilevel Poisson synchronization, with weak scaling to 64,000 processes."
resource: "doi:10.1088/0004-637X/715/2/1221"
source_kind: paper
authors: [Almgren A.S., Beckner V.E., Bell J.B., Day M.S., Howell L.H., Joggerst C.C., Lijewski M.J., Nonaka A., Singer M., Zingale M.]
year: 2010
venue: "Astrophys. J. 715:1221–1238"
local_file: "~/papers/mosaic/astrophysical-simulation-codes/2010-ApJ-Almgren-1010880004-637X7152-1221.pdf"
tags: [software, hydro, amr, self-gravity, multigrid, unsplit, riemann-solver, dual-energy, performance, benchmark]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

CASTRO is an Eulerian, block-structured AMR code for the multicomponent
compressible Euler equations with a user-supplied EOS, self-gravity,
nuclear reactions and (in Part II) radiation (§1, §2). The hydrodynamics is
an unsplit second-order Godunov method: PPM reconstruction of primitive
variables with an extremum-preserving limiter, characteristic tracing and
full 3D corner coupling after Miller & Colella (2002), and a two-shock-type
Riemann solver that needs no EOS call (§5.2). Reactions are Strang-split;
gravity and external sources are time-centred by a predictor–corrector
(§5.1). The AMR is Berger–Oliger/Berger–Colella with subcycling, refluxing
and a multilevel Poisson synchronization (§6). Merged into
[CASTRO](/software/castro.md),
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md) and
[Poisson solvers for self-gravity on adaptive meshes](/methods/multigrid-self-gravity.md).

# Key claims

1. **Equations** (§2, eqs. 1–6). Conservative Euler with species, passive
   and EOS-auxiliary scalars; gravity enters as the non-conservative
   sources $\rho\mathbf g$ and $\rho\mathbf v\cdot\mathbf g$, not as a flux. No
   MHD, no relativity.
2. **EOS and networks** (§3, eqs. 7–9). The EOS takes $(\rho, e, X_k)$;
   gamma law, Helmholtz and Lattimer–Swesty are shipped; tabular EOSs are
   inverted by Newton–Raphson. Burning leaves the density unchanged.
3. **Gravity** (§4, eq. 10). Constant, monopole (radial profile per level),
   or full Poisson $\nabla^2\Phi = 4\pi G\rho$ with Dirichlet boundary values
   from the coarsest-level monopole, finite differences, geometric
   multigrid V-cycles with red–black Gauss–Seidel; optional point mass.
4. **Time integration** (§5, eqs. 11–12c). Strang splitting: half reaction
   step, hydro step, half reaction step. Fluxes are "purely explicit, based
   on an unsplit Godunov method", "formally second-order in both space and
   time".
5. **Source predictor–corrector** (§5.1, eqs. 15–20). The hydro step uses
   old-time sources; after it the Poisson equation is re-solved with the
   new density and the gravity source is corrected by half the difference.
   Contrasted with FLASH and ENZO, which extrapolate the half-step gravity
   from $t^n$ and $t^{n-1}$.
6. **Post-step fixes** (§5.1). Density floor, mass-fraction renormalization,
   optional sponge, and evolution of $\rho e$ when kinetic energy dominates
   (after Bryan et al. 1995), a dual-energy-like treatment.
7. **Time step** (eqs. 23–24). $\Delta t = \nu\min_i\Delta t_i$ with
   $\Delta t_i = \min_{\mathbf x}h_i/(\vert v_i\vert + c_s)$, $\nu\in(0,1)$: a
   minimum over directions, not a sum.
8. **Reconstruction** (§5.2, eqs. 27–29). PPM on primitive variables,
   default Colella & Sekora (2008) / McCorquodale & Colella (2010) limiter,
   which "avoids reducing the order … at smooth local extrema" and "is
   insensitive to asymmetries caused by roundoff"; options: unsplit PLM, or
   the Miller & Colella (2002) / Colella & Woodward (1984) PPM limiters.
   The flattening coefficient has the opposite convention from FLASH (1 =
   no flattening).
9. **Characteristic tracing** (eqs. 30–32). Integrals of the parabola over
   each wave's domain of dependence give the traced states, with sources
   (including gravity) added; corner coupling "exactly as given in
   Section 4.2.1 in Miller & Colella (2002)", not reproduced.
10. **Riemann solver** (§5.2, eqs. 33–35). Colella, Glaz & Ferguson
    (1997)-type, from Bell, Colella & Trangenstein (1989): linearized
    Rankine–Hugoniot star state with Lagrangian sound speeds, carrying
    $\rho e$ so no EOS call is needed; sampling by shock speed or
    transonic-rarefaction interpolation; small quadratic artificial
    viscosity; species fluxes rescaled to sum to the density flux. No HLLE,
    HLLC, Roe or LLF option is described.
11. **AMR structure** (§6.1). Levels are unions of non-overlapping
    rectangular grids of arbitrary size with an even number of cells per
    direction; $r_{\mathrm{ref}}\in\{2, 4\}$; proper nesting with a buffer of 2
    (ratio 2) or 1 (ratio 4) coarse cells, "since four ghost cells are
    needed for the PPM algorithm"; no parent–child relation (Fig. 1);
    Berger–Rigoutsos clustering; regrid every $k_l$ steps.
12. **Multilevel time stepping** (§6.2.1). Recursive subcycling
    $\Delta t_{l+1} = \Delta t_l/r_{\mathrm{ref}}$; synchronization by volume
    averaging and explicit refluxing (Berger & Colella 1989).
13. **Multilevel gravity** (§6.2.2–§6.2.3, eqs. 36–40). Composite Poisson
    solves at the start and after regrids; level solves with a lagged
    correction (after Miniati & Colella 2007); after subcycling, a two-level
    composite correction solve driven by the refluxed density change and a
    gradient-mismatch flux register; the resulting acceleration change
    gives momentum and energy "sync sources" applied with $\tfrac12\Delta t$
    on both levels.
14. **Software and parallelism** (§7.1). BoxLib, C++ plus Fortran 90; MPI
    with at least one grid per core per level, or MPI+OpenMP with one larger
    grid per socket; knapsack or Morton space-filling-curve distribution,
    switched automatically. No GPU.
15. **I/O** (§7.2–§7.3). About 13 GB/s on single-level uniform grids on
    Franklin (XT4), about 5 GB/s for multilevel runs.
16. **Scaling** (§7.4, Fig. 2). MPI weak scaling on jaguarpf, one $64^3$
    grid per processor, 8 → 64,000 processors, "scales excellently" without
    gravity and with monopole gravity; 24.8 µs per cell per step per core at
    64,000; Poisson gravity scales "relatively good … up to only 13,824
    processors". Hybrid MPI+OpenMP cuts linear-solver time by "at least a
    factor of 3" on a $768^3$ strong-scaling case (no figure). Two-level AMR
    overhead is 5% (8 processors) to 19% (64,000).
17. **Split vs unsplit** (§8.3, Fig. 9). All three dimensionally split
    variants produce spurious secondary Rayleigh–Taylor instabilities,
    attributed to alternating compression and expansion between sweeps;
    unsplit PPM with the new limiter is cleanest. Unsplit costs about 2× CPU
    and memory in 2D; in 3D slightly under 2× CPU and under 10% more memory.
18. **Coordinates** (§1). 1D spherical, 1D/2D cylindrical, 1D/2D/3D
    Cartesian.

**Tests** (§8; shock tubes at $\nu = 0.9$, Sedov at $\nu = 0.5$).
[Sod](/benchmarks/sod-shock-tube.md) on 32 base cells plus 2 levels
(effective 128), "excellent agreement" with the exact solution, no error
norm (§8.1.1, Fig. 3); double rarefaction (internal energy fails at the
centre, §8.1.2); strong shock (§8.1.3);
[Sedov–Taylor](/benchmarks/sedov-taylor-blast-wave.md) in 1D spherical, 2D
$r$–$z$, 3D Cartesian and cylindrical 2D, 3 or 4 levels, against the Kamm &
Timmes (2007) solution (§8.2, Figs. 6–8); single-mode
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md), six schemes
(§8.3); hydrostatic white dwarf, "clear second order convergence in the max
norm" of the spurious velocity, peak below 1% of the central sound speed
(§8.4, Fig. 11); homologous dust collapse (§8.5); reacting bubbles against
FLASH (§8.6); a Type Ia demonstration (§8.7). All hydro tests are
qualitative.

# Notation map

| Almgren et al. (2010) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf U$ | $u$ | |
| $\mathbf u$ | $\mathbf v$ | **collision:** registry $u$ is the conserved state |
| $E$ | $E/\rho$ | **collision:** specific total energy; the paper's $\rho E$ is the registry $E$ |
| $e$, $\rho$, $p$, $T$, $\gamma$ | same | |
| $c$ | $c_s$ | **collision:** registry $c$ is the speed of light |
| $\Gamma_1$ | words | first adiabatic index of a general EOS |
| $\mathbf F$ | $\mathbf f(u)$, $\hat f$ | |
| $\mathbf S$, $\mathbf S_{\mathrm{react}}$, $S_{\mathrm{ext}}$ | $s(u)$ | |
| $\mathbf Q$, $q$ | words | primitive state |
| $q_{L,i+1/2}$, $q_{R,i+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | applied to primitives |
| $\lambda_k$, $r_k$, $l_k$ | $\lambda^{(p)}$ and eigenvectors | $k$ also indexes species |
| $\sigma^{\mathrm{CFL}}$ | $\nu$ | |
| $\sigma_k$ | words | wave-wise Courant number |
| $\chi$ | words | flattening coefficient |
| $h$; $\Delta x_i$ | $h$; $h_l$ | **in-paper collision:** $h$ is also the tanh smoothing length (eqs. 47, 50) |
| $\ell$; $r_\ell$ | $l$; $r_{\mathrm{ref}}$ | |
| $\phi$, $\mathbf g$, $G$ | $\Phi$, $\mathbf g$, $G$ | |
| $L_\ell$, $L^{\mathrm{comp}}_{\ell,m}$ | words | level and composite Laplacians; not $\mathcal L(u)$ |
| $\kappa$ (sponge) | words | **collision:** not opacity |
| $W_{L,R}$ | words | **collision:** Lagrangian sound speeds, not the Lorentz factor |
| $n_{\mathrm{dim}}$ | $d$ | |

# Pages created or updated

* [CASTRO](/software/castro.md).
* [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md), [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md), [Dual-energy formalism](/methods/dual-energy-formalism.md), [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md), [Poisson solvers for self-gravity on adaptive meshes](/methods/multigrid-self-gravity.md), [Conservative self-gravity](/methods/conservative-self-gravity.md).
* [Sod shock tube](/benchmarks/sod-shock-tube.md), [Sedov–Taylor blast wave](/benchmarks/sedov-taylor-blast-wave.md), [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md).
* Also cited on [Enzo (AMR code for cosmological and astrophysical fluid flow)](/software/enzo.md) (its gravity time-centring).
* Also cited on [Hydrostatic white dwarf](/benchmarks/hydrostatic-white-dwarf.md), [General equations of state in Godunov codes](/methods/general-equation-of-state.md).
* Also cited on (batch 3) [Cell-update throughput](/definitions/cell-updates-per-second.md), [Parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md).
* Also cited on (batch 4) [Density and pressure floors](/methods/numerical-floors.md), [FLASH](/software/flash.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2010-ApJ-Almgren-1010880004-637X7152-1221.pdf`.
   * **Version.** arXiv:1005.0114v1 [astro-ph.IM], 1 May 2010, 52 pages
     (AAS LaTeX preprint), not the typeset ApJ article; section, equation
     and page numbers here are the preprint's. A user guide is cited
     (CASTRO User Guide 2009); no repository URL, licence or code version
     is printed.
   * **Identity.** doi:10.1088/0004-637X/715/2/1221, checked on Crossref:
     Astrophys. J. 715(2):1221–1238, online 2010-05-07, print 2010-06-01;
     authors as on page 1.
   * **How it was read.** Text extraction, all sections; preprint pages 9,
     10, 19 and 20 checked visually. Figs. 1, 9, 15 and 16 are read from
     their captions only, Fig. 2 from the text only.
   * **Recorded as printed.** The primitive-variable system (p. 9) and the
     sync-source equations (pp. 19–20) are unnumbered, and the numbering
     jumps from 25 to 27; in eq. 25 the $\rho e$ source is printed as
     $S_{\mathrm{ext},\rho E}$; §8.1.3 calls the pressure jump of eq. 43 "six
     orders of magnitude" while $1000/0.01 = 10^5$; the dust-collapse
     smoothing length "$h = 4\times10^6$" has no unit.
   * **Reference list:** 51 entries in the preprint, against 49 in
     Crossref's record of the published article (not reconciled); no titles
     or DOIs printed.

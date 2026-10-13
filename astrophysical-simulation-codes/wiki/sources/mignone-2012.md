---
type: Source
title: "Mignone et al. (2012) — The PLUTO code for adaptive mesh computations in astrophysical fluid dynamics"
description: "Describes PLUTO-CHOMBO, the block-structured AMR version of PLUTO: a cell-centred unsplit CTU scheme with GLM divergence cleaning (chosen over CT to ease AMR), unsplit parabolic terms, a leaf-cell time step for stiff local sources, and subcycled Berger–Colella AMR from Chombo, tested on MHD and relativistic MHD problems with AMR speed-ups up to about 1978× in 1D and strong scaling to 1024–2048 cores."
resource: "doi:10.1088/0067-0049/198/1/7"
source_kind: paper
authors: [Mignone A., Zanni C., Tzeferacos P., van Straalen B., Colella P., Bodo G.]
year: 2012
venue: "Astrophys. J. Suppl. 198:7"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2012-ApJS-Mignone-1010880067004919817.pdf"
tags: [software, mhd, amr, divergence-cleaning, unsplit, riemann-solver, performance, benchmark]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper couples the single-patch integrators of PLUTO (static-grid
version: Mignone et al. 2007, "Paper I") to the Chombo AMR library. The
single-patch scheme is a cell-centred, dimensionally unsplit, second-order
corner transport upwind (CTU) finite-volume method after Mignone &
Tzeferacos (2010, "MT"). Normal predictors come from characteristic
tracing (PPM, third-order improved WENO, or TVD-limited linear) or from a
characteristic-free MUSCL–Hancock step in primitive variables. The
solenoidal constraint is controlled by GLM cleaning (Dedner et al. 2002),
not CT, to ease the port to AMR. New elements: parabolic terms inside the
CTU corner-coupled states; a time step for stiff point-local sources
evaluated on leaf cells only; and a shock-detecting HLL + MinMod switch.
Merged into [PLUTO](/software/pluto.md),
[GLM divergence cleaning](/methods/glm-divergence-cleaning.md) and
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).

# Key claims

1. **Equations** (§2, eqs. 1–3). Newtonian MHD with viscosity,
   resistivity, thermal conduction, cooling and gravity, total pressure
   $P^* = p + \tfrac12 B^2$ (no $4\pi$); ideal, barotropic or isothermal EOS;
   passive scalars. Relativistic MHD (§2.2) with ideal or Taub–Mathews EOS,
   without dissipative terms. Saturated anisotropic conduction (eqs. 6–7,
   App. A) blends a classical and a saturated flux.
2. **$\nabla\cdot\mathbf B$ control** (§3, eq. 14). PLUTO offers Powell's
   eight-wave method, CT (Paper I) and GLM; **the AMR version uses GLM
   only**: $\partial_t\psi + c_h^2\nabla\cdot\mathbf B = -(c_h^2/c_p^2)\psi$ with
   $\nabla\psi$ added to the induction equation, the damping operator-split.
   Rationale (§1, §7): no elliptic cleaning cost, and none of the care CT
   needs for staggered fields at fine–coarse interfaces. In the
   relativistic rotor, divergence errors leave the domain at the speed of
   light (§6.3). How $c_h$, $c_p$ are set for Newtonian runs is deferred to
   MT.
3. **Integrator** (§3.1, eqs. 15–21). CTU (Colella 1990) as in MT; Riemann
   problems between corner-coupled, time-centred states; six Riemann
   solves per zone per step in 3D. Parabolic terms enter the corner states
   unsplit (eq. 19), with transverse hyperbolic fluxes from first-order
   Godunov (eq. 20) and parabolic fluxes by central differences (eq. 21).
   Cooling, chemistry and GLM damping are operator-split.
4. **Time step** (eq. 23). Courant number with a hyperbolic and a
   parabolic part, stable for $\nu \le 1$ in 2D and $\nu \le 1/2$ in 3D; a
   source-limited step (eq. 24) bounds the relative change of pressure and
   species.
5. **Normal predictors** (§3.2–§3.3). Characteristic tracing from left
   eigenvector projections (eqs. 25–31), with two reference-state choices
   that "may reduce" formal second order in smooth flow; PPM (eqs. 33–37),
   Yamaleev & Carpenter (2009) third-order WENO (eqs. 38–39), or linear TVD
   with MC, harmonic (van Leer), van Albada or MinMod limiters. The
   primitive MUSCL–Hancock predictor (eqs. 43–44) needs no
   eigen-decomposition and is the default for relativistic MHD.
6. **Riemann solvers** (§3.1). Rusanov (LLF), HLL, HLLC and HLLD for MHD and
   relativistic MHD; Roe for hydro and MHD only.
7. **AMR** (§4). Chombo block-structured AMR with Berger–Rigoutsos
   clustering; integer ratios 2 and 4, mixable per level; disjoint,
   properly nested patches (one row of level-$l$ cells between levels
   $l+1$ and $l-1$); subcycling $\Delta t_l = \Delta t_{l-1}/r_{\mathrm{ref}}$
   with optional extra substeps; recursive level advance (Fig. 4); coarse
   ghost data interpolated linearly in time (eq. 46); conservative
   MC-limited linear prolongation in volume coordinates (eq. 45);
   volume-weighted restriction (eq. 47); refluxing with space–time averaged
   fine fluxes (eqs. 48–49). Cartesian and cylindrical $(r,z)$ only.
8. **Refinement criterion** (§4.1, eqs. 50–51). Löhner (1987)
   second-derivative indicator, default filter $\epsilon = 0.01$.
9. **Leaf-cell source time step** (§4.2, eqs. 52–53). Forcing
   $\Delta t_l = \Delta t^0_{\min}/2^l$ makes fine levels take steps $2^l$
   smaller than needed when the source time scale does not depend on the
   mesh; the source-limited step is evaluated on leaf cells only, since
   covered cells are overwritten by restriction; expected speed-up about
   $2^l$.
10. **Parallelism** (§4.3). MPI only; each level is distributed by boxes,
    with no intra-box parallelism; load = grid points per box,
    Kernighan–Lin knapsack balancing. Performance degrades when blocks per
    level approach the number of processors or when the ideal workload per
    processor approaches the maximum box size.
11. **Shock switch** (App. B, eq. B1). Zones with a large normalized
    pressure jump and $\nabla\cdot\mathbf v < 0$ use HLL, their neighbours
    MinMod reconstruction; stated to preserve second order; off unless
    stated.

**Tests** (§5 with characteristic tracing, $\gamma = 5/3$; §6 with the
MUSCL–Hancock predictor). Torrilhon shock tube up to 10 levels (Table 2
gains 1 → 1977.8, the last from an inferred static time); 3D rotated
Ryu–Jones shock tube (gain about 23); [field-loop advection](/benchmarks/field-loop-advection.md)
with 2–4 levels, $\langle B^2\rangle$ retained from about 94% to about 98%
(§5.2, Fig. 11); resistive reconnection with Sweet–Parker scaling and
strong scaling (§5.3); current sheet (§5.4); 3D magnetic
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md), efficiency
> 0.8 to 512 cores (§5.5, Figs. 17–18); shock–cloud with anisotropic
conduction (§5.6); radiative jet shocks (§5.7). Relativistic MHD: shock
tube (speed-ups 3.4–50.4, Table 3); inclined Alfvén test (Table 4);
rotor; cylindrical and 3D spherical
[magnetized blast waves](/benchmarks/mhd-blast-wave.md) (§6.4–§6.5;
relativistic set-ups, AMR ~4.5× faster in 2D, efficiency > 0.75 to 2048
processors in 3D); Kelvin–Helmholtz (AMR ≈40× faster); 3D shock–cloud;
3D jet. No convergence-order study is reported.

Batch 9: the "3D rotated Ryu–Jones shock tube" (§5.1.2) is not in [Ryu & Jones (1995)](/sources/ryu-1995.md), which is strictly 1D; PLUTO rotates the Ryu–Jones 2a states (eq. 55), with the rotation matrix of Mignone et al. (2010); the earliest 3D inclined 2a among the ingested sources is [Gardiner & Stone (2008)](/sources/gardiner-2008.md), §5.4, which this paper lists among later uses (see [PLUTO](/software/pluto.md), batch 9).

# Notation map

| Mignone et al. (2012) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $\mathbf v$, $p$ | $\rho$, $\mathbf v$, $p$ | |
| $\mathcal E$ | $E$ | total energy density; **collision:** registry $\boldsymbol{\mathcal E}$ is the EMF |
| $p_t$ | $P^*$ | |
| $\mathbf B$ | $\mathbf B$ | Heaviside–Lorentz-type units |
| $\Gamma$ | $\gamma$ | eq. 62 writes $\gamma$ for the adiabatic index (in-paper inconsistency) |
| $\gamma$ | $W$ | **collision:** Lorentz factor |
| $\rho\gamma$, $\mathbf m$, $\mathcal E$ (RMHD) | $D$, $S_i$, $\tau$ | the relativistic $\mathcal E$ already subtracts $\rho\gamma$ (eq. 9) |
| $\mathbf U$, $\bar{\mathbf U}$ | $u$ | |
| $\mathbf V$ | words | primitive vector |
| $\mathsf F$, $\mathbf F_{d,\pm}$ | $\mathbf f(u)$, $\hat f_{i+1/2}$ | |
| $\mathbf S_p$ | $s(u)$ | point-local sources |
| $\mathcal L_{H,d}$, $\mathcal L_{P,d}$ | words | directional increments, not the full $\mathcal L(u)$ |
| $\psi$, $c_h$, $c_p$ | $\psi$, $c_h$, $c_p$ | |
| $C_a$ | $\nu$ | Courant number |
| $\nu$ | words | **collision:** viscosity (eq. 4) and per-wave Courant number (eq. 26) |
| $\eta$, $\mathbf J$ | words, $\mathbf J$ | resistivity |
| $\kappa_\parallel$, $\kappa_\perp$ | words | **collision:** conductivities, not opacity |
| $c_s$, $c_{\mathrm{iso}}$ | words | isothermal sound speed |
| $\mathbf g$ | $\mathbf g$ | |
| $\ell$; $r^\ell$ | $l$; $r_{\mathrm{ref}}$ | the ratio may change per level |
| $\Delta x_d$, $\Delta x^\ell$; $\Delta t^\ell$ | $h$, $h_l$; $\Delta t_l$ | |
| max box size | words | an upper bound, not the fixed $N_{\mathrm b}$ |
| $\chi$, $\chi_r$, $\sigma$, $\epsilon$ | words | refinement indicator, threshold, tagged variable, filter |

# Pages created or updated

* [PLUTO](/software/pluto.md).
* [Constrained transport](/methods/constrained-transport.md) (why the AMR version avoids CT), [GLM divergence cleaning](/methods/glm-divergence-cleaning.md), [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md), [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md), [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).
* [Field-loop advection](/benchmarks/field-loop-advection.md), [MHD blast wave](/benchmarks/mhd-blast-wave.md) (relativistic variants), [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md).
* Also cited on (batch 3) [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md), [Relativistic magnetic rotor](/benchmarks/relativistic-magnetic-rotor.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2012-ApJS-Mignone-1010880067004919817.pdf`.
   * **Version.** The publisher's version of record (31 pages, © 2012
     AAS), not a preprint. PLUTO and Chombo are distributed at
     http://plutocode.ph.unito.it; Chombo from
     https://seesar.lbl.gov/anag/chombo/ (§7). Chombo is "written in a
     combination of C++ and Fortran77 with MPI" (§4). PLUTO's version,
     language and licence are not printed.
   * **Identity.** doi:10.1088/0067-0049/198/1/7, printed on page 1 and
     checked on Crossref: Astrophys. J. Suppl. 198(1), article 7; online
     2011-12-22, issue 2012-01; 81 references. The year is the issue year,
     2012.
   * **How it was read.** Text extraction, all 31 pages; pages 4, 5, 6, 8
     and 9 checked visually for equations. Eqs. 63–64, 67–70 and 75–78 were
     read from the text layer only.
   * **Recorded as printed.** §5.1.2 stops at $t = 0.2\cos\alpha\cos\gamma$
     in the text and $t = 0.02\cos\alpha\cos\gamma$ in the Fig. 8 caption;
     eq. 62 uses $\gamma$ for the adiabatic index; §5.6 prints the domain as
     "$y\in[-1.4\times6.6]$"; eq. 39 divides undivided differences by
     $\Delta x^2$; footnote 5 corrects mislabelled plots in MT and Mignone et
     al. (2010).
   * **Reference list:** 81 entries, titles not printed (AAS style).
     Same-author-year suffixes in printed order: `balsara-2001` /
     `-b`; `mignone-2007` (Paper I) / `-b` (with McKinney);
     `mignone-2010` (Rossi et al.) / `-b` (MT, J. Comput. Phys. 229:2117) /
     `-c` (J. Comput. Phys. 229:5896). This paper is cited by
     [Stone et al. (2020)](/sources/stone-2020.md) under its printed-order
     key `mignone-2012-b`, which the merge resolves to this slug.

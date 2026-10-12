---
type: Source
title: "Bryan et al. (2014) — ENZO: An adaptive mesh refinement code for astrophysics"
description: "Method paper of Enzo 2.3, an open-source comoving-coordinate block-structured AMR code with four fluid solvers (split PPM, unsplit MUSCL with GLM cleaning, constrained-transport MHD, ZEUS), the dual-energy formalism, subcycled Berger–Colella AMR with refluxing, FFT plus grid-by-grid multigrid gravity, N-body, chemistry and radiation, 14 verification tests, MPI scaling to 13,824 and 16,384 cores, and a CUDA port about 5× faster per node."
resource: "doi:10.1088/0067-0049/211/2/19"
source_kind: paper
authors: [Bryan G.L., Norman M.L., O'Shea B.W., Abel T., Wise J.H., Turk M.J., Reynolds D.R., Collins D.C., Wang P., Skillman S.W., Smith B., Harkness R.P., Bordner J., Kim J.-h., Kuhlen M., Xu H., Goldbaum N., Hummels C., Kritsuk A.G., Tasker E., Skory S., Simpson C.M., Hahn O., Oishi J.S., So G.C., Zhao F., Cen R., Li Y.]
year: 2014
venue: "Astrophys. J. Suppl. 211:19"
local_file: "~/papers/mosaic/astrophysical-simulation-codes/2014-ApJS-Bryan-1010880067-004921121.pdf"
tags: [software, hydro, mhd, amr, cosmology, dual-energy, constrained-transport, divergence-cleaning, riemann-solver, self-gravity, multigrid, radiation, gpu, performance, verification, benchmark]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The first systematic method paper of Enzo 2.3, an open-source Cartesian
block-structured AMR code for astrophysical flow in 1–3 dimensions,
written in comoving coordinates so that cosmological expansion is included
(§2.1). Four interchangeable fluid solvers — direct-Eulerian PPM (hydro),
MUSCL with Dedner GLM cleaning (hydro and MHD), Godunov MHD with
constrained transport (Collins et al. 2010) and ZEUS (hydro) — run on a
level-by-level, subcycled AMR hierarchy with flux correction, conservative
projection and Berger–Rigoutsos clustering (§3–§4). Coupled physics:
FFT and multigrid self-gravity, particle-mesh N-body, primordial chemistry,
cooling, ray-tracing and flux-limited-diffusion radiation, conduction, star
formation and feedback (§5–§8). Fourteen verification tests, scaling, a
cost model, a CUDA port and the development process close the paper
(§11–§13). Merged into [Enzo](/software/enzo.md),
[dual-energy formalism](/methods/dual-energy-formalism.md) and
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).

# Key claims

1. **Equations** (§2.1, eqs. 1–8). Comoving ideal MHD with gravity in
   units with permeability 1, scale factor $a$, $E$ and $e$ as energy
   densities, total pressure $P^* = p + B^2/(2a)$, and
   $\nabla^2\Phi = \frac{4\pi G}{a}(\rho_{\mathrm{total}} - \rho_0)$. The
   non-cosmological limit is $a = 1$. The Dedner solver uses a different
   comoving field scaling, $a^{3/2}$ instead of $a^2$, with an extra source
   (§4.2). No relativistic solver is described.
2. **Four solvers** (§2.2.2, §4). PPM (hydro only); MUSCL-type Godunov with
   or without $\mathbf B$ and Dedner cleaning; staggered CT MHD; ZEUS
   second-order finite differences (hydro only). Expansion terms are
   operator-split and integrated implicitly, time-centred (§4.1).
3. **PPM** (§4.1). Direct-Eulerian Colella–Woodward, **dimensionally
   split**; parabolic reconstruction of $p$, $\rho$, $\mathbf v$ (eqs.
   40–41) with the CW84 monotonicity, characteristic domain-of-dependence
   averaging, optional steepening, flattening and diffusion. Interface
   states "third-order accurate in space and second-order accurate in
   time"; the multi-D scheme "formally second-order accurate in space and
   time" (§2.2.2). Gravity enters time-centred (eqs. 38–39).
4. **Dual-energy formalism** (§4.1.1, eqs. 42–45). An internal-energy
   equation, differenced non-conservatively, is carried with $E$; the
   pressure uses $E - \tfrac12 v^2$ when its fraction of $E$ exceeds
   $\eta_1 = 10^{-3}$ and $e$ otherwise; $e$ is reset from $E$ when the
   thermal fraction relative to the neighbourhood maximum of $E$ exceeds
   $\eta_2 = 0.1$. Motivated by kinetic/thermal ratios up to $10^8$ in
   cosmological flows; related to the Ryu et al. (1993) entropy scheme.
5. **Riemann solvers** (§4.1.2). Two-shock (PPM only); HLL and HLLC (PPM,
   MUSCL, MHD-CT); HLLD (MUSCL and MHD-CT). No Roe or LLF. In PPM and MUSCL
   a negative density at an interface triggers an HLL recomputation of that
   cell's fluxes (Lemaster & Stone 2009).
6. **MUSCL–Dedner** (§4.2, eqs. 48–51). Piecewise linear reconstruction in
   primitive or conservative variables; GLM scalar $\psi$ with constant
   $c_h$; **dimensionally unsplit**, second-order Runge–Kutta (Shu & Osher
   1988). No damping coefficient is printed.
7. **MHD-CT** (§4.3). Godunov base scheme of Li et al. (2008), MUSCL–Hancock
   or PLM; EMFs by the first-order Balsara & Spicer (1999) method or the
   second-order Gardiner & Stone (2005) methods, without saying which
   Gardiner–Stone variant. $\nabla\cdot\mathbf B$ is kept to machine
   precision, but monopoles from other sources persist. On AMR:
   divergence-free prolongation of all three face components together
   (Balsara 2001), and the electric field, not $\mathbf B$, is projected
   from fine to coarse.
8. **ZEUS** (§4.4). Staggered velocities, operator-split, von
   Neumann–Richtmyer quadratic viscosity ($Q_{\mathrm{AV}} \approx 2$);
   "formally second-order accurate in space but first-order accurate in
   time"; solves internal energy, so total energy is not conserved.
9. **AMR** (§3). Berger–Colella patches of variable size; $r_{\mathrm{ref}}$
   typically 2 or 4, "generally $r = 2$"; subgrids align with coarse cells
   and lie wholly in one parent; no other nesting rule is stated. Ghost
   zones: 3 for PPM and ZEUS, 6 for gravity. Subcycling by recursive
   `EvolveLevel` ("W-cycle"), with finer steps not restricted to
   $\Delta t/2^n$ (Fig. 2). Conservative, monotone interpolators limited
   along cell diagonals (App.). Projection averages with weight $r^{-d}$,
   $r^{-(d-1)}$ for faces and $r^{-1}$ for edges (eq. 26); refluxing over
   the $r^{d-1}$ fine faces (eq. 27). Berger–Rigoutsos clustering with
   efficiency "typically over 30%" (§3.5). Thirteen refinement criteria
   (§3.6), among them slope, baryon mass, shocks, Jeans length (4 cells by
   default), shear and the Löhner (1987) estimator.
10. **Gravity** (§5.1). Root grid by FFT (periodic, or isolated by the
    James 1977 method); subgrids by a 7-point stencil solved by multigrid
    **grid by grid** with Dirichlet values interpolated from the parent and
    optional sibling iterations. Not a coherent level-wide solve; a
    HYPRE-based AMR solver is announced as future work.
11. **Coupling and time step** (§2.2.12, §9). Chemistry and conduction are
    subcycled, the rest share one level step. Hydro step
    $\nu\, a h/(c_s + \vert v_x\vert)$, $\nu \sim 0.3$–$0.5$, combined over
    directions by a harmonic sum (eq. 95), "maximum
    $\kappa_{\mathrm{hydro}} = 0.8$"; MHD with $c_f$, $\nu \sim 0.5$.
12. **Parallelism** (§12.1). MPI only, the grid as unit of distribution,
    greedy or Hilbert-curve load balancing, full hierarchy metadata
    replicated on every rank. Hybrid MPI+OpenMP is "under development".
13. **Scaling** (§12.2, Figs. 19–20). Unigrid weak scaling, $128^3$ cells per
    task: 20% drop in cell updates per task from 8 to 4,096 tasks, 40% to
    13,824. AMR strong scaling ($512^3$ root, 6 levels, 302,311 grids):
    refined levels scale to 2,048 cores; the root level degrades beyond
    1,024.
14. **Cost model** (§12.2.4, eqs. 113–115). For $r_{\mathrm{ref}} = 2$ the work
    of level $l$ grows with $l$ unless the fine/coarse refined-volume ratio
    is below 1/16.
15. **GPU** (§12.3, Fig. 22). PPM and Dedner MHD ported to CUDA, with host
    and device copies around each solver call; on Cray XK6 nodes with one
    K20, about 5× per node against 16 CPU cores, about 80× one core.
16. **Process** (§11.1.1, §13). Answer-testing suites against "gold
    standard" results; mandatory push suite and peer-reviewed pull
    requests.

**Tests** (§11.2). [Sod](/benchmarks/sod-shock-tube.md), 100 root cells,
unigrid and 2 AMR levels: E1 errors ($\sum_i h_i\vert\cdot\vert$ against the exact solution) PPM $2.8\times10^{-3}$, ZEUS
$9.3\times10^{-3}$, MUSCL $7.9\times10^{-3}$ unigrid; $9.6\times10^{-4}$,
$3.8\times10^{-3}$, $2.4\times10^{-3}$ with AMR (Fig. 4). Wave pool and shock
pool through static refined regions (ZEUS puts the shock in the wrong
place). [Double Mach reflection](/benchmarks/double-mach-reflection.md),
960×240, PPM (Fig. 7). 2D [Sedov blast](/benchmarks/sedov-taylor-blast-wave.md)
with 4 AMR levels: PPM matches "extremely well", ZEUS lags (Figs. 8–9).
Point-source gravity, orbit, self-similar infall, Zel'dovich pancake.
[Orszag–Tang](/benchmarks/orszag-tang-vortex.md), CT against Dedner,
"approximately equal effective resolution", resolution not printed
(Fig. 14). One-zone collapse, photo-evaporation, cosmological I-front,
anisotropic conduction. No convergence-order study, field-loop, Brio–Wu
or MHD blast test.

# Notation map

| Bryan et al. (2014) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $\mathbf v$, $p$ | $\rho$, $\mathbf v$, $p$ | comoving density and pressure, peculiar velocity |
| $E$ | $E$ | energy density in eqs. 3, 5; specific in §4.2 and, implicitly, eqs. 36, 44–45 |
| $e$ | $\rho e$ | **collision:** internal energy per volume in eqs. 5, 7, 42; specific only in §4.2 |
| $p^*$ | $P^*$ | with $B^2/(2a)$ |
| $\mathbf B$; $\mathbf B_f$, $\mathbf B_c$ | $\mathbf B$; words | permeability 1; comoving $a^2$ (CT) vs $a^{3/2}$ (Dedner) |
| $a$ | $a$ | scale factor |
| $\phi$, $\mathbf g$ | $\Phi$, $\mathbf g$ | |
| $c_s$, $c$ | $c_s$ | §4.1 writes $c$; **collision** with the speed of light |
| $v_f$, $v_A$ | $c_f$, $c_A$ | |
| $\Delta x_l$; $\Delta t_l$ | $h_l$; $\Delta t_l$ | |
| $d$; $r$; $l$ | $d$; $r_{\mathrm{ref}}$; $l$ | |
| $q$, $F$ (eqs. 26–27) | $u$, $\hat f$ | |
| $\kappa_{\mathrm{hydro}}$, $\kappa_{\mathrm{MHD}}$ | $\nu$ | **collision:** registry $\kappa$ is opacity |
| $\kappa_{\mathrm{cond}}$ | words | conductivity |
| $E_r$ | $E_{\mathrm r}$ | |
| $D$ (FLD) | words | **collision** with the Valencia $D$ |
| $\psi$, $c_h$ | $\psi$, $c_h$ | |
| $\eta_1$, $\eta_2$ | $\eta_1$, $\eta_2$ | |
| $\Lambda$, $\Gamma$ | words | cooling and heating rates |
| $N_J$ | words | cells per Jeans length |

# Pages created or updated

* [Enzo](/software/enzo.md).
* [Constrained transport](/methods/constrained-transport.md), [GLM divergence cleaning](/methods/glm-divergence-cleaning.md), [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md), [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md), [Dual-energy formalism](/methods/dual-energy-formalism.md), [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md), [Poisson solvers for self-gravity on adaptive meshes](/methods/multigrid-self-gravity.md).
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), [Sod shock tube](/benchmarks/sod-shock-tube.md), [Sedov–Taylor blast wave](/benchmarks/sedov-taylor-blast-wave.md), [Double Mach reflection](/benchmarks/double-mach-reflection.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2014-ApJS-Bryan-1010880067-004921121.pdf`.
   * **Version.** arXiv:1307.2265v1 [astro-ph.IM], 8 July 2013 (the only
     arXiv version), headed "Draft version July 22, 2013", 60 pages; not the
     typeset ApJS article. It describes Enzo 2.3 (enzo-dev changeset
     `5d8c412`, §11.1.1); http://enzo-project.org, development on
     Bitbucket in Mercurial (§13). The licence is called only
     "open-source"; the language is not stated.
   * **Identity.** doi:10.1088/0067-0049/211/2/19, checked on Crossref:
     Astrophys. J. Suppl. 211(2), article 19, issued 2014-03-20. Page 1
     prints "The Enzo Collaboration:" as a label before 28 named authors,
     the first being Greg L. Bryan; Crossref lists the same 28 plus "The
     Enzo Collaboration" as a 29th, organizational author. The collection
     keyed the paper "the-2013", taking the label for a surname and the
     preprint year; the slug is the first named author and the issue year.
   * **How it was read.** Text extraction, all sections; eqs. 1–8 checked
     on the rendered page 4. Figs. 19 and
     21 are raster images, read from the text only.
   * **Recorded as printed.** The Jeans-cell number is $N_J$ in eq. 29, "$J_J$"
     in the text and "$J$" in Table 1; the wave pool prints
     "$\lambda = k/2\pi$"; $\alpha_B$ is given in "s⁻¹"; §12.2.4 writes the
     level ratio both as $f_l/f_{l+1}$ and $f_{l+1}/f_l$; eq. 95 puts the
     Courant factor over a harmonic sum whose terms already contain it; the
     1D shock pool refines "from $z = 0.25$"; eqs. 44–45 use $E$ and $e$ as
     specific quantities without saying so.
   * **Reference list:** 202 entries in the preprint, against 205 in
     Crossref's record of the published article; no titles or DOIs printed.
     Printed slips kept in the bibliography notes: Woodward & Colella
     "1984b, J. Comp. Phys., 54, 174" carries the vol:page of Colella &
     Woodward's PPM paper (the blast-wave paper is the printed 1984a,
     54:115); `gnedin-1995` / `-b` and `wang-2009` / `-b` are a/b pairs with
     identical venues; Miyoshi & Kusano is printed as an AGU abstract;
     `wang-2009-c` has no volume or page.

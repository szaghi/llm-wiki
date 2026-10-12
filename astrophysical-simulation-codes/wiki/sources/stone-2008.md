---
type: Source
title: "Stone et al. (2008) — Athena: A new code for astrophysical MHD"
description: "Method paper of Athena, a second-order unsplit Godunov code for ideal MHD with face-centred constrained transport whose edge EMFs come from the face fluxes by upwinded gradients, CTU+CT integrators in 2D and 3D, HLLE/HLLC/HLLD/Roe solvers, MPI weak scaling above 85% to 20,000 processors, and a 1D–3D test suite showing second-order convergence for all wave families."
resource: "doi:10.1086/588755"
source_kind: paper
authors: [Stone J.M., Gardiner T.A., Teuben P., Hawley J.F., Simon J.B.]
year: 2008
venue: "Astrophys. J. Suppl. 178:137–177"
local_file: "~/papers/mosaic/astrophysical-simulation-codes/2008-ApJS-Stone-101086588755.pdf"
tags: [software, mhd, hydro, constrained-transport, unsplit, riemann-solver, verification, benchmark, performance]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

Athena solves compressible ideal MHD and hydrodynamics, with adiabatic
or isothermal/barotropic equations of state, by a second-order,
directionally unsplit Godunov method. Mass, momentum and energy are
cell-centred volume averages; the magnetic field is a set of
face-centred area averages evolved by constrained transport (CT). The
paper is the implementation reference for the mathematics of Gardiner &
Stone (2005, 2D; 2008, 3D). It claims three novelties (§1): edge EMFs for
CT built from the face Godunov fluxes with upwinded gradients and a
cell-centred reference EMF (§5.3); characteristic-tracing PLM/PPM
reconstruction extended to multidimensional MHD, with $\nabla\cdot\mathbf B$
source terms in the interface states (§4.2, §5.2, §6.2); and two unsplit
integrators extended to MHD, CTU+CT (described here) and VL+CT (deferred to
Stone & Gardiner 2008). The test suite (§8) covers 1D, 2D and 3D hydro and
MHD. Merged into [Athena](/software/athena.md),
[constrained transport](/methods/constrained-transport.md),
[unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md) and
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md).

# Key claims

1. **Equations** (§2, eqs. 1–5). Ideal MHD in conservative form with
   magnetic permeability 1, total pressure $P^* = p + \tfrac12 B^2$ and
   $E = \frac{p}{\gamma-1} + \tfrac12\rho v^2 + \tfrac12 B^2$. A barotropic
   EOS drops the energy equation. Curvilinear coordinates are not
   implemented; they are listed as "underway" (§9).
2. **Discretization** (§3). Uniform Cartesian grid; the face-centred,
   area-averaged field is updated by the CT difference equations (16–18)
   with edge-centred, time- and line-averaged EMFs
   $\boldsymbol{\mathcal E} = -\mathbf v\times\mathbf B$ (eqs. 22–24). CT keeps
   the cell-averaged divergence (eq. 25) exactly zero; the cell-centred
   field is the mean of the two face values (eqs. 26–28). Stated cost:
   face-centred CT "complicates the implementation of the algorithm, and
   the interface to AMR drivers" (§3.2).
3. **Reconstruction** (§4.2). Primitive variables, with limiting in
   characteristic variables and characteristic tracing over half a step
   for CTU+CT. PLM uses the monotonized-central limiter in characteristic
   variables (eq. 38) and, for HLL-family solvers only, an extra correction
   for waves moving away from the interface (eqs. 44–45). PPM follows
   Colella & Woodward (1984) (eqs. 46–60); the Colella & Sekora (2007)
   extremum-preserving limiters are optional. The scheme is formally
   second order; "third-order" PPM lowers the error amplitude, and
   "improving the convergence rate of the reconstruction algorithm is not
   always the best way to improve the overall accuracy" (§4.2.3).
4. **Riemann solvers** (§4.3). HLLE (eqs. 61–63, positive-definite in 1D),
   HLLC ("highly recommended" for adiabatic hydro), HLLD ("the best choice
   for many MHD applications", as accurate as Roe and "much faster"), Roe
   (eqs. 64–68), and an exact solver for isothermal hydro only. When Roe
   gives a negative density or pressure in an intermediate state, that one
   interface is recomputed with HLLE (§4.3.2).
5. **2D CTU+CT** (§5.1, steps 1–11). Two Riemann solves per direction,
   transverse-flux corrections of the interface states with
   $\nabla\cdot\mathbf B$ source terms (eqs. 71–73), a half-step CT update of
   the in-plane face field (eqs. 74–75), time step by eq. 78 with
   $\nu \le 1$. It reduces exactly to the 1D algorithm for grid-aligned
   flow.
6. **CT edge EMF** (§5.3, eqs. 79–81). The corner EMF is the average of the
   four neighbouring face EMFs plus gradient corrections, each derivative
   upwinded by the sign of the contact (mass-flux) velocity and built from
   a cell-centre reference EMF. "Simple arithmetic averaging does not work
   for the unsplit integrators adopted here" (§5).
7. **3D CTU+CT** (§6). Full 3D CTU needs 12 Riemann solves per cell and is
   stable to $\nu \le 1$; Athena's primary integrator is the six-solve
   variant, stable for $\nu \le 1/2$, found by Gardiner & Stone (2008) "as
   accurate as the twelve-solve method" and "dramatically simpler to
   implement". The $\nabla\cdot\mathbf B$ source terms are minmod-limited
   (eqs. 88–89). It reduces exactly to 2D or 1D under symmetry.
8. **H-correction** (App. C). The Sanders et al. (1998) carbuncle fix:
   each Roe eigenvalue modulus is bounded below by the maximum of a
   half wave-speed difference over a five-point (2D) or nine-point (3D)
   stencil (eqs. C1–C2), applied only to the final multidimensional
   fluxes; HLL-type solvers modify their wave-speed bounds instead.
9. **Mesh** (§1, §8.4, §9). Uniform grid with MPI domain decomposition;
   one AMR demonstration (magnetic Rayleigh–Taylor, five levels, base
   8×16, effective 256×512); SMR/AMR with CTU+CT is deferred to "a future
   communication". No refluxing, subcycling or load-balancing details.
10. **Implementation** (§7). C and Fortran 95 versions; modular solvers,
    reconstructions and integrators behind common interfaces; array of
    per-cell structs; 1D pencils for vectorization. About 10× the flops
    per cell of ZEUS but about 4× slower with HLLD. Table 1 (C, 3D,
    $128^3$, 2.2 GHz Opteron), in $10^3$ cell updates per CPU second:
    isothermal hydro 328 (Roe) / 340 (HLLC); adiabatic hydro 224 / 242;
    isothermal MHD 108 (Roe) / 124 (HLLD); adiabatic MHD 85.9 / 97.6;
    ZEUS adiabatic MHD 404.
11. **Parallelism** (§7, Fig. 6). MPI domain decomposition; MHD with
    third-order reconstruction needs 4 ghost cells (more with the
    H-correction); boundary exchange is sequential in $x$, $y$, $z$, so no
    diagonal messages are needed. Weak scaling on Red Storm (Cray XT-3),
    $32^3$ or $64^3$ cells per processor: efficiency "above 85%" to 20,000
    processors. No threading or GPU.
12. **Gravity** (§8.3, §9). Fixed-potential source terms conserve total
    energy exactly; self-gravity conserves total momentum exactly; both are
    described in Gardiner & Stone "in preparation".
13. **CTU+CT vs VL+CT** (§1): CTU+CT is "generally less diffusive and more
    accurate"; VL+CT needs no characteristic tracing (§4.2). On higher
    order (§3.1) the paper cites Greenough & Rider (2003): second-order
    Godunov gave more accuracy per cost than fifth-order WENO on 1D hydro.

**Tests** (§8; CTU+CT throughout). 1D hydro: [linear waves](/benchmarks/linear-wave-convergence.md)
(second order for HLLC and Roe, HLLE slightly worse, Fig. 7);
[Sod](/benchmarks/sod-shock-tube.md) (100 cells, Fig. 8); Woodward–Colella
interacting blast waves; Shu–Osher; Einfeldt 1-2-0-3. 1D MHD: linear waves
(second order, Fig. 12); [Brio–Wu](/benchmarks/brio-wu-shock-tube.md)
(Fig. 13); Torrilhon; Ryu–Jones 2a and 4d. 2D hydro:
[double Mach reflection](/benchmarks/double-mach-reflection.md) (260×80 and
520×160, Fig. 16); Liska–Wendroff implosion (the diagonal jet forms with the
unsplit integrator only, Fig. 17); Liska–Wendroff single-mode
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) (Fig. 18). 2D
MHD: circularly polarized Alfvén wave (second order, Figs. 19–20);
[field-loop advection](/benchmarks/field-loop-advection.md) (256×128,
Fig. 21); [Orszag–Tang](/benchmarks/orszag-tang-vortex.md) ($192^2$,
Figs. 22–24); MHD rotor; magnetic Rayleigh–Taylor with AMR (Fig. 27);
[MHD blast wave](/benchmarks/mhd-blast-wave.md) (200×300, Figs. 28–30). 3D:
Noh (Fig. 31); oblique linear MHD waves (second order in all families,
Fig. 32); oblique Alfvén wave; two 3D field loops (Fig. 34); oblique RJ2a;
3D MHD blast (Fig. 36).

# Notation map

| Stone et al. (2008) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $P$ | $p$ | gas pressure |
| $P^* = P + B^2/2$, $\mathsf P^*$ | $P^*$ | total pressure; the tensor is $P^*$ times the identity |
| $\mathbf M$ | $\rho\mathbf v$ | momentum |
| $\boldsymbol U$ (3D, 8 components), $\boldsymbol q$ (1D, 7 components) | $u$ | |
| $\boldsymbol W$, $\boldsymbol w$ | none (words) | primitive vector; the registry has no symbol |
| $\boldsymbol F, \boldsymbol G, \boldsymbol H$ | components of $\mathbf f(u)$ | |
| $\boldsymbol F^{n+1/2}_{i-1/2}$ | $\hat f_{i-1/2}$ | **collision:** the superscript $n+1/2$ is a time average over $[t^n, t^{n+1}]$, not a midpoint value |
| $\boldsymbol q_{L,i-1/2}$, $\boldsymbol q_{R,i-1/2}$ | $u^-_{i-1/2}$, $u^+_{i-1/2}$ | |
| $\mathcal E$, $\mathcal E^r$ | $\boldsymbol{\mathcal E}$, words | EMF; $\mathcal E^r$ is the cell-centre reference EMF |
| $\mathbf J$ | $\mathbf J$ | |
| $\delta t$; $\delta x$, $\delta y$, $\delta z$ | $\Delta t$; $h$ | the paper allows anisotropic cells |
| $C_0$ | $\nu$ | Courant number |
| $C_f$, $C_A$ | $c_f$, $c_A$ | |
| $C_s$ | none (words) | **collision:** the paper's $C_s$ is the slow magnetosonic speed, not $c_s$ |
| $a$ (App. A), $c_s$ (§8.1) | $c_s$ | adiabatic sound speed |
| $C$ | none (words) | isothermal sound speed |
| $\lambda^\alpha$; $\lambda^M$, $\lambda^0$ | $\lambda^{(p)}$; $\max_p\lambda^{(p)}$, $\min_p\lambda^{(p)}$ | |
| $b^+$, $b^-$ | none (words) | HLL wave-speed bounds |
| $b = B/\sqrt{4\pi}$ (App. A) | $\mathbf B$ | **unit inconsistency in the paper:** §2 uses permeability 1 ($B^2/2$), App. A3 and the Orszag–Tang set-up use $\sqrt{4\pi}$ factors |
| $\eta$, $\bar\eta$ | none | local to the H-correction |

# Pages created or updated

* [Athena](/software/athena.md).
* [Constrained transport](/methods/constrained-transport.md), [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md), [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md), [Conservative self-gravity](/methods/conservative-self-gravity.md).
* [Linear wave convergence](/benchmarks/linear-wave-convergence.md), [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), [Field-loop advection](/benchmarks/field-loop-advection.md), [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md), [Sod shock tube](/benchmarks/sod-shock-tube.md), [MHD blast wave](/benchmarks/mhd-blast-wave.md), [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md), [Double Mach reflection](/benchmarks/double-mach-reflection.md).
* Also cited on (batch 3) [Circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md), [Liska–Wendroff implosion](/benchmarks/liska-wendroff-implosion.md), [Relativistic magnetic rotor](/benchmarks/relativistic-magnetic-rotor.md), [Shu–Osher shock tube](/benchmarks/shu-osher-shock-tube.md), [Cell-update throughput](/definitions/cell-updates-per-second.md), [Parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md), [Cholla (GPU-native astrophysical MHD code)](/software/cholla.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2008-ApJS-Stone-101086588755.pdf`.
   * **Version.** The published journal version (ApJS typeset pages
     137–177, 41 PDF pages), not a preprint. Two implementations are
     described, C and Fortran 95; the code is "freely available for
     download on the web", but no URL, version number or licence is
     printed.
   * **Identity.** doi:10.1086/588755, checked on Crossref: "Athena: A New
     Code for Astrophysical MHD", Astrophys. J. Suppl. 178(1):137–177,
     published in print 2008-09; authors as on page 1.
   * **How it was read.** Text extraction, all sections; Greek letters,
     minus signs and absolute-value bars are lost in the text layer, so
     the key equations were checked on rendered pages (PDF pp. 2, 6, 7, 9,
     13, 15, 17, 22, 23, 26, 28). Not checked visually: the H-correction
     $\eta$ (eq. C2), whose absolute value is assumed from Sanders et al.;
     the eigenvector matrices of Apps. A–B are not reproduced.
   * **Recorded as printed.** App. C cites the HLL wave speeds as
     "equations (53) and (54)" (they are eqs. 62–63); §8.4 cites the LW03
     Rayleigh–Taylor test as Fig. 16 (it is Fig. 18); Brio–Wu runs on 800
     zones in the text but 400 in the Fig. 13 caption; the 3D oblique RJ2a
     stops at $t_f = 1$ in the text but $t = 0.2$ in the Fig. 35 caption;
     §2 uses permeability-1 units while App. A3 and Orszag–Tang use
     $\sqrt{4\pi}$ factors; Table 2 prints the Torrilhon right state as
     $\cos(3)$, $\sin(3)$ literally; eq. 79 prints the face EMFs averaged into the corner
     $(i-\tfrac12, j-\tfrac12)$ with indices $j+1$ and $i+1$, where the faces
     touching that corner are $j-1$ and $i-1$ (checked on the page image,
     p. 149); the formula is not reproduced in this bundle.
   * **Reference list:** 81 entries, titles not printed (ApJS style)
     except two books. Stone & Gardiner (2008, New Astron., in press,
     "SG08") would take this source's own key and is keyed
     `stone-2008-b`. Printed slips kept in the bibliography notes, not
     verified: Woodward & Colella (1984) printed with page 174, the page of
     Colella & Woodward's PPM paper (the blast-wave paper is 54:115 as
     printed by the other citing sources); Miyoshi & Kusano printed
     "J. Comput. Phys., 315, 344"; Liska & Wendroff "25, 3"; Stone &
     Gardiner 2007a "Phys. Fluids, 19, 4104"; Wheatley et al. "Phys. Rev.
     Lett., 95, 125".

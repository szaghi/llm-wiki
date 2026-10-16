---
type: Source
title: "Hoelzl et al. (2021) — The JOREK non-linear extended MHD code and applications to large-scale instabilities and their control in magnetically confined fusion plasmas"
description: "Reference overview of the fully implicit non-linear extended-MHD code JOREK: ansatz-based reduced and full MHD models with their extensions, G1 Bézier/Hermite finite elements with a toroidal Fourier series, GMRES with a per-harmonic block preconditioner, STARWALL free-boundary coupling, verification benchmarks, and ELM and disruption applications."
resource: "doi:10.1088/1741-4326/abf99f"
source_kind: paper
authors: [Hoelzl M., Huijsmans G.T.A., Pamela S.J.P., Bécoulet M., Nardon E., Artola F.J., Nkonga B., Atanasiu C.V., Bandaru V., Bhole A., Bonfiglio D., Cathey A., Czarny O., Dvornova A., Fehér T., Fil A., Franck E., Futatani S., Gruca M., Guillard H., Haverkort J.W., Holod I., Hu D., Kim S.K., Korving S.Q., Kos L., Krebs I., Kripner L., Latu G., Liu F., Merkel P., Meshcheriakov D., Mitterauer V., Mochalskyy S., Morales J.A., Nies R., Nikulsin N., Orain F., Pratt J., Ramasamy R., Ramet P., Reux C., Särkimäki K., Schwarz N., Singh Verma P., Smith S.F., Sommariva C., Strumberger E., van Vugt D.C., Verbeek M., Westerhof E., Wieschollek F., Zielinski J.]
year: 2021
venue: "Nucl. Fusion 61:065001"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2021_Crossref_Nuclear_Fusion_Hoelzl_The_JOREK_non-linear_extended_MHD_code_and_applications_to_l.pdf"
tags: [review, code, mhd, reduced-mhd, full-mhd, extended-mhd, tokamak, finite-elements, spectral, time-integration, linear-solver, stabilization, free-boundary, wall, disruption, vde, runaway-electrons, impurities, neutrals, particles, elm, pedestal, edge, benchmark, verification]
timestamp: 2026-10-16T20:00:00Z
---

# Summary

The reference overview of [JOREK](/software/jorek.md), a massively
parallel, fully implicit, non-linear extended-MHD code for realistic
tokamak X-point plasmas, developed since 2002 (as "JOREK 2" since 2006).
It sets out a hierarchy of models. The base is an ansatz-based
(Galerkin-truncated, not aspect-ratio-ordered) reduced MHD model in the
variables $\psi$, $u$, $j$, $\varpi$, $\rho$, $T$, $v_\parallel$; a full
visco-resistive MHD model in the Weyl gauge sits beside it. Extensions:
drift-ordered diamagnetic Ohm's law with gyroviscous cancellation,
neoclassical poloidal friction, a bootstrap-current source, separate
electron and ion temperatures, a diffusive neutral fluid, a
[coronal-equilibrium impurity fluid](/methods/coronal-equilibrium-impurity-model.md),
pellet and SPI ablation sources, a
[runaway-electron fluid](/methods/runaway-electron-fluid-model.md), a
kinetic particle framework (Boris full orbit, RK4 and variational guiding
centre, relativistic tracers, moment projection), an electrostatic ITG
fluid model and a fully kinetic electrostatic model. Free boundary and
resistive walls come from the Green's-function code STARWALL, coupled
implicitly through a natural boundary condition on the current definition
equation. Space is discretized with $G^1$ isoparametric cubic
[Bézier/Hermite elements](/methods/bezier-finite-elements.md) (4 degrees of
freedom per node and variable) on flux-aligned grids that can extend to
the first wall, times a real toroidal Fourier series. Time advance is a
linearized implicit three-level scheme (Crank–Nicolson or BDF2); the
sparse system is solved by restarted GMRES with a block-diagonal
preconditioner, one block per toroidal harmonic (or "mode group"), each
LU-factorized by a direct solver and reused across steps; parallelism is
MPI+OpenMP. Verification covers finite-element convergence (fifth-order
growth-rate error), heat-transport anisotropy up to $10^{10}$, energy
conservation, reduced- versus full-MHD benchmarks against CASTOR3D,
SpeCyl and BOUT++, SOLPS, GO for the runaway fluid, VDE benchmarks with
DINA, CEDRES++, CASTOR3D, M3D-C1 and NIMROD, and pusher tests with ASCOT5.
The application chapters review ELMs and their control, QH-mode,
detachment, disruptions, ITG, TAEs and stellarator work.

# Key claims

1. **Ansatz-based reduction** (§2.3.1, Eqs. 25–27). JOREK's reduced MHD is
   a Galerkin truncation of full MHD on the ansatz $\mathbf A=\psi\nabla\phi$
   and a velocity of $\mathbf E\times\mathbf B$, ion diamagnetic and
   parallel parts, "not an aspect ratio expansion of the full MHD model";
   "there are no approximations on geometry" once ansatz and projections
   are fixed. Derived.
2. **Equilibrium preserved with constant $F_0$** (§2.3.1). Using $F_0$
   instead of $F(\psi)$ keeps the Grad–Shafranov equilibrium because all
   $F$-terms lie in the kernel of the two momentum projections; the
   Shafranov shift enters through the initial $\psi$. Derived.
3. **Energy conservation** (§2.3.3, Fig. 17). The single-fluid reduced
   model conserves energy at the equation level; gyroviscous cancellation
   breaks this at a small order in the diamagnetic parameter, and finite
   time step and toroidal truncation add errors. Derived (from the cited
   work) and Shown.
4. **Momentum** (§2.3.3). Reduced MHD does not conserve linear momentum
   locally (two scalar momentum equations); globally the vertical component
   is conserved (test function $\ln R$), the horizontal ones if $n=1$ is
   excluded. Full MHD conserves momentum at the equation level. Derived.
5. **Current continuity** (§2.3.3). The reduced model satisfies
   $\nabla\cdot\mathbf J=0$ in weak form (Eq. 31); poloidal currents exist
   and can be reconstructed a posteriori (Eq. 43). Derived.
6. **No fast magnetosonic waves** (§2.3.3). The velocity ansatz lacks
   perpendicular compression, which removes them. Attributed.
7. **Finite-β internal kink failure** (§2.3.3, Figs. 18–19). Reduced MHD
   fails for pressure-driven internal kinks at finite $\beta$: it keeps the
   parallel field perturbation near zero instead of letting it balance the
   pressure perturbation, leaving a spurious stabilizing energy term
   proportional to the squared imbalance. Edge ballooning modes are
   largely unaffected (modified Mercier criterion
   $4\alpha_{\mathrm b}(1-q^2)>\hat s^2q^2+\alpha_{\mathrm b}^2$ with
   $q\gg1$). Derived (after Graves et al.) and Shown.
8. **Finite-element convergence** (§4.1, Figs. 13–14). The growth-rate
   error converges as $N^{-5}$, with $N$ the geometric mean of the radial
   and poloidal grid counts, for a tearing mode (full MHD) and the cbm18
   $n=20$ ballooning mode (reduced MHD); full MHD gives only third order on
   the ballooning case (under investigation). Shown.
9. **Anisotropic heat transport** (§4.2, Fig. 16). On a flux-aligned grid
   $\kappa_\parallel/\kappa_\perp>10^{10}$ is resolved on 200×200 points
   within 0.3% core-temperature error, error $\propto N^{-3}$; on an
   unaligned grid the error is $\propto N^{-2}$ and the limit about
   $10^9$. Shown.
10. **Energy balance** (§4.3, Fig. 17). Well satisfied in a 3D VDE and in an
    ITER RMP case with diamagnetic flows; about 90% in massive-injection
    runs with Taylor–Galerkin stabilization. Shown.
11. **Reduced vs full MHD, peeling–ballooning** (§4.5, Fig. 22). Growth
    rates in a JET-like X-point case, with and without diamagnetic
    effects, agree within 5%. Shown.
12. **JOREK vs BOUT++** (§4.5, Fig. 21). Linear ballooning growth rates
    agree within 4%, with and without diamagnetic effects. Shown.
13. **JOREK vs SpeCyl** (§4.4, Fig. 20). Non-linear 2/1 tearing at
    $S=10^6$: maximum deviation about 5%, attributed to toroidal versus
    cylindrical geometry. Shown.
14. **Runaway fluid vs GO** (§4.7, Fig. 24). Current conversion agrees to
    about 1%. Shown.
15. **3D VDE benchmark** (§4.8, Figs. 28–29). JOREK (reduced) vs M3D-C1 and
    NIMROD (full): thermal quench 0.14 / 0.24 / 0.20 ms; vertical force in
    good agreement; horizontal force "a factor 2 smaller" in NIMROD; no
    $I_p$ toroidal asymmetry in JOREK (versus 1–4% in the full-MHD codes)
    because of its $\Phi=0$ wall condition. Shown. The horizontal-force
    characterization differs from that of the benchmark paper itself
    ([Artola et al. (2021)](/sources/artola-2021.md), §4.1.4: "good
    agreement in magnitude", 2.5–3.5 kN), which also states the boundary
    condition as $\Phi=$ const.
16. **Passive coils vs CASTOR3D** (§4.8, Fig. 30). ASDEX Upgrade PSL VDE
    growth rate within about 20% over orders of magnitude of PSL
    conductivity. Shown.
17. **Pushers** (§4.9, Fig. 31). Boris conserves energy near machine
    precision; RK4 error scales between fourth and fifth order; the
    modified Qin variational integrator has bounded error but is unstable
    above about 1000 gyro-periods per step. Shown.
18. **Scaling** (§3.6, Figs. 9–10). JT-60SA ELM case (about 5000 nodes,
    $n=1$–15): about 50% relative efficiency from 16 to 160 compute nodes
    (about 85% at 32); STARWALL speed-up 63.3 on 128 MPI tasks. Shown.
19. **Disruption mode coupling** (§6.2.1). The MGI-triggered thermal quench
    in JET proceeds by a current-profile avalanche 2/1 → 3/2 → 4/3; SPI
    regimes are set by the ordering of shard transit time and local
    current-decay time (a resistive diffusion time over the local current-profile scale). Shown
    (simulations) and Derived (scaling).
20. **ITER halo fraction** (§6.3, Fig. 62). The halo-current fraction
    depends on the ratio of current-quench time to wall time: about 10%
    when it is small, up to about 50% when it is large; the predicted
    10–20% for 50–150 ms current quenches means the disruption mitigation
    system "could be used to reduce the halo current electromagnetic loads
    by more than a factor 2". Shown.
21. **Type-I ELM cycles** (§5.1, Fig. 39). Multiple type-I ELM cycles in
    realistic ASDEX Upgrade simulations "for the first time"; diamagnetic
    drift is "imperative" for cycling, and ELM frequency rises with heating
    power. Shown (from the cited work).
22. **Coronal-equilibrium thermal quench** (§2.7). In the axisymmetric
    impurity benchmark (Lyons et al. 2019), JOREK's coronal-equilibrium
    model gives a thermal collapse about twice slower than M3D-C1 and
    NIMROD, which resolve charge states. Stated.

# Models and numerics

**Coordinates and equilibrium** (§2.1–2.2, App. A). $(R,Z,\phi)$ with
$\phi$ clockwise seen from above (COCOS 8), Jacobian $R$. A built-in
Grad–Shafranov solver on the same finite-element grid takes $p$ (through
$T$ and $\rho$) and $FF'$ against $\psi_N$, solves on an initial grid,
builds a flux-aligned grid and re-solves; Picard or Newton iterations; a
free-boundary solve through STARWALL.

**Full MHD** (Eqs. 1–5; the paper uses $\mu_0=1$ and $\rho_0$-normalized
units, written here in SI form):

$$\begin{aligned}
\partial_t\mathbf A &= -\mathbf E-\nabla\Phi,\\
\rho\,\partial_t\mathbf v &= -\rho\mathbf v\cdot\nabla\mathbf v-\nabla p+\mathbf J\times\mathbf B+(\text{viscous force})+\mathbf S_{\mathbf v},\\
\partial_t\rho &= -\nabla\cdot(\rho\mathbf v)+\nabla\cdot(\mathsf D\nabla\rho)+S_\rho,\\
\partial_t p &= -\mathbf v\cdot\nabla p-\Gamma p\nabla\cdot\mathbf v+\nabla\cdot(\mathsf K\nabla T)+(\Gamma-1)(\text{viscous heating})+S_p,
\end{aligned}$$

with $p=\rho T$ ($T=T_e+T_i$ in energy units per ion mass, normalized),
$\mathbf B=F\nabla\phi+\nabla\times\mathbf A$, $\mu_0\mathbf J=\nabla\times\mathbf B$;
$F(\psi)=RB_\phi$ is fixed in time from the equilibrium "for numerical
reasons". $\mathsf D$ and $\mathsf K$ are the anisotropic diffusion and
conduction tensors, $\mathsf K=\kappa_\parallel\mathbf b\mathbf b+\kappa_\perp(\mathsf I-\mathbf b\mathbf b)$
(Eq. 13); the factor $\Gamma-1$ is absorbed into $\kappa$ in the paper.

* Ohm's law (Eq. 6): $\mathbf E=-\mathbf v\times\mathbf B+\eta(\mathbf J-\mathbf J_x)+(\text{diamagnetic term in }\nabla_\perp p_i-\nabla_\parallel p_e)$,
  $\eta\propto T^{-3/2}$ (Spitzer), $\mathbf J_x$ toroidal, either fixed or
  bootstrap-evolving (Sauter formulas).
* Weyl gauge $\Phi=0$ in full MHD, so $A_\phi$ evolves even in steady
  state.
* Viscosity (Eqs. 9–12): parallel Braginskii/CGL part; perpendicular
  viscosity $\propto T^{-3/2}$ (constant magnetic Prandtl number);
  heuristic neoclassical poloidal friction towards a neoclassical velocity;
  gyroviscous cancellation. Ion diamagnetic heat-flux terms are omitted to
  avoid ITG destabilization.
* Heat conduction (Eqs. 13–14): $\kappa_\parallel\propto T^{5/2}$
  (Spitzer–Härm) with an optional cap as a flux-limiter proxy;
  $\kappa_\perp$ and $D_\perp$ are ad-hoc profiles; $D_\parallel$ is
  usually unused.
* Sources (Eqs. 15–16) are written so that mass and energy sources carry
  consistent momentum and kinetic energy.
* Weak form (Eqs. 17–24): Galerkin; $\mathbf J\times\mathbf B$ in
  Maxwell-stress form plus integration by parts avoids second derivatives;
  velocity test functions along $\mathbf e_R$, $\mathbf e_Z$, $\mathbf B$,
  so the parallel projection of $\mathbf J\times\mathbf B$ vanishes
  exactly at the discrete level.

**Reduced MHD** (§2.3.1, Eqs. 25–39, Table 1). Ansatz

$$\mathbf A=\psi\nabla\phi,\qquad \mathbf B=F_0\nabla\phi+\nabla\psi\times\nabla\phi,\qquad
\mathbf v=-R^2\nabla u\times\nabla\phi+\mathbf v_{\mathrm{dia},i}+v_\parallel\mathbf b,$$

with $u=\Phi/F_0$ and $\mathbf v_{\mathrm{dia},i}$ the ion diamagnetic velocity; JOREK evolves the coefficient $\hat v_\parallel=v_\parallel/B$ of
$\mathbf B$ rather than $v_\parallel$ itself (Notation map). Strong-form reading of the weak flux equation (Eq. 28):

$$\partial_t\psi=-R\,[u,\psi]-\eta\,(j-j_x)+F_0\,\partial_\phi u-(\text{diamagnetic term}),\qquad [f,g]=\mathbf e_\phi\cdot\nabla f\times\nabla g ,$$

where the poloidal current is neglected in the resistive term. The two
scalar momentum equations are the projections of the momentum equation on
$\mathbf B$ times a test function and on the $\mathbf E\times\mathbf B$
test direction (Eqs. 30–31); density and pressure follow full MHD with
the prescribed fields. Definition equations (Eqs. 38–39):
$j=\Delta^*\psi$ ($j=-RJ_\phi$ in normalized units) and
$\varpi=\nabla\cdot\nabla_{\mathrm{pol}}u$, both projected on the $G^1$
basis. Five evolved fields and two defined ones; a variant drops
$v_\parallel$ (no slow waves). Poloidal current reconstruction: Eq. 43.

**Boundary conditions** (§2.3.2). Dirichlet on all variables where the
boundary is a flux surface. Where field lines hit the wall: Bohm sheath
conditions, with $\psi$, $j$, $u$, $\varpi$ fixed, the parallel velocity
set to $c_s$, no Dirichlet on $\rho$ and zero diffusive particle flux;
sheath heat fluxes with transmission factors $\delta_{\mathrm{sh}}$ of
about 2–3 (ions), 5–6 (electrons) and 7–8 (single temperature), imposed as natural
conditions on the conductive flux. Optional limitation of $j$ to the ion
saturation current. Free boundary replaces the Dirichlet conditions on
$\psi$ and $j$ by the STARWALL natural condition.

**Extensions** (§2.4–2.14). RMPs by a ramped vacuum boundary perturbation
or self-consistent coils through STARWALL; two temperatures; one diffusive
neutral fluid with ionization, recombination and radiation (recycling
conditions recent; kinetic neutrals planned); impurities as a constant
radiation background, a coronal-equilibrium fluid (all charge states
convected with the plasma, ionization energy as potential energy), or
kinetic tungsten; pellets with NGS-type ablation and a localized
deposition source moving on straight lines (converged in the toroidal
width for D pellets, not necessarily for impurity pellets, whose radiated
power scales inversely with it), applied per shard for SPI;
JOREK–STARWALL (below); kinetic particles (Boris full orbit with a
toroidal correction, relativistic full-orbit or guiding-centre tracers,
OPEN-ADAS charge states, binary collisions, sputtering; pressure or
current coupling; moments projected on the finite-element basis with an
optional fourth-order smoothing of weight $10^{-10}$–$10^{-12}$; 100–1000
particle steps per fluid step for fast ions, 1–10 for heavy impurities);
a runaway-electron density fluid with primary and secondary sources;
full MHD with diamagnetic, neoclassical, rotation and bootstrap terms
(sheath conditions and stabilization recent, no neutrals yet); an
electrostatic ITG fluid model (CYCLONE-benchmarked); fully kinetic
electrostatic ions with adiabatic electrons.

**Free boundary and walls** (§2.9). STARWALL: thin-wall triangles and a
Green's-function vacuum (not discretized). The vacuum response enters as
a natural condition on the boundary integral of the current definition
equation: the tangential field equals a vacuum response matrix times the
normal field plus a coupling matrix times the wall and coil currents,
which obey circuit equations. Response matrices are computed once per
grid and wall, exchanged by MPI-IO; the coupling is fully implicit with
the wall currents eliminated analytically, so the matrix size is
unchanged. Free or fixed boundary per harmonic; PF, 3D and passive coils
and sensors. Halo currents follow the Zakharov–Atanasiu formalism as a
post-processor for wall forces; the implicit wall-potential coupling is
not implemented and $\Phi=0$ on the wall. STARWALL is MPI-parallel.

**Spatial discretization** (§3.1). Cubic Bézier basis on element-local
coordinates in $[0,1]^2$ for both geometry and variables (isoparametric); $G^1$ continuity
(continuous value and real-space gradient) with 4 degrees of freedom per
node and variable and element-specific scale factors, a generalization of
the HELENA bicubic Hermite elements, with local refinement. $G^1$ is not
strictly enforced at the magnetic axis and near X-points (more than four
elements per node). Flux-aligned grids per topology (no, upper, lower,
double X-point), wall-extended patches to the first wall, polar or
rectangular grids for VDEs. Toroidal direction: real Fourier series;
$N_{\mathrm{tor}}$ counts cosines and sines separately (odd), an optional
periodicity keeps multiples of a base $n$, and the number of planes is at
least $2(N_{\mathrm{tor}}-1)$ for de-aliasing (powers of two fastest,
FFTW).

**Time integration** (§3.2, App. C). A three-level scheme with
implicitness $\theta_{\mathrm t}$ and multistep weights $\xi_{\mathrm t}$,
$\phi_{\mathrm t}$ (Eq. 62, Notation map), second order when
$\phi_{\mathrm t}+\theta_{\mathrm t}-\xi_{\mathrm t}=1/2$, used with
$\phi_{\mathrm t}=0$ and linearized once per step (Eqs. 56, 64).
Crank–Nicolson: $(\theta_{\mathrm t},\xi_{\mathrm t})=(1/2,0)$; BDF2
(Gear): $(1,1/2)$; implicit Euler $(1,0)$, not used in production. The definition
equations are imposed at the new time level. Newton iterations were tested
and dropped (cost and memory outweighed larger steps).

**Stabilization** (§3.3). Variational multiscale framework (SUPG and
Taylor–Galerkin as subsets): anisotropic artificial diffusion with parallel
and perpendicular coefficients $\propto(\mathbf v\cdot\mathbf b)^2$ and
$|\mathbf v|^2-(\mathbf v\cdot\mathbf b)^2$, scaled by an intrinsic time
$\tau_{\mathrm s}\sim h_e/(\text{maximum wave speed})$ that vanishes under refinement;
Taylor–Galerkin uses $\tau_{\mathrm s}=\Delta t/2$; full MHD uses a global
hyperbolic VMS. The effect on physics and conservation is claimed
negligible.

**Matrix, solver, parallelization** (§3.4–3.6). Sparse matrix (about one
non-zero in several thousand) assembled with distributed domain
decomposition; Gauss quadrature in the element coordinates, direct summation or FFT
toroidally; matrix-free assembly tested and rejected. Axisymmetric runs:
direct solve (PaStiX mostly, MUMPS, WSMP, STRUMPACK; PT-Scotch/ParMETIS
ordering; low-rank compression only tested). 3D runs: restarted GMRES on
the global matrix, preconditioned by the diagonal blocks of the
toroidal-harmonic block structure (block Jacobi in harmonics), each solved
by direct LU on one or more MPI tasks. The analysis runs once; LU is
redone when the GMRES count exceeds a threshold, so factors are reused in
linear phases but recomputed almost every step in strongly non-linear
phases, where it dominates the cost. "Mode groups" form multi-harmonic,
possibly overlapping blocks; complex-arithmetic block solves save memory.
Stated limits: preconditioner memory, direct-solver scalability,
degradation under strong mode coupling. The number of MPI tasks is a
multiple of the number of harmonics; the full state is duplicated on all
ranks; parallel HDF5 for particles. CPU only; GPUs planned (particles
first).

**Code management** (§3.7). Fortran 90/95 (F2003/2008 for particles) with
C/C++ cores, over 250k lines, over 40 users; git, issue tracker, pull
request reviews, about 50 regression tests per push (Intel and gfortran,
debug flags).

# Tests and results

| Test | Setup | Result | Location |
|---|---|---|---|
| FE convergence, tearing (full MHD) | circular, grids (27,180)–(90,600) | error $\propto N^{-5}$ | §4.1, Fig. 13 |
| FE convergence, cbm18 $n=20$ | circular | 5th order (reduced), 3rd (full) | §4.1, Fig. 14 |
| Anisotropic conduction | $R_0=100$ m, $a=1$ m, 1/1 island, one implicit-Euler step | $>10^{10}$ at 0.3% (aligned, $N^{-3}$); $\approx10^9$ (unaligned, $N^{-2}$) | §4.2, App. D |
| Energy balance | 3D VDE; ITER 15 MA RMP; MMI | good; small Ohmic-heating discrepancy at the quench end; ≈90% (MMI) | §4.3, Fig. 17 |
| 1/1 kink, 2/1 tearing vs CASTOR3D | η scans | full MHD agrees; reduced deviates at low η and "clearly fails" at finite β | §4.4, Figs. 18–19 |
| 2/1 tearing vs SpeCyl | $R_0/a=10$, zero β, $S=10^6$ | ≤5% | §4.4, Fig. 20 |
| Ballooning vs BOUT++ | circular, aspect ratio 3.3, $q_{95}=3$, $\eta=6.1\times10^{-6}$ Ω m | within 4% (linear) | §4.5, Fig. 21 |
| Peeling–ballooning, reduced vs full | JET-like X-point | within 5% | §4.5, Fig. 22 |
| SOL vs SOLPS | MAST-U Super-X | roll-over less steep (no charge exchange) | §4.6, Fig. 23 |
| Runaway fluid vs GO | $R_0=10$ m, $I_p=0.67$ MA, 1.7 keV → 25 eV in ≈60 ms | ≈1% | §4.7, Fig. 24 |
| Resistive kink with runaway fraction 0, 0.5, 1 | $I_p=0.31$ MA | $S^{-1/3}$ recovered at large η | §4.7, Fig. 25 |
| Axisymmetric VDE vs DINA | ITER 15 MA; 7.5 MA vertical oscillation | LCFS within a few cm; position matches | §4.8, Figs. 26a, 27 |
| Axisymmetric VDE vs M3D-C1, NIMROD | NSTX-like | "excellent agreement" | §4.8, Fig. 26b |
| 3D VDE vs M3D-C1, NIMROD | NSTX, $n\in[0,10]$ | see claim 15 | §4.8, Figs. 28–29 |
| PSL VDE vs CASTOR3D | ASDEX Upgrade | ≤20% (needs high SOL resistivity) | §4.8, Fig. 30 |
| Banana orbit | 26 periods | see claim 17 | §4.9, Fig. 31 |
| Relativistic tracer vs ASCOT5 | JET thermal-quench fields, 5000 electrons of 1 MeV | good; slight deviation | §4.10, Fig. 32 |

Earlier JOREK–STARWALL tests: equilibria and tearing with a wall, RWM
growth rates against analytic values, VDEs against CEDRES++ within
10–20%, coil fields against Biot–Savart. Applications (§§5–7, read from
the text, figures not examined): ELM physics and cycles, pellet triggering
(DIII-D threshold 1.5–1.8 mm; JET 10–20% agreement with thermography;
ASDEX Upgrade lag time), vertical kicks, RMP penetration and suppression,
QH-mode and the edge harmonic oscillation, detachment, 2/1 locking,
radiation-driven island growth, the MGI avalanche, the $I_p$ spike in JET
85943 (incomplete relaxation rather than helicity dissipation, against
Boozer), SPI mixing and TPF above 2 for single injection, ITER halo
fractions (TPF of fast-quench halo currents ≲1.15), runaway-electron VDEs
and JET benign termination ($n=1$ double tearing at two $q=4$ surfaces,
losses within 100 µs), ITG with $10^9$ ions agreeing with GENE, XGC and
ORB5, TAE excitation, the ITPA TAE benchmark ($10^8$ particles, pressure
coupling, the only full-orbit code), and a QA-stellarator approximation
with virtual coil currents.

# Notation map

| Hoelzl et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $(R,Z,\phi)$, $x=R\cos\phi$, $y=-R\sin\phi$ | $(R,Z,\phi)$ | $\phi$ clockwise from above, COCOS 8 |
| $\Psi=R\mathbf A\cdot\mathbf e_\phi$ ($\psi$ in Eq. 25) | $\psi$ | per radian; $\Psi_N\to\psi_N$ |
| $F$, $F_0$ | $F$, $F_0$ | |
| $u=\Phi/F_0$ | $u$ | $u_{SI}=u/\sqrt{\mu_0\rho_0}$ |
| $\Phi$ | $\Phi$ | Weyl gauge $\Phi=0$ in full MHD |
| $j=-RJ_\phi=\Delta^*\Psi$ | $j$ | normalized, $\mu_0=1$; $j_{\phi,SI}=-j/(R\mu_0)$ |
| $\omega=\Delta_{pol}u$ | $\varpi$ | **collision:** registry $\omega$ is a frequency |
| $\mathbf w=\nabla\times\mathbf v$ | words (vorticity vector) | |
| $\rho=n_em_{ion}$ | $\rho$ | $\rho_{SI}=\rho\rho_0$ |
| $T=T_e+T_i$, $p=\rho T$ | $T$, $p$ | $T_{SI}=T/(k_B\mu_0n_0)$, $p_{SI}=\rho T/\mu_0$ |
| $v_\parallel$ ($\mathbf v_\parallel=v_\parallel\mathbf B$) | $\hat v_\parallel=v_\parallel/B$ | **collision:** registry $v_\parallel=\mathbf v\cdot\mathbf b$ is a speed; JOREK's $v_\parallel$ is the coefficient $\hat v_\parallel$ |
| $\mathbf v_E$, $\mathbf v_{dia,i}$ ($\mathbf v_i^*$) | $\mathbf v_E$; $\mathbf v_{\mathrm{dia},i}$ | $-R^2\nabla u\times\nabla\phi$; ion diamagnetic velocity |
| $\delta^*$ ($\delta_*$) | words (diamagnetic parameter $m_i/(eF_0\sqrt{\mu_0\rho_0})$) | |
| $\mathbf J_\star$, $j_S$, $j_B$ | $\mathbf J_x$, $j_x$ | bootstrap form $j_0+j_B-j_{B,0}$ |
| $\gamma$ | $\Gamma$ | **collision:** registry $\gamma$ is a growth rate |
| $\underline{\boldsymbol\tau}$ ($\underline{\boldsymbol\tau}_f$, $\underline{\boldsymbol\tau}_{neo}$, $\underline{\boldsymbol\tau}_{gv}$) | $\mathsf\Pi$ (viscous part; $\mathsf\Pi_{\mathrm{neo}}$, $\mathsf\Pi_{\mathrm{gv}}$ the neoclassical and gyroviscous parts) | viscous stress |
| $\nu_\parallel,\nu_\perp,\nu_{neo}$ | $\nu$; words | dynamic; $\nu_{SI}=\nu\sqrt{\rho_0/\mu_0}$ |
| $\underline{\boldsymbol\kappa}$, $\kappa_\parallel,\kappa_\perp$ | $\mathsf K$; $\kappa_\parallel$, $\kappa_\perp$ | $(\Gamma-1)$ absorbed; $\kappa_{SI}=\kappa\sqrt{\rho_0/\mu_0}/(\Gamma-1)$ |
| $\underline{\mathbf D}$, $D_\perp$ | $\mathsf D$; $D_\perp$ | $D_{SI}=D/\sqrt{\mu_0\rho_0}$ |
| $\eta$ | $\eta$ | $\eta_{SI}=\eta\sqrt{\mu_0/\rho_0}$ |
| $t$ | $t$ | $t_{SI}=t\sqrt{\mu_0\rho_0}$, about $\tau_A/2.5$ for ITER |
| $\gamma_n=\ln[E_n(t_2)/E_n(t_1)]/[2(t_2-t_1)]$ | $\gamma$ | amplitude growth rate |
| $\tau_A=a\sqrt{\mu_0\rho_0}/B_0$ | $\tau_A$ | length $a$ |
| $[f,g]$, $\Delta^*$, $\Delta_{pol}$ | $[f,g]$, $\Delta^*$, $\nabla\cdot\nabla_{\mathrm{pol}}$ | |
| $\gamma_{sh}$, $\gamma_{sh,i}$, $\gamma_{sh,e}$; $c_b$ | $\delta_{\mathrm{sh}}$ (per species); words (natural-BC coefficients) | **collision** with growth rate $\gamma$ |
| $c_s$ | $c_s$ | |
| $\mathbf B\times\mathbf n=M_{vac}\mathbf B\cdot\mathbf n+M_I\mathbf I$ | words | STARWALL response matrices; wall/coil currents |
| $\eta_{wall,thin}=\eta_{wall}/d_{wall}$ | $\eta_w/d_w$ | ITER $1.33\times10^{-5}$ Ω |
| HF $=(1/I_{p,0})\int\lvert\mathbf J\cdot\mathbf n\rvert/2\,dS_{wall}$ | words (halo fraction) | |
| $s,t$ | words (element coordinates) | **collision:** registry $s$ is a radial label |
| $n_{tor}$, $n_{period}$, $n_{plane}$ | $N_{\mathrm{tor}}$ (real harmonics, odd); words | |
| $n_{flux}$, $n_{tht}$ | words; $N=\sqrt{n_{flux}n_{tht}}$ | |
| App. C: $(1+\xi)A^{n+1}-(1+2\xi)A^n+\xi A^{n-1}=\Delta t[\theta B^{n+1}+(1-\theta-\phi)B^n-\phi B^{n-1}]$ | $\theta_{\mathrm t}$, $\xi_{\mathrm t}$, $\phi_{\mathrm t}$ | **collision:** $\phi$ is the toroidal angle; $A$, $B$ are generic operators of $\partial_tA(\mathbf u)=B(\mathbf u,t)$ (**collision** with $\mathbf A$, $\mathbf B$) |
| $\tau^*$ | $\tau_{\mathrm s}$ | stabilization time scale |
| Mercier: $4\alpha(1-q^2)>s^2q^2+\alpha^2$ | $4\alpha_{\mathrm b}(1-q^2)>\hat s^2q^2+\alpha_{\mathrm b}^2$ | **collision:** native $s$ (shear) vs registry radial label |
| $e_{tot}$, $\Gamma_{tot}$, $S_E$ (Eqs. 57–60) | words | **collision:** $\Gamma_{tot}$ (energy flux) vs $\Gamma$ |

# Pages created or updated

Chunk 1 (2026-10-16) created every page of the bundle; chunks 2 and 3 (2026-10-16) extended many. This source is cited on:

* [Ballooning mode](/definitions/ballooning-mode.md)
* [Bootstrap current and its MHD implementation](/definitions/bootstrap-current.md)
* [BOUT++](/software/bout-plus-plus.md)
* [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md)
* [CASTOR3D](/software/castor3d.md)
* [cbm18 ideal-ballooning benchmark](/benchmarks/cbm18-ballooning-benchmark.md)
* [CLT–M3D-C1 tearing and resistive-kink benchmark](/benchmarks/clt-m3d-c1-benchmark.md)
* [Collisional-radiative (non-equilibrium) impurity model](/methods/collisional-radiative-impurity-model.md)
* [Coronal-equilibrium impurity model](/methods/coronal-equilibrium-impurity-model.md)
* [DIII-D gas-injection impurity benchmark (Lyons et al. 2019)](/benchmarks/diii-d-mgi-impurity-benchmark.md)
* [Disruption: phases, current quench and current spike](/definitions/disruption.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Double tearing mode](/definitions/double-tearing-mode.md)
* [Edge harmonic oscillation and QH-mode](/definitions/edge-harmonic-oscillation.md)
* [Edge-localized mode (ELM) and ELM-free regimes](/definitions/edge-localized-mode.md)
* [Electromagnetic wall forces (vertical and sideways)](/definitions/wall-forces.md)
* [Fluid neutral models and plasma–neutral atomic sources](/methods/fluid-neutral-models.md)
* [Free-boundary and resistive-wall coupling](/methods/resistive-wall-coupling.md)
* [Grad–Shafranov equation](/definitions/grad-shafranov-equation.md)
* [Halo current](/definitions/halo-current.md)
* [Hybrid kinetic-MHD models](/methods/hybrid-kinetic-mhd.md)
* [Implicit time integration and preconditioned Krylov solvers for nonlinear MHD](/methods/implicit-time-integration.md)
* [Interchange modes and the Mercier criterion](/definitions/interchange-mode.md)
* [ITER runaway-electron benchmarks (JOREK–GO, JOREK–DINA)](/benchmarks/iter-runaway-electron-benchmarks.md)
* [ITPA n = 6 TAE benchmark](/benchmarks/itpa-tae-benchmark.md)
* [JOREK](/software/jorek.md)
* [JOREK3D](/software/jorek3d.md)
* [Linear MHD eigenvalue codes](/methods/linear-mhd-eigenvalue-codes.md)
* [M3D](/software/m3d.md)
* [M3D-C1](/software/m3d-c1.md)
* [Massive gas injection](/definitions/massive-gas-injection.md)
* [NIMROD](/software/nimrod.md)
* [NSTX VDE benchmarks of JOREK, M3D-C1 and NIMROD (axisymmetric and 3D)](/benchmarks/nstx-vde-benchmarks.md)
* [ORB5](/software/orb5.md)
* [Particle pushers: Boris, slow-manifold Boris, guiding-centre and gyrokinetic](/methods/particle-pushers.md)
* [Particle-to-finite-element moment projection](/methods/particle-to-mesh-projection.md)
* [Pellet ablation and fragmentation models](/methods/pellet-ablation-models.md)
* [Pressure coupling and current coupling](/methods/pressure-and-current-coupling.md)
* [Reduced MHD for stellarators](/methods/stellarator-reduced-mhd.md)
* [Reduced MHD for tokamaks](/methods/reduced-mhd.md)
* [Reduced-MHD boundary condition suppresses the toroidal asymmetry of the plasma current](/results/reduced-mhd-current-asymmetry.md)
* [Resistive internal kink (m/n = 1/1)](/definitions/resistive-internal-kink.md)
* [Resistive tearing mode](/definitions/tearing-mode.md)
* [Resonant magnetic perturbations and plasma response](/definitions/resonant-magnetic-perturbation.md)
* [Runaway current reconstitution after an MHD flush](/results/runaway-reconstitution-after-mhd-flush.md)
* [Runaway electrons and their generation mechanisms](/definitions/runaway-electrons.md)
* [Runaway-electron fluid model coupled to MHD](/methods/runaway-electron-fluid-model.md)
* [Shattered pellet injection and massive material injection](/definitions/shattered-pellet-injection.md)
* [Sheath (Bohm) boundary conditions](/methods/sheath-boundary-conditions.md)
* [Single-fluid visco-resistive MHD model](/methods/visco-resistive-mhd-model.md)
* [STARWALL](/software/starwall.md)
* [Thermal quench](/definitions/thermal-quench.md)
* [Toroidal Alfvén eigenmode (TAE)](/definitions/toroidal-alfven-eigenmode.md)
* [Toroidal radiation asymmetry and first-wall energy impact](/definitions/radiation-asymmetry.md)
* [Variational multiscale (VMS) stabilization for MHD finite elements](/methods/variational-multiscale-stabilization.md)
* [Vertical displacement event (hot and cold VDE)](/definitions/vertical-displacement-event.md)
* [Vertical-force mitigation by massive material injection](/results/vertical-force-mitigation.md)
* [XTOR-K](/software/xtor-k.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2021_Crossref_Nuclear_Fusion_Hoelzl_The_JOREK_non-linear_extended_MHD_code_and_applications_to_l.pdf`
   * **Version.** arXiv:2011.09120v3 [physics.plasm-ph], 21 April 2021, an
     accepted-manuscript-level preprint of 127 pages (body pp. 1–105,
     bibliography pp. 107–123, Appendices A–D pp. 123–127). Page and section
     numbers above are those of this version.
   * **Identity.** doi:10.1088/1741-4326/abf99f, checked on Crossref:
     Nucl. Fusion 61(6), article 065001, online 20 May 2021, issue June
     2021; 53 authors, first author Hoelzl M.; title matches.
   * **How read.** Everything read. §§1–4 and Appendices A–D closely, with
     key equations checked on the rendered pages (pp. 9–19, 26–28, 35–37,
     51–52, 125–126). §§5–7 (applications) read in full from the text and
     summarized briefly; their figures were not examined.
   * **Recorded as printed.**
     * §4.4 text: "a low-β m=n=1 tearing-mode"; Fig. 18 caption: "2/1
       tearing mode". §4.4 announces benchmarks against "MISHKA and
       CASTOR" but shows only CASTOR3D.
     * Eq. 28 writes $\delta_*$ and $j_\star$ where Eqs. 6 and 8 use
       $\delta^*$ and $\mathbf J_\star$; §2.3 weak form lists
       $(\mathbf A,\mathbf V,\rho,T)$ in spaces indexed by $p$.
     * Eq. 44: the text names "$\delta r_c$ and $\phi_c$", the equation
       uses $\delta\phi_c$; the radial argument of tanh is a squared
       distance over a length.
     * App. C uses $\phi$ as a time-scheme weight, clashing with the
       toroidal angle.
     * App. D: unbalanced parenthesis in the island perturbation, read as
       $(R-R_{\mathrm{axis}})\cos\phi$.
     * Eqs. 49–50 (fully kinetic model) are schematic in normalized units,
       with no $e/T_e$ factor on the potential term.
     * App. B gives $u_{SI}$ in m s⁻¹ while calling $Ru$ the stream
       function and $F_0u$ the potential.
     * §4.1: "$p=4$ because the Bezier elements are bi-cubic" uses $p$ as
       the order of accuracy (degree plus one).
     * Fig. 38 caption records that the labels of Figs. 4a/b of its
       ref. [45] were swapped in the original (an erratum to that paper).
     * §3.6 refers to §3.4 for the size of the $n=0$ block, which §3.4
       does not discuss.
     * §4.8 characterizes the 3D VDE horizontal force as "factor 2 smaller
       in NIMROD"; the benchmark paper reports "good agreement in
       magnitude" (see claim 15). It states the wall condition as
       $\Phi=0$, the benchmark paper as $\Phi=$ const.
     * "Alfvèn" (p. 6); spellings Huysmans/Huijsmans and Hölzl; Alenikova
       ([278]) vs Aleynikova ([169], [248]).
     * As of v3, refs. [71], [73], [92], [99], [112], [115], [124], [133],
       [148], [220], [233], [266], [268], [278], [293], [301] are submitted
       or private communications; [231] is "accepted".
   * **Reference list.** 303 printed entries ([1]–[303]), merged into the
     bibliography under `hoelzl-2021`. Three works are printed twice and
     dedup to one entry each: [33]=[46] (`sauter-1999`), [168]=[288]
     (`matsuyama-2017`), [248]=[273] (`lehnen-2015`), giving 300 entries.
     The VDE benchmark printed "submitted" (2020), ref. [99], is the
     ingested `artola-2021`; `artola-2020-b` is the COMPASS Varenna–Lausanne
     2020 paper; the thesis printed "Francisco Javier Artola Such" (ref.
     [93]) is `artola-2018-c`; works printed as "submitted" under
     `nikulsin-2020` and `pamela-2021` are folded into `nikulsin-2021` and
     `pamela-2022`. Wrong or malformed DOIs omitted: [158] (prints [157]'s
     DOI), [119] (a PII), [104] (malformed). Garbled author strings
     resolved: [48] `chew-1956`, [174] `qin-2009`, [85] `parks-2020` (true
     first author likely Bosviel; year printed 2020 for EPS 2019); [140]
     "S. L. Xiaoye" is Xiaoye S. Li. The JOREK website [42] is
     `jorek-2021`.

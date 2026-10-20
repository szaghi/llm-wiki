---
type: Method
title: "Local time stepping"
description: "Local time stepping lets regions, cells or subdomains of a locally refined semi-discretization advance with their own explicit steps instead of the global CFL step of the smallest cell; the page compares leapfrog LTS for waves, asynchronous cell-level LTS, overlapping-subdomain LTS, clustered ADER-DG LTS and multi-time-step partitioned coupling by interface treatment, conservation, order, stability and speedup."
status: established
aliases: [LTS, local time-stepping, LF-LTS, stabilized LF-LTS, leapfrog local time stepping, asynchronous time integration, asynchronous Runge–Kutta, LESAULTS, clustered local time stepping, multi-time step, subcycling, Gravouil–Combescure method]
tags: [multirate, local-time-stepping, explicit, stability, parallel, structure-preserving]
timestamp: 2026-10-20T16:00:00Z
---

# Local time stepping

Local mesh refinement, material contrast or small distorted cells force any standard
explicit scheme to take a **global** step set by the most restrictive element, even
when that element is one of very few
([Grote et al. 2021](/sources/grote-2021.md), §1;
[Unfer 2021](/sources/unfer-2021.md), §1;
[Sreejith et al. 2022](/sources/sreejith-2022.md), §1). **Local time stepping (LTS)**
lets each region, cell or subdomain advance with a step close to its own stability
limit and couples the regions at their interfaces. It is the spatially organized
member of the multirate idea: where [multirate GARK](/methods/multirate-gark.md) and
[multirate infinitesimal](/methods/multirate-infinitesimal-methods.md) methods split
the right-hand side into fast and slow terms, LTS splits the unknowns by mesh region.
Throughout this page $H$ is the coarse (macro) step, $h=H/m$ the local (micro) step
and $m$ the step ratio (registry multirate notation; the sources write $\Delta t$ and
$\Delta t/p$, $\Delta t_i$, $\Delta t^s$ and $\Delta t^f$, or $R_{\delta t}$).

## What the gain can be

Two sources give the attainable speedup under ideal conditions. Unfer (2021, §3.1,
Eq. 44) defines the **asynchronous speed-up number**
$A_s=N_{\mathrm{cell}}\big/\big(\min_i h_i\sum_i1/h_i\big)$ ($N_{\mathrm{cell}}$ cells, local
steps $h_i$; page-local symbols), the ratio of updates of global and local stepping.
Sreejith et al. (2022, §3, Eqs. 1–3) derive, for two subdomains with step ratio $m$ and
node ratio $N_1/N_2$ (large subdomain at the coarse step, overlap neglected),
$S_{\mathrm{th}}=m\,(N_1/N_2+1)/(N_1/N_2+m)$, which tends to $m$ only when the refined
region is a vanishing fraction of the mesh. Measured speedups stay below these bounds:
random memory access (Unfer), data locality lost by partitioning
([Doehring et al. 2024b](/sources/doehring-2024-b.md), §7.1.1) and load imbalance
(Sreejith et al.) all cost.

## Leapfrog-based LTS for second-order wave equations

For $\ddot u=-Lu$ with $L$ the symmetric positive definite stiffness operator of a
mass-lumped conforming finite-element space (page-local reading of the registry $L$ for
this second-order problem), leapfrog, $u_{n+1}-2u_n+u_{n-1}=-H^2Lu_n$, is explicit,
second order, time-reversible, [symplectic](/properties/symplecticity.md) and conserves a
discrete energy; it is stable if the eigenvalues of $H^2L$ lie in $(0,4)$, as recalled by
Grote et al. (2021, §1, §4.1). The LF-LTS method of Diaz & Grote, as recalled there,
takes $m$ local leapfrog steps of size $H/m$ in the refined region and one step $H$
elsewhere, through the split $L=L\Pi_{\mathrm c}+L\Pi_{\mathrm f}$ with the coarse/fine
degree-of-freedom projections $\Pi_{\mathrm c},\Pi_{\mathrm f}$ (page-local). Grote, Mehlin &
Sauter proved its optimal convergence, but only under a CFL condition that depends on the
smallest elements, and in general LF-LTS can become unstable at isolated step sizes where
eigenvalue curves of the LTS operator become tangent to the stability bounds.

**Stabilized LF-LTS** (Grote et al. 2021, §2.4, eqs. 2.18–2.23). Rewriting the inner loop
with Chebyshev polynomials $T_m$ (page-local) and **damping** them as in
[Runge–Kutta–Chebyshev](/methods/stabilized-explicit-runge-kutta.md) methods gives

$$P_{m,\varepsilon_{\mathrm d}}(x)=2\Big(1-\frac{T_m(\delta-x/\omega)}{T_m(\delta)}\Big),\qquad \delta=1+\frac{\varepsilon_{\mathrm d}}{m^2},\qquad \omega=\frac{2T_m'(\delta)}{T_m(\delta)},$$

with damping parameter $\varepsilon_{\mathrm d}\in[0,\tfrac12]$ (page-local, as are $\delta$, $\omega$ and $x$;
the source's $\nu$, renamed because $\nu$ is the registry Courant number, and its $p$ for $m$). The scheme is
$u_{n+1}-2u_n+u_{n-1}=-H^2L_{m,\varepsilon_{\mathrm d}}u_n$ with
$L_{m,\varepsilon_{\mathrm d}}=L\,\frac{P_{m,\varepsilon_{\mathrm d}}(H^2\Pi_{\mathrm f}L)}{H^2\Pi_{\mathrm f}L}$
(a polynomial of degree $m-1$ in $\Pi_{\mathrm f}L$), realized by a three-term inner
recurrence with one application of $L\Pi_{\mathrm c}$ per global step and $m$ applications of
$L\Pi_{\mathrm f}$ restricted to the refined region and its neighbours. For
$\varepsilon_{\mathrm d}=0$ it is the original LF-LTS; for $m=1$ plain leapfrog; with
$\Pi_{\mathrm f}=I$ the (stabilized) leapfrog–Chebyshev method; away from the interface the
coarse region takes a plain leapfrog step. Carle & Hochbruck developed the same algorithm
independently. Under a CFL condition on $H/\Delta x_{\mathrm c}$ that involves **only the coarse
mesh width** $\Delta x_{\mathrm c}$ and is independent of $m$ (eq. 3.8), Grote et al. prove:

- **Thm. 3.5**: the stabilized operator is symmetric, continuous and coercive, with
  coercivity constant of order $\varepsilon_{\mathrm d}/m^2$;
- **Thm. 3.7**: $H^2\lambda_{\max}\le4-\varepsilon_{\mathrm d}/(\varepsilon_{\mathrm d}+1)$, so the
  spectrum stays strictly inside the leapfrog interval;
- **Cor. 3.8**: a modified discrete energy is non-negative and exactly conserved;
- **Thms. 3.9–3.11**: stability with constants independent of $n$, $H$, $\Delta x$ and the
  final time, and an $L^2$ error $\mathcal O(\Delta x^{k+1}+H^2)$ (FE degree $k$, page-local) with
  constants independent of $m$.

The proof deteriorates as $\varepsilon_{\mathrm d}\to0$; numerically a small fixed damping is
enough. In 1D tests the convergence is $\mathcal O(\Delta x_{\mathrm c}^2)$ for $m=2,5,17,1000$, the energy is
constant to about $10^{-13}$ over 30,000 steps, the maximal stable step is 99.7 % of the
optimal leapfrog step at $\varepsilon_{\mathrm d}=0.01$ (98.4 % at 0.05, 87.6 % at 0.5; Table 1),
and a critical eigenmode that grows linearly in time without damping stays bounded with
$\varepsilon_{\mathrm d}=0.01$ (§4.2, Fig. 7); on graded meshes of an L-shaped domain the method
recovers optimal $H^1$ and $L^2$ rates (§4.3).

## Asynchronous cell-level LTS

In Unfer's asynchronous framework (2021, §3.2) every cell of an unstructured
finite-volume mesh has its own step, scheduled on a discretized time grid. At each event
time the mesh splits into refreshed cells, their face neighbours and sleeping cells. Each
cell carries a **conservative** state, integrated whenever it or a neighbour is refreshed,
and an **extrapolated** state, updated only at its own refresh and used to evaluate
fluxes. The scheme is **conservative by construction**: whenever the flux on a face
changes, both adjacent cells are integrated up to that time, so no flux-correction
("flux capacitor", flux-memory) step is needed (§1). For the first-order centred variant
Unfer proves an invariant-domain property under a local CFL condition (Prop. 1), a
convex-combination stability argument, a TV bound, consistency and a cell entropy
inequality (§3.3; see [entropy stability](/properties/entropy-stability.md)), the last two
conditional on a **recall mechanism**: if the re-estimated local step drops below the
step in use, the cell is recalled and the event restarts. Without recall a shock cannot
enter a quiescent region whose local step is infinite (Burgers example, Eq. 78).

**Asynchronous Runge–Kutta.** Unfer's "ARK" means *asynchronous* Runge–Kutta, not
additive Runge–Kutta as elsewhere in this bundle ([IMEX RK](/methods/imex-runge-kutta.md)).
ARK2 evaluates each face flux at the midpoint of the interval over which that flux is
actually used; ARK3, the paper's contribution, is built on the Shu–Osher
[SSPRK(3,3)](/methods/strong-stability-preserving-runge-kutta.md) tableau, with parabolic
extrapolated states, cubic conservative states and three face-flux evaluations per face
interval, and reverts to SSPRK(3,3) under a global step (§3.5). A formal truncation
analysis gives $\mathcal O(\Delta x^3)$ in smooth regions (§3.5.3), but "there is no claim
… that the SSP property holds", and strong shocks need fallbacks to first order, previous
stage fluxes and per-stage recall. The time-continuous Taylor representations of cell
states play the part of a [dense output](/methods/dense-output.md).

## Overlapping-subdomain LTS

LESAULTS (Sreejith et al. 2022, §2–4) splits the mesh into **overlapping** subdomains,
each advanced by the unchanged explicit Lax–Wendroff or two-step Taylor–Galerkin (TTGC)
scheme with a step that divides a common macro step. During the substeps the interface
values of each subdomain are **frozen at $t_n$** as Dirichlet data; at $t_{n+1}$ the two
overlapping solutions are joined by a Heaviside-like switch inside the overlap (Eq. 4),
replacing the hyperbolic-tangent blending of the earlier Deccoup method of Esnault et al.
A global spectral analysis of the boundary-polluted amplification factor sizes the
overlap: the frozen-boundary error vanishes beyond $m+1$ nodes for Lax–Wendroff (three-point
stencil) and is negligible beyond about $2m+1$ for TTGC, giving overlaps of $m_1+m_2+1$ and
$2(m_1+m_2)+1$ cells. The error relative to the single-rate solver is the difference of
one large step and $m$ small steps of the same scheme; it stays below 1 % dissipation for
all wavenumbers up to a Courant number of 0.1 (LW) or 0.25 (TTGC) with $m=2$ (§5.2). The
method is "not strictly conservative" (§5.5). Spatial orders 2 and 3 are retained at
fixed Courant number (§5.4), which tests only the combined space–time error.

## LTS inside ADER-DG

[Wolf et al. (2022)](/sources/wolf-2022.md) use the clustered LTS of SeisSol, which groups
elements into time clusters for structured data access, together with a locally implicit
space–time predictor for a stiff poroelastic source (see
[ADER time integration](/methods/ader-time-integration.md)). The paper develops no LTS
algorithm or stability statement; it reports that LTS cuts time to solution by 6–10×
against global stepping on SuperMUC-NG, with parallel efficiency about 72.5 % from 25 to
400 nodes at order 7 and worse scaling than global stepping (§7.3).

**Global stepping on adaptive meshes, for contrast.**
[Babbar & Chandrashekar (2025)](/sources/babbar-2025.md) run single-stage
[Lax–Wendroff flux reconstruction](/methods/lax-wendroff-flux-reconstruction.md) on
dynamically refined curvilinear meshes with one global step for all elements, chosen by
error-based [step-size control](/methods/step-size-control.md) instead of a CFL formula
(§5–6). Their savings come from refinement, not from local steps: peak element counts of
13,957 against 262,144 for the equivalent uniform mesh on Kelvin–Helmholtz, 7,793 against
327,680 on the double Mach reflection, about 85,000 against 574,464 on a Mach 3 cylinder;
and from the controller, which needs 1.51–2.08 times fewer global steps than the best
hand-tuned CFL number on curved meshes (§6, Table 1). The step remains set by the most
restrictive element, which is the cost LTS removes; the paper does not compare with LTS.

## Multi-time-step partitioned coupling

[Pulicani et al. (2026)](/sources/pulicani-2026.md) subcycle across a fluid–structure
interface: an explicit finite-volume fluid (forward Euler or SSPRK(3,3), ALE) takes $m$
fine steps per step of an implicit [Newmark](/methods/newmark-method.md) structure, and a
Lagrange multiplier enforces continuity of the normal velocity at each fine step. In the
Gravouil–Combescure approach, as recalled there (§4), each subdomain's end-of-step
velocity splits into a "free" part (no interface force) and a "link" part linear in the
multiplier; the constraint becomes a small interface problem whose structural operator
is factored once. The coarse free structural velocity is interpolated linearly at fine
steps, and the fluid interface mesh is extrapolated from the corrected structural
kinematics. No sub-iteration over the coarse step is done. Energy-method results of
structural dynamics, as recalled (§1), guarantee multi-time-step stability for any
Newmark schemes when velocity (not displacement) continuity is imposed; for this
fluid–structure coupling stability is shown only numerically.

## Stabilized multirate for parabolic problems on refined meshes

For diffusion-dominated problems the explicit step is limited quadratically by the smallest
cell, and [Abdulle, Grote & Rosilho de Souza (2022)](/sources/abdulle-2022.md) attack the
same locally-refined-mesh setting without separate local steps. Their
[multirate RKC method](/methods/multirate-runge-kutta-chebyshev.md) splits the
semi-discrete right-hand side by a 0/1 selector of the degrees of freedom on and next to the
refined elements into a cheap stiff part $f^{\{\mathrm f\}}$ and an expensive mildly stiff
part $f^{\{\mathrm s\}}$; one global step of an outer
[RKC](/methods/stabilized-explicit-runge-kutta.md) scheme, with stages set by the coarse-mesh
spectral radius, sees the fast part only through an averaged force computed by a short inner
RKC run (§1, §3, §5.2). There is no interface treatment: the slow force is frozen at the
outer stage value, and no time interpolation or extrapolation of stage values is done, which
the authors contrast with interpolation-based multirate RKC on adaptive meshes, reported in
their own earlier work, as recalled there, to "cause numerical instabilities" (§1). The
method is first order with a proved stability condition on the scalar multirate test
equation (Thm. 4.5). On a heat problem through a narrow channel the speedup over RKC grows
as the channel narrows, up to about 40, and the solution differs from RKC's by at most
$3\cdot10^{-4}$ in relative $L^2$/$H^1$ norm (§5.3, Fig. 15).

## Interface treatment compared

| Approach | Interface coupling | Conservation | Order across the interface | Stability evidence |
|---|---|---|---|---|
| Stabilized LF-LTS (Grote et al. 2021) | polynomial in $\Pi_{\mathrm f}L$, one symmetric operator | exact modified energy | 2, proved, $m$-independent constants | proved, $m$-independent CFL |
| Asynchronous ARK3 (Unfer 2021) | face fluxes at face-event times from extrapolated states | by construction | 3, formal truncation analysis | local CFL + recall; first-order proofs only |
| LESAULTS (Sreejith et al. 2022) | interface frozen at $t_n$, overlap, Heaviside merge | not strict | not established in time | spectral analysis, LES runs |
| GC multi-time-step (Pulicani et al. 2026) | Lagrange multiplier on velocity at each fine step | controlled interface dissipation | observed ≈2 (fluid 1.41 in the coupled case) | numerical; stable to $m=300$ |
| mRKC (Abdulle et al. 2022) | none: right-hand-side split, slow force frozen per outer stage | not addressed | 1, proved (Thm. 4.6) | proved on the scalar test equation; coupled case numerical |
| P-ERK families (Doehring et al. 2024b) | shared stages, one global step | linear invariants, shared $b$ | design order observed | linear only; monotonicity lost |

The last two rows are not LTS in the strict sense. mRKC takes one global step and
differs from the fast-partition Runge–Kutta of
[multirate GARK](/methods/multirate-gark.md) in that the fast part is reached by an inner
stabilized run of length $\eta$ (page-local, not the registry entropy), not by micro steps
$H/m$. The
[paired explicit Runge–Kutta](/methods/paired-explicit-runge-kutta.md)
families take one global step and give each partition a different number of stage
evaluations, which the authors call "conceptually similar to local time-stepping" without
its interpolation, intermediate storage or flux exchange (Doehring et al. 2024b, §1). The
explicit multirate partitioned scheme MRK2 with buffer zones of Kang & Constantinescu is
on [multirate GARK](/methods/multirate-gark.md).

## Measured speedups

| Source | Setting | Step ratio or $A_s$ | Speedup |
|---|---|---|---|
| Unfer 2021 | 1D smooth wave on stretched mesh, 1 thread | $A_s\approx11$ | 6.0–7.5 vs SSPRK(3,3) |
| Unfer 2021 | 1D, uniform mesh | $A_s=1.1$ | 0.43–0.87 (slower) |
| Unfer 2021 | double Mach reflection, 3840×960 | $\langle A_s\rangle=4.6$ | 1.98; 36.5 with asynchronous AMR |
| Sreejith et al. 2022 | 2D vortex, $m=10$ | — | 1.92–2.21 (90–98 % of $S_{\mathrm{th}}$) |
| Sreejith et al. 2022 | cylinder LES, $Re=3900$, 720 cores, $m=5$ | — | 2.37 ($S_{\mathrm{th}}=2.57$) |
| Sreejith et al. 2022 | Sandia flame D LES, 360 cores, $m=4$ | — | 2.05 ($S_{\mathrm{th}}=2.28$) |
| Wolf et al. 2022 | poroelastic ADER-DG, SuperMUC-NG | — | 6–10 vs global stepping |
| Abdulle et al. 2022 | heat equation through a narrow channel, width $1/2^k$, $k\le15$ | — | up to ≈40 vs RKC (CPU time); 10–70 vs RKC2 at width $1/2^{12}$ |
| Pulicani et al. 2026 | piston–rod FSI | $m$ up to 300 | stability, not speed, reported |

In the multi-thread case Unfer's 1D speedup collapses (0.98 at $N=800$ on 8 threads)
because many time-step classes are sparsely populated (§4.1).

## Qualifications

- **Order statements are of different kinds.** Grote et al. prove a fully discrete error
  bound; Unfer's third order is a formal truncation analysis excluding recall and
  fallbacks; Sreejith et al. and Pulicani et al. measure at fixed Courant number, so
  spatial and temporal errors are not separated. Pulicani et al.'s "second order in time
  and space" with a third-order fluid integrator is the combined rate, and their
  stage-wise multiplier coupling of SSPRK(3,3) is not analysed for order.
- **Baselines.** Unfer's speedups are against the same code run synchronously with
  asynchronous data structures, not an optimized synchronous code; Sreejith et al.'s
  Table 4 case 4 and Table 7 print theoretical speedups that their own formula does not
  reproduce from the printed node counts (2.25 rather than 2.31 for case 4, whose counts
  repeat case 1, and 2.48 rather than 2.28 for Table 7) *(compiler check of their Eq. (1),
  not in the source)*.
- **Generalizations in the introductions.** Sreejith et al. state that multirate and AMR
  schemes are "often limited to structured block grids" (§1); the asynchronous and
  AMR-partitioned methods of Unfer and Doehring et al. run on unstructured and
  quad/octree meshes. Sreejith et al. also cite Knoth & Wolke and Sandu's MRI-GARK as
  "third-" and "fourth-order" LTS extensions, a loose attribution for methods that split
  the right-hand side rather than the mesh.
- **"Asynchronous" in other sources.** In [Goswami, Matthew & Aditya (2023)](/sources/goswami-2023.md)
  (§1, §4) "asynchronous" means halo data delayed between processes at a common step, not
  cell-wise local steps; see [low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md).
- Grote et al.'s §4.2 states the stability interval for $(H^2/4)L$ as $(0,4)$; with the
  scaling of §4.1 and Fig. 6 it is $(0,1)$ for $(H^2/4)L$, i.e. $(0,4)$ for $H^2L$.
- Unfer prints the ARK3 stage-3 extrapolation (Eq. 105) and the sentence describing it
  with different slopes (in the second-derivative term, $\tfrac12\Delta t_1^2+\Delta t_3^2-\Delta t_3\Delta t_1$
  printed against $\tfrac12\Delta t_1^2+(\Delta t_3-\Delta t_1)^2$ described, with the source's
  stage offsets $\Delta t_1$, $\Delta t_3$); they agree only when $\Delta t_1=0$, i.e. under a
  global step *(compiler check, not in the source)*.

# Citations

- [Grote et al. (2021)](/sources/grote-2021.md) — §1, §2.4 (eqs. 2.18–2.23, Remarks 2.6–2.7), §3 (eq. 3.8, Thms. 3.5–3.11, Cor. 3.8), §4 (Table 1, Figs. 3–10), App. B.
- [Unfer (2021)](/sources/unfer-2021.md) — §1, §3.1 (Eqs. 44–47), §3.2 (Eqs. 48–56), §3.3 (Prop. 1, Eqs. 68–100), §3.5 (Eqs. 101–118), §4 (tables, Figs. 5–20), Apps. A–C.
- [Sreejith et al. (2022)](/sources/sreejith-2022.md) — §1, §2 (Eq. 4), §3 (Eqs. 1–3), §4 (Figs. 7–8), §5 (Eqs. 23–33, Figs. 11–15), §6 (Tables 4–7).
- [Wolf et al. (2022)](/sources/wolf-2022.md) — §4.2, §7.3 (Fig. 15).
- [Doehring et al. (2024b)](/sources/doehring-2024-b.md) — §1, §7.1.1.
- [Pulicani et al. (2026)](/sources/pulicani-2026.md) — §1, §4.4 (Eqs. 56–60, Algorithm 3), §5.3–5.5 (Figs. 9–27), §6.
- [Abdulle, Grote & Rosilho de Souza (2022)](/sources/abdulle-2022.md) — §1, §3, §5.2–5.3 (Figs. 12–16), Thms. 4.5–4.6.
- [Babbar & Chandrashekar (2025)](/sources/babbar-2025.md) — §5–6 (global error-controlled step on adaptive meshes, element counts, Table 1).
- [Goswami, Matthew & Aditya (2023)](/sources/goswami-2023.md) — §1, §4 (meaning of "asynchronous").

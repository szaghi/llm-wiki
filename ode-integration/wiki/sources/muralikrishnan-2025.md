---
type: Source
title: "Muralikrishnan & Speck (2025) — Error Analysis and Parallel Scaling Study of a Parareal Parallel-in-Time Integration Algorithm for Particle-in-Fourier Schemes"
description: "Applies Parareal to particle-in-Fourier Vlasov–Poisson simulations with a lenient-tolerance particle-in-Fourier or a particle-in-cell coarse propagator, proves error bounds explicit in mesh size, particles per cell, NUFFT tolerance and coarse step, and reaches 2.4x to 5.8x speedups over spatial parallelization on 1536 GPUs."
resource: "doi:10.1137/24m1673097"
source_kind: paper
authors: [Muralikrishnan S., Speck R.]
year: 2025
venue: "SIAM J. Sci. Comput. S311-S336"
local_file: "/home/stefano/papers/mosaic/ode-integration/2025_Crossref_SIAM_Journal_on_Scientific_Computing_Muralikrishnan_Error_Analysis_and_Parallel_Scaling_Study_of_a_Parareal_Para.pdf"
tags: [parallel, parareal, kinetic, hpc, order-reduction]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper applies [Parareal](/methods/parareal.md) to particle-in-Fourier
(PIF) discretizations of the electrostatic
[Vlasov–Poisson](/benchmarks/vlasov-poisson-equation.md) system (3D-3V,
optionally with fixed external fields). PIF deposits particle charge
directly onto a truncated Fourier basis through nonuniform FFTs (NUFFT) of
tolerance $\mathrm{tol}$. It is aliasing-free and, before time
discretization, conserves charge, momentum and energy, but it is expensive
and scales poorly in space: every rank holds all modes and needs an
`MPI_Allreduce` over them. Coarse propagators built by spatial coarsening
are undefined for randomly placed particles or ineffective when high modes
matter, and temporal coarsening is limited for multiscale oscillatory
dynamics.

The contribution is the choice of coarse propagator: PIF with a lenient
NUFFT tolerance, or standard particle-in-cell (PIC, cloud-in-cell deposit
and FFT Poisson solve), each with or without temporal coarsening; the
correction acts on all particle positions and velocities. Writing PIF in
matrix form, the authors bound $\lVert\mathcal F-\mathcal G\rVert$ and insert it into
the Gander–Hairer superlinear Parareal bound. Theorems 5.2–5.3 make the
error explicit in mesh width, particles per cell, NUFFT tolerance and
coarse step.

Landau damping, two-stream instability and a Penning trap (IPPL with
cuFINUFFT on A100 GPUs) confirm the predicted scalings in particles per
cell, mesh width, tolerance and, for Landau damping with a PIF coarse
propagator, the coarse step. The Penning trap converges only like
$h_{\mathcal G}^{k}$ instead of $h_{\mathcal G}^{2k}$, a reduction of the
convergence rate the authors cannot explain (it is not the classical
[order reduction](/definitions/order-reduction.md) of Runge–Kutta methods).
Converged Parareal keeps the semi-discrete conservation
([symplecticity and invariants](/properties/symplecticity.md)) only at
near-machine-precision tolerances. The time stepper is the second-order
kick–drift–kick velocity Verlet or Boris scheme. A strong-scaling study to 1536
GPUs (32 in space × 48 in time) gives 4.2x, 4.7x and 2.4x speedups over
space-only parallelization with a linear shape function, and 5.8x, 5.6x and
4.4x with an order-7 B-spline. The Penning trap needs multi-block Parareal.
The paper sits within [parallel-in-time integration](/methods/parallel-in-time-integration.md).

# Version read

arXiv:2407.00485v2 [math.NA], stamped 15 June 2025, 26 pages, all read.
It thanks anonymous referees, so it is the post-review text, but it is not
the SIAM version of record; the archive filename says "Crossref_SIAM" but
the file is the arXiv typeset. Title and authors match Crossref. The file
prints no DOI, no volume, no journal page range and no journal header.
**Crossref gives the pages S311–S336 but no volume**, and the volume is
not guessed here, so the venue is recorded without one. The S pages point
to a special-section issue. Numbering is that of arXiv v2. Code:
https://github.com/srikrrish/ippl/tree/parapif-paper-v1.0.0.

# Key claims

Registry notation: propagators $\mathcal F$, $\mathcal G$ (source $F$, $G$),
slices $T_j$ of length $\Delta T$ (source index $n$), $N$ slices, iterate
$U^{(k)}_j$ (source $U^k_n$), fine step $h$ (source $\Delta t_f$), order $p$,
mesh width $\Delta x$ (source $h$), wave vector $\xi$ (source $k$). Page-local:
coarse step $h_{\mathcal G}$ (source $\Delta t_g$), particles per cell $P_c$,
NUFFT tolerance $\mathrm{tol}$ (source $\varepsilon$), B-spline order $m_S$,
particle-to-Fourier matrix $\mathsf P$ and Poisson symbol $\mathsf L$ (source
$P$, $L$), error $e^{(k)}_j$ against the time-exact PIF solution, initial
error $\delta$, and the Gander–Hairer constants $\alpha=\lVert\mathcal F-\mathcal G\rVert$,
$\beta=\lVert\mathcal G\rVert$.

1. Spatial coarsening of particles is undefined for PIF, and dropping
   Fourier modes is ineffective when high modes matter; temporal
   coarsening is limited for multiscale oscillatory problems (§1, §4).
   **Stated**
2. Using standard PIC as coarse propagator for structure-preserving PIF
   is "a non-standard and novel contribution" (§1). **Stated**
3. Lemma 5.1:
   $\lVert\mathsf P^H\mathsf L\mathsf P-\mathsf P_h^H\mathsf L\mathsf P_h\rVert\le\lVert\mathsf L\rVert\,\lVert\mathsf P-\mathsf P_h\rVert\,(\lVert\mathsf P\rVert+\lVert\mathsf P_h\rVert)$
   in any norm (§5.2, Eq. (5.4)). **Proved**
4. Theorem 5.2 (PIC coarse propagator, B-spline of order $m_S$, local
   truncation error $O(h_{\mathcal G}^{p+1})$, coarse Lipschitz constant
   $C_{\mathrm{pic}}$):
   $e^{(k)}_{j+1}\le\bar C^{\,j-k}\frac{(C_{\mathrm{grid}}\Delta x^{\min(m_S+1,2)}+C_{\mathrm{noise}}P_c^{-1/2}+C_{\mathrm{time}}\Delta T\,h_{\mathcal G}^p)^k}{k!}\prod_{i=1}^k(j+1-i)\,\delta$,
   $\bar C=\max(1,C_{\mathrm{pic}})$ (§5.4, Eq. (5.6)). **Proved** (relies on
   cited PIC error estimates and on the assertion, not proved, that
   $\lVert\mathsf L\rVert$, $\lVert\mathsf P\rVert$, $\lVert\mathsf P_h\rVert$ are bounded
   independently of grid and particle number)
5. Theorem 5.3 (PIF coarse propagator with NUFFT tolerance $\mathrm{tol}$):
   the same structure with $\lVert\mathcal F-\mathcal G\rVert\le C_{\mathrm{nufft}}\mathrm{tol}+C_{\mathrm{time}}\Delta T\,h_{\mathcal G}^p$,
   using $\lVert\mathsf P-\mathsf P_h\rVert=O(\mathrm{tol})$ from the NUFFT literature
   (§5.5, Eq. (5.13)). **Proved** (modulo the cited NUFFT estimate)
6. The underlying bound
   $e^{(k)}_{j+1}\le\bar\beta^{\,j-k}\frac{\alpha^k}{k!}\prod_{i=1}^k(j+1-i)\,\delta$,
   $\bar\beta=\max(1,\beta)$, is taken from Gander & Hairer (2008) and Gander,
   Lunet, Ruprecht & Speck (§5.4, Eq. (5.7)). **Stated**
7. Remark 5.4: PIF with NUDFT, or NUFFT at near-machine precision, is
   structure preserving; the converged Parareal solution is so only if the
   Parareal tolerance is also near machine precision; symmetric Parareal is
   left to future work (§5.5). **Stated**
8. With a second-order integrator ($p=2$), $\prod_{i=1}^k(j+1-i)\le j^k$ and
   $j\Delta T\le T$ give an expected $O(h_{\mathcal G}^{2k})$ convergence
   (§6.2.3). **Derived**
9. Landau damping, PIC coarse propagator, $32^3$ modes, $T=19.2$,
   $h=h_{\mathcal G}=0.05$: the error follows $O(P_c^{-k/2})$ for
   $P_c\in\{5,\dots,80\}$; velocity errors follow position errors slightly
   higher (Fig. 1). **Shown**
10. Penning trap, PIC coarse propagator, $P_c=10$,
    $\Delta x\in\{1.56,0.78,0.39,0.19\}$: the error follows $O(\Delta x^{2k})$ for
    early iterations and large $\Delta x$ and departs from it later because
    of noise; Landau damping and two-stream needed about 1000 particles per
    cell to see the grid error dominate (Fig. 2, §6.2.2). **Shown**
11. Penning trap, PIC coarse propagator, $64^3$ modes, $T=19.2$,
    $h=3.125\times10^{-3}$, $h_{\mathcal G}\in\{0.025,\dots,0.4\}$: the error does
    **not** follow $O(h_{\mathcal G}^{2k})$; convergence appears only at high $k$
    and small $h_{\mathcal G}$, with virtually no speedup on 16 slices. The
    authors attribute this to a large $C_{\mathrm{time}}$ from the fast
    modified cyclotron frequency 4.875 (period 1.29) (Fig. 3(a,b), §6.2.3).
    **Shown**
12. The same Penning trap with $T=1.2$ and a 16 times smaller fine step
    converges better but only as $O(h_{\mathcal G}^{k})$; the reason is unknown,
    further step reductions do not help, and a PIF coarse propagator
    behaves the same, so the reduced rate belongs to the test dynamics, not
    to the coarse propagator (Fig. 3(c,d)). **Shown**
13. Landau damping, $16^3$ modes, $P_c=640$, $h=3.125\times10^{-3}$: a PIF
    coarse propagator (tolerance $10^{-6}$ on both levels) shows
    $O(h_{\mathcal G}^{2k})$; a PIC coarse propagator is dominated by noise and
    shows no convergence in $h_{\mathcal G}$ (Fig. 4). Two-stream behaves the
    same. **Shown**
14. Landau damping, PIF coarse propagator, coarse tolerance
    $\mathrm{tol}\in\{10^{-1},\dots,10^{-7}\}$: the error follows $O(\mathrm{tol}^k)$;
    two-stream and the Penning trap are similar (Fig. 5). **Shown**
15. Parameter study: for larger fine steps and looser fine tolerances PIC,
    possibly with time coarsening, gives the least time to solution; for
    accurate runs PIF with a loose coarse tolerance is best when time
    coarsening is possible; with little time coarsening (Penning trap) PIC
    is best (§6.3, App. A.4). **Shown** (three mini-apps; the
    generalization is **Stated**)
16. App. A.4 ($64^3$ modes, $P_c=10$, $T=19.2$, 16 time-parallel GPUs):
    best speedups over the serial-in-time reference are 1.2, 1.2, 1.4 at
    $h=0.05$ and 2.0, 2.0, 1.1 at $h=0.003125$ for Landau damping, two-stream
    and Penning trap (Figs. 11–12). **Shown**
17. Multi-block Parareal (16 blocks) raises the Penning-trap speedup with a
    PIC coarse propagator from 1.1 to 1.5 at $h=0.003125$; for Landau and
    two-stream it helps PIC but does not beat the best PIF coarse
    propagator, and with a PIF coarse propagator it generally does not pay
    (App. A.5). **Shown**
18. With a PIC coarse propagator the energy error of the iterates is orders
    of magnitude larger and grows in early iterations, matching serial PIF
    only near convergence; momentum error stays near machine precision;
    charge conservation depends on the fine tolerance, energy on the fine
    and Parareal tolerances (Figs. 8–9, App. A.2). **Shown**
19. Fine NUFFT and Parareal tolerances are chosen ($10^{-7}$ and $10^{-8}$ at
    $h=0.003125$; $10^{-4}$ and $10^{-5}$ at $h=0.05$) so that energy and charge
    errors match serial stepping; mismatched tolerances give "bloated
    speedups" (App. A.2–A.3). **Shown**/**Stated**
20. Errors in later slices decrease about as fast as in early ones,
    consistent with Parareal as an approximate Newton method; each rank
    checks convergence locally and exits when its own criterion holds and
    the previous slice has converged, with no global reduction (Fig. 10,
    App. A.3). **Shown**
21. Time-parallel GPUs are added only once spatial efficiency drops below
    50%, since Parareal would need to converge in two iterations to reach
    50% efficiency (App. A.4). **Stated**
22. Strong scaling: $128^3$ modes, $P_c=10$ (20 971 520 particles),
    $h=0.003125$, $T=19.2$; 32 spatial GPUs times $\{2,4,8,16,32,48\}$
    temporal GPUs. Coarse propagators: PIF with tolerance $10^{-3}$ (Landau)
    or $10^{-4}$ (two-stream) and $h_{\mathcal G}=0.05$ on the whole interval; PIC
    with 16 blocks and $h_{\mathcal G}=0.0125$ (Penning) (§6.3, Fig. 6).
    **Shown**
23. Space–time parallelization does not pay off with 2 and 4 time GPUs,
    breaks even at 8 and gains from 16 on; at 1536 GPUs the speedups are 4.2
    (Landau), 4.7 (two-stream) and 2.4 (Penning) with a linear shape
    function (§6.3, Fig. 6). **Shown**
24. The `MPI_Allreduce` after the scatter dominates at many modes and many
    spatial GPUs; it costs the same on both levels without time
    coarsening, which explains the smaller Penning-trap speedup (§6.3).
    **Shown** (component timings, not plotted)
25. With an order-7 B-spline in the fine PIF (and, for the Penning trap, a
    PIC coarse propagator on a mesh of width $2\Delta x$ with $h_{\mathcal G}=0.003125$
    and 16 blocks) the speedups at 1536 GPUs are 5.8, 5.6 and 4.4, from
    lower noise (Landau, two-stream) and an eight times smaller coarse grid
    (Penning) (§6.3.1). **Shown**
26. The push rate is about $10^9$ particles per second at 1536 GPUs in all
    tests (§6.3.1, §7). **Shown**
27. For multiscale oscillatory problems (Penning trap) time coarsening
    gives large errors and many iterations and whole-interval Parareal
    converges very slowly, so it must run in blocks; overall speedups are
    about 4–6x (Landau, two-stream) and 2–4x (Penning) over spatial
    parallelization alone (§7). **Shown**
28. For Vlasov–Maxwell, with hyperbolic field equations, Parareal may be
    problematic; ParaExp or ParaDiag are suggested for the field part (§7).
    **Stated**

Speedups are measured against spatial parallelization alone (and in App.
A against serial-in-time runs on the same GPU count), not against the best
serial code.

# Printed slips

- Proof of Theorem 5.3 (p. 9): "$\|F-G\|\le C_{nufft}\varepsilon+C_{time}\Delta Tt_g^p$",
  missing $\Delta$ on $t_g$ (as in (5.13)).
- Eq. (5.3): $\frac{dv}{dt}=\frac{q_e}{m_e}(P^HLPq_e+v\times B_{ext})$ omits
  $E_{ext}$, although (2.5) and the Penning-trap test include it.
- (5.6) and (5.13) define $\delta=\max_{n=1,\dots,N}e^0_n$, reusing $N$
  (modes per dimension) for the number of slices. The iteration index $k$
  clashes with the wave vector $k$, $L$ is both the domain length and the
  Poisson-symbol matrix, and $\alpha$ is both the perturbation amplitude and
  $\lVert F-G\rVert$.
- Eq. (6.4) applies $G$ to the iterates ("$Gx_n^{k+1}-Gx_n^k$"), which reads
  as the coarse propagation of the iterates rather than the iterates
  themselves.
- §3: "the key step ... is to NUFFTs of type 1 and 2" (missing verb); §5.3
  "multiples it with"; §6.3 "it need to converge"; ref. [1]
  "Univerisität".

*(Compiler checks, not in the sources.)* The step from (5.9) to (5.10) treats $\lVert F-G\rVert$
as the right-hand-side difference without a Grönwall factor over $\Delta T$,
and that the unnormalized $P$ has an operator norm that grows with the
particle and mode counts unless a normalization is implied.

# Notation map

| Muralikrishnan & Speck (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $F$, $G$ | $\mathcal F$, $\mathcal G$ | **$F$ collides with the elementary differential $F(\tau)$** |
| $U^k_n$, $T_n$, $\Delta T$, $\Omega_n$ | $U^{(k)}_j$, $T_j$, $\Delta T$, $[T_j,T_{j+1}]$ | |
| $\Delta t_f$, $\Delta t_g$ | $h$, $h_{\mathcal G}$ (page-local) | fine and coarse steps; $n_g=\Delta T/h_{\mathcal G}$ |
| **$h$** | $\Delta x$ | mesh width; **$h$ is the registry step** |
| $p$ | $p$ | classical order of the time integrator |
| **$N$** | $N_x$ | modes per dimension; **collision with the slice count $N$** (also used for it in (5.6)) |
| $N_m$, $N_g$, $N_p$ | page-local | modes, grid points, particles |
| **$k$** (wave vector) | $\xi$ | **collision with the iteration index $k$** |
| **$P$**, $P_h$ | $\mathsf P$, $\mathsf P_h$ | particle-to-Fourier map and its coarse approximation |
| **$L$** (matrix), $L$ (length) | $\mathsf L$, domain length | Poisson symbol; **$L$ is the registry linear operator** |
| **$\varepsilon$** | $\mathrm{tol}$ | NUFFT tolerance; **collision with the stiffness parameter $\varepsilon$** |
| $\epsilon$ | $\mathrm{tol}_{\mathrm P}$ | Parareal stopping tolerance (6.4) |
| $u=\{x,v\}$ | $y$ | phase-space state of all particles |
| $e^k_{n+1}$, $\delta$ | $e^{(k)}_{j+1}$, $\delta$ (page-local) | error pair against time-exact PIF; initial error |
| **$\alpha$**, **$\beta$**, $\bar\beta$ | page-local | Gander–Hairer constants; **collisions with Shu–Osher $\alpha_{ij},\beta_{ij}$**; $\alpha$ is also the perturbation amplitude in §6.1 |
| $C_{pic}$, $C_{pif}$, $C_{grid}$, $C_{noise}$, $C_{time}$, $C_{nufft}$, **$\gamma$** | page-local | error constants; **$\gamma$ collides with the tree density** |
| **$m$** | $m_S$ | B-spline order; **$m$ is the registry multirate ratio** |
| $P_c=N_p/N_g$ | $P_c$ | particles per cell or mode |
| $\omega_+$, $\omega_z$, $\omega_-$ | — | Penning-trap frequencies |

# Reference list

The paper prints 57 references in numbered style (SIAM, alphabetical,
titles printed, no DOIs). All are merged complete into the
[bibliography](/bibliography.md) with `citedby` muralikrishnan-2025. Ref.
[14], the Parallel-in-time community webpage, prints the corporate author
as "P. Community" and no date; it is keyed with the citing year. Ref. [21]
is a software release without venue, [25] (ParaDiag) and [57] are arXiv
preprints, and [49] is a book chapter without editors or publisher. Ref.
[32] prints "X. Jianyuan" (given name and surname as printed) and [48] "M.
C. Pinto", keyed as printed (`pinto-2022`) and not merged with the
`campospinto-*` entries. `kraus-2017` and `kraus-2017-b` take printed-order
suffixes.

# Pages created or updated

Chunk 5 (2026-10-20). This source is cited on:

* [Order reduction](/definitions/order-reduction.md)
* [Parallel-in-time integration](/methods/parallel-in-time-integration.md)
* [Parareal](/methods/parareal.md)
* [Symplecticity and quadratic-invariant preservation](/properties/symplecticity.md)
* [Vlasov–Poisson equation (Landau damping, two-stream instability)](/benchmarks/vlasov-poisson-equation.md)

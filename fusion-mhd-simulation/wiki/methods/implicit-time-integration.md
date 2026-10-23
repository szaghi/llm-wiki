---
type: Method
title: "Implicit time integration and preconditioned Krylov solvers for nonlinear MHD"
description: "The linearized three-level theta/xi scheme of JOREK (Crank–Nicolson, BDF2, implicit Euler) solved each step by restarted GMRES with a block-Jacobi preconditioner over toroidal harmonics whose blocks are LU-factorized and reused, set against the split-implicit, leapfrog, backward-Euler, Newton–Krylov, BDF (CVODE) and explicit Runge–Kutta advances of the other codes; includes the variable-step order condition and the BDF2-versus-BDF5 printed slip (closed by fiat)."
status: established
aliases: [theta-xi scheme, Gear scheme, BDF2, Crank–Nicolson, linearized implicit scheme, block-Jacobi preconditioner, toroidal-harmonic preconditioner, mode groups]
tags: [time-integration, linear-solver, numerics]
timestamp: 2026-10-16T18:35:00Z
---

# Implicit time integration and preconditioned Krylov solvers for nonlinear MHD

Resistive MHD in fusion plasmas spans the Alfvén and fast-wave time scales,
the resistive time and the transport time; an implicit advance removes the
explicit stability limit of the fastest waves and lets the step follow the
physics of interest. In [JOREK](/software/jorek.md) every variable is advanced
fully implicitly with a linearized multistep scheme, and the resulting sparse
system is solved by a preconditioned Krylov method
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §3.2, §3.4–3.5, App. C).

## The θ/ξ scheme

Write the semi-discrete system as $\partial_t\mathcal M(\mathbf u)=\mathcal F(\mathbf u,t)$,
with $\mathcal M$ the (possibly nonlinear) quantity whose time derivative
appears and $\mathcal F$ the spatial operator and sources, and index time
levels by $k$. The general three-level scheme is
$$(1+\xi_{\mathrm t})\,\mathcal M^{k+1}-(1+2\xi_{\mathrm t})\,\mathcal M^{k}+\xi_{\mathrm t}\,\mathcal M^{k-1}=\Delta t\Big[\theta_{\mathrm t}\mathcal F^{k+1}+(1-\theta_{\mathrm t}-\phi_{\mathrm t})\mathcal F^{k}-\phi_{\mathrm t}\mathcal F^{k-1}\Big],$$
second-order accurate if $\theta_{\mathrm t}+\phi_{\mathrm t}-\xi_{\mathrm t}=\tfrac12$
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), App. C, Eq. 62; the
condition was checked by the compiler with $\mathcal M=t^2/2$,
$\mathcal F=t$). With $\phi_{\mathrm t}=0$ the named members are
Crank–Nicolson $(\theta_{\mathrm t},\xi_{\mathrm t})=(\tfrac12,0)$, the Gear
scheme BDF2 $(1,\tfrac12)$ and implicit Euler $(1,0)$, the last not used in
production (§3.2).

**Linearization.** Expanding $\mathcal M^{k+1}-\mathcal M^{k}\approx\mathcal J_{\mathcal M}^{k}\,\delta\mathbf u^{k}$
and $\mathcal F^{k+1}\approx\mathcal F^{k}+\mathcal L^{k}\delta\mathbf u^{k}$, with
$\delta\mathbf u^{k}=\mathbf u^{k+1}-\mathbf u^{k}$,
$\mathcal J_{\mathcal M}=\partial\mathcal M/\partial\mathbf u$ and
$\mathcal L=\partial\mathcal F/\partial\mathbf u$, gives one linear system per
step,
$$\Big[(1+\xi_{\mathrm t})\,\mathcal J_{\mathcal M}^{k}-\Delta t\,\theta_{\mathrm t}\,\mathcal L^{k}\Big]\delta\mathbf u^{k}=\Delta t\,\mathcal F^{k}+\xi_{\mathrm t}\,\mathcal J_{\mathcal M}^{k}\,\delta\mathbf u^{k-1}$$
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eqs. 56, 64). The
definition equations of the auxiliary variables (toroidal current and
vorticity) are imposed at $t^{k+1}$ (§3.2). Newton iterations were tested:
they allow larger steps, but their cost and memory gave limited net benefit
and they are not in the code (§3.2). [Bhole et al. (2023)](/sources/bhole-2023.md)
(§3.3.5, Eq. 40) describe the same advance as one Newton iteration with an
approximate Jacobian, with the time-derivative operator evaluated with the
mass-matrix coefficients at $\mathbf u^{k}$, and treat their
[VMS](/methods/variational-multiscale-stabilization.md) and
[shock-capturing](/methods/shock-capturing-artificial-viscosity.md) terms
with the same $\theta_{\mathrm t}$-weighting.

**Variable time step.** Bhole et al. write the scheme for a step ratio
$r=\Delta t_{k-1}/\Delta t_k$:
$$\frac{(1+r\xi_{\mathrm t})\mathbf u^{k+1}-\big(1+\xi_{\mathrm t}(1+r)\big)\mathbf u^{k}+\xi_{\mathrm t}\mathbf u^{k-1}}{\Delta t_k}=\theta_{\mathrm t}\mathcal F^{k+1}+(1-\theta_{\mathrm t})\mathcal F^{k}$$
(Eq. 40, citing Beam and Warming). The scheme is consistent for every $r$, but
with $\theta_{\mathrm t}=1$ it is second order only if
$\xi_{\mathrm t}=1/[r(1+r)]$, which reduces to $\tfrac12$ at $r=1$ (reader's
check, re-derived by the compiler). The paper does not say whether
$\xi_{\mathrm t}$ is adapted when $\Delta t$ changes, and its 3D runs change
$\Delta t$ repeatedly between 0.1 and 5 normalized units (§4.3.1).

## Linear solver and preconditioner

- **Matrix.** The global sparse matrix (about one non-zero in several
  thousand entries) is assembled with distributed domain decomposition; element
  matrices use Gauss quadrature in the poloidal plane and direct summation or
  an FFT toroidally. Matrix-free assembly was tested and rejected because the
  preconditioner dominates memory anyway
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §3.4).
- **Axisymmetric runs** are solved directly (PaStiX mostly, MUMPS, WSMP,
  STRUMPACK; PT-Scotch or ParMETIS ordering; low-rank compression only tested)
  (§3.5).
- **3D runs** use restarted GMRES on the distributed global matrix (§3.5);
  BiCGSTAB was added later ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md),
  §5).
- **Physics-based preconditioner.** Linear eigenfunctions of an axisymmetric
  equilibrium are single-$n$, so only the diagonal blocks of the matrix
  ordered by toroidal harmonic are kept: a block-Jacobi preconditioner in
  toroidal harmonics, each block LU-factorized by a direct solver on one or
  more MPI tasks ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §3.5). The
  symbolic analysis runs once; the factorization is done at the first step and
  repeated only when the GMRES iteration count exceeds a threshold, so
  factors are reused over many steps in linear phases, while in strongly
  non-linear phases re-factorization happens almost every step and dominates
  the cost. "Mode groups" form multi-harmonic, possibly overlapping blocks to
  capture strong coupling; complex-arithmetic block solves reduce memory and
  cost. The stated limitations are preconditioner memory, direct-solver
  scalability and degradation under strong mode coupling (§3.5). A later
  preconditioner retains selected non-linear couplings between harmonics and
  speeds up convergence, and a spectral analysis of original and
  preconditioned systems was made
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §5). For 3D JOREK–STARWALL runs of runaway-electron beam termination in DEMO,
  [Vannini et al. (2025)](/sources/vannini-2025.md) (§5) state that without
  the enhanced preconditioner of Holod et al. (2021, not ingested) "the
  simulation results here presented would not have been possible"; they give
  no time step, resolution or cost.
- **Mode groups in stellarators.** In JOREK3D the mode-group preconditioner
  couples adjacent harmonics of the same toroidal mode family; it "has been
  important for making simulations computationally manageable", and in more
  optimized configurations the coupling stays strong into the second and
  third sidebands, so stellarator runs remain costlier than tokamak runs
  ([Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §2.4).
- **NIMROD's direct-solver preconditioner.** In a two-fluid DIII-D QH-mode
  run of [NIMROD](/software/nimrod.md) the algebraic systems of the
  [semi-implicit leapfrog](/methods/semi-implicit-leapfrog.md) are
  preconditioned with the SuperLU_DIST direct solver: per toroidal Fourier
  mode (summed over the physical quantities) 34 GB of memory, 9 s of
  factorization and 340 ms per application on 64 Perlmutter CPU cores, about
  $340\ \mathrm{ms}\times22\approx7.5$ s of application per Krylov iteration
  for 22 modes ([Rahman et al. (2024)](/sources/rahman-2024.md), §II B,
  §III A 1). The same paper proposes, without testing, a
  [Fourier-neural-operator surrogate](/methods/fourier-neural-operator-surrogates.md)
  prediction (about 280 MB, about 1 s for the 44 planes of 22 modes) as an
  inexpensive initial guess or preconditioner of the Krylov iteration, and
  quotes "120× memory reduction" against SuperLU_DIST; the comparison sets an
  approximate surrogate of $\sim10^{-2}$ relative error against an exact
  factorization, and the surrogate is never placed in the solver (§III A 1,
  §IV; reader's note).
- **A failure mode of block-Jacobi.** In M3D-C1 the runaway-electron
  continuity equation, convected along $\mathbf b$ at a speed far above
  $v_A$, puts its toroidal derivative into off-diagonal blocks that "can
  dominate the matrix" at Alfvénic steps, so GMRES with the per-plane
  block-Jacobi preconditioner is ill-conditioned. Liu et al. replace that
  equation by a method of characteristics outside the implicit system
  ([Liu et al. (2021)](/sources/liu-2021.md), §3).
- **Parallel layout.** The number of MPI tasks is a multiple of the number of
  harmonics; rank 0 carries I/O and the $n=0$ block; the ELM case of JT-60SA
  reaches about 50% strong-scaling efficiency from 16 to 160 nodes
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §3.6, Figs. 9–10).
- **Conditioning and dissipation.** At low resistivity the JOREK3D tearing
  runs needed a hyperresistivity $\eta_h$ for solver convergence, changing the
  growth rate by less than 1.5% where tested
  ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §VI). Stabilization
  terms raise the GMRES cost per solve but permit larger steps
  ([Bhole et al. (2023)](/sources/bhole-2023.md), Table 1).

## Practice in the corpus

| Code / study | Advance | Step | Source |
|---|---|---|---|
| JOREK, NSTX VDE benchmark | Crank–Nicolson or Gear | 5–10 $\tau_A$ (2D phase), 0.1–0.2 $\tau_A$ (3D phase) | [Artola et al. (2021)](/sources/artola-2021.md), §2–3 |
| JOREK, divertor neutrals | BDF2 | $2.246\times10^{-6}$ s fluid; $2\times10^{-8}$ s kinetic neutrals | [Korving et al. (2023)](/sources/korving-2023.md), §II C, §V D, §V F |
| JOREK3D, W7-A | implicit Euler to damp start-up transients, then Crank–Nicolson | e.g. $1.621\times10^{-2}$ ms (tearing) | [Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §V–VI |
| [M3D-C1](/software/m3d-c1.md) | split-implicit: velocity, then field, then pressure(s), then density | 0.5 $\tau_A$, halved to 0.25 $\tau_A$ in the most dynamic interval | [Artola et al. (2021)](/sources/artola-2021.md), §2–3 |
| M3D-C1 | $\theta$-implicit | 1.0 $\tau_A$ | [Zhang et al. (2021)](/sources/zhang-2021.md), §2 |
| M3D-C1 | split-implicit, steps beyond the Alfvénic scale for transport-time runs | — | [Saxena et al. (2025)](/sources/saxena-2025.md), code description |
| [NIMROD](/software/nimrod.md) | [semi-implicit leapfrog](/methods/semi-implicit-leapfrog.md) | flow-CFL adapted | [Artola et al. (2021)](/sources/artola-2021.md), §2–3 |
| NIMROD, DIII-D QH-mode, two-fluid with C and D ions | mixed implicit/semi-implicit leapfrog, SuperLU_DIST-preconditioned solves | $5\times10^{-9}$ s (compressional-Alfvén CFL ≈800, flow CFL ≈2), ≈7 s per step on 11 CPU nodes | [Rahman et al. (2024)](/sources/rahman-2024.md), §II B, §III A |
| JOREK, AUG flux pumping | "implicit Gear scheme", order not stated | $2.30\times10^{-3}$ ms on a $100\times100$ polar grid | [Zhang et al. (2025)](/sources/zhang-2025.md), §2.4 |
| JOREK, AUG SPI | JOREK's standard implicit scheme (by citation, not described) | 0.1 normalized units ($\approx6.1\times10^{-8}$ s), raised gradually to 1–2 units ($\approx0.61$ µs each) in the CQ | [Tang et al. (2025)](/sources/tang-2025.md), §3.1 |
| JOREK, AUG EDA H-mode | implicit (scheme not restated) | one JOREK time unit, $\sqrt{\mu_0\rho_0}=0.6687\,\mu$s, halved at times in the nonlinear phase "to improve convergence of the iterative solver" | [Cathey et al. (2023)](/sources/cathey-2023.md), §2.2 |
| M3D-C1 with runaway electrons | split $\theta$-implicit (momentum, then plasma and RE densities, then field and pressure), GMRES with block-Jacobi; RE density by characteristics with subcycles | 0.65 µs (benchmark) | [Liu et al. (2021)](/sources/liu-2021.md), §2–3 |
| MIPS and MEGA (kinetic thermal ions) | explicit RK4 for fluid and particles, finite differences | not stated | [Sato et al. (2024)](/sources/sato-2024.md), §2 |
| [CLT](/software/clt.md) | explicit RK4 | $\approx8.5\times10^{-3}\,\tau_A$ | [Zhang et al. (2021)](/sources/zhang-2021.md), §2 |
| [GMEC](/software/gmec.md) | explicit RK4; resistive and numerical-diffusion terms implicit | 0.05–0.2 $R_0/v_A$ | [Jiang et al. (2024)](/sources/jiang-2024.md), §IV D, §IX |
| [BOUT++](/software/bout-plus-plus.md) | BDF through CVODE (SUNDIALS) | — | [Seto et al. (2023)](/sources/seto-2023.md), §2 |
| [HYMAGYC](/software/hymagyc.md) | fully implicit backward Euler (linear MHD) | — | [Vlad et al. (2025)](/sources/vlad-2025.md), §3 |
| [XTOR-K](/software/xtor-k.md) | preconditioned Newton–Krylov for the fluid, Boris ions, Picard iteration to joint convergence | 16 particle steps per fluid step | [Vlad et al. (2025)](/sources/vlad-2025.md), §6 |

The CLT–M3D-C1 pair shows the cost of explicitness: the same tearing and kink
cases run with about 120 times smaller steps in the explicit code
([Zhang et al. (2021)](/sources/zhang-2021.md), §2;
[benchmark](/benchmarks/clt-m3d-c1-benchmark.md)). Kinetic and source terms
are often left explicit inside an otherwise implicit fluid advance:
energetic-particle moments averaged over an MHD step
([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §II), runaway-electron
sources ([Bandaru et al. (2024)](/sources/bandaru-2024.md), §II A) and
kinetic-neutral sources, applied once per fluid step but multiplying implicit
terms "to maintain the highest order accuracy"
([Korving et al. (2023)](/sources/korving-2023.md), §IV C). The
[atomic-source splitting](/methods/operator-splitting-of-atomic-sources.md)
page treats the alternative.

Implicitness does not lift the cost of resolving the physics. In ITER
pedestal runs the "small Alfven-like time steps needed … even with a fully
implicit scheme" restrict the simulated time to a few tens of ms, against an
energy confinement time above 3 s
([Becoulet et al. (2022)](/sources/becoulet-2022.md), §7). Cathey et al.
(2023, §2.2) add that the MHD model itself requires mode frequencies far
below the ion cyclotron frequency, so a step much shorter than one JOREK
time unit would not make faster physics valid.

## Qualifications

- **Energy conservation.** BDF2 "does not conserve energy exactly"; the
  steady-state power balance of a divertor case closes to $10^{-3}$–$10^{-2}$
  ([Korving et al. (2023)](/sources/korving-2023.md), §V F, Eq. 32). In
  [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) the finite time step is
  one of the listed sources of energy-balance error (§2.3.3, §4.3).
- **Notation clash at the source.** App. C of Hoelzl et al. uses the toroidal
  angle symbol for the third time weight, written $\phi_{\mathrm t}$ here
  (reader's note).

## Contradictions

**Order of JOREK's Gear scheme — Closed by human fiat (2026-10-16) as a
printed slip.** [Artola et al. (2021)](/sources/artola-2021.md) (arXiv v1,
§2 and Table 1) state that JOREK uses "typically the Crank-Nicolson or the
BDF5 Gears scheme". [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§3.2,
App. C), [Bhole et al. (2023)](/sources/bhole-2023.md) (Eq. 40, Gear = BDF2
at $\xi_{\mathrm t}=\tfrac12$) and [Korving et al. (2023)](/sources/korving-2023.md)
(§II C, §V F) describe the Gear scheme as BDF2, and the three-level form of
Eq. 62 cannot represent a five-step method. Checking the published version of
Artola et al. (Phys. Plasmas 28:052511), or a fiat closure by the human, would
settle it. [Zhang et al. (2025)](/sources/zhang-2025.md) (§2.4) call the
JOREK advance an "implicit Gear scheme" without giving its order, so it does
not bear on the slip.

* **Closed by human fiat (2026-10-16): JOREK's Gear scheme is BDF2.** The
  "BDF5" of Artola et al. (2021, arXiv v1) is a printed slip; the published
  version was not checked.
  *Fiat closure — `status: hypothesis` attribution: the closure is the
  human's judgment, not a source superseding a source; a later source can
  reopen it.*

# Citations

- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §3.2, §3.4–3.6, App. C.
- [Bhole et al. (2023)](/sources/bhole-2023.md) — Eq. 40, Table 1.
- [Korving et al. (2023)](/sources/korving-2023.md) — §II C, §IV C, §V D–F.
- [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — §V–VI.
- [Artola et al. (2021)](/sources/artola-2021.md) — §2–3, Table 1.
- [Zhang et al. (2021)](/sources/zhang-2021.md) — §2.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §5.
- [Seto et al. (2023)](/sources/seto-2023.md) — §2.
- [Saxena et al. (2025)](/sources/saxena-2025.md) — code description (M3D-C1).
- [Jiang et al. (2024)](/sources/jiang-2024.md) — §IV D, §IX.
- [Vlad et al. (2025)](/sources/vlad-2025.md) — §3, §6.
- [Bogaarts et al. (2022)](/sources/bogaarts-2022.md) — §II.
- [Bandaru et al. (2024)](/sources/bandaru-2024.md) — §II A.
- [Becoulet et al. (2022)](/sources/becoulet-2022.md) — §7.
- [Cathey et al. (2023)](/sources/cathey-2023.md) — §2.2.
- [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) — §2.4.
- [Liu et al. (2021)](/sources/liu-2021.md) — §2–3.
- [Sato et al. (2024)](/sources/sato-2024.md) — §2.
- [Rahman et al. (2024)](/sources/rahman-2024.md) — §II B, §III A 1, §IV.
- [Zhang et al. (2025)](/sources/zhang-2025.md) — §2.4.
- [Tang et al. (2025)](/sources/tang-2025.md) — §3.1.
- [Vannini et al. (2025)](/sources/vannini-2025.md) — §5.

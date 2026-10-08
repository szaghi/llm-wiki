---
type: Source
title: "Christlieb, Feng, Seal & Tang (2016) — A high-order positivity-preserving single-stage single-step method for ideal MHD"
description: "Single-stage single-step (Picard-integral Lax-Wendroff) FD-WENO for MHD with unstaggered potential-based CT and a positivity flux limiter whose guarantee rests on an LF-positivity conjecture later refuted by Wu (2018)."
resource: "doi:10.1016/j.jcp.2016.04.016"
source_kind: paper
authors: [Christlieb A.J., Feng X., Seal D.C., Tang Q.]
year: 2016
venue: "J. Comput. Phys. 316:218-242"
local_file: "~/papers/mosaic/div-free-amr/2016-JCP-Christlieb-101016jjcp201604016.pdf"
tags: [vector-potential, constrained-transport, positivity, weno, finite-difference, lax-wendroff, high-order, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The paper is the single-stage, single-step successor of
[Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md):
* The fluid is advanced by the Taylor-discretized Picard-integral WENO
  (PIF-WENO) scheme. Time-averaged fluxes are expanded to third order by
  Cauchy–Kovalevskaya, then WENO-reconstructed, which needs one
  reconstruction per step.
* The potential is advanced alongside it, in the Weyl gauge, by a
  Lax–Wendroff Hamilton–Jacobi WENO scheme.
* $B$ is reset each step to the fourth-order central curl of the
  potential, as in Rossmanith's unstaggered CT.
* A parametrized flux limiter, a convex combination with the
  Lax–Friedrichs flux, enforces density and pressure positivity on demand.

The stated motive for avoiding Runge–Kutta stages is AMR.

It is merged into
[vector-potential evolution](/methods/vector-potential-evolution.md),
[positivity–divergence coupling](/results/positivity-divergence-coupling.md)
(including a closed `Contradictions` entry) and
[exact discrete divergence](/properties/exact-discrete-divergence.md).

# Key claims

1. **Why single-stage** (§1). High-order multistage RK on AMR needs ghost
   values at intermediate stages, which high-order time interpolation at
   ghost points cannot supply to high order. A single-stage, single-step
   method needs fewer synchronizations, and its Taylor form stores less.
2. **The CT step** (§2). Update the conserved variables, update the
   potential, then set $B^{n+1} = \nabla\times A$. That reset changes the
   pressure. When the positivity limiter is on, the total energy is
   adjusted to keep the pressure unchanged (eq. 13), which gives up energy
   conservation.
3. **The potential update** (§4).
   * In 2D only $A_z$ is evolved, a strongly hyperbolic Hamilton–Jacobi
     equation. The first time derivative uses a global-LF numerical
     Hamiltonian on WENO5 one-sided derivatives. Higher derivatives are
     converted by Cauchy–Kovalevskaya (49 distinct spatial derivatives)
     and taken by central differences.
   * $B$ is the fourth-order central curl (eq. 38).
   * The stencil is 11 points wide, against 15 for the Qiu
     Lax–Wendroff-HJ approach the scheme builds on.
   * In 3D the weakly hyperbolic system gets the smoothness-switched
     artificial resistivity of the 2014 paper. Here $\nu \approx 0.01$
     suffices.
4. **The positivity limiter** (§5). Each face flux becomes
   $\theta(\hat F - \hat f^{\mathrm{LF}}) + \hat f^{\mathrm{LF}}$, with
   $\theta$ chosen by a two-step box-shrinking search: a linear density
   constraint, then a concave pressure constraint with 10 bisection steps.
   Its guarantee rests on **Claim 1**, conjectured by Cheng et al. (2013):
   at CFL $\le 0.5$ the LF update of admissible data is admissible. The
   authors state it is unproven and verified only on random states.
5. **Results** (§6).
   * Fourth order in space and third in time on the 2D and 3D smooth
     Alfvén waves, with or without the energy adjustment.
   * Rotated shock tube: without CT, oscillations in the field.
   * Orszag–Tang: without CT the run crashes at $t = 1.67$.
   * The limiter is needed for the rotor, the 2D and 3D blasts (negative
     pressure at the first or second step otherwise) and the 3D
     cloud–shock at $256^3$.
   * The energy error stays below 1% except on the coarsest meshes, grows
     linearly in time and decreases with refinement. Without the limiter,
     energy is conserved to round-off.

# Notation map

| Christlieb et al. (2016) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $A$, $A^z$ (collocated) | collocated potential | not the edge $A_h \in V_h^1$ |
| $B = \nabla\times A$ (eq. 38, fourth-order central) | $B_h = C_h^{\mathrm{c}} A$ | fourth-order central curl |
| discrete divergence-free condition | $D_h^{\mathrm{c}} B_h = 0$ with the matching fourth-order central divergence | not the second-order one of Wu 2018 |
| $\hat f$, $\hat g$ (eq. 50) | first-order Lax–Friedrichs flux | |
| $\theta_{i+1/2,j}$ | limiter parameter | |
| $\mathcal{G}$-type admissibility ($\rho > \epsilon_\rho$, $p > \epsilon_p$) | $\mathcal{G}$ | |

# Pages created or updated

* Updated [Vector-potential evolution](/methods/vector-potential-evolution.md): the single-stage, single-step variant.
* Updated [Positivity–divergence coupling](/results/positivity-divergence-coupling.md): the energy adjustment after the curl reset, and a closed `Contradictions` entry (Claim 1 against Wu 2018, Theorem 4.1).
* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md): the published AMR stage-coupling motive.

# Citations

1. `~/papers/mosaic/div-free-amr/2016-JCP-Christlieb-101016jjcp201604016.pdf` (doi:10.1016/j.jcp.2016.04.016): text extraction, all pages including the reference list (63 entries). The Cauchy–Kovalevskaya expansions (eqs. 30–37) and the limiter's box-shrinking algorithm (§5, after eq. 55) were read in outline, and no equation from them is reproduced. Figures were read from their captions only.

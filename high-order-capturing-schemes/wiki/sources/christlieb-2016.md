---
type: Source
title: "Christlieb, Feng, Seal & Tang (2016) — A high-order positivity-preserving single-stage single-step method for the ideal magnetohydrodynamic equations"
description: "Single-stage single-step FD-WENO for ideal MHD: Picard-integral (Taylor) time stepping of fluxes, unstaggered vector-potential constrained transport evolved with a Lax–Wendroff Hamilton–Jacobi WENO scheme, and a parameterized positivity flux limiter."
resource: "doi:10.1016/j.jcp.2016.04.016"
source_kind: paper
authors: [Christlieb A.J., Feng X., Seal D.C., Tang Q.]
year: 2016
venue: "J. Comput. Phys. 316:218-242"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2016-JCP-Christlieb-101016jjcp201604016.pdf"
tags: [mhd, finite-difference, weno, constrained-transport, positivity, single-step]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

A storage-lean, AMR-friendly alternative to SSP-RK FD-WENO for MHD,
which keeps both a discrete divergence-free field and positivity.
Merged into the new [Taylor time discretization](/methods/taylor-time-discretization.md),
[constrained transport](/methods/constrained-transport.md) and
[flux limiter](/methods/positivity-preserving-flux-limiter.md) pages. It
opens a `Contradictions` entry on
[positivity preservation](/properties/positivity-preserving.md) about
the first-order Lax–Friedrichs MHD scheme.

# Key claims

1. **Why single-step** (§1): multistage RK complicates AMR ghost values
   and synchronization; among Lax–Wendroff-type families only ADER had
   been applied to MHD.
2. **PIF-WENO** (§3): WENO reconstruction of time-averaged fluxes from a
   third-order Taylor/Cauchy–Kowalewski expansion; one reconstruction
   per step.
3. **Unstaggered CT** (§§2, 4): Weyl-gauge vector potential on the cell
   mesh; in 2D, $A_z$ obeys a strongly hyperbolic HJ equation solved by a
   Lax–Wendroff WENO scheme (LF Hamiltonian, central differences for
   higher time derivatives, 11-point stencil, nothing stored); in 3D,
   artificial resistivity ($\nu \approx 0.01$) for weak hyperbolicity;
   fourth-order curl.
4. **Positivity** (§5): the LF update's positivity under CFL $\le 0.5$ is
   conjectured (Cheng et al.) but unproven (Claim 1). Flux blending with
   four interface factors in convex admissible sets (Claim 2), plus an
   energy correction that breaks energy conservation where active.
5. **Tests** (§6, CFL 0.5): smooth Alfvén wave (fourth order in space,
   third in time); rotated shock tube (CT removes oscillations);
   Orszag–Tang (crashes at $t = 1.67$ without CT); low-β rotor and blast
   waves (limiter required); 2D and 3D cloud–shock; energy errors below
   1%, linear in time, decreasing with resolution.

# Notation map

| Christlieb et al. (2016) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $q = (\rho, \rho\mathbf u, \mathcal E, \mathbf B)$ | $u$ | $\mathbf u$ is the velocity $\mathbf v$; $\mathcal E$ the energy $E$ |
| $\mathbf A$ | $\mathbf A$ | |
| $F^n$, $G^n$ (time-averaged fluxes) | $\mathcal{F}^n$ | |
| $\hat{\mathbf f}$ (LF), $\hat{\mathbf F}$ (high order) | $\hat f^{\mathrm{LO}}$, $\hat f^{\mathrm{HO}}$ | |
| $\theta_{i+1/2,j}$ | $\theta_{i+1/2}$ | |
| $\epsilon_\rho$, $\epsilon_p$ | $\epsilon_{\mathcal{G}}$ | |
| $\alpha_x$, $\alpha_y$ | $\alpha$ per direction | |
| $\nu$ (artificial resistivity) | — | not the CFL number $\nu$ |

# Pages created or updated

* Created [MHD blast wave in a low-β medium](/benchmarks/mhd-blast-wave.md).
* Created [MHD rotor](/benchmarks/mhd-rotor.md).
* Created [Orszag–Tang vortex (2D MHD)](/benchmarks/orszag-tang-vortex.md).
* Created [Shock–cloud interaction (MHD and relativistic MHD)](/benchmarks/shock-cloud-interaction.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Created [Constrained transport for high-order capturing schemes (MHD)](/methods/constrained-transport.md).
* Updated [Positivity-preserving flux limiters (high/low-order flux blending)](/methods/positivity-preserving-flux-limiter.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Created [Lax–Wendroff (Taylor) single-step time discretization](/methods/taylor-time-discretization.md).
* Updated [Positivity preservation (invariance of the admissible set)](/properties/positivity-preserving.md).
* Updated [Notation registry](/notation.md): batch-3 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2016-JCP-Christlieb-101016jjcp201604016.pdf` (doi:10.1016/j.jcp.2016.04.016; typeset article): text extraction, all sections. The Taylor-expanded flux formulas and the limiter's closed-form box are illegible in the text layer and are not reproduced. Reference list: 63 entries.

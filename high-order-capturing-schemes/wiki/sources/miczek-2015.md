---
type: Source
title: "Miczek, Röpke & Edelmann (2015) — New numerical solver for flows at various Mach numbers"
description: "Shows by Mach-number scaling that the Roe upwind matrix dissipates momentum like 1/Ma at low Mach, and preconditions only the dissipation term with a new matrix whose scaling matches the physical Jacobian and which switches off for Ma ≥ 1: Mach-independent kinetic-energy loss down to Mach 1e-10 on the Gresho vortex, with unlimited second-order reconstruction and no shock tests."
resource: "doi:10.1051/0004-6361/201425059"
source_kind: paper
authors: [Miczek F., Röpke F.K., Edelmann P.V.F.]
year: 2015
venue: "Astron. Astrophys. 576:A50"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2015-A&A-Miczek-10105100046361201425059.pdf"
tags: [riemann-solver, low-mach]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper targets the low-Mach accuracy failure of Godunov-type (Roe)
finite-volume schemes for the Euler equations, with stellar astrophysics
in mind. A Mach-number expansion yields two requirements: well-prepared
data stay incompressible, and kinetic energy is conserved. A scaling
analysis of the Roe upwind matrix in primitive variables finds terms of
order $1/\mathrm{Ma}_r$ where the physical Jacobian has terms of order 1.
The cure preconditions only the dissipation. The new matrix fixes the
Weiss–Smith matrix's spurious pressure coupling into mass and energy, and
recovers plain Roe for $\mathrm{Ma} \ge 1$. The tests are smooth, use
unlimited second-order reconstruction, and include no shocks. Merged into
[low-Mach-number fluxes](/methods/low-mach-number-fluxes.md) and the
Riemann-solver page.

# Key claims

1. **Low-Mach limit** (§§2–3, eqs. 3–12). The momentum flux carries
   $1/\mathrm{Ma}_r^2$ on the pressure. As $\mathrm{Ma}_r \to 0$,
   $p = p_0(t) + \mathrm{Ma}_r^2 p_2$ and $\nabla\cdot\mathbf v = 0$.
   Sound waves form a separate class, with pressure fluctuations linear
   in $\mathrm{Ma}_r$.
2. **Godunov fluxes break requirement 1** (§6.2, eq. 29, quoting Guillard
   & Murrone). The interface pressure has fluctuations of order
   $\mathrm{Ma}_r$, driven by the velocity jump. This is intrinsic to the
   Godunov strategy.
3. **Scaling** (§7). The physical Jacobian has entries of order 1, except
   the pressure column of the velocity rows, which is of order
   $1/\mathrm{Ma}_r^2$. The Roe upwind matrix has a velocity block of
   order $1/\mathrm{Ma}_r$. That block is the origin of the excess
   dissipation.
4. **Preconditioned dissipation** (§8, eqs. 33–35). Only the dissipation
   term changes, to $P_{\mathrm{pc}}^{-1}\vert P_{\mathrm{pc}}A\vert_{\mathrm{Roe}}$.
   The time derivative and the central flux are unchanged.
5. **Weiss–Smith versus the new matrix** (eqs. 36–37, from the page images).
   * Weiss–Smith leaves order-$1/\mathrm{Ma}_r^2$ terms in the pressure
     column of the mass and energy rows, which prevents hydrostatic
     equilibrium.
   * The new matrix adds off-diagonal terms proportional to
     $\delta_{\mathrm{pc}} = 1/\mu_{\mathrm{pc}} - 1$. Its dissipation has
     the physical Jacobian's scaling, and it reduces to Roe for
     $\mathrm{Ma} \ge 1$.
6. **Caveats** (§8). The flux is not unique, stability is not proved, and
   $\mathrm{Ma}_{\mathrm{cut}}$ is not given.
7. **Reconstruction** (§§1, 6). All runs use unlimited piecewise-linear
   reconstruction. The flux change "can thus be combined with any kind of
   reconstruction", and the gain is largest at low order. Higher-order
   reconstruction "may slightly alleviate" the problem.

**Tests** (§§4, 6, 9):
* **Gresho vortex** on $40\times40$, one revolution, at maximum Mach
  $10^{-1}$ to $10^{-10}$. The kinetic energy kept is in Table 1:

  | | $10^{-1}$ | $10^{-2}$ | $10^{-3}$ |
  |---|---|---|---|
  | Roe | 94.47 % | 74.52 % | 49.24 % |
  | preconditioned, implicit ESDIRK34 | 98.70 % | 98.72 % | 98.72 % |
  | preconditioned, explicit RK3 | 97.70 % | 97.74 % | 98.31 % |

* **Smooth Kelvin–Helmholtz** at Mach $10^{-2}$, $128^2$ and $1024^2$.
* **Gresho vortex plus an acoustic packet.** Sound speed unchanged; the
  vortex is preserved only with preconditioning.

# Notation map

| Miczek et al. (2015) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$; $\varrho$, $q$, $p$, $E$ | $u$; $\rho$, $\mathbf v$, $p$, $E/\rho$ | the paper's $E$ is specific; $q$ is the weight power |
| $F_{l+1/2}$; $U^L$, $U^R$ | $\hat f_{i+1/2}$; $u^-$, $u^+$ | |
| $M$, $M_r$, $M_{\mathrm{cut}}$ | $\mathrm{Ma}$, $\mathrm{Ma}_r$, $\mathrm{Ma}_{\mathrm{cut}}$ | $M$ is the TVB constant |
| $P$, $P_V$ | $P_{\mathrm{pc}}$ | |
| $\mu$, $\delta$ | $\mu_{\mathrm{pc}}$, $\delta_{\mathrm{pc}}$ | collide with $\mu$, $\delta_k$ |
| $D$ (upwinding matrix) | $\Theta_{i+1/2}$ | |
| $V$ | $\mathbf W$ | primitive state |
| $\alpha$, $\beta$, $\phi_i$, $\kappa$, $\psi$, $\xi$ | local (words) | all collide with registry symbols |
| $c_{\mathrm{CFL}}$ | $\nu$ (advective) | |

# Pages created or updated

* Created [Low-Mach-number numerical fluxes](/methods/low-mach-number-fluxes.md).
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md) (low Mach).
* Updated [Notation registry](/notation.md): $\mathrm{Ma}$, $\mathrm{Ma}_r$, $\mathrm{Ma}_{\mathrm{cut}}$, $P_{\mathrm{pc}}$, $\mu_{\mathrm{pc}}$, $\delta_{\mathrm{pc}}$.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2015-A&A-Miczek-10105100046361201425059.pdf`.
   * **Version.** arXiv:1409.8289v2 (6 February 2015), the A&A accepted
     manuscript at proof stage ("manuscript no. lowmach"). It is not the
     typeset article.
   * **Identity.** doi:10.1051/0004-6361/201425059, checked on Crossref:
     Astron. Astrophys. 576:A50, 2015.
   * **How it was read.** Text extraction, all sections. The matrices of
     pp. 9–11 and eqs. 13–15, 29 and 36–37 were checked on the page
     images.
   * **Recorded as printed.** Eq. 15, the time step, is dimensionally
     inverted, apparently a typesetting error.
   * **Reference list:** 43 entries. A&A style prints no article titles.

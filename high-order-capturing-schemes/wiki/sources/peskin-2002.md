---
type: Source
title: "Peskin (2002) — The immersed boundary method"
description: "Review of the continuous-forcing immersed boundary method for viscous incompressible flow with immersed elastic structures: Eulerian–Lagrangian coupling through the Dirac delta, spreading as the adjoint of interpolation, the postulates and formula of the 4-point discrete delta function, second-order Runge–Kutta time stepping, and the method's limits (first order at sharp interfaces, stiffness, volume loss); no compressible flow."
resource: "doi:10.1017/S0962492902000077"
source_kind: paper
authors: [Peskin C.S.]
year: 2002
venue: "Acta Numer. 11:479–517"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2002-ActaNumer-Peskin-101017s0962492902000077.pdf"
tags: [immersed-boundary, boundary-treatment, review]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The canonical review of Peskin's immersed boundary (IB) method for
fluid–structure interaction in viscous incompressible flow, mostly
biofluid dynamics. The equations of motion of an incompressible elastic
material come from least action (§2): Eulerian Navier–Stokes with a body
force, a Lagrangian elastic energy, and interaction equations through the
Dirac delta. The spatial discretization (§§4–5) couples a fixed Cartesian
grid to a moving Lagrangian grid through a smoothed delta function. §6
constructs the standard 4-point kernel from postulates, and §7 gives the
time stepping. The paper has no numerical tests, no compressible flow
and no shocks. Merged into [immersed-boundary methods](/methods/immersed-boundary-method.md).

# Key claims

1. **Formulation** (§2, eqs. 2.43–2.48). Navier–Stokes with
   $\nabla\cdot\mathbf v = 0$ and a body force spread from the Lagrangian
   force density; the boundary moves with the interpolated velocity; the
   force is the variational derivative of the elastic energy. Elastic
   surfaces need no change except a singular force (§3), equivalent to the
   stress-jump conditions.
2. **Adjointness** (§5). The same $\delta_h$ spreads and interpolates, so
   momentum and power agree in the two descriptions for any kernel; mass,
   force and torque need the zeroth and first moment conditions. Discrete
   mass is conserved exactly, and an energy identity holds for uniform
   density.
3. **Discrete delta** (§6, eqs. 6.1–6.27). Postulates: continuity,
   support of four meshwidths, even/odd partition of unity (against the
   null space of the central-difference gradient), zero first moment,
   constant sum of squares. They give $\phi(0) = \tfrac12$,
   $\phi(\pm1) = \tfrac14$ and the closed form of eq. 6.27, which is
   $C^1$ and close to $\tfrac14(1 + \cos\tfrac{\pi r}{2})$. Exact
   translation invariance is impossible with bounded support
   (eqs. 6.9–6.14). A 3-point kernel suits the MAC scheme; higher moments
   widen the support by two each.
4. **Time stepping** (§7, eqs. 7.2–7.12). Formally second-order
   Runge–Kutta (midpoint rule, trapezoidal viscous term), with FFT solves
   for constant density.
5. **Limits** (§8). Second order for smooth solutions, first order at
   sharp interfaces (smeared over a meshwidth); explicit elastic forces
   force small steps; the interpolated velocity is not divergence-free, so
   enclosed volume leaks. No convergence proof exists.
6. **Rigid bodies** (§9) are held by stiff springs to target points (the
   feedback-forcing idea traced to Sirovich and to Goldstein, Handler and
   Sirovich).

# Notation map

| Peskin (2002) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf u$ | $\mathbf v$ | velocity |
| $\mathbf f$ | $\mathbf b_{\mathrm{IB}}$ | $\mathbf f$ is the flux |
| $\mathbf X(q,r,s,t)$, $\mathbf F$ | $\mathbf X_{\mathrm{IB}}$, $\mathbf F_{\mathrm{IB}}$ | $\mathbf X$ is the mapped coordinate |
| $\delta_h$, $\phi$ | $\delta_h$, $\phi_{\mathrm{IB}}$ | $\phi_i$ is the PPM flattening |
| $r$ (kernel argument) | words | $r$ is the stencil count |
| $D^0_h$, $L_h$, $S_h$ | words | central difference, compact Laplacian, skew advection |
| $\wp$ | words | Peskin's variation symbol |

# Pages created or updated

* Created [Immersed-boundary methods](/methods/immersed-boundary-method.md).
* Updated [Inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md) (what "changes the PDE" means).
* Updated [Notation registry](/notation.md): $\mathbf X_{\mathrm{IB}}$, $\mathbf F_{\mathrm{IB}}$, $\mathbf b_{\mathrm{IB}}$, $\delta_h$, $\phi_{\mathrm{IB}}$.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2002-ActaNumer-Peskin-101017s0962492902000077.pdf`.
   * **Version.** The published article (Cambridge University Press).
   * **Identity.** doi:10.1017/S0962492902000077, checked on Crossref:
     Acta Numerica 11:479–517, 2002, author C. S. Peskin. The existing
     bibliography entry gave the initials as "S."; corrected from page 1.
   * **How it was read.** Text extraction, all sections; eqs. 6.21–6.27 and
     7.2–7.12 checked on the page images.
   * **Reference list:** 74 entries. Three unpublished works print the year
     "200x" and take the citing year, 2002, with a note (bundle rule).
     Fauci & McDonald is printed 1994 (Crossref: 1995), kept as printed.

---
type: Method
title: "Immersed-boundary methods"
description: "Bodies on a Cartesian grid that does not fit them: Peskin's continuous-forcing method (singular body force spread and interpolated with a discrete delta function, first order at sharp interfaces, incompressible only) and the discrete-forcing sharp-interface ghost-cell methods used for compressible flow, which are not conservative at the wall and, in one hypersonic comparison, miss the cold-wall heat flux."
status: established
aliases: [IB method, immersed boundary, ghost-cell immersed boundary, direct forcing, continuous forcing, Peskin method]
tags: [boundary-treatment, immersed-boundary, cartesian-grid, moving-boundary]
timestamp: 2026-10-13T00:00:00Z
---

# Immersed-boundary methods

An immersed-boundary (IB) method computes the flow around a body on a
Cartesian grid that does not fit it, and imposes the wall condition by
modifying the equations or the solution near the wall. Two families
appear in this corpus. The conservative alternative, which cuts the
cells, is [cut-cell finite volume](/methods/cut-cell-finite-volume.md);
the high-order finite-difference alternative is
[inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md).

## Continuous forcing (Peskin)

[Peskin (2002)](/sources/peskin-2002.md) formulates viscous
incompressible flow with an immersed elastic material as Eulerian
Navier–Stokes with a body force $\mathbf b_{\mathrm{IB}}$, coupled to the
Lagrangian configuration $\mathbf X_{\mathrm{IB}}$ through the Dirac delta
(§2, eqs. 2.43–2.48): the Lagrangian force density $\mathbf F_{\mathrm{IB}}$,
the variational derivative of an elastic energy, is spread to the grid,
and the boundary moves with the interpolated fluid velocity. The wall
condition is not imposed; it is the result of the forcing. Rigid or
fixed bodies are tied to target points by stiff springs (§9).
* **Discretization** (§§4–5). Central differences, a skew-symmetric
  advection operator and a compact Laplacian on the Eulerian grid. The
  same discrete delta $\delta_h$ spreads and interpolates, so spreading is
  the adjoint of interpolation: momentum and power agree in both
  descriptions for any kernel, and mass, force and torque agree under the
  moment conditions on $\delta_h$.
* **The discrete delta** (§6). From postulates (continuity, support
  $\vert\varrho_{\mathrm{IB}}\vert < 2$, even/odd partition of unity, zero first moment,
  constant sum of squares) comes the 4-point kernel
  $\phi_{\mathrm{IB}}(\varrho_{\mathrm{IB}}) = \tfrac18\left(3 - 2\vert\varrho_{\mathrm{IB}}\vert + \sqrt{1 + 4\vert\varrho_{\mathrm{IB}}\vert - 4\varrho_{\mathrm{IB}}^2}\right)$
  for $\vert\varrho_{\mathrm{IB}}\vert \le 1$ and
  $\tfrac18\left(5 - 2\vert\varrho_{\mathrm{IB}}\vert - \sqrt{-7 + 12\vert\varrho_{\mathrm{IB}}\vert - 4\varrho_{\mathrm{IB}}^2}\right)$
  for $1 \le \vert\varrho_{\mathrm{IB}}\vert \le 2$ (eq. 6.27). Exact grid translation
  invariance is impossible for any kernel of bounded support (eqs. 6.9–6.14).
* **Accuracy and cost** (§8). Second order for smooth solutions, but
  first order at a sharp interface, which is smeared over about one cell;
  explicit elastic forces impose a severe time-step limit; the enclosed
  volume is not conserved. These are stated, not measured.
* **Scope.** Incompressible flow only. The paper contains no compressible
  flow, no shocks and no capturing scheme.

## Discrete forcing: sharp-interface ghost-cell methods

The compressible IB methods of this corpus overwrite values near the
wall instead of adding a force. Ghost cells inside the body are filled
from an **image point**, the reflection of the ghost node across the
wall, whose value is interpolated from fluid cells; the wall condition
is applied at the boundary intercept
([Başkaya et al. (2024)](/sources/baskaya-2024.md), §3, Fig. 1;
[Seshadri & De (2020)](/sources/seshadri-2020.md), §§4–5).
* **Geometry** ([Seshadri & De (2020)](/sources/seshadri-2020.md), §§3–4).
  Nodes are classified by ray tracing against the surface triangulation,
  since signed distance misclassifies points near sharp edges. Near edges
  and vertices the reconstruction direction follows angle-weighted
  pseudo-normals, which the authors find as influential for accuracy as
  the order of the boundary formula.
* **Order is traded for robustness near shocks.** Quadratic interpolation
  gives negative density and pressure at boundary nodes in shocked flow,
  so the compressible version uses inverse-distance weighting (§4.6),
  which reproduces only constants (compiler's observation; the rule is
  in the authors' earlier work, not ingested). WENO5 needs three ghost layers, TVD
  one (§5). No boundary order is measured. This is the failure that
  [weighted extrapolation](/methods/weighted-extrapolation.md) is designed
  to avoid.
* **Moving bodies.** The field is extended into the body so that a node
  uncovered by the motion already holds a value (§5); mass conservation
  is claimed qualitatively. The base scheme is Edwards' LDFSS flux
  splitting with TVD or WENO5 and low-Mach preconditioning.
* **Not conservative at the wall.** The ghost values make the wall flux
  only implicitly consistent with the boundary condition. The errors come
  from the nonlinear flux, the image-point interpolation and the wall
  curvature ([Başkaya et al. (2024)](/sources/baskaya-2024.md), §3).

**Cold-wall heat flux, attributed to conservation.** On a Mach 8.98
reacting cylinder with a 300 K wall, a conservative cut-cell method
reproduces the body-fitted reference and the measured stagnation heat
flux (7.19 MW/m² against 7.40 measured), while the CHESS ghost-cell
solver gives 0.167 MW/m² with a correct pressure and a larger shock
stand-off. The cut-cell solver with its conservative flux treatment
switched off is closer but still "clearly wrong". The authors attribute
the error to conservation, not to reconstruction order, as a hypothesis,
and concede that the solvers also differ in other respects; second-order reconstruction suffices in the
conservative method. On an adiabatic wall all methods agree. Their
explanation, that conservation errors scale with the truncation error
and matter only where gradients are steep, is stated, not measured
([Başkaya et al. (2024)](/sources/baskaya-2024.md), §§4.5, 5, Table 7).

**Later uses (batch 12).**
* *Ray-traced IB with multiresolution and WENO5.* Brahmi et al. run
  viscous shock reflection over two concave arcs with the solid
  "embedded in a Cartesian grid tracked using a ray-tracing technique",
  as in Seshadri & De's node classification above, combined with
  adaptive multiresolution refinement, WENO5 inviscid fluxes,
  fourth-order central viscous fluxes and third-order Runge–Kutta, on
  grids of up to 33.55 million points
  ([Brahmi et al. (2020)](/sources/brahmi-2020.md), §2.1;
  [Brahmi et al. (2020b)](/sources/brahmi-2020-b.md), §2;
  [shock reflection from double concave wedges](/benchmarks/double-concave-shock-reflection.md)).
  Neither paper states the IB variant (ghost cell or forcing), the
  interpolation or the wall's thermal condition; the method is deferred
  to Chaudhuri et al. (2011, 2012), not ingested. No boundary accuracy or
  conservation error is measured, so these uses add no evidence on the
  order or conservation questions above.

# Citations

1. [Peskin (2002)](/sources/peskin-2002.md), §§2, 4–9.
2. [Seshadri & De (2020)](/sources/seshadri-2020.md), §§3–6, 8 (author manuscript).
3. [Başkaya et al. (2024)](/sources/baskaya-2024.md), §§3, 4.5, 5 (arXiv v1).
4. [Brahmi et al. (2020)](/sources/brahmi-2020.md), §2.1.
5. [Brahmi et al. (2020b)](/sources/brahmi-2020-b.md), §2.

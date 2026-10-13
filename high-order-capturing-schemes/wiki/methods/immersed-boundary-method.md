---
type: Method
title: "Immersed-boundary methods"
description: "Bodies on a Cartesian grid that does not fit them: Peskin's continuous-forcing method (singular body force spread and interpolated with a discrete delta function, first order at sharp interfaces, incompressible only) and the discrete-forcing sharp-interface ghost-cell methods, incompressible (Mittal et al.'s image-point method) and compressible, which are not conservative at the wall and, in one hypersonic comparison, miss the cold-wall heat flux."
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

The ghost-cell IB methods of this corpus, compressible
([Başkaya et al. (2024)](/sources/baskaya-2024.md);
[Seshadri & De (2020)](/sources/seshadri-2020.md)) and incompressible
([Mittal et al. (2008)](/sources/mittal-2008.md)), overwrite values near
the wall instead of adding a force. Ghost cells inside the body are
filled from an **image point**, the reflection of the ghost node across
the wall, whose value is interpolated from the surrounding nodes
(fluid nodes in the compressible sources; in Mittal et al.'s stencil the
ghost node itself or other ghost nodes can appear, see batch 13 below);
the wall condition is applied at the boundary intercept
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
(INCA) reproduces the body-fitted reference and the measured stagnation
heat flux (7.19 MW/m² against 7.40 measured), while the CHESS ghost-cell
solver gives 0.167 MW/m² with a correct pressure and a larger shock
stand-off; second-order reconstruction suffices in the conservative
method, so reconstruction order is not the cause (§4.5). CHESS and INCA
"clearly differ also in several other aspects", so that comparison alone
leaves open whether the error is inherent to ghost-cell methods (§5).
The isolating experiment is INCA with its conservative cut-cell flux
treatment switched off, a ghost-cell method of nominally the same order
whose only difference from INCA's cut-cell method is the conservative
flux treatment (§5, Fig. 18). It fails too: on the cold cylinder its heat
flux is closer to the reference than CHESS's but "both ghost-cell
methods give clearly wrong results", and on the ablator its blowing rate
shows "a very similar overprediction" to CHESS's. The authors take this
to consolidate the diagnosis that the conservation errors of ghost-cell
methods cause the cold-wall errors. On an adiabatic wall all methods
agree. Their explanation, that conservation errors scale with the
truncation error and matter only where gradients are steep, is stated,
not measured ([Başkaya et al. (2024)](/sources/baskaya-2024.md), §§4.5, 5, Table 7, Fig. 18).

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

**Later uses (batch 13).**
* *An incompressible ghost-cell method.* [Mittal et al. (2008)](/sources/mittal-2008.md)
  is a discrete-forcing, sharp-interface ghost-cell method for
  incompressible viscous flow around stationary, moving and deforming 3D
  bodies and zero-thickness membranes, described by surface
  triangulations (§§1, 2.2). The construction is the same as in the
  compressible sources (the section above, which opened with "the
  compressible IB methods of this corpus", was widened at the 2026-10-13
  deep lint), and this paper has no compressible flow, no shock and no
  capturing scheme.
* *Image point and stencil* (§2.2.2, eqs. 14–19, Figs. 5–6). The image
  point is the ghost node mirrored across the boundary intercept, which
  lies exactly midway between them. Its value is the trilinear
  interpolant (bilinear in 2D) of the 8 (4) surrounding nodes, with
  weights that depend only on geometry and grid and a truncation error
  that is second order in $h$ (Appendix A). The stencil is not always
  made of fluid cells only (the description above said so until the
  2026-10-13 deep lint): when the
  ghost node is one of the 8 nodes its row is replaced by the wall
  condition at the intercept, and when other ghost nodes are in it the
  ghost values are coupled and solved by point Gauss–Seidel, "within
  about 10 iterations in most cases". The intercept search (closest
  vertex, then the normal intercepts on its elements, then a wider search,
  then the closest point on an edge or a vertex) is where the paper spends
  its robustness effort: a wrong intercept gives oversized stencils and
  poor iterative convergence.
* *Wall closures* (eqs. 20–23). Velocity takes a Dirichlet condition: the
  wall value is the mean of the ghost and image values, imposed
  implicitly as "ghost value plus interpolated image value equals twice
  the wall value". The pressure correction of the fractional step takes a
  Neumann condition by a central difference along the probe, which the
  authors call "nominally first-order", because the interpolation error
  is divided by a probe length of order $h$. Both closures are solved
  fully coupled with the discrete momentum and Poisson equations of the
  neighbouring fluid cells. The authors argue that the pressure gradient
  is then first order locally and second order globally, and that
  velocity stays second order because the gradient enters the update
  multiplied by $\Delta t = O(h)$ (stated, not measured). Against the
  ghost-fluid method of Gibou et al., which interpolates along grid
  lines, the midway intercept keeps both closures well conditioned as the
  wall approaches a node, without "lower-order fixes" (§§1, 2.2.2).
* *Node classification by the closest element.* A node is fluid or solid
  according to the sign of the dot product of the outward normal of its
  closest surface element with the vector from that element to the node
  (§2.2.2, Fig. 4); for moving bodies the test is repeated each step near
  the previous fluid–solid boundary only. This is a local signed-distance
  test, the kind [Seshadri & De (2020)](/sources/seshadri-2020.md) reject
  above because it misclassifies points near sharp edges, and Seshadri &
  De list Mittal et al. among the signed-distance methods (their §3.2),
  correctly. Mittal et al. report no misclassification in their tests,
  which include an airfoil; neither paper measures the misclassification
  rate, so the two rules stand side by side without a test that decides
  between them.
* *Fresh cells on moving bodies* (§2.2.3, Fig. 7). A node that the body
  uncovers in a step (solid at $t^n$, fluid at $t^{n+1}$) is at most one
  cell deep under the time-step limit $\nu \lesssim 0.5$ (eq. 25), and
  lacks the old convective, diffusive and pressure-gradient terms. Its
  intermediate velocity is interpolated instead, following Ye et al.'s
  (1999) cut-cell method: normal to the wall, image point, trilinear
  interpolation on the 7 non-fresh nodes around it plus the intercept;
  the pressure then follows from the Poisson equation. Consistency is
  argued from every fresh cell having been a ghost cell the step before.
  This differs from Seshadri & De's field extension above, and from the
  volume-weighted neighbour fill of freshly cleared cells in
  [cut-cell finite volume](/methods/cut-cell-finite-volume.md). Freshly
  covered nodes are only re-classified, and no conservation statement is
  made: only the face velocities are discretely divergence-free (§2.1).
* *Measured order: velocity only, from a graph* (§3.1, Figs. 8–9). In a
  self-convergence study (a cylinder at $\mathrm{Re} = 100$, four uniform
  grids from $70^2$ to $210^2$ against a $630^2$ solution of the same
  scheme, 2000 fixed time steps), the velocity errors in $L_1$, $L_2$ and
  the maximum norm, largest around the cylinder, follow a second-order
  reference line: "globally and locally second-order accurate". No rates
  are printed; the compiler's read-off of the maximum-norm curve is a
  slope of about 2. The pressure error is not measured, the comparison is
  with the scheme's own fine solution rather than an exact one, and the
  run covers only an early transient. This is the first measured
  boundary order among the ghost-cell sources on this page (Seshadri &
  De measure none), and it is for incompressible flow without shocks.
* *The solver it sits in* (§2.1). Collocated cell-centred velocity and
  pressure with face velocities from a Rhie–Chow-like averaging, Van
  Kan's fractional step, second-order Adams–Bashforth convection,
  Crank–Nicolson diffusion, second-order central differences, and a
  geometric-multigrid pressure Poisson solve. The collocated layout needs
  one set of ghost cells, where a staggered one needs four (§2.2.2).
  Validation against published data (cylinders at $\mathrm{Re}$ 40 to
  1000, a NACA 0008 airfoil, a sphere, impulsively started bodies) gives
  mean cylinder drag within 4% of Henderson's values and airfoil drag and
  lift within 0.006 of Kunz & Kroo's (§§3.2–3.3); the rest is graphical
  (§§3.4–3.5).

# Citations

1. [Peskin (2002)](/sources/peskin-2002.md), §§2, 4–9.
2. [Seshadri & De (2020)](/sources/seshadri-2020.md), §§3–6, 8 (author manuscript).
3. [Başkaya et al. (2024)](/sources/baskaya-2024.md), §§3, 4.5, 5, Fig. 18 (arXiv v1).
4. [Brahmi et al. (2020)](/sources/brahmi-2020.md), §2.1.
5. [Brahmi et al. (2020b)](/sources/brahmi-2020-b.md), §2.
6. [Mittal et al. (2008)](/sources/mittal-2008.md), §§1, 2.1–2.2, 3.1–3.5, Appendix A.

---
type: Source
title: "Peskin (2002) — The immersed boundary method"
description: "Acta Numerica review of the mathematical structure of the immersed boundary method: derivation of the Eulerian–Lagrangian equations from the principle of least action, spatial discretization, the identities that make spreading the adjoint of interpolation and conserve force, torque, momentum and energy, the postulates and construction of the 4-point delta function, Runge–Kutta time stepping, open problems and applications."
resource: "doi:10.1017/S0962492902000077"
source_kind: paper
authors: [Peskin C.S.]
year: 2002
venue: "Acta Numer. 11:479-517"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2002_Crossref_Acta_Numerica_Peskin_The_immersed_boundary_method.pdf"
tags: [immersed-boundary, fluid-structure-interaction, delta-function, conservation, review, biofluid]
timestamp: 2026-11-08T17:54:00Z
---

# Summary

Peskin sets out the mathematical structure of the
[classical immersed boundary method](/methods/classical-immersed-boundary-method.md).
The equations of an incompressible viscoelastic material, derived from the
principle of least action, become a viscous fluid of variable density driven
by a force density, coupled to Lagrangian elasticity through the Dirac delta;
an immersed boundary is the case of elastic material confined to surfaces.
The numerical method uses a fixed Cartesian grid, a moving Lagrangian grid
and a [regularized delta function](/operators/regularized-delta-function.md)
in [spreading and interpolation](/operators/spreading-and-interpolation.md).
Because the same kernel is used in both, spreading is the adjoint of
interpolation and the coupling neither creates nor destroys force, torque,
momentum or energy ([discrete conservation](/properties/discrete-conservation.md)).
The 4-point delta function follows from explicit postulates. Peskin lists the
open problems — stiffness of explicit elastic forces, first-order accuracy at
interfaces ([first-order accuracy of regularized-delta forcing](/results/first-order-accuracy-of-regularized-delta-forcing.md)),
volume leakage — and the applications in biofluid dynamics.

# Version read

Version of record, Acta Numerica 11, 479–517 (2002), 39 pages (Cambridge
online). Sections on the equations of motion, the immersed boundary
formulation, spatial discretization, identities, delta-function construction
and temporal discretization read in full; the research directions and
applications read for their content; reference list read in full. The text
layer omits some display equations (the 4-point kernel is reconstructed from
the derivation in §6 and checks against the stated values $\varphi(0)=1/2$,
$\varphi(\pm1)=1/4$, $C=3/8$). Section numbers follow the paper's order:
§2 equations of motion, §3 immersed boundaries, §4 spatial discretization,
§5 identities, §6 delta function, §7 time stepping, §8 research directions,
§9 applications.

# Key claims

1. The immersed boundary formulation of an incompressible elastic material follows from the principle of least action by introducing Eulerian variables, including a pseudo-velocity for the perturbation, through the delta function (§2). **Derived**
2. The resulting system is a viscous incompressible fluid of non-uniform density with a body force, two interaction equations with kernel $\delta(\mathbf x-\mathbf X)$, and a Lagrangian elasticity law; the viscous term is added afterwards (§2). **Derived**
3. Spreading relates densities, interpolation relates values; the difference comes from the map $\mathbf s\mapsto\mathbf X$ in the delta's argument (§2). **Stated**
4. A fibre material's force density lies in the osculating plane of the fibres (§2). **Derived**
5. Elastic surfaces give force and mass densities singular like a 1-D delta on the surface; the formulation is equivalent to stress-jump conditions (§3, citing Peskin and Printz 1993, Lai and Li 2001). **Stated**
6. To avoid leaks the Lagrangian spacing must keep markers less than $h/2$ apart (§4). **Stated**
7. The skew-symmetric advection operator is skew for any $\mathbf u$, not only divergence-free ones (§4). **Derived**
8. For any $\delta_h$, Eulerian and Lagrangian momentum and power agree because spreading is the adjoint of interpolation with the same kernel (§5). **Proved**
9. With unit sum and vanishing first moment for all shifts, mass, force and torque agree in both descriptions (§5). **Proved**
10. For uniform density and translation-invariant elastic energy the spatially discrete method conserves momentum, and kinetic plus elastic energy decreases by exactly the viscous dissipation; these results are not available for non-uniform density (§5). **Proved**
11. The postulates (continuity, support $4h$, even–odd sums $1/2$, zero first moment, constant sum of squares) determine the 4-point $\varphi$; it is symmetric and $C^1$ without being required to be (§6). **Derived**
12. Exact translation invariance $\sum_j\varphi(r_1-j)\varphi(r_2-j)=\Phi(r_1-r_2)$ is incompatible with bounded support (§6). **Proved**
13. The cosine kernel $\tfrac14(1+\cos(\pi r/2))$ approximates the 4-point kernel well and satisfies all postulates but the first moment; a 3-point kernel suits schemes without the $D_0$ null-space problem; higher moments widen the support two points at a time (§6). **Stated**
14. With $\delta_h$, smooth functions are interpolated to second order, but at a true immersed boundary the interpolation is only first order (§6). **Stated**
15. Time stepping is a second-order Runge–Kutta scheme with a preliminary half step and a final step, implicit where possible but explicit in the elastic force (§7, after Lai and Peskin 2000). **Stated**
16. Open problems: the severe time-step restriction from explicit elastic forces, first-order accuracy, lack of volume conservation (§8). **Stated**
17. Applications include heart valves and the whole heart, platelets, swimming organisms, biofilms, the cochlea, valveless pumping, filaments and flags, sails, parachutes and insect flight (§9). **Stated** (cited)

# Notation map

| Peskin (2002) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $(q,r,s)$ | $\mathbf s$ | Lagrangian coordinates |
| $\mathbf X(q,r,s,t)$ | $\mathbf X(\mathbf s,t)$ | agree |
| $M(q,r,s)$, $\tilde M$ | $M_\Gamma$, excess mass page-local | |
| $E[\mathbf X]$, $\mathcal E$ (density) | $\mathcal E[\mathbf X]$ | elastic energy |
| $\mathbf F$, $\mathbf f$ | $\mathbf F$, $\mathbf f$ | agree |
| $\wp$ (perturbation) | $\wp$ | agree |
| $\delta_h$, $\phi(r)$ | $\delta_h$, $\varphi(r)$ | $\phi$ is the level set in the registry |
| $g_h$, $G_h$ | Eulerian and Lagrangian grids | |
| $D_0^h$, $L_h$, $S_h(\mathbf u)$ | $D_0$, $L_h$, $S_h(\mathbf u)$ | agree |
| $\tau$, $T$ | $\boldsymbol\tau$, $T$ | fibre direction, tension |

# Reference list

74 printed references (unnumbered, alphabetical), merged complete into the
[bibliography](/bibliography.md) from the printed list (Crossref deposits
none). Peskin's 1972 PhD thesis is a separate entry from the 1972 paper;
three items are printed as "200x" unpublished work and one as submitted.

# Pages created or updated

Chunk 1 (2026-11-08), list updated in chunk 4 (2026-11-08). This source is cited on:

- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Sharp and diffuse interface representations](/definitions/sharp-and-diffuse-interface.md)
- [Classical (Peskin) immersed boundary method](/methods/classical-immersed-boundary-method.md)
- [Fluid–structure coupling in immersed boundary methods](/methods/fluid-structure-coupling.md)
- [Immersed interface method](/methods/immersed-interface-method.md)
- [Regularized delta function $\delta_h$](/operators/regularized-delta-function.md)
- [Spreading and interpolation operators $\mathcal S$, $\mathcal J$](/operators/spreading-and-interpolation.md)
- [Discrete conservation](/properties/discrete-conservation.md)
- [First-order accuracy of regularized-delta forcing at interfaces](/results/first-order-accuracy-of-regularized-delta-forcing.md)

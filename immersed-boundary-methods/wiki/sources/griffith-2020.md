---
type: Source
title: "Griffith & Patankar (2020) — Immersed methods for fluid–structure interaction"
description: "Annual Review of immersed methods for elastic structures and prescribed kinematics: regularized-delta coupling with fibre and finite-element structures, immersed interface methods that apply jump conditions, kernels and quadrature, penalty and Lagrange-multiplier formulations, explicit-coupling stability, benchmarks and biomedical applications, and open issues."
resource: "doi:10.1146/annurev-fluid-010719-060228"
source_kind: paper
authors: [Griffith B.E., Patankar N.A.]
year: 2020
venue: "Annu. Rev. Fluid Mech. 52:421-448"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2020_Crossref_Annual_Review_of_Fluid_Mechanics_Griffith_Immersed_Methods_for_FluidStructure_Interaction.pdf"
tags: [review, fluid-structure-interaction, immersed-interface, delta-function, finite-element, biofluid]
timestamp: 2026-11-08T18:12:00Z
---

# Summary

Griffith and Patankar review immersed methods for fluid–structure interaction
with elastic structures and structures with prescribed kinematics, extending
Mittal and Iaccarino's review of rigid bodies. They contrast the
regularized-delta coupling of the [classical method](/methods/classical-immersed-boundary-method.md)
and its finite-element variants with [immersed interface methods](/methods/immersed-interface-method.md)
that apply jump conditions, discuss kernels and quadrature
([regularized delta function](/operators/regularized-delta-function.md)),
penalty and Lagrange-multiplier formulations and explicit versus implicit
coupling ([fluid–structure coupling](/methods/fluid-structure-coupling.md)),
and show applications up to $Re\approx20{,}000$.

# Version read

Version of record (Annual Reviews download), Annu. Rev. Fluid Mech. 52,
421–448 (2020). Introduction, formulations, discretization, benchmarks and the
summary and future-issue lists read; applications skimmed. The text layer
carries no section numbers, so claims are located by part. Title and authors
match Crossref.

# Key claims

1. The key challenge of immersed methods is the operators coupling the Eulerian and Lagrangian frames (introduction). **Stated**
2. Regularized-delta methods are broadly applicable but lower-order accurate at interfaces, because they smooth stress discontinuities, and give slowly converging force distributions (introduction; summary points). **Stated**
3. Immersed interface methods improve velocity, deformation and stress accuracy, at the cost of more complex geometry computations (introduction; jump conditions). **Stated**
4. With nodal quadrature the coupling operators are adjoint, and too-sparse markers leak; Gaussian quadrature lets the structural mesh be coarse relative to the fluid grid (discretization). **Stated**
5. Immersed formulations do not appear to suffer added-mass instabilities even with explicit coupling, but stiff structures or large penalty parameters need small time steps (introduction). **Stated**
6. For a cylinder at $Re=200$ the immersed boundary method generates spurious interior flow, removed by the immersed interface method (benchmarks, Fig. 3). **Shown**
7. Future issues: adjoint coupling operators for immersed interface methods, scalable implicit solvers, turbulence models, verification and validation of biomedical models (future issues). **Stated**

# Notation map

| Griffith & Patankar (2020) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol\chi(\mathbf s,t)$ | $\mathbf X(\mathbf s,t)$ | structural deformation map |
| $\mathcal S$, $\mathcal J$ | $\mathcal S$, $\mathcal J$ | agree |
| $\phi(r)$, $B_k$ | $\varphi(r)$, B-spline kernels | $\phi$ is the level set |
| $U(J)$, $\kappa$ | volumetric energy, bulk modulus | registry $\kappa$ is the volume fraction |

# Reference list

All 157 entries of the Crossref deposit of the review's literature list are
merged complete into the [bibliography](/bibliography.md).

# Pages created or updated

Chunk 3 (2026-11-08), list updated in chunk 4 (2026-11-08). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Sharp and diffuse interface representations](/definitions/sharp-and-diffuse-interface.md)
- [Classical (Peskin) immersed boundary method](/methods/classical-immersed-boundary-method.md)
- [Fluid–structure coupling in immersed boundary methods](/methods/fluid-structure-coupling.md)
- [Immersed interface method](/methods/immersed-interface-method.md)
- [Regularized delta function $\delta_h$](/operators/regularized-delta-function.md)
- [First-order accuracy of regularized-delta forcing at interfaces](/results/first-order-accuracy-of-regularized-delta-forcing.md)

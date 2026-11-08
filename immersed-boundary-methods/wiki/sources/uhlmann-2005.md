---
type: Source
title: "Uhlmann (2005) — An immersed boundary method with direct forcing for the simulation of particulate flows"
description: "Combines Peskin's regularized-delta transfer with an explicit direct forcing evaluated at Lagrangian points that move rigidly with suspended particles, giving smooth hydrodynamic forces on moving bodies without time-step penalties; validated on cylinders and settling discs and spheres, up to 1000 particles."
resource: "doi:10.1016/j.jcp.2005.03.017"
source_kind: paper
authors: [Uhlmann M.]
year: 2005
venue: "J. Comput. Phys. 209(2):448-476"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2005_Crossref_Journal_of_Computational_Physics_Uhlmann_An_immersed_boundary_method_with_direct_forcing_for_the_simu.pdf"
tags: [direct-forcing, delta-function, particulate-flow, moving-boundary, diffuse-interface]
timestamp: 2026-11-08T18:08:00Z
---

# Summary

Uhlmann evaluates the [direct forcing](/methods/direct-forcing.md) of
Fadlun et al. at Lagrangian force points on the particle surfaces and
transfers velocities and forces with the 3-point
[regularized delta function](/operators/regularized-delta-function.md) of
Roma et al. ([spreading and interpolation](/operators/spreading-and-interpolation.md)).
The force is explicit, introduces no parameter and no time-step limit, and
varies smoothly as particles move across the grid, unlike reconstruction-based
direct forcing. Particles obey Newton's equations, weakly coupled to the
fluid. Tests range from a cylinder to the sedimentation of 1000 spheres.

# Version read

arXiv:1809.08170v1 (2018), a posting of the published paper that states on
its first page "published in J. Comput. Phys., 209(2):448–476, 2005"; layout
and page numbers differ from the journal. §§1–4 read in full, §5 for set-up
and results. Title and author match Crossref.

# Key claims

1. Feedback ("virtual boundary") forcing adds problem-dependent spring and damping constants and time scales that must be resolved (§1). **Stated**
2. Reconstruction-based direct forcing (Fadlun et al., Kim et al.) gives strong force oscillations for arbitrarily moving objects; volume-fraction smoothing (Kajishima and Takiguchi) gives mesh-scale oscillations and a non-solenoidal velocity near particles (§1, §5). **Shown**
3. The force is computed at Lagrangian points that follow the rigid motion (no extra degrees of freedom), with volumes forming a one-mesh-width shell; forcing the interior made no significant difference in 2-D tests (§2–§3). **Stated**/**Shown**
4. With the 3-point kernel, the coupling introduces no additional time-step restriction (CFL close to $\sqrt3$) and the velocity is discretely divergence-free (§3). **Stated**
5. The hydrodynamic force follows from the coupling force plus the rate of change of fluid momentum inside the particle (§4, Appendix B). **Derived**
6. Weak coupling is stable only for $\rho_p/\rho_f\gtrsim1.05$ (discs) and $\gtrsim1.2$ (spheres), independent of $\Delta t$ (§4). **Shown**
7. Decaying vortices in an embedded circle: second order, error smooth under sub-grid shifts of the boundary (§5.1). **Shown**
8. Cylinder at $Re=100$ ($D/h=38.4$): $St$ within 4 %, lift and drag fluctuation amplitudes within 3 % and 8 %, mean drag 11 % high (8 % on a larger domain), like Lai and Peskin (§5). **Shown**
9. Oscillating cylinder at $Re=185$: drag smooth with position; the 4-point kernel smoother, at higher cost (§5). **Shown**
10. Settling discs (drafting–kissing–tumbling), a settling sphere and 1000 sedimenting spheres demonstrate efficiency (§5). **Shown**

# Notation map

| Uhlmann (2005) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf X_l$, $\Delta V_l$ | $\mathbf X_\ell$, volume of force point $\ell$ | |
| $\mathbf F$, $\mathbf f$ | $\mathbf F_\ell$, $\mathbf f$ | |
| $\mathbf U^{(d)}$ | $\mathbf u_\Gamma(\mathbf X_\ell)$ | rigid-body velocity |
| $\tilde{\mathbf u}$, $\tilde{\mathbf U}$ | $\tilde{\mathbf u}$, $\tilde{\mathbf U}_\ell$ | provisional velocity |
| $\mathbf u_c$, $\boldsymbol\omega_c$, $\mathbf x_c$ | same | particle velocity, angular velocity, centre |
| $\phi$ (pseudo-pressure) | page-local | $\phi$ is the level set |
| $\rho_p$, $\rho_f$ | same | particle and fluid density |

# Reference list

37 references, merged complete into the [bibliography](/bibliography.md)
from the Crossref deposited list of the journal version.

# Pages created or updated

Chunk 2 (2026-11-08). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Flow past a sphere](/benchmarks/flow-past-sphere.md)
- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Direct (discrete-time) forcing](/methods/direct-forcing.md)
- [Feedback forcing](/methods/feedback-forcing.md)
- [Regularized delta function $\delta_h$](/operators/regularized-delta-function.md)
- [Spreading and interpolation operators $\mathcal S$, $\mathcal J$](/operators/spreading-and-interpolation.md)
- [Discrete conservation](/properties/discrete-conservation.md)
- [First-order accuracy of regularized-delta forcing at interfaces](/results/first-order-accuracy-of-regularized-delta-forcing.md)

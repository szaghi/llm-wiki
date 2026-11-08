---
type: Source
title: "Fadlun, Verzicco, Orlandi & Mohd-Yusof (2000) — Combined immersed-boundary finite-difference methods for three-dimensional complex flow simulations"
description: "Compares feedback and direct (discrete-time) forcing in a second-order staggered finite-difference solver: direct forcing removes the gains and the time-step penalty, while the accuracy is set by how the forcing is interpolated — stepwise below first order, volume-fraction first order, linear velocity reconstruction second order; applied to a vortex ring, a sphere and LES of a piston–cylinder assembly."
resource: "doi:10.1006/jcph.2000.6484"
source_kind: paper
authors: [Fadlun E.A., Verzicco R., Orlandi P., Mohd-Yusof J.]
year: 2000
venue: "J. Comput. Phys. 161(1):35-60"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2000_Crossref_Journal_of_Computational_Physics_Fadlun_Combined_Immersed-Boundary_Finite-Difference_Methods_for_Thr.pdf"
tags: [direct-forcing, feedback-forcing, reconstruction, incompressible, les, moving-boundary]
timestamp: 2026-11-08T17:50:00Z
---

# Summary

Fadlun, Verzicco, Orlandi and Mohd-Yusof implement the
[feedback forcing](/methods/feedback-forcing.md) of Goldstein et al. and the
[direct forcing](/methods/direct-forcing.md) of Mohd-Yusof in a second-order
finite-difference solver on staggered (Cartesian or cylindrical) grids. Both
give the same results, but direct forcing runs at a time step about 60 times
larger. The order of accuracy depends on how the forcing is placed on the
grid: linear reconstruction of the velocity at the first point outside the
body is second order ([sharp and diffuse interfaces](/definitions/sharp-and-diffuse-interface.md);
[first-order accuracy of regularized-delta forcing](/results/first-order-accuracy-of-regularized-delta-forcing.md)).
Applications include a vortex ring against experiment,
[flow past a sphere](/benchmarks/flow-past-sphere.md), and the first
immersed-boundary large-eddy simulation, of a motored piston–cylinder
assembly with a moving piston.

# Version read

Version of record, J. Comput. Phys. 161, 35–60 (2000), 26 pages. §§1–2 and
the Appendix read in full, §3 (applications) read for the set-up and
conclusions. Page-1 title and authors match Crossref.

# Key claims

1. Earlier immersed-boundary work: Peskin's elastic boundaries (rigid bodies by stiff springs, force system as complex as for elastic ones), Briscolini and Santangelo's mask method, Goldstein et al.'s feedback forcing with spectral methods (spurious oscillations without spreading over 3–4 points), Saiki and Biringen with fourth-order differences (§1). **Stated** (cited)
2. Feedback forcing behaves as a damped oscillator; its gains are flow dependent and make the equations stiff; Goldstein et al. ran at CFL $O(10^{-3})$ (§2.1). **Stated**
3. Treating the proportional term implicitly raises the stable CFL to $0.025$–$0.1$; sharp corners prevent small gains; smooth geometries reach CFL $0.5$ (§2.1). **Shown**
4. Direct forcing imposes the boundary value exactly at each step, has no free constants, costs no extra CPU and does not affect stability when each term is taken at the right time level (§2.2, Appendix). **Stated**/**Derived**
5. The accuracy is independent of the forcing law and depends on the interpolation: stepwise geometry converges slower than first order, volume-fraction weighting at first order (and underestimates boundary velocities), linear velocity reconstruction at second order (§2.3, Fig. 5). **Shown**
6. Linear reconstruction assumes a nearly linear profile near the wall, which needs fine near-wall grids; combining immersed boundaries with embedded grids could help, at a cost to be assessed (§2.3). **Stated**
7. Moving boundaries need no change of method — only the forcing points are recomputed each step; sharp corners are treated like the rest of the boundary (§2.3). **Stated**
8. With direct forcing the vortex-ring case runs at CFL $1.5$, near the RK3 limit $\sqrt3$, with long-term dynamics preserved; feedback forcing is at its limit at CFL $0.025$ (§2.4, Fig. 6). **Shown**
9. Vortex-ring formation agrees with the authors' experiment; the sphere's recirculation length and surface pressure for $Re=100$–$1000$ agree with body-fitted results (§3.1–3.2). **Shown**
10. The piston–cylinder LES is, to the authors' knowledge, the first immersed-boundary simulation with an LES model, validated against experiments (§3.3). **Stated**/**Shown**

# Notation map

| Fadlun et al. (2000) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf V$ (boundary velocity) | $\mathbf u_\Gamma$ | |
| $\bar{\mathbf V}$ (interpolated target) | $\mathbf V$ | target at the forcing point |
| $\alpha_f$, $\beta_f$ | $\alpha_f$, $\beta_f$ | agree |
| $\psi_b/\psi$ | solid fraction $1-\kappa$ of the cell | |
| $\mathrm{RHS}^{l+1/2}$ | $\mathbf{RHS}^{n+1/2}$ | |
| $l$ (time level), $\gamma_l,\rho_l,\alpha_l$ | $n$; RK coefficients page-local | |

# Reference list

27 printed references, merged complete into the [bibliography](/bibliography.md)
from the Crossref deposited list.

# Pages created or updated

Chunk 1 (2026-11-08). This source is cited on:

- [Flow past a sphere](/benchmarks/flow-past-sphere.md)
- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Sharp and diffuse interface representations](/definitions/sharp-and-diffuse-interface.md)
- [Classical (Peskin) immersed boundary method](/methods/classical-immersed-boundary-method.md)
- [Direct (discrete-time) forcing](/methods/direct-forcing.md)
- [Feedback forcing](/methods/feedback-forcing.md)
- [First-order accuracy of regularized-delta forcing at interfaces](/results/first-order-accuracy-of-regularized-delta-forcing.md)

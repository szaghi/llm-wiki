---
type: Source
title: "Balsara, Käppeli, Boscheri & Dumbser (2023) — Curl constraint-preserving reconstruction and the guidance it gives for mimetic scheme design"
description: "Edge-collocated, globally curl-preserving WENO-like reconstruction (2D to fourth order, 3D to third) with vertex potentials from multidimensional Riemann solvers: the edge-vertex mirror of divergence-free reconstruction and CT."
resource: "doi:10.1007/s42967-021-00160-3"
source_kind: paper
authors: [Balsara D.S., Käppeli R., Boscheri W., Dumbser M.]
year: 2023
venue: "Commun. Appl. Math. Comput. 5:235-294"
local_file: "~/papers/mosaic/div-free-amr/2023-CAMC-Balsara-101007s42967-021-00160-3.pdf"
tags: [curl-constraint, mimetic, reconstruction, multidimensional-riemann-solver, weno, involution]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The paper treats PDEs whose involution keeps a vector field curl-free, or
evolves its curl by a given law. Its examples are Godunov–Peshkov–Romenski
(GPR) hyperelasticity and heat conduction, multiphase flow, first-order
CCZ4 relativity and a hyperbolic Schrödinger equation. It designs mimetic
finite-volume "WENO-like" schemes for them on structured meshes:
* the vector's components live on edges;
* the driving potential lives at vertices and is supplied by a
  multidimensional Riemann solver;
* a curl-preserving reconstruction fills the zone interior.

It is the one-degree-down counterpart of divergence-free reconstruction
and CT, merged into
[divergence-free reconstruction](/methods/divergence-free-reconstruction.md)
and [discrete exactness theorems](/results/discrete-exactness-theorems.md).
The PDF read is the open-access published version (received March 2021,
online 2021, in the 2023 volume).

# Key claims

1. **Collocation** (§1.1). In the GPR heat-conduction model the thermal
   impulse $\mathbf J$ obeys
   $\partial_t \mathbf J + \nabla(\mathbf J\cdot\mathbf v + T) + \mathbf v\times(\nabla\times\mathbf J) = $
   a source term. Zero circulation over every face holds discretely only
   if $\mathbf J$ is on edges and the scalar is at vertices. The curl,
   the "Burgers vector" $\mathbf R = \nabla\times\mathbf J$, is then a
   divergence-free face field.
2. **2D reconstruction** (§2).
   * Edge moments come from 1D WENO along the edges.
   * Correction terms that vanish on the edges make the interior
     polynomial exactly curl-free, or matched to a reconstructed
     circulation. This is nonlinear hybridization, inherited from WENO.
   * The construction is given in closed form at orders 2 and 3.
   * At order 4 the edges leave five free parameters and two zone-centred
     modes. They are fixed by least squares against a conventional FV-WENO
     reconstruction, keeping the constraint exact, so no auxiliary system
     is evolved.
3. **3D reconstruction** (§3), to third order. Each zone has six face
   circulation conditions, of which five are independent, against a single
   divergence condition. The curl is reconstructed volumetrically with the
   divergence-free reconstruction of Balsara et al. Then the curl of the
   vector polynomial is matched to it: 12 coefficients at second order and
   36 at third.
4. **Upwinding** (§§2.5, 3.4). With one upwinded potential per vertex,
   the first-order scheme is properly upwinded advection plus
   multidimensional dissipation. Higher order lowers the dissipation. This
   mirrors the Balsara–Käppeli result for the divergence-free induction
   equation.
5. **Von Neumann analysis** (§4, 2D, constant velocity). Maximum CFL
   numbers are 1.150 7 at third order with SSP-RK3 and 1.304 0 at fourth
   order with SSP-RK(5,4). Fourth order cuts dissipation and dispersion by
   about an order of magnitude at 10 or more zones per wavelength, and is
   more isotropic.
6. **Tests** (§§5–6).
   * On a stationary curl-free toy problem: design orders 2 to 4, curl at
     machine precision, and quadratic energy best preserved at fourth
     order.
   * A staggered semi-implicit scheme from the authors' group is the most
     diffusive.
   * Without curl preservation the equilibrium breaks and the code
     eventually blows up.
   * With a prescribed curl source, a zone-centred Godunov scheme has curl
     errors 2–4 orders of magnitude larger.
   * On GPR blasts, its circulation grows unregulated, regardless of the
     relaxation time, and the $\tau = 0.1$ solution differs visibly.

# Notation map

| Balsara et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| edge components $V^x, V^y, V^z$ of $\mathbf J$ | element of $V_h^1$ | curl-constrained vector |
| vertex potential $\phi = \mathbf v\cdot\mathbf J$ (+$T$) | element of $V_h^0$ | from the multidimensional Riemann solver |
| discrete circulation over a face | $C_h$ applied to $V_h^1$ data | |
| curl-free update from vertex potentials | $C_h G_h = 0$ | |
| Burgers vector $\mathbf R = \nabla\times\mathbf J$ | element of $V_h^2$, with $D_h\mathbf R = 0$ | |
| ECCP | edge-centred curl-preserving scheme | paper's name |

# Pages created or updated

* Updated [Divergence-free reconstruction](/methods/divergence-free-reconstruction.md): a section on the curl-constrained counterpart.
* Updated [Discrete exactness theorems](/results/discrete-exactness-theorems.md): $C_h G_h = 0$ as a design principle.

# Citations

1. `~/papers/mosaic/div-free-amr/2023-CAMC-Balsara-101007s42967-021-00160-3.pdf` (doi:10.1007/s42967-021-00160-3): text extraction, all pages including the reference list (55 entries). The closed-form coefficient formulas (§§2–3) were read in outline, and none is reproduced. Figures were read from their captions only.

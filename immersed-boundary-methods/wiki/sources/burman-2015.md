---
type: Source
title: "Burman, Claus, Hansbo, Larson & Massing (2015) — CutFEM: Discretizing geometry and partial differential equations"
description: "Overview of the cut finite element method: unfitted finite elements on a background mesh with level-set geometry, Nitsche imposition of boundary and interface conditions, and ghost-penalty stabilization making accuracy and conditioning independent of the cut; interface, fictitious-domain, Stokes and surface problems, with the libCutFEM implementation on FEniCS."
resource: "doi:10.1002/nme.4823"
source_kind: paper
authors: [Burman E., Claus S., Hansbo P., Larson M.G., Massing A.]
year: 2015
venue: "Int. J. Numer. Methods Eng. 104(7):472-501"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2014_Crossref_International_Journal_for_Numerical_Methods_in_Engineering_Burman_CutFEM_Discretizing_geometry_and_partial_differential_equati.pdf"
tags: [cutfem, finite-element, nitsche, ghost-penalty, level-set, surface-pde]
timestamp: 2026-11-08T18:08:00Z
---

# Summary

Burman, Claus, Hansbo, Larson and Massing review [CutFEM](/methods/cutfem.md),
unfitted finite elements on cut meshes. The geometry lives on a background
mesh, typically as a level set; Nitsche's method imposes boundary and interface
conditions weakly; and ghost-penalty terms on faces of cut elements give
coercivity, optimal error estimates and condition numbers independent of how
the boundary cuts the mesh — the finite-element counterpart of the
[small-cell problem](/definitions/small-cell-problem.md) and its cure. They
cover interface problems with large contrast, fictitious-domain Poisson and
Stokes problems, surface PDEs and bulk–surface coupling, and their
open-source implementation.

# Version read

Version of record (open access), Int. J. Numer. Methods Eng. 104, 472–501,
published online 29 December 2014 in the 2015 volume; the archive file is
named with the online year. §§1–3 read in full, §§4–6 (geometry,
implementation, examples) read in outline. Page-1 title and authors match
Crossref.

# Key claims

1. CutFEM aims at a discretization "as independent as possible of the geometric description" with the accuracy and robustness of standard finite elements, so that CAD or image data can be used without conforming mesh generation (§1). **Stated**
2. In the unfitted Nitsche interface method each cut element carries two sets of basis functions, restrictions to each side, and optimal approximation holds because the trace-inequality constant is independent of the interface position (§2.1). **Derived** (cited Hansbo and Hansbo)
3. Interface weights $|K_i|/|K|$ depend on the cut and are not robust for large coefficient contrast; coefficient-dependent weights fix the contrast but not bad cuts (§2.1, §3). **Derived**
4. In a fictitious domain, arbitrarily small cut elements break the inverse inequality; the ghost penalty on faces of cut elements extends coercivity to the mesh domain and gives cut-independent condition numbers (§2.2, §3). **Proved** (cited analyses)
5. With ghost penalty and suitable weights the system is robust in the perfect-conductor and vanishing-diffusion limits (§3.1–3.2). **Derived**/**Shown**
6. Surface PDEs (Laplace–Beltrami) and coupled bulk–surface problems are discretized on the background mesh with ghost-penalty stabilization (§2–§3). **Derived**
7. The level set is reconstructed piecewise linearly and integrated by sub-triangulation; libCutFEM on FEniCS/DOLFIN implements it (§4–§5). **Stated**
8. Poisson in complex ("popcorn", Olympic rings) geometries, Stokes in a fictitious domain and surface problems illustrate the method (§6). **Shown**

# Notation map

| Burman et al. (2015) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Omega_1$, $\Omega_2$, $\Gamma$ | two sides of $\Gamma$ | |
| $\alpha_i$, $c$ | $\beta$, $\kappa_0$ | diffusion and reaction coefficients |
| $\kappa_i=|K_i|/|K|$ | element volume fractions | same role as the cut-cell $\kappa$ |
| $\phi$ | $\phi$ | level set; agree |
| $\mathcal T_h$, $G_h$, $\mathcal F_G$ | background mesh, cut elements, ghost-penalty faces | |
| $j(\cdot,\cdot)$, $\gamma$ | ghost penalty and its parameter | |

# Reference list

The paper's reference list (about 50 entries) is merged complete into the
[bibliography](/bibliography.md) from the Crossref deposited list (51
entries).

# Pages created or updated

Chunk 2 (2026-11-08), list updated in chunk 3 (2026-11-08). This source is cited on:

- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Small-cell problem](/definitions/small-cell-problem.md)
- [CutFEM (cut finite element method)](/methods/cutfem.md)

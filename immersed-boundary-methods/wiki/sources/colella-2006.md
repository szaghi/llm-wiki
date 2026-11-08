---
type: Source
title: "Colella, Graves, Keen & Modiano (2006) — A Cartesian grid embedded boundary method for hyperbolic conservation laws"
description: "Second-order unsplit Godunov embedded-boundary method that is formally consistent (fluxes interpolated to face centroids, O(h) truncation error at the boundary) and stable for small cut cells by hybridizing conservative and non-conservative updates and redistributing the difference; second order in L1 for smooth flows and robust for strong shocks."
resource: "doi:10.1016/j.jcp.2005.05.026"
source_kind: paper
authors: [Colella P., Graves D.T., Keen B.J., Modiano D.]
year: 2006
venue: "J. Comput. Phys. 211(1):347-366"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/2006_Crossref_Journal_of_Computational_Physics_Colella_A_Cartesian_grid_embedded_boundary_method_for_hyperbolic_con.pdf"
tags: [cut-cell, embedded-boundary, redistribution, small-cell, compressible, godunov]
timestamp: 2026-11-08T18:08:00Z
---

# Summary

Colella, Graves, Keen and Modiano extend the unsplit Godunov method to an
embedded-boundary (cut-cell) representation of irregular domains
([cut-cell method](/methods/cut-cell-method.md)). Interpolating face fluxes
to the face centroids makes the discretization formally consistent: $O(h)$
truncation error near the boundary instead of the $O(1)$ of earlier methods.
The [small-cell problem](/definitions/small-cell-problem.md) is solved by a
hybrid of the conservative and a non-conservative divergence weighted by the
volume fraction, with the resulting mass defect redistributed to neighbours
([redistribution](/methods/redistribution.md)), keeping local conservation
([discrete conservation](/properties/discrete-conservation.md)). A
modified-equation argument explains the observed second order in $L^1$ and
first order in $L^\infty$; strong-shock problems show robustness
([shock–obstacle interaction](/benchmarks/shock-obstacle-interaction.md)).

# Version read

An author preprint (LBNL layout, no journal header or page numbers), with
title, authors and abstract identical to the published paper in Crossref;
claims are those of the version read. Method sections read in full,
convergence tables and the shock examples read for their conclusions. The
text layer garbles most display equations; the hybrid update and the
redistribution formula are reconstructed from the prose (see
[redistribution](/methods/redistribution.md)). No section numbers are
printed in the text layer for the subsections; the paper's main parts are
cited as §1 (introduction), §2 (geometry, stable evolution, redistribution),
§3 (flux computation), §4–§5 (results).

# Key claims

1. The method is formally consistent: $O(h)$ truncation error at the embedded boundary and $O(h^2)$ inside, giving $O(h^2)$ error in $L^1$ and $O(h)$ in $L^\infty$, unlike earlier formally inconsistent methods with $O(1)$ boundary truncation errors (§1). **Stated**/**Shown**
2. An explicit conservative update is limited to $\Delta t=O(h\,\kappa_{\max}^{1/D}/v)$, the small-cell problem (§2). **Stated**
3. Hybridizing conservative and non-conservative divergences with weight $\kappa$ cancels the small denominator; redistributing the mass defect to neighbours with weights summing appropriately keeps local conservation; weights must be bounded independently of $1/\kappa$ (§2). **Derived**
4. Mass-weighted redistribution is more robust than volume weighting for strong shocks (§2, citing Pember et al.). **Stated** (cited)
5. Interpolating fluxes to face centroids (linear in 2-D, bilinear in 3-D) gives the consistent conservative divergence (§2). **Derived**
6. A modified-equation analysis predicts $O(h^2)$ solution error for non-characteristic boundaries and $O(h)$ error concentrated at characteristic ones, hence second order in $L^1$, $O(h^{3/2})$ in $L^2$ and first order in $L^\infty$ (§2). **Derived**
7. The non-conservative divergence, which dominates in small cells, must make a small cell relax to a locally constant state around it; covered-face states are extrapolated along the boundary normal with limited slopes (§3). **Stated**
8. Smooth 2-D and 3-D problems: truncation error first order in $L^\infty$ and second in $L^1$; solution error second order in $L^1$, intermediate in other norms (§4). **Shown**
9. Strong shocks interacting with the embedded boundary (shock reflection from a ramp) are computed robustly (§5). **Shown**

# Notation map

| Colella et al. (2006) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\kappa_{\mathbf i}$ | $\kappa_{\mathbf i}$ | volume fraction; agree |
| $\alpha_{\mathbf i\pm\frac12\mathbf e_d}$ | $a_{\mathbf i\pm\frac12\mathbf e_m}$ | apertures; $\alpha$ reserved |
| $\mathbf U$, $\vec F$ | $\mathbf q$, $\boldsymbol{\mathcal F}$ | conserved variables, flux |
| $(\nabla\cdot\vec F)^C$, $(\nabla\cdot\vec F)^{NC}$ | same with $\boldsymbol{\mathcal F}$ | |
| $\eta_{\mathbf i}$ (hybrid weight) | $\kappa_{\mathbf i}$ (the choice made) | $\eta$ is the penalty parameter in the registry |
| $\delta M_{\mathbf i}$, $w_{\mathbf i,\mathbf i'}$ | $\delta\mathbf M_{\mathbf i}$, $w_{\mathbf i\mathbf j}$ | |
| $D$ | $d$ | dimension |
| $W$ | primitive variables, page-local | |

# Reference list

19 references, merged complete into the [bibliography](/bibliography.md)
from the Crossref deposited list.

# Pages created or updated

Chunk 2 (2026-11-08), list updated in chunk 3 (2026-11-08). This source is cited on:

- [Shock–obstacle interaction](/benchmarks/shock-obstacle-interaction.md)
- [Small-cell problem](/definitions/small-cell-problem.md)
- [Cut-cell (embedded-boundary) finite-volume method](/methods/cut-cell-method.md)
- [Flux redistribution for cut cells](/methods/redistribution.md)
- [Discrete conservation](/properties/discrete-conservation.md)

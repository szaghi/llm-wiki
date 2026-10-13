---
type: Source
title: "Clemens & Weiland (2001) — Discrete electromagnetism with the finite integration technique"
description: "Review of FIT: Maxwell's integral equations become exact topological matrix equations on a primal-dual grid doublet, with all discretization error confined to the material (Hodge) matrices."
resource: "doi:10.2528/PIER00080103"
source_kind: paper
authors: [Clemens M., Weiland T.]
year: 2001
venue: "Progress In Electromagnetics Research (PIER) 32:65-87"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2001-PIER-Clemens-102528PIER00080103.pdf"
tags: [fit, electromagnetics, dual-grid, hodge, maxwell, conservation]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Review of Weiland's **Finite Integration Technique** (FIT, 1977): Maxwell's
equations in integral form are discretized on a **grid doublet**
$\{G, \tilde G\}$ — a primal cell complex and its dual (cell foci or
barycenters as dual vertices, one-to-one edge–face pairing). Electric grid
voltages live on primal edges, magnetic facet fluxes on primal faces;
magnetomotive forces on dual edges, dielectric fluxes/currents on dual
faces, charges in dual cells. The resulting **Maxwell-Grid-Equations
(MGE)** involve only incidence matrices and are *exact*; conservation of
charge and energy is provable algebraically before any computation
([method page](/methods/finite-integration-technique.md)).

# Key claims

1. **Topology/metric split, sharpest form**: the MGE
   ($\mathsf{C}\,\hat e = -\tfrac{d}{dt}\hat b$, $\mathsf{S}\,\hat b = 0$,
   plus dual-grid Ampère/Gauss with $\tilde{\mathsf{C}}, \tilde{\mathsf{S}}$)
   contain **only topological information** and hold exactly; "the
   discretization error is found to be located in the discrete constitutive
   material equations."
2. **Material matrices are discrete Hodge operators**: they couple primal
   and dual degrees of freedom (1-forms to 2-forms), carrying all metric
   and material content — diagonal on orthogonal Cartesian doublets,
   symmetric but non-diagonal for the nonorthogonal variant (N-FIT), and
   *the same objects* as edge-FE mass matrices computed by Whitney-form
   quadrature ([Whitney forms](/definitions/whitney-forms.md)).
3. **Algebraic stability dividends**: the exact algebraic identities of
   the discrete operators explain long-term-stable time integration and
   spurious-mode-free eigenvalue solvers — structural properties, not
   tuning.
4. **Priority note, as stated by the authors**: the differential-forms /
   algebraic-topology formulations of lattice electromagnetism "closely
   resemble (or paraphrase)" FIT formulations "already established for
   more than 20 years."

# Notation map

| Clemens & Weiland | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathsf{C}, \mathsf{S}$ (coefficients in $\{-1,0,1\}$) | combinatorial parts of $C_h, D_h$ | primal incidence matrices; $\tilde{\mathsf{C}}, \tilde{\mathsf{S}}$ dual |
| $\hat e$ (edge voltages), $\hat b$ (facet fluxes) | $E_h \in V_h^1$, $B_h \in V_h^2$ | integral DOFs |
| material matrices $M_\epsilon, M_\mu, M_\kappa$ | discrete Hodge operators | all metric/material content; all error |
| grid doublet $\{G, \tilde G\}$ | primal–dual complex pair | the EM face of staggering |

# Pages created or updated

* Created [Finite integration technique (FIT)](/methods/finite-integration-technique.md).
* Updated [Whitney forms](/definitions/whitney-forms.md) (FIT material matrices = edge-FE mass matrices).

# Citations

1. `~/papers/mosaic/div-free-amr/2001-PIER-Clemens-102528PIER00080103.pdf` (doi:10.2528/PIER00080103) — text extraction, pp. 65–87.

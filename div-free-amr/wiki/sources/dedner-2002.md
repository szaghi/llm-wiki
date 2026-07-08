---
type: Source
title: "Dedner et al. (2002) — Hyperbolic divergence cleaning for the MHD equations"
description: "Introduces GLM-MHD: the divergence constraint coupled through a generalized Lagrange multiplier, with divergence errors transported at finite speed and damped."
resource: "doi:10.1006/jcph.2001.6961"
source_kind: paper
authors: [Dedner A., Kemm F., Kröner D., Munz C.-D., Schnitzer T., Wesenberg M.]
year: 2002
venue: "J. Comput. Phys. 175:645-673"
local_file: "~/papers/mosaic/div-free-amr/2002-JCP-Dedner-101006jcph20016961.pdf"
tags: [glm, divergence-cleaning, hyperbolic, lagrange-multiplier, finite-volume]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Introduces the **generalized Lagrange multiplier (GLM) formulation of MHD**
([method page](/methods/glm-divergence-cleaning.md)), transplanting the
Munz et al. GLM–Maxwell construction: the constraint is coupled to the
induction equation through a new scalar $\psi$,
$$\partial_t \mathbf{B} + \nabla\cdot(u B^T - B u^T) + \nabla\psi = 0,
\qquad \mathcal{D}(\psi) + \nabla\cdot\mathbf{B} = 0,$$
where the choice of the linear operator $\mathcal{D}$ generates the whole
cleaning family. The recommended *mixed* correction makes divergence errors
obey a telegraph equation — transported to the boundary at the maximal
admissible speed and damped en route. The corrected system is hyperbolic,
still conserves $\rho, \rho u, \mathbf{B}, e$, and installs as an **add-on
to any existing MHD solver** — local, explicit, any grid.

# Key claims

1. **The family in one operator** (their §2): $\mathcal{D}(\psi) = 0$ →
   *elliptic* correction, which is exactly the Brackbill–Barnes
   [projection](/methods/projection-method.md), rediscovered;
   $\mathcal{D} = \psi/c_p^2$ → *parabolic* (Marder-type diffusion of
   divergence); $\mathcal{D} = \partial_t\psi/c_h^2$ → *hyperbolic*
   ($\psi$ and $\nabla\cdot\mathbf{B}$ obey a wave equation, errors leave at
   finite speed $c_h$); $\mathcal{D} = \partial_t\psi/c_h^2 + \psi/c_p^2$ →
   *mixed* (telegraph equation: transport **and** damping). For every
   choice, $\nabla\cdot\mathbf{B}$ and $\psi$ satisfy the same equation.
2. **Conservation is kept**: the only source term sits in the equation for
   the unphysical $\psi$ — unlike the
   [eight-wave](/methods/eight-wave.md) source terms, the physical
   conservation laws are untouched, so the Lax–Wendroff jump-condition risk
   does not arise.
3. **Hyperbolicity**: the 9-variable GLM–MHD system (primitive vector
   including $\psi$) is diagonalizable with real eigenvalues; the cleaning
   waves travel at $\pm c_h$, decoupled from the MHD eigensystem.
4. **No stability tax for damping**: in the mixed correction the damping is
   a source term, so $c_p$ carries no CFL-type restriction; $c_p \to \infty$
   recovers the purely hyperbolic variant.
5. **Empirical claim**: versus no correction and versus the Powell source
   terms, GLM yields "more robust schemes with significantly smaller
   divergence errors"; comparison with projection/CT is explicitly deferred
   to [Tóth (2000)](/sources/toth-2000.md), since the design goal is
   add-on locality on arbitrary grids, not maximal constraint strength.

# Notation map

| Dedner et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\psi$ | $\psi_h$ (cleaning scalar) | unphysical multiplier field |
| $\mathcal{D}$ | — | operator selecting the cleaning family; no registry symbol (named inline) |
| $c_h$, $c_p$ | cleaning wave speed / damping parameter | $c_h$ finite, grid-maximal |
| $\nabla\cdot\mathbf{B}$ cell values | $D_h^{\mathrm{c}}$-type evaluations | constraint controlled, never held exactly |

# Pages created or updated

* Created [GLM divergence cleaning](/methods/glm-divergence-cleaning.md).
* Updated [Eight-wave formulation](/methods/eight-wave.md) (conservation contrast; robustness comparison).
* Updated [Projection method](/methods/projection-method.md) (GLM elliptic limit).

# Citations

1. `~/papers/mosaic/div-free-amr/2002-JCP-Dedner-101006jcph20016961.pdf` (doi:10.1006/jcph.2001.6961) — text extraction, pp. 645–673.

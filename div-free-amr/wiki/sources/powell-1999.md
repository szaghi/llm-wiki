---
type: Source
title: "Powell et al. (1999) — A solution-adaptive upwind scheme for ideal magnetohydrodynamics"
description: "Primary formulation of the eight-wave scheme: MHD solved in Godunov's symmetrizable form with source terms, the divergence advected as a passive scalar."
resource: "doi:10.1006/jcph.1999.6299"
source_kind: paper
authors: [Powell K.G., Roe P.L., Linde T.J., Gombosi T.I., De Zeeuw D.L.]
year: 1999
venue: "J. Comput. Phys. 154:284-309"
local_file: "~/papers/mosaic/div-free-amr/1999-JCP-Powell-101006jcph19996299.pdf"
tags: [eight-wave, symmetrizable, riemann-solver, godunov, adaptive, space-physics]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The primary presentation of the **eight-wave scheme**
([method page](/methods/eight-wave.md)): ideal MHD is solved in its
*symmetrizable* form — Godunov's observation that the pure divergence form
is not symmetrizable, and becomes so exactly when a multiple of
$\nabla\cdot\mathbf{B}$ is added to each equation. The resulting source
terms make $\nabla\cdot\mathbf{B}/\rho$ a passively advected scalar, and the
Roe-type approximate Riemann solver acquires an eighth wave (the divergence
wave, speed $u$). Around this core the paper builds a complete explicit,
high-resolution, solution-adaptive finite-volume MHD code — limited
reconstruction, optimally smoothing multi-stage time stepping, adaptive
refinement/coarsening — validated against exact solutions and applied to 3D
solar-wind/magnetosphere interaction, aided by splitting off an embedded
steady field $\mathbf{B}_0$ ("$B_0 - B_1$ splitting") for accuracy near a
strong dipole.

# Key claims

1. **Symmetrizability requires the source terms** (their §2, after
   Godunov): without them the system is not symmetrizable, is not Galilean
   invariant, has a zero eigenvalue in the flux Jacobian, and admits no
   entropy conservation law; with them all waves propagate at $u \pm c$ and
   the entropy equation follows.
2. **The divergence is passively advected** (their eqs. 26–27):
   $\partial_t(\nabla\cdot\mathbf{B}) + \nabla\cdot(\mathbf{u}\,\nabla\cdot\mathbf{B}) = 0$,
   so with clean initial and boundary data the constraint holds along
   particle paths — to truncation error, "even for long integration times."
   Acknowledged ambiguity: isolated recirculating regions cut off from
   boundaries (which do occur in their 3D runs).
3. **Discrete realization**: cell-averaged source
   $S_i \propto (\nabla\cdot B)_i$ with the cell divergence computed as the
   face integral $\frac{1}{V_i}\sum_{\text{faces}} \mathbf{B}\cdot\hat{n}\,dS$;
   midpoint quadrature; eight-wave Roe solver with the Roe–Balsara
   eigenvector normalization.
4. **The trade is stated openly**: the source terms break exact
   conservation; the authors weigh local conservation errors against the
   defective character of the unmodified system and choose
   symmetrizability. (The failure mode this trade admits — incorrect jump
   conditions at strong shocks, not converging away with resolution — was
   demonstrated by [Tóth (2000)](/sources/toth-2000.md) §6.3.)
5. **Constraint-approach taxonomy** (their §1): Hodge
   [projection](/methods/projection-method.md), staggered
   [constrained transport](/methods/constrained-transport.md), hybrid
   CT–Godunov schemes ([flux-CT](/methods/flux-ct.md)), and their
   symmetrizable-form alternative — the same three-family split later
   systematized by Tóth.

# Notation map

| Powell et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $B_x, B_y, B_z$ cell-centered | $B_h$, cell-collocated | finite-volume averages |
| $(\nabla\cdot B)_i$ via face integral | $D_h^{\mathrm{f}}$-type face sum evaluated per cell | used only in the source term, not as a held invariant |
| $S \propto \nabla\cdot\mathbf{B}$ | eight-wave source terms | momentum, induction, energy rows |
| $\mathbf{B} = \mathbf{B}_0 + \mathbf{B}_1$ | embedded-field splitting | steady $\mathbf{B}_0$ subtracted analytically |

# Pages created or updated

* Updated [Eight-wave formulation](/methods/eight-wave.md) (primary grounding: symmetrizable form, divergence wave, discrete source term).

# Citations

1. `~/papers/mosaic/div-free-amr/1999-JCP-Powell-101006jcph19996299.pdf` (doi:10.1006/jcph.1999.6299) — text extraction, pp. 284–309.

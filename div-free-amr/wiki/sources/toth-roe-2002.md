---
type: Source
title: "Tóth & Roe (2002) — Divergence- and curl-preserving prolongation and restriction formulas"
description: "Second-order prolongation/restriction preserving discrete divergence (and sometimes curl) at 2:1 interfaces, for staggered and vertex-collocated storage; locality fails beyond staggering."
resource: "doi:10.1006/jcph.2002.7120"
source_kind: paper
authors: [Tóth G., Roe P.L.]
year: 2002
venue: "J. Comput. Phys. 180:736-750"
local_file: "~/papers/mosaic/div-free-amr/2002-JCP-Toth-101006jcph20027120.pdf"
tags: [amr, prolongation, restriction, divergence-constraint, curl-preserving, collocation]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Constructs second-order **prolongation and restriction formulas preserving
the discrete divergence** (and, in some cases, the curl) of a vector field
at factor-of-2 resolution changes on 2D/3D Cartesian grids — examining
**both staggered and collocated** storage. The central finding is a
locality trichotomy ([Result page](/results/transfer-operator-locality-limits.md)):
face-centered staggered storage admits *local* divergence-preserving
prolongation and restriction; vertex-based collocated storage admits local
prolongation but only *global* restriction; cell-centered collocated
storage "does not seem to lend itself" to either locally. Conclusion,
verbatim: "This suggests the use of face-centered storage for AMR schemes
which require the divergence-free property." Validated in BATSRUS on a 3D
Kelvin–Helmholtz AMR run: divergence zero to machine precision through six
regriddings.

# Key claims

1. **Face-staggered transfer operators** (§3): restriction = flux summation
   satisfying $\Omega D = \sum \omega\, d^{i,j,k}$ — exactly the
   commutation $D_H R = R\, D_h$; prolongation = limited linear
   interpolation on coarse faces plus interior components fixed by equating
   the eight fine-cell divergences to $\tfrac18$ of the coarse one;
   second-order accurate, curl-preserving variants given. Working with
   *fluxes* rather than field components makes the formulas aspect-ratio
   clean. Second construction of
   [$P_D$](/operators/divergence-free-prolongation.md), independent of
   Balsara's polynomial route.
2. **Vertex-collocated storage** (§4): a local divergence-preserving
   prolongation exists — but for a divergence defined with tangential
   averaging of face fluxes, *not* the naive central difference; local
   restriction is argued impossible (every coarse-corner component is
   shared by seven neighboring fine cells), and only global (multigrid-
   style) restriction survives — usable for multigrid, "but not in the
   adaptive mesh refinement context."
3. **Cell-centered collocated storage**: dismissed for local
   divergence-preserving transfer (divergence/curl stencils reach into
   neighbor cells of different resolution); global projection remains the
   general fallback, including for initializing divergence-free data.
4. **Continuous divergence-free interpolation** (§3.3, eqs. 13): low-order
   polynomials matching the discrete formulas, continuous in the normal
   component but with an **unavoidable transverse discontinuity** at cell
   boundaries (decaying at second order) — flux conservation forbids a
   perfect match at this polynomial order. Useful for field-line tracing.
5. **AMR practice**: alongside these operators BATSRUS retains eight-wave,
   parabolic control, and projection as divergence-control options — the
   transfer operators solve the *regridding* part of the problem, not the
   evolution part.

# Notation map

| Tóth & Roe | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U, V, W$ / $u, v, w$ (fluxes) | coarse/fine face data in $V_H^2$ / $V_h^2$ | field components pre-multiplied by face areas |
| $D$, $d^{i,j,k}$ (eqs. 1–2) | $D_H$, $D_h$ ($\mathrm{f}$-stencil) | |
| $\Omega D = \sum \omega d$ | $D_H R = R\, D_h$ | restriction commutation, in flux form |
| prolongation of §3.2 | $P_D$ | with curl-preserving variants |
| vertex-based $D$ (eq. 23–24) | tangentially-averaged divergence | *not* $D_h^{\mathrm{c}}$; bespoke stencil enabling collocated prolongation |

# Pages created or updated

* Created [Locality limits of divergence-preserving transfer](/results/transfer-operator-locality-limits.md).
* Updated [Divergence-space prolongation $P_D$](/operators/divergence-free-prolongation.md) (second construction; curl-preserving variants).
* Updated [Divergence-free reconstruction](/methods/divergence-free-reconstruction.md) (continuous interpolation; unavoidable transverse discontinuity).
* Updated [CT–finite-volume equivalence](/results/ct-finite-volume-equivalence.md) (`Contradictions` development: Tóth's own 2002 recommendation of face-centered storage for AMR).

# Citations

1. `~/papers/mosaic/div-free-amr/2002-JCP-Toth-101006jcph20027120.pdf` (doi:10.1006/jcph.2002.7120) — text extraction, pp. 736–750.

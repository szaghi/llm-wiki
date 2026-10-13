---
type: Source
title: "Almgren, Bell, Colella, Howell & Welcome (1998) — A conservative adaptive projection method for the variable density incompressible Navier-Stokes equations"
description: "Projection-method AMR with subcycling: MAC-projected advection velocities, approximate nodal projections, and a four-mismatch elliptic synchronization suite at coarse-fine interfaces."
resource: "doi:10.1006/jcph.1998.5890"
source_kind: paper
authors: [Almgren A.S., Bell J.B., Colella P., Howell L.H., Welcome M.L.]
year: 1998
venue: "J. Comput. Phys. 142:1-46"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1998-JCP-Almgren-101006jcph19985890.pdf"
tags: [amr, projection, incompressible, subcycling, synchronization, free-stream]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The IAMR-lineage paper: variable-density incompressible Navier–Stokes on a
[Berger–Colella hierarchy](/definitions/block-structured-amr.md) with
subcycling, built on the *approximate projection* formulation
([method page](/methods/amr-projection-method.md)). Each step: Godunov
advection–diffusion with face-based advection velocities made
divergence-free at the half time by an intermediate **MAC projection**;
conservative flux-form updates; then a **node-based approximate projection**
of the cell-centered velocity at the end of the step. The adaptive emphasis
is the **synchronization suite**: the recursive subcycled advance leaves
four identified mismatches at coarse–fine interfaces, each repaired by its
own (mostly elliptic) correction. Designed as a substrate for general
low-Mach models (anelastic, combustion) where conservation and
[free-stream preservation](/properties/free-stream-preservation.md) of
scalars are load-bearing.

# Key claims

1. **Two projections per step, different collocations**: the MAC projection
   acts on face-normal advection velocities — the exact
   $D_h^{\mathrm{f}}$-stencil constraint of the
   [MAC method](/methods/mac-method.md) — while the end-of-step projection
   acts on cell-centered velocities with node-based pressure and is
   **approximate**: the projected field satisfies the constraint only to
   the discretization/solver accuracy of the non-compact stencil.
2. **The four mismatches** (§3): (M.1) fine data must replace coarse
   (averaging down); (M.2) coarse vs time-averaged fine *advection
   velocities* disagree at the interface — repaired by an elliptic "MAC
   sync solve" whose gradient re-advects level data; (M.3) hyperbolic flux
   mismatch — classical [refluxing](/methods/refluxing.md), but with
   *elliptic* refluxing solves when viscosity/diffusivity is present
   (corrections enter Crank–Nicolson right-hand sides); (M.4) the level
   projections enforce only Dirichlet matching — a composite two-level
   nodal **sync projection** repairs the Neumann residual. Corrections from
   (S.2)–(S.3) are themselves not divergence-free and are projected before
   application.
3. **Skipping elliptic synchronization costs accuracy** — documented here
   and in the cited anelastic literature: two-way nesting without the
   elliptic matching conditions loses accuracy at interfaces.
4. **Free-stream preservation as a design requirement**: constant scalar
   fields with no sources remain constant *independent of the refinement
   pattern and velocity field* — a property engineered via conservative
   advection with MAC-projected velocities plus the synchronization suite.
5. **Positioning**: unlike its nonconservative predecessors, conservation
   holds grid-by-grid; unlike single-rate AMR (Minion), all levels run at
   their own CFL-optimal step.

# Notation map

| Almgren et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U, \rho, c$ cell-centered; $p$ node-based, time-staggered | $u_h$ cell-collocated; $\phi_h$ nodal | approximate-projection collocation |
| MAC-projected face velocities | $u_h$ face-collocated with $D_h^{\mathrm{f}} u_h = 0$ | intermediate advection field |
| $D^{E\to C}, G^{C\to E}$ | $D_h^{\mathrm{f}}, G_h$ pair (face/cell) | MAC solve operators |
| $\delta U^\ell$ velocity registers | interface mismatch accumulators | analog of refluxing registers for face velocities |
| "sync projection" | composite two-level nodal projection | repairs elliptic matching at interfaces |

# Pages created or updated

* Created [AMR projection method](/methods/amr-projection-method.md).
* Created [Free-stream preservation](/properties/free-stream-preservation.md).
* Updated [MAC method](/methods/mac-method.md) (reuse as intermediate projection).
* Updated [Refluxing](/methods/refluxing.md) (elliptic generalization).
* Updated [Projection method](/methods/projection-method.md) (AMR realization pointer).

# Citations

1. `~/papers/mosaic/div-free-amr/1998-JCP-Almgren-101006jcph19985890.pdf` (doi:10.1006/jcph.1998.5890) — text extraction, pp. 1–46.

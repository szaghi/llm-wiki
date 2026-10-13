---
type: Source
title: "Hyman & Shashkov (1997) — Natural discretizations for the divergence, gradient, and curl on logically rectangular grids"
description: "Builds discrete vector analysis on nonorthogonal logically rectangular grids: natural DIV/GRAD/CURL from coordinate-invariant definitions, with discrete exactness theorems including converses."
resource: "doi:10.1016/S0898-1221(97)00009-6"
source_kind: paper
authors: [Hyman J.M., Shashkov M.]
year: 1997
venue: "Comput. Math. Appl. 33(4):81-104"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1997-CMA-Hyman-101016S0898122197000096.pdf"
tags: [mimetic, support-operator, discrete-vector-analysis, logically-rectangular, curvilinear]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

First of the Hyman–Shashkov series constructing a **discrete vector
analysis** on logically rectangular, *nonorthogonal, nonsmooth* grids.
Defines the discretization spaces (cell and nodal scalars; vector fields by
face-normal and edge-tangential components), the **natural** discrete
divergence (from Gauss's theorem), curl (from Stokes's theorem), and
gradient (edge differences), together with discrete volume/surface/line
integrals — then proves discrete versions of the main theorems of vector
analysis, **including the converses** (exactness, not just composition
identities). The operators factor into purely combinatorial difference
operators and purely metric operators (edge lengths, face areas, volumes),
separating topology from geometry. Deliberately formulated in advanced-
calculus language rather than algebraic topology, for the scientific-
computing audience — while acknowledging the differential-forms lineage.

# Key claims

1. **Natural spaces and operators**: scalars in $HC$ (cell) and $HN$
   (nodal); vectors in $\mathcal{HS}$ (face-normal components) and
   $\mathcal{HL}$ (edge-tangential components). Natural operators:
   $\mathbf{GRAD}: HN \to \mathcal{HL}$,
   $\mathbf{CURL}: \mathcal{HL} \to \mathcal{HS}$,
   $\mathbf{DIV}: \mathcal{HS} \to HC$ — coordinate-invariant definitions
   valid on nonorthogonal, nonsmooth grids.
2. **Discrete exactness with converses**
   ([Result page](/results/discrete-exactness-theorems.md)):
   $\mathbf{DIV}\,\vec A = 0$ **iff** $\vec A = \mathbf{CURL}\,\vec B$;
   $\mathbf{CURL}\,\vec A = 0$ **iff** $\vec A = \mathbf{GRAD}\,\varphi$;
   line integrals of gradients are path-independent, and closed-path-zero
   circulation implies gradient form.
3. **Support-operator method**
   ([definition page](/definitions/support-operator-method.md)): a *prime*
   operator is discretized to satisfy its integral identity (e.g. DIV from
   Gauss); *derived* operators are defined as adjoints (GRAD :=
   $-\mathbf{DIV}^{*}$) — announced here, developed in the sequel, because
   the natural operators alone have mismatched domains/ranges and cannot
   form div grad, grad div, curl curl.
4. **Topology–metric factorization**: DIV, GRAD, CURL decompose into
   primitive forward/backward differences (combinatorial) composed with
   primitive metric multiplications (lengths, areas, volumes) — the
   finite-difference mirror of "incidence matrices plus Hodge star."

# Notation map

| Hyman & Shashkov | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $HN$, $HC$ | $V_h^0$, $V_h^3$ | nodal / cell scalars |
| $\mathcal{HL}$, $\mathcal{HS}$ | $V_h^1$, $V_h^2$ | edge-tangential / face-normal components |
| $\mathbf{GRAD}, \mathbf{CURL}, \mathbf{DIV}$ | $G_h, C_h, D_h$ | the natural (prime) instances |
| $\mathbf{DIV}\,\mathbf{CURL} = 0$ etc. | $D_h C_h = 0$, $C_h G_h = 0$ | plus converses — see Result page |
| adjoint/derived operators | — | sequel paper; not yet in registry |

# Pages created or updated

* Created [Discrete exactness theorems](/results/discrete-exactness-theorems.md).
* Created [Support-operator method](/definitions/support-operator-method.md).

# Citations

1. `~/papers/mosaic/div-free-amr/1997-CMA-Hyman-101016S0898122197000096.pdf` (doi:10.1016/S0898-1221(97)00009-6) — text extraction, pp. 81–104.

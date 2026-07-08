---
type: Source
title: "Etienne, Paschalidis, Haas, Mösta & Shapiro (2015) — IllinoisGRMHD: an open-source, user-friendly GRMHD code for dynamical spacetimes"
description: "Open-source consolidation of the vector-potential GRMHD scheme with the damped generalized Lorenz gauge; roundoff-identical to the original code at twice the speed."
resource: "doi:10.1088/0264-9381/32/17/175009"
source_kind: paper
authors: [Etienne Z.B., Paschalidis V., Haas R., Mösta P., Shapiro S.L.]
year: 2015
venue: "Class. Quantum Grav. 32:175009 (arXiv:1501.07276)"
local_file: "~/papers/mosaic/div-free-amr/2015-CQG-Etienne-1010880264938132175009.pdf"
tags: [vector-potential, gauge, grmhd, amr, production-code, open-source]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The open-source consolidation of the Illinois
[vector-potential GRMHD](/methods/vector-potential-evolution.md) line:
ground-up rewrite for community adoption (modularity, documentation,
maintainability), producing **roundoff-precision identical output** to the
original closed-source code on adaptive-mesh grids at nearly twice the
speed on hundreds-to-thousands of cores. Staggered $A_i$/$B^i$ as in the
2010 scheme, constructed to reproduce staggered CT exactly on uniform
grids.

# Key claims

1. **Generalized Lorenz gauge, damped**: the default gauge is
   $\nabla_\mu A^\mu = \xi\, n_\mu A^\mu$ with damping parameter
   $\xi \sim 1.5/\Delta t_{\max}$ (coarsest-level timestep, CFL-limited) —
   the Lorenz cure of [Etienne et al. (2012)](/sources/etienne-2012.md)
   plus exponential damping of the gauge sector, the gauge-field analog of
   [GLM's](/methods/glm-divergence-cleaning.md) mixed
   transport-plus-damping design.
2. **The monopole contrast drawn explicitly**: the competing open-source
   GRHydro "has not been developed to forbid the generation of monopoles
   … when magnetized fluids flow across AMR grid boundaries" — interface
   constraint integrity named as the differentiator among production
   GRMHD codes.
3. **Reproducibility as a design goal**: bitwise-identical AMR output
   across the rewrite — regression discipline rare in this literature.

# Notation map

| IllinoisGRMHD | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| staggered $A_i$, $B^i$ | $V_h^1$, $V_h^2$ | as Etienne 2010 |
| $[\sqrt{\gamma}\Phi]$, $\xi$ | gauge scalar and damping rate | generalized Lorenz sector |

# Pages created or updated

* Updated [Vector-potential evolution](/methods/vector-potential-evolution.md) (damped generalized Lorenz gauge; production consolidation).

# Citations

1. `~/papers/mosaic/div-free-amr/2015-CQG-Etienne-1010880264938132175009.pdf` (doi:10.1088/0264-9381/32/17/175009) — text extraction, 37 pp.

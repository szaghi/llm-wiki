---
type: Source
title: "Perot (2011) — Discrete conservation properties of unstructured mesh schemes"
description: "Review distinguishing primary from secondary conservation: derived-quantity invariants are harder, materially improve fidelity, and depend on formulation more than discretization family."
resource: "doi:10.1146/annurev-fluid-122109-160645"
source_kind: paper
authors: [Perot J.B.]
year: 2011
venue: "Annu. Rev. Fluid Mech. 43:299-318"
local_file: "~/papers/mosaic/div-free-amr/2011-AnnRevFluidMech-Perot-101146annurev-fluid-122109-160645.pdf"
tags: [conservation, secondary-conservation, unstructured, discrete-calculus, review]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Review organizing discrete conservation into a two-tier taxonomy
([property page](/properties/secondary-conservation.md)): **primary**
conservation (the scheme's own unknowns — mass, momentum, energy; local
conservation "often follows from global"), possessed by most flux-based
methods irrespective of flux approximation; and **secondary** conservation
(derived quantities — kinetic energy, entropy, vorticity, dilatation),
which is "typically much harder to achieve" yet materially improves
physical fidelity. Surveys mechanisms across method families (flux-based,
discrete-calculus/staggered, variational), including conservation on
moving/distorting subdomains without ALE remap.

# Key claims

1. **Secondary conservation is where fidelity lives**: the carbuncle
   phenomenon traces to entropy violation; kinetic-energy conservation is
   critical for the turbulent cascade; vorticity conservation matters in
   turbulence and shallow-water flows — invariants that are not unknowns
   govern solution quality.
2. **A subset of every family**: each major discretization approach
   contains a sub-family with extra conservation properties (his Venn
   diagram) — structure-preservation is orthogonal to the FD/FV/FE split.
3. **Formulation over discretization**: the closing analysis suggests
   secondary conservation "is not directly related to any particular
   discretization method, but … to how the problem is formulated" — and
   might be arranged to hold *automatically*.

# Notation map

| Perot | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| primary/secondary conservation | — | taxonomy adopted at the property page |
| discrete calculus methods | staggered/complex-based schemes | Perot's umbrella term |

# Pages created or updated

* Created [Secondary conservation](/properties/secondary-conservation.md).

# Citations

1. `~/papers/mosaic/div-free-amr/2011-AnnRevFluidMech-Perot-101146annurev-fluid-122109-160645.pdf` (doi:10.1146/annurev-fluid-122109-160645) — text extraction, pp. 299–318.

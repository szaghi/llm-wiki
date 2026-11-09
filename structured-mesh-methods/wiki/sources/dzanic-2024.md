---
type: Source
title: "Dzanic, Mittal, Kim, Yang, Petrides, Keith & Anderson (2024) — DynAMO: Multi-agent reinforcement learning for dynamic anticipatory mesh optimization with applications to hyperbolic conservation laws"
description: "Multi-agent reinforcement learning of local refinement policies that anticipate future solution states, as a decentralized partially observable Markov decision process, for discontinuous Galerkin solutions of hyperbolic problems."
resource: "doi:10.1016/j.jcp.2024.112924"
source_kind: paper
authors: [Dzanic T., Mittal K., Kim D., Yang J., Petrides S., Keith B., Anderson R.]
year: 2024
venue: "J. Comput. Phys. 506:112924"
local_file: "/home/stefano/papers/mosaic/structured-mesh/2024_Crossref_Journal_of_Computational_Physics_Dzanic_DynAMO_Multi-agent_reinforcement_learning_for_dynamic_antici.pdf"
tags: [reinforcement-learning, adaptation, discontinuous-galerkin]
timestamp: 2026-11-08T21:01:00Z
---

# Summary

Dzanic et al. learn anticipatory refinement policies by multi-agent reinforcement learning ([reinforcement-learning meshing](/methods/reinforcement-learning-meshing.md)).

# Version read

arXiv:2310.01695v2 (9 March 2024, preprint submitted to Elsevier); metadata from the version of record, J. Comput. Phys. 506, 112924 (2024). Abstract, §1 and §3 by structure read; experiments in outline.

# Key claims

1. Instantaneous error indicators make adapted meshes suboptimal at later times (§1). **Stated**
2. Learned anticipatory policies outperform threshold-based refinement and generalize across mesh sizes, remesh intervals, times and initial conditions (§5). **Shown**

# Notation map

| Dzanic, Mittal, Kim, Yang, Petrides, Keith & Anderson (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| Dec-POMDP | decentralized partially observable Markov decision process |  |

# Reference list

51 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 5 (2026-11-08). This source is cited on:

- [Reinforcement-learning mesh generation and adaptation](/methods/reinforcement-learning-meshing.md)

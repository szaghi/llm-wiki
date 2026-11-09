---
type: Source
title: "Kirilov, Zhou, Peiró & Moxey (2026) — High-order curvilinear mesh generation from third-party meshes"
description: "End-to-end high-order meshing of meshes from other software: reconstruction of mesh–CAD connectivity, vertex projection, curving, node-sliding optimization and boundary-layer splitting, even with non-watertight CAD."
resource: "doi:10.1016/j.cad.2025.103962"
source_kind: paper
authors: [Kirilov K.S., Zhou J., Peiró J., Moxey D.]
year: 2026
venue: "Comput.-Aided Des. 191:103962"
local_file: "/home/stefano/papers/mosaic/structured-mesh/2026_Crossref_Computer-Aided_Design_Kirilov_High-order_curvilinear_mesh_generation_from_third-party_mesh.pdf"
tags: [high-order-mesh, curving, cad]
timestamp: 2026-11-08T21:01:00Z
---

# Summary

Kirilov et al. make a posteriori curving work for imported meshes without CAD links ([high-order mesh curving](/methods/high-order-mesh-curving.md); [NekMesh](/software/nekmesh.md)).

# Version read

Version of record, Comput.-Aided Des. 191, 103962 (2026; online September 2025). Abstract and §1 read; method by structure; examples in outline.

# Key claims

1. Missing mesh–CAD connectivity hampers a posteriori curving in multi-software workflows (§1). **Stated**
2. Reconstructed connectivity and vertex projection give valid high-order meshes even from invalid, non-watertight CAD given a valid linear mesh (§1). **Stated**

# Notation map

| Kirilov, Zhou, Peiró & Moxey (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| BRep | boundary representation |  |

# Reference list

35 references, merged complete into the [bibliography](/bibliography.md) from the Crossref deposited list.

# Pages created or updated

Chunk 5 (2026-11-08). This source is cited on:

- [High-order mesh curving](/methods/high-order-mesh-curving.md)
- [NekMesh (open-source high-order mesh generator)](/software/nekmesh.md)

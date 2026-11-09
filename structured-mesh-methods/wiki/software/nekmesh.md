---
type: Software
title: "NekMesh (open-source high-order mesh generator)"
description: "Open-source generator of valid curvilinear high-order meshes for spectral/hp element simulation: a CAD-independent pipeline of modules that meshes from CAD or curves linear meshes from many formats, splits a thick curved prism layer into boundary-layer elements, and optimizes and untangles meshes in a variational framework that generalizes elastic and Winslow models."
status: established
aliases: [NekMesh]
tags: [software, high-order-mesh, curving, boundary-layer, optimization]
timestamp: 2026-11-08T21:01:00Z
---

# NekMesh

[Green et al. (2024)](/sources/green-2024.md) present NekMesh, an
open-source package of the Nektar++ ecosystem that produces valid,
high-quality curvilinear meshes of complex three-dimensional geometries for
high-order simulation; they note that few open-source tools can do so.

**Architecture.** Mesh processing is a pipeline of input, processing and
output modules, independent of the CAD engine. The tool generates 2-D and
3-D meshes directly from CAD (boundary representations and NURBS, STEP
files through OpenCASCADE and other engines), or post-processes linear
meshes from formats such as Gmsh, CADfix, Pointwise and Star-CCM+ into
high-order ones; where no CAD is available, spherigon patches smooth the
surface mesh. High-order nodes on edges and faces are projected onto the
CAD and optimized element by element.

**Boundary layers.** Curved boundary layers with any number and thickness
of layers come from an isoparametric splitting of a single thick curved
prism layer.

**Optimization and untangling.** A variational (energy-minimization)
framework recasts linear elasticity, thermo-elasticity, nonlinear
hyperelasticity and the Winslow equations as functionals of the node
positions, generalizing these models for optimization and untangling — the
same family of approaches as [high-order mesh curving](/methods/high-order-mesh-curving.md)
and [variational grid generation](/methods/variational-grid-generation.md).
Examples include aeronautical and automotive geometries.

## Third-party meshes

[Kirilov et al. (2026)](/sources/kirilov-2026.md) extend the NekMesh workflow
to meshes from other generators by reconstructing mesh–CAD connectivity
before curving and optimization.

# Citations

- [Green et al. (2024)](/sources/green-2024.md) — abstract, program summary, §1–§2.
- [Kirilov et al. (2026)](/sources/kirilov-2026.md) — §1.

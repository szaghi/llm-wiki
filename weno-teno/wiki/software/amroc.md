---
type: Software
title: "AMROC"
description: "Deiterding's open-source C++ framework for block-structured adaptive mesh refinement, with Clawpack-based finite-volume solvers for thermally perfect reacting gas mixtures, level-set and ghost-cell boundaries, and, since Peng et al., structured curvilinear mapped meshes."
status: established
aliases: [AMROC, Blockstructured Adaptive Mesh Refinement in object-oriented C++, AMROC-Clawpack]
tags: [software, finite-volume, immersed-boundary]
timestamp: 2026-10-24T05:59:00Z
---

# AMROC

AMROC ("Blockstructured Adaptive Mesh Refinement in object-oriented
C++") is Deiterding's open-source framework for
[block-structured adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
on Cartesian meshes, after Berger & Oliger and Berger & Colella. As
[Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) §1–2 describe
it, the Clawpack package is implemented in AMROC with detailed chemical
kinetics for multispecies thermally perfect gas mixtures, and these
solvers have been used for supersonic combustion and detonation; walls
that are not Cartesian are represented by a level set with ghost-fluid
boundary cells. [Wang et al. (2022a)](/sources/wang-2022.md) implement
their immersed-boundary variants in it. Both sources are by groups that
include the framework's author.

## Numerics in the sources

| | Peng et al. (2022) | Wang et al. (2022a) |
|---|---|---|
| Equations | reacting multispecies Euler, planar or axisymmetric, thermally perfect (CHEMKIN-II) | Euler, ideal gas; reacting H$_2$–air in one case |
| Reconstruction | [MUSCL–Hancock](/methods/muscl-hancock.md) with minmod, mapped-mesh slopes | MUSCL–Hancock on primitive variables |
| Flux | AUSM (Liou–Steffen) or hybrid Roe/HLL with multidimensional entropy correction and mass-fraction positivity correction | primitive-variable Riemann solver (PVRS); [HLL](/methods/hll-riemann-solvers.md) for the reacting case |
| Chemistry | Strang splitting, semi-implicit fourth-order generalized Runge–Kutta (GRK4A) | 12 species, 42 reactions |
| Geometry | body-fitted mapped meshes (new) | ghost-cell [immersed boundary](/methods/immersed-boundary-method.md) on a stationary [level set](/methods/level-set-method.md) |
| Refinement | three to five levels, factor 2 | uniform grids; adaptive refinement left to future work |

Both use second-order schemes; neither uses a WENO, TENO or DG
discretization inside the framework.

## Mapped curvilinear meshes

Peng et al. extend AMROC-Clawpack to structured curvilinear meshes
while keeping the data layout: the uniform computational mesh of every
level is mapped to the physical one, and the finite-volume update is
done in physical space with a capacity function, the ratio of physical
to computational cell area (§2.2, Eqs. 9–12, after LeVeque). Fluxes are
evaluated after rotating the momentum into the face-normal frame
(Eqs. 13–14); MUSCL slopes divide by centroid-to-face distances
(Eqs. 18–20); restriction is area-weighted and prolongation bilinear
with Newton-solved weights (Eqs. 29–31); slip walls reflect the rotated
normal velocity in the ghost cells (§2.6). The motivation is the cost
of the level-set treatment when many cells are cut and the small time
steps of small cut cells (§1). The extension is verified by
[manufactured solutions](/definitions/method-of-manufactured-solutions.md),
multispecies shock tubes and boxes and a cellular detonation, and
validated on Lehr's [shock-induced combustion](/benchmarks/shock-induced-combustion.md)
experiments (§3–4).

## Ghost-cell boundaries

The baseline ghost-cell method of AMROC, in Wang et al.'s description,
reflects the ghost point across the wall to a mirror point, bilinearly
interpolates the fluid state there and reverses the normal (and, for
no-slip walls, the tangential) velocity (§2.3.1, Eqs. 16–18). Its
accuracy drops when the mirror stencil reaches into the solid, which
Wang et al.'s hybrid reconstruction repairs (see
[immersed-boundary methods](/methods/immersed-boundary-method.md)).
They compare it with a cut-cell method in a different framework, AMReX.

## Qualifications

- Peng et al. print the MUSCL reconstruction on mapped meshes so that
  both face values of a cell add half the left slope times the distance
  to the left face and half the right slope times the distance to the
  right face (Eqs. 19–20; page-local); for linear data this reproduces
  the face values only when the two centroid-to-face distances are
  equal, so either the formula
  or the code differs from an exact linear reconstruction on stretched
  meshes *(compiler check, not in the sources)*; the paper gives no
  means to decide which.
- Peng et al. attribute the block-structured refinement to "Berger and
  Colella [16]", where their reference [16] is Berger & Oliger; their
  reference to AMROC's 2011 overview is never cited in the text.
- Neither source discusses free-stream preservation on mapped meshes.
  For a uniform planar flow the update of a cell is the uniform flux
  dotted with the sum of its face normals times face lengths, which
  vanishes for any closed quadrilateral, so the finite-volume form with
  exact edge lengths preserves it; the axisymmetric source term is not
  covered by this argument *(compiler check, not in the sources)*.

# Citations

- [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) — §1; §2.1–2.6, Eqs. (9)–(31); §3–4 (accepted manuscript).
- [Wang et al. (2022a)](/sources/wang-2022.md) — §1; §2.1–2.3, Eqs. (4)–(18); §3.6; §4.

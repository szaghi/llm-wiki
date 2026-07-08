---
type: Definition
title: "Block-structured AMR"
description: "Adaptive refinement by a hierarchy of properly nested rectangular patches aligned to coarse grid lines, refined in space and time by a fixed ratio."
status: established
aliases: [SAMR, patch-based AMR, Berger-Colella AMR]
tags: [amr, block-structured, hierarchy, subcycling]
timestamp: 2026-07-08T00:00:00Z
---

# Block-structured AMR

Adaptive mesh refinement in which the refined region is a **hierarchy of
rectangular grid patches**: level $l{+}1$ patches have mesh spacing
$\Delta x_l / r$ for a fixed (even) refinement ratio $r$, with $r=2$ giving
the 2:1 interface. Defined by
[Berger & Colella (1989)](/sources/berger-colella-1989.md), refining the
earlier rotated-grid approach into grid-aligned patches specifically to make
conservation maintainable.

## Defining discipline

* **Alignment and proper nesting**: every patch starts and ends on corners
  of cells of the next coarser level; a level-$l$ cell is separated from any
  level-$l{-}2$ cell by at least one level-$l{-}1$ cell in each coordinate
  direction (a patch may span several parent patches).
* **Space–time refinement (subcycling)**: $\Delta t_l / \Delta x_l$ is
  constant across levels, so one coarse step corresponds to $r$ fine steps
  and the same explicit integrator runs unmodified on every level.
* **Finest-wins solution**: the solution at a point is the value on the
  finest patch containing it; covered coarse cells are overwritten by the
  conservative average (restriction $R$, [notation](/notation.md)) of their
  fine children.
* **Coupling operators**: patch boundary (ghost) values come from sibling
  patches or from the ghost-fill $\Gamma$ — bilinear interpolation in space,
  linear in time, from the parent level; interface conservation is restored
  by [refluxing](/methods/refluxing.md).
* **Automatic regridding**: error estimation flags cells, buffer zones of
  unflagged cells absorb feature motion between regriddings (finite
  propagation speed), and clustering heuristics emit new patches; nesting is
  enforced by construction.

Within this corpus, this hierarchy — and specifically its $r=2$ coarse–fine
interface with $\Gamma$, $R$, and prolongation $P$ as the transfer
operators — is the structure on which every AMR divergence-constraint
question is posed. [Evans & Hawley (1988)](/sources/evans-hawley-1988.md)'s
claim that CT admits adaptive meshes naturally predates this framework and
concerns smoothly moving zones, not patch hierarchies.

# Citations

1. [Berger & Colella (1989)](/sources/berger-colella-1989.md), §2–6.

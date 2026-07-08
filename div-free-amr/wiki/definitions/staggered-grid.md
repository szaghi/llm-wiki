---
type: Definition
title: "Staggered grid"
description: "Mesh arrangement placing different physical quantities at different locations — cell centers, faces, edges, nodes — within one cell."
status: established
aliases: [staggered mesh]
tags: [collocation, discretization]
timestamp: 2026-07-08T00:00:00Z
---

# Staggered grid

A mesh on which distinct physical quantities are assigned distinct
*centerings* within a cell — cell centers, face centers, edge midpoints,
nodes — as opposed to a *collocated* grid, where all unknowns share the same
locations. Collocation is load-bearing for this domain: which discrete
divergence a scheme can hold exactly is determined by where its field
degrees of freedom live.

The arrangement originates with the
[MAC method](/methods/mac-method.md) of
[Harlow & Welch (1965)](/sources/harlow-welch-1965.md): face-normal
velocities and cell-centered pressure, giving a compact two-point
divergence per direction and a five-point pressure Laplacian free of
checkerboard modes. Its electromagnetic counterpart is the
[Yee lattice](/methods/yee-scheme.md) ([Yee (1966)](/sources/yee-1966.md)):
$E_h$ on edges, $B_h$ on faces — chosen there so perfectly-conducting
boundary conditions are imposed exactly by the placement — plus *time*
staggering (leapfrog, fields offset by half a step).

In the [constrained transport](/methods/constrained-transport.md) arrangement
of [Evans & Hawley (1988)](/sources/evans-hawley-1988.md) (their Figs. 1–2):
thermodynamic quantities at cell centers; velocities and momenta
face-centered; magnetic flux/field components face-centered (normal to their
face, a *different* face assignment than the velocity components); EMFs and
vector-potential components on edges. This is exactly the
$V_h^1$ (edges) / $V_h^2$ (faces) / $V_h^3$ (cells) assignment of the
discrete complex ([notation](/notation.md)): the placement makes the
once-per-edge EMF assembly, and hence $D_h C_h = 0$, possible with compact
second-order differences.

Zone increments need not be constant: the staggering definitions (their
eqs. 4.1–4.3) allow stretched and time-varying ("adaptive") spacings, at the
cost of progressive loss of second-order truncation accuracy when adjacent
zones differ by more than a few percent.

Staggering is a *sufficient* arrangement for the CT constraint mechanism, not
a necessary one: for the Godunov CT variants the staggered field can be
eliminated entirely, yielding an identical pure finite-volume scheme on
cell-centered data whose exact invariant is a corner-centered divergence —
see [CT–finite-volume equivalence](/results/ct-finite-volume-equivalence.md)
([Tóth (2000)](/sources/toth-2000.md)).

# Citations

1. [Harlow & Welch (1965)](/sources/harlow-welch-1965.md), Fig. 2.
2. [Yee (1966)](/sources/yee-1966.md), Fig. 1.
3. [Evans & Hawley (1988)](/sources/evans-hawley-1988.md), §IV(a)–(b), Figs. 1–2.
4. [Tóth (2000)](/sources/toth-2000.md), §4.4.

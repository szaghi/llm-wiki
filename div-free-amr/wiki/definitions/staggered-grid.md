---
type: Definition
title: "Staggered grid"
description: "Mesh arrangement placing different physical quantities at different locations — cell centers, faces, edges, nodes — within one cell."
status: established
aliases: [staggered mesh]
tags: [collocation, discretization]
timestamp: 2026-10-13T00:00:00Z
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

## Contradictions

**Is staggering necessary?** Sources take opposite positions:

* [Tóth (2000)](/sources/toth-2000.md) §4.4: "the staggered representation
  of the magnetic field is unnecessary" — the Godunov CT variants are
  algebraically identical to collocated finite-volume schemes.
* [Londrillo & Del Zanna (2000)](/sources/londrillo-delzanna-2000.md) §3:
  staggered collocation "is by no means a numerical trick but arises in a
  consistent way" — a unique EMF flux function at common points *entails
  necessarily* the staggered placement. Their
  [2004 formalization](/sources/londrillo-delzanna-2004.md) §2.1 explicitly
  rejects the "persistent viewpoint" that staggering only serves to express
  the divergence and suits upwinding poorly. It builds reconstruction, the
  Riemann solvers and the momentum fluxes on the staggered data, and
  measures monopole damage in the collocated counterparts
  ([UCT](/methods/upwind-constrained-transport.md)).
* [Balsara & Kim (2016)](/sources/balsara-kim-2016.md) §1 take the
  necessity side in its strongest, unscoped form: "any divergence-free
  formulation of MHD requires the use of a Yee-type mesh". The statement is
  a premise. It comes with no argument, and Tóth (2000) is not cited. The
  only reason given is constructive: the electric field lives at edges, so
  the fluxes must be upwinded multidimensionally there. That is Londrillo
  and Del Zanna's reading, so the source adds a citation to that side, not
  new evidence. Read literally, as a universal claim, it is contradicted by
  the collocated results above.
* *Not evidence either way* (compiler note): [Balsara & Kim (2004)](/sources/balsara-kim-2004.md)
  frame their comparison as "cleaning vs staggered mesh". Their staggered
  scheme is flux-CT, which Tóth proved equivalent to a collocated
  finite-volume scheme, so the test separates constraint *mechanism* (local
  exact update vs global projection) and not field *placement*.

**Scoped resolution (compiled):** the claims quantify over different
things. Tóth's is an algebraic identity for specific second-order schemes —
staggering can be *rewritten away* after the fact, at the cost of wider
symmetrized stencils and relocating the exact invariant to
$D_h^{\mathrm{k}}$. Londrillo & Del Zanna's is a *constructive* consistency
requirement for building (high-order) schemes with a unique EMF — the
design-time collocation of the update. Neither refutes the other; whether
"necessary" means "ineliminable from the final algebra" (no) or "forced on
the construction" (yes) is exactly the live question of this domain. Both
positions stand; no supersession recorded. *Development:* on the AMR
question specifically, Tóth's own later locality results favor staggered
storage — see the resolved dispute at
[CT–finite-volume equivalence](/results/ct-finite-volume-equivalence.md)
and [transfer locality limits](/results/transfer-operator-locality-limits.md).
*Further development (hypothesis-grade):*
[Zaghi (2026)](/sources/zaghi-2026.md) is a collocated code that *does* hold
an exact interior divergence without staggering ($D_h^{\mathrm{c}}
C_h^{\mathrm{c}} = 0$ on uniform grids), which is a point for the
"eliminable" reading. At 2:1 seams it loses that exactness, and after five
failed local fixes it names re-staggering the field at the seam as the only
exact route ([seam divergence source](/results/collocated-seam-divergence-source.md)).
That is a point for the "forced on the construction" reading, precisely at
refinement interfaces. The dispute's scoped resolution survives: staggering
is avoidable on uniform grids and, so far, unavoidable at 2:1 interfaces.

# Citations

1. [Harlow & Welch (1965)](/sources/harlow-welch-1965.md), Fig. 2.
2. [Yee (1966)](/sources/yee-1966.md), Fig. 1.
3. [Evans & Hawley (1988)](/sources/evans-hawley-1988.md), §IV(a)–(b), Figs. 1–2.
4. [Tóth (2000)](/sources/toth-2000.md), §4.4.
5. [Londrillo & Del Zanna (2000)](/sources/londrillo-delzanna-2000.md), §3.
6. [Zaghi (2026)](/sources/zaghi-2026.md): issues #29, #30.
7. [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md), §§2.1, 2.4, 4.
8. [Balsara & Kim (2004)](/sources/balsara-kim-2004.md), §§I, II.d.
9. [Balsara & Kim (2016)](/sources/balsara-kim-2016.md), §§1, 4.

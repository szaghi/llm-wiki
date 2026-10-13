---
type: Result
title: "CT–finite-volume equivalence"
description: "The Godunov CT variants are algebraically identical to pure finite-volume schemes on the cell-centered field, which conserve a corner-centered divergence exactly."
status: established
tags: [constrained-transport, finite-volume, equivalence, collocation]
timestamp: 2026-10-13T00:00:00Z
---

# CT–finite-volume equivalence

**Statement** ([Tóth (2000)](/sources/toth-2000.md) §4.4). Each of the
field-, flux-, and transport-flux-interpolated
[CT variants](/methods/flux-ct.md) can be rewritten, by composing the
staggered update with the face-to-center interpolation, as a *pure finite
volume scheme* for the cell-centered field $B_h$: a conservative flux-form
update whose symmetrized fluxes are symmetric averages of base-scheme data over
a wider stencil (6 cells × 2 time levels for field-CT). In terms of the cell
centered variables (density, momentum, energy and $B_h$) the recast scheme is **identical**
to the original staggered one — "the staggered representation of the magnetic
field is unnecessary."

**The conserved invariant relocates.** The recast scheme does not conserve
the cell-centered divergence $D_h^{\mathrm{c}} B_h$; it conserves the
corner-centered $D_h^{\mathrm{k}} B_h$ ([notation](/notation.md)) — a contour
integral over a diagonally rotated volume — exactly, to roundoff: if the
staggered field satisfies $D_h^{\mathrm{f}} B_h = 0$ in the four cells meeting
a corner, the interpolated cell-centered field satisfies
$D_h^{\mathrm{k}} B_h = 0$ there, and the updates with the symmetrized fluxes maintain it.

## Consequences

* **Staggering is a representation choice, not the constraint mechanism**,
  for these schemes: the divergence-preserving structure survives intact in
  a fully collocated (cell-centered) formulation — at the cost of wider,
  symmetrized flux stencils ([staggered grid](/definitions/staggered-grid.md)).
* "Exact divergence" claims must always name their stencil: the equivalence
  moves the invariant from $D_h^{\mathrm{f}}$ (staggered view) to
  $D_h^{\mathrm{k}}$ (collocated view) — see
  [exact discrete divergence](/properties/exact-discrete-divergence.md).

**Which cell-centred field.** The equivalence concerns the cell-centred
field defined as the face-to-centre average of the staggered field. The
flux-CT primary source,
[Balsara & Spicer (1999)](/sources/balsara-spicer-1999.md) §2.1, also
advances a separate cell-centred field with the base scheme's own fluxes
(eqs. 10–12) within each step. That field is not the face average: the
authors state that the two differ by "the order of magnitude of the
discretization error", and reconcile them only in the total energy, by an
optional correction (eq. 16). Each step restarts from the interpolated
face field. The paper does not discuss the equivalence.

**The field-CT primary sources.**
[Dai & Woodward (1998, JCP)](/sources/dai-woodward-1998.md) and
[Dai & Woodward (1998, ApJ)](/sources/dai-woodward-1998-b.md) have the same
structure as Balsara & Spicer: the split Godunov sweeps advance a
cell-averaged field $B_h^{*}$, set initially to the two-face average, that
"does not exactly satisfy the divergence-free condition" (JCP §3.2). Its
divergence is "interpolation-dependent" and "O(1) if strong shocks are
involved, no matter what kind of interpolation is used" (JCP §5), with no
stencil named; the net cell flux computed from it is one order lower than
in the same scheme without the field update (ApJ §4, Figs. 18–19). The
papers do not say whether $B_h^{*}$ is reset to the face average each step.
*Compiler reading:* the equivalence holds the corner divergence of the
face-average field, not of $B_h^{*}$, so the O(1) values do not bear on it.
The stencil count above agrees with the printed construction: a face
update differences two corner values, each a four-cell average at two
time levels, and the two corners together span six cells (JCP eqs. 25–26,
50–51; the four-cell average is printed for the new level).

**Scope.** Proved for the Godunov CT variants in 2D with the standard
face-to-center averaging (generalization to nonuniform grids and 3D stated);
it is a statement about these particular schemes, not a claim that every
staggered scheme admits a collocated rewrite.

## Contradictions

**Does the equivalence survive AMR?**
[Balsara (2001)](/sources/balsara-2001.md) §III (intro) claims it does not
carry over to hierarchies: divergence-free transfer between levels requires
the constraint's control volumes at finer levels to nest inside coarse
ones — "all the staggered mesh formulations satisfy this property; the
zone-centered formulation of Tóth does not satisfy this property." The
corner-centered volumes of $D_h^{\mathrm{k}}$ (diagonally rotated) do not
tile under 2:1 refinement the way faces do.

**Development:** [Tóth & Roe (2002)](/sources/toth-roe-2002.md) — Tóth's
own subsequent work — proves the locality trichotomy
([transfer locality limits](/results/transfer-operator-locality-limits.md))
and concludes (§7) that face-centered storage is indicated "for AMR schemes
which require the divergence-free property." On the AMR question the two
camps have effectively converged; the single-grid equivalence itself stands
unrefuted.

**Status (compiled):** the two results are formally compatible — Tóth's
identity ([Tóth (2000)](/sources/toth-2000.md) §4.4) is stated on a single uniform grid; Balsara's claim concerns level
transfer — and the 2002 development resolves the *practical* dispute in
favor of staggered storage at interfaces, from Tóth's own hand. The
single-grid equivalence remains valid; its "staggering unnecessary" reading
does not extend to hierarchies. Effectively settled by convergence of the
parties; no formal supersession.

# Citations

1. [Tóth (2000)](/sources/toth-2000.md), §4.4, eqs. (23)–(27), §7.
2. [Balsara (2001)](/sources/balsara-2001.md), §III.
3. [Tóth & Roe (2002)](/sources/toth-roe-2002.md), §7.
4. [Balsara & Spicer (1999)](/sources/balsara-spicer-1999.md), §2.1, eqs. 10–12, 16.
5. [Dai & Woodward (1998, JCP)](/sources/dai-woodward-1998.md), §§3.2, 3.6, 5, eqs. 25–28, 50–51.
6. [Dai & Woodward (1998, ApJ)](/sources/dai-woodward-1998-b.md), §4, p. 323, Figs. 18–19.

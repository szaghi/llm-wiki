---
type: Source
title: "Strand (1994) — Summation by parts for finite difference approximations for d/dx"
description: "Constructs and catalogues SBP first-derivative operators for diagonal, full, and restricted-full norms, with boundary/interior order combinations and explicit coefficients."
resource: "doi:10.1006/jcph.1994.1005"
source_kind: paper
authors: [Strand B.]
year: 1994
venue: "J. Comput. Phys. 110:47-67"
local_file: "~/papers/mosaic/div-free-amr/1994-JCP-Strand-101006jcph19941023.pdf"
tags: [sbp, high-order, boundary-closure, energy-method]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Systematic construction of finite-difference approximations of $d/dx$
satisfying the **summation-by-parts (SBP) rule** — the discrete analog of
integration by parts that transfers the continuous energy method to the
semi-discretization ([SBP definition page](/definitions/summation-by-parts.md)).
Building on Kreiss–Scherer, derives necessary and sufficient conditions on
the boundary closure for three norm classes (diagonal, full, restricted
full), proves existence for every interior order, computes the operator
families with Maple, and lists explicit coefficients (Appendices A–B),
including minimum-bandwidth choices for parallel hardware.

The PDF is a fully image-only scan (0 extractable characters); read
visually, all 21 pages. No illegible ranges.

# Key claims

1. **The SBP characterization** (Theorem 2.1): $\mathsf{Q}$ satisfies the SBP
   rule $(u, \mathsf{Q}v)_h = -(\mathsf{Q}u, v)_h - u_0 v_0$ iff it has the
   block form $h\mathsf{Q} = \begin{pmatrix} \mathsf{H}^{-1}B & \mathsf{H}^{-1}C \\ -C^T & D\end{pmatrix}$
   with $B$ skew plus $B_1(1,1) = -\tfrac12$, $D$ the antisymmetric interior
   stencil.
2. **Existence at every order** (Theorem 2.2): for every interior order
   $2s$ there exist a norm and an SBP operator accurate of order $\tau$ at
   the boundary points ([Result page](/results/sbp-operator-existence.md)).
3. **Order combinations found**: diagonal norms — boundary order
   $\tau \le 4$, interior $2\tau$; unique closures for $\tau = 1, 2$,
   one-parameter family at $\tau = 3$, three-parameter at $\tau = 4$;
   parameters used to minimize bandwidth. Full norms — boundary
   $\tau = 3, 5$, interior $\tau + 1$. Restricted full norms — boundary 3,
   interior 4, three-parameter family.
4. **Diagonal norms win for systems**: for first-order hyperbolic *systems*
   stability results exist only for diagonal norms; full and restricted-full
   norms "should not be used" there (their ref. [4]) — and diagonal norms
   deliver interior order $2\tau$ at the same boundary bandwidth (9) where
   the other classes deliver only $\tau + 1$.
5. **Finite-precision caveat**: the exact rational coefficients of the
   higher-order closures involve enormous integers; "it is doubtful if the
   difference operator satisfies the summation by parts energy norm in
   finite precision arithmetic."

# Notation map

| Strand | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $H$ (norm matrix) | $\mathsf{H}$ | renamed: registry $H$ is the coarse spacing |
| $Q$ (difference operator) | $\mathsf{D}_1$ acting as $\mathsf{H}^{-1}\mathsf{Q}$-form | Strand's $Q$ *is* the derivative approximation; modern split $\mathsf{D}_1 = \mathsf{H}^{-1}\mathsf{Q}$ |
| $(u,v)_h = \langle u^I, H u^I\rangle + \sum u_\nu v_\nu h$ | $(u,v)_h = u^T \mathsf{H} v$ | semi-infinite line, boundary-modified norm |
| $\tau$, $2s$ | boundary / interior order | |
| diagonal / full / restricted full | norm classes | full: $\mathsf{H}$ SPD block; restricted: first row/column decoupled |

Registry extension made during this ingestion: the SBP block
($\mathsf{H}, \mathsf{Q}, \mathsf{D}_1$).

# Pages created or updated

* Created [Summation by parts (SBP)](/definitions/summation-by-parts.md).
* Created [SBP operator existence and families](/results/sbp-operator-existence.md).
* Extended [Notation registry](/notation.md) (SBP block).

# Citations

1. `~/papers/mosaic/div-free-amr/1994-JCP-Strand-101006jcph19941023.pdf` (doi:10.1006/jcph.1994.1005) — read visually, pp. 47–67. **DOI corrected 2026-10-08 (DOI audit).** The DOI recorded earlier, 10.1006/jcph.1994.1023, resolves on Crossref to Andreassen et al., on spectral viscosity in a stratified atmosphere; the correct DOI, verified on Crossref by title, authors and pages, is 10.1006/jcph.1994.1005. The archive filename still embeds the old DOI.

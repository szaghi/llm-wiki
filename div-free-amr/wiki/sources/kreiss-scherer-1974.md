---
type: Source
title: "Kreiss & Scherer (1974) — Finite Element and Finite Difference Methods for Hyperbolic Partial Differential Equations"
description: "Book chapter that constructs the first summation-by-parts difference operators for d/dx: none exists in the unweighted norm, diagonal norms give boundary order τ with interior order 2τ, and full boundary-block norms give interior order τ+2 or τ+1."
resource: "doi:10.1016/b978-0-12-208350-1.50012-1"
source_kind: paper
authors: [Kreiss H.-O., Scherer G.]
year: 1974
venue: "Mathematical Aspects of Finite Elements in Partial Differential Equations (Academic Press), pp. 195-212"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1974-AcadPress-Kreiss-101016b978-0-12-208350-150012-1.pdf"
tags: [sbp, energy-method, high-order, boundary-closure]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A book chapter comparing Galerkin finite elements with finite differences
for hyperbolic initial–boundary-value problems (§1). Galerkin is
energy-stable by construction but needs a mass matrix inverted and
controls dispersion and dissipation poorly; for finite differences the
hard part is stability at boundaries. The authors reduce general geometry
to a half-strip, periodic in the tangential direction, by appeal to
overlapping grids, and then construct difference approximations of
$d/dx$ that satisfy a discrete energy identity mirroring integration by
parts (eq. 2.5). This is the summation-by-parts property
([SBP](/definitions/summation-by-parts.md)); the chapter never uses that
name. Lemma 2.1 proves that no such operator exists in the unweighted
norm. Theorem 2.1 constructs operators in a norm with positive diagonal
weights on the first $2\tau$ points: boundary order $\tau$, interior
order $2\tau$, with the weights tabulated for $\tau = 1$–$4$ (Table 1).
A full SPD boundary block in the norm gives interior order $\tau+2$
($\tau+1$) for even (odd) $\tau$ (Lemma 2.3, Table 2). §3 applies the
operators dimension by dimension to symmetric hyperbolic systems, with
boundary conditions imposed strongly, and asserts the energy estimate.
There is no divergence content and there are no numerical experiments.

# Key claims

1. **Galerkin is energy-stable** (§1, eqs. 1.5–1.9). For a semibounded
   spatial operator the Galerkin equations give a non-increasing norm
   (eq. 1.8); as an ODE system the mass matrix is SPD and the stiffness
   part is non-positive (eq. 1.9). Stated disadvantages (p. 197): inverting
   the mass matrix "can be very costly", and dispersion, dissipation and
   discontinuity propagation are poorly controlled.
2. **Boundary-fitted differences with interpolated Dirichlet data** (p. 198,
   Figs. 1–2). "A priori energy estimates … only exist for methods of low
   order of accuracy", and the grid introduces "local parasite" solutions.
   With overlapping grids (Fig. 3) "one can construct the interpolation in
   such a way that no stability problem arises" (p. 199). The chapter gives
   neither a construction nor a reference: this is an **unproved
   assertion**.
3. **Continuous and discrete identities** (eqs. 2.2, 2.5). On the half-line,
   $(u, u_x) + (u_x, u) = -|u(0)|^2$; the target is the same identity for
   the difference operator in a discrete scalar product, with the boundary
   value $u_0$ on the right. In registry form:
   $(u,\mathsf{D}_1 u)_h + (\mathsf{D}_1 u, u)_h = -u_0^2$ for real $u$.
4. **Operator form** (p. 200). The operator is $1/h$ times a block matrix:
   an $r\times r$ boundary block, an antisymmetric band interior, and a
   coupling block with its negative adjoint. The authors call this form
   natural: it "arises from any reasonable difference approximation of the
   Cauchy problem when making modifications near the boundary".
5. **Lemma 2.1 (non-existence in the unweighted norm).** No difference
   operator satisfies eq. 2.5 in the scalar product $h\sum_\nu u_\nu v_\nu$
   (eq. 2.4), i.e. with $\mathsf{H} = hI$. The proof: the boundary block
   splits into a diagonal part and an antisymmetric part (eq. 2.6);
   consistency (eq. 2.7) and order-$\tau$ boundary accuracy (eq. 2.8) give
   compatibility conditions (eq. 2.10); the $(0,0)$ condition fixes the
   corner entry at $-\tfrac12$ (eq. 2.12), and the $(0,1)$ condition then
   requires a quantity equal to $\tfrac12$ by consistency to vanish.
6. **Diagonal norm** (eq. 2.12′, p. 203). Weights $\lambda_\nu > 0$ on the
   first $r$ points and 1 beyond. Eq. 2.5 then holds if the operator is the
   inverse weight matrix times the block matrix of claim 4, with corner
   entry $-\tfrac12$. This is the factorization
   $\mathsf{D}_1 = \mathsf{H}^{-1}\mathsf{Q}$ in its original form.
7. **Worked second-order example** (p. 203). A one-sided difference at the
   boundary point and central differences inside factor with weights
   $(\tfrac12, 1, 1, \dots)$: the classical second-order SBP operator,
   matching Table 1 at $\tau = 1$.
8. **Lemma 2.2 (necessary condition).** Boundary order $\tau$ requires the
   interior stencil to satisfy the odd-moment conditions of order $2\tau$
   (eq. 2.16). In the diagonal norm the interior order is therefore forced
   to $2\tau$.
9. **Theorem 2.1 (existence, diagonal norm).** If $r = 2\tau$ and the
   linear system eq. 2.24 for the weights has a positive solution, a norm
   (eq. 2.12′) and an operator exist, accurate of order $\tau$ near the
   boundary and $2\tau$ in the interior. With $r = 2\tau$ the system has a
   unique solution. Positive solutions are computed for $\tau = 1, 2, 3, 4$
   (Table 1, p. 208): "All $\lambda_j$'s are positive".
10. **Practicality** (p. 207): "It is very doubtful whether these formulas
    have any practical interest for $\tau > 4$", because the boundary block
    and the interior formula "become rather complicated".
11. **Full boundary-block norm** (p. 209). The norm carries an SPD
    $r\times r$ block on the boundary points; eq. 2.5 holds if the operator
    is the inverse block times the block matrix of claim 4, subject to
    compatibility (eq. 2.25) and symmetry (eq. 2.26) conditions.
12. **Lemma 2.3** ($\tau \le 8$, "by explicit calculations"). The
    conditions are satisfiable iff the interior odd-moment conditions hold
    up to order $\tau+1$; the interior order is $\tau+2$ for even $\tau$
    and $\tau+1$ for odd $\tau$. Operators are constructed for $\tau = 3$
    ($4\times4$ blocks) and $\tau = 5$ ($6\times6$), with positive
    eigenvalues of the norm block (Table 2: smallest 0.1365351193 for
    $\tau = 3$ and 0.1018573642 for $\tau = 5$, "single precision only").
13. **Systems** (§3, eqs. 3.1–3.4). A symmetric hyperbolic system on the
    half-strip, with boundary conditions on the ingoing characteristics
    (eqs. 3.2–3.3), is semi-discretized by applying the operator "of our
    kind" in the normal direction and a centred periodic operator in the
    tangential one (eq. 3.4). The grid function "satisfies the boundary
    conditions": imposition is **strong (by injection)**, not by penalty.
    "There is no difficulty in deriving an energy estimate": the estimate
    is asserted, not written out. The chapter does not distinguish norm
    classes here. Time is not discretized.
14. **Divergence constraints: none.** No divergence operator, solenoidal
    constraint or divergence measurement. The link to the bundle is the
    operator class.

**Relation to the bundle.** [Strand (1994)](/sources/strand-1994.md)
builds on this chapter: his block form with corner entry $-\tfrac12$ is
already printed here, for the diagonal (p. 203) and the full (p. 209)
norm, in the sufficient direction ("holds if"). The restricted-full class
is Strand's. Strand's caveat that only diagonal norms carry stability
proofs for systems is not in this chapter.

# Tests

None. The numerical content is the coefficient tables: Table 1 (diagonal
weights, $\tau = 1$–$4$) and Table 2 (norm and boundary blocks with the
eigenvalues of the norm block, $\tau = 3, 5$).

Reader's verification (computed, not printed): the Table 1 weights equal
the standard rational diagonal-norm weights to all printed digits, e.g.
$17/48,\ 59/48,\ 43/48,\ 49/48$ at $\tau = 2$.

# Notation map

| Kreiss & Scherer | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $Q$ (approximation of $\partial/\partial x$, with $1/h$ and the inverse norm weights) | $\mathsf{D}_1$ | **collision:** registry $\mathsf{Q}$ is the almost-skew factor, not the derivative |
| block matrix $\begin{pmatrix}B&C\\-C^*&D\end{pmatrix}$ (times $1/h$) | $\mathsf{Q}$ | unnamed in the paper |
| $B = B_1 + B_2$ (boundary block) | upper-left block of $h\mathsf{Q}$ | **collision:** registry $\mathsf{B} = \mathsf{Q}+\mathsf{Q}^T$; KS's $B_1$ is half of $\mathsf{B}$ at the left end |
| $D$ (antisymmetric interior band, entries $\alpha_1,\dots,\alpha_s$) | interior stencil of $h\mathsf{Q}$ | words |
| $\Lambda = \mathrm{diag}(\lambda_0,\dots,\lambda_{r-1})$; norm 2.12′ | $\mathsf{H}$ (diagonal norm) | **collision:** registry $\lambda_k$ is a characteristic speed |
| $A$ (SPD boundary norm block; also the Galerkin mass matrix, eq. 1.9) | boundary block of $\mathsf{H}$ (full norm) | **collision:** registry $A$ is the $\mathsf{D}_2$ factor |
| $(u,v)_h$ | $(u,v)_h$ | same |
| $\tau$ | $\tau$ | boundary order, as on the SBP pages |
| $r$ (boundary-block size $= 2\tau$; also the number of ingoing characteristics in §3) | words | **collision:** registry $r$ is the refinement ratio |
| $s$ (interior stencil half-width) | words | the SBP definition page writes interior order $2s$ (Strand); here $s$ counts stencil entries |
| $H_1, H_2$ (system coefficient matrices) | words | **collision** with $\mathsf{H}$, $H$ |
| $P$ (semibounded spatial operator) | words | **collision:** registry $P$ is prolongation |

# Pages created or updated

* Created this Source page.
* Updated [Summation by parts](/definitions/summation-by-parts.md): origin paragraph (Lemma 2.1, Theorem 2.1, Lemma 2.3); the systems caveat attributed to Strand.
* Updated [SBP-SAT technique](/methods/sbp-sat.md): strong imposition in the original construction.
* Updated [SBP operator existence](/results/sbp-operator-existence.md).

# Citations

1. `/home/stefano/papers/mosaic/div-free-amr/1974-AcadPress-Kreiss-101016b978-0-12-208350-150012-1.pdf`.
   * **Version read.** The publisher's scan (Elsevier ScienceDirect PDF of
     the Academic Press chapter, 18 pp., pp. 195–212).
   * **Identity.** doi:10.1016/b978-0-12-208350-1.50012-1, checked on
     Crossref: type book-chapter; title and authors match; container
     "Mathematical Aspects of Finite Elements in Partial Differential
     Equations"; pp. 195–212; issued 1974; publisher Elsevier (Academic
     Press imprint). The volume editor is not printed in the PDF.
   * **How it was read.** The text layer is poor OCR; every equation,
     matrix and table was read from page renders of all 18 pages, Table 2
     at 220 dpi. The proof algebra of eqs. 2.17–2.23 was read but is not
     reproduced; Table 2 prints only upper triangles, and the full blocks
     are not reproduced. Figs. 1–4 are line sketches without data.
   * **Recorded as printed.**
     * Theorem 2.1 says "such that (2.15) holds" where eq. 2.5 is the
       evident conclusion.
     * The diagonal-norm scalar product carries the primed label "(2.12′)".
     * p. 207 says "Replace (2.5) by" when it introduces a new scalar
       product, meaning the norm (2.4)/(2.12′), not identity 2.5.
   * **Reference list.** 1 entry, merged: Swartz & Wendroff, Math. Comp.
     23 (1969), first page not printed (`swartz-1969`). The bibliography
     entry for this chapter is now `@incollection`; key renamed
     `kreiss-1974` → `kreiss-scherer-1974`. The bibliography holds 3834
     entries after this batch.

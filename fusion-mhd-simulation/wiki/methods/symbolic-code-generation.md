---
type: Method
title: "Symbolic derivation and automatic discretization of MHD operators"
description: "Construction of MHD solvers by symbolic computation: the vector equations are expanded, linearized and written in curvilinear (flux or field-aligned) coordinates by a symbolic engine, and every generated scalar term is discretized automatically; realized at run-time-independent level in SCELT (C++ polynomial algebra, Fourier times cubic elements) and at compile time in GMEC's C++20 metaprogramming solver (finite differences, merged coefficients)."
status: established
aliases: [symbolic computation, automatic discretization, code generation, Compile-time Symbolic Solver, CSS, symbolic vector analysis]
tags: [numerics, code, finite-elements, finite-differences, spectral]
timestamp: 2026-10-16T00:00:00Z
---

# Symbolic derivation and automatic discretization of MHD operators

Written out in non-orthogonal flux coordinates, the full MHD equations reach
"up to 500 terms" per equation ([Ma & Guo (2022)](/sources/ma-2022.md), §3,
attributing the count to Qin et al. 1999), and a field-aligned reduced-MHD
current alone expands to 48 terms
([Jiang et al. (2024)](/sources/jiang-2024.md), §IV). Hand coding such
expansions is error-prone; two codes of this bundle generate them
symbolically and discretize each generated term automatically.

## SCELT: symbolic vector analysis and term-by-term discretization

[SCELT](/software/scelt.md) ([Ma & Guo (2022)](/sources/ma-2022.md)) has two
C++ modules.

1. **Symbolic vector analysis** (§3.1.1–3.1.2). A linked-list polynomial
   algebra (classes for symbolic variables, monomials, polynomials and
   polynomial vectors) carries, for each symbol, its number of time and
   spatial derivatives per direction, a tag binding it to numerical data, an
   exponent and a flag marking first-order (perturbed) quantities. Covariant
   and contravariant vector operators (gradient, divergence, curl, dot and
   cross products) are built directly in magnetic flux coordinates
   $(s,\phi,\theta)$, with $s=\sqrt{1-\psi/\psi_{\max}}$ in the tests and the
   poloidal-plane metric $g_{ss},g_{s\theta},g_{\theta\theta}$ and Jacobian.
   The module linearizes the vector equations automatically. Inputs read like
   the operator: the Grad–Shafranov operator is entered as
   $R^2\nabla\cdot(R^{-2}\nabla H)$ (Fig. 3).
2. **Automatic discretization** (§3.1.3, App. A). Every generated term has the
   form
   $$G(s,\phi,\theta)\,\partial_s^{\,a}\partial_\phi^{\,b}\partial_\theta^{\,c}H,\qquad a+c<3,$$
   with $G$ an equilibrium or metric coefficient and $H$ an unknown (Eq. 9), so
   only $H$, $\partial_sH$, $\partial_\theta H$ and the three second derivatives
   are ever needed. With $\partial_\phi G=0$ and $\partial_\phi\to-in$ the term
   becomes $(-in)^bG\,\partial_s^a\partial_\theta^cH$. The unknown is expanded
   as $H=\sum_{m,k}\hat H_{m,k}v_k(s)e^{im\theta}$, $k=1..N_v$,
   $|m|\le m_0$, with radial cubic elements $v_k$, and the coefficient as
   $G=\sum_{m_g}\hat G_{m_g}(s)e^{im_g\theta}$, which turns products into
   convolutions $\hat G_{m-m_h}$; Galerkin projection on
   $v_k(s)e^{-im\theta}$ gives the matrix entries term by term, and
   coefficients of the same unknown are summed. Finite differences are
   mentioned as an alternative.

The modules are verified on a manufactured 2D Poisson problem on a D-shaped
domain (L1 error order 3.98) and on the inverse Grad–Shafranov equation for
the Solov'ev equilibrium (order 3.81), "consistent with the order of the
radial discretization" (§3.2, Figs. 4–5). The generated eigenproblem is
described on [linear MHD eigenvalue codes](/methods/linear-mhd-eigenvalue-codes.md).
Ma and Guo describe SCELT, "as far as we know", as the first code in the
fusion community built directly by symbolic computation, contrasting it with
general-purpose Mathematica packages (Qin et al. 1999; the VEST project) and
with Lin et al. (2020), the first to bridge analytic expressions and
simulation codes (§1, §5).

## GMEC: the Compile-time Symbolic Solver

[GMEC](/software/gmec.md) ([Jiang et al. (2024)](/sources/jiang-2024.md),
§V, §VII) generates its discrete equations at compile time with a C++20
metaprogramming library, the Compile-time Symbolic Solver (CSS).

- CSS expands vector equations into components in
  [field-aligned coordinates](/methods/field-aligned-coordinates.md), applies
  finite-difference stencils of arbitrary order and offset, merges homogeneous
  terms and emits run-time instructions with "zero-overhead"; custom passes
  drop terms (e.g. the $\partial_y$ terms of the perpendicular Poisson problem),
  composed with a monadic bind (§V).
- It also assembles the implicit and Poisson matrices; the fourth-order biased
  stencil needs 45 matrix loads for one coefficient, and the full expansions of
  the vorticity Poisson equation and of the parallel current have 18 and 48
  terms (§IV, Fig. 8).
- Scheme, order and boundary conditions are template parameters, so changing
  them (or the shifted-metric type) requires recompilation (§V).
- **Merging of coefficients** precomputes, in one contiguous array, the
  products of stencil coefficients and equilibrium metric factors, leaving one
  multiplication per offset variable; the parallel-current evaluation becomes
  "6 times faster than the usual method" at `-O2`, against about 60
  multiplications per point otherwise (§VII B).
- GMEC Part II uses the same symbolic expansion to code the hybrid
  equations ([Liu et al. (2024)](/sources/liu-2024.md), §II).

## Comparison

| | SCELT | GMEC (CSS) |
|---|---|---|
| Problem | linear eigenproblem, full compressible resistive MHD | linear initial-value reduced MHD (+ gyrokinetic particles) |
| Coordinates | axisymmetric flux coordinates | field-aligned, Boozer- or PEST-based |
| Discretization generated | poloidal Fourier × radial cubic elements, Galerkin | finite differences, arbitrary order |
| When | at program run, before matrix assembly | at compile time |
| Source | [Ma & Guo (2022)](/sources/ma-2022.md) | [Jiang et al. (2024)](/sources/jiang-2024.md) |

## Qualifications

- No listing of the generated equations is given in either paper; CSS details
  "will be reported elsewhere" ([Jiang et al. (2024)](/sources/jiang-2024.md),
  §V).
- Jiang et al. state that one multiplication per offset variable "can be
  proved" to be minimal; no proof is given (§VII B).
- SCELT's radial element is a "cubic B-spline" in §3.1.3 and a "cubic
  Hermitian element" in App. A; App. A writes the $\theta$-derivative factor as
  $(-im_h)^c$ for an ansatz $e^{+im_h\theta}$, which gives $(+im_h)^c$ (reader's
  notes; recorded, not resolved). Ma and Guo also attribute a 1984 symbolic
  application to Gladd with a reference that duplicates the venue of the FAR
  code paper (reader's note).

# Citations

- [Ma & Guo (2022)](/sources/ma-2022.md) — §1, §3.1–3.2, §5, Eq. 9, App. A, Figs. 2–5.
- [Jiang et al. (2024)](/sources/jiang-2024.md) — §IV, §V, §VII, Fig. 8.
- [Liu et al. (2024)](/sources/liu-2024.md) — §II.

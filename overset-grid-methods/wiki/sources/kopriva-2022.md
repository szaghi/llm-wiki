---
type: Source
title: "Kopriva et al. (2022) — On the theoretical foundation of overset grid methods for hyperbolic problems: well-posedness and conservation"
description: "Proves with the energy method when the continuous overset initial-boundary value problem for linear symmetric hyperbolic systems is well posed, equal to the single-domain problem and conservative: characteristic coupling in one dimension, and weighted penalty coupling at the overlap boundaries and inside the overlap in one and two dimensions."
resource: "doi:10.1016/j.jcp.2021.110732"
source_kind: paper
authors: [Kopriva D.A., Nordström J., Gassner G.J.]
year: 2022
venue: "J. Comput. Phys. 448:110732"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2022_Crossref_Journal_of_Computational_Physics_Kopriva_On_the_theoretical_foundation_of_overset_grid_methods_for_hy.pdf"
tags: [stability, energy-method, conservation, sbp-sat, overset-grid]
timestamp: 2026-11-02T15:04:00Z
---

# Summary

Before any discretization, is the overset problem itself sound? Kopriva, Nordström & Gassner study the linear, constant-coefficient symmetric hyperbolic system on two partially overlapping subdomains coupled at the overlap boundaries, and ask whether this initial-boundary value problem is well posed, whether its solution equals that of the single-domain problem, and whether it is conservative. With the energy method — integration by parts over the overlap and its complements, a global energy that discounts the double-counted overlap with weights $\eta$ and $1-\eta$, and penalty (lifting) terms — they prove energy bounds and equivalence for characteristic coupling in one dimension, show that without diagonalization the energy method leaves unbounded interface terms, and restore boundedness with weighted penalties at both overlap boundaries and, in two dimensions, at points inside the overlap. The coupling conditions that give energy bounds are the same that give conservation. The results are collected on [well-posedness and energy stability of overset problems](/results/overset-well-posedness.md); they underlie [discontinuous Galerkin](/methods/discontinuous-galerkin-on-overset-grids.md) and [high-order](/methods/high-order-overset-discretization.md) overset discretizations and the [conservative overset interface](/methods/conservative-overset-interface.md).

# Version read

arXiv preprint 2105.04664v1 (10 May 2021), 29 pages, all read; theorem and equation numbers are those of the preprint. The paper is purely analytical: no numerical tests.

# Key claims

1. Scalar 1-D advection on $(a,d)$ split into $[a,c]$ and $[b,d]$ with $v(b,t)=u(b,t)$: both subproblems are energy bounded by the initial data, the overlap counted once (Thm 1, Eq. (15)); the overset problem is well posed and its solution equals the single-domain solution on each subdomain (Thm 2). **Proved**
2. 1-D symmetric systems with characteristic boundary and interface conditions: energy bounded (Thm 3) and equivalent to the single-domain problem (Thm 4); the proof decouples the characteristic variables, which needs diagonalization. **Proved**
3. Without characteristic decoupling the energy method leaves interface terms not bounded by data (Eqs. (51)–(52)); the authors argue that overset methods work in practice because the two solutions differ only by truncation error (Remark 2). **Derived** / **Stated**
4. Weighted penalty coupling at both overlap boundaries in both subdomains is energy bounded if $\beta A+\Sigma_u=\Sigma_v$ and $2\Sigma_v-\beta A\ge0$, with $\beta=\eta$ at $x=b$ and $\beta=1-\eta$ at $x=c$; the penalty then adds dissipation $\mathcal P=(u-v)^T(\Sigma_u+\Sigma_v)(u-v)\ge0$ (Thm 5, Eqs. (76)–(77)). **Proved**
5. The weighted energy $E=\|u\|^2_{\Omega_u}+\|v\|^2_{\Omega_v}-\{\eta\|u\|^2_{\Omega_O}+(1-\eta)\|v\|^2_{\Omega_O}\}$ is non-negative for $0<\eta<1$ and bounds each subdomain energy (Lemma 2). **Proved**
6. Upwind example: $\eta=\beta=\tfrac12$, $\Sigma_u=\tfrac12|A^-|$, $\Sigma_v=\tfrac12A^+$ satisfies both conditions (Eqs. (78)–(79)). **Proved**
7. The penalized 1-D problem is equivalent to the single-domain problem and well posed (Thm 6), and conservative if and only if $\beta A+\Sigma_u=\Sigma_v$ — the energy condition (Thms 7–8). **Proved**
8. In 2-D with boundary-only coupling the same conditions with $A\to\vec A\cdot\hat n$ give energy bounds and conservation (Thms 9–12). **Proved**
9. Adding point penalties inside the overlap keeps energy boundedness and conservation if $(1-\eta)\Sigma^m_u=\eta\Sigma^m_v$; they add dissipation proportional to the jump $u-v$ (Thms 13, 15); equivalence and well-posedness are stated with proof by reference (Thm 14). **Proved** / **Stated**
10. Remark 5 states that conservation is necessary for energy boundedness and energy boundedness sufficient for conservation; the necessity is shown for the sufficient energy condition used, not for the problem in general. **Stated**
11. The weight $\eta$ is arbitrary at the continuous level and can favour the better-resolved subdomain numerically (Remark 4). **Stated**

# Printed slips

- Eq. (126): the lower-right block is printed $-2\eta\Sigma_v^m$; Eq. (124) gives $+2\eta\Sigma_v^m$, consistent with Eq. (127) *(compiler check, not in the sources)*.
- Eq. (1): lower summation limit printed "$i-1$"; p. 13 "$\Sigma_u$ and $\Sigma_u$" for $\Sigma_u$ and $\Sigma_v$; Theorems 6 and 8 cite "(54)–(54)" for (54)–(55); Eq. (84) uses $\Sigma_L$, $\Sigma_R$; p. 22 cites Theorem 2 for Lemma 2; Eq. (123) $u^T$ for $v^T$; Eqs. (116)–(117) initial data $u_0$, $v_0$ for $\omega_0$.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Omega_u$, $\Omega_v$, $\Omega_O$ | the two component domains and their overlap | |
| $u$, $v$, $\omega$ | solutions on the subdomains and on the single domain | |
| $\Sigma_u$, $\Sigma_v$ | penalty matrices | the registry's SAT penalty $\Sigma$ (§8) |
| $\eta$ | overlap weight, $0<\eta<1$ | page-local on the well-posedness page |
| $A^\pm$ | positive and negative parts of the coefficient matrix | |

# Reference list

25 printed references, numbered, merged complete into the [bibliography](/bibliography.md) with `citedby` kopriva-2022. The SBP–SAT overset stability papers of Nordström and co-workers are cited as the numerical predecessors. No printed duplicates.

# Pages created or updated

Chunk 3 (2026-11-02). This source is cited on:

- [Composite overlapping grid](/definitions/composite-overlapping-grid.md)
- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Conservative overset interface](/methods/conservative-overset-interface.md)
- [Discontinuous Galerkin methods on overlapping grids](/methods/discontinuous-galerkin-on-overset-grids.md)
- [High-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Well-posedness and energy stability of overset problems](/results/overset-well-posedness.md)
- [Overture (and its grid generator Ogen)](/software/overture.md)

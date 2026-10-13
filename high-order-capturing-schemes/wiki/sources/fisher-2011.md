---
type: Source
title: "Fisher, Carpenter, Yamaleev & Frankel (2011) — Boundary closures for fourth-order energy stable weighted essentially non-oscillatory finite-difference schemes"
description: "Boundary closures for the fourth-order energy-stable WENO (ESWENO) scheme that satisfy summation by parts, keep WENO stencil biasing up to the boundary on non-uniform flux points fixed by the norm, and give provable L2 stability with global third (diagonal norm) or fourth (block norm) order."
resource: "doi:10.1016/j.jcp.2011.01.043"
source_kind: paper
authors: [Fisher T.C., Carpenter M.H., Yamaleev N.K., Frankel S.H.]
year: 2011
venue: "J. Comput. Phys. 230:3727-3752"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2011-JCP-Fisher-101016jjcp201101043.pdf"
tags: [weno, boundary-treatment, summation-by-parts, stability, finite-difference]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The paper extends the periodic ESWENO of Yamaleev and Carpenter to
finite domains by casting the WENO target operator in SBP form and
adding design-order energy stabilization. The central result is that
the flux points near each boundary must be non-uniform and derived
from the SBP norm. Merged into the new
[energy-stable WENO](/methods/energy-stable-weno.md) page and into the
WENO-Z, critical-point, smoothness-indicator and finite-difference pages.

# Key claims

1. **Motivation** (§1): conventional WENO boundary closures are ad hoc
   and reduce accuracy (from $2p$ to $p + 1$ by discarding stencils), and
   WENO has no energy estimate.
2. **SBP framework** (§2.1, Theorem 1): an SBP derivative operator
   whose dissipation part is built from positive-semidefinite diagonal
   matrices, with an SAT boundary penalty, is $L^2$-stable and
   $(z_{bc} + 1)$-order accurate for boundary accuracy $z_{bc}$.
3. **WENO in matrix form** (§2.2): interpolation to flux points,
   weights (eq. 13) $\tilde\omega = d(1 + \tau/(\epsilon + \beta))$, and
   telescoping differentiation. In the smooth limit this is the target
   operator.
4. **Non-uniform flux points** (§3, Lemma 1): needed so that SBP,
   accuracy and biasing hold together, with positions given by the norm
   $P$ (eq. 24). Diagonal-norm closures give global order $p + 1$,
   block-norm closures $2p$.
5. **Energy stabilization** (§4): the symmetric part of the WENO
   operator is decomposed into SBP dissipation matrices. Their possibly
   negative diagonals are made smoothly non-negative by an added term,
   which gives ESWENO.
6. **Accuracy** (§5): the sufficient condition is $w - d = O(\delta x^3)$
   (eq. 41). The bound $O(\delta x^3) \le \epsilon \le O(\delta x^2)$
   (eq. 42) gives design order for any number of vanishing derivatives,
   and with only $\epsilon > 0$ the order may fall to two. The
   recipe of Appendix A (eq. 75) sets $\epsilon \propto \delta x^4$,
   below that window. The paper does not discuss the difference.
7. **Tests** (§6): eigenvalues move to the left half-plane with
   stabilization; design order on advection, quasi-1D nozzles and the 2D
   vortex; the diagonal-norm closure diverges without stabilization; a
   reacting H₂–air shear layer.

# Notation map

| Fisher et al. (2011) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathcal{P}$, $\mathcal{Q}$, $\mathcal{D}$ | $\mathsf P$, $\mathsf Q$, $\mathsf D$ | SBP norm and operators |
| $\bar w^{(r)}_j$, $\bar d^{(r)}_j$ | $\omega_k$, $d_k$ | candidates $r \in \{L, C, R\}$ |
| $\bar\beta^{(r)}_j$, $\bar\tau_j$, $\epsilon$ | $\beta_k$, $\tau$, $\varepsilon$ | |
| $\delta x$ | $h$ | |
| $\bar{\mathbf x}$ (flux points), $\mathbf x$ | flux points, $x_j$ | |
| $\Delta$, $\Lambda_i$ | difference operator, dissipation diagonals | words on concept pages |

# Pages created or updated

* Updated [Accuracy at critical points](/properties/accuracy-at-critical-points.md).
* Updated [Conservative finite-difference (flux) formulation](/methods/conservative-finite-difference.md).
* Created [Energy-stable WENO (ESWENO) with summation-by-parts boundary closures](/methods/energy-stable-weno.md).
* Updated [Isentropic vortex advection (smooth accuracy test)](/benchmarks/isentropic-vortex.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [Smoothness indicator](/definitions/smoothness-indicator.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Updated [WENO-Z](/methods/weno-z.md).
* Updated [Notation registry](/notation.md): batch-4 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2011-JCP-Fisher-101016jjcp201101043.pdf` (doi:10.1016/j.jcp.2011.01.043, checked on Crossref; typeset JCP article): text extraction, all sections and appendices; eqs. 13, 19, 41–49 and 73–75 read from the page images (pp. 3731, 3735, 3736, 3747). The appendix interpolation and dissipation coefficients are not reproduced. Reference list: 23 entries.

---
type: Result
title: "Conservation–orthogonality incompatibility"
description: "No conservative scheme can guarantee the discrete Lorentz acceleration is exactly orthogonal to the magnetic field in every cell; proved by counterexample."
status: established
tags: [impossibility, conservation, lorentz-force, divergence-constraint]
timestamp: 2026-10-13T00:00:00Z
---

# Conservation–orthogonality incompatibility

**Statement** ([Tóth (2000)](/sources/toth-2000.md), Appendix A). A scheme
cannot simultaneously satisfy (i) numerical conservation of momentum —
necessary, by Lax–Wendroff, for correct weak solutions — and (ii) the
"orthogonality property": that the discretized acceleration due to the
Lorentz force is exactly perpendicular to the magnetic field in every grid
cell, for arbitrary initial data satisfying $D_h B_h = 0$ in some discrete
sense.

**Proof shape** (explicit counterexample). Take $\rho, p$ constant, $\mathbf u = 0$;
choose cell-centered data with $B^y = 0$ in all neighbors of a cell $(i,j)$,
a finite $B^x_{i,j} = 1$ with truncation-level $B^y_{i,j} = \Delta x^k$, and
neighbor values giving finite current $J^z_{i,j} = 1$ — all while
$D_h^{\mathrm{c}} B_h = 0$ in every cell (free parameters exceed
constraints). Consistency forces a finite momentum change in $(i,j)$ with a
nonzero $x$-component (orthogonality to the tilted $B_{i,j}$), while
orthogonality forces the neighbors' $\rho u_x$ to stay zero — so total
$\rho u_x$ is not conserved. Contradiction.

## Consequences

* For conservative shock-capturing MHD there is **no discrete divergence
  constraint whose satisfaction eliminates all unphysical Lorentz-force
  effects**; the choice of stencil for $D_h$ "is always somewhat arbitrary"
  (Tóth §1.1). Holding one
  [exact discrete divergence](/properties/exact-discrete-divergence.md) is a
  scheme property, not a guarantee of pointwise-physical forces.
* This bounds what *any* divergence-preserving construction — including
  [CT](/methods/constrained-transport.md) and its
  [collocated equivalents](/results/ct-finite-volume-equivalence.md) — can
  promise at the momentum equation.

**Scope.** The proof is for conservative, consistent single-step updates of
the momentum density with cell-wise orthogonality demanded exactly; it does
not forbid orthogonality to truncation error, nor non-conservative
formulations (which trade away correct jump conditions — see
[eight-wave](/methods/eight-wave.md)).

**The truncation-order loophole, occupied.**
[Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md) §2.4
show that for second-order conservative fluxes the orthogonality defect
equals $|B|^2$ times the divergence on the stencil the momentum fluxes use,
plus a remainder. [Upwind constrained transport](/methods/upwind-constrained-transport.md)
feeds the exactly held staggered field into those fluxes, so the first term
vanishes identically and only the remainder is left. This is consistent with
the theorem, which forbids only exact cell-wise orthogonality. Two compiler
cautions:
* The estimate concerns the smooth (centered) part of the flux; the upwind
  dissipation contributes only a diffusive term.
* The remainder is a two-point-averaging error derived for smooth data
  ($O(h^2)$). The paper does not bound it separately at discontinuities, so
  "monopole-free" there means "free of the divergence term", not
  "orthogonal to $O(h^2)$".

# Citations

1. [Tóth (2000)](/sources/toth-2000.md), §1.1, Appendix A, Fig. 21.
2. [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md), §2.4, eqs. 48–52.

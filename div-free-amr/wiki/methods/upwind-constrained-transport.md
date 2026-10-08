---
type: Method
title: "Upwind constrained transport (UCT)"
description: "CT design in which staggered face fields are primary data everywhere (reconstruction, Riemann solvers, fluxes) and the edge EMF is a four-state upwind flux, making the divergence condition built-in."
status: established
aliases: [UCT, upwind CT]
tags: [constrained-transport, upwind-emf, godunov, monopoles]
timestamp: 2026-10-08T00:00:00Z
---

# Upwind constrained transport (UCT)

A design framework for Godunov-type MHD schemes, named and formalized by
[Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md) from
the outline in [Londrillo & Del Zanna (2000)](/sources/londrillo-delzanna-2000.md).
[Constrained transport](/methods/constrained-transport.md) keeps
$D_h^{\mathrm{f}} B_h = 0$ ([notation](/notation.md)) in the induction
update. UCT adds the demand that **every other step of the scheme be
consistent with that invariant**:

1. **Primary data.** The face fields $B_h \in V_h^2$ are the magnetic
   unknowns. Cell-centered values are derived from them, never evolved.
2. **Reconstruction.** A face component is continuous along its own
   coordinate, so it is not reconstructed there. Only transverse
   reconstruction is needed, and only the variables that enter the local
   wave fan (fluid variables and tangential field) are reconstructed and
   upwinded ([divergence-free reconstruction](/methods/divergence-free-reconstruction.md)).
3. **Fluxes.** Momentum and energy fluxes take the staggered normal
   component directly, not a cell-centered average.
4. **Edge EMF.** The EMF $E_h$ at an edge is a single-valued four-state
   upwind flux: the average of the four reconstructed edge states, minus the
   upwind dissipation from *both* overlapping 1D Riemann fans. There are
   Roe-type and HLL forms; for LLF the formula reduces to the
   Kurganov–Noelle–Petrova central flux.
5. **Time integration.** All fluxes are evaluated at the same stage, with
   no time splitting.

## Properties

* **Monopole cancellation.** For second-order fluxes the component of the
  Maxwell-stress divergence along $B$ equals $|B|^2$ times the divergence on
  the stencil the momentum fluxes use, plus a two-point-averaging remainder
  ($O(h^2)$ for smooth data). Item 3 makes that stencil the exactly held
  $D_h^{\mathrm{f}}$, so the divergence term vanishes identically, at
  discontinuities too. A collocated or flux-averaged CT scheme sees
  $D_h^{\mathrm{c}}$ of the averaged field instead, which is $O(1)$ at
  transverse jumps ([flux-CT](/methods/flux-ct.md)). Exact orthogonality
  remains impossible for any conservative scheme, and this does not claim
  it; see the scope and cautions at
  [conservation–orthogonality incompatibility](/results/conservation-orthogonality-incompatibility.md).
* **Measured benefit** (same underlying solver, UCT against the collocated
  base scheme). On [rotated shock tubes](/benchmarks/rotated-shock-tube.md)
  the error in the normal field drops 2.7–21×, while the scheme's own
  divergence stays at $10^{-13}$–$10^{-12}$. On Orszag–Tang and the rotor
  the base schemes show visible monopole damage. On a smooth CP Alfvén wave
  UCT is about 10% less accurate, a cost of interpolating to cell centers.
* **High order.** On point values the exact invariant lives on deconvolved
  face variables. The point values used in fluxes are recovered by an
  implicit inversion, so their divergence holds only to the inversion's
  precision ($10^{-7}$–$10^{-6}$ maxima at third order). The alternative is
  to evolve the point-value vector potential and take its two-point curl
  ([vector-potential evolution](/methods/vector-potential-evolution.md)).
* **Same construction for SR and GR MHD**, per the authors. They also claim
  a natural extension to AMR and unstructured grids; for the unstructured
  triangular counterpart they cite De Sterck's MUCT.

# Citations

1. [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md), §§1.1, 2.1–2.4, 3, 4, Appendix A.
2. [Londrillo & Del Zanna (2000)](/sources/londrillo-delzanna-2000.md): the original four-state EMF and staggering-from-consistency argument.

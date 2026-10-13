---
type: Source
title: "Londrillo & Del Zanna (2004) — The upwind constrained transport method"
description: "Formalizes upwind constrained transport: staggered face fields as primary data in reconstruction, Riemann solvers and four-state edge EMFs, making the divergence condition built-in and cancelling numerical monopoles."
resource: "doi:10.1016/j.jcp.2003.09.016"
source_kind: paper
authors: [Londrillo P., Del Zanna L.]
year: 2004
venue: "J. Comput. Phys. 195:17-48"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2004-JCP-Londrillo-101016jjcp200309016.pdf"
tags: [constrained-transport, upwind-emf, divergence-free-reconstruction, monopoles, godunov]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Turns the outline of [Londrillo & Del Zanna (2000)](/sources/londrillo-delzanna-2000.md)
into a general design framework, **upwind constrained transport (UCT)**
([method page](/methods/upwind-constrained-transport.md)). The staggered
face fields are the primary data not only of the induction update but also
of reconstruction, of the Riemann solvers and of the momentum and energy
fluxes. The paper derives three consequences. The normal component needs no
reconstruction and takes no part in upwinding. The edge EMF is a four-state
upwind flux that combines both overlapping 1D wave fans. And numerical
monopoles cancel because the momentum fluxes see the divergence on the
stencil the scheme holds exactly. The method is applied to a Roe-type
positive scheme (Liu–Lax) and to second- and third-order HLL central
schemes. These are compared with their collocated "base scheme" counterparts
on a CP Alfvén wave, rotated shock tubes, Orszag–Tang and the fast rotor.

# Key claims

1. **Consistency demands for MHD** (§1.1). A scheme is "consistent with the
   specific properties of the MHD system" if three things hold. The
   discretized $\partial_i B_i$ entering the divergence are consistent
   approximations. They vanish exactly for divergence-free initial data. And
   the discretized induction equation preserves this exactly in time. In a
   finite-volume setting the CT form, with face fluxes $B_h \in V_h^2$ and
   edge EMFs $E_h \in V_h^1$, meets all three: $D_h^{\mathrm{f}} B_h = 0$ is
   preserved algebraically (their eqs. 11–13; [notation](/notation.md)).
2. **The normal component is not reconstructed** (§2.2). Along its own
   coordinate a face component is continuous across a discontinuity, and its
   face values already give the cell-centered value and the parallel
   derivative to second order. Reconstruction is needed only along the
   transverse coordinates. The parallel derivative may be discontinuous. By
   the divergence relation and the commutativity of the two-point
   differences, its jump equals transverse differences of the other
   components (their eq. 25). This "duality" matches the MHD
   Rankine–Hugoniot structure, where $B_n$ is continuous and does not enter
   the wave fan.
3. **Collocated derivatives produce $O(1)$ divergence at discontinuities**
   (§2.2.1). A collocated scheme building face values as midpoint averages
   of cell-centered data effectively uses the central difference
   $D_h^{\mathrm{c}}$. Across a discontinuity this differs from the
   staggered derivative by an $O(1)$ term, so the divergence it implies is
   $O(1)$ there (their eqs. 30–32). The authors know of no collocated scheme
   that properly recovers the divergence-free condition in reconstruction.
4. **Four-state upwind EMF** (§2.3, eqs. 41–42; HLL form eq. 56). At an edge
   two 1D Riemann fans overlap, and the EMF has two independent upwind
   representations. The one-valued flux combines them as the four-state
   average minus the dissipation from *both* directions. It reduces to the
   correct 1D flux for discontinuities aligned with $x$, $y$ or the diagonal.
   For LLF and HLL it reduces to the central-scheme formulas of
   Kurganov–Noelle–Petrova. For a given velocity, the induction equation
   written for the vector potential is a Hamilton–Jacobi equation, and the
   EMF formula coincides with the Hamilton–Jacobi flux.
5. **Monopole cancellation** (§2.4, eqs. 48–52). For second-order fluxes,
   $[B\cdot(\nabla\cdot T)]_{\mathrm{num}} = |B|^2\,[D B]_{\mathrm{num}} + O(h^2)$,
   where $T$ is the Maxwell stress. Its accuracy is therefore that of the
   divergence on the stencil the momentum fluxes use:
   * Earlier CT variants evolve staggered data but feed cell-centered
     averages into the fluxes. Their effective divergence is
     $D_h^{\mathrm{c}}$ of the averaged field. Its residual
     $h^2 \tfrac{1}{4h^3} D^3 b$ is $O(1)$ at transverse jumps, so those
     schemes produce monopoles.
   * UCT feeds the staggered data directly, so the term is
     $D_h^{\mathrm{f}} B_h = 0$ and monopoles cannot arise.
   * Exact cancellation also requires all flux derivatives at the same time
     level, so **time splitting breaks it**.
6. **High order on point values** (Appendix A). The primary data become
   deconvolved face variables $\hat b$, evolved exactly so that the
   point-value divergence of $\hat b$ is preserved to machine precision. The
   point values $b$ used in fluxes are recovered by an implicit inversion,
   $(I - \tfrac{1}{24}\tilde D^{(2)})\, b = \hat b$, so the divergence of $b$
   holds only to the inversion's precision. Third-order runs measure
   $10^{-12}$ on the CP wave and $10^{-7}$–$10^{-6}$ (maxima) on shock
   tubes. An equivalent route evolves the point-value vector potential and
   takes the face fields as its two-point curl.
7. **Evidence** (§4, Tables 1–5). UCT against its collocated base scheme,
   same underlying solver:
   * Rotated shock tubes (256×2 strip, $\alpha = \tan^{-1}2$): UCT lowers
     the error in the supposedly constant $B_n$ by 2.7–21×. For example on
     ST-3 with the positive scheme it drops from $4.3\cdot10^{-3}$ to
     $5\cdot10^{-4}$. The second-order maximum of $D_h^{\mathrm{f}} B_h$ is
     $10^{-13}$–$10^{-12}$.
   * The central divergence of the *interpolated* cell-centered field stays
     $O(10$–$100)$ at the fronts for both UCT and base scheme. The stencil
     decides what "divergence-free" measures.
   * Orszag–Tang and the rotor: the base schemes show monopole damage
     (structured filaments, noise inside the rotor).
   * On the smooth CP wave UCT is about 10% *less* accurate than the base
     scheme, which the authors attribute to the extra interpolation to cell
     centers.
8. **Test-design caution** (§4.2). Divergence-free properties are hidden if
   the initial field is uniform or if the propagation direction lies along
   cell sides or diagonals. In those cases every representation of the
   divergence is exactly zero, so the test cannot discriminate
   ([rotated shock tube](/benchmarks/rotated-shock-tube.md)).

# Notation map

| Londrillo & Del Zanna (2004) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $b_i$ (staggered, face-averaged) | $B_h \in V_h^2$ | primary data |
| $\tilde B_i$, $B_i$ (cell-centered) | collocated $B_h$ | interpolated, $\tfrac12$ of adjacent faces (eq. 23) |
| $E_k$ (line-averaged, edges) | $E_h \in V_h^1$ | |
| $A_k$ | $A_h \in V_h^1$ | eqs. 14–15 |
| $D_i$ (two-point divided difference) | components of $D_h^{\mathrm{f}}$, $C_h$ | |
| $D_i^{(c)}$ (central difference) | components of $D_h^{\mathrm{c}}$ | |
| $[\nabla\cdot b]_{\mathrm{num}}$ / $[\nabla\cdot B]_{\mathrm{num}}$ | $D_h^{\mathrm{f}} B_h$ / $D_h^{\mathrm{c}}$ of the interpolated field | their eq. 57 |
| $\hat b_i$, $\hat f_i$ (Appendix A) | deconvolved point-value primary data | no registry symbol |
| SUP / BS | collocated base scheme | |
| $T$ (Maxwell stress) | written out in prose | |

# Pages created or updated

* Created [Upwind constrained transport](/methods/upwind-constrained-transport.md).
* Created [Rotated shock tube](/benchmarks/rotated-shock-tube.md).
* Updated [Flux-CT and the Godunov CT variants](/methods/flux-ct.md): the monopole objection to cell-centered fluxes.
* Updated [Constrained transport](/methods/constrained-transport.md): the high-order point-value form.
* Updated [Divergence-free reconstruction](/methods/divergence-free-reconstruction.md): the normal component needs no reconstruction; the derivative-jump identity.
* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md): the same field measured on two stencils; time splitting.
* Updated [Conservation–orthogonality incompatibility](/results/conservation-orthogonality-incompatibility.md): truncation-order orthogonality claimed for UCT.
* Updated [Staggered grid](/definitions/staggered-grid.md): further support for the constructive side of the `Contradictions`.

# Citations

1. `~/papers/mosaic/div-free-amr/2004-JCP-Londrillo-101016jjcp200309016.pdf` (doi:10.1016/j.jcp.2003.09.016): text extraction, pp. 17–48, Appendix A and the reference list (35 entries).

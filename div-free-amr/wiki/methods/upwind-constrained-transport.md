---
type: Method
title: "Upwind constrained transport (UCT)"
description: "CT design in which staggered face fields are primary data everywhere (reconstruction, Riemann solvers, fluxes) and the edge EMF is a four-state upwind flux, making the divergence condition built-in."
status: established
aliases: [UCT, upwind CT]
tags: [constrained-transport, upwind-emf, godunov, monopoles]
timestamp: 2026-10-13T00:00:00Z
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
   Kurganov–Noelle–Petrova central flux. At first order the UCT EMF equals
   the $\mathcal{E}^\circ$ algorithm of
   [Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md). That
   construction is not upwinded in the multidimensional derivatives, and it
   goes oscillatory on field-loop advection, which motivated their
   contact-upwinded $\mathcal{E}^c$ ([flux-CT](/methods/flux-ct.md)).
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
* **Fourth-order finite-volume realization**
  ([Felker & Stone (2018)](/sources/felker-2018.md)). The base scheme is the
  McCorquodale–Colella fourth-order FV method: PPM4 reconstruction,
  average↔point conversions by transverse Laplacians, and an SSP-RK4
  integrator. UCT is carried at the same order:
  * the face averages of $B_h$ are never reconstructed; the cell averages
    the fluid needs are recovered from them by an unlimited fourth-order
    "inverse reconstruction";
  * the four corner states of $E_h$ come from PPM4 transverse
    reconstruction of the face Riemann states of $v$ and $B$;
  * a single-valued corner EMF is selected by the HLL four-state formula,
    with Einfeldt wavespeeds taken from the four adjacent face solves.
  
  On smooth problems the measured order is four; at $128\times64$ the
  error is nearly four orders of magnitude below that of second-order
  $\mathcal{E}^c$. In 3D the invariant is held to round-off
  ([field loop](/benchmarks/field-loop-advection.md)). AMR is future work
  and needs fourth-order prolongation and restriction operators.
* **Relation to $\mathcal{E}^c$**
  ([Felker & Stone (2018)](/sources/felker-2018.md), Appendix A). In two limiting cases, the
  HLL-UCT corner EMF built from second-order reconstruction agrees to second
  order with the $\mathcal{E}^c$ algorithm of Gardiner & Stone:
  * a stationary domain, where $\mathcal{E}^c$ reduces to the unbiased
    average with correct viscosity;
  * supersonic grid-aligned flow, which additionally requires identical
    Riemann states of $B_2$.
  
  In general the two cannot match exactly. Combined with Gardiner & Stone's
  own first-order identity with $\mathcal{E}^\circ$, this places the
  Athena EMF family inside second-order UCT. The equivalence is proved only
  for these cases.
* **A composition formula for any Jacobian-free solver**
  ([Mignone & Del Zanna (2021)](/sources/mignone-2021.md) §5, eq. 33).
  * Write the 1D induction flux at a face as weighted left/right fluxes
    plus a diffusion term linear in the transverse field:
    $a^L F^L + a^R F^R - (d^R B_t^R - d^L B_t^L)$.
  * The edge EMF is then assembled from the four adjacent faces using only
    two kinds of input: the base solver's $a$ and $d$ coefficients, and 1D
    reconstructions of the transverse velocity and of the staggered field
    to the edge.
  * Coefficients are derived for LLF, HLL, HLLC, HLLD and GFORCE. HLLC
    reduces to HLL when $B_n \ne 0$. HLLD needs a switch to the degenerate
    three-wave limit as $B_n \to 0$.
  * The two new schemes are UCT-HLLD and UCT-GFORCE.
* **Measured ranking** (second order, Roe or HLLD base solver).
  * UCT-HLLD is the least dissipative and stays stable, and its dissipation
    is the same whichever 1D solver feeds the fluid.
  * UCT-HLL is the most diffusive: it suppresses KH growth at low
    resolution, and its MRI Maxwell stress is about a third of UCT-HLLD's
    (0.07 against 0.21).
  * The new formula reproduces the original UCT-HLL.
* **A second fourth-order FV realization, with point values**
  ([Berta et al. (2024)](/sources/berta-2024.md)). Also on the McCorquodale–Colella base, it
  differs from Felker & Stone in three ways.
  * MP5 and WENO-Z are rewritten to reconstruct interface values directly
    from cell-centre *point* values. There is one Riemann solve per face,
    with no extra solve on face-averaged states, and fewer ghost layers
    (3 instead of 4 transversally for the EMF).
  * The edge EMF uses the composition formula above: UCT-HLLD for MHD, and
    UCT-GFORCE extended to special-relativistic MHD.
  * A discontinuity detector (Jameson's pressure sensor, or a new
    odd/even-derivative ratio) triggers an order-reduction fallback. The
    point-value recovery and flux quadrature revert to second order, and
    the reconstruction drops to WENO3 or linear.
  
  Results: design order on vortices and CP Alfvén waves in MHD and RMHD.
  Numerical decay of Alfvén waves scales as $N^{-5}$, against $N^{-3}$ at
  second order. Accuracy that needs $512^3$ at second order is reached
  with about $34^3$. The fallback was essential on the blast and the
  cloud–shock problem. AMR and non-Cartesian grids are left to companion
  work.
* **A finite-volume ADER realization for relativistic MHD** ([Balsara & Kim (2016)](/sources/balsara-kim-2016.md), §4.2).
  The four states meeting at a vertex feed a two-dimensional MuSIC Riemann
  solver: 1D HLLC or HLLEM problems bound a strongly interacting state,
  which carries a linear sub-structure in the entropy and Alfvén waves.
  The edge field is the mean of two components of the resulting vertex
  fluxes, so it is single-valued and multidimensionally upwinded.
  Whether the scheme meets UCT's other requirements (staggered normal
  components in the momentum and energy fluxes, face fields not
  reconstructed along their own direction) is not stated. The paper
  reconstructs a zone-centred field and does not say how it relates to
  the face fields.
* **A finite-difference realization, to ninth order** ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md)). Zone-centred
  variables are point values advanced by alternative-FD WENO; only the
  face-averaged $B_h$ keeps a finite-volume, Stokes-law update.
  * No volumetric divergence-free reconstruction is built. Face fields
    are reconstructed in 2D within each face, then interpolated to zone
    centres for the fluxes.
  * The edge EMF from a 2D LLF Riemann solver is the average of the four
    zone-centred point values of $E$, WENO-interpolated to the edge, plus
    a dissipation term proportional to the jumps of the face-reconstructed
    normal fields at that edge. An HLL version with eight supersonic cases
    is also given.
  * Point values of the EMF are turned into edge averages by 1D WENO
    interpolation along the edge.
  * The same algorithm covers electrodynamics, MHD and relativistic MHD.
    Design orders 3, 5, 7 and 9 are met. On one core the FD scheme is 7 to
    14 times faster than an FV-WENO scheme in 2D and 5 to 12 times in 3D,
    without the ADER and flux-count economies FV could use.
* **Same construction for SR and GR MHD**, per the authors. They also claim
  a natural extension to AMR and unstructured grids; for the unstructured
  triangular counterpart they cite De Sterck's MUCT.

# Citations

1. [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md), §§1.1, 2.1–2.4, 3, 4, Appendix A.
2. [Londrillo & Del Zanna (2000)](/sources/londrillo-delzanna-2000.md): the original four-state EMF and staggering-from-consistency argument.
3. [Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md), §3.2.2: the first-order equivalence with $\mathcal{E}^\circ$.
4. [Felker & Stone (2018)](/sources/felker-2018.md), §§4–5, Appendix A.
5. [Mignone & Del Zanna (2021)](/sources/mignone-2021.md), §§4–7.
6. [Berta et al. (2024)](/sources/berta-2024.md), §§3–6, Appendix B.
7. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §§1–4, 6, 7.4.
8. [Balsara & Kim (2016)](/sources/balsara-kim-2016.md), §4.2.

---
type: Result
title: "Local conservation is equivalent to a flux form"
description: "Coppola and Veldman prove that a banded periodic matrix has vanishing column sums iff it factors as (I − T⁻¹)F, so for volume-consistent schemes global conservation of a linear invariant implies local conservation with an explicit face flux, and every globally conservative finite-difference scheme is a cell-centred finite-volume scheme; the same zero-sum-to-flux step makes subcell limiting and time blending conservative."
status: established
aliases: [global conservation implies local conservation, flux-form equivalence, finite-difference finite-volume equivalence, discrete main theorem of calculus]
tags: [finite-difference, finite-volume, kinetic-energy-preserving, dg]
timestamp: 2026-10-23T23:45:00Z
---

# Local conservation is equivalent to a flux form

A semi-discretization $V\frac{d}{dt}\phi+\mathcal C\phi=0$ is
*volume-consistent* when $V$ is a diagonal matrix of control volumes, so
that $\mathbf 1^\top V\phi$ approximates $\int\phi\,dx$ (page-local $V$,
$\mathcal C$ and $\phi$; [Coppola & Veldman (2023)](/sources/coppola-2023.md),
§2.4, Eqs. (18)–(19)). On a periodic grid it is:

- **globally conservative** when $\mathbf 1^\top\mathcal C\phi=0$ for every
  $\phi$, i.e. the column sums of $\mathcal C$ vanish (Eq. (20));
- **locally conservative** when it has a flux form,
  $\mathcal C\phi=(I-\mathcal T^{-1})\mathbf F\phi$ (Eq. (21)).

Here $\mathcal T$ is the page-local periodic shift, $(\mathcal T\phi)_i=\phi_{i+1}$,
and component $i$ of $\mathbf F\phi$ is the flux at $x_{i+1/2}$. The theorem
says the two notions coincide.

## Statement

**Lemma A.1** (Coppola & Veldman (2023), App. A.1). Let
$D=\sum_{k=-\bar k}^{\bar k}\mathrm{diag}(\mathsf c_k)\,\mathcal T^k$ be a periodic
banded matrix with semi-bandwidth $\bar k$ and diagonals $\mathsf c_k$
(page-local). Then $D=(I-\mathcal T^{-1})F$ for some banded $F$ **iff** all
column sums of $D$ vanish, $\sum_k\mathcal T^{-k}\mathsf c_k=\mathbf 0$. The flux
matrix is explicit:

$$F=\sum_{k=-\bar k}^{\bar k}\mathrm{diag}(\mathsf b_k)\,\mathcal T^k,\qquad \mathsf b_k=\sum_{h=k}^{\bar k}\mathcal T^{k-h}\mathsf c_h ,$$

with inverse $\mathsf c_k=\mathsf b_k-\mathcal T^{-1}\mathsf b_{k+1}$ (Eqs. (A.1)–(A.3)).
The authors call it "a discrete relative of the Main Theorem of calculus".

**Example** *(compiler check, not in the sources)*. Take the central
difference $D=\tfrac12(\mathcal T-\mathcal T^{-1})$, so $\mathsf c_1=\tfrac12$ and
$\mathsf c_{-1}=-\tfrac12$. The lemma gives $\mathsf b_{-1}=0$,
$\mathsf b_0=\mathsf b_1=\tfrac12$, i.e. $F=\tfrac12(I+\mathcal T)$, the face flux
$\tfrac12(\phi_i+\phi_{i+1})$. Indeed
$(I-\mathcal T^{-1})\tfrac12(I+\mathcal T)=\tfrac12(\mathcal T-\mathcal T^{-1})$.

## Consequences

- **Global equals local** (Observation 1, §2.4). For volume-consistent
  discretizations of transport equations, discrete global and local
  conservation are equivalent, both characterized by vanishing column sums.
  Coppola & Veldman cite Perot for the same principle: any globally
  conservative method with locally supported weight functions is locally
  conservative.
- **Finite differences are finite volumes** (Observations 3 and 5, §3.2–3.4).
  - The divergence form $V\frac{d\rho}{dt}=-D(\rho v)$ conserves iff $D$ has
    vanishing column sums. Derivative matrices with vanishing row sums have
    them if they are (skew-)symmetric or circulant.
  - Every split discretization that conserves mass globally is a
    cell-centred finite-volume scheme. Its face mass flux has explicit
    coefficients (Eq. (53)).
  - The classical second-order Lagrangian derivative on a non-uniform grid
    is neither skew-symmetric nor circulant and does not conserve (Eq. (35)).
  - See [conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
    and [split convective forms](/methods/split-convective-forms.md).
- **Quadratic invariants** (Lemma A.3, Corollary A.4). The discrete product
  rule $\mathrm{diag}(\phi)D\psi-\mathrm{diag}(\psi)D^\top\phi=(I-\mathcal T^{-1})\mathbf f$
  holds for any banded $D$ with an explicit $\mathbf f$, with no row- or
  column-sum assumption. For skew-symmetric $D$ this makes global
  kinetic-energy conservation local as well
  ([kinetic energy preservation](/properties/kinetic-energy-preservation.md)).

## The same structure in nodal DG

Diagonal-norm SBP discretizations have the analogous property. As recalled
by [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md)
after Fisher & Carpenter, they can be rewritten as differences of
inter-node fluxes. The DGSEM, surface terms included, takes the subcell
flux form of their Eqs. (8)–(11), which gives subelement-wise conservation.
[Ranocha et al. (2023)](/sources/ranocha-2023.md) state the same for the
flux-differencing DG form with diagonal mass and boundary operators (§2,
after Eq. (2.5)). See [flux differencing](/methods/flux-differencing.md) and
[summation-by-parts operator](/operators/summation-by-parts-operator.md).

The property survives dense norms and a filter on the volume terms.
[Cicchino et al. (2022)](/sources/cicchino-2022.md) (§3.1.1, Eqs. (34)–(42)) prove it for
their nonlinearly stable split form of energy-stable
[flux reconstruction](/methods/flux-reconstruction.md) applied to Burgers' equation, a modal
or nodal scheme of degree $N$ in which both the conservative and the non-conservative volume
terms of $\alpha\,\partial_x(\tfrac12u^2)+(1-\alpha)\,u\,\partial_xu$ and the face terms are
multiplied by the inverse of the filtered mass matrix $M+K_{\mathrm{FR}}$, with
$K_{\mathrm{FR}}=c_{\mathrm{FR}}(D^N)^\top MD^N$ (page-local $K_{\mathrm{FR}}$ and correction
parameter $c_{\mathrm{FR}}$, page-local split weight $\alpha\in[0,1]$, not the DG–FV blending coefficient; $M$ is dense in general). Testing with the constant function and
using the summation-by-parts property of the stiffness operator, which holds for any
quadrature exact to degree $2N-1$ and uncollocated nodes (Eq. (24)), they obtain for every
$\alpha$

$$\mathbf 1^\top(M+K_{\mathrm{FR}})\frac{d\hat u}{dt}=-\mathbf 1^\top\sum_{\text{faces}}(\text{face quadrature of }\hat n\,h)\quad(\text{Eq. (42), in words}),$$

i.e. the element integral changes only through the single-valued numerical face fluxes:
local, hence global, conservation. *(compiler check, not in the sources: $\mathbf 1^\top K_{\mathrm{FR}}=0$
because $D^N$ annihilates constants for $N\ge1$, so the left side is the time derivative of
the element integral itself.)* All schemes of their tests conserve to $O(10^{-16})$ (§4).

## Zero sums turned into fluxes: limiting and blending

The step "vanishing sum, hence differences of fluxes" is also how two sources keep
nonlinear corrections conservative.

- **Subcell limiting of DG** ([Pazner (2021)](/sources/pazner-2021.md), §4,
  Props. 8–10, Eqs. (49)–(57)). The antidiffusive residuals $r^H_i-r^L_i$ between the
  high- and low-order DG updates sum to zero over each element (Prop. 8) and, by the
  Kronecker structure, along every line of nodes in each direction (Prop. 9). Hence the
  nodal antidiffusive flux in direction $k$ is a difference of subcell-face fluxes,
  $r_{i,k}=r_{m_i^+,k}-r_{m_i^-,k}$, where the face flux $r_{m,k}$ is the sum of the nodal
  ones on one side of the face (page-local symbols). Limiting each face with the minimum of
  the coefficients of its two nodes is then conservative (Prop. 10), and with $2d$ provisional
  states per node it is also invariant-domain preserving (Prop. 11). *(compiler check, not
  in the sources: on one line this is Lemma A.1 above with the partial sums as flux, the
  zero line sum playing the role of the vanishing column sums.)* See
  [convex limiting](/methods/convex-limiting.md).
- **Blending in time** ([Puppo et al. (2023)](/sources/puppo-2023.md), §3.3.4,
  Eqs. (28)–(32)). The cell-wise blend of a high-order and a first-order implicit solution
  in [Quinpi](/methods/quinpi.md) leaves an interface mass defect, which is redistributed to
  the two neighbouring cells in proportion to their high-order weights; the result is a
  conservative scheme with an explicit interface flux, in which the high-order flux is
  weighted by the harmonic mean of the two cells' high-order weights. Without the correction
  the shock position is wrong (Fig. 7; see [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)).

**Upwind finite differences in flux form, and vertex residuals.**
[Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) (§3.1) write Iserles'
interpolatory upwind differences $\delta u_i=\sum_k\alpha^{\mathrm I}_ku_{i+k}$ (page-local
coefficients $\alpha^{\mathrm I}_k$, summing to zero) in conservative form,
$\delta u_i=\hat u_{i+1/2}-\hat u_{i-1/2}$ with face values $\hat u_{i+1/2}=\sum_k\beta^{\mathrm I}_ku_{i+k}$
and $\beta^{\mathrm I}_k=\sum_{m\ge k}\alpha^{\mathrm I}_m$. *(compiler check, not in the sources:
this is Lemma A.1 with constant diagonals, $\mathsf b_k=\sum_{h\ge k}\mathsf c_h$.)* In 2D the
nodal update of their [discrete kinetic relaxation scheme](/methods/discrete-kinetic-relaxation-scheme.md)
is split into four residuals sent by the quads around the node, and the residuals of one quad
sum to an approximation of the flux through its boundary, which "guarantees the local
conservation" and lets a single quad be recomputed by a first-order scheme in their MOOD step
without breaking it (§2.1, Eqs. (15)–(16), Fig. 1).

**Interface fluxes between phases.** In a conservative cut-cell scheme the two phases of a
cell are coupled only through an interfacial flux on the interface segment, entered with
opposite signs in the two phases. [Long et al. (2023)](/sources/long-2023.md) (§2.3, §3.2,
Eqs. (5), (26)–(27)) keep this structure with phase change: the liquid and vapour interfacial
fluxes, built from one phase-change Riemann solution, sum to
$\big[0,\ -\sigma_{\mathrm{st}}\kappa_{\mathrm c}n,\ \dot m\,Q_{\mathrm{lat}}-\sigma_{\mathrm{st}}\kappa_{\mathrm c}s_{\mathrm p}\big]^\top$
(page-local surface tension $\sigma_{\mathrm{st}}$, curvature $\kappa_{\mathrm c}$, mass flux $\dot m$,
latent heat $Q_{\mathrm{lat}}$, phase-interface speed $s_{\mathrm p}$). Mass is conserved exactly, and
the momentum and energy defects are the physical surface-tension force and the latent-heat
and surface-tension work, so total energy is conserved once the latent heat of the converted
mass is counted (Eq. (34)). The authors contrast this with ghost-fluid phase-change methods,
"inherently non-conservative", and state that reinitialization of the level set can still
delete under-resolved droplets and so break conservation (§1, §3.2). See
[Riemann solvers with phase change](/methods/phase-change-riemann-solver.md) and
[level-set methods](/methods/level-set-method.md).

**Flux balance at immersed walls.** [Başkaya et al. (2024)](/sources/baskaya-2024.md)
(§3, §5) compare the two ways of imposing a wall on a Cartesian finite-volume mesh for
reacting hypersonic flow ([immersed-boundary methods](/methods/immersed-boundary-method.md)).
Ghost-cell methods fill solid cells by extrapolation from an image point and reconstruct
fluxes "without considering the location and shape of the fluid-solid interface", so they do
not conserve mass, momentum and energy at the wall; the errors "result from the nonlinearity
of the flux function, from the image point interpolation, and from the interface curvature".
The cut-cell (cut-element) method of the INCA code keeps the flux balance over the fluid part
of each cut cell, with face fluxes scaled by the wetted areas and the wall exchange computed
from the boundary condition, and is "a consistent and conservative extension of the finite
volume flux balance" (§3.2). Switching the cut-cell flux treatment off in the same code gives
a ghost-cell method of nominally the same order, and only this switch separates the two runs
(§5). On the HEG cylinder with an isothermal 300 K wall the grid-converged stagnation heat flux
of the cut-cell method is 7.144 MW/m², against 7.345 MW/m² body-fitted and $7.402\pm0.220$ MW/m²
measured, while the ghost-cell method of a second code gives 0.167 MW/m² (Table 7); both
ghost-cell methods mispredict the cold-wall heat flux and overpredict the ablation blowing rate
(Fig. 18; [flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)). The
authors conclude that "conservation errors inherent to ghost-cell IB methods are responsible
for large errors at cold walls", acting as an unphysical surface blowing, and expect them to
converge at the truncation rate of the base scheme, hence to be small where wall gradients are
small, as on adiabatic walls (§4.5.2, §5); the convergence of the conservation error is stated,
not measured, and the evidence is two ghost-cell implementations.

A conservative scheme need not be written in flux form to conserve mass: the
semi-Lagrangian finite-volume update of [Zheng et al. (2022)](/sources/zheng-2022.md)
integrates the reconstruction over the upstream cell, cut by the Eulerian mesh and
integrated by Green's theorem as line integrals; the line integrals over interior mesh
segments are exact and cancel between neighbouring pieces, which gives mass conservation
for periodic data (Prop. 3.1, Eq. (25)), observed at $O(10^{-13})$ (Figs. 13, 18). See
[semi-Lagrangian finite-volume WENO](/methods/semi-lagrangian-finite-volume.md).

## Qualifications

- **Flux consistency is assumed.** The Lax–Wendroff consistency of the flux,
  i.e. that the face flux of a constant state $\phi=\phi_a\mathbf 1$ equals
  the physical flux, $\mathbf F\phi=f(\phi_a)\mathbf 1$, is
  *assumed* at the stated generality. The authors write "we can not (yet)
  prove this" (§2.4, Eq. (22)). The lemma provides a flux form, not its
  consistency. See [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md).
- **Periodic grids only.** The proofs are for periodic grids. The extension
  to non-periodic boundaries is only pointed to via SBP operators.
- **A dissenting remark on DG.** [Bai & Li (2022)](/sources/bai-2022.md) write in their
  introduction that for the DG method "the cost per cell is higher and the local conservation
  can not be easily guaranteed", whereas the finite-volume scheme "can easily achieve local
  conservation" (§1, p. 2). The remark is a passing characterization in a comparison of
  FD, FV and DG approaches to multiphase flow, with no argument, definition or reference
  attached, and it does not say which DG formulation is meant. It is at odds with the flux-form
  results recorded above for nodal DG (Rueda-Ramírez et al., Ranocha et al., Cicchino et al.);
  it is recorded here as an attributed remark, not as a contradiction, because no argument is
  given that could be weighed against those proofs. In Bai & Li's own sharp-interface DG
  scheme the non-conservative steps are elsewhere: ghost-fluid states, the projection mixing
  of cut cells and the deletion of isolated structures, whose mass loss is reported (§2.5,
  Fig. 6).
- **Diagonal control volumes.** Coppola & Veldman allow non-diagonal $V$ in
  principle (Remark 2) but prove the results for diagonal $V$.
- **Order on stretched grids.** The choice $V=\mathrm{diag}(D\mathbf x)$ keeps
  the order of $D$ on smoothly stretched grids. The local spacing
  $\tfrac12(x_{i+1}-x_{i-1})$ degrades a fourth-order formula to second order
  (Observation 2, §2.5). In tests it degrades fourth-order central and
  second-order dual-sided schemes to roughly first order (§7.2, Fig. 1).
  This is a question of accuracy, not of conservation.

# Citations

- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — §2.4 Eqs. (18)–(22) Observation 1 Remarks 1–2, §2.5 Observation 2, §3.2–3.4 Observations 3, 5 Eqs. (35), (53), App. A Lemma A.1 Eqs. (A.1)–(A.3), Lemma A.3, Corollary A.4, §7.2 Fig. 1.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.1 Eqs. (8)–(11).
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §2.
- [Pazner (2021)](/sources/pazner-2021.md) — §4, Props. 8–11, Eqs. (49)–(57) (arXiv v1).
- [Puppo et al. (2023)](/sources/puppo-2023.md) — §3.3.4, Eqs. (28)–(32), Fig. 7 (arXiv v2).
- [Zheng et al. (2022)](/sources/zheng-2022.md) — §2.3, Prop. 3.1, Figs. 13, 18.
- [Cicchino et al. (2022)](/sources/cicchino-2022.md) — §3.1 (Eqs. (24), (28)), §3.1.1 (Eqs. (34)–(42)), §4 (arXiv v1).
- [Bai & Li (2022)](/sources/bai-2022.md) — §1 (p. 2), §2.5, Fig. 6.
- [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) — §2.1 (Eqs. (15)–(16), Fig. 1), §3.1.
- [Long et al. (2023)](/sources/long-2023.md) — §1, §2.3 (Eq. (5)), §3.2 (Eqs. (26)–(27), (34)).
- [Başkaya et al. (2024)](/sources/baskaya-2024.md) — §3, §3.2, §4.5.2 (Table 7), §5 (Fig. 18) (author preprint).

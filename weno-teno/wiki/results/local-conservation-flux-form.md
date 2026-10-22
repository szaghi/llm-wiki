---
type: Result
title: "Local conservation is equivalent to a flux form"
description: "Coppola and Veldman prove that a banded periodic matrix has vanishing column sums iff it factors as (I − T⁻¹)F, so for volume-consistent schemes global conservation of a linear invariant implies local conservation with an explicit face flux, and every globally conservative finite-difference scheme is a cell-centred finite-volume scheme."
status: established
aliases: [global conservation implies local conservation, flux-form equivalence, finite-difference finite-volume equivalence, discrete main theorem of calculus]
tags: [finite-difference, finite-volume, kinetic-energy-preserving, dg]
timestamp: 2026-10-21T00:00:00Z
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

## Qualifications

- **Flux consistency is assumed.** The Lax–Wendroff consistency of the flux,
  i.e. that the face flux of a constant state $\phi=\phi_a\mathbf 1$ equals
  the physical flux, $\mathbf F\phi=f(\phi_a)\mathbf 1$, is
  *assumed* at the stated generality. The authors write "we can not (yet)
  prove this" (§2.4, Eq. (22)). The lemma provides a flux form, not its
  consistency. See [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md).
- **Periodic grids only.** The proofs are for periodic grids. The extension
  to non-periodic boundaries is only pointed to via SBP operators.
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

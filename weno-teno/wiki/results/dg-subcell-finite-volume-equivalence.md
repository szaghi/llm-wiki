---
type: Result
title: "Equivalence of DG and subcell finite volumes"
description: "Vilar and Abgrall prove that a degree-N DG scheme on any polygonal cell split into as many subcells as degrees of freedom, with an invertible projection onto subcell means, is exactly a finite-volume scheme on those means with explicit reconstructed fluxes on the interior subcell faces and the DG numerical flux on the cell boundary."
status: established
aliases: [DG as subcell finite volumes, reconstructed subcell fluxes, subcell flux form of DG, Vilar reconstructed flux, DG–FV equivalence]
tags: [dg, finite-volume, limiting, conservation]
timestamp: 2026-10-23T15:13:00Z
---

# Equivalence of DG and subcell finite volumes

A [discontinuous Galerkin](/methods/discontinuous-galerkin.md) scheme of
degree $N$ on a cell can be rewritten, without approximation, as a
conservative finite-volume scheme on the mean values of the solution over a
partition of the cell into subcells. The subcell faces inside the cell carry
*reconstructed fluxes* determined by the DG residual, and the faces on the
cell boundary carry the DG numerical flux. The statement is due to
[Vilar & Abgrall (2024)](/sources/vilar-2024.md) on 2D unstructured and
polygonal grids, extending Vilar's 1D result; on tensor-product
Legendre–Gauss–Lobatto elements the same structure is the subcell flux
form of the [DGSEM](/methods/dgsem.md). It is the exact foundation of
limiters that correct DG at the subcell level
([MOOD-type a posteriori limiting](/methods/mood-a-posteriori-limiting.md),
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).

## Setting

Scalar law $\partial_tu+\nabla\cdot f(u)=0$ in 2D, cell $K$, modal DG
solution $u_h=\sum_{p=1}^{n_N}u_p\sigma_p$ with $n_N=(N+1)(N+2)/2$
basis functions $\sigma_p$ of $\mathbb P^N$ (page-local), matrix form
$M\,dU/dt=\Phi$ with mass matrix $M$ and residual

$$\Phi_m=\int_Kf(u_h)\cdot\nabla\sigma_m\,dx-\int_{\partial K}\sigma_m\,h_n\,dS,$$

$h_n$ the normal numerical flux (global Lax–Friedrichs in the paper)
(Eqs. (2.1)–(2.8)). Split $K$ into $n_N$ subcells $S_m$ and let $\bar u_m$
be the subcell means (*submeans*). Then $d\bar U/dt=PM^{-1}\Phi$ with the
projection matrix $P_{mp}=\frac1{\lvert S_m\rvert}\int_{S_m}\sigma_p\,dx$
(Eqs. (2.9)–(2.13)). A subdivision is admissible iff $P$ is invertible;
with more subcells than degrees of freedom a left inverse $P^+$ with
$P^+P=I$ returns the moments in the least-squares sense (Remark 1)
(page-local $P$, $P^+$, $n_N$, $\sigma_p$).

Write the subcell update in flux form,
$\frac{d\bar u_m}{dt}=-\frac1{\lvert S_m\rvert}\sum_{\text{faces }mp}\varepsilon_{mp}\hat F_{mp}$,
with face-integrated fluxes $\hat F_{mp}=\hat F_{pm}$, orientation signs
$\varepsilon_{mp}=-\varepsilon_{pm}\in\{0,\pm1\}$, and the boundary condition
$\hat F=h_n$ on $\partial K$ (Eqs. (2.14)–(2.19)). Collecting the interior
fluxes in a vector $\hat F$ gives the linear system

$$-A\hat F=\mathsf VPM^{-1}\Phi+b,$$

with $A_{mp}=\varepsilon_{mp}$ the subcell–face adjacency matrix,
$\mathsf V=\mathrm{diag}(\lvert S_1\rvert,\dots,\lvert S_{n_N}\rvert)$ and
$b_m=\int_{\partial S_m\cap\partial K}h_n\,dS$ (page-local $A$,
$\mathsf V$, $b$; Eqs. (2.20)–(2.21)).

## Theorem 2.1 (reconstructed fluxes from the residual)

The subgrid graph Laplacian $\mathsf L=AA^\top$ has rank $n_N-1$ and kernel
spanned by $\mathbf 1$. With $\Pi=\frac1{n_N}\mathbf 1\mathbf 1^\top$ and
any scalar $c_\Pi\ne0$ (page-local), its generalized inverse
$\mathsf L^+=(\mathsf L+c_\Pi\Pi)^{-1}-c_\Pi^{-1}\Pi$ (a technique Vilar &
Abgrall take from Abgrall's work on residual distribution) gives

$$\hat F=-A^\top\mathsf L^+\big(\mathsf VPM^{-1}\Phi+b\big)\qquad\text{(Eq. (2.23))}.$$

**Theorem 2.1.** The DG scheme $dU/dt=M^{-1}\Phi$ is equivalent to the
subcell finite-volume scheme $d\bar U/dt=-\mathsf V^{-1}(A\hat F+b)$ with
$\hat F$ of Eq. (2.23); the moments are recovered by
$dU/dt=-(\mathsf VP)^{-1}(A\hat F+b)$ (Eqs. (2.24)–(2.26)).

The right-hand side sums to zero over the cell because testing the DG
scheme with the constant function gives the cell-average equation; this is why the system is
solvable *(compiler check, not in the sources)*. When the subcell graph
has cycles, as on triangles, $A\hat F=r$ has many solutions, and
$\hat F=A^\top\mathsf L^+r$ is the one of minimum Euclidean norm *(compiler
check, not in the sources)*. Vilar & Abgrall note that the choice of the
boundary flux is "not unique" but recovers the cell-average equation.

Only $\Phi$ and $b$ depend on time; $P$, $A$ and $\mathsf L^+$ are
precomputed, and for cells mapped to a reference element they depend only
on the order and the subdivision (Remark 2).

## Theorem 2.2 (reconstructed fluxes from the fluxes)

Replace $f(u_h)$ by its $L^2$ projection $f_h$ onto $(\mathbb P^{N+1})^2$
(unnecessary for nodal, collocated DG) and define the *sub-resolution
basis functions* $\phi_m\in\mathbb P^N$ by
$\int_K\phi_m\psi\,dx=\int_{S_m}\psi\,dx$ for all $\psi\in\mathbb P^N$, the
$L^2$ projections of the subcell indicator functions (Eqs. (2.27)–(2.28)).
Then

$$\hat F=F-A^\top\mathsf L^+G,\qquad G_m=\int_{\partial K}\tilde\phi_m\,(f_h\cdot n-h_n)\,dS,$$

with $F$ the face integrals of the interior polynomial flux $f_h\cdot n$ on
the subcell faces and $\tilde\phi_m=\phi_m-1$ on $\partial K\cap\partial
S_m$, $\phi_m$ elsewhere on $\partial K$ (Eqs. (2.33)–(2.38); page-local
$F$, $G$, $\phi_m$). **Theorem 2.2** states the same equivalence with
these fluxes. The reconstructed flux is the interior flux minus a
correction that distributes the boundary jump $f_h\cdot n-h_n$ inside the
cell, weighted by the sub-resolution functions: in DG, the numerical
diffusion of the interface flux jump is spread onto the subcell faces.
Dropping the correction, $\hat F=F$, gives Wang's spectral volume scheme
(Remark 4). The authors draw the analogy with SBP-SAT and with CPR
([flux reconstruction](/methods/flux-reconstruction.md)). They call
Theorems 2.1 and 2.2 "perfectly equivalent"; the residual form is simpler
to implement and needs no sub-resolution functions (§2.2).

## Evidence

- **Independence of the subdivision.** Uncorrected DG written as subcell
  finite volumes gives exactly the same solution for the four subdivisions
  tested (uniform and non-uniform structured, uniform and non-uniform
  Voronoi-type polygonal) on a crenel advected over five periods at fourth
  order on 576 cells (§4.1.1, Figs. 16–18).
- **Conditioning.** The $\lVert\cdot\rVert_\infty$ condition numbers of
  $P$ grow with the order and are larger for structured than polygonal and
  for uniform than non-uniform subdivisions; at $\mathbb P^3$, 31.75, 29.28,
  27.89 and 26.94 (Table 2).
- With the correction switched on, the subdivision matters: uniform ones
  resolve better, which the authors trace to the numerical admissibility
  detector's dependence on the subcell aspect ratio
  (§4.1.1, Figs. 19–21; see
  [MOOD-type a posteriori limiting](/methods/mood-a-posteriori-limiting.md)).

## Relation to other subcell flux forms

On collocated LGL nodes the diagonal mass matrix lets the DGSEM, surface
terms included, be written as differences of inter-node fluxes, which
differ from Fisher & Carpenter's because the surface terms are transformed
too, the nodal values acting as subcell values of widths
$\mathsf w_i$ (as recalled by
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md),
Eqs. (8)–(11); [DGSEM](/methods/dgsem.md),
[local conservation](/results/local-conservation-flux-form.md)). Theorem
2.1 does the same for modal DG on unstructured cells, where no diagonal
norm exists, at the price of a small dense linear algebra per cell shape.
[Deng et al. (2025)](/sources/deng-2025.md) take the opposite route for
modal Legendre DG: they treat the Gauss-point values as subcell means of
widths equal to the Gauss weights, without exact averaging, and side with
Hennemann et al. that projecting DG data onto equidistant subcells gives a
non-conservative blended form (§1, §3.2;
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).

## Qualifications

- The theorems are stated for scalar laws; the paper applies the
  construction to the Euler equations in §4.3 without restating them for
  systems.
- Equivalence needs exactly $n_N$ subcells and an invertible $P$; with more
  subcells only the least-squares return of Remark 1 is available.
- In the preprint read, §3.4 divides each $\mathbb P^5$ cell into "20
  subcells" because "the dimension of $P^5$ is 20"; the paper's own formula
  $n_N=(N+1)(N+2)/2$ gives $n_5=21$ *(compiler check, not in the
  sources)*.

# Citations

- [Vilar & Abgrall (2024)](/sources/vilar-2024.md) — §2.1 Eqs. (2.1)–(2.26), Thm. 2.1, Remarks 1–2; §2.2 Eqs. (2.27)–(2.40), Thm. 2.2, Remark 4; §4.1.1 Table 2, Figs. 16–21; §4.3 (HAL preprint v1).
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.1 Eqs. (8)–(11).
- [Deng et al. (2025)](/sources/deng-2025.md) — §1, §3.2.

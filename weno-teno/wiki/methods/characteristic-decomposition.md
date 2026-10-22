---
type: Method
title: "Characteristic decomposition"
description: "Local characteristic decomposition projects stencil data onto the eigenvectors of the flux Jacobian at an interface state, reconstructs each field separately and projects back; the bundle's WENO, TENO and central-upwind schemes rely on it to suppress oscillations, while OEDG shows a method that does without it."
status: established
aliases: [local characteristic decomposition, LCD, characteristic-wise reconstruction, characteristic projection, reconstruction in characteristic variables]
tags: [characteristic, reconstruction, weno, teno, central-scheme]
timestamp: 2026-10-21T00:00:00Z
---

# Characteristic decomposition

For a system $\partial_tu+\partial_xf(u)=0$, $u\in\mathbb R^m$, a nonlinear reconstruction
applied component by component to the conserved variables couples the fields at a
discontinuity and produces oscillations. Local characteristic decomposition freezes the
Jacobian at an interface: with $R_{i+1/2}$, $L_{i+1/2}=R_{i+1/2}^{-1}$ the right- and
left-eigenvector matrices of $A$ at an average of the two neighbouring states, every datum of
the stencil is projected, $\zeta_k=L_{i+1/2}u_k$ (page-local symbol), the scalar
reconstruction is applied to each of the $m$ fields, and the result is projected back with
$R_{i+1/2}$. The same matrix is used for all stencil points of one interface, so the
projection is linear and exactly invertible.

## Finite-difference and finite-volume algorithms

[Fu (2023)](/sources/fu-2023.md) gives both algorithms for TENO (§3.4 Algorithm 1, §3.6
Algorithm 2), and they are the ones used, with WENO in place of TENO, across the
finite-difference papers of this bundle.

- **Finite difference** (Algorithm 1): at $x_{i+1/2}$, with Roe-average eigenvectors, project
  the point values and point fluxes of the $K$-point stencil,
  $\zeta_k=L_{i+1/2}u_k$, $g_k=L_{i+1/2}f(u_k)$ (page-local $g_k$); split each field by
  [Lax–Friedrichs](/methods/lax-friedrichs-flux.md),
  $g^{(l)\pm}=\tfrac12\big(g^{(l)}\pm a^{(l)}\zeta^{(l)}\big)$, with $a^{(l)}$ the maximum
  $l$-th characteristic speed over the whole domain; reconstruct $\hat g^{(l)\pm}_{i+1/2}$;
  sum, and return $\hat f_{i+1/2}=R_{i+1/2}\hat g_{i+1/2}$.
- **Finite volume** (Algorithm 2): project the cell averages with Roe-average eigenvectors,
  reconstruct $u^\mp_{i+1/2}$ in characteristic space, project back, then call a Riemann
  solver; conservative variables are reconstructed in characteristic space "towards better
  oscillation suppressing".

Users of the finite-difference algorithm with Lax–Friedrichs splitting (the averaged state is
listed below): [Fu (2021)](/sources/fu-2021.md) (§5; Rusanov splitting, LLF for extreme
cases), [Li et al. (2022)](/sources/li-2022-b.md) ("global Lax–Friedrichs flux splitting with
local characteristic fields", with Eq. (38)), [Luo & Wu (2021)](/sources/luo-2021-b.md) (§5),
[Takagi et al. (2022)](/sources/takagi-2022.md) (§4, where THINC is applied per characteristic
component and per split-flux direction), and [Wang & Don (2022)](/sources/wang-2022-b.md)
(§3.3, well-balanced shallow-water WENO). [Wang et al. (2023)](/sources/wang-2023-b.md) apply
it to the WENO-Z *interpolation* of point values in [A-WENO](/methods/alternative-weno.md)
(§2).

## Variants of the frozen state and of where the projection acts

- **Averaged state.** Roe averages in [Fu (2023)](/sources/fu-2023.md),
  [Fu (2021)](/sources/fu-2021.md), [Luo & Wu (2021)](/sources/luo-2021-b.md),
  [Takagi et al. (2022)](/sources/takagi-2022.md) and [Wang & Don (2022)](/sources/wang-2022-b.md);
  an arithmetic average of primitive variables (with $E$ and $H$ derived from it) in
  [Chertock et al. (2023)](/sources/chertock-2023.md) (Apps. A–B), which state that
  $\hat u_{i+1/2}=\tfrac12(\bar u_i+\bar u_{i+1})$ "or another type of average" may be used
  (§2.1).
- **Per zone instead of per interface.** [Balsara et al. (2024)](/sources/balsara-2024.md)
  reconstruct once per zone, in the characteristic variables of zone $i$, obtaining both
  $u^-_{i+1/2}$ and $u^+_{i-1/2}$ from one projection (§VI, steps 2–3); this is what lets
  their [fluctuation-form scheme](/methods/fluctuation-form-fd-weno.md) use one
  reconstruction per zone instead of two.
- **In the numerical diffusion, not only in the reconstruction.**
  [Chertock et al. (2023)](/sources/chertock-2023.md) use the projection also to give each
  field its own central-upwind diffusion, the
  [LCD central-upwind scheme](/methods/lcd-central-upwind-scheme.md) (§3).

For the Euler equations, [Chertock et al. (2023)](/sources/chertock-2023.md) (App. A) print,
at the averaged state with velocity $v$, sound speed $c$ and enthalpy $H$,

$$R_{i+1/2}=\begin{pmatrix}1&1&1\\ v-c&v&v+c\\ H-vc&\tfrac12v^2&H+vc\end{pmatrix},$$

and its inverse with $2H-v^2=2c^2/(\gamma-1)$; App. B gives the 2D version.

## Why it is used, and what it costs

[Chertock et al. (2023)](/sources/chertock-2023.md) (§2.1) state that the minmod limiter
applied to conservative variables "typically leads to large oscillations", which is why it is
applied to characteristic variables. [Fu (2023)](/sources/fu-2023.md) (§3.4) makes the cost
explicit: the hybrid TENO uses the optimal linear scheme **without** characteristic
decomposition wherever the TENO indicator flags smoothness and reports an overall efficiency
gain "by a factor of four" ([hybrid central-WENO schemes](/methods/hybrid-weno.md)).

[Wang & Don (2022)](/sources/wang-2022-b.md) (§3.3) use the linearity of the projection: an
[affine-invariant WENO](/methods/affine-invariant-weno.md) operator stays affine invariant in
characteristic variables, so the shallow-water still-water state is preserved without
further linearization ([well-balancing](/properties/well-balancing.md)).

## A method that needs none

[Peng et al. (2024)](/sources/peng-2024.md) apply the [OEDG](/methods/oedg.md) damping to
the conservative variables with one coefficient (the maximum over components), without
characteristic decomposition (§2, Eq. (2.17)). They argue (Remark 2.12) that eigenvectors are
defined only up to scaling, so a damping coefficient that is not
[scale invariant](/properties/scale-invariance.md) depends on that arbitrary choice when
applied in characteristic variables, and a characteristic decomposition can destroy scale
invariance. On the [Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md)
(640 cells) OEDG works with or without it, while the earlier OFDG without it "smears much"
(Ex. 5.7, Fig. 4).

## Qualifications

- Chertock et al. evaluate the field speeds at the reconstructed states while $R$
  diagonalizes the Jacobian at a third state; for nonlinear systems the per-field quantities
  are therefore an approximation, not an exact diagonalization.
- [Fu (2023)](/sources/fu-2023.md) calls the splitting with a global per-field maximum speed
  "Rusanov"; most of the literature calls it global Lax–Friedrichs (naming convention, see
  [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)).

# Citations

- [Fu (2023)](/sources/fu-2023.md) — §3.4 (Algorithm 1, hybrid TENO, Eqs. (21)–(24)), §3.6 (Algorithm 2).
- [Chertock et al. (2023)](/sources/chertock-2023.md) — §2.1 (Eqs. (2.5)–(2.8)), §3, Apps. A–B (arXiv v2).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §VI (pointwise algorithm, steps 2–3).
- [Fu (2021)](/sources/fu-2021.md) — §5.
- [Li et al. (2022)](/sources/li-2022-b.md) — Eq. (38) and the numerical set-up.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §5.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4, §4.11.
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.3.
- [Wang et al. (2023)](/sources/wang-2023-b.md) — §2.
- [Peng et al. (2024)](/sources/peng-2024.md) — §2 (Eq. (2.17), Remark 2.12), Ex. 5.7.

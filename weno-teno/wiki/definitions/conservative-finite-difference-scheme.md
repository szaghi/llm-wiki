---
type: Definition
title: "Conservative finite-difference scheme"
description: "A conservative finite-difference scheme evolves point values by differences of numerical fluxes at half points, du_i/dt = −(f̂_{i+1/2} − f̂_{i−1/2})/Δx, with the flux built so that the difference approximates ∂_x f to high order; the sources build it by reconstructing split point fluxes, by interpolating states with derivative corrections, or in fluctuation form."
status: established
aliases: [conservative FD scheme, Shu–Osher finite difference, FD-WENO, finite-difference flux reconstruction, flux-difference form]
tags: [finite-difference, reconstruction, weno, teno]
timestamp: 2026-10-21T12:00:00Z
---

# Conservative finite-difference scheme

A conservative finite-difference (FD) scheme for $\partial_tu+\partial_xf(u)=0$ evolves the **point
values** $u_i\approx u(x_i)$ on a uniform grid by the flux-difference form

$$\frac{du_i}{dt}=-\frac{1}{\Delta x}\big(\hat f_{i+1/2}-\hat f_{i-1/2}\big),$$

(Li et al. 2022, Eq. (2); Fu 2023, Eq. (2); Takagi et al. 2022, Eq. (4); Fu 2021, Eq. (8)). The
fluxes telescope, so the sum of $u_i\Delta x$ changes only through boundary fluxes. The difference
from a finite-volume scheme lies in what $\hat f_{i+1/2}$ must approximate: in FD the flux difference
divided by $\Delta x$ must equal $\partial_xf$ at $x_i$ to high order, whereas a finite-volume flux is
the physical flux at the interface.

## Shu–Osher flux reconstruction

The classical construction (Shu & Osher, as recalled by Fu 2021, §2 and Takagi et al. 2022, §2.1)
introduces a function $\phi$ (page-local) defined implicitly by

$$f\big(u(x)\big)=\frac1{\Delta x}\int_{x-\Delta x/2}^{x+\Delta x/2}\phi(\xi)\,d\xi ,$$

so that $\partial_xf(u(x_i))=\big(\phi(x_{i+1/2})-\phi(x_{i-1/2})\big)/\Delta x$ exactly. The point
fluxes $f_i$ are then the cell averages of $\phi$, and any finite-volume reconstruction of $\phi$ at
$x_{i+1/2}$ from the $f_j$ yields a high-order $\hat f_{i+1/2}$ (Fu 2021, Eqs. (6)–(10)). Upwinding
requires a [flux splitting](/methods/lax-friedrichs-flux.md) $f=f^++f^-$ with
$\pm\partial f^\pm/\partial u\ge0$: $\hat f^+_{i+1/2}$ is reconstructed from a left-biased stencil,
$\hat f^-_{i+1/2}$ by mirror symmetry, and $\hat f_{i+1/2}=\hat f^+_{i+1/2}+\hat f^-_{i+1/2}$ (Li et
al. 2022, §2). For systems the reconstruction is applied to characteristic projections of the split
fluxes ([characteristic decomposition](/methods/characteristic-decomposition.md)); Fu (2023,
Algorithm 1) gives the full sequence with Roe-averaged eigenvectors and a Rusanov splitting that uses
the maximum characteristic speed over the whole domain. Multi-dimensional schemes apply the 1-D
operator dimension by dimension. [WENO-JS](/methods/weno-js-reconstruction.md),
[WENO-Z](/methods/weno-z.md), [WENO-ZN](/methods/weno-zn.md), [TENO](/methods/targeted-eno.md) and
[TENO-THINC](/methods/teno-thinc.md) are used in this form in the bundle. Takagi et al. (2022, §2.1)
call $\phi$ the "primitive function" and the $f_i$ "cell-averaged values".

Balsara et al. (2024, §I) recall that Shu–Osher FD-ENO schemes "offered high order accuracies at a
price point that is much lower than their finite volume counterparts of comparable order for
multidimensional problems", and note that for linear systems with constant coefficients the
dimension-by-dimension FD scheme keeps pointwise accuracy in several dimensions (§II).

## Other flux constructions

- **Alternative formulation.** The flux is a monotone two-point flux of *interpolated* states plus
  even-derivative corrections,
  $\hat f_{i+1/2}=h(u^-_{i+1/2},u^+_{i+1/2})-\tfrac1{24}\Delta x^2(\partial_x^2f)_{i+1/2}+\tfrac{7}{5760}\Delta x^4(\partial_x^4f)_{i+1/2}+\dots$
  (Ye et al. 2022, Eqs. (11)–(13); Wang et al. 2023, Eqs. (2)–(4)). Any Riemann solver can be used
  and any variables interpolated ([alternative WENO](/methods/alternative-weno.md),
  [AFTENO](/methods/afteno.md)). Ye et al. (2022, §1) draw the load-bearing distinction: classical
  WENO/TENO *reconstruct* split fluxes, the alternative family *interpolates* states.
- **Weighted compact nonlinear schemes.** Fu (2023, §3.7) recalls the three steps of WCNS:
  nonlinear node-to-interface interpolation, interface flux evaluation, compact interface-to-node
  flux differencing, and names the lack of conservation as the main flaw of the family
  ([WCNS](/methods/weighted-compact-nonlinear-scheme.md)).
- **Fluctuation form.** For systems with non-conservative products, Balsara et al. (2024, Eq. (4.1))
  replace the flux difference by an internal term plus boundary fluctuations,
  $\frac{du_i}{dt}=-A(u_i)\frac{u^-_{i+1/2}-u^+_{i-1/2}}{\Delta x}-\frac1{\Delta x}\big(D^-_{i+1/2}+D^+_{i-1/2}\big)$,
  with one WENO reconstruction of the point values per zone (page-local fluctuations $D^\pm$). For a
  linear constant-coefficient system with the local Lax–Friedrichs limit it is algebraically
  identical to the upwind FD scheme $-A^+\frac{u^-_{i+1/2}-u^-_{i-1/2}}{\Delta x}-A^-\frac{u^+_{i+1/2}-u^+_{i-1/2}}{\Delta x}$,
  which they state reduces to Shu–Osher LLF FD-WENO for linear fluxes (§V)
  ([fluctuation-form FD-WENO](/methods/fluctuation-form-fd-weno.md)).

## Conservation in matrix form

Coppola & Veldman (2023) write a semi-discretization as $V\frac{d}{dt}\phi+\mathcal C\phi=0$ with a
diagonal control-volume matrix $V$ on a periodic, possibly non-uniform grid (page-local $V$,
$\mathcal C$, $\phi$, shift $\mathcal T$ and flux matrix $\mathbf F$, as on the
[local conservation](/results/local-conservation-flux-form.md) page). Global conservation of a linear
invariant is equivalent to vanishing column sums of $\mathcal C$ (§2.4, Eq. (20)), and their Lemma A.1
shows that any such matrix factors as a flux difference, $\mathcal C=(I-\mathcal T^{-1})\mathbf F$
with an explicit numerical flux $\mathbf F$. Hence, for volume-consistent discretizations, global and
local conservation coincide (Observation 1), and every FD scheme built from divergence and advective
forms that conserves mass globally is a cell-centred finite-volume scheme (Observation 5;
[local conservation and flux form](/results/local-conservation-flux-form.md)).
Choosing $V=\mathrm{diag}(D\,x)$, with $D$ the (page-local) derivative matrix applied to the
coordinates, keeps the design order on smoothly stretched grids, whereas the local spacing
$\tfrac12(x_{i+1}-x_{i-1})$ reduces a fourth-order formula to second order (Observation 2, §2.5);
numerically the degradation is to "roughly first order" (§7.2, Fig. 1b). The consistency assumption needed for the
[Lax–Wendroff theorem](/results/lax-wendroff-theorem.md), that the flux of a constant state is the
physical flux, is assumed rather than proved at this generality (§2.4, Eq. (22)).

## Qualifications

- The flux-difference form makes a scheme conservative; it does not by itself make it high order.
  Wang et al. (2023, §1) stress that in the FD context a standard finite-volume two-point flux is
  limited to second order, and that the high order of A-WENO comes from the derivative corrections.
- Balsara et al. (2024, §II) reject the naive nonlinear upgrade of the linear upwind FD scheme
  (frozen $A(u_i)^\pm$) because it cannot preserve a stationary contact; their fluctuation form
  restores it with anti-diffusive terms ([stationary contact
  preservation](/properties/stationary-contact-preservation.md)).

# Citations

- [Li et al. (2022)](/sources/li-2022-b.md) — §2, Eqs. (1)–(4).
- [Fu (2021)](/sources/fu-2021.md) — §2, Eqs. (4)–(10).
- [Fu (2023)](/sources/fu-2023.md) — §2, Eqs. (1)–(4); §3.4, Algorithm 1; §3.7.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §2.1, Eqs. (1)–(5).
- [Ye et al. (2022)](/sources/ye-2022.md) — §1; §3.1, Eqs. (11)–(13).
- [Wang et al. (2023)](/sources/wang-2023-b.md) — §1; §2, Eqs. (2)–(4).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §I; §II, Eqs. (2.2)–(2.6); §IV, Eq. (4.1); §V, Eqs. (5.1)–(5.5).
- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — §2.4–2.5, Eqs. (18)–(26); App. A.1, Lemma A.1; §3.4; §7.2.

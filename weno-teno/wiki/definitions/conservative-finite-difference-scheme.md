---
type: Definition
title: "Conservative finite-difference scheme"
description: "A conservative finite-difference scheme evolves point values by differences of numerical fluxes at half points, du_i/dt = −(f̂_{i+1/2} − f̂_{i−1/2})/Δx, with the flux built so that the difference approximates ∂_x f to high order: by reconstructing split fluxes, interpolating states with corrections, central fluxes with high-order dissipation, implied fluxes of compact schemes, or in fluctuation form."
status: established
aliases: [conservative FD scheme, Shu–Osher finite difference, FD-WENO, finite-difference flux reconstruction, flux-difference form]
tags: [finite-difference, reconstruction, weno, teno]
timestamp: 2026-10-22T20:00:00Z
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

Browne, Haas, Fasel & Brehm (2022, §2.2) apply the same construction to a disturbance formulation of
the compressible Navier–Stokes equations: the state is split exactly into a steady baseflow
$u_{\mathrm b}$ and a disturbance $u'=u-u_{\mathrm b}$ (page-local symbols), and only $u'$ is
evolved, with fifth-order WENO reconstruction of the Rusanov-split disturbance fluxes in
characteristic variables. Subtracting the baseflow splitting from the total-flow splitting
$\tfrac12\big(f(u)\pm a\,u\big)$ leaves a dissipation $\tfrac12\big(a_{\mathrm b}u'+(a-a_{\mathrm b})(u_{\mathrm b}+u')\big)$,
with $a_{\mathrm b}$ the baseflow spectral radius; they call the term $(a-a_{\mathrm b})u_{\mathrm b}$
"not consistent with the formal definition of the Rusanov flux" and destabilizing, and adopt
$f'^{\pm}=\tfrac12\big(f'\pm a\,u'\big)$, the total spectral radius acting on the disturbance only
(Eqs. (18)–(21); $a_{\mathrm b}$ in place of $a$ for the linearized equations, Eq. (22)). No analysis or
test supports the stability claim. Their viscous terms are deliberately discretized in non-conservative
chain-rule form with second-order central differences (Eqs. (34)–(36)), and a manufactured-solution
test gives observed orders of about 5.8–6.0 for the convective right-hand side alone and about 2 with
the viscous terms (App. A, Tables A.1–A.2).

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
  WENO/TENO *reconstruct* split fluxes, the alternative family *interpolates* states. Chu, Kurganov
  & Na (2022, §§3–4) carry the form over to non-conservative systems
  $\partial_tu+\partial_xf(u)+\mathcal C(u)\partial_xu=0$ (they write the product on the right-hand
  side, $+B(u)\partial_xu$ with $B=-\mathcal C$) through the quasi-conservative form
  $\partial_tu+\partial_xK(u)=0$ with the global flux
  $K(u)=f(u)+\int^x\mathcal C(u)\,\partial_\xi u\,d\xi$ (page-local $K$): the two-point flux of $K$
  is a [path-conservative](/methods/path-conservative-scheme.md) [central-upwind](/methods/central-upwind-scheme.md) flux, and the derivative corrections of $K$ split into finite
  differences of $f$ and of $\mathcal C(u)\partial_xu$ (Eq. (4.1)).
- **Weighted compact nonlinear schemes.** Fu (2023, §3.7) recalls the three steps of WCNS:
  nonlinear node-to-interface interpolation, interface flux evaluation, compact interface-to-node
  flux differencing, and names the lack of conservation as the main flaw of the family
  ([WCNS](/methods/weighted-compact-nonlinear-scheme.md)). Hiejima (2022, §2.2, Eq. (5)) uses the
  name for a scheme without the third step: primitive variables are interpolated to $x_{i\pm1/2}$ at
  orders 5 to 11, an AUSMDV flux is evaluated there, and the flux derivative is the plain difference
  $(\hat f_{i+1/2}-\hat f_{i-1/2})/\Delta x$, "the WCNS does not include a compact procedure for
  calculating the flux derivative". The scheme is conservative by construction, and the paper says
  nothing about conservation. *(Compiler check, not in the sources: for exact interface values,
  $\big(f(x_i+\Delta x/2)-f(x_i-\Delta x/2)\big)/\Delta x=\partial_xf(x_i)+\tfrac{\Delta x^2}{24}\partial_x^3f(x_i)+O(\Delta x^4)$,
  so the operator is formally second order for point values whatever the interpolation order, the
  limit Wang et al. (2023) state for an uncorrected two-point flux; Hiejima shows no convergence
  test.)*
- **Central flux plus high-order dissipation.** Sciacovelli, Passiatore, Cinnella & Pascazio (2021,
  §3, Eqs. (20)–(35)), after Lerat & Corre, write the flux as a central part corrected by recursive
  truncation-error terms plus a dissipation of matching odd order: on $2(P+2)+1$ points,
  $\hat f_{i+1/2}=\Big[\big(1-\sum_{p=0}^Pa_p\Delta^{2+2p}\big)\{\!\{f\}\!\}\Big]_{i+1/2}-\mathcal D_{i+1/2}$
  with $a_0=\tfrac16$, $a_1=-\tfrac1{30}$, $a_2=\tfrac1{140}$, $a_3=-\tfrac1{630}$, where
  $\Delta^m$ is the undivided difference of the registry, here centred at half points for even and
  odd $m$ alike, and $\{\!\{f\}\!\}_{i+1/2}=\tfrac12(f_i+f_{i+1})$. The central part is the
  $2(P+2)$-order central difference; the dissipation
  $\mathcal D=(-1)^{P+1}\tfrac{|a_P|}{2}\rho(A)\,\Delta^{2P+3}u$ (page-local $\mathcal D$; magnitudes
  $\tfrac1{12},\tfrac1{60},\tfrac1{280},\tfrac1{1260}$ for orders 3, 5, 7, 9) uses the spectral radius
  $\rho(A)$ instead of a Roe matrix, and is blended with a second-order term switched on by a shock
  sensor ([artificial viscosity](/methods/artificial-viscosity.md)). The schemes are odd-order only,
  neither TVD nor monotonicity-preserving, and their dispersion error is exactly that of the central
  scheme (§3).
- **Implied flux of central and compact differencing.** Wong et al. (2021, §4.1), after Subramaniam,
  Wong & Lele, state that "any central explicit or compact finite difference scheme can be rewritten
  into the flux-difference forms", and give the implied interface flux of an eighth-order explicit
  midpoint-and-node scheme; their positivity limiters then act on that flux, so the limited scheme
  stays conservative ([WCNS](/methods/weighted-compact-nonlinear-scheme.md), whose conservation is
  disputed there).
- **Fluctuation form.** For systems with non-conservative products, Balsara et al. (2024, Eq. (4.1))
  replace the flux difference by an internal term plus boundary fluctuations,
  $\frac{du_i}{dt}=-A(u_i)\frac{u^-_{i+1/2}-u^+_{i-1/2}}{\Delta x}-\frac1{\Delta x}\big(D^-_{i+1/2}+D^+_{i-1/2}\big)$,
  with one WENO reconstruction of the point values per zone (page-local fluctuations $D^\pm$). For a
  linear constant-coefficient system with the local Lax–Friedrichs limit it is algebraically
  identical to the upwind FD scheme $-A^+\frac{u^-_{i+1/2}-u^-_{i-1/2}}{\Delta x}-A^-\frac{u^+_{i+1/2}-u^+_{i-1/2}}{\Delta x}$,
  which they state reduces to Shu–Osher LLF FD-WENO for linear fluxes (§V)
  ([fluctuation-form FD-WENO](/methods/fluctuation-form-fd-weno.md)).

## Moving meshes and two-medium flows

- **Curvilinear moving meshes.** Li, Duan & Tang (2022, §§2–3, after Duan & Tang) write the
  conservation law in time-dependent curvilinear coordinates and evolve $(Ju)_i$ by
  $\frac{d}{dt}(Ju)_i=-\sum_k\frac1{\Delta\xi_k}\big(\hat F_{k,i+1/2}-\hat F_{k,i-1/2}\big)$ in each
  computational direction $\xi_k$ (page-local $\xi_k$, $\hat F_k$; $J$ the Jacobian of the map), with
  the Jacobian evolved by the same flux form. The $2n$th-order entropy-conservative flux is the
  LeFloch–Mercier–Rohde combination
  $\hat F^{2n}_{i+1/2}=\sum_{m=1}^nc_{n,m}\sum_{s=0}^{m-1}\hat F(u_{i-s},u_{i-s+m})$ of a symmetric
  two-point flux, with $\sum_mm\,c_{n,m}=1$ and $\sum_mm^{2s-1}c_{n,m}=0$, $s=2,\dots,n$ (page-local
  $n$ and $c_{n,m}$, the source's $w$, which the registry reserves for entropy variables; Eq. (3.6)). The same combination applied to the metric terms, written in conservative
  cross-product form, satisfies the discrete geometric conservation laws, and free-stream preservation
  is quoted as proved in Duan & Tang (Eqs. (3.7)–(3.10), Remark 3.1). Duan & Tang (2022, §3,
  Prop. 3.1, Theorem 3.2, Prop. 3.2) prove the corresponding statements for
  [special-relativistic hydrodynamics and MHD](/definitions/relativistic-hydrodynamics.md): the
  combination (their order $2p$, coefficients with the same two constraints) is $2p$th-order accurate
  for the flux, for the symmetrizing source term and for the Jacobian evolution; the metrics,
  discretized in cross-product form with the same central operator, satisfy the discrete geometric
  conservation laws exactly because the difference operators commute; and the fully discrete SSP
  Runge–Kutta scheme preserves free streams
  ([entropy-conservative fluxes](/methods/entropy-conservative-flux.md),
  [free-stream preservation](/properties/free-stream-preservation.md),
  [adaptive moving mesh](/methods/adaptive-moving-mesh.md)).
- **Two-medium flows.** Zheng, Shu & Qiu (2021, §2.3, §3.2) keep a sharp interface in a point-value
  scheme yet stay conservative by updating one computational variable per node, the volume-fraction
  mix of the two fluids' values in the interface cell, with a single flux difference, and redistributing
  it to the fluids afterwards; the interface fluxes come from blending a high-order
  [alternative-formulation](/methods/alternative-weno.md) flux with a low-order interface flux. Conservation
  follows by construction, which they contrast with the non-conservative ghost-fluid family (§1;
  [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)).
- **Viscous fluxes.** Wang et al. (2021, §3.1.2, Eqs. (3.29)–(3.30)) keep the viscous terms in flux
  form too: sixth-order central nodal derivatives, then a sixth-order central interpolation of the
  viscous flux to $x_{i+1/2}$, so that the derivative stencil reaches $i\pm3$ and the interpolation
  $i-2,\dots,i+3$.

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
- Sciacovelli et al. (2021, Eqs. (23), (29)) print the dissipation of the general member as
  $-\tfrac{a_P}{2}\rho(A)\Delta^{2P+3}u$ (their dissipation matrix taken as $\rho(A)$), which with the signed $a_P$ above has the opposite sign of
  their explicit members (Eqs. (25)–(28)); the members, used here, are the dissipative ones
  *(compiler check, not in the sources: the order-3 member adds $-\tfrac1{12}\rho(A)\Delta^4u/\Delta x$
  to $du_i/dt$, which damps every Fourier mode)*. The dissipated quantity of Eq. (23) carries a tilde that
  is never defined; the JST-blended form (Eq. (30)) acts on the conserved variables.
- Wang et al. (2021, §3.1.2) state that their viscous discretization does not exceed the WENO
  stencil. *(Compiler check, not in the sources: the derivative stencil $i\pm3$ and the interpolation
  stencil $i-2,\dots,i+3$ printed in Eqs. (3.29)–(3.30) each exceed the five-point WENO stencil, and
  composed they reach $i-5,\dots,i+6$.)*

# Citations

- [Li et al. (2022)](/sources/li-2022-b.md) — §2, Eqs. (1)–(4).
- [Fu (2021)](/sources/fu-2021.md) — §2, Eqs. (4)–(10).
- [Fu (2023)](/sources/fu-2023.md) — §2, Eqs. (1)–(4); §3.4, Algorithm 1; §3.7.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §2.1, Eqs. (1)–(5).
- [Ye et al. (2022)](/sources/ye-2022.md) — §1; §3.1, Eqs. (11)–(13).
- [Wang et al. (2023)](/sources/wang-2023-b.md) — §1; §2, Eqs. (2)–(4).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §I; §II, Eqs. (2.2)–(2.6); §IV, Eq. (4.1); §V, Eqs. (5.1)–(5.5).
- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — §2.4–2.5, Eqs. (18)–(26); App. A.1, Lemma A.1; §3.4; §7.2.
- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — §3, Eqs. (18)–(35).
- [Wong et al. (2021)](/sources/wong-2021.md) — §4.1, Eqs. (73)–(80); §5.2.
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — §2, Eqs. (2.2)–(2.3); §3, Eqs. (3.1)–(3.10), Remark 3.1.
- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) — §1; §2.2–2.3, Eqs. (4)–(5); §3.2.
- [Wang et al. (2021)](/sources/wang-2021.md) — §3.1, Eq. (3.1); §3.1.2, Eqs. (3.29)–(3.30).
- [Browne et al. (2022)](/sources/browne-2022.md) — §2.2, Eqs. (16)–(22), (34)–(36); App. A, Tables A.1–A.2.
- [Chu, Kurganov & Na (2022)](/sources/chu-2022.md) — §3, Eqs. (3.1)–(3.3); §4, Eq. (4.1).
- [Hiejima (2022)](/sources/hiejima-2022.md) — §2.2, Eq. (5).
- [Duan & Tang (2022)](/sources/duan-2022.md) — §3, Eqs. (3.4)–(3.17), Prop. 3.1, Theorem 3.2, Prop. 3.2.

---
type: Method
title: "Path-conservative schemes"
description: 'Path-conservative schemes discretize systems with a non-conservative product $\mathcal C(u)\partial_xu$ by integrating it along a path between interface states and over each cell; the central-upwind (PCCU) and HLL/HLLI fluctuation forms of the bundle use the straight-line path in $u$ or, for well-balancing, a path linear in equilibrium variables, and reduce to conservative fluxes when $\mathcal C=0$.'
status: established
aliases: [path-conservative method, PCCU scheme, path-conservative central-upwind scheme, A-WENO PCCU scheme, Dal Maso–LeFloch–Murat path]
tags: [numerical-flux, central-scheme, riemann-solver, finite-volume, finite-difference, well-balanced]
timestamp: 2026-10-23T23:00:00Z
---

# Path-conservative schemes

A non-conservative hyperbolic system

$$\partial_tu+\partial_xf(u)+\mathcal C(u)\,\partial_xu=0$$

($\mathcal C$ the matrix of the non-conservative product, registry §10) has no flux for the
term $\mathcal C(u)\partial_xu$, so neither the conservative form of the
[semi-discrete scheme](/results/local-conservation-flux-form.md) nor the
[Lax–Wendroff theorem](/results/lax-wendroff-theorem.md) applies to it. As recalled by
[Chu et al. (2022)](/sources/chu-2022.md) (§1, §2), weak solutions are then defined as Borel
measures following Dal Maso, LeFloch and Murat, which requires a family of paths in state
space connecting the two sides of a jump, and path-conservative schemes discretize the
product by integrating it along such a path at each interface and over each cell;
[Kurganov et al. (2023)](/sources/kurganov-2023.md) (§1) recall the same Borel-measure basis.
Chu et al. and Balsara et al. use the straight-line (linear segment) path

$$\Psi_{i+1/2}(\mathsf s)=u^-_{i+1/2}+\mathsf s\,\big(u^+_{i+1/2}-u^-_{i+1/2}\big),\qquad \mathsf s\in[0,1]$$

(page-local $\Psi$ and path parameter $\mathsf s$; [Chu et al. (2022)](/sources/chu-2022.md),
Eq. (4.2); [Balsara et al. (2024)](/sources/balsara-2024.md), Eqs. (3.2)–(3.3)); the
well-balanced variant of Kurganov et al. uses a path linear in equilibrium variables (section
below).

**Sign convention.** Chu et al. and Kurganov et al. write $\partial_tu+\partial_xf=B(u)\partial_xu$ with the product
on the right-hand side (§1, Eq. (1.1) in both), Balsara et al. write it on the left with $+C$
(Eq. (2.4)); this page uses the registry form above, so their $B$ is $-\mathcal C$.

## The two discrete non-conservative terms

With reconstructed interface states $u^\pm_{i+1/2}$ and a reconstruction $\tilde u$ inside
$I_i$, the product contributes (page-local symbols)

$$\mathcal B_i=\int_{I_i}\mathcal C(\tilde u)\,\partial_x\tilde u\,dx,\qquad
\mathcal B_{\Psi,i+1/2}=\int_0^1\mathcal C\big(\Psi_{i+1/2}(\mathsf s)\big)\,\frac{d\Psi_{i+1/2}}{d\mathsf s}\,d\mathsf s
=\tilde{\mathcal C}\big(u^-_{i+1/2},u^+_{i+1/2}\big)\big(u^+_{i+1/2}-u^-_{i+1/2}\big),$$

where, for the straight-line path, $\tilde{\mathcal C}(u_{\mathrm a},u_{\mathrm b})=\int_0^1\mathcal C\big(u_{\mathrm a}+\mathsf s(u_{\mathrm b}-u_{\mathrm a})\big)d\mathsf s$
is the path-averaged matrix of Balsara et al. (Eqs. (3.2)–(3.5); the identity is immediate
since $d\Psi/d\mathsf s$ is constant). The cell term $\mathcal B_i$ is Chu et al.'s $B_j$
(Eq. (2.8)) and the interface term their $B_{\Psi,j+1/2}$ (Eq. (2.9)), both with opposite sign.
The schemes differ in how the interface term is shared between the two neighbouring cells.

## Path-conservative central-upwind (PCCU) scheme

The second-order finite-volume PCCU scheme of Castro Díaz, Kurganov and Morales de Luna
(2019), as recalled by [Chu et al. (2022)](/sources/chu-2022.md) (§2, Eqs. (2.1)–(2.9)) and
by [Kurganov et al. (2023)](/sources/kurganov-2023.md) (§2, Eqs. (2.1)–(2.6)), is, in the sign
convention of this page,

$$\frac{d\bar u_i}{dt}=-\frac1{\Delta x}\Big[\hat f_{i+1/2}-\hat f_{i-1/2}+\mathcal B_i
+\frac{a^+_{i-1/2}}{a^+_{i-1/2}-a^-_{i-1/2}}\,\mathcal B_{\Psi,i-1/2}
-\frac{a^-_{i+1/2}}{a^+_{i+1/2}-a^-_{i+1/2}}\,\mathcal B_{\Psi,i+1/2}\Big],$$

where $\hat f$ is the [central-upwind flux](/methods/central-upwind-scheme.md) with the
one-sided speeds $a^\pm_{i+1/2}$ of Eq. (2.7). *(compiler check, not in the sources: since
$a^-\le0\le a^+$, both weights are in $[0,1]$ and sum to one across an interface, so cell $i$
receives the left-going share of the fluctuation at $x_{i+1/2}$ and the right-going share of
the one at $x_{i-1/2}$; with $\mathcal C=0$ the scheme is the conservative central-upwind
scheme.)* The reconstruction is piecewise linear with the generalized minmod limiter,
parameter $\theta\in[1,2]$ (page-local, not the Zhang–Shu factor), larger $\theta$ less dissipative and more oscillatory (Eqs. (2.3)–(2.4)).
Chu et al. include in $\hat f$ the built-in anti-diffusion term

$$\big(u^+_{i+1/2}-u^-_{i+1/2}\big)\to\big(u^+_{i+1/2}-u^-_{i+1/2}\big)-\mathrm{minmod}\big(u^+_{i+1/2}-u^{\mathrm{HLL}}_{i+1/2},\,u^{\mathrm{HLL}}_{i+1/2}-u^-_{i+1/2}\big),$$

with $u^{\mathrm{HLL}}$ the HLL intermediate state (Eqs. (2.5)–(2.6)), which they say "was
switched off" in the 2019 scheme because that scheme was built on an earlier CU flux (§2) —
the same correction that the
[adaptive-diffusion CU flux](/methods/adaptive-diffusion-central-upwind-flux.md) uses.
For the two-layer shallow-water system the speeds are not eigenvalues but the bounds of a
Lagrange-theorem estimate (§2, citing Kurganov–Petrova).

## Fifth-order A-WENO PCCU scheme

[Chu et al. (2022)](/sources/chu-2022.md) lift the PCCU scheme to fifth order inside the
[alternative WENO](/methods/alternative-weno.md) finite-difference framework (point values
$u_i$). The device is the **global flux**: the system is rewritten in quasi-conservative form
$\partial_tu+\partial_xK(u)=0$ with

$$K(u)=f(u)+\int^x\mathcal C\big(u(\xi,t)\big)\,\partial_\xi u(\xi,t)\,d\xi$$

(page-local $K$; §4). The PCCU flux of $K$ is used as the finite-volume flux of A-WENO, and
the A-WENO high-order corrections $-\frac{\Delta x^2}{24}(K_{xx})+\frac{7\Delta x^4}{5760}(K_{xxxx})$
are split into finite differences of the point fluxes $f_i$ and of the point values of
$\mathcal C(u)\partial_xu$, the latter with fourth-order one-sided and central derivatives on
the six-point stencil $i-2,\dots,i+3$ (Eq. (4.1)). The interface states come from fifth-order
[WENO-Z](/methods/weno-z.md) interpolation of point values with linear weights
$d=(1/16,5/8,5/16)$, $q=2$, $\epsilon=10^{-12}$, in local characteristic variables
([characteristic decomposition](/methods/characteristic-decomposition.md), Remark 6.2). The 2D
scheme is dimension by dimension with global fluxes in $x$ and $y$ (§5, Eq. (5.2)).

**Cell integral in a finite-difference scheme.** A-WENO has no piecewise polynomial inside
$I_i$ that is uniformly fifth order, so $\mathcal B_i$ cannot be evaluated as in the
second-order scheme (§4). Chu et al. build quartic interpolants of $\mathcal C$-entries and of
the components of $u$ through $x_{i-1/2},x_{i-1/4},x_i,x_{i+1/4},x_{i+1/2}$, using
$u^+_{i-1/2}$, $u_{i\mp1/4}$, $u_i$, $u^-_{i+1/2}$, and integrate their product exactly
(Eqs. (4.3)–(4.4)); the quarter-point values are WENO-Z interpolations on the same three
candidate stencils with new linear weights $d_0=15/64$, $d_1=21/32$, $d_2=7/64$ at
$x_{i-1/4}$ (mirror at $x_{i+1/4}$) and the same $\beta_k$ and $\tau_5$. Fifth-order accuracy of
the quadrature is stated ("easy to show"), not proved (Remark 4.1). *(compiler check, not in
the sources: these linear weights reproduce exactly the five-point Lagrange interpolant at
$x_{i-1/4}$ on $\{x_{i-2},\dots,x_{i+2}\}$.)*

## Fluctuation form with an HLL/HLLI solver

[Balsara et al. (2024)](/sources/balsara-2024.md) take the other route: a path-conservative
[HLL-type](/methods/hll-riemann-solvers.md) Riemann solver whose resolved state is implicit in
the path-averaged matrices $\tilde{\mathcal C}(u^-,u^{\mathrm{HLL}})$ and
$\tilde{\mathcal C}(u^{\mathrm{HLL}},u^+)$ (Eq. (3.1)), solved by a few fixed-point iterations
started from the single-path state, with four-point Gauss–Lobatto quadrature of the path
integrals "often sufficient" (§III). Its fluctuations, plus an interior quasilinear term, give
the [fluctuation-form FD-WENO](/methods/fluctuation-form-fd-weno.md) scheme; Balsara et al.
do not cite the Dal Maso–LeFloch–Murat theory by name.

## Well-balanced PCCU: paths linear in equilibrium variables

[Kurganov et al. (2023)](/sources/kurganov-2023.md) (§4) make the second-order PCCU scheme
well-balanced for steady states with algebraic equilibrium variables $\mathsf E(u)\equiv$ const,
where $\partial_xf+\mathcal C\,\partial_xu=\mathsf M(u)\,\partial_x\mathsf E(u)$ with $\mathsf M$
invertible (page-local; §1, Eqs. (1.4)–(1.5)). Derived through
[flux globalization](/methods/flux-globalization.md), the scheme is in local form (Remark 4.2)
the PCCU scheme above with three changes:

1. **reconstruct $\mathsf E$**, not $u$, and recover $u^\pm$ from $\mathsf E(u^\pm)=\mathsf E^\pm$;
2. take the **path linear in $\mathsf E$**, $\mathsf E(\Psi(\mathsf s))=\mathsf E^-+\mathsf s(\mathsf E^+-\mathsf E^-)$
   (Eq. (4.7)), and evaluate $\mathcal B_i$ and $\mathcal B_{\Psi,i+1/2}$ by the trapezoidal rule on
   $\mathsf M\,\partial_x\mathsf E$, so that each differs from the corresponding flux difference
   only by a term proportional to the jump of $\mathsf E$ (Eqs. (4.8)–(4.10)); at a discrete steady state that term vanishes and
   the flux differences cancel the non-conservative contributions exactly (Theorem 4.1);
3. build the **diffusion term** of the [central-upwind flux](/methods/central-upwind-scheme.md)
   from modified states $\check u^\pm$ (page-local) that coincide when $\mathsf E^+=\mathsf E^-$ (Eq. (4.15)).

The original PCCU scheme with a path linear in $u$ preserves only the lake at rest of two-layer
shallow water and fails on a discontinuous steady state over a step (§1, §7.2 Ex. 5), and for
the nozzle system the non-well-balanced PCCU variant with linear paths in $p$ and the
cross-section produces large oscillations on small perturbations (§7.1, Ex. 3). A similar
segment-path idea, applied to the jump of a global source integral across interfaces, makes
the WENO global-flux scheme of [Ciallella et al. (2023)](/sources/ciallella-2023.md) exact at the
lake at rest; the authors call it "similar to classical strategies used in well-balanced path
conservative methods" (§3.3).

## Comparison of the two routes

| | PCCU / A-WENO PCCU (Chu et al. 2022) | well-balanced PCCU (Kurganov et al. 2023) | fluctuation-form FD-WENO (Balsara et al. 2024) |
|---|---|---|---|
| unknowns | cell averages (2nd order) or point values (5th order) | cell averages (2nd order) | point values |
| interface solver | none: one-sided speeds $a^\pm$ | none: one-sided speeds $a^\pm$ | HLL or HLLI, implicit resolved state |
| sharing of $\mathcal B_\Psi$ | weights $a^\pm/(a^+-a^-)$ | weights $a^\pm/(a^+-a^-)$ | HLL fluctuations $\mathcal D^\pm$ |
| cell term | quadrature of $\mathcal C\partial_x\tilde u$ (Eq. (4.4)) | trapezoidal rule on $\mathsf M\,\partial_x\mathsf E$ (Eq. (4.8)) | interior term $A(u_i)(u^-_{i+1/2}-u^+_{i-1/2})$ |
| path | straight line in $u$ | straight line in $\mathsf E$ | straight line in $u$ |
| stationary contacts | not claimed | discontinuous steady states preserved (Theorem 4.1) | preserved with HLLI anti-diffusion |
| lake at rest | via equilibrium variables, asserted | special case of constant $\mathsf E$ *(compiler check, not in the sources: $q_1=q_2=0$ and constant layer energies give $h_1$, $h_2+b$ constant)* | passed "without any special modifications" |

All three use the two-layer shallow-water equations as a test system. For lake-at-rest
preservation see [well-balancing](/properties/well-balancing.md); for exact stationary jumps
see [stationary contact preservation](/properties/stationary-contact-preservation.md).

## Qualifications

- None of the three sources discusses the dependence of the computed weak solution on the
  choice of path; Chu et al. and Balsara et al. fix the straight line in $u$, Kurganov et al.
  the straight line in $\mathsf E$, chosen for well-balancing.
- The well-balancing of the A-WENO PCCU scheme for the two-layer lake at rest is asserted
  ("capable of exactly preserving"), with no proof and no round-off table; the evidence is the
  small-perturbation test (Chu et al., §6.1, Ex. 2).
- Chu et al.'s Table 7.1 rates are self-convergence rates on successive meshes and are erratic
  (e.g. 7.69, 3.55, 5.01, 5.37 for $h_1+w$); the paper reads them as exceeding the formal
  order. The printed rate formula omits the $\log_2$ that the table values carry (§7.1).
- Chu et al. print the lower limit of the smoothness-indicator integral (3.6) as
  $x_{j+1/2}$ (it must be $x_{j-1/2}$), write $u^-_{j+1/2}$ for $\phi^-_{j+1/2}$ in the
  printed derivative of the quartic interpolant, and print two vanishing differences in the 2D
  path term $C^{(6)}_{\Psi}$ where $(h_1)^+-(h_1)^-$ and $w^+-w^-$ are meant by analogy with
  $B^{(5)}_\Psi$.

# Citations

- [Chu et al. (2022)](/sources/chu-2022.md) — §1, §2 (Eqs. (2.1)–(2.9)), §3 (Eqs. (3.1)–(3.7)), §4 (Eqs. (4.1)–(4.4), Remark 4.1), §5 (Eq. (5.2)), §6 (Eqs. (6.1)–(6.4), Remarks 6.1–6.3), §7.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §II (Eqs. (2.4)–(2.5)), §III (Eqs. (3.1)–(3.6)), §IV (accepted manuscript).
- [Kurganov et al. (2023)](/sources/kurganov-2023.md) — §1 (Eqs. (1.1), (1.4)–(1.5)), §2 (Eqs. (2.1)–(2.6), Remark 2.2), §4 (Eqs. (4.5)–(4.15), Theorem 4.1, Remark 4.2), §7 (Exs. 3, 5).
- [Ciallella et al. (2023)](/sources/ciallella-2023.md) — §3.3 (Eq. (38)) (author manuscript).

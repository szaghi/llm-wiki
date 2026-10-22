---
type: Source
title: "Hiejima (2022) — A high-order weighted compact nonlinear scheme for compressible flows"
description: "Explicit WCNS-type interpolation of primitive variables on TENO-like pyramids of substencils, at fifth to eleventh interpolation order with Jiang–Shu or TENO weights, feeding an AUSMDV flux with a two-point flux difference; Sod, Lax, Shu–Osher and double Mach reflection tests."
resource: "doi:10.1016/j.compfluid.2021.105199"
source_kind: paper
authors: [Hiejima T.]
year: 2022
venue: "Comput. Fluids 232:105199"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Computers_amp_Fluids_Hiejima_A_high-order_weighted_compact_nonlinear_scheme_for_compressi.pdf"
tags: [compact-scheme, teno, weno, finite-difference, very-high-order, low-dissipation]
timestamp: 2026-10-22T20:00:00Z
---

# Summary

The paper builds a family of explicit
[weighted compact nonlinear schemes (WCNS)](/methods/weighted-compact-nonlinear-scheme.md) for
the three-dimensional Euler equations. Primitive point values $(\rho,v,p)$ are interpolated
nonlinearly from the nodes to the interfaces $x_{i+1/2}$, and the two interface states feed an
AUSMDV flux; the flux derivative is the plain two-point difference
$(\hat f_{i+1/2}-\hat f_{i-1/2})/\Delta x$ of Eq. (5), and the paper states that its WCNS "does
not include a compact procedure for calculating the flux derivative". The update is therefore
in [conservative finite-difference](/definitions/conservative-finite-difference-scheme.md)
form by construction. The paper says nothing about conservation and does not bear on the open
contradiction of the WCNS page.

The contribution is the interpolation. On a full stencil of $K=2r-1$ points it uses $K-2$
candidate substencils in the "pyramid" pattern of the original
[TENO](/methods/targeted-eno.md) scheme: a central three-point stencil, then pairs of one-sided
stencils each one point wider. Each candidate is a Taylor expansion about $x_i$ with
one-sided or central difference derivatives, and the linear weights $d_k$ give interpolation
of order $K$ for $K=7,9,11$; $K=5$ is Deng & Zhang's WCNS. Two weightings are compared.
WCNS-JS uses [Jiang–Shu weights](/methods/weno-js-reconstruction.md) with the Deng–Zhang
[smoothness indicator](/definitions/smoothness-indicator.md) $\beta_k=\sum_n[\mathsf D^n_k]^2$.
WCNS-T uses a $\tau$-free TENO measure $\gamma_k=(\beta_k+\epsilon)^{-6}$ with cut-off
$C_T=10^{-5}$.

The evidence is numerical and qualitative: [Sod and Lax](/benchmarks/sod-and-lax-shock-tubes.md),
[Shu–Osher](/benchmarks/shu-osher-problem.md) and
[double Mach reflection](/benchmarks/double-mach-reflection.md), with
[Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md) roll-up on the slip line as the
marker of [numerical dissipation](/definitions/numerical-dissipation.md), plus an
[approximate dispersion relation](/definitions/approximate-dispersion-relation.md) in the
appendix. No convergence test is shown. WCNS-JS does not improve with order; WCNS-T resolves
more small scales as the order rises, with weak $C_T$-dependent oscillations, and its
eleventh order matches its ninth on Shu–Osher. The double Mach reflection needs a first-order
fallback where interpolated $\rho$ or $p$ is negative, an ad hoc form of
[bound preservation](/properties/bound-preservation.md). The introduction recalls
[mapped WENO](/methods/mapped-weno.md), [WENO-Z](/methods/weno-z.md),
[WENO-CU6](/methods/weno-cu6.md) and [adaptive TENO](/methods/adaptive-teno.md), and lists
Roe, van Leer and AUSM fluxes as the choices WCNS allows; the AUSMDV flux used here stands
where other schemes of the bundle use an [HLL-family](/methods/hll-riemann-solvers.md) solver. With
interface states and a two-point flux and no derivative corrections, the scheme is the
uncorrected skeleton of [alternative WENO](/methods/alternative-weno.md).

# Version read

Version of record (Elsevier typeset, Comput. Fluids 232, 105199), 11 pages, all read; Tables
1–6 and Eqs. (19)–(23) read visually because the text layer scrambles the fractions, and
Eq. (5) with its context on p. 2 checked visually by the compiler. Page 1 matches Crossref
(title, single author, venue, DOI). Equation, table and figure numbers are those of this
version.

# Key claims

Registry notation (see the notation map): full stencil $K=2r-1$ points, linear weights
$d_k$, indicators $\beta_k$, regularization $\epsilon$, TENO exponent $q$, difference
operators $\mathsf D^n_k\approx\Delta x^n\partial_x^n u|_i$ on substencil $S_k$. Substencils
keep the source's numbering $S_1,\dots,S_{K-2}$ ($S_1$ central).

1. WCNS can use any numerical flux (flux-difference splitting, flux-vector splitting, AUSM) and is "easy to apply … to general coordinates, in contrast to the WENO scheme"; "in terms of resolution, the WCNS slightly outperforms the WENO scheme with the same order of accuracy" (§1). **Stated** (no citation or test)
2. "the WCNS is less robust than the WENO because the results of the former can sometimes blow up, i.e., the interpolated pressure or density becomes negative" (§1). **Stated**
3. Zhao et al. "confirmed that all shock-capturing schemes are first-order accurate downstream of shocks" (§1). **Stated**
4. "almost all methods with multipoint interpolation above the seventh order of accuracy cause spurious oscillations near strong discontinuities", hence the spread of fifth- to seventh-order schemes (§1). **Stated**
5. The flux derivative is $(\hat f_{i+1/2}-\hat f_{i-1/2})/\Delta x$ with AUSMDV interface fluxes; "in this study, the WCNS does not include a compact procedure for calculating the flux derivative" (§2.2, Eq. (5)). **Stated** (design choice) *(compiler check, not in the sources: the unknowns are point values at $x_i=i\Delta x$ (Eq. (6)), and for exact interface values $\big(f(x_{i+1/2})-f(x_{i-1/2})\big)/\Delta x=f'(x_i)+\tfrac{\Delta x^2}{24}f'''(x_i)+O(\Delta x^4)$, so the spatial operator is formally second order whatever the interpolation order $K$; the paper's "fifth to eleventh order" are interpolation orders, and no test measures the scheme's order.)*
6. Time integration is a four-step fourth-order Runge–Kutta scheme (Jameson–Schmidt–Turkel) at CFL 0.8 (§2.2). **Stated**
7. The order-$K$ interpolation uses $K-2$ substencils in a pyramid (Fig. 1); the selection prevents non-physical oscillations "even for very high-order difference methods", "based on the robust nature of the fifth-order WENO scheme containing a three-point stencil", and the pyramid makes the order easy to raise (§2.3). **Stated**
8. Explicit difference coefficients of $\mathsf D^n_k$ are given for $K=7$ (Table 1), $K=9$ (Table 3) and $K=11$ (Table 5). **Derived** (tables; one header slip, see Printed slips)
9. Linear weights, $K=7$: $d=(\tfrac{35}{64},\tfrac{35}{128},\tfrac{7}{128},\tfrac{7}{64},\tfrac1{64})$; $K=9$: $(\tfrac{525}{1024},\tfrac{525}{2048},\tfrac{105}{2048},\tfrac{63}{512},\tfrac{9}{512},\tfrac9{256},\tfrac1{256})$; $K=11$: $(\tfrac{8085}{16384},\tfrac{8085}{32768},\tfrac{1617}{32768},\tfrac{2079}{16384},\tfrac{297}{16384},\tfrac{99}{2048},\tfrac{11}{2048},\tfrac{11}{1024},\tfrac1{1024})$, for $S_1,\dots,S_{K-2}$; the weights of the right state are the mirror permutation (Tables 2, 4, 6). **Derived** *(compiler check, not in the sources: with exact rationals, each set sums to 1 and its combination of the candidate Lagrange interpolants at $x_{i+1/2}$ equals the $K$-point Lagrange interpolant on $\{i-\tfrac{K-1}2,\dots,i+\tfrac{K-1}2\}$, for $K=7,9,11$.)*
10. Seventh-order case in full: the five candidates expanded with their truncation terms (Eqs. (19)–(23)); combining them with $d_k$ eliminates the derivatives of orders 3 to 6 and gives a seventh-order interpolation at $x_{i+1/2}$ (§2.6, Eq. (24)). **Derived**
11. Nonlinear form: $u^-_{i+1/2}=u^{\mathrm{opt}}_{i+1/2}+\sum_k(\omega_k-d_k)u^{(k)}_{i+1/2}$, which reduces to the optimal linear interpolation when $\omega_k\simeq d_k$ (Eq. (25)). **Derived** (identity)
12. Smoothness indicator $\beta_k=\sum_{n=1}^{(K-1)/2}[\mathsf D^n_k]^2$ (Eq. (14), after Deng & Zhang): it grows at discontinuities, so $\omega_k\to0$ (§2.4). **Stated**
13. WCNS-JS: $\omega_k=\alpha_k/\sum_l\alpha_l$, $\alpha_k=d_k/(\epsilon+\beta_k)^2$, $\epsilon=10^{-40}$ (Eq. (15)). **Stated**
14. WCNS-T: $\chi_k=\gamma_k/\sum_l\gamma_l$ with $\gamma_k=1/(\epsilon+\beta_k)^q$, $\epsilon=10^{-40}$, $q=6$, "based on information provided in Refs. [11–14]"; $\delta_k=0$ if $\chi_k<C_T$ (1 otherwise), $C_T=10^{-5}$, $\omega_k=d_k\delta_k/\sum_ld_l\delta_l$ (Eqs. (16)–(18)); the interpolation keeps high order in smooth regions and captures shocks (§2.5.2). **Stated** (no global indicator $\tau$ and no constant $C$ in $\gamma_k$)
15. Sod (101 points, $t=0.2$): WCNS-JS suppresses oscillations at the shock "even for the eleventh-order accuracy"; WCNS-T shows "a slight undershoot … at $x=0$ and a slight overshoot … at the contact discontinuity with increasing accuracy" (§3.1, Fig. 2). **Shown**
16. Lax (101 points, $t=0.14$): the two weightings differ little, WCNS-T slightly better at the contact; every scheme overshoots in $v_1$ near $x=-0.25$, "where the distributions are continuous but not differentiable"; with $C_T=10^{-7}$ the plateau between shock and contact oscillates (§3.2, Fig. 3). **Shown** (the $C_T=10^{-7}$ part **Stated**, not shown)
17. Shu–Osher (201 and 401 points, $t=1.8$): WCNS-JS shows "no difference based on the accuracy" and misses the small waves, attributed to the dissipation of the Jiang–Shu weights; WCNS-T resolves them; "the eleventh-order case is the same as the ninth-order case"; at 401 points results are "very similar to the exact solution" (§3.3, Figs. 4–5). **Shown**
18. Double Mach reflection ($1024\times256\times5$, $t=0.2$): WCNS-JS shows no Kelvin–Helmholtz roll-up on the slip line at any order; WCNS-T shows ripples at fifth order, more wavy structure and small scales at seventh and ninth, and none at eleventh, "probably caused by the first-order interpolation that was used when the primitive variable became negative" (§3.4, Fig. 7). **Shown**
19. Where interpolated $\rho$ or $p$ is negative, a first-order interpolation is used, "due to the difficulty of calculating this problem using a high-order accuracy interpolation due to the strong shock wave" (§3.4). **Stated** (procedure, details not given)
20. Double Mach reflection with WCNS-T at $2048\times512\times5$: the structure is the same at every order except along the slip line and the wall jet; small scales increase with order, and at eleventh order "much more small scales are observed, up to the end of the wall jet, and the direction of the rolled-up vortex is different" (§3.4, Figs. 8–9). **Shown**
21. "the high-order accuracy works effectively when it is based on the premise that a suitable grid resolution is being satisfied" (§§3.4, 4). **Shown** (qualitative)
22. Approximate dispersion relation (Pirozzoli's method, 100 points): WCNS-T is better than WCNS-JS, "However, both cases are not so different in accuracy", and the curves of orders 5 to 11 nearly coincide, which the paper reads as an open issue of the nonlinear weights (Appendix, Fig. A.1). **Shown**
23. "high-order interpolations have a disadvantage in parallel computations" (§4). **Stated**
24. The interpolation improves on the author's earlier one "based on uniformity substencil", which "requires strong suppression of numerical oscillations"; interpolation where the solution is continuous but not differentiable remains an issue (§4). **Stated** (no comparison shown)
25. Future work: tune $q$ and $C_T$ of WCNS-T at eleventh order, following adaptive TENO (§§3.3, 4). **Stated**

# Printed slips

- Table 5, $n=2$ block: the last column header is printed "$c^{(k)}_{2,i+54}$"; it should be $c^{(k)}_{2,i+5}$, as in the other blocks.
- Double Mach reflection labels: the text calls condition (A) "the condition after the shock" and (B) "the undisturbed flow preceding the shock", and imposes "post-shock condition (A)" at the inflow and on $0\le x\le1/6$; but Eq. (29) assigns $(\rho,v_1,v_2,p)=(1.4,0,0,1)$, the gas at rest into which the Mach 10 shock moves (sound speed 1, consistent with the shock speed $10/\sin\theta$ on the upper boundary), to (A), and $(8,8.25\sin\theta,-8.25\cos\theta,116.5)$ to (B). The labels of the text and Fig. 6 and the values of Eq. (29) are swapped against each other.
- Eqs. (11)–(12) write the last point $q_{i+r-1}$ (first point $q_{i-r+1}$) for every one-sided substencil; by Fig. 1 and the tables, $S_{2s}$ ends at $i+s+1$ and $S_{2s+1}$ starts at $i-s-1$.
- Eq. (14) sums over $n=1,\dots,r-1$ (in the source's $r$; $(K-1)/2$ here), but $\mathsf D^n_k$ is blank in the tables for $n$ at least the number of points of $S_k$; the sum is implicitly over the available $n$.
- Eq. (24) sums over $k=1,\dots,5$ in a general-looking formula; it holds for $K=7$ only.
- Eq. (13) indexes the direction of the interface flux by $j$, Eq. (5) by $l$.
- §1: "a 10-point 8th-oder TENO10-A scheme".

# Notation map

| Hiejima (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $r$ | $K=2r-1$ | **the source's $r$ is an order parameter (order $2r-1$ on $2r-1$ points), not the registry's candidate-stencil size $r$** |
| $S_k$, $k=1,\dots,2r-3$ | $S_k$, source numbering kept | $S_1$ central three-point; $S_{2s}$ forward and $S_{2s+1}$ backward, $s+2$ points; the registry's $S_0$ is the most upwind |
| $\boldsymbol Q$, $\boldsymbol F_l$ | $u$, $f^{(l)}$ | conserved state and flux |
| $\boldsymbol q=(\rho,u_1,u_2,u_3,p)$, $u_l$ | $(\rho,v,p)$, $v_l$ | primitive variables interpolated component-wise; velocity |
| $h$, $\Delta x_l$ | $\Delta x$ | grid spacing |
| $q^k_{L,i+1/2}$, $q^k_{R,i+1/2}$ | $u^{(k)}_{i+1/2}$ for $u^-_{i+1/2}$ and $u^+_{i+1/2}$ | candidate values; $L$ expanded about $x_i$, $R$ about $x_{i+1}$ |
| $\tilde{\boldsymbol q}_L$, $\tilde{\boldsymbol q}_R$, $q^{\mathrm{OP}}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$, $u^{\mathrm{opt}}_{i+1/2}$ | nonlinear and optimal linear interface values |
| $\mathcal L^n(q^k_i)$, $c^{(k)}_{n,j}$ | $\mathsf D^n_k$ (page-local), kept | difference approximation of $\Delta x^n\partial_x^nu$ at $x_i$ on $S_k$; **$\mathcal L$ is the semi-discrete operator in the registry** |
| $C^k_L$, $C^k_R$ | $d_k$ | linear weights, $C_R$ the mirror permutation of $C_L$ |
| $IS_k$ | $\beta_k$ | Deng–Zhang form $\sum_n[\mathsf D^n_k]^2$, not the Jiang–Shu formula |
| $\alpha^k_L$, $\omega^k_L$, $\varepsilon$ | $\alpha_k$, $\omega_k$, $\epsilon$ | $\epsilon=10^{-40}$ |
| $\gamma^k_L$, $\chi^k_L$, $q_T$ | $\gamma_k$, $\chi_k$, $q$ | $\tau$-free TENO measure; **$\gamma$ is also the ratio of specific heats (1.4)** |
| $\delta^k_L$, $C_T$ | $\delta_k$, $C_T$ | agrees |
| $\Phi(\varphi)$, $\varphi$ | $\tilde\vartheta(\vartheta)$, $\vartheta$ | modified and reduced wavenumber (Appendix) |
| $(N_x,N_y,N_z)$ | kept | grid points; 1D tests on a $N_x\times21\times21$ grid |

# Reference list

31 printed references in numbered style ([1]–[31]), all parsed and merged complete into the
[bibliography](/bibliography.md) with `citedby` `hiejima-2022`. [21] (Wada & Liou) and [22]
(Jameson, Schmidt & Turkel) are AIAA papers printed without a year; their keys take the year
implied by the AIAA paper number. The author string of [29] is garbled as printed ("Henderson
GB-DLF, Vasilev EI, Elperin T") and kept so. All other references print DOIs. No printed
duplicates.

# Pages created or updated

Chunk 3 (2026-10-22), cited further in chunks 4–5 (2026-10-23). This source is cited on:

* [Adaptive TENO (TENO-A, TENO-AA)](/methods/adaptive-teno.md)
* [Alternative WENO (A-WENO)](/methods/alternative-weno.md)
* [Approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
* [Bound preservation](/properties/bound-preservation.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Mapped WENO](/methods/mapped-weno.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Targeted ENO (TENO)](/methods/targeted-eno.md)
* [Weighted compact nonlinear schemes (WCNS)](/methods/weighted-compact-nonlinear-scheme.md)
* [WENO-CU6](/methods/weno-cu6.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
* [WENO-Z weights](/methods/weno-z.md)

---
type: Source
title: "Jeong et al. (2022) — Development of a WENO scheme based on radial basis function with an improved convergence order"
description: "WENO-G: finite-difference WENO whose candidate and global interpolants are cell-average Gaussian-RBF interpolants with RBF-dependent ideal weights and a locally fitted shape parameter, reaching sixth order on a five-point stencil, with smoothness indicators from generalized undivided differences with exponential vanishing moments."
resource: "doi:10.1016/j.jcp.2022.111502"
source_kind: paper
authors: [Jeong B., Yang H., Yoon J.]
year: 2022
venue: "J. Comput. Phys. 468:111502"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Journal_of_Computational_Physics_Jeong_Development_of_a_WENO_scheme_based_on_radial_basis_function.pdf"
tags: [weno, rbf, smoothness-indicator, critical-points, high-order, finite-difference]
timestamp: 2026-10-23T10:00:00Z
---

# Summary

The paper builds WENO-G, a [conservative finite-difference](/definitions/conservative-finite-difference-scheme.md)
WENO scheme in which the quadratic candidate polynomials of fifth-order
[WENO-JS](/methods/weno-js-reconstruction.md) are replaced by Gaussian
radial-basis-function interpolants $e^{-\lambda_{\mathrm s}^2x^2}$ augmented by
linear polynomials ([RBF-based WENO](/methods/rbf-weno.md)). The cell-average
interpolation stays in the original RBF space, through Lagrange functions that
reproduce it in the cell-average sense; earlier RBF-WENO work instead
cell-averages each translate. All three candidates share the space built on
the central substencil, so RBF-dependent linear weights $\bar d_k$ exist, are
unique and tend to $(1/10,3/5,3/10)$ as $\Delta x\to0$.

Expanding the Lagrange coefficients in $\lambda_{\mathrm s}\Delta x$ gives the
truncation error. The local choice
$\lambda_{\mathrm s}^2\approx-\frac1{14}f^{(5)}/f^{(3)}$ cancels the
$\Delta x^5$ term, so the linear scheme is sixth-order on a five-point stencil
(Theorem 3.5), one order above polynomials of the same dimension.

New [smoothness indicators](/definitions/smoothness-indicator.md) come from
generalized undivided differences exact on exponential polynomials, each one
order smaller with a fitted parameter. They enter
[WENO-Z](/methods/weno-z.md)-type weights, and Prop. 4.5 proves
$\lvert\omega_k-\bar d_k\rvert=O(\Delta x^4)$ whatever the
[critical points](/properties/critical-point-accuracy.md), enough for sixth
order. WENO-JS, [mapped WENO](/methods/mapped-weno.md) (WENO-M) and WENO-Z are
the comparisons. Splitting is [Lax–Friedrichs](/methods/lax-friedrichs-flux.md),
systems use [characteristic decomposition](/methods/characteristic-decomposition.md),
and time stepping is [TVD-RK3](/methods/ssp-runge-kutta.md) (RK4 for order
tests). The introduction recalls the
[Lax–Wendroff theorem](/results/lax-wendroff-theorem.md) and the
[ENO property](/definitions/eno-property.md).

Sixth order is observed for linear advection, [Burgers](/benchmarks/burgers-equation-tests.md)
and a 1D Euler density wave, at 1.3–1.9 times the CPU time of WENO-JS. Sharper
results are shown qualitatively for the [Shu–Osher](/benchmarks/shu-osher-problem.md),
[Lax and Sod](/benchmarks/sod-and-lax-shock-tubes.md) and
[Woodward–Colella](/benchmarks/woodward-colella-blast-wave.md) problems, a
[2D Riemann problem](/benchmarks/two-dimensional-riemann-problems.md) and the
[double Mach reflection](/benchmarks/double-mach-reflection.md).

# Version read

Version of record (Elsevier typeset, article 111502), 26 pages, all read; pages
4–12 and 24–25 checked visually where the extraction dropped primes and
fractions. Page 1 matches Crossref (title, authors in printed order, venue,
DOI). Equation, lemma and table numbers cited here are those of this version.

# Key claims

Registry notation (see the notation map): the source's grid index $j$ is $i$,
its conserved variable $q$ is $u$, its substencils $\mathbb S_k$ are $S_k$
($S_0$ the most upwind), its weight exponent $p$ is $q$, its $\varepsilon$ is
$\epsilon$, its Gaussian shape parameter $\lambda$ is $\lambda_{\mathrm s}$, its
global indicator $\tau=\lvert\nabla^4f\rvert^2$ is $\tau_{\mathrm G}$, its Lagrange functions $L_n$ are $\Psi_n$, its five-point exponent $\mu$ is $\nu$, its
first/second-difference mix $\theta$ is $\theta_{\mathrm G}$.

1. The Gaussian-RBF cell-average interpolant built from Lagrange functions that reproduce the space $\Phi_m=\mathrm{span}\{\phi_{\mathrm G}(\cdot-x_n)\}+\mathbb P^1$ in the cell-average sense (15) satisfies $\frac1{\Delta x}\int_{I_n}Gh\,dx=\bar h_n$ (Prop. 3.2, §3.2). **Proved**
2. The linear system (17) for the Lagrange functions is uniquely solvable "at least for small $\Delta x$", since the cell averages of the translates tend to their point values as $\Delta x\to0$ (§3.2). **Stated** (limit argument, no proof)
3. As $\Delta x\to0$ the Lagrange coefficients at $x_{i+1/2}$ tend to the classical five-point coefficients; their expansion in $\lambda_{\mathrm s}\Delta x$ is given to $O((\lambda_{\mathrm s}\Delta x)^6)$ in Appendix (56) (Remark 3.3, Eq. (19)). **Derived**. *(compiler check, not in the sources: solving (17) in 250-digit arithmetic with exact error-function cell averages, $\Delta x=1$, and fitting in $\lambda_{\mathrm s}\in\{0.01,\dots,0.04\}$ reproduces every coefficient of (56), e.g. $\Psi_2=\frac{47}{60}-\frac15(\lambda_{\mathrm s}\Delta x)^2+\frac1{10}(\lambda_{\mathrm s}\Delta x)^4$, to six digits.)*
4. With one RBF space on the central substencil $S_1$ for all three candidates, the RBF linear weights are unique: $\bar d_0=C_0/C_{0,0}$, $\bar d_2=C_4/C_{2,2}$, $\bar d_1=1-\bar d_0-\bar d_2$; they depend on $\lambda_{\mathrm s}\Delta x$ and tend to the classical weights as $\Delta x\to0$ (§3.3, Eqs. (23)–(24)). **Derived**
5. Truncation error of the five-point Gaussian-RBF reconstruction: $Gh(x_{i+1/2})=h-\frac1{60}\big(h^{(5)}+14h^{(3)}\lambda_{\mathrm s}^2\big)\Delta x^5+\big(\frac{h^{(6)}}{140}+\frac{h^{(4)}\lambda_{\mathrm s}^2}{12}-\frac{h''\lambda_{\mathrm s}^4}6\big)\Delta x^6+O(\Delta x^7)$ (Eq. (26), §3.4). **Derived**
6. The choice $\lambda^2_{\mathrm s,i+1/2}\approx-\frac1{14}f^{(5)}/f^{(3)}$ (27) removes the $\Delta x^5$ term, leaving an $O(\Delta x^6)$ interface error (Eq. (28)). **Derived**
7. When $h^{(3)}\approx0$, the truncated coefficients $\Psi^*_n=a_n+(\lambda_{\mathrm s}\Delta x)^2\ell_{n,2}$ keep a $\Delta x^6$ local error "regardless of issue of nullifying denominator", since $\sum_n\ell_{n,2}\bar h_{i-2+n}=-\frac7{30}\Delta x^3h^{(3)}+O(\Delta x^4)$ (§3.4). **Derived**
8. **Theorem 3.5:** for $h\in C^6$, the flux difference of the Gaussian-RBF flux (20) approximates $\partial_xf\vert_{x_i}$ to $O(\Delta x^6)$; the proof uses $\lambda_{\mathrm s,i+1/2}-\lambda_{\mathrm s,i-1/2}=O(\Delta x)$, needed because the RBF space is not shift- and scale-invariant (§3.4). **Proved** (sketch)
9. This is likened to finite-element "superconvergence": one order above the maximum attainable with polynomials of the same dimension (§3.4). **Stated**
10. When $f^{(5)}\approx0$ one may set $\lambda_{\mathrm s}=0$, so the interpolant reduces to the polynomial one "while still preserving the sixth-order accuracy" (Remark 3.7). **Stated**
11. With flux splitting, the reconstruction of $\hat f_{i+1/2}$ involves six grid points, from whose divided differences $\lambda_{\mathrm s,i+1/2}$ is computed (Remark 3.6). **Stated**
12. **Lemma 4.1:** the generalized first undivided difference with operator $D+\nu_kI$ satisfies $\nabla^1_kf=(f'_{i+1/2}+\nu_kf_{i+1/2})\Delta x+O(\Delta x^3)$, hence $O(\Delta x^2)$ when $\nu_k=-f'_{i+1/2}/f_{i+1/2}+O(\Delta x)$ (Eq. (32)). **Proved**
13. **Lemma 4.3:** with $D^2-\nu_k^2I$, $\nabla^2_kf=(f''_{i+1/2}-\nu_k^2f_{i+1/2})\Delta x^2+O(\Delta x^3)$, hence $O(\Delta x^3)$ when $\nu_k^2=f''_{i+1/2}/f_{i+1/2}+O(\Delta x)$ (Eq. (34)). **Proved**
14. **Lemma 4.4:** with $D^2(D^2-\nu^2I)$ on five points, $\nabla^4f=(f^{(4)}_i-f''_i\nu^2)\Delta x^4+O(\Delta x^5)$, $O(\Delta x^5)$ for a fitted $\nu$; the printed choice (36) is inconsistent with this expansion (see Printed slips). **Proved** (modulo the slip). *(compiler check, not in the sources: solving (30) symbolically with the offsets measured from $x_{i+1/2}$ reproduces Appendix (54)–(55) exactly at the printed orders; with offsets from $x_i$ the five-point vector is the symmetric $(1+\frac1{12}(\nu\Delta x)^2,-4-\frac43(\nu\Delta x)^2,6+\frac52(\nu\Delta x)^2,\dots)$.)*
15. **Prop. 4.5:** with $\epsilon=\Delta x^\ell$, $0<\ell\le4(2q-1)/q$, $q\ge1$, the weights $\alpha_k=\bar d_k\big(1+(\tau_{\mathrm G}/(\beta_k+\epsilon))^q\big)$ (39), with $\beta_k=(\theta_{\mathrm G}\lvert\nabla^1_kf\rvert+\lvert\nabla^2_kf\rvert)^2$ (37), satisfy $\lvert\bar d_k-\omega_k\rvert\le c\Delta x^4$ regardless of critical points; the proof uses $\beta_k=A_k\Delta x^{r_\beta}+\dots$ with $r_\beta\ge2$ and $\tau_{\mathrm G}=O(\Delta x^8)$. **Proved**
16. $\omega_k^\pm-\bar d_k=O(\Delta x^4)$ is sufficient for sixth-order accuracy of $\hat f_{i+1/2}$ (Eq. (41), attributed to Hu, Wang & Adams). **Stated**
17. Linear advection, $u_0=\sin^2(2\pi x)$, $t=2$: WENO-G reaches $L^\infty$ error $3.08\times10^{-10}$ (order 6.00) at $N_x=640$, against $1.62\times10^{-7}$ (JS), $1.96\times10^{-8}$ (M) and $1.96\times10^{-8}$ (Z); $L^1$ order 6.01 (Table 1). **Shown**
18. Linear advection, $u_0=\sin(2\pi x-\sin(2\pi x)/\pi)$: WENO-G has $L^\infty$ order 6.01 and $L^1$ order 5.99 at $N_x=640$, while WENO-JS degrades ($L^\infty$ orders 3.62, 3.62, 3.54, 4.13) (Table 2). **Shown**. *(compiler check, not in the sources: every printed order in Tables 1, 2, 4 and 6 equals $\log_2(e_{N/2}/e_N)$ of the printed errors to within 0.011.)*
19. CPU time to $t=8$ for the second advection datum (MATLAB, Intel i9-12900): 57.18 s for WENO-G against 40.30 s (JS), 42.28 s (M) and 40.51 s (Z) at $N_x=640$ (Table 3). **Shown**
20. Error against CPU time favours WENO-G over JS, M and Z for $u_0=\sin^2(2\pi x)$ (Fig. 1). **Shown**
21. Burgers, $u_0=0.5+\sin(2\pi x)$, $t=0.06$: $L^\infty$ error $4.79\times10^{-12}$ (order 6.01) at $N_x=640$, against $1.04\times10^{-10}$ for JS; $L^1$ order 5.92 (Table 4); CPU time 2.734 s against 2.114 s (Table 5). **Shown**
22. 1D Euler density wave, $t=4$: $L^\infty$ order 5.99, $L^1$ order 6.00 at $N_x=640$; $L^\infty$ error $2.53\times10^{-10}$ against $1.25\times10^{-7}$ (JS) (Table 6); CPU time 342.7 s against 267.6 s (Table 7). **Shown**
23. Discontinuous advection, $t=11$, $\Delta x=1/100$: WENO-G is "less diffusive" and sharper at discontinuities (Fig. 2). **Shown** (qualitative)
24. Shock–entropy interaction, Lax, Sod and interacting blast waves: WENO-G resolves the high-frequency waves behind the shock and the contacts better than JS, M and Z (Figs. 3–6). **Shown** (qualitative)
25. The exponential-vanishing-moment indicators beat the Jiang–Shu indicators inside the same RBF-WENO (Example 5.9, Fig. 7). **Shown** (qualitative)
26. In 2D (Riemann problem, double Mach reflection) WENO-G "better resolves complex structures" than JS, M and Z (Figs. 8–10). **Shown** (qualitative)
27. Multiquadric and inverse-multiquadric RBFs were tried; the Gaussian gave "better or at least similar results" (Remark 5.12). **Stated** (no data)

# Printed slips

- Eq. (19), p. 6: the classical coefficients are printed $(\frac1{30},-\frac{13}{60},\frac{47}{30},\frac9{20},-\frac1{20})$; the third is $\frac{47}{60}$, since the coefficients must sum to 1 (used in §3.4) and Appendix (56) gives $L_2=\frac{47}{60}+O((\lambda\Delta x)^2)$.
- Eq. (36), Lemma 4.4, p. 11: $\mu^2=\frac{f''_{j+1/2}}{f_{j+1/2}}+O(\Delta x)$ copies (34); the lemma's own expansion $(f^{(4)}_j-f''_j\mu^2)\Delta x^4$ and its hypothesis "$f''_j$ non-zero" require $\mu^2=f^{(4)}_j/f''_j+O(\Delta x)$.
- Lemma 4.4 proof, p. 11: "Taylor expansion of f around $x_j$", but the coefficients (55) solve (30) with expansion point $x_{j+1/2}$; an expansion about $x_j$ gives a symmetric vector different from (55). The leading-order statement is unaffected.
- Theorem 3.5, p. 9: "the function given in (5)"; $h$ is defined in (4). Lemma 4.3 proof drops the subscript $k$ in "$\lvert\nabla^2f\rvert=O(\Delta x^3)$".
- p. 13: the text introducing Table 3 follows the discussion of $\sin^2(2\pi x)$, but Table 3 is for $\sin(2\pi x-\sin(2\pi x)/\pi)$ at $t=8$, and it lists only times, not "the CPU cost to obtain one additional order of accuracy".
- Eq. (10): the WENO-Z indicator is printed squared, $\tau_5:=\lvert\beta_2-\beta_0\rvert^2$, against $\tau_5=\lvert\beta_0-\beta_2\rvert$ in Luo & Wu (2021, Eq. (4)) and Wang & Don (2022, Eqs. (6)–(8)) ([WENO-Z](/methods/weno-z.md)).
- Eq. (44): $\alpha=\max_q\lvert f'(q)\rvert$ "over the whole range of q" is called "the local numerical viscosity"; as defined it is the global Lax–Friedrichs constant.
- Ref. [48]: "J. Sci. Comput. 318 (2016) 110–121"; volume 318 with pages 110–121 is how Fan, Zhang & Qiu (2022), Ji, Liang & Fu (2022), Wan & Xia (2022) and other sources print Zhu & Qiu's 2016 paper in J. Comput. Phys. (bibliography entry `zhu-2016`).
- Not stated: the value of $\epsilon$ in the experiments, the thresholds for "$h^{(3)}\approx0$" and "$f^{(5)}\approx0$", the treatment of a negative $\lambda_{\mathrm s}^2$ from (27) or $\nu_k^2$ from (34), and the six-point divided-difference formula for $f^{(5)}$. The shock tubes (49)–(51) are run on domains called "periodic", and the Sod problem is printed with left velocity $0.75$.

# Notation map

| Jeong et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $q$ (also $u$) | $u$ | conserved variable |
| $j$, $x_{j\pm1/2}$, $\bar x$ | $i$, $x_{i\pm1/2}$, $x_{i+1/2}$ | grid index; $\bar x$ is the evaluation point |
| $h$, $\bar h_n=f(x_n)$ | kept | Shu–Osher auxiliary function; point fluxes are its cell averages |
| $\hat f_{j+1/2}$, $\hat f^k_{j+1/2}$ | $\hat f_{i+1/2}$, $\hat f^{(k)}_{i+1/2}$ | numerical and candidate fluxes |
| $\mathbb S^5$, $\mathbb S_k$ | full stencil, $S_k$ | $S_0$ most upwind for $f^+$; agrees |
| $d_k$, $\bar d_k$ | $d_k$, $\bar d_k$ | classical and RBF linear weights; **$\bar d_k$ is not a cell average** |
| $\beta_k$ (Eqs. (8), (37)) | $\beta_k$ | Jiang–Shu and the new indicator, same symbol in the source |
| $\tau_5$, $\tau$ | $\tau_5$ (printed squared), $\tau_{\mathrm G}$ | WENO-Z indicator and the new global indicator $\lvert\nabla^4f\rvert^2$ |
| $\alpha_k$, $\omega_k$, $\varepsilon$, $p$ | $\alpha_k$, $\omega_k$, $\epsilon$, $q$ | **the source's $p$ is the weight exponent**; $\varepsilon$ is also the entropy-wave amplitude in (49) |
| $\ell$ | kept | exponent of $\epsilon=\Delta x^\ell$; also the degree bound $\Pi_{<\ell}$ and a derivative order |
| $\phi$, $\lambda$ | $\phi_{\mathrm G}$, $\lambda_{\mathrm s}$ (local) | Gaussian RBF and shape parameter, as on [RBF-based WENO](/methods/rbf-weno.md); **$\lambda$ collides with the eigenvalues $\lambda_l$** |
| $\Phi_m$, $\Pi_{<2}$ | $\Phi_m$, $\mathbb P^1$ | RBF space plus linear polynomials |
| $L_n$, $L^k_n$; $C_n$, $C_{k,n}$, $a_n$, $\ell_{n,2}$, $\ell_{n,4}$ | $\Psi_n$, $\Psi^k_n$ (local); kept | Lagrange functions (renamed: **$L$ is the left-eigenvector matrix in the registry**), their values at $x_{i+1/2}$, classical coefficients, expansion coefficients; as on [RBF-based WENO](/methods/rbf-weno.md) |
| $\nabla^\alpha_kf$, $\nabla^4f$, $p_\alpha(D)$, $E_m$ | kept | generalized undivided differences and annihilating operators; **$\alpha$ here is a difference order** |
| $\nu_k$, $\mu$ | $\nu_k$, $\nu$ (local) | exponential parameters, as on [smoothness indicators](/definitions/smoothness-indicator.md); **$\nu$ is the CFL number in the registry** |
| $\theta$ | $\theta_{\mathrm G}$ | mix of first and second differences, 0.1 (advection) or 0.25 (Euler); **$\theta$ is the Zhang–Shu factor** |
| $\alpha$ (Eq. (44)), $f^\pm$ | $a$, $f^\pm$ | Lax–Friedrichs splitting speed (global) |
| $s$, $u\pm s$ | $c$, $v\pm c$ | sound speed and eigenvalues |
| $N$ | $N_x$ | number of grid points; **$N$ is the DG degree in the registry** |

# Reference list

48 printed references in numbered Elsevier style ([1]–[48]), roughly
alphabetical, all parsed and merged complete into the
[bibliography](/bibliography.md) with `citedby` `jeong-2022`. No DOIs are
printed. Ref. [7] (Christlieb, Sands & Yang) is an arXiv preprint; ref. [17]
prints the year 2013 with SIAM J. Numer. Anal. 52(2), recorded as printed;
ref. [48] has a suspect venue–volume pair ("J. Sci. Comput. 318"). Two Ha 2013,
two Ha 2016 and two Harten 1987 works are told apart by venue. No printed
duplicates were found.

# Pages created or updated

Chunk 4 (2026-10-23), cited further in chunks 5–6 (2026-10-23). This source is cited on:

* [Accuracy at critical points](/properties/critical-point-accuracy.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)
* [Mapped WENO](/methods/mapped-weno.md)
* [RBF-based WENO](/methods/rbf-weno.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
* [WENO-Z weights](/methods/weno-z.md)

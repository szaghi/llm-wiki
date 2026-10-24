---
type: Source
title: "Crin-Barat & Manea (2026) — Asymptotic-preserving finite difference method for partially dissipative hyperbolic systems"
description: "Proves that the second-order central-difference semi-discretization of linear partially dissipative hyperbolic systems keeps, uniformly in the mesh width, the hypocoercive decay rate under the Kalman rank condition and the diffusive relaxation limit of damped linearized Euler at rate O(epsilon^2), using a discrete Littlewood–Paley decomposition adapted to the difference operator."
resource: "doi:10.1093/imanum/draf066"
source_kind: paper
authors: [Crin-Barat T., Manea D.]
year: 2026
venue: "IMA J. Numer. Anal. 46:2191-2230"
local_file: "/home/stefano/papers/mosaic/weno-teno/2025_Crossref_IMA_Journal_of_Numerical_Analysis_Crin-Barat_Asymptotic-preserving_finite_difference_method_for_partially.pdf"
tags: [asymptotic-preserving, finite-difference, stiff-source, spectral-analysis]
timestamp: 2026-10-23T14:52:00Z
---

# Summary

The paper is peripheral to this bundle: it is numerical analysis of the simplest
linear semi-discretization, with no reconstruction, flux construction, shock
capturing or time integrator. It enters through
[asymptotic preservation](/properties/asymptotic-preservation.md).

The object is a one-dimensional linear partially dissipative system
$\partial_tu+A\partial_xu=-\mathsf Bu$, with $A$, $\mathsf B$ symmetric and
$\mathsf B=\mathrm{diag}(0,\tilde{\mathsf B})$ damping only a block of the
unknowns. It is discretized in space by the central difference
$(D_hu)_i=(u_{i+1}-u_{i-1})/(2\Delta x)$ on an infinite uniform grid, with time
left continuous. Among the two-point differences, only $D_h$ is $\ell^2$-stable
for every symmetric $A$ (Proposition 3.4). Its only structural property used is
the discrete integration by parts $\langle u,D_hv\rangle=-\langle D_hu,v\rangle$:
the central scheme has no [numerical dissipation](/definitions/numerical-dissipation.md),
and all decay comes from $\mathsf B$.

"Asymptotic-preserving" has two senses here, both uniform in $\Delta x$:
preservation of the large-time decay rate, and preservation of a diffusive
relaxation limit. Theorem 2.1 ("numerical hypocoercivity"): under the Kalman rank
condition the semi-discrete solution decays like $(1+t)^{-1/2}$ with an
$\Delta x$-independent constant. The proof uses a Lyapunov functional with a
Beauchard–Zuazua corrector, without Fourier analysis. Theorem 2.6 and Corollary
2.7: for the damped linearized compressible Euler system in diffusive scaling,
the semi-discrete solution converges to the discrete heat equation
$\partial_t\rho-D_h^2\rho=0$ at rate $O(\varepsilon^2)$, uniformly in
$\Delta x$ and in time, in discrete Besov, Sobolev and $\ell^\infty$ norms. The
tool is a discrete Littlewood–Paley decomposition whose dyadic annuli are defined
through the symbol $\sin(k_w\Delta x)/\Delta x$ of $D_h$ rather than through
$\lvert k_w\rvert$, which gives $\Delta x$-uniform Bernstein estimates. Python
experiments show the $(1+t)^{-1/2}$ decay, the $O(\varepsilon^2)$ rate and its
independence of $\Delta x$. Extensions to general Kalman systems and to the
Jin–Xin relaxation are sketched without proof.

# Version read

The archive file is arXiv:2404.06380v2 [math.AP], 16 April 2024, 30 pages, all
read; the figures are plots described only by their captions. It is not the
version of record: the IMA J. Numer. Anal. article (46:2191-2230, issue of 2026,
DOI from Crossref, not printed in the file) has 40 pages, and its content can
differ. The filename's "2025_Crossref_IMA_Journal" labels the published article,
but the PDF is the preprint. Title and authors agree with Crossref. Every claim,
equation and number on this page is that of arXiv v2.

# Key claims

Registry notation, with $\Delta x$ for the source's grid width $h$ and
$\vartheta=k_w\Delta x$. Page-local: $\mathsf B$, $\tilde{\mathsf B}$ the damping
matrix and its positive definite block, $\lambda_{\mathsf B}$ its coercivity
constant; $u=(u_1,u_2)$ the conserved and dissipated parts; $m$ the system size;
$D_h$, $D_h^\pm$ the central and one-sided differences; $\ell^2_h$ the norm
$\lVert u\rVert^2=\Delta x\sum_iu_i^2$ and $h^1_h$ its discrete $H^1$ analogue;
$\delta^j_h$ the $j$-th dyadic block and $\dot B^s_h$ the discrete homogeneous Besov
space; $\varepsilon$ the relaxation parameter.

1. With the forward difference $D_h^+$ the semi-discrete system is $\ell^2$-stable if $A$ is negative, with $D_h^-$ if $A$ is positive, and with $D_h$ for every real symmetric $A$ (§3.3, Proposition 3.4). **Proved**
2. $D_h$ satisfies $\langle u,D_hv\rangle_{\ell^2_h}=-\langle D_hu,v\rangle_{\ell^2_h}$, hence $\langle u,D_hu\rangle=0$ (§3.4, Proposition 3.5, called well known). **Stated**
3. Theorem 2.1: for $u_0\in h^1_h$ and $(A,\mathsf B)$ satisfying the Kalman rank condition, $\lVert u_2(t)\rVert_{\ell^2_h}+\lVert D_hu(t)\rVert_{\ell^2_h}\le C(1+t)^{-1/2}\lVert u_0\rVert_{h^1_h}$ for all $t>0$, with $C$ independent of $\Delta x$, $t$ and $u_0$ (§2.1, Eq. (2.2); proof §4). **Proved**
4. The rate (2.2) is sharp with respect to the continuous case, whose optimality for $H^1$ data is attributed to Crin-Barat, Shou & Zuazua (2024) (Remark 2.2, §1.1). **Stated** (discrete sharpness supported only numerically, claim 15)
5. Intermediate estimate: $\lVert u(t)\rVert_{\ell^2_h}+(1+t)^{1/2}\lVert D_hu(t)\rVert_{\ell^2_h}\le C\lVert u_0\rVert_{h^1_h}$ (§4.1, Eq. (4.12)). **Proved**
6. The continuous problem lacks exponential decay "essentially" because its hyperbolic and dissipative operators have different orders (§1.1). **Stated**
7. The symbol of $D_h$ is $\mathrm i\sin(\vartheta)/\Delta x$; it becomes small near $\vartheta=\pm\pi$, so a dyadic decomposition based on $\lvert k_w\rvert$ (Hong & Yang 2019) gives no Bernstein estimate for $D_h$, while one based on $\sin(\vartheta)/\Delta x$ does (§1.3, Eqs. (1.9)–(1.11), §2.2.2). **Derived**
8. Bernstein estimate: universal $c,C>0$ exist with $c\,2^j\lVert\delta^j_hu\rVert_{\ell^2_h}\le\lVert D_h\delta^j_hu\rVert_{\ell^2_h}\le C\,2^j\lVert\delta^j_hu\rVert_{\ell^2_h}$ for every $\Delta x$, $u$ and $j$ (§3.5.2, Proposition 3.8). **Proved**
9. Embeddings: $\lVert u\rVert_{\dot h^s_h}\le C_s\lVert u\rVert_{\dot B^s_h}$ for every $s$, and $\lVert u\rVert_{\ell^\infty_h}\le C\lVert u\rVert_{\dot B^{1/2}_h}$ (Proposition 2.4, Eqs. (2.6)–(2.7)). **Proved**
10. Theorem 2.3: for $s'>0$ and $s\in(0,s')$, the band-limiting truncation $T_h$ satisfies $\lVert T_hu\rVert_{\dot B^s_h}\le C_{s',s}\lVert u\rVert_{H^{s'}(\mathbb R)}$ for every $\Delta x$ (Eq. (2.5); proof §6). **Proved**
11. Theorem 2.6: for $s'>2$, $s\in(2,s')$ and data truncated to order $\varepsilon^2$, the semi-discrete damped Euler system $\partial_t\rho^\varepsilon+D_hv^\varepsilon=0$, $\varepsilon^2\partial_tv^\varepsilon+D_h\rho^\varepsilon+v^\varepsilon=0$ satisfies, for every $T$, $\lVert(\rho^\varepsilon-\rho)(T)\rVert_{\dot B^{s-2}_h}+\lVert\rho^\varepsilon-\rho\rVert_{L^1_T(\dot B^s_h)}+\lVert D_h\rho^\varepsilon+v^\varepsilon\rVert_{L^1_T(\dot B^{s-1}_h)}\le C\varepsilon^2$, with $C$ depending on the data and not on $\Delta x$, $\varepsilon$ or $T$ (Eq. (2.8); proof §5). **Proved**
12. Corollary 2.7: the same $O(\varepsilon^2)$ convergence, uniform in $\Delta x$, holds in discrete Sobolev norms, and for $s'>5/2$ in $\ell^\infty_h$, together with the residual of the discrete Darcy law $v=-D_h\rho$ (§2.2.2). **Proved**
13. The $O(\varepsilon^2)$ rate is "one order higher" than the $O(\varepsilon)$ of Crin-Barat & Danchin (2023) for the nonlinear damped Euler system, at the cost of more regular data (Remark 2.8, §5.1). **Stated**
14. The low/high-frequency threshold is $2^{J_\varepsilon}=\kappa_0/\varepsilon$ with a small constant $\kappa_0$, so the high-frequency regime disappears as $\varepsilon\to0$ (§2.2.1, Definition 3.9). **Derived**
15. Damped linearized Euler with $\varepsilon=1$, $\Delta x=2^{-4}$: the computed solution shows "a decay rate of exactly $(1+t)^{-1/2}$" (§7.1, Fig. 3). **Shown**
16. With $\Delta x=2^{-4}$, $T=5$, the $\ell^\infty_h$ error and the Darcy residual converge at "exactly $O(\varepsilon^2)$", which the authors call proof of sharpness of Theorem 2.6 (§7.2, Fig. 5). **Shown** (numerical evidence, not a proof)
17. With $\varepsilon=2^{-5}$, $T=5$, the error $\lVert(\rho^\varepsilon-\rho)(T)\rVert_{\ell^\infty_h}$ is 1.375812666e−05, 1.376071039e−05 and 1.376255148e−05, and the Darcy residual in $L^1_T(\ell^\infty_h)$ is 1.468560202e−03, 1.525401187e−03 and 1.537860425e−03, for $\Delta x=2^{-4},2^{-5},2^{-6}$: the relaxation is uniform in $\Delta x$ (§7.2, Fig. 6 table). **Shown**
18. On the whole line, unlike the torus of Blaustein & Filbet (2024), there is no low-frequency spectral gap, which forces the low/high-frequency split (§2.2.2). **Stated**
19. The approach differs from IMEX Runge–Kutta asymptotic-preserving schemes (Boscarino & Russo, Jin, Hu & Shu): the property is established for the space semi-discretization through a frequency-based framework (§2.2.2). **Stated**
20. Under extra conditions on $A$, the result extends to the convergence of a general discrete Kalman system to a discrete diffusive system ("one can readily generalize") (§8.1, Eqs. (8.1)–(8.2)). **Stated** (no proof)
21. The relaxation limit of a discrete Jin–Xin approximation should be justifiable in the same framework; product laws for $f(\rho^\varepsilon)$ are the open difficulty (§8.2). **Stated** (conjecture)
22. The paper claims "a novel approach for numerically approximating the solutions of a class of parabolic equations ... utilizing only first-order discrete operators", meaning first-derivative operators (§8). **Stated**

*(Compiler check, not in the sources.)* $D_h^2u_i=(u_{i+2}-2u_i+u_{i-2})/(4\Delta x^2)$,
so the limit heat equation is discretized on the wide five-point stencil, and
$D_h$ itself is second-order accurate although the paper calls it a "first-order"
operator.

# Printed slips

- **Eq. (8.4)** (Jin–Xin approximation): "$\varepsilon^2(\partial_tu^\varepsilon+\partial_x\rho^\varepsilon)=u^\varepsilon-f(\rho^\varepsilon)$". *(Compiler check, not in the sources:)* this gives $\varepsilon^2\partial_tu^\varepsilon=(u^\varepsilon-f(\rho^\varepsilon))-\varepsilon^2\partial_x\rho^\varepsilon$, an anti-damping term that makes $u^\varepsilon-f(\rho^\varepsilon)$ grow like $e^{t/\varepsilon^2}$. The paper's own system (1.7) puts the damping as $+v^\varepsilon$ on the left, so the right-hand side should be $f(\rho^\varepsilon)-u^\varepsilon$.
- **§2.2.2 heading:** "the incompressible linearized Euler system", for the damped linearized compressible system (1.7) (Remark 1.3, §1.3).
- **Eq. (3.33):** "$x\in[-\pi+c,\pi+c]$"; the next line and (3.34) use $[-\pi+c,\pi-c]$.
- **§4.1 after (4.2):** "$\varepsilon_i$, $i=1,2,\dots,k-1$", while the sum in (4.2) runs to $N-1$.
- **After (4.10):** "$\varepsilon^*:=\min\{\lambda,\varepsilon_1,\varepsilon_1,\dots,\varepsilon_{N-1}\}$", with $\varepsilon_1$ twice.
- **Theorem 2.3:** "every $u\in H^s(\mathbb R)$" in a bound on $\lVert T_hv\rVert$ by $\lVert v\rVert_{H^{s'}}$: the variable and the space of the hypothesis disagree with the bound.
- **Eqs. (1.11), (3.21):** the annuli require $\sin(\xi h)/h\in C_j\subset(0,\infty)$, which excludes every negative $\xi$, while (3.25) asks $\sum_j\varphi_j=1$ on the whole interval and the proof of (3.31) treats negative $\xi$ "by symmetry"; the absolute value $\lvert\sin(\xi h)\rvert/h$ is needed. Eqs. (1.14) and (3.32) also lack it.
- **Proposition 3.4, proof:** it shows $\lVert e^{\mathrm iA}\rVert=1$ for symmetric $A$ and $\lVert e^{A}\rVert\le1$ for negative $A$ and concludes, but the exponents (3.15)–(3.17) also contain $-\mathsf Bt$, and $A$ and $\mathsf B$ need not commute. *(Compiler check, not in the sources:)* the bound still holds, by the energy identity, because the Hermitian part of the exponent, $-\mathsf B$ (plus a negative semidefinite term for the one-sided differences), is negative semidefinite.
- **Remark 2.2:** Theorem 2.1 is said to apply to "(1.7)", the $\varepsilon$-scaled system; it applies to (1.5), that is, (1.7) with $\varepsilon=1$ as in §7.1. The Fig. 4 caption cites "(2.1)" for (1.7); §4 opens with "(2.3)" for (2.2).
- Notation slips: Lemma 3.3 and Proposition 3.2 mix $u$ and $v$; "$B^s_h$" for $\dot B^s_h$ in the proof of Proposition 2.4; "Theorem (2.6)" in §7.
- Reference list: "Boscarino, S. & Russo, A. (2009)", while the 2024 entry of the same pair prints "Russo, G."; "Porretta & Zuazua (2016)" is printed with "Math. Comp. 86 (303), 2017, 97-119".

# Notation map

| Crin-Barat & Manea (arXiv v2) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U=(U_1,U_2)$ | $u=(u_1,u_2)$ | conserved and dissipated parts |
| $A$ | $A$ | constant symmetric flux matrix, agrees |
| $B$, $\tilde B$ | $\mathsf B$, $\tilde{\mathsf B}$ (page-local) | **collision**: $B$ is the SBP boundary matrix in the registry |
| $\lambda$ | $\lambda_{\mathsf B}$ (page-local) | coercivity constant of $\tilde{\mathsf B}$; **not an eigenvalue $\lambda_l$** |
| $N$, $N_2$ | $m$, size of $u_2$ | **$N$ is the DG degree in the registry**; also the norm $N(y)$ of (4.10) |
| $h$, $n$ | $\Delta x$, $i$ | **$h$ is the numerical flux in the registry** |
| $D_h$, $D_h^+$, $D_h^-$ | kept (page-local) | central, forward ("upwind") and backward ("downwind") differences; **not the SBP differentiation matrix $D$** |
| $\xi$, $\sin(\xi h)/h$ | $k_w$, $\sin\vartheta/\Delta x$ | **collision**: $\xi$ is a reference node in the registry |
| $\ell^2_h$, $h^s_h$, $\dot B^s_h$ | kept | discrete spaces |
| $C_j$, $F_h(j)$, $\varphi_j$, $\delta^j_h$ | kept (page-local) | dyadic interval, its preimage, partition of unity, localization |
| $J_\varepsilon$, $\kappa$ | $J_\varepsilon$, $\kappa_0$ (page-local) | **$\kappa$ is the kinetic energy in the registry** |
| $\varepsilon$; $\varepsilon_k$, $\varepsilon_0$, $\varepsilon^*$ | $\varepsilon$; corrector weights | the relaxation parameter and the weights of (4.2) share a letter |
| $\eta_0$ | time weight (page-local) | **not an entropy** |
| $\rho^\varepsilon$, $u^\varepsilon$ | $\rho^\varepsilon$, $v^\varepsilon$ | density and velocity perturbations |
| $w^\varepsilon=D_h\rho^\varepsilon+u^\varepsilon$ | damped mode (page-local) | **$w$ is the entropy variable in the registry** |
| $L(t)$, $I(t)$ | Lyapunov functional, corrector | **$L$ is the left-eigenvector matrix in the registry** |
| $T_h$ | truncation (band-limiting) operator | from Strikwerda |

# Reference list

The paper prints 48 references in author–year style, alphabetical and unnumbered,
merged complete into the [bibliography](/bibliography.md) with `citedby` including
`crinbarat-2026`. No DOIs are printed. Pre-publication items are kept as their own
entries: Crin-Barat, Shou & Zuazua (2024, accepted in Ann. IHP C, arXiv:2308.08280),
Ma, Huang & Yong (2023, arXiv), Hu & Shu (2024, published electronically in Math.
Comp.) and Boscarino & Russo (2024, SeMA, no volume). Same-author same-year keys
follow the printed labels (Crin-Barat & Danchin 2022a/b; Crin-Barat & Danchin 2023
and Crin-Barat & Shou 2023). Jin (2010) and Jin (2012) print the same title and pages
(lecture-notes and Riv. Mat. Univ. Parma versions) and stay two entries. Doubtful
items, recorded as printed: Porretta & Zuazua (label 2016, journal year 2017); Yong
(2004), pages "47–266"; Boscarino & Russo (2009), initial "A."; Dolbeault, Mouhot &
Schmeiser (2015), whose printed title ("Numerical schemes for hyperbolic conservation
laws with stiff relaxation terms") does not fit its citation in §2.2.2 as the
continuous approach to hypocoercivity, to be checked on Crossref. No item is
unparseable.

# Pages created or updated

Chunk 9 (2026-10-23), cited further in chunks 10–11 (2026-10-23/24). This source is cited on:

* [Asymptotic preservation](/properties/asymptotic-preservation.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)

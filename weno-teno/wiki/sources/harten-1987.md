---
type: Source
title: "Harten et al. (1987) — Uniformly high order accurate essentially non-oscillatory schemes, III"
description: "Founding ENO paper: Godunov-type schemes of any order built from reconstruction by adaptive stencils chosen by smallest divided differences (via primitive function or deconvolution), a Cauchy–Kowalewski space–time expansion with a Riemann-flux pointer, and characteristic-wise reconstruction for systems, tested on Burgers, nonconvex, Sod, Lax and blast-wave problems."
resource: "doi:10.1016/0021-9991(87)90031-3"
source_kind: paper
authors: [Harten A., Engquist B., Osher S., Chakravarthy S.R.]
year: 1987
venue: "J. Comput. Phys. 71:231-303"
local_file: "/home/stefano/papers/mosaic/weno-teno/1987_Crossref_Journal_of_Computational_Physics_Harten_Uniformly_high_order_accurate_essentially_non-oscillatory_sc.pdf"
tags: [finite-volume, reconstruction, eno-property, characteristic, riemann-solver, very-high-order]
timestamp: 2026-10-30T08:43:00Z
---

# Summary

Harten et al. (1987a), the third paper of a series (I: Harten & Osher, II: "in
preparation"), build a hierarchy of conservative schemes of any order $r$ for
hyperbolic systems, generalizing [Godunov's scheme](/methods/godunov-scheme.md)
and its second-order [MUSCL](/methods/muscl-hancock.md) extension. The scheme
is written as reconstruction of a piecewise polynomial of degree $r-1$ from cell
averages, evolution "in the small", and cell averaging (Eq. (1.10)). The
reconstruction must be accurate, conservative and **essentially
non-oscillatory**, $TV(\mathcal R(\cdot;\bar u))\le TV(u)+O(\Delta x^r)$ (1.9c),
which "excludes a Gibbs-like phenomenon but allows for the production of
spurious oscillations on the level of the truncation error"
([ENO property](/definitions/eno-property.md)); "ENO stands for essentially
non-oscillatory" (§7).

[ENO reconstruction](/methods/eno-reconstruction.md) uses Harten's adaptive-stencil
interpolation: the stencil grows one point at a time towards the side with the
smaller absolute divided difference (3.4), an asymptotic measure of smoothness
([smoothness indicators](/definitions/smoothness-indicator.md)). It is applied
to the primitive function (RP, non-uniform grids allowed) or by deconvolution
of the cell averages with minmod-limited one-sided derivatives (RD, uniform
grids; [cell-average to point-value conversion](/operators/cell-average-point-value-conversion.md)).
TVD schemes are recalled as "necessarily only first-order accurate at local
extrema" ([TVD](/definitions/total-variation-diminishing.md)); the monotone
evolution and averaging operators carry the scalar TV bound from the
reconstruction to the scheme ([monotone schemes](/definitions/monotone-scheme.md)).

The time integral of the flux is replaced by a Gaussian-type quadrature, with
point values from a local space–time Taylor expansion built by a
**Cauchy–Kowalewski procedure** on each side and combined by an exact or
[Roe](/methods/roe-riemann-solver.md) Riemann flux that acts only as a "pointer"
(4.14). For systems the reconstruction acts on characteristic variables
$l_l(\bar u_i)\bar u_j$ with eigenvectors frozen at the state of the cell being
reconstructed (5.8) ([characteristic decomposition](/methods/characteristic-decomposition.md));
§6 details the Euler equations. A local positivity check reduces the order where
the reconstructed $p$ or $\rho$ could become negative.

Tests: [Burgers](/benchmarks/burgers-equation-tests.md) refinement tables for
$r=1,\dots,5$, [nonconvex Riemann problems](/benchmarks/nonconvex-scalar-riemann-problem.md),
[Sod and Lax](/benchmarks/sod-and-lax-shock-tubes.md), where characteristic
reconstruction removes the "noise" of component-wise reconstruction, and the
[Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md).
Variants: characteristic-method flux, semi-discrete Runge–Kutta form, moving
grids with front tracking, and a 2D outline.

# Version read

Version of record (journal typeset), received 11 April 1986, revised 13
October 1986, dedicated "to Peter Lax on his 60th birthday", as an Acrobat
Capture image scan (2000) of the 1987 issue: 73 PDF pages = pp. 231–303, all read
visually because the OCR layer is unreliable for equations; Tables IA–IIB
re-read at 220 dpi, and Tables IB and IIB checked again on page images for this
page. Page 1 matches the Crossref record (title, the four authors in the order
Harten, Engquist, Osher, Chakravarthy; venue, pages). No DOI is printed. Not the
1997 J. Comput. Phys. 131 reprint, nor the reprint in the 1997 Springer collection
*Upwind and High-Resolution Schemes* (Harten et al. (1987c) in the bibliography).

# Key claims

Registry notation: $\Delta x$, $\Delta t$ (source $h$, $\tau$), cell $I_i$ and
average $\bar u_i$ (source $j$, $v_j$), numerical flux $\hat f_{i+1/2}$ (source
$\bar f_{j+1/2}$), eigenvalues $\lambda_l$ and eigenvectors $r_l$, $l_l$ (source
$a_k$, $r_k$, $l_k$), $v$ and $p$ for velocity and pressure (source $q$, $P$),
$N_x$ cells. Page-local: $\mathcal R(x;\bar u)$ the reconstruction (source $R$),
$\mathcal H_m$ the ENO interpolant (source $H_m$), $N_t$ time steps (source $N$),
$h^{\mathrm{God}}$ and $h^{\mathrm{Roe}}$ the exact Riemann and Roe fluxes
(source $f^R$, $f^{\mathrm{ROE}}$), $\epsilon_{\mathrm R}$ the entropy-correction
threshold (source $\epsilon$). The order $r$ is the source's: $\mathcal R$ has
degree $r-1$ on $r$ cells, as the registry's $r$-point stencil.

1. The scheme (1.14)/(1.16) is in conservation form with numerical flux $\hat f_{i+1/2}=\frac1{\Delta t}\int_0^{\Delta t}f(u_h(x_{i+1/2},t^n+s))\,ds$, and its local truncation error in the sense of cell averages is $O(\Delta x^{r+1})$ when the leading error coefficient $e(x)$ of (1.9a) is Lipschitz (§1, Eqs. (1.8), (1.16)–(1.17)). **Derived**
2. The cumulative error is expected to be $O(\Delta x^r)$ in cell averages, and the final $\mathcal R(x;\bar u^{N_t})$ approximates $u(x,t^{N_t})$ to $O(\Delta x^r)$ pointwise (§1, Eqs. (1.18a,b)). **Derived** (stated as expectation)
3. Where $e(x)$ fails to be Lipschitz (at extrema for MUSCL-type schemes, at roots of higher derivatives for higher order), the local error is only $O(\Delta x^r)$ and the pointwise error $O(\Delta x^{r-1})$; such schemes are called "*r*th order accurate" in quotation marks: $L_1$ order $r$, max-norm order $r-1$ (§1, Remark 1.2). **Stated**
4. In the scalar case $TV(\bar E_h(\Delta t)\bar u)\le TV(\mathcal R(\cdot;\bar u))$ because exact evolution and averaging are monotone, hence $TV(\bar E_h\bar u)\le TV(u)+O(\Delta x^r)$ (Eqs. (1.13a,b)). **Derived**
5. TVD schemes are necessarily only first-order accurate at local extrema (§2, p. 239). **Stated**
6. Paper II [16] is cited for showing that strict non-oscillation, $N_0(\bar u^{n+1})\le N_0(\bar u^n)$ with $N_0$ the number of local extrema (2.1), limits accuracy to second order (§2). **Stated** (cited)
7. Conjecture (scalar): $TV(\bar u^{n+1})\le TV(\bar u^n)+O(\Delta x^{p+1})$ for some $p>0$, "based on heuristic analysis and extensive numerical experimentation" (Eq. (1.22)). **Stated** (conjecture)
8. The number of points in the adaptive stencil, "independent of its orientation, is always $(r+1)$" (§2, p. 239). **Stated**
9. The adaptive interpolation satisfies $\frac{d^k}{dx^k}\mathcal H_m=\frac{d^k}{dx^k}w+O(\Delta x^{m+1-k})$ and $TV(\mathcal H_m(\cdot;w))\le TV(w)+O(\Delta x^{m+1})$, both proved in [16] (§3, Eqs. (3.5a,b)). **Stated** (cited)
10. RP: $\frac{d^l}{dx^l}\mathcal R=\frac{d^l}{dx^l}u+O(\Delta x^{r-l})$ and exact conservation (3.9)–(3.10); RP does not require a uniform mesh (§3(1)). **Derived**
11. For RP with $m=r$ and RD with $m=r-1$, $e(x)$ is discontinuous where the stencil changes orientation, so the schemes are "*r*th order accurate"; RD with $m=r$ gives a globally Lipschitz $e(x)$ and pointwise order $r$, via (3.23) (Remarks 3.1–3.2). **Derived**
12. RD with $r=2$, $m=1$ and RP with $r=2$ are piecewise-linear reconstructions with the slope of the "2nd-order accurate" TVD scheme of [5]; the RP slope (3.24) differs from RD only at local extrema, where RD gives slope 0; RD with $m=r=2$ is "essentially the same" as the non-oscillatory second-order scheme of [15] (Remark 3.2). **Stated**
13. The Cauchy–Kowalewski-based flux (4.14) is $r$th-order accurate in the sense of (1.8): (4.15) follows from (4.16a–d) and the quadrature order (§4). **Derived**
14. For constant-coefficient advection the flux (4.14b) equals the exact abstract flux, and the scheme reduces to $\bar u_i^{n+1}=\bar{\mathcal R}(x_i-a\Delta t;\bar u^n)$ (Eqs. (4.17)–(4.18c)), provided the quadrature is exact for degree $r-1$. **Derived**
15. The Riemann solver in (4.14b) only acts as a "pointer" identifying which Taylor expansion's domain of validity contains $x_{i+1/2}$, so it can be replaced by $h^{\mathrm{Roe}}$ (4.21) with the scheme staying $r$th order (§4, pp. 252–253). **Derived** (heuristic)
16. Component-wise reconstruction (5.1) may produce large spurious oscillations when discontinuities interact, because the scalar reconstruction needs at least $r+1$ points of smoothness between discontinuities (§2 p. 240; §5). **Stated**, then **Shown** in Figs. 11–12.
17. $h^{\mathrm{Roe}}$ admits a stationary expansion shock and needs entropy viscosity terms in genuinely nonlinear fields ([13, 14, 9]) (§4 p. 253; §5 p. 259). **Stated**
18. The ENO schemes were found stable under a CFL restriction of 1 in all experiments (except the mesh-oscillation datum $\bar u_i^0=(-1)^i$, footnote 1) and strongly damp high-frequency noise (§7, p. 264). **Shown** (not displayed)
19. Burgers' equation (7.1), periodic, $t=0.3$, CFL 0.6: observed orders rise with $r$; at $N_x=64\to128$ the $L_1$ rates are 0.99, 1.83, 2.56, 3.53, 4.62 for RP and 0.99, 2.18, 3.35, 4.53, 5.53 for RD, $r=1,\dots,5$ (Tables IA, IB). **Shown**
20. Nonconvex Riemann problems (7.7) with the crude entropy correction $\epsilon_{\mathrm R}=0.1\,\Delta x/\Delta t$: the shock lags the exact location by 8, 3 and 1 cells for $r=1,2,4$; under refinement ($N_x=80$, $N_t=160$) the lag in cells stays the same, from which the authors conclude convergence to the entropy solution (§7 A2, Figs. 6, 8). **Shown**
21. The importance of the Riemann solver decreases with increasing order; for $r>1$ the Cauchy–Kowalewski step is "in general, more important than the Riemann solver" (§7 A2, p. 274). **Stated** (argued from Figs. 3, 14, 16)
22. On Sod's problem characteristic reconstruction removes the "noise" of component-wise reconstruction, which remains "acceptable for practical calculations" (Figs. 10–11); on Lax's problem the component-wise version is "much noisier" (Fig. 12 vs 15) (§7 B1). **Shown**
23. For the fourth-order scheme on Lax's problem, "the sum of the jumps in the reconstruction is only about 35% of the size of the shock, while about 65% of the shock jump is described by the smooth polynomial part of the reconstruction" (Fig. 16, p. 279). **Shown**
24. Because the Riemann solution is self-similar, the rate of convergence of any scheme is limited to first order ([27]); in time steps, $r=4$ with $N_t=35$ gives about the result of $r=2$ with $N_t=70$ (§7 B1, p. 280). **Shown**/**Stated**
25. Blast waves: the "4th-order" scheme with $N_x=800$ is taken as the "converged" solution and $N_x=400$ agrees in velocity and pressure; the 4th-order scheme with $N_x=100$ (not shown) is of the same quality as the 2nd-order one with $N_x=200$ (§7 B2, Figs. 17–19). **Shown**
26. The local positivity check (7.13b), $\sum_{k=1}^{r-1}\lvert\partial_x^kp_i\rvert\frac{(\Delta x/2)^k}{k!}<0.8\,p_i$ and the same for $\rho$, reduces the reconstruction order locally when it fails; in the blast-wave run the order was reduced during two time steps before the interaction and only in the interaction zone, and never in the Riemann problems (§7 B2, p. 285). **Shown** (reported)
27. Semi-discrete Runge–Kutta form (7.18): the experiments of [2] show no spurious oscillations for CFL $\le0.5$, oscillations and eventually instability beyond; it is easier to program but less efficient and uses more storage than the fully discrete form (§7 C2). **Stated** (cited to [2])
28. The characteristic-method flux (7.17) and the Cauchy–Kowalewski flux (4.14) are "computationally equivalent"; the characteristic one "seems to be slightly more accurate" (§7 C1, p. 289). **Stated**
29. Irregular (random) grids lose the extra order of (1.18): the error of scheme (7.20) on (7.1) is $O(\Delta x^{r-1})$ in $L_1$, $L_2$, $L_\infty$ (§7 C3, p. 297). **Shown** (not displayed)
30. Strang-type dimensional splitting [29] is only second-order accurate in time and therefore unsuitable for the higher-order ENO schemes in 2D; for the 2D rotated-square advection the small spurious oscillations at the corners for $r\ge2$ are "small enough to be computationally acceptable" ([12]) (§7 C4). **Stated**

The stencil rule as printed ((3.4); $w[\cdot]$ divided differences, $i_k(i)$ the
left index of the $(k+1)$-point stencil, $i_1(i)=i$):

$$i_{k+1}(i)=\begin{cases}i_k(i)-1&\text{if }\big\lvert w[x_{i_k(i)-1},\dots,x_{i_k(i)+k}]\big\rvert<\big\lvert w[x_{i_k(i)},\dots,x_{i_k(i)+k+1}]\big\rvert,\\ i_k(i)&\text{otherwise,}\end{cases}$$

with ties to the right. A jump in the $p$th derivative inside the stencil gives
$w[\cdot]=O(\Delta x^{-k+p})$ (3.3d). RD uses
$\operatorname{minmod}(x,y)=s\min(\lvert x\rvert,\lvert y\rvert)$ if
$\mathrm{sgn}\,x=\mathrm{sgn}\,y=s$, $0$ otherwise (3.16), on the one-sided
derivatives of $\mathcal H_m(\cdot;\bar u)$. The crude entropy correction is
$h^{\mathrm{Roe}}=\frac12[f(u_1)+f(u_2)-\max(\lvert\bar a(u_1,u_2)\rvert,\epsilon_{\mathrm R})(u_2-u_1)]$
(7.8a), $\bar a$ the Rankine–Hugoniot speed; no entropy correction is used in
the Euler runs (p. 275) or the Burgers runs (p. 267).

Test setups as printed. Burgers (7.1) $u_t+(u^2/2)_x=0$ on $[-1,1]$,
$u_0=1+\frac12\sin\pi x$, shock at $t=2/\pi$, accuracy at $t=0.3$, $N_x=8$–$128$,
plus an IBVP variant. Nonconvex flux $f(u)=\frac14(u^2-1)(u^2-4)$ (7.7b), RD,
CFL 0.8: $u^-=2$, $u^+=-2$, and $u^-=-3$, $u^+=3$; $N_x=40$. Sod (7.10a)
$(\rho,v,p)=(1,0,1)$ / $(0.125,0,0.10)$, 50 steps; Lax (7.10b)
$(0.445,0.698,3.528)$ / $(0.5,0,0.571)$, "used by Lax in [18]", 85 steps; both
100 cells, $\Delta x=0.1$, CFL 0.8, final times not printed. Blast waves (7.11):
$\rho=1$, $v=0$, $p=10^3$, $10^{-2}$, $10^2$ on $[0,0.1)$, $[0.1,0.9)$, $0.9\le x<1$,
reflecting walls by ghost states (7.12), output $t=0.010$–$0.038$.

# Printed slips

1. p. 239: "the scheme (1.23b) is highly nonlinear"; there is no (1.23b), and the scheme introduced two lines above is (2.5b).
2. p. 247 (Remark 3.1): "(See Remark 1.4)"; §1 has Remarks 1.1–1.3, and the definition referred to is Remark 1.2.
3. (3.19b) prints $D_{k,j}=\bar D_{k,j}-\sum_{l=k+1}^{r-1}\alpha_lD_{l,j}$. *(Compiler check, not in the sources: row $k$ of (3.13a) reads $\bar D_k=\sum_{l\ge k}\alpha_{l-k}D_l$, so the back-substitution carries $\alpha_{l-k}$; it coincides with the printed $\alpha_l$ for $k=0$, the case used in (3.21).)*
4. (6.5c) prints "$P_t+qP_x+\gamma Pu_x=0$"; in §6 $u$ is the state vector and $q$ the velocity, and the recursion (6.6a) uses $\gamma Pq_x$.
5. (A.9)–(A.10): with $\tilde d_k=h^kd_{i,k}$ as printed, the coefficients $c_1=\tilde d_1-\tilde d_2/2+\tilde d_3/3-\dots$, $c_2=\tilde d_2-\tilde d_3+11\tilde d_4/12-\dots$ are those of an expansion in forward differences $k!\,h^kd_{i,k}$. *(Compiler check, not in the sources: for $w=x^2$, $h=1$, nodes $0,1,2,\dots$, $d_1=d_2=1$; the printed $c_1$ gives $\frac12$ while $hq'(0)=0$; with $\tilde d_k=k!h^kd_{i,k}$, $c_1=1-\frac22=0$ and $c_2=2=h^2q''$.)*
6. $b_{j,l}$ denotes the $l$th derivative in (4.2b), (4.11a), (6.3b) and the Taylor coefficient (derivative$/k!$) in (A.1), (A.15), (A.18).
7. Table IIB, $L_\infty$, $r=5$, $J=8\to16$: rate printed "−65". *(Compiler check, not in the sources: $\log_2(9.192\times10^{-3}/1.441\times10^{-2})=-0.65$.)*
8. Table IB, $L_\infty$, $r=5$, $J=32$: printed $1.191\times10^{-4}$, between $2.343\times10^{-3}$ ($J=16$) and $5.242\times10^{-6}$ ($J=64$) with printed rates 3.61 and 5.20. *(Compiler check, not in the sources: the printed value gives $\log_2$ ratios 4.30 and 4.51; $1.911\times10^{-4}$ gives 3.62 and 5.19.)*
9. Table IB, $L_1$, row $J=64$: printed $1.096\times10^{-4}$ ($r=3$), $1.096\times10^{-5}$ ($r=4$), $1.936\times10^{-6}$ ($r=5$), with printed rates 3.67/3.35, 4.39/4.53, 5.40/5.53 on either side. *(Compiler check, not in the sources: from the $J=32$ and $J=128$ entries ($1.399\times10^{-4}$, $1.071\times10^{-6}$; $4.056\times10^{-5}$, $8.385\times10^{-8}$; $1.919\times10^{-5}$, $9.810\times10^{-9}$) the printed rates give $1.096\times10^{-5}$, about $1.93\times10^{-6}$ and about $4.6\times10^{-7}$; the printed $r=4$ entry repeats the $r=3$ mantissa and the printed $r=5$ entry matches the $r=4$ value.)*
10. p. 285: "reduced during two time steps before the interaction in Fig. 16d"; Fig. 16 is the Lax reconstruction and has no panel d; the blast-wave interaction is in Fig. 17 (the same sentence cites Fig. 17c).
11. Fig. 15 (p. 283): the panel labelled "PRESSURE" carries the axis range 0–1.54 of the velocity panels of Figs. 13, 14, 16, and the panel labelled "VELOCITY" the range 0–3.53 of their pressure panels (printed tick labels).
12. p. 277: Sod's problem "proposed by Sod in [23]"; ref. [23] is Osher (SIAM J. Numer. Anal. 21, 1984) and Sod is ref. [28].
13. Typos: "Interaction of Blas Waves" (p. 280), "the '2-order' scheme" (p. 284), "reconstrution" (p. 255), "Researh supported" (p. 231).
14. (5.8b) uses $p$ for the order of reconstruction ("here $p$ is the desired order of reconstruction"), elsewhere $r$; (1.22) and §4 use $p$ for other quantities.

# Notation map

| Harten et al. (1987a) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $h$, $\tau$, $\lambda=\tau/h$ | $\Delta x$, $\Delta t$, $\Delta t/\Delta x$ | **collision**: $\tau$ is the WENO-Z global indicator, $\lambda$ the eigenvalues |
| $I_j$, $x_j$, $x_{j+1/2}$ | $I_i$, $x_i$, $x_{i+1/2}$ | agree up to the index letter |
| $v_j^n$, $\bar u_j^n$ | $\bar u_i^n$ | numerical and exact cell averages |
| $\bar w$, $A_h$, $E(\tau)$, $\bar E_h(\tau)$ | sliding average, averaging, evolution and scheme operators (local) | |
| $\bar f_{j+1/2}$, $\hat f$ | $\hat f_{i+1/2}$, exact time-averaged flux | **collision**: the source's $\hat f$ is the exact flux, the registry's the numerical flux |
| $r$ | $r$ | order; $\mathcal R$ of degree $r-1$ on $r$ cells, $r+1$ points of the primitive |
| $R(x;\bar w)$, $\mathbf R$ | $\mathcal R(x;\bar u)$ (local) | **collision** with the right-eigenvector matrix $R$ |
| $H_m(x;w)$, $q_{m,j+1/2}$, $i_m(j)$ | $\mathcal H_m$ (local), interpolant, stencil left index | **collision** with the enthalpy $H$ |
| $w[x_i,\dots,x_{i+k}]$ | divided difference (local) | not undivided ($\Delta^mf_i$ of §10) |
| $W(x)$ | $\mathfrak W(x)$, primitive function (local) | renamed because of the **collision** with the Lorentz factor $W$ |
| $\alpha_k$ (§3); $\alpha_k$, $\beta_k$ (§4) | deconvolution coefficients; quadrature weights and nodes (local) | **collision** with the weights $\alpha_k$ and the indicators $\beta_k$ |
| $C$, $D_{k,j}$, $\bar D_{k,j}$ | deconvolution matrix, scaled derivatives (local) | |
| $M(x,y)$ | $\operatorname{minmod}(x,y)$ | **collision** with the mass matrix $M$ |
| $e(x)$, $d(x)$ | leading error coefficients (local) | **collision** of $e$ with the specific internal energy |
| $b_{j,l}$, $\tilde v_j(x,t)$ | Taylor data, Cauchy–Kowalewski expansion (local) | |
| $a_k$, $r_k$, $l_k$, $A(u)$ | $\lambda_l$, $r_l$, $l_l$, $A(u)$ | eigenvectors at the cell state $\bar u_i$ in (5.8), at the Roe state $\hat u$ in (5.11) |
| $f^R$, $f^{\mathrm{ROE}}$ | $h^{\mathrm{God}}$, $h^{\mathrm{Roe}}$ | two-point fluxes $h(u^-,u^+)$ |
| $\bar a(u_1,u_2)$ | Rankine–Hugoniot speed (local) | |
| $\delta_k$ | wave strength $l_l(\hat u)(u^+-u^-)$ (local) | **collision** with the TENO flag $\delta_k$ |
| $\epsilon$ | $\epsilon_{\mathrm R}$ (local) | entropy-correction threshold $0.1/\lambda$; not the weight regularization |
| $\rho$, $q$, $P$, $E$, $m$, $H$, $c$, $\gamma$ | $\rho$, $v$, $p$, $E$, $\rho v$, $H$, $c$, $\gamma$ | $u$ is the state vector |
| $b_1$, $b_2$ | $(\gamma-1)/c^2$, $\frac12v^2b_1$ (local) | left eigenvectors (6.2d–f) |
| $J$, $N$ | $N_x$, $N_t$ | **collision**: $J$ is the element Jacobian, $N$ the DG degree |
| $r_c$ | observed order (local) | "computational order of accuracy" |
| $\sigma_{j+1/2}$, $\xi_{j+1/2}$ | interface speed and position (local) | moving grid; **collision** of $\xi$ with the DG nodes |

# Reference list

The paper prints 32 references, numbered [1]–[32] in alphabetical order, most
without titles (journal, volume, first page only). The list is merged complete
into the [bibliography](/bibliography.md), with `citedby` including
`harten-1987`; entries are identified by volume and page where printed-order
suffixes would mislead. Ref. [22] (J. Comput. Phys. 32, 101, 1979) is
[Van Leer (1979)](/sources/vanleer-1979.md); ref. [9] (J. Comput. Phys. 49, 357,
1983) is [Harten (1983a)](/sources/harten-1983.md); ref. [8] (J. Comput. Phys. 49,
151) is Harten (1983d); refs. [13] and [14] are Harten & Hyman (1983) and
Harten, Lax & van Leer (1983). Pre-publication forms enter as their own entries:
ref. [16] (paper II, "in preparation", undated, a work distinct from this
paper), ref. [15] (paper I as MRC report 2823, May 1985, "SIAM J. Numer. Anal.,
in press"), ref. [12] (Saint-Etienne, January 1986, in preparation), ref. [1]
(Ben-Artzi & Falcovitz, "in press") and ref. [24] (Osher & Tadmor, "in press").
No item is unparseable.

# Pages created or updated

Chunk 12 (2026-10-30). This source is cited on:

* [Accuracy at critical points](/properties/critical-point-accuracy.md)
* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Cauchy–Kowalewski procedure](/methods/cauchy-kowalewski-procedure.md)
* [Cell-average to point-value conversion](/operators/cell-average-point-value-conversion.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [ENO property](/definitions/eno-property.md)
* [ENO reconstruction (essentially non-oscillatory schemes)](/methods/eno-reconstruction.md)
* [Exact Riemann solver](/methods/exact-riemann-solver.md)
* [Generalized Riemann problem (GRP) solvers](/methods/generalized-riemann-problem.md)
* [Godunov scheme](/methods/godunov-scheme.md)
* [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)
* [Monotone schemes and monotone numerical fluxes](/definitions/monotone-scheme.md)
* [MUSCL and MUSCL–Hancock schemes](/methods/muscl-hancock.md)
* [Operator splitting for stiff source terms](/methods/operator-splitting.md)
* [Riemann problems with nonconvex scalar fluxes](/benchmarks/nonconvex-scalar-riemann-problem.md)
* [Roe approximate Riemann solver](/methods/roe-riemann-solver.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)

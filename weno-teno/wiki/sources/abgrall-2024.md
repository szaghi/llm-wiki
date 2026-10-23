---
type: Source
title: "Abgrall & Nassajian Mojarrad (2024) — An Arbitrarily High Order and Asymptotic Preserving Kinetic Scheme in Compressible Fluid Dynamic"
description: "Extends to two space dimensions an arbitrarily high-order, computationally explicit, asymptotic-preserving discrete kinetic (BGK/relaxation) scheme: deferred-correction time stepping with an implicit but explicitly computable relaxation term, upwind finite differences in vertex-residual form, a flux limiter and a MOOD fallback, with a linear stability analysis allowing CFL numbers above one."
resource: "doi:10.1007/s42967-023-00274-w"
source_kind: paper
authors: [Abgrall R., Nassajian Mojarrad F.]
year: 2024
venue: "Commun. Appl. Math. Comput. 6:963-991"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Communications_on_Applied_Mathematics_and_Computation_Abgrall_An_Arbitrarily_High_Order_and_Asymptotic_Preserving_Kinetic.pdf"
tags: [asymptotic-preserving, finite-difference, limiting, stiff-source, positivity]
timestamp: 2026-10-23T10:00:00Z
---

# Summary

The paper extends the one-dimensional scheme of Abgrall & Torlo (2022) to two
space dimensions on Cartesian grids. A system $\partial_tu+\sum_d\partial_{x_d}f^{(d)}(u)=0$
is approximated by a [discrete kinetic relaxation](/methods/discrete-kinetic-relaxation-scheme.md)
(BGK, Jin–Xin, Aregba-Driollet–Natalini type) system
$\partial_t\mathsf f+\sum_d\Lambda^{(d)}\partial_{x_d}\mathsf f=\big(\mathbb M(\mathbb P\mathsf f)-\mathsf f\big)/\varepsilon$
with constant diagonal velocity matrices $\Lambda^{(d)}$, a linear projection
$\mathbb P$ and a Maxwellian satisfying $\mathbb P\mathbb M(u)=u$,
$\mathbb P\Lambda^{(d)}\mathbb M(u)=f^{(d)}(u)$; $\varepsilon$ plays the role of a
Knudsen number.

Time stepping is [deferred correction](/methods/deferred-correction.md): a
high-order implicit collocation operator is approached by iterating a low-order
operator in which convection is explicit and the relaxation term keeps its implicit
form. Because $\mathbb P$ annihilates the source, the projected update is explicit,
so the Maxwellian is known and only a small, space-independent matrix
$\mathrm{Id}+\frac{\Delta t}{\varepsilon}\Omega$ is inverted. Space derivatives are
Iserles' upwind interpolatory differences of orders 1–4, written in
[conservative finite-difference](/definitions/conservative-finite-difference-scheme.md)
form and, in 2D, as a sum of four vertex residuals per quad, whose quad sum is the
boundary flux ([local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md)).

Results: a contraction estimate for the deferred-correction iteration with a constant
independent of $\varepsilon$; formal [asymptotic preservation](/properties/asymptotic-preservation.md)
up to $O(\varepsilon)$; a von Neumann analysis of the iterations giving CFL bounds
above one. Two stabilizations are tested: a limiter blending first- and higher-order
differences in the spirit of [TVD limiters](/definitions/total-variation-diminishing.md),
and a [MOOD](/methods/mood-a-posteriori-limiting.md) fallback that recomputes
flagged quads at first order when $\rho\le0$, $p\le0$ or a NaN appears
([bound preservation](/properties/bound-preservation.md)); the first-order scheme
"amounts to global [Lax–Friedrichs](/methods/lax-friedrichs-flux.md)". Tests:
2D linear advection (orders 2 and 4 at CFL 1), the
[isentropic vortex](/benchmarks/isentropic-vortex.md) (fourth order; a run to
$T=200$), a radial [Sod problem](/benchmarks/sod-and-lax-shock-tubes.md) and a
strong radial shock that needs MOOD.

# Version read

Version of record (Springer typeset, open access), pp. 963–991, 29 pages, all
read; pp. 966–970 and 975–987 were read on the page images to resolve garbled
equations, the Fig. 2 caption and Table 1. Page 1 matches Crossref (title, two
authors, venue, DOI). The filename carries the online year 2023; the published
issue is 2024. Numbers cited here are those of the version of record.

# Key claims

Registry notation (see the notation map): the kinetic unknown is written
$\mathsf f\in\mathbb R^L$ to keep $f$ for the physical flux; the source's $A_i(u)$
is $f^{(d)}(u)$; its deferred-correction operators $L_1$, $L_2$ and weight block $W$ are
$\mathcal D^1$, $\mathcal D^2$ and $\Omega$, as on the [DeC](/methods/deferred-correction.md) page; its relaxation parameter $\varepsilon$ is kept (it is not the
weight regularization $\epsilon$).

1. The class of fully explicit kinetic methods is arbitrarily high order in space and time and includes the Jin–Xin relaxation schemes (abstract). **Stated**
2. The methods run at CFL $\ge1$ on regular Cartesian meshes in multi-D: CFL 1 throughout the tests, CFL 1.2 for the vortex to $T=200$ with five iterations (Remark 1), and "we have not been able to run higher than CFL 1.3" at fourth order in space and time (§4, §6). **Shown**
3. The scheme is computationally explicit: applying $\mathbb P$ to the deferred-correction update (11) gives $\mathbb PF^{(r+1)}$ explicitly (Eq. 12), so only $\mathrm{Id}+\frac{\Delta t}{\varepsilon}\Omega$ must be inverted (Eqs. 13–14a), at a cost "of the same order of a fully explicit scheme" (abstract). **Derived**
4. Splitting-based relaxation schemes are limited to second order in time; higher order needs nontrivial manipulations (§1). **Stated**
5. Lemma 1: for linear flux formulas, $\lVert \mathcal D^2(F)-\mathcal D^1(F)\rVert_{-1,I}\le\gamma_{\mathrm{DeC}}\Delta t\lVert F\rVert_{2,I}$, with $\gamma_{\mathrm{DeC}}$ the largest finite-difference coefficient times the largest kinetic speed (§2.2). **Proved** (see Printed slips)
6. Lemma 2: under uniform bounds on $(\mathrm{Id}+\frac{\Delta t}{\varepsilon}\Omega)^{-1}$ and $\frac{\Delta t}{\varepsilon}(\mathrm{Id}+\frac{\Delta t}{\varepsilon}\Omega)^{-1}W$, $\mathcal D^1$ is inverse-Lipschitz in both discrete norms with a constant independent of $F$, $I$ and $\varepsilon$ (§2.2). **Proved**
7. Proposition 1: if $F^*$ is the unique solution of $\mathcal D^2(F)=0$, there is $\theta_{\mathrm{DeC}}$ independent of $\varepsilon$ with $\lVert F^{(r+1)}-F^*\rVert_{L^2}\le(\theta_{\mathrm{DeC}}\Delta t)^{r+1}\lVert F^{(0)}-F^*\rVert_{L^2}$ (§2.2). **Proved** (two-line sketch via a discrete Poincaré inequality and Lemmas 1–2)
8. Proposition 2 (asymptotic preservation): Eq. (14a) is consistent with the limit $\mathsf f=\mathbb M(u^\varepsilon)+O(\varepsilon)$, $\partial_tu^\varepsilon+\sum_d\partial_{x_d}f^{(d)}(u^\varepsilon)=O(\varepsilon)$; as $\varepsilon\to0$ the iteration becomes a deferred-correction discretization of the conservation law itself (§2.2). **Derived**
9. For time orders 1, 2 and 4 (implicit Euler, Crank–Nicolson, a three-node fourth-order collocation) the two matrices of Lemma 2 are uniformly bounded; at first order they are $\varepsilon/(\varepsilon+\Delta t)$ and $\Delta t/(\varepsilon+\Delta t)$ (§2.3). **Derived** (fourth order "easy to observe", not shown) *(compiler check, not in the sources: the fourth-order $\Omega=\begin{pmatrix}1/3&-1/24\\2/3&1/6\end{pmatrix}$ has eigenvalues $\tfrac14\pm\tfrac{\sqrt3}{12}\mathrm i$, so $\mathrm{Id}+\frac{\Delta t}{\varepsilon}\Omega$ is invertible for every $\varepsilon>0$.)*
10. Iserles: the interpolatory upwind method with $r$ backward and $s$ forward points has order $r+s$, and only the members $[r,r]$, $[r,r+1]$, $[r,r+2]$ are stable (§3.1). **Stated**
11. The four vertex residuals of a quad sum to an approximation of the flux through its boundary (Eq. 16), which "guarantees the local conservation" (§2.1). **Derived**
12. The Fourier symbols of the first- to fourth-order upwind differences have non-negative real part: $\Re g^{(2)}=(\cos\vartheta-1)^2$, $\Re g^{(3)}=\frac13(\cos\vartheta-1)^2$, $\Re g^{(4)}=\frac13(1-\cos\vartheta)^3$ (§4). **Derived**
13. For the transport equation the deferred-correction errors obey $G_{1,r+1}-G_1=(-1)^{r+1}g^{r+1}(1-G_1)$ (Eq. 20), $G_{2,r+1}-G_2=(-1)^{r+1}(g/2)^{r+1}(1-G_2)$ (Eq. 21) and $G_{4,r+1}-G_4=(-1)^{r+1}g^{r+1}M^{r+1}\big((1,1)^\top-G_4\big)$ (Eq. 24); the iteration converges to the implicit scheme if $\lvert g\rvert<1$, $\lvert g\rvert<2$, $\lvert g\rvert\,\lVert M\rVert_2<1$ (§4). **Derived**
14. "The larger $\rho$ is achieved for $r+1$ iterations for scheme of order $r$" (§4, Fig. 2). **Shown** (stability-region plots)
15. Table 1 CFL bounds: DeC(2,2) 0.4, DeC(2,3) $2/\sqrt3$, DeC(2,4) $\sqrt{2.2}$, DeC(4,4) $0.75\sqrt{6.8}$, DeC(4,5) 2.25, DeC(4,6) $1.5\sqrt2$ (§4). **Derived** (internally inconsistent, see Printed slips)
16. "Even with the BGK source term, the schemes are always stable for CFL $=1+\delta$"; fourth/fourth order is stable for CFL $\approx1.3$ on the periodic vortex (§4); Remark 1 then says the source term is not in the analysis and observed limits are more severe than the linear analysis suggests. **Shown** / **Stated**
17. With the four-wave model the 2D stability reduces to the 1D results of Abgrall & Torlo (§4). **Stated**
18. The first-order version of the scheme "amounts to global Lax–Friedrichs" (§3.2.2). **Stated**
19. The flux limiter ignores the projection onto conservative variables, so weaknesses are expected (§3.2.1). **Stated**
20. Linear advection, CFL 1, $T=10$: finest-mesh slopes 2.08/2.07/2.07 at second order (Table 2) and 4.01/4.01/4.00 at fourth order (Table 3, $L^\infty$ error $6.9070\times10^{-6}$ at $h=0.003125$). **Shown**
21. Isentropic vortex, fourth order in space and time, CFL 1, four-wave model: convergence at the predicted order at $T=5$ (Fig. 6); at $T=200$ on $200\times200$ the pressure error stays in $[-4.2\times10^{-3},1.6\times10^{-3}]$ (Fig. 7). **Shown**
22. Radial Sod ($200\times200$, CFL 1, $T=0.16$): limiter and MOOD give almost identical results; MOOD never activates the first-order scheme and shows over- and undershoots at the shock; with the limiter the overshoot disappears and the undershoot shrinks (§5.2.2, Figs. 8–9). **Shown**
23. Strong radial shock (pressure ratio 1000): MOOD is required; the first-order quads are few and localized at discontinuities (§5.2.3, Fig. 10). **Shown**
24. The streaming part of the algorithm at CFL 1 can be made very efficient (§6). **Stated**

# Printed slips

*(compiler check, not in the sources: every computation in the items below was redone symbolically or numerically from the printed formulas.)*

- §4, symbol maxima: "$g^{(1)}(\vartheta)=1-e^{i\vartheta}$" with "$\max\lvert g^{(1)}\rvert=4$", and "$\max\lvert g^{(2)}\rvert=2$". For $\delta^x_1\mathsf f=\mathsf f_i-\mathsf f_{i-1}$ the symbol is $1-e^{-i\vartheta}$ with maximum 2, while $\lvert g^{(2)}(\pi)\rvert=4$: the two maxima are swapped. The printed $\max\lvert g^{(3)}\rvert=\frac32$, $\max\lvert g^{(4)}\rvert=\frac83$ and the three real-part formulas are correct.
- §4: "we only consider the case $r=1$, $s=2$", while the symbol and §3.1 use $r=1$, $s=3$; "$g^{(4)}(\theta-1)$" and "$g_1=g^{(4)}(\theta)$" should read $g^{(4)}(\vartheta)$ and $g^{(4)}(\vartheta_1)$.
- §4 (iii): $G_4(g)=\frac1{2\theta}(24-g^2,\ 24-12g+2g^2)^\top$, $\theta=24+12g+2g^2$. Solving the printed $2\times2$ system gives $\frac1\theta(\dots)$; the printed factor gives $G_4(0)=(\frac12,\frac12)$ instead of $(1,1)$.
- §4: "$\lvert g\rvert\le\big(\frac{337+\sqrt{104353}}{1152}\big)^{-1}\approx1.745356304$". The bracket is the largest eigenvalue of $M^\top M$, $\approx0.572949$, so $\lVert M\rVert_2\approx0.756934$ and the condition $\lvert g\rvert\lVert M\rVert_2<1$ is $\lvert g\rvert<(\dots)^{-1/2}\approx1.321119$; the printed bound is $1/\lVert M\rVert_2^2$. (The spectral radius of $M$ is $1/(2\sqrt3)$, so the norm condition is only sufficient.)
- Eq. (21): "$G_{2,r+1}(g)-G_3(g)$" should be $G_2(g)$; the following "$\lvert g\rvert g\le2$" should be $\lvert g\rvert<2$.
- Table 1 against the text and Fig. 2: with the printed bound $\lvert\nu g(\vartheta_1)+\mu g(\vartheta_2)\rvert\le2\max(\lvert\mu\rvert,\lvert\nu\rvert)\max\lvert g\rvert\le\rho$, the fourth-order entries equal $0.75\rho=2\rho/\max\lvert g^{(4)}\rvert$, DeC(2,2) and DeC(2,4) equal $\rho$, and DeC(2,3) $=2/\sqrt3$ while $\rho^2_3=\sqrt3$; no single rule maps $\rho$ to the tabulated CFL. "$\sqrt{2.2}\approx1.58$" is wrong ($\sqrt{2.2}=1.483$). For order 2 the table also contradicts claim 14 (DeC(2,4) above DeC(2,3)).
- §3.2.1: "$\delta^x_2\mathsf f-\delta^x_1\mathsf f=\frac16(\mathsf f_{i-2}-3\mathsf f_i+2\mathsf f_{i+1})$" is $\delta^x_3-\delta^x_1$; with the second-order upwind $\delta^x_2$ of §3.1 the difference is $\frac12\mathsf f_{i-2}-\mathsf f_{i-1}+\frac12\mathsf f_i$. The limited difference then double-counts the $\frac16$, and the later "$\delta^x_1(1+\theta r)$" drops it.
- §3.2.1, limiter function: the second branch "$r<-6+\theta$" should be $-6+\alpha$; the third branch "$r>6(M-1)+\alpha$" leaves $(6(M-1)-\alpha,6(M-1)+\alpha]$ uncovered.
- §3.1: the first-order flux is printed $\hat{\mathsf f}_{i+1/2}=\mathsf f_{i+1}$; for $\delta^x_1=\mathsf f_i-\mathsf f_{i-1}$ it is $\mathsf f_i$.
- §3.1: the printed fourth-order centred flux $\frac{\mathsf f_{i-1}}{12}+\frac34\mathsf f_i+\frac34\mathsf f_{i+1}+\frac{\mathsf f_{i+2}}{12}$ does not reproduce the printed $\delta^x_4$ (wrong signs of the $i\pm2$ terms); the consistent flux is $-\frac1{12}\mathsf f_{i-1}+\frac7{12}\mathsf f_i+\frac7{12}\mathsf f_{i+1}-\frac1{12}\mathsf f_{i+2}$. The centred case is not used.
- §3.1, stencil orientation: the general formula for $a>0$ takes $s$ forward points, but every example uses the mirrored, backward-biased stencil; the printed $\alpha_k$ with $r=1$, $s=2$ give $-\frac13\mathsf f_{i-1}-\frac12\mathsf f_i+\mathsf f_{i+1}-\frac16\mathsf f_{i+2}$, the mirror of the printed $\delta^x_3$. Accordingly the first-order error constant is $-\frac12$, not the printed $+\frac12$, and the third-order one is $+\frac1{12}$, the printed $c_{2,1}$ rather than $c_{1,2}$.
- Eq. (15b): the fourth residual repeats the quad label of the third, rows 2 and 4 belong to quads $[i,i+1]\times[j-1,j]$ and $[i-1,i]\times[j,j+1]$, and in row 1 the $\Lambda_y$ term carries $\Delta y$ instead of $\Delta x$.
- Eq. (16): summing the vertex residuals of quad $[i,i+1]\times[j,j+1]$ gives $\frac{\Delta y}2\Lambda_x(\dots)+\frac{\Delta x}2\Lambda_y(\dots)$, not the printed $\frac{\Delta x}2\Lambda_x$, $\frac{\Delta y}2\Lambda_y$, and the $y$ part should involve $\mathsf f_{i,j+1}+\mathsf f_{i+1,j+1}-\mathsf f_{ij}-\mathsf f_{i+1,j}$ rather than repeat the $x$ pattern.
- §2.1 (iii): "Set $\mathbf F^{n+1}=\mathbf F^{(M)}$" uses the number of sub-nodes $M$ as the number of corrections, while Table 1 runs 5 and 6 iterations with $M=2$.
- §2.1, Maxwellian family: the roles of $i$ (angle) and $j$ (speed level) are swapped against the definitions of $\lambda_j$ and $\Lambda_x$; the factor $12iJ/(\lambda(J+1)(2J+1))$ reduces correctly to $2/\lambda$ for the four-wave model.
- §5.2.1: $v_2=\frac{\sqrt2}2+\dots$ in the initial data against $v_{2,\infty}=\frac{\sqrt3}2$ in the free stream and in the vortex centre.
- Lemma 1: the proof uses $\lVert\Lambda_x\rVert^2\lVert\Omega\rVert^2$ but the stated constant has no $\lVert\Omega\rVert$; the hypothesis uses the derivative coefficients $\alpha_l$ for the flux.
- §4: the 2D amplification is written $G^r_k(\nu g(\vartheta_1)+\mu g(\vartheta_2))$, swapping $\mu$ and $\nu$ against $g=\mu g_1+\nu g_2$ (harmless for the bound).
- The values of $\varepsilon$ and $\lambda$ used in the tests are never stated; the radial Sod problem is run with periodic boundaries.
- Typos: "Crank-Nicholson", "iteraion", "bellow", "acccurate", "Liions" (ref. [26]); "convergence for the density" for the scalar advection test.

# Notation map

| Abgrall & Nassajian Mojarrad (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u\in\mathbb R^K$, $A_i(u)$ | $u\in\mathbb R^m$, $f^{(d)}(u)$ | conserved variables and physical flux; **$K$ is the TENO stencil size in the registry** |
| $f\in\mathbb R^L$, $F$ | $\mathsf f$ (page-local), $F$ | kinetic unknowns (point values at nodes) and their vector over the sub-steps ($U$ on the DeC page); **$f$ is the physical flux in the registry** |
| $\Lambda_i$, $\lambda_{ij}$, $\lambda$ | $\Lambda^{(d)}$, $\lambda_{jd}$, $\lambda_{\mathrm k}$ (four-wave model) | diagonal kinetic velocities |
| $\mathbb P$, $\mathbb M$ | kept | projection and Maxwellian |
| $\varepsilon$ | kept | relaxation time; **not the weight regularization $\epsilon$** |
| $N$, $J$, $N'$ | kept | number of kinetic blocks, speed levels, angular count; **$N$ is the DG degree in the registry** |
| $t_{(p)}=t_n+\beta_p\Delta t$, $M$ | $t^{n,m}=t^n+\mathsf t_m\Delta t$, $M_{\mathrm s}$ (as on the [DeC](/methods/deferred-correction.md) page) | deferred-correction sub-nodes; **$\beta_p$ collides with $\beta_k$; $M$ also the limiter bound and a $2\times2$ matrix in §4, and the mass matrix in the registry** |
| $w_{pq}$, $W$, $\mathbf w_0$, $B$ | $\Omega_{mk}$, $\Omega$, kept, kept | collocation weights, their block, first column, $\mathrm{diag}(\beta_p)$; **$B$ is the SBP boundary matrix in the registry** |
| $L_1$, $L_2$ | $\mathcal D^1$, $\mathcal D^2$ | low- and high-order deferred-correction operators, as on the DeC page; **$L$ is the left-eigenvector matrix in the registry** |
| $r$ | kept | correction index; also backward stencil count and limiter ratio |
| $\delta^x$, $\delta^x_q$, $\hat f_{i+1/2,j}$ | kept, $\hat{\mathsf f}_{i+1/2,j}$ | undivided upwind differences of order $q$ and their flux form; **$q$ is the weight exponent in the registry** |
| $\alpha_k$, $\beta_k$, $c_{r,s}$ | kept | Iserles derivative and flux coefficients, error constant; **collide with $\alpha_k$, $\beta_k$** |
| $\Phi^{K,k}_{l,(i,j)}$ | kept | residual sent by quad $K$ to vertex $(i,j)$ |
| $\theta$ (Fourier angle) | $\vartheta$ | reduced wavenumber |
| $\theta$, $r$, $\psi$, $\alpha$, $M$ (§3.2.1) | kept | limiter function, ratio, limiter, margin, bound; **$\theta$ is the Zhang–Shu factor, $\psi$ the entropy potential in the registry** |
| $\gamma$, $\theta$ (Lemma 1, Prop. 1) | $\gamma_{\mathrm{DeC}}$, $\theta_{\mathrm{DeC}}$ (page-local) | Lipschitz and contraction constants |
| $\mu=a\Delta t/\Delta x$, $\nu=b\Delta t/\Delta y$ | kept | directional CFL numbers measured with kinetic speeds; registry $\nu$ is the 1D CFL number |
| $g^{(q)}$, $G_k$, $G_{k,r}$, $\rho^r_k$ | kept | Fourier symbols, amplification factors, stability radii; **$\rho$ is the density in the registry** |
| $\rho$, $\mathbf v$, $p$, $E$, $\gamma$ | $\rho$, $v$, $p$, $E$, $\gamma$ | agrees |
| $\beta$ (§5.2.1) | $\mathcal E$ | vortex strength, 5 |

# Reference list

26 printed references in numbered Springer style ([1]–[26], alphabetical), all
parsed and merged complete into the [bibliography](/bibliography.md) with `citedby`
`abgrall-2024`. No DOIs are printed. Ref. [3] (Abgrall & Torlo 2022, Commun. Math.
Sci.) would take the key of the ingested `abgrall-2022` (Abgrall, Öffner & Ranocha),
a different work, and is entered under a disambiguated key. Ref. [12] prints issue
"7/8"; [16] is a book; [26] is a proceedings volume with the editor printed
"Liions". No printed duplicates were found.

# Pages created or updated

Chunk 4 (2026-10-23), cited further in chunks 5–7 (2026-10-23). This source is cited on:

* [Asymptotic preservation](/properties/asymptotic-preservation.md)
* [Bound preservation](/properties/bound-preservation.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Deferred correction (DeC) time integration](/methods/deferred-correction.md)
* [Discrete kinetic relaxation schemes](/methods/discrete-kinetic-relaxation-scheme.md)
* [IMEX Runge–Kutta schemes](/methods/imex-runge-kutta.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md)
* [MOOD a posteriori limiting](/methods/mood-a-posteriori-limiting.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)

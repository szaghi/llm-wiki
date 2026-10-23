---
type: Method
title: "PAMPA scheme"
description: "PAMPA (Point-Average-Moment PolynomiAl-interpreted) is an Active-Flux-type method that evolves cell averages conservatively and interface point values by a non-conservative residual form; Abgrall et al. make its third-order 1D version bound preserving by blending fluxes and residuals with low-order ones, with closed-form coefficients and GQL positivity."
status: established
aliases: [Point-Average-Moment PolynomiAl-interpreted scheme, BP PAMPA, bound-preserving PAMPA]
tags: [finite-volume, bound-preserving, positivity, limiting, active-flux]
timestamp: 2026-10-23T15:08:00Z
---

# PAMPA scheme

PAMPA (Point-Average-Moment PolynomiAl-interpreted) is the
[Active Flux](/methods/active-flux.md)-type method of Abgrall, as recalled by
[Abgrall et al. (2026)](/sources/abgrall-2026.md) (§1–2): its degrees of freedom are
the cell averages $\bar u_i$ and the point values $u_{i+1/2}$ at the interfaces,
one per interface and shared by the two neighbouring cells. The averages are
evolved by the conservative (flux) form of the conservation law, the point values
by a non-conservative residual form of the same PDE, both by the method of lines.
The point values may be conservative, primitive or entropy variables; Abgrall et
al. use conservative variables for both kinds of degree of freedom and the
third-order version only. Under Lax–Wendroff-type assumptions the scheme
converges to a weak solution, as recalled from Abgrall (§2;
[Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)). The high-order scheme
is not [bound preserving](/properties/bound-preservation.md) and oscillates at
discontinuities; earlier PAMPA papers stabilized it a posteriori with a MOOD-type
fallback ([MOOD a posteriori limiting](/methods/mood-a-posteriori-limiting.md)),
and Abgrall et al. replace that fallback by a priori
[convex limiting](/methods/convex-limiting.md) (§1).

Notation on this page follows the registry with the index shift of the source
page: cell $I_i=[x_{i-1/2},x_{i+1/2}]$ carries $\bar u_i$, node $x_{i+1/2}$ carries
$u_{i+1/2}$ (the source numbers nodes by integers and cells by half integers).

## Third-order scheme

On $I_i$, with $\hat x=(x-x_{i-1/2})/\Delta x\in[0,1]$ (page-local), the solution
is the parabola through the two point values with mean $\bar u_i$,
$$u_h\vert_{I_i}=u_{i-1/2}\,\ell_0(\hat x)+\bar u_i\,\ell_{1/2}(\hat x)+u_{i+1/2}\,\ell_1(\hat x),\qquad
\ell_0=(1-\hat x)(1-3\hat x),\ \ \ell_{1/2}=6\hat x(1-\hat x),\ \ \ell_1=\hat x(3\hat x-2)$$
(Eq. (2.8); $\ell_0,\ell_{1/2},\ell_1$ page-local, not the Lagrange basis of DGSEM
pages). The averages use the physical flux at the shared point values, the
"high-order exact flux",
$$\bar u^{n+1}_i=\bar u^n_i-\frac{\Delta t}{\Delta x}\Big(f(u^n_{i+1/2})-f(u^n_{i-1/2})\Big)\qquad(2.6\mathrm a),$$
and each point value receives one residual from each adjacent cell, a
right-going $\vec\Phi_i$ from $I_i$ and a left-going $\overleftarrow\Phi_{i+1}$ from
$I_{i+1}$ (page-local):
$$u^{n+1}_{i+1/2}=u^n_{i+1/2}-2\frac{\Delta t}{\Delta x}\Big(\vec\Phi_i+\overleftarrow\Phi_{i+1}\Big),\qquad
\vec\Phi^{\mathrm{HO}}_i=a^+\big(u_{i-1/2}-3\bar u_i+2u_{i+1/2}\big),\quad
\overleftarrow\Phi^{\mathrm{HO}}_{i+1}=a^-\big(-2u_{i+1/2}+3\bar u_{i+1}-u_{i+3/2}\big),$$
with $a^\pm$ the positive and negative parts of $f'(u_{i+1/2})$ (Eqs. (2.6b), (2.7),
(2.9)). The residuals are $\tfrac{\Delta x}2a^\pm$ times the one-sided derivatives of
the two cell parabolas at the node *(compiler check, not in the sources: the
derivative of the parabola at $\hat x=1$ is $2(u_{i-1/2}-3\bar u_i+2u_{i+1/2})/\Delta x$)*.
For systems $a^\pm$ becomes $R\Lambda^\pm L$ with $\Lambda^\pm$ the positive and
negative parts of the eigenvalues. Time stepping is SSP-RK3, a convex combination of
forward-Euler steps, so bound preservation of the Euler step carries over
([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).

## First-order scheme

The low-order scheme pairs a local [Lax–Friedrichs](/methods/lax-friedrichs-flux.md)
flux of neighbouring averages with Lax–Friedrichs-type residuals that, unlike the
staggered first-order scheme of Duan, Barsukow & Klingenberg recalled by the
authors, mix point values and averages (Eqs. (2.1)–(2.5)):
$$\hat f^{\mathrm{LO}}_{i+1/2}=\tfrac12\big(f(\bar u_i)+f(\bar u_{i+1})\big)-\tfrac{a_{i+1/2}}2\big(\bar u_{i+1}-\bar u_i\big),\qquad a_{i+1/2}=\max\{\lvert f'(\bar u_i)\rvert,\lvert f'(\bar u_{i+1})\rvert\},$$
$$\vec\Phi^{\mathrm{LO}}_i=\tfrac12\big(f(u_{i+1/2})-f(\bar u_i)\big)-\tfrac{a^{\mathrm L}_{i+1/2}}2\big(\bar u_i-u_{i+1/2}\big),\qquad
\overleftarrow\Phi^{\mathrm{LO}}_{i+1}=\tfrac12\big(f(\bar u_{i+1})-f(u_{i+1/2})\big)-\tfrac{a^{\mathrm R}_{i+1/2}}2\big(\bar u_{i+1}-u_{i+1/2}\big),$$
with $a^{\mathrm L}_{i+1/2}=\max\{\lvert f'(\bar u_i)\rvert,\lvert f'(u_{i+1/2})\rvert\}$ and
$a^{\mathrm R}_{i+1/2}$ the same with $\bar u_{i+1}$ (page-local). As recalled from
Abgrall's earlier work, it is bound preserving under
$\frac{\Delta t}{\Delta x}\max a_{i+1/2}\le\tfrac12$,
$\frac{\Delta t}{\Delta x}\max a^{\mathrm{L,R}}_{i+1/2}\le\tfrac12$ and
$L_f\frac{\Delta t}{\Delta x}\le1$, with $L_f$ the Lipschitz constant of $f$ (page-local) (§2).

## Bound-preserving blending

**Averages** (§3.1, after Vilar). The flux is
$\hat f_{i+1/2}=\hat f^{\mathrm{LO}}_{i+1/2}+\mathsf e_{i+1/2}\Delta\hat f_{i+1/2}$ with the
antidiffusive flux $\Delta\hat f_{i+1/2}=f(u_{i+1/2})-\hat f^{\mathrm{LO}}_{i+1/2}$ and
$\mathsf e_{i+1/2}\in[0,1]$ the weight of the **high-order** flux (page-local; it is
$1-\alpha$ in the convention of the convex-limiting page). The update is the convex
combination
$$\bar u^{n+1}_i=\Big(1-\tfrac{\Delta t}{\Delta x}(a_{i-1/2}+a_{i+1/2})\Big)\bar u_i+\tfrac{\Delta t}{\Delta x}a_{i-1/2}\tilde u^{\mathrm L}_i+\tfrac{\Delta t}{\Delta x}a_{i+1/2}\tilde u^{\mathrm R}_i,$$
$$\tilde u^{\mathrm L}_i=u^*_{i-1/2}+\mathsf e_{i-1/2}\frac{\Delta\hat f_{i-1/2}}{a_{i-1/2}},\qquad
\tilde u^{\mathrm R}_i=u^*_{i+1/2}-\mathsf e_{i+1/2}\frac{\Delta\hat f_{i+1/2}}{a_{i+1/2}},\qquad
u^*_{i+1/2}=\frac{\bar u_i+\bar u_{i+1}}2-\frac{f(\bar u_{i+1})-f(\bar u_i)}{2a_{i+1/2}}$$
(Eqs. (3.1)–(3.4)) under $\Delta t\le\Delta x/(a_{i-1/2}+a_{i+1/2})$, so bound
preservation reduces to admissibility of the intermediate states $\tilde u$. The
state $u^*_{i+1/2}$ is the Lax–Friedrichs bar state (the authors' "first-order
finite volume Riemann intermediate state"), which lies between $\bar u_i$ and
$\bar u_{i+1}$ (§3.1). **Proposition 3.1** (scalar, global bounds
$u_{\min}\le u\le u_{\max}$ of the initial data, page-local): with
$$\mathsf e_{i+1/2}=\min\Big(1,\ \frac{a_{i+1/2}}{\lvert\Delta\hat f_{i+1/2}\rvert}\min\big(u_{\max}-u^*_{i+1/2},\ u^*_{i+1/2}-u_{\min}\big)\Big)$$
(Eq. (3.5)) the averages stay in $[u_{\min},u_{\max}]$; the two-sided minimum is
needed because each coefficient enters one intermediate state with each sign.

**Point values** (§3.2). Each residual is blended separately,
$\vec\Phi_i=\vec\Phi^{\mathrm{LO}}_i+\mathsf t^{\mathrm L}_{i+1/2}\Delta\vec\Phi_i$,
$\overleftarrow\Phi_{i+1}=\overleftarrow\Phi^{\mathrm{LO}}_{i+1}+\mathsf t^{\mathrm R}_{i+1/2}\Delta\overleftarrow\Phi_{i+1}$
(Eq. (3.7); $\Delta\Phi=\Phi^{\mathrm{HO}}-\Phi^{\mathrm{LO}}$, $\mathsf t^{\mathrm{L,R}}$
page-local). Two coefficients per point value are allowed because the point-value
update need not be conservative, which the authors name as the point of the
construction (§3.2). The update becomes
$$u^{n+1}_{i+1/2}=\Big(1-2\tfrac{\Delta t}{\Delta x}(a^{\mathrm L}_{i+1/2}+a^{\mathrm R}_{i+1/2})\Big)u_{i+1/2}
+2\tfrac{\Delta t}{\Delta x}a^{\mathrm L}_{i+1/2}\Big(u^{*,\mathrm L}_{i+1/2}-\mathsf t^{\mathrm L}_{i+1/2}\frac{\Delta\vec\Phi_i}{a^{\mathrm L}_{i+1/2}}\Big)
+2\tfrac{\Delta t}{\Delta x}a^{\mathrm R}_{i+1/2}\Big(u^{*,\mathrm R}_{i+1/2}-\mathsf t^{\mathrm R}_{i+1/2}\frac{\Delta\overleftarrow\Phi_{i+1}}{a^{\mathrm R}_{i+1/2}}\Big),$$
with the node bar states
$u^{*,\mathrm L}_{i+1/2}=\tfrac12(\bar u_i+u_{i+1/2})-\frac{f(u_{i+1/2})-f(\bar u_i)}{2a^{\mathrm L}_{i+1/2}}$ and
$u^{*,\mathrm R}_{i+1/2}=\tfrac12(u_{i+1/2}+\bar u_{i+1})-\frac{f(\bar u_{i+1})-f(u_{i+1/2})}{2a^{\mathrm R}_{i+1/2}}$
(Eqs. (3.9)–(3.12); page-local). **Proposition 3.2:**
$\mathsf t^{\mathrm L}_{i+1/2}=\min\big(1,\frac{a^{\mathrm L}_{i+1/2}}{\lvert\Delta\vec\Phi_i\rvert}\min(u^{*,\mathrm L}_{i+1/2}-u_{\min},\,u_{\max}-u^{*,\mathrm L}_{i+1/2})\big)$,
and $\mathsf t^{\mathrm R}$ likewise, keep the point values in the bounds (Eqs.
(3.13)–(3.14); the proof is printed for one coefficient). Each $\mathsf t$ enters
once, with a minus sign, so a one-sided bound would suffice; the authors take the
two-sided minimum on purpose, against a wrong estimate of the upwind direction that
can flip the sign of $\Delta\Phi$, "especially in the transonic case" (§3.2). The
convex-combination condition of the point update,
$2\frac{\Delta t}{\Delta x}(a^{\mathrm L}_{i+1/2}+a^{\mathrm R}_{i+1/2})\le1$, follows from
the first-order condition $\frac{\Delta t}{\Delta x}\max a^{\mathrm{L,R}}\le\tfrac12$
of §2 *(compiler check, not in the sources)*.

**Local maximum principle and smooth extrema** (§3.3). For the averages the
coefficients can instead enforce local bounds
$u^{\min}_i=\min(\bar u_i,u^*_{i-1/2},u^*_{i+1/2})$, $u^{\max}_i$ likewise (Eq. (3.17)), with
$$\mathsf e_{i+1/2}=\begin{cases}\min\Big(1,\frac{a_{i+1/2}}{\lvert\Delta\hat f_{i+1/2}\rvert}\min\big(u^{\max}_{i+1}-u^*_{i+1/2},\ u^*_{i+1/2}-u^{\min}_i\big)\Big),&\Delta\hat f_{i+1/2}>0,\\
\min\Big(1,\frac{a_{i+1/2}}{\lvert\Delta\hat f_{i+1/2}\rvert}\min\big(u^*_{i+1/2}-u^{\min}_{i+1},\ u^{\max}_i-u^*_{i+1/2}\big)\Big),&\Delta\hat f_{i+1/2}<0\end{cases}$$
(Eq. (3.18)), a formula the authors call standard (Kuzmin, Vilar). A smooth-extrema
detector taken from earlier a posteriori work compares the derivatives of the cell
parabola at the two nodes with the range of the derivatives of the two neighbouring
parabolas there; if both pass (factors equal to 1) the cell is smooth and only the
global bounds are enforced. Neither the local bounds nor the detector act on the
point values, and the authors observed no problem from this; for Euler both act
"naively" on the density only (§3.3, Algorithm 1). In the tests the bounds are
relaxed by $\max\big(10^{-4},10^{-3}(u_{\max}-u_{\min})\big)$, "as usually taken in
MOOD papers" (§4).

## Positivity for the Euler equations

For $G=\{\rho>0,\ \rho e>0\}$ the authors use the
[geometric quasilinearization](/methods/geometric-quasilinearization.md) of Wu & Shu:
$u\in G$ iff $\rho>0$ and $u\cdot n(v_*)>0$ for all $v_*\in\mathbb R$,
$n(v_*)=(v_*^2/2,-v_*,1)^\top$, because $u\cdot n(v_*)=\rho e+\tfrac12\rho(v-v_*)^2$
(§3.4, Eq. (3.19)). Every constraint is then linear in the intermediate state, and
the coefficients are
$$\mathsf e^\rho_{i+1/2}=\min\Big(1,\frac{a_{i+1/2}\,\rho^*_{i+1/2}}{\lvert\Delta\hat f^\rho_{i+1/2}\rvert}\Big),\qquad
\mathsf e^e_{i+1/2}=a_{i+1/2}\min_{v_*\in\mathbb R}\frac{u^*_{i+1/2}\cdot n(v_*)}{\lvert\Delta\hat f_{i+1/2}\cdot n(v_*)\rvert},\qquad
\mathsf e_{i+1/2}=\min(\mathsf e^\rho_{i+1/2},\mathsf e^e_{i+1/2}),$$
and the analogues for $\mathsf t^{\mathrm{L,R}}$ with the node bar states (§3.4). Both
numerator and denominator are quadratics in $v_*$; writing them as
$Q(v_*)=\mathsf a_1v_*^2-2\mathsf b_1v_*+2\mathsf c_1>0$ and
$P(v_*)=\mathsf a_2v_*^2-2\mathsf b_2v_*+2\mathsf c_2$ and setting $v_*=p/q$ (all
page-local), Appendix A obtains the minimum in closed form as a Rayleigh quotient,
$$\min_{v_*}\frac{Q(v_*)}{\lvert P(v_*)\rvert}=\Big(\max_{\lambda\in\sigma(\mathsf C)}\lvert\lambda\rvert\Big)^{-1},\qquad
\mathsf C=\mathsf B^{-1/2}\mathsf A\,\mathsf B^{-1/2},\quad
\mathsf A=\begin{pmatrix}\mathsf a_2&-\mathsf b_2\\-\mathsf b_2&2\mathsf c_2\end{pmatrix},\ 
\mathsf B=\begin{pmatrix}\mathsf a_1&-\mathsf b_1\\-\mathsf b_1&2\mathsf c_1\end{pmatrix},$$
with $\mathsf B$ positive definite because $Q>0$: the inverse spectral radius of a
symmetric $2\times2$ matrix. The maximum over $(p,q)\ne0$ includes $q=0$, the limit
$v_*\to\infty$, where the ratio is $\mathsf a_1/\lvert\mathsf a_2\rvert=\rho^*/\lvert\Delta\hat f^\rho\rvert$,
so the closed form returns the smaller of the energy and the density ratios and is
consistent with the separate density coefficient *(compiler check, not in the
sources)*. The authors state that the same analysis applies in several dimensions,
announced for a separate paper (§1).

## Evidence

All tests use SSP-RK3 at CFL 0.2 (§4).

- **Accuracy and bounds.** On $u_t+u_x=0$ with $u_0=\cos(2\pi x)$ to $t=3$, strict
  global bounds degrade the rates at the finest step $\Delta x=1.25\times10^{-3}$ to
  $2.61$, $2.18$, $1.78$ ($L^1$, $L^2$, $L^\infty$) for the averages and $2.61$,
  $2.20$, $1.81$ for the point values; with the relaxed bounds all rates are
  $3.00$ (Tables 1–2). The authors attribute the loss to the strict global bounds
  (the local principle is switched off by the smooth-extrema detector): the
  coefficients (3.5), (3.13)–(3.14) can be below one on smooth data (Remark 4.1).
- **Scalar discontinuities.** The
  [Jiang–Shu composite wave](/benchmarks/jiang-shu-composite-advection.md) (400
  cells, one period) stays non-oscillatory within $[0,1]$ or $[-0.001,1.001]$; the
  [Burgers](/benchmarks/burgers-equation-tests.md) self-steepening shock shows a
  point-value spike without the blending and none with it, and needs no sonic-point
  treatment; the [Buckley–Leverett problem](/benchmarks/buckley-leverett-problem.md)
  agrees with Zhang & Shu's result (Ex. 1–3).
- **Euler.** On the near-vacuum isentropic problem ($\gamma=3$, minimum density
  $5\times10^{-6}$, pressure $1.25\times10^{-16}$) density and pressure stay positive
  and the density converges at about third order (finest-step $L^1$ order $1.73$,
  attributed to local positivity corrections; Table 3), while without the limiter the
  scheme "quickly blows up" (not plotted). [Sod](/benchmarks/sod-and-lax-shock-tubes.md),
  [Shu–Osher](/benchmarks/shu-osher-problem.md), [LeBlanc](/benchmarks/leblanc-shock-tube.md)
  (to $t=6$, convergence to the shock position with 500, 1000, 5000 cells),
  [double rarefaction](/benchmarks/double-rarefaction-problem.md) and
  [Sedov](/benchmarks/sedov-blast-wave.md) run without failures (Ex. 4–9). The Jacobian
  splitting of PAMPA for Euler "may lead to non-physical solutions", as observed by
  Duan, Barsukow & Klingenberg and others, and the authors state that their blending
  "cures completely this problem" (§2).

## Qualifications

- The coefficients are "optimal" for the sufficient condition that every
  intermediate state be admissible; a larger coefficient could still keep the full
  update admissible *(compiler check, not in the sources)*.
- Propositions 3.1 and 3.2 do not restate the time-step conditions they need; the
  condition for the averages is given before (3.5), the one for the point values
  only in §2.
- The coefficients with $u_{\min}=0$ for the density allow equality,
  $\rho^*\pm\mathsf e\Delta\hat f^\rho/a\ge0$, while §3.4 states strict constraints;
  no margin $\epsilon$ is mentioned.
- Printed slips, by the paper's own definitions: the basis properties print
  $\ell_0(1)=0$ twice where the second row needs $\ell_1(0)=0$ (p. 35); the first
  display of the proof of Prop. 3.1 has $u^*_{j+1}$ where (3.6) and the next display
  have $u^*_j$ (p. 38); the last positivity constraint of p. 44 uses the right-going
  residual where (3.7), (3.11) have the left-going one; §3.4 writes the node bar
  states with indices $j\mp1/2$, otherwise used for cells.
- The Sedov set-up prints nodes $x_i=i\Delta x$, $\Delta x=2/N$, $N=401$,
  $-N\le i\le N$, a span of $[-2,2]$, inconsistent with the central cell
  $[-\Delta x/2,\Delta x/2]$, the "401 cells" of Fig. 10 and the plots on $[-1,1]$, and
  its point pressure $e_{\min}/(\gamma-1)$ does not follow from the paper's
  $p=(\gamma-1)e$ *(compiler check, not in the sources)*.
- One-dimensional only; $\gamma=1.4$ in every Euler test except the isentropic
  problem ($\gamma=3$) and the double rarefaction ($\gamma=5/3$) (§4.2). The
  LeBlanc shock position the authors give, "at time $t=6$, the shock wave should
  be located at $x=8$" (Ex. 7), is that of $\gamma=5/3$: an exact Riemann solve
  of the printed data puts the shock at $x\approx7.98$ for $\gamma=5/3$ and at
  $x\approx7.12$ for $\gamma=1.4$ *(compiler check, not in the sources)*; the
  paper does not say which $\gamma$ its exact solution uses
  ([LeBlanc shock tube](/benchmarks/leblanc-shock-tube.md)).

# Citations

- [Abgrall et al. (2026)](/sources/abgrall-2026.md) — §1; §2, Eqs. (2.1)–(2.9); §3.1–3.4, Eqs. (3.1)–(3.19), Props. 3.1–3.2, Algorithm 1; Appendix A; §4, Ex. 1–9, Tables 1–3, Remark 4.1, Figs. 1–10.

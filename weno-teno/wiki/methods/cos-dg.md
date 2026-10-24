---
type: Method
title: "COS(DG): convex oscillation-suppressing DG"
description: "COS(DG) replaces each DG cell polynomial, once per time step after the last Runge–Kutta stage, by a convex combination of itself and its cell average with an exponential factor driven by entropy-induced distances to the neighbours; it conserves, is locally scale- and evolution-invariant, L2-nonexpansive, entropy non-increasing and accuracy-preserving."
status: established
aliases: [COS, COS(DG), convex oscillation-suppressing DG, convex oscillation suppression, local COS, COS operator]
tags: [dg, limiting, entropy-stable, bound-preserving, low-dissipation]
timestamp: 2026-10-24T06:00:00Z
---

# COS(DG): convex oscillation-suppressing DG

[Cao et al. (2026)](/sources/cao-2026.md) propose a post-processing step for
Runge–Kutta [discontinuous Galerkin](/methods/discontinuous-galerkin.md)
schemes that suppresses spurious oscillations near discontinuities without a
troubled-cell indicator, without characteristic decomposition and without
derivatives of the solution. After the **final** Runge–Kutta stage of each
time step, and only then, the DG polynomial $u_h$ of every cell $I_i$ is
replaced by a convex combination of itself and its cell average,
$$u^{\mathrm{OS}}_h\big\vert_{I_i}=\big(1-\theta^{\mathrm{OS}}_i\big)\,\bar u_i+\theta^{\mathrm{OS}}_i\,u_h\big\vert_{I_i},\qquad \theta^{\mathrm{OS}}_i\in[0,1],$$
so every non-mean mode is scaled by the same factor (page-local
$\theta^{\mathrm{OS}}_i$, $u^{\mathrm{OS}}_h$; §2.1, Eq. (5)). The form is that
of the [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md) with
a different purpose and a different factor. The paper is by the group of
[OEDG](/methods/oedg.md) (same corresponding author), states that COS(DG)
inherits the essential properties of OEDG and of standard DG while enhancing
some of them (§1), and contrasts the two on five points (Remark 3; below).

## The COS factor (1D scalar)

For a scalar law on cells of width $\Delta x_i$, with $N$ the DG degree
(Eqs. (6)–(9)):
$$\theta^{\mathrm{OS}}_i=\exp\Big(-\frac{a_i\,\Delta t}{\Delta x_i}\,\sigma^{\mathrm{OS}}_i\Big),\qquad a_i=\max_{i-1\le\ell\le i+1}\lvert f'(\bar u_\ell)\rvert,\qquad \sigma^{\mathrm{OS}}_i=\sigma^{\mathrm{OS},-}_i+\sigma^{\mathrm{OS},+}_i,$$
$$\sigma^{\mathrm{OS},\pm}_i=\begin{cases}C_{\mathrm{OS}}\,\dfrac{\big\lVert u_{i\pm1}-u_i\big\rVert^2_{L^2(I_{i\pm1})}}{\mathsf N^\pm_i}, & \mathsf N^\pm_i\ge\epsilon_{\mathrm{OS}},\\ 0, & \text{otherwise,}\end{cases}\qquad \mathsf N^\pm_i=\big\lVert u_{i\pm1}-\bar u_i\big\rVert^2_{L^2(I_{i\pm1})},$$
where $u_i$ is the polynomial of cell $i$ **extrapolated** onto the neighbour
$I_{i\pm1}$, so the numerator measures how far the cell's polynomial misses
the neighbour's, and the normaliser is the neighbour's fluctuation about the
cell's own mean (page-local $\sigma^{\mathrm{OS}}_i$, $\mathsf N^\pm_i$,
$C_{\mathrm{OS}}$ and the switch threshold $\epsilon_{\mathrm{OS}}$, not the
weight regularization $\epsilon$). The constants are $C_{\mathrm{OS}}=0.31$, $0.005$, $0.00036$ for $N=1,2,3$ and
$\epsilon_{\mathrm{OS}}=10^{-8}\max\{\bar u_i^2,1\}$, used in every computation of the paper
(§2.1). The factor depends only on cells $i-1$, $i$, $i+1$ (Property 2.1). The
authors state that $\sigma^{\mathrm{OS}}_i$ is $O(\Delta x^{2N})$ in smooth
regions, generically $O(\Delta x^{2N-2})$ near smooth extrema and $O(1)$
across jumps (§2.1, §5.1).

In a modal basis every coefficient of degree $\ge1$ is multiplied by
$\theta^{\mathrm{OS}}_i$; in a nodal basis each nodal value is blended with the
cell average computed by a quadrature exact on $\mathbb P^N$, so the same
step serves modal and nodal DG (§2.1).

**Time step** (Eq. (26)). With an $m$-stage Runge–Kutta method in Shu–Osher
form, the stages start from the previous post-processed solution and run
unmodified; $u^{\mathrm{OS}}_h$ is computed once from the final stage. With
[SSP-RK3](/methods/ssp-runge-kutta.md):
$$\begin{aligned}u^{(1)}_h&=u^{\mathrm{OS},n-1}_h+\Delta t\,\mathcal L\big(u^{\mathrm{OS},n-1}_h\big),\\ u^{(2)}_h&=\tfrac34u^{\mathrm{OS},n-1}_h+\tfrac14\big(u^{(1)}_h+\Delta t\,\mathcal L(u^{(1)}_h)\big),\\ u^n_h&=\tfrac13u^{\mathrm{OS},n-1}_h+\tfrac23\big(u^{(2)}_h+\Delta t\,\mathcal L(u^{(2)}_h)\big),\\ u^{\mathrm{OS},n}_h&=\big(1-\theta^{\mathrm{OS}}\big)\,\bar u^n+\theta^{\mathrm{OS}}\,u^n_h.\end{aligned}$$
OEDG and most limiters act after every stage (§1, Remark 3).

**Damping-ODE form** (Thm 2.3). $u^{\mathrm{OS}}_h$ is the exact solution at
pseudo-time $\hat t=\Delta t$ of the linear problem
$$\frac{d}{d\hat t}\int_{I_i}y_h\,\varphi_h\,dx+\frac{a_i\sigma^{\mathrm{OS}}_i}{\Delta x_i}\int_{I_i}\big(y_h-\bar y_i\big)\,\varphi_h\,dx=0\quad\forall\varphi_h\in\mathbb P^N(I_i),\qquad y_h(\cdot,0)=u^n_h,$$
with the coefficient frozen at $u^n_h$ (page-local $y_h$, test functions $\varphi_h$, $\hat t$); the
fluctuation $y_h-\bar y_i$ decays like $e^{-a_i\sigma^{\mathrm{OS}}_i\hat t/\Delta x_i}$
(Eq. (16)). Remark 4 writes a formal semi-discrete counterpart, DG plus the
term $-\frac{a_i\sigma^{\mathrm{OS}}_i}{\Delta x_i}\int_{I_i}(u_h-\bar u_i)\varphi_h\,dx$,
and leaves its analysis to future work.

## Systems: entropy-induced distances

A component-wise COS, with a diagonal matrix of factors, does not guarantee
entropy stability, and a scalar factor built from the maximum of the
component indicators "often leads to excessive dissipation and loss of
accuracy" (§2.3). The authors keep one scalar factor per cell and replace the
$L^2$ norm in numerator and normaliser by a distance induced by a convex
function $\eta_{\mathrm d}$ of the conserved variables, in practice a convex
[entropy](/properties/entropy-stability.md) (page-local $\eta_{\mathrm d}$,
footnote 1; Eqs. (18)–(21)):

- **Jensen distance**
  $\lVert u_{\mathrm a}-u_{\mathrm b}\rVert^2_{\eta_{\mathrm d},I}=\int_I4\big(\eta_{\mathrm d}(u_{\mathrm a})+\eta_{\mathrm d}(u_{\mathrm b})-2\eta_{\mathrm d}(\tfrac{u_{\mathrm a}+u_{\mathrm b}}2)\big)\,dx$ (Eq. (20));
- **frozen-Hessian distance**
  $\lVert u_{\mathrm a}-u_{\mathrm b}\rVert^2_{\eta_{\mathrm d},I}=\int_I(u_{\mathrm a}-u_{\mathrm b})^\top\,\eta_{\mathrm d}''(\bar u_i)\,(u_{\mathrm a}-u_{\mathrm b})\,dx$ (Eq. (21)).

For $\eta_{\mathrm d}(u)=u^2$ both reduce to the squared $L^2$ distance
(Example 2.1); on a compact convex set where the eigenvalues of
$\eta_{\mathrm d}''$ lie in $[c_{\min},c_{\max}]$, $c_{\min}>0$, both are
bounded below and above by $c_{\min}$ and $c_{\max}$ times the squared $L^2$
distance (Lemma 2.1; page-local $c_{\min}$, $c_{\max}$). A Taylor expansion
links them: the Jensen integrand is $\frac18(u_{\mathrm a}-u_{\mathrm b})^\top\big(\eta_{\mathrm d}''(u_\sharp)+\eta_{\mathrm d}''(u_\flat)\big)(u_{\mathrm a}-u_{\mathrm b})$
for two intermediate states $u_\sharp$, $u_\flat$ on the segment (Eq. (22); page-local
$u_{\mathrm a}$, $u_{\mathrm b}$, $u_\sharp$, $u_\flat$). For the Euler equations
$\eta_{\mathrm d}=-\rho\ln(p\rho^{-\gamma})$ on
$G=\{\rho>0,\ E-\tfrac12\rho\lvert v\rvert^2>0\}$, which is the registry's
$\eta$ up to the factor $1/(\gamma-1)$ (Example 2.2). The Jensen distance
requires the extrapolated polynomials to be admissible, which may need a
positivity limiter before COS; the frozen-Hessian distance is defined for all
states (§2.3). The threshold becomes
$\epsilon_{\mathrm{OS}}=10^{-8}\max\{\eta_{\mathrm d}(\bar u_i),1\}$ and $a_i$ the largest
spectral radius of $A$ at the three cell averages. The authors call the
method characteristic-decomposition-free; it still evaluates spectral radii
and, in the local variant, extremal eigenvalues. Both distances gave "similar
results throughout our test cases", and only the frozen-Hessian one is shown
(§6).

**Multi-D** (§3, Eqs. (24)–(29)). On a quasi-uniform mesh with faces $\mathsf e$ (page-local) and face
neighbours $K'$ of $K$,
$\theta^{\mathrm{OS}}_K=\exp\big(-\sum_{\mathsf e\subset\partial K}\frac{\lvert\mathsf e\rvert\,a_{\mathsf e}\,\Delta t}{\lvert K\rvert}\sigma^{\mathrm{OS}}_{\mathsf e,K}\big)$,
with $\sigma^{\mathrm{OS}}_{\mathsf e,K}$ the 1D indicator built from $K'$ and $a_{\mathsf e}$ the
larger spectral radius of the normal flux Jacobian at $\bar u_K$ and
$\bar u_{K'}$. On a rectangle the exponent is
$-\Delta t\big((a_{i-1/2,j}\sigma_{i-1/2,j}+a_{i+1/2,j}\sigma_{i+1/2,j})/\Delta x+(a_{i,j-1/2}\sigma_{i,j-1/2}+a_{i,j+1/2}\sigma_{i,j+1/2})/\Delta y\big)$.

## Local COS

A cheaper variant applies the damping only at interfaces flagged by a
Lax-type entropy criterion, inspired by a criterion of the literature: the
interface $x_{i+1/2}$ is flagged when
$\lambda_m(\bar u_i)-\lambda_m(\bar u_{i+1})>\delta_{\mathrm L}\big(\lvert\lambda_m(\bar u_i)\rvert+\lvert\lambda_m(\bar u_{i+1})\rvert\big)$
or the same holds for $\lambda_1$, the smallest and largest eigenvalues of
$A$, with $\delta_{\mathrm L}=0.05$ (page-local; Eq. (23)); the condition
$\mathsf N^\pm_i\ge\epsilon_{\mathrm{OS}}$ is then replaced by the flag. In multi-D the
eigenvalues are those of the normal flux Jacobian. The authors state that
$\delta_{\mathrm L}=0.05$ sufficed "across all DG orders and Euler equations
with various Mach numbers" and that the test costs $O(1)$ per interface
(§2.4; see [troubled-cell indicators](/definitions/troubled-cell-indicator.md)).

## Properties proved

- **Conservation** (Property 2.4): cell averages are unchanged.
- **$L^2$ nonexpansiveness** (Thm 2.2):
  $\lVert u^{\mathrm{OS}}_h\rVert_{L^2(\Omega)}\le\lVert u_h\rVert_{L^2(\Omega)}$,
  from $\lVert u^{\mathrm{OS}}_h\rVert^2_{L^2(I_i)}=(\theta^{\mathrm{OS}}_i)^2\lVert u_h\rVert^2_{L^2(I_i)}+\Delta x_i\big(1-(\theta^{\mathrm{OS}}_i)^2\big)\bar u_i^2$
  and Jensen's inequality.
- **Entropy non-increase** (Thm 2.4): for every convex entropy $\eta$, not
  necessarily the $\eta_{\mathrm d}$ of the distance,
  $\int_{I_i}\eta(u^{\mathrm{OS}}_h)\,dx\le\int_{I_i}\eta(u_h)\,dx$, by
  pointwise convexity and Jensen's inequality on the mean, an argument the
  authors liken to that for bound-preserving limiters. An entropy-stable base
  DG scheme therefore stays entropy stable; the authors state that this is not
  guaranteed for OEDG (§1; [entropy stability](/properties/entropy-stability.md)).
- **Local [scale invariance](/properties/scale-invariance.md)** (Property 2.3):
  $\sigma^{\mathrm{OS}}_i$ is unchanged under $u_h\mapsto\sigma u_h+\mu$ on
  the three-cell stencil, so $u^{\mathrm{OS}}_h$ transforms affinely with the
  data; OEDG is invariant only under one affine map of the whole domain,
  because its normaliser is a global range. The invariance holds where the
  switch $\mathsf N^\pm_i\ge\epsilon_{\mathrm{OS}}$ is not active, since $\epsilon_{\mathrm{OS}}$ is not
  invariant *(compiler check, not in the sources)*.
- **Evolution invariance** (Property 2.5, the definition credited to OEDG):
  for $\partial_tu+\lambda_{\mathrm{ev}}\partial_xf(u)=0$ at fixed CFL number,
  $a_i\Delta t$ does not depend on $\lambda_{\mathrm{ev}}$, so results coincide
  at corresponding times (page-local $\lambda_{\mathrm{ev}}>0$).
- **Accuracy of one COS step** (Thm 4.1; 1D scalar Thm 2.1): if $u_h$ is
  $(N+1)$th-order accurate in $L^2$, $N\ge d/2$, the exact solution stays in
  the interior of $G$ and $\eta_{\mathrm d}''\succ0$ there, then there is
  $h^*$ independent of $t$ with
  $\lVert u^{\mathrm{OS}}_h-u_h\rVert_{L^2(\Omega)}\le C\Delta x^{N+1}$ for
  $\Delta x\le h^*$ and $a_{\max}\Delta t/\Delta x\le C_{\mathrm{cfl}}$ (page-local bound $C_{\mathrm{cfl}}$), for
  either distance. The proof uses inverse inequalities, a compact convex
  subset of $G$ containing all extrapolated polynomials for small
  $\Delta x$ (Lemma 4.4) and $1-e^{-c}\le c$.
- **Weighted envelope** (Thms 5.1–5.2). With
  $\mathsf k_i=\nu_i(\Psi^-_i+\Psi^+_i)$, $\nu_i=a_i\Delta t/\Delta x_i$ and
  $\Psi^\pm_i=\sigma^{\mathrm{OS},\pm}_i/C_{\mathrm{OS}}$, so that
  $\theta^{\mathrm{OS}}_i=e^{-C_{\mathrm{OS}}\mathsf k_i}$, and $\mathsf X_i$ the largest
  of three dimensionless measures (overshoot above and undershoot below the
  range of the three neighbouring means, and the size of the modes of degree
  $\ge2$, each divided by a frozen local scale), one COS step gives
  $\mathsf k_i\,\mathsf X_i[u^{\mathrm{OS}}_h]\le1/(e\,C_{\mathrm{OS}})$, from
  $\max_{x\ge0}xe^{-C_{\mathrm{OS}}x}=1/(eC_{\mathrm{OS}})$ (page-local $\mathsf k_i$, $\nu_i$,
  $\Psi^\pm_i$, $\mathsf X_i$; Eqs. (44)–(49)). Corollary 5.1 turns this into
  a design rule: for a tolerance $\tau_{\mathrm v}\in(0,1)$, choosing
  $C_{\mathrm{OS}}\ge1/(e\tau_{\mathrm v})$ guarantees $\mathsf k_i\mathsf X_i\le\tau_{\mathrm v}$
  (page-local $\tau_{\mathrm v}$). The authors read §5 as the justification of
  one problem-independent constant.

## Comparison with OEDG

Cao et al. list five differences from the OE step of
[OEDG](/methods/oedg.md), whose operator they recall exactly and show to be a
modal filter with mode-dependent exponents $\sum_{m\le l}\sigma^m_i$
(Remark 3):

| | OEDG | COS(DG) |
|---|---|---|
| damping | mode-dependent, higher modes more | one factor for all non-mean modes |
| indicator | jumps of derivatives up to order $N$ | differences of extrapolated polynomials, derivative-free |
| frequency | after every Runge–Kutta stage | once per time step |
| scale invariance | global (domain-wide range) | local (three-cell stencil) |
| basis | modal formulation needed | modal or nodal |

They also recall oscillation-free DG (OFDG) of Lu, Liu and Shu, whose damping
terms sit in the semi-discrete form, become stiff at strong discontinuities
and need modified exponential Runge–Kutta methods, and which "may suffer
excessive smearing or persistent oscillations" when scales or wave speeds
vary widely, citing the OEDG paper (§1). Two alternative indicators recalled
after OFDG and OEDG are respectively not scale-invariant and only globally
scale-invariant (Remark 1, Eqs. (10)–(11)).

## Bound preservation

COS controls oscillations, not bounds. In all discontinuous Euler runs the
Zhang–Shu positivity-preserving limiter is applied at the Runge–Kutta stages,
since COS does not act there (§6). Remark 2 proposes, without using it, a
combined limiter of the same convex form with factor
$\min\{\theta^{\mathrm{OS}}_i,\theta_i\}$, $\theta_i$ the Zhang–Shu factor
over $\lceil(N+3)/2\rceil$ Gauss–Lobatto points, and states that DG with
bound-preserving limiters alone "may reduce, but still exhibit, spurious
oscillations" ([bound preservation](/properties/bound-preservation.md)).

## Numerical evidence

Python, double precision, uniform Cartesian meshes, $\mathbb P^1$–$\mathbb P^3$,
CFL number $\nu=0.3$, $0.16$, $0.1$ for $N=1,2,3$, SSP-RK3 on
discontinuous problems and an $(N+1)$-stage order-$(N+1)$ Runge–Kutta method
on smooth ones (§6):

- **Accuracy.** Smooth [Burgers](/benchmarks/burgers-equation-tests.md) at
  $t=0.6$ converges at order $N+1$ (e.g. $N=3$, 1280 cells: $L^1$ error
  $1.37\times10^{-11}$, rate 3.96; Table 1). On the
  [isentropic vortex](/benchmarks/isentropic-vortex.md) at $t=0.01$ the
  $N=1$ rates rise from 1.84 to 2.00, $N=3$ gives 3.98–4.01, and $N=2$ gives
  about 2.8–2.95 ($L^1$ 2.89 at 1280 cells), which the text reads as the
  expected order (Table 2).
- **Comparisons.** Against seven KXRCF-flagged limiters (TVB with tuned
  $M$, the moment limiters of Biswas–Devine–Flaherty and Burbeau–Sagaut–Bruneau,
  [MP](/methods/monotonicity-preserving-limiter.md), modified MP,
  [WENO and simple WENO](/methods/weno-limiter-dg.md)), whose results are
  taken from Zhu et al.'s 2013 comparison, and against OFDG and OEDG,
  third-order COS(DG) gives the sharpest non-oscillatory profiles on a single
  strong shock (pressure ratio $10^5$), the [Lax tube](/benchmarks/sod-and-lax-shock-tubes.md),
  the [Woodward–Colella](/benchmarks/woodward-colella-blast-wave.md) and
  [Shu–Osher](/benchmarks/shu-osher-problem.md) problems (Figs. 1, 6, 8, 10,
  11), and on 2D Burgers (Fig. 13).
- **Multi-scale Lax problem** (Ex. 6.8): two Lax tubes of very different
  amplitude side by side; OEDG shows undershoots in the small-scale part,
  COS(DG) does not (Fig. 9), which the authors attribute to local against
  global scale invariance.
- **Cost** (Table 3; Woodward–Colella and Shu–Osher, 400 cells, one core): the
  OE step takes 35.3–40.6 % of the OEDG run time, the COS step 15.6–18.8 %,
  local COS with its criterion 6.3–10.4 %.
- **1D advection.** Two piecewise-smooth profiles and
  [Jiang–Shu advection](/benchmarks/jiang-shu-composite-advection.md)
  (256 cells; Exs. 6.3–6.5, Figs. 3–5).
- **2D.** Pentagram advection, four [2D Riemann problems](/benchmarks/two-dimensional-riemann-problems.md),
  [double Mach reflection](/benchmarks/double-mach-reflection.md)
  ($960\times240$), where local COS resolves Kelvin–Helmholtz roll-ups along
  the slip line (Fig. 16), and the Mach 80 and Mach 2000
  [jets](/benchmarks/high-mach-astrophysical-jet.md), run with fourth-order
  global COS(DG) plus the positivity limiter (Figs. 17–18).

## Qualifications

- **Design rule and the constants used.** Corollary 5.1 needs
  $\tau_{\mathrm v}<1$, hence $C_{\mathrm{OS}}>1/e\approx0.368$. All three constants
  used in §6 lie below it, and the envelope $1/(eC_{\mathrm{OS}})$ they give is about
  $1.19$, $73.6$ and $1022$ for $N=1,2,3$ *(compiler check, not in the
  sources)*. The constants are therefore empirical, and §5 bounds the
  oscillation measure for them only in this weaker sense.
- **One step, not the scheme.** Theorem 4.1 bounds the perturbation of a
  single COS step applied to an accurate state; accumulation over many steps
  is not analysed, so the convergence of the full COS(DG) scheme rests on the
  tables. The stated $O(\Delta x^{2N})$ behaviour of the indicator is
  asserted, not proved separately.
- **Entropy stability is conditional.** Theorem 2.4 is a cell-wise statement
  about the post-processing; stability of the scheme still needs an
  entropy-stable base DG method and time stepper.
- **Printed slips.** Remark 4 prints the cell average in the semi-discrete
  term as $\bar u_j$; from Eqs. (5) and (13) it is $\bar u_i$ of the cell
  $I_i$. Example 6.8 calls its data the Lax setup combined with "a scaled
  version (by $10^{-4}$)", while the printed states are the Lax density and
  pressure multiplied by $10^2$ on $[-15,0)$ and by $10^{-2}$ on $[0,15]$,
  velocities unscaled, a ratio of $10^4$ between the halves *(compiler
  check, not in the sources)*. The Mach 2000 jet "runs to $t=0.001$" in the
  text while Fig. 18 shows $t=0.0005$, $0.001$ and $0.0015$.

# Citations

- [Cao et al. (2026)](/sources/cao-2026.md) — §1; §2.1, Eqs. (5)–(9), (13), (16), (26), Properties 2.1–2.6, Thms 2.1–2.3, Remarks 1–4; §2.3, Eqs. (18)–(22), Lemma 2.1, Thm 2.4, Examples 2.1–2.2; §2.4, Eq. (23); §3, Eqs. (24)–(29); §4, Thm 4.1, Lemmas 4.1–4.4; §5, Eqs. (44)–(49), Def. 5.1, Thms 5.1–5.2, Cor. 5.1; §6, Exs. 6.1–6.15, Tables 1–3, Figs. 1, 3–18.

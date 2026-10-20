---
type: Method
title: "Bound-preserving flux limiting of Runge–Kutta stages and updates"
description: "Writing a high-order Runge–Kutta update as a low-order Euler update plus antidiffusive fluxes and limiting those fluxes makes explicit methods of any order bound preserving under a forward-Euler step restriction, and DIRK methods with a backward Euler low-order scheme for every step; covers the semi-discrete maximum principle, GMC and FCT limiters, and stage limiting."
status: established
aliases: [GMC limiter, global monolithic convex limiting, space-time flux limiting, flux-corrected transport in time, FCT, monolithic convex limiting, internal SSP, maximum principle preserving flux limiting, MPP flux limiting, SSP stages]
tags: [positivity, ssp, explicit, implicit, structure-preserving, runge-kutta]
timestamp: 2026-10-20T16:00:00Z
---

# Bound-preserving flux limiting of Runge–Kutta stages and updates

[SSP Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md) transfer a
bound that forward Euler preserves to the whole step, but explicit SSP methods stop at
order 4 and implicit ones at order 6 ([Kuzmin et al. 2022](/sources/kuzmin-2022.md), §1,
§3.1.1, recalled). Kuzmin et al. instead enforce bounds on the **fully discrete update**
of a finite-volume scheme for a scalar conservation law, for explicit Runge–Kutta methods
of any order: the high-order update is written as a first-order forward Euler update with
the local Lax–Friedrichs (LLF) flux plus antidiffusive fluxes, and those fluxes are limited
so that the result stays within admissible bounds. The time integrator is unchanged; the
correction is algebraic. Positivity is the case of the bound $0$ from below (Def. 2).
[Quezada de Luna & Ketcheson (2022)](/sources/quezadadeluna-2022.md) carry the
construction to diagonally implicit Runge–Kutta methods and convection–diffusion: the
low-order scheme becomes backward Euler, and the limited scheme keeps the global bounds
for every step size. [Ern & Guermond](/methods/invariant-domain-preserving-time-stepping.md)
limit every stage of an explicit or IMEX method written in incremental form, which is the
same family of ideas organized around the abscissa gaps.

## Semi-discrete maximum principle

**Theorem 1** (§2.1, Eqs. (9)–(12)). Let $G=[\alpha,\beta]^d$ be a box (page-local bounds).
If the ODE can be written

$$y_i'=a_i(y)\bigl(g_i(y)-y_i\bigr),\qquad y\in G\Rightarrow g(y)\in G,\qquad 0\le a_i(y)\le C\ \text{on }G,$$

(page-local $a_i$, $g$, $C$) and has a unique global solution, then $y(t)\in G$ for all
$t\ge0$. The proof shows $y+\epsilon y'\in G$ for $\epsilon<1/C$ (a convex combination of
$y_i$ and $g_i$) and applies Nagumo's invariance lemma (Horváth). The authors call it the
first result of its kind (§1). The first-order LLF finite-volume scheme has this form: with
cell averages $y_i$, faces $S_{ij}$ of the cell $K_i$, wave-speed bounds
$\lambda^{\max}_{ij}$ and the *bar states*
$\bar y_{ij}=\frac{y_i+y_j}2-\frac{(f(y_j)-f(y_i))\cdot n_{ij}}{2\lambda^{\max}_{ij}}$, which lie
between $y_i$ and $y_j$, it reads
$\lvert K_i\rvert y_i'=\sum_j\lvert S_{ij}\rvert\lambda^{\max}_{ij}(\bar y_{ij}-y_i)$ and is
bound preserving (Corollary 1, Eqs. (5)–(8); all symbols page-local). A semi-discretization
is *bound preserving* (BP) for $[y^{\min},y^{\max}]$ if data in the interval stay in it;
"invariant domain preserving" if the interval is an invariant set of the PDE, "positivity
preserving" if it is the nonnegative half-line (Def. 2).

**Diffusion.** Quezada de Luna & Ketcheson (2022, §3, Eqs. (7)–(14)) add a central
diffusive flux with face coefficient $\epsilon_{ij}\ge0$ (page-local) and show that the
convection–diffusion scheme keeps the bar-state form: with
$\lambda_{ij}=\lambda^{\max}_{ij}\bigl(1+\frac{2\epsilon_{ij}}{\lambda^{\max}_{ij}\lvert x_j-x_i\rvert}\bigr)$ the combined bar
state is a convex combination of the advective bar state and the diffusive one
$\frac{y_i+y_j}2$, so it lies between $y_i$ and $y_j$ and the semi-discretization
$\lvert K_i\rvert y_i'=\sum_j\lvert S_{ij}\rvert\lambda_{ij}(\bar y_{ij}-y_i)$ is local
extremum diminishing (page-local symbols). Forward Euler on it is maximum principle
preserving only for $h=O(\Delta x^2)$, because diffusion enters $\lambda_{ij}$
(Remark 1); backward Euler is for every $h$ (Eq. (14), cited to Horváth and others).

## The GMC limiter

The high-order scheme is the LLF scheme plus antidiffusive fluxes $g_{ij}$ (page-local),
the difference between low- and high-order face fluxes. Limited fluxes $\ell_{ij}g_{ij}$,
$\ell_{ij}\in[0,1]$ (page-local), must satisfy, for local bounds
$y^{\min}_i\le y_i\le y^{\max}_i$ and a relaxation parameter $\kappa\ge0$ (page-local),

$$(1+\kappa)\,(y^{\min}_i-y_i)\le\bar y^*_i-y_i\le(1+\kappa)\,(y^{\max}_i-y_i),$$

with $\bar y^*_i$ the flux-corrected bar state (§2.2, Eqs. (14)–(20)); then the corrected
semi-discretization is BP by Theorem 1, with $a_i=(1+\kappa)\omega_i/\lvert K_i\rvert$ and
$\omega_i=\sum_j\lvert S_{ij}\rvert\lambda^{\max}_{ij}$ (page-local; Eq. (18)). The
**global monolithic convex (GMC)** limiter enforces the constraint with Zalesak's
flux-corrected-transport algorithm: sums of positive and negative fluxes, ratios to the
bounds $\mathcal Q^\pm_i$, and $\ell_{ij}=\min$ of the ratios of the two cells (Eqs.
(24)–(26); page-local $\mathcal Q^\pm_i$). Unlike classical FCT, whose bounds depend on
$h$ and on a low-order predictor and hence have no semi-discrete or steady-state
counterpart (Remark 4), the GMC bounds are independent of $h$, which keeps a well-defined
semi-discrete problem and allows convergence to steady states (Remark 6). Larger $\kappa$
relaxes the bounds and improves accuracy but tightens the step restriction: forward Euler
on the limited scheme is BP under the sufficient condition

$$(1+\kappa)\,h\,\omega_i/\lvert K_i\rvert\le1\qquad\text{(Eq. (28))},$$

and any SSP method is then BP for $h\le\mathcal C$ times that bound (§3).

## Limiting the Runge–Kutta update and stages

Kuzmin et al. sort explicit methods into three classes (§3.1):

- **SSP methods**: stages and update are convex combinations of forward Euler steps; the
  GMC-limited semi-discretization needs nothing more.
- **Internal SSP methods** (term introduced there): the stages satisfy the SSP stage
  conditions but the weights need not; Euler-based
  [extrapolation methods](/methods/extrapolation-methods.md), of any order, are the example.
  Only the final update must be limited.
- **General methods**, such as Butcher's seven-stage sixth-order RK76: intermediate stages
  are not BP even for the low-order scheme, and stages and update may need limiting.

**Space–time limiting of the final update** (§3.2, Eqs. (38)–(41)). With the forward Euler
LLF predictor $y^{\mathrm{FE}}_i$ and $H^{\mathrm{RK}}_{ij}=\sum_kb_kH_{ij}(Y_k)$ the
$b$-weighted high-order face flux (page-local),
$y^{\mathrm{RK}}_i=y^{\mathrm{FE}}_i+\frac h{\lvert K_i\rvert}\sum_jg^{\mathrm{RK}}_{ij}$
with $g^{\mathrm{RK}}_{ij}=\lvert S_{ij}\rvert(H^{\mathrm{FE}}_{ij}-H^{\mathrm{RK}}_{ij})$;
limiting $g^{\mathrm{RK}}_{ij}$ with GMC bounds gives an update in
$[y^{\min}_i,y^{\max}_i]$ under (28), conservative because the factors are symmetric and
the fluxes antisymmetric (Remark 5). **Intermediate stages** are limited the same way
against the predictor $y_n+c_kh\cdot(\text{LLF})$, with the bounds scaled by $c_k$
(§3.3, Eqs. (43)–(45)). A Barth–Jespersen-type slope limiter keeps the reconstructions
within the bounds (§3.4).

**Stagewise limiting from the previous stage.** Ern & Guermond ([2022](/sources/ern-2022.md), [2023](/sources/ern-2023.md)) limit every
stage against a low-order Euler step of length $(c_i-c_{i'})h$ taken from the closest
earlier limited stage $Y_{i'}$, after rewriting the tableau in incremental form; the step
bound is then $h_{\mathrm{FE}}$ divided by the largest abscissa gap, and the IMEX version
adds a parabolic limiter after a quasi-linear backward Euler step. They acknowledge
Kuzmin et al. for the idea of limiting after each stage beyond the SSP paradigm and claim
the incremental rewriting and the efficiency maximization as their own (Part I, §1.2). The
method, the efficiency ratio and the comparison are on
[invariant-domain preserving time stepping](/methods/invariant-domain-preserving-time-stepping.md).

## Implicit extension: DIRK methods with a backward Euler low-order scheme

Kuzmin et al. state the implicit extension as possible without showing it (§6).
Quezada de Luna & Ketcheson (2022), both coauthors of Kuzmin et al., show it for
scalar convection–diffusion, with any $M$-stage DIRK method as the high-order scheme and
backward Euler on the local-extremum-diminishing low-order scheme as the low-order one.
The target is the **global** maximum principle
$\min_ju^n_j\le u^{n+1}_i\le\max_ju^n_j$ (page-local cell averages; Eq. (2)).

- **Space–time antidiffusive flux.** The high-order update is written with the
  time-averaged face flux $G^{\mathrm H}_{ij}=\sum_mb_m(\text{convective}-\text{diffusive
  flux})(Y_m)$ of the DIRK stages, and the low-order one with the backward Euler flux
  $G^{\mathrm L}_{ij}$; the limited scheme
  $u^{n+1}_i=u^n_i-\frac h{\lvert K_i\rvert}\sum_j\lvert S_{ij}\rvert\bigl(G^{\mathrm L}_{ij}-\ell_{ij}(G^{\mathrm L}_{ij}-G^{\mathrm H}_{ij})\bigr)$
  corrects the low-order scheme in space and in time at once (page-local symbols; §2,
  §4, Eqs. (6), (19)–(22)). Earlier space–time flux-corrected transport combined
  explicit schemes and was bound preserving only under a step restriction (§1).
- **FCT around the backward Euler solution** (§5, Eqs. (22)–(24)). With
  $u^{\mathrm L,n+1}$ the backward Euler solution, Zalesak's algorithm with bounds
  $Q^\pm_i=\frac{\lvert K_i\rvert}h(u^{\max/\min}-u^{\mathrm L,n+1}_i)$ (page-local) gives
  $u^{\min}\le u^{n+1}_i\le u^{\max}$ for every $h$, conservatively; the limiter is computed
  explicitly once $u^{\mathrm L,n+1}$ is known, at the cost of one extra nonlinear backward
  Euler solve per step. Repeating the limiting on the remaining flux ("iterative FCT",
  Remark 3) recovers accuracy.
- **GMC with an implicit low-order flux** (§6, Thm. 1, Eqs. (25)–(31)). The low-order flux
  is evaluated at $u^{n+1}$ and the limited scheme is rewritten as a backward-Euler-like
  update towards a flux-corrected bar state with the relaxation parameter $\kappa\ge0$ of
  the GMC limiter (they write $\gamma$). Theorem 1: if $u^n_i\in[u^{\min},u^{\max}]$ and the
  limited fluxes satisfy the GMC bounds, then $u^{n+1}_i\in[u^{\min},u^{\max}]$ with no
  restriction on $h$; the scheme is conservative. The bounds depend on $u^{n+1}$, so the
  limiter is part of the nonlinear system, which they solve by a fixed-point iteration
  suggested by Kuzmin, each iterate a convex combination of $u^n_i$ and the target state,
  to $10^{-12}$ (Eq. (31)); Newton with an exact Jacobian is impractical (§6).
- **Intermediate stages** (§7). The bounds above hold for $u^{n+1}$ only. Either every DIRK
  stage is limited too, which "can (at least formally) reduce the order", or the method
  has **SSP stages**: with $X(r)=(I+rA)^{-1}$, if $AX(r)\ge0$ and $AX(r)\mathbf 1\le\mathbf 1$
  entrywise, all stages are bound preserving for $h\le rh_{\mathrm{FE}}$ (Eq. (32)), the
  stage half of the SSP conditions, "more relaxed than those required for the full method
  to be SSP"; Kuzmin et al. call such methods internal SSP. Backward Euler
  [extrapolation methods](/methods/extrapolation-methods.md) satisfy (32) for every $r$,
  so their stages are unconditionally bound preserving (§7.1).

The time discretization need not be SSP, can be of any order and diagonally implicit, so
the scheme avoids the SSP order barriers of 4 (explicit) and 6 (implicit), and existing
high-order implicit SSP methods "are not A-stable" (§1, §9). Their §1 recalls the
Bolley–Crouzeix and Spijker barrier for unconditionally positive general linear methods;
the limited scheme is nonlinear, so the barrier does not bind it (see
[positivity preservation](/properties/positivity-preservation.md)).

**Other implicit uses.** [Sayyari & Yamaleev (2026)](/sources/sayyari-2026.md) (§6.2, Eq.
(22)) blend a high-order entropy-stable residual and a first-order positivity-preserving
residual with an element-wise factor $\theta_f\in[0,1]$ (page-local) inside each
pseudotime iteration of a BDF1 or BDF2 dual time-stepping solver; positivity follows from
the explicit argument because each pseudotime update is a forward Euler step scaled by a
factor in $(0,1)$ (see [implicit stage solvers](/methods/implicit-stage-solvers.md)).
Their blending is a convex combination of whole residuals per element, not a flux-by-flux
limiter.

## Results

With WENO5 in one dimension and global bounds (§5): SSP54 (Kraaijevanger/Spiteri–Ruuth),
ExE-RK5 (fifth-order Euler extrapolation, 11 stages) and RK76, with
$h=0.4\Delta x/(1+\kappa)$.

- Bounds are kept to round-off (undershoots of order $-10^{-15}$ against $-1.32\times10^{-2}$
  for the unlimited scheme at $t=100$ on a composite advection profile; Fig. 2).
- With $\kappa=1$ all limited schemes keep their optimal rates on smooth linear advection;
  with $\kappa=0$ only RK76 limited at the final update keeps order 5, while SSP54,
  ExE-RK5 and stagewise-limited RK76 fall to 2.66–2.70 (Table 3). On Burgers before the
  shock $\kappa=1$ suffices except for ExE-RK5, which needs $\kappa\ge2$ (Table 4). On the
  semi-discrete operator alone, GMC with $\kappa\ge0.5$ keeps the sixth-order WENO rate,
  and $\kappa=0$ drops it to 3 (Table 2).
- Global bounds do not cure non-entropic solutions: a non-WENO fifth-order reconstruction
  with RK76 converges to a wrong solution of a nonconvex KPP problem, with or without the
  limiter (Table 5).
- The authors state that limiters enforcing **local** bounds are at most second-order
  accurate, while global bounds do not degrade the rates of smooth solutions (§1, citing
  Zhang–Shu); Quezada de Luna & Ketcheson (2022, §1) repeat the statement for TVD and FCT
  limiters.

With WENO5, the five-stage fifth-order SDIRK of Kennedy & Carpenter and $h=0.5\Delta x$,
Quezada de Luna & Ketcheson (2022, §8) report:

- **Bounds.** The unlimited WENO-SDIRK scheme violates the bounds on every test (e.g.
  $\delta=-2.08\times10^{-5}$ on advection, $-2.41\times10^{-5}$ on viscous Burgers,
  $-6.03\times10^{-8}$ on KPP, about $-4\times10^{-2}$ at intermediate times on solid-body
  rotation and swirling vortex, with $\delta$ the smallest distance to the bounds over all
  steps, page-local); the FCT and GMC versions stay within round-off (Figs. 2–8). Backward
  Euler alone is bound preserving but very dissipative (error $9.42\times10^{-1}$ against
  $1.25\times10^{-4}$ on advection, Table 1).
- **Accuracy.** On linear advection ($\epsilon=0$) full accuracy needs two FCT iterations
  ($1.15\times10^{-4}$, rate 4.15) or $\kappa\ge2$ ($1.16\times10^{-4}$, rate 4.15); with one
  iteration or $\kappa=0$ the rate falls to 3.65 or 3.10 (Table 1). With physical diffusion
  $\epsilon=10^{-3}$ one iteration and $\kappa=0$ suffice, rates 4.52–4.55 (Table 2), and
  in two dimensions two iterations or $\kappa\ge1$ (Table 5). Backward Euler extrapolation
  IEX4 with MPP stages gives rates 3.63–4.61 (Table 3).
- **Entropy.** Global bounds do not select the entropy solution; on KPP the limited
  schemes keep $u\in[\pi/4,14\pi/4]$ "without a noticeable degradation in accuracy", and
  only the dissipative backward Euler scheme is entropy stable for every entropy pair
  (§8.8).

## Qualifications

- **Scope.** Kuzmin et al. treat scalar conservation laws, periodic one-dimensional tests
  and explicit methods, and state the extension to finite elements, implicit Runge–Kutta
  methods and entropy stability as possible, not shown (§6). The implicit extension has
  since been shown, for DIRK methods and scalar convection–diffusion in one and two
  dimensions, by Quezada de Luna & Ketcheson (2022, §§4–7); Ern & Guermond (2022, 2023)
  give finite-element and IMEX versions of stagewise limiting. Finite elements for the
  GMC update itself and entropy stability remain unshown in the ingested sources.
- **Measured order with a fifth-order baseline.** Quezada de Luna & Ketcheson pair WENO5
  with a fifth-order SDIRK and refine $h=0.5\Delta x$ with the mesh, yet every measured
  rate, unlimited baseline included, is about 4 (3.3–4.7), which they call "full
  accuracy" (Tables 1–5). The paper does not separate temporal from spatial error and
  does not explain the gap, so the temporal order of the limited DIRK schemes is not
  established by these tables; stiff order reduction of a stage-order-one SDIRK on the
  diffusive tests would be one candidate, not discussed there *(compiler remark, not in
  the sources)*.
- **"No step restriction" is a property of the solution.** Theorem 1 of Quezada de Luna &
  Ketcheson concerns the solution of the nonlinear limited system; convergence of their
  fixed-point iteration for large $h$ is not analysed (§6).
- **Printed slips** *(compiler checks of pp. 31–32)*. The
  one-dimensional bound (B.7b) omits the factor $\omega_i$ in the relaxation term of
  $\mathcal Q^+_i$, unlike (20) and the companion $\mathcal Q^-_i$. The SSP step bound
  (B.9) places $(1+\kappa)$ in the numerator, $h\le\mathcal C(1+\kappa)\Delta x/(\cdot)$,
  whereas (28) and the step $0.4\Delta x/(1+\kappa)$ of §5 require it in the denominator.
  Appendix A.1 calls the Shu–Osher form of SSP54 its "Butcher form".
- **Local versus global bounds.** The "at most second order" statement for local bounds
  is a blanket claim attributed to Zhang–Shu; Kuzmin et al. themselves relax the bounds
  with $\kappa>0$ to recover accuracy, so it is recorded as attributed, not as established.

# Citations

- [Kuzmin et al. (2022)](/sources/kuzmin-2022.md) — §1, §2.1 (Defs. 1–3, Thm. 1, Cor. 1, Eqs. (3)–(13)), §2.2 (Eqs. (14)–(26)), §3 (Eqs. (27)–(30), Remark 4), §3.1–3.4 (Eqs. (31)–(49), Remarks 5–6), §4, §5 (Tables 2–5, Figs. 2–4), §6, App. A–B; arXiv v2.
- [Quezada de Luna & Ketcheson (2022)](/sources/quezadadeluna-2022.md) — §1, §2 (Eqs. (2), (5)–(6)), §3 (Eqs. (7)–(16), Remark 1), §4 (Eqs. (17)–(21), Remark 2), §5 (Eqs. (22)–(24), Remark 3), §6 (Thm. 1, Eqs. (25)–(31)), §7 (Eq. (32), §7.1), §8 (Tables 1–5, Figs. 2–8), §9; arXiv v1.
- [Ern & Guermond (2022)](/sources/ern-2022.md) — §1.2, §3, §5.3; HAL v2.
- [Ern & Guermond (2023)](/sources/ern-2023.md) — §2.3–2.4, §3.3; HAL v1.
- [Sayyari & Yamaleev (2026)](/sources/sayyari-2026.md) — §6.2 (Eq. (22)); arXiv v3.

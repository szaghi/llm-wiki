---
type: Method
title: "Bound-preserving flux limiting of Runge–Kutta stages and updates"
description: "Writing a high-order Runge–Kutta update of a finite-volume scheme as a low-order forward Euler update plus antidiffusive fluxes, and limiting those fluxes against step-independent bounds, makes explicit Runge–Kutta methods of any order bound preserving under a forward-Euler-type step restriction; the page covers the semi-discrete maximum principle, the GMC limiter and its stage and final-update variants."
status: established
aliases: [GMC limiter, global monolithic convex limiting, space-time flux limiting, flux-corrected transport in time, FCT, monolithic convex limiting, internal SSP]
tags: [positivity, ssp, explicit, structure-preserving, runge-kutta]
timestamp: 2026-10-20T10:00:00Z
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
  Zhang–Shu).

## Qualifications

- **Scope.** Scalar conservation laws, periodic one-dimensional tests, explicit methods.
  The extension to finite elements, implicit Runge–Kutta methods and entropy stability is
  stated in the conclusions as possible, not shown (§6).
- **Printed slips** *(compiler checks of pp. 31–32)*. The
  one-dimensional bound (B.7b) omits the factor $\omega_i$ in the relaxation term of
  $\mathcal Q^+_i$, unlike (20) and the companion $\mathcal Q^-_i$. The SSP step bound
  (B.9) places $(1+\kappa)$ in the numerator, $h\le\mathcal C(1+\kappa)\Delta x/(\cdot)$,
  whereas (28) and the step $0.4\Delta x/(1+\kappa)$ of §5 require it in the denominator.
  Appendix A.1 calls the Shu–Osher form of SSP54 its "Butcher form".
- **Local versus global bounds.** The "at most second order" statement for local bounds
  is a blanket claim attributed to Zhang–Shu; Kuzmin et al. themselves relax the bounds
  with $\gamma>0$ to recover accuracy, so it is recorded as attributed, not as established.

# Citations

- [Kuzmin et al. (2022)](/sources/kuzmin-2022.md) — §1, §2.1 (Defs. 1–3, Thm. 1, Cor. 1, Eqs. (3)–(13)), §2.2 (Eqs. (14)–(26)), §3 (Eqs. (27)–(30), Remark 4), §3.1–3.4 (Eqs. (31)–(49), Remarks 5–6), §4, §5 (Tables 2–5, Figs. 2–4), §6, App. A–B; arXiv v2.

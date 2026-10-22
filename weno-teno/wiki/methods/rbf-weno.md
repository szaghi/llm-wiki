---
type: Method
title: "RBF-based WENO"
description: "RBF-based WENO replaces the polynomial candidates of finite-difference WENO by radial-basis-function interpolants; Jeong, Yang and Yoon's WENO-G uses Gaussians plus linear polynomials interpolated in the cell-average sense, RBF-dependent ideal weights and a locally fitted shape parameter that makes the five-point scheme sixth order, with new exponential-moment smoothness indicators."
status: established
aliases: [RBF-WENO, WENO-G, Gaussian RBF WENO, radial basis function WENO, RBF-ENO]
tags: [weno, reconstruction, finite-difference]
timestamp: 2026-10-23T10:00:00Z
---

# RBF-based WENO

An RBF-based WENO keeps the stencils and the weighting of [WENO](/methods/weno-js-reconstruction.md) but
builds the candidate and global interpolants in a space spanned by translates of a radial basis
function, possibly augmented by low-degree polynomials. Jeong, Yang & Yoon (2022, §1) recall the
lineage: Iske–Sonar and Sonar, Aboiyar et al. (polyharmonic-spline ADER-WENO), Bigoni & Hesthaven
(multiquadrics, arbitrary order), Hesthaven & Mönkeberg (RBF-ENO, entropy-stable, 2-D unstructured),
Guo & Jung, Han et al. (Gauss-kriging) and Christlieb, Sands & Yang, and the exponential-polynomial
WENO of Ha et al. Their own scheme, **WENO-G**, is a finite-difference scheme on the five-point
stencil of WENO5 that reaches sixth order.

## Cell-average Gaussian interpolation

In the [conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
the point fluxes are cell averages of an implicit function, so the interpolant must match cell
averages, not point values. With the Gaussian $\phi_{\mathrm G}(x)=e^{-\lambda_{\mathrm s}^2x^2}$
(page-local; shape parameter $\lambda_{\mathrm s}$) the space is
$\Phi_m=\mathrm{span}\{\phi_{\mathrm G}(\cdot-x_n):x_n\in\text{stencil}\}+\mathbb P^1$, $m=3$ or 5
(Eq. (12)), and the interpolant is written in Lagrange form $\sum_n\Psi_n(x)\bar h_n$ (page-local
$\Psi_n$, $\bar h_n$ the cell averages, i.e. the point fluxes), with the $\Psi_n$ fixed by reproducing
every $g\in\Phi_m$ in the cell-average sense, $\sum_n\Psi_n(x)\frac1{\Delta x}\int_{I_n}g=g(x)$
(Eqs. (14)–(17)). Proposition 3.2 proves that the result matches the given cell averages. Unique
solvability of the linear system is argued only "at least for small $\Delta x$", by the limit of the
cell-averaged translates (§3.2). Remark 3.4 contrasts this with the earlier route of
[1, 3, 23–25] in the paper, which applies the averaging functional to each translate and works in the
space of averaged RBFs; WENO-G stays in the original RBF space.

As $\lambda_{\mathrm s}\Delta x\to0$ the coefficients at $x_{i+1/2}$ tend to the classical five-point
ones $(\tfrac1{30},-\tfrac{13}{60},\tfrac{47}{60},\tfrac9{20},-\tfrac1{20})$, with explicit
corrections in $(\lambda_{\mathrm s}\Delta x)^2$ and $(\lambda_{\mathrm s}\Delta x)^4$ (Remark 3.3,
Appendix Eq. (56)).

## RBF ideal weights

All three local interpolants on the three-point substencils use one space $\Phi_3$ built on the
central substencil $\{x_{i-1},x_i,x_{i+1}\}$; this makes the ideal weights $\bar d_k$ (page-local)
that recombine them into the global interpolant exist and be unique (§3.3, Eqs. (21)–(24)):
$\bar d_0=C_0/C_{0,0}$, $\bar d_2=C_4/C_{2,2}$, $\bar d_1=1-\bar d_0-\bar d_2$, with $C_n$ and $C_{k,n}$
the global and local Lagrange coefficients at $x_{i+1/2}$. They depend on $\lambda_{\mathrm s}\Delta x$
and tend to $(\tfrac1{10},\tfrac35,\tfrac3{10})$ as $\Delta x\to0$. The paper stresses (§3.3,
Remark 2.1) that an RBF space is not shift- and scale-invariant, unlike polynomials, so the
order of the flux difference needs $\lambda_{\mathrm s}$ to vary slowly between neighbouring
interfaces.

## Sixth order from the shape parameter

The truncation error of the five-point Gaussian interpolant at $x_{i+1/2}$ is (Eq. (26))

$$h(x_{i+1/2})-\hat f_{i+1/2}=\tfrac1{60}\big(h^{(5)}+14h^{(3)}\lambda_{\mathrm s}^2\big)\Delta x^5+O(\Delta x^6),$$

(Eq. (26) writes it as the expansion of the interpolant), so the local choice
$\lambda_{\mathrm s,i+1/2}^2\approx-\tfrac1{14}f^{(5)}/f^{(3)}$ (Eq. (27)) cancels the $\Delta x^5$
term. **Theorem 3.5:** for $h\in C^6$ on an interval containing the stencil, the flux difference
approximates $\partial_xf(x_i)$ to $O(\Delta x^6)$; the proof uses
$\lambda_{\mathrm s,i+1/2}-\lambda_{\mathrm s,i-1/2}=O(\Delta x)$. The authors liken this to finite-element
superconvergence: one order above what polynomials of the same dimension give (§3.4). Where
$h^{(3)}\approx0$ the expansion is truncated after the $(\lambda_{\mathrm s}\Delta x)^2$ term, which keeps
sixth order without dividing by a vanishing denominator; where $f^{(5)}\approx0$ one may set
$\lambda_{\mathrm s}=0$, the polynomial interpolant (Remark 3.7). $f^{(3)}$ and $f^{(5)}$ come from
divided differences over the six points that the split-flux reconstruction involves (Remark 3.6). With
WENO weights, $\omega^\pm_k-\bar d_k=O(\Delta x^4)$ suffices for sixth order (Eq. (41), after Hu, Wang &
Adams).

## Weights and indicators

The weights are of [WENO-Z](/methods/weno-z.md) type with the RBF ideal weights,
$\alpha_k=\bar d_k\big(1+(\tau_{\mathrm G}/(\beta_k+\epsilon))^q\big)$, $q=1$ except $q=2$ for the
interacting blast waves (Eq. (39)), with new indicators built from "generalized undivided differences"
that annihilate exponentials (§4; [smoothness indicators](/definitions/smoothness-indicator.md)):
$\beta_k=(\theta_{\mathrm G}|\nabla^1_kf|+|\nabla^2_kf|)^2$ and $\tau_{\mathrm G}=|\nabla^4f|^2$
(page-local; $\theta_{\mathrm G}=0.1$ for advection, 0.25 for Euler). **Proposition 4.5:** with
$\epsilon=\Delta x^\ell$, $0<\ell\le4(2q-1)/q$, $|\omega_k-\bar d_k|\le c\Delta x^4$ "regardless of
critical points" ([critical-point accuracy](/properties/critical-point-accuracy.md)). The numerical
value of $\epsilon$ used in the experiments is not given.

## Results (Jeong, Yang & Yoon 2022, §5)

FD with global Lax–Friedrichs splitting (called "local" in the paper), characteristic decomposition for
Euler, TVD-RK3 at CFL 0.4 and classical RK4 with $\Delta t\sim\Delta x^{3/2}$ for order tests.

- Sixth order: linear advection of $\sin^2(2\pi x)$, $L^\infty$ error $3.08\times10^{-10}$ at $N_x=640$
  (order 6.00) against $1.62\times10^{-7}$ (WENO-JS) and $1.96\times10^{-8}$ (WENO-M, WENO-Z); on
  $\sin(2\pi x-\sin(2\pi x)/\pi)$, which has critical points, WENO-G keeps 6.01 where WENO-JS drops to
  3.5–4.1 (Tables 1–2); [Burgers](/benchmarks/burgers-equation-tests.md) $L^\infty$ order 6.01 (Table 4);
  1-D Euler density wave 5.99 (Table 6).
- Cost (MATLAB): 1.3–1.9 times WENO-JS at equal $N_x$ (e.g. 57.18 s against 40.30 s at 640 points,
  Table 3), but less error per CPU time on smooth advection (Fig. 1).
- Shock problems ([Shu–Osher](/benchmarks/shu-osher-problem.md),
  [Sod and Lax](/benchmarks/sod-and-lax-shock-tubes.md),
  [Woodward–Colella](/benchmarks/woodward-colella-blast-wave.md),
  [2-D Riemann](/benchmarks/two-dimensional-riemann-problems.md),
  [double Mach reflection](/benchmarks/double-mach-reflection.md)): sharper waves and contacts than
  WENO-JS, WENO-M and WENO-Z by visual comparison only. The exponential-moment indicators beat the
  Jiang–Shu ones inside the same RBF scheme (Example 5.9). Multiquadric and inverse multiquadric RBFs
  gave "better or at least similar" results (Remark 5.12, no data).

## Qualifications

- Eq. (27) gives $\lambda_{\mathrm s}^2<0$ whenever $f^{(5)}$ and $f^{(3)}$ have the same sign, which
  turns the Gaussian into a growing exponential of $x^2$; likewise the fitted exponent $\nu_k^2=f''/f+O(\Delta x)$ of the
  exponential undivided differences (page-local $\nu_k$, Eq. (34)) can be negative. Neither case, nor the thresholds for "$h^{(3)}\approx0$" and
  "$f^{(5)}\approx0$", is addressed in the paper.
- The sixth order is a smooth-data, linear-weight result; the shock tests carry no error norms.
- Jeong, Yang & Yoon print the third classical coefficient as $\tfrac{47}{30}$ (Eq. (19)); their own
  Appendix (56) gives $\tfrac{47}{60}$, and only that value makes the coefficients sum to 1.
- They recall WENO-Z with $\tau_5=|\beta_2-\beta_0|^2$, squared (Eq. (10)), where the other sources of
  the bundle write $|\beta_0-\beta_2|$ ([WENO-Z](/methods/weno-z.md)); the recall is not used in their
  scheme.

# Citations

- [Jeong, Yang & Yoon (2022)](/sources/jeong-2022.md) — §1; §2, Eqs. (3)–(10), Remark 2.1; §3, Eqs. (11)–(28), Prop. 3.2, Remarks 3.3–3.7, Theorem 3.5; §4, Eqs. (29)–(43), Prop. 4.5; §5, Tables 1–7, Figs. 1–10, Remark 5.12; App., Eqs. (54)–(56).

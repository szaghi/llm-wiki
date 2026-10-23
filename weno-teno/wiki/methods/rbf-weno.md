---
type: Method
title: "RBF-based WENO"
description: "RBF-based WENO and TENO replace polynomial candidates by radial-basis-function interpolants: Jeong, Yang and Yoon's WENO-G fits the Gaussian shape parameter to reach sixth order on five points with RBF ideal weights; Liang and Fu's Gaussian-RBF TENO selects one target stencil by TENO flags, needs no linear weights and adapts the shape parameter to the local scale."
status: established
aliases: [RBF-WENO, WENO-G, Gaussian RBF WENO, radial basis function WENO, RBF-ENO, non-polynomial TENO, Gaussian RBF TENO]
tags: [weno, teno, reconstruction, finite-difference]
timestamp: 2026-10-23T23:55:00Z
---

# RBF-based WENO

An RBF-based WENO keeps the stencils and the weighting of [WENO](/methods/weno-js-reconstruction.md) but
builds the candidate and global interpolants in a space spanned by translates of a radial basis
function, possibly augmented by low-degree polynomials. Jeong, Yang & Yoon (2022, §1) recall the
lineage: Iske–Sonar and Sonar, Aboiyar et al. (polyharmonic-spline ADER-WENO), Bigoni & Hesthaven
(multiquadrics, arbitrary order), Hesthaven & Mönkeberg (RBF-ENO, entropy-stable, 2-D unstructured),
Guo & Jung, Han et al. (Gauss-kriging) and Christlieb, Sands & Yang, and the exponential-polynomial
WENO of Ha et al. Their own scheme, **WENO-G**, is a finite-difference scheme on the five-point
stencil of WENO5 that reaches sixth order. Liang & Fu (2024a) carry Gaussian RBFs into
[TENO](/methods/targeted-eno.md) with a different answer to the linear-weight problem (last section).

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

## Gaussian-RBF TENO without linear weights (Liang & Fu 2024a)

Liang & Fu (2024a) build a fifth-order finite-difference scheme of the [TENO](/methods/targeted-eno.md)
family whose candidates are Gaussian-RBF interpolants and which needs no linear weights. They list three
drawbacks of the RBF and exponential-polynomial WENO variants above: one fixed non-polynomial basis over
the whole domain, optimal linear weights that are "complicated and time-consuming" or may "not exist"
with non-polynomial bases above third order, and shape-parameter fitting by ratios of high derivatives,
which they call unstable at critical points, citing Jeong et al. among others (§1). Jeong et al.'s
WENO-G answers the second point by building all three local spaces on the central substencil (above);
Liang & Fu answer it by dropping the convex combination.

**Stencil selection.** The TENO5 machinery ($q=6$, $C_T=10^{-5}$, $\tau_5=|\beta_1-\beta_2|$ of the
two non-central candidates in their numbering) is kept only to classify the three three-point
stencils as smooth ($\delta_k=1$) or not. Each flag pattern selects one *target stencil*, "which utilizes
as many smooth data as possible while not crossing the non-smooth region": the five-point stencil when
all are smooth, a four-point one ($\{x_{i-2},\dots,x_{i+1}\}$ or $\{x_{i-1},\dots,x_{i+2}\}$) when the
downwind or the upwind candidate is cut, a three-point one when only one candidate is smooth (§3.1,
Fig. 2). The flux is the single reconstruction on the target stencil, so the order "recursively"
drops from 5 to 4 to 3 near discontinuities, against classical TENO5, in which the renormalized
combination of two candidates "will not achieve any accuracy order" above that of one candidate (§3.1).
This is the stencil logic of [adaptive TENO](/methods/adaptive-teno.md) of Fu et al., by which the authors
say it is "motivated". *(Compiler check, not in the sources: the all-cut pattern cannot occur, since
$\sum_k\chi_k=1$ forces $\max_k\chi_k\ge\tfrac13>C_T$.)*

**Interface-centred Gaussians on the primitive.** On a target stencil $\{I_{i-r},\dots,I_{i+k}\}$
the primitive $H(x)=\int_{x_{i-r-1/2}}^xh\,d\xi$ (page-local) is known at the interfaces,
$H(x_{l+1/2})=\Delta x\sum_{j=i-r}^lf_j$, and is interpolated there by
$R(x)=\sum_j\alpha^{\mathrm R}_j\exp\big(-\lambda_{\mathrm s}^2(x-x_{j+1/2})^2\big)$ with Gaussians centred at
the interfaces and no polynomial augmentation ($\alpha^{\mathrm R}_j$ page-local); $R'$ is the flux,
with $R'=h+O(\Delta x^{k+r+1})$ (Eqs. (18)–(24)). A Taylor expansion "up to degree
$\lambda_{\mathrm s}^2\Delta x^2$" gives explicit fluxes, e.g. on the five-point stencil (Eq. (25))

$$\hat f_{i+1/2}=\tfrac1{60}\big(2f_{i-2}-13f_{i-1}+47f_i+27f_{i+1}-3f_{i+2}\big)
-\tfrac{\lambda_{\mathrm s}^2\Delta x^2}{60}\big(-12f_{i-2}+18f_{i-1}+18f_i-42f_{i+1}+18f_{i+2}\big),$$

the classical fifth-order flux plus a zero-sum correction stencil; the four- and three-point fluxes have
the same structure around the fourth-order and ENO3 fluxes. Their error expansion (Eq. (29)) gives
$h-\hat f_{i+1/2}=\tfrac1{60}\big(h^{(5)}+30\lambda_{\mathrm s}^2h^{(3)}\big)\Delta x^5+O(\Delta x^6)$
on five points, fourth order on four, third on three, the $\lambda_{\mathrm s}^2$ terms entering at the order
of the polynomial truncation term. *(Compiler check, not in the sources: substituting the cell-average
expansions of Eq. (28) into the $\lambda_{\mathrm s}^2$ parts of all six fluxes of Eq. (25) reproduces the
$\lambda_{\mathrm s}^2$ terms of Eq. (29); at $\lambda_{\mathrm s}=0$ the fluxes are the polynomial ones, and each
correction stencil sums to zero.)* Jeong et al.'s Eq. (26) has the same polynomial term with
$14\lambda_{\mathrm s}^2h^{(3)}$. *(Compiler check, not in the sources: the two interpolation spaces differ
(cell-centred Gaussians plus $\mathbb P^1$ in the cell-average sense, against interface-centred Gaussians on the
primitive), so the coefficients need not agree.)*

**Shape parameter from the local scale.** Instead of cancelling the leading error, Liang & Fu set
$\lambda_{\mathrm s}=\lambda_0+\lambda_\Delta\big(1-\varphi(\mu_d)\big)$ with $\varphi(\mu_d)=(1-\mu_d)^4(1+4\mu_d)$,
$\mu_d=1-\min\big(1,\min(\sigma_{i-1},\sigma_i,\sigma_{i+1})/C_r\big)$ with Ren et al.'s ratio
$\sigma_i=\big(|2(f_i-f_{i-1})(f_{i+1}-f_i)|+\epsilon_\sigma\big)/\big((f_i-f_{i-1})^2+(f_{i+1}-f_i)^2+\epsilon_\sigma\big)$,
$C_r=0.4$, $\lambda_0=\lambda_\Delta=3$, $\epsilon_\sigma=10^{-40}$ (Eqs. (30)–(32); the source's $\alpha_1,\alpha_2,m,\eta_i,g,c_r,\varepsilon$;
$\lambda_0,\lambda_\Delta$ page-local, $\mu_d$, $\sigma_i$, $\varphi$, $C_r$, $\epsilon_\sigma$ as on
[adaptive TENO](/methods/adaptive-teno.md)): a flat kernel ($\lambda_{\mathrm s}\to3$) in smooth low-wavenumber regions, a sharp one
($\lambda_{\mathrm s}\to6$) at high-wavenumber fluctuations. In cells that the TENO-flag detector of
Liang et al. (2022) marks as genuine discontinuities, the flux is the two-steepness tanh jump flux of
that work ($\mathcal A=0.91$, or 1.23 under the stricter sensor; first-order fallback where
$(f_{i+1}-f_i)(f_i-f_{i-1})\le10^{-15}$; §3.3, Eqs. (33)–(36); [TENO-THINC](/methods/teno-thinc.md)).

**Results** (Rusanov splitting, Roe-averaged characteristic decomposition, SSP-RK3 at CFL 0.4, the
symmetry-preserving implementation of Fleischmann et al.; §4). ADR on 128 points: dispersion and
dissipation better than TENO5 and WENO5-Z, with the background linear scheme restored "up to an
intermediate wavenumber" (Fig. 3; [approximate dispersion relation](/definitions/approximate-dispersion-relation.md)).
Fifth order in $L_\infty$ on a Gaussian pulse (Fig. 4; grid sequence only in the figure). Sharper Sod and
Lax solutions at 100 points, better shocklets on [Shu–Osher](/benchmarks/shu-osher-problem.md) at 200,
more slip-line structure on [double Mach reflection](/benchmarks/double-mach-reflection.md) at
$400\times100$ than WENO5-Z and TENO5 at $1000\times250$, and more small-scale structure on
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md),
[Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md) and three
[2-D Riemann configurations](/benchmarks/two-dimensional-riemann-problems.md) (3, 8, 11 at $800^2$),
all by visual comparison except the kinetic-energy histories and spectra (Figs. 5–16). On the
[interacting blast waves](/benchmarks/woodward-colella-blast-wave.md) (400 points, Roe flux with entropy
fix) TENO5 needs $C_T=10^{-4}$ to run stably, while the present scheme keeps one parameter set "without
the necessity of parameter tuning case by case" (§4.3, §5). Wall time on double Mach reflection is
55.23 s against 40.04 s (TENO5) and 36.51 s (WENO5-Z) at $400\times100$, and 895.52 s against
630.89 s and 593.16 s at $1000\times250$, which the authors call "not significant" (Table 1;
hardware not stated). *(Compiler check, not in the sources: the ratios are 1.38 and 1.42 against TENO5, 1.51 against
WENO5-Z.)*

## Qualifications

- Liang & Fu (2024a) fix $\lambda_0$, $\lambda_\Delta$ in the units of $x$: $\lambda_{\mathrm s}$ multiplies physical
  distance and enters the fluxes only as $\lambda_{\mathrm s}^2\Delta x^2$, so the size of the correction
  depends on the length unit and on $\Delta x$. *(Compiler check, not in the sources: with
  $\lambda_{\mathrm s}\in[3,6]$, $\lambda_{\mathrm s}\Delta x\in[0.03,0.06]$ on Sod with $\Delta x=0.01$ but
  $[0.15,0.3]$ on Shu–Osher with $\Delta x=0.05$.)* This is the lack of scale invariance of RBF spaces that
  Jeong et al. point out (Remark 2.1; [scale invariance](/properties/scale-invariance.md)); Liang & Fu do not
  discuss it. They state that as $\Delta x\to0$ the scheme "will degenerate to the classical polynomial
  reconstruction" (§3.2).
- Liang & Fu write the six flag patterns as products ("$\delta_1\delta_2=0$, $\delta_0=1$") that must mean
  "$\delta_1=\delta_2=0$", and number the patterns ($\hat f^n$) and the fluxes of Eq. (25) ($R'_n$) in
  different orders for the two four-point stencils; the mapping is fixed only by the stencils of Fig. 2.
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
- [Liang & Fu (2024a)](/sources/liang-2024.md) — §1; §3.1, Fig. 2; §3.2, Eqs. (16)–(32), Fig. 3; §3.3, Eqs. (33)–(36); §4, Figs. 4–16, Table 1; §5.

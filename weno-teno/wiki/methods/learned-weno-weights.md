---
type: Method
title: "Learned WENO weights"
description: "Learned WENO weights replace the smoothness-indicator formula of a WENO-type scheme by a trained network that outputs the nonlinear weights; the page describes WENO3-NN, the five-point WENO5-NN, WCNS3-MR-NN, the constrained DSP-WENO, learned MUSCL slopes and scheme selection, the ROUND operators fitted to WENO3-NN, and a learned DG smoothness indicator."
status: established
aliases: [WENO3-NN, WENO3-NN1, WENO3-NN2, WENO5-NN, WCNS3-MR-NN, DSP-WENO, learned MUSCL slopes, learned discretization, neural-network WENO, data-driven WENO weights, machine-learned reconstruction, data-driven shock capturing]
tags: [machine-learning, weno, reconstruction, finite-volume, finite-difference]
timestamp: 2026-10-23T20:37:00Z
---

# Learned WENO weights

A **learned WENO scheme** keeps the WENO structure, a convex combination of
candidate reconstructions, but obtains the nonlinear weights from a trained
network instead of from smoothness indicators. The bundle's example is
**WENO3-NN** of [Bezgin, Schmidt & Adams (2022)](/sources/bezgin-2022.md),
retrained and analysed by [Huang et al. (2026)](/sources/huang-2026.md) (§§3.2–3.4);
[Fu (2023)](/sources/fu-2023.md) (§3.10) lists it among the TENO-related schemes
because its weighting includes a TENO-style cut-off "to guarantee max order and
the ENO property", and reports results similar to or better than WENO5-JS in 1D
and 2D (as recalled). Bezgin et al. (§3.2, Eqs. (12)–(13)) state the premise:
any map $\mathbb R^3\to\mathbb R^2$ whose outputs lie in $[0,1]$ and sum to one is
a third-order WENO-type weighting function, and a network with a softmax output
is such a map.

## WENO3-NN

On the compact stencil $\{I_{i-1},I_i,I_{i+1}\}$ the third-order WENO
reconstruction is $u^-_{i+1/2}=\omega_0\,\mathrm{UW2}+\omega_1\,\mathrm{CD2}$
with UW2 $=\tfrac32\bar u_i-\tfrac12\bar u_{i-1}$, CD2 $=\tfrac12(\bar u_i+\bar u_{i+1})$
and linear weights $d_0=1/3$, $d_1=2/3$ (see
[normalised-variable diagram](/definitions/normalised-variable-diagram.md);
Bezgin et al. 2022, §2, Eqs. (6)–(10), with the Jiang–Shu WENO3 as baseline).
WENO3-NN produces $(\omega_0,\omega_1)$ from $(\bar u_{i-1},\bar u_i,\bar u_{i+1})$
(Bezgin et al. 2022, §3.2, Fig. 1, Eqs. (11)–(22); Huang et al. 2026, §3.2,
Eqs. (3.8)–(3.13), Fig. 1):

- **Input ("Delta") layer.** Features
  $\lvert\bar u_i-\bar u_{i-1}\rvert$, $\lvert\bar u_{i+1}-\bar u_i\rvert$,
  $\lvert\bar u_{i+1}-\bar u_{i-1}\rvert$,
  $\lvert\bar u_{i+1}-2\bar u_i+\bar u_{i-1}\rvert$, each divided by the maximum of
  the first two and $\epsilon=10^{-15}$ (Bezgin et al., Eqs. (14)–(15)), described
  as "normalized amplitudes of first and second-order derivatives". Both papers call
  the result "Galilean invariance"; it is invariance under adding a constant to the
  data, not under a change of inertial frame. *(Compiler check, not in the sources:
  the features are differences normalized by a difference, hence invariant under
  adding a constant and, up to $\epsilon$, under scaling; they depend only on the
  ratio of the two one-sided differences, so the weights are functions of the
  normalised cell average alone, see the
  [normalised-variable diagram](/definitions/normalised-variable-diagram.md).)*
- **Body.** Three hidden layers of 16 nodes with swish activations, softmax output
  of two weights (Bezgin et al., §3.2); 658 trainable parameters (Huang et al.).
- **ENO layer.** $\tilde\omega_k=\omega_k\psi_k/\sum_j\omega_j\psi_j$ with
  $\psi_k=0$ when $\omega_k<c_{\mathrm{eno}}=2\times10^{-4}$, else 1 (page-local
  $\psi_k$, $c_{\mathrm{eno}}$): a sharp cut-off on the weights, analogous to
  TENO's cut-off on the scale-separated measure ([targeted ENO](/methods/targeted-eno.md)),
  applied at test time only (Bezgin et al., Eq. (16)). The softmax saturates and
  cannot return an essentially zero weight; without the layer the trained network
  gives the discontinuous stencil of a single jump a weight of about $10^{-4}$,
  hence the threshold, and the scheme reconstructs negative densities or pressures
  in the interacting blast waves (App. A.4, Eq. (A.1), Fig. 21;
  [ENO property](/definitions/eno-property.md)). The layer acts only near
  discontinuities (A.4).
- **Loss.** $\mathcal L=\mathcal L_r+b_d\,\mathcal L_d+b_W\lVert\Theta\rVert^2$
  (page-local weights $b_d$, $b_W$; $\Theta$ the network parameters), where the
  reconstruction loss $\mathcal L_r$ penalizes the face-value error weighted by
  $\varsigma^{p_s}$ and the ideal-weight loss $\mathcal L_d$ penalizes
  $\omega_k-d_k$ weighted by $1-\varsigma^{p_s}$, with the well-resolvedness
  indicator
  $\varsigma=\dfrac{\lvert\bar u_{i-1}-2\bar u_i+\bar u_{i+1}\rvert}{\lvert\bar u_i-\bar u_{i-1}\rvert+\lvert\bar u_{i+1}-\bar u_i\rvert+10^{-15}}\in[0,1]$
  (page-local $\varsigma$, $p_s$; 0 for linear data, 1 at discontinuities;
  Bezgin et al., Eqs. (17)–(22), who derive $\varsigma$ from the ratio of the
  second- to the first-order Taylor term). $p_s=0$ penalizes the reconstruction
  only; $p_s\to\infty$ would recover the linear scheme. $b_W=10^{-9}$. *(Compiler
  check, not in the sources: $\varsigma=1$ at every discrete extremum of the
  averages, smooth or not, which is where the weights are seen to degenerate.)*
- **Variants.** Bezgin et al. (§3.4, A.3, Table 3) keep WENO3-NN1 ($p_s=0.1$,
  $b_d=0.1$) and WENO3-NN2 ($p_s=0.03$, $b_d=0.1$), chosen from a grid of
  $p_s\in\{0,0.01,0.03,0.1,0.3,1\}$, $b_d\in\{0.01,0.1,1\}$; a smaller $p_s$ lets the
  weights deviate further from $d_k$, a larger $b_d$ pulls them back. Huang et al.
  retrain with the NN1 values, note that the choices are not optimal and that the
  network may be over-parameterized (a rational variant uses 105 parameters).
- **Training data** (Bezgin et al., §3.3, Table 1, A.1–A.2; Huang et al., §3.3,
  Table 1): random cubic polynomials, jumps, sawtooth, $\sin(k\pi x)$ with
  $k\in[2,20]$ and $\tanh(kx)$ with $k\in[5,30]$, sampled at $\Delta x=0.01$; Adam,
  100 epochs, learning rate $10^{-3}$, mini-batch 100. Jumps are placed on faces only,
  because on three cell averages a jump inside a cell is indistinguishable from a
  linear function and a jump at a face from a sine extremum; five random seeds per
  model, and the model kept is the one with the lowest validation error among those
  that pass all 1-D benchmarks.

## WENO5-NN (Nogueira et al. 2024)

Nogueira, Fernández-Fidalgo, Ramos, Couceiro & Ramírez (2024) extend the WENO3-NN methodology to the five-point
stencil of finite-difference WENO5-JS ([WENO-JS](/methods/weno-js-reconstruction.md)): the three candidate fluxes
and the linear weights $(d_0,d_1,d_2)=(0.1,0.6,0.3)$ are kept, and a network returns $(\omega_0,\omega_1,\omega_2)$
directly (Abstract; §2, Eqs. (5)–(10); §3). This WENO5-NN is not the WENO5-NN of Stevens & Colonius recalled below,
which perturbs the WENO5-JS coefficients and whose post-processing "results in a reduction in the overall accuracy
of the method to first-order", in Nogueira et al.'s description (§1).

- **Inputs.** Four features (§3.1, Eqs. (12)–(14)): the absolute-value analogues of the Jiang–Shu indicators,
  page-local $\beta^{\mathrm{abs}}_k$, e.g.
  $\beta^{\mathrm{abs}}_0=\tfrac{13}{12}|f_{i-2}-2f_{i-1}+f_i|+\tfrac14|f_{i-2}-4f_{i-1}+3f_i|$, each divided by the
  largest of the three, and the five-point maximum $\varsigma^{\mathrm s}=\max_k\varsigma_k$ of three-point ratios of
  the form of $\varsigma$ above, $\varsigma_k=|f_{j-1}-2f_j+f_{j+1}|/(|f_j-f_{j-1}|+|f_{j+1}-f_j|+10^{-15})$ centred
  on the three nodes $j=i-1,i,i+1$, which the authors call a five-point extension of Jameson's shock detector
  (page-local $\varsigma_k$, $\varsigma^{\mathrm s}$; the source's $\delta_k$, $\gamma_i$, $\gamma^s$). Squared
  indicators as inputs trained less accurately, and adding $\varsigma^{\mathrm s}$ improved the results
  "considerably" (stated, no data; [smoothness indicators](/definitions/smoothness-indicator.md)).
- **Body.** Dense layers of 32, 16 and 16 neurons with swish activations, three outputs (Eq. (11), Fig. 2); the
  output activation is not stated.
- **ENO layer and plateau bypass.** Weights at or below $4\times10^{-7}$ are zeroed and the rest renormalized, at
  inference only (Eq. (15); [ENO property](/definitions/eno-property.md)). Because the max-normalization turns
  machine-zero data such as $(10^{-16},10^{-15},10^{-16})$ into $(0.1,1,0.1)$, a curvature-based plateau detector
  after Clain, Loubère & Machado sets $\omega_k=d_k$ in flat regions and skips the network there; its formula and
  threshold are not given (§3.1).
- **Loss.** A loss of the WENO3-NN type, "after" Bezgin et al.: the reconstruction error weighted by
  $(\varsigma^{\mathrm s})^{p_s}$ and the ideal-weight deviation $\sum_k(\omega_k-d_k)^2$ weighted by
  $(1-\varsigma^{\mathrm s})^{p_s}$, as printed (WENO3-NN weights it by $1-\varsigma^{p_s}$), plus a regularization
  with $b_W=10^{-9}$ (Eqs. (16)–(17)). Fig. 5 maps the pair of hyperparameters the
  paper calls "$\alpha$ and $\beta$" ($\alpha$ is the exponent $p_s$; the paper does not say which coefficient
  $\beta$ is), over $(0.2,0.1)$, $(0.5,0.1)$, $(0.05,0.1)$, $(0.2,0.25)$, $(0.2,0.05)$: similar
  dispersion, different high-wavenumber dissipation, "a family of schemes"; $(0.2,0.1)$ is kept (§3.3).
- **Training** (§3.2, Tables 1–2): static functions only, sampled at $\Delta x=0.01$, with wider ranges than
  WENO3-NN ("necessary" for strong shocks and for dispersion): 655861 jumps with states in $\mathcal U(-40,80)$,
  460355 samples of $\sin(k\pi x)$, $k\in[2,27]$, 72135 sawtooth, 82837 $\tanh(kx)$, $k\in[5,30]$, and 52700 cubic,
  63935 quadratic, 2893 linear and 393 constant samples, with outliers removed by ranges of $\varsigma^{\mathrm s}$;
  Nadam at learning rate $10^{-3}$, mini-batches of 128, 1000 epochs, five repetitions, the network kept being the
  best on the 1-D tests.

**Results** (characteristic-wise global Lax–Friedrichs splitting, explicit third-order Runge–Kutta, §4). On the
2-D entropy wave ([density-wave advection](/benchmarks/density-wave-advection.md), $25^2$ to $400^2$) the $L_2$
density errors of WENO5-NN are $8.47\times10^{-2}$ to $1.59\times10^{-7}$ with orders 4.16, 5.12, 5.06, 4.68,
against $1.16\times10^{-1}$ to $7.88\times10^{-7}$ and 2.80, 4.46, 4.90, 5.00 for WENO5-JS: four to six times
smaller errors, but the order "seems to start to drop below 5 at the finest grid", as for WENO3-NN (Table 3). In
the approximate dispersion relation the chosen network has less dispersion error than WENO5-JS over a wide range
and less dissipation in the well-resolved range (Fig. 5;
[approximate dispersion relation](/definitions/approximate-dispersion-relation.md)). It is less dissipative than
WENO5-JS and stable on the Sod, Lax, [123](/benchmarks/double-rarefaction-problem.md) and
[Leblanc](/benchmarks/leblanc-shock-tube.md) tubes (where it "greatly reduces the overshoots" of WENO5-JS at 900
points), the [Shu–Osher problem](/benchmarks/shu-osher-problem.md) (200 points, with a slight phase error),
2-D Riemann configurations 3 and 6, [double Mach reflection](/benchmarks/double-mach-reflection.md) ($960\times240$),
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) ($128\times512$, with a "slight loss of symmetry")
and the [Mach 3 step](/benchmarks/forward-facing-step.md) (§4.2–4.4, figure comparisons). The cost is "several
times" that of WENO5-JS, unmeasured; the authors present the network as a tool for discovering analytical weight
functions rather than as a production scheme (§3.1, §5).

## WCNS3-MR-NN (Fan et al. 2025b)

[Fan et al. (2025b)](/sources/fan-2025-b.md) attribute the accuracy loss of earlier learned schemes
(Stevens & Colonius' network, WENO3-NN, the WENO5-NN of Nogueira et al. and a data-driven WCNS3) to the
requirement that the network predict, for *every* lower-order candidate, weights close to the linear
ones; at fine scales small deviations then contaminate the accuracy (§1). They move the problem into the
third-order [weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md) with the
multi-resolution weighting of Zhu & Shu in the modified form of Qin et al.
([multi-resolution WENO](/methods/multi-resolution-weno.md)), on point values of a staggered
finite-difference grid:

- **A target at one corner.** With nested candidates, the one-point value $u^{(1)}=u_i$ and the
  three-point value $u^{(2)}=-\tfrac18u_{i-1}+\tfrac34u_i+\tfrac38u_{i+1}$, the multi-resolution combination
  of the hierarchical polynomials is rewritten as a combination $\omega_1u^{(1)}+\omega_2u^{(2)}$ of the
  candidates themselves (the "MR-q" form, Eqs. (19)–(20)), whose optimal weights are $(0,1)$. Third order
  then holds iff $\omega_1=O(\Delta x^2)$ and $\omega_2=O(1)$ (Eqs. (29)–(30)). With a softmax output
  $\omega_1=(1+e^{\delta_{\mathrm{sm}}})^{-1}$ ($\delta_{\mathrm{sm}}$ the logit difference, page-local), a
  tolerance $\lvert\omega_1-d_1\rvert\le\epsilon_{\mathrm a}$ is an interval of width $O(\epsilon_{\mathrm a})$
  around $\ln3$ for the Jiang–Shu target $d_1=\tfrac14$ and around $\ln10$ for the original
  multi-resolution form ($d_1=\tfrac1{11}$), but the half-line $\delta_{\mathrm{sm}}\ge\ln(1/\epsilon_{\mathrm a}-1)$ for the
  MR-q target $d_1=0$; e.g. $\delta_{\mathrm{sm}}\ge13.82$ for $\epsilon_{\mathrm a}=10^{-6}$ (App. A, Eqs. (A.4)–(A.6),
  Table A.6). *(Compiler check, not in the sources: for $\epsilon_{\mathrm a}=10^{-2}$ the Jiang–Shu interval is
  $[\ln(1/0.26-1),\ln(1/0.24-1)]=[\ln3-0.0527,\ln3+0.0541]$ and the MR-q bound $\ln99=4.595$, as tabulated.)*
  Only the MR-q form keeps optimal $L^\infty$ accuracy in their advection test (Fig. A.19).
- **Features.** The four normalized differences of WENO3-NN (Delta layer) plus a **scale-variant**
  feature $\log_{10}\Delta_{\max}$, $\Delta_{\max}$ the largest one-sided difference, because on three points
  a smooth extremum and a jump give essentially the same normalized data, while $\Delta_{\max}$ shrinks
  under refinement only at the extremum (§3.1.1, Eqs. (24)–(26), Fig. 4;
  [scale invariance](/properties/scale-invariance.md)).
- **Network and safety layer.** Three hidden layers of 16 swish nodes with layer normalization and a
  softmax output (a single layer of 8 nodes gives similar results, Remark 4); at inference a hard cut-off
  at $C_T=2\times10^{-4}$, taken from WENO3-NN, with renormalization (§3.1.2–3.1.3, Eqs. (27)–(31)).
- **Loss and training.** An $L^1$ distance to low-dissipation multi-resolution weights (base $30$,
  amplifying parameter $1$) plus $1.2$ times a scale-weighted $L^1$ distance to high-dissipation ones
  (base $10$, amplifying parameter $50$), switched off at large $\Delta_{\max}$ by the factor
  $1-\tanh(2\Delta_{\max})$, plus an $L^2$ weight penalty $10^{-5}$ (§3.1.4, Eqs. (32)–(35)). Six function
  families, 4000 samples each, rescaled by $10^a/\Delta_{\max}$ with $a\sim\mathcal U(-4,4)$; Adam, learning rate
  $10^{-4}$, batches of 500, 100 epochs (§3.2, Table 1, Eq. (36)).

**Results** (characteristic-wise interpolation, Roe flux, SSP-RK3 at CFL 0.5; §4). On linear advection of
$10^{-3}\sin(2\pi x)$ the order is 3.00 from $N=80$ to $5120$ in all three norms ($L^1$ error
$8.28\times10^{-6}$ at $N=20$, $6.29\times10^{-14}$ at $N=10240$, Table 3), and on the 1D Euler density wave
third order to $N=10240$ (Table 4; [density-wave advection](/benchmarks/density-wave-advection.md)). Two
re-implementations inside the same WCNS with the WENO3-NN network, with Jiang–Shu weighting (WCNS3-NN1) and
with multi-resolution weighting (WCNS3-NN2), reach about second order in $L^1$, $L^2$ and first order in
$L^\infty$ (Figs. 6–7). On Lax, Sod, Woodward–Colella and 2D Riemann configurations 3 and 5 the resolution
is comparable to the fifth-order WCNS5-JS in several cases, better than WCNS3-JS and WCNS3-MR throughout
(§§4.3–4.4), and its approximate dispersion relation shows lower dissipation than both
([approximate dispersion relation](/definitions/approximate-dispersion-relation.md)). Wall-clock times
are close to those of WCNS3-MR, e.g. $2800.06$ against $2808.29$ s on Riemann configuration 5 at
$400\times400$ (Table 5, Intel i5-13600KF CPU with an RTX 4070 Ti GPU; where the network runs is not
stated).

## DSP-WENO: learned weights inside a feasible region (Charles & Ray 2025)

[Charles & Ray (2025)](/sources/charles-2025.md) (§4, arXiv v2) learn the two weight perturbations of the
third-order sign-preserving WENO used in entropy-stable [TeCNO](/methods/tecno-scheme.md) fluxes, but impose the
constraints **strongly** ([sign-preserving WENO](/methods/sign-preserving-weno.md)). For each four-point
stencil a hand-derived vertex algorithm builds the convex polygon of perturbations that satisfy
consistency, the sign property and third-order accuracy (at most five vertices, six cases of the jump
ratios); a small network (three hidden layers of 5 ReLU neurons, softmax output, 120 parameters) outputs
five convex weights, and the perturbation is their combination of the vertices, so every output satisfies
the constraints by construction (§4.1, Eqs. (24)–(30), Algorithm SM1). The inputs are the two jump ratios
(through $\tanh$) and three scaled absolute jumps. Training uses interface values of synthetic smooth and
piecewise-linear functions only (100 000 samples, $\Delta x=1/40,1/100,1/200$; §4.2–4.3), and one network
serves advection, Burgers and 1D/2D Euler (§6). The authors prefer this to a weak, penalty-type imposition,
which "cannot guarantee" the sign property and hence entropy stability (§6).

**Results.** Third-order convergence on smooth advection and the isentropic vortex, where ENO3 loses order;
larger errors than the unconstrained sign-preserving schemes on smooth data, being more dissipative; far
smaller overshoots than those schemes at shocks (Burgers, Sod-type, Shu–Osher, Lax, 2D Riemann,
Kelvin–Helmholtz); reconstruction about five times as costly as SP-WENO, 95% of it in the vertex search (§5,
Tables 2–4, Fig. 3). The scheme is not positivity preserving (Remark 5). Details and the comparison with
ENO and SP-WENO are on [sign-preserving WENO](/methods/sign-preserving-weno.md).

## Learned MUSCL slopes (de Romémont et al. 2026)

[de Romémont et al. (2026)](/sources/deromemont-2026.md) learn not weights but stencil coefficients. A
convolutional network applied to the min–max-normalized primitive variables outputs, for every cell,
variable and direction, three coefficients with zero sum (imposed by a final linear layer) that define a
learned slope $\sum_{j=-1}^1\mathsf a_ju_{i+j}/\Delta x$ (page-local $\mathsf a_j$); the slope replaces the
finite-difference slope of a second-order MUSCL finite-volume scheme whose van Albada limiter is kept, now
applied to the ratio of learned slopes, with the Rusanov flux and explicit Euler steps (§3.1, §4.1–4.2,
Eqs. (12)–(17)). Training is supervised against fine solutions sub-sampled by a factor 2, with $L^1$ and
$L^2$ losses plus soft penalties on a discrete entropy inequality, on total-variation increase and on the
$L^1$ norm of the network parameters, their coefficients tuned by Bayesian optimization (§4.4, Eqs.
(18)–(25), Table 2). Because the limited scheme is stable by itself, they train on single steps, without the
unrolled multi-step accumulation of earlier learned discretizations (§1, §4.4). Boundary conditions enter
through padding matched to the boundary type, the learned contribution being zeroed at slip walls, and a
slip-wall model is obtained by fine-tuning a periodic one (§4.3, §4.6). A linearized von Neumann analysis
with frozen coefficients gives less dissipation and dispersion than the centred slope (§5, Fig. 4).

**Results.** $L^1$ error reductions against the same scheme on the same coarse grid of 49.2% (Sod,
128 cells), 46% (Shu–Osher), 22%, 39%, 48% and 28% (four 2D Riemann problems at $512^2$), 6% (2D explosion)
and 19% (forward-facing step) (§6); no gain on a smooth advected sine, where the baseline scheme is
"slightly better" and both are second order (§7, Fig. 16); comparable time-to-error on one V100 GPU (§8,
Fig. 17).

## Learned scheme selection

[Huang et al. (2025b)](/sources/huang-2025-b.md) train a network to predict which of two candidate
reconstructions (MUSCL or THINC) the boundary-variation-diminishing rule would select, so that only one is
built per cell (deepMTBVD); the network chooses a scheme, not weights. It is described on
[boundary variation diminishing](/definitions/boundary-variation-diminishing.md).

## Order, dissipation and cost

**Order.** The ideal-weight loss is the point of the design. Earlier networks trained
on the reconstruction error alone "were not able to achieve full-order convergence"
(Bezgin et al., §3.2): the WENO5-NN of Stevens & Colonius needs post-processing of its
weights and drops to first order (§1, as recalled). On the face reconstruction of a
function (not a PDE solve), WENO3-NN converges at order 1.90 on $\tanh(2x)$ and 1.95 on
$\sin^3(\pi x)$ with $p_s=0$, and at 2.93 and 2.33 with $p_s=0.1$, against 3.00 and
2.44 for WENO3-JS and 3.01 and 2.40 for WENO3-Z (§3.4, Fig. 2; the text rounds the
latter to "$\mathcal O(2.5)$"). WENO3-JS and WENO3-Z degenerate at the saddle point of
$\sin^3(\pi x)$, which WENO3-NN "distinguish[es]", like WENO-F3+ (§3.5, Fig. 4;
[critical-point accuracy](/properties/critical-point-accuracy.md)).

**Errors.** With LLF fluxes, characteristic reconstruction, TVD-RK3 at CFL 0.6, WENO3-NN
beats WENO3-JS, WENO3-Z and WENO3-N on every test (Bezgin et al., §§4.1–4.7). The
$L_1$ errors of Table 4 (A.6) qualify the comparison with fifth order: on $\sin^3$
advection WENO3-NN2 has $2.445\times10^{-2}$ against $2.572\times10^{-3}$ for WENO5-JS
(and $1.180\times10^{-1}$ for WENO3-JS), on the Gaussian–square–triangle–ellipse
advection $1.609\times10^{-1}$ against $9.964\times10^{-2}$; on the Sod, Lax and
[double-rarefaction](/benchmarks/double-rarefaction-problem.md) tubes it is below
WENO5-JS ($1.035\times10^{-2}$, $2.416\times10^{-2}$, $1.967\times10^{-2}$ against
$1.106\times10^{-2}$, $2.590\times10^{-2}$, $2.393\times10^{-2}$). At $N=400$ it
matches WENO3-JS at $N=800$ on the
[interacting blast waves](/benchmarks/woodward-colella-blast-wave.md) and the
[Shu–Osher problem](/benchmarks/shu-osher-problem.md); it keeps a Gresho vortex at
$M_0=0.01$ that WENO3-JS/Z deform, and resolves finer structures in
[double Mach reflection](/benchmarks/double-mach-reflection.md) and
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md), with a slightly stronger
post-shock instability behind the incident shock (Figs. 11–16).

**Dissipation.** In Pirozzoli's approximate dispersion relation WENO3-NN2 is less
dissipative than WENO3-JS over the whole range and slightly less than WENO5-JS at high
wavenumbers; WENO3-NN1 has zero dissipation at the cut-off wavenumber, which the
authors read as under-resolved wave packets kept "akin to soliton solutions" and call
"counterintuitive to classical discretization-design principles" (§4.8, Fig. 17;
[approximate dispersion relation](/definitions/approximate-dispersion-relation.md)).

**Cost.** Bezgin et al. (§4.9, Table 2) time JAX on a GPU on double Mach reflection
($1024\times256$, 3700 steps): 1676 and 1743 ns per cell and step for NN1 and NN2,
4.31 and 4.48 times WENO3-JS (389 ns) and about 3 times WENO5-JS (561 ns), with the
networks "not optimized". Huang et al. (Table 2) count FLOPs per reconstruction,
counted with JAX after Bezgin et al.: WENO3-NN 2139, Rational-WENO3-NN 508,
WENO5-JS 55, WENO3-JS 19, LD-ROUND 20, ROUND 11. The two measures differ by more
than an order of magnitude in the ratio to WENO3-JS (4.3 in time against about 113
in FLOPs *(compiler check, not in the sources: $2139/19\approx112.6$)*); time on a GPU is not
proportional to FLOPs.

## What the normalised-variable diagram shows

Sampling the trained network with $\bar u_{i-1}=0$, $\bar u_{i+1}=1$ and
$\bar u_i$ in steps of 0.02, on the *assumption* that it is scale independent,
Huang et al. (§3.4, Fig. 2) find that WENO3-NN behaves like classical WENO3 on
$0\le\tilde u_i\le1$: UW2 near 0, the third-order line P3 near $1/2$, CD2 near 1,
below the line $2.5\tilde u_i$ (convection-bounded for CFL $\le0.4$). Its
distinguishing feature is at $\tilde u_i<0$, i.e. a critical point inside cell
$i$: there it leaves UW2 and tends toward CD2 as $\tilde u_i$ decreases. The
authors attribute this to the loss balance: for less smooth data the
reconstruction loss dominates the ideal-weight loss and drives the network
toward the face-value-optimal central operator, which they credit for the
network's lower dissipation (a qualitative argument, §3.4). Bezgin et al. (§3.5,
Fig. 3) see the same tendency in physical space: on a piecewise sine with a jump
both variants follow $d_0=1/3$ over most of the domain and degenerate to
$\omega_0=0$ or 1 only at the extrema and the jump.

## From the network to closed form

Huang et al. (§4) then design closed-form operators on the diagram that keep
these features: a piecewise-linear ROUND that takes *more* central contribution
than WENO3-NN for $\tilde u_i<0$ (switching to CD2 below $\tilde u_i=-1.15$), and
LD-ROUND with controlled anti-dissipation on $(0,1)$; see
[ROUND schemes](/methods/round-scheme.md). The method, learning the diagram shape
from a network and then fitting a closed form, is claimed applicable to
Rational-WENO3-NN and WCNS3-MR-NN (§7).

On sine advection to $t=20$ (Table 3) ROUND and LD-ROUND have smaller $L_1$ errors
than WENO3-NN at 23–31% of its CPU time (hardware not stated): e.g. at
$N_x=1280$, $L_1=8.37\times10^{-6}$ (WENO3-NN, 37.0 s), $6.05\times10^{-6}$
(ROUND, 8.5 s), $3.21\times10^{-6}$ (LD-ROUND, 11.3 s). On the Shu–Osher problem
with 400 cells WENO3-NN is "significantly smeared out" relative to both
closed-form schemes (§6.4).

## A learned smoothness indicator for DG

Yu & Hesthaven (2022) apply the same idea one level down, to the indicator rather
than the weights: a feedforward network replaces the least-squares estimate of the
modal decay rate of a nodal DG element, which then sets a Laplacian artificial
viscosity ([artificial viscosity](/methods/artificial-viscosity.md),
[smoothness indicators](/definitions/smoothness-indicator.md),
[troubled-cell indicators](/definitions/troubled-cell-indicator.md)).

- **Network.** 11 inputs (the element solution divided by its largest nodal
  magnitude and resampled at 11 equispaced points), three hidden ReLU layers of
  32, 16 and 8 neurons, one output, 1057 parameters; Adam at learning rate
  $10^{-4}$, mean-squared error plus a size-normalized weight penalty, best of 20
  trainings (§3, §4.1.2).
- **Labels.** Jumps get decay rate 1, kinks 2, and constants, noisy constants,
  linear and trigonometric functions 4 (Table 1). Since the viscosity is full below
  rate 1 and zero above 3, outputs outside $[1,3]$ are clipped without loss; the
  authors call this compactness of input and output "critical to the success of
  training the network" (Abstract; §4.1.1).
- **2-D.** The 1-D network runs on each edge of a triangle and the edge rates are
  combined, by the minimum or by discarding the largest and averaging the rest
  (Eqs. (4.8)–(4.9)).

The network rates jumps near 1 and smooth zones above 3 more reliably than the
averaged least-squares estimate, which over-dissipates constant regions below
degree 4 (§4.1.3, Fig. 4); on smooth convergence tests it fires only on the
coarsest grids and the errors then equal those of the inviscid scheme (Tables 2–3).
It stabilizes shock tubes, 2-D Riemann problems, Sedov, double Mach reflection and
an unstructured forward-facing step, but the degree-2 scheme fails on the
[astrophysical jet](/benchmarks/high-mach-astrophysical-jet.md), for lack of smoothness
information in low-degree polynomials (§5.4.6). *(Compiler check, not in the sources:
division by the largest nodal magnitude makes the input invariant under scaling but
not under adding a constant, unlike the WENO3-NN features.)*

## Qualifications

- **Two schemes named WENO5-NN.** Nogueira et al. (2024) and Stevens & Colonius (recalled by Bezgin et al. 2022, §1,
  and Nogueira et al., §1) use the same name for different constructions: direct regression of the weights with an ENO
  layer, against a perturbation of the WENO5-JS coefficients with post-processing.
- Nogueira et al. (2024, §3.2) call the third loss term a regularization "on the neural network weights", while
  Eq. (17) prints it as $\omega_0^2+\omega_1^2+\omega_2^2$, the squared output weights; the hyperparameters of Fig. 5
  are called "$\alpha$ and $\beta$" without saying which coefficient $\beta$ is. Their outlier table lists the
  oscillatory functions, which the text omits. Their evidence of lower dissipation on double Mach reflection and the
  Riemann problems is the appearance of small structures, which the paper itself cites as possibly non-physical.

- The diagram of a non-normalisable scheme is one section through its weights; Huang
  et al. do not verify the scale-independence assumption used to sample WENO3-NN.
  Bezgin et al.'s Delta layer makes it hold by construction up to $\epsilon$ (see the
  compiler check above).
- None of the three compact schemes of Huang et al. reaches observed third order on
  smooth data: $L_1$ orders 2.4–2.6, $L_\infty$ orders 1.6–1.7 (Table 3); the paper
  does not discuss this. Bezgin et al.'s reconstruction orders on $\sin^3(\pi x)$
  (2.33 to 2.44 for WENO3-NN, -JS and -Z alike) show the same critical-point limit;
  the "maximum-order" of their title refers to recovering third order on functions
  without critical points.
- Bezgin et al.'s abstract claims performance "similar to or better than the classical
  WENO5-JS scheme"; their Table 4 supports it for the shock tubes only, and §4.1 itself
  says WENO3-NN does not reach WENO5-JS/Z "for functions with a local maximum".
- Bezgin et al. describe the Stevens–Colonius network once as reduced to first order
  and once as needing "a rescaling of the network output in order to guarantee
  convergence" (§1, §5). Their conclusion calls the new loss term one "on the network
  weights"; it acts on the reconstruction weights, and the term on the network weights
  is the $b_W$ regularization.
- Bezgin et al. state that the ENO layer "can be easily implemented via a ReLU",
  $\tilde\omega_k=\mathrm{ReLU}(\omega_k-c_{\mathrm{eno}})/\sum_j\mathrm{ReLU}(\omega_j-c_{\mathrm{eno}})$
  (Eq. (A.3)). *(Compiler check, not in the sources: this subtracts $c_{\mathrm{eno}}$
  from the surviving weights too, so $(0.4,0.6)$ becomes $(0.39996,0.60004)$ instead
  of staying unchanged; the difference is negligible but the forms are not
  equivalent.)*
- **Fan et al. (2025b) and WENO3-NN.** The second-order behaviour of WCNS3-NN1 and WCNS3-NN2 concerns
  WCNS re-implementations of the WENO3-NN network on point values, not the finite-volume WENO3-NN of Bezgin et
  al., whose own tests are recorded above; the two results are not about the same scheme and are not recorded
  as a contradiction. Fan et al.'s general statement that WENO3-NN-type networks lose accuracy under refinement
  (§1) is shown only for these re-implementations.
- Fan et al. (2025b) state that Remark 3's weights are convex, $\omega_k\ge0$. *(Compiler check, not in the
  sources: the MR-q weights of the multi-resolution scheme used as training targets are
  $\omega_1=\omega^{\mathrm p}_1-\omega^{\mathrm p}_2d^{\mathrm{MR}}_1/d^{\mathrm{MR}}_2$, which is negative for example for
  $\omega^{\mathrm p}=(0.05,0.95)$ and $d^{\mathrm{MR}}=(\tfrac1{11},\tfrac{10}{11})$, below the range of a softmax.)* The paper
  does not discuss it. Its Table 1 lists $\tan(kx)$, $k\in\mathcal U(5,30)$, on $[-1,1]$ among the smooth
  training functions where the text says tanh, the family of the WENO3-NN training set above *(compiler check,
  not in the sources: $\tan(kx)$ has poles in $[-1,1]$ for $k\ge5$, since $\pi/(2k)\le0.32$)*; the text speaks of
  polynomials "up to degree three" where the table has degrees $0$ to $2$; and App. A writes the MR-q target as
  "$d_1=\gamma_1=0$" although the multi-resolution linear weight $\tfrac1{11}$ is not zero.
- Charles & Ray (2025, §5.2.1) write that the errors of DSP-WENO "are about an order of magnitude larger than
  those of SP-WENO and SP-WENOc" on smooth advection. Their Table 3 gives, at $N=1000$, $5.02\times10^{-8}$
  against $4.22\times10^{-8}$ (SP-WENO) on Test 1 and $1.66\times10^{-6}$ against $8.94\times10^{-7}$ on Test 2,
  factors of about 1.2 and 1.9; factors of about seven appear in their reconstruction-only Table 2
  ($1.22\times10^{-6}$ against $1.68\times10^{-7}$ at $N=1280$), where §5.1 makes the same statement, and on the
  isentropic vortex of Table 4 ($2.73\times10^{-4}$ against $3.57\times10^{-5}$ at $N=400$)
  *(compiler check, not in the sources)*.
- de Romémont et al. (2026) summarize their gains as "20–50%" (abstract, §1, §9), while their 2D explosion
  and forward-facing-step gains are 6% and 19% (§6.3). They state that the learned scheme "is not constrained
  by the temporal resolution of the training data, allowing users to freely select time steps"; their only
  time-step study (Sod, App. A, Table A.1, explicit Euler) gives gains of 49.1% at $\Delta t/\Delta x=0.01$
  (CFL 0.022), 33.8% at $0.1$, 16.3% at $0.15$ and $-20.8\%$, $-42.9\%$, $-56.8\%$, $-34.8\%$ at $0.2$ to
  $0.35$ (CFL 0.44 to 0.77), i.e. a worse error than the baseline MUSCL scheme there. Their §5 writes the CFL number as
  $a\Delta x/\Delta t$, the inverse of their Eqs. (14)–(15). The entropy and total-variation terms are soft
  training penalties; no discrete entropy inequality is proved for the scheme.
- Huang et al. state that ROUND needs "only 5% of the cost of WENO3-NN"; their
  Table 2 gives $11/2139\approx0.5\%$ in FLOPs.
- Yu & Hesthaven attribute a slight asymmetry of the viscosity on a Burgers test to the
  randomness of the training samples (§5.2): nothing in the inputs enforces reflection
  symmetry ([symmetry preservation](/properties/symmetry-preservation.md)). Their text
  calls Eq. (4.9) "the average of the largest two" edge rates; the printed formula
  averages the two smallest.

# Citations

- [Bezgin, Schmidt & Adams (2022)](/sources/bezgin-2022.md) — Abstract; §1; §2, Eqs. (6)–(10); §3.2, Eqs. (11)–(22), Fig. 1; §3.3, Table 1; §3.4, Fig. 2; §3.5, Figs. 3–4; §§4.1–4.9, Table 2, Figs. 5–17; §5; App. A.1–A.6, Eqs. (A.1)–(A.3), Tables 3–4, Figs. 20–21.
- [Huang et al. (2026)](/sources/huang-2026.md) — §§3.2–3.4, Eqs. (3.8)–(3.14), Table 1, Fig. 2; §4; §5.1, Table 2; §6.1, Table 3; §6.4; §7.
- [Fu (2023)](/sources/fu-2023.md) — §3.10: WENO3-NN among TENO-related schemes.
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — Abstract; §3, Eq. (3.4); §4.1–4.2, Eqs. (4.1)–(4.9), Table 1, Fig. 4; §5, Tables 2–3; §5.2; §5.4.6.
- [Nogueira et al. (2024)](/sources/nogueira-2024.md) — Abstract; §1; §2, Eqs. (5)–(10); §3.1–3.3, Eqs. (11)–(17), Tables 1–2, Figs. 2, 5; §3.4, Fig. 6; §4, Table 3, Figs. 8–22; §5.
- [Fan et al. (2025b)](/sources/fan-2025-b.md) — §1; §2.2; §3, Eqs. (19)–(36), Remarks 3–4, Table 1, Figs. 3–5; §4, Tables 3–5, Figs. 6–18; App. A, Eqs. (A.1)–(A.6), Table A.6, Fig. A.19: WCNS3-MR-NN.
- [Charles & Ray (2025)](/sources/charles-2025.md) — §1; §4, Eqs. (24)–(31), Algorithm SM1; §5, Tables 2–4, Fig. 3; §6; Remark 5: DSP-WENO, constrained learned weights (arXiv v2).
- [de Romémont et al. (2026)](/sources/deromemont-2026.md) — §1; §3.1; §§4.1–4.6, Eqs. (12)–(25), Tables 1–2; §5, Fig. 4; §§6–9, Figs. 6–17; App. A, Table A.1: learned MUSCL slope coefficients.
- [Huang et al. (2025b)](/sources/huang-2025-b.md) — §3.3: learned BVD selection (deepMTBVD).

---
type: Method
title: "Learned WENO weights"
description: "Learned WENO weights replace the smoothness-indicator formula of a WENO scheme by a trained neural network that outputs the nonlinear weights; this page describes WENO3-NN and the five-point WENO5-NN of Nogueira et al. (architecture, ENO layers, ideal-weight loss, training, order, dissipation, cost), the ROUND operators fitted to WENO3-NN, and a learned DG smoothness indicator."
status: established
aliases: [WENO3-NN, WENO3-NN1, WENO3-NN2, WENO5-NN, neural-network WENO, data-driven WENO weights, machine-learned reconstruction, data-driven shock capturing]
tags: [machine-learning, weno, reconstruction, finite-volume, finite-difference]
timestamp: 2026-10-23T05:41:00Z
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

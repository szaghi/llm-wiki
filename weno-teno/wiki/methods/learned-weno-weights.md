---
type: Method
title: "Learned WENO weights"
description: "Learned WENO weights replace the smoothness-indicator formula of a WENO scheme by a trained neural network that outputs the nonlinear weights; this page describes WENO3-NN (architecture, invariance layer, ENO cut-off layer, loss, training data), what its normalised-variable diagram reveals, its cost, and the closed-form ROUND operators fitted to it."
status: established
aliases: [WENO3-NN, neural-network WENO, data-driven WENO weights, machine-learned reconstruction]
tags: [machine-learning, weno, reconstruction, finite-volume]
timestamp: 2026-10-21T12:00:00Z
---

# Learned WENO weights

A **learned WENO scheme** keeps the WENO structure, a convex combination of
candidate reconstructions, but obtains the nonlinear weights from a trained
network instead of from smoothness indicators. The chunk-1 example is
**WENO3-NN** of Bezgin, Schmidt and Adams (2022), retrained and analysed by
[Huang et al. (2026)](/sources/huang-2026.md) (§§3.2–3.4); [Fu (2023)](/sources/fu-2023.md)
(§3.10) lists it among the TENO-related schemes because its weighting includes a
TENO-style cut-off "to guarantee max order and the ENO property", and reports
results similar to or better than WENO5-JS in 1D and 2D (as recalled).

## WENO3-NN

On the compact stencil $\{I_{i-1},I_i,I_{i+1}\}$ the third-order WENO
reconstruction is $u^-_{i+1/2}=\omega_0\,\mathrm{UW2}+\omega_1\,\mathrm{CD2}$
with UW2 $=\tfrac32\bar u_i-\tfrac12\bar u_{i-1}$, CD2 $=\tfrac12(\bar u_i+\bar u_{i+1})$
and linear weights $d_0=1/3$, $d_1=2/3$ (see
[normalised-variable diagram](/definitions/normalised-variable-diagram.md)).
WENO3-NN produces $(\omega_0,\omega_1)$ from $(\bar u_{i-1},\bar u_i,\bar u_{i+1})$
([Huang et al. (2026)](/sources/huang-2026.md), §3.2, Eqs. (3.8)–(3.13), Fig. 1):

- **Input ("Delta") layer.** Features
  $\lvert\bar u_i-\bar u_{i-1}\rvert$, $\lvert\bar u_{i+1}-\bar u_i\rvert$,
  $\lvert\bar u_{i+1}-\bar u_{i-1}\rvert$,
  $\lvert\bar u_{i+1}-2\bar u_i+\bar u_{i-1}\rvert$, each divided by the maximum of
  the first two and $\epsilon$. The paper calls this "Galilean invariance";
  *(compiler check, not in the sources: the printed features are differences
  normalized by a difference, hence invariant under adding a constant to the data and,
  up to $\epsilon$, under scaling it.)*
- **Body.** Three hidden layers of 16 nodes, softmax output of two weights;
  658 trainable parameters.
- **ENO layer.** $\tilde\omega_k=\omega_k\psi_k/\sum_j\omega_j\psi_j$ with
  $\psi_k=0$ when $\omega_k<c_{\mathrm{eno}}=2\times10^{-4}$, else 1 (page-local
  $\psi_k$, $c_{\mathrm{eno}}$): a sharp cut-off on the weights, analogous to
  TENO's cut-off on the scale-separated measure ([targeted ENO](/methods/targeted-eno.md)).
- **Loss.** $\mathcal L=\mathcal L_r+b_d\,\mathcal L_d+b_W\lVert\Theta\rVert^2$
  (page-local weights $b_d$, $b_W$; $\Theta$ the network parameters), where the
  reconstruction loss $\mathcal L_r$ penalizes the face-value error weighted by
  $\varsigma^{p_s}$ and the ideal-weight loss $\mathcal L_d$ penalizes
  $\omega_k-d_k$ weighted by $1-\varsigma^{p_s}$, with the well-resolvedness
  indicator
  $\varsigma=\dfrac{\lvert\bar u_{i-1}-2\bar u_i+\bar u_{i+1}\rvert}{\lvert\bar u_i-\bar u_{i-1}\rvert+\lvert\bar u_{i+1}-\bar u_i\rvert+10^{-15}}\in[0,1]$
  (page-local $\varsigma$, $p_s$; 0 for linear data, 1 at discontinuities).
  Huang et al. retrain with $p_s=0.1$, $b_d=0.1$, values shown by Bezgin et al.
  to improve dissipation; they note the choices are not optimal and the network
  may be over-parameterized (a rational variant uses 105 parameters).
- **Training data** (§3.3, Table 1): random cubic polynomials, jumps, sawtooth,
  $\sin(k\pi x)$ with $k\in[2,20]$ and $\tanh(kx)$ with $k\in[5,30]$, sampled at
  $\Delta x=0.01$; Adam, 100 epochs, learning rate $10^{-3}$, mini-batch 100.

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
network's lower dissipation (a qualitative argument, §3.4).

## From the network to closed form

Huang et al. (§4) then design closed-form operators on the diagram that keep
these features: a piecewise-linear ROUND that takes *more* central contribution
than WENO3-NN for $\tilde u_i<0$ (switching to CD2 below $\tilde u_i=-1.15$), and
LD-ROUND with controlled anti-dissipation on $(0,1)$; see
[ROUND schemes](/methods/round-scheme.md). The method, learning the diagram shape
from a network and then fitting a closed form, is claimed applicable to
Rational-WENO3-NN and WCNS3-MR-NN (§7).

**Cost** (Table 2, FLOPs per reconstruction, counted with JAX after Bezgin et
al.): WENO3-NN 2139, Rational-WENO3-NN 508, WENO5-JS 55, WENO3-JS 19,
LD-ROUND 20, ROUND 11. On sine advection to $t=20$ (Table 3) ROUND and LD-ROUND
have smaller $L_1$ errors than WENO3-NN at 23–31% of its CPU time (hardware not
stated): e.g. at $N_x=1280$, $L_1=8.37\times10^{-6}$ (WENO3-NN, 37.0 s),
$6.05\times10^{-6}$ (ROUND, 8.5 s), $3.21\times10^{-6}$ (LD-ROUND, 11.3 s). On the
Shu–Osher problem with 400 cells WENO3-NN is "significantly smeared out" relative
to both closed-form schemes (§6.4).

## Qualifications

- The diagram of a non-normalisable scheme is one section through its weights;
  the scale-independence assumption used to sample WENO3-NN is not verified
  in the paper.
- None of the three compact schemes reaches observed third order on smooth data:
  $L_1$ orders 2.4–2.6, $L_\infty$ orders 1.6–1.7 (Table 3); the paper does not
  discuss this.
- Huang et al. state that ROUND needs "only 5% of the cost of WENO3-NN"; their
  Table 2 gives $11/2139\approx0.5\%$ in FLOPs.

# Citations

- [Huang et al. (2026)](/sources/huang-2026.md) — §§3.2–3.4, Eqs. (3.8)–(3.14), Table 1, Fig. 2; §4; §5.1, Table 2; §6.1, Table 3; §6.4; §7.
- [Fu (2023)](/sources/fu-2023.md) — §3.10: WENO3-NN among TENO-related schemes.

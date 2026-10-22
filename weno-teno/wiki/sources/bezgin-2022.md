---
type: Source
title: "Bezgin et al. (2022) — WENO3-NN: A maximum-order three-point data-driven weighted essentially non-oscillatory scheme"
description: "Third-order finite-volume WENO on the three-cell stencil whose two nonlinear weights come from a small neural network with invariant difference features, a test-time TENO-like cut-off and a training loss that penalizes deviation from the linear weights, which restores the design order lost by earlier learned schemes."
resource: "doi:10.1016/j.jcp.2021.110920"
source_kind: paper
authors: [Bezgin D.A., Schmidt S.J., Adams N.A.]
year: 2022
venue: "J. Comput. Phys. 452:110920"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Journal_of_Computational_Physics_Bezgin_WENO3-NN_A_maximum-order_three-point_data-driven_weighted_es.pdf"
tags: [machine-learning, weno, reconstruction, finite-volume, eno-property, spectral-analysis]
timestamp: 2026-10-22T20:00:00Z
---

# Summary

This is the original WENO3-NN paper of the
[learned WENO weights](/methods/learned-weno-weights.md) family. A
finite-volume WENO3 scheme on $\{\bar u_{i-1},\bar u_i,\bar u_{i+1}\}$ keeps the
two classical second-order candidates and the linear weights $d_0=1/3$,
$d_1=2/3$ of [WENO-JS](/methods/weno-js-reconstruction.md), but takes its
nonlinear weights from a multilayer perceptron (three hidden layers of 16
swish nodes, softmax output) in place of the Jiang–Shu formula and its
[smoothness indicators](/definitions/smoothness-indicator.md). Prior knowledge
enters in three places. A "Delta layer" feeds the network four absolute first
and second differences normalized by the larger first difference, so the
weights are invariant to adding a constant and, up to $\epsilon$, to scaling
([scale invariance](/properties/scale-invariance.md)). A test-time "ENO layer"
cuts weights below $c_{eno}=2\times10^{-4}$ to zero and renormalizes, like
the [TENO](/methods/targeted-eno.md) cut-off, to restore the
[ENO property](/definitions/eno-property.md) that a saturating softmax cannot
reach. The training loss adds to the face-value error a penalty on the
deviation of the weights from $d_k$, blended per sample by a resolvedness
indicator built from the normalized second difference. The authors' central
claim is that this penalty restores the design order: without it the scheme
converges at second order, with it at about third order, like WENO3-JS and
[WENO3-Z](/methods/weno-z.md). On $\sin^3(\pi x)$ the network also
distinguishes the saddle point at which WENO3-JS and WENO3-Z degenerate
([critical points](/properties/critical-point-accuracy.md)).

The network is trained offline on 1D canonical functions; two variants are
kept (NN1, NN2). The tests use a local Lax–Friedrichs flux
([Rusanov](/methods/lax-friedrichs-flux.md)),
[characteristic decomposition](/methods/characteristic-decomposition.md) and
third-order [TVD Runge–Kutta](/methods/ssp-runge-kutta.md): linear
advection, [Sod and Lax](/benchmarks/sod-and-lax-shock-tubes.md), the
[123 problem](/benchmarks/double-rarefaction-problem.md), the
[Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md),
[Shu–Osher](/benchmarks/shu-osher-problem.md), a low-Mach Gresho vortex, the
[double Mach reflection](/benchmarks/double-mach-reflection.md) and the
[Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md).
WENO3-NN beats the WENO3-JS, Z and N schemes on all of them and approaches
WENO5-JS on several. An
[approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
shows low [dissipation](/definitions/numerical-dissipation.md) for NN2 and zero
dissipation at the cut-off wavenumber for NN1. On a GPU the cost is about 4.3
to 4.5 times that of WENO3-JS. The [normalised-variable diagram](/definitions/normalised-variable-diagram.md)
reading of WENO3-NN is not in this paper.

# Version read

Version of record (Elsevier typeset, © 2021 Elsevier Inc., issue 2022), 25
pages, all read; text extraction clean, pp. 3–6, 8 and 13 checked visually
for the equations and the Fig. 2 legend. Page 1 matches Crossref (title,
three authors, venue, DOI). Equation, figure and table numbers cited here are
those of this version.

# Key claims

Registry notation: the Jiang–Shu exponent $p$ is $q$, the reconstructed face
value (printed $u^+_{i+1/2}$) is the left state $u^-_{i+1/2}$, the
resolvedness indicator $\gamma$ is renamed $\varsigma$, the loss exponent
$\alpha$ is renamed $p_s$ and the loss weights $\beta_{d}$, $\beta_{W}$ are $b_d$, $b_W$
(all page-local, as on the [learned WENO weights](/methods/learned-weno-weights.md)
page), and the reduced wavenumber $\xi$ is $\vartheta$.

1. Any map $\mathbb R^3\to\mathbb R^2$ with outputs in $[0,1]$ summing to 1 can be regarded as a third-order WENO-type weighting function; a network with softmax output is such a map (§3.2, Eqs. 12–13). **Stated**
2. The Delta-layer features (Eqs. 14–15) are invariant to adding a constant (called "Galilean invariant"), so the whole weighting function is (§3.2). **Stated** (by construction)
3. The network alone cannot output essentially zero weights because the softmax saturates; this lets spurious oscillations through and can reconstruct negative densities or pressures at very strong shocks (interacting blast waves) (§3.2, App. A.4, Fig. 21). **Shown**
4. Without the ENO layer, WENO3-NN1 gives the discontinuous stencil of a single jump a weight "of around $10^{-4}$", hence $c_{eno}=2\times10^{-4}$ (App. A.4, Fig. 21). **Shown**
5. The ENO layer affects the solution only near discontinuities (App. A.4). **Stated**
6. Earlier learned WENO schemes trained only on the reconstruction error "were not able to achieve full-order convergence upon mesh refinement"; Stevens & Colonius's WENO5-NN needs post-processing and is first order (§1, §3.2). **Stated**
7. Without the ideal-weight penalty ($p_s=0$) WENO3-NN converges at second order: $O(\Delta x^{1.90})$ on $\tanh(2x)$ and $O(\Delta x^{1.95})$ on $\sin^3(\pi x)$ (§3.4, Fig. 2). **Shown**
8. With $p_s=0.1$ it reaches $O(\Delta x^{2.93})$ on $\tanh(2x)$ (WENO3-JS 3.00, WENO3-Z 3.01) and $O(\Delta x^{2.33})$ on $\sin^3(\pi x)$ (WENO3-JS 2.44, WENO3-Z 2.40); the text summarizes the latter as "$\mathcal O(2.5)$ which is in accordance with the WENO3-JS and WENO3-Z" (§3.4, Fig. 2). **Shown**
9. Both variants lower the $L_2$ error in the coarse regime for $\sin^3(\pi x)$, improving on classical WENO for coarsely resolved features while keeping full order (§3.4). **Shown**
10. On a piecewise sine with a jump (Eq. 23) both variants follow $d_0=1/3$ over most of the domain, deviating less than WENO3-N, and degenerate to $\omega_0=0$ or $1$ at the extrema and at the jump; NN2 deviates slightly more than NN1 (§3.5, Fig. 3). **Shown**
11. On $\sin^3(\pi x)$ WENO3-JS and WENO3-Z degenerate at the saddle point $x=0$, while WENO3-NN "distinguish the saddle point", like WENO-F3+ (§3.5, Fig. 4). **Shown**
12. The learned weighting function resembles WENO-F3+ qualitatively, with a much smaller deviation from the linear weight (§3.5, Figs. 3–4). **Shown**
13. Linear advection ($N_x=200$, $t=10$): WENO3-NN outperforms WENO3-JS, Z and N and is much closer to WENO5-JS; the square wave is diffused about as much as by WENO5-JS and WENO5-Z; NN2 is slightly better than NN1 (§4.1, Figs. 5–7). **Shown**
14. $L_1$ errors (Table 4; Euler $L_1=L_1^\rho+L_1^v+L_1^p$), in the order $\sin^3$, Gaussian–square–triangle–ellipse, discontinuous advection, Sod, Lax, 123: WENO3-NN2 $2.445\times10^{-2}$, $1.609\times10^{-1}$, $4.235\times10^{-2}$, $1.035\times10^{-2}$, $2.416\times10^{-2}$, $1.967\times10^{-2}$; WENO3-JS $1.180\times10^{-1}$, $3.702\times10^{-1}$, $8.260\times10^{-2}$, $1.636\times10^{-2}$, $3.949\times10^{-2}$, $2.540\times10^{-2}$; WENO5-JS $2.572\times10^{-3}$, $9.964\times10^{-2}$, $2.634\times10^{-2}$, $1.106\times10^{-2}$, $2.590\times10^{-2}$, $2.393\times10^{-2}$; WENO5-Z is best except on the 123 problem (App. A.6). **Shown**
15. On the three shock tubes WENO3-NN has a lower $L_1$ error than WENO5-JS, and on the 123 problem lower than WENO5-Z ($1.967\times10^{-2}$ against $2.282\times10^{-2}$) (App. A.6, Table 4). **Shown**
16. Lax problem: WENO3-NN is better than WENO5-JS and closer to WENO5-Z; NN2 shows a slight velocity overshoot like WENO5-JS (§4.2, Fig. 9). **Shown**
17. 123 problem: WENO3-NN handles the strong rarefactions "without introducing invalid pressure values" (§4.2, Fig. 10). **Shown**
18. Interacting blast waves: WENO3-NN at $N_x=400$ resembles WENO3-JS at $N_x=800$ and gives the best density among the three-point schemes (§4.3, Fig. 11). **Shown**
19. Shu–Osher: WENO3-NN at $N_x=400$ is comparable to WENO3-JS at $N_x=800$; WENO5-Z is best overall; at $N_x=800$ WENO3-NN approaches WENO5-JS (§4.4, Fig. 12). **Shown**
20. Gresho vortex ($M_0=0.01$, $96\times96$): WENO3-JS and WENO3-Z strongly deform the vortex, WENO3-NN only slightly smears it compared with WENO5-JS; NN1 is sharper but noisier than NN2 (§4.5, Fig. 13). **Shown**
21. Double Mach reflection ($1024\times256$): WENO3-NN resolves finer structures than WENO3-JS, Z and N, like WENO5-JS, and suppresses some of its spurious oscillations, but shows a slightly more pronounced post-shock instability behind the incident shock than WENO3-N or WENO5-JS (§4.6, Fig. 14). **Shown**
22. Rayleigh–Taylor: WENO3-NN gives finer structures than WENO3-JS and Z; at $256\times1024$ WENO5-JS shows no vortical structures at all (§4.7, Figs. 15–16). **Shown**
23. Approximate dispersion relation: WENO3-NN2 is considerably less dissipative than WENO3-JS over the whole wavenumber range and slightly less than WENO5-JS at high wavenumbers, with a monotone dissipation curve; WENO3-NN1 keeps dissipation minimal with zero dissipation at the cut-off wavenumber, read as under-resolved wave packets kept without interacting with resolved scales, "akin to soliton solutions" (§4.8, Fig. 17). **Shown** (curves), **Stated** (interpretation)
24. Cost (double Mach reflection, $1024\times256$, 3700 steps, JAX on a GPU), ns per cell and step: WENO3-JS 389 (1.00), WENO3-Z 396 (1.02), WENO3-N 411 (1.06), WENO3-NN1 1676 (4.31), WENO3-NN2 1743 (4.48), WENO5-JS 561 (1.44); the networks are not optimized (§4.9, Table 2). **Shown**
25. WENO3-NN "exhibits a performance similar to or better than the classical WENO5-JS" and "outperforms the classical WENO3-JS/Z/N schemes across all benchmark problems" (abstract, §5). **Shown** for the WENO3 comparison; against WENO5-JS only on the shock tubes, since Table 4 gives WENO5-JS about ten times lower error on $\sin^3$ advection and §4.1 concedes the gap "for functions with a local maximum"
26. Hyperparameters: decreasing $p_s$ at fixed $b_d=0.1$ lets the weights deviate further from $d_k$, increasing $b_d$ at fixed $p_s=0.1$ pulls them back; at $b_d=1$, $\omega_0$ deviates only at smooth extrema (App. A.3, Fig. 20). **Shown**
27. Linear advection of $\sin^3(\pi x)$ to $t=2$ with CFL 0.05: WENO3-NN1 and NN2 have lower errors than WENO3-JS, Z and N "and also show better convergence behavior" (App. A.5, Fig. 22; no orders printed). **Shown**

# Printed slips

- Eq. (9): $\beta_k=\sum_{l=0}^{r-1}\Delta x^{2l-1}\int\frac{d^l}{dx^l}u^k\,dx$, with the sum from $l=0$ and the integrand not squared; only the $l=1$ term with a squared derivative reproduces Eq. (10), $\beta_0=(\bar u_i-\bar u_{i-1})^2$. *(compiler check, not in the sources.)*
- Eq. (27): the Gaussian is printed $G(x,\beta,z)=e^{\beta(x-z)^2}$, without the minus sign.
- §2: "we will only present the calculation of $u^+_{i+1/2}$", but Eq. (7) builds the left-biased state, the left argument $u^-_{i+1/2}$ of the flux in Eq. (5).
- Eq. (A.3) is called equivalent to Eq. (A.2), but $\mathrm{ReLU}(\omega_k-c_{eno})$ also shifts the surviving weights before renormalization: $\omega=(0.4,0.6)$ becomes $(0.39996,0.60004)$ instead of $(0.4,0.6)$; the difference is negligible. *(compiler check, not in the sources.)*
- Conclusion: "a newly introduced loss term on the network weights" allows full-order convergence; the new term acts on the reconstruction weights $\omega_k$ (as the abstract says), the term on the network weights is the $\ell_2$ regularization.
- §3.4: "$\mathcal O(2.5)$" for $\sin^3(\pi x)$ where the Fig. 2 legend gives 2.33 (NN), 2.44 (JS) and 2.40 (Z).
- Figs. 3–4 captions: "Comparison of the smoothness measures" for plots of $\omega_0$.
- Conclusion: "reconstruction via Harten polynomials" against "ENO polynomials" in §§1 and 3.
- §4.7: the Rayleigh–Taylor initial pressure $1+2y$ / $1.5+y$ is hydrostatic only with a gravity source term, which the homogeneous Euler system (26) does not contain. *(compiler check, not in the sources: $\partial_yp=2=\rho$ below and $1=\rho$ above the interface, a balance with a body force of unit magnitude per unit mass that no printed equation carries.)*
- §4.9: the GPU is named "Nvidia GTX2080".
- Ref. [12]: DOI printed truncated ("10.1002/fld."), authors printed as "W. Xiaoshuai, Z. Yuxin". Table 4: "2.282E- 2". Typos: "looses" (§1), "intersting" (§4.8), "Therfore" (App. A.6), "timeis" (§4.5).

# Notation map

| Bezgin et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar u_i$, $x_{i\pm1/2}$, $\hat f_{i+1/2}$ | same | agree |
| $u^+_{i+1/2}$ (as printed) | $u^-_{i+1/2}$ | the reconstructed left-biased state |
| $S_0$, $S_1$, $S^3$ | $S_0$, $S_1$, full stencil | two-point candidates, three-point stencil |
| $u^{(k)}_{i+1/2}$ | $u^{(k)}_{i+1/2}$ | candidate values (upwind and central second-order) |
| $r$, $d_k$, $\beta_k$, $\alpha_k$, $\omega_k$ | same | $r=2$; agree |
| $p$ | $q$ | Jiang–Shu exponent, 2 |
| $\epsilon$ | $\epsilon$ | $10^{-15}$; also in the Delta layer |
| $\omega^{NN}_k$, $\tilde\omega^{NN}_k$ | kept | raw network weights and weights after the ENO layer |
| $c_{eno}$, $\psi_j$ | kept | weight cut-off and 0/1 flag; analogous to $C_T$, $\delta_k$, but applied to the weights, not to $\chi_k$ |
| $\tilde\Delta_j$, $\Delta_j$ | kept | raw and normalized difference features |
| $\gamma$, $\epsilon_\gamma$ | $\varsigma$ (page-local), kept | resolvedness indicator in $[0,1]$; **$\gamma$ is the ratio of specific heats and $\gamma_k$ the TENO measure in the registry; $\varsigma$ is a THINC symbol in registry §10, unused on these pages** |
| $\alpha$ (loss) | $p_s$ (page-local) | exponent on the resolvedness indicator, 0.1 (NN1), 0.03 (NN2); **collides with $\alpha_k$** |
| $\beta_d$, $\beta_W$ | $b_d$, $b_W$ (page-local) | loss weights; **collide with $\beta_k$** |
| $\beta$ (Eq. 27) | kept | Gaussian constant of the advection test |
| $\mathcal L$, $\mathcal L_r$, $\mathcal L_d$ | kept | losses; **$\mathcal L$ is the semi-discrete operator in the registry** |
| $W$, $b$, $a$, $\sigma$ | kept | network weights, biases, activations, activation; **$\sigma$ is the affine scaling of §10** |
| $\theta$ | $\Theta$ | network parameters; **$\theta$ is the Zhang–Shu factor in the registry** |
| $\xi$, $\tilde\xi_R$, $\tilde\xi_I$ | $\vartheta$, $\tilde\vartheta_r$, $\tilde\vartheta_i$ | approximate dispersion relation |
| $N$ | $N_x$ | number of cells |
| $\gamma$ (gas) | $\gamma$ | 1.4; 5/3 for Rayleigh–Taylor |

# Reference list

23 printed references in numbered style ([1]–[23]), all parsed and merged
complete into the [bibliography](/bibliography.md) with `citedby`
`bezgin-2022`. Items recorded as printed: [9] (Shu's lecture notes) carries a
journal-like venue; [10] is a conference paper with arXiv identifier and [11]
an arXiv preprint; [12] prints a truncated DOI, which is not recorded as a
DOI; [21] is a Springer chapter; [23] is software (JAX, 2018). No printed
duplicates.

# Pages created or updated

Chunk 3 (2026-10-22), cited further in chunk 4 (2026-10-23). This source is cited on:

* [Accuracy at critical points](/properties/critical-point-accuracy.md)
* [Approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Double rarefaction (123) problem](/benchmarks/double-rarefaction-problem.md)
* [ENO property](/definitions/eno-property.md)
* [Gresho vortex](/benchmarks/gresho-vortex.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Learned WENO weights](/methods/learned-weno-weights.md)
* [Normalised-variable diagram](/definitions/normalised-variable-diagram.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)
* [Scale and affine invariance](/properties/scale-invariance.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Targeted ENO (TENO)](/methods/targeted-eno.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
* [WENO-Z weights](/methods/weno-z.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)

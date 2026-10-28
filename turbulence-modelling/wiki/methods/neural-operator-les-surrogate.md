---
type: Method
title: "Neural-operator surrogates of large-eddy simulation"
description: "A neural operator (Fourier, implicit Fourier or transformer-based) learns the time advance of the filtered velocity field on the LES grid and replaces the whole LES solver in an autoregressive rollout; trained on filtered DNS or, physics-informed, on the residual of the Smagorinsky-closed filtered equations, and compared with dynamic and static Smagorinsky LES."
status: established
aliases: [neural operator, Fourier neural operator, FNO, IFNO, implicit Fourier neural operator, transformer-based neural operator, TNO, LESnets, LESnets-I, physics-informed neural operator, PINO, data-driven LES surrogate]
tags: [neural-network, data-driven, les, sgs-model]
timestamp: 2026-10-28T07:06:00Z
---

# Neural-operator surrogates of large-eddy simulation

A **neural-operator LES surrogate** does not model the subgrid stress
$\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$ inside a solver, as a
[neural-network SGS model](/methods/neural-network-sgs-model.md) does. It
learns the map that advances the filtered velocity on the LES grid,
$\bar{\boldsymbol u}(t_{n-n_{\mathrm{in}}+1}),\dots,\bar{\boldsymbol u}(t_n)\mapsto\bar{\boldsymbol u}(t_{n+1}),\dots$,
and replaces the LES solver altogether: the prediction is fed back as input
and the flow is advanced by an **autoregressive rollout** (page-local:
$n_{\mathrm{in}}$ the number of input time levels, $\mathcal G_{\boldsymbol\theta}$
the network). Both sources of this bundle come from one group and test the
idea on periodic boxes against filtered DNS and against Smagorinsky-type
LES on the same coarse grid. [Li et al. (2024)](/sources/li-2024.md) train
the operator on filtered-DNS trajectories (data-driven);
[Zhao et al. (2025)](/sources/zhao-2025.md) train it on the residual of the
filtered Navier–Stokes equations closed by the
[Smagorinsky model](/methods/smagorinsky-model.md), with no labelled
trajectories (physics-informed). Every test in both papers is an a
posteriori rollout from initial fields not used in training (see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).

## The operator layer

Both papers build on the Fourier neural operator (FNO), which Li et al.
(2024, §III, Eqs. 12–14) and Zhao et al. (2025, §2.3, Eqs. 9–14) describe. A
lifting network $P$ maps the input fields to $d_v$ channels (page-local
$d_v$, the channel width), $n_L$ Fourier layers (page-local $n_L$; the
registry's $L$ is the integral length) update the latent field
$v$, and a projection $Q$ returns the velocity. One layer is

$$v_{l+1}(\boldsymbol x)=\sigma\Big(W v_l(\boldsymbol x)+\mathfrak F^{-1}\big(R_\phi\cdot\mathfrak F v_l\big)(\boldsymbol x)\Big),$$

with $\sigma$ the activation (GELU in both), $W$ a pointwise linear map,
$\mathfrak F$ the discrete Fourier transform and $R_\phi$ complex weights
acting on the lowest $k_{\max}$ modes only (page-local $\mathfrak F$,
$R_\phi$, $k_{\max}$; the registry keeps $\hat\phi$ for the test filter).
The truncation is what makes the layer independent of the grid size.

- **Implicit FNO (IFNO).** Zhao et al. (2025, Eq. 15) also use the
  implicit form $v_{l+1}=v_l+\delta t\,\sigma(Wv_l+\mathfrak F^{-1}(R_\phi\cdot\mathfrak Fv_l))$,
  with weights shared across layers and $\delta t$ the interval between
  input and output (page-local).
- **Modified FNO.** Li et al. (2024, §III, Fig. 1) merge the velocity
  components and the $n_{\mathrm{in}}=5$ input time levels into channels
  (plus three coordinate channels), so the transform is 3-D, not 4-D. They
  state that this improves accuracy and cost over their earlier FNO for
  LES; no ablation is shown. All their FNO results use this version.
- **Transformer-based neural operator (TNO).** Li et al. (2024, §IV,
  Figs. 2–3, Eqs. 16–25) reshape the $N_x\times N_y\times N_z$ grid into a
  sequence of $N_xN_yN_z$ tokens and apply multi-head *linear* (Galerkin-type,
  softmax-free) attention with a 3-D rotary position embedding, then
  reshape back and finish with one Fourier layer and a feed-forward
  network (the "spectral regressor"). Linear attention costs
  $O(N_sN_d^2)$ instead of $O(N_s^2N_d)$ for $N_s$ tokens of embedding size
  $N_d$ (page-local), a complexity argument not timed separately (Eqs.
  19–21). The authors read attention as a kernel integral and state that,
  with Fourier kernels and mode truncation, it "is equivalent to the
  fourier neural operator" (§IV, Eq. 20). Because the token sequence is
  never downsampled, they argue, the model keeps the high-frequency content
  that general transformer surrogates lose to grid downsampling (§I).

## Two ways of training

**Data-driven (Li et al. 2024).** The loss is the mean squared error of
the predicted filtered velocity summed over several chained rollout steps
(Eqs. 28–31, Fig. 2); the number of chained steps is not stated. Each
network takes $n_{\mathrm{in}}=5$ filtered-DNS fields and returns the next
one. The data are 100 initial fields of 600 time levels in isotropic
turbulence and 200 fields of 90 levels in the mixing layer, split 80/20
(§V A 1, §V B 1).

**Physics-informed (Zhao et al. 2025, "LESnets").** The network maps one
filtered field at $t_n$ to the following ten ($T=11$ frames) and is
trained only on the residual of the filtered equations, the
physics-informed neural operator (PINO) idea. In registry notation the
two residuals are

$$\mathcal L_{\mathrm{PDE}}=\big\|\partial_i\bar u_i\big\|^2+\big\|\partial_t\bar u_i+\partial_j(\bar u_i\bar u_j)+\partial_i\bar p-\nu\nabla^2\bar u_i+\partial_j\tau^d_{ij}\big\|^2,\qquad \tau^d_{ij}=-2(C_s\Delta)^2\lvert\bar S\rvert\bar S_{ij},$$

with $\bar p$ the kinematic pressure, norms over the output frames and the
domain, and the residual written here from the filtered equation (Eq. 4)
moved to one side (§2.5, Eqs. 3–5, 17; printed form in Qualifications).
Space derivatives are spectral, the pressure comes from a Poisson
equation in Fourier space, and $\partial_t$ is a central difference across
output frames (§2.4, Eq. 16; Algorithm 1). The differences from the
original PINO, as stated by the authors (§2.4–2.5):

- the initial field is an *input*, not a loss term, so one filtered field
  per case suffices and the output can be fed back for rollout;
- no labelled trajectories enter the loss;
- the output interval is free, because no labels fix it.

The original PINO with an initial-condition loss, $\mathcal L_{\mathrm{PDE}}+w_{\mathrm{ic}}\mathcal L_{\mathrm{ic}}$
($w_{\mathrm{ic}}$ from 0.1 to 10, page-local), diverges in rollout of
decaying isotropic turbulence; for $w_{\mathrm{ic}}=0.1$, 0.2 and 0.5 it
fails at the first iteration (App. A, Fig. A1). Zhao et al. (2025, §2.4)
cite the original PINO paper for 6% relative $L_2$ error at $T=0.125$ but
about 74% at $T=0.5$ on 2-D turbulence.

**Hybrids.** Zhao et al. (2025) add two variants:

- *Data plus PDE loss* (§5.4, Eq. 27), $\mathcal L_{\mathrm{PDE}}+w_{\mathrm{data}}\mathcal L_{\mathrm{data}}$
  with 5000 labelled trajectories ($w_{\mathrm{data}}$ page-local): the
  results move between the data-driven FNO and LESnets as the weight
  changes; $w_{\mathrm{data}}=0.1$ is closest to filtered DNS.
- *Learned Smagorinsky coefficient* (§4, Eqs. 25–26, Algorithm 2): $C_s$
  becomes a trainable parameter with its own Adam optimizer, driven by the
  same residual evaluated on a single 11-frame trajectory of either
  Smagorinsky LES (run with $C_s=0.1$) or filtered DNS; this residual
  updates only $C_s$. See [Smagorinsky model](/methods/smagorinsky-model.md)
  and, for the data-assimilation motivation the authors cite,
  [ensemble Kalman calibration](/methods/ensemble-kalman-closure-calibration.md).

  | Data for the coefficient loss | Learned $C_s$ (weights 5 to 100, learning rate $10^{-5}$) |
  |---|---|
  | Smagorinsky LES with $C_s=0.1$ | 0.1123, 0.0998, 0.0998, 0.0982 |
  | filtered DNS ($k_c=10$) | 0.1892, 0.1866, 0.1859, 0.1856 |

  (Table 4.) The fDNS-learned coefficient is about 0.19, yet the a
  posteriori results are "comparable" to the SM-data case, and the learned
  value is not always unique (§4.2). At weight 50 and learning rate
  $10^{-6}$ both data sets give about 0.07 (0.0661, 0.0680; Table 4).

## Test flows

| | Li et al. (2024) | Zhao et al. (2025) |
|---|---|---|
| [Isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md) | forced, DNS $256^3$, $Re_\lambda\approx100$; sharp spectral filter, $k_c=21$, LES $64^3$ | decaying, DNS $128^3$, $Re_\lambda\approx60$; sharp spectral filter, $k_c=10$, LES $32^3$ |
| [Temporal mixing layer](/benchmarks/temporal-mixing-layer.md) | $8\pi\times8\pi\times4\pi$, DNS $256\times256\times128$; Gaussian filter, $\Delta=4$ DNS spacings, filter-to-grid ratio 1, LES $64\times64\times32$ | same domain and DNS grid, $Re_\theta=20$ initially; sharp spectral filter, $\Delta=8$ DNS spacings, ratio 2, LES $64\times64\times32$ |
| LES baselines | dynamic Smagorinsky and dynamic mixed model, coefficients by global least squares (test filters $2\Delta$, $4\Delta$) | Smagorinsky, $C_s=0.1$ (isotropic), $C_s=\sqrt{0.001}\approx0.032$ (mixing layer) |
| Rollout tests | 10 new initial fields; isotropic to $t/T_E\approx40$; mixing layer to $650$ momentum-thickness times | 5 new initial fields; 250 network steps (5000 DNS steps, about $5T_E$ in isotropic turbulence) |

(Li et al. §V; Zhao et al. §3, Tables 1, 3. $T_E$ is the large-eddy
turnover time, page-local, both papers' $\tau=L/u^{\mathrm{rms}}$. The value $\sqrt{0.001}\approx0.032$ is
a *compiler check, not in the sources*.)

## Results

**Accuracy and stability.**

- *Isotropic turbulence, data-driven (Li et al. 2024, §V A 2).* The TNO is
  comparable to dynamic Smagorinsky LES and better than the FNO and the
  dynamic mixed model. Its spectrum is closer to filtered DNS than the
  dynamic Smagorinsky spectrum for $3\le k\le17$, and farther for $k\ge18$; its
  velocity-increment PDFs stay consistent with filtered DNS where both
  dynamic models deviate (Figs. 6–8). All four models run stably (Fig. 9).
- *Mixing layer, data-driven (§V B 2).* The TNO is the most accurate of all
  in momentum thickness, directional kinetic energies, spectra and vortex
  structures and stays stable to $t/\tau_\theta\approx650$
  ($\tau_\theta$ page-local, the initial momentum thickness over the
  velocity difference). The FNO momentum thickness "becomes unreliable"
  after $400\,\tau_\theta$ and its kinetic energies diverge after
  $200\,\tau_\theta$ (Figs. 16–17). The two dynamic LES under- then
  over-predict the kinetic energies and predict larger vortices than
  filtered DNS (Figs. 17, 20).
- *Isotropic turbulence, physics-informed (Zhao et al. 2025, §3.1).*
  LESnets are stable and close to filtered DNS over about $5T_E$ and track
  the Smagorinsky LES they encode; the data-driven FNO, though best in
  test loss, deviates by $t\approx2T_E$ and fails to predict the kinetic
  energy at $t\approx T_E$; the data-driven IFNO over-predicts rms
  velocity, vorticity, kinetic energy and dissipation, while LESnets
  under-predict them (Figs. 6–8). The implicit backbone helps data-driven
  training but gives "a negligible enhancement" for LESnets.
- *Mixing layer, physics-informed (§3.2).* The FNO does not diverge; the
  data-driven models predict the momentum thickness better than LES, and
  LESnets are comparable to Smagorinsky LES (Figs. 13–14).
- *Reynolds-number extrapolation (Li et al. 2024, §V A 4).* Trained at
  $Re_\lambda\approx100$, the TNO is run without retraining at 160 and 250
  on the same $64^3$ grid: it is more accurate than both dynamic models in
  the second-order structure function and the increment PDFs, and less
  accurate than dynamic Smagorinsky in the spectrum (Figs. 12–13). The
  authors offer the self-similarity of turbulence as the "theoretical
  foundation" of the extrapolation.

**Size and cost.**

| | Parameters | Inference per step or rollout | LES on the same grid |
|---|---|---|---|
| TNO, isotropic (Li et al., Table I) | $268.6\times10^6$ | 1.021 s GPU, 12.48 s CPU per time node | 105.6 s (dynamic Smagorinsky), 166.4 s (dynamic mixed) CPU per time node |
| FNO, isotropic (Li et al., Table I) | $563.9\times10^6$ | 0.206 s GPU, 4.366 s CPU | — |
| TNO, mixing layer (Table II) | — | 1.691 s GPU, 20.18 s CPU | 83.55 s, 97.86 s |
| LESnets (FNO), isotropic (Zhao et al., Table 5) | $1061.7\times10^6$ | 1.51 s for 250 steps | 45.62 s (Smagorinsky) |
| LESnets (FNO), mixing layer (Table 6) | — | 3.18 s for 250 steps | 126.79 s |

Li et al. time the networks on one V100 GPU or one Xeon Gold 6240 CPU and
the LES on a cluster of Xeon Gold 6148 CPUs (16 cores each); Zhao
et al. on A100 GPUs against LES on a Xeon Gold 6148 cluster. Zhao et al.
state LESnets are about 30 (isotropic) and 40 (mixing layer) times faster
than LES, that training costs 1–5% more per epoch than the data-driven
counterpart with the same parameters and memory, and that LESnets are less
efficient than LES once training time is counted (§5.1). Li et al. train
the TNO in 11.2 h (isotropic) and 10.6 h (mixing layer), the FNO in 14.6 h
and 15.2 h (§V A 1, §V B 1).

**Sensitivity (Zhao et al. 2025, §5.2–5.3, Table 7, Figs. 24–25).**
Prediction is "significantly weakened" with fewer than six layers; a
channel width $d_v<80$ or $k_{\max}\le8$ may be insufficient; $n_L=6$,
$d_v=80$, $k_{\max}=12$ give converged results. With 2000 initial fields
the test loss is already about 0.059 but the a posteriori rms velocity and
spectra are too high; 3000 fields are needed.

## What the surrogates inherit and what they cannot do

- **Bounded by the encoded LES.** Zhao et al. (2025, §3.1, §6) state that
  LESnets' accuracy is bounded by the SGS model in the loss and by the
  operator architecture: their results are "closer to SM", i.e. they
  reproduce Smagorinsky LES, not filtered DNS.
- **Loss is not a predictor of rollout.** Zhao et al. (2025, §3.1, §5.4)
  find the lowest test loss in the data-driven FNO and the earliest
  divergence in rollout; Li et al. (2024) report lower training and test
  losses for the TNO in the mixing layer (Figs. 5, 15) together with
  better rollout. See
  [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).
- **Periodic boxes only.** Both papers test only triply periodic flows
  (the mixing layer with diffusion buffer zones). Li et al. (2024, §VI)
  state that the TNO needs separate training per configuration and
  extensions such as geometry-aware FNOs for boundaries and non-uniform
  grids; Zhao et al. (2025, §6) that non-uniform grids and complex
  boundaries need other discretizations of the loss.

## Qualifications

- **Different FNO verdicts, different setups.** In Li et al. (2024) the
  modified FNO runs stably in forced isotropic turbulence and fails late in
  the mixing layer; in Zhao et al. (2025) the data-driven FNO diverges early
  in *decaying* isotropic turbulence and does not diverge in the mixing
  layer. The flows (forced against decaying), Reynolds numbers, grids,
  filters, FNO variants and training sets differ, so the two results are
  not on a common case.
- **Dynamic coefficients.** Li et al. (2024, Eqs. 8, 10–11) average the
  Germano least-squares terms over the whole domain, so the dynamic
  coefficients are uniform in space also in the inhomogeneous mixing layer
  (see [dynamic procedure](/methods/dynamic-procedure.md)).
- **Cost comparisons** set network inference, on GPU or CPU, against full
  LES time advance on other hardware, and exclude training (Li et al.
  Tables I–II; Zhao et al. §5.1, which says so).
- **Printed slips, Li et al. (2024).** The text calls the TNO "three times
  slower than the FNO" (§V A 3); Table I gives a CPU ratio
  $12.48/4.366=2.86$ and a GPU ratio $1.021/0.206=4.96$ *(compiler check,
  not in the sources)*. The dynamic mixed model is printed as
  $\tau_{ij}=C_1\Delta^2\lvert\bar S\rvert\bar S_{ij}+\dots$ (Eq. 9) while its
  Germano tensors use $-2\Delta^2\lvert\bar S\rvert\bar S_{ij}$ (Eqs. 10–11), a
  factor $-2$ apart. The rotary-embedding identity (Eq. 23) multiplies a
  rotation matrix by a scalar. The number of attention layers, the number
  of heads and the embedding size of the TNO are not stated.
- **Printed slips, Zhao et al. (2025).** Eqs. 17 and 25 write the SGS term
  as "$-\nabla\tau$", a gradient where Eq. 4 has the divergence
  $-\partial_j\tau_{ij}$ (on the right-hand side), and Algorithm 1 adds the
  scalar $\mathfrak F^{-1}(\hat p)$ (their Fourier pressure) to the vector
  momentum residual instead of its gradient (line 19). Algorithm 1 also
  sums unsquared norms of the continuity plus momentum residuals, a
  different $\mathcal L_{\mathrm{PDE}}$ from Eq. 17. In §5.4 two
  consecutive sentences give opposite directions for the shift between
  FNO-like and LESnets-like results as the data weight decreases; since the
  weight multiplies $\mathcal L_{\mathrm{data}}$ (Eq. 27), a large weight
  is the FNO-like end, as the second sentence states *(compiler check, not
  in the sources)*. The paper also calls the training-stage behaviour of the
  coefficient loss an "a priori test" (§4.1).
- **Notation.** Both papers write the test filter with a tilde, which the
  registry reserves for the Favre filter, and use $\langle\cdot\rangle$ for
  a domain average; Zhao et al. write the Smagorinsky coefficient
  $C_{Smag}$ and $\lambda$ both for perturbation amplitudes and the
  learning rate.

# Citations

- [Li et al. (2024)](/sources/li-2024.md) — arXiv v2: §I (downsampling in transformer surrogates); §II, Eqs. 7–11 (dynamic baselines); §III, Eqs. 12–15, Fig. 1 (modified FNO); §IV, Eqs. 16–31, Figs. 2–3 (TNO, linear attention, rotary embedding, loss, rollout); §V A, Tables I, Figs. 5–13 (isotropic turbulence, cost, extrapolation); §V B, Table II, Figs. 15–21 (mixing layer); §VI.
- [Zhao et al. (2025)](/sources/zhao-2025.md) — arXiv v3: §2.1, Eqs. 3–5; §2.3, Eqs. 9–15 (FNO, IFNO); §2.4, Eq. 16; §2.5, Eq. 17, Algorithm 1 (LESnets); §3.1–3.2, Tables 1–3, Figs. 5–14; §4, Eqs. 25–26, Algorithm 2, Table 4 (learned coefficient); §5.1, Tables 5–6 (cost); §5.2–5.4, Table 7, Figs. 24–27; §6; App. A, Fig. A1.

---
type: Source
title: "Bezgin et al. (2025) — ML-ILES: End-to-end optimization of data-driven high-order Godunov-type finite-volume schemes for compressible homogeneous isotropic turbulence"
description: "Machine-learned implicit LES: small networks replace the TENO6-A weighting of four fixed candidate polynomials in an HLLC finite-volume scheme, one network per primitive field, trained end-to-end through the differentiable JAX-Fluids solver on filtered DNS of compressible decaying isotropic turbulence at turbulent Mach numbers 0.4 to 0.8."
resource: "doi:10.1016/j.jcp.2024.113560"
source_kind: paper
authors: [Bezgin D.A., Buhendwa A.B., Schmidt S.J., Adams N.A.]
year: 2025
venue: "J. Comput. Phys. 522:113560"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Journal_of_Computational_Physics_Bezgin_ML-ILES_End-to-end_optimization_of_data-driven_high-order_Go.pdf"
tags: [implicit-les, data-driven, model-consistent-training, weno, isotropic-turbulence, compressible]
timestamp: 2026-10-29T10:04:00Z
---

# Summary

Bezgin et al. (2025) build ML-ILES, a machine-learned
[implicit LES](/definitions/implicit-les.md) for compressible decaying
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md).
The HLLC + TENO6-A finite-volume scheme is kept (the four candidate
polynomials of the six-point stencil, the HLLC Riemann solver, TVD-RK3),
and only the [TENO](/methods/weno-scheme.md) weighting (smoothness
measures, cut-off, optimal weights) is replaced by three small multilayer
perceptrons, one each for density, velocity (applied to every component)
and pressure, which map the five first differences of the stencil to four
convex weights through a softmax (3132 parameters in all). The scheme is
trained [end-to-end](/methods/model-consistent-training.md): the
differentiable JAX-Fluids solver is unrolled for $N_T\in\{1,2,5\}$ coarse
steps and a cell-wise mean-absolute error against box-filtered $512^3$
runs ($32^3$, factor 16 in space and time) at $M_t=0.4$, 0.6, 0.8 is
differentiated with `jax.grad`; no adjoint is derived. The authors place
this against offline-trained explicit
[neural-network SGS models](/methods/neural-network-sgs-model.md) and
against [reinforcement-learning](/methods/reinforcement-learning-closure.md)
and [discretization-consistent](/definitions/discretization-consistent-closure.md)
closures.

In short in-solver rollouts (which the paper calls "a priori") each model
is best at the horizon it was trained for; over the full decay
("a posteriori", the [two testing modes](/definitions/a-priori-and-a-posteriori-testing.md))
the $N_T=1$ model has the lowest spectral error at all three Mach numbers
and the $N_T=5$ model the highest, so the cell-wise fit does not decide
the spectral behaviour. ML-ILES follows the filtered kinetic-energy
spectrum up to the cut-off, improves the high-wavenumber
[dissipation](/properties/numerical-dissipation.md) of TENO6-A, gives the
best density spectra at higher $M_t$ against TENO6-A and the compressible
ALDM (which uses a Ducros [shock sensor](/definitions/shock-sensor.md)),
and carries over to $64^3$. The learned weights differ by field: pressure
discards the downwind polynomial, density keeps it small, velocity
resembles the TENO6-A optimal weights. The reference "DNS" runs at
$k_{\max}\eta\approx2.3$ against the authors' own full-resolution
criterion $k_{\max}\eta\ge\pi$
([DNS](/definitions/direct-numerical-simulation.md)). Cost: 2.7–4.4 times
TENO6-A per cell and step on one GPU. The coarse-graining box filter
"corresponds to implicit filtering commonly used in finite-volume methods
(the LES grid itself acts as a filter)" (§4.1; see
[LES](/definitions/large-eddy-simulation.md)).

# Version read

Version of record (Elsevier, open access CC BY-NC; received 1 April 2024,
revised 20 October 2024, accepted 3 November 2024, online 14 November
2024), 18 pages, all read; pages 4–8 and 10–13 checked visually for
equations and tables. Page 1 matches the metadata (title, four authors,
venue, DOI). Numbering on this page is that of the version read.

# Key claims

Page-local symbols: $\mathcal N^\rho$, $\mathcal N^u$, $\mathcal N^p$ the
reconstruction networks; $N_H$ the hidden units per layer; $N_T$ the number
of unrolled coarse steps (also the trajectory length of the error
metrics); $p_k$ the candidate polynomials, $\mathsf w_k$ their weights
(registry §11); $\tau_\lambda=\lambda/u_{\mathrm{rms}}$ the Taylor time
scale; $\Delta_{\mathrm{LES}}/\Delta_{\mathrm{DNS}}$ the coarse-graining
ratio; $k_{\max}$ the largest resolved wavenumber.

1. In ILES "the nonlinear discretization error of the convective term functions as an SGS model", the truncation error being shaped to match the desired SGS behaviour (§1, citing [2]). **Stated**
2. Machine-learned ILES models, in which the learned part is the discretization, "may provide better extrapolation capabilities to unseen meshes and flow configurations" than explicit LES closures (§1). **Stated**
3. ML-ILES replaces the TENO6-A weighting by $\mathcal N^\rho$, $\mathcal N^u$, $\mathcal N^p$, which output the convex weights of the four Harten-type polynomials; the weighting is the only difference from HLLC + TENO6-A (§3.1, §5). **Derived** (construction)
4. "The overall reconstruction scheme, as it uses Harten-type polynomials $p_k$ as building blocks, is at least third-order accurate" (§3.1). **Stated** (no order test shown)
5. Inputs made of first differences (Eq. 19) "make the reconstruction Galilean invariant" (§3.1). **Stated**
6. Each network maps $\mathbb R^5\to\mathbb R^4$ with 3 hidden layers of $N_H=20$ units, Leaky ReLU and softmax output, 1044 parameters; 3132 in total (§3.1, Table 5). **Derived** *(Compiler check, not in the sources: $5\cdot20+20+2(20\cdot20+20)+20\cdot4+4=1044$; for $N_H=5$ and 10 the same count gives 114 and 324 per network, 342 and 972 in total, as in Table 5.)*
7. The HLLC flux in central form (Eq. 28) "reveals three dissipation mechanisms, corresponding to the three-wave solution of the underlying Riemann problem" (§3.2, citing [22]). **Stated**
8. End-to-end optimization "is essential" for learning a discretization, because only the optimal solution trajectory is known a priori, not the optimal discretization; it improves inference stability because the gradients carry the PDE dynamics and the models see their own error accumulation (§4.2). **Stated**
9. Thermodynamically consistent decaying-turbulence initial conditions of Ristorcelli & Blaisdell exist only for a limited Mach range; snapshots of forced turbulence in statistical steady state are used instead (§4.1). **Stated**
10. Forced turbulence reaches statistical steady state after $t/\tau\approx25$, with $Re_\lambda\approx200$ averaged over the runs and $k_{\max}\eta\approx2.3$, while $k_{\max}\eta\ge\pi$ ($\eta/\Delta x\ge1$) "is required to fully resolve all scales"; if not all scales are resolved, TENO6-A "acts as an ILES model" (§4.1, Figs. 2–3). **Shown** *(Compiler check, not in the sources: $2.3<\pi$, so the $512^3$ reference does not meet the paper's own criterion.)*
11. At $M_t=0.8$ eddy shocklets appear as thin regions of negative dilatation; at $M_t=0.4$ the turbulence is essentially shock free (§4.1, Fig. 5). **Shown**
12. In short rollouts (Table 2) each ML-ILES model gives the lowest cell-wise error summed over $M_t$ at its training horizon: $N_T=1$ at 1 step (8.821e-02), $N_T=2$ at 2 steps (1.284e-01), $N_T=5$ at 5, 10 and 20 steps (2.241e-01, 3.282e-01, 4.571e-01); ALDM 9.250e-02 to 5.156e-01; TENO6-A 1.015e-01 to 5.318e-01 (§5.1). **Shown**
13. The short-rollout results "are meant to demonstrate the training fit … rather than indicate their potential to comprehensively reproduce turbulence dynamics" (§5.1). **Stated**
14. Over the full decay (Table 3, MAE/MSE) $N_T=1$ has the lowest total spectral error at every Mach number (0.8849/0.3698 at 0.4; 0.7923/0.3048 at 0.6; 0.6178/0.1701 at 0.8), against TENO6-A (1.110/0.5324; 1.153/0.5817; 1.173/0.5752) and ALDM (1.099/0.5497; 1.252/0.8017; 1.428/0.9929); $N_T=5$ is worst (1.480/1.183; 1.562/1.298; 1.428/1.064) (§5.2). **Shown**
15. "The cell-wise error computed in the previous section does not necessarily correspond to good spectral properties during the decay": the longest-horizon model wins the short rollouts and loses the full decay (§5.2). **Shown**
16. At $M_t=0.4$ ML-ILES follows the filtered kinetic-energy spectrum up to the cut-off, like ALDM, with "considerable improvements in terms of dissipation properties in the high wave number range" over TENO6-A; density spectra are similar for the three (§5.2, Fig. 7). **Shown**
17. At $M_t=0.6$ and 0.8 the ML-ILES kinetic-energy spectrum "nearly overlaps" the filtered one up to the cut-off while ALDM and TENO6-A underpredict at high wavenumbers (ALDM closer); for density ML-ILES is best, and TENO6-A beats ALDM as $M_t$ rises, "potentially" because ALDM was optimized for lower-Mach turbulence (§5.2, Fig. 7). **Shown** (explanation **Stated**)
18. For $p_{\mathrm{rms}}$, ML-ILES and ALDM nearly overlap at $M_t=0.4$ and are slightly closer to the filtered DNS late in the decay; at higher $M_t$ ML-ILES is closer to TENO6-A, both following the filtered DNS closely at 0.8; overall ML-ILES is closest (§5.2, Fig. 8). **Shown**
19. Trained at $\Delta_{\mathrm{LES}}/\Delta_{\mathrm{DNS}}=16$ ($32^3$), ML-ILES at $64^3$ ($\Delta_{\mathrm{LES}}/\Delta_{\mathrm{DNS}}=8$) agrees well with the filtered DNS and "clearly outperforms TENO6-A" in kinetic-energy and density spectra at all $M_t$ (§5.2, Fig. 9). **Shown**
20. Restricting the network output to weights of Harten-type polynomials "provides a fallback mechanism … while guaranteeing convergence upon mesh refinement" (§5.2). **Stated** (one refinement shown)
21. The learned reconstructions differ by field: at $M_t=0.4$ the downwind weight is small and nearly uniform for density, larger and more variable for velocity, and $\langle\mathsf w^p_3\rangle\approx0$ for pressure through the decay; for density and pressure "clearly an upwind-biased reconstruction is preferred", $\langle\mathsf w_3\rangle$ being zero for pressure and about 0.08 for density (§5.3, Figs. 10–12). **Shown**
22. The velocity reconstruction "somewhat resembles" the spectrally optimized TENO6-A linear weights $d_k$ and is stable across Mach numbers, so ML-ILES "seems to learn a similar strategy purely from data" (§5.3). **Shown**
23. The spatial adaptation of the density weights increases with $M_t$, most visibly for $\mathsf w^\rho_1$ (§5.3, Figs. 10–12). **Shown**
24. Smaller networks ($N_H=5$, 10; 342 and 972 parameters) give slightly higher spectral errors than $N_H=20$ (Table 4) but still below TENO6-A and ALDM (§5.4). **Shown**
25. Cost per cell and time step, $32^3$, NVIDIA RTX A6000, double precision (Table 5): ALDM 327.20 ns, TENO6-A 452.70 ns, ML-ILES 1238.14 ns ($N_H=5$), 1259.10 ns ($N_H=10$), 2004.14 ns ($N_H=20$); the text says "roughly three-times" and "roughly 4.5 times" TENO6-A (§5.4). **Shown** *(Compiler check, not in the sources: $1238.14/452.70=2.73$, $2004.14/452.70=4.43$.)*
26. Training is in single precision; the coarse-grained data and all full-decay runs are in double precision (§4.2, §5). **Stated**
27. The framework "allows for easy extension to more complex training settings without manual derivation and implementation of adjoint equations" (§4.2). **Stated**

The reconstruction in registry notation: at the face $i+\tfrac12$,
$\psi^-_{i+1/2}=\sum_{k=0}^3\mathsf w_kp_k$ with the left-biased candidates
(Eqs. 11–14, as printed) $p_0=\tfrac16(2\bar\psi_{i-2}-7\bar\psi_{i-1}+11\bar\psi_i)$,
$p_1=\tfrac16(-\bar\psi_{i-2}+5\bar\psi_i+2\bar\psi_{i+1})$,
$p_2=\tfrac16(2\bar\psi_i+5\bar\psi_{i+1}-\bar\psi_{i+2})$,
$p_3=\tfrac1{12}(3\bar\psi_i+13\bar\psi_{i+1}-5\bar\psi_{i+2}+\bar\psi_{i+3})$,
applied to the primitive variables, with the overbar here the
finite-volume cell average. TENO6-A sets
$\gamma^{\mathrm T}_k=(1+\tau_6/(\mathrm{IS}_k+\epsilon))^6$,
$\chi^{\mathrm T}_k=\gamma^{\mathrm T}_k/\sum_l\gamma^{\mathrm T}_l$,
$\delta^{\mathrm T}_k=0$ if $\chi^{\mathrm T}_k<C_T$ else 1, and
$\mathsf w_k=d_k\delta^{\mathrm T}_k/\sum_ld_l\delta^{\mathrm T}_l$
(Eqs. 15–18), $C_T$ adapted to local smoothness; ML-ILES outputs
$\mathsf w_k$ directly through the softmax. The loss (Eqs. 41–42) is
$\mathcal L(\boldsymbol\theta)=\sum_{\psi\in\{\rho,\boldsymbol u,p,T\}}\lambda_\psi\frac1{N_T}\sum_{n=1}^{N_T}\frac1{N_xN_yN_z}\sum_{i,j,k}\lvert\psi^{n}_{i,j,k}(\boldsymbol\theta)-\psi^{n,\mathrm{FDNS}}_{i,j,k}\rvert$
with $\lambda_\psi$ the inverse initial reference values; Adam, batch of
24 samples, learning rate $10^{-4}$, 50 epochs. The spectral error
(Eqs. 43–45) averages $\lvert\log(E^{\mathrm{ILES}}_\psi/E^{\mathrm{FDNS}}_\psi)\rvert$
(or its square) over resolved wavenumbers up to $N_x/2$ and over the
decay. The forcing (Eqs. 37–39, modified from Hickel et al.) holds the
energy of the first two shells constant with a solenoidal spectral
term, plus a uniform cooling. $M_t=\sqrt{\langle u_iu_i\rangle}/\langle c\rangle$
and $Re_\lambda=\langle\rho\rangle\sqrt{\langle u_iu_i\rangle}\lambda/\langle\mu\rangle$
use $\sqrt{\langle u_iu_i\rangle}$, not $u_{\mathrm{rms}}$ (Eq. 33), with
$\langle\cdot\rangle$ the volume average.

# Printed slips

- **Eq. (12):** $p^-_{1,i+1/2}=\tfrac16(-\bar\psi_{i-2}+5\bar\psi_i+2\bar\psi_{i+1})$, while Fig. 1a places $S_1$ on $\{i-1,i,i+1\}$. *(Compiler check, not in the sources: for linear data $\bar\psi_j=j$ the printed form gives $i+\tfrac23$, not $i+\tfrac12$; with $\bar\psi_{i-1}$ in the first term it gives $i+\tfrac12$.)*
- **Eq. (10):** the index $\bar\psi_{i-k+l}$, $l=0,\dots,r_k-1$, does not reproduce the stencils of Eqs. (11), (13), (14) and Fig. 1a. *(Compiler check, not in the sources: it gives $S_0=\{i,i+1,i+2\}$, $S_2=\{i-2,i-1,i\}$, $S_3=\{i-3,\dots,i\}$, against $S_0=\{i-2,i-1,i\}$, $S_2=\{i,i+1,i+2\}$, $S_3=\{i,\dots,i+3\}$ of the figure.)*
- **Eq. (34):** $\lambda=\sqrt{\langle u_iu_i\rangle/\langle(\partial u_i/\partial x_i)^2\rangle}$. *(Compiler check, not in the sources: with summation the denominator is the dilatation variance of Eq. (40), so $\tau_\lambda=\lambda/u_{\mathrm{rms}}=\sqrt3/\theta_{\mathrm{rms}}$, about 3.9 at $M_t=0.4$ ($\theta_{\mathrm{rms}}=0.44$) and 0.84 at $M_t=0.8$ ($\theta_{\mathrm{rms}}=2.05$), whereas Table 1 prints $\tau_\lambda\approx0.42$ at all three Mach numbers.)*
- **§4.1 and Fig. 5 caption:** "The Taylor microscale Reynolds number … is $Re_\tau\approx200$", where Eq. (33) and Table 1 define $Re_\lambda$.
- **§3.2:** the wave-speed list "(s−, s+, sL, sK, s∗)" has $s^K$ where Eqs. (23)–(26) define $s^L$, $s^R$; Eq. (28) writes $\lvert S_L\rvert$, $\lvert S_*\rvert$, $\lvert S_R\rvert$ in upper case against $s^L$, $s^*$, $s^R$ of Eqs. (21)–(27).
- **§5.4:** "still achieve lower spectral errors … compared to TENO6-A and ALDM, cf. Table 2"; the spectral errors are in Table 3, Table 2 holding the cell-wise errors.
- **§5.2, Fig. 8 caption:** $p_{\mathrm{rms}}=\langle p'p'\rangle$, without a square root.
- **Typos:** "larger-eddy simulations" (§1), "subrid-scale" (§6).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar\psi_i$, $\bar{\mathbf U}_{i,j,k}$ | cell averages | **collision:** the overbar is the finite-volume cell average, not the LES filter; in Eqs. 25–26 $\bar u$, $\bar c$ are averaged interface states |
| $\langle\cdot\rangle$ | volume average | |
| $\omega_k$, $\alpha_k$, $d_k$ | $\mathsf w_k$, $a_k$, $d_k$ | **collision** of $\omega_k$ with vorticity and specific dissipation rate |
| $\beta_k$, $\gamma_k$, $\chi_k$, $\delta_k$, $C_T$, $\tau_6$, $\varepsilon$ | $\mathrm{IS}_k$, $\gamma^{\mathrm T}_k$, $\chi^{\mathrm T}_k$, $\delta^{\mathrm T}_k$, $C_T$, $\tau_6$, $\epsilon$ | TENO6-A, registry §11 |
| $p_k$, $S_k$ | candidate polynomials and substencils (page-local) | $k=0,\dots,3$, $S_3$ the four-point downwind stencil |
| $\theta$ (network) | $\boldsymbol\theta$ | trainable parameters |
| $\theta$, $\theta_{rms}$ (Eq. 40) | $\nabla\cdot\boldsymbol u$ and its rms | **collision** with the network parameters |
| $\tau_{ij}$ | $\sigma_{ij}$ | viscous stress; no SGS stress exists in the scheme |
| $\epsilon=\langle\sigma_{ij}S_{ij}/\rho\rangle$ | $\varepsilon$ | |
| $\lambda$ | Taylor microscale $\lambda$ (Eq. 34); heat conductivity (Eq. 8) | **collision**; $\lambda_\rho$, $\lambda_{\mathbf u}$, $\lambda_p$, $\lambda_T$ are loss weights |
| $Ma_t$, $Re_\lambda$ | $M_t$, $Re_\lambda$ | velocity scale $\sqrt{\langle u_iu_i\rangle}=\sqrt3u_{\mathrm{rms}}$ |
| $\tau_\lambda$, $\tau$ | $\tau_\lambda$ (page-local) | §5.2 calls $10\tau$ "approximately 10 eddy turn-over times" |
| $\mathcal R=1/(\gamma Ma_t^2)$ | non-dimensional gas constant | the Mach number is set through the sound speed |
| $s^L$, $s^R$, $s^*$, $s^\pm$ | HLLC wave speeds (page-local) | Einfeldt and Batten estimates |
| FDNS | filtered DNS | box filter, factor 16 in space and time |
| "a priori evaluation" | short in-solver rollouts (1–20 steps) | the model runs inside the solver; not the registry's a priori |
| "a posteriori" | a posteriori | full decay |

# Reference list

40 printed references, numbered style. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug. Two items
are bundle sources: [8] [Duraisamy et al. (2019)](/sources/duraisamy-2019.md)
and [15] [Beck & Kurz (2023)](/sources/beck-2023.md). No cited work falls
on the key of a different ingested source. [7], [12] and [15]
print no article number (for [12] and [15] it appears only inside the
printed URLs), [24] prints no volume, [27] (Shu 1998) prints no book title
or publisher, [39] is the Optax software (2020, GitHub URL). No item is
printed twice and none is unparseable.

# Pages created or updated

Chunk 15 (2026-10-28). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Discretization-consistent closure](/definitions/discretization-consistent-closure.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Model-consistent (a posteriori) training of learned closures](/methods/model-consistent-training.md)
- [Neural-network subgrid-scale models](/methods/neural-network-sgs-model.md)
- [Reinforcement-learning turbulence closures](/methods/reinforcement-learning-closure.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)

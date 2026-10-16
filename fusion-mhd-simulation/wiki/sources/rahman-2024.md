---
type: Source
title: "Rahman et al. (2024) — Sparsified time-dependent Fourier neural operators for fusion simulations"
description: "Sparsified Fourier neural operators (ST-FNO), whose layer connectivity follows the field dependencies of the governing equations, are trained on NIMROD two-fluid QH-mode and GTC internal-kink poloidal-plane snapshots, giving 37% and about 2x fewer parameters at baseline accuracy, a claimed 120x memory saving against SuperLU_DIST preconditioning, and a need for frequent retraining when extrapolating in time."
resource: "doi:10.1063/5.0232503"
source_kind: paper
authors: [Rahman M.M., Bai Z., King J.R., Sovinec C.R., Wei X., Williams S., Liu Y.]
year: 2024
venue: "Phys. Plasmas 31:123902"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2024_Crossref_Physics_of_Plasmas_Rahman_Sparsified_time-dependent_Fourier_neural_operators_for_fusio.pdf"
tags: [machine-learning, extended-mhd, hybrid-kinetic, particles, pedestal, kink, tokamak, linear-solver, gpu]
timestamp: 2026-10-16T23:59:00Z
---

# Summary

The paper builds **ST-FNO**, a Fourier-neural-operator surrogate that maps
2D poloidal-plane snapshots of perturbed fields at one time level (or a
window of $k_i$ levels) to the next $k_o$ levels. The baseline FNO lifts all
$n_F$ fields together into one wide channel stack. ST-FNO splits each Fourier
layer into per-equation operators whose inputs are only the fields on which
the evolution equation of the output field depends, with weak dependencies
dropped by hand; the authors relate this to the dependency ordering exploited
by the [semi-implicit leapfrog](/methods/semi-implicit-leapfrog.md) of
[NIMROD](/software/nimrod.md). Two datasets are used: (i) a NIMROD two-fluid
extended-MHD run of a DIII-D quiescent-H-mode edge with carbon and deuterium
ions (10 fields on a 64×64 grid at $\phi=0$, resampled from the finite-element
mesh); (ii) a GTC run of an internal kink in DIII-D #141216 with fluid
electrons and gyrokinetic ions (7 fields, ion velocity moments standing in for
$\delta f_i$), for which the field magnitude is split off and learned by a
separate small network. A per-field relative-$L_2$ loss replaces MSE. The
parameter count falls from 92.8 M to 58.2 M (NIMROD, 37%) and from 45.4 M to
21.2 M (GTC, 2.1×) at test errors close to the baseline. Against the
SuperLU_DIST preconditioner of NIMROD, ST-FNO is claimed to need about 120×
less memory and to supply a cheap initial guess, but it is never coupled to
either code. Train-on-past tests show the surrogate beats persistence only for
3–4 snapshots (NIMROD) or one snapshot in the nonlinear kink phase (GTC), and
autoregressive rollout accumulates error quickly.

# Key claims

1. **Parameter scaling** (§II A). Each Fourier layer holds about
   (width)²×(retained modes)² weights, linear in the retained-mode count and
   quadratic in the hidden width. Stated (heuristic). Compiler's check: the
   printed estimates are a factor of about 4 below Tables I–II (23.0 M
   against 92.8 M for NIMROD), with ratios preserved.
2. **Sparsification** (§II B 2, §II C 2). Count estimates of 252 against 400
   (NIMROD) and 92 against 196 (GTC) in units of (modes)²×(width)² per field;
   measured 58.2 M against 92.8 M (Table I) and 21.2 M against 45.4 M (Table
   II). Derived and Shown. The §III A 1 text value "67.5×10⁶ … 30%" contradicts
   Table I.
3. **Accuracy unchanged** (Figs. 3, 8; Tables I–II). ST-FNO and the baseline
   reach "very similar inference accuracy"; the test curves overlap. Shown.
4. **Loss choice** (§II B 2). MSE is "not a suitable error metric or loss
   function for multi-variable fusion simulation data" because it ignores the
   magnitude differences between fields; the per-field relative $L_2$ error of
   Eq. 5 "can faithfully represent the average relative difference". Stated;
   framed against "many other existing loss functions", citing
   [Gopakumar et al. (2024)](/sources/gopakumar-2024.md). The contrast does
   not hold for that source: Gopakumar et al. already train with a relative
   (squared) $L_2$ loss (their Eq. 11) and use MSE only as a reported
   evaluation metric (compiler's comparison).
5. **Dropped couplings harmless** (§II B 1). Removing the momentum dependence
   on density and the ion-temperature dependence on $\mathbf B$ and density
   "does not significantly affect the model accuracy". Stated ("our
   experiments indicate"); no data shown.
6. **Memory** (§III A 1). ST-FNO about 280 MB; the NIMROD SuperLU_DIST
   preconditioner 34 GB, 9 s factorization and 340 ms application per toroidal
   mode on 64 Perlmutter cores; hence "120× memory reduction" for a
   single-plane estimate. Timings Shown, comparison Stated.
7. **Time** (§III A 1). Inference 5–20 ms per step on one A100; an initial
   guess on the 44 planes needed for 22 toroidal modes costs about 1 s against
   about 7.5 s of SuperLU_DIST application per Krylov iteration, and an
   estimate every 200 steps costs 1 s against about 1400 s of NIMROD. Stated,
   from measured unit costs; it equates an approximate surrogate prediction
   with an exact solver step, and the surrogate is never used as an initial
   guess or preconditioner (future work, §IV).
8. **Spatial error** (§III A 1, Figs. 4–5). Random-split relative differences
   of $10^{-2}$–$10^{-3}$ for most NIMROD fields, largest near the X-point,
   where the poloidal field stagnates. Shown.
9. **Against persistence** (Figs. 6a, 11). One-step inference beats the
   previous-iterate estimate (the last snapshot) by up to 5× for most NIMROD
   test snapshots, and by less in the nonlinear GTC phase. Shown.
10. **Retraining needed** (§III A 2, Fig. 6b–c). Trained on the past, ST-FNO
    beats persistence "for the first 3–4 snapshots, then a retraining of the
    model becomes necessary"; persistence itself degrades after snapshot 250;
    with $k_i=k_o=5$, ST-FNO wins for almost all points at 180, 220, 240
    training snapshots. Shown.
11. **Autoregression accumulates error** (Fig. 6d). Chaining a one-step model
    "will quickly increase the prediction error". Shown.
12. **GTC sequential** (§III B 2, Fig. 11d–f). The field magnitude of the
    linear phase is predicted for the next 30–40 snapshots from 80 training
    samples; in the nonlinear phase only the next snapshot beats persistence,
    "suggesting that retraining is needed for every snapshot". Shown.
13. **GTC random split** (§III B 1, Fig. 11a–c). Magnitude-network error
    $10^{-4}$–$10^{-2}$, normalized-field error about $6\times10^{-2}$, larger
    at the ends of the window (out-of-distribution data); the magnitude spans
    $10^{-5}$–$10^{0}$. Shown.
14. **GTC timing** (§III B 1). Training about 6.78 s per epoch, inference about
    2.00 ms per snapshot (100 GTC steps) against about 0.7 s per GTC step.
    Shown; the implied ratio of about $3.5\times10^4$ is not stated.
15. **Generality** (§II D, Eq. 16). For any system whose time derivatives
    are functions of the fields and their spatial derivatives, the
    connectivity can follow the right-hand-side dependencies on a regular
    grid "regardless of the numerical algorithms being used"; particle data
    enter as moments. Stated.
16. **Closure information** (§II C 1). The learned ion moments "effectively
    [provide] closure information for the kinetic system". Stated, untested.
17. **Limitations** (§IV). Training is expensive; confidence over many output
    steps needs study; coupling to NIMROD would require mapping back to the FEM
    mesh, fully 3D complex-Fourier output and on-the-fly retraining. Stated.

# Models and numerics

**FNO blocks** (§II A, Fig. 1). Inputs are the normalized fields on an
$n_1\times n_2$ grid at $k_i$ levels, padded with the two grid coordinates and
lifted linearly to a hidden width of 20 per field. A Fourier layer takes an
FFT in both directions, keeps the lowest 12 modes per direction, multiplies
them by learned complex weights (the spectral convolution, said to learn the
Green's function), inverts the FFT, adds a 1×1 convolution and applies GeLU; a
projection maps back to $k_o$ output levels. Baseline: four fully coupled
layers. ST-FNO: four layers, each a set of per-equation operators with $m$
inputs and $n$ outputs, about $mn$×(modes)²×(width)² weights each. 500
epochs on one A100 (Perlmutter); optimizer, learning rate and batch size not
given. Code: github.com/liuyangzhuan/STFNO; data: zenodo.org/records/13901806.

**NIMROD model encoded** (§II B 1, Eqs. 1–4), for perturbations about a
steady state, in registry notation:

$$\begin{aligned}
\rho\,(\partial_t\mathbf v+\mathbf v\cdot\nabla\mathbf v) &= \mathbf J\times\mathbf B-\nabla p-\nabla\cdot\mathsf\Pi_i,\\
\partial_t\mathbf B &= \nabla\times\Big[\mathbf v\times\mathbf B+\frac{1}{n_ee}\big(\mathbf J\times\mathbf B-\nabla p_e-\nabla\cdot\mathsf\Pi_e\big)-\eta\mathbf J\Big],\\
\partial_tn_s+\nabla\cdot(n_s\mathbf v) &= \nabla\cdot(D_\perp\nabla n_s)+\nabla\cdot\Big(D_4\,\frac{1}{R^2}\frac{\partial^2}{\partial\phi^2}\nabla n_s\Big),\\
\frac{n_s}{\Gamma-1}\big(\partial_tT_s+\mathbf v_s\cdot\nabla T_s\big) &= -\nabla\cdot\mathbf q_s-p_s\nabla\cdot\mathbf v_s,
\end{aligned}$$

with $\rho=m_dn_d+m_cn_c+m_en_e$, $p=n_eT_e+(n_c+n_d)T_i$ (one ion
temperature), $\mu_0\mathbf J=\nabla\times\mathbf B$, quasineutrality
$n_e=n_d+Z n_c$, $\eta$ Spitzer with a multi-ion collision time, $D_4$ a
$\phi$-directed hyperdiffusivity (page-local), $\mathbf v_s$ the species
velocity and $\mathbf q_s$ the conductive heat flux (page-local; not the
safety factor), with perpendicular, parallel and cross terms. $\mathsf\Pi$
contains perpendicular, parallel and gyro-viscosity and neoclassical
poloidal-flow damping; neoclassical current drive enters through
$\mathsf\Pi_e$. Ten fields: $\mathbf v$, $\mathbf B$, $n_c$, $n_d$, $T_e$,
$T_i$. ST-FNO connectivity (Fig. 1e): $\mathbf v$ from ($\mathbf v$,
$\mathbf B$, $T_e$, $T_i$; density dropped); $n_c$, $n_d$ from ($\mathbf v$,
$n_c$, $n_d$); $\mathbf B$ from ($\mathbf v$, $\mathbf B$; Hall, $\nabla p_e$ and
$1/n_e$ dependencies dropped as subdominant to the ideal advective term);
$T_e$ from 7 inputs and $T_i$ from 4 ($\mathbf v$, $T_i$).

**NIMROD run** (§II B, §III A). 2D high-order finite elements in the poloidal
plane with toroidal Fourier series: 96×256 bi-quartic elements, 22 toroidal
modes, an unmeshed inner core; $\Delta t=5\times10^{-9}$ s, compressional-Alfvén
CFL about 800 and flow CFL about 2; 11 Perlmutter CPU nodes, about 7 s per
step. Algebraic systems preconditioned by SuperLU_DIST
([implicit time integration](/methods/implicit-time-integration.md)). The case
extends King et al. (2017) and Pankin et al. (2020) on a DIII-D QH-mode,
described as "a saturated tokamak edge perturbation"
([ELM](/definitions/edge-localized-mode.md) context). Data: 257 snapshots,
steps 12 000–63 200, one per 200 steps, mapped from $(R,Z)$ to a uniform
64×64 grid in a radial label from the inner to the outer boundary and a
geometric poloidal angle, normalized by the global mean and standard deviation
of each field.

**GTC model encoded** (§II C 1, Eqs. 6–14; Gaussian units as printed). Fluid
electrons and gyrokinetic ions. The [δf](/methods/delta-f-method.md) weight
obeys

$$\frac{dw_p}{dt}=(1-w_p)\Big[-\Big(v_{\parallel p}\frac{\delta\mathbf B_\perp}{B}+\mathbf v_E\Big)\cdot\nabla\ln f_0-\frac{\mu v_{\parallel p}\,\mathbf b\cdot\nabla\langle\delta B_\parallel\rangle}{T_i}+\frac{Z}{T_i}\Big(v_{\parallel p}E_\parallel-\mathbf v_d\cdot\nabla\big(\Phi+\tfrac{\mu}{Z}\langle\delta B_\parallel\rangle\big)\Big)\Big],$$

with $\langle\cdot\rangle$ the gyroaverage. The ion density, parallel flow and
perpendicular and parallel pressures are velocity moments of $\delta f_i$.
Faraday's law $\partial_tA_\parallel=\mathbf b\cdot\nabla(\Phi_{\mathrm{eff}}-\Phi)$,
with an effective potential from the electron density, $\delta B_\parallel$
and the Clebsch displacement of the field; electron continuity with
parallel-flow, E×B, curvature and $\nabla B$ fluxes; Ampère's law for the
electron parallel flow; gyrokinetic Poisson equation for $\Phi$ at the new
level. Seven fields: $\delta n_e$, $\delta n_i$, $\delta u_i$ (ion flow
moment, page-local), $\delta p_{\perp i}$, $\delta p_{\parallel i}$,
$A_\parallel$, $\Phi$; connectivity (Fig. 1g) from 5, 3 (each ion moment), 4
and 2 inputs. Each field is normalized per snapshot by its RMS, and a
two-layer fully connected network maps the log-RMS at one level to the next
(Eq. 15), separating exponential linear growth at fixed pattern from pattern
evolution at fixed amplitude. Data are taken directly on GTC's field-aligned
2D grid.

**GTC run** (§III B). DIII-D #141216 at 1750 ms; mesh 100×250×24 (radial,
poloidal, parallel), $\Delta t=1.483\times10^{-8}$ s, 20 000 steps, $n=0,1$;
3.9 h on 6 Perlmutter GPU nodes. One snapshot per 100 steps, steps
4000–18 800 (149 snapshots); the first 3999 steps dropped as initial noise and
the last 200 as "physically unreliable due to numerical instabilities";
linear-to-nonlinear transition near step 15 300 (snapshot 114). Random split
74 train / 75 test.

**Metrics.** Field loss (Eq. 5): for each field, the square root of the summed
squared $L_2$ error over the output levels divided by the summed squared norm
of the truth, averaged over fields and snapshots. Plot metric (Eq. 17): the
pointwise difference divided by the maximum of the true field. Reference: the
previous iterate (persistence).

# Tests and results

**Table I (NIMROD, random split, $k_o=1$; errors ×10⁻³):**

| Model | $k_i$ | Train | Test | Parameters (M) |
|---|---|---|---|---|
| Baseline FNO | 1 / 3 / 5 | 8.76 / 5.61 / 5.65 | 9.19 / 5.8 / 6.94 | 92.8 |
| ST-FNO | 1 / 3 / 5 | 7.97 / 5.79 / 6.13 | 8.7 / 6.09 / 7.39 | 58.2 |

**Table II (GTC, random split, $k_o=1$; train ×10⁻³, test ×10⁻²):**

| Model | $k_i$ | Train | Test | Parameters (M) |
|---|---|---|---|---|
| Baseline FNO | 1 / 3 / 5 | 9.96 / 9.51 / 8.23 | 1.78 / 1.77 / 1.79 | 45.4 |
| ST-FNO | 1 / 3 / 5 | 10.8 / 7.93 / 7.95 | 1.77 / 1.81 / 1.85 | 21.2 |

* GTC test error is about twice the training error for every model (a
  generalization gap); NIMROD shows none.
* NIMROD: inference 5–20 ms per step; 280 MB; sequential tests with 130, 180,
  220, 240 training snapshots (Fig. 6b); autoregression depths 1–5 from 130
  (Fig. 6d).
* GTC: sequential tests with 80–130 training snapshots (Fig. 11d–f).
* No comparison with other surrogates; no uncertainty or repeat-seed
  statistics.

# Notation map

| Rahman et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $F$, $F_s$, $F^k$, $\bar F$ | words (field, $s$-th field, perturbation at level $k$, prediction) | **collision:** registry $F=RB_\phi$ |
| $n_F$, $k_i$, $k_o$, $k_0$ | $n_F$, $k_i$, $k_o$ (page-local); words | $k_0$ (autoregression depth) collides typographically with $k_o$ |
| $\mathrm P_m$, $\mathrm Q_m$, $\mathrm F_{m,n}$ | words (lifting, projection, Fourier operator) | |
| $W$ (width), $M$ (modes), $R$, $W$ (operators) | words | **collision:** registry $W_{\mathrm{mag}}$, Boozer $M$, major radius $R$ |
| $[F^k]$, $\mathbb K$ | words (RMS, snapshot set) | |
| $\mathbf V$, $\mathbf V_\alpha$, $\mathbf v_e$ | $\mathbf v$, $\mathbf v_s$ (page-local) | |
| $\rho$, $\mathbf B$, $\mathbf J$, $p$, $p_e$, $p_i$ | $\rho$, $\mathbf B$, $\mathbf J$, $p$, $p_e$, $p_i$ | $k_B$ explicit in the paper; registry $T$ in energy units |
| $\boldsymbol\Pi$, $\boldsymbol\Pi_e$ | $\mathsf\Pi_i$, $\mathsf\Pi_e$ | |
| $n_c$, $n_d$, $n_e$, $n_\alpha$; $Z_c$ | $n_s$ ($n_{\mathrm{imp}}$ for carbon); $Z$ | **collision:** registry $Z_c$ is the current-centroid height |
| $D_{n_\alpha}$, $D_{n_\alpha,hypd}$ | $D_\perp$; $D_4$ (page-local) | |
| $\gamma$ (Eq. 4) | $\Gamma$ | **collision:** registry $\gamma$ is a growth rate |
| $\mathbf q_\alpha$ | $\mathbf q_s$ (page-local) | **collision risk** with the safety factor $q$ |
| $r$, $\theta$ (resampling grid) | words | **collision:** native $r\in[0,1]$ runs from the inner boundary of the unmeshed core, not the minor radius |
| $w$ | $w_p$ | **collision:** registry $w$ is an island width |
| $\delta f_i$, $f_{i0}$, $v_\parallel$, $\mu$ | $\delta f$, $f_0$, $v_{\parallel p}$, $\mu$ | |
| $\delta\mathbf B_\perp$, $\delta B_\parallel$, $A_\parallel$/$\delta A_\parallel$ | $\delta\mathbf B_\perp$, $\delta B_\parallel$, $A_\parallel$ | used interchangeably as printed |
| $\phi$ (GTC), $\phi_{\mathrm{eff}}$ | $\Phi$, $\Phi_{\mathrm{eff}}$ (page-local) | **collision:** registry $\phi$ is the toroidal angle |
| $\mathbf v_E$, $\mathbf v_d$, $\mathbf v_*$ | $\mathbf v_E$, $\mathbf v_d$, $\mathbf v_{\mathrm{dia},s}$ | |
| $\hat{\mathbf b}_0$, $B_0$, $B_0^*$ | $\mathbf b$, $B$, $B^*_\parallel$ | |
| $\boldsymbol\kappa$ | words (field-line curvature) | **collision:** registry $\kappa$ is a conductivity |
| $\langle\langle\cdot\rangle\rangle$ | $\langle\cdot\rangle$ | gyroaverage |
| $n_i$, $u_i$, $\delta P_{\perp i}$, $\delta P_{\parallel i}$ | $\delta n_i$, $\delta u_i$ (page-local), $\delta p_{\perp i}$, $\delta p_{\parallel i}$ | |
| $\psi$, $\alpha_0$, $\delta\psi$, $\delta\alpha$ | $\psi$; words (Clebsch coordinates) | normalization of $\psi$ not stated |
| $\rho_i$ | $\rho_L$ | **collision:** registry $\rho$ is mass density |
| $Z_i$, $Z_s$, $\Omega_e$ | $Z$, $\Omega_e$ | |
| $\Delta t_m$, $\Delta t$ | $\Delta t$ | |
| $\mathbf F$, $\mathscr L$ (Eq. 16) | words | **collision:** registry $\mathcal L$ is a linearized operator, $\mathbf u$ the discrete state |

# Pages created or updated

Chunk 3 (2026-10-16) created or updated the pages below. This source is cited on:

* [Fourier neural operator surrogates of MHD simulations](/methods/fourier-neural-operator-surrogates.md)
* [Implicit time integration and preconditioned Krylov solvers for nonlinear MHD](/methods/implicit-time-integration.md)
* [NIMROD](/software/nimrod.md)
* [Semi-implicit leapfrog](/methods/semi-implicit-leapfrog.md)
* [Single-fluid visco-resistive MHD model](/methods/visco-resistive-mhd-model.md)
* [The δf particle method](/methods/delta-f-method.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2024_Crossref_Physics_of_Plasmas_Rahman_Sparsified_time-dependent_Fourier_neural_operators_for_fusio.pdf`
   * **Version.** Publisher version of record (AIP, open access CC BY) with
     the AIP download cover: 13 PDF pages, cover plus article pages
     123902-1 to -12. Submitted 8 August 2024, accepted 12 November, online
     4 December 2024.
   * **Identity.** doi:10.1063/5.0232503, checked on Crossref: title, seven
     authors, Phys. Plasmas 31(12), article 123902, December 2024, 41
     references.
   * **How read.** Full text; equations and tables read in full; plot values
     are the reader's approximate readings.
   * **Recorded as printed.**
     * §III A 1 gives the ST-FNO size as "67.5×10⁶ … 30% model size
       reduction"; Table I gives 58.2 M (37% below 92.8 M), matching the
       252/400 estimate.
     * "Up to 2× parameter reduction" (§I) and "a factor of 2" (abstract) hold
       for GTC (2.14×); the NIMROD reduction is 1.6×.
     * §III A 2: "time step 56 000 (snapshot 131)"; with snapshot 1 at step
       12 000 and 200 steps per snapshot this is snapshot 221 (snapshot 131 is
       the GTC step 17 000 of Fig. 12); the sentence repeats 130 and 180
       training snapshots for both times.
     * Persistence for $k_i=k_o=5$ is defined as the snapshot $k-5$, then said
       to use "only snapshot $k-1$".
     * The autoregression depth $k_0$ is called $k_o$ "varying from 1 to 5"
       (§III A 2).
     * Fig. 1(b) caption: "$k_o=1$, $k_o=1$" for $k_i=1$, $k_o=1$.
     * §II A: the final projection is called $\mathrm P_m$ (the lifting
       operator) instead of $\mathrm Q_m$; post-IFFT dimensions printed with
       $nW$ for $mW$.
     * Fig. 1(e): the two temperature rows swap order between inputs and
       outputs; the mapping of the 4-input operator to $T_i$ matches the text.
     * Parameter estimates a factor of about 4 below the tabulated counts
       (compiler's check, Key claim 1).
     * "the training time per epoch is about three to tens" (§III A 1,
       confirmed on the rendered page).
     * Eq. 15 has a prefactor $1/n_F$ only, so it sums rather than averages
       over snapshots.
     * §III B 1: "snapshots 4000 and 18 800" are time steps (snapshots 1 and
       149).
     * Naming drift: $\delta n_i$, $\delta u_i$ against $n_i$, $u_i$ in Eqs.
       7–8; $A_\parallel$ and $\delta A_\parallel$ both used; Eq. 13 text names
       $\delta u_e$, the equation has $u_{\parallel e}$; $\mathbf v_d$ is called
       a "drift current".
     * Eqs. 7–10 use an unsubscripted $m$ and $B_0^*$; Eq. 14's left side
       $Z_i^2\rho_i^2/T_i$ times a density relies on an unstated unit
       convention.
     * Speed-up comparisons set a surrogate forward pass against exact
       per-iteration and per-step solver costs; the surrogate's error,
       retraining, training time and data generation are not costed.
     * Fig. 3 shows $k_o=5$ cases; Tables I–II report only $k_o=1$.
   * **Reference list.** 41 printed entries (1–41, no DOIs), merged into the
     bibliography under `rahman-2024`. Key decisions: the FNO paper (ref. 12,
     "2020b") is `li-2020-c` and PINO (ref. 31, printed 2021, A. Stuart
     omitted) is `li-2022-b`, shared with `gopakumar-2024`; Li J. et al.
     (ref. 8, GTC tearing, "2020a") is `li-2020-b`; GPTune (ref. 14) is
     `liu-2021-c`; refs. 29 and 41 ("2023a/b") are `li-2023` (geo-FNO) and
     `li-2023-b` (SuperLU_DIST); ref. 24 is the ingested `gopakumar-2024`;
     Rosofsky et al. (arXiv 2302.08332, "Magnetohydrodynamics
     with physics informed neural operators") is `rosofsky-2023-b`, a
     different work from `rosofsky-2023` (MLST 4:025022, cited by
     `gopakumar-2024`), with which it had been wrongly merged; pre-publication citations are kept as distinct entries (human ruling 2026-10-16);
     reused keys include `sovinec-2004`, `sovinec-2010`, `king-2017`,
     `pankin-2020`, `lin-1998`, `hoelzl-2021` and `howell-2022`. Ref. 18 lacks
     an opening quotation mark; ref. 25 ends "and on behalf of JET
     Contributors"; ref. 26 is a chapter of Gottlieb & Orszag (1977);
     publisher lower-casing ("gene", "elms", "nimrod", "superlu") is kept.

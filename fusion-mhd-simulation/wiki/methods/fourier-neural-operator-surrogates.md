---
type: Method
title: "Fourier neural operator surrogates of MHD simulations"
description: "Neural operators that learn the snapshot-to-snapshot map of 2D poloidal-plane fields of MHD-type codes through truncated-Fourier convolution layers, as fully coupled multi-variable models trained on JOREK blob runs and MAST camera movies or as equation-sparsified models (ST-FNO) trained on NIMROD and GTC runs, with their error metrics, the persistence baseline, rollout error growth and speed-up claims whose protocols do not compare like with like."
status: established
aliases: [FNO, Fourier neural operator, multi-variable FNO, ST-FNO, sparsified time-dependent FNO, neural-operator surrogate, data-driven surrogate]
tags: [verification, numerics, machine-learning, reduced-mhd, extended-mhd, edge]
timestamp: 2026-10-16T18:00:00Z
---

# Fourier neural operator surrogates of MHD simulations

A Fourier neural operator (FNO) is a neural network that approximates an
operator between function spaces, here the map from the fields of a
simulation at one or a few past instants to the fields at the next instants.
Its hidden layers convolve a latent field with a learned kernel by
multiplication in Fourier space, keeping only the lowest Fourier modes. Two
sources of this bundle train FNOs on 2D poloidal-plane data of MHD-type codes:
[Gopakumar et al. (2024)](/sources/gopakumar-2024.md) on
[JOREK](/software/jorek.md) runs of a field-free fluid model and on MAST
fast-camera movies, and [Rahman et al. (2024)](/sources/rahman-2024.md) on a
[NIMROD](/software/nimrod.md) two-fluid edge run and a GTC gyrokinetic
internal-kink run. Neither couples the surrogate back into the code it
emulates: both evaluate it offline against held-out snapshots of the same run
or dataset.

## Page-local notation

The registry ([notation](/notation.md)) has no machine-learning symbols, and
the source symbols clash with it ($\kappa$, $\phi$, $\nu$, $u$, $R$, $T$,
$W$, $M$). This page uses its own symbols, defined only here:
$\mathcal G_{\vartheta}$ the learned operator with trainable parameters
$\vartheta$ (not the poloidal angle $\theta$); $\mathsf h_\ell$ the latent
field after layer $\ell$ and $d_{\mathrm h}$ its width (channels per field);
$\mathsf W_\ell$ the local (pointwise or small-stencil) linear map,
$\mathsf R_\ell$ the complex spectral weights and $\mathsf b_\ell$ the bias of
layer $\ell$; $\sigma_{\mathrm a}$ the activation (GELU in both sources);
$\mathfrak F$ the discrete Fourier transform over the two spatial directions;
$k_{\max}$ the number of retained Fourier modes per direction;
$\mathbf y^{j}$ the stacked normalized fields at snapshot $j$, $y^{j}_\lambda$
its $\lambda$-th field, $\tilde{\mathbf y}^{j}$ the prediction;
$N_{\mathrm F}$ the number of fields; $N_{\mathrm{in}}$ and $N_{\mathrm{out}}$
the input and output snapshots per pass; $\|\cdot\|_2$ the $L_2$ norm of the
vectorized grid array.

## Architecture

Both sources use the same three-stage FNO: a pointwise lifting of the input
(fields at $N_{\mathrm{in}}$ snapshots plus the grid coordinates) to width
$d_{\mathrm h}$, a stack of Fourier layers, and a pointwise projection to the
$N_{\mathrm{out}}$ output snapshots
([Gopakumar et al. (2024)](/sources/gopakumar-2024.md), §2.3, Eqs. 4–8, App. B;
[Rahman et al. (2024)](/sources/rahman-2024.md), §II A, Fig. 1). A Fourier
layer is
$$\mathsf h_{\ell+1}=\sigma_{\mathrm a}\Big(\mathsf W_\ell\,\mathsf h_\ell+\mathfrak F^{-1}\big[\mathsf R_\ell\cdot\mathfrak F\mathsf h_\ell\big]_{k_{\max}}+\mathsf b_\ell\Big),$$
where $[\cdot]_{k_{\max}}$ discards every mode above $k_{\max}$ per direction.
The spectral term is a global convolution with a learned kernel; Rahman et al.
describe it as learning "the underlying Green's function". Gopakumar et al.
add a learned linear map of the grid coordinates inside every layer, and
skip connections whose placement the equations do not give (Eq. 8, Fig. 4).
Configurations:

| | Gopakumar et al. (2024), JOREK | Gopakumar et al. (2024), cameras | Rahman et al. (2024), NIMROD and GTC |
|---|---|---|---|
| Fourier layers | 6 | 6 | 4 |
| $k_{\max}$ | 16 (ablation 2–32) | 8 | 12 |
| width | 32 | 16 | 20 per field |
| $N_{\mathrm{in}}\to N_{\mathrm{out}}$ | $10\to5$, rolled out to 50 instants | $10\to10$, sliding window | $1,3,5\to1$ (also 5) |
| grid | $100\times100$ regular | $448\times640$, $400\times512$ | $64\times64$ $(r,\theta)$; GTC $(\psi,\theta)$ grid |
| parameters | 6.3 M (2 fields), 9.5 M (3 fields) | 0.20 M | 92.8 M / 58.2 M (NIMROD), 45.4 M / 21.2 M (GTC), baseline / ST-FNO |

(Gopakumar et al., Tables 2, B1, D1–D2; Rahman et al., §III, Tables I–II.)
All training in both papers runs on one Nvidia A100. Neither model is
physics-informed: there is no PDE residual or conservation constraint in the
loss (Gopakumar et al., §2.3; Rahman et al., Eqs. 5, 15).

**Cost of the spectral weights.** Rahman et al. estimate the parameters of a
Fourier layer that maps $m_{\mathrm{in}}$ fields to $m_{\mathrm{out}}$ fields
as $\approx m_{\mathrm{in}}m_{\mathrm{out}}k_{\max}^2d_{\mathrm h}^2$, so a
fully coupled layer costs $N_{\mathrm F}^2k_{\max}^2d_{\mathrm h}^2$: linear in
the retained-mode count, quadratic in the width (§II A). The estimate
reproduces the tabulated ratios but is a factor of about 4 below the tabulated
counts, e.g. $400\,k_{\max}^2d_{\mathrm h}^2=23.0$ M against 92.8 M
([Rahman et al. (2024)](/sources/rahman-2024.md), reader's check; the factor is
consistent with complex weights on two retained frequency corners, which the
paper does not state). Gopakumar et al. give the cost of the layer as
$O(n\,k_{\max})$ for $n$ grid points, although the transform itself stays
$O(n\log n)$; truncation reduces only the weight multiplication (§2.3.1,
reader's note).

## Coupling between fields: dense, absent, or equation-sparsified

How the $N_{\mathrm F}$ coupled fields share a model is the design choice the
two papers differ on.

- **Multi-variable FNO** ([Gopakumar et al. (2024)](/sources/gopakumar-2024.md),
  §2.3.3). The fields form a separate tensor axis, the transform acts per field
  over space, $\mathsf R_\ell$ is extended to the field axis, and
  $\mathsf W_\ell$ is a 3D convolution over field and space axes, so one
  model learns all couplings. Against single-field FNOs of the same parameter
  count it is reported to lower the rollout error of density and temperature
  in all three JOREK cases (§3.1.4, Fig. 11); see Qualifications for the
  potential.
- **Fully coupled baseline and ST-FNO**
  ([Rahman et al. (2024)](/sources/rahman-2024.md), §II B 2, §II C 2, §II D).
  The baseline lifts all fields into one channel stack, coupling every field
  to every other in every layer. ST-FNO (sparsified time-dependent FNO)
  replaces each layer by a set of operators, one per evolution equation, fed
  only by the fields on that equation's right-hand side, with weak
  dependencies dropped by hand. For the ten NIMROD fields
  ($\mathbf v$, $\mathbf B$, two ion densities, $T_e$, $T_i$) the operators are
  $\mathbf v\leftarrow(\mathbf v,\mathbf B,T_e,T_i)$ (density dropped),
  $(n_{\mathrm C},n_{\mathrm D})\leftarrow(\mathbf v,n_{\mathrm C},n_{\mathrm D})$,
  $\mathbf B\leftarrow(\mathbf v,\mathbf B)$ (Hall, $\nabla p_e$ and $1/n_e$
  terms dropped as subdominant to ideal advection), $T_e\leftarrow(\mathbf v,\mathbf B,T_e)$
  and $T_i\leftarrow(\mathbf v,T_i)$ (the $T_e$ inputs inferred by the
  compiler from the operator size, seven input fields; the figure orders the
  temperature rows inconsistently), giving
  $4\times(24+10+18+7+4)=252$ against $4\times10^2=400$ units of
  $k_{\max}^2d_{\mathrm h}^2$. For the seven GTC fields (electron density,
  four ion moments standing in for the ion $\delta f$, $A_\parallel$,
  $\Phi$) the count is $92$ against $196$ (Fig. 1e, 1g). The authors state
  that the connectivity "exploits the same structure of the MHD equations"
  as NIMROD's [semi-implicit leapfrog](/methods/semi-implicit-leapfrog.md)
  (§II B 2). Measured, ST-FNO reaches the baseline's test error with 37 %
  fewer parameters for NIMROD and 2.1 times fewer for GTC
  (Tables I–II, below). Dropping the momentum dependence on density and the
  ion-temperature dependence on $\mathbf B$ and density "does not
  significantly affect the model accuracy", stated without data (§II B 1).

Rahman et al. generalize the construction to any system
$\partial_t\mathbf y=\mathcal N(\mathbf y,\nabla\mathbf y,\nabla^2\mathbf y,\dots)$
on a regular grid, the operator for each field following the dependencies of
its right-hand side $\mathcal N$, with particle data replaced by moments
(§II D, Eq. 16). The two papers together span dense, absent (single-field)
and sparsified coupling, but neither compares all three: Gopakumar et al.
compare dense with absent, Rahman et al. dense with sparsified (compiler's
observation).

## Training data

| Data | Physics and grid | Dataset | Source |
|---|---|---|---|
| JOREK isothermal blob | field-free fluid model, $\rho$ and $u$ | 120 runs (100 train) | [Gopakumar et al. (2024)](/sources/gopakumar-2024.md), §2.1, Table 1 |
| JOREK blob with temperature | $\rho$, $u$, $T$ | 120 runs (Table 2: 160 train) | idem |
| JOREK 1–10 blobs with temperature | $\rho$, $u$, $T$ | 2000 runs (1500 train) | idem |
| MAST visible cameras | rbb (central-solenoid view), rba (lower divertor) | 55 and 48 shots of the M9 campaign | idem, §3.2, App. G |
| NIMROD, DIII-D QH-mode edge, two-fluid with C and D ions | 10 perturbed fields at $\phi=0$, resampled to $64\times64$ $(r,\theta)$ | 257 snapshots, one per 200 steps | [Rahman et al. (2024)](/sources/rahman-2024.md), §II B, §III A |
| GTC, DIII-D #141216 internal kink, fluid electrons and gyrokinetic ions | 7 perturbed fields on GTC's field-aligned $(\psi,\theta)$ grid | 149 snapshots, one per 100 steps | idem, §II C, §III B |

**JOREK data.** The model is JOREK reduced MHD with all magnetic fields and
currents set to zero, "similar to the Euler system": in canonical symbols
$\partial_t\rho=-\nabla\cdot(\rho\mathbf v)+D_\perp\nabla^2\rho$,
$\rho\,\partial_t\mathbf v=-\rho\mathbf v\cdot\nabla\mathbf v-\nabla p+\nu\nabla^2\mathbf v$,
$\partial_tp=-\mathbf v\cdot\nabla p-\Gamma p\nabla\cdot\mathbf v+\kappa_\perp\nabla^2T$
with isotropic coefficients, $\Gamma=5/3$, the poloidal ansatz
$\mathbf v=R^2\nabla\phi\times\nabla u$ and vorticity $\nabla^2u$
([Gopakumar et al. (2024)](/sources/gopakumar-2024.md), §2.1, Eqs. 1–3; the
native "density" is quoted in m$^{-3}$, i.e. used as a number density). Blobs
in a 1 m square slab centred at $R=10$ m move outward by buoyancy; in the
isothermal case buoyancy and inertia both scale with density, so every blob
moves at the same speed. Each run has $200\times200$ bicubic elements,
$\Delta t=0.15\,\mu$s and 2000 steps (300 µs), downsampled to 200 instants and
a $100\times100$ grid, and costs about 350 core-hours (§2.1). The two
datasets are thus 2D, axisymmetric and, for JOREK, free of magnetic field.

**Normalization.** Gopakumar et al. divide each field by the order of
magnitude of its training maximum and then scale it linearly to $[-1,1]$
(§2.3). Rahman et al. subtract the global mean and divide by the standard
deviation per field for NIMROD; for GTC they divide each snapshot by its RMS
and learn the logarithm of the RMS with a separate two-layer fully connected
network, to separate exponential linear growth at fixed pattern from the
fixed-amplitude, evolving pattern of the nonlinear phase (§II C 2, Eq. 15).

## Losses and error metrics

Gopakumar et al. train with a relative-$L_2$ reconstruction term plus an
equally weighted "difference" term on temporal increments,
$$\mathrm{loss}=\frac{1}{N_{\mathrm s}}\sum_{\text{samples}}\left(\sum_{j}\frac{\|\tilde{\mathbf y}^{j}-\mathbf y^{j}\|_2^2}{\|\mathbf y^{j}\|_2^2}+\sum_{j}\frac{\big\|(\tilde{\mathbf y}^{j+N_{\mathrm{out}}}-\tilde{\mathbf y}^{j})-(\mathbf y^{j+N_{\mathrm{out}}}-\mathbf y^{j})\big\|_2^2}{\|\mathbf y^{j+N_{\mathrm{out}}}-\mathbf y^{j}\|_2^2}\right)$$
over $N_{\mathrm s}$ samples ([Gopakumar et al. (2024)](/sources/gopakumar-2024.md),
Eq. 11), with backpropagation through the autoregressive rollout. They report
MSE in the normalized domain (Table 2) and MAE in the figures. Rahman et al.
argue that MSE "is not a suitable error metric or loss function for
multi-variable fusion simulation data" because it does not distinguish the
magnitudes of different fields, and use the per-field relative error averaged
over fields and snapshots,
$$\mathrm{loss}=\frac{1}{N_{\mathrm F}|\mathbb K|}\sum_{j\in\mathbb K}\sum_{\lambda=1}^{N_{\mathrm F}}\left(\frac{\sum_{k=1}^{N_{\mathrm{out}}}\|y_\lambda^{j+k}-\tilde y_\lambda^{j+k}\|_2^2}{\sum_{k=1}^{N_{\mathrm{out}}}\|y_\lambda^{j+k}\|_2^2}\right)^{1/2},$$
with $\mathbb K$ the set of snapshot indices
([Rahman et al. (2024)](/sources/rahman-2024.md), §II B 2, Eq. 5).

**Persistence baseline.** Rahman et al. compare every prediction with the
"previous iterate" $\tilde{\mathbf y}^{j}=\mathbf y^{j-1}$, i.e. with doing
nothing (§III). Gopakumar et al. have no such baseline and no comparison with
another surrogate in this paper; an earlier workshop version found FNOs better
than ConvLSTM and U-Net on blob diffusion (§1, citing Gopakumar et al. 2023).

## Results

**Accuracy on held-out data (random splits).**

| Case | Model | Error | Source |
|---|---|---|---|
| JOREK isothermal blob | multi-variable FNO | MSE $7.58\times10^{-5}$ (normalized) | [Gopakumar et al. (2024)](/sources/gopakumar-2024.md), Table 2 |
| JOREK blob with temperature | multi-variable FNO | MSE $2.56\times10^{-5}$ | idem |
| JOREK multi-blob | multi-variable FNO | MSE $1.33\times10^{-4}$ | idem |
| MAST rbb, rba cameras | single-field FNO | MSE $1.97\times10^{-3}$, $3.80\times10^{-3}$ | idem |
| NIMROD QH-mode, $N_{\mathrm{in}}=1,3,5$ | baseline / ST-FNO | test loss $(9.19,5.8,6.94)$ / $(8.7,6.09,7.39)\times10^{-3}$ | [Rahman et al. (2024)](/sources/rahman-2024.md), Table I |
| GTC kink, $N_{\mathrm{in}}=1,3,5$ | baseline / ST-FNO | test loss $(1.78,1.77,1.79)$ / $(1.77,1.81,1.85)\times10^{-2}$ | idem, Table II |

The GTC test loss is about twice the training loss for every model, the
NIMROD one is not (Rahman et al., Tables I–II, reader's note). NIMROD
pointwise errors are $10^{-2}$–$10^{-3}$ of the field maximum for most
fields, largest near the X-point, a stagnation point of the poloidal field
with "differing dynamics" (§III A 1, Figs. 4–5). One-step predictions beat
the persistence baseline by up to a factor 5 for most NIMROD test snapshots
and by less in the nonlinear GTC phase (Figs. 6a, 11).

**Extrapolation in time.** Trained on the past and tested on the future
(sequential split), the NIMROD ST-FNO beats persistence "for the first 3–4
snapshots, then a retraining of the model becomes necessary"; with
$N_{\mathrm{in}}=N_{\mathrm{out}}=5$ it beats persistence at almost all
points for 180–240 training snapshots
([Rahman et al. (2024)](/sources/rahman-2024.md), §III A 2, Fig. 6b–c). For
GTC, 80 training snapshots predict the amplitude of the linear phase for the
next 30–40 snapshots, but in the nonlinear phase ST-FNO beats persistence for
one snapshot only, "suggesting that retraining is needed for every snapshot"
(§III B 2, Fig. 11d–f).

**Rollout error growth.** Chaining a one-step model "will quickly increase
the prediction error due to error accumulation"
([Rahman et al. (2024)](/sources/rahman-2024.md), §III A 2, Fig. 6d). In the
JOREK multi-blob case the physical-space MAE grows almost linearly over the
rollout from instant 10 to 50: density from about $0.25$ to
$1.8\times10^{18}$ m$^{-3}$, potential from about 4 to 44, temperature from
about 0.05 to 0.37 eV; a model rolled out to 200 instants "quickly loses
grip" and gives "noisy, incoherent output"
([Gopakumar et al. (2024)](/sources/gopakumar-2024.md), §3.1.3, Fig. 10,
App. C). With five output instants per pass the error spikes at multiples of
the output size; the pushforward trick is cited as a remedy but not applied
(§3.1.5, Fig. 12).

**Ablations** ([Gopakumar et al. (2024)](/sources/gopakumar-2024.md)).
The error falls with $k_{\max}$ and saturates at 8 modes; 8, 16 and 32 modes
are indistinguishable (§3.1.6, Figs. 13–14). On the multi-blob set the test
MAE falls from about $6.2\times10^{-3}$ at 250 training runs to about
$3.4\times10^{-3}$ at 1500 and rises slightly at 1750, while training time
grows linearly; about 500 runs suffice (§3.1.7, Figs. 15–16). A model trained
on $100\times100$ and evaluated on $500\times500$ without retraining gives MSE
$7.90\times10^{-5}$ (zero-shot super-resolution, §3.1.8, Fig. 17); how the
$500\times500$ reference was produced from the $200\times200$-element run is
not stated (reader's note). Initial conditions outside the training
distribution (13 blobs, twice the maximum amplitude) are predicted correctly
only at the first output instant (§3.1.9, Fig. 18).

**Camera forecasts.** The camera FNO follows ramp-up, L-mode, H-mode and the
L–H transition and locates plasma–wall contact regions, but smooths out ELM
filaments (see [edge-localized mode](/definitions/edge-localized-mode.md)) and
cannot time the transition, being "a regression model and not a
classification model"; it predicts the next 12 ms of frames in 6 ms, with no
hardware or latency breakdown
([Gopakumar et al. (2024)](/sources/gopakumar-2024.md), §3.2). This
application emulates experimental images, not an MHD code.

## Cost claims and their protocols

- **"Six orders of magnitude"**
  ([Gopakumar et al. (2024)](/sources/gopakumar-2024.md), abstract, §3.1.1).
  The comparison is 0.025–0.03 s of FNO inference for a rollout against the
  "approximately 350 core hours" of a JOREK run; no timing protocol is given.
  At 48 cores, 350 core-hours is about 7.3 h of wall time, about $10^6$ times
  0.025 s; but the rollout covers the first 50 of the 200 stored instants, a
  quarter of the run, so at equal simulated time the ratio is about
  $2.2$–$2.6\times10^5$; core-seconds against GPU-seconds would give about
  $5\times10^7$ (compiler's arithmetic from the printed numbers). Training
  (up to 11 h for the JOREK cases) and data generation (2000 runs × 350 core-hours, about
  $7\times10^5$ core-hours) are excluded.
- **Against NIMROD's preconditioner**
  ([Rahman et al. (2024)](/sources/rahman-2024.md), §III A 1). ST-FNO needs
  about 280 MB, against 34 GB for the SuperLU_DIST factorization that
  preconditions NIMROD's solves per toroidal mode, "120× memory reduction".
  An estimate on the 44 planes needed for 22 toroidal modes takes about
  $20\ \mathrm{ms}\times44\approx1$ s, against about 7.5 s of preconditioner
  application per Krylov iteration; a field estimate every 200 steps costs
  1 s against about 1400 s of NIMROD stepping. These compare an approximate
  forward pass with exact solver operations; the surrogate is never used as
  an initial guess or preconditioner in the paper (future work, §IV), and its
  $\sim10^{-2}$ error and retraining cost are not costed (reader's note). See
  [implicit time integration](/methods/implicit-time-integration.md).
- **GTC.** ST-FNO infers one snapshot (100 GTC steps) in about 2.0 ms and
  trains at about 6.8 s per epoch; GTC averages about 0.7 s per step (§III B 1).
  The implied ratio of about $3.5\times10^4$ per snapshot is not stated by the
  paper and sets one A100 against six GPU nodes (reader's arithmetic).

## Limits stated by the sources

- **Two dimensions only.** Scaling to 3D is not demonstrated; GPU memory, the
  cost of 3D training data and the choice of operator basis are the stated
  obstacles ([Gopakumar et al. (2024)](/sources/gopakumar-2024.md), §3.1.10).
  Coupling ST-FNO into NIMROD would need a map back to the finite-element mesh,
  a fully 3D complex-Fourier output and automatic on-the-fly retraining
  ([Rahman et al. (2024)](/sources/rahman-2024.md), §IV).
- **No physics validation.** Neither paper checks conservation, energy or a
  physical scaling of the predicted fields; errors are reported only as norms
  of the field difference ([Gopakumar et al. (2024)](/sources/gopakumar-2024.md),
  §3; Rahman et al., §III). Rahman et al. state that the learned ion moments
  "effectively [provide] closure information for the kinetic system", which
  nothing in the paper tests (§II C 1).
- **No uncertainty estimate.** No repeat-seed statistics or prediction
  confidence; Rahman et al. list the confidence of many-step prediction as
  open (§IV).

## Qualifications

- **Multi-variable claim and Fig. 11(b).** Gopakumar et al. state "much better
  performance" of the multi-variable FNO without qualification (§3.1.4), but
  in their Fig. 11(b) (single blob with temperature) the multi-variable
  potential error oscillates up to about 0.009 MAE, above the single-field
  potential curve. The claim holds as shown for density and temperature, not
  for the potential in that case. Comparisons are valid only within one field,
  since each field has its own normalization (§3.1.4; reader's note).
- **Parameter counts of ST-FNO.** The text of
  [Rahman et al. (2024)](/sources/rahman-2024.md) (§III A 1) gives 67.5 M
  parameters and a 30 % reduction for the NIMROD ST-FNO; Table I gives 58.2 M
  against 92.8 M, a 37 % reduction, which matches the 252/400 estimate. This
  page follows the table. The "up to 2×" reduction of the abstract holds for
  GTC (2.14×); the NIMROD reduction is 1.6×.
- **Printed accuracy and cost values of Gopakumar et al.** The abstract quotes
  normalized MSE $\approx10^{-5}$, §3 "$\sim10^{-4}$", Table 2
  $2.56\times10^{-5}$–$1.33\times10^{-4}$. For the rba camera Table 2 gives
  MSE $3.80\times10^{-3}$ and §3.2.3 $1.70\times10^{-4}$; training times and
  pair counts of both cameras also differ between table and text (Table 2;
  §3.2.2–3.2.3). The table values are quoted here.
- **Loss design.** Rahman et al. contrast their Eq. 5 with "many other existing
  loss functions", citing Gopakumar et al. (§II B 2). Gopakumar et al. already
  train on a relative-$L_2$ loss of per-field normalized data and report MSE
  only as an evaluation metric; their relative norm, however, is taken over
  all fields at once, while Eq. 5 normalizes each field separately (compiler's
  reading of the two equations). The disagreement is about the reported
  metric and per-field weighting, not about MSE as a training loss.
- **Version read.** Gopakumar et al. were read as arXiv v2 (June 2024, posted
  after publication); numbers are cited by section, figure and table.

# Citations

- [Gopakumar et al. (2024)](/sources/gopakumar-2024.md) — §1, §2.1, §2.3, §2.3.1, §2.3.3, §3.1.1–3.1.10, §3.2, Eqs. 1–3, 8, 11, Tables 1–2, B1, D1–D2, Figs. 10–18, App. C, G.
- [Rahman et al. (2024)](/sources/rahman-2024.md) — §II A–D, §III A–B, §IV, Eqs. 5, 15–16, Tables I–II, Figs. 1, 4–6, 11.

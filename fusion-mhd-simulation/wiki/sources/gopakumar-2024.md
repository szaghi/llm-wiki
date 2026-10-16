---
type: Source
title: "Gopakumar et al. (2024) — Plasma surrogate modelling using Fourier neural operators"
description: "Multi-variable Fourier neural operators trained on 2D field-free JOREK blob simulations and on MAST fast-camera movies reach normalised MSE of 1e-5 to 1e-4, roll out 50 steps in 0.03 s (claimed six orders of magnitude faster than JOREK), super-resolve zero-shot and forecast 12 ms of camera frames in 6 ms."
resource: "doi:10.1088/1741-4326/ad313a"
source_kind: paper
authors: [Gopakumar V., Pamela S., Zanisi L., Li Z., Gray A., Brennand D., Bhatia N., Stathopoulos G., Kusner M., Deisenroth M.P., Anandkumar A., JOREK Team, MAST Team]
year: 2024
venue: "Nucl. Fusion 64:056025"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2024_Crossref_Nuclear_Fusion_Gopakumar_Plasma_surrogate_modelling_using_Fourier_neural_operators.pdf"
tags: [machine-learning, reduced-mhd, edge, tokamak, gpu]
timestamp: 2026-10-16T00:00:00Z
---

# Summary

The paper trains Fourier neural operators (FNO) as data-driven surrogates
for two "solvers". The first is [JOREK](/software/jorek.md) run in 2D (one
poloidal plane) with a field-free fluid model: the reduced model of
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md) with all magnetic fields and
currents set to zero, close to an Euler system. Axisymmetric density blobs in
a 1 m × 1 m slab centred at $R=10$ m move outward by buoyancy and diffuse.
Three datasets of rising complexity are built: a single isothermal blob
(density and potential), a single blob with non-uniform temperature, and 1 to
10 blobs with non-uniform temperature (2000 runs). The second is the visible
fast-camera data of MAST (central-solenoid view rbb, lower-divertor view rba;
M9 campaign). The methodological contribution is a **multi-variable FNO**:
the physical fields form a separate tensor axis, so one model learns all
coupled fields, and a 3D convolution mixes the field and spatial axes. The
simulation surrogate is an FNO-2d (Fourier transform in space only) rolled
out autoregressively from 10 input steps to 50 output steps, 5 per pass,
trained with a relative-$L_2$ reconstruction loss plus a loss on temporal
increments. The camera surrogate maps a sliding window of 10 frames to the
next 10, without feeding back its outputs. Normalised-domain MSE is
$7.6\times10^{-5}$, $2.6\times10^{-5}$ and $1.3\times10^{-4}$ for the three
simulation cases and $2\times10^{-3}$–$4\times10^{-3}$ for the cameras (Table
2; the text gives other camera values). A 50-step rollout takes 0.025–0.03 s,
claimed as a six-orders-of-magnitude speed-up over JOREK. Ablations cover step
size, number of Fourier modes (saturating at 8), training-set size (little gain
beyond about 500 runs), zero-shot super-resolution, out-of-distribution
failure and error growth in long rollouts. The models are not physics-informed
and no physical diagnostic of the predictions is checked.

# Key claims

1. **Multi-variable beats per-variable FNO at equal parameter count**
   (§3.1.4, Fig. 11). Shown for density and temperature in all three cases.
   Not supported for the potential in the single blob with non-uniform
   temperature: there the multi-variable curve oscillates up to about 0.009
   MAE, above the single-variable one (Fig. 11b), while the text claims "much
   better performance" without qualification. The authors note that
   comparisons hold only within one field, each field having its own
   normalisation.
2. **Accuracy and cost** (Table 2, §3.1.1–3.1.3). MSE in the normalised domain
   $7.58\times10^{-5}$ (isothermal, 2 fields, 6,321,000 parameters, 48 min
   training), $2.56\times10^{-5}$ (non-uniform $T$, 3 fields, 9,467,000
   parameters, 97 min), $1.33\times10^{-4}$ (multi-blob, 1500 training runs,
   682 min), all on one Nvidia A100. Shown.
3. **"Speedup of 6 orders of magnitude"** (abstract, §3.1.1). Stated: 0.025 s
   inference for 50 steps against "approximately 350 core hours" per JOREK run,
   with no timing protocol. The surrogate emulates only a quarter of a run;
   CPU core-hours are set against GPU seconds; training and data generation
   (about $7\times10^5$ core-h) are excluded (see Recorded as printed).
4. **Rollout error grows almost linearly** from $t=10$ to $t=50$ (§3.1.3, Fig.
   10; App. C, Fig. C1). Physical-space MAE: density about
   $0.25\to1.8\times10^{18}$ m⁻³, potential about $4\to44$ (axis labelled V),
   temperature about $0.05\to0.37$ eV. A model trained to 200 instances
   "quickly loses grip". Shown.
5. **Step size** (§3.1.5, Fig. 12). Errors spike at multiples of the output
   size; a step of 1 is smoothest in cases (a) and (b) but in case (c)
   overtakes the others only after $t\approx45$. A step of 5 is retained for
   training efficiency. The pushforward trick of Brandstetter et al. is cited
   as the remedy for the train/inference distribution shift, not applied.
   Shown.
6. **Mode truncation** (§3.1.6, Figs. 13–14). MAE falls with the number of
   retained modes and saturates at 8: 8, 16 and 32 modes are indistinguishable
   (about 0.011 MAE at $t=50$) against about 0.0145 with 2 modes. Shown.
7. **Training-set size** (§3.1.7, Figs. 15–16). On 1835 multi-blob runs (85
   held out), test MAE falls from about $6.2\times10^{-3}$ (250 runs) to about
   $3.4\times10^{-3}$ (1500 runs) and rises slightly at 1750; training time
   grows linearly ($0.6\to4.7\times10^4$ s). "Gains … do not scale well at
   all"; about 500 runs suffice. Shown.
8. **Zero-shot super-resolution** (§3.1.8, Figs. 17, A6). Trained at 100×100,
   evaluated at 500×500 with MSE $7.90\times10^{-5}$, lower than the 100×100
   multi-blob figure of Table 2; the paper does not comment. Shown.
9. **No extrapolation** (§3.1.9, Fig. 18). With 13 blobs, twice the maximum
   amplitude and 1.5 times the width of the training set, the prediction is
   right only at the first instance. Shown qualitatively; the
   neural-tangent-kernel explanation is Stated.
10. **Camera forecasts** (§3.2, Figs. 20–25). The camera FNO follows ramp-up,
    flat-top, L-mode, H-mode and the L–H transition (shot 30428), locates
    plasma–wall interaction regions and reproduces reflections, but smooths
    out [ELM](/definitions/edge-localized-mode.md) filaments and cannot
    pinpoint the transition time, being "a regression model". Shown.
11. **Real time** (§3.2). With a 1.2 ms frame interval, "the FNO only requires
    6 ms to predict the next 12 ms". Stated; no hardware or latency breakdown.
12. **3D not demonstrated** (§3.1.10). GPU memory, the cost of 3D training data
    and the choice of operator basis are listed as obstacles. Stated.
13. **Earlier comparison** (§1, citing Gopakumar et al. 2023). FNO trains
    faster, needs fewer parameters and outperforms ConvLSTM and U-Net on blob
    diffusion. Attributed; not repeated here.

# Models and numerics

**Training data: JOREK field-free model** (§2.1, Eqs. 1–3, checked on the
rendered page), in registry notation:

$$\begin{aligned}
\partial_t\rho &= -\nabla\cdot(\rho\mathbf v)+D_\perp\nabla^2\rho,\\
\rho\,\partial_t\mathbf v &= -\rho\,\mathbf v\cdot\nabla\mathbf v-\nabla p+\nu\nabla^2\mathbf v,\\
\partial_tp &= -\mathbf v\cdot\nabla p-\Gamma p\nabla\cdot\mathbf v+\kappa_\perp\nabla^2T,
\end{aligned}$$

with $\Gamma=5/3$ and isotropic (spatially constant) $D_\perp=3.4$ m² s⁻¹,
$\nu=2.25\times10^{-6}$ kg m⁻¹ s⁻¹, $\kappa_\perp=2.25\times10^{-7}$ (units
printed kg m⁻¹ s⁻¹). The momentum equation is projected with
$\nabla\phi\cdot\nabla\times(R^2\,\cdot)$ under the poloidal ansatz
$\mathbf v=R^2\nabla\phi\times\nabla u$ (the potential plays the role of the
stream function $u$), with vorticity $\varpi=\nabla^2u$, giving equations for
$\rho$, $u$, $T$ that are not printed ([reduced MHD](/methods/reduced-mhd.md),
referred to Hoelzl et al. 2021). Isothermal variant: $T$ constant, the
pressure equation dropped; buoyancy and inertia both scale with $\rho$, so all
blobs move at the same speed. Background density $10^{18}$ m⁻³ and temperature
1 eV; Dirichlet conditions at the wall.

* Discretization: 200×200 bicubic [Bézier elements](/methods/bezier-finite-elements.md),
  $\Delta t=0.15$ µs, 2000 steps (300 µs), downsampled to 200 time slices
  (1.5 µs) on a regular 100×100 grid. About 350 core-h per run (16 cores per
  run on the EOSC-hub cloud for single blobs; 48 cores on CINECA Marconi for
  the 2000 multi-blob runs).
* Initial conditions (Table 1): 1–10 blobs; $R\in[9.4,10.4]$ m,
  $Z\in[-0.4,0.4]$ m (multi-blob; single blobs at $(R,Z)=(10,0)$); width
  0.02–0.1 m; density amplitude $(1$–$4)\times10^{19}$ m⁻³; temperature
  amplitude 12–72 eV. Single-blob sets: 120 runs (100 train, 20 test);
  multi-blob set: 2000 runs (1500 train in Table 2); a separate 1835-run set
  for §3.1.7; other ablations use the first 250 multi-blob runs.

**FNO** (§2.3, Eqs. 4–8, checked on rendered pages). Page-local symbols (see
the notation map): an operator $\mathcal G_\vartheta$ with trainable
parameters $\vartheta$ maps an input function to an output function by
lifting, a stack of Fourier layers and a projection. A Fourier layer maps the
latent field $v_\ell$ to

$$v_{\ell+1}=\sigma\Big(\mathcal F^{-1}\big(\mathsf R_\ell\,\mathcal F(v_\ell)\big)+\mathsf W_\ell v_\ell+\mathsf C_\ell g+b_\ell\Big),$$

with $\mathcal F$ the FFT, $\mathsf R_\ell$ complex weights on the $k_{\max}$
retained modes, $\mathsf W_\ell$ a local linear map, $\mathsf C_\ell$ the
point-wise map of the grid coordinates $g$, $b_\ell$ a bias and $\sigma$ the
GELU; skip connections (Highway networks) are added, placement not given.

* **Multi-variable layout** (§2.3.3): tensors [batch, fields, time, $x$,
  $y$]; time is the channel axis; the FFT acts per field over space;
  $\mathsf R_\ell$ is extended to the field axis and $\mathsf W_\ell$ is a
  Conv3d across fields and space.
* **Simulation FNO** (Table B1): input of 10 time steps plus 2 grid
  coordinates for 3 fields on 100×100; lift to width 32; 6 Fourier layers;
  projections to 128 and to 5 output steps; 16 modes unless stated.
  Per-field normalisation in two stages (division by the order of magnitude of
  the training maximum, then linear scaling to $[-1,1]$). Adam, up to 500
  epochs, learning rate 0.005 halved every 100 epochs, backpropagation through
  the rollout. Loss (Eq. 11): the sum over rollout steps of the relative
  squared $L_2$ error of the predicted fields plus the relative squared $L_2$
  error of their increments over one output step, equally weighted.
* **Camera FNO** (Tables D1–D2): Conv2d variant, width 16, 8 modes,
  201,900 parameters; inputs 448×640 (rbb) or 400×512 (rba); relative-$L_2$
  loss without the increment term; uniform $(R,Z)$ grids from Calcam
  calibration with the MAST CAD model. A 200-frame shot gives 180 pairs.
* No PDE residual or conservation constraint; all training on one A100.
  Code: github.com/Plasma-FNO.

# Tests and results

| Case | Fields | Parameters | Training (min) | Training size | MSE (normalised) |
|---|---|---|---|---|---|
| Single blob, isothermal | 2 | 6,321,000 | 48 | 100 | $7.58\times10^{-5}$ |
| Single blob, non-uniform $T$ | 3 | 9,467,000 | 97 | 160 | $2.56\times10^{-5}$ |
| Multiple blobs, non-uniform $T$ | 3 | 9,467,000 | 682 | 1500 | $1.33\times10^{-4}$ |
| Camera, solenoid (rbb) | 1 | 201,900 | 1568 | 7661 | $1.97\times10^{-3}$ |
| Camera, divertor (rba) | 1 | 201,900 | 935 | 5851 | $3.80\times10^{-3}$ |

* Inference: 0.025 s (isothermal) or 0.03 s per 50-step rollout.
* Learning curves (Fig. 6): multi-blob test loss plateaus near 0.28 against
  0.13 in training; single-blob cases fall below about 0.1.
* Cameras: rbb 55 shots (50/5), 7661 train and 828 test pairs; rba 48 shots
  (45/3), 701 test pairs; test shots listed in App. G.
* No comparison with another surrogate and no physics validation
  (conservation, blob velocity scaling, energy); errors are MSE/MAE only.

# Notation map

| Gopakumar et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $R$, $Z$, $\phi$ | $R$, $Z$, $\phi$ | orientation of $\phi$ not stated |
| $\rho$ | $\rho$ | values quoted in m⁻³, i.e. used as a number density; JOREK evolves a normalised mass density — **flag** |
| $\vec v$ | $\mathbf v$ | |
| $p$, $T$ | $p$, $T$ | $T$ in eV |
| $D$ | $D_\perp$ | isotropic, $\mathbf B=0$ |
| $\mu$ | $\nu$ | dynamic viscosity; **collision:** registry $\mu$ is the magnetic moment |
| $\kappa$ (Eq. 3) | $\kappa_\perp$ | isotropic; **collision:** native $\kappa$ is also the kernel operator of Eqs. 5–7 |
| $\gamma$ | $\Gamma$ | **collision:** registry $\gamma$ is a growth rate |
| $\Phi$ | $u$ | "electric potential … equivalent to the velocity stream function", $\vec v=R^2\nabla\phi\times\nabla\Phi$; same sign as the registry ansatz, no $F_0$ since $\mathbf B=0$ |
| $w=\nabla^2\Phi$ | $\varpi$ | plain Laplacian here |
| $G_\theta$, $\theta$ | $\mathcal G_\vartheta$, $\vartheta$ (page-local) | **collision:** registry $\theta$ is a poloidal angle |
| $a$, $A$, $D$; $u$, $U$, $D'$ | words (input/output function, space, domain) | **collision** with $a$, $D_\perp$, $u$ |
| $\nu_t$ | $v_\ell$ (page-local) | **collision:** registry $\nu$ is viscosity; native $t$ is a layer index here |
| $W$, $R$, $C$, $b$ | $\mathsf W_\ell$, $\mathsf R_\ell$, $\mathsf C_\ell$, $b_\ell$ (page-local) | **collision:** native $R$ vs major radius |
| $\kappa(a;\phi)$, $\kappa_\phi$ | words (kernel integral operator) | **collision** with $\kappa_\perp$ and $\phi$ |
| $\sigma$, $\mathcal F$, $\mathcal F^{-1}$ | $\sigma$, $\mathcal F$, $\mathcal F^{-1}$ (page-local) | GELU; FFT |
| $g$ | $g$ (page-local) | grid coordinates; **collision:** registry $g$ is a marker sampling density |
| $k_{\max}$ | $k_{\max}$ (page-local) | retained modes per layer |
| $T_{in}$, step, $T_{out}$; $T$ in Eq. 11 | words | **collision:** native $T$ also the temperature |
| $\tilde y_t$, $y_t$, $N$ | words (prediction, label, batch size) | |

# Pages created or updated

Chunk 3 (2026-10-16) created or updated the pages below. This source is cited on:

* [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md)
* [Fourier neural operator surrogates of MHD simulations](/methods/fourier-neural-operator-surrogates.md)
* [JOREK](/software/jorek.md)
* [Reduced MHD for tokamaks](/methods/reduced-mhd.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2024_Crossref_Nuclear_Fusion_Gopakumar_Plasma_surrogate_modelling_using_Fourier_neural_operators.pdf`
   * **Version.** arXiv:2311.05967v2 [physics.plasm-ph], 18 June 2024, posted
     after publication; not the publisher PDF. 53 pp.: main text pp. 1–38,
     references pp. 39–41, appendices A–G pp. 42–53. Pagination differs from
     the NF article, so locations are given by section, figure and table.
   * **Identity.** doi:10.1088/1741-4326/ad313a, checked on Crossref: title,
     authors, Nucl. Fusion 64(5), article 056025, May 2024 (online 9 April
     2024), 47 references. Crossref gives the 11th author's surname as "Peter
     Deisenroth"; the person is Marc Peter Deisenroth. The team authors refer
     to the author lists of Hoelzl et al. (2021) and Meyer et al. (2017).
   * **How read.** Full text; Eqs. 1–3, 4–8, 10 and 11 checked on rendered
     pages; plot values are the reader's approximate readings.
   * **Recorded as printed.**
     * Abstract "MSE … ≈ $10^{-5}$" against "∼ $10^{-4}$" in §3; Table 2
       ranges from $2.56\times10^{-5}$ to $1.33\times10^{-4}$.
     * Camera MSE: rba $3.80\times10^{-3}$ (Table 2) against
       $1.70\times10^{-4}$ (§3.2.3), a factor of about 22; rbb
       $1.97\times10^{-3}$ against $1.7\times10^{-3}$ (§3.2.2).
     * Camera training times: rbb 1568 min (Table 2) against "27 hours 45
       minutes" (§3.2.2); rba 935 min against "9 hours 10 minutes" (§3.2.3).
       rba training pairs 5851 (Table 2) against 5815 (§3.2.3).
     * Non-uniform-$T$ single blob: training size 160 in Table 2, but §2.1
       gives 120 runs per single-blob set (100 train, 20 test).
     * Speed-up (compiler's check): 350 core-h at 48 cores is about 7.3 h wall
       time, about $10^6$ times 0.025 s; but the surrogate covers 50 of 200
       downsampled instances (500 of 2000 steps), giving about
       $2.6\times10^5$ at equal physical time; core-seconds against
       GPU-seconds give about $5\times10^7$.
     * Eq. 10 integrates over $\tau$ a function of $x$, and is said to follow
       "by replacing the convolution operation with the Fourier transform" in
       Eq. 9 (rendered p. 11).
     * The FNO cost is given as $O(nk_{\max})$; the FFT remains
       $O(n\log n)$ and truncation reduces only the weight multiplication.
     * Symbol overloading: $\kappa$ (conductivity and kernel), $\phi$
       (toroidal angle and kernel parameter), $T$ (temperature and rollout
       length), $t$ (layer index in Eq. 5, time index in Eq. 11).
     * Fig. 8 caption lists "(c) temperature", but only panels (a) and (b) are
       printed (p. 18).
     * Fig. 15: y-axis labelled MAE, caption says mean squared error; the
       curve rises at 1750 runs.
     * Fig. 11(b) contradicts the unqualified multi-variable claim (Key claim
       1).
     * §3.2.1 names the rbb camera twice; the second should be rba.
     * Table D1 prints projection shapes (50, 448, 648, …) for a 640-wide
       input, and "(50, 16 448, 640)" without commas.
     * App. D calls the camera FNO "auto-regressive", contradicting §2.3.2 and
       §3.2 (sliding window), and says "Conv2d represents the 3D convolutional
       layer".
     * §3.2 refers to the individual-FNO architecture "given in Appendix D",
       which tabulates only the camera models.
     * Two affiliations numbered 4 (Liverpool should be 3).
     * $\kappa$ printed in kg m⁻¹ s⁻¹, not a heat-conductivity unit.
     * Whether the 500×500 reference for super-resolution is the 200×200 FEM
       solution sampled finer or a new run is not stated.
     * Typos: "traini§ng" (p. 4), "starting form 10" (p. 21), "wiht … H-mod"
       (Fig. 21), "the the multiple blobs" (Fig. 17); a sentence in §3.2.2
       breaks off ("can be seen in Though the camera …").
   * **Reference list.** 47 printed entries ([1]–[47]), equal to the Crossref
     count, merged into the bibliography under `gopakumar-2024`; about 24 are
     pure ML/CS works, kept in full. Key decisions: the FNO paper is
     `li-2020-c` and PINO `li-2022-b` (the bundle's `li-2020` and `li-2022`
     are different works); Kirk et al. PPCF 48:B433 is `kirk-2006-b` (not the
     PRL `kirk-2006`); the authors' earlier papers are `gopakumar-2023` (FNO
     for plasma modelling) and `gopakumar-2023-b` (Fourier-RNNs); ref. [26],
     printed only as "C. et al.", is `c-2022`; reused keys include
     `smith-2020`, `hoelzl-2021` and `wiesen-2015`. Printed defects: [1], [7],
     [8] end in truncated "… and" author lists; [18] lists "M. Team"; [23] is
     printed as Physics of Plasmas vol. 59 for a PPCF article; [36] has a
     malformed arXiv id "2202.033786"; [40] prints year 2020 for a 2018 arXiv
     id; [42] carries a publisher copyright line; [46] is Calcam on Zenodo.

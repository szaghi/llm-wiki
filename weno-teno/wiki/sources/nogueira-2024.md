---
type: Source
title: "Nogueira et al. (2024) — Machine learning-based WENO5 scheme"
description: "A fifth-order finite-difference WENO scheme whose three nonlinear weights are output by a small neural network fed with absolute-value smoothness measures and a Jameson-type shock detector, filtered by a sharp ENO cut-off and bypassed on plateaus; less dissipative than WENO5-JS on standard Euler tests, at several times its cost."
resource: "doi:10.1016/j.camwa.2024.05.031"
source_kind: paper
authors: [Nogueira X., Fernández-Fidalgo J., Ramos L., Couceiro I., Ramírez L.]
year: 2024
venue: "Comput. Math. Appl. 168:84-99"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Computers_amp_Mathematics_with_Applications_Nogueira_Machine_learning-based_WENO5_scheme.pdf"
tags: [machine-learning, weno, smoothness-indicator, spectral-analysis, finite-difference]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper builds a fifth-order finite-difference WENO scheme whose nonlinear weights
are computed by a feed-forward neural network, extending the WENO3-NN methodology of
[Bezgin et al. (2022)](/sources/bezgin-2022.md) from three- to five-point stencils
(see [learned WENO weights](/methods/learned-weno-weights.md)). The authors call it
WENO5-NN; it is a different scheme from the WENO5-NN of Stevens & Colonius, which the
paper describes as a perturbation of the WENO5-JS coefficients. The base is
[WENO5-JS](/methods/weno-js-reconstruction.md): candidate fluxes and linear weights
$d_k=(0.1,0.6,0.3)$ are kept and only the weight formula is replaced. The network
takes four inputs, the max-normalized absolute-value analogues of the Jiang–Shu
[smoothness indicators](/definitions/smoothness-indicator.md) and a five-point
extension of Jameson's shock detector, has three hidden layers (32, 16, 16 neurons,
swish activation) and outputs the three weights. A non-trained "ENO layer", a sharp
cut-off at $4\times10^{-7}$ with renormalization, restores the
[ENO property](/definitions/eno-property.md); a curvature-based plateau detector
bypasses the network and sets $\omega_k=d_k$ in flat regions.

Training uses only static canonical functions sampled with $\Delta x=0.01$ (jumps,
sinusoids, sawtooth, tanh, polynomials up to cubic) and a loss that weights the
reconstruction error by the shock detector to a power and the deviation from the
linear weights by its complement. An
[approximate-dispersion-relation](/definitions/approximate-dispersion-relation.md)
analysis shows that two loss hyperparameters define a family of schemes; the chosen
member has lower dispersion and dissipation errors than WENO5-JS over a wide
wavenumber range.

Tests use characteristic-wise global [Lax–Friedrichs splitting](/methods/lax-friedrichs-flux.md)
and third-order Runge–Kutta. On the 2D [entropy wave](/benchmarks/density-wave-advection.md)
WENO5-NN is fifth order with errors 4–6 times smaller than WENO5-JS, the order
dropping to 4.68 on the finest grid. On the [Sod and Lax](/benchmarks/sod-and-lax-shock-tubes.md),
[123](/benchmarks/double-rarefaction-problem.md) and [LeBlanc](/benchmarks/leblanc-shock-tube.md)
tubes, the [Shu–Osher problem](/benchmarks/shu-osher-problem.md),
[2D Riemann configurations](/benchmarks/two-dimensional-riemann-problems.md) 3 and 6,
[double Mach reflection](/benchmarks/double-mach-reflection.md),
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) and the
[Mach 3 step](/benchmarks/forward-facing-step.md) it is shown less dissipative than
WENO5-JS and stable. The cost is "several times" that of WENO5-JS, unmeasured; the
authors present the method as a route to new analytical weight functions.

# Version read

Version of record (Elsevier typeset, open access; received 11 October 2023, accepted
25 May 2024, online 7 June 2024), 16 pages (pp. 84–99), all read; pp. 86–88 checked
visually for Eqs. (12)–(17), Table 1 and Fig. 5. Page 1 matches Crossref (title,
five authors, venue, DOI). Numbering cited here is that of this version.

# Key claims

Registry notation (see the notation map): the source's linear weights $c_k$ are
$d_k$, its JS exponent $m$ is $q$, its reduced wavenumber $w$ is $\vartheta$; its
absolute-value measures $\delta_k$ are written $\beta^{\mathrm{abs}}_k$, its shock
detectors $\gamma_i$, $\gamma^s$ are written $\varsigma_k$, $\varsigma^{\mathrm s}$, and its loss
exponent and coefficients $\alpha$, $\beta_d$, $\beta_W$ are written $p_s$, $b_d$, $b_W$, as on
[learned WENO weights](/methods/learned-weno-weights.md), to keep $\delta_k$, $\gamma$, $\alpha_k$
and $\beta_k$ free.

1. WENO5-NN, a network that outputs the three WENO5 weights directly, outperforms WENO5-JS in most tests and generalizes across resolutions (Abstract, §5). **Shown**
2. The WENO5-NN of Stevens & Colonius [18] perturbs the WENO5-JS coefficients and needs post-processing that reduces the overall accuracy to first order; the present approach regresses the weights directly, following WENO3-NN [16] (§1). **Stated**
3. Architecture: inputs $(\bar\beta^{\mathrm{abs}}_1,\bar\beta^{\mathrm{abs}}_2,\bar\beta^{\mathrm{abs}}_3,\varsigma^{\mathrm s})$, hidden layers of 32, 16 and 16 neurons with swish activation $x/(1+e^{-x})$, three outputs, size chosen "after several tests" (§3.1, Eq. (11), Fig. 2). **Stated** (the output activation is not stated)
4. The squared indicators $\beta_k$ as inputs gave a less accurate network than the absolute-value measures $\beta^{\mathrm{abs}}_k$ of Eq. (12), obtained from the Jiang–Shu formulas by replacing squares with absolute values (§3.1). **Stated** (no data shown)
5. Adding $\varsigma^{\mathrm s}=\max_k\varsigma_k$, $\varsigma_k=\lvert f_{j-1}-2f_j+f_{j+1}\rvert/(\lvert f_j-f_{j-1}\rvert+\lvert f_{j+1}-f_j\rvert+10^{-15})$ over the three three-point substencils (Eq. (13)), "considerably" improves the results (§3.1). **Stated** (no data shown) *(Compiler check, not in the sources: $\lvert a-2b+c\rvert\le\lvert b-a\rvert+\lvert c-b\rvert$, so $\varsigma_k\in[0,1)$, consistent with the stated range $[0,1]$.)*
6. The normalization $\bar\beta^{\mathrm{abs}}_k=\beta^{\mathrm{abs}}_k/\max_l\beta^{\mathrm{abs}}_l$ misleads the network near machine zero: $(10^{-16},10^{-15},10^{-16})$ maps to $(0.1,1,0.1)$, which "may correspond with a non-smooth situation"; a curvature-based plateau detector after Clain et al. [25] sets $\omega_k=d_k$ there and saves network calls (§3.1, Eq. (14)). **Stated** (the detector formula and threshold are not given)
7. The ENO layer $\tilde\omega_k=\omega_k\psi_k/\sum_j\omega_j\psi_j$, $\psi_j=0$ if $\omega_j\le4\times10^{-7}$ and 1 otherwise, restores the ENO property and stops the network from giving small non-zero weights to discontinuous stencils; the threshold follows the procedure of [16] (§3.1, Eq. (15)). **Stated**
8. The loss is $\mathcal L=\mathcal L_r+b_d\mathcal L_d+b_W\lVert W\rVert_2^2$, with the reconstruction error weighted by $(\varsigma^{\mathrm s})^{p_s}$ and the deviation from $d_k$ by $(1-\varsigma^{\mathrm s})^{p_s}$; across a discontinuity $\varsigma^{\mathrm s}=1$ and $\mathcal L_d=0$ (§3.2, Eqs. (16)–(17)). **Stated**
9. Training: mini-batch 128, $b_W=10^{-9}$, 80/20 split, learning rate $10^{-3}$, Nadam, 1000 epochs, LeCun normal initialization, TensorFlow, seed 1; five repetitions with different validation sets show "small variability"; the network kept is the one best on the 1D tests (§3.2). **Stated**
10. The training set (Table 1) contains only static canonical functions (655861 discontinuity, 460355 sinusoid, 72135 sawtooth, 82837 tanh, 52700 cubic, 63935 quadratic, 2893 linear, 393 constant samples) and no Euler solutions; its jump and frequency ranges are wider than in [16], which was found necessary for strong-shock robustness and dispersion (§3.2.1). **Stated**
11. Outliers are removed by $\varsigma^{\mathrm s}$ range per function class (Table 2) and repeated entries dropped; the $\varsigma^{\mathrm s}$ histogram is dominated by $[0.9,1]$ (§3.2.1, Fig. 4). **Shown**
12. WENO5-NN has a smaller dispersion error than WENO5-JS over a large wavenumber range and less dissipation in the well-resolved range; changing the loss hyperparameters $(\alpha,\beta)$ gives a family with similar dispersion and different high-wavenumber dissipation; $(0.2,0.1)$ is chosen (§3.3, Fig. 5). **Shown**
13. Near the saddle points of $\sin^3(\pi x)$ the WENO5-NN weights deviate less from $d_k$ than those of WENO5-JS, and the authors say WENO5-NN "also alleviates" the [critical-point](/properties/critical-point-accuracy.md) order loss of WENO5-JS (§3.4, Fig. 6). **Shown** (weight traces only; no order test at critical points)
14. At the discontinuity of Eq. (19) WENO5-NN "behaves slightly differently" from WENO5-JS (§3.4, Fig. 7). **Shown**
15. 2D entropy wave, $L_2$ density errors on $25^2$ to $400^2$: WENO5-JS $1.16\times10^{-1}$ to $7.88\times10^{-7}$ with orders 2.80, 4.46, 4.90, 5.00; WENO5-NN $8.47\times10^{-2}$ to $1.59\times10^{-7}$ with orders 4.16, 5.12, 5.06, 4.68; the order "seems to start to drop below 5 at the finest grid", as for WENO3-NN in [16] (§4.1, Table 3). **Shown** *(Compiler check, not in the sources: $\log_2$ of the successive printed error ratios gives 2.805, 4.457, 4.901, 5.005 and 4.166, 5.117, 5.059, 4.681.)*
16. Sod (50 and 200 points): WENO5-NN is more accurate, especially in velocity, with a sharper contact and a similar shock, and generalizes across resolutions (§4.2.1, Figs. 8–9). **Shown**
17. Lax (100 points): WENO5-NN captures the density and velocity discontinuities more accurately and gives a "very accurate" velocity at the tail of the expansion (§4.2.2, Fig. 10). **Shown**
18. 123 problem: WENO5-NN is more accurate at 100 points, especially in velocity near the low-density region, and more accurate in internal energy "in all the domain"; both schemes have their largest errors in the low-density region (§4.2.3, Figs. 11–13). **Shown**
19. LeBlanc ($\gamma=5/3$, 900 points): both schemes misplace the discontinuity at $x=7.9756$, but WENO5-NN "greatly reduces the overshoots" of WENO5-JS; at 5000 points it converges to the exact solution (§4.2.4, Figs. 14–15). **Shown**
20. Shu–Osher (200 points): WENO5-NN resolves the entropy waves, which WENO5-JS loses, with a slight phase error; behaviour is similar to WENO-NS and WENO-Z as presented in [38] (§4.3, Fig. 16). **Shown**
21. Riemann configuration 3 ($400\times400$, $t=0.8$): WENO5-NN is symmetric about $y=x$, shows Kelvin–Helmholtz roll-ups on the primary slip lines and agrees with fine-grid WENO results of [44]; configuration 6 ($1000\times1000$, $t=0.3$): small-scale structures along the slip lines, absent in WENO5-JS, with no claim on physical accuracy (§4.4.1, Figs. 17–18). **Shown**
22. Double Mach reflection ($960\times240$, $t=0.3$): WENO5-NN reproduces the Mach-stem instabilities and small structures at the jet and slip line, WENO5-JS does not (§4.4.2, Figs. 19–20). **Shown**
23. Rayleigh–Taylor ($128\times512$, $t=1.95$): more vortical structures and tail instabilities, with a "slight loss of symmetry" (§4.4.3, Fig. 21). **Shown**
24. Mach 3 step ($t=4$): WENO5-NN captures the Kelvin–Helmholtz instability at the triple point (§4.4.4, Fig. 22). **Shown**
25. The same network is used in each direction in 2D (§4.4). **Stated**
26. The cost is "considerably higher" (§3.1) and "several times" (§5) that of WENO5-JS, with no timing or hardware reported; future hardware such as TPUs is expected to make network-based schemes competitive. **Stated**

# Printed slips

- Double Mach reflection: the text imposes "pre-shock conditions … for $x<\frac16$" on the bottom boundary, but by the initial condition Eq. (31) the state at $y=0$, $x<1/6$ is the post-shock one. *(Compiler check, not in the sources: at $y=0$ the pre-shock condition $y\le1.732(x-0.1667)$ fails for $x<0.1667$.)*
- §3.2 calls the last loss term an $L_2$ regularization "on the neural network weights $\lVert W\rVert_2^2$", while Eq. (17) prints $\lVert W\rVert_2^2=\omega_0^2+\omega_1^2+\omega_2^2$, the output WENO weights.
- Weight indices: $c_k$, $\omega_k$ run over $k=1,2,3$ in §2 and the first paragraph of §3.1, but over $0,1,2$ in Fig. 2 and Eqs. (15), (17), where $c_0$ is undefined under the §2 indexing.
- The text after Eq. (17) refers to "$-f^s_{i+1/2}$" as the exact value; Eq. (17) prints $f^s_{i+1/2}$.
- The hyperparameter "$\beta$" of §3.3 and Fig. 5 is never identified with $\beta_d$ or $\beta_W$ of Eq. (16) (here $b_d$, $b_W$); $\alpha$ is also the Lax–Friedrichs speed (Eq. (2)) and the unnormalized weights (Eq. (9)).
- §3.2.1 lists outlier removal for "discontinuities, sawtooth, cubic and quadratic functions", while Table 2 also lists the oscillatory function.
- §4.4.3 speaks of results "on both grids" for Rayleigh–Taylor, but only $128\times512$ is specified.
- The Fig. 22 caption (Mach 3 step) repeats the contour levels of Fig. 21 (30 levels from 0.3 to 6.15), and the grid is printed "100 × 300" for a domain three times longer in $x$, unlike "960 × 240" for the double Mach reflection.
- Naming: "NN-WENO5" once (§4.1); "WENO-NN", "WENO-JS" without the 5 (§3.3, §4.2); Abstract "a neural network that compute".

# Notation map

| Nogueira et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $f_i$, $f_{i+1/2}$ | $f_i$, $\hat f_{i+1/2}$ | point values of the split flux, reconstructed flux |
| $f^\pm$, $\alpha=\max\lvert f'\rvert$ | $f^\pm$, $a$ | global Lax–Friedrichs splitting; **$\alpha$ collides with $\alpha_k$** |
| $f^k_{i+1/2}$, $k=1,2,3$ | $\hat f^{(k)}_{i+1/2}$, $k=0,1,2$ | $k=1$ is the most upwind stencil, the registry's $S_0$ |
| $r$ | $r$ | 3; agrees |
| $c_k$ | $d_k$ | $(0.1,0.6,0.3)$ |
| $\beta_k$, $\varepsilon=10^{-6}$, $m=2$ | $\beta_k$, $\epsilon$, $q$ | WENO5-JS weights |
| $\alpha_k$, $\omega_k$ | $\alpha_k$, $\omega_k$ | agrees |
| $\delta_k$, $\bar\delta_k$ | $\beta^{\mathrm{abs}}_k$, $\bar\beta^{\mathrm{abs}}_k$ | absolute-value measures and normalized inputs; **$\delta_k$ is the TENO cut-off flag in the registry** |
| $\gamma_1,\gamma_2,\gamma_3$, $\gamma^s$ | $\varsigma_k$, $\varsigma^{\mathrm s}$ (page-local) | Jameson-type detectors, of the form of the WENO3-NN $\varsigma$; **$\gamma$ collides with the TENO $\gamma_k$ and the ratio of specific heats** |
| $\omega^{NN}_k$, $\tilde\omega^{NN}_k$, $\psi_j$ | kept | network and ENO-layer weights; $\psi_j$ page-local as on [learned WENO weights](/methods/learned-weno-weights.md) |
| $\mathcal L$, $\mathcal L_r$, $\mathcal L_d$, $\beta_d$, $\beta_W$, $\alpha$ (loss) | $\mathcal L$, $\mathcal L_r$, $\mathcal L_d$, $b_d$, $b_W$, $p_s$ | loss terms and hyperparameters, as for WENO3-NN; **$\beta_d$ collides with $\beta_k$, $\alpha$ with $\alpha_k$** |
| $w$, $W(w)$ | $\vartheta$, $\tilde\vartheta$ | reduced and modified wavenumbers |
| $\rho$, $u$, $v$, $p$ | $\rho$, $v_1$, $v_2$, $p$ | |

# Reference list

49 printed references in numbered Elsevier style ([1]–[49]), all parsed and merged
complete into the [bibliography](/bibliography.md) with `citedby` `nogueira-2024`.
Ref. [16] is the ingested `bezgin-2022`. Refs. [8] (Abgrall & Han Veiga, neural
limiter, Commun. Appl. Math. Comput. 5:532–572) and [12] (Tsoutsanis & Dumbser, C&F
225:104961) share author–year labels with ingested sources but are different works,
keyed apart by venue. Refs. [12] and [14] print no article number (taken from the
printed DOI); [22] prints no book title; [26] prints both ICLR 2015 and 2017; [45]
prints "Numer. Math. 10 (4)" with a DOI of Numer. Math. Theory Methods Appl. No
printed duplicates were found.

# Pages created or updated

Chunk 7 (2026-10-23), cited further in chunks 8–10 (2026-10-23). This source is cited on:

* [Accuracy at critical points](/properties/critical-point-accuracy.md)
* [Approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
* [ENO property](/definitions/eno-property.md)
* [Learned WENO weights](/methods/learned-weno-weights.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)

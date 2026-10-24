---
type: Source
title: "Huang et al. (2025) — A low-dissipation reconstruction scheme for compressible single- and multi-phase flows based on artificial neural networks"
description: "deepMTBVD: a small neural network, trained on the choices of the MUSCL-THINC-BVD scheme in 1D Riemann problems, selects MUSCL or THINC per cell before reconstruction, so only one candidate is built; proofs that min–max normalization keeps the BVD choice, tests on Euler and five-equation flows."
resource: "doi:10.1016/j.jcp.2025.113894"
source_kind: paper
authors: [Huang M., Cheng L., Ying W., Deng X., Xiao F.]
year: 2025
venue: "J. Comput. Phys. 530:113894"
local_file: "/home/stefano/papers/mosaic/weno-teno/2025_Crossref_Journal_of_Computational_Physics_Huang_A_low-dissipation_reconstruction_scheme_for_compressible_sin.pdf"
tags: [bvd, thinc, machine-learning, multiphase, finite-volume]
timestamp: 2026-10-23T19:57:00Z
---

# Summary

Huang et al. (2025b) target the cost of
[boundary variation diminishing](/definitions/boundary-variation-diminishing.md)
(BVD) reconstruction in Godunov-type finite volumes. MUSCL-THINC-BVD (Deng et al.)
builds both candidates in every cell, MUSCL with the van Leer limiter and
[THINC](/methods/thinc-reconstruction.md) with $\beta_{\mathrm T}=1.6$, and keeps
the one with the smaller total boundary variation over a five-cell stencil. The
authors label data by running that scheme on 1D Euler Riemann problems, train
offline a fully connected network (6 inputs, two hidden layers of 8 sigmoid
neurons, one output) to predict its choice, and at run time evaluate the network
once per cell and build only the selected reconstruction. The scheme is called
deepMTBVD; the network acts as a learned
[troubled-cell indicator](/definitions/troubled-cell-indicator.md) for a hybrid
reconstruction.

Two short proofs support the input normalization: for strictly monotone three-cell
data both candidates lie strictly between the neighbour averages, and min–max
normalization of the five-cell stencil leaves the BVD choice unchanged. The loss
is a weighted focal loss that penalizes MUSCL cells classified as THINC, since
THINC in smooth regions adds anti-diffusion error
([numerical dissipation](/definitions/numerical-dissipation.md)). One network
trained on 1D Euler data serves every variable, the
[five-equation model](/definitions/five-equation-model.md) with a
[stiffened-gas](/definitions/stiffened-gas-equation-of-state.md) liquid, and 2D by
dimensional splitting.

The solver is LeVeque–Shyue wave propagation with
[HLLC](/methods/hll-riemann-solvers.md) and
[SSP-RK2](/methods/ssp-runge-kutta.md). Tests: linear advection, where deepMTBVD
keeps second order and MUSCL-THINC-BVD drops to first; [Sod, Lax and a strong Lax
problem](/benchmarks/sod-and-lax-shock-tubes.md);
[double Mach reflection](/benchmarks/double-mach-reflection.md); the
[Mach 3 step](/benchmarks/forward-facing-step.md); an
[underwater explosion](/benchmarks/underwater-explosion.md); and an air–R22
[shock–bubble interaction](/benchmarks/shock-bubble-interaction.md). Resolution is
reported as comparable to MUSCL-THINC-BVD and sharper than MUSCL. Total time falls
because the saved reconstruction outweighs the inference cost; the abstract says
"up to 40%".

# Version read

The archive file is the version of record (J. Comput. Phys. 530:113894, online 26
February 2025), 25 pages, all read (pp. 5–7 and 22 checked on the page images).
Page 1 matches the Crossref record. Label in this bundle: Huang et al. (2025b);
it cites [Huang et al. (2025a)](/sources/huang-2025.md), the TENO-THINC RKDG
limiter of Huang, Li & Fu, as ref. [32].

# Key claims

Registry notation: averages $\bar u_i$, traces $u^\mp_{i+1/2}$ (source
$\hat u_{i+1/2,L}$, $\hat u_{i+1/2,R}$), THINC steepness $\beta_{\mathrm T}$
(source $\beta$) and jump centre $x^c_i$ (source $\tilde x_i$), volume fraction
$\phi_k$ (source $\alpha_k$), stiffened-gas constant $p_{\infty,k}$. Page-local:
$\mathsf s_i$ the limited MUSCL slope (source $\sigma_i$), $\theta_{\mathrm T}$ the
THINC sign (source $\theta$), $\mathsf C$ the normalized average of THINC,
$\mathrm{BV}$, $\mathrm{TBV}$ the boundary variations, $\chi^{\mathrm m}_i$ the
monotone indicator (source $\chi_i$), $\kappa_{\mathrm{NN}}$ the network output and
$\kappa_{\mathrm{ref}}$ its threshold (source $\kappa$, $\kappa_{\rm ref}$), $c_t$
and $\eta_{\mathrm f}$ the focal-loss weights and exponent (source $\omega_t$,
$\eta$).

1. BVD schemes build all candidate reconstructions before selecting one per cell, which leaves room for efficiency gains (§1, §3.3). **Stated**
2. deepMTBVD trains a network on the labels of MUSCL-THINC-BVD and uses it to choose THINC or MUSCL per cell beforehand, so only one reconstruction is built per cell (§1, §3.3, Algorithm 2). **Derived** (construction)
3. Conclusion 1: if $\bar u_{i-1},\bar u_i,\bar u_{i+1}$ are strictly monotone, both reconstructions in $I_i$ satisfy $(\hat u(x)-\bar u_{\min})/(\bar u_{\max}-\bar u_{\min})\in(0,1)$, with the extremes over $\{\bar u_{i-1},\bar u_{i+1}\}$ (Eq. (27), App. A). **Proved** (the MUSCL part through the TVD bound)
4. Conclusion 2: if the five averages of the stencil are not all equal, min–max normalization over them (Eq. (28)) leaves the BVD choice unchanged, because every boundary variation is divided by the same range (App. B, Eqs. (34)–(35)). **Proved** (the printed chain has swapped labels, see Printed slips)
5. Inputs are the five normalized averages and $\chi^{\mathrm m}_i$, set to 0 when the stencil range is below $10^{-15}$ or $\chi^{\mathrm m}_i=0$ (local extremum); two hidden layers of 8 sigmoid neurons; one output $\kappa_{\mathrm{NN}}\in[0,1]$ (§3.3.1–3.3.2, Eqs. (29)–(30), Fig. 3). **Stated**
6. The loss is $-c_t(1-\kappa_t)^{\eta_{\mathrm f}}\log\kappa_t$ with $\kappa_t=\kappa_{\mathrm{NN}}$ for THINC labels and $1-\kappa_{\mathrm{NN}}$ for MUSCL labels, $\eta_{\mathrm f}=2$, class weights 0.1 and 0.5 (Eqs. (31)–(32)). **Stated**
7. Class-weight ratio 1:5 gives accuracy 0.975 and false-positive rate 0.0046, against 0.981 and 0.013 for binary cross-entropy; ratios 1:2, 1:10, 1:20, 1:50, 1:100 give accuracies 0.968, 0.963, 0.948, 0.923, 0.901 and false-positive rates 0.0118, 0.0044, 0.0038, 0.0024, 0.0024 (App. C, Table 5). **Shown**
8. Training data come from six 1D Euler Riemann problems (Table 6), advanced 10 SSP-RK3 steps at CFL 0.1 on $\Delta x\in\{1/100,1/200,1/300,1/400\}$, de-duplicated with an $\infty$-norm distance threshold $10^{-3}$ (Algorithm 1, App. D). **Stated**; Table 6 case 6 is the initial data of the Lax test of §4.2.2 and case 2, with $v=0$, that of the strong Lax test of §4.2.3, while App. D says the short runs are meant "to prevent the data from being pre-trained in actual numerical examples".
9. 8000 training and 2000 validation samples, Adam, batch 128, learning rate 0.001, 2000 iterations; "an accuracy rate of over 98% on both the training and validation sets" (§3.3.2). **Stated**; Table 5 gives 0.975 for the adopted ratio 1:5.
10. Because of the normalization, the network trained on 1D Euler data applies unchanged to every variable, to the five-equation model and to 2D by splitting (Remark 1). **Stated**
11. $\kappa_{\mathrm{ref}}=0.45$ throughout; $\kappa_{\mathrm{ref}}=1$ reduces deepMTBVD to MUSCL, below about 0.1 discontinuities appear in the rarefaction, and between 0.1 and 0.45 there is no significant improvement (Remark 2, App. E, Figs. 19–20). **Shown**
12. Linear advection of $\sin(\pi x)$ on $[-1,1]$ to $t=10$, 400 to 12 800 cells: MUSCL and deepMTBVD are second order in $L^1$, MUSCL-THINC-BVD only first order, and MUSCL-THINC-BVD is the slowest above 6400 cells (§4.1, Fig. 4). **Shown** (figure only)
13. Sod (200 cells, $t=0.25$): deepMTBVD resolves shock and contact as well as MUSCL-THINC-BVD (§4.2.1, Fig. 5). **Shown**
14. Lax (200 cells, $t=0.16$): both BVD schemes resolve contact and shock better than MUSCL; deepMTBVD has weaker oscillations between shock and contact than MUSCL-THINC-BVD, and its THINC cells nearly coincide with those of MUSCL-THINC-BVD (§4.2.2, Fig. 6). **Shown**
15. Strong Lax (100 cells, $t=0.012$): deepMTBVD is sharper than MUSCL and less dissipative than MUSCL-THINC-BVD near the strong contact (§4.2.3, Fig. 7). **Shown**
16. Times at $N=10\,000$ (Table 1, MUSCL-THINC-BVD against deepMTBVD, Examples 1–3): totals 40.04 and 32.67 s, 55.30 and 45.01 s, 45.36 and 34.51 s; reconstruction 37.04 and 9.11, 51.20 and 13.41, 42.17 and 8.93 s; selection 2.99 and 23.56, 4.10 and 31.60, 3.18 and 25.58 s. **Shown** (no hardware stated)
17. Times at $N=100\,000$ (Table 2): totals 6265.50 and 2566.02 s, 7268.35 and 3926.57 s, 5975.97 and 3635.13 s. **Shown**
18. The saving is "10% to 40%" (Remark 3), "up to 40%" in the abstract and conclusion. **Stated** *(compiler check, not in the sources: from the printed totals the reductions are 18.4%, 18.6%, 23.9% in Table 1, 59.0%, 46.0%, 39.2% in Table 2, 14.0% in Table 3 and 11.1% in Table 4; two Table 2 values exceed 40%.)*
19. Double Mach reflection ($\Delta x=\Delta y=1/200$, $t=0.2$): the BVD schemes resolve slip-line vortices that MUSCL misses; totals 260.46 s and 223.87 s (Table 3, Fig. 8). **Shown**
20. Mach 3 step ($\Delta x=\Delta y=1/160$, $t=4$): deepMTBVD resolves the vortical structure like MUSCL-THINC-BVD, with consistent THINC cells; totals 242.54 s and 215.66 s (Table 4, Figs. 9–10). **Shown**
21. Compared with Cheng's results, too many THINC cells are selected around the shock at the top of the step, "due to the dimension-splitting process" (§4.2.5). **Stated**
22. Underwater explosion ($600\times600$): MUSCL smears the water–air interface; both BVD schemes keep it sharp and resolve the water bridge; density along $x=0$ agrees with Shukla et al. and Hu et al. on a coarser mesh than Shukla's (§4.3.1, Figs. 12–14). **Shown**
23. Air–R22 shock–bubble (400 cells per diameter): deepMTBVD is comparable to MUSCL-THINC-BVD and sharper than MUSCL, and classifies fewer cells as THINC with very similar results (§4.3.2, Figs. 16–18). **Shown**
24. The numerical stability of deepMTBVD in multiphase flow is better than that of the BVD scheme (§4.3). **Stated** (no dedicated evidence)
25. Deng et al. showed that MUSCL-THINC-BVD keeps interfaces narrower than higher-order polynomial reconstruction such as WENO-JS (§4.3). **Stated** (cited)
26. $\beta_{\mathrm T}$ from 1.6 to 2.2 gives good or acceptable results for sharp discontinuities; $\beta_{\mathrm T}=1.6$ throughout, and $\beta_{\mathrm T}\lvert n_x\rvert$ in multi-D after Xiao et al. (§3.2). **Stated**

The selection rule reproduced from Deng et al. (Eqs. (24)–(26)): THINC if $\delta<\mathsf C<1-\delta$ ($\delta=10^{-8}$), $(\bar u_{i+1}-\bar u_i)(\bar u_i-\bar u_{i-1})>0$ and $\mathrm{TBV}^{\mathrm T}_{i,\min}<\mathrm{TBV}^{\mathrm M}_{i,\min}$, where $\mathrm{TBV}^s_{i,\min}$ is the minimum of $\mathrm{BV}(s_1,s,s_2)=\lvert u^{s_1,-}_{i-1/2}-u^{s,+}_{i-1/2}\rvert+\lvert u^{s,-}_{i+1/2}-u^{s_2,+}_{i+1/2}\rvert$ over the four choices of $(s_1,s_2)$ in the neighbours.

# Printed slips

- MUSCL boundary values after Eq. (20): both are printed $\bar u_i-\frac{x_{i\mp1/2}-x_i}{x_{i+1/2}-x_{i-1/2}}\sigma_i$. *(Compiler check, not in the sources: evaluating Eq. (19) at $x_{i\mp1/2}$ gives $\bar u_i+\frac{x_{i\mp1/2}-x_i}{x_{i+1/2}-x_{i-1/2}}\sigma_i$; the printed signs swap the two values.)*
- Eq. (28), §3.3.1 and App. B: $\tilde u_{\max}=\max\{\bar u_{i-2},\bar u_{i-1},\bar u_i,\bar u_{i+1},\bar u_{i+1}\}$, and the same for the minimum, with $\bar u_{i+1}$ twice and $\bar u_{i+2}$ missing; the text after Eq. (29) lists $\bar u_{i+2}$.
- Eq. (35), App. B: under the hypothesis $TBV^T_{i,\min}<TBV^M_{i,\min}$ the printed chain reads $\widetilde{TBV}^T_{i,\min}=\frac1{\tilde u_{\max}-\tilde u_{\min}}\min\{BV(M,M,M),BV(T,M,T),BV(M,M,T),BV(T,M,M)\}=\frac{TBV^M_{i,\min}}{\cdot}<\frac{TBV^T_{i,\min}}{\cdot}=\widetilde{TBV}^M_{i,\min}$: the middle label changes from $T$ to $M$ and the final inequality reverses the hypothesis.
- Table 3: deepMTBVD reconstruction 88.25 s plus selection 136.62 s is 224.87 s, printed total 223.87 s. Table 4: MUSCL-THINC-BVD reconstruction 212.22 s plus selection 50.32 s is 262.54 s, printed total 242.54 s; with 262.54 s the saving would be 17.9%, not 11.1%.
- Eq. (5): $p_k(\rho_k,e_k)=(\gamma_k-1)\rho(e_k-e_{\infty,k})-\gamma_kp_{\infty,k}$, with the mixture density $\rho$ in a single-phase law.
- Eq. (10) against Eq. (5): the mixture law is printed $p=\big(\rho e-\sum_k\phi_k\rho_ke_{\infty,k}+\sum_k\frac{\phi_kp_{\infty,k}}{\gamma_k-1}\big)\big/\sum_k\frac{\phi_k}{\gamma_k-1}$. *(Compiler check, not in the sources: Eq. (5) with $\rho_k$ gives $\rho_ke_k=\frac{p+\gamma_kp_{\infty,k}}{\gamma_k-1}+\rho_ke_{\infty,k}$, and summing with the weights $\phi_k$ gives $-\sum_k\frac{\phi_k\gamma_kp_{\infty,k}}{\gamma_k-1}$ in place of the printed $+\sum_k\frac{\phi_kp_{\infty,k}}{\gamma_k-1}$; the paper does not say which convention the code uses.)*
- Eq. (11), Wood's sound speed, printed $\rho c^2=\frac{\phi_1}{\rho_1c_1^2}+\frac{\phi_2}{\rho_2c_2^2}$. *(Compiler check, not in the sources: the right side has the dimension of an inverse pressure, so the left side must be $1/(\rho c^2)$.)*
- §4.3.1: "In water medium, the volume fraction of air $\alpha_1=10^{-8}$", while phase 1 carries the liquid parameters $\gamma_1=4.4$, $p_{\infty,1}=6\times10^8$ Pa.
- §4.3.2: the shock is "leftward-moving" from $x=275$ mm towards a bubble at $x=225$ mm with post-shock velocity $-113.5$ m/s, yet "Inflow and outflow conditions are imposed on the left and right boundaries respectively". *(Compiler check, not in the sources: the post-shock state lies to the right of the shock, so the inflow boundary is the right one.)* The same section refers to "Fig. 11 in physical experiments [75]", while the paper's own Fig. 11 is the underwater-explosion sketch, and the Fig. 15 caption says "Example 6".
- §4.2.1: "the deepMTBVD scheme performs consistently with the MUSCL scheme … This indicates that the ANN accurately selected the THINC scheme"; Fig. 5 compares it with MUSCL-THINC-BVD. Typos: "MUSCH-THINC-BVD", "Woodward and Celella", "We donate $S_i$", "Rimemann".
- References: [75] (Haas & Sturtevant, J. Fluid Mech. 181) and [76] (Picone & Boris, J. Fluid Mech. 189) printed with the year 2006; [67] (ICCV 2017) with 2018.

# Notation map

| Huang, Cheng, Ying, Deng & Xiao | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar{\boldsymbol U}_i$, $\bar u_i$ | $\bar u_i$ | finite-volume averages |
| $\hat u^s_{i-1/2,R}$, $\hat u^s_{i+1/2,L}$ | $u^{s,+}_{i-1/2}$, $u^{s,-}_{i+1/2}$ | the two traces of cell $i$'s candidate $s$ |
| $\boldsymbol U^L$, $\boldsymbol U^R$ | $u^-$, $u^+$ | |
| $\mathcal A^\pm\Delta\boldsymbol U$, $s^k$, $\boldsymbol W^k$ | fluctuations, wave speeds, waves (local) | LeVeque–Shyue form |
| $\boldsymbol A(\boldsymbol U^L,\boldsymbol U^R)$ | dissipation matrix of the flux (local) | printed without $\tfrac12$ |
| $\sigma_i$, $\tilde\Delta$ | $\mathsf s_i$ (local), van Leer $\psi$ | **collision** with the sigmoid $\sigma(x)$ of §3.3.1 |
| $\beta$, $\tilde x_i$ | $\beta_{\mathrm T}$, $x^c_i$ | **collision** of $\beta$ with $\beta_k$ |
| $\theta$, $A$, $B$, $C$, $\epsilon=10^{-20}$ | $\theta_{\mathrm T}$, $\mathcal A$, $\mathcal B$, $\mathsf C$ (local) | $\mathsf C=(\varsigma+1)/2$; **collision** of $\theta$ with the Zhang–Shu factor |
| $\delta$ | $10^{-8}$ in Eq. (24), $10^{-3}$ in Algorithm 1 | **two meanings** in the source; **collision** with $\delta_k$ |
| $BV$, $TBV^s_{i,\min}$, $M$, $T$ | $\mathrm{BV}$, $\mathrm{TBV}$ (local), MUSCL, THINC | |
| $\chi_i$ | $\chi^{\mathrm m}_i$ (local) | **collision** with the TENO $\chi_k$ |
| $\zeta=10^{-15}$ | flat-stencil threshold (local) | **collision** with $\zeta$ (characteristic variables) |
| $\kappa$, $\kappa_t$, $\kappa_{\rm ref}$ | $\kappa_{\mathrm{NN}}$, $\kappa_t$, $\kappa_{\mathrm{ref}}$ (local) | **collision** with the kinetic energy $\kappa$ |
| $\omega_t$, $\eta$ | $c_t$, $\eta_{\mathrm f}$ (local) | **collision** with $\omega_k$ and the entropy $\eta$ |
| $\alpha_k$, $\rho_k$, $\gamma_k$, $p_{\infty,k}$, $e_{\infty,k}$ | $\phi_k$, $\rho_k$, $\gamma_k$, $p_{\infty,k}$, $e_{\infty,k}$ (local) | |
| $\boldsymbol V$ | $v$ | |

# Reference list

The paper prints 77 references, numbered [1]–[77]. The list is merged complete into
the [bibliography](/bibliography.md), with `citedby` including `huang-2025-b`.
Refs. [32], [51] and [52] are the ingested [Huang et al. (2025a)](/sources/huang-2025.md),
[Bezgin et al. (2022)](/sources/bezgin-2022.md) and
[Nogueira et al. (2024)](/sources/nogueira-2024.md). Ref. [49] (Yu & Shu,
multi-layer perceptron estimator of the TVB constant, Mathematica 1) is a different
work from the planned source of the same key and takes the key it already has in
the bibliography. The Deng 2018 and Lu 2021 pairs are suffixed in printed order and
matched by volume and page. Ref. [41] has the first author "W. E"; ref. [61] (Wood
& Lindsay, *A textbook of sound*) is printed as a Physics Today item; refs. [28],
[38], [42], [46], [47], [51] and [55] are printed without pages or article numbers.
No printed duplicates; no item is unparseable.

# Pages created or updated

Chunk 10 (2026-10-23). This source is cited on:

* [Boundary variation diminishing (BVD)](/definitions/boundary-variation-diminishing.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Five- and six-equation diffuse-interface models](/definitions/five-equation-model.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Learned WENO weights](/methods/learned-weno-weights.md)
* [Mach 3 forward-facing step](/benchmarks/forward-facing-step.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)
* [THINC reconstruction](/methods/thinc-reconstruction.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [Underwater explosion](/benchmarks/underwater-explosion.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)

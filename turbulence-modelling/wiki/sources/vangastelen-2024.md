---
type: Source
title: "van Gastelen et al. (2024) — Energy-conserving neural network for turbulence closure modeling"
description: "Builds a discretize-first neural closure for 1D Burgers and Korteweg–de Vries whose skew-symmetric-plus-dissipative structure and auxiliary subgrid-energy variables make it stable for any weights, conserve momentum and allow backscatter, matching a vanilla CNN in accuracy but not in robustness."
resource: "doi:10.1016/j.jcp.2024.113003"
source_kind: paper
authors: [van Gastelen T., Edeling W., Sanderse B.]
year: 2024
venue: "J. Comput. Phys. 508:113003"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Journal_of_Computational_Physics_van_Energy-conserving_neural_network_for_turbulence_closure_mode.pdf"
tags: [neural-network, structure-preserving, backscatter, discretization-consistent-closure, burgers]
timestamp: 2026-10-26T10:26:00Z
---

# Summary

van Gastelen et al. (2024) build a machine-learned closure for the filtered
discrete equations of two 1D model problems, viscous Burgers and
Korteweg–de Vries (KdV). By construction the closure is stable and can still
represent [backscatter](/definitions/energy-backscatter.md). The approach is
"discretize first, filter next", in the sense of
[discretization-consistent closure](/definitions/discretization-consistent-closure.md).
An energy-conserving fine-grid discretization (skew-symmetric convection, see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)) is
filtered by a discrete cell average onto a coarse grid. With a piecewise-constant
reconstruction, the discrete energy splits exactly into a resolved part and a
subgrid part. The exact closure term is the discrete commutator error and
includes the discretization error.

The contribution is an energy-conserving [neural-network closure](/methods/neural-network-sgs-model.md).
Auxiliary subgrid variables $\mathbf s$ are added, one per coarse cell. They are
a linear compression of the subgrid content found by an SVD, and $\tfrac12\|\mathbf s\|^2$
approximates the subgrid energy. The extended state is closed by a CNN-parameterized
skew-symmetric operator, which exchanges energy between resolved and subgrid
variables without creating it, plus a dissipative operator. The modelled total
energy then cannot grow for any network weights, as long as the coarse
discretization conserves energy. Zero-sum convolution weights conserve momentum
to machine precision. Training starts with derivative fitting and finishes with
trajectory fitting, a form of [model-consistent training](/methods/model-consistent-training.md).

The model is compared with a vanilla CNN closure, a constant-coefficient
[Smagorinsky](/methods/smagorinsky-model.md) model and no closure, all tested
[a posteriori](/definitions/a-priori-and-a-posteriori-testing.md) against the
filtered fine-grid solution (called DNS; a 1D resolved discretization, not a
3D [DNS](/definitions/direct-numerical-simulation.md)). The structure-preserving
model is stable in every test, about one order of magnitude more accurate than no
closure, and better than Smagorinsky on Burgers. Its accuracy is roughly on par
with the CNN, which is better on KdV at most resolutions. Its advantage is
robustness: it is consistent across training seeds, extrapolates better in
viscosity, and stays physical in a space-time extrapolation of KdV. The
introduction places it among [LES](/definitions/large-eddy-simulation.md)
closures that remove backscatter by clipping or a
[dynamic procedure](/methods/dynamic-procedure.md), and among
[reinforcement-learning](/methods/reinforcement-learning-closure.md) and
[physics-informed](/methods/physics-informed-neural-network.md) approaches.

# Version read

arXiv:2301.13770v5 [math.NA] (15 March 2024; footer "Preprint submitted to
Elsevier, March 18, 2024"), the post-review text (the acknowledgements thank
the reviewers), not the typeset version of record. 34 pages (main text
pp. 1–24, references pp. 25–27, Appendices A–E pp. 28–34), all read. Locators
are the preprint's sections, equations, figures and appendices. Title and
authors match Crossref. The coarse time step carries an overbar that the text
extraction loses (Eq. 52); it is restored from the stated meaning. Code:
github.com/tobyvg/ECNCM_1D (Julia).

# Key claims

1. With the averaging filter $\mathbf W=\mathbf M_H^{-1}\mathbf O\mathbf M_h$ and the reconstruction $\mathbf R=\mathbf O^T$, $\mathbf W\mathbf R=\mathbf I$; inner products are invariant under reconstruction, $(\mathbf R\bar{\mathbf a},\mathbf R\bar{\mathbf b})_{h}=(\bar{\mathbf a},\bar{\mathbf b})_{H}$, and $\mathbf R\bar{\mathbf u}$ is orthogonal to $\mathbf u^<$ in the fine inner product (§2.3, §2.5, Eqs. 19, 27; App. A, Eqs. A.1–A.3). **Proved**
2. The total discrete energy splits exactly, $\mathcal E_h=\tfrac12\|\bar{\mathbf u}\|^2_H+\tfrac12\|\mathbf u^<\|^2_h=\bar{\mathcal E}_h+\mathcal E^<_h$; in the inviscid limit only the sum is conserved, so the resolved energy can increase (backscatter) while the total decreases (§2.5, Eqs. 28–29; Fig. 2 right, KdV). **Proved** (decomposition), **Shown** (exchange)
3. Discrete momentum is invariant under filtering, $(\mathbf 1_h,\mathbf u)_h=(\mathbf 1_H,\bar{\mathbf u})_H$, so the exact closure term adds no momentum, $(\mathbf 1_H,c(\mathbf u))_H=0$ (§2.6, Eqs. 31–32; App. A, Eq. A.4). **Proved**
4. The closure term $c(\mathbf u)=\mathbf W f_h(\mathbf u)-f_H(\bar{\mathbf u})$ is the discrete equivalent of the LES commutator error and also contains the discretization error relative to the fine-grid simulation (§2.4, Eq. 24). **Derived**
5. The extended system (Eq. 33) satisfies $d\mathcal E_s/dt=(\bar{\mathbf u},f_H(\bar{\mathbf u}))_H-\|\mathbf Q\mathbf a\|_2^2$, the skew-symmetric term cancelling, so "this formulation guarantees stability provided that $f_H$ is structure-preserving", whatever the network weights (§3.1, Eq. 37). **Proved**
6. The exact-energy choice $\mathbf s=\pm\sqrt{\mathbf W(\mathbf u^<)^2}$ "resulted in poor performance during testing": small model errors flipped the sign of some $s_i$ and the simulation diverged, and "attempts at resolving this issue were not successful"; the authors use the local linear compression $s_i=\mathbf t^T\boldsymbol\mu_i$ instead (§3.2). **Stated** (no data shown)
7. The optimal compression vector is $\mathbf t=J^{-1/2}\hat{\mathbf t}$, with $\hat{\mathbf t}$ the first left singular vector of the subgrid snapshot matrix; minimizing the energy error is equivalent to minimizing the projection error (App. C, Eq. C.1). **Derived**
8. For a Burgers snapshot ($\nu=0.01$, $N_x=1000$, $I=20$, $J=50$), the compressed subgrid energy $\tfrac12\|\mathbf s\|^2_H$ captures the true subgrid energy "both qualitatively and quantitatively", including the oscillations from the travelling shock, though some energy is missed (§3.2, Fig. 3). **Shown**
9. Momentum conservation of the closure holds to machine precision for any parameters when the weights of the convolutions $\mathbf B_i^{j1}$ are made zero-sum, $\bar b_j=b_j-\sum_kb_k/(2B+1)$ (§3.3.3, Eqs. 47–50). **Derived**
10. In the trained Burgers model the skew-symmetric (energy-redistributing) term $\|(\mathbf K-\mathbf K^T)\mathbf a\|$ is the largest term, larger than the coarse discretization $\|f_H(\bar{\mathbf u})\|$ (§3.3.4, Fig. 5). **Shown**
11. Appendix B argues that a closure must add dissipation: the fine-grid diffusion operator removes at least as much energy as the coarse one, provided the eigenvalues of the difference operator $\mathbf D^\Delta$ are nonpositive; this is supported only by a "numerical 'proof'" (Fig. B.17) for realistic $I$ and $J$ (App. B, Eqs. B.1–B.2). **Shown** (numerically), not **Proved**
12. The compression error on the validation set converges monotonically under coarse-grid refinement, DOF $\in\{20,\dots,100\}$, for Burgers ($N_x=1000$) and KdV ($N_x=600$); the authors attribute the faster KdV convergence to its lower fine-grid resolution (§4.3.1, Fig. 6). **Shown**
13. For Burgers cases (i) and (ii), no closure, Smagorinsky and the structure-preserving model show "almost monotonic convergence" of the integrated error; "SP improves upon NC with roughly one order of magnitude, surpassing SM"; the CNN error is erratic, "sometimes less accurate than NC (case (i), DOF = 90)" (§4.3.1, Fig. 7). **Shown**
14. For KdV the CNN outperforms the structure-preserving model at most DOF but yields no stable models at DOF $\in\{90,100\}$; the structure-preserving model is slightly better at the lowest DOF (§4.3.1, Fig. 7). **Shown**
15. Cost: for Burgers both learned models are "at least 2× faster than the DNS", the CNN slightly cheaper; a DNS takes at most 5 s on a laptop CPU and training about 20 min per network; for KdV the speed-up is "roughly 20×", attributed to the DNS time step $10^{-4}$, larger DNS steps being unstable (§4.3.2, Fig. 7 bottom). **Shown**
16. Over 10 replica models per method at DOF = 60 differing only in random seed (20 simulations each), every structure-preserving model produced only stable simulations and their errors nearly overlap; CNNs are "hit or miss", with large outliers, and in case (ii) two CNN models were 100% unstable (§4.4, Fig. 8). **Shown**
17. For KdV (DOF = 40) the structure-preserving model and the CNN conserve momentum "up to machine precision (single-precision)", and the structure-preserving model also conserves energy to that level (§4.5, Fig. 9); the conclusion words the energy result as "energy conservation up to a time discretization error" (§6). **Shown**
18. For Burgers (DOF = 40) the modelled total energy always decreases while the resolved energy oscillates through backscatter, matching the filtered DNS qualitatively (§4.5, Fig. 10). **Shown**
19. In the unstable CNN case (Burgers, DOF = 90) noise builds up and energy accumulates at high wavenumbers from about $t=2$; Smagorinsky is too dissipative, no closure not dissipative enough, and the structure-preserving model captures the energy trajectory and spectrum; it shows, and no closure to a lesser extent, the expected $k^{-2}$ slope (§4.6, Figs. 11–12). **Shown**
20. Viscosity extrapolation: trained on $\nu\in[10^{-2},10^{-1}]$ (5 log-spaced values, $N_x=5000$), tested on 9 values in $[10^{-3},10^{-1}]$ at DOF 50 and coarse time step 0.01, the "SP scheme consistently outperforms the other closure models" inside and outside the training range; the CNN degrades as $\nu$ decreases even inside it, and Smagorinsky beats no closure everywhere (§4.7, Fig. 13). **Shown**
21. Space-time extrapolation on KdV (domain $[0,96]$, $T=50$, 3× and 5× the training data): the structure-preserving model stays free of numerical noise and reproduces the resolved-energy distribution of the DNS; the CNN's resolved energy exceeds the DNS total energy, a "nonphysical influx of energy"; the CNN has the lower error early on and the structure-preserving model "slowly catches up" past the training region (§4.8, Figs. 14–16). **Shown**
22. Without closure the resolved energy is conserved in the KdV extrapolation, because the coarse discretization conserves energy (§4.8). **Shown**
23. The vanilla CNN closure conserves momentum by multiplying its output by a forward-difference operator (§4.1.1, Eq. 53, credited to refs. [24, 32]). **Stated**
24. The constant-coefficient Smagorinsky model was chosen as "the best performing non-machine learning closure in [32], outperforming the dynamic Smagorinsky model" (§4.1.1). **Stated** (cited)
25. Open problems for 2D/3D Navier–Stokes (§5): the dependence on the compression factor $J$ (remedies: training over several $J$, continuous or finite-element formulations, graph convolutions, Fourier neural operators); linear compression may limit 2D/3D, autoencoders being an alternative; the 3D analogue of $\mathbf s$ is "probably the sub-grid scale stress tensor", requiring several subgrid equations. **Stated**
26. Parameter counts: 2780 (Burgers) and 5352 (KdV) for the structure-preserving model, 3261 for the CNN (§4.2, Table E.1). **Stated**

The closure (Eqs. 33, 37) in the notation of this page, with
$\mathbf a=[\bar{\mathbf u};\mathbf s]\in\mathbb R^{2I}$ and
$\mathbf M_2=\mathrm{blockdiag}(\mathbf M_H,\mathbf M_H)$:
$$\frac{d\mathbf a}{dt}=\begin{bmatrix}f_H(\bar{\mathbf u})\\ \mathbf 0\end{bmatrix}+\mathbf M_2^{-1}(\mathbf K-\mathbf K^T)\mathbf a-\mathbf M_2^{-1}\mathbf Q^T\mathbf Q\mathbf a,\qquad \frac{d\mathcal E_s}{dt}=(\bar{\mathbf u},f_H(\bar{\mathbf u}))_H-\|\mathbf Q\mathbf a\|_2^2,$$
with $\mathcal E_s=\tfrac12\|\mathbf a\|^2_{\mathbf M_2}$, $\mathbf Q=\mathbf q\mathbf B_1$, $\mathbf K=\mathbf B_2^T\mathbf m\mathbf B_3$, and the diagonal fields $\mathbf q$, $\mathbf m$ the outputs of a CNN fed with $\bar{\mathbf u}$, $\mathbf s$ and $f_H(\bar{\mathbf u})$ (Eqs. 43–46). For KdV the dissipative part is omitted (§4.2).

# Printed slips

- **Duplicate reference:** refs. [29] and [32] are the same work, printed identically (Shankar et al., "Differentiable physics-enabled closure modeling for burgers' turbulence", Mach. Learn.: Sci. Technol. 4 (2023) 015017); ref. [49] is its arXiv preprint.
- **§1:** "In [29] physics-informed neural networks (PINNs) were succesfully applied to Burgers' equation"; [29] is the differentiable-physics closure paper of Shankar et al., not a PINN paper.
- **Eq. 57:** "NMRSE" for NRMSE.
- **App. C, first sentence:** "such that $s\approx\mathbf W(\mathbf u')^2$", while §3.2 prints "$s^2\approx\mathbf W(u')^2$"; the square is missing in App. C.
- **CNN input:** printed $f(\bar u)$ in Eq. 45, $f_H(\bar u)$ in §3.3.1, $f_h(\bar u)$ in Eq. 53, where the closure is also written $\tilde c(\mathbf u;\Theta)$ with argument $\mathbf u$ rather than $\bar{\mathbf u}$.
- **Energy conservation wording:** "up to machine precision (single-precision)" (§4.5, Fig. 9) against "energy conservation up to a time discretization error" (§6).
- **Fig. 13:** the y-axis reads "NRMSE ū", the caption "Integrated solution error".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $N$ (fine-grid points) | $N_x$ | **collision** with the polynomial degree $N$ |
| $I$, $J$ | $I$, $J$ | page-local: coarse cells, fine cells per coarse cell ($N_x=IJ$) |
| $h$, $H$ | $h$, $H$ | fine and coarse grid spacing, $h=H/J$ |
| $\omega$, $\Omega$ (mass matrices) | $\mathbf M_h$, $\mathbf M_H$ | **collision** with the specific dissipation rate $\omega$ and the rotation tensor $\Omega_{ij}$; $\Omega$ is also the domain |
| $(\cdot,\cdot)_\omega$, $(\cdot,\cdot)_\Omega$ | $(\cdot,\cdot)_h$, $(\cdot,\cdot)_H$ | page-local inner products |
| $\Omega_2$ | $\mathbf M_2$ | |
| $\bar{\mathbf u}=\mathbf W\mathbf u$ | $\bar{\mathbf u}$ | overbar = discrete top-hat (cell-average) filter, consistent with the registry |
| $\mathbf u'=\mathbf u-\mathbf R\bar{\mathbf u}$ | $\mathbf u^<$ | **collision:** the prime is the registry's Reynolds fluctuation |
| $E_h$, $\bar E_h$, $E'_h$, $E_s$ | $\mathcal E_h$, $\bar{\mathcal E}_h$, $\mathcal E^<_h$, $\mathcal E_s$ | discrete kinetic energies; $E$ is the registry's total energy |
| $\mathbf s$, $\mathbf t$, $\boldsymbol\mu_i$ | same, page-local | subgrid variables, compression vector, subgrid content of cell $i$ |
| $\mathbf K$, $\mathbf Q$ | same, page-local | learned skew-generating and dissipative operators; the source also writes $\mathbf Q$ for the forward difference (Eq. 9) |
| $\mathbf k$, $\mathbf q$ (CNN outputs) | $\mathbf m$, $\mathbf q$ | **collision:** $k$ is the turbulent kinetic energy (and the wavenumber in §4.6) |
| $\Theta$ | $\boldsymbol\theta$ | trainable parameters |
| $\varepsilon$, $\mu$ (KdV) | $\varepsilon_{\mathrm{KdV}}$, $\mu_{\mathrm{KdV}}$ | **collision** with the dissipation rate and the viscosity |
| $C_s$, $\boldsymbol\nu_t=(hC_s)^2\lvert\bar{\mathbf Q}\bar{\mathbf u}\rvert$ | $C_s$, $\nu_t$ | filter width = coarse grid spacing; fitted $C_s$ not reported |
| $L$, $L_n$, $L_s$ | $\mathcal L$ | derivative-fitting, trajectory-fitting and compression losses |
| derivative fitting / trajectory fitting | a priori / a posteriori training | the paper does not use the registry terms |
| $k$ (§4.6) | $k$ | wavenumber in the spectra |

# Reference list

58 printed references, numbered [1]–[58] in Elsevier numbered style with DOIs.
The list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. The printed duplicate [29]/[32] is one work and is folded
into one entry (`shankar-2023`); its arXiv preprint [49] is a distinct entry. Ref. [10] is the
2022 arXiv preprint of the ingested `prakash-2022` and stays a distinct entry (`prakash-2022-b`);
ref. [25] is the arXiv preprint of the ingested `kurz-2023` and stays
distinct (`kurz-2022-d`); ref. [33] (Kang & Constantinescu, arXiv 2023) is a different work
from the ingested `kang-2023` (`kang-2023-b`); ref. [26] is the ingested
`bae-2022`. Parsing remarks: [53] has an acknowledgement footnote glued to its
title (truncated); [4], [43] print no pages, [46] no volume.

# Pages created or updated

Chunk 5 (2026-10-26). This source is cited on:

- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Discretization-consistent closure](/definitions/discretization-consistent-closure.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Model-consistent (a posteriori) training of learned closures](/methods/model-consistent-training.md)
- [Neural-network subgrid-scale models](/methods/neural-network-sgs-model.md)
- [Physics-informed neural networks for RANS](/methods/physics-informed-neural-network.md)
- [Reinforcement-learning turbulence closures](/methods/reinforcement-learning-closure.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)

---
type: Source
title: "de Romémont et al. (2026) — A data-driven learned discretization approach in finite volume schemes for hyperbolic conservation laws and varying boundary conditions"
description: "Second-order MUSCL finite-volume scheme whose slopes are three-point stencils with coefficients predicted by a convolutional network, kept under the van Albada limiter and trained against decimated fine-grid solutions with entropy and total-variation penalties; boundary types enter through padding, slip walls through transfer learning."
resource: "doi:10.1016/j.compfluid.2026.106978"
source_kind: paper
authors: [de Romémont G., Renac F., Nunez J., Gueyffier D., Chinesta F.]
year: 2026
venue: "Comput. Fluids 307:106978"
local_file: "/home/stefano/papers/mosaic/weno-teno/2026_Crossref_Computers_amp_Fluids_de_A_data-driven_learned_discretization_approach_in_finite_volu.pdf"
tags: [machine-learning, muscl, finite-volume, limiting, boundary-conditions]
timestamp: 2026-10-23T20:43:00Z
---

# Summary

de Romémont et al. (2026) carry the "learned discretization" of Bar-Sinai et al.
(data-driven stencil coefficients, earlier applied to smooth finite-difference
solutions) into a second-order [MUSCL](/methods/muscl-hancock.md) finite-volume
scheme for scalar laws and the compressible Euler equations in 1D and 2D, with
discontinuities and non-periodic boundaries. A convolutional network reads the
min–max normalized primitive variables and returns, in each cell and for each
variable and direction, three coefficients $(\mathsf a_{-1},\mathsf a_0,\mathsf a_1)$
of a learned slope $\Delta x\,\hat\partial_xu_i=\sum_j\mathsf a_ju_{i+j}$; a final
linear layer imposes $\sum_j\mathsf a_j=0$. The learned slope replaces the finite
difference inside MUSCL, and the van Albada
[limiter](/definitions/total-variation-diminishing.md) is kept, applied to the ratio
of learned slopes. The flux is the [Rusanov flux](/methods/lax-friedrichs-flux.md)
and time stepping is explicit Euler. It is the MUSCL-type counterpart of the
[learned WENO weights](/methods/learned-weno-weights.md): the network sets stencil
coefficients, the classical limiter stays in charge of monotonicity.

Training is supervised against fine-grid solutions decimated by a factor 2, with
$L^1$ and $L^2$ errors plus three soft penalties (a discrete entropy inequality, a
total-variation increase and an $L^1$ norm of the network parameters). Because the
limited scheme is stable on its own, the authors train on single steps, without the
multi-step unrolling of earlier learned discretizations. Boundary types enter
through padding layers; at slip walls the learned contribution is set to zero, and a
model trained on periodic data is fine-tuned on slip-wall data.

Tests are run on Burgers data ([Burgers tests](/benchmarks/burgers-equation-tests.md)),
[Sod](/benchmarks/sod-and-lax-shock-tubes.md), [Shu–Osher](/benchmarks/shu-osher-problem.md),
four Lax–Liu [2D Riemann problems](/benchmarks/two-dimensional-riemann-problems.md),
a circular [explosion](/benchmarks/explosion-and-implosion-problems.md) and the
[forward-facing step](/benchmarks/forward-facing-step.md). They report $L^1$ error
reductions from 6% (explosion) to 49.2% (Sod) against the same scheme on the same
coarse grid; the abstract summarizes them as "20–50% gains". In the time-step study
of Appendix A the gain becomes negative from $\nu=0.44$ on. On smooth data the two
schemes give the same second-order errors.

# Version read

The archive file is the version of record (Comput. Fluids 307:106978, received 19
February 2025, online 19 January 2026), 17 pages, all read. Pages 7–10 were also
checked on the page images for the von Neumann formula and the 2D Riemann data.
Page 1 matches the Crossref record (title, five authors, venue, DOI). The 1D Burgers
code is released at `https://github.com/guigzair/Burgers_1D` (§1).

# Key claims

Registry notation: conserved $u$ (source $\mathbf w$), cells $I_i$ of width
$\Delta x$ (source $h$), traces $u^\pm_{i+1/2}$, entropy pair $(\eta,F_\eta)$
(source $(\eta,\boldsymbol q)$), limiter $\psi(r_i)$ (source $\Phi$), CFL number
$\nu$ (source $C_{CFL}$). Page-local: learned coefficients $\mathsf a_j$ (source
$\alpha_j$), $\mathsf C_o=\Delta t/\Delta x$ (source $Co$), resolution ratio
$\mathsf R=\Delta x_{\mathrm{coarse}}/\Delta x_{\mathrm{fine}}$, loss weights
$c_2,c_{\mathrm{ent}},c_{\mathrm{TV}},c_{\mathrm{reg}}$ (source $\lambda_\bullet$),
amplification factor $\hat S$.

1. The method extends the learned interpolation of Bar-Sinai et al. to MUSCL-type finite-volume approximations of scalar laws and systems, with discontinuous solutions and varying boundary conditions (abstract, §1). **Stated**
2. The learned model "accurately reproduces fine-grid results on very coarse meshes achieving 20–50% gains in accuracy" against the standard second-order scheme on the same grid (abstract, §1, §9). **Shown**; the gains printed in §6 range from 6% (explosion) to 49.2% (Sod), see claims 13–15.
3. Because the flux-limited scheme is stable on its own, training needs no error accumulation over unrolled steps, unlike earlier learned discretizations, which "significantly" reduces training time (§1, §4.4, §4.6, §9). **Stated** (no timing comparison with unrolled training)
4. The entropy penalty, $\mathcal L_{\mathrm{ent}}=\sum_j\max\big(0,\int_{I_j\times T_j}\partial_t\eta+\nabla\cdot F_\eta\big)^2$ (Eq. 21), "aims at enforcing the model to capture the unique entropy weak solution" (§4.4). **Stated**; it is a soft term of the loss, and no discrete entropy inequality is proved for the scheme.
5. The total-variation penalty $\max\big(0,TV(u^{n+1})-TV(u^n)\big)$ (Eq. 24) is a soft constraint against spurious oscillations; the authors note that a TV bound does not hold in general in several dimensions or for systems (§4.4). **Stated**
6. The $L^1$ penalty on all network parameters (Eq. 25) "has an effect of reducing oscillations for strong shocks" (§4.4). **Stated**
7. A three-point slope stencil (half-width 1) suffices: "no remarkable improvement comes from increasing the stencil size" (§4.6). **Stated** (no larger-stencil results shown)
8. At slip walls, mirroring the flow in the padding creates an artificial discontinuity and an unphysical shock; "symmetric" padding, which zeroes the learned contribution at the wall, stabilizes the scheme (§4.3, Table 1). **Stated**
9. Without the transfer-learning step (periodic training, then fine-tuning on slip-wall data with the coefficients zeroed at edges), the method "has a tendency to diverge" at walls (§4.6). **Stated**
10. The model is trained with explicit Euler at $\mathsf C_o=0.01$, and the authors say the method "is not constrained by the temporal resolution of the training data, allowing users to freely select time steps" (§1, §6, §9). **Shown** only for Sod in Table A.1, where the gain is 49.1% at $\mathsf C_o=0.01$ ($\nu=0.022$), 33.8% at $\mathsf C_o=0.1$, $-20.8\%$ at $\mathsf C_o=0.2$ ($\nu=0.44$) and $-56.8\%$ at $\mathsf C_o=0.3$.
11. With the limiter set to 1 and the coefficients frozen at a base state, $\bar{\mathsf a}_j$, linear advection gives $\hat S(\vartheta)=1-\nu(1-e^{-\mathrm i\vartheta})\big(1+\tfrac12[\bar{\mathsf a}_{-1}(e^{-\mathrm i\vartheta}-1)+\bar{\mathsf a}_1(e^{\mathrm i\vartheta}-1)]\big)$ (§5). **Derived** *(compiler check, not in the sources: re-derived from the printed linearized scheme using $\bar{\mathsf a}_0=-\bar{\mathsf a}_{-1}-\bar{\mathsf a}_1$; it agrees.)*
12. Fig. 4 shows less dissipation and a phase closer to the exact one for the trained coefficients than for the centred slope $(-\tfrac12,0,\tfrac12)$; the conclusion says the analysis "confirms a reduction of the dispersion and dissipation errors" (§5, §9; see [approximate dispersion relation](/definitions/approximate-dispersion-relation.md)). **Shown**; the frozen $\bar{\mathsf a}_j$, the base state and $\nu$ of Fig. 4 are not printed, and the comparison is with the centred slope, not with the van Albada reference scheme.
13. 1D Euler: Sod, 128 coarse cells against 1024 fine, gain 49.2%, errors reduced mainly near sharp gradients; Shu–Osher, 1024 against 4096 cells, gain 46% (§6.2, Figs. 7–8). **Shown**
14. 2D Riemann problems, $512^2$ against $2048^2$: Lax–Liu configuration 3, gain 22%, with residual artefacts and lost symmetry between the two plumes; configuration 4, 39%; configuration 6, 48%, with "notably high" symmetry; configuration 12, 28% (§6.3, Figs. 10–13). **Shown**
15. Explosion, $256^2$ against $1024^2$: gain 6%. Forward-facing step, $384\times128$ against $768\times256$: gain 19%, with an overshoot and spurious oscillations attributed to "the double boundary condition at the corner" (§6.3, Figs. 14–15). **Shown**
16. Burgers with the Ray–Hesthaven composite data, 256 against 1024 cells, $t=0.39$: smaller and narrower error spikes at discontinuities; no gain number printed (§6.1, Fig. 6). **Shown**
17. Convergence study, 2D Euler, periodic, $\mathsf C_o=0.03$: the learned solver has lower error on randomized Riemann data; on an advected sine wave both solvers are "identical", second order is approximately retrieved and "the standard FV scheme is slightly better" (§7, Fig. 16). **Shown**
18. Cost on one NVIDIA V100: on a fixed mesh the learned solver is slower (inference and padding; TensorFlow lacks in-place updates and periodic padding); time against mesh size has slopes $-1.1$ (learned) and $-1$ (reference) on a log–log plot; at a given error level the two solvers have "comparable computational performances" (§8, Fig. 17). **Shown**
19. The 1D models have about 3500 trainable parameters and the 2D Euler model 10 500; training takes about 10 min (1D Euler, §4.6) and 6 h (2D Euler) on one V100. **Stated**
20. A second-order Heun integrator gave no improvement of the reference solutions and lengthened training (§3.1). **Stated**
21. The stability bound of the learned method "seems a bit lower" than that of the standard MUSCL–Rusanov scheme (§6). **Shown** only through Table A.1.
22. Restricting the network to coefficient prediction inside a finite-volume scheme avoids the "black-box issues" of end-to-end solvers and PINNs (§1, §9). **Stated**
23. None of the test cases of §6 is in the training data (§6). **Stated**

# Printed slips

- §5: "with $C_{FL}=\frac{ah}{\Delta t}$ the CFL number as defined in Eq. (15)". Eqs. (14)–(15) define $Co=\Delta t/h$ and $C_{CFL}=Co\times\lvert\lambda\rvert_{max}$, that is $a\Delta t/h$; the printed ratio is inverted.
- §3.2.2, subsonic inflow: $\boldsymbol v_\Gamma=\boldsymbol v_{-1}-\frac{\boldsymbol n(p_{-1}-p_\Gamma)}{p_0c_0}$, where the subsonic-outflow formula of the same section has $\rho_0c_0$. *(Compiler check, not in the sources: only $\rho_0c_0$ makes the quotient a velocity.)*
- §4.2: the constraint $\sum_{j=-k}^k\alpha_j=0$ "enforces the derivative to be at least first-order accurate". *(Compiler check, not in the sources: by Taylor expansion, $\sum_j\alpha_ju(x+jh)=u\sum_j\alpha_j+hu'\sum_jj\alpha_j+O(h^2)$ with $\alpha_j$ carrying $1/h$ as in Eq. (16), so consistency also needs $h\sum_jj\alpha_j=1$, which is not stated as imposed.)*
- §2.4: the slip-wall boundary state is printed $(\rho,\rho(\boldsymbol v-(\boldsymbol v\cdot\boldsymbol n)\boldsymbol n)^T,\rho E)^T$, while the conserved vector is $(\rho,\rho\boldsymbol v^T,E)^T$ with $E$ per unit volume.
- Fig. 3 caption: "all primitives are normalized between 0 and 1"; §4.2: the normalization layer outputs all variables to $[-1,1]$.
- §5: "Fig. 4 shows the numerical dissipation and dispersion for Eq. (26)"; Eq. (26) is the error definition of §6, and the amplification factor is unnumbered. §7: "the choice of the stencil, $k=1$, in the ML reconstruction model Eq. (13)"; $k$ is defined in Eq. (16), the learned reconstruction is Eq. (17), and Eq. (13) is the reference MUSCL.
- Sod gain: 49.2% in §6.2, 49.1% in Table A.1 at $Co=0.01$, the setting of §6.
- Training time of the 1D models: "approximately 10mn … for the 1D Euler equations" (§4.6), "20mn for the 1D models" (§8).
- App. B.2: "50 initial conditions integrated on 10,000 time steps making 490,000 samples"; $50\times10\,000=500\,000$. App. B.4: "10 initial conditions composed of 37.5% $\mathbf f_1$, 37.5% $\mathbf f_2$ and 25% $\mathbf f_3$", which is not a whole number of conditions per family.
- App. A: "reaching $Co=0.1$ … both solutions explodes in finite time for the same CFL number (approaching 1.)"; Table A.1 lists $C_{CFL}=0.22$ at $Co=0.1$ and stops at $0.77$, and the value at which the runs blow up is not shown.
- Explosion test: the text cites "[65, Section 17.1.1]" (Toro's book), the Fig. 14 caption "[38]" (Liska & Wendroff). "[66, Section 2.4.2]" (§1) and "[66, Section 13.6]" (§4.4) cite section numbers in [66], a journal article (Toro & Billett, IMA J. Numer. Anal. 2000).
- "no-slip" (§4.6) and "non-slip boundary dataset" (App. B) for the slip-wall condition actually used; "$\forall t\in[O,T]$" (Eq. 22); "not induced by the tization" (§6, truncated word).
- Sod (Fig. 7) and Shu–Osher (Fig. 8) captions print the same final time $T=0.156$; neither test's initial data is printed.

# Notation map

| de Romémont et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf w$, $\mathbf u$ | $u$; primitive $(\rho,v,p)$ | reconstruction is in primitive variables, component by component |
| $r$ (number of variables) | $m$ | **collision** with the slope ratio $r$ of $\Phi(r)$ |
| $\Omega_a$ | $G$ | admissible set |
| $\eta$, $\boldsymbol q$ | $\eta$, $F_\eta$ | Euler $\eta=-\rho s$; Burgers $\eta=u^2/2$, $F_\eta=u^3/3$ |
| $h$, $I_i$, $x_{i\pm1/2}$ | $\Delta x$, $I_i$, $x_{i\pm1/2}$ | uniform Cartesian cells |
| $\mathbf w^\mp_{i+1/2}$ | $u^\mp_{i+1/2}$ | agree |
| $\hat{\mathbf f}$, $\rho(\mathbf w^-,\mathbf w^+)$ | $h^{\mathrm{LF}}$, $a$ | **collision** of the spectral radius $\rho$ with density |
| $A^\pm$, $\Lambda^\pm$, $R$ | $A^\pm$, $\Lambda^\pm$, $L$ | source $A=R^{-1}\Lambda R$, so its $R$ is the registry's left-eigenvector matrix $L$ |
| $\Phi$, $\phi_i$ | $\psi$, $\psi(r_i)$ | van Albada $\psi(r)=(r^2+r)/(r^2+1)$ |
| $\hat\partial_{x_p}$, $\alpha_j$, $\boldsymbol\alpha$, $k$ | $\hat\partial_{x_d}$, $\mathsf a_j$ (local), half-width | **collision** of $\alpha_j$ with the weights $\alpha_k$; carry $1/h$ in Eq. (16), dimensionless in §5 |
| $Co$ | $\mathsf C_o=\Delta t/\Delta x$ (local) | not the CFL number |
| $C_{CFL}$, $C_{FL}$ | $\nu$ | |
| $R$ (resolution ratio) | $\mathsf R$ (local) | **collision** with the eigenvector matrix |
| $\lambda_2,\lambda_{ent},\lambda_{TVD},\lambda_{reg}$ | $c_2,c_{\mathrm{ent}},c_{\mathrm{TV}},c_{\mathrm{reg}}$ (local) | **collision** with the eigenvalues $\lambda_l$ |
| $\hat S_h(k,\Delta t)$, $k$, $\theta$ | $\hat S(\vartheta)$, $k_w$, $\vartheta$ | **collision** of $\theta$ with the Zhang–Shu factor |
| $\mathbf L_{coarse}$, $\mathbf L_{ML}$ | mean $L^1$ errors (local) | against the decimated fine solution |

# Reference list

The paper prints 75 references, numbered [1]–[75] in Elsevier style. The list is
merged complete into the [bibliography](/bibliography.md), with `citedby` including
`deromemont-2026`. Ref. [36] (Li et al., finite volume graph network, arXiv 2023)
is a different work from the planned source of the same first-author key and takes
a disambiguated key; Kochkov et al. (PNAS 118) and Zhuang et al. (Phys. Rev. Fluids
6) are printed with the year 2021 and are matched by volume and page to the existing
entries. Three items are printed with garbled authors and are kept as printed with a
note: [11] "Da K." for the Adam paper (arXiv:1412.6980), [24] "Jessica LSE" and [72]
"Yu B, et al." (deep Ritz method). Ref. [20] (Harten) is printed with the 1997
reprint volume, J. Comput. Phys. 135. Printed arXiv identifiers lack the dot. No
printed duplicates; no item is unparseable.

# Pages created or updated

Chunk 10 (2026-10-23). This source is cited on:

* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Learned WENO weights](/methods/learned-weno-weights.md)
* [Mach 3 forward-facing step](/benchmarks/forward-facing-step.md)
* [MUSCL and MUSCL–Hancock schemes](/methods/muscl-hancock.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
* [Two-dimensional explosion and implosion problems](/benchmarks/explosion-and-implosion-problems.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)

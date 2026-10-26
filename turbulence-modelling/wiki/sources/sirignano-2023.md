---
type: Source
title: "Sirignano & MacArt (2023) — Deep learning closure models for large-eddy simulation of flows around bluff bodies"
description: "Trains one gated neural network, which closes all unclosed LES terms near and away from walls, through the continuous adjoint of the LES equations on short windows of filtered DNS of rectangular prisms; the closure runs stably for thousands of time units and matches or beats dynamic Smagorinsky, AMD and no-model LES out of sample."
resource: "doi:10.1017/jfm.2023.446"
source_kind: paper
authors: [Sirignano J., MacArt J.F.]
year: 2023
venue: "J. Fluid Mech. 966:A26"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Journal_of_Fluid_Mechanics_Sirignano_Deep_learning_closure_models_for_large-eddy_simulation_of_fl.pdf"
tags: [les, sgs-model, neural-network, model-consistent-training, a-priori-a-posteriori, separated-flow]
timestamp: 2026-10-26T07:37:00Z
---

# Summary

Sirignano & MacArt (2023) build a deep-learning closure for incompressible
[LES](/definitions/large-eddy-simulation.md) of flow around bluff bodies and
train it **in situ**, through the solver, by
[model-consistent training](/methods/model-consistent-training.md): the
gradient of the loss comes from the continuous adjoint of the LES equations
in mapped coordinates. One gated $\tanh$ network maps the filtered
velocity-gradient tensor to a $3\times3$ tensor whose divergence replaces
*all* unclosed terms: the divergence of the SGS stress, plus the terms that
filtering produces at the immersed body and on non-uniform meshes. The same
network acts at near-wall and far-field points, so the LES uses no separate
[wall model](/methods/machine-learning-wall-model.md)
([neural-network SGS models](/methods/neural-network-sgs-model.md)). The
loss is the mismatch with filtered DNS at the end of many windows of 0.1
time units, each started from filtered DNS. The authors set this against
[a priori](/definitions/a-priori-and-a-posteriori-testing.md) training and
against [reinforcement learning](/methods/reinforcement-learning-closure.md),
and they list adjoint-based RANS corrections
([field inversion](/methods/field-inversion-machine-learning.md)) as
precedents.

The [DNS](/definitions/direct-numerical-simulation.md) database holds four
rectangular prisms in confined cross-flow (aspect ratios 1, 2 and 4,
$Re=1000$ or $2000$ on the prism height). LES grids keep $1/64$ or $1/512$
of the DNS points. Two networks are trained on one case each and compared
with no-model [implicit LES](/definitions/implicit-les.md), the
[dynamic](/methods/dynamic-procedure.md)
[Smagorinsky model](/methods/smagorinsky-model.md) and the
[anisotropic minimum-dissipation model](/methods/anisotropic-minimum-dissipation-model.md).
Although trained only on short windows, the learned closures run stably for
thousands of time units. They match or beat the baselines on drag,
mean streamlines, resolved stresses and near-wall profiles, in and out of
sample. A network of identical architecture trained a priori fits the SGS
stress almost perfectly but does worse a posteriori. Both learned models
also run in a second solver, on a triangular prism and a cylinder: they
stay stable and are in some cases accurate, which bears on
[discretization consistency](/definitions/discretization-consistent-closure.md).
The baselines use the [Boussinesq](/definitions/boussinesq-hypothesis.md)
eddy-viscosity form; the learned closure does not. The authors name
[tensor-basis](/methods/tensor-basis-neural-network.md) architectures as
future work.

# Version read

Version of record, J. Fluid Mech. 966, A26 (Cambridge University Press,
Open Access CC-BY 4.0; received 10 September 2022, revised 3 April 2023,
accepted 16 May 2023), 23 pages, all read. Eqs. (2.1)–(2.10), (3.3)–(3.5)
and (4.1) were also checked visually, because the text layer garbles them.
Page 1 matches the metadata; no identity problem. Section, equation, figure
and table numbers on this page are those of this version.

# Key claims

1. Most deep-learning RANS/LES closures are trained a priori, which decouples the objective from the PDE model and "hinders predictive accuracy and even stability in a posteriori predictions": the network is trained on DNS inputs but receives LES or RANS inputs in prediction (§1, §5). **Stated**
2. Adjoint-based methods "utilize the PDEs directly during gradient calculations and therefore they do not suffer this inconsistency challenge"; reinforcement learning depends on the fidelity of the agent to the physical dynamics (§1). **Stated**
3. One network models all unclosed terms $-\partial_j\tau_{ij}+\Gamma_i$, where $\Gamma_i$ collects the boundary terms of filtering at the bluff body and the commutation-error terms of a non-uniform filter (Ghosal 1996). The same network acts near walls and in the far field, as a unified free-stream/wall closure with no discrete wall model (§2, §2.1, Eqs. 2.2–2.3). **Derived** (formulation)
4. Because its inputs are velocity derivatives, the closure is Galilean invariant but not rotationally invariant (§2.1). **Stated**
5. The adjoint system has as many equations as the Navier–Stokes system (three momentum, one continuity), whatever the dimension of $\boldsymbol\theta$, which makes the gradient evaluation efficient (§2.2, after Eq. 2.10). **Derived**
6. Global convergence of adjoint-trained neural-network PDE models, as hidden units and training time go to infinity, is proven only for linear PDE operators (Sirignano, MacArt & Spiliopoulos 2023); the nonlinear case is open (§2.2). **Stated**
7. Training windows are 0.1 time units, "only a fraction of the mean-flow time scale", and nothing guarantees a priori that the resulting PDE is stable as $t\to\infty$; yet the trained models "can yield stable, accurate Navier–Stokes solutions on $t\in[0,\infty)$" (§2.2, §3). **Shown**
8. Training is distributed over "tens to hundreds of GPUs"; each GPU holds $M$ forward and adjoint solutions as a $4\times N_1\times N_2\times N_3\times M$ tensor, with synchronised RMSprop over MPI (§2.3). **Stated** (no timings given)
9. The LES keeps $1/64$ ($\Delta/\Delta_{\mathrm{DNS}}=4$) or $1/512$ ($\Delta/\Delta_{\mathrm{DNS}}=8$) of the DNS points and is run "for several thousand time units before recording statistics" (§3.2). **Shown**
10. Drag coefficients $C_D$ (filtered DNS / no model / dynamic Smagorinsky / AMD / DL-AR1 / DL-AR2): case (i) 2.45/1.88/2.15/2.53/2.43/2.51; (ii) 1.94/1.61/1.65/1.96/1.90/1.95; (iii) 2.09/1.62/1.68/1.89/1.84/1.96; (iv) 1.61/1.53/1.54/1.67/1.54/1.61 (Table 2). **Shown**
11. "Compared with the filtered DNS data, the deep learning models consistently perform as well or better than the dynamic Smagorinsky and AMD models"; AMD is the most accurate non-learned model but is outperformed in every case "by the in-sample or nearest DL model" (§4.1, Table 2). **Shown**
12. Drag coefficients evaluated on DNS and on filtered DNS do not differ significantly (§4.1). **Stated**
13. No-model LES is worse than the learned models in all cases; for case (i) it underpredicts the upper separation region and overpredicts the wake recirculation, and dynamic Smagorinsky and AMD do the opposite (§4.2, Fig. 2). **Shown**
14. For the out-of-sample case (ii), DL-AR1 (trained at $Re=1000$) is visually more accurate than DL-AR2 (trained at $Re=2000$) despite DL-AR2's geometric similarity; for case (iv) DL-AR1 "almost perfectly matches both recirculation regions". The authors suggest that the Reynolds number affects accuracy more than the blockage geometry (§4.2, Figs. 3, 5). **Shown** (interpretation **Stated**)
15. In the boundary-layer regions, no-model and dynamic-Smagorinsky LES give resolved Reynolds stresses $R^{\mathrm{res}}_{ij}$ that are "incorrectly large" where filtered DNS approaches zero; AMD improves this but keeps a larger variance of $R^{\mathrm{res}}_{11}$ and $R^{\mathrm{res}}_{22}$ than the learned LES (§4.2, Figs. 8–9). **Shown**
16. "For all cases and all statistics, the DL-LES results more closely match the filtered-DNS-evaluated statistics than the no-model, dynamic Smagorinsky and AMD LES" (§4.2, Figs. 8–9). **Shown** (see claim 22 and Printed slips)
17. For most cases and stations the LES mesh does not resolve $y^+<10$ and no wall model is used; the learned closures nonetheless "generally slightly outperform the AMD model and dramatically outperform the dynamic Smagorinsky model and implicitly modelled LES" for near-wall mean profiles in wall units (§4.3, Fig. 10). **Shown**
18. Only the in-sample DL-AR1 captures the sign reversal of the cross-stream velocity near $x=0$ for case (i); for case (iii) AMD is not more accurate than dynamic Smagorinsky or no-model LES for the cross-stream velocity (§4.3). **Shown**
19. A network with identical architecture and hyperparameters trained a priori fits the DNS SGS stress "almost perfectly" (Fig. 11), yet the adjoint-trained model "substantially outperforms" it a posteriori for all flow statistics, even in sample (§5, Figs. 11–12). **Shown**
20. On out-of-sample geometries at $Re=1000$, run in the comparison solver: for the equilateral triangular prism AMD is least accurate, DL-AR1 is comparable to no-model and dynamic Smagorinsky LES and DL-AR2 nearly matches the DNS streamlines; for the cylinder both learned models "suppress all artificial primary recirculation", in agreement with DNS, where no-model LES and AMD predict two recirculation regions, and they predict the separation-bubble extent best (§6, Figs. 13–14). **Shown**
21. Running a trained model in the comparison solver (semi-implicit, without the mapped-coordinate discretization) instead of the training solver gives similar primary separation and a less accurate wake, a difference smaller than the gap between the learned and the comparison models; the models are "at least stable, and in some cases accurate" with out-of-sample numerics (§6, Fig. 15). **Shown**
22. The conclusion states that the learned closures and AMD "had similar error for the RMS velocity components" (§7). **Stated**
23. Any multiparametric closure, "traditional one- or two-equation closures" included, could replace the network in the adjoint training, and the method applies in principle to any semi-discretization, unstructured finite volumes and elements included (§2, §7). **Stated**
24. Preliminary tests of the models trained at $Re=1000$ and $2000$ on a wake at $Re=12\,000$ "are stable and, in some cases, accurate"; the results are not shown (§7). **Stated**
25. AMD "is known to outperform the DS model on highly anisotropic meshes (Zahiri & Roohi 2019)" (§3.2). **Stated**

The closure (Eq. 2.3) reads, in registry notation,
$\partial_t\bar u_i=-\partial_i\bar p-\partial_j(\bar u_i\bar u_j)+Re^{-1}\partial_j\partial_j\bar u_i-\partial_jh_{ij}(\nabla\bar{\boldsymbol u};\boldsymbol\theta)$,
$\partial_k\bar u_k=0$. The network (Eq. 2.7) has three $\tanh$ layers of 50
units and two multiplicative gates $G^1$, $G^2$ fed by the input; the
training loss (Eq. 2.8) is
$\mathcal L(\boldsymbol\theta)=\sum_{n=1}^{N}\int_\Omega\lVert\bar{\boldsymbol u}^{\boldsymbol\theta}(t_n+\tau_{\mathrm{tr}})-\bar{\boldsymbol u}^{\mathrm{DNS}}(t_n+\tau_{\mathrm{tr}})\rVert\,d\boldsymbol x$
with $\tau_{\mathrm{tr}}=0.1$. The AMD baseline (Eq. 3.5) is
$\nu_t=C_{\mathrm{AMD}}\max[-(\Delta_k\partial_k\bar u_i)(\Delta_k\partial_k\bar u_j)\bar S_{ij},0]/(\partial_l\bar u_m\partial_l\bar u_m)$
with $C_{\mathrm{AMD}}=0.3$ "for second-order central discretizations".

# Printed slips

1. §4.2 states that "for all cases and all statistics" the learned LES matches filtered DNS more closely than the three baselines; the conclusion (§7) states that the learned closures and AMD "had similar error for the RMS velocity components". The two statements differ in strength.
2. §2 calls $x_2$ "the transverse direction" with slip walls and $x_3$ spanwise; §3.1 prints "The streamwise ($\pm x_2$) boundaries are slip walls" and "The cross-stream ($x_3$) direction is periodic", while $x_1$ is the streamwise direction and §4.3 uses "cross-stream velocity" for $\bar u_2$.
3. §2.2 imposes "$\hat u_2=0$" on the adjoint velocity at the transverse boundaries and then states that "$\hat u_2$ and $\hat u_3$ satisfy Neumann boundary conditions at $x_2=\{-L_2/2,L_2/2\}$": $\hat u_2$ receives both a Dirichlet and a Neumann condition.
4. Eq. (2.4) carries a prefactor $\tfrac12$ in front of a norm that is not squared; Eq. (2.8), the loss used, has neither.
5. Eq. (2.10) integrates the gradient over $\int_0^T$, although the adjoint is solved on the windows $[t_n,t_n+\tau]$ and summed over $n$.
6. §4.1 attributes the better case-(iv) drag of DL-AR2 to "the higher degree of geometric similarity"; §4.2 states for the same case that "One would expect the DL-AR2 model to outperform the DL-AR1 model … though the opposite is observed" (streamlines rather than drag).
7. Typos: Table 2 caption "dynamic Smagorinky"; Fig. 9(d) axis "Fltered DNS"; §4.2 "resolved Reynolds for the no-model" (missing "stress"). The reference title of Kaltenbach & Choi (1995) is printed scrambled ("Large-eddy an airfoil simulation of flow around on a structured mesh").
8. Eq. (3.4) writes the Smagorinsky closure with "$\approx$" and does not define the normalization of $\lvert\bar S\rvert$ (a gap, not a slip).

# Notation map

| Sirignano & MacArt (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_i$, $p$, $Re$ | $u_i$, $p$, $Re$ | dimensionless incompressible, $\rho=1$; $Re_0=\rho u_\infty H_0/\mu$ on the prism height $H_0$ |
| $x_1$, $x_2$, $x_3$ | $x$, $y$, $z$ | streamwise, transverse (cross-stream), spanwise; the near-wall profiles use $x_2$ as wall-normal distance from the prism faces |
| $\bar\phi$, $G$ | $\bar\phi$, $G$ | LES filter; a box filter of width $\Delta$ for the filtered DNS; **collision:** $G^1$, $G^2$ are also the network gates |
| $\tau^{\mathrm{SGS}}_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$ | $\tau_{ij}$ | positive trace, full tensor |
| $\Gamma_i$ | $\Gamma_i$ (page-local) | boundary and commutation-error terms |
| $h(z;\theta)$, $h_{ij}$ | $h_{ij}(\nabla\bar{\boldsymbol u};\boldsymbol\theta)$ (page-local network output) | enters as $-\partial_jh_{ij}$ |
| $z$, $z_{mi}=\partial\bar u_i/\partial x_m$; $u_x=\nabla u$ | $\boldsymbol\zeta$ (input features: the filtered velocity gradient) | **collision:** $z_j=g_j(x_j)$ is also the mapped coordinate |
| $\theta$ | $\boldsymbol\theta$ | weights and biases $W^1\dots W^6$, $b^1\dots b^6$ |
| $J(\theta)$ | $\mathcal L(\boldsymbol\theta)$ | Eqs. 2.4, 2.8 |
| $\tau$ (training interval) | $\tau_{\mathrm{tr}}$ (page-local, as on [model-consistent training](/methods/model-consistent-training.md)) | **collision:** not a stress |
| $\hat u_i$, $\hat p$ | $u^{\mathrm a}_i$, $p^{\mathrm a}$ (page-local adjoint variables) | **collision:** not a test filter |
| $g_j$, $c_j$ | (mesh map and its metric, page-local) | |
| $N$, $M$, $N_1,N_2,N_3$ | (training windows, solutions per GPU, mesh cells) | **collision:** $N$ is not a polynomial degree |
| $\bar\Delta$, $\Delta_{\mathrm{DNS}}$, $\bar\Delta_k$ | $\Delta$, $\Delta_{\mathrm{DNS}}$, $\Delta_k$ (directional spacings, page-local) | implicit filtering: filter width = local LES spacing |
| $\bar S_{ij}$, $\lvert\bar S\rvert$ | $\bar S_{ij}$, $\lvert\bar S\rvert$ | normalization of $\lvert\bar S\rvert$ not printed |
| $C_S$, $C_{\mathrm{AMD}}$ | $C_s$, $C_{\mathrm{AMD}}$ (page-local) | $C_s$ dynamic; $C_{\mathrm{AMD}}=0.3$ |
| $\nu_t$ | $\nu_t$ | SGS eddy viscosity of the baselines |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle$ | spanwise and time average (Eq. 3.1) |
| $\tau^R_{ij}=\langle\bar u_i\bar u_j\rangle-\langle\bar u_i\rangle\langle\bar u_j\rangle$ | $R^{\mathrm{res}}_{ij}$ | positive trace, resolved part |
| $\langle\bar u''_i\rangle$ | (rms of the resolved velocity) | |
| $\ell_{1,\phi}$ | (pointwise absolute error of a mean statistic) | Eq. 4.1 |
| $\tau_w$, $u_\tau$, $\delta_v$, $y^+$, $\bar u_i^+$ | $\tau_w$, $u_\tau$, $\delta_\nu$, $y^+$, $u^+$ | $\tau_w$ averaged over the top and bottom prism faces |
| $c_d$ | $C_D$ | definition not printed |
| $H_0$, $L_0$, AR | (prism height, length, aspect ratio $L_0/H_0$) | |

# Reference list

33 printed references, author–year (JFM) style, all parsed; no DOIs are
printed. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Sirignano,
MacArt & Spiliopoulos (2023), J. Comput. Phys. 481:112016, is a different
work from this source and from the bibliography's arXiv entry
`sirignano-2023-b`; it takes the key `sirignano-2023-c`, so that no
citation points at this source by mistake. Ling, Jones & Templeton (2016a)
and Ling, Kurzawski & Templeton (2016b) are `ling-2016` and `ling-2016-b`.
The citations of Bae & Koumoutsakos (2022), Duraisamy et al. (2019) and Goc
et al. (2021) are the bundle's Sources [bae-2022](/sources/bae-2022.md),
[duraisamy-2019](/sources/duraisamy-2019.md) and
[goc-2021](/sources/goc-2021.md); the title of the last is printed with
"computational fluid mechanics". The scrambled title of Kaltenbach & Choi
(1995) is recorded as printed; Jameson (2003) is a VKI lecture series and
Slotnick et al. (2014) a NASA contractor report.

# Pages created or updated

Chunk 4 (2026-10-26), cited further in chunk 5. This source is cited on:

- [Circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Discretization-consistent closure](/definitions/discretization-consistent-closure.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Anisotropic minimum-dissipation model](/methods/anisotropic-minimum-dissipation-model.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Field inversion and machine learning](/methods/field-inversion-machine-learning.md)
- [Machine-learning wall models](/methods/machine-learning-wall-model.md)
- [Model-consistent (a posteriori) training of learned closures](/methods/model-consistent-training.md)
- [Neural-network subgrid-scale models](/methods/neural-network-sgs-model.md)
- [Reinforcement-learning turbulence closures](/methods/reinforcement-learning-closure.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Tensor-basis neural network and the integrity basis](/methods/tensor-basis-neural-network.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)

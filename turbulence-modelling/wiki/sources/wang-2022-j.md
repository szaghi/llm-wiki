---
type: Source
title: "Wang et al. (2022) — Constant-coefficient spatial gradient models for the sub-grid scale closure in large-eddy simulation of turbulence"
description: "Derives a constant-coefficient spatial gradient model (SGM-7-19) that writes the second-order gradient model with first-order filtered velocity gradients on a seven-point stencil, explaining the coefficients an earlier neural network learned; tested a priori and a posteriori in forced isotropic turbulence and a temporal mixing layer."
resource: "doi:10.1063/5.0101356"
source_kind: paper
authors: [Wang Y., Yuan Z., Wang X., Wang J.]
year: 2022
venue: "Phys. Fluids 34:095108"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Physics_of_Fluids_Wang_Constant-coefficient_spatial_gradient_models_for_the_sub-gri.pdf"
tags: [les, sgs-model, gradient-model, structural-model, a-priori-a-posteriori, mixing-layer]
timestamp: 2026-10-28T07:09:00Z
---

# Summary

Wang et al. (2022) propose a constant-coefficient spatial gradient model
(SGM) for the subgrid-scale stress of
[large-eddy simulation](/definitions/large-eddy-simulation.md). The
authors' earlier ANN-based spatial gradient model writes $\tau_{ij}$ as a
quadratic form in the first-order filtered velocity gradients at the seven
points of a stencil (the local point and its six axial neighbours), with
49 coefficients supplied by a [neural network](/methods/neural-network-sgs-model.md);
only 19 of them mattered, and they were nearly constant and symmetric. The
paper explains the pattern: the multi-point first-order-gradient model is a
discretization of the local higher-order
[gradient model](/methods/gradient-model.md), here truncated at second
order, $\tau_{ij}=\tfrac{\Delta^2}{12}\partial_k\bar u_i\partial_k\bar u_j+\tfrac{\Delta^4}{288}\partial_k\partial_l\bar u_i\partial_k\partial_l\bar u_j$.
A Taylor expansion of the neighbour gradients, or a discretization of the
second-order gradients that splits each product into upwind and downwind
halves, gives the same constants: $1/8$ local–local, $-1/144$
local–neighbour, $+1/144$ neighbour–same-neighbour, the SGM-7-19 model.

[A priori](/definitions/a-priori-and-a-posteriori-testing.md), on forced
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md) at
$Re_\lambda\approx250$, SGM-7-19 correlates with the filtered-DNS stress at
0.973, against 0.945 for the Clark model and 0.985 for the network. A
posteriori it is compared with the
[dynamic Smagorinsky](/methods/dynamic-procedure.md) and
[dynamic mixed](/methods/scale-similarity-model.md) models and with
[implicit LES](/definitions/implicit-les.md) (a tuned hyperviscosity) in
isotropic turbulence and a weakly compressible
[temporal mixing layer](/benchmarks/temporal-mixing-layer.md) seeded by a
[digital filter](/methods/inflow-turbulence-generation.md); SGM-7-19 comes
closest to filtered DNS in spectra, strain-rate and velocity-increment PDFs,
momentum thickness, kinetic energy and Reynolds shear stress, with
[backscatter](/definitions/energy-backscatter.md) clipped for stability,
while the [Smagorinsky](/methods/smagorinsky-model.md)-based models are too
dissipative. Its cost is 1.5–1.7 times that of the dynamic Smagorinsky
model. The mixing-layer LES also agrees better with filtered DNS when the
initial perturbation length exceeds the LES filter width.

# Version read

Version of record (AIP; submitted 31 May 2022, accepted 10 August 2022,
published online 8 September 2022), 23 PDF pages (an AIP cover page and
article pages 095108-1 to 095108-22), all read; equations, Tables I–II and
Appendix A read visually because text extraction lost minus signs and
indices. Page 1 matches the metadata. No identity problem: the paper is
the constant-coefficient follow-up of the authors' dynamic spatial
gradient model (ref. 42, Phys. Fluids 33:075119) and ANN spatial gradient
model (ref. 60, AIP Adv. 11:055216), not either of them. Numbering on this
page is that of this version.

# Key claims

Page-local symbols: $S=0,\dots,6$ the stencil location (0 local; 1–6 the
neighbours along $x-$, $x+$, $y-$, $y+$, $z-$, $z+$ in the isotropic case);
$g^{L_1,L_2}$ the dimensionless coefficient of the product of the gradient
of $\bar u_i$ at $S=L_1$ and of $\bar u_j$ at $S=L_2$ (not the registry's
integrity-basis coefficients $g^{(n)}$), $g^{P,P}$, $g^{P,N}$, $g^{N,P}$,
$g^{N,N}$, $g^{N,-N}$ its local–local, local–neighbour, neighbour–local,
same-neighbour and opposite-neighbour values, $c_1,\dots,c_4$ the
coefficients of the four-coefficient model (Eq. 17); $h_{\mathrm{DNS}}$,
$h_{\mathrm{LES}}$ the grid spacings, $\Delta/h_{\mathrm{LES}}=2$
throughout; $\Delta_d$ the digital-filter width of the initial
perturbations; $C(\cdot)$, $E_r(\cdot)$ the a priori correlation
coefficient and relative error (Eqs. 9–10).

1. In the ANN spatial gradient model (ref. 60) only 19 of the 49 terms of the seven-point model are dominant; the dominant coefficients are narrowly distributed, $g^{P,P}$ is one order larger than $g^{P,N}$, $g^{N,P}$, $g^{N,N}$, and $g^{N,P}=g^{P,N}=-g^{N,N}$ (§II C, Table I). **Stated** (from ref. 60)
2. The multi-point spatial gradient model built from first-order gradients is equivalent to a local higher-order gradient model "with accuracy up to any orders" (§I, §III). **Derived** (to second order, Appendix A)
3. Using only first-order velocity gradients "automatically guarantees the Galilean invariance" while keeping an accuracy similar to that of approximate deconvolution and DIAD with fewer terms (§II C). **Stated**
4. Expanding the neighbour gradients by Taylor series in the four-coefficient model and matching the second-order gradient model gives $c_4=1/144$ and $c_1+6(c_2+c_3+c_4)=1/12$, an under-determined two-parameter model (§III, App. A, Eqs. 18, A4). **Derived**
5. Imposing $c_2=c_3$ gives a one-parameter model (Eq. 19); imposing further $g^{N,P}=-g^{N,N}$ ($c_2=-c_4$) gives $g^{P,P}=1/8$, $g^{P,N}=g^{N,P}=-1/144$, $g^{N,N}=+1/144$, the SGM-7-19 model (Eq. 20, A6). **Derived**
6. Central differences of the second-order gradients give a model without local–neighbour products ($g^{P,P}=1/12$, $g^{P,N}=0$, $g^{N,N}=1/288$, $g^{N,-N}=-1/288$); splitting each product of second-order gradients into an upwind and a downwind half reproduces the ANN pattern and the SGM-7-19 coefficients (§III, Eqs. 21–23, Table II). **Derived**
7. SGM-7-19 is "not a case-by-case result inspired by a particular outcome of ANN, but a result with solid theoretical basis"; the network "identifies the most accurate way to approximate Eq. (15) using the form of Eq. (14)" (§III). **Stated**
8. A priori, at $\Delta=16h_{\mathrm{DNS}}$, $C(\tau_{11},\tau_{12})$ and $E_r(\tau_{11},\tau_{12})$: Clark gradient model $(0.945,0.946)$/$(0.368,0.333)$; ANNSGM-7-19 $(0.985,0.981)$/$(0.135,0.197)$; upwind–downwind (SGM-7-19) $(0.973,0.973)$/$(0.241,0.237)$; central differences $(0.968,0.969)$/$(0.288,0.264)$ (Table II). **Shown**
9. The upwind–downwind form beats central differences because it uses all seven stencil points, central differences only the six neighbours; the remaining gap to the network is attributed to higher-order gradients it captures implicitly (§III). **Stated**
10. Forced isotropic turbulence a posteriori ($128^3$, $\Delta=16h_{\mathrm{DNS}}$): the dynamic Smagorinsky and dynamic mixed models overestimate the spectrum at low and underestimate it at high wavenumbers, through the strong dissipation of their Smagorinsky parts; SGM-7-19 is overall closest to filtered DNS (Fig. 2). **Shown**
11. Implicit LES needs an artificially adjusted hyperviscosity to keep its spectrum near DNS; "Otherwise, the ILES always diverges in the simulation" (§IV). **Stated**
12. Strain-rate PDFs: SGM-7-19 "almost merges" with filtered DNS; implicit LES PDFs are wider, the dynamic models slightly narrower; for $\lvert\bar S\rvert$, implicit LES puts the peak near the filtered-DNS rms while filtered DNS has it below; the dynamic models get the location but overestimate the peak; SGM-7-19 predicts both (Figs. 3–4). **Shown**
13. Velocity-increment PDFs: all models agree at large separations; at $r/\Delta=1$ SGM-7-19 is best; the dynamic models give larger vortical structures, SGM-7-19 more small-scale structure (Figs. 5–6). **Shown**
14. Mixing-layer DNS: the self-similar linear growth of the momentum thickness is "clearly longer and more concrete" for $\Delta_d=8h_{\mathrm{DNS}}$ and $16h_{\mathrm{DNS}}$ than for 32 and 64, which are not used as benchmarks (Fig. 8). **Shown**
15. Mixing-layer momentum thickness: the dynamic Smagorinsky model captures the transitional region but deviates in the linear-growth region, the dynamic mixed model does worse, SGM-7-19 best; implicit LES also agrees well in momentum thickness (Fig. 9). **Shown**
16. All LES agree better with filtered DNS for $\Delta_d=16h_{\mathrm{DNS}}$ than for $8h_{\mathrm{DNS}}$ (LES filter $\Delta=8h_{\mathrm{DNS}}$): the initial perturbation lengths must exceed the filter width so that filtering the initial condition does not affect them (§V, Figs. 9–13, Conclusions). **Shown**
17. Implicit LES does not recover the filtered spectra of the mixing layer despite its good momentum thickness; all explicit models do better, SGM-7-19 closest (Figs. 10–11). **Shown**
18. Mid-plane kinetic energy: implicit LES over-predicts it, SGM-7-19 and the dynamic mixed model predict it best; streamwise kinetic energy over the domain: SGM-7-19 follows filtered DNS most closely (Figs. 12–13). **Shown**
19. Spanwise velocity-increment PDFs in the mixing layer ($r/\Delta=1,2,4,8$): SGM-7-19 agrees with filtered DNS, especially at large separations, unlike isotropic turbulence where the models coincide there (Fig. 14). **Shown**
20. Reynolds shear stress profile: SGM-7-19 recovers it, the dynamic models overestimate it (the mixed model slightly less); $Q$ iso-surfaces at $t=30$: the dynamic models give larger structures than filtered DNS, SGM-7-19 closer, notably in small vortices (Figs. 15–16). **Shown**
21. Subgrid modelling time per step on Xeon Gold 6148 (64 cores isotropic, 32 cores mixing layer): dynamic Smagorinsky 0.272 and 0.245 s, dynamic mixed 0.567 and 0.575 s, SGM-7-19 0.399 and 0.425 s, i.e. 1, 2.1, 1.5 and 1, 2.3, 1.7 relative to the dynamic Smagorinsky model; the mixed model is costlier because of repeated double filtering (Table V, §VI). **Shown**
22. Appendix B (mixing layer seeded with the most unstable and subharmonic linear-stability modes, DNS $256^3$, LES $64^3$): SGM-7-19 best for momentum thickness; the dynamic Smagorinsky model under-predicts and the mixed model over-predicts the growth; the former over-dissipates the vortex rollers and the latter induces strip-shaped noise (Figs. 17–20). **Shown**
23. Because the coefficients follow from a Taylor expansion, the performance "should be equally expected in other flow configurations as long as the grids are uniform"; non-uniform grids of wall-bounded flows need re-derived coefficients and the commutation error between filtering and differentiation (Conclusions). **Stated**

The model (Eq. 20), in registry notation:

$$\begin{aligned}\tau_{ij}={}&\tfrac18\Delta^2\,\partial_k\bar u_i\big|_{0}\,\partial_k\bar u_j\big|_{0}+\tfrac1{144}\Delta^2\sum_{L=1}^6\partial_k\bar u_i\big|_{L}\,\partial_k\bar u_j\big|_{L}\\&-\tfrac1{144}\Delta^2\sum_{L=1}^6\Big(\partial_k\bar u_i\big|_{0}\,\partial_k\bar u_j\big|_{L}+\partial_k\bar u_i\big|_{L}\,\partial_k\bar u_j\big|_{0}\Big),\end{aligned}$$

summed over $k$, with $|_L$ the value at stencil point $S=L$; it holds on
uniform grids with $h_{\mathrm{LES}}=\Delta/2$ and a Gaussian filter. It
targets the second-order truncation of the higher-order gradient model
(Eq. 15), $\tau_{ij}=\sum_{n\ge1}\frac{(2\alpha_{\mathrm G})^n}{n!}\partial^n\bar u_i\cdot\partial^n\bar u_j$
with $\alpha_{\mathrm G}=\Delta^2/24$ (the source's $\alpha$; registry §11, as on
the gradient-model page).

# Printed slips

- **Table I against Table II:** Table I prints the ANNSGM-7-19 local–neighbour and same-neighbour coefficients as $-1.6\times10^{-2}$ and $+1.6\times10^{-2}$ (with $g^{P,P}=+1.8\times10^{-1}$), while Table II prints the ANNSGM-7-19 values $g^{P,N}(g^{N,P})=-0.0016$ and $g^{N,N}=+0.0016$. The text's "one order larger" for $g^{P,P}$ agrees with Table I.
- $g^{N,-N}$ appears in Table II and §III, defined only after the table ("$-N$ represents the opposite locations").
- Typos: "the forced impressible HIT" (§IV), "LES of the force HIT" (Table V caption), "it is trivial show" (§III).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar u_i$, $\Delta$ | $\bar u_i$, $\Delta$ | Gaussian filter (Eq. 8) |
| $\tilde{(\cdot)}$, $\tilde\Delta=2\Delta$ (§II B) | $\hat{(\cdot)}$, $\hat\Delta$ | **collision:** test filter of the dynamic models |
| $\tilde{(\cdot)}=\overline{\rho(\cdot)}/\bar\rho$ (§V) | $\tilde{(\cdot)}$ | Favre filter in the mixing-layer equations |
| $\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$ | $\tau_{ij}$ | positive trace; Favre form $\widetilde{u_iu_j}-\tilde u_i\tilde u_j$ in §V |
| $\tau^A_{ij}$ | $\tau^d_{ij}$ | deviatoric part |
| $\tau^R_{ij}$, $\tau^{model}_{ij}$ | $\tau_{ij}$ (model) | higher-order gradient and spatial gradient model stresses |
| $\bar S_{ij}$, $\lvert\bar S\rvert$ | $\bar S_{ij}$, $\lvert\bar S\rvert$ | factor two included |
| $\mathcal L_{ij}$, $\mathcal M_{ij}$, $\alpha_{ij}$, $\beta_{ij}$ | $L_{ij}$, $M_{ij}$ (page-local), … | dynamic procedure, test filter written tilde |
| $C_1$, $C_2$, $h_{1,ij}$, $h_{2,ij}$ | (dynamic mixed model coefficients and tensors, page-local) | |
| $\alpha=\Delta^2/24$ (Eq. 15) | $\alpha_{\mathrm G}$ (registry §11) | **collision:** $\alpha=PrRe(\gamma-1)M^2$ in §V |
| $g^{L_1,L_2}$, $g^{P,P}$, … | $g^{L_1L_2}$ (registry §11), the class values $g^{P,P}$, … page-local | not the integrity-basis $g^{(n)}$ |
| $u^{rms}=\sqrt{\langle u_iu_i\rangle}$ | (three-component rms, page-local) | $Re_\lambda=u^{rms}\lambda/(\sqrt3\nu)$ |
| $L_I$, $\tau=L_I/u^{rms}$ | $L$, $T_E$ | **collision:** $\tau$ is a time |
| $\eta$, $\lambda$, $Re_\lambda$, $\varepsilon$ | $\eta$, $\lambda$, $Re_\lambda$, $\varepsilon$ | |
| $x_1$, $x_2$, $x_3$ (mixing layer) | $z$, $y$, $x$ | spanwise, normal, streamwise |
| $\theta$, $\theta_0$ | $\theta$, $\theta_0$ | momentum thickness |
| $Re_\omega$ | (Reynolds number on half the initial vorticity thickness, page-local) | App. B |
| $Q$ | $Q$-criterion | |
| fDNS | filtered DNS | |

# Reference list

88 printed references, numbered (AIP) style. The list is merged complete
into the [bibliography](/bibliography.md) with `citedby` this slug. Ref. 9
is the ingested [duraisamy-2019](/sources/duraisamy-2019.md). The
authors' own works are mapped to existing entries: ref. 42 (Phys. Fluids
33:075119) is `wang-2021-g`, ref. 60 (AIP Adv. 11:055216) is
`wang-2021-f`, ref. 47 (Phys. Fluids 30:125101) is `wang-2018-e`, ref. 67
(J. Comput. Phys. 229:5257) is `wang-2010`; the existing `wang-2021-b` is
a different work. Ref. 46 prints the third author as "E. Weinan"; ref. 20
(Bardina et al. 1980) prints the AIAA paper number as pages "80–1357". No
item is unparseable.

# Pages created or updated

Chunk 11 (2026-10-27), cited further in chunk 16. This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Temporally developing mixing layer](/benchmarks/temporal-mixing-layer.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Gradient (Clark) model and the clipping of structural SGS models](/methods/gradient-model.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [Neural-network subgrid-scale models](/methods/neural-network-sgs-model.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Symbolic-regression turbulence closures](/methods/symbolic-regression-closure.md)

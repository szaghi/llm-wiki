---
type: Source
title: "McConkey et al. (2022) — Deep structured neural networks for turbulence closure modeling"
description: "Proposes a non-negative optimal eddy viscosity and a linear/non-linear split of the Reynolds-stress anisotropy, learned by two neural networks and injected into a v2-f-type RANS model; shows the split improves the conditioning of the injection by an order of magnitude on the periodic hill."
resource: "doi:10.1063/5.0083074"
source_kind: paper
authors: [McConkey R., Yee E., Lien F.S.]
year: 2022
venue: "Phys. Fluids 34:035110"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Physics_of_Fluids_McConkey_Deep_structured_neural_networks_for_turbulence_closure_model.pdf"
tags: [rans, data-driven, neural-network, eddy-viscosity, separated-flow, a-priori-a-posteriori]
timestamp: 2026-10-25T20:38:00Z
---

# Summary

McConkey et al. (2022) address the ill-conditioning of RANS equations closed
by an injected, learned Reynolds stress. They start from the optimal eddy
viscosity of Wu et al. (2018), the least-squares fit of the
[Boussinesq closure](/definitions/boussinesq-hypothesis.md)
$a_{ij}\approx-2\nu_t\langle S_{ij}\rangle$ to the anisotropy
$a_{ij}=R_{ij}-\tfrac23k\delta_{ij}$, which can be negative. They propose a
non-negative optimal eddy viscosity $\nu_t^\dagger$ (a non-negative
least-squares fit) and the split $a_{ij}=-2\nu_t^\dagger\langle S_{ij}\rangle+a^\perp_{ij}$.
The linear part enters the momentum equation implicitly as an effective
viscosity, $\partial_ja^\perp_{ij}$ explicitly as a source, in an open-loop
"one-time correction" of a converged base solution.

On the [periodic hill](/benchmarks/periodic-hill.md) ($Re_h=5600$, steepness
$\alpha=1.2$), injecting DNS-derived quantities gives a velocity error about
ten times smaller with the split than with the fully explicit injection of
$a_{ij}$; even the optimal linear fit leaves errors of the order of 100% in
the anisotropy. The base model is the OpenFOAM $k$-$\varepsilon$-$\varphi$-$f$
form of the $\overline{v^2}$-$f$ elliptic-relaxation model.

Two fully connected networks (14 hidden layers of 30 SELU neurons) learn
$\nu_t^\dagger$ (exponential output, hence non-negative) and the three
independent components of $a^\perp_{ij}$ from 33 Galilean-invariant features:
three heuristic scalars, $\varphi$, and 29 non-vanishing invariants of a
47-tensor minimal integrity basis built from $\langle S_{ij}\rangle$,
$\langle\Omega_{ij}\rangle$, $\nabla k$ and $\nabla\langle v'^2\rangle$ (see
[tensor-basis neural network](/methods/tensor-basis-neural-network.md) for
the integrity-basis idea). Trained on four hills of the McConkey et al.
(2021) dataset and tested on the fifth, the corrected solution reduces the
reattachment error from 20% to 8.9%, and the converged velocity error is
smaller than the closure-term error. The paper reports
[a priori and a posteriori](/definitions/a-priori-and-a-posteriori-testing.md)
errors separately. Its training is a priori on DNS labels, the counterpoint of
[model-consistent training](/methods/model-consistent-training.md) and of
[field inversion](/methods/field-inversion-machine-learning.md).

# Version read

arXiv preprint arXiv:2201.01710v1 [physics.flu-dyn], 5 January 2022 (header
"Dated: 6 January 2022"), 18 pages, not the AIP version of record. Title on
page 1: "Deep Structured Neural Networks for Turbulence Closure Modelling"
(spelling differs from the published title only). Authors match Crossref.
The version read prints no DOI. Section, equation, figure and table numbers
on this page are those of the preprint.

# Key claims

Page-local symbols: $a_{ij}=R_{ij}-\tfrac23k\delta_{ij}=2kb_{ij}$ (dimensional
anisotropy), $\nu_t^*$ and $\nu_t^\dagger$ (unconstrained and non-negative
optimal eddy viscosity), $a^\perp_{ij}$ (non-linear part), $\varphi=\langle v'^2\rangle/k$,
subscript $_{\mathrm{DNS}}$ for DNS-derived quantities. $\langle S_{ij}\rangle$
is the mean strain rate.

1. The unconstrained optimal eddy viscosity $\nu_t^*=-\tfrac12a_{ij}\langle S_{ij}\rangle/(\langle S_{kl}\rangle\langle S_{kl}\rangle)$ (Eq. 6, closed form of the least-squares problem Eq. 5) can be negative, "especially when the eigenframes of $a$ and $S$ are poorly aligned"; treated implicitly it can give a negative effective viscosity and destabilize the solution (§II A). **Stated**
2. The non-negative least-squares fit $\nu_t^\dagger=\arg\min_{\nu_t\ge0}\|a_{ij}+2\nu_t\langle S_{ij}\rangle\|$ (Eq. 7) "guarantees that the injected eddy viscosity will not destabilize the iterative solution, at least in terms of reducing the diagonal dominance of the (assembled) coefficient matrix" (§II A). **Stated** (argument, no analysis)
3. "The present work is the first to propose a stability constraint on the optimal eddy viscosity and to implement this constraint into a neural network" (§I). **Stated**
4. The approximation $R_{ij}\approx-2\nu_t\langle S_{ij}\rangle$ (Eq. 4) of Liu et al. and Brener et al. is deficient because $R_{ii}=2k$ while $\langle S_{ii}\rangle=0$; the optimal eddy viscosity must be formulated on $a_{ij}$ (Eq. 3) (§II). **Derived**
5. Even with an eddy viscosity optimized on DNS data ($\nu^*_{t,\mathrm{DNS}}$ or $\nu^\dagger_{t,\mathrm{DNS}}$), errors "on the order of 100%" occur in all components of $a_{ij}$ for the $\alpha=1.2$ hill, the principal components are severely underpredicted, and the optimal fit gives no substantial gain over the base RANS anisotropy (Fig. 1; legend RMSEs, labelled "m²/s²": $a_{xx}$ 7.94, 7.69, 7.78; $a_{xy}$ 2.48, 3.52, 4.10; $a_{yy}$ 6.94, 6.72, 7.05 for $\nu^*_{t,\mathrm{DNS}}$, $\nu^\dagger_{t,\mathrm{DNS}}$, base RANS) (§II B). **Shown**
6. The linear approximation fails for all components of $a_{ij}$ in the separation, with noticeable $a_{yy}$ errors at reattachment and the largest $a_{xy}$ errors in the acceleration over the right hill (Figs. 2–3; local $R^2$ and Thompson et al.'s fit factor, Eq. 8) (§II B). **Shown**
7. Injecting only $\nu^\dagger_{t,\mathrm{DNS}}$ (no non-linear term) gives RMSE$_U=1.672\times10^{-3}$ m/s and RMSE$_V=2.978\times10^{-4}$ m/s, with large errors at separation and reattachment: the "upper limit" of a linear closure based on $\nu_t^\dagger$ (Fig. 4, §II B). **Shown**
8. Conditioning: $a_{ij,\mathrm{DNS}}$ injected fully explicitly gives RMSE$_U=2.613\times10^{-3}$ m/s and RMSE$_V=6.408\times10^{-4}$ m/s; $\nu^\dagger_{t,\mathrm{DNS}}$ implicit plus $a^\perp_{ij,\mathrm{DNS}}$ explicit gives $2.265\times10^{-4}$ and $6.444\times10^{-5}$ m/s, "an order of magnitude" smaller. Part of the difference may come from the first-order schemes needed to stabilize the explicit injection (Figs. 5–6, §II C). **Shown**
9. Data-driven closure frameworks should be judged by the conditioning error left after a perfect closure prediction, and a conditioning analysis should accompany every new decomposition or injection framework (§II C, §IV B). **Stated**
10. Open-loop ("one-time correction", Ho & West) frameworks are limited to steady flows; iterative frameworks (Liu et al.) can converge to solutions that depend on the initial field (§II D). **Stated** (cited)
11. An exponential output activation $f(x)=e^x$ guarantees a non-negative predicted eddy viscosity, possible because $\nu_t^\dagger$ is a non-negative label (§III B). **Derived**
12. Both networks have 14 hidden layers of 30 neurons, SELU activations, LeCun initialization and no batch normalization; 13,141 (eddy-viscosity network) and 13,203 (anisotropy network) trainable parameters (§III B). **Stated**. With 33 inputs, $33\cdot30+30+13(30\cdot30+30)+31=13{,}141$, and two more outputs add $2\cdot31=62$ *(compiler check, not in the sources)*.
13. Integrity-basis terms involving the mean pressure gradient (Wu et al.) are numerically unstable "in our experience"; replacing it by $\nabla\langle v'^2\rangle$ gives much more stable terms (§III C). **Stated**
14. For two-dimensional incompressible mean flow many of the 47 basis-tensor invariants vanish identically, directly or by continuity; all third invariants vanish because each base tensor has zero determinant; 29 first and second invariants remain — "an outcome not previously discussed in detail" (§III C, App. A, Table II). **Derived** (symbolic evaluation)
15. Adding the second invariant "effectively doubles" the number of invariant features for a three-dimensional flow (47 → 94) (§III C, §V). **Stated**
16. All 33 inputs are Galilean invariant, and the set "represents one of the richest feature sets used in a data-driven turbulence closure model" (§III C). **Stated**
17. Validation should use cases distinct from training; 4-fold cross-validation over the training geometries $\alpha=0.5,0.8,1.0,1.5$, selecting the fold with the smallest gap between training and validation error (§III E). **Stated**
18. A priori on $\alpha=1.2$: MSE of $\nu_t^\dagger$ $1.89\times10^{-7}$ m$^4$s$^{-2}$; MSEs of $a^\perp_{xx}$, $a^\perp_{xy}$, $a^\perp_{yy}$ $2.31\times10^{-12}$, $9.40\times10^{-13}$, $9.56\times10^{-13}$ m$^4$s$^{-4}$ (§IV A, Figs. 11–14). **Shown**
19. $\nu_t^\dagger$ is harder to predict than $a^\perp_{ij}$, which the authors read as the RANS fields carrying more information about $a^\perp_{ij}$; the diagonal components are better predicted than the shear component (§IV A). **Shown**
20. A posteriori, the injected predictions reproduce the separated-region size, the top and bottom boundary layers, reattachment and the acceleration over the right hill; the base model under-predicts the $V$ bulge in the separated region (over-predicting separation) and $V$ over the right hill (Figs. 15–18, §IV B). **Shown**
21. The corrected solution slightly under-predicts $U$ along the top wall, the base model over-predicts it; both $U$ error histograms are skewed towards over-prediction (Figs. 16, 18). **Shown**
22. Reattachment $x_R/h$: 4.50 (DNS), 5.42 (base), 4.10 (corrected) (Fig. 21 legend); relative errors 20% and 8.9% (§IV B). **Shown**. $(5.42-4.50)/4.50=20.4\%$ and $(4.50-4.10)/4.50=8.9\%$ *(compiler check, not in the sources)*.
23. The relative error of the converged $U$ is smaller than that of the closure term (Fig. 20): "under certain conditions, the RANS equations can suppress rather than amplify errors in the closure prediction" (§IV B, §V). **Shown**
24. SHAP (eddy-viscosity network, global): $\varphi$ is the most important feature; the heuristic scalars rank high; the first invariant of $B_7$ ranks third and its second invariant twenty-fifth, while for $B_5$ the second invariant ranks much higher than the first (Fig. 22, §IV C). **Shown**
25. SHAP (local): the heuristic $q_3$ dominates in the separated region; $\varphi$ dominates at the top wall and matters near walls; $q_1$, designed to detect near-wall regions, does not strongly influence the near-wall prediction (Fig. 23, §IV C). **Shown**
26. Machine-learning augmentation can improve "even a sophisticated RANS model" (three transport equations plus an elliptic relaxation equation), and more sophisticated models "may benefit even more" from their richer mean fields (§V). **Stated** (one test case)
27. Direct prediction of the components of $a^\perp_{ij}$ is not coordinate invariant; a tensor-basis network for $a^\perp_{ij}$ is proposed as future work (§V). **Stated**

**Base model (Source page only).** The $k$-$\varepsilon$-$\varphi$-$f$ model as
implemented in OpenFOAM v2006 (Eqs. 10–16): $\nu_t=C_\mu\varphi kT$, transport
equations for $k$, $\varepsilon$ and $\varphi$, an elliptic relaxation
equation for $f$, $T=\max(k/\varepsilon,C_T\sqrt{\nu/\varepsilon})$,
$L=C_L\max(k^{3/2}/\varepsilon,C_\eta(\nu^3/\varepsilon)^{1/4})$, with
$C_\mu=0.22$, $C_{\varepsilon1}=1.4(1+0.05\sqrt{1/\varphi})$,
$C_{\varepsilon2}=1.9$, $C_T=6.0$, $C_L=0.25$, $C_{f1}=1.4$, $C_{f2}=0.3$,
$C_\eta=110$, $\sigma_k=1.0$, $\sigma_\varepsilon=1.3$. It reformulates the
Lien–Kalitzin variant of Durbin's $\overline{v^2}$-$f$ model in
$\varphi=\langle v'^2\rangle/k$ (Laurence, Uribe & Utyuzhnikov 2005).
Numerics: PIMPLE, second-order upwind convection for the mean flow,
first-order convection for the turbulence equations, $y^+\le1$.

# Printed slips

- **Eq. (14).** Second derivatives printed with a single denominator, "$L^2\frac{\partial^2f}{\partial x_j}$" and "$\nu\frac{\partial^2\phi}{\partial x_j}$", where a Laplacian ($\partial x_j\partial x_j$) is meant.
- **Table II (App. A).** Identical expressions for different basis tensors with different zero/non-zero marks: $B_{15}$ and $B_{16}$ both "$A_{v2}A_k$"; $B_{18}$ and $B_{26}$ both "$RA_{v2}S$"; $B_{19}$ and $B_{27}$ both "$RA_{v2}S^2$".
- **Table II against Table I and the text.** Table II marks 21 tensors with a non-zero first invariant (including $B_{44}$), giving $21+9=30$; Table I uses 20 first invariants ($B_{44}$ absent) and the text says 29 remained. The omission of $I_1(B_{44})$ is not explained.
- **Attribution of the base model.** The introduction attributes the $k$-$\varepsilon$-$\phi_t$-$f$ model to ref. 31 (Hanjalić, Popovac & Hadžiabdić 2004); §II E and §III A attribute it to ref. 38 (Laurence, Uribe & Utyuzhnikov 2005).
- **§IV C.** The text lists the Fig. 23 locations (b)–(f), but the figure has six locations, (b)–(g); (g) is mentioned only afterwards.
- **Typos.** Fig. 4 caption "A poteriori"; §III C "a scalar input feature was extract"; §II A "an non-negativity".
- **Ref. 47.** "AIAA Paper 2005–522 (2016)": the paper number carries the year 2005, the entry the year 2016.

# Notation map

| McConkey et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\vec U=(U,V,W)$, overbar | $\langle u_i\rangle$, $\langle\cdot\rangle$ | **collision:** the source's overbar is the Reynolds average, not the LES filter |
| $\vec u'$ | $u_i'$ | |
| $p$, $p'=p+\tfrac23k$ | $p$ (kinematic), (modified pressure) | $p'$ is not a fluctuation |
| $\tau\equiv\overline{\vec u'\vec u'}$ | $R_{ij}$ | positive trace, kinematic; **collision:** not an SGS stress |
| $a\equiv\tau-\tfrac13\mathrm{tr}(\tau)I$ | $a_{ij}=R_{ij}-\tfrac23k\delta_{ij}=2kb_{ij}$ (page-local) | dimensional anisotropy |
| $S$ | $\langle S_{ij}\rangle$ | mean strain rate |
| $R$ | $\langle\Omega_{ij}\rangle$ | **collision:** $R$ is the rotation-rate tensor, not the Reynolds stress |
| $\lVert S\rVert$, $\lVert\tau\rVert$ | $\lvert S\rvert/\sqrt2$, Frobenius norm | no factor two |
| $A:B$ | $A_{ij}B_{ij}$ | |
| $\nu_t^*$, $\nu_t^\dagger$ | $\nu_t^*$, $\nu_t^\dagger$ (page-local) | Eqs. 6, 7 |
| $a^\perp$ | $a^\perp_{ij}$ (page-local) | Eq. 9 |
| tilde ($\tilde\nu_t^\dagger$, $\tilde a$) | (network prediction) | **collision:** neither a Favre filter nor the SA variable |
| subscript $\theta$, $\psi$ | subscript $_{\mathrm{DNS}}$, (base RANS) | **collision** with the registry's momentum thickness $\theta$ and parameters $\boldsymbol\theta$ |
| $P$ | $P_k$ | |
| $v^2$ (printed), $\phi=v^2/k$ ($\phi_t$) | $\langle v'^2\rangle$, $\varphi$ (page-local) | wall-normal stress of the $\overline{v^2}$-$f$ family |
| $f$ | (elliptic-relaxation variable) | also the activation $f(x)=e^x$ |
| $T$, $L$ | (turbulent time and length scales) | **collision:** $L$ is also the number of hidden layers and the registry's integral length |
| $y_\perp$ | $d$ | wall distance |
| $q_1,q_2,q_3$ | (heuristic input scalars, Eq. 17) | |
| $A_k$, $A_{v2}$ | (antisymmetric tensors of $\nabla k$, $\nabla\langle v'^2\rangle$) | |
| $B_1,\dots,B_{47}$ | (minimal integrity basis of four tensors) | not Pope's $T^{(n)}$ |
| $I_1$, $I_2$ | (first, second invariants) | |
| $R^2$, $R_i$ | (coefficient of determination; Thompson et al. fit factor) | |
| $\alpha$ | (hill steepness factor) | **collision** with the DG/FV blending factor $\alpha$ |
| $H$, $Re_H$ | $h$, $Re_h$ | hill height; $Re_h=5600$ |
| $x_r$ | $x_R$ | reattachment point |
| $\lambda$ | (L2 regularization weight, $10^{-5}$) | **collision** with the Taylor microscale |
| input features, labels | $\boldsymbol\zeta$, (training targets) | |

# Reference list

47 printed references, numbered (AIP style) with titles. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Refs. 3 and 8 print the same Duraisamy title as an arXiv preprint (2020) and
as Phys. Rev. Fluids 6 (2021); the preprint is kept as its own entry,
`duraisamy-2020`, and
ref. 8 and ref. 4 are the ingested sources
[duraisamy-2021](/sources/duraisamy-2021.md) and
[duraisamy-2019](/sources/duraisamy-2019.md). Refs. 10, 11 and 21 print no
venue; ref. 9 prints "arXiv" without an identifier; ref. 22 (Kaandorp 2018,
Delft) prints no document type; ref. 37 (Ho & West 2021) prints only a DOI;
ref. 43 (Keras) prints a raw `\url{}`. Two Zhang 2019 works are
disambiguated in printed order. No printed duplicates.

# Pages created or updated

Chunk 3 (2026-10-25). This source is cited on:

- [Periodic hill](/benchmarks/periodic-hill.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Model-form uncertainty in turbulence closures](/definitions/model-form-uncertainty.md)
- [Field inversion and machine learning](/methods/field-inversion-machine-learning.md)
- [Model-consistent (a posteriori) training of learned closures](/methods/model-consistent-training.md)
- [Tensor-basis neural network and the integrity basis](/methods/tensor-basis-neural-network.md)

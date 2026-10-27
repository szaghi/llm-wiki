---
type: Source
title: "Eivazi et al. (2022) — Physics-informed neural networks for solving Reynolds-averaged Navier–Stokes equations"
description: "Solves the two-dimensional incompressible RANS equations with a physics-informed neural network that outputs mean velocity, pressure and Reynolds stresses, trained on boundary data and equation residuals without a turbulence model; tested on Falkner–Skan, zero- and adverse-pressure-gradient boundary layers, a NACA4412 suction side and the periodic hill."
resource: "doi:10.1063/5.0095270"
source_kind: paper
authors: [Eivazi H., Tahani M., Schlatter P., Vinuesa R.]
year: 2022
venue: "Phys. Fluids 34:075117"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Physics_of_Fluids_Eivazi_Physics-informed_neural_networks_for_solving_Reynolds-averag.pdf"
tags: [rans, data-driven, neural-network, boundary-layer]
timestamp: 2026-10-25T20:39:00Z
---

# Summary

Eivazi et al. (2022) apply [physics-informed neural networks](/methods/physics-informed-neural-network.md)
to the two-dimensional incompressible RANS equations without any
turbulence model or closure assumption, in particular without the
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md). The averaged
system is underdetermined (six unknowns $\langle u\rangle$, $\langle v\rangle$,
$\langle p\rangle$, $R_{11}$, $R_{12}$, $R_{22}$ against three equations);
the authors close it with data. A fully connected network (8 hidden layers
of 20 tanh neurons) maps $(x,y)$ to the six mean quantities and is trained,
by Adam and then BFGS, on a loss that adds the squared RANS residuals,
computed by automatic differentiation at interior and boundary points, to a
supervised mismatch with reference data on the domain boundaries only,
Reynolds-stress components included. The Reynolds number enters only
through $\nu$ in the residuals.

Five cases are reported with relative $\ell_2$ errors: a laminar
Falkner–Skan layer in an adverse pressure gradient (errors at most 0.12%,
pressure recovered without pressure data); the zero-pressure-gradient
[turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md) DNS of
Eitel-Amor et al. ($1000<Re_\theta<7000$; 1.02–6.46%); the adverse-pressure-gradient
layer of Bobke et al. at Clauser parameter about 1 (0.28–7.96%); the
suction-side layer of a NACA4412 airfoil at $Re_c=2\times10^5$ (1.56–11.36%);
and the [periodic hill](/benchmarks/periodic-hill.md) at $Re_h=2800$,
where the mean streamwise velocity error is 2.77% and the wall-normal
velocity and Reynolds-stress errors are 16.7–28.2%. The supervision uses
Reynolds stresses on the inflow and outflow boundaries taken from the
DNS or LES of the same flow. The paper does not discuss generalization to
flows without such boundary data, does not compare with
[field inversion](/methods/field-inversion-machine-learning.md), and does
not use the terms of [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).

# Version read

arXiv preprint arXiv:2107.10711v1 [physics.flu-dyn], 22 July 2021, 6 pages
(two-column), all read; pp. 2–5 also read visually for Eq. (1), Fig. 1 and
the captions. Not the Phys. Fluids version of record (2022), whose content
and reference list may differ; every claim here is from v1. Page-1 title
and authors match the metadata; no identity problem. Numbering on this
page is that of this version. The preprint does not print the numbers of
collocation and boundary points, learning rates, epochs, training time or
hardware.

# Key claims

1. PINNs solve the incompressible RANS equations "without any specific model or assumption for turbulence", using only data on the domain boundaries, Reynolds-stress components included, plus the RANS residuals (Abstract, §1, §4). **Shown**
2. Reynolds averaging leaves an underdetermined system that traditional solvers close with modelling assumptions; here boundary data and the network supply the closure (§1). **Stated**
3. The network inputs are $(x,y)$ and its outputs $\langle u\rangle$, $\langle v\rangle$, $\langle p\rangle$, $R_{11}$, $R_{12}$, $R_{22}$; the derivatives in the residuals come from automatic differentiation (§2, Fig. 1). **Stated** (method definition)
4. The loss is $\mathcal L=\mathcal L_e+\mathcal L_b$, the mean squared residuals of the three equations $\mathcal E_1=\langle u\rangle\partial_x\langle u\rangle+\langle v\rangle\partial_y\langle u\rangle+\rho^{-1}\partial_x\langle p\rangle-\nu\nabla^2\langle u\rangle+\partial_xR_{11}+\partial_yR_{12}$, $\mathcal E_2$ (the $y$ counterpart with $\partial_xR_{12}+\partial_yR_{22}$) and $\mathcal E_3=\partial_x\langle u\rangle+\partial_y\langle v\rangle$ over $N_e$ points, plus the mean squared mismatch of the six outputs over $N_b$ boundary samples; loss weights are possible but none is reported as used (§2, Eq. 1, Fig. 1). **Stated**
5. The Reynolds number is set only through $\nu$ in the equations (§1). **Stated**
6. The laminar case uses 8 hidden layers of 20 neurons with tanh activation, trained by Adam and then BFGS stopped on an increment tolerance; the other cases use a "similar model architecture and training procedures" (§3). **Stated**
7. Laminar Falkner–Skan layer in an adverse pressure gradient ($Re=100$, $m=-0.08$, $\beta_{FS}=2m/(m+1)=-0.1739$, separation at $-0.1988$): errors 0.07% ($\langle u\rangle$), 0.12% ($\langle v\rangle$), 0.001% ($\langle p\rangle$), with only boundary velocity supervised; the pressure is predicted accurately without pressure data (§3, Fig. 2, Table 1). **Shown**
8. Zero-pressure-gradient layer ($1000<Re_\theta<7000$, DNS of Eitel-Amor et al. 2014), continuity and streamwise momentum only, outputs $\langle u\rangle$, $\langle v\rangle$, $R_{12}$: errors 1.02%, 4.25%, 6.46% (§3, Table 1, Fig. 3). **Shown**
9. Zero-pressure-gradient case: shape factor and $C_f$ along $Re_\theta$, and inner-scaled $\langle u\rangle$ and $R_{12}$ profiles at $Re_\theta=2500$, 4000, 5500, agree with the reference (§3, Fig. 3). **Shown**
10. Adverse-pressure-gradient layer ($910<Re_\theta<3360$, constant Clauser parameter $\beta_C=(\delta^*/\tau_w)\,dP_\infty/dx\simeq1$, Bobke et al. 2017), continuity and both momentum equations: errors 0.28% ($\langle u\rangle$), 1.57% ($\langle v\rangle$), 4.60% ($\langle p\rangle$), 7.96% ($R_{12}$) (§3, Table 1, Fig. 4). **Shown**
11. Adverse-pressure-gradient case: the $R_{12}$ predictions "coincide with the reference data" without a turbulence model; shape factor, $C_f$ and profiles at $Re_\theta=1623$, 2138, 2588 agree (§3, Fig. 4). **Shown**
12. NACA4412 suction-side layer at $Re_c=2\times10^5$ (well-resolved spectral-element LES of Vinuesa et al. 2018), $0.5<x/c<1$, inputs in wall-tangent and wall-normal coordinates, all six outputs: errors 1.56% ($\langle u\rangle$), 2.17% ($\langle v\rangle$), 7.30% ($\langle p\rangle$), 9.43% ($R_{11}$), 11.36% ($R_{12}$), 4.69% ($R_{22}$) (§3, Table 1, Fig. 5). **Shown**
13. NACA4412: inner-scaled profiles of $\langle u\rangle$, $R_{12}$, $R_{11}$, $R_{22}$ at $x/c\simeq0.625$, 0.75, 0.875 show "excellent agreement" (§3, Fig. 5). **Shown**
14. Periodic hill at $Re_h=2800$ (crest height and bulk velocity at the crest; spectral-element DNS reference), $1<x/h<5$: errors 2.77% ($\langle u\rangle$), 19.70% ($\langle v\rangle$), 8.61% ($\langle p\rangle$), 28.18% ($R_{11}$), 16.70% ($R_{12}$), 20.24% ($R_{22}$) (Table 1). **Shown**
15. Periodic hill: the PINN simulates the separated flow "without a turbulence model"; the extent of the separated region and the reattachment point are "accurately predicted", and $\langle u\rangle$ profiles at five stations agree (§3, Fig. 6). **Shown** (visual comparison; no reattachment length is printed)
16. Periodic hill: since velocity and Reynolds stresses vanish on the walls, supervised data are needed only at the inlet and outlet, plus pressure on all boundaries (§3). **Stated**
17. The average relative errors are 3.91% (zero pressure gradient) and 3.60% (adverse pressure gradient) (§4). **Shown**
18. For the NACA4412 and the periodic hill, PINNs give the streamwise velocity "with less than 3% error" and "good accuracy even in the simulation of Reynolds-stress components" (§4); the hill's Reynolds-stress errors in Table 1 are 16.70–28.18%. **Shown**
19. Jin et al. (2021) simulated turbulence directly with PINNs, in good agreement with DNS (§1). **Stated** (cited)

# Printed slips

1. The Fig. 4 caption labels a panel "(d) Inner-scaled mean streamwise velocity $U^+$ ...", but the figure has panels (a)–(c) and the text refers to "Figure 4(c)" (p. 4).
2. Eq. (1b) sums over three governing equations, but the zero-pressure-gradient case uses two (continuity and streamwise momentum) and the laminar case has no Reynolds-stress terms: Eq. (1) is the general form, not the one used in every case.
3. §1: "extraction of turbulence theory form data".
4. §3: "Results for E is reported in Table 1"; "cf" printed in roman once (p. 4) against $c_f$ elsewhere.
5. The periodic-hill DNS reference is described ("DNS simulation using a spectral-element method") without a citation.

# Notation map

| Eivazi et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $V$, $P$ | $\langle u\rangle$, $\langle v\rangle$, $\langle p\rangle$ | Reynolds-averaged; $P$ is divided by $\rho$ explicitly in the equations |
| $\overline{u^2}$, $\overline{uv}$, $\overline{v^2}$ | $R_{11}$, $R_{12}$, $R_{22}$ | **collision:** the source's overbar is a Reynolds average, not the LES filter; kinematic, positive convention, entering the momentum equations with a plus sign |
| $\overline{uv}^+$, $U^+$ | $R_{12}/u_\tau^2$, $u^+$ | inner scaling |
| $\epsilon_i^n$ | $\mathcal E_i^n$ (page-local residual) | **collision:** not the dissipation rate $\varepsilon$ |
| $L$, $L_e$, $L_b$ | $\mathcal L$, $\mathcal L_e$, $\mathcal L_b$ | total, residual and boundary-data losses |
| $N_e$, $N_b$ | (numbers of residual and boundary points) | values not printed |
| $\mathbf U_b^n$, $\tilde{\mathbf U}_b^n$ | (boundary data vector, network prediction) | **collision:** the tilde is a prediction, not a Favre filter |
| $\boldsymbol w$, $\boldsymbol b$ | $\boldsymbol\theta$ | network weights and biases |
| $E_i$ | (relative $\ell_2$ error in %, written in words) | **collision:** not the total energy $E$ |
| $m$, $\beta_{FS}$ | (Falkner–Skan exponent and pressure-gradient parameter) | |
| $\beta=\delta^*/\tau_w\,dP_\infty/dx$ | $\beta_C$ (Clauser parameter, page-local) | **collision:** the registry $\beta(\boldsymbol x)$ is the field-inversion correction |
| $Re_\theta$, $Re_c$, $Re_b$ | $Re_\theta$, $Re_c$, $Re_h$ | the source's $Re_b$ is based on the crest height and the bulk velocity at the crest |
| $H$ (hill crest height), $H_{12}=\delta^*/\theta$ | $h$ (page-local hill height), (shape factor) | $h$ is not the element size here |
| $c_f=2(u_\tau/U_\infty)^2$ | $C_f$ | |
| $u_\tau=\sqrt{\tau_w/\rho}$, $\ell^*=\nu/u_\tau$ | $u_\tau$, $\delta_\nu$ | |
| $x_n$, $y_n$ | (wall-tangent and wall-normal coordinates, NACA4412) | |

# Reference list

27 printed references, author–year style, without titles (journal, volume,
first page, year; some arXiv numbers). The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug; the entries carry
a placeholder title because none is printed. No printed duplicates and no
unparseable items. Güemes et al. (2021) is printed as "Phys. Fluids (2021),
arXiv:2103.07387" without volume or page; Guastoni et al. (2020), Arzani et
al. (2021), Baydin et al. (2018) and Kingma & Ba (2017) are arXiv-only;
Abadi et al. (2016) prints "et al.". Raissi (2019a, b) take suffixes in
printed order. The citation of Duraisamy, Iaccarino & Xiao (2019) is the
bundle's Source [duraisamy-2019](/sources/duraisamy-2019.md). The reference
list of the version of record may differ.

# Pages created or updated

Chunk 3 (2026-10-26), cited further in chunk 9. This source is cited on:

- [NACA 4412 airfoil](/benchmarks/naca-4412-airfoil.md)
- [Periodic hill](/benchmarks/periodic-hill.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Field inversion and machine learning](/methods/field-inversion-machine-learning.md)
- [Physics-informed neural networks for RANS](/methods/physics-informed-neural-network.md)

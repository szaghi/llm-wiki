---
type: Definition
title: "Notation registry"
description: "Normative symbol registry — every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-10-26T10:28:00Z
---

# Notation registry

Every concept page of this bundle writes mathematics in the symbols below.
A source's own symbols are translated on its Source page (`# Notation map`).
The registry was seeded on 2026-10-25 from the first chunk: the
data-driven modelling reviews, the MHD turbulence review, explicit and
implicit LES, backscatter, wall models and the wall-model survey,
transition and hybrid RANS/LES models, kinetic-energy-preserving DG and
FLEXI, learned closures. It follows Pope's *Turbulent Flows* for averaging
and the positive (kinematic) convention for the Reynolds and subgrid
stresses, because most sources do. Extend this registry, and log the
extension, before writing a symbol it lacks.

**Conventions that the sources split on, fixed here.** The Reynolds stress
and the subgrid stress carry a **positive trace**
($R_{ii}=2k$, $\tau_{ii}=2k_{\mathrm{sgs}}$); sources that print the
negative convention ($-\rho\overline{u_i'u_j'}$, $\bar u_i\bar u_j-\overline{u_iu_j}$)
are translated on their Source page. The strain-rate magnitude always
carries the factor two, $|S|=\sqrt{2S_{ij}S_{ij}}$. The wall-normal
coordinate is always $y$ (sources with $z$ wall-normal are translated).
The overbar is the LES filter, never a Reynolds average.

**Clashes kept on purpose.** A few letters carry two meanings in
well-separated families; the family is always clear from the page, and a
page that needs both meanings renames one locally and says so: $k$
(turbulent kinetic energy; the wavenumber magnitude on spectral pages,
where the kinetic energy is then written $K$), $\gamma$ (ratio of specific
heats; the intermittency of transition models, only on transition pages),
$\Omega_{ij}$ (rotation-rate tensor; a system rotation rate is
$\Omega_{\mathrm{rot}}$), $\delta$ (boundary-layer thickness or channel
half-height; $\delta_{ij}$ the Kronecker delta carries indices), $N$ (the
polynomial degree of element methods; grid sizes are $N_x$, $N_x\times
N_y\times N_z$).

## 1. Flow equations

| Symbol | Meaning | Note |
|---|---|---|
| $u_i$, $\boldsymbol u$ | velocity | components $(u,v,w)$ in $(x,y,z)$, $x$ streamwise, $y$ wall-normal, $z$ spanwise |
| $p$ | pressure | kinematic ($p/\rho$) in incompressible pages, said per page |
| $\rho$, $T$, $E$ | density, temperature, total energy per unit volume | compressible pages |
| $\mu$, $\nu=\mu/\rho$ | dynamic and kinematic molecular viscosity | $\nu_w$, $\mu_w$ at the wall |
| $\gamma$, $Pr$ | ratio of specific heats, Prandtl number | $c_p$ specific heat at constant pressure |
| $S_{ij}=\tfrac12(\partial_ju_i+\partial_iu_j)$ | strain-rate tensor | $S^d_{ij}=S_{ij}-\tfrac13S_{kk}\delta_{ij}$ deviatoric part |
| $\Omega_{ij}=\tfrac12(\partial_ju_i-\partial_iu_j)$ | rotation-rate tensor | |
| $\lvert S\rvert=\sqrt{2S_{ij}S_{ij}}$, $\lvert\Omega\rvert=\sqrt{2\Omega_{ij}\Omega_{ij}}$ | magnitudes | always with the factor two; sources without it are translated |
| $\omega_i=\epsilon_{ijk}\partial_ju_k$ | vorticity | the specific dissipation rate $\omega$ (§4) has no index |
| $\sigma_{ij}$ | viscous stress, $2\mu S^d_{ij}$ (Newtonian, Stokes hypothesis) | |
| $f_i$ | body force per unit mass (forcing) | |

## 2. Averaging and filtering

| Symbol | Meaning | Note |
|---|---|---|
| $\langle\phi\rangle$ | Reynolds (ensemble, time or homogeneous-direction) average | the averaging directions are said per page |
| $\phi'=\phi-\langle\phi\rangle$ | Reynolds fluctuation | |
| $\langle\phi\rangle_\rho=\langle\rho\phi\rangle/\langle\rho\rangle$, $\phi''$ | Favre average and Favre fluctuation | |
| $\bar\phi=G*\phi$ | LES (low-pass) filter with kernel $G$ | grid, explicit or implicit filter, said per page |
| $\Delta$ | filter width | definition per page (grid spacing, cube root of the cell volume, element size over $N+1$, …) |
| $\tilde\phi=\overline{\rho\phi}/\bar\rho$ | Favre-filtered quantity | never used for a Reynolds or a test-filter operation |
| $\hat\phi$, $\hat\Delta$ | test filter and its width | dynamic procedure; $\hat\Delta/\Delta$ the filter-width ratio |
| $\phi^{>}$, $\phi^{<}$ | resolved and unresolved (subfilter) parts | $\phi=\bar\phi+\phi^<$ in LES |
| $\hat G(k)$ | filter transfer function | of a homogeneous filter |
| $\phi_{\boldsymbol k}$ | Fourier coefficient at wavevector $\boldsymbol k$ | never a hat |

## 3. Stresses, energy and closures

| Symbol | Meaning | Note |
|---|---|---|
| $R_{ij}=\langle u_i'u_j'\rangle$ | Reynolds stress (kinematic, positive trace) | $\langle\rho u_i''u_j''\rangle$ in Favre form |
| $k=\tfrac12R_{ii}$ | turbulent kinetic energy | $k_{\mathrm{res}}$, $k_{\mathrm{sgs}}$, $k_{\mathrm{tot}}$ the resolved, subgrid and total parts |
| $b_{ij}=R_{ij}/(2k)-\tfrac13\delta_{ij}$ | normalized anisotropy tensor | |
| $\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$ | subgrid-scale (SGS) stress | positive trace; $\bar\rho(\widetilde{u_iu_j}-\tilde u_i\tilde u_j)$ compressible; $\tau^d_{ij}$ deviatoric part |
| $\nu_t$, $\mu_t=\rho\nu_t$ | eddy viscosity (RANS or SGS, said per page) | |
| $R_{ij}-\tfrac23k\delta_{ij}=-2\nu_t\langle S_{ij}\rangle$ | Boussinesq (linear eddy-viscosity) closure | $\tau^d_{ij}=-2\nu_t\bar S^d_{ij}$ in LES |
| $\Pi=-\tau_{ij}\bar S_{ij}$ | local SGS energy flux | positive = forward cascade (resolved to subgrid), negative = backscatter |
| $P_k=-R_{ij}\partial_j\langle u_i\rangle$ | production of $k$ | |
| $\varepsilon$ | dissipation rate of turbulent kinetic energy | $\varepsilon=2\nu\langle s_{ij}s_{ij}\rangle$ with $s_{ij}$ the fluctuating strain |
| $C_s$ | Smagorinsky coefficient, $\nu_t=(C_s\Delta)^2\lvert\bar S\rvert$ | values per page and source |
| $L_{ij}=\widehat{\bar u_i\bar u_j}-\hat{\bar u}_i\hat{\bar u}_j$ | resolved (Leonard) stress of the Germano identity | |
| $T^{(n)}$, $g^{(n)}$ | integrity-basis tensors of Pope (1975), $n=1,\dots,10$, and their coefficients | $b_{ij}=\sum_ng^{(n)}T^{(n)}_{ij}$ |

## 4. RANS and transition model variables

| Symbol | Meaning | Note |
|---|---|---|
| $\omega$ | specific dissipation rate, $\varepsilon/(\beta^*k)$ | $k$-$\omega$ family |
| $\tilde\nu$ | Spalart–Allmaras working variable | the only tilde that is not a Favre filter; $\chi=\tilde\nu/\nu$ |
| $d$ | distance to the nearest wall | |
| $C_\mu$, $\beta^*$, $\sigma_k$, $\sigma_\omega$, $c_{b1}$, … | model constants | named as in the original model; values given per page |
| $F_1$, $F_2$ | SST blending functions | |
| $\gamma$ | intermittency (transition pages only) | see the clash list above |
| $Re_\theta$, $Re_{\theta c}$ | momentum-thickness Reynolds number; its critical (onset) value | |
| $Tu$ | free-stream turbulence intensity (percent) | |
| $f_k$, $f_\varepsilon$, $f_\omega$ | PANS ratios of unresolved to total $k$, $\varepsilon$, $\omega$ | |

## 5. Walls and boundary layers

| Symbol | Meaning | Note |
|---|---|---|
| $\tau_w$, $u_\tau=\sqrt{\tau_w/\rho_w}$ | wall shear stress, friction velocity | |
| $\delta_\nu=\nu_w/u_\tau$ | viscous length | |
| $y^+=y/\delta_\nu$, $u^+=\langle u\rangle/u_\tau$ | wall (inner) units | $\Delta x^+$, $\Delta y^+$, $\Delta z^+$ grid spacings in wall units |
| $\kappa$, $B$ | von Kármán constant, log-law intercept | $u^+=\kappa^{-1}\ln y^++B$; values per page and source |
| $A^+$ | van Driest damping constant | |
| $\delta$, $\delta^*$, $\theta$ | boundary-layer thickness (or channel half-height), displacement and momentum thickness | $\delta_{99}$ the 99% thickness |
| $Re_\tau=u_\tau\delta/\nu_w$ | friction Reynolds number | |
| $h_{\mathrm{wm}}$ | wall-model matching height | $U_{\mathrm{LES}}$ the LES velocity there |
| $(\cdot)^*$ | semi-local scaling (local $\bar\rho(y)$, $\bar\mu(y)$) | $u_\tau^*=\sqrt{\tau_w/\bar\rho(y)}$; $\delta^*$ keeps its displacement meaning |
| $C_f$, $C_p$ | skin-friction and pressure coefficients | $C_L$, $C_D$ lift and drag coefficients |

## 6. Element discretizations

| Symbol | Meaning | Note |
|---|---|---|
| $N$ | polynomial degree of DG, flux-reconstruction and spectral-element methods | sources' $p$, $k$; order $N+1$; $(N+1)^d$ nodes per element |
| $\xi$, $\xi_i$, $w_i$ | reference coordinate, quadrature nodes, quadrature weights | LGL or Gauss, said per page; never $\omega_i$ |
| $D_{ij}$ | differentiation matrix | |
| $\{\!\{\phi\}\!\}$ | arithmetic mean of two states | split forms, two-point fluxes |
| $f^{\#}(u_L,u_R)$, $f^*$ | two-point volume flux, interface numerical flux | |
| $h$ | element or cell size | $\Delta$ stays the filter width |
| $\alpha$ | DG/finite-volume blending factor ($\alpha=1$ pure finite volume) | |

## 7. Data-driven models

| Symbol | Meaning | Note |
|---|---|---|
| $\boldsymbol\zeta$ | input features of a learned model | |
| $\boldsymbol\theta$ | trainable parameters (weights, biases, model coefficients) | |
| $\mathcal L$ | loss function | |
| $\beta(\boldsymbol x)$ | spatial correction field of field inversion (multiplier of a model term) | the SST constant $\beta^*$ carries a star |
| $\boldsymbol\delta$ | model discrepancy (target of a learned correction) | |
| $s_t$, $a_t$, $r_t$, $\pi_{\boldsymbol\theta}$ | state, action, reward, policy of reinforcement learning | |
| a priori / a posteriori | testing on filtered or averaged reference data outside the solver / testing (or training) with the model inside the solver | |

## 8. Turbulence scales and spectra

| Symbol | Meaning | Note |
|---|---|---|
| $\eta=(\nu^3/\varepsilon)^{1/4}$, $\tau_\eta$ | Kolmogorov length and time | |
| $\lambda$, $Re_\lambda$ | Taylor microscale, Taylor-scale Reynolds number | |
| $L$ | integral length scale | defined per page |
| $E(k)$ | three-dimensional energy spectrum at wavenumber magnitude $k$ | spectral pages: TKE written $K=\int E\,dk$ (clash list above) |
| $k_c$ | cutoff wavenumber of the filter or grid | |
| $\nu_t(k\mid k_c)$ | spectral eddy viscosity | |

## 9. Dimensionless numbers

| Symbol | Meaning | Note |
|---|---|---|
| $Re$ | Reynolds number | reference length and velocity stated per page ($Re_c$ chord, $Re_D$ diameter, $Re_b$ bulk, $Re_h$ hill height) |
| $M$ | Mach number | $M_\infty$, $M_b$, $M_e$, $M_t$ turbulent Mach number |
| $Pr_t$ | turbulent Prandtl number | |
| $St$ | Strouhal number | |

## 10. MHD turbulence

| Symbol | Meaning | Note |
|---|---|---|
| $\boldsymbol B$, $\boldsymbol B_0$, $\boldsymbol b$ | magnetic field, mean (guide) field, fluctuation | $\boldsymbol b$ in velocity (Alfvénic) units, $\boldsymbol b=\delta\boldsymbol B/\sqrt{4\pi\rho}$, unless a page says otherwise |
| $v_A=B_0/\sqrt{4\pi\rho}$ | Alfvén speed | Gaussian units; SI pages write $B_0/\sqrt{\mu_0\rho}$ |
| $\boldsymbol Z^\pm=\boldsymbol u\pm\boldsymbol b$ | Elsasser fields | $Z^+$ propagates along $+\boldsymbol B_0$ |
| $\eta_m$ | magnetic diffusivity (resistivity) | never $\eta$, which is the Kolmogorov length |
| $Pm=\nu/\eta_m$, $Rm$ | magnetic Prandtl number, magnetic Reynolds number | $Rm$ based on the outer scale unless a page says otherwise |
| $S_L$ | Lundquist number | never $S$ (strain rate) |
| $\lambda$, $\xi$, $l_\parallel$ | perpendicular scale, scale along the fluctuation, parallel coherence length along the local field | MHD pages only; the Taylor microscale is not used there |
| $\tau_A$, $\tau_{\mathrm{nl}}$ | Alfvén and nonlinear times | |
| $\theta_\lambda$ | alignment angle between Elsasser increments at scale $\lambda$ | |
| $H_m=\boldsymbol A\cdot\boldsymbol B$, $H_c=\boldsymbol u\cdot\boldsymbol B$ | magnetic helicity density, cross-helicity density | $\boldsymbol A$ the vector potential |
| $\beta_p$ | plasma beta | |

## 11. Shared page-local symbols

Symbols defined on a page for one family of methods and reused on a few
others. They are listed so that every page writes them the same way; a page
that uses one still says what it means.

| Symbol | Meaning | Pages |
|---|---|---|
| $e_q=b_q(\Delta/\delta)^{a_q}$ | relative error of a quantity $q$ in WMLES, its error constant and convergence rate ($q=p$ for $C_p$, $u$ for the mean velocity) | wall-modelled LES, equilibrium wall model; sources' $\varepsilon_q$, $\beta_q$, $\alpha_q$ |
| $f(y^+)$ | law-of-the-wall profile, $u^+=f(y^+)$ | law of the wall, wall models |
| $k_u$, $\omega_u$ | unresolved (modelled) turbulent kinetic energy and specific dissipation rate of PANS | PANS, $k$-$\omega$ SST |
| $(\cdot)_{\mathrm m}$ | a quantity computed from the model's own solution, not from reference data | a priori and a posteriori testing, field inversion, model-consistent training |
| $\mathcal F_h$ | filter induced by a discretization (numerically induced filter) | discretization-consistent closure |
| $v^-$, $f^-$ | backscatter volume fraction; net backscatter normalized by the total SGS flux | energy backscatter |
| $\lambda_{CB}$ | critical-balance scale (transition from weak to strong MHD turbulence) | MHD pages |
| $\lambda_D$ | disruption scale of the aligned MHD cascade | MHD pages |
| $\varpi^\pm=\nabla_\perp^2\zeta^\pm$ | Elsasser vorticities, $\zeta^\pm$ the Elsasser potentials | MHD pages |
| $\sigma_c$, $\sigma_r$ | normalized cross-helicity, normalized residual energy | MHD pages |
| $\Gamma_E$, $h_{\min}$ | dynamo growth rate of the magnetic energy; finest cell size of an adaptive grid | small-scale dynamo, numerical dissipation, mesh adaptation, RAMSES |
| $x_R$ | reattachment length of a separated flow | backward-facing step, LES pages |
| $\Delta p_s^+$ | streamwise pressure gradient in inner units | wall law in adverse pressure gradient, turbulent boundary layers |
| $\nu_t^*$, $\nu_t^\dagger$, $a^\perp_{ij}$ | best-fit (optimal) eddy viscosity of a reference stress, unconstrained and non-negative; the non-linear remainder of the anisotropy | Boussinesq hypothesis; McConkey et al. (2022) |
| $c_{RS}$ | stress–strain alignment indicator | Boussinesq hypothesis; Cato et al. (2023) |
| $Re_y$ | local Reynolds number $Uy/\nu$ of an explicit wall law | law of the wall, equilibrium wall model |
| $\nu_t^{\mathrm{hyb}}$, $\nu_t^{\mathrm{RANS}}$, $R^{\mathrm{res}}_{ij}$ | hybrid eddy viscosity of constrained LES, its RANS part, the resolved stress | wall-modelled LES, hybrid RANS/LES, immersed boundary methods |
| $\gamma_{\mathrm{RL}}$, $\Delta t_{\mathrm{RL}}$, $N_s$ | discount factor, action interval and episode length of a reinforcement-learning closure | reinforcement-learning closures |
| $\kappa^{(2)}$, $\kappa^{(4)}$, $\Psi_i$, $\Phi_i$ | second- and fourth-difference dissipation coefficients of JST-type artificial dissipation; Jameson pressure sensor, Ducros vorticity factor | numerical dissipation, low-dissipation low-dispersion scheme, log-layer mismatch |
| $N_f$ | highest modal degree kept by a modal test filter | LES, Vreman model, mesh adaptation, DGSEM |
| $\ell_\Delta$ | filter width in grid units | fractional SGS model, energy backscatter |
| $\alpha_k$, $\beta_k$ | resolved and unresolved fractions of the turbulent kinetic energy | active model split, turbulent channel flow |
| $m_a$ | anisotropy exponent, $l_\parallel\propto\lambda^{m_a}$ | critical balance, compressible MHD turbulence |
| $A_\sigma$ | pre-shock average Atwood number | shock-generated turbulence, Rayleigh–Taylor mixing |
| $R_y=d\sqrt k/\nu$ | wall-distance Reynolds number of low-Reynolds-number RANS damping | $k$-$\varepsilon$ models, $k$-$\omega$ SST |
| $\tau^{\mathrm{ani}}_{ij}$, $\xi^{\mathrm{AR}}_{ij}$, $\tau^{\mathrm a}_{ij}$, $\nu^{\mathrm a}$ | anisotropic (non-eddy-viscosity) part of the SGS stress, its anisotropic redistribution, the anisotropic model stress and its coefficient | Boussinesq hypothesis, energy backscatter, gradient model |
| $\mathsf S_{ij}$, $\mathsf W_{ij}$, $b^\perp_{ij}$, $G^m$ | mean strain and rotation scaled by $k/\varepsilon$; non-linear part of the anisotropy; coefficient of the $m$-th basis tensor | Boussinesq hypothesis, tensor-basis neural network, symbolic-regression closures |
| $\tau_{\mathrm{tr}}$, $h_{ij}$ | training window of an adjoint-trained closure; the network's stress output | model-consistent training, neural-network SGS models |
| $\Delta_k$ | grid spacing in direction $k$ | anisotropic minimum-dissipation model, LES |
| $\tau_s$, $\tau_g$, $\sigma_{\mathrm{IP}}$ | solution- and gradient-jump penalty parameters; interior-penalty coefficient | jump-penalty stabilization, implicit LES |
| $f_q$, $\boldsymbol c_q$, $w_q$, $\tau_{\mathrm{LB}}$ | lattice distribution functions, discrete velocities, lattice weights, relaxation time | lattice Boltzmann methods, ProLB, immersed boundary methods |
| $a_{\mathrm K}$, $D_x$ | split-form weights; discrete derivative operator | pressure-equilibrium preservation, kinetic-energy preservation |
| $N_x$ | number of grid points per direction (not the polynomial degree $N$) | GHOST, lattice Boltzmann methods, MHD pages, DNS |
| $B_{\mathrm{OT}}$ | field amplitude of the Orszag–Tang vortex (no mean field) | decaying MHD turbulence, GHOST |
| $d_i$, $\alpha_H$, $\epsilon_H$ | ion inertial length; Hall coefficient and its normalized strength | exact laws, decaying MHD turbulence, GHOST, lattice Boltzmann methods |
| $C_{\mathrm f}$ | dissipative coefficient of the ensemble-Kalman-calibrated mixed model of Wang et al. (2023c), $C_{\mathrm f}=2C_s^2$ (the source's $C_D$) | gradient model, Smagorinsky model, ensemble Kalman calibration, model-consistent training, isotropic turbulence |
| $C_{\mathrm A}$ | constant of the autonomous eddy-viscosity model | autonomous eddy-viscosity model, spectral eddy viscosity, dynamic procedure |
| $\vartheta_m$, $\alpha_f$, $s_f$ | modal index, strength and order of an exponential modal filter | spectral vanishing viscosity, subcell finite-volume shock capturing |
| $\lambda_{\theta l}$, $Tu_l$ | local pressure-gradient parameter and local turbulence intensity of correlation-based transition models | local-correlation-based transition models, laminar kinetic energy transition models |
| $L_r$ | recirculation length behind a bluff body | circular-cylinder wake, neural-network SGS models, LES pages |

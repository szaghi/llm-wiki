---
type: Definition
title: "Notation registry"
description: "Normative symbol registry of the bundle: averaging and filtering, stresses and closures, RANS, wall, element-discretization, data-driven, spectral, MHD and shared page-local symbols, with the sign and normalization conventions fixed here; every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-10-27T11:02:00Z
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
| $\alpha_k$, $\beta_k$ | modelled (subgrid) fraction $k_{\mathrm{sgs}}/k_{\mathrm{tot}}$ and unresolved fraction $1-k_{\mathrm{res}}/k_{\mathrm{tot}}$ of the turbulent kinetic energy (equal only when the mixed resolved–subgrid terms vanish) | active model split, turbulent channel flow |
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
| $\mu_b$, $\nu_b$, $P_\nu=\nu/\nu_b$, $Re_{\mathrm{bulk}}$ | dynamic and kinematic bulk viscosity; viscous Prandtl number of shear to bulk viscosity; bulk-viscous Reynolds number | bulk viscosity, bottleneck effect, compressible MHD turbulence, small-scale dynamo, numerical dissipation, high-order gas-kinetic scheme |
| $\boldsymbol u_{\mathrm c}$, $\boldsymbol u_{\mathrm s}$, $E_{\mathrm c}(k)$, $E_{\mathrm s}(k)$ | compressive and solenoidal Helmholtz parts of the velocity and their spectra (never $\parallel$/$\perp$, which refer to the magnetic field) | bulk viscosity, bottleneck effect, compressible MHD turbulence, small-scale dynamo |
| $\varepsilon_s$, $\varepsilon_d$ | solenoidal and dilatational parts of the viscous dissipation (on weak-wave turbulence $\varepsilon_s$ is that page's energy flux) | isotropic turbulence, artificial-viscosity shock capturing, shock-generated turbulence, bulk viscosity |
| $\beta_\omega$, $\gamma_\omega$ | destruction and production coefficients of the $\omega$ equation ($k$-$\omega$, SST, the $\omega$ equation of Reynolds-stress models), used where a page needs a name distinct from the field-inversion multiplier $\beta(\boldsymbol x)$ or the DG blending factor $\alpha$; a page quoting a model's constant table may keep the original names | $k$-$\omega$ SST, field inversion, model-form uncertainty, law of the wall, turbulent boundary layer, Reynolds-stress model ($\beta_\omega$), $k$-$\omega$ model, RANS wall functions |
| $g_{\tilde\nu}$ | data-assimilated multiplicative source correction of the SA equation | field inversion, model-form uncertainty, Boussinesq hypothesis, square cylinder, shock/boundary-layer interaction |
| $b^\Delta_{ij}$, $b^R_{ij}$ | additive anisotropy correction; frozen production correction (the $k$-equation residual $R$) of data-driven RANS | Boussinesq hypothesis, symbolic-regression closures, tensor-basis neural network, model aggregation |
| $\nu_{\mathrm{eff}}$, $\nu_{\mathrm{clip}}$ | effective viscosity of a stress projected on the resolved strain; its clipping floor | gradient model, super-resolution SGS models, numerical dissipation, spectral-element method |
| $\sigma_b$ | upwind fraction of a blended convective flux (on symbolic-regression closures a normalizing scale) | numerical dissipation, detached-eddy simulation, TRACE |
| $\mathcal J$ | Jacobian determinant of the reference-to-physical element map | geometric conservation law, DGSEM, flux reconstruction, high-order gas-kinetic scheme, kinetic-energy preservation |
| $T_E$ | large-eddy turnover time | DNS, isotropic-turbulence surrogates, a priori and a posteriori testing, multi-resolution independent simulations |
| $\tau_\theta$ | time unit of the temporal mixing layer, $\theta_0/\Delta U$ | temporal mixing layer, neural-operator LES surrogates |
| $c_{ax}$ | axial chord of a cascade blade | compressor cascade, laminar separation bubble, detached-eddy simulation |
| $\varphi_f$, $\Delta_f$, $\boldsymbol\Lambda$, $\boldsymbol\ell$, $\boldsymbol u_{\mathrm{slip}}$ | fluid volume fraction, kernel width, filtered-gradient ratio, slip length and wall slip velocity of volume-filtered immersed boundaries (Rickard & Kasbaoui) | immersed boundary methods, wall-modelled LES, law of the wall, LES, turbulent channel flow |
| $\eta_p$ | permeability of volume penalization | immersed boundary methods |
| $k_+$, $\varepsilon_+$, $L_+$, $\tau_+$ | ratios of modelled to total turbulent kinetic energy, dissipation, length and time scale of continuous eddy simulation and PITM (not wall units; not the $\alpha_k$, $\beta_k$ above, whose total energy is defined differently) | continuous eddy simulation, hybrid RANS/LES, periodic hill, PANS |
| $\beta_{\mathrm{CES}}$, $\psi_\beta$ | coefficient and factor of the CES modification of the SST destruction term | continuous eddy simulation, hybrid RANS/LES |
| $\mu_t^{\mathrm{bl}}$ | wall-distance-blended eddy viscosity of a hybrid RANS/LES (not $\nu_t^{\mathrm{hyb}}$ of constrained LES) | flamelet-based tabulated chemistry, hybrid RANS/LES |
| $\phi^{\ln}$ | logarithmic mean of a two-point flux | entropy conservation, kinetic-energy preservation |
| $\mathrm{IS}_k$, $a_k$, $\mathsf w_k$ | smoothness indicator, unnormalized and normalized weight of WENO stencil $k$ (not $\alpha_k$, $\beta_k$ above) | WENO schemes |
| $A_{\mathrm{pl}}$, $m_{\mathrm{pl}}$, $y_1^+$ | constants of a power-law wall function; first-element height in wall units | RANS wall functions, $k$-$\omega$ model, DGSEM |
| $\varsigma_i$, $C_\sigma$, $\mathcal D_\sigma$ | singular values of the velocity gradient, constant and differential operator of the $\sigma$ model | sigma model, neural-network SGS models |
| $P_A$, $Q_A$, $R_A$ | invariants of the resolved velocity-gradient tensor | neural-network SGS models, tensor-basis neural network |
| $t_{\mathrm{run}}$ | run length in flow-through times | grid-point requirements, boundary-layer-conforming grids |
| $\gamma^{\mathrm T}_k$, $\chi^{\mathrm T}_k$, $\delta^{\mathrm T}_k$, $C_T$, $d_k$ | scale-separated smoothness measure of TENO stencil $k$, its normalized form, the 0/1 cut-off flag, the cut-off threshold and the optimal linear weights (with $\mathrm{IS}_k$, $\mathsf w_k$ above) | WENO/TENO schemes, shock sensors |
| $\beta_{\mathrm{TH}}$, $\alpha_{\mathrm{TH}}$ | steepness and flux auxiliary of the THINC jump reconstruction | WENO/TENO schemes (TENO-THINC), numerical dissipation |
| $\chi_f$ | strength of a relaxation or explicit filter (never bare $\chi$, the SA ratio) | explicit modal filtering, large-eddy simulation, implicit LES, low-dissipation schemes |
| $\tau^{\mathrm{gr}}_{ij}$, $\tau^{\mathrm{sf}}_{ij}$, $\tau^{\mathrm{ef}}_{ij}$, $N_{\mathrm{AD}}$, $\varepsilon_{\mathrm{DD}}$, $N_{\mathrm{st}}$ | grid-truncation and sub-filter parts of the total stress $\tau^{\mathrm{tot}}_{ij}$ of explicitly filtered LES, the explicitly-filtered stress; number of van Cittert terms of approximate deconvolution, limiter of dynamic deconvolution, stencil size of iterative deconvolution (filter-to-grid ratio written $\Delta/h$) | scale-similarity model, large-eddy simulation, a priori and a posteriori testing, energy backscatter, Taylor–Green vortex |
| $\tau_t$, $\Gamma_k$, $\Gamma_\omega$ | turbulent time scale $1/\omega$ of the $k$-$\tau$ model; diffusivities of the $k$ and $\omega$ ($\tau$) equations | $k$-$\tau$ model, Nek5000, spectral element method |
| $\Phi_L$, $\chi_\Phi$, $\psi$, $L_{vK}$ | length-scale variable $\sqrt k\,L$ of the $k$-$\sqrt k L$ model, its normalized form and positive surrogate; von Kármán length | scale-adaptive simulation, hybrid RANS/LES |
| $f_P$, $f_{P2}$, $f_R$, $\mathcal G_{\tilde\nu}$, $\mathcal G_\Omega$ | shielding functions and sensors of ZDES mode 2 (2020) | detached-eddy simulation, lattice Boltzmann method, ProLB |
| $k_L$, $R_{\mathrm{TRG}}$, $c_\theta$, $\gamma_A$, $\gamma_B$ | laminar kinetic energy; natural-transition transfer term; local $Re_\theta$ calibration constant; intermittency-like onset measures | laminar kinetic energy transition model, ERCOFTAC T3 |
| $\mathcal E_{\mathrm{SA}}$, $\boldsymbol W_{\mathrm{SA}}$ | entropy function and entropy variables of the entropy-stable SA system | entropy conservation, Spalart–Allmaras model |
| $L_{\mathrm{sc}}$, $Se_{\mathrm{sc}}$, $k_{Se}$ | scaled interaction length and separation criterion of shock/boundary-layer interactions, and the factor of the latter (the registry's $(\cdot)^*$ is semi-local scaling) | shock/turbulent boundary-layer interaction, FLEXI |
| $h_n$ | nozzle exit height of a jet (the registry's $h$ is the cell size) | inflow turbulence generation, FW-H analogy, wall-modelled LES |
| $\tilde\omega_\ell=\ln\omega$ | logarithmic $\omega$ variable of log-$\omega$ formulations | $k$-$\omega$ model, $k$-$\omega$ SST, laminar kinetic energy transition model |
| $\delta_r$ | boundary-layer thickness at a reference station (shock interaction, synthetic inflow) | Morkovin hypothesis, inflow turbulence generation, shock/turbulent boundary-layer interaction |
| $d_{\mathrm{IP}}$ | distance of the image (interpolation) point from an immersed wall | immersed boundary methods, RANS wall functions |
| $\alpha_{\mathrm{KT}}$, $\beta_{\mathrm{KT}}$, $a_s$, $b_s$, $E_D$, $\ell^\pm$ | von Kármán–Taylor constants and shear-source strengths of nearly incompressible MHD transport models; residual energy; Elsasser correlation lengths (not the registry's $\lambda$) | compressible MHD turbulence, critical balance |
| $C_I$ | Yoshizawa coefficient of the isotropic subgrid stress | Smagorinsky model, explicit modal filtering, Boussinesq hypothesis |
| $\tau_{\mathrm{col}}$, $\tau_{\mathrm{col},t}$ | collision time of a gas-kinetic (BGK) scheme and its turbulent increment, $\tau_{\mathrm{col}}+\tau_{\mathrm{col},t}=(\mu+\mu_t)/p$ (never $\tau_t$, the $k$-$\tau$ time scale) | high-order gas-kinetic scheme, large-eddy simulation, lattice Boltzmann method |
| $C_{\mathrm{Th}}$, $M_{\mathrm{tip}}$, $\psi_{\mathrm w}$, $R_{\mathrm r}$ | rotor thrust coefficient (not the TENO cut-off $C_T$), tip Mach number, wake age (not the $k$-$\sqrt kL$ surrogate $\psi$), rotor radius | Caradonna–Tung rotor, FW-H acoustic analogy |
| $C_h$ | Stanton number (the registry's $St$ is the Strouhal number) | Morkovin hypothesis, wall-modelled LES, non-equilibrium wall models |
| $h_p$ | plunge amplitude of an oscillating body (not the cell size $h$) | circular-cylinder wake |
| $F$, $D_{\mathrm m}$, $a_{\mathrm{cf}}$, $F_{\mathrm{num}}$, $F_{\mathrm{sgs}}$ | thickening factor, molecular diffusivity, counterflow strain rate; numerical and subgrid parts of the thickening | thickened flame model, flamelet-based tabulated chemistry |
| $\alpha_\omega$, $\alpha^*_\omega$ | destruction coefficients of Heinz's $\omega=\varepsilon/k$ form (not $\beta$, $\beta^*$) | continuous eddy simulation, $k$-$\omega$ model, detached-eddy simulation |
| $\mathsf s_{ij}$, $\mathsf w_{ij}$ | resolved strain and rotation normalized by the strain magnitude in tensor-basis SGS models | tensor-basis neural network, symbolic-regression closures |
| $\beta_{RC}$ | Clauser pressure-gradient parameter | adverse-pressure-gradient wall law, non-equilibrium wall models |
| $P_{\mathrm{TV}}$ | threshold of the relative total-variation limiter of bandwidth-optimized WENO | WENO schemes |
| $\eta_Z$, $\zeta_Z$ | thickness and position coordinates of a counterflow mixing layer in mixture fraction | thickened flame model |
| $C_{\mathrm{DM}}$ | constant of the Duan–Martín temperature–velocity relation (not the TENO cut-off $C_T$) | Morkovin hypothesis, compressible velocity transformations, Baldwin–Lomax model, inverse-velocity-transformation wall model |
| $\lambda_{\mathrm{AD}}$ | adjustable-dissipation parameter of Deng et al.'s BVD reconstruction (not the Taylor microscale $\lambda$) | low-dissipation low-dispersion schemes, implicit LES, numerical dissipation, direct numerical simulation, isotropic turbulence |
| $\Pi^{\mathrm t}_{\mathrm{pd}}$, $\Pi^{\mathrm{sgs}}_{\mathrm{pd}}$, $\Pi_{\mathrm{sph}}$ | turbulent and subgrid pressure-dilatation terms; spherical (trace) part of the subgrid energy transfer (never the bare SGS flux $\Pi$) | pressure dilatation, energy backscatter, bulk viscosity |
| $\mu_{b,\mathrm{AV}}$, $Pr_{\mathrm{AV}}$ | artificial bulk viscosity and its Prandtl number (the physical or subgrid bulk viscosity is $\mu_b$, §11 above) | bulk viscosity, artificial-viscosity shock capturing, numerical dissipation |
| $M_{\mathrm{sgs}}$ | subgrid Mach number | energy backscatter, shock-generated turbulence, Taylor–Green vortex |
| $\mathsf S^\omega_{ij}$, $\mathsf W^\omega_{ij}$, $t_{\mathrm{turb}}$ | mean strain and rotation scaled by $1/\omega$ (the $k/\varepsilon$-scaled forms are $\mathsf S_{ij}$, $\mathsf W_{ij}$); generic turbulent time scale of an EARSM | explicit algebraic Reynolds-stress model, Boussinesq hypothesis |
| $\{\cdot\}_e$, $[\![\cdot]\!]$ | element average; interface jump (never $\langle\cdot\rangle$, the Reynolds average) | shock sensors, artificial-viscosity shock capturing, entropy conservation, explicit modal filtering |
| $\vartheta^{\mathrm t}_m$, $\vartheta^{\mathrm t}_c$, $\vartheta^{\mathrm t}_{\max}$ | unnormalized total degree of an orthonormal mode, its cut-off and maximum (the normalized index is $\vartheta_m$) | explicit modal filtering, Taylor–Green vortex |
| $\nu^\omega_{\mathrm{eff}}$ | effective viscosity defined by $-\mathrm dE_k/\mathrm dt=\nu^\omega_{\mathrm{eff}}\langle\omega_i\omega_i\rangle$ (not the projected $\nu_{\mathrm{eff}}$) | numerical dissipation, spectral element method |
| $\tau_{\mathrm M}$, $\tau_{\mathrm C}$, $\boldsymbol r_{\mathrm M}$, $r_{\mathrm C}$ | momentum and continuity stabilization parameters and residuals of residual-based VMS | variational multiscale method, immersed boundary method |
| $\Theta$, $\tilde\Theta$ | temporal filter width and its dimensionless form (temporal LES) | large-eddy simulation, lattice Boltzmann method, Taylor–Green vortex |
| $L_{\mathrm{int}}$ | interaction length of a shock/boundary-layer interaction (not the scale-separation length $L_{\mathrm{sc}}$) | shock–turbulent boundary layer interaction, wall-modelled LES, equilibrium and non-equilibrium wall models |
| $\mu^w_{\mathrm{sgs}}$, $\lambda^w_{\mathrm{sgs}}$ | wall-model eddy viscosity and eddy conductivity | equilibrium wall model, wall-modelled LES |
| $\varpi_{\mathrm p}$ | angular frequency of a pitching airfoil | dynamic stall, NACA 0012 airfoil |
| $\alpha_h$ | hill-width factor of the parametrized periodic hill | periodic hill |
| $C_{\mathrm{MT}}$, $y_{0,\mathrm r}$ | Mason–Thomson wall-damping constant of the Smagorinsky length (the sources' $C_0$, not the gradient-model $C_0$); aerodynamic roughness length | Smagorinsky model, LESGO, equilibrium wall model, law of the wall, actuator models |
| $\epsilon_{\mathrm G}$, $a_{\mathrm i}$, $C'_{\mathrm{Th}}$ | Gaussian kernel width of actuator forces; axial induction factor; local (disk-velocity) thrust coefficient | actuator line and disk models, LESGO |
| $\gamma^*_{\mathrm{PaSR}}$, $\tau_{\mathrm{ch}}$, $\tau_{\mathrm{mix}}$, $u'_\Delta$ | reacting fraction of a partially stirred reactor cell; chemical and mixing time scales; subgrid velocity scale | thickened flame model, flamelet-based tabulated chemistry |
| $s_{\mathrm L}$ | laminar flame speed (the registry's $S_L$ is the Lundquist number) | flamelet-based tabulated chemistry, thickened flame model |
| $F_r$, $L_i$, $L_c$, $L_k$, $C_x$, $\beta_F$, $n_F$ | resolution control function of self-adaptive turbulence eddy simulation (SATES), its integral, cut-off and Kolmogorov lengths and constants (not the SST $\beta^*$) | hybrid RANS/LES, 30P30N high-lift airfoil |
| $c_k$, $c_\varepsilon$ | constants of one-equation subgrid kinetic-energy models (not the DES length factor $C_k$) | one-equation subgrid kinetic-energy models |
| $C_k$, $\mathcal A(\cdot)$ | DES length-scale factor $C_{\mathrm{DES}}=C_kC_s$ of the dynamic RSM-IDDES; volume-weighted average over a cell's direct neighbours | detached-eddy simulation, dynamic procedure, Reynolds-stress model |
| $\nu^{\mathrm{RNG}}_t$, $C_\nu$ | RNG spectral eddy viscosity of the subgrid equation and its constant | spectral eddy viscosity, subgrid velocity enrichment |
| $\mathcal T_{ij}$, $\mathcal T^{\mathrm{eq}}_{ij}$, $t_r$ | subgrid inertial stress of pseudo-DNS, its database equilibrium value, relaxation time | pseudo-direct numerical simulation |
| $\tau^{\mathrm{num}}_{ij}$, $\tau^{\mathrm{mod}}_{ij}$ | numerical and modelled parts of the subgrid stress | implicit LES, numerical dissipation |
| $\alpha_{\mathrm W}$, $b_{\mathrm W}$, $\epsilon_{\mathrm Z}$ | nonlinear and linear weights of weighted compact nonlinear schemes; WENO-Z-type regularization parameter | weighted compact nonlinear schemes, WENO schemes, 30P30N high-lift airfoil |
| $\phi_{\mathrm n}$, $\mathsf b_k$, $g_k$, $\lambda_{\mathrm R}$ | normalized variable, blending weights and dissipation parameters of the ROUND reconstruction | WENO schemes, numerical dissipation |
| $k_s$, $k_g$, $\Delta U^+$ | equivalent sand-grain and geometric roughness heights; roughness function | law of the wall, RANS wall functions, turbulent boundary layer |
| $\alpha_{\mathrm G}$, $g^{L_1L_2}$ | gradient-model filter-moment coefficient and the coefficients of the spatial gradient model (not the basis-tensor $g^{(n)}$) | gradient model |
| $\eta_{\mathrm{DA}}$ | fraction of data-assimilation samples in training | field inversion and machine learning |
| $\lambda^b_i$, $C_{1c}$, $C_{2c}$, $C_{3c}$, $X_{ic}$ | eigenvalues of the anisotropy tensor $b_{ij}$; barycentric weights of the one-, two- and three-component limiting states; vertex coordinates of the barycentric map | barycentric anisotropy map |
| $\delta_{\mathrm G}$, $a_{\mathrm D}$, $b_{\mathrm D}$ | radius of Germano's differential filter; coefficients of the explicit differential filter of Najafiyazdi et al. | explicit modal filtering, scale-similarity model, large-eddy simulation |
| $\delta^{*,\mathrm{sgs}}_\nu$ | semi-local viscous length with the SGS viscosity added to the molecular one | compressible velocity transformations, numerical dissipation, large-eddy simulation |
| $s_{\mathrm{RA}}$, $b_{\mathrm{wk}}$ | Reynolds-analogy factor; wake coefficient of the outer-layer velocity law | Morkovin's hypothesis, compressible velocity transformations, inflow turbulence generation, law of the wall |
| $F_{\mathrm{DES}}$, $F_{\mathrm{DDES}}$, $d_{\mathrm{DDES}}$, $f_d$, $r_d$ | length-scale switch functions and DDES length of SST-based DES/DDES; DDES shielding function and its argument | detached-eddy simulation, $k$-$\omega$ SST, ANSYS Fluent |
| $\alpha_{\mathrm T}$, $k_h$, $\omega_{\mathrm f}$ | upwinding parameter of flux reconstruction ($\lambda_{\mathrm{up}}=1-2\alpha_{\mathrm T}$); numerical wavenumber and frequency of eigensolution analysis | eigensolution analysis, flux reconstruction, spectral difference method |
| $C_{\mathrm{KX}}$ | threshold of the KXRCF troubled-cell indicator (not the DES factor $C_k$) | shock sensors, flux reconstruction |
| $\tau^{\mathrm{sh}}$ | total shear stress in the Renard–Deck skin-friction decomposition | skin-friction decomposition |
| $\psi_H$, $\varphi_{\mathrm L}$, $\alpha_{\mathrm{EB}}$ | dissipation factor of the scale-resolving hybrid (hybrid temporal LES); reduced-stress function and elliptic-blending variable of the Lag EB $k$-$\varepsilon$ model | hybrid RANS/LES, detached-eddy simulation, $k$-$\varepsilon$ models, circular-cylinder wake |
| $\Xi_\Delta$, $\Omega_{\mathrm{fs}}$ | subgrid flame-wrinkling factor; flame sensor of the dynamically thickened flame | thickened flame model, flamelet-based tabulated chemistry |

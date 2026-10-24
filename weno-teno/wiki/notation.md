---
type: Definition
title: "Notation registry"
description: "Normative symbol registry — every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-10-23T11:06:00Z
---

# Notation registry

Every concept page of this bundle writes mathematics in the symbols below.
A source's own symbols are translated on its Source page (`# Notation map`).
The registry was seeded on 2026-10-21 from the first chunk: the TENO review,
the WENO-Z, Z+, ZN, affine-invariant and alternative-WENO papers, the
compact-stencil (ROUND) papers, central-upwind schemes, entropy-stable DG
and subcell limiting, geometric quasilinearization and cell-average
decomposition, OEDG and Active Flux. It follows the Jiang–Shu and
Shu–Osher conventions for reconstruction and the summation-by-parts
conventions for DG, because most sources do. Extend this registry, and
log the extension, before writing a symbol it lacks.

**Clashes kept on purpose.** A few letters carry two meanings in
well-separated families; the family is always clear from the subscript or
the page, and a page that needs both meanings renames one locally and says
so: $\alpha$ (unnormalized weights $\alpha_k$ carry a stencil subscript;
the DG–FV blending coefficient $\alpha$ of subcell limiting has none),
$\gamma$ (ratio of specific heats; the TENO scale-separated measure
$\gamma_k$ always carries a stencil subscript), $q$ (the exponent of
nonlinear weights; never the entropy flux, which is $F_\eta$), $r$ (the
number of points of a classical WENO candidate stencil; the slope ratio
$r_i$ of TVD limiters carries a cell subscript), $N$ (the DG polynomial
degree; grid sizes are written $N_x$, $N_x\times N_y$). $L$ is the
left-eigenvector matrix $R^{-1}$, never the semi-discrete operator, which
is $\mathcal L$.

## 1. Conservation law

| Symbol | Meaning | Note |
|---|---|---|
| $\partial_tu+\partial_xf(u)=0$ | one-dimensional conservation law | $u\in\mathbb R^m$ for a system of $m$ equations; vectors are not bold |
| $\partial_tu+\sum_d\partial_{x_d}f^{(d)}(u)=0$ | multi-dimensional law, flux $f^{(d)}$ in direction $d$ | in 2D also $f^{(1)}=f$, $f^{(2)}=g$ when a page says so |
| $A(u)=\partial f/\partial u$ | flux Jacobian | $A^{(d)}$ in direction $d$ |
| $\lambda_l(u)$, $l=1,\dots,m$ | eigenvalues of $A$, ordered $\lambda_1\le\dots\le\lambda_m$ | |
| $R$, $L=R^{-1}$ | right- and left-eigenvector matrices | evaluated at an interface average, $R_{i+1/2}$ (Roe or arithmetic, stated per page) |
| $a$ | maximum wave speed, $a=\max_l\lvert\lambda_l\rvert$ | local (per interface, $a_{i+1/2}$) or global; sources' $\alpha$, $\lambda_{\max}$ |
| $G$ | admissible set (invariant region) of states | e.g. $\{\rho>0,\ p>0\}$; convex unless a page says otherwise |
| $S(u)$ | source term of a balance law $\partial_tu+\partial_xf(u)=S(u)$ | |

## 2. Grid, time step and semi-discretization

| Symbol | Meaning | Note |
|---|---|---|
| $x_i$, $\Delta x$ | grid points (finite difference) or cell centres (finite volume), uniform spacing | $x_{i+1/2}=x_i+\Delta x/2$ the interfaces; 2D indices $(i,j)$ with $\Delta y$ |
| $I_i=[x_{i-1/2},x_{i+1/2}]$ | cell $i$ | element of a DG mesh also $K$ |
| $u_i$ | point value $u(x_i)$ | finite-difference unknown |
| $\bar u_i=\frac1{\Delta x}\int_{I_i}u\,dx$ | cell average | finite-volume and DG unknown |
| $u^-_{i+1/2}$, $u^+_{i+1/2}$ | left state (from cell $i$) and right state (from cell $i+1$) at $x_{i+1/2}$ | sources' $u^L$, $u^R$; Wu–Shu-type traces $u^\pm$ inside a cell are translated to this convention |
| $\hat f_{i+1/2}$ | numerical flux at $x_{i+1/2}$ | |
| $\frac{d}{dt}u_i=-\frac1{\Delta x}\big(\hat f_{i+1/2}-\hat f_{i-1/2}\big)$ | conservative semi-discrete scheme | $\bar u_i$ in place of $u_i$ for finite volumes |
| $\mathcal L$ | semi-discrete spatial operator, $\frac{d}{dt}u=\mathcal L(u)$ | |
| $t^n$, $\Delta t$, $u^n$ | time levels and step | |
| $\nu$ | CFL number, $\nu=a\Delta t/\Delta x$ in 1D | multi-D definitions stated per page |
| $[\![a]\!]=a^+-a^-$ | jump across an interface | |
| $\{\!\{a\}\!\}=\tfrac12(a^-+a^+)$, $\{\!\{a\}\!\}_{\log}=\dfrac{a^+-a^-}{\ln a^+-\ln a^-}$ | arithmetic and logarithmic means | |
| $\mathbb P^N$ | polynomials of degree at most $N$ | $\mathbb Q^N$ tensor-product degree $N$ |

## 3. Fluxes, splitting and Riemann solvers

| Symbol | Meaning | Note |
|---|---|---|
| $h(u^-,u^+)$ | two-point numerical (surface) flux | monotone in the scalar case; LF, HLL, HLLC, Roe named per page |
| $h^{\mathrm{LF}}=\tfrac12\big(f(u^-)+f(u^+)\big)-\tfrac a2(u^+-u^-)$ | (local) Lax–Friedrichs / Rusanov flux | global LF when $a$ is a domain maximum |
| $f^\pm(u)=\tfrac12\big(f(u)\pm au\big)$ | Lax–Friedrichs flux splitting, $\pm\partial f^\pm/\partial u\ge0$ | finite-difference flux reconstruction acts on $f^+$ and (mirrored) $f^-$ |
| $a^+_{i+1/2}\ge0\ge a^-_{i+1/2}$ | one-sided local speeds of central-upwind schemes | |
| $s^-$, $s^+$ | HLL-type wave-speed estimates | sources' $S_L$, $S_R$ |
| $f^{\mathrm{vol}}(u_j,u_l)$ | symmetric two-point volume flux of flux differencing | |
| $f^{\mathrm{ec}}(u^-,u^+)$ | entropy-conservative two-point flux | |

## 4. Nonlinear reconstruction: ENO, WENO, TENO

| Symbol | Meaning | Note |
|---|---|---|
| $r$ | number of points of each candidate stencil of classical WENO; design order $2r-1$ | $r=3$ is WENO5 |
| $K$ | number of points of the full (TENO) stencil | design order stated per scheme; $K$-point TENO is not always $K$th order |
| $S_k$ | candidate stencil $k$, $k=0,1,\dots$, $S_0$ the most upwind | widths $r_k$ for TENO's incremental stencils; a page whose source numbers stencils differently says so |
| $\hat f^{(k)}_{i+1/2}$ | candidate flux (or value) reconstructed on $S_k$ | $u^{(k)}$ for value reconstruction |
| $d_k$ | linear (ideal, optimal) weights, $\sum_kd_k=1$ | sources' $\gamma_k$, $C_k$, $c_k$ |
| $\beta_k$ | smoothness indicator of $S_k$ | Jiang–Shu form unless a page says otherwise; sources' $IS_k$ |
| $\epsilon$ | regularization of the weights | values per page; never a vortex strength (renamed locally) |
| $q$ | exponent of the nonlinear weights | Jiang–Shu $q=2$; WENO-Z $q=1$ or $2$; TENO $q=6$ |
| $\alpha_k$, $\omega_k$ | unnormalized and normalized nonlinear weights, $\omega_k=\alpha_k/\sum_l\alpha_l$ | TENO's final weights also $\omega_k$ |
| $\tau$ | global smoothness indicator of WENO-Z-type weights | subscript = number of points of the global stencil, $\tau_5=\lvert\beta_0-\beta_2\rvert$; it is not the power of $\Delta x$ it carries ($\tau_7=O(\Delta x^6)$, Li et al. 2022) |
| $\gamma_k$ | TENO scale-separated smoothness measure, $\gamma_k=\big(C+\tau/(\beta_k+\epsilon)\big)^q$ | $C$ the TENO constant |
| $\chi_k=\gamma_k/\sum_l\gamma_l$ | normalized measure | |
| $\delta_k\in\{0,1\}$ | TENO cut-off flag (1 = stencil kept) | |
| $C_T$ | TENO cut-off threshold | |
| $g(\omega)$ | mapping function of mapped WENO | |
| $u^{\mathrm T}(x)$, $\beta_{\mathrm T}$ | THINC hyperbolic-tangent profile and its steepness | $\beta_{\mathrm T}$ never written $\beta$, to keep $\beta_k$ |
| $\tilde u_i$, $\tilde u_{i+1/2}$ | normalized cell average and normalized face value of the normalised-variable diagram | $\tilde u_i=(\bar u_i-\bar u_{i-1})/(\bar u_{i+1}-\bar u_{i-1})$ for a left-biased face |
| $r_i$, $\psi(r_i)$ | slope (gradient) ratio and TVD limiter | |

## 5. Gas dynamics and MHD

| Symbol | Meaning | Note |
|---|---|---|
| $\rho$, $v$, $p$ | density, velocity (vector in multi-D, components $v_1,v_2,v_3$), pressure | sources' $u$ for velocity is translated |
| $E=\frac{p}{\gamma-1}+\tfrac12\rho\lvert v\rvert^2$ | total energy per unit volume | ideal gas |
| $e$, $H$, $c$ | specific internal energy, specific total enthalpy, sound speed $c=\sqrt{\gamma p/\rho}$ | |
| $\gamma$ | ratio of specific heats | sources' $\Gamma$ |
| $u=(\rho,\rho v,E)$ | conserved variables of the Euler equations | |
| $s=\ln(p\rho^{-\gamma})$ | physical specific entropy | |
| $B$, $\psi_{\mathrm{GLM}}$ | magnetic field; divergence-cleaning field of GLM-MHD | |
| $W=(1-\lvert v\rvert^2)^{-1/2}$ | Lorentz factor (relativistic flows, $c=1$) | sources' $\gamma$ |
| $M$, $\mathrm{Re}$, $\mathrm{Pr}$ | Mach, Reynolds and Prandtl numbers | $M$ never a matrix on gas-dynamics pages |

## 6. Entropy and kinetic energy

| Symbol | Meaning | Note |
|---|---|---|
| $\eta(u)$, $F_\eta(u)$ | convex (mathematical) entropy and its entropy flux, $F_\eta'=\eta'f'$ | sources' $(U,F)$, $(\eta,q)$; for Euler $\eta=-\rho s/(\gamma-1)$ unless a page says otherwise |
| $w=\eta'(u)$ | entropy variables | |
| $\psi=w\cdot f(u)-F_\eta(u)$ | entropy flux potential | |
| $[\![w]\!]\cdot f^{\mathrm{ec}}=[\![\psi]\!]$ | Tadmor's entropy-conservation condition | |
| $\kappa=\tfrac12\rho\lvert v\rvert^2$ | kinetic energy per unit volume | |

## 7. Discontinuous Galerkin and summation-by-parts operators

| Symbol | Meaning | Note |
|---|---|---|
| $N$ | DG polynomial degree; design order $N+1$ | sources' $k$, $p$, $K$ |
| $u_h$ | DG solution, $u_h\vert_K\in\mathbb P^N$ | |
| $\xi_j$, $\mathsf w_j$, $j=0,\dots,N$ | reference nodes and quadrature weights (Legendre–Gauss–Lobatto unless a page says Gauss) | sources' $\omega_j$; $\mathsf w$ keeps $\omega_k$ for WENO weights |
| $M=\mathrm{diag}(\mathsf w_j)$, $D$ | mass (norm) matrix and nodal differentiation matrix | |
| $Q=MD$, $B=\mathrm{diag}(-1,0,\dots,0,1)$ | SBP stiffness and boundary matrices | |
| $Q+Q^\top=B$ | summation-by-parts property | |
| $J$, $Ja^{(d)}$ | Jacobian of the element map and contravariant metric terms | |
| $\alpha$ | DG–finite-volume blending coefficient of subcell limiting, $0$ = pure DG, $1$ = pure FV | |
| $\theta$ | scaling factor of a Zhang–Shu-type limiter, $\tilde u_h=\theta(u_h-\bar u)+\bar u$ | $0\le\theta\le1$ |

## 8. Bound preservation

| Symbol | Meaning | Note |
|---|---|---|
| $G$ | admissible set (§1) | |
| $g_i(u)$ | constraint functions, $G=\{u:g_i(u)>0\}$ | |
| $u_*$, $n_*$ | free auxiliary state and normal of the geometric quasilinearization | |
| $\varpi$ | boundary weight of a cell-average decomposition | the bound-preserving CFL condition is proportional to it |
| $\nu_{\mathrm{BP}}$ | bound-preserving CFL number | definition stated per page |

## 9. Spectral analysis

| Symbol | Meaning | Note |
|---|---|---|
| $\vartheta=k_w\Delta x$ | reduced wavenumber, $k_w$ the wavenumber | sources' $\xi$, $w$, $\varphi$ |
| $\tilde\vartheta(\vartheta)=\tilde\vartheta_r+\mathrm i\,\tilde\vartheta_i$ | modified wavenumber; dispersion (real part) and dissipation (imaginary part) | sign of $\tilde\vartheta_i$ stated per page (dissipative for $\tilde\vartheta_i\le0$ in the convention of Fu 2023) |

## 10. Shared page-local symbols

Symbols of a single method family, used on more than one page with the same
meaning. They are page-local in the sense of §§1–9 (each page still defines
them where it uses them), and listed here so that every page of the family
uses the same letter.

| Symbol | Meaning | Pages |
|---|---|---|
| $\sigma$, $\mu$ | scaling and translation of an affine map $u\mapsto\sigma u+\mu$ | affine-invariant WENO, scale invariance, ENO property |
| $\mathsf m$ | descaler of affine-invariant weights | affine-invariant WENO, WENO-JS, scale invariance |
| $\langle f\rangle$ | stencil mean | affine-invariant WENO |
| $\Delta^mf_i$ | $m$-th undivided difference centred at $x_i$ | WENO-ZN, troubled-cell indicators |
| $\Theta$, $C_\Theta$ | WENO-ZN adaptive term and its constant | WENO-ZN (the adaptive-diffusion central-upwind flux uses its own page-local $\Theta$) |
| $z_k$, $\zeta$, $\mu$ | WENO-Z+ ratio terms and the WENO-Z+M coefficient | WENO-Z+ |
| $\mu_d$, $\sigma_i$, $b$, $b_1$, $b_2$, $\xi_{\mathrm A}$ | TENO-A discontinuity measure, its mapping and constants | adaptive TENO, troubled-cell indicators |
| $x^c_i$, $\varsigma$, $\mathcal T$, $\mathcal A$ | THINC jump centre, normalized position of the cell average in the jump $\varsigma=(\bar u_i-f_{\mathrm m})/f_{\mathrm j}$, and profile parameters | THINC, TENO-THINC, symmetry preservation |
| $\varsigma$ (learned weights) | WENO3-NN resolvedness indicator; no page uses it together with the THINC $\varsigma$ | learned WENO weights, smoothness indicators |
| $\varrho_K$, $\varrho^{(d)}_K$ | exponential modal decay rate of a DG solution in element $K$ (Basile et al.; per direction $d$, Mossier et al.) | hp-adaptation, troubled-cell indicators, smoothness indicators |
| $\mathfrak a_K$ | algebraic modal decay exponent predicted by Yu et al.'s network | artificial viscosity, hp-adaptation, troubled-cell indicators |
| $N_{\mathrm{GL}}$ | number of Gauss–Lobatto points of a cell-average decomposition, endpoint weight $1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$ | optimal cell-average decomposition, bound preservation, positivity-preserving Navier–Stokes flux, SSP Runge–Kutta |
| $a^{\mathrm{NS}}$ | Lax–Friedrichs coefficient of a positivity-preserving viscous (Navier–Stokes) flux | positivity-preserving Navier–Stokes flux, bound preservation, optimal cell-average decomposition |
| $\vartheta_{\mathrm{ESW}}$, $\mathsf D_p$, $\varepsilon_{\mathrm s}$ | effective scaled wavenumber of a scale sensor, its $p$-th difference operator and regularization | scale sensors, adaptive TENO, MDCD schemes, hybrid WENO |
| $c_{\mathrm{disp}}$, $c_{\mathrm{diss}}$ | dispersion and dissipation parameters of MDCD schemes | MDCD schemes, approximate dispersion relation, numerical dissipation |
| $\mathcal R$, $\mu_0$, $\mu_1$ | normalised reconstruction operator, intercept and slope of a linear one | normalised-variable diagram, ROUND, numerical dissipation |
| $u^{\mathrm{HLL}}$ | HLL intermediate state | HLL solvers, central-upwind, fluctuation-form FD-WENO |
| $\mathcal C(u)$ | matrix of the non-conservative product $\mathcal C(u)\partial_xu$ | fluctuation-form FD-WENO, HLL solvers |
| $\zeta$, $\bar\zeta_k$ | local characteristic variables $L_{i+1/2}u$ | characteristic decomposition, LCD central-upwind |
| $\mathcal P$, $\mathcal M$, $\mathcal Q$ | diagonal weights of the central-upwind numerical diffusion | central-upwind, LCD central-upwind |
| $\varsigma_e$, $\mathsf q$, $\mu_e$ | Kuzmin–Vedral blending factor, sensor exponent, element viscosity | WENO-stabilized continuous finite elements, artificial viscosity, troubled-cell indicators |
| $\varkappa$ | directional anisotropy of a cell-average decomposition, $\in[-1,1]$ | optimal cell-average decomposition, Zhang–Shu limiter |
| $c_0$ | CFL constant of the first-order bound-preserving scheme | optimal cell-average decomposition, bound preservation |
| $\zeta_{i*}$, $\varphi_i$ | GQL auxiliary variables and affine constraint function | geometric quasilinearization, divergence-free magnetic field |
| $\sigma^m_i$ | OEDG damping coefficient of mode $m$ in cell $i$ | OEDG, artificial viscosity |
| $\mathcal T$, $V$, $\mathcal C$, $\mu_\bullet$ | periodic shift, control volumes, convective matrix and split weights of Coppola & Veldman | split convective forms, kinetic energy preservation, local conservation |
| $\mathcal E$ | vortex strength | isentropic vortex, shock–vortex interaction |
| $\phi_k$, $\rho_k$, $Y_k$ | volume fraction, phase density and mass fraction of phase or component $k$ | five-equation model, stiffened-gas equation of state, multicomponent Euler equations, shock–water column, gas–liquid Riemann problems |
| $p_{\infty,k}$ | stiffened-gas constant of phase $k$, $p_k=(\gamma_k-1)\rho_ke_k-\gamma_kp_{\infty,k}$ | stiffened-gas equation of state, multiphase benchmarks |
| $u_{\mathrm e}$, $\delta u=u-u_{\mathrm e}$ | reference equilibrium state and deviation from it | well-balancing, unstaggered central schemes, TVD |
| $\beta_{\mathrm{ms}}$ | multiscale exponent of the stiff scaling $\varepsilon^{\beta_{\mathrm{ms}}}$ | asymptotic preservation, well-balancing |
| $\Xi_i$ | Sciacovelli et al.'s product shock sensor | troubled-cell indicators, artificial viscosity, numerical dissipation |
| $\varphi_{\mathrm D}$ | Zheng et al.'s discontinuity indicator | troubled-cell indicators, level-set methods, alternative WENO |
| $\bar u^{(1)}_i$ | first normalized moment of $u$ on $I_i$ (Hermite WENO) | Hermite WENO, multi-resolution WENO |
| $\tau^{\mathrm{ref}}_5$ | Wong et al.'s TENO reference indicator (not the registry's $\tau_5$) | smoothness indicators, TENO, WENO-Z, critical points |
| $P_{\mathrm{opt}}$, $P_k$ | optimal (central) and candidate polynomials of CWENO-type reconstructions | CWENO, semi-Lagrangian finite volumes |
| $W_j$ | least-squares row weights of WLS-ENO | WLS-ENO, ENO property |
| $\ell_j$ | Lagrange basis polynomial of node $\xi_j$ | DGSEM, subcell limiting |
| $\beta_{\mathrm p}$ | plasma beta $2p/\lvert B\rvert^2$ | MHD blast wave, high-Mach jets |
| $r_{\mathrm{RK}}$ | order of a Runge–Kutta method | discontinuous Galerkin, OEDG |
| $\Phi_{\mathrm D}$, $\Psi_{\mathrm D}$, $\Psi^*$, $\epsilon_{\mathrm D}$ | classical Ducros ratio, modified (compression-only, non-squared) Ducros sensor, its switching threshold, regularization | Ducros shock sensor, hybrid WENO, wall-modelled LES, URANOS |
| $\alpha_{\mathrm D}$, $\beta_{\mathrm D}$ | α-damping coefficient and curvature coefficient of the interface velocity states in the viscous flux of gradient-based schemes | α-damping viscous flux, gradient-based reconstruction |
| $\lambda_{\mathrm s}$ | scaling $\lambda_{\mathrm s}^{n-1}$ of the $n$-th derivative in Qin et al.'s smoothness indicators | smoothness indicators, multi-resolution WENO, shock-capturing boundary closure |
| $\eta_{\mathrm Z}$, $\xi_{\mathrm Z}$ | dispersion and dissipation parameters of Zhou et al.'s optimized WCNS interpolation ($c_{\mathrm{disp}}=\tfrac{64}{45}\eta_{\mathrm Z}$, $c_{\mathrm{diss}}=\tfrac{64}{45}\xi_{\mathrm Z}$) | weighted compact nonlinear schemes, MDCD schemes, approximate dispersion relation, numerical dissipation |
| $\mathsf G=1/(\gamma-1)$, $\mathsf G_k$, $\mathsf A$, $\bar W$, $\mathsf w^\pm$ | inverse of $\gamma-1$ (per component), stiffened-gas coefficient $\gamma p_\infty/(\gamma-1)$, mixture molar mass and Fujiwara et al.'s interface weights | multicomponent Euler equations, stiffened-gas equation of state, pressure-equilibrium preservation, split convective forms, double-flux method |
| $K$, $\mathcal G$ (flux globalization) | global flux $K=f-\mathcal G$ and the integral $\mathcal G$ of the source term; no page uses it together with the amplification factor $\mathcal G$ | flux globalization, central-upwind, path-conservative, well-balancing, shallow-water equations |
| $\mathcal G$, $\delta_\nu$ (spectral) | fully discrete Runge–Kutta amplification factor and total dispersion error | approximate dispersion relation, MDCD schemes |
| $\check u^\pm$, $\mathsf E$, $\mathsf M$ | modified interface states and the equilibrium variables of moving-equilibrium well-balancing | flux globalization, central-upwind, path-conservative, well-balancing |
| $\dot m$, $\sigma_{\mathrm{st}}$, $\kappa_{\mathrm c}$, $s_{\mathrm p}$ | interfacial mass flux, surface-tension coefficient, curvature (of an interface or of an immersed boundary) and interface speed | Riemann solvers with phase change, level-set methods, Rankine–Hugoniot condition, local conservation |
| $\{\!\{a\}\!\}_{\mathrm G}$, $\{\!\{a\}\!\}_{\mathrm H}$, $\mathsf j_a$, $N_{\mathrm T}$ | geometric and harmonic means, relative jump, truncation order of De Michele & Coppola's asymptotic means | entropy-conservative fluxes, logarithmic mean, pressure-equilibrium preservation |
| $\{\!\{\cdot\}\!\}_{\exp,k}$, $\{\!\{\cdot\}\!\}_{\ln\exp,k}$, $T^{\mathrm v}_k$ | Peyvan et al.'s exponential means and vibrational temperature of species $k$ | entropy-conservative fluxes, logarithmic mean, multicomponent Euler equations |
| $\beta^{\mathrm{IMP}}_k$, $\tau^{\mathrm{IMP}}$, $\xi_{\mathrm{NS}}$ | IMWENO-P smoothness indicators, global indicator and WENO-NS parameter (Zhong et al.) | smoothness indicators, critical-point accuracy, WENO-Z, scale invariance |
| $\lambda_{\mathrm E}$, $\theta_{\mathrm E}$ | parameter and argument of Chen & Deng's exponential weights | exponential nonlinear weights, WCNS, critical-point accuracy, scale invariance |
| $\tau_{\mathrm{AZ}}$ | TENO-AZ adaptive cut-off factor (Tang) | adaptive TENO, critical-point accuracy, smoothness indicators |
| $\beta^{\mathrm{abs}}_k$, $\varsigma_k$, $\varsigma^s$ | Nogueira et al.'s absolute-difference indicators and the network's per-stencil and summed outputs | learned WENO weights, smoothness indicators |
| $s_{\mathrm{mix}}$, $\epsilon_{\mathrm{tol}}$, $\mathcal S_K$ | mixture entropy, entropy-filter tolerance and filter switch of Trojak & Dzanic | entropy filtering, multicomponent Euler equations |
| $\mathcal E(h)$ (shallow water) | hydrostatic (enthalpy-like) potential of the depth in the equilibrium variables of Goudon & Minjeaud; no page uses it together with the vortex strength $\mathcal E$ | well-balancing, flow over a bump, shallow-water equations, operator splitting |
| $N_\phi$ | number of phases | phase-field methods, discrete equations method, bound preservation |
| $W_k$, $\epsilon_k$, $\Omega_k$ | molar mass, molar internal energy and mass production rate of species $k$ | multicomponent Euler equations, operator splitting |
| $\mathfrak q$ | electric charge density $\nabla\cdot\mathcal E$ (or $\nabla\cdot\mathfrak E$) of resistive relativistic MHD | relativistic hydrodynamics, cell-average to point-value conversion, magnetized vortex |
| $\eta_{\mathrm m}$ | magnetic resistivity (not the entropy $\eta$) | constrained transport, HLL solvers, IMEX Runge–Kutta, numerical dissipation, relativistic hydrodynamics, tearing-mode instability |
| $w_{\mathrm h}$ | relativistic enthalpy density $\rho h$ (not the entropy variables $w$) | force-free splitting, MHD blast wave, tearing-mode instability |
| $a^\nu$ | Lax–Friedrichs coefficient applied to the viscous flux alone (Ching et al.), as opposed to the total-flux $a^{\mathrm{NS}}$ | positivity-preserving Navier–Stokes flux, optimal cell-average decomposition |
| $\psi^{\mathrm{SBM}}$, $\beta$, $\tau_{\mathrm S}$ | SBM slope limiter of Chu et al. and its two parameters | total variation diminishing, low-dissipation central-upwind schemes, numerical dissipation |
| $\mathcal W_{i+1/2}$, $C_{\mathrm W}$, $\alpha_{\mathrm W}$ | weak local residual of Chu et al. (2025a), its constant and contact exponent | low-dissipation central-upwind schemes, troubled-cell indicators |
| $Q_{\mathrm h}$, $V_f$ | hybridized SBP operator and face interpolation matrix | summation-by-parts operators, flux differencing |
| $\tau_{\mathrm{ZQ}}$ | global indicator of the scale-invariant Zhu–Qiu weights (Fan et al. 2025a) | scale invariance |
| $\mathsf b$ | buoyancy of thermal rotating shallow water | dam-break problems, hydrostatic equilibrium tests |
| $\phi_{\mathrm G}$ | Godunov potential of the MHD Powell term in the modified Tadmor condition | Godunov–Powell source term, entropy-conservative fluxes, flux differencing |
| $\kappa_{\mathrm s}$, $\varphi_{\mathrm J}$ | strength and Jameson pressure factor of Duan et al.'s shock sensor $\exp(-\kappa_{\mathrm s}\varphi_{\mathrm J}\Psi_{\mathrm D})$; other pages (asymptotic preservation, pressure equilibrium, carbuncle) use $\kappa_{\mathrm s}$ for unrelated page-local quantities and never with this sensor | troubled-cell indicators, Ducros shock sensor, double Mach reflection, forward-facing step, Leblanc tube, Sedov, 2D Riemann problems, high-Mach jets, Woodward–Colella, steady shock problems |
| $\varepsilon_{\mathrm s}$ (shock position) | Ren et al.'s sub-cell position of a steady shock in matrix stability analyses; no page uses it together with the scale-sensor regularization $\varepsilon_{\mathrm s}$ | carbuncle phenomenon, matrix stability analysis, steady shock problems |
| $s_{\max}$ | maximum signal speed of a Rusanov-type dissipation (Zampa & Dumbser and others); split convective forms use the same letter for Zampa & Dumbser's dissipation speed | MOOD, artificial viscosity, path-conservative schemes, split convective forms |
| $\lambda_{\mathrm s}$ (RBF) | shape parameter of a Gaussian or multiquadric RBF reconstruction, adaptive in Liang & Fu (2024a) as $\lambda_{\mathrm s}=\lambda_0+\lambda_\Delta(1-\varphi(\mu_d))$; no page uses it together with Qin et al.'s scaling $\lambda_{\mathrm s}$ | RBF-WENO, adaptive TENO |
| $\beta_{\mathrm e}$, $\epsilon_K$ | Lin & Chan's user-defined blending fraction $\beta_{\mathrm e}\in[0,1]$ and elementwise modal smoothness factor $\epsilon_K\in[0,1]$, which relax the cell entropy bound by $1-\beta_{\mathrm e}\epsilon_K$ in the shock-capturing variant of entropy-bounded subcell limiting | subcell limiting, troubled-cell indicators, entropy stability, carbuncle phenomenon, high-Mach jets |
| $n_{\mathrm g}$, $g$ | degree of the nodal-density interpolant of Zuo & Zhu's troubled-cell tests (the sources' $2r$) and the interpolant | troubled-cell indicators, hybrid WENO |
| $\mathcal E$ (MHD) | electric field $\mathcal E=-v\times B$ (plus resistive terms), its edge or $z$ component $\mathcal E_z$ in constrained transport, radial component $\mathcal E_r$; no page uses it together with the vortex strength $\mathcal E$ (relativistic hydrodynamics, which needs both, writes the electric field $\mathfrak E$) | constrained transport, divergence-free magnetic field, GLM divergence cleaning, force-free splitting, HLL solvers, semi-implicit all-Mach scheme, lid-driven cavity, magnetized vortex, tearing-mode instability |
| $\mathcal A$ (MHD) | magnetic vector potential, $B=\nabla\times\mathcal A$; no page uses it together with the THINC parameter $\mathcal A$ (field-loop advection and Kelvin–Helmholtz keep their earlier $\mathsf A$, $\mathsf A_3$) | semi-implicit all-Mach scheme |

$\mathcal T$, $\mathcal C$, $\zeta$ and $\mu$ carry two family meanings
(THINC/shift, non-conservative/convective matrix, Z+/characteristic
variables, Z+M coefficient/affine translation); no page uses both families. $\mathcal G$ is likewise the global part of the flux on flux-globalization pages and the Runge–Kutta amplification factor on spectral pages, and $\mathsf G$ is $1/(\gamma-1)$ on multicomponent pages but Ramani & Shkoller's target map on the moving-mesh pages; no page uses both meanings. The
gravitational potential is written $\phi$ without subscript on well-balancing pages; the
volume fraction always carries its phase index, $\phi_k$. $B$ is also the boundary matrix of $Q+Q^\top=B$ on the SBP pages (summation-by-parts operators, flux differencing); flux differencing uses it in both senses, the magnetic field only inside MHD formulas such as $\phi_{\mathrm G}$. The MUSCL parameter is written $\kappa_{\mathrm M}$ and the minmod
parameter is declared page-local wherever used, to keep $\kappa$ (kinetic energy) and $\theta$
(Zhang–Shu factor) free.

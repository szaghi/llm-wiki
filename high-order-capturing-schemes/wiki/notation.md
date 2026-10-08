---
type: Definition
title: "Notation registry"
description: "Normative symbol registry — every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-10-08T00:00:00Z
---

# Notation registry

This page is **normative** for the bundle. Concept pages must use these symbols
exclusively; each Source page maps its paper's native notation to this registry
in a `# Notation map` section. Extend this registry (and record the extension in
[the log](/log.md)) before writing math that needs a symbol it lacks.

The registry was seeded once, at scaffolding, from the conventions most
common in the literature (Shu's reviews). It is wiki-native law from then on.

## Conservation law

| Symbol | Meaning |
|---|---|
| $u$ | conserved state; $u \in \mathbb{R}^m$ for a system |
| $f(u)$ | physical flux; $\partial_t u + \partial_x f(u) = 0$ in 1D, $\partial_t u + \nabla\cdot \mathbf{f}(u) = 0$ in $d$ dimensions |
| $A(u)$ | flux Jacobian $f'(u)$ |
| $\lambda^{(p)}$, $\Lambda$ | eigenvalues of $A$, $p = 1,\dots,m$; $\Lambda = \mathrm{diag}(\lambda^{(p)})$ |
| $R$, $L$ | right and left eigenvector matrices, $A = R \Lambda L$, $L = R^{-1}$ |
| $\rho$, $\mathbf{v}$, $p$, $E$, $\gamma$ | density, velocity, pressure, total energy density, ratio of specific heats (Euler) |
| $\mathbf{B}$ | magnetic field (MHD) |

## Grid and time

| Symbol | Meaning |
|---|---|
| $x_i$ | cell centre (FV) or grid point (FD) |
| $x_{i+1/2}$ | cell interface |
| $I_i$ | cell $[x_{i-1/2}, x_{i+1/2}]$ |
| $h$ | uniform spacing; $h_i$ on a non-uniform grid; $h_x$, $h_y$, $h_z$ the directional spacings in multi-D (added in batch 3) |
| $t^n$, $\Delta t$ | time level and time step |
| $\nu$ | CFL number, $\nu = \Delta t \max_p |\lambda^{(p)}| / h$ |

## Discrete unknowns and fluxes

| Symbol | Meaning |
|---|---|
| $\bar u_i$ | cell average of $u$ over $I_i$ (finite volume) |
| $u_i$ | point value $u(x_i)$ (finite difference) |
| $u^-_{i+1/2}$, $u^+_{i+1/2}$ | reconstructed interface states from the left and from the right of $x_{i+1/2}$ |
| $\hat f_{i+1/2}$ | numerical flux at $x_{i+1/2}$; conservative semi-discretization $\frac{d}{dt} u_i = -\frac{1}{h}\left(\hat f_{i+1/2} - \hat f_{i-1/2}\right)$ |
| $\mathcal{H}$ | Shu–Osher flux function of the conservative FD form: $f(u(x)) = \frac{1}{h}\int_{x-h/2}^{x+h/2} \mathcal{H}(\xi)\, d\xi$, so $\hat f_{i+1/2}$ approximates $\mathcal{H}(x_{i+1/2})$; its primitive is known at interfaces, $\int^{x_{i+1/2}} \mathcal{H} = h\sum_{j \le i} f(u_j)$ |
| $f^+$, $f^-$ | flux splitting $f = f^+ + f^-$ with $\partial f^+/\partial u \ge 0$, $\partial f^-/\partial u \le 0$ |
| $\alpha$ | Lax–Friedrichs splitting speed, $f^\pm = \frac{1}{2}\left(f \pm \alpha u\right)$, $\alpha \ge \max |\lambda|$ |

## Reconstruction and nonlinear weights

A scheme of design order $2r-1$ combines $r$ candidate stencils of $r$
cells each.

| Symbol | Meaning |
|---|---|
| $r$ | number of candidate stencils, and cells per candidate stencil |
| $S_k$ | candidate stencil $k = 0,\dots,r-1$, ordered left to right (stencil index convention fixed per page) |
| $p_k(x)$ | candidate polynomial of degree $r-1$ on $S_k$ |
| $q_k$ | candidate approximation at the target point (e.g. $p_k(x_{i+1/2})$) |
| $P(x)$ | polynomial on the big stencil $\bigcup_k S_k$, degree $2r-2$ |
| $d_k$ | linear (optimal) weights, $\sum_k d_k = 1$, with $\sum_k d_k q_k$ reproducing the big-stencil value |
| $\beta_k$ | smoothness indicator of $S_k$ |
| $\varepsilon$ | regularization in the nonlinear weights |
| $\tilde\omega_k$ | unnormalized nonlinear weight (e.g. $d_k / (\varepsilon + \beta_k)^{q}$) |
| $q$ | power in the unnormalized weight |
| $\omega_k$ | normalized nonlinear weight, $\omega_k = \tilde\omega_k / \sum_l \tilde\omega_l$; the reconstruction is $\sum_k \omega_k q_k$ |
| $\tau$ | global smoothness indicator of WENO-Z-type weights |

## Time discretization

| Symbol | Meaning |
|---|---|
| $\mathcal{L}(u)$ | spatial operator of the semi-discretization $\frac{d}{dt}u = \mathcal{L}(u)$ |
| $\Delta t_{\mathrm{FE}}$ | step limit under which forward Euler is strongly stable (or positivity-preserving) |
| $\mathcal{C}$ | SSP coefficient: the SSP method is stable for $\Delta t \le \mathcal{C}\, \Delta t_{\mathrm{FE}}$ |
| $s$ | number of Runge–Kutta stages |

## Positivity and admissibility

| Symbol | Meaning |
|---|---|
| $\mathcal{G}$ | admissible set of states (e.g. $\rho > 0$, $p > 0$ for Euler) |
| $\theta$ | scaling or blending parameter of a positivity-preserving limiter, $\theta \in [0,1]$ |

## Primitive functions and divided differences

Added 2026-10-08 (batch 1: harten-1987, shu-1988, shu-1989, shu-1998).

| Symbol | Meaning |
|---|---|
| $\mathcal{U}(x)$ | primitive of the solution, $\mathcal{U}(x) = \int_{x_{1/2}}^{x} u(\xi)\,d\xi$; exactly known at interfaces from cell averages, $\mathcal{U}(x_{i+1/2}) = \sum_{j \le i} h_j \bar u_j$ |
| $w[x_a, \dots, x_b]$ | Newton divided difference of a function $w$ over the listed points |
| $\Delta^{l} w_i$ | $l$-th undivided (forward) difference, $\Delta^{l} w_i = \Delta^{l-1} w_{i+1} - \Delta^{l-1} w_i$, $\Delta^0 w_i = w_i$ (uniform grids) |

## Fluxes and upwinding

| Symbol | Meaning |
|---|---|
| $\hat f(a, b)$ | two-argument monotone flux: Lipschitz, nondecreasing in $a$, nonincreasing in $b$, $\hat f(a,a) = f(a)$; the interface flux is $\hat f_{i+1/2} = \hat f(u^-_{i+1/2}, u^+_{i+1/2})$ |
| $\hat a_{i+1/2}$ | Roe speed, $\hat a_{i+1/2} = (f(u_{i+1}) - f(u_i))/(u_{i+1} - u_i)$ (scalar); for systems the eigenvalues of a Roe or arithmetic-mean Jacobian at $x_{i+1/2}$ |
| $\alpha_{i+1/2}$ | local Lax–Friedrichs speed (the maximum of $\vert f'(u)\vert$ over the states between $u_i$ and $u_{i+1}$, or over the stencil) |
| $\ell^{(p)}$, $r^{(p)}$ | $p$-th left (row) and right (column) eigenvectors of the Jacobian frozen at $x_{i+1/2}$; local characteristic variable $w^{(p)}_j = \ell^{(p)} u_j$ |

## Runge–Kutta in Shu–Osher form

| Symbol | Meaning |
|---|---|
| $u^{(i)}$ | stage value, $u^{(0)} = u^n$, $u^{(s)} = u^{n+1}$ |
| $a_{ik}$, $b_{ik}$ | Shu–Osher coefficients, $u^{(i)} = \sum_{k=0}^{i-1}\left(a_{ik} u^{(k)} + b_{ik}\,\Delta t\,\mathcal{L}(u^{(k)})\right)$, $a_{ik} \ge 0$, $\sum_k a_{ik} = 1$; with all $b_{ik} \ge 0$, $\mathcal{C} = \min_{i,k} a_{ik}/b_{ik}$ |
| $\tilde{\mathcal{L}}$ | downwind ("adjoint") operator: approximates the same derivative as $\mathcal{L}$ but is stable for forward Euler run backward in time; replaces $\mathcal{L}$ where $b_{ik} < 0$ |

## Limiting

| Symbol | Meaning |
|---|---|
| $\operatorname{minmod}(z_1,\dots,z_k)$ | smallest argument in magnitude if all have one sign, else 0 |
| $\operatorname{median}(x,y,z)$ | the argument lying between the other two; $\operatorname{median}(x,y,z) = x + \operatorname{minmod}(y-x, z-x)$ |
| $\delta^2 \bar u_i$ | second difference $\bar u_{i-1} - 2\bar u_i + \bar u_{i+1}$ |
| $\kappa$ | Suresh–Huynh monotonicity constant in $u^{\mathrm{MP}}_{i+1/2} = \bar u_i + \operatorname{minmod}(\bar u_{i+1} - \bar u_i,\ \kappa(\bar u_i - \bar u_{i-1}))$ |
| $u^{\mathrm{or}}_{i+1/2}$ | unlimited ("original") high-order interface value before an MP bound |
| $u^{\mathrm{MD}}$, $u^{\mathrm{LC}}$ | MP auxiliary values: median value and large-curvature value adjoined to enlarge the admissible interval near extrema |
| $u^{\min}$, $u^{\max}$ | ends of the MP admissible interval; the limited value is $\operatorname{median}(u^{\mathrm{or}}, u^{\min}, u^{\max})$ |
| $\mathcal{D}^{\mathrm{M4}}_{i+1/2}$ | interface curvature $\operatorname{minmod}(4\delta^2\bar u_i - \delta^2\bar u_{i+1}, 4\delta^2\bar u_{i+1} - \delta^2\bar u_i, \delta^2\bar u_i, \delta^2\bar u_{i+1})$ |
| $\Delta u_i$, $u_{6,i}$ | PPM parabola in cell $I_i$: jump $u^-_{i+1/2} - u^+_{i-1/2}$ and curvature coefficient $6\left(\bar u_i - \tfrac12(u^+_{i-1/2} + u^-_{i+1/2})\right)$ |
| $\phi_i$ | PPM flattening coefficient, $0 \le \phi_i \le 1$ (1 = fully flattened to $\bar u_i$) |

## Weight families after WENO-JS

Added 2026-10-08 (batch 2: henrick-2005, borges-2008, castro-2011, hu-2010, fu-2016, balsara-2016, zhu-2016, rathan-2017, pirozzoli-2002, martin-2006).

| Symbol | Meaning |
|---|---|
| $n_{\mathrm{cp}}$ | order of a critical point: $f' = \dots = f^{(n_{\mathrm{cp}})} = 0$, $f^{(n_{\mathrm{cp}}+1)} \neq 0$ ($n_{\mathrm{cp}} = 0$: no critical point) |
| $g_k(\omega)$ | Henrick mapping of a weight toward $d_k$ |
| $\tau_{2r-1}$, $\tau_6$ | global (reference) smoothness indicators built from several $\beta_k$ on the whole stencil; $\tau$ when the variant is clear from context |
| $C_w$ | additive constant in weights of the form $\left(C_w + \tau/(\beta_k + \varepsilon)\right)^q$ (WENO-CU6, TENO); $C_w = 1$ with $q = 1$ is WENO-Z |
| $\gamma_k$ | TENO per-stencil smoothness measure $\left(C_w + \tau_K/(\beta_k + \varepsilon)\right)^q$ before normalization (subscripted; distinct from the ratio of specific heats $\gamma$) |
| $\chi_k$, $\delta_k$, $C_T$ | TENO normalized smoothness measure, its 0/1 cutoff, and the cutoff threshold |
| $\gamma_{\mathrm{Hi}}$, $\gamma_{\mathrm{Lo}}$ | WENO-AO parameters setting the linear weights of the large central stencil and of the central small stencil |
| $\vartheta$ | threshold of a hybrid scheme's switch to the capturing scheme |

## Positivity, alternative finite differences and divergence constraints

Added 2026-10-08 (batch 3: gottlieb-2001, titarev-2004, zhang-2010, zhang-2012, hu-2013, guo-2014, christlieb-2016, reyes-2018, balsara-2025, balsara-2026).

| Symbol | Meaning |
|---|---|
| $\rho(u)$, $p(u)$ | density and pressure as functions of the conserved state; $p$ is concave in $u$ wherever $\rho > 0$, which makes $\mathcal{G}$ convex |
| $\epsilon_{\mathcal{G}}$ | positivity floor of a limiter (e.g. $10^{-13}$); distinct from the weight regularization $\varepsilon$ |
| $\nu_0$ | CFL bound under which the first-order scheme with a given flux keeps cell averages in $\mathcal{G}$ |
| $\mathcal{P}_i(x)$, $K$ | the (vector) polynomial of degree $K$ that represents the solution in $I_i$ (FV reconstruction or DG), with cell average $\bar u_i$ |
| $\hat x^{(a)}_i$, $\hat w_a$, $N_{\mathrm{GL}}$ | Gauss–Lobatto points in $I_i$ ($\hat x^{(1)}_i = x_{i-1/2}$, $\hat x^{(N_{\mathrm{GL}})}_i = x_{i+1/2}$) and weights on $[-\tfrac12, \tfrac12]$, $\sum_a \hat w_a = 1$, exact for degree $2N_{\mathrm{GL}} - 3 \ge K$ |
| $\theta_\rho$, $\theta_p$ | scaling factors of the Zhang–Shu limiter for density and pressure (special cases of $\theta$) |
| $\hat f^{\mathrm{LO}}_{i+1/2}$, $\hat f^{\mathrm{HO}}_{i+1/2}$ | first-order (positivity-preserving) and high-order numerical fluxes; a flux limiter uses $\theta_{i+1/2}\hat f^{\mathrm{HO}} + (1-\theta_{i+1/2})\hat f^{\mathrm{LO}}$ |
| $S_L$, $S_R$, $S_M$ | left, right and contact wave-speed estimates of an HLL-type Riemann solver; $S_D$, $S_U$ the transverse pair of a 2D solver |
| $\eta$ | coercivity constant of a linear operator, $\eta = \inf_{\vert u\vert = 1} -\operatorname{Re}\langle \mathcal{L}u, u\rangle / \vert \mathcal{L}u\vert^2$ |
| $\mathcal{F}^n_i$ | time-averaged flux $\frac{1}{\Delta t}\int_{t^n}^{t^{n+1}} f(u(x_i, t))\,dt$ of a single-step (Picard/Taylor) scheme |
| $\boldsymbol{\mathcal{E}}$, $\mathbf{A}$ | electric field (ideal MHD: $\boldsymbol{\mathcal{E}} = -\mathbf{v}\times\mathbf{B}$) and magnetic vector potential, $\mathbf{B} = \nabla\times\mathbf{A}$; $\boldsymbol{\mathcal{E}}$ avoids a clash with the energy $E$ |
| $\bar B_{x;i+1/2,j,k}$ | face average of the normal field component on a Yee-type (staggered) mesh; $\bar{\mathcal{E}}_{z;i+1/2,j+1/2,k}$ the edge average |
| $\mathcal{K}(x, y)$, $\ell$, $R$ | GP covariance kernel, its length hyperparameter, and the GP stencil radius ($2R+1$ cells; $R = r - 1$ for the same stencil as WENO) |
| $\boldsymbol{\mathcal K}$, $\mathbf C$, $\mathbf t_*$, $\mathbf z$, $f_0$ | GP kernel matrix of point values, covariance matrix of cell averages, prediction vector, weights $\mathbf z = \mathbf C^{-1}\mathbf t_*$, constant prior mean |
| $\mu^{(k)}_i$, $\mathbf e^{(k)}_i$, $c^{(k)}_i$ | eigenpairs of $\boldsymbol{\mathcal K}$ on sub-stencil $S_k$, and the coefficients of the point values in that eigenbasis (GP smoothness indicator) |
| $K_{\mathrm{L}}$ | Lipschitz constant in time of a time-dependent linear operator $\mathcal{L}(t)$ |
| $\sigma$ | constant $0 < \sigma < 1$ in the accuracy CFL condition $\nu \le \sigma/2$ of the Hu–Adams–Shu flux limiter |

## Spectral analysis

| Symbol | Meaning |
|---|---|
| $\xi$ | scaled wavenumber $k h$, $0 \le \xi \le \pi$ |
| $\tilde\xi(\xi)$ | modified wavenumber of a scheme for $\partial_x$; $\operatorname{Re}\tilde\xi$ measures dispersion, $\operatorname{Im}\tilde\xi$ dissipation (negative for a dissipative upwind scheme on right-running waves) |

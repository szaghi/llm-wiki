---
type: Definition
title: "Notation registry"
description: "Normative symbol registry — every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-10-13T00:00:00Z
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
| $R$, $L$ | right and left eigenvector matrices, $A = R \Lambda L$, $L = R^{-1}$ (distinct from the GP stencil radius $R$, which is used only on GP pages) |
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
| $p_k(x)$ | candidate polynomial of degree $r-1$ on $S_k$ (degree $K$ in polynomial WENO, degree $k$ in a nested extrapolation; stated on those pages) |
| $q_k$ | candidate approximation at the target point (e.g. $p_k(x_{i+1/2})$) |
| $P(x)$ | polynomial on the big stencil $\bigcup_k S_k$, degree $2r-2$ |
| $d_k$ | linear (optimal) weights, $\sum_k d_k = 1$, with $\sum_k d_k q_k$ reproducing the big-stencil value |
| $\beta_k$ | smoothness indicator of $S_k$ |
| $\varepsilon$ | regularization in the nonlinear weights |
| $\tilde\omega_k$ | unnormalized nonlinear weight (e.g. $d_k / (\varepsilon + \beta_k)^{q}$) |
| $q$ | power in the unnormalized weight (the bare letter; the jump/average notation $[\![q]\!]$, $\{\!\{q\}\!\}$ and the subscript form $q_{\mathrm{Roe}}$ below use $q$ as a generic placeholder, and $q_k$ is the candidate value) |
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
| $\Delta^{l} w_i$ | $l$-th undivided (forward) difference, $\Delta^{l} w_i = \Delta^{l-1} w_{i+1} - \Delta^{l-1} w_i$, $\Delta^0 w_i = w_i$ (uniform grids); the order is always written, $\Delta^1 w_i$ included, since an unsuperscripted $\Delta u_i$ is the PPM jump |

## Fluxes and upwinding

| Symbol | Meaning |
|---|---|
| $\hat f(a, b)$ | two-argument monotone flux: Lipschitz, nondecreasing in $a$, nonincreasing in $b$, $\hat f(a,a) = f(a)$; the interface flux is $\hat f_{i+1/2} = \hat f(u^-_{i+1/2}, u^+_{i+1/2})$ |
| $\hat a_{i+1/2}$ | Roe speed, $\hat a_{i+1/2} = (f(u_{i+1}) - f(u_i))/(u_{i+1} - u_i)$ (scalar); for systems the eigenvalues of a Roe or arithmetic-mean Jacobian at $x_{i+1/2}$ (a speed; the Roe-averaged state quantities themselves are written $q_{\mathrm{Roe}}$, batch 12) |
| $\alpha_{i+1/2}$ | local Lax–Friedrichs speed (the maximum of $\vert f'(u)\vert$ over the states between $u_i$ and $u_{i+1}$, or over the stencil); Riemann-solver pages write the same speed of a Rusanov flux as $S$ (batch 11) |
| $\ell^{(p)}$, $r^{(p)}$ | $p$-th left (row) and right (column) eigenvectors of the Jacobian frozen at $x_{i+1/2}$; local characteristic variable $w^{(p)}_j = \ell^{(p)} u_j$ |

## Runge–Kutta in Shu–Osher form

| Symbol | Meaning |
|---|---|
| $u^{(i)}$ | stage value, $u^{(0)} = u^n$, $u^{(s)} = u^{n+1}$ |
| $a_{ik}$, $b_{ik}$ | Shu–Osher coefficients, $u^{(i)} = \sum_{k=0}^{i-1}\left(a_{ik} u^{(k)} + b_{ik}\,\Delta t\,\mathcal{L}(u^{(k)})\right)$, $a_{ik} \ge 0$, $\sum_k a_{ik} = 1$; with all $b_{ik} \ge 0$, $\min_{i,k} a_{ik}/b_{ik}$ is a lower bound on $\mathcal{C}$, equal to it for an optimal representation (the coefficient belongs to the method; amended 2026-10-12, deep lint) |
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
| $\Delta u_i$, $u_{6,i}$ | PPM parabola in cell $I_i$ (no superscript, so distinct from the undivided difference $\Delta^1 w_i$): jump $u^-_{i+1/2} - u^+_{i-1/2}$ and curvature coefficient $6\left(\bar u_i - \tfrac12(u^+_{i-1/2} + u^-_{i+1/2})\right)$ |
| $\phi_i$ | PPM flattening coefficient, $0 \le \phi_i \le 1$ (1 = fully flattened to $\bar u_i$) |

## Weight families after WENO-JS

Added 2026-10-08 (batch 2: henrick-2005, borges-2008, castro-2011, hu-2010, fu-2016, balsara-2016, zhu-2016, rathan-2017, pirozzoli-2002, martin-2006).

| Symbol | Meaning |
|---|---|
| $n_{\mathrm{cp}}$ | order of a critical point: $f' = \dots = f^{(n_{\mathrm{cp}})} = 0$, $f^{(n_{\mathrm{cp}}+1)} \neq 0$ ($n_{\mathrm{cp}} = 0$: no critical point) |
| $g_k(\omega)$ | Henrick mapping of a weight toward $d_k$ |
| $\tau_{2r-1}$, $\tau_6$ | global (reference) smoothness indicators built from several $\beta_k$ on the whole stencil; $\tau$ when the variant is clear from context |
| $C_w$ | additive constant in weights of the form $\left(C_w + \tau/(\beta_k + \varepsilon)\right)^q$ (WENO-CU6, TENO); $C_w = 1$ with $q = 1$ is WENO-Z |
| $\gamma_k$ | TENO per-stencil smoothness measure $\left(C_w + \tau_K/(\beta_k + \varepsilon)\right)^q$ before normalization (subscripted; distinct from the ratio of specific heats $\gamma$); $\tau_K$ is Fu et al.'s global indicator over the full stencil of $K$ points, a member of the $\tau_{2r-1}$, $\tau_6$ family above: here $K$ counts points, distinct from the polynomial degree $K$ (batch 3) |
| $\chi_k$, $\delta_k$, $C_T$ | TENO normalized smoothness measure, its 0/1 cutoff, and the cutoff threshold (distinct from the DMP floor $\delta_0$, batch 4, and the HLLEM coefficient $\delta_p$) |
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
| $\hat x^{(a)}_i$, $\hat w_a$, $N_{\mathrm{GL}}$ | Gauss–Lobatto points in $I_i$ ($\hat x^{(1)}_i = x_{i-1/2}$, $\hat x^{(N_{\mathrm{GL}})}_i = x_{i+1/2}$) and weights on $[-\tfrac12, \tfrac12]$, $\sum_a \hat w_a = 1$, exact for degree $2N_{\mathrm{GL}} - 3 \ge K$ (the points of a positivity limiter; general quadrature points, e.g. of a DG moment projection, are $x_G$, $w_G$, batch 4) |
| $\theta_\rho$, $\theta_p$ | scaling factors of the Zhang–Shu limiter for density and pressure (special cases of $\theta$) |
| $\hat f^{\mathrm{LO}}_{i+1/2}$, $\hat f^{\mathrm{HO}}_{i+1/2}$ | first-order (positivity-preserving) and high-order numerical fluxes; a flux limiter uses $\theta_{i+1/2}\hat f^{\mathrm{HO}} + (1-\theta_{i+1/2})\hat f^{\mathrm{LO}}$ |
| $S_L$, $S_R$, $S_M$ | left, right and contact wave-speed estimates of an HLL-type Riemann solver; $S_D$, $S_U$ the transverse pair of a 2D solver |
| $\eta$ | coercivity constant of a linear operator, $\eta = \inf_{\vert u\vert = 1} -\operatorname{Re}\langle \mathcal{L}u, u\rangle / \vert \mathcal{L}u\vert^2$ |
| $\mathcal{F}^n_i$ | time-averaged flux $\frac{1}{\Delta t}\int_{t^n}^{t^{n+1}} f(u(x_i, t))\,dt$ of a single-step (Picard/Taylor) scheme |
| $\boldsymbol{\mathcal{E}}$, $\mathbf{A}$ | electric field (ideal MHD: $\boldsymbol{\mathcal{E}} = -\mathbf{v}\times\mathbf{B}$) and magnetic vector potential, $\mathbf{B} = \nabla\times\mathbf{A}$; $\boldsymbol{\mathcal{E}}$ avoids a clash with the energy $E$ |
| $\bar B_{x;i+1/2,j,k}$ | face average of the normal field component on a Yee-type (staggered) mesh; $\bar{\mathcal{E}}_{z;i+1/2,j+1/2,k}$ the edge average |
| $\mathcal{K}(x, y)$, $\ell$, $\Sigma^2$, $R$ | GP covariance kernel, its length hyperparameter, its amplitude (signal variance), and the GP stencil radius ($2R+1$ cells; $R = r - 1$ for the same stencil as WENO; distinct from the eigenvector matrix $R$, which GP pages do not use) |
| $\boldsymbol{\mathcal K}$, $\mathbf C$, $\mathbf t_*$, $\mathbf z$, $f_0$ | GP kernel matrix of point values, covariance matrix of cell averages, prediction vector, weights $\mathbf z = \mathbf C^{-1}\mathbf t_*$, constant prior mean |
| $\mu^{(k)}_i$, $\mathbf e^{(k)}_i$, $c^{(k)}_i$ | eigenpairs of $\boldsymbol{\mathcal K}$ on sub-stencil $S_k$, and the coefficients of the point values in that eigenbasis (GP smoothness indicator) |
| $K_{\mathrm{L}}$ | Lipschitz constant in time of a time-dependent linear operator $\mathcal{L}(t)$ |
| $\sigma$ | constant $0 < \sigma < 1$ in the accuracy CFL condition $\nu \le \sigma/2$ of the Hu–Adams–Shu flux limiter |

## One-step schemes, DG limiting, AMR and numerical boundaries

Added 2026-10-08 (batch 4: qiu-2005, dumbser-2007, balsara-2009, dumbser-2013, dumbser-2014, zanotti-2015, fisher-2011, baeza-2016, li-2016, lu-2016).

| Symbol | Meaning |
|---|---|
| $\zeta$ | local cell coordinate $\zeta = (x - x_i)/h \in [-\tfrac12, \tfrac12]$ (distinct from the scaled wavenumber $\xi$) |
| $P_l(\zeta)$ | Legendre polynomials scaled to $[-\tfrac12, \tfrac12]$: $P_0 = 1$, $P_1 = \zeta$, $P_2 = \zeta^2 - \tfrac1{12}$, $P_3 = \zeta^3 - \tfrac{3}{20}\zeta$ |
| $\hat u^{(l)}_i$ | modal coefficient (moment) of the cell polynomial, $\mathcal{P}_i = \sum_{l=0}^{K} \hat u^{(l)}_i P_l(\zeta)$, $\hat u^{(0)}_i = \bar u_i$; in multi-D, products $P_l P_m$ with coefficients $\hat u^{(lm)}_i$ |
| $d_{\mathrm c}$ | unnormalized linear weight of the central stencil in polynomial (Dumbser–Käser) WENO, where every one-sided stencil has linear weight 1 |
| $u^{\mathrm p}_i(x,t)$ | element-local space–time predictor polynomial on $I_i \times [t^n, t^{n+1}]$ (ADER) |
| $\mathcal{B}_i$ | troubled-cell flag (limiter status), $\mathcal{B}_i \in \{0, 1\}$ |
| $N_{\mathrm s}$, $\bar v_{i,m}$ | number of subcells per direction in a DG cell, and the subcell averages of the a posteriori subcell limiter |
| $\Pi$, $\mathcal{R}$ | cell-to-subcell projection (subcell averaging of $\mathcal{P}_i$) and subcell-to-cell reconstruction (constrained least squares); $\mathcal{R}\circ\Pi = I$ for $N_{\mathrm s} \ge K + 1$ |
| $\delta_{\mathrm{DMP}}$, $\delta_0$, $\epsilon_{\mathrm{DMP}}$ | relaxation of a discrete maximum principle, its absolute floor and its relative factor ($\delta_0$ is one symbol, not the TENO cutoff $\delta_k$ at $k = 0$) |
| $g(t)$ | boundary data, $u(a, t) = g(t)$ at an inflow boundary $x = a$ |
| $C_a$ | offset of the first grid point from the boundary, $x_0 = a + C_a h$, $C_a \in [0, 1)$ ("cut cell" when $C_a \to 0$) |
| $u^{*(k)}$, $n_{\mathrm b}$ | boundary approximations of $\partial^k_x u(a, t)$, $k = 0, \dots, n_{\mathrm b} - 1$, used in the ghost-point Taylor expansion |
| $k_{\mathrm{ILW}}$ | number of the $u^{*(k)}$ obtained by the inverse Lax–Wendroff procedure in its simplified version; the rest are extrapolated |
| $\mu$, $\theta_{\mathrm{ILW}}$ | diffusion coefficient of $u_t + f(u)_x = \mu u_{xx}$, and the convection/diffusion blending weight of the boundary derivatives |
| $\omega^{\mathrm{ext}}_k$ | weights of a weighted (WENO-type) boundary extrapolation; distinct from the reconstruction weights $\omega_k$ |
| $r_{\mathrm{AMR}}$, $N_{\mathrm{lev}}$ | refinement factor between consecutive AMR levels and number of levels above the base grid |
| $M$, $\operatorname{minmod}_M$ | TVB constant and TVB-modified minmod: $\operatorname{minmod}_M(a_1, \dots) = a_1$ if $\vert a_1\vert \le M h^2$, else $\operatorname{minmod}(a_1, \dots)$ |
| $x_G$, $w_G$ | Gauss-type quadrature points in $I_i$ and their weights (Gauss or Gauss–Lobatto), for general quadrature; the Gauss–Lobatto points of a positivity limiter are $\hat x^{(a)}_i$, $\hat w_a$ (batch 3) |
| $V_i$ | cell $I_i$ with its node-sharing (Voronoi) neighbours |
| $\mathsf B$ | universal oscillation-indicator matrix of polynomial WENO on a reference element, $\beta_k = \hat{\mathbf u}_k^{\mathsf T}\mathsf B\,\hat{\mathbf u}_k$ for the coefficient vector $\hat{\mathbf u}_k$ of candidate $k$ |
| $\mathsf P$, $\mathsf Q$, $\mathsf D$ | summation-by-parts norm (symmetric positive definite), the matrix with $\mathsf Q + \mathsf Q^{\mathsf T}$ zero except its two corner entries, and the derivative operator $\mathsf D = \mathsf P^{-1}\mathsf Q$ |
| $\varsigma$, $x_N$ | index of a ghost point beyond a boundary ($x_{-\varsigma}$ at inflow, $x_{N+\varsigma}$ at outflow), and the last interior grid point |
| $e_j$ | Lagrange extrapolation coefficients to an outflow ghost point, $u_{N+\varsigma} = \sum_j e_j u_{N+1-j}$ |
| $\nu_{\max}$ | largest Courant number for which a given spatial scheme with a given time integrator is linearly stable |
| $x^{\mathrm g}$, $\breve u_k$ | target (ghost) point of a weighted extrapolation and its nested partial results, $\breve u_0 = u_{j_0}$ at the nearest node |
| $\lambda_{\mathrm{UW}}$ | tuning parameter of the single-weight extrapolation map $\omega \mapsto (e^{\lambda_{\mathrm{UW}}\omega} - 1)/(e^{\lambda_{\mathrm{UW}}} - 1)$ |

## Boundary conservation, moving boundaries, mapped grids and block AMR

Added 2026-10-08 (batch 5: jiang-1999, mccorquodale-2011, chen-2016, owen-2018, wang-2025, ding-2020, lu-2021, liu-2022, liu-2023, liu-2025).

| Symbol | Meaning |
|---|---|
| $c$ | sound speed, $c = \sqrt{\gamma p/\rho}$ (Euler) |
| $T$, $T_b$ | temperature, and its prescribed value on an isothermal wall |
| $\Phi$ | potential of a divergence projection, $\nabla^2\Phi + \nabla\cdot\mathbf B = 0$, $\mathbf B \leftarrow \mathbf B + \nabla\Phi$ (distinct from the PPM flattening $\phi_i$) |
| $f^{*(k)}$, $f_{-\varsigma}$ | boundary approximations of $\partial^k_x f(u(a, t))$, and ghost-point flux values expanded from them independently of the ghost state ($f_{-\varsigma} \ne f(u_{-\varsigma})$ in general) |
| $\varpi_j$, $\tilde{\mathcal M}$ | boundary quadrature weights of a high-order total mass ($\varpi_j = 1$ away from the boundary), and that mass $\tilde{\mathcal M} = h\sum_j \varpi_j u_j$ (distinct from the nonlinear weights $\omega_k$) |
| $\hat f^{\mathrm{tot}}_{i+1/2}$ | Runge–Kutta total flux, the stage fluxes weighted as in the final update, e.g. $\tfrac16(\hat f^{(0)} + 2\hat f^{(1)} + 2\hat f^{(2)} + \hat f^{(3)})$ for RK4 and $\tfrac16(\hat f^{n} + \hat f^{(1)} + 4\hat f^{(2)})$ for SSP-RK3 |
| $\hat f^{\mathrm R}_{i+1/2}$ | Riemann-solver flux at a face, before any derivative correction |
| $\dot a$ | velocity of a moving boundary $x = a(t)$ |
| $\epsilon_{\mathrm{ILW}}$ | small constant that regularizes the convection/diffusion blending weights of a moving-boundary ILW (e.g. $10^{-6}$) |
| $\mathbf X = (X^1, X^2, X^3)$, $\mathcal J$ | computational coordinates of a mapped grid, and the Jacobian $\mathcal J = \det(\partial\mathbf x/\partial\mathbf X)$ (distinct from the wavenumber $\xi$ and the cell coordinate $\zeta$) |
| $\tilde m^a_b$, $\tilde f^a$ | metric terms $\mathcal J\,\partial X^a/\partial x^b$ and contravariant fluxes $\tilde f^a = \sum_b \tilde m^a_b f_b$ |
| $\mathbf e_d$ | unit vector of coordinate direction $d$ (distinct from the extrapolation coefficients $e_j$) |
| $\Delta_h$, $\Delta^\perp_h$ | second-order discrete Laplacian (divided by $h^2$), and its restriction to the directions tangential to a face |
| $\mathbf W$ | primitive state $(\rho, \mathbf v, p)$ |
| $\langle w\rangle_i$, $\langle w\rangle_{i+1/2}$ | cell average and face average of a function $w$ of the solution (used where $\bar{\ }$ would be ambiguous, e.g. for $\mathbf W$ or products) |
| $C_2$, $C_3$ | curvature-ratio and third-derivative constants of the modified Colella–Sekora limiter (1.25 and 0.1) |
| $\chi$, $k_m$ | fraction of a coarse step in a Runge–Kutta dense output, $0 \le \chi \le 1$, and the stage increments $k_m = \Delta t\,\mathcal L(u^{(m-1)})$ (distinct from the TENO measure $\chi_k$) |
| $M_s$, $\mathrm{Re}$, $\mathrm{Pr}$ | shock Mach number, Reynolds number, Prandtl number |

## MHD divergence and curl constraints, reviews and codes

Added 2026-10-08 (batch 6: balsara-2004, balsara-2009-b, mignone-2010, christlieb-2014, balsara-2016-b, balsara-2023, seo-2023, berta-2024, ding-2024, bernardini-2021, shu-2009, shu-2020).

| Symbol | Meaning |
|---|---|
| $\psi$ | gauge scalar of the vector-potential equation, $\partial_t\mathbf A + (\nabla\times\mathbf A)\times\mathbf v = -\nabla\psi$ (Weyl gauge $\psi = 0$); in use since batch 3, registered at the batch-6 deep lint |
| $\psi_{\mathrm{GLM}}$, $c_h$, $c_p$, $\alpha_p$ | GLM cleaning scalar, cleaning speed, damping parameter, and dimensionless damping $\alpha_p = c_h\min_d h_d/c_p^2$ |
| $c_f$, $c_A$, $c_s$; $c_{f,d}$ | fast magnetosonic, Alfvén and slow speeds; $c_{f,d}$ the fast speed in direction $d$ |
| $\hat B_{x,\mathbf m}$ | coefficient of the mode $\mathbf m$ (monomial or Legendre, written as letters, e.g. $\hat B_{x,xx}$ for the $x^2$ term) of the reconstructed $B_x$ inside one zone; cyclically for $B_y$, $B_z$ |
| $f^{**}_x$, $f^{**}_y$ | numerical fluxes from the strongly interacting state of a multidimensional Riemann solver at an edge or vertex |
| $A^{\mathrm{DDF}}_x$, $A^{\mathrm{DDF}}_y$ | cell-wise constant shifts of the normal-field traces that make a discrete divergence of the traces vanish |
| $\rho e(u)$ | internal-energy density as a function of the conserved state, concave for $\rho > 0$ |
| $\mathbf J$, $\boldsymbol\Omega$ | a curl-constrained vector field (edge-collocated) and its curl $\boldsymbol\Omega = \nabla\times\mathbf J$, divergence-free (distinct from the mapped-grid Jacobian $\mathcal J$) |

## Cleaning parameters, MHD eigensystems and viscous positivity

Added 2026-10-09 (batch 7: zhang-2017, balsara-2017-d, ryu-1995, derigs-2018, mignone-2010-b, tomida-2026, balsara-2001).

| Symbol | Meaning |
|---|---|
| $L_{\mathrm{GLM}}$, $C_r$ | GLM damping length and the dimensionless ratio $C_r = c_p^2/(c_h L_{\mathrm{GLM}})$; then $\alpha_p = \min_d h_d/(C_r L_{\mathrm{GLM}})$ |
| $\hat\psi_{\mathrm{GLM}}$ | GLM scalar in field units, $\psi_{\mathrm{GLM}} = c_h\hat\psi_{\mathrm{GLM}}$ (the convention of the entropy-consistent GLM system) |
| $\alpha_f$, $\alpha_s$; $B_\perp$ | normalization factors of the fast and slow MHD eigenvectors; magnitude of the field tangential to the sweep direction (subscripted, so distinct from the Lax–Friedrichs speed $\alpha$) |
| $\mathbf f^{\mathrm v}$, $\boldsymbol\tau$, $\mathbf q$ | viscous flux of the compressible Navier–Stokes equations, $\partial_t u + \nabla\cdot\mathbf f(u) = \nabla\cdot\mathbf f^{\mathrm v}$; viscous stress tensor; heat-flux vector (bold, so distinct from the WENO-Z $\tau$ and the weight power $q$) |
| $\beta^{\mathrm v}_{i+1/2}$ | penalty coefficient of a Lax–Friedrichs-type viscous (or total) numerical flux |
| $\theta_e$ | single-ratio internal-energy scaling factor of the scaling limiter (one ratio for the whole state, no quadratic solve) |
| $\hat f^{\mathrm{EC}}$, $\hat f^{\mathrm{ES}}$ | entropy-conservative and entropy-stable numerical fluxes |

## Riemann-solver design, shock instability, low Mach and well-balancing

Added 2026-10-12 (batch 8: simon-2019, simon-2019-b, miczek-2015, edelmann-2021, xie-2021, dumbser-2016, navasmontilla-2019, kitamura-2019).

| Symbol | Meaning |
|---|---|
| $u^{\mathrm{HLL}}_*$; $u^{\mathrm{HLLC}}_{*L}$, $u^{\mathrm{HLLC}}_{*R}$ | HLL intermediate (star) state, and the two HLLC star states (distinct from the ILW boundary derivatives $u^{*(k)}$) |
| $S_L^-$, $S_R^+$ | clipped wave speeds $\min(S_L, 0)$ and $\max(S_R, 0)$ of the upwind form of an HLL-type flux |
| $\mathbf d^{\mathrm{HLL}}$ | dissipation vector of the HLL flux in central form, $\hat f^{\mathrm{HLL}} = \tfrac12\left(f(u^-) + f(u^+)\right) + \mathbf d^{\mathrm{HLL}}$ |
| $\delta_p$, $\mathcal I$ | anti-diffusion coefficient of intermediate family $p$ in an HLLEM (HLLI) flux, $0 < \delta_p \le 1$ for the Dumbser–Balsara weight (the bound is solver-specific: Balsara & Nkonga's HLLI weight differs, and their 2D factors can exceed 1; batch 11) (in use since batch 7; distinct from the TENO cutoff $\delta_k$), and the set of intermediate families resolved |
| $v_n$, $v_t$ | velocity components normal and tangential to a face, $v_n = \mathbf v\cdot\mathbf n$ |
| $\Theta_{i+1/2}$ | numerical viscosity matrix, $\hat f_{i+1/2} = \tfrac12\left(f(u^-) + f(u^+)\right) - \tfrac12\Theta_{i+1/2}(u^+ - u^-)$ |
| $S^{\mathrm w}_L$, $S^{\mathrm w}_R$; $\alpha_{\mathrm{SWM}}$, $\epsilon_{\mathrm{SWM}}$ | widened wave speeds $S_L - \alpha_{\mathrm{SWM}}\epsilon_{\mathrm{SWM}}$, $S_R + \alpha_{\mathrm{SWM}}\epsilon_{\mathrm{SWM}}$ of a selective-wave-modified HLL dissipation; tuning coefficient and sensor-sized increment (subscripted, so distinct from the Lax–Friedrichs $\alpha$ and the weight regularization $\varepsilon$) |
| $\omega_{\mathrm p}$ | pressure-ratio shock sensor, $0 < \omega_{\mathrm p} \le 1$, near 1 in smooth flow (distinct from the nonlinear weights $\omega_k$) |
| $\varphi_{\mathrm p}$ | entropy-control factor, $\varphi_{\mathrm p} \le 1$, scaling the pressure part of the entropy-wave strength |
| $\nu_y$ | Courant number $\sqrt\gamma\,\Delta t/h_y$ of the linear saw-tooth perturbation analysis across a grid-aligned shock |
| $\mathrm{Ma}$, $\mathrm{Ma}_r$, $\mathrm{Ma}_{\mathrm{cut}}$ | local flow Mach number $\vert\mathbf v\vert/c$, reference Mach number of a nondimensionalization, and the lower cut-off of a low-Mach rescaling (distinct from the TVB constant $M$ and the shock Mach number $M_s$) |
| $M_{\mathrm{prop}}$, $M_{\mathrm{sig}}$ | grid-frame shock propagation speed over the upstream sound speed (equals $M_s$ into gas at rest), and the post-shock signal Mach number $c_{\mathrm{post}}/c_{\mathrm{pre}}$ as a function of $M_s$ |
| $\epsilon_{\mathrm{sh}}$, $\epsilon_{\mathrm g}$ | sub-cell position of a captured steady shock, $\epsilon_{\mathrm{sh}} \in [0, 1)$, and the alternating centreline grid displacement of Quirk's test, in cell sizes |
| $P_{\mathrm{pc}}$, $\mu_{\mathrm{pc}}$, $\delta_{\mathrm{pc}}$ | low-Mach preconditioning matrix applied to the dissipation only, its Mach parameter $\mu_{\mathrm{pc}} = \min[1, \max(\mathrm{Ma}, \mathrm{Ma}_{\mathrm{cut}})]$, and $\delta_{\mathrm{pc}} = 1/\mu_{\mathrm{pc}} - 1$ |
| $\mathbf s(u)$, $u^{\mathrm{eq}}$ | source term of a balance law $\partial_t u + \nabla\cdot\mathbf f(u) = \mathbf s(u)$ (bold, so distinct from the stage count $s$), and a known steady (equilibrium) state of it |
| $\varphi_{\mathrm g}$, $\mathbf g$ | gravitational potential and acceleration, $\mathbf g = -\nabla\varphi_{\mathrm g}$ (distinct from the PPM flattening $\phi_i$ and the boundary data $g(t)$) |

## Deep-lint additions (2026-10-12)

| Symbol | Meaning |
|---|---|
| $\theta_{\mathrm{rot}}$, $\phi_{\mathrm{rot}}$ | in-plane and out-of-plane angles of a problem rotated against the grid (distinct from the limiter $\theta$ and the PPM $\phi_i$) |
| $\varrho$ | radial distance from a set-up centre (distinct from the density $\rho$ and the stencil count $r$) |
| $\mathcal T$, $\vert\mathcal T\vert$, $\vert\partial_i\mathcal T\vert$ | a triangular cell, its area and the length of its edge $i$ |
| $\delta^{\mathrm{MC}}\bar u_i$ | monotonized-central limited slope of cell $I_i$ (distinct from the PPM jump $\Delta u_i$) |
| $u^{\mathrm S}$ | source-term half-step state $u + 2\Delta t\,\mathbf s(u)$ of a split positivity-preserving update |
| $\hat u^{(t)}$, $\hat f^{(x)}$, … | space–time modal coefficients of the predictor, indexed by the derivative they represent (extends $\hat u^{(lm)}$) |

## Butcher form, step-size control, relaxation and multistep methods

Added 2026-10-12 (batch 9: ranocha-2020, ranocha-2022, nusslein-2021, hadjimichael-2016, higueras-2019, runge-1895).

| Symbol | Meaning |
|---|---|
| $\mathsf a_{ij}$, $\mathsf b_j$, $\mathsf c_i$ | Butcher tableau of an $s$-stage Runge–Kutta method: stage values $Y_i = u^n + \Delta t\sum_j \mathsf a_{ij}\mathcal L(Y_j)$ at times $t^n + \mathsf c_i\Delta t$, update $u^{n+1} = u^n + \Delta t\sum_j \mathsf b_j\mathcal L(Y_j)$ (sans-serif, so distinct from the Shu–Osher $a_{ik}$, $b_{ik}$; explicit iff $\mathsf a_{ij} = 0$ for $j \ge i$); $\mathsf A$, $\mathsf b$, $\mathsf c$ are the matrix and vectors |
| $Y_i$ | Butcher stage value, $i = 1,\dots,s$ ($Y_1 = u^n$ for an explicit method); not the Shu–Osher $u^{(i)}$, whose stages are combinations of forward-Euler steps |
| $p_{\mathrm t}$, $\hat p_{\mathrm t}$, $\tilde p_{\mathrm t}$ | order of a time integrator, of its embedded method, and of a method with modified weights (distinct from the pressure $p$ and the field index $(p)$) |
| $\hat{\mathsf b}_j$, $\tilde{\mathsf b}_j$ | weights of the embedded method of a pair (error estimate $\Delta t\sum_j(\mathsf b_j - \hat{\mathsf b}_j)\mathcal L(Y_j)$), and weights modified after the stages are known |
| $z$, $R_{\mathrm{st}}(z)$ | $z = \Delta t\,\lambda$ for the test equation $u' = \lambda u$, and the stability function, $u^{n+1} = R_{\mathrm{st}}(z)\,u^n$ (distinct from the eigenvector matrix $R$) |
| $\mathcal C_{\mathrm{eff}}$, $\mathcal C_{\mathrm{obs}}$ | effective SSP coefficient $\mathcal C/s$ (per operator evaluation), and the observed coefficient: the largest $\Delta t/\Delta t_{\mathrm{FE}}$ at which a test stays monotone, both steps measured on that test |
| $\mathrm{err}^{n+1}$, $\mathtt{tol}$ | weighted root-mean-square local error estimate of a step, $\mathrm{err}^{n+1} \le 1$ meaning "within tolerance", and the tolerance |
| $\beta^{\mathrm c}_1$, $\beta^{\mathrm c}_2$, $\beta^{\mathrm c}_3$; $k_{\mathrm c}$ | PID step-size controller coefficients and its exponent order, $\Delta t^{n+1} = (\mathrm{err}^{n+1})^{-\beta^{\mathrm c}_1/k_{\mathrm c}}(\mathrm{err}^{n})^{-\beta^{\mathrm c}_2/k_{\mathrm c}}(\mathrm{err}^{n-1})^{-\beta^{\mathrm c}_3/k_{\mathrm c}}\Delta t^n$ (distinct from the smoothness indicators $\beta_k$) |
| $U(u)$, $\mathcal S(u)$ | convex entropy function of a conservation law, and a convex functional of the discrete solution (the global entropy $\int U(u)\,dx$ in its quadrature form, or any convex quantity a time integrator must not increase) |
| $\gamma^n_{\mathrm R}$, $\Psi^n(\gamma)$ | relaxation parameter of step $n$, and the relaxation residual whose positive root it is (subscripted, so distinct from the ratio of specific heats $\gamma$) |
| $m$ (multistep) | number of steps of a linear multistep method, as on the [barrier page](/results/ssp-order-barriers.md) (distinct from the system size $m$ by context) |
| $\Omega_{\Delta t}$ | step-history sum of a variable-step multistep method, $\Omega_{\Delta t} = 1 + \sum_{j=1}^{m-1}\Delta t^{n-j}/\Delta t^{n}$, equal to $m$ for fixed steps (distinct from a domain $\Omega$) |
| $\Delta t_{\mathrm{FE}}(u)$ | forward-Euler step limit evaluated at the state $u$ (extends $\Delta t_{\mathrm{FE}}$) |
| $a_{i,n}$, $b_{i,n}$ | coefficients of a variable-step $m$-step method, $u^{n+1} = \sum_{i=1}^{m}\left(a_{i,n}u^{n+1-i} + \Delta t^n b_{i,n}\mathcal L(u^{n+1-i})\right)$, depending on the step history (two indices, so distinct from the Shu–Osher $a_{ik}$, $b_{ik}$) |
| $\mathcal L(t, u)$ | the operator of a non-autonomous system $u' = \mathcal L(t, u)$ (extends $\mathcal L(u)$) |
| $\mathsf I$, $\mathbf 1$ | identity matrix and vector of ones in Butcher-form formulas |
| $N_{\mathrm{dof}}$, $u^{n+1}_{\mathrm{emb}}$ | number of unknowns in an error norm, and the embedded solution of a pair |
| $\mathtt{atol}$, $\mathtt{rtol}$ | absolute and relative error tolerances of step-size control |

## Immersed and embedded boundaries

Added 2026-10-12 (batch 10: peskin-2002, berger-2021, giuliani-2022, barriosanchez-2024, natarajan-2022, seshadri-2020, baskaya-2024).

| Symbol | Meaning |
|---|---|
| $\kappa_i$ | volume fraction of a cut cell, $\vert I_i\vert = \kappa_i h^d$, $0 < \kappa_i \le 1$ ($\kappa_i = 1$ for a regular cell; subscripted, so distinct from the Suresh–Huynh constant $\kappa$) |
| $u^{\mathrm{pr}}_i$ | provisional state of a cell after a step whose $\Delta t$ is set by the regular cells, before small-cell stabilization |
| $\mathcal N_i$, $N^{\mathrm{ov}}_i$ | merging neighbourhood of cell $I_i$ in state redistribution ($\mathcal N_i = \{i\}$ for a cell that needs none), and the number of neighbourhoods that contain $I_i$, its own included |
| $\widehat{\mathcal V}_i$, $\hat{\mathbf x}_i$ | weighted volume $\sum_{j\in\mathcal N_i}\vert I_j\vert/N^{\mathrm{ov}}_j$ and weighted centroid of a merging neighbourhood |
| $\bar u^{\mathcal N}_i$, $q^{\mathcal N}_i(\mathbf x)$ | weighted average of $u^{\mathrm{pr}}$ over $\mathcal N_i$, and its limited linear reconstruction about $\hat{\mathbf x}_i$ |
| $(\nabla\cdot\mathbf f)^{\mathrm c}_i$, $(\nabla\cdot\mathbf f)^{\mathrm{nc}}_i$ | conservative flux divergence of a cut cell (flux balance over its volume) and the non-conservative neighbourhood average used by flux redistribution |
| $\mathsf W$ | redistribution matrix of state redistribution, $\widehat{\mathcal V} = \mathsf W\,\vert I\vert$ (vector of cell volumes); the scheme is conservative iff every column of $\mathsf W$ sums to one |
| $\eta^{\mathrm{self}}_i$, $\eta^{\mathrm{nb}}_i$ | weights of weighted state redistribution: the share a small cell keeps of its own provisional state, and the share its neighbourhood contributes (superscripted, so distinct from the coercivity constant $\eta$) |
| $\mathbf X_{\mathrm{IB}}(t)$, $\mathbf F_{\mathrm{IB}}$, $\mathbf b_{\mathrm{IB}}$ | Lagrangian configuration of an immersed boundary (a function of the Lagrangian labels), its force density, and the Eulerian body force it produces (distinct from the mapped coordinates $\mathbf X$) |
| $\delta_h$, $\phi_{\mathrm{IB}}(\varrho_{\mathrm{IB}})$ | discrete delta function of the immersed-boundary method (in $d$ dimensions, $h^{-d}$ times the product of $\phi_{\mathrm{IB}}$ over the coordinate directions), its one-dimensional kernel, and the kernel argument $\varrho_{\mathrm{IB}}$, a distance in meshwidths (subscripted, so distinct from the radial $\varrho$) |

## Spectral analysis

Added 2026-10-08 (batch 2, with the modified-wavenumber definition; dated from the log at the 2026-10-13 deep lint).

| Symbol | Meaning |
|---|---|
| $\xi$ | scaled wavenumber $k h$, $0 \le \xi \le \pi$ |
| $\tilde\xi(\xi)$ | modified wavenumber of a scheme for $\partial_x$; $\operatorname{Re}\tilde\xi$ measures dispersion, $\operatorname{Im}\tilde\xi$ dissipation (negative for a dissipative upwind scheme on right-running waves) |

## Recovery DG, characteristic boundaries and MHD Roe matrices (batch 11, 2026-10-13)

| Symbol | Meaning |
|---|---|
| $\mu_{\mathrm{IP}}$, $\sigma_{\mathrm{DG}}$, $\omega_{\mathrm{DG}}$ | penalty coefficient, symmetry coefficient and jump-of-derivative coefficient of the interior-penalty DG diffusion family (subscripted, so distinct from the diffusion coefficient $\mu$, the flux-limiter constant $\sigma$ and the weights $\omega$) |
| $[\![q]\!]_{i+1/2}$, $\{\!\{q\}\!\}_{i+1/2}$ | jump and average of $q$ across the interface $x_{i+1/2}$ ($q$ a generic placeholder, distinct from the weight power $q$) |
| $u^{\mathrm{rec}}_{i+1/2}$ | recovered polynomial spanning the two cells that share $x_{i+1/2}$ |
| $\mathscr L^{(p)}$ | amplitude variation of the characteristic wave of family $p$ at a boundary (script, so distinct from the spatial operator $\mathcal L$; where pressure $p$ appears nearby, the families are written out as $\mathscr L^{(1)},\dots,\mathscr L^{(5)}$) |
| $K_{\mathrm{NR}}$, $\sigma_{\mathrm{NR}}$, $p_\infty$ | relaxation coefficient and constant of a partially non-reflecting outflow condition, and the target pressure |
| $L_x$ | domain length in $x$ |
| $(\hat f_x)_k$, $(\hat f_y)_k$ | $k$-th component of the numerical flux in direction $x$ or $y$ |
| $\nabla_u$ | gradient with respect to the conserved state $u$ |
| $S$ | single signal speed of a local Lax–Friedrichs (Rusanov) flux, where no left/right pair $S_L$, $S_R$ is used; the same quantity as the local Lax–Friedrichs speed $\alpha_{i+1/2}$, written $S$ on Riemann-solver pages beside $S_L$, $S_R$ (distinct from the stencils $S_k$) |
| $RU$, $LU$, $LD$, $RD$ (subscripts) | the four states meeting at a cell edge in a multidimensional Riemann problem: right/left, up/down |

## Shock reflection, diffraction and bodies in a shock tube (batch 12, 2026-10-13)

| Symbol | Meaning |
|---|---|
| $\theta_{\mathrm w}$ | angle of the reflecting wall: the half-angle of a wedge or cone, or the local inclination of a curved wall, measured as the page that uses it states (subscripted, so distinct from the limiter $\theta$ and $\theta_{\mathrm{rot}}$) |
| $\theta_{\mathrm{tr}}$ | wall angle at which regular reflection turns into Mach reflection |
| $M_s^*$ | shock Mach number at which the flow behind a shock moving into gas at rest becomes sonic in the laboratory frame ($\approx 2.07$ for $\gamma = 1.4$) |
| $D$ | diameter of a body (cylinder or sphere) |
| $C_D$ | drag coefficient: the drag force over $\tfrac12\rho\vert\mathbf v\vert^2$ of the post-shock flow times the frontal area of the body |
| $\Gamma$ | circulation, the integral of the vorticity $\nabla\times\mathbf v$ over an area |
| $p_*$, $v_{n*}$; $\rho_{*L}$, $\rho_{*R}$; $c_{*L}$, $c_{*R}$ | pressure and normal velocity of the star region of a Riemann problem between $u^-$ and $u^+$, and the densities and sound speeds on either side of its contact |
| $f^{\mathrm p}_L$, $f^{\mathrm p}_R$, $f^{\mathrm p}$ | pressure functions of the exact Euler Riemann solver: the velocity jump across the left or right wave as a function of the star pressure, and $f^{\mathrm p} = f^{\mathrm p}_L + f^{\mathrm p}_R + v_n^+ - v_n^-$, whose root is $p_*$ |
| $g^{\mathrm{TS}}_L$, $g^{\mathrm{TS}}_R$ | shock factors of the pressure functions, as used by the two-shock approximation |
| $p_{\mathrm{PV}}$, $p_{\mathrm{TR}}$, $p_{\mathrm{TS}}$ | star-pressure estimates of the primitive-variable, two-rarefaction and two-shock approximate-state Riemann solvers |
| $\mathrm{TOL}$, $Q_{\mathrm{user}}$ | convergence tolerance of the star-pressure iteration, and the pressure-ratio threshold that switches an adaptive Riemann solver between estimates |
| $q^{\mathrm w}_L$, $q^{\mathrm w}_R$, $\bar c_{\mathrm E}$ | pressure-based correction factors of the HLL-type wave speeds $S_L = v_n^- - c^- q^{\mathrm w}_L$, $S_R = v_n^+ + c^+ q^{\mathrm w}_R$, and the averaged sound speed of Einfeldt's estimate, $S_{L,R}$ = a mean normal velocity $\mp \bar c_{\mathrm E}$ |
| $q_{\mathrm{Roe}}$ (e.g. $\rho_{\mathrm{Roe}}$, $c_{\mathrm{Roe}}$) | ($q$ a generic placeholder, distinct from the weight power $q$) a quantity evaluated at the Roe-averaged state of $u^-$ and $u^+$ ($\sqrt\rho$-weighted velocities and total enthalpy, Roe 1981; $\rho_{\mathrm{Roe}} = \sqrt{\rho^-\rho^+}$ from the later Roe–Pike form, Toro; $c_{\mathrm{Roe}}$ from them); the Roe speeds $\hat a_{i+1/2}$ are the eigenvalues of $A$ at this state |

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
| $h$ | uniform spacing; $h_i$ on a non-uniform grid |
| $t^n$, $\Delta t$ | time level and time step |
| $\nu$ | CFL number, $\nu = \Delta t \max_p |\lambda^{(p)}| / h$ |

## Discrete unknowns and fluxes

| Symbol | Meaning |
|---|---|
| $\bar u_i$ | cell average of $u$ over $I_i$ (finite volume) |
| $u_i$ | point value $u(x_i)$ (finite difference) |
| $u^-_{i+1/2}$, $u^+_{i+1/2}$ | reconstructed interface states from the left and from the right of $x_{i+1/2}$ |
| $\hat f_{i+1/2}$ | numerical flux at $x_{i+1/2}$; conservative semi-discretization $\frac{d}{dt} u_i = -\frac{1}{h}\left(\hat f_{i+1/2} - \hat f_{i-1/2}\right)$ |
| $\mathcal{H}$ | Shu–Osher flux primitive of the conservative FD form: $f(u(x)) = \frac{1}{h}\int_{x-h/2}^{x+h/2} \mathcal{H}(\xi)\, d\xi$, so $\hat f_{i+1/2}$ approximates $\mathcal{H}(x_{i+1/2})$ |
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

---
type: Method
title: "Gaussian-process reconstruction and GP-WENO"
description: "Reconstruction as the posterior mean of a Gaussian process conditioned on cell averages: data-independent weights from a squared-exponential kernel, order 2R+1 on 2R+1 cells, a length hyperparameter tuned to the flow, and WENO-type nonlinear weights from GP (RKHS-norm) smoothness indicators."
status: established
aliases: [GP-WENO, Gaussian process reconstruction, GP-SE]
tags: [weno, non-polynomial, kernel-methods, finite-volume, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Gaussian-process reconstruction and GP-WENO

**GP prediction** ([Reyes et al. (2018)](/sources/reyes-2018.md), §2;
checked on the page images). A GP is a distribution over functions
fixed by a mean $\bar f(x)$ and a symmetric positive-definite covariance
kernel $\mathcal{K}(x, y)$; the default is the squared exponential
$$\mathcal{K}(x, y) = \Sigma^2\exp\left[-\frac{(x - y)^2}{2\ell^2}\right].$$
Conditioning on data $\mathbf f$ at the training points gives the
posterior mean
$\tilde f_* = \bar f(x_*) + \mathbf k_*^{T}\boldsymbol{\mathcal K}^{-1}(\mathbf f - \bar{\mathbf f})$,
with $\boldsymbol{\mathcal K}_{ij} = \mathcal{K}(x_i, x_j)$ and $k_{*,i} = \mathcal{K}(x_*, x_i)$.
For **reconstruction from cell averages** the averages are linear
functionals of the GP, so they are jointly Gaussian with covariances
$C_{kh} = \iint \mathcal{K}(x, y)\,dg_k(x)\,dg_h(y)$ and prediction vector
$t_{*,k} = \int \mathcal{K}(x, x_*)\,dg_k(x)$ (cell-average measures
$dg_k$). This gives $\tilde f_* = f_0 + \mathbf z^{T}(\mathbf G - f_0\mathbf 1)$ with
$\mathbf z^{T} = \mathbf t_*^{T}\mathbf C^{-1}$; for the SE kernel these
integrals are closed-form error functions. The weights $\mathbf z$ do
not depend on the data, so on a fixed (or AMR-level-wise) grid they
are computed once. $\Sigma^2$ has no effect on the mean, and a zero
mean ($f_0 = 0$) works well.

**Order and conditioning.** On $2R+1$ cells the method converges at
order $2R+1$ (third to eleventh order for $R = 1$–$5$), the order of
WENO with $r = R+1$ on the same stencil (§5.2). For smooth data the SE
kernel's $C^\infty$ native space gives fast convergence. $\mathbf C$ becomes
nearly singular for $\ell/h \gg 1$: in double precision errors plateau
near $10^{-7}$ (condition number $\sim 10^8$; breakdown for $\ell/h > 48$
at $R = 2$), so the weights are precomputed in quadruple precision
(plateau near $10^{-12}$, condition number $\sim 10^{18}$) and truncated
to double. A "nugget" regularization costs accuracy.

**GP-WENO** (§2.5). The $2R+1$-cell stencil is split into $R+1$
sub-stencils $S_k$ of $R+1$ cells. The optimal weights $d_k$ are the least-squares solution of the
overdetermined system that makes the weighted sub-stencil predictions
reproduce the full-stencil one (eqs. 30–34); they are computed once and
depend on the kernel. The nonlinear weights are the Jiang–Shu form
$\tilde\omega_k = d_k/(\varepsilon + \beta_k)^{q}$, with $q = 1$ and
$\varepsilon = 10^{-36}$. The **GP smoothness indicator** is the squared
norm of the sub-stencil point values in the reproducing-kernel Hilbert
space,
$$\beta_k = \sum_{i=1}^{R+1}\frac{\left(c^{(k)}_i\right)^2}{\mu^{(k)}_i},\qquad c^{(k)}_i = \left(\mathbf e^{(k)}_i\right)^{T}\mathbf f^{(k)},$$
where $(\mu^{(k)}_i, \mathbf e^{(k)}_i)$ are eigenpairs of the pointwise
kernel matrix on the sub-stencil. Equivalently,
$\beta_k = -2\ln P(\mathbf f^{(k)}) + \text{const}$: a large indicator is a
small likelihood under the smoothness model. Unlike the polynomial
indicators of the [smoothness-indicator](/definitions/smoothness-indicator.md)
page, no Taylor-expansion proof of accuracy is given; the design order
is observed numerically (§2.5).

**Length scale.** $\ell$ is a tuning knob absent from polynomial
methods. Errors are minimal for $\ell$ near the physical feature size
(the Gaussian half-width in advection; $\ell/h = 3$, about half the
post-shock wavelength, in the
[Shu–Osher problem](/benchmarks/shu-osher-problem.md)), and tend to
WENO-JS's for $\ell \gg h$. The defaults are $\ell/h = 6$ or $12$
(§§2.4, 5).

**Results** ([Reyes et al. (2018)](/sources/reyes-2018.md), §5; 1D FV, RK4,
characteristic variables, HLLC or Roe). GP-R2 costs about the same as
WENO-JS and reaches a given error 30% sooner; GP-R3 60% sooner. Near
discontinuities the GP indicators keep more amplitude. Counter to
polynomial intuition, the smallest stencil (GP-R1) oscillates most at
shocks, because the truncated kernel eigen-expansion approximates the
RKHS norm worst on small stencils. Brio–Wu and Ryu–Jones MHD shock
tubes show slow-shock oscillations comparable to WENO-JS's. The kernel
form is isotropic and needs no tensor structure, which motivates
multi-D extensions.

# Citations

1. [Reyes et al. (2018)](/sources/reyes-2018.md), §§1–5, Appendices A–C (eqs. 1, 3, 17, 24–35, 42 read from the page images).

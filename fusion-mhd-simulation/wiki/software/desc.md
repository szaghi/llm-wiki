---
type: Software
title: "DESC"
description: "Pseudospectral 3D ideal-MHD inverse equilibrium code in Python/JAX that expands the flux-surface geometry and stream function in a global Fourier–Zernike basis and drives the force residual to zero at collocation nodes with a Newton-type solver; against VMEC it converges exponentially in radial resolution, stays accurate at the axis and reaches about tenfold lower force error at equal runtime."
status: established
aliases: [DESC stellarator code suite]
tags: [code, equilibrium, stellarator, spectral, verification]
timestamp: 2026-10-16T00:00:00Z
---

# DESC

DESC is a fixed-boundary 3D ideal-MHD inverse equilibrium code from Princeton
University, written in Python with JAX just-in-time compilation
([Panici et al. (2023)](/sources/panici-2023.md), §1, §3.2). The cited paper is
the first of a three-part suite and is a verification comparison with
[VMEC](/software/vmec.md); the original DESC method paper (Dudt & Kolemen 2020)
is not ingested. See
[three-dimensional inverse equilibrium solvers](/methods/inverse-equilibrium-solvers.md).

## Equilibrium problem

DESC solves $\mathbf J\times\mathbf B=\nabla p$, $\nabla\times\mathbf B=\mu_0\mathbf J$,
$\nabla\cdot\mathbf B=0$ with nested flux surfaces and $p$ a flux function, so it
cannot represent islands. Inputs are the boundary shape, $p$, and either
$\iota$ or the net toroidal current (Panici et al. 2023, §1–3).

## Coordinates and basis

* Computational coordinates $(s,\theta,\zeta)$ with $s=\sqrt{\psi_{t,N}}$, a
  poloidal angle $\theta$ equal to the straight-field-line angle minus a
  stream function $\lambda$, and $\zeta$ the cylindrical toroidal angle. This
  version uses the VMEC-like angle; the original DESC used the
  straight-field-line angle itself (Panici et al. 2023, §3.2, Eq. 3.16).
* $R$, $Z$ and $\lambda$ are expanded in Zernike polynomials in $(s,\theta)$
  times Fourier modes in $\zeta$ with $N_{\mathrm{fp}}$ periodicity, truncated
  at radial, poloidal and toroidal resolutions $L$, $M$, $N$; ANSI and Fringe
  index sets are available (Eqs. 3.17–3.20, Table 2).
* The Zernike basis enforces the near-axis analyticity condition by
  construction: the $m$-th poloidal Fourier coefficient behaves as $s^{m}$
  times an even power series in $s$ (Lewis & Bellan 1990) (Eq. 3.21).

## Solver

The force residual $\mathbf J\times\mathbf B-\nabla p$ is split into its radial
and helical components, weighted by volume, and evaluated on a collocation
grid; the resulting nonlinear system in the spectral coefficients is solved by
SciPy Newton-type methods such as Levenberg–Marquardt, with quadratic
convergence near the solution (Panici et al. 2023, §3.2, Eqs. 3.25–3.28). An
energy objective is possible, but the force objective is "faster (by a factor
of two in some cases)" with better convergence "in extensive testing" (no data
shown) (§3.2). Runs are on CPU; runtimes never fall below about 2 min because
of JIT compilation; MPI parallelism, GPU benchmarking and pre-compilation are
future work (§5.3.2, §6).

## Verification against VMEC

All from Panici et al. (2023). Accuracy is measured by a common metric: the
magnitude of the force residual, flux-surface- or volume-averaged and
normalized by the volume average of $|\nabla p|$, computed for VMEC a
posteriori from its Fourier output (§4, App. A).
* **D-shaped tokamak** (about 3 % $\beta$): VMEC converges at first order in
  radial resolution (fit slope $-1.02$), DESC exponentially, with errors from
  about $5\times10^{-5}$ at $L=16$ to $4\times10^{-7}$ at $L=24$; DESC meets
  the $10^{-4}$ threshold borrowed from EFIT practice and VMEC does not, even
  at 1024 surfaces (§5.2, §5.4, Figs. 7–8).
* **W7-X standard configuration** at $\beta\approx2\,\%$: flux surfaces and
  spectral width agree, but VMEC's Fourier coefficients violate the near-axis
  $s^{m}$ scaling and its force error rises sharply toward the axis, while the
  DESC error stays flat to the axis (about $10^{-2}$, $3\times10^{-4}$ and
  $10^{-4}$ at $L=M=N=12$, 16, 20) (§5.1, §5.3, Figs. 4–5, 10–11). At equal
  runtime on the same CPU DESC reaches about one order of magnitude lower error
  (fits: error $\propto t^{-0.46}$ for DESC, $t^{-0.27}$ for VMEC) (Fig. 12).
* **Mercier stability** of a quasi-helically symmetric finite-$\beta$
  equilibrium (aspect ratio about 20): DESC at $L=12$ matches near-axis
  asymptotics (Landreman & Jorge 2020) down to the axis; VMEC deviates near the
  axis even with 801 surfaces, the deviation dominated by the geodesic
  curvature term, which needs higher radial derivatives (§5.4, Figs. 15–16).
  See [quasi-symmetry](/definitions/quasi-symmetry.md).

## Use by MHD codes

GMEC reads DESC equilibria through external MATLAB scripts; DESC "provides
high-precision derivatives" and supplied the 2/1 tearing equilibrium of the
GMEC–MAS benchmark ([Jiang et al. (2024)](/sources/jiang-2024.md), §VI C,
§IX C). [Liu et al. (2024)](/sources/liu-2024.md) (§II D) list DESC as an
alternative equilibrium source for the hybrid GMEC runs. See
[GMEC](/software/gmec.md).

## Limitations

* Nested surfaces only: no islands or stochastic regions (Panici et al. 2023,
  §2).
* Fixed boundary in the cited paper (§3).
* The DESC force error oscillates at collocation surfaces (Fig. 11).
* The comparison integrates VMEC errors over $\psi_{t,N}\in[0.1,0.99]$ but DESC
  errors over the full volume, which the authors note favours VMEC (§4).

# Citations

1. [Panici et al. (2023)](/sources/panici-2023.md) — §§1–6, App. A–C, Figs. 4–16.
2. [Jiang et al. (2024)](/sources/jiang-2024.md) — §VI C, §IX C.
3. [Liu et al. (2024)](/sources/liu-2024.md) — §II D.

---
type: Software
title: "LESGO"
description: "LESGO is an open-source incompressible LES code, pseudo-spectral in the wall-parallel directions and second-order finite-difference on a staggered wall-normal grid, used as the host of wall-model studies: the LaRTE model and an a posteriori comparison of machine-learning wall models."
status: established
aliases: [lesgo]
tags: [software, les, wmles, wall-model, machine-learning]
timestamp: 2026-10-25T13:34:00Z
---

# LESGO

**LESGO** is an open-source, parallel LES code for incompressible wall-bounded
flow that discretizes the wall-parallel directions pseudo-spectrally and the
wall-normal direction with second-order centred finite differences on a
staggered grid. In the sources it is the platform on which wall models for
[wall-modelled LES](/methods/wall-modelled-les.md) are developed and compared:
the [Lagrangian relaxation towards equilibrium (LaRTE) model](/methods/lagrangian-relaxation-towards-equilibrium-wall-model.md)
of [Fowler et al. (2022)](/sources/fowler-2022.md) and the
[machine-learning wall models](/methods/machine-learning-wall-model.md)
assessed by [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md).

## Discretization

As described by Vadrot et al. (2023b, §II A), with the wall-normal coordinate
written $y$ here (the source uses $z$, the atmospheric convention of the code):

- pseudo-spectral in the streamwise and spanwise directions, second-order
  finite differences in the wall-normal direction, on a uniform grid
  $N_x\times N_y\times N_z$;
- staggered in the wall-normal direction, with the first plane of wall-parallel
  velocity at half a cell, $\Delta y/2$, and the last grid point just outside
  the domain, so that $\Delta y=L_y/(N_y-1)$.

Fowler et al. (2022, §5) describe it as a "mixed pseudo-spectral and centred
finite-difference" code. Neither source states the time-integration scheme or
the de-aliasing rule.

## Closures available

- **SGS models** (Vadrot et al. 2023b, §II A): constant-coefficient
  [Smagorinsky](/methods/smagorinsky-model.md), [dynamic](/methods/dynamic-procedure.md)
  and Lagrangian dynamic Smagorinsky, the Lagrangian scale-dependent dynamic
  model of Bou-Zeid et al., and the anisotropic minimum-dissipation (AMD) model.
  Fowler et al. (2022) use the Lagrangian scale-dependent dynamic model;
  Vadrot et al. use AMD and find that switching to the Lagrangian
  scale-dependent model changes the mean velocity very little at
  $Re_\tau=5200$, for the equilibrium and the learned wall models alike (App. B,
  Fig. 18).
- **Wall models**: the [equilibrium wall model](/methods/equilibrium-wall-model.md)
  in algebraic log-law form, $\tau_w=\rho\big[\kappa U_{\mathrm{LES}}/\ln(h_{\mathrm{wm}}/y_0)\big]^2$
  with $y_0=\nu\exp(-\kappa B)/u_\tau$ (page-local), $\kappa\approx0.4$,
  $B\approx5$, solved iteratively (Vadrot et al. 2023b, Eqs. 1–2); integral,
  slip and POD-inspired models; and, added by Vadrot et al., three published
  learned models (two supervised networks and one multi-agent
  reinforcement-learning model), released with the paper. Fowler et al. (2022)
  add the LaRTE model and its composite version with a laminar Stokes-layer
  response.
- **Matching and filtering.** The wall model takes its input at the first
  velocity plane, $h_{\mathrm{wm}}=\Delta y/2$, in both studies. Against
  [log-layer mismatch](/definitions/log-layer-mismatch.md), Fowler et al. (2022,
  §5.1) filter the LES velocity with a wall-parallel spatial filter of width
  twice the grid spacing (after Bou-Zeid et al.), and Vadrot et al. (2023b,
  Table II) filter the equilibrium-model input with a sharp filter of side twice
  the grid spacing.

## Configurations run

- **[Channel flow](/benchmarks/turbulent-channel-flow.md)** (Fowler et al.
  2022, §5.1): domain $8\pi\times2\times3\pi$ in channel half-heights, grid
  $128\times30\times48$, so $(\Delta x^+,\Delta y^+,\Delta z^+)=(196,67,196)$
  at $Re_\tau=1000$; the same grid up to $Re_\tau=5\times10^5$, with the
  wall-model height $h_{\mathrm{wm}}=\delta/30$ ($h^+_{\mathrm{wm}}=33$ at
  $Re_\tau=1000$, 16,667 at $5\times10^5$).
- **Sudden spanwise pressure gradient channel** (Fowler et al. 2022, §5.2):
  initial $Re_{\tau}=1000$, then a spanwise pressure gradient ten times the
  streamwise one; same grid, time step at constant CFL between $10^{-4}$ and
  $4\times10^{-4}\,\delta/u_\tau$, ensembles of five runs.
- **Half channel** (Vadrot et al. 2023b, §II A, §III): $2\pi\delta\times
  2\pi\delta\times\delta$, periodic in the wall-parallel directions, symmetry at
  $y=\delta$, constant pressure gradient; eleven friction Reynolds numbers from
  180 to $10^{10}$ on $24^3$, $48^3$ and $72^3$ grids (one learned model only
  on $32^3$, where neighbouring input planes are $0.03\delta$ apart as in its
  training). Larger domains ($4\pi\times2\pi$, $4\pi\times4\pi$) change the
  mean velocity little at $Re_\tau=5200$ (App. B, Fig. 17).

## Cost data

Vadrot et al. (2023b, §IV D) count 5 operations for the algebraic equilibrium
model and 56, 1609 and 17,412 for the three learned models, quote an overhead of
10–30% of the LES cost for ODE-based equilibrium models from the literature,
and measure the ODE-based equilibrium model at about four times the cost of the
reinforcement-learning model on their cluster (no hardware detail, training
cost excluded).

## Qualifications

- Vadrot et al. (2023b, Table I) list the inputs of one learned model with
  wall-normal derivatives and velocity components in a $y$-wall-normal
  convention, while the paper itself uses $z$ wall-normal; the table follows
  the original model's convention without saying so.
- The two sources describe the code only in the passages summarized above;
  details of time advancement, de-aliasing and parallelization are not given.

# Citations

- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §II A–B, Eqs. (1)–(2), Tables I–II (code, models, matching); §III; §IV D (cost); App. B, Figs. 17–18.
- [Fowler et al. (2022)](/sources/fowler-2022.md) — §5, §5.1–5.2 (code, SGS model, grids, filtering, SSPG set-up).

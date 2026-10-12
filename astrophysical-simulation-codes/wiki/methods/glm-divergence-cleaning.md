---
type: Method
title: "GLM divergence cleaning"
description: "Mixed hyperbolic–parabolic control of the magnetic divergence (Dedner et al. 2002): a scalar ψ couples to the induction equation, carries divergence errors away at speed c_h and damps them; PLUTO's AMR version and Enzo's MUSCL solver use it on cell-centred fields, PLUTO explicitly to avoid the staggered-field transfer operators that constrained transport needs at coarse–fine interfaces."
status: established
aliases: [GLM, Dedner cleaning, Dedner divergence cleaning, generalized Lagrange multiplier, mixed hyperbolic/parabolic divergence cleaning, MUSCL-Dedner]
tags: [mhd, divergence-cleaning, amr, gpu]
timestamp: 2026-10-12T00:00:00Z
---

# GLM divergence cleaning

The generalized Lagrange multiplier (GLM) formulation of Dedner et al.
(2002) keeps all fields cell-centred and adds a scalar $\psi$ to the
system ([Mignone et al. (2012)](/sources/mignone-2012.md), §3, eq. 14):
$$\partial_t\mathbf B - \nabla\times(\mathbf v\times\mathbf B) + \nabla\psi = 0,\qquad \partial_t\psi + c_h^2\,\nabla\cdot\mathbf B = -\frac{c_h^2}{c_p^2}\,\psi .$$
Divergence errors travel away at speed $c_h$ and are damped by the
right-hand side. [Enzo](/software/enzo.md)'s Dedner solver carries
$\psi$ as a ninth conserved variable next to $\rho$, $\rho\mathbf v$, the
total energy and $\mathbf B$ ([Bryan et al. (2014)](/sources/bryan-2014.md),
§4.2, eqs. 48–51).

## Why codes choose it

[PLUTO](/software/pluto.md) offers Powell's eight-wave formulation,
[constrained transport](/methods/constrained-transport.md) (face-centred
field, static grids) and GLM; **its AMR version uses GLM only**. The
stated reasons are that GLM avoids the cost of elliptic cleaning and
the care the staggered field needs in prolongation and restriction at
fine–coarse interfaces (Mignone et al. 2012, §1, §3, §7).

## Discretization in production codes

* **PLUTO (CTU).** The damping term is point-local and
  operator-split; the hyperbolic part rides in the
  [CTU integrator](/methods/unsplit-godunov-integrators.md)
  (Mignone et al. 2012, §2.3, eq. 12; §3.1). With characteristic
  normal predictors the back-projection carries multidimensional source
  terms for $B_x$ and $\psi$ (eq. 31). The characteristic-free
  MUSCL–Hancock predictor needs neither the eigen-decomposition nor the
  $\partial B_x/\partial x$ terms (§3.3, eq. 43).
* **Enzo (MUSCL–Dedner).** Piecewise-linear reconstruction in primitive
  or conservative variables, HLL, HLLC or HLLD fluxes, dimensionally
  unsplit, second-order Runge–Kutta in time (Shu & Osher 1988)
  (Bryan et al. 2014, §4.2). In comoving coordinates this solver uses a
  different comoving field scaling from Enzo's other solvers, and the
  Dedner solver adds a source
  $-\frac{\dot a}{2a}\mathbf B$ to the induction equation (§4.2, end).
* **Choice of $c_h$ and $c_p$.** PLUTO's relativistic rotor transports
  divergence errors "out of the domain at the speed of light", i.e.
  $c_h = 1$ in its units with $c = 1$ (Mignone et al. 2012, §6.3). The
  paper does not state how $c_h$ and $c_p$ are set in Newtonian runs; it
  defers to Mignone & Tzeferacos (2010) (§3). Enzo uses
  a constant $c_h$ and prints no damping coefficient (Bryan et al. 2014,
  §4.2).
* **GPU.** Enzo's Dedner solver is ported to CUDA; driven MHD turbulence
  at $256^3$ cells per node runs about 5× faster per node than on 16
  CPU cores, about 80× a single core (Bryan et al. 2014, §12.3, Fig. 22).

## Evidence

* **[Field-loop advection](/benchmarks/field-loop-advection.md), PLUTO
  AMR.** Base $64\times32$, 2 to 4 levels of ratio 2, WENO + Roe,
  $\nu = 0.4$: the loop keeps about 94 % of its initial
  volume-averaged $\vert\mathbf B\vert^2$ with the fewest levels and about
  98 % with the most (Mignone et al. 2012, §5.2, Fig. 11).
* **Relativistic rotor, PLUTO AMR.** The growth of the mean
  $\vert\nabla\cdot\mathbf B\vert$ stays at the levels of van der Holst et
  al. (2008) (Mignone et al. 2012, §6.3, Fig. 26).
* **[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), Enzo.**
  Dedner and CT give "approximately equal effective resolution"; the
  resolution is not printed (Bryan et al. 2014, §11.2.10, Fig. 14).

Neither source reports a convergence order for its GLM solver.

## Later uses (batch 3)

* **GLM on GPUs for memory.** [gPLUTO](/software/gpluto.md), the OpenACC
  rewrite of PLUTO, offers divergence cleaning (Dedner et al. 2002; Mignone
  et al. 2010) next to Powell's method and upwind
  [constrained transport](/methods/constrained-transport.md)
  ([Rossazza et al. (2026)](/sources/rossazza-2026.md), §2.1). Its
  strong-scaling runs use cleaning "because this algorithm requires less
  device memory than the constrained transport method", which allows a
  slightly larger grid per node; no bytes per cell are printed (§4.1). The
  choice of $c_h$ and $c_p$ is not printed. This adds a GPU-memory reason to
  PLUTO's AMR reason above.
* **gPLUTO strong scaling with GLM** (§4.1–§4.2, Tables 4–5). FP64,
  SSP-RK3, WENOZ, HLLD; six groups of four runs, each spanning an 8-fold
  increase in nodes, up to 256 nodes of 4 GPUs. 3D
  [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md): mean efficiency
  at the largest node count of each group 0.90 (MareNostrum 5, NVIDIA
  Hopper) and 0.89 (Leonardo Booster, A100). 3D
  [circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md):
  the text gives 0.97 (Leonardo) and 0.93 (MareNostrum 5), which Table 5
  does not reproduce under the Table 4 rule. No $\nabla\cdot\mathbf B$
  diagnostic and no accuracy measure is reported for any of these runs.
* **Codes that chose CT instead.** [Cholla](/software/cholla.md) names
  cleaning as an alternative and chooses CT for "its overall accuracy",
  its fit to static structured grids, and the match between GPU efficiency
  and "the algebraic complexity of CT"
  ([Caddy & Schneider (2024)](/sources/caddy-2024.md), §1).
  [IDEFIX](/software/idefix.md) and [AthenaK](/software/athenak.md)
  describe CT only ([Lesur et al. (2023)](/sources/lesur-2023.md), §2.4;
  [Stone et al. (2026)](/sources/stone-2026.md), §3).

# Citations

1. [Mignone et al. (2012)](/sources/mignone-2012.md), §1, §2.3, §3, §3.1, §3.3, §5.2, §6.3, §7.
2. [Bryan et al. (2014)](/sources/bryan-2014.md), §4.2, §11.2.10, §12.3 (arXiv v1).
3. [Rossazza et al. (2026)](/sources/rossazza-2026.md), §2.1, §4.1–§4.2 (arXiv v1).
4. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §1 (arXiv v2).
5. [Lesur et al. (2023)](/sources/lesur-2023.md), §2.4 (arXiv v1).
6. [Stone et al. (2026)](/sources/stone-2026.md), §3 (arXiv v1).

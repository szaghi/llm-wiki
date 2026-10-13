---
type: Method
title: "GLM divergence cleaning"
description: "Mixed hyperbolic–parabolic control of the magnetic divergence (Dedner et al. 2002): a scalar ψ couples to the induction equation, carries divergence errors away at speed c_h and damps them; PLUTO's AMR version and Enzo's MUSCL solver use it on cell-centred fields, PLUTO explicitly to avoid the staggered-field transfer operators that constrained transport needs at coarse–fine interfaces."
status: established
aliases: [GLM, Dedner cleaning, Dedner divergence cleaning, generalized Lagrange multiplier, mixed hyperbolic/parabolic divergence cleaning, MUSCL-Dedner]
tags: [mhd, divergence-cleaning, amr, gpu]
timestamp: 2026-10-13T00:00:00Z
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

## Later uses (batch 9)

### The method in its primary source

[Dedner et al. (2002)](/sources/dedner-2002.md) is the origin of the
formulation above. Its induction and $\psi$ equations (eqs. 4, 19) are
those printed above from Mignone et al. (2012), with the induction flux
written as $\nabla\cdot(\mathbf v\mathbf B - \mathbf B\mathbf v)$.

* **A family of corrections** (§2, eqs. 12–19). The operator linking $\psi$
  to $\nabla\cdot\mathbf B$ may be elliptic (a Poisson projection after
  Brackbill & Barnes, rejected as nonlocal), parabolic
  ($\psi = -c_p^2\nabla\cdot\mathbf B$, a diffusion of the divergence whose
  explicit form limits $c_p$), hyperbolic (a wave equation: errors carried
  away at speed $c_h$) or mixed. The mixed choice is the equation above: a
  telegraph equation in which the damping is a source, so it puts no
  stability limit on $c_p$, and $c_p \to \infty$ recovers the hyperbolic
  case. With the hyperbolic or mixed correction the system stays hyperbolic
  and in conservation form for $\rho$, $\rho\mathbf v$, $\mathbf B$ and $E$
  (p. 650).
* **Choice of $c_h$** (§4, eq. 40, p. 656). The time step is set by the
  Courant number $\nu$ and the largest $\vert v_n\vert + c_f$ alone, and
  $c_h$ is then "the maximal value which is compatible with" it: $\nu$
  times the smallest cell height divided by $\Delta t$, recomputed every
  step and uniform in space. This extends "Choice of $c_h$ and $c_p$"
  above: Enzo's constant $c_h$ departs from the original prescription,
  and PLUTO's $c_h = 1$ in the relativistic rotor is a separate choice; both
  are qualifications, not contradictions.
* **Choice of $c_p$** (eqs. 44–46, p. 657, §5). The damping is applied by
  operator splitting with the exact factor
  $\psi \leftarrow \exp\!\left(-\Delta t\,c_h^2/c_p^2\right)\psi$,
  "unconditionally stable"; this is the operator-split damping PLUTO uses
  above. A constant $c_p$ proved grid- and scheme-dependent, so the ratio
  $c_p^2/c_h$ is fixed instead, at **0.18**, found optimal on the
  peak-in-$B_x$ test "independent of the order and the grid resolution"
  (Fig. 2) and used in all runs. The ratio has the dimension of a length
  (reader's remark at ingestion; the paper does not discuss it), so 0.18
  refers to the test domains of extent 1–2.
* **Riemann problem for the cleaning pair** (eqs. 41–43). In 1D the normal
  field $B_x$ and $\psi$ decouple from the MHD waves and travel at
  $\pm c_h$; the interface values solve a linear $2\times2$ Riemann problem,
  $\tilde B_{x,i+1/2} = \tfrac12(B_x^- + B_x^+) - \tfrac{1}{2c_h}(\psi^+ - \psi^-)$,
  $\tilde\psi_{i+1/2} = \tfrac12(\psi^- + \psi^+) - \tfrac{c_h}{2}(B_x^+ - B_x^-)$
  (superscripts $\mp$ as for $u^\mp_{i+1/2}$),
  and any MHD flux is then evaluated with $\tilde B_{x,i+1/2}$ as its normal field. The
  correction is thus an add-on to an existing solver, on unstructured
  triangles in the paper.
* **EGLM and Powell's terms** (eqs. 20–24, 36). The extended system
  (EGLM), derived from GLM–Maxwell, adds $-(\nabla\cdot\mathbf B)\mathbf B$
  to the momentum equation and $-\mathbf B\cdot\nabla\psi$ to the energy
  equation, starting from (eq. 22)
  $$\mathbf J\times\mathbf B = \nabla\cdot\left(\mathbf B\mathbf B - \tfrac12\vert\mathbf B\vert^2\mathsf I\right) - (\nabla\cdot\mathbf B)\,\mathbf B$$
  (eq. 22 and the sign of the momentum source, eq. 24b, checked by the
  compiler on the page image). Since $\mathbf J\times\mathbf B$ is
  orthogonal to $\mathbf B$, the component of the divergence-form force
  along $\mathbf B$ is $+(\nabla\cdot\mathbf B)\vert\mathbf B\vert$
  (projection by the compiler; Dedner et al. do not state it). EGLM has the
  same eigenvalues as GLM, but its nonconservative terms can violate
  conservation even for divergence-free data. Powell's source terms
  (momentum $-(\nabla\cdot\mathbf B)\mathbf B$, induction
  $-(\nabla\cdot\mathbf B)\mathbf v$, energy $-(\nabla\cdot\mathbf B)\,\mathbf v\cdot\mathbf B$)
  instead advect the errors with the flow.
* **Convergence order** (§5, Table II). On the Dai–Woodward 1D Riemann
  problem run in 2D with a first-order scheme, the $L_1$ error of mixed GLM
  falls from 6.45517676 to 0.22792806 over 1,024 to 1,048,576 elements, with
  experimental orders 1.061, 0.875, 0.804, 1.069, 1.014; mixed EGLM is
  similar; Powell's terms degrade (0.880, 0.622, 0.432) and fail on the two
  finest grids with negative pressures. This qualifies the statement under
  Evidence that no source reports a convergence order for its GLM solver:
  the original does, for a first-order solver on a discontinuous problem.
* **Recommendation** (§5–6). Mixed GLM over mixed EGLM, hyperbolic GLM,
  Powell's terms and no correction: smallest divergence errors, no loss of
  conservation, robustness on a shock reflection, a 2D MHD Riemann problem
  and an MHD Kelvin–Helmholtz flow, where the uncorrected scheme fails or
  costs about 50 % more time. Applicability "on arbitrary grids in 2D and
  3D" is stated; the tests are 2D only. The paper's motivation — local,
  explicit, usable with "any existing MHD solver ... on arbitrary grids" —
  agrees with PLUTO's AMR reason above.

# Citations

1. [Mignone et al. (2012)](/sources/mignone-2012.md), §1, §2.3, §3, §3.1, §3.3, §5.2, §6.3, §7.
2. [Bryan et al. (2014)](/sources/bryan-2014.md), §4.2, §11.2.10, §12.3 (arXiv v1).
3. [Rossazza et al. (2026)](/sources/rossazza-2026.md), §2.1, §4.1–§4.2 (arXiv v1).
4. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §1 (arXiv v2).
5. [Lesur et al. (2023)](/sources/lesur-2023.md), §2.4 (arXiv v1).
6. [Stone et al. (2026)](/sources/stone-2026.md), §3 (arXiv v1).
7. [Dedner et al. (2002)](/sources/dedner-2002.md), §§1–6, eqs. 4–49, Tables I–II, Fig. 2.

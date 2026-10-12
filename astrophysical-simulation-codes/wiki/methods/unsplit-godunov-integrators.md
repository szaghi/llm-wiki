---
type: Method
title: "Unsplit Godunov integrators"
description: "Second-order, directionally unsplit time integrators of the astrophysical Godunov codes — corner transport upwind (CTU) with characteristic tracing, the van Leer / MUSCL–Hancock predictor–corrector (VL, VL2) and method-of-lines SSP Runge–Kutta — with their Riemann-solve counts, Courant limits, and the evidence the codes give against dimensional splitting."
status: established
aliases: [CTU, corner transport upwind, CTU+CT, VL+CT, VL2, van Leer integrator, MUSCL-Hancock, method-of-lines Runge-Kutta, unsplit integrator]
tags: [time-integration, unsplit, hydro, mhd, constrained-transport]
timestamp: 2026-10-12T00:00:00Z
---

# Unsplit Godunov integrators

An unsplit integrator updates all directions from one state per stage,
instead of sweeping direction by direction. The codes of this bundle use
three families, all formally second order in space and time.

| Code | Integrators | Source |
|---|---|---|
| [Athena](/software/athena.md) | CTU+CT (2D; 3D six-solve), VL+CT | [Stone et al. (2008)](/sources/stone-2008.md), §1, §5–6 |
| [Athena++](/software/athena-plus-plus.md) | method of lines: RK1, VL2 (default), SSPRK(2,2), SSPRK(3,3); no CTU | [Stone et al. (2020)](/sources/stone-2020.md), §3.2.3 |
| [PLUTO](/software/pluto.md) | CTU, six Riemann solves per zone in 3D | [Mignone et al. (2012)](/sources/mignone-2012.md), §3.1 |
| [Castro](/software/castro.md) | unsplit PPM with characteristic tracing and full corner coupling | [Almgren et al. (2010)](/sources/almgren-2010.md), §5 |
| [GAMER](/software/gamer.md) | CTU+CT and VL+CT | [Zhang et al. (2018)](/sources/zhang-2018.md), §3.2 |
| [Enzo](/software/enzo.md) | MUSCL–Dedner with RK2; MHD-CT on MUSCL–Hancock; PPM and ZEUS are split | [Bryan et al. (2014)](/sources/bryan-2014.md), §4 |
| Hyperion ([Athena](/software/athena.md) module) | VL for radiation; VL or CTU for the gas | [Skinner & Ostriker (2013)](/sources/skinner-2013.md), §3.3–3.4 |

## Corner transport upwind (CTU)

Colella's (1990) corner transport upwind scheme builds time-centred
interface states by characteristic tracing over $\Delta t/2$, corrects
them with transverse flux gradients, and solves a second set of Riemann
problems.
* **Athena 2D CTU+CT** (Stone et al. 2008, §5.1, steps 1–11, Fig. 4):
  reconstruct and solve Riemann problems in $x$ and $y$; build corner
  EMFs; correct the interface states by $\Delta t/2$ with transverse flux
  gradients plus $\nabla\cdot\mathbf B$ source terms, and advance the
  in-plane face fields by $\Delta t/2$ with
  [CT](/methods/constrained-transport.md); solve the Riemann problems
  again (H-correction if needed); rebuild corner EMFs; update. The scheme
  reduces exactly to the 1D algorithm for grid-aligned flow.
* **Athena 3D.** Full CTU (Saltzman 1994) needs 12 Riemann solves per
  cell per step for stability up to $\nu \le 1$. Athena's primary 3D
  integrator is a six-solve variant, stable only for $\nu \le 1/2$; it
  was found "as accurate as the twelve-solve method" at about the same
  cost and "dramatically simpler to implement". With two transverse
  terms in 3D, the $\nabla\cdot\mathbf B$ source terms are minmod-limited
  (§6, eqs. 88–89, 95). The 3D scheme reduces exactly to 2D or 1D for
  flows with that symmetry (§6, §9).
* **Characteristic tracing in Athena.** Reconstruction is in primitive
  variables with slope limiting in characteristic variables: PLM with the
  monotonized-central limiter (eq. 38), or PPM after Colella & Woodward
  (1984) (eqs. 46–60), with the Colella–Sekora extremum-preserving
  limiters as an option. For HLL-family solvers PLM adds a correction for
  waves moving away from the interface (eqs. 44–45); without it the flux
  would be first order. It is not added for the Roe or exact solvers
  (§4.2.2). PPM lowers the error amplitude but not the formal order (§4.2.3).
* **PLUTO** (Mignone et al. 2012, §3.1, eqs. 15–21). CTU after Mignone &
  Tzeferacos (2010), six Riemann solves per zone in 3D. The corner-coupled
  states add $\Delta t/2$ times the transverse hyperbolic increments, from
  first-order Godunov fluxes between cell-centred states, and the
  parabolic increments, from second-order central differences (eqs.
  19–21). Viscosity, resistivity and thermal conduction thus enter
  unsplit; cooling, chemistry and the GLM damping are operator-split.
  Stability: $\nu \le 1$ in 2D, $\nu \le 1/2$ in 3D, with $\nu$ equal to
  $\Delta t$ times the cell maximum of the largest directional
  $\max_p\vert\lambda^{(p)}\vert/h$ plus the sum over directions of twice the largest diffusion
  coefficient over $h^2$ (eq. 23).
* **PLUTO normal predictors.** Characteristic tracing (eqs. 25–31) with
  PPM, third-order improved WENO or TVD linear reconstruction; both
  classical reference-state choices may reduce formal second order in
  smooth flow, which taking the reconstructed interface value as
  reference avoids (§3.2). Alternatively a characteristic-free primitive
  MUSCL–Hancock half step (eqs. 43–44), the default for relativistic MHD
  (§3.3, §6).
* **Castro** (Almgren et al. 2010, §5.2). PPM on primitive variables with
  the Colella–Sekora / McCorquodale–Colella limiter, characteristic
  tracing over the domain of dependence of each wave (eqs. 30–32), source
  terms (gravity included) added in the tracing, and full 3D corner
  coupling "exactly as given in Section 4.2.1 in Miller & Colella (2002)"
  (not reproduced). The flux is "formally second-order in both space and
  time" (§5). Reactions are Strang-split around the hydro step (eqs.
  12a–c), and gravity is time-centred by a predictor–corrector (§5.1).
* **GAMER** (Zhang et al. 2018, §3.2). CTU+CT in 8 steps after Athena;
  it is "generally less diffusive than the VL scheme due to the
  transverse flux gradient correction", so all GAMER accuracy tests use
  it.

## Van Leer predictor–corrector (VL, VL2, MUSCL–Hancock)

* **Athena.** VL+CT, a MUSCL–Hancock-like predictor–corrector, needs no
  characteristic tracing and no eigen-decomposition, which the authors
  call a better fit for complex physics such as relativistic MHD
  (Stone et al. 2008, §1, §4.2; details in Stone & Gardiner 2009).
  CTU+CT is "generally less diffusive and more accurate"; VL+CT "has
  definite advantages" for some applications (§1).
* **Athena++ VL2.** Written in the low-storage form of Ketcheson (2010),
  the printed coefficients give
  $$u^{n+1/2} = u^n + \tfrac{\Delta t}{2}\,\mathcal L(u^n),\qquad u^{n+1} = u^n + \Delta t\,\mathcal L(u^{n+1/2}),$$
  where the predictor must use first-order (donor-cell) fluxes
  (Stone et al. 2020, §3.2.3, eqs. 11–15). Courant limit $\nu = 1$ in 1D
  and $\nu = 1/2$ in 2D and 3D; positive-definite for $\nu \le 1/3$ with
  first-order fluxes in both steps.
* **GAMER VL+CT** (7 steps): first-order fluxes with the longitudinal
  field set to its face value, edge EMFs, $\Delta t/2$ predictor,
  reconstruction at the half step, Riemann solve, edge EMFs, full update
  (Zhang et al. 2018, §3.2).
* **Hyperion.** The radiation subsystem uses Athena's VL with PLM and an
  HLL flux; the gas uses VL or CTU; the Courant number is "usually 0.4"
  for VL ([Skinner & Ostriker (2013)](/sources/skinner-2013.md), §3.1,
  eqs. 29–32; §3.3–3.4).
* **Enzo MHD-CT** builds on the Godunov scheme of Li et al. (2008) with
  "both MUSCL-Hancock and Piecewise Linear Method" reconstruction
  ([Bryan et al. (2014)](/sources/bryan-2014.md), §4.3).

## Method-of-lines Runge–Kutta

Athena++ drops CTU because the characteristic projection is too complex
for relativity and integrates $\frac{d}{dt}u = \mathcal L(u)$ instead
(Stone et al. 2020, §3.2.3):
* SSPRK(2,2) and SSPRK(3,3) have SSP coefficient 1, hence $\nu = 1$, the
  same as RK1, which is stable only with donor-cell fluxes. In practice
  $\nu = 1$ works for RK2 and RK3 with PLM and PPM on most problems. The
  framework also admits 2S and 3S* low-storage methods such as RK4()4[2S].
* Recommended pairs: RK1 with donor cell (testing), VL2 or RK2 with PLM
  or PPM, RK3 with PPM.
* On [linear waves](/benchmarks/linear-wave-convergence.md) the error is
  strictly second order whenever VL2 or PLM is used; RK3+PPM errors are
  at least 10× lower than VL2+PLM and some families approach third order, attributed
  to temporal errors dominating (§3.3.1, Fig. 11).
* Enzo's MUSCL–Dedner solver is dimensionally unsplit with the
  second-order Runge–Kutta of Shu & Osher (1988)
  (Bryan et al. 2014, §4.2).

## Against dimensional splitting

* **Rayleigh–Taylor.** In Castro all three dimensionally split variants
  (PLM, old PPM, new PPM) produce spurious secondary instabilities,
  attributed to alternating compression and expansion between sweeps in
  regions of varying strain. Unsplit PLM and old PPM show mild anomalies
  at bubble and spike tips; unsplit new PPM is cleanest
  (Almgren et al. 2010, §8.3, Fig. 9;
  [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)).
* **Liska–Wendroff implosion.** A jet along the diagonal forms with
  Athena's unsplit integrator but not with split ones; the authors
  conclude the jet is correct (Stone et al. 2008, §8.3, Fig. 17).
  Athena++ keeps the problem symmetric to double-precision machine
  epsilon, which requires direction-unbiased stencils and value-safe
  floating point (no reassociation, no FMA contraction)
  (Stone et al. 2020, §3.3.5, Fig. 17).
* **Split schemes still in use.** Enzo's PPM is direct-Eulerian and
  dimensionally split, with interface states "third-order accurate in
  space and second-order accurate in time" and the multi-D scheme
  "formally second-order accurate in space and time"; its ZEUS scheme is
  operator-split and "first-order accurate in time"
  (Bryan et al. 2014, §2.2.2, §4.1, §4.4).

## Cost

* Athena's unsplit integrator stores left and right states and fluxes at
  every interface of the 3D grid, which raises memory use and lowers cache
  performance (Stone et al. 2008, §7).
* Castro's unsplit scheme costs about 2× the CPU time and memory of the
  split one in 2D; in 3D slightly less than 2× the CPU time and under
  10 % more memory, thanks to strip-mining (Almgren et al. 2010, §8.3).

## Time-step definitions

The codes define the Courant number differently, so the printed limits
are not directly comparable:
* Athena 2D: $\Delta t = \nu\min\!\left(\frac{h}{\vert v_x\vert + c_{f,x}},\ \frac{h}{\vert v_y\vert + c_{f,y}}\right)$
  with $\nu \le 1$ (eq. 78); $\nu \le 1/2$ for the 3D six-solve CTU
  (eq. 95) (Stone et al. 2008, with $c_{f,x}$ the fast speed in $x$; the
  paper allows a different cell size per direction).
* Castro: the minimum over directions of $h/(\vert v_d\vert + c_s)$,
  times $\nu \in (0,1)$ (Almgren et al. 2010, §5.1, eqs. 23–24).
* PLUTO: the largest directional advective rate plus a sum of diffusive
  rates (eq. 23, above).
* Enzo: a harmonic sum of the directional steps, "yields a maximum"
  Courant number of 0.8; as printed, eq. 95 applies the Courant factor to
  steps that already contain it (Bryan et al. 2014, §9, eqs. 88, 95).

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §1, §4.2, §5.1, §6, §7, §8.3.
2. [Stone et al. (2020)](/sources/stone-2020.md), §3.2.3, §3.3.1, §3.3.5.
3. [Mignone et al. (2012)](/sources/mignone-2012.md), §3.1–3.3, §6.
4. [Almgren et al. (2010)](/sources/almgren-2010.md), §5, §5.1–5.2, §8.3 (arXiv v1).
5. [Zhang et al. (2018)](/sources/zhang-2018.md), §3.2 (arXiv v4).
6. [Bryan et al. (2014)](/sources/bryan-2014.md), §2.2.2, §4.1–4.4, §9 (arXiv v1).
7. [Skinner & Ostriker (2013)](/sources/skinner-2013.md), §3.1, §3.3–3.4 (arXiv v1).

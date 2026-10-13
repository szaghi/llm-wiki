---
type: Method
title: "Unsplit Godunov integrators"
description: "Second-order, directionally unsplit time integrators of the astrophysical Godunov codes — corner transport upwind (CTU) with characteristic tracing, the van Leer / MUSCL–Hancock predictor–corrector (VL, VL2) and method-of-lines SSP Runge–Kutta — with their Riemann-solve counts, Courant limits, and the evidence the codes give against dimensional splitting."
status: established
aliases: [CTU, corner transport upwind, CTU+CT, VL+CT, VL2, van Leer integrator, MUSCL-Hancock, method-of-lines Runge-Kutta, unsplit integrator, SSP-RK3, IMEX Runge-Kutta]
tags: [time-integration, unsplit, hydro, mhd, constrained-transport, gpu]
timestamp: 2026-10-13T00:00:00Z
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
* Castro: the minimum over directions of $h/(\vert v_x\vert + c_s)$ and its $y$, $z$ analogues,
  times $\nu \in (0,1)$ (Almgren et al. 2010, §5.1, eqs. 23–24).
* PLUTO: the largest directional advective rate plus a sum of diffusive
  rates (eq. 23, above).
* Enzo: a harmonic sum of the directional steps, "yields a maximum"
  Courant number of 0.8; as printed, eq. 95 applies the Courant factor to
  steps that already contain it (Bryan et al. 2014, §9, eqs. 88, 95).

## Later uses (batch 3)

The GPU codes of batch 3 use method-of-lines Runge–Kutta, except
[Cholla](/software/cholla.md), which uses VL+CT. None of the batch-3 papers runs CTU.

| Code | Integrators | Source |
|---|---|---|
| [AthenaK](/software/athenak.md) | method of lines, low-storage SSP RK1–RK4 (Ketcheson 2010); IMEX RK for stiff sources; no CTU | [Stone et al. (2026)](/sources/stone-2026.md), §3, §3.4 |
| [IDEFIX](/software/idefix.md) | method of lines: Euler, TVD RK2 and RK3 (Gottlieb & Shu 1998); RKL [super time stepping](/methods/super-time-stepping.md) for parabolic terms | [Lesur et al. (2023)](/sources/lesur-2023.md), §2.7–2.8 |
| [Cholla](/software/cholla.md) | VL+CT (Stone & Gardiner 2009), default in place of CTU | [Caddy & Schneider (2024)](/sources/caddy-2024.md), §2.2 |
| [gPLUTO](/software/gpluto.md) | method of lines, SSP-RK3 (Shu & Osher 1988) | [Rossazza et al. (2026)](/sources/rossazza-2026.md), §2.2 |
| [Quokka](/software/quokka.md) | method of lines, RK2-SSP | [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.2.1 |
| [GRaM-X](/software/gram-x.md) | method of lines, RK2 or RK4, shared with the spacetime evolution | [Shankar et al. (2023)](/sources/shankar-2023.md), §II C, §IV |
| [ADAM](/software/adam.md) (NASTO) | method of lines, three-stage third-order SSP RK (finite-difference WENO) | [Zaghi et al. (2023)](/sources/zaghi-2023.md), §3.1 |
| [STREAmS](/software/streams.md) | three-stage third-order low-storage RK of Spalart, Moser & Rogers (1991) (finite differences) | [Bernardini et al. (2021)](/sources/bernardini-2021.md), §2.2 |

ADAM/NASTO and STREAmS are finite-difference codes, not Godunov
finite-volume codes; they enter this page only as method-of-lines data
points.

### Method of lines

* **AthenaK** keeps the Athena++ method of lines with Ketcheson's
  low-storage SSP integrators, RK1 through RK4. CTU is not implemented,
  because it "does not extend easily to the relativistic equations of
  motion", the reason Athena++ gave. Reconstruction (PLM, PPM4, PPMX,
  WENOZ) is always on primitive variables; characteristic reconstruction
  "has not yet been implemented" ([Stone et al. (2026)](/sources/stone-2026.md),
  §3). Diffusive fluxes are added to the hyperbolic flux and computed
  explicitly at every stage, not operator split (§3.3). On 1D hydro linear
  waves, RK3 with PPMX or WENOZ converges at fourth order until nonlinear
  effects or round-off take over, while PLM and PPM4 converge at second
  order (§3.1, Fig. 1); in MHD the fast wave converges only at second
  order "even in one-dimension" (§3.2, Fig. 3).
* **IMEX in AthenaK.** The two-fluid ion–neutral drag is integrated with
  the second- and third-order IMEX schemes of Pareschi & Russo (2005;
  printed "Pareshi") or the positivity-preserving scheme of Krapp et al.
  (2024). In a stiff two-fluid relaxation test the Pareschi–Russo IMEX2
  overshoots and then oscillates, while the Krapp et al. variant
  "smoothly converges" (§3.4, Fig. 7 left; qualitative).
* **IDEFIX** combines whole Euler sub-steps (reconstruction, Riemann
  solve, CT and the update) with fixed weights: Euler; RK2, whose second stage
  takes 1/2 of the new Euler step and 1/2 of the initial state; RK3, with
  1/4 and 3/4 at the second stage and 2/3 and 1/3 at the third — the TVD RK of Gottlieb & Shu (1998)
  ([Lesur et al. (2023)](/sources/lesur-2023.md), §2.7, eq. 9, Table 1).
  The paper does not call the scheme unsplit; the stage structure (all
  directions from the same state, one combination per stage) implies it.
  Reconstruction is on primitive variables without characteristic
  decomposition, and the code is "at most globally second order" whatever
  the reconstruction (§2.3, footnote 1). Parabolic terms can be sub-cycled
  with second-order RKL stages placed before and after the main
  integrator to keep second order in time (§2.8; see
  [super time stepping](/methods/super-time-stepping.md)).
* **gPLUTO** runs SSP-RK3 with WENOZ or parabolic reconstruction of
  primitive variables and HLLD
  ([Rossazza et al. (2026)](/sources/rossazza-2026.md), §2.2, eq. 5,
  §4.1). Its $\mathcal L$ in eq. 5 already contains the factor
  $\Delta t$, so it is $\Delta t\,\mathcal L$ in the registry's notation;
  eq. 4 as printed carries $\Delta t/h$ in a time derivative (recorded as
  printed). The paper says gPLUTO "offers a variety of
  algorithms"; only SSP-RK3 is used in its runs.
* **Quokka** uses RK2-SSP. Method of lines with higher-order
  reconstruction is unstable with forward Euler and stable with RK of
  order at least 2, "the same finding" as Athena++; single-step
  characteristic-tracing PPM does not have this problem
  ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.2.1). This
  agrees with the Athena++ statement above that RK1 is stable only with
  donor-cell fluxes. The method of lines couples corners through the
  stages rather than through diagonal fluxes, and formally needs a smaller
  step than CTU by a factor $1/d$; the authors still call it more robust,
  citing CTU instabilities in supersonic turbulence with strong cooling
  unless the Courant number is below about 0.1 (Schneider & Robertson
  2017) (§2.2.1).
* **GRaM-X** advances fluid and spacetime with the same RK2 or RK4
  ([Shankar et al. (2023)](/sources/shankar-2023.md), §II C); one global
  time step on all AMR levels, so no refluxing is needed (§III A, §III C).
* **ADAM/NASTO** writes a three-stage third-order SSP RK in Butcher form
  (eq. 7 prints a single-index coefficient $a_l$ with no stage dependence,
  recorded as printed) with one global time step for all levels
  ([Zaghi et al. (2023)](/sources/zaghi-2023.md), §3.1, eqs. 6–9).
* **STREAmS** prints the Spalart–Moser–Rogers coefficients as
  $(0, 17/60, -5/12)$ and $(8/15, 5/12, 3/4)$; with $+17/60$ as printed the
  weights do not sum to 1, while the standard scheme has $-17/60$ (the
  cited original was not checked; recorded as printed)
  ([Bernardini et al. (2021)](/sources/bernardini-2021.md), §2.2, eq. 11).
  Its time-step analysis in wall units finds the explicit compressible
  step always more restrictive than the incompressible one, "easily
  exceeding an order of magnitude" at low Mach number (§2.2, eqs. 12–14).

### Van Leer + CT in Cholla

[Caddy & Schneider (2024)](/sources/caddy-2024.md) (§2.2) make Stone &
Gardiner's VL+CT the default of [Cholla](/software/cholla.md), replacing
the CTU of Schneider & Robertson (2015), because it is "more robust than
the CTU algorithm" described there; they call it "very similar in
structure to the MUSCL-Hancock integrator". The step: time step;
piecewise-constant interface states; HLLD; edge EMFs; half-step update of
$u$ and the face fields; PLM or PPM reconstruction at the half step;
HLLD; edge EMFs; full update; then operator-split extra physics in
"first order operator-split fashion" and the ghost exchange (§2.2,
steps 1–10). This matches GAMER's 7-step VL+CT above. Further
statements:
* The piecewise-constant predictor is "too diffusive to be used on its
  own in both reconstruction steps" but "excellent for debugging"
  (§2.2.2).
* PPM is "formally second order" inside this integrator and "does not
  improve the overall order of convergence" (§2.2.6); on 3D linear waves
  it lowers the error about tenfold at unchanged order (§3.1.1).
* The MHD blast wave becomes unstable when the plasma beta is lowered
  tenfold from 0.2 to 0.02, "like Stone & Gardiner (2009)" (§3.1.5). The
  "robust for low-β flows" statement of Stone et al. (2008) concerns
  CTU+CT on the isothermal blast at the same beta 0.02, so this qualifies,
  and does not contradict, it: different integrator and equation of
  state.

### Time-step definitions (batch 3)

The new codes add more Courant-number conventions; the printed limits
are again not directly comparable:
* AthenaK: $\Delta t \le \nu\min\left(h/\max_p\vert\lambda^{(p)}\vert\right)$,
  the minimum taken over all cells and all directions with the largest
  signal speed of each direction, and "Generally we use CFL ≤ 1/Ndim",
  i.e. $\nu \le 1/d$ ([Stone et al. (2026)](/sources/stone-2026.md), §3,
  eq. 3). Explicit diffusion adds a limit proportional to $h^2$ divided by
  $2d$ times the diffusion coefficient (eq. 10).
* Athena++ states $\nu = 1$ for RK2 and RK3 (above). AthenaK's
  $\nu \le 1/d$ is a usage convention ("Generally we use"), not a
  stability claim. The open question is Athena++'s $\nu = 1$ against
  Quokka's bound below; see Contradictions.
* Quokka: a stability-polynomial analysis bounds the step by the cell
  maximum of the sum over directions of the directional signal speed
  (eq. 19); since that bound is only necessary, the code uses the more
  conservative $\Delta t = \nu\,h/\max(\vert\mathbf v\vert + c_s)$ and
  defines the Courant number $\nu$ as a stability coefficient divided by
  $d$ (eqs. 20–21). The coefficient is 1 for forward Euler and RK2-SSP on
  linear constant-coefficient systems, so the largest stable $\nu$ for
  RK2-SSP in 3D is 1/3; using $\max(\vert\mathbf v\vert + c_s)$ without
  the factor $d$ can violate eq. 19 (footnote 3)
  ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.2.1).
* IDEFIX: $\Delta t$ equals $\nu < 1$ divided by the cell maximum of the
  sum over directions of the largest signal speed over $h$ plus twice the
  largest diffusion coefficient over $h^2$, a point-wise combination of
  hyperbolic and parabolic limits after Beckers (1992) (eq. 10). IDEFIX
  states that PLUTO's Courant number carries a dimension prefactor (its
  $\nu$ equals $d$ times PLUTO's) and that PLUTO computes global
  hyperbolic and parabolic steps separately, so the IDEFIX step "can be
  somewhat larger" ([Lesur et al. (2023)](/sources/lesur-2023.md), §2.7).
  IDEFIX cites for this an orbital-advection paper of Mignone et al.
  (2012, A&A), not the PLUTO-AMR paper behind eq. 23 above, which
  combines both rates in one Courant number; the two descriptions may
  refer to different PLUTO modules or versions. Recorded as a
  qualification, not a contradiction.
* Cholla: $\Delta t = \nu\min\left(\frac{h}{\vert v_x\vert + c_f},\ \frac{h}{\vert v_y\vert + c_f},\ \frac{h}{\vert v_z\vert + c_f}\right)$
  over the grid (eq. 11, which allows a different cell size per direction
  and prints a single $c_f$, with only $B_x$ in eq. 12). VL+CT is
  "formally" limited to $\nu \le 0.5$, "though that is an estimate";
  in practice it is unstable at 0.5 and stable at 0.4, and runs typically
  use 0.3 "to improve the accuracy of the operator splitting"
  ([Caddy & Schneider (2024)](/sources/caddy-2024.md), §2.2.1,
  footnote 4). This is a measured practical limit below the 1/2 stated
  for Athena++'s VL2 in 2D and 3D (above); the two are different
  formulations of the van Leer integrator in different codes, so it is
  a qualification.
* GRaM-X (relativistic units) defines the Courant number as $\Delta t/h$:
  0.8 in its 1D shock tubes and 0.25 in 2D and 3D, with RK4
  ([Shankar et al. (2023)](/sources/shankar-2023.md), §IV).
* ADAM/NASTO: a local Courant number, the largest of the three
  directional $\vert v\vert + c_s$ over the smallest cell size, times
  $\Delta t$, and one global step from the local conditions (eqs. 8–9);
  the value used is not printed (Zaghi et al. 2023, §3.1).
* gPLUTO prints no Courant number (Rossazza et al. 2026).

### Symmetry and floating point

Quokka recovers the exactly symmetric
[Liska–Wendroff implosion](/benchmarks/liska-wendroff-implosion.md) on
NVIDIA GPUs only with symmetrically coded RK2-SSP flux sums and `nvcc`
option `fmad=false`, extending to GPUs the Athena++ requirement of
value-safe floating point without fused multiply–add contraction recorded
above ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3.1.9).

### Cost on GPUs

AthenaK's MHD runs about two times slower than hydro per cell, attributed
to the Riemann solver and CT ([Stone et al. (2026)](/sources/stone-2026.md),
§5.1, Table 2). GRaM-X's throughput drops about 1.8 times from ideal gas
with RK2 to tabulated EOS with RK4 (twice the stages; two changes at
once) ([Shankar et al. (2023)](/sources/shankar-2023.md), §V A).

## Later uses (batch 4)

| Code | Integrators | Source |
|---|---|---|
| [TIGRESS](/software/tigress.md) ([Athena](/software/athena.md) modules) | VL+CT (Stone & Gardiner 2009) with PLM and Roe | [Kim & Ostriker (2017)](/sources/kim-2017.md), §2.1 |

* **A production MHD use of Athena's VL+CT.**
  [Kim & Ostriker (2017)](/sources/kim-2017.md), §2.1, run the
  predictor–corrector of Stone & Gardiner (2009) with piecewise-linear
  reconstruction, the Roe solver and
  [constrained transport](/methods/constrained-transport.md) for
  supernova-driven, self-gravitating shearing-box turbulence. Two
  safeguards are added: the H-correction where the signal-speed difference
  exceeds 20 km s⁻¹, and the first-order flux correction of Lemaster &
  Stone (2009) in cells with negative density or pressure after the
  second-order update (see
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)).
  Cooling is operator-split before the integrator step. No integrator
  comparison is made, and the Courant number is not stated.
* **Particles in the same step.** Sink/star particles are advanced with a
  symplectic kick–drift–kick: each step begins
  with the previous step's second kick, and particle positions are
  advanced before the MHD step (§2.2.2, §2.2.5; see
  [sink particles](/methods/sink-particles.md)).

## Later uses (batch 6)

### 2D CTU+CT in its primary source

[Gardiner & Stone (2005)](/sources/gardiner-2005.md) (arXiv v1 read)
construct the 2D CTU+CT that Athena implements (Corner transport upwind,
above). Their single-step scheme combines [PPM](/methods/ppm.md) interface
states, Colella's CTU and face-centred
[constrained transport](/methods/constrained-transport.md), in eight steps
(§4.3): PPM interface states with multidimensional terms; Riemann solve;
contact-upwinded corner EMFs; transverse correction with source terms;
second Riemann solve; corner EMFs at $t^{n+1/2}$; CT update of the face
fields; finite-volume update of the rest. It is "second order accurate,
unsplit, and preserves the $\nabla\cdot\mathbf B = 0$ constraint throughout
the time step", and reduces exactly to 1D PPM for plane-parallel
grid-aligned flow.

* **Against dimensional splitting** (§1, §2.1). For MHD with a
  cell-centred field, split updates "will not generally satisfy the
  divergence free constraint between directional sweeps"; this is the
  stated reason for an unsplit integrator, an MHD argument alongside the
  hydrodynamic ones of the section on splitting above.
* **Multidimensional terms in the characteristic step** (§3.1, eqs. 25–33).
  In 2D the primitive induction equation keeps terms in the normal
  derivative of the normal field that vanish in 1D. The $x$-direction
  characteristic evolution adds $v_y\,\partial_xB_x$ to the $B_y$
  equation, evaluated as $v_{y,i}(B_{x,i+1/2} - B_{x,i-1/2})/h$ from the face
  values (eq. 32), and the $y$ sweep adds $v_x\,\partial_yB_y$ to the $B_x$
  equation; the normal field at an interface is the face value, not
  reconstructed. Without these terms "the field loop disintegrates in
  oscillations before completing a fraction of an orbital period"
  (§3.3.1). These terms are distinct from the source terms of the
  transverse step below.
* **What hydrodynamic CTU lacks** (§4.1). The hydrodynamic transverse
  correction (eqs. 57–60) "fail[s] to preserve the $\nabla\cdot\mathbf B = 0$
  condition". Two changes: the face fluxes are integrated to the corners
  with a CT EMF, equivalent to advancing the face normal fields to
  $t^{n+1/2}$ by CT (eqs. 65–70); and the states receive $\Delta t/2$ times
  (eqs. 61–64, 72–73)
  $$s_{x,i,j} = \left(0,\ B_x,\ B_y,\ B_z,\ 0,\ 0,\ v_z,\ B_zv_z\right)^{\mathsf T}_{i,j}\ \frac{B_{x,i+1/2,j} - B_{x,i-1/2,j}}{h}$$
  in the conserved order $(\rho, \rho\mathbf v, \mathbf B, E)$, and its
  analogue in $y$, needed because primitive interface states are not
  formally advanced by $\Delta t/2$ (eq. 71). These are numerical terms,
  not physical sources. The $v_z\,\partial_xB_x$ term is placed here and
  not in the characteristic step; otherwise a loop advected with uniform
  $v_z$ grows a spurious coherent $B_z$ (§4.1.2). This is the origin of the
  "$\nabla\cdot\mathbf B$ source terms" of Athena's 2D CTU+CT above.
* **Corrector EMF** (§4.2, eqs. 74–78). The reference EMF
  $v_yB_x - v_xB_y$ is evaluated at $t^{n+1/2}$ from the half-step face
  fields and a half-step finite-volume update of density and momenta.
* **Riemann solver and the H-correction.** All tests use the Roe solver
  of Cargo & Gallice (1997); no carbuncle fix is mentioned. The
  "H-correction if needed" in Athena's step list above is not part of the
  2005 description.
* **Time step.** A Courant number is printed only for the first-order
  scheme, $\Delta t = 0.4\min\left(h/\max_p\vert\lambda^{(p)}_x\vert,\ h/\max_p\vert\lambda^{(p)}_y\vert\right)$
  with the directional maxima of the eigenvalue moduli (eq. 52); none is
  printed for the CTU+CT tests. This neither agrees nor disagrees with the
  $\nu \le 1$ of Athena's eq. 78 (Time-step definitions, above).
* **PLM against PPM** (§5.4, Fig. 11). On 2D linear waves the CTU+CT
  scheme with PPM converges at fitted orders 2.0 (fast), 2.26 (Alfvén),
  2.29 (slow) and 2.11 (entropy); with PLM every mode scales as $N^{-2}$
  with a slightly larger error. This agrees with the statement above that
  PPM lowers the error amplitude, not the formal order. See
  [linear wave convergence](/benchmarks/linear-wave-convergence.md).
* **Low β.** The 2D adiabatic Londrillo & Del Zanna blast wave at ambient
  plasma beta 0.02 runs "stable and accurate" with CTU+CT (§5.6). The
  Cholla instability at the same beta (Van Leer + CT in Cholla, above)
  concerns VL+CT in 3D, so this is a further qualification, not a
  contradiction; see [MHD blast wave](/benchmarks/mhd-blast-wave.md).
* **Scope.** 2D only; the 3D extension "principally involves
  modifications to the 'source terms'" and is deferred (§6). The scheme is
  called "ideally suited" to static or adaptive refinement (§1, §6),
  stated without a demonstration.

## Later uses (batch 8)

### CTU in its primary source

[Colella (1990)](/sources/colella-1990.md) is the origin of the corner
transport upwind scheme summarized under Corner transport upwind (CTU),
above. Its 2D construction agrees with that summary and adds:

* **Where the name comes from** (§1, eqs. 1.2–1.6, Figs. 1–2). The
  first-order scheme for linear advection integrates the upstream data
  over the region the characteristics sweep through each edge, corners
  included. Its limit is the per-direction maximum,
  $\max(v_x\Delta t/h,\ v_y\Delta t/h) \le 1$ (sufficient), where unsplit
  donor cell, without the transverse term, needs
  $v_x\Delta t/h + v_y\Delta t/h \le 1$ (necessary).
* **"A second set of Riemann problems" is literal** (§2, eqs. 2.13–2.15).
  The transverse correction is an upwind difference of fluxes from
  transverse Riemann problems, solved either between cell-centred states
  (eq. 2.13, first-order Godunov transverse fluxes, "sufficiently
  accurate ... to yield an algorithm that is second-order accurate") or
  between the normal-predictor states of the transverse edges (eq. 2.15);
  the edge Riemann problem follows. The count is twice that of the split
  scheme (§6).
* **Design requirements** (p. 173): reduction to the 1D Colella–Woodward
  method for grid-aligned 1D problems, equal linear Courant limits for the
  unlimited and fully limited schemes and for the split scheme, and a
  maximum principle for limited linear advection. The first is the
  "reduces exactly to the 1D algorithm" property stated for Athena and
  Gardiner & Stone above.
* **Stability** (eq. 2.17). $\Delta t\max_{i,j,p}(\vert\lambda^{(p)}_x\vert/h,\ \vert\lambda^{(p)}_y\vert/h) \le 1$,
  proved (by Fourier analysis) only when the two flux Jacobians commute,
  and used as the time-step control of all runs with "no evidence of
  instability". This is the per-direction form of Athena's eq. 78
  (Time-step definitions, above).
* **Limiting variables.** For general systems the slopes are limited in
  characteristic amplitudes (eqs. 2.5–2.6); the gas-dynamics algorithm of
  §4 limits primitive variables componentwise (eqs. 4.7–4.8) with the
  steeper slope of Colella (1985). Characteristic limiting in Athena's CTU
  is therefore not the 1990 gas-dynamics choice.
* **Reference states** (eqs. 2.10–2.11, p. 183). The reference state is
  the extrapolation under the fastest wave toward the edge, and the
  predictor's second-order consistency with the characteristic relations
  holds for smooth nonlinear flow only if the reference state differs
  from the cell value by $O(h)$. PLUTO's remark that "both classical
  reference-state choices" may lose second order (above) concerns this
  construction; whether PLUTO's choices include exactly eq. 2.11 cannot
  be judged from either paper.
* **Robustness** (§5 end, §6, pp. 197–198). The unsplit scheme is "more
  sensitive to various details of the implementation": eq. 2.15 is
  "essential" (otherwise "considerably lower resolution in the jet along
  the wall in the double Mach region"), as are careful wall conditions and
  a multidimensional flattening (see [PPM](/methods/ppm.md)). As printed,
  p. 192 says the §5 runs used the cell-centred (eq. 2.13-type) states;
  the inconsistency is recorded on the Source page.
* **3D** (§6, p. 199). The 3D analogue with all three requirements
  "requires 12 solutions to the Riemann problem per zone per time step",
  against 3 for splitting; dropping the maximum principle, with
  donor-cell-type transverse derivatives in the predictor, gives 6. The
  12- and 6-solve counts quoted for Athena and PLUTO above therefore
  originate here. Colella states **no Courant limit** for either 3D
  variant: the pairing of 12 solves with $\nu \le 1$ and of 6 with
  $\nu \le 1/2$ is Stone et al.'s (2008) (refined in batch 9: first printed by [Gardiner & Stone (2008)](/sources/gardiner-2008.md)), who cite Saltzman (1994) for the
  full scheme; Colella cites Saltzman & Colella only for Lagrangian grid
  motion. Which variant to use is "undoubtedly problem dependent".
* **Cost** (§6, p. 198). Twice the Riemann solves of the split algorithm
  and, with the Riemann solve half of the 1D cost, **50 % more time**; a
  vectorized Cray-1 code advanced "about 24,000 zones by one time step in
  each cpu second". Castro's about 2× in 2D (Cost, above) is a later,
  different implementation.
* **Split against unsplit** (§5, Figs. 9–10). On the
  [double Mach reflection](/benchmarks/double-mach-reflection.md) at
  $h = 1/120$ the unsplit and operator-split results with the same
  parameters are "essentially identical". The stated aim is "the same
  robustness and resolution as the existing operator split algorithms";
  the motivations are settings that need unsplit updates (front tracking,
  Lagrangian and porous-media codes, implicit–explicit hybrids), not a
  split-scheme accuracy defect. This qualifies, and does not contradict,
  the evidence under Against dimensional splitting, which comes from other
  problems (Rayleigh–Taylor, Liska–Wendroff) and other codes.
* **Method of lines against CTU.** The advection limits above (maximum
  for CTU, sum for donor cell) are the contrast behind Quokka's statement
  that the method of lines "formally needs a smaller step than CTU by a
  factor $1/d$" (Method of lines, above). They are CTU results, not
  method-of-lines ones, and neither close nor reopen the RK2 entry under
  Contradictions.

**Attributions checked.** PLUTO's CTU (corner-coupled states from
first-order Godunov transverse fluxes between cell-centred states, $\nu \le 1$
in 2D) is Colella's eq. 2.13 with the limit of eq. 2.17; Gardiner &
Stone's path (normal states, Riemann solve, transverse correction) is
Colella's eq. 2.15. GAMER's statement that CTU is "generally less
diffusive than the VL scheme" is GAMER's own; Colella has no VL
comparison.

### A split code: FLASH's first version

| Code | Integrators | Source |
|---|---|---|
| [FLASH](/software/flash.md) (first version) | dimensionally split PPM, Strang-type with the sweep order reversed every step; unsplit PPM not present | [Fryxell et al. (2000)](/sources/fryxell-2000.md), §3.2, Fig. 22 |

[Fryxell et al. (2000)](/sources/fryxell-2000.md) give the alternation
"second-order accuracy in time" (§3.2). Their 2D Sod tube along the
diagonal shows "slightly larger oscillations (on the order of a few
percent)" at the rarefaction tail and the contact than the grid-aligned
one, attributed to the directional splitting, with the same location
and thickness of the waves (§7.2). Fig. 22 lists unsplit PPM "for
illustrative purposes only; they are not present in the current version".
This adds a split-scheme data point to Split schemes still in use, above.

## Later uses (batch 9)

### 3D CTU+CT in its primary source

[Gardiner & Stone (2008)](/sources/gardiner-2008.md) is the 3D scheme
summarized under "Athena 3D" above. It agrees with that summary in
substance and adds or refines the following.

* **Who pairs the solve counts with the Courant limits.** The 12-solve
  CTU (after Colella 1990, Saltzman 1994 and Miller & Colella 2002) is
  "optimally stable for CFL numbers ≤ 1" (§4.1); the 6-solve variant is
  "stable for CFL < 1/2", a strict bound found experimentally, with no
  proof (§4.2). The pairing is therefore printed first by Gardiner & Stone
  (2008) and restated by Stone et al. (2008), who cite them. This refines
  the batch-8 statement that the pairing "is Stone et al.'s (2008)"; the
  point that Colella (1990) prints no Courant limit for either 3D variant
  stands.
* **Whose words.** The phrases "as accurate as the twelve-solve method"
  and "dramatically simpler to implement" quoted under "Athena 3D" are
  Stone et al.'s (2008) characterization of Gardiner & Stone. Gardiner &
  Stone themselves write that both variants are "accurate and robust for
  approximately the same computational cost" and prefer the 6-solve one
  "as a result of its simplicity and smaller memory footprint" (§6). Two
  6-solve steps at a Courant number of 1/2 cost about one 12-solve step at
  1 (§4.2).
* **The 12-solve scheme for MHD** (§4.1, eqs. 21–34). Each interface state
  is first advanced by $\Delta t/3$ of a single transverse flux gradient,
  then by $\Delta t/2$ of the transverse gradients built from those cross
  fluxes. As written it is not a useful MHD method: parallel gradients
  enter in primitive form and transverse ones in conservative form, so the
  MHD source terms are dropped and the result is formally first order, with
  secular field evolution in the field-loop test. The authors implemented
  the corrections but do not print them.
* **The 6-solve scheme** (§4.2, eqs. 35–50), in six steps: PPM interface
  states with multidimensional induction terms and Riemann fluxes; edge
  EMFs; a $\Delta t/2$ transverse correction with source terms; Riemann
  fluxes at $t^{n+1/2}$; edge EMFs at $t^{n+1/2}$, with a cell-centre
  reference EMF from face-averaged $\mathbf B$ and from $\rho$, $\rho\mathbf v$
  after a conservative $\Delta t/2$ update with the first fluxes (eq. 48);
  the full update. It reduces exactly to 2D CTU and to 1D PPM under the
  corresponding symmetry.
* **Where minmod enters.** In two places, not one. (i) The characteristic
  interface-state step adds limited transverse induction terms, e.g. for
  the $x$ interface
  $\partial_tB_y + \partial_x(v_xB_y) - B_x\partial_xv_y - v_y\,\mathrm{minmod}(\partial_xB_x,\ -\partial_yB_y) = 0$
  (eqs. 15–20). (ii) The $\Delta t/2$ transverse correction adds limited
  source terms to the energy and to the transverse field components
  (eqs. 39, 43, 46). The momentum source $\mathbf B\,\partial_xB_x$ is
  **not** limited (eq. 38), and the interface-normal field needs no source
  term: it is advanced by a loop of edge EMFs (eq. 40).
* **Corner EMF.** No new 3D EMF is defined: both variants reuse the
  contact-upwinded EMF of [Gardiner & Stone (2005)](/sources/gardiner-2005.md)
  (§4 intro); see [constrained transport](/methods/constrained-transport.md).
* **Accuracy and the Courant number** (§5.2–5.3, §6). On 3D linear waves
  both variants converge at second order for all four families, the
  6-solve with lower errors except for the slow wave; on the circularly
  polarized Alfvén wave the 12-solve run at Courant number 0.4 matches the
  6-solve one, and at 0.8 its travelling-wave error is slightly lower and
  its standing-wave error higher. The authors attribute the dominant error
  difference to the Courant-number dependence of the truncation error.
* **Time step.** No time-step formula and no Courant number for the
  6-solve runs are printed; eq. 95 of Stone et al. (2008) (Time-step
  definitions, above) has no counterpart here.
* **Low β in 3D.** The 3D adiabatic blast wave at ambient plasma beta 0.02
  runs robustly with the 6-solve CTU+CT to $t = 0.02$ (§5.5; see
  [MHD blast wave](/benchmarks/mhd-blast-wave.md)). Cholla's 3D VL+CT
  instability at the same beta (Van Leer + CT in Cholla, above) concerns a
  different integrator, so this is a further qualification, not a
  contradiction.
* **Scope.** Static and adaptive refinement with these integrators are
  deferred to a future paper (§6).

## Contradictions

* **Is RK2 with $\nu = 1$ stable in 3D?** *Open.*
  [Stone et al. (2020)](/sources/stone-2020.md), §3.2.3: RK2 and RK3 have
  SSP coefficient 1, so their CFL constraint is $\nu = 1$, which in
  practice "seems to work for both PLM and PPM reconstruction for most
  problems", with no dependence on dimension stated; VL2 needs
  $\nu = 1/2$ in 2D and 3D. Non-closing evidence on the other side:
  AthenaK, of the same lineage, bounds the step by the per-direction
  minimum and "generally" uses $\nu \le 1/d$
  ([Stone et al. (2026)](/sources/stone-2026.md), §3, eq. 3), a usage
  convention, not a stability claim.
  [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.2.1, eqs. 19–21
  and footnote 3: for RK2-SSP the stability coefficient is 1 when the
  step is bounded by the cell maximum of the sum over directions of the
  signal speed over $h$, so with the single-direction bound the largest
  stable $\nu$ in 3D is 1/3, and dropping the factor $d$ "can violate"
  stability. Stone et al. (2020) do not print how their $\Delta t$ is
  normalized across directions: if it is the per-direction minimum (as in
  Athena and AthenaK), the two claims are incompatible; if it is the sum
  over directions, they agree. The entry closes when a source states the
  Athena++ normalization.

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §1, §4.2, §5.1, §6, §7, §8.3.
2. [Stone et al. (2020)](/sources/stone-2020.md), §3.2.3, §3.3.1, §3.3.5.
3. [Mignone et al. (2012)](/sources/mignone-2012.md), §3.1–3.3, §6.
4. [Almgren et al. (2010)](/sources/almgren-2010.md), §5, §5.1–5.2, §8.3 (arXiv v1).
5. [Zhang et al. (2018)](/sources/zhang-2018.md), §3.2 (arXiv v4).
6. [Bryan et al. (2014)](/sources/bryan-2014.md), §2.2.2, §4.1–4.4, §9 (arXiv v1).
7. [Skinner & Ostriker (2013)](/sources/skinner-2013.md), §3.1, §3.3–3.4 (arXiv v1).
8. [Stone et al. (2026)](/sources/stone-2026.md), §3, §3.1–3.4, §5.1 (arXiv v1).
9. [Lesur et al. (2023)](/sources/lesur-2023.md), §2.3, §2.7–2.8 (arXiv v1).
10. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §2.2, §3.1.1, §3.1.5 (arXiv v2).
11. [Rossazza et al. (2026)](/sources/rossazza-2026.md), §2.2, §4.1 (arXiv v1).
12. [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.2.1, §3.1.9 (arXiv v2).
13. [Shankar et al. (2023)](/sources/shankar-2023.md), §II C, §III, §IV, §V A (arXiv v2).
14. [Zaghi et al. (2023)](/sources/zaghi-2023.md), §3.1.
15. [Bernardini et al. (2021)](/sources/bernardini-2021.md), §2.2.
16. [Kim & Ostriker (2017)](/sources/kim-2017.md), §2.1, §2.2.2, §2.2.5
    (arXiv v2).
17. [Gardiner & Stone (2005)](/sources/gardiner-2005.md), §§1, 2.1, 3.1, 3.3.1, 4.1–4.3, 5.4, 5.6, 6, eqs. 25–33, 52, 57–78 (arXiv v1).
18. [Colella (1990)](/sources/colella-1990.md), §§1–6, eqs. 1.2–1.6, 2.5–2.17, 4.7–4.10, Figs. 9–10.
19. [Fryxell et al. (2000)](/sources/fryxell-2000.md), §§3.2, 7.2, Fig. 22.
20. [Gardiner & Stone (2008)](/sources/gardiner-2008.md), §§1, 3.1, 4.1–4.2, 5.2–5.5, 6, eqs. 15–50.

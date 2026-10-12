---
type: Method
title: "Unsplit Godunov integrators"
description: "Second-order, directionally unsplit time integrators of the astrophysical Godunov codes — corner transport upwind (CTU) with characteristic tracing, the van Leer / MUSCL–Hancock predictor–corrector (VL, VL2) and method-of-lines SSP Runge–Kutta — with their Riemann-solve counts, Courant limits, and the evidence the codes give against dimensional splitting."
status: established
aliases: [CTU, corner transport upwind, CTU+CT, VL+CT, VL2, van Leer integrator, MUSCL-Hancock, method-of-lines Runge-Kutta, unsplit integrator, SSP-RK3, IMEX Runge-Kutta]
tags: [time-integration, unsplit, hydro, mhd, constrained-transport, gpu]
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

## Contradictions

* **Is RK2 with $\nu = 1$ stable in 3D?** *Open.*
  [Stone et al. (2020)](/sources/stone-2020.md), §3.2.3: RK2 and RK3 have
  SSP coefficient 1, so their CFL constraint is $\nu = 1$, and "in
  practice, the limit $C_0 = 1$ seems to work for both PLM and PPM
  reconstruction for most problems", with no dependence on dimension
  stated; VL2 needs $\nu = 1/2$ in 2D and 3D.
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

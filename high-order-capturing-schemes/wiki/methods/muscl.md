---
type: Method
title: "MUSCL"
description: "Van Leer's second-order extension of Godunov's method: piecewise-linear cells with slopes stored independently of the averages and limited by monotonicity algorithms, an interface Riemann problem with one-step characteristic time-centring, and (in the original) a Lagrangean step plus least-squares remap; later also a single-step Eulerian scheme and, in the semi-discrete literature, any limited piecewise-linear reconstruction."
status: established
aliases: [Monotonic Upstream-centered Scheme for Conservation Laws, MUSCL scheme, van Leer's scheme]
tags: [godunov, reconstruction, limiter, finite-volume, euler]
timestamp: 2026-10-13T00:00:00Z
---

# MUSCL

**Name and origin.** MUSCL, "Monotonic Upstream-centered Scheme for
Conservation Laws", is the gas-dynamics code that P. R. Woodward wrote at
Leiden Observatory along the lines of
[van Leer (1979)](/sources/vanleer-1979.md) (§1, p. 102); the separate remap
step was Woodward's idea (Acknowledgments). The method is the
second-order sequel to Godunov's method: Godunov's cells carry uniform
states, MUSCL's carry linear ones.

## The original scheme (van Leer 1979)

**Piecewise-linear cells with stored slopes** (§2.2, eqs. 39–41). Each cell
carries $\mathcal P_i = \bar u_i + \hat u^{(1)}_i\zeta$, the
[reconstruction](/methods/finite-volume-reconstruction.md) of degree
$K = 1$ with the correct average. The slope $\hat u^{(1)}_i$ is not
computed from neighbouring averages: it is "independent of the slab
averages; [it] can not be derived from the latter and must be stored
separately" (p. 107), so each cell keeps two data per quantity per
dimension, which "potentially has the effect of a mesh refinement of a
factor two" (p. 102). With every slope zero the scheme is Godunov's, which
"accounts for the first-order accuracy of Godunov's scheme" (p. 107).

**Lagrangean step plus remap** (§§2–3). The core scheme works in the mass
coordinate and distributes specific volume, velocity and pressure, not
total energy, so that the monotonicity algorithm stays explicit in $p$
(eqs. 47–48). Slopes are updated by differencing the new interface values,
a "temporary substitute" for least-squares fitting (eq. 51.5). A separate
step remaps the results to the Eulerian grid by least-squares fitting that
conserves the zeroth and first moments (§3.2). Its step condition,
$\Delta t \le \min(h/\vert v_x\vert,\ h/c)$ to leading order (eq. 99), is
"less stringent than the usual condition for a fully Eulerian scheme",
$\Delta t \le h/(\vert v_x\vert + c)$ (eq. 100). Multi-D is by Strang
splitting (§3.4).

**Interface Riemann problem** (§2.3; App. A). The interface states are the
cell profiles evaluated at the interface. The star state starts from the
acoustic guess
$$p_* \approx \frac{(\rho c)^+ p^- + (\rho c)^- p^+ - (\rho c)^-(\rho c)^+(v_n^+ - v_n^-)}{(\rho c)^- + (\rho c)^+}$$
(eq. 60) and is iterated by a tangent (Newton-type) iteration, quadratic
where Godunov's chord iteration is linear in the data jumps (eqs. A1–A3;
[exact Riemann solver](/methods/exact-riemann-solver.md)). In smooth flow
the interface jumps are $O(h^3)$, against $O(h)$ for Godunov, so the code
iterates only where the guess departs from the neighbouring pressures by
more than 1 % (p. 110).

**Second order in time, in one step** (§§2.3–2.4, eqs. 64–90). The
characteristic equations written at a discontinuity give the time
derivatives of the resolved interface state, with the cell slopes as the
space derivatives on each side. A half step, e.g.
$v_{n*} + \tfrac12\Delta t\,\partial_t v_{n*}$ (eq. 70), gives time-centred
interface values, and the update is accurate to $O(\Delta t^3)$ per step.
There are no Runge–Kutta stages. In the linear limit the scheme reduces to
Fromm's upstream-centred second-order scheme, as Godunov's reduces to
Courant–Isaacson–Rees (p. 111; App. B).

**Monotonicity algorithms** (§3.3). At the start of each Lagrangean step
(eq. 101, Fig. 3)
$$\hat u^{(1)}_i \leftarrow \operatorname{minmod}\left(2\Delta^1\bar u_{i-1},\ \hat u^{(1)}_i,\ 2\Delta^1\bar u_i\right),$$
applied to specific volume, velocity and pressure. Its stated rules: the
linear profile must not exceed the neighbouring averages; the slope is
zero at an extremum of the averages, and zero when its sign disagrees with
their trend (p. 117). With the central slope
$\hat u^{(1)}_i = \tfrac12(\bar u_{i+1} - \bar u_{i-1})$ (eq. B1) this is
the registry's monotonized-central slope $\delta^{\mathrm{MC}}\bar u_i$ (an
algebraic identity; the paper does not use the name).
* The factors 2 may be lowered for stronger limiting, but not below 1
  plus a term of the order of the data jump, "lest the scheme lose its
  second-order accuracy"; with
  factors 0 the scheme is Godunov's (p. 118).
* In the remap the factors 2 are divided by the fraction of the cell's
  mass that crosses the Eulerian boundary and by the fraction that stays,
  so that the averages of both parts stay within the neighbouring
  averages; "positivity is guaranteed only for the zone averages"
  (eqs. 102–103, p. 119).
* The **harmonic-mean slope**
  $$\hat u^{(1)}_i = \frac{2\,\Delta^1\bar u_{i-1}\,\Delta^1\bar u_i}{\Delta^1\bar u_{i-1} + \Delta^1\bar u_i}$$
  when the two differences have one sign, else 0 (eq. B2), "automatically"
  meets the crudest monotonicity condition.
* Both algorithms "will clip real peaks to the same degree as a
  first-order method would do" (p. 119). A narrow-base variant built on the
  saved interface values limits as (101) near a plateau and less near a
  peak (eq. 104); van Leer lists a monotonicity algorithm that clips peaks
  less among the desired improvements (§5).
* For the system the paper claims no monotonicity: "the nonlinearity of
  slab interactions makes it impossible to fully guarantee monotonicity,
  especially for the largest allowed time steps" (p. 118).

**Slope options** (App. B). Central differencing of averages (B1),
differencing of interface values, and moment (least-squares) fitting are
compared through the linear analysis of van Leer's earlier paper: moment
fitting is "vastly superior", its convective error smaller "by two orders"
of the mesh size, and interface differencing has a largest dissipative
error 3 times smaller than central differencing and 3 times larger than
moment fitting. MUSCL uses interface differencing in the Lagrangean step
and moment fitting in the remap.

**Results** (§4). On [Sod's shock tube](/benchmarks/sod-shock-tube.md) with
100 cells and $\nu = 0.9$ the profiles at $t = 0.14154$ are called "superior
to all methods tested by Sod". In the Mach 3
[wind tunnel with a step](/benchmarks/forward-facing-step.md), MUSCL on 10
zones of entrance height mimics Godunov on 30, and Godunov "will not run
more than twice as fast", so in 2D MUSCL is "at least an order of
magnitude more efficient than Godunov's method". On the coarsest grid
($15\times5$) a visible Mach stem is "an artifact due to the monotonicity
algorithms", which force pressure contours perpendicular to a reflecting
wall (p. 123).

## Later forms and uses

**Three meanings of "MUSCL".** The name now covers (1) van Leer's
Lagrangean step plus remap; (2) a single-step Eulerian scheme (Colella's,
compared by Woodward & Colella below); and (3) in the semi-discrete
literature, a limited piecewise-linear reconstruction driven by a
Runge–Kutta integrator, the "TVD MUSCL scheme" of
[Shu (1998)](/sources/shu-1998.md) (Fig. 4.1) and
[Gottlieb, Shu & Tadmor (2001)](/sources/gottlieb-2001.md) (§2.1;
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md)). The third keeps no stored
slopes and no characteristic time-centring.

**The two Eulerian forms compared** ([Woodward & Colella (1984)](/sources/woodward-1984.md)).
* MUSCL ranks second by accuracy on a given grid, after
  [PPM](/methods/ppm.md) and ahead of ETBFCT, BBC, MacCormack and Godunov
  (§VII). On the [interacting blast waves](/benchmarks/interacting-blast-waves.md)
  its density error is 0.162 at 200 zones and 0.0401 at 1200, against
  PPMLR's 0.0760 and 0.0133, and matching 200-zone PPMLR costs it 6.2 times
  the CPU time (§VIa, Table I).
* Unlike PPM, MUSCL's two forms differ in accuracy (§§VIb–VII). The
  single-step form is noisy along the nearly steady reflected shock of the
  [double Mach reflection](/benchmarks/double-mach-reflection.md); the
  Lagrange-plus-remap form is not, but is less accurate there, which
  "demonstrates the extra sensitivity of single-step Eulerian schemes to
  vanishing characteristic speeds" (§VIc;
  [slowly moving shock anomaly](/definitions/slowly-moving-shock-anomaly.md)).
  *Compiler reading:* van Leer's own Lagrangean step uses interface
  differencing and his remap moment fitting; neither paper links this
  asymmetry to the difference between the forms.
* MUSCL's shocks are about one zone wide, thin enough to show the
  "numerical instability of 2-D, strong, stationary shocks" that Godunov's
  method shows (§VIb;
  [numerical shock instability](/definitions/numerical-shock-instability.md)).
* For 1D advection MUSCL "is a linear hybridization technique" (§IIIb).
  Because it constrains $\rho$, $p$ and the velocity rather than the
  conserved variables, it avoids ETBFCT's negative pressures (§§IIIb, VIb).

**As a base for other schemes.**
* [PPM](/methods/ppm.md) is "a MUSCL-type higher-order Godunov method"
  with parabolas, and keeps van Leer's second-order treatment of the
  nonlinear wave interaction ([Colella & Woodward (1984)](/sources/colella-1984.md), §§1–2).
* [ENO](/methods/eno-reconstruction.md) began with a second-order
  non-oscillatory modification of MUSCL by Harten and Osher
  ([Harten et al. (1987)](/sources/harten-1987.md)), and
  [ADER](/methods/ader.md) traces its one-step lineage to MUSCL
  ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §1).
* In 1D, Balsara's divergence-free reconstruction of face fields reduces to
  van Leer's MUSCL ([Balsara (2001)](/sources/balsara-2001.md), eq. 3.40;
  [divergence-free reconstruction](/methods/divergence-free-reconstruction.md)).
* A minmod-limited MUSCL slope is the last fallback of Titarev and Toro's
  order reduction in FV-WENO ([Titarev & Toro (2004)](/sources/titarev-2004.md), §3).
* Second-order MUSCL with HLL-type solvers is the setting of
  [Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md) (§§II–III), and
  AMReX-based codes use "van Leer" limiting
  ([Natarajan et al. (2022)](/sources/natarajan-2022.md), §2) or a van Leer
  MUSCL limiter ([Giuliani et al. (2022)](/sources/giuliani-2022.md), §5.1;
  [AMReX](/software/amrex.md)). Van Leer (1979) prints two limiters, the
  MC-type (101) and the harmonic-mean (B2); those pages do not say which
  is meant.

**TVD.** Harten et al. class the MUSCL scheme as TVD in the scalar case
([total variation diminishing](/properties/total-variation-diminishing.md);
[Harten et al. (1987)](/sources/harten-1987.md)). Van Leer (1979) makes no
TVD claim, and for the gas-dynamics system states that monotonicity cannot
be fully guaranteed (p. 118). The two statements differ in scope (scalar
scheme against the system), so they qualify each other and do not
conflict.

# Citations

1. [van Leer (1979)](/sources/vanleer-1979.md), §§1–5, Apps. A–B (eqs. 39–104, A1–A3, B1–B2).
2. [Woodward & Colella (1984)](/sources/woodward-1984.md), §§IIIb, VIa–VII, Table I.
3. [Colella & Woodward (1984)](/sources/colella-1984.md), §§1–2.
4. [Harten et al. (1987)](/sources/harten-1987.md), introduction (the ENO series).
5. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §1.
6. [Balsara (2001)](/sources/balsara-2001.md), eq. 3.40.
7. [Titarev & Toro (2004)](/sources/titarev-2004.md), §3.
8. [Shu (1998)](/sources/shu-1998.md), §4.2, Fig. 4.1.
9. [Gottlieb, Shu & Tadmor (2001)](/sources/gottlieb-2001.md), §2.1.
10. [Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §§II–III.
11. [Giuliani et al. (2022)](/sources/giuliani-2022.md), §5.1 (arXiv v2).
12. [Natarajan et al. (2022)](/sources/natarajan-2022.md), §2 (arXiv v1).

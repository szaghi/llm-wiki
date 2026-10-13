---
type: Method
title: "Piecewise parabolic method (PPM)"
description: "Colella and Woodward's MUSCL-type higher-order Godunov method: a monotonized parabolic reconstruction with contact steepening, characteristic domain-of-dependence averaging, one Riemann solve per interface and added dissipation (flattening, diffusive flux) near shocks, in Lagrange-plus-remap and direct-Eulerian forms; and the variants the production codes of this bundle run, from split direct-Eulerian PPM to method-of-lines PPM inside second-order integrators."
status: established
aliases: [PPM, piecewise parabolic method, Colella-Woodward PPM, CW84, PPM4, characteristic PPM]
tags: [hydro, reconstruction, riemann-solver, time-integration]
timestamp: 2026-10-13T00:00:00Z
---

# Piecewise parabolic method (PPM)

PPM is a higher-order extension of Godunov's method of the MUSCL type,
specified by [Colella & Woodward (1984)](/sources/colella-1984.md) in one
dimension, with multidimensional runs built by operator splitting. The
original paper gives three formulations: a scalar advection scheme on a
non-uniform mesh (§1); a Lagrangian gas-dynamics scheme in planar,
cylindrical or spherical geometry (§2), which with a remap onto the fixed
mesh is the **two-step (Lagrange-plus-remap) Eulerian** scheme, an
approach the paper credits to Noh; and a **single-step (direct)
Eulerian** scheme (§3). Its verification is in the companion paper,
Woodward & Colella (1984), not ingested here. Below, all statements
without another citation are from Colella & Woodward (1984).

## Reconstruction

**Parabola.** On each cell $I_i$ the profile is the parabola with edge
values $u^+_{i-1/2}$ (left edge) and $u^-_{i+1/2}$ (right edge) and mean
equal to the cell average $u_i^n$; its curvature coefficient is
$6\left(u_i^n - \tfrac12(u^+_{i-1/2} + u^-_{i+1/2})\right)$ (eqs. 1.4–1.5).

**Interface value.** Before limiting, both edges adjacent to $x_{i+1/2}$
take one interface value: the derivative at $x_{i+1/2}$ of the quartic
through the cumulative integrals at the five interfaces $x_{i-3/2}$ to
$x_{i+5/2}$, so that it depends on cells $i-1$ to $i+2$ (eq. 1.6,
non-uniform mesh). It is built from limited cell slopes, zero unless
$(u_{i+1}^n - u_i^n)(u_i^n - u_{i-1}^n) > 0$, which keep it between
$u_i^n$ and $u_{i+1}^n$ (eqs. 1.7–1.8; eq. 1.8 carries a misprint,
recorded on the Source page). It is "third-order accurate for variable
mesh spacing, even where the mesh spacing changes discontinuously". On a
uniform mesh without limiting it is
$$\tfrac{7}{12}\left(u_i^n + u_{i+1}^n\right) - \tfrac{1}{12}\left(u_{i-1}^n + u_{i+2}^n\right)$$
(eq. 1.9).

**Monotonicity constraint** (eq. 1.10). Two resets make each parabola
monotone and free of new extrema:
1. at a local extremum, $(u^-_{i+1/2} - u_i^n)(u_i^n - u^+_{i-1/2}) \le 0$,
   both edges are set to $u_i^n$ and the profile is constant;
2. where the parabola overshoots, the edge on the far side is reset so that
   the derivative vanishes at the opposite edge:
   $u^+_{i-1/2} \to 3u_i^n - 2u^-_{i+1/2}$ when
   $(u^-_{i+1/2} - u^+_{i-1/2})\left(u_i^n - \tfrac12(u^+_{i-1/2} + u^-_{i+1/2})\right) > (u^-_{i+1/2} - u^+_{i-1/2})^2/6$,
   and symmetrically $u^-_{i+1/2} \to 3u_i^n - 2u^+_{i-1/2}$.

After these resets the two edge values at an interface generally differ:
this step creates the discontinuities at cell edges (p. 177).

**Accuracy as printed.** The advection scheme is "third-order accurate in
general; in the limit of very small time steps, for equally spaced zones,
it is fourth-order accurate" (Fig. 2 caption, p. 178). The gas-dynamics
schemes keep this spatial accuracy but are second order in time by
design, after van Leer: third order in space and time would need
"numerous solutions of the Riemann problem" (p. 181).

## Contact steepening

A discontinuity detector (eqs. 1.14–1.17, Fig. 3) blends the edge values
toward the edges of the limited linear profiles of the two neighbouring
cells, with a weight between 0 and 1 that grows with a normalized third
derivative. It is nonzero only where the second derivative changes sign,
the first and third derivatives have opposite signs and the jump exceeds
a relative threshold of 0.01; the two weight coefficients are 20 and 0.05
in Woodward & Colella (p. 181). It runs just before the monotonicity step;
if it fires in smooth flow "the scheme remains second-order accurate"
(p. 180). In gas dynamics it acts **on density only and only at
contacts**: a cell qualifies when $\gamma$ times a problem-dependent
constant (0.1 in Woodward & Colella) times
$\vert\rho_{i+1} - \rho_{i-1}\vert/\min(\rho_{i+1}, \rho_{i-1})$ is at
least $\vert p_{i+1} - p_{i-1}\vert/\min(p_{i+1}, p_{i-1})$ (eq. 3.2). The
pure Lagrangian scheme does without it ("contact discontinuities
automatically remain sharp", p. 183); the two-step scheme applies it to
density in the remap (p. 187).

## Interface states: characteristic tracing

**Advection.** The flux value is the average of the upwind parabola over
the distance $\vert v_x\vert\Delta t$ from the interface, its domain of
dependence (eqs. 1.11–1.13).

**Lagrangian scheme** (§2, eqs. 2.5–2.9). Specific volume, velocity and
pressure are interpolated, pressure rather than total energy because
limiting the pressure profile behaves better near shocks (p. 183). The
interface states are the parabola averages over the domains of dependence
of the two acoustic characteristics, at the Lagrangian sound speed
$\rho c_s = (\gamma p\rho)^{1/2}$. Body forces and curvilinear area terms
correct them (eq. 2.9) so that a smooth steady solution produces no false
jump.

**Direct Eulerian scheme** (§3, eqs. 3.3–3.7, Fig. 5). Density, normal and
transverse velocity and pressure are interpolated in the volume
coordinate. A first guess averages the parabolae over the domain of
dependence of the fastest characteristic moving toward the interface
(eq. 3.3); alone, it would make advection first order (p. 188). It is
then corrected family by family, with eigenvalues $v_x - c_s$, $v_x$ and
$v_x + c_s$: each family moving toward the interface adds the difference
between its own domain-of-dependence average and the first guess,
projected on that family, while families moving away add nothing; the
transverse velocity moves with the contact. The stated requirements are
that the amount of each family crossing the interface be correct to
second order and that the flux reduce to the exact advection flux when
pressure and velocity are uniform (p. 189). Source terms enter the
tracing (eq. 3.7) and are time-centred in the final update (eq. 3.8). The
pressure gradient is differenced apart from the area-weighted flux
divergence (eq. 3.1).

## Riemann solver

One Riemann problem per interface gives the time-averaged interface
pressure and velocity (eq. 2.8, p. 185). Each side contributes one
equation whose wave speed is that side's Lagrangian shock speed, a
function of the unknown interface pressure through the factor
$1 + \frac{\gamma+1}{2\gamma}(\text{pressure ratio} - 1)$; the pair is
solved by van Leer's Newton iteration "with a fixed number of
iterations". In smooth flow the equations are a finite-difference
approximation of the characteristic equations. The Eulerian scheme uses
the Cartesian form with the same iteration and, inside a rarefaction fan,
linear interpolation between the states on either side (p. 191). In the
stationary-shock test of Fig. 8, 6 iterations are used: "If only 2
iterations are performed, very large errors are generated in the single
zone just behind the shock." See
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md)
for the two-shock solvers of the codes.

## Dissipation near shocks

**Why monotonicity is not enough** (§4). Slow shocks leave low-amplitude
post-shock oscillations in both Eulerian forms, in the entropy and in the
Riemann invariant $v_x - 2c_s/(\gamma-1)$ carried by the characteristic
that crosses the shock; the scalar case is well behaved (p. 192). In
Lagrangian PPM a very strong planar shock ($\gamma = 5/3$, pressure jump
over six orders) leaves oscillations of "about 1.3% amplitude" (Fig. 6).
Even first-order Godunov leaves a 3 % error behind a nearly stationary
strong shock (Fig. 8), so flattening cannot cure that case.

**Flattening** (eq. 4.1, Appendix). Each edge value is blended toward
$u_i^n$ with a coefficient between 0 and 1; **1 is full flattening, i.e.
locally Godunov's first-order method, and 0 none** (p. 192). A cell is a
shock candidate where $(p_{i+1} - p_{i-1})/\min(p_{i+1}, p_{i-1}) > 0.33$
and $v_{x,i-1} - v_{x,i+1} > 0$ (eq. A.1); the coefficient grows with the
steepness $(p_{i+1} - p_{i-1})/(p_{i+2} - p_{i-2})$ above 0.75 with slope
10, and the upstream neighbour's value is also taken (eq. A.2, printed
with an inconsistency recorded on the Source page). The Lagrangian and
multidimensional variants add a noise-wavelength term from a Lagrangian
shock-speed estimate and a shock-strength term (eqs. A.4–A.11, constants
on p. 200). In the two-step scheme flattening acts in the Lagrangian step,
not in the remap. The calibration over the parameter space for
$\gamma = 1.4$ gives post-shock density oscillations of $\tfrac34$ % of
the jump at worst, $\tfrac14$ % typically, and a shock width of at most
two cells; "experimentation with different values of the parameters is
not recommended" (pp. 200–201).

**Diffusive flux** (eqs. 4.2–4.5). A term proportional to $u_i - u_{i+1}$
is added to $\hat f_{i+1/2}$ with coefficient
$K\max(v_{x,i} - v_{x,i+1}, 0)$ in 1D, akin to Lapidus; in multi-D an
undivided-difference $-\nabla\cdot\mathbf v$ replaces the velocity jump,
to detect shocks transverse to the sweep. Single-step Eulerian PPM used
$K = 0.1$, MacCormack's method $K = 1$ (p. 196). Alternatively the grid
oscillates by the same amount on alternate steps, adding only the
advection scheme's own dissipation (eq. 4.3).

**Unsolved case** (pp. 193–194). A strong shock nearly at rest on the
grid, such as the Mach 3 wind-tunnel shock near the wall and the Mach
stem, keeps errors no flattening removes: Godunov dissipation at a shock
vanishes with the shock speed, and small tangential velocities in the
shock column create large spurious sources in the 1D sweeps.

## Lagrange-plus-remap versus direct Eulerian

Both are Eulerian on a fixed mesh. The two-step scheme takes the
Lagrangian step, then remaps with the advection scheme on the moved,
non-uniform mesh, interpolating density (not specific volume) in the
volume coordinate and building the total energy from edge values of
$p$, $\rho$ and $v_x$ (pp. 186–187). The single-step scheme traces
characteristics directly on the fixed mesh (§3). The paper names
multiple fluids as "easily added, particularly to the two-step Eulerian
version", and a general equation of state as available through Colella &
Glaz (§5).

## Use in production codes

The codes of this bundle state their PPM as follows (each row cites the
code's own source).

| Code | PPM as stated | Source |
|---|---|---|
| [Enzo](/software/enzo.md) | direct-Eulerian Colella–Woodward PPM, dimensionally split, primitive variables, characteristic domain-of-dependence averaging, optional steepening, flattening and diffusive flux; two-shock solver with PPM only; $n_{\mathrm g} = 3$ | [Bryan et al. (2014)](/sources/bryan-2014.md), §3, §4.1, §4.1.2 |
| [Athena](/software/athena.md) | CTU with characteristic tracing; Colella–Woodward interpolation and monotonicity conditions (eqs. 46–60), Colella–Sekora extremum-preserving limiters as an option | [Stone et al. (2008)](/sources/stone-2008.md), §4.2.3 |
| [Athena++](/software/athena-plus-plus.md) | method of lines; primitive or characteristic variables; Colella–Sekora / McCorquodale et al. limiter on Cartesian meshes, Mignone's modification of the Colella–Woodward limiter on curvilinear grids; the uniform-mesh interface value of eq. 1.9 (their eq. 10) | [Stone et al. (2020)](/sources/stone-2020.md), §3.2.1 |
| [AthenaK](/software/athenak.md) | "PPM4 (Colella & Woodward 1984)" and the extremum-preserving PPMX, on primitive variables only | [Stone et al. (2026)](/sources/stone-2026.md), §3 |
| [Castro](/software/castro.md) | unsplit, primitive variables, characteristic tracing with sources in the traced states, full corner coupling; Colella–Sekora / McCorquodale–Colella limiter by default, Miller–Colella or Colella–Woodward as options; two-shock-type solver | [Almgren et al. (2010)](/sources/almgren-2010.md), §5.2 |
| [PLUTO](/software/pluto.md) | characteristic tracing with PPM ("fourth-order" interface values, eqs. 33–37) | [Mignone et al. (2012)](/sources/mignone-2012.md), §3.2 |
| [IDEFIX](/software/idefix.md) | primitive variables, extremum-preserving limiter, "4th order accurate on regularly spaced grids"; the code "at most globally second order" | [Lesur et al. (2023)](/sources/lesur-2023.md), §2.3 |
| [Quokka](/software/quokka.md) | method of lines (RK2-SSP), primitive variables, eq. 1.9 regrouped symmetrically; Miller–Colella flattening | [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.2.1 |
| [Cholla](/software/cholla.md) | PPM after Felker & Stone (2018) inside the VL+CT predictor–corrector | [Caddy & Schneider (2024)](/sources/caddy-2024.md), §2.2.6 |
| [GAMER](/software/gamer.md) | PLM or PPM; CTU + PPM + Roe in the scaling runs | [Zhang et al. (2018)](/sources/zhang-2018.md), §5.2 |
| [FLASH](/software/flash.md) | split PPM (FLASH 2.5), as described by Castro's authors | [Almgren et al. (2010)](/sources/almgren-2010.md), §5.2, §8.6 |
| GRMHD codes of the [EHT comparison](/results/eht-grmhd-code-comparison.md), [H-AMR](/software/h-amr.md) among them | all codes except iharm3D "applied the piecewise-parabolic-method (PPM)" | [Porth et al. (2019)](/sources/porth-2019.md), §6, Table 1 |

**Direct-Eulerian PPM.** Enzo's PPM is the §3 scheme as printed, split,
with the optional steepening, flattening and diffusive flux; it carries
the internal-energy equation of the
[dual-energy formalism](/methods/dual-energy-formalism.md)
([Bryan et al. (2014)](/sources/bryan-2014.md), §4.1, §4.1.1). Its
gravity source is time-centred as
$\frac{\Delta t}{2}\mathbf g^{n+1/2}(\rho^n + \rho^{n+1})$ (eq. 38),
whereas Colella & Woodward average the old- and new-time products of
density and acceleration (eq. 3.8): the same time-centring at a different
time level of the acceleration.

**Departures from the original limiter.**
* Quokka applies no Colella–Woodward slope limiting and no contact
  steepening: interface values are clipped to the range of the cell and
  its two neighbours, then the overshoot correction (reset 2 above) is
  applied, and at extrema the profile reverts to **linear** rather than
  constant (reset 1). It is formally second order; fourth-order PPM is
  rejected because it prevents per-cell local source evaluation
  ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.2.1,
  footnote 4).
* Castro's default extremum-preserving limiter "can yield negative
  densities" at a steep star–ambient interface; white-dwarf merger runs
  therefore use the original Colella–Woodward limiter
  (`castro.ppm_type = 1`), "strictly monotonicity preserving"
  ([Katz et al. (2016)](/sources/katz-2016.md), §2.1). This agrees with
  the construction of reset 1–2.
* Athena++, Castro, IDEFIX and Athena (as an option) use the
  Colella–Sekora family of extremum-preserving limiters, which the
  original paper does not contain (sources in the table).

**Flattening conventions.** Castro's flattening coefficient has the
opposite convention to FLASH's, with 1 meaning no flattening and 0 first
order ([Almgren et al. (2010)](/sources/almgren-2010.md), eqs. 27–29).
Colella & Woodward's coefficient is 1 for full flattening (eq. 4.1), so
FLASH keeps the original convention and Castro inverts it. Quokka finds
Colella–Woodward flattening insufficient in multiple dimensions, uses the
multidimensional flattening of Miller & Colella (2002) without artificial
viscosity, and calls flattening "essential" in its stationary shock tube,
LeBlanc, slow-shock and radiative-shock tests
([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.2.1,
§§3.1.3–3.1.6, 3.3.3). Its radiation transport reconstructs with PPM
without flattening (§2.2.2; see
[M1 radiation transport](/methods/m1-radiation-transport.md)). Later
Castro flattening follows Zingale & Katz (2015)
([Katz et al. (2016)](/sources/katz-2016.md), App. A).

**Source terms in the tracing.** Castro traces parabolically reconstructed
sources under each characteristic, so gravity reaches the transverse
Riemann solves, and Katz et al. argue that "the $\Delta t$ factor of the
original PPM paper should be $\Delta t/2$"
([Katz et al. (2016)](/sources/katz-2016.md), App. A, eqs. A10–A13).
Colella & Woodward print the full $\Delta t$ in the source corrections of
eqs. 2.9 and 3.7 and justify them only as making eq. 2.8 a
finite-difference approximation of the characteristic equations. Katz et
al. do not name the equation and argue within Castro's unsplit
reference-state construction, not the 1D sweeps of the original; this is
recorded as a qualification, not adjudicated.

**Integrators.** In the original, PPM is a single-step scheme with
characteristic tracing over $\Delta t$. Athena's CTU and PLUTO's
predictors keep characteristic tracing in an unsplit integrator
([Stone et al. (2008)](/sources/stone-2008.md), §4.2;
[Mignone et al. (2012)](/sources/mignone-2012.md), §3.2); see
[unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md).
Athena++, AthenaK, IDEFIX and Quokka use PPM as a pure reconstruction in
method-of-lines Runge–Kutta integrators. Method of lines with higher-order
reconstruction is unstable with forward Euler and stable with RK of
order at least 2, while "single-step characteristic-tracing PPM does not
have this problem"
([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.2.1; the same
finding as [Stone et al. (2020)](/sources/stone-2020.md), §3.2.3).

**Ghost cells.** Castro's proper-nesting buffer is set "since four ghost
cells are needed for the PPM algorithm"
([Almgren et al. (2010)](/sources/almgren-2010.md), §6); Enzo uses
$n_{\mathrm g} = 3$ for PPM ([Bryan et al. (2014)](/sources/bryan-2014.md), §3).
Colella & Woodward state no ghost-cell count. From their equations, the
interface value uses cells $i-1$ to $i+2$, a cell's parabola cells $i-2$
to $i+2$, and flattening uses pressures at $i \pm 2$ and the neighbours'
coefficients; the two codes' counts depend on which of these options
they implement.

## Measured behaviour across codes

* **Order.** In the second-order integrators PPM lowers the error constant,
  not the order: Athena's PPM is "formally second order" and lowers the
  error amplitude, with the lesson that "improving the convergence rate of
  the reconstruction algorithm is not always the best way to improve the
  overall accuracy" ([Stone et al. (2008)](/sources/stone-2008.md),
  §4.2.3); in Cholla, PPM is "formally second order" and its 3D
  linear-wave errors are about an order of magnitude below PLM's at
  unchanged order ([Caddy & Schneider (2024)](/sources/caddy-2024.md),
  §2.2.6, §3.1.1); AthenaK's PPM4 converges at second order on 1D linear
  waves, its PPMX at fourth ([Stone et al. (2026)](/sources/stone-2026.md),
  §3.1–3.2). Enzo's interface states are "third-order accurate in space
  and second-order accurate in time" and its multidimensional scheme
  "formally second-order accurate in space and time"
  ([Bryan et al. (2014)](/sources/bryan-2014.md), §4.1); Cholla's
  cosmology version calls its PPM "third-order accurate in space and
  second-order accurate in time"
  ([Villasenor et al. (2021)](/sources/villasenor-2021.md), §2.2). These
  agree with the original's third-order spatial and second-order temporal
  accuracy (p. 181), and with its fourth-order uniform-mesh interface value
  (eq. 1.9), which PLUTO and IDEFIX quote as "fourth-order".
* **Stalls.** IDEFIX's PPM+RK3 stops converging at high resolution on
  oblique MHD linear waves, as does an Athena++ PPM run with primitive
  reconstruction ([Lesur et al. (2023)](/sources/lesur-2023.md), §4.2);
  Athena++ reports RK3+PPM errors at least 10 times below VL2+PLM
  ([Stone et al. (2020)](/sources/stone-2020.md)). The open question is
  on [linear wave convergence](/benchmarks/linear-wave-convergence.md).
* **Oscillations next to MHD waves.** On the
  [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md), Athena's PPM
  shows small velocity oscillations ([Stone et al. (2008)](/sources/stone-2008.md),
  §8.2); Athena++ needs characteristic reconstruction
  ([Stone et al. (2020)](/sources/stone-2020.md), §3.3.3); Cholla's PPM
  oscillates with primitive or characteristic limiting, less than the PPM
  of Stone et al. (2008) ([Caddy & Schneider (2024)](/sources/caddy-2024.md),
  §3.1.4). Cholla's PPM also gave spurious oscillations in
  [field-loop advection](/benchmarks/field-loop-advection.md) and no gain
  over PLM on the
  [circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)
  (§3.1.2–3.1.3).
* **Dissipation.** PPM is slightly less diffusive than PLM on the
  [double Mach reflection](/benchmarks/double-mach-reflection.md)
  ([Stone et al. (2008)](/sources/stone-2008.md), §8.3;
  [Lesur et al. (2023)](/sources/lesur-2023.md), §4.1). In the
  [magnetized torus](/benchmarks/magnetized-torus-accretion.md), PLM runs
  of H-AMR and Athena++ give accretion rates "a factor of two to almost
  six" below their PPM runs; "even when the overall order of the scheme
  is fixed to second order, the PPM method can significantly reduce the
  dissipation" ([Porth et al. (2019)](/sources/porth-2019.md), App. A).
* **Cost.** PPM halves Athena++'s single-core MHD throughput relative to
  PLM ([Stone et al. (2020)](/sources/stone-2020.md), Table 2); Quokka's
  V100 Sedov throughput is 113.34 Mzones/s with PPM against 157.75 with
  PLM ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), Tables 1–2;
  see [cell-update throughput](/definitions/cell-updates-per-second.md)).
* **Split versus unsplit.** On single-mode
  [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md), Castro's
  split PLM, old-limiter and new-limiter PPM all show spurious secondary
  instabilities; unsplit new-limiter PPM is cleanest
  ([Almgren et al. (2010)](/sources/almgren-2010.md), §8.3).

# Citations

1. [Colella & Woodward (1984)](/sources/colella-1984.md), §§1–5, eqs. 1.4–1.17, 2.5–2.10, 3.1–3.8, 4.1–4.5, Appendix, Figs. 2, 6, 8.
2. [Bryan et al. (2014)](/sources/bryan-2014.md), §3, §4.1, §4.1.1–4.1.2 (arXiv v1).
3. [Stone et al. (2008)](/sources/stone-2008.md), §4.2, §4.2.3, §8.2–8.3.
4. [Stone et al. (2020)](/sources/stone-2020.md), §3.2.1, §3.2.3, §3.3.3, Table 2.
5. [Stone et al. (2026)](/sources/stone-2026.md), §3, §3.1–3.2 (arXiv v1).
6. [Almgren et al. (2010)](/sources/almgren-2010.md), §5.2, §6, §8.3, §8.6 (arXiv v1).
7. [Katz et al. (2016)](/sources/katz-2016.md), §2.1, App. A.
8. [Mignone et al. (2012)](/sources/mignone-2012.md), §3.2.
9. [Lesur et al. (2023)](/sources/lesur-2023.md), §2.3, §4.1–4.2 (arXiv v1).
10. [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.2.1–2.2.2, §§3.1.3–3.1.6, 3.3.3, Tables 1–2 (arXiv v2).
11. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §2.2.6, §3.1.1–3.1.4 (arXiv v2).
12. [Villasenor et al. (2021)](/sources/villasenor-2021.md), §2.2.
13. [Zhang et al. (2018)](/sources/zhang-2018.md), §5.2 (arXiv v4).
14. [Porth et al. (2019)](/sources/porth-2019.md), §6, Table 1, App. A (arXiv v2).

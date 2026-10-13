---
type: Method
title: "Inverse Lax–Wendroff numerical boundary treatment"
description: "Ghost-point values for wide-stencil high-order finite differences on Cartesian grids cut by an arbitrary boundary: a Taylor expansion from the boundary point whose normal derivatives come from the boundary data through the PDE (inflow) or from extrapolation (outflow), stable under the periodic CFL limit for any cut-cell distance; extended to sign-changing wind, exact conservation, moving bodies and fluid–structure interfaces."
status: established
aliases: [ILW, simplified inverse Lax-Wendroff, SILW, inverse Lax-Wendroff procedure, cut-cell boundary treatment, moving-boundary ILW]
tags: [boundary-treatment, finite-difference, weno, stability, cut-cell, moving-boundary, conservation]
timestamp: 2026-10-13T00:00:00Z
---

# Inverse Lax–Wendroff numerical boundary treatment

**The problem** ([Li, Shu & Zhang (2016)](/sources/li-2016.md), §1;
[Lu et al. (2016)](/sources/lu-2016.md), §1). A
[WENO](/methods/weno.md) or upwind-biased finite-difference stencil
needs values at ghost points beyond the boundary, and on a Cartesian
grid the boundary need not pass through grid points. Outflow ghost
values from Lagrange extrapolation are usually stable. Inflow is the
hard case, especially when the first grid point lies very close to the
boundary ($C_a \to 0$). This is the "cut-cell" problem, which leads to
instability or an extremely small time step. The alternatives are
body-fitted or overlapping meshes, embedded-boundary methods (second
order, then fifth order by Baeza et al. with filtered Lagrange
extrapolation), and immersed-boundary forcing. ILW resembles
immersed-boundary methods but does not change the PDE.

**The procedure** (Tan and Shu 2010, as summarized by
[Li, Shu & Zhang (2016)](/sources/li-2016.md), §2.3). With
$x_0 = a + C_a h$, assign each ghost point by a Taylor expansion about
the boundary,
$$u_{-\varsigma} = \sum_{k=0}^{n_{\mathrm b}-1}\frac{u^{*(k)}\,\left((C_a - \varsigma)h\right)^k}{k!},$$
which is $n_{\mathrm b}$-th order if each $u^{*(k)}$ is order
$n_{\mathrm b} - k$. At an inflow boundary of $u_t + f(u)_x = 0$, the
PDE converts normal derivatives into time derivatives of the data
$g(t)$, the reverse of the Lax–Wendroff procedure, hence the name:
$$u^{*(0)} = g,\qquad u^{*(1)} = -\frac{g'}{f'(g)},\qquad u^{*(2)} = \frac{f'(g)\,g'' - 2f''(g)\,(g')^2}{f'(g)^3},\ \dots$$
(checked on the page image). At an outflow boundary,
$u_{N+\varsigma} = \sum_{j=1}^{n_{\mathrm b}}e_j\,u_{N+1-j}$ with Lagrange
coefficients $e_j = \prod_{l \ne j}\frac{l + \varsigma - 1}{l - j}$. In
multi-D the expansion runs along the boundary normal through each ghost
point, with tangential derivatives from the boundary data
([Lu et al. (2016)](/sources/lu-2016.md), §2.5). Near shocks a
WENO-type extrapolation replaces Lagrange
([Lu et al. (2016)](/sources/lu-2016.md), §3;
[weighted extrapolation](/methods/weighted-extrapolation.md)).

**Simplified ILW (SILW).** The algebra of high derivatives in
multi-D, for systems and for moving boundaries is heavy. SILW obtains
only the first $k_{\mathrm{ILW}}$ of the $u^{*(k)}$ by ILW and
extrapolates the rest from interior points alone. Including the
boundary data in that extrapolant makes the scheme *less* stable
([Li, Shu & Zhang (2016)](/sources/li-2016.md), §2.4).

## Stability

([Li, Shu & Zhang (2016)](/sources/li-2016.md), §§3–5; linear advection,
upwind-biased schemes of orders 3–13, which are the linear-weight
versions of WENO, with SSP-RK3.) Two analyses agree for both the
semi-discrete and the fully discrete schemes. The rigorous one is the
GKS normal-mode analysis of the two quarter-plane problems. The other
visualizes the eigenvalue spectrum of the full matrix.
* Full ILW is stable for every $C_a$ under the same CFL limit as the
  periodic problem. With $g = 0$ all ghost values vanish, so the
  initial–boundary-value problem is as stable as the Cauchy problem.
  Outflow extrapolation is also stable (Goldberg's theorem). That result is
  one-dimensional. On complex 2D domains, where ghost values come from
  interpolation along normals, straight Lagrange extrapolation can turn
  the scheme mildly unstable, as Tan and Shu also observed. This is a
  difference of scope, not a contradiction
  ([weighted extrapolation](/methods/weighted-extrapolation.md);
  [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §§5.2, 6).
* SILW needs $k_{\mathrm{ILW}}$ at least the threshold below, for all
  $C_a$, at the periodic limit $\nu_{\max}$ of SSP-RK3 (Tables 3.1–3.2,
  read from the page images):

  | order | 3 | 5 | 7 | 9 | 11 | 13 |
  |---|---|---|---|---|---|---|
  | $\nu_{\max}$ | 1.62 | 1.43 | 1.24 | 1.12 | 1.04 | 0.99 |
  | minimum $k_{\mathrm{ILW}}$ | 2 | 3 | 4 | 6 | 8 | 10 |

  Below the threshold, instability appears in bands of $C_a$, typically
  but not only small $C_a$. The numerical tests reproduce every
  threshold.
* Nonlinear problems can be more stable. For Burgers with fifth order,
  $k_{\mathrm{ILW}} = 2$ sufficed because the boundary state is small
  relative to the global wave speed, and $k_{\mathrm{ILW}} = 2$ is
  stable at fifth order for $\nu \le 1.02$.
* Time-dependent data inside Runge–Kutta stages must be matched as
  $u^{(1)} \sim g + \Delta t\,g'$ and
  $u^{(2)} \sim g + \tfrac12\Delta t\,g' + \tfrac14\Delta t^2 g''$
  (Carpenter et al.). The naive $g(t^n + \Delta t)$, $g(t^n + \Delta t/2)$
  drops to second order (§2.2;
  [SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).

## Convection–diffusion and Navier–Stokes

([Lu et al. (2016)](/sources/lu-2016.md).) For
$u_t + f(u)_x = \mu u_{xx}$ the two limits need opposite treatments.
Pure convection takes $u_x$ from ILW and $u_{xx}$ from extrapolation.
Pure diffusion takes $u_x$ from extrapolation and $u_{xx}$ from ILW,
$u^{\mathrm{ilw}}_{xx} = \frac1\mu\left(g' + f'(g)\,u^{\mathrm{ext}}_x\right)$.
The general case blends the two (eqs. 2.10–2.11, checked on the page image):
$$\theta_{\mathrm{ILW}} = \frac{f'(g)^2h^2}{f'(g)^2h^2 + 9\mu^2},\qquad
u_x = \theta_{\mathrm{ILW}}u^{\mathrm{ilw}}_x + (1 - \theta_{\mathrm{ILW}})u^{\mathrm{ext}}_x,\qquad
u_{xx} = (1 - \theta_{\mathrm{ILW}})u^{\mathrm{ilw}}_{xx} + \theta_{\mathrm{ILW}}u^{\mathrm{ext}}_{xx}.$$
* **Systems.** The convective matrix is diagonalized for the
  convection-dominated treatment, imposing characteristic inflow data.
  The diffusion matrix is diagonalized for the diffusion-dominated one,
  and the blending is done per diffusive characteristic field.
* **Navier–Stokes.** The system is incompletely parabolic: there is no
  diffusion in the mass equation. Following Strikwerda and
  Gustafsson–Sundström, it is treated as a hyperbolic equation plus a
  parabolic system. When more conditions are given than the Euler limit needs,
  they are taken in the order $E$, $\rho u$, $\rho$.
* **Results.** Tests run at third order with $C_a = 10^{-6}$. They are
  stable and third order from $\mathrm{Re} = 1$ to $10^6$, including
  mixed regimes and a 45° polygonal boundary. A Mach 3 flow past a
  cylinder on a Cartesian grid captures the bow shock with an isothermal
  no-slip wall.

**Scale dependence.** [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md)
(§1) note that the outflow WENO extrapolation weights of the ILW papers
are neither dimensionless nor scale-independent, which a later
modification overcame, and they propose dimensionless weights
([weighted extrapolation](/methods/weighted-extrapolation.md)). The ILW
papers themselves later criticize the explicit $h$ in the Tan–Shu weights
and replace it with constant linear weights
([Lu et al. (2021)](/sources/lu-2021.md), §2.1). A 3D moving-body
variant still uses weights built from $h_x^2 + h_y^2 + h_z^2$
([Liu et al. (2022)](/sources/liu-2022.md), Appendix C).

## Sign-changing wind: expanding the flux separately

([Lu et al. (2021)](/sources/lu-2021.md), §2.) Every ILW derivative
above divides by $f'(g)$. The procedure therefore needs the wind to stay
away from zero at the boundary, and it loses robustness where a boundary
turns from inflow to outflow through a sonic point. The fix exploits the
fact that a Lax–Friedrichs split flux needs both $u$ and $f(u)$ at the
ghost points, and nothing forces the ghost flux to equal $f$ of the ghost
state. The two get separate Taylor expansions:
$$u_{-\varsigma} = \sum_{k=0}^{4}\frac{\left((C_a - \varsigma)h\right)^k}{k!}u^{*(k)},\qquad
f_{-\varsigma} = \sum_{k=0}^{4}\frac{\left((C_a - \varsigma)h\right)^k}{k!}f^{*(k)},$$
with $u^{*(0)} = g$, $f^{*(0)} = f(g)$ and $f^{*(1)} = -g'(t)$ from the
PDE. Every other derivative is extrapolated from the interior (eqs.
2.6–2.8). No eigenvalue appears in a denominator.
* **Systems.** At $x = a$ the signs of $v_x - c$, $v_x$ and $v_x + c$ decide
  how many conditions are imposed (four cases). The missing conserved
  component comes from the extrapolated outgoing characteristic
  variables, dividing only by entries of the eigenvector matrices. A
  solid wall is imposed as $\rho v_x = 0$ instead of by reflection. In 2D
  the same is done in a frame rotated to the boundary normal (§§2.2–2.3;
  [characteristic decomposition](/methods/characteristic-decomposition.md)).
* **Results.** Fifth order with FD-WENO in 1D and 2D, including
  boundaries where the wind changes sign and the
  [isentropic vortex](/benchmarks/isentropic-vortex.md) (§3). Double Mach
  reflection on the true ramp and the Mach 3
  [cylinder](/benchmarks/supersonic-cylinder-flow.md) run stably.
* **Stability caveat.** For $u$ itself only $u^{*(0)}$ comes from the
  data. That is below the SILW threshold in the table above, whose
  analysis does not cover the split $u$/$f$ expansion. The authors flag
  stability as a possible issue above fifth order (§4). No CFL number is
  printed for the runs.

## Conservation

([Ding, Shu & Zhang (2020)](/sources/ding-2020.md).) A conservative
finite-difference scheme conserves $h\sum_j u_j$, which approximates the
true total mass only to second order once the solution is not periodic
(eq. 1.7). With ILW boundaries the conservation error therefore sits at
truncation level: $10^{-3}$ to $10^{-8}$ in their tests (Tables 2.1,
2.8–2.10).
* **A high-order mass.** Define
  $\tilde{\mathcal M} = h\sum_j \varpi_j u_j$ with Mock–Lax boundary
  quadrature weights. For fifth order and a grid point on the boundary,
  $\varpi_0, \dots, \varpi_3 = \tfrac{251}{720}, \tfrac{299}{240}, \tfrac{211}{240}, \tfrac{739}{720}$,
  and $\varpi_j = 1$ further in (eq. 2.12). For a cut cell the weights
  are polynomials in the offset (eq. 2.14).
* **One modified flux.** By summation by parts, $\tilde{\mathcal M}$
  changes only by boundary terms. Requiring that the inflow term equal
  $\int_{t^n}^{t^{n+1}} f(g(t))\,dt$ fixes the single flux
  $\hat f_{-1/2}$ (eq. 2.18). The outflow side is left alone, since the
  high-order flux already gives the outgoing flux accurately. Only the
  Runge–Kutta-averaged flux of the final stage,
  $\hat f^{\mathrm{tot}}_{i+1/2} = \tfrac16\left(\hat f^{n} + \hat f^{(1)} + 4\hat f^{(2)}\right)_{i+1/2}$
  for TVD-RK3, is modified (eq. 2.10).
* **2D.** The weights come from polygon quadratures over the cut cells
  and are not unique (Appendix A). The defect is spread over one inflow
  flux per grid line, in proportion to the local flux magnitudes. $x$- or
  $y$-fluxes are chosen by whether the inflow normal lies within 45° of
  the $x$ direction (eqs. 2.37–2.41).
* **Effect.** The conservation error drops to $10^{-15}$–$10^{-16}$ with
  fifth order unchanged. Only one test differs visibly: in a long
  [interacting-blast-wave](/benchmarks/interacting-blast-waves.md) run
  ($t = 19$, $N = 800$) the non-conservative shock is misplaced (Fig. 2.5).
  The double Mach reflection on the real wedge and the Mach 3
  [cylinder](/benchmarks/supersonic-cylinder-flow.md) look the same with
  and without the fix.

## Moving boundaries

A boundary moving across the fixed grid changes three things
([Liu et al. (2023)](/sources/liu-2023.md), §2;
[Liu et al. (2022)](/sources/liu-2022.md), §§2–3).
* **Relative speed.** The data are differentiated along the moving
  boundary, $g'(t) = u_t + \dot a\,u_x$, so every ILW relation uses the
  speed relative to the boundary, $f'(g) - \dot a$. Inflow means
  $f'(g) - \dot a > 0$ at a left boundary (eq. 2.9).
* **Mesh motion.** The body may move at most one cell per step. Points
  that leave the body ("newly emerging points") need no special
  treatment beyond one extra ghost layer, after Tan and Shu (2011)
  ([Liu et al. (2023)](/sources/liu-2023.md), §2;
  [Liu et al. (2022)](/sources/liu-2022.md), eq. 15).
* **Runge–Kutta stages.** The boundary is held at its $t^n$ position.
  $u_t$ and $u_{tt}$ come from the material derivative and so involve the
  boundary velocity and acceleration. The mixed derivative $u_{tx}$,
  needed only to first order, is extrapolated linearly from the
  interior values of $u_t$ instead of being derived by Lax–Wendroff
  ([Liu et al. (2023)](/sources/liu-2023.md), eqs. 2.20–2.21;
  [Liu et al. (2022)](/sources/liu-2022.md), §3.2.3).

**Convection–diffusion on moving boundaries**
([Liu et al. (2023)](/sources/liu-2023.md), §2). With $\dot a = 0$ the
blending weight is that of Lu et al. (2016), with $f'(g)$ replaced by
$f'(g) - \dot a$. The ILW quotients are multiplied through by the weights,
and the two weights are regularized by $\epsilon_{\mathrm{ILW}} = 10^{-6}$:
$$\frac{(f'(g) - \dot a)^2h^2}{(f'(g) - \dot a)^2h^2 + (3\mu + \epsilon_{\mathrm{ILW}})^2}\ \ \text{on } u_x,\qquad
\frac{9\mu^2}{(f'(g) - \dot a + \epsilon_{\mathrm{ILW}})^2h^2 + 9\mu^2}\ \ \text{on the ILW part of } u_{xx}$$
(eqs. 2.15–2.18). Then nothing divides by a vanishing speed or diffusion
coefficient, and one algorithm covers pure convection, pure diffusion and
everything between. Third order holds in 1D and 2D, with the boundary
speed equal to the wave speed in one case, and for Navier–Stokes with an
isothermal no-slip wall on a flow-driven rigid body (§§3–4). There the
density at the wall comes from the outgoing acoustic characteristic, and
the blend uses the sound speed $c$ (eqs. 3.15–3.18). No stability
analysis is given.

**Three dimensions** ([Liu et al. (2022)](/sources/liu-2022.md), §3).
The frame rotated to the boundary normal is not unique in 3D. The ILW
ghost values do not depend on the choice of tangent vectors (Theorem 1,
proved for Euler, asserted for Navier–Stokes). A material derivative
defined only on the moving surface equals the usual one under
no-penetration (Theorem 2). With third-order WENO and SILW
($k_{\mathrm{ILW}} = 2$ of $n_{\mathrm b} = 3$, the threshold above),
an isentropic flow around a moving cylinder converges at third order
($L^1$ order 3.21 at $h = 1/40$, Table 1). Shock–cylinder and
shock–sphere runs at $M_s = 3$ and 6 are robust but reported only as
contour plots ([shock-driven cylinder lift-off](/benchmarks/shock-cylinder-lift-off.md)).

## Interfaces between two media

([Liu et al. (2025)](/sources/liu-2025.md), §§3–4.) At a moving interface
between a compressible fluid (third-order FD-WENO on a fixed Cartesian
grid) and an elastic solid (DG on a Lagrangian mesh), the boundary data
are themselves unknown. For each derivative order $k = 0, 1, 2$, the
normal derivatives of both sides are solved together in one local linear
system. Its rows are the outgoing characteristics of each medium, with
extrapolated data, and the velocity and traction conditions, together
with their time derivatives converted to space derivatives through the
PDEs. There is no sub-iteration.
* **Added mass.** A weakly coupled version, in which each solver takes
  the other side's value separately, is stable for all $C_a$ only while
  the fluid-to-solid density ratio stays below about 1.67. The coupled
  version is stable for all $C_a \in [0, 1)$ at density ratios from
  $10^{-2}$ to $10^2$ (eigenvalue spectra, §4, Figs. 5–6). The analysis
  runs at a Courant number of 0.2, set by the DG solid, far below the
  fluid scheme's own limit $\nu_{\max} = 1.62$.
* **Results.** Third order in 1D and 2D, and shock-induced deformation
  without oscillations (§5). The interface procedure can take more CPU
  time than the flow solvers (Tables 8, 10, 12).

## In the reviews (batch 6)

[Shu (2020)](/sources/shu-2020.md), §8, credits the inverse Lax–Wendroff procedure jointly to Huang,
Shu and Zhang (2008), boundary conditions for fast-sweeping WENO
Eikonal solvers, and to Tan and Shu (2010). He cites Goldberg and Tadmor
for earlier discussions of the procedure. Solid walls and symmetry lines
use (anti)symmetric ghosts. Outflow extrapolation of suitable order is
stable, and inflow is the hard case, especially for cut cells. The review
also lists the moving-boundary, convection–diffusion and simplified
variants above. In 2009, ghost values came from the boundary condition
with local characteristic decomposition, or from one-sided WENO
([Shu (2009)](/sources/shu-2009.md), §3.5.4).

**Later uses (batch 10).** The alternatives named above now have pages:
[immersed-boundary methods](/methods/immersed-boundary-method.md) and [cut-cell finite volume](/methods/cut-cell-finite-volume.md).
* *What "changes the PDE" means.* Peskin's method replaces the wall
  condition by a singular body force spread with a discrete delta
  function; it is equivalent to the stress-jump conditions but smears the
  interface over about one cell and is first order there ([Peskin (2002)](/sources/peskin-2002.md),
  §§3, 8). ILW keeps a sharp wall and a high-order ghost-point formula.
* *Ghost-cell IB for compressible flow* fills ghost points from an image
  point, as ILW does from the wall, but with interpolation from the fluid
  instead of the PDE. Near shocks, quadratic interpolation gave negative
  density and pressure, and the boundary order was dropped to
  inverse-distance weighting ([Seshadri & De (2020)](/sources/seshadri-2020.md), §4.6).
* *Conservation at the wall.* On a cold-wall hypersonic cylinder a
  ghost-cell solver misses the stagnation heat flux by a factor of about
  40 while a conservative cut-cell method matches the body-fitted result;
  switching off the conservative flux treatment in the cut-cell solver
  also gives a clearly wrong, though closer, heat flux. The authors
  attribute the failure to conservation, as a hypothesis ([Başkaya et al. (2024)](/sources/baskaya-2024.md), §§4.5, 5). This goes further than
  the conservation section above, where the error of non-conservative
  ILW was visible in one test only.

**Later uses (batch 11).** A boundary treatment without ghost points,
[Navier–Stokes characteristic boundary conditions](/methods/characteristic-boundary-conditions.md),
rejects extrapolation on well-posedness grounds: extrapolating a variable
"acts as an additional physical condition … and therefore overspecifies
the boundary conditions" ([Poinsot & Lele (1992)](/sources/poinsot-1992.md), §2.1).
With a non-dissipative sixth-order compact interior scheme, a
zeroth-order extrapolation outlet gave no steady state in a ducted shear
layer, wrong outlet profiles in Poiseuille flow, and spurious
short-wavelength waves that travelled upstream and spawned a vortex at
the inlet (§§4–6). Their argument is general (§2.1); their evidence is
zeroth-order extrapolation of primitive variables with a centred,
low-dissipation scheme, whereas Goldberg's theorem and the ILW tests
concern high-order extrapolation with upwind-biased WENO. The
disagreement is recorded as open on the
[NSCBC page](/methods/characteristic-boundary-conditions.md). The two agree on the rest: incoming
characteristics take boundary data and outgoing ones come from the
interior, and Navier–Stokes conditions are built as inviscid conditions
plus viscous ones following Strikwerda, as in the convection–diffusion
section above. NSCBC deviates from Strikwerda's counts in two cases
(§2.5).

# Citations

1. [Li, Shu & Zhang (2016)](/sources/li-2016.md), §§1–5 (§2.2–2.5 formulas and Tables 3.1–3.2 read from the page images).
2. [Lu et al. (2016)](/sources/lu-2016.md), §§1–4 (eqs. 2.10–2.11 read from the page image).
3. [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §1.
4. [Lu et al. (2021)](/sources/lu-2021.md), §§2–4 (eqs. 2.6–2.15 read from the page images).
5. [Ding, Shu & Zhang (2020)](/sources/ding-2020.md), §§1–2 (eqs. 2.8–2.18 read from the page images; Appendix A weights not transcribed).
6. [Liu et al. (2023)](/sources/liu-2023.md), §§2–4 (eqs. 2.9–2.21 read from the page images).
7. [Liu et al. (2022)](/sources/liu-2022.md), §§2–5, Appendices B–C.
8. [Liu et al. (2025)](/sources/liu-2025.md), §§3–5.
9. [Shu (2020)](/sources/shu-2020.md), §8.
10. [Shu (2009)](/sources/shu-2009.md), §3.5.4.
11. [Peskin (2002)](/sources/peskin-2002.md), §§3, 8.
12. [Seshadri & De (2020)](/sources/seshadri-2020.md), §4.6 (author manuscript).
13. [Başkaya et al. (2024)](/sources/baskaya-2024.md), §§4.5, 5 (arXiv v1).
14. [Poinsot & Lele (1992)](/sources/poinsot-1992.md), §§2.1, 2.5, 4–6.

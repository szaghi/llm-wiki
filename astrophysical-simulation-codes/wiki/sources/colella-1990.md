---
type: Source
title: "Colella (1990) — Multidimensional Upwind Methods for Hyperbolic Conservation Laws"
description: "Origin of the corner transport upwind (CTU) scheme: a first-order upwind scheme that integrates across zone corners, stable up to a Courant number of 1 per direction, extended to a second-order unsplit predictor–corrector with characteristic tracing, transverse Riemann-problem corrections and one edge Riemann solve, on quadrilateral grids and for 2D gas dynamics with multidimensional flattening; twice the Riemann solves and 50% more time than splitting in 2D, and 12 (or 6) solves per zone in 3D."
resource: "doi:10.1016/0021-9991(90)90233-Q"
source_kind: paper
authors: [Colella P.]
year: 1990
venue: "J. Comput. Phys. 87:171–200"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/1990-JCP-Colella-1010160021-99919090233-Q.pdf"
tags: [hydro, unsplit, time-integration, riemann-solver]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper builds second-order, conservative, explicit Godunov-type
methods for hyperbolic conservation laws in two space dimensions
**without operator splitting**: all fluxes are computed from one state at
$t^n$ and differenced together. The starting point is a first-order upwind
scheme for linear advection that integrates the upstream data over the
region the characteristics sweep through each zone edge, corners included;
the paper names it **corner transport upwind (CTU)** (§1). CTU is stable up
to a Courant number of 1 in each direction, where unsplit donor cell needs
the directional Courant numbers to sum to at most 1. Second order comes
from a predictor that extrapolates time-centred edge states with limited
normal slopes and an upwind transverse flux difference, characteristic
for systems, followed by one Riemann solve per edge (§2). The method is
extended to quadrilateral grids (§3) and specialized to 2D gas dynamics in
primitive variables with multidimensional flattening and a Lapidus
viscosity (§4). On the double Mach reflection the unsplit and split
results are "essentially identical" (§5). The unsplit scheme needs twice
the Riemann solves of the split one and about 50 % more time; in 3D it
would need 12 solves per zone per step against 3, or 6 with one
requirement relaxed (§6). See
[unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md).

# Key claims

Equations below are in the [registry](/notation.md) notation (scalar
$u$, advection velocity $(v_x, v_y)$ with both components positive, one
cell size $h$ although the paper allows different spacings per
direction; see the Notation map).

1. **Design requirements** (Introduction, p. 173). (1) For a 1D problem
   aligned with a grid direction the method reduces to the second-order
   Godunov method of Colella & Woodward; (2) the unlimited second-order
   and the fully limited first-order schemes have the same linear CFL
   limit as the operator-split scheme; (3) for linear advection the fully
   limited scheme satisfies a maximum principle. The paper is 2D only; in
   3D "such a study would strain the capabilities of present computer
   technology".
2. **First-order CTU** (§1, eqs. 1.2–1.4, Figs. 1–2). The new average is
   the area-weighted average of four upstream zones (eq. 1.2); in
   conservation form with the edge values (eq. 1.4)
   $$u^{n+1/2}_{i,j+1/2} = u^n_{i,j} + \frac{v_x\Delta t}{2h}\left(u^n_{i-1,j} - u^n_{i,j}\right),\qquad u^{n+1/2}_{i+1/2,j} = u^n_{i,j} + \frac{v_y\Delta t}{2h}\left(u^n_{i,j-1} - u^n_{i,j}\right),$$
   averages over the region swept through each edge, which account for
   transport across zone corners. CTU is first order and satisfies a
   maximum principle (non-negative weights). The transverse term is "a
   time-centered correction term to the donor-cell flux which estimates
   the effect on the flux of the gradients in the transverse direction";
   it removes a leading-order truncation term of donor cell that "is
   always destabilizing" (p. 175).
3. **Courant limits** (eqs. 1.5–1.6, p. 175). CTU:
   $\max(v_x\Delta t/h,\ v_y\Delta t/h) \le 1$ (sufficient); unsplit donor
   cell: $v_x\Delta t/h + v_y\Delta t/h \le 1$ (necessary), "as is easily
   checked using Fourier analysis".
4. **Second-order advection** (eqs. 1.7–1.9, pp. 175–176). The predictor
   adds the normal slope term, $(h/2 - v_x\Delta t/2)$ times the limited
   slope over $h$, to the first-order edge value; the slope is van Leer's
   monotonized central difference (eq. 1.9). Tangential derivatives are
   **upwind and unlimited**, normal ones **monotonized central**; with
   full limiting the scheme reduces to first-order CTU. A numerically
   evaluated amplification factor shows that "as long as the time step
   satisfies (1.5), the second-order algorithm does not amplify any
   Fourier modes" (p. 176). No monotonicity proof: oblique linear
   discontinuities "appear" monotone.
5. **Algorithm for systems** (§2, p. 179): monotonized central slopes;
   time-centred left and right edge states; a Riemann problem normal to
   each edge; conservative differencing of all fluxes at once. The basis
   is the multidimensional theory of characteristics (eqs. 2.3–2.4), in
   which the transverse derivative acts as a source in the 1D
   characteristic equation.
6. **Characteristic tracing** (eqs. 2.5–2.12, pp. 180–182). Slopes are
   limited in characteristic amplitudes after Harten (eqs. 2.5–2.6). The
   normal step extrapolates by $\pm h/2$ minus $\Delta t/2$ times the
   normal flux Jacobian applied to the slope (eq. 2.8), keeping only the
   characteristic components that move toward the edge, and the
   transverse step subtracts $\Delta t/2$ times the transverse flux
   derivative (eq. 2.9). Reference states are the extrapolation under the
   fastest wave toward the edge (eqs. 2.10–2.11); the explicit form
   (eq. 2.12) is "essentially that given in" Colella & Woodward for 1D
   PPM-type states with piecewise-linear profiles. The extra cost of the
   projection is small.
7. **Transverse correction, two choices** (eqs. 2.13–2.15, p. 182). The
   transverse term is an upwind difference of transverse fluxes from
   transverse Riemann problems (eq. 2.14), between either the cell-centred
   states (eq. 2.13: first-order Godunov transverse fluxes, "sufficiently
   accurate ... to yield an algorithm that is second-order accurate") or
   the normal-predictor states of the transverse edge (eq. 2.15), given for
   oblique discontinuities with "moderately strong nonlinear" behaviour,
   where (2.13) overshoots or spreads. Each edge thus needs a transverse
   Riemann problem besides the normal one.
8. **Consistency** (p. 183). For constant coefficients the time-centred
   edge state satisfies finite-difference approximations of the
   characteristic relations whatever the reference state (eq. 2.16); for
   smooth nonlinear solutions the same holds "modulo terms which are
   second order in the mesh spacing", provided the reference state
   differs from the cell value by $O(h)$; in this sense the predictor is
   "upstream-centered".
9. **Stability limit for systems** (eq. 2.17, p. 183).
   $$\Delta t\,\max_{i,j,p}\left(\frac{\vert\lambda^{(p)}_x\vert}{h},\ \frac{\vert\lambda^{(p)}_y\vert}{h}\right) \le 1,$$
   necessary and sufficient for Fourier stability of the fully limited
   and the unlimited schemes when the two flux Jacobians commute; the
   paper has "not proven (2.17) for any problem" in which they do not
   commute. It was the time-step control of all gas-dynamics runs, with
   "no evidence of instability".
10. **Quadrilateral grids** (§3, eqs. 3.1–3.12, Fig. 4). Metric terms from
    corner coordinates, a free-stream-exact predictor, and a Courant
    condition per zone interpreted as "Δt must be less than the time it
    takes a wave propagating in a direction normal to a zone edge to reach
    an opposite zone edge" (eq. 3.12), checked by numerical Fourier
    evaluation for advection under a linear map only.
11. **Gas dynamics** (§4, eqs. 4.1–4.8). Polytropic Euler equations in
    arc-length coordinates; the normal predictor works in primitive
    variables $(\rho, v_x, v_y, p)$ with **componentwise** limiting and
    closed-form eigenvectors; the runs use the steeper fourth-order-type
    slope of Colella (1985), capped by the monotonized central limiter
    (p. 191).
12. **Multidimensional flattening** (eqs. 4.9–4.10, pp. 192–193). The 1D
    flattening and Lapidus viscosity of Colella & Woodward carry over, with
    "One important modification": the slopes in **every** direction of a
    zone are multiplied by one coefficient, the minimum over directions,
    each itself the minimum of the zone's value and its upwind-in-pressure
    neighbour's. The coefficient is a function of
    $\vert p_{i+1} - p_{i-1}\vert/\vert p_{i+2} - p_{i-2}\vert$ equal to 1
    below 0.75, 0 above 0.85, linear between, active only in compression
    where $\vert p_{i+1} - p_{i-1}\vert/\min(p_{i+1}, p_{i-1}) > 0.33$;
    **1 means no flattening**. The 2D Lapidus viscosity has coefficient
    0.1; the values are those of the split algorithms of Colella &
    Woodward.
13. **Boundaries** (eqs. 4.11–4.12, pp. 193–194). The numerical domain of
    dependence of a point is the $9\times9$ block around it, so the mesh is
    extended by **four** points per side; reflecting walls get one-sided
    slopes and mirror Riemann states.
14. **Cost** (§6, p. 198). "Twice as many solutions to the Riemann problem
    as the corresponding operator split algorithm"; with the Riemann solve
    half of the 1D cost, the method takes **50 % more time**. A vectorized
    Cray-1 code advanced "about 24,000 zones by one time step in each cpu
    second" (regular reflection).
15. **Robustness** (§5 end, §6, pp. 197–198). The unsplit scheme is "more
    sensitive to various details of the implementation": choice (2.15) for
    the transverse derivative is "essential" (otherwise "considerably
    lower resolution in the jet along the wall in the double Mach
    region"), as are careful wall conditions and the multidimensional
    flattening, "required to eliminate low-amplitude noise behind the
    shocks"; split algorithms needed only 1D flattening per sweep.
16. **3D outlook** (§6, p. 199). The 3D analogue with properties (1)–(3)
    "requires 12 solutions to the Riemann problem per zone per time step",
    against 3 for splitting; relaxing (3), the maximum principle, with
    donor-cell-type transverse derivatives in the predictor gives **6**,
    which ignores transport from zones offset in all three directions
    (third-order truncation terms). Both give this paper's results on 2D
    problems aligned with the mesh; the choice is "undoubtedly problem
    dependent". **No Courant limit is stated for either 3D variant.**
17. **Motivation and uses** (Introduction, §5). The stated aim is "the
    same robustness and resolution as the existing operator split
    algorithms", for settings that need unsplit updates (front tracking,
    Lagrangian and porous-media codes, implicit–explicit hybrids). The
    method has been used on body-fitted meshes, in the AMR of Berger &
    Colella, in conservative front tracking and, in scalar form, for
    porous-media flow (p. 194).

# Tests

No convergence-rate study and no error norms: second order is argued by
truncation analysis (§§1–2), not measured.

1. **Steady regular reflection** (§5, Figs. 5–7, after Yee, Warming &
   Harten). $4\times1$ domain, $60\times20$ zones, reflecting floor,
   supersonic outflow, Dirichlet inflow and top states; 500 steps at a
   Courant number of 0.9 to steady state, 29° incident shock. Shocks
   "nearly monotone" and "fairly narrow", "about 2–2½ zones in the normal
   direction"; slightly broader with flattening, low-amplitude
   oscillations without it; no uncontrolled diffusion of
   supersonic–supersonic shocks.
2. **[Double Mach reflection](/benchmarks/double-mach-reflection.md)**
   (§5, Figs. 8–10, after Woodward & Colella). Mach 10 shock on a 30°
   wall, $400\times100$ zones, $h = 1/120$, wall starting 20 mesh lengths
   from the lower left corner, $t = 0.2$, matching "the finest grid
   results" of Woodward & Colella. Unsplit (Fig. 9) and operator split
   (Fig. 10) with the same parameters: "essentially identical". The
   Courant number is not printed.

# Notation map

| Paper | Canonical | Note |
|---|---|---|
| $\rho$ (§1, advected scalar) | $u$ | **collision**: registry $\rho$ is density; in §4 the paper's $\rho$ is density |
| $\mathbf u = (u, v)$ | $\mathbf v = (v_x, v_y)$ | **collision**: registry $u$ is the state |
| $U$, $M$ | $u$, $m$ | state and number of components |
| $\mathbf F = (F^x, F^y)$ | $\mathbf f$ | physical flux |
| $F^x_{i+1/2,j}$, $F^y_{i,j+1/2}$ | $\hat f_{i+1/2}$ per direction | numerical flux |
| $A^x$, $A^y$, $A^{\mathbf n}$ | $A(u)$ per direction | flux Jacobians |
| $\lambda^{x,\nu}$ | $\lambda^{(p)}_x$ | **collision**: the paper's wave index $\nu$ is the registry Courant number |
| $l^{x,\nu}$, $r^{x,\nu}$, $\alpha^{x,\nu}$ | in words | left and right eigenvectors, characteristic amplitudes; not in the registry |
| $\Delta x$, $\Delta y$ | $h$ | the paper allows different spacings per direction |
| $U^{n+1/2}_{i+1/2,j,L}$, $U^{n+1/2}_{i+1/2,j,R}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ at $t^{n+1/2}$ | |
| $\hat U$, $U^T$, $\tilde U_{L,R}$, $P_S$ | in words | normal-predictor state, transverse Riemann state, reference states, characteristic projection |
| $\Delta^xU$ | in words | limited slope |
| $c$ | $c_s$ | **collision**: $c$ is the speed of light |
| $E$ | $E/\rho$ | the paper's $E$ is per unit mass |
| $\chi$, $\tilde\chi$, $\zeta$, $\delta$, $z_0$, $z_1$ | in words | flattening coefficient and parameters; **collision** with $\chi_{\mathrm E}$; 1 = no flattening |
| CFL number | $\nu$ | |
| $(\xi, \eta)$, $J$, $(a, b)$ | in words | mapped and arc-length coordinates |

# Pages created or updated

* Created this Source page.
* Updated [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md):
  CTU from its primary source (construction, limits, cost, 3D counts),
  the attributions checked.
* Updated [Athena](/software/athena.md): the origin of the 12- and 6-solve
  counts.
* Updated [PLUTO](/software/pluto.md): its transverse fluxes are
  Colella's choice (2.13).
* Updated [PPM](/methods/ppm.md): Colella's multidimensional flattening
  and its convention.
* Updated [Double Mach reflection](/benchmarks/double-mach-reflection.md) (batch-8 section: unsplit against split in the CTU paper).

# Citations

1. Colella P. (1990), "Multidimensional upwind methods for hyperbolic
   conservation laws", J. Comput. Phys. 87(1):171–200,
   doi:10.1016/0021-9991(90)90233-Q. Local file:
   `/home/stefano/papers/mosaic/astrophysical-simulation-codes/1990-JCP-Colella-1010160021-99919090233-Q.pdf`.
   * **Version read.** The published journal version, a 30-page scan
     (received June 20, 1984; revised October 21, 1987). Not a preprint.
     The bibliography's suggestion that LBL-17023 (`colella-1989`) is a
     report version of this paper is not verified: the paper does not
     mention that report.
   * **Identity.** Checked on Crossref: title, single author, vol. 87,
     issue 1, pp. 171–200, issued 1990-03.
   * **How it was read.** The OCR layer is poor; every equation and the
     reference list were read from rendered pages (110 dpi, with 220 dpi
     zooms of pp. 191–193, 195, 197, 199–200). The quadrilateral-grid
     formulas (eqs. 3.4–3.11, 4.5–4.7) were read but are given in
     structure only.
   * **Recorded as printed.** (a) p. 192 says the transverse Riemann
     states of the §5 calculations are the cell-centred ones ("we use the
     latter choice", the (2.13) type), while pp. 197–198 call choice
     (2.15) "essential" for those runs; not resolved. (b) p. 191: the
     second index of the fourth-order-type slope difference is printed
     $i+1$ twice (reader's reading: $i-1$ meant). (c) p. 175: the
     donor-cell edge values are printed as the cell's own value at the
     upwind edges, an index that looks shifted for $v_x, v_y > 0$ (reader's
     reading). (d) eq. 4.9: the operator in the compression test's first
     index is illegible in the scan. (e) The double Mach mesh,
     $400\times100$ zones at $h = 1/120$, implies a $3.33\times0.83$
     domain, smaller than Woodward & Colella's $4\times1$ (inferred, not
     printed).
   * **Reference list:** 25 printed entries (Crossref counts 26; the
     extra item is not identified). Colella's MUSCL paper, printed SIAM J.
     Sci. Stat. Comput. 6:107 (an interior page; Crossref 6:104–117), is
     `colella-1985-c`; Colella & Glaz, J. Comput. Phys. 59:264, is
     `colella-1985`; Harten (1983), 49:357, is `harten-1983-b`; van Leer
     (1977), 23:276, is `vanleer-1977-b`; van Leer's chapter in Computing
     Methods in Applied Sciences and Engineering VI is `vanleer-1984-b`,
     not the private communication `vanleer-1984`; Chern & Colella "in
     press" (UCRL-97200) is `chern-1990`, kept apart from `chern-1989`
     (same authors and journal, no year in either; unresolved). Saltzman
     & Colella (LAUR-85-678, `saltzman-1985`) is cited for Lagrangian grid
     motion. Bibliography: 2314 entries.

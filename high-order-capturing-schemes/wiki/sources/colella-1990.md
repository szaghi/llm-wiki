---
type: Source
title: "Colella (1990) — Multidimensional upwind methods for hyperbolic conservation laws"
description: "Second-order conservative unsplit Godunov schemes in 2D: corner transport upwind for advection (Courant limit max ≤ 1, against the sum form of donor cell), a predictor–corrector for systems with characteristic limiting, upwind tracing and a transverse correction from transverse Riemann fluxes, extensions to quadrilateral grids and gas dynamics, and the 12- or 6-solve 3D variants."
resource: "doi:10.1016/0021-9991(90)90233-Q"
source_kind: paper
authors: [Colella P.]
year: 1990
venue: "J. Comput. Phys. 87:171–200"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1990-JCP-Colella-1010160021-99919090233-Q.pdf"
tags: [godunov, unsplit, multidimensional, cfl, characteristic-tracing, gas-dynamics]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

Colella builds second-order, conservative, unsplit Godunov-type schemes
in two dimensions: every flux is evaluated and differenced in one step
from the characteristic form of the full multidimensional equations at
each edge, with no operator splitting. For scalar advection the
first-order member, corner transport upwind (CTU), averages the
piecewise-constant data over the region the characteristics sweep back
from each cell, corners included; this adds a transverse term to donor
cell and raises the Courant limit from the sum of the directional Courant
numbers to their maximum. For systems the scheme is a predictor–corrector:
characteristically limited slopes, time-centred edge states by upwind
tracing, a transverse correction from differences of transverse Riemann
fluxes, a normal Riemann problem and a conservative update. The paper
extends it to smooth quadrilateral grids, specializes it to polytropic
Euler with multidimensional flattening and reflecting walls, and runs a
steady regular shock reflection and the Mach 10 double Mach reflection.
The unsplit scheme matches the resolution of the split one at twice the
Riemann solves and is more sensitive to implementation details.

# Key claims

1. **Design criteria** (Introduction, p. 173). (1) On a grid-aligned 1D
   problem the scheme reduces to the second-order Godunov method of
   Colella and Woodward; (2) the unlimited second-order and the fully
   limited first-order schemes have the same linear Courant limit, equal
   to that of operator splitting; (3) the fully limited scheme obeys a
   maximum principle for linear advection. TVD is rejected as the
   multi-D criterion because, by Goodman and LeVeque, it implies at most
   first order.
2. **CTU for advection** (§1, eqs. 1.1–1.4, Figs. 1–2). The new value is
   a nonnegative-weight average of four cells over the back-traced cell
   (eq. 1.2); in conservation form the edge states carry a transverse
   upwind term (eqs. 1.3–1.4,
   [corner transport upwind](/methods/corner-transport-upwind.md)). First
   order, maximum principle. Donor cell is the same scheme without the
   transverse term, "subtracting from the donor cell algorithm a term
   which, to leading order in the truncation error, is always
   destabilizing" (p. 175).
3. **Courant limits** (eqs. 1.5–1.6, p. 175). CTU:
   $\max(v_x\Delta t/h_x,\ v_y\Delta t/h_y) \le 1$ (sufficient); donor
   cell: $v_x\Delta t/h_x + v_y\Delta t/h_y \le 1$ (necessary), "as is
   easily checked using Fourier analysis". The second-order scheme
   amplifies no Fourier mode under eq. 1.5, checked numerically on the
   amplification factor (p. 176).
4. **Second-order advection** (eqs. 1.8–1.9, p. 176). The edge state
   adds an MC-limited normal slope (van Leer's monotonized central
   difference, eq. 1.9); transverse differences are upwind and
   unlimited. This asymmetry makes the fully limited scheme reduce to
   first-order CTU. Oblique linear discontinuities "appear" monotone.
5. **Multidimensional characteristics** (§2, eqs. 2.3–2.4). On
   characteristic surfaces the system reduces to 1D characteristic
   equations normal to an edge with tangential derivatives as sources.
6. **Algorithm for systems** (§2, p. 179): MC slopes; time-centred edge
   states; Riemann problems for the equations projected on the edge
   normal; conservative differencing of all fluxes at once.
7. **Characteristic limiting** (eqs. 2.5–2.6, after Harten). Central and
   doubled one-sided differences are expanded on the right
   eigenvectors; each coefficient is the smallest in magnitude with the
   sign of the central one if the one-sided ones agree in sign, else 0.
   Riemann-invariant interpolation is the alternative, available only
   for special systems.
8. **Normal predictor** (eqs. 2.7–2.12). Robustness changes, redundant
   for constant coefficients: components of waves not propagating toward
   the edge are discarded, and reference states are the trace of the
   farthest-reaching wave (eqs. 2.10–2.11). The explicit result (eq.
   2.12) is the PPM characteristic tracing of Colella and Woodward for
   piecewise-linear data.
9. **Transverse correction** (eqs. 2.13–2.15, p. 182). The normal
   predicted state is corrected by $-\tfrac{\Delta t}{2h_y}$ times the
   difference of two transverse Riemann fluxes (eq. 2.14). Inputs: cell
   averages (eq. 2.13), transverse first-order Godunov, "sufficiently
   accurate … to yield an algorithm that is second-order accurate"; or
   the normal-predicted states of the transverse edges (eq. 2.15), for
   "moderately strong nonlinear discontinuities which are oblique to the
   mesh".
10. **Upstream centring** (eq. 2.16, p. 183). For constant coefficients
    the edge value satisfies finite-difference approximations to the
    characteristic relations through the edge whatever the reference
    states; for smooth nonlinear solutions up to second-order terms.
11. **System Courant limit** (eq. 2.17). The largest directional Courant
    number over fields and cells at most 1; proved necessary and
    sufficient, for the limited and unlimited scheme, only when the two
    Jacobians commute. Otherwise unproved, but used as the gas-dynamics
    time-step control with "no evidence of instability".
12. **Quadrilateral grids** (§3, eqs. 3.1–3.12). Finite-volume update
    with edge normals and zone areas; the metric term is differenced to
    cancel the transverse flux difference exactly without transverse
    gradients (eq. 3.10); Courant condition eq. 3.12: a wave normal to an
    edge must not reach the opposite edge in $\Delta t$.
13. **Gas dynamics** (§4). Predictor in primitive variables along local
    arc-length directions with explicit eigenvectors (p. 190); slopes
    from a fourth-order limited central difference (p. 191);
    multidimensional flattening, one coefficient (minimum over the two
    directions) multiplying the slopes in both (eqs. 4.9–4.10), with
    $\delta = 0.33$, $z_0 = 0.75$, $z_1 = 0.85$ and a 2D Lapidus viscous
    flux with coefficient 0.1, "all as in" Colella and Woodward;
    reflecting walls by mirror states (eqs. 4.11–4.12). The numerical
    domain of dependence is a $9\times9$ block (4 ghost cells).
14. **Cost** (§6, pp. 198–199). 2D: twice the Riemann solves of
    splitting, about 50 % more time, about 24,000 zones per CPU second
    on a vectorized Cray 1. 3D: the full CTU analogue of eq. 1.2 needs 12
    Riemann solves per zone per step against 3 for splitting; relaxing
    criterion (3), with donor-cell transverse predictors that drop the
    corner-coupling (third-order truncation) terms, needs 6. Which is
    appropriate is "undoubtedly problem dependent". No 3D Courant limit
    is stated.
15. **AMR** (§5). The gas-dynamics algorithm "has been used in adaptive
    mesh refinement calculations", citing Berger and Colella.

# Tests

1. **Steady regular shock reflection** (§5, Figs. 5–7; Yee, Warming and
   Harten's set-up). Domain $4\times1$, $60\times20$ grid
   ($h_x = 1/15$, $h_y = 1/20$), incident angle 29°; reflecting bottom,
   supersonic outflow on the right, Dirichlet left and top. Left state
   $(\rho, v_x, v_y, p) = (1, 2.9, 0, 1/1.4)$; top state
   $(1.69997, 2.61934, v_y, 1.52819)$ with $\vert v_y\vert = 0.50632$
   (sign not legible, see Citations). 500 steps at Courant number 0.9 to
   steady state. Shocks about 2–2½ zones wide normal to the shock; with
   flattening slightly broader, spread on the high-pressure side; without
   it, low-amplitude oscillations (Fig. 7, profile at $y = 0.525$).
   Unlike first-order upwind, supersonic–supersonic shocks do not diffuse
   uncontrollably; the difficulty is keeping them broad enough to
   dissipate.
2. **Double Mach reflection** (§5, Figs. 8–10; Woodward and Colella's
   set-up). Mach 10 shock on a 30° ramp, $400\times100$,
   $h_x = h_y = 1/100$, wall starting 20 mesh lengths from the lower-left
   corner, shown at $t = 0.2$ (the finest grid of Woodward and Colella).
   Unsplit (Fig. 9) and split (Fig. 10) are "essentially identical", but
   the unsplit scheme needed eq. 2.15 rather than 2.13 (or the wall jet
   loses resolution), careful reflecting-wall conditions, and
   multidimensional flattening against low-amplitude post-shock noise.
   Visual comparison only; no error norms.

# Notation map

| Colella (1990) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $\mathbf F = (F^x, F^y)$ | $u$, $\mathbf f(u)$ | |
| $M$ (number of equations) | $m$ | |
| $A^x$, $A^{\mathbf n}$ | $A$ (per direction) | |
| $\lambda^{\mathbf n,\nu}$, $l^{\mathbf n,\nu}$, $r^{\mathbf n,\nu}$ | $\lambda^{(p)}$, $\ell^{(p)}$, $r^{(p)}$ | **collision**: the paper's field index $\nu$ is the registry CFL number |
| $\Delta x$, $\Delta y$ | $h_x$, $h_y$ | |
| $U^n_{i,j}$ | $\bar u^n_{i,j}$ | cell average |
| $U^{n+1/2}_{i+1/2,j,L}$, $U^{n+1/2}_{i+1/2,j,R}$ | time-centred $u^-_{i+1/2,j}$, $u^+_{i+1/2,j}$ | |
| $\Delta^x U$ | $\delta^{\mathrm{MC}}\bar u_{i,j}$ (taken in $x$) | **collision**: registry $\Delta^l w_i$ and the PPM $\Delta u_i$ |
| $\alpha^\nu$, $\alpha^\nu_C$, $\alpha^\nu_L$, $\alpha^\nu_R$ | characteristic amplitudes $\ell^{(p)}\cdot(\text{difference})$, words | **collision**: registry $\alpha$ is the Lax–Friedrichs speed |
| $P_S$ | words (projection onto waves moving toward the edge) | |
| $\tilde U_L$, $\tilde U_R$; $U^T$ | words (reference states; transverse Riemann solution) | |
| $\rho$ (advected scalar, §1) | $u$ | **collision**: registry $\rho$ is density |
| $\mathbf u = (u, v)$ (advection velocity, §1) | $\mathbf v = (v_x, v_y)$ | **collision**: registry $u$ is the state |
| $\sigma_{i,j}$ (zone area) | $\vert I_{i,j}\vert$ | **collision**: registry $\sigma$ is the Hu–Adams–Shu constant |
| $J$, $(\xi, \eta)$ | $\mathcal J$, $\mathbf X$ | **collision**: registry $\xi$ is the scaled wavenumber |
| $\chi_{i,j}$ (flattening factor on the slope) | $1 - \phi_i$ | Colella's $\chi = 1$ means no flattening, the opposite of $\phi_i$; **collision**: TENO $\chi_k$ |
| $\delta$, $z_0$, $z_1$ | words (flattening thresholds) | **collision**: TENO $\delta_k$, DMP $\delta_0$ |
| $(\rho, u, v, p)$, $\gamma$, $c$ | $\rho$, $\mathbf v$, $p$, $\gamma$, $c$ | |

# Pages created or updated

* Created [Corner transport upwind (CTU)](/methods/corner-transport-upwind.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md)
  (batch-17 block: the 2D limit 1/2 is the donor-cell limit, CTU's is 1).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md)
  (batch-17 block: Harten-style characteristic limiting of slopes,
  wave-discarding tracing).
* Updated [Piecewise parabolic method (PPM)](/methods/ppm.md) (batch-17
  block: the unsplit corner-coupled framework, multidimensional
  flattening).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/1990-JCP-Colella-1010160021-99919090233-Q.pdf`.
   * **Version read.** The published journal version, a 30-page scanned
     image PDF with an OCR layer. Received June 20, 1984; revised October
     21, 1987.
   * **Identity.** doi:10.1016/0021-9991(90)90233-Q, not printed on the
     page; taken from the PDF's PII and checked on Crossref:
     "Multidimensional upwind methods for hyperbolic conservation laws",
     sole author Phillip Colella, J. Comput. Phys. 87(1):171–200,
     published in print March 1990.
   * **How it was read.** The OCR layer garbles the equations, so every
     equation was read from page images (110 dpi, selected pages at
     200–250 dpi). Eqs. 3.8–3.11, 4.3–4.8 and the fourth-order slope
     formula (p. 191) were read and summarized, not transcribed.
   * **Recorded as printed** (reader's reading).
     - The top boundary state of the regular-reflection test prints
       $v_y$ as ".50632"; a minus sign may be lost in the scan, and the
       value is not reproduced with a sign.
     - The signs of the right-state sum in eq. 2.12 are small on the scan
       and are taken as printed.
     - Where the OCR and the scan differ (the p. 191 limiter citation
       "[5]"; the page of ref. 18, "47" on the scan, 41 in the OCR), the
       scan was followed.
   * **Reference list:** 25 printed entries (Crossref counts 26), all
     merged. Colella's MUSCL paper, printed SIAM J. Sci. Stat. Comput.
     6:107, lands on `colella-1985` (6:104); a Richtmyer & Morton title
     variant on `richtmyer-1967`; the Computing Methods VI chapter on
     `vanleer-1984-b`. Chern & Colella "in press", undated, is
     `chern-1990`. Bibliography: 3270 entries.

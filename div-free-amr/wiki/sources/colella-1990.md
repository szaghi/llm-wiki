---
type: Source
title: "Colella (1990) — Multidimensional Upwind Methods for Hyperbolic Conservation Laws"
description: "Second-order, conservative, dimensionally unsplit Godunov schemes built on the corner transport upwind (CTU) scheme: transverse corner corrections, a per-direction CFL limit of 1, characteristic tracing and limiting for systems, mapped grids, gas dynamics, and the 12- and 6-solve 3D counts; pure hydrodynamics."
resource: "doi:10.1016/0021-9991(90)90233-Q"
source_kind: paper
authors: [Colella P.]
year: 1990
venue: "J. Comput. Phys. 87:171-200"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1990-JCP-Colella-1010160021-99919090233-Q.pdf"
tags: [ctu, unsplit, godunov, shock-capturing]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper builds second-order, conservative, **dimensionally unsplit**
Godunov-type finite-volume schemes for hyperbolic conservation laws in 2D.
Edge fluxes come from the characteristic form of the full
multidimensional equations at the zone edge, and all fluxes are evaluated
and differenced at once, with no operator splitting. The scalar prototype
is the first-order **corner transport upwind (CTU)** scheme (§1,
eqs. 1.2–1.4): it averages the piecewise-constant data over the upstream
region swept by the characteristics, which adds a transverse "corner"
correction to donor cell and raises the stability limit from the sum of
the directional Courant numbers to their maximum. The scheme is extended
to second order by a predictor–corrector, to systems (§2: characteristic
limiting and tracing, transverse correction by Riemann problems), to
quadrilateral grids (§3) and to polytropic gas dynamics (§4). Tests (§5)
show resolution essentially identical to the operator-split second-order
Godunov method at about 50% more cost. It is compiled in
[Corner transport upwind (CTU)](/methods/corner-transport-upwind.md).

**Bearing on divergence constraints: none.** The paper is pure
hydrodynamics; it mentions neither $\nabla\cdot\mathbf B$, nor
incompressibility, nor a discrete divergence. The bundle's MHD pages take
from it only the unsplit integrator.

# Key claims

1. **Design criteria** (Introduction, p. 173). (1) For 1D problems aligned
   with a grid direction the scheme reduces to the second-order Godunov
   method of Colella–Woodward (ref. [7]). (2) The unlimited second-order
   and fully limited first-order schemes share, as linear schemes, the CFL
   limit of the operator-split scheme. (3) For linear advection the fully
   limited scheme satisfies a maximum principle. TVD is rejected as a
   multi-D criterion because Goodman–LeVeque show that it implies at most
   first order (p. 172). The motives for unsplitting are front tracking,
   coupling to implicit methods and existing unsplit application codes
   (p. 172).
2. **First-order CTU** (§1, eqs. 1.2–1.4, Figs. 1–2). For
   $\partial_t\rho + \mathbf u\cdot\nabla\rho = 0$, $u, v > 0$, the new
   value is the area-weighted average of the four upstream zones swept by
   $\mathbf u$ (eq. 1.2). In conservation form
   $$\rho^{n+1}_{i,j} = \rho^n_{i,j} + \frac{u\Delta t}{\Delta x}\big(\rho^{n+1/2}_{i-1/2,j} - \rho^{n+1/2}_{i+1/2,j}\big) + \frac{v\Delta t}{\Delta y}\big(\rho^{n+1/2}_{i,j-1/2} - \rho^{n+1/2}_{i,j+1/2}\big)$$
   (eq. 1.3), with edge values
   $\rho^{n+1/2}_{i+1/2,j} = \rho^n_{i,j} + \frac{v\Delta t}{2\Delta y}(\rho^n_{i,j-1} - \rho^n_{i,j})$
   and the $y$-edge analogue (eq. 1.4). The name: "it takes into account
   the effect of information propagating across corners of zones in
   calculating the flux" (p. 174). Edge values are nonnegative-weight
   sums, hence the maximum principle.
3. **CFL, unsplit against donor cell** (§1, eqs. 1.5–1.6). CTU:
   $\max(u\Delta t/\Delta x,\ v\Delta t/\Delta y) \le 1$ (1.5). Donor
   cell: $u\Delta t/\Delta x + v\Delta t/\Delta y \le 1$ (1.6). (1.5) is
   stated sufficient and (1.6) necessary, "easily checked using Fourier
   analysis". Donor cell is CTU without the time-centred transverse
   correction, and dropping that correction "is always destabilizing"
   (p. 175).
4. **Second-order scalar scheme** (§1, eqs. 1.7–1.9). The edge value adds
   the normal-derivative term,
   $\rho^{n+1/2}_{i+1/2,j} = \rho^n_{i,j} + (\frac{\Delta x}{2} - u\frac{\Delta t}{2})\frac{\Delta^x\rho_{i,j}}{\Delta x} - \frac{v\Delta t}{2\Delta y}(\rho^n_{i,j} - \rho^n_{i,j-1})$
   (1.8), with $\Delta^x\rho$ van Leer's monotonized central difference
   (1.9). Transverse derivatives are upwind differences, not limited;
   normal derivatives are limited central differences (p. 176). Only so
   does full limiting recover first-order CTU. Second order in smooth
   regions by a linear error analysis; the numerically evaluated
   amplification factor has no amplified mode under (1.5) (p. 176).
5. **Systems: the four steps** (§2, p. 179). Monotonized slopes;
   time-centred left and right edge states; a Riemann problem normal to
   the edge; conservative differencing of the edge fluxes in both
   directions.
6. **Characteristic limiting** (§2, eqs. 2.5–2.6, after Harten). Central
   and one-sided differences are expanded in the right eigenvectors and
   each amplitude is limited: the minimum modulus of the three, with the
   sign of the central one, when the one-sided amplitudes agree in sign,
   else zero. In (2.5) the central difference carries the factor 1/2 and
   the one-sided ones the factor 2, so this is the limiter of (1.9) in
   characteristic variables.
7. **Characteristic tracing** (§2, eqs. 2.7–2.12). A normal step (2.8)
   and a transverse step (2.9). Components whose characteristics do not
   propagate toward the edge are discarded by the projection $P_S$ (2.10);
   reference states (2.11) turn (2.12) into the 1D tracing of [7] for
   piecewise-linear data, "essentially that given in [7]" (p. 182). For
   constant coefficients the two changes "lead to identical values", but
   give "a somewhat more robust algorithm for strongly nonlinear problems"
   (p. 181).
8. **Transverse correction by Riemann problems** (§2, eqs. 2.13–2.16).
   The transverse flux derivative is a difference of Godunov fluxes from
   transverse Riemann problems (2.14). The simplest states, the two zone
   values (2.13), suffice for second order. Using the predicted edge
   states (2.15) keeps a strong oblique discontinuity from overshooting or
   spreading; in §5 this "is essential" for the double-Mach wall jet
   (pp. 197–198). For constant coefficients the predictor satisfies the
   characteristic relations along the characteristic surfaces through the
   edge (2.16): "upstream-centered for smooth solutions" (p. 183).
9. **CFL for systems** (§2, eq. 2.17):
   $\max_{i,j,\nu}(|\lambda^{x,\nu}_{i,j}\Delta t/\Delta x|,\ |\lambda^{y,\nu}_{i,j}\Delta t/\Delta y|) \le 1$.
   It is necessary and sufficient for Fourier stability only when the two
   flux Jacobians commute. "We have not proven (2.17) for any problem for
   which $A^x$ and $A^y$ do not commute"; it is used for all gas-dynamics
   runs with "no evidence of instability" (p. 183).
10. **Quadrilateral grids** (§3, eqs. 3.1–3.12). A mapped formulation
    written only through corner-coordinate differences; a geometric term
    (3.10) that exactly cancels the flux difference when there are no
    transverse gradients; the CFL (3.12): "Δt must be less than the time
    it takes a wave propagating in a direction normal to a zone edge to
    reach an opposite zone edge" (p. 187).
11. **Gas dynamics** (§4, eqs. 4.1–4.12). Limiting in primitive variables
    in an arc-length frame; the fourth-order slope of Colella (1985);
    **multidimensional flattening** with one coefficient for both
    directions, the minimum of the two directional ones ($\delta = 0.33$,
    $z_0 = 0.75$, $z_1 = 0.85$; eqs. 4.9–4.10); 2D Lapidus artificial
    viscosity, coefficient 0.1 (p. 193); reflecting-wall slopes and
    Riemann states (4.11–4.12). The domain of dependence is a 9×9 block,
    so 4 ghost cells are needed per side (p. 193).
12. **Cost and 3D** (§6, pp. 198–199).
    * In 2D, twice as many Riemann solutions as operator splitting, about
      50% more time; about 24,000 zones/s on a Cray-1.
    * A 3D analogue of (1.2) satisfying criteria (1)–(3) needs **12
      Riemann solutions per zone per time step**, against 3 for operator
      splitting.
    * Relaxing criterion (3), with donor-cell-type transverse predictors
      that ignore transport from zones offset in all three directions
      (third-order truncation terms), needs **6**.
    * Which 3D formulation is appropriate is "undoubtedly problem
      dependent".
    * Quadratic (PPM) interpolants as in [7] are named a straightforward
      extension (p. 198); a Lagrangian 2D version is not.

# Tests

1. **Steady regular shock reflection** (§5, Figs. 5–7), after Yee,
   Warming & Harten. Domain 4×1, $60\times20$ grid; reflecting bottom,
   supersonic outflow right, Dirichlet data on the other sides; 500 steps
   at CFL 0.9 to steady state. Shocks about 2–2½ zones wide normal to the
   front; without flattening, low-amplitude oscillations (Fig. 7, profile
   at $y = 0.525$). Unlike first-order upwind, the difficulty at
   supersonic shocks is ensuring *enough* dissipation.
2. **Double Mach reflection** (§5, Figs. 8–10), after Woodward & Colella.
   Mach 10 shock on a 30° wedge; $400\times100$ grid, wall starting 20
   zones from the lower-left corner, $\Delta x = \Delta y = 1/100$,
   $t = 0.2$, "the finest grid results in [22]". Unsplit (Fig. 9) and
   operator-split (Fig. 10) results are "essentially identical". Required:
   the transverse states (2.15) rather than (2.13), care with the
   reflecting boundaries, and the multidimensional flattening (4.10),
   which removes post-shock noise; split schemes need only 1D flattening
   per sweep.

No magnetic test, no divergence measurement, no convergence table.

# Notation map

| Colella (1990) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta x$, $\Delta y$ | $h$ (per direction) | |
| $\Delta t$; superscripts $n$, $n+1/2$, $n+1$ | $\Delta t$; $n$, $n+1/2$, $n+1$ | |
| $\rho$ (advected scalar, §1) | $w$ | **collision:** $\rho$ is density in §4 |
| $\rho^n_{i,j}$, $U^n_{i,j}$ | $\bar w_{i,j}$ | zone averages |
| $U_{i+1/2,j,L}$, $U_{i+1/2,j,R}$ | $w^-_{i+1/2}$, $w^+_{i+1/2}$ | edge states from the left and right zone |
| $\Delta^x\rho$, $\Delta^x U$ | words (limited slopes) | $\Delta$ is a difference here |
| $u$, $v$ (advection velocity) | components of $u_h$; words | |
| $A^x$, $A^y$ (flux Jacobians) | words | **collision:** $A_h$ vector potential; $A_k$ are swept areas in eq. 1.2 |
| $\lambda^{x,\nu}$ | $\lambda_k$ (per direction) | |
| $r^{x,\nu}$, $l^{x,\nu}$ | words | **collision:** $r$ refinement ratio, $l$ level index |
| $\alpha^\nu$ | words | **collision:** $\alpha^{\mathrm{LF}}$ |
| $P_S$ (characteristic projection) | words | **collision:** $P$ prolongation |
| $F^x$, $F^y$ | words (base-scheme numerical fluxes) | $f^{x,*}$ is registered for field components only |
| $U^T$, $\sigma$, $J$, $\xi$, $\eta$, $\mathbf n^\xi$, $\mathbf n^\eta$, $\chi$, $\delta$, $z_0$, $z_1$, $M$ | words | method-local |

# Pages created or updated

* Created [Corner transport upwind (CTU)](/methods/corner-transport-upwind.md): the method from its primary source and its MHD uses in the bundle.
* Updated [PPM](/methods/ppm.md): Colella's unsplit corner-coupled framework predates the unsplit PPM codes; the 6- and 12-solve counts.
* Updated [Constrained transport](/methods/constrained-transport.md) (CTU as the unsplit integrator of CT codes).
* Updated [CASTRO](/software/castro.md) (unsplit framework traced to Colella 1990).
* Updated Source pages of [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md) and [Miniati & Martin (2011)](/sources/miniati-martin-2011.md) (CTU attribution checked).

# Citations

1. `~/papers/mosaic/div-free-amr/1990-JCP-Colella-1010160021-99919090233-Q.pdf`.
   * **Version read.** The published journal article, an image scan (30
     pp.) with an Acrobat Capture OCR layer. Received June 20, 1984;
     revised October 21, 1987.
   * **Identity.** doi:10.1016/0021-9991(90)90233-Q, checked on Crossref:
     title and sole author match; J. Comput. Phys. 87(1):171–200, issued
     March 1990. Crossref's reference count is 26; the printed list has 25
     entries.
   * **How it was read.** The OCR layer is unusable for equations; every
     equation was read from page renders at 110–220 dpi. Eqs. 1.2–1.9,
     2.5–2.17, 3.3 and 4.9–4.12 were read cleanly; eqs. 3.4–3.11 and
     4.3–4.7 were read at 110 dpi and are summarized, not reproduced.
   * **Recorded as printed.**
     * The fourth-order slope on p. 191 is unnumbered in the scan; p. 192
       refers to it as "(4.8)". It prints
       $\mathrm{sgn}(q_{i+1,j} - q_{i+1,j})$, presumably for
       $q_{i-1,j}$ (reader's reading); not reproduced as an equation.
     * §5 Dirichlet state at $y = 1$: the minus sign of $v = -.50632$ is
       faint in the scan (uncertain); the DMR spacing reads $1/100$ with
       a faint middle digit, consistent with 400 zones over length 4.
     * Crossref counts 26 references against 25 printed; unexplained.
   * **Reference list.** 25 entries, all merged. JCP journal entries of
     the period carry no titles. Colella's MUSCL paper, printed "SIAM J.
     Sci. Stat. Comput. 6, 107 (1985)", was merged into `colella-1985`
     (6:104). Almgren et al. (1998) cite this paper under a different
     title ("A multidimensional second order Godunov scheme for
     conservation laws"); page 1 and Crossref give the title above. The
     bibliography holds 3779 entries after this batch.

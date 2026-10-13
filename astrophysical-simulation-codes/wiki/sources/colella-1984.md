---
type: Source
title: "Colella & Woodward (1984) — The Piecewise Parabolic Method (PPM) for Gas-Dynamical Simulations"
description: "Method paper of PPM: a MUSCL-type higher-order Godunov method with a monotonized parabolic reconstruction, contact steepening, characteristic domain-of-dependence averaging and one Riemann solve per interface, in advection, Lagrangian, Lagrange-plus-remap and direct-Eulerian forms, with flattening and a diffusive flux as the extra dissipation it shows such schemes need near shocks."
resource: "doi:10.1016/0021-9991(84)90143-8"
source_kind: paper
authors: [Colella P., Woodward P.R.]
year: 1984
venue: "J. Comput. Phys. 54:174–201"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/1984-JCP-Colella-1010160021-99918490143-8.pdf"
tags: [hydro, reconstruction, riemann-solver, time-integration]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The original specification of the
[piecewise parabolic method (PPM)](/methods/ppm.md), a higher-order
extension of Godunov's method of the MUSCL type. It is given in three
one-dimensional formulations: a scalar advection scheme on a non-uniform
mesh (§1); a Lagrangian gas-dynamics scheme in planar, cylindrical or
spherical geometry (§2), which with a remap gives a two-step
Lagrange-plus-remap Eulerian scheme; and a single-step ("direct")
Eulerian scheme (§3). Multidimensional runs use operator splitting
(Introduction). The abstract names three novelties: a parabolic
interpolation that represents discontinuities, contacts above all, more
steeply; a simpler and more robust computation of the nonlinear wave
interactions (averaging over each characteristic's domain of dependence,
then one Riemann solve per interface); and the finding that higher-order
Godunov methods of this type need dissipation beyond monotonicity
limiting near shocks, supplied by flattening, an explicit diffusive flux
or an oscillating grid (§4, Appendix). The authors call the algorithms
"the minimal ones": every simplification they tried degraded the results
(§5). The paper has no test section of its own; its comparisons are in
the companion paper, Woodward & Colella (1984), J. Comput. Phys. 54:115.

# Key claims

Equations below are in the [registry](/notation.md) notation
(paper index $j$ written $i$; see the Notation map).

1. **Advection scheme and accuracy** (§1, eqs. 1.1–1.3, Figs. 1–2). The
   zone averages are advanced by exact advection of a piecewise parabolic
   profile constrained to create no new extrema, stable for
   $\vert v_x\vert\Delta t \le \min_i(\text{zone width})$. The scheme is
   "third-order accurate in general; in the limit of very small time
   steps, for equally spaced zones, it is fourth-order accurate" (Fig. 2
   caption; p. 178).
2. **Parabola** (eqs. 1.4–1.5). On each zone, the parabola with edge
   values $u^+_{i-1/2}$ and $u^-_{i+1/2}$ and zone mean $u_i^n$; its
   curvature coefficient is $6\left(u_i^n - \tfrac12(u^+_{i-1/2} + u^-_{i+1/2})\right)$.
3. **Interface value** (eqs. 1.6–1.9). The value at $x_{i+1/2}$ is the
   derivative of the quartic through the cumulative integrals at the five
   interfaces $x_{i-3/2},\dots,x_{i+5/2}$, so it depends on zones $i-1$ to
   $i+2$ (eq. 1.6, non-uniform mesh). It uses an average zone slope
   (eq. 1.7), replaced in the paper's runs by a limited slope (eq. 1.8),
   zero unless $(u_{i+1}^n - u_i^n)(u_i^n - u_{i-1}^n) > 0$. This keeps
   the interface value between $u_i^n$ and $u_{i+1}^n$ and gives a value
   "third-order accurate for variable mesh spacing, even where the mesh
   spacing changes discontinuously". On a uniform mesh, unlimited:
   $$\tfrac{7}{12}\left(u_i^n + u_{i+1}^n\right) - \tfrac{1}{12}\left(u_{i+2}^n + u_{i-1}^n\right) \qquad \text{(eq. 1.9).}$$
4. **Monotonicity constraint** (eq. 1.10, pp. 178–179). Both edge values
   start at the interface value. If $u_i^n$ is a local extremum,
   $(u^-_{i+1/2} - u_i^n)(u_i^n - u^+_{i-1/2}) \le 0$, both are reset to
   $u_i^n$ (constant profile). If the parabola overshoots, the edge on
   the far side is reset so that the derivative vanishes at the opposite
   edge: $u^+_{i-1/2} \to 3u_i^n - 2u^-_{i+1/2}$ when
   $(u^-_{i+1/2} - u^+_{i-1/2})\left(u_i^n - \tfrac12(u^+_{i-1/2} + u^-_{i+1/2})\right) > (u^-_{i+1/2} - u^+_{i-1/2})^2/6$,
   and symmetrically for $u^-_{i+1/2}$. This step creates the
   discontinuities at zone edges (p. 177).
5. **Domain-of-dependence averages** (eqs. 1.11–1.13). The interface
   value used in the flux is the average of the upwind parabola over the
   distance $\vert v_x\vert\Delta t$ from the interface (closed forms in
   eq. 1.12). The same averages are the characteristic-tracing kernels of
   §§2–3.
6. **Discontinuity detection ("contact steepening")** (eqs. 1.14–1.17,
   Fig. 3). Inside a detected discontinuity the edge values are blended
   toward the edges of the limited linear profiles of the two neighbours.
   The blending weight rises with a normalized third derivative and is
   nonzero only where the second derivative changes sign, the first and
   third derivatives have opposite signs, and the jump is not small
   (relative threshold 0.01). Constants of Woodward & Colella: 20 and 0.05
   for the two coefficients of the weight (p. 181). It is applied just
   before the monotonicity step; if it fires in smooth flow "the scheme
   remains second-order accurate" (p. 180). In gas dynamics it acts on
   density only and only at contacts, flagged where $\gamma$ times a
   problem-dependent constant (0.1 in Woodward & Colella) times
   $\vert\rho_{i+1} - \rho_{i-1}\vert/\min(\rho_{i+1}, \rho_{i-1})$ is at
   least $\vert p_{i+1} - p_{i-1}\vert/\min(p_{i+1}, p_{i-1})$ (p. 181,
   eq. 3.2). It is not used in the pure Lagrangian scheme ("contact
   discontinuities automatically remain sharp", p. 183) and is used on
   density in the remap of the two-step scheme (p. 187).
7. **Lagrangian scheme** (§2, eqs. 2.1–2.10, Fig. 4). Mass coordinate,
   geometry index 0, 1, 2 (planar, cylindrical, spherical), $\gamma$-law
   gas. The interpolated variables are specific volume, velocity and
   **pressure** rather than total energy, because limiting the pressure
   profile behaves better near shocks (p. 183). Time accuracy is second
   order by design, after van Leer: third order in space and time would
   need "numerous solutions of the Riemann problem", and strong-shock test
   calculations lose "very little accuracy" (p. 181; no data shown).
   Interface states are parabola averages over the domain of dependence of
   the $\pm$ characteristics, at the Lagrangian sound speed
   $\rho c_s = (\gamma p\rho)^{1/2}$ (eqs. 2.5–2.6); body forces and
   curvilinear area terms correct them by terms of order $\Delta t\,\rho c_s\,g$
   (eq. 2.9) so that a smooth steady solution gives no false jump.
   Gravity enters the conservative update time-centred, as the average of
   its old- and new-time values (eq. 2.10).
8. **Riemann solver** (eq. 2.8, p. 185; §3, p. 191). The pressure and
   velocity at the interface solve two nonlinear equations, one per side,
   whose wave speeds are the Lagrangian shock speeds of each side
   (each depends on the unknown interface pressure through the
   shock-strength factor $1 + \frac{\gamma+1}{2\gamma}(\text{pressure ratio} - 1)$).
   They are solved by van Leer's Newton iteration "with a fixed number of
   iterations". In smooth flow eq. 2.8 is a finite-difference
   approximation of the characteristic equations. The Eulerian scheme
   uses the Cartesian solver with the same iteration and, inside a
   rarefaction fan, linear interpolation between the states on either side
   (p. 191). Fig. 8 uses 6 iterations: "If only 2 iterations are
   performed, very large errors are generated in the single zone just
   behind the shock."
9. **Two-step Eulerian scheme** (§2 end, pp. 186–187). A Lagrangian step
   followed by a remap with the §1 advection scheme on the moved,
   non-uniform mesh, an approach "first proposed by Noh". Interpolation is
   in the volume coordinate; density, not specific volume, is
   interpolated; the total energy for the remap is built from the edge
   values of $p$, $\rho$ and $v_x$.
10. **Single-step (direct) Eulerian scheme** (§3, eqs. 3.1–3.8, Fig. 5).
    Interpolated variables $\rho$, $v_x$, the transverse velocity and $p$,
    in the volume coordinate; steepening on $\rho$ only. A first guess
    averages the parabolae over the domain of dependence of the fastest
    characteristic toward the interface (eq. 3.3); used alone it would make
    advection first order (p. 188). It is then corrected wave family by
    wave family, with eigenvalues $v_x - c_s$, $v_x$, $v_x + c_s$: each
    family that moves toward the interface contributes the difference
    between its own domain-of-dependence average and the first guess,
    projected on the family, and families moving away contribute nothing;
    the transverse velocity moves with the contact (eqs. 3.4–3.7). The
    stated requirements: each family's crossing amount correct to second
    order, and the exact §1 advection flux in the absence of pressure and
    velocity gradients (p. 189). Source terms enter the tracing (eq. 3.7)
    and are time-centred in the final update (eq. 3.8).
11. **Separate pressure term** (eqs. 3.1, 3.8). The pressure gradient is
    differenced apart from the area-weighted flux divergence, for
    curvilinear geometry.
12. **Post-shock noise is a property of systems** (§4, Figs. 6, 8). Slow
    shocks leave low-amplitude oscillations behind them in both Eulerian
    forms unless dissipation is added; the errors sit in the entropy and in
    the Riemann invariant $v_x - 2c_s/(\gamma-1)$ carried by the
    characteristic that crosses the shock; the scalar case is well behaved
    (p. 192).
13. **Flattening** (eq. 4.1, Fig. 7, Appendix). Each edge value is blended
    toward $u_i^n$ with a coefficient between 0 and 1, where **1 is full
    flattening (locally Godunov's first-order method) and 0 none** (§4,
    p. 192). The shock indicator is
    $(p_{i+1} - p_{i-1})/\min(p_{i+1}, p_{i-1}) > 0.33$ together with
    $v_{x,i-1} - v_{x,i+1} > 0$ (eq. A.1); the steepness measure is
    $(p_{i+1} - p_{i-1})/(p_{i+2} - p_{i-2})$ (p. 192). The simplest scheme
    (eq. A.2) builds its zone term from $\max\left(0, 10\,(\text{steepness} - 0.75)\right)$
    where the shock indicator is set, takes the larger of the zone's and
    its upstream neighbour's values, and adds an artificial viscosity of
    coefficient 0.1 (A.3); as printed, A.2 subtracts the term from 1 (see
    Recorded as printed). The
    Lagrangian and multidimensional variants add a noise-wavelength term
    from a Lagrangian shock-speed estimate and a shock-strength term
    (eqs. A.4–A.11; constants on p. 200). The residual post-shock errors
    are "a fraction of a percent" in most cases and below 2 % in all
    tested (p. 198). In the two-step scheme flattening is applied in the
    Lagrangian step, not in the remap. "Experimentation with different
    values of the parameters is not recommended" (p. 201).
14. **Diffusive flux** (eqs. 4.2–4.5). An explicit term proportional to
    $u_i - u_{i+1}$ is added to $\hat f_{i+1/2}$ with coefficient
    $K\max(v_{x,i} - v_{x,i+1}, 0)$ in 1D, akin to Lapidus (eq. 4.4), and
    in multi-D a coefficient from an undivided-difference
    $-\nabla\cdot\mathbf v$, needed to detect shocks transverse to the
    sweep (eq. 4.5). Single-step Eulerian PPM used $K = 0.1$; MacCormack's
    method needed $K = 1$ (p. 196). Alternatively the grid oscillates by
    the same amount on alternate steps, which adds only the advection
    scheme's own dissipation (eq. 4.3) and requires two successive sweeps
    per direction.
15. **Multidimensional failure mode** (pp. 193–194). A strong shock with
    vanishing grid-relative characteristic speed (the Mach 3 wind-tunnel
    shock near the wall and the Mach stem of Woodward & Colella) leaves
    errors no flattening removes: Godunov dissipation at a shock vanishes
    as the shock speed goes to zero, and small tangential velocities in
    the shock column create large spurious sources in the 1D sweeps.
16. **Announced extensions** (§5). Multiple fluids, "easily added,
    particularly to the two-step Eulerian version"; a general equation of
    state through Colella & Glaz.

# Tests

The paper defers verification to Woodward & Colella (1984). The
evidence printed here:

1. **Very strong planar shock, Lagrangian PPM** (§4, Fig. 6, p. 193).
   $\gamma = 5/3$, pressure jump over six orders of magnitude, 30 zones
   displayed. Without flattening, post-shock oscillations of "about 1.3%
   amplitude", in the two Riemann invariants whose characteristics cross
   the shock. With flattening the oscillations are "dramatically reduced"
   and the shock is broadened "only slightly"; the required dissipation
   is obtained once the effective shock width is "barely more than one
   mesh length" (pp. 192–193).
2. **Nearly stationary, extremely strong shock, first-order single-step
   Godunov** (§4, Fig. 8, p. 195). Pressure jump over six orders,
   velocity jump unity, nearly 8000 steps to cross 160 zones. An error
   of 3 % immediately behind the shock, decaying downstream, so
   flattening cannot cure it. 6 Riemann iterations; 2 give "very large
   errors" in the zone behind the shock.
3. **Parameter calibration** (Appendix, pp. 200–201). "Fairly
   exhaustive" steady-shock runs over the parameter space for
   $\gamma = 1.4$: post-shock density oscillation $\tfrac34$ % of the
   density jump at worst, typically $\tfrac14$ %; effective shock width
   never above two mesh lengths, one for fast-moving shocks.
4. Qualitative references to Woodward & Colella: oscillations behind the
   incident shock near the floor and behind the Mach stem of the Mach 3
   wind tunnel with single-step MUSCL and Godunov (pp. 193–194).

# Notation map

| Paper | Canonical | Note |
|---|---|---|
| $a$, $a^n_j$ (scalar, zone average) | $u$, $u_i^n$ | index $j \to i$ |
| $\xi_{j+1/2}$, $r_{j+1/2}$ | $x_{i+1/2}$ | |
| $\Delta\xi_j$, $\Delta r_j$ | $h$ on a uniform mesh; zone width in words otherwise | the paper is written for non-uniform zones; the registry has no non-uniform width |
| $a_{R,j}$, $a_{L,j+1}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | edge values; $a_{L,j}$ is $u^+_{i-1/2}$ |
| $a_{j+1/2}$ | "interface value", in words | the unlimited value before the monotonicity step |
| $\Delta a_j$, $a_{6,j}$ | in words | parabola coefficients |
| $\delta a_j$, $\delta_m a_j$ | in words | average and limited slopes |
| $f^a_{j+1/2,L}$, $f^a_{j+1/2,R}$ | "domain-of-dependence average", in words | **collision**: $f$ is the registry flux |
| $\eta_j$, $\tilde\eta_j$, $\eta^{(1)}$, $\eta^{(2)}$ | steepening weight, in words | **collision** with the dual-energy $\eta_1$, $\eta_2$ |
| $\epsilon$ | thresholds, in words | two different ones: 0.01 (detection), 0.33 (eq. A.1) |
| $K_0$ | contact-detection constant, in words | |
| $f_j$, $\tilde f_j$ | flattening coefficient, in words | **collision** with the flux $f$; 1 = fully flattened |
| $w_j$, $s_j$, $\omega_j$, $\kappa_j$, $\sigma_j$ | in words | **collision**: $\kappa$ is the opacity |
| $\nu_{j+1/2}$, $K$ | diffusion coefficient, in words; $K$ kept in prose | **collision**: $\nu$ is the Courant number |
| $u$ (sweep velocity), $v$ (transverse) | $v_x$, transverse velocity | **collision**: $u$ is the registry state |
| $\tau$ (specific volume) | $1/\rho$ | **collision** with the Valencia $\tau$ |
| $c$ | $c_s$ | **collision**: $c$ is the speed of light |
| $C = (\gamma p\rho)^{1/2}$ | $\rho c_s$ | Lagrangian sound speed |
| $W_L$, $W_R$, $W_j$ | Lagrangian shock speeds, in words | **collision** with the Lorentz factor $W$ |
| $\alpha$ (geometry index) | in words | collision risk with $\alpha_{\mathrm L}$, $\alpha_{\mathrm c}$ |
| $A(r)$, $V(r)$ (area, volume coordinate) | in words | **collision**: $A(u)$ is the flux Jacobian |
| $\mathbf A(\mathbf V)$, $\lambda_\pm$, $\lambda_0$ | primitive-variable Jacobian in words; $\lambda^{(p)}$ | the registry $A(u)$ is the conservative Jacobian |
| $U$, $F(U)$, $H(U)$, $G$ | $u$, $f(u)$, pressure term in words, $s(u)$ | |
| $\beta^\#$ | wave amplitudes, in words | **collision** with the shift $\beta^i$ and $\beta_{\mathrm p}$ |
| $p$, $\rho$, $\gamma$, $g$ | $p$, $\rho$, $\gamma$, $\mathbf g$ | |
| $E$ | $E/\rho$ | the paper's $E$ is specific (per unit mass); see Recorded as printed |
| $m$, $\Delta m_j$ | mass coordinate, in words | |

# Pages created or updated

* Created [Piecewise parabolic method (PPM)](/methods/ppm.md): the
  method as printed, and its use in the codes of this bundle as their own
  sources state it.
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md):
  PPM's own Riemann solver (eq. 2.8, fixed Newton iterations, 2 against 6
  iterations).

# Citations

1. Colella P., Woodward P.R. (1984), J. Comput. Phys. 54:174–201,
   doi:10.1016/0021-9991(84)90143-8. Local file:
   `/home/stefano/papers/mosaic/astrophysical-simulation-codes/1984-JCP-Colella-1010160021-99918490143-8.pdf`.
   * **Version read.** The published journal version (Academic Press
     scan, 28 pages, pp. 174–201; received 3 August 1982, revised
     25 August 1983). Not a preprint.
   * **Identity.** Checked on Crossref: title, the two authors,
     J. Comput. Phys. vol. 54, issue 1, pp. 174–201, issued 1984-04.
   * **How it was read.** The PDF is an OCR'd image scan. Every equation
     was read from rendered page images (110 dpi), eqs. 1.8 and A.10 also
     at 300 dpi; the text layer was not trusted for symbols. Eq. 1.6 (the
     non-uniform interface formula) and eqs. 2.9, 3.6–3.7, A.3, A.5–A.11
     were read but are given here in structure only. The OCR layer reads
     the calibration fractions $\tfrac34$ % and $\tfrac14$ % (p. 200) as
     "4%" and ":%".
   * **Recorded as printed.** (a) Eq. 1.8: the limited slope is the
     minimum of $\vert\delta a_j\vert$, $2\vert a^n_j - a^n_{j-1}\vert$ and
     again $2\vert a^n_j - a^n_{j-1}\vert$, the second and third arguments
     identical (verified at 300 dpi); the text's guarantee that the
     interface value lies between the neighbouring averages implies
     $2\vert a^n_{j+1} - a^n_j\vert$ for the third, which is inferred, not
     printed. (b) Eq. A.2 as printed, $\tilde f_j = 1 - w_j\max(0, \dots)$,
     gives full flattening wherever the shock indicator is 0, against the
     §4 statement that the coefficient "should be equal to 0 away from
     strong shocks"; not resolved. (c) Eqs. A.2 and A.10 print $f_i$ on
     the left, and A.10 prints $\max(\tilde f_j, \tilde f_j + s_j)$ where
     $\tilde f_{j+s_j}$ (the upstream neighbour, as in A.2) is evidently
     meant. (d) §2 (p. 183) cites the detection algorithm as
     "(1.16)–(1.18)", elsewhere "(1.15)–(1.17)"; there is no eq. 1.18.
     (e) Fig. 8: the text puts the 3 % error in the density, the caption
     in the entropy. (f) §2 calls $E$ "total energy per unit volume" while
     using $e = E - u^2/2$, a per-mass relation. (g) Eq. 3.6 prints
     $\rho_{i+1/2,S}$, index $i$ for $j$.
   * **Reference list:** 12 entries, numbered 1–12; titles printed for
     three, no DOIs. Colella's "A direct Eulerian MUSCL scheme for gas
     dynamics", printed "in press" with no year, is `colella-1985-c`
     (SIAM J. Sci. Statist. Comput. 6:104, 1985; Crossref). Colella &
     Glaz, "Efficient solution algorithms for the Riemann problem for real
     gases", printed "in preparation", is `colella-1985`
     (J. Comput. Phys. 59:264; Crossref). Van Leer's private
     communication, no year, is `vanleer-1984` (year is the citing date).
     Woodward & Colella (1984) is printed with pages 115–173, which
     confirms that page 174, as other sources print it, is this paper's
     first page (`woodward-1984`). Van Leer (1977) 23:276 lands on
     `vanleer-1977-b`. Bibliography: 2200 entries.

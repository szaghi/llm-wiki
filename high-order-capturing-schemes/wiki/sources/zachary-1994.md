---
type: Source
title: "Zachary et al. (1994) — A higher-order Godunov method for multidimensional ideal magnetohydrodynamics"
description: "A Strang-split second-order Godunov scheme for ideal MHD in a nonconservative form that keeps the ∇·B terms out of the differentiated fluxes: primitive-variable characteristic tracing with a hybrid characteristic/MUSCL slope, a linearized Engquist–Osher flux summed over sonic points, HLLE and Rusanov fallbacks at strong rarefactions and transonic degeneracies, and an optional end-of-step projection that made no noticeable difference in 2D."
resource: "doi:10.1137/0915019"
source_kind: paper
authors: [Zachary A.L., Malagoli A., Colella P.]
year: 1994
venue: "SIAM J. Sci. Comput. 15:263–284"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1994-SISC-Zachary-1011370915019.pdf"
tags: [mhd, godunov, characteristic-tracing, riemann-solver, projection, operator-splitting]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper extends the one-dimensional higher-order Godunov MHD scheme of
Zachary and Colella (1992) to two and three dimensions by Strang
splitting. The equations are written in a nonconservative form in which
the terms proportional to $\nabla\cdot\mathbf B$ stay out of the
differentiated fluxes; each 1D sweep is then a quasi-conservative system
whose normal-field derivative terms are treated as sources. The predictor
traces characteristics in primitive variables with a hybrid slope that
limits each characteristic field against a fourth-order MUSCL slope,
with a steepness factor set by local linear degeneracy. The corrector is
a linearized Riemann solver with eigenvectors frozen at the arithmetic
mean of the primitive states, evaluating an Engquist–Osher flux as a sum
of physical fluxes at the sonic points of each wave. An HLLE flux replaces
it at strong rarefactions and Rusanov dissipation at transonic
degeneracies. $\nabla\cdot\mathbf B$ is controlled by the nonconservative
form plus an optional end-of-step projection, which made no noticeable
difference on the 2D tests.

# Key claims

1. **Nonconservative form** (§2.1, eqs. 1a–1g). Momentum and energy
   carry terms of the form (transverse field)$\cdot\nabla$(normal
   component) outside the divergence, so the form differs from
   conservation form by terms proportional to $\nabla\cdot\mathbf B$
   (Gaussian units). Motivation: to minimize how far the terms of the
   directional operators "would have to sum to zero due to the
   divergence-free constraint", by analogy with advective differencing in
   incompressible flow; Brackbill and Barnes are cited for the reduction
   of monopole forces by a nonconservative momentum form (p. 265).
2. **Split 1D system** (eqs. 2–4). Each sweep solves
   $\partial_t u + \partial_x f(u) + A(u)\partial_x(\cdot) = 0$ with the
   normal field constant in the sweep, so its derivative terms in the
   transverse-field and energy equations are "formally" sources (p. 266).
   The discretization, eq. 4, prints no operator between the two
   interface terms of the nonconservative part (see Citations).
3. **Strang splitting** (eqs. 5–6): $xyzzyx$ sweeps, second order in time
   if each 1D operator is.
4. **Hybrid slope** (§2.2, eqs. 7–12). Backward, forward and centred
   differences and the MUSCL "monotonized, fourth-order difference" are
   each expanded on the right eigenvectors. The limited coefficient is
   the smallest in magnitude among twice the one-sided, the centred and
   the MUSCL ones, with the sign of the centred one, if the one-sided
   ones agree in sign, else zero (eq. 10). The factor 2 drops to 1 where
   the field is locally linearly degenerate, detected by a sign change of
   its structure coefficient $\nabla\lambda^{(p)}\cdot r^{(p)}$ between
   neighbours (eq. 11). The MUSCL term "enforce[s] monotonicity in each
   variable". Pure MUSCL primitive slopes gave "moderate amplitude
   (5–10%) fluctuations at shocks, compound waves, and certain types of
   rarefaction waves", which Colella's flattening "does not fix" (p. 267).
5. **Primitive-variable sources** (eqs. 13–15). In primitive variables the
   normal-field derivative terms change "only the $\mathbf B_\perp$-equations,
   and not the pressure equation" (p. 269); the traced states are
   corrected by them.
6. **Eigenvectors** are those of Zachary and Colella (1992), in primitive
   variables, not reprinted. "We always have a set of complete, linearly
   independent eigenvectors" (p. 273). No normalization is stated.
7. **Riemann solver** (§2.3.1, eqs. 18–19). The jump in primitive
   variables is expanded on eigenvectors at the arithmetic mean of the two
   states; intermediate states bound the entropy wave, whose mean speed
   picks the upwind side. Wave speeds are interpolated linearly, replacing
   the cubic Hermite interpolation of 1992 because the structure
   coefficients become very large at strong gradients; "Changing to a
   linear, rather than a cubic, interpolation does not alter any of our
   results" (p. 270).
8. **Engquist–Osher flux for systems** (eqs. 20–28). Bell, Colella and
   Trangenstein's form is unsuitable because some terms must be
   differenced as gradients. The flux is $f(\text{left state})$ plus an
   alternating sum of physical fluxes at the sonic points of each linearly
   interpolated wave speed (eqs. 25–27); any split of the flux into two
   parts has its own such flux, so one part can be differenced as a
   divergence and the other as a gradient (eq. 28). Presented without
   derivation in the 1992 paper, derived here.
9. **Strong rarefactions** (§2.3.2, eqs. 29–30). Where the fast speed at
   the mean state is below the jump of the entropy speed across the
   problem, the flux is replaced by the HLLE flux with
   $S_R = \max(\lambda_R^+, \lambda_e^+, 0)$ and
   $S_L = \min(\lambda_L^-, \lambda_e^-, 0)$, called "positively
   conservative", after Einfeldt et al., who showed that "any linear
   Riemann solver must fail" for some strong rarefactions. Where an
   intermediate density falls below its outer state, that side is
   interpolated in specific volume.
10. **Degeneracies** (§2.3.3, eqs. 31–33). At $B_x = 0$ (fivefold
    degeneracy with the entropy speed) and at $B_\perp = 0$, fast and slow
    waves lose genuine nonlinearity and the Engquist–Osher flux "may fail
    and the entropy condition may not be satisfied" (p. 273). Detection
    by Bell, Colella and Trangenstein's structure-coefficient test with
    constant 0.1 (eq. 31), plus an empirical Alfvén/slow test because
    that one fails as $B_x/B_\perp \to 0$ (eq. 32). At a transonic
    degeneracy the flux correction of the two waves is replaced by
    Rusanov dissipation (eq. 33). Whether this yields the correct weak
    solutions is "far from settled" (p. 269).
11. **$\nabla\cdot\mathbf B$** (§2.4, eq. 34). The centred, unstaggered
    scheme keeps $\nabla\cdot\mathbf B = 0$ "only to the truncation error
    of the method", which "could be O(1)" at discontinuities. A
    Brackbill–Barnes projection may be applied at the end of each step,
    with second-order central gradient and divergence, giving
    "nonstandard discretizations of the Laplacian" solved by multigrid.
    "For the two-dimensional problems presented in this paper, we did not
    find any noticeable difference regardless of whether or not we
    applied a projection" (p. 275). The conclusions say the
    nonconservative form "appears to suppress the occurrence of monopole
    forces" (p. 283). Vector-potential or flux-function formulations are
    set aside because they need a staggered mesh unsuited to
    characteristic analysis (p. 274).
12. **Order, cost, time step** (§§3–4, eq. 35). "explicit, second-order
    Godunov method" (p. 283); 15 μs per cell in 1D and twice that in 2D,
    about 32,000 mesh points per second in 2D on a Cray Y-MP; all runs at
    Courant number 0.8 with no artificial viscosity. A fully unsplit
    version after Colella (1990) is announced as future work (pp. 264,
    283).

# Tests

All visual comparisons; no error norms or convergence orders.

1. **Sod shock tube** (§3.1, Figs. 1–2). $\gamma = 1.4$, 100 points, 50
   steps. Shock "well resolved within three grid points"; contact more
   diffused (no contact detection); "a small undershoot at the base of
   the rarefaction wave", attributed to the linearized solver. Against
   PPM with and without contact detection: very similar apart from the
   undershoot; PPM with detection has the sharper contact
   ([Sod shock tube](/benchmarks/sod-shock-tube.md)).
2. **Brio–Wu** (Fig. 3). $\gamma = 2$, $B_x = 0.75\sqrt{4\pi}$,
   $B_y = \pm\sqrt{4\pi}$ (Gaussian), 800 points, 400 steps: "excellent
   agreement", a small perturbation at rarefactions, shocks "extremely
   sharp" without post-shock oscillations
   ([Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md)).
3. **Strong variant** (Fig. 4). $B_x = 0$, left pressure 1000,
   $\gamma = 5/3$, 200 points, 100 steps; "we could solve this problem
   with a $\gamma \ne 2$, while the Brio and Wu solver could not"
   (p. 276).
4. **Einfeldt's 1–2–0–3 rarefaction** (Fig. 5). $\gamma = 1.4$,
   $\rho = 1$, $v_x = \mp2$, $p = 0.4$, 100 points, $t = 0.1$; handled by
   the strong-rarefaction switch ([double rarefaction](/benchmarks/double-rarefaction.md)).
5. **Magnetized explosion** (§3.2.1, Figs. 6–8). Radius 0.1, $\rho = 1$,
   pressure 100 inside and 1 outside, uniform $B_y = 0$, 10 or 100,
   $120^2$, 48 steps, no flattening or viscosity; "identical to" Kössl,
   Müller and Hillebrandt (1990). From isotropic ($B_y = 0$) to highly
   anisotropic ($B_y = 100$). Step-like contour irregularities near strong
   discontinuities are called a known feature of higher-order Godunov
   methods, curable by flattening and quadratic viscosity (p. 281).
   Domain size and end time are not stated.
6. **Compressible Orszag–Tang vortex** (§3.2.2, Fig. 9). Periodic,
   $192^2$, $\mathbf v = (-\sin y, \sin x)$, $\mathbf B = (-\sin y, \sin 2x)$
   as in Picone and Dahlburg, Mach number 1 and plasma beta 10/3; $\gamma$,
   the base density and pressure and the domain are not stated. One time
   is shown, "after 300 timesteps (approximately 2 Alfvén transit
   times)", with a pressure cut at grid row 60. The decay "appears to
   closely match" Dahlburg and Picone
   ([Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)).

# Notation map

| Zachary et al. (1994) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $F$ | $u$, $f(u)$ | |
| $\mathbf W$ | $\mathbf W$ extended by $\mathbf B$ | primitive state |
| $\mathbf u$, $u_x$ | $\mathbf v$, $v_x$ | |
| $E$ | $E/\rho$ | the paper's $\rho E$ is the registry $E$; Gaussian units |
| $\lambda_k$, $\mathbf r_k$, $\bar{\mathbf R}_k$ | $\lambda^{(p)}$, $r^{(p)}$ | $\bar{\mathbf R}_k$ frozen at the mean state |
| $\alpha_k$, $\bar\alpha_k$ | words (characteristic amplitudes) | **collision**: Lax–Friedrichs $\alpha$, normalizations $\alpha_f$, $\alpha_s$ |
| $\kappa_{lm}$ | $\nabla\lambda^{(l)}\cdot r^{(m)}$ (words) | **collision**: Suresh–Huynh $\kappa$, cut-cell $\kappa_i$ |
| $\gamma$ (slope factor, eq. 10) | words | **collision**: ratio of specific heats |
| $\mathbf W_e$ | words (arithmetic mean state) | |
| $F^{EO}$, $F^G$ | words (Engquist–Osher flux); HLL-type $\hat f$ | |
| $b^+$, $b^-$ | $S_R$, $S_L$ | |
| $\nu$ (eq. 33) | $S$ | **collision**: registry $\nu$ is the CFL number |
| $\sigma$ (eq. 35) | $\nu$ | **collision**: Hu–Adams–Shu $\sigma$ |
| $v_f$, $v_{ax}$, $c_s$ | $c_f$, $c_A$, $c$ | **collision**: the paper's $c_s$ is the sound speed, the registry's the slow speed |
| $c$ (= 0.1, eq. 31) | words | **collision**: sound speed $c$ |
| $\phi$ (eq. 34) | $\Phi$ | the registry's sign convention is the self-consistent one (see Citations) |
| $\mathcal L_x$ | words (split operator) | **collision**: spatial operator $\mathcal L$ |

# Pages created or updated

* Updated [Constrained transport for high-order capturing schemes (MHD)](/methods/constrained-transport.md)
  (batch-17 block: the 1994 projection, printed sign, no noticeable
  difference in 2D).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md)
  (batch-17 block: hybrid characteristic/MUSCL slope, degeneracy-set
  steepness, the 1992 eigenvectors not reprinted).
* Updated [Piecewise parabolic method (PPM)](/methods/ppm.md) (batch-17
  block: the Sod comparison, flattening insufficient for MHD).
* Cited on [Corner transport upwind (CTU)](/methods/corner-transport-upwind.md).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/1994-SISC-Zachary-1011370915019.pdf`.
   * **Version read.** The publisher's version of record (SIAM download
     stamped 11/27/14), 22 pages. Received 22 June 1992; accepted
     (revised) 24 June 1993.
   * **Identity.** doi:10.1137/0915019, checked on Crossref: title and
     authors as on page 1, SIAM J. Sci. Comput. 15(2):263–284, March 1994.
   * **How it was read.** Text layer for prose; all equations from page
     renders at 110 and 250 dpi. Eq. 27 checked at 250 dpi.
   * **Recorded as printed** (reader's reading).
     - Eq. 4 prints no operator between the two interface terms of the
       nonconservative part (checked at 250 dpi); a minus is presumably
       meant. Not reproduced as a formula.
     - Eq. 12 prints the factor $\Delta x/\Delta t$ where $\Delta t/\Delta x$
       is dimensionally required.
     - Eq. 34 prints $\nabla^2\phi + \nabla\mathbf B = 0$ (no dot) and then
       $\mathbf B = \mathbf B - \nabla\phi$; as printed these are
       sign-inconsistent, since the divergence of the result is twice the
       original divergence (compiler's algebra). The registry's
       $\nabla^2\Phi + \nabla\cdot\mathbf B = 0$,
       $\mathbf B \leftarrow \mathbf B + \nabla\Phi$ is self-consistent.
     - Eq. 35 prints the time step as a maximum over cells; a minimum is
       presumably meant.
     - The Orszag–Tang definitions of the Mach number and plasma beta
       are garbled (a missing square and a missing division).
     - The right density of the Einfeldt test prints as "$l$", read as 1.
   * **Reference list:** 25 entries, all merged. Roe, printed J. Comput.
     Phys. 53:357, lands on `roe-1981`; Liu, printed J. Differential
     Equations 18 (1981), on `liu-1975` (Crossref 18:218, 1975). Same-year
     Bell entries are `bell-1989` and `bell-1989-b`. Printed spellings
     ("Tragenstein", "H. Hillebrandt") are kept in the fragment.
     Bibliography: 3270 entries.

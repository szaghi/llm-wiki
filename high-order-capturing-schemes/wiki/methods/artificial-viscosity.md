---
type: Method
title: "Artificial viscosity (shock-capturing diffusion)"
description: "Capturing shocks by adding a dissipative term that acts only where the solution is steep: the von Neumann–Richtmyer idea and its switched, sensor-based descendants, from Lapidus's viscosity and characteristic switches in finite volumes to the pressure-sensor, field-aligned viscosity that stabilizes high-order continuous Galerkin elements; vanishing under mesh refinement, at the price of hand-tuned coefficients."
status: established
aliases: [shock-capturing viscosity, shock-capturing stabilization, discontinuity capturing, artificial dissipation, sensor-based viscosity]
tags: [artificial-viscosity, dissipation, finite-element, stabilization, strong-shocks, mhd]
timestamp: 2026-10-16T00:00:00Z
---

# Artificial viscosity (shock-capturing diffusion)

**Idea.** Add to the equations, or to the weak form, a dissipative term
whose coefficient is large only in steep regions. The discontinuity is
then spread over a few cells and the high-wavenumber oscillations of a
non-dissipative or high-order scheme near it are damped, while smooth
regions are left almost untouched. Von Neumann and Richtmyer (1950)
formulated the effect of unresolved scales on compressible flow as such a
viscosity, and Wilkins extended it to 2D; Godunov's method replaced it by
an explicit evaluation of the subscale effects through Riemann problems
([Bhole et al. (2023)](/sources/bhole-2023.md), §1;
[Godunov's method](/methods/godunov-method.md)).

## Forms in this bundle

* **Explicit finite differences and finite volumes.**
  * Lapidus's viscosity is a conservative fractional step consistent with
    a nonlinear diffusion of the form $h^2(\vert u_x\vert u_x)_x$. It is
    applied only near discontinuities and never to the mass equation, to
    limit mass diffusion across the contact. Artificial viscosity does not
    spread a contact; truncation error does. With fourth- and sixth-order
    methods "the appropriate high-order artificial viscosity" made the
    explicit time step "prohibitively small"
    ([Sod (1978)](/sources/sod-1978.md), §1 and eq. 20).
  * In Woodward & Colella's comparison, artificial-viscosity schemes
    (MacCormack with Lapidus viscosity; BBC, a von Neumann–Richtmyer
    Lagrangian step with remap) smear shocks over three or more zones, and
    they rank below PPM and MUSCL in accuracy
    ([Woodward & Colella (1984)](/sources/woodward-1984.md), §§II–III).
  * A second-difference viscosity minus a fourth-difference
    hyperviscosity, switched per characteristic field by a limiter
    function of one-sided differences, can be added to a second-order TVD
    MHD scheme without breaking the TVD property
    ([Balsara (1998)](/sources/balsara-1998-b.md), §4).
  * The fourth-order finite-volume scheme adds an artificial viscosity
    that is $O(h^4)$ in smooth flow and reduces to PPM's at strong
    compressions ([fourth-order finite volume](/methods/fourth-order-finite-volume.md)).
* **DG.** Artificial viscosity is one of the three families of a priori
  DG limiters, with slope or moment limiters and (H)WENO limiters
  ([WENO limiters for DG](/methods/weno-limited-dg.md);
  [Dumbser et al. (2014)](/sources/dumbser-2014.md), §3.1).
* **High-order continuous Galerkin** (below). Here the viscosity is the
  "BV" half of the stabilization, and
  [VMS stabilization](/methods/variational-multiscale-stabilization.md)
  is the "$L^2$" half for smooth solutions.

## Sensor-based viscosity for $C^1$ finite elements

[Bhole et al. (2023)](/sources/bhole-2023.md) (§3.2) add to the weak form of
a full-MHD system, discretized with bi-cubic Hermite–Bézier elements, the
term

$$\nabla w_h : \left(\mathbb D_{\mathrm{sc}}\,\nabla u_h\right), \qquad \mathbb D_{\mathrm{sc}} = \mu_{\mathrm{sc}}\left[C_\parallel\,\hat{\mathbf b}\otimes\hat{\mathbf b} + C_\perp\left(\mathbb I - \hat{\mathbf b}\otimes\hat{\mathbf b}\right)\right],$$

that is,
$\mu_{\mathrm{sc}}C_\perp\,\nabla w_h:\nabla u_h + \mu_{\mathrm{sc}}(C_\parallel - C_\perp)\,(\hat{\mathbf b}\cdot\nabla w_h)\cdot(\hat{\mathbf b}\cdot\nabla u_h)$.
The anisotropy follows the strong field-aligned anisotropy of magnetized
plasmas; $C_\parallel = C_\perp$ recovers the isotropic form. The scalar
coefficient is

$$\mu_{\mathrm{sc}} = h_{\mathrm e}^2\,\frac{\dot p_{\mathrm{op}} + \dot p_{\mathrm{src}}}{p}\,\chi_{\mathrm p}, \qquad \chi_{\mathrm p} = h_{\mathrm e}\,\frac{\vert\nabla p\vert}{p} \qquad \text{(eq. 32)} .$$

* $\chi_{\mathrm p}$ is the dimensionless shock detector.
* $\dot p_{\mathrm{op}}$ and $\dot p_{\mathrm{src}}$ (eq. 33) are the
  magnitudes of the pressure rates produced by the differential operator
  and by the sources, through the chain rule on density, impurity density
  and temperature. Their ratio to $p$ is an inverse time, the "shock
  strength" that modulates the sensor. With the mass sources of pellet
  ablation, $\dot p_{\mathrm{src}}$ makes strong local sources raise the
  viscosity: in the source, such sources are what create the shocks
  (§1).
* So $\mu_{\mathrm{sc}}$ has the dimension of a diffusivity, $h_{\mathrm e}^2$
  times an inverse time times the sensor, and it scales as
  $h_{\mathrm e}^3$ at fixed gradients: it goes to zero under refinement
  (compiler's reading of eq. 32; the paper states the vanishing).
* It acts on the momentum, density, energy and impurity equations only,
  not on the induction equation (eq. 38).
* The form follows Bassi et al.'s viscosity for DG (2011) and its use for
  $C^1$ Powell–Sabin elements on the 2D Euler equations (Giorgiani et al.
  2018).
* A stronger modulation, chosen "based on experience" after eq. 32 failed
  at a tenfold lower resistivity, replaces
  $(\dot p_{\mathrm{op}} + \dot p_{\mathrm{src}})/p$ by an operator-only rate
  (eq. 49, §4.3.2).

**Evidence.** All of it comes from implicit (BDF2, one Newton step,
GMRES) simulations of shattered-pellet injection into a JET-like plasma
(§4). No convergence study and no standard shock test is shown.
* Without the viscosity, the linear solver fails once discontinuities
  form: at about 0.59 ms in reduced MHD and about 1.4 ms in full MHD with
  axisymmetric sources. With it, the runs continue, and a pressure jump
  near the impurity source is smeared locally, more for larger
  $C_{\mathrm{sc}}$ (Figs. 4–7).
* In 3D full MHD, $C_{\mathrm{sc}} = 10$ allows larger steps: 1182 steps
  against 8096 to reach about 1.5 ms. Each GMRES solve costs more (15.2 s
  against 6.0 s; the system is worse conditioned), but the total falls
  from 13.6 h to 5 h on 64 MPI processes (Table 1).
* The integrated thermal energy and plasma current agree with the
  unstabilized run as far as that run goes (to about 1.75 ms). The
  thermal quench itself happens later, so it has no unstabilized
  reference (Fig. 14).
* The viscosity map is large only near pressure jumps: near the
  boundaries, where the initial pressure profile has a jump, and at moving
  shocks near the impurity clouds (Fig. 13).

**Over-stabilization is visible.** $C_{\mathrm{sc}} = 50$ "has altered the
dynamics". The stronger modulation of eq. 49 with $C_{\mathrm{sc}} = 10$
at low resistivity gives a "very diffusive" scheme with no thermal
quench and no current spike (§4.3; Figs. 11, 15–19). The coefficients
depend on the transport parameters and on the grid, and are hand-tuned
(§5).

**The time-step argument differs from the explicit one.** Sod found that
a high-order artificial viscosity makes an *explicit* step prohibitively
small. In Bhole et al.'s *implicit* scheme the viscosity *raises* the
usable step, because it removes the unresolved high wavenumbers that make
Newton–GMRES fail. These claims concern different time integrators, so
they do not contradict each other.

# Citations

* [Bhole et al. (2023)](/sources/bhole-2023.md), §§1, 3.2, 4, eqs. 31–33,
  38, 49, Table 1, Figs. 4–19.
* [Sod (1978)](/sources/sod-1978.md), §1, eq. 20.
* [Woodward & Colella (1984)](/sources/woodward-1984.md), §§II–III.
* [Balsara (1998)](/sources/balsara-1998-b.md), §4.
* [Dumbser et al. (2014)](/sources/dumbser-2014.md), §3.1.

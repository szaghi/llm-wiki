---
type: Method
title: "Variational multiscale (VMS) stabilization of continuous Galerkin methods"
description: "Upwinding for continuous Galerkin finite elements on advection-dominated systems: model the unresolved scales as u' ≈ −τ R(u_h) and add their effect on the resolved scales to the weak form; with a diagonal time-scale matrix h_e/λ_max and the residual truncated to its advective part it reduces to a streamline-diffusion (SUPG-type) term per variable, local to each element, and it vanishes as h_e → 0."
status: established
aliases: [VMS, variational multiscale method, residual-based stabilization, SUPG-type stabilization, streamline diffusion]
tags: [finite-element, stabilization, dissipation, mhd, implicit]
timestamp: 2026-10-16T00:00:00Z
---

# Variational multiscale (VMS) stabilization of continuous Galerkin methods

**The problem.** A continuous Galerkin finite-element method takes trial
and test functions from the same space. Its approximation of the
differential operators is then centred, and for advection-dominated
flows it suffers dispersion errors that can give "entirely wrong
numerical solutions"; the method has no built-in mechanism to damp the
spurious waves these errors create
([Bhole et al. (2023)](/sources/bhole-2023.md), abstract and §3). This is the
finite-element form of the problem that upwind fluxes solve in finite
volumes ([Godunov's method](/methods/godunov-method.md)), and Bhole et al.
call the VMS term "similar to an up-winding mechanism that stabilizes
finite volumes schemes" (§3.1). They list Taylor–Galerkin methods, bubble
functions, SUPG and VMS as the established families of stabilized
Galerkin methods (§1); only VMS is developed in the source.

## Formulation

Weak form. Find $u_h \in \mathcal V_h$ such that
$\int_\Omega w_h\cdot\mathscr R(u_h)\,d\Omega = 0$ for every test function
$w_h \in \mathcal V_h$ (second-order terms integrated by parts).

Scale split. Write $\mathcal V = \mathcal V_h \oplus \mathcal V'$ and
$u = u_h + u'$, and split test functions alike. The weak form becomes
one problem tested on $\mathcal V_h$ and one on $\mathcal V'$
(Bhole et al., eqs. 20–22). Linearize the residual about the resolved
part,

$$\mathscr R(u_h + u') \approx \mathscr R(u_h) + \mathscr J\,u', \qquad \mathscr J = \frac{\partial\mathscr R}{\partial u}(u_h),$$

and model the fine scales by $u' \approx -\tau_{\mathrm{VMS}}\,\mathscr R(u_h)$
with $\tau_{\mathrm{VMS}} \approx \mathscr J^{-1}$ (eq. 23). Substituting
and moving $\mathscr J$ onto the test function gives the stabilized weak
form (eq. 24):

$$\int_\Omega w_h\cdot\mathscr R(u_h)\,d\Omega \;-\; \int_\Omega \left(\mathscr J^{*}w_h\right)\cdot\left(\tau_{\mathrm{VMS}}\,\mathscr R(u_h)\right)d\Omega = 0 \qquad \forall\, w_h \in \mathcal V_h .$$

The first integral is the Galerkin method; the second is the effect of
the unresolved scales on the resolved ones. Because the term is
proportional to the residual of the strong form, it vanishes on an exact
solution, so the stabilization is consistent.

**The time-scale matrix is the design choice.** For linear operators
$\mathscr J^{-1}$ can be expressed exactly; for nonlinear systems an
optimal $\tau_{\mathrm{VMS}}$ is "still an open question", and practical
choices rest on heuristics and physical properties of the model (§3.1).
If $\mathscr J$ is symmetric and $\mathscr R(u_h)$ is replaced by
$\mathscr J u_h$, the term is a sum of dissipative contributions, one per
block of $\mathscr J$ (eq. 26; stated, the derivation is one line).

## Bhole et al.'s choices for full MHD

* **Diagonal time scale** (eq. 25):
  $$\tau_{\mathrm{VMS}} = \frac{h_{\mathrm e}}{\lambda_{\max,\mathrm e}}\,\mathrm{diag}\left(C^{\mathrm{VMS}}_1, \dots, C^{\mathrm{VMS}}_m\right), \qquad C^{\mathrm{VMS}}_\ell \ge 0 .$$
  $h_{\mathrm e}$ is the shorter of the two segments joining midpoints of
  opposite edges of the element, taken as straight-edged;
  $\lambda_{\max,\mathrm e}$ is the largest fast-magnetosonic speed over the
  element. Since $\lambda_{\max,\mathrm e}$ does not depend on the mesh,
  $\tau_{\mathrm{VMS}} \to 0$ as $h_{\mathrm e} \to 0$, and the source states
  that the order of accuracy of the underlying Galerkin method is kept
  (§1; no convergence study is shown).
* **Truncated residual** (eq. 27). Following common practice, both
  $\mathscr J^{*}w_h$ and $\mathscr R(u_h)$ are replaced by the first-order
  part $\mathscr A$: no time derivative, no second-order (diffusive) terms
  and no sources. The added term is $(\mathscr A^{*}w_h)\cdot(\tau_{\mathrm{VMS}}\mathscr A u_h)$,
  a least-squares product of the advective operator with itself, not a
  full-residual VMS. In primitive variables
  $(\mathbf A, \mathbf v, \rho, T, \rho_{\mathrm f})$ (vector potential,
  velocity, density, temperature, impurity density) $\mathscr A$ is the
  acoustic block of the Euler equations plus passive advection of
  $\mathbf A$ and $\rho_{\mathrm f}$ (eq. 28). It carries no Lorentz-force
  or induction coupling between the $\mathbf A$ and $\mathbf v$ blocks, so it
  is not the first-order part of the full-MHD Jacobian (compiler's reading
  of eq. 28).
* **Diagonal option, used in every test** (eqs. 29–30).
  $\mathscr A_{\mathrm d}$ advects each variable by $\mathbf v\cdot\nabla$
  (the $\mathbf A$ block by $-\mathbf v\times\nabla\times$). The term then
  becomes a streamline diffusion per variable,
  $\tau_\ell\,(\mathbf v\cdot\nabla w_{h,\ell})(\mathbf v\cdot\nabla u_{h,\ell})$,
  the SUPG form, with the time scale set by the fast speed rather than by
  $\vert\mathbf v\vert$ (compiler's reading).
* **Element-local.** The fine scales are assumed to vanish on element
  boundaries, so the term is assembled element by element. It adds local
  contributions only, and "no additional communications associated with
  the parallel programming are involved" (p. 16).
* **Time integration.** The stabilized weak form is advanced implicitly
  with the same $\theta_{\mathrm{BDF}}$ weighting as the other terms
  (eq. 40), one Newton iteration per step and preconditioned GMRES.

## Limits

* VMS controls dispersion for smooth solutions but "does not provide a
  mechanism for BV stability": near shocks high-order Galerkin solutions
  still develop Gibbs oscillations. Bhole et al. pair it with a
  sensor-based [artificial viscosity](/methods/artificial-viscosity.md) for
  that, the same split as an $L^2$ stabilization plus a BV stabilization
  (§§1, 3.3).
* In the source, the effect of VMS alone is never isolated: every
  stabilized run combines VMS ($C^{\mathrm{VMS}}_\ell = 10^{-2}$) with the
  artificial viscosity, and the unstabilized run has neither (§4.3.1).
  Attributing the reported gains to VMS has no support there.

# Citations

* [Bhole et al. (2023)](/sources/bhole-2023.md), §§1, 3.1, 3.3, eqs. 19–30,
  37, 39–40.

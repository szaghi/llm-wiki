---
type: Software
title: "SCELT"
description: "Symbolic computation aided eigenvalue and linear code for tokamaks: a C++/MATLAB linear eigenvalue code for compressible resistive MHD in axisymmetric flux coordinates whose equations are derived and discretized automatically (poloidal Fourier, radial cubic finite elements), verified on the resistive internal kink (η^0.3766), ideal-kink β_p threshold and 2/1 tearing (η^0.5590) scalings."
status: established
aliases: [symbolic computation aided eigenvalue and linear code for tokamaks]
tags: [full-mhd, tokamak, spectral, finite-elements, tearing, kink, verification]
timestamp: 2026-10-16T18:35:00Z
---

# SCELT

SCELT is a linear eigenvalue code for single-fluid, compressible, resistive
("full", non-reduced) MHD in axisymmetric toroidal geometry, from the
Institute of Plasma Physics, Chinese Academy of Sciences, released under
GPL-3.0 in C++ and MATLAB with the EIGEN library
([Ma & Guo (2022)](/sources/ma-2022.md), page 1, §1). What distinguishes it is
the construction method, not the physics model: the equations are derived and
discretized by symbolic computation. The authors claim it as the first
physics code in the fusion community built directly with symbolic
computation (§1, §5). See
[symbolic code generation](/methods/symbolic-code-generation.md) and
[linear MHD eigenvalue codes](/methods/linear-mhd-eigenvalue-codes.md).

## Physics model

Normalized compressible resistive MHD with $\mu_0=1$: continuity, momentum
with a Laplacian viscosity, pressure with Ohmic heating and $\Gamma=5/3$,
Faraday's law, resistive Ohm's law, $\mathbf J=\nabla\times\mathbf B$ and
$\nabla\cdot\mathbf B=0$ (Ma & Guo 2022, §2, Eqs. 1–7). Linearizing about a
static axisymmetric equilibrium with time dependence $e^{i\omega t}$ gives the
generalized eigenproblem
$$\omega\,\mathcal A\,\hat{\mathbf u}=\mathcal B\,\hat{\mathbf u},\qquad \hat{\mathbf u}=(v_s,v_\phi,v_\theta,\delta p,B_s,B_\theta)^{\mathrm T},$$
where $s=\sqrt{\psi_N}$ is the radial flux label of the flux coordinates
$(s,\phi,\theta)$ and the toroidal field component is eliminated with
$\nabla\cdot\mathbf B=0$ (Eq. 8; §4 defines the label through the normalized
poloidal flux). The paper's matrices are written here $\mathcal A$, $\mathcal B$ to
avoid a clash with $\mathbf B$.

## Symbolic module

A linked-list polynomial algebra (symbolic variables, monomials, polynomials,
polynomial vectors) carries covariant and contravariant grad, div, curl, dot
and cross operators built directly in magnetic flux coordinates (radial label,
toroidal angle, poloidal angle). It linearizes the nonlinear equations
automatically, a flag marking first-order quantities, and expands them into
scalar form; the non-orthogonal metric produces up to about 500 terms per
equation (Ma & Guo 2022, §3.1.1–3.1.2). Every generated term has the form
"coefficient $\times$ mixed partial derivative of an unknown", with at most
second-order radial–poloidal derivatives for this model (§3.1.3, Eq. 9).

## Discretization and solver

* Each term is discretized automatically: Fourier harmonics in the poloidal
  angle, cubic finite elements in the radial label with Galerkin projection
  (the text says cubic B-spline, App. A says cubic Hermite), $\partial_\phi\to-in$
  toroidally, and equilibrium coefficients expanded in poloidal harmonics,
  which yields convolutions (§3.1.3, App. A). Local radial refinement is
  supported (§3.1.3).
* Boundary conditions: a perfectly conducting wall at the edge; at the axis,
  regularity conditions relating the radial and poloidal components of each
  poloidal harmonic of $\mathbf v$ and $\mathbf B$, which the authors say can
  matter for numerical stability (§3.1.4, App. B, Eq. B.6).
* The dense eigenproblem is solved by MATLAB `eig` for all eigenpairs;
  spurious modes are removed by an eigenvalue window, an oscillation
  parameter on the radial coefficients (threshold about 15) and manual
  inspection (§3.1.5, Eq. 10).
* Equilibria come from SCELT's own inverse Grad–Shafranov solver given $q$ and
  $p$ (§3.2, Eqs. 13–14; see the
  [Grad–Shafranov equation](/definitions/grad-shafranov-equation.md)).
* No parallelism, run times or resolution counts are reported (§4).

## Verification

From Ma & Guo (2022):
* **Module tests.** A Poisson problem on a shaped domain with a manufactured
  solution converges at order 3.98, the inverse Grad–Shafranov equation on the
  Solov'ev equilibrium at order 3.81 (§3.2, Figs. 4–5).
* **[Resistive internal kink](/definitions/resistive-internal-kink.md)**
  ($m=n=1$, circular, $R_0=5$, $a=1$, $p_0=5\times10^{-5}$ normalized):
  $\gamma\propto\eta^{0.3766}$ over $\eta=10^{-8}$ to $10^{-4.6}$ (normalized),
  against the $\eta^{1/3}$ theory (§4.1, Fig. 8).
* **Ideal internal kink.** A poloidal-beta threshold of about 0.375, called
  "consistent" with Bussac's 0.3 although the figure shows $\gamma$ against
  $p_0$ only (§4.1, Fig. 10).
* **2/1 [tearing mode](/definitions/tearing-mode.md):**
  $\gamma\propto\eta^{0.5590}$ over $\eta=10^{-9}$ to $10^{-6.2}$ (normalized),
  against $\eta^{3/5}$; the velocity perturbation peaks at $q=2$ (§4.2,
  Figs. 11–12).

## Limitations

* The full dense eigensolve with filtering "is only suitable for solving
  unstable problems"; stable global Alfvén eigenmodes have not been obtained
  (§3.1.5).
* No cross-code benchmark (MARS, CASTOR, NOVA) is shown; agreement is with
  analytic scalings only (§4).
* Several normalizations are misprinted (length scale $a$ dropped), recorded
  on the Source page.

# Citations

1. [Ma & Guo (2022)](/sources/ma-2022.md) — §§1–5, App. A–B, Figs. 4–12.

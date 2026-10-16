---
type: Method
title: "Variational multiscale (VMS) stabilization for MHD finite elements"
description: "Residual-based stabilization of the Galerkin weak form in which the unresolved scales are modelled as minus a stabilization matrix times the residual; in JOREK it uses a diagonal matrix scaled by element size over the fast magnetosonic speed and a residual truncated to its convective part, and it contains streamline diffusion and Taylor–Galerkin stabilization as special cases."
status: established
aliases: [VMS, variational multiscale method, residual-based stabilization, streamline diffusion, Taylor–Galerkin stabilization, TG2]
tags: [stabilization, finite-elements, numerics, full-mhd, reduced-mhd]
timestamp: 2026-10-16T20:00:00Z
---

# Variational multiscale (VMS) stabilization for MHD finite elements

The Galerkin method gives centred approximations that suffer dispersion errors
in convection-dominated flow; residual-based stabilization adds a term that
vanishes with the residual and with the mesh size
([Bhole et al. (2023)](/sources/bhole-2023.md), §1, §3). In
[JOREK](/software/jorek.md) the framework is the variational multiscale
method, of which streamline-upwind Petrov–Galerkin and Taylor–Galerkin
stabilization are subsets ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md),
§3.3). Bhole et al. combine it with a
[shock-capturing artificial viscosity](/methods/shock-capturing-artificial-viscosity.md)
on the [Bézier–Hermite elements](/methods/bezier-finite-elements.md); the
VMS term is an $L^2$-type stabilization, the shock-capturing term a BV-type
one (§1, §3).

## Formulation

Write the model in primitive variables as $\mathcal R(\mathbf u)=0$, with
$\mathcal R$ the residual of the equations (time derivative, fluxes and
sources). In the full-MHD model with impurities of Bhole et al. the unknowns
are $\mathbf u=(A_R,A_Z,\psi,v_R,v_Z,v_\phi,\rho,T,\rho_{\mathrm{imp}})$,
$\rho_{\mathrm{imp}}=m_{\mathrm{imp}}n_{\mathrm{imp}}$ the impurity mass
density (Eqs. 17–18). The solution and test spaces are split into resolved and
unresolved parts, $\mathbf u=\bar{\mathbf u}+\mathbf u'$, and the residual is
linearized about the resolved part,
$\mathcal R(\bar{\mathbf u}+\mathbf u')\approx\mathcal R(\bar{\mathbf u})+\mathcal L\,\mathbf u'$
with $\mathcal L=\partial\mathcal R/\partial\mathbf u$ (Eq. 23). Modelling the
subscales as $\mathbf u'\simeq-\tau_{\mathrm s}\,\mathcal R(\bar{\mathbf u})$,
$\tau_{\mathrm s}\approx\mathcal L^{-1}$, and moving $\mathcal L$ onto the
test function $\mathbf w$ gives
$$\int_\Omega\mathbf w\cdot\mathcal R(\bar{\mathbf u})\,\mathrm dV-\int_\Omega\big(\mathcal L^{\mathsf T}\mathbf w\big)\cdot\big(\tau_{\mathrm s}\,\mathcal R(\bar{\mathbf u})\big)\,\mathrm dV=0\qquad\forall\,\mathbf w$$
([Bhole et al. (2023)](/sources/bhole-2023.md), Eq. 24). The subscales are
assumed to vanish on element boundaries, so the term is element-local and has
no inter-element jump contributions (§3.1); it adds only local element
contributions and no parallel communication (p. 16). If $\mathcal L$ is
symmetric and $\mathcal R\approx\mathcal L\bar{\mathbf u}$, the term is a sum of
products $\int(\mathcal L_\ell^{\mathsf T}\mathbf w)\cdot\tau_\ell\,\mathcal L_\ell\bar{\mathbf u}$
and is dissipative (Eq. 26).

**Stabilization matrix.** It is diagonal,
$$\tau_{\mathrm s}=\frac{h_e}{v^{e}_{\mathrm f,\max}}\,\mathrm{diag}\big(C_{A_R},C_{A_Z},C_{\psi},C_{v_R},C_{v_Z},C_{v_\phi},C_\rho,C_T,C_{\rho_{\mathrm{imp}}}\big),$$
with $C_i\ge0$ user constants, $v^e_{\mathrm f,\max}$ the largest fast
magnetosonic speed in element $e$, and $h_e$ the shorter of the two segments
joining the midpoints of opposite edges of the element, treated as
straight-edged ([Bhole et al. (2023)](/sources/bhole-2023.md), Eq. 25). Since
$v^e_{\mathrm f,\max}$ does not depend on the mesh, $\tau_{\mathrm s}\propto h_e$
and the term vanishes under refinement, which the authors state keeps the
order of accuracy of the Galerkin method (§1, §3.1; no convergence study is
shown).

**Truncated residual.** In practice the residual is replaced by its
first-order (convective) part $\mathcal L_a$: second-order diffusive terms,
the time derivative and the sources are dropped, and
$$\mathcal D_{\mathrm{VMS}}(\bar{\mathbf u},\mathbf w)=\big(\mathcal L_a^{\mathsf T}\mathbf w\big)\cdot\big(\tau_{\mathrm s}\,\mathcal L_a\bar{\mathbf u}\big)$$
(Eq. 27). Acting on $(\mathbf A,\mathbf v,\rho,T,\rho_{\mathrm{imp}})$ the
operator is
$$\mathcal L_a=\begin{bmatrix}-\mathbf v\times\nabla\times & 0 & 0 & 0 & 0\\ 0 & \mathbf v\cdot\nabla & \frac{T}{\rho}\nabla & \nabla & 0\\ 0 & \rho\,\nabla\cdot & \mathbf v\cdot\nabla & 0 & 0\\ 0 & (\Gamma-1)T\,\nabla\cdot & 0 & \mathbf v\cdot\nabla & 0\\ 0 & 0 & 0 & 0 & \mathbf v\cdot\nabla\end{bmatrix}$$
(Eq. 28; the paper writes $\nabla^{\mathsf T}$ for the divergence): the
acoustic block of the Euler equations in primitive variables plus passive
advection of $\mathbf A$ and $\rho_{\mathrm{imp}}$. The option used in every
test of the paper keeps only the diagonal,
$\mathcal L_d=\mathrm{diag}(-\mathbf v\times\nabla\times,\ \mathbf v\cdot\nabla,\ \mathbf v\cdot\nabla,\ \mathbf v\cdot\nabla,\ \mathbf v\cdot\nabla)$
(Eqs. 29–30), which reduces the method to streamline diffusion per variable,
$\tau_{\mathrm s}(\mathbf v\cdot\nabla\mathbf w)\cdot(\mathbf v\cdot\nabla\bar{\mathbf u})$,
with the time scale set by the fast speed rather than by $|\mathbf v|$; for
$\mathbf A$ the term is
$\tau_{\mathrm s}(\mathbf v\times\nabla\times\mathbf A^{*})\cdot(\mathbf v\times\nabla\times\mathbf A)$.
The term is assembled per projected equation with the test functions of the
model (momentum test functions weighted by $\rho$, the toroidal momentum row
projected on $\mathbf B$) and is advanced implicitly with the same
$\theta_{\mathrm t}$-weighting as the rest of the
[implicit scheme](/methods/implicit-time-integration.md) (Eqs. 37, 40).

## Anisotropic artificial diffusion and Taylor–Galerkin

[Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§3.3) write the same
framework, for density advection, as an anisotropic artificial diffusion
$$\underline{\mathbf D}_{\mathrm{VMS}}=D_{\parallel,\mathrm{VMS}}\,\mathbf b\otimes\mathbf b+D_{\perp,\mathrm{VMS}}(\mathsf I-\mathbf b\otimes\mathbf b),\quad D_{\parallel,\mathrm{VMS}}=\tau^{\parallel}_{\mathrm s}(\mathbf v\cdot\mathbf b)^2,\quad D_{\perp,\mathrm{VMS}}=\tau^{\perp}_{\mathrm s}\big(\mathbf v\cdot\mathbf v-(\mathbf v\cdot\mathbf b)^2\big),$$
with $\tau_{\mathrm s}\sim h_e/c_{\max}$ ($c_{\max}$ the largest wave speed),
so that the diffusion vanishes under refinement. Second-order Taylor–Galerkin
(TG2) is the choice $\tau_{\mathrm s}=\Delta t/2$; with the reduced-MHD velocity
$\mathbf v=-R^2\nabla u\times\nabla\phi+\hat v_\parallel\mathbf B$ it adds
$$\frac{\Delta t}{2}\nabla\cdot\big(\hat v_\parallel^2\,\mathbf B\,\mathbf B\cdot\nabla\rho\big)+\frac{\Delta t}{2}\nabla\cdot\Big(R^4\,\nabla u\times\nabla\phi\,\big[(\nabla u\times\nabla\phi)\cdot\nabla\rho\big]\Big)$$
to the density equation (§3.3; $\hat v_\parallel$ is the coefficient of
$\mathbf B$, as in the [reduced-MHD](/methods/reduced-mhd.md) ansatz of the
source). Taylor–Galerkin with optional fourth-order hyperdiffusion was the
earlier JOREK stabilization for reduced MHD
([Bhole et al. (2023)](/sources/bhole-2023.md), §1, §3.2). Full MHD uses a
global hyperbolic VMS formulation
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §3.3). The review lists
stabilized finite elements for reduced and full MHD among the 2021–2024
numerical developments ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §5).
The predictive HL-3 QH-mode runs in reduced MHD apply Taylor–Galerkin
stabilization to the $u$, $\rho$, $T$ and $\hat v_\parallel$ equations, stated to act
"without affecting the physical solution"; no test of that statement is shown
([Liang et al. (2025)](/sources/liang-2025.md), §III).

## Evidence

- Hoelzl et al. state that the stabilization has negligible effect on the
  physics and on energy and momentum conservation, checked by the convergence
  tests (§3.3); the energy balance closes to about 90% in massive-material
  injection runs with Taylor–Galerkin stabilization (§4.3).
- Bhole et al. run VMS with $\mathcal L_d$ and $C_i=10^{-2}$ in the full-MHD
  axisymmetric and 3D neon-SPI cases, always together with shock capturing
  (§4.2.1.2, §4.3.1); the cost and accuracy results are on the
  [shock-capturing page](/methods/shock-capturing-artificial-viscosity.md).

## Qualifications

- **VMS alone is never isolated.** Every stabilized run of
  [Bhole et al. (2023)](/sources/bhole-2023.md) combines VMS with shock
  capturing, the unstabilized run has neither, and the reduced-MHD test does
  not say whether VMS was on (§4.2.1.1, §4.3.1; reader's note). The benefit
  reported there cannot be attributed to the VMS term.
- **$\mathcal L_a$ is not the convective part of the MHD Jacobian.** It omits
  every magnetic coupling: the Lorentz force in the momentum rows and the
  cross terms of $\nabla\times(\mathbf v\times\mathbf B)$, and also the impurity
  contribution to the pressure, although the text calls it the residual with
  the second-order terms excluded (Eq. 28; reader's note). The
  stabilization is therefore a hydrodynamic one with a fast-wave time scale.
- **Missing coefficient.** Eq. 25 prints eight coefficients for nine
  unknowns: $C_{v_\phi}$ is absent and the $\psi$ slot is labelled $C_{A_\phi}$
  (reader's note); the matrix above restores the ninth entry by the paper's
  own rule.
- The symbol the paper uses for the Jacobian also denotes the ionization
  potential-energy term (Eq. 13) and the operator part of a tendency (Eq. 33)
  (reader's note).
- The version of Bhole et al. read is the HAL submission (October 2022); the published version
  has more references and may differ ([Bhole et al. (2023)](/sources/bhole-2023.md),
  identity).

# Citations

- [Bhole et al. (2023)](/sources/bhole-2023.md) — §1, §3.1, Eqs. 20–30, 37, 40.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §3.3, §4.3.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §5.
- [Liang et al. (2025)](/sources/liang-2025.md) — §III.

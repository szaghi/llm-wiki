---
type: Method
title: "Continuous-Galerkin spectral-element method"
description: "The continuous-Galerkin spectral-element method expands the solution in tensor-product Lagrange polynomials on LGL nodes, continuous across elements by direct stiffness summation; this page covers its formulation, the derivative jumps and weak wall-stress imposition that shape LES on it, nodal subgrid coefficients and filter widths, and implicit RANS source terms."
status: established
aliases: [SEM, CG-SEM, continuous Galerkin spectral element method, spectral/hp continuous Galerkin, direct stiffness summation]
tags: [spectral-element, les, wmles, sgs-model, numerical-dissipation]
timestamp: 2026-10-27T10:58:00Z
---

# Continuous-Galerkin spectral-element method

The **continuous-Galerkin spectral-element method (CG-SEM)** divides the
domain into hexahedral (or quadrilateral) elements and represents the
solution in each by tensor-product Lagrange polynomials of degree $N$ on
$N+1$ Legendre–Gauss–Lobatto (LGL; the sources' GLL) nodes per direction,
$(N+1)^3$ nodes per element. Unlike the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md), the
solution is **continuous** across element faces: shared face nodes carry one
value, imposed by a gather–scatter, or direct stiffness summation (DSS), of
the element contributions; the gradient is not continuous. Collocated LGL
quadrature gives a diagonal mass matrix. In this bundle the method is the
discretization of [Nek5000 and NekRS](/software/nek5000.md) (incompressible;
[Fischer et al. 2022](/sources/fischer-2022.md);
[Gillyns et al. 2022](/sources/gillyns-2022.md);
[Mukha et al. 2025](/sources/mukha-2025.md);
[Tomboulides et al. 2025](/sources/tomboulides-2025.md), for RANS), of the
continuous option of
[Nektar++](/software/nektar-plus-plus.md)
([Saini et al. 2023](/sources/saini-2023.md)), and of the atmospheric model
NUMA ([Reddy et al. 2026](/sources/reddy-2026.md), compressible at low Mach
number).

## Formulation

Reddy et al. (2026, §4, Eqs. 15–23) write the system as
$\partial_t\boldsymbol q+\nabla\cdot\mathcal F(\boldsymbol q)=\mathcal S(\boldsymbol q)$
(page-local $\boldsymbol q$ the state, $\mathcal F$ the flux, $\mathcal S$
the source) and take its weak form element by element with the Lagrange
basis $\psi$ on the $(N+1)^3$ LGL points, the roots of
$(1-\xi^2)P'_N(\xi)$ ($P_N$ the Legendre polynomial, page-local), with
weights $w_i=\frac{2}{N(N+1)}\big(1/P_N(\xi_i)\big)^2$ (Eq. 21). Integration
is inexact (collocated), the mass matrix is diagonal, and because the
solution is continuous, flux terms survive only at physical boundaries; the
element contributions are assembled by DSS through a map from element-local
to global node numbers (Eqs. 22–23). A diffusion term with a
space-dependent coefficient $\mu(\boldsymbol x)$ (page-local, an eddy
diffusivity) is integrated by parts as
$$\int_{\Omega_e}\psi\,\nabla\cdot(\mu\nabla\boldsymbol q)\,d\Omega_e=\int_{\Gamma_e}\mu\,\psi\,(\boldsymbol n\cdot\nabla\boldsymbol q)\,d\Gamma_e-\int_{\Omega_e}\mu\,\nabla\psi\cdot\nabla\boldsymbol q\,d\Omega_e\qquad(\text{Eq. 18}),$$
which admits an eddy diffusivity that varies within an element (below).

In Nek5000 (Mukha et al. 2025, §II.B; Fischer et al. 2022, §2.1–2.3, as on
the Nek5000 page): $N=7$, the $P_N$–$P_{N-2}$ formulation (pressure two
degrees lower), 3/2 over-integration of the convective term,
BDF3 for the viscous term with third-order extrapolation (EXT3) of
convection, operator splitting, a conjugate-gradient momentum solve and a
GMRES pressure-Poisson solve with an additive overlapping Schwarz
preconditioner and an XXT coarse-grid solver; derivatives are tensor
contractions with the differentiation matrix $D_{ij}$, and the
gather–scatter has a unit-depth stencil for every $N$. NUMA advances
explicitly with a five-stage third-order strong-stability-preserving
Runge–Kutta scheme, or with a second-order IMEX additive Runge–Kutta scheme
that treats acoustic and gravity waves implicitly (Reddy et al. 2026, §5–8).

**Implicit RANS source terms.** Tomboulides et al. (2025, §2.2, Eqs.
32–38) fold the non-linear source terms of two-equation RANS models into
the Helmholtz operator of the BDF$k$/EXT$k$ scheme. Each transported scalar
$\phi\in\{k,\tau_t\}$ ($\tau_t=1/\omega$ the turbulent time scale of the
[$k$-$\tau$ model](/methods/k-tau-model.md), page-local, not a stress) obeys
$\rho(\partial_t\phi+\boldsymbol u\cdot\nabla\phi)=\nabla\cdot(\Gamma\nabla\phi)+s_{nl}\phi+s_l$,
with $s_l$ the part of the source independent of $\phi$ and $s_{nl}$ a
coefficient multiplying $\phi$ ($\Gamma$ the diffusivity, $\Gamma_k$ or
$\Gamma_\omega$ of the $k$-$\tau$ page; page-local $s_l$, $s_{nl}$). The
Galerkin semi-discretization with the nodal LGL basis reads
$$\mathsf M\frac{d\boldsymbol\phi}{dt}=-\mathsf C\boldsymbol\phi-\mathsf K\boldsymbol\phi+\mathsf M\boldsymbol f+\mathsf M\mathsf S_{nl}\boldsymbol\phi,$$
with $\mathsf M$ the diagonal mass matrix, $\mathsf C$ convection,
$\mathsf K$ the symmetric positive-definite stiffness and $\mathsf S_{nl}$
the diagonal matrix of nodal $s_{nl}$ values (page-local matrices). Writing
$\hat{\mathsf K}=\mathsf K-\mathsf M\mathsf S_{nl}$, the implicit step
solves the Helmholtz system $\big((b_0/\Delta t)\mathsf M+\hat{\mathsf K}\big)\Delta\boldsymbol\phi=\dots$
with BDF coefficients $b_j$ and extrapolated convection, which costs nothing
beyond the Helmholtz solve already needed, and leaves only the convective
CFL limit, about 0.5 for BDF2 (higher with the operator-integration-factor
characteristics scheme) (§2.2). Every printed term of $s_{nl}$ is
non-positive for non-negative coefficients, $k$ and $\tau_t$, so $\hat{\mathsf K}$ stays
symmetric positive definite *(compiler check, not in the sources)*. On an
OECD/NEA T-junction the $k$-$\tau$ model so treated ran at CFL $\sim2$,
whereas the authors' regularized $k$-$\omega$ model, whose extra
wall-distance source terms cannot be treated implicitly, was restricted to
CFL $\sim0.1$ (§3.5, §4).

## Consequences of continuity for LES

**Mass but not momentum.** Mukha et al. (2025, §II.B) state that the
continuous velocity conserves mass globally if it is locally divergence-free,
but global momentum conservation is not guaranteed, because velocity
derivatives jump across element boundaries; the jumps shrink with refinement
and are negligible at wall-resolved resolution, but significant for
[wall-modelled LES](/methods/wall-modelled-les.md).

**Derivative jumps and Gibbs spikes.** On coarse meshes the fluctuation
statistics show spikes at element faces, a Gibbs phenomenon of the $C^0$
discretization that vanishes as the mesh approaches DNS resolution (Gillyns
et al. 2022, §2, §6). Mukha et al. (2025, §III.B.2, §III.C, Figs. 3, 7) see
the jumps in the log-law indicator
$\kappa y^+\,\mathrm d\langle u\rangle^+/\mathrm dy^+$, which converges only
for $y>0.25\delta$ on their two finer meshes, and in spikes of the subgrid
viscosity, which they call "just numerical artifacts"; ensuring the
continuity of velocity derivatives is, in their words, "a missing component
in the current WMLES methodology".

**Weakly imposed wall stress.** With a Neumann condition on the wall-parallel
velocity, the wall-model stress enters the weak form as a natural boundary
term (Mukha et al. 2025, §II.C.2, Eqs. 7–12): with $\tau^{\mathrm{tot}}_{ij}$
(page-local) the combined viscous and subgrid stress, test functions $v_i$
and $\tau_{w,i}$ the wall-parallel stress,
$$\int_\Omega\frac{\partial v_i}{\partial x_j}\tau^{\mathrm{tot}}_{ij}\,d\Omega=\int_{\partial\Omega}\big[v_i\tau_{w,i}+(\tau^{\mathrm{tot}}_{jk}n_kn_j)\,v_in_i\big]\,dS,$$
where the second term vanishes by the strongly imposed non-penetration
$v_in_i=0$ and the first vanishes for no-slip, so only the Neumann condition
feeds the modelled stress. Because the condition is weak, the stress computed
from the mean velocity gradient at the wall differs from the modelled one
by 12.58%, 10.86% and 8.07% of the reference on their three channel meshes
at $Re_\tau\approx8000$, against modelled-stress errors below 1% (Table II);
the authors judge the wall-gradient value one that "should essentially be
disregarded" and call the issue "unique to the finite element method"
(§II.C.3, §III.B.2). The alternative, imposing no-slip and a wall value of
the subgrid viscosity that produces the modelled stress (strong imposition),
fails in the CG-SEM through the momentum imbalance: errors of the stress
implied by the driving pressure gradient of 38.05%, 25.73% and 15.65%
(Table IV, §III.D). Details are on
[wall-modelled LES](/methods/wall-modelled-les.md) and the
[equilibrium wall model](/methods/equilibrium-wall-model.md).

**Subgrid models as stabilizers.** In Mukha et al.'s WMLES (§III.C, Fig. 8)
the explicit [Vreman](/methods/vreman-model.md) and Sigma models stabilize
the solution better than Nek5000's high-pass relaxation filter used as an
implicit model (a forcing $\chi_{\mathrm{hp}}(\boldsymbol u-\boldsymbol u^{\mathrm{lp}})$
added to the momentum equation, page-local $\chi_{\mathrm{hp}}$ its strength
and $\boldsymbol u^{\mathrm{lp}}$ the modally low-pass-filtered velocity, as
printed in §II.A, Eq. 4): two filtered modes with $\chi_{\mathrm{hp}}=100$
increase near-wall oscillations and over-predict
$\langle u'u'\rangle$, and filtering alone "does not introduce enough damping
to avoid the contamination of the solution with numerical artifacts"; with
Sigma or the filter the wall-gradient stress errors grow to $-25.72\%$ and
$-84.85\%$ against 8.07% with Vreman (§III.C).

## Subgrid coefficients and filter width on spectral elements

**Nodal against elemental coefficients.** Reddy et al. (2026, §1, §3.3)
state that subgrid models in element-based Galerkin methods have assumed an
eddy diffusivity constant within each element even for high-order elements,
and compare that elemental form (the maximum over the element's LGL points)
with a nodal form expanded in the same basis as the solution, which Eq. (18)
admits. The elemental form is the more dissipative in all four of their
tests ($N=4$: tracer advection, a two-dimensional Burgers system, the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) on $32^3$
elements, a density current); the models compared are on
[residual-based dynamic SGS model](/methods/residual-based-dynamic-sgs-model.md),
[Smagorinsky](/methods/smagorinsky-model.md) and
[Vreman](/methods/vreman-model.md).

**Filter width.** Reddy et al. (2026, §3.4) use
$\Delta=\min(\Delta x,\Delta y,\Delta z)/(N+1)$ on isotropic meshes, with
$\Delta x$ the element size, and list in Table 1 the anisotropic
alternatives $(\Delta x\Delta y\Delta z)^{1/3}/N$ and the Scotti–Meneveau–Lilly
correction of it. Mukha et al. (2025, §II.D) base the subgrid length scale
on the local LGL spacing and conservatively assign the maximum over the
element to the whole element. The DG sources use $V_e^{1/3}/(N+1)$ (see the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md), "Filter
width").

## Numerical dissipation

Reddy et al. (2026, §1) call a spectral-element discretization "ideal" for
comparing subgrid models "due to the lack of inherent numerical dissipation
present", and define in the Taylor–Green vortex an effective viscosity
$\varepsilon=\nu_{\mathrm{eff}}\langle\omega_i\omega_i\rangle$ (page-local
$\nu_{\mathrm{eff}}$) that lumps subgrid and numerical dissipation (§7.1).
[Saini et al. (2023)](/sources/saini-2023.md), §2.1, §6, run the continuous
spectral/hp solver of Nektar++ at order 4 (velocity) and 3 (pressure) with
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
and measure its numerical plus model dissipation at about a quarter of that
of a second-order finite-volume LES at similar cost. Mukha et al. (2025)
need the subgrid model for stability (above). See
[numerical dissipation](/properties/numerical-dissipation.md).

## Near-wall resolution and $N$-convergence in RANS

Tomboulides et al. (2025, §3) show that the CG-SEM of
[Nek5000](/software/nek5000.md) gives RANS solutions insensitive to
$N$ and to the near-wall resolution once the wall singularity of $\omega$ is
removed by the [$k$-$\tau$ model](/methods/k-tau-model.md): in a
[channel](/benchmarks/turbulent-channel-flow.md) at $Re_\tau\approx5200$
with 7 elements across the half channel, $N=3,5,7,9$ put the first LGL
point at $y^+=1.7$, 0.73, 0.39, 0.25, and velocity, $k^+$ and the scaled
time scale are indistinguishable except at $N=3$ (§3.1, Figs. 1–2); airfoil
results at $N=5$ and 7 differ by less than 0.1% (§3.4), and T-junction
profiles at $N=5$, 7, 9 by "very minor" amounts (§3.5). They attribute the
persistent oscillations of the standard $k$-$\omega$ model with a large
prescribed wall $\omega$ to the negligible numerical diffusion of high-order
codes (§1); see [$k$-$\omega$ model](/methods/k-omega-model.md).

## Qualifications

- **Absence of numerical dissipation.** Reddy et al.'s statement is not
  tested in their paper, which measures no numerical dissipation separately;
  Saini et al. (2023) measure numerical and model dissipation together, and
  Mukha et al. (2025) and Gillyns et al. (2022) report derivative jumps and
  instabilities on coarse meshes. The sources address different quantities,
  so no contradiction is recorded.
- **Version and framing (Reddy et al. 2026).** The version read is a
  preprint dated 4 March 2021; its title names the Navier–Stokes equations
  while §2 solves the compressible Euler equations with no molecular
  viscosity. Table 1 divides by $N$ where the width used (§3.4) and the
  same table's aspect ratios divide by $N+1$.
- **Node counts (Mukha et al. 2025, arXiv v1).** The total node counts of
  Table I equal $(N+1)^3$ times the number of elements, those of Table V
  $N^3$ times it, although both captions say "total number of nodes"
  *(compiler check, not in the sources)*; the first counts element-local
  nodes with duplicates, the second approximately unique nodes.
- **High-pass filter strength.** Mukha et al. filter two modes with
  $\chi_{\mathrm{hp}}=100$, whereas Gillyns et al. (2022) used
  $\chi_{\mathrm{hp}}=10$ on the highest mode, as recalled by Mukha et al.
  (§II.D). Mukha et al. also did not see the divergence without time
  averaging of the wall-model input that Gillyns et al. report (§II.C.1);
  the two concern different set-ups (wall law, matching height, subgrid
  treatment), as recorded on the
  [equilibrium wall model](/methods/equilibrium-wall-model.md) page.
- **Not among the methods of the First High-Order CFD Workshop.** The summary of the First
  High-Order CFD Workshop by [Wang et al. (2013)](/sources/wang-2013.md)
  cites Patera's spectral element method among the
  high-order methods for unstructured meshes (§1) and defines the acronym
  SEM in its Table I, but none of the participants of Tables II–VII
  submitted CG-SEM results. The only spectral-element entry is Stuttgart's
  discontinuous DGSEM on the
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) (Table VII),
  whose order study is reported on the DGSEM page.

# Citations

- [Mukha et al. (2025)](/sources/mukha-2025.md) — arXiv 2404.05378v1: §II.A, Eq. (4) (high-pass relaxation filter); §II.B (CG-SEM in Nek5000, mass and momentum conservation); §II.C.1–II.C.4, Eqs. (7)–(14) (weak wall-stress term, Neumann and viscosity-based conditions); §II.D (SGS length scale); §III.B–III.D, Tables I–IV, Figs. 3, 7–8 (derivative jumps, wall-stress errors, SGS treatments); Table V.
- [Reddy et al. (2026)](/sources/reddy-2026.md) — preprint of 4 March 2021: §1 (element-constant eddy diffusivity, lack of numerical dissipation); §3.3–3.4, Table 1 (elemental and nodal coefficients, filter width); §4, Eqs. (15)–(23) (CG-SEM in NUMA, LGL nodes, DSS, variable-coefficient diffusion); §5–8 (time integration, tests); §7.1 (effective viscosity).
- [Fischer et al. (2022)](/sources/fischer-2022.md) — §2.1–2.3 (spectral elements, gather–scatter, time stepping).
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §2, §6 ($C^0$ continuity, Gibbs spikes at element faces).
- [Saini et al. (2023)](/sources/saini-2023.md) — §2.1, §6 (Nektar++ continuous Galerkin with SVV, dissipation against finite volumes).
- [Wang et al. (2013)](/sources/wang-2013.md) — §1 (Patera's method cited); Tables I–VII (acronyms and participants).
- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) — §1 (oscillations of high-order $k$-$\omega$); §2.2, Eqs. (32)–(38) (implicit source terms in the Helmholtz operator); §3.1, Figs. 1–2; §3.4–3.5 ($N$-convergence, CFL on the T-junction).

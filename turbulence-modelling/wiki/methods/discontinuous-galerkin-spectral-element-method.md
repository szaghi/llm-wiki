---
type: Method
title: "Discontinuous Galerkin spectral element method"
description: "The DGSEM is a collocated nodal discontinuous Galerkin scheme on tensor-product hexahedra with Legendre–Gauss or Gauss–Lobatto nodes; this page states its weak and strong forms, the SBP property, its cost per degree of freedom and how its interface dissipation shapes LES on it."
status: established
aliases: [DGSEM, nodal discontinuous Galerkin, collocation DG, DG spectral element method]
tags: [dg, numerical-dissipation, kinetic-energy-preserving, les, dns]
timestamp: 2026-10-25T13:42:00Z
---

# Discontinuous Galerkin spectral element method

The **discontinuous Galerkin spectral element method (DGSEM)** approximates the
solution of a conservation law $\partial_t U+\nabla\cdot(F^c(U)-F^v(U,\nabla U))=0$
in each hexahedral element by a tensor-product Lagrange polynomial of degree
$N$ on $N+1$ nodes per direction, $(N+1)^3$ nodes per element, with the
interpolation and quadrature nodes collocated (Legendre–Gauss, LG, or
Legendre–Gauss–Lobatto, LGL). Elements couple only through a numerical
interface flux $f^*$ (an approximate Riemann solver), and viscous terms
through a lifting procedure. It is the discretization of the
[FLEXI](/software/flexi.md) framework derived in full by
[Krais et al. (2021)](/sources/krais-2021.md), the baseline of the
kinetic-energy-preserving LES of [Flad & Gassner (2017)](/sources/flad-2017.md)
and of the learned closures of [Beck & Kurz (2023)](/sources/beck-2023.md).

## Approximation on curvilinear hexahedra

Each element is the image of the reference cube $E=[-1,1]^3$ under a polynomial
map $\boldsymbol x=\boldsymbol\chi(\boldsymbol\xi)$ of geometry degree
$N_{\mathrm{geo}}$ (independent of $N$), with Jacobian determinant
$\mathcal J$ (page-local symbols). The solution is
$$U(\boldsymbol\xi,t)\approx\sum_{i,j,k=0}^{N}U_{ijk}(t)\,\ell_i(\xi^1)\ell_j(\xi^2)\ell_k(\xi^3),\qquad \ell_j(\xi)=\prod_{i\ne j}\frac{\xi-\xi_i}{\xi_j-\xi_i},$$
and the differentiation matrix is $D_{ij}=\ell_j'(\xi_i)$ (Krais et al. 2021,
§3.1, Eqs. 2–18; Flad & Gassner 2017, §2.1, Eqs. 4–9; Beck & Kurz 2023,
§III A, Eq. 7). The divergence is transformed to reference space with the
contravariant metric terms $\mathcal J\boldsymbol a^i$; Krais et al. (2021,
Eq. 4) compute them in the **curl form**, which satisfies the discrete metric
identities, the condition they state (citing Kopriva) for free-stream
preservation on curved meshes.

Because the nodes are collocated with Gauss-type quadrature, the mass matrix is
diagonal, $M=\mathrm{diag}(w_0,\dots,w_N)$ in one direction. For LG nodes the
quadrature is exact to degree $2N+1$ and the diagonal mass matrix is exact (for
a constant Jacobian); for LGL nodes it is exact to degree $2N-1$ and the mass
matrix is a lumped approximation (Krais et al. 2021, §3.1, Eq. 15).

## Weak and strong forms

Integrating by parts against the test function gives the **weak form**; the
semi-discrete update of the first reference direction reads (Krais et al. 2021,
Eq. 30, Cartesian factors omitted)
$$\frac{\partial U_{ijk}}{\partial t}=-\frac{1}{\mathcal J_{ijk}}\Big[\sum_{m=0}^{N}\mathcal F^1_{mjk}\hat D_{im}+\big[f^*\hat s\big]^{+\xi^1}_{jk}\frac{\ell_i(1)}{w_i}+\big[f^*\hat s\big]^{-\xi^1}_{jk}\frac{\ell_i(-1)}{w_i}+\dots\Big],$$
with $\mathcal F^1$ the contravariant flux, $\hat s$ the surface element and
$\hat D$ the weak-form differentiation matrix (see Qualifications for its
printed form). Integrating by parts a second time gives the **strong form**,
whose volume term uses $D$ itself and whose surface term is the jump
$f^*-\mathcal F$ between the numerical and the interior flux, which vanishes
for a continuous solution (Krais et al. 2021, Eqs. 32–33). The two forms are
analytically and discretely identical for LGL quadrature, and for LG with
special care of the interior fluxes (Krais et al. 2021, §3.1, citing Kopriva &
Gassner).

On LGL nodes the strong-form DGSEM has the **summation-by-parts (SBP)**
property
$$(MD)+(MD)^{\mathsf T}=B,\qquad B=\mathrm{diag}(-1,0,\dots,0,1)$$
(Flad & Gassner 2017, Eq. 9). It is the property that lets the volume term be
rewritten with a symmetric two-point flux $f^{\#}$, the split-form DG
described on [kinetic-energy preservation](/properties/kinetic-energy-preservation.md);
both Flad & Gassner (2017, §2.1) and Krais et al. (2021, §3.3) call the LGL
variant essential for it.

## Viscous terms

The gradients are introduced as auxiliary unknowns (lifting) and discretized
with the same DGSEM. In the BR1 scheme of Bassi & Rebay (as recalled by Krais
et al. 2021, Eqs. 34–42) both the lifted solution and the viscous flux at an
interface are arithmetic means, $U^*=\{\!\{U\}\!\}$ and
$F^{v*}=\tfrac12\big(F^v(U^L,\nabla U^L)+F^v(U^R,\nabla U^R)\big)$; FLEXI lifts
the primitive variables. BR2 adds an interface penalty on the solution jump,
controlled by a constant $\eta_{BR}\ge1$; Flad & Gassner (2017, §2.1, App. E)
use $\eta_{BR}=2$ as one of their small-scale damping strategies and
$\eta_{BR}=1$ in the interior with $\eta_{BR}=40$ at the walls of their channel,
where weakly imposed wall conditions otherwise give too-large wall velocities.

## Non-linear stability: de-aliasing or split form

For under-resolved turbulence the collocated evaluation of non-linear fluxes
produces aliasing. Two remedies appear in the sources:

- **Polynomial de-aliasing (over-integration).** The fluxes are evaluated on
  $Q+1$ points with $Q=\lfloor\tfrac32(N+1)-1\rfloor$ ($Q=11$ for $N=7$, i.e.
  $12^3$ quadrature points per element) and projected back by a modal cut-off
  (Flad & Gassner 2017, §2.1, Eq. 11). As recalled there, the rational flux of
  the compressible equations cannot be projected exactly, so the rule assumes
  weak compressibility. Without it, the $N=7$ DG implicit LES of decaying
  isotropic turbulence was unstable (§1, stated without figure).
- **Split form (flux differencing)** on LGL nodes, which builds the
  de-aliasing into the volume term. Flad & Gassner (2017, §6.1) state that it
  costs at least three times less than polynomial de-aliasing in their
  in-house code (no timing given).

## Cost per degree of freedom

Krais et al. (2021, §5.6, Table 3) count, per element and variable, $3(N+1)^4$
operations for the volume integral against $3(N+1)^3$ for the volume fluxes and
$O((N+1)^2)$ to $O((N+1)^3)$ for the surface terms, so the operations per
degree of freedom grow as $O(N)$. The tensor-product structure keeps every
operator one-dimensional. The measured memory per degree of freedom decreases
with $N$: 1.47 KiB at $N=1$, 0.74 KiB at $N=5$, 0.567 KiB at $N=12$ (Table 4).
The explicit time step obeys (Eqs. 65–66)
$$\Delta t\le \mathrm{CFL}\,c^{c}_{RK}(N)\,\frac{h}{\lambda^c(2N+1)},\qquad \Delta t\le \mathrm{CFL}_d\,c^{v}_{RK}(N)\,\frac{h^2}{\lambda^v(2N+1)},$$
with $h$ the element size, $\lambda^c$ the largest convective signal speed,
$\lambda^v$ the largest eigenvalue of the diffusion matrix, and
$c^{c}_{RK}(N)$, $c^{v}_{RK}(N)$ (page-local) empirical factors depending on
$N$, the node set and the Runge–Kutta scheme; Krais et al. state that the
classical $1/(2N+1)$ scaling alone is "in practice not accurate" and print no
values of the factors.

## The DGSEM as an LES discretization

**Interface dissipation.** Element methods with Riemann solvers have very low
dispersion error over a broad range of scales, with dissipation near zero for
resolved scales and very high near the cut-off; the interface dissipation acts
like a high-frequency filter (Flad & Gassner 2017, Abstract, §3.1). Beck & Kurz
(2023, §V) add that this numerical dissipation is localized at the element faces
and becomes more so as $N$ grows; the time-averaged coefficient of their
element-wise quadratic reinforcement-learning Smagorinsky model peaks at the
element centre and falls towards zero at the faces, which they read, as a
hypothesis needing further study, as homogenizing the total dissipation (see
[numerical dissipation](/properties/numerical-dissipation.md) and
[reinforcement-learning closures](/methods/reinforcement-learning-closure.md)).

**Implicit LES on the DGSEM.** With Roe or Lax–Friedrichs fluxes and
over-integration, DG [implicit LES](/definitions/implicit-les.md) of decaying
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
($N=7$) is excellent at $144^3$ degrees of freedom but fails at $48^3$, where
energy piles up at intermediate wavenumbers; adding a
[Smagorinsky](/methods/smagorinsky-model.md) or small–small VMS model does not
cure it. Flad & Gassner (2017, §1) infer that roughly 40% of the total
dissipation must be resolved, an "applicability plateau", and explain the
failure by the lack of the low-wavenumber plateau of the
[spectral eddy viscosity](/methods/spectral-eddy-viscosity.md) in the interface
dissipation (§3.1). On a dissipation-free kinetic-energy-preserving split form,
an explicit Smagorinsky model ($C_s=0.12$) succeeds at $48^3$ (§4). Beck & Kurz
(2023, §V A) find in forced isotropic turbulence at 24 and 36 degrees of
freedom per direction that the no-model LES is the best of their reference
closures for $N=3$ and degrades as $N$ grows to 5 and 8.

**Filter width.** A DG element of volume $V_e$ carries $N+1$ nodes per
direction; Beck & Kurz (2023, Eq. 11) set $\Delta=V_e^{1/3}/(N+1)$ and stress
that the choice is not unique (nodes are not equidistant, elements may be
skewed). Flad & Gassner (2017, App. A) print the filter width as the cell
volume divided by $(N+1)^3$ (see Qualifications).

**Resolution per wavelength.** Flad & Gassner (2017, §1, §3) estimate the
resolved wavenumber with 3 points per wavelength (optimistic) and state the
polynomial resolution limit as $\pi$ points per wavelength ($k=15.28$ for $48$
degrees of freedom per direction); Beck & Kurz (2023, §IV A) take 4 points per
wavelength as the resolution limit of the schemes, citing earlier analysis.
The two numbers belong to different criteria and neither source defines a
common error tolerance.

## Variants and relatives

The DGSEM coexists with finite-volume subcells in the
[subcell finite-volume shock-capturing](/methods/subcell-finite-volume-shock-capturing.md)
schemes, where a troubled element is solved on $(N+1)^3$ subcells with the same
data structures. Krais et al. (2021, §3.2) handle non-conforming hexahedral
interfaces (2:1 and 4:1) with Kopriva-type mortars: interpolation to the small
sides and $L^2$ projection of their fluxes back to the large side. The flux
reconstruction scheme used with [PANS](/methods/partially-averaged-navier-stokes.md)
by Dzanic et al. (2022) is described there as a generalization of nodal DG.

## Qualifications

- **Weak-form differentiation matrix.** Krais et al. (2021, Eq. 31) print
  $\hat D_{ij}=-\frac{w_i}{w_j}D_{ji}$. Dividing the weak-form volume term
  $\sum_m w_m D_{mi}\mathcal F_m$ by the mass $w_i$ gives
  $\hat D_{ij}=-\frac{w_j}{w_i}D_{ji}$, consistent with their own
  $\ell_i/w_i$ for the surface term *(compiler check, not in the sources)*.
- **Filter width.** Flad & Gassner (2017, App. A) define $\Delta$ as "the local
  cell volume divided be $(N+1)^3$", which is a volume, not a length; the cube
  root of that ratio, which coincides with Beck & Kurz's (2023)
  $V_e^{1/3}/(N+1)$, is the dimensionally consistent reading *(compiler check,
  not in the sources)*.
- The 40% applicability plateau is inferred by Flad & Gassner (2017) from two
  resolutions of one test case at $N=7$; the authors present it as a
  finding, not a bound.
- The factor-3 saving of split forms over de-aliasing (Flad & Gassner 2017,
  §6.1) is stated without timings or hardware.

# Citations

- [Krais et al. (2021)](/sources/krais-2021.md) — §3.1, Eqs. (1)–(42) (geometry, weak and strong forms, BR1); §3.2 (mortars); §3.3 (split form); §4.4, Eqs. (65)–(67) (time step); §5.6, Tables 3–4 (operation counts, memory).
- [Flad & Gassner (2017)](/sources/flad-2017.md) — §1 (DG implicit LES, applicability plateau); §2.1, Eqs. (4)–(12) (LGL DGSEM, SBP, de-aliasing, split form); §3.1, §4, §6.1; App. A, App. E (BR2 at walls).
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §III A, Eqs. (7)–(8) (DGSEM in FLEXI); Eq. (11) (filter width); §IV A (resolution limit); §V A–B (no-model LES against $N$, face-localized dissipation).
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §2.2 (flux reconstruction as a generalization of nodal DG).

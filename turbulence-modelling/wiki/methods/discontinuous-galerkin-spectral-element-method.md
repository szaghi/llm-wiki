---
type: Method
title: "Discontinuous Galerkin spectral element method"
description: "The DGSEM is a collocated nodal discontinuous Galerkin scheme on tensor-product hexahedra; this page states its weak and strong forms, SBP property, modal filtering and filtered artificial viscosity, cost, how interface dissipation and penalties shape LES on it, its implicit filter, element-local filters and mortars, and modal, interior-penalty and continuous relatives."
status: established
aliases: [DGSEM, nodal discontinuous Galerkin, collocation DG, DG spectral element method]
tags: [dg, numerical-dissipation, kinetic-energy-preserving, entropy-stable, les, dns]
timestamp: 2026-10-26T07:42:00Z
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
kinetic-energy-preserving LES of [Flad & Gassner (2017)](/sources/flad-2017.md),
of the learned closures of [Beck & Kurz (2023)](/sources/beck-2023.md) and
of the entropy-stable spectral vanishing viscosity of
[Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md).

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
preservation on curved meshes; Mateo-Gabín et al. (2022, §3) use the same
conservative Kopriva form for the same reason.

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
(Flad & Gassner 2017, Eq. 9; Mateo-Gabín et al. 2022, Eq. 47, write it with
the mass matrix $P$ and $Q=PD$, $Q+Q^{\mathsf T}=B$). It is the property that
lets the volume term be rewritten with a symmetric two-point flux $f^{\#}$,
the split-form DG described on [kinetic-energy preservation](/properties/kinetic-energy-preservation.md);
both Flad & Gassner (2017, §2.1) and Krais et al. (2021, §3.3) call the LGL
variant essential for it. Mateo-Gabín et al. (2022, §3, Eq. 51) use the
three-dimensional form with the Pirozzoli flux (kinetic-energy preserving)
or the Chandrashekar flux (entropy conserving), and gradients of the entropy
variables as the lifted unknowns.

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
Mateo-Gabín et al. (2022, §3, Eq. 57; §5.1, Eq. 115) treat physical and
artificial viscous fluxes alike with BR1 and show that the interior-face
contributions of both then vanish from the discrete entropy balance; with
their wall treatment (Eqs. 58–61) the adiabatic-wall contributions vanish
too.

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

## Modal filtering and filtered artificial viscosity

**Nodal–modal transforms.** On LGL nodes the nodal values $Q_i$ of a degree-$N$
polynomial and its Legendre coefficients $Q^{(m)}_j$ are related by a
forward matrix $\mathcal V^{-1}$ and a backward (Vandermonde) matrix
$\mathcal V$ that are exact inverses, and the collocated quadrature satisfies
a **discrete Parseval identity**
$$\sum_{i=0}^{N}w_iU_iV_i=\sum_{j=0}^{N}\|\mathcal P_j\|_N^2\,U^{(m)}_jV^{(m)}_j,$$
with $\mathcal P_j$ the Legendre polynomials and $\|\cdot\|_N$ the discrete
norm, exact except for $j=N$, which needs only to be positive
(Mateo-Gabín et al. 2022, §4.1, Properties 1–3, Eqs. 72–78; page-local
$\mathcal V$, $\mathcal P_j$, $Q^{(m)}_j$). A modal filter with
coefficients $\varphi_j$ (page-local) is the nodal matrix
$\mathcal H=\mathcal V\,\mathrm{diag}(\varphi_j)\,\mathcal V^{-1}$ (Eq. 81),
and Parseval gives their Theorem 1,
$$\sum_iw_iQ_i(\mathcal HQ)_i=\sum_j\|\mathcal P_j\|_N^2\,\varphi_j\,(Q^{(m)}_j)^2\ge0\quad\text{for }\varphi_j\ge0,$$
extended to tensor-product hexahedra in Theorem 2 and Property 4 (§4.2). A
tensor-product kernel $\varphi_{ijk}=\varphi_i\varphi_j\varphi_k$ is applied
as three one-dimensional products, which the authors count as $3(N+1)$
operations against $(N+1)^3$ for a general kernel (Eqs. 95–96).

**Filtered artificial viscosity.** Mateo-Gabín et al. (2022, §5) add an
artificial dissipative flux written as a symmetric positive semi-definite
matrix times the gradient $G$ of the entropy variables, and filter it so that
its dissipation stays non-negative by placing the filter between the two
halves of a symmetric factorization. For a scalar coefficient times a
constant matrix, $\mathcal B_a=\mu_a\mathcal C$,
$$F_a^{\mathcal H}=\sqrt{\mu_a/\mathcal J}\;\mathcal C\;\mathcal H\big(\sqrt{\mathcal J\mu_a}\,G\big),$$
and for a general matrix factored as $\mathcal B_a=\mathcal R^{\mathsf T}\mathcal D\mathcal R$
(Cholesky, $\mathcal D$ diagonal and non-negative) the filter acts on
$\sqrt{\mathcal J\mathcal D}\,\mathcal R\,G$ (Eqs. 101–102; page-local
$\mathcal C$, $\mathcal R$, $\mathcal D$, $G$). The filtered flux replaces the
artificial flux in volume and surface terms; with BR1 the volume dissipation
is non-negative by Property 4, the interface and adiabatic-wall terms vanish,
and the semi-discrete scheme is **entropy stable** for the thermodynamic
entropy, or kinetic-energy stable up to the pressure work (Eqs. 109–118; see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).
With a high-pass kernel this is a
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md) of
the explicit modal-filter kind, which the authors present as an entropy-stable
modification of the Smagorinsky–SVV of Manzanero et al. (2020).

**Where the filter acts.** A von Neumann analysis of linear
advection–diffusion with $N=7$, upwind interface flux, BR1 and the kernel
$\varphi_j=(j/N)^{P_{\mathrm{SVV}}}$ (after Moura et al.; $P_{\mathrm{SVV}}$
page-local) shows that the exponent acts mainly at low wavenumbers, where
the SVV supplies almost all the dissipation, whereas at other wavenumbers
the added viscosity is smaller than the dissipation of the Riemann solver
(Mateo-Gabín et al. 2022, §5.2, Figs. 2–3). $P_{\mathrm{SVV}}=0$ recovers the
unfiltered viscous operator.

**Shock capturing by artificial viscosity.** Entropy-conserving split forms
alone are not robust at shocks, because entropy stability presupposes
positive density, which oscillations near shocks can violate (Mateo-Gabín et
al. 2022, §1). Their remedy adds the Guermond–Popov regularization flux
(density diffusion carried consistently into momentum and energy, plus a
viscosity), written in entropy variables with a non-negative Cholesky
diagonal whenever $\rho,p\ge0$ (§2.2.3, App. D), SVV-filtered and switched by
an element-wise density-gradient sensor. On the Chandrashekar split form
with matrix-dissipation Roe interface flux it reproduces the Shu–Osher
problem with 50 to 100 elements at $N=5$ and $N=8$, and captures the main
shock of a Mach 3 forward-facing step within one element on an unstructured
mesh of 3653 quadrilaterals at $N=7$ (§6.2–6.3, Figs. 5–7). They contrast it
with order-lowering approaches such as the
[subcell finite-volume](/methods/subcell-finite-volume-shock-capturing.md)
schemes. The choice of $P_{\mathrm{SVV}}$ has no systematic rule: $O(1)$
suits supersonic flow, about $10^{-2}$ turbulent flow, and the admissible
range is found by trial and error (App. A, Fig. 8).

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
[Kurz et al. (2023)](/sources/kurz-2023.md), §4.2, see the same no-model
LES of forced isotropic turbulence on the KEP split-form DGSEM ($N=5$ and
7, 24 to 48 degrees of freedom per direction) pile up energy at high
wavenumbers, a static Smagorinsky model ($C_s=0.17$) over-dissipate near
the resolution limit, and an element-wise
[reinforcement-learning](/methods/reinforcement-learning-closure.md)
Smagorinsky coefficient match the DNS spectrum.

**The implicit filter of the DGSEM.** Kurz et al. (2023, §1, §3.3) describe
the filter that an under-resolved DG discretization imposes as an
element-local $L_2$ projection onto the polynomial basis, coupled across
elements by the numerical fluxes, so that the whole operator is "a complex
filter with typically non-linear kernel" whose form is unknown; exact
closure terms for such an implicitly filtered LES cannot be computed even
from DNS (see [discretization-consistent closure](/definitions/discretization-consistent-closure.md)).
They find that policies trained at 36 and 48 degrees of freedom per
direction predict different coefficient distributions on either grid and
read this as different discretizations inducing different implicit filters
(§4.4).

**Interface penalties.** Beyond the Riemann-solver dissipation, the
penalty terms on face jumps act as subgrid dissipation.
[Kou et al. (2023)](/sources/kou-2023.md) penalize the solution jump (the
symmetric-interior-penalty viscous flux with an enlarged parameter) or the
gradient jump in HORSES3D with a Roe flux and no over-integration; on the
Taylor–Green vortex at $32^3$ elements and $N=3$ the unpenalized scheme
diverges and both penalties beat Smagorinsky and Vreman models adapted to
DG (§4.2). The method, its eigenanalysis and its parameters are on
[jump-penalty stabilization](/methods/jump-penalty-stabilization.md). Kou et
al.'s one-dimensional analysis is for modal Legendre DG with Gauss–Legendre
quadrature, not the collocated DGSEM (§2.1, App. A).

**SVV-filtered explicit model.** Mateo-Gabín et al. (2022, §6.1, Fig. 4) run
the inviscid [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) on
$8^3$ elements at $N=8$ with the Pirozzoli split form and a low-dissipation
Roe flux, taking the artificial viscosity from a
[Smagorinsky model](/methods/smagorinsky-model.md) with $C_s=0.2$ (the
magnitude of the strain rate is not defined further) and filtering it with
the high-pass SVV kernel above. Unfiltered ($P_{\mathrm{SVV}}=0$) the model
is excessively dissipative; $P_{\mathrm{SVV}}\approx0.1$ gives a spectrum
close to $k^{-5/3}$ over most resolved wavenumbers at $t=20$ and leaves the
highest modes almost unchanged, the SVV acting on low-to-medium
wavenumbers. Their reference for the dissipation rate is the viscous
$Re=1600$ computation of van Rees et al. on $768^3$ points, while their own
test is inviscid; during the first five time units the scheme dissipates
less than the reference, then reaches a comparable level (Fig. 4a).

**Filter width.** A DG element of volume $V_e$ carries $N+1$ nodes per
direction; Beck & Kurz (2023, Eq. 11) set $\Delta=V_e^{1/3}/(N+1)$ and stress
that the choice is not unique (nodes are not equidistant, elements may be
skewed). Mateo-Gabín et al. (2022, Eq. 125) print the same width as
$\Delta^3=V_e/(N+1)^3$, and Basile et al. (2023, §2.2) use
$\Delta=|K|^{1/3}/(N+1)$ as the subgrid length of their DG
[detached-eddy simulation](/methods/detached-eddy-simulation.md) on
tetrahedra, with $|K|$ the element volume, instead of the largest cell
dimension of classical DES. [Lederer et al. (2023)](/sources/lederer-2023.md),
§3.1, use $\Delta=(\Delta x\Delta y\Delta z)^{1/3}/(N+1)$ for the WALE
viscosity of their hybrid mixed method. Flad & Gassner (2017, App. A) print the filter
width as the cell volume divided by $(N+1)^3$ (see Qualifications).

**Resolution per wavelength.** Flad & Gassner (2017, §1, §3) estimate the
resolved wavenumber with 3 points per wavelength (optimistic) and state the
polynomial resolution limit as $\pi$ points per wavelength ($k=15.28$ for $48$
degrees of freedom per direction); Beck & Kurz (2023, §IV A) take 4 points per
wavelength as the resolution limit of the schemes, citing earlier analysis.
The two numbers belong to different criteria and neither source defines a
common error tolerance. Kurz et al. (2023, §3.5) also take about 4 points
per wavelength as the resolution capability of the DGSEM at $N=5$ and 7,
and fit their reward up to $2.6$–$3$ points per wavelength. For linear
acoustic propagation with a DG spectral/hp method at $N=5$,
[Moratilla-Vega et al. (2024)](/sources/moratillavega-2024.md), §3, §4.4,
use the 1% dispersion–diffusion rule of Moura et al. ($|kh|_{1\%}=8.071$,
$h$ the element size) for the highest reliable frequency and quote 5 points
per wavelength for that scheme against 22 for second-order methods; their
second-order finite-volume LES damps high-frequency waves within a few jet
diameters, which the DG acoustic solver then propagates (§4.3–4.4). The
time step follows $\mathrm{CFL}=1/(2N+1)$ (Eq. 12, after Bauer et al.).

## Variants and relatives

The DGSEM coexists with finite-volume subcells in the
[subcell finite-volume shock-capturing](/methods/subcell-finite-volume-shock-capturing.md)
schemes, where a troubled element is solved on $(N+1)^3$ subcells with the same
data structures. Krais et al. (2021, §3.2) handle non-conforming hexahedral
interfaces (2:1 and 4:1) with Kopriva-type mortars: interpolation to the small
sides and $L^2$ projection of their fluxes back to the large side. The flux
reconstruction scheme used with [PANS](/methods/partially-averaged-navier-stokes.md)
by Dzanic et al. (2022) is described there as a generalization of nodal DG.

**Modal DG on simplices and hp-adaptation.** Basile et al. (2023, §2.1) use
the modal DG solver CODA (Airbus, ONERA, DLR) on hybrid prism/tetrahedron
meshes: a hierarchical basis orthonormalized by modified Gram–Schmidt in each
element (so the mass matrix is diagonal and the degree-$N$ basis contains the
degree-$(N-1)$ one), a Roe flux with a Harten-type entropy fix, BR1 viscous
terms, Gauss–Legendre quadrature on hexahedra and Witherden–Vincent rules on
simplices, and a three-stage explicit Runge–Kutta scheme. It is not a DGSEM
(no collocation, no tensor product), but the hierarchical basis gives the
modal content per degree directly, which drives their
[hp-adaptation](/methods/mesh-adaptation.md) for hybrid RANS/LES of a
Mach 0.9 jet: an error estimator summing the energy of the highest modal
level and the inter-element momentum jumps, and a smoothness indicator
$\sigma$ fitted to the decay of modal energy with degree,
$E^{(q)}\simeq Cq^{-\sigma}$, with elements p-enriched when $\sigma>5/3$
(the inertial-range slope) and h-refined otherwise (§3.1–3.2, Eqs. 8–12;
page-local $E^{(q)}$, $q$, $\sigma$). They argue that a DG discretization
has two cut-off wavenumbers, that of the mesh and that of the full
discretization, between which the element spectrum lies (§3.2); that pure
p-adaptation on fixed meshes needs very high degrees, which complicates load
balancing, raises the cost per degree of freedom and risks instabilities
from aliasing or too little numerical dissipation (§1); and, citing earlier
Taylor–Green tests, that high-order DG resolves turbulence better
than low order at equal degrees of freedom (§4.2.1). Their coarse meshes
show spurious peaks of the r.m.s. velocity on the jet axis, which they
attribute to the inter-element discontinuities of DG on coarse elements and
to poor sampling, and which decrease with adaptation (§4.2.3, Fig. 10).

**Interior-penalty DG for RANS.** [Zhao et al. (2023b)](/sources/zhao-2023-b.md)
discretize the compressible RANS mean-flow equations with an interior
penalty DG (IPDG) whose viscous penalty uses a jump-based lifting quantity,
the viscous flux evaluated with the interface jump in place of the gradient,
$L=-F^v(U,[U])$, so that the fourth-order tensor $g$ (page-local), the
Jacobian of the viscous flux with respect to the gradient, never has to be
formed (§3.1, Eqs. 3-1–3-7); the
interface fluxes are local Lax–Friedrichs and the average viscous flux plus
a penalty $C_{\mathrm{IP}}N^2/h_f$ times $L$ (Eq. 3-9; page-local constant
and face scale). The two [$k$-$\omega$ SST](/methods/k-omega-sst-model.md)
equations are solved instead by a first-order cell-centred finite-volume
scheme on the same mesh, piecewise constant per element, "to pursue
numerical stability and positivity", with the DG velocity gradients
$L^2$-projected onto that space (§3.2). Time stepping is implicit BDF2 with
Newton–GMRES, shocks are handled by a flux-divergence artificial viscosity.
Order tests on an isentropic vortex and Couette flow reach roughly the
design order on fine meshes (Tables 4-1, 4-2); the turbulence equations are
first-order accurate by construction. The scheme is not stated to be
collocated or nodal.

**Hybrid mixed methods.** The mass-conserving mixed-stress method of
Lederer et al. (2023, §2.2) is a DG relative for incompressible flow, with
an exactly divergence-free $H(\mathrm{div})$ velocity, hybrid facet
unknowns and a DG upwind convective form; its upwind penalty is the object of
the [high-order projection-based upwind method](/methods/high-order-projection-based-upwind-method.md).

## DGSEM in a turbomachinery code

[Morsbach et al. (2024)](/sources/morsbach-2024.md), §2, run implicit LES of
a low-pressure-turbine cascade with the DGSEM of DLR's TRACE solver:
sixth order ($N=5$) on collocated LGL nodes, curved elements of geometry
degree 4, free-stream preservation by the mapping of Kopriva and Gassner,
the Kennedy–Gruber split form for stability (see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)),
a Roe interface flux, BR1 with a central flux and no penalty, third-order
SSP Runge–Kutta, and no explicit subgrid model; the unresolved scales are
left to the scheme's dispersion and dissipation. Inflow turbulence comes
from a Fourier-mode synthetic generator weakly imposed through a central
flux on inflow faces (see
[inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
Cost (Table 2): $189.4\times10^6$ degrees of freedom ($876\,960$ elements)
on 5120 MPI ranks at 25 852 CPU hours per convective time, time step
$13.65\times10^{-6}$ convective times, 100 convective times averaged; the
coarse mesh ($312\,424$ elements) costs 5861 CPU hours per convective time.
Blade resolution averages $(\Delta x^+,\Delta y^+,\Delta z^+)=(23.1,0.742,15.0)$
in wall units divided by $N$ (§3.1). The fine LES agrees with experiment in
midspan loading, the pressure plateau of the
[laminar separation bubble](/definitions/laminar-separation-bubble.md) and
the secondary-flow loss cores; the coarse mesh is "not entirely
sufficient" downstream of the transition peak (§4.1).

## Implementation choices in HORSES3D

[Ferrer et al. (2023)](/sources/ferrer-2023.md) describe a second DGSEM
framework, [HORSES3D](/software/horses3d.md), with the same weak form on
curvilinear hexahedra (§3.3, Eqs. 4–8) and these options: Gauss nodes,
"more accurate", or Gauss–Lobatto nodes, which allow split forms; convective
interface fluxes from central and Lax–Friedrichs to Roe, low-dissipation
Roe and matrix dissipation; viscous fluxes by BR1, BR2 or symmetric interior
penalty. For [implicit LES](/definitions/implicit-les.md) they list three
sources of dissipation: dissipative Riemann solvers, an interior-penalty
parameter raised above the minimum required for coercivity, and split forms
combined with spectral vanishing viscosity (§4.1). They call DG "very
suitable for ILES" because its dissipation and dispersion errors sit at high
wavenumbers, so that numerical dissipation acts mainly on under-resolved
scales. Flad & Gassner (2017) report the $48^3$ failure of DG implicit LES
described above; Ferrer et al. list both implicit and explicit options
without adjudicating between them. HORSES3D also adapts the polynomial
degree anisotropically, one degree per element and direction, from a
$\tau$-estimate of the truncation error (§3.6; see
[mesh adaptation](/methods/mesh-adaptation.md)).

## Element-local filters, mortars and grid adaptation

**Modal test filter.** A cut-off of the modal coefficients is an
element-local low-pass filter. [Blind et al. (2023)](/sources/blind-2023.md),
§2.3, use it as the test filter of an LES modelling-residual estimator in
[FLEXI](/software/flexi.md): with $N=5$ they zero the coefficients of
degrees 4 and 5 in one direction only (a uni-directional modal cut-off,
equally applicable on unstructured hexahedra), evaluate the residual at the
imagined coarser resolution by changing only the subgrid length scale,
square it exactly by projecting to degree $2N$, and average it over each
element, because without averaging the estimator flags element boundaries
as high-error regions, an artefact of the discontinuous solution. They state
that the method transfers to any DG-type scheme "as long as an element-local
filter operation can be specified" (§2.1). The adaptation it drives is on
[mesh adaptation](/methods/mesh-adaptation.md).

**Filter width under the test filter.** With $\Delta=V_e^{1/3}/(N+1)$ as
above and a test filter keeping modes up to degree $N_f=3$ (page-local), Blind
et al. take the test-level length
$\hat\Delta=\big[(N+1)/(N_f+1)\big]^{1/3}\Delta$ for the isotropic Vreman
length scale (§2.3).

**Non-conforming mortars.** FLEXI's mortars are limited to 2-to-1
interfaces, a halving of the element size across a face (Blind et al. 2023,
§3.2), which covers the 2:1 and 4:1 face types of Krais et al. (2021, §3.2)
above, both cut at the middle of the big face; Blind et al. keep the smallest required spacing
from the wall until the optimal spacing has at least doubled, then insert a
2-to-1 interface, which saves up to about half of the elements of a
structured mesh with the same near-wall spacing in a channel at
$Re_\tau=2000$; the time step is unchanged, set by the smallest element, so
the saving is in processors. Ferrer et al. (2023, §3.6) couple faces of
different polynomial degree by mortars, at the price of entropy stability.

**Continuous spectral elements.** The continuous Galerkin spectral element
method of [Nek5000 and NekRS](/software/nek5000.md) uses the same GLL
tensor-product bases but enforces $C^0$ continuity by a gather–scatter
operation, so the velocity is continuous across faces and its gradient is
not (Fischer et al. 2022, §2.3; Gillyns et al. 2022, §2). Gillyns et al.
(2022, §2, §6) observe Gibbs spikes of the fluctuation statistics at element
faces on coarse meshes, which vanish near DNS resolution.
[Nektar++](/software/nektar-plus-plus.md) offers the continuous form too:
[Saini et al. (2023)](/sources/saini-2023.md), §2.1, run its incompressible
continuous-Galerkin spectral/hp solver at order 4 (velocity) and 3
(pressure) with spectral vanishing viscosity and find its numerical plus
model dissipation about a quarter of that of a second-order finite-volume
LES at similar cost ("around 1/4th", §6; see [numerical dissipation](/properties/numerical-dissipation.md));
[Slaughter et al. (2023)](/sources/slaughter-2023.md), §3.1, combine
spectral/hp elements in the plane with Fourier modes in the span,
stabilized by gradient-jump penalisation and SVV.

## Qualifications

- **Test-level eddy viscosity.** Blind et al. (2023, §2.3) state that the
  test-level eddy viscosity is "a factor of $[(P+1)/(N_f+1)]^{2/3}\approx1.59$
  larger" ($P$ their degree); with $N=5$ and $N_f=3$ the expression is
  $1.5^{2/3}\approx1.31$ *(compiler check, not in the sources)*. The version
  read is the arXiv v1 preprint, retitled at publication.
- **Weak-form differentiation matrix.** Krais et al. (2021, Eq. 31) print
  $\hat D_{ij}=-\frac{w_i}{w_j}D_{ji}$. Dividing the weak-form volume term
  $\sum_m w_m D_{mi}\mathcal F_m$ by the mass $w_i$ gives
  $\hat D_{ij}=-\frac{w_j}{w_i}D_{ji}$, consistent with their own
  $\ell_i/w_i$ for the surface term *(compiler check, not in the sources)*.
- **Filter width.** Flad & Gassner (2017, App. A) define $\Delta$ as "the local
  cell volume divided be $(N+1)^3$", which is a volume, not a length; the cube
  root of that ratio, which coincides with Beck & Kurz's (2023)
  $V_e^{1/3}/(N+1)$, is the dimensionally consistent reading *(compiler check,
  not in the sources)*. Mateo-Gabín et al. (2022, Eq. 125) print exactly this
  reading, $\Delta^3=V_e/(N+1)^3$.
- Mateo-Gabín et al. (2022) print the Smagorinsky viscosity as
  $\mu_a=C_s^2\Delta^2|S|$ with no density factor (Eq. 125); they print the switching rule of the
  forward-facing step with the one-dimensional sensor $s_1$ although they
  define the two-dimensional sensor $s_2$ for it (§6.3); and they call the
  first five non-dimensional time units of the Taylor–Green vortex "the first
  five seconds" (§6.1). The version read is the arXiv v3 preprint.
- Basile et al. (2023, Eq. 18) print the degree update of p-enriched
  elements as $\max(N_K+1,N_{\max})$; with their marking condition
  $N_K+1\le N_{\max}$ (Eqs. 15–16) this always returns $N_{\max}$ and
  leaves the argument $N_K+1$ without effect, whereas
  $\min(N_K+1,N_{\max})$ would raise the degree by one step
  *(compiler check, not in the sources)*. The version read is the HAL
  author manuscript.
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
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §1; §2.2–2.3 (entropy-stable artificial fluxes, Guermond–Popov); §3, Eqs. (39)–(61) (LGL DGSEM, SBP, split form, BR1, walls); §4, Eqs. (72)–(100) (modal filtering, Parseval, Theorems 1–2); §5, Eqs. (101)–(122) (filtered artificial viscosity, entropy stability, von Neumann analysis); §6, Eqs. (123)–(128), Figs. 4–7 (TGV, Shu–Osher, forward-facing step); App. A.
- [Basile et al. (2023)](/sources/basile-2023.md) — §1; §2.1–2.2 (modal DG in CODA, DG length scale); §3.1–3.2, Eqs. (8)–(12) (error and smoothness indicators); §4.2.1, §4.2.3 (degree-of-freedom distribution, interface peaks).
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §3.3, Eqs. (4)–(8) (HORSES3D weak form, nodes, fluxes); §3.6 (anisotropic $p$-adaptation, mortars); §4.1 (implicit-LES options).
- [Blind et al. (2023)](/sources/blind-2023.md) — §2.1 (transfer to DG); §2.3 (modal test filter, length scales, element averaging); §3.2, Tables 2–3 (2-to-1 mortars, savings).
- [Fischer et al. (2022)](/sources/fischer-2022.md) — §2.3 (continuous spectral elements, gather–scatter).
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §2, §6 ($C^0$ continuity, Gibbs spikes).
- [Kurz et al. (2023)](/sources/kurz-2023.md) — arXiv v2: §1, §3.3 (implicit DG filter); §3.5 (resolution capability); §4.2, §4.4 (no-model pile-up, resolution-dependent policies).
- [Kou et al. (2023)](/sources/kou-2023.md) — §2.1–2.2, App. A (modal DG, HORSES3D with Roe and SIP, no over-integration); §4.2 (Taylor–Green vortex).
- [Lederer et al. (2023)](/sources/lederer-2023.md) — arXiv v1: §2.2 (mixed-stress DG relative); §3.1 (filter width).
- [Moratilla-Vega et al. (2024)](/sources/moratillavega-2024.md) — §2.2, Eqs. (11)–(13) (DG acoustic solver, CFL, 1% rule); §3; §4.3–4.4 (points per wavelength, dissipation of the LES).
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §2 (TRACE DGSEM); §3.1, Table 2 (resolution, cost); §4.1.
- [Saini et al. (2023)](/sources/saini-2023.md) — §2.1, Table 1 (Nektar++ continuous Galerkin); §5–6.
- [Slaughter et al. (2023)](/sources/slaughter-2023.md) — Research Square preprint v1: §3.1 (Fourier spectral/hp, GJP, SVV).
- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §3.1, Eqs. (3-1)–(3-10) (improved IPDG, fluxes, artificial viscosity); §3.2 (finite-volume SST equations, BDF2); §4, Tables 4-1–4-2.

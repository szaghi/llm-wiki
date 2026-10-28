---
type: Method
title: "Discontinuous Galerkin spectral element method"
description: "The DGSEM is a collocated nodal discontinuous Galerkin scheme on tensor-product hexahedra; this page states its forms, SBP property, de-aliasing, modal filtering, cost and GPU implementation, how dissipation and penalties shape LES on it, and its modal, hybridized, mixed and continuous relatives in shock–turbulence, RANS, time-integration and error-estimation work."
status: established
aliases: [DGSEM, DG-SEM, modal DG, nodal discontinuous Galerkin, collocation DG, DG spectral element method, hybridizable discontinuous Galerkin, HDG]
tags: [dg, numerical-dissipation, kinetic-energy-preserving, entropy-stable, les, dns, flux-reconstruction]
timestamp: 2026-10-28T16:59:00Z
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
with the same DGSEM. In the BR1 scheme of Bassi & Rebay, as Krais et al.
(2021, Eqs. 34–42) cite and use it, both the lifted solution and the viscous flux at an
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
  (Flad & Gassner 2017, §2.1, Eq. 11). Flad & Gassner state that the rational
  flux of the compressible equations cannot be projected exactly, so the rule
  assumes weak compressibility. Without it, the $N=7$ DG implicit LES of decaying
  isotropic turbulence was unstable (§1, stated without figure).
- **Split form (flux differencing)** on LGL nodes, which builds the
  de-aliasing into the volume term. Flad & Gassner (2017, §6.1) state that it
  costs at least three times less than polynomial de-aliasing in their
  in-house code (no timing given).

**Measured comparison in a flux-reconstruction code.**
[Brillon & Nadarajah (2026)](/sources/brillon-2026.md) compare the
split-form, entropy-stable nonlinearly stable flux reconstruction
(described on [flux reconstruction](/methods/flux-reconstruction.md);
its collocated LGL variant is "also known as DG-SEM", §3.1.4) with
strong-form DG with a Roe flux and over-integration on $2(N+1)$
quadrature points per direction, the number they state is needed to
integrate the cubic non-linearity of the viscous flux exactly (§2.10,
§3.1.4). On the viscous Taylor–Green vortex:

- strong DG without over-integration at $N=7$ on $64^3$ degrees of
  freedom fails in the transition near $t^*=6$: "a linearly stable scheme
  can be unstable in the absence of over-integration" (§3.1.3, Fig. 11);
- per Runge–Kutta step on $4^3$ elements, over-integrated strong DG costs
  about twice the CPU time of the split form for $N\in[5,12]$, with sum
  factorization in both (§3.1.3, Fig. 12);
- GL nodes integrate exactly to degree $2N+1$ and LGL to $2N-1$, as above;
  at $N=5$ the collocated LGL split form departs from the expected
  dissipation rate near $t^*\approx5$, while the uncollocated split form
  on GL flux nodes, made entropy stable by evaluating the two-point fluxes
  on entropy-projected variables, does not; with three extra quadrature
  points both agree, "with sufficient integration accuracy, the solution
  is independent of the choice of flux nodes" (§3.1.4, Fig. 13);
- a collocated strong-form scheme without de-aliasing is stabilized by an
  added high-pass-filtered Smagorinsky model, but "a stable scheme without
  any de-aliasing can lead to inaccuracies" (§3.1.8, Fig. 20).

The factor of three of Flad & Gassner and the factor of two of Brillon &
Nadarajah come from different codes and different over-integration rules
($\lfloor\tfrac32(N+1)\rfloor$ against $2(N+1)$ points); they are recorded
side by side, not as a contradiction.

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

**Indicator-switched modal filter.** The modal filter can also be applied
to the solution itself, element by element. Wang (2024, §2.3, Eqs. 17–19)
applies the exponential filter $\mathcal V\Lambda\mathcal V^{-1}$ of
Hesthaven and Warburton after every Runge–Kutta stage, but only in elements
whose Persson–Peraire smoothness indicator of the density exceeds a
threshold, and compares it with the entropy filter of Dzanic and
Witherden, which chooses the filter strength per element to enforce a
discrete minimum entropy principle and positivity; on the Taylor–Green
vortex the switched filter leaves the solution unchanged at a 5.5% cost,
and the entropy filter costs about 15% more per iteration than the switched
filter on the LS89 vane (§4.1, §4.4.3). Formulas, thresholds and results are
on [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md).

**A filter whose strength does not depend on the time step.**
[Hamedi & Vermeire (2022)](/sources/hamedi-2022.md) apply the nodal filter
$\mathcal V\Lambda\mathcal V^{-1}$ in a flux-reconstruction scheme whose
Radau correction functions recover collocation-based nodal DG (Gauss
solution points, Rusanov interface flux, BR2), the scheme run throughout
(§2.1). Because a fixed filter applied after every step has a cumulative
strength over a fixed time that grows as the step shrinks, they apply after
every step the root $\Lambda^{1/n}$, $n=T_{\mathrm{char}}/\Delta t$
($T_{\mathrm{char}}$ a characteristic time, page-local), which by
construction has after $n$ steps the effect of one application of
$\Lambda$ per $T_{\mathrm{char}}$ (§3.2, Eqs. 28–30), valid, they state,
with a high-order time integrator away from its stability limit. The
exponential filter function acts on the total degree of each orthonormal
mode and has cut-off, damping and order parameters optimized for
$N=3$–5 on more than 14,000 inviscid Taylor–Green runs at $16^3$ degrees
of freedom; the filter stabilizes a channel at $Re_\tau=395$ that is
unstable unfiltered at $N=5$, with mean velocity and Reynolds stresses in
agreement with DNS, and leaves the forces and pressure of a stalled
NACA 0020 nearly unchanged (§3.3–5.2). The
parameters and results are on
[explicit modal filtering](/methods/explicit-modal-filtering.md); the
authors state that the filters are tied to the DG-recovering correction
function and the Rusanov flux (§2.1, §3.4).

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
viscosity of their hybrid mixed method.
[Alberti et al. (2025)](/sources/alberti-2025-b.md), §2.3, divide every
subgrid length scale of their DG [detached-eddy simulation](/methods/detached-eddy-simulation.md)
by a normalization $s_\Delta$ (page-local), testing $N+1$, $N$ and
$N_{\mathrm{dof}}^{1/3}$, where $N_{\mathrm{dof}}=(N+1)(N+2)(N+3)/6$ is the
number of modes of their complete (Pascal) basis in three dimensions; the
two degree-based options per $N_{\mathrm{dof}}^{1/3}$ tend to 1.82 as
$N\to\infty$ (Table 1). They find $s_\Delta=N+1$ best across all degrees
tested in channels at $Re_\tau=400$ and 5200, while $N_{\mathrm{dof}}^{1/3}$,
and $N$ at low to moderate degree, move the solution too fast towards RANS
(§3.1.3, §4). For non-Cartesian hexahedra they take the grid lengths from
an "equivalent hexahedron" with the element's principal moments of
inertia, rescaled to the element volume, exact on Cartesian cells (§2.3,
Eq. 23). Flad & Gassner (2017, App. A) print the filter
width as the cell volume divided by $(N+1)^3$ (see Qualifications).
[Duan & Wang (2024)](/sources/duan-2024.md), §3, Eqs. (28)–(30), test the
same width ("d3") against $V_e^{1/3}$ and an intermediate
$V_e^{1/3}/\sqrt{N+1}$ in FR/CPR wall-modelled LES with element-averaged
eddy viscosity, and recommend the intermediate width with the Vreman model,
arguing that the subgrid models were calibrated on second-order schemes and
that $V_e^{1/3}/(N+1)$ under-dissipates on high-order ones (§5.4, §6; see
[flux reconstruction](/methods/flux-reconstruction.md)).

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

**Flux reconstruction recovering nodal DG.** The
[flux-reconstruction](/methods/flux-reconstruction.md) solver ATHOS of
[Wang (2024)](/sources/wang-2024-b.md), §2.2, §3, Fig. 1, places solution
and flux points on LGL nodes of tensor-product quadrilaterals and hexahedra
and chooses the correction functions "in such a way that the nodal
discontinuous Galerkin approach is recovered", with LDG viscous fluxes
(zero solution-jump penalty) and Rusanov, Roe or HLLC interface fluxes. Its implicit LES of turbine cascades, the robustness ranking of
the Riemann solvers and the indicator-switched filters are on the
flux-reconstruction page and on
[subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md).
[Liu & Yuan (2023)](/sources/liu-2023-b.md), §2.2, choose the VCJH
correction-function parameter that recovers collocation nodal DG, with
Gauss–Legendre solution points (to limit aliasing, citing Witherden &
Vincent), as the base of their a posteriori subcell limiter for
one-dimensional detonations.
[Vermeire (2024)](/sources/vermeire-2024.md), §3, Eqs. (6)–(13), use the
FRDG variant in lifting-collocation-penalty form on Gauss solution points,
whose lifting coefficients recover DG for linear equations, for implicit
LES of incompressible flow with entropically damped artificial
compressibility (scheme and results on
[flux reconstruction](/methods/flux-reconstruction.md) and
[implicit LES](/definitions/implicit-les.md)); one of the references of
their [SD7003 airfoil](/benchmarks/sd7003-airfoil.md) runs is a DG
computation at $N=7$ by Beck et al. that they cite (§4.3).

**Fully-discrete spatial eigenanalysis of FR-DG.**
[Tonicello et al. (2023)](/sources/tonicello-2023.md), §3, Fig. 7,
App. Figs. 29–30, analyse the DG recovery of flux reconstruction (FR-DG)
beside the spectral-difference recovery (FR-SD) for 1D linear advection
with explicit Runge–Kutta time integration: with upwind fluxes FR-DG has
the more restrictive CFL limit, so its dissipation curves extend to
higher frequencies, and it is spatially less dissipative than FR-SD
overall. The method and its findings are on
[eigensolution analysis](/methods/eigensolution-analysis.md).

**DG in the first High-Order CFD Workshop.** The workshop summary of
[Wang et al. (2013)](/sources/wang-2013.md) compares DG submissions (BR2,
interior penalty, the DGSEM with five-stage Runge–Kutta, CPR, reconstructed
DG) with finite-volume and finite-difference codes by error against cost,
measured in TauBench work units; the authors caution that the cost of
one case on different computers differed by as much as 30%, so that
differences below 30% decide nothing (§3.2, §6). For smooth problems the
high-order methods beat the second-order finite-volume TAU code in error
against cost (bump and NACA 0012 cases; §5.1–5.2, §6); two BR2 DG
codes on the laminar delta wing are "almost identical" in error against
degrees of freedom, "a perfect cross-code verification", yet differ greatly
in work units because of their solvers (§5.5). On the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $Re=1600$ the
DG-like schemes reach their order for two of the three error measures,
unlike the finite-difference and finite-volume codes, and Beck's DGSEM
order study at constant equivalent resolution converges spectrally at
constant cost, a result the authors restrict to explicit time integration;
the near-equality of twelfth-order central and fourth-order
dispersion-relation-preserving finite differences "seems to indicate" that
dispersion error dominates, consistent with DG being "dissipative but
[having] particularly good dispersive accuracy" (§5.6). For RANS
(RAE 2822 with SA, EARSM or Wilcox $k$-$\omega$, three DG groups) uniform
refinement brought "virtually no improvement from high order" and a large
spread among groups, while adaptive mesh optimization was "markedly
superior" (§5.4; see
[RAE 2822](/benchmarks/rae-2822-airfoil.md)); the authors find high-order
RANS less robust than low-order RANS in reaching a steady state, believe
this "related to nonsmoothness introduced in the turbulence models" and
call for "smooth turbulence models", and note that line-implicit solvers
for stiff near-wall meshes need memory scaling as $N^6$ (§6, the source's
$p^6$).

**A log-law basis in the wall-adjacent DG cell.** The SUPES solver used by
[Lv et al. (2021)](/sources/lv-2021.md), §III, is a DG scheme on arbitrary
elements that they extend with a piecewise-parabolic finite-volume method:
only the wall-adjacent cells use the DG variational form, with a local
Lax–Friedrichs flux, symmetric interior-penalty viscous traces, a strongly
imposed wall state, the Vreman model and explicit third-order Runge–Kutta.
In those cells one monomial of the wall-normal basis of their third-order
(P3) scheme is replaced by the law of the wall,
$\{1,\,y,\,\kappa^{-1}\ln((y+y_0)/y_0)\}$ ($y_0$ a viscous or roughness
length, page-local), so that the DG solver itself computes the coefficient
of the log term and the wall shear stress follows from the coefficients,
$\tau_w/\rho=a_w^2+\nu a_1$ ($a_w$, $a_1$ the coefficients of the log and
linear terms, page-local; §II A, Eqs. 3–6, §II C). They distinguish it from
earlier DG wall modelling that computed the wall flux from the log law
outside the polynomial (Frere et al.) or added the log function as an extra
basis solved outside the LES (their earlier work; §II B 2); the wall-model content is on
[non-equilibrium wall models](/methods/nonequilibrium-wall-model.md) and
[wall-modelled LES](/methods/wall-modelled-les.md). Citing earlier work,
they state that SUPES can reach a tenfold speed-up over a finite-volume solver on unstructured
meshes but "remains more costly on structured curvilinear meshes" (§III).

**Modal and reconstructed DG for multi-material flow.** The review of
diffuse-interface methods of [Maltsev et al. (2022)](/sources/maltsev-2022.md),
§III B–C, §V, mentions modal DG with a Taylor basis and the $P_NP_M$
reconstructed DG of Dumbser et al. (finite volumes at $N=0$, DG at $M=N$)
for multi-material flow, without turbulence, and concludes that DG for
diffuse-interface models is used mostly with reduced five-equation models
on structured meshes.

**DG, its hybridized forms and DG combustion LES in a multiphase review.**
[Lv & Ekaterinaris (2023)](/sources/lv-2023.md), §3.1, Eq. (20), write
the one-dimensional DG weak form on a reference element, with a Riemann
flux at the element ends, and state that any basis with a well-conditioned
mass matrix is admissible, nodal or modal; equally spaced nodes with
Lagrange polynomials become unsuitable at very high order because the
condition number of the mass matrix deteriorates, which well-chosen nodes
avoid (citing Karniadakis & Sherwin and Hesthaven & Warburton). They list
the viscous discretizations (interior penalty, Bassi–Rebay, LDG, compact,
recovery, reconstructed and direct DG). Hybridized and embedded DG
(§3.4, Eq. 28) add a face unknown $\hat U$ (page-local) with the
one-sided flux $\hat F(\hat U,U_f)=F(\hat U)+|\partial F/\partial U(\hat U)|_{\max}(\hat U-U_f)$;
only the face unknowns are globally coupled, which lowers memory and cost
for steady problems and implicit time integration, and the embedded form
also enforces continuity at each face node, reducing the global unknowns
further. Two DG combustion LES of the first author's group are reviewed
(§6.3, Figs. 14–16): the Volvo bluff-body premixed flame at $N=3$ on
10,000 hexahedra (64 degrees of freedom per element) with a
[thickened flame model](/methods/thickened-flame-model.md), where "the
reaction zone is captured by only one or two elements" against "more than
ten cells" for second-order schemes (stated, not run side by side), and a
piloted dimethyl-ether jet flame at $N=2$ on 12,000 elements with a
[flamelet/progress-variable model](/methods/flamelet-tabulated-chemistry.md),
in "excellent agreement" with the measurements except near the nozzle.
Their conclusion is that stabilization techniques struggle to generalize
to high degree, unstructured meshes and three dimensions (§7; shock
capturing on [artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
and [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)).

**Residual-stabilized continuous Galerkin.** At the low-order end of the
continuous family, [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md)
run implicit LES of the [periodic hill](/benchmarks/periodic-hill.md) with
SUPG/PSPG-stabilized trilinear ($Q_1$) continuous finite elements in Lethe,
the stabilization term supplying the dissipation (§1, §3.1; see
[jump-penalty stabilization](/methods/jump-penalty-stabilization.md) for
the formulation and its time-step dependence). Their literature table
(Table 1, $Re_h=5600$) lists the high-order DG under-resolved DNS of Krank
et al. ($N=6$, 65K cells, 22.5M degrees of freedom, reattachment
$x_R/h=4.82\pm0.09$) next to Krank et al.'s $N=7$ DNS ($x_R/h=5.04\pm0.09$),
as tabulated by Prieto Saavedra et al., against their own $Q_1$ runs with
0.5M to 16M degrees of freedom.

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

**Modal DG for incompressible hybrid RANS/LES.** Alberti et al. (2025, §2.2,
Eqs. 19–22) run Spalart–Allmaras-based DDES and IDDES in an incompressible
modal DG with an orthonormal hierarchical basis of complete polynomials
defined in physical space, a Godunov-type exact Riemann flux with
artificial compressibility, BR2 viscous fluxes, order $N+1$ for velocity
and $\tilde\nu$ and $N$ for pressure, and the three-stage linearly implicit
Rosenbrock scheme ROS3Pw with flexible GMRES and an additive-Schwarz
preconditioner. The SA source uses only the positive part of $\tilde\nu$
and limits $r$ to 10 (§2.1, Eq. 6). On fine grids they find that the
eddy viscosity of the LES branch falls to an equivalent Smagorinsky
constant of about 0.01, "ILES-like", and that high-order DG then behaves
"more like a wall-modeled ILES rather than a simple WMLES" (§3.1.3, §4).
At roughly equal degrees of freedom in the $Re_\tau=400$ channel, $N=6$ on
$8^3$ elements beats $N=2$ on $16^3$ elements, which approaches it only at
$N=4$ "despite having more than three times as many DOFs" (§3.1.3, Table 4,
Fig. 14); in the $Re_\tau=5200$ channel, raising $N$ on a fixed mesh moves
the RANS/LES interface towards the wall and improves the centreline
velocity (Fig. 13). They attribute the failure of the IDDES length
$\Delta_{dw}$ (the source's $\Delta_{hwn}$; see the DES page) in DG to the higher wall-normal growth rates that DG
meshes need, which make it progress in a "staircase" (§3.1.2, Fig. 12).
Results by model variant are on
[detached-eddy simulation](/methods/detached-eddy-simulation.md) and
[log-layer mismatch](/definitions/log-layer-mismatch.md).

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
[Lederer et al. (2026)](/sources/lederer-2026.md), §2.3, replace its IMEX
time integration by a Chorin-type projection: a statically condensed
Stokes-like step solved with an element-wise BDDC preconditioner, then a
hybridized mixed Poisson projection solved with algebraic multigrid; they
call exact quadrature of all bilinear forms "crucial for maintaining the
stability of the method" (§2.2). Details are on the HOPU page.

**Hybridizable DG for steady RANS.**
[Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md), §2–4, solve
the steady incompressible RANS equations with $k$-$\omega$ closures (see
[Wilcox $k$-$\omega$ model](/methods/k-omega-model.md)) by a hybridizable
DG (HDG) method: element unknowns (velocity of degree $N$, a reduced
pressure space, the symmetric velocity gradient as auxiliary unknown) are
eliminated by static condensation, leaving a global system in the facet
traces of velocity and pressure (Eqs. 72–75); the velocity is exactly
divergence free and $H(\mathrm{div})$-conforming, and the method energy
stable, as the authors state citing their earlier work. The convective trace
is upwinded, and the diffusive trace carries the stabilization
$\tau_{\mathrm{HDG}}=Re/\ell$ (page-local; the source's $\tau$) with a problem-dependent length $\ell$; manufactured
solutions give the smallest error near $\ell\approx10^2$ at $Re=10^5$,
$10^7$ and $10^9$, with optimal rates (about $N+1$ for velocity and $N$
for pressure at $N=3$) (§2.1, §5.1, Table 1, Figs. 4–6; see
[method of manufactured solutions](/methods/method-of-manufactured-solutions.md)).
The wall shear computed from the auxiliary gradient unknown (degree $N$)
converges at order $N+1$, one order above the shear from the gradient of
the velocity polynomial (degree $N-1$) (§5.2.1, Table 3, Fig. 15). Their
list of obstacles to high-order RANS, stiffness, positivity of $k$ and
$\omega$, the singular wall value of $\omega$, and min/max switches that
put discontinuities inside elements, and their remedies (interpolating
$1/\omega$, removing wall-touching elements from the $\omega$ problem, a
mean-preserving scaling limiter on $k$ and $1/\omega$, segregated
fixed-point coupling) concern the turbulence model (see the
$k$-$\omega$ page). At equal degrees of
freedom the fourth-order HDG has a much smaller numerical error than a
second-order finite-volume code on a flat plate at $Re=10^7$ (§6,
Figs. 37–45).

## Modal DG for steady RANS: wall functions, adaptation, error estimation

**Wall functions on high-order DG.** [Ghidoni et al. (2026)](/sources/ghidoni-2026.md),
§2, discretize the compressible RANS equations with the Wilcox
$k$-$\log\omega$ model by a modal DG with an orthogonal hierarchical basis
defined in physical space ($(N+1)(N+2)(N+3)/6$ functions per element,
degrees up to $N=6$), primitive variables, exact local Riemann problems
for the inviscid flux, a BR2-type viscous flux, and linearized backward
Euler with pseudo-transient continuation, GMRES and block Jacobi (PETSc).
They state that a wall-resolved DG solution needs a first element of height
$y^+\sim10$, against $\sim1$ for finite volumes, with $y^+$ measured on the
element height (§1); the wall value of $\omega$ in the wall-resolved runs
is set from an effective distance that shrinks with the degree,
$r_Ny_1$ with $r_N=\exp(-\sum_{n=1}^N1/n)$ and $y_1$ the
first-element height (Eq. 4; page-local symbols, the source's $\alpha^l$,
renamed because $\alpha$ is the registry's DG/FV blending factor). Their explicit wall
function takes its input at the interior quadrature point of the wall
element closest to the opposite face, a choice borrowed from
[wall-modelled LES](/methods/wall-modelled-les.md), so that all work stays
element-local; it is described, with its errors and time savings, on
[wall functions for RANS](/methods/rans-wall-function.md).

**Modal DG in CODA for anisotropic adaptation.**
[Schotte et al. (2026)](/sources/schotte-2026.md), §2.2, §4.1, run steady
RANS with the negative Spalart–Allmaras model in the modal DG of CODA
(the hierarchical orthonormal basis described above for Basile et al.):
Roe flux with a Harten-type entropy fix for transonic cases or a
Liu–Vinokur fix for subsonic ones, BR2 with stabilization parameter 3 on
triangles and 4 on tetrahedra, a Laplacian artificial viscosity driven by
the Persson–Peraire sensor with the calibration of Glaubitz et al. at
shocks, a positivity-preserving limiter, implicit backward Euler with
GMRES, and degree staging ($N=0$, then 1, 2, …). They state that the
compact DG stencil allows exact residual Jacobians, unlike finite-volume
schemes on skewed tetrahedra (§1), and call degrees $N=2$ and 3 "a sweet
spot for modal DG applied to complex configurations" (§3). Two pieces
of their metric-based adaptation are DG-specific (§3, Eqs. 15–25): the
element Hessian of the Mach number is computed from a DG weak form, a face
integral of the averaged lifted (BR1) gradients projected onto constants,
and the element size comes from spectral error estimators built on the
energy of the degree-$N$ modes of the momentum. The adaptation strategy
and results: see [mesh adaptation](/methods/mesh-adaptation.md).

**Discretization-error transport.** [Wang & Roy (2023)](/sources/wang-2023.md)
estimate the discretization error of a modal DG solution of the steady
two-dimensional Euler equations (tensor-product Legendre basis,
Gauss–Legendre quadrature, backward-Euler pseudo-time marching; §2.1) by
error transport equations: subtracting the DG weak form evaluated at the
projected exact solution from the discrete equations gives a nonlinear
equation for the error whose source is the negative truncation error
(Eq. 12), and its linearization about the discrete solution reuses the
Jacobian of the implicit solver (Eq. 13). With the truncation error
estimated from a reconstruction of degree $r-1$, the corrected solution
reaches order $r$ on smooth problems once an iterative correction is
applied; on problems with singularities the estimate barely improves on
the uncorrected error, which the authors trace to the truncation-error
estimate (§4–5); see
[mesh adaptation](/methods/mesh-adaptation.md) and
[method of manufactured solutions](/methods/method-of-manufactured-solutions.md).
Wang & Roy write the order of accuracy as $p$, so their degree is $N=p-1$.

**Output-based adaptation of DG for time-averaged turbulent outputs.**
[Fidkowski (2022)](/sources/fidkowski-2022.md) adapts a DG discretization
(Roe convective flux, BR2 viscous flux, curved cubic triangles, element
degrees up to 5, default $N=2$, third-order modified extended BDF in time;
§2.2) of unsteady two-dimensional airfoil flows (NACA 0012 at $Re=10^4$ and
$2\times10^4$, $M=0.2$, $7^\circ$; a high-lift airfoil at $Re=10^6$ with a
simplified DES) for the error of the time-averaged lift, without an
unsteady adjoint, which is unstable in all three cases (Figs. 4, 11, 17).
A steady Spalart–Allmaras RANS model with a production multiplier trained by
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)
to reproduce the time-averaged state supplies a steady adjoint; restricted
to the Navier–Stokes components it serves as a surrogate of the
time-averaged unsteady adjoint, and weights the residual of the
time-averaged solution in the enriched space of degree $N+1$ (estimate E1)
or the residual of the augmented steady system (E2) (§2.2, §4, Eqs. 7,
19–23). Element indicators $|\delta\Psi_e^{\mathsf T}\delta R_e|$ (adjoint and
residual perturbations of element $e$, page-local) drive fixed-fraction
degree refinement or anisotropic metric optimization (MOESS) with 2 to 4
unsteady runs per adapted mesh and no state storage (§5). The estimates
are within about a factor of 2 in later adaptive iterations, and
adaptation with uncorrected RANS converges to a wrong lift (Tables 1–3,
§6); the adaptation results are on
[mesh adaptation](/methods/mesh-adaptation.md).

## Linearly implicit time integration of DG URANS

[Ghidoni et al. (2022)](/sources/ghidoni-2022.md) assess adaptive time-step
control for linearly implicit high-order time integration of unsteady RANS
with the Wilcox $k$-$\omega$ model in log form ($\tilde\omega_\ell=\ln\omega$,
registry §11; $k$ limited at zero, $\tilde\omega_\ell$ subject to
realizability conditions; constants not printed), discretized by the
authors' modal DG: orthonormal hierarchical basis built by modified
Gram–Schmidt in a physical-space frame aligned with the element's principal
axes of inertia, BR2 viscous flux, Godunov flux with an exact Riemann
solver, and for incompressible flow an exact Riemann solver of a locally
artificial-compressibility-perturbed Euler system used only in the flux
(§2–3). The semi-discrete system is an ODE for compressible flow and a DAE
for incompressible flow (zero rows for the pressure). They state that the
turbulence model adds the stiffness that motivates the study (§1).

**Schemes.** One-step Rosenbrock (linearly implicit Runge–Kutta) schemes
solve one linear system per stage with the Jacobian assembled once per
step: ROS3PL (order 3, 4 stages, embedded order 2), RODASP (order 4, 6
stages, embedded 3), ROD5\_1 (order 5, 8 stages, embedded 4). Two-step
linearly implicit peer schemes peer3, peer4, peer5 (orders 3–5, $s$ = 3–5
stages, embedded $s-2$) carry $s$ stages of equal order, give continuous
output, tolerate an approximate or frozen Jacobian and are not
self-starting; the authors start them with their earlier procedure, which
chooses the starter's step from the asymptotic local and global error
orders (Eqs. 41–50). All schemes are A- and L-stable (Table 1, §4.1–4.2).
Freezing the peer Jacobian saves cost up to a refresh interval of 10
(peer3) or 5 (peer4, peer5) steps, at most about 24% for peer5 (§4.2,
Fig. 3). The design orders are verified on laminar travelling waves
(incompressible) and an isentropic vortex (compressible) at $N=6$ (Tables
2–3, 5–6).

**Near-stability zone and step control.** Although linearly A- and
L-stable, a linearly implicit scheme applied to the nonlinear system has a
step-size limit set by the accuracy of its per-step linearization, which the
authors call the **near-stability zone** (§4). The local error estimate
must include every variable, $k$ and $\tilde\omega_\ell$ among them, in an
$L^2$ norm, $r=\big(\sum_jr_j^2\big)^{1/2}$ with $r_j$ the norm of the
difference between the solution and its embedded companion for variable $j$
(Eq. 67; page-local $r$, $r_j$): the turbulence variables, irregular and
the main cause of instability, would be under-weighted by a domain average,
and using them alone would give too small steps (§5). Controllers (the
tolerance $\mathrm{TOL}$ and estimator order $q_r$ page-local): standard
$\Delta t^{n+1}=\Delta t^n(\mathrm{TOL}/r^{n+1})^{1/q_r}$ (Eq. 63); PI 4.2;
and Söderlind's digital filters H211b,
$$\Delta t^{n+1}=\Delta t^n\Big(\frac{\Delta t^n}{\Delta t^{n-1}}\Big)^{-1/4}\Big(\frac{\mathrm{TOL}}{r^{n+1}}\Big)^{1/(4q_r)}\Big(\frac{\mathrm{TOL}}{r^n}\Big)^{1/(4q_r)},$$
and H312b (Eqs. 64–66), optionally with a smooth arctan limiter
$\Delta t^{n+1}=\Delta t^n[1+\kappa_{\mathrm s}\arctan((\Delta t^{n+1}-\Delta t^n)/(\kappa_{\mathrm s}\Delta t^n))]$
($\kappa_{\mathrm s}$ page-local, 0.4 found the best compromise) and a cap
$\Delta t_{\mathrm{limit}}$ (Eqs. 68–70).

**Findings** (two-dimensional URANS at $N=5$: cylinder at $Re_D=3900$
compressible at $M=0.1$ and incompressible, cylinder at $Re_D=1.4\times10^5$,
tandem cylinders at $Re=1.66\times10^5$; a three-blade vertical-axis
wind turbine at $Re=1.6\times10^5$, tip-speed ratio 1.5, at $N=2$ on an
extruded mesh):

- for small steps adaptivity brings nothing (no rejected steps); it pays
  near the near-stability zone, which it extends by up to an order of
  magnitude, sometimes at reduced cost; H211b with the smooth limiter and
  H312b are the most robust on the stiffer cases (§6.1–6.3, §7, Tables
  10–14);
- capping the maximum step substantially improves robustness and
  efficiency, while bounding the step-change factor does not (§6.3,
  Figs. 26–28);
- ROS3PL is most efficient at loose accuracy, ROD5\_1 (compressible) or
  RODASP and peer5 (incompressible) at tight accuracy; observed orders on
  the turbulent cylinder are 2.8 (ROS3PL), 4.3 (RODASP), 5.4 (ROD5\_1), 3.3,
  3.1 and 1.8 (peer3, peer4, peer5) (§6.1, Fig. 15);
- on the turbine, ROS3PL with smoothed H211b runs at a mean step
  $0.023c/u_\infty$ ($c$ the chord), 1.64 times the largest stable fixed
  step and about 6 times the mean step of the authors' earlier adaptive
  implementation, with about 9.5% rejected steps and power coefficient
  0.173 against 0.171 of a reference two-dimensional RANS (§6.4,
  Table 17).

The two-dimensional URANS values of the $Re_D=3900$ cylinder ($C_D=1.52$
incompressible, 1.62 compressible; $St=0.23$) differ from LES, DNS and
experiment but agree with other two-dimensional URANS; the authors state
that the aim is efficiency and robustness, not prediction (§6.1, Table 9;
see [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)).
They also state that the compressible solver is more efficient than the
incompressible one on complex cases because the DAE linear systems are
worse conditioned (§6, §6.4).

## High-order DG for RANS: entropy stability and robust turbulence variables

**An entropy-stable DGSEM for RANS–Spalart–Allmaras.**
[Lodares et al. (2022)](/sources/lodares-2022.md) build, to their
knowledge the first, provably entropy-stable DGSEM for the compressible
RANS equations closed by the [Spalart–Allmaras](/methods/spalart-allmaras-model.md)
model: LGL collocation with the SBP property, curvilinear hexahedra with
Kopriva's conservative metric terms, BR1 lifting of the entropy-variable
gradients, and split-form volume terms (§4.1–4.4). The Navier–Stokes
entropy is augmented by $\tfrac12\rho\tilde\nu^2$; the SA part of the
analysis decouples, and the SA equation is entropy stable provided
$c_{b2}\le1$ and its diffusion coefficient stays non-negative, entropy
growing only where SA production exceeds destruction (§3.2, Eqs. 38–50).
For $\tilde\nu<0$ they use a variant of the negative SA model with the
diffusion coefficient clipped at zero; the variant and its constants are on
the SA page. Discretely, any Navier–Stokes two-point flux extends to the
SA equation by multiplying the mass-flux representation by
$\{\!\{\tilde\nu\}\!\}$; the SA interface flux is the mass flux times
$\{\!\{\tilde\nu\}\!\}$ minus $\tfrac12\lambda_\nu|\text{mass flux}|[\![\tilde\nu]\!]$
(page-local toggle $\lambda_\nu$: 0 entropy conserving, 1 entropy stable);
adiabatic free- and no-slip walls from a mirrored ghost state with
$-\rho\tilde\nu$ give dissipative boundary terms, whereas inflow and outflow
boundaries "can increase and/or decrease the entropy" (§4.4–4.5, §5.2).
The two configurations are kinetic-energy preserving (Pirozzoli flux,
Lax–Friedrichs) and thermodynamic-entropy stable (Chandrashekar flux,
matrix dissipation); see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)
and [entropy conservation](/properties/entropy-conservation.md). Results:

- a three-dimensional manufactured solution converges spectrally in $N$,
  with $h$-convergence exponents of the total error near $N+1$ in most
  variables (e.g. 7.09, 6.49, 7.34 for the standard, Pirozzoli and
  Chandrashekar forms at $N=8$; Table 1; see
  [method of manufactured solutions](/methods/method-of-manufactured-solutions.md));
- with random initial data at $\mu=10^{-8}$, $N=10$ and central fluxes the
  standard DG diverges and both split forms stay stable (§7.2, Figs. 5–6);
- on the coarsest NASA turbulence-modelling-resource grids, a flat plate at
  $Re=5\times10^6$ (816 elements, $N$ up to 10) and the
  [NACA 0012](/benchmarks/naca-0012-airfoil.md) at $Re=6\times10^6$
  ($113\times33$ grid with quadratic edges, $N=2$ to 6), the Pirozzoli form
  converges towards the fine-grid finite-volume references: at $N=6$,
  $C_L=1.0894$, $C_D=0.01250$ at $10^\circ$ against 1.0909 and 0.01231, and
  $C_L=1.5502$, $C_D=0.02144$ at $15^\circ$ against 1.5461 and 0.02124
  (§7.3–7.4, Table 2; see [turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md)).

Steady states come from a linearized implicit Euler solver with a
finite-difference Jacobian (graph colouring, a quasi-compact BR1 stencil on
Gauss–Lobatto nodes), PETSc GMRES with additive Schwarz and a CFL number
grown by switched evolution relaxation to about $10^{12}$ (§6, Fig. 1).
The authors suggest the same route for other RANS models and as the RANS
part of an entropy-stable [DES](/methods/detached-eddy-simulation.md)
(§8).

**Limiting and positivity of turbulence variables in modal DG.**
[Jiang et al. (2025)](/sources/jiang-2025.md) implement the $k$-$\sqrt kL$
model behind [scale-adaptive simulation](/methods/scale-adaptive-simulation.md)
in a modal DG with the Taylor basis of Luo et al., local Lax–Friedrichs
fluxes and BR2, steady GMRES and unsteady ESDIRK (§2). They state that
high-order DG solutions of turbulence variables oscillate where nonlinear
functions are approximated at high order, and use three devices (§3):
Hermite-WENO limiting of $k$ in cells flagged by an element-resolution
indicator (see [WENO](/methods/weno-scheme.md)); a smooth positive
surrogate of the length-scale variable in the source terms and eddy
viscosity, after Moro et al.'s SA treatment; and a compact second
derivative for the von Kármán length scale, the gradient of the DG
polynomial of first derivatives corrected by the BR2 global lift
operator, so that only face neighbours enter and the order matches the
first derivatives (§3.2, Eqs. 14–20). Without the stabilization the
implicit solver diverges on a flat plate ($M=0.3$, $Re=3\times10^6$),
with it the residual drops 5 to 6 orders at third and fourth order
(Fig. 1b); the lift operator removes an anomaly of the length scale near
$y^+\approx3000$ that the cell-local derivative produces (Fig. 2). On the
RAE2822 airfoil ($M=0.734$, $Re=6.5\times10^6$, $\alpha=2.79^\circ$) third
and fourth order give $C_L=0.779$ and 0.782, $C_D=0.0177$ and 0.0176,
against 0.803 and 0.0168 measured (§4.2). They note that the laminar
stretch near the plate's leading edge, where $C_f$ departs from theory,
lengthens with grid density and order, a numerical, not physical,
transition (§4.1).

**Third-order DG against finite volumes under coefficient uncertainty.**
[An et al. (2025)](/sources/an-2025.md), whose solver follows the cited
DG work of Jiang et al., solve
steady two-dimensional RANS with the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md)
in their in-house third-order DG solver (Roe flux, mean-flow and SA
equations fully coupled, $p$-multigrid-preconditioned GMRES smoothed by
line-implicit Gauss–Seidel; §2.2.2, Eq. 14) and in the second-order
finite-volume code CFL3D (MUSCL and Roe, approximate factorization;
§2.2.1). Their appendix motivates the limiting: at the edge of the
eddy-viscosity layer the weak solution of $\tilde\nu$ has discontinuous
first derivatives, high-order solutions oscillate, $\tilde\nu$ turns
negative and the solver diverges, so a Hermite-WENO limiter, triggered by a
modal detector on $\rho\tilde\nu$ (the logarithm of a ratio of inner
products of its degree-$N$ and degree-$(N-1)$ expansions, against a
case-dependent threshold), is
followed by a Zhang–Shu-type positivity limiter on $\tilde\nu$ (Eqs.
A.1–A.2). On the [backward-facing step](/benchmarks/backward-facing-step.md)
the DG grid is 0.21 times the finite-volume one ($249\times81$ against
$436\times225$) with results "comparable to or even better than FVM" (the
finite volumes better before the step and in the separation, DG after
reattachment, §3.1, Fig. 6), and on the [Gaussian bump](/benchmarks/gaussian-bump.md)
DG on about $201\times81$ points beats finite volumes on $401\times161$ at
the crest and in the separation (§3.2, Fig. 16). DG is more sensitive to
the model coefficients, and the authors hypothesize that its lower
numerical dissipation "may amplify" the errors of the SA model in separated
shear layers (§3.1); their Bayesian recalibration of seven SA constants
"tailored for DG schemes" is on
[Bayesian closure calibration](/methods/bayesian-closure-calibration.md).
A discontinuity of the DG solution near the step corner, also seen with
FUN3D in the NASA turbulence-modelling resource and attributed to the
geometric corner, prompts their call for more robust limiters (§3.1). The
polynomial degree is not printed; the paper states the order only, as
"third-order".

**A high-order DG transition model.** [Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md),
Appendix and §V, run a laminar-kinetic-energy transition model in the
modal DG RANS solver of [Ghidoni et al. (2026)](/sources/ghidoni-2026.md)
above (hierarchical orthogonal basis, exact Riemann solver, BR2,
logarithmic primitive variables for pressure, temperature and $\omega$,
residual-based [artificial viscosity](/methods/artificial-viscosity-shock-capturing.md),
pseudo-transient implicit solver), at $N=4$ on plates of 4000 elements with
$y_1^+=1$ and on airfoils. They report that high degrees do not converge
from a free-stream start, so each degree is initialized from the converged
lower one, and that large far-field elements make $k_L$ and $k_T$ negative,
whose clipping to zero then removes the free-stream turbulence at the
leading edge; a plain $k$-$\tilde\omega$ model is less sensitive (§V).
The model is on
[laminar kinetic energy transition models](/methods/laminar-kinetic-energy-transition-model.md).

**Finite-volume and flux-reconstruction relatives.** The same obstacles
(near-wall cells of aspect ratio $10^2$ to $10^3$, negative SA working
variable at the under-resolved boundary-layer edge) are addressed in a
fourth-order finite-volume RANS solver by
[Huang et al. (2022b)](/sources/huang-2022-d.md), whose 30P-30N run on
53,870 cells is compared with a DG solution at $N=4$ with 1,119,530 degrees
of freedom, their grid being 4.8% of that (§3.3, Figs. 33–34; see
[low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md)
for their reconstruction). In the implicit flux-reconstruction code
[COOLFluiD](/software/coolfluid.md), [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md)
transport $\ln\omega$ in the SST model, the idea Bassi et al. introduced
for DG with the Wilcox $k$-$\omega$ model (see
[$k$-$\omega$ SST](/methods/k-omega-sst-model.md) and
[flux reconstruction](/methods/flux-reconstruction.md)).

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

**HORSES3D settings for explicitly filtered LES.**
[Ranjbar et al. (2026)](/sources/ranjbar-2026.md), §II.A, §III, run the
HORSES3D DGSEM on Gauss–Lobatto nodes with Williamson's third-order
low-storage Runge–Kutta scheme and choose per case: the standard (non-split)
form with a low-dissipation Roe flux and BR1 without penalty for decaying
isotropic turbulence; the Chandrashekar split form with the same flux and
BR1 for the Taylor–Green vortex; and the split form with BR2 and penalty
1.5 for a channel at $Re_\tau=395$, "presence of walls necessitates BR2".
Gauss–Lobatto nodes are stated to be preferred for energy- or
entropy-stable SBP-SAT and split-form schemes. Their element filter width
is $\Delta=\mathcal J^{1/3}/\prod_{i=1}^3(N_i+1)^{1/3}$ with $N_i$ the
degree per direction (Eq. 42, after Komperda et al.). They build the
nodal–modal transform for any orthogonal basis and any collocation grid
from discrete orthogonality under the nodal quadrature, three
one-dimensional matrix products per element in three dimensions (§II.B,
Eqs. 17–27), and use it for a self-tuning modal filter, described on
[explicit modal filtering](/methods/explicit-modal-filtering.md). On
their coarse no-model channel mesh the r.m.s. velocities do not vanish
at the wall, which they attribute to the weak enforcement of the wall
condition, and jump between elements; the modal filter removes both
(§III.C, Fig. 15). A static [Smagorinsky](/methods/smagorinsky-model.md)
model on that channel crashed for $C_s<0.15$ and was inaccurate at
$C_s=0.2$ (§III.C, results not shown).

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
stabilized by gradient-jump penalisation and SVV. The continuous method,
including its weakly imposed wall stress and the derivative jumps that
matter for wall-modelled LES ([Mukha et al. 2025](/sources/mukha-2025.md);
[Reddy et al. 2026](/sources/reddy-2026.md)), has its own page,
[continuous-Galerkin spectral-element method](/methods/spectral-element-method.md).

## The DGSEM on GPUs (GALÆXI)

[Kurz et al. (2025)](/sources/kurz-2025.md) port FLEXI's DGSEM, with split
form, BR1 lifting, low-storage Runge–Kutta schemes and the
[subcell finite-volume blending](/methods/subcell-finite-volume-shock-capturing.md),
to NVIDIA GPUs in CUDA Fortran as [GALÆXI](/software/galaexi.md), keeping
FLEXI's data structures and user interface. Their semi-discrete form (§2.2,
Eqs. 10–19) is the weak form above, with curl-form metric terms (Eq. 11; see
[geometric conservation law](/properties/geometric-conservation-law.md)),
written with the code routines that compute each term:

- **Operation counts** (Table 1): the volume integral costs $O(N^4)$ per
  element, conversion to primitive variables $O(N^3)$ or $O(N^2)$, the
  prolongation to faces, the face fluxes and the surface integral $O(N^2)$,
  the Jacobian scaling $O(N^3)$; at $N=7$ with the split form the volume
  integral takes 39.0% of the run time and the volume–surface routines
  about 15%, so the overhead of the unstructured mesh is "negligible"
  (§3.3, Fig. 5).
- **Kernels** (§3.3, App. A): one thread per degree of freedom for pointwise
  operations; a race-free surface integral in which each thread owns one
  volume node and loops over the six faces of its element; one thread
  block per element for the volume integral, all fluxes kept in shared
  memory.
- **Streams** (§3.2): three prioritized CUDA streams (element interiors,
  inner faces, MPI faces at top priority) hide the communication behind
  local work, worth up to 92% more speed-up at low loads (Fig. 8).
- **Memory** (§4.3, Table 2): 1.457 KiB per degree of freedom at $N=1$
  falling to 0.787 KiB at $N=12$, with the surface-to-volume ratio
  $6(N+1)^2/(N+1)^3$; 48 million degrees of freedom fit on a 40 GiB A100 at
  $N=7$.
- **Scaling** (§4.4, Figs. 6–8): weak and strong scaling on up to 1024 A100
  GPUs of JUWELS Booster are almost perfect as long as each GPU holds more
  than about $10^6$ degrees of freedom; below that the code is
  "low-load-bound" (kernel launches, tail effects, then communication),
  whereas CPU FLEXI has a narrow optimum of 3000 to 10,000 degrees of
  freedom per core and loses performance at high loads (cache and memory
  bandwidth, as stated there).
- **Verification** (§5.1, Fig. 9): manufactured solutions converge at design
  order for $N=2$ to 9, both for standard DG on Legendre–Gauss nodes and
  for split-form DG on LGL nodes.

On the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at
$Re=1600$ ($N=7$, $64^3$ to $512^3$ degrees of freedom) GALÆXI and FLEXI give
identical results ("up to machine precision" at Mach 0.1), converging to the
references of DeBonis (Mach 0.1) and of Chapelier et al. (Mach 1.25) (§5.2,
Fig. 11). A wall-resolved LES of a [NASA Rotor 37](/benchmarks/nasa-rotor-37.md)
mid-span cascade ($N=5$, $2.6\times10^8$ degrees of freedom, no subgrid
model) on 128 A100 GPUs costs about 147 kWh per convective time against
339 kWh for FLEXI on 32,768 CPU cores, an energy saving of 56.8% that the
authors call "a rough estimate" (§6.3, Table 3).

## The DGSEM and modal DG in compressible shock–turbulence tests

**Supersonic Taylor–Green vortex.** In the comparison of
[Chapelier et al. (2024)](/sources/chapelier-2024.md) ($Re=1600$, $M_0=1.25$,
$64^3$ to $512^3$ degrees of freedom, no subgrid model), FLEXI runs a
fourth-order DGSEM ($N=3$) with a Roe flux and the second Harten–Hyman
entropy fix, BR1 and fourth-order low-storage Runge–Kutta, and the modal DG
code CODA a fourth-order total-degree hierarchical orthonormal basis
(20 modes per element at degree 3) with a Roe flux, BR1 and
localized [artificial diffusivity](/methods/artificial-viscosity-shock-capturing.md)
(§III.B.a, f). Both give, with the filtered compact finite differences of
NS3D, the highest solenoidal dissipation on all grids; at $64^3$ CODA
under-estimates the early kinetic energy, attributed to the dissipation of
the Riemann flux, while FLEXI stays closer to the central-difference codes
(§IV.A, Figs. 5, 7). The authors conclude that DG, spectral difference and
DGSEM "capture small scales well on coarse grids", better than finite
differences with local scheme switching or TENO, and that high order beats
second order in this compressible setting (§V).
[Witherden et al. (2025)](/sources/witherden-2025.md), §5.1, Fig. 12,
Table 1, set the same CODA and FLEXI data (order 4, artificial viscosity
and subcell finite volumes) against [PyFR](/software/pyfr.md) with entropy
filtering at equal resolution and order: the flux-reconstruction runs show
dilatational dissipation closer to the $2048^3$ TENO reference, which they
read as less shock dissipation (see
[flux reconstruction](/methods/flux-reconstruction.md)).

**Oblique shock/turbulent-boundary-layer interaction.**
[Gao et al. (2022)](/sources/gao-2022.md) run FLEXI's split-form DGSEM
(Pirozzoli two-point flux, approximate Riemann solver with the
Harten–Hyman entropy fix, BR1, five-stage fourth-order low-storage
Runge–Kutta) as an implicit LES, relying "solely" on the interface
Riemann-solver dissipation, of an oblique shock reflecting on a Mach 2
turbulent boundary layer ($8^\circ$ deflection, $Re_{\theta_0}=1628$),
which they state is the first high-order DGSEM implicit LES of this
interaction (§1, §3.1). At $N=6$ on $129\times81\times26$ elements (about
93 million degrees of freedom; $\Delta y^+_{\min}=1.6$, $\Delta x^+=30$,
$\Delta z^+=16$ at the reference station "in combination with $N=6$"), with
a synthetic-eddy inflow and anisotropic linear forcing, the undisturbed
boundary layer matches the DNS of Wenzel et al., and the separation and
reattachment points are $16.7\delta_r$ and $19.5\delta_r$ against
$17.6\delta_r$ and $19.3\delta_r$ in the much finer LES of Morgan et al.
(§5.2–5.3, Table 2, Figs. 16–22). On 16,384 cores the shock-free boundary
layer runs at about 1.55 µs per degree of freedom, stage and core, which
the authors put 94.0% above the FLEXI baseline of Krais et al. (load
imbalance of the synthetic eddies, forcing, statistics), and the
interaction at 1.84 µs with the
[finite-volume subcells](/methods/subcell-finite-volume-shock-capturing.md)
switched by a filtered [shock sensor](/definitions/shock-sensor.md); the
two runs cost about 46,173 and 196,608 CPU hours (§5.2–5.3, Eq. 19). See
[shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).

**The same interaction over an elastic panel (ALE DGSEM).**
[Gao et al. (2023)](/sources/gao-2023.md) repeat a Mach 2 oblique-shock
interaction (8° deflection, $Re_{\theta}=2188$ at the reference station)
over a panel that deforms, with FLEXI's split-form arbitrary
Lagrangian–Eulerian DGSEM (Pirozzoli kinetic-energy-preserving two-point
flux, LGL nodes, BR1, five-stage fourth-order Runge–Kutta) coupled loosely
to a Legendre spectral finite-element Timoshenko beam of the same degree,
so that fluid and structure meshes match at the interface (§2–3). The
geometric conservation law is discretized with the same polynomial basis
(see [geometric conservation law](/properties/geometric-conservation-law.md)).
Turbulence is wall-resolved implicit LES, "no explicit SGS model" (§1).
At $N=6$ on $223\times89\times26$ elements (about 177 million degrees of
freedom; $\Delta x^+=30$, $\Delta y^+=1.6$ at the wall, $\Delta z^+=16$
at the reference station) the run takes $8.0\times10^5$ CPU hours on
16,384 cores at $3.26\times10^{-6}$ s per degree of freedom, stage and
core, which they put 55.7% above the split-form ALE DGSEM with prescribed
mesh motion in free stream (§5.1, Table 4, Eq. 68); the shock-free
boundary layer at the same conditions runs at about 1.74 µs, 34.6% above
the baseline of Kempf et al. (§5.2). Against the rigid-panel run of Gao et
al. (2022) the separated area is 49.0% larger, a new unsteadiness
appears at the panel frequency ($St\approx0.01$), and the
separation-induced low frequency $St\approx0.03$ is essentially unchanged
(§5.3–5.4). The shock capturing changed between the two runs (see
[subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)).

**Laminar hypersonic interactions with the DGSEM.**
[Potluri et al. (2023)](/sources/potluri-2023.md) use a strong-form
collocated LGL DGSEM, its SBP subcell flux-difference form and the split
form with the Chandrashekar two-point flux (§3.1, Eqs. 4–7), with BR1 in
entropy or conservative variables (§3.2), for laminar hypersonic
shock/boundary-layer interactions; there is no turbulence in the paper.
On a Mach 2.15 laminar interaction, $N=2,3,4$ at about $150\times108$
degrees of freedom give "virtually indistinguishable" wall pressure but
different skin friction, $N=2$ being lower before separation and less
smooth in the bubble (§4.3, Table 2, Figs. 6–7); on a Mach 8.1 cylinder at
equal degrees of freedom $N=2$ oscillates in the stagnation heat flux and
$N=1$ overshoots it, so that heat flux "can depend significantly on the
$N$, even if the DoF count is kept constant" (§4.7, Fig. 15). Their
subcell blending with a hypersonic wall modification is on the subcell
page.

**Supersonic isothermal turbulence with modal DG.**
[Cernetic et al. (2024)](/sources/cernetic-2024.md) use their GPU modal DG
code (Legendre basis on Cartesian cells, truncated to total degree $N$, so
$(N+1)(N+2)(N+3)/6$ coefficients per field; HLLC flux; strong-stability-preserving
Runge–Kutta of matching order) for driven isothermal turbulence at rms Mach
0.1 to 12.8. It is a modal relative, not the nodal collocated DGSEM. Two
changes make high Mach numbers stable (§3): a von Neumann–Richtmyer viscous
pressure at the internal quadrature points (see
[artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)),
and the re-projection of the primitive variables onto the basis from their
values at the internal Gauss points, $\frac{1}{|K|}\int_Kf\phi_l\,dV$ ($K$ a
cell, $\phi_l$ the basis, $f$ a primitive variable; page-local), before
extrapolation to the faces, instead of taking the face velocity as the
ratio of the momentum and density polynomials, which can produce extreme
values in shocked turbulence (§3.2, Eq. 17, Fig. 3). At $256^3$ cells DG of
orders 2 and 3 extends the resolved spectral range markedly against a
second-order finite-volume scheme in subsonic turbulence, but the advantage
"nearly disappears" in the supersonic regime (§5, Fig. 5); at Mach 3.2, DG of
order 2 resolves the sonic scale at $1024^3$, and at $512^3$ "does nearly
as well as" finite volumes at $1024^3$ (§6, Figs. 8, 11).

**Cost against order with shocks.** For $N_x^3$ cells ($N_x$ cells per direction) and
degree $N$, Cernetic et al. (2024, §7, Eqs. 33–35) count about $(N+1)^6$
operations per cell and evaluation for their modal scheme and a total cost
$\propto N_x^4N^8$ to a fixed time; with an idealized error model, high order
pays for smooth problems and small target errors, but for a single planar
shock with error $\propto N_x^{-1}(N+1)^{-1}$ it is "always computationally
favorable" to refine the mesh rather than raise the degree. They conclude
that with many shocks orders above 3 are unlikely to be cost-effective, a
"sweet spot" at order 2 or 3 ($N=1$ or 2), and suggest $h$-refinement at
shocks with $p$-refinement in smooth regions. The count assumes a
total-degree basis, $(N+1)^3$ volume quadrature points and $N+1$
Runge–Kutta stages per step; the collocated tensor-product DGSEM above has
$O(N^4)$ volume work per element, $O(N)$ per degree of freedom (Krais et
al. 2021; Kurz et al. 2025, Table 1); Cernetic et al. give no timing.

**Modal Runge–Kutta DG with TENO limiters.** At the other end of the
family, [Huang & Fu (2024)](/sources/huang-2024.md) and
[Huang et al. (2025)](/sources/huang-2025.md) use the Cockburn–Shu modal
Runge–Kutta DG with a scaled Legendre basis on uniform Cartesian grids
($N=2$, SSP-RK3 at CFL 0.15, Rusanov or local Lax–Friedrichs flux), in
which a troubled-cell indicator flags cells and a limiter rebuilds their
higher modes; their TENO-based indicator and limiters are on
[shock sensors](/definitions/shock-sensor.md) and
[WENO](/methods/weno-scheme.md). Huang et al. (2025, §1) state that the
TENO limiter makes "no essential difference" between modal and nodal
bases, citing a nodal spectral-difference version (see
[spectral difference](/methods/spectral-difference-method.md)). Neither
paper runs a turbulent flow.

**Modal DG for adjoint RANS.** [Fanizza et al. (2025)](/sources/fanizza-2025.md),
§2.3, discretize steady compressible RANS with the Spalart–Allmaras model in
ONERA's Aghora code: modal DG with a hierarchical orthonormal basis of total
degree $N$, $(N+d)!/(N!\,d!)$ functions per element in $d$ dimensions,
diagonal mass matrix, Roe or local Lax–Friedrichs fluxes, BR2 viscous terms
and Gauss–Legendre quadrature with $(N+1)^d$ points. The discrete adjoint of
this discretization drives their [field inversion](/methods/field-inversion-machine-learning.md);
on a laminar cylinder the lowest cost minimum is reached at $N=2$, the
lowest degree at which the baseline is free of grid dependence, and they
recommend assimilating at that degree (§4.1).

## The DGSEM in a transonic implicit LES

[Klose et al. (2025)](/sources/klose-2025.md), §2–3, run DLR's
[TRACE](/software/trace.md) DGSEM as implicit LES ("dissipation is added
implicitly via the numerical dissipation of the Riemann solver") of a
transonic [compressor cascade](/benchmarks/compressor-cascade.md) at inlet
Mach 1.21 and $Re=1.35\times10^6$: LGL collocation, $N=3$, the
entropy-conserving Chandrashekar split form with its matching Riemann
solver, BR1 with a central flux, explicit third-order Runge–Kutta, and
subcell finite-volume blending at shocks. Spans of 5%, 10% and 20% of the
chord on a coarse grid (54.6 to 218 million degrees of freedom, 15,583 to
77,950 CPU hours per convective time) and a refined 10% span (375 million,
152,850 CPU hours) give the same buffet frequency, $fc/U\approx0.16$ against
about 0.14 in the experiment, but an amplitude of the shock oscillation that
falls with span on the coarse grid and rises with refinement (Tables 1–2);
the authors call the coarse runs under-resolved. Wall-unit spacings divided
by $N$ have maxima $(65,2.5,40)$ on the coarse grid and $(35,2,25)$ on the
fine one (§3). See
[shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).

## Qualifications

- **Printed forms (Lv & Ekaterinaris 2023).** The review prints the
  mass matrix as $\int_{-1}^{1}\varphi_j\varphi_i\,d\xi$ while its
  reference element and Eq. (20) use $[0,1]$, and calls the representation
  "of order p or degree p+1" while its expansion has $p+1$ basis
  functions of degree $p$ and its "DGP3" is fourth order; this page writes
  the degree $N$. The combustion comparisons with second-order schemes are
  stated from the cited works.
- **The log basis of Lv et al. (2021).** Eq. (3) writes the basis function
  $\kappa^{-1}\log((y+y_0)/y_0)$, Eq. (8) $\log((y-y_0)/y_0)$. The paper
  does not say how $y_0$ is set in the runs.

- **Two performance figures of the same shock-free boundary layer.**
  Gao et al. (2022) report about 1.55 µs per degree of freedom, stage and
  core, 94.0% above the FLEXI baseline of Krais et al.; Gao et al. (2023,
  §5.2) report about 1.74 µs for the shock-free boundary layer at their
  conditions, 34.6% above the baseline of Kempf et al. The runs differ
  (moving-mesh framework, conditions, statistics collection, which they
  name as the main overhead) and the baselines differ, so the values are
  recorded side by side, not as a contradiction.

- **Memory per degree of freedom.** Krais et al. (2021, Table 4) report for
  CPU FLEXI 1.47 KiB at $N=1$ and 0.567 KiB at $N=12$; Kurz et al. (2025,
  Table 2) report for GALÆXI 1.457 and 0.787 KiB. The codes differ; the
  values are recorded side by side, not as a contradiction.
- **Printed slips (Cernetic et al. 2024, arXiv v2).** Eq. (35) prints the
  total cost as $\tfrac56N_x^4(1+N)^4(10N^4+100N^3+315N^2+523N+372)$; the
  paper's own ingredients, which reproduce its Eq. (33), give $351N^2$ in
  place of $315N^2$ *(compiler check, not in the sources)*; the leading
  scaling is unaffected. Eq. (8) prints the Kronecker index of the
  orthonormality as $\delta_{l,k}$ for $\delta_{l,m}$, and the context of
  Eq. (10) writes the error $\propto h^{-(N+1)}$ with $h$ the cell size,
  while elsewhere the paper writes $\propto N_x^{-(N+1)}$ with $N_x$ cells
  per direction.
- **Printed slip (Kurz et al. 2025, arXiv v2).** Eq. (15) prints the
  Lagrange polynomial with the product index equal to its own label and the
  factor $(x_i-x)$, which cannot satisfy the Kronecker property of their
  Eq. (16); the correct form is the one at the top of this page.

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
- **Wall units on element grids.** Morsbach et al. (2024, §3.1) give blade
  resolutions in wall units divided by $N$; Wang (2024, §4.2, Eq. 26, after
  Jia et al.) divides the first-cell $y^+$ by $N+1$. The two are different
  conventions for a per-degree-of-freedom spacing, not a disagreement, but
  their values are not directly comparable.
- The 40% applicability plateau is inferred by Flad & Gassner (2017) from two
  resolutions of one test case at $N=7$; the authors present it as a
  finding, not a bound.
- The factor-3 saving of split forms over de-aliasing (Flad & Gassner 2017,
  §6.1) is stated without timings or hardware; the factor-2 measurement of
  Brillon & Nadarajah (2026, §3.1.3) is for one code (PHiLiP, flux
  reconstruction) on one cluster, in the arXiv v1 preprint.
- **Two "sweet spots".** Cernetic et al. (2024) place the cost-effective
  order of modal DG for shocked turbulence at order 2 or 3 ($N=1$ or 2);
  Schotte et al. (2026, §3) call $N=2$ and 3 a sweet spot for modal DG on
  complex RANS configurations. The statements concern different flows and
  criteria (an idealized cost model with many shocks against practice on
  steady aerodynamic cases) and are not competing claims.
- Ghidoni et al. (2026)
  measure $y^+$ on the first-element height, not on a node distance or
  the element height over $N+1$ (§1), a third convention beside those of
  Morsbach et al. and Wang (2024) above.
- Ranjbar et al. (2026) is the arXiv v1 preprint; their Smagorinsky
  channel runs are reported without data.
- **Printed slips (Lodares et al. 2022).** Eq. (93) labels the SA viscous
  volume term with the superscript NS; Table 2 names the NACA 0012
  reference "FUN3D, 897×257" and the legends of Fig. 10 "CFL3D, 897 x 257";
  the thermodynamic configuration is called entropy stable (§4.6) and
  entropy conserving (§5.3, abstract). The entropy proof covers adiabatic walls only and permits
  entropy growth wherever SA production exceeds destruction.
- **Wall resolution on DG grids, again.** Gao et al. (2022, Table 2) give
  their wall-unit spacings "in combination with $N=6$" without saying
  whether they are per element or per degree of freedom, a fourth
  convention beside those listed above.
- Gao et al. (2022, §4.2) print the DG/FV saving in the laminar
  interaction as "around 35% less" CPU time; the printed times give 25.9%
  less (see [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md))
  *(compiler check, not in the sources)*.
- Jiang et al. (2025) name their schemes by order in the text and by
  degree in the figures (DG(P1)–DG(P3) for second to fourth order).
- **Printed slips (Ghidoni et al. 2022).** §1 and §7 call ROS3PL
  "third order/three stages" while Table 1 gives four stages. In Table 2,
  the ROD5\_1 pressure order printed 5.00 for the step $T/160$ follows from
  the printed errors $3.96\times10^{-10}$ and $4.79\times10^{-11}$ as
  $\log_2 8.27=3.05$ (the velocity columns give 4.99), consistent with the
  authors' remark that errors below $10^{-11}$ are polluted by the spatial
  error *(compiler check, not in the sources)*. The text gives the
  compressible $Re_D=3900$ cylinder $c'_L=1.19$ and $St=0.225$ where Table 9
  gives 1.13 and 0.23. The printed H211b, PI 4.2 and H312b formulas follow
  from the step-prediction relation (Eq. 62) only if its $\Delta t$ carries
  the exponent $q_r$, which is not printed *(compiler check, not in the
  sources)*; several percentages of Tables 13–14 are not reproduced by the
  error limits printed in their captions, which repeat those of Table 13
  in Table 14, and Table 14 and Table 18 give different clock-time changes
  for the same tandem runs *(compiler check, not in the sources)*.
- Ghidoni et al. (2022, Fig. 15) observe order 1.8 for peer5 (design
  order 5) on the turbulent cylinder, while §4.2 introduces peer schemes as
  "proposed to overcome the order reduction" of traditional Rosenbrock
  schemes at high stiffness; the paper does not discuss the observed
  order.
- Fidkowski (2022, §4, Eq. 18) assumes that the correlation between
  adjoint and residual fluctuations is negligible for chaotic flows; no
  regularized unsteady adjoint is computed to check it. The "DES" of the
  high-lift case uses a fixed, mesh-independent attenuation of the wall
  distance, $d_{\max}\tanh(d/d_{\max})$ with $d_{\max}=0.02c$ (Eq. 3),
  chosen to keep the model constant during adaptation.

# Citations

- [Hamedi & Vermeire (2022)](/sources/hamedi-2022.md) — §2.1 (FR recovering nodal DG, Rusanov, BR2); §3.2, Eqs. (28)–(30) (time-step-independent filter); §3.3–3.4, Tables 4–6 (optimized exponential filter); §5.1–5.2.
- [Fidkowski (2022)](/sources/fidkowski-2022.md) — §2.2, Eqs. (4)–(7) (DG with Roe and BR2, augmented system); §4, Eqs. (17)–(23) (E1, E2); §5, Eq. (24) (indicators, $p$-adaptation and MOESS); §6, Tables 1–3, Figs. 4, 11, 17 (unstable unsteady adjoints, adaptation results).
- [Ghidoni et al. (2022)](/sources/ghidoni-2022.md) — §1–3, Eqs. (1)–(18) (modal DG URANS with $k$-$\log\omega$); §4.1–4.2, Eqs. (19)–(50), Tables 1–7, Fig. 3 (Rosenbrock and peer schemes, starting procedure, near-stability zone); §5, Eqs. (51)–(70), Table 8 (error estimator, controllers, limiters); §6.1–6.4, Tables 9–17, Figs. 5–31 (cylinders, tandem cylinders, VAWT); §7, Tables 18–19; printed slips in §1, §6.1, §7, Eq. (62), Tables 2, 13–14.
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
- [Wang (2024)](/sources/wang-2024-b.md) — arXiv v2: §2.2, Eqs. (9)–(16), Fig. 1 (FR recovering nodal DG on LGL points, LDG); §2.3, Eqs. (17)–(19) (switched modal filter, entropy filter); §3; §4.1; §4.2, Eq. (26); §4.4.3.
- [Duan & Wang (2024)](/sources/duan-2024.md) — §3, Eqs. (26)–(30) (element-averaged eddy viscosity, filter widths); §5.4; §6.
- [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md) — §1; §3.1 (SUPG/PSPG continuous Galerkin in Lethe); Table 1 (DG under-resolved DNS and DNS of Krank et al., as tabulated).
- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §3.1, Eqs. (3-1)–(3-10) (improved IPDG, fluxes, artificial viscosity); §3.2 (finite-volume SST equations, BDF2); §4, Tables 4-1–4-2.
- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv 2404.12703v2: §2.2, Eqs. (10)–(19), Table 1 (DGSEM routines and operation counts); §3.2–3.3, Fig. 5, App. A (streams, kernels, time breakdown); §4.3–4.4, Table 2, Figs. 6–8 (memory, scaling); §5.1–5.2, Figs. 9–11 (manufactured solutions, Taylor–Green vortex); §6.3, Table 3 (Rotor 37 cascade, energy).
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — HAL hal-04582857v1: §III.B.a, f (CODA modal DG, FLEXI DGSEM); §IV.A, Figs. 5, 7; §V.
- [Cernetic et al. (2024)](/sources/cernetic-2024.md) — arXiv 2401.06841v2: §2, Eqs. (5)–(9) (modal DG); §3.1–3.2, Eq. (17), Fig. 3 (artificial viscosity, primitive-variable projection); §5–6, Figs. 5, 8, 11; §7, Eqs. (33)–(35), Figs. 13–14 (cost model); Conclusions.
- [Fanizza et al. (2025)](/sources/fanizza-2025.md) — §2.3, Eqs. (6)–(15) (modal DG in Aghora); §4.1 (degree for data assimilation).
- [Klose et al. (2025)](/sources/klose-2025.md) — ASME accepted manuscript: §2–3, Tables 1–2 (TRACE DGSEM implicit LES of a transonic cascade).
- [Mukha et al. (2025)](/sources/mukha-2025.md) — arXiv 2404.05378v1: §II.B (continuous spectral elements in Nek5000).
- [Reddy et al. (2026)](/sources/reddy-2026.md) — preprint of 4 March 2021: §4 (continuous spectral elements in NUMA).
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) — arXiv 2411.12108v1: §2.10 (strong DG with over-integration); §3.1.3, Figs. 11–12 (instability without over-integration, cost); §3.1.4, Fig. 13 (GL against LGL flux nodes, DG-SEM); §3.1.8, Fig. 20.
- [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) — arXiv 2512.03315v1: §II.A (HORSES3D settings, Gauss–Lobatto nodes); §II.B, Eqs. (17)–(27), (42) (nodal–modal transform, filter width); §III.C, Fig. 15 (wall fluctuations, Smagorinsky).
- [Lederer et al. (2026)](/sources/lederer-2026.md) — arXiv 2408.06698v1: §2.2–2.3 (mixed-stress method, exact quadrature, projection splitting).
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §2–2.1, Eqs. (6)–(37) (HDG RANS, stabilization); §4, Eqs. (72)–(75) (static condensation); §5.1, Table 1, Figs. 4–6; §5.2.1, Table 3, Fig. 15 (wall shear from the auxiliary unknown); §6, Figs. 37–45.
- [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) — §1 (DG wall resolution); §2, Eqs. (2)–(11) (modal DG RANS, BR2, wall $\omega$, implicit solver); §3.3, Fig. 1 (wall-function feeding point).
- [Schotte et al. (2026)](/sources/schotte-2026.md) — §1 (compact stencil); §2.2, Eqs. (5)–(7) (modal DG in CODA); §3, Eqs. (15)–(25) (sweet spot, DG Hessian, spectral estimators); §4.1 (degree staging, solver).
- [Wang & Roy (2023)](/sources/wang-2023.md) — Journal Pre-proof: §2.1, Eqs. (1)–(10) (modal DG); §3.1, Eqs. (11)–(16) (error transport equations, orders); §4–5.
- [Lodares et al. (2022)](/sources/lodares-2022.md) — §1; §3.2, Eqs. (38)–(50) (SA entropy, stability conditions); §4.1–4.6, Eqs. (51)–(79) (LGL DGSEM for RANS–SA, two-point and interface fluxes, walls); §5, Eqs. (80)–(118); §6, Eqs. (119)–(123) (implicit solver); §7, Tables 1–2, Figs. 1–10; §8.
- [Jiang et al. (2025)](/sources/jiang-2025.md) — §2, Eqs. (8)–(9) (modal Taylor-basis DG); §3.1–3.2, Eqs. (10)–(20) (HWENO limiting of $k$, positive surrogate, lift-operator derivatives); §4.1–4.2, Figs. 1–4 (flat plate, RAE2822).
- [Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md) — Appendix, Eqs. (A1)–(A9) (modal DG RANS solver, AV, implicit solver); §V (order-by-order initialization, negative $k_L$, $k_T$).
- [Huang et al. (2022b)](/sources/huang-2022-d.md) — §3.3, Figs. 33–34 (finite-volume 30P-30N against a DG $N=4$ reference).
- [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md) — §1.1 ($\ln\omega$ transport after Bassi et al.'s DG; flux reconstruction in COOLFluiD).
- [Gao et al. (2022)](/sources/gao-2022.md) — §1; §3.1, Eqs. (8)–(11) (split-form FLEXI DGSEM, implicit LES); §5.1–5.3, Table 2, Eq. (19), Figs. 16–22 (SWBLI resolution, performance, results).
- [Huang & Fu (2024)](/sources/huang-2024.md) — §3, Eqs. (16)–(25) (modal RKDG).
- [Huang et al. (2025)](/sources/huang-2025.md) — §1; §2, Eqs. (1)–(10) (modal RKDG).
- [Wang et al. (2013)](/sources/wang-2013.md) — §3.2 (work units); §5.1–5.6, Figs. 15–27 (DG against finite volumes and differences; Taylor–Green; RAE 2822); §6 (RANS robustness, memory of line-implicit solvers).
- [Lv et al. (2021)](/sources/lv-2021.md) — §II A–C, Eqs. (3)–(12) (log-law basis, wall shear from coefficients); §III, Eqs. (13)–(20) (SUPES DG with PPM finite volumes).
- [Maltsev et al. (2022)](/sources/maltsev-2022.md) — §III B–C, §V (modal and reconstructed DG for multi-material flow, passing mention).
- [Gao et al. (2023)](/sources/gao-2023.md) — §1; §3.1, Eqs. (16)–(39) (split-form ALE DGSEM, GCL); §5.1–5.4, Table 4, Eq. (68), Figs. 18–30 (implicit LES of the interaction over an elastic panel, performance).
- [Potluri et al. (2023)](/sources/potluri-2023.md) — §3.1–3.2, Eqs. (4)–(14) (strong, subcell and split forms; BR1); §4.3, Table 2, Figs. 6–7; §4.7, Fig. 15, Table 3 (dependence on $N$ at fixed degrees of freedom).
- [Liu & Yuan (2023)](/sources/liu-2023-b.md) — §2.2 (VCJH flux reconstruction recovering collocation nodal DG on Gauss–Legendre points).
- [Tonicello et al. (2023)](/sources/tonicello-2023.md) — §3, Fig. 7, App. Figs. 29–30 (FR-DG against FR-SD eigencurves, CFL limits).
- [Lv & Ekaterinaris (2023)](/sources/lv-2023.md) — §3.1, Eq. (20) (DG weak form, nodal and modal bases, mass-matrix conditioning, viscous discretizations); §3.4, Eq. (28) (HDG/EDG face unknowns); §6.3, Figs. 14–16 (DG combustion LES, reviewed); §7.
- [Vermeire (2024)](/sources/vermeire-2024.md) — §3, Eqs. (6)–(13) (FRDG recovering DG for linear equations); §4.3 (DG reference at $N=7$ for SD7003, cited).
- [Alberti et al. (2025)](/sources/alberti-2025-b.md) — §2.1, Eq. (6) (positive-part SA source, $r$ limit); §2.2, Eqs. (19)–(22) (incompressible modal DG, artificial-compressibility Godunov flux, BR2, ROS3Pw); §2.3, Eq. (23), Table 1 (length-scale normalization, equivalent hexahedron); §3.1.2–§3.1.3, Tables 4–5, Figs. 12–14; §4.
- [An et al. (2025)](/sources/an-2025.md) — §2.2.1–§2.2.2, Eq. (14) (CFL3D and third-order DG RANS–SA); §3.1–§3.2, Figs. 6, 16 (step and bump, DG against finite volumes); Appendix, Eqs. (A.1)–(A.2) (HWENO and positivity limiting of $\tilde\nu$).
- [Witherden et al. (2025)](/sources/witherden-2025.md) — §5.1, Fig. 12, Table 1 (CODA and FLEXI against entropy-filtered PyFR on the supersonic Taylor–Green vortex).

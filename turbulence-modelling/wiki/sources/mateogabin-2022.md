---
type: Source
title: "Mateo-Gabín et al. (2022) — An entropy stable spectral vanishing viscosity for discontinuous Galerkin schemes: Application to shock capturing and LES models"
description: "Constructs a spectral vanishing viscosity for the Gauss–Lobatto DGSEM that is provably entropy stable, by placing a modal Legendre filter between symmetric factors of the artificial-dissipation matrix, and applies it as an SVV-filtered Smagorinsky LES model on the inviscid Taylor–Green vortex and as shock capturing."
resource: "doi:10.1016/j.jcp.2022.111618"
source_kind: paper
authors: [Mateo-Gabín A., Manzanero J., Valero E.]
year: 2022
venue: "J. Comput. Phys. 471:111618"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Journal_of_Computational_Physics_Mateo-Gabín_An_entropy_stable_spectral_vanishing_viscosity_for_discontin.pdf"
tags: [dg, entropy-stable, sgs-model, numerical-dissipation, kinetic-energy-preserving]
timestamp: 2026-10-26T20:48:00Z
---

# Summary

Mateo-Gabín et al. (2022) build a
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md) (SVV)
for the Gauss–Lobatto
[discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
that is entropy stable at the semi-discrete level. An artificial dissipative
flux is added to the compressible Navier–Stokes equations, either as an
increased molecular viscosity $\mu_a$ or as the Guermond–Popov viscous
regularization (density diffusion $\alpha_a$ plus viscosity $\mu_a$). Each is
written as a symmetric positive semi-definite matrix times the gradient of
entropy variables, for two entropies: the kinetic energy, for
[kinetic-energy-preserving split forms](/properties/kinetic-energy-preservation.md)
(Pirozzoli flux), and the thermodynamic entropy, for entropy-stable split
forms (Chandrashekar flux). The SVV filters this flux modally in the Legendre
basis, so that dissipation acts on chosen modes. The filter is placed between
symmetric factors of the dissipation matrix (a square root of a scalar
coefficient, or a Cholesky factorization). A discrete Parseval identity and
the non-negativity of $\langle Q,\mathcal F\star Q\rangle$ for non-negative
kernel coefficients then make the filtered volume dissipation non-negative,
and the BR1 interface and wall treatments cancel the remaining terms.

A von Neumann analysis on advection–diffusion with $N=7$ and the kernel
$(i/N)^{P_{SVV}}$ shows that $P_{SVV}$ mainly controls the dissipation at low
wavenumbers, where the SVV supplies nearly all of it, and that the Riemann
solver dominates elsewhere ([numerical dissipation](/properties/numerical-dissipation.md)).
As an LES model the SVV filters a [Smagorinsky](/methods/smagorinsky-model.md)
viscosity added to the molecular one ([Boussinesq](/definitions/boussinesq-hypothesis.md)
form): on the inviscid [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
with $8^3$ elements and $N=8$, the unfiltered Smagorinsky model is too
dissipative, and $P_{SVV}\approx0.1$ gives a spectrum close to $k^{-5/3}$. The
paper contrasts this explicit model with [implicit LES](/definitions/implicit-les.md),
which relies on the scheme's own dissipation. As shock capturing (the
Guermond–Popov flux with a density-gradient switch) it is tested on the
Shu–Osher problem and a Mach 3 forward-facing step; shock capturing occupies
half of the numerical section.

# Version read

arXiv preprint 2109.06653v3 [math.NA], 16 September 2022, Springer "Noname
manuscript" template, 37 pages, all read. It is not the typeset version of
record and carries no DOI. Page-1 title and authors match the published
article. Metadata (year, venue, DOI) are those of the published version;
equation, section, figure and reference numbers on this page are those of
the preprint.

# Key claims

1. An entropy-stable SVV for DGSEM is obtained by filtering artificial-viscosity fluxes so that the volume dissipation stays non-negative, with the filter applied between the symmetric (square-root or Cholesky) factors of the dissipation matrix (§5, Eqs. 101–102; §5.1, Eqs. 109–110). **Proved** (semi-discrete)
2. The Navier–Stokes viscous flux in kinetic-energy entropy variables gives the artificial dissipation $D_a^{\mathcal K}=\mu_a\big(2S_{ij}S_{ij}-\tfrac23(\nabla\cdot\boldsymbol u)^2\big)\ge0$, printed as $\mu_a\big(2|\mathsf S|^2-\tfrac23(\vec\nabla\cdot\vec u)^2\big)$ (§2.2.1, Eq. 25). **Derived**
3. In thermodynamic entropy variables the artificial Navier–Stokes dissipation is a quadratic form with a diagonal Cholesky factor, non-negative provided $\mu_a$, the diagonal entries and $T$ are positive (§2.2.2, Eqs. 26–27, App. C; factors from Fisher & Carpenter). **Derived**
4. The Guermond–Popov flux in thermodynamic entropy variables, $\mathcal B_{GP}=\alpha_a\rho\mathcal B^\alpha_{GP}+\mu_ap\mathcal B^\mu_{GP}$, admits a Cholesky decomposition with non-negative diagonal whenever $\rho,p\ge0$, hence entropy-stable dissipation (§2.2.3, Eqs. 28–30; App. D, Eqs. 134–137). **Derived**
5. The Legendre nodal-to-modal and modal-to-nodal matrices on Gauss–Lobatto points are mutual inverses (Eq. 75) and satisfy $w_iB_{ij}=\|L_j\|_N^2F_{ji}$ (Eq. 76), which gives the discrete Parseval identity $\sum_iw_iU_iV_i=\sum_j\|L_j\|_N^2\hat U_j\hat V_j$ (Eqs. 77–78). **Proved**
6. Theorem 1: $\langle Q,\mathcal F\star Q\rangle_N=\sum_j\|L_j\|_N^2\hat{\mathcal F}_j\hat Q_j^2\ge0$ for non-negative filter coefficients; a similar result is used by Nordström & Winters (§4.1, Eqs. 82–84). **Proved**
7. Theorem 2 and Property 4 extend the Parseval identity and the positivity to 3D tensor-product elements (§4.2, Eqs. 89–93, 99–100). **Proved**
8. A tensor-product kernel $\hat{\mathcal F}_{ijk}=\hat{\mathcal F}_i\hat{\mathcal F}_j\hat{\mathcal F}_k$ reduces the filtering cost from "$(N+1)^3$ operations" to "$3(N+1)$ operations" (three 1D matrix–vector products) (§4.2, Eqs. 95–96). **Stated**
9. Two multidimensional kernels are built from a 1D kernel: high-pass $\hat{\mathcal F}^{1D}_i\hat{\mathcal F}^{1D}_j\hat{\mathcal F}^{1D}_k$ (Eq. 97) and non-high-pass $1-(1-\hat{\mathcal F}^{1D}_i)(1-\hat{\mathcal F}^{1D}_j)(1-\hat{\mathcal F}^{1D}_k)$ (Eq. 98) (§4.2, Fig. 1). **Stated**
10. With BR1 interface fluxes for the artificial viscosity (averages of the flux and of the entropy variables), the interior-face contribution of the filtered artificial flux vanishes (§5.1, Eq. 115). **Proved**
11. For no-slip and free-slip adiabatic walls with the boundary treatment of Eqs. 60–61, the physical-boundary contribution of the filtered artificial flux vanishes, and the semi-discrete entropy balance (Eq. 118) is non-positive (Eqs. 116–118; inviscid and viscous parts cited). **Proved**
12. For the kinetic energy the pressure-work term cannot be bounded, so kinetic-energy stability is not a strict entropy statement; kinetic-energy-preserving schemes are described as robust and cheaper for subsonic flows, thermodynamic-entropy schemes as preferred for supersonic flows (§5.1; §2.3, Eq. 35). **Stated**
13. Von Neumann analysis (1D advection–diffusion, $N=7$, upwind flux, BR1, $\mu_a=0.01$, $P_{SVV}\in\{0,0.1,1,10\}$): the effect of $P_{SVV}$ is most evident at low wavenumbers, where the SVV gives almost all the dissipation; elsewhere the added viscosity is smaller than the Riemann-solver dissipation; the results are "in agreement with" Manzanero et al. (§5.2, Figs. 2–3). **Shown**
14. With $\hat{\mathcal F}_i=(i/N)^{P_{SVV}}$, $P_{SVV}=0$ recovers the unfiltered viscous operator, and only $\mu_a=0$ removes the viscosity entirely (§5.2, after Eq. 122). **Stated**
15. Inviscid TGV, $8^3$ elements, $N=8$, Pirozzoli kinetic-energy-preserving split form with a low-dissipation Roe solver, Smagorinsky viscosity with $C_s=0.2$ filtered by a high-pass SVV: the unfiltered model ($P_{SVV}=0$) is excessively dissipative, and $P_{SVV}\approx0.1$ is optimal, with a spectrum close to $k^{-5/3}$ over most resolved wavenumbers at $t=20$ (§6.1, Fig. 4). **Shown**
16. In the TGV the SVV changes the highest modes little and acts on low-to-medium wavenumbers, avoiding high-frequency energy pile-up (§6.1). **Shown**
17. Against the van Rees et al. reference ($768^3$, quoted at "Re = 1600", a viscous computation, while the test is inviscid) the scheme dissipates less during the first five time units and then rises to a comparable level (§6.1, Fig. 4a). **Shown**
18. Shu–Osher: SVV alone does not control the strong shock, so a density-gradient sensor $s_1$ sets $P_{SVV}=0$ where $s_1>10$ and $P_{SVV}=2$ elsewhere; with an SVV-filtered Guermond–Popov flux, all three discretizations (50 elements $N=5$; 100 elements $N=5$ and $N=8$) reproduce the flow features without most spurious oscillations (§6.2, Eq. 127, Fig. 5). **Shown**
19. In Shu–Osher the Guermond–Popov density regularization removes fluctuations in the lower part of the shock, and the SVV filtering smooths the downstream region while leaving low-order modes almost unaltered (§6.2). **Shown** (qualitative)
20. Mach 3 forward-facing step, 3653 unstructured quadrilaterals, $N=7$, faces not aligned with the flow: the main shock is resolved within one element, and the wake and mixing-layer structures are captured at $t=10$ (§6.3, Figs. 6–7). **Shown** (qualitative)
21. $P_{SVV}=O(1)$ suits supersonic flows, while turbulent cases need a flatter profile, $P_{SVV}\approx O(10^{-2})$, "even without the help of the LES approach"; there is no systematic strategy for choosing $P_{SVV}$, and only a range of values keeps the Shu–Osher solution close to the reference (App. A, Fig. 8). **Shown**/**Stated**
22. Compared with the earlier Smagorinsky-SVV of Manzanero et al. (same group), the SVV-LES "improves the results for a wide range of values of the SVV exponent, reducing the impact of the choice of $P_{SVV}$", and, "in contrast to the method presented in [24], the approach described herein is entropy stable" (§7). **Stated** (entropy stability proved here)
23. Lundquist & Nordström reached a similar conclusion with a filter kernel $J^{-1/2}\mathcal FJ^{1/2}$ for time stability (§5.1, after Eq. 110). **Stated**
24. Entropy-preserving split-form schemes are not by themselves stable for shocks, because entropy stability rests on positive density, which oscillations near shocks can violate; shock capturing must add density regularization (§1). **Stated**

# Printed slips

- **Sensor in §6.3.** The forward-facing step uses the sensor $s_2$ (Eq. 128), but the switching rule is printed with $s_1$ ("$s_1<1$: … $s_1\geqslant1$: …").
- **Coefficient names.** $\mu_a$, $\alpha_a$ in the text; $\mu_\alpha$, $\alpha_\alpha$ in Table 1 and §6.3.
- **Eq. 26.** "the Cholesky decomposition of the matrix $\tilde{\mathcal B}_a^{\mathcal S}=\mathcal L_v^{S,T}\mathcal D_v^S\mathcal L_v^S$": the factors are those of $\tilde{\mathcal B}_v^{\mathcal S}$ (the artificial matrix is $\frac{\mu_ap}{\rho}\tilde{\mathcal B}_v^{\mathcal S}$), and the next expression uses $\tilde{\mathcal B}_v^{\mathcal S}$.
- **Eq. 30.** $D_a^{GP}=\vec\nabla\mathbf w^{S,T}\tilde{\mathcal B}_{GP}\vec\nabla\mathbf w$ carries a tilde and an unsuperscripted $\mathbf w$; Eq. 28 defines $\mathcal B_{GP}$ without a tilde.
- **Eq. 66.** The parameter of Tadmor's step kernel is printed "$\varepsilon M=0.25$", without further definition.
- **Eq. 122.** The kernel is printed "$\hat{\mathcal F}_i=\mathrm{diag}[(i/N)^{P_{SVV}}]$", an index on a diagonal matrix.
- **Time units (§6.1).** "During the first five seconds" for the non-dimensional TGV time.
- **Typos.** "discontinous" (keywords), "aditional", "aproach", "capturig"; reference [42] title printed "finite folume schemes".
- **Eq. 125** *(compiler check, not in the sources)*. $\mu_a=C_S^2\Delta^2|\mathsf S|$ is used as a dynamic viscosity but has no density factor, so it has the dimension of a kinematic viscosity; the TGV has $\rho\approx1$.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf q=(\rho,\rho\vec u,\rho e)^T$ | ($\rho$, $\rho u_i$, $E$) | $\rho e$ is the total energy per unit volume, registry $E$ |
| $\overleftrightarrow f_e$, $\overleftrightarrow f_v$, $\overleftrightarrow f_a$, $\overleftrightarrow f_{GP}$ | (inviscid, viscous, artificial, Guermond–Popov fluxes) | |
| $\mu_a$ ($\mu_\alpha$), $\alpha_a$ ($\alpha_\alpha$) | (artificial viscosity, density-diffusion coefficient) | **collision:** $\alpha_a$ is not the DG blending factor $\alpha$ |
| $\tau_{ij}$ | $\sigma_{ij}$ | **collision:** viscous stress, not the SGS stress |
| $\mathsf S$, $S_{ij}$, $\lvert\mathsf S\rvert$ | $S_{ij}$, $\lvert S\rvert$ | the paper does not state its magnitude convention; Eq. 25 is the Navier–Stokes dissipation only if $\lvert\mathsf S\rvert^2=S_{ij}S_{ij}$, i.e. $\lvert\mathsf S\rvert=\lvert S\rvert/\sqrt2$ *(compiler check, not in the sources)* |
| $\Delta$, $\Delta^3=$ cell volume$/(N+1)^3$ | $\Delta$ | filter width; agrees |
| $C_S=0.2$ | $C_s$ | |
| $\kappa=\theta\mu R$, $\theta=\gamma/((\gamma-1)Pr)$ | (thermal conductivity, its factor) | **collision:** $\kappa$ is not the von Kármán constant, $\theta$ not the momentum thickness |
| $\mathcal E$, $\mathcal K=\rho\lvert\vec u\rvert^2/2$, $\mathcal S=-\rho s/(\gamma-1)$ | (mathematical entropy, kinetic energy, thermodynamic entropy function) | |
| $\mathbf w$, $\mathbf w^{\mathcal K}$, $\mathbf w^{\mathcal S}$ | (entropy variables) | **collision:** not the velocity component $w$ |
| $\mathcal B$, $\mathcal L$, $\mathcal D$, $D$ | (dissipation matrix, Cholesky factor, diagonal, local dissipation) | **collision:** $D$ is also the SBP derivative matrix $D_{ij}$, which agrees with the registry |
| $N$ | $N$ | polynomial degree; agrees |
| $w_i$ | $w_i$ | Gauss–Lobatto weights; agrees |
| $l_i$, $L_i$, $F$, $B$ | (Lagrange, Legendre polynomials; forward, backward transform matrices) | $B$ also the SBP boundary matrix |
| $Q_j$, $\hat Q_j$ | (nodal, modal coefficients) | **collision:** the hat is a modal coefficient, not a test filter |
| $\hat{\mathcal F}_k$, $\mathcal F\star$, $\mathcal H$ | (filter-kernel coefficients, filtering operator, nodal filter matrix) | **collision:** $\mathcal F\star$ weights the dissipative flux (high values = more dissipated mode), not the solution |
| $P_{SVV}$ | (kernel exponent) | kernel $(i/N)^{P_{SVV}}$ after Moura et al. |
| $\{\{\cdot\}\}$, $[\![\cdot]\!]$ | $\{\!\{\cdot\}\!\}$, (jump) | |
| $J$ | $\mathcal J$ (registry §11) | Jacobian determinant of the element map |
| $E(k)$ | $E(k)$ | kinetic-energy spectrum; $E$ also the reference element |
| $s_1$, $s_2$ | (density-gradient sensors) | |

# Reference list

57 printed references, numbered style [1]–[57]. The list is merged complete
into the [bibliography](/bibliography.md) with `citedby` this slug. Several
items have incomplete printed data: [1] Reed & Hill (1977), [2] Cockburn
et al. (2000), [29] Merriam (1989), [35] Winters et al. (2021) and [44]
Carlson (2011) print no venue, [13] no pages. [23] Lodares et al. is printed
"Under review in Journal of Computational Physics (2021)" and is its own
pre-publication entry; [36] and [54] are arXiv preprints. [16] Persson &
Peraire is printed as an AIAA conference paper and [51] Hindenlang et al. as
a chapter. [55] Pope is printed with the venue "Measurement Science and
Technology 12 (2001) 2020–2021" and recorded as printed. The first author
of [40] is printed "D. C. D. R. Fernández". No printed duplicates or
unparseable items.

# Pages created or updated

Chunk 2 (2026-10-25), cited further in chunks 3, 6, 7, 8. This source is cited on:

- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
- [Subcell finite-volume shock capturing for DG](/methods/subcell-finite-volume-shock-capturing.md)
- [Entropy conservation and entropy stability](/properties/entropy-conservation.md)
- [Geometric conservation law and free-stream preservation](/properties/geometric-conservation-law.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [HORSES3D](/software/horses3d.md)

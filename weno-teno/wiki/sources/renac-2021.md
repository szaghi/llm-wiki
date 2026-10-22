---
type: Source
title: "Renac (2021) — Entropy stable, robust and high-order DGSEM for the compressible multicomponent Euler equations"
description: "Entropy-stable, positivity-preserving Gauss–Lobatto DGSEM for the multicomponent Euler equations of a mixture of polytropic gases: a new entropy-conservative flux with three logarithmic means, an entropy-stable positive relaxation flux, and a proof of cell-average positivity on unstructured quadrilaterals."
resource: "doi:10.1016/j.jcp.2021.110584"
source_kind: paper
authors: [Renac F.]
year: 2021
venue: "J. Comput. Phys. 445:110584"
local_file: "/home/stefano/papers/mosaic/weno-teno/2021_Crossref_Journal_of_Computational_Physics_Renac_Entropy_stable_robust_and_high-order_DGSEM_for_the_compressi.pdf"
tags: [dg, entropy-stable, positivity, bound-preserving, multiphase, riemann-solver]
timestamp: 2026-10-22T12:00:00Z
---

# Summary

The paper builds a [DGSEM](/methods/dgsem.md) on Gauss–Lobatto nodes for the
conservative [multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
of a mixture of $n_c$ polytropic ideal gases in thermal and mechanical
equilibrium, unknowns $(\rho Y,\rho,\rho v,E)$. The scheme has three
properties: [entropy stability](/properties/entropy-stability.md) for the
mixture entropy $\eta=-\rho s$; positivity of the partial densities and of the
internal energy ([bound preservation](/properties/bound-preservation.md)); and
exact [preservation of stationary material interfaces](/properties/stationary-contact-preservation.md).

There are three layers. (1) A new two-point
[entropy-conservative flux](/methods/entropy-conservative-flux.md) for the
mixture that needs only three [logarithmic means](/operators/logarithmic-mean.md),
against $n_c+1$ for a Gouasmi-type flux re-derived in an appendix; it is also
formally [kinetic-energy preserving](/properties/kinetic-energy-preservation.md).
(2) An entropy-stable, positive three-point flux, obtained by composing the
Coquel–Perthame energy relaxation (a polytropic law with a constant
$\gamma_{\mathrm r}>\max_i\gamma_i$ plus an advected extra internal energy) with
Bouchut's pressure relaxation solver. Its relaxation entropy is convex but not
strictly convex, which blocks the general relaxation framework, and the
pressure relaxation supplies the entropy inequality instead. The result is an
HLLC-like three-wave solver ([HLL family](/methods/hll-riemann-solvers.md)).
(3) [Flux differencing](/methods/flux-differencing.md) with the EC flux in the
volume and the relaxation flux at interfaces, on
[summation-by-parts](/operators/summation-by-parts-operator.md) operators,
gives a semi-discrete cell entropy inequality.

Theorem 6.1 proves that the forward-Euler DGSEM keeps the cell averages
admissible under a CFL condition with factor $1/(2N(N+1))$ on unstructured
straight-sided quadrilaterals, extending Zhang–Shu's Cartesian result through
a quadrilateral version of the Perthame–Shu lemma; the proof is a Gauss–Lobatto
[cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
with boundary weight $\mathsf w_0=2/(N(N+1))$. A
[Zhang–Shu-type scaling limiter](/methods/zhang-shu-scaling-limiter.md) adapted
to the mixture restores nodal positivity, and
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) steps extend the result in time.
The tests ($N=3$, Aghora code) are a smooth convection problem, an
entropy-conservation check, six two-component Riemann problems including a
[Sod-type](/benchmarks/sod-and-lax-shock-tubes.md) case, a
[shock–helium bubble](/benchmarks/shock-bubble-interaction.md) (whose interface
rolls up in [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md)
vortices), a Richtmyer–Meshkov instability with re-shock and a Mach 2
shock–hydrogen bubble. An appendix shows that an EC flux with scalar Roe-type
dissipation is less robust.

# Version read

arXiv preprint 2001.05710v3 [math.NA], 16 Jul 2021 ("Preprint submitted to
Elsevier, July 19, 2021"), not the version of record; 33 pages (text pp. 1–25,
appendices A–D pp. 25–30, references pp. 31–33), all read, pp. 6, 13–17 and 29
checked visually because the extraction garbles their equations. Title and
single author match Crossref; venue and DOI come from Crossref. Equation,
lemma, table and figure numbers cited here are those of the arXiv v3.

# Key claims

Registry notation (see the notation map): DG degree $N$, Gauss–Lobatto
weights $\mathsf w_i$, admissible set $G$, element $K$, cell average
$\bar u_K$, entropy pair $(\eta,F_\eta)$, entropy variables $w$, two-point
EC flux $f^{\mathrm{ec}}$, interface flux $h$, HLL-type speeds $s^\pm$; the
relaxation constant is $\gamma_{\mathrm r}$, the inverse temperature $1/T$ is
written out.

1. The flux (24) is symmetric, consistent and entropy conservative for the multicomponent Euler system with the mixture entropy pair (13) (Lemma 3.1, §3.1). **Proved**
2. It needs only three logarithmic means, $\{\!\{\rho_{n_c}\}\!\}_{\log}$, $\{\!\{\rho\}\!\}_{\log}$ and $\{\!\{1/T\}\!\}_{\log}$, against $n_c+1$ for the flux (B.1); it is cheaper for $n_c>2$ and less exposed to floating-point exceptions, since the logarithmic mean needs positive arguments (Remark 3.1). **Stated** (the count is evident from the formula)
3. The flux (24) is formally kinetic-energy preserving in Jameson's sense, but the property can fail discretely (Remark 3.2). **Stated**
4. The entropy $\rho\zeta$ of the energy-relaxation system (32) is convex but not strictly convex, and satisfies the minimization principle $-s(Y,\tau,e)=\min_{e_r+e_s=e}\zeta$ with a unique minimum at equilibrium (40) (Lemma 4.1, Eqs. 41–48). **Proved**
5. Because $\rho\zeta$ is not strictly convex, the general Coquel–Perthame / Marmignon–Naddei–Renac framework for entropy-stable relaxation schemes does not apply directly; Bouchut's pressure relaxation scheme replaces it (§4.2, §4.3.1). **Derived**
6. The three-point scheme (27) with flux (51)/(53) is consistent, Lipschitz continuous, entropy stable in the sense (28) and positive (keeps $G$) under $\frac{\Delta t}{\Delta x}\max_j\lvert\lambda(u_j)\rvert<\frac12$, $\lvert\lambda(u)\rvert=\lvert v\cdot n\rvert+a/\rho$, provided $\gamma_{\mathrm r}>\max_i\gamma_i$ (§4.3.2, §4.4, Appendix C). **Proved** (largely by reference to Marmignon et al. Th. 4.3 and Bouchut Prop. 2.21)
7. Lemma 3.2 (Perthame–Shu Th. 4 extended to quadrilaterals): a positive three-point scheme gives a positive scheme (30) on quadrilateral meshes under the CFL condition (31); the proof extends to star-shaped polygons (Appendix A). **Proved**
8. Theorem 6.1: for the forward-Euler DGSEM (65) with the relaxation flux at interfaces and the EC volume flux, if all nodal values lie in $G$ then the cell averages at $t^{n+1}$ lie in $G$ under the CFL condition (66) with right-hand side $\frac{1}{2N(N+1)}$, on unstructured straight-sided quadrilateral meshes and for any $N$ (§6.2). **Proved**
9. The DGSEM resolves stationary material interfaces ($v=0$, equal $p$, different $(Y,\rho)$) exactly at the nodes: both (24) and (53) reduce to $(0,0,pn^\top,0)^\top$ and the volume residual vanishes; if the interface lies on mesh faces the relaxation solver gives the exact solution (proof of Theorem 6.1, p. 16). **Proved**; confirmed by RP4 (Fig. 4). **Shown**
10. The factor $\frac{2}{N(N+1)}=\mathsf w_0=\mathsf w_N$ separates (66) from (31); neither condition is optimal (Remark 6.1). **Stated**
11. The semi-discrete scheme (62)–(63) satisfies the cell entropy inequality (64), as an instance of the Fisher–Carpenter flux-differencing schemes, whose high-order accuracy is proved elsewhere (§5.2). **Stated** (cited)
12. The flux-level entropy inequality (21) is not proved directly: it follows from the scheme-level inequality (28) by Bouchut's Lemma 2.8 (§3.2, §4.3.2). **Stated**
13. Convection of void-fraction and density waves: the design order $N+1$ is recovered (e.g. $N=3$, $L^1$ errors $9.2849\times10^{-5}$, $3.0461\times10^{-6}$, $3.0281\times10^{-7}$ on meshes $1/16$, $1/32$, $1/64$, observed orders 4.16, 4.96, 3.33); the first-order scheme reaches only 0.77 at $1/256$ (§7.1, Table 1). **Shown**
14. With the EC flux also at interfaces (RP0, $N_K=100$ cells, $N=3$) the global entropy error tends to zero with $\Delta t$ at third order, the order of the time integrator (orders 1.16, 2.25, 2.87, 2.98, 3.00; error from $-6.34260\times10^{-8}$ to $-2.89133\times10^{-11}$); with the ES flux the dissipation is $-7.6977\times10^{-7}$ independently of $\Delta t$ (§7.2, Table 3). **Shown**
15. Riemann problems RP1–RP5 ($N=3$, 100 cells): shocks and contacts well captured; small oscillations in RP2 (He–N$_2$) with a train at the rarefaction tail; positivity kept in the near-vacuum RP3; the stationary interface of RP4 exact; spurious oscillations around the moving interface of RP5, "inherent to discretely conservative schemes" (§7.2, Figs. 3–4). **Shown**
16. Shock–helium bubble ($M=1.22$, 238,673 unstructured elements, $N=3$): no significant spurious oscillations; interface-point trajectories close to Kawai–Terashima (§7.3, Figs. 5–6). **Shown**
17. Richtmyer–Meshkov with re-shock ($M=1.21$, air–acetone / SF$_6$, Atwood number 0.6053, $1601\times118$ Cartesian elements): good resolution of shocks, interface and vortices on a mesh coarse relative to earlier studies (§7.4, Fig. 7). **Shown**
18. Strong shock–hydrogen bubble ($M=2$, 74,504 unstructured elements): results compare well with the literature, showing robustness on unstructured meshes (§7.5, Fig. 8). **Shown**
19. In practice the bound $\Delta t\max_K\frac{1}{\lvert K\rvert}\sqrt{\sum_{e\in\partial K}\lvert e\rvert^2}\,\lvert\lambda(\bar u_K)\rvert\le0.4$ kept positivity in all runs; it is simpler and less restrictive than (66) (§7). **Shown**
20. A Roe-type ES flux (flux (24) plus scalar dissipation, Eq. D.1) is entropy stable but not Lipschitz continuous, blocks positivity proofs, needs CFL 0.2 instead of 0.4, and the 2D runs stop on negative solutions, with spurious oscillations at shocks (Appendix D, Figs. D.9–D.10). **Proved** (entropy stability) / **Shown** (loss of robustness)
21. Fluxes of the "EC plus upwind dissipation" type are not Lipschitz continuous, which the positivity results of Bouchut, Perthame–Shu and others require (§1.2). **Stated**
22. Simple-wave solvers (HLL, Roe, Rusanov, relaxation) need upper bounds of the maximum wave speed, and fast estimates (two-rarefaction, Guermond–Popov) do not exist for this model "to the best of our knowledge" (§1.3). **Stated**
23. Dellacherie's relaxation for multicomponent Euler does not hold for the separated mixture in Eulerian coordinates considered here (§1.3). **Stated**

# Printed slips

- Eqs. (59)–(60): the sums are printed $\sum_{1\le i,j\le p}$ (checked visually, p. 14), while the nodes run from 0 to $p$.
- §7.5: "In Fig. 6 we plot contours of pressure, void fraction and numerical Schlieren" for the hydrogen bubble, which is Fig. 8.
- §7.4 (p. 23): "$At=\frac{\rho_2-\rho_1}{\rho_1+\rho_2}=0.6053$ where $\rho_2=\gamma_2$ is taken as the pre-shock density of the mixture"; the air–acetone mixture is component 1, so the clause should read $\rho_1=\gamma_1$. *(compiler check, not in the sources: with $\rho_1=\gamma_1=1.24815$ and equal pressure and temperature, $\rho_2=\rho_1r_1/r_2\approx5.08$ with $r_i=(\gamma_i-1)C_{v_i}$, which gives $At\approx0.605$.)*
- Eq. (64): the surface sum is printed without the quadrature weight $\omega_k$ (p. 15), which the analogous sum in the proof of Theorem 6.1 carries.
- Eq. (67b) uses $\breve V$, defined only through $\breve\rho$; *(compiler check, not in the sources)* reading $\breve V=(\breve\rho,\rho v,\rho E)$ makes (67b) consistent.
- Lemma 3.1 refers to "the HRM model (1)" without defining HRM.
- Table 1, $p=1$: the error grows from $1/4$ to $1/8$ (negative orders), and the $p=3$ order falls to 3.33 at $1/64$, while the text says "The expected p+1 order of convergence is recovered".
- Abstract: "guaranty", "The later results" (latter).

# Notation map

| Renac (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf u=(\rho\mathbf Y,\rho,\rho\mathbf v,\rho E)$ | $u=(\rho Y,\rho,\rho v,E)$ | the source's $E$ is specific (per unit mass) |
| $\mathbf Y$, $n_c$, $\alpha_i$ | kept | mass fractions of the first $n_c-1$ components, number of components, void fractions; **$\alpha_i$ collides with $\alpha_k$** |
| $\rho_i$, $e_i$, $\mathrm p_i$, $T_i$, $\gamma_i$, $C_{v_i}$, $r_i$ | kept | component quantities, $r_i=(\gamma_i-1)C_{v_i}$ |
| $\mathrm p$, $\gamma(\mathbf Y)$, $r(\mathbf Y)$ | $p$, $\gamma(Y)$, $r(Y)$ | mixture pressure and coefficients; **$r(Y)$ collides with the WENO stencil size $r$** |
| $\gamma$ (no argument) | $\gamma_{\mathrm r}$ | relaxation constant, $\gamma_{\mathrm r}>\gamma_{\max}$ |
| $\tau=1/\rho$ | kept | specific volume; **collides with the WENO-Z indicator $\tau$** |
| $\theta=1/T$ | $1/T$ | inverse temperature; **$\theta$ is the limiter scaling factor in the registry** |
| $\eta=-\rho s$, $\mathbf q=-\rho s\mathbf v$ | $\eta$, $F_\eta$ | mixture entropy pair (no factor $1/(\gamma-1)$) |
| $\eta'(\mathbf u)$, $\psi$ | $w$, $\psi$ | entropy variables; flux potential $\psi=r(Y)\rho v$ |
| $[\![a]\!]$, $\bar a$, $\hat a$ | $[\![a]\!]$, $\{\!\{a\}\!\}$, $\{\!\{a\}\!\}_{\log}$ | jump, arithmetic and logarithmic means |
| $\mathbf h_{ec}$, $\mathbf h$ | $f^{\mathrm{ec}}$, $h$ | EC volume flux, interface flux |
| $\Omega^a$, $\Omega^r$ | $G$, kept | admissible sets of the model and of the relaxation system |
| $\mathbf w$, $e_r$, $e_s$, $\zeta$, $\zeta^r$ | kept | relaxation unknowns and entropies; **$\mathbf w$ is not the entropy variables** |
| $a$, $a_L$, $a_R$, $\pi$ | kept | Lagrangian sound speeds and relaxation pressure; $a/\rho$ is the Eulerian wave speed; **not the registry maximum wave speed $a$** |
| $S_L$, $S_R$ | $s^-$, $s^+$ | outer waves of the relaxation solver |
| $u^\star$, $\mathrm p^\star$ | kept | star normal velocity and pressure |
| $p$ | $N$ | DG degree; **$p$ is the pressure in the registry** |
| $\omega_i$ | $\mathsf w_i$ | Gauss–Lobatto weights, $\mathsf w_0=\mathsf w_N=2/(N(N+1))$ |
| $\ell_k$, $D_{ik}$, $J^{ij}_\kappa$ | $\ell_k$, $D$, $J$ | Lagrange basis, differentiation matrix, Jacobian |
| $\kappa$, $\langle u_h\rangle_\kappa$ | $K$, $\bar u_K$ | element and cell average; **$\kappa$ is the kinetic energy in the registry** |
| $\theta^\rho_\kappa$, $\theta^{Y_i}_\kappa$, $\theta^e_\kappa$ | $\theta$ | limiter scaling factors |
| $\varepsilon=10^{-10}$ | kept | positivity floor |
| $N$ | $N_K$ | number of cells or elements; **$N$ is the DG degree in the registry** |
| $\nu_{AD}$ | kept | dissipation coefficient of the Roe-type flux |

# Reference list

80 printed references in numbered style ([1]–[80]), sorted alphabetically by
first author, all parsed and merged complete into the
[bibliography](/bibliography.md) with `citedby` `renac-2021`. Same-author
same-year works take suffixes in printed order (Renac 2015 [62]/[65]). [8]
prints no volume or pages, [21] only the article number; [18] and [65] are book
chapters with no book title printed; [54] is an arXiv preprint (2103.03731)
kept as its own entry; the author of [64] is printed as a dash (Renac). No
printed duplicates or unparseable items.

# Pages created or updated

Chunk 2 (2026-10-22), cited further in chunks 3–5 (2026-10-22/23). This source is cited on:

* [Bound preservation](/properties/bound-preservation.md)
* [Discontinuous Galerkin spectral element method (DGSEM)](/methods/dgsem.md)
* [Double rarefaction (123) problem](/benchmarks/double-rarefaction-problem.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)
* [Five- and six-equation diffuse-interface models](/definitions/five-equation-model.md)
* [Flux differencing and split-form DG](/methods/flux-differencing.md)
* [Gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Kinetic energy preservation](/properties/kinetic-energy-preservation.md)
* [Logarithmic mean](/operators/logarithmic-mean.md)
* [Multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
* [Optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
* [Richtmyer–Meshkov instability](/benchmarks/richtmyer-meshkov-instability.md)
* [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Stationary contact preservation](/properties/stationary-contact-preservation.md)
* [Summation-by-parts operator](/operators/summation-by-parts-operator.md)
* [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)

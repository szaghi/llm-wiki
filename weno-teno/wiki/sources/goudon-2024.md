---
type: Source
title: "Goudon & Minjeaud (2024) — An explicit well-balanced scheme on staggered grids for barotropic Euler equations"
description: "Hydrostatic reconstruction adapted to an explicit kinetic-flux staggered finite-volume scheme for barotropic Euler with a potential source: exact lake-at-rest preservation with dry zones, non-negative density, a semi-discrete entropy inequality and a well-balanced second-order MUSCL version."
resource: "doi:10.1051/m2an/2024035"
source_kind: paper
authors: [Goudon T., Minjeaud S.]
year: 2024
venue: "ESAIM Math. Model. Numer. Anal. 58:1263-1299"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_ESAIM_Mathematical_Modelling_and_Numerical_Analysis_Goudon_An_explicit_well-balanced_scheme_on_staggered_grids_for_baro.pdf"
tags: [well-balanced, finite-volume, positivity, entropy-stable, shallow-water]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper makes an explicit staggered finite-volume scheme
[well-balanced](/properties/well-balancing.md) for the one-dimensional barotropic
Euler equations with a potential source $-\rho\partial_xz$. The
[shallow-water equations](/definitions/shallow-water-equations.md) are the case
$p=\rho^2/2$. Densities live on primal cells $[x_j,x_{j+1}]$, velocities on dual
cells centred at the nodes $x_j$. The baseline is the authors' earlier scheme. Its
mass fluxes $\mathcal F^\pm$ come from a uniform "Maxwellian" velocity distribution of
half-width $c(\rho)$, the momentum convection fluxes upwind the velocity with the
dual mass fluxes, and the pressure is centred.

The new ingredient is a hydrostatic reconstruction at the velocity nodes, in the
manner of Audusse et al. It sets $z_j=\max(z_{j-1/2},z_{j+1/2})$ and reconstructs
densities $\rho^r_j$ and $\rho^\ell_j$ from $\mathcal E(\rho)+z$, with a
positive part. These densities enter the mass and convection fluxes. A discrete
source turns pressure plus source into $p(\rho^r_j)-p(\rho^\ell_j)$.

The resulting first-order scheme:

* is consistent, also near dry areas;
* preserves lake-at-rest states exactly, dry shores included;
* keeps the density non-negative under a CFL condition, a
  [bound-preservation](/properties/bound-preservation.md) result;
* satisfies a semi-discrete [entropy](/properties/entropy-stability.md)
  (total-energy) inequality. The fully discrete one stays open.

A [MUSCL](/methods/muscl-hancock.md)-type second-order version reconstructs $\rho$
and $\mathcal E(\rho)+z$ linearly. It adds a correction
$\tfrac12(\rho^r_j-\rho^\ell_j)\lvert\delta z_j\rvert$ to the source that removes
the first-order defect, and it still preserves the equilibria, dry areas included.

The tests cover:

* lakes at rest with and without dry zones for $\gamma\in\{1.4,2,3,4\}$, and
  convergence to them from constant data;
* LeVeque's perturbed lake;
* the Houghton–Kasahara [flow over a bump](/benchmarks/flow-over-a-bump.md) in
  four regimes, against exact asymptotic references;
* two tests of Castro, Pardo, Parés & Toro (2010);
* a wet/dry Riemann problem over a step;
* the 2D Thacker paraboloid.

Rest states are kept to machine precision. Smooth moving steady states, which the
scheme does not preserve exactly, converge at second order in $L^1$. The Thacker
test gives an observed order of 1.8. No high-order reconstruction is involved, and
positivity comes from the CFL condition and the monotonicity of the mass fluxes, not
from a [flux limiter](/methods/positivity-preserving-flux-limiter.md).

# Version read

HAL deposit hal-04654775v1 (20 July 2024) of the version of record (EDP Sciences and
SMAI typeset, CC-BY 4.0). PDF page 1 is the HAL cover; PDF pages 2–38 are journal
pp. 1263–1299. Received 4 May 2023, accepted 7 May 2024. Title, authors, venue and
DOI match Crossref. Equation numbers and page locators are the journal's.

# Key claims

Registry notation, with these page-local symbols. The velocity is $v$, the
topography (potential) $z$ and the barotropic pressure $p(\rho)$, with
$c(\rho)=\sqrt{p'(\rho)}$. The equilibrium potential is
$\mathcal E(\rho)=p(\rho)/\rho+\int_0^\rho p(s)/s^2\,ds$, and the free-surface
level $\eta_{\mathrm l}$. Further, $\delta z_j=z_{j+1/2}-z_{j-1/2}$,
$[a]_+=\max(0,a)$ and $[a]_-=\min(0,a)$. The staggered indices are the source's:
half-integer indices are density cells, integer indices velocity nodes.

1. The naive centred source $S_j=\rho_j\,\delta z_j/\Delta x_j$ is $O(\Delta x_j)$ consistent but does not preserve the discrete equilibrium: $p(\hat\rho_{j+1/2})-p(\hat\rho_{j-1/2})+\hat\rho_j\,\delta z_j$ does not vanish in general (§2.1, p. 1268). **Derived**
2. Without source, the staggered scheme preserves positivity and entropy dissipation under a CFL condition and is consistent with Euler, as proved in the authors' earlier work (§2.1, p. 1268). **Stated**
3. The dual-mesh mass balance (11) holds with the dual density (9) and the dual fluxes (10) (§2.1). **Derived**
4. With the hydrostatic reconstructions (14)–(16) and the fluxes and source (17), the scheme (18) is flux-consistent (it reduces to the original fluxes where $z$ is locally constant), and $S_j/\Delta x_j$ is consistent with $\rho\partial_xz$. For shallow water away from wet/dry transitions, $S_j=\tfrac12(\rho_{j+1/2}+\rho_{j-1/2})\delta z_j-\tfrac12(\rho^r_j-\rho^\ell_j)\lvert\delta z_j\rvert$ (Eq. (19)), a first-order approximation (§2.2). **Derived**
5. For general pressure laws, $S_j=\delta z_j\,\rho_{j+1/2}+o(\lvert\delta z_j\rvert)$ if $\delta z_j\le0$ and $\delta z_j\,\rho_{j-1/2}+o(\lvert\delta z_j\rvert)$ if $\delta z_j\ge0$, near dry cells too, using $p(\rho)=o(\mathcal E(\rho))$ (Eq. (24), pp. 1269–1270). **Derived**
6. Away from wet/dry transitions the consistency error is first order. In dry areas it stays first order if $\lim_{\rho\to0}p''(\rho)\ne0$ (Remark 2.1). **Derived**
7. At a discrete equilibrium (2), $\mathcal E(\rho^r_j)=\mathcal E(\rho^\ell_j)=[\eta_{\mathrm l}-z_j]_+$, hence $\rho^r_j=\rho^\ell_j$. Mass fluxes, convection fluxes and pressure plus source then vanish, and equilibria with dry areas are preserved exactly. The positive part is essential in the dry area (§2.2, p. 1271). **Proved**
8. The Doyen–Gunawan staggered shallow-water scheme (25), which upwinds on the material velocity, is well-balanced for lakes at rest without dry areas. Its well-balancing relies on its specific fluxes and on the shallow-water pressure law (Remark 2.2). **Derived**
9. Under the CFL condition $\frac{\Delta t}{\Delta x_{j+1/2}}\big([\lambda^+(\rho_{j+1/2},v_{j+1})]_++[\lambda^-(\rho_{j+1/2},v_j)]_-\big)\le1$ (as printed; see Printed slips), with $\lambda^\pm=v\pm c$, the scheme (18) keeps densities non-negative. The proof uses $\rho^\ell_{j+1}\le\rho_{j+1/2}$, $\rho^r_j\le\rho_{j+1/2}$ and the monotonicity of $\rho\mapsto\pm\mathcal F^\pm$ (§2.2, p. 1272). **Proved** (concluded by reference to Prop. 3.7 of the earlier work)
10. The semi-discrete scheme (26) satisfies an internal-plus-potential energy inequality (34) and a kinetic energy inequality (35). Summing (34) and the mean of (35) at $j$ and $j+1$ gives the semi-discrete entropy inequality $\frac{d\eta_{j+1/2}}{dt}+\frac1{\Delta x_{j+1/2}}(H_{j+1}-H_j)\le0$, with $\eta_{j+1/2}$ the discrete total energy (§2.2, pp. 1272–1275). **Proved**
11. Key lemma (31): for hydrostatic states built with $z^*=\max(z_1,z_2)$, the source-free inequality (30) of the earlier work carries over to the reconstructed states. It follows from Lemma 4.4 of that work plus the two case-split inequalities (32)–(33) (p. 1273). **Proved**
12. A fully discrete entropy inequality is open. For collocated hydrostatic-reconstruction schemes it holds only up to an error that vanishes with the mesh (Audusse et al. 2016) or with ad hoc artificial viscosity (Berthon et al. 2019) (p. 1275). **Stated**
13. The second-order version reconstructs $\rho$ and $\mathcal E(\rho)+z$ linearly. It derives interface topographies $z^\pm_j$ and $z^{ml}_j=\max(z^-_j,z^+_j)$ and reconstructed densities $\rho^{ml,r/\ell}_j$. It uses the corrected source (36), $S^{ml}_j=p(\rho^r_j)-p(\rho_{j+1/2})-p(\rho^\ell_j)+p(\rho_{j-1/2})+\tfrac12(\rho^r_j-\rho^\ell_j)\lvert\delta z_j\rvert$, built on the first-order reconstructions (§2.3). **Derived**
14. Putting $\rho^{ml,r/\ell}_j$ directly into the source gives an inconsistent approximation, because $z^\pm_j$ are two second-order approximations of $z$ at the same point $x_j$ (§2.3, p. 1276). **Stated**
15. For shallow water with $\min(\rho_{j-1/2},\rho_{j+1/2})\ge\lvert\delta z_j\rvert$, $S^{ml}_j$ reduces exactly to the centred $\tfrac12(\rho_{j+1/2}+\rho_{j-1/2})\delta z_j$ of Remark 2.2, a second-order approximation. For general pressure laws $S^{ml}_j/\Delta x_j$ is second-order accurate when $\min(\mathcal E(\rho_{j\pm1/2}))\ge\lvert\delta z_j\rvert$, and equals $\tfrac12(\rho_{j-1/2}+\rho_{j+1/2})\delta z_j+o(\lvert\delta z_j\rvert)$ otherwise (§2.3, p. 1277). **Derived**
16. The second-order scheme preserves equilibria without dry areas. With dry areas it preserves them through two limiter properties and a four-case argument (§2.3, pp. 1277–1278). **Proved**
17. Both schemes keep the lake at rest without dry area to machine precision for $\gamma\in\{1.4,2,3,4\}$ and $\Delta x\in\{1,0.1,0.01\}$ up to $T=1500$. The errors are smaller for $\gamma=1.4$ and on coarser meshes (§3.1, Fig. 3). **Shown**
18. The same holds for the lake at rest with a dry zone on top of the bump, up to $T=1000$ (§3.1, Fig. 5). **Shown**
19. From constant initial density ($\gamma=2$) the solution converges to the equilibrium to machine precision by $T=10000$, faster on coarser meshes; the authors attribute this to larger numerical diffusion. With a dry area the decay is first exponential, then much slower (§3.1, Figs. 4, 6). **Shown**
20. On LeVeque's perturbed lake the second-order scheme is clearly better than the first-order one at $\Delta x=10^{-2}$, against a reference at $4\times10^{-4}$. A reflected perturbation forms when the right-going wave crosses the bump; it is larger for $\gamma$ close to 1 and almost vanishes for $\gamma=3$ (§3.2, Figs. 7–9). **Shown**
21. Moving-water steady states are not preserved exactly. The discretization error is proportional to the mesh size and is visible on the discharge $\rho v$ (§3.3, p. 1285). **Stated** and **Shown** (Figs. 11–12, 18)
22. For $F_0=0.2$ and $F_0=1.9$ (subcritical and supercritical, $M_c<M_0$) the MUSCL version is second-order accurate in $L^1$ for velocity and height (§3.3.1, Fig. 13). **Shown**
23. For $F_0=0.3$ (stationary shock) and $F_0=0.7$ (moving shock) the constant states and profiles match the asymptotic reference. Extra transient structures near the upstream shock and the downstream rarefaction vanish at later times ($T=100$, 250, 2000) (§§3.3.2–3.3.3, Figs. 14–17). **Shown**
24. Castro et al. Test 1 (smooth, $t=100$): the discharge oscillations are of order $\Delta x$, or $\Delta x^2$ at second order, and the $L^1$ residual confirms first- and second-order convergence. On Test 2 (transcritical with a shock, $t=200$) the second-order scheme improves accuracy but does not reach second order, because of the shock and the limiter (§3.3.4, Figs. 18–21). **Shown**
25. Wet/dry fronts over a step (Gallouët, Hérard & Seguin): both schemes capture the formation and propagation of the dry bed created by two receding rarefactions, also over the step (§3.4, Figs. 22–23). **Shown**
26. The scheme extends directly to 2D Cartesian (MAC-type) grids by applying the hydrostatic reconstruction row by row and column by column. On the 2D Thacker paraboloid the $L^1$ errors at $T=4\pi$ give an observed order of 1.8 for the MUSCL version (§3.5, Fig. 24). **Shown**

# Printed slips

- p. 1269, shallow-water equilibrium relations: printed $\rho^r_j=\rho_{j+1/2}-[\delta z_j]_-$. From (14)–(15) with $\mathcal E(\rho)=\rho$: if $\delta z_j\le0$ then $z_j=z_{j-1/2}$ and $\rho^r_j=\rho_{j+1/2}+\delta z_j=\rho_{j+1/2}+[\delta z_j]_-$; if $\delta z_j\ge0$ then $\rho^r_j=\rho_{j+1/2}$. The companion $\rho^\ell_j=\rho_{j-1/2}-[\delta z_j]_+$ is correct, and (19) holds in both sign cases with the corrected $\rho^r_j$ *(compiler check, not in the sources)*.
- p. 1269, before (20): the condition is printed "$\mathcal E(\rho_{j+1/2})\ge\delta z_j$", which should read $\ge\lvert\delta z_j\rvert$ (the preceding sentence has $\ge-\delta z_j$).
- p. 1267: the kinetic fluxes are printed as $\mathcal F^\pm(\rho,v)=\int_{\pm\xi>0}M_{\rho,v}(\xi)\,d\xi$ with $M_{\rho,v}=\frac1{2c}\mathbf 1_{\lvert\xi-v\rvert\le c}$. This integral is a dimensionless fraction. Recovering (6), $\frac{\rho}{4c}(v+c)^2$ for $\lvert v\rvert\le c$, needs the integrand $\rho\,\xi\,M_{\rho,v}(\xi)$ *(compiler check, not in the sources)*.
- p. 1271: "the positive part in the definiton (14) of $\rho^r_j$ and $\rho^\ell_j$". The positive part is in (15)–(16); (14) defines $z_j$.
- p. 1272, positivity CFL: printed with $+[\lambda^-(\rho_{j+1/2},v_j)]_-$, where $[\cdot]_-=\min(0,\cdot)\le0$. From (6)–(7), $\mathcal F^+(\rho,v)\le\rho[\lambda^+]_+$ and $\mathcal F^-(\rho,v)\ge\rho[\lambda^-]_-$. The displayed lower bound then gives $\bar\rho_{j+1/2}\ge\rho_{j+1/2}\big(1-\frac{\Delta t}{\Delta x_{j+1/2}}([\lambda^+]_+-[\lambda^-]_-)\big)$, so the condition needs $-[\lambda^-]_-$. As printed it is weaker than the argument requires *(compiler check, not in the sources)*.
- p. 1277: the restated $S^{ml}_j$ carries $-\tfrac12(\rho^r_j-\rho^\ell_j)\lvert\delta z_j\rvert$ where (36) has $+$. The expansions that follow and the shallow-water reduction require the $+$ of (36).
- p. 1277, shallow-water consistency: printed $S^{ml}_j=\frac{\rho_{j+1/2}+\rho_{j+1/2}}2(z_{j+1/2}-z_{j-1/2})$. It must be $\rho_{j+1/2}+\rho_{j-1/2}$, as (19) plus the correction of (36) gives *(compiler check, not in the sources)*.
- p. 1277: the expansion block ends with "$S_j=\ldots$" where $S^{ml}_j$ is meant.
- p. 1286, Fig. 10 caption: "(a) $M_c<M_0$ and $F_0>1$. (b) (b) $M_c<M_0$ and $F_0>1$." By the text (p. 1283), (a) is the $F_0<1$ case, and "(b)" is doubled.
- p. 1286: the text gives $\Delta x=0.05$ for Figs. 11–12, the Fig. 12 caption $0.04$.
- p. 1287: the text announces final times $T=100$, 250 and 2000 for Figs. 15–16, but Fig. 15 shows $T=100,250,1000$ and Fig. 16 $T=250,1000,2000$. Figs. 15–16 use $\Delta x=0.2$, Fig. 14 $\Delta x=0.1$.
- pp. 1279–1280: the "constant density" datum is printed $\rho_{j+1/2}=\sum_k\delta x_{k+1/2}\rho_{eq}(x_{k+1/2})$. This sum is the total mass on $[0,20]$, not a density; the mean density is the sum divided by the domain length 20 *(compiler check, not in the sources)*.
- Fig. 13 and §3.3.1 speak of the "height $h$", while the paper's variable is $\rho$. $\eta$ denotes both the equilibrium level (2) and the discrete entropy $\eta_{j+1/2}$ (p. 1275).
- Typos: "garanties", "discetizations", "resconstructions", "slowlier", "bassin", "conserrvation" (ref. [21]).

# Notation map

| Goudon & Minjeaud 2024 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $u$ | $\rho$, $v$ | density (water depth for shallow water), velocity |
| $p(\rho)=\kappa\rho^\gamma$ | $p(\rho)$ | barotropic law; tests use $p=g\rho^\gamma/\gamma$. **Collision**: the source's $\kappa$ is a constant, registry $\kappa$ the kinetic energy; $\gamma$ is the barotropic exponent |
| $c(\rho)=\sqrt{p'(\rho)}$, $\lambda^\pm=u\pm c$ | $c$, $\lambda_1,\lambda_2$ | sound speed and eigenvalues; agree |
| $z$ | $z$ (local) | potential, bottom topography |
| $\mathcal E(\rho)$ | $\mathcal E(\rho)$ (local) | equilibrium (enthalpy-like) potential, $\mathcal E'=p'/\rho$, as on the well-balancing, MUSCL and flow-over-a-bump pages; **collision** with the vortex strength $\mathcal E$, which those pages do not use |
| $\eta$ (level) | $\eta_{\mathrm l}$ (local) | free-surface level; **collision** with the entropy $\eta$ |
| $\eta_{j+1/2}$, $H_j$ | $\eta$, $F_\eta$ | discrete total energy as entropy, and its flux; **collision**: $H$ is not the enthalpy |
| $\Phi$ | internal energy (local) | $\rho\Phi'-\Phi=p$, $\Phi'=\mathcal E$ |
| $W=\mathcal E(\rho)+z$ | $\mathcal E(\rho)+z$ | **collision** with the Lorentz factor $W$ |
| $x_j$, $x_{j+1/2}$ | velocity nodes, density-cell centres | **collision**: registry $x_{i+1/2}$ are interfaces; the staggered layout inverts the roles |
| $\delta x_{j+1/2}$, $\delta x_j$, $\delta t$ | $\Delta x_{j+1/2}$, $\Delta x_j$, $\Delta t$ | primal and dual mesh sizes |
| $\mathcal F^\pm$, $\mathcal F_j$ | kinetic split mass fluxes (local) | analogous to the splitting $f^\pm$ |
| $\mathbb F_j$, $\mathbb G_{j+1/2}$, $\Pi_{j+1/2}$, $S_j$ | well-balanced mass and convection fluxes, pressure, discrete source | $S_j$ is an undivided difference in (17)–(18) |
| $\rho^r_j$, $\rho^\ell_j$ | hydrostatic reconstructions from $\rho_{j+1/2}$ and $\rho_{j-1/2}$ | |
| $[a]_+$, $[a]_-$ | $\max(0,a)$, $\min(0,a)$ | |
| $M_{\rho,u}(\xi)$ | — | uniform "Maxwellian" of half-width $c$; $\xi$ a microscopic velocity, **collision** with the nodes $\xi_j$ |
| $\pi$, $\tilde\pi$, $\nu$ | MUSCL slopes of $\rho$, $\mathcal E(\rho)+z$, $v$ | **collision**: registry $\nu$ is the CFL number |
| $C_{\delta t}$ | $\nu$ | CFL constant, 0.5 or 0.4 |
| $F_0$, $M_0$, $M_c$, $Z_c$ | Froude number and Houghton–Kasahara constants | |
| $q=\rho u$ | discharge $\rho v$ | **collision** with the exponent $q$ |

# Reference list

The paper prints 69 references, numbered [1]–[69] in alphabetical order; no DOIs
are printed. The list is merged complete into the [bibliography](/bibliography.md)
with `citedby` including `goudon-2024`. [16] (the CALIF3S library) prints no
author, year or URL. [9] is a CEMRACS technical report dated 2023, [48] an NCAR
manuscript of 1967, [25] an AIAA paper and [26] a NASA technical paper.
Same-author same-year works take suffixes in printed order (Deshpande 1986,
Goudon 2020, Herbin 2021). No item is unparseable.

# Pages created or updated

Chunk 7 (2026-10-23), cited further in chunks 8–10 (2026-10-23). This source is cited on:

* [Bound preservation](/properties/bound-preservation.md)
* [Entropy stability](/properties/entropy-stability.md)
* [MUSCL and MUSCL–Hancock schemes](/methods/muscl-hancock.md)
* [Shallow-water flow over a bump and lake at rest](/benchmarks/flow-over-a-bump.md)
* [Well-balancing](/properties/well-balancing.md)

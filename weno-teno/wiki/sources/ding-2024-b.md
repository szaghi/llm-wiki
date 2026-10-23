---
type: Source
title: "Ding & Wu (2024) — GQL-based bound-preserving and locally divergence-free central discontinuous Galerkin schemes for relativistic magnetohydrodynamics"
description: "Arbitrary-order central DG schemes on overlapping meshes for special relativistic MHD with a general equation of state, proved bound-preserving through geometric quasilinearization; in 2D locally divergence-free spaces and a discretized symmetrization source cancel the divergence error, and the optimal cell-average decomposition is extended to overlapping meshes."
resource: "doi:10.1016/j.jcp.2024.113208"
source_kind: paper
authors: [Ding S., Wu K.]
year: 2024
venue: "J. Comput. Phys. 514:113208"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Journal_of_Computational_Physics_Ding_GQL-based_bound-preserving_and_locally_divergence-free_centr.pdf"
tags: [dg, relativistic, mhd, bound-preserving, central-scheme]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper builds central [discontinuous Galerkin](/methods/discontinuous-galerkin.md)
(CDG) schemes of arbitrary order for special
[relativistic MHD](/definitions/relativistic-hydrodynamics.md) with a general
equation of state satisfying a Taub-type inequality and causality. CDG
evolves two copies of the solution, on a primal mesh and on a dual mesh
shifted by half a cell, and evaluates fluxes where the other copy is
continuous, so no Riemann solver is needed. The schemes are provably
[bound-preserving](/properties/bound-preservation.md): updated cell averages
keep $D>0$, $p>0$ and $\lvert v\rvert<1$. Every proof runs through the
[geometric quasilinearization](/methods/geometric-quasilinearization.md) (GQL)
form of the admissible set, whose constraints are linear in $u$; the authors
call it essential, because the standard technique, as they call it, of
splitting a multidimensional scheme into formally 1D bound-preserving schemes
does not apply here.

In 1D, CDG keeps $B_1$ exactly constant and bound preservation holds under
$\tau_{\max}\le\tfrac{\varpi}2\Delta x$ when the point values on the
Gauss–Lobatto nodes of both half-cells are admissible, which a three-step
[Zhang–Shu-type scaling limiter](/methods/zhang-shu-scaling-limiter.md)
enforces. In 2D the authors discretize the symmetrizable modified RMHD system,
the relativistic analogue of Godunov's form, with
[locally divergence-free](/properties/divergence-free-magnetic-field.md)
spaces for $(B_1,B_2)$ and a source built from the jump of the normal field
across the interior lines of the other mesh's cell. In the proof the
divergence-error terms of fluxes and source cancel exactly on the four quarter
cells; without the source, bound preservation needs globally coupled discrete
divergence-free conditions that the local limiter does not keep. The
[optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
of Cui, Ding and Wu is extended to overlapping meshes by quarter-cell
splitting, which gives a milder CFL bound than the Zhang–Shu decomposition
($\varpi=1/4$ against $1/6$ for degree 2 and 3).

$\mathbb P^2$ CDG with SSP-RK3 and four equations of state reaches third order
on [circularly polarized Alfvén waves](/benchmarks/circularly-polarized-alfven-wave.md)
and runs three 1D Riemann problems (Lorentz factor 223.61, pressure jump about
$10^{12}$), the [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), a
rotor, a [shock–cloud interaction](/benchmarks/mhd-shock-cloud-interaction.md),
[blast waves](/benchmarks/mhd-blast-wave.md) up to $B_a=2000$ and Mach-50
[jets](/benchmarks/high-mach-astrophysical-jet.md); removing the limiter (or,
for the jets, the source or the locally divergence-free spaces) makes the
runs fail.

# Version read

Version of record (Elsevier typeset, J. Comput. Phys. 514 (2024) 113208),
38 pages, all read; pp. 4, 5, 12, 15–17, 20, 23 and 27 read visually because
the text extraction drops the script letters and the jump brackets. Page 1
matches Crossref (title, authors, venue, DOI). Equation, theorem, table and
example numbers cited here are those of this version.

# Key claims

Registry notation (see the notation map): the source's polynomial degree $k$
is $N$, its CAD boundary weight $\bar\omega$ is $\varpi$, its anisotropy
$\delta$ is $\varkappa$, its GQL auxiliary variables $v^*$, $B^*$, $n^*$ are
$v_*$, $B_*$, $n_*$, its Gauss–Lobatto point count $L$ is $N_{\mathrm{GL}}$
with endpoint weight $1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$, its CFL number
$C_{\rm cfl}$ is $\nu$.

1. Theorem 3.1: in 1D the CDG scheme (17)–(18) for conservative RMHD keeps the primal and dual cell averages in $G$ if the point values on the $N_{\mathrm{GL}}$-point Gauss–Lobatto nodes of both half-cells are admissible (26), the discrete divergence-free condition (27) holds, and $0<\tau_{\max}\le\tfrac{\varpi}{2}\Delta x$ with $\Delta t=\theta\tau_{\max}$, $\theta\in(0,1]$ (29) (§3.2). **Proved**
2. In 1D the $B_1$ component of the flux vanishes identically, so fully discrete CDG with SSP stepping keeps $B_1$ exactly constant on both meshes and (27) holds automatically (Remark 3). **Derived**
3. Bound preservation of the forward-Euler step carries over to SSP time stepping, a convex combination of forward-Euler steps (Remark 2, §4.5). **Stated**
4. The three-step 1D limiter (density, then $E-\sqrt{D^2+\lvert m\rvert^2}$, then the $\varepsilon$-shrunk constraint $\Phi_\varepsilon$) keeps (27), and limiters of this type "may not destroy" high-order accuracy (Remark 4). **Stated** (accuracy **Shown** in Example 5.1)
5. The limiter must also enforce admissibility at the Gauss flux-quadrature points, not only at the Gauss–Lobatto nodes of Theorem 3.1, otherwise the primitive-variable recovery needed for the flux can fail; this does not arise in non-relativistic MHD (Remark 6). **Stated**
6. Theorem 4.1: the 2D locally divergence-free CDG scheme (37)–(38) for the modified RMHD system (7) is bound-preserving, given a feasible 2D cell-average decomposition (57) on overlapping meshes, admissible point values on its node set (61) and $0<\tau_{\max}\big(\tfrac{\alpha_1}{\Delta x}+\tfrac{\alpha_2}{\Delta y}\big)\le\tfrac{\varpi}{2}$ (62), with $\alpha_\ell=\max\{1,\beta_\ell\}$ and $\beta_\ell$ the largest normalized normal-field jump (63) (§4.4). **Proved**
7. In the proof the flux term contributes $-(v_*\cdot B_*)\,\mathrm{div}_{ij}B^J_h$ and the source term $+(v_*\cdot B_*)\,\mathrm{div}_{ij}[\![B^J_h]\!]$; their difference is $-\frac1{\Delta x\Delta y}\sum_{m,\sigma}\iint_{\Omega_{i+m/4,j+\sigma/4}}\nabla\cdot B^J_h=0$, by Gauss-quadrature exactness, the divergence theorem on the quarter cells and local divergence-freeness (Eqs. (70)–(74)). **Proved**
8. Theorem 4.2: without the symmetrization source, the locally divergence-free scheme (78) only gives $\bar u^{I,\mathcal H,\Delta t}_{ij}\cdot n_*+p^*_m>-\Delta t(v_*\cdot B_*)\,\mathrm{div}_{ij}B^J_h$ under (79), so bound preservation needs the stronger, globally coupled discrete conditions $\mathrm{div}_{ij}B^J_h=0$ and $\mathrm{div}_{i+1/2,j+1/2}B^I_h=0$ (83) (§4.7). **Proved**
9. Conditions (83) hold for globally divergence-free fields (locally divergence-free with continuous normal component), but the local scaling limiter is incompatible with global divergence-freeness; enforcing (83) and (61) together without losing accuracy and conservation is "unresolved" (§4.7). **Stated**
10. Corollary 4.1: with the Zhang–Shu decomposition the 2D bound is $\tau_{\max}(\alpha_1/\Delta x+\alpha_2/\Delta y)\le\tfrac12\cdot\tfrac1{N_{\mathrm{GL}}(N_{\mathrm{GL}}-1)}$, $N_{\mathrm{GL}}=\lceil(N+3)/2\rceil$: $\varpi=1/6$ for $N=2,3$, $1/12$ for $N=4,5$, $1/20$ for $N=6,7$ (Eq. (76)). **Proved** (consequence of Theorem 4.1)
11. Corollary 4.2: with the Cui–Ding–Wu decomposition the bound is $\varpi_\star(\varkappa,\mathbb P^N)/2$ with $\varkappa=(\alpha_1\Delta y-\alpha_2\Delta x)/(\alpha_1\Delta y+\alpha_2\Delta x)$, in closed form for $N\le7$; at $\varkappa=0$, $\varpi_\star=1/4$ ($N=2,3$), $2-\sqrt{14}/2\approx0.1292$ ($N=4,5$), $1-\sqrt{30}/6\approx0.08713$ ($N=6,7$). **Proved** (via Cui, Ding and Wu's theorems) *(compiler check, not in the sources: the general $N=4,5$ and $N=6,7$ formulas at $\varkappa=0$ evaluate to $0.129171$ and $0.087129$, equal to the printed closed forms.)*
12. The Cui–Ding–Wu decomposition gives a milder CFL constraint and needs fewer internal nodes than the Zhang–Shu one (one merged node at $\varkappa=0$ for $N=2$, against six), so it is used in all 2D tests (§4.6, Example 4.2, Fig. 1). **Stated**
13. $\beta_\ell$ is proportional to the normal-field jump at cell interfaces, at truncation-error level in smooth regions and observed much smaller than 1 in all tests, so $\alpha_\ell=1$ and $\varkappa=0$ for $\Delta x=\Delta y$ (Remark 9). **Stated** (observation, no data shown)
14. The 2D limiter keeps the locally divergence-free property (Remark 8). **Stated**
15. The GQL approach is "essential": the locally divergence-free constraint couples the interface states, so splitting the multidimensional scheme into formally 1D bound-preserving schemes does not work for RMHD (§1, §4.4). **Stated**
16. The theoretical CFL condition is sufficient, not necessary; all tests use $\nu=0.25$ with $\Delta t=\nu\Delta x$ (1D) and $\Delta t=\nu/(1/\Delta x+1/\Delta y)$ (2D) (§5). **Shown** *(compiler check, not in the sources: with $\varpi_\star=1/4$ and $\alpha_\ell=1$, Corollary 4.2 allows $\Delta t\le\tau_{\max}\le\tfrac18/(1/\Delta x+1/\Delta y)$, and Theorem 3.1 with $\varpi=1/6$ allows $\Delta t\le\Delta x/12$ in 1D, so the tests run above the proved bounds; $\tau_{\max}$ and $\theta$ of the runs are not stated.)*
17. $\mathbb P^2$ CDG with the limiter reaches third order: the 1D $v_2$ $l^1$ error falls from 6.53e-05 ($N_x=20$) to 1.96e-09 ($N_x=640$), the 2D $B_2$ $l^1$ error from 1.92e-03 ($20^2$) to 3.07e-08 ($640^2$), at order 3.00; limiter and source do not degrade accuracy (Example 5.1, Tables 1–2). **Shown**
18. 1D Riemann problems I–III (ideal, RC and IP equations of state, 1000 cells) agree with a first-order Lax–Friedrichs reference on 400,000 cells; without the limiter the code fails "after a few time steps" (Examples 5.2–5.4, Figs. 3–5). **Shown**
19. Orszag–Tang ($600^2$): without the limiter the code fails at $t\approx2.196$; the relative global divergence error stays $O(10^{-4})$, the local one zero (Example 5.5, Figs. 6–7). **Shown**
20. Shock–cloud interaction ($560\times400$): without the limiter the code fails at the first step; global divergence error about $10^{-5}$, local zero (Example 5.7, Figs. 7, 9). **Shown**
21. Blast waves ($B_a=0.1$, $0.5$, $2000$, $400^2$): robust with the limiter, failure without it, local divergence error exactly zero (Example 5.8, Figs. 10–11). **Shown**
22. RMHD jets ($M_b=50$, $W\approx7.09$, $M_r\approx354.37$, $\beta_{\mathrm p}=0.001$): the code "would quickly break down" without any one of the limiter, the symmetrization source or the locally divergence-free spaces (Example 5.9, Figs. 12–14). **Shown** (failure runs described, not displayed)
23. The ideal equation of state "provides a poor approximation for most relativistic flows", being inconsistent with relativistic kinetic theory; all four equations of state used satisfy the Taub-type inequality and causality (§5). **Stated** (citing earlier work)
24. For the conservative RMHD system, bound preservation of finite-volume and non-central DG schemes is tied to a discrete divergence-free condition, and exact solutions may lose it when $\nabla\cdot B\ne0$, so the system "may be ill-posed outside the DF regime"; the modified system stays bound-preserving without it (§1). **Stated** (citing Wu and Wu & Shu)
25. The discrete divergence-free condition of CDG on overlapping meshes is "distinct from the one" for non-central DG (§1). **Stated**

# Printed slips

- Lemma 2.2, Eq. (12): $p^*_m=\tfrac12\big((1-\lvert v^*\rvert^2)B^*+(v^*\cdot B^*)^2\big)$
  is printed with the vector $B^*$ where a scalar is needed; by analogy with
  $p_m=\tfrac12\big((1-\lvert v\rvert^2)\lvert B\rvert^2+(v\cdot B)^2\big)$
  (p. 2) it should read $\lvert B^*\rvert^2$.
- Examples 5.2–5.4: the right state is given for "$0.5<x\le0.5$", an empty
  set; the stated domain is $[0,1]$. The axes of Figs. 3–4 are labelled from
  $-0.5$ to $0.5$, and Example 5.4 reports wall heating "around $x=0$"; neither
  agrees with the domain $[0,1]$ and an interface at $x=0.5$.
- §3.1 (p. 6) and pp. 11–13: the dual cells are written $I_{j+1/2}$,
  $I_{i+1/2,j+1/2}$ in the spaces $\mathbb P^k(\cdot)$ and $\mathbb B^k(\cdot)$
  and in Eq. (20), while they are named $J_{j+1/2}$, $J_{i+1/2,j+1/2}$
  elsewhere.
- §4.7: "if we remove the systematization sources" (symmetrization); the
  section title "Why we need the symmetrization source terms bound
  preservation?" lacks "for".
- Proof of Corollary 2.1: "$\pm F_\ell\cdot n_1=\pm v_lD$" writes $l$ for $\ell$.

# Notation map

| Ding & Wu (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol U=(D,\boldsymbol m,\boldsymbol B,E)$ | $u=(D,m,B,E)$ | lab-frame conserved variables, $u\in\mathbb R^8$ in every dimension |
| $\boldsymbol W=(\rho,\boldsymbol v,\boldsymbol B,p)$, $W$ | kept, $W$ | primitive vector and Lorentz factor; **same letter, bold and italic** |
| $\boldsymbol F_i$ | $f^{(i)}$ | fluxes |
| $h$, $e$, $p_m$, $p_{tot}$ | kept | specific enthalpy (with rest mass), internal energy, magnetic and total pressure |
| $\Gamma$ | $\gamma$ | adiabatic index of the ideal equation of state |
| $\xi=\rho hW^2$ | kept locally | unknown of the primitive recovery (Eq. (9)); **$\xi$ also the local coordinate $\xi_{j_0}$ and the registry's reference nodes** |
| $\mathcal G$, $\mathcal G_*$, $\mathcal G_\varepsilon$, $\Phi_\varepsilon$ | $G$; kept | admissible set, its GQL form, $\varepsilon$-shrunk set and constraint; **$\varepsilon$ kept to leave $\epsilon$ to the weight regularization** |
| $\boldsymbol n_1$, $\boldsymbol n^*$, $\boldsymbol v^*$, $\boldsymbol B^*$ | $n_1$, $n_*$, $v_*$, $B_*$ | GQL normals and free auxiliary variables, as on the GQL page |
| $p^*_m$ | kept | auxiliary magnetic pressure of the GQL constraint |
| $q(\boldsymbol U)$, $\Phi(\boldsymbol U)$ | $g_i(u)$ | explicit constraint functions (Eq. (33)); **$q$ collides with the weight exponent** |
| $\boldsymbol S(\boldsymbol U)$ | kept | symmetrization source, $-(\nabla\cdot B)S$; **not the registry's balance-law source $S(u)$** |
| $I_j$, $J_{j+1/2}$; $\boldsymbol U^I_h$, $\boldsymbol U^J_h$ | kept | primal and dual cells and CDG solutions |
| $k$ | $N$ | polynomial degree, order $N+1$ |
| $\mathbb B^k$ | kept | divergence-free subspace of $[\mathbb P^N]^2$ |
| $\tau_{\max}$, $\theta$ | kept | CDG dissipation parameter and $\Delta t/\tau_{\max}$; **$\theta$ is the Zhang–Shu factor in the registry** |
| $\theta_1$, $\theta_2$, $\theta_3$ | $\theta$ | scaling factors of the three limiter steps |
| $Q=k+1$, $\omega_\mu$ | kept, $\mathsf w_\mu$ | Gauss points per half-cell segment and weights; **$Q$ is the SBP matrix in the registry** |
| $L$, $\hat\omega_1$ | $N_{\mathrm{GL}}$, $\varpi$ | Gauss–Lobatto point count and endpoint weight $1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$; **$L$ is the left-eigenvector matrix in the registry** |
| $\bar\omega$, $\bar\omega_\star$, $\tilde\omega_s$ | $\varpi$, $\varpi_\star$, $\mathsf w_s$ | boundary weight (optimal), internal weights of the cell-average decomposition |
| $\lambda_1$, $\lambda_2$, $\delta$ | kept, kept, $\varkappa$ | direction weights and anisotropy $\in[-1,1]$; **$\lambda$ collides with eigenvalues** |
| $\alpha_\ell$, $\beta_\ell$ | kept | CFL factors from normal-field jumps; **collide with $\alpha_k$, $\beta_k$** |
| $[\![\cdot]\!]$, $\{\{\cdot\}\}$ | $[\![\cdot]\!]$, $\{\!\{\cdot\}\!\}$ | jump (right minus left) and arithmetic mean; agree |
| $\mathcal L$, $\mathcal H$, $\mathcal S$ | $\mathcal L$; kept | cell-average right-hand side, its flux and source parts |
| $\varepsilon^{\rm global}_{\rm div}$, $\varepsilon^{\rm local}_{\rm div}$ | kept | relative divergence errors (Eqs. (90)–(91)) |
| $C_{\rm cfl}$ | $\nu$ | 0.25 in all tests |
| plasma beta | $\beta_{\mathrm p}$ | |
| $M_b$, $M_r$ | kept | jet-beam Mach number and relativistic Mach number of Example 5.9 |

# Reference list

64 printed references, numbered Elsevier style ([1]–[64]), all parsed and
merged complete into the [bibliography](/bibliography.md) with `citedby`
`ding-2024-b`. Two arXiv preprints ([54] Cai, Qiu & Wu 2024; [64] Peng, Sun &
Wu 2023, OEDG) are kept as their own entries. Refs. [9], [13] and [35] print no
pages or article number, ref. [50] no volume. No printed duplicates and no
unparseable items.

# Pages created or updated

Chunk 8 (2026-10-23). This source is cited on:

* [Bound preservation](/properties/bound-preservation.md)
* [Circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Geometric quasilinearization (GQL)](/methods/geometric-quasilinearization.md)
* [High-Mach astrophysical jets](/benchmarks/high-mach-astrophysical-jet.md)
* [MHD blast wave and rotor](/benchmarks/mhd-blast-wave.md)
* [MHD shock–cloud interaction](/benchmarks/mhd-shock-cloud-interaction.md)
* [Optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)
* [Oscillation-eliminating discontinuous Galerkin (OEDG)](/methods/oedg.md)
* [Special relativistic hydrodynamics and MHD](/definitions/relativistic-hydrodynamics.md)
* [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)

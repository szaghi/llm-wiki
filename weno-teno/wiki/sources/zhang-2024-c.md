---
type: Source
title: "Zhang & Zhu (2024) — Finite difference and finite volume ghost multi-resolution WENO schemes with increasingly higher order of accuracy"
description: "Ghost multi-resolution WENO (GMR-WENO) of orders three, five and seven builds one polynomial on one central stencil in a cell-local Legendre basis and takes its lower-degree truncations as candidates, combined CWENO-style with WENO-Z-type weights; errors match MR-WENO at orders five and seven at lower CPU cost."
resource: "doi:10.1016/j.jcp.2024.112890"
source_kind: paper
authors: [Zhang Y., Zhu J.]
year: 2024
venue: "J. Comput. Phys. 504:112890"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Journal_of_Computational_Physics_Zhang_Finite_difference_and_finite_volume_ghost_multi-resolution_W.pdf"
tags: [weno, cweno, reconstruction, finite-difference, finite-volume]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

Zhang & Zhu (2024) simplify the [multi-resolution WENO](/methods/multi-resolution-weno.md)
(MR-WENO) of Zhu & Shu (2018) into **ghost multi-resolution WENO (GMR-WENO)** of orders $K=3,5,7$,
in finite-difference form (flux reconstruction from split point fluxes,
[Lax–Friedrichs splitting](/methods/lax-friedrichs-flux.md)) and finite-volume form (Gauss
quadrature on the faces in 2D). MR-WENO builds a polynomial on each of a hierarchy of nested
central stencils. GMR-WENO builds **one** polynomial $P_{\mathrm{opt}}$ of degree $K-1$ on **one**
central stencil of $K$ cells, written in a Legendre basis orthogonal on the target cell $I_i$. Its
$L^2(I_i)$ projections onto degrees $K-2,\dots,0$ are the "ghost" candidates; by orthogonality they
are truncations of the Legendre expansion. The hierarchy therefore descends one degree at a time,
and every candidate has cell average $\bar u_i$.

The candidates are combined in the [CWENO](/methods/cweno.md) form, so any positive linear weights
summing to one are admissible; the paper uses $10:5:1$, $100:25:10:5:1$ and
$1000:125:100:25:10:5:1$. Jiang–Shu-type [smoothness indicators](/definitions/smoothness-indicator.md)
on $I_i$ and [WENO-Z](/methods/weno-z.md)-type weights follow, with SSP Runge–Kutta 3 at CFL 0.6.

The evidence is numerical. On [Burgers tests](/benchmarks/burgers-equation-tests.md) and
[density-wave advection](/benchmarks/density-wave-advection.md) GMR-WENO5 and GMR-WENO7 give errors
identical to MR-WENO5 and MR-WENO7 to the printed digits, while GMR-WENO3 errors are about half those
of MR-WENO3. The CPU-time ratio GMR:MR lies between 1:1.23 and 1:2.25 on the
[Shu–Osher](/benchmarks/shu-osher-problem.md) and Titarev–Toro problems,
[Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md), the
[Sedov blast wave](/benchmarks/sedov-blast-wave.md),
[double Mach reflection](/benchmarks/double-mach-reflection.md) and
[shock–vortex interaction](/benchmarks/shock-vortex-interaction.md), where GMR-WENO is judged
visually equal or better. No theorem is proved, and no spectral analysis backs the claimed
"high spectral resolutions".

# Version read

Version of record (Elsevier typeset; received 3 August 2023, accepted 25 February 2024, online
29 February 2024), 24 pages, all read; the reconstruction formulas on pp. 3–5 checked visually.
Page 1 matches Crossref (title, two authors, venue, DOI). Numbering cited here is that of this
version.

# Key claims

Registry notation: the source's $h$ is $\Delta x$, its order $k$ is $K$, its input $\bar w_j$ is
$\bar u_j$ (or $f^+(u_j)$ in finite differences), its $P^{(k)}_1$ is $P_{\mathrm{opt}}$ and its
ghost $P^{(k)}_\ell$ is $P_\ell$ ($\ell=2,\dots,K$, degree $K-\ell$), its Legendre $L_r$ are
$\mathsf L_r$ with coefficients $\hat u_r$ (page-local), its $d^{(k)}_r$, $\beta^{(k)}_r$,
$\bar\omega^{(k)}_r$, $\omega^{(k)}_r$ are $d_\ell$, $\beta_\ell$, $\alpha_\ell$, $\omega_\ell$, and
its $\tau_k$ is $\tau_K$.

1. GMR-WENO uses one central stencil only ($3$, $5$ or $7$ cells for orders 3, 5, 7) "without introducing any equivalent multi-resolution representations" (Abstract, §1, §2.1). **Stated** (construction)
2. "This is the first time that only one central spatial stencil is utilized in designing high-order finite difference and finite volume WENO schemes" (Abstract). **Stated** (priority claim) *(compiler check, not in the sources: the CWENO reconstructions recorded on [CWENO](/methods/cweno.md), e.g. [Puppo et al. (2023)](/sources/puppo-2023.md), Eqs. (7), (11), also combine one optimal polynomial on a central stencil with lower-degree candidates, which they build on smaller stencils; GMR-WENO's candidates are truncations of the optimal polynomial itself)*
3. The ghost polynomials are the $L^2(I_i)$ projections of $P_{\mathrm{opt}}$; in the orthogonal Legendre basis they are obtained by dropping the top modes, $P_\ell=\bar u_i+\sum_{r=1}^{K-\ell}\hat u_r\mathsf L_r$ (Eqs. 2.12–2.25, Remark 1). **Derived** *(compiler check, not in the sources: the seven printed $\mathsf L_r$ are pairwise orthogonal on $[x_{i-1/2},x_{i+1/2}]$, and solving the cell-average conditions in that basis reproduces every printed coefficient $\hat u_r$ for $K=3,5,7$.)*
4. The linear weights "can be any positive numbers with a summation of one" (Abstract, §2.1 Step 2). **Stated** (follows from the CWENO form, Eq. 2.26, which returns $P_{\mathrm{opt}}$ for any such weights)
5. The schemes reach third, fifth and seventh order in smooth regions (§1; Tables 3.2–3.9). **Shown**
6. Near strong discontinuities the accuracy degrades "gradually" to first order, e.g. "if the three-point central stencil contains strong discontinuities, the accuracy decreases to the second-order or finally to the first-order" (§1, §4). **Stated** (no test isolates the intermediate orders) *(compiler check: every ghost polynomial of degree $\ge1$ depends on all $K$ cell averages, since each $\hat u_r$ of $P_{\mathrm{opt}}$ does, e.g. $\hat u_1$ for $K=5$ involves $\bar u_{i\pm2}$; a discontinuity anywhere in the stencil enters every candidate except the constant $P_K=\bar u_i$.)*
7. "The number of real spatial stencils is smaller than that of classical same order WENO schemes" (§1). **Stated**
8. GMR-WENO3 has smaller errors than MR-WENO3: Burgers, 200 points, $L^1$ $1.27\times10^{-5}$ against $2.25\times10^{-5}$ (Table 3.2); 1D Euler, 140 points, $L^1$ $1.01\times10^{-5}$ against $2.30\times10^{-5}$ (Table 3.6). **Shown**
9. GMR-WENO5 and GMR-WENO7 give $L^1$ errors identical to MR-WENO5 and MR-WENO7 to the printed digits in all accuracy tables, with slightly smaller $L^\infty$ errors in the Euler tests (Tables 3.2–3.9). **Shown**
10. Observed orders of the third-order schemes exceed 3 on the meshes used ($L^1$ 4.35 at 140 points, Table 3.6; 4.53, Table 3.7), while the $L^\infty$ orders on Burgers stay between 2.25 and 3.37 (Table 3.2). **Shown**
11. GMR-WENO needs less CPU time than MR-WENO for a given $L^1$ or $L^\infty$ error (Figs. 3.1–3.8). **Shown**
12. The CPU-time ratio GMR:MR ranges over 1:1.23–1:2.18 (finite difference) and 1:1.27–1:2.25 (finite volume) in Examples 3.5–3.10, e.g. double Mach reflection 10285.53 s against 22286.90 s for GMR-WENO7-FD (Table 3.1; Intel Core i5-8265U, Visual Fortran). **Shown** *(compiler check, not in the sources: all 36 printed ratios agree with the printed times to two decimals.)*
13. GMR-WENO "perform better" than MR-WENO on the Shu–Osher problem, the blast waves and the Titarev–Toro problem (Examples 3.5, 3.6, 3.8). **Shown** (visual comparison only)
14. Both families "work well" on the Sedov blast wave (Example 3.7). **Shown**
15. In double Mach reflection ($1200\times400$) GMR-WENO "resolve two Mach stems well than the MR-WENO schemes do" (Example 3.9). **Shown** (visual)
16. The schemes have "the advantages of low computational costs and high spectral resolutions" (§1, §4). **Stated** (no dispersion or dissipation analysis is presented)
17. The Legendre basis lets the smoothness indicators be written as sums of perfect squares (§2.1 Step 3). **Stated**
18. Accuracy tests use $\Delta t\sim\Delta x^{K/3}$ so that the third-order time error does not dominate (§3). **Stated**
19. An extension to unstructured meshes is announced as ongoing work (§4). **Stated**

# Printed slips

- Eq. (2.27): the indicator sum runs over $\alpha=1,\dots,l$ "where $l=2(r-1)$". With the paper's indexing $P^{(k)}_r$ has degree $k-r$, so $l=2(r-1)$ gives an empty sum for the top polynomial ($r=1$) and too many terms for the low-degree ones; it matches the increasing-degree indexing of MR-WENO. $\beta_r$ is defined for $r=1,\dots,k-1$, while Eq. (2.29) needs $r=1,\dots,k$ ($\beta_k$ is deferred to the cited MR-WENO papers).
- Eq. (2.4): "$L_r(x)$, $r=1,2\dots,6$ are:" precedes a list that starts with $L_0$.
- Tables 3.8 and 3.9: both column groups are headed "MR-WENO3-FD scheme" (and likewise for the other orders and FV); the left groups, with the smaller third-order errors, are GMR-WENO.
- Table 3.1 caption "Examples 3.5-3.9" and the text "from Example 3.5 to Example 3.9", while the table also has rows for Example 3.10.
- Examples 3.3 and 3.4 print the exact solutions as "$\rho(x,0)=1+0.2\sin(x-t)$" and "$\rho(x,0)=1+0.2\sin(x+y-2t)$" (for $\rho(x,t)$, $\rho(x,y,t)$).
- Example 3.6 writes "$(\rho,u,p,\gamma)^T=$" with three-component vectors; $\gamma$ is never given.
- Example 3.8: "The density of the numerical simulation in this example is ten times bigger than the density of the standard shock/turbulence problem [1]". *(Compiler check, not in the sources: the densities are of the same size; the perturbation wavenumber is $20\pi$ against 5, a ratio $4\pi\approx12.6$.)* Ref. [1] is the MP-WENO paper of Balsara & Shu, not the origin of the Shu–Osher problem.
- §1: "In the same year, Balsara et al. [1] designed a WENO-AO scheme"; ref. [1] is the 2000 MP-WENO paper, and the WENO-AO paper is not in the reference list.
- §2.2: "$u^-_{i+1/2,k+\sigma_l}=w_v(y_v+\sigma_lh)$" uses $k$ for $v$.
- "absolute deference" (§2.1 Step 4), "resolve two Mach stems well than" (Example 3.9).

# Notation map

| Zhang & Zhu (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $h$ | $\Delta x$ | same spacing in $y$ |
| $(i,v)$, $J_v$ | $(i,j)$ | $y$ cell index; the source's $j$ is a running stencil index |
| $u_i$, $\bar u_i$, $\tilde{\bar u}_{i,v}$ | $u_i$, $\bar u_i$, $\bar u_{i,j}$ | point value, 1D and 2D cell averages |
| $\bar w_j$, $\tilde w_j$ | $\bar u_j$ | generic input of the 1D routine; $f^+(u_j)$ in finite differences |
| $w_i(x)$ | $P_{\mathrm{rec}}$ | final reconstruction polynomial on $I_i$, as on [CWENO](/methods/cweno.md) |
| $S_1$, $S_2$, $S_3$ | kept | central stencils of 3, 5, 7 cells; **index = (order−1)/2, not the registry's $S_0$ most upwind** |
| $k$, $\nu$ | $K$ | order = number of stencil cells = number of candidates |
| $L_r(x)$, $r=0,\dots,6$ | $\mathsf L_r$ (page-local) | monic Legendre polynomials in $(x-x_i)/\Delta x$; **$L$ is the left-eigenvector matrix in the registry** |
| $A^{(k)}_r$ | $\hat u_r$ (page-local) | Legendre coefficients of $P_{\mathrm{opt}}$; **$A$ is the flux Jacobian in the registry** |
| $P^{(k)}_1$ | $P_{\mathrm{opt}}$ | degree $K-1$ |
| $P^{(k)}_\ell$, $\ell=2,\dots,k$ | $P_\ell$ | ghost polynomials, degree $K-\ell$; index 1 = highest degree, the reverse of MR-WENO |
| $d^{(k)}_r$, $\bar d^{(k)}_r$ | $d_\ell$ | linear weights and their unnormalized values |
| $\beta^{(k)}_r$ | $\beta_\ell$ | |
| $\tau_k$ | $\tau_K$ | $\big(\sum_{\ell=2}^K\lvert\beta_1-\beta_\ell\rvert/(K-1)\big)^{(K-1)/2}$; subscript = stencil points, agrees |
| $\bar\omega^{(k)}_r$, $\omega^{(k)}_r$ | $\alpha_\ell$, $\omega_\ell$ | exponent 1 on $\tau_K/(\epsilon+\beta_\ell)$ |
| $\varepsilon$ | $\epsilon$ | $10^{-6}$ |
| $f^\pm$, $\alpha$ | $f^\pm$, $a$ | global Lax–Friedrichs; **$\alpha$ is $\alpha_k$ in the registry** |
| $\hat f(a,b)$ | $h^{\mathrm{LF}}(u^-,u^+)$ | global Lax–Friedrichs two-point flux |
| $\varpi_l$, $\sigma_l$, $\kappa$ | $\mathsf w_l$, $\xi_l$, $N_{\mathrm G}$ (page-local) | Gauss weights, nodes on $[-\frac12,\frac12]$, number of nodes 2, 3, 4; **$\kappa$ is the kinetic energy in the registry** |
| $L(u)$ | $\mathcal L(u)$ | semi-discrete operator |

# Reference list

47 printed references in numbered style ([1]–[47], alphabetical), all parsed and merged complete into
the [bibliography](/bibliography.md) with `citedby` `zhang-2024-c`. No DOIs are printed. [12] is a
NASA/ICASE contract report; [14] prints the journal as "Comput. Phys. 115" (kept as printed); [33] is
AIAA paper 2008-757; [44] prints "J. Sci. Comput. 85 (29) (2020)". No cited key collides with a
different ingested source and no printed duplicates were found.

# Pages created or updated

Chunk 8 (2026-10-23), cited further in chunks 9–12 (2026-10-23/30). This source is cited on:

* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Density-wave advection](/benchmarks/density-wave-advection.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Multi-resolution WENO](/methods/multi-resolution-weno.md)
* [Negative linear weights](/methods/negative-linear-weights.md)
* [Sedov blast wave](/benchmarks/sedov-blast-wave.md)
* [Shock–vortex interaction](/benchmarks/shock-vortex-interaction.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)

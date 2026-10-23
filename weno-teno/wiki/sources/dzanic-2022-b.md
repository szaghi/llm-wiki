---
type: Source
title: "Dzanic & Witherden (2022) — Positivity-preserving entropy-based adaptive filtering for discontinuous spectral element methods"
description: "Entropy filtering: an element-wise exponential modal filter for nodal DG and flux reconstruction whose strength is the smallest that restores positivity and a local discrete minimum entropy principle at the solution nodes, found by bisection, implemented in PyFR and tested from shock tubes to a transonic delta-wing LES."
resource: "doi:10.1016/j.jcp.2022.111501"
source_kind: paper
authors: [Dzanic T., Witherden F.D.]
year: 2022
venue: "J. Comput. Phys. 468:111501"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Journal_of_Computational_Physics_Dzanic_Positivity-preserving_entropy-based_adaptive_filtering_for_d.pdf"
tags: [entropy-filtering, flux-reconstruction, dg, bound-preserving, shock-capturing]
timestamp: 2026-10-22T20:00:00Z
---

# Summary

The paper proposes [entropy filtering](/methods/entropy-filtering.md), a
shock-capturing method for nodal discontinuous spectral element methods: nodal
[DG](/methods/discontinuous-galerkin.md) and
[flux reconstruction](/methods/flux-reconstruction.md) (FR). After every
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) stage, each element whose
nodal values violate a constraint is filtered by the second-order exponential
modal filter $H_i(\hat u_i)=\hat u_i\,e^{-\zeta p_i^2}$, $p_i$ the degree of
mode $i$. The single strength $\zeta$ is the smallest for which the filtered
nodal values satisfy positivity of $\rho$ and $p$
([bound preservation](/properties/bound-preservation.md)) and a local discrete
minimum entropy principle ([entropy stability](/properties/entropy-stability.md)).
The bound in that principle is the minimum nodal entropy over the element and
its face neighbours at the previous stage. $\zeta=0$ returns the unfiltered
solution and $\zeta\to\infty$ the element mean, which is assumed admissible
for DG and FR with DG correction functions, SSP stepping, a CFL condition and
a positivity-preserving, entropy-stable
[HLL-family](/methods/hll-riemann-solvers.md) Riemann solver. A feasible
$\zeta$ therefore exists, and 20 bisection iterations find it element-locally.
The authors present the filter as a nonlinear generalization of the
[Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md), relate it
to [convex limiting](/methods/convex-limiting.md), and contrast it with
[artificial viscosity](/methods/artificial-viscosity.md). The constraint check
itself plays the role of a
[troubled-cell indicator](/definitions/troubled-cell-indicator.md). For
Navier–Stokes an explicit operator split filters the inviscid update, adds the
viscous increment, then filters again for positivity only.

The method is implemented in [PyFR](/software/pyfr.md). Test cases:
[Sod](/benchmarks/sod-and-lax-shock-tubes.md) (first-order convergence for
$\mathbb P^2$–$\mathbb P^7$); [Shu–Osher](/benchmarks/shu-osher-problem.md);
the [isentropic vortex](/benchmarks/isentropic-vortex.md) (rates between $N$
and $N+1$, filter overhead 1.1–2.0% on a V100);
[double Mach reflection](/benchmarks/double-mach-reflection.md);
[Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md); a
[Mach 800 jet](/benchmarks/high-mach-astrophysical-jet.md); the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at Re 1600, where
the filter stays inactive; the Daru–Tenaud viscous shock tube; and an LES of
the transonic VFE-2 delta wing.

# Version read

arXiv:2201.10502v3 [math.NA], 28 Jul 2022 ("Preprint submitted to Elsevier"),
not the version of record; 25 PDF pages (the footer counts 22, Algorithms 2–4
sit on pages "23 of 22" to "25 of 22"), all read, pp. 7, 10, 12, 14, 24 and 25
checked visually. Page 1 matches Crossref; it prints the title in title case
and the second author as "F. D. Witherden" (Crossref "Witherden F."). No DOI
is printed. Not to be confused with dzanic-2022 (the time-reversibility shock
capturing paper of Dzanic, Trojak & Witherden, its ref. [6]). Equation,
algorithm and table numbers are those of arXiv v3.

# Key claims

Registry notation (see the notation map): the source's degree $p$ and
$\mathbb P_p$ are $N$ and $\mathbb P^N$, its pressure $P$ is $p$, its
entropy $\sigma=\rho\log(P\rho^{-\gamma})$ is $\rho s$ (physical sign,
non-decreasing), its positivity functionals $\Gamma$ are $g_i$; the claims keep its
filter strength $\zeta$ and mode degree $p_i$, which the
[entropy filtering](/methods/entropy-filtering.md) page writes
$\zeta_{\mathrm F}$ and $n_j$.

1. Shock-capturing techniques for discontinuous spectral element methods fall into artificial viscosity, limiting, stencil modification and filtering; filtering resolves discontinuities sharply at minimal cost without changing the underlying scheme (§1). **Stated**
2. If the element mean $\bar u$ satisfies the positivity constraints (16) and the entropy constraint (17), at least one $\zeta$ makes the filtered solution satisfy both, with at least one inequality active; in practice it is "generally unique, although this is not guaranteed" (§3.1). **Derived** (from the endpoint behaviour of the filter; no theorem)
3. The adaptive filter needs only four properties: one free parameter; conservation of the element integral; a value recovering the unfiltered solution; a value recovering the mean mode (§3.1). **Stated**
4. The filter strength is $\zeta=\arg\min_{\zeta\ge0}$ subject to $g_i(\tilde u(x_j))\ge0$ and $\rho s(\tilde u(x_j))\ge(\rho s)_{\min}$ at every solution node (Eq. 19); a local minimum suffices when several $\zeta$ satisfy the constraints exactly (§3.1). **Stated**
5. For sufficiently resolved smooth solutions the unfiltered solution already satisfies the constraints, so the standard scheme is recovered (§3.1). **Stated**; supported by the isentropic vortex and Taylor–Green runs, **Shown**
6. With the degenerate filter $H_i(\hat u_i)=\hat u_i$ for $p_i=0$ and $\zeta\hat u_i$ otherwise, the method recovers the Zhang–Shu linear convex limiter between the low-order ($\zeta=0$) and high-order ($\zeta=1$) solutions; with a nontrivial filter it is a "nonlinear (and generally non-convex) limiting operation" (Remark "Limiting", §3.1). **Derived**
7. Taking the local minimum entropy over the element and its face neighbours (Eqs. 20–21) suffices because under a standard CFL condition the one-step domain of influence lies within the element and its direct neighbours; computed before the step and enforced after it, the local discrete minimum entropy is non-decreasing over its domain of influence (§3.2). **Derived**
8. The choice of entropy functional among admissible pairs is "posited to have a minor overall effect" (§3.2). **Stated** (not tested)
9. For the Euler equations, positivity of $\rho$ and $p$ and the entropy $\rho s$ with flux $v\rho s$ are preserved by the element mean under SSP time integration, a CFL condition and an entropy-stable positivity-preserving Riemann solver (Godunov, local Lax–Friedrichs, HLLC with suitable wave speeds) (§4.1, citing Zhang–Shu, Zhang–Xia–Shu and Chen–Shu). **Stated**
10. Source terms are admissible if the discretization preserves the constraints on the element mean; for entropy, the source contribution would augment the bound, or a strictly positive entropy source can be ignored at the cost of a relaxed constraint (Remark "Source terms", §4.1). **Stated**
11. For Navier–Stokes the element-mean entropy assumption fails for the mixed discretization, so an explicit operator split is used: filtered inviscid step, viscous increment, positivity-only re-filter, with no-slip replaced by slip for the hyperbolic step (§4.1, Alg. 4). **Stated**
12. A parabolic discretization satisfying the minimum entropy principle on the element mean would remove the split at a significant cost reduction (Remark "Navier–Stokes", §4.1). **Stated**
13. Implementation: 20 bisection iterations on the initial bracket $[0,-\log\varepsilon]$, $\varepsilon=10^{-8}$; floors $\rho_{\min}=p_{\min}=10^{-8}$; entropy tolerance $\epsilon_\sigma=10^{-4}$ (Eq. 27) (§4.3, Alg. 2). **Stated**
14. The relaxed entropy tolerance is beneficial because the logarithm makes the constraint sensitive to precision as $\rho\to\rho_{\min}$ or $p\to p_{\min}$, and because strict entropy enforcement can degrade accuracy (§4.3). **Stated**
15. Sod tube at $t=0.2$: first-order convergence of the point-mean density errors, least-squares rates in $L^1$ 0.91, 0.94, 0.93, 0.92, 0.87, 0.86 and in $L^2$ 1.05, 0.98, 1.01, 1.01, 0.98, 1.03 for $\mathbb P^2$–$\mathbb P^7$ (Tables 1–2). **Shown**
16. Sod tube at fixed number of degrees of freedom: lower degree gives marginally lower error, attributed to more elements and hence a more localized filter; $L^1$ rates 0.85, 0.93, 0.91, 0.88, 0.85, 0.87, $L^2$ rates 0.92, 1.06, 1.05, 1.03, 0.95, 1.08 (Tables 3–4, Fig. 2). **Shown**
17. Isentropic vortex: $L^2$ density error rates "generally in the range of $p$ to $p+1$", i.e. $N$ to $N+1$: 2.59 ($\mathbb P^2$), 4.00, 4.27, 6.73, 6.10, 8.13 ($\mathbb P^7$) (Table 5). **Shown**
18. Filter overhead on a smooth problem (isentropic vortex, 40 elements per direction, $\mathbb P^3$, $\Delta t=2\cdot10^{-4}$, 5 flow-throughs, NVIDIA V100): +1.1%, +1.7% and +2.0% time to solution for 5, 10 and 20 iterations (§5.1.3). **Shown**
19. Double Mach reflection ($\mathbb P^3$, $2400\times600$, $t=0.2$): sub-element shock resolution, no spurious oscillations, Kelvin–Helmholtz roll-up along the slip line kept; $\zeta$ active mainly at the shock fronts and much smaller than the mean-mode value (Fig. 4). **Shown**
20. Kelvin–Helmholtz instability ($\mathbb P^4$, $100^2$ to $800^2$ elements, $t=2$, unseeded): roll-up resolved, no spurious oscillations, pressure waves not over-dissipated (Fig. 5). **Shown**
21. Mach 800 jet ($\mathbb P^3$, $200\times600$ and $800\times2400$, $t=0.002$): robust; the filter is active mainly at the leading shock, less at the cocoon–jet interface on the fine mesh; "significantly better resolution" than Wu & Shu's mildly magnetized DG results with the Zhang–Shu limiter, partly attributable to the magnetic field there (Fig. 6). **Shown** (qualitative, cross-paper)
22. Taylor–Green vortex at Re 1600, $M=0.08$ ($\mathbb P^3$ with $96^3$ to $160^3$ degrees of freedom; $\mathbb P^3$–$\mathbb P^5$ at about $120^3$): agreement with the DNS of van Rees et al. and near identity with unfiltered runs, so the filter is predominantly inactive (Fig. 7). **Shown**
23. Viscous shock tube ($\mathbb P^4$, $800\times400$, viscosity $10^{-3}$ to $10^{-4}$, $t=1$): good agreement with Guermond et al., small-scale features more pronounced at high Re; about 16 elements needed the positivity re-filter after the viscous step, with $\zeta\sim10^{-4}$ (Figs. 8–9). **Shown**
24. VFE-2 delta-wing LES ($\mathbb P^3$, 4.1 M mixed prism and tetrahedral elements, 104 M degrees of freedom per component, Re $3\cdot10^6$, $M=0.8$, angle of attack $20.5^\circ$): surface pressure coefficient matches the PSP data of Konrath et al. at $x/c=0.2,0.4,0.6$, with a slight overprediction of the secondary-vortex peak at $x/c=0.8$ (Figs. 10–11). **Shown**
25. The approach "is free of problem-dependent tunable parameters" and easy to implement on unstructured meshes (§6). **Stated** (the tolerances of claim 13 are fixed global constants)

# Printed slips

- Algorithms 3 and 4 (pp. 24–25): the SSP-RK3 stages are printed $u^{(2)}=\tfrac34u^n+\tfrac14u^{(1)}+\Delta t\,\mathcal L(u^{(1)})$ and $u^{n+1}=\tfrac13u^n+\tfrac23u^{(2)}+\Delta t\,\mathcal L(u^{(2)})$; the factors $\tfrac14$ and $\tfrac23$ on the $\Delta t$ terms are missing. *(compiler check, not in the sources: for $u'=\lambda u$, $z=\lambda\Delta t$, the printed stages give $u^{n+1}=(1+\tfrac{11}6z+\dots)u^n$, not first-order consistent; with the factors the stability polynomial is $1+z+z^2/2+z^3/6$.)*
- Algorithm 4, third stage: "$u^{n+1}_k=u^{n+1}_k+\Delta u^{n+1,V}_k$"; by analogy with stages 1–2 the right-hand side should start from the filtered inviscid $u^{n+1,I}_k$.
- Tables 1–4 report $L^2$ errors smaller than the $L^1$ errors throughout (e.g. 6.87E-03 and 1.21E-03 at $\mathbb P^2$, 100 degrees of freedom), whereas Eq. (28) defines a mean absolute error and a root-mean-square error over the same points, for which $L^2\ge L^1$. *(compiler check, not in the sources: power-mean inequality.)* Either the $L^2$ used differs from Eq. (28) or the labels are inconsistent.
- Tables 1 and 2 use different mesh sets ($N=40$–$640$ and $20$–$320$ elements) for what §5.1.1 describes as one convergence study.
- Fig. 1 caption labels the interior interface points $u^+_i$ and the exterior ones $u^-_i$; the text defines $u^-_i$ from the element of interest and $u^+_i$ from the neighbour.
- Eq. (10): $\partial_t\bar u=-\int_{\partial\Omega_k}F\cdot n\,dx$ lacks the factor $1/V_k$ required by the definition of $\bar u$ in Eq. (11).
- Isentropic vortex (p. 10): the density is printed $p^{1/\gamma}$ with lowercase $p$ undefined; if it is the printed pressure, the far-field density is $(1/(\gamma M^2))^{1/\gamma}\ne1$ *(compiler check, not in the sources)*.
- Taylor–Green pressure (p. 14) printed $P_0+\tfrac1{16}(\cos2x+\cos2y)(\cos(2z+2))$; the velocity field is even in $z$ and so is the pressure it induces, which $(\cos2z+2)$ is and $\cos(2z+2)$ is not: a misplaced parenthesis. *(compiler check, not in the sources.)*
- Eq. (31): $\varepsilon_K=dK/dt$ is negative in the decaying Taylor–Green vortex, yet Fig. 7 plots it positive; a minus sign is missing.
- Double Mach reflection (p. 12): "No-slip adiabatic wall boundary conditions" on the bottom boundary of an inviscid computation; §4.1 itself replaces no-slip by slip for the hyperbolic step.
- Algorithm 2: "for $i\in\{0,..,n_{\mathrm{iters}}\}$" with $n_{\mathrm{iters}}=20$ is 21 iterations if inclusive, against "20 iterations" in §4.3; and "$\varepsilon=10^{-8}$ // Machine precision (FP32)" is below the FP32 unit roundoff $2^{-24}\approx6\times10^{-8}$ *(compiler check, not in the sources)*.
- Appendix A describes the Vandermonde matrix $\mathbf V$ as mapping "from the nodal basis to a modal basis", but Algorithm 2 uses $\hat u=\mathbf V^{-1}u$, i.e. $\mathbf V$ maps modal to nodal.
- The Remark "Limiting" parametrizes $\zeta$ in the opposite sense to Eq. (18) ($\zeta=0$ low order there, unfiltered in Eq. 18).
- Refs. [26] and [27] (Zhang & Shu, J. Comput. Phys. 229, issues 9 and 23) are printed with years 2010 and 2011 for the same volume.

# Notation map

| Dzanic & Witherden (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf u$, $\mathbf u_i$, $\bar{\mathbf u}$, $\tilde{\mathbf u}$ | $u$, $u(x_i)$, $\bar u$, kept | state, nodal value, element mean, filtered solution |
| $\hat{\mathbf u}_i$ | kept | modal coefficient; **the hat is not a numerical flux** |
| $\mathbf F$, $\mathbf F_I$, $\mathbf F_V$ | $f$ | flux, inviscid and viscous parts |
| $\mathbf u^-_i$, $\mathbf u^+_i$ | $u^-$, $u^+$ | interior and exterior interface values (text convention; Fig. 1 swaps them) |
| $\rho$, $\mathbf v$, $P$, $E$ | $\rho$, $v$, $p$, $E$ | primitive and conserved quantities; **$P$ is $p$** |
| $\mathbf q=[\rho,\mathbf v,P]$ | kept | primitive variables of the initial data |
| $\mathbb P_p$, $p$ | $\mathbb P^N$, $N$ | degree of the approximation, design order $N+1$; **$p$ collides with the pressure** |
| $p_i$ | $n_j$ (page-local) | degree of the modal basis function $\psi_j$ |
| $\phi_i$, $\psi_i$, $\ell_j$, $\mathbf g_j$ | $\ell_j$, kept, $\ell_j$, kept | nodal (Lagrange) and orthogonal modal bases; FR correction functions |
| $H_i$, $\zeta$ | $H_j$, $\zeta_{\mathrm F}$ (page-local) | filter function and strength; **$\zeta$ collides with the page-local characteristic variables and the WENO-Z+ coefficient** |
| $\Gamma$, $\Gamma_1=\rho$, $\Gamma_2=P$ | $g_i$ | constraint functionals; **$\Gamma$ is not $\gamma$** |
| $\sigma=\rho\log(P\rho^{-\gamma})$, $\boldsymbol\Sigma=\mathbf v\sigma$ | $\rho s=-(\gamma-1)\eta$, $-(\gamma-1)F_\eta$ | physical sign, $\partial_t\sigma+\nabla\cdot\boldsymbol\Sigma\ge0$; **density-weighted, not the specific entropy $s$**; $\sigma$ is the affine scaling on registry pages |
| $\sigma^*_k$, $\sigma^k_{\min}$, $\mathcal N(k)$ | kept, $(\rho s)^K_{\min}$, kept | element-minimum and local-minimum nodal entropy, face-neighbour set |
| $\epsilon_\sigma$, $\rho_{\min}$, $P_{\min}$, $\varepsilon$ | kept, kept, $p_{\min}$, $\epsilon_{\mathrm m}$ (page-local) | entropy tolerance $10^{-4}$, floors $10^{-8}$, machine precision setting the bisection bracket, $10^{-8}$ |
| $S$, $I$ | kept | nodal and interface-node index sets |
| $V_k$, $\Omega_k$ | kept | element volume and element; **$V_k$ is not a control volume of Coppola & Veldman** |
| $\mathbf V$ | kept | Vandermonde matrix |
| $N$, $M$ | kept | elements per direction, degrees of freedom; **$N$ is the DG degree and $M$ the Mach number in the registry** |
| $\mu$, $Pr$ | kept, $\mathrm{Pr}$ | dynamic viscosity, Prandtl number 0.73 |
| $K$, $\varepsilon_K$, $\varepsilon_E$ | kept | kinetic energy and dissipation rates of the Taylor–Green diagnostics |

# Reference list

57 printed references in numbered style ([1]–[57]), all parsed and merged
complete into the [bibliography](/bibliography.md) with `citedby`
`dzanic-2022-b`. Refs. [16] and [19] are two chapters of the same Dafermos
book, kept as two entries. Refs. [6] (arXiv:2110.03653) and [51]
(arXiv:2111.07915) are printed as preprints and kept as their own entries.
Ref. [7] (Boris & Book) is printed with the 1997 J. Comput. Phys. reprint
volume, [54] is a NASA technical memorandum, and [31] (Godunov 1959) has no
DOI. Refs. [26] and [27] are kept with their printed years (see Printed slips).
No printed duplicates were found.

# Pages created or updated

Chunk 3 (2026-10-22), cited further in chunks 4–6 (2026-10-23). This source is cited on:

* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Bound preservation](/properties/bound-preservation.md)
* [Convex limiting and invariant-domain-preserving schemes](/methods/convex-limiting.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Entropy filtering for DG and FR](/methods/entropy-filtering.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Flux reconstruction and energy-stable FR](/methods/flux-reconstruction.md)
* [High-Mach astrophysical jets](/benchmarks/high-mach-astrophysical-jet.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [PyFR](/software/pyfr.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [Viscous shock tube (Daru–Tenaud)](/benchmarks/viscous-shock-tube.md)
* [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)

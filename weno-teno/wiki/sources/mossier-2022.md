---
type: Source
title: "Mossier et al. (2022) — A p-Adaptive Discontinuous Galerkin Method with hp-Shock Capturing"
description: "A p-adaptive DGSEM in FLEXI that switches troubled elements to a second-order TVD finite-volume scheme on 2N+1 subcells per direction, with one modal-decay indicator driving both shock detection and degree changes; speedups of 1.3 to 4 on standard compressible tests."
resource: "doi:10.1007/s10915-022-01770-6"
source_kind: paper
authors: [Mossier P., Beck A., Munz C.-D.]
year: 2022
venue: "J. Sci. Comput. 91:4"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Journal_of_Scientific_Computing_Mossier_A_p-Adaptive_Discontinuous_Galerkin_Method_with_hp-Shock_Cap.pdf"
tags: [dg, hp-adaptation, limiting, troubled-cell, software]
timestamp: 2026-10-23T10:00:00Z
---

# Summary

The paper builds a hybrid scheme for the compressible Euler equations in the open-source
[DGSEM](/methods/dgsem.md) code [FLEXI](/software/flexi.md). In smooth regions the scheme is
$p$-adaptive: each element has its own degree $N\in[N_{\min},N_{\max}]$, and elements of
different degree are coupled through interpolation to, and modal projection from, the higher
degree at the interface. Troubled elements switch whole to a second-order
[TVD](/definitions/total-variation-diminishing.md) (minmod) finite-volume scheme on an
element-local subcell grid. This extends FLEXI's earlier
[subcell finite-volume scheme](/methods/subcell-finite-volume-limiting.md), which uses $N+1$
subcells, to an arbitrary number of subcells. The chosen $2N_{\max}+1$, taken from Dumbser et
al., is the largest number that does not shorten the explicit time step. The authors call the
combination "hp-adaptive", but the "h" is the subcell refinement inside finite-volume
elements: the DG mesh never changes, so no element is split as in
[mesh refinement](/methods/adaptive-mesh-refinement.md). The other "hp" source of the bundle
refines the mesh ([hp-adaptation](/methods/hp-adaptation.md)).

A single a priori [indicator](/definitions/troubled-cell-indicator.md), the modal decay rate of
Mavriplis, drives both decisions. It is the exponential fit of the Legendre-mode energy in each
reference direction, and four thresholds per degree, linear in $N$, turn it into DG/FV
switching and degree raising or lowering. The implementation keeps FLEXI's static arrays by
allocating arrays for every degree in the range and finite-volume arrays for every element,
trading memory for speed.

The tests show [free-stream preservation](/properties/free-stream-preservation.md) on a curved
mixed DG/FV mesh to round-off, and convergence at the order of the lowest degree present. The
performance overhead is at most 15 % for a half-half degree split and up to 80 % for a
checkerboard. The applications are [Sod](/benchmarks/sod-and-lax-shock-tubes.md),
[Shu–Osher](/benchmarks/shu-osher-problem.md),
[double Mach reflection](/benchmarks/double-mach-reflection.md), the
[forward-facing step](/benchmarks/forward-facing-step.md), a transonic airfoil and a 3D
[spherical explosion](/benchmarks/explosion-and-implosion-problems.md). With far fewer degrees of
freedom per element, the adaptive runs are faster than static FLEXI by factors of 1.3 to 4 and
resolve shocks as sharply or more sharply. The finer subcells also suppress the acoustic waves
generated at DG/FV interfaces. Memory grows by about 20 % ($p$-adaptive) and about 4 times
(hp-adaptive). All evidence is numerical.

# Version read

The version of record (Springer typeset, open access CC BY 4.0; J. Sci. Comput. 91, article 4,
published online 18 February 2022), 36 pages. Page 1 prints the DOI, title and authors,
matching Crossref. The Springer header on page 1 labels the paper "REVIEW", though it is an
original research article. No identity problem. Equation, table and figure numbers are those of
the journal version.

# Key claims

Registry notation: $N$ the DG degree, $a$ the maximum signal speed, $\nu$ the CFL number,
$\varrho_K$ the exponential modal decay rate (registry §10), $N_{\mathrm{FV}}$ the number of subcells per direction (page-local).

1. The scheme is a $p$-adaptive DGSEM in smooth regions and a second-order TVD finite-volume scheme on $N_{\mathrm{FV}}^d$ subcells in troubled elements; the DG mesh is never changed at run time (§1, §4). **Stated**
2. Elements of different degree are coupled by transforming the lower-degree surface data to the higher degree $M$, evaluating the Riemann solver at the degree-$M$ nodes, and projecting the flux back to degree $N$ by modal cut-off. No restriction is placed on the degrees of neighbouring elements (§3.3, Eqs. 14–17). **Stated**
3. The projection from degree $N$ to $M<N$ by Legendre modal truncation is called "conservative"; interpolation is used for $N<M$ (§3.3). **Stated**
4. Time step: $\Delta t=\nu\,\alpha_{\mathrm{RK}}(N)\,\Delta x_{\mathrm{DG}}/\big((2N+1)\,a\big)$ with $\alpha_{\mathrm{RK}}(N)>1$; on finite-volume subcells $\Delta t=\nu\,\alpha_{\mathrm{RK}}(0)\,\Delta x_{\mathrm{FV}}/a$ (Eqs. 18, 31). **Stated**
5. Following Dumbser et al., a subcell finite-volume scheme does not impose a smaller time step than its DG element up to $N_{\mathrm{FV}}=2N+1$, so this choice "should not increase the total number of time steps". The step counts confirm it: DMR 4695/4726/4765, forward-facing step 19,969/19,136/19,993, 3D explosion 235/241/248 (static/$p$/hp) (§4.3, Tables 3, 4, 6). **Shown**
6. The DG-to-FV map is the subcell integral mean (Eqs. 27–29). The FV-to-DG map is its pseudo-inverse, a constrained least-squares fit with conservation of the element integral as constraint, after Dumbser and Zanotti, and satisfies $V^{\mathrm{FV2DG}}V^{\mathrm{DG2FV}}=I$ (§4.3, Eq. 30). **Stated**
7. The subcell metric terms are the subcell integral means of $J$ and $Ja^{(i)}$, i.e. $V^{\mathrm{DG2FV}}$ applied to the DG metrics (Eqs. 19–21). **Stated**
8. The modal decay rate serves both as shock detector (very small decay rate: finite volume) and as error estimator (small: raise $N$; large: lower $N$) (§5, Eqs. 33–36). **Stated**
9. The thresholds are linear in $N$, which reduces the free parameters to four, the end values $FV^{N_{\min}}_{\mathrm{lower}}$, $FV^{N_{\max}}_{\mathrm{lower}}$, $DG^{N_{\min}}_{\mathrm{refine}}$, $DG^{N_{\max}}_{\mathrm{refine}}$, tuned per test case (§7.3, Eqs. 37–38). **Stated**
10. $p$-adaptation is done only at the start of a time step. The DG-to-FV switch is also checked after every Runge–Kutta stage, but the FV-to-DG switch is not, because it "could violate the time step restriction" (§7.2). **Stated**
11. Free-stream preservation on a curved mesh (checkerboard of $N=2$ and $N=7$ in the DG half, $N_{\mathrm{FV}}=15$ in the FV half, geometry degree 2): $L^2$ errors $7.79\times10^{-16}$ to $3.37\times10^{-15}$ and $L^\infty$ errors $6.35\times10^{-14}$ to $2.89\times10^{-13}$ after 165 steps (§8.1, Table 1). **Shown**
12. With two degrees in a checkerboard ($N_{\max}=6$, $N_{\min}\in\{2,\dots,5\}$), the $p$-adaptive DGSEM converges at the order $N_{\min}+1$ of the lowest degree present, e.g. 3.11, 2.97, 3.00, 3.00 for $N_{\min}=2$ and 5.95, 6.00, 5.99, 5.98 for $N_{\min}=5$, at CFL 0.05 (§8.2, Table 2). **Shown**
13. Single-core cost per degree of freedom and time step: with a uniform degree the adaptive code is only slightly slower than open-source FLEXI (nearly equal for $N>4$, about 15 % slower at $N=2$). A half-half degree split costs at most 15 % more, a checkerboard (worst case) up to 80 % (Xeon Gold 6140, GNU 8.3.0) (§8.3, Fig. 7). **Shown**
14. Sod: the adaptive run ($N\in[2,5]$, $N_{\mathrm{FV}}=11$) resolves the shock more sharply than the static run ($N=5$, $N_{\mathrm{FV}}=6$), with 151.6 against 216.0 degrees of freedom per element ("about 25% less"). The highest degree appears only at the contact, with slightly raised degrees at the rarefaction (§8.4, Figs. 8–9). **Shown**
15. Shu–Osher: the adaptive run matches the reference better behind the shock with a mean of 70.8 degrees of freedom per element against 216 (§8.5, Figs. 10–11). **Shown**
16. Double Mach reflection: degrees of freedom per element 216/35/54, wall time 15,578/3856/6569 s, memory 4.9/5.9/19.0 GB (static/$p$/hp); speedups of "a factor 4" and "almost a factor 2.5", memory up by 20 % and 4 times (§8.6, Table 3). **Shown**
17. DG/FV interfaces emit acoustic waves, because the two operators have different resolution and transfer functions. The waves are strongest for $N_{\mathrm{FV}}=N+1$, and $N_{\mathrm{FV}}=2N+1$ "almost completely avoids" them (§8.6–8.7, Figs. 13, 16). **Shown** (qualitative, from schlieren images)
18. Forward-facing step: degrees of freedom per element 216/44/82, wall time 65,782/19,774/40,217 s, memory 4.8/5.8/18.7 GB; speedups of "almost a factor 3" and "about 1.6" (§8.7, Table 4). **Shown**
19. Transonic airfoil ($M=0.73$): degrees of freedom per element 125/30.5/32.5, time steps 176,737/61,589/61,410, wall time 10,160 s (static, 32 cores) against 24,692 and 27,149 s (adaptive, one core), memory 20.2/25.5/66.7 GB. The adaptive runs need about 3 times fewer time steps, because the most restrictive elements are not at the maximum degree. Only about 3 elements, in the wake, are limited, yet the finer subcells improve the wake structures substantially (§8.8, Table 5). **Shown**
20. 3D spherical explosion: degrees of freedom per element 216/56/141, wall time 10,839/3557/8601 s (AMD EPYC 7302), memory 39.8/48.6/157.3 GB. The $p$-adaptive run is three times faster, the hp-adaptive run only 25 % faster, because almost 8 % of the elements are limited (§8.9, Table 6). **Shown**
21. The memory increase is dominated by the metric terms precomputed for every allowed degree and by the finite-volume arrays, which "largely shadow" the solution storage (§6, §8.6). **Stated**
22. Load balancing for parallel runs is "work in progress"; every comparison is single-core except the static airfoil run (§8.3, §9). **Stated**
23. Li and Jameson showed that $h$-refinement is better at discontinuities and $p$-refinement more efficient in smooth regions, which motivates the hybrid (§1). **Stated** (cited)
24. Split-form (de-aliased) DG is deliberately not used, to isolate the stabilizing effect of the subcells (§9). **Stated**

*Compiler checks, not in the sources.* Equating the two time-step limits of claim 4 with
$\Delta x_{\mathrm{FV}}=\Delta x_{\mathrm{DG}}/N_{\mathrm{FV}}$ gives
$N_{\mathrm{FV}}=(2N+1)\,\alpha_{\mathrm{RK}}(0)/\alpha_{\mathrm{RK}}(N)$, i.e. $2N+1$ only up to the
ratio of the Runge–Kutta factors. The paper states only the conclusion. The speedups recomputed
from the tables are 4.04 and 2.37 (DMR), 3.33 and 1.64 (forward-facing step), 3.05 and 1.26 (3D
explosion). Legendre truncation to degree $M$ keeps the reference-space mean $\int u\,d\xi$; it keeps the
element integral $\int Ju\,d\xi$ when $J$ is of degree at most $M$ in each direction, in
particular on affine elements, and not in general on curved ones. The paper does not discuss
this case of its "conservative" (claim 3).

# Printed slips

- Eqs. (7) and (22) print the third contravariant flux as $J\mathbf a^2\cdot F$; by Eq. (6) it is $J\mathbf a^3\cdot F$.
- Eqs. (37)–(38) interpolate with $N$ where $N-N_{\min}$ is needed: as printed, $FV^N_{\mathrm{lower}}$ does not reproduce the end values at $N=N_{\min}$ and $N=N_{\max}$ unless $N_{\min}=0$. Under (37), (38) gives $FV^N_{\mathrm{upper}}=FV^{N+1}_{\mathrm{lower}}$.
- §7.3: the second bullet for finite-volume elements switches back to DG for "$ind>FV^N_{lower}$", while the first bullet and Fig. 4 with its caption use $FV^N_{\mathrm{upper}}$. With $FV^N_{\mathrm{lower}}$ the hysteresis band would vanish.
- §4.3: "For $N_{FV}+1>N$, this leads to an over determined system." The system has $N_{\mathrm{FV}}$ equations for $N+1$ unknowns per direction, so it is overdetermined for $N_{\mathrm{FV}}>N+1$.
- §7.3 introduces four thresholds per degree, but the reduction to "four free parameters" covers only $FV_{\mathrm{lower}}$ and $DG_{\mathrm{refine}}$; how $DG^N_{\mathrm{coarse}}$ is set is never stated. The paper also prints "$DG^N_{coasre}$" once.
- The Fig. 5 caption puts both the DG and the FV discretization in "the left half".
- §8.4: "about 25% less DOFs" for 151.6 against 216.0, which is $1-151.6/216.0=0.30$.
- §8.7: "almost a factor 3" for a speedup of $65{,}782/19{,}774=3.33$.
- §8.8: "about 3 times more time than the globally refined computation on 32 cores", where Table 5 gives $24{,}692/10{,}160=2.43$ and $27{,}149/10{,}160=2.67$.
- §1 cites "Persson and Peraire [20]", but ref. [20] lists Persson as sole author.
- §2 prints the momentum flux as $\rho v\times v$; the dyadic product is meant.
- Typos: "Discontinious" (heading of §3.2), "euqation", "trough", "singe core", "Experimenal", "empathize".
- Ref. [33] prints a ResearchGate DOI (10.13140/RG.2.2.26934.32322/1), not a journal DOI.

# Notation map

| Mossier et al. 2022 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u=[\rho,\rho v,E]^T$, $F$, $\gamma$ | $u$, $f^{(d)}$, $\gamma$ | agree; $\gamma=1.4$ |
| $\mathcal F$, $\mathcal F_i=J_{geo}\mathbf a^i\cdot F$ | contravariant flux | |
| $J_{geo}$, $\mathbf a^i$, $\mathbf a_i$ | $J$, $Ja^{(i)}/J$ | Jacobian and contravariant (covariant) basis vectors |
| $N$ | $N$ | DG degree, element-local; §1 also uses $p$ for the order |
| $M$ | — (local) | degree of the higher-degree neighbour at an interface |
| $N_{min}$, $N_{max}$, $N_{geo}$ | $N_{\min}$, $N_{\max}$ | degree range; geometry degree |
| $N_{FV}$ | $N_{\mathrm{FV}}$ (local) | subcells per direction |
| $\psi_l$, $\ell_i$ | $\ell_j$ | Lagrange basis on Legendre–Gauss nodes (not LGL) |
| $\xi^k_m$, $\omega_m$ | $\xi_j$, $\mathsf w_j$ | Gauss nodes in a subinterval and weights; **collision** with $\omega_k$ |
| $w=2/N_{FV}$ | — | subcell width in reference space |
| $V_{Leg}$, $V_{M2N}$ | — | nodal-to-modal Vandermonde; degree-change operator (maps $u_N\to u_M$ despite its name) |
| $V^{DG2FV}$, $V^{FV2DG}$ | — | subcell-mean operator and its pseudo-inverse |
| $\zeta_{ijk}$, $\lambda_i$ | — | tensor Legendre basis; **collision**: $\lambda_i$ here are Legendre polynomials, not eigenvalues |
| $w_m$ | — (local) | relative energy of mode $m$ in one direction |
| $\sigma^1,\sigma^2,\sigma^3$, $ind=\min_i\lvert\sigma^i\rvert$ | $\varrho_K$ | exponential modal decay rate; **collision** with the affine scaling $\sigma$ |
| $FV^N_{lower}$, $FV^N_{upper}$, $DG^N_{refine}$, $DG^N_{coarse}$ | — (local) | thresholds per degree |
| $\lambda^c$ | $a$ | maximum signal speed |
| $CFL$, $\alpha_{RK}(N)$ | $\nu$, $\alpha_{\mathrm{RK}}(N)$ | **collision**: $\alpha_{\mathrm{RK}}$ is not the blending coefficient $\alpha$ |
| PID | cost per degree of freedom and time step | wall time × cores / (DOF × steps) |

# Reference list

The paper prints 34 references, numbered [1]–[34] and sorted alphabetically. The list is merged
complete into the [bibliography](/bibliography.md), with `citedby` including `mossier-2022`.
Ref. [15] (Li, Premasuthan, Jameson 2010) has a garbled venue ("In: AIAA-201010 of 11 American
Institute of Aeronautics and Astronautics, pp. 10–1007"), recorded as printed. Ref. [20]
(Persson 2013) prints a DOI but no venue. Ref. [17] is a 1989 MIT dissertation, and ref. [33]
carries the ResearchGate DOI noted above. No duplicate keys arose.

# Pages created or updated

Chunk 4 (2026-10-23), cited further in chunks 5–7 (2026-10-23). This source is cited on:

* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Block-structured adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Discontinuous Galerkin spectral element method (DGSEM)](/methods/dgsem.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [FLEXI](/software/flexi.md)
* [Free-stream preservation](/properties/free-stream-preservation.md)
* [h- and hp-adaptation for DG](/methods/hp-adaptation.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Mach 3 forward-facing step](/benchmarks/forward-facing-step.md)
* [MOOD a posteriori limiting](/methods/mood-a-posteriori-limiting.md)
* [Roe approximate Riemann solver](/methods/roe-riemann-solver.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Subcell finite-volume limiting for DG](/methods/subcell-finite-volume-limiting.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [Two-dimensional explosion and implosion problems](/benchmarks/explosion-and-implosion-problems.md)
* [WENO limiters for discontinuous Galerkin](/methods/weno-limiter-dg.md)

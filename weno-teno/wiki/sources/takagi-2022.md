---
type: Source
title: "Takagi et al. (2022) — A novel high-order low-dissipation TENO-THINC scheme for hyperbolic conservation laws"
description: "Hybrid finite-difference reconstruction that runs fifth-order TENO in smooth regions and switches to THINC in cells flagged by a parameter-free discontinuity detector built only from TENO's binary stencil flags; fifth order on smooth data, sharper contacts and more small-scale structure on standard Euler tests, at about 17 % extra cost over TENO5."
resource: "doi:10.1016/j.jcp.2021.110899"
source_kind: paper
authors: [Takagi S., Fu L., Wakimura H., Xiao F.]
year: 2022
venue: "J. Comput. Phys. 452:110899"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Journal_of_Computational_Physics_Takagi_A_novel_high-order_low-dissipation_TENO-THINC_scheme_for_hyp.pdf"
tags: [teno, thinc, hybrid-scheme, troubled-cell, finite-difference, low-dissipation]
timestamp: 2026-10-21T12:00:00Z
---

# Summary

The paper builds [TENO-THINC](/methods/teno-thinc.md), a hybrid reconstruction for the
[conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md).
It uses fifth-order [TENO](/methods/targeted-eno.md) in smooth regions and the
non-polynomial [THINC reconstruction](/methods/thinc-reconstruction.md) in cells judged
to contain a genuine discontinuity. TENO keeps the spectral properties of its linear
scheme up to intermediate wavenumbers in the
[approximate dispersion relation](/definitions/approximate-dispersion-relation.md), but
its stencil selection smears contacts. THINC with steepness $\beta_{\mathrm T}=1.6$
represents a jump inside a cell, but it is anti-diffusive on smooth scales.

The contribution is a parameter-free
[discontinuity indicator](/definitions/troubled-cell-indicator.md) built only from the
binary flags $\delta_k$ that TENO5 already computes from its
[smoothness indicators](/definitions/smoothness-indicator.md). In a one-cell model step
the jump cell has all flags equal to 1, while its neighbours have lost the stencil
that crosses the jump. A cell flag $\zeta_i\in\{2,1,-1,0\}$ and a seven-cell rule turn
this pattern into a detector. In a flagged cell the TENO flux is replaced by the THINC
flux, or by first order where the data are not monotone. The paper contrasts this
switch with the [BVD](/definitions/boundary-variation-diminishing.md) selection and with
the sensors of [hybrid schemes](/methods/hybrid-weno.md), which depend on parameters.
It also cites [WENO-JS](/methods/weno-js-reconstruction.md),
[mapped WENO](/methods/mapped-weno.md) and
[artificial viscosity](/methods/artificial-viscosity.md) as background.

All evidence is numerical. The setting is characteristic-wise reconstruction
([characteristic decomposition](/methods/characteristic-decomposition.md)), Rusanov
[flux splitting](/methods/lax-friedrichs-flux.md),
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) and a
[symmetry-preserving](/properties/symmetry-preservation.md) implementation. The scheme
is fifth order on a Gaussian pulse, and it beats [WENO-Z](/methods/weno-z.md) and TENO5
on square waves, Sod and Lax, [Shu–Osher](/benchmarks/shu-osher-problem.md) and the
[Woodward–Colella blast wave](/benchmarks/woodward-colella-blast-wave.md). It is also
tested on [double Mach reflection](/benchmarks/double-mach-reflection.md),
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md),
[2D Riemann problems](/benchmarks/two-dimensional-riemann-problems.md),
[Mach 80 and 2000 jets](/benchmarks/high-mach-astrophysical-jet.md), run with a
positivity-preserving flux limiter (see [convex limiting](/methods/convex-limiting.md)),
and the inviscid [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md).

# Version read

Version of record (Elsevier typeset, © 2021 Elsevier Inc.), J. Comput. Phys.
452:110899, available online 20 Dec 2021, with the issue year 2022. It has 24 pages and
prints its DOI. Page 1 matches Crossref; there is no identity problem.

# Key claims

The source labels the TENO5 stencils $S_0=\{i-1,i,i+1\}$, $S_1=\{i,i+1,i+2\}$ and
$S_2=\{i-2,i-1,i\}$, so $S_2$ is the most upwind one. This labelling is kept below
because the detector is defined on it; $\delta_{k,i}$ is the flag of $S_k$ at cell $i$.

1. On linear advection of a Gaussian pulse, TENO-THINC reaches the design fifth order, with $L_\infty$ errors identical to those of the fifth-order upwind linear scheme on every grid ($\Delta x=0.01$ to $0.000625$; errors $4.63\times10^{-3}$ to $5.24\times10^{-9}$; observed orders 4.81, 4.98, 4.99, 4.97). Neither TENO's nonlinear adaptation nor THINC is activated (§4.1, Table 2). **Shown**
2. The detector ((19)–(20)) is parameter-free; the hybrid inherits only the TENO5 parameters $q=6$ and $C_T=10^{-5}$ (§3.2, §4). **Stated** (by construction)
3. For the model step (18) with TENO5 and $C_T=10^{-5}$, the jump cell has $\delta_{1,i}=\delta_{2,i}=1$, while $\delta_{1,i-1}=0$ and $\delta_{2,i+1}=0$ (§3.1, Table 1). **Derived** (computed table)
4. In well-resolved smooth regions all $\delta_k=1$, THINC is never activated, and the scheme recovers exactly the spectral properties and order of the TENO linear scheme (§3.2). **Stated** (supported by claim 1)
5. In under-resolved smooth regions where some $\delta_k=0$, the hybrid "mainly" uses TENO with nonlinear adaptation; only patterns that satisfy (19)–(20) trigger THINC (§3.2). **Stated**
6. The THINC reconstruction is bounded by $f_{i-1}$ and $f_{i+1}$, cannot create new extrema and needs no extra limiter (§2.3). **Stated**
7. THINC with $\beta_{\mathrm T}=1.6$ has a positive imaginary part of the modified wavenumber, $\tilde\vartheta_i>0$, in some wavenumber ranges, like the Superbee limiter. This anti-diffusion squares smooth profiles and motivates confining THINC to discontinuities (§2.3). **Stated** (cited)
8. The THINC flux used here ((16), with $\mathrm{sgn}(\varsigma)$ and $\lvert\varsigma\rvert$) differs from the form of Deng, Shimizu and Xiao (2019); the paper links the difference to symmetry breaking by round-off (§2.3). **Stated**
9. Jiang–Shu multi-wave advection ($N_x=200$ to $t=200$, $N_x=400$ to $t=2000$): TENO-THINC preserves the square wave much better than WENO5-Z and TENO5, and the smooth waves are similar to TENO5 (§4.2, Figs. 2–3). **Shown**
10. Sod ($t=0.2$) and Lax ($t=0.14$), $N_x=100$: shocks as sharp as WENO5-Z and TENO5, contacts better resolved (§4.3, Figs. 4–5). **Shown**
11. Shu–Osher, $N_x=200$, $t=1.8$: similar to TENO5 and slightly better than WENO5-Z; CFL 0.4 or 0.6 makes a negligible difference (§4.4, Figs. 6–7). **Shown**
12. Woodward–Colella blast waves, $N_x=400$, $t=0.038$, CFL 0.35, Roe flux splitting with entropy fix: the contact is resolved markedly better than with WENO5-Z and TENO5 (§4.5, Fig. 8). **Shown**
13. Blast-wave refinement ($N_x=400$ to $3200$): with $C_T=10^{-4}$ the solution converges monotonically to the reference; with the default $C_T=10^{-5}$ a small overshoot appears near the strong contact at very high resolution (§4.5, Fig. 9). **Shown**
14. Double Mach reflection at $512\times128$ and $1024\times256$: TENO-THINC resolves more small-scale structure than WENO5-Z, TENO5 and the six-point TENO6, and on the coarse grid it is similar to WENO5-Z on the fine grid (§4.6, Figs. 10–11). **Shown**
15. Cost per time step on double Mach reflection (Table 3, hardware not stated): WENO5-Z 696/2802 ms, TENO5 810/3255 ms, TENO-THINC 946/3810 ms, TENO6 867/3330 ms at $512\times128$ / $1024\times256$. TENO-THINC costs 16.8 % (17.1 %) more than TENO5 and 9.1 % (14.4 %) more than TENO6 (§4.6). **Shown**
16. Double Mach reflection results are insensitive to the CFL number (0.4 or 0.6) and to $\epsilon\in\{10^{-8},10^{-12},10^{-40}\}$ (§4.6, Figs. 12–13). **Shown**
17. Rayleigh–Taylor at $64\times256$ and $128\times512$, $t=1.95$: TENO-THINC captures markedly more small-scale vortical structure than WENO5-Z and TENO5, with Rusanov and Roe fluxes alike, and preserves symmetry (§4.7, Figs. 14–17). **Shown**
18. 2D Riemann configurations 3 and 12 at $1024^2$: more fine structure than WENO5-Z and TENO5, sharp and stable shocks, symmetry preserved (§4.8, Figs. 18–19). **Shown**
19. Mach 80 and Mach 2000 jets at $800\times400$, CFL 0.35, with the Hu–Adams–Shu positivity-preserving flux limiter: all three schemes are stable, and TENO-THINC resolves the most small-scale structure, followed by TENO5 and WENO5-Z (§4.9, Fig. 20). **Shown**
20. Inviscid Taylor–Green vortex at $64^3$ up to $t=10$: TENO-THINC preserves kinetic energy better and gives a larger enstrophy growth than WENO5-Z and TENO5 (§4.10, Fig. 21). **Shown**
21. THINC activation maps (with $\epsilon=10^{-8}$ for clarity) show activation mainly near genuine discontinuities in 1D, double Mach reflection, Riemann configuration 3 and Rayleigh–Taylor (§4.11, Figs. 22–25). **Shown**
22. The scheme "is straightforward to be deployed in a finite-volume solver without any modification on the reconstruction scheme itself" (§5). **Stated**
23. The results "are among the best in the literature and thus serve as the state-of-the-art reference" (abstract, §5). **Stated**
24. TENO candidate stencils of increasing width each contain at least one upwind point, so even-order TENO avoids purely downwind stencils (§2.2.1). **Stated** (cited)

# Printed slips

- Fig. 10 caption: "at the simulation time t = 2.0", while §4.6 gives $t=0.2$.
- §4.4: the initial data (29) are given on $-5\le x\le5$, but the text says "The computational domain is [0,10]".
- §2.3: the THINC conservation constraint is printed as $f_i=\int_{x_{i-1/2}}^{x_{i+1/2}}h(x)\,dx$, without the factor $1/\Delta x$ of (3).
- §2.1 calls the implicit function $h$ of (3) the "primitive function" and the point fluxes $f_i$ "cell-averaged values".
- §4: "$q=6$ and $C_T=10^{-5}$ without tuning case-by-case [15][2]": [2] is the WENO-Z paper of Castro et al., not a source of TENO parameters.
- §1: [8] is cited twice in the list "[18][26][8][45][48][8][44]".
- "TENO6" is used as a comparator in §4.6 but never defined.
- Reference [64] prints the authors as "N.J. Von, R. Richtmyer" (von Neumann and Richtmyer); [55] (Rusanov) has no volume.

# Notation map

| Takagi et al. 2022 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $f(u)$, $\partial f/\partial u>0$ | $u$, $f(u)$ | systems through characteristic decomposition with Roe eigenvectors |
| $f_i$ | $f(u_i)$ | point flux; the paper calls it a "cell-averaged value" of $h$ |
| $h(x)$ | $\phi(x)$ | page-local on the [conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md) page: implicit function whose sliding averages are $f$ (3); **collision** with the two-point flux $h$ |
| $\hat f_{i+1/2}$ | $\hat f_{i+1/2}$ | agree; the negative-speed part is mirrored |
| $K$ | $K$ | full-stencil size, $K=5$; $K-2$ candidate stencils |
| $S_k$, $r_k$ | $S_k$, $r_k$ | **numbering differs**: $S_0$ central, $S_1$ downwind-biased, $S_2$ upwind (registry: $S_0$ most upwind); kept on this page |
| $\beta_{k,r}$ | $\beta_k$ | Jiang–Shu smoothness indicator |
| $\tau_K$, $\tau_5=\lvert\beta_{1,3}-\beta_{2,3}\rvert$ | $\tau$, $\tau_5$ | the outer stencils, as in the registry's $\lvert\beta_0-\beta_2\rvert$ after relabelling |
| $\gamma_k=\big(1+\tau_K/(\beta_{k,r}+\varepsilon)\big)^q$ | $\gamma_k$ with $C=1$ | agree |
| $\chi_k$, $\delta_k$, $C_T$, $q$ | $\chi_k$, $\delta_k$, $C_T$, $q$ | agree; $q=6$, $C_T=10^{-5}$ |
| $\varepsilon$ ($10^{-40}$ in TENO) | $\epsilon$ | the THINC monotonicity threshold $10^{-15}$ and the $\varepsilon=10^{-8}$ of §4.11 are local |
| $d_k$ ($6/10$, $3/10$, $1/10$) | $d_k$ | for $S_0$, $S_1$, $S_2$ |
| $w_k$ | $\omega_k$ | final TENO weights |
| $\beta$ (THINC steepness, 1.6) | $\beta_{\mathrm T}$ | **collision** with $\beta_k$ |
| $h_i(x)=f_++f_-\tanh(\beta(X_i-d_i))$ | $u^{\mathrm T}(x)$ | THINC profile applied to point fluxes |
| $d_i$ (jump centre) | $x^c_i$ | page-local on the [THINC](/methods/thinc-reconstruction.md) page; **collision** with the linear weights $d_k$ |
| $f_+$, $f_-$, $T$, $A$ | $f_{\mathrm m}$, $f_{\mathrm j}$, $\mathcal T$, $\mathcal A$ | page-local on the THINC page |
| $X_i$, $B=e^{\lvert\alpha\rvert\beta}$ | — | THINC auxiliaries; $B$ **collides** with the SBP boundary matrix (the THINC page writes it out) |
| $\alpha=(f_i-f_+)/f_-$ | $\varsigma$ | page-local on the THINC page; **collision** with $\alpha_k$ |
| $\zeta_i\in\{2,1,-1,0\}$ | $\zeta_i$ | detector flag (19), new |
| $h$ (Table 2), $N$ | $\Delta x$, $N_x$ | grid spacing and number of cells |
| $\beta$ in (26) | — | width parameter of the Jiang–Shu test, kept local |

# Reference list

The paper prints 76 references, numbered [1]–[76]. The list is merged complete into
the [bibliography](/bibliography.md), with `citedby` including `takagi-2022`. [64] is
recorded with its mangled author list as printed, [55] has no volume, [44] is an arXiv
preprint, [24] a conference contribution and [63] a book. No item is unparseable.

# Pages created or updated

Chunk 1 (2026-10-21), cited further in chunks 2–11 (2026-10-22/24). This source is cited on:

* [Approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
* [Bound preservation](/properties/bound-preservation.md)
* [Boundary variation diminishing (BVD)](/definitions/boundary-variation-diminishing.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Convex limiting and invariant-domain-preserving schemes](/methods/convex-limiting.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [ENO property](/definitions/eno-property.md)
* [High-Mach astrophysical jets](/benchmarks/high-mach-astrophysical-jet.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Jiang–Shu composite-wave advection](/benchmarks/jiang-shu-composite-advection.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Mapped WENO](/methods/mapped-weno.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Positivity-preserving flux limiter (Hu–Adams–Shu)](/methods/positivity-preserving-flux-limiter.md)
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)
* [Roe approximate Riemann solver](/methods/roe-riemann-solver.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Symmetry preservation](/properties/symmetry-preservation.md)
* [Targeted ENO (TENO)](/methods/targeted-eno.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
* [TENO-THINC](/methods/teno-thinc.md)
* [THINC reconstruction](/methods/thinc-reconstruction.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
* [WENO-Z weights](/methods/weno-z.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)

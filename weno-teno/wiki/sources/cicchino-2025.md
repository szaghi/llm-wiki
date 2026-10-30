---
type: Source
title: "Cicchino & Nadarajah (2025) — Discretely nonlinearly stable weight-adjusted flux reconstruction high-order method for compressible flows on curvilinear grids"
description: "Builds nonlinearly stable flux reconstruction for 3D Euler on curvilinear hexahedra with a sum-factorized weight-adjusted inverse of the FR mass matrix, proves free-stream preservation, conservation and entropy conservation, and proves that an uncollocated scheme cannot be exactly kinetic-energy preserving unless surface nodes are volume nodes."
resource: "doi:10.1016/j.jcp.2024.113532"
source_kind: paper
authors: [Cicchino A., Nadarajah S.]
year: 2025
venue: "J. Comput. Phys. 521:113532"
local_file: "/home/stefano/papers/mosaic/weno-teno/2025_Crossref_Journal_of_Computational_Physics_Cicchino_Discretely_nonlinearly_stable_weight-adjusted_flux_reconstru.pdf"
tags: [flux-reconstruction, dg, entropy-stable, kinetic-energy-preserving, performance]
timestamp: 2026-10-23T14:51:00Z
---

# Summary

The paper builds nonlinearly stable [flux reconstruction](/methods/flux-reconstruction.md)
(NSFR) for the three-dimensional compressible Euler equations on curvilinear
hexahedral grids. Following the authors' earlier work, energy-stable FR is written
as [DG](/methods/discontinuous-galerkin.md) with the modified mass matrix
$M+K_{\mathrm{FR}}$. The entropy-stable volume term is Chan's hybridized
skew-symmetric operator applied in [flux-differencing](/methods/flux-differencing.md)
(Hadamard-product) form. Its two-point fluxes are evaluated on the
[entropy-projected](/methods/entropy-projection.md) conservative variables, with the
metric cofactor matrix averaged inside the reference two-point flux. Because the FR
correction then acts on the volume terms through $M+K_{\mathrm{FR}}$, it cancels in
the entropy estimate. Classical ESFR flux differencing, with the correction on the
surface only, leaves a factor $(M+K_{\mathrm{FR}})M^{-1}$ on the volume term, which
the authors say makes it unstable.

On curved elements $M+K_{\mathrm{FR}}$ is dense and differs from element to element.
The paper replaces its inverse by a weight-adjusted inverse built from a
tensor-product reference ESFR projection, so only a diagonal matrix of Jacobian
values is inverted per element, and the operation is sum-factorized at
$O(n^{d+1})$ flops ($n=N+1$). Theorems prove order $N+1$ for the weight-adjusted
inverse, [free-stream preservation](/properties/free-stream-preservation.md),
[local and global conservation](/results/local-conservation-flux-form.md) and
discrete [entropy](/properties/entropy-stability.md) conservation in the
$(M+K_{\mathrm{FR}})$-norm. Theorem 6.4 is an impossibility result for
[kinetic energy preservation](/properties/kinetic-energy-preservation.md): an
uncollocated discretization cannot be exactly kinetic-energy preserving if the
surface quadrature nodes are not a subset of the volume nodes.

The numerical tests use the PHiLiP code. A
[manufactured solution](/definitions/method-of-manufactured-solutions.md) on a
nonsymmetrically warped grid shows order $N+1$. Maximum-CFL tables favour
$c_+$ and $c_{\mathrm{HU}}$ over $c_{\mathrm{DG}}$. An inviscid
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) on $4^3$ elements
conserves entropy to $10^{-13}$ with Gauss and Gauss–Lobatto quadrature, but
kinetic energy only with Gauss–Lobatto. Timings put NSFR-EC about 13 % above
conservative DG in CPU time. Overintegrated DG is far more expensive, and
conservative DG at $N=5$ diverges. The [SBP](/operators/summation-by-parts-operator.md)
property of the hybridized operator underlies every proof.

# Version read

The archive file is the version of record (Elsevier typeset, J. Comput. Phys.
521:113532; received 12 December 2023, online 6 November 2024), 21 pages, all read;
pages 7–9, 13 and 14 were also checked visually for equations, and Table 4 and the
§7.4 text against the text layer. Page 1 prints title, authors, venue and DOI
matching Crossref; there is no identity problem.

# Key claims

Registry notation. Page-local: $K_{\mathrm{FR}}$ the ESFR correction operator and
$c_{\mathrm{FR}}$ its parameter, with the named values $c_{\mathrm{DG}}=0$,
$c_+$ (the maximum-time-step value of Vincent et al.) and $c_{\mathrm{HU}}$ (Huynh's
$g_2$), as on [flux reconstruction](/methods/flux-reconstruction.md); $M_m$ the
element mass matrix with Jacobian, $m$ the element index; $\tilde\Pi$ the reference
ESFR projection; $\tilde u$ the entropy-projected conservative variables; $n=N+1$,
$d$ the dimension; $w_{\kappa}$ the kinetic-energy variables.

1. Nonlinear stability of FR schemes requires the FR correction functions to act on the nonlinear volume terms (§1, recalled from the authors' earlier work). **Stated**
2. NSFR is free-stream preserving, globally conservative and entropy conserving for general modal bases on quadrature rules of at least strength $2N-1$, for any ESFR correction function (§1, §6). **Proved**
3. Written as DG in the modified-norm framework, all FR contributions arise from the modified mass matrix $M_m+K_{\mathrm{FR}}$ (Eq. (36) against Eq. (24)) (§3.2). **Derived**
4. The metric splitting $\tfrac12(C_m(\xi_i)+C_m(\xi_j))$ is placed inside the reference two-point flux, Eq. (40), rather than in a physical skew-symmetric stiffness operator. The two are equivalent, but only the former allows the Hadamard product at $O(n^{d+1})$ through the tensor-product reference operator (§3.3). **Stated**
5. The weight-adjusted inverse $(M_m+K_{\mathrm{FR}})^{-1}\approx\tilde\Pi\,(\mathrm{diag}(\mathsf w_j)J_m)^{-1}\tilde\Pi^\top$ (Eq. (47)), with $\tilde\Pi=(M+K_{\mathrm{FR}})^{-1}\chi^\top\mathrm{diag}(\mathsf w_j)$ per direction (Eq. (46)), reduces the per-element cost to inverting a diagonal matrix and allows sum-factorization (§4). **Derived**
6. Theorem 4.1: the weight-adjusted inverse keeps order $O(h^{N+1})$ for $c_{\mathrm{FR}}\le c_+$. The proof uses Chan & Wilcox's weight-adjusted estimate and the numerical observation, from earlier works, that the ESFR projection has DG order for $c_{\mathrm{FR}}\le c_+$ (§4). **Proved** (partly resting on numerical evidence)
7. Sum-factorized interpolation costs $dn^{d+1}$ flops instead of $n^{2d}$, with arithmetic intensity $dn^{d+1}/\big((d+2)n^d+dn^2\big)$ (§5, Eq. (48)). **Derived**
8. Applying the weight-adjusted inverse costs $2dn^{d+1}+n^d$ flops, against $n^{2d}$ to build, $n^{3d}$ to invert and $n^{2d}$ to apply a dense mass matrix (§5). **Derived**
9. The authors' sum-factorized Hadamard product evaluates the volume–volume block in $dn^{d+1}$ flops and each surface–volume block in $dn^d$, so NSFR differs in cost from conservative strong DG only in the evaluation of the two-point flux (§5). **Stated** (from the authors' earlier paper)
10. Theorem 6.1: NSFR with the weight-adjusted inverse is free-stream preserving if the geometric conservation law holds discretely (conservative-curl metric terms, consistent surface metrics) (§6.1). **Proved**
11. Theorem 6.2: NSFR with the weight-adjusted inverse is locally conservative, because $\mathbf 1^\top K_{\mathrm{FR}}=0$ and the volume term is skew-symmetric; Remark 6.1: it is globally conservative with a telescoping flux (§6.2). **Proved**
12. Theorem 6.3: NSFR with the weight-adjusted inverse conserves entropy in the $(M_m+K_{\mathrm{FR}})$-norm if the two-point flux satisfies Tadmor's condition $[\![w]\!]\cdot f^{\mathrm{ec}}=[\![\psi]\!]$ and an entropy-conservative surface flux on entropy-projected states is used; it is therefore nonlinearly stable (§6.3, Eq. (58)). **Proved**
13. Classical ESFR flux differencing keeps $(M_m+K_{\mathrm{FR}})M_m^{-1}$ on the volume term (Eq. (56)), "which renders it unstable" (§6.3). **Derived**
14. The substitution of Tadmor's condition is possible only because the two-point flux is built from the conservative variables of the projected entropy variables (§6.3). **Derived**
15. Entropy dissipation must be added through jumps of the projected entropy variables; a jump in conservative variables with a positive scalar does not provably dissipate entropy (as recalled from Chandrashekar). Roe dissipation recast in entropy variables is used (§6.3). **Stated**
16. Theorem 6.4: an uncollocated high-order discretization cannot be exactly discretely kinetic-energy preserving if the surface quadrature nodes are not a subset of the volume nodes. The fifth component of $w_\kappa=\partial\kappa/\partial u=\big(-\tfrac12\lvert v\rvert^2,v_1,v_2,v_3,0\big)$ is zero, so $w_\kappa$ cannot be mapped back to conservative variables at surface nodes. With Gauss–Lobatto nodes (surface nodes among the volume nodes) the scheme can be kinetic-energy preserving (§6.3, Eq. (59)). **Proved**
17. Remark 6.2: a collocated scheme on Gauss nodes can be kinetic-energy preserving (Ortleb), and Theorem 6.4 does not apply to collocation (§6.3). **Stated**
18. NSFR-EC with the weight-adjusted inverse converges at order $N+1$ with $c_{\mathrm{DG}}$ and $c_+$ on the warped grid for $N=3,4,5$; the $c_+$ errors are slightly larger, a trade-off for larger steps (§7.1, Fig. 2). **Shown**
19. Maximum CFL on $4^3$ elements (Table 1), in the order $c_{\mathrm{DG}}$ Gauss, $c_+$ Gauss, $c_{\mathrm{HU}}$ Gauss, $c_{\mathrm{DG}}$ Gauss–Lobatto, $c_+$ Gauss–Lobatto: $N=3$: 0.18, 0.21, 0.22, 0.16, 0.24; $N=4$: 0.17, 0.29, 0.24, 0.14, 0.28; $N=5$: 0.17, 0.22, 0.23, 0.16, 0.20. The gain from $c_{\mathrm{DG}}$ to $c_+$ is smaller than in the linear analysis of Vincent et al. (§7.2). **Shown**
20. Unlike Gassner & Kopriva, no CFL gain from Gauss–Lobatto against Gauss nodes was found, except for $N=3$ with $c_+$; the authors attribute this to the loss of integration strength of Gauss–Lobatto rules for a rational flux on a curvilinear mesh (§7.2). **Shown** (attribution **Stated**)
21. With Gauss integration, $c_{\mathrm{HU}}$ and a Lagrange basis on Gauss–Lobatto nodes, the modified mass matrix is exactly the Gauss–Lobatto collocated mass matrix, so NSFR with $c_{\mathrm{HU}}$ is the nonlinear extension of the Gassner–Kopriva CFL gain (§7.2). **Stated**
22. For $N=3$ and $N=5$, $c_{\mathrm{HU}}$ allowed a slightly larger CFL than $c_+$; the best $c_{\mathrm{FR}}$ for nonlinear fluxes may lie slightly below the linear $c_+$, but no conclusion is drawn without a nonlinear von Neumann analysis (§7.2). **Shown** / **Stated**
23. Inviscid Taylor–Green vortex, $4^3$ elements, $N=4,5$, Cartesian and warped grids: NSFR-EC conserves entropy to $O(10^{-13})$ with Gauss and Gauss–Lobatto nodes, with and without overintegration, for $c_{\mathrm{DG}}$ and $c_+$; conservative DG on Gauss nodes diverges. Conservation and free-stream preservation hold to $O(10^{-16})$ (§7.3, Tables 2–3, Fig. 3). **Shown**
24. Kinetic energy (minus pressure work) is conserved to $O(10^{-12})$ with Gauss–Lobatto but not with Gauss nodes, as Theorem 6.4 predicts; the volume kinetic-energy identity holds to machine precision for both (§7.3, Figs. 4–5). **Shown**
25. CPU time scales as $O(N^{d+1})$ for conservative DG, overintegrated DG and NSFR-EC, and $c_{\mathrm{DG}}$ and $c_+$ cost the same; overintegrated DG costs most (§7.4, Fig. 6; four Intel i5-8600 cores, residual and inverse mass matrix applied 10 times). **Shown**
26. Full Taylor–Green runs to $t=14$ on $4^3$ and $8^3$ warped grids, $N=3,4,5$, one node with 8 AMD Rome 7532 processors, averages of 4 runs (Table 4): NSFR-EC with $c_{\mathrm{DG}}$ takes about 13 % more CPU time and 12 % more wall-clock time than conservative DG. Overintegrated DG is printed as taking "364% longer CPU time and 365% longer wall clock time" than NSFR-EC (see Printed slips). Conservative DG at $N=5$ diverges at $t=9.06$ ($4^3$) and $t=6.70$ ($8^3$) (§7.4). **Shown**
27. The conclusion states that discrete kinetic-energy preservation "is achievable only for the collocated case on Gauss-Legendre-Lobatto quadrature nodes" (§8). **Stated**

*(Compiler check, not in the sources.)* From Table 4, the mean ratio of
NSFR-EC to conservative DG over the four cases where both ran is 1.129 in CPU time
and 1.116 in wall-clock time, matching the printed 13 % and 12 %.

# Printed slips

- **§7.4:** "the overintegrated conservative DG scheme took 364% longer CPU time and 365% longer wall clock time than the NSFR-EC-$c_{DG}$ scheme". *(Compiler check, not in the sources:)* the mean ratios over the six cases of Table 4 are 3.638 (CPU) and 3.645 (wall clock): overintegrated DG takes 364 % and 365 % **of** the NSFR-EC time, that is, about 264 % and 265 % longer.
- **§8 against §6.3:** the conclusion restricts kinetic-energy preservation to the collocated case on Gauss–Lobatto nodes, while Theorem 6.4 allows any uncollocated scheme whose surface nodes are volume nodes, and Remark 6.2 allows collocation on Gauss nodes.
- **§7.1:** "$\beta=\frac1{50}$ and $l=2$ in the warping Eq. (60)", but Eq. (60) defines $l=(x_R-x_L)/(2\pi)$, which on the stated domain $[-1,1]^3$ is $1/\pi$; either $l$ is the domain length here or the value disagrees with (60).
- **§7.1:** "$c_3=\frac{\pi}{100},(\gamma-1)$", a stray comma (checked on the page image).
- **Table 1 caption:** "Max CFL for $p=4$ and $p=5$", while the sub-tables are $p=3,4,5$.
- **§7.3:** "to verify Lemma 6.4" for Theorem 6.4; "does not exit" for "exist"; §6.3 "the approximate solution in bounded".
- **§7.4:** overintegration is described as "$2(p+1)$ quadrature points" for exact integration up to degree $4p+3$, and later as "overintegrated by $2(p+1)$"; under the §7 convention (number of nodes $=(p+1)+$ overintegration) the second reading means $3(p+1)$ points.
- **§3.1:** "$p+4$ quadrature nodes (with a minimum equivalent integration strength of $2p+3$)": *(compiler check, not in the sources)* $p+4$ Gauss nodes integrate degree $2p+7$ exactly and $p+4$ Gauss–Lobatto nodes degree $2p+5$.
- **§6.1 and §1:** "Fisher and Carpenter [18]" and "Fisher and co-authors [18]", but [18] is Fisher's single-author thesis and Fisher & Carpenter is [28].

# Notation map

| Cicchino & Nadarajah (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $p$ | $N$ | DG/FR degree; **$p$ is the pressure in the registry** |
| $n=p+1$, $d$ | $n=N+1$, $d$ (page-local) | flop counts |
| $m$, $M$ (element index, number of elements) | $m$ kept, in words | **$M$ is the mass matrix in the registry** |
| $\chi(\xi^r)$, $\phi(\xi^r)$ | kept | solution basis (row vectors) and Lagrange flux basis on the quadrature nodes |
| $W$, $W_f$ | $\mathrm{diag}(\mathsf w_j)$, surface weights | **$W$ is also the conserved vector of Eq. (9)** |
| $J_m$, $C_m$ | $J$, metric cofactors ($Ja^{(d)}$) | conservative-curl form |
| $M_m$, $M+K$ | $M_m$, reference $M+K_{\mathrm{FR}}$ | |
| $K_m$, $c$, $c_{DG}$, $c_+$, $c_{HU}$ | $K_{\mathrm{FR}}$, $c_{\mathrm{FR}}$, $c_{\mathrm{DG}}$, $c_+$, $c_{\mathrm{HU}}$ (page-local) | **$K$ is the TENO stencil size and a DG element, $c$ the sound speed** |
| $c_{(s,v,w)}=c_{1D}^{(s+v+w)/p}$ | kept | tensor-product ESFR parameters |
| $S_\xi$, $D_\xi=M^{-1}S_\xi$ | $Q$, $D$ | |
| $\tilde Q-\tilde Q^\top$ | kept | hybridized skew-symmetric operator (Chan) |
| $\tilde\Pi$, $\Pi$ | $\tilde\Pi$ (page-local), $\Pi$ | reference ESFR projection; $L^2$ projection |
| $U$, $F$ | $\eta$, $F_\eta$ | convex entropy, $\partial_t\eta+\nabla\cdot F_\eta\le0$ |
| $v=U'(u)$, $\tilde v$ | $w$, projected $w$ | **collision**: $v$ is the velocity in the registry |
| $\psi_k$ | $\psi$ | entropy potential, agrees |
| $f_s$, $F^r_m$ | $f^{\mathrm{ec}}$ / $f^{\mathrm{vol}}$, matrix of reference two-point fluxes | |
| $\tilde u$ | $\tilde u$ (page-local) | entropy-projected conservative variables |
| $v_{K.E.}$ | $w_\kappa$ (page-local) | kinetic-energy variables; $\kappa$ the kinetic energy |
| $u$, $v$, $w$ (velocity components) | $v_1$, $v_2$, $v_3$ | |
| $\beta$ | $\rho/(2p)$, or the warping amplitude | **one letter for two things; not a smoothness indicator** |
| GL, LGL/GLL | Gauss, Gauss–Lobatto | |
| CFL | $\nu$ | adaptive step from the maximum wave speed; RK4 |

# Reference list

The paper prints 78 references, numbered [1]–[78], merged complete into the
[bibliography](/bibliography.md) with `citedby` including `cicchino-2025`. Ref. [35]
is the ingested [Cicchino et al. (2022)](/sources/cicchino-2022.md) and ref. [33] the
ingested [Abgrall et al. (2022)](/sources/abgrall-2022.md); ref. [36] (Cicchino et
al., provably stable FR on curvilinear elements, JCP 463:111259) is a different
work keyed `cicchino-2022-b`. Same-author same-year keys follow the printed order
(Abgrall 2018 preprint and article, Chan 2019, Vincent 2011, Castonguay 2012). Refs.
[11], [34], [35], [40] and [74] print article numbers without volumes; [5] and [71]
(Huynh's AIAA papers) print no paper number; [31] is an arXiv preprint kept as its
own entry; [39] prints "complex geometrics" in its title. No item is unparseable.

# Pages created or updated

Chunk 9 (2026-10-23), cited further in chunks 10–12 (2026-10-23/30). This source is cited on:

* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Entropy projection](/methods/entropy-projection.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Flux differencing and split-form DG](/methods/flux-differencing.md)
* [Flux reconstruction and energy-stable FR](/methods/flux-reconstruction.md)
* [Free-stream preservation](/properties/free-stream-preservation.md)
* [Kinetic energy preservation](/properties/kinetic-energy-preservation.md)
* [Local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md)
* [Method of manufactured solutions](/definitions/method-of-manufactured-solutions.md)
* [Summation-by-parts operator](/operators/summation-by-parts-operator.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)

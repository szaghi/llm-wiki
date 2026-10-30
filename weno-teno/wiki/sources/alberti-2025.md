---
type: Source
title: "Alberti et al. (2025) — Continued development of an entropy-aware high-order modal Discontinuous Galerkin solver for the Navier–Stokes equations"
description: "Modal DG for compressible Navier–Stokes with entropy-projected operators: compares five spreading terms of Abgrall's entropy correction, traces the entropy integration error to the rational pressure, and makes BR1 and BR2 viscous terms entropy stable by projecting the viscous fluxes onto the DG space."
resource: "doi:10.1016/j.compfluid.2025.106730"
source_kind: paper
authors: [Alberti L., Carnevali E., Colombo A., Crivellini A.]
year: 2025
venue: "Comput. Fluids 299:106730"
local_file: "/home/stefano/papers/mosaic/weno-teno/2025_Crossref_Computers_amp_Fluids_Alberti_Continued_development_of_an_entropy-aware_high-order_modal_D.pdf"
tags: [dg, entropy-stable, navier-stokes]
timestamp: 2026-10-23T11:24:00Z
---

# Summary

The authors' [discontinuous Galerkin](/methods/discontinuous-galerkin.md) solver uses
an orthonormal, hierarchical modal basis in physical space. The unknowns are
conservative variables, but every spatial operator is evaluated on the $L^2$
projection of the entropy variables, the
[entropy projection](/methods/entropy-projection.md). The convective part is closed
by Abgrall's [entropy correction term](/methods/entropy-correction-term.md) ("direct
enforcement of entropy balance", DEEB). The correction adds the element integration
error of the entropy flux, spread over the non-constant modes by a spreading term, so
that the semi-discrete [entropy balance](/properties/entropy-stability.md) holds
whenever the interface flux satisfies Tadmor's condition.

The paper has three contributions. (1) Four alternative spreading terms
(DEEB$_a$–DEEB$_d$) are compared with the standard one for dimensional consistency,
quadrature needs, convergence, entropy conservation, robustness and cost. DEEB$_b$ is
an entropy viscosity, and clipping the correction to its dissipative sign is tested.
(2) The integration error comes only from the rational pressure. Writing the pressure
gradient in strong form gives entropy conservation without correction but loses
momentum conservation. (3) An extra $L^2$ projection of the viscous fluxes makes the
lifting identities of the
[Bassi–Rebay discretizations](/methods/bassi-rebay-viscous-discretization.md) exact
for rational viscous matrices. This gives an entropy bound for BR2 and an
entropy-production identity for BR1.

Tests: the [isentropic vortex](/benchmarks/isentropic-vortex.md) with the Ismail–Roe
[entropy-conservative flux](/methods/entropy-conservative-flux.md) and an exact-Riemann
Godunov flux; under-resolved inviscid
[Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md) and
[Richtmyer–Meshkov](/benchmarks/richtmyer-meshkov-instability.md) runs at degrees 4–7
with no limiter, scored by a completion index; a Navier–Stokes
[manufactured solution](/definitions/method-of-manufactured-solutions.md); and a
viscous Kelvin–Helmholtz flow at Atwood number 0.99. Every DEEB variant is more robust
than the uncorrected scheme, the standard spreading term is cheapest, and only the
projected BR2 completes the hardest viscous case, at 1.34–1.62 times the cost of BR2.

# Version read

Version of record (Elsevier typeset, open access; received 28 March 2025, accepted 12
June 2025, online 24 June 2025), 17 pages, all read; pp. 2–7 and 9–12 checked on the
page images for equations, grid sizes and captions. Page 1 matches Crossref (title,
four authors, venue, DOI). The grids written $2^4\times2^4$ and $2^5\times2^5$ have
16×16 and 32×32 elements (the text extraction renders them "24 × 24", "25 × 25").
Numbering cited here is that of this version.

# Key claims

Registry notation: the source's $\mathcal S$, $\sigma_i$, $\mathbf v$, $\mathbf v_h$
are $\eta$, $F_\eta$, $w$, $w_h$; its degree $p$ is $N$. Page-local: $\mathsf r_K$ the
element entropy integration error (source $\alpha_K$); $\mathsf K_{ij}(w)$ the
symmetric viscous matrices, $F_{v,i}=-\mathsf K_{ij}\partial_jw$; $\mathsf P=\partial u/\partial w$;
$\mathsf r_F$, $\mathsf R$ the local and global lifting operators; $\mathsf p_F$ the BR2
penalty (source $\eta_F$); $\Pi_{\mathrm{BR1}}$, $\Pi_{\mathrm{BR2}}$ the projected
schemes.

1. In the entropy-projection framework the identity $\sum_K\int_K(\partial_iw_h)^\top f^{(i)}(w_h)=\sum_F\int_F[\![\psi_i(w_h)]\!]n_{F,i}$ fails under quadrature, because the integrand is not polynomial while the rule is exact only up to degree $2N$; very high-order Gauss rules are "unpractical and not very robust" (§2.1.1, Eq. (18), citing the authors' ref. [2]). **Stated**
2. Adding $\mathsf r_K$ (Eq. (20)) through the spreading term (22) recovers the semi-discrete entropy balance (25), so entropy conservation or stability holds iff the interface flux satisfies Tadmor's condition (19), printed as $[\![w_h]\!]^\top\hat f-[\![\psi_i]\!]n_{F,i}\ge0$ (§2.1.1, Eqs. (21)–(25)). **Derived**
3. Because entropy variables are used, $\mathsf r_K=\mathcal O(h_K^{2N+d})$ (§2.1.1). **Stated**
4. The spreading term leaves the constant mode untouched, so the means of the conservative variables are conserved; with the orthonormal basis it reduces to a ratio of modal coefficients (Eqs. (22)–(23)). **Derived**
5. The form of $\mathsf r_K$ of Abgrall, Öffner & Ranocha (Eq. (26)) gives entropy conservation for any numerical flux, at the price of a numerical entropy flux and a larger correction; the authors prefer entropy-conservative fluxes and keep (26) for cases without them, such as real-gas equations of state (§2.1.1). **Stated**
6. Any positive semi-definite matrix in the generic spreading term (28) gives a consistent correction, also discretely with positive-weight Gauss quadrature (§2.1.1). **Stated**
7. DEEB$_{\mathrm{std}}$ and DEEB$_c$ are quadrature free but dimensionally inconsistent; DEEB$_a$, DEEB$_b$, DEEB$_d$ are dimensionally consistent but need explicit quadrature (Table 1). **Stated**
8. DEEB$_b$, the Laplacian-like form with $\mathsf P$ replaced by $\mu^{-1}\mathsf K_{ij}$, is an entropy viscosity with a piecewise-constant virtual viscosity $\mu^*=\mathsf r_K/\int_K\partial_iw_h^\top\mu^{-1}\mathsf K_{ij}\partial_jw_h$; $\mathsf r_K<0$ means anti-diffusion, and the clipping $\mathsf r_K=\max(0,\mathsf r_K)$ enforces the balance only when entropy would grow (Eqs. (29)–(30)). **Derived**
9. The integration error comes only from the rational pressure: $\partial_i\psi_i=\partial_i(p\,w_{1+i})$ (Eqs. (31)–(32)). **Derived**
10. Treating the pressure gradient in strong form in the momentum equations (Eq. (33)) gives entropy conservation or stability without correction, but the mean momentum then receives a nonzero term (Eq. (35)): "the integration error is essentially shifted into the momentum equations" (§2.1.1). **Derived**
11. Projecting the viscous face flux onto the DG space (Eq. (37)) makes the lifting identity (13) usable for rational $\mathsf K_{ij}(w_h)$, and with Lemma 1 (a generalized Young inequality, after May) an upper bound (42) on the BR2 entropy rate follows; without the projection the identities do not hold (§2.1.2, Eqs. (36)–(42)). **Derived** (see Printed slips for the signs of (42))
12. For BR1 with the projection (44) the entropy rate is exactly $-\sum_K\int_K(\partial_iw_h+\mathsf R_i)^\top\mathsf K_{ij}(\partial_jw_h+\mathsf R_j)\le0$ (Eq. (47)), an identity where BR2 gives only a bound (§2.1.2). **Derived**
13. The BR2 penalty requirement $\mathsf p_F\ge\mathrm{card}(\mathcal F_K)+1$ is unchanged by the projection; smaller values often work in practice (§2.1.2). **Stated**
14. Isentropic vortex ($N=3,4$): all strategies (DEEB$_{\mathrm{std}}$, DEEB$_b$, strong-form pressure) converge at order $N+1$ with the Godunov flux and $N$ with the Ismail–Roe flux; DEEB$_b$ slightly lowers the errors of the entropy-conservative flux (§3.1.1, Fig. 1). **Shown**
15. The entropy conservation error converges at rate $2N+1$ with the Godunov flux and is at machine level with the Ismail–Roe flux, for DEEB$_b$ and for the strong-form pressure, which the authors call a "numerical proof" that pressure drives the integration error (§3.1.1, Fig. 2). **Shown**
16. The strong-form pressure spoils momentum conservation, with an error at least $\mathcal O(h_K^{2N+d})$, like $\mathsf r_K$ (Fig. 3). **Shown**
17. The uncorrected entropy-projection scheme (STD) is much more robust than the conservative-variable scheme, which completes the robustness tests only up to $N=1$ (ref. [2]); the strong-form pressure variant is less robust than STD and is left out of the robustness charts (§3.1.2). **Stated**
18. Kelvin–Helmholtz, Atwood 0.75, $N=4$–$7$: every DEEB variant raises the completion index over STD; DEEB$_a$ and DEEB$_b$ are more robust on triangles; clipping matters only for DEEB$_b$ on fine grids; on fine triangular grids all DEEB variants complete up to $N=3$ while STD fails for $N>1$ (§3.1.2, Fig. 4). **Shown**
19. Richtmyer–Meshkov, $N=4$–$7$: with clipping, DEEB$_a$ completes all runs and DEEB$_b$ crashes once ($N=6$); without clipping both lose robustness markedly; DEEB$_c$, DEEB$_d$, DEEB$_{\mathrm{std}}$ are insensitive to it; STD is least stable, especially on triangles (§3.1.2, Fig. 6). **Shown**
20. Cost relative to DEEB$_{\mathrm{std}}$ (Kelvin–Helmholtz, 32×32, $N=3$–$7$): DEEB$_a$ 1.2–1.3, DEEB$_b$ 1.3–1.5, DEEB$_c$ 1.2–1.3, DEEB$_d$ 1.2–1.3, on two nodes with two Intel Xeon E5-2620 v4 each, 32 MPI processes (Table 2). **Shown**
21. DEEB$_c$ could be made quadrature free through the orthonormality of the basis (§3.1.2). **Stated**
22. Manufactured solution ($\mathrm{Re}=100$, $N=1$–$6$, meshes $2^k\times2^k$, $k=1$–$4$): $\Pi_{\mathrm{BR1}}$ and $\Pi_{\mathrm{BR2}}$ keep order $N+1$, like BR1 and BR2 (§3.2.1, Fig. 8). **Shown**
23. Viscous Kelvin–Helmholtz, Atwood 0.99, $\mathrm{Re}=100$, viscosity exponent $3/4$: only $\Pi_{\mathrm{BR2}}$ reaches the final time at $N=3$, with the least entropy production in the common window, and it fails for $\mathsf p_F<2$; with exponent 0, all schemes complete for $\mathrm{Re}<500$ and only $\Pi_{\mathrm{BR2}}$ at $\mathrm{Re}=500$, with threshold $\mathsf p_F=4$ (§3.2.2, Figs. 9–12). **Shown**
24. The $\Pi_{\mathrm{BR2}}$/BR2 cost ratio is 1.34, 1.42, 1.52, 1.58, 1.62 for $N=3$–$7$; the overhead "tends to hinder its applicability in production-grade solvers" (Table 4, §4). **Shown**
25. A globally decreasing mathematical entropy does not guarantee consistent entropy evolution in each element; only $\Pi_{\mathrm{BR1}}$ and $\Pi_{\mathrm{BR2}}$ control the local entropy production (§3.2.2). **Stated**
26. DEEB$_b$ needs a Prandtl number even in inviscid runs ($\mathrm{Pr}=0.72$, "somewhat arbitrary") (Appendix). **Stated**
27. A scheme that is at once entropy conservative or stable and kinetic-energy preserving in this framework "requires special attention and is left for future work" (§1). **Stated**

# Printed slips

- **Eq. (42).** Printed: $\sum_K\int_K\partial_t\eta\le-(1+\epsilon)\sum_K\int_K\partial_iw_h^\top\mathsf K_{ij}\partial_jw_h-\frac1\epsilon\sum_K\int_K\mathsf R_i^\top\mathsf K_{ij}\mathsf R_j-\sum_K\mathsf p_F\sum_{F}\int_K\mathsf r_{F,i}^\top\mathsf K_{ij}\mathsf r_{F,j}$ for all $\epsilon>0$. *(Compiler check, not in the sources: the cross terms of (40) are $-2\sum_K\int_K\partial_iw_h^\top\mathsf K_{ij}\mathsf R_j$, and Lemma 1 bounds them from above by $+\epsilon\int\partial w^\top\mathsf K\partial w+\epsilon^{-1}\int\mathsf R^\top\mathsf K\mathsf R$. This gives $-(1-\epsilon)$ and $+\frac1\epsilon$ in place of the printed $-(1+\epsilon)$ and $-\frac1\epsilon$. The printed bound, with every term negative, is the lower-bound side of the inequality. Concluding stability from the corrected bound needs a further estimate of $\mathsf R$ by the local lifts and a large enough penalty, which the paper does not write out; its remark that "a larger $\eta_F$ increases the entropy stability" fits the corrected form.)*
- §2: $N_{\mathrm{DoF}}=\prod_{m=1}^d(k+m)/m$ uses $k$ for the degree, $p$ elsewhere.
- The penalty requirement is stated two ways: "greater than the number of cell faces" (after Eq. (14)) and "$\eta_F\ge\mathrm{card}(\mathcal F_K)+1$" (§2.1.2).
- Appendix A.3: the corner entry prints "$V_2^2$" where A.4–A.5 use lowercase $\mathrm v$.
- Table 2 caption "KHI, $A=0.33$", $p=\{3,\dots,7\}$, whereas the inviscid Kelvin–Helmholtz runs are described only at $A=0.75$, $p=4$–$7$. Table 4 caption "Viscous KHI, $A=0.95$", whereas §3.2.2 runs it at $A=0.99$.
- §3.2.2 refers to "the coarse rectilinear mesh $2^4\times2^4$ illustrated in Section 3.1.1"; that mesh is defined in §3.1.2.
- §3.1: "the alternative strategies outlined in , responsible for" has an empty cross-reference. Fig. 3 text writes "$\alpha_k$" for $\alpha_K$.
- The captions name the time integrator "SSPRK35", the text "fourth-order five-stage" (Spiteri–Ruuth).
- Refs. [18] and [38] are the same work (Gottlieb & Groth 1988, J. Comput. Phys. 78:437–458), printed twice with different initials. Ref. [1] prints "Front Phys 2022;356" with no volume.

# Notation map

| Alberti et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf q=[\rho,\rho\mathbf u,\rho E]^\top$, $\mathbf q_h$ | $u$, $u_h$ | velocity $\mathbf u$ is the registry $v$ |
| $\mathbf v$, $\mathbf v_h$ | $w$, $w_h$ | entropy variables and their $L^2$ projection |
| $\bar{\mathbf v}_h=\mathbf v_h-\mathbf v_{h,0}$ | deviation from the element mean (local) | **collision** with the cell-average bar |
| $\mathcal S=-\rho s/(\gamma-1)$, $\sigma_i=u_i\mathcal S$ | $\eta$, $F_\eta$ | same sign and scaling |
| $s=\ln(P\rho^{-\gamma})$, $P$ | $s$, $p$ | |
| $\theta=\rho$, $\psi_i=\rho u_i$ | entropy potentials; $\psi$ | agree |
| $\mathbf F_{c,i}$, $\mathbf F_{v,i}$ | $f^{(i)}$, viscous flux (local) | |
| $\mathbf K_{ij}$, $\mathbf K^*_{ij}=\mu^{-1}\mathbf K_{ij}$ | $\mathsf K_{ij}$ (local) | **collision** with the TENO $K$ and the element $K$ |
| $\mathbf P=\partial\mathbf q/\partial\mathbf v$ | $\mathsf P$ (local) | symmetric positive definite |
| $\alpha_K$ | $\mathsf r_K$ (local) | **collision** with $\alpha_k$ and the blending $\alpha$ |
| $\mu^*$ | virtual entropy viscosity (local) | |
| $p$ (polynomial degree) | $N$ | **collision** with the pressure $p$ |
| $\phi_{h,l}$, $N_{DoF}$, $Q_{\kappa,l}$, $V_{\kappa,l}$ | modal basis, its size, modal coefficients (local) | $l=1$ the constant mode |
| $[\![\circ]\!]=\circ^+-\circ^-$, $\{\circ\}$ | $[\![\cdot]\!]$, $\{\!\{\cdot\}\!\}$ | agree |
| $\mathbf r_F$, $\mathbf R$ | $\mathsf r_F$, $\mathsf R$ (local) | **collision** of $R$ with the eigenvector matrix |
| $\eta_F$ | $\mathsf p_F$ (local) | **collision** with the entropy $\eta$ |
| $\boldsymbol\Pi_F$, $\boldsymbol\Pi_i$; $\Pi_{BR1}$, $\Pi_{BR2}$ | projected viscous fluxes; projected schemes | |
| $\lambda=-\tfrac23\mu$, $\beta$ (power-law exponent; vortex strength in (52)) | bulk coefficient; local | **collision** of $\beta$ with $\beta_k$ and of $\lambda$ with the eigenvalues |
| $A$ (Atwood number), CI | Atwood number, completion index (local) | |
| $\eta(\cdot,\cdot)$, $\varepsilon(\cdot,\cdot)$ | $L^2$ error, conservation error (local) | **collision** with $\eta$ |

# Reference list

The paper prints 42 references, numbered [1]–[42]. The list is merged complete into
the [bibliography](/bibliography.md), with `citedby` including `alberti-2025`. Refs.
[18] and [38] are a printed duplicate of one work (Gottlieb & Groth 1988) and are
folded into one entry. Ref. [24] is the ingested source
[Abgrall et al. (2022)](/sources/abgrall-2022.md) and ref. [9] the ingested
[Renac (2021)](/sources/renac-2021.md). Refs. [1], [2], [24] lack a volume or article
number, and refs. [29], [31] print abbreviated book titles. No item is unparseable.

# Pages created or updated

Chunk 9 (2026-10-23), cited further in chunks 10–12 (2026-10-23/30). This source is cited on:

* [Bassi–Rebay viscous discretizations (BR1, BR2)](/methods/bassi-rebay-viscous-discretization.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Entropy correction terms](/methods/entropy-correction-term.md)
* [Entropy projection](/methods/entropy-projection.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Method of manufactured solutions](/definitions/method-of-manufactured-solutions.md)
* [Richtmyer–Meshkov instability](/benchmarks/richtmyer-meshkov-instability.md)

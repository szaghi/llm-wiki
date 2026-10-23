---
type: Source
title: "Cicchino et al. (2022) — Nonlinearly stable flux reconstruction high-order methods in split form"
description: "Shows that energy-stable flux reconstruction in split form admits no general nonlinear stability proof when the correction filter acts only on surface terms, and builds a split form that applies the filter to the volume terms as well, proved conservative and energy stable for Burgers' equation on modal, uncollocated or overintegrated bases."
resource: "doi:10.1016/j.jcp.2022.111094"
source_kind: paper
authors: [Cicchino A., Nadarajah S., Del Rey Fernández D.C.]
year: 2022
venue: "J. Comput. Phys. 458:111094"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Journal_of_Computational_Physics_Cicchino_Nonlinearly_stable_flux_reconstruction_high-order_methods_in.pdf"
tags: [dg, entropy-stable, kinetic-energy-preserving, numerical-flux]
timestamp: 2026-10-22T20:00:00Z
---

# Summary

[Energy-stable flux reconstruction](/methods/flux-reconstruction.md) (ESFR, VCJH) is
provably linearly stable on affine elements, and
[split forms](/methods/split-convective-forms.md) of the
[discontinuous Galerkin](/methods/discontinuous-galerkin.md) volume term give
nonlinear (entropy) stability, but earlier attempts to combine the two obtained a
proof only for DG itself or for Huynh's $g_2$ lumped-Lobatto scheme, which is
collocated Gauss–Lobatto [DGSEM](/methods/dgsem.md) in disguise. The paper explains
why: when the chain-rule split is applied through the differentiation matrix and the
ESFR correction filter acts only on the surface terms, the energy balance in the
broken Sobolev norm $M+K_m$ contains a volume term that is neither zero nor
sign-definite.

The remedy is to split with respect to the stiffness matrix $Q$, which has the
[summation-by-parts](/operators/summation-by-parts-operator.md) property for any
quadrature exact to degree $2N-1$, dense norms and uncollocated nodes included, and
to apply the filter $(M_m+K_m)^{-1}$ to the non-conservative volume term too; on
non-Gauss–Lobatto nodes the face term must also be split. For DG the scheme
coincides with Chan's (2018) form, which is the [flux-differencing](/methods/flux-differencing.md)
scheme with an [entropy-conservative](/methods/entropy-conservative-flux.md)
two-point flux for Burgers. For one-dimensional Burgers with split weight $2/3$ the
paper proves local and global conservation, a flux form in the sense of
[local conservation](/results/local-conservation-flux-form.md), and
[energy (entropy) stability](/properties/entropy-stability.md) with an
energy-conserving or a local [Lax–Friedrichs](/methods/lax-friedrichs-flux.md)
interface flux; a Sherman–Morrison inverse of $M_m+K_m$ on affine elements shows the
new scheme to be the DG split form plus one extra volume term.

The numerics ([Burgers tests](/benchmarks/burgers-equation-tests.md), 8 periodic
elements, $N=4,5$, run past shock formation) confirm energy conservation to
$O(10^{-12})$ with the energy-conserving flux and monotone decay with Lax–Friedrichs
on collocated, uncollocated and overintegrated nodes, where the conservative DG and
the surface-only ("classical") ESFR split forms do neither; manufactured-solution
tests give orders near $N+1$, about 5.7 for the largest stable correction parameter
at $N=5$. There is no shock-capturing component.

# Version read

arXiv 2103.02647v1 [math.NA], 3 March 2021 (title page dated 5 March 2021), 23
pages, all read; pp. 11–12 checked visually. Not the version of record: the journal
article followed peer review and may differ in sections, tests and equations.
Page 1 matches Crossref in title (title case on arXiv) and authors. Numbers cited
here are those of the arXiv v1.

# Key claims

Registry notation (see the notation map): the source's degree $p$ is $N$, its
stiffness matrix $S_\xi$ is $Q$, its quadrature weights $W$ are $\mathrm{diag}(\mathsf w_j)$,
its split weight $\alpha$ is kept (page-local, not the DG–FV blending coefficient;
$\alpha_{\mathrm s}$ on the concept pages, where $K_m$, $c$ and $\lambda$ are
written $K_{\mathrm{FR}}$, $c_{\mathrm{FR}}$ and $\lambda_{\mathrm s}$);
$M$, $D$ and $B$ agree with the registry.

1. Jameson et al. proved the FR surface reconstruction identical to the CPR correction field; ESFR recovers DG, spectral difference and spectral volume by the choice of correction function; Allaneau–Jameson (1D) and Zwanenburg–Nadarajah (3D, modal, uncollocated) recast ESFR as a filtered DG scheme (§1). **Stated**
2. Neither Ranocha, Öffner & Sonar (2016) nor Abe et al. (2018) gave a general nonlinearly stable ESFR scheme; the stable case of Abe et al. is Huynh's $g_2$ lumped-Lobatto scheme, equivalent to collocated Gauss–Lobatto DG (§1, §3). **Stated**
3. In the classical ESFR split form (Eq. 21) the energy balance (Eq. 23) contains $-(1-\alpha)u_mK_mUD u_m^\top$, with $U=\mathrm{diag}(u_m)$; $K_mUD\ne0$ and is in general not positive semi-definite, so no stability claim can be made unless $K_m=0$ or $K_m$ is diagonal (§3). **Derived**
4. Huynh's $g_2$ lumped-Lobatto scheme equals collocated Gauss–Lobatto DG, or the Huynh correction parameter with $M+K_m$ integrated exactly to degree $\ge2N$ and the volume flux on Gauss–Lobatto nodes; it is not the Huynh parameter with $M+K_m$ and volume flux on one node set (Remark 3.1, footnote 1, Tables 1–3). **Derived**, then **Shown**
5. The stiffness matrix satisfies $Q+Q^\top=\sum_f\chi(\xi_f)^\top W_f\,\mathrm{diag}(\hat n^\xi)\,\chi(\xi_f)$ for quadrature exact to degree $\ge2N-1$, whatever the node collocation (Eq. 24). **Derived**
6. The proposed ESFR strong split form (Eq. 28) applies $(M_m+K_m)^{-1}$ to the conservative volume term, the non-conservative volume term and the split face terms. **Definition** (the contribution)
7. On non-Gauss–Lobatto volume nodes the face interpolation of the volume flux differs from the flux of the face-interpolated solution, so the face term is split as $f^{*}-\alpha\chi(\xi_f)\hat f-(1-\alpha)f_f$ (§3.1, before Eq. 28). **Derived**
8. For DG, Eq. 28 equals Eq. A.14 of Chan (2018); for collocated Gauss–Lobatto DG the face splitting disappears, as in Gassner (2013) (§3.1). **Stated**
9. On affine elements $(M_m+K_m)^{-1}=M_m^{-1}-\dfrac{1}{1+c(2N+1)(N!\,c_N)^2}M_m^{-1}K_mM_m^{-1}$, with $c_N$ the leading coefficient of the Legendre polynomial $P_N$ (Lemma 3.1, Eqs. 30–32, Sherman–Morrison in a normalized Legendre basis). **Proved**
10. Since $K_mM_m^{-1}Q=0$ on affine elements, the proposed scheme is the DG split form plus one extra volume term, $\frac{1-\alpha}{1+c(2N+1)(N!\,c_N)^2}M_m^{-1}K_mM_m^{-1}\chi^\top UW\partial_\xi\chi\,\hat u^\top$ (Eq. 33). **Derived**
11. The weak form (Eq. 29) is not equivalent to integrating Eq. 26 by parts continuously and then discretizing (Remark 3.2). **Stated**
12. The strong split form is locally and globally conservative for any $\alpha$ and quadrature exact to degree $2N-1$: $\hat1(M_m+K_m)\frac{d}{dt}\hat u^\top=-\hat1\sum_f\chi(\xi_f)^\top W_f\,\mathrm{diag}(\hat n)f^{*\top}$ (§3.1.1, Eqs. 34–42). **Proved**
13. In the broken Sobolev norm $\lVert u\rVert^2_{M_m+K_m}$ the dense ESFR norm cancels against the filter (Eq. 43). **Derived**
14. With $\alpha=2/3$ the volume terms vanish and the energy rate reduces to surface terms (Eq. 46, §3.1.2). **Proved**
15. For the interface flux $f^*=\tfrac12\big(\tfrac12(u^+)^2+\tfrac12(u^-)^2\big)-\lambda(u^+-u^-)$ the interface contributes $(u^+-u^-)^2\big(\tfrac1{12}(u^+-u^-)-\lambda\big)$ to the energy rate, so stability requires $\lambda\ge\tfrac1{12}(u^+-u^-)$, with equality for the energy-conserving flux (Eqs. 47–49). **Proved**
16. Local Lax–Friedrichs, $\lambda=\tfrac12\max(\lvert u^-\rvert,\lvert u^+\rvert)\ge\tfrac1{12}(u^+-u^-)$, gives energy (entropy) stability (Eq. 50). **Proved**
17. No nonlinear stability claim can be made in general if the ESFR filter acts only on the surface (abstract, §1, Eq. 23); numerically the classical split neither conserves nor monotonically dissipates energy (Tables 1–3). **Derived** / **Shown**
18. Energy tests ($N=4,5$, 8 elements, RK4 with $\Delta t=10^{-4}$, $t=3$): the proposed split with the DG, largest-stable ($c_+$) and $c=10^4$ parameters conserves energy to $O(10^{-12})$ with the energy-conserving flux and decreases it monotonically with Lax–Friedrichs, on collocated Gauss–Lobatto (Table 1), uncollocated Gauss with $N+1$ nodes (Table 2) and overintegrated Gauss with $N+3$ nodes (Table 3); conservative DG and the classical split do neither, except the classical split with Huynh's lumped-Lobatto scheme (collocated only). **Shown**
19. All schemes are conservative to $O(10^{-16})$ (§4). **Shown**
20. Manufactured-solution convergence (Lax–Friedrichs, $t=1$): at $N=4$ conservative DG and the DG-parameter split reach order 5.02, the $c_+$ split 5.00, the classical $c_+$ split 4.98 (Table 4); at $N=5$ DG reaches 6.02, the $c_+$ split 5.70–5.76, the classical $c_+$ split 5.60–5.73 (Table 5); with overintegration the classical $c_+$ split runs from 6.33 to 5.06 ($N=4$, Table 6) and from 7.18 to 6.04 ($N=5$, Table 7). **Shown**
21. "All schemes yield the expected convergence rates of $p+1$" (§4.2). **Stated** (see Printed slips)
22. The extra volume term of Eq. 33 is of design order, as the convergence tests show (§3.1, §4.2). **Shown**
23. The maximum time step grows with $c$; $c_+$ has no analytical value and is the numerical upper limit before an order of accuracy is lost (§2.2, citing Castonguay's thesis). **Stated**
24. Building $K_m=c(D^N)^\top M_mD^N$ from the scheme's own differentiation matrix requires $c$ taken from a normalized Legendre basis (Remark 2.1). **Stated**
25. The derivation is one-dimensional; the extension to three-dimensional ESFR split forms "is straightforward" (§1). **Stated**

# Printed slips

- Eq. 29 drops a face term. Integrating the non-conservative volume term of Eq. 28 by parts with Eq. 24 leaves $-(1-\alpha)(M_m+K_m)^{-1}\chi^\top U\Pi^\top\sum_f\chi_f^\top W_f\,\mathrm{diag}(\hat n)\chi_f\hat u^\top$ (the term that appears in the paper's own Eq. 38), and it does not cancel the face term $+(1-\alpha)(M_m+K_m)^{-1}\sum_f\chi_f^\top W_f\,\mathrm{diag}(\hat n)f_f^\top$ of Eq. 28 in general, while the $\alpha$ terms do cancel. Eq. 29 shows only $f^*$ on the face, so as printed it equals Eq. 28 only when the two terms coincide (e.g. collocated Gauss–Lobatto nodes). *(compiler check, not in the sources: integration by parts of Eq. 28 with Eq. 24.)*
- §4.2: "All schemes yield the expected convergence rates of $p+1$", while Tables 5 and 7 give 5.70–5.76 for the $c_+$ split and 5.60–5.73 for the classical $c_+$ split at $p=5$; the paper's own definition of $c_+$ (§2.2) explains the shortfall, but the sentence is inaccurate.
- Eq. 12: "the ESFR scheme is derived using $p+1$ correction functions $g^{f,k}$", while the functions are indexed by face and facet node (two, $g^L$ and $g^R$, in 1D); the count is unexplained.
- Tables 1–3 label rows "EFSR Split" and "EFSR Classical Split" next to "ESFR Classical Split … Lumped-Lobatto".
- Typos: "Tamdor's" (§1), "Lax-Freidrichs" (§3.1.2), "contructing" (§1), "stablility" (§3), "does not effect the order" (§4); ref. [25] "G. Shnücke", ref. [13] "arbitraryorder".

# Notation map

| Cicchino et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $p$ | $N$ | polynomial degree; design order $N+1$; **$p$ is the pressure in the registry** |
| $N_p$, $N_{vp}$, $N_{fp}$, $N_f$ | kept | numbers of basis functions, volume and facet nodes, faces |
| $M$ (number of elements) | kept in words | **collides with the mass matrix $M$** |
| $\chi(\xi_v)$, $\chi(\xi_f)$ | kept | basis (Vandermonde) at volume and facet nodes; row-vector convention |
| $\hat u_m$, $u_m$, $U=\mathrm{diag}(u_m)$ | kept | modal coefficients, nodal values; **$U$ is not the conserved vector** |
| $\xi^r$, $J^\Omega_m$ | $\xi$, $J$ | reference coordinate and Jacobian |
| $W$, $W_f$ | $\mathrm{diag}(\mathsf w_j)$, kept | volume and facet quadrature weights |
| $M_m$, $M$ | $M$ | mass matrix with and without the Jacobian; dense in general |
| $S_\xi$ | $Q$ | stiffness matrix $\chi^\top W\partial_\xi\chi$ |
| $D=M^{-1}S_\xi$, $D^p$ | $D$, $D^N$ | differentiation matrix and its $N$-th power |
| $B=\mathrm{diag}[-1,\dots,1]$ | $B$ | agrees |
| $K_m=c(D^p)^\top M_mD^p$ | $K_{\mathrm{FR}}$ (page-local) | ESFR correction operator; **$K$ is the TENO stencil size and a DG element in the registry** |
| $c$, $c_{DG}$, $c_{SD}$, $c_{HU}$, $c_+$ | $c_{\mathrm{FR}}$, $c_{\mathrm{DG}}$, $c_{\mathrm{SD}}$, $c_{\mathrm{HU}}$, $c_+$ (page-local) | ESFR correction parameter; **$c$ is the sound speed in the registry** |
| $c_p=\frac{(2p)!}{2^p(p!)^2}$ | $\mathsf c_N$ (page-local) | leading Legendre coefficient |
| $g^{f,k}$, $g^L$, $g^R$ | kept | correction functions; **$g$ is the mapped-WENO function in the registry** |
| $\Pi^p_m$ | $\Pi$ | discrete $L^2$ projection |
| $\hat f^r_m$, $f^{*,r}_m$, $f^{C,r}_m$, $f^r_f$ | $\hat f$, $f^*$, kept, $f_f$ | projected flux, numerical flux, correction flux, flux of face values |
| $\alpha$ | $\alpha_{\mathrm s}$ (page-local) | split weight, $2/3$ for Burgers; **not the DG–FV blending coefficient $\alpha$** |
| $\lambda$ | $\lambda_{\mathrm s}=a/2$ (page-local) | dissipation coefficient of the interface flux; local Lax–Friedrichs has $a=\max\lvert u\rvert$ |
| $w_0$, $v_p$ | $u^+$, $u^-$ | right and left traces at an interface; **$w$ is the entropy variable in the registry** |
| $\lVert u\rVert^2_{M+K}$ | kept | broken Sobolev (ESFR) norm; energy $=\tfrac12u^2$ entropy |
| GLL, GL | Gauss–Lobatto, Gauss | node families |

# Reference list

34 printed references, numbered [1]–[34], all parsed and merged complete into the
[bibliography](/bibliography.md) with `citedby` `cicchino-2022`. Undated items
take the citing paper's year with a note: [32] (Castonguay's thesis) as
`castonguay-2022`, [23] ("accepted in JCP") as `crean-2022` and [25] (submitted) as
`friedrich-2022`; [31] and [34] print article numbers without volumes; [5] is a book
and [15], [32] are theses. No printed duplicates were found.

# Pages created or updated

Chunk 3 (2026-10-22), cited further in chunks 4–7 (2026-10-23). This source is cited on:

* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Discontinuous Galerkin spectral element method (DGSEM)](/methods/dgsem.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)
* [Flux differencing and split-form DG](/methods/flux-differencing.md)
* [Flux reconstruction and energy-stable FR](/methods/flux-reconstruction.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md)
* [Split convective forms](/methods/split-convective-forms.md)
* [Summation-by-parts operator](/operators/summation-by-parts-operator.md)

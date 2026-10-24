---
type: Source
title: "Kurganov et al. (2023) — Well-balanced path-conservative central-upwind schemes based on flux globalization"
description: "Second-order finite-volume path-conservative central-upwind schemes for non-conservative systems that reconstruct equilibrium variables, let the global part of the flux jump at interfaces and correct the numerical diffusion, and so preserve discontinuous and moving steady states of nozzle flow and two-layer shallow water exactly."
resource: "doi:10.1016/j.jcp.2022.111773"
source_kind: paper
authors: [Kurganov A., Liu Y., Xin R.]
year: 2023
venue: "J. Comput. Phys. 474:111773"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Journal_of_Computational_Physics_Kurganov_Well-balanced_path-conservative_central-upwind_schemes_based.pdf"
tags: [well-balanced, central-scheme, path-conservative, non-conservative-systems, finite-volume]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper builds second-order, well-balanced finite-volume schemes for one-dimensional
non-conservative systems $\partial_tu+\partial_xf(u)+\mathcal C(u)\partial_xu=0$ whose steady
states satisfy $\partial_xf+\mathcal C\partial_xu=\mathsf M(u)\partial_x\mathsf E(u)$ with $\mathsf M$
invertible, so that a steady state is $\mathsf E(u)\equiv$ const for algebraically given
equilibrium variables $\mathsf E$ (page-local). It combines two existing ingredients.
[Flux globalization](/methods/flux-globalization.md) rewrites the system in the
quasi-conservative form $\partial_tu+\partial_xK=0$ with a global flux
$K=f-\mathcal G$ and solves it with a Riemann-solver-free
[central-upwind](/methods/central-upwind-scheme.md) flux. The
[path-conservative](/methods/path-conservative-scheme.md) central-upwind (PCCU) scheme of Castro
Díaz, Kurganov and Morales de Luna integrates the non-conservative product inside cells and
along a path across interfaces.

The straightforward flux-globalized scheme assumes $\mathcal G$ continuous, reconstructs
$K$ and preserves only smooth steady states. The new scheme lets $\mathcal G$ jump at every
interface and computes its one-sided values recursively from the PCCU cell and interface
integrals. It reconstructs $\mathsf E$ instead of $K$, uses a path linear in $\mathsf E$,
and evaluates the integrals by trapezoidal quadratures; Theorem 4.1 proves that the global
fluxes are then constant at discrete steady states. Because $u^+\ne u^-$ at a discontinuous
steady state, the diffusion term of the flux is rebuilt from modified states. Remark 4.2 shows
that the result can be written as a local PCCU scheme with a modified diffusion term.

The schemes are written out for isentropic nozzle flow with a discontinuous cross-section and
for the two-layer [shallow-water equations](/definitions/shallow-water-equations.md) over a
discontinuous bottom, with Newton inversions of $\mathsf E\mapsto u$. Seven 1D examples (SSP-RK3,
CFL 1/2, generalized minmod with parameter 1.3) show
[well-balancing](/properties/well-balancing.md) to machine precision for discontinuous steady
states, convergence to discontinuous and moving-water steady states, and clean propagation of
small perturbations, where the original PCCU scheme and the flux-globalized scheme without the
new ingredients fail or oscillate. No convergence-order study is reported.

# Version read

Version of record (Elsevier typeset, J. Comput. Phys. 474:111773, © 2022, online 17 Nov 2022),
32 pages, DOI printed on page 1. Title and authors match Crossref. The equations of
pp. 4–5, 8–11, 13–15 and 27–28, garbled in the text layer, were read on the page images.
Section, equation, table and figure numbers are those of this version.

# Key claims

Registry notation with the page-local symbols of the [path-conservative](/methods/path-conservative-scheme.md)
page: the system is $\partial_tu+\partial_xf+\mathcal C\partial_xu=0$ (the source writes
$U_t+F_x=BU_x$, so $B=-\mathcal C$), cell index $i$, one-sided speeds $a^\pm_{i+1/2}$, cell and
interface integrals $\mathcal B_i$, $\mathcal B_{\Psi,i+1/2}$ (the source's $B_j$, $B_{\Psi,j+1/2}$
with opposite sign). Equilibrium variables $\mathsf E$, matrix $\mathsf M$, global flux
$K=f-\mathcal G$ with $\mathcal G(x)=-\int_{\hat x}^x\mathcal C(u)\partial_\xi u\,d\xi$, all
page-local (see the Notation map).

1. Weak solutions of the non-conservative system cannot be understood in the distributional sense; discontinuous solutions are understood as Borel measures (Dal Maso–LeFloch–Murat), the basis of path-conservative finite-volume schemes (§1). **Stated**
2. For many balance-law systems $\partial_xf+\mathcal C\partial_xu=\mathsf M(u)\partial_x\mathsf E(u)$ (1.4); if $\mathsf M$ is invertible, steady states satisfy $\mathsf E(u)\equiv$ const (1.5). The paper restricts itself to $\mathsf E$ given by an algebraic relation; integral (global) equilibrium variables are left to future work (§1). **Stated**
3. The first-order PCCU scheme (2.1)–(2.2) coincides with the semi-discrete [HLL](/methods/hll-riemann-solvers.md) scheme for non-conservative systems (Remark 2.2, citing Castro, Morales de Luna & Parés 2017). **Stated**
4. The flux-globalization central-upwind schemes of Chertock, Kurganov et al. rest on the continuity of the global part $\mathcal G$; for a non-conservative system $\mathcal G$ is no longer continuous, so a direct extension does not give a robust well-balanced method (§1). **Stated**
5. The straightforward flux-globalized scheme of §3 (reconstruct $K$, recover $u^\pm$ from $K(u^\pm)=K^\pm$) preserves only smooth steady states $K\equiv$ const; neither it nor the original PCCU scheme preserves general, possibly discontinuous, steady states (§4, opening). **Stated**, and **Shown** in Examples 1 and 4.
6. Theorem 4.1: with the one-sided global parts $\mathcal G^-_{1/2}=0$, $\mathcal G^-_{i+1/2}=\mathcal G^+_{i-1/2}-\mathcal B_i$, $\mathcal G^+_{i+1/2}=\mathcal G^-_{i+1/2}-\mathcal B_{\Psi,i+1/2}$ and $K^\pm_{i+1/2}=f(u^\pm_{i+1/2})-\mathcal G^\pm_{i+1/2}$ (4.1)–(4.4), piecewise-linear reconstruction of $\mathsf E$ (4.5), the path $\mathsf E(\Psi_{i+1/2}(\mathsf s))=\mathsf E^-+\mathsf s(\mathsf E^+-\mathsf E^-)$ (4.7) and the trapezoidal quadratures (4.8), (4.10), discrete data at a steady state $\mathsf E_i\equiv\hat{\mathsf E}$ give $K^+_{i+1/2}=K^-_{i+1/2}=K^+_{i-1/2}$ for all $i$ (4.11) (Theorem 4.1, p. 7). **Proved**
7. With the plain central-upwind diffusion term $\frac{a^+a^-}{a^+-a^-}(u^+-u^-)$ of (3.3), the scheme is well-balanced only if $a^+_{i+1/2}a^-_{i+1/2}=0$ or $u^+_{i+1/2}=u^-_{i+1/2}$ at every interface; at steady states with $\mathsf E^+=\mathsf E^-$ but $u^+\ne u^-$, generic in Examples 1 and 5, the residual (4.14) does not vanish (§4.2). **Derived**
8. Replacing $u^\pm$ in the diffusion term by modified states $\check u^\pm_{i+1/2}$ (page-local) defined by $\check{\mathsf E}(\check u^\pm)=\mathsf E^\pm$ (4.16), built so that $\check u^+=\check u^-$ whenever $\mathsf E^+=\mathsf E^-$ and $\check u^\pm=u^\pm+\mathcal O(\Delta x^2)$ for smooth solutions, restores well-balancing; the modified states enter only the numerical diffusion, never the global fluxes (§4.2, (4.15)). **Derived**
9. Since $K$ is no longer reconstructed, the new scheme can be rewritten in local form: it is the PCCU scheme (2.1) with the flux (2.2) whose diffusion term uses $\check u^\pm$, which eases extension to several dimensions and unstructured grids (Remark 4.2). **Derived**
10. Many non-conservative systems have a last component $\mathsf W$ with $\partial_t\mathsf W=0$ (cross-section for the nozzle, bottom for two-layer shallow water); the modified states then use $\check{\mathsf W}_{i+1/2}=(\mathsf W^+_{i+1/2}+\mathsf W^-_{i+1/2})/2$ (4.18)–(4.19) (Remark 4.3). **Derived**
11. For the nozzle system the quadratures (5.6)–(5.7) make Theorem 4.1 hold; the modified $(\Sigma\rho)^\pm$ come from (5.11) with the averaged cross-section $(\Sigma^++\Sigma^-)/2$ and coincide with the reconstructed ones whenever $\Sigma^+=\Sigma^-$ (§5). **Derived**
12. For the two-layer system the quadratures (6.6)–(6.7) are well-balanced; the systems (6.12)–(6.13) for the modified depths may have several solutions even at a steady state, and Algorithm 6.1 (solve the "$-$" system first, use its solution as the Newton initial guess for the "$+$" system) gives equal modified states on both sides at steady states (§6). **Derived**; the independence of the order of the two steps (Remark 6.1) is **Shown** only as numerical experience, without data.
13. The nozzle inversion equation (A.1) has a unique positive root when $q^+_{\mathrm n}=0$ and otherwise up to two (supersonic and subsonic); the sonic root is $h_0^+=\big((q^+_{\mathrm n})^2/(\kappa_{\mathrm p}\gamma\mathsf z^+)\big)^{1/(\gamma+1)}$ and the inflection point $h_1^+=\big(3(q^+_{\mathrm n})^2/(\kappa_{\mathrm p}\gamma(2-\gamma)\mathsf z^+)\big)^{1/(\gamma+1)}$, with $h=\Sigma\rho$ and $\mathsf z=\Sigma^{1-\gamma}$; Newton from an initial guess chosen by the Mach number in the convex region converges monotonically and quadratically (Appendix A, Algorithm A.1). **Derived** *(compiler check, not in the sources: for $\Phi(h)=q^2/(2h^2)+\frac{\kappa_{\mathrm p}\gamma}{\gamma-1}\mathsf zh^{\gamma-1}-\mathsf E$, $\Phi'=0$ gives $h^{\gamma+1}=q^2/(\kappa_{\mathrm p}\gamma\mathsf z)$ and $\Phi''=0$ gives $h^{\gamma+1}=3q^2/(\kappa_{\mathrm p}\gamma(2-\gamma)\mathsf z)$, the printed $h_0^+$ and $h_1^+$.)*
14. Example 1 (discontinuous nozzle steady state, $N_x=200$, $t=20$): the well-balanced PCCU scheme preserves the steady state with $L^1$ and $L^\infty$ errors $0$ in $q_{\mathrm n}$ and $8.88\times10^{-16}$ in $\mathsf E$ (Table 7.1). **Shown**
15. Example 1 at $N_x=5000$, $t=0.16$: neither the non-well-balanced PCCU scheme nor the flux-globalized scheme of §3 preserves the discontinuous steady state (Fig. 7.1). **Shown**
16. Example 1, convergence to a discontinuous steady state ($t=200$, $N_x=250$): the new scheme gives $q_{\mathrm n}=-13.583$ and the §3 scheme $-13.973$, against the exact $q_{\mathrm n}\approx-13.446$ of Cuong & Thanh; the non-well-balanced PCCU scheme does not converge to the exact steady state, and the §3 scheme's $\mathsf E$ has a small jump at $x=0$ (§7.1). **Shown**
17. Example 2 (six nozzle Riemann problems of Kröner & Thanh): the new scheme agrees with the exact solutions of Kröner & Thanh's Tests 3–7 and 9 and "clearly outperforms" their well-balanced scheme; the non-well-balanced PCCU scheme is reasonable only in Tests 1, 3, 5, 6 and fails in Tests 2 and 4 even at $N_x=1000$; the §3 scheme has lower resolution, especially in Tests 2, 5, 6 at $N_x=100$. **Shown** (no figure of the Kröner–Thanh scheme is given)
18. Example 3 (smooth convergent and divergent nozzles): both well-balanced schemes propagate a $10^{-2}$ perturbation without oscillations, the non-well-balanced PCCU scheme produces large oscillations; the new scheme is slightly sharper, especially for the convergent nozzle. **Shown**
19. Example 4 (discontinuous convergent–divergent nozzle): at $N_x=1000$ the §3 scheme produces large spikes near $x=7.5$ and $12.5$ and converges to a discrete steady state with non-constant $\mathsf E$, the new scheme to the steady state (5.3); the §3 scheme generates substantial spurious waves in the perturbation test even at $N_x=2000$. **Shown**
20. Example 5 (two-layer steady state over a step, $N_x=100$, $t=0.05$): the new scheme preserves the discontinuous steady state exactly, the original PCCU scheme does not and produces spurious waves for a $10^{-3}$ perturbation at both $N_x=200$ and $1000$. **Shown**
21. Example 6 (two-layer Riemann problems over a step): the original PCCU scheme shows spikes and oscillations at $N_x=100$, and still significant spikes and inaccuracy near $x=0$ at $N_x=1000$; the new scheme does not. **Shown**
22. Example 7 (two-layer moving-water steady state over a bump): the new scheme converges to a discrete moving-water steady state by $t=100$ and resolves a $10^{-4}$ perturbation better than the original PCCU scheme (§7.2). **Shown**
23. The original PCCU scheme applied to the two-layer system (1.11) preserves only lake-at-rest states $v_1=v_2\equiv0$, $h_1\equiv$ const, $w=h_2+b\equiv$ const (§1, §4). **Stated**
24. Upwind well-balanced nozzle methods (Coquel, Saleh & Seguin; Cuong & Thanh) are accurate but complicated, needing exact or sophisticated approximate Riemann solvers; the new scheme is "substantially simpler yet as accurate or even more accurate" (§1). **Stated** (no comparison with those methods beyond the exact $q$ of Example 1)
25. Replacing the cross-section by a continuous piecewise-linear interpolant in the §3 scheme gives slightly more accurate and less oscillatory results in many examples but fails to capture the steady state of Example 4 (Remark C.1). **Shown** (stated from experiments, no figure)

# Printed slips

- §7.1, p. 15: the text sets "$\gamma=1.4$ (except for Example 1, where $\gamma=1.6$)" and states that the data (7.2) give "$q(x,0)\equiv3$ and $E(x,0)\equiv5.5$". *(compiler check, not in the sources: with $\kappa_{\mathrm p}=1$, $\rho=p^{1/\gamma}$ and $\mathsf E=v^2/2+\frac{\gamma}{\gamma-1}\rho^{\gamma-1}$, the states $(\Sigma,p,v)=(1.5,1,2)$ and $(2.5,0.326848262627536,2.413875590219353)$ give $q_{\mathrm n}=3$ and $\mathsf E=14/3\approx4.6667$ on both sides for $\gamma=1.6$; for $\gamma=1.4$ the left state gives $\mathsf E=5.5$ but the right state gives $q_{\mathrm n}=2.715$, $\mathsf E=5.456$.)* The data are a steady state for $\gamma=1.6$, with $\mathsf E\equiv14/3$; the printed $5.5$ is the left-state value for $\gamma=1.4$.
- p. 13, after (6.11): "At the cell interfaces $x=x_{j+1/2}$ at which $s^+_{j+\frac12}s^-_{j-\frac12}=0$ or $Z^+_{j+\frac12}=Z^-_{j-\frac12}$". The general rule (4.15), the nozzle analogue (p. 11) and the closing remark on p. 14 ("whenever $Z^+_{j+\frac12}=Z^-_{j+\frac12}$") use the index $j+\frac12$ on both sides.
- p. 10: "the global flux $\boldsymbol K$ in (5.1)": $\boldsymbol K$ is defined in (5.2); (5.1) defines $U$, $F$, $B$.
- p. 9: "the studied system (1.7), (5.2)" and "the nozzle flow system (1.7), (5.2)": the quasi-conservative system is (1.6) with (5.2), as written later on pp. 10–11; (1.7) is the global part of the balance-law case.
- p. 19, Example 3: "the NWB PCCU scheme produces large physical oscillations", where the context requires "unphysical".
- p. 26, Example 7: the domain is $[0,20]$ with free boundary conditions at $x=20$, yet the text describes "a secondary wave around $x\in[18,22]$", and the axes of Fig. 7.21 run to 25. Either the domain or the interval is misprinted.
- Grammar: "the RHS of (4.14) will vanished" (p. 8); "unphysical waves are still presence" (p. 23).

# Notation map

| Kurganov et al. 2023 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $F(U)$ | $u$, $f(u)$ | |
| $B(U)$, product on the right, $U_t+F_x=BU_x$ | $-\mathcal C(u)$, $\partial_tu+\partial_xf+\mathcal C\partial_xu=0$ | sign convention of the path-conservative page |
| $\mathcal A(U)=\partial F/\partial U-B$ | $A+\mathcal C$ | quasilinear matrix, eigenvalues $\lambda_l$ |
| $S(U)$ | $S(u)$ | balance-law source |
| $K=F-R$, $R=\int^x_{\widehat x}BU_\xi\,d\xi$ | $K=f-\mathcal G$ (page-local) | **collision** with $K$ (TENO points, element) and $R$ (right eigenvectors) |
| $M(U)$, $E(U)$ / $\boldsymbol E$ | $\mathsf M(u)$, $\mathsf E(u)$ (page-local) | **collision** with the mass matrix $M$ and the total energy $E$; in §5 the source's scalar $E$ is also the Bernoulli-type energy, an overload inside the source |
| $C_j$, $j$, $\overline U_j$ | $I_i$, $i$, $\bar u_i$ | |
| $U^\mp_{j+1/2}$ | $u^\mp_{i+1/2}$ | agree |
| $N$ (number of cells) | $N_x$ | |
| $s^\pm_{j+1/2}$ | $a^\pm_{i+1/2}$ | one-sided speeds; the source's cross-section $a$ is renamed instead |
| $\mathcal F_{j+1/2}$, $\mathcal K_{j+1/2}$ | $\hat f_{i+1/2}$, numerical flux of $K$ | central-upwind (HLL) form |
| $B_j$, $B_{\Psi,j+1/2}$ | $-\mathcal B_i$, $-\mathcal B_{\Psi,i+1/2}$ | page-local symbols of the path-conservative page |
| $\Psi_{j+1/2}(s)$, $s$ | $\Psi_{i+1/2}(\mathsf s)$, $\mathsf s$ | path and parameter |
| $\widehat U^\pm$, $\widehat E$, $\widehat W$ | $\check u^\pm$, $\check{\mathsf E}$, $\check{\mathsf W}$ (page-local) | **collision**: the hat is the numerical flux in the registry; the source also uses the hat for steady constants $\widehat K$, $\widehat E$ |
| $V$, $W$, $G$, $C$, $D$ | — | split $(V,W)$ with $W_t=0$ (Remark 4.3); the source's $C$ is not the registry $\mathcal C$ |
| $\theta$ (generalized minmod, 1.3) | $\theta$ (page-local) | **collision** with the Zhang–Shu factor $\theta$; kept page-local as on the central-upwind and flux-globalization pages |
| $a(x)$ (nozzle cross-section) | $\Sigma(x)$ (page-local) | **collision** with the wave speed $a$ |
| $\rho$, $u$, $p$, $\gamma$ | $\rho$, $v$, $p$, $\gamma$ | velocity $u\to v$ |
| $p=\kappa\rho^\gamma$ | $p=\kappa_{\mathrm p}\rho^\gamma$ | **collision** with the kinetic energy $\kappa$ |
| $q=a\rho u$ (nozzle), $q_i=h_iu_i$ (two-layer) | $q_{\mathrm n}=\Sigma\rho v$, $q_k=h_kv_k$ | discharges; $q_{\mathrm n}$ as on the flux-globalization page |
| $h_1$, $h_2$, $Z$, $g$, $r$, $w=h_2+Z$ | $h_1$, $h_2$, $b$, $g$, $r$, $w=h_2+b$ | as on the well-balancing page; $r$ is page-local (registry $r$: stencil points) |
| $E_1$, $E_2$ | $\mathsf E_1$, $\mathsf E_2$ | layer Bernoulli energies |
| $h^\pm$, $Z^\pm$ (App. A) | $h^\pm=(\Sigma\rho)^\pm$, $\mathsf z^\pm=(\Sigma^\pm)^{1-\gamma}$ | local re-use of $h$ and $Z$ in the source |
| $\mathcal M^\pm$ | local Mach number | registry $M$ |
| $\varepsilon=10^{-4}$, $\lambda=0.9$ (Alg. A.1), $\delta=10^{-3}$ (B.2) | — | Newton-guess constants; not the WENO $\epsilon$, not eigenvalues |

# Reference list

The paper prints 45 references, numbered [1]–[45] and sorted alphabetically. The list is
merged complete into the [bibliography](/bibliography.md), with `citedby` including
`kurganov-2023`. Same-author same-year works take suffixes in printed order (Chertock 2018
[10], [12], [13]; Kurganov 2007 [26], [30]; Cuong [18], [19]). [14] (Chertock et al., J. Sci.
Comput. 90, 2022) prints no article number or pages; [33] (LeFloch 1989) is an IMA preprint;
[34] (LeFloch 2002) prints the book title and subtitle in an unusual order. [21] prints the
first author as "D. Donat" and [22] the second author as "J.M. Corderán"; both are kept as
printed. No item is unparseable.

# Pages created or updated

Chunk 6 (2026-10-23), cited further in chunks 7–10 (2026-10-23). This source is cited on:

* [Central-upwind schemes](/methods/central-upwind-scheme.md)
* [Flux globalization for balance laws](/methods/flux-globalization.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Path-conservative schemes](/methods/path-conservative-scheme.md)
* [Shallow-water equations](/definitions/shallow-water-equations.md)
* [Shallow-water flow over a bump and lake at rest](/benchmarks/flow-over-a-bump.md)
* [Well-balancing](/properties/well-balancing.md)

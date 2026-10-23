---
type: Source
title: "Dzanic & Witherden (2023) — Positivity-preserving entropy filtering for the ideal magnetohydrodynamics equations"
description: "Extends entropy filtering of nodal DG and flux-reconstruction schemes to ideal MHD with Powell's source term through an operator-split pair of filters, and replaces the filter-strength optimization by a precomputed, nodewise root-bracketing algorithm that is 2.4 to 6.5 times faster on GPUs."
resource: "doi:10.1016/j.compfluid.2023.106056"
source_kind: paper
authors: [Dzanic T., Witherden F.D.]
year: 2023
venue: "Comput. Fluids 266:106056"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Computers_amp_Fluids_Dzanic_Positivity-preserving_entropy_filtering_for_the_ideal_magnet.pdf"
tags: [entropy-filtering, flux-reconstruction, dg, mhd, bound-preserving, shock-capturing]
timestamp: 2026-10-23T16:00:00Z
---

# Summary

The paper carries the authors' [entropy filtering](/methods/entropy-filtering.md)
(Dzanic & Witherden 2022) from the Euler equations to ideal MHD, discretized by
nodal discontinuous spectral element methods: nodal DG and
[flux reconstruction](/methods/flux-reconstruction.md) with DG correction
functions, implemented in PyFR. The
[solenoidal constraint](/properties/divergence-free-magnetic-field.md) is
handled by Powell's eight-wave non-conservative source term, evaluated with
the *global* discrete divergence of $B$ (interior term plus interface jump
term). The source term breaks the argument that the element mean of the update
is a convex combination of first-order states, so the authors split the filter:
the conservative flux update is filtered by $H_e$, which enforces positivity of
$\rho$ and $p$ and a local discrete minimum principle on $p\rho^{-\gamma}$; the
explicit source contribution is then added and only positivity is re-enforced
by a second filter $H_p$. They state that positivity of the DG element mean
with a field that is not exactly divergence-free is unproven, so the existence
of an admissible filter strength is not guaranteed after the source step. This
qualifies the [bound preservation](/properties/bound-preservation.md) claimed
in the title.

The second contribution is an efficient strength solve. It works on
$f=e^{-\zeta_{\mathrm F}}\in[0,1]$, precomputes the degree-$k$ components of
the element solution, so that the filtered solution is a polynomial in $f$, and
solves node by node with the Illinois method, each node's root bracketing the
next. On a 3D magnetized [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md)
run on 16 V100 GPUs this is 2.4 times ($N=3$) and 6.5 times ($N=4$) faster
than the repeated matrix–vector evaluation of the 2022 paper.

The evidence is numerical; no theorem is proved. The tests are a near-vacuum
magnetized vortex (convergence rates between $N$ and $N+1$, negligible filter
activity), the [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md), the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) against a WENO
reference, a shock–cloud interaction against Wu–Shu's positivity-preserving DG
with WENO limiter, an extreme [magnetized blast wave](/benchmarks/mhd-blast-wave.md)
(pressure ratio $10^5$) on triangles, and the 3D Rayleigh–Taylor instability
in hydrodynamic, weakly and strongly magnetized regimes.

# Version read

arXiv 2301.03129v2 [math.NA], stamped 17 Sep 2023, in the Elsevier preprint
template ("Preprint submitted to Elsevier"), not the typeset version of record;
24 pages. Title and authors match page 1 and Crossref (Crossref gives the second
author as "Witherden F."; page 1 prints F. D. Witherden). Section, equation,
table and figure numbers are those of the arXiv v2.

# Key claims

Registry notation: $N$ is the polynomial degree (the source's $p$, $\mathbb P_p$),
$p$ the thermal pressure (the source's $P$), $\zeta_{\mathrm F}$ the filter
strength and $n_j$ the total degree of mode $j$, as on the
[entropy filtering](/methods/entropy-filtering.md) page; $\sigma_{\mathrm s}=p\rho^{-\gamma}=e^{s}$
is the source's entropy functional (page-local, see the Notation map).

1. Entropy filtering extends to ideal MHD on nodal DG/FR, combined with Powell's eight-wave source term. It resolves strong discontinuities robustly "without tunable parameters" and recovers high-order accuracy in smooth regions (Abstract, §1, §6). **Shown**
2. The entropy solution of ideal MHD satisfies a minimum principle on the specific entropy, $\sigma_{\mathrm s}(u(x,t+\Delta t))\ge\min_x\sigma_{\mathrm s}(u(x,t))$, as in gas dynamics (Tadmor); attributed to Dao & Nazarov in the vanishing-viscosity sense (§2.1, Eq. (5)). **Stated**
3. Only the Powell-modified, non-conservative form of ideal MHD is symmetrizable and Galilean invariant when $B$ is not exactly solenoidal; with the source term, $\nabla\cdot B$ is suppressed to the order of the approximation error; the non-conservative form can give inaccurate predictions near discontinuities (Tóth) (§2.3). **Stated** (cited)
4. The global discrete divergence (interior term plus interface jump term, Eq. (19)) is used in the source term rather than the local interior divergence (Eq. (18)). The global one is called "correct" because its space is consistent with the solution space; the local one is "usually sufficient" in practice (§2.3). **Stated**
5. With the source term, $\bar u^{n+1}\in G$ (positivity and entropy) is not guaranteed under the usual assumptions on the Riemann solver, the CFL condition and SSP time stepping. Wu & Shu showed positivity of the mean if $B$ is locally divergence-free; Bouchut et al. with the Zhang–Shu mean/Godunov equivalence give $\bar u^*\in G$ for the source-free update $u^*=u^n+\Delta t\,\mathcal L_1(u^n)$ (§3.2, Eqs. (29)–(31)). **Stated**
6. Operator-split filtering, $\tilde u^*=H_e[u^n+\Delta t\,\mathcal L_1(u^n)]$, $\tilde u^{n+1}=H_p[\tilde u^*+\Delta t\,\mathcal L_2(u^n)]$, with $\mathcal L_1=-\nabla\cdot f$ and $\mathcal L_2$ the Powell source (§3.2, Eqs. (32)–(33)). **Derived** (construction)
7. It "remains to be proven" that the element mean of nodal DG preserves positivity of density and pressure when $B$ is not exactly locally divergence-free, so the existence of a positivity-preserving filtered solution is not mathematically guaranteed when small divergence errors are present (§3.2). **Stated** (open gap)
8. The positivity filter $H_p$ is "very rarely" needed: the entropy constraints on $\tilde u^*$ are usually restrictive enough that positivity is only checked (§3.2). **Stated** (no numbers)
9. The source is split explicitly as $\mathcal L_2(u^n)$, not as $\mathcal L_2(u^*)$ in Strang fashion, so as not to limit temporal accuracy (§3.2). **Stated**
10. Unless the linear kernel that recovers the Zhang–Shu scaling limiter is used, the filtered field's divergence can grow; the nonlinear filter may introduce minor divergence errors, which the source term mitigates at the next update; the effects were "found to be negligible" (§3.2). **Stated**
11. The splitting extends to SSP-RK3 as $H_p[H_e[\cdot]+\cdot]$ at every stage, with the entropy bounds of $H_e$ taken from the previous stage (§3.2, Eq. (34)). **Derived**
12. A feasible filter strength exists if the element mean satisfies the constraints; the problem is nonlinear and non-convex in one scalar, any root-bracketing solver works, and convergence to a local minimum suffices (§3.1). **Stated** (from the 2022 paper)
13. The constraints are implemented with a tolerance, $\rho-\epsilon_{\mathrm f}$, $p-\epsilon_{\mathrm f}$ and $\sigma_{\mathrm s}-\sigma_{\mathrm s,\min}-\epsilon_{\mathrm f}$, with $\epsilon_{\mathrm f}=10^{-8}$; $\sigma_{\mathrm s,\min}$ is the discrete minimum over the element and its face neighbours at the previous stage (§3.1, §4). **Stated**
14. The strength is solved for $f=e^{-\zeta_{\mathrm F}}\in[0,1]$ with the Illinois (modified regula falsi) method, tolerance $10^{-8}$, at most 20 iterations (§4.1). **Stated**
15. With the degree-$k$ components $u^{(k)}=\mathsf V\mathsf I^{(k)}\mathsf V^{-1}u$ precomputed, the filtered solution is $\tilde u=\sum_{k=0}^{N}f^{k^2}u^{(k)}$, free of matrix–vector products inside the iteration. Nodewise solves with element value $f=\min_jf_j$, each $f_j$ the upper bracket of the next node, need "effectively only one full evaluation" of the filter, and the filter then costs "typically less than" the flux divergence (§4.1, Eqs. (35)–(37)). **Stated** (the cost ratio is not quantified)
16. Near-vacuum magnetized vortex ($\mu=5.38948938512$): $L^1$ errors of $B$ converge at rates 2.89, 3.80, 4.62 and 5.23 for $N=2$ to $5$ on $20^2$ to $67^2$ elements, "on the order of $p$ to $p+1$" (§5.1, Table 1). **Shown** (the printed rates are the least-squares slopes over all six meshes, 2.895, 3.805, 4.622, 5.229 *(compiler check, not in the sources)*)
17. The $N=2$ errors are "marginally lower" than those of Wu & Shu's positivity-preserving third-order DG, even after removing the $1/A$ normalization (§5.1). **Shown** (against a table not reproduced)
18. The maximum limiting factor $1-f$ over the vortex run is "on the order of $10^{-4}$ to $10^{-7}$": the filter is "essentially negligible for smooth solutions" (§5.1, Table 2). **Shown** (but see Printed slips)
19. Brio–Wu ($N=3$, 200 and 400 elements): rarefactions and shock resolved within an element without noticeable oscillations; minor density oscillations between the compound wave and the contact and minor undershoots ahead of the contact (§5.2, Fig. 2). **Shown**
20. Orszag–Tang ($N=3$, $64^2$ to $256^2$): minor density oscillations at low resolution that vanish with refinement; $\lvert\nabla\cdot B\rvert$ concentrated at strong gradients and decreasing with resolution; filter activity concentrated at discontinuities; the pressure cut at $y=0.3125$, $t=0.48$ agrees with a Jiang–Wu WENO reference (§5.3, Figs. 3–6). **Shown**
21. Shock–cloud interaction ($N=2$, $400^2$): no observable spurious oscillations, symmetry kept; "roughly equally performative" as Wu–Shu DG with WENO limiter and "marginally better" on small scales behind the cloud; without the positivity-preserving filter the run diverged with negative pressure (§5.4, Figs. 7–9). **Shown**
22. Extreme magnetized blast ($p_e=10^4$, $p_a=0.1$, $B_0=1000/\sqrt{4\pi}$) on unstructured triangles, $N=4$, about $1.2\cdot10^5$ and $5\cdot10^5$ elements: discontinuities resolved across 1–2 solution nodes, discrete shock thickness decreasing in proportion to the mesh size, minor density oscillations (mesh imprinting) on the coarse mesh. Without the positivity-preserving modifications the scheme "would diverge almost instantly" (§5.5, Figs. 10–13). **Shown** (the last sentence **Stated**)
23. For the blast, HLL was "much better behaved" than HLLC, though both were stabilized by the filter; in the other cases Rusanov, HLL and HLLC differed negligibly (§4, §5.5). **Stated**
24. 3D magnetized Rayleigh–Taylor ($N=3$, $64\times64\times128$): well-behaved in the hydrodynamic, weakly ($0.1B_c$) and strongly ($0.5B_c$) magnetized regimes; the field imparts anisotropy and slows the growth (§5.6, Figs. 14–16). **Shown**
25. On 16 V100 GPUs to $t=1$ (weakly magnetized run), the new algorithm needs 25.3 GPU hours against 61.4 at $N=3$ (about 2.4 times faster) and 39.8 against 257 at $N=4$ on $51\times51\times102$ elements, about the same number of degrees of freedom (about 6.5 times); the speedup grows with order (§5.6, Fig. 17, §6). **Shown**
26. Linear stability gives a cutoff field $B_c=\sqrt{(\rho_h-\rho_l)gL}=\sqrt2$ above which the Rayleigh–Taylor instability is fully damped (§5.6, Eq. (52), citing Stone & Gardiner). **Stated**

# Printed slips

- Eq. (36): printed $\tilde{\mathbf u}=\sum_{i=0}^{p}f^{p_i^2}\mathbf u^{(k)}$, summing over $i$ a term indexed by $k$. With Eqs. (35) and (37) it reads $\sum_{k=0}^{p}f^{k^2}\mathbf u^{(k)}$.
- Eqs. (39)–(40) against §5.1 *(compiler check, not in the sources)*: with $\delta P=-\frac{\mu^2(1+r^2)}{8\pi^2}\phi(r)^2$ and $\phi(r)=\exp(1-r^2)$ as printed, $(1+r^2)e^{2(1-r^2)}$ is maximal at $r=0$ and $\mu^2/(8\pi^2)=0.367879\approx e^{-1}$, so $\min p=1-e^{-1}e^2=-1.718$, a negative pressure. The stated minimum "approximately $2\epsilon=2\cdot10^{-8}$" follows only with $\phi(r)$ unsquared in $\delta P$ (or $\phi=\exp((1-r^2)/2)$): $1-e^{-1}e=2.0\times10^{-8}$. One exponent is misprinted; the paper does not say which.
- §5.5: "a very small plasma-beta of $\beta\approx2.5\cdot10^{-4}$" for $P_a=0.1$, $B_0=1000/\sqrt{4\pi}$. With the paper's $\beta=2P/(\mathbf B\cdot\mathbf B)$ this is $2.5\times10^{-6}$; $2.5\times10^{-4}$ is the value for the original $B_0=100/\sqrt{4\pi}$ *(compiler check, not in the sources)*.
- §2.1 defines the "magnetic pressure" as $P_b=\frac12(\gamma-1)\mathbf B\cdot\mathbf B$, whereas the flux (Eq. (2)) and $\beta=2P/(\mathbf B\cdot\mathbf B)$ use $\frac12\mathbf B\cdot\mathbf B$. The colour bars of Figs. 10d and 11d (23000–28000) contain $\frac13B_0^2=2.65\times10^4$ and not $\frac12B_0^2=3.98\times10^4$, so the plots use the printed definition *(compiler check, not in the sources)*.
- §5.1 says the maximum $1-f$ is "on the order of $10^{-4}$ to $10^{-7}$", but Table 2 prints values down to $3.30\times10^{-8}$ ($N=2$, $25^2$) and $3.79\times10^{-8}$ ($N=4$, $25^2$).
- Eq. (17): the induction and energy rows of the Powell source are printed with $\boldsymbol u$ and $\boldsymbol u\cdot\boldsymbol B$, where the velocity $\mathbf v$ is meant ($\mathbf u$ is the conserved state).
- Eq. (15): the mean update is printed without the $1/V_k$ of the mean defined in Eq. (16).
- Eq. (43) prints the Orszag–Tang field as $B=\big(\sin(2\pi y),-\sin(4\pi x)\big)/\sqrt{4\pi}$. This is the negative of the field Dao & Nazarov (2022) and Lesur et al. (2023) print, $\big(-\sin(2\pi y),\sin(4\pi x)\big)/\sqrt{4\pi}$ with the same velocity, and differs from Rueda-Ramírez et al.'s in the sign of $B_1$ only ([Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)). Ideal MHD is invariant under $B\mapsto-B$, so the flow is that of the former *(compiler check, not in the sources)*; whether the sign is a slip cannot be decided from the paper.
- Typos: "descending figures" for "fingers" and "as it not stiff" (§5.6). In the reference list, [4] "Caletch plasma jet" and [5] "$u_t+uu_x=\mu_{xx}$".

# Notation map

| Dzanic & Witherden 2023 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf u=[\rho,\rho\mathbf v,\mathbf B,E]$ | $u$ | conserved MHD state; **collision**: Eq. (17) also prints $\mathbf u$ for the velocity |
| $\mathbf q=[\rho,\mathbf v,\mathbf B,P]$; $u,v,w$ | primitive state; $v_1,v_2,v_3$ | velocity components translated |
| $\mathbf F$ | $f^{(d)}$ | physical flux |
| $P$ | $p$ | thermal pressure |
| $p$, $\mathbb P_p$ | $N$, $\mathbb P^N$ | polynomial degree; **collision** with pressure, resolved by the source's capital $P$ |
| $p_i$ | $n_j$ (local) | total degree of mode $i$, as on the entropy-filtering page |
| $\sigma=P\rho^{-\gamma}$, $\sigma_{\min}$ | $\sigma_{\mathrm s}=e^{s}$, $\sigma_{\mathrm s,\min}$ (local) | specific entropy functional; **differs** from the 2022 paper's $\rho\ln(P\rho^{-\gamma})=\rho s$; monotone in $s$, so the minimum principle is the same; **collision** with $\sigma$ (affine scaling) of §10 |
| $\sigma$, $\boldsymbol\Sigma$ (Eq. (4)) | $-\eta$, $-F_\eta$ | entropy pair in the physical (increasing) sign |
| $\Gamma_1,\Gamma_2,\Gamma_3$ | $g_i$ | constraint functions; $\Gamma_3=\sigma-\sigma_{\min}$ |
| $\epsilon=10^{-8}$ | $\epsilon_{\mathrm f}$ (local) | constraint tolerance; not the WENO $\epsilon$ |
| $G$, $G_P$ | $G$, $G_P$ | admissible set with and without the entropy constraint |
| $H$, $\hat H_i$; $H_e$, $H_p$ | filter and modal kernel; entropy and positivity filters | |
| $\zeta$ | $\zeta_{\mathrm F}$ (local) | filter strength; **collision** with $\zeta$ of §10, renamed as on the entropy-filtering page |
| $f=e^{-\zeta}$, $1-f$ | $f$ (local), limiting factor | **collision** with the flux $f$; used only in the strength solve |
| $\mathbf V$, $\boldsymbol\Lambda$, $\mathbf I^{(k)}$ | $\mathsf V$, $\boldsymbol\Lambda$, $\mathsf I^{(k)}$ (local) | Vandermonde, diagonal filter, degree selector |
| $\mathbf u^{(k)}$ | $u^{(k)}$ (local) | degree-$k$ component; **collision** with the RK stages $\mathbf u^{(1)}$, $\mathbf u^{(2)}$ of Eq. (34) and with the candidate value $u^{(k)}$ of §4 |
| $\phi_i$, $\bar\phi_i$, $\mathbf h_i$ | $\ell_j$; interface basis; FR correction functions in $\mathrm{RT}_p$ | **collision**: $\phi$ is also the vortex profile (Eq. (40)) and the registry volume fraction $\phi_k$ |
| $\mathbf u^-$, $\mathbf u^+$; $\bar{\mathbf F}$ | $u^-$ (own element), $u^+$ (neighbour); $h(u^-,u^+)$ | interior and exterior traces; common flux |
| $L_1$, $L_2$ | $\mathcal L_1$, $\mathcal L_2$ (local) | flux divergence and Powell source; registry $L$ is the left-eigenvector matrix |
| $\mathbf S_{\mathbf B}$, $\mathbf S_{\mathbf G}$ | $S(u)$ | Powell source; gravity source (Rayleigh–Taylor only) |
| $\beta=2P/(\mathbf B\cdot\mathbf B)$ | $\beta_{\mathrm p}$ | plasma beta |
| $P_b=\tfrac12(\gamma-1)\mathbf B\cdot\mathbf B$ | — | the paper's "magnetic pressure"; see Printed slips |
| $\mu$, $\delta u$, $\delta B$, $\delta P$ | vortex parameters (local) | not the affine translation $\mu$ of §10 |
| $B_c$, $\rho_h$, $\rho_l$, $g$, $L$ | Rayleigh–Taylor cutoff field, heavy and light densities, gravity, length (local) | $L$ is not the eigenvector matrix |

# Reference list

The paper prints 50 references, numbered [1]–[50] in order of citation, all
with DOIs. The list is merged complete into the [bibliography](/bibliography.md)
with `citedby` including `dzanic-2023`. Same-author same-year works take
suffixes in printed order (Zhang 2011 [16], [33], [34]; Li 2005 [19], [39]).
Ref. [23] (Dao & Nazarov, Comput. Methods Appl. Mech. Engrg. 398:115269, 2022)
is a different work from the ingested `dao-2022` (J. Sci. Comput. 92:77) and
is keyed apart from it. Refs. [13], [14] and [17] are the ingested
`dzanic-2022`, `ruedaramirez-2022` and `dzanic-2022-b`. The titles of [4] and
[5] are kept as printed; [16] prints J. Comput. Phys. vol. 229 with year 2011,
while [32] prints the same volume with 2010. No item is unparseable.

# Pages created or updated

Chunk 5 (2026-10-23), cited further in chunk 6 (2026-10-23). This source is cited on:

* [Bound preservation](/properties/bound-preservation.md)
* [Brio–Wu MHD shock tube](/benchmarks/brio-wu-shock-tube.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Entropy filtering for DG and FR](/methods/entropy-filtering.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Flux reconstruction and energy-stable FR](/methods/flux-reconstruction.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [MHD blast wave and rotor](/benchmarks/mhd-blast-wave.md)
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)
* [PyFR](/software/pyfr.md)
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)

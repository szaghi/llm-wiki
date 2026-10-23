---
type: Source
title: "Huang et al. (2026) — A unified framework for non-linear reconstruction schemes in a compact stencil. Part 2: Learning operators from neural networks"
description: "Projects the trained WENO3-NN network onto the normalised-variable diagram, finds that it tends to the central scheme inside cells holding a critical point, and fits two closed-form compact operators, ROUND and the anti-dissipative LD-ROUND, that are cheaper and more accurate than the network."
resource: "doi:10.1016/j.jcp.2026.114764"
source_kind: paper
authors: [Huang M., Deng X., Matar O.K., Ying W.]
year: 2026
venue: "J. Comput. Phys. 555:114764"
local_file: "/home/stefano/papers/mosaic/weno-teno/2026_Crossref_Journal_of_Computational_Physics_Huang_A_unified_framework_for_non-linear_reconstruction_schemes_in.pdf"
tags: [round-scheme, machine-learning, normalised-variable-diagram, compact-stencil, numerical-dissipation]
timestamp: 2026-10-21T12:00:00Z
---

# Summary

Part 2 of the compact-stencil framework of [Deng (2023)](/sources/deng-2023.md) (its ref. [24]), which it
does not redefine. A three-cell finite-volume reconstruction
$u^-_{i+1/2}[\bar u_{i-1},\bar u_i,\bar u_{i+1}]$ is replaced by
a scalar normalised operator $\tilde u_{i+1/2}=\mathcal R(\tilde u_i)$
on the [normalised-variable diagram](/definitions/normalised-variable-diagram.md),
which makes the scheme [scale-invariant](/properties/scale-invariance.md) and
lets accuracy, CBC/[TVD](/definitions/total-variation-diminishing.md), ENO and
[dissipation](/definitions/numerical-dissipation.md) properties be read off a
curve.

The authors retrain the data-driven WENO3-NN of Bezgin, Schmidt & Adams
([learned WENO weights](/methods/learned-weno-weights.md)): a 658-parameter
network with a Delta input layer, three 16-node hidden layers, softmax output
and an ENO cut-off layer, trained on a loss that balances face-reconstruction
error against distance from the linear weights. Sampled with
$\bar u_{i-1}=0$, $\bar u_{i+1}=1$, WENO3-NN behaves like classical
[WENO-JS](/methods/weno-js-reconstruction.md) and [WENO-Z](/methods/weno-z.md)
third-order weights for $0\le\tilde u_i\le1$, built on two-point
[smoothness indicators](/definitions/smoothness-indicator.md); for
$\tilde u_i<0$, a critical point inside cell $i$, it moves from the
second-order upwind toward the second-order central operator. Two closed-form
[ROUND](/methods/round-scheme.md) operators follow: a piecewise-linear ROUND
that reproduces this with a larger central share, and LD-ROUND, which adds
controlled anti-dissipation above the P3 line, the behaviour seen in
[THINC](/methods/thinc-reconstruction.md).

The schemes cost 11 and 20 FLOPs against 2139 for WENO3-NN, have lower
high-wavenumber dispersion and dissipation than WENO5-JS in the
[approximate dispersion relation](/definitions/approximate-dispersion-relation.md),
and give smaller errors than WENO3-NN at a quarter of its CPU time in a
sine-advection test. Euler tests with an HLLC flux, HLL for the double Mach
reflection to avoid the [carbuncle](/definitions/carbuncle-phenomenon.md)
([HLL family](/methods/hll-riemann-solvers.md)), cover the
[Lax tube](/benchmarks/sod-and-lax-shock-tubes.md), [Shu–Osher](/benchmarks/shu-osher-problem.md),
[blast waves](/benchmarks/woodward-colella-blast-wave.md), a
[2D Riemann problem](/benchmarks/two-dimensional-riemann-problems.md), the
[double Mach reflection](/benchmarks/double-mach-reflection.md),
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) and
Richtmyer–Meshkov instabilities, [shock–vortex interaction](/benchmarks/shock-vortex-interaction.md),
a supersonic planar [jet](/benchmarks/high-mach-astrophysical-jet.md) and a
Mach 6 air–helium [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md).
They show ROUND comparable to WENO3-NN and LD-ROUND resolving finer
structures, in several cases more than WENO5-JS. The multi-resolution WENO
literature ([WENO-AO and multi-resolution WENO](/methods/weno-ao.md)) is
cited among the learned compact schemes. Evidence is numerical; there are no
theorems.

# Version read

Version of record (Elsevier typeset, open access CC BY 4.0), 23 pages, all
read; pp. 4–9 also read visually to check every equation of §§2–4. Page 1
matches Crossref (title, four authors, venue, DOI printed). Received 7 July
2025, accepted 6 February 2026. Equation, table and figure numbers cited here
are those of this version.

# Key claims

Registry notation (see the notation map): the source's $\phi$, $h$,
$\hat\phi_i$, $\hat\phi_{i+1/2}$, $\hat{\mathcal R}_i$ are $u$, $\Delta x$,
$\tilde u_i$, $\tilde u_{i+1/2}$, $\mathcal R$ (the normalised operator, page-local
as on the [normalised-variable diagram](/definitions/normalised-variable-diagram.md)
and [ROUND](/methods/round-scheme.md) pages).

1. Sampled on the normalised-variable diagram, WENO3-NN recovers the third-order linear scheme P3 near $\tilde u_i=0.5$, the second-order central CD2 near $\tilde u_i=1$ and the second-order upwind UW2 near $\tilde u_i=0$, like traditional third-order WENO (§3.4, Fig. 2a). **Shown**
2. For $0<\tilde u_i<1$ WENO3-NN lies predominantly below $\tilde u_{i+1/2}=k\tilde u_i$, $k=2.5$, so CFL $\le0.4$ is needed for it to satisfy the convection boundedness criterion strictly across discontinuities (§3.4). **Shown** (diagram) / **Stated** (the CBC–CFL link, cited)
3. As $\tilde u_i$ decreases below 0, WENO3-NN departs from UW2 and tends toward CD2 (§3.4, Fig. 2b). **Shown**
4. Explanation: $\tilde u_i<0$ means cell $i$ holds a critical point; there the reconstruction loss dominates the linear-weight loss of Eq. (3.12) and drives the network toward CD2, which is credited for WENO3-NN's better dissipation (§3.4). **Derived** (qualitative argument)
5. For smooth monotone data $\tilde u_i=\tfrac12-\frac{u''(x_c)\Delta x}{4u'(x_c)}+O(\Delta x^2)\to\tfrac12$, so the linear-weight loss dominates there (Eq. 3.14). **Derived**
6. The new piecewise-linear ROUND (Eq. 4.1) recovers P3 near 0.5, UW2 near 0, stays below $\tfrac52\tilde u_i$ on $(0,1)$ (CBC for CFL $\le0.4$), and tends to CD2 as $\tilde u_i$ decreases below 0 with a larger central share than WENO3-NN; the text says it also tends to CD2 near 1 (see Printed slips) (§4.1, Fig. 3). **Shown** (by construction)
7. The larger central share for $\tilde u_i<0$ is "motivated by numerical experiments, indicating that incorporating more central schemes in less smooth regions can further enhance accuracy and improve dissipation properties" (§4.1). **Stated** (experiments not shown)
8. LD-ROUND (Eq. 4.2) introduces controlled anti-dissipation: part of its curve lies above the P3 line for $0<\tilde u_i<1$, the anti-dissipation region of [Deng (2023)](/sources/deng-2023.md), while keeping the $\tilde u_i<0$ branch of ROUND (§4.2, Fig. 4). **Shown** (by construction)
9. Its shape parameters are 180 and 600 (source $\theta_1$, $\theta_2$); larger values mean more anti-dissipation and "may introduce excessive anti-dissipation errors and potentially lead to numerical instability" (§4.2). **Stated**
10. FLOPs (Table 2; JAX counts following Bezgin et al.): WENO3-JS 19, WENO5-JS 55, WENO3-NN 2139, Rational-WENO3-NN 508, ROUND 11, LD-ROUND 20 (§5.1). **Shown** (count)
11. ROUND needs "approximately half the FLOPs of WENO3-JS and only 5% of the cost of WENO3-NN"; LD-ROUND is twice ROUND, comparable to WENO3-JS, nearly half WENO5-JS and "less than 10%" of WENO3-NN (§5.1; see Printed slips). **Stated**
12. In the approximate-dispersion-relation analysis all schemes disperse alike at low wavenumbers; both ROUND schemes have lower high-wavenumber dispersion error than WENO5-JS and WENO3-NN, ROUND has markedly lower high-wavenumber dissipation, LD-ROUND has dissipation similar to WENO5-JS at low wavenumbers and lower at high ones, and both approach vanishing dissipation near the cut-off wavenumber, as WENO3-NN does (§5.2, Fig. 5). **Shown**
13. Sine advection to $t=20$ with $N_x=320/640/1280$ (Table 3): $L_1$ errors WENO3-NN $2.38\times10^{-4}$, $4.40\times10^{-5}$, $8.37\times10^{-6}$ (orders 2.44, 2.39); ROUND $1.72\times10^{-4}$, $3.25\times10^{-5}$, $6.05\times10^{-6}$ (2.40, 2.43); LD-ROUND $1.15\times10^{-4}$, $1.92\times10^{-5}$, $3.21\times10^{-6}$ (2.58, 2.58); $L_\infty$ orders WENO3-NN 1.64, 1.60, ROUND 1.63, 1.63, LD-ROUND 1.74, 1.72 (§6.1). **Shown**
14. CPU times (s, Table 3, hardware not stated): WENO3-NN 2.6/9.6/37.0, ROUND 0.6/2.2/8.5, LD-ROUND 0.7/2.8/11.3; ROUND costs about 25% of WENO3-NN, and on the same grid LD-ROUND's errors and CPU time are both less than half of WENO3-NN's (§6.1, abstract). **Shown**
15. In error against CPU time both ROUND schemes are substantially more efficient than WENO3-NN; ROUND is cheapest but less accurate than LD-ROUND (§6.1, Fig. 6). **Shown**
16. None of the three compact schemes shows third order in this test: Table 3 gives $L_1$ orders 2.4–2.6 and $L_\infty$ orders 1.6–1.7, and the paper does not comment (§6.1). **Shown**
17. Jiang–Shu complex-wave advection (200 cells, $t=2$): ROUND is comparable or superior to WENO3-NN on extrema (Gaussian, triangle, semi-ellipse); LD-ROUND is markedly better on extrema and slightly better on the square wave (§6.2, Fig. 7). **Shown**
18. Shu–Osher problem (400 cells): WENO3-NN is "significantly smeared out", the proposed schemes capture the small-scale waves, LD-ROUND best (§6.4, Fig. 9). **Shown**
19. 2D Riemann configuration 3 ($600\times600$): ROUND gives slightly fewer vortical structures than WENO3-NN, LD-ROUND finer structures than WENO5-JS, and both keep symmetry (§6.6, Fig. 11). **Shown**
20. Double Mach reflection ($\Delta x=1/400$, HLL to avoid the carbuncle): WENO3-NN, WENO5-JS and ROUND are comparable; LD-ROUND resolves more vortical structure along the slip line (§6.7, Fig. 12). **Shown**
21. Rayleigh–Taylor instability ($128\times512$): ROUND is finer than WENO5-JS but slightly less detailed than WENO5-Z; LD-ROUND is richer than both; both reproduce the "upturned tail of the light fluid", said to be typical of high-order schemes (§6.8, Fig. 13). **Shown**
22. Richtmyer–Meshkov instability ($\Delta x=1/200$, $t=2$): ROUND is comparable to WENO3-NN, LD-ROUND finer than WENO5-JS (§6.9, Fig. 14). **Shown**
23. Shock–vortex interaction: ROUND is more accurate at the shock front than WENO3-NN and WENO5-JS; LD-ROUND is most accurate near $x\approx0.55$ and captures the lowest pressure near $x\approx0.95$ (§6.10, Fig. 15). **Shown**
24. Supersonic planar jet: ROUND is comparable to WENO5-JS; LD-ROUND gives more intricate vortical structures, outperforming the earlier ROUND_A/ROUND_A+ and an LES with TCD-WENO on a finer grid (§6.11, Fig. 16). **Shown** (qualitative)
25. Mach 6 air–helium shock–bubble interaction (level set, multi-resolution, finest $1024\times256$): the proposed schemes are comparable to WENO5-JS, ROUND slightly more dissipative at $t=0.018$ and $0.024$, LD-ROUND with more complex vortical structures than WENO5-JS (§6.12, Fig. 17). **Shown**
26. The methodology (learn the diagram shape from a network, then fit a closed-form ROUND) applies to Rational-WENO3-NN and WCNS3-MR-NN, and ROUND extends to unstructured grids through the virtual upwind point method (§7). **Stated**

# Printed slips

- Eq. (2.5) prints the upwinding term as $-\lvert a_{i+1/2}\rvert(u^-_{i+1/2}-u^+_{i+1/2})$; the dissipative form, as in the registry's Lax–Friedrichs flux, is $-\lvert a_{i+1/2}\rvert(u^+_{i+1/2}-u^-_{i+1/2})$.
- §2.2, Eq. (2.9): first-order upwind is printed $\mathcal R^{UW}_i=\bar u_{i-1}$ with normalised form $\tilde u_i$; $\bar u_{i-1}$ normalises to $0$, and $\tilde u_i$ is the normal form of $\bar u_i$. *(compiler check, not in the sources: substitution in the definition of $\tilde u_{i+1/2}$.)*
- Eq. (3.3) names the indicators $IS_0$ and $\beta_1$, Eq. (3.4) $IS_0$, $IS_1$; Eq. (3.6) has $IS_k$ inside $\zeta_j$; Eq. (3.10) has $\Delta_i$ on the left and $j$ on the right; Eq. (4.3) says "$k=0,1$" for weights used as $\omega_{i,1},\omega_{i,2}$ with $\theta_1,\theta_2$.
- §5.1: ROUND costs "only 5% of the cost of WENO3-NN"; Table 2 gives $11/2139\approx0.5\%$ (LD-ROUND $20/2139\approx0.9\%$, consistent with "less than 10%"). *(compiler check, not in the sources: division of the Table 2 counts.)*
- §4.1 says ROUND "tends toward the second-order central scheme as $\hat\phi_i$ approaches 1.0", but Eq. (4.1) uses $\tfrac3{50}\tilde u_i+\tfrac{47}{50}$ on $[91/116,1]$, slope 0.06 against the CD2 slope 1/2: it meets CD2 only at $\tilde u_i=1$. *(compiler check, not in the sources: the P3 line meets $\tfrac3{50}x+\tfrac{47}{50}$ at $x=91/116\approx0.784$.)*
- §6.3 runs the Lax problem "at $t=0.15$", the caption of Fig. 8 says $t=0.16$.
- §6.2, Eq. (6.4): $z=0.7$ with the Gaussian group on $\lvert x+0.7\rvert\le0.1$; $\beta$ is printed "log2 36δ²" for $\log2/(36\delta^2)$.
- §6.8 (Rayleigh–Taylor): the printed initial state ($\rho=2$, $p=2y+1$ for $y\ge0.5$; $\rho=1$, $p=y+1.5$ below) gives $p=1.5$ at the bottom and $p=3$ at the top, while the prescribed boundary states are bottom $(1,0,0,2.5)$ and top $(2,0,0,1)$; the gravity source term is not given. *(compiler check, not in the sources: evaluation of the printed pressures at $y=0$ and $y=1$.)*
- Fig. 15 caption lists "WENO5-JS (green triangle), WENO5-JS (brown square)"; §6.10 compares with WENO3-NN and WENO5-JS.
- Fig. 12 caption "double Mach 10 refection"; "recommanded" (§3.2); ref. [53] prints the authors as "D. Kinga, J.B. Adam, et al." for the paper "A method for stochastic optimization".

# Notation map

| Huang et al. (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\phi$, $f(\phi)$ | $u$, $f(u)$ | scalar 1D law |
| $\bar\phi_i$, $h$ | $\bar u_i$, $\Delta x$ | finite-volume cell average, uniform width |
| $\phi^L_{i+1/2}$, $\phi^R_{i+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | face states |
| $\tilde f_{i+1/2}$, $\tilde\alpha_{i+1/2}$ | $\hat f_{i+1/2}$, $a_{i+1/2}$ | numerical flux and its signal speed; **$\alpha$ is reused below** |
| $\mathcal R_i$, $\hat{\mathcal R}_i$ | $u^-_{i+1/2}[\cdot]$, $\mathcal R$ | conventional and normalised reconstruction operators, as on the NVD page; **plain $R$ is the eigenvector matrix in the registry** |
| $\hat\phi_i$, $\hat\phi_{i+1/2}$ | $\tilde u_i$, $\tilde u_{i+1/2}$ | normalised variable and face value; agrees with the registry definition |
| UW, DW, UW2, CD2, P3 | kept | first-order upwind and downwind, second-order upwind and central, third-order linear |
| $d_0$, $d_1$ | $d_0$, $d_1$ | $1/3$ on UW2, $2/3$ on CD2; agrees |
| $IS_0$, $IS_1$ ($\beta_1$) | $\beta_0$, $\beta_1$ | Jiang–Shu indicators |
| $\zeta_k$, $\omega_k$ | $\alpha_k$, $\omega_k$ | unnormalized and normalized weights |
| $\epsilon$ | $\epsilon$ | regularization; **also the vortex strength of §6.10** |
| $\tau_Z$ | $\tau$ | third-order WENO-Z indicator $\lvert\beta_0-\beta_1\rvert$ |
| $\omega^{NN}_k$, $\tilde\omega^{NN}_k$, $\Theta$ | kept | network weights before and after the ENO layer, network parameters |
| $c_{eno}$, $\psi_j$ | kept | ENO-layer threshold $2\times10^{-4}$ and flag; analogous to $C_T$, $\delta_k$ but on weights; **$\psi$ is the TVD limiter in the registry** |
| $\mathcal L_r$, $\mathcal L_d$, $\beta_d$, $\beta_W$ | $\mathcal L_r$, $\mathcal L_d$, $b_d$, $b_W$ (page-local on [learned WENO weights](/methods/learned-weno-weights.md)) | reconstruction and linear-weight losses and their weights; **$\mathcal L$ is the semi-discrete operator and $\beta$ the smoothness indicator in the registry** |
| $\gamma^s_i$, $\alpha$, $\epsilon_\gamma$ | $\varsigma$, $p_s$, $10^{-15}$ (page-local on learned WENO weights) | well-resolvedness indicator, its exponent ($0.1$), $10^{-15}$; **$\gamma$ and $\alpha$ collide with the ratio of specific heats and the weights** |
| $\omega_{i,k}$, $\theta_k$ | $\varphi_k$, numbers | LD-ROUND blending weights, written $\varphi_k$ with their shape parameters as numbers on the ROUND page; **$\theta$ is the Zhang–Shu scaling factor in the registry** |
| $k$ | kept | slope of the CBC line $\tilde u_{i+1/2}=k\tilde u_i$, $k=2.5$ for CFL $0.4$; **collides with the stencil index** |
| $\gamma$ | $\gamma$ | ratio of specific heats in the Euler tests; agrees |

# Reference list

73 printed references in numbered style ([1]–[73]), all parsed and merged
complete into the [bibliography](/bibliography.md) with `citedby`
`huang-2026`. Refs. [25] and [33] are arXiv preprints, kept as their own
entries. Ref. [53] is garbled as printed and kept as printed; ref. [49] prints
author names in an unusual order, kept as printed; ref. [60] (Quirk 1997)
prints only "Springer, 1997". Refs. [15], [37], [54] and [62] lack a volume or
a page number. DOIs are printed only for [10] and [43]. No printed duplicates.

# Pages created or updated

Chunk 1 (2026-10-21), cited further in chunks 2–7 (2026-10-22/23). This source is cited on:

* [Accuracy at critical points](/properties/critical-point-accuracy.md)
* [Approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
* [Boundary variation diminishing (BVD)](/definitions/boundary-variation-diminishing.md)
* [Carbuncle phenomenon](/definitions/carbuncle-phenomenon.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [ENO property](/definitions/eno-property.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Learned WENO weights](/methods/learned-weno-weights.md)
* [Normalised-variable diagram](/definitions/normalised-variable-diagram.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)
* [Richtmyer–Meshkov instability](/benchmarks/richtmyer-meshkov-instability.md)
* [ROUND schemes](/methods/round-scheme.md)
* [Scale and affine invariance](/properties/scale-invariance.md)
* [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
* [Shock–vortex interaction](/benchmarks/shock-vortex-interaction.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Symmetry preservation](/properties/symmetry-preservation.md)
* [THINC reconstruction](/methods/thinc-reconstruction.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
* [Weighted compact nonlinear schemes (WCNS)](/methods/weighted-compact-nonlinear-scheme.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
* [WENO-Z weights](/methods/weno-z.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)

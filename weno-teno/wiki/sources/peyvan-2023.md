---
type: Source
title: "Peyvan et al. (2023) — High-order methods for hypersonic flows with strong shocks and real chemistry"
description: "Compares filtered spectral difference and flux reconstruction, entropy-stable DGSEM with subcell blending, modal DG and FD WENO on one-dimensional strong-shock and reacting problems, then derives entropy-conservative two-point fluxes, with a new logarithmic–exponential mean, for five-species air with vibrational energy."
resource: "doi:10.1016/j.jcp.2023.112310"
source_kind: paper
authors: [Peyvan A., Shukla K., Chan J., Karniadakis G.E.]
year: 2023
venue: "J. Comput. Phys. 490:112310"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Journal_of_Computational_Physics_Peyvan_High-order_methods_for_hypersonic_flows_with_strong_shocks_a.pdf"
tags: [dg, entropy-stable, multicomponent, hypersonic, numerical-flux, shock-capturing]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper has two parts. The first compares high-order methods on
one-dimensional strong-shock and reacting problems relevant to hypersonics:
spectral difference (SD) and [flux reconstruction](/methods/flux-reconstruction.md)
(FR), both stabilized by the positivity-preserving
[entropy-based adaptive modal filter](/methods/entropy-filtering.md) of
Dzanic & Witherden; the entropy-stable [DGSEM](/methods/dgsem.md) (ES-DGSEM)
with the [subcell finite-volume blending](/methods/subcell-finite-volume-limiting.md)
of Hennemann et al.; the positivity-preserving modal DG of Zhang & Shu; and
the positivity-preserving fifth-order finite-difference WENO of Zhang & Shu.
The tests are the [Leblanc shock tube](/benchmarks/leblanc-shock-tube.md), a
Mach-10 variant of the [Shu–Osher problem](/benchmarks/shu-osher-problem.md)
and a three-species reacting [Sod problem](/benchmarks/sod-and-lax-shock-tubes.md).
The authors conclude that ES-DGSEM is the most robust, oscillates least and
needs the fewest tuning parameters, but smears discontinuities more than FR
and SD. FR and SD overshoot more, SD the most. Modal DG fails on the
reacting Sod problem, and WENO is comparable to ES-DGSEM.

The second part extends ES-DGSEM to five-species air ($N$, $O$, $NO$, $N_2$,
$O_2$) with a rigid-rotor harmonic-oscillator internal energy, i.e. the
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
with one vibrational mode per diatomic species. New
[entropy-conservative two-point fluxes](/methods/entropy-conservative-flux.md)
are derived from Tadmor's condition with the Gouasmi et al. multicomponent
entropy. The vibrational term needs a new mean built from the
[logarithmic mean](/operators/logarithmic-mean.md) and an "exponential mean",
evaluated stably near equal states by a series in $\sinh x/x$. The fluxes
give [entropy stability](/properties/entropy-stability.md) together with the
blending. Mutation++ supplies thermodynamics, transport and Park's
five-reaction chemistry; viscous terms use BR1.

On a smooth periodic [density-wave](/benchmarks/density-wave-advection.md)-type
temperature perturbation, the global entropy rate stays of order $10^{-5}$,
which the authors attribute to the $\sim10^{-7}$ Newton tolerance of the
temperature inversion. The scheme matches the Grossman–Cinnella
non-equilibrium Sod reference. Equilibrium and finite-rate chemistry agree
at a driver temperature of 2000 K and diverge from 3000 K on. The steady
viscous flow behind a Mach-10 shock agrees with Marxen et al. except for small
$N$ and $NO$ differences. All tests are one-dimensional, with the
Carpenter–Kennedy low-storage RK45.

# Version read

The arXiv preprint arXiv:2211.12635v1 [physics.flu-dyn] of 22 Nov 2022
(page dated "November 24, 2022"), not the version of record; 25 pages, main
text pp. 1–22, references pp. 23–25. Section, equation and figure numbers
are those of the arXiv v1. Title and authors match the Crossref card; page 1
prints the last author as "George Em Karniadakis", whence the initials G.E.,
while Crossref gives "Karniadakis G.".

# Key claims

Notation of the Notation map: $N=3$ is the DGSEM degree throughout, $\rho_k$
the partial densities, $r_k$ the species gas constants, $e^0_k$ the
formation energies, $T^{\mathrm v}_k$ the vibrational temperatures,
$\mathsf a_k\in\{3/2,5/2\}$ and $\mathsf b_k\in\{0,1\}$ the
translational–rotational coefficient and the vibration switch.

1. ES-DGSEM with high/low-order flux blending is the most stable of the methods compared, gives negligible oscillations and needs "the least computational effort" for reactive flows with strong shocks (abstract; §4.1–4.3; §5). **Shown** on 1D tests; no timings are printed for the cost claim.
2. New two-point entropy-conservative fluxes for the five-species rigid-rotor harmonic-oscillator Euler equations, Eqs. (89)–(91), satisfy Tadmor's condition $[\![w]\!]\cdot f^{\mathrm{ec}}=[\![\psi]\!]$ (§3):
   $$\begin{aligned}
   f^{\mathrm{ec}}_{\rho_k}&=\{\!\{v\}\!\}\{\!\{\rho_k\}\!\}_{\log},\\
   f^{\mathrm{ec}}_{\rho v}&=\frac{1}{\{\!\{1/T\}\!\}}\sum_kr_k\{\!\{\rho_k\}\!\}+\{\!\{v\}\!\}\sum_kf^{\mathrm{ec}}_{\rho_k},\\
   f^{\mathrm{ec}}_{E}&=\sum_k\Big(e^0_k-\mathsf b_kr_kT^{\mathrm v}_k+\frac{\mathsf a_kr_k}{\{\!\{1/T\}\!\}_{\log}}+\frac{\mathsf b_kr_k}{\{\!\{1/T\}\!\}_{\ln\exp,k}}-\tfrac12\{\!\{v^2\}\!\}\Big)f^{\mathrm{ec}}_{\rho_k}+\{\!\{v\}\!\}f^{\mathrm{ec}}_{\rho v}.
   \end{aligned}$$
   **Derived**
3. Entropy-conservative fluxes had not been derived before for hypersonic flows whose internal energy has translational, rotational and vibrational parts; Gouasmi et al. covered only constant or polynomial-in-$T$ specific heats (§1). **Stated**
4. The jump of the vibrational term is written with a new mean: $[\![\ln(e^{T^{\mathrm v}_ka}-1)]\!]=[\![a]\!]/\{\!\{a\}\!\}_{\ln\exp,k}$, with $\{\!\{a\}\!\}_{\ln\exp,k}=\{\!\{e^{T^{\mathrm v}_ka}-1\}\!\}_{\log}\,\{\!\{a\}\!\}_{\exp,k}$ and $\{\!\{a\}\!\}_{\exp,k}=[\![a]\!]/[\![e^{T^{\mathrm v}_ka}]\!]$ (Eqs. (78)–(82)). **Derived**
5. For $a^+\to a^-$ the exponential mean is evaluated stably by a truncated series in $x=T^{\mathrm v}_k\{\!\{a\}\!\}\mathsf j_a$, $\mathsf j_a=(a^+-a^-)/(a^++a^-)$ (Eqs. (84)–(87)), after the device of Winters et al. for the logarithmic mean. No switching threshold is printed. **Derived**
6. The new fluxes are said to be kinetic-energy preserving as well, citing Ranocha (end of §3). **Stated** (not shown)
7. With entropy-conservative interface fluxes and no stabilization, limiter or sources, the global entropy rate stays of order $10^{-5}$ up to $t=0.1$ (170 elements), not at machine zero. The authors attribute this to the $\sim10^{-7}$ tolerance of the Newton–Raphson energy-to-temperature inversion in Mutation++ (§4.4, Fig. 4). **Shown** (the attribution is **Stated**)
8. The authors say they checked numerically that the two-point fluxes satisfy the Tadmor relation (§4.4). **Stated** (no figure or number)
9. Leblanc problem (1000 elements, $\Delta t=2.0893\times10^{-8}$, $\alpha_{\max}=0.5$, Chandrashekar flux): ES-DGSEM smears the contact more than FR and SD but oscillates least. SD has the largest oscillations and undershoots, which the authors attribute to its degree-$(N+1)$ flux polynomial (§4.1, Fig. 1). **Shown**
10. "According to our experience, employing artificial viscosity cannot stabilize the high-order spectral method for high-pressure ratios shock waves" (§4.1). **Stated**
11. Mach-10 Shu–Osher variant (170 elements, $\Delta t=9.9964\times10^{-5}$, reference on 3000 elements): SD and FR miss the dip at $x=2.82$ and FR the valley at $x=3.265$, while ES-DGSEM resolves all features (§4.2, Fig. 2). **Shown**
12. The modal filter has a problem-dependent entropy threshold ($10^{-4}$) that must be tuned to avoid over-filtering smooth high-gradient regions. The ES-DGSEM blending is "not problem dependent", its parameter "usually kept at 0.5" (§4.2). **Stated** (with the evidence of Fig. 2)
13. Three-species Sod problem (800 elements; modal DG with $N=2$ on 1066 elements for equal degrees of freedom; reference ES-DGSEM on 4000 elements): every scheme except modal DG gets the right solution. Modal DG gives non-physical species densities, pressure and velocity. FR and SD agree better with the reference but oscillate; WENO and ES-DGSEM do not oscillate but smear more; SD undershoots strongly in $O_2$ (§4.3, Fig. 3). **Shown**
14. Zhang & Shu's positivity-preserving DG with sources fails on the three-species high-pressure-ratio Sod problem, while their positivity-preserving FD WENO succeeds (§1); §4.3 reproduces this. **Stated** and **Shown**
15. FR and SD extended to the five-species non-equilibrium Sod problem are unstable: the filter cannot find a strength that keeps the five species densities and the pressure positive and satisfies the entropy criterion at once (§4.5.1). **Stated** (no figure)
16. Hypersonic ES-DGSEM (200 elements, CFL 0.01 because of the stiff sources) matches the Grossman–Cinnella non-equilibrium Sod reference in pressure, density, velocity and all five mass fractions (§4.5.1, Fig. 6). **Shown**
17. Equilibrium and finite-rate chemistry agree at a driver temperature of 2000 K, start to deviate at 3000 K, where equilibrium overestimates the post-shock velocity, and deviate more at 4000 K; finite-rate chemistry is needed at high temperature (§4.5.2, Fig. 7). **Shown**
18. Viscous ES-DGSEM with BR1 and Mutation++ transport (45 elements) agrees with the steady post-shock profile of Marxen et al. except for a small discrepancy in $Y_N$ and $Y_{NO}$ (§4.6, Fig. 8). **Shown**
19. The authors attribute that discrepancy to weak inflow conditions through the Riemann solver against Dirichlet ones in the reference code, and to the reference not conserving mass: "The summation of all the five species mass fractions from Marxen's results adds up to 1.0035 at x = 0.01". They conclude that their results "are likely more accurate" (§4.6). **Stated**
20. The high-order accuracy of flux-differencing DGSEM comes from the symmetry and consistency of the two-point flux, not from entropy conservation (§2.3.1, attributed to Gassner et al.). **Stated**
21. ES-DGSEM was preferred to WENO because "the DGSEM scheme can readily scale to large parallel computations compared to the high-order WENO schemes" (§5). **Stated** (no scaling data)
22. Low-order finite-volume methods suffer from bow-shock carbuncles, wrong surface heating and grid-alignment dependence (§1, cited). **Stated**

# Printed slips

- Leblanc problem (§4.1 and Fig. 1 caption): "the pressure ratio is $10^9$ and the density ratio is $10^5$", but the printed states $\rho=2$ and $0.001$ give a density ratio $2\times10^3$ *(compiler check, not in the sources)*.
- Mach-10 Shu–Osher left state, Eq. (93): $(\rho,v,p)=(3.857143,\,9.76153,\,116.5)$ for a shock into $(1,0,1)$ with $\gamma=1.4$. The Rankine–Hugoniot relations for $M_s=10$ give $p=(2\gamma M_s^2-(\gamma-1))/(\gamma+1)=116.5$ and $\rho=(\gamma+1)M_s^2/((\gamma-1)M_s^2+2)=5.714286$, and with that density $v=M_s\sqrt\gamma\,(1-1/\rho)=9.76153$; the printed pressure and velocity are the Mach-10 values. The printed density $3.857143$ is the post-shock density $27/7$ of a Mach-3 shock, the one of the classical Shu–Osher state $(27/7,\,4\sqrt{35}/9,\,31/3)\approx(3.857143,\,2.629369,\,10.333333)$ printed in exact form by [Li et al. (2022b)](/sources/li-2022-b.md) Eq. (40) and [Ye et al. (2022)](/sources/ye-2022.md) Eq. (44) (see the [Shu–Osher page](/benchmarks/shu-osher-problem.md)) *(compiler check, not in the sources)*. The paper does not say which density the runs used.
- Fig. 2 caption: "the pressure ratio is 100", while the initial data give 116.5.
- §4.5.2 prints "$p_r/p_l=1,561$", but $p_l/p_r=195256/125.07=1561.2$ (inverted); the Fig. 7 caption says "1500".
- Eq. (11), $e^*_{i,rot}=R^*/M_i$, lacks the factor $T^*$; Eq. (60), with $\mathsf a_k=5/2$ for diatomic species, implies $e_{\mathrm{rot}}=r_kT$.
- Eq. (62) prints the vibrational part of $c_{vk}$ with a minus sign. The derivative of $T^{\mathrm v}_k/(e^{T^{\mathrm v}_k/T}-1)$ in $T$ is $+\frac{(T^{\mathrm v}_k)^2}{T^2}\frac{e^{T^{\mathrm v}_k/T}}{(e^{T^{\mathrm v}_k/T}-1)^2}>0$ *(compiler check, not in the sources)*.
- Eq. (27) prints the Arrhenius rate with $\exp(+\nu_\xi/(k_B^*T^*))$, although $\nu_\xi$ is called the activation energy; with this sign the exponential factor decreases as the temperature rises *(compiler check, not in the sources)*.
- Eq. (29) sums over the reactions $\xi$ a summand indexed by the species $i$; Eq. (26) writes products over $m=1,\dots,N_s$ of factors indexed by $i$.
- Eq. (24) prints the Stefan–Maxwell system $\sum_iQ^*_{ij}=-d^*_j$ without the unknown $\tau^*_i$ of Eq. (23).
- Eq. (66), $\omega_{1,k}=e_k/T-s_k-v^2/(2T)$, differs by the constant $r_k$ from the Gibbs form of Eq. (65), $g_k/T=e_k/T+r_k-s_k$; a constant does not change the jumps, so Eqs. (73)–(91) are unaffected *(compiler check, not in the sources)*. The text calls $\omega=\partial(\rho s)/\partial U$, while its last component $-1/T$ belongs to $-\rho s$; the index range is printed "$k=0,\dots,N_s$".
- Eq. (86) prints $\xi/\sinh(\theta_k\xi)$. Substituting $a^\pm=\{\!\{a\}\!\}(1\pm\mathsf j_a)$ in Eq. (81) gives $\{\!\{a\}\!\}_{\exp,k}=\{\!\{a\}\!\}\mathsf j_a/\big(e^{T^{\mathrm v}_k\{\!\{a\}\!\}}\sinh(T^{\mathrm v}_k\{\!\{a\}\!\}\mathsf j_a)\big)$, the argument Eq. (87) uses. The series $\sinh x/x$ has only even powers, so the remainder after the $x^6$ term is $O(x^8)$, not the printed $O(x^9)$ *(compiler check, not in the sources)*.
- §4.5.1 prints the reference density in "kg/s" and calls the air "79% nitrogen N and 21% oxygen O" (atomic symbols), while Table 2 has $N_2$ and $O_2$ with mass fractions 0.767082 and 0.232918.
- §4.6: the inflow sponge is printed on "$x\in[-10^{-4},10^4]$" in a domain $[0,0.02]$; the sponge exponent is $N_s$ in Eq. (101) and "$N_3=3$", "$N=3$" in the text; "beg" and "end" are swapped in the sentence after Eq. (101).
- Typos: "transnational" (§2.2.1), "Newton-Rophson", "Mutaion++" (§4.4).

# Notation map

| Peyvan et al. 2023 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $P$ | $N$ | DGSEM degree, LGL nodes $0,\dots,N$ |
| $N$ (number of elements) | $N_x$ | **collision** with the degree $N$ |
| $U=(\rho_1,\dots,\rho_{N_s},\rho u,\rho E)$, $F^a$, $F^v$, $S$ | $u$, $f$, viscous flux, $S$ | conserved variables, fluxes, source; **the source's $u$ is the velocity $v$** |
| $\rho_i$, $Y_i$, $\chi_i$ ($X_i$) | $\rho_k$, $Y_k$, $\chi_k$ (local) | partial density $\rho Y_k$ (the registry's $\rho_k$ is a phase density), mass and mole fractions; **$\chi_k$ is the TENO measure in the registry** |
| $M_i$, $\dot\omega_i$ | $W_k$, $\Omega_k$ | molar mass and mass production rate (§10) |
| $e^0_k$, $r_k=R/M_k$ | kept | formation energy, species gas constant |
| $a_k$, $\alpha_k$ | $\mathsf a_k$, $\mathsf b_k$ | **collision**: $a$ is the wave speed and $\alpha_k$ the WENO weights |
| $\theta_k$ | $T^{\mathrm v}_k$ | vibrational temperature; **collision** with the Zhang–Shu factor $\theta$ |
| $s_k$, $\rho s$ | $-\eta$ (up to normalization) | physical-like entropy of Gouasmi et al.; registry $\eta$ is convex |
| $\omega$ ($\omega_{1,k},\omega_2,\omega_3$) | $w$ | entropy variables; **collision**: $\omega_j$ are also the LGL weights $\mathsf w_j$ in §2.3 |
| $\phi$, $\psi$ | kept, $\psi$ | entropy potential; entropy-flux potential $\psi=\sum_k\rho_kr_kv$ |
| $[[a]]$, $\{\{a\}\}$ | $[\![a]\!]$, $\{\!\{a\}\!\}$ | agree |
| $\{\{a\}\}^{ln}$ | $\{\!\{a\}\!\}_{\log}$ | logarithmic mean (Ismail–Roe evaluation) |
| $\{\{a\}\}^{exp,k}$, $\{\{a\}\}^{ln,exp,k}$ | $\{\!\{a\}\!\}_{\exp,k}$, $\{\!\{a\}\!\}_{\ln\exp,k}$ | new means (contribution) |
| $\xi=(a^+-a^-)/(a^++a^-)$ | $\mathsf j_a$ | **collision** with the reference nodes $\xi_j$; $\xi$ is also the reaction index |
| $z_{1,k}=\rho_k$, $z_2=u$, $z_3=1/T$ | kept | parameter vector of the derivation |
| $F^{EC}$; $f_{1,k}$, $f_2$, $f_3$ | $f^{\mathrm{ec}}$; $f^{\mathrm{ec}}_{\rho_k}$, $f^{\mathrm{ec}}_{\rho v}$, $f^{\mathrm{ec}}_E$ | entropy-conservative flux and its components |
| $F^{**}$ | $f^{\mathrm{vol}}$ | symmetric consistent two-point volume flux |
| $M$, $D$, $B$, $H=MD$ | $M$, $D$, $B$, $Q=MD$ | SBP matrices; $H$ is the registry's $Q$ |
| $\Delta$, $\bar F_{k,j}$, $F^{FV}$ | kept | subcell difference matrix, flux-differencing subcell fluxes, low-order HLLC subcell fluxes |
| $\alpha$, $\alpha_{max}$ | $\alpha$, $\alpha_{\max}$ | DG–FV blending coefficient; agrees |
| $\lvert J\rvert$ | $J$ | element Jacobian |
| $\sigma$ | kept | viscous stress (Eq. (3)) and sponge coefficient (Eq. (101)); **$\sigma$ is the affine scaling in §10** |
| $Re_\infty$, $Pr_\infty$, $Ec_\infty$ | $\mathrm{Re}$, $\mathrm{Pr}$, $Ec$ | non-dimensional groups |
| $M_s$ | $M_s$ | shock Mach number |

# Reference list

The paper prints 49 references, numbered [1]–[49]. The list is merged
complete into the [bibliography](/bibliography.md), with `citedby` including
`peyvan-2023`. [24] (Gupta 1990) and [30] (Gurvich et al. 1989) print no
venue or publisher and are entered as a report and a book; [45] is a NASA
technical memorandum. [13] prints a duplicated author ("George Em
Karniadakis, George Karniadakis"), entered as printed. Ref. [18] (Dzanic &
Witherden 2022, J. Comput. Phys. 468:111501) is the ingested source
[Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md), keyed
`dzanic-2022-b`, not `dzanic-2022`. No item is unparseable.

# Pages created or updated

Chunk 6 (2026-10-23), cited further in chunks 7–8 (2026-10-23). This source is cited on:

* [Density-wave advection](/benchmarks/density-wave-advection.md)
* [Discontinuous Galerkin spectral element method (DGSEM)](/methods/dgsem.md)
* [Entropy filtering for DG and FR](/methods/entropy-filtering.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)
* [Flux reconstruction and energy-stable FR](/methods/flux-reconstruction.md)
* [Leblanc shock tube](/benchmarks/leblanc-shock-tube.md)
* [Logarithmic mean](/operators/logarithmic-mean.md)
* [Multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Spectral difference method](/methods/spectral-difference-method.md)
* [Subcell finite-volume limiting for DG](/methods/subcell-finite-volume-limiting.md)

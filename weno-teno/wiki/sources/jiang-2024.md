---
type: Source
title: "Jiang et al. (2024) — Embedment of WENO-Z reconstruction in Lagrangian WLS scheme implemented on GPU for strongly-compressible multi-phase flows"
description: "A meshless Lagrangian weighted-least-squares particle method for compressible multiphase flow, stabilized by Roe-type intermediate states between particle pairs and by WENO-Z+-type reconstruction on collinear virtual points, run on one GPU and tested on shock tubes, underwater explosion and bubble collapse near a wall."
resource: "doi:10.1016/j.cma.2024.117209"
source_kind: paper
authors: [Jiang T., Liu Y.-H., Meng Z.-F., Sun P.-N., Wei X.-Y., Wang D.-S.]
year: 2024
venue: "Comput. Methods Appl. Mech. Eng. 430:117209"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Computer_Methods_in_Applied_Mechanics_and_Engineering_Jiang_Embedment_of_WENO-Z_reconstruction_in_Lagrangian_WLS_scheme.pdf"
tags: [weno-z, particle-method, multiphase, gpu, riemann-solver]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper builds a meshless Lagrangian particle method for inviscid compressible
multiphase flow with strong shocks and large volume changes. The base
discretization is the Lagrangian weighted-least-squares method (LWLS, also called
the finite pointset method): each particle fits a second-order Taylor expansion to
its neighbours by weighted least squares and obtains the first derivatives of
$v_1,v_2,p,pv_1,pv_2$ in a non-conservative Lagrangian Euler system (log-density,
velocity, specific internal energy), closed by the
[stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md).
Plain LWLS oscillates at discontinuities, so two stabilizations are proposed.
**LWLS-RR** treats each particle pair as a one-dimensional Riemann problem along
the joining line and replaces the neighbour values in the least-squares data by the
intermediate states of a linearized Lagrangian
[Roe-type solver](/methods/roe-riemann-solver.md). **LWLS-WENO-Z** builds the left
and right states of that Riemann problem by a three-stencil reconstruction with the fifth-order
WENO5 cell-average coefficients on six collinear virtual points (applied to point
values, it gives a second-order midpoint value, as checked on
[WENO-Z+](/methods/weno-z-plus.md) *(compiler check, not in the sources)*), with
[WENO-Z](/methods/weno-z.md)-type weights carrying the extra term of
[WENO-Z+](/methods/weno-z-plus.md), whose coefficient is the pair distance to the
power $2/3$. Values at the virtual points are copied from, or extrapolated to first
order from, the nearest particle. Primitive variables are reconstructed
component-wise, without [characteristic decomposition](/methods/characteristic-decomposition.md).
Particle shifting, a static multi-level particle refinement and an interface
repulsive force complete the method, which runs in CUDA on one GPU with explicit
two-stage Runge–Kutta stepping.

The observed order on smooth [density waves](/benchmarks/density-wave-advection.md)
is about 2 for LWLS-RR and 2.2–2.35 for LWLS-WENO-Z, so the scheme is not fifth
order. The other tests are [Sod tubes](/benchmarks/sod-and-lax-shock-tubes.md),
a cylindrical [explosion](/benchmarks/explosion-and-implosion-problems.md), the
[Shu–Osher problem](/benchmarks/shu-osher-problem.md), a one-sided
[blast wave](/benchmarks/woodward-colella-blast-wave.md), a
[gas–liquid Riemann problem](/benchmarks/gas-liquid-riemann-problems.md), the
[Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md), an
[underwater explosion](/benchmarks/underwater-explosion.md) and a cavitation
[bubble collapse near a wall](/benchmarks/bubble-collapse-near-wall.md) with about
2.09 million particles. Evidence is visual comparison with exact, grid-based and
SPH results; LWLS-WENO-Z is shown less dissipative than LWLS-RR and the SPH
variants, at about five times the cost of LWLS-RR, and the GPU runs 213–243 times
faster than one CPU core.

# Version read

Version of record (Elsevier typeset; received 8 May 2024, accepted 30 June 2024,
online 24 July 2024), 28 pages, all read; pages 4, 6, 7, 8, 14 and 19 checked
visually for Eqs. (6)–(17), Table 2b and the underwater-explosion data. Page 1
matches Crossref (title, six authors, venue, DOI). Numbering cited here is that of
this version.

# Key claims

Registry notation (see the notation map): the source's $SI_{ks}$ are $\beta_k$,
its $D_{ks}$ are $d_k$, its unnormalized weights $\beta^L_{ks}$ are $\alpha_k$, its
$\xi_{ks}$ is $z_k$ and its $\gamma_{weno}$ is $\mu$.

1. LWLS applied directly to compressible flow produces dispersion and oscillation, and its cost is large for millions of particles (§1, §3). **Stated**
2. The authors know of no earlier LWLS particle method for strongly compressible multiphase flow (§1), nor of LWLS-RR used for it (§2.2). **Stated**
3. LWLS-RR: the Roe-type Lagrangian intermediate states $p^{iv}=\tfrac12[p_L+p_R+C_{LR}(\mu_L-\mu_R)]$ and $v^{iv}=\tfrac12[v_L+v_R+(p_L-p_R)\varepsilon_{ni}/C_{LR}]$, with $C_{LR}=\tfrac12(c_L\rho_L+c_R\rho_R)$ and $\mu_{L,R}$ the velocity components along the pair, enter the least-squares data (Eqs. (9a)–(9c)); the discrete equations (10a)–(10d) carry a factor 2 absent from the plain LWLS Eqs. (5a)–(5d), not explained in the text. **Derived**
4. LWLS-RR is smooth but about first order or lower near non-uniform particles ("excessive dissipation"), and still has "slightly lower error or lower dissipation than the WCSPH with Riemann solver" (Remark 1). **Stated** (the comparison is shown only qualitatively, Fig. 9)
5. LWLS-WENO-Z uses the three three-point candidate values of Eq. (13), the Jiang–Shu-type indicators of Eq. (14) and weights $\alpha_k=d_k\big(1+z_k^2+\mu/z_k\big)$, $z_k=(\tau_5+10^{-10})/(\beta_k+10^{-10})$, $\tau_5=\lvert\beta_2-\beta_0\rvert$, $(d_0,d_1,d_2)=(1/10,3/5,3/10)$, $\mu=\lVert x_i-x_n\rVert^{2/3}$ (Eqs. (12)–(15)), attributed to "WENO-Z+ in [20]" (Luo & Wu 2021). **Derived** (construction)
6. The value at a virtual point is copied from the nearest particle if that particle lies within $\lambda_d\Delta x_0$ ($0<\lambda_d\le0.1$), and otherwise extrapolated to first order with the least-squares gradient (Eq. (11)); the authors say this differs from [11,55,61]. **Stated**
7. The method differs from WENO-SPH [11,55,61–63] in the LWLS approximation, the smoothness indicators, particle shifting, multi-level refinement and the GPU algorithm, and from the Eulerian [WLS-ENO](/methods/wls-eno.md) [31,32], which is single-phase with fixed points (Remark 3). **Stated**
8. On the 1D smooth Euler test ($t=2$, $N=100,200,400$, $h/\Delta x_0\in\{1.2,1.5,1.9\}$, particles fixed) LWLS-RR converges at order about 2.00 and LWLS-WENO-Z at 2.22–2.35 with lower errors (Tables 1a, 1b). **Shown**
9. On the 2D smooth Euler test ($t=1$, $N=51^2,101^2,201^2$) LWLS-RR converges at 2.005–2.021 and LWLS-WENO-Z at 2.215–2.351 (Tables 2a, 2b). **Shown**
10. On a non-uniform particle distribution (Fig. 3) the LWLS-WENO-Z errors are "slightly larger … but they are all the same order of magnitude" as on the uniform one (Table 2c, §4.1.2). **Shown** *(Compiler check, not in the sources: at $h/\Delta x_0=1.2$ the $L_{RMS}$ ratio non-uniform/uniform is $2.20\times10^{-3}/6.13\times10^{-4}\approx3.6$ at $51^2$ and $7.67\times10^{-4}/1.24\times10^{-4}\approx6.2$ at $101^2$, and the non-uniform rate is $\log_2(2.20/0.767)\approx1.52$.)*
11. A larger smoothing length raises the computing time roughly in proportion and changes the errors only slightly; $h/\Delta x_0\approx1.5$ is used afterwards (§4.1). **Shown**
12. 1D Sod ($\Delta x_0=0.0025$, $t=0.15$): LWLS-WENO-Z matches the exact solution with lower dissipation than GSPH [56] and WENO-SPH [11] (Fig. 4). **Shown**
13. 2D cylindrical Sod ($\Delta x_0=0.01$, $t=0.2$): lower dissipation than MWSPH [61] and WENO-SPH [11] (Fig. 5a); accuracy increases from no refinement to one and two refinement levels (Fig. 5b). **Shown**
14. LWLS-WENO-Z captures the Shu–Osher problem ($\Delta x_0=0.01$, $t=1.8$) and a 1D blast wave with pressure ratio $10^5$ ($\Delta x_0=0.0025$, $t=0.012$) close to WENO-Z references on 5000 points [28] (Figs. 6, 7). **Shown**
15. It captures the 1D gas–liquid problem of Gu et al. [22] "without the additional treatment" of the interface that mesh-based WENO schemes need, and converges under particle refinement (Fig. 8). **Shown**
16. Rayleigh–Taylor ($t=2.05$, $\Delta x_0=0.002$): LWLS-WENO-Z and WENO-SPH are less dissipative than LWLS-RR and RR-SPH, and LWLS-RR less than RR-SPH (Fig. 9); finer particles ($\Delta x_0=0.001$, $0.0005$) give more roll-ups and weaker asymmetry, consistent with [19] (Fig. 10). **Shown**
17. LWLS-WENO-Z costs about five times LWLS-RR (§5.2.1). **Stated** (no table)
18. GPU speed-up (NVIDIA Titan RTX against one core of an Intel Xeon Silver 4214, $10^4$ Rayleigh–Taylor steps): 213, 233 and 243 at $125\times501$, $251\times1001$ and $501\times2001$ particles; GPU time grows by less than four times per fourfold particle count; full runs to $t=2$ take about 7 h ($\Delta x_0=0.001$) and 32 h ($\Delta x_0=0.0005$) (Table 3). **Shown**
19. Underwater explosion ($\Delta x_0=0.01$ with two refinement levels, about $2.2\times10^5$ particles): density and pressure along $x=0$ agree with the grid-based results of Hu et al. [2], Shukla [5] and Shyue [1]; LWLS-WENO-Z is less dissipative than LWLS-RR (Figs. 11, 12). **Shown**
20. The first particle-shifting correction suffices for expanding interfaces but cannot stop the tensile instability under fast compression (bubble collapse); the second, with refinement, removes it, consistent with Pineda et al. [60] (Fig. 13). **Shown**
21. Bubble collapse near a wall ($H_b/r_b=1.25$, $r_b/\Delta x_0=20$): LWLS-WENO-Z reproduces the bubble depression at $t_d\approx15.3$ and 17 and a micro-jet above 500 m/s; LWLS-RR is too dissipative for either (Fig. 14). **Shown**
22. Pressure histories ($H_b/r_b=2$ and 1.25, about 2.09 million particles) agree with SPH-ALE [59], with small differences after $t_d>15$ when the micro-jet exceeds 500 m/s; vortex-ring, apple and concave-ring shapes are reproduced, and the asymmetry grows as $H_b/r_b$ decreases (Figs. 15–19). **Shown**
23. Riemann-solver weakly compressible SPH is "about first-order or lower near the region of non-uniform particles" (Remark 1, citing [11,52,55–60]). **Stated**

# Printed slips

- Eq. (14): all three smoothness indicators are labelled $SI^L_0$, while the text announces three indicators $SI^L_{ks}$ and Eq. (15) uses $SI^L_2$ and $SI^L_{ks}$.
- Eq. (14), third indicator: the second term is printed $\tfrac14(3\varphi_i-4\varphi_{i+1}+\varphi_{i+1})^2$, with $\varphi_{i+1}$ twice and no $\varphi_{i+2}$, although the first term of the same indicator and the stencil of Eq. (13) use $\varphi_{i+2}$.
- Eq. (13) switches between $\varphi$ and $\phi$ ($\varphi^L_0$ but $\phi^L_1$, $\phi^L_2$).
- Matrix $\mathbf M$ (p. 4): row 2 prints "$dx_2\Delta y_2$" for $\Delta x_2\Delta y_2$; Eq. (6a) prints the second-order factor $(x_{kn}-x_k)$ without the subscript $i$.
- Table 2b, $h/\Delta x_0=1.5$, $L_2$ at $201\times201$: printed $3.95\times10^{-4}$ with rate 2.347 from $2.01\times10^{-4}$; the rate holds for $3.95\times10^{-5}$ (the $L_{RMS}$ on the same row is $3.98\times10^{-5}$), while $3.95\times10^{-4}$ would give $-0.97$ *(compiler check, not in the sources: $\log_2(2.01/0.395)=2.347$)*.
- Table 1b, $h/\Delta x_0=1.9$, $L_2$ at $N=100$: printed $9.23\times10^{-4}$ with rate 2.25 to $1.52\times10^{-4}$, but $\log_2(9.23/1.52)=2.60$; a value near $7.2\times10^{-4}$ (cf. $L_{RMS}=7.36\times10^{-4}$ on the same row) would give 2.25 *(compiler check, not in the sources)*.
- Table 3: the first row prints $125\times501$ particles for $\Delta x_0=0.002$ on $[0,0.25]\times[0,1]$, where the other rows follow $L/\Delta x_0+1$ ($251\times1001$, $501\times2001$), which would give $126\times501$ *(compiler check, not in the sources)*. The printed speed-ups $53.21/0.25=213$, $170.27/0.73=233$, $560.82/2.31=243$ are consistent; the text rounds them to "about 200 times".
- §4.2.2: the inner region of the cylindrical Sod problem, where $(p,\rho)=(1,1)$, is not printed; only the domain $x^2+y^2\le1.5$ is.
- §5.2.3: for $H_b/r_b=1.25$ the second circle of the refined region is centred at $y=0.0135$ m, while $H_b=0.0125$ m; no reason is given.
- Naming: "CBNW" and "CNBW" (§5.2.3, Figs. 13–15); "TIS" (§3.3.3) and "TSI" (§3.4.2); "Getforce Titan RTX" (§3.4); "Courant-Friedrichs-Levy" (§2.2); "wall time t=2" for the physical time (§5.2.1), whereas Fig. 9 is at $t=2.05$.
- Symbol reuse: $Cr$ is both the particle-shifting coefficient (Eq. 16a) and the convergence rate (Eq. 21); $\omega$ both the particle volume (Eqs. 7, 16a, 18) and the WENO weight (Eqs. 12, 15); $\beta$ denotes the unnormalized weights.
- Printed data disagreement, not necessarily a slip: §5.1.3 prints the water pressure of the air–water problem as $0.000359$ (problem attributed to Gu et al. [22]), whereas [Zheng et al. (2021)](/sources/zheng-2021.md) Ex. 5 print $3.059\times10^{-4}$ for the same states $(1.241,2.753)$ / $(0.991,\cdot)$ with $\gamma=5.5$, $p_\infty=1.505$, and [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) print a garbled tuple containing the same $3.059\times10^{-4}$ (see [gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md)). Which value Gu et al. print cannot be settled from these sources.

# Notation map

| Jiang et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho,p,e$, $\mathbf u=(u,v)$ | $\rho$, $p$, $e$, $v=(v_1,v_2)$ | Lagrangian, internal-energy form |
| $\gamma$, $P_B$ | $\gamma$, $p_\infty$ | stiffened gas $p=(\gamma-1)\rho e-\gamma p_\infty$ |
| $c$ | $c$ | sound speed $\sqrt{\gamma(p+p_\infty)/\rho}$ |
| $C_{LR}$ | kept | mean acoustic impedance $\tfrac12(c_L\rho_L+c_R\rho_R)$, called a speed of sound in the source |
| $p^{iv}$, $\mathbf u^{iv}$ | $p^{iv}$, $v^{iv}$ | Riemann intermediate states |
| $\mu_L$, $\mu_R$ | kept | velocity components along the pair; **$\mu$ collides with the WENO-Z+ coefficient** below |
| $\boldsymbol\varepsilon_{ni}$ | $\varepsilon_{ni}$ | unit vector from particle $i$ to $n$; $\varepsilon$ also the second shifting coefficient |
| $\varphi_k$, $k=i-2,\dots,i+3$ | kept | primitive values $(\rho,v_1,v_2,p)$ at collinear virtual points |
| $\varphi^L_{i+1/2}$, $\varphi^R_{i+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | left and right states at the pair midpoint |
| $ks=0,1,2$, $\varphi^L_{ks}$ | $S_k$, $u^{(k)}$ | stencil 0 = $\{i-2,i-1,i\}$, the most upwind; agrees |
| $SI^L_{ks}$ | $\beta_k$ | Jiang–Shu indicators |
| $\lvert SI_2^L-SI_0^L\rvert$ | $\tau_5$ | |
| $\xi_{ks}$ | $z_k$ | WENO-Z+ ratio term, as on [WENO-Z+](/methods/weno-z-plus.md) |
| $\beta^L_{ks}$ | $\alpha_k$ | **unnormalized weights, not smoothness indicators; collides with $\beta_k$** |
| $\omega^L_{ks}$ | $\omega_k$ | normalized weights; **$\omega_i$ is also the particle volume** |
| $D_{ks}$ | $d_k$ | linear weights |
| $\gamma_{weno}$ | $\mu$ | WENO-Z+ coefficient $\lVert x_i-x_n\rVert^{2/3}$; **$\gamma$ collides with the ratio of specific heats** |
| $10^{-10}$ | $\epsilon$ | |
| $h$, $\Delta x_0$, $w_{in}$ | kept | smoothing length, initial spacing, kernel weight |
| $Cr$ | kept | shifting coefficient and convergence rate (both) |
| $r_b$, $H_b$, $t_d=t/(r_b/c_L)$ | kept | bubble radius, wall distance, scaled time |

# Reference list

92 printed references in numbered Elsevier style ([1]–[92]), all parsed and merged
complete into the [bibliography](/bibliography.md) with `citedby` `jiang-2024`. Only
ref. [63] prints a DOI. Ref. [20] (Luo & Wu, JCP 445:110608) is the ingested
`luo-2021-b`; refs. [11], [29], [42], [88], [89] share an author–year label with
ingested sources but are different works and are keyed apart by venue; ref. [91]
(Jiang et al. 2024, CPC 296:109023) is keyed apart from this source's own slug.
Printed oddities are kept as printed ("K.Y.Lam Lam" [13], "compact unwind scheme"
[15], "Cavitaion" [60], "Yong Kong" [87]). No printed duplicates were found.

# Pages created or updated

Chunk 7 (2026-10-23), cited further in chunks 8–12 (2026-10-23/30). This source is cited on:

* [Bubble collapse near a wall](/benchmarks/bubble-collapse-near-wall.md)
* [Density-wave advection](/benchmarks/density-wave-advection.md)
* [Gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md)
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)
* [Roe approximate Riemann solver](/methods/roe-riemann-solver.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Two-dimensional explosion and implosion problems](/benchmarks/explosion-and-implosion-problems.md)
* [Underwater explosion](/benchmarks/underwater-explosion.md)
* [WENO-Z weights](/methods/weno-z.md)
* [WENO-Z+ and WENO-Z+M](/methods/weno-z-plus.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)

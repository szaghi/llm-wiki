---
type: Source
title: "Wang et al. (2023) — An efficient hybrid multi-resolution WCNS scheme for solving compressible flows"
description: "Fifth-order explicit WCNS whose node-to-midpoint interpolation is a simplified multi-resolution WENO on nested 5-, 3- and 1-point stencils with a new parameter-free constant-level indicator, switched off by a hybrid test on the extreme points of the derivative of the five-point interpolant; claimed fifth order for arbitrary linear weights at roughly WENO-JS cost."
resource: "doi:10.1016/j.jcp.2022.111877"
source_kind: paper
authors: [Wang Z., Zhu J., Wang C., Zhao N.]
year: 2023
venue: "J. Comput. Phys. 477:111877"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Journal_of_Computational_Physics_Wang_An_efficient_hybrid_multi-resolution_WCNS_scheme_for_solving.pdf"
tags: [compact-scheme, multi-resolution, hybrid-scheme, smoothness-indicator, troubled-cell, finite-difference]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

Wang, Zhu, Wang & Zhao propose a fifth-order finite-difference **hybrid multi-resolution
WCNS** for the compressible Euler and Navier–Stokes equations. The base is the explicit
[weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md): sixth-order
midpoint-to-node flux differencing with coefficients $(75/64,-25/384,3/640)$ and a
Lax–Friedrichs flux of interpolated left and right solution values at the midpoints. The
node-to-midpoint interpolation follows the multi-resolution WCNS (MR-WCNS) of Zhang, Wang &
Zhang, which transposes [multi-resolution WENO](/methods/multi-resolution-weno.md) to WCNS.

The paper makes two changes. (i) A simplified multi-resolution interpolation on nested central
stencils of 5, 3 and 1 points, combined in the [CWENO](/methods/cweno.md) manner. It uses
Jiang–Shu [smoothness indicators](/definitions/smoothness-indicator.md) for the degree-4 and
degree-2 polynomials, a new parameter-free indicator for the constant, and WENO-Z-type weights
with a squared global indicator. The authors claim this keeps fifth order for any linear
weights, while the original MR-WCNS loses it for two of three tested weight sets. (ii) A
[hybrid](/methods/hybrid-weno.md) switch: the nonlinear interpolation is used only where an
extreme point of the derivative of the five-point interpolant lies inside the stencil;
elsewhere the linear fifth-order midpoint value is used. The authors present this
[troubled-cell indicator](/definitions/troubled-cell-indicator.md) as problem-independent and
free of tuning parameters.

All evidence is numerical. Accuracy is tested on 1D and 2D sine
[density-wave advection](/benchmarks/density-wave-advection.md), for Euler and Navier–Stokes.
The shock tests are Shu–Osher, Woodward–Colella blast waves, double Mach reflection,
shock–bubble interaction, single- to treble-mode Richtmyer–Meshkov instability, inviscid and
viscous Rayleigh–Taylor instability, a viscous shock–mixing layer and the Daru–Tenaud viscous
shock tube. Both MR-WCNS schemes resolve more structure than WENO-JS. The hybrid scheme costs
0.81 to 1.07 times WENO-JS, against 1.50 to 2.31 times for the original MR-WCNS. No theorem is
proved.

# Version read

Version of record (Elsevier typeset, J. Comput. Phys. 477, 111877), 22 pages, DOI printed on
page 1; received 16 Aug 2022, online 9 Jan 2023. Title, authors and venue match Crossref; no
identity problem. Equation, table and figure numbers are those of the version of record.

# Key claims

Registry notation, with the [multi-resolution WENO](/methods/multi-resolution-weno.md) page's
nested-stencil labels: $T_1=\{x_i\}$, $T_2=\{x_{i-1},x_i,x_{i+1}\}$,
$T_3=\{x_{i-2},\dots,x_{i+2}\}$, polynomials $P_m$ of degree $2m-2$, linear weights $d_m$,
indicators $\beta_m$, weights $\alpha_m$, $\omega_m$ ($m=1$ the smallest; the source numbers the
stencils the other way round, see the Notation map). $u_i$ are node values, $u^-_{i+1/2}$ the
left interpolated midpoint value.

1. The node-to-midpoint nonlinear interpolation dominates the resolution and accuracy of WCNS (§1, §3 after Eq. (3.3)). **Stated** (cited)
2. In the classical WCNS/WENO-JS interpolation the linear weights are fixed by the design order; MR-WCNS makes their choice free by nesting the stencils (§1, §3 Step 2.2). **Stated**
3. The original MR-WCNS costs "more than 50%" more CPU time than WENO-JS (§1, "roughly estimated"); Table 5.1 gives factors from 1.50 (Ex. 4.3) to 2.31 (Ex. 4.7, $n=60$) (§5). **Shown**
4. The predefined linear weights of the original MR-WCNS "have a negative impact on the smoothness indicators for the smooth problems": it reaches fifth order only with $(d_3,d_2,d_1)=(100,10,1)/111$, not with $d_m=1/3$ or $(1,10,100)/111$ (§1, Remark 2, Ex. 4.1, Figs. 4.1–4.4). **Shown** (only graphically; no error table for the second and third weight sets)
5. The proposed MR-WCNS reaches fifth order with all three tested weight sets, which "truly realizes the arbitrariness of the linear weights" (Remark 2, Ex. 4.1, Figs. 4.1–4.4). **Shown** (three weight sets; no proof)
6. $P_3=d_3\tilde P_3+d_2P_2+d_1P_1$ with $\tilde P_3=(P_3-d_2P_2-d_1P_1)/d_3$ holds for any $d_1+d_2+d_3=1$, $d_3\ne0$, after Levy, Puppo & Russo (Eqs. (3.17)–(3.18)). **Derived** (identity)
7. The new constant-level indicator $\beta_1=\min\big((u_{i-1}-u_i)^2,(u_i-u_{i+1})^2\big)$ (Eq. (3.22)) is simpler than that of the original MR-WCNS, has no artificial parameter and is cheaper. The weights are $\alpha_m=d_m\big(1+\tau/(\epsilon+\beta_m)\big)$ with $\tau=\big((\lvert\beta_3-\beta_2\rvert+\lvert\beta_3-\beta_1\rvert)/2\big)^2$ and $\epsilon=10^{-6}$ (Eq. (3.23)) (§3 Steps 2.3–2.4). **Stated**
8. The hybrid switch is problem-independent and has no artificial parameter. The nonlinear interpolation is used where an extreme point of $P_3'$ lies inside $T_3$; elsewhere the linear value $P_3(x_{i+1/2})=(3u_{i-2}-20u_{i-1}+90u_i+60u_{i+1}-5u_{i+2})/128$ is used (Step 2, Eq. (3.9), Remark 1, §6). **Stated**; the marked points are plotted in Figs. 4.5(c)–4.18(d). **Shown** (qualitative)
9. The scheme "can gradually decrease from high-order accuracy to first-order accuracy near the discontinuities" (Abstract, §1). **Stated** (no analysis in this paper)
10. 1D Euler accuracy ($\rho_0=1+0.2\sin(\pi x)$, $t=2$, default weights): at 320 points the $L^1$ errors are $1.93\times10^{-10}$ (WENO-JS), $2.07\times10^{-11}$ (MR-WCNS) and $1.10\times10^{-11}$ (hybrid), all of order about 5 (Table 4.1). **Shown**
11. 1D Navier–Stokes accuracy ($\mu=0.0005$, $\mathrm{Pr}=2/3$, $\gamma=5/3$, $\mathrm{Re}=1000$; asymptotic convergence errors): at 320 points $L^1$ $7.68\times10^{-9}$, $7.45\times10^{-10}$, $7.31\times10^{-10}$ (Table 4.2). **Shown**
12. 2D Euler and Navier–Stokes accuracy: fifth order for all schemes; at $320\times320$, $L^1$ $4.28\times10^{-10}$, $4.95\times10^{-11}$, $4.65\times10^{-11}$ (Euler) and $1.44\times10^{-8}$, $1.52\times10^{-9}$, $1.50\times10^{-9}$ (Navier–Stokes) for WENO-JS, MR-WCNS and hybrid (Tables 4.3–4.4). **Shown**
13. In the accuracy tests the hybrid errors are "much smaller" than WENO-JS (about one order of magnitude) and its efficiency is "the highest among these three methods" (Ex. 4.1, Figs. 4.1–4.4). **Shown** (the claim concerns the accuracy tests; in Table 5.1 the hybrid scheme is slower than WENO-JS in four of twelve shock runs)
14. On the shock problems both MR-WCNS schemes resolve more structure than WENO-JS on the same grid; for the blast waves the hybrid scheme "gives better results than the other two schemes" (Exs. 4.3–4.10). **Shown** (qualitative)
15. Hybrid symmetry errors (Eq. (4.6)) for shock–bubble interaction are $4.57\times10^{-13}$ at $t=0.2$ and $7.28\times10^{-7}$ at $t=0.4$. The growth at $t=0.4$ "may be caused by the vanishing numerical viscosity", after Fleischmann et al. (Ex. 4.6). **Shown**; explanation **Stated**
16. Richtmyer–Meshkov symmetry errors (Eq. (4.6)) are $3.05\times10^{-11}$, $6.28\times10^{-14}$ and $8.28\times10^{-10}$ for $n=20,40,60$ (Ex. 4.7). **Shown**
17. In the Richtmyer–Meshkov runs the marked points are periodic rather than symmetric in some regions. The authors attribute this to the local characteristic decomposition: classifying in conservative variables would give symmetric marks. They keep characteristic variables because these "more accurately identify the troubled cells" (Ex. 4.7). **Stated**
18. Rayleigh–Taylor symmetry errors (Eq. (4.9)) are $1.07\times10^{-12}$ (inviscid) and $1.55\times10^{-14}$ (viscous, $\mathrm{Re}=50000$) (Ex. 4.8). **Shown**
19. CPU times relative to WENO-JS (Table 5.1): hybrid 0.89, 0.81, 0.87, 1.01, 1.05, 0.94, 1.05, 1.07, 0.86, 0.84, 0.96, 0.85; MR-WCNS 1.50, 1.64, 1.92, 1.86, 1.81, 1.76, 1.84, 2.31, 1.70, 1.89, 2.22, 1.75 (Exs. 4.3–4.10). No hardware, compiler or parallel setting is given (§5). **Shown**
20. The proposed method performs like the existing MR-WCNS at lower cost, and both outperform WENO-JS (§5, §6). **Shown** (qualitative and Table 5.1)
21. Implicit WCNS (non-zero compact coefficient in Eq. (3.3)) needs a tridiagonal solve, so the explicit form (coefficient zero) is used (§3). **Stated**
22. The Lax–Friedrichs flux is chosen "from the perspective of stability and computational efficiency" (§3 after Eq. (3.5)). **Stated**
23. Local [characteristic decomposition](/methods/characteristic-decomposition.md) with Roe-averaged eigenvectors reduces spurious oscillations; all interpolations act on characteristic variables, dimension by dimension (Remark 3, App. A). **Stated**

# Printed slips

- Eq. (3.20), $\beta$ of the degree-4 polynomial: the cross term $-3495756\,u_iu_{i+1}$ is missing from the bracket; the printed list has $-3495756\,u_{i-1}u_i$ but no $u_iu_{i+1}$ term. *(compiler check, not in the sources)*: evaluating the Jiang–Shu indicator (3.19) of the five-point interpolant (3.7) symbolically reproduces the other fourteen printed coefficients exactly and gives $-3495756$ for $u_iu_{i+1}$. Without it the printed bracket does not vanish on constant data (it sums to $3495756$).
- §3 after (3.3): "the implicit WCNS scheme involves the solution of a diagonal matrix", one sentence after "a tridiagonal matrix will be generated".
- §3 Step 2.2: "multi-resolution WNEO scheme" (for WENO).
- Ex. 4.10: "Fig. 4.16(d) marks the points where the nonlinear MR-WCNS scheme needs to be used": the marks for this example are in Fig. 4.18(d) (Fig. 4.16 is the viscous Rayleigh–Taylor case). The same paragraph says "both schemes" while three are compared.
- Eqs. (4.6), (4.9): $N_x$, $N_y$ are called "the numbers of grid points", while the sums run over $i=0,\dots,N_x$ and the denominators use $N_x+1$, $N_y+1$; the upper limit $(N_y-1)/2$ of (4.6) needs $N_y$ odd.
- Eq. (4.10): the perturbation is introduced as "a fluctuation for the horizontal and vertical velocity components", but only $v'$ is given.

# Notation map

| Wang et al. 2023c | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $h$ | $\Delta x$ | uniform spacing |
| $\mathbf U$, $\mathbf F_c$, $\mathbf F_v$ | $u$, $f$, viscous flux | vectors not bold |
| $u$, $v$ (velocity) | $v_1$, $v_2$ | **collision**: the source's $u$ is also the scalar unknown |
| $f'_i$ | $\partial_xf$ at $x_i$ | midpoint-to-node flux derivative |
| $\kappa$; $a_1,a_2,a_3$ | compact coefficient (in words); $\mathsf a_1,\mathsf a_2,\mathsf a_3$ (page-local) | flux-difference coefficients $(75/64,-25/384,3/640)$; **collision**: $\kappa$ is the kinetic energy and $a$ the wave speed in the registry |
| $u^L_{i+1/2}$, $u^R_{i+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | interpolated solution values, not point fluxes |
| $S_1$, $S_2$, $S_3$ (5, 3, 1 points) | $T_3$, $T_2$, $T_1$ | order reversed; the registry's $S_k$ are shifted stencils |
| $p_1$, $p_2$, $p_3$; $\tilde p_1$ | $P_3$, $P_2$, $P_1$; $\tilde P_3$ | point-value interpolants of degree 4, 2, 0 |
| $\gamma_1,\gamma_2,\gamma_3$ | $d_3$, $d_2$, $d_1$ | linear weights; default $(100,10,1)/111$ for $(d_3,d_2,d_1)$; **collision** with $\gamma$ (ratio of specific heats) |
| $\beta_1$, $\beta_2$, $\beta_3=\min(\beta_{31},\beta_{32})$ | $\beta_3$, $\beta_2$, $\beta_1$ | Jiang–Shu for the first two; new min-of-squared-differences for the constant |
| $\tau$ | $\tau$ (page-local) | $\big((\lvert\beta_3-\beta_2\rvert+\lvert\beta_3-\beta_1\rvert)/2\big)^2$ in registry labels; not the registry's $\tau_5$ |
| $\bar\omega_n$, $\omega_n$ | $\alpha_m$, $\omega_m$ | Z-type, power 1 on the ratio |
| $\varepsilon$ | $\epsilon$ | $10^{-6}$ |
| $\mathbf L_{i+1/2}$, $\mathbf R_{i+1/2}$, $\mathbf W$ | $L_{i+1/2}$, $R_{i+1/2}$, $\zeta$ | characteristic variables (§10); Roe average |
| $\sigma$, $Re$, $Pr$ | Euler/Navier–Stokes switch, $\mathrm{Re}$, $\mathrm{Pr}$ | |
| $T$ | final time, temperature (§2), period (Ex. 4.9) | overloaded in the source |
| $SE$ | symmetry error | Eqs. (4.6), (4.9) |
| MR-WCNS($k$), Hybrid MR-WCNS($k$) | scheme with the $k$th linear-weight set | $k=1$: $(100,10,1)/111$; $k=2$: $1/3$ each; $k=3$: $(1,10,100)/111$ for $(d_3,d_2,d_1)$ |

# Reference list

The paper prints 51 references, numbered [1]–[51]; no reference prints a DOI. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby` including
`wang-2023-c`. [4] is an AIAA conference paper without pages and [32] a NASA contractor
report; [32], [35] and [36] print "et al.". Same-surname-year works take suffixes in printed
order ([36] Z.J. Wang 2017, [38] Q. Wang 2017). Two cited works share an author–year key with
different Source pages and are re-keyed at the merge: [37] (Wang et al. 2021, Comput. Methods
Appl. Mech. Eng. 382:113853) and [48] (Zheng et al. 2021, Appl. Math. Mech. 42:405–424). [15]
(Hiejima 2022) and [39] (Wong et al. 2021) are ingested sources. No item is unparseable.

# Pages created or updated

Chunk 6 (2026-10-23), cited further in chunks 7–10 (2026-10-23). This source is cited on:

* [Central WENO (CWENO)](/methods/cweno.md)
* [Density-wave advection](/benchmarks/density-wave-advection.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Multi-resolution WENO](/methods/multi-resolution-weno.md)
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [Viscous shock tube (Daru–Tenaud)](/benchmarks/viscous-shock-tube.md)
* [Weighted compact nonlinear schemes (WCNS)](/methods/weighted-compact-nonlinear-scheme.md)
* [WENO-Z weights](/methods/weno-z.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)

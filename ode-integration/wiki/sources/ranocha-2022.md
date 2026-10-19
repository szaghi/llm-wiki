---
type: Source
title: "Ranocha et al. (2022) — Optimized Runge-Kutta Methods with Automatic Step Size Control for Compressible Computational Fluid Dynamics"
description: "Shows that error-based PID step-size control of explicit embedded Runge–Kutta pairs matches or beats tuned CFL control in compressible CFD, optimizes controllers under step-size-control stability, and builds new low-storage 3S*+ pairs of orders 3–5."
resource: "doi:10.1007/s42967-021-00159-w"
source_kind: paper
authors: [Ranocha H., Dalcin L., Parsani M., Ketcheson D.I.]
year: 2022
venue: "Commun. Appl. Math. Comput. 4:1191-1228"
local_file: "/home/stefano/papers/mosaic/ode-integration/2021_Crossref_Communications_on_Applied_Mathematics_and_Computation_Ranocha_Optimized_Runge-Kutta_Methods_with_Automatic_Step_Size_Contr.pdf"
tags: [step-size-control, embedded-pair, low-storage, runge-kutta, explicit, cfd]
timestamp: 2026-10-19T12:00:00Z
---

# Summary

The paper asks whether error-based [step-size control](/methods/step-size-control.md)
with an [embedded Runge–Kutta pair](/methods/embedded-runge-kutta-pair.md) can match
hand-tuned CFL control for explicit time integration of compressible CFD
semi-discretizations (entropy-dissipative nodal DG/SBP collocation in the SSDC
solver built on [PETSc TS](/software/petsc-ts.md)), where the step is usually limited
by linear stability, not accuracy. On 2D linear advection, a standard PI controller
settles at essentially the largest stable CFL number $\nu$ over tolerances
$10^{-5}$–$10^{-3}$. It uses as many right-hand-side evaluations as the best tuned
CFL number and finds a doubled stable step on a curvilinear grid without tuning.

The central technical point is **step-size-control stability**. When $h$ sits on the
boundary of the stability region, the coupled dynamics of method, error estimator and
PID controller have a fixed point whose Jacobian must have spectral radius below one.
A controller designed for one pair can be unstable for another. The authors
therefore optimize the PID exponents $(\beta_1,\beta_2,\beta_3)$ for each pair by
brute-force search on three Euler problems ([Taylor–Green vortex](/benchmarks/taylor-green-vortex.md),
[isentropic vortex](/benchmarks/isentropic-vortex.md), a source-term flow), restricted
to controllers stable along the whole boundary, and recommend controllers for 14 pairs.

They then build new [low-storage](/methods/low-storage-runge-kutta.md) 3S\*$_+$
pairs (orders 3, 4, 5, with FSAL variants) on the main methods of
Parsani–Ketcheson–Deconinck, whose [optimized stability polynomials](/methods/optimal-stability-polynomial.md)
target DG spectra, with embedded methods whose stability region contains that of
the main method. The third-order pairs are up to 18% more efficient than
Bogacki–Shampine BS3(2)3F, and the higher-order ones up to 25–35% better than the
Kennedy–Carpenter–Lewis pairs. In industrial-scale runs error-based control at
tolerance $10^{-8}$ costs about half of CFL control at $\nu=1$ and needs no tuning.
Third-order pairs, including the [SSP](/methods/strong-stability-preserving-runge-kutta.md)
SSP3(2)4[3S\*$_+$], are recommended. The methods are contributed to
[DifferentialEquations.jl](/software/differentialequations-jl.md). All evidence is
numerical.

# Version read

arXiv:2104.06836v2 [math.NA], stamped 24 Jul 2021 (title page dated 21 July 2021).
This is not the journal version of record: the issue is 2022, the paper was online
in 2021, and the archive filename carries the online year. The PDF has 51 pages: 34
pages of main paper (with references and Appendices A–B), then 17 pages of
Supplementary Material dated 14 April 2021, not re-dated for v2. Title and authors
match Crossref; there is no identity problem. Section, table, equation and page
numbers on this page are those of arXiv v2.

# Key claims

1. In the stability-limited regime of 2D linear advection (spatial degree 4, uniform grid), a PI controller ($\beta_1=0.7$, $\beta_2=-0.4$) with KCL4(3)5[2R$_+$]C takes almost exactly the same number of steps as a tuned CFL controller at the largest stable $\nu=2.1$ for tolerances in $[10^{-5},10^{-3}]$; there the right-hand-side count and error barely depend on the tolerance, while below $10^{-6}$ the controller detects accuracy limits (§3, Fig. 2). **Shown**
2. On a curvilinear unstructured grid $\nu=2.1$ remains stable but $\nu$ can be doubled ($4.2$ for KCL4(3)5[2R$_+$]C; $2.5$ against $1.3$ for SSP3(2)3) without much larger error, and the error-based controller finds this step by itself (§3, Fig. 3). **Shown**
3. CK4(3)5[2N] and KCL4(3)5[2R$_+$]C share the largest stable $\nu=2.1$ on this problem, with nearly identical cost and error (§3). **Shown**
4. The efficiency of CFL control "always bears a linear sensitivity" to $\nu$ and $\Delta x$, while error-based control is relatively insensitive to $\mathrm{atol}$, $\mathrm{rtol}$ (§3). **Stated** (illustrated)
5. Outside the asymptotic regime, step-size-control stability matters: for $y'=\lambda y$ the map (pair + PID) has fixed points on the stability boundary, and stability requires the spectral radius of its Jacobian (4.2) to be below one (§4, Eqs. (4.1)–(4.2), citing Hairer–Wanner Prop. IV.2.3). **Stated** (background)
6. A controller designed for one pair need not suit another: PI34, $(\beta_1,\beta_2,\beta_3)=(0.70,-0.40,0)$, with BS5(4)7F on advection at tolerance $10^{-5}$ needs 5015 evaluations and 132 rejections, while the optimized $(0.28,-0.23,0)$ needs 4119 and none, at equal error (§4, Table 2). **Shown**
7. PI34 is step-size-control unstable for BS5(4)7F near the negative real axis (spectral radius up to about 2.2 near $\arg z=\pi$), whereas $(0.28,-0.23,0)$ is stable along the whole boundary (§4, Fig. 4). **Shown** (computed)
8. For SSP4(3)10[3S\*$_+$] no tested PID controller is step-size-control stable, nor for SSP3(2)9[3S\*$_+$] with the embedded method of Conde et al.; a new embedded method for the latter, with a stable controller, did not beat SSP3(2)4[3S\*$_+$] (§5). **Shown** / **Stated**
9. Good controllers are usually within about 5% of the best performance, and no single controller is best on every test (§5.4). **Shown**
10. Among general-purpose pairs (spatial degree 2), BS3(2)3F is about 50% more efficient than BS5(4)7F and DP5(4)6F when stability-limited (Taylor–Green, tolerance $10^{-5}$: 5256, 7722, 8014 evaluations); T5(4)6F is about 5% better than BS5(4)7F (§5.5.1, Table 3). **Shown**
11. Matching temporal to spatial order is not necessary on a fixed mesh: BS3(2)3F stays the most efficient general-purpose method up to spatial degree 4, and even 7 at tolerance $10^{-8}$ (§5.5.1, Suppl. Tables 2–5). **Shown**
12. SSP3(2)4[3S\*$_+$] with $(0.55,-0.27,0.05)$ is about 50% better than SSP3(2)3 or BS3(2)3F at loose and medium tolerances on Taylor–Green (3438 against 5256/5261 evaluations), but its cost grows sharply at tight tolerances, and its embedded estimator "does not seem to be reliable enough" (§5.5.2, Table 4). **Shown**
13. The 2R low-storage pairs of Kennedy–Carpenter–Lewis are beaten by BS3(2)3F on every test at almost every tolerance; the authors attribute this to the 2R constraints, the lack of FSAL, and embedded stability regions smaller than the main method's in places (§5.5.4, Fig. 5). **Shown** (explanation **Stated**)
14. Low Mach numbers stress real-axis stability more than the rest of the advection spectrum, and methods with longer negative-real-axis coverage do better there (Taylor–Green at Mach 0.1) (§5.5.4). **Shown** (experiments mentioned, not displayed)
15. The new third-order pairs RK3(2)5[3S\*$_+$] and RK3(2)5F[3S\*$_+$] are up to 18% more efficient than BS3(2)3F, in line with the scaled real stability intervals ($0.99$ against $0.84$, Suppl. Table 1), and up to 5% (Taylor–Green) and 13% (isentropic vortex) better than KCL4(3)5[3R$_+$]C with an optimized PID (§6.2, Table 6). **Shown**
16. The new fourth-order pairs are up to 25% more efficient than the best KCL methods with the KCL-recommended controller; their main methods make good embedded methods and controllers hard to design (§6.2). **Shown**
17. The new fifth-order pairs beat KCL5(4)9[2R$_+$]S with its prescribed controller by up to 25% (source term), 35% (isentropic vortex) and 18% (Taylor–Green), but lose to the new third- and fourth-order pairs unless the tolerance is very tight (§6.2). **Shown**
18. FSAL pairs are often more efficient than non-FSAL ones, especially at loose tolerances; the new 3S\*$_+$ FSAL pairs are recommended for stability-limited hyperbolic problems (§6.2). **Shown**
19. Pairs with more stages, or third-order methods optimized for a fifth-order spatial discretization, gave no consistent speed-up, consistent with the similar scaled convex hulls of the DG spectra for degrees 1–4 (§6.2–6.3, Fig. 7). **Shown**
20. Viscous shock (Mach 2.5, Re 10): RK3(2)5F[3S\*$_+$] is about 18% and SSP3(2)4[3S\*$_+$] about 50% more efficient than BS3(2)3F (533, 450, 615 evaluations at spatial degree 2, tolerance $10^{-5}$) (§7.1, Table 7). **Shown**
21. NASA juncture flow ($\approx4.09\times10^7$ unknowns, Re $2.4\times10^6$, Mach 0.189): CFL control at $\nu=1.0$ works but costs about 50% more evaluations and wall-clock time than error control at tolerance $10^{-8}$ (BS3(2)3F: 3598 against 1786 evaluations, 1171.60 s against 586.49 s); SSP3(2)4[3S\*$_+$] is nearly 50% faster than BS3(2)3F (§7.2, Table 8; Shaheen XC40). **Shown**
22. Imperial Front Wing ($3.4\times10^6$ hexahedra, Re $2.2\times10^5$, Mach 0.036): error control at $10^{-8}$ again costs about half of CFL control at $\nu=1.0$. At spatial degree 1, CFL control at $\nu=1.0$ crashed for SSP3(2)4[3S\*$_+$]; $\nu=0.85$ worked and was a few percent cheaper than untuned error control (1304 against 1352 evaluations) (§7.3, Tables 9–10). **Shown**
23. Error-based control moves the choice of critical parameters from the spatial-discretization developer to the time-integrator developer; the recommended default tolerance for applied CFD is about $10^{-8}$ (§8). **Stated**
24. Error-based control is robust for "cold start-up" from free-stream data around complex geometries, which CFL approaches must handle by adjusting the CFL scaling (§8). **Stated** ("not demonstrated in this article")
25. The advice of Kennedy–Carpenter–Lewis that "coping with step size control instability is probably best accomplished by reducing step sizes" can be improved on by optimizing the controller (§8). **Stated** (supported by §4–6)
26. This is presented as the first systematic study of how controller parameters and step-size-control stability affect the efficiency of explicit Runge–Kutta methods in CFD (§8). **Stated**
27. A good time integrator is the combination of main method, error estimator and step-size controller, not the main method alone (§8). **Stated**

# Printed slips

- Algorithm 1 (p. 4): "$\widehat u^{n+1}\leftarrow(S_2+\delta_sS_1+\delta_{s+1}S_3)/(\sum_{i=1}^{s+1}\delta_i)$". The loop already adds $\delta_sS_1$, the tables list only $\delta_1,\dots,\delta_s$ with $\delta_s=0$, and no $\delta_{s+1}$ is given; Ketcheson (2010) uses $\delta_{s+1}$, $\delta_{s+2}$ and $\sum_{j=1}^{s+2}\delta_j$. The indices look shifted by one. The new methods use Algorithm 2 and are unaffected. Suspected; not checked against Ketcheson (2010).
- §7.2 (p. 20): "the wing span is 77.89ℓ" with $\ell=557.1$ mm (about 43 m), against a fuselage of $8.69\ell$ (about 4.8 m): implausible for a wind-tunnel model; suspected slip, not checked against the juncture-flow geometry.
- §6.3 (p. 18): "$p\in 1,2,3,4$", set braces missing.
- §2.2 against §4: $k$ is defined as $\min(q,\widehat q)+1$ and later as "the order of the error estimator"; the two agree only when $\widehat q=q-1$.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u(t)$, $\frac{d}{dt}u=f(t,u)$, $u\in\mathbb R^m$ | $y(t)$, $y'=f(t,y)$, $y\in\mathbb R^d$ | non-autonomous form |
| $\Delta t_n$, $u^n$ | $h_n$, $y_n$ | $t_{n+1}=t_n+h_n$ in both |
| $y_i$ | $Y_i$ | stage values |
| $A$, $b$, $c$, $\widehat b\in\mathbb R^{s+1}$ | $A$, $b$, $c$, $\hat b$ | $\widehat b_{s+1}\neq0$ marks an FSAL pair |
| $u^{n+1}$, $\widehat u^{n+1}$ | $y_{n+1}$, $\hat y_{n+1}$ | |
| **$q$, $\widehat q$** | $p$, $\hat p$ | **collision:** registry $q$ is the stage order |
| **$p$** | spatial polynomial degree, written in words here | **collision** with the registry classical order; $p$ also denotes pressure in (5.2)–(5.5) |
| $k=\min(q,\widehat q)+1$ | $k=\min(p,\hat p)+1$ | agrees |
| $\Delta t_{n+1}=\varepsilon_{n+1}^{\beta_1/k}\varepsilon_n^{\beta_2/k}\varepsilon_{n-1}^{\beta_3/k}\Delta t_n$ | $h_{n+1}=h_n\,\mathrm{err}_n^{-\beta_1/k}\mathrm{err}_{n-1}^{-\beta_2/k}\mathrm{err}_{n-2}^{-\beta_3/k}$ | $\varepsilon_{n+1}=1/w_{n+1}$ and $w_{n+1}=\mathrm{err}_n$; the $\beta$ values carry over unchanged |
| **$\varepsilon_{n+1}$** | $1/\mathrm{err}_n$ | **collision** with the registry stiffness parameter $\varepsilon$ |
| $w_{n+1}$ | $\mathrm{err}_n=\lVert y_{n+1}-\hat y_{n+1}\rVert_{\mathrm{WRMS}}$ | weight $\mathrm{atol}+\mathrm{rtol}\max\{\lvert y_{n+1,i}\rvert,\lvert\hat y_{n+1,i}\rvert\}$ |
| atol, rtol, tol | $\mathrm{atol}$, $\mathrm{rtol}$ | tol when $\mathrm{atol}=\mathrm{rtol}$ |
| $\nu$ | $\nu$ | agrees; normalized so that a real stability interval of 2 means $\nu=1$ |
| $R(z)$, $z=\Delta t\lambda$ | $P(z)$, $z=h\lambda$ | explicit methods: stability polynomial |
| $E(z)$ | kept | embedded minus main stability polynomial |
| **$J(z)$** | kept | Jacobian of the controller recursion; **not** the registry Jacobian $J=\partial f/\partial y$ |
| **$\beta_i$** (Algorithms 1–2) | kept | 3S\* low-storage coefficients; **collide** with the PID exponents $\beta_1,\beta_2,\beta_3$ |
| $\gamma_{1,i}$, $\gamma_{2,i}$, $\gamma_{3,i}$, $\delta_i$, $S_j$ | kept | 3S\* coefficients and registers (Ketcheson 2010) |
| $\iota_r$ | kept | real stability interval; $\iota_r/s$ scaled by effective stages |
| $s$ in method names | kept | effective evaluations per step (stages minus one for FSAL) |
| $\sigma$ | kept | CFL normalization in (3.2); also the source term in (5.1) |

# Reference list

80 printed references, numbered [1]–[80], alphabetical by first author; the
supplement re-prints [37] under the same number. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` ranocha-2022. Same-key
collisions take suffixes in printed order (Ketcheson 2020 ×2, Parsani 2015 ×2,
Ranocha 2020 ×3, Söderlind 2006 ×2). Pre-publication citations (PETSc/TS arXiv 2018,
Almquist–Dunham, Buscariolo et al., Conde–Fekete–Shadid arXiv 2018,
Montijano–Rández–Ketcheson "in preparation") are separate entries. [4], [27] and [68]
are printed incomplete, and [38] prints year 2013 with a DOI containing
"camcos.2012.7.247". No printed duplicates and no unparseable items.

# Pages created or updated

Chunk 1 (2026-10-19). This source is cited on:

* [DifferentialEquations.jl](/software/differentialequations-jl.md)
* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md)
* [Optimal stability polynomials for explicit Runge–Kutta methods](/methods/optimal-stability-polynomial.md)
* [PETSc TS](/software/petsc-ts.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)

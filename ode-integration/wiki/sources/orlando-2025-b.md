---
type: Source
title: "Orlando et al. (2025) — A quantitative comparison of high-order asymptotic-preserving and asymptotically-accurate IMEX methods for the Euler equations with non-ideal gases"
description: "Compares a pressure-based IMEX Runge–Kutta scheme with fixed-point stage solves against the linearly implicit semi-implicit IMEX approach on low-Mach Euler flows with non-ideal gases, at orders two to four, for accuracy, cost and robustness, and extends the semi-implicit method to a general EOS."
resource: "doi:10.1016/j.cma.2025.118037"
source_kind: paper
authors: [Orlando G., Boscarino S., Russo G.]
year: 2025
venue: "Comput. Methods Appl. Mech. Engrg. 442:118037"
local_file: "/home/stefano/papers/mosaic/ode-integration/2025_Crossref_Computer_Methods_in_Applied_Mechanics_and_Engineering_Orlando_A_quantitative_comparison_of_high-order_asymptotic-preservin.pdf"
tags: [imex, asymptotic-preserving, implicit-stage-solvers, stiff, order-reduction, cfd]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

The paper compares two [IMEX Runge–Kutta](/methods/imex-runge-kutta.md) time discretizations of the non-dimensional compressible Euler equations in the low-Mach regime, on the same nodal DG spatial discretization (deal.II, matrix-free, quadrilaterals). Both remove the acoustic CFL restriction.

- **IMEX-DG** (from the authors' earlier work, including [Orlando & Bonaventura (2025)](/sources/orlando-2025.md)): continuity is explicit, and the pressure gradient and enthalpy flux are implicit with the DIRK companion. The resulting nonlinear Helmholtz-type pressure equation is solved stage-wise by a Picard (fixed-point) iteration with lagged enthalpy.
- **SI-IMEX-DG**: the [semi-implicit IMEX-RK](/methods/semi-implicit-imex-runge-kutta.md) framework of Boscarino, Filbet & Russo. The right-hand side is $\mathcal H(y_{\mathrm E},y_{\mathrm I})$, the explicit argument is advanced with $A^{\mathrm E}$ and the implicit one with $A^{\mathrm I}$, and each stage needs one linear pressure equation.

The new elements are a cost, accuracy and robustness comparison at orders two, three and four, with type I, type II and type ARS implicit companions. The paper also linearizes the internal-energy–pressure relation, $(\rho e)_{\mathrm I}\approx[(\rho e)_{\mathrm E}/p_{\mathrm E}]\,p_{\mathrm I}$, which removes the nonlinear pressure equation from SI-IMEX for a general EOS. Finally it derives a formal low-Mach limit for a general EOS that is incompressible only when $d\bar p/dt=0$.

Both methods are [asymptotic preserving](/definitions/asymptotic-preserving-scheme.md) and asymptotically accurate "in the range of low Mach accuracy established by the spatial discretization". Accuracy degrades at $\varepsilon=10^{-4}$, which the authors attribute mainly to DG on quadrilaterals, with stiff [order reduction](/definitions/order-reduction.md) as a possible contributor. SI-IMEX is cheaper at moderate Mach, but the gap shrinks to about 5% at $\varepsilon=10^{-3}$, where one Picard iteration suffices (see [implicit-stage solvers](/methods/implicit-stage-solvers.md)). Type I schemes are more robust than type II for SI-IMEX at low Mach. IMEX is more robust with time-dependent Dirichlet data, which make the system non-autonomous and fall outside SI-IMEX theory. The EOS linearization saves about 70% CPU. The type II [L-stability](/properties/a-stability.md) condition is recalled. The tests are the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), a traveling [isentropic vortex](/benchmarks/isentropic-vortex.md), a Sod tube with Peng–Robinson EOS, an open tube and a low-Mach Kelvin–Helmholtz instability.

# Version read

arXiv:2501.12733v5 [math.NA], 22 Oct 2025, Elsevier preprint template ("Preprint submitted to Elsevier"). This is not the CMAME version of record, and v5 postdates the July 2025 publication. The file has 39 PDF pages: an unnumbered Highlights page and 38 numbered pages, so PDF page = printed page + 1. Title and authors match Crossref, and the DOI is not printed. Equation, table and reference numbers cited here are those of arXiv v5. It is a different, later paper than [Orlando & Bonaventura (2025)](/sources/orlando-2025.md) (JCP 529:113889), which it cites as [74].

# Key claims

Notation: $h$ is the step and $\varepsilon$ the reference Mach number (source $M$). The explicit and implicit tableaux are $(A^{\mathrm E},b^{\mathrm E},c^{\mathrm E})$ and $(A^{\mathrm I},b^{\mathrm I},c^{\mathrm I})$; the source writes them $(\tilde A,\tilde b,\tilde c)$ and $(A,b,c)$. The SI-IMEX state copies are $y_{\mathrm E}$, $y_{\mathrm I}$ (source $\mathbf U_E$, $\mathbf U_I$).

1. For stiffly accurate type II IMEX-RK schemes, A-stability plus [stiff accuracy](/properties/stiff-accuracy.md) of the implicit part does not by itself give L-stability, because $A^{\mathrm I}$ is singular. The supplementary condition $e_s^\top\hat A^{-1}a=\sum_{m=2}^s\hat w_{sm}a^{\mathrm I}_{m1}=0$ is required (Eq. 32, citing [16]). All implicit companions in Appendix A are L-stable ("one can easily verify"). (§3.1) **Stated**
2. The low-Mach limit for a general EOS is $\nabla\cdot\bar u=-\frac{1}{\bar\rho\bar c^2}\frac{d\bar p}{dt}$. Incompressibility $\nabla\cdot\bar u=0$ holds iff $d\bar p/dt=0$, which follows under periodic or free-slip boundaries. A time-dependent Dirichlet outflow pressure yields a non-solenoidal limit that depends on the EOS. (§2.2, Eqs. 23–25) **Derived**
3. For the ideal gas the limit compressibility is spatially uniform, $\nabla\cdot\bar u=-\frac1\gamma\frac{d\log\bar p}{dt}$ (Eq. 27). For the stiffened gas $\nabla\cdot\bar u=-\frac{1}{\gamma(\bar p+\pi_\infty)}\frac{d\bar p}{dt}$ (Eq. 87). It is not uniform for a general EOS. **Derived**
4. With $b^{\mathrm E}=b^{\mathrm I}$ in the SI-IMEX-RK method, the explicit and implicit copies coincide at step ends ($y_{\mathrm E,n}=y_{\mathrm I,n}$ for all $n$), so the doubling of unknowns in the partitioned system (Eq. 39) is only apparent. (§3.3) **Stated** (from [13])
5. The SI-IMEX approach gives a linear pressure equation per stage for the ideal and stiffened gases. For a general (e.g. cubic) EOS the proposed approximation $\frac{(\rho e)_{\mathrm I}}{p_{\mathrm I}}p_{\mathrm I}\approx\frac{(\rho e)_{\mathrm E}}{p_{\mathrm E}}p_{\mathrm I}$ (Eq. 53) keeps it linear and reduces exactly to the ideal-gas system. (§3.4, Eq. 54) **Derived**
6. IMEX-DG uses a Picard iteration with lagged enthalpy instead of Newton, because the fully implicit enthalpy makes the system "strongly nonlinear and difficult to control"; two or three iterations suffice. (§3.2, citing [26, 36]) **Stated**/**Shown** (Tables 16–17)
7. Taylor–Green vortex, IMEX-DG with the type II IMEX-RK(3,3,3), $r=2$, $N_{el}=60$: $\delta p$ scales as $O(\varepsilon^2)$ down to $\varepsilon=10^{-4}$ ($L^2$: $1.57\times10^{-2}$, $1.57\times10^{-4}$, $1.57\times10^{-6}$, $1.62\times10^{-8}$). $\delta\rho$ scales as $O(\varepsilon^2)$ down to $10^{-3}$, with rate 1.1 at $10^{-4}$. $\nabla\cdot u$ stagnates at $1.82\times10^{-3}$ (interpolation error of the initial datum in nodal DG). (§4.1, Table 1, Fig. 2) **Shown**
8. Taylor–Green, SI-IMEX: with the type II (3,3,3) scheme it is stable only down to $\varepsilon=10^{-3}$, with $\delta\rho$ rate 0.6 at $10^{-3}$ (Table 2). With the type I (4,3,3) scheme it is stable at $10^{-4}$, but $\delta\rho$ stagnates at $1.68\times10^{-6}$ (Table 4). IMEX with type I improves $\delta\rho$ at $10^{-4}$ to $4.66\times10^{-9}$ (rate 1.5, Table 3). Conclusion: type I schemes have superior stability at low Mach (consistent with [15]), and low-Mach accuracy depends on the time-discretization strategy and the scheme. **Shown**
9. Traveling vortex, IMEX-RK(2,2,2), $r=1$: IMEX and SI-IMEX give the same accuracy, and the rate degrades to 1.2 at $\varepsilon=10^{-2}$ (Tables 5–6). Degree $r=2$ for velocity and $r=1$ elsewhere restores second order (rate 2.4 at the finest level, Table 7). **Shown**
10. Traveling vortex, third-order schemes, $r=2$, $C_u\approx0.094$, $C\approx0.07/\varepsilon$: third order up to $\varepsilon=10^{-3}$ for all combinations except SI-IMEX with type II at $10^{-3}$ (rates 2.6, 0.7; Table 9). At $10^{-4}$ SI-IMEX is stable only with type I, and the error saturates for all combinations. (Tables 8–11) **Shown**
11. The IMEX method tolerates doubling the step ($C_u\approx0.19$) at the same accuracy "because of the superior stability provided by the fixed point loop" [36]. Even so, SI-IMEX (especially with type II) is generally cheaper in wall-clock time; at $\varepsilon=10^{-3}$ the gain shrinks to about 5%. (§4.2, Fig. 6) **Shown**
12. Fourth order, $r=3$, $C_u\approx0.05$, $C\approx0.035/\varepsilon$: SI-IMEX needs $C_u\approx0.025$ for stability at $\varepsilon\le10^{-2}$. ARS(5,5,4) gives the expected rates up to $10^{-3}$ (Tables 12–13), except IMEX at $10^{-2}$ (finest rate 1.0, Table 12). With the type II IMEX-RK(6,6,4), IMEX keeps its accuracy to $10^{-3}$ (Table 14), while SI-IMEX has "severe issues" from $10^{-3}$ (Table 15 stops at $10^{-2}$). **Shown**
13. The saturation and order reduction at $\varepsilon=10^{-4}$ are attributed mainly to the low-Mach inaccuracy of DG on quadrilaterals. Round-off (quadruple precision is needed at very low Mach [20]) and stiff order reduction [88] are named as further possible causes. (§4.2) **Stated**
14. Fixed-point loop: at $\varepsilon=10^{-1}$ the iteration count grows as the tolerance tightens ($10^{-4},10^{-6},10^{-10}$ give 1, 3, 5 iterations, errors $3.35\times10^{-4}$, $3.17\times10^{-4}$, $3.17\times10^{-4}$). At $\varepsilon=10^{-4}$ one iteration suffices at any tolerance. Hence IMEX and SI-IMEX have similar cost at low Mach. (Table 16) **Shown**
15. The Picard iteration converges at first order: experimental contraction rates after 3 iterations are about 0.01–0.08, and the EOC tends to about 1 (1.07 at the 1st step, 0.84 at the 200th). (Table 17, Eqs. 79–80) **Shown**
16. Sod tube with Peng–Robinson EOS, $r=0$, $N_{el}=500$, $h\approx1.33\times10^{-3}$, $C\approx1.23$, $C_u\approx0.47$: IMEX and SI-IMEX agree excellently with each other and well with an SSPRK3 reference on 32000 elements. (§4.3, Fig. 7) **Shown**
17. Open tube ($\varepsilon=10^{-4}$), IMEX-RK(2,2,2), $r=1$: IMEX is stable at $h=3.735\times10^{-3}$ ($C\approx310$, $C_u\approx0.13$) and matches the leading-order solution. SI-IMEX needs $h=1.8675\times10^{-3}$ ($C\approx155$) and then saves about 37% CPU at fixed $h$. (§4.4, Fig. 8) **Shown**
18. Open tube, third order, $r=2$: IMEX is stable at $h=1.8675\times10^{-3}$ ($C\approx292$) with both type I and type II. SI-IMEX needs $h=4.66875\times10^{-4}$, and is then stable only with type II, not type I. The failure is attributed to the time-dependent Dirichlet data, which make the system non-autonomous (outside SI-IMEX theory, which assumes periodic or no-flux boundaries [6, 15, 50]), and to $c^{\mathrm I}\ne c^{\mathrm E}$ for type I, so that $y_{\mathrm E}$ and $y_{\mathrm I}$ live at different times. (§4.4) **Shown** (cause: **Stated**)
19. With large density and pressure variations and time-dependent boundary data, IMEX is "globally more robust and allows for sizeable larger time steps". (§4.4) **Shown**
20. Open tube with a stiffened gas ($\gamma=4.4$, $\pi_\infty=680$, $q_\infty=0$), type II third order, $h=2.334375\times10^{-4}$, $C\approx1530$: IMEX and SI-IMEX agree. The leading-order solution depends on the EOS, with $\lvert\nabla\cdot\bar u\rvert\lesssim2.5\times10^{-4}$. (Eq. 89, Fig. 10) **Shown**/**Derived**
21. Low-Mach Kelvin–Helmholtz instability (ideal gas): IMEX-RK(2,2,2), $r=1$, $120^2$ elements, $h=2\times10^{-3}$, $C\approx15$, $C_u\approx0.10$ agrees with [90] and between IMEX and SI-IMEX. Third order with $r=2$ on $80^2$ elements (same DOFs) resolves finer details. (§4.5, Figs. 11–12) **Shown**
22. Kelvin–Helmholtz with the general cubic EOS ($a(T)=1/(2\sqrt T)$, $b=5\times10^{-3}$, nitrogen $c_v\approx742.0$, $R_g\approx296.8$): the linearized SI-IMEX (Eq. 54) shows no difference from SI-IMEX with the nonlinear pressure equation, at about **70% CPU saving**. (Fig. 13) **Shown**
23. With $p(\mathbf x,0)=10^5/\gamma$ ($T_{\max}\approx320$), SI-IMEX needs $h=5\times10^{-4}$. With the full Peng–Robinson $a(T)$, $b$ (Eq. 93) and the NIST $e^\#(T)$ (Eq. 94), IMEX is stable while SI-IMEX shows "severe issues" in the development of the instability. (§4.5) **Shown**
24. A Schur-complement (velocity elimination) formulation avoids discretizing a second-order elliptic operator with DG penalty terms (SIPG), at the cost of a non-symmetric system $\mathbf C\mathbf A^{-1}\mathbf B$, solved by Jacobi-preconditioned GMRES. The SPD systems are solved by CG with geometric multigrid. (§3.5) **Stated**
25. Conclusion: both methods are AP and AA "in the range of low Mach accuracy established by the spatial discretization"; SI-IMEX gives a sizeable CPU saving at the same accuracy, particularly at moderate Mach; and type I schemes give superior stability at low Mach. (§5) **Shown**

*(Compiler checks, not in the sources.)* As printed, the explicit companion of the type-I third-order pair of Table 20 fails the third-order condition $b^{\mathrm E\top}A^{\mathrm E}c^{\mathrm E}=\tfrac16$: the left side is $0.19885$, while every other condition of order $\le3$, coupling conditions included, holds; its fourth explicit row differs from the one printed by [Southworth et al. (2024)](/sources/southworth-2024.md) for I-IMEX(3,4,3), with which the pair is third order (see the [semi-implicit IMEX](/methods/semi-implicit-imex-runge-kutta.md) page). The paper nevertheless observes third order with this pair (Tables 8–11). Claim 25's ranking of type I over type II is test-dependent: in the open tube (claim 18) only type II works for SI-IMEX. The $(s,\sigma,p)$ names do not count evaluations as defined. IMEX-RK(3,3,3) has four explicit stages with $b^{\mathrm E}_4\ne0$, and IMEX-RK(6,6,4) has seven stages. Table 21 has the same diagonal $\gamma=\frac{1767732205903}{4055673282236}$ as the third-order Kennedy–Carpenter scheme of [Orlando et al. (2025)](/sources/orlando-2025.md). The implicit part of ARS(5,5,4) is a five-stage, stiffly accurate SDIRK of order 4 with $\gamma=\tfrac14$ and $R(\infty)=0$, padded with an explicit first stage. AA is shown only up to $\varepsilon=10^{-3}$.

# Printed slips

- Eq. (31): "$a_{sl}=b_l,\quad i=1,\dots,s$"; the index should be $l$.
- §3.4 and §4 (p. 15) cite "(37)" for the fixed-point loop ("equations (37) and (50) constitute a linear system for $\xi^{(\tilde k+1)}$", "(51) reduces to (37)"). Eq. (37) is $\partial_t\mathbf U=\mathbf H(\mathbf U,\mathbf U)$, and the fixed-point equation of §3.2 is unnumbered.
- Table 4 is printed before Table 3 (p. 17). The headers of Table 10 ("error 𝐮") and Table 13 ("L2 rate 𝐮") miss the $\delta$.
- Fig. 3 caption plots "$p-(1-M^2)$" while Fig. 4 has "$p-(1+M^2)$"; by Eq. (77) the background is $1+M^2$.
- p. 26: "IMER-RK(2,2,2)".
- Fig. 9 caption gives $h=2.334375\times10^{-4}$ and $1.245\times10^{-3}$, while the text (p. 27) and the legends give $4.66875\times10^{-4}$ and $1.8675\times10^{-3}$.
- Eq. (88): the denominator is printed $4(\gamma+\pi_\infty)(1+\frac14\sin3t)$. From Eq. (87) with $\bar p=1+\frac14\sin3t$ it should be $4\gamma(1+\frac14\sin3t+\pi_\infty)$; the bound (89) is consistent with (87), not with (88).
- §4.5: "$N_{el}=120\times120=14400$ elements along each direction" gives a total count, not a count per direction.
- Fig. 13 caption: "Peng-Robinson EOS (4)", where Eq. (4) is the ideal-gas law and the test uses the general cubic EOS. §4.3: "Peng-Robinson EOS (9)", where Eq. (9) is the constant-$c_v$ internal-energy relation.
- Table 20 is attributed to [13] in the text ("method of type I [13]") but to [15] in the caption.
- References: [90] "Zampa, E., Dumbser, E., 2025" (M. Dumbser); [3] author printed "J-P., P." (Pelteret J.-P.); [68] "Ocher, S." (Osher).

# Notation map

| Orlando, Boscarino & Russo | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$, $t^n$ | $h$, $t_n$ | |
| $M$ | $\varepsilon$ | reference Mach number $u_0/\sqrt{p_0/\rho_0}$; **also the ODE dimension in Eq. (28) (registry $d$); the registry reserves $M$ for the mass matrix** |
| $(\tilde A,\tilde b,\tilde c)$ | $(A^{\mathrm E},b^{\mathrm E},c^{\mathrm E})$ | **tilde marks the explicit tableau**, opposite to [Orlando & Bonaventura (2025)](/sources/orlando-2025.md) |
| $(A,b,c)$ | $(A^{\mathrm I},b^{\mathrm I},c^{\mathrm I})$ | implicit (DIRK) tableau |
| $\mathbf a$, $\hat{\mathcal A}$ | $a$, $\hat A$ | first column below row 1 and invertible trailing block of a type II $A^{\mathrm I}$ |
| $\hat w_{lm}$ | kept | entries of $\hat A^{-1}$ |
| $\mathbf f_E$, $\mathbf f_I$ | $f^{\mathrm E}$, $f^{\mathrm I}$ | non-autonomous form |
| $\mathbf v^{(l)}$, $\mathbf U^{(l)}$ | $Y_i$ | stage values |
| $\mathbf H(\mathbf U_E,\mathbf U_I)$ | $\mathcal H(y_{\mathrm E},y_{\mathrm I})$ | SI-IMEX partitioned right-hand side (page-local subscripts) |
| $R(z)$ | $R(z)$ | stability function of the implicit part; $R(\infty)=0$ for L-stability |
| $(s,\sigma,p)$ | kept | implicit evaluations, explicit evaluations, order (see the compiler checks) |
| $\xi^{(\tilde k)}$, $\tilde k$, $\eta$, $L$ | kept | Picard pressure iterate, iteration index, tolerance, maximum iterations; **$\eta$ is not the registry entropy**, and $L$ is also the tube length |
| $\gamma$ | kept (ratio of specific heats) | **also the diagonal $247/2000$ of Table 23** |
| $c$ | kept (sound speed) | **collides with the abscissae** |
| $b$, $a(T)$, $r_1,r_2$ | kept | cubic-EOS co-volume, attraction, constants; **$b$ collides with the weights** |
| $r$, $N_{el}$ | kept | DG degree, elements per direction |
| $C$, $C_u$ | kept | acoustic and advective Courant numbers (Eq. 73), with factors $r$ and $\sqrt d$ |
| $\bar\cdot,\cdot',\cdot''$ | kept | orders $\varepsilon^0,\varepsilon^1,\varepsilon^2$ of the Mach expansion |

# Reference list

91 printed references, numbered [1]–[91], in alphabetical order (Elsevier numbered style with author–year entries). The list is merged complete into the [bibliography](/bibliography.md) with `citedby` orlando-2025-b. [21] is Boscheri & Pareschi, JCP 434:110206, the ingested source [Boscheri & Pareschi (2021)](/sources/boscheri-2021.md), keyed `boscheri-2021`. [20] is a different 2021 paper by Boscheri et al. (JCP 424:109866), keyed `boscheri-2021-c`; the two must not be conflated. [74] is the ingested source [Orlando & Bonaventura (2025)](/sources/orlando-2025.md). The only printed DOI is that of [14]. [88] prints "Wanner, G., Hairer, E., 1996" in reversed author order and is merged into `hairer-1996`; [68] prints the author "Ocher, S." and is merged into `osher-1982`; [54] (Karniadakis & Sherwin, printed 2005) is merged into `karniadakis-2013`. [11], [19], [37], [49] and [59] take suffixed keys (`bassi-1997-b`, `boscheri-2020-b`, `dumbser-2016-c`, `harten-1983-b`, `kronbichler-2012-b`) because the bibliography already held other works under the plain keys. [3] and [90] carry garbled author strings, and [48], [64] and [80] lack a publisher or volume. There are no printed duplicates.

# Pages created or updated

Chunk 3 (2026-10-19). This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [Asymptotic-preserving scheme](/definitions/asymptotic-preserving-scheme.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Kennedy–Carpenter additive Runge–Kutta methods (ARK3, ARK4, ARK5)](/methods/kennedy-carpenter-ark-methods.md)
* [Order reduction](/definitions/order-reduction.md)
* [Semi-implicit and linearly implicit IMEX Runge–Kutta methods](/methods/semi-implicit-imex-runge-kutta.md)
* [Sod shock tube](/benchmarks/sod-shock-tube.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Stiff accuracy](/properties/stiff-accuracy.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)

---
type: Source
title: "Orlando & Bonaventura (2025) — Asymptotic-preserving IMEX schemes for the Euler equations of non-ideal gases"
description: "Derives low-Mach limits of the Euler equations for a general equation of state and proves formally that IMEX Runge–Kutta pressure-based schemes are asymptotic preserving: strongly for type I and type ARS methods, weakly (well-prepared data) for type II, with DG tests up to acoustic Courant 19300."
resource: "doi:10.1016/j.jcp.2025.113889"
source_kind: paper
authors: [Orlando G., Bonaventura L.]
year: 2025
venue: "J. Comput. Phys. 529:113889"
local_file: "/home/stefano/papers/mosaic/ode-integration/2025_Crossref_Journal_of_Computational_Physics_Orlando_Asymptotic-preserving_IMEX_schemes_for_the_Euler_equations_o.pdf"
tags: [imex, asymptotic-preserving, stiff, stability, order-reduction, cfd]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

The paper studies a general class of [IMEX Runge–Kutta](/methods/imex-runge-kutta.md) time discretizations of the compressible Euler equations in the low-Mach regime, for a general equation of state (ideal gas, stiffened gas, general cubic such as van der Waals and Peng–Robinson). The scheme follows the Casulli–Greenspan / Dumbser–Casulli pressure-based approach. Continuity, momentum advection and the kinetic-energy flux are explicit. The pressure gradient and the enthalpy flux are implicit, and their coupling gives a nonlinear Helmholtz equation for the pressure, solved by fixed-point iteration.

Section 2 derives formal low-Mach limits. With one length scale, the leading pressure is spatially constant and $\nabla\cdot\bar u=-\frac{1}{\bar\rho c^2(\bar p,\bar\rho)}\frac{d\bar p}{dt}$. With two length scales, the pressure perturbation obeys a wave equation for ideal and stiffened gases. The authors present the two-scale extension to a general EOS as new.

Section 3 classifies the methods by their implicit tableau: type I ($A^{\mathrm I}$ invertible), type II (first column structure with an invertible trailing block) and type ARS. Theorems 3.4 and 3.7 show formally that the IMEX stage equations are a consistent discretization of the single-scale and two-scale limits. The paper thus defines when the scheme is [asymptotic preserving](/definitions/asymptotic-preserving-scheme.md): type I and ARS methods are AP for general data ("strongly AP"), and type II methods only for well-prepared pressure ("weakly AP"). Asymptotic accuracy is tied to [L-stability](/properties/a-stability.md). For [stiffly accurate](/properties/stiff-accuracy.md) type II methods this needs the extra condition $R(\infty)=0$ of Boscarino and Russo.

Section 5 tests a DG discretization (deal.II) with a Kennedy–Carpenter third-order additive Runge–Kutta scheme (Table 1), whose implicit part is an [ESDIRK](/methods/diagonally-implicit-runge-kutta.md), and a fourth-order type-ARS scheme of Calvo, de Frutos and Novo. The tests are the [isentropic vortex](/benchmarks/isentropic-vortex.md) (convergence and Mach scaling), colliding acoustic pulses, density layering, an open tube with time-dependent pressure, the [Gresho vortex](/benchmarks/gresho-vortex.md) and baroclinic vorticity generation, at acoustic Courant numbers up to about 19300. The fourth-order scheme loses the $O(\varepsilon^2)$ density scaling from $\varepsilon=10^{-4}$, which the authors attribute partly to [order reduction](/definitions/order-reduction.md).

# Version read

HAL preprint hal-04458836v2 ("Preprint submitted on 19 Nov 2024 (v2), last revised 22 Oct 2025 (v5)"). This is a pre-publication version, not the JCP version of record. It has 47 PDF pages: a HAL cover and 46 numbered pages (text pp. 3–39, Appendix A pp. 39–40, references pp. 40–46). Title and authors match Crossref, and the DOI is not printed. Section, equation, table and reference numbers cited here are those of HAL v2. It is a different paper from [Orlando et al. (2025)](/sources/orlando-2025-b.md), which cites it and builds on it.

# Key claims

Notation: $h$ is the step and $\varepsilon$ the reference Mach number (source $M$, $M^2=RU^2/P$). The explicit and implicit tableaux are $(A^{\mathrm E},b^{\mathrm E},c^{\mathrm E})$ and $(A^{\mathrm I},b^{\mathrm I},c^{\mathrm I})$; the source writes them $(A,b,c)$ and $(\tilde A,\tilde b,\tilde c)$. Overbars and primes are the orders $\varepsilon^0,\varepsilon^1,\varepsilon^2$ of the Mach expansion.

1. For the single-length-scale low-Mach limit with a general EOS, the leading pressure is spatially constant ($\nabla\bar p=\nabla p'=0$), $p''$ acts as the incompressible dynamic pressure, and $\nabla\cdot\bar u=-\frac{1}{\bar\rho c^2(\bar p,\bar\rho)}\frac{d\bar p}{dt}$. The derivation uses no Hilbert expansion of $e$; $e(\bar p,\bar\rho)$ is evaluated from the EOS. (§2.2, Eqs. 22–32) **Derived**
2. Under periodic or free-slip boundaries $d\bar p/dt=0$, and every EOS gives the incompressible Euler limit. A time-dependent $\bar p$ imposed by Dirichlet data gives $\nabla\cdot\bar u\ne0$, which depends on the EOS. For an ideal gas $\nabla\cdot\bar u=-\frac1\gamma\frac{d\log\bar p}{dt}$ is uniform in space; for a general EOS it is not. (§2.2, Eqs. 30, 33; verified in §5.4) **Derived**/**Shown**
3. In the two-length-scale analysis ($\xi=\varepsilon x$), restricted to variations on the acoustic scale, $\partial_t\bar\rho=0$, $\bar p$ is constant and $p'$ satisfies the wave equation $\partial_t^2p'=\nabla_\xi\cdot(c^2(\bar p,\bar\rho)\nabla_\xi p')$. This holds for the ideal gas (Eq. 45, recovering Klein [57]) and for the stiffened gas (Eqs. 46–47); supplementary terms appear for the general cubic EOS. (§2.3) **Derived**
4. The authors present the two-length-scale extension to a general EOS as new; the single-scale general-EOS limit was already in Dellacherie [28]. (§1, §2.2) **Stated**
5. Definition 3.1: an IMEX-RK method is type I if $A^{\mathrm I}$ is invertible, and type II if $A^{\mathrm I}=\begin{pmatrix}0&0\\ a&\hat A\end{pmatrix}$ with $\hat A\in\mathbb R^{(s-1)\times(s-1)}$ invertible. It is type ARS if in addition $a=0$ and $b^{\mathrm E}_1=0$. (§3, Def. 3.1, citing [3, 9, 54, 71]) **Stated** (definition recalled)
6. Theorem 3.4: assume the stage-wise Hilbert expansion (Assumption 3.2) and, for type II non-ARS schemes, a well-prepared initial pressure $\nabla\bar p^0=\nabla p'^{,0}=0$ (Assumption 3.3). Then the IMEX-RK stage system (Eq. 53) is a consistent discretization of the single-scale limit (Eqs. 31–32) as $\varepsilon\to0$, with local stage and update errors $O(h^2)$. (Eqs. 55–67) **Proved** (formal; rests on the expansion assumption)
7. Theorem 3.7: under Assumptions 3.5 (two-scale stage expansion) and 3.6 (well-prepared data for type II non-ARS), the stage system (Eq. 53) is AP for the two-scale limit (Eq. 42). The consistency of the energy equation and of the update stage is only said to be "analogous". (§3.2, Eqs. 70–75) **Proved** (formal, partly sketched)
8. Because momentum and energy are coupled implicitly, the stability condition depends neither on $\varepsilon$ nor on the sound speed; only a "mild CFL-type restriction based on the flow velocity" is needed. (§3.1, citing [21, 32, 78]) **Stated**
9. Type I and type ARS schemes are **strongly AP** (AP for general initial data). Type II non-ARS schemes are **weakly AP**, since they need a well-prepared initial pressure. A divergence-free initial velocity is not needed to recover the incompressible limit, unlike the schemes of Noelle et al. [65] (later corrected in [7]) and Thomann et al. [81]. (§3.1) **Stated**/**Derived**
10. AP does not imply asymptotic accuracy (the order is kept as $\varepsilon\to0$). "Since the seminal paper [71], it is quite established that L-stability is necessary to guarantee asymptotic accuracy." (§3.1) **Stated**
11. An A-stable, stiffly accurate method is L-stable [85]. For type II this fails because $A^{\mathrm I}$ is singular, and a stiffly accurate type II method needs the extra condition $R(\infty)=\sum_{m=2}^s\hat w_{sm}a^{\mathrm I}_{m1}=0$, with $\hat w_{lm}$ the entries of $\hat A^{-1}$ (Eq. 68, citing Boscarino–Russo [10]). Stiffly accurate type ARS schemes are L-stable. (§3.1) **Stated**
12. Implicit methods of order higher than one cannot be unconditionally TVD for hyperbolic problems [39], and the same holds for IMEX methods [12, 31]. The paper does not address this, and its schemes may not be $L^\infty$-stable. (§3) **Stated**
13. Both implicit companions used (Tables 1, 2) are stiffly accurate. The Table 2 implicit method is type ARS and hence L-stable, and Eq. (68) gives $R(\infty)=0$ for the Table 1 implicit method, so it is also L-stable. (§5) **Stated** (compiler-checked for Table 1, with the minus sign restored on $a^{\mathrm I}_{32}$; see the slips: $\sum\hat w_{sm}a^{\mathrm I}_{m1}\approx2\times10^{-16}$)
14. Isentropic vortex convergence at $\varepsilon=10^{-3}$, acoustic Courant number $C\approx3.5$: the Table 1 scheme with DG degree $r=2$ gives $L^2$ rates 3.2, 3.0, 3.0 for $N_{el}=15\to120$ (errors $4.70\times10^{-2}\to8.07\times10^{-5}$). The Table 2 scheme with $r=3$ gives 3.9, 3.9, 3.5 for $N_{el}=10\to80$ (errors $3.27\times10^{-2}\to1.32\times10^{-5}$). "The expected convergence rates are achieved." (§5.1, Table 3) **Shown**
15. Mach scaling for the isentropic vortex (Table 1 scheme, $r=2$, $N_{el}=120$): $\lVert\nabla\rho\rVert$ scales as $O(\varepsilon^2)$ (rate 2.0) down to $\varepsilon=10^{-5}$ (rate 1.9), then degrades to rate 1.1 at $10^{-6}$. $\lVert\nabla\cdot u\rVert$ scales as $O(\varepsilon)$ throughout (rate 1.0). Degree $r+1=3$ for velocity gives rate 1.2 at $10^{-6}$. (Table 4) **Shown**
16. With the fourth-order Table 2 scheme ($r=3$, $N_{el}=80$), the density fluctuations scale only as $O(\varepsilon)$ from $\varepsilon=10^{-4}$ (rates 1.4, 1.0, 1.0). The authors attribute this partly to the "well-known order reduction phenomenon experienced for very stiff problems using high-order time discretization methods [55, 85]". The third-order scheme with $r=3$ keeps the correct scaling to $10^{-5}$. Velocity degree $r+1=4$ restores rate 2.0 to $10^{-5}$, with rate 0.9 at $10^{-6}$. (§5.1, Table 5) **Shown** (the order-reduction attribution is **Stated**)
17. The $O(\varepsilon)$ scaling of $\nabla\cdot u$, instead of the quadratic rate the continuous expansion predicts, is attributed to interpolating the initial datum into the non-divergence-free DG space; Zampa–Dumbser [88] obtain quadratic rates with compatible finite elements. (§5.1) **Stated**
18. Colliding acoustic pulses ($\varepsilon=1/11$): IMEX steps $h=1.63\times10^{-2}$ ($C_u\approx0.1$, $C\approx0.56$), $3.26\times10^{-2}$ ($C_u\approx0.2$, $C\approx1.16$) and $8.15\times10^{-2}$ ($C_u\approx0.5$, $C\approx2.9$) agree with an SSP-RK3 reference ($N_{el}=880$, $h=2.54687\times10^{-4}$, $C\approx0.14$). Larger steps hit the stability limit of the explicit part [26]. (§5.2, Figs. 1–2) **Shown**
19. With the stiffened gas at $\pi_\infty=6.8\times10^3$ and the same step, $C\approx80$: the IMEX scheme is stable but the pressure pulses are "completely damped". At $h=2.0375\times10^{-4}$ (80 times smaller, $C\approx1$) the pulses are resolved with no spurious oscillations. "If a sufficient low time step is employed, the method seems naturally to be able to deal with low Mach acoustics." (§5.2, Fig. 4) **Shown**
20. Density layering at $\varepsilon=10^{-4}$ ($C\approx1400$): the IMEX scheme reaches the incompressible limit solution (Eqs. 101–102) from ill-prepared (not divergence-free) initial velocity. An explicit SSP-RK3 run with a step about 6666 times smaller preserves the layer shape but does not reach the limit. At $\varepsilon=0.02$ the IMEX step is about 33 times (ideal gas) or 66 times (stiffened gas) the explicit step. (§5.3, Fig. 6) **Shown**
21. Open tube, $\varepsilon=10^{-4}$, $h=9.3375\times10^{-4}$: ideal gas $C_u\approx0.07$, $C\approx155$; stiffened gas ($\pi_\infty=6.8\times10^3$) $C_u\approx0.015$, $C\approx19300$, where "an explicit scheme would require a time step around 65000 times smaller"; Peng–Robinson ($a=1$, $b=0.15$) $C\approx150$. The numerical density and velocity match the leading-order limit: linear velocity for the ideal and stiffened gases, nonlinear for Peng–Robinson. (§5.4, Figs. 9–11) **Shown**
22. Gresho vortex, $80\times80$ elements, $r=2$, $h=2\times10^{-3}$ ($C_u\approx0.32$; $C\approx320$ at $\varepsilon=10^{-3}$ and $3200$ at $10^{-4}$): the relative kinetic energy after 1, 2 and 3 rotations is 0.999981, 0.999977, 0.999968 (ideal gas, both $\varepsilon$); 0.999984, 0.999981, 0.999977 (stiffened-gas water, $\varepsilon=10^{-4}$); and 0.999981, 0.999977, 0.999968 (Peng–Robinson). The authors contrast this with a loss of about 1.5% after one rotation in [1, 81]. (§5.5, Tables 6–8) **Shown**
23. Baroclinic vorticity generation, $\varepsilon=0.05$, $200\times40$ elements, $r=2$, $h=4\times10^{-3}$ ($C_u\approx0.27$, $C\approx2.5$ ideal gas; $C\approx3.5$, $C_u\approx0.23$ stiffened gas): a Kelvin–Helmholtz instability develops along the density interface, and its development depends on the EOS. (§5.6, Figs. 15–16) **Shown**
24. Appendix A: in 1D the implicit subsystem has eigenvalues $\frac u2\pm\sqrt{\frac{c^2}{\varepsilon^2}+\frac{u^2}4}$ and 0 and carries all the acoustics. The explicit subsystem has eigenvalues $0,u,u$; it is pressureless gas dynamics, only weakly hyperbolic (the Jacobian is not diagonalizable), so delta-shocks and vacuum can occur. For smooth solutions it reduces to Burgers' equation plus a transport equation for $\rho$. (App. A, Eqs. 124–127) **Derived**
25. No operator splitting, flux splitting or relaxation is used, unlike [1, 22, 23, 57, 65]. (§6) **Stated**
26. The IMEX-DG method is accurate down to $\varepsilon=10^{-4}$–$10^{-5}$ on quadrilaterals, below typical Mach numbers of water flows, despite the known $O(\varepsilon)$ pressure-error issue of upwind fluxes on quadrilateral and Cartesian meshes (Guillard–Viozat [42], Jung–Perrier [53]). (§5.1) **Shown**/**Stated**

*(Compiler checks, not in the sources.)* The Table 1 scheme, attributed by the paper to Kennedy & Carpenter, has diagonal $\gamma=\frac{1767732205903}{4055673282236}\approx0.4358665215$, $c_2=2\gamma$, first implicit column nonzero. It is therefore type II non-ARS and by §3.1 only weakly AP. Yet the colliding-pulses and density-layering tests run it on pressure data with $\nabla p'\ne0$, and the paper does not comment on this. The implicit part of the Table 2 scheme is a five-stage, stiffly accurate SDIRK of order 4 with $\gamma=\tfrac14$ and $R(\infty)=0$, padded with an explicit first stage. The AP proofs assume stage-wise Hilbert expansions, which the paper says "can be justified only for smooth functions". The blanket claim 10 frames L-stability as necessary for asymptotic accuracy; other pages of this bundle state the requirement as global stiff accuracy for specific relaxation problems.

# Printed slips

- **Table 1, implicit row 3:** $a^{\mathrm I}_{32}$ is printed $\frac{640167445237}{6845629431997}$ without a minus sign. The row then sums to 0.78703, not $c_3=\tfrac35$, and $R(\infty)\approx0.957$ instead of 0. With the minus sign the row sums to 0.60000 and $R(\infty)\approx0$ (checked visually on PDF p. 23 and numerically).
- §5.1: "In Table 1 we report results for the case of polynomial degree r = 2 …" refers to the convergence results in Table 3.
- Eq. (20) prints "$bar\mathbf u(\mathbf x,t)$", an unrendered macro.
- §3 after Eq. (50): "DIRK method, namely $\tilde a_{lm}=0$ for $l>m$"; $l<m$ is meant.
- Eq. (64): the sum runs over $l$ but the summand has superscript $(n,m)$, and the factor $h$ is missing (it appears in Eq. 65).
- Eq. (72): "$\bar\rho(x,t^n)\bar u(x,\Delta t)$" for $\bar u(x,t^n)$. Eq. (94): "$U^{(n,2,L)}$" for $U^{(n,l,L)}$. Eq. (90): "$a_{ll}$" where elsewhere the implicit coefficients are $\tilde a_{ll}$.
- Def. 3.1 labels the partitioned matrix "$A=\begin{pmatrix}0&0\\ \tilde a&\tilde A\end{pmatrix}$", reusing $\tilde A$ for its own sub-block (and $\mathcal A$ in Eq. 68).
- §4 after Eq. (86): "for $M_{loc}\approx1$, we obtain the Rusanov flux, whereas for $M_{loc}\ll1$, we obtain a local Lax-Friedrichs flux". By Eq. (86), $M_{loc}\to0$ gives the centred flux, and the Rusanov flux is the local Lax–Friedrichs flux.
- The Fig. 3 and 4 captions write "$p_\infty$" for $\pi_\infty$. §5.2 says "we keep $\tilde u_0=2\sqrt{1.4}$" where Eq. (98b) names it $\bar u_0$.
- References: [88] "E. Zampa and E. Dumbser" (M. Dumbser); [85] "G. Wanner and E. Hairer" (order reversed); [80] "cell-centered an staggered". Several entries print issue numbers in the volume slot (e.g. [1] "5 (2019)", [27] "17 (2012)", [57] "2 (1995)").
- Affiliation: "École polyechnique, Institute Polytechnique de Paris".

# Notation map

| Orlando & Bonaventura | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$, $t^n$ | $h$, $t_n$ | |
| $M$ | $\varepsilon$ | reference Mach number; **the registry reserves $M$ for the mass matrix** |
| $M_{loc}$ | kept | local Mach number in the flux blend (Eq. 85) |
| $(A,b,c)=(a_{lm},b_l,c_l)$ | $(A^{\mathrm E},b^{\mathrm E},c^{\mathrm E})$ | **the untilded tableau is the explicit one** |
| $(\tilde A,\tilde b,\tilde c)$ | $(A^{\mathrm I},b^{\mathrm I},c^{\mathrm I})$ | **tilde marks the implicit tableau**, opposite to the semi-implicit IMEX sources of this bundle |
| $\tilde a$, $\tilde A$ (Def. 3.1 block) | $a$, $\hat A$ | first column below row 1 and invertible trailing block of a type II $A^{\mathrm I}$ |
| $\hat w_{lm}$ | kept | entries of $\hat A^{-1}$ |
| $R(z)$, $R_\infty$ | $R(z)$, $R(\infty)$ | stability function of the implicit part |
| $f_E$, $f_I$ | $f^{\mathrm E}$, $f^{\mathrm I}$ | non-autonomous form $f(y,t)$ |
| $v^n$, $v^{(n,l)}$ | $y_n$, $Y_l$ | stage values |
| $l$, $m$ | $i$, $j$ | stage indices |
| $\bar f,f',f''$ | kept | orders $\varepsilon^0,\varepsilon^1,\varepsilon^2$ of the Mach expansion |
| $\xi=Mx$ | $\xi=\varepsilon x$ | acoustic length scale |
| $\gamma$ | kept (ratio of specific heats) | only the EOS meaning in the source; the diagonal of Table 1 is written $\gamma$ only in the compiler checks |
| $c$ | kept (sound speed) | **collides with the abscissae $c$** |
| $b$ (co-volume), $a$ (cubic EOS) | kept | **$b$ collides with the weights**, $a$ with the first column of a type II tableau |
| $s$ | $s$ | stages; also the specific entropy in Eq. (14) |
| $r$, $N_{el}$ | kept | DG degree, elements per direction |
| $C$, $C_u$ | kept | acoustic and advective Courant numbers (Eq. 95), including the factor $r$; the registry $\nu$ is the generic Courant number |
| $\hat\tau^{(n,l)}$, $\hat\tau^{n+1}$ | kept | local truncation errors of a stage and of the update on the exact limit solution |

# Reference list

89 printed references, numbered [1]–[89], numeric style in alphabetical order. The list is merged complete into the [bibliography](/bibliography.md) with `citedby` orlando-2025. No DOIs are printed, and many entries print no volume. Several put an issue number in the volume slot and are recorded as printed. [44] (Happenhofer et al., "ArXiv e-prints (2011)") is a preprint without identifier. [9] (Boscarino–Pareschi–Russo, "In press to SIAM books, 2024") is kept as the in-press entry `boscarino-2024-c`, distinct from the published book `boscarino-2024`. [85] ("G. Wanner and E. Hairer") is merged into `hairer-1996`. [12] and [33] are `boscheri-2020-b` and `dumbser-2016-c`, because the bibliography already held other works under those keys, and the two Orlando 2023 items [67] (PhD thesis) and [69] follow the existing keys `orlando-2023-c` and `orlando-2023-b`. [20] is a NASA technical memorandum. [54] is Kennedy & Carpenter's ARK paper (Appl. Numer. Math. 2003). There are no printed duplicates or unparseable items.

# Pages created or updated

Chunk 3 (2026-10-19). This source is cited on:

* [Asymptotic-preserving scheme](/definitions/asymptotic-preserving-scheme.md)
* [Colliding acoustic pulses](/benchmarks/colliding-acoustic-pulses.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [Gresho vortex](/benchmarks/gresho-vortex.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Kennedy–Carpenter additive Runge–Kutta methods (ARK3, ARK4, ARK5)](/methods/kennedy-carpenter-ark-methods.md)
* [Stiff accuracy](/properties/stiff-accuracy.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
* [Total variation diminishing (TVD) time stepping](/definitions/total-variation-diminishing.md)
* [Uniform accuracy of IMEX schemes for hyperbolic relaxation systems](/results/uniform-accuracy-relaxation-systems.md)

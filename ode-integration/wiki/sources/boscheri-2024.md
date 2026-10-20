---
type: Source
title: "Boscheri & Thomann (2024) — A Structure-Preserving Semi-implicit IMEX Finite Volume Scheme for Ideal Magnetohydrodynamics at all Mach and Alfvén Numbers"
description: "Builds a second-order semi-implicit IMEX finite-volume scheme for ideal MHD whose step is limited only by the material speed at any Mach and Alfvén number, using a three-way flux split, two decoupled linear implicit solves per stage and an exactly divergence-free vector potential."
resource: "doi:10.1007/s10915-024-02606-1"
source_kind: paper
authors: [Boscheri W., Thomann A.]
year: 2024
venue: "J. Sci. Comput. 100:67"
local_file: "/home/stefano/papers/mosaic/ode-integration/2024_Crossref_Journal_of_Scientific_Computing_Boscheri_A_Structure-Preserving_Semi-implicit_IMEX_Finite_Volume_Sche.pdf"
tags: [imex, asymptotic-preserving, stiff, implicit-stage-solvers, cfd]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper builds SIFV-EB (semi-implicit finite volume, implicit in energy and $\mathbf B$), a second-order finite-volume scheme for the ideal MHD equations. Its time step is limited only by the material (convective) speed, at any acoustic Mach number $\varepsilon_{\mathrm c}$ and any Alfvén Mach number $\varepsilon_{\mathrm b}$. The flux is split three ways, into convective $\mathbf f^c$, pressure $\mathbf f^p$ and magnetic $\mathbf f^b$ parts, and the whole hydrodynamic energy flux goes into $\mathbf f^p$. The convective part is explicit, with a Rusanov flux whose dissipation scales only with $\lvert u\rvert$. The pressure and magnetic parts are implicit. Freezing selected factors at $t_n$ (e.g. $\lVert\mathbf B\rVert^2\approx\mathbf B^n\cdot\mathbf B^{n+1}$, $(\rho E+p)u\approx(\rho E^n+p^n)u^{n+1}$) turns the implicit part into two **decoupled linear systems** solved in sequence: a vector system for the magnetic potential $\mathbf A^{n+1}$, then a scalar elliptic system for $(\rho E)^{n+1}$. Both are solved by GMRES, and no Newton or Picard iteration is needed (see [implicit-stage solvers](/methods/implicit-stage-solvers.md)).

The authors state that the three-term split does not fit the two-term [IMEX Runge–Kutta](/methods/imex-runge-kutta.md) class. They recast it in the [semi-implicit IMEX-RK](/methods/semi-implicit-imex-runge-kutta.md) form $y'=\mathcal H(y_{\mathrm E},y_{\mathrm I})$ of Boscarino, Filbet & Russo and integrate it with the two-stage LSDIRK2 pair, whose implicit part is the [stiffly accurate](/properties/stiff-accuracy.md) [SDIRK](/methods/diagonally-implicit-runge-kutta.md) with $\gamma=1-1/\sqrt2$. A collocated curl–divergence pair with $\mathbb D(\mathbb C(\mathbf q))=0$ keeps $\nabla\cdot\mathbf B=0$ to machine precision. The [asymptotic-preserving](/definitions/asymptotic-preserving-scheme.md) property for $\varepsilon_{\mathrm c}\to0$ at $\varepsilon_{\mathrm b}=1$ is asserted by reference to an earlier proof, not proved here. The scheme is stated not to be [positivity preserving](/properties/positivity-preservation.md).

The evidence is numerical. A traveling MHD vortex shows second-order convergence over six density levels. The other tests are seven Riemann problems, the blast wave, the rotor, Orszag–Tang, low-Mach field-loop advection, a magnetized Kelvin–Helmholtz instability with steps up to about $10^4$ times the explicit magneto-sonic step, and a 3D cloud–shock interaction.

# Version read

arXiv:2403.04517v1 [math.NA], 7 Mar 2024, typeset in the Springer JSC submission template ("will be inserted by the editor", "Received: date / Accepted: date"). This is the submitted manuscript, not the version of record. It has 34 pages. Title and authors match Crossref (printed in sentence case), and the DOI is not printed. Page, equation and table numbers cited here are those of arXiv v1. The code is in Fortran, available on request.

# Key claims

Notation: $h$ is the step. $\varepsilon_{\mathrm c}=\lVert\mathbf v\rVert/c$ and $\varepsilon_{\mathrm b}=\lVert\mathbf v\rVert/b$ are the acoustic and Alfvén Mach numbers (source $M_c$, $M_b$). The tableaux are $(A^{\mathrm E},b^{\mathrm E},c^{\mathrm E})$ and $(A^{\mathrm I},b^{\mathrm I},c^{\mathrm I})$. MHD symbols are those of the source (Gaussian units).

1. The three-way flux form (Eq. 14) separates convective $\mathbf f^c$, pressure $\mathbf f^p$ and magnetic $\mathbf f^b$ fluxes. Unlike the splitting of [59] (used in [31, 36]), the hydrodynamic energy flux is not split into convective and pressure parts and goes entirely into $\mathbf f^p$; $\rho m$ also enters $\mathbf f^p$. (§2.2, Eq. 14) **Derived**
2. Sub-system eigenvalues: convective $\lambda^c_{1..4}=0$, $\lambda^c_{5..8}=u$ (Eq. 16b). Pressure $\lambda^p_{1..6}=0$, $\lambda^p_{7,8}=\tfrac12\big(u\mp\sqrt{u^2+4(c^2-(\gamma-1)(m+k+u^2))}\big)$ (Eq. 17b), which "might become complex" for highly magnetized fluids, so the pressure sub-system can be elliptic. Magnetic $\lambda^b_{5,6}=\tfrac12\big(u\mp\sqrt{u^2+4(B_x/\sqrt{4\pi\rho})^2}\big)$ and $\lambda^b_{7,8}=\tfrac12\big(u\mp\sqrt{u^2+4\lVert\mathbf B\rVert^2/(4\pi\rho)}\big)$ are real, so that sub-system is hyperbolic (Eq. 18b). (§2.2) **Derived**
3. The step obeys a CFL condition built on the convective sub-system alone, $h\le\mathrm{CFL}\,(\Delta x\Delta y\Delta z)^{1/3}/\max_\Omega\lvert\lambda^c\rvert^n$ (Eq. 20), with CFL $=0.9$ in all tests. (§4) **Stated** (stability not proved; shown in tests)
4. The semi-implicit linearization $\lVert\mathbf B\rVert^2\approx\mathbf B^n\cdot\mathbf B^{n+1}$ makes the 1D magnetic sub-system (Eq. 23) linear in $(B_y^{n+1},B_z^{n+1})$. (§3.1) **Derived**
5. The energy sub-system becomes one scalar linear elliptic equation (Eq. 28) for $(\rho E)^{n+1}$. This follows from the ideal-gas EOS (Eq. 4) and the semi-implicit discretization of $(\rho E^n+p^n)u^{n+1}$ and $\tfrac{\lVert\mathbf B^{n+1}\rVert^2}{8\pi}u^n$. (§3.1, Eqs. 26–30) **Derived**
6. The magnetic and energy implicit systems are **decoupled** and solved in sequence: first $\mathbf A^{n+1}$ (or $\mathbf B^{n+1}$ in 1D), then $(\rho E)^{n+1}$; momentum is then updated explicitly. (§3.1, §3.5, §5) **Derived**
7. In multi-D the scheme evolves the vector potential $\mathbf A$ in non-conservative form (Eq. 31), with $\mathbf B=\nabla\times\mathbf A$ (Eq. 32). The semi-implicit magnetic step (Eqs. 33–35) uses $(\nabla\times\mathbf A)\otimes(\nabla\times\mathbf A)\approx\mathbf B^n\otimes(\nabla\times\mathbf A^{n+1})$. (§3.2) **Derived**
8. The time semi-discrete scheme is **asymptotic preserving for $\varepsilon_{\mathrm b}=1$, $\varepsilon_{\mathrm c}\to0$**, toward incompressible Euler for well-prepared data. The proof is in [49]: the Euler sub-scheme "coincides" with that of [49], "thus the proof can be applied directly … for $M_b=\mathcal O(1)$". (§3.2, p. 11) **Stated** (proof cited, not given)
9. The three-way split "is not suitable for the class of IMEX Runge-Kutta methods [53, 3] that allows only the splitting according to two time scales". A two-way semi-implicit form, following [12], is used instead. (§3, p. 7) **Stated**
10. Second order in time comes from the semi-implicit IMEX-RK framework of [12] (Boscarino–Filbet–Russo 2016) with the LSDIRK2 pair (Eq. 39) of [3], $\gamma=1-1/\sqrt2$, $c^{\mathrm E}_2=1/(2\gamma)$. (§3.3) **Stated** (order taken from [12, 3]; confirmed numerically in claim 15)
11. LSDIRK2 is called stiffly accurate because $b^{\mathrm E}=b^{\mathrm I}$ and $b^{\mathrm I}$ equals the last row of $A^{\mathrm I}$. Stiff accuracy is "a crucial property for assuring asymptotic consistency and accuracy of the scheme, see also [15]", and the update takes the last stage, $y_{n+1}=Y_s$. (§3.3, p. 12) **Stated**
12. The discrete divergence and curl built on the central gradient (Eq. 50) satisfy $\mathbb D(\mathbb C(\mathbf q))=0$ (Eq. 53), so $\mathbf B^{n+1}=\mathbb C(\mathbf A^{n+1})$ is divergence-free to machine accuracy. The proof is cited to Appendix A of [17]. (§3.4) **Stated** (identity "easy to check"; proof cited)
13. Implicit numerical dissipation, a Laplacian $\mathbb L(\lambda^b\Delta x,\cdot)$ with magnetic-subsystem eigenvalues as coefficients, is added to every component of $\mathbf A$ following [44]. "This operator is discretized implicitly, thus it does not affect the stability of the overall scheme." (§3.5 step 2, p. 15) **Stated**
14. No numerical dissipation is added to the implicit pressure fluxes, so the scheme does not degrade at low Mach number, unlike explicit finite-volume schemes whose viscosity scales as $O(1/\varepsilon_{\mathrm c})$. (§1, §3, §5) **Stated** (supported qualitatively by claim 20)
15. MHD traveling vortex, $t_f=1$, meshes $32^2$ to $256^2$: "for all regimes, the expected EOC of two is achieved" in the $L^2$ errors of $\rho,u,p,B_x,A_z$ for background density $\rho_0=10^{-k}$, $k=0,\dots,5$. At $\rho_0=1$ and $256^2$ the $\rho$ error is $9.26\times10^{-4}$ (EOC 2.03). The low-density rows are irregular: at $\rho_0=10^{-5}$ the EOC runs 0.91, 2.81, 3.12 in $\rho$ and 3.24, 3.36, 2.04 in $u$. (§4.1, Table 2) **Shown**
16. "The scheme is not naturally positivity preserving." (§4.1, p. 17) **Stated**
17. On the vortex the SIFV-EB step is "several orders of magnitude larger" than a fully explicit magneto-sonic step at low $\varepsilon_{\mathrm c}$ and $\varepsilon_{\mathrm b}$. Fig. 1 plots $h/h_{\mathrm{MHD}}$ between $10^0$ and about $10^3$ over $\rho_0=1,\dots,10^{-5}$. (§4.1, Fig. 1) **Shown**
18. Riemann problems RP1–RP7 (2000 cells) give correct shock positions for RP2–RP7. The RP1 density and pressure overshoot also appears with HLLEM, Osher and Rusanov. The scheme is "clearly more diffusive than an explicit approximate Riemann solver", which the authors attribute to its semi-implicit nature and the larger material steps; $h/h_{\mathrm{MHD}}$ runs from about 1 to about 23. The first step always uses an explicit magneto-sonic step, because a zero initial velocity would give an infinite material step. (§4.2, Figs. 2–4) **Shown**
19. Blast and rotor: $\lVert\nabla\cdot\mathbf B\rVert_\infty$ stays between about $10^{-14}$ and $10^{-10}$ over 1000 steps, and the step is "up to four times larger than a classical explicit solver". (§4.4, Fig. 7) **Shown**
20. Magnetized Kelvin–Helmholtz with $\varepsilon_{\mathrm c}$ (source $M_x$) $=10^{-1},\dots,10^{-4}$: results rescaled by the Mach number are "almost identical", while "fully explicit schemes would not preserve the vortical structures as the value of $M_x$ gets smaller, as noticed in [47]". The step is "up to 10,000 times larger compared to a fully explicit method" (Fig. 12: ratio about $10^1,10^2,10^3,10^4$). (§4.7, Figs. 11–12) **Shown** (the explicit-scheme failure is cited, not shown)
21. Field loop: the solution is qualitatively unchanged for $A_0=10^{-3},\dots,1$ ($\varepsilon_{\mathrm b}\approx7.9\cdot10^3$ down to $\approx7.9$) with the same step in every run, "demonstrating that the new SIFV-EB scheme is independent of the magnetic scales". $\lVert\nabla\cdot\mathbf B\rVert_\infty$ stays at machine accuracy. (§4.6, Figs. 9–10) **Shown**
22. 3D cloud–shock interaction ($180^3$ cells): the second-order scheme "greatly improves" on first order and shows "genuinely 3D magnetized flows at reasonable compute times due to the linear implicit structure". No timings are given. (§4.8, Fig. 13) **Shown** (qualitative; no cost data)
23. The only earlier semi-implicit scheme for the low-Alfvén regime is [36] (Fambri 2021): first order in time, staggered, with a nonlinearly coupled implicit sub-system that needs a fixed-point method nested with Newton [24]. (§1, §3) **Stated**

*(Compiler checks, not in the sources.)* LSDIRK2 satisfies the order-2 conditions, including the coupling conditions $b^{\mathrm E\top}c^{\mathrm I}=b^{\mathrm I\top}c^{\mathrm E}=\tfrac12$. Its explicit part is not stiffly accurate: the last row $(c^{\mathrm E}_2,0)\ne b^{\mathrm E}$, with $c^{\mathrm E}_2\approx1.707>1$. The pair is therefore not globally stiffly accurate, and claim 11 concerns only the implicit part plus $b^{\mathrm E}=b^{\mathrm I}$. Claim 9 holds only for the two-tableau class cited: [additive and GARK methods](/methods/generalized-additive-runge-kutta.md) allow more than two partitions. Claim 15 is loose, since Table 2 shows EOCs from 0.91 to 3.36 at $\rho_0\le10^{-3}$, and 1.67–1.69 for $u$ at $256^2$ for $\rho_0=1$ and $10^{-1}$.

# Printed slips

- §4 preamble (p. 16): "we set $\gamma = 3/5$"; Table 3 states "In all cases $\gamma=5/3$".
- §2–§3: the ideal MHD system is called "(31)" several times ("The ideal MHD system (31) exhibits 8 characteristic speeds", "the MHD system (31) reduces to", …). Eq. (31) is the later $\mathbf A$ formulation; Eq. (1) is meant.
- Eq. (42): $\mathbb F_x=\big(\mathcal F_{i+\frac12jk}-\mathcal F_{i+\frac12jk}\big)/\Delta x$; the second index should be $i-\frac12$. Eqs. (48)–(49) print both interface coefficients as $h_{i+\frac12jk}$, the second for $h_{i-\frac12jk}$.
- Eq. (54): the left side is printed $\mathbb L(\nu,q)$, while the text and right side use $\kappa$.
- Eq. (40b): $\tilde{\mathbf q}^i_I=\mathbf q^n_E+\dots$ uses $\mathbf q^n_E$ for the implicit stage (harmless, since both equal $\mathbf q^n$). The update $\mathbf q^{n+1}=\mathbf q^s$ never defines $\mathbf q^s$.
- §3.5 step 4 (p. 15): the display for $(\rho\mathbf v)^{\star\star}$, $(\rho E)^{\star\star}$ is unnumbered (numbering jumps from (58) to (60)), and $h^n$ in Eqs. (60)–(61) is never defined. "After inserting the definition (27) in the momentum equations (30)": Eq. (30) is the 1D $(\rho u)^{\star\star}$ definition.
- Eqs. (70)–(71), Orszag–Tang: $B_y$ is printed with $\sin(4\pi y)$ (standard: $\sin(4\pi x)$), and the printed $A_z=\frac1{8\pi^{3/2}}(\cos2\pi x+2\cos\pi y)$ does not generate the printed $\mathbf B$; $\cos4\pi x+2\cos2\pi y$ does. §4.5 gives $\Omega=[0,1]^2$, but the Fig. 8 axes run to about $2\pi$. The text gives snapshots at "$t=\{0.5,1,2,4\}$" and the Fig. 8 caption "$t=0.5$, $2$, $3$ and $4$".
- Fig. 3 caption "RP7 at time $t_f=0.2$" against $t_f=0.25$ in Table 3. Fig. 7 caption "for 1000 time steps", while the axis ends near 400. Fig. 10 caption has a stray "·".
- Eqs. (75)–(76), cloud–shock: the shock is printed at "$x_0=0.0$" while $\mathbf A$ uses $(x-0.05)$. The curl of the printed $\mathbf A$ gives $B_y=-0.564$ where Eq. (75) gives $+0.56418958$, and the two printed magnitudes differ (0.56418958 against 0.56418956).
- §4.8: "$N_x=N_y=N_z=180^3$ cells, corresponding to approximately $16.5\cdot10^6$ degrees of freedom". $180^3\approx5.83\cdot10^6$ cells, and the DOF figure matches neither cells nor unknowns.
- Table 1: $\varepsilon_{\mathrm c}=16.06$ at $\rho_0=1$ against $0.449$ at $\rho_0=10^{-1}$, a factor of about 36 where the other levels scale by about $\sqrt{10}$.
- §4.1: $\delta A_z=\frac{\tilde B}{2\pi}\exp(1-r^2)$ lacks the factor $\tfrac12$ in the exponent present in Eqs. (64)–(65). Eq. (66) prints a dimensionally odd $\partial(\delta B_\theta)^2/(8\pi r)$. Eq. (74) writes $\eta(x)$ for a function of $y$.
- References: [2] Ascher–Ruuth–Spiteri is printed with year 1982 (Appl. Numer. Math. 25 is 1997). [56] prints "C-M. Tang S. A. Orszag." without "and".

# Notation map

| Boscheri & Thomann | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$, $t^n$ | $h$, $t_n$ | |
| $\Delta t_{\mathrm{MHD}}$ | $h_{\mathrm{MHD}}$ | explicit magneto-sonic step |
| $M_c=\lVert\mathbf v\rVert/c$, $M_b=\lVert\mathbf v\rVert/b$, $M_x$ | $\varepsilon_{\mathrm c}$, $\varepsilon_{\mathrm b}$ | acoustic and Alfvén Mach numbers; **the registry reserves $M$ for the mass matrix** |
| $\beta=\tilde p/\tilde m$ | kept | plasma beta |
| $\mathbf q$, $\mathbf q_E$, $\mathbf q_I$ | $y$, $y_{\mathrm E}$, $y_{\mathrm I}$ | state; explicit and implicit argument copies (page-local) |
| $\mathcal H(\mathbf q_E,\mathbf q_I)$ | $\mathcal H(y_{\mathrm E},y_{\mathrm I})$ | partitioned right-hand side |
| $(\tilde c,\tilde A,\tilde b)$ | $(c^{\mathrm E},A^{\mathrm E},b^{\mathrm E})$ | **tilde marks the explicit tableau** |
| $(c,A,b)$ | $(c^{\mathrm I},A^{\mathrm I},b^{\mathrm I})$ | implicit tableau |
| $k_i$ | $\mathcal H(Y^{\mathrm E}_i,Y^{\mathrm I}_i)$ | stage derivatives, translated to stage values |
| $\mathbf q^i_E$, $\tilde{\mathbf q}^i_I$ | $Y^{\mathrm E}_i$, $Y^{\mathrm I}_i-ha^{\mathrm I}_{ii}\mathcal H(\cdot)$ | the source's implicit stage omits its diagonal term |
| $\alpha=1-1/\sqrt2$ | $\gamma$ | SDIRK diagonal; **$\alpha$ is also the Rusanov dissipation (Eq. 44) and the boundary slope (Eq. 63)** |
| $\tilde c=1/(2\alpha)$ | $c^{\mathrm E}_2$ | |
| $\gamma$ | $\gamma$ (ratio of specific heats) | **collides with the SDIRK diagonal $\gamma$ of this page; the meaning is fixed by context** |
| $\lambda^c,\lambda^p,\lambda^b$ | kept | sub-system eigenvalues; **not the Dahlquist $\lambda$**; $\lambda^b$ is also a dissipation coefficient |
| $\rho e,\rho k,\rho m$ | kept | internal, kinetic, magnetic energy densities, $m=\lVert\mathbf B\rVert^2/8\pi$ |
| $\mathbb F,\mathbb B,\mathbb H,\mathbb G,\mathbb C,\mathbb D,\mathbb L$ | kept | discrete flux, central flux, diffusion, gradient, curl, divergence, Laplacian; **$\mathbb B$ (operator) against $\mathbf B$ (field)** |
| $h^n$ (Eqs. 60–61) | kept, page-local | $(\rho E^n+p^n)/\rho^{n+1}$; **collides with the registry step $h$** |
| CFL | $\nu$ | on the material speed only |

# Reference list

62 printed references, numbered [1]–[62], alphabetical by first author. The list is merged complete into the [bibliography](/bibliography.md) with `citedby` boscheri-2024. [20] is Boscheri & Pareschi, JCP 434:110206, the ingested source [Boscheri & Pareschi (2021)](/sources/boscheri-2021.md). Printed slips are merged under the published identity: [2] prints the wrong year 1982 for Ascher–Ruuth–Spiteri and is `ascher-1997`; [24] prints 2007 for Brugnano–Casulli and is `brugnano-2008`; [56] prints a malformed author string ("C-M. Tang S. A. Orszag.") and is `orszag-1979`; [52], printed with Osher first, is `hofer-1976`. Same-key pairs follow the keys already in the bibliography, not the printed order: [13]/[14] are `boscarino-2017-b`/`boscarino-2017` and [30]/[32] `dumbser-2016-b`/`dumbser-2016`; [17], [21], [22] and [42] take the suffixed keys `boscheri-2023-b`, `boscheri-2022-b`, `bouchut-2007-b` and `harten-1983-b`. [11] has no pages, and [38] is a proceedings paper with no editors or publisher. No DOIs or arXiv identifiers are printed.

# Pages created or updated

Chunk 3 (2026-10-19). This source is cited on:

* [Asymptotic-preserving scheme](/definitions/asymptotic-preserving-scheme.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [Positivity preservation in time integration](/properties/positivity-preservation.md)
* [Semi-implicit and linearly implicit IMEX Runge–Kutta methods](/methods/semi-implicit-imex-runge-kutta.md)
* [Stiff accuracy](/properties/stiff-accuracy.md)

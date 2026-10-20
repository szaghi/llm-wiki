---
type: Source
title: "Boscheri & Pareschi (2021) — High order pressure-based semi-implicit IMEX schemes for the 3D Navier-Stokes equations at all Mach numbers"
description: "Builds a third-order pressure-based semi-implicit IMEX finite-volume solver for compressible Navier–Stokes at all Mach numbers, whose stages need one linear pressure solve, with a formal low-Mach asymptotic-preserving proof of the first-order scheme and Mach-uniform convergence."
resource: "doi:10.1016/j.jcp.2021.110206"
source_kind: paper
authors: [Boscheri W., Pareschi L.]
year: 2021
venue: "J. Comput. Phys. 434:110206"
local_file: "/home/stefano/papers/mosaic/ode-integration/2021_Crossref_Journal_of_Computational_Physics_Boscheri_High_order_pressure-based_semi-implicit_IMEX_schemes_for_the.pdf"
tags: [imex, asymptotic-preserving, stiff, implicit-stage-solvers, cfd]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper builds a cell-centred, collocated Cartesian solver ("SI-P", semi-implicit pressure) for the 3D compressible Navier–Stokes equations at all Mach numbers, for ideal gases and for a general (Redlich–Kwong) equation of state. The Mach number enters through the stiffness parameter $\varepsilon=\rho_0u_0^2/p_0$, which scales like the squared Mach number. Convective and viscous fluxes are explicit, the pressure gradient is implicit, and the energy equation is semi-implicit: the kinetic energy in $(\rho E)^{n+1}$ is written $\varepsilon\frac{(\rho u)^n}{2\rho^n}(\rho u)^{n+1}$ and the enthalpy flux $h_{\mathrm{enth}}^n(\rho u)^{n+1}$. Substitution gives an elliptic pressure equation. It is **linear** in $p^{n+1}$ for an ideal gas; for a general EOS it is mildly nonlinear and is solved by a nested Newton method. No Picard iteration on the pressure is needed, and the step is limited by the material speed $\lvert u\rvert$, not the acoustic speed $c/\sqrt\varepsilon$.

A formal Hilbert expansion in $\varepsilon$ shows that the first-order semi-discrete scheme is [asymptotic preserving](/definitions/asymptotic-preserving-scheme.md) for the incompressible limit, and a direct computation shows that the first-order fully discrete scheme keeps pressure and velocity constant across a contact.

High order in time comes from the [semi-implicit IMEX Runge–Kutta](/methods/semi-implicit-imex-runge-kutta.md) reformulation of Boscarino, Filbet & Russo. The system is written $y'=\mathcal H(y_{\mathrm E},y_{\mathrm I})$, the explicit argument is advanced with $A^{\mathrm E}$ and the implicit one with $A^{\mathrm I}$, and each implicit stage is one linear pressure solve. Four [IMEX](/methods/imex-runge-kutta.md) tableaux are printed. The [stiffly accurate](/properties/stiff-accuracy.md) SA DIRK(3,4,3) is declared the only one consistent with the stiff limit, and SSP3(4,3,3), whose explicit part is [SSP](/methods/strong-stability-preserving-runge-kutta.md), is used for high Mach. Space is handled by fourth-order central differences for implicit terms and a CWENO finite-volume reconstruction for explicit terms, with an a-priori flattener at shocks.

The evidence is numerical. Third order holds uniformly in $\varepsilon\in[10^{-6},1]$ on the [isentropic vortex](/benchmarks/isentropic-vortex.md). The other tests are shock tubes (ideal gas and Redlich–Kwong), the [Gresho vortex](/benchmarks/gresho-vortex.md) at three Mach numbers with one time step, a viscous shock and the 3D [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) against DNS.

# Version read

arXiv:2008.01789v1 [math.NA], 4 Aug 2020, with the footer "Preprint submitted to Journal of Computational Physics, August 6, 2020". This is the submitted manuscript, not the JCP version of record. It has 37 pages (text pp. 1–35, references pp. 35–37). The DOI is not printed. Title and authors match Crossref. Equation, table and reference numbers cited here are those of arXiv v1.

# Key claims

Notation: $h$ is the step and $\varepsilon=\rho_0u_0^2/p_0\propto$ Mach$^2$. The explicit and implicit tableaux are $(A^{\mathrm E},b^{\mathrm E},c^{\mathrm E})$ and $(A^{\mathrm I},b^{\mathrm I},c^{\mathrm I})$; the source writes them $(\tilde A,\tilde b,\tilde c)$ and $(A,b,c)$. Physical symbols ($\rho,u,p,e,E,k$) are those of the source; its enthalpy $h$ is written $h_{\mathrm{enth}}$ (see the notation map).

1. The first-order semi-discrete scheme (Eqs. 22–24) is locally and globally conservative, and its step is limited only by the material speed, $h\le\mathrm{CFL}\,\min_\Omega(\Delta x,\Delta y,\Delta z)/\max_\Omega\lvert u\rvert$ with CFL $<1$ (Eq. 27). The explicit acoustic restriction (Eq. 20), with speeds $\lvert u\pm c/\sqrt\varepsilon\rvert$, gives $h=O(\sqrt\varepsilon)$. (§3.1) **Derived**
2. Writing $(\rho E)^{n+1}:=(\rho e)^{n+1}+\varepsilon\frac{(\rho u)^n}{2\rho^n}(\rho u)^{n+1}$ and the enthalpy flux as $h_{\mathrm{enth}}^n(\rho u)^{n+1}$ makes the pressure equation (29) linear in $p^{n+1}$ for an ideal gas, so no Picard iteration is needed, unlike the cited solvers [23, 68]. (§3.1, Eqs. 26, 29, 32) **Derived**
3. For a general EOS the pressure equation $g(p^{n+1})=\mathcal P(p^{n+1})+\mathcal Rp^{n+1}-b^n=0$ is solved by a nested Newton method following Brugnano–Casulli [13], tolerance $10^{-10}$. (§3.1, Eqs. 33–36) **Stated** (algorithm); convergence shown in claim 14.
4. The first-order semi-discrete scheme is asymptotic preserving as $\varepsilon\to0$ (inviscid case). The leading-order discrete system implies $\nabla\cdot u^{n+1}_{(0)}=O(h)$ with a constant independent of $\varepsilon$ (Eq. 41), via $-\big((\rho^n)^2\frac{\partial e}{\partial\rho}-p^n\big)\nabla\cdot u^{n+1}=O(h)$ (Eq. 46). For an ideal gas this reduces to $h_{\mathrm{enth}}^n\nabla\cdot u^{n+1}=O(h)$ (Eq. 47). (§3.1) **Derived** (formal expansion, not a theorem with estimates)
5. A compact Lagrange-interpolation finite-difference operator for $\partial_x(h_{\mathrm{enth}}\,\partial_xp)$ (Eq. 53) keeps the pressure stencil on $[i-1,i+1]$ at second order and on $[i-2,i+2]$ at fourth order (Eq. 83). The fully discrete substitution of [23, 68] gives $[i-2,i+2]$ already at second order. The correction $C_E=E_2-E_1$ is quantified (Eq. 61) and does not compromise the incompressible limit. (§3.2) **Derived**
6. The first-order fully discrete scheme with the enthalpy discretization $h_{\mathrm{enth},i}^n=\rho_i^nh_{\mathrm{enth},i}^n/\rho_i^{n+1}$ (Eq. 58) preserves a constant pressure $p_0$ and velocity $u_0$ exactly across a moving contact, independently of $\varepsilon$. (§3.3, Eqs. 62–68) **Proved** (direct computation); shown numerically in claim 13.
7. High order in time uses the semi-implicit IMEX-RK formalism of [58]: the system is written as a partitioned autonomous system $y_{\mathrm E}'=\mathcal H(y_{\mathrm E},y_{\mathrm I})$, $y_{\mathrm I}'=\mathcal H(y_{\mathrm E},y_{\mathrm I})$. For autonomous systems the doubling of unknowns is only apparent, and one set of stage derivatives $\mathcal H(Y^{\mathrm E}_i,Y^{\mathrm I}_i)$ is computed. (§3.4.1, Eqs. 75–77) **Stated** (cited from [58])
8. The IMEX schemes used have $b^{\mathrm E}=b^{\mathrm I}$ and a stiffly accurate implicit part, "crucial for assuring asymptotic consistency and accuracy of the scheme [60]". (§3.4.1) **Stated**
9. Four IMEX tableaux are used: SP(1,1,1) (forward/backward Euler, Eq. 78), SA SSP(3,3,2) (Eq. 79), SA DIRK(3,4,3) with diagonal $0.435866$ (Eq. 80), and SSP3(4,3,3) with coefficients $0.241694$, $0.060424$, $0.129153$ (Eq. 81). The triplet $(s,\tilde s,p)$ counts implicit stages, explicit stages and order. (§3.4.1) **Stated** (from [55, 54])
10. "In the stiff limit only (80) [SA DIRK(3,4,3)] can be used in order to be consistent with the limit model at the discrete level [20, 60]"; (80) is used for low Mach and (81) for high Mach flows. (§3.4.1) **Stated**
11. Isentropic vortex at $\varepsilon=1$ ($L^1$, $t=1$, CFL 0.9): SI-P O3 with SA DIRK(3,4,3) gives $L^1(\rho)$ from $7.677\times10^{-5}$ ($16^2$) to $1.741\times10^{-7}$ ($128^2$), orders 2.72, 2.95, 3.11. With SSP(4,3,3) the orders for $\rho$ are 2.72, 2.91, 2.67; SI-P O2 reaches 2.01 for $\rho$. (Table 1) **Shown**
12. The orders are uniform in $\varepsilon\in[10^{-6},10^{-1}]$. For $\rho u$ with SA DIRK(3,4,3) the finest-level orders are 2.87, 2.95, 2.98, 2.99, 2.99, 2.99 at $\varepsilon=10^{-1},\dots,10^{-6}$, and $L^1(\rho u)$ at $128^2$ is $\approx5.448\times10^{-6}$ for $\varepsilon\le10^{-4}$. SI-P O2 gives orders 2.05–2.22. (Table 2) **Shown**
13. RP0, a contact with density ratio $10^5$ ($\rho_L=1000$, $\rho_R=0.01$, $p=10^5$) at Mach numbers in $[2.7\cdot10^{-4},8.5\cdot10^{-2}]$, keeps pressure and velocity constant "up to machine precision" at first and third order. (§4.2, Fig. 2) **Shown**
14. For the Redlich–Kwong shock tubes RK1 and RK2, the Newton algorithm (36) "has always converged to a tolerance $\delta=10^{-10}$ in at most four iterations". (§4.2) **Shown**
15. In RP2 (two shocks) and RP3 (two rarefactions), non-physical oscillations appear in the density, "also present in [23]". (§4.2, Figs. 4–5) **Shown**
16. High-order implicit time discretizations cannot remove over- and undershoots at strong discontinuities. The oscillations are "generated by the violation of the explicit CFL stability condition" and remain bounded, and "high order implicit schemes are not $L^\infty$ stable but only $L^2$ stable" (citing [61], observed in [68]). (§3.6) **Stated**
17. The a-priori flattener $\chi^n=\min[1,\max(0,-(\nabla\cdot u^n+k_1c^n_{\min})/(k_1c^n_{\min}))]$, $k_1=10^{-3}$, blends $y^{n+1}=\chi^ny^{n+1,\mathrm{lo}}+(1-\chi^n)y^{n+1,\mathrm{hi}}$, the first-order and the high-order (CWENO) candidate solutions. It flags only shocked cells and is never activated in smooth low-Mach flows. (§3.6, Eqs. 104–105, Fig. 8) **Shown**
18. The Gresho vortex is preserved at Mach numbers $10^{-1},10^{-2},10^{-3}$ ($80\times80\times4$ cells, CFL 0.15, $t_f=0.4\pi$) with the same time step for all Mach numbers. (§4.3, Fig. 9) **Shown**
19. The normalized kinetic energy $K/K_0$ of the Gresho vortex at $t_f$ is 0.997 (second order) and 0.998 (third order) on the fine mesh (cell size $1/80$), and 0.984 and 0.988 on the coarse mesh ($1/40$). The curves for the three Mach numbers almost overlap (CFL 0.25). (§4.3, Fig. 10) **Shown**
20. The viscous shock ($M_s=2$, $Re=100$, $Pr=0.75$, $\mu=2\times10^{-2}$, $200\times4\times4$, CFL 0.5, $t_f=0.2$) matches the Becker profile for $\rho$, $u$, $p$ and the heat flux $q_x$. The heat flux is implicit in the pressure equation (ideal gas). (§4.4, Fig. 11) **Shown**
21. On the 3D Taylor–Green vortex ($Re=100,200$, $120^3$ cells, $p_0=10^3$, CFL 0.5, $t_f=10$), the dissipation rate $-dK/dt$ fits the Brachet et al. DNS [48] on a coarser mesh than second-order solvers need (e.g. [68]). (§4.5, Fig. 13) **Shown** (qualitative, no error figures)
22. All simulations use the advective CFL condition (106) with viscous eigenvalues $\lambda_v=\max(\tfrac43\frac\mu\rho,\frac{\gamma\mu}{Pr\,\rho})$ (Eq. 21) and no $c/\sqrt\varepsilon$ dependence. (§4, Eq. 106) **Stated**
23. The design avoids an implicit equation for the total energy, which "would become fully nonlinear"; the pressure-based system stays mildly nonlinear for nonlinear equations of state. (§5) **Stated**

*(Compiler checks, not in the sources.)* As printed, the SA DIRK(3,4,3) tableau (Eq. 80) is not usable; see the printed slips. The implicit first row $c^{\mathrm I}_1=a^{\mathrm I}_{11}=0.435866$ is not a slip: it is the type-I structure also printed by [Orlando et al. (2025b)](/sources/orlando-2025-b.md) (Table 20) and [Southworth et al. (2024)](/sources/southworth-2024.md) (I-IMEX(3,4,3)), and since $b^{\mathrm I}_1=0$ and $a^{\mathrm I}_{i1}=0$ for $i\ge2$ it changes only the stage value passed to the explicit part. The "(3,4,3)" label is inherited from ARS(3,4,3) and no longer counts the implicit stages (see the [semi-implicit IMEX](/methods/semi-implicit-imex-runge-kutta.md) page). SSP3(4,3,3) is not stiffly accurate (last implicit row $\ne b^{\mathrm I}$), and its explicit part is SSPRK(3,3) padded with a zero first stage. The blanket statement of claim 16 holds only in the sense "not unconditionally", since SSP theory gives conditional $L^\infty$ bounds for some implicit methods. Claim 4 covers only the first-order scheme; high-order AP rests on the cited stiff-accuracy requirement and on Table 2.

# Printed slips

- **Eq. (80), SA DIRK(3,4,3).** (i) Implicit row 4 prints $a^{\mathrm I}_{44}=0.416993$, but $b^{\mathrm I}_4=0.435866$ and the scheme is called stiffly accurate. With $a^{\mathrm I}_{44}=0.435866$ the row sums to $c_4=1$; as printed it sums to $0.981126$. (ii) The explicit rows do not sum to $c^{\mathrm E}$: row 3 gives $1.437745+0.719812=2.157557\ne0.717933$, and row 4 gives $0.916993+1/2+0.416993=1.833986\ne1$.
- Eq. (75): the stage sums are printed "$\sum_{i=1}^s\tilde a_{ij}k_j$", with the summation index $i$ for $j$.
- Eq. (76b): "$\tilde Q_I^i=Q_E^n+\dots$" uses $Q_E^n$ for $Q_I^n$ (harmless, since both equal $Q^n$).
- Eq. (36): the Newton step prints the derivative "$\frac{dg(p^{n+1,k})}{p^{n+1,k}}$" without $d$ in the denominator. $\Delta p^k=p^{n+1,k+1}-p^{n+1,k}$ is then used as $p^{n+1,k+1}=p^{n+1,k}-\Delta p^k$ (sign inconsistency), and the stopping test "$\Delta p^k<\delta$" lacks a norm.
- Eqs. (33)–(36) call the general-EOS pressure equation "piecewise linear", although its nonlinearity comes from a smooth EOS (the term is borrowed from [13]).
- Eqs. (22)–(24), (31): the momentum convective flux is printed $\nabla\cdot((\rho u)^n\otimes(\rho u)^n)$, which is dimensionally $\rho^2u\otimes u$; $(\rho u)^n\otimes u^n$ is meant.
- Eq. (24): the equation number (25) is printed on an empty line.
- §3.4.1, Eq. (71): $\partial_tQ=H$ with $H$ "the spatial approximation of the terms $\nabla\cdot F+\nabla p$". Given Eq. (69), the sign should be $-(\nabla\cdot F+\nabla p)$.
- Eq. (73): the energy component reads $\rho_I(ku)_E+\rho_I(hu)_E$, which does not match the semi-discrete scheme (24) (kinetic flux fully explicit, momentum implicit in the enthalpy flux).
- Eq. (12) ff.: $\varepsilon$ is "related to the global Mach number $M=u_0/c$", but the relation is not stated.
- §1 "IMEX Runga-Kutta"; §3.4.1 "listened hereafter" (for "listed"); "Navier-stokes".
- §4.1: errors are said to be "measured in $L^1$, $L^2$ and $L^\infty$ norm", but Table 1 reports only $L^1$. Scheme names drift: "SA-SSP2" against "SA SSP(3,3,2)", and "SSP(4,3,3)" against "SSP3(4,3,3)".
- §4.1, Eq. (107): the initial condition $U=(1+\delta\rho,1,1,0,1+\delta p)$ has no vortex velocity perturbation, so as printed it is a density and pressure perturbation advected at $(1,1)$. This contradicts the stated stationarity with exact solution equal to the initial condition. The vortex strength $\epsilon$ in $\delta T$ (Eq. 108) is never given a value and is easy to confuse with $\varepsilon$.
- Table 1, SA DIRK(3,4,3): the last order for $\rho E$ is 4.37 (spike) and for $\rho u$ 2.62 (drop).
- Table 3, RP0: $u_L=u_R=0$, but the text describes a contact "moving at constant velocity", and Fig. 2 plots $u\approx1$.
- §4.3: "$K/K_0$ is 0.984 for M=2 and 0.988 for M=3" uses $M$ for the order in a section where $M$ is the Mach number.
- References: [59] and [60] are the same work (Boscarino, Qiu, Russo & Xiong, JCP 392:594–618, 2019). [66] Ascher–Ruuth–Spiteri is printed with year 1982 (Appl. Numer. Math. 25 is 1997). [43] Lax–Wendroff is printed in "J. Comp. Phys., 13, 1960" (Comm. Pure Appl. Math.). [52] Osher–Solomon is printed "Math. Comput., 38, 1997" (vol. 38 is 1982). [6] Becker has garbled pages "321–1923". [13] "463472" and [57] "85104" are missing dashes. [34] Gresho–Chan has no venue or year, and [12] is "submitted" with no year. [4] (Einfeldt et al.) is cited for high-order semi-implicit DG on staggered meshes, which does not match its content. Many entries print rotated author lists (e.g. [1] "P. Lax A. Harten and B. van Leer", [58] "F. Filbet S. Boscarino and G. Russo"), a BibTeX separator error.

# Notation map

| Boscheri & Pareschi | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$, $t^n$ | $h$, $t_n$ | |
| $\varepsilon=\rho_0u_0^2/p_0$ | $\varepsilon$ | stiffness parameter $\propto$ Mach$^2$ (factor $\gamma$ unstated); not a step size |
| $\epsilon$ (Eq. 108) | kept | isentropic-vortex strength; **distinct from $\varepsilon$**, value unstated |
| $M$ | not used | **Mach number (§2.3, §4.3) and CWENO polynomial degree (§3.4.2, §4.3); the registry reserves $M$ for the mass matrix** |
| $Q$, $Q_E$, $Q_I$ | $y$, $y_{\mathrm E}$, $y_{\mathrm I}$ | state; explicit and implicit argument copies (page-local subscripts) |
| $H(Q_E,Q_I)$ | $\mathcal H(y_{\mathrm E},y_{\mathrm I})$ | partitioned right-hand side; **printed with the wrong sign (slips)** |
| $(\tilde c,\tilde A,\tilde b)$ | $(c^{\mathrm E},A^{\mathrm E},b^{\mathrm E})$ | **tilde marks the explicit tableau** |
| $(c,A,b)$ | $(c^{\mathrm I},A^{\mathrm I},b^{\mathrm I})$ | implicit tableau |
| $k_i$ | $\mathcal H(Y^{\mathrm E}_i,Y^{\mathrm I}_i)$ | stage derivatives, translated to stage values |
| $(s,\tilde s,p)$ | kept | implicit stages, explicit stages, order |
| $\delta$ | not used | diagonal $0.435866$ of (80), quoted by value; **$\delta$ is also the SSP3(4,3,3) coefficient 0.060424 and the Newton tolerance** |
| $\alpha,\eta$ (Eq. 81) | kept, page-local | SSP3(4,3,3) coefficients; $\eta$ is not the registry entropy and is also the viscous-flux coefficient (Eq. 101) |
| $k$ | kept | specific kinetic energy $\tfrac12u^2$; also the Newton iteration index |
| $h$ | $h_{\mathrm{enth}}$ | **specific enthalpy, collides with the registry step $h$** |
| $\gamma$ | $\gamma$ (ratio of specific heats) | only the EOS meaning here |
| $\lambda$, $\lambda_s$, $\lambda_v$ | kept | heat conductivity, CWENO linear weights, viscous eigenvalue; **not the Dahlquist $\lambda$** |
| SA, SSP | [stiff accuracy](/properties/stiff-accuracy.md), [SSP](/methods/strong-stability-preserving-runge-kutta.md) | no SSP coefficient is given |
| CFL | Courant number $\nu$ on the material speed | |

# Reference list

68 printed references, numbered [1]–[68], in roughly alphabetical order by BibTeX label. The list is merged complete into the [bibliography](/bibliography.md) with `citedby` boscheri-2021. Printed duplicate: [59] and [60] are the same Boscarino–Qiu–Russo–Xiong (2019) paper, folded into `boscarino-2019`. Many entries print rotated author lists (a BibTeX "and" error); they are keyed by the true first author, recovered from the printed string (e.g. [51], printed with Osher first, is `hofer-1976`). Printed years that disagree with the published works are merged under the published year: [66] Ascher–Ruuth–Spiteri (printed 1982) into `ascher-1997`, [52] Osher–Solomon (printed 1997) into `osher-1982`, [13] Brugnano–Casulli (printed 2007) into `brugnano-2008`. [34] has no venue or year, and [12] is "submitted" and kept as the pre-publication entry `boscheri-2021-b`, distinct from this source. No DOIs are printed.

# Pages created or updated

Chunk 3 (2026-10-19). This source is cited on:

* [Asymptotic-preserving scheme](/definitions/asymptotic-preserving-scheme.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [Gresho vortex](/benchmarks/gresho-vortex.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Semi-implicit and linearly implicit IMEX Runge–Kutta methods](/methods/semi-implicit-imex-runge-kutta.md)
* [Stiff accuracy](/properties/stiff-accuracy.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)

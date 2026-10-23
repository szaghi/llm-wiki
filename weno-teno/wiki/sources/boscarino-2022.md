---
type: Source
title: "Boscarino et al. (2022) — High Order Semi-implicit WENO Schemes for All-Mach Full Euler System of Gas Dynamics"
description: "An asymptotic-preserving and asymptotically accurate semi-implicit scheme for the full Euler equations at all Mach numbers: explicit material waves, implicit acoustic waves via one linear elliptic pressure equation per stage, new type-A stiffly accurate IMEX Runge–Kutta tableaux, and fifth-order finite-difference WENO."
resource: "doi:10.1137/21m1424433"
source_kind: paper
authors: [Boscarino S., Qiu J.-M., Russo G., Xiong T.]
year: 2022
venue: "SIAM J. Sci. Comput. 44:B368-B394"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_SIAM_Journal_on_Scientific_Computing_Boscarino_High_Order_Semi-implicit_WENO_Schemes_for_All-Mach_Full_Eule.pdf"
tags: [all-mach, asymptotic-preserving, imex, semi-implicit, weno]
timestamp: 2026-10-23T10:00:00Z
---

# Summary

The paper builds a high-order scheme for the non-dimensional full compressible Euler equations
with global Mach number $\varepsilon$, valid from compressible shocks ($\varepsilon=1$) to the
incompressible limit ($\varepsilon\to0$). It extends the authors' isentropic all-Mach scheme
(2019) to the full system, in which the pressure depends on every conserved variable.

The time discretization comes first. A [semi-implicit splitting](/methods/semi-implicit-all-mach-scheme.md)
treats the material waves (convective flux plus a fraction of the pressure) explicitly, and the
acoustic pressure term and the energy flux $\frac{E+p}{\rho}\rho v$ semi-implicitly. The
splitting parameter is fixed, unlike in Cordier, Degond and Kumbaro. The kinetic energy in the
equation of state is taken from explicit values, so each implicit stage needs only one linear
elliptic equation for the pressure perturbation $p_2=(p-\bar p)/\varepsilon^2$. High order in
time comes from a partitioned [IMEX Runge–Kutta](/methods/imex-runge-kutta.md) framework, with
new type-A (invertible implicit matrix), stiffly accurate tableaux SI-IMEX(4,4,3) and
SI-IMEX(3,3,2). The space discretization is fifth-order
[finite-difference](/definitions/conservative-finite-difference-scheme.md)
[WENO](/methods/weno-js-reconstruction.md) with global
[Lax–Friedrichs splitting](/methods/lax-friedrichs-flux.md). It is applied
[characteristic-wise](/methods/characteristic-decomposition.md) to the explicit flux and
component-wise to the implicit flux, and the elliptic operator uses a fourth-order compact
central difference.

The theory is time-semi-discrete with continuous space. The first-order scheme has
[asymptotic preservation](/properties/asymptotic-preservation.md) with an exactly
divergence-free leading-order velocity (Theorem 4.1). The high-order stiffly accurate scheme is
asymptotically accurate for well-prepared data (Prop. 4.4). The numerical tests show fourth to
fifth order, with order reduction at intermediate $\varepsilon$, on
[Sod and Lax tubes](/benchmarks/sod-and-lax-shock-tubes.md) and on
[2D Riemann problems](/benchmarks/two-dimensional-riemann-problems.md), where characteristic-wise
WENO on the explicit flux is needed to avoid oscillations. The
[Gresho vortex](/benchmarks/gresho-vortex.md) is run at $\varepsilon=10^{-1},10^{-2},10^{-6}$,
and an incompressible shear flow and a [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md)
flow at $\varepsilon=10^{-6}$. All tests use CFL 0.25 on the material speed. Recomputing the
third-order conditions from the printed SI-IMEX(4,4,3) coefficients finds one that fails
*(compiler check, not in the sources; see Key claims)*.

# Version read

arXiv 2106.02506v2 [math.NA], stamped 27 Oct 2021: an author version, not the SIAM typeset
version of record. It has 26 pages. The arXiv title writes "All Mach" where the published title
has "All-Mach"; the authors match (page 1 prints "Jing-Mei Qiu", Crossref "Qiu J."). The
published identity (SIAM J. Sci. Comput. 44(2), B368–B394) comes from Crossref. Section,
equation, table and figure numbers are those of the arXiv v2.

# Key claims

Registry notation, with page-local symbols (see the Notation map): $\varepsilon$ the global Mach
number, $c=\sqrt{\gamma p/\rho}$ the sound speed scaled by $\varepsilon$, $\alpha_{\mathrm s}$
the pressure-splitting parameter, $(\tilde c,\tilde A,\tilde b)$ and $(c,A,b)$ the explicit and
implicit Butcher tableaux, $\gamma_{\mathrm D}$ their diagonal coefficient, $p_2$ the pressure
perturbation.

1. The system is split as $\partial_tu=-\nabla\cdot\mathcal F_E-\nabla\cdot\mathcal F_{SI}$, with explicit material waves and implicit acoustic waves. This removes the acoustic restriction $\Delta t=O(\varepsilon\Delta x)$ at low Mach number (§3.1, Eqs. 3.10–3.11). **Derived**
2. The splitting parameter is fixed, $\alpha_{\mathrm s}=1$ for $\varepsilon<1$ and $\alpha_{\mathrm s}=1/\varepsilon^2$ for $\varepsilon\ge1$, whereas in Cordier–Degond–Kumbaro it depends on $\varepsilon$. For $\varepsilon\ge1$ the implicit pressure term vanishes and the update is explicit (§3.1). **Stated**
3. The density in the energy flux $\frac{E^n+p^n}{\rho^{n+1}}\rho v^{n+1}$ is taken at the new level. This is the second difference from Cordier–Degond–Kumbaro, and it "gives a better asymptotic preserving property" (§3.1, Remark 4.2). **Derived**
4. Linearizing the equation of state, $E_I=\frac{p_I}{\gamma-1}+\varepsilon^2\frac{\lvert\rho v_E\rvert^2}{2\rho_E}$, avoids nonlinear solves: each implicit stage reduces to one linear elliptic equation for $p_2$ (Eqs. 3.12, 3.19, 3.38). **Derived**
5. The first-order semi-implicit scheme (3.15) is the first-order type-A IMEX tableau (3.28) applied to the partitioned system (3.20) (Remark 3.1). **Derived**
6. Type A (invertible $A$, $a_{11}\ne0$) is "critical": it gives a pressure equation at the first stage and handles non-well-prepared data. With $a_{11}=0$ (ARS type) no proper $p_2$ exists at the first stage (§3.2.2). **Stated**
7. The AP and AA analysis needs the implicit part to be stiffly accurate; an A-stable stiffly accurate implicit part is L-stable (§3.2.2). **Stated** (cited)
8. With $\tilde b=b$ the explicit and implicit solutions coincide, so only one is stored; a different $\tilde b$ could give an embedded error estimate (§3.2.2). **Stated**
9. Two schemes are given: SI-IMEX(4,4,3) with $\gamma_{\mathrm D}=0.435866521508$, and SI-IMEX(3,3,2) with $\gamma_{\mathrm D}=1-\sqrt2/2$ and $\tilde a_{31}=-2\sqrt2/3$. Both have $c_i=\tilde c_i$ for $i\ge2$, and the third-order conditions of Pareschi and Russo are said to be "imposed" (Eqs. 3.30–3.31). **Stated** (the paper does not check the order; see below)
10. Fifth-order characteristic-wise WENO on $\mathcal F_E$ and component-wise WENO on $\mathcal F_{SI}$ is "optimal in compromising the need from both compressible and incompressible fluid solvers" (§3.3). **Shown** (Ex. 5.4)
11. The Lax–Friedrichs splitting speed is $a=\max\{\lvert v_1\rvert+\lvert v_2\rvert+\min(1,1/\varepsilon)\,c\}$, which excludes the fast acoustic speed for $\varepsilon<1$ (Eq. 3.32). **Stated**
12. Theorem 4.1: at leading order the time-discrete first-order scheme (4.43) gives $p_0^{n+1}$ constant in space and time and $\nabla\cdot v_0^{n+1}=0$, a consistent approximation of the incompressible Euler equations (2.6), so it is asymptotic-preserving (§4.1). **Proved** (formal expansion, continuous space, no-slip or periodic boundaries)
13. The scheme yields a discrete pressure Poisson equation, $\nabla\cdot\big(\frac{\rho_0^n}{\rho_0^{n+1}}(v_0^n\cdot\nabla)v_0^n\big)=-\nabla\cdot\big(\frac1{\rho_0^{n+1}}\nabla p_2^{n+1}\big)$, consistent with (2.8) because $\rho_0^n/\rho_0^{n+1}=1+O(\Delta t)$ (§4.1). **Derived**
14. The Cordier–Degond–Kumbaro scheme gives $\nabla\cdot v_0^{n+1}=O(\Delta t)$; scheme (3.15) gives $\nabla\cdot v_0^{n+1}=0$ exactly (Remark 4.2). **Derived**
15. Proposition 4.4: an SI-IMEX-RK scheme of order $r_{\mathrm{RK}}$ with stiffly accurate implicit part, applied to well-prepared data, gives $\lim_{\varepsilon\to0}p^1=p_*$ constant, $\lim_{\varepsilon\to0}\nabla\cdot v^1=0$ and a limit solution within $O(\Delta t^{r_{\mathrm{RK}}+1})$ of the incompressible one, i.e. the scheme is asymptotically accurate (§4.2, Eqs. 4.46–4.47). **Proved** (formal, by induction over stages)
16. Smooth 1D test (modified colliding pulses, $\varepsilon=10/11$, $t=0.1$): $L^1$ pressure errors $1.62\times10^{-2}$, $9.97\times10^{-4}$, $3.54\times10^{-5}$, $1.34\times10^{-6}$ for $N_x=40$–$320$, orders 4.02, 4.82, 4.72, "between 4 and 5, due to the dominance of spatial errors" (Table 5.1). **Shown**
17. Colliding acoustic pulses at $\varepsilon=1/11$, $t=1.63$, on 22 points: S4T3 matches the reference better than S2T2 (Fig. 5.1). **Shown**
18. Sod and Lax tubes ($\varepsilon=1$, $N_x=50$) are captured "without any observable numerical oscillations" by S2T2 and S4T3 (Fig. 5.2). **Shown**
19. 2D smooth test at $t=0.02$: about fourth order for $\varepsilon=1$ (4.05, 4.39) and fifth order for $\varepsilon=10^{-6}$ (5.34, 5.22), with order reduction at $\varepsilon=10^{-2}$ (errors $2.45\times10^{-3}$, $2.68\times10^{-3}$, $1.43\times10^{-3}$; order 0.91 on the last refinement) (Table 5.2, Fig. 5.3). **Shown**
20. Order degradation at intermediate Mach numbers is observed over $\varepsilon\in[10^{-6},1]$, from orders measured between $64^2$ and $128^2$ (Fig. 5.3). **Shown** (no explanation is given)
21. 2D Riemann problems ($400^2$, $\varepsilon=1$): approach A1 ($\alpha_{\mathrm s}=1$, characteristic-wise WENO on $\mathcal F_E$) is closest to the reference without obvious oscillations. A2 (component-wise everywhere) and A3 (no splitting, component-wise) oscillate in the middle region. S2T2 lies between, closer to A1, with poorer resolution: "the importance of characteristic reconstructions" (Ex. 5.4, Figs. 5.4–5.5). **Shown**
22. Gresho vortex ($100^2$, $200^2$; $\varepsilon=10^{-1},10^{-2},10^{-6}$): both schemes keep the vortex shape relatively well over 2 periods, S4T3 slightly better. Kinetic energy is "well maintained", S4T3 clearly better than S2T2 on $100^2$, with smaller differences on $200^2$, especially for small $\varepsilon$ (Ex. 5.5, Fig. 5.6). **Shown**
23. Incompressible shear flow and Kelvin–Helmholtz at $\varepsilon=10^{-6}$: the vorticity is comparable to the isentropic results of the 2019 scheme; the $L^\infty$ divergence error grows in time and jumps when fine structures are no longer resolved (Ex. 5.6, Fig. 5.7). **Shown**
24. For incompressible or weakly compressible flows without initial discontinuities, high-order linear reconstructions "would perform better than WENO reconstructions in preserving the divergence and in resolving solution structures" (Ex. 5.6). **Stated** (the divergence comparison is in Fig. 5.7; the resolution claim is not shown)
25. The semi-implicit kinetic-energy treatment of Boscheri and Pareschi (3.29) "may produce slightly better error in some test cases" and is overall comparable; the results are not reported (Remark 3.2). **Stated**
26. $\Delta t=\mathrm{CFL}\,\Delta x/a$ with CFL 0.25 in all tests; for $\varepsilon<1$, $a$ does not involve the acoustic speed (§5). **Stated**

**Order conditions of SI-IMEX(4,4,3)** *(compiler check, not in the sources)*. The tableau (3.30)
was re-read on the page image (arXiv v2, p. 9): $\tilde c=(0,\gamma_{\mathrm D},0.717933260754,1)$,
explicit rows $(\gamma_{\mathrm D})$, $(0.435866521508,\ 0.282066739245)$,
$(-0.733534082748750,\ 2.150527381100,\ -0.416993298352)$; implicit $c=(\gamma_{\mathrm D},\gamma_{\mathrm D},0.717933260754,1)$
with rows $(\gamma_{\mathrm D})$, $(0,\gamma_{\mathrm D})$, $(0,0.282066739245,\gamma_{\mathrm D})$,
$(0,1.208496649176,-0.644363170684,\gamma_{\mathrm D})$; and
$b=\tilde b=(0,1.208496649176,-0.644363170684,\gamma_{\mathrm D})$. The rows sum to $\tilde c$
and $c$. With these coefficients, $\sum_ib_i=1$, $b^\top c=b^\top\tilde c=\tfrac12$,
$b^\top(c\circ c)=b^\top(\tilde c\circ\tilde c)=b^\top(c\circ\tilde c)=\tfrac13$ and
$b^\top Ac=b^\top A\tilde c=b^\top\tilde Ac=\tfrac16$ hold to about $10^{-12}$, and the implicit
part is stiffly accurate with $R(\infty)=0$. But $b^\top\tilde A\tilde c=0.19885\ne\tfrac16$. The
difference from $b^\top\tilde Ac$ is $\gamma_{\mathrm D}\sum_ib_i\tilde a_{i1}=-0.0322$: imposing
$c_i=\tilde c_i$ only for $i\ge2$ does not carry the condition over, because $c_1\ne\tilde c_1$
and $\tilde a_{i1}\ne0$. That condition is the third-order condition of the explicit tableau on
its own, so as printed either a coefficient is misprinted or the explicit–explicit coupling is
only second order. The paper never measures the temporal order alone (Table 5.1 is dominated by
the spatial error). The SI-IMEX(3,3,2) tableau satisfies $b^\top c=\tilde b^\top\tilde c=\tfrac12$
exactly.

# Printed slips

- Table 5.2, $\varepsilon=1$, $N=32$: the error is printed $4.64\times10^{-3}$, with order 4.05 on the next refinement, but $\log_2(4.64\times10^{-3}/2.82\times10^{-5})=7.36$. An error of $4.64\times10^{-4}$ would give 4.04, so the printed order is consistent with an exponent slip in the error *(compiler check, not in the sources)*. The orders of Table 5.1 recompute correctly *(compiler check, not in the sources)*.
- Gresho pressure (5.9), middle branch: printed $2(r/R)^2-4(2r/R+\log(r/R))+6$. Integrating the radial balance $\partial_rp_2=\rho u_\theta^2/r$ with $\rho=1$, $u_\theta=2(1-r/R)$ and $p_2(R)=0$ gives $2(r/R)^2-4(2r/R-\log(r/R))+6$. Only this form is continuous at $r=R/2$ with the printed inner branch $2(r/R)^2+2-\log16$: both equal $\tfrac52-\log16$, whereas the printed middle branch gives $\tfrac52+\log16$ *(compiler check, not in the sources)*.
- Proof of Prop. 4.4, unnumbered equation after (4.58): printed $p_{0,I}^{(i)}=p_*+\Delta t\,\gamma p_*a_{ii}\nabla\cdot v_{0,I}^{(i)}$. The line above, with $E_{0,I}^{(i)}=p_{0,I}^{(i)}/(\gamma-1)$, gives a minus sign, consistent with (4.52). The conclusion is unaffected.
- (3.37)–(3.38) print the second-order operator as $\nabla(\bar H^{(i)}\nabla p)$, without the divergence dot of (3.18) and (3.35c). The label (3.37) is printed twice.
- In (3.30) the $\tilde b$ row of the explicit tableau carries a spurious "0" in the $\tilde c$ column.
- Prop. 4.4 writes "$\Omega\subset\mathbb R$" for a multi-dimensional analysis, and "zero Neumann condition" while the proof uses no-slip or periodic boundaries. The proof says "In order to prove the theorem" for a proposition and cites (3.24b) where the stage energy equation is (3.35c).
- (5.6) has an unmatched parenthesis "(0.5323, 1.206, 0, 0.3))". (3.35c) writes $\nabla\cdot$ where (3.40) writes $\nabla_W\cdot$, and $\bar H_i$ for $\bar H^{(i)}$. The shear-flow amplitude $\delta$ and layer thickness are not given. "Asymtotic" (p. 16).

# Notation map

| Boscarino et al. 2022 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\varepsilon$ | $\varepsilon$ (page-local) | global Mach number of the non-dimensionalization, as on the asymptotic-preservation page; not the WENO $\epsilon$ |
| $\rho$, $\mathbf u=(u,v)$, $\mathbf q=\rho\mathbf u$, $E$, $p$ | $\rho$, $v=(v_1,v_2)$, $\rho v$, $E$, $p$ | velocity $u$ translated to $v$ |
| $E=\frac p{\gamma-1}+\frac{\varepsilon^2}2\rho\lvert\mathbf u\rvert^2$ | scaled form of $E$ | |
| $\gamma$ (gas) | $\gamma$ | $=1.4$ |
| $\gamma$ (Eqs. 3.30, 3.31) | $\gamma_{\mathrm D}$ (local) | **collision**: diagonal coefficient of the implicit tableau |
| $c_s=\sqrt{\gamma p/\rho}$ | $c$ | sound speed multiplied by $\varepsilon$; the physical acoustic speed is $c/\varepsilon$ |
| $p_0$, $p_2$; $\mathbf u_0$, $\mathbf u_1$ | — | terms of the $\varepsilon$ expansion; $p_2$ hydrodynamic pressure |
| $p_{I,2}=(p_I-\bar p_E)/\varepsilon^2$ | $p_2$ | pressure perturbation; $\bar p_E$ the spatial mean |
| $\mathcal F_E$, $\mathcal F_{SI}$ | — (local) | explicit and semi-implicit fluxes |
| $\alpha$ | $\alpha_{\mathrm s}$ (local) | **collision** with the DG–FV blending coefficient $\alpha$ |
| subscripts $E$, $I$ | — | explicitly and implicitly treated values; $E$ is not the total energy here |
| $(\tilde c,\tilde A,\tilde b)$, $(c,A,b)$, $(s,\sigma,p)$ | — (local) | Butcher tableaux and (implicit stages, explicit stages, order); **collisions**: $A$ (flux Jacobian), $c$ (sound speed), $p$ (pressure) |
| $\delta=-2\sqrt2/3$ | $\tilde a_{31}$ of SI-IMEX(3,3,2) | |
| $r$ (Prop. 4.4) | $r_{\mathrm{RK}}$ | order of the Runge–Kutta method |
| $H^n=(E^n+p^n)/\rho^{n+1}$, $\bar H^{(j)}$ | — (local) | enthalpy-like coefficient; not the registry's specific total enthalpy |
| $\mathcal H(U_E,U_I)$ | — (local) | partitioned right-hand side |
| $\nabla_{CW}$, $\nabla_W$ | — (local) | characteristic-wise and component-wise FD-WENO divergence |
| $\Lambda$ | $a$ | Lax–Friedrichs splitting speed and CFL speed |
| S4T3, S2T2, WENO5RK3 | — | scheme labels; S2T2 uses second-order TVB reconstruction with $M=1$ |
| $M_{\rm ratio}$ | — | local Mach ratio of the Gresho test (5.10) |
| $\omega=v_x-u_y$ | vorticity | not a WENO weight |

# Reference list

The arXiv v2 prints 51 references, numbered [1]–[51] and sorted alphabetically (SIAM style,
titles printed). The list is merged complete into the [bibliography](/bibliography.md), with
`citedby` including `boscarino-2022`. Ref. [9] has no volume. [31] is a set of summer-school
lecture notes, [42] a book chapter, [49] a NASA contractor report and [50] an Inria thesis. The
repeated-author dashes of [29], [31], [33] and [43] were expanded to the preceding author list.
No item is unparseable.

# Pages created or updated

Chunk 4 (2026-10-23), cited further in chunks 5–6 (2026-10-23). This source is cited on:

* [Asymptotic preservation](/properties/asymptotic-preservation.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Gresho vortex](/benchmarks/gresho-vortex.md)
* [IMEX Runge–Kutta schemes](/methods/imex-runge-kutta.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)

---
type: Source
title: "Chen et al. (2023) — High order asymptotic preserving finite difference WENO schemes with constrained transport for MHD equations in all sonic Mach numbers"
description: "Extends the semi-implicit IMEX Runge–Kutta finite-difference WENO all-Mach framework to ideal MHD with vector-potential constrained transport: one linear elliptic pressure equation per stage, a capped Lax–Friedrichs speed, formal proofs of asymptotic preservation and asymptotic accuracy, and tests from sonic Mach 1 to 0."
resource: "doi:10.1016/j.jcp.2023.112240"
source_kind: paper
authors: [Chen W., Wu K., Xiong T.]
year: 2023
venue: "J. Comput. Phys. 488:112240"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Journal_of_Computational_Physics_Chen_High_order_asymptotic_preserving_finite_difference_WENO_sche.pdf"
tags: [asymptotic-preserving, all-mach, semi-implicit, mhd, finite-difference, weno]
timestamp: 2026-10-23T12:00:00Z
---

# Summary

The paper extends the
[semi-implicit all-Mach scheme](/methods/semi-implicit-all-mach-scheme.md) of
Boscarino, Qiu, Russo and Xiong, a semi-implicit
[IMEX Runge–Kutta](/methods/imex-runge-kutta.md) finite-difference WENO scheme,
to the ideal MHD equations at all sonic Mach numbers $\varepsilon\in[0,O(1)]$.
It combines it with the constrained transport of Christlieb, Rossmanith and
Tang, which evolves a magnetic vector potential in the Weyl gauge so that the
[magnetic field is divergence-free](/properties/divergence-free-magnetic-field.md).
In the non-dimensional system the pressure enters the momentum flux as
$p/\varepsilon^2$ and the fast speed grows like $\varepsilon^{-1}$. Explicit
schemes therefore need $\Delta t=O(\varepsilon\Delta x)$ and carry $O(\varepsilon^{-1})$
upwind dissipation.

The flux is split into an explicit part (convective and magnetic fluxes, the
constrained-transport source and the $\varepsilon^2$ magnetic energy flux) and
an implicit acoustic part. With a linearized equation of state, each implicit
stage reduces to one linear elliptic equation for the pressure perturbation
$(p-\bar p)/\varepsilon^2$. Space is discretized by fifth-order
[finite-difference WENO](/methods/weno-js-reconstruction.md):
[characteristic-wise](/methods/characteristic-decomposition.md) for the
convective flux, component-wise for the other fluxes, and Jiang–Peng
Hamilton–Jacobi WENO for the vector potential. A fourth-order compact central
difference discretizes the elliptic operator. The
[Lax–Friedrichs splitting](/methods/lax-friedrichs-flux.md) speed uses the
capped sound speed $\min(1/\varepsilon,1)\sqrt{\gamma p/\rho}$, so the
dissipation and the time step do not depend on $\varepsilon$ for $\varepsilon<1$.

The theory is formal and semi-discrete in time. Theorem 4.1 proves the
first-order scheme [asymptotic preserving](/properties/asymptotic-preservation.md)
towards incompressible MHD; Theorem 4.2 proves asymptotic accuracy of the
order-$r$ scheme when its implicit part is stiffly accurate. Tests (third-order
stiffly accurate scheme, CFL 0.25): accuracy on the
[circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)
in 1D and 2D; $\varepsilon$-range accuracy tests, with order reduction at
$\varepsilon=10^{-2}$; a [Brio–Wu-type shock tube](/benchmarks/brio-wu-shock-tube.md);
the [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md); an
[MHD blast wave](/benchmarks/mhd-blast-wave.md) with divergence error
$2.87\times10^{-11}$; field-loop advection with a CPU comparison against an
explicit WENO constrained-transport scheme; and a magnetized
[Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md) at
$\varepsilon=10^{-6}$.

# Version read

arXiv preprint arXiv:2211.16655v1 [math.NA], 30 Nov 2022 (stamp on page 1),
not the JCP version of record, which can differ in wording, numbering, tests or
timings; 27 pages, all read by text extraction, pp. 10 and 17 also visually.
Title and authors match Crossref; the file prints no DOI. Equation, table and
example numbers cited here are those of the arXiv v1.

# Key claims

Registry notation (see the notation map): sonic Mach number $\varepsilon$
(page-local, as on the semi-implicit page), velocity $v$, momentum $\rho v$,
vector potential $\mathsf A$ (2D component $\mathsf A_3$), Lax–Friedrichs speed
$a$, implicit Butcher coefficients $\mathsf a_{ij}$.

1. For non-dimensional ideal MHD, explicit shock-capturing schemes need $\Delta t=\mathrm{CFL}\,\Delta x/\max_l\lvert\lambda_l\rvert=O(\varepsilon\Delta x)$, and standard upwind viscosity scales as $\varepsilon^{-1}$ (§2.2). **Derived**
2. Formal asymptotics with well-prepared data give the incompressible MHD limit: $d\rho_0/dt=0$, $p_0$ constant, $\nabla\cdot v_0=0$, $\nabla\cdot B=0$, with $p_2$ the incompressible pressure (§2.3, Eqs. 2.8–2.13). **Derived** (after earlier work; incompressible-limit theory **Stated**)
3. Constrained transport: $B=\nabla\times\mathsf A$ with $\partial_t\mathsf A+(\nabla\times\mathsf A)\times v=0$ (Weyl gauge) gives $\nabla\cdot B=0$ identically (§2.4, Eqs. 2.15–2.17). **Derived** (background)
4. The first-order semi-implicit scheme (3.1) needs one linear elliptic equation (3.5) for $p_2^{n+1}$ per step and no nonlinear solve (§3.1). **Derived**
5. For $\varepsilon\ge1$ a switch on the pressure terms ($\alpha_p=1$ for $\varepsilon<1$, $1/\varepsilon^2$ for $\varepsilon\ge1$) removes the implicit pressure term and the scheme becomes explicit (§3.1). **Stated**
6. The high-order scheme is a partitioned semi-implicit IMEX-RK with a DIRK implicit part; stiff accuracy $b_j=\mathsf a_{sj}$ makes the update equal to the last stage (§3.2, Eqs. 3.7–3.10). **Stated**
7. Fifth-order WENO is applied characteristic-wise to the convective flux, component-wise to the magnetic energy and implicit acoustic fluxes, and as Jiang–Peng WENO with a Lax–Friedrichs Hamiltonian to the vector-potential equation (§3.3). **Stated**
8. The splitting speed uses $\hat c=\min(1/\varepsilon,1)\sqrt{\gamma p/\rho}$ inside the fast speed (Eq. 3.12), so the dissipation coefficient $a$ and the time step are independent of $\varepsilon$ for $\varepsilon<1$ (§3.3, §5). **Stated** (design choice; effect **Shown**)
9. At small $\varepsilon$ the true eigenvectors "will make such a spectral characteristic decomposition to be unstable"; the eigenvectors at $\varepsilon=1$ are used instead, "which works well from our numerical results" (§3.3). **Stated** (no analysis)
10. The operator $\nabla\cdot(\bar H\nabla p_2)$ is kept continuous in the substitution and discretized by a compact fourth-order central difference (§3.4, Eq. 3.18; §5). **Stated**
11. Theorem 4.1: the first-order scheme (3.1), continuous in space, is asymptotic preserving: with well-prepared data it is at leading order a consistent discretization of incompressible MHD (§4.1). **Proved** (formal)
12. Theorem 4.2: an order-$r$ semi-implicit IMEX-RK scheme with stiffly accurate implicit part, well-prepared data and periodic or compact-support boundaries gives $\lim_{\varepsilon\to0}p^1=p^*$ (constant), $\lim_{\varepsilon\to0}\nabla\cdot v^1=0$, $\nabla\cdot B^1=0$ and $\lim_{\varepsilon\to0}V^1=V_{\mathrm{inc}}(\Delta t)+O(\Delta t^{r+1})$: asymptotic accuracy (§4.2, Eqs. 4.5–4.6). **Proved** (formal, induction over stages)
13. Example 5.1 (1D circularly polarized Alfvén wave, $\varepsilon=1$, $T=1$, $\Delta t\propto\Delta x^{5/3}$): fifth order, $L^1$ error of $\rho v_2$ $6.27\times10^{-10}$ at $N=160$, order 5.00 (Table 5.1). **Shown**
14. Example 5.2 (1D $\varepsilon$-range, $\gamma=1.4$, $T=0.05$): orders near 5 for $\varepsilon=1$ (4.94 at $N=160$), $10^{-6}$ and $0$ (4.72 at $N=160$); order reduction at $\varepsilon=10^{-2}$ (2.78, 1.11, 1.72, 1.60), called "typical behavior of high-order IMEX schemes for these multi-scale problems" (Table 5.2). **Shown**
15. Example 5.4 (2D Alfvén wave rotated by $\pi/4$, $\varepsilon=1$): order 5.00 for $\rho v_1$ and 4.13 for $B_1$ at $128^2$ in $L^1$, the latter because $B=\nabla\times\mathsf A$ uses a fourth-order central difference (Table 5.3). **Shown**
16. Example 5.5 (2D $\varepsilon$-range, $T=0.01$): high order for $\varepsilon=1$, $10^{-6}$ and $0$ (5.00, 5.70, 5.73 at $N=128$); order degeneracy at $\varepsilon=10^{-2}$, with errors 2.09e-03, 2.09e-03, 2.41e-03 at $N=16,32,64$ (Table 5.4). **Shown**
17. Example 5.7 (MHD blast wave, $200^2$, $\varepsilon=0.9$, $T=0.02$): maximum discrete divergence error $2.87\times10^{-11}$, against $2.77\times10^{-11}$ for the explicit constrained-transport scheme (§5.2). **Shown**
18. Example 5.8 (field-loop advection, $256\times128$, $T=\sqrt5$): CPU seconds IMEX / explicit with constrained transport are 7634.880 / 4736.466 at $\varepsilon=0.5$, 5687.467 / 19719.964 at $\varepsilon=0.1$ and 8015.959 / 38666.192 at $\varepsilon=0.05$ (Table 5.5; hardware not stated). **Shown**
19. Example 5.8: at $256\times128$ the IMEX scheme keeps the symmetric density-deviation structure better than the explicit scheme, which needs $384\times192$ to match; magnetic-pressure profiles are almost identical, and both schemes "slightly distort the profile at $y=0.15$" (§5.2, Fig. 5.6). **Shown**
20. Example 5.9 (magnetized Kelvin–Helmholtz, $\varepsilon=10^{-6}$, $256\times128$, $T=0.8$): vorticity and Mach-ratio fields are "comparable to" earlier all-Mach results, which the authors take as verification of the AP property (Fig. 5.7). **Shown** (qualitative)
21. All 2D solutions keep $\nabla\cdot B=0$ "up to machine round off errors" (§5.2). **Shown** (quantified for Example 5.7 only)
22. In 1D $\nabla\cdot B=0$ holds automatically, and the conservative $B$ equation (3.6) replaces constrained transport (§3.1, §5.1). **Stated**
23. The explicit reference schemes (fifth-order WENO with SSP-RK3, without and with constrained transport) use the same capped speed (3.11)–(3.12), which "leads to much better results" at low sonic Mach number (§5). **Stated**
24. "To our best knowledge, there are very few AP schemes for MHD systems in literature" (§1). **Stated**

# Printed slips

- §3.3: the conservative finite-difference form is printed $(v_i)_t=\frac1{\Delta x}(\hat f_{i+1/2}-\hat f_{i-1/2})$, without the minus sign.
- Theorem 4.2 states a bounded domain $\Omega\subset\mathbb R$ for a multidimensional scheme.
- Example 5.9 prints the velocity as $1-2\eta(x)$ while the profile function is defined in $y$.
- The symbol $\alpha$ is both the pressure switch of §3.1 and the Lax–Friedrichs speed of §3.3.
- §1: "shallow water equations in all Fraude numbers" (Froude). Example 5.4: "applied on all both directions".
- The tableau of the third-order stiffly accurate scheme used in every test is not printed, and neither are the linear solver of the elliptic equation nor the hardware of Table 5.5.

# Notation map

| Chen et al. (2023-b) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\varepsilon$ | $\varepsilon$ (page-local) | sonic Mach number $u_0\sqrt{\rho_0/p_0}$, as on the [semi-implicit page](/methods/semi-implicit-all-mach-scheme.md); not the WENO $\epsilon$ |
| $\rho$, $\mathbf u=(u,v,w)$, $\mathbf B$, $E$, $p$ | $\rho$, $v=(v_1,v_2,v_3)$, $B$, $E$, $p$ | |
| $\mathbf q=\rho\mathbf u$ | $\rho v$ | |
| $\mathbf A$, $A_z$ | $\mathsf A$, $\mathsf A_3$ (page-local) | vector potential; **$A$ is the flux Jacobian in the registry** |
| $a$, $c_a$, $c_f$, $c_s$ | $c$, kept | dimensionless sound speed $\varepsilon^{-1}\sqrt{\gamma p/\rho}$; Alfvén, fast and slow speeds |
| $\hat a$, $\hat c_f$ | $\hat c$, $\hat c_f$ | capped speeds of Eq. (3.12) |
| $\alpha$ (§3.3) | $a$ | global Lax–Friedrichs speed $\max_k(\lvert v_k\rvert+\hat c_f^{(k)})$ |
| $\alpha$ (§3.1) | $\alpha_p$ (page-local) | pressure switch; **same symbol in the source** |
| $p_0$, $p_2$, $\rho_0$, $\mathbf u_0$ | kept | terms of the $\varepsilon$ expansion; the source reuses $\rho_0$, $p_0$ for reference scales |
| $H^n$, $H_I$, $\bar H$ | $H$ | linearized specific total enthalpy $(E+p)/\rho$ |
| $\tilde A$, $\tilde b$, $\tilde c$; $A$, $b$, $c$ | kept; $\mathsf a_{ij}$, $b$, $c$ | explicit and DIRK tableaux; stiffly accurate: $b^\top=e_s^\top A$ |
| $s$, $r$ | kept | number of stages, order; **$r$ is the WENO stencil size in the registry** |
| $\Phi_{\rm WENO5}$, $f_i^\pm$ | WENO5, $f^\pm$ | finite-difference flux reconstruction with Lax–Friedrichs splitting |
| $R$, $L$, $w_j$, $g_j$ | $R$, $L$, $\zeta$, kept | eigenvectors at the arithmetic mean, characteristic variables and fluxes |
| $H_T$, $\hat H_T$, $\beta$ | kept, $\beta_{\mathrm{HJ}}$ (page-local) | Hamiltonian, Lax–Friedrichs numerical Hamiltonian; **$\beta_k$ is a smoothness indicator in the registry** |
| $\eta(y)$ (Ex. 5.9) | page-local | shear-layer profile; **$\eta$ is the entropy in the registry** |
| $M_a$ | $M$ | local sonic Mach number |

# Reference list

63 printed references in alphabetical numbered style ([1]–[63], with titles),
all merged complete into the [bibliography](/bibliography.md) with `citedby`
`chen-2023-b`. Ref. [42] (Leidi et al.) is an arXiv preprint and ref. [59]
(Wu, Jiang & Shu, SIAM J. Numer. Anal.) is "in press, 2022"; both are kept in
pre-publication form. Ref. [8] is the bundle's `boscarino-2022`; ref. [30]
(Huang, Xing & Xiong, JCP 463:111255) is a different work from the bundle's
`huang-2022` and was re-keyed. Same-author same-year pairs are suffixed in
printed order (Dai 1998, Wu 2018, Jin 2022). No printed duplicates or
unparseable items.

# Pages created or updated

Chunk 5 (2026-10-23), cited further in chunks 6–8 (2026-10-23). This source is cited on:

* [Asymptotic preservation](/properties/asymptotic-preservation.md)
* [Brio–Wu MHD shock tube](/benchmarks/brio-wu-shock-tube.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [IMEX Runge–Kutta schemes](/methods/imex-runge-kutta.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Magnetic field-loop advection](/benchmarks/field-loop-advection.md)
* [MHD blast wave and rotor](/benchmarks/mhd-blast-wave.md)
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)
* [Semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md)

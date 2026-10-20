---
type: Source
title: "Birke et al. (2024) — A Well-Balanced Semi-implicit IMEX Finite Volume Scheme for Ideal Magnetohydrodynamics at All Mach Numbers"
description: "Combines a convective/pressure flux split, a two-stage semi-implicit IMEX Runge–Kutta method whose implicit stage is one linear pressure equation, and deviation well-balancing into a second-order finite-volume scheme for ideal MHD with gravity whose step is Mach-independent."
resource: "doi:10.1007/s10915-023-02422-z"
source_kind: paper
authors: [Birke C., Boscheri W., Klingenberg C.]
year: 2024
venue: "J. Sci. Comput. 98:34"
local_file: "/home/stefano/papers/mosaic/ode-integration/2024_Crossref_Journal_of_Scientific_Computing_Birke_A_Well-Balanced_Semi-implicit_IMEX_Finite_Volume_Scheme_for.pdf"
tags: [imex, asymptotic-preserving, implicit-stage-solvers, structure-preserving, cfd]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper builds a second-order, semi-implicit, well-balanced finite-volume scheme for the 3D ideal MHD equations with a gravitational source, aimed at low-Mach flows such as deep convective layers of stars. The flux is split into a *convective* part (all transport and magnetic terms, plus the source) and a *pressure* part (pressure gradient in momentum, enthalpy flux in energy). The convective part is explicit: a Godunov-type finite-volume method with a Rusanov flux whose dissipation uses only convective eigenvalues, and minmod-limited reconstruction. The pressure part is implicit, with dissipation-free central differences. Freezing the enthalpy at $t_n$ and writing the kinetic energy as $\tfrac12(\rho u)^n(\rho u)^{n+1}/\rho^{n+1}$ turns the implicit part into one **linear** elliptic equation for $p^{n+1}$. It is solved by GMRES, with no Picard or fixed-point iteration (see [implicit-stage solvers](/methods/implicit-stage-solvers.md)). The step then obeys a CFL condition on the convective eigenvalues only, independent of the Mach number.

Second order in time comes from a two-stage [IMEX Runge–Kutta](/methods/imex-runge-kutta.md) method written in the [semi-implicit](/methods/semi-implicit-imex-runge-kutta.md) form $y'=\mathcal H(y_{\mathrm E},y_{\mathrm I})$ of Boscarino, Filbet & Russo, with the LSDIRK2(2,2,2) pair of Pareschi & Russo ($\gamma=1-1/\sqrt2$). Well-balancing follows Berberich et al.: the scheme evolves the deviation $\Delta\mathbf q=\mathbf q-\tilde{\mathbf q}$ from a known magnetohydrostatic equilibrium $\tilde{\mathbf q}$ and reconstructs only the deviation. A staggered constrained-transport step after the explicit stage keeps the discrete divergence at machine precision. Theorem 1 proves that a discrete equilibrium is preserved to machine precision.

The numerical tests are a Sod tube with gravity, 1D and 2D Euler and 2D MHD equilibria preserved with exactly zero error and zero GMRES iterations, and perturbations of size $10^{-10}$ that only the well-balanced variant resolves. A gravitational Euler vortex at Mach $10^{-1},\dots,10^{-5}$ shows Mach-independent dissipation. The abstract calls the time stepping [asymptotic preserving](/definitions/asymptotic-preserving-scheme.md), but the paper gives no low-Mach asymptotic analysis.

# Version read

arXiv:2306.16286v1 [math.NA], 28 Jun 2023, typeset in the Springer JSC submission template ("will be inserted by the editor", "Received: date / Accepted: date"). This is the submitted manuscript, not the version of record. It has 24 pages. Title (sentence case) and authors match Crossref. Equation, section, table and reference numbers cited here are those of arXiv v1.

# Key claims

Notation: $h$ is the step and $\varepsilon=\lvert\mathbf v\rvert/c$ is the Mach number (source $\mathcal M$). The tableaux are $(A^{\mathrm E},b^{\mathrm E},c^{\mathrm E})$ and $(A^{\mathrm I},b^{\mathrm I},c^{\mathrm I})$, and the source's enthalpy $h$ is written $h_{\mathrm{enth}}$. MHD symbols are those of the source (Gaussian units).

1. Splitting the flux into convective $\mathbf F^c$ and pressure $\mathbf F^p$ parts (Eq. 8) gives a convective sub-system with eigenvalues $u\pm\sqrt{\mathbf B^2/4\pi}$, $u\pm B_x/\sqrt{4\pi}$, $0$ (Eq. 9b), and a pressure sub-system with eigenvalues $\tfrac12(u\pm\sqrt{u^2+4c^2})$ and six zeros (Eq. 10b). (§2.2) **Stated** (eigenvalues given without derivation)
2. Treating the pressure sub-system implicitly makes the step restriction depend only on the convective eigenvalues (Eq. 11), hence independent of the Mach number. (§2.2) **Derived**
3. The gravitational source can go into the explicit (convective) sub-system, because it does not change the eigenvalues and poses no low-Mach difficulty. (§2.2, Introduction) **Stated**
4. Freezing the enthalpy at $h_{\mathrm{enth}}^n$ in the energy flux and writing the kinetic energy as $(\rho k)^{n+1}=\tfrac12(\rho u)^n(\rho u)^{n+1}/\rho^{n+1}$ (Eq. 22) makes the implicit part linear. A single linear elliptic pressure equation (Eq. 25 in 1D, Eq. 41 in 3D) is solved per implicit stage, without any fixed-point iteration, "differently from [16,18]" (Dumbser et al. 2019; Fambri 2021). (§3.1) **Derived**
5. The pressure system is solved by GMRES with a tolerance of typically $10^{-12}$. (§3.1) **Stated**
6. The scheme is in flux form and therefore locally and globally conservative. (§3.1) **Stated**
7. No numerical dissipation is added in the implicit part, "even in the case of shock waves"; the Rusanov dissipation $s_{\max}$ uses only convective eigenvalues and is independent of the Mach number. (Introduction, §3.2, Eqs. 28, 31) **Stated**
8. Second order in time comes from the IMEX Runge–Kutta method LSDIRK2(2,2,2) of Pareschi & Russo [29] (Table 1, $\gamma=1-1/\sqrt2$, $c^{\mathrm E}_2=1/(2\gamma)$), used in the semi-implicit stage form (Eqs. 33a–34). "The only implicit evaluation lies in (33c)", which is the pressure equation. (§3.3.1) **Stated** (order taken from [29]; no temporal convergence test is shown)
9. Second order in space comes from minmod-limited piecewise linear reconstruction (Eqs. 36–37) of the deviation only; the implicit central operators (Eq. 31) are already second order. (§3.3.2) **Stated**
10. Reconstructing only $\Delta\mathbf q$, while evaluating $\tilde{\mathbf q}$ exactly at interfaces, "is essential for the well-balancing". (§3.2, Eq. 29) **Stated** (used in Theorem 1)
11. The constrained-transport method of Gardiner & Stone [21], applied directly after the explicit update, keeps the discrete divergence (Eq. 45) at machine accuracy, and this "is checked and validated at each time step". (§3.5) **Stated** (no divergence plot shown)
12. **Theorem 1:** if $\mathbf q^n_{i,j,k}=\tilde{\mathbf q}_{i,j,k}$ in all cells, the fully discrete scheme of §§3.1–3.5 preserves the solution up to machine precision. (§3.6) **Proved** (the uniqueness of the solution $p^{n+1}=\tilde p$ of the reduced pressure system (Eq. 49) is asserted, not proved)
13. Setting $\tilde{\mathbf q}=0$ recovers the non-well-balanced semi-implicit scheme. (§3.7, §4) **Stated**
14. Sod shock tube with gravity $g_x=-1$, 100 cells, $t_f=0.2$: good agreement with an explicit second-order reference on 20000 cells, showing shock capability outside the low-Mach regime. (§4.1, Fig. 1) **Shown**
15. 1D Euler steady state (Eq. 53), $t_f=1$, without $\tilde{\mathbf q}$: the equilibrium is kept only to second order, $L^1(\rho)=2.1451\times10^{-3}$, $4.2949\times10^{-4}$, $1.0332\times10^{-4}$, $2.7888\times10^{-5}$ for $N_x=20,40,80,160$, EOC 2.32, 2.19, 2.08. (Table 2) **Shown**
16. The same test with $\tilde{\mathbf q}$ equal to the initial data gives all $L^1$ errors $0.0000\times10^{0}$, 0 GMRES iterations and residual $0.0000\times10^{0}$ for $N_x=20,\dots,160$. (§4.2, Table 3) **Shown**
17. The 2D isothermal Euler atmosphere (Eq. 54) and the 2D MHD equilibrium (Eq. 56), $t_f=1$, grids $20^2$ to $160^2$, give all $L^1$ errors exactly zero, 0 iterations and residual 0. (§§4.3, 4.5, Tables 4–5) **Shown**
18. Perturbed equilibria (Eqs. 55, 57) on $64\times64$, $t_f=0.15$: with amplitude $10^{-1}$ both variants resolve the perturbation; with amplitude $10^{-10}$ only the well-balanced variant does. (§§4.4, 4.6, Figs. 2–3) **Shown**
19. Gravitational Euler vortex (data of Thomann et al. [32]), $40\times40$, $t_f=1.26$ (one turn), maximum Mach $10^{-1},\dots,10^{-5}$: no qualitative difference between Mach numbers (Fig. 4). The kinetic-energy loss depends on the grid ($N=20,40$) but not on the Mach number ($10^{-3},10^{-4}$) (Fig. 5), "indicat[ing] that the numerical dissipation is independent of the Mach number". (§4.7) **Shown**
20. The time-stepping algorithm is "asymptotic preserving (AP)". (Abstract, keywords) **Stated** (no low-Mach asymptotic analysis and no proof that the $\varepsilon\to0$ limit is a consistent incompressible discretization; the only evidence is claim 19)
21. All tests use the CFL condition (Eq. 11) with CFL $=0.9$. (§4) **Stated**

*(Compiler checks, not in the sources.)* LSDIRK2(2,2,2) has $b^{\mathrm E}=b^{\mathrm I}=(1-\gamma,\gamma)$ and satisfies the order-2 conditions, including the coupling conditions $b^{\mathrm E\top}c^{\mathrm I}=b^{\mathrm I\top}c^{\mathrm E}=\tfrac12$. Its implicit part is the L-stable, [stiffly accurate](/properties/stiff-accuracy.md) two-stage [SDIRK](/methods/diagonally-implicit-runge-kutta.md) with invertible $A^{\mathrm I}$. The explicit part is not stiffly accurate, since its last row $(c^{\mathrm E}_2,0)\ne b^{\mathrm E}$, so the pair is not globally stiffly accurate. The paper states none of these properties beyond order 2. Theorem 1 is proved for the first-order step; its extension to the two-stage method rests on each stage having the same structure. The nonsingularity of the non-symmetric pressure matrix (Eq. 49) is assumed.

# Printed slips

- **Eq. (11), p. 5** (checked visually): printed $h\le\mathrm{CFL}\,\min_\Omega\dfrac{\max\lvert\lambda^c\rvert}{\min(\Delta x,\Delta y,\Delta z)}$. The fraction is inverted relative to Eq. (7) and is dimensionally wrong; $\min(\Delta x,\Delta y,\Delta z)/\max\lvert\lambda^c\rvert$ is meant.
- §3.3.1: "LSDIRK(2,2,2)" in the text against "LSDIRK2(2,2,2)" in the next sentence and the Table 1 caption.
- Eq. (33b): $\mathbf q_I^i=\mathbf q_E^n+\dots$ uses $\mathbf q_E^n$ (harmless, since $\mathbf q_E^n=\mathbf q_I^n=\mathbf q^n$). The stage arguments for $i=1$ are not defined, although (33c) runs over $1\le i\le s$.
- Eqs. (32)–(34): $\mathcal H=+\partial_x\mathbf F^c+\partial_x\mathbf F^p+\mathbf S$ with $\mathbf q^{n+1}=\mathbf q^n+h\sum_ib_i\mathbf k_i$. For $\partial_t\mathbf q+\partial_x\mathbf F=\mathbf S$ the flux terms should carry a minus sign.
- Eq. (43): the first electric-field difference prints $\Delta E_{i+1/2,j-1/2,k}$ without the $z$ subscript.
- §3.7, steps 1 and 5: the staggered index "$\mathbf B_{z,i,k,k+1/2}$" is printed for $\mathbf B_{z,i,j,k+1/2}$. Step 6 cites the 1D pressure equation (25) where the 3D one (41) is meant.
- Proof of Theorem 1, Eq. (48): $(\Delta\mathbf v)^*$ is listed instead of the momentum deviation $(\Delta\rho\mathbf v)^*$.
- §4.2–§4.3: the text calls the residual "of the size of the machine accuracy", while Tables 3–5 print exactly $0.0000\times10^{0}$. The Table 5 caption says "different numbers of cells $N_x$" for $(N_x,N_y)$ columns.
- Ref. [34] (Varma & Chandrashekar 2019) prints "Computers & Fluids, 281:292–313, 2019"; volume 281 does not fit a 2019 issue.
- Typos: "propsed" (p. 2), "differently form" (p. 7), "constained" (p. 12), "magnethydrostatic", "graviatational", "defintions".

# Notation map

| Birke et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$, $t^n$ | $h$, $t_n$ | |
| $\mathcal M=\lvert\mathbf v\rvert/c$, $\mathcal M_{\max}$ | $\varepsilon$ | Mach number, the stiffness parameter of the AP property |
| $\mathbf q$, $\mathbf q_E$, $\mathbf q_I$ | $y$, $y_{\mathrm E}$, $y_{\mathrm I}$ | state; explicit and implicit argument copies (page-local) |
| $\mathcal H(\mathbf q_E,\mathbf q_I)$ | $\mathcal H(y_{\mathrm E},y_{\mathrm I})$ | partitioned right-hand side; **printed with the wrong sign (slips)** |
| $(\hat c,\hat A,\hat b)$ | $(c^{\mathrm E},A^{\mathrm E},b^{\mathrm E})$ | **hat marks the explicit tableau** (the registry's $\hat b$ is the embedded weight) |
| $(c,A,b)$ | $(c^{\mathrm I},A^{\mathrm I},b^{\mathrm I})$ | implicit tableau |
| $\mathbf k_i$ | $\mathcal H(Y^{\mathrm E}_i,Y^{\mathrm I}_i)$ | stage derivatives, translated to stage values |
| $\gamma=1-1/\sqrt2$ | $\gamma$ | SDIRK diagonal; **the source also uses $\gamma$ for the ratio of specific heats** |
| $\beta=1/(2\gamma)$ | $c^{\mathrm E}_2$ | explicit abscissa |
| $h$ | $h_{\mathrm{enth}}$ | **specific enthalpy, collides with the registry step $h$** |
| $c$ | kept (sound speed) | **collides with the abscissae $c$** |
| $\tilde{\mathbf q}$, $\Delta\mathbf q$, $\bar{\mathbf q}$ | kept | equilibrium, deviation, reassembled state $\Delta\mathbf q+\tilde{\mathbf q}$ |
| $\hat{\mathbf F}$ | kept | numerical flux (hat also marks the explicit tableau) |
| $\lambda^{\mathrm{MHD}},\lambda^c,\lambda^p$ | kept | eigenvalues of the full, convective and pressure sub-systems; **not the Dahlquist $\lambda$** |
| $\eta$ | kept, page-local | perturbation amplitude; **not the registry entropy $\eta$** |
| $m$ | kept | magnetic energy $\mathbf B^2/8\pi$ |
| CFL | $\nu$ | on the convective eigenvalues |
| LSDIRK2(2,2,2) | kept | (implicit stages, explicit stages, order) |

# Reference list

35 printed references, numbered [1]–[35], alphabetical. The list is merged complete into the [bibliography](/bibliography.md) with `citedby` birke-2024. [8] is Boscheri & Pareschi, JCP 434:110206, the ingested source [Boscheri & Pareschi (2021)](/sources/boscheri-2021.md). [19] (Fambri et al., "ArXiV.") prints no year, venue or identifier and is kept as the preprint entry `fambri-2024`, distinct from the published `fambri-2023`. [10] (Boscheri & Tavelli 2022) and [20] (Gaburro, Castro & Dumbser 2021) are `boscheri-2022-b` and `gaburro-2021-c`, because the bibliography already held other works under those keys; the three Boscheri 2023 works [6], [7], [9] take `boscheri-2023`, `-b`, `-c` in printed order. [34] prints volume 281 for a 2019 Computers & Fluids paper, kept as printed. No DOIs are printed, and there are no printed duplicates or unparseable items.

# Pages created or updated

Chunk 3 (2026-10-19). This source is cited on:

* [Asymptotic-preserving scheme](/definitions/asymptotic-preserving-scheme.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [Semi-implicit and linearly implicit IMEX Runge–Kutta methods](/methods/semi-implicit-imex-runge-kutta.md)
* [Sod shock tube](/benchmarks/sod-shock-tube.md)

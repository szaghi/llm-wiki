---
type: Method
title: "Tensor-train WENO"
description: "Tensor-train WENO evolves the fields of a three-dimensional finite-difference WENO5-JS Euler solver in low-rank tensor-train format, with shift operators for differences, cross interpolation for the nonlinear flux and weight steps, rounded SSP-RK3 and a mesh-dependent truncation tolerance; it keeps fifth order and is fast on low-rank flows."
status: established
aliases: [WENO-TT, TT-WENO, tensor-train WENO scheme, LF-cross, WENO-cross, TT-SSPRK3]
tags: [weno, finite-difference, reconstruction, software]
timestamp: 2026-10-24T06:00:00Z
---

# Tensor-train WENO

**Tensor-train WENO** (WENO-TT; [Danis et al. (2025)](/sources/danis-2025.md), arXiv v1 read)
is an implementation layer, not a new reconstruction: the fifth-order
[conservative finite-difference](/definitions/conservative-finite-difference-scheme.md)
[WENO-JS](/methods/weno-js-reconstruction.md) scheme for the 3D Euler equations is run with
every 3D array (conserved variables, split fluxes, reconstructed interface fluxes) stored
and advanced in **tensor-train (TT) format**, a low-rank separated representation. Linear
operations act on the small TT cores; the nonlinear steps of the scheme, which have no
explicit TT algorithm, are done by cross interpolation of an ordinary element-wise routine.
The authors present it as the first finite-difference WENO scheme in TT form for
compressible flow (Abstract).

## Baseline scheme

The "full-tensor" (FT) reference is component-wise WENO5-JS with global
[Lax–Friedrichs splitting](/methods/lax-friedrichs-flux.md) $f^\pm=\tfrac12(f\pm au)$, the
Jiang–Shu indicators, linear weights $\tfrac1{10},\tfrac35,\tfrac3{10}$ (most upwind to most
downwind), $q=2$ and $\epsilon=\Delta x^2$ following Don & Borges, dimension by dimension
without characteristic projection, and SSP-RK3 (§2.2, Eqs. (5)–(10); §5.8). The paper numbers
its stencils from the downwind side; the registry's $S_0$ is its $S_2$.

## Tensor-train representation

As recalled from Oseledets (§3, Eqs. (11)–(14)), a 3D array is approximated by

$$X(i,j,k)\approx\sum_{l_1=1}^{\mathsf r_1}\sum_{l_2=1}^{\mathsf r_2}\mathfrak G_1(1,i,l_1)\,\mathfrak G_2(l_1,j,l_2)\,\mathfrak G_3(l_2,k,1),$$

with cores $\mathfrak G_1,\mathfrak G_2,\mathfrak G_3$, summation indices $l_1,l_2$ and TT ranks
$[\mathsf r_1,\mathsf r_2]$ (page-local symbols; the source's $G_k$, $\alpha_k$, $r_k$, renamed to
keep the registry's admissible set $G$, weights $\alpha_k$ and stencil size $r$), "a discrete
separation of variables". **TT rounding** recompresses a TT to lower ranks with relative
error at most $\varepsilon_{\mathrm{TT}}$ (page-local tolerance) by a QR sweep and a truncated-SVD
sweep. **Cross interpolation** (AMEn, from the MATLAB TT-Toolbox) builds a TT of a function
from element evaluations only, to a relative tolerance $\varepsilon_{\mathrm{cross}}$.

## The TT finite-difference scheme

- **Differences by shifts** (§4.1, Eqs. (15)–(19)). With shift operators $T^x,T^y,T^z$
  (page-local), $\hat f^{(1)}_{i+1/2,j,k}=T^x\hat f^{(1)}_{i-1/2,j,k}$, the semi-discrete scheme becomes
  $\partial_tu+\frac1{\Delta x}(T^x-1)\hat f^{(1)}+\frac1{\Delta y}(T^y-1)\hat f^{(2)}+\frac1{\Delta z}(T^z-1)\hat f^{(3)}=0$,
  $\hat f^{(d)}$ the numerical flux in direction $d$;
  in TT form each shift acts on one core only.
- **LF-cross** (§4.2, Algorithm 1). The split fluxes need $1/\rho$, $\sqrt{\cdot}$, $\lvert\cdot\rvert$
  and $\max$, for which the authors know no explicit TT algorithm (§4.1). One AMEn cross
  interpolation of the element-wise Lax–Friedrichs routine returns all ten split-flux
  components (five variables, two signs) as one TT with an extra index of size 10; this is
  stated to be "∼30 % faster" than two separate cross interpolations (no data shown). Computing
  fluxes and weights by TT arithmetic with rounding after each operation lost "significant
  performance" and was abandoned (stated).
- **WENO-cross** (§4.3, Algorithm 2). For each direction, variable and side, the input is the
  set of five shifted copies $T^{-2}v,\dots,T^{2}v$ of the split flux $v$, and the element-wise
  WENO5-JS routine is cross-interpolated as a whole: ten cross interpolations per direction
  for the Euler system. Cross-interpolating each division inside the weights separately is
  slow because $\beta_k=O(\Delta x^2)$ in smooth regions and $O(1)$ at jumps, so the
  unnormalized weights vary over many orders; the whole-routine approach avoids rounding and
  is "significantly more robust", which the authors attribute to the output staying close
  to the stencil values by the [ENO property](/definitions/eno-property.md).
- **TT-SSPRK3** (§4.4, Eqs. (21)–(22)). Each forward-Euler step and each convex combination
  of [SSP-RK3](/methods/ssp-runge-kutta.md) is followed by TT rounding,
  $\mathcal F(u)=\mathrm{round}\big(u+\Delta t\,\mathcal L(u),\varepsilon_{\mathrm{TT}}\big)$.
- **Boundary conditions** (§4.5, Eqs. (23)–(30)). Three ghost points per side; periodic,
  inflow/outflow and symmetry conditions are set by editing the ghost slices of the core of
  the normal direction and adding rank-1 TT corrections followed by rounding.

## Choice of the tolerance

To keep the TT truncation error below the $O(\Delta x^5)$ discretization error in the
unnormalized $L^2$ norm, $\|v\|_{L^2}=\Delta x^{3/2}\|v\|_F$ on a uniform grid, the authors
use the triangle inequality with the assumption $\|u_{\mathrm{TT}}-u_{\mathrm{FT}}\|_F\le\varepsilon_{\mathrm{TT}}\|u_{\mathrm{TT}}\|_F$,
which gives $\varepsilon_{\mathrm{TT}}\le C\Delta x^{7/2}/\|u_{\mathrm{TT}}\|_F$, and set (§4.6,
Eqs. (32)–(35))

$$\varepsilon_{\mathrm{TT}}=\varepsilon_{\mathrm{cross}}=\frac{C_\varepsilon V^{1/2}\Delta x^{7/2}}{\max_c\|u_c\|_F},$$

with $V$ the domain volume, the maximum over the five conserved variables $u_c$ (page-local index $c$), and a
problem-dependent constant $C_\varepsilon$ (page-local): 500 for linear advection, 10 for
Burgers and the manufactured solution, $2/\sqrt V$ for the isentropic vortex. The assumption
that the accumulated TT–FT difference is bounded by one rounding estimate is not proved.

## Results

All runs are serial MATLAB; the hardware is not stated (§5).

- **Order** (Tables 1–4). 3D linear advection, 3D Burgers, the
  [isentropic vortex](/benchmarks/isentropic-vortex.md) on a 3D mesh and a trigonometric
  [manufactured solution](/definitions/method-of-manufactured-solutions.md) all converge at
  fifth order in TT form, with errors matching FT: e.g. advection at $320^3$, $L^2$ error
  $5.45\times10^{-10}$ (TT) against $5.50\times10^{-10}$ (FT); Burgers order 4.96 at $320^3$.
  On the vortex $C_\varepsilon=1/\sqrt V$ and $2/\sqrt V$ keep FT accuracy, while $100/\sqrt V$
  and $500/\sqrt V$ "become almost 4th-order" with larger errors; $2/\sqrt V$ also keeps the
  exact solution's TT ranks (Fig. 4). On the manufactured solution, whose exact ranks are 3 for
  $\rho$, 5 for the momenta and 7 for $\rho E$, $C_\varepsilon=100$ drops $\rho E$ to fourth
  order on the finest grid.
- **Speed and memory** (Figs. 5, 7, 9). Against the FT solver, TT is as fast at $40^3$ and
  102 times faster at $320^3$ on the vortex, about 35 ($C_\varepsilon=10$) to "slightly less
  than 65" ($C_\varepsilon=100$) times on the manufactured solution at $320^3$, and "more than
  1000" times on a Sod tube in a 3D box at $640^3$, where the FT timings at $320^3$ and $640^3$
  are **extrapolated**. Memory compression reaches about $10^{-4}$ (vortex, density) and below
  $10^{-5}$ (Sod).
- **Shocks** (§§5.5–5.8). The [Sod](/benchmarks/sod-and-lax-shock-tubes.md),
  [Shu–Osher](/benchmarks/shu-osher-problem.md), [double Mach reflection](/benchmarks/double-mach-reflection.md)
  and [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) results agree with FT
  visually. Cross interpolation fails on the double-Mach initial condition, which is built
  instead as a rounded sum of $N_y$ rank-1 TTs, with initial rank about $N_y\cot(\pi/3)$, and the
  ranks grow further as the flow evolves; Rayleigh–Taylor also suffers rank growth.

The authors conclude that low-rank problems benefit, that a global $\varepsilon_{\mathrm{TT}}$ is a
limitation for localized features, and suggest, without testing, a domain decomposition with
local tolerances (§5.8, §6).

## Qualifications

- **The 1000-fold figure** of the abstract and conclusions rests on extrapolated FT timings for
  a rank-1, effectively one-dimensional problem; the speed-ups on genuinely 3D low-rank
  solutions are 35–102.
- **Attainable cross accuracy.** At the finest manufactured-solution grid the rule demands
  $\varepsilon_{\mathrm{cross}}\approx1.2\times10^{-12}$, while AMEn cross "usually stagnates at
  about an error of $10^{-11}$" (§5.4).
- **Component-wise reconstruction.** The Rayleigh–Taylor results are said to agree
  "excellently" with characteristic-wise results of other papers, by visual comparison only.
- **Printed slips** (arXiv v1). The double-Mach initial condition, Eq. (41), is printed as
  "$x<\tfrac16$", independent of $y$, while the text describes an oblique shock whose position
  changes with $y_j$; §5.7 puts the supersonic inflow on the right and the outflow on the left;
  the Fig. 11 caption gives $T=2$ against $T=0.2$ in the text. Eq. (29) lacks a "+" between two
  kinetic-energy terms, Eq. (38) writes the fourth argument of the manufactured fields as $y$
  for $t$, and §5.4 lists the exact rank of $\rho v_1$ twice, as 3 and as 5. The introduction describes WENO-Z as a modification of the smoothness indicators;
  [WENO-Z](/methods/weno-z.md) changes the weights through a global indicator and keeps the
  Jiang–Shu indicators.

# Citations

- [Danis et al. (2025)](/sources/danis-2025.md) — Abstract; §2.2, Eqs. (5)–(10); §3, Eqs. (11)–(14); §4.1–4.6, Eqs. (15)–(35), Algorithms 1–2; §5, Tables 1–4, Figs. 4–12; §6 (arXiv v1).

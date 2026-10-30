---
type: Source
title: "Zheng et al. (2021) — A high order conservative finite difference scheme for compressible two-medium flows"
description: "Fifth-order conservative finite-difference scheme for two-medium flows: alternative-formulation WENO on characteristic primitive variables, level-set interface tracking, cell merging with a low-order interface flux, and a smooth discontinuity indicator that blends low- and high-order fluxes, with accuracy propositions."
resource: "doi:10.1016/j.jcp.2021.110597"
source_kind: paper
authors: [Zheng F., Shu C.-W., Qiu J.]
year: 2021
venue: "J. Comput. Phys. 445:110597"
local_file: "/home/stefano/papers/mosaic/weno-teno/2021_Crossref_Journal_of_Computational_Physics_Zheng_A_high_order_conservative_finite_difference_scheme_for_compr.pdf"
tags: [multiphase, alternative-weno, finite-difference, interface-capturing, troubled-cell, weno]
timestamp: 2026-10-22T12:00:00Z
---

# Summary

The paper builds a fifth-order
[conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
for compressible two-medium flows (gas–gas with the $\gamma$-law, gas–water with the
[stiffened-gas](/definitions/stiffened-gas-equation-of-state.md) "Tait" law) in 1D and 2D.
It is motivated by the [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md):
ghost-fluid and related interface methods are not conservative. Conservative schemes that
reconstruct fluxes or conserved variables produce pressure and velocity oscillations at a
material interface.

The scheme has four parts. (i) The [alternative formulation of WENO](/methods/alternative-weno.md):
a two-point [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md) on interpolated interface
states plus central $\Delta x^2f_{xx}$ and $\Delta x^4f_{xxxx}$ corrections. The fifth-order
WENO interpolation ([WENO-JS](/methods/weno-js-reconstruction.md) weights) acts on primitive
variables in the [characteristic fields](/methods/characteristic-decomposition.md) of the
primitive system, which a flux-reconstruction FD scheme cannot do. (ii) A
[level set](/methods/level-set-method.md) tracks the interface, and each fluid keeps its own
nodal values. (iii) Near the interface, cells are merged, and a low-order flux $\hat f^L$ comes
from an ALE-type space–time balance with the interface flux $(0,p,v_1p)$. It is blended with
the high-order flux as $\hat f=\hat f^L+\varphi(\hat f^H-\hat f^L)$. Here $\varphi$ is a
discontinuity indicator ([troubled-cell indicators](/definitions/troubled-cell-indicator.md))
built from [smoothness indicators](/definitions/smoothness-indicator.md) and a
[WENO-Z](/methods/weno-z.md)-type global $\tau$. (iv) The mixed-cell value is redistributed
to the two fluids, again blended by $\varphi$. Time stepping is
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md), with each stage written as one conservative
update from $u^n$.

Propositions 2.1–2.3 give the accuracy budget, $\varphi=1+O(\Delta x^5)$ with
$\Delta t=O(\Delta x^r)$, $r\le2$. The indicator is $1+O(\Delta x^6)$ on smooth data and
$O(\Delta x^4)$ at a jump. Tests: fifth order on [Burgers-reducible](/benchmarks/burgers-equation-tests.md)
artificial-interface problems, a two-medium [Shu–Osher problem](/benchmarks/shu-osher-problem.md),
[gas–water Riemann problems](/benchmarks/gas-liquid-riemann-problems.md) and 2D
[shock–bubble interactions](/benchmarks/shock-bubble-interaction.md).

# Version read

Version of record (Elsevier typeset, © 2021, DOI printed on page 1, available online
30 July 2021), 31 pages. Title, authors, venue and DOI match page 1 and Crossref. No
identity problem. Equation, table and figure numbers are those of the journal version.

# Key claims

Local symbols (see the Notation map): $\Phi$ level set, $\phi_i$ fluid-I volume fraction of a
cell, $\varphi_{i+1/2}$ discontinuity indicator, $p_\infty$ stiffening pressure, $f_s$ interface
flux.

1. The scheme is conservative: the computational variables are updated by a flux difference, (5)/(29), and both the assembly of the computational variable from the two fluids' nodal values and its redistribution conserve the total (§2.3, §3.2). **Derived**
2. Reconstructing fluxes or conserved variables across a material interface puts jumps in every component and spoils $v$ and $p$. Finite-volume methods above second order, and flux-reconstruction FD, cannot interpolate primitive variables; the alternative FD formulation [14] can (§1). **Stated**
3. Local characteristic decomposition has "a reduced effect at the interface", whose characteristic structure is unclear with two fluids on its sides (§1). **Stated**
4. The alternative flux (1), $\hat f_{i+1/2}=h(u^-_{i+1/2},u^+_{i+1/2})-\frac1{24}\Delta x^2f_{xx}\vert_{i+1/2}+\frac7{5760}\Delta x^4f_{xxxx}\vert_{i+1/2}$, with the 6-point central differences (2)–(3), gives a fifth-order conservative FD scheme (§2.1, recalled from [25]). **Stated**
5. Proposition 2.1: the flux (6), which multiplies both corrections by $\varphi_{i+1/2}$, satisfies $(\hat f_{i+1/2}-\hat f_{i-1/2})/\Delta x=f(u)_x\vert_{x_i}+O(\Delta x^5)$ if $\varphi_{i\pm1/2}=1+O(\Delta x^3)$ (§2.2.4, Eq. 25). **Proved** (assumes a Lipschitz flux and $u^\pm=u+O(\Delta x^5)$)
6. Proposition 2.2: the blend (16) of $\hat f^H$ and $\hat f^L$ satisfies (26) if $\varphi=1+O(\Delta x^5)$ and $\Delta t=O(\Delta x^r)$, $r\le2$ (§2.2.4; Appendix A). **Proved**
7. Proposition 2.3: the redistribution (19)–(20) is fifth-order accurate for both fluids if $\varphi=1+O(\Delta x^4)$ (§2.2.4). **Proved** (one case; the others "similar")
8. The low-order fluxes next to the interface stencil are only first order, and the middle flux $\hat f^L_{i_n+1/2}$ of (14) is "at least zero order", $O(\Delta x^{2-r})$ (Appendix A). **Proved**
9. Combined requirement on the indicator: $\varphi_{i+1/2}=1+O(\Delta x^5)$ together with $\Delta t=O(\Delta x^r)$, $r\le2$ (§2.2.4, p. 11). **Derived**
10. The indicator $\varphi_{i+1/2}=\big(1/(\bar\beta+1)\big)^2$, with $\tau=\frac14\sum_{r'=1}^4(\beta_0-\beta_{r'})^2$ and $\bar\beta=\frac14\sum_{r'=1}^4\tau/(\beta_{r'}+\epsilon)$ over a 6-point stencil and four 3-point stencils, satisfies $0\le\varphi\le1$, $\varphi=1+O(\Delta x^6)$ on smooth data and $\varphi=O(\Delta x^4)$ when the stencil contains a discontinuity (§2.2.4; Appendix B). **Proved** (Taylor expansion written as $\beta_{r'}=u'(x_{i+1/2})^2\Delta x^2\big(1+O(\Delta x^2)\big)$, which takes $u'(x_{i+1/2})\neq0$ and $\epsilon$ negligible; neither assumption is stated)
11. The mass of each component is conserved in the interface average (10), because the first component of the interface flux $f_s$ is zero (§2.2, p. 5). **Derived**
12. CFL number 0.5 in 1D and 2D; the accuracy tests use $\Delta t=O(\Delta x^{5/3})$ so that the spatial error dominates (§2.2, §3.1, §4). **Stated**
13. 1D artificial-interface accuracy test ($\gamma=3$, identical fluids, full interface algorithm on): density errors converge at fifth order, $L_1$ from 1.05E-05 ($N_x=80$) to 1.07E-08 ($N_x=320$), last order 5.14 (Table 2). **Shown**
14. The indicator itself converges at about sixth order in that test: $L_1$ error 1.30E-07 ($N_x=80$) to 3.67E-11 ($N_x=320$), order 5.98 (Table 3). **Shown**
15. 2D artificial-interface test: fifth order, $L_1$ error 9.57E-06 ($80\times80$) to 1.24E-08 ($320\times320$), order 5.06 (Table 4). **Shown**
16. Pure 1D contact (Ex. 2): the interface moves at the correct speed; velocity and pressure deviations are roughly $10^{-11}$–$10^{-10}$, against about $10^{-4}$–$10^{-3}$ for conservative-variable WENO-JS (read off the log plot) (§4, Fig. 6). **Shown**
17. 2D pure interface (Ex. 9): "no oscillations other than those at the round-off error" in velocity and pressure (§4, Fig. 12). **Shown**
18. Two-medium shock–sine-wave problem (Ex. 3): the scheme and WENO-JS are "nearly the same", comparable to the DG scheme of [6] with fewer degrees of freedom (§4, Fig. 7). **Shown**
19. Strong shock on a gas–gas interface (Ex. 4): an FD-WENO-based original ghost-fluid method misplaces the shock front and the interface; the proposed scheme does not (§4, Fig. 8). **Shown**
20. Gas–water Riemann problem I (Ex. 5): correct interface location, with "a small trough along the interface in the density plot" compared with [6] (§4, Fig. 9). **Shown**
21. Gas–water Riemann problem III (Ex. 7): WENO-JS "produces a jump at the interface"; the proposed scheme places the interface correctly (§4, Fig. 11). **Shown**
22. 2D air shock on a helium bubble and underwater shock on a gas bubble ($280\times240$ cells): the "main features … correctly captured" in "high resolution" (§4, Figs. 14–15). **Shown** (qualitative, no reference solution)
23. CPU times for Examples 1–7: 64.30, 2.71, 1.40, 2.37, 2.27, 0.55, 0.43 s (Table 1), with no hardware, compiler or grid stated. **Shown**
24. The mixture rules $1/(\gamma-1)=\phi/(\gamma^I-1)+(1-\phi)/(\gamma^{II}-1)$ and the analogous rule for $\gamma p_\infty/(\gamma-1)$ are used only to plot mixed cells and "do not participate in the computation of time evolution" (§4). **Stated**
25. Interface-tracking methods (GFM, MGFM, real GFM, interface treatment, single-fluid, path-conservative) are non-conservative, so convergence to weak solutions is not assured; conservative schemes "tend to give oscillatory results if no special care is taken" [32] (§1). **Stated**

# Printed slips

- §3.1.5, p. 19: the reinitialization stops when "$e_1<\Delta\tau\Delta x\Delta y$ or $k\le20$"; as a stopping criterion "$k\le20$" is inverted (an iteration cap would be $k\ge20$).
- Appendix A redefines $\alpha^*_I=x(t^*)-x_{i_n-1/2}$ and $\alpha^n_I$ as lengths, while $\alpha$ is a volume fraction everywhere else (Eq. 4); the identity "$\alpha^*_I=\alpha^n_I+u\Delta t+O(\Delta x^5)$" holds only for the length meaning.
- Appendix A: "the flux $\hat F^L_{i+1/2}$, $i=i_n\pm1$, is only first order accurate"; the fluxes meant are at $x_{i_n-1/2}$ and $x_{i_n+3/2}$.
- The indicator's smoothness indicators are written $\sum_{k=1}^5$ for every $r$, although $p_1,\dots,p_4$ are quadratics and only $k=1,2$ contribute (harmless).
- The $\epsilon$ of the discontinuity indicator is not stated ($\varepsilon=10^{-6}$ is given only for the WENO weights).
- References [19] and [30] carry swapped titles, and [30] the wrong volume. [19] (Peng, Merriman, Osher, Zhao, Kang, J. Comput. Phys. 155:410–438, 1999) is printed with the title "A level set approach for computing solutions to incompressible two-phase flow". [30] (Sussman, Smereka, Osher) is printed as "A PDE-based fast local level set method", J. Comput. Phys. 134:146–159, 1994 *(compiler check, not in the sources: Crossref gives Peng et al. 1999 as "A PDE-Based Fast Local Level Set Method", 155:410–438, and Sussman et al. 1994 as "A Level Set Approach for Computing Solutions to Incompressible Two-Phase Flow", 114:146–159)*.

# Notation map

| Zheng et al. 2021 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $F(U)$, $G(U)$ | $u$, $f$, $g$ | conserved variables and fluxes |
| $u$, $v$ (velocity) | $v_1$, $v_2$ | |
| $\rho$, $p$, $E$, $c$, $\gamma$ | agree | |
| $\bar p$ | $p_\infty$ (registry §10 $p_{\infty,k}$) | stiffening pressure of the stiffened-gas ("Tait") law |
| $U^{n,I}_i$, $U^{n,II}_i$, $U^n_i$ | nodal values of fluid I, II; computational variable | two-fluid storage |
| $\alpha_i$ (volume fraction) | $\phi_i$ (registry §10 $\phi_k$, here indexed by cell) | **collision** with the unnormalized weights $\alpha_k$ |
| $\alpha$ (in the LF flux) | $a$ | maximum wave speed |
| $\phi$ (level set) | $\Phi$ (local) | renamed to free $\phi$ |
| $\varphi_{i+1/2}$ | $\varphi_{i+1/2}$ (local; $\varphi_{\mathrm D}$ on the [level-set page](/methods/level-set-method.md)) | discontinuity indicator; **collision** with the GQL constraint $\varphi_i$ of §10, a different family |
| $u^-_{i+1/2}$, $u^+_{i+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | minus = left state; agrees (the source's wording is "right and left limits") |
| $\hat F(U^-,U^+)$ | $h^{\mathrm{LF}}(u^-,u^+)$ | global or local not specified |
| $\hat F^H$, $\hat F^L$, $\hat F_s$ | $\hat f^H$, $\hat f^L$, $f_s$ (local) | high-order, low-order interface, interface flux $(0,p,v_1p)$ |
| $\gamma_k$ (linear weights) | $d_k$ | position-dependent at a general $x$; $1/16,5/8,5/16$ at $x_{i+1/2}$ *(compiler check, not in the sources)*; **collision** with $\gamma$ |
| $\bar\omega_k$, $\omega_r$ | $\alpha_k$, $\omega_k$ | $q=2$, $\epsilon=10^{-6}$ |
| $\beta_r$, $\tau$ | $\beta_k$, $\tau$ | $\tau$ is a mean of squared differences over a 6-point stencil, not $\tau_5$ |
| $\beta$ (unindexed) | $\bar\beta$ (local) | mean of $\tau/(\beta_{r'}+\epsilon)$ |
| $W$, $A(W)$, $R$, $L$ | primitive variables, primitive Jacobian, $R$, $L$ | characteristic projection of the primitive system |
| $\mathcal L$ | $\mathcal L$ | agree |
| $N$ | $N_x$ | number of grid intervals |

# Reference list

The paper prints 35 references, numbered [1]–[35] and sorted alphabetically by first author,
with no DOIs. The list is merged complete into the [bibliography](/bibliography.md), with
`citedby` including `zheng-2021`. Fedkiw 1999 [8]/[9] take suffixes in printed order. Ref. [6]
(Cheng et al. 2020, DG for two-medium flows) needs a disambiguated key, because `cheng-2020`
already holds a different work. Refs. [19] and [30] are recorded with the printed titles and
a note on the swap (see Printed slips). No item is unparseable.

# Pages created or updated

Chunk 2 (2026-10-22), cited further in chunks 3–12 (2026-10-22/30). This source is cited on:

* [Alternative WENO (A-WENO)](/methods/alternative-weno.md)
* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)
* [Level-set and ghost-fluid interface methods](/methods/level-set-method.md)
* [Positivity-preserving flux limiter (Hu–Adams–Shu)](/methods/positivity-preserving-flux-limiter.md)
* [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
* [WENO-Z weights](/methods/weno-z.md)

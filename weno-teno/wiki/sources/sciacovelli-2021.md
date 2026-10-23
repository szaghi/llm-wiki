---
type: Source
title: "Sciacovelli et al. (2021) — Assessment of a high-order shock-capturing central-difference scheme for hypersonic turbulent flow simulations"
description: "Finite-difference central scheme with a ninth-order Jameson-type adaptive scalar dissipation and a three-factor shock sensor (Bhagatwala–Lele, Ducros, Jameson), assessed on shock tubes, a real-gas reacting shock tube, an underexpanded jet, compressible Taylor–Green vortices and supersonic and hypersonic boundary layers as DNS and implicit LES."
resource: "doi:10.1016/j.compfluid.2021.105134"
source_kind: paper
authors: [Sciacovelli L., Passiatore D., Cinnella P., Pascazio G.]
year: 2021
venue: "Comput. Fluids 230:105134"
local_file: "/home/stefano/papers/mosaic/weno-teno/2021_Crossref_Computers_amp_Fluids_Sciacovelli_Assessment_of_a_high-order_shock-capturing_central-differenc.pdf"
tags: [central-scheme, finite-difference, numerical-dissipation, troubled-cell, turbulence, implicit-les]
timestamp: 2026-10-22T12:00:00Z
---

# Summary

The paper assesses a [conservative finite-difference](/definitions/conservative-finite-difference-scheme.md)
central scheme with high-order adaptive [artificial dissipation](/methods/artificial-viscosity.md)
for DNS and implicit LES of high-speed, possibly reacting, turbulent flows. The starting
point is the Lerat–Corre family of odd-order schemes, order $2P+3$ on $2(P+2)+1$ points:
a central flux of order $2(P+2)$ plus a dissipation $\propto\delta^{2P+3}u$, whose
leading truncation error is an even derivative and hence dissipative. The authors
replace the Roe matrix of the dissipation by the scalar spectral radius $a$ of the flux
Jacobian ([Rusanov](/methods/lax-friedrichs-flux.md)), to avoid extending Roe
averaging to real gases. They blend it, in the Jameson–Schmidt–Turkel form, with a
second-order term switched on by a [shock sensor](/definitions/troubled-cell-indicator.md).
The sensor is the product of the Bhagatwala–Lele dilatation switch, the Ducros
dilatation–vorticity ratio and Jameson's pressure second difference. The default member
is ninth order ($P=3$).

The [numerical dissipation](/definitions/numerical-dissipation.md) of the ninth-order
term acts only above $\vartheta\approx0.35\pi$, and the dispersion of every member is
that of its central part, as shown by modified-wavenumber analysis
([approximate dispersion relation](/definitions/approximate-dispersion-relation.md)). On
the [isentropic vortex](/benchmarks/isentropic-vortex.md) ninth order holds over the whole grid range only for
$\nu\lesssim0.0125$, because the third-order [SSP Runge–Kutta](/methods/ssp-runge-kutta.md)
time error dominates otherwise. The [Sod and Lax tubes](/benchmarks/sod-and-lax-shock-tubes.md)
and the [Shu–Osher problem](/benchmarks/shu-osher-problem.md) give bounded oscillations
and some entropy-wave damping, attributed to the scalar dissipation. A reacting
five-species shock tube agrees with its reference, and an underexpanded jet shows the
selectivity of each sensor factor. On the compressible [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
the scheme behaves as an implicit LES without energy pile-up, and the order of the
dissipation, not of the convective fluxes, decides the result. Grid studies of a
$M=2.25$ boundary layer give resolution guidelines, and a $M_\infty=10$ reacting
transitional boundary layer is run as a DNS. [WENO-JS](/methods/weno-js-reconstruction.md)
and TENO are cited only as the upwind alternative. Nothing is proved.

# Version read

arXiv:2103.16426v1 [physics.flu-dyn], 30 Mar 2021, "Preprint submitted to Computers &
Fluids" (dated March 31, 2021): not the version of record. 45 pages, all read; pp. 9–11
checked visually because text extraction garbled Eqs. (23)–(36). Title and authors match
Crossref. Equation, figure and page numbers here are those of arXiv v1.

# Key claims

Registry notation (see the notation map): the source's conservative variables $w$ are
$u$, its grid index $j$ is $i$, its spacing $\delta x$ is $\Delta x$, its spectral radius
$\rho(A)$ is $a$, its numerical flux $\mathcal F$ is $\hat f$, its reduced wavenumber
$k\delta x$ is $\vartheta$, its CFL is $\nu$, its coefficients $a_p$ are $\mathsf a_p$. The difference and average operators
$\delta$, $\mu$ are kept page-local.

1. The odd-order family (order $2P+3$, stencil $2(P+2)+1$) has the leading truncation error $\frac{\mathsf a_P}{2}\Delta x^{2P+3}\,\partial_x^{2(P+2)}u$, an even derivative, which the authors call dissipative (§3, Eq. (24)). **Derived** (coefficients referred to Lerat & Corre)
2. Explicit odd-order constant-coefficient schemes are $L^\infty$-stable under a CFL condition for non-smooth data, so their oscillations at discontinuities stay bounded in space and time (§3, p. 9). **Stated** (cited; a linear result applied to a nonlinear system scheme)
3. The schemes are equivalently a standard central difference of order $2(P+2)$ for the flux derivative plus a high-order artificial viscosity of order $2P+3$ on the same stencil (§3, pp. 9–10). **Derived**
4. The same schemes follow in finite volume from MUSCL reconstruction of the physical fluxes; with the Roe matrix one gets a flux-extrapolation high-order Roe scheme with minimal damping per characteristic field (§3, p. 9). **Stated** (cited)
5. The scalar dissipation $a$ (Rusanov) avoids the non-unique and costly extension of Roe averaging to real gases (§3, p. 10). **Stated**
6. For $k_2=0$ and $k_{2(P+2)}=\mathsf a_P/2$ the blended dissipation (30) recovers the upwind schemes (23) (§3, p. 10). **Derived** (see Printed slips on $k_\varepsilon$ and signs)
7. The ninth-order dissipation is a tenth-order viscosity that damps $\vartheta\gtrsim0.35\pi$ (wavelengths of fewer than 6 points) and leaves larger scales almost unaffected (§3, p. 11, Fig. 1). **Shown**
8. Every member has exactly the dispersion error of the central scheme of order $2(P+2)$ (§3, p. 11). **Derived**
9. The ninth-order dissipation is a suitable implicit subgrid regularization for LES, converging to DNS under grid refinement (§3, p. 11). **Stated**, then **Shown** in §5
10. Isentropic vortex: the observed order varies between 3 and 9 as $\nu$ decreases; a ninth-order range appears for $\nu\le0.2$, and at $\nu=1.25\times10^{-2}$ and $6.25\times10^{-3}$ ninth order holds over $100^2$–$500^2$, consistent with the suggested $\nu\lesssim0.01$ (§4.1, Fig. 2). **Shown**
11. With error model $C_t\Delta t^{3}+C_x\Delta x^{9}$, a constant temporal-to-spatial error ratio needs $\Delta t\propto\Delta x^{9/3}=\Delta x^3$, whereas a constant CFL imposes $\Delta t\propto\Delta x$; this explains the maximum of the local slope (§4.1, Eq. (40)). **Derived**
12. Sod and Lax tubes (200 points): good agreement; single-species and N$_2$–O$_2$ solutions superpose; contact smearing is due to the high-order dissipation, since the shock-capturing term is off at the contact (constant pressure) (§4.2, Fig. 3). **Shown**
13. Shu–Osher (200 points, reference 2000, $t=1.8$): pressure and velocity agree, with bounded oscillations near the shock; density and entropy are damped behind the shock, attributed to the scalar dissipation acting equally on acoustic and entropy fields (§4.3, Fig. 4). **Shown**
14. In 1D the Ducros factor is inactive, and the Bhagatwala–Lele factor strongly improves the entropy waves of Shu–Osher by suppressing spurious activation of Jameson's pressure sensor; no difference for the shock tubes (§4.3). **Shown**
15. Real-gas reacting shock tube (Park 5-species, $T_L=9000$ K, $\nu=0.02$): rarefaction, contact, shock and mass fractions agree with Grossman & Cinnella; the Bhagatwala–Lele factor had to be turned off "for better numerical robustness" (§4.4, Fig. 5). **Shown**
16. Underexpanded jet: the Ducros factor alone is close to one even in smooth irrotational regions; the Bhagatwala–Lele and Jameson factors trace large gradients (Jameson slightly more selective); Jameson cannot tell a shock from a high-vorticity solenoidal region, Bhagatwala–Lele can over-damp dilatation on under-resolved grids; the product localises the dissipation on the shocks and Mach disk, with sensor values $<0.02$ elsewhere (§5.1, Fig. 8). **Shown**
17. Underexpanded jet: the Mach disk location and width agree with experiment and simulations; $\Delta x=2$ mm captures the mean profiles, $0.5$ mm gives nearly converged $T_{rms}$, and under-resolved grids stay stable (§5.1, Fig. 7). **Shown**
18. Taylor–Green vortex at $M=0.1$ superposes on spectral results with the low-order dissipation off; no energy pile-up even at $64^3$; grid convergence at $512^3$; faster convergence at larger initial Mach number (§5.2, Fig. 9). **Shown**
19. At low $M$ the spectrum beyond the cut-off is more damped because the acoustic time-step limit needs more steps to $t=16$, i.e. more applications of the dissipation (§5.2, p. 26). **Shown** / **Derived** (interpretation)
20. Taylor–Green at $M=1$: third-order dissipation on $256^3$ is similar to ninth order on $64^3$; ninth order is nearly grid converged on $256^3$, higher orders gain little, and third-order dissipation with convective fluxes up to tenth order gives nearly identical results, so the dissipation order is the fundamental ingredient (§5.2, Fig. 11). **Shown**
21. Viscous fluxes above fourth order have negligible influence; second order over-dissipates at $256^3$, and the agreement of $128^3$ with second-order viscous fluxes is fortuitous (§5.2, Fig. 12). **Shown**
22. Supersonic boundary layer ($M=2.25$): DNS and ILES-A are nearly identical; $\Delta x^+<15$ and $\Delta z^+<10$ suffice, spanwise resolution matters more than streamwise; ILES-D (64 times coarser than DNS) mispredicts transition and overestimates the log law (§5.3.1, Figs. 13–16, Table 1). **Shown**
23. Hypersonic reacting boundary layer ($M_\infty=10$, $5520\times256\times240$): transition near $(x-x_0)/\delta^*_{in}\approx3300$, $T_{rms}$ at the production peak twice the free-stream value; $\Delta x^+=4.8$, $\Delta y_w^+=0.52$, $\Delta z^+=4.0$ classify it as a well-resolved DNS (§5.3.2, Figs. 17–18). **Shown**
24. Near non-periodic boundaries the convective stencil and the dissipation are reduced progressively to fourth order, with fourth-order one-sided differences at the boundary (§3, p. 12). **Stated**

# Printed slips

- p. 10: "$k_\varepsilon$ is a constant equal to $a_0/a_P$", but Eqs. (33)–(35) print the factors $\frac15$, $\frac3{70}$, $\frac1{105}$, which are $\lvert\mathsf a_P/\mathsf a_0\rvert$ with $\mathsf a_0=\frac16$, $\mathsf a_1=-\frac1{30}$, $\mathsf a_2=\frac1{140}$, $\mathsf a_3=-\frac1{630}$ read off Eqs. (25)–(28) *(compiler check, not in the sources: e.g. $\lvert\mathsf a_3/\mathsf a_0\rvert=6/630=1/105$)*.
- Eq. (23) prints the dissipation as "$-\frac{a_P}{2}\lvert Q\rvert\delta^{2P+3}\tilde w$", but the explicit members (25)–(28) carry $+\frac1{12}$, $-\frac1{60}$, $+\frac1{280}$, $-\frac1{1260}$, i.e. $+\frac{\mathsf a_P}{2}$.
- $\tilde w$ appears in Eqs. (23), (25)–(29) without definition; Eq. (30) uses $w$.
- p. 8: $Q=\frac12I$ "gives Lax–Friedrichs' scheme". *(Compiler check, not in the sources: the Lax–Friedrichs scheme $u^{n+1}_i=\tfrac12(u^n_{i-1}+u^n_{i+1})-\frac{\Delta t}{2\Delta x}(f_{i+1}-f_{i-1})$ has the flux $\tfrac12(f_i+f_{i+1})-\frac{\Delta x}{2\Delta t}(u_{i+1}-u_i)$, i.e. $\lvert Q\rvert=\frac{\Delta x}{\Delta t}I$ with $\mathcal D=\frac12\lvert Q\rvert\delta w$; $\frac12I$ needs a normalization the paper does not state.)*
- p. 7: thermal conductivity "$\lambda=\mathrm{Pr}/(\mu c_p)$"; should be $\mu c_p/\mathrm{Pr}$.
- Eq. (39): the error norm $\sqrt{\frac1h\sum_{i,j}(\cdot)^2}$ carries a factor $1/h$ that does not make an $L^2$ norm.
- Eq. (50) names the kinetic energy $E_k$, the text and figures $K$.
- Fig. 1 caption "up to of the ninth-order scheme"; typos "3th-order", "2th ord", "exessive", "Root-main-square", "Tayor-Green", "perscribed".
- §5.3.1: the nominal $M=2.25$ case is compared in Fig. 15 with Wenzel et al. at $M=2.5$ and $2.0$ and Pirozzoli et al. at $M=2.0$; the $M=2.25$ reference [84] is cited but not plotted.
- Shock-tube runs use $k_{10}=1/630$, twice the stated default $1/1260$, without comment.
- References: [25] "AIAA Journal 81 (1259)" (AIAA paper 81-1259); [74] without journal name ("II 83 (1) (1989) 32–78"); [54] without venue or year; [76] first author "P. J. Ferrer" for Martínez Ferrer.

# Notation map

| Sciacovelli et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $w$, $f(w)$, $A$ | $u$, $f(u)$, $A$ | conservative variables, flux, Jacobian |
| $j$, $j+\frac12$, $\delta x$, $h$ | $i$, $i+\frac12$, $\Delta x$ | point values on a uniform grid |
| $\delta$, $\delta^k$ | kept; on concept pages $[\![u]\!]_{i+1/2}$ for $\delta u$ at an interface and $\Delta^m$ (registry §10, centred at the interface for odd $m$) | undivided central difference across a cell; **collides with the TENO flag $\delta_k$ and with the error ratio $\delta$ of Eq. (40)** |
| $\mu$ | kept | two-point average ("cell-average operator"); **collides with the viscosity $\mu$** |
| $\mathcal F$, $\mathcal H$, $\mathcal D$ | $\hat f$, kept, kept | numerical flux $=$ central part $-$ dissipative part |
| $\rho(A)$ | $a$ | spectral radius; **$\rho$ is the density** |
| $Q$, $A_R$ | kept | dissipation matrix, Roe matrix; **$Q$ is the SBP stiffness matrix in the registry** |
| $a_p$, $P$ | $\mathsf a_p$ (local), $P$ | Lerat–Corre coefficients and family index; order $2P+3$; $a$ is the registry wave speed |
| $\varepsilon_2$, $\varepsilon_{2(P+2)}$, $k_2$, $k_{2(P+2)}$, $k_\varepsilon$ | $\mathsf c_2$, $\mathsf c_{2P+4}$ (local), $k_2$, $k_{2P+4}$, $k_\varepsilon$ | JST-type blended coefficients and constants, as on [numerical dissipation](/definitions/numerical-dissipation.md) |
| $\varphi_j$ | $\Xi_i$ (local) | shock sensor (Eq. (36)), as on [troubled-cell indicators](/definitions/troubled-cell-indicator.md) and [artificial viscosity](/methods/artificial-viscosity.md); $\varphi_i$ is the GQL constraint function of registry §10 |
| $\epsilon=10^{-16}$ | $\epsilon$ | regularization of the Ducros factor |
| $\varepsilon$ (Eq. (24)) | kept | leading truncation error |
| $k\delta x$, $\Phi$, $D$ | $\vartheta$; errors of $\tilde\vartheta_r$ and $\tilde\vartheta_i$ | dispersion and dissipation errors of Fig. 1; **$D$ is the differentiation matrix in the registry** |
| $\tau$, $p$, $q$ (§4.1) | $\Delta t$, kept | time step, temporal and spatial orders; **$\tau$ collides with the WENO-Z $\tau$, $q$ with the weight exponent** |
| CFL | $\nu$ | |
| $c$, $\gamma$, $M$ | $c$, $\gamma$, $M$ | agree |
| $\lambda$ | kept | thermal conductivity; **$\lambda$ is an eigenvalue in the registry** |
| $E_k$ / $K$, $\Omega$ | kept | volume-integrated kinetic energy, enstrophy; **$K$ collides with the TENO stencil size** |

# Reference list

96 printed references, numbered [1]–[96], all merged complete into the
[bibliography](/bibliography.md) with `citedby` `sciacovelli-2021`. No DOIs are printed.
Doubtful items are kept as printed: [25] garbled venue (the 1981 AIAA paper 81-1259,
keyed `jameson-1981` with the year inferred from the paper number), [54] no venue or
year, [74] journal name missing, [62] spring-school lecture notes; [7], [22], [23],
[70], [82], [92], [93], [95] are conference papers with paper numbers. No printed
duplicates.

# Pages created or updated

Chunk 2 (2026-10-22), cited further in chunks 3–9 (2026-10-22/23). This source is cited on:

* [Approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Ducros shock sensor](/definitions/ducros-shock-sensor.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Roe approximate Riemann solver](/methods/roe-riemann-solver.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)

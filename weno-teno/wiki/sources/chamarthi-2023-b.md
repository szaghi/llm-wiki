---
type: Source
title: "Chamarthi (2023) — Efficient high-order gradient-based reconstruction for compressible flows"
description: "Raises gradient-based reconstruction to a seventh-order upwind scheme by two free parameters in the second derivative, limits it with a monotonicity-preserving limiter (MEG7), and restores high order on nonlinear problems by switching between flux and state reconstruction with a density-based discontinuity detector."
resource: "doi:10.1016/j.jcp.2023.112119"
source_kind: paper
authors: [Chamarthi A.S.]
year: 2023
venue: "J. Comput. Phys. 486:112119"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Journal_of_Computational_Physics_Chamarthi_Efficient_high-order_gradient-based_reconstruction_for_compr.pdf"
tags: [finite-difference, reconstruction, low-dissipation, hybrid-scheme, troubled-cell, compact-scheme]
timestamp: 2026-10-23T16:00:00Z
---

# Summary

The paper extends the author's
[gradient-based reconstruction (GBR)](/methods/gradient-based-reconstruction.md)
for the [conservative finite-difference](/definitions/conservative-finite-difference-scheme.md)
discretization of the compressible Euler and Navier–Stokes equations on uniform
Cartesian grids. In GBR the interface states come from a two-moment Legendre
expansion in each cell,
$u^-_{i+1/2}=u_i+\tfrac{\Delta x}2(\partial_xu)_i+\tfrac{\Delta x^2}{12}(\partial_x^2u)_i$.
The first derivatives are the sixth-order central differences that the viscous
fluxes also need, so the gradients are shared between the convective and the
[α-damping viscous](/methods/alpha-damping-viscous-flux.md) terms. The companion
paper, [Chamarthi (2023a)](/sources/chamarthi-2023.md), obtained a fourth-order scheme. Here the second
derivative is a difference of interface gradients with two free parameters, and
Fourier analysis ([approximate dispersion relation](/definitions/approximate-dispersion-relation.md))
picks the values that give a seventh-order upwind scheme on the same nine-point
flux stencil. Shocks are captured by applying the Suresh–Huynh
[monotonicity-preserving limiter](/methods/monotonicity-preserving-limiter.md)
to the GBR interface value in characteristic variables (scheme MEG7, with
conservative and primitive variants).

The second contribution addresses the loss of order of state-reconstruction
finite-difference schemes on nonlinear problems: an interface flux evaluated
from reconstructed states is only second-order accurate. At each interface the
scheme switches between a seventh-order reconstruction of point fluxes and the
flux of the limited states. The binary switch comes from a density-based
[discontinuity detector](/definitions/troubled-cell-indicator.md) after Li et
al., in the spirit of [hybrid schemes](/methods/hybrid-weno.md). The Riemann
solver is HLLC and time stepping is SSP-RK3 with CFL 0.2.

The baseline is a seventh-order explicit
[WCNS](/methods/weighted-compact-nonlinear-scheme.md) with
[mapped](/methods/mapped-weno.md) weights (WCNS7M). Tests: isentropic-vortex
convergence (observed rates 6.0 to 6.7 on the finest grids), 1D shock tubes,
Le Blanc, Sedov (where WCNS7M fails), blast wave, Shu–Osher and Titarev–Toro,
Richtmyer–Meshkov, 2D shock–entropy wave, double Mach reflection, a 2D Riemann
problem, the [viscous shock tube](/benchmarks/viscous-shock-tube.md) at
$\mathrm{Re}=1000$, a shock–shear layer, and an inviscid Taylor–Green vortex
comparing fourth- and seventh-order GBR. WCNS7M costs 1.38 to 1.97 times as
much as MEG7-prim (Table 2).

# Version read

arXiv preprint arXiv:2305.00762v1 [physics.flu-dyn], 1 May 2023 ("Preprint
submitted to Elsevier, May 2, 2023"), not the JCP version of record; 30 pages,
all read, pp. 6–11, 13–14, 17 and 24–26 also visually (equations, tables, the
Appendix A listing). Page 1 matches Crossref apart from capitalization
("Gradient-based Reconstruction"); the file prints no DOI. Equation, table and
reference numbers cited here are those of the arXiv v1.

# Key claims

Registry notation (see the notation map): reconstructed variable $u$ (point
values, conservative or primitive), x-index $i$, scaled gradient
$\delta_i=\Delta x\,(\partial_xu)_i$, GBR parameters $\alpha_{\mathrm D}$,
$\beta_{\mathrm D}$ (page-local, as on the gradient-based-reconstruction and
α-damping pages), reduced wavenumber $\vartheta$.

1. GBR with $\alpha_{\mathrm D}=38/7$, $\beta_{\mathrm D}=3/190$ in Eqs. (19)–(21) is a seventh-order upwind scheme for linear advection, with leading error $\mathrm i\tilde\vartheta=\mathrm i\vartheta+\vartheta^8/280-\mathrm i\vartheta^9/360-\vartheta^{10}/560+O(\vartheta^{11})$ (§2.2, Eq. 22, Appendix A). **Derived** (Fourier analysis) *(compiler check, not in the sources: the Fourier symbol of the flux formula Eq. (33) differenced gives exactly this series.)*
2. The resulting second derivative and interface values are Eqs. (23)–(24), which use only cell-centre values and scaled gradients, e.g. $u^-_{i+1/2}=\tfrac1{840}(420\delta_i+60\delta_{i-1}-60\delta_{i+1}+478u_i+178u_{i-1}+3u_{i-2}+178u_{i+1}+3u_{i+2})$ (§2.2). **Derived**
3. The fourth-order GBR of the companion paper is the case $\alpha_{\mathrm D}=4$, $\beta_{\mathrm D}=0$ and has the same flux stencil (Remark 2.2, §3.2, Eq. 64). **Derived**
4. Lele's sixth-order compact first derivatives in place of the explicit ones also give seventh order for the same parameters, with better spectral properties at the cost of a tridiagonal solve (Remark 2.3). **Stated**
5. GBR is a finite-difference scheme on point values, fundamentally different from van Leer's third-order finite-volume scheme, although both use the same Legendre polynomial (Remark 2.5). **Stated**
6. For nonlinear Euler problems the linear GBR is only second-order accurate when the interface flux is $f(u^\mp_{i+1/2})$ of reconstructed states; reconstructing the point fluxes $f(u_i)$ restores the design order (§2.4, Eqs. 29–30, citing van Leer & Nishikawa). **Stated** (Table 1 supports the remedy)
7. High order requires computing the interface fluxes and the interface states independently: the hybrid flux $\sigma_{i+1/2}F(f^-)+(1-\sigma_{i+1/2})f(u^-)$, and likewise from the right (Eqs. 31–32), keeps high order in smooth regions and non-oscillatory capturing at discontinuities; the states in the dissipation term are always the limited ones (§2.4). **Shown** (Table 1, Examples 3.2–3.11)
8. The detector uses density only, because density sees both shocks and contacts, pressure and velocity only shocks (§2.4). **Stated**
9. A threshold $\psi_c$ above 0.5 reduces accuracy, below 0.5 produces oscillations (§2.4). **Stated** (no data)
10. The detector-based hybrid suits explicit GBR better than implicit (compact) GBR, whose global solve makes it expensive (§2.4). **Stated**
11. Viscous fluxes use the α-damping interface gradient with $\alpha_{\mathrm D}=4$ (the source's $\alpha_v$) and sixth-order cell gradients, a fourth-order viscous scheme with better spectral properties than the sixth-order α-damping scheme of Chamarthi et al. (2022) (§2.1, Eqs. 12–13). **Stated** (cited)
12. The viscous discretization is not truly high order on nonlinear problems (second order with Sutherland's law), yet it gave better results than truly high-order schemes with poor spectral properties (Remark 2.1). **Stated** (cited)
13. Isentropic vortex (strength 5, $[-5,5]^2$, $t=10$): $L_2$ density errors on $25^2$ to $200^2$ give rates 5.25, 6.03, 6.59 (MEG7-cons), 5.13, 6.00, 6.68 (MEG7-prim) and 4.71, 6.35, 6.24 (WCNS7M); both MEG7 variants are said to have "achieved seventh-order accuracy" (Ex. 3.1, Table 1). **Shown** (the observed rates stay below 7)
14. Sod and Lax (200 points): all schemes capture rarefaction, contact and shock without obvious oscillations (Ex. 3.2, Figs. 2–3). **Shown**
15. Le Blanc (900 points, $\gamma=5/3$, $t=6$): WCNS7M is slightly more dissipative; MEG7 places the discontinuity at $x=8$ closer to the exact solution (Ex. 3.3, Fig. 4). **Shown**
16. Sedov 1D (900 points, $t=10^{-3}$): both MEG7 variants run without noticeable oscillations and WCNS7M fails; MEG7-cons needed the positivity-preserving approach of Zhang & Shu (Ex. 3.3, Fig. 5). **Shown**
17. Blast wave (600 points, $t=0.038$): MEG7-prim predicts the density extrema best; MEG7 captures the velocity discontinuity near $x\approx0.87$ with fewer points (Ex. 3.4, Fig. 6). **Shown**
18. Shu–Osher (200 points) and Titarev–Toro (1000 points): MEG7 resolves the density extrema and high-frequency waves better than WCNS7M (Ex. 3.5, Figs. 7–8). **Shown**
19. Richtmyer–Meshkov ($320\times80$, $t=9$): MEG7-cons has a thinner interface than WCNS7M, MEG7-prim lower dissipation still with small-scale roll-ups (Ex. 3.6, Fig. 9). **Shown**
20. 2D shock–entropy wave ($400\times80$): MEG7 has less dissipation and dispersion error than WCNS7M; the shock-stable HLLC of Fleischmann et al. avoids the carbuncle seen in the companion paper (Ex. 3.7, Fig. 10). **Shown**
21. Double Mach reflection ($1024\times256$): MEG7-cons resolves the slip-line vortices better than WCNS7M; MEG7-prim shows none but a better-resolved wall jet, so primitive reconstruction is "slightly more dissipative" here (Ex. 3.8, Fig. 11). **Shown**
22. 2D Riemann problem ($400\times400$, $t=0.8$): MEG7-cons resolves the slip-line structures better than WCNS7M; conservative and primitive variants differ little (Ex. 3.9, Fig. 12). **Shown**
23. Viscous shock tube ($\mathrm{Re}=1000$, $1280\times640$): WCNS7M departs markedly in the primary vortex at $x=0.75$ and in the right-wall vortex system; MEG7 stays much closer to the $4000\times2000$ reference (Ex. 3.10, Fig. 13). **Shown**
24. Shock–shear layer ($320\times80$): all schemes capture the oblique shock without oscillation; MEG7 resolves the shear-layer vortices better (Ex. 3.11, Fig. 14). **Shown**
25. Wall-clock times (Table 2, same machine and flags, hardware not stated) for MEG7-prim, MEG7-cons, WCNS7M: Richtmyer–Meshkov 224, 205, 345 s; Riemann 1025, 1031, 1502 s; DMR 1806, 1946, 2493 s; viscous shock tube 35455, 38062, 70082 s. MEG7 is "at least 40% cheaper than the WCNS7M scheme, on average", and twice as fast on the viscous shock tube, where gradients are shared (§3.1). **Shown** (see Printed slips)
26. Seventh-order GBR is less dissipative than fourth-order GBR, which has slightly better dispersion (§3.2, Fig. 15). **Shown** (Fourier plots)
27. Inviscid Taylor–Green vortex ($64^3$, $t=10$): seventh-order GBR keeps more kinetic energy and gives higher enstrophy than fourth-order GBR (§3.2, Fig. 16). **Shown**
28. WCNS, unlike WENO, can use any approximate Riemann solver, which allows a like-for-like comparison with one solver (§3). **Stated**
29. The extension to curvilinear grids is straightforward and "presented elsewhere"; GBR suits multi-component reacting flows because species gradients are computed once (§4). **Stated**

# Printed slips

- **Eq. (42), third WCNS sub-stencil:** printed $\tfrac1{16}(-u_{i-1}+9u_i+9u_{i+1}+u_{i+2})$, whose coefficients sum to $18/16$; the four-point Lagrange interpolant at $x_{i+1/2}$ is $\tfrac1{16}(-1,9,9,-1)$. *(compiler check, not in the sources)*
- **Eq. (48), mapping denominator:** printed $C_k^2-(1-2C_k)\omega_k$; with this sign the map does not fix the ideal weight ($C_k=1/64$ gives $-63/3904$), with $+(1-2C_k)\omega_k$ it does, as the text requires. *(compiler check, not in the sources)*
- Eq. (46) prints $IS_k$ without the square of the inner sum and without the coefficients; Eqs. (45) and (47) carry stray indices ($\alpha_{k,m}$, $w^M_{3,m}$, $q^{L,4}$).
- Eqs. (35)–(37): $\varepsilon$ is defined but does not appear in the printed detector, which is undefined for constant density.
- The detector is attributed to "Li et al. [52]" (Li & Jaberi 2012) and then to "the original paper of Li et al. [53]" (Li, Chen & Ren 2022).
- Eqs. (8)/(14) print the Legendre expansion with $\frac1{\Delta x}$ and $\frac{3\kappa}{2\Delta x^2}$ prefactors on the derivatives, inconsistent with Eq. (15); Eq. (23) gives $\Delta x^2(\partial_x^2u)_i$ although labelled $(\partial_x^2u)_i$.
- Eq. (34) uses $i$ (the paper's y index) for the x direction; Eq. (27) mixes $i$ and $j$ subscripts and contains an undefined $\hat\Phi_{j-1}$.
- Lax problem: "t = 01.4" in the text, $t=0.14$ in the Fig. 3 caption. Table 1 grid sizes print as "252, 502, 1002, 2002" ($25^2,\dots,200^2$).
- Table 2: normalized times differ in the last digit from the printed seconds (MEG7-cons, viscous shock tube: $38062/35455=1.074$, printed 1.076; WCNS7M: $70082/35455=1.977$, printed 1.97).
- "At least 40% cheaper … on average" (§3.1): from Table 2, MEG7-prim saves 35%, 32%, 28% and 49% against WCNS7M. *(compiler check, not in the sources)*
- Titarev–Toro: the initial data are printed on $[0,10]$ with the jump at $x=0.5$, while the Fig. 8(a) axis spans $[-5,5]$.
- Symbol reuse: $\xi$ is the MP parameter (7) and the detector constant ($10^{-3}$); $\varepsilon$ has three uses; $\kappa$ is the Legendre parameter and the conductivity.
- Typos: "Richtmeyer", "WCN7M", "Hyunh", "Collela", "substensils"; §2.2 refers to "Equation (9)" for Eq. (15).

# Notation map

| Chamarthi (2023b) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Phi$ ($Q$ or $U$) | $u$ | point value, conservative $(\rho,\rho v,E)$ or primitive $(\rho,v,p)$ |
| $j$, $i$ | $i$, $j$ | **x and y indices swapped** relative to the registry |
| $\Phi^L_{j+1/2}$, $\Phi^R_{j+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | interface states from cells $i$ and $i+1$ |
| $\Phi_L$, $\Phi_R$ (Eqs. 20–21) | kept | auxiliary extrapolations inside the interface gradient |
| $\Phi'_j$ | $\delta_i=\Delta x\,(\partial_xu)_i$ (page-local, as on [gradient-based reconstruction](/methods/gradient-based-reconstruction.md)) | sixth-order central difference |
| $\alpha$, $\beta$ | $\alpha_{\mathrm D}$, $\beta_{\mathrm D}$ (page-local) | GBR parameters; **$\alpha$ collides with $\alpha_k$ and the DG blending coefficient, $\beta$ with $\beta_k$** |
| $\alpha_v$ | $\alpha_{\mathrm D}$ (page-local on [α-damping viscous flux](/methods/alpha-damping-viscous-flux.md)) | α-damping coefficient of the viscous gradient, $4$ |
| $\kappa$ | $\kappa_{\mathrm M}$ | Legendre parameter, $1/3$; **$\kappa$ is the kinetic energy in the registry** |
| $F^c_L$, $F^c_R$, $f_j$ | interface fluxes, $f(u_i)$ | $F(f_L)$ is the reconstructed point flux, $F(Q_L)$ the flux of the state |
| $\lvert A_{j+1/2}\rvert$ | $\lvert A\rvert_{i+1/2}$ | generic upwind matrix; HLLC in practice |
| $\xi$ (MP), $d_j$ | $\xi_{\mathrm{MP}}$ (page-local), kept | MP parameter 7 and curvature |
| $\psi_j$, $\psi_c$ | $\psi_{\mathrm d}$, $\psi_c$ (page-local) | detector and threshold; **$\psi$ is the entropy potential in the registry** |
| $\sigma_{j+1/2}$ | $\sigma_{i+1/2}$ | binary switch, 1 = smooth; **$\sigma$ is the affine scaling in §10** |
| $C_k$, $w_k$, $\alpha_k$, $IS_k$, $w^M_k$ | $d_k$, $\omega_k$, $\alpha_k$, $\beta_k$, $g(\omega_k)$ | WCNS7M baseline |
| $\epsilon$ (vortex strength) | $\mathcal E$ | |
| $k$ (Fourier) | $\vartheta$ | reduced wavenumber |
| $\nu$ | $\nu_{\mathrm{kin}}$ | kinematic viscosity; **$\nu$ is the CFL number in the registry** |

# Reference list

71 printed references in numbered style ([1]–[71]), all merged complete into
the [bibliography](/bibliography.md) with `citedby` `chamarthi-2023-b`.
Ref. [1] is the companion `chamarthi-2023`; ref. [49] is its arXiv preprint,
kept as a separate entry. Refs. [4] and [14] print no volume, ref. [71] no page
or article number; ref. [20] (Jiang & Shu) is printed with year 1995 and
volume "126 (126)", kept as printed; ref. [41] prints no journal name but a JCP
DOI. No printed duplicates.

# Pages created or updated

Chunk 5 (2026-10-23), cited further in chunks 6–7 (2026-10-23). This source is cited on:

* [Approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Gradient-based reconstruction (MEG/MIG schemes)](/methods/gradient-based-reconstruction.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Leblanc shock tube](/benchmarks/leblanc-shock-tube.md)
* [Mapped WENO](/methods/mapped-weno.md)
* [Monotonicity-preserving (MP) limiter](/methods/monotonicity-preserving-limiter.md)
* [Richtmyer–Meshkov instability](/benchmarks/richtmyer-meshkov-instability.md)
* [Shock–mixing-layer interaction](/benchmarks/shock-mixing-layer-interaction.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Targeted ENO (TENO)](/methods/targeted-eno.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
* [Viscous shock tube (Daru–Tenaud)](/benchmarks/viscous-shock-tube.md)
* [Weighted compact nonlinear schemes (WCNS)](/methods/weighted-compact-nonlinear-scheme.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)
* [α-damping viscous flux discretization](/methods/alpha-damping-viscous-flux.md)

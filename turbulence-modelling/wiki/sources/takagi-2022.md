---
type: Source
title: "Takagi et al. (2022) — A novel high-order low-dissipation TENO-THINC scheme for hyperbolic conservation laws"
description: "Fifth-order finite-difference hybrid that keeps TENO5 in smooth and under-resolved regions and switches to THINC reconstruction in cells flagged by a parameter-free discontinuity indicator built from TENO's own stencil flags; tested on inviscid Euler problems and an inviscid Taylor–Green vortex at 64^3."
resource: "doi:10.1016/j.jcp.2021.110899"
source_kind: paper
authors: [Takagi S., Fu L., Wakimura H., Xiao F.]
year: 2022
venue: "J. Comput. Phys. 452:110899"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Journal_of_Computational_Physics_Takagi_A_novel_high-order_low-dissipation_TENO-THINC_scheme_for_hyp.pdf"
tags: [shock-capturing, numerical-dissipation, compressible, implicit-les]
timestamp: 2026-10-29T10:05:00Z
---

# Summary

Takagi et al. (2022) build a hybrid finite-difference reconstruction for
hyperbolic conservation laws: the fifth-order targeted ENO scheme (TENO5)
runs in smooth and in under-resolved regions, and the non-polynomial THINC
(tangent of hyperbola for interface capturing) reconstruction replaces it in
cells that hold a genuine discontinuity. The paper belongs to
shock-capturing numerics, a [WENO-family](/methods/weno-scheme.md) scheme;
turbulence enters only as motivation (low
[numerical dissipation](/properties/numerical-dissipation.md) for
under-resolved, [implicit](/definitions/implicit-les.md) LES of flows with
shocks) and through one inviscid
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $64^3$. The
authors defer turbulence predictions to a later paper.

The contribution is a parameter-free discontinuity indicator. TENO5 already
computes, for each of its three candidate stencils, a binary flag
$\delta^{\mathrm T}_k$ (smooth 1, non-smooth 0). A per-cell pattern
$\zeta_i\in\{2,1,-1,0\}$ records whether the right-biased and the
left-biased stencils are flagged (Eq. 19); a cell is declared
discontinuous when $\zeta_i=0$, a cell among $i-3,\dots,i-1$ has
$\zeta\in\{1,2\}$ and a cell among $i+1,\dots,i+3$ has $\zeta\in\{-1,2\}$
(Eq. 20). There the TENO interface flux is replaced by the THINC flux
(Eq. 16), or by a first-order flux where the data are not monotone (Eq. 17).
The indicator adds no parameter to those of TENO5 ($q=6$, $C_T=10^{-5}$).
The authors contrast it with the shock sensors of hybrid compact/WENO
schemes, which they call case- and parameter-sensitive, and list
[artificial viscosity](/methods/artificial-viscosity-shock-capturing.md)
only as an established alternative.

On the Gaussian pulse the scheme is fifth-order with errors identical to the
linear upwind scheme. On the multi-wave advection, shock tubes, blast waves,
double Mach reflection, the inviscid single-mode Rayleigh–Taylor
instability (a shock-capturing test, not the
[mixing-layer turbulence](/benchmarks/rayleigh-taylor-mixing.md)),
two-dimensional Riemann problems and Mach 80 and 2000 jets it resolves
contacts and small structures better than WENO5-Z and TENO5, at 16.8–17.1%
more cost than TENO5. On the inviscid Taylor–Green vortex it preserves
kinetic energy and captures enstrophy growth better than both.

# Version read

Version of record (Elsevier, received 2 April 2021, online 20 December
2021); 24 pages, all read, with Eqs. (8)–(20) and Table 1 checked visually.
Page 1 matches Crossref. Equation, section and reference numbers on this
page are those of the version of record.

# Key claims

1. TENO5-THINC is fifth-order on the Gaussian pulse, with $L_\infty$ errors identical to those of the fifth-order upwind linear scheme at every resolution ($h=0.01$ to $0.000625$: 4.63E−3, 1.65E−4, 5.25E−06, 1.65E−07, 5.24E−09; orders 4.81, 4.98, 4.99, 4.97): neither TENO's nonlinear adaptation nor THINC is activated in smooth regions (§4.1, Table 2). **Shown**
2. The discontinuity criterion (Eqs. 19–20) is parameter-free; the hybrid's only parameters are those of TENO5 ($q=6$, $C_T=10^{-5}$, $\epsilon_W=10^{-40}$) and the THINC steepness $\beta_{\mathrm{TH}}=1.6$ (§3.2 item 3, §4). **Stated**
3. In well-resolved smooth regions all $\delta^{\mathrm T}_k=1$, THINC is never activated, and the scheme restores the spectral properties and order of TENO's background linear scheme exactly (§3.2 item 1). **Derived** (from the construction; Table 2 agrees)
4. When some $\delta^{\mathrm T}_k=0$ the local scales are either under-resolved high-wavenumber fluctuations or genuine discontinuities; only the latter satisfy Eqs. (19)–(20) and go to THINC, while under-resolved fluctuations stay with nonlinear TENO (§3.2 item 2). **Stated** (activation maps, Figs. 22–25)
5. For a one-cell step (Eq. 18), the cell holding the jump has $\delta^{\mathrm T}_{1,i}=\delta^{\mathrm T}_{2,i}=1$, with $\delta^{\mathrm T}_{1,i-1}=0$ and $\delta^{\mathrm T}_{2,i+1}=0$ in its neighbours (§3.1, Table 1). **Shown** (Table 1 is reproduced by an implementation of Eqs. 8–12 on the data of Eq. 18 *(compiler check, not in the sources)*)
6. The THINC reconstruction (Eqs. 15–16) is bounded by $f_{i-1}$ and $f_{i+1}$, so it creates no new extrema and needs no monotonicity limiter (§2.3). **Stated**
7. The THINC flux of Eq. (16) differs from the form of Deng et al. (2019) [5], which "may cause the symmetry breaking from floating point errors" (§2.3). **Stated**
8. With $\beta_{\mathrm{TH}}=1.6$ THINC can have a positive imaginary part of the modified wavenumber in some ranges (anti-diffusion, as TVD-SuperBee): undesirable for smooth scales [51], excellent at discontinuities [6]; this is the rationale of the hybrid (§2.3). **Stated**
9. Multi-wave advection ($N_x=200$ to $t=200$ with SSP-RK3; $N_x=400$ to $t=2000$ with a five-stage fourth-order SSP-RK): the square wave is kept markedly better than by WENO5-Z and TENO5; on the Gaussian, triangle and half-ellipse the scheme performs like TENO5 (§4.2, Figs. 2–3). **Shown**
10. Sod and Lax shock tubes ($N_x=100$): shocks as sharp as with WENO5-Z and TENO5, contacts better resolved (§4.3, Figs. 4–5). **Shown**
11. Shu–Osher problem ($N_x=200$, $t=1.8$): similar to TENO5, slightly better than WENO5-Z; CFL 0.4 against 0.6 makes a negligible difference (§4.4, Figs. 6–7). **Shown**
12. Interacting blast waves ($N_x=400$, CFL 0.35, Roe flux splitting with entropy fix): shock and density peak as with WENO5-Z and TENO5, contact "significantly better" than both and better than other WENO schemes in Figs. 13–14 of [15] (§4.5, Fig. 8). **Shown**
13. Blast-wave grid convergence ($N_x=400$ to $3200$): with $C_T=10^{-4}$ the solution converges monotonically to the reference; with $C_T=10^{-5}$ a small overshoot appears near the strong contact at very high resolution. $C_T=10^{-5}$ stays the default; its optimization is out of scope (§4.5, Fig. 9). **Shown**
14. Double Mach reflection: at $512\times128$ and $1024\times256$ the scheme resolves small structures significantly better than WENO5-Z and TENO5 and captures the Mach stems sharply; its $512\times128$ result resembles WENO5-Z at $1024\times256$; it also beats the six-point TENO6, especially on the coarse mesh (§4.6, Figs. 10–11). **Shown**
15. Cost per time step on the double Mach reflection (ms, $512\times128$ / $1024\times256$): WENO5-Z 696 / 2802, TENO5 810 / 3255, present 946 / 3810, TENO6 867 / 3330; the present scheme is 16.8% (17.1%) more expensive than TENO5 and 9.1% (14.4%) more than TENO6, "not significant"; the hardware is not stated (§4.6, Table 3). **Shown**
16. The double Mach reflection is insensitive to CFL (0.4 against 0.6, Fig. 12) and to TENO's $\epsilon_W$ ($10^{-8}$, $10^{-12}$, $10^{-40}$, Fig. 13) (§4.6). **Shown**
17. Rayleigh–Taylor instability ($64\times256$, $128\times512$, $t=1.95$): TENO5 is less dissipative than WENO5-Z, and the present scheme captures significantly more small-scale vortical structures than both, also with the Roe flux instead of Rusanov's; symmetry is preserved (§4.7, Figs. 14–17). **Shown**
18. Two-dimensional Riemann configurations 3 ($t=0.3$) and 12 ($t=0.25$) on $1024^2$: more small-scale structure than WENO5-Z and TENO5, sharp stable shocks, symmetry preserved (§4.8, Figs. 18–19). **Shown**
19. Mach 80 and Mach 2000 jets ($800\times400$, $\gamma=5/3$, CFL 0.35, positivity-preserving flux limiter [31]): all three schemes are stable and sharp, the present one best on small structures, then TENO5, then WENO5-Z; the authors also rank it above WENO5-JS (Fig. 5.4 of [75]) and high-order DG (Figs. 4.5–4.6 of [74]) by figure reference (§4.9, Fig. 20). **Shown**
20. Inviscid Taylor–Green vortex at $64^3$ to $t=10$: the present scheme preserves kinetic energy and captures enstrophy growth better than WENO5-Z and TENO5 (§4.10, Fig. 21). **Shown**
21. THINC activation maps (with $\epsilon_W=10^{-8}$ for clarity) show THINC firing near discontinuities in 1-D (Sod, Lax, Shu–Osher, blast waves) and around genuine discontinuities in 2-D (double Mach reflection, Riemann configuration 3, Rayleigh–Taylor) for each characteristic component and split-flux direction (§4.11, Figs. 22–25). **Shown**
22. The scheme, validated in finite differences, can be used in finite-volume solvers without changing the reconstruction (§5). **Stated**
23. "The present results are among the best in the literature and thus serve as the state-of-the-art reference" (§5; abstract). **Stated**
24. TENO robustness up to ten-point eighth order is shown in [14]; even-order TENO is stable because no candidate stencil is purely downwind (§2.2.1). **Stated**
25. The performance of hybrid compact-WENO/ENO schemes depends on shock sensors that are "mostly case and parameter sensitive" [41][12]; boundary variation diminishing (BVD) [60] is a parameter-free alternative (§1). **Stated**
26. The turbulence performance of the scheme is deferred to "a forthcoming separate paper" (§5). **Stated**

The THINC interface flux (Eq. 16, characteristic speed positive), with
$f_\pm$ the mean and half-jump of the neighbouring values:

$$\hat f_{i+1/2}=f_++f_-\frac{A_{\mathrm{TH}}+T_{\mathrm{TH}}}{1+A_{\mathrm{TH}}T_{\mathrm{TH}}},\qquad T_{\mathrm{TH}}=\tanh(0.5\beta_{\mathrm{TH}}),\quad A_{\mathrm{TH}}=\frac{\operatorname{sgn}(\alpha_{\mathrm{TH}})}{T_{\mathrm{TH}}}\frac{B_{\mathrm{TH}}-1}{B_{\mathrm{TH}}+1},\quad B_{\mathrm{TH}}=e^{|\alpha_{\mathrm{TH}}|\beta_{\mathrm{TH}}},\quad \alpha_{\mathrm{TH}}=\frac{f_i-f_+}{f_-}.$$

# Printed slips

- Double Mach reflection final time: §4.6 "the simulation time is t = 0.2"; Fig. 10 caption "at the simulation time t = 2.0".
- Shu–Osher domain: Eq. (29) sets the initial data on $-5\le x<-4$ and $-4\le x\le5$, while the text says "The computational domain is [0,10]".
- Eq. (15) prints an unbalanced parenthesis: "$h_i(x)=f_++f_-(\tanh(\beta(X_i-d_i))$".
- The THINC conservation constraint is printed $f_i=\int_{x_{i-1/2}}^{x_{i+1/2}}h(x)\,dx$, without the $1/\Delta x$ of Eq. (3).
- §1 cites "[18][26][8][45][48][8][44]", with [8] twice; §4 cites "[15][2]" for the TENO5 parameters, where [2] is the WENO-Z paper; TENO6 is used in §4.6 without a citation there.
- Ref. [64] prints the first author as "N.J. Von" (von Neumann).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $f(u)$, $f_i$, $h(x)$ | (flux, its point values, primitive function, page-local) | **collision:** $h(x)$ against the cell size $h$; Table 2's $h$ is the grid spacing |
| $\hat f_{i+1/2}$, $\hat f_{k,i+1/2}$ | (interface flux, candidate-stencil flux, page-local) | **collision:** hat is not a test filter here |
| $\beta_{k,r}$ | $\mathrm{IS}_k$ | Jiang–Shu smoothness indicator; **collision** with $\beta(\boldsymbol x)$ |
| $\tau_K$, $\tau_5=\lvert\beta_{1,3}-\beta_{2,3}\rvert$ | $\mathrm{IS}_{\mathrm G}$ (global reference indicator, page-local, as on the [WENO](/methods/weno-scheme.md) page) | **collision** with $\tau_{ij}$ |
| $\gamma_k$, $\chi_k$ | $\gamma^{\mathrm T}_k$, $\chi^{\mathrm T}_k$ (registry §11) | scale-separated measure and its normalization; **collision** with $\gamma$ and the SA $\chi$ |
| $\delta_k$, $\delta_{k,i}$ | $\delta^{\mathrm T}_k$ (registry §11) | binary stencil flag; **collision** with $\delta$ and $\delta_{ij}$ |
| $d_k$, $w_k$ | $d_k$, $\mathsf w_k$ | optimal linear and nonlinear weights ($d_k=6/10$, $3/10$, $1/10$) |
| $q$, $C_T$ | $q$, $C_T$ | TENO exponent and cutoff |
| $\varepsilon$ | $\epsilon_W$ | small number ($10^{-40}$ in TENO, $10^{-15}$ in the THINC fallback); **collision** with $\varepsilon$ |
| $\beta$ (THINC) | $\beta_{\mathrm{TH}}$ (registry §11) | jump steepness, 1.6; **collision** with $\beta(\boldsymbol x)$ |
| $\alpha$, $A$, $B$, $T$ | $\alpha_{\mathrm{TH}}$ (registry §11), $A_{\mathrm{TH}}$, $B_{\mathrm{TH}}$, $T_{\mathrm{TH}}$ (page-local, as on the WENO page) | THINC flux auxiliaries; **collision** of $\alpha$ with the DG blending factor, of $T$ with the temperature |
| $d_i$, $X_i$, $f_\pm$ | (jump centre, normalized cell coordinate, neighbour mean and half-jump, page-local) | $d_i$ collides with the wall distance $d$ |
| $\zeta_i$ | $\zeta_i$ (page-local) | discontinuity pattern, values $2,1,-1,0$ |
| $N$ | $N_x$ | number of cells, not a polynomial degree |
| $\rho$, $u$, $v$, $w$, $p$, $\gamma$ | $\rho$, $u$, $v$, $w$, $p$, $\gamma$ | Euler variables; $\gamma=5/3$ in the Rayleigh–Taylor and jet tests |

# Reference list

76 printed references, numbered style ([1]–[76], alphabetical by first
author). The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Ref. [64] (von
Neumann & Richtmyer 1950, printed "N.J. Von") is mapped to `vonneumann-1950`; ref. [42] (Li, Fu & Adams 2021, J.
Comput. Phys. 428:109960) is keyed `li-2021-h`, distinct from the Source `li-2021`, a different work. Same-author same-year works are keyed in
printed order (Deng 2018, Fu 2019, Haimovich 2017, Lusher 2020). Ref. [55]
(Rusanov 1961) prints no volume. All items parsed.

# Pages created or updated

Chunk 8 (2026-10-27). This source is cited on:

- [Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)

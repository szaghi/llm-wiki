---
type: Source
title: "Danis et al. (2025) — Tensor-train WENO scheme for compressible flows"
description: "Evolves a finite-difference WENO5-JS solver for 3D Euler entirely in tensor-train format: shift operators on single cores, cross interpolation for the Lax–Friedrichs splitting and the WENO reconstruction, rounded SSP-RK3 and a mesh-dependent truncation tolerance; fifth order is kept and low-rank problems run up to two or three orders of magnitude faster."
resource: "doi:10.1016/j.jcp.2025.113891"
source_kind: paper
authors: [Danis M.E., Truong D., Boureima I., Korobkin O., Rasmussen K.Ø., Alexandrov B.S.]
year: 2025
venue: "J. Comput. Phys. 529:113891"
local_file: "/home/stefano/papers/mosaic/weno-teno/2025_Crossref_Journal_of_Computational_Physics_Danis_Tensor-train_WENO_scheme_for_compressible_flows.pdf"
tags: [weno, finite-difference, efficiency, performance]
timestamp: 2026-10-23T14:53:00Z
---

# Summary

The paper builds [tensor-train WENO](/methods/tensor-train-weno.md): a
[conservative finite-difference](/definitions/conservative-finite-difference-scheme.md)
[WENO5-JS](/methods/weno-js-reconstruction.md) solver for the three-dimensional
Euler equations in which every 3D field (conserved variables, fluxes,
reconstructions) is stored and evolved in tensor-train (TT) format, a low-rank
separated representation $u(i,j,k)\approx G_1(i)G_2(j)G_3(k)$ with matrix-valued
cores. The baseline "full-tensor" scheme is unchanged: component-wise WENO5-JS with
$q=2$, $\epsilon=\Delta x^2$, global [Lax–Friedrichs](/methods/lax-friedrichs-flux.md)
flux splitting and [SSP-RK3](/methods/ssp-runge-kutta.md).

Differences are taken with shift operators that act on one TT core only.
Element-wise division, square root, absolute value and maximum have no explicit TT
algorithm, so the nonlinear steps use AMEn cross interpolation of an ordinary
element-wise routine. The **LF-cross** step is one cross interpolation that returns
all ten split flux components. The **WENO-cross** step is ten cross interpolations
per direction, each taking the five shifted copies of the stencil as input. Time
stepping is SSP-RK3 with TT rounding after every forward-Euler step and stage.
Boundary conditions edit the ghost slices of one core and add rank-1 corrections.
The rounding tolerance is set to $\epsilon_{\mathrm{TT}}=C_\epsilon V^{1/2}\Delta x^{7/2}/\max_q\lVert q\rVert_F$, so that the truncation error does not spoil fifth order. The
constant $C_\epsilon$ is chosen per problem.

Smooth tests ([Burgers](/benchmarks/burgers-equation-tests.md), linear advection,
[isentropic vortex](/benchmarks/isentropic-vortex.md), a manufactured solution)
reach fifth order with TT errors equal to the full-tensor ones. Shock tests
([Sod](/benchmarks/sod-and-lax-shock-tubes.md),
[Shu–Osher](/benchmarks/shu-osher-problem.md),
[double Mach reflection](/benchmarks/double-mach-reflection.md),
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md)) are captured as by the
full-tensor solver. The serial MATLAB TT solver is 102 times faster on the vortex at
$320^3$, 35–65 times on the manufactured solution, and more than 1000 times on the
rank-1 Sod problem at $640^3$; the last figure is measured against extrapolated
full-tensor timings. In double Mach reflection and Rayleigh–Taylor the ranks grow,
which the authors name as the limitation.

# Version read

The archive file is arXiv:2405.12301v1 [math.NA], 20 May 2024 (title page dated 22
May 2024), 29 pages (25 of text, references on the last 3), all read; the
contour plots of Fig. 6 are images and nothing was read off them. It is not the
version of record: the J. Comput. Phys. article (529:113891, 2025) can differ after
review. Page 1 prints the title in title case ("Tensor-Train WENO Scheme for
Compressible Flows") and the same six authors as Crossref. Every claim, equation
and number on this page is that of arXiv v1.

# Key claims

Registry notation, with $\Delta x=\Delta y=\Delta z$ the uniform spacing. Page-local:
$\mathsf r_1,\mathsf r_2$ the TT ranks; $\epsilon_{\mathrm{TT}}$, $\epsilon_{\mathrm{cross}}$
the rounding and cross-interpolation tolerances; $\lVert\cdot\rVert_F$ the Frobenius
norm of the array of grid values; $V$ the domain volume; $C_\epsilon$ the tolerance
constant; FT and TT the full-tensor and tensor-train solvers.

1. This is "the first study that develops a finite difference WENO scheme using the tensor-train approach for compressible flows", and the first systematic study of the relation between rank, truncation error and TT error for compressible WENO solvers (Abstract). **Stated**
2. A 3D array is written $u(i,j,k)=\sum_{\alpha_1=1}^{\mathsf r_1}\sum_{\alpha_2=1}^{\mathsf r_2}G_1(1,i,\alpha_1)G_2(\alpha_1,j,\alpha_2)G_3(\alpha_2,k,1)+$ error (§3.1, Eqs. (11)–(12), recalled from Oseledets). **Stated**
3. With shift operators $T^x$, $T^y$, $T^z$ the scheme reads $\partial_tu+\frac1{\Delta x}(T^x-1)\hat f+\frac1{\Delta y}(T^y-1)\hat g+\frac1{\Delta z}(T^z-1)\hat h_z=0$, and in TT form each shift acts only on the corresponding core (§4.1, Eqs. (16)–(19)). **Derived**
4. To the authors' knowledge, explicit TT algorithms for element-wise maximum, square root, absolute value and reciprocal do not exist, hence the flux splitting and the reconstruction are computed by cross interpolation (§4.1). **Stated**
5. Computing the physical fluxes and $a$ separately in TT form, with rounding after each addition and multiplication, caused "significant performance loss" and was abandoned (§4.2). **Stated** (no data shown)
6. The single cross interpolation returning all ten split components was "∼30% faster" than two separate ones for $\hat f^\pm$ (§4.2). **Stated** (no data shown)
7. The best AMEn initial guess for LF-cross is the conserved component of largest rank (§4.2, Alg. 1). **Stated**
8. Cross-interpolating every TT division inside WENO is slow because $\beta_k=O(\Delta x^2)$ in smooth regions but $O(1)$ at discontinuities, so $\alpha_k$ varies strongly. WENO-cross, which evaluates the whole reconstruction element-wise from the shifted stencil copies, avoids TT rounding and is "significantly more robust"; its output stays close to the stencil values "due to the ENO property" (§4.3). **Stated**
9. WENO-cross needs 10 cross interpolations per direction for the Euler system (5 components × 2 sides) (§4.3, Alg. 2). **Stated**
10. TT-SSPRK3 rounds after each forward-Euler step, $\mathcal F(u)=\mathrm{round}(u+\Delta t\,\mathcal L(u),\epsilon_{\mathrm{TT}})$, and after each stage combination (§4.4, Eqs. (21)–(22)). **Stated**
11. Assuming $\lVert u_{\mathrm{TT}}-u_{\mathrm{FT}}\rVert_F\le\epsilon_{\mathrm{TT}}\lVert u_{\mathrm{TT}}\rVert_F$ and $\lVert v\rVert_{L^2}=\Delta x^{3/2}\lVert v\rVert_F$, the triangle inequality gives $\lVert u-u_{\mathrm{TT}}\rVert_{L^2}\le C_1\Delta x^5+\Delta x^{3/2}\epsilon_{\mathrm{TT}}\lVert u_{\mathrm{TT}}\rVert_F$, so $\epsilon_{\mathrm{TT}}\le C_2\Delta x^{7/2}/\lVert u_{\mathrm{TT}}\rVert_F$ keeps fifth order; the operational rule is $\epsilon_{\mathrm{TT}}=C_\epsilon V^{1/2}\Delta x^{7/2}/\max_q\lVert q\rVert_F$, with $\epsilon_{\mathrm{cross}}=\epsilon_{\mathrm{TT}}$ (§4.6, Eqs. (32)–(35)). **Derived** (the bound on the accumulated TT–FT difference is assumed, not proved)
12. 3D linear advection ($C_\epsilon=500$): FT and TT are both fifth order; at $320^3$ the TT $L^2$ error is $5.45\times10^{-10}$ against $5.50\times10^{-10}$ for FT (§5.1, Table 1). **Shown**
13. 3D Burgers ($C_\epsilon=10$): TT errors very close to FT, order 4.96 at $320^3$, errors $9.01\times10^{-10}$ (TT) and $9.03\times10^{-10}$ (FT) (§5.2, Table 2). **Shown**
14. Isentropic vortex ($C_\epsilon=2/\sqrt V$): TT orders at the last refinement 5.12 ($\rho$), 5.15 ($\rho v_1$), 5.45 ($\rho v_2$), 5.37 ($E$) (§5.3, Table 3). **Shown**
15. Isentropic vortex: $C_\epsilon=1/\sqrt V$ and $2/\sqrt V$ match FT accuracy; $100/\sqrt V$ and $500/\sqrt V$ "become almost 4th-order" with larger errors. $2/\sqrt V$ keeps both the accuracy and the rank of the exact solution, while $1/\sqrt V$ gives higher ranks except on the finest grid (§5.3, Fig. 4). **Shown**
16. Isentropic vortex: equal cost at $40^3$, TT 102 times faster at $320^3$, density compression ratio about $10^{-4}$ on the finest grid; all runs serial (§5.3, Fig. 5). **Shown** (hardware not stated)
17. Manufactured solution: the exact TT ranks are 3 for $\rho$, 5 for the momenta and 7 for $E$. With $\epsilon_{\mathrm{TT}}$ below the line of Eq. (35) ($C_\epsilon=100$) the error is dominated by the discretization; to its left it depends on $\epsilon_{\mathrm{TT}}$ only (§5.4, Fig. 6). **Shown**
18. Manufactured solution with $C_\epsilon=10$: fifth order for every variable ($\rho$ 5.00 at $320^3$); with $C_\epsilon=100$, $E$ drops to fourth order on the finest grid (§5.4, Table 4). **Shown**
19. Manufactured solution at $320^3$: speed-up "slightly less than 65" ($C_\epsilon=100$) and 35 ($C_\epsilon=10$); compression about $10^{-4}$ for density and slightly below $10^{-3}$ for $E$; $\epsilon_{\mathrm{TT}}=\epsilon_{\mathrm{cross}}\approx1.2\times10^{-12}$ on the finest grid, while AMEn cross "usually stagnates at about an error of $10^{-11}$" (§5.4, Fig. 7). **Shown**
20. Sod (3D grid, rank 1): sharp shock and contact; speed-up "more than 1000" and compression "less than $10^{-5}$" at $640^3$; the FT timings at $320^3$ and $640^3$ are extrapolated (§5.5, Fig. 9). **Shown** (speed-up partly extrapolated)
21. Shu–Osher at $200^3$: TT and FT agree, and both under-resolve the high-frequency region; with refinement TT converges to the reference (§5.6, Fig. 10). **Shown**
22. Double Mach reflection: cross interpolation fails for the initial condition, which is built as a sum of $N_y$ rank-1 TTs with rounding, giving an initial rank $\approx N_y\cot(\pi/3)$; the rank grows further as the flow evolves (§5.7). **Shown**
23. Rayleigh–Taylor ($\gamma=5/3$): symmetry is maintained, and the component-wise TT results are "in an excellent agreement" with characteristic-wise results of the literature (§5.8, Fig. 12). **Shown** (visual comparison)
24. A single global $\epsilon_{\mathrm{TT}}$ limits rank control for localized features; a dynamic domain decomposition with different tolerances is suggested, not pursued (§5.8). **Stated**
25. "The traditional WENO-JS scheme could be accelerated up to 1000 times when solved in the TT-format" for low-rank problems (Abstract, §6). **Stated** (rests on claim 20)

*(Compiler check, not in the sources.)* Every order of Tables 1–4, recomputed as
$\log_2(e_{N_x}/e_{2N_x})$ from the printed errors, agrees with the printed order to
within 0.02. In the Burgers test, $u$ depends on $x+y+z$ only, so the breaking time
is $1/(3\pi)$ and the final time $T=1/(12\pi)$ is a quarter of it, consistent with
the text's "well before the breaking time".

# Printed slips

- **Eq. (41)** (double Mach reflection): the post-shock state is assigned "if $x<\frac16$", independent of $y$, although the text describes an oblique shock at $\theta=\pi/3$ meeting the wall at $(1/6,0)$, says that "the location of the discontinuity changes at each $y_j$" and derives the rank $N_y\cot(\pi/3)$ from it (checked on the page image).
- **§5.7:** "The supersonic inflow and subsonic outflow boundary conditions are enforced on the right and left boundaries, respectively", while the post-shock state lies at $x<1/6$ and the shock moves right.
- **Fig. 11 caption:** "at T = 2", while the text runs to $T=0.2$.
- **Eq. (29):** "$\frac12(\rho_{BC}u^2_{BC}+\rho_{BC}v^2_{BC}\rho_{BC}w^2_{BC})$", a "+" missing before the last term (checked on the page image).
- **Eq. (38):** arguments printed "$\rho(x,y,z,y)$", "$u(x,y,z,y)$", … for $(x,y,z,t)$; the energy variable $e$ is not defined.
- **§5.4:** "$r_1=r_2=3$ for $\rho_{TT}$, $r_1=r_2=3$ for $\rho u_{TT}$, $r_1=r_2=5$ for $\rho u_{TT}$, $\rho v_{TT}$, and $\rho w_{TT}$", with $\rho u_{TT}$ listed twice with two ranks.
- **§1:** "first introduced by Lie et al. [24]", for Liu, Osher & Chan.
- **§1:** "In [4], the smoothness indicators of the WENO-JS scheme was modified and the method was given the name WENO-Z"; as recalled by [Li et al. (2022b)](/sources/li-2022-b.md), [Luo & Wu (2021)](/sources/luo-2021-b.md) and [Wang & Don (2022)](/sources/wang-2022-b.md), [WENO-Z](/methods/weno-z.md) keeps the Jiang–Shu $\beta_k$ and changes the unnormalized weights through the global indicator $\tau_5$.
- **§5.2:** "$T=1/12\pi$", read as $1/(12\pi)$ (see the compiler check).
- Typos: "memory compression ration" (§5.5), "Chosing" (§4.6 heading).

# Notation map

| Danis et al. (arXiv v1) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U=(\rho,\rho u,\rho v,\rho w,\rho E)$ | $u=(\rho,\rho v,E)$ | **collision**: $u,v,w$ are velocity components, $v_1,v_2,v_3$ in the registry |
| $F,G,H$; $\hat F,\hat G,\hat H$ | $f^{(1)},f^{(2)},f^{(3)}$; $\hat f$ per direction | **$H$ is the enthalpy, $h$ the numerical flux in the registry** |
| $\alpha=\max\lvert f'(u)\rvert$ | $a$ | global LF speed; **also used for the unnormalized weights** |
| $v_i=f^+(u_i)$ | $f^+(u_i)$ | **collision**: $v$ is the velocity in the registry |
| $S_r$, $r=0,1,2$ ($S_0$ downwind-most) | $S_{2-r}$ | **ordering reversed**: the registry's $S_0$ is the most upwind |
| $d_0,d_1,d_2=\tfrac3{10},\tfrac35,\tfrac1{10}$ | $d_2,d_1,d_0$ | follow the stencil relabelling |
| $\beta_r$, $\alpha_r=d_r/(\beta_r+\varepsilon)^2$, $\omega_r$ | $\beta_k$, $\alpha_k$ with $q=2$, $\omega_k$ | Jiang–Shu form |
| $\varepsilon=\Delta x^2$ | $\epsilon$ | **the same letter is the TT error tensor in Eq. (11)** |
| $v^-_{i+1/2}$ | $\hat f^+_{i+1/2}$ reconstructed from the left | minus = left-biased, as in the registry's $u^-$ |
| $[r_1,r_2]$ | $\mathsf r_1,\mathsf r_2$ (page-local) | **collision** with the stencil size $r$ |
| $\varepsilon_{TT}$, $\varepsilon_{cross}$, $C_\varepsilon$ | $\epsilon_{\mathrm{TT}}$, $\epsilon_{\mathrm{cross}}$, $C_\epsilon$ (page-local) | |
| $T^x,T^y,T^z$ | kept (page-local) | shift operators |
| $L(u)$, $\mathcal F(u)$ | $\mathcal L(u)$, rounded forward-Euler step | |
| $h$ | $\Delta x$ | uniform spacing |
| $\lambda$ | $\nu$ | CFL number, $\Delta t=\nu\Delta x/\max(\lvert v\rvert+c)$ |
| $\gamma$ ("specific heat constant") | $\gamma$ | ratio of specific heats |

# Reference list

The paper prints 39 references, numbered [1]–[39] in alphabetical order, merged
complete into the [bibliography](/bibliography.md) with `citedby` including
`danis-2025`. Ref. [7] (Danis & Alexandrov, LANL report LA-UR-24-24283) prints no
year; it is a different work from this source and does not take the key
`danis-2025` (its report number points to 2024). Refs. [1], [5] and [39] are arXiv
preprints kept as their own entries. Ref. [13] (J. Chem. Phys. 156(2)) has no page
or article number, [23] (Russian J. Numer. Anal. Math. Modelling, 2011) no volume or
pages, and [32] (Shu 1998, pp. 325–432) no book title. No item is unparseable.

# Pages created or updated

Chunk 9 (2026-10-23). This source is cited on:

* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Tensor-train WENO](/methods/tensor-train-weno.md)

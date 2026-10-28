---
type: Source
title: "Vermeire (2024) — High-Order Implicit Large Eddy Simulation using Entropically Damped Artificial Compressibility"
description: "Combines entropically damped artificial compressibility with the FRDG flux reconstruction scheme as a fully explicit incompressible implicit LES, and tests it on the Taylor–Green vortex, a wall-resolved channel at Re_tau 395 and the SD7003 airfoil: suitable up to polynomial degree four, with some instabilities above."
resource: "doi:10.1016/j.compfluid.2023.106065"
source_kind: paper
authors: [Vermeire B.C.]
year: 2024
venue: "Comput. Fluids 268:106065"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Computers_amp_Fluids_Vermeire_High-Order_Implicit_Large_Eddy_Simulation_using_Entropically.pdf"
tags: [implicit-les, flux-reconstruction, high-order, incompressible-flow, numerical-dissipation, taylor-green-vortex]
timestamp: 2026-10-28T11:49:00Z
---

# Summary

Vermeire (2024) names two costs of incompressible LES: the pressure,
which needs a globally coupled Poisson solve or, with Chorin's artificial
compressibility, a pseudo-time sub-iteration at each physical step; and
the resolution demand of low-order schemes. The paper combines Clausen's
entropically damped artificial compressibility (EDAC), which adds a
pressure-diffusion term to the artificial-compressibility pressure
equation and gives a fully explicit system, with the
[flux reconstruction](/methods/flux-reconstruction.md) scheme in its FRDG
variant (lifting-collocation-penalty form, Rusanov flux with the Davis
wave speed, BR2 viscous flux). No subgrid model is used: the
interface upwinding is the subgrid dissipation of an
[implicit LES](/definitions/implicit-les.md). EDAC stays inline on this
page and on the flux-reconstruction and implicit-LES pages.

Three cases vary the polynomial degree $N$ and the incompressibility
factor $M_{\mathrm{AC}}$ at fixed degrees of freedom: the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $Re=1600$
(one quarter and one half of the reference DNS resolution per direction,
$N=1$–6), the wall-resolved
[turbulent channel](/benchmarks/turbulent-channel-flow.md) at
$Re_\tau=395$ ($N=1$–4), and the transitional
[SD7003 airfoil](/benchmarks/sd7003-airfoil.md) at $Re_c=60{,}000$,
$\alpha=8^\circ$ on a coarse 57,100-hexahedron mesh. Accuracy improves
strongly with $N$ at fixed degrees of freedom; $N=1$ is over-dissipative
in the vortex (most of its dissipation is
[numerical](/properties/numerical-dissipation.md)), over-predicts the
channel mean velocity and fully separates the airfoil, while $N\ge2$
captures the [laminar separation bubble](/definitions/laminar-separation-bubble.md)
and $N=4$ matches the reference forces. The divergence error falls about
linearly with $M_{\mathrm{AC}}$ and also with $N$, so high $N$ at a loose
factor beats $N=1$ at a strict one; at $N\ge3$ results are only weakly
sensitive to $M_{\mathrm{AC}}$. The low-resolution vortex runs and most
channel runs at $N\ge5$ oscillate or diverge (the medium-resolution vortex
stays stable up to $N=6$), which the author attributes to insufficient
numerical dissipation. The
conclusion is that EDAC with FR suits low and moderately resolved
implicit LES with $N\le4$. Evidence is numerical only.

# Version read

Version of record (Elsevier; received 18 February 2023, accepted 25
September 2023, online 31 October 2023), 19 pages, all read. Page 1
matches the metadata; no identity issue. Equation, figure, table and
section numbers are those of this version.

# Key claims

Page-local symbols: $M_{\mathrm{AC}}$ the incompressibility factor of
EDAC (the source's $M$, not a Mach number) and $\zeta=1/M_{\mathrm{AC}}^2$;
$N_m$ the degree of the geometry mapping (the source's $p_m$); $E_k$ the
volume-averaged kinetic energy; $\mathcal Z$ the volume-averaged enstrophy
(the source's $\epsilon$); $\psi_{\mathrm{div}}$ the volume-averaged
divergence error; $t_\delta=\delta/u_b$ and $t_c=tu_\infty/c$ the channel
and airfoil convective times.

1. EDAC gives a fully explicit formulation of the incompressible Navier–Stokes equations, without the pseudo-time problem of artificial compressibility and the global coupling of Poisson approaches, which reduces cost and simplifies implementation (§1, citing Clausen [8]). **Stated**
2. EDAC had been used for laminar and well-resolved LES and DNS [8–10], but its suitability for moderately resolved LES "remains to be shown" (§1). **Stated**
3. Implicit LES with FR relies on the numerical dissipation of approximate Riemann solvers at element interfaces, "akin to a numerical dissipation stabilized under-resolved DNS", and moves seamlessly between implicit LES and DNS as the resolution changes (§1). **Stated**
4. Cross-product metrics are free-stream preserving with Gauss solution points and the FRDG correction function provided $N_m\le N$ (§3, citing [30, 31]). **Stated**
5. Vortex: low-order, low-resolution runs over-predict the kinetic-energy dissipation rate significantly; raising $N$ to 4 improves agreement with the reference DNS (Fig. 3, §4.1). **Shown**
6. Vortex, low resolution: $N=5$ agrees better but oscillates after the peak dissipation; at $N=6$ the oscillations grow and the $M_{\mathrm{AC}}=1/5$ and $1/10$ runs become unstable (Fig. 3, §4.1). **Shown**
7. Vortex, medium resolution: raising $N$ up to 6 keeps improving the agreement without instability (Fig. 4, §4.1). **Shown**
8. Vortex: at low $N$ the dissipation rate is over-predicted while the enstrophy is under-predicted, so most of the dissipation is numerical, not physical (Figs. 5–6, §4.1). **Shown**
9. Reducing $M_{\mathrm{AC}}$ increases the numerical dissipation at $N=1$ but reduces it at higher $N$ (Figs. 5–6, §4.1). **Shown**
10. Vortex, low resolution, high $N$: the enstrophy exceeds the reference DNS, suggesting spurious turbulent structures (Fig. 5, §4.1). **Shown**
11. $\psi_{\mathrm{div}}$ decreases approximately linearly with $M_{\mathrm{AC}}$ and also with $N$; the medium-resolution $N=6$, $M_{\mathrm{AC}}=1/5$ run has less divergence error than $N=1$ with $M_{\mathrm{AC}}=1/40$ (Figs. 7–8, §4.1). **Shown**
12. Channel: additional runs at $N=5$ and 6 were mostly unstable, suggesting that the numerical dissipation at these degrees "may not be sufficient for ILES" (§4.2). **Shown** (stability) / **Stated** (cause)
13. Channel: averaging over $1380t_\delta$ after $2760t_\delta$ of start-up converges $Re_\tau$ to within 1% of the target in all cases (§4.2). **Shown**
14. Channel mean velocity: $N=1$ over-predicts $u^+$, most toward the centreline, and reducing $M_{\mathrm{AC}}$ degrades it down to $1/20$ with little change at $1/40$; $N=2$ over-predicts less and is insensitive to $M_{\mathrm{AC}}$; at $N=3$ the low resolution deviates slightly and the medium one agrees well; $N=4$ slightly under-predicts at both resolutions; sensitivity to $M_{\mathrm{AC}}$ is weak for $N\ge3$ (Figs. 11–12, §4.2). **Shown**
15. Channel: the low-resolution $N=4$, $M_{\mathrm{AC}}=1/5$ run was unstable (§4.2). **Shown**
16. Channel: lower-order runs predict larger velocities because the damping of turbulent structures inhibits momentum transport from the centre to the walls (Figs. 9–10, §4.2). **Shown** (observation) / **Stated** (explanation)
17. Channel fluctuations: $N=1$ over-predicts the streamwise and spanwise rms and under-predicts the wall-normal rms near the wall, more so as $M_{\mathrm{AC}}$ decreases; $N=2$ over-predicts all three; $N=3$ and 4 predict all three accurately for every $M_{\mathrm{AC}}$ (Figs. 13–18, §4.2). **Shown**
18. SD7003: $N=1$ gives fully separated flow without a distinct suction-side pressure recovery; $N=2$ shows a laminar separation bubble with attached turbulent flow downstream; $N=3$ moves transition upstream; $N=4$ agrees with the high-order compressible reference at Mach 0.2 [11] (Figs. 20–21, §4.3). **Shown**
19. SD7003 forces (Table 3): $(C_L,C_D)=(0.949,0.110)$, $(1.002,0.045)$, $(0.971,0.041)$, $(0.950,0.046)$ for $N=1$–4; references Vermeire et al. [11] $(0.941,0.049)$, Garmann et al. [38] $(0.969,0.039)$, Beck et al. [39] $(0.932,0.050)$; $N=4$ "shows good agreement while requiring significantly fewer degrees of freedom" (§4.3). **Shown**
20. EDAC with FR is suitable for low and moderately resolved implicit LES with $N\le4$, with instabilities at higher degrees; it is fully explicit, with no coupled solver, no pseudo-time stepping and no explicit SGS model (Abstract, §5). **Shown**
21. Higher-order solutions have lower divergence error even with less strict incompressibility factors (Abstract). **Shown**

The method in registry notation (Eqs. 1–5): the pressure equation
$\partial_tp+u_j\partial_jp+M_{\mathrm{AC}}^{-2}\partial_ju_j=Re^{-1}\partial_j\partial_jp$
is recast with the momentum equations, assuming $\partial_ju_j=0$ and in
dimensional form, as $\partial_t\boldsymbol q+\partial_j(\boldsymbol F_{e,j}+\boldsymbol F_{v,j})=0$
with $\boldsymbol q=(p,u_i)$, $\boldsymbol F_{e,j}=(u_j(p+\zeta),\,u_iu_j+\delta_{ij}p)$,
$\boldsymbol F_{v,j}=-\nu(\partial_jp,\,\partial_ju_i)$, $p$ kinematic.
The FR update at the solution points adds a correction field built from
the jumps between the common and the internal flux at the face flux
points, weighted by lifting coefficients that for FRDG solve Eq. (13) and
recover DG for linear equations; other choices recover energy-stable
[spectral difference](/methods/spectral-difference-method.md), spectral
volume and [DG](/methods/discontinuous-galerkin-spectral-element-method.md)
schemes. Gauss solution points, quadratic mapping ($N_m=2$, or 1 when
$N=1$, see [geometric conservation](/properties/geometric-conservation-law.md)).
Time integration: classical RK4 (vortex), an optimal explicit Runge–Kutta
scheme [36] (channel), paired explicit Runge–Kutta [37] (airfoil). The
channel grid puts the first solution point at $y^+=1$; the code is not
named.

# Printed slips

- **Eqs. (23)–(24):** "$C_L=L/(2\rho_\infty u_\infty^2)$", "$C_D=D/(2\rho_\infty u_\infty^2)$, where $L$ and $D$ are the time average lift and drag coefficients": $L$ and $D$ are the forces being normalized. *(Compiler check, not in the sources: $L/(\rho_\infty u_\infty^2)$ has the dimension of an area, so the printed formula has no reference area.)*
- **Eq. (17):** the Taylor–Green initial pressure is printed $\frac{1}{\gamma Ma^2}+\frac1{16}\cos(2z+2)[\cos(2x)+\cos(2y)]$. *(Compiler check, not in the sources: for the printed velocity of Eqs. (14)–(16), $\frac1{16}(\cos2z+2)(\cos2x+\cos2y)$ satisfies $\nabla^2p=-\partial_iu_j\partial_ju_i$ and the printed $\cos(2z+2)$ does not.)* $\gamma$ is not defined in the paper; $Ma=0.08$ is.
- **§4.2:** the text places the streamwise, wall-normal and spanwise rms "in Figs. 13, 15 and 17 for the coarse resolution simulations and in Figs. 14, 16 and 18 for the medium", while the captions of Fig. 15 and Fig. 17 read spanwise and wall normal.
- **§5:** SD7003 "Lift, drag, and pressure coefficient distributions converged to reference DNS data", while §4.3 calls the references "reference compressible simulations" (FR at $N=4$, sixth-order finite differences, DG at $N=7$).
- **§4.3:** "compressibility factor $M=0.2$", where §2 and §4 call $M$ the "incompressibility factor"; the resolutions are "low" in the set-up and tables, "coarse" in the discussion.
- **§3, Eq. (6):** $\mathbf u^h$ is called "the global piecewise continuous approximation", while the next paragraph says the element-wise polynomials are not continuous across interfaces.
- **§5:** "with higher values of $p_s$ This, combined …" (missing stop); the abstract writes "solutions polynomials".
- **References:** [20] and [24] print the authors "Vermeire CAPereira BC"; [17] "Vermeire B.C. BC"; [31] "Bolduc MP, Ghoreishi BC"; [36] "Nasab S Hedayati"; [6], [26], [27] print the journal "J Comput Fluid Dyn"; [1] prints "135(2):118–25, 118"; [8] and [10] print no page or article number.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $p_s$ | $N$ | solution polynomial degree; order $N+1$ |
| $p_m$ | $N_m$ (page-local) | mapping degree |
| $M$ | $M_{\mathrm{AC}}$ (page-local) | incompressibility factor; **collision** with the Mach number $M$ |
| $Ma$ | $M$ | Mach number of the vortex initial pressure, 0.08 |
| $\zeta=1/M^2$ | $\zeta$ (page-local) | |
| $\mathbf v$, $u_i$; $p$ | $\boldsymbol u$, $u_i$; $p$ | $p$ kinematic |
| $\mathbf u=[p,u_i]^T$ | $\boldsymbol q$ (page-local) | **collision:** bold $\mathbf u$ is not the velocity |
| $\mathbf F_e$, $\mathbf F_v$, $[\hat{\mathbf F}]_{f,l}$ | $\boldsymbol F_e$, $\boldsymbol F_v$; $f^*$ minus the internal flux | interface jump at flux point $l$ of face $f$ |
| $\boldsymbol\xi$ | $\xi_i$ | reference coordinates |
| $\boldsymbol\delta_i$ | (FR correction field) | **collision** with $\delta$ (channel half-height) |
| $\alpha_{j,f,l}$ | (lifting coefficients) | **collision** with the DG blending factor $\alpha$ and the angle of attack |
| $\mathbf J$ | $\mathcal J=\det\mathbf J$ | metric Jacobian |
| $e_k$ | $E_k$ (page-local) | volume-averaged kinetic energy, Eq. (18) |
| $\epsilon$ | $\mathcal Z$ (page-local) | enstrophy with factor 1/2, Eq. (19); **collision** with the dissipation rate $\varepsilon$ |
| $\psi$ | $\psi_{\mathrm{div}}$ (page-local) | divergence error, Eq. (20); not the $k$-$\sqrt kL$ surrogate $\psi$ |
| $\boldsymbol\omega$ | $\omega_i$ | vorticity |
| $u_\tau=\sqrt{\tau/\rho}$, $\delta$ | $u_\tau=\sqrt{\tau_w/\rho_w}$, $\delta$ | |
| $u^+_{rms}$, $v^+_{rms}$, $w^+_{rms}$ | $\langle u'^2\rangle^{1/2}/u_\tau$, … | |
| $Re=u_\infty c/\nu$, $\alpha$ | $Re_c$, $\alpha$ (angle of attack) | |
| $C_L$, $C_D$ | $C_L$, $C_D$ | as printed in Eqs. (23)–(24) |

# Reference list

39 printed references, numbered style, no DOIs. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Same-author same-year works are keyed in printed order (Vermeire
2019 and 2020). Refs. [20] and [24], printed with the author string
"Vermeire CAPereira BC", are keyed `pereira-2020-b` and `pereira-2020-c`;
the "Nasab S Hedayati" item [36] is keyed under Hedayati Nasab. Ref. [34]
(Wang et al., High-order CFD methods: current status and perspective) is
the ingested [wang-2013](/sources/wang-2013.md). Refs. [6], [26], [27]
print the journal "J Comput Fluid Dyn", [1] a duplicated
page, [8] and [10] no pages. No item is unparseable.

# Pages created or updated

Chunk 13 (2026-10-28). This source is cited on:

- [SD7003 airfoil](/benchmarks/sd7003-airfoil.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Laminar separation bubble](/definitions/laminar-separation-bubble.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Flux reconstruction](/methods/flux-reconstruction.md)
- [Spectral difference method](/methods/spectral-difference-method.md)
- [Geometric conservation law and free-stream preservation](/properties/geometric-conservation-law.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)

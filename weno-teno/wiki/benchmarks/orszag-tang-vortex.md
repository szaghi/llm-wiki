---
type: Benchmark
title: "Orszag–Tang vortex"
description: "Periodic two-dimensional ideal-MHD benchmark in which smooth vortical velocity and magnetic fields steepen into interacting shocks and current sheets; used for high-order MHD shock capturing, density-bound limiting, entropy stability, divergence control and long-time robustness, in two normalizations that differ by a rescaling, and in relativistic single-fluid and two-fluid versions."
status: established
aliases: [Orszag–Tang, Orszag–Tang MHD vortex, OT vortex]
tags: [benchmark, mhd, dg, teno, limiting, relativistic]
timestamp: 2026-10-23T11:06:00Z
---

# Orszag–Tang vortex

The Orszag–Tang vortex is the ideal-MHD analogue of a two-dimensional
vortex problem: on a periodic square, a smooth velocity field
$v=(-\sin2\pi y,\ \sin2\pi x)$ (in unit-square coordinates) and a
magnetic field with a doubled $x$ wavenumber are superposed on a
uniform density and pressure. The smooth data steepen into MHD shocks
by the output times, so a scheme must capture them, keep density within
bounds and control $\nabla\cdot B$, while the structure that develops
between the shocks serves as a visual measure of resolution.

## Setup

Two normalizations are printed.

**Unit square.** [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md)
§5.3.1 and [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md)
§6.2 print, on periodic $[0,1]^2$,

$$
\begin{aligned}
\rho&=\frac{25}{36\pi},\qquad p=\frac{5}{12\pi},\qquad
(v_1,v_2)=\big(-\sin(2\pi y),\ \sin(2\pi x)\big),\\
(B_1,B_2)&=\frac{1}{\sqrt{4\pi}}\big(-\sin(2\pi y),\ -\sin(4\pi x)\big),
\end{aligned}
$$

to $t=1$, in GLM-MHD form (divergence cleaning by the field
$\psi_{\mathrm{GLM}}$; $\nabla\cdot B=0$ is not enforced exactly). The
2022 paper does not state $\gamma$; the 2021 paper states $\gamma=5/3$,
$\mu_0=1$ (magnetic permeability, page-local) and a unit sound speed.

**$2\pi$-periodic square.** [Liu et al. (2021)](/sources/liu-2021.md)
§4.2 print, on periodic $[0,2\pi]^2$ with $\gamma=5/3$,
$\rho=\gamma^2$, $p=\gamma$, $v=(-\sin y,\ \sin x,\ 0)$,
$B=(-\sin y,\ \sin2x,\ 0)$, to $t=3$.
[Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) Ex. 5.6 (arXiv v1)
print the same data, with vector potential $\mathsf A_3=0.5\cos2x+\cos y$
(page-local; $B_1=\partial_y\mathsf A_3$, $B_2=-\partial_x\mathsf A_3$ give the printed
field), on $192^2$ points to $T=4$.
[Liu, Feng & Wang (2023a)](/sources/liu-2023.md) §4.3 print the same
data again ($200^2$, contours at $t=3$, slice at $y=0.625\pi$) and run
on to $t=100$.
[Berta et al. (2024)](/sources/berta-2024.md) §5.6 (arXiv v4) print
$\rho=25/9$, $p=5/3$, $(v_1,v_2)=(-\sin y,\ \sin x)$,
$(B_1,B_2)=(-\sin y,\ \sin2x)$, periodic (the domain is not printed),
to $t=2\pi$, the unit-square $t=1$ under the scaling below; their
relativistic-MHD version halves the velocity,
$(v_1,v_2)=(-0.5\sin y,\ 0.5\sin x)$, citing earlier relativistic
papers.

The two are one problem up to a rescaling *(compiler check, not in the
sources)*. Multiplying $\rho$, $p$ and $|B|^2$ of the unit-square data
by $4\pi$ gives $\rho=25/9=\gamma^2$, $p=5/3=\gamma$ and $|B|$ of order
one, and leaves every wave speed unchanged, since ideal MHD is
invariant under a common scaling of $\rho$, $p$ and $|B|^2$ at fixed
velocity; both states have unit sound speed,
$\gamma p/\rho=1$. Stretching $x$ by $2\pi$ at unchanged velocity
stretches $t$ by $2\pi$, so Liu et al.'s $t=3$ corresponds to
$t=3/(2\pi)\approx0.477$ in the unit square, close to the $t=0.5$
snapshots and pressure slices of Rueda-Ramírez et al. (2021); both
unit-square papers run to $t=1$. The printed sign of $B_2$ differs
($-\sin4\pi x$ against $+\sin2x$); no source comments on it.

[Dao & Nazarov (2022)](/sources/dao-2022.md) §5.3 (arXiv v1) and
[Lesur et al. (2023)](/sources/lesur-2023.md) §4.2 (arXiv v1) print the
unit-square data with $\gamma=5/3$ (Dao & Nazarov) and the same
$\rho$, $p$, $v$, but with $B=\frac{1}{\sqrt{4\pi}}\big(-\sin(2\pi y),\
+\sin(4\pi x)\big)$: the sign of $B_2$ of Liu et al., not that of
Rueda-Ramírez et al. Lesur et al. stop at $t=0.5$; Dao & Nazarov run
to $t=0.5$ and on to $t=1.0$, noting that results beyond $t=0.5$ have
"rarely been reported" and that up to $t=0.5$ the problem is easy for
shock-capturing schemes. They state that $t=3.14$ in Tóth's
normalization corresponds approximately to their $t=0.5$, which is the
$2\pi$ time scaling above: $3.14/(2\pi)=0.4997$ *(compiler check, not in
the sources)*.

[Dematté et al. (2024)](/sources/dematte-2024.md) §4.1.5 mix the two:
on the unit square $[0,1]^2$ they print the $2\pi$-periodic amplitudes,
$\rho=\gamma^2$, $p=\gamma$, $v=(-\sin2\pi y,\ \sin2\pi x,\ 0)$,
$B=(-\sin2\pi y,\ \sin4\pi x,\ 0)$, $\gamma=5/3$, and output at
$t=0.5/2\pi$, $2/2\pi$, $3/2\pi$ and $5/2\pi$, i.e. Liu et al.'s times
under the $2\pi$ time scaling. In the rescaling above this is the
$2\pi$-periodic problem shrunk to the unit square *(compiler check,
not in the sources)*.

**Relativistic single-fluid version.** [Ding & Wu (2024)](/sources/ding-2024-b.md)
Example 5.5 run relativistic MHD on periodic $[0,2\pi]^2$ with
$\rho=1$, $v=A(-\sin y,\ \sin x,\ 0)$, $A=0.99/\sqrt2$, so the maximum
Lorentz factor is about $7.09$, $B=(-\sin y,\ \sin2x,\ 0)$, $p=10$, and
the equation of state $h=\tfrac{5p}{2\rho}+\sqrt{1+\tfrac94(p/\rho)^2}$
they label TM, on $600^2$ cells, with $\log\rho$ and $W$ shown at $t=2.82$
and $6.85$ (Fig. 6).

**Three-dimensional versions.** Dao & Nazarov §5.4, after Helzel et
al., extend the 2D data with $v_3=0$, $B_3=0$ and add the velocity
perturbation $\big(-a\sin2\pi z\sin2\pi y,\ a\sin2\pi z\sin2\pi x,\ a\sin2\pi z\big)$
with $a=0.2$ (page-local), periodic, to $t=0.5$. Lesur et al. §5 use
another 3D field as their performance test: on the periodic unit cube
with the 2D $\rho$ and $p$,
$v=\big(-\sin2\pi y,\ \sin2\pi x+\cos2\pi z,\ \cos2\pi x\big)$ and
$B=B_0\big(-\sin2\pi y,\ \sin4\pi x,\ \cos2\pi x+\sin2\pi y\big)$,
$B_0=1/\sqrt{4\pi}$, to $t=1$.

[Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) §5.3.2
(arXiv v2) also compute on periodic $[0,1]^2$ with $\gamma=5/3$ to
$t=0.48$, with $v$ as above and $B=\frac1{\sqrt{4\pi}}\big(-\sin(2\pi y),\
\sin(2\pi x)\big)$, but print $\rho=\tfrac{25}{36}\pi$ and
$p=\tfrac{5}{12}\pi$, with $\pi$ in the numerator. These printed data
are not a rescaling of the other two: the sound speed is still 1, but
$2p/\lvert B\rvert^2$ is $\pi^2$ times larger, and $B_2$ has the
wavenumber of $v$ instead of the doubled one *(compiler check, not in
the sources)*. The pressure axis of their own Fig. 14 (slice at
$y/L=0.3125$, which they state agrees with Jiang & Wu's published
slice) is labelled from $0.0$ to $0.3$: the magnitude of the
$p=5/(12\pi)\approx0.133$ printed by Rueda-Ramírez et al., not of
$5\pi/12\approx1.31$. Against that figure and the other sources'
printed data the placement of $\pi$ is a printed slip *(compiler
check, not in the sources)*; the $B_2$ wavenumber cannot be checked
from the paper. Their $t=0.48$ is the unit-square counterpart of Liu et
al.'s $t=3$ to two digits.

[Dzanic & Witherden (2023)](/sources/dzanic-2023.md) §5.3, Eq. (43)
(arXiv v2) print the unit-square data with $\gamma=5/3$,
$\rho=25/(36\pi)$, $p=5/(12\pi)$ and $B_2=-\sin(4\pi x)/\sqrt{4\pi}$, as
Rueda-Ramírez et al., but $B_1=+\sin(2\pi y)/\sqrt{4\pi}$, the opposite
sign of $B_1$ to every other source; their pressure slice agrees with
Jiang & Wu's, and whether the sign is a slip cannot be decided from the
paper *(compiler check, not in the sources)*. They show density at
$t=0.5$ and the slice at $y=0.3125$, $t=0.48$.

**Relativistic two-fluid version.** [Bhoriya, Kumar & Chandrashekar (2023)](/sources/bhoriya-2023.md)
§6.2.1 (arXiv v2) run the unit-square vortex for two relativistic
fluids (ions and electrons) coupled to Maxwell's equations: each
species with density $25/(72\pi)$, pressure $5/(24\pi)$ and velocity
$\big(-\tfrac12\sin2\pi y,\ \tfrac12\sin2\pi x\big)$, $B=(-\sin2\pi y,\ \sin4\pi x)$,
electric field $-v\times B$ of the ions, charge-to-mass ratios
$\pm10^3/\sqrt{4\pi}$ (skin depth about $3.0\times10^{-3}$),
$\gamma=5/3$, $200^2$ cells, CFL 0.45, to $t=1$ (divergence to $t=2$).

[Fu (2023)](/sources/fu-2023.md) §5.3 reproduces Orszag–Tang results
from the TENO-MHD paper it reviews, on $200\times200$, with a
WENO5-JS reference on $512\times512$ and 30 density contours from 1.1
to 6.3, without reprinting the data; the reviewed work (Fu & Tang) uses
an unstaggered constrained-transport framework for the [divergence-free](/properties/divergence-free-magnetic-field.md)
constraint.

## Runs in the sources

| Source | Scheme | Grid | Divergence treatment |
|---|---|---|---|
| [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) §5.3.1 | split-form [DGSEM](/methods/dgsem.md), $N=3$, Chandrashekar–Klingenberg volume flux, LLF surface flux, subcell-wise [FV blending](/methods/subcell-finite-volume-limiting.md) | $256^2$ elements | GLM cleaning |
| [Fu (2023)](/sources/fu-2023.md) §5.3, Fig. 19 (reproduced) | [TENO-A](/methods/adaptive-teno.md), 5 to 8 points | $200^2$ | constrained transport |
| [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) §6.2 | entropy-stable DGSEM, $N=3$ and $7$, element-wise blending with first-order FV or the TVD-ES [subcell scheme](/methods/tecno-scheme.md), indicator on $p$; code [FLUXO](/software/fluxo.md) | $256^2$, $512^2$, $1024^2$ DOFs | GLM cleaning with Powell and GLM non-conservative terms |
| [Liu et al. (2021)](/sources/liu-2021.md) §4.2 | finite-volume [WLS-ENO](/methods/wls-eno.md), locally divergence-free, second and third order, HLL flux, positivity-preserving framework | $200^2$ (both orders), $600^2$ (second order) | locally divergence-free reconstruction plus Godunov–Powell source term |
| [Liu, Feng & Wang (2023a)](/sources/liu-2023.md) §4.3 | one-step HLL [generalized Riemann problem](/methods/generalized-riemann-problem.md) finite volumes with the WLS-ENO reconstruction, compared with forward-Euler and SSP-RK2 HLL; Barth–Jespersen-type limiter on $\rho$, $p$; CFL 0.8, 100 cores | $200^2$ | locally divergence-free reconstruction plus Godunov–Powell source term |
| [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) §5.3.2 | flux reconstruction, $\mathbb P_7$, vector-valued residual-based [artificial viscosity](/methods/artificial-viscosity.md), $c_\mu=3$ | $32^2$, $64^2$ elements | none stated |
| [Dao & Nazarov (2022)](/sources/dao-2022.md) §§5.3–5.4 | continuous Galerkin $\mathbb P_1$, $\mathbb P_3$ with residual-based [artificial viscosity](/methods/artificial-viscosity.md), RK4, CFL 0.3 | $450\times450$ nodes (2D), $120^3$ nodes ($\mathbb P_3$, 3D) | projection cleaning; pseudo-time and hyperbolic (GLM) cleaning compared |
| [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) Ex. 5.6 | semi-implicit IMEX fifth-order finite-difference WENO, all-Mach formulation at $\varepsilon=1$ | $192^2$ | constrained transport through $\mathsf A_3$ |
| [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) §5.3 | nodal DG / flux reconstruction, $\mathbb P_3$, positivity-preserving [entropy filtering](/methods/entropy-filtering.md) | $64^2$, $128^2$, $256^2$ elements, $\Delta t=4,2,1\times10^{-4}$ | Powell source term |
| [Bhoriya, Kumar & Chandrashekar (2023)](/sources/bhoriya-2023.md) §6.2.1 | [entropy-stable](/properties/entropy-stability.md) finite differences, orders 3 and 4, IMEX | $200^2$ | hyperbolic (perfectly hyperbolic Maxwell) cleaning |
| [Berta et al. (2024)](/sources/berta-2024.md) §5.6 | fourth-order finite volume, pointwise MP5 or WENO-Z (LINEAR second-order comparison), Roe or HLLD with UCT-HLLD (MHD), GFORCE with UCT-GFORCE (RMHD), SSPRK(5,4), CFL 0.5 | MHD $64^2$, $512^2$; RMHD $128^2$, $1024^2$ | upwind constrained transport |
| [Dematté et al. (2024)](/sources/dematte-2024.md) §4.1.5, §4.5 | cell-centred [semi-implicit all-Mach](/methods/semi-implicit-all-mach-scheme.md) finite volume, explicit Rusanov advection with MUSCL–Hancock, implicit pressure sub-system by Picard iterations and GMRES, CFL 0.8 on the flow speed | $1000^2$ | unstaggered constrained transport from a vector potential |
| [Ding & Wu (2024)](/sources/ding-2024-b.md) Ex. 5.5 | $\mathbb P^2$ bound-preserving, locally divergence-free central DG for relativistic MHD, SSP-RK3, CFL 0.25, locally divergence-free WENO limiter in troubled cells | $600^2$ | locally divergence-free spaces plus a symmetrization source on the jumps of the normal field |
| [Lesur et al. (2023)](/sources/lesur-2023.md) §4.2, §5 | second-order Godunov finite volume of [IDEFIX](/software/idefix.md), primitive reconstruction (linear, LimO3, PPM), HLLD or Roe, RK2/RK3 | $128^2$, reference $1024^2$ (as captioned) | constrained transport |

## Findings

**Bounds that can always be met.** Rueda-Ramírez et al. (2022) impose on
density a local discrete maximum principle ("TVD-like" bounds, Eq.
(53)) taken from the low-order solution of the next Runge–Kutta stage,
following earlier work. Because the low-order finite-volume methods are
monotone in primitive variables, these bounds can always be met.
Second-order finite volumes (minmod on primitive variables) give looser
bounds than first-order ones, hence less limiting and more turbulent
structures (Figs. 10–11). The same paper applies the blending to the
[KPP problem](/benchmarks/kpp-rotating-wave.md), the
[Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
and the [high-Mach jet](/benchmarks/high-mach-astrophysical-jet.md),
with different bounds for each.

**Second-order subcells and convergence to a reference code.**
Rueda-Ramírez et al. (2021) first run pure finite volumes ($\alpha=1$)
on $256^2$ DOFs with $N=7$ at $t=0.5$: the entropy-stable TVD
reconstruction resolves more and imprints the irregular
Legendre–Gauss–Lobatto subcell mesh less than first-order FV, and of
three treatments of the boundary subcells the one without boundary
reconstruction is best (Fig. 6). The blended scheme then converges with
resolution towards Athena solutions (second-order FV, constrained
transport, Rusanov flux, $1024^2$ and $2048^2$) in pressure slices at
$y=0.3125$ and $y=0.4277$; $N=7$ captures some features better than
$N=3$ and needs a smaller blending coefficient (Figs. 7–10). The total
mathematical entropy stays constant while the solution is smooth and
decreases once shocks form (Fig. 11); see
[entropy stability](/properties/entropy-stability.md).

**Divergence and energy without a limiter.** Liu et al. use no limiter
besides the positivity-preserving one: their locally divergence-free
WLS-ENO captures the shocks sharply (density profiles along
$y=0.625\pi$, shocks near $x=0.5$, $1.6$, $4.4$), keeps the divergence
norm controlled over time and conserves total energy to a relative
deviation within $10^{-5}$ at third order on $200^2$ (Figs. 5–8).

**Long-time robustness of a one-step GRP scheme.** Liu, Feng & Wang
show density and pressure contours at $t=3$ (ranges $[1.4,5.8]$ and
$[0.6,6.2]$, 30 levels) and the slice at $y=0.625\pi$ (Figs. 4–5), then
run to $t=100$ "(can continue to run)" with no negative pressure or
density, recording the evolution of the kinetic and magnetic energies
(Fig. 6). They set this against Jiang & Wu (1999), whom they cite as
reporting that "negative pressure may be generated beyond t = 3.9"; the
schemes differ, so this is a comparison of robustness, not a
contradiction. The HLL-GRP divergence norm is "almost relatively low"
compared with the forward-Euler and RK2 schemes (Fig. 7).

**Component-wise viscosity.** Dzanic et al. use the problem to show
the benefit of a vector-valued viscosity: the density component and
the magnetic component of their artificial viscosity are "particularly
distinct", since hydrodynamic and magnetic shocks occur independently,
so dissipation is added only to the components that need it (Fig. 13).
The pressure slice at $y/L=0.3125$ agrees well with Jiang & Wu on
$64^2$ elements and is over-diffused at small scales on $32^2$
(Figs. 12, 14).

**Long times and divergence cleaning in continuous finite elements.**
Dao & Nazarov capture all shocks "locally and accurately" with
$\mathbb P_1$ and $\mathbb P_3$ to $t=1.0$ with unchanged parameters;
printed ranges are $\rho_h\in[0.0814,\,0.495]$ ($\mathbb P_1$, $t=0.5$)
and $[0.0377,\,0.419]$ ($\mathbb P_3$, $t=1.0$), the artificial
viscosity below $4.2\times10^{-4}$, and $\mathbb P_3$ reproduces a
twisting central density upsurge seen with a third-order DG scheme
(Figs. 3–4). Without cleaning, they state, the solution breaks near
$t\approx0.7$ on a fine mesh. On a coarse $40\times40$ $\mathbb P_1$
run, projection, pseudo-time stepping (10 pseudo-iterations) and
hyperbolic cleaning all keep $\int\lvert\nabla\cdot B_h\rvert$ small,
pseudo-time stepping being best and costliest (Fig. 5); up to $t=0.5$
cleaning makes no noticeable difference. The 3D run reproduces the 2D
solution in its $z=0$ cut (Fig. 6). See
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md).

**Solver combinations and performance in a Godunov code.** Lesur et al.
compare density cuts at $y=0.316$ and $y=0.425$ across reconstruction,
Riemann solver and time stepper: RK3 with PPM and Roe is the most
accurate combination at a given resolution, and constrained transport
keeps $\lvert\nabla\cdot B\rvert\ll10^{-12}$ in all runs (Figs. 10–11).
The 3D field is their performance benchmark (HLLD, linear
reconstruction, RK2, double precision): 41.3 Mcell/s on a dual AMD Rome
node, 25.0 on a dual Intel Cascade Lake node, 484 on four V100 GPUs and
1240 on four MI250X, i.e. 19.3 and 49.6 times the Cascade Lake node
(they print 19.3 for $484/25.0=19.36$ *(compiler check, not in the
sources)*), with weak-scaling efficiency above 80 % on V100 and AMD
Rome and above 95 % on MI250X (Table 4, Fig. 18).

**Positivity filtering in DG.** Dzanic & Witherden find minor density
oscillations on the coarse meshes that vanish with refinement,
virtually none on $256^2$; $\lvert\nabla\cdot B\rvert$ concentrates at
strong gradients and decreases with resolution; the filter acts mostly
at discontinuities, with spurious activation in smooth regions
decreasing with refinement; the pressure slice agrees with Jiang & Wu's
WENO result (Figs. 3–6).

**IMEX all-Mach scheme in the compressible regime.** Chen, Wu & Xiong
show density at $T=0.5,2,3,4$ and a pressure cut along $y=0.625\pi$ at
$T=3$, in agreement with the explicit constrained-transport results
they cite (Figs. 5.2–5.3).

**Entropy and divergence in the two-fluid version.** Bhoriya et al.
find results comparable to Balsara et al.'s two-fluid computations;
the entropy decays sharply from about $t\approx0.4$, when
discontinuities form, the third-order scheme dissipating slightly more
than the fourth; the divergence error concentrates at discontinuities
with similar $L^1$ norms for both orders up to $t=2$ (Figs. 4–7).

**Magnetic islands as a dissipation probe.** Berta et al. show the
thermal pressure at $t=2\pi$ (Figs. 9–10). In MHD at only 64 points
the fourth-order scheme with MP5 and HLLD resolves a magnetic island
(an O-point) in the central current sheet; they recall that the
tearing instability develops on ideal time scales only if the
numerical dissipation is low enough. As a scalar proxy they use the
normalized pressure maximum $\max(p)/\langle p\rangle$ at the end of
the run, which grows with resolution: MP5 with HLLD against LINEAR
gives an average effective-resolution gain of about 2.23, hence a
speedup of about 2.58 once the 4.3 times higher cost per cell update
is counted ($2.23^3/4.3=2.58$ *(compiler check, not in the
sources)*), which they call "only a rough estimate". In RMHD the
schemes do not differ visibly at 128 points, while at 1024 points the
fourth-order runs produce several, still unresolved, O-points in the
high-pressure filament. See
[numerical dissipation](/definitions/numerical-dissipation.md).

**Velocity-based time step.** Dematté et al. report results in line with
the literature at their four output times (Fig. 9). In the same run the
normalized residuals of the nested Picard iterations stay between
$10^{-12}$ and $10^{-4}$ with two iterations per loop, and the GMRES
solves of the magnetic and pressure systems need fewer than ten
iterations per step (§4.5, Figs. 21–22).

**Bound preservation in relativistic MHD.** Ding & Wu's central DG code
fails at $t\approx2.196$ without the bound-preserving limiter; with it,
the relative global divergence error, which adds the normal jumps of
$B$ across cell edges to the divergence inside the cells, stays at order $10^{-4}$, and the relative local
error, inside the cells, stays zero (Figs. 6, 7a, 7d; see
[bound preservation](/properties/bound-preservation.md),
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).

**Adaptive dissipation at high order.** Fu (2023) shows TENO5-A to
TENO8-A on $200^2$ against WENO5-JS on $512^2$, as evidence that the
adaptive TENO family carries over to MHD with constrained transport
(Fig. 19).

## Qualifications

- All fourteen sources compare contour plots or slices; none reports an
  error norm (Berta et al.'s normalized pressure maximum is a scalar
  proxy, not an error). Rueda-Ramírez et al. (2021) compare with another code,
  Dzanic et al. with another paper's slice.
- Lesur et al.'s text gives the 2D resolution as "$128^3$, plus a
  reference case at $512^3$", their captions $128^2$ and $1024^2$; the
  captions are taken here. Dao & Nazarov's Fig. 3(c) caption reads
  $t=0.5$ for a panel whose printed range and the text place at
  $t=1.0$.
- Dao & Nazarov's cleaning ranking rests on one coarse $\mathbb P_1$ run
  without timings; the break-up at $t\approx0.7$ is stated, not shown.
- Dzanic et al. refer to the Orszag–Tang density contours as "Fig. 7",
  which is their explosion test; the contours are their Fig. 12.
- Fu (2023) is a review: the run is reproduced from the cited TENO-MHD
  work and its setup is not reprinted, so grid, time and data
  differences between the runs cannot be checked from the bundle.
  Its contour range, 1.1 to 6.3, lies far above the uniform initial
  density $25/(36\pi)\approx0.221$ of the unit-square normalization and
  brackets the uniform density $\gamma^2=25/9\approx2.78$ of the
  $2\pi$-periodic one, which points to that normalization *(compiler
  check, not in the sources)*.
- Liu et al. cite "Orszag-Tang (1979)" without a reference-list entry.

# Citations

- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §5.3.1, Eq. (53), Figs. 10–11 (arXiv v2).
- [Fu (2023)](/sources/fu-2023.md) — §5.3, Fig. 19 (reproduced).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §6.2, Figs. 6–11 (arXiv v1).
- [Liu et al. (2021)](/sources/liu-2021.md) — §4.2, Figs. 5–8.
- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — §5.3.2, Figs. 12–14 (arXiv v2).
- [Dao & Nazarov (2022)](/sources/dao-2022.md) — §§5.3–5.4, Figs. 3–6 (arXiv v1).
- [Lesur et al. (2023)](/sources/lesur-2023.md) — §4.2, §5, Table 4, Figs. 10–11, 18 (arXiv v1).
- [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) — Ex. 5.6, Figs. 5.2–5.3 (arXiv v1).
- [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) — §5.3, Eq. (43), Figs. 3–6 (arXiv v2).
- [Bhoriya, Kumar & Chandrashekar (2023)](/sources/bhoriya-2023.md) — §6.2.1, Figs. 4–7 (arXiv v2).
- [Liu, Feng & Wang (2023a)](/sources/liu-2023.md) — §4.3, Figs. 4–7.
- [Berta et al. (2024)](/sources/berta-2024.md) — §5.6, Figs. 9–10 (arXiv v4).
- [Dematté et al. (2024)](/sources/dematte-2024.md) — §4.1.5, §4.5, Figs. 9, 21–22.
- [Ding & Wu (2024)](/sources/ding-2024-b.md) — Example 5.5, Figs. 6–7.

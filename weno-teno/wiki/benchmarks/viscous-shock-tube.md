---
type: Benchmark
title: "Viscous shock tube (Daru–Tenaud)"
description: "Two-dimensional Navier–Stokes shock tube of Daru and Tenaud in a closed box [0,1]×[0,0.5] with a 100:1 density and pressure jump at Reynolds number 200, 1000 and above; the Mach 2.37 shock reflects from the end wall, interacts with the boundary layer and forms a lambda-shock and a primary vortex, a test of viscous discretizations, shock capturing and resolution."
status: established
aliases: [Daru–Tenaud viscous shock tube, viscous shock-tube problem, shock–boundary-layer interaction in a shock tube]
tags: [benchmark, low-dissipation, finite-difference, dg]
timestamp: 2026-10-23T15:15:00Z
---

# Viscous shock tube (Daru–Tenaud)

A closed two-dimensional shock tube is filled with a gas at rest, with
a diaphragm at $x=0.5$ separating a high state on the left from a state
with one hundredth of its density and pressure (equal temperature) on
the right. The shock runs to the right wall, reflects, and meets the
boundary layer that the contact and the shock have left on the bottom
wall. The interaction separates the boundary layer, forms a
lambda-shaped shock foot and rolls the separated layer into a primary
vortex near $x\approx0.75$, with a smaller vortex system near the right
wall. Because the flow is viscous, a grid-converged solution exists at
finite Reynolds number, so schemes can be compared against a fine
reference rather than only against each other. Only the lower half of
the tube is computed, with a symmetry condition on top.

## Data

| | [Chamarthi (2023a)](/sources/chamarthi-2023.md) Ex. 4.1; [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) Ex. 3.10 | [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) §5.2.2 |
|---|---|---|
| domain | $[0,1]\times[0,0.5]$ | $[0,1]\times[0,0.5]$ |
| left state ($x<0.5$), $(\rho,v_1,v_2,p)$ | $(120,0,0,120/\gamma)$ | $(120,0,0,120/\gamma)$ |
| right state | $(1.2,0,0,1.2/\gamma)$ | $(1.2,0,0,1.2/\gamma)$ |
| $\gamma$, viscosity | $\gamma=7/5$, $\mu=1/1000$, $\mathrm{Re}=1000$ | $\mu=10^{-3},\,5\cdot10^{-4},\,2\cdot10^{-4},\,10^{-4}$ |
| boundaries | walls, symmetry on top | no-slip adiabatic walls, slip adiabatic top |
| final time | $t=1$ (also $t=0.5$ in Chamarthi 2023a) | $t=1$ |
| discretization | $1280\times640$ points, conservative finite differences | $\mathbb P_4$ flux reconstruction, $800\times400$ elements |
| reference | grid-converged $4000\times2000$ solution of the cited study | Guermond et al., qualitative |

**Reynolds number 200.** Three further sources run the same states on
$[0,1]\times[0,0.5]$ to $t=1$ at $\mathrm{Re}=200$:

| Source | Boundaries | Prandtl number | Grid | Reference |
|---|---|---|---|---|
| [Liu et al. (2023b)](/sources/liu-2023-b.md) §5.5, Eq. (47) | adiabatic no-slip walls; constant viscosity | 0.73 | uniform quadrilaterals, $h=1/250$, $1/500$ | high-order gas-kinetic scheme on $1500\times750$ |
| [Zhao, Ji, Shyy & Xu (2023)](/sources/zhao-2023.md) §4.8 | symmetric top, no-slip adiabatic walls elsewhere; $\mu=0.005$ | 1 | triangles, $h=1/400$ | non-compact high-order gas-kinetic scheme at $h=1/720$ |
| [Wang et al. (2023c)](/sources/wang-2023-c.md) Example 4.10 | constant viscosity | 0.73 | $800\times400$, CFL 0.3 | — |

**Reynolds numbers 1000 and 10000 on quadrilaterals.**
[Lin, Chan & Tomas (2023)](/sources/lin-2023.md) §8.5 (arXiv v2) run
$\gamma=1.4$, $\mathrm{Pr}=0.73$, a reflective wall on top and adiabatic
no-slip walls on the bottom and sides, $2K_{1D}\times K_{1D}$
quadrilaterals ($K_{1D}$ the number of elements across the height 0.5,
page-local), $T=1$, CFL 0.5, with $N=1,2,3$ each on $K_{1D}=150$, $200$, $300$ at $\mathrm{Re}=1000$ (Fig. 12)
and $N=2$, $K_{1D}=200$ at $\mathrm{Re}=1000$ and $10000$; diagnostic is
a numerical schlieren
$\exp\!\big(-10(g-g_{\min})/(g_{\max}-g_{\min})\big)$ with $g=\lVert\nabla\rho\rVert$.

**DG with non-uniform subcell limiting.** [Deng, Jiang & Yan (2025)](/sources/deng-2025.md)
§4.6, Eq. (4.11), run $(120,0,0,120/\gamma)$ for $x\le0.5$ and
$(1.4,0,0,1.2/\gamma)$ beyond, as printed, on $[0,1]\times[0,0.5]$ with a
symmetry condition on top and no-slip adiabatic walls elsewhere, at
$\mathrm{Re}=1000$ to $t=1$, with fourth-order DG on $750\times375$
elements: BR2 viscous terms in the DG elements, second-order central
differences in the finite-volume subcells, and non-uniform
[ROUND](/methods/round-scheme.md) reconstruction in troubled elements;
$\gamma$ and $\mathrm{Pr}$ are not printed.

Chamarthi (2023a) states the shock Mach number as 2.37; the shock-tube
relation for a pressure ratio of 100 between equal-temperature states
of one gas with $\gamma=1.4$ gives a shock pressure ratio of 6.39 and
$M=2.371$ *(compiler check, not in the sources)*.

## Runs and findings

**Viscous fluxes and odd–even decoupling.** Chamarthi (2023a) uses the
case to test the [α-damping viscous flux](/methods/alpha-damping-viscous-flux.md):
with Shen & Zha's sixth-order viscous scheme, which does not damp the
highest wavenumbers, the TENO5 run shows saw-tooth oscillations at
$t=0.5$, while every α-damping run is free of odd–even decoupling
(Figs. 4–5).

**Resolution of the gradient-based schemes.** Among TENO5, MEG6 and MIG4
([gradient-based reconstruction](/methods/gradient-based-reconstruction.md)),
MIG4 comes closest to the fine-grid primary vortex (Chamarthi 2023a,
Fig. 5). Chamarthi (2023b) repeats the case with the seventh-order MEG7:
the seventh-order mapped explicit [WCNS](/methods/weighted-compact-nonlinear-scheme.md)
baseline (WCNS7M) deviates significantly at the primary vortex near
$x=0.75$ and at the right-wall vortex system, and MEG7 is much closer to
the $4000\times2000$ reference (Fig. 13).

**Positivity-only limiting of entropy-stable DG.** Lin, Chan & Tomas
run entropy-stable DG blended elementwise with a low-order
positivity-preserving scheme (bound relaxation $\zeta_{\mathrm r}=0.1$, their $\zeta$, no shock capturing): all runs
are robust, $N=2$ and $3$ oscillate more near the shock than $N=1$ at
equal degrees of freedom, and the higher-order solutions resemble the
fine-grid references they cite, but do not converge uniformly to them
($N=3$, $K_{1D}=200$ differs near $x\in[0.45,0.65]$ at the bottom wall,
while they state that the $N=3$ runs at $K_{1D}=100$ and $300$ resemble the
reference; Fig. 12 shows $K_{1D}=150$, $200$, $300$). Adding Persson–Peraire-type shock-capturing blending changes
the shock structure in $[0.45,0.64]\times[0.04,0.18]$ and the boundary
layer below it substantially, and these results "appear to be
incorrect" against the references; the relaxation factor $\zeta_{\mathrm r}$
matters little at $\mathrm{Re}=1000$, more at $10000$ (Figs. 13–14). See
[convex limiting](/methods/convex-limiting.md) and
[artificial viscosity](/methods/artificial-viscosity.md).

**Primary vortex at $\mathrm{Re}=200$.** Liu et al. (2023b) compare the
height of the primary vortex (Table 2): 0.166 with their implicit
fourth-order [RBF differential-quadrature](/methods/rbf-differential-quadrature.md)
finite volumes and with LSFD-FV on $h=1/500$, 0.161 with their
second-order scheme on the same mesh, against 0.168 (M-AUSMPW+), 0.166
(compact high-order gas-kinetic scheme) and 0.165 (WENO gas-kinetic
scheme) from the literature. In the bottom-wall density both
fourth-order solvers on $h=1/250$ beat the second-order one on $h=1/500$,
and IRBFDQ-FV is more accurate than LSFD-FV at $h=1/500$ (Fig. 13).
Zhao et al. find that their fourth-order compact
[gas-kinetic scheme](/methods/gas-kinetic-scheme.md) resolves the
lambda shock and vortices on $h=1/400$ without troubled-cell detection
and in the lower-wall density outperforms a third-order CPR gas-kinetic
scheme on $h=1/500$ that needs it (Figs. 13–14). Wang et al. (2023c)
capture the thin boundary layer, the reflected shock, the lambda shock
and the separation bubble with their hybrid multi-resolution
[WCNS](/methods/weighted-compact-nonlinear-scheme.md), whose switch marks
the points that need the nonlinear interpolation, at 0.85 of WENO-JS's
CPU time (Fig. 4.18, Table 5.1).

**Cost.** This is the most expensive case of both Chamarthi papers. Chamarthi
(2023a, Table 1) prints wall-clock times of 58680 s for TENO5 with
compact viscous gradients (ratio 1.147 to MIG4), 50880 s for TENO5 with
explicit gradients (0.994), 48506 s for MEG6 (0.948) and 51146 s for
MIG4 (1). Chamarthi (2023b, Table 2) prints 35455 s for MEG7-prim,
38062 s for MEG7-cons and 70082 s for WCNS7M, and calls MEG7 "twice as
fast" here because the gradients are shared between the inviscid and
viscous fluxes. Neither paper names the hardware.

**A positivity fix at start-up.** Deng, Jiang & Yan's run fails at
the start on negative density or pressure until they add an a
posteriori fix: where a negative value appears at a Gauss volume point,
the finite-volume subcells are recomputed with the first-order Godunov
scheme; the fix is triggered only in the initial stage, and the
results agree with Daru & Tenaud's along the bottom wall and along
$y=0.05$ (Figs. 18–19); see
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)
and [bound preservation](/properties/bound-preservation.md).

**Positivity filtering at higher Reynolds number.** Dzanic & Witherden
run four viscosities with [entropy filtering](/methods/entropy-filtering.md)
in [flux reconstruction](/methods/flux-reconstruction.md): agreement with
Guermond et al. is good, small-scale features are more pronounced at
high Reynolds number, the filter acts sporadically, and about 16
elements need the positivity re-filter after the viscous step, with
filter strength about $10^{-4}$ (Figs. 8–9).

## Qualifications

- All comparisons are visual (density contours, vortex position,
  bottom-wall density); no error norm is given.
- Zhao et al. use $\mathrm{Pr}=1$ where the other $\mathrm{Re}=200$
  sources use 0.73; they also describe the flow as "bounded in a unit
  square cavity" while computing the lower half $[0,1]\times[0,0.5]$
  with a symmetry top (arXiv v1).
- Lin, Chan & Tomas print the high state $(120,0,0,120/\gamma)$ for
  "$x>0.5$", the right half, where every other source puts it on the
  left. They also state that $(N,K_{1D})=(1,300)$, $(2,200)$ and
  $(1,150)$ have the same 720000 degrees of freedom; with
  $(N+1)^2$ nodes on $2K_{1D}^2$ quadrilaterals the first two give
  720000 and the third 180000, while $(3,150)$ gives 720000, the
  configuration their next sentence compares *(compiler check, not in
  the sources)*.
- Chamarthi (2023a) and (2023b) are read as arXiv preprints. In
  Chamarthi (2023a) the text attributes the tridiagonal solve to the
  TENO5/explicit-gradient run, whereas the compact (tridiagonal)
  gradients belong to MIG4; Chamarthi (2023b) prints a normalized
  WCNS7M time of 1.97 for the ratio $70082/35455=1.977$
  *(compiler check, not in the sources)*.
- Deng, Jiang & Yan print the right density as $1.4$ with pressure
  $1.2/\gamma$; Chamarthi (2023a, 2023b) and Dzanic & Witherden print
  the equal-temperature state $(1.2,0,0,1.2/\gamma)$, one hundredth of
  the left state, and Deng, Jiang & Yan compare with Daru & Tenaud's
  results for this problem.
- Dzanic & Witherden compare with a different reference
  (Guermond et al.) at the same and higher Reynolds numbers; their
  results and Chamarthi's are not compared with each other.

# Citations

- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — Ex. 4.1, Table 1, Figs. 4–5 (arXiv v2).
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — Ex. 3.10, Table 2, Fig. 13 (arXiv v1).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §5.2.2, Figs. 8–9.
- [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) — §8.5, Eqs. (68)–(69), Figs. 12–14 (arXiv v2).
- [Liu et al. (2023b)](/sources/liu-2023-b.md) — §5.5, Eq. (47), Table 2, Fig. 13.
- [Zhao, Ji, Shyy & Xu (2023)](/sources/zhao-2023.md) — §4.8, Figs. 13–14 (arXiv v1).
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — Example 4.10, Fig. 4.18, Table 5.1.
- [Deng, Jiang & Yan (2025)](/sources/deng-2025.md) — §4.6, Eq. (4.11), Figs. 18–19.

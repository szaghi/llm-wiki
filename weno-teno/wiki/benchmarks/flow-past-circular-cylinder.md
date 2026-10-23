---
type: Benchmark
title: "Flow past a circular cylinder"
description: "Cylinder flows in four regimes: supersonic and hypersonic inviscid flow with a detached bow shock (steady shock capturing, limiters, immersed walls); hypersonic viscous flow over isothermal or catalytic walls in perfect or reacting gas, including a type IV shock–shock interaction (wall heat flux); subsonic inviscid flow testing wall treatments; viscous flow at Re 40 and 100."
status: established
aliases: [cylinder flow, supersonic cylinder, bow shock over a cylinder, cylinder wake at Re 40, flow over a cylinder]
tags: [benchmark, limiting, immersed-boundary, flux-reconstruction]
timestamp: 2026-10-23T15:17:00Z
---

# Flow past a circular cylinder

A uniform stream past a circular cylinder of diameter $D$ is run in
four regimes that test different things. **Supersonic inviscid flow** forms a
detached bow shock ahead of the cylinder and a steady flow behind it; the
test asks whether a shock-capturing scheme converges to a steady state
(residual to round-off) without oscillations behind the shock; in both
supersonic sources some nonlinear weights and limiters stall that
convergence. **Subsonic inviscid flow** has an exact steady solution
that is fore–aft symmetric with zero drag, so any drag, asymmetry or
entropy produced at the wall measures the error of the wall boundary
condition. **Hypersonic viscous flow** over a cold isothermal wall
adds a boundary layer behind the bow shock and is judged by the wall
pressure and heat flux. **Viscous subsonic flow**
at Reynolds numbers 40 (a steady closed wake) and 100 (periodic vortex
shedding) validates the wall treatment of a viscous solver against
literature values of wake length, separation angle, drag coefficient and
Strouhal number.

## Supersonic and hypersonic inviscid flow

**Mach 3 on a curvilinear grid.** [Wan & Xia (2022)](/sources/wan-2022.md)
Ex. 4.6, after Jiang & Shu, map $(\xi,\eta)\in[0,1]^2$ to
$x=-\big(R_x-(R_x-0.5)\xi\big)\cos\big(\theta(2\eta-1)\big)$,
$y=\big(R_y-(R_y-0.5)\xi\big)\sin\big(\theta(2\eta-1)\big)$ with
$R_x=3$, $R_y=6$, $\theta=\pi/2$; inflow $(\rho,v_1,v_2,p)=(1,\,3\sqrt{1.4},\,0,\,1)$,
inflow boundary at $\xi=0$, reflective wall at $\xi=1$, outflow at
$\eta=0,1$. The wall $\xi=1$ is the half circle of radius 0.5, so $D=1$,
and the inflow speed $3\sqrt{1.4}$ is Mach 3 for $\rho=p=1$, $\gamma=1.4$
*(compiler check, not in the sources)*. On $60\times80$ cells their
[hybrid WENO](/methods/hybrid-weno.md) scheme (WENO-H), CWENOZ and
multi-resolution WENO all reach residues of about $10^{-14}$; on
$120\times160$ only WENO-H reaches round-off, and its shock is sharper.

**Mach 5 and Mach 10 on triangles.** [Chen et al. (2022)](/sources/chen-2022.md)
§6.4 run inviscid flow at angle of attack 0 over a cylinder of diameter 1
on 12,070 and 47,976 triangles (Mach 10 on the coarse grid only), with
van Leer flux-vector splitting and implicit LU-SGS time stepping up to
CFL 100, to compare second-order
[gradient reconstructions](/methods/unstructured-gradient-reconstruction.md)
with slope limiting (MLP-pw with Venkatakrishnan's limiter) against their
vertex-based reconstruction with nonlinear weights (NW):

- Mach 5: NW converges in fewer steps and less CPU time than
  node-averaging Green–Gauss and vertex-stencil least squares; the
  face-stencil least squares does not converge on the coarse grid and
  diverges on the fine one; on the fine grid only NW converges fully
  (Fig. 15). Every method except NW shows a post-shock pressure
  overshoot along the stagnation line (Figs. 16–17).
- Mach 10: only NW converges fully; the others diverge or stall
  (Fig. 19).
- One reconstruction step on the coarse Mach-5 grid costs 6.77 ms
  (node-averaging), 23.49 ms (face least squares), 40.36 ms (vertex least
  squares), 17.92 ms (their vertex-based method with MLP-pw) and 14.84 ms
  (with NW); no hardware is stated (Table 2).

**Mach 3 and Mach 20 with an immersed cylinder.** [Bezgin et al. (2023)](/sources/bezgin-2023.md)
§5.2.2 (arXiv v1) validate the inviscid fluid–solid interface fluxes of
the level-set [immersed boundary](/methods/immersed-boundary-method.md)
in [JAX-Fluids](/software/jax-fluids.md): a cylinder of diameter 0.2
centred on the east boundary of $[-0.3,0]\times[-0.4,0.4]$,
$480\times1280$ cells, Dirichlet inflow on the west and zero gradient on
the other sides, initial and inflow state
$(\rho,v_1,v_2,p)=(1,\sqrt{1.4}\,M,0,1)$ with $M=3$ and $20$, HLLC, run
to steady state. The steady bow shocks "compare well" with the
literature (Fig. 14); no quantity is measured. They call the inflow the
post-shock state; $(1,\sqrt{1.4}\,M,0,1)$ is the undisturbed free stream
at Mach $M$ *(compiler check, not in the sources)*.

**Mach 8 and Mach 20 on triangles with a compact scheme.**
[Zhao, Ji, Shyy & Xu (2023)](/sources/zhao-2023.md) §4.7 (arXiv v1)
run inviscid flow at Mach 8 and Mach 20 with an adiabatic reflective
wall on a refined regular triangular mesh, with their fourth-order
compact [gas-kinetic scheme](/methods/gas-kinetic-scheme.md) at CFL 0.8,
the same nonlinear reconstruction as in all their tests and no
troubled-cell detection. The Mach 20 case starts from $t=0$ "without
additional treatment in the initial phase"; agreement with their
non-compact high-order gas-kinetic scheme on structured meshes is
asserted, with no comparison figure (Figs. 10–11).

**Mach 7 on shock-adapted high-order meshes.** [Nguyen et al. (2024)](/sources/nguyen-2024.md)
§4.3 (arXiv v1) run inviscid flow over a unit cylinder at
$M_\infty=7$ with a slip wall and supersonic inflow and outflow, on 900
quadrilaterals of degree 4, with HDG and an
[artificial viscosity](/methods/artificial-viscosity.md) driven by a
density-gradient indicator, the mesh being moved three times by an
optimal-transport map that clusters elements at the bow shock
([adaptive moving mesh](/methods/adaptive-moving-mesh.md)). The mesh
density grows with adaptation, the artificial viscosity shrinks in
amplitude and width, the pressure and Mach profiles along $y=0$ converge
(the second and third adaptive meshes being close), and the final mesh
shows no oscillation or overshoot (Figs. 9–12). No error norm is given.

**Shallow-water analogue.** [Del Grosso et al. (2024)](/sources/delgrosso-2024.md)
§5.8 (HAL preprint) run the supercritical shallow-water flow past a
cylinder of radius 0.5 m sitting on a bottom bump, with inflow depth 1
and velocity $5\sqrt{gh}$ (Froude number 5), wall condition on the
cylinder and 81,272 triangles, to a residual below $10^{-6}$ or
$t=200$ s. Their two-point (face-based) scheme develops a
[carbuncle](/definitions/carbuncle-phenomenon.md); their multi-dimensional-aware (nodal) scheme at first and
second order does not (Fig. 17). The domain size is not printed.

Wan & Xia and Chen et al. report the same observation from different
discretizations: in their runs the switch of a nonlinear scheme or
limiter stalled steady-state convergence, and their smoother switch
(Wan & Xia's three-region hybrid detector, Chen et al.'s nonlinear
weighting in place of a limiter) converged. Neither source discusses the
[carbuncle phenomenon](/definitions/carbuncle-phenomenon.md) of
blunt-body flows on this test.

## Hypersonic viscous flow

Two sources print the same free stream and wall: $T_\infty=124.94$ K,
isothermal wall at $T_{\mathrm w}=294.44$ K, $\mathrm{Re}=1.835\times10^5$.

- [Liu et al. (2023b)](/sources/liu-2023-b.md) §5.7 run it at
  $M=8.03$, with $\mathrm{Re}$ based on the cylinder radius, on
  $60\times160$ quadrilaterals with first-cell spacing 1/2000, with
  their implicit [RBF differential-quadrature](/methods/rbf-differential-quadrature.md)
  finite-volume method (Roe flux, a discrete gas-kinetic viscous flux),
  initialized by a first-order run at CFL 1000 and continued at CFL 1.0.
  The strong shock is captured "without the carbuncle phenomenon" (see
  [carbuncle phenomenon](/definitions/carbuncle-phenomenon.md)); wall
  pressure and heat flux agree with Wieting's experiment and a
  gas-kinetic BGK computation that they cite, and the heat flux is
  better than with their second-order scheme (Figs. 17–18).
- Zhao, Ji, Shyy & Xu (2023) §4.7 print $M=5$ with the same
  $T_\infty$, $T_{\mathrm w}$ and $\mathrm{Re}$, an outflow boundary on
  the right and high-aspect-ratio triangles, and run their fourth-order
  compact gas-kinetic scheme at CFL 0.35 (Fig. 12); the Reynolds-number
  length is not stated.

[Nguyen et al. (2024)](/sources/nguyen-2024.md) §4.5 run the
Gnoffo–White case: $M_\infty=17.6$, $\mathrm{Re}=376{,}000$,
$T_\infty=200$ K, isothermal wall at $500$ K, Sutherland viscosity,
supersonic inflow and outflow, on 1500 quadrilaterals of degree 4 with
one optimal-transport adaptation. The adapted mesh has smaller elements
at the wall and at the shock; the pressure coefficient barely changes
between the meshes, but the wall heat-transfer coefficient is lower on
the initial mesh, and on the adapted mesh it "agrees very well" with the
LAURA results of Gnoffo & White (Figs. 17–22).

**Type IV shock–shock interaction.** [Deng, Jiang & Yan (2025)](/sources/deng-2025.md)
§4.7 send an oblique shock onto the bow shock of a cylinder of
diameter 0.0762 m with an isothermal no-slip wall at $T_{\mathrm w}=294.44$ K,
after the experiment of Wieting & Holden: the outer boundary is split at
$(-0.1536,-0.0339)$ m into an upper inlet with $\rho_\infty=0.023$
kg m$^{-3}$, $v=(1.692\times10^3,0)$ m/s, $T_\infty=110.56$ K, and a lower,
post-shock inlet with $\rho=0.077$ kg m$^{-3}$, $v=(1.58\times10^3,\ 0.35\times10^3)$
(units of the second component not printed), $T=234.67$ K, obtained
from the Rankine–Hugoniot relations to match the experiment. With
$R=287$ J/(kg K) and $\gamma=1.4$, which the paper does not print, the
upper stream is Mach 8.03, the free-stream Mach number of Liu et al. (2023b)'s
run above, and the lower one Mach 5.27 turned by $12.5^\circ$
*(compiler check, not in the sources)*. They run fourth-order DG with
Godunov-type finite-volume subcells reconstructed by the non-uniform
[ROUND](/methods/round-scheme.md) scheme on $43\times94$ curvilinear
elements (circumferential × radial) with a cubic boundary, BR2 viscous
fluxes in the DG cells. The time-averaged wall pressure agrees well with
the experiment; the heat flux follows the measured trend but its peak is
under-predicted, and glitches after the peak are tentatively linked to
"shock anomalies"; the maximum wall pressure and heat flux are tracked
in time, normalized by the undisturbed stagnation values (Figs. 20–23).
The authors note that their finite-volume metrics, taken from the DG
transformation, "may lead to the violation of the free-stream
preservation or the geometric conservation law", which they do not fix
(§4.7); see [free-stream preservation](/properties/free-stream-preservation.md)
and [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md).

**Reacting air and immersed walls.** [Başkaya et al. (2024)](/sources/baskaya-2024.md)
§4.5 (author preprint) run the HEG cylinder of Knight et al. (2012),
radius 0.045 m, total enthalpy 22.4 MJ/kg, $M_\infty=8.98$,
$v_\infty=5956$ m/s, $T_\infty=901$ K, $p_\infty=476$ Pa,
$\rho_\infty=1.547\times10^{-3}$ kg m$^{-3}$, in five-species air
(mass fractions of N$_2$, O$_2$, NO, N, O $=0.7543$, $0.00713$,
$0.01026$, $6.5\times10^{-7}$, $0.2283$) with the Park mechanism, for
three walls: inert adiabatic, inert isothermal at $T_{\mathrm w}=300$ K
and fully catalytic isothermal at 300 K. A body-fitted solver (US3D,
modified Steger–Warming flux, MUSCL) is the reference for two
[immersed-boundary](/methods/immersed-boundary-method.md) treatments on
adaptive Cartesian grids: a strictly conservative cut-cell method in
INCA (third-order WENO with HLLC, RK3) and ghost-cell methods in CHESS
and in INCA with the cut-cell fluxes switched off, all with the same
thermochemistry library.

- Adiabatic wall: shock stand-off and dissociation agree for all
  methods (Fig. 7).
- Isothermal wall: body-fitted and cut-cell results match "almost
  exactly", the CHESS ghost-cell result shows a larger stand-off
  distance (Fig. 8). The stagnation heat flux goes from 8.422 to
  7.308 MW/m$^2$ body-fitted (wall spacings 0.44 to 0.05 μm) and from
  6.684 to 7.189 MW/m$^2$ with cut cells (2.5 to 0.3125 μm); the authors
  take the medium-fine values, 7.345 and 7.144 MW/m$^2$, as converged,
  against $7.402\pm0.220$ MW/m$^2$ measured and 5.971 MW/m$^2$ for an
  earlier simulation in Knight et al.; the CHESS ghost-cell method gives
  0.167 MW/m$^2$ (Table 7). The wall pressure is accurate for all
  methods (Fig. 9).
- Fully catalytic wall: body-fitted and cut-cell results agree, and
  catalysis raises the heat flux only within the experimental
  uncertainty (Fig. 11); taking the body-fitted run as reference, the
  cut-cell stagnation heat flux is 2.7% lower on the inert and 0.2% lower
  on the catalytic wall.
- INCA's ghost-cell variant, which differs from its cut-cell version
  only in the conservative flux treatment, also misses the cold-wall
  heat flux, so the authors attribute the failure to the conservation
  errors of ghost-cell methods, which act as an unphysical surface
  blowing and matter where wall gradients of the conserved variables are
  large (§5, Fig. 18).

## Subsonic inviscid flow

| Source | Method | $M$ | Domain and grid | Measures |
|---|---|---|---|---|
| [Funada & Imamura (2023)](/sources/funada-2023.md) §3.3 | [flux reconstruction](/methods/flux-reconstruction.md) of order $k$ on hierarchical Cartesian grids with sharp-interface [immersed boundary](/methods/immersed-boundary-method.md) conditions (LO, HO-i/f, HO-i/c, HO-e), SLAU flux, implicit MFGS | 0.3 | $200\times200$ square, $D=1$; $\Delta x_{\min}=0.0977,0.0488,0.0244$; Riemann far field | $L_2$ entropy error, surface $C_p$, drag |
| [Wei et al. (2023)](/sources/wei-2023.md) §7.2 | second-order cell-centred finite volume with weighted least-squares gradients and five boundary treatments, including their ghost-cell constraint (WLSQ-GCC); LU-SGS, CFL 20 | 0.38 | radius 0.5, far field at 20 radii, $160\times40$ quadrilateral O-grid, 3000 steps | Mach and entropy contours, $C_p$, windward–leeward pressure difference, cost |

**Order of immersed walls.** Funada & Imamura's four constructions
differ in how the wall state at a flux point is built. With the
$L_2$ entropy error plotted against $\sqrt{N_{\mathrm{DoF}}}$ the slopes are
"much steeper" than the design order; the authors attribute this to the
error concentrating near the wall on these hierarchical grids and
re-plot against $1/\Delta x_{\min}$, on which HO-i/c (wall curvature
imposed) and HO-e (tangential velocity extrapolated) are of order $k$
and LO and HO-i/f are not (Figs. 17–19). At $k=3$, $\Delta x_{\min}=0.0244$
the drag coefficients are $5.0\times10^{-2}$ (LO), $1.2\times10^{-2}$
(HO-i/f), $9.1\times10^{-5}$ (HO-i/c) and $4.5\times10^{-4}$ (HO-e); the
stagnation $C_p$ of HO-i/c and HO-e is closer to the theoretical 1.023,
and the LO and HO-i/f velocity fields are fore–aft asymmetric (Table 2,
Figs. 20–21). They run the same comparison on a sphere at $M=0.2$
(drags $1.5\times10^{-2}$, $1.4\times10^{-2}$, $7.0\times10^{-4}$,
$9.0\times10^{-4}$; theoretical stagnation $C_p=1.010$) and on a channel
bump (§3.2, §3.4, Tables 1, 3).

**Linear exactness of boundary gradients.** Wei et al. find that only
WLSQ-GCC and the curvature-corrected ghost-cell treatment give
symmetric Mach contours downstream, the others zigzag lines, and the
ghost-cell treatment a "non-physical protrusion" on the leeward side
(Figs. 17–18). WLSQ-GCC produces the least spurious entropy around the
cylinder, which the authors read as "lower overall numerical
dissipation" (Fig. 19), and the best symmetry of the windward–leeward
pressure difference, at most 0.0041 of $p_\infty$ (Eq. 42, Fig. 22). Its
total time is 1.044 times that of the vertex-stencil least squares,
with at most two secant iterations per boundary cell (Table 5); the
weighting variant with $n=4$ crashed on this case because of
ill-conditioning (§7.2). See
[unstructured gradient reconstruction](/methods/unstructured-gradient-reconstruction.md).

## Viscous flow at low Reynolds number

| Source | Method | $M$ | $L_w/D$ | separation angle | $C_d$ |
|---|---|---|---|---|---|
| [Kou et al. (2022)](/sources/kou-2022.md) §5.2, Table 1, meshes 1/2/3 | flux reconstruction with volume-penalization immersed boundary | 0.2 | 2.30 / 2.30 / 2.27 | 51.2° / 52.0° / 52.0° | 1.50 / 1.51 / 1.52 |
| Kou et al., body-fitted FR | flux reconstruction | 0.2 | 2.24 | 51.0° | 1.53 |
| [Chen et al. (2022)](/sources/chen-2022.md) §6.7, Table 3 | vertex-based finite volume, without / with face-gradient correction | 0.3 | 2.14 / 2.095 | — | 1.588 / 1.591 |

Both sources run $\mathrm{Re}=40$ based on the diameter. Kou et al. place
the cylinder in $[-30D,50D]\times[-30D,30D]$ with uniform elements in
$[-D,D]^2$ of size $0.03D$ ($P=3$, 532,576 DOFs), $0.015D$ ($P=2$,
915,525) and $0.01D$ ($P=2$, 1,476,000), penalization parameter equal to
the time step, no-slip adiabatic wall and characteristic far field. They
compare with Dennis & Chang (2.35, 53.8°, 1.52), Fornberg (2.24, 55.6°,
1.50) and Choi et al. (2.21, 53.6°, 1.49) as printed in their Table 1,
and quote a literature range of 1.48 to 1.59 for the incompressible drag
(App. D). Their pressure coefficient agrees with the body-fitted run,
the wall vorticity less well, since only the surface velocity is
penalized. Local $p$-refinement (P1 far field, P2 buffer, P3 within
$0.25D$ of the wall) gives results very close to uniform P3 with 148,296
DOFs, 0.278 of 532,576 (see [hp-adaptation](/methods/hp-adaptation.md)).
See [immersed-boundary methods](/methods/immersed-boundary-method.md) and
[flux reconstruction](/methods/flux-reconstruction.md).

Chen et al. use 20,000 triangles with first layer $0.001$ of the
reference length, HLLC flux and LU-SGS at CFL $10^3$. Only their
vertex-based least-squares variants converge fully; the face-gradient
correction shortens the wake, which they read as extra numerical
dissipation. They compare with a wake length of 2.13 and a drag of 1.48,
both labelled "Experiment" in Table 3, and call 1.588 "close to the
experimental result".

**Compressible wakes.** Kou et al. App. D run the compressible
cylinder benchmark of Canuto & Taira at $M=0.1$ to $0.5$, $\mathrm{Re}=40$
(steady, $h=0.015D$) and $\mathrm{Re}=100$ (unsteady, $h=0.02D$, wake
refined), with $P=2$ in $[-20D,40D]\times[-20D,20D]$: mean drag, wake
geometry, maximal lift and Strouhal number agree with that reference and
the trend with Mach number is captured (Fig. D.25).

## Qualifications

- The two viscous sources run at different Mach numbers (0.2 and 0.3),
  so their wake lengths need not agree; their reference values for
  $L_w/D$ already spread from 2.13 to 2.35. Both computed drag values,
  1.50–1.53 and 1.588–1.591, lie inside the 1.48–1.59 range Kou et al.
  quote *(compiler check, not in the sources)*.
- Chen et al.'s drag reference 1.48 is cited to Visbal, a work whose
  printed title names a Navier–Stokes solver, so the label "Experiment"
  in their Table 3 is doubtful; 1.588 differs from 1.48 by 7.3 %
  *(compiler check, not in the sources)*.
- In Chen et al.'s Table 3 the variants with and without nonlinear
  weighting give identical wake lengths and drag, so the viscous test
  does not exercise the nonlinear weights.
- The supersonic runs are evaluated by residual histories and contour
  plots; no source compares the shock stand-off distance with a
  reference value.
- The two subsonic inviscid sources use different error measures
  (entropy error and drag against the exact zero, contour symmetry) and
  Mach numbers (0.3, 0.38). The theoretical stagnation $C_p$ values of
  Funada & Imamura follow from the isentropic relation with
  $\gamma=1.4$, which they do not print *(compiler check, not in the
  sources)*.
- Funada & Imamura's sphere diameter is not stated in §3.4.
- Başkaya et al. expect the ghost-cell conservation errors to converge
  at the truncation rate of the base scheme, but show no convergence
  study of them, and their grid study covers the body-fitted and
  cut-cell runs only; the ghost-cell result is for one wall spacing,
  1.0 μm (Table 7).
- Nguyen et al. print neither $\gamma$ nor $\mathrm{Pr}$ for their
  cylinder runs; their mesh moves at fixed connectivity, so the element
  counts above hold for every adapted mesh, and their claims are visual
  or against LAURA.
- Liu et al. (2023b) and Zhao et al. print identical free-stream
  temperature, wall temperature and Reynolds number at different Mach
  numbers (8.03 and 5); neither paper compares with the other, and
  Zhao et al. show no comparison with experiment for their run.

# Citations

- [Wan & Xia (2022)](/sources/wan-2022.md) — Ex. 4.6.
- [Chen et al. (2022)](/sources/chen-2022.md) — §6.4, §6.7, Tables 2–3, Figs. 15–19, 27–28.
- [Kou et al. (2022)](/sources/kou-2022.md) — §5.2, Table 1, Fig. 14, App. D, Fig. D.25.
- [Bezgin et al. (2023)](/sources/bezgin-2023.md) — §5.2.2, Fig. 14 (arXiv v1).
- [Funada & Imamura (2023)](/sources/funada-2023.md) — §3.2–3.4, Tables 1–3, Figs. 17–25.
- [Wei et al. (2023)](/sources/wei-2023.md) — §7.2, Eq. 42, Table 5, Figs. 17–22.
- [Liu et al. (2023b)](/sources/liu-2023-b.md) — §5.7, Figs. 17–18.
- [Zhao, Ji, Shyy & Xu (2023)](/sources/zhao-2023.md) — §4.7, Figs. 10–12 (arXiv v1).
- [Başkaya et al. (2024)](/sources/baskaya-2024.md) — §4.5, Tables 6–7, Figs. 7–11; §5, Fig. 18 (author preprint).
- [Nguyen et al. (2024)](/sources/nguyen-2024.md) — §2.2, §3, §4.3, §4.5, Figs. 9–12, 17–22 (arXiv v1).
- [Del Grosso et al. (2024)](/sources/delgrosso-2024.md) — §5.8, Fig. 17 (HAL preprint).
- [Deng, Jiang & Yan (2025)](/sources/deng-2025.md) — §4.7, Figs. 20–23.

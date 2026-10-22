---
type: Benchmark
title: "Flow past a circular cylinder"
description: "Cylinder flows in two regimes: supersonic and hypersonic inviscid flow with a steady detached bow shock, used to test convergence of steady-state shock capturing and limiters, and viscous subsonic flow at Re 40 and 100, validated through wake length, separation angle and drag coefficient."
status: established
aliases: [cylinder flow, supersonic cylinder, bow shock over a cylinder, cylinder wake at Re 40, flow over a cylinder]
tags: [benchmark, limiting, immersed-boundary, flux-reconstruction]
timestamp: 2026-10-23T10:00:00Z
---

# Flow past a circular cylinder

A uniform stream past a circular cylinder of diameter $D$ is run in two
regimes that test different things. **Supersonic inviscid flow** forms a
detached bow shock ahead of the cylinder and a steady flow behind it; the
test asks whether a shock-capturing scheme converges to a steady state
(residual to round-off) without oscillations behind the shock; in both
supersonic sources some nonlinear weights and limiters stall that
convergence. **Viscous subsonic flow**
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

Both sources report the same observation from different
discretizations: in their runs the switch of a nonlinear scheme or
limiter stalled steady-state convergence, and their smoother switch
(Wan & Xia's three-region hybrid detector, Chen et al.'s nonlinear
weighting in place of a limiter) converged. Neither source discusses the
[carbuncle phenomenon](/definitions/carbuncle-phenomenon.md) of
blunt-body flows on this test.

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

# Citations

- [Wan & Xia (2022)](/sources/wan-2022.md) — Ex. 4.6.
- [Chen et al. (2022)](/sources/chen-2022.md) — §6.4, §6.7, Tables 2–3, Figs. 15–19, 27–28.
- [Kou et al. (2022)](/sources/kou-2022.md) — §5.2, Table 1, Fig. 14, App. D, Fig. D.25.

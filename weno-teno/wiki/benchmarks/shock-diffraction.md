---
type: Benchmark
title: "Shock diffraction"
description: "Two-dimensional Euler benchmark of a Mach 5.09 shock diffracting around a backward-facing corner into gas at rest, with a relativistic counterpart; the expansion behind the corner drives density and pressure towards zero, so the sources use it as a robustness test of positivity-preserving and limited high-order schemes."
status: established
aliases: [shock diffraction problem, shock diffraction at a corner, shock diffraction around a backward-facing step, Mach 5.09 shock diffraction]
tags: [benchmark, positivity, bound-preserving, dg, relativistic]
timestamp: 2026-10-22T18:00:00Z
---

# Shock diffraction

A planar shock of Mach number $5.09$ runs to the right along a channel
of height 5 and leaves it at a backward-facing corner, where the
channel opens downwards into a much larger box. The shock diffracts
around the corner, and the gas expanding behind it reaches very low
density and pressure next to the vertical wall below the corner. The
problem has no exact solution; the sources read it as a robustness
test: a scheme must keep density and pressure positive in the
expansion and stay free of oscillations at the strong shock, and the
contours of density and pressure at $t=2.3$ are compared visually.
Three sources of the bundle run it, two in the Euler form and one in a
relativistic form.

## Setup

[Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) Ex. 4.7 and
[Du, Shu & Zhong (2022)](/sources/du-2022.md) Ex. 4.4 print the same
data, with $\gamma=1.4$:

- domain $[0,1]\times[6,11]\cup[1,13]\times[0,11]$: the channel
  $0\le x\le1$, $6\le y\le11$ opens at the corner $(1,6)$ into the box
  $1\le x\le13$, $0\le y\le11$;
- a right-moving shock of Mach number $5.09$ initially at $x=0.5$,
  $6\le y\le11$, moving into air at rest with $\rho=1.4$, $p=1$;
- inflow at $x=0$, $6\le y\le11$; outflow at $x=13$ and at $y=0$,
  $1\le x\le13$; reflecting walls on $0\le x\le1$, $y=6$ and on $x=1$,
  $0\le y\le6$;
- final time $t=2.3$; 20 density contours from 0.066227 to 7.0668 and
  40 pressure contours from 0.091 to 37 (Du et al. on triangles, Fan et
  al.).

The top boundary differs: Fan et al. state outflow on $y=11$,
$0\le x\le13$; Du et al. impose the exact motion of the shock there.

The pre-shock state has sound speed $c=\sqrt{1.4\cdot1/1.4}=1$, so the
shock moves at speed $5.09$, and the Rankine–Hugoniot conditions give
the post-shock state
$\rho=1.4\cdot\frac{(\gamma+1)M^2}{(\gamma-1)M^2+2}=7.041$,
$v_1=\frac{2c}{\gamma+1}\big(M-\frac1M\big)=4.078$,
$p=1+\frac{2\gamma}{\gamma+1}(M^2-1)=30.06$ with $M=5.09$ *(compiler
check, not in the sources)*. Neither source prints this state.

### Relativistic version

[Chen & Wu (2022)](/sources/chen-2022-b.md) Ex. 4.11 (arXiv v1) run a
[relativistic](/definitions/relativistic-hydrodynamics.md) shock
diffraction at a corner: a shock with speed $0.8$ along $x=3.4$,
$6\le y\le11$, pre-shock $\rho=1.4$, $p=1$ at rest, post-shock
$(\rho,v_1,v_2,p)=(2.58962919872684,\ 0.40445979062926,\ 0,\ 2.865544850466692)$;
reflecting walls on the corner, inflow on $x=0$, $6\le y\le11$, outflow
elsewhere, $t=8$. The paper states no $\gamma$ for the example, whose
default is $5/3$: with $\gamma=5/3$ the printed post-shock state
satisfies the relativistic Rankine–Hugoniot conditions of a shock of
speed 0.8 against the pre-shock state to round-off, while with
$\gamma=1.4$ the momentum and energy jumps fail by about 0.55
*(compiler check, not in the sources)*.

## Runs in the sources

| Source | Scheme | Mesh | Notes |
|---|---|---|---|
| [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) Ex. 4.7 | positivity-preserving hybrid [HWENO](/methods/hermite-weno.md), finite volume, cubic reconstruction, SSP-RK3; Euler and Navier–Stokes ($\mathrm{Re}=1000$, $\mathrm{Pr}=0.72$) | $\Delta x=\Delta y=1/32$ | time step with $a=1/12$, $b=0.001$ as in their whole paper |
| [Du, Shu & Zhong (2022)](/sources/du-2022.md) Ex. 4.4 | RKDG $P^1$, $P^2$ with the improved vs the original [simple WENO limiter](/methods/weno-limiter-dg.md), KXRCF threshold $C_k=0.01$, SSP-RK3 | triangles, $h=1/16$ | CFL 0.3 ($P^1$), 0.18 ($P^2$) |
| [Du, Shu & Zhong (2022)](/sources/du-2022.md) Ex. 4.10 | as above, DG on polygonal cells from random point clouds | 219,200 ($P^1$) and 493,200 ($P^2$) points | positivity-preserving limiter for $P^2$; 20 density contours 0.066227–7.1 |
| [Chen & Wu (2022)](/sources/chen-2022-b.md) Ex. 4.11 | third-order finite-volume WENO on triangles with a physical-constraint-preserving limiter and HLL flux, vs first-order HLL | $h=1/40$; first order also $h=1/160$ | relativistic; CFL 0.5 |

## Findings across sources

**Positivity behind the corner.** Fan et al. use the problem to show
robustness in the low-density, low-pressure region behind the corner.
Their scaling positivity limiter is triggered in only 0.23 % of the
cells, identically for the hybrid and non-hybrid schemes and for both
Reynolds numbers, and they state that the earlier hybrid HWENO of Zhao,
Chen & Qiu blows up on this problem from loss of positivity, without a
figure (§1, §4, Fig. 4.7, Table 4.2). Du et al. switch on a
positivity-preserving limiter for their $P^2$ runs on point clouds; on
triangles no positivity limiter is mentioned. See
[bound preservation](/properties/bound-preservation.md) and the
[Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md).

**Limiters and troubled cells.** On triangles Du et al.'s improved
limiter, which combines only two polynomials per edge direction, gives
results "almost identical" to the original limiter; it saves 6.6 %
($P^1$) and 11.73 % ($P^2$) of the CPU time although it flags more
cells at $P^2$ (12.63 % against 9.48 %; Figs. 4.6–4.7, Table 4.8). On
point clouds both limiters give the same quality, more oscillatory than
on triangles, with savings of 9.90 % and 40.91 % (Fig. 4.16,
Table 4.18). Fan et al.'s hybrid scheme applies its nonlinear HWENO
reconstruction in 5.07 % (Euler) and 4.39 % (Navier–Stokes) of the
cells, and saves 63.76 % ($\mathrm{Re}=\infty$) and 64.45 %
($\mathrm{Re}=1000$) of the CPU time of the non-hybrid
positivity-preserving scheme, hardware not stated (Table 4.2). See
[troubled-cell indicators](/definitions/troubled-cell-indicator.md).

**Third against first order in the relativistic case.** Chen & Wu
compare their third-order scheme at $h=1/40$ with the first-order HLL
scheme at $h=1/40$ and $h=1/160$ (Fig. 17); the figure is the evidence,
and no error norm is given.

## Qualifications

- Evidence is visual throughout; no source reports a reference
  solution or an error norm.
- Fan et al. and Du et al. differ in the top boundary condition
  (outflow against the exact shock motion) and in the discretization
  family (finite volume on a Cartesian grid against DG on triangles and
  polygons), so their contour plots are not directly comparable.
- Chen & Wu do not describe the corner geometry beyond "wedge walls",
  and give no $\gamma$ for the example (see the relativistic setup).

# Citations

- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — §1; §4, Ex. 4.7, Fig. 4.7, Table 4.2.
- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — §4.2; Ex. 4.4, Figs. 4.5–4.7, Table 4.8; Ex. 4.10, Fig. 4.16, Table 4.18.
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — Ex. 4.11, Fig. 17 (arXiv v1).

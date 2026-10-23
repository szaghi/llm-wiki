---
type: Benchmark
title: "MHD shock–cloud interaction"
description: "Ideal and relativistic MHD robustness test in which a strong planar fast shock with a rotational discontinuity overruns a dense cloud ten to thirty times the ambient density, in two and three dimensions; used for positivity-preserving DG, order-reduced fourth-order finite volumes, entropy-stable moving meshes and bound-preserving central DG."
status: established
aliases: [shock–cloud interaction, cloud–shock interaction, Dai–Woodward shock–cloud problem, magnetized cloud–shock interaction]
tags: [benchmark, mhd, relativistic, positivity]
timestamp: 2026-10-23T15:15:00Z
---

# MHD shock–cloud interaction

A planar MHD discontinuity, which launches a strong fast shock and a
rotational wave, runs into a dense cloud at rest in pressure equilibrium
with its surroundings. The shocked cloud is crushed into a
mushroom-like structure with strong density, pressure and field
gradients and small-scale features on its trailing side. The test
stresses positivity of pressure, divergence control and the robustness
of high-order limiting in ideal and relativistic MHD
([Berta et al. (2024)](/sources/berta-2024.md) §5.8, citing Balsara,
Ziegler, Miniati & Martin and Helzel et al. for the MHD version and
Mignone for the relativistic one;
[Dzanic & Witherden (2023)](/sources/dzanic-2023.md) §5.4, citing Dai &
Woodward and the setup of Balbás & Tadmor). It is the magnetized relative of the
hydrodynamic [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md),
with which it is not merged: the cloud is denser than the ambient gas
and the shock is magnetized.

## Setup as printed

States are $(\rho,v_1,v_2,v_3,B_1,B_2,B_3,p)$ in units without $4\pi$.

**Classical MHD.**

| Source | Domain, boundaries | Shocked (left) state | Pre-shock (right) state | Cloud | $\gamma$, $t$ |
|---|---|---|---|---|---|
| [Berta et al. (2024)](/sources/berta-2024.md) §5.8, Eq. (56) | unit cube; inflow at $x=0$, zero gradient elsewhere; jump at $x=0.6$ | $(3.86859,0,0,0,0,2.1826182,-2.1826182,167.345)$ | $(1,-11.2536,0,0,0,0.56418958,0.56418958,1)$ | sphere $\rho=10$, radius 0.15, centre $(0.8,0.5,0.5)$, in equilibrium with the ambient | 5/3, 0.06 |
| [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) §5.4, Eqs. (44)–(45) | $[0,1]\times[-0.5,1.5]$ (instead of $[0,1]^2$), periodic top and bottom, left Neumann, right Dirichlet; jump at $x=0.6$ | $(3.86859,0,0,0,2.1826182,-2.1826182,1,167.345)$ | $(1,-11.2536,0,0,0,0.56418958,0.56418958,1)$ | disc radius 0.15, centre $(0.8,0.5)$, state $(10,0,0,0,2.1826182,-2.1826182,1,167.345)$ | 5/3, 0.06 |

Dzanic & Witherden extend the domain so that the top and bottom
boundaries lie outside the domain of influence over the run, and solve
on a one-element-deep hexahedral mesh to carry $B_3$.

**Relativistic MHD.**

| Source | Domain, boundaries | Left state | Right state | Cloud | $\gamma$, $t$ |
|---|---|---|---|---|---|
| Berta et al. (2024) §5.8, Eq. (57) | unit cube, as above; jump at $x=0.6$ | $(39.5052,0,0,0,0,0,1.9753,129.72386)$ | $(1,-\sqrt{0.99},0,0,0,0,0.5,10^{-3})$ | sphere $\rho=10$, radius 0.15, centre $(0.8,0.5,0.5)$ | 4/3, 0.6 |
| [Duan & Tang (2022)](/sources/duan-2022.md) Exs. 6.6, 6.10 (from He & Tang) | $[-0.2,1.2]\times[0,1]$ (and $\times[0,1]$ in 3D); inflow left, outflow elsewhere; shock at $x=0.05$ moving right | printed under the header $(\rho,v,p,B)$: $(3.86859,0.68,0,0,1.25115,0,0.84981,-0.84981)$ | same header: $(1,0,0,0,0,0.16106,0.16106,0.05)$ | disc (sphere in 3D) $\rho=30$, radius 0.15, centre $(0.25,0.5)$ ($(0.25,0.5,0.5)$) | 5/3 (the paper's default), 1.2 |
| [Ding & Wu (2024b)](/sources/ding-2024-b.md) Ex. 5.7 (setup of He & Tang and of Wu & Tang, as cited) | $[-0.2,1.2]\times[0,1]$, $560\times400$; inflow left, outflow elsewhere; shock at $x=0.05$ moving right | $(3.86859,0.68,0,0,0,0.8498108108786,-0.8498108108786,1.251148954517)$ | $(1,0,0,0,0,0.1610642582333,0.1610642582333,0.05)$ | disc $\rho=30$, radius 0.15, centre $(0.25,0.5)$ | ideal, $\gamma=5/3$, 1.2 |

Berta et al.'s 3D MHD states are the 2D states of the literature with
the cloud made spherical. In both of their setups the pre-shock medium
streams in the $-x$ direction onto the shocked region, in the
relativistic one at $v_1=-\sqrt{0.99}$, a Lorentz factor of 10
*(compiler check, not in the sources)*.

Ding & Wu (2024b) print their states in the order $(\rho,v,B,p)$. Their left
state is Duan & Tang's read under Duan & Tang's printed header
$(\rho,v,p,B)$, and their right state is Duan & Tang's read in the order
$(\rho,v,B,p)$, to more digits *(compiler check, not in the sources)*;
this is the reading recorded under Qualifications.

## Runs and findings

**Positivity-preserving entropy filtering in DG.** Dzanic & Witherden
run nodal DG / flux reconstruction at $\mathbb P_2$ on $400^2$ elements
(with respect to $[0,1]^2$), $\Delta t=4\times10^{-6}$, with their
[entropy filter](/methods/entropy-filtering.md): the strong
discontinuities are resolved without observable spurious oscillations,
small-scale features of the cloud are not excessively dissipated, the
symmetry is kept, and the divergence error and the limiting concentrate
at discontinuities (Figs. 7–8). Against Wu & Shu's third-order
positivity-preserving DG with a [WENO limiter](/methods/weno-limiter-dg.md)
on the same mesh the filter is "roughly equally performative" in
resolving discontinuities and "marginally better" on the small-scale
features on the trailing side of the cloud (Fig. 9). Without the
positivity-preserving filter the scheme diverged with negative pressure.

**Order reduction in fourth-order finite volumes.** Berta et al. run
both setups on $256^3$ zones with their fourth-order constrained-transport
finite-volume scheme (Fig. 14). The scheme "properly recovers the
expected structures", and the order-reduction procedure, extended to
the selective flux integration (the Laplacian conversion of point
fluxes to face averages is switched off in flagged cells), "has been
fundamental for the correct evolution of the simulations"; see
[troubled-cell indicators](/definitions/troubled-cell-indicator.md).

**Entropy-stable adaptive moving meshes.** Duan & Tang's fifth-order
entropy-stable scheme on an [adaptive moving mesh](/methods/adaptive-moving-mesh.md)
(MM-O5, monitor parameter 800) concentrates the mesh points near the
cloud and is compared with the same scheme on uniform meshes (UM-O5)
through schlieren images of $\ln\rho$ and $\lvert B\rvert$:

| Run | MM-O5 | UM-O5, same grid | UM-O5, finer grid |
|---|---|---|---|
| 2D (Table 6.1, 4 cores) | $210\times150$: 4 min 16 s | 2 min 05 s | $560\times400$: 40 min 28 s |
| 3D (Table 6.2, 32 cores) | $210\times150\times150$: 3 h 9 min 57 s | 2 h 8 min 44 s | $420\times300\times300$: 34 h 46 min 49 s |

In both, MM-O5 is better than the uniform mesh of equal size and
comparable to the finer uniform one, at 10.5 % (2D) and a printed
9.06 % (3D) of its CPU time (Figs. 6.10–6.12, 6.18–6.20); from the
table the 3D ratio is $11397/125209=9.10\,\%$ *(compiler check, not in
the sources)*.

**Bound-preserving central DG.** Ding & Wu (2024b)'s $\mathbb P^2$ locally
divergence-free central DG scheme for relativistic MHD (SSP-RK3, CFL
0.25, locally divergence-free WENO limiter in troubled cells, then the
bound-preserving limiter) fails at the first time step without the
bound-preserving limiter. With it the run completes, with schlieren
images of $\log\rho$, $\log p$, $W$ and $\lvert B\rvert$ at $t=1.2$
(Fig. 9), a relative global divergence error of about $10^{-5}$ and a
relative local error of zero (Fig. 7c); see
[bound preservation](/properties/bound-preservation.md) and
[discontinuous Galerkin](/methods/discontinuous-galerkin.md).

## Qualifications

- **Dzanic & Witherden's printed states.** Their left state puts
  $2.1826182$ in $B_1$, $-2.1826182$ in $B_2$ and $1$ in $B_3$, against
  $B_1=0$ in their own right state and in Berta et al.'s left state;
  as printed, $B_1$ jumps from $2.1826182$ to $0$ across the plane
  $x=0.6$, so the initial field is not divergence-free, and the cloud
  carries the shocked pressure $167.345$ while sitting in the pre-shock
  region of pressure 1 *(compiler check, not in the sources)*. Berta et
  al.'s states, a normal field of zero on both sides and a cloud in
  pressure equilibrium with the ambient, are the self-consistent
  reading; the paper does not show which data the solver used.
- **Duan & Tang's state ordering.** Read in the order of the printed
  header $(\rho,v,p,B)$, the right state has $p=0$ and $B_1=0.16106$
  while the left state has $B_1=0$; read as $(\rho,v,B,p)$ it has
  $B=(0,0.16106,0.16106)$ and $p=0.05$, consistent with the left
  state's normal field *(compiler check, not in the sources)*. The left
  state is consistent only under the printed header. Ding & Wu (2024b)'s states,
  printed in the order $(\rho,v,B,p)$, coincide with this reading of
  both states.
- Duan & Tang's text refers to "iso-surfaces of $\rho=1.52$" where the
  caption of their Fig. 6.18 reads $\ln\rho=1.52$, and to "the bubble"
  for the cloud.
- All comparisons are visual (contours, schlieren images, a figure of
  another paper); no source reports an error norm or a conservation
  measure for this test.
- Berta et al. are read as arXiv v4, Dzanic & Witherden as arXiv v2,
  Duan & Tang as arXiv v1, Ding & Wu (2024b) as the version of record.

# Citations

- [Berta et al. (2024)](/sources/berta-2024.md) — §5.8, Eqs. (56)–(57), Fig. 14 (arXiv v4).
- [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) — §5.4, Eqs. (44)–(45), Figs. 7–9 (arXiv v2).
- [Duan & Tang (2022)](/sources/duan-2022.md) — Exs. 6.6, 6.10, Tables 6.1–6.2, Figs. 6.10–6.12, 6.18–6.20 (arXiv v1).
- [Ding & Wu (2024b)](/sources/ding-2024-b.md) — Example 5.7, Figs. 7c, 9.

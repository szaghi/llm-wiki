---
type: Benchmark
title: "Dam-break problems"
description: "Shallow-water Riemann problems with water at rest at two depths separated by a removed dam, in one dimension, between reflecting walls, over non-flat bottoms, in thermal shallow water and in the radial two-dimensional form, used to test shock and rarefaction capturing, multi-dimensional dissipation, characteristic central-upwind fluxes, spectral shock capturing, space-time shock tracking and learned entropy-stable fluxes."
status: established
aliases: [dam break, dam-break problem, shallow-water dam break, circular dam break, radial dam break, cylindrical dam break]
tags: [benchmark, shallow-water, riemann-solver, shock-tracking]
timestamp: 2026-10-24T05:33:00Z
---

# Dam-break problems

A dam-break problem is a Riemann problem of the
[shallow-water equations](/definitions/shallow-water-equations.md): water at rest stands at a
depth $h_{\mathrm L}$ on one side of a dam and at a smaller depth $h_{\mathrm R}\ge0$ on the
other, and the dam is removed at $t=0$. Over a flat bottom the solution is a bore (a shock)
running into the shallow water and a rarefaction running into the deep water, with a uniform
intermediate state between them; with $h_{\mathrm R}=0$ the shock is replaced by a wet–dry
front. Here $h$ is the depth, $b$ the bottom elevation, $H_{\mathrm s}=h+b$ the free-surface
level, $g$ the gravity and $r$ the distance from the centre of a radial dam (all page-local,
as on the shallow-water page). In the thermal (Ripa) shallow-water
equations the layer also carries a buoyancy $\mathsf b$ (page-local; the
sources' $b$), advected with the flow, and the pressure term
$\tfrac g2h^2$ becomes $\tfrac{\mathsf b}2h^2$. Three variants run in the bundle: the one-dimensional problem
on an open or a mirrored domain, the one-dimensional problem between reflecting walls, where
the waves bounce back and interact, and the radial problem, in which a cylinder of deep water
collapses into a circular bore and an inward rarefaction.

The gas–liquid "Martin–Moyce dam break", the collapse of a water column in air, is a different
problem (a two-phase interface flow, not a shallow-water Riemann problem); it is recorded on
the [five-equation model](/definitions/five-equation-model.md) and
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md) pages.

## Setups

| Source | Variant | Data as printed | Domain, boundaries | Grid, time |
|---|---|---|---|---|
| [Del Grosso et al. (2024)](/sources/delgrosso-2024.md) §5.3 | radial, flat bottom | $h=10$ m for $r<r_0=11$ m, $h=1$ m outside, $v=0$, $g=9.81$ | $[0,50]^2$ m | $100\times100$ squares and 23736 triangles; $t=0.69$ s |
| Del Grosso et al. §5.3.1 | radial, non-flat bottom | $b=\tfrac12\big(1+\cos(2\pi r/2)\big)$, $h=11-b$ inside $r_0$, $h=2-b$ outside | as above | 23736 triangles; $t=0.69$ s |
| [Kolluru et al. (2024)](/sources/kolluru-2024.md) §3.3, Eq. (8c) | 1D, flat bottom | $h=h_{\mathrm L}$ for $x<0$, $h_{\mathrm R}$ for $x>0$, $v=0$, $h_{\mathrm L}>h_{\mathrm R}\ge0$ | $[-5,5]$, mirror-symmetrized about $x=-5$ for the Fourier basis | $N_x=2665$; outputs $t=0.5,1,1.5,2$ |
| [Naudet & Zahr (2024)](/sources/naudet-2024.md) §5.2, Eq. (54) | 1D between walls, flat bottom | $H_{\mathrm s}=3$ on $[-5,0)$, $1$ on $(0,5]$, $v=0$, $g=1$ | $(-5,5)$, non-penetration walls at both ends; time interval $(0,6)$ | 5 space-time slabs; 8 spatial elements, 32 triangles with $q=1$, $p=2$ in the first slab |
| [Chu et al. (2025b)](/sources/chu-2025-b.md) Ex. 7 | 1D thermal (Ripa), non-flat bottom | $(h,v,\mathsf b)=(5-b,0,1)$ for $y<0$, $(2-b,0,5)$ otherwise; $b=\cos(10\pi(y+0.3))+1$ on $[-0.4,-0.2]$, $\tfrac12[\cos(10\pi(y-0.3))+1]$ on $[0.2,0.4]$, $0$ elsewhere | $[-1,1]$, free boundaries | $\Delta y=1/100$ (also $1/200$, $1/400$); $t=0.2$; reference PCCU on $1/2000$ |
| Chu et al. (2025b) Ex. 9 | radial thermal, flat bottom, no Coriolis | $(h,v_1,v_2,\mathsf b)=(1.5,0,0,1)$ for $r<0.5$, $(1.2,0,0,1.5)$ otherwise | $[-1,1]^2$, free boundaries | $\Delta x=\Delta y=1/50$; $t=0.15$; reference on $1/400$ |
| [Liu et al. (2026)](/sources/liu-2026.md) §5.1.2, Eq. (5.5) | 1D, flat bottom, randomized | training: $h_{\mathrm L}=3.5$, $h_{\mathrm R}=1$, $v=0$, jump at $x=0$, each perturbed by a uniform random amount (within $\pm0.2$ for the depths, $\pm0.1$ for the velocities and the jump position); test: $h_{\mathrm L}=3.5691196$, $h_{\mathrm R}=1.178673$, $v_{\mathrm L}=-0.064667$, $v_{\mathrm R}=-0.045197$, jump at $x=0.003832$ | $(-5,5)$, Dirichlet | PyClaw (HLLE) data on 512 points, $\Delta t=0.005$, 300 trajectories of 20 steps; test to $T=1.5$ |

Del Grosso et al. use CFL 0.5 for their first-order and 0.25 for their second-order
schemes, with the minmod limiter, in all their tests (§5). Kolluru et al. print neither
$h_{\mathrm L}$, $h_{\mathrm R}$ nor $g$ (their Eq. (8c) is symbolic). Del Grosso et al.'s
radial non-flat case is a cosine bump, with a topography "inspired by" an earlier test; the
region where the bump formula holds is not printed. Naudet & Zahr's free-surface data
coincide with the depth because their bottom is flat. Chu et al.
(2025b) write the one-dimensional Ripa problem in the variable $y$ and
use SSP-RK3 with CFL 0.45 and the generalized minmod limiter with
parameter 1.3 in all their tests (§5). In their Example 7 the free
surface $h+b$ is 5 on the left and 2 on the right, and the buoyancy
jumps from 1 to 5, so the left state has $\tfrac{\mathsf b}2h^2=\tfrac12(5-b)^2$
and the right one $\tfrac52(2-b)^2$ *(compiler check, not in the sources)*.

**Wave pattern of the walled case** *(compiler check, not in the sources)*. For
$h_{\mathrm L}=3$, $h_{\mathrm R}=1$, $g=1$, the intermediate state of the Riemann problem
solves $2\big(\sqrt{gh_{\mathrm L}}-\sqrt{gh_*}\big)=(h_*-h_{\mathrm R})\sqrt{g(h_*+h_{\mathrm R})/(2h_*h_{\mathrm R})}$,
which gives $h_*\approx1.849$, $v_*\approx0.745$ and a bore speed
$h_*v_*/(h_*-h_{\mathrm R})\approx1.623$. The rarefaction head moves at
$-\sqrt{gh_{\mathrm L}}\approx-1.732$ and its tail at $v_*-\sqrt{gh_*}\approx-0.615$. The head
reaches the wall $x=-5$ at $t\approx2.89$ and the bore reaches $x=5$ at $t\approx3.08$, so
both reflections, and their interaction with the rest of the solution, fall inside Naudet &
Zahr's interval $(0,6)$.

## Findings

**Multi-dimensional versus two-point fluxes (radial).** Del Grosso et al. compare their
multi-dimensional-aware finite-volume scheme, in which the face fluxes come from a nodal
solver (several states around each node), with the classical two-point face-based scheme on
the same unstructured grids. On both radial dam breaks the two-point scheme is "slightly less
diffusive" than the multi-point one, as the authors had observed for the Euler equations in
earlier work, and the second-order schemes are much less diffusive than the first-order ones
(§5.3, Figs. 7–10). The radial tests are thus a measure of dissipation; the same paper uses
other problems (colliding flow, odd–even decoupling, a supercritical cylinder flow) to show
that the multi-point scheme avoids the
[carbuncle](/definitions/carbuncle-phenomenon.md) that the two-point scheme develops. The
scheme is designed to be [well-balanced](/properties/well-balancing.md), positive and
[entropy-stable](/properties/entropy-stability.md); only wet states ($h>0$) are treated (§2,
§6).

**Spectral shock capturing (1D).** Kolluru et al. run the problem with their spectral
relaxation (SR) Fourier method, which damps high wavenumbers towards a filtered state with a
positive kernel (see [artificial and spectral viscosity](/methods/artificial-viscosity.md)),
without dealiasing, at $N_x=2665$. The Fejér–Korovkin kernel with parameters $(0.55,0.99)$ is
slightly overdamped; the de la Vallée-Poussin kernel with $(0.70,0.98)$ is closer to the
reference but oscillatory (§3.3, Fig. 13). On their water-hump problem (Fig. 12) the
Fejér–Korovkin kernel with $(0.5,0.99)$ follows the Godunov (CLAWPACK) reference through shock
formation, while the de la Vallée-Poussin kernel with $(0.8225,0.98)$ shows bounded oscillations
at the shock.

**Space-time shock tracking (walled).** Naudet & Zahr's space-time
[implicit shock tracking](/methods/implicit-shock-tracking.md) (HOIST) tracks the bore and the
head and tail of the rarefaction as surfaces in space-time, and the second slab is stretched in
time so that the wall reflections are "represented perfectly" (§5.2, Fig. 15). The test is
coarse by design: 32 curved triangles in the first slab, against grids of thousands of cells
for the capturing schemes above.

**Characteristic central-upwind fluxes (thermal, 1D and radial).** Chu et al. (2025b) apply
their flux-globalization [LCD central-upwind](/methods/lcd-central-upwind-scheme.md) scheme
(LCD-PCCU), in which the numerical diffusion of the path-conservative
[central-upwind](/methods/central-upwind-scheme.md) flux is set field by field in local
characteristic variables of the [globalized flux](/methods/flux-globalization.md), and
compare it with the scalar-diffusion PCCU scheme. Both are
[well-balanced](/properties/well-balancing.md) through a reconstruction in equilibrium
variables. On the one-dimensional problem the $L^1$ errors of $h+b$ at $t=0.2$ are (Table 5.4):

| $\Delta y$ | 1/100 | 1/200 | 1/400 |
|---|---|---|---|
| PCCU | 5.44e-2 | 3.08e-2 | 1.48e-2 |
| LCD-PCCU | 2.99e-2 | 1.65e-2 (printed 1.65e-3) | 7.50e-3 |

with rates 0.821, 1.057 (PCCU) and 0.858, 1.137 (LCD-PCCU), close to 1, as the authors
expect for discontinuous solutions (§5.1); the authors call LCD-PCCU "much more accurate"
(§5.2), and its errors are 0.51–0.55 times PCCU's *(compiler check, not in the
sources)*. On the radial problem LCD-PCCU resolves $h$ and $\mathsf b$ more sharply, in the
plane and along the diagonal $y=x$, than PCCU, which smears them (Figs. 5.14–5.15).

**Learning the flux and the entropy from data (1D).** Liu et al. (2026)
(arXiv v1) train a neural entropy-stable flux and a convex neural
entropy on randomized dam breaks generated by PyClaw, the training
window containing the discontinuities from the start. On the test datum the learned model keeps the shock
structure even with noise at the full relative level $\xi=1$ ($\xi$
page-local), better than on Burgers' equation, where the training data
end before the shock forms; the discrete conservation remainder stays
of order $10^{-5}$ and their discrete entropy remainder non-positive over
a family of 101 dam breaks, $h=6-0.01k$ for $x<0.01k$ and $0.1+0.01k$
beyond, at rest ($k$ page-local, their index; Eq. (5.6)) (§5.2.2,
Figs. 5.4–5.6). The test datum has small non-zero velocities and is a
perturbed dam break rather than water at rest; see
[Burgers equation tests](/benchmarks/burgers-equation-tests.md).

## Qualifications

- Only Chu et al. (2025b) report an error norm for the dam break; the other comparisons are
  visual, against a fine-grid or a reference solution.
- Chu et al. (2025b) print the LCD-PCCU error at $\Delta y=1/200$ as 1.65e-3, which with its
  printed neighbours would give rates 4.18 and $-2.18$; 1.65e-2 reproduces the printed rates
  0.858 and 1.137 ($\log_2(2.99/1.65)=0.858$, $\log_2(1.65/0.750)=1.138$) *(compiler check, not
  in the sources)*. They also print the bottom of Example 7 with $x$ inside a function of $y$,
  and the mesh as $\Delta x$; the first bump carries no factor $\tfrac12$, the second does.
- Kolluru et al.'s values of $h_{\mathrm L}$, $h_{\mathrm R}$ and $g$ are not printed, so their run
  cannot be reproduced from the paper; Liu et al. (2026) do not print $g$ either.
- Naudet & Zahr write the free-surface height and a boundary-normal component with the same
  letter in one sentence of §5.2; the page writes $H_{\mathrm s}$ for the former.

# Citations

- [Del Grosso et al. (2024)](/sources/delgrosso-2024.md) — §5 (CFL, limiter), §5.3, §5.3.1, Figs. 7–10 (HAL preprint).
- [Kolluru et al. (2024)](/sources/kolluru-2024.md) — §3.3, Eqs. (8b)–(8c), Figs. 12–13 (arXiv v2).
- [Naudet & Zahr (2024)](/sources/naudet-2024.md) — §5.2, Eq. (54), Fig. 15.
- [Chu et al. (2025b)](/sources/chu-2025-b.md) — §3, §5.2, Examples 7 and 9, Table 5.4, Figs. 5.11, 5.14–5.15.
- [Liu et al. (2026)](/sources/liu-2026.md) — §5.1.2, Eqs. (5.5)–(5.6), §5.2.2, Figs. 5.4–5.6 (arXiv v1).

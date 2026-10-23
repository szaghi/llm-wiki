---
type: Benchmark
title: "Dam-break problems"
description: "Shallow-water Riemann problems with water at rest at two depths separated by a removed dam, in one dimension, between reflecting walls, and in the radial two-dimensional form, used to test shock and rarefaction capturing, multi-dimensional dissipation, spectral shock capturing and space-time shock tracking."
status: established
aliases: [dam break, dam-break problem, shallow-water dam break, circular dam break, radial dam break, cylindrical dam break]
tags: [benchmark, shallow-water, riemann-problem, shock-tracking]
timestamp: 2026-10-23T11:06:00Z
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
as on the shallow-water page). Three variants run in the bundle: the one-dimensional problem
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

Del Grosso et al. use CFL 0.5 for their first-order and 0.25 for their second-order
schemes, with the minmod limiter, in all their tests (§5). Kolluru et al. print neither
$h_{\mathrm L}$, $h_{\mathrm R}$ nor $g$ (their Eq. (8c) is symbolic). Del Grosso et al.'s
radial non-flat case is a cosine bump, with a topography "inspired by" an earlier test; the
region where the bump formula holds is not printed. Naudet & Zahr's free-surface data
coincide with the depth because their bottom is flat.

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

## Qualifications

- None of the three sources reports an error norm for the dam break; the comparisons are
  visual, against a fine-grid or a reference solution.
- Kolluru et al.'s values of $h_{\mathrm L}$, $h_{\mathrm R}$ and $g$ are not printed, so their run
  cannot be reproduced from the paper.
- Naudet & Zahr write the free-surface height and a boundary-normal component with the same
  letter in one sentence of §5.2; the page writes $H_{\mathrm s}$ for the former.

# Citations

- [Del Grosso et al. (2024)](/sources/delgrosso-2024.md) — §5 (CFL, limiter), §5.3, §5.3.1, Figs. 7–10 (HAL preprint).
- [Kolluru et al. (2024)](/sources/kolluru-2024.md) — §3.3, Eqs. (8b)–(8c), Figs. 12–13 (arXiv v2).
- [Naudet & Zahr (2024)](/sources/naudet-2024.md) — §5.2, Eq. (54), Fig. 15.

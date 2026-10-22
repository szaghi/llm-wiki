---
type: Benchmark
title: "Two-dimensional explosion and implosion problems"
description: "Multi-dimensional Euler tests with Sod-type circular, spherical and diamond-shaped initial discontinuities: the long-time cylindrical explosion and the Liska–Wendroff implosion used as gauges of numerical dissipation, and short-time radial and spherical explosions used for monotonicity, symmetry and adaptive-cost tests."
status: established
aliases: [explosion problem, implosion problem, cylindrical explosion, spherical explosion, 2D explosion, Liska–Wendroff implosion]
tags: [benchmark, low-dissipation, central-scheme, teno]
timestamp: 2026-10-23T16:00:00Z
---

# Two-dimensional explosion and implosion problems

Two families of multi-dimensional Euler tests start from a uniform gas at
rest with a region of different density and pressure. In an
**explosion** the inner region carries the higher state, a shock runs
outwards and a contact follows; in an **implosion** the inner region
carries the lower state, a shock converges on the centre and reflects.
The sources use them in two ways. Run for a long time, the contact of the
explosion becomes unstable and the implosion sends a jet along the
diagonal: the amount of small-scale structure and the length of the jet
then serve as gauges of
[numerical dissipation](/definitions/numerical-dissipation.md). Run for a
short time, a circular or spherical Sod problem tests monotonicity and
symmetry on unstructured or adaptive meshes. All runs solve the Euler
equations; every source prints $\gamma=1.4$ except Ji, Liang & Fu, who
print no $\gamma$ for their explosions.

## Long-time cylindrical explosion

[Chertock et al. (2023)](/sources/chertock-2023.md) Ex. 6 (arXiv v2) and
[Wang et al. (2023)](/sources/wang-2023-b.md) Ex. 6 print the same data:
$(\rho,v_1,v_2,p)=(1,0,0,1)$ for $x^2+y^2<0.16$, i.e. inside the circle
of radius 0.4, and $(0.125,0,0,0.1)$ outside, computed in the first
quadrant $[0,1.5]^2$ with solid walls at $x=0$ and $y=0$ and free
boundaries at $x=1.5$ and $y=1.5$, $\Delta x=\Delta y=3/800$, $t=3.2$.

Both papers compare a new scheme with its predecessor on the shape of
the contact: the [LCD central-upwind scheme](/methods/lcd-central-upwind-scheme.md)
of Chertock et al. gives a "substantially curlier" contact and a
slightly wider mixing layer than the original
[central-upwind scheme](/methods/central-upwind-scheme.md), with the
shock still stable (Fig. 5.6); the
[adaptive diffusion central-upwind flux](/methods/adaptive-diffusion-central-upwind-flux.md)
of Wang et al. in [A-WENO](/methods/alternative-weno.md) gives a "much
curlier" contact than their earlier adaptive diffusion central flux
(Fig. 6). Wang et al. state the reasoning behind the gauge: the contact
is physically unstable and "may be stabilized by the ND only", so less
dissipation shows as more roll-up.

## Implosion

The diamond-shaped implosion is attributed by the sources to Liska &
Wendroff.

| Source | Low state inside | Domain and boundaries | Grid | $t$ |
|---|---|---|---|---|
| [Chertock et al. (2023)](/sources/chertock-2023.md) Ex. 7 | $(0.125,0,0,0.14)$ for $\lvert x\rvert+\lvert y\rvert<0.15$ | $[0,0.3]^2$, solid walls | $\Delta x=1/2000$ (also $1/2500$, $3/10000$ for the old scheme) | 2.5 |
| [Wang et al. (2023)](/sources/wang-2023-b.md) Ex. 7 | same | $[0,0.3]^2$, solid walls | $\Delta x=3/4000$ | 2.5 |
| [Liang et al. (2022)](/sources/liang-2022.md) §4.9 | $(0.125,0,0,0.14)$ for $\lvert x+y\rvert<0.15$ and $\lvert x-y\rvert<0.15$ | "periodic box" $[-0.3,0.3]^2$ | $800\times800$ | 0.8 |

The ambient state is $(1,0,0,1)$ in all three. The two printed regions
are the same diamond, since $\max(\lvert x+y\rvert,\lvert x-y\rvert)=\lvert x\rvert+\lvert y\rvert$,
and Liang et al.'s $800\times800$ grid on a side of 0.6 has the spacing
$3/4000$ of Wang et al. *(compiler check, not in the sources)*. A solution
of Liang et al.'s problem that keeps the symmetry of the data, even in
$x$ and in $y$, is in the periodic box the same as the solution on the
quadrant $[0,0.3]^2$ with solid walls on all four sides, because
evenness and period $0.6$ make $x=\pm0.3$ mirror lines as well as $x=0$
*(compiler check, not in the sources)*. The three sources thus run one
problem; Liang et al. stop at $t=0.8$, the others at $t=2.5$.

What is measured differs. Chertock et al. and Wang et al. read the
distance the jet travels along $y=x$ as a sign of low dissipation: the
new schemes send it further. Chertock et al. add an efficiency
statement: at equal CPU time the new scheme on $\Delta x=1/2000$ "still
achieves a much higher resolution" than the old one on $1/2500$, and the
old one needs $3/10000$ to look "similar"; no timings or hardware are
given. Equal CPU time on these two grids means the new scheme costs about
$(2500/2000)^3\approx1.95$ times as much per cell and step, counting the
time-step reduction *(compiler check, not in the sources)*. Liang et al.
use the problem for [symmetry preservation](/properties/symmetry-preservation.md):
their low-dissipation TENO scheme with a
[THINC](/methods/thinc-reconstruction.md)-type jump reconstruction keeps
"rigorous flow symmetry", with a symmetry-preserving implementation
technique taken from earlier work, since such schemes "may cause the
so-called symmetry breaking issue … due to machine round-off errors"
(Fig. 21).

**A training variant.** [Bezgin et al. (2023)](/sources/bezgin-2023.md)
(§7.4, Eq. 49, arXiv v1) use a corner implosion on $[0,1]^2$ as the
training and test problem of a learned flux in
[JAX-Fluids](/software/jax-fluids.md): $(\rho,v_1,v_2,p)=(0.14,0,0,0.125)$
for $x+y\le0.15$ and $(1,0,0,1)$ otherwise, walls at the lower left and
an "open domain" for the rarefaction (the boundaries are not fully
specified). Density and pressure of the inner state are swapped against
the Liska–Wendroff data above, and the domain is larger than the
quadrant $[0,0.3]^2$, so it is a different problem. The reference is WENO3-JS with second-order Runge–Kutta
and HLLC on $128\times128$, $\Delta t=2.5\times10^{-4}$, sampled every
$10^{-3}$ for 2501 steps and coarse-grained to $32\times32$. A Rusanov
flux whose dissipation coefficient is a small neural network
(Rusanov-NN; see [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)
and [learned WENO weights](/methods/learned-weno-weights.md)), trained
end-to-end through the differentiable solver on the first 1000 coarse
steps, is less dissipative than the classical Rusanov flux, stays
stable over all 2501 steps and has lower relative $L_1$ errors of
density and pressure, also beyond the training horizon (Figs. 20–21).

## Short-time radial and spherical explosions

**Unstructured triangles.** [Ji, Liang & Fu (2022)](/sources/ji-2022.md)
§5.6 (preprint) run two cylindrical explosions on a disc of radius 1
centred at $(1,1)$ with 18,464 triangles ($h\approx1/50$) to $t=0.2$:
EP01, $(1,0,0,1)$ inside $\lVert r\rVert\le0.5$ and $(0.125,0,0,0.1)$
outside; EP02, $(1,0,0,2)$ inside and $(1,0,0,1)$ outside. On EP01 their
unstructured finite-volume [TENO](/methods/targeted-eno.md) schemes
(TENO3 to TENO6), WENO5 and [CWENO5](/methods/cweno.md) all preserve
monotonicity; on EP02 TENO and CWENO5 are similar, while WENO5 shows
spurious oscillations near the discontinuities (Figs. 12–17).

**Spherical explosions in three dimensions.** Two sources run the Sod
states $(\rho,v,p)=(1,0,1)$ for $r\le0.5$ and $(0.125,0,0.1)$ outside:

- Ji et al. §5.9, on uniform tetrahedra with $h\approx1/30$ to $t=0.25$,
  domain not printed: TENO3 to TENO6 show no obvious artefacts in
  density and pressure profiles, which "agree with the analytical
  solutions well" (Fig. 26), although no analytical solution or its
  source is given.
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) §8.9, on
  $[-1,1]^3$ with $50^3$ elements and Dirichlet boundaries to $t=0.2$,
  local Lax–Friedrichs flux ("robust … for this focusing wave problem"),
  against a one-dimensional spherical reference with geometric source
  term. Static DG with finite-volume subcells, $p$-adaptive and
  [hp-adaptive](/methods/hp-adaptation.md) DG take 10,839 s, 3557 s and
  8601 s on one AMD EPYC 7302 core, with 235, 241 and 248 time steps and
  39.8, 48.6 and 157.3 GB of memory (Table 6). The speedups are 3.05
  and 1.26 *(compiler check, not in the sources)*; the authors explain
  the small gain of the hp variant by almost 8 % of the elements being
  finite-volume limited.

A two-dimensional radial Sod problem and a three-dimensional spherical
one on an adaptive moving mesh are recorded on
[Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md).

## Qualifications

- The long-time gauges are visual. Grid-converged solutions of these
  physically unstable flows are not shown by any source, and more
  small-scale structure is not by itself evidence of accuracy (the same
  caveat as for the [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md)
  and [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md)
  instabilities).
- Each long-time comparison is against one predecessor only: Wang et
  al. against their own earlier adaptive diffusion central flux,
  Chertock et al. against the original central-upwind scheme.
- Liang et al.'s final time is given only in the caption of Fig. 21.
- Ji et al. print "$\lVert r\rVert\le0.5$" without restating the centre
  of the disc; the 3D domain is not printed.

# Citations

- [Chertock et al. (2023)](/sources/chertock-2023.md) — Exs. 6–7, Fig. 5.6 (arXiv v2).
- [Wang et al. (2023)](/sources/wang-2023-b.md) — Exs. 6–7, Figs. 6–7.
- [Liang et al. (2022)](/sources/liang-2022.md) — §4, §4.9, Fig. 21.
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §5.6, §5.9, Figs. 12–17, 26 (preprint).
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — §8.9, Table 6.
- [Bezgin et al. (2023)](/sources/bezgin-2023.md) — §7.4, Eq. 49, Figs. 20–21 (arXiv v1).

---
type: Benchmark
title: "Two-dimensional explosion and implosion problems"
description: "Multi-dimensional Euler tests with Sod-type circular, spherical and diamond-shaped initial discontinuities: the long-time cylindrical explosion and the Liska–Wendroff implosion used as gauges of numerical dissipation, and short-time radial and spherical explosions used for monotonicity, symmetry and adaptive-cost tests."
status: established
aliases: [explosion problem, implosion problem, cylindrical explosion, spherical explosion, 2D explosion, Liska–Wendroff implosion]
tags: [benchmark, low-dissipation, central-scheme, teno]
timestamp: 2026-10-24T06:00:00Z
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
equations; every source prints $\gamma=1.4$ except Ji, Liang & Fu
(2022), who print no $\gamma$ for their explosions; their sequel (2023)
states $\gamma=1.4$ for all its Euler tests (§2.1).

## Long-time cylindrical explosion

[Chertock et al. (2023)](/sources/chertock-2023.md) Ex. 6 (arXiv v2),
[Wang et al. (2023b)](/sources/wang-2023-b.md) Ex. 6 and
[Chu et al. (2025c)](/sources/chu-2025-c.md) Ex. 4 (arXiv v1) print the same data:
$(\rho,v_1,v_2,p)=(1,0,0,1)$ for $x^2+y^2<0.16$, i.e. inside the circle
of radius 0.4, and $(0.125,0,0,0.1)$ outside, computed in the first
quadrant $[0,1.5]^2$ with solid walls at $x=0$ and $y=0$ and free
boundaries at $x=1.5$ and $y=1.5$, $\Delta x=\Delta y=3/800$, $t=3.2$.

Chertock et al. and Wang et al. (2023b) compare a new scheme with its predecessor on the shape of
the contact: the [LCD central-upwind scheme](/methods/lcd-central-upwind-scheme.md)
of Chertock et al. gives a "substantially curlier" contact and a
slightly wider mixing layer than the original
[central-upwind scheme](/methods/central-upwind-scheme.md), with the
shock still stable (Fig. 5.6); the
[adaptive diffusion central-upwind flux](/methods/adaptive-diffusion-central-upwind-flux.md)
of Wang et al. (2023b) in [A-WENO](/methods/alternative-weno.md) gives a "much
curlier" contact than their earlier adaptive diffusion central flux
(Fig. 6). Wang et al. (2023b) state the reasoning behind the gauge: the contact
is physically unstable and "may be stabilized by the ND only", so less
dissipation shows as more roll-up.

Chu et al. (2025c) use the problem to compare their new
[low-dissipation central-upwind scheme](/methods/low-dissipation-central-upwind-scheme.md)
(NEW), whose subcell projection places the jump at
$x_{i+1/2}+v^{\mathrm{int}}\Delta t$ ($v^{\mathrm{int}}$ the
page-local intermediate velocity) instead of at the interface, with the
original LDCU scheme of Kurganov & Xin (OLD); both second order with the
generalized minmod limiter (minmod parameter $\theta=1.3$, page-local), SSP-RK3, CFL 0.475. OLD
oscillates along the free boundaries $x=1.5$ and $y=1.5$, NEW much less,
while OLD "achieves a slightly better resolution" of the contact here
(Fig. 3.4). The gauge does not favour the new scheme on this test, in
contrast with the two comparisons above.

## Implosion

The diamond-shaped implosion is attributed by the sources to Liska &
Wendroff.

| Source | Low state inside | Domain and boundaries | Grid | $t$ |
|---|---|---|---|---|
| [Chertock et al. (2023)](/sources/chertock-2023.md) Ex. 7 | $(0.125,0,0,0.14)$ for $\lvert x\rvert+\lvert y\rvert<0.15$ | $[0,0.3]^2$, solid walls | $\Delta x=1/2000$ (also $1/2500$, $3/10000$ for the old scheme) | 2.5 |
| [Wang et al. (2023b)](/sources/wang-2023-b.md) Ex. 7 | same | $[0,0.3]^2$, solid walls | $\Delta x=3/4000$ | 2.5 |
| [Liang et al. (2022)](/sources/liang-2022.md) §4.9 | $(0.125,0,0,0.14)$ for $\lvert x+y\rvert<0.15$ and $\lvert x-y\rvert<0.15$ | "periodic box" $[-0.3,0.3]^2$ | $800\times800$ | 0.8 |
| [Tang (2024)](/sources/tang-2024.md) §4.4.3, Eq. (35) | $(0.125,0,0,0.14)$ for $\lvert x\rvert+\lvert y\rvert<0.15$ | $[-0.3,0.3]^2$, reflecting | $400\times400$ | 2.5 |
| [Chu et al. (2025a)](/sources/chu-2025.md) Ex. 5 | $(0.125,0,0,0.14)$ for $\lvert x\rvert+\lvert y\rvert<0.15$ | $[0,0.5]^2$ as printed, solid walls on all four sides | $\Delta x=1/2000$ | 2.5 |
| [Chu et al. (2025c)](/sources/chu-2025-c.md) Ex. 5 | $(0.125,0,0,0.14)$ for $\lvert x\rvert+\lvert y\rvert<0.15$ | $[0,0.3]^2$, solid walls | $\Delta x=1/2000$ | 2.5 |

The ambient state is $(1,0,0,1)$ in all six. The two printed regions
are the same diamond, since $\max(\lvert x+y\rvert,\lvert x-y\rvert)=\lvert x\rvert+\lvert y\rvert$,
and Liang et al. (2022)'s $800\times800$ grid on a side of 0.6 has the spacing
$3/4000$ of Wang et al. (2023b) *(compiler check, not in the sources)*. A solution
of Liang et al. (2022)'s problem that keeps the symmetry of the data, even in
$x$ and in $y$, is in the periodic box the same as the solution on the
quadrant $[0,0.3]^2$ with solid walls on all four sides, because
evenness and period $0.6$ make $x=\pm0.3$ mirror lines as well as $x=0$
*(compiler check, not in the sources)*. The three sources thus run one
problem; Liang et al. (2022) stop at $t=0.8$, the others at $t=2.5$. Tang's
full box with reflecting walls is, for a symmetric solution, the same
problem again, on a grid of spacing $3/2000$, twice that of Wang et al. (2023b)
*(compiler check, not in the sources)*. Chu et al. (2025a) print
the quadrant as $[0,0.5]^2$, with the same diamond and walls on all four
sides; the walls at $x=0.5$ and $y=0.5$ then lie farther from the
diamond than the mirror lines $x,y=0.3$ of the other runs, so their
problem is not the same after the waves reach the outer walls
*(compiler check, not in the sources)*.

What is measured differs. Chertock et al. and Wang et al. (2023b) read the
distance the jet travels along $y=x$ as a sign of low dissipation: the
new schemes send it further. Chertock et al. add an efficiency
statement: at equal CPU time the new scheme on $\Delta x=1/2000$ "still
achieves a much higher resolution" than the old one on $1/2500$, and the
old one needs $3/10000$ to look "similar"; no timings or hardware are
given. Equal CPU time on these two grids means the new scheme costs about
$(2500/2000)^3\approx1.95$ times as much per cell and step, counting the
time-step reduction *(compiler check, not in the sources)*. Liang et al. (2022)
use the problem for [symmetry preservation](/properties/symmetry-preservation.md):
their low-dissipation TENO scheme with a
[THINC](/methods/thinc-reconstruction.md)-type jump reconstruction keeps
"rigorous flow symmetry", with a symmetry-preserving implementation
technique taken from earlier work, since such schemes "may cause the
so-called symmetry breaking issue … due to machine round-off errors"
(Fig. 21). Tang reads the jet as Chertock et al. and Wang et al. (2023b) do:
the adaptive-cut-off TENO-AZ builds finer and longer diagonal jets,
while the TENO-Z and TENO-LAD results "show a large amount of noise"
(§4.4.3, Fig. 12; see [adaptive TENO](/methods/adaptive-teno.md)).

Chu et al. (2025a) (arXiv v1, two authors; the version of record
adds Menshov) also measure how far the jet goes. Their adaptive
[low-dissipation central-upwind schemes](/methods/low-dissipation-central-upwind-scheme.md)
switch the reconstruction, in local characteristic variables, from the
Minmod2 limiter to an overcompressive limiter in cells flagged as
rough, either by a minmod-based detector (A-MM) or by a weak local
residual above $C_{\mathrm W}(\Delta x)^2$ (A-WLR, $C_{\mathrm W}=5$ here; SSP-RK3, CFL 0.4). The
jet goes much further with both adaptive schemes than with the
Minmod2 scheme LDCU. A-MM "seems to contain even smaller amount of
numerical diffusion" than A-WLR, which, the authors show, flags only
cells along the shocks, and a smaller $C_{\mathrm W}$ makes A-WLR sharp
on coarse meshes but gives "severe instabilities" on $\Delta x=1/2000$
(Figs. 4.7–4.8). Symmetry about $y=x$, lost to round-off in these
low-dissipation schemes, is enforced by averaging mirrored cell values
after each time step (Remark 4.1).

Chu et al. (2025c) run Chertock et al.'s problem on Chertock et al.'s
finest grid for the new scheme and find NEW slightly less oscillatory,
with a jet that propagates further, "slightly higher resolution" than
OLD (Fig. 3.5). Both of their 2D tests are attributed to Liska &
Wendroff.

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
[Ji, Liang & Fu (2023)](/sources/ji-2023.md) §4.3 rerun EP01 and EP02 on
the same mesh to $t=0.2$ with their dual-stencil-selection TENO4-D to
TENO7-D and find the discontinuities captured without obvious
oscillations, in agreement with the reference and with CWENO of the same
order (Figs. 3–6).

**Circular Sod explosion and conservation.**
[Gaburro et al. (2024)](/sources/gaburro-2024.md) §5.1.4 (arXiv v1) use
the same states, $(1,0,0,1)$ inside $r\le0.5$ and $(0.125,0,0,0.1)$
outside, on $[-1,1]^2$ with walls, to $t=0.25$, on polygonal meshes with
$h=1/50$ and $1/215$, against a one-dimensional radial reference with
geometric source terms. Their ADER-DG evolves primitive variables; applied
everywhere, shocks included, it gives a wrong shock speed, and switching
to a conservative finite-volume update only in the shock-triggered
subcells "is enough to restore" the correct speed at $\mathbb P^2$ and $\mathbb P^3$
(Fig. 3). The switch follows from their modified
[Lax–Wendroff theorem](/results/lax-wendroff-theorem.md) (§4): a
scheme whose local conservation defect vanishes with $h$ converges, if
it converges, to a weak solution; the defect of the primitive-variable
update vanishes for smooth flow and for contacts but not at shocks, so
the conservative update is applied in the shock cells only.

**Lagrangian particles.** [Jiang et al. (2024)](/sources/jiang-2024.md)
§4.2.2 run a cylindrical Sod problem on the disc $x^2+y^2\le1.5$ with
$(p,\rho)=(1,1)$ inside and $(0.1,0.125)$ outside, the inner radius not
printed, with particle spacing $\Delta x_0=0.01$ to $t=0.2$: their
Lagrangian weighted-least-squares scheme with WENO-Z-type pair states
is less dissipative than the WENO-SPH and MWSPH particle methods of the
literature, and its accuracy rises with the number of local refinement
levels on $\Delta x_0=0.02$ (Fig. 5).

**Spherical explosions in three dimensions.** Two sources run the Sod
states $(\rho,v,p)=(1,0,1)$ for $r\le0.5$ and $(0.125,0,0.1)$ outside:

- Ji, Liang & Fu (2022) §5.9, on uniform tetrahedra with $h\approx1/30$ to $t=0.25$,
  domain not printed: TENO3 to TENO6 show no obvious artefacts in
  density and pressure profiles, which "agree with the analytical
  solutions well" (Fig. 26), although no analytical solution or its
  source is given. Their sequel (2023) §4.9 repeats the case on the
  same kind of mesh ($h\approx1/30$, $t=0.25$; the sentence giving both
  is printed at the end of §4.8): TENO6-D and TENO7-D show no obvious
  artefacts and agree with the analytical solutions and with CWENO
  (Fig. 21).
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

**Circular explosion with a posteriori viscosity, low-Mach scheme.**
[Zampa & Dumbser (2025)](/sources/zampa-2025.md) §4.3 (arXiv v1) run the
circular Sod data, $(\rho,p)=(1,1)$ for $r\le0.5$ and $(0.125,0.1)$
outside, at rest, on the periodic $[-1,1]^2$ with 120×120 elements to
$t=0.25$, against a radial reference. Their semi-implicit compatible
finite-element scheme for weakly compressible flow, of degree 2, adds an
artificial viscosity only in cells that fail a relaxed discrete maximum
principle, after which the step is recomputed; the viscosity is active
only near the discontinuities and no spurious oscillations appear
(Figs. 3–4). The scheme evolves a non-conservative entropy equation, and
the authors do not expect it to compute shocks correctly at large shock
Mach numbers (§3.2.2); agreement with the reference is shown by plots.

**Learned slopes on a circular explosion.** [de Romémont et al.
(2026)](/sources/deromemont-2026.md) §6.3 take the circle of radius 0.2
centred at $(0.5,0.5)$ in $[0,1]^2$ with the same Sod states, citing
Toro's book in the text and Liska & Wendroff in the caption of Fig. 14.
Their second-order MUSCL finite volumes with
[learned slopes](/methods/learned-weno-weights.md) on $256^2$ reduce the
relative $L^1$ error of the same scheme with standard slopes on the same
grid, against a $1024^2$ reference, by 6 %, the smallest gain of their
tests and outside the "20–50%" of their abstract; the final time is not
printed.

**Explosion among obstacles on triangles.** [Liang et al.
(2025)](/sources/liang-2025.md) §4.7 call "implosion inside multiple
circles" a unit disc with eight circular solid holes around a central
disc, $(\rho,v_1,v_2,p)=(1,0,0,1)$ in the central disc and
$(0.125,0,0,0.14)$ elsewhere (values given only in the labels of Fig.
19), reflective boundaries, 911,276 triangles ($h\approx1/400$),
snapshots at $t=0.15$, $0.25$, $0.75$, $1.0$; no source of the setup is
printed. The high state sits in the central disc, so in this page's
terms the data are an explosion that then reflects off the obstacles and
the outer wall *(compiler check, not in the sources)*. Their
unstructured TENO6-E resolves richer interfacial instabilities than
CWENO6 at 20583.60 s against 46562.19 s, "about 44.2%" of the CWENO6
cost (Fig. 20; hardware not stated).

A two-dimensional radial Sod problem and a three-dimensional spherical
one on an adaptive moving mesh are recorded on
[Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md). The
two-fluid "cylindrical explosion" of
[Chu et al. (2025b)](/sources/chu-2025-b.md) Ex. 5, a
high-pressure gas bubble in water below a layer of air, is a
gas–liquid problem and is recorded on
[underwater explosion](/benchmarks/underwater-explosion.md). The
relativistic-MHD cylindrical explosions of Komissarov, which
[Stone et al. (2026)](/sources/stone-2026.md) §3.5 run with a
first-order flux fallback in their GPU AMR code (Fig. 10), are
magnetized blasts and are recorded on
[MHD blast wave and rotor](/benchmarks/mhd-blast-wave.md); the same
paper's supernova in a turbulent multiphase interstellar medium
($2048^3$ cells, with heating and cooling, §3.1, Fig. 2) is an
application run, not a test with a reference solution.

## Qualifications

- The long-time gauges are visual. Grid-converged solutions of these
  physically unstable flows are not shown by any source, and more
  small-scale structure is not by itself evidence of accuracy (the same
  caveat as for the [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md)
  and [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md)
  instabilities).
- Each long-time comparison is against one predecessor only: Wang et
  al. (2023b) against their own earlier adaptive diffusion central flux,
  Chertock et al. against the original central-upwind scheme, Chu et
  al. (2025c) against the original LDCU scheme.
- de Romémont et al.'s gain is a relative $L^1$ error reduction on one
  grid against a fine-grid run of the standard scheme, not an order or
  a convergence statement.
- Liang et al. (2022)'s final time is given only in the caption of Fig. 21.
- Chu et al. (2025a)'s adaptive schemes depend on the constant $C_{\mathrm W}$
  of the residual threshold, tuned per problem; the authors conclude
  that this hurts the robustness of A-WLR and that the minmod-based
  detector gives the robust adaption strategy (§5).
- Ji, Liang & Fu (2022) print "$\lVert r\rVert\le0.5$" without restating the centre
  of the disc; the 3D domain is not printed. Ji, Liang & Fu (2023) print
  the disc as "a unit circle of radius $R=1$ centered at $[1,1]$" again.

# Citations

- [Chertock et al. (2023)](/sources/chertock-2023.md) — Exs. 6–7, Fig. 5.6 (arXiv v2).
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — Exs. 6–7, Figs. 6–7.
- [Liang et al. (2022)](/sources/liang-2022.md) — §4, §4.9, Fig. 21.
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §5.6, §5.9, Figs. 12–17, 26 (preprint).
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — §8.9, Table 6.
- [Bezgin et al. (2023)](/sources/bezgin-2023.md) — §7.4, Eq. 49, Figs. 20–21 (arXiv v1).
- [Tang (2024)](/sources/tang-2024.md) — §4.4.3, Eq. (35), Fig. 12.
- [Ji, Liang & Fu (2023)](/sources/ji-2023.md) — §4.3, Eqs. (39)–(40), Figs. 3–6; §4.9, Eq. (45), Fig. 21.
- [Gaburro et al. (2024)](/sources/gaburro-2024.md) — §5.1.4, Fig. 3 (arXiv v1).
- [Jiang et al. (2024)](/sources/jiang-2024.md) — §4.2.2, Fig. 5.
- [Chu et al. (2025a)](/sources/chu-2025.md) — §2.2, §4.2, Example 5, Remark 4.1, Figs. 4.7–4.8 (arXiv v1).
- [Chu et al. (2025b)](/sources/chu-2025-b.md) — Example 5 (cross-reference).
- [Chu et al. (2025c)](/sources/chu-2025-c.md) — §3, Examples 4–5, Figs. 3.4–3.5 (arXiv v1).
- [Zampa & Dumbser (2025)](/sources/zampa-2025.md) — §3.2.2, §4.3, Figs. 3–4 (arXiv v1).
- [de Romémont et al. (2026)](/sources/deromemont-2026.md) — §6.3, Fig. 14.
- [Liang et al. (2025)](/sources/liang-2025.md) — §4.7, Figs. 19–20.
- [Stone et al. (2026)](/sources/stone-2026.md) — §3.1, §3.5, Figs. 2, 10 (cross-reference).

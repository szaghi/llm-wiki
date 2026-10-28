---
type: Benchmark
title: "Gaussian (Boeing) bump"
description: "The Boeing Gaussian speed bump, a smooth-body separation behind a Gaussian hill at bump-width Reynolds number 2 million (spanwise-periodic) or 3.41 million (3D): wall-modelled LES on it depends more on the subgrid model, the mesh and cell anisotropy than on the wall condition, and its separation converges non-monotonically."
status: established
aliases: [Gaussian bump, Boeing bump, Boeing Gaussian bump, Boeing speed bump, Gaussian speed bump, spanwise-periodic Gaussian bump, 2D Gaussian bump, 3D Gaussian bump]
tags: [benchmark, wmles, sgs-model, separated-flow, boundary-layer]
timestamp: 2026-10-28T11:49:00Z
---

# Gaussian (Boeing) bump

A turbulent boundary layer passes over a smooth hill of Gaussian profile,
proposed by Boeing Research & Technology to mimic the smooth junctions of
an aircraft wing and fuselage; it accelerates over the windward side and
separates without a geometric edge on the leeward side, so the separation
point is set by the turbulence and its modelling, not by the geometry
([Zhou & Bae (2024)](/sources/zhou-2024-b.md), §1). On this page $L$ is the
bump width (the reference length; page-local, not the registry's integral
scale), $h_0$ the bump height, $x_0$ the Gaussian length, $x$ measured from
the peak, $Re_L=U_\infty L/\nu$, and $L_s$ the horizontal length of the mean
separation bubble (page-local). In this bundle the case is a test of
[wall-modelled LES](/methods/wall-modelled-les.md) of smooth-body
separation: of the [subgrid-scale model](/definitions/large-eddy-simulation.md),
the mesh and its anisotropy, and the wall boundary condition, and of
monotonic grid convergence.

## Geometry and configurations

Two forms are run, with $h_0=0.085L$ and $x_0=0.195L$ in both.

- **Spanwise-periodic ("2D") bump**, height $h_0e^{-(x/x_0)^2}$, at
  $Re_L=2\times10^6$ ([Agrawal et al. (2022)](/sources/agrawal-2022.md),
  §VIII; [Zhou & Bae (2024)](/sources/zhou-2024-b.md), §2.2).
- **Three-dimensional bump**, tapered across the span,
  $h(x,z)=\tfrac{h_0}{2}e^{-(x/x_0)^2}\{1+\mathrm{erf}([L/2-2z_0-|z|]/z_0)\}$
  with $z_0$ a spanwise taper length (page-local), at
  $Re_L=3.41\times10^6$ ([Agrawal et al. (2022)](/sources/agrawal-2022.md),
  §VIII, Eq. 16).

| Item | [Agrawal et al. (2022)](/sources/agrawal-2022.md), §VIII | [Zhou & Bae (2024)](/sources/zhou-2024-b.md), §2 |
|---|---|---|
| Form | spanwise-periodic and 3D | spanwise-periodic |
| Solver | [CharLES](/software/charles.md), compressible, Voronoi grids | incompressible, energy-conserving second-order unstructured finite volumes (You, Ham & Moin), fractional step, CFL 1.0 |
| Wall treatment | algebraic equilibrium wall-stress model with a $C^1$-continuous assumed profile, matched at the first off-wall point | the exact mean wall stress of the reference imposed (three idealized conditions, below) |
| SGS models | [dynamic tensor-coefficient Smagorinsky](/methods/dynamic-tensor-coefficient-smagorinsky-model.md), dynamic Smagorinsky, [Vreman](/methods/vreman-model.md) | Vreman ($c=0.025$ and 0.07), dynamic Smagorinsky, [AMD](/methods/anisotropic-minimum-dissipation-model.md) (constant 0.3), [mixed similarity](/methods/scale-similarity-model.md) ($C_s=0.13$), none |
| Grids | periodic: 3, 12, 52 M cells; 3D: 29, 117, 452 M cells | four isotropic meshes, $\Delta_c/L=1.90\times10^{-3}$ to $2.38\times10^{-4}$ (1.94 M to 993 M cells); three anisotropic meshes $4:1:2$ at the same cell volume |
| Domain | periodic: $-1.0<x/L<2.5$, top at $y/L=1.0$, span $0.08L$; 3D: $-1.0<x/L<1.5$, inviscid side walls at $z/L=\pm0.5$, top wall at $y/L=0.5$ | $2L$ long ($0.85L$ upstream and $1.15L$ downstream of the peak), $L$ high, span $0.08L$ |
| Inflow | periodic: RANS mean profile at $x/L=-1.0$; 3D: plug flow | Lund rescale–recycle precursor LES, $Re_\tau\approx620$, $Re_\theta\approx1074$, $\delta_{\mathrm{in}}/L=0.0061$ |
| Statistics | temporal averaging of the dynamic coefficients; minimum spacings $\Delta/L=1.3\times10^{-3}$, $6.3\times10^{-4}$, $3.1\times10^{-4}$ on the three grids (Tables II–III) | 2 flow-throughs of transient, 3 of statistics |
| Reference | periodic: quasi-DNS of Uzun & Malik; 3D: surface pressure of Williams et al., skin friction of Gray et al., oil flow | the hybrid DNS–wall-resolved LES of Uzun & Malik ("DNS"), $L_s/L=0.32$, cell size about $1.10\times10^{-4}L$ at the thickest bubble |

Zhou & Bae use the cube root of the cell volume, $\Delta_c$, as the mesh
label; the boundary layer at $x/L=-0.65$ is covered by about 5, 9, 18 and
36 cells on their four isotropic meshes, the fine mesh having 10 to 30
wall units in the attached regions, comparable to a wall-resolved mesh in
the streamwise and spanwise directions but an order of magnitude coarser
in the wall-normal one (§2.2.3, Table 1). The precursor's log law is checked
on the [law of the wall](/definitions/law-of-the-wall.md) page, its method on
[inflow turbulence generation](/methods/inflow-turbulence-generation.md).

## What the case tests

**The subgrid model decides the bubble.** To remove the wall-stress
modelling error, [Zhou & Bae (2024)](/sources/zhou-2024-b.md), §2.2,
replace the no-slip wall by conditions that all impose the reference mean
wall stress $\tau^{\mathrm{ref}}_w$ (page-local): a velocity Neumann
condition $\partial u/\partial y|_w=\tau^{\mathrm{ref}}_w/\mu$ (Eq. 2); an
"equilibrium" Dirichlet condition with a wall eddy viscosity
$\nu_{t,w}$ (page-local) calibrated by a running average so that
$\rho(\nu+\nu_{t,w})\breve u_{\mathrm c}/h_{\mathrm{wm}}=\tau^{\mathrm{ref}}_w$ at the first cell centre $h_{\mathrm{wm}}$ ($\breve u_{\mathrm c}$ the running time average of the first-cell-centre velocity, as on the [equilibrium wall model](/methods/equilibrium-wall-model.md) page) (Eqs. 4–7); and a
"non-equilibrium" form that adds $\tfrac{h_{\mathrm{wm}}}{2}\partial p/\partial x$
to the stress (Eqs. 8–9), $\nu_{t,w}$ clipped at zero (see
[equilibrium wall model](/methods/equilibrium-wall-model.md) and
[non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)). With
the Neumann condition the bubble is measured from the sign of the mean
velocity at the first cell centre. On the baseline mesh
($\Delta_c/L=4.76\times10^{-4}$, 124 M cells) only AMD, Vreman $c=0.025$
and the mixed-similarity model separate; the Vreman $c=0.025$ bubble is
"similar to the DNS", the mixed-similarity one "significantly larger",
while no model, dynamic Smagorinsky and Vreman $c=0.07$ stay attached
(§3.1, Fig. 4). The mean eddy viscosity in the boundary layer is of the
order of the molecular one, largest for AMD and smallest for Vreman
$c=0.025$; the subgrid dissipation $\Pi=-\tau_{ij}\bar S_{ij}$ rises
strongly on the leeward side and is highest for the mixed-similarity model
(Figs. 5, 10). The first-cell velocity differs between subgrid models over
the whole bump, not only in the bubble, so "the performance of wall models
can be sensitive to the choice of the SGS model" (Fig. 7). Dynamic
Smagorinsky's subgrid activity drops in the wall-adjacent cells, which
raises the first-cell mean velocity (§3.1, Fig. 11; the activity
parameter is on [large-eddy simulation](/definitions/large-eddy-simulation.md)).

**The wall condition matters less.** With the two eddy-viscosity
conditions the subgrid model and the mesh still largely set $L_s$; the
non-equilibrium condition "notably improves" the bubble as measured by
$C_f$ for the eddy-viscosity models but changes the velocity-based length
little, and the boundary condition has "a negligible impact on the
convergence behavior". The authors conclude that the wall condition "can
enhance the prediction of flow separation" but "has a less dominant effect
on the simulation compared to the SGS model", its influence being "mainly
limited to the skin friction on the wall" (§3.2, Figs. 13–16, §4). Clipping
of $\nu_{t,w}$ occurs only for $0<x/L<0.7$, below 13% of the time on
average (§3.2). The same diagnosis, from the wall-model side, is on the
[building-block-flow wall model](/methods/building-block-flow-wall-model.md)
page.

**Non-monotonic grid convergence.** Both sources find the separation
moving non-monotonically under refinement, for different models:

- [Agrawal et al. (2022)](/sources/agrawal-2022.md), §VIII.A, Figs. 13–14:
  on the periodic bump dynamic Smagorinsky and Vreman separate on the
  coarse grid, lose the separation on the medium one and recover it on the
  fine one, while the tensor-coefficient model converges monotonically
  toward the reference $C_f$ and on the fine grid recovers the
  favourable-pressure-gradient $C_f$ peak that dynamic Smagorinsky
  under-predicts; both dynamic models give the reference bubble extent on
  the fine grid, Vreman a smaller one.
- [Zhou & Bae (2024)](/sources/zhou-2024-b.md), §3.1, Fig. 8: $L_s$
  converges to the reference 0.32 monotonically only with Vreman
  $c=0.025$; with AMD and Vreman $c=0.07$ the convergence is non-monotonic,
  "leading to a spurious diminishment or shrinking of the separation
  bubble upon mesh refinement", which they say agrees with Whitmore et al.
  and Agrawal et al. and ties to the subgrid model. The mixed-similarity
  model over-predicts the bubble but gives consistent sizes across meshes,
  which the authors read as a possible benefit of its anisotropic stress.
  Without a model the result improves markedly on the fine mesh, where the
  separated boundary layer has over 150 cells, close to wall-resolved
  resolution.

[Goc et al. (2021)](/sources/goc-2021.md), §3.3, cite a collapse of the
separation bubble under refinement reported by Iyer & Malik for a Gaussian
bump, beside the collapse of a flap bubble on their finest high-lift grid,
and leave cause and remedy open; [Hu et al. (2024)](/sources/hu-2024.md),
§1, cite Iyer & Malik's grids of 3.4 M, 16 M and 25 M cells, with a small
effect of resolution on $C_p$, a visible one on $C_f$, the coarse grid far
from the DNS and convergence on the medium and fine ones (see
[grid-point requirements](/results/les-grid-point-requirements.md)).

**Dynamic Smagorinsky: separation or none.**
[Agrawal et al. (2022)](/sources/agrawal-2022.md) report a separating
dynamic Smagorinsky model on their coarse and fine periodic grids, while
[Zhou & Bae (2024)](/sources/zhou-2024-b.md), §3.1, find no separation with
it on any of their four isotropic meshes. Zhou & Bae restrict their result
to their solver and set-up, cite Iyer & Malik as also finding none, and
name clipping, filtering, mesh topology and numerics as possible causes;
the set-ups differ in the equations (compressible against incompressible),
the grids (Voronoi against hybrid structured–unstructured) and the wall
treatment (an equilibrium wall model against the imposed reference
stress). The detail is on the
[dynamic procedure](/methods/dynamic-procedure.md) page. Zhou & Bae add that
the correct near-wall asymptotics of dynamic Smagorinsky in wall-resolved
LES without damping is not shown to carry over to coarse WMLES, "an open
question" (§3.1, §4).

**Mesh anisotropy.** On meshes with cells $4:1:2$
(streamwise : wall-normal : spanwise) at the same cell volume, the bubble
prediction degrades, most for Vreman $c=0.025$; the mixed-similarity model
loses its consistency across meshes; AMD's $C_p$ and first-cell velocity
are barely affected, and the separated layer at $x/L=0.2$ becomes attached
or nearly so for the other models ([Zhou & Bae (2024)](/sources/zhou-2024-b.md),
§3.3, Figs. 17–20). The authors attribute this, without isolating it by a
test, to the filter width taken as the cube root of the cell volume by all
models except AMD, which is "specifically designed for anisotropic
meshes". Their recommendation: Vreman $c=0.025$ is "comparatively robust"
on isotropic meshes, but users "should be cautious" with anisotropic ones
(§4).

**The three-dimensional bump.** On the 3D bump
[Agrawal et al. (2022)](/sources/agrawal-2022.md), §VIII.B, Figs. 15–19,
find dynamic Smagorinsky separating on the coarse grid, both dynamic models
losing the separation on the medium grid and both separating on the fine
grid (first cell at $y^+\sim30$ upstream), with a bubble of the size
measured by Gray et al.; the tensor-coefficient model is monotonic in $C_f$
and $C_p$ and gives the best fine-grid $C_p$. Both dynamic models capture
the small $C_p$ rise at the apex and the counter-rotating vortex pair of
the oil flow, which the Vreman model misses even on the finest grid, in agreement, as they cite it, with Iyer & Malik, who found no separation with Vreman up to 450 M cells. The
suction peak is mainly inviscid, since a free-slip run (not shown) also
predicts it (see [wall-modelled LES](/methods/wall-modelled-les.md)).
DTCSM costs 15 against 13 GPU-node-hours per flow-through for dynamic
Smagorinsky on the 52 M-cell periodic grid, 112 against 100 on the 452
M-cell 3D grid (§IX, Tables IV–V).

**A reference for aircraft-scale WMLES.**
[Kiris et al. (2023)](/sources/kiris-2023.md), §I, §VI 1f, list the bump,
with the [NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md),
among the academic WMLES of nonequilibrium boundary layers whose grid
spacing per unit span is much finer than in full-airframe WMLES, and call
for continued research on both because no high-lift submission they
reviewed resolved smooth-body separation on the flaps (see
[NASA CRM high-lift](/benchmarks/nasa-crm-high-lift.md)).
[Zhou & Bae (2024)](/sources/zhou-2024-b.md), §4, call for subgrid models
robust for separation, monotonic convergence and anisotropic meshes,
naming the tensor-coefficient model, the dynamic nonlinear model of Uzun &
Malik, and unified subgrid and wall models such as the building-block flow
model.

## Qualifications

- The reference of both sources for the periodic bump is the simulation
  of Uzun & Malik, a hybrid DNS–wall-resolved LES that Zhou & Bae call
  "DNS" throughout and Agrawal et al. a quasi-DNS; experiments are cited
  but not used for the periodic form.
- Zhou & Bae impose the reference mean wall stress, so their bubbles
  measure the subgrid model and mesh with an exact mean wall model, not a
  predictive WMLES; with the Neumann condition the separation cannot be
  read from $C_f$. Their solver is unnamed (You, Ham & Moin's code);
  Agrawal et al. run CharLES. Results of the two are not on the same
  grids or wall treatment and are not compared quantitatively by either.
- Zhou & Bae's inflow layer, $\delta_{\mathrm{in}}/L=0.0061$, is "approximately 10% larger" than in the DNS of Uzun & Malik, with $Re_\theta\approx1074$ against about 1035, as they print, and an
  AMD-generated inflow changes the bump profiles negligibly (§2.3, App. A,
  Fig. A.21).
- The two works that cite Iyer & Malik describe its outcome differently:
  [Goc et al. (2021)](/sources/goc-2021.md) as a collapse of the bubble
  under refinement, [Hu et al. (2024)](/sources/hu-2024.md) as convergence
  on the medium and fine grids after a deviating coarse grid; the cited
  work is not ingested, and the two descriptions are recorded side by
  side.
- Agrawal et al. were read in an accepted manuscript; their §VIII.B says
  the DTCSM $C_f$ trough "moves towards DNS" under refinement, while the 3D
  reference they list is the experiment of Gray et al.

# Citations

- [Zhou & Bae (2024)](/sources/zhou-2024-b.md) — §1; §2.1–2.3, Eqs. 1–9, Tables 1–2, Figs. 1–3; §3.1–3.3, Figs. 4–20; §4; App. A, Fig. A.21.
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — accepted manuscript: §VIII.A–B, Eq. 16, Figs. 13–19; §IX, Tables IV–V.
- [Goc et al. (2021)](/sources/goc-2021.md) — §3.3 (cited bubble collapse of Iyer & Malik).
- [Hu et al. (2024)](/sources/hu-2024.md) — §1 (cited grid study of Iyer & Malik).
- [Kiris et al. (2023)](/sources/kiris-2023.md) — §I; §VI 1f (cited as an academic WMLES case; not run).

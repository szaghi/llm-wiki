---
type: Benchmark
title: "Shock–cylinder interaction"
description: "A shock wave meeting a circular cylinder on an overlapping grid, with the shock crossing the interpolation boundary: a Mach 1.5 shock driving a free rigid cylinder with self-convergence, AMR equivalence and cost data, detonations around moving cylinders, and the Mach 3 bow shock with drag, stand-off distance and patch-refinement gains."
status: established
aliases: [shock-driven cylinder, shock diffraction by a cylinder, supersonic flow past a cylinder, bow shock stand-off, detonation–cylinder interaction]
tags: [benchmark, shock-capturing, compressible, moving-grid, amr]
timestamp: 2026-11-02T14:54:00Z
---

# Shock–cylinder interaction

A planar shock that reaches a circular cylinder, or a supersonic stream that
forms a bow shock in front of one, tests whether discontinuities cross
the interpolation boundary of an overlapping grid cleanly; Henshaw &
Schwendeman (2006), Picard et al. (2021), Wang (1995) and Chesshire &
Henshaw (1990) all use it. Each of them uses the grid of
[flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md):
a body-fitted annular grid around the cylinder over a Cartesian
background, so that the incident shock passes from the background into the
annulus, and the reflected and bow shocks lie across the overlap. The
inter-grid transfer of the cases below (not of Wang's, listed at the end) is
non-conservative; how
this is judged is on
[shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md)
and [conservative overset interface](/methods/conservative-overset-interface.md).

## Cases

**Mach 1.5 shock driving a free rigid cylinder (Henshaw & Schwendeman 2006,
§6.3.2, Figs. 16–19, Tables 5–6).** [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md):
- *Setup.* Inviscid Euler equations; a cylinder of radius $1/2$ and mass
  $1/2$ at $(-1/2,0)$ in $[-2,2]^2$, free to move under the pressure force
  (Newton–Euler equations); a Mach 1.5 shock starting at $x=-1.5$ into gas
  with $\rho=\gamma=1.4$, $p=1$ (so $a=1$); post-shock state
  $\rho=2.6069$, $u=0.6944$, $v=0$, $p=2.4583$, which are the normal-shock
  values for Mach 1.5 *(compiler check, not in the sources)*. Inflow at
  $x=-2$, zero normal derivative at $x=2$, slip walls at $y=\pm2$ and on
  the cylinder.
- *Grids.* An annulus moving with the body (6 radial intervals) over a
  fixed Cartesian grid with $40j\times40j$ intervals, spacing $h_j=1/(10j)$;
  adaptive refinement by a factor 4 per level on every component grid,
  annulus included. The finest uniform grid, $j=32$, has about
  $1.56\times10^6$ points, 8200 of them on the annulus. Second-order
  slope-limited Godunov scheme with a Roe solver, one global time step at
  CFL factor 0.9.
- *Self-convergence at $t=1$, 1-norm, $j=8,16,32$:* $\rho$ 6.1e-3, 2.2e-3,
  7.8e-4 (rate 1.49); $u$ 2.5e-3, 9.2e-4, 3.3e-4 (1.47); $v$ 1.3e-3,
  4.5e-4, 1.6e-4 (1.48); $T$ 1.1e-3, 4.1e-4, 1.5e-4 (1.47). For the
  non-smooth pressure-driven piston the same paper measures 1-norm rates
  1.32–1.34 and finds them consistent with linear-advection theory for
  non-smooth solutions (§6.2.2).
- *AMR.* Runs with equal effective resolution, one base grid $j=32$
  without refinement, $j=8$ with one level, $j=2$ with two levels, give
  cylinder position, velocity and force curves "in excellent agreement"
  (Fig. 18).
- *Cost per step* (2.2 GHz Xeon, 2 GB): 17.8 s without AMR ($j=32$), of
  which 91.6% is the flux update and 3.7% the grid-connectivity update;
  3.81 s with one AMR level ($j=8$), of which 63.7% update, 14.5%
  interpolation, 5.5% regridding, 4.3% connectivity update; AMR overhead
  "about 20%" (Table 6).
- See [AMR on overlapping grids](/methods/amr-on-overset-grids.md) and
  [moving overset grids](/methods/moving-overset-grid.md).

**Detonations around cylinders (Henshaw & Schwendeman 2006, §7, Figs.
20–23).** Reactive Euler equations with one-step Arrhenius kinetics (heat
release 4, reciprocal activation energy 0.075):
- A cylinder of radius 0.15 and mass 1, impulsively given unit speed and
  then free, compresses unburnt gas ($\rho=1$, $T=0.93$) until a detonation
  forms. The shock position on the symmetry line converges with
  resolution, the von Neumann pressure peak is not converged on the finest
  grid, and the cylinder position, velocity and force converge well
  (Fig. 21).
- A Chapman–Jouguet detonation (speed about 3.1816) runs through 26 free
  cylinders of unit density in $[-1/2,4]\times[-1,1]$; a local detonation
  forms in front of each impacted cylinder and speeds the overall front
  beyond the steady CJ value. With one refinement level the number of
  component grids varies from 28 to about 400 during the run; the base
  background grid has $721\times321$ points. Qualitative comparison of a
  coarse and a refined run at $t=0.7$.

**Mach 3 flow past a fixed cylinder (Picard et al. 2021, §4.3, Figs.
12–19, Tables 5–7).** [Picard et al. (2021)](/sources/picard-2021.md), a
cell-centred second-order MUSCL–Hancock/HLLC finite-volume scheme in which
receptor ("ghost") cells, two layers on each grid, receive volume-weighted
reconstructions from the cells they intersect; no hole is cut:
- *Setup.* Air, $\gamma=1.4$; $M_\infty=3$, $p_\infty=96774$ Pa,
  $\rho_\infty=0.519$ kg/m$^3$; a shock initially 8 cylinder diameters
  upstream, travelling toward the body; domain $[-10,10]^2$ m; CFL 0.4;
  run to a non-dimensional time 52.5. Single-grid reference: a body-fitted
  O-grid joined to an H-grid. Overset: an O-grid patch around the cylinder
  over a Cartesian substrate that does not contain the cylinder.
- *Crossing.* The moving shock crosses the substrate-to-patch boundary with
  no visible spurious reflection (Fig. 14).
- *Drag, equal resolution* (time average over $t\in[40,52.5]$, Table 5):
  single grid 207328, 203606, 201774, 203000 N against overset 210871,
  206604, 202320, 202164 N for 50, 100, 200, 400 cells along the
  perimeter; the force converges toward about $202\times10^3$ N.
- *Refined patch on a coarse substrate* (substrate 100 cells, cell-size
  ratio $\kappa_h=1,2,4$ of substrate to patch, Picard et al.'s $\chi$; Table 6): drag differs from the equivalent fine
  single mesh by 1.47%, 0.27%, 0.5%; the single mesh costs 0.97, 2.3 and
  3.5 times the CPU time and 0.97, 2.41 and 3.8 times the memory of the
  overset run. Hardware and absolute times are not given.
- *Bow-shock stand-off* (Table 7), against the value $0.3649D$ of Sinclair
  & Cui: $0.433$, $0.428$, $0.398$, $0.372$ (in units of $D$) for 50–400
  perimeter cells; with substrate 100 and $\kappa_h=1,2,4$: $0.428$,
  $0.395$, $0.372$ (1.95% error), i.e. the refined patch reaches the
  stand-off of the uniformly refined grids.

## Related cases on other pages

[Wang (1995)](/sources/wang-1995.md) diffracts a Mach 1.5 shock by a fixed
cylinder with a fully conservative interface (qualitative agreement with a
shadowgraph), and [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md)
impulsively start a cylinder at Mach 2 in viscous flow, the bow shock
crossing the interpolation boundary nearly parallel to it; both are on
[flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md).
Picard et al. (2021) also run a shock–helium-bubble interaction and the
double Mach reflection with the patch boundary crossed by discontinuities;
these are on
[shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md).

## What the cases measure

| Source | Body | Measured | Reference |
|---|---|---|---|
| Henshaw & Schwendeman (2006) | free, shock-driven | 1-norm self-convergence ≈1.5; AMR equivalence; cost | self-convergence |
| Henshaw & Schwendeman (2006) | moving, detonation | convergence of shock position and body motion | grid refinement |
| Picard et al. (2021) | fixed, Mach 3 | drag, stand-off, cost gains of a refined patch | single grid; analytic stand-off |

## Qualifications

- Henshaw & Schwendeman caption Fig. 19 "at $t=1$" while the text shows
  the refined grids "at time $t=1.5$", the last frame of Fig. 16; they
  caption Fig. 20 with $t=0.035$ where the text and panel labels give
  $t=0.35$.
- For the impulsively moved cylinder (§7.1), Henshaw & Schwendeman state a
  representative spacing $h_j=2/(5j)$, while their Cartesian and radial
  grid definitions give $0.04/j$ and only the printed circumferential count
  gives $2/(5j)$, a factor 10 apart *(compiler check, not in the sources)*;
  which number is the slip is not decidable from the paper.
- Picard et al. call $D=1$ m the cylinder's "radius" while normalizing the
  stand-off by $D$ and placing the shock "8 cylinder diameters" upstream;
  they give the travelling shock a Mach number "equal to $M_{sh}=1$", which
  would be a null shock, and do not define the length scale of their
  non-dimensional time for this case. The case data above are recorded as
  printed.
- Picard et al. print a drag difference of 0.47% for 400 perimeter cells,
  while their own forces give $\lvert202164-203000\rvert/203000=0.41\%$; the
  other three rows agree with the printed forces *(compiler check, not in
  the sources)*.
- Picard et al. state the method is not globally conservative (it
  interpolates conserved variables, not fluxes); their conservation error
  measurements are on the shock-capturing page.

# Citations

- [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) — §4.2 (scheme, global time step); §6.3.2, Figs. 16–19, Tables 5–6 (shock-driven cylinder, self-convergence, AMR equivalence, cost); §6.2.2, Table 3 (1-norm rates for the non-smooth pressure-driven piston); §7.1–7.2, Eq. (24), Figs. 20–23 (detonation by an impulsively moved cylinder; CJ detonation through 26 cylinders).
- [Picard et al. (2021)](/sources/picard-2021.md) — §3.2 (ghost-cell exchange, two layers, no hole cutting, non-conservation); §4.3, Figs. 12–19, Tables 5–7 (Mach 3 cylinder: drag, cost ratios, stand-off).
- [Wang (1995)](/sources/wang-1995.md) — §5.4, Figs. 18–20 (shock diffraction, cross-reference).
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §6.4 Test 2 (Mach 2 impulsive start, cross-reference).

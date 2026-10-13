---
type: Benchmark
title: "Shock reflection from a cylinder"
description: "A planar shock (Mach 1.34 to 2.84, and relativistic variants at Mach 1.2 to 1.7) hits a circular cylinder: regular reflection turns into Mach reflection with triple points and slip lines, and the Mach stems collide behind the body; compared with the Bryson–Gross schlieren and triple-point loci, it is run on body-fitted grids and on Cartesian grids that do not fit the body, where it tests cut-cell small-cell stabilization, AMR interfaces crossing the body, and moving embedded boundaries."
status: established
aliases: [shock diffraction by a cylinder, Bryson–Gross cylinder, shock–cylinder interaction]
tags: [benchmark, euler, embedded-boundary, mach-reflection]
timestamp: 2026-10-13T00:00:00Z
---

# Shock reflection from a cylinder

**Set-up.** A planar shock moving into gas at rest strikes a circular
cylinder. The incident shock first reflects regularly; between 40° and
50° from the forward stagnation point the reflection turns into Mach
reflection, with Mach stems on the cylinder, triple points and slip
lines, and the Mach shocks meet behind the body and reflect from the
symmetry plane, again regularly first. The reference is the schlieren
series of Bryson and Gross (1961). In the embedded-boundary variants
the body is not grid-fitted; the body-fitted variant below runs it on an
O-grid (both lines corrected at the 2026-10-13 deep lint, from the
batch-12 reading of the original). It is distinct from the steady [supersonic cylinder flow](/benchmarks/supersonic-cylinder-flow.md)
and from the free body of [shock-driven cylinder lift-off](/benchmarks/shock-cylinder-lift-off.md).

**Variants.**
* *Mach 2, stationary cylinder.* Radius 0.15 centred at $(0.5, 0.5)$ in
  $[0, 1.00001]\times[0, 1]$, shock at $x = 0.2$, $302\times302$ cells, run
  to $t = 0.25$. Of 416 cut cells, 160 are below half a cell and the
  smallest volume fraction is $1.17\times10^{-4}$. Second-order MUSCL
  (CFL 0.85) and method of lines (CFL 1), both with a local Lax–Friedrichs
  flux and [state redistribution](/methods/state-redistribution.md), run
  robustly; MUSCL is better in the subsonic region ahead of the body, the
  method of lines smoother along the wall, and both place the wall shocks
  alike ([Berger & Giuliani (2021)](/sources/berger-2021.md), §5.2,
  Figs. 10–11).
* *Mach 2.81, AMR crossing the body.* $[0, 1]^2$, cylinder centred at
  $(0.5, 0.5)$ (radius not printed), shock at $x = 0.2$, upstream density
  1, outflow in $x$ and walls in $y$, base grid $256^2$ with two levels.
  Refining only the upper half of the cylinder, so that coarse–fine
  boundaries cross cut cells, gives the same solution in the refined
  region as refining all of it, with re-redistribution; the reflected
  shock, primary Mach stem, contact and triple point match Bryson and
  Gross at $t = 0.068$ and $0.088$ ([Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md),
  §4.3, Figs. 5–7). The upstream pressure is printed ambiguously.
* *Moving cylinder.* A cylinder of diameter 0.04 m moves at the
  pre-shock flow speed into a stationary shock of Mach 1.34 or 2.82, with
  [moving cut cells](/methods/cut-cell-finite-volume.md) and four AMR
  levels (114 points per diameter); before the shock arrives no waves
  appear, and the Mach 2.82 run reproduces the Bryson–Gross features
  qualitatively ([Natarajan et al. (2022)](/sources/natarajan-2022.md),
  §3.3, Fig. 6). Its printed post-shock density does not match its stated
  density ratio.

All simulation comparisons are qualitative: no error norms are reported,
and no run scores itself against the experiment's triple-point loci
(corrected at the 2026-10-13 deep lint, see below).

**Later uses (batch 12).** *The original experiment.*
[Bryson & Gross (1961)](/sources/bryson-1961.md) (§2, plates 2–4,
fig. 6) is the reference named above. A cylinder of $D = \tfrac12$ in. in
air in a 4 in. × 12 in. shock tube, mean $M_s = 2.82$ (plates at 2.81,
2.82 and 2.84), photographed by schlieren over about 7 diameters of
incident-shock travel, in two series a factor 10 apart in $\mathrm{Re}$
($7.79\times10^4$ and $0.78\times10^4$, the latter printed $0.87\times10^4$
in the fig. 6 caption). It corrected or qualified three lines of this
page, quoted below in their earlier wording; the lines themselves were
corrected in place at the 2026-10-13 deep lint.
* *Set-up wording.* The line "The incident shock reflects into a detached
  bow shock, Mach stems form on the cylinder" compresses the sequence. The
  reflection is [regular](/definitions/mach-reflection.md) at first and
  becomes Mach reflection between 40° and 50° from the forward stagnation
  point; the wave the plates label is the reflected shock. The Mach shocks
  that meet behind the body reflect from the symmetry plane, again regular
  first, with Mach reflection beginning 0.5 to 1.0 diameters behind the
  cylinder, so each side carries two triple-point loci (p. 4).
* *"The body is not grid-fitted."* This holds for the embedded-boundary
  uses above, not for the benchmark itself: the body-fitted variant below
  runs it on an O-grid.
* *"All comparisons are qualitative."* This holds for the simulations. The
  experiment gives quantitative data: the triple-point loci of both
  reflections in $(x/D, y/D)$ out to $x/D \approx 7$ and the slip-line
  vortex locus (fig. 6), the two transition locations, and the finding
  that a factor 10 in $\mathrm{Re}$ leaves the loci unchanged. No
  simulation on this page has scored itself against these loci.

Two further cautions for a comparison. The plates carry no times, so the
times $t = 0.068$ and $0.088$ of the AMR variant are simulation times; a
run is matched to a plate by the position of the incident shock. And the
experiment is viscous: boundary-layer separation on the aft sides, the
wake interacting with the reflected shock, and a vortex into which the
slip surface rolls up, formed by the boundary layer meeting the shock when
the Mach shock first appears, are features an Euler run should not be
expected to reproduce. Whitham's shock-dynamics theory, extended in the
paper to blunt bodies, predicts both triple-point loci in "good"
agreement. A 1 in. sphere run in the same tube is the experimental
reference of the [shock passing a sphere](/benchmarks/shock-sphere-interaction.md).

*Body-fitted and relativistic variants.*
[Tsai et al. (2012)](/sources/tsai-2012.md) (§V) run the cylinder on a
body-fitted O-grid of 721 rays by 201 circles (smallest radial spacing
0.01, diameter 1, outer boundary diameter 8) with a kinetic beam
flux-vector splitting of Steger–Warming form, a TVD/ENO flux correction
whose member is not stated, Strang splitting and Riemann-invariant wall
conditions. They cite the earlier non-relativistic body-fitted
computation of Yang, Liu and Lomax (1987) for validation.
* *Non-relativistic, $M_s = 2.81$.* The computed density at $t = 1.07$
  (time unit not defined) is overlaid on a Bryson–Gross schlieren
  photograph and called in "good agreement ... except for the viscous and
  thermal dissipative effects"; the comparison is visual.
* *Special-relativistic, $M_s = 1.2$, 1.5, 1.7.* $\gamma = 1.4$, upstream
  $p = \rho = 1$ at rest, shock speeds 0.669, 0.837, 0.948 of the speed of
  light. Printed post-shock $(p, \rho)$: (2.046, 1.657), (6.419, 3.450),
  (24.941, 7.219), with flow speeds 0.282, 0.653, 0.888. Run to $t = 4$;
  regular reflection turns into Mach reflection at $t = 0.5$–1.25 and the
  Mach stems collide behind the body at $t = 2.0$. At $M_s = 1.5$ the
  paper plots wall-pressure histories at 0°–180° and a triple-point
  trajectory close to a straight line; at $M_s = 1.7$ it prints the field
  extremes at $t = 4$ (density 59.15 and pressure 315.32 at the front
  stagnation point). No grid study or error norm. An axisymmetric sphere
  counterpart is run at the same $M_s$.

# Citations

1. [Berger & Giuliani (2021)](/sources/berger-2021.md), §5.2 (arXiv v1).
2. [Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §4.3 (arXiv v1).
3. [Natarajan et al. (2022)](/sources/natarajan-2022.md), §3.3 (arXiv v1).
4. [Bryson & Gross (1961)](/sources/bryson-1961.md), §2, plates 2–4, fig. 6.
5. [Tsai et al. (2012)](/sources/tsai-2012.md), §V.A, Figs. 1–8.

---
type: Benchmark
title: "Shock passing a sphere"
description: "A planar shock passes a fixed sphere: regular then Mach reflection on the front, Mach stems colliding behind, and a drag history with a large early peak and a negative phase; scored against the Bryson–Gross triple-point loci (M_s 2.85 and 4.41) and shock-tube drag and surface-pressure data at M_s 1.10–1.33, with Euler and relativistic runs on body-fitted grids."
status: established
aliases: [shock diffraction over a sphere, shock–sphere interaction, unsteady drag of a sphere behind a shock]
tags: [benchmark, euler, 3d, mach-reflection]
timestamp: 2026-10-13T00:00:00Z
---

# Shock passing a sphere

**Set-up.** A planar shock moving into gas at rest passes a fixed sphere
of diameter $D$. On the front the reflection is regular at first and
turns into [Mach reflection](/definitions/mach-reflection.md); the Mach
stems wrap round the body and collide behind it, where a second pair of
triple points forms. It is the axisymmetric counterpart of the
[shock reflection from a cylinder](/benchmarks/shock-reflection-from-cylinder.md),
and the two share their experimental origin. Two kinds of reference data
exist: the triple-point loci of strong shocks, and the drag and surface
pressure behind weak shocks in a shock tube. In a tube the walls reflect
the diffracted waves back onto the sphere, so the tube size is part of
the set-up.

**Experimental data.**
* *Triple-point loci, strong shocks.* Bryson and Gross photographed (by
  schlieren) a 1 in. sphere (a table-tennis ball filled with Wood's
  metal, hung on 8 nylon strings) in air in the Harvard 4 in. × 12 in.
  shock tube at $M_s = 2.85$ and 4.41, with Re about constant, over about
  3.5 diameters of shock travel. The pattern is like the cylinder's: two
  pairs of triple-point loci. A spherical shock, reflected from the point
  where the converging Mach shock collides at the rear stagnation point,
  crosses the second Mach shock. The measured loci at the two $M_s$
  coincide with each other and with Whitham's shock-dynamics prediction
  of the first triple point; the theory gives the same pattern for all
  $M_s \ge 3$ and does not predict the second triple point
  ([Bryson & Gross (1961)](/sources/bryson-1961.md), Figs. 7–9). The loci
  of Fig. 9 are plotted in diameters and can be digitized. No photograph
  carries a time, so a simulation must be matched by incident-shock
  position.
* *Drag histories, weak shocks.* In a 200 mm circular tube, a 40 mm
  sphere with an internal accelerometer gives $C_D$ against time for
  $M_s = 1.10$–$1.33$ in air ($\gamma = 1.4$, post-shock states printed in
  the source's Table 1). $C_D$ peaks near 0.5 diameters of shock travel,
  is negative from about 1.6 to 2.6, then settles to a small positive
  value. The peak falls from 14.48 at $M_s = 1.10$ to 4.52 at
  $M_s = 1.33$, against a steady value below 0.42. Two spheres side by
  side always peak higher than one, most when they touch
  ([Zhang et al. (2017)](/sources/zhang-2017-c.md), Figs. 9, 11–12). The
  peak's height and timing depend on the filtering and polynomial fit of
  the signal.
* *Surface pressure and drag of an 80 mm sphere at $M_s = 1.22$.* The
  data of Tanno et al. (2003, surface transducers every 15°) and Sun et
  al. (2005, drag) are not ingested; they enter this bundle only as
  digitized circles in [Martyushov, Igra & Elperin (2016)](/sources/martyushov-2016.md),
  Figs. 3–4.
* *Reflection transition.* Quoted from Tanno et al.: on the sphere the
  reflection turns from regular to Mach at a critical angle of about 33°
  (how it is measured is not stated) at $M_s = 1.22$, and a cylinder's
  drag maximum coincides with that transition. Zhang et al.'s own
  reading, drawn from the literature rather than measured, is that the
  transition has "very little influence" on the sphere's drag ([Zhang et al. (2017)](/sources/zhang-2017-c.md), §4.1).

**Simulations.**
* *Euler, fixed sphere, $M_s = 1.22$.* A dimensionally split Harten–Yee
  TVD scheme with face-frozen eigenvectors
  ([characteristic decomposition](/methods/characteristic-decomposition.md))
  on a two-block body-fitted elliptic grid, $D = 80$ mm, pre-shock
  101 kPa and 300 K. The surface pressure matches Tanno et al. at 140 and
  208 µs and is too low on the rear at 296 and 380 µs, which the authors
  attribute to the experiment's support strut. The drag history agrees
  with Sun et al., with peak $C_D = 7.55$ and $C_D = -0.16$ later (as printed; the figures
  disagree: Fig. 6's axis tops at 7.50 and Fig. 4 shows the late value
  near 0). Three
  grids (70×200, 120×300, 200×500) give overlapping drag peaks
  ([Martyushov, Igra & Elperin (2016)](/sources/martyushov-2016.md),
  §§3–4). No error norm is given, and the tube cross-section and the
  dimensionality (axisymmetric or 3D) are not stated.
* *Relativistic, axisymmetric.* A special-relativistic ideal gas
  ($\gamma = 1.4$, upstream $p = \rho = T = 1$, speed of light 1) at
  $M_s = 1.2$, 1.5 and 1.7, with a relativistic kinetic beam scheme on a
  body-fitted O-grid. The sequence is regular reflection, Mach reflection,
  Mach-stem collision behind the body and shock interaction in the wake.
  Against the cylinder at $M_s = 1.2$, the sphere has a weaker pressure
  behind the front shock and a smaller standoff distance; at
  $M_s = 1.7$ its flow is "more elongated and swept back"
  ([Tsai et al. (2012)](/sources/tsai-2012.md), §V.B). Output is
  qualitative (contour plots), with no grid study.

**Reading the drag data.** The two weak-shock data sets normalize time
differently: by the shock transit time across one diameter
([Zhang et al. (2017)](/sources/zhang-2017-c.md)), and by the radius over
293.4 m/s, the square root of the gas constant times the pre-shock
temperature ([Martyushov, Igra & Elperin (2016)](/sources/martyushov-2016.md)).
Their peak times cannot be compared without conversion. Both report a
negative drag phase, explained differently: by the diffracted waves
focusing at the rear stagnation point, with weak wall reflections, for a
40 mm sphere in a 200 mm tube (area ratio 25)
([Zhang et al. (2017)](/sources/zhang-2017-c.md), §4.1); and by
tube-wall reflections hitting the rear of a large (80 mm) sphere in a
small tube ([Martyushov, Igra & Elperin (2016)](/sources/martyushov-2016.md),
§3), whose computational cross-section is not printed. The set-ups
differ, so the two explanations are not incompatible claims about one
flow. Martyushov et al.'s printed peak
($C_D = 7.55$ at $M_s = 1.22$) and Zhang et al.'s range (14.48 to 4.52
over $M_s = 1.10$–$1.33$) concern different spheres and data reductions.

**Related set-ups.** A *free* sphere lifted from a wall by an $M_s = 3$ or
6 shock is the 3D variant of the
[shock-driven cylinder lift-off](/benchmarks/shock-cylinder-lift-off.md),
a different problem. Martyushov et al. state, but do not run, a
moving-grid formulation for a free sphere.

# Citations

1. [Bryson & Gross (1961)](/sources/bryson-1961.md), §2 (sphere), Figs. 7–9.
2. [Zhang et al. (2017)](/sources/zhang-2017-c.md), §§2–4.
3. [Martyushov, Igra & Elperin (2016)](/sources/martyushov-2016.md), §§2–4.
4. [Tsai et al. (2012)](/sources/tsai-2012.md), §V.B.

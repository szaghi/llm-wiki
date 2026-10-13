---
type: Definition
title: "Regular and Mach reflection"
description: "The two ways a shock reflects from a wall or a symmetry plane: regular reflection, with incident and reflected shocks meeting on the wall, and Mach reflection, where a Mach stem joins the wall to a triple point carrying a slip line; single and double triple points, the transition angle θ_tr, and the Mach stems that collide behind a body."
status: established
aliases: [regular reflection, Mach reflection, RR, MR, Mach stem, triple point, single triple point, double triple point, STP, DTP, transition angle]
tags: [mach-reflection, euler]
timestamp: 2026-10-13T00:00:00Z
---

# Regular and Mach reflection

When a shock meets a wall inclined to it, or a symmetry plane where two
shocks collide, it reflects in one of two ways. The distinction decides
what a computed pattern must contain, and its location is the most
quantitative datum the shock-reflection experiments offer a simulation.

**Regular reflection** (RR). The incident shock and the reflected shock
meet at a point on the wall.

**Mach reflection** (MR). The meeting point leaves the wall. Four
features then appear, with the labels of the Bryson–Gross plates: the
**incident shock**, the **reflected shock**, the **Mach stem** (Mach
shock), which joins the wall to the meeting point, and a **slip line**
(contact discontinuity) running from that point; the meeting point is
the **triple point**, and its path in time is the triple-point locus,
Whitham's "shock-shock"
([Bryson & Gross (1961)](/sources/bryson-1961.md), plates 1–6). A
single Mach reflection on the front face of a 25° wedge at $M_s = 1.7$
shows the same four features
([Yeom & Chang (2010)](/sources/yeom-2010.md), §4.1).

**Single and double triple point** (STP, DTP). A Mach reflection with one
triple point may develop a second triple point with its own Mach stem.
On the second of two concave arcs, at $M_s = 3.5$ and 4.5, the reflection
goes from regular to a single triple point and then to a double; at
$M_s = 4.5$ the two triple points later merge again, STP → DTP → STP
([Brahmi et al. (2020)](/sources/brahmi-2020.md), §4.1, Figs. 5–7; see
[shock reflection from double concave wedges](/benchmarks/double-concave-shock-reflection.md)).
The [double Mach reflection](/benchmarks/double-mach-reflection.md)
benchmark is named for a configuration with two Mach stems on a straight
wedge.
Toro's textbook lists four reflection types, regular, single Mach,
complex Mach and double Mach reflection, citing Ben-Dor and Glaz et al.,
and computes single Mach reflections on 25° and 30° wedges at
$M_s = 1.7$ and 1.2 against photographs
([Toro (1997)](/sources/toro-1997.md), §17.2).

**Transition angle** $\theta_{\mathrm{tr}}$. The wall angle
$\theta_{\mathrm w}$ at which regular reflection turns into Mach
reflection. On a curved wall the local inclination changes as the shock
advances, so one run passes through the transition:
* On a circular cylinder at $M_s = 2.82$ the reflection is regular at
  first, and Mach reflection begins between 40° and 50° of azimuth from
  the forward stagnation point
  ([Bryson & Gross (1961)](/sources/bryson-1961.md), p. 4).
* On a sphere, Zhang et al. quote from Tanno et al. a critical angle of
  about 33° at $M_s = 1.22$ (how the angle is measured is not stated) and
  that for a cylinder the drag peak coincides with the transition; their
  own reading, drawn from the literature, is that for a sphere the
  transition "has very little influence" on drag
  ([Zhang et al. (2017)](/sources/zhang-2017-c.md), §4.1; not measured
  there).
* On concave arcs the transition angle (its convention is not stated)
  rises with $M_s$ and is nearly
  the same on both arcs up to $M_s = 2.5$
  ([Brahmi et al. (2020)](/sources/brahmi-2020.md), Fig. 4). The computed
  value depends on the grid until the grid is fine enough: at
  $M_s = 1.6$ it grows from 9.6° to 12.7° over five grids and is
  independent of the grid from the fourth (Table 2).
* Whitham's shock-dynamics theory has no regular reflection: it predicts
  Mach reflection on cones for every $\theta_{\mathrm w}$ up to 90°, and
  the measured triple-point-locus angles lie below its curve, which
  Bryson and Gross attribute to that omission (fig. 2).
* A blast wave reflecting from a wall near the transition is photographed
  by [Kleine, Grönig & Takayama (2006)](/sources/kleine-2006.md) (Fig. 6, 120 µs), with no
  transition angle or height measured.

**Mach stems colliding behind a body.** Behind a cylinder or sphere the
two diffracted Mach shocks meet on the symmetry plane, which acts as a
wall: a second reflection forms, regular first and Mach reflection
beginning 0.5 to 1.0 diameters behind the cylinder, so each side carries
a second triple-point locus. On a sphere the converging Mach shock
collides at a point on the rear stagnation point, and the reflected
spherical shock passes through the second Mach shock
([Bryson & Gross (1961)](/sources/bryson-1961.md), p. 4, figs. 6, 8).
Relativistic computations show the same sequence, regular reflection,
transition, stem collision behind the body, then shock-on-shock
interaction in the wake
([Tsai et al. (2012)](/sources/tsai-2012.md), §V).

**For a simulation.**
* *Measuring a triple point.* Brahmi et al. trace triple points by
  accumulating, step after step, the larger of the current and previous
  pressure-gradient magnitude $\vert\nabla p\vert$, which draws the
  trajectories (§4.1, eq. 8).
* *Matching an experiment.* The Bryson–Gross photographs carry no times;
  a simulation matches a plate by incident-shock position, and the
  triple-point loci in $(x/D, y/D)$ are the scoreable data
  ([shock reflection from a cylinder](/benchmarks/shock-reflection-from-cylinder.md)).
* *Slip lines.* The slip line of a Mach reflection is physically unstable;
  in Euler runs its roll-up has no converged limit and measures the
  scheme's effective viscosity
  ([double Mach reflection](/benchmarks/double-mach-reflection.md),
  Titarev & Toro).
* *Spurious triple points.* A first-order low-dissipation Riemann solver
  can kink a Mach stem and create a triple point that is not physical
  ([numerical shock instability](/definitions/numerical-shock-instability.md)).
* *Naming.* "Diffraction" is used for both mechanisms: Bryson and Gross
  call the passage of a shock over cones, cylinders and spheres
  diffraction, and Yeom and Chang call reflection from a compression
  wedge diffraction. In this bundle,
  [shock diffraction](/benchmarks/shock-diffraction.md) is the expansion
  around a backward-facing corner.

**Benchmarks that exhibit it.**
[Double Mach reflection](/benchmarks/double-mach-reflection.md),
[shock reflection from a cylinder](/benchmarks/shock-reflection-from-cylinder.md),
[shock passing a sphere](/benchmarks/shock-sphere-interaction.md),
[shock reflection from double concave wedges](/benchmarks/double-concave-shock-reflection.md),
[Schardin's problem](/benchmarks/schardin-problem.md).

# Citations

1. [Bryson & Gross (1961)](/sources/bryson-1961.md), §2, plates 1–6, figs. 2, 6, 9.
2. [Tsai et al. (2012)](/sources/tsai-2012.md), §V.
3. [Brahmi et al. (2020)](/sources/brahmi-2020.md), §4.1, Table 2, Figs. 4–7.
4. [Yeom & Chang (2010)](/sources/yeom-2010.md), §4.1, Figs. 4–5.
5. [Zhang et al. (2017)](/sources/zhang-2017-c.md), §4.1.
6. [Kleine, Grönig & Takayama (2006)](/sources/kleine-2006.md), §3.2, Fig. 6.
7. [Toro (1997)](/sources/toro-1997.md), §17.2.

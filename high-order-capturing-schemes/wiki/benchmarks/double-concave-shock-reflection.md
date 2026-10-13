---
type: Benchmark
title: "Shock reflection from double concave wedges"
description: "A planar shock in air (M_s 1.6–4.5) runs over two concave circular arcs in series: regular-to-Mach transition angles on each arc, a single-to-double triple-point sequence on the second arc, an empirical time scaling of shock attenuation, circulation-rate plateaus and impulse attenuation; single-code viscous reference data with a grid study, no experiment."
status: established
aliases: [double-concave cylindrical wedges, double-concave cylindrical reflectors, shock diffraction over double concave cylindrical wedges]
tags: [benchmark, navier-stokes, 2d, mach-reflection, immersed-boundary]
timestamp: 2026-10-13T00:00:00Z
---

# Shock reflection from double concave wedges

**Provenance.** Both sources are one study by one group with one code:
Part I on shock dynamics ([Brahmi et al. (2020)](/sources/brahmi-2020.md))
and Part II on vorticity generation
([Brahmi et al. (2020b)](/sources/brahmi-2020-b.md)), the same
configuration, solver and grids. Their agreement is therefore not
independent evidence. Neither part compares with an experiment or with
another code. The papers call the problem "shock-wave diffraction"; it
is a reflection problem on a concave wall, unrelated to the
backward-corner [shock diffraction](/benchmarks/shock-diffraction.md).
The wave vocabulary (regular and Mach reflection, single and double
triple point, transition angle) is defined on
[regular and Mach reflection](/definitions/mach-reflection.md).

**Set-up** ([Brahmi et al. (2020)](/sources/brahmi-2020.md), §3, Fig. 1;
[Brahmi et al. (2020b)](/sources/brahmi-2020-b.md), §3, Fig. 2).
* *Geometry.* Two concave circular arcs in series, both of radius
  50 mm, each with an initial wall (diffraction) angle
  $\theta_{\mathrm w} = 75°$ (the papers' $\omega_1$, $\omega_2$). The
  centre of the first arc lies above that of the second. In units of the
  arc radius: inlet height 0.32, outlet height 1.8, length 3.4. Part II
  does not print the domain size.
* *Boundaries.* Inflow on the left, outflow on the right, symmetry planes
  on the top and bottom right, no-slip on the solid. The thermal wall
  condition is not stated.
* *Initial data.* The shock starts 5 mm ahead of the first concave
  corner, with the Rankine–Hugoniot state behind it and air at rest at
  $T = 300$ K and $p = 101.3$ kPa ahead of it.
* *Gas.* Air, $\gamma = 1.4$, $\mathrm{Pr} = 0.72$, Sutherland viscosity;
  Part II gives $\mathrm{Re}$ of order $10^6$ (post-shock properties,
  arc radius).
* *Shock Mach numbers.* $M_s = 1.6$, 2.0, 2.5, 3.5, 4.5. Both abstracts
  call the range "transonic to supersonic"; every one of these shocks is
  supersonic.

**Scheme of record** (both parts, §2). An in-house compressible
Navier–Stokes solver: [WENO](/methods/weno.md) of fifth order for the
inviscid fluxes, fourth-order central differences for the viscous fluxes,
third-order Runge–Kutta, adaptive multiresolution refinement, and an
[immersed boundary](/methods/immersed-boundary-method.md) with the solid
embedded in the Cartesian grid and tracked by ray tracing. Neither part
states the Riemann solver or flux splitting, the IB variant or the
multiresolution thresholds. Courant number 0.7, time step about
$10^{-8}$ s.

**Grid study** ([Brahmi et al. (2020)](/sources/brahmi-2020.md), §4.1,
Tables 1–2). Five grids at $M_s = 1.6$, with finest spacings
$h_x/h_y$ in µm and point counts in millions:

| Grid | $h_x$ / $h_y$ (µm) | Points (M) | $\theta_{\mathrm{tr}}$ arc 1 / arc 2 |
|---|---|---|---|
| G0 | 95 / 88 | 1.83 | 9.6° / 9.7° |
| G1 | 60 / 50 | 5.04 | 10.7° / 10.8° |
| G2 | 40 / 40 | 8.84 | 11.8° / 11.8° |
| G3 | 30 / 29 | 17.3 | 12.7° / 12.6° |
| G4 | 20 / 21 | 33.55 | 12.7° / 12.6° |

The transition angle rises with resolution until G3 and is unchanged from
G3 to G4. Wall pressure, skin friction at $t = 294$ µs, and shock
position and velocity are also grid-independent from G3; G4 is used
for all other runs. In Part II the primary-vortex topology changes with
resolution, but the circulation history does not
([Brahmi et al. (2020b)](/sources/brahmi-2020-b.md), §4.1, Figs. 3–4).

**Transition angle against $M_s$** ([Brahmi et al. (2020)](/sources/brahmi-2020.md),
§4.1, Fig. 4). $\theta_{\mathrm{tr}}$ rises with $M_s$ (the papers do not
state from what the angle is measured). It is nearly the
same on both arcs up to $M_s = 2.5$ and larger on the second arc at
$M_s = 3.5$ (by about 4%) and $M_s = 4.5$ (by about 7%). The values are
given only graphically, with a fitted curve whose formula is not printed;
read off the figure (compiler's reading, not printed) they are about 12°
at $M_s = 1.6$, 14° at 2.0, 24–25° at 2.5, 67°/70° at 3.5 and 70°/75° at
4.5 (first/second arc).

**Wave configurations** ([Brahmi et al. (2020)](/sources/brahmi-2020.md),
§4.1, Figs. 5–7). Triple points are traced by accumulating, step by step,
the maximum of the pressure-gradient magnitude $\vert\nabla p\vert$
(eq. 8).
* First arc: Mach reflection with a weak reflected shock at the end of
  the arc for $M_s = 1.6$ and 2.5; regular reflection at the start, then
  transition to Mach reflection, for $M_s = 3.5$ and 4.5.
* Second arc: the same as the first for $M_s \le 2.5$. At $M_s = 3.5$ and
  4.5 regular reflection turns into a single-triple-point Mach reflection,
  then a second triple point appears (single to double triple point). At
  $M_s = 4.5$ the two triple points later merge (single, double, single).
  The second Mach stem is larger at 4.5 than at 3.5. Schlieren instants:
  123, 135, 141, 144 µs at $M_s = 3.5$; 99, 105, 108, 111 µs at 4.5. The
  authors read the return to a single triple point as the flow "retaining
  the memory of past events", an interpretation, not a measurement.
* Primary and secondary corner vortices form at the cavity entrance; the
  interaction of the near-wall instability with the primary vortex is
  named "one of the main sources" of secondary shocks (qualitative).

**Shock attenuation and the time scaling** ([Brahmi et al. (2020)](/sources/brahmi-2020.md),
§4.2, eqs. 9–10, Figs. 8–9). The incident shock keeps its initial speed
until it reaches the corner and then slows; the velocity deficit grows
with $M_s$, and stronger shocks start to slow earlier. With time scaled
by the initial shock speed over the arc radius, times the factor
$$(M_s+1)\ln(M_s+1)^{1/\gamma} - \frac{\gamma-1}{\gamma}\left(M_s^2-1\right),$$
shock position and velocity for all five $M_s$ collapse onto one curve.
The factor was "found from the data analysis", with no derivation, and is
tested only for $\gamma = 1.4$ and one radius, so its claimed dependence
on $\gamma$ and on the radius is untested. The precedence of
$\ln(M_s+1)^{1/\gamma}$ is ambiguous as printed: read as
$\frac1\gamma\ln(M_s+1)$, the factor is about 1.33 at $M_s = 1.6$ and 1.20
at 4.5 (compiler's arithmetic); $\left[\ln(M_s+1)\right]^{1/\gamma}$ is not
excluded by the typography.

**Circulation** ([Brahmi et al. (2020b)](/sources/brahmi-2020-b.md),
§4.1, Fig. 5). The circulation $\Gamma$, integrated over the whole
domain, grows linearly in time. $\Gamma/t$, scaled by the specific gas
constant times $T = 300$ K, reaches the constants **1.78, 3.79, 5.72,
11.42, 18.73** for $M_s = 1.6$, 2.0, 2.5, 3.5, 4.5 (grid G4). This agrees
qualitatively with Sun and Takayama's finding that $\Gamma/t$ depends
only on $M_s$ for a fixed gas and angle. Vorticity production starts
in the wall boundary layer before the shock diffracts ($t = 12$ µs at
$M_s = 2.0$), consistent with Tseng and Yang.

**Vorticity balance** ([Brahmi et al. (2020b)](/sources/brahmi-2020-b.md),
§4.2, eq. 9, Figs. 7–9). In the 2D vorticity transport equation the
stretching term vanishes, leaving the dilatation term
$-(\nabla\times\mathbf v)(\nabla\cdot\mathbf v)$, the baroclinic term
$\frac{1}{\rho^2}\nabla\rho\times\nabla p$ and the viscous term
$\nabla\times(\nabla\cdot\boldsymbol\tau/\rho)$. The dilatation term
dominates; it and the unsteady and convective parts are almost constant
in time, growing in magnitude with $M_s$. The viscous term is "quite
important" relative to the baroclinic term for $M_s \le 2.5$, and the
order is inverted for $M_s \ge 3.5$, a finding the abstract claims "for
the first time". The normalization of the plotted terms is not stated.

**Impulse attenuation** ([Brahmi et al. (2020b)](/sources/brahmi-2020-b.md),
§§4.3, 6, Figs. 10–13). Static and dynamic pressure impulses (time
integrals of $p$ and of $\tfrac12\rho\vert\mathbf v\vert^2$) and the
overpressure relative to the pre-shock pressure are recorded at a probe
at the start of the first arc ($(0.26, 1.6)$ in arc radii) and one at the
start of the second ($(1.22, 0.86)$). The first arc reduces the dynamic
impulse by up to 90% ($M_s = 2.5$) and the static impulse by up to 75%
($M_s = 4.5$). The peak overpressure is not reduced, because the
reflected shock and shocklets give second-probe peaks above the first
probe's; at high $M_s$ the overpressure at the second probe turns
negative (vortex suction).

**Disagreement with Soni et al. (2017), as reported.** Soni et al. found
$\theta_{\mathrm{tr}}$ larger on the second reflector for $M_s$ up to 2.5,
and explained it by subsonic flow behind the Mach stems carrying
information. Here the two arcs agree up to $M_s = 2.5$. The authors
attribute the difference to a different reflector orientation and shock
entrance and do not reconcile it further
([Brahmi et al. (2020)](/sources/brahmi-2020.md), §§1, 4.1). Soni et al.
(2017) is not ingested, so this is recorded as the citing paper's report,
not as a contradiction.

**What a scheme can be scored against.** Table 2 and Fig. 4 transition
angles, the triple-point sequence on the second arc, the collapse of the
scaled shock histories, the five $\Gamma/t$ plateaus and the impulse
deficits. All are numerical, from a single code, with a grid study but
no error norms, no order measurement and no experiment.

**Recorded as printed.** Both parts print the energy equation (eq. 3)
with the pressure work as the divergence of $\rho\mathbf v$; the
divergence of $p\mathbf v$ is meant (checked at 300 dpi in both).

**Related set-ups.** A shock on a straight wedge:
[double Mach reflection](/benchmarks/double-mach-reflection.md) (Mach 10,
30°) and [Schardin's problem](/benchmarks/schardin-problem.md) (a
triangular wedge at Mach about 1.3). A convex body:
[shock reflection from a cylinder](/benchmarks/shock-reflection-from-cylinder.md).
Here the double triple point forms on a curved concave wall, not on a
straight wedge.

# Citations

1. [Brahmi et al. (2020)](/sources/brahmi-2020.md), §§1–5, Tables 1–2, Figs. 1–9, eqs. 3, 8–10.
2. [Brahmi et al. (2020b)](/sources/brahmi-2020-b.md), §§2–4, 6, Table 1, Figs. 2–13, eqs. 3, 9.

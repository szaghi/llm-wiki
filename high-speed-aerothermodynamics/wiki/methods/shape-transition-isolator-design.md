---
type: Method
title: "Shape-transition isolator design"
description: "Parameterises a curved isolator whose cross-section changes shape by linearly blending entrance and exit sections with area rescaling and translating them along a B-spline offset line, whose three free variables are optimised for exit total-pressure recovery by a multi-island genetic algorithm coupled to RANS."
status: established
aliases: [shape-transition isolator, curved shape-transition isolator, Barger blending, offset-line parameterisation]
tags: [isolator, design-method, optimization]
timestamp: 2026-10-14T00:00:00Z
---

# Shape-transition isolator design

A shape-transition isolator connects an intake exit and a combustor
entrance of different cross-sectional shape (for example rectangular to
circular) and, when curved, offsets its centreline. The method below builds
the duct geometrically from prescribed sections and optimises its
centreline with CFD; the inviscid route that carves an intake out of an
axisymmetric parent flow is
[Inward-turning intake design](/methods/inward-turning-intake-design.md).

[Meng et al. (2018)](/sources/meng-2018.md), §2, parameterise a curved
isolator whose cross-section changes shape along its length in two steps:

1. **Section blending** (§2.1, after Barger). Each intermediate
   cross-section is the linear blend of the entrance and exit section
   curves, weighted by the normalised streamwise position between them.
   The blend alone does not preserve area: unscaled, it overshoots the
   design area by up to about 16% at mid-length (approximate, read from
   Fig. 3). Each section is therefore rescaled by a factor found by
   numerical iteration so that its area matches a prescribed area
   distribution along the duct.
2. **Offset line** (§2.1, Fig. 5, Table 1). The sections are translated
   along an offset line, a B-spline through five control points at
   normalised streamwise/transverse positions (0, 0), (first variable, 0),
   (0.5, third variable times the offset-to-length ratio), (second
   variable, offset-to-length ratio) and (1, offset-to-length ratio). The
   second and fourth points fix zero end slopes, which the authors state
   makes the line monotone. The three free variables are the design
   variables.

**Optimisation** (§2.2, §3, Fig. 6). A multi-island genetic algorithm in
Isight drives a loop of geometry, grid, 3-D RANS with the
[SST k–ω model](/methods/sst-k-omega-model.md) and objective evaluation.
The objective is the exit $\sigma_0$ without back pressure at entrance
Mach 2, total pressure 100 kPa and total temperature 300 K, chosen because
back-pressured runs are too costly; each evaluation runs 5000 steps
(Table 3). For the rectangular-to-circular case none of the three
variables converges, the first settles near 0.3 after 300 iterations and the
objective converges after about 200 iterations to roughly 0.89 (Fig. 8);
the authors read the non-convergence of the variables as evidence that
the objective is nonlinear in them, which justifies a global algorithm.

**Outcome.** For 800 mm long isolators with a 40 mm offset, the optimised
rectangular-to-circular duct recovers 1.59% more total pressure than a
baseline rectangular-to-circular design "successfully applied in the
scramjet", has exit Mach number 1.96 with better uniformity, and holds the
shock train furthest downstream under back pressure (§4.2–4.3, Figs. 11,
12, 14); results are on
[Isolator and shock train](/definitions/isolator-shock-train.md). The
authors relate the method to Smart's REST shape-transition inlets and mention streamline tracing (Billig & Kothari)
without using it (§1).

# Citations

1. [Meng et al. (2018)](/sources/meng-2018.md), §1, §2.1–2.2 (Figs. 3, 5–6, Table 1), §3 (Table 3), §4.1–4.3 (Figs. 8, 11–14).

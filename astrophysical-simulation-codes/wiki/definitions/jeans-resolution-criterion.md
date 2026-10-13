---
type: Definition
title: "Jeans resolution criterion (Truelove condition)"
description: "The requirement that the local Jeans length be resolved by at least four cells (Truelove et al.), used as an AMR refinement criterion and, at the finest level, as the density threshold for sink-particle creation; stated to apply only to gas in self-gravitational collapse, with more cells needed for MHD."
status: established
aliases: [Truelove criterion, Truelove condition, Jeans condition, Jeans refinement criterion, cells per Jeans length, Jeans number]
tags: [self-gravity, amr, sink-particles]
timestamp: 2026-10-12T00:00:00Z
---

# Jeans resolution criterion (Truelove condition)

The Jeans length of gas of density $\rho$ and (isothermal) sound speed
$c_s$ is
$$\lambda_{\mathrm J} = \sqrt{\frac{\pi c_s^2}{G\rho}}$$
([Federrath et al. (2010)](/sources/federrath-2010.md), eq. 2;
[Krumholz et al. (2004)](/sources/krumholz-2004.md), eq. 5). The
**Truelove condition** requires it to be resolved by at least four cells,
$$N_{\mathrm J} \equiv \frac{\lambda_{\mathrm J}}{h} \ge 4,$$
which Truelove et al. (1997) found sufficient to prevent artificial
fragmentation ([Krumholz et al. (2004)](/sources/krumholz-2004.md), §2.2;
[Federrath et al. (2010)](/sources/federrath-2010.md), §2.2.1).
Krumholz et al. state it as cell size below one quarter of the Jeans
length (their Truelove number 0.25 $= 1/N_{\mathrm J}$). Heitsch et al. (2001) find that with MHD "more
than four cells are required"
([Federrath et al. (2010)](/sources/federrath-2010.md), §2.2.1).

At fixed $h$ the condition is a density bound: a cell violates it when
$$\rho > \frac{\pi c_s^2}{N_{\mathrm J}^2Gh^2}$$
([Krumholz et al. (2004)](/sources/krumholz-2004.md), eqs. 6–7), so the
resolvable density falls as $h^{-2}$. A cell at that bound holds more than
about $0.07$ Bonnor–Ebert masses for $N_{\mathrm J} = 4$, so a violation
does not by itself mean the gas is unstable (§2.2, eqs. 8–9).

## Scope

[Federrath et al. (2010)](/sources/federrath-2010.md) stress that the
Truelove and Heitsch criteria "are only meaningful in regions that are
undergoing self-gravitational collapse" (§2.2.1), and argue that gas in
shocks may exceed the corresponding density without violating it, since
"By definition, the Truelove criterion only applies to gravitationally
bound gas in freefall collapse" (§2.2.8; an interpretation, asserted).
Pure AMR can satisfy it only for the first object to collapse: refining
that object stalls the whole run on its Courant step (§2.2.1). This is the
motivation for [sink particles](/methods/sink-particles.md).

## Uses

* **Refinement criterion.** [Enzo](/software/enzo.md) refines on the
  Jeans length with 4 cells per Jeans length by default
  ([Bryan et al. (2014)](/sources/bryan-2014.md), §3.6, eq. 29; Bryan et al.
  cite Truelove et al. 1998 for it, and print the cell number
  inconsistently; the printed symbols are mapped on the Source page).
  FLASH, in [Federrath et al. (2010)](/sources/federrath-2010.md), refines
  to keep at least 12 cells per $\lambda_{\mathrm J}$ on every level below
  the finest and 5 on the finest (§4.2.1), and refines at 6 and derefines
  above 12 cells in the gas–sink gravity test (§3.2). See
  [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).
* **Sink-creation threshold at the finest level.**
  * [Krumholz et al. (2004)](/sources/krumholz-2004.md), §2.2: a sink
    forms in any finest-level cell that violates the condition with
    $N_{\mathrm J} = 4$, taking the mass above the threshold. The
    violation implies $\nabla\cdot\mathbf v < 0$ by continuity, which
    mirrors the SPH conditions of converging, bound flow.
  * [Federrath et al. (2010)](/sources/federrath-2010.md), §2.2.1 and
    eq. 32: the threshold is set by $\lambda_{\mathrm J} = 2r_{\mathrm{acc}}$,
    i.e. $\rho_{\mathrm{thr}} = \pi c_s^2/(4Gr_{\mathrm{acc}}^2)$; four
    cells per $\lambda_{\mathrm J}$ require $r_{\mathrm{acc}}\ge2h$, and
    the paper uses $r_{\mathrm{acc}}\simeq2.5h$ (5 cells). The threshold
    is a necessary condition only; five further checks follow (see
    [sink particles](/methods/sink-particles.md)).
  * In both, a separate refinement criterion keeps every cell within a
    sink's accretion radius on the finest level
    ([Krumholz et al. (2004)](/sources/krumholz-2004.md), §2.1;
    [Federrath et al. (2010)](/sources/federrath-2010.md), §2.2.2).

The related free-fall time is
$t_{\mathrm{ff}} = \sqrt{3\pi/(32G\rho)}$
([Federrath et al. (2010)](/sources/federrath-2010.md), eq. 1).

The original Truelove et al. (1997) paper is not in the archive; the
condition is recorded here as the ingested sources state it.

## Later uses (batch 4)

* **A Larson–Penston sink threshold.**
  [Kim & Ostriker (2017)](/sources/kim-2017.md), §2.2.1, eq. 7, create
  sinks in [TIGRESS](/software/tigress.md) above the density of the
  Larson–Penston collapse solution at half a cell,
  $$\rho_{\mathrm{thr}} = \frac{8.86\,c_s^2}{\pi Gh^2},$$
  with $c_s$ the isothermal sound speed $(p/\rho)^{1/2}$, together with
  potential-minimum and converging-flow checks (see
  [sink particles](/methods/sink-particles.md)). They state that the
  Truelove threshold has "the same parameter dependence, but with a
  coefficient of π/16 instead of 8.86/π", which agrees with the bound
  above at $N_{\mathrm J} = 4$. From the printed coefficients (computed
  here, not stated in the paper), their threshold is about 14 times the
  $N_{\mathrm J} = 4$ bound, and at it $\lambda_{\mathrm J}/h = \pi/\sqrt{8.86}\approx1.06$:
  the criterion is used as a physically motivated sink trigger on a
  uniform grid, not as a refinement criterion.
  **Open qualification:** between the $N_{\mathrm J} = 4$ density and this
  threshold, collapsing gas in TIGRESS is evolved with $N_{\mathrm J}$
  falling from 4 to about 1.06, below the Truelove condition stated at the
  top of this page (compiler arithmetic from the printed coefficients).
  The only test is a single collapsing sphere, which cannot show
  artificial fragmentation; no source tests it.
* **Resolution needed to capture collapse.** The same paper requires the
  pressure at the threshold to greatly exceed the two-phase equilibrium
  pressure, $3110\,k_{\mathrm B}$ cm⁻³ K scaled with the heating rate, for
  collapse to be "captured"; in Solar-neighbourhood conditions this needs
  $h < 20$ pc, and even the marginal case "is inaccessible for current
  cosmological galaxy formation simulations" (§2.2.1, eq. 8, Fig. 3).
  Instantaneous conversion of sinks into star clusters is stated valid up
  to $h = 8$ pc.
* **Sixteen cells per Jeans length in later FLASH runs.**
  [Mathew & Federrath (2021)](/sources/mathew-2021.md), §2.3, in
  [FLASH](/software/flash.md): "On all other AMR levels, $\lambda_{\mathrm J}$ is
  always resolved with at least 16 grid cell lengths to prevent
  underestimation of the turbulent energy and to resolve the local
  collapse reasonably well (Federrath et al. 2011)". This raises the 12
  cells of Federrath et al. (2010) above, in a different paper and set-up,
  and gives a reason beyond Truelove's artificial fragmentation: the
  turbulent energy. At the finest level $2r_{\mathrm{acc}} = 5h$, which
  "ensures that the Truelove et al. (1997) criterion is satisfied", the
  same 5 cells as in Federrath et al. (2010). The Jeans length is defined
  as above.

# Citations

1. [Krumholz et al. (2004)](/sources/krumholz-2004.md), §§2.1–2.2,
   eqs. 5–9 (arXiv preprint v1).
2. [Federrath et al. (2010)](/sources/federrath-2010.md), §§1, 2.2.1,
   2.2.2, 2.2.8, 3.2, 4.2.1, eqs. 1–2, 32 (arXiv v2).
3. [Bryan et al. (2014)](/sources/bryan-2014.md), §3.6, eq. 29 (arXiv v1).
4. [Kim & Ostriker (2017)](/sources/kim-2017.md), §2.2.1, eqs. 7–8,
   Fig. 3 (arXiv v2).
5. [Mathew & Federrath (2021)](/sources/mathew-2021.md), §2.3, eq. 4
   (arXiv v2).

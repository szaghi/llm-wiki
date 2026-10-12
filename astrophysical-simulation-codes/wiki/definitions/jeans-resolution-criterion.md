---
type: Definition
title: "Jeans resolution criterion (Truelove condition)"
description: "The requirement that the local Jeans length be resolved by at least four cells (Truelove et al.), used as an AMR refinement criterion and, at the finest level, as the density threshold for sink-particle creation; stated to apply only to gas in self-gravitational collapse, with more cells needed for MHD."
status: established
aliases: [Truelove criterion, Truelove condition, Jeans condition, Jeans refinement criterion, cells per Jeans length, Jeans number]
tags: [self-gravity, amr]
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
  inconsistently as $N_J$, "$J_J$" and "$J$").
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

# Citations

1. [Krumholz et al. (2004)](/sources/krumholz-2004.md), §§2.1–2.2,
   eqs. 5–9 (arXiv preprint v1).
2. [Federrath et al. (2010)](/sources/federrath-2010.md), §§1, 2.2.1,
   2.2.2, 2.2.8, 3.2, 4.2.1, eqs. 1–2, 32 (arXiv v2).
3. [Bryan et al. (2014)](/sources/bryan-2014.md), §3.6, eq. 29 (arXiv v1).

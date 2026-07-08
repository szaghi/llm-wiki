---
type: Method
title: "Refluxing (coarse-fine flux correction)"
description: "Restores discrete conservation at AMR interfaces by replacing the coarse flux with the accumulated sum of fine fluxes on shared edges."
status: established
aliases: [flux correction, flux synchronization]
tags: [amr, conservation, refluxing, coarse-fine-interface]
timestamp: 2026-07-08T00:00:00Z
---

# Refluxing (coarse-fine flux correction)

The correction pass that makes a conservative scheme remain conservative on
a [block-structured AMR](/definitions/block-structured-amr.md) hierarchy,
introduced by [Berger & Colella (1989)](/sources/berger-colella-1989.md).

At a coarse cell abutting a fine patch (but not covered by it), the
uncorrected scheme uses the coarse flux on the shared edge while the fine
patch used its own fine fluxes there — the two sides disagree and mass,
momentum, or energy is created at the interface. Conservation requires the
flux out of the coarse cell to equal the space-and-time sum of the fine
fluxes on that edge:
$$F^{\mathrm{eff}}_{i+\frac12,j} = \frac{1}{r^2}\sum_{k=1}^{r}\sum_{m=1}^{r} F^{\,\mathrm{fine},k}_{\,\mathrm{edge}\,m},$$
accumulated over the $r$ subcycled fine steps ($r^2$ becomes $r^{d}$
appropriately with dimension and geometry).

**Implementation** (their eqs. 3–5): keep an edge register $\delta F$ on the
outer boundary of each fine patch; initialize with *minus* the provisional
coarse flux; add each fine-step flux sum; after $r$ fine steps, apply
$\delta F$ as a correction to the abutting coarse cells. Storage is
proportional to patch perimeters only. Covered coarse cells need no flux
fix — they are overwritten by the conservative average outright, which is
equivalent (to roundoff) to summing fine fluxes around them.

## Relevance to the divergence constraint

Refluxing repairs conservation of *cell* quantities ($V_h^3$ densities) at
interfaces. It says nothing about *face* quantities: a face-flux invariant
like $D_h B_h = 0$
([exact discrete divergence](/properties/exact-discrete-divergence.md))
needs its own interface synchronization — supplied for staggered CT by the
exactly analogous
[electric-field correction](/methods/electric-field-correction.md) on edge
EMFs ([Balsara (2001)](/sources/balsara-2001.md)).

For diffusive/elliptically-coupled systems the correction generalizes:
flux mismatches enter the right-hand sides of *elliptic refluxing solves*
rather than being added pointwise, and face-velocity mismatches get their
own elliptic sync solve —
[AMR projection method](/methods/amr-projection-method.md)
([Almgren et al. (1998)](/sources/almgren-1998.md)).

# Citations

1. [Berger & Colella (1989)](/sources/berger-colella-1989.md), §3, Figs. 3.1–3.2.
2. [Almgren et al. (1998)](/sources/almgren-1998.md), §3.

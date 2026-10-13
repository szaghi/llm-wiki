---
type: Method
title: "Refluxing (coarse-fine flux correction)"
description: "Restores discrete conservation at AMR interfaces by replacing the coarse flux with the accumulated sum of fine fluxes on shared edges."
status: established
aliases: [flux correction, flux synchronization]
tags: [amr, conservation, refluxing, coarse-fine-interface]
timestamp: 2026-10-13T00:00:00Z
---

# Refluxing (coarse-fine flux correction)

The correction pass that makes a conservative scheme remain conservative on
a [block-structured AMR](/definitions/block-structured-amr.md) hierarchy,
introduced by [Berger & Colella (1989)](/sources/berger-colella-1989.md).

**Before refluxing.** The earlier AMR algorithm of
[Berger & Oliger (1984)](/sources/berger-oliger-1984.md) has no flux
correction: covered coarse values are updated by injection of fine values,
and the paper states only that stable interface conditions maintaining the
conservation form "have been derived" and "will also be reported
elsewhere" (p. 493).

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

The separation is directly measured in one AMR library
([Zaghi (2026)](/sources/zaghi-2026.md), hypothesis):
* In its MHD solver, reflux keeps the volume integrals of a periodic box
  with 2:1 seams at round-off ($\le 4.7\cdot10^{-14}$), $B_h$ and $\psi_h$
  included. The Euler version of the test drifts at $10^{-5}$ without
  reflux.
* In its collocated Maxwell solver, reflux on and off leaves the 2:1 seam
  divergence bit-identical.
* The finite-volume variant with active reflux reproduces the
  finite-difference seam-divergence runaway to 4–5 significant figures.

Conservation and solenoidality are different defects with different
mechanisms ([seam divergence source](/results/collocated-seam-divergence-source.md)).

For diffusive/elliptically-coupled systems the correction generalizes:
flux mismatches enter the right-hand sides of *elliptic refluxing solves*
rather than being added pointwise, and face-velocity mismatches get their
own elliptic sync solve —
[AMR projection method](/methods/amr-projection-method.md)
([Almgren et al. (1998)](/sources/almgren-1998.md)).

**Refluxing changes elliptic sources: self-gravity.** In CASTRO each
synchronization volume-averages level $l+1$ onto level $l$, then refluxes
level-$l$ cells next to, but not covered by, the fine grids. Refluxing
changes the coarse density and with it the gravitational source. The
refluxing-only density change is therefore kept apart, and a **second
flux register** records the mismatch of $\partial\phi_{\mathrm g}/\partial n$ (the
gravitational potential) between coarse and fine faces. Both drive a
two-level composite correction solve, whose result corrects momentum
and energy. It is then added to the next-coarser register, so the
correction propagates down the hierarchy ([Almgren et al. (2010)](/sources/almgren-2010.md), §6.2.3,
eqs. 36–40; [AMR projection method](/methods/amr-projection-method.md)).

**Codes without a flux register.**
* A GPU lattice-Boltzmann AMR couples levels only through interpolated
  ghost distributions and averaged interface cells. It claims no
  conservation across levels and measures none ([Jaber, Essel & Sullivan (2025)](/sources/jaber-essel-sullivan-2025.md), §3.4).
* ADAM's 2023 paper never mentions refluxing ([Zaghi et al. (2023)](/sources/zaghi-2023.md)).
* The AMReX software paper names only an unspecified "multilevel
  synchronization" ([Zhang et al. (2019)](/sources/zhang-2019.md)).

**With multistage time integration.** In Flash-X on AMReX, the flux
register between each pair of levels can hold a linear combination of the
Runge–Kutta stage fluxes. The correction is applied once at the end of
the step. Paramesh, which advances all levels at once, needs a different
path ([Couch et al. (2021)](/sources/couch-2021.md)).
*Compiler reading:* this keeps the register consistent with the stage
weights of the scheme. It is the conservation-side counterpart of the
stage-coupling requirement recorded for the divergence invariant at
seams ([exact discrete divergence](/properties/exact-discrete-divergence.md)).

**A flux correction stated by citation only.** ALPACA, a block-tree
multiresolution code with local time stepping, applies a "Resolution jump
flux correction" at the last Runge–Kutta stage of each step (Algorithm 1).
The paper gives no formula, no register description and no conservation
measurement; all of it is deferred to Kaiser et al. (2019, J. Comput.
Phys. X 4:100038). Conservation across resolution jumps is therefore
asserted by reference, not shown ([Hoppe et al. (2022)](/sources/hoppe-2022.md), Algorithm 1).

# Citations

1. [Berger & Colella (1989)](/sources/berger-colella-1989.md), §3, Figs. 3.1–3.2.
2. [Almgren et al. (1998)](/sources/almgren-1998.md), §3.
3. [Zaghi (2026)](/sources/zaghi-2026.md): issue #21 §2, #29; FLUME `verification.md` (conservation across AMR seams, MV-11).
4. [Couch et al. (2021)](/sources/couch-2021.md), AMR and performance sections.
5. [Almgren et al. (2010)](/sources/almgren-2010.md), §§6.2.1, 6.2.3.
6. [Jaber, Essel & Sullivan (2025)](/sources/jaber-essel-sullivan-2025.md), §3.4.
7. [Zaghi et al. (2023)](/sources/zaghi-2023.md).
8. [Zhang et al. (2019)](/sources/zhang-2019.md).
9. [Hoppe et al. (2022)](/sources/hoppe-2022.md), Algorithm 1.
10. [Berger & Oliger (1984)](/sources/berger-oliger-1984.md), §3, p. 493.

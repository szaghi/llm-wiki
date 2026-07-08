---
type: Method
title: "Electric-field correction"
description: "Restores divergence-free consistency at AMR interfaces by replacing coarse edge EMFs with time-averaged sums of the subcycled fine edge EMFs."
status: established
aliases: [EMF correction, E-field synchronization]
tags: [amr, constrained-transport, coarse-fine-interface, subcycling, divergence-constraint]
timestamp: 2026-07-08T00:00:00Z
---

# Electric-field correction

The face-field analog of [refluxing](/methods/refluxing.md), introduced by
[Balsara (2001)](/sources/balsara-2001.md) §V for
[constrained-transport](/methods/constrained-transport.md) AMR.

**The inconsistency it repairs.** Over one coarse step, the coarse face
field updates with coarse edge EMFs (his eq. 5.1) while the overlying fine
faces update twice with fine edge EMFs (eqs. 5.2–5.3). Synchronizing by
area-weighted restriction — coarse face := average of its four fine faces
(eq. 5.4) — then *disagrees* with the coarse update, and the divergence of
the abutting (uncovered) coarse zones becomes nonzero even though it was
zero at every prior time. Restriction alone cannot preserve the invariant
under subcycling.

**The correction** (eqs. 5.6–5.7): on every coarse edge shared with a fine
patch boundary, replace the coarse EMF contribution by the time-averaged
sum of the fine edge EMFs accumulated over the subcycled fine steps — then
the coarse update, the fine updates, and the restriction are mutually
consistent, and the divergence-free evolution survives on the whole
hierarchy. The exact analogy: flux correction restores *flux* consistency
at interfaces and thereby conservation of $V_h^3$ densities; electric-field
correction restores *EMF* consistency ($V_h^1$ data) and thereby the
$D_h^{\mathrm{f}} B_h = 0$ invariant ([notation](/notation.md),
[exact discrete divergence](/properties/exact-discrete-divergence.md)).

Storage mirrors refluxing: edge registers on fine-patch perimeters,
accumulated during subcycling, applied at synchronization.

# Citations

1. [Balsara (2001)](/sources/balsara-2001.md), §V, Fig. 3.

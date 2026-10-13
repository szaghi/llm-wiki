---
type: Source
title: "Evans & Hawley (1988) — Simulation of MHD flows: a constrained transport method"
description: "Introduces constrained transport (CT): staggered flux-based induction-equation update preserving the divergence constraint to machine roundoff."
resource: "doi:10.1086/166684"
source_kind: paper
authors: [Evans C.R., Hawley J.F.]
year: 1988
venue: "Astrophys. J. 332:659-677"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1988-ApJ-Evans-101086166684.pdf"
tags: [constrained-transport, staggered, mhd, induction-equation, general-relativity]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Foundational paper introducing **constrained transport (CT)** for the MHD
induction equation. The induction equation is written in integral form with
magnetic flux through cell faces as the fundamental variable; face-flux updates
are assembled from edge electromotive-force (EMF) contributions, each edge EMF
computed once and used in exactly two face updates with opposite signs, so the
net flux through every closed cell surface — the discrete divergence — is
conserved identically. The formulation is developed simultaneously for
Newtonian and general-relativistic (3+1) MHD: with the magnetic vector density
$\mathscr{B}^i \equiv \gamma^{1/2} B^i$ the GR induction equation takes the
same "Cartesian-looking" form as the flat-space one, so CT applies in
arbitrary coordinates and curved, dynamic spacetimes unchanged.

The PDF is an image-only scan (zero extractable text); it was read visually,
all 19 pages. No illegible ranges.

# Key claims

1. **Constraint preservation to roundoff.** The CT update preserves the
   discrete divergence of the face-flux field exactly in the algebra; in
   practice the monitored divergence measure $\xi$ (their eq. 5.6) sits at
   $\sim 10^{-15}$, accumulating roundoff at a problem-dependent rate (up to
   $10^{-10}$ in one run); evolving the field in double precision keeps it at
   $10^{-15}$–$10^{-14}$ throughout ([exact discrete divergence](/properties/exact-discrete-divergence.md)).
2. **Generality of the transport algorithm.** The scheme (their §IV) places
   *no restriction on the order of accuracy* of the transport technique used
   for the edge EMFs; works in 2D and 3D and in arbitrary coordinate systems;
   is claimed to admit adaptive meshes naturally, because the flux-integral
   form (their eq. 2.12) already accounts for moving/changing zone geometry —
   with the caveat that the adaptive remap must be built from eq. (4.20)-form
   updates; "straightforward differencing of the adaptive mesh equation (2.10)
   would be disastrous to constraint satisfaction."
3. **CT preserves only divergence *changes*.** If the initial data violate the
   constraint, the violation persists; inflow/outflow boundaries can admit
   non-divergence-free field — they recommend monitoring a global constraint
   diagnostic during simulations.
4. **Advantage over vector-potential evolution.** Evolving $A$ keeps the
   field solenoidal but the Lorentz force then needs *second* differences of
   $A$; monotonic/hybrid schemes introduce new extrema in first derivatives,
   producing anomalous current oscillations (their Fig. 3–4, Cartesian
   advection and black-hole accretion tests). CT needs only one derivative of
   the evolved quantity. Choptuik's counterargument via Richardson's
   hypothesis is discussed and rebutted for flux-limited schemes, whose local
   adaptivity violates the smoothness premise.
5. **Divergence-consistent vector-potential differencing.** Their eq. (4.17):
   defining face fields as edge-differences of $A$ reproduces a field exactly
   divergence-free in the sense of the same discrete divergence (4.9) —
   usable for initial data and boundary conditions.

# Notation map

| Evans & Hawley | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathscr{B}^i = \gamma^{1/2} B^i$ (magnetic vector density) | $B_h$ | face-collocated DOFs; the metric hides in the density definition |
| $\Phi_S$ (face flux, eq. 4.5–4.6) | elements of $V_h^2$ | flux is the fundamental evolved quantity |
| $\mathscr{F}_{(l)}$ (edge EMF contributions, eq. 4.11) | $E_h \in V_h^1$ | edge-collocated |
| $A_k$ on edges (eq. 4.15–4.16) | elements of $V_h^1$ | vector potential shares edge collocation with $E_h$ |
| eq. (4.9), flux-difference divergence | $D_h$ | exactly $D_h : V_h^2 \to V_h^3$ |
| eqs. (4.13) update + (4.7) telescoping | $\partial_t B_h = -C_h E_h$, preservation via $D_h C_h = 0$ | *compiled translation*: they never write the complex identity; their once-per-edge/twice-per-face sign cancellation **is** $D_h C_h = 0$ |
| $u^i = V^i - V_g^i - \beta^i$ (eq. 4.12) | net transport velocity | includes grid velocity $V_g^i$ (adaptive mesh) and shift $\beta^i$ (GR) |
| $\xi$ (eq. 5.6) | normalized measure of $D_h B_h$ | diagnostic, not part of the scheme |

# Pages created or updated

* Created [Constrained transport](/methods/constrained-transport.md).
* Created [Exact discrete divergence](/properties/exact-discrete-divergence.md).
* Created [Staggered grid](/definitions/staggered-grid.md).

# Citations

1. `~/papers/mosaic/div-free-amr/1988-ApJ-Evans-101086166684.pdf` (doi:10.1086/166684) — read visually, pp. 659–677.

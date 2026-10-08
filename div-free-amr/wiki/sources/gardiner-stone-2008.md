---
type: Source
title: "Gardiner & Stone (2008) — An unsplit Godunov method for ideal MHD via constrained transport in three dimensions"
description: "The 3D Athena algorithm: unsplit CTU integration with upwind CT electric fields, PPM interface states with divergence-balanced MHD source terms, 6- and 12-solve variants."
resource: "doi:10.1016/j.jcp.2007.12.017"
source_kind: paper
authors: [Gardiner T.A., Stone J.M.]
year: 2008
venue: "J. Comput. Phys. 227:4123-4141"
local_file: "~/papers/mosaic/div-free-amr/2008-JCP-Gardiner-101016jjcp200712003.pdf"
tags: [constrained-transport, ctu, unsplit, godunov, ppm, production-code, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The 3D algorithm of the Athena code: single-step, second-order **unsplit
CTU** (corner transport upwind) integration combined with
[constrained transport](/methods/constrained-transport.md). Face
(area-averaged) fields are argued to be *the* natural discrete
representation — the induction equation's integral form is area-based —
and edge EMFs are built from Godunov fluxes by the upwind-biased
$\mathcal{E}^c$ CT algorithm (predictor: Godunov electric fields;
corrector: upwinded according to the contact mode), which reduces exactly
to the 1D algorithm for plane-parallel grid-aligned flow. Two CTU
variants: 12-solve (Saltzman-complete) and the simpler 6-solve, described
in detail.

# Key claims

1. **Dimensional splitting is impossible for MHD**: the constraint couples
   all three field components, which must update together — violating the
   independence assumption of split operators; hence unsplit CTU.
2. **PPM interface states need divergence-balanced "MHD source terms"**:
   the terms $\propto \partial B_x/\partial x$ etc. in the primitive-form
   induction equation must enter the characteristic tracing *and* the
   transverse-flux-gradient steps so as to respect the balance implied by
   $\nabla\cdot\mathbf{B} = 0$ — otherwise a field loop confined to the
   $(x,y)$-plane, advected with $v_z \ne 0$, spuriously grows $B_z$.
3. **The stencil made operational**: "if $\nabla\cdot\mathbf{B} = 0$ [holds]
   on a stencil which is different from that used to construct the fluxes
   of $B_z$, the latter will show unphysical evolution" — the field-loop
   test *detects* stencil-inconsistency, turning the scheme-specific
   nature of the constraint
   ([exact discrete divergence](/properties/exact-discrete-divergence.md))
   into a measurable failure mode; conversely, round-off-constant $B_z$
   certifies constraint preservation on the right stencil.
4. **Cost claim vs cleaning**: since CT needs no elliptic solves, CT-based
   Godunov schemes are expected "more cost effective" than
   divergence-cleaning approaches — an explicit cross-family judgment
   from the CT camp.
5. **6-solve vs 12-solve**: the economical variant halves the Riemann
   solves per zone per step; trade-offs assessed on a 3D test suite.

# Notation map

| Gardiner & Stone | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| area-averaged face $B$, edge $\mathcal{E}$ | $B_h \in V_h^2$, $E_h \in V_h^1$ | |
| $\mathcal{E}^c$ CT algorithm | upwind EMF assembly | contact-mode-biased corrector |
| "MHD source terms" | $\partial_x B_x$-type primitive terms | induction equation only |
| CTU 6-/12-solve | unsplit multidim integration | Colella/Saltzman lineage |

# Pages created or updated

* Updated [Constrained transport](/methods/constrained-transport.md) (unsplit necessity; upwind $\mathcal{E}^c$; 1D-reduction property).
* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md) (field-loop test as stencil-consistency detector).

# Citations

1. `~/papers/mosaic/div-free-amr/2008-JCP-Gardiner-101016jjcp200712003.pdf` (doi:10.1016/j.jcp.2007.12.017) — text extraction, pp. 4123–4141. **DOI corrected 2026-10-08.** The DOI recorded here earlier, 10.1016/j.jcp.2007.12.003, which the archive filename also embeds, belongs to Artebrant & Torrilhon (2008), JCP 227:3405 (Crossref). The work read is Gardiner & Stone, JCP 227:4123–4141, DOI 10.1016/j.jcp.2007.12.017 (Crossref; printed by mignone-2021). The Layer-1 filename was left unchanged.

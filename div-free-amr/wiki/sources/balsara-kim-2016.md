---
type: Source
title: "Balsara & Kim (2016) — Subluminal RMHD with an ADER-WENO predictor and a multidimensional Riemann solver"
description: "Fourth-order finite-volume scheme for special-relativistic MHD on a Yee-type mesh: reconstruction of the four-velocity keeps the velocity subluminal, an ADER predictor works in primitive variables, and the edge electric fields come from a two-dimensional MuSIC Riemann solver at each edge instead of averaged 1D fluxes."
resource: "doi:10.1016/j.jcp.2016.02.001"
source_kind: paper
authors: [Balsara D.S., Kim J.]
year: 2016
venue: "J. Comput. Phys. 312:357-384"
local_file: "~/papers/mosaic/div-free-amr/2016-JCP-Balsara-101016jjcp201602001.pdf"
tags: [constrained-transport, staggered, multidimensional-riemann-solver, relativistic-mhd, high-order]
timestamp: 2026-10-09T00:00:00Z
---

# Summary

A one-step, second- to fourth-order finite-volume scheme for special-relativistic
MHD. The fluid variables are zone-centred. The magnetic field lives on the faces
of a Yee-type mesh and is updated by edge electric fields
([constrained transport](/methods/constrained-transport.md)).
* **Reconstruction.** WENO or PPM in the primitive vector
  $(\rho, \gamma v_x, \gamma v_y, \gamma v_z, P_g, B_x, B_y, B_z)$. Reconstructing the
  spatial four-velocity $\gamma v$ makes the recovered velocity subluminal by
  construction, at every order (§2, eqs. 2.4–2.5).
* **Predictor.** ADER in the same primitive variables: Lax–Wendroff at
  second order, nodal space–time Picard iteration at third and fourth (§3).
* **Corrector.** A MuSIC multidimensional Riemann solver at each vertex
  returns multidimensionally upwinded fluxes. The edge electric field is
  taken from them (§4.2).

For the divergence constraint the only new element is the last one: the
edge field now comes from a genuinely two-dimensional Riemann solver instead
of averaged one-dimensional fluxes. No test reports a measure of
$\nabla\cdot B$, and no AMR run is shown.

# Key claims

1. **Yee-mesh necessity, stated as a premise** (§1, p. 358). "In a numerical
   code, keeping the magnetic field divergence-free requires the use of a
   staggered, Yee-type mesh"; "any divergence-free formulation of MHD
   requires the use of a Yee-type mesh". The paper gives no argument for
   necessity, and it does not cite Tóth (2000). Recorded as an attributed
   position under the [staggered grid](/definitions/staggered-grid.md)
   `## Contradictions` entry.
2. **The electric field is a flux component** (§1 p. 358, §4.2 p. 366),
   after Balsara and Spicer, and this carries over to RMHD: from eq. 2.1 the
   sixth component of the $y$-flux equals minus the seventh of the $x$-flux,
   which is $E_z$ ([flux-CT](/methods/flux-ct.md)).
3. **The edge field needs multidimensional upwinding, and two dimensions
   suffice** (§4.2 p. 366). "One dimensional Riemann solvers cannot
   arbitrate the multidimensionally upwinded direction." The flux along the
   edge does not contribute to the edge field, so the solver at a $z$-edge is
   two-dimensional.
4. **MuSIC solver at a $z$-edge** (§4.2, eqs. 4.1–4.15; eqs. 4.5–4.13 checked
   on the page images). The four states meeting at the vertex are bounded
   by four 1D HLLC or HLLEM problems. The strongly interacting state is a
   mean $\bar U$ (eq. 4.5) plus a linear sub-structure in the entropy and
   Alfvén waves (eqs. 4.2, 4.10–4.13), limited by a Barth–Frederickson-type
   criterion. Setting the sub-structure to zero gives a more dissipative,
   HLL-like variant (p. 368). Only the subsonic strongly interacting state
   is described.
5. **Edge field** (§4.2 p. 369): $E_z = \tfrac12\left(-(F_{\mathrm{num}})_7 + (G_{\mathrm{num}})_6\right)$,
   the mean of two components of the vertex fluxes from one 2D solve. This
   is a value of $E_h$ that belongs to none of the registry's averaged
   constructions ($\mathcal E^{\circ}$, $\mathcal E^{\alpha}$,
   $\mathcal E^{c}$; [notation](/notation.md)).
6. **No doubled dissipation, claimed** (§1 p. 358; §4.2 p. 369).
   Multidimensional Riemann solvers "completely eliminate any need to double
   the dissipation in the evaluation of the electric field", and the edge
   fields "will avoid all the issues raised by Gardiner and Stone". No
   test checks either claim: there is no field-loop or comparable run.
7. **Divergence-free reconstruction is delegated** (§1 p. 359): it "requires
   drawing on" Balsara 2001, 2004 and 2009 and "carries over directly to
   RMHD" ([divergence-free reconstruction](/methods/divergence-free-reconstruction.md)).
   The paper does not say how the zone-centred $B$ in the reconstructed
   primitive vector is obtained from the face fields.
8. **AMR, claimed suitability only.** The one-step update is "suited for
   AMR" (abstract; §1 p. 359). No transfer operator, interface treatment or
   AMR run is given.
9. **No positivity guarantee** (§1 p. 359): for multidimensional
   higher-order RMHD, positivity of density and pressure and a subluminal
   velocity "cannot be guaranteed".

**Tests** (§§5–6). Boosted relativistic hydrodynamic and RMHD vortices
reach design order: $L_1$ density order 4.51 and $L_1$ $B_x$ order 3.90 at
fourth order on $512^2$ (Table 6). Table 4, meant for third-order RMHD,
repeats Table 3 (hydrodynamics) digit for digit, so the third-order RMHD
accuracy is not documented. Further tests: an RMHD rotor resolution study,
an RMHD blast, a new RMHD vortex–shock interaction, an axisymmetric jet, and
the long-term decay of torsional Alfvén waves. The decay is "almost
imperceptible" at fourth order, with no numbers given. The vortex field is
initialized from $A_z$, so it starts divergence-free.

# Notation map

| Balsara & Kim (2016) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| face-centred $B_x, B_y, B_z$ | $B_h \in V_h^2$ | Yee-type collocation (§4) |
| edge-centred $E_x, E_y, E_z$ | $E_h \in V_h^1$ | from the vertex fluxes of a 2D solver; none of $\mathcal E^{\circ}, \mathcal E^{\alpha}, \mathcal E^{c}$ |
| $F_{\mathrm{num}}, G_{\mathrm{num}}$ (vertex fluxes) | (words) | 2D vertex fluxes, not the 1D base-scheme fluxes $f^{x,*}, f^{y,*}$ |
| $\bar A, \bar B$; $A, B, C$ (Jacobians, eq. 3.1) | (words) | $B$ here is a matrix, $A$ is not $A_h$ |
| $A_z$, $\mathbf A$ (initialization) | $A_h$ | initial data only |
| $\psi$ (similarity variable), $\phi$ (flattener) | (words) | collide with $\psi_h$ and $\phi_h$ |
| $\Delta x, \Delta y$ | $h$ | uniform Cartesian meshes |

# Pages created or updated

* Updated [Staggered grid](/definitions/staggered-grid.md): the necessity position, attributed, in `## Contradictions`.
* Updated [Flux-CT](/methods/flux-ct.md): edge fields from a 2D Riemann solver as a further successor of the averaging step.
* Updated [Upwind constrained transport](/methods/upwind-constrained-transport.md): the finite-volume ADER realization for RMHD.
* Updated [Constrained transport](/methods/constrained-transport.md): production list.

# Citations

1. `~/papers/mosaic/div-free-amr/2016-JCP-Balsara-101016jjcp201602001.pdf` (doi:10.1016/j.jcp.2016.02.001, checked on Crossref: J. Comput. Phys. 312:357–384, May 2016; publisher's Version of Record): text extraction, all sections; eqs. 4.5–4.13 and Table 4 read from the page images. Appendices A (Jacobians) and B (modified RMHD HLLC) read in outline only and not reproduced. Record defects noted: Table 4 duplicates Table 3; the blast test is called fourth and then third order; the flattener's $\phi$ and $\eta$ conventions are opposite and not linked; §3.3 miscounts coefficients. Reference list: 73 entries.

---
type: Source
title: "Dai & Woodward (1998) — On the divergence-free condition and conservation laws in numerical simulations for supersonic magnetohydrodynamic flows"
description: "Argues that Godunov MHD schemes keep either conservation or the divergence constraint but not both, objects to projection, and holds both with face-averaged fields updated by the integral induction law; compares runs with and without that update."
resource: "doi:10.1086/305176"
source_kind: paper
authors: [Dai W., Woodward P.R.]
year: 1998
venue: "Astrophys. J. 494:317-335"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1998-ApJ-Dai-101086305176.pdf"
tags: [constrained-transport, godunov, staggered, projection, mhd, astrophysics]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper argues that existing multidimensional Godunov MHD schemes satisfy
either the eight conservation laws or $\nabla\cdot\mathbf B = 0$, but not
both, except to truncation accuracy, and singles out the Poisson
"clean-up" as nonconservative in energy and field, with O(1) errors at
discontinuities (§1, stated, not tested). The remedy keeps density,
momentum and energy as cell averages and holds each field component as a
face average, advanced by the exact integral induction law with line- and
time-averaged edge values of $\mathbf u\times\mathbf B$ (eqs. 11–23). The
net flux through every cell surface is then conserved exactly (eqs. 15,
23). The field update composes with split or unsplit Godunov schemes
(§2.1, eq. 27). In the example scheme the edge values are four-cell,
two-level averages of the updated cell-centred velocity and field
(eqs. 28–32), the same construction as the companion
[Dai & Woodward (1998, JCP)](/sources/dai-woodward-1998.md).

The distinctive content is a comparison on a Mach-15 shock–cloud problem
with and without the field update: the solutions are "not significantly
different", the largest differences sit where the uncontrolled run has the
largest net cell flux, and the authors conclude that "it is the
conservation laws which play the crucial role" for supersonic flows (§§3–4).

# Key claims

1. **Objection to the clean-up** (§1, p. 317), asserted without a test:
   * the Poisson solve needs global information, "not favored in the
     existing parallel computers";
   * evaluating $\nabla\cdot\mathbf B$ by derivatives "may introduce O(1)
     truncation errors near MHD discontinuities", so the cleaned divergence
     is zero "only to the accuracy of a numerical scheme";
   * "more seriously, the clean-up may destroy the conservative property of
     a Godunov scheme": afterwards the conservation laws for total energy
     and the three field components hold only to truncation accuracy, "and
     truncation errors may be O(1) near MHD discontinuities", easily
     detected for an oblique strong shock.

   The clean-up is credited to Brackbill & Barnes (1980) "for subsonic MHD
   flows" and its Godunov use to Balsara (1996), Ryu et al. (1995) and
   Zachary et al. (1994).
2. **Structural observation** (§2, p. 319; §4): the $B_x$ conservation law
   has no $x$-derivative, which lets eight conservation laws and the
   constraint hold exactly in one set of eight difference equations.
3. **Face averages** (eqs. 11–14). Each field component is the average
   over its face; the cell-centred field is "only intermediate", used for
   the flux calculation; a face average is "well defined even if a
   discontinuity surface … coincides with an interface".
4. **Exact discrete constraint** (eqs. 15–16): a cell is divergence-free
   iff its area-weighted net face flux vanishes.
5. **Face update** (eqs. 17–25). Exact in integral form; the edge values
   are line-and-time averages (eqs. 20–22); per cell the net flux at
   $\Delta t$ equals that at 0 (eq. 23). In 2D the edge values sit at
   corners, and the out-of-plane component equals its cell average and is
   updated by the finite-volume step, not by CT (p. 320).
6. **The field must be updated unsplit** (p. 320): "Although the flow
   variables W may be updated using either a dimensionally split or
   unsplit technique, the magnetic field b should be updated in an unsplit
   manner in order to exactly maintain the divergence-free constraint."
   CT of Evans & Hawley and Stone & Norman also satisfies the condition
   exactly.
7. **Composition** (§2.1, eqs. 26–27): unsplit, field update after the
   Godunov step; Strang split, field update after each triple of sweeps.
   The abstract claims second order in space and time "if the original
   Godunov schemes are".
8. **Cell-centred field** (p. 323): initially the two-face average; then
   advanced by the split sweeps, so it "does not exactly satisfy the
   divergence-free condition" and serves only for the time-averaged fluxes.
9. **1D solver** (pp. 323–324): linear reconstruction; effective
   left/right states per wave family by domain-of-dependence averaging
   (one state for all families would be "only first-order accurate"); an
   approximate Riemann solver for the time-averaged flux.
10. **Edge value, interpolated, not upwinded** (eqs. 28–32). 2D: the
    corner value is $\mathbf u\times\mathbf B$ of the corner velocity and
    field averaged over the old and new time levels, each a plain average
    of the four adjacent cells (eqs. 31–32). The paper calls this "our
    current algorithm".
11. **Divergence-free initial data** (§3, p. 328). In 2D the potential
    follows exactly from the face fluxes; field lines are its contours.
    "The net magnetic flux across each numerical cell is exactly the same
    as its initial value all the time in these simulations"; no value is
    printed.
12. **With versus without the field update** (§3, p. 334, Figs. 12–18):
    "not significantly different, although some differences exist in small
    scales", located near the cloud centre and in the tail shear layer,
    where the uncontrolled run has its largest net cell flux. The authors
    leave open whether truncation-level divergence errors "have serious
    influences on the dynamics if conservation laws are exactly satisfied".
13. **The cell-centred divergence** (§4, p. 334): "interpolation-dependent",
    with maximum magnitude "O(1), no matter what kind of interpolation is
    used" on the problems shown. The net flux computed from the cell
    fields of the proposed scheme is "1 order lower" than without the
    field update (Fig. 19 against Fig. 18). The cell fields "do not
    necessarily have to exactly satisfy the divergence-free condition", by
    analogy with approximate Riemann solvers.
14. **Self-reported limit** (§4, p. 335). In split schemes the three sets
    of interface fluxes come from different instants; "it is not clear
    whether or not an interpolation may be introduced among these three
    sets of time-averaged fluxes … under the second-order accuracy in
    time". A multidimensional Riemann solver at cell corners is suggested.
    *Compiler reading:* this qualifies the abstract's unconditional
    second-order claim for the split scheme actually run (eq. 27).

**Divergence treatment, in sum.** Staggered-face CT-type update; no
projection, no source term, no cleaning. The comparison scheme without the
field update has no divergence control at all, yet conserves all eight
quantities.

# Tests

Uniform grids, $\gamma = 5/3$, Courant numbers "around 0.6", Gaussian
units, the split scheme of eq. 27 with linear reconstruction (§3). No error
norms or convergence orders anywhere.

1. **Linear fast wave at 30°** (Fig. 1): periodic, $128^2$ down to $8^2$,
   $t = 10$; initial state not printed; convergence shown visually.
2. **Nonlinear fast wave** (Fig. 2): $128^2$, $t = 1$–5, steepening into a
   shock.
3. **Rotated shock tubes at 45°** (Figs. 3–5): $256^2$, $t = 0.06$,
   normal field 5 ([rotated shock tube](/benchmarks/rotated-shock-tube.md)).
   45° chosen "only because it is easy to set initial conditions which
   exactly satisfy the divergence-free condition"; the problems are still
   not $x$–$y$ symmetric because of the transverse field. Jump conditions
   satisfied (Fig. 3); "there would be O(1) truncation errors in the jump
   conditions if the scheme were not conservative for any one of eight
   conserved quantities". The normal field is flat at plot scale in Figs.
   3–4 and dips to about 4.99997 in Fig. 5 (axis reading); "the variation
   … is a symptom of truncation errors".
4. **Orszag–Tang vortex** (Figs. 6–7): velocity
   $(-\sin 2\pi y, \sin 2\pi x)$, field $(-\sin 2\pi y, \sin 4\pi x)$,
   $\beta_0 = 10/3$, $M_0 = 1$, $128^2$–$512^2$, $t = 0.5$; qualitative.
5. **Mach-15 shock on a circular cloud** (Figs. 8–9), three grids up to
   $768\times512$, cloud 10× denser.
6. **Mach-12 shock on "MHD"-letter clouds** (Figs. 10–11), density 50 in
   the letters, $512\times384$; robustness.
7. **With versus without the field update** (Figs. 12–19), Mach-15 shock,
   cloud 10× denser, $384\times256$. Density "very hard to find
   differences"; velocity differences near the cloud centre and in the
   tail; $B_x$ "more clean in the tail" with the update; $B_y$ differences
   near the cloud front. **Net cell flux** from the cell-centred field,
   colour-bar ranges: $-2.84\cdot10^{-2}$ to $1.74\cdot10^{-2}$ without the
   update (Fig. 18), $-4.75\cdot10^{-3}$ to $2.75\cdot10^{-3}$ with it
   (Fig. 19); units, normalization and interpolation are not stated.

# Notation map

| Dai & Woodward | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $b_{x,i,j,k}, b_{y,i,j,k}, b_{z,i,j,k}$ | $B_h \in V_h^2$ | the evolved field |
| $B_{i,j,k}$ (cell average) | $B_h^{*}$ | split-updated, not divergence-free |
| eqs. 15–16 | $D_h^{\mathrm f} B_h$ times cell volume | |
| $\Omega \equiv \mathbf u\times\mathbf B$; $\bar\Omega$ (eqs. 20–22) | $-E_h \in V_h^1$, at $n+1/2$ | **sign:** $\Omega = -E$ |
| $D_{\Delta t}$ (eqs. 17–19, 24–25) | $B_h^{n+1} = B_h^n - \Delta t\, C_h E_h^{n+1/2}$ | **collision:** not a divergence |
| $L_{\Delta t}$, $L^x_{\Delta t}$ | words (base-scheme operator) | |
| $A_z$ | $A_h$ | corner-collocated in 2D |
| $\Delta x_i$, $\Delta y_j$, $\Delta z_k$ | $h$ | uniform in all tests |
| $\alpha$ (rotation angle), $\xi$, $\eta$, $B_\xi$ | words; $B_n$ on the benchmark page | **collision:** $\alpha^{\mathrm{LF}}$ |
| $\beta_0$, $M_0$ | words | Orszag–Tang parameters |

# Pages created or updated

* Updated [Flux-CT and the Godunov CT variants](/methods/flux-ct.md): field-interpolated CT from its primary sources.
* Updated [Constrained transport](/methods/constrained-transport.md): unsplit field update with split fluid; the with/without comparison.
* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md): net cell flux of the cell-centred field with and without CT; the open question on dynamics.
* Updated [CT–finite-volume equivalence](/results/ct-finite-volume-equivalence.md): the cell-centred field of field-CT as printed.
* Updated [Staggered grid](/definitions/staggered-grid.md): staggering of the field only.
* Updated [Tóth (2000)](/sources/toth-2000.md): "DW not yet ingested" replaced.
* Updated [Projection method](/methods/projection-method.md): the Open Contradictions entry.
* Updated [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) (the set-up and runs as printed, §§3–4).
* Updated [Rotated shock tube](/benchmarks/rotated-shock-tube.md) (the 45° runs, Figs. 3–5).

# Citations

1. `~/papers/mosaic/div-free-amr/1998-ApJ-Dai-101086305176.pdf`.
   * **Version read.** The published journal version (AAS typeset, 19
     pp.). Received 21 October 1996, accepted 4 September 1997.
   * **Identity.** doi:10.1086/305176, checked on Crossref: authors match;
     vol. 494, issue 1, pp. 317–335, issued 10 February 1998; reference
     count 27. Crossref spells the last word of the title
     "Magnetohydrodynamical"; page 1 prints "magnetohydrodynamic".
   * **How it was read.** The text layer is OCR-like with ligature damage;
     all equations were read from rendered pages (pp. 318–323, 325, 326,
     328, 333, 334).
   * **Recorded as printed.**
     * The §1 section plan does not match the printed headings (§2
       conservation laws, §2.1 schemes, §3 examples, §4 conclusions); this
       page uses the printed headings.
     * Eq. 30 prints $\Omega_y$ on the right for the $z$-edge value,
       presumably $\Omega_z$ (reader's reading).
     * Eq. 20 averages over $x_i<x<x_{i+1}$ while p. 326 defines the line
       average over $x_{i-1}<x<x_i$; not resolved.
     * The edge-averaged field of eqs. 28–30 is not defined explicitly,
       and no 3D stencil is printed.
     * Whether the cell-centred field is re-synchronised to the face
       average every step or only at $t = 0$ is not stated (p. 323).
     * The text cites "Colella (1994)", "Stang 1968" and "Evan & Hawley";
       the list has Colella 1990, Strang 1968, Evans & Hawley. The in-text
       labels 1994c and 1995 of Dai & Woodward appear swapped against the
       list.
   * **Reference list.** 27 entries, all merged (ApJ style, titles not
     printed except one book). The "1994c" printed "ApJ, 776, 436" is ApJ
     436:776 on Crossref; Stone & Norman printed "ApJ 80:791" is ApJS
     80:791. Bibliography key renamed `dai-1998` → `dai-woodward-1998-b`.
     The bibliography holds 3711 entries after this batch.

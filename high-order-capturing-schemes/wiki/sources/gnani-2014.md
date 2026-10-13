---
type: Source
title: "Gnani, Lo, Zare-Behtash & Kontis (2014) — Experimental investigation on shock wave diffraction over sharp and curved splitters"
description: "High-speed schlieren sequences of weak shocks (M_s = 1.31 and 1.59) diffracting over three splitter tips in a small square shock tube: sharp ramp and symmetric wedge behave alike, a rounded tip moves separation downstream, damps the Kelvin–Helmholtz instability and keeps the contact surface from rolling up, and lambda shocklets on the shear layer appear only at 1.59. Qualitative experiment, no simulation."
resource: "doi:10.1016/j.actaastro.2014.02.018"
source_kind: paper
authors: [Gnani F., Lo K.H., Zare-Behtash H., Kontis K.]
year: 2014
venue: "Acta Astronaut. 99:143–152"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2014-ActaAstronaut-Gnani-101016jactaastro201402018.pdf"
tags: [2d, vortex-sheet, mach-reflection]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A purely experimental paper, with no equations and no simulation. A
planar shock leaves a small square shock tube and diffracts around the tip
of a splitter plate; high-speed schlieren records six frames per run.
Three tips are tested: a sharp one-sided ramp (tip angle 172°), a sharp
symmetric wedge, and a rounded tip of radius 2.8 mm, each at
$M_s = 1.31$ and $1.59$. The flow features are identified and labelled:
diffracted shock, expansion wave, contact surface, vortex,
Kelvin–Helmholtz vortices on the shear layer, lambda shocklets, and the
splitting of the wall-reflected diffracted shock into left- and
right-hand shocks around the vortex. The findings are qualitative, and the
authors note that waves reflected from the walls of the small test section
contaminate the late flow (§4). It is a low-$M_s$ variant related to the
[corner-diffraction benchmark](/benchmarks/shock-diffraction.md), not the
same configuration.

# Key claims

1. **Sharp ramp and symmetric wedge are equivalent** (§3.2, §4): the
   two "behave in a similar manner and can be categorised as sharp
   wedges"; the structures "appear to be identical and in the same
   position at the same time" (Figs. 4 vs 7, 5 vs 9).
2. **Lambda shocklets only at $M_s = 1.59$** (§3.1, Fig. 5; §3.2,
   Fig. 7; §4). A train of small lambda shocks forms on the outer side of
   the slipstream from the tip and ends about 90° around the vortex. At
   $M_s = 1.31$ there are none, which the authors read as subsonic flow
   along the slipstream. This is consistent with the literature thresholds
   restated in §1 (Skews et al.: a lambda structure for $M_s \ge 1.35$).
3. **Kelvin–Helmholtz vortices** (§§3.1–3.3, §4). On the sharp ramp at
   $M_s = 1.31$ they appear from the tip to about 120° around the vortex,
   later between 90° and 270°, and are fully damped at 360 µs. On the
   symmetric wedge they start later and are more damped. On the rounded
   tip none develop: the thicker curved-tip shear layer "has a dampening
   effect".
4. **Reflected diffracted shock and vortex** (§3.1, Fig. 6). The
   diffracted shock reflects from the upper wall of the test section and
   returns to the vortex, splitting into an accelerated left-hand and a
   decelerated right-hand shock; the right-hand shock forms a Mach
   reflection on the slipstream with an extra stem. At $M_s = 1.59$ the
   interaction is the "strong vortex–strong shock" type of Chang & Chang,
   with the shock transmitted through and distorting the vortex; at 1.31 it
   does not displace the vortex (§4).
5. **Rounded tip** (§3.3, Figs. 10–13). Separation occurs downstream of
   the onset of curvature, at a distance only "roughly estimated" and
   "greater for a higher Mach number"; the expansion fan is not centred
   (after Skews). A convergent–divergent passage between the wall and the
   shear layer accelerates the flow and produces an internal shear layer;
   at $M_s = 1.59$ an internal terminator, a secondary internal shock and a
   recompression shock appear about 90° around the vortex and vanish as
   the vortex leaves the corner. The contact surface does not roll up into
   the vortex but ends on the splitter wall (agreeing with Skews).
6. **Effect of $M_s$** (abstract, §3.1). At 1.59 the flow evolves faster
   and with stronger structures; the vortex grows faster, is stretched
   horizontally, rotates counter-clockwise and turns turbulent earlier.
7. **Literature regime map restated** (§1, attributed, not new data).
   Perturbed region subsonic for $M_s < 2.068$ (Skews et al.); separation
   for wedge angles above 20°; a limiting configuration above a critical
   corner angle of 75°; a terminator for $M_s$ = 1.6–1.87; no new features
   above $M_s = 3.0$; Lighthill's linear theory predicting the inflexion
   point of the diffracted shock; no triple point for corner angles of
   120°–170° (Bazhenova et al.).

# Tests

All experimental.

**Facility** (§2.1). Square shock tube, internal side 24.8 mm, wall
2.6 mm; driver 700 mm, driven section 1750 mm; driven gas at ambient
conditions (the species is not named); acetate diaphragms of 19 µm
($M_s = 1.31$) and 75 µm ($M_s = 1.59$), ruptured by a plunger. Reynolds
numbers based on the duct side: $1.08\times10^6$ and $1.68\times10^6$.
How $M_s$ was measured is not described.

**Models** (Fig. 3). Splitter plates 5.63 mm thick: (a) ramp, tip angle
172°; (b) symmetric wedge; (c) rounded tip, radius 2.8 mm. The optical
section is 55.23 mm high, with the model's lower surface 24.8 mm above
the lower window edge. The spanwise extent is not stated.

**Diagnostic** (§2.2). Z-type schlieren, Photron SA1.1 camera at
16,800 frames per second, 1 µs exposure; a wind-off reference image is
subtracted. Time zero is the frame before the shock reaches the tip.

**Runs.** Six frames each, at 60, 120, 180, 240, 300 and 360 µs: ramp
at 1.31 (Fig. 4) and 1.59 (Fig. 5, schematic Fig. 6); symmetric wedge at
1.31 (Fig. 7) and 1.59 (Fig. 9); rounded tip at 1.31 (Fig. 10) and 1.59
(Fig. 12, schematics Figs. 11, 13).

**Use as benchmark data.** Only qualitative: feature positions at fixed
times for a specified geometry and two values of $M_s$, which a numerical
schlieren of a 2D simulation could be compared with frame by frame. No
triple-point trajectory, vortex-centre position or pressure history is
reported; the gas and initial state are not stated; and a simulation would
have to include the confining walls, since the wall-reflected diffracted
shock is a central feature of the reported interaction.

# Notation map

| Gnani et al. (2014) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $M$ (incident shock Mach number) | $M_s$ | registry $M$ is the TVB constant |
| Reynolds number | $\mathrm{Re}$ | based on the duct side, 24.8 mm |
| $\Delta$ (separation distance, rounded tip) | words | never quantified |
| $R$ (tip radius) | words | $R$ is the right-eigenvector matrix |
| IS, DS, ES, CS, V, TL, KH, LHS, RHS, S, InT, SInS, RS | words | figure labels, not symbols |

# Pages created or updated

* Updated [Shock diffraction at a backward-facing corner](/benchmarks/shock-diffraction.md) (low-$M_s$ diffraction over sharp and rounded splitter tips as a related variant, qualitative).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/2014-ActaAstronaut-Gnani-101016jactaastro201402018.pdf`.
   * **Version.** The published version of record (Elsevier, open access,
     CC BY 3.0); received 21 November 2013, accepted 21 February 2014,
     online 27 February 2014.
   * **Identity.** doi:10.1016/j.actaastro.2014.02.018, printed on page 1
     and checked on Crossref: Acta Astronautica 99:143–152, June 2014,
     authors Gnani, Lo, Zare-Behtash, Kontis (University of Glasgow).
   * **How it was read.** Text extraction, all sections; the geometry
     (Fig. 3) and schlieren sequences (Figs. 4, 5, 7, 9, 10, 12) checked on
     rendered pages. Features were taken from the authors' labels, not
     re-identified on the low-resolution images.
   * **Recorded as printed.** The symmetric wedge's tip angle is 172° in
     the abstract, §1 and §4, but Fig. 3(b) labels it 176°; the text does
     not resolve which is right.
   * **Reference list:** 28 entries, all merged (Crossref deposits 28).
     Bazhenova et al. (Acta Astronaut. 6:401), printed 1977, is 1979 on
     Crossref and keyed `bazhenova-1979`. Ref. [3] prints "sock wave" in
     its title (kept). Ref. [13] (Jones, Proc. Camb. Philos. Soc. 53) is
     entered as a journal article. Ref. [24] is the existing
     `anderson-1990`. Góngora-Orozco is keyed `gongoraorozco`. No DOIs are
     printed. Skews (1967) and Bazhenova et al. (1984) are shared with
     [Kleine et al. (1995)](/sources/kleine-1995.md).

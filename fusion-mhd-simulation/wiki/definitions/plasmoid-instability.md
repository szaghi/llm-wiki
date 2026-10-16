---
type: Definition
title: "Plasmoid instability and plasmoid-mediated reconnection"
description: "Break-up of a thin current sheet at high Lundquist number into chains of plasmoids that make resistive reconnection fast; in nonlinear NIMROD simulations of peeling-ballooning ELMs, axisymmetric counter-current sheets and finger-like edge current sheets form and the latter break into current blobs read as 3D plasmoid-mediated reconnection."
status: established
aliases: [plasmoid-mediated reconnection, current-sheet break-up, reconnection burst, plasmoid chain]
tags: [elm, edge, pedestal, mhd, extended-mhd, tearing]
timestamp: 2026-10-16T20:00:00Z
---

# Plasmoid instability and plasmoid-mediated reconnection

A current sheet in a resistive plasma reconnects slowly when it is
Sweet–Parker-like. Above a critical Lundquist number $S$ the sheet itself
becomes unstable: it breaks into a chain of plasmoids (magnetic islands in
2D, flux ropes in 3D) that grow on Alfvénic time scales, and the
reconnection rate becomes fast and nearly independent of $S$. This is the
plasmoid instability. [Ebrahimi & Bhattacharjee (2023)](/sources/ebrahimi-2023.md)
(p. 1) state it in this form, attribute the theory to the cited
literature (Biskamp 1986, Loureiro 2007, Bhattacharjee 2009, Huang 2013 and
others), and give no equation for the critical $S$ or the rate.

They separate two classes of reconnection (p. 1):

- **forced or driven reconnection**, where oppositely directed fields are
  brought together by an external or a primary perturbation, so that the
  reconnection is secondary to it;
- **spontaneous reconnection**, which comes from an instability of the
  current distribution itself: the [tearing mode](/definitions/tearing-mode.md),
  and at high $S$ the plasmoid chains of a thin sheet.

The term is unrelated to the "plasmoid" of pellet physics, the ionized
ablation cloud whose $E\times B$ drift toward the low-field side is studied
in the shattered-pellet sources
([plasmoid drift](/definitions/plasmoid-drift.md);
[shattered pellet injection](/definitions/shattered-pellet-injection.md)).

## Plasmoids in peeling–ballooning ELMs (NIMROD)

Ebrahimi & Bhattacharjee (2023) simulate peeling–ballooning
[edge-localized modes](/definitions/edge-localized-mode.md) in two
reconstructed DIII-D equilibria with [NIMROD](/software/nimrod.md). Case A
uses resistive MHD with Spitzer resistivity from the toroidally averaged
temperature, which the paper calls a realistic Lundquist number, and 43
toroidal modes; case B (DIII-D 145701) uses a uniform diffusivity with
$S\sim10^5$ (p. 2, Figs. 1–6). The sequence is:

1. **Linear phase.** Intermediate-$n$ ballooning modes ($n=10$–14) grow;
   low-$n$ peeling-parity modes ($n=1$–6), stated to be linearly stable,
   and $n\ge20$ grow by nonlinear coupling (Fig. 2a).
2. **Secondary growth ("reconnection burst").** After the first saturation,
   several peeling–ballooning modes grow sharply again at about
   1.6–1.7 ms. Axisymmetric ($n=0$) poloidal fields form; the paper calls
   them nonlinear peeling–ballooning structures made locally coherent and
   zonal, and attributes them to the electromotive force of the modes
   themselves (Fig. 2c).
3. **Two types of current sheet** (p. 3, Fig. 3a).
   - *Type 1:* a poloidally extended axisymmetric toroidal current sheet,
     driven by the zonal fields through Ampère's law. Its sign is opposite
     to the equilibrium edge current, so it removes the free energy (edge
     current) of the peeling drive. On the low-field side the peeling–
     ballooning modes break it during the secondary growth.
   - *Type 2:* finger-like non-axisymmetric current sheets extending
     radially and vertically in and out of the scrape-off layer. As the
     modes saturate they break into small-scale current blobs, which the
     paper calls plasmoids. Pressure fingers carry current.
4. **Relaxation.** The edge pressure broadens, the blobs decay and the
   current relaxes to a mostly axisymmetric profile near 2 ms; a second
   burst follows at about 2.3–2.6 ms (Figs. 2b, 3b–c).

The toroidally averaged fluctuation electromotive force, the toroidal
component of $(\tilde{\mathbf v}\times\tilde{\mathbf B})^{(0)}$ (toroidal average
of the product of the non-axisymmetric parts, registry §11) evaluated from the
Fourier amplitudes, has a bi-directional poloidal
pattern consistent with the $n=0$ counter-current (case B, Fig. 6d; the
average here is toroidal, not flux-surface). No quantitative balance between
this term and the evolution of the $n=0$ current is given; the same quantity
enters the axisymmetric balance on [MHD dynamo](/definitions/mhd-dynamo.md). A two-fluid run
(Hall and electron-inertia terms in Ohm's law, $S\sim5\times10^4$, 86 modes)
shows poloidal flow vortices at about the poloidal Alfvén speed, about
14 km/s; whether they come from local reconnection or from Maxwell and
Reynolds stresses is left open (p. 4, Fig. 5).

## Qualifications

- **Identification rests on snapshots.** The blobs are identified as
  plasmoids from current-density snapshots alone; no island, flux,
  reconnection-rate or convergence diagnostic is given (Source page).
- **No Lundquist scan.** The abstract states that the sheets break "at high
  Lundquist numbers", but the three runs differ in $S$ and in model, so no
  $S$-dependence is isolated (Source page, claim 13).
- **Version.** The paper was read as arXiv v1 (single author, 2021); the
  published Nucl. Fusion version has two authors and may differ.
- **Cycles.** The "two ELM cycles" of case A are two bursts within about
  1 ms without described heating or current sources, not pedestal-recovery
  cycles; see the qualification on
  [edge-localized modes](/definitions/edge-localized-mode.md).
- **Sign conventions.** The printed curl and electromotive-force components
  imply different orientations of $\phi$; the sign of the emf is not to be
  used quantitatively (Source page).

## Contradictions

None open.

# Citations

- [Ebrahimi & Bhattacharjee (2023)](/sources/ebrahimi-2023.md) — pp. 1–5, Eqs. 1–6, Figs. 1–6.

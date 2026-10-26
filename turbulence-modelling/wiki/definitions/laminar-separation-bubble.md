---
type: Definition
title: "Laminar separation bubble"
description: "A closed region of reversed flow formed when a laminar boundary layer separates under an adverse pressure gradient, transitions in the detached shear layer and reattaches turbulent; its signatures, unsteadiness and frequencies in scale-resolving simulations, and why RANS transition models struggle to size it."
status: established
aliases: [LSB, separation-induced transition, laminar separation, transitional separation bubble]
tags: [transition, separated-flow, boundary-layer, rans, implicit-les, turbomachinery]
timestamp: 2026-10-26T07:38:00Z
---

# Laminar separation bubble

A laminar separation bubble (LSB) forms when a laminar boundary layer meets
an adverse pressure gradient strong enough to separate it before transition.
The detached shear layer becomes unstable, transitions to turbulence and,
energized by the turbulent mixing, reattaches to the wall, enclosing a
region of recirculating flow. Transition triggered this way is
*separation-induced transition*, one of the three routes, with natural and
bypass transition, that the
[local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)
are built to cover ([Menter et al. (2022)](/sources/menter-2022.md), §1).
Slaughter et al. (2023) describe the sequence in a scale-resolving
simulation as laminar separation under the adverse pressure gradient,
Kelvin–Helmholtz roll-up of the separated shear layer, bursting, and
ejection of low-momentum fluid into the free stream; following Serdar et
al., as they recall, "LSBs are amplifiers of other instabilities"
([Slaughter et al. (2023)](/sources/slaughter-2023.md), §4.1, §4.3;
Research Square preprint v1).

Bubbles of this kind govern three of the bundle's cases: airfoils at chord
Reynolds numbers $Re_c=2\times10^4$–$2\times10^5$ (Carreño Ruiz &
D'Ambrosio 2022), the suction side of a low-pressure-turbine blade at an
exit Reynolds number of $9\times10^4$ (Morsbach et al. 2024), and the
elements of a multi-element wing in ground effect at
$Re=2.2\times10^5$ (Slaughter et al. 2023).

## Signatures

- **Pressure plateau.** The bubble shows as a plateau in the surface
  pressure followed by a recovery at reattachment. On the T161 turbine
  cascade the plateau lies between $x/C_{ax}=0.7$ and 0.9 of the axial chord
  ([Morsbach et al. (2024)](/sources/morsbach-2024.md), §4.1, Fig. 7). On the
  inverted wing the pressure decreases monotonically along the suction sides
  except on the mainplane between $x/c=0.50$ and 0.65 (Slaughter et al.
  2023, §4.1, Fig. 7).
- **Skin friction and topology.** The skin friction is negative in the
  bubble. Slaughter et al. bound each bubble by two bifurcation lines of a
  line-integral convolution of the wall shear (§4.1, Figs. 6, 9–10); on the
  mainplane the boundary-layer profiles show an inflection near
  $x/c\approx0.4$ and reversed flow up to $x/c\approx0.5$, the reversed
  region extending to $y/c\approx0.001$ from the wall (Fig. 12).
- **Transition location.** Carreño Ruiz & D'Ambrosio (2022) take the
  transition point as the location where the skin friction starts to drop,
  between separation and reattachment
  ([Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md), §3.5).
  Slaughter et al. see two-dimensional Tollmien–Schlichting-type waves at
  the start of the mainplane bubble breaking down quickly to turbulence,
  the exact route being unclear (§4.3, Fig. 22b).
- **Thickness and adverse pressure gradient.** A strong adverse pressure
  gradient "thins" the bubbles on the mainplane and first flap; the bubble
  on the ground plane under the wing is larger and thicker (Slaughter et
  al. 2023, §4.1). At very low Reynolds number a thicker bubble raises the
  effective camber, so the lift curves near first reattachment lie above
  those of higher Reynolds numbers (Carreño Ruiz & D'Ambrosio 2022, §6.1,
  Fig. 17).

## Unsteadiness and frequencies

In the implicit LES of the Imperial Front Wing slice, the surface-pressure
variance is largest in and around the bubbles, with the maximum of
$\mathrm{RMS}(C_p)-\overline{C_p}$ at $x/c\approx0.55$ on the mainplane and
$0.61$ on the first flap (Slaughter et al. 2023, §4.3, Fig. 14). The
pressure spectrum at the mainplane maximum "coincides perfectly" with the
peaks of the element lift spectra at $St=60$, 140 and 200; since there is
almost no pressure fluctuation upstream, the authors infer that "the LSB is
causal of these pressure fluctuations" on the mainplane, while on the first
flap upstream fluctuations prevent the inference, although the frequencies
of the two bubbles are "locked" (§4.3, Fig. 15).
The second flap shows no suction-side bubble; the authors attribute this to
"wake transition", a bypass transition caused by the wakes of the upstream
elements (§4.1, Fig. 11; see
[Imperial Front Wing](/benchmarks/imperial-front-wing.md)).

At very low Reynolds number the bubble can couple to vortex shedding. On
the SD7003 at $Re_c=23{,}000$, $\alpha=2^\circ$, unsteady RANS with trailing-edge
shedding raises the mean lift by 22.8% over the steady solution, and near
bubble bursting the RANS either settles or keeps shedding whose time
average is a closed bubble (Carreño Ruiz & D'Ambrosio 2022, §5, Table 11).

## Prediction with RANS transition models

Correlation-based transition models size the bubble through the production
of $k$ in the separated shear layer. Both RANS sources find this the
weak point; details of the models are on the
[transition-model page](/methods/local-correlation-based-transition-model.md).

- **Separation-induced corrections.** The $\gamma$-$Re_\theta$ model lets
  the intermittency exceed one in separated regions, through
  $\gamma_{\mathrm{sep}}$, and γ-alg-SST through a bubble term, an
  "obviously unphysical enhancement" that compensates the slow response of
  the two-equation turbulence model (Menter et al. 2022, §2, Eqs. 13–18;
  Carreño Ruiz & D'Ambrosio 2022, §2, Eqs. 5–6). Without the bubble term
  the Eppler 387 bubble at $Re=10^5$ is far too large and lift drops at
  $4^\circ$–$8^\circ$; the one-equation γ-SST overpredicts bubble size at low
  Reynolds number on Eppler 387 and Pak-B (Menter et al. 2022, Figs. 4–5,
  10, 16–19, 24).
- **Airfoils.** On SD7003 at $Re_c=60{,}000$, $\alpha=4^\circ$, the best
  calibration places separation, transition and reattachment at 0.202,
  0.518 and 0.660 chords against 0.23, 0.55 and 0.65 of the reference LES;
  after reattachment the skin friction stays too low, which can cause early
  stall, and at $Re_c=30{,}000$, $\alpha=8^\circ$ no calibration reattaches while
  the LES does at $x/c=0.53$ (Carreño Ruiz & D'Ambrosio 2022, Tables 5,
  7, §7).
- **Turbine cascade.** With the measured inflow turbulence, both SST and the
  SSG/LRR-$\omega$ Reynolds-stress model coupled to $\gamma$-$Re_\theta$ fail
  to reproduce the midspan pressure plateau: separation slightly delayed,
  premature reattachment, a very thin bubble; the mixed-out wake loss is
  underestimated by 35% and 29%. Reducing the inflow length scale to
  $1/16.7$ of its specified value, which the authors call "common practice",
  lowers the free-stream turbulence so much that the flow separates early
  and does not reattach before the trailing edge, yet the wake loss comes
  within 2.7% of the LES, "a lucky cancellation of errors" (Morsbach et al.
  2024, §4.1, Figs. 4, 7–9). The authors conclude that separation-induced
  transition is not predicted and that tuned transition-model versions or
  laminar-kinetic-energy models may be needed (§5).

Both RANS sources find the bubble extent, and with it the
post-reattachment recovery, mispredicted. Carreño Ruiz & D'Ambrosio
tune the coefficient $s_1$ (page-local) of the separation-induced correction and propose a second
parameter for it, which they do not implement (§4, §7); Morsbach et al. suggest tuned transition-model
versions or laminar-kinetic-energy models (§5). The cases differ (airfoils
against a turbine cascade), and no source of the bundle tests both remedies
on one case.

## Resolution in scale-resolving simulation

Wall-resolved LES resolves the bubble directly but is sensitive to
resolution downstream of transition. On the T161 cascade the 6th-order DG
implicit LES (189 million degrees of freedom) captures the plateau and the
base-pressure recovery; a coarser mesh (67.9 million) gives the same blade
loading but a skin friction that differs downstream of the transition
peak, "indicating that the resolution on the coarse mesh is not entirely
sufficient" (Morsbach et al. 2024, §3.1, §4.1, Fig. 7). In the LES the
transitional separated shear layer carries nearly one-component turbulence,
which becomes nearly isotropic after transition; the Reynolds-stress model
misses this (§4.2, Fig. 15). The structures over the bubble dominate the
wake turbulence near midspan (§4.2, Fig. 12). Slaughter et al. check
resolution by the first quadrature point inside the high-order elements
($y^+$ slightly above one only in two small mainplane regions) and by the
spanwise Fourier modal energy, with no grid-convergence study (§3.6, Figs.
4–5; see [Nektar++](/software/nektar-plus-plus.md) and
[implicit LES](/definitions/implicit-les.md)).

## Qualifications

- Slaughter et al. print the pressure coefficient as "$C_p=\frac12\rho V^2$"
  (§4.1, manuscript p. 9), the dynamic pressure, without the numerator $p-p_\infty$
  *(compiler check, not in the sources)*. They also locate bubbles on "the suction side of both the first and
  second flaps" (p. 11), while the rest of the paper places them on the
  mainplane and first flap and finds none on the second flap's suction side.
  Their conclusions tie a mode at $St=30$ on the second flap to its
  pressure-side bubble (§6), whereas §4.3 attributes energy at $St=10$–$20$
  to it; $St$ is not defined.
- Morsbach et al. tune the RANS inflow turbulence to reproduce the decay of
  the LES, not of the experiment, so that LES–RANS differences can be
  attributed to modelling (§3.3); the LES itself decays faster than the
  experiment by design (reduced length scale).

# Citations

- [Slaughter et al. (2023)](/sources/slaughter-2023.md) — §3.6 Figs. 4–5, §4.1 Figs. 6–7, 9–12, §4.3 Figs. 14–15, 22, §6 (Research Square preprint v1).
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §3.1, §3.3, §4.1 Figs. 4, 7–9, §4.2 Figs. 12, 15, §5.
- [Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md) — §2 Eqs. 5–6, §3.5 Tables 5, 7, §4, §5 Table 11, §6.1 Fig. 17, §7.
- [Menter et al. (2022)](/sources/menter-2022.md) — §1, §2 Eqs. 13–18, Figs. 4–5, 10, 16–19, 24.

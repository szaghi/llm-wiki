---
type: Benchmark
title: "Imperial Front Wing"
description: "The Imperial Front Wing, a three-element inverted race-car wing in ground effect proposed as an open motorsport benchmark; a spanwise-periodic slice at Re 220,000 and ride height 0.36 chords, computed by stabilized spectral/hp implicit LES, shows laminar separation bubbles and wake-induced transition that lower-fidelity models must reproduce."
status: established
aliases: [IFW, Imperial front wing, inverted multi-element wing in ground effect]
tags: [benchmark, implicit-les, spectral-element, transition, separated-flow]
timestamp: 2026-10-26T07:40:00Z
---

# Imperial Front Wing

The Imperial Front Wing (IFW) is a three-element inverted wing (mainplane,
flap 1, flap 2) derived from an unraced front-wing specification of a
Formula One car (McLaren MP4-17D), operating close to a moving ground.
[Slaughter et al. (2023)](/sources/slaughter-2023.md) propose it as an open
benchmark for motorsport aerodynamics, a field without public test cases,
organized as a hierarchy of configurations of growing complexity whose data
would calibrate RANS, transition and reduced-order models; earlier
experiments (Pegrum; Buscariolo et al.) and computations on the full wing
covered only time-averaged and integral quantities (§1, §2.1). The first
level, and the only one computed so far in this bundle, is a slice of the
wing extruded in span: a multi-element aerofoil in ground effect whose
boundary layers are transitional, so the case tests the prediction of
[laminar separation bubbles](/definitions/laminar-separation-bubble.md),
wake-induced transition and the unsteady interaction of the elements.

## Configuration

From [Slaughter et al. (2023)](/sources/slaughter-2023.md), §2.1 and
§3.2–3.6 (read in the Research Square preprint v1):

- slice at $Y=250$ mm of the IFW CAD, extruded spanwise; mainplane chord
  $c=0.25$ m; ride height $h/c=0.36$ (page-local $h$, set from the
  footplate of the full wing);
- incompressible flow at $Re=2.2\times10^5$ on $c$ and the free-stream
  velocity; Dirichlet velocity $U_\infty$ on floor and ceiling (a moving
  ground), no-slip wing, convective outflow;
- domain about $10c$ upstream, 28 chords downstream, $10c$ tall (about 5%
  blockage); span $0.16c$ (0.04 m), periodic, 64 Fourier modes;
- [Nektar++](/software/nektar-plus-plus.md) Fourier spectral/hp element
  method: 2D spectral/hp elements in the plane with polynomial degree 6 for
  velocity and 5 for pressure, velocity-correction splitting, second-order
  implicit–explicit time stepping;
- no SGS model ([implicit LES](/definitions/implicit-les.md)): gradient-jump
  penalization in the plane (see
  [jump-penalty stabilization](/methods/jump-penalty-stabilization.md)) and
  [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
  with an exponential kernel in the Fourier direction;
- boundary-layer mesh of 10 curved layers (growth 1.4) on the elements and 5
  on the floor, three wake-refinement regions; first quadrature point at
  $y^+<1$ except two small mainplane regions where it is "slightly above
  one";
- time step $1.6\times10^{-6}$ in convective units, a transient of about 40
  and averaging over 8 convective units; forces and surface pressure sampled
  every 10 steps.

The spanwise modal energy falls to $10^{-7}$ of the mean mode before the
SVV cutoff, and the lift varies by about 5% over "a large range of spanwise
lengths" (data not shown), which the authors take as adequate span and
spanwise resolution; no grid-convergence study in the plane and no
comparison with experiment is made (§3.3, §3.6).

## What the case shows

**Forces and pressure.** The time-averaged coefficients are
$C_L=-8.33$ (downforce) and $C_D=0.17$ (§4.2). The suction peak of $C_p$
is about $-11$ at the mainplane leading edge; the authors call flap 2
"seemingly misaligned" with the local flow, its stagnation point lying away
from the leading edge (§4.1, Fig. 7).

**Laminar separation bubbles and wake transition.** Laminar separation
bubbles sit on the suction sides of the mainplane and flap 1, thinned by the
strong adverse pressure gradient, on the floor (larger and thicker) and on
the pressure side of flap 2; each is bounded by two bifurcation lines of the
surface shear-stress pattern. The suction side of flap 2 has none, which the
authors attribute to a bypass ("wake") transition driven by the wakes of the
upstream elements (§4.1, Figs. 6, 9–11). On the mainplane the profile has an
inflection near $x/c=0.4$ and reversed flow until about $0.5$; the bubble
shows Kelvin–Helmholtz roll-up, bursting and ejection of low-momentum fluid,
and two-dimensional Tollmien–Schlichting waves at its onset break down
quickly (§4.1, §4.3, Figs. 12, 17, 22).

**Frequencies locked between elements.** The lift spectra show narrowband
peaks at $St=60$ on all elements, $140$ and $200$ on the mainplane, $40$ on
all elements (strongest on flap 1) and $30$ on flap 2 only (§4.2, Fig. 13).
The surface-pressure spectrum at the maximum-rms point inside the mainplane
bubble "coincides perfectly" with the lift peaks at 60, 140 and 200, and
since upstream pressure fluctuations are almost absent the authors infer that
the bubble causes them; mainplane and flap-1 lift are in phase at $St=40$
and out of phase at $St=60$ (§4.3, Figs. 15–16). The paper draws the
inference from the coinciding peaks and the quiet upstream signal; it
computes no stability analysis.

**Wake.** The wake meanders about one chord behind flap 2 and breaks up a
few chords downstream through a Kelvin–Helmholtz-type instability; three
turbulent-kinetic-energy peaks persist at $x/c=2$, the maximum falls from
0.012 at $x/c=2.5$ to 0.008 at 4 and rises by 50% at $x/c=6$, which the
authors attribute to production by the Kelvin–Helmholtz mode without a
computed budget (§4.3, Figs. 21, 23–24). The floor shear layer shows no
visible interaction with the wake within a few chords.

## Qualifications

- The Strouhal number is never defined (Figs. 15 and 20 use frequency per
  convective time unit, compared in the text as the same $St$), and the
  non-dimensional time uses a "characteristic length" not stated to be $c$.
  With the printed time step, sampling every 10 steps over 8 convective
  units gives $5\times10^5$ samples, against the "roughly 35,000 samples" of
  the cross-spectral analysis *(compiler check, not in the sources)*; the
  paper does not reconcile the two.
- The preprint prints the pressure coefficient as "$C_p=\tfrac12\rho V^2$"
  (the dynamic pressure) and the turbulent kinetic energy as half the sum of
  the mean fluctuations, not of their squares, while the text says "half the
  sum of the variances" (§4.1, §4.3). §6 attributes $St=30$ to the flap-2
  pressure-side bubble, §4.3 attributes energy at $St=10$–20 to it.
- The span of $0.16c$ is chosen small on purpose: the authors found a
  far-wake spanwise length scale by autocorrelation and set it aside as of
  less interest, judging such wake-breakdown modes "unlikely to exist in
  reality" (§3.3); the lift sensitivity to the span is reported without
  data.
- The open release of the data set is announced, not part of the paper
  (§5).

# Citations

- [Slaughter et al. (2023)](/sources/slaughter-2023.md) — §1; §2.1; §3, §3.1–3.6, Figs. 1–5; §4.1–4.3, Figs. 6–24; §5–6.

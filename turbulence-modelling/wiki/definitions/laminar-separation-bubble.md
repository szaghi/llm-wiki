---
type: Definition
title: "Laminar separation bubble"
description: "A closed region of reversed flow formed when a laminar boundary layer separates under an adverse pressure gradient, transitions in the detached shear layer and reattaches turbulent; its signatures, unsteadiness, role in dynamic stall and shock interactions, and why RANS and hybrid transition models struggle to size it."
status: established
aliases: [LSB, separation-induced transition, laminar separation, transitional separation bubble]
tags: [transition, separated-flow, boundary-layer, rans, implicit-les, turbomachinery]
timestamp: 2026-10-28T06:46:00Z
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
ejection of low-momentum fluid into the free stream, and, citing Serdar et
al., state that "LSBs are amplifiers of other instabilities"
([Slaughter et al. (2023)](/sources/slaughter-2023.md), §4.1, §4.3;
Research Square preprint v1).

Bubbles of this kind govern several of the bundle's cases, among them airfoils at chord
Reynolds numbers $Re_c=2\times10^4$–$2\times10^5$ (Carreño Ruiz &
D'Ambrosio 2022), the suction side of a low-pressure-turbine blade at an
exit Reynolds number of $9\times10^4$ (Morsbach et al. 2024), and the
elements of a multi-element wing in ground effect at
$Re=2.2\times10^5$ (Slaughter et al. 2023).

## Signatures

- **Pressure plateau.** The bubble shows as a plateau in the surface
  pressure followed by a recovery at reattachment. On the T161 turbine
  cascade the plateau lies between $x/c_{ax}=0.7$ and 0.9 of the axial chord $c_{ax}$ (registry §11)
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
  the exact route being unclear (§4.3, Fig. 22b). Sandberg & Michelassi
  (2022) describe the separated-flow route as Kelvin–Helmholtz roll-up of the
  separated shear layer followed by secondary instability, with
  Tollmien–Schlichting waves possibly dominant at large Reynolds number and
  small adverse pressure gradient (citing Hatman & Wang 1999) and a
  three-dimensional absolute instability of two-dimensional shedding
  (citing Jones et al. 2008) as a further path
  ([Sandberg & Michelassi (2022)](/sources/sandberg-2022.md), §3.3.3).
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

**Wake passing.** In turbomachinery the incoming wakes of the upstream row
make the bubble periodic. Sandberg & Michelassi (2022) cite the LES of a
low-pressure-turbine stage by Pichler et al. (2017a) at an isentropic exit
Reynolds number of $10^5$: once the wake apex passes the separation point,
the separation and reattachment points move downstream at roughly one half
and one quarter of the local isentropic velocity, and the bubble disappears
for about 25% of the time (§3.3.3.4, Fig. 6). The stakes are large: changing
the leading-edge geometry, and with it the bubble, changed the overall
blade loss by up to 30% (citing Wheeler et al. 2009; §3.3.2). See
[turbine cascades](/benchmarks/turbine-cascade.md).

## Prediction with RANS transition models

Correlation-based transition models size the bubble through the production
of $k$ in the separated shear layer. The RANS sources find this the
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
  10, 16–19, 24). Sandberg & Michelassi (2022) cite the same device of
  Langtry & Menter (2009), a separation-aware term that raises the
  intermittency "above unity" in transitional separated regions, and add
  that the $\gamma$-$Re_\theta$ model suppresses wake-induced
  transition, because the low
  $Re_\theta$ of the incoming wakes is not fed into the blade boundary
  layers; they also cite the $k$-$\overline{v^2}$-$\omega$ model of
  Lopez & Walters, which transports the wall-normal fluctuation energy, as
  having predicted the bubble accurately in a low-Reynolds-number turbine
  (citing Akolekar et al. 2018) (§3.3.3.3–§3.3.3.4).
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

- **Compressor cascades.** Liu et al. (2024) find that a
  [Reynolds-stress model](/methods/reynolds-stress-model.md) coupled to
  Menter's one-equation intermittency model (SSG/LRR-$\omega$-$\gamma$)
  resolves the mid-chord bubbles on the suction side of the PVD compressor
  cascade ($Re\approx2.3\times10^5$) and of the NACA65 K48 cascade, with the
  $C_p$ plateaus near 45% ($-7^\circ$ incidence) and 35% ($0^\circ$) of the
  axial chord, which fully turbulent SST and SSG/LRR-$\omega$ miss; the
  separation-induced transition agrees with oil flow only when the
  $\omega$-production is $\gamma$-blended with a Kato–Launder term, the
  original production giving upstream bypass transition instead
  ([Liu et al. (2024)](/sources/liu-2024.md), Figs. 1, 8–9, 12, 15). They
  explain why the bubble matters downstream: in the transitional model the
  laminar layer separates, the separation raises the strain and triggers
  intermittency production, and the turbulent layer after reattachment is
  fuller than the fully turbulent one and resists the corner separation
  further downstream (Discussion, Fig. 18).
- **Turbine cascades and an airfoil with a laminar-kinetic-energy model.**
  Pacciani et al. (2025) attribute the overlong bubbles of many closures to
  the delayed response of the turbulence model, and target them with a
  separation switch that adds a production of laminar fluctuation energy and
  boosts its transfer to turbulence (see
  [laminar-kinetic-energy transition models](/methods/laminar-kinetic-energy-transition-model.md);
  [Pacciani et al. (2025)](/sources/pacciani-2025.md), §4.5). On the
  aft-loaded T106C cascade at $Tu=0.8\%$ their model reproduces the
  measured bursting of the bubble into an open separation at
  $Re_{2,is}=0.8\times10^5$, with transition too early, a smaller separated
  region and an underestimated loss, and closed bubbles at $1.2$ and
  $1.6\times10^5$ with the isentropic Mach number in the bubble slightly
  underestimated; on the front-loaded T108 the short bubbles, wake loss
  and lapse rate are matched, but the post-reattachment wall shear is
  lower than measured, attributed to the turbulence model (§6.2, Figs.
  18–23). The authors call the T106C result satisfactory for two-dimensional
  RANS, given the three-dimensional secondary flows that an LES of the case
  shows (§6.2). On the S809 airfoil at $Re=2\times10^6$, $Tu=0.2\%$,
  transition is separation-induced on both sides up to about $5.5^\circ$
  (§6.3).

Carreño Ruiz & D'Ambrosio and Morsbach et al. both find the bubble extent, and with it the
post-reattachment recovery, mispredicted. Carreño Ruiz & D'Ambrosio
tune the coefficient $s_1$ (page-local) of the separation-induced correction and propose a second
parameter for it, which they do not implement (§4, §7); Morsbach et al. suggest tuned transition-model
versions or laminar-kinetic-energy models (§5). The cases differ (airfoils
against a turbine cascade), and no source of the bundle tests both remedies
on one case. Pacciani et al. (2025) implement the second remedy and report
separated-flow predictions as accurate as those of their earlier LKE
model built for that purpose, with transition lengths that remain too
short (§7); they do not compute the T161 cascade or the very-low-Reynolds
airfoils.

- **A plate bubble with a laminar-kinetic-energy model.** Ghidoni &
  Noventa (2026) compute the ERCOFTAC T3C4 plate, the only separated case
  of their flat-plate set, with a reformulated
  [laminar-kinetic-energy model](/methods/laminar-kinetic-energy-transition-model.md)
  in a high-order DG solver, run pseudo-unsteady with time-step adaptation:
  the model captures separation, transition onset and reattachment but
  underestimates the peak shape factor, i.e. the bubble height
  ([Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md), §IV A, Appendix;
  see [ERCOFTAC T3 flat plates](/benchmarks/ercoftac-t3-flat-plate.md)).
  They omit, "for the sake of brevity", the separation-induced production
  and transfer terms of Dellacasagrande et al., which they say would reduce
  this error; the shear-layer limiter of Dellacasagrande et al. that they
  do keep, which approximates $Re_\theta$ by $d^2\lvert S\rvert/\nu$ to locate
  shear layers and avoids an overproduction of laminar fluctuation energy
  that would lengthen the bubble, and the Kubacki–Dick correction of the
  shear sheltering, both matter only on T3C4 (§II). On airfoils at high
  incidence, numerical separation during convergence makes runs fail,
  which they also ascribe to the missing separation-induced terms (§V).
- **Hybrid RANS/LES of a compressor cascade.** On the suction side of the
  V103 compressor cascade ($Re=138\,500$ on the axial chord $c_{ax}$,
  registry §11, $Tu=3.25\%$,
  separation-induced transition; pressure side bypass transition), Möller
  et al. (2024) find that fully turbulent SST-DDES misses the bubble,
  producing modelled $k$ ahead of separation and ending in an open
  separation near the trailing edge, while their transitional DDES
  (DDES coupled to the one-equation $\gamma$ model) reproduces $C_p$ and the
  bubble of the LES and DNS, with $C_f$ almost identical to the DNS up to
  separation and transition near $x/c_{ax}\approx0.65$ but too low after
  reattachment, because $\gamma$ suppresses the near-wall modelled
  production while the resolved $k$ is slightly low
  ([Möller et al. (2024)](/sources/moller-2024.md), §III.B.1, Figs. 5–9;
  accepted manuscript). Synthetic inflow turbulence closes the bubble
  slightly earlier, in better agreement with the DNS (§III.B.2, Figs.
  13–14). The bubble is sensitive to numerical dissipation: a purely
  central flux oscillates and suppresses the laminar separation, a 25%
  upwind fraction overpredicts the bubble, 5% agrees best with the DNS
  (§III.B.3, Fig. 19; see [DES](/methods/detached-eddy-simulation.md),
  [numerical dissipation](/properties/numerical-dissipation.md) and
  [compressor cascades](/benchmarks/compressor-cascade.md)).
- **Transonic compressor cascade.** Klose et al. (2025) find that URANS
  with SST and the $\gamma$-$Re_\theta$ model predicts a mainly laminar
  suction side, with a substantially lower $C_f$ than the implicit LES, in
  which the layer ahead of the shock is driven by intermittent turbulence
  ([Klose et al. (2025)](/sources/klose-2025.md), §6, Fig. 7; ASME accepted
  manuscript; below).
- **Without a transition model, a learned correction.** Fidkowski (2022)
  computes the [NACA 0012](/benchmarks/naca-0012-airfoil.md) at $M=0.2$,
  $\alpha=7^\circ$ and $Re=2\times10^4$ by unsteady Navier–Stokes with no
  turbulence model: the flow breaks down at about 40% chord into a
  separation bubble that reattaches at about 60% chord. Fully turbulent
  Spalart–Allmaras RANS gives no bubble and a persistent, mesh-independent
  lift error whose discretization-error estimates are "imperceptibly
  small"; a production multiplier obtained by field inversion of the
  time-averaged unsteady state, and learned by a small network, recovers
  the bubble well enough for output-based adaptation to converge the mean
  lift (0.6569 at 20 250 degrees of freedom, actual error 0.0011)
  ([Fidkowski (2022)](/sources/fidkowski-2022.md), §6.2, Table 2, Figs.
  10, 12; see [field inversion](/methods/field-inversion-machine-learning.md)
  and [mesh adaptation](/methods/mesh-adaptation.md)). At $Re=10^4$ the
  upper-surface layer instead breaks into unsteady vortices about
  mid-chord and leaves a large time-averaged separation (§6.1).

## Bubbles in unsteady and shock-loaded flows

**Dynamic stall.** On a NACA 0012 pitching as
$\alpha=10^\circ+15^\circ\sin(\omega t)$ at $Re_c=1.35\times10^5$ and reduced
frequency 0.1, the wall-resolved LES of Baldan & Guardone (2025) shows the
bubble forming near the leading edge in the upstroke; while it is present
the loads do not depend on the spanwise domain extent (maximum $C_L$
difference 0.05 across spans of $0.2c$–$1.2c$ up to $\alpha\approx22^\circ$),
and its bursting at about $22^\circ$ triggers the dynamic-stall vortex
([Baldan & Guardone (2025)](/sources/baldan-2025.md), §2.1, Figs. 3–6; arXiv
v2). In span-averaged space–time maps transition starts at the trailing edge
near $\alpha=2^\circ$ and progresses towards the bubble, reached at $10^\circ$;
the vortex develops beyond $15^\circ$ (Fig. 6). See
[NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md).

Batther & Lee (2022) follow the bubble through the onset of dynamic stall on
a NACA 0012 pitching up at a constant rate ($Re=2\times10^5$, $M=0.1$), with
delayed DES and transition models against the wall-resolved LES of Visbal
& Garmann ([Batther & Lee (2022)](/sources/batther-2022.md), §4.2, Table 3;
see [dynamic stall](/definitions/dynamic-stall.md)):

- transition, identified by a non-zero eddy viscosity at the first grid
  point, moves rapidly upstream after $\alpha=8^\circ$, and a bubble first
  forms near the leading edge around $10^\circ$ (§4.2.3, Fig. 8);
- at $15.2^\circ$ the boundary layer behind the bubble reattaches along two
  distinct branches, which explain two kinks in the pressure recovery of
  $C_p$ (§4.2.2, §4.2.5, Figs. 6, 15);
- at about $16.9^\circ$ the bubble collapses under the adverse pressure
  gradient ("suction collapse"), the separated shear layer rolls up into the
  dynamic-stall vortex near $18.6^\circ$, and the vortex is shed after
  $23.2^\circ$; the bursting is the initial trigger of the dynamic-stall
  process, and the bubble's earlier history "seemingly does not have a
  significant impact" on the vortex formation, in agreement with the LES
  (§4.2.3, §4.2.5);
- the stall is of the "pressure-gradient bubble-bursting" leading-edge
  type, since the reversed flow near the trailing edge does not propagate
  upstream, unlike the mixed-type stall at $Re=10^6$ of Benton & Visbal
  that the authors cite (§4.2.2, Fig. 7);
- against the LES, the DDES bubble at $15.2^\circ$ is larger with weaker
  reverse flow, oscillates more even after spanwise averaging, and
  collapses earlier; fully turbulent Spalart–Allmaras forms an abrupt
  turbulent separation bubble at $14.1^\circ$–$14.5^\circ$ instead (§4.2.5,
  §4.4, Figs. 14, 22);
- strong high-frequency surface-pressure oscillations at $x/c=0.05$
  precede the vortex formation, as in the experiment of Lorber & Carta,
  which the authors cite (§4.2.5, Fig. 16).

The two pitching studies agree that the bubble's bursting triggers the
dynamic-stall vortex, at different motions and Reynolds numbers
($22^\circ$ in Baldan & Guardone's sinusoidal cycle at $1.35\times10^5$,
about $17^\circ$ in Batther & Lee's ramp at $2\times10^5$).

**Shock-induced separation of a laminar layer.** On the transonic NLR-7301
airfoil ($Re=2.2\times10^6$, $Tu=0.03\%$), where the shock dominates
transition near $M_\infty=0.724$–$0.748$, the laminar-kinetic-energy model
of Ghidoni & Noventa (2026) misplaces the transition location by up to 81%
of its reference value (§V, Fig. 29). In the transonic TCTA
compressor cascade (inlet $M=1.21$, $Re=1.35\times10^6$ on the chord), the
time-averaged implicit LES of Klose et al. (2025) shows a slender
separation bubble beneath the oscillating mid-chord shock, followed by a
large recirculation reaching the trailing edge, "indicating an open
separation bubble" (§4, Fig. 4). The bubble shrinks as the spanwise domain
grows from 5% to 20% of the chord, in partial agreement, the authors
state, with Touber & Sandham, while the shock-oscillation frequency
barely changes ($ft_c=0.165$, 0.164, 0.163); the simulated separation
lengths, $0.12\le L_{\mathrm{sep}}/c\le0.22$ ($L_{\mathrm{sep}}$ page-local),
match the $0.18c$ given by Touber & Sandham's $St_{\mathrm{sep}}\approx0.03$
(§5, Table 2, Fig. 6). During the buffet cycle the growing bubble forces
velocity perturbations upstream through the subsonic part of the boundary
layer, which thickens it and produces intermittent oblique compression
waves (§7, §8). See
[shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).

**Bubbles and the drag crisis of a cylinder.** Mays et al. (2023) state
that in the critical and super-critical regimes of a smooth circular
cylinder the boundary layer transitions right after laminar separation and
reattaches, so that separation is delayed and the drag drops, as cited from
Zdravkovich and Rodríguez et al.; in the critical regime the shedding is
disrupted and the mean lift is an order of magnitude larger, and the LES of
Lehmkuhl et al. which they cite found three configurations, one-bubble
asymmetric, two-bubble asymmetric and two-bubble symmetric (super-critical)
([Mays et al. (2023)](/sources/mays-2023.md), §1). They list four physical
aspects that decide whether a model reproduces the free-shear-layer
transition: the onset of the Kelvin–Helmholtz instability, the spread of the
Kelvin–Helmholtz vortices, the descent into turbulence, and roll-up and
shedding (§1). Their scale-resolving hybrid reproduces the one-bubble
asymmetric state at $Re_D=2.5\times10^5$, with an asymmetric $C_p$, an
upward-deflected recirculation and a mean lift an order of magnitude
larger than at the other Reynolds numbers, and the return to symmetry in
the super-critical regime (§3.2.2, Figs. 6, 8). See
[circular-cylinder wake](/benchmarks/circular-cylinder-wake.md).

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
[implicit LES](/definitions/implicit-les.md)). Wang (2024) computes the
T106C cascade at an exit Reynolds number of $8\times10^4$ with no
free-stream turbulence, where the suction-side layer separates laminar and
transitions in the reattachment zone, by flux-reconstruction implicit LES
($N=3$, 7.87 million degrees of freedom per equation, mean $y^+\approx0.5$,
$x^+\approx20$, $z^+\approx6$), and obtains an isentropic Mach number in
"excellent agreement" with the experiment for two Riemann solvers
([Wang (2024)](/sources/wang-2024-b.md), §4.2, Table 4, Figs. 7–8; arXiv v2;
see [flux reconstruction](/methods/flux-reconstruction.md) and
[turbine cascades](/benchmarks/turbine-cascade.md)).

The bubble is also a workshop target for scale-resolving methods. The
first High-Order CFD Workshop posed the SD7003 wing at $Re_c=60{,}000$,
$M=0.1$, spanwise periodic over $0.2c$, as its implicit-LES case, with
$\alpha=4^\circ$ giving a relatively long bubble and $\alpha=8^\circ$ a
shorter one, and asked for methods that handle "in a seamless fashion, the
mixed laminar, transitional, and turbulent flow regions"; the summary
specifies the case without showing results
([Wang et al. (2013)](/sources/wang-2013.md), §4.13, case C3.3). It is the
airfoil and Reynolds number of the RANS calibration of Carreño Ruiz &
D'Ambrosio above, whose reference is an LES.

Vermeire (2024) computes the shorter-bubble case, SD7003 at $\alpha=8^\circ$,
$Re_c=60{,}000$, by implicit LES with flux reconstruction and entropically
damped artificial compressibility (incompressibility factor 0.2) on an
"intentionally coarse" mesh of 57,100 hexahedra (span $0.2c$, 10 elements in
span), and finds the bubble decided by the polynomial degree at fixed mesh
([Vermeire (2024)](/sources/vermeire-2024.md), §4.3, Figs. 20–21, Table 3;
see the [SD7003 airfoil](/benchmarks/sd7003-airfoil.md)). With $N=1$ the flow
is fully separated, with no distinct suction-side pressure recovery; $N=2$
shows a laminar separation bubble and attached turbulent flow downstream;
$N=3$ moves transition upstream; $N=4$ agrees with the high-order
compressible reference simulations, with $C_L=0.950$, $C_D=0.046$ against
0.941 and 0.049 of the author's earlier $N=4$ computation, 0.969 and 0.039 of
Garmann et al. and 0.932 and 0.050 of Beck et al. (Table 3). The $N=1$ case
gives $C_D=0.110$; $N=2$ gives $C_L=1.002$, the largest lift.

**A bubble in a hybrid model without a transition model.** On the MD-30P30N
three-element airfoil at $Re_C=9\times10^6$, Wu et al. (2024) read a plunge in
$C_p$ at $x/c\approx0.15$ at $8^\circ$ as a large recirculation bubble, i.e. as
laminar–turbulent transition captured, weakening as the incidence rises
([Wu et al. (2024)](/sources/wu-2024.md), §3.3, Fig. 23). Their
[SATES-σ](/methods/self-adaptive-turbulence-eddy-simulation.md) hybrid has no
transition model; it lowers the eddy viscosity in pure-shear (laminar) regions
through the σ-model operator, and the authors state that transition "may not
be captured accurately if the computational grid resolution is insufficient"
(§2.2, §4; see the [30P30N airfoil](/benchmarks/30p30n-high-lift-airfoil.md)).

Lederer et al. (2026) compute the Eppler 387 airfoil by implicit LES with a
mass-conserving mixed-stress discretization of degree $N=3$, with and
without the [high-order projection-based upwind](/methods/high-order-projection-based-upwind-method.md)
(HOPU) stabilization, on three meshes of 2352 to 14 400 hexahedra, and
compare with the NASA TM 4062 measurements
([Lederer et al. (2026)](/sources/lederer-2026.md), §4, Tables 1–2; arXiv
v1; see [Eppler 387 airfoil](/benchmarks/eppler-387-airfoil.md)). At
$Re=3\times10^5$, $\alpha=4^\circ$ the finest mesh places separation and
reattachment at $x/c=0.467$ and 0.560 against 0.40 and 0.58 measured, the
experiment separating earlier; at $Re=10^5$, $\alpha=10^\circ$ a small
leading-edge bubble from 0.010 to 0.027 appears (Table 2). The bubble
extent grows with resolution, and the coarse meshes fail to predict a
meaningful bubble at $Re=10^5$, giving a smaller separation or "an
(unphysical) almost natural transition"; the sharp peak of the
displacement thickness at separation and its subsequent fall are missed on
the two coarser meshes (§4.1–§4.2, Fig. 10). HOPU leaves the pressure
distribution, lift, drag and the separation and reattachment points
essentially unchanged, e.g. $C_L=1.274$ and 1.271, $C_D=0.0432$ and 0.0436 on
the coarsest mesh at $Re=10^5$, while improving the turbulent boundary
layer after reattachment; the authors read the finest-mesh agreement as an
advantage of a low-dissipation discretization that preserves the laminar
instabilities leading to transition (§4.1, §5, Table 2; see
[implicit LES](/definitions/implicit-les.md)).

**Bubble size in a hybrid model on coarse meshes.** On the drag-crisis
cylinder, the scale-resolving hybrid RANS/LES of Mays et al. (2023), with
URANS shielding near the wall and first-cell $y^+<1$ on meshes about five
times coarser than the reference LES, matches the reference drag closely
($C_D=0.292$ on the finer grid against 0.296 at $Re_D=5.3\times10^5$) but captures the bubble
sizes and the mean lift less well: agreement around the $C_p$ plateau that
marks the bubble is weaker at $Re_D=2.5$ and $3.8\times10^5$, which the
authors attribute to small variations in the separation and reattachment
points (§3.2.2, Table 4). URANS with the same Lag elliptic-blending
$k$-$\varepsilon$ model partly captures the bubble, through a slight
inflection of $C_p$ near separation and a non-zero mean lift, while missing
the drag crisis (§3.2.1; see [k-ε models](/methods/k-epsilon-model.md)).
The authors conclude that near-wall resolution must remain high, because
under-resolution there "is fatal" to the prediction of transition and
separation (§4; see [hybrid RANS/LES](/definitions/hybrid-rans-les.md)).

**Bubbles as targets of mesh adaptation.** Ims & Wang (2023) adapt the
meshes of flux-reconstruction implicit LES of the T106c ($Re=80\,000$, $N=2$)
and T106a ($Re=60\,000$, $N=1$) cascades with three error indicators; on the
T106a the coarse starting mesh leaves the laminar flow unresolved, which the
authors call "less challenging for the flow solver but more challenging for
the error indicators", and none of the indicators refines much at the
leading edge, which the authors put down, with a "possibly", to the
laminar flow there being already resolved
([Ims & Wang (2023)](/sources/ims-2023.md), §5.1–§5.2). The indicators
mark cells along the suction-side bubble from separation into the wake,
the smoothness indicator favouring small boundary-layer cells on both
surfaces (§5.1, Figs. 9–12); details on
[mesh adaptation](/methods/mesh-adaptation.md) and
[turbine cascades](/benchmarks/turbine-cascade.md).

## Qualifications

- Vermeire (2024) describes the SD7003 references as "high-order compressible
  simulations" in §4.3 but as "reference DNS data" in §5, and prints the lift
  and drag coefficients as $L/(2\rho_\infty u_\infty^2)$ and
  $D/(2\rho_\infty u_\infty^2)$ with $L$, $D$ called "coefficients" (Eqs.
  23–24); the table values above are as printed.
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
- Baldan & Guardone describe the dynamic-stall phase of bubble formation
  with transition "initiating at the trailing edge and progressing
  downstream" (Introduction); from the trailing edge the progression is
  upstream, as their §2.1 says ("progresses towards the LSB").

# Citations

- [Slaughter et al. (2023)](/sources/slaughter-2023.md) — §3.6 Figs. 4–5, §4.1 Figs. 6–7, 9–12, §4.3 Figs. 14–15, 22, §6 (Research Square preprint v1).
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §3.1, §3.3, §4.1 Figs. 4, 7–9, §4.2 Figs. 12, 15, §5.
- [Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md) — §2 Eqs. 5–6, §3.5 Tables 5, 7, §4, §5 Table 11, §6.1 Fig. 17, §7.
- [Menter et al. (2022)](/sources/menter-2022.md) — §1, §2 Eqs. 13–18, Figs. 4–5, 10, 16–19, 24.
- [Liu et al. (2024)](/sources/liu-2024.md) — Figs. 1, 8–9, 12, 15, 18, Discussion.
- [Pacciani et al. (2025)](/sources/pacciani-2025.md) — §4.5, §6.2 Figs. 18–23, §6.3, §7.
- [Wang (2024)](/sources/wang-2024-b.md) — §4.2, Table 4, Figs. 7–8 (arXiv v2).
- [Möller et al. (2024)](/sources/moller-2024.md) — §III.B.1–3, Figs. 5–9, 13–14, 19 (accepted manuscript).
- [Baldan & Guardone (2025)](/sources/baldan-2025.md) — Introduction, §2.1, Figs. 3–6 (arXiv v2).
- [Klose et al. (2025)](/sources/klose-2025.md) — §4 Fig. 4, §5 Table 2 Fig. 6, §6 Fig. 7, §7, §8 (ASME accepted manuscript).
- [Lederer et al. (2026)](/sources/lederer-2026.md) — §4, §4.1–§4.2 Tables 1–2 Fig. 10, §5 (arXiv v1).
- [Batther & Lee (2022)](/sources/batther-2022.md) — §4.2.2–4.2.5, §4.4, Table 3, Figs. 6–8, 14–16, 22.
- [Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md) — §II, §IV A, §V Fig. 29, Appendix.
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §3.3.2, §3.3.3, §3.3.3.3–§3.3.3.4, Fig. 6.
- [Wang et al. (2013)](/sources/wang-2013.md) — §4.13 (case C3.3).
- [Fidkowski (2022)](/sources/fidkowski-2022.md) — §6.1–6.2, Table 2, Figs. 10, 12.
- [Mays et al. (2023)](/sources/mays-2023.md) — §1, §3.2.1, §3.2.2 Table 4 Figs. 6, 8, §4.
- [Ims & Wang (2023)](/sources/ims-2023.md) — §5.1 Figs. 9–12, §5.2.
- [Vermeire (2024)](/sources/vermeire-2024.md) — §4.3, Figs. 20–21, Table 3 (SD7003 bubble against polynomial degree in EDAC flux-reconstruction implicit LES); §5; Eqs. (23)–(24).
- [Wu et al. (2024)](/sources/wu-2024.md) — §2.2, §3.3, Fig. 23, §4 (bubble on the MD-30P30N at $8^\circ$ in SATES-σ).

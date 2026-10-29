---
type: Benchmark
title: "30P30N three-element high-lift airfoil"
description: "The 30P30N slat–main–flap airfoil in three forms: the modified BANC-III geometry at Mach 0.17, chord Reynolds number 1.7 million and 5.5°, where hybrid and LES approaches and scheme dissipation are compared; the workshop RANS case at Mach 0.2, 9 million and 16°; and hybrid runs at Mach 0.2, 9 million over 8–24°, with four hybrids compared at 21°."
status: established
aliases: [30P30N, 30P-30N, 30P/30N, MD 30P30N, modified 30P30N, BANC-III 30P30N, three-element high-lift airfoil]
tags: [benchmark, hybrid-rans-les, des, separated-flow, numerical-dissipation, aeroacoustics]
timestamp: 2026-10-29T07:38:00Z
---

# 30P30N three-element high-lift airfoil

The 30P30N is a two-dimensional three-element high-lift airfoil (slat, main
element, flap) whose slat and flap are deflected by $30^\circ$. The flow
combines a separated shear layer in the slat cove that rolls up, impinges
on the slat wall and radiates slat noise, the thin boundary layers of three
elements, the merging of the slat wake with the main-element boundary layer,
and possible separation on the flap. In this bundle it is run in three
distinct forms that should not be mixed:

- the **modified 30P30N of the BANC-III workshop** (Benchmark Problems for
  Airframe Noise Computations) at $M=0.17$, $Re=1.7\times10^6$ on the stowed
  chord and incidence $5.5^\circ$, a scale-resolving test of the slat-cove
  shear layer;
- the **workshop RANS case** at $M=0.2$, $Re=9\times10^6$ and $16^\circ$
  (case C3.1 of the first High-Order CFD Workshop), a steady
  [Spalart–Allmaras](/methods/spalart-allmaras-model.md) test of high-order
  discretizations;
- a **scale-resolving stall sweep** at the workshop's $M=0.2$ and
  $Re_C=9\times10^6$, six incidences from $8^\circ$ to $24^\circ$, against
  the experiment of Chin et al., which tests whether a hybrid model
  predicts the maximum lift and the drop after stall.

On this page $\alpha$ denotes the angle of attack (page-local; the
registry's $\alpha$ is the DG/finite-volume blending factor) and $C$ the
stowed chord. The three-dimensional high-lift aircraft configurations are
on [NASA CRM high-lift](/benchmarks/nasa-crm-high-lift.md) and
[JAXA Standard Model](/benchmarks/jaxa-standard-model.md).

## Configuration: modified 30P30N (BANC-III)

| Item | [Wu et al. (2023)](/sources/wu-2023-b.md), §2.3 | [Wang et al. (2024)](/sources/wang-2024.md), §4 |
|---|---|---|
| Chord | stowed chord $C=18$ in | $C=0.457$ m |
| Elements | slat $0.15C$, flap $0.3C$, both deflected $30^\circ$ (Fig. 2) | slat $0.15C$, flap $0.3C$, both deflected $30^\circ$ to the main-element chord |
| Conditions | $M=0.17$, $Re=1.71\times10^6$, $\alpha=5.5^\circ$ | $M_\infty=0.17$, $Re=1.7\times10^6$ on the stowed chord, $\alpha=5.5^\circ$ on the main-element chord |
| Domain | $30C$ in the $x$-$y$ plane; span $C/9$, "as recommended by the BANC-III workshop"; periodic in span | radial extent about $90C$; span "a minimum of $0.74C$, determined by the correlation of two-point pressure fluctuations" (citing the BANC-III summary) |
| Grid | multi-block structured, refined in the slat cove: 7.2 M (60 span cells), 19 M and 27 M cells (80 span cells) | about 27 million cells |
| Time step | $\Delta t\,U_\infty/C=10^{-4}$ (coarse), $5\times10^{-5}$ (medium, fine) | $\Delta t\,U_\infty/C=2\times10^{-5}$ |
| Statistics | 10 time units $C/U_\infty$ after 10, from a converged RANS field | time and spanwise averages |
| Reference data | JAXA wind tunnel ($C_L=2.82$, $C_p$); FSU (slat-cove PIV, rms $C_p$ on the slat; $C_L=2.84$); wall-modelled LES of Zhang et al. ($C_L=2.848$, $C_D=0.067$) | Pascioni et al. (FSU) for $C_p$ and slat-cove profiles; FSU and JAXA for the slat-trailing-edge pressure spectrum |

Wu et al. print the chord in inches, Wang et al. in metres. Both use the measurement lines of the BANC guidelines across the
slat-cove shear layer (L1–L7).

## Results on the modified 30P30N

**Model, scheme and grid at fixed conditions.**
[Wu et al. (2023)](/sources/wu-2023-b.md) run, in the structured
finite-difference solver PHengLEI, three groups of cases (Table 2): the
self-adaptive turbulence eddy simulation (SATES, the unified RANS–LES–DNS
model of Han and coworkers formerly called VLES, recorded on
[hybrid RANS/LES](/definitions/hybrid-rans-les.md)) on three grids; SATES
with three convective schemes on the fine grid; and
[Smagorinsky](/methods/smagorinsky-model.md) LES ($C_s=0.1$), SST-IDDES
([detached-eddy simulation](/methods/detached-eddy-simulation.md)) and
SATES with the same scheme on the fine grid. The schemes are the
fourth-order [weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md)
with Z-type weights at regularization parameter $\epsilon_{\mathrm Z}=100$,
which makes the weights effectively linear (WCNS-L), or $10^{-6}$ (WCNS-Z)
(registry §11), and a second-order blend of central and upwind
interpolation with upwind fraction $\sigma_b=0.02$ (BCD). Their error is
taken against the experimental mean $C_L=2.83$:

| Case | Grid | Model | Scheme | $C_L$ | $C_D$ | $C_L$ error |
|---|---|---|---|---|---|---|
| A1 | 7.2 M | SATES | WCNS-L | 2.85 | 0.054 | 0.7% |
| A2 | 19 M | SATES | WCNS-L | 2.75 | 0.064 | −2.8% |
| A3 | 27 M | SATES | WCNS-L | 2.82 | 0.070 | −0.4% |
| B1 | 27 M | SATES | BCD | 2.52 | 0.072 | −11.0% |
| B2 | 27 M | SATES | WCNS-Z | 2.64 | 0.074 | −6.7% |
| C1 | 27 M | Smagorinsky LES | WCNS-L | 2.64 | 0.070 | −6.7% |
| C2 | 27 M | SST-IDDES | WCNS-L | 2.27 | 0.076 | −19.8% |

The printed errors follow from the table's coefficients and 2.83
*(compiler check, not in the sources)*. Their reading (§3.2–3.4):

- *Grid.* The mean $C_p$ is insensitive to the grid and agrees with the
  JAXA and FSU data even on 7.2 M cells; the peak rms $C_p$ on the slat
  falls with refinement, and on the coarse grid the slat-cove turbulent
  kinetic energy is too low at L1 and too high at L7, which the authors
  read as a delayed shear-layer instability that refinement moves
  upstream (Figs. 6–8). Resolved kinetic energy exceeds the modelled one
  at most points of the mid-span plane even on the coarse grid (Figs.
  9–10).
- *Scheme.* The lower dissipation of WCNS makes the slat shear layer
  unstable sooner than BCD; the Z-type weights lose accuracy near
  high-order critical points and add dissipation in the shear layer, so
  the authors recommend linear interpolation for shock-free low-Mach
  flow (Figs. 11–15; see [numerical dissipation](/properties/numerical-dissipation.md)).
  Outside the cove shear layer no scheme matches the PIV turbulent
  kinetic energy, which the authors attribute, citing the WMLES study, to
  poor PIV resolution from a shortage of particles (Fig. 16).
- *Model.* SST-IDDES delays the shear-layer transition, carries larger
  $\mu_t/\mu$ in the attached boundary layers and a considerable eddy
  viscosity in the slat cove, and separates early on the flap suction side,
  "which may have been caused by the GIS" (grid-induced separation),
  "although the turbulent boundary layer was partially protected to avoid
  modeled stress depletion"; SATES predicts the slat-cove reattachment
  best and resolves more turbulent kinetic energy than IDDES; LES resolves
  the most and predicts a larger main-element separation bubble than
  SATES (Figs. 17–25).

**Scheme for budget analysis.** [Wang et al. (2024)](/sources/wang-2024.md),
§4, run a Spalart–Allmaras-based DDES with a sixth-order optimized upwind
scheme (OPT6) chosen on the [periodic hill](/benchmarks/periodic-hill.md)
for the turbulent-kinetic-energy budget (see
[low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md)).
The mean $C_p$ agrees with Pascioni et al.; the spanwise vorticity,
velocity magnitude and turbulent kinetic energy along lines through the
slat shear layer agree with the same data, their maxima decreasing away
from the slat trailing edge; the slat-trailing-edge pressure spectrum
agrees with the FSU and JAXA data, broadband with a tone near 21 kHz
(Figs. 8–10). In the slat cove the turbulent kinetic energy has three
maxima: the trailing-edge shedding region, the shear layer behind the
slat leading edge, and the unsteady impingement on the wall. The budget
terms take recurring spatial patterns (production and dissipation
"monopole", diffusion "outward", advection "inward"); along the slat
shear layer production dominates and decays to about 10% of its initial
value, with diffusion, mainly turbulent transport, the main balance, and
the budget does not close, which the authors attribute to insufficient
grid resolution by analogy with the hill, without a grid study on the
airfoil (Figs. 11–12).

**Nonlinear weights of the compact scheme.** [Wu et al. (2024b)](/sources/wu-2024-b.md),
§IV.C.1, rerun SATES in PHengLEI on the 27-million-cell grid of
[Wu et al. (2023)](/sources/wu-2023-b.md) (domain $30C$, span $C/9$,
$M=0.17$, $Re=1.71\times10^6$, $\alpha=5.5^\circ$), now with the
fifth-order [weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md)
and a Roe flux, and vary only the nonlinear interpolation weights:
Jiang–Shu (WCNS-JS), Z-type (WCNS-Z), the sharp TENO cut-off (WCNS-T), the
authors' smooth $\tanh$ cut-off (WCNS-ST) and its adaptive-threshold form
(WCNS-STA), with the linear fifth-order scheme as the numerical reference.
Their reading (Figs. 7–10):

- WCNS-JS is over-dissipative: it suppresses the Kelvin–Helmholtz
  instability of the slat-cove shear layer and its time-averaged $C_p$
  deviates significantly, mostly on the flap, which the authors attribute
  to suppressed suction-side turbulence and a stronger separation under
  the adverse pressure gradient; WCNS-Z is better but still dissipative
  near high-order critical points;
- WCNS-T, WCNS-ST and WCNS-STA resolve more small structures, promote the
  initial shear-layer instability and agree in $C_p$ with the experiment
  and with the linear scheme;
- in the dual-time sub-iterations (second-order backward differentiation
  with LU-SGS) WCNS-T converges worse than WCNS-ST and WCNS-STA, and along
  two lines through the slat cove the time-averaged spanwise vorticity of
  WCNS-ST agrees better with the stereo-PIV data of Pascioni et al. than
  that of WCNS-T, which the authors attribute to the better sub-iteration
  convergence.

Normalized by WCNS-JS, the CPU cost on this case is 0.97 (linear), 1.03
(Z), 1.51 (T), 1.52 (ST) and 1.68 (STA) (Table I). The weights are defined
on [weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md)
and the closure on
[self-adaptive turbulence eddy simulation](/methods/self-adaptive-turbulence-eddy-simulation.md).
Wu et al. (2024b), §I, cite their group's earlier work (their ref. 14,
[Wu et al. (2023)](/sources/wu-2023-b.md)) for the statement that Z-type
weights are over-dissipative on this airfoil; the Z-weight results of
Wu et al. (2023) are given above.

## Workshop RANS case ($M=0.2$, $Re=9\times10^6$, $\alpha=16^\circ$)

[Wang et al. (2013)](/sources/wang-2013.md), §4.11, specify case C3.1 of
the first High-Order CFD Workshop: two-dimensional RANS with the
Spalart–Allmaras or $k$-$\omega$ model, $M=0.2$, $\alpha=16^\circ$,
$Re=9\times10^6$, fully turbulent, reference chord 0.5588 m; no workshop
results are shown. [Huang et al. (2022b)](/sources/huang-2022-d.md), §3.3,
run these conditions with steady Spalart–Allmaras RANS on a hybrid mesh of
53,870 cells: their optimized fourth-order variational-reconstruction
finite-volume scheme gives lift and drag closer to the DLR reference than
the fourth-order scheme with earlier weights and the second-order scheme,
and its skin friction is closer to a degree-4 DG solution of 1,119,530
degrees of freedom; the fourth-order scheme carries the slat-wake eddy
viscosity to the outlet, where the second-order one dissipates it (Figs.
33–35). The details are on
[NASA CRM high-lift](/benchmarks/nasa-crm-high-lift.md), where they were
first recorded. [Bose & Park (2018)](/sources/bose-2018.md), §4.3, cite a
wall-modelled LES of the 30P/30N at $Re_c=9\times10^6$ with an
equilibrium wall model (Bodart et al. 2013) that captures the maximal lift
but stalls at about $23^\circ$ against about $21^\circ$ in the experiment
(see [wall-modelled LES](/methods/wall-modelled-les.md)).

## Scale-resolving stall sweep ($M=0.2$, $Re_C=9\times10^6$, $8^\circ$–$24^\circ$)

[Wu et al. (2024)](/sources/wu-2024.md), §3.3, run the "MD-30P30N" at
$Re_C=9\times10^6$ on the stowed chord and $M=0.2$, at
$\alpha=8$, 16, 19, 21, 23 and $24^\circ$, with the same group's solver
[PHengLEI](/software/phenglei.md) and the fourth-order
[weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md)
with linear weights. Their set-up:

| Item | [Wu et al. (2024)](/sources/wu-2024.md), §3.3 |
|---|---|
| Domain | radius 100 chords; span 11% of the chord, periodic |
| Grids | 12.8 M (coarse) and 26.4 M (fine) cells, $y^+\approx1$ |
| Models | SST-IDDES, SATES-SM (constant $C_x=0.61$) and SATES-σ (local $C_x$), see [self-adaptive turbulence eddy simulation](/methods/self-adaptive-turbulence-eddy-simulation.md) |
| Reference | experiment of Chin et al., blockage-corrected |
| Averaging | time not printed |

Their results (Figs. 18–26):

- *Grid and model at $21^\circ$.* SATES-σ gives the same $C_p$ on the two
  grids, in good agreement with the experiment and better than SATES-SM
  and IDDES, especially at the suction peaks near the leading edges of the
  main element and the flap (Fig. 22).
- *Other incidences.* SATES-σ agrees with the measured $C_p$ at 8, 16
  and $23^\circ$; at $8^\circ$ a plunge of $C_p$ at $x/C\approx0.15$ is read as a large
  recirculation bubble with laminar–turbulent transition, weakening as the
  incidence grows (Fig. 23; see
  [laminar separation bubble](/definitions/laminar-separation-bubble.md)).
  Velocity profiles at $x/C=0.45$, 0.8982, 0.975, 1.0321, 1.0752 and
  1.1125 agree better with SATES-σ than with SATES-SM near the wall,
  especially on the flap under the strong adverse pressure gradient, and
  differ from the data in the outer layer (Fig. 25).
- *Lift and stall.* The total-lift error of SATES-σ is "always less than
  6.5%, even at post-stall conditions", and the model captures the maximum
  lift and the stall; the slat lift agrees, the flap lift is
  over-predicted, which the authors attribute to the free-air computation
  against the wind-tunnel blockage (Fig. 26). They cite RANS studies and a
  transitional and turbulent DDES that show no appropriate drop of lift
  after stall, and attribute the DDES failure to its thick RANS layer,
  whose eddy viscosity damps the boundary-layer unsteadiness (§1, §3.3).
- *Limit.* Because SATES-σ works close to its LES mode, transition "may
  not be captured accurately if the computational grid resolution is
  insufficient", unlike DDES, which is closer to URANS (§4).

**Four hybrids at $21^\circ$.** [Wu et al. (2026)](/sources/wu-2026-b.md),
§4.2, return to the same conditions ($Re_C=9\times10^6$, $M=0.2$) at
$\alpha=21^\circ$, which they call the "critical stall angle of attack",
with the high-order branch PHengLEI-HyOrder (sixth-order WCNS with
smooth scale-separating weights) and four models: SATES-SM, SATES-II,
SST-IDDES and AIDDES (see
[self-adaptive turbulence eddy simulation](/methods/self-adaptive-turbulence-eddy-simulation.md)
and [detached-eddy simulation](/methods/detached-eddy-simulation.md)).

| Item | [Wu et al. (2026)](/sources/wu-2026-b.md), §4.2 |
|---|---|
| Domain | circle of radius 100 chords; span 12% of the chord, periodic |
| Grids | two-dimensional grids of about 140 000 and 330 000 cells extruded on 30 and 80 spanwise points: m1 about 4.26 M, m2 about 27 M cells |
| Time step | printed "$\Delta tC/U_\infty$" $=2\times10^{-4}$ (m1), $1\times10^{-4}$ (m2); statistics over more than 40 000 steps |
| Reference | experiment of Chin et al. (1993, as cited): $C_p$, $C_f$, velocity-magnitude profiles at six stations |

Their results (Figs. 12–14):

- *Grid.* $C_p$ agrees with the experiment on both grids; the fine grid
  gives a more accurate $C_f$ at the main-element leading edge by
  resolving a faster transition (Fig. 12).
- *Models.* SATES-SM separates prematurely on the slat upper surface,
  which the authors attribute to its lack of wall modelling; SATES-II
  returns $F_r\to1$ near the walls; IDDES suppresses the Kelvin–Helmholtz
  instability of the slat wake, giving a "relatively stable
  quasi-two-dimensional" wake; AIDDES gives stronger three-dimensional
  fluctuations than IDDES (Fig. 13).
- *Profiles.* SATES-II improves the near-wall profiles at $x/C=0.85$–0.975
  and in the flap boundary layer; IDDES deviates much less than SATES-SM
  thanks to its shielding but lacks resolution of the wake turbulence;
  AIDDES improves the downstream profiles under the varying adverse
  pressure gradient (Fig. 14).

Wu et al. (2024) print a span of 11% of the chord and grids of 12.8 M and
26.4 M cells, Wu et al. (2026) a span of 12% and grids of 4.26 M and 27 M
cells, each for its own runs at the same conditions.

## What the case shows

- On the modified 30P30N the lift depends more on the convective scheme and
  the hybrid model than on the grid: at 27 M cells the scheme moves $C_L$
  from −11.0% to −0.4% and the model from −19.8% to −0.4%, while the three
  grids stay within 3% ([Wu et al. (2023)](/sources/wu-2023-b.md), Table 2).
  The slat-cove shear layer is the sensitive region: excess dissipation,
  numerical or modelled, delays its instability.
- Two hybrids at the same nominal conditions reach opposite outcomes: the
  SA-DDES of [Wang et al. (2024)](/sources/wang-2024.md) agrees with the
  measured $C_p$ and slat-cove profiles, the SST-IDDES of
  [Wu et al. (2023)](/sources/wu-2023-b.md) is 19.8% low in lift with early
  flap separation. The set-ups differ: SA-based DDES with the sixth-order
  OPT6 scheme, span $0.74C$, about 27 million cells (Wang et al.), against
  SST-based IDDES with fourth-order WCNS-L, span $C/9$, 27 million cells
  (Wu et al.). Wu et al. cite a successful IDDES of the airfoil by
  Ashton et al. without discussing the difference.

- At fixed model and grid, the choice of nonlinear weights alone decides
  whether the slat-cove shear layer becomes unstable and whether the flap
  $C_p$ agrees with the experiment ([Wu et al. (2024b)](/sources/wu-2024-b.md),
  Figs. 7–8); Wu et al. (2023) also vary the scheme at fixed model and
  grid (Table 2, above).

- The stall sweep of [Wu et al. (2024)](/sources/wu-2024.md) is the only
  form here that varies the incidence through $C_{L,\max}$; at the
  conditions of the workshop RANS case its evidence for stall prediction is
  numerical, one model family (SATES) against IDDES on two grids.
- At $21^\circ$ the constant-coefficient SATES-SM separates prematurely
  on the slat, which Wu et al. (2026) attribute to its lack of wall
  modelling, and the wall-treated SATES-II improves the near-wall profiles
  ([Wu et al. (2026)](/sources/wu-2026-b.md), §4.2).

## Qualifications

- Wu et al. print no wall-unit resolution, and Wang et al. print no grid
  study on the airfoil; neither prints an integrated resolved fraction of
  the turbulent kinetic energy (Wu et al. show scatter plots, Figs. 10, 25).
- Wu et al. call $Re=1.71\times10^6$ "moderate" (§2.3) while the title and
  abstract speak of high Reynolds number. Their §3.1 says the $C_L$ of
  cases A1–A3 "differed by less than 3%", which holds for each error
  against 2.83, while A1 and A2 differ by 3.6% of A2, and the sequence
  2.85, 2.75, 2.82 is not monotone in the grid *(compiler check, not in
  the sources)*. Their §3.4
  refers to grid resolution "in section B" and schemes "in section C",
  while Table 2 labels the grid group A and the scheme group B.
- [Wu et al. (2024)](/sources/wu-2024.md) print 12.8 M and 26.4 M cells
  for the two grids (§3.3) and "a relatively coarse grid containing
  approximately 24 million cells" in the Conclusions (§4). They print the
  airfoil's time step as $\Delta t\,D/U_\infty=1\times10^{-4}$, with the
  diameter symbol of their cylinder cases. They do not print the chord
  length, so the identity of their "MD-30P30N" with the 0.5588 m workshop
  chord of Wang et al. (2013) is not established by the page.
- [Wu et al. (2026)](/sources/wu-2026-b.md), §4.2, print the
  non-dimensional time step as "$\Delta tC/U_\infty$"; by dimension the
  non-dimensional step is $\Delta t\,U_\infty/C$ *(compiler check, not in
  the sources)*.
- [Wu et al. (2026)](/sources/wu-2026-b.md) give the 30P30N runs "three
  compute nodes of 160 CPU cores" and the base-flow runs "10 compute nodes
  with a total of 640 CPU cores" (§4).
- [Wu et al. (2024b)](/sources/wu-2024-b.md) do not state the averaging
  time on the airfoil and give the sub-iteration convergence only as
  residual histories (Fig. 9); they cite "Fig. 6" for the slat-cove small
  scales, which their Fig. 7 shows (Fig. 6 is the geometry).
- The workshop RANS case and the BANC-III case differ in Mach number,
  Reynolds number, incidence and chord (0.5588 m against 0.457 m); results
  of one do not validate the other.

## Contradictions

**Spanwise extent of the modified 30P30N.** *Open.*
[Wu et al. (2023)](/sources/wu-2023-b.md), §2.3, run a span of $C/9$, "as
recommended by the BANC-III workshop"; [Wang et al. (2024)](/sources/wang-2024.md),
§4, set the span to "a minimum of $0.74C$, determined by the correlation of
two-point pressure fluctuations", citing the BANC-III summary (Choudhari
& Lockard 2015). Both attribute their span to the workshop; the two
printed spans differ by a factor of about 6.7 *(compiler check, not in
the sources)*.

# Citations

- [Wu et al. (2023)](/sources/wu-2023-b.md) — §1; §2.1–2.3, Table 1, Fig. 2; §3.1–3.4, Table 2, Figs. 4–25; §4.
- [Wang et al. (2024)](/sources/wang-2024.md) — §3.3 (scheme choice); §4, Figs. 8–12; §5.
- [Wang et al. (2013)](/sources/wang-2013.md) — §4.11 (case C3.1; specification only).
- [Huang et al. (2022b)](/sources/huang-2022-d.md) — §3.3, Figs. 33–35.
- [Bose & Park (2018)](/sources/bose-2018.md) — §4.3 (cited WMLES of Bodart et al.).
- [Wu et al. (2024)](/sources/wu-2024.md) — §1; §3.3, Figs. 18–26; §4.
- [Wu et al. (2024b)](/sources/wu-2024-b.md) — §I; §IV.C.1, Figs. 6–10; Table I.
- [Wu et al. (2026)](/sources/wu-2026-b.md) — §3.4 (PHengLEI-HyOrder); §4.2, Figs. 12–14 (30P30N at $21^\circ$: domain, grids, time step, four hybrids, $C_p$, $C_f$, profiles).

---
type: Definition
title: "Edge-localized mode (ELM) and ELM-free regimes"
description: "Repetitive edge MHD instability of the H-mode pedestal, set off by coupled peeling-ballooning modes, that expels pedestal energy and particles in filaments; with the naturally ELM-free or small-ELM regimes (QH-mode, EDA H-mode, QCE) and the active control methods (RMPs, pellets, vertical kicks) as reproduced by nonlinear MHD codes, including ITER RMP suppression, current-sheet reconnection in peeling-ballooning ELMs and the two-stage crash of resistive drift-ballooning ELMs."
status: established
aliases: [ELM, type-I ELM, ELM crash, pedestal collapse, QH-mode, EDA H-mode, QCE, ELM suppression, quasi-coherent mode, QCM]
tags: [elm, pedestal, edge, ballooning, mhd, extended-mhd, tokamak]
timestamp: 2026-10-16T18:00:00Z
---

# Edge-localized mode (ELM) and ELM-free regimes

An edge-localized mode is a repetitive MHD instability of the steep-gradient
edge region of an H-mode plasma, the pedestal. Each ELM crash expels part of
the pedestal energy and particles in field-aligned filaments into the
scrape-off layer and onto the divertor. The pedestal then rebuilds, which
makes the instability cyclic. In the JOREK simulations reviewed by
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§5.1), the onset of type-I
ELMs is a coupled peeling–ballooning instability. It combines the
pressure-driven [ballooning mode](/definitions/ballooning-mode.md) with the
current-driven peeling (edge kink) mode. In the resistive non-linear model, a
peeling–tearing mode takes the place of the ideal external kink.
[Ebrahimi & Bhattacharjee (2023)](/sources/ebrahimi-2023.md) (p. 1) use the
same definition for their NIMROD study and call the coupled modes
"ideal-like".

The mode is three-dimensional, nonlinear and spans many toroidal harmonics, so
nonlinear initial-value codes are the tools of choice. Hoelzl et al. (2021,
§5.1) note that ELM thresholds from linear codes compare worse with experiment
than JOREK's nonlinear thresholds (their ref. [45]).

## ELM dynamics in nonlinear simulations

Hoelzl et al. (2021, §5.1) summarize the following [JOREK](/software/jorek.md)
results.

- **Filaments and sheared flows.** The filaments are sheared by an
  axisymmetric ($n=0$) flow driven by the Maxwell stress.
- **ELM types and heat loads.** The simulations distinguish conductive from
  convective ELMs. Homoclinic tangles split the strike lines.
- **Nonlinear coupling.** In ASDEX Upgrade, low-$n$ harmonics are excited
  nonlinearly as a solitary magnetic perturbation.
- **Divertor heat load.** The Eich scaling of the ELM energy fluence in JET
  is reproduced. Background flows make it slightly underestimated.
- **ELM cycles.** Multiple type-I ELM cycles in realistic ASDEX Upgrade
  geometry were obtained "for the first time". Diamagnetic drift is
  "imperative" for cycling, and the ELM frequency rises with heating power.
  This makes extended (diamagnetic) MHD, not ideal or single-fluid
  resistive MHD alone, the minimum model for ELM cycles (see the
  qualification on NIMROD "cycles" below).
- **Bootstrap current.** The self-consistent bootstrap current that
  rebuilds the edge current between crashes is part of the cycle model.
  [Saxena et al. (2025)](/sources/saxena-2025.md) (§1) cite JOREK's Sauter
  implementation for ELM cycles. See
  [bootstrap current](/definitions/bootstrap-current.md).

### Nonlinear coupling of toroidal harmonics

Three later sources make the "low-$n$ harmonics are excited nonlinearly"
statement specific.

- **Three-wave rule.** A harmonic $n_3=n_1\pm n_2$ is driven by the pair
  $(n_1,n_2)$ with growth rate $\gamma_{n_3}=\gamma_{n_1}+\gamma_{n_2}$; when
  several pairs contribute, the dominant pair mostly sets the rate
  ([Cathey et al. (2023)](/sources/cathey-2023.md), §3.1, after Krebs et al.
  2013 as cited; [Cathey et al. (2024)](/sources/cathey-2024.md), §3.4). In
  the EDA case of Cathey et al. (2023, Fig. 5) the linearly stable
  $n=1$–3, 12 and 13 grow early in the nonlinear phase at about
  $4$–$6\times10^4$ s$^{-1}$, against a linear peak of about
  $2.7\times10^4$ s$^{-1}$ (figure readings), as the rule predicts. In a
  predictive HL-3 QH-mode run $n=1$ is excited at about 16 ms by $n=2$ and
  $n=3$ with $\gamma_{n=1}\approx\gamma_{n=2}+\gamma_{n=3}$, and the growth
  of $n=4$, 5, 10 and 11 changes through coupling
  ([Liang et al. (2025)](/sources/liang-2025.md), §IV B 1, Fig. 7a).
- **NIMROD.** In DIII-D peeling–ballooning ELMs, intermediate-$n$
  ballooning modes ($n=10$–14) grow linearly, and the low-$n$ peeling-parity
  modes ($n=1$–6), stated to be linearly stable, and $n\ge20$ grow by
  coupling ([Ebrahimi & Bhattacharjee (2023)](/sources/ebrahimi-2023.md),
  p. 2, Fig. 2a). This agrees with the JOREK picture on a second code.
- **ELMs and $n=1$.** Adjacent moderate-$n$ peeling–ballooning modes
  ($n$ and $n+1$, about 6–8) interact nonlinearly to produce an $n=1$
  perturbation ([Howell et al. (2022)](/sources/howell-2022.md), §I, citing
  Pankin 2007); see the next section.

### ELMs as seeds of tearing modes

In DIII-D ITER-baseline discharge 174446, ELMs at 3335 and 3363 ms are
followed by a small, slowly growing $n=1$ signal, and the ELM at 3396 ms
triggers a robustly growing $2/1$ neoclassical tearing mode
([Howell et al. (2022)](/sources/howell-2022.md), §III A, Fig. 2,
experimental). Howell et al. replace the ELM in NIMROD by a transient
boundary magnetic perturbation as a seed (see
[resonant magnetic perturbations](/definitions/resonant-magnetic-perturbation.md)).
In that simulation the reconstructed pedestal flow shear is needed to
stabilize the peeling–ballooning modes, i.e. to keep ELMs out (§III A,
stated).

### Reconnection and current relaxation in peeling–ballooning ELMs (NIMROD)

[Ebrahimi & Bhattacharjee (2023)](/sources/ebrahimi-2023.md) describe three
phases in a resistive-MHD NIMROD run at Spitzer resistivity with 43
toroidal modes (p. 2, Figs. 2–4):

1. linear growth of intermediate-$n$ ballooning modes with nonlinearly
   driven low-$n$ peeling modes;
2. saturation with a "secondary nonlinear surge" of several
   peeling–ballooning modes and nonlinear generation of axisymmetric
   (zonal) poloidal fields and currents;
3. relaxation, as the modes "nonlinearly suppress the edge current, as well
   as peeling it away".

The zonal fields drive an axisymmetric toroidal current sheet of sign
opposite to the equilibrium edge current, which removes the peeling drive;
finger-like non-axisymmetric current sheets break into small current blobs,
read as 3D [plasmoid-mediated reconnection](/definitions/plasmoid-instability.md).
In the modal decomposition the $n=1$ and $n=2$ currents surround the whole
device and dominate on the high-field side (peeling structure), while the
nonlinear $n=12$ current spreads poloidally far beyond its linear
localization (Fig. 4). A second DIII-D equilibrium reproduces both current
sheets and the $n=0$ counter-current (Fig. 6).

### Pedestal collapse in a full annulus

[Seto et al. (2023)](/sources/seto-2023.md) (§5) simulate a pedestal collapse
with [BOUT++](/software/bout-plus-plus.md). They use a four-field two-fluid
reduced-MHD model of drift-wave resistive ballooning modes (DWRBM). It
contains ion diamagnetism, gyroviscous cancellation and hyper-resistivity,
on the marginally IBM-unstable cbm18_dens4 equilibrium.

- **Diagnostic.** The pedestal energy loss is
  $\Delta W_{\mathrm{ped}}/W_{\mathrm{ped}}$: the integral of the pressure
  perturbation over the pedestal volume divided by the integral of the
  equilibrium pressure there (Eq. 36).
- **Field solver.** The collapse needs the $n=0$ and low-$n$ components,
  which the flute-ordered field solver cannot treat. The authors therefore
  use the [hybrid 2D/1D field solver](/methods/hybrid-2d-1d-field-solver.md).
  A scan of the largest $n$ handled by the 2D solver, over 4, 8 and 12,
  changes the result very little (Fig. 6).
- **Full torus vs quarter torus** (§5.3, Figs. 7–8).
  - Both domains reach a similar final energy loss, about 0.065–0.07 read
    from Fig. 7a, and nearly identical pressure profiles at $450\,\tau_A$.
  - The collapse paths differ. In the quarter torus, the linearly unstable
    high-$n$ modes trigger the collapse directly, at about $231\,\tau_A$
    (in the two-crash reading of Seto et al. (2024) the two crashes there
    are only $3\,\tau_A$ apart).
  - In the full torus, these modes saturate at about $210\,\tau_A$. Low-$n$
    and zonal modes grow first and the spectrum peak shifts down. The
    collapse comes later, at about $313\,\tau_A$, and the down-shifted modes
    trigger it. Seto et al. (2024) identify this collapse as the second of two
    crashes and the saturation at about $210\,\tau_A$ as the first (bullet
    "Two crashes, not one" below).
  - The authors conclude that a wedge domain "may be enough" for the final
    energy-loss level, but the full annulus is needed to simulate the loss
    process self-consistently. This rests on one case. Seto et al. (2024)
    add a half-torus run that falls between the two and attribute the
    difference to the finer $2N/N$ fundamental islands of a $2\pi/N$ wedge,
    which stochastize sooner (§III, Figs. 13–15).
- **Global $(2,1)$ structure.** After the full-torus collapse, a global
  $(m,n)=(2,1)$ structure with
  [tearing](/definitions/tearing-mode.md) parity coexists with the high-$n$
  filaments (§5.3, Figs. 9–10).
- **Two crashes, not one** ([Seto et al. (2024)](/sources/seto-2024.md),
  same authors; the same run by the compiler's identification). The energy-loss rate of the full-torus run has
  two peaks: a small first crash when the linear modes saturate, with $2/1$
  islands at $q=2$ and turbulence only near their X-points, and the main
  second crash $103\,\tau_A$ later, when the island harmonics have
  stochastized $q=2$ and down-shifted middle-$n$ turbulence covers the flux
  surface. The interval is $64\,\tau_A$ for a half torus and $3\,\tau_A$ for
  a quarter torus, and the final loss stays at about 6% of the pedestal
  energy for all three. The 2023 saturation at about $210\,\tau_A$ and
  collapse at about $313\,\tau_A$ are therefore the first and the second
  crash (compiler's cross-check: the 2023 difference, $103\,\tau_A$, equals the
  2024 crash interval). Full account on
  [two-stage ELM crash](/results/two-stage-elm-crash.md).
- **Cost.** The full-torus run cost $8.3\times10^5$ core-hours, about 40% of
  it in the field solver (§5.3).

### Natural ELMs in ITER scenarios

[Becoulet et al. (2022)](/sources/becoulet-2022.md) (§3, Figs. 2–3) run
JOREK, with two-fluid diamagnetic terms, toroidal rotation and neoclassical
poloidal friction, on three ITER H-mode scenarios at 5.3 T, seeding
$n=1$–9. At 15 MA the most unstable harmonics are $n=2$–4 and the ELM loses
4 MJ; at 12.5 MA an $n=5$ precursor is followed by an $n=7,9$ crash that
loses 2 MJ; at 10 MA (a high-$\beta_p$ steady-state scenario) the $n=3$ mode
saturates and rotates in the electron diamagnetic ($E\times B$) direction
with no crash, a QH-mode-like state. Diamagnetic effects and rotation are
stated to be the most important factors for the rotation of the ballooning
modes before the crash (§3, attributed).

### ELMs as an unwanted side effect

High-$n$ edge-localized modes also go unstable in a 3D VDE simulation when the
diffusivities are not raised. They were suppressed on purpose in the
NSTX benchmark, because that benchmark targets low-$n$ wall forces
([Artola et al. (2021)](/sources/artola-2021.md), §4.1.1; see
[vertical displacement events](/definitions/vertical-displacement-event.md)).

## Regimes without large ELMs

[Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (§2.1) review JOREK
simulations of three naturally ELM-free or small-ELM regimes.
[Cathey et al. (2024)](/sources/cathey-2024.md) compare the three ASDEX
Upgrade cases side by side, with reduced MHD, diamagnetic terms and a
Sauter bootstrap source, and [Cathey et al. (2023)](/sources/cathey-2023.md)
is the primary EDA paper. Pedestal parameters of the three discharges at
$\psi_N=0.95$ (Cathey et al. 2024, Table 1):

| Regime | Average triangularity | $q_{95}$ | $\beta_p$ | $n_{e}$ (m$^{-3}$) | $T_{e}$ (eV) |
|---|---|---|---|---|---|
| QH-mode (#39279) | 0.38 | 6.8 | 1.50 | $1.74\times10^{19}$ | 831 |
| Small ELMs (QCE proxy) | 0.24 | 5.4 | 0.69 | $4.52\times10^{19}$ | 281 |
| EDA H-mode (#36330) | 0.41 | 5.3 | 0.91 | $6.70\times10^{19}$ | 328 |

- **Small ELMs and the quasi-continuous exhaust (QCE) regime.**
  - ASDEX Upgrade simulations at low triangularity "agree qualitatively"
    with the QCE regime.
  - They change to large ELMs at higher heating power and at sufficiently
    low separatrix density.
  - Hoelzl et al. (2021, §5.1) list earlier small-ELM work.
  - In the case reviewed by Cathey et al. (2024, §3.3, Fig. 4), a type-I
    ELMy discharge with the separatrix density raised artificially develops
    quasi-continuous activity. Pedestal fluctuations at the outboard
    midplane are at 20–40 kHz, "qualitatively similar" to QCE observations.
    The dominant modes, $n=8$ and 10 near the separatrix, are identified as
    resistive peeling–ballooning modes by their resistivity sensitivity and
    phase velocity.
  - Lowering the separatrix density gives a type-I ELM, consistent with the
    experimental access condition of a separatrix density above about 0.3 of
    the Greenwald density. Raising the heating power also ends the small
    ELMs within a few ms, and a type-I ELM follows at about 20 ms. The stated
    reasons are a lower resistivity ($\eta\propto T^{-3/2}$) and stronger
    diamagnetic and $E\times B$ flows, both of which remove drive from the
    resistive peeling–ballooning modes (§3.3, mechanism stated).
- **EDA H-mode.**
  - The MHD activity fluctuates and low-$n$ harmonics ($n=1$–3) dominate it.
  - The pedestal fluctuation frequencies fall in the experimental range
    (Fig. 1).
  - (These two items are the review's summary of the primary paper below;
    see Contradictions for the dominant $n$.)
  - *Primary result.* JOREK starts from the CLISTE reconstruction of the
    argon-seeded EDA discharge #36330. Ideal analysis (MISHKA) places the
    operational point just inside the $n\approx15$ ballooning boundary, but
    at realistic resistivity resistive peeling–ballooning modes are
    unstable for $n=5$–11, most strongly $n=6$–9, peaking at the maximum
    of $\nabla T_e$ near $\psi_N\approx0.98$
    ([Cathey et al. (2023)](/sources/cathey-2023.md), §2.1, §3, Figs. 2,
    5–6; see [ballooning mode](/definitions/ballooning-mode.md)).
  - In the nonlinear phase the dominant $n$ shifts down, through nonlinear
    energy transfer and through the depletion of the pedestal density
    (§4.1, Fig. 9; Cathey et al. 2024, §3.5). An ergodic layer forms outside
    $\psi_N\approx0.965$ and the pedestal loses about 2.5 MJ/s of heat and
    $6.9\times10^{21}$ ions/s continuously, unlike the transient losses of
    JOREK type-I ELMs; density falls more than $T_e$ (Cathey et al. 2023,
    §4.2, Fig. 10).
  - Local fluctuation levels relative to the toroidal average are about 50%
    in $T_e$ and 40% in $n_e$ at $\psi_N\approx0.98$ (§4.3, Fig. 11).
  - The fluctuation frequency is about 35 kHz in the linear and early
    nonlinear phase and chirps down to 8–18 kHz (about 13 kHz in the
    abstract) as the radial-electric-field well becomes shallower (§4.3).
    The measured quasi-coherent mode (QCM) is at 20–40 kHz. The simulated
    poloidal wavenumber, 0.1–0.5 cm$^{-1}$, is below the QCM values
    (0.6–0.9 cm$^{-1}$ in AUG) and closer to those measured in the QCE
    regime (§4.3). The authors conclude only that the simulated modes
    "could be related" to the QCM (§4.3, §5).
- **QH-mode.**
  - A saturated kink-peeling mode forms the edge harmonic oscillation (EHO),
    first shown for DIII-D (Hoelzl et al. 2021, §5).
  - ASDEX Upgrade simulations recover the EHO in the density. At higher
    pedestal density the regime gives way to large ELMs (Hoelzl et al. 2024,
    Fig. 2).
  - "$q_{95}$ windows" exist inside which QH-mode can exist. In those
    windows, external-kink formation prevents the pedestal from building up
    to an ELM.
  - A nonlinear drop of $q_{95}$, from current redistribution including the
    self-consistent bootstrap current, lowers the growth rates. It acts as a
    saturation mechanism.
  - In ITER $Q=10$ and ASDEX Upgrade QH-mode cases, low-$n$ harmonics
    ($n=1$–3) dominate at an $E\times B$ velocity of about 20 km/s (Hoelzl
    et al. 2021, §5).
  - *Detail of the AUG case* (Cathey et al. 2024, §3.2, Fig. 3; $n=0$–6
    kept). Only $n=1$ and 2 are linearly unstable; $n=2$ grows faster, but
    $n=1$ dominates the saturated state, with the energy of the higher
    harmonics falling steeply with $n$. The density fluctuation peaks at
    about 27 kHz, against about 10 kHz measured; the gap is attributed to the
    missing NBI torque and the single temperature. Raising the particle
    source gives a type-I ELM once the pedestal density exceeds about
    $2.3\times10^{19}$ m$^{-3}$, the threshold seen in the same discharge.
    Doubling the toroidal resolution leaves the EHO unchanged (fn. 10).
  - In the ITER 10 MA scenario the saturated $n=3$ QH-like mode locks to a
    static $n=3$ RMP, with strong density transport and almost unchanged
    $T_e$ ([Becoulet et al. (2022)](/sources/becoulet-2022.md), §5).
  - *Predictive HL-3 case* ([Liang et al. (2025)](/sources/liang-2025.md)).
    JOREK reduced MHD with diamagnetic terms, no momentum source, reaches a
    QH-mode at $q_{95}=2.5$ dominated by a saturated $n=2$ kink-peeling mode,
    with only $n=2$ and 3 linearly unstable; the edge harmonic oscillation
    has a 7.5 kHz fundamental and differs between the high- and low-field
    sides. At $q_{95}=2.3$ the QH-mode is lost and an ELM-like burst removes
    about 3% of the thermal energy in about 1 ms after an $n=8$ precursor
    (§IV B–C, Figs. 7, 13–20). The access contrast with the higher-$q$ AUG
    windows is drawn by the authors (§IV C).
  - The saturated mode, its frequency and its structure across the three
    devices are on [edge harmonic oscillation and QH-mode](/definitions/edge-harmonic-oscillation.md).
- **Spectra compared** (Cathey et al. 2024, §3.5, Fig. 6). In the small-ELM
  and EDA cases the linearly dominant modes are resistive, ballooning
  (low-field-side) modes at medium-to-high $n$, and the nonlinear spectra are
  flat, with active energy exchange. In QH-mode the linearly dominant mode
  is an $n=2$ kink-peeling mode, slower than the resistive
  peeling–ballooning modes, overtaken later by $n=1$, and the nonlinear
  spectrum falls steeply with $n$.
- **JT-60SA outlook.** Linear JOREK scans of JT-60SA scenario 4-1 show that
  the unstable pedestal spectrum narrows from $n=1$–30 at ten times the
  realistic resistivity to $n=3$, 6 and 9 at realistic resistivity, with
  flows included (Cathey et al. 2024, §4; details on
  [ballooning mode](/definitions/ballooning-mode.md)).

## Active ELM control

- **Resonant magnetic perturbations (RMPs).** Full treatment on
  [resonant magnetic perturbations](/definitions/resonant-magnetic-perturbation.md).
  - Simulations show screening of the vacuum field by the plasma response,
    then mitigation and then suppression, with locking to the RMP field.
    Nonlinear mode coupling is essential (Hoelzl et al. 2021, §5).
  - JOREK–STARWALL makes the RMP model free-boundary and recovers the
    measured flux-surface corrugation (Hoelzl et al. 2024, §2.2; see
    [resistive-wall coupling](/methods/resistive-wall-coupling.md)).
  - An island forms at the pedestal top in ELM-suppressed ASDEX Upgrade
    plasmas (that experimental paper was still submitted when reviewed).
  - Adding electron polarization drift and neoclassical toroidal viscosity
    recovers the KSTAR density pump-out, through stepwise growth of the
    $5/1$ and $6/1$ islands. Island-mediated mode coupling reproduces RMP
    ELM suppression in KSTAR (Fig. 3).
  - ITER predictions put suppression within the coil-current design limits
    (Hoelzl et al. 2024, §2.2). The primary result: in the 15 MA scenario,
    $n=3$ RMPs suppress the crashes above a peak coil current of about
    45 kAt (45–60 kAt in the abstract) against a 90 kAt limit, and $n=2$, 3
    and 4 at 60 kAt all replace the crash by saturated "edge MHD turbulence"
    ([Becoulet et al. (2022)](/sources/becoulet-2022.md), §4, Figs. 5, 7).
- **Pellet ELM triggering.**
  - DIII-D: the triggering threshold lies between 1.5 and 1.8 mm pellets.
  - ASDEX Upgrade: the lag time after an ELM, during which pellets fail to
    trigger, is reproduced.
  - (Hoelzl et al. 2021, §5; Hoelzl et al. 2024, §2.3.)
  - Triggered ELMs reduce the peak heat flux less than hoped, because a
    smaller wetted area cancels part of the benefit. This matches the
    experiments (Hoelzl et al. 2024, §2.3).
- **Vertical kicks.** Downward plasma motion destabilizes peeling–ballooning
  modes by raising the edge current (Hoelzl et al. 2021, §5).

## Qualifications

- **Reviews, not evidence.** The JOREK ELM results taken from Hoelzl et al.
  (2021, 2024) come from two reviews. They point to the original papers and
  give no growth rates or convergence data of their own. Hoelzl et al.
  (2024) contain no equations. Several items rest on submitted papers or
  private communications at the time of review (the AUG pedestal-top island;
  the HL-2A mitigation threshold). Cathey et al. (2024) is itself largely a
  comparative review of the authors' earlier papers.
- **Conditional agreement.** The qualitative agreement with QCE and the
  conclusions on the full annulus each rest on a few cases, as stated above.
- **"ELM cycles" in single-fluid MHD.** Ebrahimi & Bhattacharjee (2023, p. 2,
  Fig. 3c) report "two ELM cycles" in a resistive single-fluid NIMROD run,
  which seems to contradict the JOREK finding that diamagnetic drift is
  imperative for cycling. The two use the word for different phenomena. The
  NIMROD "second cycle" is a second burst about 1 ms after the first, in a
  run without described heating or current sources, so the pedestal cannot
  have been rebuilt by transport; it is a renewed release of
  peeling–ballooning drive not yet exhausted. The JOREK cycle is crash,
  inter-ELM rebuild by sources, crash. Recorded as a terminological
  qualification, not as a contradiction.
- **Single temperature and missing torque.** The AUG EDA and QH runs use one
  temperature and no NBI torque source. The simulated radial-electric-field
  well is therefore too deep in the linear phase ($-29$ kV/m against the
  measured $-20\pm4$ kV/m in EDA), which affects intermediate- and high-$n$
  stability and the QH frequency (Cathey et al. 2023, §2.2; Cathey et al.
  2024, §2.3, §3.2). Cathey et al. (2023) state both that the nonlinear
  well "matches" the measurement (§2.2, Fig. 4) and that it is shallower,
  about $-15$ kV/m (§4.3); the time of the Fig. 4 profile is not given.
- **Mode velocity frames.** In EDA the simulated mode moves at about
  $-15$ km/s (electron diamagnetic direction) in the laboratory frame and
  at about $+1$ km/s (ion diamagnetic) in the plasma frame where its
  amplitude peaks (Cathey et al. 2023, §3.2, Fig. 7); the "1 km/s in the ion
  diamagnetic direction" of Cathey et al. (2024, §3.4) is the plasma-frame
  value. C-Mod measures 7–15 km/s in the plasma frame, so the direction
  agrees and the magnitude does not.
- **Resistivity in the HL-3 case.** The edge resistivity is about 4 times
  Spitzer ($2.6\times10^{-6}$ Ω m at 500 eV against a neoclassically
  corrected realistic value of $0.7\times10^{-6}$ Ω m), because realistic
  values "would exceed the computational capability of present HPC
  resources"; no convergence study is shown and the ELM-like burst is
  stated to be under-resolved (Liang et al. 2025, §III, §IV C).
- **Resistivity and time span in ITER.** The ITER RMP and natural-ELM runs
  use a resistivity about two orders above realistic and cover a few tens of
  ms (Becoulet et al. 2022, §2, §7); the published version of that paper was
  not read.

## Contradictions

**Dominant toroidal harmonics in the simulated EDA H-mode — Open.**
[Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (§2.1, Fig. 1) state that
the fluctuating MHD of the AUG EDA simulation is dominated by low-$n$
harmonics, $n=1$–3. The primary paper,
[Cathey et al. (2023)](/sources/cathey-2023.md), finds a linear phase
dominated by $n=6$–9, and in the time-averaged nonlinear spectra $n=2$ and 3
dominate with $n=1$ weaker ($n=3>2>1\approx4$ by eye, Fig. 9); the same
paper also writes the nonlinear dominant set as $n=2$–5 (§4 intro) and as a
shift "from $n=7$ to $n=3$" (§5). [Cathey et al. (2024)](/sources/cathey-2024.md)
(§3.4–3.5, Fig. 6) repeat the linear $n=6$–9, report only a shift
"towards lower toroidal mode numbers" in the nonlinear phase, and show a
flat EDA spectrum with no clear low-$n$ dominance. The statements differ in
the phase and the spectral measure they describe. A time-resolved spectrum
of the EDA run with the averaging window stated, or the authors'
explicit choice of one description, would settle it.

# Citations

- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §5 (ELMs §5.1; pellets, kicks, RMPs, QH-mode in §5).
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §2.1–2.3, Figs. 1–3.
- [Cathey et al. (2023)](/sources/cathey-2023.md) — §§1–5, Figs. 2–11.
- [Cathey et al. (2024)](/sources/cathey-2024.md) — §§2–4, Table 1, Figs. 3–8.
- [Becoulet et al. (2022)](/sources/becoulet-2022.md) — §§2–5, §7, Figs. 2–14.
- [Ebrahimi & Bhattacharjee (2023)](/sources/ebrahimi-2023.md) — pp. 1–5, Figs. 2–6.
- [Howell et al. (2022)](/sources/howell-2022.md) — §I, §III A, Fig. 2.
- [Seto et al. (2023)](/sources/seto-2023.md) — §5, Eqs. 28–37, Figs. 5–10.
- [Artola et al. (2021)](/sources/artola-2021.md) — §4.1.1.
- [Saxena et al. (2025)](/sources/saxena-2025.md) — §1.
- [Seto et al. (2024)](/sources/seto-2024.md) — §§I–IV, Figs. 3, 10–15.
- [Liang et al. (2025)](/sources/liang-2025.md) — §§III–V, Figs. 7, 13–20.

---
type: Definition
title: "Edge-localized mode (ELM) and ELM-free regimes"
description: "Repetitive edge MHD instability of the H-mode pedestal, set off by coupled peeling-ballooning modes, that expels pedestal energy and particles in filaments; with the naturally ELM-free or small-ELM regimes (QH-mode, EDA H-mode, QCE) and the active control methods (RMPs, pellets, vertical kicks) as reproduced by nonlinear MHD codes."
status: established
aliases: [ELM, type-I ELM, ELM crash, pedestal collapse, QH-mode, EDA H-mode, QCE, ELM suppression]
tags: [elm, pedestal, edge, ballooning, mhd, extended-mhd, tokamak]
timestamp: 2026-10-16T00:00:00Z
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
  resistive MHD alone, the minimum model for ELM cycles.
- **Bootstrap current.** The self-consistent bootstrap current that
  rebuilds the edge current between crashes is part of the cycle model.
  [Saxena et al. (2025)](/sources/saxena-2025.md) (§1) cite JOREK's Sauter
  implementation for ELM cycles. See
  [bootstrap current](/definitions/bootstrap-current.md).

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
    high-$n$ modes trigger the collapse directly, at about $231\,\tau_A$.
  - In the full torus, these modes saturate at about $210\,\tau_A$. Low-$n$
    and zonal modes grow first and the spectrum peak shifts down. The
    collapse comes later, at about $313\,\tau_A$, and the down-shifted modes
    trigger it.
  - The authors conclude that a wedge domain "may be enough" for the final
    energy-loss level, but the full annulus is needed to simulate the loss
    process self-consistently. This rests on one case.
- **Global $(2,1)$ structure.** After the full-torus collapse, a global
  $(m,n)=(2,1)$ structure with
  [tearing](/definitions/tearing-mode.md) parity coexists with the high-$n$
  filaments (§5.3, Figs. 9–10).
- **Cost.** The full-torus run cost $8.3\times10^5$ core-hours, about 40% of
  it in the field solver (§5.3).

### ELMs as an unwanted side effect

High-$n$ edge-localized modes also go unstable in a 3D VDE simulation when the
diffusivities are not raised. They were suppressed on purpose in the
NSTX benchmark, because that benchmark targets low-$n$ wall forces
([Artola et al. (2021)](/sources/artola-2021.md), §4.1.1; see
[vertical displacement events](/definitions/vertical-displacement-event.md)).

## Regimes without large ELMs

[Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (§2.1) review JOREK
simulations of three naturally ELM-free or small-ELM regimes.

- **Small ELMs and the quasi-continuous exhaust (QCE) regime.**
  - ASDEX Upgrade simulations at low triangularity "agree qualitatively"
    with the QCE regime.
  - They change to large ELMs at higher heating power and at sufficiently
    low separatrix density.
  - Hoelzl et al. (2021, §5.1) list earlier small-ELM work.
- **EDA H-mode.**
  - The MHD activity fluctuates and low-$n$ harmonics ($n=1$–3) dominate it.
  - The pedestal fluctuation frequencies fall in the experimental range
    (Fig. 1).
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

## Active ELM control

- **Resonant magnetic perturbations (RMPs).**
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
    (Hoelzl et al. 2024, §2.2).
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

- **Reviews, not evidence.** The JOREK ELM results above come from two
  reviews. They point to the original papers and give no growth rates or
  convergence data of their own. Hoelzl et al. (2024) contain no equations.
  Several items rest on submitted papers or private communications at the
  time of review (the AUG pedestal-top island; the HL-2A mitigation
  threshold).
- **Conditional agreement.** The qualitative agreement with QCE and the
  conclusions on the full annulus each rest on a few cases, as stated above.

## Contradictions

None open.

# Citations

- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §5 (ELMs §5.1; pellets, kicks, RMPs, QH-mode in §5).
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §2.1–2.3, Figs. 1–3.
- [Seto et al. (2023)](/sources/seto-2023.md) — §5, Eqs. 28–37, Figs. 5–10.
- [Artola et al. (2021)](/sources/artola-2021.md) — §4.1.1.
- [Saxena et al. (2025)](/sources/saxena-2025.md) — §1.

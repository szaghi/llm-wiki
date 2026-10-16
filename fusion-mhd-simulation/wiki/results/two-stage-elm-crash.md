---
type: Result
title: "Two-stage crash of resistive drift-ballooning ELMs"
description: "In BOUT++ full-annulus simulations a pedestal collapse driven by resistive drift-ballooning modes proceeds in two crashes: the saturating linear modes first nonlinearly create 2/1 islands with turbulence confined to their X-points, and the main loss follows when the island harmonics have stochastized q = 2 and down-shifted middle-n turbulence covers the surface; the interval shrinks from 103 to 3 Alfvén times as the toroidal wedge number grows from 1 to 4, while the final loss stays about 6% of the pedestal energy."
status: established
aliases: [two-stage ELM crash, two-step pedestal collapse, RDBM ELM crash, wedge-number effect on ELM crash]
tags: [elm, pedestal, ballooning, tearing, reduced-mhd, finite-differences, edge]
timestamp: 2026-10-16T18:00:00Z
---

# Two-stage crash of resistive drift-ballooning ELMs

**Statement.** In a full-annulus [BOUT++](/software/bout-plus-plus.md)
simulation of a pedestal collapse ("ELM crash") driven by resistive
drift-ballooning modes (RDBM), the rate of pedestal energy loss has two
peaks. The first crash is triggered directly by the saturating linear
RDBMs, whose nonlinear coupling generates $m/n=2/1$ magnetic islands at
$q=2$; turbulence and heat flux then stay confined around the island
X-points and little energy is lost. The second, main crash comes when the
higher harmonics of the island have overlapped and stochastized the $q=2$
region, so that turbulence spreads over the whole flux surface; it is
triggered by down-shifted middle-$n$ turbulence, not by the low-$n$ modes
([Seto et al. (2024)](/sources/seto-2024.md), Abstract, §III–IV). The
interval between the crashes shrinks as the simulated toroidal wedge
narrows, while the final energy loss does not change.

## Setting

* **Model.** A scale-separated four-field two-fluid
  [reduced-MHD](/methods/reduced-mhd.md) model (vorticity, parallel vector
  potential, pressure and parallel ion flow) with ion diamagnetism through a
  generalized flow potential, Chang–Callen gyroviscous cancellation,
  constant resistivity and hyper-resistivity, flat ion density, and no
  equilibrium $E\times B$ or neoclassical poloidal flow (the equilibrium
  $E\times B$ flow cancels the ion diamagnetic flow) (Seto et al. 2024, §II,
  Eqs. 1–4; the model of Seto et al. 2020, as cited). It is the model that
  [Seto et al. (2023)](/sources/seto-2023.md) (§5.1) call the drift-wave
  resistive ballooning model (DWRBM).
* **Equilibrium and spectrum.** A TOQ shifted-circular equilibrium,
  marginally unstable to ideal ballooning, with $q=2$ at the peak of the
  pressure gradient; the linear spectrum peaks at $n=32$ with
  $\gamma\tau_A=7.86\times10^{-2}$ and is unstable for $11\le n\le52$
  (Seto et al. 2024, §II, Figs. 1–2). The same model, coefficients, grid and
  spectrum appear for the cbm18_dens4 case of Seto et al. (2023, §5), so the
  run is that case (compiler's identification; Seto et al. 2024 do not name
  the equilibrium). $\tau_A$ is a poloidal Alfvén time built on 3.5 m and
  2 T, not given in seconds.
* **Numerics.** The [hybrid 2D/1D field solver](/methods/hybrid-2d-1d-field-solver.md)
  with $0\le n\le4$ in the 2D solver and $4<n\le80$ in the flute-ordered 1D
  solver, $n\ge81$ removed by a low-pass filter; 1028 radial and 128
  parallel points and $256/N$ binormal points on a wedge $2\pi/N$, so the
  binormal spacing is the same for every $N$; initial perturbations on all
  harmonics except $n=0$ (Seto et al. 2024, §II).
* **Diagnostic.** The pedestal energy loss is the integral of the pressure
  perturbation over the volume inside the initial pressure-gradient peak,
  divided by the integral of the equilibrium pressure there (Eq. 5; Seto et
  al. 2023, Eq. 36, use the same definition). Per-$n$ budgets of
  perpendicular kinetic, magnetic and internal energy are split into linear
  and nonlinear transfer terms, the latter further into three-wave
  contributions of pairs $(n_1,n_2)$ to $n_3=|n_1-n_2|$ (Eqs. 6–29).

## The two stages ($N=1$, full torus)

| Event | Time | Energy loss (fraction of pedestal energy) |
|---|---|---|
| First crash (saturation of the $n=32$ kinetic energy, defines $t=0$) | $0$ | about 0.005 |
| Second crash | $103\,\tau_A$ | about 0.04 |
| End of run | $200\,\tau_A$ | about 0.063 |

(Seto et al. 2024, §III, Fig. 3; loss values read from the figure.)

1. **Before and at the first crash.** The $n=0$–4 magnetic energies grow at
   almost twice the rate of the $n=32$ magnetic energy, i.e. they are driven
   nonlinearly by RDBM pairs (Fig. 6). At $t=0$ the $n=32$-peaked RDBMs
   dominate the drive of the $n=0$ pressure deformation (Fig. 12a); a forward
   cascade to high $n$ and an inverse cascade to low $n$ follow, and the
   spectral peak shifts below $n=32$ (Figs. 4–5). The $n=1$ perturbation
   forms $2/1$ islands with [tearing](/definitions/tearing-mode.md) parity,
   produced by nonlinear parity mixing (Fig. 8, Fig. 10b–f).
2. **Between the crashes.** The radial $E\times B$ heat flux exists only in
   the stochastic region around the X-points of the $2/1$ island, whose
   width "seems to be determined by" the X-points of the $2/1$ and $8/4$
   islands (Fig. 10). Inside the islands the poloidal flow is laminar, and
   vortex-like flow and energy loss occur only outside them (Fig. 11). The
   harmonics $4/2$, $6/3$ and $8/4$ grow, overlap and stochastize $q=2$; at
   $50\,\tau_A$ the heat flux leaves through the two $8/4$ X-points
   (Fig. 10g–k).
3. **Second crash.** With $q=2$ fully stochastic, pressure and radial-flow
   filaments spread poloidally and vortices cover the domain (Fig. 11). At
   $50$ and $103\,\tau_A$ "a wide range of resonant modes with the
   down-shifted middle-n mode" drives the $n=0$ pressure deformation
   (Fig. 12). In the Maxwell-stress channel the pair $(n_1,n_2)=(1,0)$ feeds
   the $n=1$ kinetic energy at the first crash and at $50\,\tau_A$, and
   reverses sign at the second crash, returning energy to the magnetic field
   (Fig. 9).

**Interpretation by the authors.** "The m/n = 2/1 magnetic islands have the
stabilization effect" (§IV), and the first-crash coupling converts
perpendicular kinetic into magnetic energy, "effectively postponing the
substantial loss of the internal energy" (§IV). Large losses
"predominantly arise from the intricate overlaps of fine magnetic islands,
rather than the mere presence of low-n magnetic islands" (§IV). These are
interpretations: there is no run without islands and no computed ratio of
stochastic to island volume.

## Dependence on the toroidal wedge

| Wedge number $N$ (domain $2\pi/N$) | Fundamental islands | Crash interval | Final loss at $200\,\tau_A$ |
|---|---|---|---|
| 1 | $2/1$ | $103\,\tau_A$ | about 0.063 |
| 2 | $4/2$ | $64\,\tau_A$ | about 0.063–0.065 |
| 4 | $8/4$, already stochastic at $t=0$ | $3\,\tau_A$ | about 0.063–0.065 |

(Seto et al. 2024, §III–IV, Figs. 13–15; losses read from the figure.) A wedge
keeps only multiples of $N$, so its fundamental islands are $2N/N$; they are
finer, have more X-points and stochastize sooner, and for $N=4$ the two crashes
nearly coincide, so that "the RDBMs directly trigger the ELM crash",
consistent with the authors' earlier one-fifth-wedge work (Seto et al. 2020,
as cited). The peak loss rate is largest for $N=4$ (about 0.14 against 0.086
for $N=1$ and 0.06 for $N=2$, in units of $10^{-2}\tau_A^{-1}$, figure
reading). The authors conclude that "nonlinear interactions of all channels
in the full torus domain can significantly affect the trigger dynamics of
ELMs driven by the RDBMs" (Abstract, §IV).

## Relation to the earlier description of the same run

[Seto et al. (2023)](/sources/seto-2023.md) (§5.3) describe the full-torus
run as a single collapse at about $313\,\tau_A$, preceded by saturation of
the linearly unstable modes at about $210\,\tau_A$, and the quarter-torus
run as a collapse at about $231\,\tau_A$; the final losses agree, about
0.065–0.07. The difference $313-210=103\,\tau_A$ equals the first-to-second
crash interval of Seto et al. (2024), so the "collapse" of 2023 is the
*second* crash and the 2023 "saturation" is the first crash (compiler's
cross-check; Seto et al. 2024 state only that the full annulus
"qualitatively change[s]" the crash process relative to $N=4$ and that the
mechanism "has not been clarified in detail", §I). The two papers agree on
the down-shifted modes as the trigger; Seto et al. (2024) add the first
crash, the island mechanism and the $N=2$ case, and they report having
confirmed the $n=1$ tearing parity after the second crash in the 2023 work
(§III). This is a reinterpretation by the same authors, not a
contradiction; it is reflected on [edge-localized mode](/definitions/edge-localized-mode.md),
[BOUT++](/software/bout-plus-plus.md) and the
[hybrid 2D/1D field solver](/methods/hybrid-2d-1d-field-solver.md).

## Range of validity

* **Loss channels.** With constant hyper-resistivity and a linearized
  parallel Laplacian (no magnetic flutter), the stochastic electron heat
  transport of Rechester–Rosenbluth type and the stochastic
  hyper-resistivity of Kaw et al. are absent: "ELM energy loss in this work
  is driven by E × B convection and numerical diffusion"; with them, faster
  low-$n$ growth and larger stochastic losses "may be expected" (Seto et al.
  2024, §II, §IV, attributed).
* **One case.** One equilibrium, one parameter set, one run per $N$; no X-point
  and a domain inside the last closed surface (§II).
* **Version.** Read as the arXiv v1 preprint; the published version was not
  checked (Source page).

## Contradictions

None open. The timing reconciliation with Seto et al. (2023) above is a
compiler's cross-check of two papers by the same authors.

# Citations

- [Seto et al. (2024)](/sources/seto-2024.md) — Abstract, §§I–IV, Eqs. 1–34, Figs. 1–15.
- [Seto et al. (2023)](/sources/seto-2023.md) — §5.1, §5.3, Figs. 5–10.

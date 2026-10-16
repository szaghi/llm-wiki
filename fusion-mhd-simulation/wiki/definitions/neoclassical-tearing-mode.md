---
type: Definition
title: "Neoclassical tearing mode"
description: "A tearing mode that is classically stable but metastable: once a seed island exceeds a critical width, the loss of the bootstrap current inside the island drives its growth; simulated in NIMROD with heuristic neoclassical closures and a transient boundary perturbation that seeds a 2/1 NTM in a DIII-D ITER-baseline plasma through a time-ordered sequence of three-wave couplings."
status: established
aliases: [NTM, 2/1 NTM, neoclassical tearing, metastable tearing mode]
tags: [tearing, extended-mhd, bootstrap-current, tokamak, disruption]
timestamp: 2026-10-16T12:00:00Z
---

# Neoclassical tearing mode

A neoclassical tearing mode (NTM) is a [tearing mode](/definitions/tearing-mode.md)
whose drive comes from the helical perturbation of the
[bootstrap current](/definitions/bootstrap-current.md). The bootstrap current
is a pressure-gradient-driven parallel current that results from the viscosity
between trapped and passing particles. Inside a magnetic island the pressure
flattens, the bootstrap current disappears there, and the resulting helical
current deficit reinforces the island. In a plasma that is stable to classical
tearing the mode is therefore linearly stable but *metastable*: it needs a seed
island above a critical width, and once that width is exceeded it grows
([Howell et al. (2022)](/sources/howell-2022.md), §I, §III B). Howell et al.
(§I) call NTMs "the leading root physics mechanism that causes disruptions in
tokamaks" (see [disruption](/definitions/disruption.md)).

**Seeds.** Seeds come from transients that couple nonlinearly to the resonant
helicity: sawteeth (a $1/1$ sawtooth crash coupling to pre-existing $4/3$ and
$3/2$ islands seeds $2/1$ NTMs in the DIII-D ITER Baseline Scenario, a result
of Bardóczi et al. 2021 cited by Howell et al. 2022, §I; see
[sawtooth crash](/definitions/sawtooth-crash.md)) and
[edge-localized modes](/definitions/edge-localized-mode.md). For the ELM
channel, the $n$-th and $(n+1)$-th moderate-$n$ peeling–ballooning harmonics
($n\sim6$–8) interact nonlinearly to produce an $n=1$ perturbation (Pankin et
al. 2007, cited in §I). Removing the sawtooth removes one seed:
[magnetic flux pumping](/definitions/magnetic-flux-pumping.md) by a $1/1$
quasi-interchange keeps $q_0\ge1$ and thereby prevents sawteeth
([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §4.4). A different onset
path, a reversal of the resistive-interchange parameter by a hollow pressure
profile, is shown for classical tearing by
[radiation-triggered tearing](/results/radiation-triggered-tearing.md) and
proposed by [Zeng et al. (2023)](/sources/zeng-2023.md) (§1) as a possible
NTM seed at high $\beta$.

**Growth signature.** For an NTM the helical flux grows linearly in time; for
classically driven (Rutherford) tearing it grows quadratically (Howell et al.
2022, §III B, citing Qu & Callen and Rutherford). *Compiler's check:* this
follows from the [modified Rutherford equation](/definitions/modified-rutherford-equation.md)
with the helical flux $\propto w^2$ for island width $w$: a constant
$dw/dt$ gives $w^2\propto t^2$, and a bootstrap drive $\propto1/w$ gives
$w^2\propto t$.

## MHD implementation: heuristic neoclassical closures

Single-fluid MHD contains no trapped particles, so NTM simulations need a
closure. NIMROD uses the heuristic stress closures of Gianakon et al. (2002):
an ion stress that damps the poloidal flow toward its equilibrium value in the
momentum equation, and an electron stress in Ohm's law,
$\mathbf E=-\mathbf v\times\mathbf B+\eta\mathbf J-\frac{1}{n_ee}\nabla\cdot\mathsf\Pi_e$,
whose divergence is

$$\nabla\cdot\mathsf\Pi_e=-\nu_{{\rm pol},e}\,\frac{m_e}{e}\,\langle B_0^2\rangle\,\frac{(\mathbf J-\mathbf J_0)\cdot\mathbf e_\Theta}{(\mathbf B_0\cdot\mathbf e_\Theta)^2}\,\mathbf e_\Theta,$$

with $\nu_{{\rm pol},e}$ the (page-local) neoclassical electron poloidal-flow
damping rate, $\mathbf e_\Theta$ a basis vector along the equilibrium poloidal
field, subscript $0$ the equilibrium and $\langle B_0^2\rangle$ computed once
from it ([Howell et al. (2022)](/sources/howell-2022.md), §II A, Eqs. 5,
8–10). The electron force produces the bootstrap drive; the ion force gives
poloidal flow damping and the neoclassical polarization enhancement.
Subtracting $\mathbf v_0$ and $\mathbf J_0$ holds the equilibrium against
decay. The ion closure is valid to $O(m_e/m_i)$, the electron closure for
strong ion poloidal damping, and both assume $Z_{\rm eff}=1$ (§II A). This
is a third class of bootstrap implementation, next to the imposed
non-inductive currents of M3D-C1 and JOREK (see
[bootstrap current](/definitions/bootstrap-current.md)). XTOR, XTOR-2F, TM1
and JOREK's neoclassical ion friction use closures of the same family (§I).

## Seeding by a transient boundary perturbation

Howell et al. impose a transient normal field on the computational boundary
(the reconstructed separatrix), $\mathbf n\cdot\mathbf B=\mathbf n\cdot\mathbf B_{\rm mp}(\mathbf x)\,\mathrm{Env}(t)\,e^{i\omega t}$,
with $\mathbf B_{\rm mp}$ the $n=1$ Fourier component of the vacuum field of a
planar coil array and $\mathrm{Env}$ a compact-support bump function
$\exp[-1/(1-\tau^2)]$ on $\tau\in[-1,1]$, smooth to all orders. The modulation
frequency is chosen near the rotation of the resonant mode because linear
theory predicts the weakest flow screening there (§II B, Eqs. 11–12,
Fig. 1). The pulse lasts 1 ms and has a broad poloidal spectrum. Amplitude,
frequency and offset are not given.

## The DIII-D ITER Baseline Scenario simulation

**Case.** DIII-D shot 174446 at 3390 ms ($\beta_N\sim1.8$, $q_{95}\sim3.4$,
$q=2$ at 0.69 of a normalized toroidal-flux label whose square-rooting is not
stated), a kinetic EFIT with
reconstructed toroidal and poloidal flows; $q_0$ is raised above 1 to
suppress the $1/1$ kink and sawteeth, and pedestal flow shear suppresses
ELMs in the simulation (§III A, Figs. 3–4). Parameters at $q=2$ are within a
few times experiment: $S=2.5\times10^6$ against $7.9\times10^6$, Prandtl number
23 against 11, $\nu_{{\rm pol},e}=8\times10^5$ against $1.3\times10^5$ s$^{-1}$,
with the ratio $\nu_{{\rm pol},e}/(\nu_{ei}+\nu_{{\rm pol},e})=0.55$ against 0.43
(Table I). The fourth root of $\kappa_\parallel/\kappa_\perp$ is 100 against
260, so the anisotropy itself differs by a factor of about 46 (compiler's
check, recorded on the Source page).

**Evolution.** The $2/1$ helical flux rises and falls with the pulse, decays
until 1.5 ms, grows slowly until about 8 ms and then grows "robustly" and
linearly at about 3.4 Wb/s, against 3.3 Wb/s from a modified-Rutherford
analysis with the simulated parameters (§III B, Fig. 5A). That analysis is a
companion paper "in preparation"; the agreement rests on it. The island is
2–3 cm wide at 3 ms and 5 cm at 15 ms (Fig. 7). From about 4 ms a sequence of
core modes grows, $6/5$, then $5/4$ and $4/3$, then $3/2$; each peaks and
decays as the next grows, and their overlapping islands create a core
stochastic region that flattens the pressure inside $q=2$ (Figs. 5B, 7, 8).

**Energy transfer.** A generalization of the Ho–Craddock toroidal-Fourier
power analysis to shaped toroidal equilibria splits the power into each
harmonic into linear, quasi-linear, nonlinear, dissipative, advective and
Poynting-flux parts (App. A). During the slow phase nonlinear and linear power
contribute "roughly equally" to $n=1$; at 5 ms the $n=1$ nonlinear power peaks
near $q=6/5$, consistent with a $5+6\to1$ three-wave transfer, and at 8.39 ms
the $n=3$ and $n=2$ interactions dominate (Figs. 10, 12, 13). The seeding is
"a sequence of 3-wave coupling interactions that evolve in time", not a
single interaction (§IV). Resistive and neoclassical electron powers are
negative: they enable growth by changing the mode structure, not by
transferring power. The analysis resolves toroidal, not poloidal, harmonics
(§IV).

**Sensitivity (runs not shown).** A larger electron damping rate makes the
pulse alone trigger robust growth, followed by an inverse core sequence; a
smaller one lets the plasma return to quiescence (§V).

## Comparison with experiment and resilience

The experiment shows the same two-phase $2/1$ growth after successive ELMs and
a core-mode sequence ($4/3$, $3/2$ NTMs before the $2/1$). The core modes,
however, exist before the triggering ELM and evolve over about 100 ms, against
a few ms in the simulation, which the authors attribute partly to the enhanced
resistivity and modified core profiles (§V). The classical $\Delta'$ is
negligible in this plasma, so a $\Delta'$-based resilience assessment is
inadequate; the authors propose scans of the seeding amplitude as an NTM
resilience metric (§V).

## Contradictions

None open. The source's abstract speaks of two growth phases and §III B of
three; this is a printed inconsistency, recorded on the
[Source page](/sources/howell-2022.md).

# Citations

- [Howell et al. (2022)](/sources/howell-2022.md) — §I–V, Eqs. 1–16, Table I, Figs. 1–13, App. A.
- [Zeng et al. (2023)](/sources/zeng-2023.md) — §1 (resistive-interchange reversal as possible NTM seed).
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §4.4 (flux pumping removes the sawtooth seed).

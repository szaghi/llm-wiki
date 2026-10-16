---
type: Definition
title: "Energetic particle mode (EPM) and frequency chirping"
description: "Alfvénic mode whose existence and frequency are set by the energetic particles themselves rather than by a gap eigenmode of the bulk plasma, typically sitting in the shear-Alfvén continuum and dominated by a single poloidal harmonic; nonlinearly its frequency sweeps (chirps), and the codes of the NLED-AUG benchmark disagree on the sweep direction."
status: established
aliases: [EPM, energetic-particle mode, frequency chirping, chirping mode]
tags: [alfven-eigenmode, energetic-particles, hybrid-kinetic, tokamak]
timestamp: 2026-10-16T00:00:00Z
---

# Energetic particle mode (EPM) and frequency chirping

An energetic particle mode is a shear-Alfvénic mode that exists because of a
non-perturbative energetic-particle (EP) response. The EPs set its frequency;
it is not a normal mode of the bulk plasma that the EPs merely destabilize. It
sits in the shear-Alfvén continuum and needs an EP drive large enough to
overcome continuum damping
([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §IV.B, citing Chen
1994). Two criteria are used to separate it from a
[TAE](/definitions/toroidal-alfven-eigenmode.md):

- **Continuum location.** Bogaarts et al. identify the AUG-NLED $n=1$ mode as
  an EPM from its structure and from its frequency lying in the continuum,
  below the TAE gap
  ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §IV.B, Fig. 8).
- **Harmonic content.** Vlad et al. call the same mode an EPM because "its
  spectrum is dominated by the single $m=2$ harmonic". A TAE would show the
  characteristic $m,m+1$ pair. They apply this criterion even though the mode
  frequency lies "almost within the shear Alfvén toroidal gap"
  ([Vlad et al. (2025)](/sources/vlad-2025.md), footnote 1).

## The NLED-AUG EPM

In the off-axis-peaked [NLED-AUG case](/benchmarks/nled-aug-benchmark.md)
all codes find the same linear mode. It is an $n=1$ EPM dominated by $m=2$,
localized near the axis at $s\approx0.2$, where the EP density gradient is
positive ($\partial n_h/\partial s>0$, the EP profile being hollow)
([Vlad et al. (2025)](/sources/vlad-2025.md), §§3, 5, 6). The growth rate
rises linearly with the EP density gradient in JOREK, HYMAGYC and MEGA
([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), Fig. 9). Both JOREK
and MEGA find the dominant resonance at $v_{\parallel p}\approx-2\sqrt{T_h/m_h}$
(thermal speed as normalized by Bogaarts et al.) and none at the opposite sign (ibid., Fig. 10). Power-exchange analysis in HYMAGYC finds
the drive mainly from co- and counter-passing EPs in the inner half. Trapped
EPs give a subdominant outer drive about 10× weaker, which the authors link to
the late TAE ([Vlad et al. (2025)](/sources/vlad-2025.md), §3, Fig. 6).

The EPM saturates in HYMAGYC at $t\approx0.14$ ms, after a few overshoots.
Saturation fills the hollow EP core and lowers the mid-radius peak
([Vlad et al. (2025)](/sources/vlad-2025.md), §3, Fig. 13).

In the JOREK study of AUG #31213, $m=3$ EPMs are found at $t=0.6$ and
0.65 s, when $q>2.5$ in the core
([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §V, Table I).

## Frequency chirping

Chirping is the nonlinear sweep of a mode's frequency as the resonant EPs
are redistributed. In the NLED-AUG benchmark the sweep differs between codes
([Vlad et al. (2025)](/sources/vlad-2025.md), §§3–5):

- **Downward in HYMAGYC and MEGA.** The EPM chirps down, following the lower
  Alfvén continuum of the toroidal gap as the mode peak moves slightly
  outward (Fig. 3).
- **Upward in ORB5.** The EPM chirps up into the TAE gap. Its structure
  expands strongly in radius and overlaps the late external TAE, which the
  authors relate to core-to-edge EP transport.
- **Not reported in XTOR-K.**

Vlad et al. state the opposite direction plainly ("opposite to the one
observed by both HYMAGYC and MEGA", §5). They name candidate causes without
quantifying any of them: pressure versus current coupling, fast-ion inertia
(present in the fully gyrokinetic ORB5, absent in the hybrids) and particle
boundary conditions (§7).

## Contradictions

**EPM vs TAE labelling of the AUG-NLED $n=1$ mode.** Open.
The 2021 linear NLED-AUG benchmark (Vlad et al. 2021) called the off-axis
$n=1$ mode a TAE.
[Vlad et al. (2025)](/sources/vlad-2025.md) (footnote 1) reclassify it as
an EPM because a single $m=2$ harmonic dominates, while conceding that its
frequency lies almost within the toroidal gap.
[Bogaarts et al. (2022)](/sources/bogaarts-2022.md) (§IV.B, Fig. 8) had
already called it an EPM, but on the different criterion of continuum
location below the gap.

The two criteria are not equivalent. Harmonic content and location relative
to the gap can disagree, as they do here for a mode "almost within" the gap.
The 2021 paper is not ingested, so its argument is known only as restated.
A single stated criterion would settle it: for example, the existence of the
mode without EPs, or its frequency's dependence on EP parameters, applied to
one continuum computation (FALCON or HELENA/CASTOR) of the case.

**TAE vs EPM at $t=0.7$ s in AUG #31213.** Open, within one source.
[Bogaarts et al. (2022)](/sources/bogaarts-2022.md) list the $t=0.7$ s mode
as "TAE, m=2,3" in Table I and in the conclusion. The Fig. 16 caption calls
it "the m=2,3 coupled EPM mode". The $m=2,3$ coupling favours the TAE
reading under the Vlad et al. criterion. The paper itself does not resolve
it.

**Chirping direction.** Open (benchmark spread, recorded with the full spread
on the [NLED-AUG benchmark](/benchmarks/nled-aug-benchmark.md)). Down in
HYMAGYC and MEGA, up in ORB5, all within
[Vlad et al. (2025)](/sources/vlad-2025.md) (§§3–5).

# Citations

- [Vlad et al. (2025)](/sources/vlad-2025.md): the NLED-AUG EPM, its saturation and chirping, and the reclassification.
- [Bogaarts et al. (2022)](/sources/bogaarts-2022.md): EPM identification by continuum location in JOREK; the EPMs of AUG #31213; resonances.

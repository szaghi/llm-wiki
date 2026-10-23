---
type: Benchmark
title: "NLED-AUG energetic-particle benchmark"
description: "EUROfusion reference case built on ASDEX Upgrade discharge #31213 at 0.84 s with an off-axis-peaked Maxwellian energetic-deuteron population driving an n = 1 energetic particle mode; used for linear comparisons (JOREK against HYMAGYC, MEGA, ORB5) and for the first nonlinear four-code benchmark (HYMAGYC, MEGA, ORB5, XTOR-K), which agrees qualitatively and disagrees on chirping direction, saturation level and transport."
status: established
aliases: [NLED-AUG, NLED AUG reference case, AUG-NLED, "AUG #31213 NLED case"]
tags: [benchmark, verification, energetic-particles, hybrid-kinetic, alfven-eigenmode]
timestamp: 2026-10-16T16:51:00Z
---

# NLED-AUG energetic-particle benchmark

The NLED-AUG case is Lauber's (2016) EUROfusion reference case for
nonlinear energetic-particle dynamics. It is built on ASDEX Upgrade
discharge #31213 at $t=0.84$ s
([Vlad et al. (2025)](/sources/vlad-2025.md), §2, Table 1;
[Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §IV.B). The case has
an off-axis-peaked and an on-axis-peaked EP-density variant. The pages of
this bundle use the off-axis variant. Its most unstable mode is an $n=1$
[energetic particle mode](/definitions/energetic-particle-mode.md)
dominated by $m=2$ near the axis.

## Setup (Vlad et al. 2025, Table 1)

- **Equilibrium.** Fully shaped AUG equilibrium from EQDSK, rescaled with
  CHEASE to keep exactly $q_0\simeq2.39897$, which leaves the toroidal
  Alfvén gap fully open. COCOS = 2 with $B_\phi>0$ and $I_p>0$.
  $B=2.208$ T and $R_0=1.666$ m at the magnetic axis, $a=0.4826$ m.
- **Species.** Deuterium bulk ions and deuterium EPs, with
  $Z_in_i=n_e-Z_hn_h$ and $Z_i=Z_h=1$. On axis
  $n_{e}=0.1716\times10^{20}$ m$^{-3}$ and
  $n_{h}=0.00458\times10^{20}$ m$^{-3}$. The EP density peaks at
  $0.0215\times10^{20}$ m$^{-3}$ near $s\approx0.4$, and
  $n_{h0}/n_{i0}=0.0274$ on axis.
- **EP distribution.** Isotropic Maxwellian at uniform $T_h=93$ keV. The
  thermal speed is $\sqrt{T_h/m_h}=0.2535\,v_A$ (defined without the
  factor 2), and $\rho_L/a=0.0413$.
- **Normalization.** $\tau_A=R_0/v_A=2.000\times10^{-7}$ s with
  $v_A=8.329\times10^6$ m/s on axis.
- **Physics restrictions.** A single toroidal harmonic $|n|=1$ is kept. The
  EP nonlinearity is kept self-consistently and the fluid nonlinearity is
  omitted. The authors note that this omission is applied differently in each
  code: HYMAGYC's MHD is linear, MEGA's MHD is nonlinear, and XTOR-K filters
  its increments to $n=1$.
- **Radial coordinate.** $s=\sqrt{\psi_N}$.

The derived entries of Table 1 are internally consistent (reader's
recomputation). The Maxwellian is not a kinetic equilibrium. The δf codes
suppress the term that would relax it; XTOR-K and JOREK, being full-$f$, do
not (see the [δf method](/methods/delta-f-method.md)).

Bogaarts et al. (2022, §IV.B) use the same discharge and time with an
isotropic Maxwellian at 93 keV and off-axis EP peaking only. Their JOREK
runs are in reduced MHD with 51 × 64 elements and $10^7$ markers. They scan
the EP density gradient after relaxation in two ways: by scaling the marker
weights, or by modifying the initial profile.

## Linear results

**Vlad et al. (2025), Table 2.** The values are growth rate $\gamma$ and
$\omega/2\pi$. FOW means finite orbit width only (drift-kinetic); FLR adds
the gyroaverage.

| code | FOW $\gamma$ [s$^{-1}$] | FOW $\omega/2\pi$ [kHz] | FLR $\gamma$ [s$^{-1}$] | FLR $\omega/2\pi$ [kHz] |
|---|---|---|---|---|
| [HYMAGYC](/software/hymagyc.md), $(s,\theta)$ stress tensor | 174,606 | 180.02 | 199,841 | 171.51 |
| HYMAGYC, $(R,Z)$ stress tensor | 231,090 | 162.42 | 215,570 | 163.00 |
| [MEGA](/software/mega.md) | 218,616 | 171.43 | 170,247 | 157.00 |
| [ORB5](/software/orb5.md) | 348,489 | 127.09 | 286,400 | 145.24 |

Normalized by $\tau_A$, $\gamma\tau_A$ spans about 0.035–0.070 (reader's
computation). ORB5 has the highest $\gamma$ and the lowest frequency in both
models: its $\gamma$ is 1.59× (FOW) and 1.68× (FLR) MEGA's. FLR raises
$\gamma$ in HYMAGYC $(s,\theta)$ and lowers it in the other three rows. FLR
lowers the frequency in MEGA, leaves it unchanged in HYMAGYC $(R,Z)$ and
raises it in ORB5 ([Vlad et al. (2025)](/sources/vlad-2025.md), §§4–5). The
mode in all codes is $m=2$-dominated and peaks at $s\approx0.2$, where
$\partial n_h/\partial s>0$.

**JOREK against the 2021 linear data**
([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §IV.B, Figs. 8–10,
values read off the figures):

- *Mode.* JOREK finds an $n=1$, $m=2$ EPM near $\sqrt{\psi_N}\approx0.2$ at
  about 150 kHz, in the continuum below the TAE gap.
- *Growth rate.* $\gamma$ grows linearly with the normalized gradient. At
  the nominal gradient JOREK is close to HYMAGYC and MEGA (about
  1.7–2.1 $\times10^5$ s$^{-1}$), and ORB5 is higher (about 3.5).
- *Frequency.* HYMAGYC about 179, MEGA about 165, JOREK about 143–150, ORB5
  about 127 kHz.
- *Resonance.* The dominant resonance is at $v_{\parallel p}\approx-2\sqrt{T_h/m_h}$
  in both JOREK and MEGA.

## Nonlinear results (Vlad et al. 2025)

All four codes agree qualitatively ([Vlad et al. (2025)](/sources/vlad-2025.md),
§7):

- the EPM saturates;
- saturation fills the hollow EP core and lowers the mid-radius peak;
- later, a subdominant counter-rotating external
  [TAE](/definitions/toroidal-alfven-eigenmode.md) ($m=2,3$, $s\approx0.4$)
  is driven where $\partial n_h/\partial s<0$.

HYMAGYC saturates at $t\approx0.14$ ms and loses about 15% of the EPs as
first-orbit losses, then about 20% more by the end of the run. XTOR-K
reports frequencies of 166 kHz (EPM, early saturation) and −196 kHz (TAE).
Its growth rates are buried in full-$f$ noise (§§3, 6).

## Code-to-code spread

The disagreements recorded by [Vlad et al. (2025)](/sources/vlad-2025.md)
are listed below. None of them is quantified as to cause.

1. **Chirping direction.** Down in HYMAGYC and MEGA, following the lower
   continuum. Up into the TAE gap in ORB5 (§§3–5).
2. **Saturation level.** MEGA's volume-integrated energy is about 15× lower
   than HYMAGYC's at the first overshoot. A HYMAGYC run with reduced EP
   density still redistributes much more than MEGA, so amplitude alone does
   not explain the gap (§4).
3. **EP redistribution.** MEGA "looks to have much lower transport than the
   other three codes" (§7). The Fig. 13 profiles end at different times:
   0.36 ms (HYMAGYC), 0.202 ms (MEGA), 0.237 ms (ORB5) and 0.605 ms
   (XTOR-K). The transport comparison therefore mixes stages of the
   evolution (reader's caveat).
4. **TAE onset delay.** About 0.1 ms after first saturation in MEGA and more
   than 0.2 ms in HYMAGYC. The authors attribute the difference to the
   steeper outer gradient that persists in MEGA (§4).
5. **Edge transport.** Strong in ORB5 and XTOR-K, "only barely observable"
   in HYMAGYC and MEGA (§7).
6. **FOW against FLR transport.** FOW-only runs transport more. The effect
   is clear in HYMAGYC, barely visible in MEGA and pronounced in ORB5 (§7,
   Fig. 14).

Vlad et al. list three candidate causes (§§5, 7):

- current coupling (MEGA) against pressure coupling (HYMAGYC, XTOR-K) — see
  [pressure and current coupling](/methods/pressure-and-current-coupling.md);
- fast-ion inertia, which ORB5 has and the hybrids lack, at this high EP
  fraction;
- the particle boundary conditions at the edge.

The authors stress that inward EP transport has been observed in AUG
off-axis-NBI discharges. They also state that this is *not* a validation,
because the experiment has an anisotropic slowing-down distribution and the
benchmark an isotropic Maxwellian (§§3, 7).

Bogaarts et al. (2022, §IV.B, Fig. 9) add a linear spread. JOREK's frequency
*decreases* with the EP gradient, from about 148 to 136 kHz. HYMAGYC's
frequency *increases* (about 150 to 179 kHz) and MEGA's too (about 157 to
165 kHz). The authors explain JOREK's lower frequency by its constant bulk
ion density, which varies in the original benchmark. They do not address the
opposite trend. Their nominal MEGA frequency, about 165 kHz read off Fig. 9,
is also below the 171.43 kHz that Vlad et al. tabulate for MEGA FOW. The
figure reading and the 2021-versus-2025 data provenance may account for
this (compiler's comparison).

## Contradictions

**Chirping direction of the NLED-AUG EPM.** Open. Down in HYMAGYC and MEGA,
up in ORB5 ([Vlad et al. (2025)](/sources/vlad-2025.md), §§3–5). The two
sides are different codes inside one source. A same-code test of the
candidate causes listed above would settle it: coupling scheme, fast-ion
inertia, and edge boundary conditions.

**Frequency trend with EP gradient.** Open.
[Bogaarts et al. (2022)](/sources/bogaarts-2022.md) (§IV.B, Fig. 9) show
JOREK's frequency falling with the EP density gradient, while the HYMAGYC
and MEGA data in the same figure rise. The constant-bulk-density
explanation covers the offset, not the sign of the trend. A JOREK scan with
the benchmark's varying bulk density would settle it.

**Labelling of the $n=1$ mode (EPM or TAE).** Open, recorded on
[energetic particle mode](/definitions/energetic-particle-mode.md).

# Citations

- [Vlad et al. (2025)](/sources/vlad-2025.md): Table 1 setup, Table 2 linear results, the nonlinear four-code comparison.
- [Bogaarts et al. (2022)](/sources/bogaarts-2022.md): JOREK linear runs against HYMAGYC, MEGA and ORB5; gradient scans; resonances.

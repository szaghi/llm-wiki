---
type: Definition
title: "Toroidal Alfvén eigenmode (TAE)"
description: "Discrete shear-Alfvén eigenmode in the toroidicity-induced gap between the continua of two neighbouring poloidal harmonics m and m+1, located near q = (m+1/2)/n and destabilized by resonant energetic particles; the standard verification target of hybrid kinetic-MHD codes."
status: established
aliases: [TAE, toroidicity-induced Alfvén eigenmode, gap mode]
tags: [alfven-eigenmode, energetic-particles, hybrid-kinetic, tokamak]
timestamp: 2026-10-16T20:00:00Z
---

# Toroidal Alfvén eigenmode (TAE)

A toroidal Alfvén eigenmode is a discrete shear-Alfvén mode with toroidal
mode number $n$. Toroidicity couples two neighbouring poloidal harmonics $m$
and $m+1$, and this coupling opens a gap in the shear-Alfvén continuum. The
TAE sits in that gap, so its structure is dominated by the coupled pair
$m,m+1$. It is located radially near the surface where

$$q=\frac{m+1/2}{n}.$$

A mode in the gap avoids continuum damping. It can be destabilized by
energetic particles (EPs) through their density or pressure gradient
([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §IV.A, citing Cheng
1985; [Liu et al. (2022)](/sources/liu-2022.md), §6.2;
[Liu et al. (2024)](/sources/liu-2024.md), §III B–C). The two-harmonic
signature is the property Vlad et al. use to tell a TAE from an
[energetic particle mode](/definitions/energetic-particle-mode.md). A mode
dominated by a single $m$ is classed as an EPM even when its frequency lies
almost within the gap ([Vlad et al. (2025)](/sources/vlad-2025.md),
footnote 1).

## Examples in the sources

- **$n=6$, ITPA case.** In the [ITPA benchmark](/benchmarks/itpa-tae-benchmark.md)
  the mode is dominated by $m=10,11$ at $r\approx0.5a$, where
  $q=1.75=\tfrac12(10+11)/6$
  ([Liu et al. (2022)](/sources/liu-2022.md), §6.2, Fig. 6;
  [Bogaarts et al. (2022)](/sources/bogaarts-2022.md), Fig. 1). Bogaarts
  et al. find its frequency, about $4\times10^5$ rad/s, inside the gap of the
  HELENA/CASTOR continuum.
- **$n=3$, GMEC test.** The mode is dominated by $m=5,6$ at $r/a\approx0.45$,
  just above the tip of the gap. At $\beta_h=0.02$ it has
  $\omega\tau_A=0.261108$ and $\gamma\tau_A=0.039025$ with
  $\tau_A=R_0/v_A$ on axis. $\gamma$ is linear in $\beta_h$, with threshold
  $\beta_{h}\approx0.0019$, in agreement with M3D-K
  ([Liu et al. (2024)](/sources/liu-2024.md), §III B, Figs. 8–11).
- **$n=6$, MEGA chirping case.** A circular, uniform-density plasma with
  linear $q$ from 1.0 to 1.3 and aspect ratio 3.2: the TAE is dominated by
  $m=6,7$ near the first gap at $r/a\approx0.26$, where $q=(2m+1)/2n$, the
  same condition as above. It sits above the lower tip of the gap with
  $\omega/\omega_A=0.4553$ ($\omega_A=v_A/R_0$ on axis). The net growth rate
  is linear in $\beta_h$; its extrapolation to $\beta_h=0$ gives the
  background damping $\gamma_d/\omega_A=0.0053$, hence the drive
  $\gamma_l/\omega_A=0.012$ and $\gamma_l/\omega=2.64\%$
  ([Hezaveh et al. (2022)](/sources/hezaveh-2022.md), §4.1, Figs. 1, 3).
  Nonlinearly it chirps both up and down, and the chirping frequencies
  leave the gap into the shear-Alfvén continuum (see
  [frequency chirping](/definitions/energetic-particle-mode.md)).
- **Late $m=2,3$ mode in the NLED-AUG case.** In the
  [NLED-AUG benchmark](/benchmarks/nled-aug-benchmark.md) a subdominant
  external TAE appears late, at $s\approx0.4$, dominated by $m=2,3$. It is
  driven where $\partial n_h/\partial s<0$ and rotates opposite to the linear
  EPM. It does not chirp in HYMAGYC, and it shows up as a second growth
  stage of the mode energy in all four codes
  ([Vlad et al. (2025)](/sources/vlad-2025.md), §§3–7).
- **$m=2,3$ mode in AUG #31213.** In the JOREK study of the AUG discharge,
  a core $m=2,3$ TAE is found at $t=0.7$ s, when $q$ crosses 2.5.
  Its labelling is disputed (see the EPM page)
  ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §V, Table I).

## Drive and resonance

EPs exchange energy with the mode through wave–particle resonances,
$\omega=k_\parallel v_{\parallel p}$, with the sideband form
$\omega\approx(v_{\parallel p}/R)\,[n-(m+\ell)/q]$ for integer $\ell$
([Liu et al. (2024)](/sources/liu-2024.md), Eq. 35; $\ell$ is written $p$
there). GMEC verifies the scaling of the resonant-island width with the
square root of the wave amplitude: the analytic slope is
$1.2558\times10^{-3}$ and the fitted slope $1.1409\times10^{-3}$, a 9% gap
the paper calls "consistent" (Liu et al. 2024, §III A, Fig. 7). In action-angle form, the resonance is
$\omega=n\omega_{\tilde\zeta}+\ell_{\mathrm r}\omega_{\tilde\theta}$ with
toroidal and poloidal transit frequencies and integer $\ell_{\mathrm r}$;
for the $n=6$ MEGA case co-passing EPs resonate at $\ell_{\mathrm r}=-m$ and
counter-passing ones at $\ell_{\mathrm r}=-(m+1)$
([Hezaveh et al. (2022)](/sources/hezaveh-2022.md), §4.2, Eq. 25, citing
Todo & Sato 1998). For passing particles, with
$\omega_{\tilde\theta}\approx v_{\parallel p}/(qR)$ and
$\omega_{\tilde\zeta}\approx v_{\parallel p}/R$, this is the sideband form
above with $\ell_{\mathrm r}=-(m+\ell)$ (compiler's reading). On the ITPA case JOREK
finds the dominant resonance at $v_{\parallel p}=v_A/3$, in agreement with
Könies et al. (2018). At saturation the resonant-particle density flattens
around the gap at $r=0.5a$
([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §IV.A, Figs. 5–6).

FLR effects reduce the drive at high EP temperature. In M3D-C1-K and GMEC
the FLR growth rate of the $n=6$ TAE is about half the zero-Larmor-radius
value ([Liu et al. (2022)](/sources/liu-2022.md), §6.2, Fig. 5;
[Liu et al. (2024)](/sources/liu-2024.md), §III C, Fig. 14).

## Other excitation

JOREK has also excited TAEs with an external antenna in JET X-point
plasmas. A wider scrape-off layer with open field lines makes the excitation
less efficient, as observed experimentally
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §7.2).

## Contradictions

**EPM vs TAE labelling.** Open, recorded on
[energetic particle mode](/definitions/energetic-particle-mode.md). It
concerns whether the AUG-NLED $n=1$ mode and the AUG #31213 mode at
$t=0.7$ s are TAEs.

# Citations

- [Bogaarts et al. (2022)](/sources/bogaarts-2022.md): the ITPA TAE in JOREK, the $v_A/3$ resonance, the AUG #31213 TAE.
- [Liu et al. (2022)](/sources/liu-2022.md): the ITPA TAE in M3D-C1-K and its gap location.
- [Liu et al. (2024)](/sources/liu-2024.md): the $n=3$ and $n=6$ TAEs in GMEC, the resonance condition and island width.
- [Vlad et al. (2025)](/sources/vlad-2025.md): the late external TAE in NLED-AUG and the two-harmonic criterion.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md): antenna-excited TAEs in JET X-point geometry.
- [Hezaveh et al. (2022)](/sources/hezaveh-2022.md): the chirping $n=6$ TAE in MEGA, damping by extrapolation to $\beta_h=0$, the action-angle resonance.

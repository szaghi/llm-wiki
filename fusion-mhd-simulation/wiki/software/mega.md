---
type: Software
title: "MEGA"
description: "Hybrid code coupling nonlinear full MHD to drift-kinetic δf energetic particles (with an ad-hoc gyro-average for FLR) through the energetic-particle current on a cylindrical grid; a reference code of the ITPA TAE, AUG-NLED and DIII-D RSAE benchmarks, it saturates about 15× lower and redistributes energetic particles much less than HYMAGYC in the nonlinear NLED-AUG benchmark."
status: established
aliases: [MEGA code]
tags: [code, hybrid-kinetic, energetic-particles, alfven-eigenmode, particles, benchmark]
timestamp: 2026-10-16T00:00:00Z
---

# MEGA

MEGA is a [hybrid kinetic-MHD](/methods/hybrid-kinetic-mhd.md) code (Todo
2006): the bulk plasma follows nonlinear full MHD and the energetic particles
(EPs) are drift-kinetic, with finite-Larmor-radius effects added by an ad-hoc
$N$-point gyro-average ([Vlad et al. (2025)](/sources/vlad-2025.md), §4).

## Model and numerics

* **Coupling.** The EP current density enters the MHD momentum equation
  (current coupling) (Vlad et al. 2025, §4). In the simplified form identified
  by [Liu et al. (2022)](/sources/liu-2022.md) (§4, Eq. 27), the equilibrium
  EP current term reduces to the equilibrium EP pressure gradient projected
  along the perturbed field, and the whole scheme is equivalent to the Park et
  al. (1999) pressure coupling that keeps only the perpendicular divergence of
  the EP pressure tensor. See
  [pressure and current coupling](/methods/pressure-and-current-coupling.md).
* **Particles.** Standard [δf](/methods/delta-f-method.md) markers (Vlad et
  al. 2025, §4; [Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §IV B);
  see [particle pushers](/methods/particle-pushers.md).
* **Dissipation.** Resistivity, viscosity and diffusion, with inverse
  Lundquist number $S^{-1}=5\times10^{-7}$ and normalized viscosity
  $5\times10^{-7}$ in the NLED-AUG benchmark, $\Gamma=5/3$ (Vlad et al. 2025,
  §4).
* **Grid.** Cylindrical $(R,\phi,Z)$, $128\times16\times256$ points with
  8 388 608 markers (16 per cell); output is analysed in flux coordinates with
  $n\in\{-1,0,1\}$ and $m=0\ldots64$. The time-stepping scheme is not stated
  (Vlad et al. 2025, §4). No GPU use is reported.

## Benchmarks

* **[NLED-AUG](/benchmarks/nled-aug-benchmark.md), linear** (off-axis EP
  profile, $|n|=1$, isotropic Maxwellian deuterium at 93 keV): the most unstable
  mode is the near-axis $m=2$ [energetic particle mode](/definitions/energetic-particle-mode.md)
  found by all codes. MEGA gives $\gamma=218\,616$ s$^{-1}$ and
  $\omega/2\pi=171.43$ kHz with finite orbit width only, and $170\,247$
  s$^{-1}$ and $157.00$ kHz with FLR; ORB5's growth rate is 1.59× (FOW) and
  1.68× (FLR) MEGA's (Vlad et al. 2025, §4–5, Table 2).
* **NLED-AUG, nonlinear** (Vlad et al. 2025, §4, §7, Figs. 8–9, 13):
  qualitative agreement with HYMAGYC (downward chirping, a slight outward
  shift, a later counter-rotating external TAE), but the saturated energy is
  "considerably lower", a factor of about 15 at the first overshoot; EP
  redistribution is much weaker; the second growth stage starts about 0.1 ms
  after the first saturation against more than 0.2 ms in HYMAGYC, which the
  authors attribute to the steeper outer EP gradient that survives in MEGA;
  there is no initial relaxation of the distribution; FOW-only and FLR
  transport differ barely.
* **NLED-AUG, JOREK comparison** (Bogaarts et al. 2022, §IV B, Figs. 9–10):
  JOREK's growth rate is close to HYMAGYC and MEGA (about
  $1.7$–$2.1\times10^5$ s$^{-1}$ at the nominal gradient); MEGA's frequency
  rises with the EP gradient (about 157 to 165 kHz) while JOREK's falls; both
  codes show the dominant resonance at a parallel velocity of about −2 thermal
  EP velocities.
* **[ITPA $n=6$ TAE](/benchmarks/itpa-tae-benchmark.md)**: MEGA is one of the
  FLR-including reference codes (Bogaarts et al. 2022, §IV A, Fig. 3); GMEC's
  frequencies without FLR are close to MEGA's, and with FLR "reasonably close"
  ([Liu et al. (2024)](/sources/liu-2024.md), §III C, Fig. 14); M3D-C1-K's
  FLR frequency sits on the lower branch with MEGA (Liu et al. 2022, §6.2).
* **[DIII-D RSAE](/benchmarks/diii-d-rsae-benchmark.md)**: MEGA peaks at $n=5$,
  as GMEC does, with a higher growth rate (Liu et al. 2024, §III D, Fig. 17).

## Limitations and benchmark spread

* The cause of MEGA's low saturation level and weak transport is not
  identified. Vlad et al. (2025) (§5, §7) list current versus pressure coupling
  (MEGA versus HYMAGYC and XTOR-K), the fast-ion inertia that hybrid models
  omit and gyrokinetic ones keep, and particle boundary conditions as
  candidates, without testing them. A HYMAGYC run with a reduced EP density
  still redistributes much more, so amplitude alone does not explain the gap
  (§4).
* The analytic equivalence of the two coupling schemes (Liu et al. 2022) and
  the observed differences are not logically incompatible (compiler's
  reading): the equivalence
  holds in the drift-kinetic limit with $n_h\ll n_i$, and the NLED-AUG case
  has an EP-to-ion density ratio of 0.027 on axis (Vlad et al. 2025, Table 1).
  The open question is recorded on
  [pressure and current coupling](/methods/pressure-and-current-coupling.md).
* The EP profiles of the nonlinear comparison end at different times (MEGA
  0.202 ms, HYMAGYC 0.36 ms, ORB5 0.237 ms, XTOR-K 0.605 ms), which weakens
  the transport comparison (Vlad et al. 2025, Fig. 13; recorded on the Source
  page).

# Citations

1. [Vlad et al. (2025)](/sources/vlad-2025.md) — §§4–5, §7, Tables 1–2, Figs. 8–9, 13–14.
2. [Bogaarts et al. (2022)](/sources/bogaarts-2022.md) — §IV, Figs. 3, 9–10.
3. [Liu et al. (2022)](/sources/liu-2022.md) — §4, §6.2.
4. [Liu et al. (2024)](/sources/liu-2024.md) — §III C–D, Figs. 14, 17.

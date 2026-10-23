---
type: Software
title: "MEGA"
description: "Hybrid code coupling nonlinear visco-resistive full MHD to drift-kinetic δf energetic particles or kinetic thermal ions through the kinetic current, on a cylindrical finite-difference grid with explicit RK4; a reference code of the ITPA TAE, AUG-NLED and DIII-D RSAE benchmarks, used for chirping-TAE, infernal-mode and high-beta LHD studies, it saturates about 15× lower and redistributes energetic particles much less than HYMAGYC in the nonlinear NLED-AUG benchmark."
status: established
aliases: [MEGA code]
tags: [hybrid-kinetic, energetic-particles, alfven-eigenmode, particles, verification, stellarator]
timestamp: 2026-10-16T18:35:00Z
---

# MEGA

MEGA is a [hybrid kinetic-MHD](/methods/hybrid-kinetic-mhd.md) code (Todo
2006): the bulk plasma follows nonlinear full MHD and the energetic particles
(EPs) are drift-kinetic, with finite-Larmor-radius effects added by an ad-hoc
$N$-point gyro-average ([Vlad et al. (2025)](/sources/vlad-2025.md), §4).
It can also treat the bulk thermal ions as drift-kinetic markers
([kinetic thermal ions](/methods/kinetic-thermal-ions.md);
[Sato et al. (2024)](/sources/sato-2024.md), §2, citing Todo et al. 2005,
2021 as the model references). Its fluid part shares the numerics of the
MHD code [MIPS](/software/mips.md) (ibid.); MIPS was "developed by
extracting this pure MHD part of the original MEGA framework"
([Sato & Todo (2026)](/sources/sato-2026.md), p. 2). In the
kinetic-thermal-ion version, switching the kinetic ions off does not
recover single-fluid MHD, because density and parallel velocity are ion
moments, so MIPS serves as the MHD reference (ibid.). Kinetic thermal ions
and kinetic energetic ions can be combined (ibid., p. 8).

## Model and numerics

* **MHD equations.** Visco-resistive full MHD with continuity, pressure and
  momentum equations, Ohm's law $\mathbf E=-\mathbf v\times\mathbf B+\eta(\mathbf J-\mathbf J_0)$,
  and source terms that hold the equilibrium against dissipation: mass and
  pressure diffusion act on $\rho-\rho_0$, $p-p_0$, and Ohmic and viscous
  heating enter the pressure equation as $\eta\mathbf J\cdot(\mathbf J-\mathbf J_0)$
  plus viscous terms ([Hezaveh et al. (2022)](/sources/hezaveh-2022.md),
  Eqs. 1–4). The viscosity enters as $\nu\rho$, a kinematic viscosity.

* **Coupling.** The EP current density enters the MHD momentum equation
  (current coupling) (Vlad et al. 2025, §4) as $(\mathbf J-\mathbf J_h)\times\mathbf B$;
  $\mathbf J_h$ is deposited from the parallel, curvature and $\nabla B$
  drift currents of the markers plus a magnetization current, with no
  $E\times B$ part "due to quasi-neutrality" (Hezaveh et al. 2022, Eqs. 1,
  5–6). With kinetic thermal ions the ion current is written through the
  marker pressures (Sato et al. 2024, Eq. 25). In the simplified form identified
  by [Liu et al. (2022)](/sources/liu-2022.md) (§4, Eq. 27), the equilibrium
  EP current term reduces to the equilibrium EP pressure gradient projected
  along the perturbed field, and the whole scheme is equivalent to the Park et
  al. (1999) pressure coupling that keeps only the perpendicular divergence of
  the EP pressure tensor. See
  [pressure and current coupling](/methods/pressure-and-current-coupling.md).
* **Particles.** Standard [δf](/methods/delta-f-method.md) markers (Vlad et
  al. 2025, §4; [Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §IV B);
  see [particle pushers](/methods/particle-pushers.md). Passive test
  particles, which respond to the fields without contributing to
  $\mathbf J_h$, can be added to raise phase-space resolution (Hezaveh et
  al. 2022, §1). Kinetic thermal ions use particle-number weights
  $\Delta V_p\,\delta f$ with a Maxwellian $f_0(\psi,\mathcal E)$ (Sato et
  al. 2024, Eq. 15).
* **Dissipation.** Resistivity, viscosity and diffusion, with inverse
  Lundquist number $S^{-1}=5\times10^{-7}$ and normalized viscosity
  $5\times10^{-7}$ in the NLED-AUG benchmark, $\Gamma=5/3$ (Vlad et al. 2025,
  §4).
* **Grid.** Cylindrical $(R,\phi,Z)$, $128\times16\times256$ points with
  8 388 608 markers (16 per cell); output is analysed in flux coordinates with
  $n\in\{-1,0,1\}$ and $m=0\ldots64$. The time-stepping scheme is not stated
  (Vlad et al. 2025, §4). No GPU use is reported.
* **Spatial and time discretization.** Finite differences on the
  cylindrical grid ([Hezaveh et al. (2022)](/sources/hezaveh-2022.md), §2):
  the Kawamura–Kuwahara third-order upwind scheme for convection terms and
  fourth-order central differences otherwise, with explicit fourth-order
  Runge–Kutta for both particles and fluid
  ([Sato et al. (2024)](/sources/sato-2024.md), §2). This fills the gap left
  by Vlad et al. (2025).
* **Kinetic-thermal-ion runs.** $256\times48\times256$ grid on a $2\pi/3$
  toroidal wedge with about $10^8$ markers (32 per cell), on NEC SX-Aurora
  TSUBASA and Fugaku; again no GPU (Sato et al. 2024, §2).
* **LHD runs** ([Sato & Todo (2026)](/sources/sato-2026.md), pp. 2–3):
  $128\times640\times128$ points in $(R,\phi,Z)$ with about
  $6.7\times10^8$ thermal-ion markers; the nonlinear run at $S=10^7$ took
  2048 SX-Aurora vector engines for about 164.4 h wall clock; no GPU.
  Dissipation $\nu=\kappa=10^{-7}v_AR_0$ (isotropic) in the earlier studies
  and $\nu=\kappa_\perp=10^{-7}v_AR_0$, $\kappa_\parallel=10^{-3}v_AR_0$ in
  the 2021 kinetic-thermal-ion study (normalized diffusivities); a realistic $\kappa_\parallel$ would impose
  a severe CFL limit on the explicit scheme. FLR is available but switched
  off, and there is no explicit ion diamagnetic term.
* **Boundary conditions** (same source, pp. 2–3). The domain contains the
  plasma and a surrounding vacuum region in which the velocity, pressure
  and density perturbations vanish; the perturbed field is zero at the
  domain edge. Thermal-ion markers are loaded in $R\in[2.55,4.75]$ m,
  $Z\in[-1.1,1.1]$ m and removed when they leave into the vacuum region.

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

## Physics applications

* **Chirping $n=6$ TAE** ([Hezaveh et al. (2022)](/sources/hezaveh-2022.md)):
  a circular linear-$q$ case followed for about 3700 Alfvén times through
  up- and down-chirping, analysed with the
  [wave-frame action-angle diagnostic](/methods/chirping-phase-space-diagnostic.md).
  Raising $\nu=\eta$ by 20× and 40× mid-run speeds up the chirp, which the
  authors read as Berk–Breizman dissipation control and propose as a
  probing tool (§4.1; see
  [frequency chirping](/definitions/energetic-particle-mode.md)).
* **Infernal modes with kinetic thermal ions**
  ([Sato et al. (2024)](/sources/sato-2024.md)): $n=3$ ideal and resistive
  [infernal modes](/definitions/infernal-mode.md), compared with MIPS; the
  kinetic ions reduce slow growth rates and suppress the resistive beta
  collapse (§3).
* **High-beta LHD** ([Sato & Todo (2026)](/sources/sato-2026.md)): with
  kinetic thermal ions MEGA lowers the growth rates of resistive ballooning
  and resonant $(3,2)$ interchange modes relative to MIPS and keeps the
  nonlinear activity peripheral at $S=10^7$, where MIPS collapses the core;
  adding 100 keV energetic ions up to $\beta_h=0.8\,\%$ lowers the linear
  growth rate without changing saturation (pp. 6–9; see
  [kinetic thermal ions confine LHD pressure-driven activity to the periphery](/results/kinetic-ions-prevent-core-collapse-lhd.md)).

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
5. [Hezaveh et al. (2022)](/sources/hezaveh-2022.md) — §§1–2, 4, Eqs. 1–6: equations, test particles, chirping TAE.
6. [Sato et al. (2024)](/sources/sato-2024.md) — §§2–3, Eqs. 6–25: kinetic thermal ions, numerics, hardware, infernal modes.
7. [Sato & Todo (2026)](/sources/sato-2026.md) — pp. 2–9: MIPS as extracted MHD part, no MHD limit with kinetic ions, LHD resolution, cost, boundary conditions, kinetic thermal and energetic ions.

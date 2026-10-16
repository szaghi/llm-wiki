---
type: Method
title: "Kinetic thermal ions in hybrid kinetic-MHD"
description: "Extension of hybrid kinetic-MHD in which the bulk thermal ions, not only an energetic minority, are δf drift-kinetic markers while the electrons stay a fluid; the ion density and parallel flow are taken from the markers instead of the fluid equations, and the ion response adds Landau damping and a phase shift of the pressure perturbation that lower slow MHD growth rates."
status: established
aliases: [KTI, kinetic thermal ions, thermal-ion kinetic-MHD, kinetic bulk ions, density and parallel-velocity synchronization]
tags: [hybrid-kinetic, particles, mhd, energetic-particles, numerics, kink, tokamak]
timestamp: 2026-10-16T12:00:00Z
---

# Kinetic thermal ions in hybrid kinetic-MHD

The classical [hybrid kinetic-MHD model](/methods/hybrid-kinetic-mhd.md)
treats a minority of energetic particles (EPs) kinetically and the whole
bulk plasma as a fluid. The kinetic-thermal-ion (KTI) variant moves the
**bulk ions** into the kinetic part as well. Thermal ions are advanced as
$\delta f$ drift-kinetic guiding-centre markers, the electrons remain a
fluid, and the fluid keeps only the equations the markers do not already
supply. Two codes of this bundle do this:
[M3D-C1-K](/software/m3d-c1-k.md), with thermal and fast deuterium both
kinetic ([Liu et al. (2022b)](/sources/liu-2022-b.md), §2), and
[MEGA](/software/mega.md), with only thermal ions and no EPs
([Sato et al. (2024)](/sources/sato-2024.md), §2). Liu et al. state that
their model "is similar to" MEGA's earlier KTI model (Sato & Todo 2019,
2020, as cited, §1). JOREK lists kinetic thermal ions as work in progress
([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §4.2).

The motivation is physics the fluid closure misses: Landau damping of
modes with $\omega/k_\parallel$ near the ion thermal speed, and the
precession and diamagnetic response of trapped thermal ions. Both papers
conclude that MHD without kinetic ions gives wrong stability answers in
the cases they study: "false positive results" for non-resonant
[fishbones](/definitions/fishbone.md)
([Liu et al. (2022b)](/sources/liu-2022-b.md), §4) and an underestimated
beta limit for [infernal modes](/definitions/infernal-mode.md)
([Sato et al. (2024)](/sources/sato-2024.md), §4).

## Why the fluid ion equations must go

If thermal ions are kinetic and the fluid still evolves the ion density
and parallel momentum, both are computed twice: once by the fluid
equations and once as marker moments. Liu et al. (2022b, §1) state that
"the error between the two approaches can lead to numerical issues or even
parasitic modes". In M3D-C1 the fluid and kinetic equations are solved one
after the other within a step. With the Park et al. (1999) scheme, as
cited, where thermal-ion pressure enters the fluid but $n$ and
$v_\parallel$ come from the fluid equations, "the difference between
$\delta n$ and $\delta v_\parallel$ from the fluid and kinetic equations
can increase with time". This violates quasineutrality and produces
parasitic modes that overwhelm the result (§2, after Eq. 2.23; no figure of
the failure is shown). Liu et al. hold that the Park scheme is "in
principle" equivalent to theirs: the fluid parallel-momentum equation
follows from moments of the kinetic equation for small ion energy without
gradient and curvature drifts (§2; derivation not shown). The failure is
therefore one of implementation under sequential splitting, not of the
model.

## The M3D-C1-K scheme: pressure coupling and synchronization

Liu et al. (2022b, §2, Eqs. 2.1–2.22) keep from MHD:

- the **perpendicular** momentum equation, with the divergence of both ion
  pressure tensors,
  $$\rho\left[\frac{\partial\mathbf v_\perp}{\partial t}+(\mathbf v_\perp+v_\parallel\mathbf b)\cdot\nabla\mathbf v_\perp\right]=\mathbf J\times\mathbf B-\nabla_\perp p_e-\nabla_\perp\cdot\mathsf P_i-\nabla_\perp\cdot\mathsf P_h+\nu\nabla^2\mathbf v_\perp,$$
  where $\mathsf P_i=p_{\parallel i}\mathbf b\mathbf b+p_{\perp i}(\mathsf I-\mathbf b\mathbf b)$
  is the thermal-ion analogue of the EP tensor $\mathsf P_h$ (Eq. 2.1). The
  authors read it as a decomposition of the perpendicular current:
  $\rho\,\partial_t\mathbf v_\perp$ is the polarization current, the
  pressure terms the drift and magnetization currents (§7);
- Faraday's law and Ohm's law $\mathbf E=-\mathbf v_\perp\times\mathbf B+\eta\mathbf J$,
  with no Hall or $\nabla_\parallel p_e$ term (Eq. 2.4);
- the electron pressure (or temperature) equation with anisotropic
  conduction, advected by $\mathbf v_\perp+v_\parallel\mathbf b$, with the
  ion $v_\parallel$ used because "electrons and ions are moving together"
  (Eqs. 2.5–2.6).

The fluid continuity and parallel-momentum equations are **replaced by
synchronization**: $\delta n_i$, $\delta n_h$ and $\delta v_\parallel$ are
deposited from the markers (Eqs. 2.17–2.20), and
$\delta\rho=m_i\delta n_i+m_h\delta n_h$,
$\delta n_e=Z_i\delta n_i+Z_h\delta n_h$ (Eqs. 2.18–2.19), which enforces
quasineutrality by construction. The parallel flow is the charge-weighted
marker flux divided by $n_{e0}+\delta n_e$ (Eq. 2.20). Each marker's
deposition weight carries the compression correction
$w_p+\delta B_\parallel/B^*_\parallel$ (see the
[δf method](/methods/delta-f-method.md)).

The kinetic ions feel the effective field

$$\mathbf E^*=\mathbf E-\frac{1}{n_ee}\nabla_\parallel p_e,$$

obtained by dropping electron parallel inertia (massless electrons). It
supplies the parallel electric force between kinetic ions and fluid
electrons, and it is "essential for the IAW simulation" (Eq. 2.11, §2).
$\mathbf E^*$ enters the weight equations (Eqs. 2.14, 2.16). The printed
guiding-centre equations (2.7–2.8) contain $\mathbf E$, not $\mathbf E^*$,
so whether the push itself includes the $\nabla_\parallel p_e$ term is not
stated; in linear runs the push uses equilibrium fields only and the
question affects the weights alone (recorded on the Source page). The
$d_i/L$ two-fluid corrections to the electron equations are dropped, which
Liu et al. justify for long-wavelength modes (§7). The semi-implicit MHD
step of M3D-C1 "is helpful for stabilizing numerical instabilities after
including ion kinetic terms" (§1, §7; no evidence shown).

## The MEGA scheme: current coupling with a fluid perpendicular flow

In MEGA the thermal ions are drift-kinetic $\delta f$ markers with
Maxwellian $f_0(\psi,\mathcal E)$ and the guiding-centre velocity
$\mathbf v_\parallel^*+\mathbf v_E+\mathbf v_B$, where
$\mathbf v_E=\mathbf E^*\times\mathbf B/B^*_\parallel$
([Sato et al. (2024)](/sources/sato-2024.md), Eqs. 6–14). The markers give
$\rho$, $v_\parallel$, $p_{\parallel i}$ and $p_{\perp i}$ (Eqs. 16–19).
The fluid evolves only $\mathbf v_\perp$, $\mathbf B$ and the electron
pressure (Eqs. 20–24):

$$\rho\frac{\partial\mathbf v_\perp}{\partial t}=-\rho[(\mathbf v_\perp+v_\parallel\mathbf b)\cdot\nabla]\mathbf v_\perp-\nabla_\perp p_e+(\mathbf J-\mathbf J_i)\times\mathbf B+\text{viscous terms},$$

with the kinetic-ion perpendicular current built from the marker pressures,

$$\mathbf J_i=\frac1B\left(p_{\parallel i}\nabla\times\mathbf b-p_{\perp i}\nabla\ln B\times\mathbf b\right)-\nabla\times\left(\frac{p_{\perp i}}{B}\mathbf b\right)$$

(Eq. 25): curvature, $\nabla B$ and magnetization currents. This is the
current-coupling form of
[pressure and current coupling](/methods/pressure-and-current-coupling.md)
applied to the bulk ions. Ohm's law and $\mathbf E^*$ contain
$-(m_i/q_i\rho)\nabla_\parallel p_e$ (Eqs. 13, 23), but that term is
**neglected in all results**, so the model has no electron diamagnetic
effect (§2). Liu et al. (2022b, §2) state that their pressure coupling and
MEGA's current coupling "are equivalent for calculating $v_\perp$", citing
[Liu et al. (2022)](/sources/liu-2022.md).

## The two implementations compared

| | M3D-C1-K | MEGA |
|---|---|---|
| kinetic ions | thermal and fast D, $\delta f$, guiding centre | thermal H only, $\delta f$, drift-kinetic |
| fluid equations kept | $\mathbf v_\perp$, $\mathbf B$, $p_e$ or $T_e$ | $\mathbf v_\perp$, $\mathbf B$, $p_e$ |
| from markers | $\delta n$, $\delta v_\parallel$, $\mathsf P_i$, $\mathsf P_h$ | $\rho$, $v_\parallel$, $p_{\parallel i}$, $p_{\perp i}$ |
| coupling | pressure, $-\nabla_\perp\cdot\mathsf P_i$ | current, $-\mathbf J_i\times\mathbf B$ |
| $\nabla_\parallel p_e$ in ion field | kept | neglected |
| MHD discretization | finite elements, semi-implicit | finite differences, explicit RK4 |
| source | [Liu et al. (2022b)](/sources/liu-2022-b.md), §2 | [Sato et al. (2024)](/sources/sato-2024.md), §2 |

## Verification: Landau damping of the ion acoustic wave

Liu et al. (2022b, §3) verify the KTI model on a 1D ion acoustic wave (IAW)
with isothermal fluid electrons ($\Gamma_e=1$), kinetic ions and a
sinusoidal initial $v_\parallel$. In MHD alone the IAW oscillates "with
little damping". With kinetic ions the frequency and Landau damping rate
follow the empirical fits of Chen (2013), as cited,

$$\omega=\omega_0\sqrt{1+3T_i/T_e},\qquad\frac{\gamma_{\mathrm{LD}}}{\omega}=1.1\left(\frac{T_i}{T_e}\right)^{7/4}\exp\!\left[-\left(\frac{T_i}{T_e}\right)^2\right],$$

with $\omega_0=k\sqrt{T_e/m_i}$ and $k$ the wavenumber, for
$T_i/T_e=0.1$–0.3 (Eqs. 3.1–3.2, Figs. 1–2). Over that range $\omega/\omega_0$
rises from about 1.15 to 1.4 and $\gamma_{\mathrm{LD}}/\omega$ from about 0
to 0.11 (figure reading; no error figures are given). At $T_i=0.3T_e$ the
damped wave shows **echoes**, "a typical nonlinear behavior for the Landau
damped mode, which is different from dissipative damping" (Fig. 3, citing
Kadomtsev 1968). No IAW-type verification of MEGA's KTI model is reported in
[Sato et al. (2024)](/sources/sato-2024.md); its linear MHD part is
benchmarked against MINERVA (see [MIPS](/software/mips.md)).

## Physical effects found

- **Landau damping of $n=1$ modes near $q_{\min}\gtrsim1$.** With an estimate
  $k_\parallel\approx(n-m/q_{\min})/R$ at $m=1.5$, Liu et al. (2022b, Eq. 4.2)
  find $\omega/k_\parallel=0.20v_{\mathrm{th},i}$ at $q_{\min}=1.04$ and
  $1.15v_{\mathrm{th},i}$ at $q_{\min}=1.15$, with
  $v_{\mathrm{th},i}=\sqrt{T_i/m_i}$, so both the fishbone-like and the
  BAE-like branches are exposed to thermal-ion Landau damping. In DIII-D
  and NSTX cases KTIs raise the fishbone frequency, lower its growth rate
  and stabilize the BAE-like branch (§§4–5; details on
  [fishbone](/definitions/fishbone.md)).
- **Phase shift of the pressure response.** For slowly growing $n=3$
  infernal modes ($\omega_r\approx\gamma$ at high $S$), KTIs make the mode
  rotate in the ion diamagnetic direction and reduce $\gamma$. The
  perpendicular ion pressure perturbation, dominated by trapped ions, stays
  in phase with the radial flow, while the adiabatic electron pressure
  lags. The electron-pressure work on $\mathbf v_\perp$ then changes sign
  ([Sato et al. (2024)](/sources/sato-2024.md), §3.1.3; numbers on
  [infernal mode](/definitions/infernal-mode.md)). The authors suggest
  trapped-ion precession as the cause and state that "the physical
  mechanism determining the phase relationship … remains unclear".
- **No effect when the mode is fast.** When $\omega_r\ll\gamma$ (low $S$,
  $10^5$–$10^6$) the KTI growth rate equals the MHD one (ibid., §3.1.2–3.1.3,
  Figs. 4, 7).
- **Nonlinear profile response.** With KTIs the resistive infernal mode no
  longer flattens the axisymmetric pressure profile (ibid., §3.2.2), and in
  the nonlinear NSTX fishbone the core EP density drops by only about 5%
  ([Liu et al. (2022b)](/sources/liu-2022-b.md), §6).
- **Mechanism depends on geometry.** Sato et al. (2024, §4) state that in
  their earlier helical-plasma work the KTI stabilization of pressure-driven
  modes reduces the ion-pressure fluctuation amplitude, whereas for tokamak
  infernal modes the electron and ion pressure amplitudes are comparable and
  the difference is their phase. This is a stated difference of mechanism
  between geometries, not a contradiction between claims.

## Limitations stated by the sources

- Electron diamagnetic drift is absent from MEGA's KTI runs and left to
  future work ([Sato et al. (2024)](/sources/sato-2024.md), §§2, 4).
- M3D-C1-K drops two-fluid $d_i/L$ terms and the Hall term; the role of
  trapped thermal ions in both drive and damping is asserted without a
  power-transfer separation (Source page of
  [Liu et al. (2022b)](/sources/liu-2022-b.md)).
- Both papers call for revisiting results obtained without kinetic thermal
  ions: non-resonant fishbone studies
  ([Liu et al. (2022b)](/sources/liu-2022-b.md), §7) and MHD infernal
  beta limits ([Sato et al. (2024)](/sources/sato-2024.md), §4).

## Contradictions

None between sources on the method. The KTI variant breaks the
"$n_h\ll n_i$" premise in the definition of the classical hybrid model; this
is a widening of scope, recorded on
[hybrid kinetic-MHD](/methods/hybrid-kinetic-mhd.md), not a disagreement.

# Citations

- [Liu et al. (2022b)](/sources/liu-2022-b.md): M3D-C1-K with kinetic thermal and fast ions, synchronization, $\mathbf E^*$, the IAW test, fishbone Landau damping.
- [Sato et al. (2024)](/sources/sato-2024.md): MEGA with kinetic thermal ions, current coupling through $\mathbf J_i$, the infernal-mode phase-shift mechanism.
- [Liu et al. (2022)](/sources/liu-2022.md): the equivalence of pressure and current coupling invoked for $\mathbf v_\perp$.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md): kinetic thermal ions in JOREK in progress.

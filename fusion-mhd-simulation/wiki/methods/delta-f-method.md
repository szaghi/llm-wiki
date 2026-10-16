---
type: Method
title: "The δf particle method"
description: "Marker method that evolves only the deviation of the energetic-particle distribution from a known equilibrium part, carrying it as a weight advanced along the characteristics; it lowers noise relative to full-f, and the hybrid codes of this bundle use it with or without suppressing the relaxation of a non-equilibrium initial distribution."
status: established
aliases: [delta-f, δf PIC, delta-f particle-in-cell, perturbative particle method]
tags: [hybrid-kinetic, energetic-particles, particles, numerics]
timestamp: 2026-10-16T00:00:00Z
---

# The δf particle method

The δf method splits the energetic-particle distribution as
$f_h=f_0+\delta f$. The equilibrium part $f_0$ is known analytically, and
markers carry only $\delta f$ through a weight $w_p$
([Liu et al. (2022)](/sources/liu-2022.md), §3, Eqs. 7–13;
[Liu et al. (2024)](/sources/liu-2024.md), §II C, Eqs. 15–19;
[Vlad et al. (2025)](/sources/vlad-2025.md), §§2–5). The coupling moments
of a [hybrid kinetic-MHD model](/methods/hybrid-kinetic-mhd.md) are then
perturbed moments ($\delta p_{\parallel h}$, $\delta p_{\perp h}$, or
$\delta\mathbf J_h$), and the equilibrium force balance is subtracted from
the fluid equation (see
[pressure and current coupling](/methods/pressure-and-current-coupling.md)).
Its alternative is *full-$f$*, which JOREK and XTOR-K use. In full-$f$ the
whole distribution is a sum over markers,

$$f_h(\mathbf x,\mathbf v,t)=\sum_{p=1}^{N_p}w_p\,\delta(\mathbf x-\mathbf x_p)\,\delta(\mathbf v-\mathbf v_p),$$

with fixed $w_p$ equal to the number of physical particles per marker
([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), Eq. 1).

## Weight equation

The collisionless kinetic equation conserves $f_h$ along the
characteristics, so $\mathrm d\delta f/\mathrm dt=-\mathrm df_0/\mathrm dt$
along every marker orbit. Let the markers be distributed with phase-space
density $g$, conserved along the same orbits. Define the weight as
$w_p=\delta f/g$. Then

$$\frac{\mathrm dw_p}{\mathrm dt}=-\left(\frac{f_h}{g}-w_p\right)\frac{1}{f_0}\frac{\mathrm df_0}{\mathrm dt}$$

([Liu et al. (2024)](/sources/liu-2024.md), Eq. 15). M3D-C1-K loads markers
from the distribution itself ($g\propto f_h$). It then writes
$w_p=\delta f/f_h$, and the equation becomes
$\mathrm dw_p/\mathrm dt=-(1-w_p)f_0^{-1}\mathrm df_0/\mathrm dt$
([Liu et al. (2022)](/sources/liu-2022.md), Eq. 8). The two forms are the
same equation for the two loading choices. GMEC loads markers uniformly
in phase space by Monte-Carlo rejection with the Jacobian as weight
([Liu et al. (2024)](/sources/liu-2024.md), §II C).

The equilibrium part is a function of the constants of motion of the
unperturbed orbits, $f_0=f_0(P_\phi,\mathcal E,\mu)$, with $\mu$ held
invariant. Its total derivative is therefore driven only by the perturbed
fields:

$$\frac{\mathrm df_0}{\mathrm dt}=\frac{\mathrm dP_\phi}{\mathrm dt}\frac{\partial f_0}{\partial P_\phi}+\frac{\mathrm d\mathcal E}{\mathrm dt}\frac{\partial f_0}{\partial\mathcal E}$$

([Liu et al. (2022)](/sources/liu-2022.md), Eq. 9). In M3D-C1-K the
canonical momentum is $P_\phi=q_h\psi+m_hv_{\parallel p}F/B$. Its rate is
the perturbed guiding-centre drift projected on $\nabla\psi$ plus the
perturbed parallel acceleration times $m_hF/B$. The energy rate is
$\mathrm d\mathcal E/\mathrm dt=q_h\mathbf v\cdot\delta\mathbf E+\mu\,\partial_t\delta B_\parallel$.
The perturbed drift is $\delta\mathbf E\times\mathbf B_0/B_0^2+v_{\parallel p}\delta\mathbf B/B_0$
(Eqs. 10–12). Eq. 13 for the perturbed parallel acceleration is printed
without perturbation subscripts on its first term and without the $1/m_h$
of Eq. 2; it is recorded on the Source page. GMEC writes $P_\phi$ with the
opposite sign of the flux term. It approximates $P_\phi\approx-q_h\psi$ in
all its simulations, so that
$\partial f_0/\partial P_\phi\propto\partial f_0/\partial\psi$
([Liu et al. (2024)](/sources/liu-2024.md), Eq. 17).

**Linear and nonlinear variants.** In linear M3D-C1-K runs the orbits use
the equilibrium fields only and $(1-w_p)\to1$. In nonlinear runs the
perturbed rates are taken as the difference between a Boris push in the full
fields and a guiding-centre push in the equilibrium fields
([Liu et al. (2022)](/sources/liu-2022.md), §3). GMEC labels its runs
linear, because it filters a single toroidal harmonic, but keeps the
particle nonlinearity "fully". Its ITPA TAE run saturates after
$550\tau_A$ "due to particle nonlinearity"
([Liu et al. (2024)](/sources/liu-2024.md), §§II A, III C).

## Moments and the compression correction

The perturbed pressures are marker sums:

- the parallel pressure sums $m_hv_{\parallel p}^2w_p$ times a shape
  function;
- the perpendicular pressure sums $\mu B\,(w_p+\delta B_\parallel/B_0)$,
  so it carries the field-compression term $\delta B_\parallel/B_0$.

The phase-space factor $f/g$ drops out for loading from $f_0$
([Liu et al. (2022)](/sources/liu-2022.md), Eqs. 15–16). Following Belova
(1997), M3D-C1-K and M3D-K replace $w_p$ in the deposition by
$w_p+(1-w_p)\,\delta B^*_\parallel/B^*_\parallel$, where
$B^*_\parallel=\mathbf B^*\cdot\mathbf b$ is the guiding-centre phase-space
Jacobian (linear form: $w_p+\delta B^*_\parallel/B^*_\parallel$). With this
term and the $\delta B_\parallel/B_0$ term, the EPs "behave like plasma with
heat capacity ratio $\Gamma=2$ in the perpendicular direction" (ibid.,
§3). The moments are then Galerkin-projected on the finite-element test
functions and a mass-matrix solve follows (Eqs. 17–18; see
[particle-to-mesh projection](/methods/particle-to-mesh-projection.md)).
Eqs. 17–18 drop the $\delta B_\parallel/B_0$ term of Eq. 16 without comment.
GMEC scatters $m_hv_{\parallel p}^2w_p$ and $\tfrac12m_hv_\perp^2w_p$
trilinearly to the 8 neighbouring nodes. With FLR, a pull-back averages the
deposition over the $N=4$ gyro-points
([Liu et al. (2024)](/sources/liu-2024.md), Eqs. 20–22).

## Initial relaxation: δf with a suppressed term versus full-f

The benchmarks of this bundle load an isotropic Maxwellian, which is not a
function of the constants of motion. Such a distribution relaxes in real and
velocity space as soon as it is evolved.

- **The δf codes suppress the relaxation.** HYMAGYC, MEGA and ORB5 solve a
  δf Vlasov equation in which the term (unperturbed phase-space
  velocity)$\cdot\nabla$(initial distribution) is suppressed, to prevent the
  initial relaxation ([Vlad et al. (2025)](/sources/vlad-2025.md), §2).
  The equilibrium is then the prescribed Maxwellian, not a kinetic
  equilibrium.
- **The full-f codes cannot.** XTOR-K relaxes within about 0.05 ms toward an
  ORB5-like profile ([Vlad et al. (2025)](/sources/vlad-2025.md), §6). In
  JOREK's ITPA TAE run the midplane EP pressure peak drops from about 9.3 to
  6.5 kPa, and the $v_\parallel$ distribution develops a dip near
  $v_\parallel=0$
  ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §IV.A, Fig. 4).
  Bogaarts et al. state that "one-to-one comparison" with codes that switch
  relaxation off is therefore difficult. A realistic NUBEAM distribution
  relaxes much less (§V, Fig. 13).
- **Losses are a separate effect.** In δf HYMAGYC about 15% of the EPs are
  first-orbit losses, because markers crossing the last closed flux surface
  are not re-injected. MEGA shows no initial relaxation
  ([Vlad et al. (2025)](/sources/vlad-2025.md), §3, Fig. 4).

Noise is the price of full-$f$. XTOR-K's linear phase is buried in full-$f$
PIC noise, so its growth rates cannot be measured, and its total energy is
too noisy to use as a diagnostic
([Vlad et al. (2025)](/sources/vlad-2025.md), §6). JOREK reaches 5%
convergence of the ITPA TAE growth rate with $2\times10^7$–$2\times10^8$
markers ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §IV.A,
Fig. 2).

## Contradictions

None between sources on the method itself. The difference in initial
relaxation between δf and full-$f$ codes is a known modelling difference,
not a contradiction. It is one of the reasons the benchmark pages give for
code-to-code spread
([ITPA TAE](/benchmarks/itpa-tae-benchmark.md),
[NLED-AUG](/benchmarks/nled-aug-benchmark.md)).

# Citations

- [Liu et al. (2022)](/sources/liu-2022.md): Eqs. 7–18, weights, $f_0(P_\phi,\mathcal E,\mu)$, compression correction, linear and nonlinear variants.
- [Liu et al. (2024)](/sources/liu-2024.md): Eqs. 15–22, the general weight equation, uniform loading, the $P_\phi$ approximation, gyro-averaged deposition.
- [Vlad et al. (2025)](/sources/vlad-2025.md): δf with the relaxation term suppressed (HYMAGYC, MEGA, ORB5) against full-$f$ (XTOR-K).
- [Bogaarts et al. (2022)](/sources/bogaarts-2022.md): the full-$f$ alternative in JOREK and its initial relaxation.

---
type: Method
title: "Kinetic (Monte Carlo) neutral model coupled to MHD"
description: "JOREK model in which atomic neutrals are Monte Carlo superparticles that undergo ionization, charge exchange, line radiation and recombination, recycle and sputter at the wall, and return their moments to the implicit fluid as explicit sources once per fluid step through a regularized finite-element projection."
status: established
aliases: [kinetic neutrals, Monte Carlo neutrals, JOREK kinetic neutral model]
tags: [neutrals, particles, edge, divertor]
timestamp: 2026-10-16T18:35:00Z
---

# Kinetic (Monte Carlo) neutral model coupled to MHD

The kinetic neutral model of [JOREK](/software/jorek.md) replaces the
[diffusive neutral fluid](/methods/fluid-neutral-models.md) by Monte Carlo
superparticles in JOREK's particle framework, so that neutral transport is
ballistic and charge exchange is represented
([Korving et al. (2023)](/sources/korving-2023.md), §IV). It uses the same
conservative plasma–neutral source terms as the fluid model and was built
for divertor and SOL studies in which the diffusive model was "not
sufficient to provide the correct plasma mechanics" (§V B).
[Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (§2.4) list it among the
2021–2024 JOREK developments.

## Particles and reactions

- **Markers.** $10^6$–$10^7$ superparticles, each standing for
  $5\times10^{13}$–$5\times10^{14}$ atoms on average, pushed by the same
  full-orbit Boris integrator as the kinetic ions and located both in
  $(R,Z,\phi)$ and in element coordinates
  ([Korving et al. (2023)](/sources/korving-2023.md), §IV A, §V D; see
  [particle pushers](/methods/particle-pushers.md)). The kinetic step is
  $\Delta t_{\mathrm{kin}}=2\times10^{-8}$ s against a fluid step of
  $2.246\times10^{-6}$ s (§V D, §V F).
- **Ionization** by weight reduction: in each kinetic step a marker loses
  the fraction $1-\exp(-n_e\langle\sigma v\rangle_{\mathrm{ion}}\Delta t_{\mathrm{kin}})$
  of its weight, which becomes plasma mass, momentum and energy (with the
  ionization energy charged to the plasma); markers whose weight falls
  below a threshold are removed (Eqs. 26–27). The printed update assigns
  the ionization probability to the surviving weight, the converse of its
  definition (recorded on the Source page).
- **Charge exchange**: with probability
  $1-\exp(-n_e\langle\sigma v\rangle_{\mathrm{cx}}\Delta t_{\mathrm{kin}})$
  the marker's velocity is resampled from a Maxwellian of thermal speed
  $\sqrt{T_e/m_i}$ shifted by the plasma velocity (as printed: $T_e$, not
  $T_i$); the momentum and kinetic
  energy difference go to the plasma, the particle source is zero
  (Eqs. 28–29). The printed momentum and energy sources omit the particle
  mass.
- **Line radiation** removes $n_ew_pL_{\mathrm{line}}(n_e,T_e)\Delta t_{\mathrm{kin}}$
  from the plasma energy (Eq. 30).
- **Recombination** is computed by the fluid: the recombined mass of each
  finite element in a fluid step becomes at least one new marker, placed
  uniformly in the element and in a toroidal sector and given the plasma
  velocity, which "ensures mass and energy conservation" (Eq. 31).
- **Wall interaction**: reflection versus thermal desorption from the TRIM
  database (cited through EIRENE), sputtering from Eckstein yields; wall
  markers are injected once per fluid step, and the authors state that
  this pulsed injection does "not result in oscillating or pulsed
  solutions" (§IV B, Eq. 24).
- **Missing physics**: no molecules and no neutral–neutral collisions;
  charge exchange exists only in the kinetic model (§IV, §IX).

## Coupling to the fluid

Particle contributions are accumulated at every kinetic step, which the
authors found "essential" for conservation, and projected once per fluid
step onto the Bézier–Fourier basis by the regularized
[particle-to-mesh projection](/methods/particle-to-mesh-projection.md)
(Eqs. 22–23). The projected mass, momentum and energy sources
$S_\rho$, $\mathbf S_{\mathbf v}$, $S_E$ enter the fluid equations as
(Eq. 25)
$$\partial_t\rho=S_\rho,\qquad \rho\,\partial_t\mathbf v=\mathbf S_{\mathbf v}-\mathbf v\,S_\rho,\qquad \partial_t(\rho T)=(\Gamma-1)\Big(S_E-\mathbf v\cdot\mathbf S_{\mathbf v}+\tfrac12 v^2S_\rho\Big).$$
The sources are explicit in the particle moments but multiply implicit MHD
terms "to maintain the highest order accuracy"; when kinetic particles
dominate, the order may drop, and (semi-)implicit coupling is left to
future work (§IV C). The fluid advance is the implicit BDF2 scheme of
[implicit time integration](/methods/implicit-time-integration.md).

## Conservation and cost

- Recombination conserves momentum to a mean relative error of about
  $10^{-4}$ and energy to about $10^{-3}$; the global steady-state power
  balance closes to $10^{-3}$–$10^{-2}$ depending on time step and particle
  number; BDF2 itself "does not conserve energy exactly" (§V F, Fig. 6,
  Eq. 32).
- With $10^6$ particles the kinetic model runs as fast as the fluid neutral
  model on 4 nodes × 36 cores and is stated to scale "almost ideally" with
  node count (no scaling data shown). A steady state costs 9000–10000 core
  hours, 60–70 h wall time (§V D).

## Benchmark against SOLPS-ITER

The model was compared with SOLPS-ITER fuelling scans of the ITER PFPO-1
H-mode (1.85 T, 5 MA, 20 MW, no impurities; Park et al. 2021), with JOREK
reduced to frozen fields and no drifts
([Korving et al. (2023)](/sources/korving-2023.md), §V, Figs. 4–5).
SOLPS-ITER includes molecules, two temperatures, a separate EIRENE grid and
the dome; JOREK includes the core but not the sub-dome region.

- Total divertor power: agreement to within 10% for upstream separatrix
  densities of $1$–$2\times10^{19}$ m$^{-3}$; the inner/outer power split
  is slightly more symmetric in JOREK.
- Detachment: at about 10% higher upstream density and less sharp, with a
  weaker density saturation from about $2.4\times10^{19}$ m$^{-3}$.
- Peak heat flux: about twice SOLPS-ITER's in the conduction-limited
  regime, with a similar slope against upstream density; at low density
  the inner-target peak is higher in JOREK, unexplained.

With $E\times B$ drifts switched on, the same model produces the
[high-field-side high-density region](/results/high-field-side-high-density-region.md)
([Korving et al. (2023)](/sources/korving-2023.md), §VI–VIII;
[Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §2.4, Fig. 4).

## Contradictions

**JOREK kinetic neutrals vs SOLPS-ITER on ITER PFPO-1** — Open.
[Korving et al. (2023)](/sources/korving-2023.md) (§V C, §IX) find JOREK's
divertor power within 10% of SOLPS-ITER (Park et al. 2021, as reported
there), but detachment at about 10% higher upstream density and peak target
heat fluxes about twice as high. The authors attribute the differences,
without a test, to the missing molecules and neutral–neutral collisions
and to JOREK's single-temperature model. Both codes are established
references for their physics. The disagreement is therefore a model
difference, not a demonstrated error of either code. A JOREK run with two
temperatures and a molecular model, or a SOLPS-ITER run with molecules and
neutral–neutral collisions removed, would settle the attribution.

# Citations

- [Korving et al. (2023)](/sources/korving-2023.md) — §IV, Eqs. 22–31; §V, Figs. 4–6; §IX.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §2.4, Fig. 4.

---
type: Method
title: "Shock-capturing artificial viscosity for MHD finite elements"
description: "Solution-dependent, field-aligned artificial diffusion added to the hydrodynamic equations of JOREK full MHD, with a coefficient built from a pressure-gradient sensor and a pressure-rate shock strength; it lets 3D shattered-pellet simulations run with larger time steps at preserved thermal-quench dynamics, but over-stabilization suppresses the quench."
status: established
aliases: [shock capturing, discontinuity capturing, artificial viscosity, pressure-sensor shock capturing]
tags: [stabilization, finite-elements, numerics, full-mhd, disruption, impurities]
timestamp: 2026-10-16T00:00:00Z
---

# Shock-capturing artificial viscosity for MHD finite elements

High-order finite elements develop Gibbs oscillations near shocks and steep
fronts; [Bhole et al. (2023)](/sources/bhole-2023.md) (§1, §3.2) add to the
[Bézier–Hermite](/methods/bezier-finite-elements.md) Galerkin form of
[JOREK](/software/jorek.md) full MHD a BV-type shock-capturing diffusion,
alongside the $L^2$-type
[VMS stabilization](/methods/variational-multiscale-stabilization.md). The
form follows Bassi et al. (discontinuous-Galerkin Navier–Stokes) and an
earlier $C^1$ Powell–Sabin finite-element implementation for 2D Euler
(§3.2). The application is massive impurity deposition by
[shattered pellet injection](/definitions/shattered-pellet-injection.md),
where ablation clouds create moving pressure discontinuities (§4). The review
of the JOREK community states that it made highly non-linear full-MHD studies
of mitigated disruptions possible that "were previously not possible"
([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §5).

## Formulation

The term added to the weak form is
$$\mathcal D_{\mathrm{sc}}(\bar{\mathbf u},\mathbf w)=\nabla\mathbf w:\big(\underline{\tau}_{\mathrm{sc}}\nabla\bar{\mathbf u}\big),\qquad \underline{\tau}_{\mathrm{sc}}=\tau_{\mathrm{sc}}\big(C^{\mathrm{sc}}_\parallel\,\mathbf b\otimes\mathbf b+C^{\mathrm{sc}}_\perp(\mathsf I-\mathbf b\otimes\mathbf b)\big),$$
equivalently
$$\mathcal D_{\mathrm{sc}}=\tau_{\mathrm{sc}}C^{\mathrm{sc}}_\perp\,\nabla\mathbf w:\nabla\bar{\mathbf u}+\tau_{\mathrm{sc}}\big(C^{\mathrm{sc}}_\parallel-C^{\mathrm{sc}}_\perp\big)\,(\mathbf b\cdot\nabla\mathbf w)\cdot(\mathbf b\cdot\nabla\bar{\mathbf u})$$
([Bhole et al. (2023)](/sources/bhole-2023.md), Eq. 31), with
$C^{\mathrm{sc}}_\parallel,C^{\mathrm{sc}}_\perp\ge0$ user factors and
$\mathbf w$ the test function. The scalar coefficient is
$$\tau_{\mathrm{sc}}=h_e^2\,\frac{\dot p_{\mathrm{op}}+\dot p_{\mathrm{src}}}{p}\;h_e\frac{\|\nabla p\|}{p},$$
$$\dot p_{\mathrm{op}}=\Big|\frac{\partial p}{\partial\rho}\mathcal T_{\mathrm{op}}(\rho)+\frac{\partial p}{\partial\rho_{\mathrm{imp}}}\mathcal T_{\mathrm{op}}(\rho_{\mathrm{imp}})+\frac{\partial p}{\partial T}\mathcal T_{\mathrm{op}}(T)\Big|,\qquad \dot p_{\mathrm{src}}=\Big|\frac{\partial p}{\partial\rho}\mathcal T_{\mathrm{src}}(\rho)+\frac{\partial p}{\partial\rho_{\mathrm{imp}}}\mathcal T_{\mathrm{src}}(\rho_{\mathrm{imp}})+\frac{\partial p}{\partial T}\mathcal T_{\mathrm{src}}(T)\Big|$$
(Eqs. 32–33), where $\mathcal T_{\mathrm{op}}(q)$ and $\mathcal T_{\mathrm{src}}(q)$
denote the rates of change of $q$ produced by the differential operator and by
the sources of its equation, $p$ is the total pressure including the impurity
contribution, $\rho_{\mathrm{imp}}=m_{\mathrm{imp}}n_{\mathrm{imp}}$ and $h_e$ is
the element size of the VMS term. The factor $h_e\|\nabla p\|/p$ is a
dimensionless pressure-gradient sensor; $(\dot p_{\mathrm{op}}+\dot p_{\mathrm{src}})/p$
is an inverse time scale, the "shock strength". The coefficient therefore has
the dimension of a diffusivity, $\tau_{\mathrm{sc}}\sim h_e^3\,|\dot p|\,\|\nabla p\|/p^2$,
and vanishes as $O(h_e^3)$ under refinement, faster for smooth pressure
(Eq. 32, §4.3.2; dimensional reading by the reader).

**Where it acts.** The term is applied to the momentum (test functions
weighted by $\rho$), density, energy and impurity equations, **not** to the
induction equation (Eq. 38, zeros in the three $\mathbf A$ slots). All tests
use the isotropic setting $C^{\mathrm{sc}}_\parallel=C^{\mathrm{sc}}_\perp=c$;
the field-aligned anisotropic form is formulated but not exercised (§3.2,
§4). It is advanced implicitly with the $\theta_{\mathrm t}$-weighting of the
[implicit scheme](/methods/implicit-time-integration.md) (Eq. 40).

**Stronger modulation.** For low resistivity a second coefficient replaces the
shock strength,
$$\tau_{\mathrm{sc}}=h_e^2\,\Theta_{\mathrm{sc}}\;h_e\frac{\|\nabla p\|}{p},\qquad \Theta_{\mathrm{sc}}=\frac1p\Big|\frac{\partial p}{\partial\rho}\mathcal T_{\mathrm{op}}(\rho)+\frac{\partial p}{\partial\rho_{\mathrm{imp}}}\mathcal T_{\mathrm{op}}(\rho_{\mathrm{imp}})+\frac1\rho\frac{\partial p}{\partial T}\mathcal T_{\mathrm{op}}(p)\Big|$$
(Eq. 49, as printed), with the source contribution dropped; it is stated to
give a larger coefficient and to damp spurious waves from the interpolation of
atomic data (§4.3.2).

## Results

All cases are JET-like (pulse 85943) SPI simulations with 100 fragments
([Bhole et al. (2023)](/sources/bhole-2023.md), §4.1).

| Case | Stabilization | Outcome | Location |
|---|---|---|---|
| Reduced MHD, axisymmetric Ar source | $c=0$ | linear solver fails at ~0.59 ms | §4.2.1.1, Figs. 4–5 |
| | $c=0.1$ | indistinguishable from $c=0$ | |
| | $c=1$ | runs further, deviates; pressure discontinuity smeared more as $c$ grows | |
| Full MHD, axisymmetric Ne source | $c=0$ | solver fails at ~1.4 ms | §4.2.1.2, Figs. 6–7 |
| | VMS + $c=1$ | past 2.5 ms; nearly identical $W_{\mathrm{th}}$, slightly lower ablation | |
| Full MHD, 3D Ne, $\eta_0=4.22\times10^{-8}\ \Omega$ m, $n\le7$ | $c=0$, no VMS | >9000 steps to ~1.7 ms; inverted harmonic ordering ($n=7$ largest), blow-up near 1.75 ms | §4.3.1, Figs. 9–10 |
| | VMS + $c=1,10,50$ | <5000 steps; low-$n$ dominance restored; TQ, 3/1, 2/1 then 1/1 growth and an $I_p$ spike reproduced with $c=10$ | Figs. 9–14 |
| Full MHD, 3D, $\eta_0=4.22\times10^{-9}\ \Omega$ m (case C) | Eq. 49, $c=10$ | $\Delta t$ held at 5 normalized units throughout; very diffusive: no TQ, no $I_p$ spike, high-$n$ energies above low-$n$ | §4.3.2, Figs. 15–19 |

GMRES cost to $t\approx1.5$ ms on 64 MPI processes (Table 1): $c=0$: 8096
steps × 6.05 s = 13.6 h; $c=1$: 3988 × 10.64 s = 11.8 h; $c=10$: 1182 ×
15.21 s = 5 h; $c=50$: 1182 × 17.62 s = 5.78 h. The cost per solve rises with
the stabilization (worse conditioning), but the larger time step wins: $c=10$
is about 2.7 times cheaper than $c=0$ (Table 1; the arithmetic checks). Maps
of $\tau_{\mathrm{sc}}$ are large only at the initial pedestal pressure jump
and at the moving fronts near the impurity clouds (Fig. 13). $W_{\mathrm{th}}$
and $I_p$ overlap between stabilized and unstabilized runs, and the authors
conclude that the term "does not alter the underlying physics" (Fig. 14);
$c=50$ "has altered the dynamics and is more than required" (Fig. 11).

## Qualifications

- **The physics-preservation check stops before the quench.** The comparison
  with the unstabilized run extends only to ~1.75 ms, where that run ends,
  while the thermal quench occurs between 2 and 3 ms (Fig. 14; reader's note).
- **Coefficients are tuned by hand.** The optimal coefficients depend on
  $\eta$, viscosity, the diffusivities and the grid, and are chosen "based on
  experience"; no well-resolved low-$\eta$ run succeeded (§4.3.2, §5).
- **Printed inconsistencies.** Eq. 49 has $\mathcal T_{\mathrm{op}}(p)$ in the
  last term where Eq. 33 has $\mathcal T_{\mathrm{op}}(T)$; with the prefactor
  $\rho^{-1}\partial p/\partial T$ the term has the dimension of a pressure rate
  only if $p\sim\rho T$ (reader's note). The text of §4.3.2 says the Eq. 33
  criterion with $c=10$ made case C diffusive, while Table 2 assigns Eq. 49 to
  case C, and the text says the "Eq. (32) sensor" failed while Table 2 labels
  criteria by Eq. 33. Table 1 gives identical step counts (1182) for $c=10$ and
  $c=50$ while Fig. 9a is said to show "a further advantage" for $c=50$; the
  text calls the $c=10$ gain both "less than twice the time" and "more than
  twice the speed up" (reader's notes 13–15).
- The reduced-MHD test does not state whether VMS was on, and no
  shock-capturing-only run isolates this term from VMS
  ([Bhole et al. (2023)](/sources/bhole-2023.md), §4.2.1.1; reader's note).
- No canonical shock test (Sod, Brio–Wu), convergence-order study or
  comparison with another code or with the JET discharge is given (reader's
  note). The version read is the HAL submission of October 2022.

# Citations

- [Bhole et al. (2023)](/sources/bhole-2023.md) — §1, §3.2, Eqs. 31–33, 38, 49, §4, Tables 1–2.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §5.

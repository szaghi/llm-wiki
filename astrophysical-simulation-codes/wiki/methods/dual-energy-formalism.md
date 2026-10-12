---
type: Method
title: "Dual-energy formalism"
description: "Carrying a non-conservative internal-energy equation alongside total energy, taking the pressure from it where kinetic energy dominates (thermal fraction below η1 = 1e-3 in Enzo) and resynchronizing it from total energy where the thermal fraction exceeds η2 = 0.1; used by Enzo (Bryan et al. 1995 lineage) and, in a dual-energy-like form, by Castro."
status: established
aliases: [dual energy, dual-energy switch, internal-energy switch, dual energy formalism]
tags: [dual-energy, hydro, cosmology, conservation]
timestamp: 2026-10-12T00:00:00Z
---

# Dual-energy formalism

The dual-energy formalism carries an internal-energy equation alongside
the total-energy equation and chooses between them cell by cell. Enzo
motivates it by kinetic-to-internal energy ratios of up to $10^8$ in
cosmological flows
([Bryan et al. (2014)](/sources/bryan-2014.md), §4.1.1).

## Enzo's switches

[Enzo](/software/enzo.md)'s PPM solver carries the internal-energy
equation (eq. 42), differenced non-conservatively with the pressure at
the old time (eq. 43), and applies two thresholds (§4.1.1, eqs. 44–45):
* **Pressure selection.** The pressure is computed from
  $E - \tfrac12\rho\vert\mathbf v\vert^2$ where
  $$\frac{E - \tfrac12\rho\vert\mathbf v\vert^2}{E} > \eta_1,$$
  and from the internal-energy equation otherwise; $\eta_1 = 10^{-3}$.
* **Resynchronization.** The internal energy is reset from the total
  energy where
  $$\frac{E_i - \tfrac12\rho_i\vert\mathbf v_i\vert^2}{\max\left(E_{i-1},E_i,E_{i+1}\right)} > \eta_2,$$
  with $\eta_2 = 0.1$.
* The paper writes eqs. 44–45 with specific energies while eq. 5 defines
  $E$ and $e$ as densities, without saying so; the forms above are the
  same ratios in registry (density) variables.
* The scheme is related to the total-energy-plus-entropy scheme of Ryu et
  al. (1993). Enzo's MHD-CT solver offers dual energy with either the
  internal energy or the entropy (§4.1.1, §4.3).
* Enzo's ZEUS solver evolves internal rather than total energy, so it
  needs no dual energy but does not conserve total energy. In the shock
  pool test ZEUS puts the shock in the wrong position, and in the Sedov
  blast it lags the analytic solution; the paper relays Clarke (2010)'s
  attribution of the lag to the internal-energy formulation (§4.4,
  §11.2.3, §11.2.5; [Sedov–Taylor blast wave](/benchmarks/sedov-taylor-blast-wave.md)).

## Castro

[Castro](/software/castro.md) evolves $\rho e$ "dual-energy-like" when the
kinetic energy dominates, after Bryan et al. (1995)
([Almgren et al. (2010)](/sources/almgren-2010.md), end of §5.1); the
paper gives no thresholds. Castro also carries $\rho e$ among the
reconstructed primitive variables, and its
[two-shock Riemann solver](/methods/approximate-riemann-solvers.md)
returns an interface $\rho e$ without calling the EOS (§5.2, eqs. 27–29,
34).

# Citations

1. [Bryan et al. (2014)](/sources/bryan-2014.md), §4.1.1, §4.3, §4.4, §11.2.3, §11.2.5 (arXiv v1).
2. [Almgren et al. (2010)](/sources/almgren-2010.md), §5.1–5.2 (arXiv v1).

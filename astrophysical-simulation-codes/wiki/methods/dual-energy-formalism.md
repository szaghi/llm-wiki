---
type: Method
title: "Dual-energy formalism"
description: "Carrying a non-conservative internal-energy equation alongside total energy, taking the pressure from it where kinetic energy dominates (thermal fraction below η1 = 1e-3 in Enzo) and resynchronizing it from total energy where the thermal fraction exceeds η2 = 0.1; used by Enzo (Bryan et al. 1995 lineage), in a dual-energy-like form by Castro, and by Cholla with a single neighbourhood threshold of 0.035 that resynchronizes both ways."
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

## Later uses (batch 2)

### The same cancellation in relativistic MHD

[Kastaun, Kalinani & Ciolfi (2021)](/sources/kastaun-2021.md) quantify, for
ideal relativistic MHD, the problem that motivates the dual-energy
formalism: the specific internal energy $e$ is recovered from the evolved
conserved variables as a small difference of the total energy and the
kinetic and magnetic parts. See
[primitive-variable recovery](/methods/primitive-variable-recovery.md).
* **Round-off** (§IV B). Cancellation in $e$ loses digits of order
  $(W\vert\mathbf v\vert)^2/e$ and of order the squared field strength per
  unit conserved density times $W/e$; together with the conditioning of the
  root-find this sets a floor on the attainable accuracy at high Lorentz
  factor or very small $e$ (Fig. 3).
* **Evolution errors** (§V B–C, Fig. 6). Relative errors in the conserved
  energy or field are amplified into $e$ by factors that grow with the
  magnetic and kinetic energy relative to $e$; for a field of $10^{15}$ G, a
  relative error of $10^{-4}$ in the field or the energy dominates $e$ at
  densities of about $10^{8}$ g cm$^{-3}$. In magnetically dominated regions
  the momentum is not amplified; only $e$ suffers the cancellation.
* **Floor corrections** (§III A, §V D). When the recovered $e$ falls below
  the zero-temperature value, only the conserved energy $\tau$ is changed;
  density and momentum are untouched. The resulting positive bias causes
  spurious heating until the thermal energy reaches the width of the energy
  error distribution.
* The paper proposes no dual-energy or entropy fallback; it accepts the
  loss as "a fundamental consequence of evolving the conserved variables"
  (§V).

## Later uses (batch 4)

### Cholla: one threshold, total energy resynchronized

[Cholla](/software/cholla.md)'s cosmology version carries the
internal-energy equation alongside total energy and applies, per cell at
the end of each step, a single test "similar to that used in Enzo"
([Villasenor et al. (2021)](/sources/villasenor-2021.md), §2.3, eq. 13).
Written in registry (density) variables:
* the advected internal energy is kept where
  $$\frac{E_i - \tfrac12\rho_i\vert\mathbf v_i\vert^2}{\max\left(E_{i-1},E_i,E_{i+1}\right)} < 0.035,$$
  the maximum taken over the cell and its neighbours (in 3D, the adjacent
  cells); otherwise the internal energy is taken as
  $E_i - \tfrac12\rho_i\vert\mathbf v_i\vert^2$;
* then the total energy is reset from the selected internal energy,
  $E = \rho e + \tfrac12\rho\vert\mathbf v\vert^2$.

The neighbourhood-maximum test has the structure of Enzo's
resynchronization test above, but one threshold serves both selection and
resynchronization, and Cholla resynchronizes both ways: cells at or above
the threshold take the internal energy from the total (Enzo's direction),
cells below it have the total energy reset from the advected internal
energy. Where the advected internal energy is selected the total energy is
therefore changed; the paper does not discuss the effect on
total-energy conservation. The paper writes the test with specific
energies.

**Choosing the threshold** (§2.3, §3.4). Too low a threshold gives
"spurious heating owing to numerical errors introduced in the total
energy evolution"; too high suppresses shock heating, because the advected
internal energy does not capture it. The value 0.035 was chosen with a new
**mean-cosmic-temperature test** (§3.4, eqs. 41–42, Figs. 5–6): in an
adiabatic cosmological run started at 230 K at redshift 100, the
mean gas temperature is compared with an estimate built from the
virial temperatures of the halos found in the run plus adiabatically
cooling gas outside them. With 0.035 heating starts at redshift about 12,
as in the estimate; [Enzo](/software/enzo.md) and Cholla with this switch
heat from redshift about 15 and follow the estimate below redshift 6. The
sharp jump near redshift 12 is attributed to unresolved early low-mass
halos, checked against a Sheth & Tormen (1999) mass-function estimate.

### Ramses-type truncation-error criterion

Villasenor et al. also implement the criterion of Teyssier (2015)
(§2.3, eqs. 14–15): the internal energy is taken from the total energy
where the thermal energy density exceeds a factor (0.5 suggested) times a
truncation-error estimate, half the density times the squared velocity
difference to neighbouring cells, and the advected internal energy is used
otherwise. In uniform-grid cosmological runs it is "overly restrictive":
* it selects the advected internal energy predominantly, "suppressing
  shock heating inside collapsed halos and significantly lowering the
  average cosmic temperature"; gas in Ramses and in Cholla with this
  criterion keeps cooling adiabatically to redshift about 6 (§3.4,
  Fig. 5);
* the gas power spectrum with it is higher than with the Enzo-like switch
  by about 50 % at small scales by redshift 5, about 80 % at redshift 2
  and about 30 % at redshift 0 (Fig. 6 caption: 30–80 % for redshift 0 to
  6);
* in the [Zel'dovich pancake](/benchmarks/zeldovich-pancake.md) it selects
  the advected internal energy throughout and suppresses the central shock
  (§3.1).

The authors note that the truncation-error estimate depends on resolution,
so the suppression "might be reduced in high resolution AMR simulations";
this is not tested (§3.4).

# Citations

1. [Bryan et al. (2014)](/sources/bryan-2014.md), §4.1.1, §4.3, §4.4, §11.2.3, §11.2.5 (arXiv v1).
2. [Almgren et al. (2010)](/sources/almgren-2010.md), §5.1–5.2 (arXiv v1).
3. [Kastaun, Kalinani & Ciolfi (2021)](/sources/kastaun-2021.md), §§III A, IV B, V B–D (arXiv v2).
4. [Villasenor et al. (2021)](/sources/villasenor-2021.md), §§2.3, 3.1, 3.4, eqs. 13–15, 41–42, Figs. 5–6 (arXiv v2).

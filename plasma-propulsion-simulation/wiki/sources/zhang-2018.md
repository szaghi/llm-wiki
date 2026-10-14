---
type: Source
title: "Zhang et al. (2018) — Investigation on plume expansion and ionization in a laser ablation plasma thruster"
description: "Couples a 2D enthalpy heat-conduction model of nanosecond laser ablation of an aluminium target (vaporization, phase explosion, plume shielding) with a 2D axisymmetric multi-species Euler plume model (AUSM+-up, finite-rate ionization to Al3+, inverse bremsstrahlung) inside a ceramic tube, validated on ablation depth and plume fronts, and gives linear fits of plume velocity, temperature, impulse bit and ablated mass over 5-30 J/cm2."
resource: "doi:10.1016/j.actaastro.2018.06.045"
source_kind: paper
authors: [Zhang Y., Wu J., Zhang D., Tan S., Ou Y.]
year: 2018
venue: "Acta Astronaut. 151:432–444"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Zhang_Investigation_on_plume_expansion_and_ionization_in_a_laser_a.pdf"
tags: [pulsed-plasma-thruster, fluid, plume, verification]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper models the first stage of the authors' laser ablation plasma
thruster (LA-PPT), which separates laser ablation from electromagnetic
acceleration with a ceramic tube: nanosecond Nd:YAG ablation of an
aluminium target and the expansion and ionization of its plume inside the
tube. A 2D $(z,r)$ enthalpy heat-conduction model of the target, with
melting, Hertz–Knudsen vaporization, a dielectric transition near the
critical temperature and phase explosion, is coupled every step to a 2D
axisymmetric inviscid multi-species Euler model of the plume (Al, Al$^+$,
Al$^{2+}$, Al$^{3+}$, e$^-$) with finite-rate ionization and
inverse-bremsstrahlung absorption, discretized by AUSM+-up. It is validated
against Porneala & Willis, checked by grid and time-step studies with an
a-priori error estimate, and run over fluences of 5–30 J/cm$^2$. The
electromagnetic stage is not modelled. Merged into
[laser-ablation plume model](/methods/laser-ablation-plume-model.md) and
[pulsed plasma thruster](/definitions/pulsed-plasma-thruster.md).

# Key claims

1. **Concept** (§1; attributed to ref. 1): $I_{sp}\approx8000$ s and thrust
   efficiency about 90% with metallic propellant; classic PPT efficiency
   "often around 10–15%"; the laser-assisted PPT of Horisawa et al. suffers
   "late ablation".
2. **2D needed** (§1): most earlier ablation-plume models are 1D; the tube
   wall confines radial expansion.
3. **Target model** (§2.1, Eqs. 1–12): $\partial_tH=\partial_z(K\partial_zT)+\partial_r(K\partial_rT)+v_{sur}\partial_zH+S$;
   vaporization $\dot m_{vap}=\beta_v\left(\frac{m_g}{2\pi k_BT_s}\right)^{1/2}p_b\exp\left[\frac{m_gL_v}{k_B}\left(\frac1{T_b}-\frac1{T_s}\right)\right]$
   with $\beta_v=0.82$, $p_b=1.01325\times10^5$ Pa, $m_g=4.48\times10^{-26}$ kg;
   homogeneous nucleation above $0.8T_c$, strong near $0.9T_c$
   (Eqs. 3–5); recession $v_{sur}=(\dot m_{vap}+\dot m_{exp})/\rho(T_s)$
   (Eq. 6); Beer–Lambert deposition and plume shielding (Eqs. 7–8);
   coordinate mapping $\xi=(z-s)/(\delta-s)$ (Eqs. 9–11).
4. **Plume model** (§2.2, Eqs. 13–24): $\partial_tQ+\partial_zF+\partial_rG+H=S$;
   $T_e=T$; quasi-neutrality $n_{Al^+}+2n_{Al^{2+}}+3n_{Al^{3+}}=n_e$;
   forward ionization rates with reference diameter $2\times10^{-10}$ m,
   $Z_i=3\times10^4$, $w=0.75$, $T_{ref}=300$ K; backward rates from
   Saha-type equilibrium constants; ionization energies 5.98577, 18.82856,
   28.44765 eV (Table 3); inverse-bremsstrahlung absorption with
   electron–neutral coefficient $10^{-36}$ cm$^5$ and electron–ion
   charge-squared weights.
5. **Validation** (§3.1, Fig. 3): computed threshold about 5 J/cm$^2$
   against 5.2 J/cm$^2$; ablation depths and plume fronts agree
   graphically (no error metric; no shock in the model).
6. **Error estimate** (§3.2, Eqs. 25–27, Table 5): summed error of 30 ns runs
   0.387–1.225%, below the 5% bound.
7. **Target history** (§3.3, Fig. 6): surface above $T_b$ at 3 ns; held at
   $0.9T_c$ from 4 to 10.5 ns; $0.8T_c$ at 11.4 ns for about 0.8 ns; below
   $T_b$ at 20 ns.
8. **Plume** (§3.4, Figs. 7–12): centreline peak velocity about 2400, 4000
   and 4600 m/s at 3.5, 10.5 and 20 ns; full single ionization (electron
   number fraction 0.5) at the front by 20 ns; the plume reaches the wall at
   60.5 ns; near the wall about 9500 K at 60.5 ns and about 25000 K at
   100 ns, with secondary and tertiary ionization.
9. **Fluence scan** (§3.5, Figs. 13–15): $V=16F+6216$ m/s and
   $T=147F+5816$ K at 200 ns, $I_b=0.14F+12.3$ µN·s, $m_a=0.031F-0.012$ µg,
   with $F$ the fluence in J/cm$^2$; at 10 J/cm$^2$ peak thrust 175 N, pulse
   width below 0.3 µs, impulse bit about 14 µN·s at 1.5 µs.

# Models and numerics

* Explicit finite differences for the target, AUSM+-up for the plume,
  stated second order in space and time; coupled every step.
* Grids $100\times200$ (target) and $100\times200$ (plume);
  $\Delta t=1\times10^{-12}$ s; tested $1\times10^4$, $2\times10^4$,
  $4\times10^4$ cells and $5\times10^{-13}$, $1\times10^{-12}$,
  $5\times10^{-12}$ s (Figs. 4–5).
* Target 6 mm diameter, 5 µm thick; tube 10 mm long, inner diameter not
  given numerically; ambient $5.0\times10^{-3}$ Pa; no-slip tube wall;
  outflow at the outlet.
* Laser (Table 1): 1064 nm, 5 ns FWHM, 10 J/cm$^2$, 2.2 mm diameter, peak
  $2.0\times10^9$ W/cm$^2$.
* No field solver; no kinetic species. Code name, language, parallelism,
  run times and the thrust computation are not stated.

# Tests and results

Key claims 5–9.

# Notation map

| Zhang et al. (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $z$, $r$, $t$ | $z$, $r$, $t$ | |
| $u$, $v$ | $u_z$, $u_r$ components of $\mathbf u_s$ | **collision**: the paper's $v$ is a fluid velocity, the registry's $\mathbf v$ the phase-space velocity |
| $n_s$, $n_e$, $T$, $T_e$ | $n_s$, $n_e$, $T$, $T_e$ | temperatures in K |
| $\rho$, $\rho_s$ | words (mass density) | not $\rho_c$ |
| $E$ | words (total energy density) | **collision** with $\mathbf E$ |
| $F$ (fluence) | words | **collision** with $F$ (thrust) |
| $I$, $I_0$ (laser intensity) | words | |
| $I_b$ (impulse bit) | $I_{\mathrm{bit}}$ | **collision** with $I_b$ (ion beam current) |
| $\eta$ (electron number fraction) | words | **collision** with $\eta$ (thrust efficiency) |
| $w$, $W$ (viscosity index) | words | **collision** with $W$ (macroparticle weight) |
| $Z$, $Z_i$ (collision-number ratio) | words | **collision** with $Z$ (charge state) |
| $\sigma$, $\sigma_s$, $\sigma_{ref}$ | words; $\sigma_{sk}$ for $\sigma_{ref}$ | electrical conductivity, surface tension, reference cross section |
| $K$, $H$, $S$ | words | thermal conductivity, enthalpy, laser source |
| $Q_s$ | words (partition function) | $Q$ is also the vector of conserved variables |
| $IP$ | words (ionization energy) | |
| $m_a$ | words (ablated mass) | |

# Pages created or updated

Chunk 1 (2026-10-14) created every page of the bundle. This source is cited on:

* [Laser-ablation plume model](/methods/laser-ablation-plume-model.md)
* [Pulsed plasma thruster](/definitions/pulsed-plasma-thruster.md)

# Citations

1. `~/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Zhang_Investigation_on_plume_expansion_and_ionization_in_a_laser_a.pdf`.
   * **Version.** Publisher's typeset version of record (Elsevier, © 2018 IAA).
   * **Identity.** doi:10.1016/j.actaastro.2018.06.045, checked on Crossref
     (title, five authors, volume, pages): Acta Astronaut. 151:432–444,
     issue 2018-10; online 2018-06-21 (printed). Received 8 Mar 2018,
     revised 17 Jun 2018, accepted 19 Jun 2018.
   * **How it was read.** Text extraction, all sections. Eq. 11 (the
     transformed heat equation) was read on the rendered page and is
     described, not transcribed; Eq. 24 was checked on rendered page 437.
     Figure values only as quoted in the text, except Fig. 3(a), read
     visually.
   * **Recorded as printed.**
     - §3.1 validates "in atmospheric conditions" against experiments that
       show a shock in ambient gas, while the model omits ambient-gas
       dynamics and §2.2 sets ambient pressure $5.0\times10^{-3}$ Pa.
     - §3.4 attributes the 6500 K side maxima at 3.5 ns to collision with
       the ambient gas, against its own "nearly vacuum" statement and §3.1.
     - Eq. 16 is written $S_p(r,x,t)$ with coordinate $z$; §3.2 sums errors
       "provided by Equation (20)", which should be Eq. 25.
     - Nomenclature $Z$, $W$, capital beta against text $Z_i$, $w$, $\beta$;
       Eq. 24 subscript $e-s$ against $e-i$ in the sum.
     - §3.4 "only primary ionization occurs in the plume" (centreline)
       against secondary and tertiary ionization near the wall.
     - About 25000 K near the wall at 100 ns (§3.4) against a maximum plume
       temperature of $147\cdot10+5816\approx7286$ K at 200 ns from the
       §3.5 fit; not reconciled.
     - §3.5 text: impulse bit 13 → 16 µN·s over 5–30 J/cm$^2$; the fit gives
       16.5 at 30 J/cm$^2$.
   * **Reference list:** 38 printed entries (Crossref reference-count 38).

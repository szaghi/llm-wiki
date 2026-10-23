---
type: Method
title: "Fluid neutral models and plasma–neutral atomic sources"
description: "Fluid treatments of atomic neutrals in MHD codes, from a single diffusive neutral density to a full neutral continuity–momentum–energy system, and the ionization, recombination, charge-exchange and radiation source terms that couple them to the plasma conservatively."
status: established
aliases: [diffusive neutral model, plasma-neutral model, Meier–Shumlak model, neutral fluid]
tags: [neutrals, edge, divertor, mhd]
timestamp: 2026-10-16T18:35:00Z
---

# Fluid neutral models and plasma–neutral atomic sources

Neutral atoms enter MHD simulations of the edge, the divertor and massive
deuterium injection. A fluid neutral model adds one or more neutral
fields and exchanges particles, momentum and energy with the plasma
through atomic reactions. The sources span three levels:
a diffusive neutral density in [JOREK](/software/jorek.md)
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.6;
[Korving et al. (2023)](/sources/korving-2023.md), §III;
[Bandaru et al. (2024)](/sources/bandaru-2024.md), Eq. 2.11); a full
neutral continuity, momentum and temperature system in
[NIMROD](/software/nimrod.md) ([Taheri et al. (2022)](/sources/taheri-2022.md),
§2); and a [kinetic Monte Carlo neutral model](/methods/kinetic-neutral-model.md)
that shares the same source terms.

## Reaction rates

With effective rate coefficients from OpenADAS (JOREK) or DEGAS2 tables
(NIMROD), the volumetric ionization and recombination rates are
$$\mathcal R_{\mathrm{ion}}=n_en_{\mathrm N}\langle\sigma v\rangle_{\mathrm{ion}}(n_e,T_e),\qquad \mathcal R_{\mathrm{rec}}=n_en_i\langle\sigma v\rangle_{\mathrm{rec}}(n_e,T_e)$$
([Korving et al. (2023)](/sources/korving-2023.md), Eq. 12;
[Taheri et al. (2022)](/sources/taheri-2022.md), Eqs. 7–8, with $n_e=n_i$).
Charge exchange adds a rate $\mathcal R_{\mathrm{cx}}$ proportional to
$\sigma_{\mathrm{cx}}n_in_{\mathrm N}$ times a mean relative speed built
from both thermal speeds and the drift $|\mathbf v-\mathbf v_{\mathrm N}|$
(Taheri et al., Eq. 9). Hydrogenic species, singly ionized, optically thin
plasma with prompt radiative loss, are common to both papers.

## Conservative three-fluid sources

[Korving et al. (2023)](/sources/korving-2023.md) (§III, Eqs. 13–18)
derive ion, electron and neutral sources that conserve particles,
momentum and energy:

- **Particles**: ions and electrons gain $\mathcal R_{\mathrm{ion}}-\mathcal R_{\mathrm{rec}}$, the neutrals the opposite.
- **Momentum**: an ionization transfers the neutral's momentum
  $m_i\mathbf v_{\mathrm N}$ to the ions; a recombination transfers the ion
  (and electron) momentum to the neutral.
- **Energy**: an ionization moves the neutral's thermal and kinetic energy
  to the ions (and the electron's share to the electrons) and costs the
  electrons the ionization energy $\varepsilon_{\mathrm{ion}}$; a
  recombination moves the ion and electron thermal and kinetic energy to
  the neutral, the rest leaving as photons.
- **Radiation**: the ADAS recombination–bremsstrahlung power coefficient
  $L_{\mathrm{PRB}}$ includes the recombination energy, so the radiated
  power is corrected to
  $P_{\mathrm{rad}}=\big(L_{\mathrm{PRB}}-\langle\sigma v\rangle_{\mathrm{rec}}\varepsilon_{\mathrm{ion}}\big)n_en_i$
  (Eq. 18).

Reduced to JOREK's assumptions ($\rho=m_in_i$, $m_e\to0$, $m_{\mathrm N}=m_i$,
$n_e=n_i$, one temperature $T=T_e+T_i$) these become the two-fluid sources of
Eqs. 19–21, written in JOREK's non-conservative "JOREK form", in which
terms in $(\mathbf v_{\mathrm N}-\mathbf v)^2$ appear. The authors state
that those terms "purely arise due to the JOREK form" (Appendix). The
printed electron-energy line of Eq. 21 makes the radiation a heating
rather than a loss, contradicting Eq. 18 and the text; the Source page
records the sign slip.

## Diffusive neutral density (JOREK)

The JOREK fluid neutral model (Fil et al. 2015, adopted unchanged) adds one
variable, the neutral mass density $\rho_{\mathrm N}$, with constant
isotropic diffusion and no momentum equation
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.6;
[Korving et al. (2023)](/sources/korving-2023.md), §III;
[Bandaru et al. (2024)](/sources/bandaru-2024.md), Eq. 2.11):
$$\partial_t\rho_{\mathrm N}=\nabla\cdot\big(D_{\mathrm N}\nabla\rho_{\mathrm N}\big)-m_i\mathcal R_{\mathrm{ion}}+m_i\mathcal R_{\mathrm{rec}},$$
with the opposite terms in the plasma density equation. In the RE study of
Bandaru et al. the electron density in these rates includes the
impurity electrons ([coronal-equilibrium model](/methods/coronal-equilibrium-impurity-model.md)),
and deuterium line and continuum radiation enter the pressure equation
(Eq. 2.8). Recycling boundary conditions were added recently
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.6). In 2021 the full
MHD model had no neutrals (§2.12).

**Performance of the diffusive model.**
- Against SOLPS on a MAST-U Super-X case, JOREK obtains a target-flux
  roll-over that is less steep than SOLPS, because charge exchange is
  missing ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.6).
- On the ITER PFPO-1 fuelling scan, with $D_{\mathrm N}\approx2\times10^2$
  m²/s tuned to the SOLPS-ITER neutral decay length, the model gives the
  right power ranges and the transition from sheath-limited to
  conduction-limited regime, but is "not sufficient to provide the correct
  plasma mechanics"; JOREK's upstream density is lower than SOLPS-ITER's
  at a given fuelling rate ([Korving et al. (2023)](/sources/korving-2023.md),
  §V B, Fig. 3). This motivated the
  [kinetic neutral model](/methods/kinetic-neutral-model.md).
- In a deuterium-dominated ITER injection, a neutral front moves inward
  from the boundary and flattens $T_e$ step by step
  ([Bandaru et al. (2024)](/sources/bandaru-2024.md), §III.B, Fig. 2b).

**Neutral sources as ablation clouds.** [Kong et al. (2025)](/sources/kong-2025.md)
(§2) use JOREK reduced MHD with parallel flow and the fluid-neutral
extension as a stand-in for a pellet ablation cloud.

- **Source.** A transient Gaussian D$_2$ neutral source of 0.05 μs sits on
  the low-field-side midplane of a JET H-mode, with rates of
  $2\times10^{26}$ to $10^{28}$ atoms/s, i.e. $10^{19}$ to $5\times10^{20}$
  atoms. The default half-$e^{-1}$ widths are 0.5 rad toroidally and 4 cm
  poloidally and radially.
- **Assimilation.** The neutrals ionize within about 0.1–0.2 μs, and the
  plasmoid $T_e$ re-equilibrates to about 3.3 keV for rates up to
  $1.4\times10^{27}$ atoms/s. At $10^{28}$ atoms/s it drops to about 1 keV by
  dilution cooling.
- **Use.** The resulting high-pressure plasmoid is the object of the
  [plasmoid-drift](/definitions/plasmoid-drift.md) study.
- **Kinetic option.** Kinetic full-$f$ neutrals are available in JOREK but
  were not used.

In the SPI studies with the CR impurity model, background-species
(hydrogenic) neutrals are ionized instantly, so no neutral field is evolved
([Hu et al. (2023)](/sources/hu-2023.md), §2.1).

## Full neutral fluid (NIMROD, Meier–Shumlak model)

[Taheri et al. (2022)](/sources/taheri-2022.md) (§2, Eqs. 1–15) evolve
neutral density, velocity and temperature alongside resistive MHD:
$$\partial_tn_i+\nabla\cdot(n_i\mathbf v)=\mathcal R_{\mathrm{ion}}-\mathcal R_{\mathrm{rec}},\qquad \partial_tn_{\mathrm N}+\nabla\cdot(n_{\mathrm N}\mathbf v_{\mathrm N})=\mathcal R_{\mathrm{rec}}-\mathcal R_{\mathrm{ion}}.$$
The momentum equations exchange $m_i(\mathcal R_{\mathrm{ion}}+\mathcal R_{\mathrm{cx}})(\mathbf v_{\mathrm N}-\mathbf v)$
(plasma side) and $m_i(\mathcal R_{\mathrm{rec}}+\mathcal R_{\mathrm{cx}})(\mathbf v-\mathbf v_{\mathrm N})$
(neutral side), plus charge-exchange friction forces; the temperature
equations carry ionization and recombination heat exchange, the
ionization energy loss $\mathcal R_{\mathrm{ion}}\varepsilon_{\mathrm{ion}}$,
charge-exchange heat exchange and frictional heating in
$|\mathbf v-\mathbf v_{\mathrm N}|^2$. Viscosity and heat flux are
isotropic for both species; neutral–ion elastic scattering is neglected,
which the authors justify for plasmas ionized by a few percent or more.
The 0D tests drop $\varepsilon_{\mathrm{ion}}$ so that energy is conserved.

The temperature-dependent cross sections make the density advance depend
on $T$, which breaks the data-dependency order that the
[semi-implicit leapfrog](/methods/semi-implicit-leapfrog.md) relies on;
the treatment of that coupling (Crank–Nicolson, JFNK and Strang-split
variants) is on
[operator splitting of atomic sources](/methods/operator-splitting-of-atomic-sources.md).

# Citations

- [Korving et al. (2023)](/sources/korving-2023.md) — §III, Eqs. 12–21, Appendix; §V B.
- [Taheri et al. (2022)](/sources/taheri-2022.md) — §2, Eqs. 1–17; §3.
- [Bandaru et al. (2024)](/sources/bandaru-2024.md) — §II, Eqs. 2.7–2.11; §III.B.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §2.6, §2.12, §4.6.
- [Kong et al. (2025)](/sources/kong-2025.md) — §2, §3.1.
- [Hu et al. (2023)](/sources/hu-2023.md) — §2.1.

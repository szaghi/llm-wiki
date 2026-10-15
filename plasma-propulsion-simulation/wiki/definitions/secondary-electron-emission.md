---
type: Definition
title: "Secondary electron emission and sheath regimes"
description: "Electron-induced emission from dielectric thruster walls and its effect on the sheath: yield models (linear, Vaughan, Furman–Pivi), the classical sheath drop and its collapse at the space-charge-saturation yield (about 0.983 for xenon), Bohm-criterion and anode-sheath conditions, and the kinetic effects (distribution depletion, sheath oscillations, SEE bursts) that fluid sheath models miss."
status: established
aliases: [SEE, secondary electron emission, electron emission yield, EEY, space-charge saturation, SCS, space-charge-limited sheath, SCL sheath, charge-saturation limit, Bohm criterion, anode sheath]
tags: [sheath, wall-interaction, hall-thruster, pic, fluid, kinetic, numerics]
timestamp: 2026-10-15T00:00:00Z
---

# Secondary electron emission and sheath regimes

Electrons that strike the dielectric channel walls of a Hall thruster release
secondary electrons. Their yield $\delta_{\mathrm{SEE}}$ (emitted per
incident electron) sets the sheath potential drop, the wall energy loss and
part of the cross-field transport ([near-wall conductivity](/definitions/near-wall-conductivity.md)).
Because the electron–material time scale is about $10^{-13}$ s, codes model
emission phenomenologically and instantaneously
([Taccogna et al. (2023)](/sources/taccogna-2023.md), §III C b;
[Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), App. 1, which
gives $10^{-13}$–$10^{-14}$ s).

## Yield models

* **General form.** The yield depends on the impact energy and angle; the
  emission energy and angle spectra complete the model. Families in use:
  linear and power law, modified power law, modified Vaughan, Sombrin,
  Furman–Pivi and machine-learning fits
  ([Taccogna et al. (2023)](/sources/taccogna-2023.md), §III C b). For Hall
  thrusters (impact energies below 1 keV) only the zero-energy yield and the
  first crossover energy, where the yield reaches 1, matter
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), App. 1).
* **Linear law.** The yield rises linearly from its zero-energy value to 1 at
  the first crossover energy, with secondaries emitted half-Maxwellian at
  2 eV ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), eq. 37).
  [Troyetsky et al. (2026)](/sources/troyetsky-2026.md) use a linear law
  through zero, yield = impact energy / 51.1 eV for BN, with secondaries
  half-Maxwellian at 2 eV. Its 51.1 eV differs from the 45 eV BN crossover of Taccogna & Garrigues' Tab. III (below); both are model inputs from different references, not competing measurements (compiler note). [Reza et al. (2022)](/sources/reza-2022.md)
  (§4.2, eq. 10) use a linear BN model with parameters 0.578, 2.9 (maximum
  yield) and 35.04 eV, secondaries at 1 eV; the equation is printed with
  $\max$ where a cap needs $\min$.
  [Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md) (Table 2) use a
  linear model after Croes with Maxwellian emission at 1.0 eV and an electron
  reflection yield of 0.5.
* **Measured parameters.** Zero-energy yield and first crossover energy
  (Taccogna & Garrigues 2019, Tab. III, attributed to Barral, Dunaevsky,
  Tondu and Villemant): Al$_2$O$_3$ 0.57, 22 eV; BN 0.24, 45 eV; SiO$_2$ 0.5,
  18 eV; BN-SiO$_2$ 0.54, 40 eV; SiC 0.69, 43 eV. Taccogna et al. (2023,
  Fig. 6, after Tondu et al. 2011) show the same crossovers for Al$_2$O$_3$
  (22 eV), BN-SiO$_2$ (40 eV) and BN (45 eV).
* **Data gap at low energy.** Yield data are lacking below 30 eV, where most
  primaries hit after the sheath decelerates them. The best measurements and
  theory suggest a zero-energy yield above 0.3–0.4 and a yield that rises again
  below 10 eV for common thruster dielectrics, which linear, power or Vaughan
  laws do not reproduce ([Taccogna et al. (2023)](/sources/taccogna-2023.md),
  §III C b). The BN zero-energy value of a linear fit, 0.24 (above), lies
  below that range; the fit parameter and the measured zero-energy yield are
  not the same quantity.
* **Angular emission.** True secondaries follow a cosine (Lambertian) law;
  elastically backscattered electrons show a double-lobe emission and keep a
  memory of the impact energy and angle
  ([Taccogna et al. (2023)](/sources/taccogna-2023.md), §III C b, Fig. 7).
* **Vaughan and Furman–Pivi.** Taccogna & Garrigues (2019, App. 1, eqs.
  38–41, Tab. IV) give a modified Vaughan model with BN parameters and the
  Furman–Pivi model with 42 free parameters. Reza et al. (2022, §4.1) verified
  a Monte Carlo Vaughan model on the Sydorenko mini-benchmark and their wall
  module on the Schwager–Birdsall collector sheath (stated, not shown).
* **Two-parameter fluid model.** Ahedo (2023, Appendix) uses an elastically
  reflected fraction and a true-SEE yield, a simplified version of the
  complete models of kinetic codes.

## Classical sheath and space-charge saturation

For a floating dielectric wall (zero net current),
$$\Delta\phi_{\mathrm{sh}}=\frac{T_e}{e}\ln\left[(1-\delta_{\mathrm{SEE}})\sqrt{\frac{m_i}{2\pi m_e}}\right],$$
valid for $\delta_{\mathrm{SEE}}<1$
([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), eqs. 26–27, after
Barral et al. 2003; the same expression in
[Giannetti et al. (2021)](/sources/giannetti-2021.md), eq. A7, and
[Reza et al. (2022)](/sources/reza-2022.md), eq. 9). Ahedo's form adds the
logarithms of the non-reflected fraction and of a tail-replenishment factor;
the argument of the first logarithm, $\sqrt{m_i/(2\pi m_e)}$, is about 200
for xenon
([Ahedo (2023)](/sources/ahedo-2023.md), eq. 75).

**Space-charge saturation.** Saturation sets in at
$$\delta^*_{\mathrm{SEE}}=1-8.3\sqrt{\frac{m_e}{m_i}}\approx0.983\ \text{(Xe)},$$
where the drop has fallen to about $T_e/e$
([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.3, after Hobbs
& Wesson 1967). The xenon value 0.983 is the cap of the BN-SiO$_2$ yield
in [Giannetti et al. (2021)](/sources/giannetti-2021.md) (eq. A2, after
Goebel & Katz) and the threshold above which a 1D radial PIC sheath becomes
saturated, with a near-flat potential and a sharp electron-density rise at
the wall ([Reza et al. (2022)](/sources/reza-2022.md), §4.1, Fig. 7: yields
0.5–0.99, steady after about 2 µs). Ahedo (2023, Appendix) states that this
charge-saturation limit "is very unstable numerically" because its potential
fall is very sensitive to the distributions, and that the Hobbs–Wesson result
holds only for a fully replenished semi-Maxwellian distribution.

**Discharge regimes.** Taccogna & Garrigues (2019, §2.6, Fig. 6) report SPT-100
current–voltage curves for three wall materials (Gascon et al. 2003,
experiment; Barral et al. 2003, 1D fluid): the transition from the
low-voltage oscillating regime to the nominal one is attributed to the yield
reaching saturation at the first crossover energy, and calculations with SEE
as the only anomalous mechanism underestimate the discharge current.

## Fluid wall models

* **Wall terms.** In the 1D model of
  [Giannetti et al. (2021)](/sources/giannetti-2021.md) (App. A), the ion wall
  loss frequency is a Bohm flux over the channel width; the electron–wall
  collision frequency is that frequency divided by $1-\delta_{\mathrm{SEE}}$;
  the wall power loss per electron is that frequency times
  $2T_e+(1-\delta_{\mathrm{SEE}})e\Delta\phi_{\mathrm{sh}}$; secondaries
  thermalize and their emission energy is neglected; every wall term is scaled
  by a calibrated factor 0.115. Taccogna & Garrigues (2019, eqs. 28–29) give
  the electron–wall momentum frequency with $\delta_{\mathrm{SEE}}/(1-\delta_{\mathrm{SEE}})$
  in place of $1/(1-\delta_{\mathrm{SEE}})$. The two are different model forms
  of the wall collisionality, adopted from different references; see
  [near-wall conductivity](/definitions/near-wall-conductivity.md).
* **Energy flux.** The energy flux to the wall is the primary flux times
  $2T_e$ (Maxwellian; 1.4–2 times $T_e$ in a kinetic model) plus the azimuthal
  kinetic energy, minus the emitted energy; adding the sheath work gives the
  boundary condition of the bulk, with a nonzero heat flux at the sheath edge
  ([Ahedo (2023)](/sources/ahedo-2023.md), eqs. 77–78).
* **Empirical alternative.** Earlier models used a wall energy-loss rate
  equal to a coefficient times a reference frequency times the mean electron
  energy times $\exp(-20\ \mathrm{eV}/\text{mean energy})$, compared with the SEE and
  saturation theory for $10^7$ s$^{-1}$ and coefficient 0.7
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), eq. 30, Fig. 3,
  after Garrigues et al. 2006). The ad-hoc wall-collision model of Hagelaar et
  al. 2002 (wall frequency 0.1 times about $10^7$ s$^{-1}$, energy loss on the same 20 eV scale, run as a fictitious MCC event) is the comparison case of
  [Reza et al. (2022)](/sources/reza-2022.md) (§5.1, eqs. 14–15).
* **Overestimate.** Fluid sheath models "tend to overestimate the wall
  losses" (Sydorenko et al. 2006; Kaganovich et al. 2007), which Giannetti et
  al. (§4) give as one reason the calibrated wall factor is small; a loss-cone
  analysis shows fluid models overestimate wall potential and loss frequencies
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.2, after
  Kaganovich 2007).

## Kinetic effects

* **Distribution depletion.** At low collisionality the electron distribution
  along $\mathbf B$ is depleted of fast electrons, which lowers the particle and
  energy fluxes to the wall against Maxwellian values and the weight of
  near-wall conductivity; field inclination to the wall reduces the effect
  ([Taccogna et al. (2023)](/sources/taccogna-2023.md), §III C a). Boltzmann
  solvers find wall-loss frequencies far below Maxwellian predictions and no
  saturation ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.1,
  after Latocha 2002 and Meezan & Cappelli 2002). In a 1D radial PIC solution
  the replenishment factor is 0.05–0.20 for $\mathbf B$ normal to the wall and
  much larger for curved $\mathbf B$
  ([Ahedo (2023)](/sources/ahedo-2023.md), eq. 46, ref. 61).
* **Sheath oscillations.** 1D radial PIC shows that the SEE beam limits $T_e$
  and carries most of the wall current, and that the sheath switches between
  saturated and non-saturated states (relaxation sheath oscillations, Sydorenko
  et al. 2009); sheath instability and inverse sheaths appear when emission
  driven by the opposite wall's beam exceeds 1 (Campanell et al.)
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.2, Fig. 14).
* **Coupling to azimuthal instabilities.** In 2D radial–azimuthal PIC the
  bulk anomalous mobility falls by 20 % as emission rises while the near-wall
  mobility doubles, so total mobility stays about constant; three SEE regimes
  appear (monotonic stable, oscillatory, space-charge-limited stable)
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.4, after
  Tavant 2018 and Taccogna 2019). In a pseudo-2D radial–azimuthal run the
  [electron drift instability](/definitions/electron-drift-instability.md)
  heats electrons until the yield passes saturation at about 1 µs; bursts of
  near-wall electrons at about 4 µs and 7 µs quench the bulk $T_e$, and the
  sheath settles saturated with a yield slightly above 1, while a 1D radial run
  stays stable ([Reza et al. (2022)](/sources/reza-2022.md), §4.3.1; see
  [reduced-order PIC](/methods/reduced-order-pic.md)).
* **Fluid against PIC.** On a shared 2D axial–radial set-up, PIC-MCC develops
  a space-charge-limited sheath with trapped secondaries near $z\approx2.1$ cm
  (axial position),
  while the five-moment fluid model, with yields of 0.92–0.983 there, does not.
  Possible causes given: suppression by the energy-limited kinetic flux wall
  condition, the different power, and instant thermalization of secondaries,
  which prevents saturation until the yield is about 1.0
  ([Troyetsky et al. (2026)](/sources/troyetsky-2026.md), Fig. 9; see
  [five-moment electron fluid model](/methods/five-moment-fluid-model.md)).
  Without that wall condition the fluid model "eventually faced runaway
  electron emission" (p. 21).

## Bohm criterion and the sheath edge

* A quasi-neutral model does not automatically satisfy the Bohm criterion,
  and grid spacing affects the presheath gradients; the remedies are imposing
  the Bohm speed as a fluid boundary condition or a forcing method for PIC ions
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.3;
  [Ahedo (2023)](/sources/ahedo-2023.md), Appendix).
* In a 1D radial PIC solution the sheath edges, placed where the
  non-neutrality reaches 2 %, coincide with radial ion Mach number about 1,
  which supports the two-scale picture of a quasi-neutral bulk plus thin
  sheaths ([Ahedo (2023)](/sources/ahedo-2023.md), Fig. 4).
* In 1D axial fluid models ions enter the anode sheath at or above the ion
  sound speed ([Giannetti et al. (2021)](/sources/giannetti-2021.md), §2.4);
  [Saravia et al. (2026)](/sources/saravia-2026.md) (eq. 10) state that the
  Bohm conditions are superfluous there because the ion characteristics always
  point outward.

## Anode sheath

* In 1D fluid models the anode sheath drop is set so that the random thermal
  electron current, reduced by the Boltzmann factor, equals the anode electron
  current (no drop when the latter exceeds the former), and the energy carried
  to the anode is the electron flux times $2T_e$ plus the
  sheath drop ([Giannetti et al. (2021)](/sources/giannetti-2021.md), eqs.
  20–21; [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.3).
  [Saravia et al. (2026)](/sources/saravia-2026.md) (§2.2) neglect it.
* Normal (electron-repelling) and inverse sheaths are joined by a generalized
  Bohm criterion, electron plus ion momentum flux equal to $T_e+T_i$; the
  transition occurs when the ion-to-electron current ratio times
  $\sqrt{m_i/m_e}$ equals $\sqrt{T_i/T_e}$
  ([Ahedo (2023)](/sources/ahedo-2023.md), Appendix, ref. 51).
* In pseudo-2D PIC runs of an oxygen-fed Hall thruster the anode sheath drop
  is 20–50 V, about 3–4 times the local $T_e$, decreasing with anode mass flow
  ([Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md), §Water electrolysis
  (oxygen)). A single-region
  pseudo-2D axial–radial PIC run produces an "unrealistic anode sheath with
  high potential drop", attributed to radial wall physics driven by axially
  averaged bulk conditions ([Reza et al. (2022)](/sources/reza-2022.md),
  §5.2).

# Citations

1. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §§2.3, 2.6, 3.1, 3.2, 3.4, eqs. 26–30, 37–41, Tabs. III–IV, Figs. 3, 6, 14, App. 1.
2. [Taccogna et al. (2023)](/sources/taccogna-2023.md), §III C a–b, Figs. 6–7.
3. [Reza et al. (2022)](/sources/reza-2022.md), §§4.1, 4.2, 4.3.1, 5.2, eqs. 9–10, 14–15, Fig. 7.
4. [Giannetti et al. (2021)](/sources/giannetti-2021.md), §§2.4, 4, eqs. 20–21, App. A.
5. [Ahedo (2023)](/sources/ahedo-2023.md), Appendix, eqs. 46, 73–78, Fig. 4.
6. [Troyetsky et al. (2026)](/sources/troyetsky-2026.md), §Simulation setup, Fig. 9, p. 21.
7. [Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md), Table 2, §Water electrolysis (oxygen).
8. [Saravia et al. (2026)](/sources/saravia-2026.md), §2.2, eq. 10.

---
type: Definition
title: "Anomalous electron cross-field transport"
description: "Electron transport across the magnetic field of a Hall thruster in excess of classical collisional mobility, attributed to azimuthal instabilities and wall effects, resolved self-consistently by kinetic models and closed in fluid and hybrid models by Bohm-type collision frequencies whose fitted coefficients span 0.01 to 7.5 in the convention nu_ano = alpha_B omega_ce / 16."
status: established
aliases: [anomalous electron transport, anomalous electron mobility, anomalous collision frequency, Bohm-type transport, anomalous collisionality, turbulent collision frequency]
tags: [anomalous-transport, hall-thruster, instability, fluid, hybrid, pic, calibration]
timestamp: 2026-10-15T00:00:00Z
---

# Anomalous electron cross-field transport

In a [Hall-effect thruster](/definitions/hall-effect-thruster.md) the
electrons must cross the radial magnetic field to reach the anode. The
electron current that crosses it is larger than the classical
[cross-field mobility](/definitions/electron-mobility-and-hall-parameter.md)
built from electron–neutral collisions predicts. This excess is called
anomalous transport. Fluid and hybrid models must supply it through an
extra term. Kinetic models can resolve it.

## The phenomenon

* The measured electron current exceeds the classical electron–atom
  collisional mobility. In 2005 the two candidate explanations were
  [near-wall conductivity](/definitions/near-wall-conductivity.md) and
  Bohm-type mobility from oscillations or turbulence, and "no general
  mobility model has yet been formulated"
  ([Boyd (2005)](/sources/boyd-2005.md), §3.4). In a 2D hybrid model of
  the P5 thruster (Koo & Boyd), the measured centreline potential lies
  between the profile computed with wall-collision mobility, which drops
  too far upstream, and the profile computed with Bohm mobility, which
  drops too far downstream (Fig. 16). Boyd bounds the accuracy of fluid
  and hybrid Hall-thruster performance predictions at about 10% because
  of this uncertainty (§3.4) and at 10–20% overall (§4).
* Taccogna & Garrigues (2019, §2.4) report, citing Janes & Lowder (1966),
  that an azimuthal field fluctuation correlated with the density
  fluctuation gives an axial drift through $E_\theta\times B_r$, a constant
  Hall parameter and a collision frequency proportional to $\omega_{ce}$;
  classical Bohm transport corresponds to $\alpha_{\mathrm B}=1$
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.4). They
  report, citing Ahedo et al. (2003), that near-wall conductivity alone
  cannot explain the anomalous transport, and that local comparisons of
  $n_e$, $T_e$ and ion velocity expose the limits of fitted models even when
  mechanisms are combined.
* The 2017 Plasma Roadmap states, citing Lafleur, Baalrud & Chabert
  (2016) and Tsikata et al. (2014), that anomalous transport in
  $\mathbf E\times\mathbf B$ discharges may be associated with fluctuations
  amplified by the differential flow between electrons and ions or between
  ion populations, and, citing Campanell & Umansky (2016), by the drift
  between wall-emitted secondary electrons and plasma electrons
  ([Adamovich et al. (2017)](/sources/adamovich-2017.md), §16). It names
  "electron transport, turbulence and confinement in magnetized
  discharges" the research priority of electric propulsion (§12).

## Instability-driven transport resolved by kinetic models

* In 2D axial–azimuthal PIC-MCC of the
  [benchmark configuration](/benchmarks/axial-azimuthal-pic-benchmark.md),
  the azimuthal electron–ion friction force produced by the
  [electron drift instability](/definitions/electron-drift-instability.md)
  is the main contributor to axial electron transport in all seven
  collisionless cases, "even in the absence of electron-wall or
  electron-neutral collisions"
  ([Charoy et al. (2020)](/sources/charoy-2020.md), §III A, Figs. 5a, 6).
  The force and its quasi-linear closure are on
  [Instability-enhanced electron–ion friction](/results/instability-enhanced-friction-force.md).
* A single-region [reduced-order PIC](/methods/reduced-order-pic.md) in the
  axial–azimuthal plane reproduces the time-averaged 2D benchmark profiles
  without an anomalous collision term. A 1D axial PIC without anomalous
  collisions cannot sustain the potential, which collapses to about 30 V by
  $z\approx0.5$ cm from the anode (read off Fig. 3c)
  ([Reza et al. (2022)](/sources/reza-2022.md), §3.2, Fig. 3). In the
  plume, downstream of the magnetic-field peak, nearly all transport comes
  from the electric (wave) force (Fig. 6).
* In GPU PIC runs of the same benchmark, coarser semi-implicit runs lose
  40% (4× coarsening) and 70% (8×) of the peak azimuthal field while the
  time-averaged axial field stays consistent. The authors suggest, as a
  hypothesis, that the transport magnitude is "relatively insensitive to
  some of the spectral characteristics of the azimuthal instability"
  ([Marks & Gorodetsky (2025)](/sources/marks-2025.md), "Plasma
  instabilities", Figs. 11–13).
* In 2D radial–azimuthal PIC, Taccogna & Garrigues (2019, §3.4) report,
  citing Tavant (2018) and Taccogna (2019), that bulk anomalous mobility
  falls by 20% as secondary emission rises while near-wall mobility
  doubles, so that the total mobility stays about constant. They report
  that 1D azimuthal PIC with a fixed axial field gives a mobility about
  ten times larger than in real thrusters.
* A 2D axial–azimuthal PIC-MCC of an SPT-100-like thruster gives a mean
  electron axial velocity of $-6328.4\pm2346.6$ m/s in argon against
  $-3488.2\pm1592.9$ m/s in xenon, with lower normalized
  [spectral entropy](/methods/spectral-entropy.md) of $E_\theta$ for argon.
  The authors conjecture "a link between ordered patterns due to the
  presence of plasma waves and an increase of anomalous transport, which
  must be verified carefully"
  ([Miranda et al. (2026)](/sources/miranda-2026.md), §3 Table 1, §4).
  The runs are start-up transients without a steady state.
* With the same anomalous collision profile, cross sections and Poisson
  solver, a 2D axial–radial [five-moment fluid model](/methods/five-moment-fluid-model.md)
  gives a discharge current of 10.1 A against 14.7 A for PIC-MCC. In the
  PIC-MCC run the axial momentum structure "correlates most closely" with
  the radial gradient of the off-diagonal electron pressure component,
  $\partial\mathsf P_{e,r\theta}/\partial r$, which the fluid model lacks;
  the authors name this anisotropic pressure, together with
  space-charge-limited sheath kinetics, as the probable cause of the gap,
  and note that numerical diffusion in the fluid model could enhance its
  cross-field transport ([Troyetsky et al. (2026)](/sources/troyetsky-2026.md), "Results:
  Model comparison", p. 16, Figs. 4, 10–11). The cross-field current of a model
  therefore depends on more than its collision-frequency closure (compiler
  note).

## Bohm-type closures in fluid and hybrid models

Fluid and hybrid models add an anomalous collision frequency
$\nu_{\mathrm{ano}}$ to the electron momentum-transfer frequency $\nu_e$. The
Bohm-type form is $\nu_{\mathrm{ano}}=\alpha_{\mathrm B}\,\omega_{ce}/16$, with
$\alpha_{\mathrm B}$ constant or piecewise constant in $z$. Taccogna &
Garrigues (2019, §2.4, Tab. II) list, after Jorns (2018), five forms in
use: near-wall conductivity $\propto c_s$ (Barral et al. 2003), Bohm-like
$\propto\omega_{ce}$ (Fife 1998), a shear-flow-reduced Bohm form (Scharfe et
al. 2008), a "small-scale turbulence" form $\propto\omega_{ce}$ times the
square of the ratio of electron drift speed to $c_s$ (Cappelli et al. 2015)
and a wave-trapping form (Lafleur et al. 2016, 2017).

Coefficients by source, converted to $\alpha_{\mathrm B}$:

| Source | Profile, in words | $\alpha_{\mathrm B}$ |
|---|---|---|
| [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.4 | uniform coefficient fitted in hybrid models (attr. Hagelaar 2002, Ahedo 2003, Koo & Boyd 2004) | $\sim0.16$ |
| [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.3, Fig. 15 | axially dependent coefficient in 2D r–z PIC; the classical Bohm limit for reference | 1 (Bohm limit); fitted 0.032–0.32 |
| [Charoy et al. (2020)](/sources/charoy-2020.md), §IV A–B, Eqs. 7–9, Fig. 7 | two zones fitted to the PIC friction force: Bohm-type outside the channel; inside, a wall-collision-like term, a fixed fraction (0.4) of a reference frequency of $10^7$ s⁻¹ | 0.17 (outside) |
| [Giannetti et al. (2021)](/sources/giannetti-2021.md), eq. 11, §4 | two levels, channel and plume, with a smooth transition | 0.075 (channel); 7.5 (plume) |
| [Reza et al. (2022)](/sources/reza-2022.md), §3.1 | three-zone step: $0<z\le0.5$ cm, $0.5<z\le1.2$ cm, $1.2<z\le2.5$ cm | 0.5; 0.053; 1.6 |
| [Reza et al. (2022)](/sources/reza-2022.md), §5.1, Table 3 | two-zone step, channel / plume (after Panelli et al. 2021) | 0.035; 5.0 |
| [Ahedo (2023)](/sources/ahedo-2023.md), Eq. 18, Fig. 4 | fitted function of $z$ in Hall thrusters, constant in electrodeless thrusters; no fitted values given | 0.16 for the turbulence level reported from 1D radial PIC |
| [Eckels et al. (2024)](/sources/eckels-2024.md), Eq. 5, Table 3 | two-zone step, inside / outside the channel, with a pressure-shifted transition (Eq. 6); outside value a multiple of the inside one | 0.109 (inside, posterior median); 1.59 (outside, product of the two medians, computed) |
| [Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md), Eq. 7, Table 1 | uniform | 0.01 |
| [Troyetsky et al. (2026)](/sources/troyetsky-2026.md), Eq. 8 | two-zone step with a linear ramp: inside for $z<2.25$ cm, plume for $z\ge2.75$ cm | 0.16; 4.0 |
| [Saravia et al. (2026)](/sources/saravia-2026.md), Eqs. 7, 21, Table 1 | two levels, channel / plume, joined by error functions | reference 0.1 (in); 1.0 (out) |

The conversions are the compiler's: a source coefficient that multiplies
$\omega_{ce}$ directly is multiplied by 16, and one that divides
$\omega_{ce}$ is inverted and multiplied by 16. Each source's printed form,
values and conversion are on its Source page (`# Notation map`). In every multi-zone profile above, the in-channel
coefficient is smaller than the plume coefficient. Ahedo (2023, §3D)
reports "a certain consensus" (attributed to his refs. 31–34) that
$\alpha_{\mathrm B}(z)$ is smaller inside the channel than in the near
plume, with a minimum near the maximum of $E_z$. Plume values exceed the
classical Bohm level $\alpha_{\mathrm B}=1$ in Giannetti et al. (7.5), Reza
et al. (1.6 and 5.0), Eckels et al. (1.59) and Troyetsky et al. (4.0);
Saravia et al.'s reference value equals it. Giannetti et al. (2021, §4) state that their
calibrated $\nu_{\mathrm{ano}}(z)$ is close to profiles calibrated on
experiments by other authors.

**Implementation.** In particle codes the term is a fictitious collision:
an elastic, isotropic electron scattering without energy loss
([Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md), Eq. 7;
[Reza et al. (2022)](/sources/reza-2022.md), §3.1;
[Troyetsky et al. (2026)](/sources/troyetsky-2026.md), PIC-MCC model),
which "only scatters velocity" in the 2D r–z PIC models reviewed by
Taccogna & Garrigues (2019, §3.3). In the fluid models it enters $\nu_e$
and hence the mobility
([Giannetti et al. (2021)](/sources/giannetti-2021.md), eq. 10;
[Saravia et al. (2026)](/sources/saravia-2026.md), eq. 6). Ahedo (2023,
Eqs. 18–21) writes the closure as an anomalous force parallel to the
electron current and states that "there is no evidence supporting" the
isotropic-turbulence assumption behind it; he proposes an alternative that
acts only on the azimuthal momentum and heat-flux equations (Eq. 26) and
adds no anomalous parallel transport.

**Sensitivity and identifiability.**
* With 2D r–z PIC and a fitted coefficient, global performance is predicted
  within 20% in thrust and discharge current
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.3). Tuning
  anomalous coefficients to match erosion does not guarantee matching
  current or performance (§2.7, attributed to Cheng & Martinez-Sanchez).
* In a calibrated [1D fluid model](/methods/one-dimensional-fluid-hall-model.md),
  the in-channel coefficient strongly affects the mean discharge current
  and the oscillation amplitude, and the steepness of the channel-to-plume
  transition matters significantly
  ([Giannetti et al. (2021)](/sources/giannetti-2021.md), §4).
* In a uniform-coefficient PIC, $\alpha_{\mathrm B}=0.01$ sustains the
  plasma and values ten times larger extinguish it because the electrons
  become too demagnetized (stated, no figure)
  ([Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md), "PlasmaSim 2D").
* The in-channel and plume coefficients dominate the Sobol' variance of
  thrust and exit ion velocity, with a total index above 0.8 for the
  in-channel coefficient on exit ion velocity; the shifted-transition
  parameters contribute little, which the authors read as
  over-parameterization. After [Bayesian calibration](/methods/bayesian-calibration.md)
  the discharge current is still over-predicted by more than 50%, and the
  authors suspect that a three-zone profile would fix it (not shown)
  ([Eckels et al. (2024)](/sources/eckels-2024.md), Obs. 4, Fig. 12).
* On synthetic data from a LANDMARK test case 3 run of a
  [1D fluid Hall model](/methods/one-dimensional-fluid-hall-model.md), calibrating on the discharge-current signal alone recovers the
  in-channel coefficient but not the plume coefficient
  ($3.50^{+1.74}_{-1.68}$ against 1.0); adding thrust and plume $T_e$
  gives $1.57^{+1.78}_{-0.67}$
  ([Saravia et al. (2026)](/sources/saravia-2026.md), §6.2, Table 5).
* Coefficients tuned with an accelerated 1D PIC (ion mass reduced 100×,
  $f_\varepsilon=20$) reproduce the 2D profiles when reused in a real-scale
  run, while the accelerated run itself shows "clear discrepancies"
  ([Reza et al. (2022)](/sources/reza-2022.md), §3.2, Fig. 4); see
  [PIC acceleration scaling](/methods/pic-acceleration-scaling.md).

**Time dependence.** Giannetti et al. (2021, §4–5) argue that the
coefficient should be a function of $z$ and $t$, and report that Dale &
Jorns measured it varying strongly over the
[breathing](/definitions/breathing-mode.md) cycle. Troyetsky et al. (2026,
Eq. 8) state that their step profile "is not representative" of
experimentally inferred distributions and report that Petronio et al.
suggest an anisotropic anomalous force.

## Self-consistent and data-driven closures

* Taccogna & Garrigues (2019, §2.4) report a self-consistent route: a 1D
  wave-energy equation with growth rates from linear kinetic theory gives
  $\nu_{\mathrm{ano}}$ (attributed to Mikellides et al. 2016, Reza et al.
  2017, Lafleur et al. 2018), with a growth rate sensitive to the assumed
  electron energy distribution. A quasi-linear friction closure tested
  against PIC is on
  [Instability-enhanced electron–ion friction](/results/instability-enhanced-friction-force.md);
  Charoy et al. (2020, Conclusion) conclude that a self-consistent fluid closure
  remains out of reach because the force depends on the strongly
  non-Maxwellian electron distribution.
* Data-driven route (Taccogna & Garrigues 2019, §2.4, §2.5): the electric
  field is obtained from moments of ion distributions measured by
  laser-induced fluorescence and $\nu_{\mathrm{ano}}$ is fitted to
  measurements. In a 2D hybrid model, adjusting the $\mu_\perp$ profile to
  the measured ion velocity shortens the acceleration region and moves
  ionization downstream (Fig. 5, attributed to Garrigues et al. 2009).
* Machine-learned closure: both reviews report the genetic-algorithm or
  machine-learning fit of Jorns (2018) as a Bohm form with a spatially
  varying coefficient, but they print different forms (see
  Contradictions):
  [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.4, give
  $\nu_{\mathrm{ano}}\propto\omega_{ce}\,c_s^2/u_{e,\theta}^2$, and
  [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. V D, Eq. 22,
  give $\nu_{\mathrm{ano}}\propto\omega_{ce}\,u_i^2/u_{e,\theta}^2$, with
  $u_{e,\theta}$ the electron azimuthal drift speed and $u_i$ the ion
  velocity. *Compiler note:* the form printed in the 2019 review is the
  inverse ratio of the "small-scale turbulence" entry of its own Tab. II;
  the review does not comment on this.

## Contradictions

* **Form of the Jorns (2018) data-driven anomalous collision frequency.**
  *Open.* [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.4
  (HAL accepted manuscript, verified on the rendered page), state that the
  best fit is $\nu_{\mathrm{ano}}\propto\omega_{ce}(c_s/u_{e,\theta})^2$, with
  the ion sound speed in the numerator.
  [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. V D, Eq. 22
  (accepted manuscript, checked on rendered p. 24), state
  $\nu_{\mathrm{ano}}\propto\omega_{ce}(u_i/u_{e,\theta})^2$, with the ion
  velocity in the numerator. Both cite the same work (Jorns, Plasma Sources
  Sci. Technol. 27:104007, 2018), which this bundle has not ingested. The
  two forms differ wherever the ion velocity differs from $c_s$. Ingesting
  Jorns (2018) (Taccogna et al. 2023, ref. 344) would close this entry.

# Citations

1. [Boyd (2005)](/sources/boyd-2005.md), §§3.4, 4, Fig. 16.
2. [Adamovich et al. (2017)](/sources/adamovich-2017.md), §§12, 16.
3. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §§2.4, 2.5, 2.7, 3.3, 3.4, Tab. II, Figs. 5, 15 (accepted manuscript).
4. [Charoy et al. (2020)](/sources/charoy-2020.md), §§III A, IV A–B, Conclusion, Eqs. 7–9, Figs. 5–7 (accepted manuscript).
5. [Giannetti et al. (2021)](/sources/giannetti-2021.md), §§2.3, 4, 5, eqs. 10–11, Fig. 6.
6. [Reza et al. (2022)](/sources/reza-2022.md), §§3.1–3.2, 5.1, Figs. 3–4, 6, Table 3 (preprint).
7. [Ahedo (2023)](/sources/ahedo-2023.md), §3D, Eqs. 18–21, 26, Fig. 4.
8. [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. V D, Eq. 22 (accepted manuscript).
9. [Eckels et al. (2024)](/sources/eckels-2024.md), Eqs. 5–6, Table 3, Obs. 4, Fig. 12.
10. [Marks & Gorodetsky (2025)](/sources/marks-2025.md), "Plasma instabilities", Figs. 11–13.
11. [Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md), Eq. 7, "PlasmaSim 2D", Table 1.
12. [Miranda et al. (2026)](/sources/miranda-2026.md), §§3–5, Table 1.
13. [Troyetsky et al. (2026)](/sources/troyetsky-2026.md), Eq. 8, "Results: Model comparison", Figs. 4, 10–11.
14. [Saravia et al. (2026)](/sources/saravia-2026.md), Eqs. 6–7, 21, Tables 1, 5, §6.2.

---
type: Result
title: "Instability-enhanced electron–ion friction and effective mobility"
description: "The azimuthal electron drift instability produces a momentum-conserving electron–ion friction force, equal to the density–field fluctuation correlation, that drives axial electron transport; a quasi-linear closure in the electron distribution slope reproduces it in PIC when fed PIC data, while the ion-trapping saturation and Maxwellian closures do not."
status: established
aliases: [anomalous friction force, electron–ion friction force, instability-enhanced collisionality, enhanced mobility, Lafleur mobility, quasi-linear friction closure]
tags: [anomalous-transport, instability, kinetic, pic, hall-thruster]
timestamp: 2026-10-14T00:00:00Z
---

# Instability-enhanced electron–ion friction and effective mobility

## Statement

In the azimuthal electron momentum balance of a Hall-thruster discharge,
the azimuthal [electron drift instability](/definitions/electron-drift-instability.md)
adds an electron–ion friction force density $R_{ei,\theta}$. It equals the
azimuthal and time average of the product of the electron density and the
azimuthal electric field fluctuations, times $-q_e$; the ions receive the
opposite force, $\mathbf R_{ie}=-\mathbf R_{ei}$. This force balances part of
the magnetic force on the azimuthal current and therefore sets an axial
electron flux, i.e. an [anomalous](/definitions/anomalous-electron-transport.md)
cross-field mobility.

## Evidence

**Friction from PIC** ([Charoy et al. (2020)](/sources/charoy-2020.md),
2D axial–azimuthal PIC-MCC with LPPic, ten cases
around the [axial–azimuthal benchmark](/benchmarks/axial-azimuthal-pic-benchmark.md),
peak field 0.005–0.02 T (printed as 50–200 G), current density
50–400 A m⁻²; positions are given in the benchmark's planar coordinates,
$x$ axial and $y$ azimuthal):
* The friction force is the main contributor to axial electron transport
  in all seven collisionless cases, without wall or neutral collisions
  (§III A, Figs. 5a, 6). Its peak is about 11 N m⁻³ at the field maximum in
  the nominal case (read off Fig. 5a); across cases it spans 0.5–20 N m⁻³
  (Fig. 10).
* Classical Coulomb (Lenard–Balescu) friction is smaller by "of the order
  of a factor of 500" (§III A, Eq. 6).
* $R_{ei}$ and $-R_{ie}$, each computed from the density–field correlation
  of its species, coincide in all cases, so the anomalous term is a
  momentum-conserving drag (§IV D, Fig. 11).
* Lower current density lowers the force; the text states that halving the
  current density halves it (§III B)¹. The force grows with the field,
  with a distinct plume peak at 0.005 T.
* With neutrals, all collisions together raise the force "by almost a
  factor 2"; ion–neutral backscattering (charge exchange) raises it,
  isotropic ion–neutral scattering does not, and the electron–neutral drag
  is negligible beside the friction (§V, Fig. 12). The mechanism proposed
  for the backscattering effect, a modified ion distribution that reduces
  Landau damping, is a hypothesis.

**Quasi-linear closure** (Charoy et al. 2020, §IV A, Eqs. 12–24). For a
single electrostatic mode and unmagnetized electrons, with the maximum
growth at $k_\theta\lambda_D=1/\sqrt2$ and a phase velocity near $c_s$,
much below the electron thermal speed, the friction reduces to
$$R_{ei,\theta}\simeq2\sqrt2\,\pi\,\omega_{pe}^2\lambda_D\;(\text{wave energy density})\;\left.\frac{d}{dv_\theta}\left[\frac{1}{n_e}\int f_e\,dv_z\,dv_r\right]\right|_{v_\theta=0},$$
where the wave energy density is $\tfrac12\varepsilon_0$ times the azimuthal
mean square of the fluctuating field (Eq. 15) and $f_e$ is the
time-averaged electron distribution. The derivation is stated, not
proved; validity requires a fluctuating potential much smaller than $T_e/e$,
which the PIC satisfies everywhere (§IV B).
* Fed with the local PIC electron distributions and wave energies, the
  closure agrees "very well" with the PIC force in all seven collisionless
  cases (§IV C, Fig. 10) and in the collisional cases (§V). Because its
  inputs come from the PIC, this tests the closure's physics, not a
  predictive model.
* The drifting-Maxwellian form of the same closure overestimates the force
  by about 3 and changes sign between $x=1.25$ and 1.75 cm, because the
  PIC distributions are strongly non-Maxwellian, especially near the anode
  (§IV B, Figs. 7–8).
* The ion-wave-trapping saturation model (Lafleur et al. 2016; Lafleur &
  Chabert 2018) sets the wave energy at $1/432$ of the thermal energy
  density. Except at 0.005 T, the PIC wave energy stays below this limit, so
  the saturated model overestimates the force (§IV B, Eqs. 10, 28–29,
  Fig. 9). Charoy et al. note that Croes et al. (2017) found saturation at
  the trapping level in radial–azimuthal PIC.
* An empirical Bohm-plus-wall model fitted to the force ($\alpha_{\mathrm B}=0.17$
  outside the channel, wall scale factor 0.4 inside) matches only for
  $x<1$ cm, goes to zero in the plume and "is not predictive" (§IV B,
  Fig. 7).

Charoy et al. conclude that the force depends sensitively on the
non-Maxwellian distribution, so a self-consistent fluid closure for
anomalous transport remains out of reach (Conclusion).

**Effective mobility.** The correlation term can be written as an
effective cross-field mobility (Lafleur et al. 2016)
$$\mu_\perp^{\mathrm{eff}}=\frac{\mu_\parallel}{1+\Omega_e^2}\left(1-\Omega_e\,\frac{\langle\tilde n_e\tilde E_\theta\rangle}{n_eE_z}\right),$$
with $\mu_\parallel=e/(m_e\nu_e)$ built on the electron–neutral frequency,
$\langle\cdot\rangle$ the average over azimuth and time, and the tildes
the fluctuations about it. The sources write the correlation of the full
density and field; since the azimuthal mean of $E_\theta$ vanishes in a
periodic domain, the two coincide (compiler note).
* In a [reduced-order](/methods/reduced-order-pic.md) radial–azimuthal PIC,
  the mobility computed from the simulated axial electron drift agrees
  with this formula evaluated on the simulated fluctuations
  ([Reza et al. (2022)](/sources/reza-2022.md), §4.3.2, Eqs. 11–13; figure
  images missing from the preprint).
* Taccogna & Garrigues (2019, §3.4, eq. 34) print the anomalous part of
  the same mobility, attributed to Lafleur et al. (2016, 2017)²
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md)).

**No conflict between the two tests** (compiler note). Reza et al. (2022)
test the identity between the fluctuation correlation and the mobility;
Charoy et al. (2020) test closures that predict the correlation's size.
Charoy et al. reject the ion-trapping saturation level as a closure while
verifying the correlation-based friction itself (Fig. 11), which is what
Reza et al. confirm.

**Insensitivity hypothesis against the closure** (compiler note,
hypothesis-grade). Marks & Gorodetsky (2025, "Plasma instabilities",
Figs. 11–13) find that coarsening the grid and time step 4× in a
semi-implicit GPU PIC of the same benchmark lowers the peak azimuthal
field by 40% while the time-averaged axial field and the cathode current
are preserved, and hypothesize that the transport is insensitive to some
spectral characteristics of the instability
([Marks & Gorodetsky (2025)](/sources/marks-2025.md)). Under the
quasi-linear closure above the friction is proportional to the wave energy
times the slope of the electron distribution; a 40% lower field amplitude,
if the same factor held for the wave energy, means about 64% less wave
energy, which the distribution slope would have to compensate for the
transport to stay unchanged. Neither paper tests this; it is recorded as a
tension, not a contradiction.

¹ Peak values read off Charoy et al.'s Fig. 10 (about 0.37, 0.95, 2.0 and
10.5 N m⁻³ at 50, 100, 200 and 400 A m⁻²) give ratios of 2.1–5 per
doubling, not a clean factor 2 (reader's plot reading; approximate).

² The printed eq. 34 uses $h$, the review's symbol for the channel width,
where the Hall parameter is meant; see
[Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), Recorded as
printed.

# Citations

1. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.4, eq. 34 (accepted manuscript).
2. [Charoy et al. (2020)](/sources/charoy-2020.md), §§III A–B, IV A–D, V, Conclusion, Eqs. 6, 10, 12–29, Figs. 5–12 (accepted manuscript).
3. [Reza et al. (2022)](/sources/reza-2022.md), §4.3.2, Eqs. 11–13 (preprint).
4. [Marks & Gorodetsky (2025)](/sources/marks-2025.md), "Plasma instabilities", Figs. 11–13.

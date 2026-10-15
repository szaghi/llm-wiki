---
type: Definition
title: "Electron drift instability (ECDI)"
description: "The azimuthal instability driven by the E x B electron drift in Hall thrusters, with millimetre wavelengths and MHz frequencies, cyclotron-resonant in linear theory and close to an ion-acoustic mode in most axial–azimuthal PIC; it carries most of the anomalous electron transport in kinetic simulations."
status: established
aliases: [ECDI, EDI, electron cyclotron drift instability, E x B electron drift instability, modified ion-acoustic instability, azimuthal instability]
tags: [instability, anomalous-transport, hall-thruster, pic, kinetic, oscillation]
timestamp: 2026-10-15T00:00:00Z
---

# Electron drift instability (ECDI)

The electron drift instability is driven by the azimuthal
$\mathbf E\times\mathbf B$ drift of magnetized electrons relative to
unmagnetized ions in a [Hall-effect thruster](/definitions/hall-effect-thruster.md).
Fully kinetic simulations find that it carries most of the
[anomalous electron transport](/definitions/anomalous-electron-transport.md)
through an electron–ion friction force
([Instability-enhanced electron–ion friction](/results/instability-enhanced-friction-force.md)).

## Linear properties

* **Cyclotron resonances.** Taccogna & Garrigues (2019, §3.4, eq. 35)
  give resonances at $k_{\theta}=n\,\omega_{ce}/|u_{e,\theta}|$, $n=1,2,\dots$,
  with $u_{e,\theta}$ the electron azimuthal drift speed, and maximum
  growth at $\omega\approx\omega_{pi}/\sqrt3$. With a radial wavenumber the
  dispersion relation becomes a modified ion-acoustic one
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md)).
* **Ion-acoustic limit.** Charoy et al. (2020, §IV A, Eqs. 18–19, after
  Lafleur et al. 2016) use the simplified ion-acoustic dispersion relation
  $$\omega_r\approx k_\theta u_{i,\theta}\pm\frac{k_\theta c_s}{\sqrt{1+k_\theta^2\lambda_D^2}},\qquad \omega_i\approx\pm\sqrt{\frac{\pi m_e}{8m_i}}\,\frac{k_\theta u_{e,\theta}}{(1+k_\theta^2\lambda_D^2)^{3/2}},$$
  whose growth rate is maximum at $k_\theta\lambda_D=1/\sqrt2$, a wavelength
  $\lambda_w=2\pi\sqrt2\,\lambda_D$. They argue, citing Lampe et al. (1972),
  that nonlinear smearing of the cyclotron resonances leaves an
  unmagnetized ion-acoustic instability, so that the magnetic field only
  supplies the drift ([Charoy et al. (2020)](/sources/charoy-2020.md),
  §IV A). [Reza et al. (2022)](/sources/reza-2022.md) (§3.2, Eq. 8) and
  [Miranda et al. (2026)](/sources/miranda-2026.md) (§3, after Boeuf &
  Garrigues 2018) use the same ion-acoustic estimates.

## Observed scales

| Source | Model | Wavelength | Frequency | Other |
|---|---|---|---|---|
| [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.4 | 1D azimuthal PIC (reviewed) | mm | MHz, discrete cyclotron harmonics in the linear stage | ion density perturbations non-quasineutral, $k_\theta\lambda_D\ge1$ |
| [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.4, Fig. 18 | 2D axial–azimuthal PIC (Boeuf & Garrigues 2018) | $\sim\lambda_D$ | $\sim\omega_{pi}$ | $|E_\theta|\sim T_e/(e\lambda_D)$; $E_\theta$ within $\pm5\times10^4$ V/m |
| [Charoy et al. (2020)](/sources/charoy-2020.md), §II B, §IV B | 2D axial–azimuthal PIC (LPPic) | short near the anode, long in the plume | not measured | $\tilde n_e/n_e\sim10\%$ in the channel, a few % just downstream |
| [Reza et al. (2022)](/sources/reza-2022.md), §3.2, Fig. 5 | pseudo-2D axial–azimuthal PIC | $\sim2$ mm | $\sim3$ MHz | dominant mode near $k_\theta\lambda_D\approx0.25$–$0.3$, $\omega/\omega_{pi}\approx0.3$ (read off the figure) |
| [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. III A d, Fig. 3 | review | mm | MHz | 3D amplitude about ten times smaller than 2D |
| [Marks & Gorodetsky (2025)](/sources/marks-2025.md), Figs. 11–13 | 2D axial–azimuthal PIC (WarpX) | two modes: short near the anode, long downstream | matches the benchmark at 1× and 2× resolution | |
| [Miranda et al. (2026)](/sources/miranda-2026.md), §3, Fig. 7a | 2D axial–azimuthal PIC (XOOPIC), Xe | $1.1\times10^{-3}$ m (spectral peak) against $9.34\times10^{-4}$ m from $2\pi\sqrt2\,\lambda_D$¹ | 1–10 MHz (attributed to Lafleur et al.) | Ar run adds a $\sim10$ mm wave |

* **Dependence on $\mathbf B$ and current density.** At a 0.01 T (printed as 100 G) field peak
  the wavelength changes sharply between a short-wavelength near-anode
  region and a long-wavelength plume region; a stronger field extends the
  long wavelengths to the anode and a 0.005 T field extends the short ones
  into the plume. Lower current density, hence lower density, gives
  longer wavelengths, as expected from $k_\theta\lambda_D=1/\sqrt2$
  ([Charoy et al. (2020)](/sources/charoy-2020.md), §II B, Figs. 3–4). The
  paper reports no measured growth rates, frequencies or wavelengths for a
  quantitative check of Eqs. 18–19.
* **Fluctuation level.** About 10% in the channel and a few percent just
  downstream of the exit, close to the ~1% measured by Tsikata et al.
  (2009), against 15–20% in radial–azimuthal PIC by others (Charoy et al.
  2020, §IV B). In 3D PIC the fluctuation amplitude is "typically one order
  of magnitude smaller than in 2D", close to Thomson-scattering estimates
  ([Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. III A d,
  attributed to refs. 62, 103–107).
* **Propellant.** Miranda et al. (2026, §4) report, citing Croes et al.
  (2018), that the instability frequency depends on the ion mass while the
  electron mobility "seems to be independent of the propellant". Their own
  argon run has a mean electron axial velocity nearly twice the xenon one
  (§3, Table 1), in a non-steady start-up transient.

## Nonlinear regime and dimensionality

Taccogna & Garrigues (2019, §3.4) report a disagreement in the literature
on the nonlinear state: 1D azimuthal PIC finds a transition to an
unmagnetized ion-sound regime (Ducrocq 2006, Boeuf 2014, Lafleur 2016)
while Janhunen et al. (2018) find a persistent cyclotron-resonant coherent
mode with an inverse cascade. The review attributes the discrepancy to the
missing axial dimension in 1D azimuthal models: particle re-injection,
convection, and a mobility about ten times too large with a fixed axial
field. In 2D radial–azimuthal PIC the full ion-sound regime is not reached
and discrete cyclotron resonances persist; 2D axial–azimuthal PIC recovers
ion-acoustic scalings. The ion-acoustic interpretation of Charoy et al.
(2020), Reza et al. (2022) and Miranda et al. (2026) is made in the
axial–azimuthal plane, consistent with this picture (compiler note).
Marks & Gorodetsky (2025, §Kinetic simulations in an engineering context)
report, citing Villafana et al. (2023), that 2D axial–azimuthal models
under-resolve the instability physics that 3D PIC shows.

## Numerical requirements

* Taccogna & Garrigues (2019, §3.4) state that numerical noise destroys
  the cyclotron resonances and "facilitates the transition to an ion
  acoustic instability"; "it seems" that more than 1000 particles per cell
  ($N_{\mathrm{ppc}}>1000$) are needed for an acceptable statistical
  level. An unattributed 1D azimuthal illustration (Fig. 16, presumably
  the authors') uses $N_{\mathrm{ppc}}=2.5\times10^4$ on a 5 cm azimuth.
* In the axial–azimuthal benchmark, about 250 particles per cell at steady
  state give converged time-averaged profiles
  ([Charoy et al. (2020)](/sources/charoy-2020.md), §II A, citing the
  benchmark), and a GPU run with 75 initial and 290 steady-state particles
  per cell falls within the benchmark band
  ([Marks & Gorodetsky (2025)](/sources/marks-2025.md), Fig. 3, Table 4).
  As convergence criteria for mean profiles these counts are a different
  criterion from the 1000-particle requirement (compiler note). Whether
  the ion-acoustic character seen at these counts is noise or physics is
  an Open entry under Contradictions below. See
  [Resolution constraints of explicit PIC](/definitions/explicit-pic-resolution-constraints.md).
* Coarsening grid and time step with a semi-implicit field solve keeps the
  dominant wavelengths and frequencies at 2× but blurs the two-mode
  structure at 4× and removes it at 8×, with the peak azimuthal field
  reduced by 40% and 70%
  ([Marks & Gorodetsky (2025)](/sources/marks-2025.md), Figs. 11–13; see
  [Semi-implicit, implicit and energy-conserving PIC](/methods/implicit-and-energy-conserving-pic.md)).
* Organization of the azimuthal field can be quantified by its
  [spectral entropy](/methods/spectral-entropy.md): 0.57 (1D) and 0.79 (2D)
  for xenon, 0.44 and 0.65 for argon
  ([Miranda et al. (2026)](/sources/miranda-2026.md), §3, Table 1).

## Coupling with walls

In 2D radial–azimuthal PIC, Taccogna & Garrigues (2019, §3.4) report,
citing Tavant (2018) and Taccogna (2019), that the instability couples to
the secondary-emission sheath: bulk anomalous mobility falls by 20% as
emission rises while near-wall mobility doubles. In a
[reduced-order](/methods/reduced-order-pic.md) radial–azimuthal PIC, the
instability heats the electrons until the wall yield passes the
space-charge-saturation threshold at about 1 µs, after which bursts of
secondary electrons cross the channel; adding the radial direction lowers
the wave energy and the mobility compared with a 1D azimuthal run
([Reza et al. (2022)](/sources/reza-2022.md), §4.3, figure images missing
from the preprint). The authors flag mobility oscillations of period
0.7 µs as an artefact of periodic re-injection over the finite axial
length. See [near-wall conductivity](/definitions/near-wall-conductivity.md)
and [secondary electron emission](/definitions/secondary-electron-emission.md).

## Modified two-stream instability (MTSI)

In 2D radial–azimuthal PIC a longer-wavelength modified two-stream
instability appears alongside the cyclotron resonances
([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.4, Fig. 17,
after 0.5 µs, attributed to Janhunen et al. 2018;
[Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. III A d). In the
radial–azimuthal benchmark of Villafana et al. (2021), seven codes
reproduce both the MTSI and the ECDI resonances "with a minimal
difference" (Taccogna et al. 2023, Fig. 4). Miranda et al. (2026, §3) note
that 1D and 2D radial–azimuthal PIC show the MTSI and that 3D PIC is needed
to settle its role.

## Other sources

The 2017 Plasma Roadmap reproduces MHz-scale density and field
fluctuations from a Hall-thruster PIC simulation (Lafleur et al. 2016) and
relates anomalous transport to fluctuations amplified by electron–ion
differential flow, without naming the instability
([Adamovich et al. (2017)](/sources/adamovich-2017.md), §16, Fig. 31).

¹ With the printed $\lambda_D=8.18\times10^{-5}$ m, $2\pi\sqrt2\,\lambda_D$
is $7.27\times10^{-4}$ m, not the printed $9.34\times10^{-4}$ m; the printed
peak $k\sim896$ m⁻¹ corresponds to $1.1\times10^{-3}$ m only as a spatial
frequency in cycles per metre. See
[Miranda et al. (2026)](/sources/miranda-2026.md), Recorded as printed.

## Contradictions

* **Cause of the ion-acoustic character of azimuthal PIC at
  $N_{\mathrm{ppc}}<1000$.** *Open.*
  [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.4, state
  that numerical noise "facilitates the transition to an ion acoustic
  instability" and that "it seems" more than 1000 particles per cell are
  needed; [Charoy et al. (2020)](/sources/charoy-2020.md), pp. 17–18, at
  about 250 per cell, attribute the ion-acoustic character to physical
  nonlinear smearing of the cyclotron resonances (after Lampe et al. 1972)
  and build their friction closure on it. The review's own §3.4 reports that 2D axial–azimuthal PIC recovers ion-acoustic scalings, the plane of Charoy et al.'s runs, so its noise statement is not specific to that plane. Neither tests the other's
  mechanism.

# Citations

1. [Adamovich et al. (2017)](/sources/adamovich-2017.md), §16, Fig. 31.
2. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.4, eqs. 34–35, Figs. 16–18 (accepted manuscript).
3. [Charoy et al. (2020)](/sources/charoy-2020.md), §§II A–B, IV A–B, pp. 17–18, Eqs. 18–19, Figs. 3–4 (accepted manuscript).
4. [Reza et al. (2022)](/sources/reza-2022.md), §§3.2, 4.3, Eq. 8, Fig. 5 (preprint).
5. [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. III A d, Figs. 3–4 (accepted manuscript).
6. [Marks & Gorodetsky (2025)](/sources/marks-2025.md), Fig. 3, Table 4, Figs. 11–13, "Kinetic simulations in an engineering context".
7. [Miranda et al. (2026)](/sources/miranda-2026.md), §§3–4, Fig. 7, Table 1.

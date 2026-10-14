---
type: Method
title: "One-dimensional fluid model of the Hall-thruster discharge"
description: "Quasi-neutral, unsteady model of the axial (z) structure of a Hall-thruster discharge with fluid neutrals and ions and drift-diffusion electrons, in which the uniform discharge current follows from an integral of the generalized Ohm's law; cheap enough (minutes per run) for parameter calibration, but dependent on an empirical anomalous-transport profile."
status: established
aliases: [1D axial fluid model, 1Dz model, one-dimensional Hall thruster model, axial quasi-neutral fluid model, LANDMARK test case 3]
tags: [fluid, hall-thruster, anomalous-transport, oscillation, calibration, numerics]
timestamp: 2026-10-14T00:00:00Z
---

# One-dimensional fluid model of the Hall-thruster discharge

The model resolves only the axial coordinate $z$ of a
[Hall-effect thruster](/definitions/hall-effect-thruster.md), from the
anode ($z=0$) to a virtual cathode line in the near plume ($z=L$), with
quantities averaged over each cross-section. It is quasi-neutral,
$n_e=n_i$, so no Poisson equation is solved. It is the axial reduction of
the [electron fluid model](/methods/electron-fluid-model.md). Below,
$u_s$ is the axial component of $\mathbf u_s$, and $L_{\mathrm{ch}}$ the
channel length.

## Lineage

[Boyd (2005)](/sources/boyd-2005.md), §3.4, lists 1D Hall models among the
models that "explore fundamental properties": Boeuf & Garrigues (Vlasov
ions, fluid neutrals at constant velocity), the first to predict the
low-frequency oscillations; Fruchtman et al. (fully fluid, absorbing
electrodes); Ahedo et al. (three-fluid 1D); and Garrigues et al. (1D PIC
ions, good qualitative agreement on thrust for xenon and krypton, though
the computed thrust lies below the measured one at every voltage of
Boyd's Fig. 14). [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md),
§2.1, Tab. I, catalogue 1D-$z$ models among 20 fluid and hybrid models,
and report that most of them give the neutrals a constant velocity and
solve only their continuity equation (Boeuf & Garrigues 1998; Morozov &
Savelyev 2000; Ahedo et al. 2002), while Barral et al. (2003) carry two
neutral populations (injected and wall-thermalized).

## Equations (Giannetti et al. 2021; Saravia et al. 2026)

The two Pisa papers solve the same system, with different wall and
energy-loss terms ([Giannetti et al. (2021)](/sources/giannetti-2021.md),
§2, eqs. 1–23, App. A;
[Saravia et al. (2026)](/sources/saravia-2026.md), §§2.1–2.2, eqs. 1–16):

* **Neutrals:** continuity only, at a constant, prescribed axial speed
  $u_n$,
  $$\partial_t n_n+\partial_z(u_nn_n)=-n_en_nk_{\mathrm{ion}},$$
  plus a wall-recombination source in Giannetti et al. The anode value of
  $n_n$ is the injected flux $\dot m/m_i$ divided by $u_n$ and by the
  channel cross-section area, minus the recombined ion backflow
  $n_e(0)u_i(0)/u_n$ (Giannetti et al., eq. 23; Saravia et al., BC5).
* **Ions:** singly charged, unmagnetized, cold ($T_i=0$ in all results),
  continuity and axial momentum, with ionization source
  $n_en_nk_{\mathrm{ion}}$. Charge exchange and the plume expansion are
  neglected.
* **Electrons:** inertia-less drift-diffusion (generalized Ohm's law) with
  a purely radial $\mathbf B$,
  $$n_eu_e=\mu_\perp\left(n_e\,\partial_z\phi-\frac1e\,\partial_zp_e\right),\qquad
  \mu_\perp=\frac{\mu_\parallel}{1+\Omega_e^2},\quad
  \mu_\parallel=\frac{e}{m_e\nu_e},\quad\Omega_e=\frac{\omega_{ce}}{\nu_e},$$
  with $\nu_e=\nu_{en}+\nu_w+\nu_{\mathrm{ano}}$ and the Bohm-type
  $\nu_{\mathrm{ano}}=\alpha_{\mathrm B}(z)\,\omega_{ce}/16$ (see
  [cross-field mobility](/definitions/electron-mobility-and-hall-parameter.md)
  and [anomalous transport](/definitions/anomalous-electron-transport.md)).
  The electron internal-energy equation carries convection, a Fourier
  conduction term built on $\mu_\perp$, Ohmic heating and collisional
  losses from tabulated rate coefficients.
* **Discharge current:** current conservation makes the axial current
  density $j_z=en_e(u_i-u_e)$ uniform in $z$. Dividing Ohm's law by
  $\mu_\perp$ and integrating across the domain gives
  $$j_z(t)=\frac{V_d+\displaystyle\int_0^{L}\left(\frac{u_i}{\mu_\perp}+\frac{1}{en_e}\,\partial_zp_e\right)dz}{\displaystyle\int_0^{L}\frac{dz}{en_e\mu_\perp}},$$
  then $u_e=u_i-j_z/(en_e)$, and $\phi$ follows from Ohm's law. Giannetti
  et al. add an electron-repelling anode sheath drop to $V_d$; Saravia
  et al. neglect it (Giannetti et al., eqs. 19–22; Saravia et al., eqs.
  12–14).
* **Ion momentum reformulation:** $\partial_z\phi$ is eliminated from the
  ion momentum equation through Ohm's law, so that the hyperbolic ion
  system carries the acoustic speed $\sqrt{(T_i+T_e)/m_i}$ (which reduces
  to $c_s$ for $T_i=0$); both papers attribute the stability gain to
  Hara (2018), Giannetti et al. adding "as amply demonstrated in the
  literature"
  ([Giannetti et al. (2021)](/sources/giannetti-2021.md), §2.4, eqs. 17–18;
  [Saravia et al. (2026)](/sources/saravia-2026.md), §2.2, eq. 11).

| | [Giannetti et al. (2021)](/sources/giannetti-2021.md) | [Saravia et al. (2026)](/sources/saravia-2026.md) |
|---|---|---|
| thruster | HT5k (SITAEL, 5 kW class), chamfered channel | LANDMARK test case 3 (below), SPT-100-based geometry |
| wall model | 1D Hobbs–Wesson sheath with SEE, inside the channel only, every wall term scaled by a calibrated coefficient | constant $\nu_w=10^7$ s$^{-1}$ in the channel, 0 outside; no SEE, no radial losses |
| extra energy loss | wall power loss from the sheath model | empirical anomalous loss $\propto\tfrac32T_e\exp(-20\,\mathrm{eV}/\tfrac32T_e)$, scaled by a calibrated coefficient |
| anode | sheath drop; ions enter the sheath edge at or above the acoustic speed | $\phi(0)=V_d$; Bohm conditions at both ends argued superfluous because ion characteristics point outward |
| cathode line | $T_e=2$ eV | $T_e=2$ eV at both ends |
| domain | $L=2L_{\mathrm{ch}}$ ($L_{\mathrm{ch}}$ not printed) | $L=2L_{\mathrm{ch}}=5$ cm, 1000 cells |

## Discretization

Both papers use finite volumes and a first-order fractional-step (Lie)
splitting into five sequential sub-steps per time step: neutrals, ions,
$T_e$ (with the old $u_e$), $j_z$, then $u_e$
([Giannetti et al. (2021)](/sources/giannetti-2021.md), §2.4;
[Saravia et al. (2026)](/sources/saravia-2026.md), §2.2):
* neutrals: first-order upwind;
* ions: Steger–Warming flux-vector splitting, which also imposes the
  characteristic boundary conditions;
* electron energy: second-order finite volume with central face gradients,
  implicit Euler;
* everything else: explicit Euler. Saravia et al. set CFL 0.8 on the
  fastest ion characteristic; Giannetti et al. print neither $\Delta t$
  nor the cell count.

Saravia et al. drop the LANDMARK artificial-viscosity term because "the
used numerical scheme made its use unnecessary" (footnote 1). Their code
is FORTRAN 95 with shared-memory parallelism, driven from Python through
f2py (§4.2). Giannetti et al. report about 1310 s of wall time per 1 ms of
simulated time on a 6-core laptop processor, with a code "not optimized"
(§2.4).

## Extended 1D model with azimuthal inertia (Ahedo 2023)

[Ahedo (2023)](/sources/ahedo-2023.md), eqs. 37–43, Fig. 3, extends the
1D-$z$ model with a variable cross-section area, electron azimuthal
inertia, an internal volumetric cathode (an emission layer of cold
electrons, ±2.5 mm in Fig. 3) and the far plume, with the effective
collision frequency $\nu_e+\nu_{\mathrm{ano}}$ in the electron momentum
and heat-flux laws. Azimuthal inertia matters near the anode, around the
cathode and in the near plume, where it bounds the azimuthal electron
velocity to the order of $\sqrt{T_e/m_e}$; it changes $\phi$ and $T_e$
little between anode and cathode (Fig. 3: plume potential about 65 V
without and 55 V with inertia, values read off the figure). The model
motivated the azimuthal-velocity limiter of
[HYPHEN](/software/hyphen.md). The bumps downstream of the cathode are
exaggerated, which Ahedo calls a limitation of the 1D-$z$ geometry. Cost:
minutes, against tens of hours for the 2D ($z$, $r$) electron model.

## Multi-fluid 1D model as a system component (Eckels et al. 2024)

[Eckels et al. (2024)](/sources/eckels-2024.md) use the 1D axial
multi-fluid code HallThruster.jl (Julia; Marks et al. 2023) as the thruster
component of a coupled cathode–thruster–plume model. Its governing
equations, field solver and collision model are not written in the paper.
Fidelity levels are 100, 150 or 200 cells and 1 to 3 ion charge states;
one evaluation takes about 1 min (p. 9, p. 10). Anomalous transport is a
two-zone Bohm-type profile whose transition moves with the facility
background pressure, and background neutrals are ingested at the anode
(eqs. 4–6, 22).

## Verification: LANDMARK test case 3

LANDMARK ("Low temperature magnetized plasma benchmarks") is a project that
defines benchmark cases for PIC, hybrid and fluid models of
$\mathbf E\times\mathbf B$ plasmas
([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.4). Its
case 2a is the [axial–azimuthal PIC benchmark](/benchmarks/axial-azimuthal-pic-benchmark.md)
([Marks & Gorodetsky (2025)](/sources/marks-2025.md)). Test case 3 is a
one-dimensional axial fluid case of this model, known here only through
[Saravia et al. (2026)](/sources/saravia-2026.md), §§2.1–2.2, Table 1,
App. A, who implement and verify it; the benchmark specification itself
(a website, their ref. 43) is not ingested. Its set-up, as Saravia et al.
give it:

* **Model:** the equations above, cold ions and cold neutrals, no radial
  ion losses, anode recombination in the neutral boundary condition;
  xenon.
* **Geometry and operating point** (Table 1, "based on the SPT-100"):
  inner and outer channel radii 3.5 and 5.0 cm, $L_{\mathrm{ch}}=2.5$ cm,
  domain $L=5.0$ cm, $\dot m=5$ mg/s, $V_d=300$ V. See
  [SPT-100](/benchmarks/spt-100.md).
* **Magnetic field** (eq. 15): Gaussian in $z$, peak 0.015 T at
  $z=L_{\mathrm{ch}}$, width 1.1 cm inside and 1.8 cm outside the channel.
* **Collisions** (eqs. 6–7): $\nu_e=\nu_{en}+\nu_w+\nu_{\mathrm{ano}}$ with
  a constant electron–neutral momentum-transfer rate coefficient (printed
  $2.5\times10^{13}$ m³/s, a slip recorded on the Source page),
  $\nu_w=10^7$ s$^{-1}$ in the channel and 0 outside, and
  $\nu_{\mathrm{ano}}=\alpha_{\mathrm B}(z)\,\omega_{ce}/16$. The profile
  $\alpha_{\mathrm B}(z)$ is a sum of two error functions of width
  $L_{\mathrm{ch}}/50$ centred on the exit plane, from an in-channel value
  to a plume value (eq. 21).
* **Energy losses:** tabulated collisional loss and ionization rates from
  the benchmark, plus an empirical anomalous loss per electron equal to a
  dimensionless energy-loss coefficient times
  $\tfrac32T_e\exp(-20\,\mathrm{eV}/\tfrac32T_e)$ (eq. 9). The same
  empirical form, with a reference frequency of $10^7$ s$^{-1}$, is reported
  by [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.3,
  eq. 30, as used by earlier models (Boeuf & Garrigues 1998; Hagelaar
  2002; Koo & Boyd 2004; Hara 2012).
* **Boundary conditions:** $\phi=V_d$ at the anode and 0 at the cathode
  line, $T_e=2$ eV at both ends, the anode neutral density set by the
  injected flow minus the recombined ions, and Bohm conditions on the ion
  velocity at both ends, which Saravia et al. argue are superfluous
  because the ion characteristics always point outward (BC1–BC6, eq. 10).
* **Artificial viscosity:** the benchmark carries a viscosity term, which
  Saravia et al. drop because their scheme does not need it (footnote 1).

**Run** ([Saravia et al. (2026)](/sources/saravia-2026.md), App. A,
Figs. 13–14): 1000 cells, CFL 0.8, run for 1 ms after a limit cycle is
reached. The oscillation damps when the energy-loss coefficient exceeds a
threshold printed as "$0.5\times10^7$ s⁻¹"; the oscillatory case presented
uses "$0.4\times10^7$ s⁻¹" (units as printed; the coefficient is
dimensionless elsewhere in the paper, see the Source page). Results against
the benchmark reference: mean $I_d$ 8.03 A (benchmark) against 7.96 A,
under 1 %; peak plasma density $1.04\times10^{19}$ m$^{-3}$, 5.4 % from the
benchmark; peak neutral density $7.87\times10^{19}$ m$^{-3}$, 2.8 % from the
benchmark (the paper does not say which run the two peak values belong
to). Oscillation frequency and amplitude agree by visual comparison; the
authors attribute the residual differences to numerical viscosity. Which of
8.03 and 7.96 A belongs to which run rests on one sentence of App. A; the
Fig. 14 caption calls the reference the "HALLIS benchmark" (recorded on the
Source page). The same model then serves as the "true" model for
synthetic-data [Bayesian calibration](/methods/bayesian-calibration.md),
with reference values neutral speed 150 m/s, energy-loss coefficient 0.4,
in-channel $\alpha_{\mathrm B}=0.1$ and plume $\alpha_{\mathrm B}=1.0$
(§2.3, Table 1); its reference current is a breathing-mode oscillation
(Fig. 2).

**What it shows.** One code-to-code verification of the mean current and
peak densities, with no error norm or convergence study. It verifies that
a code solves the benchmark's equations; it says nothing about the model's
fidelity to a thruster.

## What the 1D model reproduces and misses

* **Breathing current.** Calibrated on the discharge current alone, the
  model reproduces the [breathing mode](/definitions/breathing-mode.md):
  its maximum and minimum current fall within the measured ranges
  (16.4 A against 13.9–17.3 A, 4.5 A against 3.3–5 A), and its mean, RMS
  and frequency are close to the measured ones (8.67 against 8.65 A,
  3.9 against 4.1 A, 25.3 against 25.4 kHz)
  ([Giannetti et al. (2021)](/sources/giannetti-2021.md), §4, Table 2).
* **Local profiles.** Validated without retuning against a fast-diving
  triple Langmuir probe, the same model gives the right orders of magnitude
  and trends but overestimates the peak $T_e$ (about 29 eV against about
  18 eV, read off Fig. 9), underestimates the near-plume density and places
  the acceleration region too far upstream; the authors list neutral
  back-ingestion, section averaging, the missing plume expansion, the
  calibration choices and the 1D treatment of an end-of-life magnetic
  topology as causes, and call the calibrated model an "extrapolator" of
  partial data rather than a predictive tool
  ([Giannetti et al. (2021)](/sources/giannetti-2021.md), §§4–5, Fig. 9).
* **Pressure trends.** After global calibration on SPT-100 data, the model
  predicts thrust falling with background pressure where the experiment
  shows it rising, over-predicts $I_d$ by more than 50 %, and gives ion
  velocity profiles whose acceleration region shifts too little and is
  not steep enough; under this anomalous-transport parameterization the
  authors judge the 1D model unlikely to capture the location and
  steepness of the acceleration region and the far-field asymptote
  simultaneously, and recommend a 2D model and a three-zone profile
  ([Eckels et al. (2024)](/sources/eckels-2024.md), Obs. 1–4, Fig. 7,
  pp. 15–18, 26–28). See [SPT-100](/benchmarks/spt-100.md).
* **Free parameters.** The model needs a prescribed axial
  $\alpha_{\mathrm B}(z)$ profile, a neutral speed and a wall or
  energy-loss coefficient. Current-only data do not identify the plume
  value of $\alpha_{\mathrm B}$
  ([Saravia et al. (2026)](/sources/saravia-2026.md), §6.2; see
  [Bayesian calibration](/methods/bayesian-calibration.md)).

# Citations

1. [Boyd (2005)](/sources/boyd-2005.md), §3.4, Fig. 14.
2. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §§2.1, 2.3, 3.4, Tab. I, eq. 30 (accepted manuscript).
3. [Giannetti et al. (2021)](/sources/giannetti-2021.md), §§2, 4–5, eqs. 1–23, App. A, Table 2, Fig. 9.
4. [Ahedo (2023)](/sources/ahedo-2023.md), eqs. 37–43, Fig. 3.
5. [Eckels et al. (2024)](/sources/eckels-2024.md), pp. 9–10, 15–18, 26–28, eqs. 4–6, 22.
6. [Saravia et al. (2026)](/sources/saravia-2026.md), §§2.1–2.3, 4.2, 6.2, eqs. 1–21, Table 1, Figs. 2, 13–14, App. A, footnote 1.
7. [Marks & Gorodetsky (2025)](/sources/marks-2025.md), model description (LANDMARK case 2a).

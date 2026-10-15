---
type: Source
title: "Semyonov (2018) — Pros and cons of relativistic interstellar flight"
description: "An essay-style perspective arguing that only antimatter-powered relativistic ion propulsion could take multi-ton rockets to 0.3–0.7c, evaluating the author's earlier relativistic rocket equation for speed and proper flight time, and weighing waste-heat rejection, interstellar gas and dust radiation hazards, modest time dilation and economics against it."
resource: "doi:10.1016/j.actaastro.2018.07.012"
source_kind: paper
authors: [Semyonov O.G.]
year: 2018
venue: "Acta Astronaut. 151:736–742"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Semyonov_Pros_and_cons_of_relativistic_interstellar_flight.pdf"
tags: [context, interstellar-flight, relativistic-rocket, antimatter, perspective]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

An essay-style perspective on whether crewed relativistic interstellar
flight is feasible. It argues that only antimatter (antihydrogen) has the
energy density to bring a multi-ton rocket above $0.1c$, and that
relativistic ion propulsion (linear ion accelerators powered by an
annihilation reactor) beats direct photon or meson propulsion by
annihilation products. With the author's earlier relativistic rocket
equation it plots achievable speed and proper flight time against the
ion exhaust velocity for 1000–10000 t rockets with 1–100 TW engines. The
"cons" are waste-heat rejection (radiator mass), the relativistic
headwind of interstellar gas (hard ionizing radiation, about $10^4$ rem/s
unshielded) and dust (mechanical damage), modest time dilation (Lorentz
factor at most 1.4 below $0.7c$), economics and psychology. It concludes
that robotic missions within the local low-density cavity are the
realistic hope, and it criticises gram-scale laser-sail probes. There is
no new simulation or experiment: the figures evaluate closed-form
formulas and repeat the author's earlier work.

Although the paper discusses ion acceleration as a propulsion principle,
it is a mission-feasibility essay with no thruster or plasma model, so
under the bundle's scope rule it earns no concept page.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Fuel energy densities** (§1, Table 1). Chemical, nuclear and
   thermonuclear fuels cannot bring a multi-ton rocket above $0.1c$;
   antimatter is the "ultimate fuel". Table 1 (MJ/kg): antimatter printed
   "89,900,000.000"; hydrogen fusion 650,000,000; D–T fusion 340,000,000;
   U-235 88,000,000; natural U 81,000,000; Pu-238 15,000,000; hydrogen
   burning 140; rocket chemical fuels 50; gasoline 44; coal 24; wood 16.
   Stated.
2. **Nuclear-electric baseline** (§1, attributed to the author's ref. [1]).
   A 100 t ion-thruster rocket with a nuclear reactor reaches 200–300 km/s
   in several months.
3. **Ion propulsion over photon or meson rockets** (§2, attributed).
   Photon and meson rockets are "hardly realizable" and have poor jet
   alignment because of the long annihilation zone; high-energy ion
   propulsion from linear accelerators gives better conversion efficiency
   and near-ideal jet alignment.
4. **Ion thrust** (§2). $F_i=N\gamma_im_i\beta_ic$ with $N$ ions per
   second; thrust grows as $\gamma_i\beta_i$, so less exhaust mass is
   needed. Stated (relativistic momentum flux).
5. **Non-relativistic estimate** (§2, Eq. 1, Fig. 1).
   $M/M_0=\exp\bigl(-\beta/(\beta_i\gamma_i)\bigr)$ as printed. For a 100 t
   rocket with a 600 MW reactor and 50% efficiency, the speed at
   $M/M_0=0.5$ rises to about 1000 km/s at $\beta_i=0.005$, and the time to
   $M/M_0=0.5$ for $M_0$ = 100, 200, 300 t rises to about 10 years near
   $\beta_i=0.01$ (read off the figures). Formula evaluation.
6. **Relativistic rocket equation** (§2, Eqs. 2–3, from the author's refs.
   [1, 4]), including the annihilation mass loss:
   $$\frac{M}{M_0}=\Bigl(\frac{1-\beta}{1+\beta}\Bigr)^{\frac{1+(\gamma_i-1)/\varepsilon}{2\gamma_i\beta_i}},\qquad \beta=\frac{1-(M/M_0)^{\eta}}{1+(M/M_0)^{\eta}},\quad \eta=\frac{2\gamma_i\beta_i}{1+(\gamma_i-1)/\varepsilon}.$$
7. **Proper time at constant thrust** (§2, Eq. 4). With constant total
   mass-loss rate (annihilation plus jet) and jet power $\varepsilon P$:
   $$\tau_a=\frac{M_0c^2(\gamma_i-1)}{P(\gamma_i-1+\varepsilon)}\Bigl[1-\Bigl(\frac{1-\beta_a}{1+\beta_a}\Bigr)^{\frac{1+(\gamma_i-1)/\varepsilon}{2\gamma_i\beta_i}}\Bigr].$$
   Reader's check: the bracket equals $1-a$ by Eq. 2 and the prefactor is
   $M_0$ over the total mass-loss rate
   $P/c^2+\varepsilon P/\bigl(c^2(\gamma_i-1)\bigr)$, so Eq. 4 is
   internally consistent.
8. **Optimal exhaust velocity** (Fig. 2a). The speed at $M/M_0=0.5$ and
   0.25 for $\varepsilon$ = 0.3, 0.5, 0.7 has an interior maximum in
   $\beta_i$; read off the figure, about 0.76 for $M/M_0=0.25$,
   $\varepsilon=0.7$ and about 0.46 for $M/M_0=0.5$, $\varepsilon=0.7$.
   Proper times (Figs. 2b–c) for $M_0$ = 1000 or 10000 t and 1–100 TW
   ($\varepsilon=0.5$) span about $10^{-4}$ to $10^4$ years. Formula
   evaluation.
9. **Reachability** (§2). Nearby stars within the local low-density
   cavity are reachable in years to tens of years of proper time if
   $M_0<10000$ t, dry mass below $0.25M_0$ and engine power well above
   1 TW. Stated from Fig. 2.
10. **Radiator** (§3.1, Eq. 5, attributed). Radiator mass
    $M_r=\rho S_r\delta=\rho\delta P_t(1-\varepsilon)/(\eta\sigma T^4)$
    with a Carnot-type limit $\varepsilon_t=(T_0-T)/T_0$; the radiator
    becomes unacceptably large above about 1 TW.
11. **Interstellar headwind** (§3.2, attributed). The local cavity is
    about 400 light-years across, gas concentration about 0.3 cm⁻³
    ($3\times10^5$ m⁻³), dust grains $10^{-5}$–$10^{-6}$ m of
    $10^{-17}$–$10^{-20}$ kg at $10^{-8}$ (low-density regions) to
    $10^{-5}$ m⁻³ (dense clouds). In the rocket frame hydrogen exceeds about
    100 MeV for $v>0.5c$; the flux $\gamma nv$ exceeds $10^9$ cm⁻² s⁻¹ for
    $v\ge0.3c$, with an unshielded dose rate of about $10^4$ rem/s.
12. **Doses and dust** (§3.2, Fig. 3). 5 rem is the official safe dose,
    $10^2$ rem dangerous, $10^3$ rem lethal; the lethal dose accumulates in
    a fraction of a second for $v\ge0.3c$. Dust bombards the front at more
    than 100 m⁻² s⁻¹ for $\beta>0.3$; the impact of relativistic
    multi-atomic grains on materials has never been studied. Stated.
13. **Conceptual rocket** (§3.2, Figs. 4–5). Ion accelerators, propellant
    tanks, refrigerators, turbines and generator, annihilation reactor,
    magnetic shield, electron stripper, heat radiator, antihydrogen tanks;
    instead of a 180° turnaround that would expose the rocket, the aft
    accelerators are rotated to point the braking jets forward at an angle.
    Proposed (sketch).
14. **Time dilation** (§3.3). Practical speed is below $0.7c$, so the
    Lorentz factor is at most 1.4; a planetary system at 39 ly takes 55
    years of cruise at $0.7c$ plus 5–10 years of acceleration and
    deceleration, about 40 years by the rocket clock. Stated (reader's
    check: 39/0.7 = 55.7 years, 55.7/1.40 = 39.8 years).
15. **Outlook** (§4). Robotic flights within the local cavity are the
    "only hope". Gram-scale laser-driven probes cannot brake, have
    difficult data return, and their electronics would degrade within
    hours in the relativistic gas and dust flux. The engine should be at
    most about half the dry mass; present power plants are below 10 GW,
    naval reactors below 1 GW at about 10–30 t; launch masses of
    1000–10000 t reach 0.3–$0.7c$ in years to tens of years with a
    10–100 TW engine. Stated.

# Methods

No simulation, experiment or numerical scheme. Closed-form expressions
are evaluated: Eq. 1 (a Tsiolkovsky form), Eqs. 2–4 (relativistic rocket
equation with annihilation mass loss and constant-thrust proper time,
from the author's earlier work), Eq. 5 (radiator mass), the
incoming-particle kinetic energy $m_0c^2(\gamma-1)$ and the flux
$\gamma nv$ (footnote 2 derives the factor $\gamma$ from the invariance of
the column density). Assumptions: constant mass-loss rate during
acceleration, reactor power converted to jet power with efficiency
$\varepsilon$, proton exhaust, annihilation fuel counted in the mass loss.
The dose-rate curve of Fig. 3 comes from the author's earlier work; its
model is not given here.

# Tests and results

* **Fig. 1a**: $M_0$ = 100 t, 600 MW, $\varepsilon$ = 50%, $M/M_0$ = 0.5,
  $\beta_i$ from 0.0001 to 0.005: speed from about 20 km/s to about
  1000 km/s (read off a log axis).
* **Fig. 1b**: time to $M/M_0$ = 0.5 against $\beta_i$ (axis to 0.010) for
  $M_0$ = 100, 200, 300 t: from about $10^{-3}$ years to about 10–20 years
  (read off the figure).
* **Fig. 2a**, peak $\beta$ (read off the figure): $M/M_0$ = 0.25: about
  0.76, 0.66, 0.52 for $\varepsilon$ = 0.7, 0.5, 0.3; $M/M_0$ = 0.5: about
  0.46, 0.40, 0.28.
* **Figs. 2b–c**: proper time to $M/M_0$ = 0.5 or 0.25 for 1000 t at 100,
  10, 1 TW and 10000 t at 100, 10, 1 TW ($\varepsilon$ = 0.5), on a log
  axis from about $10^{-4}$ to $10^4$ years.
* **Fig. 3**: unshielded dose rate ($10^2$–$10^5$ rem/s) and nucleon flux
  (linear axis to $4\times10^{14}$ m⁻² s⁻¹) against $\beta$; the dose curve
  has a knee near $\beta\approx0.6$, where the nucleon penetration depth
  exceeds the thickness of a human torso (caption).
* **§3.3**: 39 ly at $0.7c$: 55 years of cruise plus 5–10 years, about 40
  years of rocket time.

# Notation map

| Semyonov (2018) | Registry | Note |
|---|---|---|
| $F_i$ | $F$ | thrust |
| $N$ | words (ions per second; also the flux $\gamma nv$; $N_0$ a column density) | three meanings in the paper; not $N_{\mathrm{ppc}}$ |
| $m_i$ | $m_i$ | ion rest mass |
| $\beta$, $\beta_i$ | words (rocket and exhaust speeds over $c$) | |
| $\gamma$, $\gamma_i$ | words (Lorentz factors) | **collision:** registry $\gamma$ is the polytropic index |
| $c$ | $c$ | speed of light |
| $M_0$, $M$, $a$ | words (launch and instantaneous rocket mass, target mass ratio) | not the Alfvén Mach number $M_A$ |
| $\dot M$, $\dot M_{ann}$, $\dot M_{jet}$ | words; $\dot m$ for the jet part | total, annihilation and jet mass-loss rates |
| $\varepsilon$ | words (jet-power efficiency, $P_{jet}/P$) | close to but not the registry's thrust efficiency $\eta$; not $\varepsilon_0$ |
| $\varepsilon_t$ | words (Carnot-type efficiency limit) | |
| $\eta$ | words (exponent of Eq. 3; radiator emissivity in Eq. 5) | **collision:** registry $\eta$ is thrust efficiency; two meanings in the paper |
| $P$, $P_{jet}$, $P_t$, $P_{exh}$ | words (reactor power and its jet, thermal, exhaust parts) | registry $P$ is electric input power; here annihilation or nuclear power |
| $\tau$, $\tau_a$ | words (proper time) | |
| $\rho$, $\delta$, $S_r$, $M_r$ | words (radiator density, wall thickness, area, mass) | **collisions** with $\rho_c$ and $\delta_{\mathrm{SEE}}$ |
| $\sigma$ | words (Stefan–Boltzmann constant) | not a cross section $\sigma_{sk}$ |
| $T$, $T_0$ | words (radiator and turbine-inlet temperatures, kelvin) | not $T_s$ |
| $n$, $n'$ | words (interstellar gas concentration, rest and rocket frame) | a number density $n_s$ with the species unspecified |
| $E_k$, $m_0$ | words (kinetic energy and rest mass of an incoming particle) | |
| $L$, $L'$ | words (distance to the destination star) | registry $L$ is a domain length |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Semyonov_Pros_and_cons_of_relativistic_interstellar_flight.pdf`.
   * **Version.** Publisher's final typeset PDF (version of record), 7
     pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.07.012, printed on page 1
     and checked on Crossref: title, sole author, Acta Astronaut.
     151:736–742 match; published in print October 2018 (no
     published-online field on Crossref). Page 1 gives received 25 May
     2018, revised 29 Jun 2018, accepted 5 Jul 2018, online 6 Jul 2018.
     Page 1 matches the filename title.
   * **How it was read.** Full text layer; Eqs. 1–4, garbled in the text
     layer ("chi_i" for $\gamma_i$, a split fraction in Eq. 3), read from
     the rendered pages 2–3. Figure values are visual readings of log axes
     and approximate.
   * **Recorded as printed.**
     * §3.2: "$10^9$ per square centimeter per second ($10^{15}$ m⁻² s⁻¹)";
       $10^9$ cm⁻² s⁻¹ is $10^{13}$ m⁻² s⁻¹. Reader's check: with
       $n=3\times10^5$ m⁻³ and $v=0.3c$, $\gamma nv\approx2.8\times10^{13}$
       m⁻² s⁻¹, agreeing with the cm⁻² figure and the Fig. 3 flux curve;
       the parenthetical value is wrong by $10^2$.
     * Table 1 prints antimatter as "89,900,000.000 MJ/kg"
       ($8.99\times10^7$), below hydrogen fusion; the intended value is
       $c^2\approx8.99\times10^{10}$ MJ/kg (a decimal point for a thousands
       separator).
     * After Eq. 3: "$\gamma_b=(1-\beta_i^2)^{-1/2}$"; the subscript should
       be $i$.
     * $\eta$ denotes both the exponent of Eq. 3 and the emissivity of
       Eq. 5.
     * The Fig. 1 caption and text give $\beta_i$ from 0.0001 to 0.005; the
       Fig. 1b axis runs to 0.010.
     * Eq. 1, called non-relativistic, carries $\gamma_i$; for
       $\beta_i\le0.005$, $\gamma_i\approx1$ and it has no numerical effect.
     * §3.3 calls the Lorentz factor the "relativistic time contraction
       factor"; it is the time-dilation factor.
   * **Reference list.** 22 printed entries ([1]–[22]), matching the
     Crossref reference count. Ref. [13], printed "I. Mann, K. Hiroshi", is
     most likely Mann & Kimura (2000) with Kimura's given name and surname
     swapped (not verified). Ref. [22] prints no year outside its URL (URL
     date 2018-05-22). The Foley & Weed article (Discover, August 2003),
     cited in the text and the Fig. 4 caption, is not in the numbered list
     and so not in the bibliography.

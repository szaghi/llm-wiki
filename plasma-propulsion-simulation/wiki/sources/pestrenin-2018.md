---
type: Source
title: "Pestrenin et al. (2018) — Curing of large prepreg shell in solar synchronous Low Earth Orbit: Precession flight regimes"
description: "Models solar-only curing of a large inflatable epoxy/carbon prepreg shell in a 300 km orbit with fitted cure kinetics and transient ANSYS heat conduction, and finds that only a spin-plus-precession attitude regime brings every element above the 80 °C cure threshold, with full cure in about 4 weeks."
resource: "doi:10.1016/j.actaastro.2018.06.029"
source_kind: paper
authors: [Pestrenin V.M., Pestrenina I.V., Rusakov S.V., Kondyurin A.V.]
year: 2018
venue: "Acta Astronaut. 151:342–347"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Pestrenin_Curing_of_large_prepreg_shell_in_solar_synchronous_Low_Earth.pdf"
tags: [context, space-structures, inflatable-structures, composite-curing, thermal-analysis]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper models the in-orbit curing of a large inflatable cylindrical
shell with spherical end caps, made of epoxy/carbon-fibre prepreg
(CE 8201-200-45S, Comfiber), heated only by solar radiation in a 300 km
circular orbit whose plane is normal to the sunlight. The cure kinetics
are a law $d\eta/dt=B(1-\eta)^\alpha\exp(-A/T)$ fitted to the
manufacturer's isothermal cure data (80–160 °C). The temperature field
comes from transient finite-element heat conduction in ANSYS with
Stefan–Boltzmann exchange to a constant ambient temperature, inner
wall-to-wall re-radiation and a lumped energy balance of the filling
gas; the cure is advanced element by element with the closed-form
isothermal solution over each time step, above a threshold of 80 °C.
Three attitude regimes are compared: a fixed inclination of the axis to
the orbit tangent; the same plus spin about the axis; spin plus
precession of the axis about the tangent. Only the spin-plus-precession
regime with spin $0.0167\Omega$, precession $0.167\Omega$ and precession
angle $\pi/2$ brings every element above the threshold, and the whole
shell is estimated to cure in about 4 weeks.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Cure kinetics** (§2, Eqs. 1–2, attributed to Moskvitin 1972).
   $d\eta/dt=Q(\eta,T)$ with $Q=B(1-\eta)^\alpha\exp\{-A/T\}$,
   $0\le\alpha<1$; $A$ and $B$ constant, $\alpha$ a function of
   temperature.
2. **Isothermal solution** (§2, Eqs. 3–5). At fixed $T_i$,
   $d\eta/dt=b_i(1-\eta)^{\alpha_i}$ with $b_i=B\exp\{-A/T_i\}$, and for
   $\eta(0)=0$: $(1-\eta)^{1-\alpha_i}=(\alpha_i-1)\,b_i\,t+1$. Derived
   (consistent with Eq. 3 on the reader's check).
3. **Fitted parameters** (Table 1, Fig. 2). For $T_i$ = 80, 100, 120, 140,
   160 °C: $\alpha_i$ = 0.66, 0.58, 0.79, 0.84, 0.95; $b_i$ =
   $7.05\times10^{-5}$, $3.14\times10^{-4}$, $1.14\times10^{-3}$,
   $2.90\times10^{-3}$, $4.00\times10^{-3}$ (units not printed). Fig. 2
   shows "good agreement" with the manufacturer's curves (degree of cure
   0.78–1.0 against time in hours, read off Fig. 2); no error metric.
4. **Temperature law** (§2, Eqs. 6–7). $b(T)=B\exp\{-A/T\}$ with $A$, $B$
   from least squares on the $b_i$; the fitted $A$ and $B$ are not
   printed.
5. **Regime 1, fixed inclination** (§4.1, Tables 2–3). With thermal
   conductivity 0.66 W/(m K), external-surface maximum and minimum
   temperatures are 140–141 °C and −77 to −78 °C for inclinations 0–90°;
   with 0.25 W/(m K), 98–106 °C and −17 to −18 °C. Raising the ambient
   temperature from 100 to 210 K raises the maximum from 141 to 153 °C and
   the minimum from −77 to −43 °C (0.66 W/(m K)). Complete cure is not
   achieved: only part of the shell exceeds 80 °C. Shown (simulation).
6. **Regime 2, plus spin** (§4.2, Fig. 4). After a transient the
   temperature oscillates with the spin period; cylindrical-part points
   may reach 80 °C depending on the spin rate, but not all points of the
   spherical caps do; complete cure is not achieved.
7. **Regime 3a, spin and precession** (§4.3, Fig. 5). For spin and
   precession both $0.2\Omega$ and precession angle $\pi/12$, cure is
   "limited to 60% of all the finite elements".
8. **Regime 3b** (§4.3, Figs. 6–8). For spin $0.0167\Omega$, precession
   $0.167\Omega$ and angle $\pi/2$, all elements periodically reach the
   cure temperature; cure maps at 6, 20 and 44 h; full cure of the whole
   shell in "about 4 weeks". The cylinder length does not affect the
   temperature distribution in this regime (stated), so it suits longer
   shells.
9. **Untreated effects** (§4.3, §5). Vacuum outgassing of low-molecular
   resin components and cosmic radiation can disturb the cure; 4-week
   cure kinetics need testing under high vacuum and radiation. Stated,
   not modelled. Conclusion: full solar-only cure requires controlled
   motion such as precession with optimal parameters.

# Methods

* **Geometry** (§4): cylinder with spherical bottoms, radius 10 m,
  cylindrical length 20 m, wall thickness 0.01 m; $z$ along the shell axis
  (Fig. 3).
* **Orbit**: circular, 300 km, orbit plane fixed normal to the sunlight
  (Fig. 3); no eclipse in this geometry.
* **Material**: CE 8201-200-45S (E201 epoxy resin with 3K-200tex carbon
  fabric), transversely isotropic with direction-independent thermal
  properties; thermal conductivity 0.25 or 0.66 W/(m K), the latter used
  after §4.1. Heat capacity, absorptance, emissivity and density are not
  printed.
* **Thermal model**: Fourier conduction in the shell; absorbed part of the
  solar flux; Stefan–Boltzmann radiation to a constant ambient temperature
  that lumps planetary effects (100–210 K explored, 150 K used after §4.1);
  re-radiation between inner walls; air fill exchanging heat with the
  inner wall; gas convection and pressure-driven volume change neglected.
* **Numerics** (§3): transient FE heat conduction in ANSYS (element type,
  mesh and time step not printed). Per step: solve conduction; take each
  element's volume-averaged temperature, held at the mean of the two step
  values; advance the cure with Eq. 5, with no cure below 80 °C; update
  the gas temperature at constant mass and volume from $C_v\,dT=dq$
  (Eqs. 8–9); pressure from the ideal-gas law (Eq. 10). The local
  temperature settles after about five rotations (§4.1).

# Tests and results

* **Kinetic fit** (Table 1, Fig. 2): five isotherms, 80–160 °C;
  qualitative agreement only.
* **Regime 1** (Table 2), inclination 0°, 30°, 60°, 90°: 0.25 W/(m K): max
  106/102/100/98 °C, min −17/−17/−18/−18 °C; 0.66 W/(m K): max
  141/141/141/140 °C, min −77/−78/−78/−77 °C.
* **Regime 1** (Table 3), ambient 100/130/170/210 K: 0.25 W/(m K): max
  106/106/108/111 °C, min −17/−16/−13/−7 °C; 0.66 W/(m K): max
  141/143/147/153 °C, min −77/−73/−62/−43 °C. The text says the external
  temperature agrees with the balloon-satellite observations of its
  ref. [1], without numbers.
* **Regime 2** (Fig. 4, inclination 0): temperature histories over about
  30 h for points on the caps and the cylinder; periodic peaks reach
  roughly 70 °C on the plotted axis (read off the figure).
* **Regime 3a** (Fig. 5): at 20 h about 60% of elements have a degree of
  cure above 20%, about 57% above 40% and about 14% above 60% (read off
  the figure).
* **Regime 3b** (Figs. 6–8): temperature scale 293.4–360.8 K over one
  precession turn (Fig. 6); element temperatures and fractions of
  elements per cure level against time (Fig. 7); cure maps at 6, 20, 44 h
  (Fig. 8); full cure in about 4 weeks.

# Notation map

The paper is outside the bundle's domain; its symbols are kept in words.

| Pestrenin et al. (2018) | Registry | Note |
|---|---|---|
| $\eta$ | words (degree of cure) | **collision:** registry $\eta$ is thrust efficiency |
| $\alpha$ (Eq. 2, Table 1) | words (cure-kinetics exponent) | also the axis inclination in §4.1–4.2 (internal overload); not $\alpha_{\mathrm B}$, $\alpha_E$ |
| $\alpha$ (§4.1) | words (inclination of the shell axis to the orbit tangent) | see above |
| $A$, $B$, $b_i$, $b(T)$ | words (activation temperature, prefactor, isothermal rate) | **collision:** registry $\mathbf B$ is the magnetic field |
| $T$, $T_i$, $T^*$, $T_n^g$ | words (material temperature, cure threshold, gas temperature) | registry $T_s$ is a species temperature in energy units; here kelvin or °C |
| ᴂ | words (thermal conductivity) | |
| $C_v$, $q$, $Q$, $m$ | words (gas heat capacity, heat, rate function or heat amount, gas mass) | **collisions:** registry $q_s$, $m_s$ species charge and mass |
| $p_n$, $\rho$, $\mu$, $R$ (Eq. 10) | words (gas pressure, density, molar mass, gas constant) | **collisions:** $\mu_0$, $\rho_c$; $R$ is also the shell radius |
| $R$, $L$, $h$ | words (shell radius, cylinder length, wall thickness) | registry $L$ is a generic length, compatible |
| $\omega_1$, $\omega_2$, $\psi$ | words (spin rate, precession rate, precession angle) | registry $\omega$ is a mode angular frequency |
| $\Omega$ | words (undefined; presumably the orbital angular velocity) | **collision:** registry $\Omega_e$ is the electron Hall parameter |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Pestrenin_Curing_of_large_prepreg_shell_in_solar_synchronous_Low_Earth.pdf`.
   * **Version.** Publisher's final typeset PDF, 6 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.029, printed on page 1
     and checked on Crossref: title, the four authors, Acta Astronaut.
     151:342–347 match; published in print October 2018 (no
     published-online field on Crossref). Page 1 gives received 15 Jan
     2018, revised 21 May 2018, accepted 10 Jun 2018, online 23 Jun 2018.
     Page 1 matches the filename title.
   * **How it was read.** Full text layer; all equations legible on the
     rendered pages. Values from Figs. 4, 5 and 7 are read off the plots.
   * **Recorded as printed.**
     * Symbol overloads: $\alpha$ is the kinetic exponent (Eq. 2) and the
       axis inclination (§4.1); $Q$ the rate function (Eqs. 1–2) and a heat
       amount (Eq. 9); $R$ the gas constant (Eq. 10) and the shell radius
       (§4). $\Omega$ is never defined.
     * §4.3 says regime 3a cure "is limited to 60% of all the finite
       elements"; reader's check of Fig. 5: about 60% holds only for a
       degree of cure above 20%, about 14% exceed 60% at 20 h, and the
       curves are still rising at the end of the plot.
     * §4.2 says cylindrical-part points "may reach the threshold value"
       of 80 °C, but the Fig. 4b peaks are about 70 °C on its axis
       (reader's reading of the figure).
     * Reader's check of Table 1 with Eq. 5, assuming $b_i$ in s⁻¹ (units
       not printed): full-cure time $1/((1-\alpha_i)b_i)$ is about 11.6,
       2.1, 1.16, 0.60 and 1.39 h for 80…160 °C, non-monotonic at 160 °C
       (because $\alpha_i=0.95$), whereas Fig. 2 shows the 160 °C curve
       reaching about 1 within about 0.35 h. Reader's check: the tabulated
       $b_i$ follow Eq. 4 only roughly; the local Arrhenius slope
       $A=\Delta\ln b/\Delta(1/T)$ falls from about 9800 K (80–100 °C) to
       about 2900 K (140–160 °C), and the fitted $A$, $B$ are not reported; the
       non-monotonic $\alpha_i$ are not discussed.
     * The title says "solar synchronous", but the model is simply an
       orbit plane normal to the sunlight at 300 km; eclipse and
       sun-synchronous nodal precession are not discussed.
     * §3, step 3 contains a stray Cyrillic "в" ("time Δt в").
   * **Reference list.** 31 printed entries, matching the Crossref
     reference count.

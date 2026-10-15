---
type: Source
title: "Zhao et al. (2018) — Numerical study on separation shock characteristics of pyrotechnic separation nuts"
description: "Simulates the unlocking of a pyrotechnic separation nut in ANSYS/LS-dyna with ALE detonation products coupled to Lagrangian solids, validated by one shock-response-spectrum measurement within ±6 dB, and splits the separation shock into a pyrotechnic explosion shock and a strain-energy release shock whose strength rises with bolt prestress (80–240 MPa)."
resource: "doi:10.1016/j.actaastro.2018.07.040"
source_kind: paper
authors: [Zhao H., Liu W., Ding J., Sun Y., Li X., Liu Y.]
year: 2018
venue: "Acta Astronaut. 151:893–903"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Zhao_Numerical_study_on_separation_shock_characteristics_of_pyrot.pdf"
tags: [context, pyroshock, separation-mechanism, explicit-dynamics, shock-response-spectrum]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper builds a 3-D finite-element model of a pyrotechnic separation
nut (explosive, housing, separator, locking piston, threaded segments,
bolt) clamping an Al6061 structure board, and simulates the whole
unlocking sequence in ANSYS/LS-dyna. The TNT detonation products and
the air are Euler (ALE) elements coupled by fluid–structure interaction
to Lagrangian solids; the bolt prestress is applied by dynamic
relaxation. The model is accepted because the shock response spectrum
(SRS) measured at one point on the board lies within ±6 dB of the
simulated one (Fig. 6). The acceleration history at that point is split
at the "separation time" into a pyrotechnic explosion shock and a
strain-energy release shock. Five prestress levels (80–240 MPa) are
compared through two frequency-independent SRS ratios $E_r$, $M_r$ and
two influence coefficients $I_E$, $I_M$. The conclusions: prestress
strengthens all three shocks, the strain-energy release shock most;
the separation-shock SRS is the envelope of the two source SRSs; and
the explosion shock dominates in 100 Hz–10 kHz. The paper has no plasma
or propulsion content.

# Key claims

Symbols are the paper's own (see the notation map). All results are
from one simulation model.

1. **Two shock sources** (§4.1, Fig. 9, shown in simulation): a
   pyrotechnic explosion shock before the separation time and a
   strain-energy release shock after it; the latter mixes with the
   unattenuated tail of the explosion shock and is "simplified as"
   strain-energy release shock.
2. **Separation time** (§4.2, Fig. 10): the instant the axial stress of
   a board element near the bolt hole (No. 521028) drops to zero; it
   comes earlier as prestress increases, which the authors attribute
   (stated) to lower friction between the locking piston and the
   threaded segments.
3. **Unlocking timeline** (§3.1, Fig. 7): detonation at 0 μs; product gas
   reaches the separator at 40 μs, launching the explosion shockwave;
   housing cavity filled at 200 μs; locking piston at the unlock position
   at 400 μs; threaded segments fully open at 480 μs.
4. **Pressure below the separator** (§3.2, Fig. 8): the two near-centre
   air elements (No. 465255, 466935) peak above 30 MPa, the outer one
   (No. 496175) stays below 5 MPa before 200 μs; afterwards the
   pressures equalise. Hence the explosion shock comes from the pressure
   pulse on the separator within the circle projected by the housing
   channel, and the pressure after 200 μs drives separation.
5. **Separation shock against prestress** (§4.2, Fig. 11; reference SRS
   the 240 MPa case): $E_r$ rises roughly linearly from 0.7 to 0.74 below
   160 MPa while $M_r$ barely changes; above 160 MPa $E_r$ and $M_r$ rise
   by 24% and 13%. The explosion shock follows the same trend (Fig. 12).
6. **Strain-energy release shock against prestress** (Fig. 13): both
   coefficients "increase obviously with prestress by 65%, from 0.36 to
   1" (see Recorded as printed).
7. **Influence coefficients** (Eq. 11, Fig. 14): $I_E$ and $I_M$ of the
   strain-energy release shock are both about 0.7, larger than those of
   the separation and explosion shocks (values not tabulated).
8. **SRS envelope** (§4.4, Fig. 15, shown in simulation and argued from
   the SRS definition): because the two sources are sequential in time,
   the separation-shock SRS equals the pointwise maximum of the two
   source SRSs. In this model the explosion shock exceeds the
   strain-energy release shock in 100 Hz–10 kHz for every prestress, and
   the separation-shock SRS coincides with it.
9. **Shock reduction** (§4.4, Conclusion 4, recommendation, not tested):
   redesign the separator, use a milder explosive, lower the prestress
   while keeping adequate connection stiffness.
10. **Prestress from torque** (Eq. 3, citing [29]):
    $\sigma=4T/(\pi Kd^3)=240$ MPa with $T=65$ N·m, $K=0.2$,
    $d=1.2$ cm.
11. **Attributed** (§1): Silverman and O'Quinn [23] identified three
    shock sources in the SN9400 nut (explosive deflagration,
    strain-energy release, collisions of inner components); Wang et al.
    [25] found that the explosive amount mainly affects the explosive
    side and the preload the non-explosive side. The present model
    keeps only two sources.

# Methods

* Code: ANSYS/LS-dyna explicit dynamics; geometry in Pro/E, meshing in
  HyperMesh (§2.2, Fig. 2); hexahedral mesh (Fig. 3), element count not
  given.
* Detonation: ALE; detonation products and surrounding air as Euler
  elements, nut and board as Lagrange elements, FSI coupling (§2.4).
  Pure Lagrange (mesh distortion) and SPH (boundary particle leakage)
  are discussed and rejected (stated).
* Materials (§2.3, Table 1): board Al6061, linear elastic, density
  2.8 g/cm³, Young's modulus 0.68 Mbar, Poisson ratio 0.33. Nut
  (30CrMnSiNi2 steel), Johnson–Cook (Eq. 1),
  $\sigma_y=(A+B\varepsilon^n)\left(1+C\ln(\dot\varepsilon/\dot\varepsilon_0)\right)(1-T^{*m})$,
  $T^*=(T-T_0)/(T_m-T_0)$: density 7.83 g/cm³, shear modulus
  0.815 Mbar, $A=0.01532$ Mbar, $B=0.00786$ Mbar, $n=1.66$,
  $C=0.0157$, $m=0.93$, $\dot\varepsilon_0=0.01$ s⁻¹, $T_m=1485.39$ K,
  $T_0=298$ K [26,27].
* Explosive (§2.3, Eq. 2, Table 2), JWL equation of state
  $p=A\left(1-\frac{\omega}{R_1\gamma}\right)e^{-R_1\gamma}+B\left(1-\frac{\omega}{R_2\gamma}\right)e^{-R_2\gamma}+\frac{\omega E}{\gamma}$,
  $\gamma=V/V_0$ the relative volume. TNT: density 1.63 g/cm³,
  detonation speed 0.693 cm/μs, detonation pressure 0.21 Mbar,
  $E=0.06$ Mbar, $A=3.738$ Mbar, $B=0.03747$ Mbar, $R_1=4.15$,
  $R_2=0.9$, $\omega=0.35$ [28].
* Prestress (§2.5, Fig. 4): dynamic relaxation on a defined bolt
  section; four bolt elements (51434, 51425, 51415, 51406) converge to
  about 240 MPa within about 200 μs of relaxation time, the farthest
  (51406) slowest.
* Error estimate (§2.7, Eqs. 4–9, after Smirnov et al. [13,32]):
  one-dimensional relative error $S_1\approx(\Delta L/L_1)^{k+1}$
  (Eq. 4), uniform-grid form $S_1\approx(1/N_1)^{k+1}$ (Eq. 5),
  $S_{err}\approx\sum_{i=1}^{3}S_i$ (Eq. 6), total error
  $S_{tol}=S_{err}\sqrt n\le S^{max}$ (Eq. 7), so
  $n_{max}=(S^{max}/S_{err})^2=(1\%/2.7\times10^{-4})^2=1372$ (Eq. 8),
  reliability coefficient $R_s=n_{max}/n$ (Eq. 9). $S_{err}\approx2.7\times10^{-4}$
  is computed "from Fig. 3" ($k$ and $N_i$ not stated); $R_s=1.372$. The
  stated rationale: systematic error grows like $n$, stochastic error
  like $\sqrt n$; only the $\sqrt n$ law is used. No grid-convergence
  study.
* Experiment (§2.6, Figs. 5–6): separation-shock test with one
  accelerometer on the board; systematic error below 6% (error bars in
  Fig. 6); "Nyquist frequency" set to 100 kHz, Savitzky–Golay filter
  cutting at 50 kHz.
* SRS (§2.6): peak absolute acceleration of an array of single-degree-of-freedom
  oscillators under base excitation, by Smallwood's digital recursive
  filter [31]; damping not stated.
* Coefficients (Eqs. 10–11, after [25]):
  $E_r=\sum_{f=f_0}^{f_N}\mathrm{SRS}_a(f)/\sum_{f=f_0}^{f_N}\mathrm{SRS}_b(f)$,
  $M_r=\max\mathrm{SRS}_a(f)/\max\mathrm{SRS}_b(f)$, reference
  $\mathrm{SRS}_b$ the 240 MPa case;
  $I_E=(E_{r,max}-E_{r,min})/E_{r,max}$, $I_M$ likewise.

# Tests and results

| Case | Section / figure | Conditions | Result |
|---|---|---|---|
| Validation | §2.6, Fig. 6 | 240 MPa prestress (implied), SRS 100 Hz–10 kHz | measured SRS inside the ±6 dB band of the simulation |
| Dynamic relaxation | §2.5, Fig. 4 | target 240 MPa | bolt elements converge to the set value |
| Error budget | §2.7 | $S_{err}=2.7\times10^{-4}$, $S^{max}=1\%$ | $n_{max}=1372$, $R_s=1.372$ |
| Separation sequence | §3.1, Fig. 7 | baseline | milestones at 40, 200, 400, 480 μs |
| Pressure below separator | §3.2, Fig. 8 | air elements 465255, 466935, 496175 | above 30 MPa near the centre, below 5 MPa outside, before 200 μs |
| Prestress sweep | §4.2, Figs. 10–13 | 80, 120, 160, 200, 240 MPa | separation shock $E_r$ 0.70 → 0.74 up to 160 MPa, then +24% ($E_r$) and +13% ($M_r$); strain-energy shock coefficients 0.36 → 1 |
| Influence coefficients | §4.3, Fig. 14 | the three shocks | $I_E$, $I_M$ about 0.7 for the strain-energy shock, lower for the others |
| SRS envelope | §4.4, Fig. 15 | five prestress levels | separation-shock SRS = explosion-shock SRS in 100 Hz–10 kHz |

Read off Fig. 6 by the reader (not printed): the measurement lies below
the simulation at low frequency (about 100 g against 200 g at 100 Hz)
and above it near 2 kHz (about 6000 g against 2000 g, at the +6 dB
line).

# Notation map

The paper is explicit structural dynamics; none of its quantities has a
registry counterpart, apart from the cell-size analogy in Eq. 4.

| Zhao et al. (2018) | Registry | Note |
|---|---|---|
| $\gamma=V/V_0$ | words (JWL relative volume) | **collision:** registry $\gamma$ is the polytropic index / ratio of specific heats |
| $A$, $B$, $R_1$, $R_2$, $\omega$ (JWL) | words | **collision:** registry $\omega$ is a mode angular frequency |
| $A$, $B$, $C$, $n$, $m$ (Johnson–Cook) | words | $n$ **collides** with the density $n_s$; the paper reuses $A$, $B$ for JWL |
| $E$ | words (JWL internal energy, Eq. 2; Young's modulus, Table 1) | **collision** with the electric field $\mathbf E$; reused by the paper for two quantities |
| $T$, $T^*$, $T_m$, $T_0$ | words (temperature, homologous temperature, melting and room temperature, Eq. 1; torque, Eq. 3) | not $T_s$ (energy units); the paper reuses $T$ for torque |
| $\sigma$, $\sigma_y$, $\sigma_Y$ | words (stress) | **collision** with the cross section $\sigma_{sk}$ |
| $p$ | words (JWL pressure; detonation pressure) | not the species pressure $p_s$ |
| $D$, $\rho$, $G$, $\nu$ | words (detonation speed, density, shear modulus, Poisson ratio) | $\nu$ **collides** with the collision frequencies $\nu_{sk}$ |
| $\Delta L$, $L_1$ | $\Delta x$, $L$ | element size and domain length (Eq. 4) |
| $N_1$, $k$ | words (cells per direction; order of accuracy) | $k$ **collides** with the wavenumber $k$ |
| $n$ (Eqs. 7–9) | words (number of time steps) | **collision** with $n_s$ |
| $S_1$, $S_{err}$, $S_{tol}$, $S^{max}$, $R_s$ | words (error estimates, reliability coefficient) | **collision** with the shape function $S(\mathbf x)$ |
| $E_r$, $M_r$, $I_E$, $I_M$, SRS | words | |
| $K$, $d$ | words (torque coefficient, bolt diameter) | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Zhao_Numerical_study_on_separation_shock_characteristics_of_pyrot.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier), 11 pages
     (893–903).
   * **Identity.** doi:10.1016/j.actaastro.2018.07.040, printed on page 1
     and checked on Crossref: title, all six authors, Acta Astronaut.
     151:893–903 match; issue October 2018 (no published-online field on
     Crossref); page 1 gives received 5 Mar 2018, revised 23 Jun 2018,
     accepted 21 Jul 2018, online 24 Jul 2018. Page 1 matches the
     filename title.
   * **How it was read.** Text layer; Eqs. 1, 2, 10 and 11 read there
     (layout-garbled but unambiguous), Eqs. 3–9 checked on rendered pages
     4–6. Figs. 7, 8 and 10–15 were read from the text and, where needed,
     from rendered pages; the SRS curves of Figs. 11–15 were not
     digitised, and the bar values of Fig. 14 are not printed ("around
     0.7"). Mesh size, element count, time step, end time, SRS damping
     and accelerometer type are not stated.
   * **Recorded as printed.**
     * §2.7: the time-step count $n$ "is 10e3 which is less than the
       $n_{max}$" (1372); read literally $10^4>1372$, while
       $R_s=n_{max}/n=1.372$ implies $n=1000$, so "10e3" stands for
       $10^3$.
     * §2.7: "the value of $S_{err}$ is taken as 1%" contradicts the
       preceding sentence ($S^{max}$ user-defined, 1–5%) and Eq. 8, where
       1% is $S^{max}$ and $S_{err}=2.7\times10^{-4}$.
     * §2.7 calls $R_s$ "always large than 1" (sic); that holds only when the
       criterion $n\le n_{max}$ is met, a pass condition, not an identity.
     * The prose before Eq. 4 names the element size $L_0$; the formula
       uses $\Delta L$.
     * §4.2 (Fig. 13): "by 65%, from 0.36 to 1".
     * Reader's check: 0.36 → 1 is +178% relative to 0.36; $(1-0.36)/1=64\%$
       is the change relative to the maximum, the normalisation of Eq. 11,
       yet §4.3 reports $I_E\approx I_M\approx0.7$ for this shock. Text,
       Fig. 13 and Fig. 14 are not mutually consistent as printed.
     * Reader's check: Eq. 3,
       $4\times65/(\pi\times0.2\times0.012^3)=2.39\times10^8$ Pa,
       consistent with 240 MPa.
     * §4.4 asserts the envelope property as exact ("always equal"); for
       sequential excitations it holds only approximately, since an
       oscillator's response to the second pulse depends on the residual
       of the first, and §4.1 itself notes the post-separation signal
       contains an "incomplete attenuation part" of the explosion shock.
     * The two-source split folds any inner-component collision
       contribution, a third source per [23], into the strain-energy
       release shock without separating it.
     * Units printed "10 KHz", "100 KHz", "50 KHz".
   * **Reference list.** 32 printed entries ([1]–[32]), matching the
     Crossref reference count. Printed-form oddities kept: [9] author
     "D.U. S", [26] author "H.A.S. M" with no title, [20] author list
     printed twice, [28] "Univercity".

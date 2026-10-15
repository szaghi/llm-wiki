---
type: Source
title: "Ahmad et al. (2018) — An investigation of millimeter wave reflectarrays for small satellite platforms"
description: "Gives a closed-form coupled-resonator model of the reflection coefficient of a printed-patch reflectarray unit cell with fringing, surface-wave, conductor-loss and roughness corrections, proposes 3-bit phase quantization, and measures two 35x35-element 60 GHz reflectarrays (33.26 dBi at boresight, about 60% aperture efficiency)."
resource: "doi:10.1016/j.actaastro.2018.06.044"
source_kind: paper
authors: [Ahmad G., Brown T.W.C., Underwood C.I., Loh T.H.]
year: 2018
venue: "Acta Astronaut. 151:475–486"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Ahmad_An_investigation_of_millimeter_wave_reflectarrays_for_small.pdf"
tags: [context, antenna, reflectarray, millimeter-wave, small-satellite, communications]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

An antenna-design paper for small-satellite inter-satellite links at
millimetre wavelengths, with two contributions. First, a closed-form
model of the reflection coefficient (magnitude and phase) of a square or
rectangular printed-patch reflectarray unit cell: the cell is an RLC
resonator coupled to a dominant-mode waveguide (Haus's small-perturbation
coupled-resonator theory), with dielectric, conductor and external
quality factors; fringing fields, surface waves (through a radiated-wave
efficiency), finite metal conductivity and conductor surface roughness
are included. Second, 3-bit phase quantization (8 discrete unit-cell
lengths) to simplify fabrication of passive mm-wave reflectarrays. The
model selects the substrate (10 mil RO5880) and is compared with CST
Microwave Studio full-wave simulations of one cell. Two 35×35-element
(19λ) reflectarrays at 60 GHz, designed for 0° and 55° beam pointing,
were fabricated, simulated in CST and measured in an NPL anechoic
chamber: 33.26 dBi measured gain at boresight, about 60% aperture
efficiency. The paper has no plasma or electric-propulsion content.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Unit-cell reflection coefficient** (§2.2, Eqs. 2–3):
   $\Gamma=\dfrac{1/Q_{ext}-1/Q_o-2j(f-f_o)/f_o}{1/Q_{ext}+1/Q_o+2j(f-f_o)/f_o}$,
   $1/Q_o=1/Q_d+1/Q_c$; $Q_o$ carries conductor and dielectric losses,
   $Q_{ext}$ radiation including surface waves. The form is attributed to
   coupled-resonator theory (Haus 1984) and perturbation theory (Pozar);
   the extension to the reflectarray cell is the paper's own.
2. **Rough-conductor conductivity** (Eq. 4, attributed to refs. [37,38]):
   $\sigma_r=\sigma/[1+\frac2\pi\tan^{-1}\{1.4(R_{rms}/\delta_s)^2\}]^2$;
   for thin substrates ($h\ll\lambda_o$) $Q_c=h\sqrt{\pi\mu f_o\sigma_r}$.
3. **External Q** (Eqs. 5–8): $Q_{ext}$ follows from the cavity-model
   stored energy ($\mathrm{TM}^{010}$ mode) and the $\mathrm{TE}_{10}$
   waveguide radiated power, scaled by the radiated-wave efficiency
   $\eta_{rad}$, with fringing-corrected effective patch dimensions
   $W_{eff}$, $L_{eff}$. Stated: $Q_{ext}$ captures infinite-array mutual
   coupling through the waveguide's periodic boundary conditions.
4. **Reflection phase** (Eq. 9): the closed-form phase
   $\Phi_{res}(f,f_o)$ of Eq. 2; only the over-coupled condition
   $Q_{ext}<Q_o$ (zero reflection phase at resonance) is useful (stated).
   Phase is controlled by patch length through
   $f_1(L_o+\delta L_o)=f_oL_o=f_2(L_o-\delta L_o)$ (Eqs. 10–11).
5. **Substrate selection** (§3.1, Figs. 4–5, shown): lower $\varepsilon_r$
   and thinner substrates give higher $\eta_{rad}$ (curves for
   $\varepsilon_r=2.24$, 6.15, 10.2, 12.8); on RO5880
   ($\varepsilon_r=2.24$) at 60 GHz thicknesses below 2 mil behave
   anomalously (phase misbehaviour and/or excessive loss); thicker
   substrates reduce the reachable phase range; 10 mil RO5880 is chosen.
   Inside a metallic waveguide, surface waves appear to improve
   $|\Gamma|$ (Fig. 5a), which the paper flags as a single-cell artefact.
6. **Model vs CST, one cell** (§3.2, Figs. 6–8, shown): with the offsets
   removed, magnitude and phase "match very well"; the raw frequency
   offset is about 1.3 GHz, equivalent to a 100 μm length offset at
   60 GHz; small-perturbation theory "do[es] not correct the frequency"
   but predicts reflection loss accurately. One model evaluation takes
   96 μs on a desktop PC.
7. **3-bit phase quantization** (§4, Eq. 12): continuous phases are mapped
   onto 8 states (0, π/4, …, 7π/4). The 0.2 dB directivity reduction of
   3-bit quantization is attributed to the authors' earlier paper [49].
   Claimed (§6): phase quantization in passive mm-wave reflectarrays "is
   not considered in other works".
8. **Measured arrays** (§6, Table 2, shown): boresight array 34.55 dBi
   (CST) vs 33.26 dBi (measured), 3 dB beamwidth 2.9° vs 2.75°, 3 dB gain
   bandwidth 8.92 GHz vs 9.37 GHz; 55° design achieves 54.2°, 30.7 dBi vs
   31.39 dBi, 5.5° vs 5.06°, 3.26 GHz vs 3.51 GHz. Cross-polarization
   isolation better than 38 dB, feed-port reflection better than −20 dB.
   Gain-bandwidth falls as the beam is steered off boresight. Aperture
   efficiency 60% (Table 3), stated as comparable to parabolic reflectors.

# Methods

* **Array phasing** (Eq. 1, cited to ref. [16]): the standard
  reflectarray phase condition with the feed at $(0,0,F)$.
* **Unit-cell model:** waveguide-coupled RLC resonator (Fig. 3, Eqs. 2–9).
  The explicit forms of $Q_d$ (ref. [35]), $\eta_{rad}$ (refs. [39,40],
  Pozar's closed-form surface-wave loss), $\Delta W$, $\Delta L$ (refs.
  [44,45]) and $\varepsilon_{eff}$ (ref. [46], a Rogers design note) are
  taken from the literature and not printed.
* **Full-wave validation:** CST Microwave Studio; single cell as a square
  patch in a "WR15 square waveguide" of aperture $a\times a$, roughness as
  an impedance surface; full arrays with the CST time-domain solver. The
  run including feed flange and feed support took about 105 h on an HPC
  cluster; the full acrylic support could not be simulated.
* **Design** (Table 1): 10 mil RO5880, $\varepsilon_r=2.24$,
  $\tan\delta=0.004$; copper $t=17$ μm, $R_{rms}=0.3$ μm; 3-bit
  quantization; focal length $F=70$ mm; array side 94.5 mm; spacing
  2.7 mm; 35×35 cells; pointing 0° and 55°; LB-15-10-A feed horn;
  Tx–Rx distance 5 m.
* **Fabrication and measurement** (§5): photolithographic PCB on rigid
  back plates, acrylic feed support ($\varepsilon_r\approx3$); NPL
  anechoic chamber, HP/Agilent 85309A-based mm-wave system with an
  Agilent N5242A VNA receiver, IF 20 MHz, LO power 16 ± 2 dBm;
  three-antenna gain method; azimuth cuts at fixed elevation. CST results
  are at 60 GHz and measurements at 61.5 GHz; the CST curves are shifted by
  1.5 GHz for comparison, the shift attributed to the feed-horn phase
  centre and to fabrication.

# Tests and results

| # | Case (section) | Conditions | Result |
|---|---|---|---|
| 1 | Radiated-wave efficiency vs thickness (§3.1, Fig. 4a) | $\varepsilon_r=2.24$, 6.15, 10.2, 12.8; up to 20 mil; first surface-wave mode | falls with thickness and $\varepsilon_r$; about 0.83 at 20 mil for $\varepsilon_r=2.24$ (figure reading) |
| 2 | $\lvert\Gamma\rvert$ vs thickness, 60 GHz (§3.1, Fig. 4b) | RO5880; smooth, rough, rough + surface-wave models | anomalous below about 2 mil; roughness adds loss; surface-wave effect small at $\varepsilon_r=2.24$ |
| 3 | $\Gamma$ vs frequency, three thicknesses (§3.1, Fig. 5) | 3.76 mm square lattice, resonance at 60 GHz | thicker: less loss, smaller phase range; 10 mil chosen |
| 4 | Model vs CST, one cell (§3.2, Figs. 6–8) | 10 mil RO5880, WR15 | good match after offset removal; offset about 1.3 GHz (≈100 μm); model predicts slightly higher loss |
| 5 | 0° array (§6, Fig. 13a–b, Table 2) | 61.5 GHz measured / 60 GHz CST | 33.26 dBi, 2.75°, 9.37 GHz measured; feed flange costs 0.4 dB gain and raises sidelobes by 2 dB |
| 6 | 55° array (§6, Fig. 13c–d, Table 2) | same | 54.2° achieved; 31.39 dBi, 5.06°, 3.51 GHz measured; sidelobes match better (less blockage) |
| 7 | Literature comparison (§6, Table 3) | refs. [52], [53], [20], [54] | this work: 60 GHz, 19λ, 33.26 dBi, 3 dB bandwidth 15.6%, efficiency 60%, cross-pol 38 dB; ref. [20] (77 GHz, 39λ) called the fair comparison: 36 dBi, 1 dB bandwidth 2.5%, efficiency 27% |

# Notation map

The paper's symbols are those of antenna engineering; none has a
counterpart in this bundle's notation registry.

| Ahmad et al. (2018) | Registry | Note |
|---|---|---|
| $\Gamma$ | words (unit-cell reflection coefficient) | |
| $f$, $f_o$ | words (frequency, resonant frequency) | |
| $Q_o$, $Q_d$, $Q_c$, $Q_{ext}$ | words (quality factors) | |
| $\eta_{rad}$ | words (radiated-wave efficiency) | **collision:** registry $\eta$ is thrust efficiency |
| $\sigma$, $\sigma_r$ | words (metal conductivity, smooth and rough) | **collision:** registry $\sigma_{sk}$ is a cross section |
| $\delta_s$, $R_{rms}$ | words (skin depth, rms roughness) | |
| $\mu$ | words (permeability of the substrate) | **collision** with mobility $\mu_\perp$; registry $\mu_0$ is vacuum permeability |
| $h$, $\varepsilon_r$, $\varepsilon_{eff}$, $\tan\delta$ | words (substrate thickness, relative and effective permittivity, loss tangent) | |
| $W$, $L$, $W_{eff}$, $L_{eff}$, $\Delta W$, $\Delta L$ | words (patch dimensions, fringing extensions) | **collision:** registry $L$ is a domain length; $W$ is macroparticle weight |
| $a$, $b$ | words (waveguide aperture) | |
| $W_s$, $W_e$, $P_{rad}$, $A_{WG}$, $Z_{WG}$ | words (stored energy, radiated power, waveguide amplitude and impedance) | **collision:** registry $P$ is electric power |
| $\Phi_{res}$, $\Delta\Phi_Q$, $\Delta\Phi_C$, $\Delta\phi_{mn}$ | words (reflection and required phases) | **collision:** registry $\phi$ is the electrostatic potential |
| $F$, $k_o$, $\lambda_o$ | words (focal length, free-space wavenumber and wavelength) | **collision:** registry $F$ is thrust, $k$ a mode wavenumber |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Ahmad_An_investigation_of_millimeter_wave_reflectarrays_for_small.pdf`.
   * **Version.** Publisher's version of record (Elsevier typeset,
     © 2018 IAA), 12 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.044, printed on page 1
     and checked on Crossref (2026-10-15): title, four authors, Acta
     Astronaut. 151:475–486 match; issued and published-print 2018-10, no
     published-online field. Page 1: received 20 May 2018, revised 7 Jun
     2018, accepted 19 Jun 2018, online 22 Jun 2018. Page 1 matches the
     filename title.
   * **How it was read.** Full text layer; Eqs. 2–9 checked on rendered
     pages 3–4 and Eq. 12 on page 6; Eq. 1 read from the text layer (vector
     arrows garbled, structure clear). Values read from Figs. 4–8 and 13
     are approximate. The text layer shows blanks where $W_s$ should
     appear on p. 477; the rendered page is blank there too.
   * **Recorded as printed.**
     * §2.2 (p. 477): "$2\,\mu m\le\delta_s\le0.2\,\mu m$ in
       $1\,GHz\le f\le100\,GHz$": the bounds are reversed (copper skin
       depth is about 2.1 μm at 1 GHz and 0.21 μm at 100 GHz).
     * Eq. 12 (p. 6, checked on the rendered page): state 1 is
       $-9\pi/32\le\Delta\Phi_C\,\%\,2\pi<9\pi/32$ and state 2 runs from
       $9\pi/32$ to $3\pi/8$, while all other states are π/4 wide and
       centred on their phase (expected first bound ±π/8); since the
       modulo lies in $[0,2\pi)$ the negative lower bound is never reached
       and $[15\pi/8,2\pi)$ is assigned to no state.
     * The captions of Figs. 5–8 give a "3.76 mm square unit cell
       lattice", while Tables 1–2 give a 2.7 mm element spacing; the
       unit-cell analysis uses a different periodicity from the built
       arrays, without comment. Reader's check: the paper calls WR15 a
       "square waveguide" of aperture $a\times a$, whereas standard WR-15
       is rectangular (3.76 × 1.88 mm).
     * §4 says the quantization scheme is "presented in section 2.2"; it
       is in §4 (Eq. 12).
     * §6: "lower frequency bands which are much more robust to
       fabrication tolerances in comparison to lower frequency bands";
       the second "lower" should be "higher".
     * Reader's check: Table 3's 15.6% 3 dB bandwidth equals 9.37 GHz
       (measured, at 61.5 GHz) divided by 60 GHz (the CST frequency);
       Table 2 gives 14.9% (CST) and 15.2% (measured) with consistent
       frequencies.
     * In the 55° case the measured gain (31.39 dBi) exceeds CST
       (30.7 dBi), while at boresight it is 1.29 dB lower; not discussed.
     * Ref. [14] is printed "Appl. Phys. Rev. 9 (2018) 034021" with DOI
       10.1103/PhysRevApplied.9.034021, which is Phys. Rev. Applied.
     * The paper states no conflict with others' published work; Table 3
       comparisons are flagged as to be read with caution.
   * **Reference list.** 54 printed entries ([1]–[54]); Crossref's
     reference count is 53. Rogers Corporation notes (refs. [36], [46]),
     the Agilent note (ref. [50]) and the IEEE standard (ref. [51]) carry no
     author-year in print and are keyed accordingly.

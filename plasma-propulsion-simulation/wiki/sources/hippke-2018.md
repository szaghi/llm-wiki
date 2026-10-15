---
type: Source
title: "Hippke (2018) — Benchmarking information carriers"
description: "An order-of-magnitude comparison of candidate carriers for interstellar communication (photons, inscribed matter, charged, short-lived and hypothetical particles, gravitational waves, neutrinos) by energy per bit, speed, focusing, extinction and lensing, concluding that photons win by orders of magnitude for fast point-to-point links and inscribed matter when latency does not matter."
resource: "doi:10.1016/j.actaastro.2018.05.038"
source_kind: paper
authors: [Hippke M.]
year: 2018
venue: "Acta Astronaut. 151:53–62"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Hippke_Benchmarking_information_carriers.pdf"
tags: [context, seti, interstellar-communication, neutrinos, gravitational-lensing]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper compares candidate carriers for interstellar communication over
pc–kpc distances with photons: artificial occulters and megastructures,
inscribed matter (physical probes), charged particles, short-lived and
massive particles, hypothetical particles (axions, tachyons), gravitational
waves and neutrinos. The criteria are energy per bit, speed, beam width
(focusing), extinction, gravitational-lensing performance, difficulty and
cost (Table 1). The central argument concerns focusing: an accelerator beam
opens at an angle of about the inverse Lorentz factor, so a particle beam as
narrow as a diffraction-limited 1 m optic costs orders of magnitude more
energy (§3.5, §5.4). Photons beat every other carrier "by orders of
magnitude" for fast point-to-point links; inscribed-matter probes are more
energy-efficient when latency does not matter; for low-rate isotropic
beacons current knowledge does not decide (§7). A long subsection (§5.6)
estimates the Sun as a gravitational lens for neutrinos. Propulsion appears
only as an efficiency factor in Eq. 2 and in one sentence on station-keeping
thrust (§5.6.6).

# Key claims

Symbols are the paper's (see the notation map).

1. **Photon capacity benchmark** (Eq. 1, §1, attributed to the author's
   ref. [8]): $C_\gamma=(d/1\,\mathrm{pc})^{-2}(\lambda/1\,\mathrm{nm})^{-1}(D/1\,\mathrm m)^{4}$
   bits J⁻¹, for equal transmitter and receiver apertures $D$ and one bit
   per photon, "valid to within 10% neglecting losses and noise".
2. **Inscribed-matter capacity** (Eq. 2, §2.2, attributed to ref. [25]):
   $C_{\mathrm{matter}}=\eta\,S\,L^{-1}v^{-2}$ bits J⁻¹; with
   $S_{\mathrm{base}}=10^{23}$ bits g⁻¹ and $v=0.1c$, about $10^{11}$ bits
   J⁻¹. A photon link of equal efficiency at $d=1.3$ pc needs $D=1$ km at
   X-ray wavelengths (1000 km at 1 μm), with $D\propto d^{1/2}$ at fixed
   wavelength.
3. **Accelerator beam width** (Eqs. 3 and 5, attributed to ref. [58]):
   $\theta_{\mathrm{beam}}=1/\gamma\approx10^{-4}/E_\mu[\mathrm{TeV}]$, i.e.
   6° at GeV, 21 arcsec at TeV, 21 mas at PeV. Compared with
   $\theta_{\mathrm{optics}}=1.22\lambda/D_t$ for $D_t=1$ m, the paper finds
   equality at $\lambda=82$ nm (15 eV) and an energy penalty of
   $7\times10^{10}$ for the same beam width (§3.5, §5.4). Derived by
   order-of-magnitude arithmetic; see Recorded as printed.
4. **Particles** (§§3.1–3.5): charged particles lose direction in
   interstellar magnetic fields and are "not usable"; muons, taus and the
   Higgs decay too fast (year-long flight needs $O(10^4)$ EeV muons or
   $O(10^{12})$ EeV taus, above the Planck energy); neutrons at $O(100)$ TeV
   ($\gamma\approx10^5$) have a dilated lifetime of about 2.8 yr and are "the
   only realistic candidate" in that class, but energy-inefficient. Argued.
5. **Neutrino capacity** (Eq. 6, §5.4, PeV neutrinos):
   $C_\nu\approx10^{-10}(d/1\,\mathrm{pc})^{-2}(V/100\,\mathrm{km}^3)$ bits
   J⁻¹, $V$ the water or ice detector volume; at GeV the collector must be
   about three orders of magnitude larger. Stated without derivation.
6. **Flavour** (§5.5): oscillations randomize neutrino flavour beyond 42 au
   even at 6.3 PeV ($L/E\approx1000$ km GeV⁻¹ for order-unity oscillation
   probability), so the usable dimensions are arrival time, energy and
   particle/antiparticle.
7. **Solar neutrino lens** (§5.6, largely literature values recombined):
   minimum focal length $z_{0,\nu}=23.5\pm0.1$ au against
   $z_{0,\gamma}=R_\odot^2/(2r_g)\approx546$ au for photons; effective lens
   radius $0.024$–$0.17\,R_\odot$ (16,700–118,300 km); caustic 1–50 m wide;
   mass gain $R_{\mathrm{lens}}^2/R_{\mathrm{image}}^2\approx5\times10^{11}$–$6\times10^{16}$
   (§5.6.4); transmission cutoff near 100 GeV (§5.6.5); station-keeping
   force (Eq. 7) $F=GM_\odot m/z_0^2\approx0.01$ N for $m=1000$ kg at
   23.5 au; PSF (Eq. 8, from ref. [113])
   $\rho\approx4.5\,(\lambda/1\,\mu\mathrm m)(b/R_\odot)$ cm, about
   $10^{-11}$ m for $\lambda=10^{-15}$ m.
8. **Gravitational waves** (§4): amplitude falls as $1/d$, against $1/d^2$
   for electromagnetic flux; lensing needs $\lambda<r_g$, i.e. above
   $10^5$ Hz; Eq. 4 gives $\mu_{\max}=4\pi r_g/\lambda\approx12.57$ for
   $\lambda\approx r_g$, with strain amplified by $\sqrt{\mu}$; GWs are
   "energetically inefficient … except perhaps over the very largest
   distances".
9. **Hypothetical particles** (§3.4, §6.5): an isotropic galaxy-filling
   broadcast is prohibitive in any carrier because of the $kT\ln2$ minimum
   energy per bit (ref. [48]); axions would have zero extinction but need an
   exactly tuned receiver; it is "unlikely that any hypothetical particles
   exceeds keV photon performance by more than a factor of a few". Argued.
10. **Conclusion** (§7): with a preference for information, speed,
    simplicity and limited energy, photons win by orders of magnitude; if
    speed does not matter, inscribed-matter probes; low-rate isotropic
    beacons cannot be constrained.

# Methods

Qualitative and order-of-magnitude benchmarking: no simulation, experiment
or code. Formulas come from the author's arXiv series "Interstellar
Communication" (refs. [8–10, 25, 55, 78]) and from particle-physics and
lensing literature, evaluated at sample conditions. Table 1 uses keV
energy, a 1 m transmitter aperture and 1 pc distance; masses and lifetimes
from CODATA 2006 (ref. [43]). Communication categories (§2): I controls only
the energy output (a modulated Cepheid), II only the directivity (an
occulter), III both (a laser). §6 relaxes the assumptions one at a time
(little information, complicated technology, unlimited energy, no time
pressure, gaps in physics, several at once).

# Tests and results

Table 1 ("Carrier performance summary"), transcribed from the rendered
page 54, for keV energy, 1 m aperture, 1 pc; (!) marks the cells printed red
("problematic properties"), best-effort in the first four rows.

| Carrier | MeV/c² | Lifetime (s) | Velocity (c) | Charged | Beam angle (″) | Extinction | Lensing | Difficulty | Initial cost | Operational cost |
|---|---|---|---|---|---|---|---|---|---|---|
| Photon | 0 | stable | 1 | no | 10⁻⁴ | 0.001 | good | low | medium | medium |
| Neutrino | ≈0.001 | oscillations | ≲1 | no | 10⁶ (!) | ≈0 | very good | medium | high (!) | medium |
| Electron | 0.51 | >10³⁶ | 0.0630 (!) | yes (!) | 10⁶ | medium | medium | ≈1 (!) | medium | medium |
| Proton | 938.27 | >10³¹ | 0.0015 (!) | yes (!) | 10⁶ (!) | ≈1 (!) | very good | low | medium | medium |
| Neutron | 939.56 | 881.5 (!) | 0.0015 (!) | no | 10⁶ (!) | ≈1 (!) | very good | low | medium | medium |
| Muon | 105.66 | 10⁻⁶ (!) | 0.0044 (!) | yes (!) | 10⁶ (!) | ≈1 (!) | very good | low | high (!) | medium |
| Tau | 1776.82 | 10⁻¹³ (!) | 0.0011 (!) | yes (!) | 10⁶ (!) | ≈1 (!) | very good | low | high (!) | medium |
| Higgs | 1.25×10⁵ | 10⁻²² (!) | 10⁻⁶ (!) | no | 10⁶ (!) | ≈0 | very good | high (!) | high (!) | high (!) |
| Inscribed matter | >0 | >10¹³ | 0…1 | no | ≈0 | ≈0 | no | low | high (!) | zero |
| Occulter | >0 | >10¹³ | 1 | possible | 10³ (!) | 0.001 | unlikely | low | high (!) | very low |
| Gravitational wave | 0 | stable | 1 | no | 4π (!) | 0 | low | high (!) | high (!) | high (!) |
| Axion | ≈10⁻⁹ | stable | ≲1 | no | 10⁻⁴ | ≈0 | good | high (!) | unclear | unclear |
| Tachyon | unclear | stable | >1 | no | unclear | unclear | unclear | high (!) | unclear | unclear |

Worked numbers in the text: a probe at $0.01c$ takes 438 yr to the nearest
star (§2.2); Higgs at 125 GeV/c² and $10^{-22}$ s needs $O(10^{22})$ EeV for
interstellar range (§3.3); GZK limit above $10^{19}$ eV (§3.5); a black-hole
merger emits $10^{47}$ J in GWs, a type Ia supernova $10^{42}$ J in photons
and $10^{40}$ J in GWs (§4.2); Sgr A* with
$M_{bh}=(4.02\pm0.2)\times10^6\,M_\odot$ at $7.86\pm0.18$ kpc,
$r_g\approx1.21\times10^{10}$ m ≈ 0.08 au, apparent size ≈ 20.2 μas
(§4.3.1); reactors radiate about 4.5% of fission energy as antineutrinos
(45 MW from a GW reactor), peak near 4 MeV (§5.1.1); the cross-section
peaks near 6.3 PeV (Glashow resonance), where 1 km³ of water detects 1%
(§5.2); the Fermilab NuMI demonstration sent 0.1 bit/s through 240 m of rock
with a beam peaking near 3.2 GeV and 400 kW wall-plug power, and a
submarine link needs $10^{14}$ muon neutrinos per second at 150 GeV, i.e.
65 MW at 10% efficiency (§5.3); a 1 m neutrino detector at the solar focus
is equivalent to a 74.6 km photon aperture (§5.6.2); the neutrino beam is
$10^{10}$ times wider than a photon beam of the same energy (§5.7).

# Notation map

The paper's symbols are those of communication physics and relativity; none
has a registry counterpart except $c$.

| Hippke (2018) | Registry | Note |
|---|---|---|
| $C_\gamma$, $C_\nu$, $C_{\mathrm{matter}}$ | words (capacity, bits per joule) | |
| $d$ | words (transmitter–receiver distance) | registry $\mathbf d$ is observed data |
| $\lambda$ | $\lambda_w$ | wavelength |
| $D$, $D_t$, $D_r$ | words (aperture diameters) | |
| $\eta$ (Eq. 2) | words (propulsion efficiency for launch and deceleration) | **collision:** registry $\eta$ is the thrust efficiency |
| $S$, $S_{\mathrm{base}}$ | words (information density per unit mass) | **collision:** registry $S(\mathbf x)$ is the shape function, $S_j$ the Sobol' indices |
| $L$ (Eq. 2) | words (Lorentz factor) | **collision:** registry $L$ is a domain length; §5.5 reuses $L$ for distance travelled |
| $\gamma$ | words (Lorentz factor) | **collision:** registry $\gamma$ is the polytropic index |
| $v$ | words (probe speed) | |
| $\theta_{\mathrm{beam}}$, $\theta_{\mathrm{optics}}$ | words (beam opening angles) | **collision:** registry $\theta$ is the azimuthal coordinate |
| $E$, $E_\mu$ | words (particle energy) | **collision:** registry $\mathbf E$ is the electric field |
| $\mu$, $\mu_{\max}$ | words (lensing magnification) | **collision:** registry $\mu_\perp$, $\mu_\parallel$, $\mu_0$ |
| $r_g$ | words (Schwarzschild radius) | not the Larmor radius $r_L$ |
| $z$, $z_0$ | words (heliocentric distance, focal length) | **collision:** registry $z$ is the axial coordinate |
| $F$ (Eq. 7, §4.3.2) | words (gravitational force or acceleration) | **collision:** registry $F$ is thrust |
| $m$ (Eq. 7) | words (detector mass) | not a species mass $m_s$ |
| $\rho$ (Eq. 8) | words (PSF width) | not the charge density $\rho_c$ |
| $V$ (Eq. 6) | words (detector volume) | |
| $b$, $R_{\mathrm{lens}}$, $R_{\mathrm{image}}$, $R$ | words (impact parameter, lens and image radii, object distance) | |
| $c$ | $c$ | speed of light |
| $kT\ln2$ | $k_BT\ln2$ in words | the paper writes $k$ for $k_B$; $T$ here is a temperature |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Hippke_Benchmarking_information_carriers.pdf`.
   * **Version.** Publisher's version of record (Elsevier, © 2018 IAA),
     10 pages. Some sentences are in bold: reader highlights in this copy,
     not author emphasis.
   * **Identity.** doi:10.1016/j.actaastro.2018.05.038, printed on page 1
     and checked on Crossref: title, the single author (ORCID
     0000-0002-0794-6339), Acta Astronaut. 151:53–62 match; issued
     2018-10, no published-online field. Page 1: received 4 Apr 2018,
     revised 11 May 2018, accepted 18 May 2018, online 28 May 2018. Page 1
     matches the filename title. Of the two Hippke 2018 files in the
     archive this is the first in filename order, hence `hippke-2018`.
   * **How it was read.** Full text layer; Eqs. 1, 4, 6, 8 and the
     $\sqrt{\mu}$ of §4.3.1 are garbled there and were read on the rendered
     pages 53, 56, 57 and 58. Table 1 is an image, read on the rendered
     page 54; its numbers are clear, the red/black colour of the first four
     rows' cells is best-effort. Eq. 6 and the inscribed-matter result rest
     on the cited preprints.
   * **Recorded as printed.**
     * Reader's check (§2.2): at fixed capacity Eq. 1 gives
       $D\propto\lambda^{1/4}$, so 1 km at 1 nm becomes about 5.6 km at
       1 μm, not the printed 1000 km; the companion paper
       ([hippke-2018-b](/sources/hippke-2018-b.md), §5.1) prints a factor of
       10 for optical and 100 for 0.1 m microwaves.
     * Reader's check (§3.5, §5.4): for $D_t=1$ m, $1.22\lambda/D_t$ equals
       the TeV beam's $10^{-4}$ rad at $\lambda\approx82$ μm, not 82 nm; at
       82 nm the optic gives about $10^{-7}$ rad, the PeV beam. The printed
       factor $7\times10^{10}$ is TeV/15 eV, pairing the TeV energy with the
       photon energy of the PeV-beam match; a consistent pairing gives about
       $7\times10^{13}$. The qualitative conclusion only strengthens.
     * Reader's check (§5.1.2): $2\times10^{16}$ J is about
       $1.25\times10^{35}$ eV, not the printed ≈$10^{38}$ eV; at 10 MeV per
       neutrino that is about $10^{28}$ particles, not $10^{31}$; even with
       $10^{31}$ the isotropic flux at 1.3 pc is about
       $5\times10^{-4}$ m⁻², not the printed $6\times10^{-10}$ m⁻². The
       printed chain does not reproduce.
     * Reader's check (§5.6.4 vs §5.7):
       $(16{,}700/0.025)^2\approx4.5\times10^{11}$ matches the printed
       lower bound, but $(118{,}300/0.005)^2\approx5.6\times10^{14}$, not
       $6\times10^{16}$; §5.7 restates the range as $10^{11}$–$10^{16}$.
       §5.6.4 calls $R_{\mathrm{image}}$ a "(diameter)" but uses it in a
       radius ratio.
     * Reader's check (§4.3.2): 1 gee at 621 $r_g$ (49.3 au) scaled as
       $r^{-2}$ gives about $3.9\times10^5$ gee at $r_g$, not the printed
       $4\times10^6$ gee, which is close to the value in m s⁻²
       (≈$3.7\times10^6$): a likely units slip.
     * Reader's check (§4.3.1): "a useful gain of $10^4$ for frequencies
       of $10^5$ Hz following eq. (4)" does not reproduce; Eq. 4 with
       $r_g=1.21\times10^{10}$ m and $\lambda=3$ km gives
       $\mu_{\max}\approx5\times10^7$.
     * Eq. 2 uses $S$, the text defines and evaluates $S_{\mathrm{base}}$;
       $L$ is called the Lorentz factor while §3.2 and Eq. 3 use $\gamma$
       for it, and §5.5 uses $L$ for distance.
     * Eq. 3 is introduced in the neutron assessment (§3.5) but defines
       $\gamma$ as "the relativistic boost factor of a muon"; copied
       verbatim into §5.4.
     * Table 1, Electron row: "Difficulty ≈ 1" in a categorical column,
       apparently shifted from Extinction.
     * §5.6.6: "Even the smallest rocket engines have kN thrust, so that
       station keeping appears trivial." Reader's check: electric (ion,
       Hall), cold-gas and other micropropulsion systems deliver μN–N
       thrust, so the premise is wrong as stated; the required 0.01 N lies
       within their range and the conclusion survives. This is the paper's
       only propulsion statement.
     * §2.3 cites "[43]" (CODATA 2006 constants) for "targeted
       communication with high data rates".
     * §5.1.3, "Muons decay after 2.2 μs (ms at GeV energies)". Reader's
       check: at 1 GeV, $\gamma\approx10$ gives about 20 μs; ms needs about
       50 GeV.
     * The paper sets the superluminal-GW claims of refs. [70,71] against
       the LIGO/Fermi coincidence of about 1.7 s (ref. [72]) and sides with
       GW speed ≈ $c$.
   * **Reference list.** 127 printed entries ([1]–[127]), matching the
     Crossref reference count. Ref. [10] (Hippke, "Interstellar
     Communication. VIII. Hard limits on the number of bits per photon",
     arXiv, 2018) has the same author and year as this source and is a
     different work from the archive's second Hippke 2018 paper; ref. [25]
     (Hippke, Leyland & Learned, "Interstellar Communication. VII.
     Benchmarking Inscribed Matter Probes", arXiv, December 2017) carries
     the title and authors of that second paper. DOIs are kept only where
     printed ([38], [61] inside an APS URL, [120]). Printed oddities kept:
     "Appl. Surf. Sci." for refs. [19] and [77]; "R. von Eshleman" (ref.
     [81]); broken superscript markup in the ref. [53] title; "4x19eV" in
     the ref. [67] title; "Proceedings of the SPIEE" (ref. [3]); "Optic
     Lett." (ref. [62]).

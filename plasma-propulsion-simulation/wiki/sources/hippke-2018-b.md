---
type: Source
title: "Hippke, Leyland & Learned (2018) — Benchmarking inscribed matter probes"
description: "Order-of-magnitude estimates showing that shielding of a data-carrying interstellar probe adds negligible mass below 0.2c, adopting a storage density of 1e23 bits per gram, and comparing the resulting 1e11 bits per joule at 0.1c with photon links, whose capacity falls as the inverse square of distance unless receivers sit at stellar gravitational lenses."
resource: "doi:10.1016/j.actaastro.2018.05.037"
source_kind: paper
authors: [Hippke M., Leyland P., Learned J.G.]
year: 2018
venue: "Acta Astronaut. 151:32–36"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Hippke_Benchmarking_inscribed_matter_probes.pdf"
tags: [context, seti, interstellar-communication, interstellar-flight]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper compares two ways of sending information between stars: physical
probes carrying data written into matter ("inscribed matter") and photon
beams, by bits per joule, bandwidth and latency. §2 estimates the shielding
a probe needs against interstellar dust and gas, cosmic rays and radiation
damage, and finds the shield mass negligible below $0.2c$ (about $10^{-4}$
to $10^{-2}$ of the payload mass). §3 sets the storage density (Bekenstein
bound, DNA, proteins, and a perfluorinated carbon "tape" storing one trit
per carbon atom) and adopts $10^{23}$ bits g⁻¹. §§4–5 take the kinetic
energy, counted twice for launch and deceleration, as the energy cost,
which gives about $10^{11}$ bits J⁻¹ at $0.1c$, and compare it with the
photon capacity of the authors' earlier work. The probe's advantage grows
with distance because beam capacity falls as the inverse square of
distance; receivers at stellar gravitational lenses restore the photon
advantage out to kpc distances. Propulsion is not modelled: it enters only
as an efficiency factor and through the Breakthrough Starshot example.

# Key claims

Symbols are the paper's (see the notation map).

1. **Shielding** (abstract, §2, §2.6): below $0.2c$, shielding against dust
   and radiation and data duplication add negligible mass: about $10^{-4}$
   of the payload for a 1:15,000 rod, about $10^{-2}$ for a 1:100 aspect
   ratio. An estimate built from cited erosion and penetration data.
2. **Front-shield rule** (§2.1, from the erosion figures of refs. [16,17]):
   a thickness of order $(1+0.1d)$ cm, $d$ the travel distance in pc, at
   $v=0.1c$. A proposed design rule.
3. **Cosmic rays** (§§2.3–2.4): a flux of about 11 cm⁻² s⁻¹ of about 1 GeV
   nucleons (ref. [17]), of which a fraction $P\approx0.1$ makes primary
   recoils, gives about 3.3 s⁻¹ cm⁻³, about $10^8$ cascades per cm³ per year
   and fewer than $10^{11}$ displaced atoms per year out of $10^{23}$ atoms
   cm⁻³; mass is better spent on error correction than on cosmic-ray
   shielding. Order-of-magnitude estimate.
4. **Storage densities** (§§3.1–3.3): Bekenstein bound
   $2\times10^{39}$ bits g⁻¹; single-electron solid state
   $3\times10^{38}$ (ref. [38]); DNA $5\times10^{20}$ (ref. [26]); proteins
   $2\times10^{21}$ (ref. [39]); hard disks $10^{18}$; perfluorocarbon tape
   $S_{\mathrm{chem}}=6\times10^{23}$ bits g⁻¹. Adopted
   $S_{\mathrm{base}}=10^{23}$ bits g⁻¹, allowing a payload fraction of about
   20%.
5. **Probe capacity** (§4.2, Eqs. 1–3):
   $C_{\mathrm{rel}}=\eta\,S\,L^{-1}v^{-2}$ bits J⁻¹, with
   $L=1/\sqrt{1-v^2/c^2}$ and $E_{\mathrm{kin}}=\tfrac12mv^2$; about
   $10^{11}$ bits J⁻¹ at $v=0.1c$ with $S_{\mathrm{base}}$ ($L=1.005$
   neglected).
6. **Photon link** (§5.1, Eqs. 4–5, from ref. [2]): received photon rate
   $\gamma\sim(d/1\,\mathrm{pc})^{-2}(D_t/1\,\mathrm m)^2(D_r/1\,\mathrm m)^2(P/1\,\mathrm W)$
   s⁻¹; with one bit per photon (ref. [52]) and $D=D_t=D_r$,
   $C_\gamma=\eta\,(d/1\,\mathrm{pc})^{-2}(\lambda/1\,\mathrm{nm})^{-1}(D/1\,\mathrm m)^4$
   bits J⁻¹. Matching $10^{11}$ bits J⁻¹ at $d=1.3$ pc needs $D=1$ km for
   X-rays, ten times larger for optical (μm) and a hundred times larger for
   microwaves (0.1 m); $D\propto d^{1/2}$ gives 3, 9 and 27 km at 10, 100
   and 1,000 pc.
7. **Slow probes** (§5.1): for $v\ll0.01c$ inscribed matter is more
   energy-efficient by many orders of magnitude.
8. **Gravitational lenses** (§5.3): with metre-scale telescopes at the
   gravitational lenses of both stars (equivalent to a 75 km aperture on the
   receiving legs, ref. [53]), photons beat a $0.1c$ probe over 1.3 pc and
   reach parity at kpc distances.
9. **Latency and range** (§6): at $0.1c$ the latency is about ten times that
   of photons; inscribed matter is favourable for more than $10^{23}$ bits
   sent over centuries; durability limits travel times to about $10^6$ yr,
   enough for the Galaxy at $0.1c$ but not for intergalactic distances.

# Methods

Analytic, order-of-magnitude estimates; no simulation, code or experiment of
the authors' own. Inputs are cited: erosion (refs. [16–22]), cosmic-ray flux
(ref. [17]), CH₂ shielding (ref. [23]), displacement cascades (ref. [24]),
DNA durability (refs. [26–33]). Energy model: non-relativistic kinetic
energy (Eq. 2), counted twice, with a propulsion efficiency $\eta$ and a
Lorentz-factor correction $L$ (Eqs. 1, 3). Photon model: the received photon
rate of ref. [2] (Eq. 4) at one bit per photon (Eq. 5). Encoding (§3.3): a
carbon chain with two univalent radicals per carbon and three
distinguishable substitution patterns, storing $\log_2 3\approx1.6$ bits per
carbon (one trit); 15 amu per trit for H/D, 28 amu for H/CH₃, 100 amu for
the fluorinated variant. Propulsion context only: the Breakthrough Starshot
laser sail (refs. [41,51]; 1 g, $0.2c$, 100 GW laser, 10 km aperture) and
photogravimagnetic sail deceleration (refs. [42–44]).

# Tests and results

No numerical tests; worked cases only. Dust erosion of 0.1 mm (0.5 mm) of
quartz per pc at $0.1c$ ($0.2c$), proton penetration of 3 mm in quartz or
graphite at $0.2c$ and 10 mm of titanium at $0.1c$ (§2.1, refs. [16,17]);
side erosion of 22 μm per $10^6$ yr for iron meteorites in the solar system,
six orders lower in interstellar space, and a design wall of 150 μm Al
lasting $10^5$ yr at $10^{-9}$ m yr⁻¹ (§2.2); CH₂ (0.94 g cm⁻³) stops 10% of
particles at 3 cm and 30% at 10 cm (§2.3); DNA half-lives on board of
$10^5$–$10^6$ yr (§2.5); a graphite probe (2.2 g cm⁻³, radius 1 cm) to
Alpha Centauri at $0.1c$ needs a front shield
$M_{\mathrm{front}}=\pi r^2\rho(1+0.1d)$ g ≈ 9 g, an equal side shield
implying a 150 m rod, a total shield of about 18 g, a volume of about
$5\times10^4$ cm³ and a payload of about 26 kg (§2.6); 1 g at $0.2c$ reaches
Alpha Centauri in about 20 yr, i.e. $10^{18}$ bits in 20 yr, about $10^9$
bit/s (§4.1); Lorentz-factor errors of about 5%, 15% and 100% at $0.3c$,
$0.5c$ and $0.9c$ (§4.2); the Starshot laser equivalently sends 100 g at
$0.002c$, reaching Alpha Centauri in 2,000 yr (§5.2); launching 1 g with
$10^{23}$ bits to $0.2c$ takes about 2 minutes (§5.4).

# Notation map

| Hippke et al. (2018) | Registry | Note |
|---|---|---|
| $v$ | words (probe speed) | |
| $c$ | $c$ | speed of light |
| $L$ | words (Lorentz factor) | **collision:** registry $L$ is a domain or channel length |
| $\eta$ | words (propulsion efficiency for launch plus deceleration) | **collision:** registry $\eta$ is the thrust efficiency |
| $P$ (§5.1) | words (transmitter power) | same kind as the registry's electric power $P$, kept in words |
| $P$ (§2.4) | words (fraction of cosmic rays producing primary recoils) | **collision** with the registry's power $P$; **internal collision** with §5.1 |
| $\gamma$ | words (received photon rate, s⁻¹) | **collision:** registry $\gamma$ is the polytropic index |
| $\lambda$ | $\lambda_w$ | wavelength |
| $d$ | words (distance, pc) | registry $\mathbf d$ is observed data |
| $D$, $D_t$, $D_r$ | words (apertures) | |
| $m$, $E_{\mathrm{kin}}$ | words (probe mass, kinetic energy) | not a species mass $m_s$; not the electric field |
| $S$, $S_{\mathrm{base}}$, $S_{\mathrm{chem}}$, $S_{BH}$, $S_{SS}$ | words (information density, bits g⁻¹) | **collision:** registry $S(\mathbf x)$ shape function, $S_j$ Sobol' indices |
| $C_{\mathrm{rel}}$, $C_\gamma$ | words (capacity, bits J⁻¹) | |
| $F_{\mathrm{nucleons}}$ | words (cosmic-ray nucleon flux) | **collision** with the registry's thrust $F$ |
| $\rho$, $r$, $h$, $M_{\mathrm{front}}$ | words (material density, probe radius and length, front-shield mass) | $\rho$ is not $\rho_c$; $r$ is not the radial coordinate |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Hippke_Benchmarking_inscribed_matter_probes.pdf`.
   * **Version.** Publisher's typeset version (Elsevier, © 2018 IAA),
     5 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.05.037, printed on page 1
     and checked on Crossref: title, the three authors, Acta Astronaut.
     151:32–36 match; issued 2018-10, no published-online field. Page 1:
     received 4 Apr 2018, revised 9 May 2018, accepted 18 May 2018, online
     28 May 2018. Page 1 matches the filename title. Second of the two
     Hippke 2018 files in archive-filename order, hence the suffix `-b`.
     The arXiv preprint "Interstellar Communication. VII. Benchmarking
     Inscribed Matter Probes" (Hippke, Leyland & Learned, December 2017)
     carries the same title and authors; the bibliography keeps it as the
     distinct entry `hippke-2017-f`, which hippke-2018 cites.
   * **How it was read.** Full text layer; Eqs. 1–5 checked on the
     rendered pages 34–35. Nothing illegible.
   * **Recorded as printed.**
     * Reader's check (§3.3): at 100 amu per trit (1.6 bits), 1 g holds
       about $6\times10^{21}$ trits, about $10^{22}$ bits; the printed
       $S_{\mathrm{chem}}=6\times10^{23}$ bits g⁻¹ corresponds to 1 amu per
       bit, about 60 times what the stated encoding gives (even 15 amu per
       trit gives about $6\times10^{22}$ bits g⁻¹). The adopted
       $S_{\mathrm{base}}$ inherits the excess.
     * §3.3 prints "35 × log2(23) ≈ 7.7 a.m.u per bit"; $35/\log_2 23\approx7.7$
       is meant. The "23 states" count is not derived.
     * Reader's check (§3.3): the "100 a.m.u per tit" of the fluorinated
       variant is reproduced by F/CF₃ substituents, not by F/CH₃ (46 amu);
       the text says only that hydrogen is replaced by fluorine.
     * §3.3: "A short tape might then be:" is followed by no example on the
       rendered page 34; the illustration is missing from the print.
     * Reader's check (§2.6): $5\times10^4$ cm³ at 2.2 g cm⁻³ is about
       110 kg, not the printed "~26 kg"; the shield-to-payload ratio is then
       about $1.6\times10^{-4}$, still "≈$10^{-4}$". The 1:15,000 aspect
       ratio is length over radius (150 m / 1 cm).
     * Reader's check (§2.2): the design erosion rate $10^{-9}$ m yr⁻¹ is
       about 45 times the quoted solar-system rate
       ($2.2\times10^{-11}$ m yr⁻¹) and further above the interstellar one;
       its origin is not stated (conservative but inconsistent with the
       cited data).
     * §2.3: "At low Lorentz factors (< 0.3)" means $v<0.3c$; a Lorentz
       factor is never below 1.
     * §1: "0.01 c takes 438 years to the nearest star, Proxima"; reader's
       check: about 4.24 ly gives about 424 yr.
     * §2.1 prints "v = 0.995" without $c$; §4 and §5.1 print "λ= nm" and
       "λ≈ nm" without a number (presumably 1 nm, the keV optimum of ref.
       [2]).
     * Eq. 3 applies $L^{-1}$ as a multiplicative correction to
       $\tfrac12mv^2$ rather than using the relativistic kinetic energy;
       negligible near $0.1c$.
     * Footnote 1: "within 27 years" from 1989 to the 2018 paper is 29
       years. The footnote's floppy-disk example: 1,474,560 bytes in
       27.918 cm³, 27.16 million floppies in a 750 m³ road train,
       $4\times10^{13}$ bytes = 40 TB.
     * §3.3: "As Richard [45] noted" cites R.P. Feynman by his first name.
   * **Reference list.** 56 printed entries ([1]–[56]), matching the
     Crossref reference count. The paper builds on its authors' own series
     (refs. [2], [52], [53]).

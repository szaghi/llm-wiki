---
type: Source
title: "Haley et al. (2018) — Massive scale, long battery life, direct to orbit connectivity for the internet of things"
description: "An industrial overview of the Myriota direct-to-orbit IoT platform (uncoordinated VHF uplink from low-power terminals to LEO satellites that store sampled spectrum for a cloud multiuser receiver), with a livestock water-tank pilot, field SNR statistics and model-predicted battery life; no propulsion or plasma content."
resource: "doi:10.1016/j.actaastro.2018.06.035"
source_kind: paper
authors: [Haley D., Beck A., Pollok A., Grant A., McKilliam R.]
year: 2018
venue: "Acta Astronaut. 151:318–323"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Haley_Massive_scale_long_battery_life_direct_to_orbit_connectivity.pdf"
tags: [context, satellite-communications, internet-of-things, nanosatellites]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

An industrial overview, by Myriota Pty Ltd (Adelaide), of a direct-to-orbit
connectivity platform for the internet of things. Small low-power terminals
send short, uncoordinated VHF messages straight to exactEarth's LEO
constellation; the satellites sample and store the spectrum and downlink it
over S band, and a cloud-hosted multiuser receiver decodes the stored
samples. The paper describes the architecture (§3), a livestock water-tank
monitoring pilot in Australia (§4), field results on decoding weak and
interfered signals (§5) and battery-life predictions (§6). It has no
equations and no analysis; the receiver design is deferred to ref. [7].
There is nothing on propulsion, plasma or numerical modelling.

# Key claims

1. **Market** (§1, attributed to refs. [1,2]): IoT is expected to become
   the largest category of connected devices in 2018; 27 billion connected
   devices are forecast by 2025, 11% of them LPWA. Terrestrial LPWA cannot
   cover the globe economically, and existing direct satellite-to-device
   links do not meet IoT cost, power and maintenance needs (ref. [4]).
2. **Heritage** (§2, refs. [5,6]): the 2011–2013 GSN project (AUD 12
   million, ITR at the University of South Australia, Australian Space
   Research Program) produced a Phase A study, a communication-system design
   and ten patent filings, validated in LEO trials in Australia and Canada
   with exactView-1 and NTS.
3. **Terminal** (§§3.1–3.2, Fig. 2): 57 mm × 46 mm × 11.5 mm, ARM
   Cortex-M4 with a software-defined radio, VHF transmit, VHF and UHF
   receive; end-to-end AES-128 with per-device keys, hidden device identity,
   authenticated sender.
4. **Space segment** (§3.3): each satellite footprint is about 5000 km in
   diameter; satellites downlink the sampled spectrum over S band.
5. **Access** (§3.4): open-loop transmission with no time or frequency slot
   assignment; the cloud multiuser receiver avoids the synchronisation and
   control overhead of orthogonal access. Stated; the algorithm is in ref.
   [7].
6. **Link** (§5.1): 500 mW transmitter output; messages about 1 kHz wide
   and 250 ms long; in AWGN, messages are acquired and decoded with very
   high probability above an SNR of 3 dB, and a small fraction below it.
   Stated; no curve shown.
7. **Field decoding** (§5.1, Figs. 6–7, shown): a 20 kHz baseband
   spectrogram with seven decoded messages, two at SNR 2.7 dB; the SNR CDF
   of 8100 field messages has 82% at SNR ≥ 6 dB (3 dB margin), 42% above
   13 dB (≥ 10 dB margin) and a maximum of 27 dB, from which the authors
   infer that transmit power could be lowered.
8. **Interference** (§5.2, Fig. 8): three messages decoded despite strong
   overlapping interferers; one example.
9. **Battery life** (§6): a per-subsystem energy model calibrated in the
   laboratory predicts 2 years at 4 position-stamped messages per day and
   4.5 years at 1 message per day for the §4 unit. Predicted, not measured;
   long-term field testing is stated to be ongoing.

# Methods

A system description plus field data; no mathematical model. Pilot (§4): two
to three water-tank monitors on each of five Australian properties, with an
off-the-shelf 4–20 mA pressure sensor (up to 3.5 m water depth), four AA
1.5 V lithium batteries, a custom PCB, an IP67 enclosure, an internal GPS
antenna and an external VHF antenna (Fig. 4), and a React web application
(Fig. 5). Field statistics are receiver-estimated SNRs of each decoded
message. The battery model (microcontroller, radio, GNSS, sensors) is
described but not given.

# Tests and results

Anecdotal (§5): on one property a pump failure was found and fixed within
hours; on another the refill duration of a timer-run pump was determined
from historical data. Quantitative results are those of claims 7–9.

# Notation map

| Haley et al. (2018) | Registry | Note |
|---|---|---|
| SNR | words (signal-to-noise ratio, dB) | not a plasma quantity |
| AWGN | words (additive white Gaussian noise channel) | printed "Additive Gaussian White Noise" |

No mathematical symbols are used; nothing collides with the registry.

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Haley_Massive_scale_long_battery_life_direct_to_orbit_connectivity.pdf`.
   * **Version.** Publisher's version of record (Elsevier, © 2018 IAA),
     6 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.035, printed on page 1
     and checked on Crossref: title, all five authors, Acta Astronaut.
     151:318–323 match; issued 2018-10, no published-online field. Page 1:
     received 30 Oct 2017, revised 16 Feb 2018, accepted 14 Jun 2018, online
     18 Jun 2018. Page 1 matches the filename title.
   * **How it was read.** Full text layer. Figs. 1–8 (photos, maps,
     spectrograms, a CDF) were not digitised; every number above is stated
     in the text.
   * **Recorded as printed.**
     * §5.1 writes "Additive Gaussian White Noise" for additive white
       Gaussian noise (cosmetic).
     * §3.1 announces a two-way service "will be offered in 2018": a
       forward-looking statement, not a result.
     * Reader's check: the §5.1 margins (82% at ≥ 6 dB = 3 dB above the
       3 dB threshold; 42% above 13 dB = ≥ 10 dB margin) are internally
       consistent.
   * **Reference list.** 7 printed entries ([1]–[7]), matching the
     Crossref reference count.

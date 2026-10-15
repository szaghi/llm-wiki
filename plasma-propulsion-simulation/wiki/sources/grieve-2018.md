---
type: Source
title: "Grieve et al. (2018) — SpooQySats: CubeSats to demonstrate quantum key distribution technologies"
description: "Describes the SpooQySats programme of iterative balloon and CubeSat flight qualification of a miniature photon-pair source towards satellite quantum key distribution, reviewing satellite-QKD configurations and trusted-node key relay and reporting polarisation-correlation data from 335 days in orbit."
resource: "doi:10.1016/j.actaastro.2018.06.005"
source_kind: paper
authors: [Grieve J.A., Bedington R., Tang Z., Chandrasekara R.C.M.R.B., Ling A.]
year: 2018
venue: "Acta Astronaut. 151:103–106"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Grieve_SpooQySats_CubeSats_to_demonstrate_quantum_key_distribution.pdf"
tags: [context, cubesat, quantum-key-distribution, quantum-communication, flight-qualification]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

A short programme paper on the "SpooQySats" programme of the Centre for
Quantum Technologies (NUS, Singapore): iterative flight qualification of
the miniature photon-pair source SPEQS (Small Photon Entangling Quantum
System) on high-altitude balloons and CubeSats, as a step towards
satellite quantum key distribution (QKD). §2 reviews four satellite-QKD
configurations (Fig. 1, reproduced from [12]) and argues that the source
should be in orbit; §3 explains trusted-node downlink with XOR key relay
(Fig. 2, from [20]); §4 gives the milestone history (Table 1), on-orbit
polarisation-correlation data from the Galassia CubeSat (Fig. 3) and the
SpooQy-1 design (Fig. 4). There is no new theory and no numerical model;
the only new data are the Fig. 3 correlation curves. The paper has no
plasma or propulsion content.

# Key claims

1. **Downlink advantage** (§2, attributed to [14]): space-to-ground links
   are less affected by turbulence than uplinks because turbulence acts
   mainly at the end of the path where the atmosphere is thickest.
2. **Entanglement distribution to two ground stations** (§2, Fig. 1
   case 3): removes the trust requirement via a Bell test but suffers
   "∼60 dB of total loss"; Micius achieved "only slightly more than a
   single pair per second" [8]. Attributed.
3. **Trusted-node relay** (§3, Fig. 2): the satellite broadcasts
   $K_A\oplus K_B$; each station recovers the other key,
   $K_A\oplus(K_A\oplus K_B)=K_B$ and $K_B\oplus(K_A\oplus K_B)=K_A$; the
   parity of independent secret strings is uniformly random and leaks no
   useful information, but the satellite must be trusted. Stated (standard
   argument).
4. **SPEQS milestones** (Table 1): 2012 basic miniature SPDC source on a
   balloon [21]; 2013 correlated SPDC pair source on a balloon [22]; 2014
   space-qualified correlated source survives a rocket explosion (GomX-2)
   [23]; 2016 space-qualified correlated source in LEO (Galassia) [24];
   2019, future, entangled photon-pair source in space (SpooQy-1) [12];
   2020+, future, QKD from CubeSats with optical links [26].
5. **On-orbit data** (§4, Fig. 3): polarisation-correlation curves over
   335 days on orbit with "little degradation in the correlations"; the
   pair rate is temperature-sensitive because temperature changes the
   optical alignment. Shown.
6. **SpooQy-1** (§4, Fig. 4): a polarisation-entangled SPEQS with an
   isostatic, thermally isolating mount designed by UNSW Canberra,
   occupying about 2/3 of the 3U spacecraft volume, for launch in 2018
   [11].
7. **Future missions** (§4): Fig. 1 cases 2 and 4 (CQuCoM proposal [26];
   a CubeSat-to-CubeSat study with UNSW Canberra [27]); inter-satellite
   links expected to be critical for trusted-node constellations [28].
   Stated, prospective.

# Methods

* Programme and review paper. Hardware: SPEQS spontaneous parametric
  down-conversion (SPDC) photon-pair sources, flown on high-altitude
  balloons and CubeSats (GomX-2, Galassia, SpooQy-1 3U with ISIS frame and
  GOMSPACE subsystems per the Fig. 4 labels).
* Measurement (Fig. 3): coincidence counts (photon pairs per 30 s) against
  polarisation rotation angle (0 to about 4.5 rad), maxima with polarisers
  aligned, minima crossed; details deferred to [24].
* No equations beyond the XOR identities of §3; no numerics, no
  simulation.

# Tests and results

* Fig. 3 (Galassia SPEQS, data updated from [25]): five curves labelled
  "335 Days, 14.5 C", "261 Days, ~15 C", "128 Days, ~15 C", "36 Days,
  ~22 C" and "Earth, 24.7 C". Peaks read off the plot (visual estimates,
  not tabulated in the paper): about 1800 pairs per 30 s (261 d), about
  1450–1500 (335 d and 128 d), about 1150 (36 d), about 500 (Earth);
  minima near zero at about 1.8 rad.
* Context numbers (§1, attributed): fibre QKD reaches "at most a few 100s
  of kilometres" [6]; the terrestrial free-space record is 144 km [7].

# Notation map

The paper uses no physical-quantity symbols.

| Grieve et al. (2018) | Registry | Note |
|---|---|---|
| $K_A$, $K_B$ | words (secret keys of stations A and B) | bit strings |
| $\oplus$ | words (bitwise XOR) | |
| QKD, SPDC, SPEQS, TRL, SWaP | words | acronyms |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Grieve_SpooQySats_CubeSats_to_demonstrate_quantum_key_distribution.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier, © 2018 IAA),
     4 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.005, printed on page 1
     and checked on Crossref: title, five authors, Acta Astronaut.
     151:103–106 match; issue October 2018 (no published-online field on
     Crossref); page 1 gives received 28 Feb 2018, revised 31 May 2018,
     accepted 3 Jun 2018, online 4 Jun 2018. Page 1 matches the filename
     title.
   * **How it was read.** Full text layer, all legible. Fig. 3 numbers are
     visual estimates only; Figs. 1, 2 and 4 are schematics, described by
     their captions.
   * **Recorded as printed.**
     * §4 places the SpooQy-1 launch in 2018 [11], while Table 1 lists the
       SpooQy-1 demonstration as 2019 and cites [12] (a 2016 paper) for
       it; launch and demonstration years differ, but the dating is
       inconsistent.
     * §4 says the Galassia source produces photons "not entangled in
       polarization", yet Fig. 3 shows "the correlation in polarization":
       consistent (correlation, not entanglement), noted against
       misreading.
     * The Fig. 3 caption says "Data updated from [25]", the text "adapted
       and updated from [25]", and the description is deferred to [24];
       refs. [24] (Tang et al., Phys. Rev. Appl.) and [25] (Chandrasekara
       et al., SPIE) carry the same title, two venues for one experiment.
     * Reference list: [6] and [10] print issue-like "(9)" and "(11)" with
       no volume; [19] prints article number "30501" (likely 030501); [16]
       prints "89970" (likely truncated); [8] has a stray opening quotation
       mark; [25] "Nanoscatellite". Not checked on Crossref.
   * **Reference list.** 28 printed entries, matching the Crossref
     reference count.

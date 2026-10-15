---
type: Source
title: "Dhara et al. (2018) — CGR-BF: An efficient contact utilization scheme for predictable deep space Delay Tolerant Network"
description: "Extends Contact Graph Routing for deep-space Delay Tolerant Networks with reactive bundle fragmentation so that contacts too small for a whole bundle are still used, argues its expected delivery time is never worse than CGR's, and shows in Earth–Mars–Moon and Jupiter/Saturn network simulations gains in transmitted data and goodput that grow with bundle size and link constraint."
resource: "doi:10.1016/j.actaastro.2018.06.023"
source_kind: paper
authors: [Dhara S., Burleigh S., Datta R., Ghose S.]
year: 2018
venue: "Acta Astronaut. 151:401–411"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Dhara_CGR-BF_An_efficient_contact_utilization_scheme_for_predictab.pdf"
tags: [context, delay-tolerant-network, routing, deep-space-communication]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper proposes CGR-BF, an extension of Contact Graph Routing (CGR)
for deep-space Delay Tolerant Networks. A bundle is reactively fragmented
at the source or at an intermediate node, so that contacts whose residual
capacity cannot carry a whole bundle (ignored by standard CGR) are still
used, and the fragments travel over multiple paths. For each feasible
path the algorithm (Algorithm 1, §2.2) computes a route capacity and an
Expected Delivery Time (EDT) with either the bundle size or the route
capacity; the path with the earliest EDT is chosen and the bundle split
into a route-capacity fragment plus remainder. A lemma argues that
CGR-BF's EDT is never worse than CGR's. Simulations with an in-house C
simulator on STK-generated Earth–Mars–Moon networks (with or without a
relay orbiter) and an extended Jupiter/Saturn network show more data
transmitted and higher goodput, the gain growing with bundle size and
with more constrained links, at negligible header overhead. The paper has
no plasma or propulsion content.

# Key claims

1. **CGR wastes residual capacity** (§1.2, §1.2.1, Table 1): standard CGR
   selects only contacts whose residual capacity can carry a whole bundle.
   Stated with an illustrative example.
2. **Fragmentation rule** (Algorithm 1 lines 36–51, §2.2): when the route
   capacity is below the bundle size, a fragment of size route capacity is
   enqueued and the rest re-queued at the front of the local queue; the
   path carrying a fragment is flagged unusable until the last fragment is
   queued.
3. **Route capacity** of a path $p$ (Algorithm 1 line 9): the minimum of
   the residual capacity of the path's first contact and the minimum
   capacity over the path's contacts.
4. **Lemma 1** (§2.2, proved informally by contradiction): for paths
   ordered by EDT $t_1<t_2<\dots<t_n$ with route capacities $c_i$,
   CGR-BF's EDT equals CGR's in the worst case (when the first path can
   carry the whole bundle) and is not larger otherwise. Corollary 1:
   CGR-BF may send more bundles than CGR in a given time.
5. **No added complexity** (§2.2.1, Fig. 7): both schemes run Dijkstra on
   the line graph (contacts as nodes); CGR-BF only keeps
   insufficient-capacity contacts. Stated, not measured.
6. **Gains, network without relay** (Table 4): Case 1, transmitted data
   +3% to +43% and goodput +0.9% to +22% for 1–500 MB bundles; Case 2 up
   to +567% transmitted and +400% goodput (200 MB); Case 3 +221%
   transmitted and +102% goodput (50 MB). Asterisked entries are bundle
   counts where CGR transmitted none. Shown.
7. **Averaged goodput gain** (§3.2): "as large as 52–72%" for initial
   bundle sizes of about 50–500 MB. Stated, from Fig. 10.
8. **Relay orbiter** (§3.2): the percentage improvement is unaffected by
   the relay, though absolute throughput is higher with it. Stated; no
   relay table is printed.
9. **Header overhead** (§3.2.2, Fig. 12): the fragmentation overhead
   (about 26 bytes per compressed header, after RFC 5050 [14]) is
   insignificant against the goodput gained. Shown in figures.
10. **Standardisation** (§1, ref. [25]): the idea has been proposed for
    the CCSDS SABR White Book as "Anticipatory Fragmentation". Stated.

# Methods

* Algorithm 1: procedures CGR-BF(B), CONSTRUCT_PATH (recursive
  depth-first enumeration of contact sequences with visited flags, EDT
  computed with the bundle size or the route capacity, earliest-EDT path
  kept) and BUNDLE_TRANSMISSION (enqueue the whole bundle or split it).
  Variables in Table 2.
* The EDT accounts only for the local queuing delay; downstream queues are
  unknown (§1.2, §3.2).
* Simulator (§3.1): custom deep-space simulator in C; Poisson bundle
  arrivals at each source with "mean equal to 1" (unit not stated); bundle
  sizes 1, 10, 50, 100, 200, 500 MB; sources generate data for 6 h;
  48 h simulated.
* Topology (§3.1, §3.3, Fig. 8, Table 3): contacts from STK [27]; Mars
  orbiters MOM, MAVEN, Mars Odyssey, MRO and one lander; lunar LRO and
  Lunar Artemis; three Earth orbiters (circular, critically inclined,
  Sun-synchronous); a ground station at Bangalore; an optional
  Sun-synchronous relay orbiter between Earth and Mars; the extended
  network adds orbiters at Jupiter (Juno parameters) and Saturn (Cassini
  parameters).
* Cases: 1, long contacts and high data rate; 2, long contacts and low
  data rate; 3, short contacts and low data rate. Results are averaged
  over cases and topologies.
* Metrics: data transmitted from sources, goodput at destination, header
  overhead.

# Tests and results

* Illustrative example (§1.2.1, Fig. 2, Table 1): 7-node network; contact
  0→1 over [20, 120] s with 1 s transmission and 5 s propagation; contact
  1→3 over [20, 28] s with 2 s transmission is rejected because only 1 s
  remains.
* §2.1 examples (Figs. 4–6): a route capacity of 4.5 bundles on P1 (EDT
  300 s) against P2 (EDT 600 s) sends 4 bundles plus a fragment; a route
  capacity below one bundle sends 3/4 of it on P1 and the rest on P2
  instead of CGR's P3 (0→6→5); intermediate-node fragmentation over
  1→2→5 and 1→3→4→5.
* Earth–Mars–Moon network (§3.2, Figs. 9–10, Table 4), gains of CGR-BF
  over CGR at 1, 10, 50, 100, 200, 500 MB:

  | Case | Transmitted | Goodput |
  |---|---|---|
  | 1 | 3%, 10%, 19%, 24%, 28%, 43% | 0.9%, 3%, 6%, 15%, 17%, 22% |
  | 2 | 5%, 23%, 54%, 246%, 567%, 82* | 3%, 15%, 44%, 160%, 400%, 31* |
  | 3 | 9%, 66%, 221%, 201*, 103*, 41* | 5%, 40%, 102%, 89*, 45*, 15* |

  (* = bundles transmitted by CGR-BF where CGR transmits none.) The
  throughput of both schemes is below the transmitted data because data
  remain blocked at intermediate nodes within the simulated time.
* Case 3 goodput (§3.2.1, Fig. 11): CGR-BF significantly better even at
  small bundle sizes.
* Extended network (§3.3, Table 5; data in Mb, CGR-BF/CGR, transmitted
  then received): Mars Lander 6288/4680, 4337/3200; MAVEN 347048/347048,
  80824/77640; MOM 345376/345376, 136566/127872; MRO 345536/345536,
  108552/105528; Mars Odyssey 69192/57768, 17624/16192; LRO 34632/34632,
  11720/10464; Lunar Artemis 34680/34680, 3024/2392; Jupiter orbiter
  344136/344136, 106536/104240; Saturn orbiter 344144/344144,
  94536/86896. Fig. 13 gives the average goodput gain per case (values
  only in the figure).

# Notation map

The paper is networking; none of its quantities has a registry
counterpart.

| Dhara et al. (2018) | Registry | Note |
|---|---|---|
| $B$, $B_{size}$ | words (bundle size) | defined identically in Table 2; not the magnetic field $\mathbf B$ |
| $m$, $m^s$ | words (contact, initial contact) | not a mass |
| route_capacity | words | |
| EDT | words (expected delivery time) | |
| $\tau$ | words (time) | |
| $t_i$, $c_i$ (Lemma 1) | words (delivery time, capacity of path $i$) | **collision:** $c$ is the speed of light |
| $s$, $d$ | words (source, destination node) | **collision** with the species index $s$ |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Dhara_CGR-BF_An_efficient_contact_utilization_scheme_for_predictab.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier), pages
     401–411, with author biographies.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.023, printed on page 1
     and checked on Crossref: title, four authors, Acta Astronaut.
     151:401–411 match; issue October 2018 (no issue number, no
     published-online field on Crossref); page 1 gives received 21 Dec
     2017, revised 18 May 2018, accepted 8 Jun 2018, online 14 Jun 2018.
     Page 1 matches the filename title.
   * **How it was read.** Full text layer; Algorithm 1 read from the
     rendered page 405 (an image), all lines legible. Figs. 1–13 are plots
     and diagrams: their values were not digitised, only statements in the
     text are recorded. No equations beyond Algorithm 1 line 9 and the
     Lemma 1 inequalities.
   * **Recorded as printed.**
     * Lemma 1 is stated as equality "in the worst case", while the proof
       concludes "equal to or less than"; the proof is informal (it does
       not treat fragments routed over several paths beyond the ordering
       argument) and writes the ordering as inequalities on paths
       ($p_1\le p_m\le p_n$) rather than on indices.
     * §1.2.1: with the contact starting at 20 s, 1 s transmission and 5 s
       propagation, arrival is 26 s; the text gives τ = 27 s.
     * §3.3 takes the Mars–Earth propagation delay as 300 s, while Table 3
       lists 1200 s for Mars orbiters to Earth orbiters or ground station
       (600 s to the relay orbiter). Not explained.
     * The §3.2 "52–72%" goodput gain for 50–500 MB is not traceable to
       the per-case values of Table 4; presumably averaged (Fig. 10).
     * Table 4 mixes percentages and bundle counts (asterisked) in the
       same cells.
     * Table 2 defines $B$ and $B_{size}$ identically; Table 3 holds
       implausible entries (MAVEN→Earth-orbiter duration "8934", Jupiter
       orbiter frequency "10123", duration "75250636"), apparently
       per-link values concatenated in typesetting.
     * Keyword "Contract graph routing" for Contact graph routing.
     * Ref. [19] prints authors "Birranea … Kaschc" (affiliation
       superscripts leaked) and no journal name.
   * **Reference list.** 28 printed entries ([1]–[28]), matching the
     Crossref reference count.

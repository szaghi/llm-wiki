---
type: Source
title: "Loureiro, Panades & Silva (2018) — Lessons learned in 20 years of application of Systems Concurrent Engineering to space products"
description: "Reviews the Total View Framework and the Systems Concurrent Engineering approach, which applies the systems engineering process simultaneously to product and service elements, presents its 2017 revision adding concepts and architectures for every life-cycle service and hazard-derived modes, illustrates it on the TIM pico-satellite formation and the Brazilian PESE programme, and lists 13 lessons, without quantitative results."
resource: "doi:10.1016/j.actaastro.2018.05.042"
source_kind: paper
authors: [Loureiro G., Panades W.F., Silva A.]
year: 2018
venue: "Acta Astronaut. 151:44–52"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Loureiro_Lessons_learned_in_20_years_of_application_of_Systems_Concur.pdf"
tags: [context, systems-engineering, concurrent-engineering, space-programme, methodology]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

A systems-engineering methodology retrospective. It reviews the Total
View Framework (analysis, integration and structure dimensions, Fig. 1,
from Loureiro's 1999 PhD) and the Systems Concurrent Engineering (SCE)
approach, which applies the systems engineering process simultaneously
to product and organisation (later "service") elements at every layer
of the breakdown structure. It recalls the 2010 revision (a mission
layer, stakeholder analysis before requirements analysis,
"implementation" instead of "physical" analysis, circumstances
distinguished from scenarios; Figs. 2–3) and presents a 2017 revision: a
solution life-cycle layer with concepts and architectures for every
life-cycle service, not only the concept of operations and the system
operational architecture, and modes derived also from functional and
implementation hazard analysis (Figs. 4–5). The update is illustrated on
the TIM pico-satellite formation (§4) and on the Brazilian PESE defence
space programme (§5), and 13 consolidated lessons are listed (§6). The
paper has no equations, no quantitative results and no validation. Its
acknowledgement says it derives from Loureiro's IAC 2017 presentation.

# Key claims

1. **Track record** (§1, stated, not documented). SCE was first presented
   at IAC 1998 and has been applied since 1999 to "more than 200" complex
   system solutions, in courses and consulting.
2. **Framework** (§2, Fig. 1, definition). Following Hitchins (the
   paper's ref. [8]), complexity results from variety, connectedness and
   disorder; the Total View Framework addresses them with its analysis,
   integration and structure dimensions respectively.
3. **Circumstances and scenarios** (§2.2, introduced in 2010).
   Circumstances are states of the elements in the environment of the
   system of interest; scenarios are states of the system itself
   (decompositions of life-cycle processes). Modes are identified from
   circumstances.
4. **Life-cycle concepts** (§3, lesson 1, argued by the TIM example).
   Modelling only an operational architecture does not give a complete
   requirement set; for multi-spacecraft solutions the concepts and
   architectures of production, testing, launch, servicing and
   decommissioning must be modelled too.
5. **Hazard-derived modes** (§3, lesson 2). Modes can be identified from
   circumstances and from functional and implementation hazard analysis,
   e.g. a battery failure leading to a sunlight-only operation mode.
6. **Services** (§3). "Service" replaces "organisation" in the
   integration dimension: the methods, people and tools that implement
   life-cycle processes.
7. **TIM** (§4, Figs. 6–7, after Schilling et al., ref. [15]). Nine
   pico-satellites from five continents for photogrammetric 3-D Earth
   observation, adopting the UNISEC Europe electrical interface standard
   (ref. [16]); SCE's contribution is to require production, testing,
   launch, servicing and decommissioning concepts and architectures for
   the formation.
8. **PESE** (§5, Figs. 8–9, stated). Assembly, integration and test of
   SGDC2 planned at LIT/INPE from 2020 implies "approximately 25% of
   Brazilian content, in cost"; SCE lets the test concepts and the LIT
   facility requirements be anticipated at the bidding stage.
9. **Consolidated lessons** (§6), among them: decompose scenarios when a
   product or service has more than 10 stakeholders or more than 10
   environment elements (lessons 4–5); failures in the energy, material
   and information flows between element and environment are hazard
   sources (lesson 7); order functional analysis as essential
   (technology-independent), technology-nonspecific and
   technology-dependent functions (lesson 9); a state is the process or
   overall function at an instant, a mode the way it is executed
   internally (lesson 12).
10. **Conclusion** (§7). "Partial results show that the modifications are
    sufficient" for life-cycle service conceptualisation, though no
    results are shown; future work is a life-cycle cost comparison of SCE
    with traditional product-focused systems engineering.

# Methods

A qualitative methodology paper: framework diagrams (Figs. 1–5) and a
narrative application to two programmes, with no model, equation, code
or experiment. The SCE process (Figs. 3, 5) runs from mission statement
and measures of effectiveness, through concept of operations and
operational architecture (in 2017, concepts and architectures for every
life-cycle service), system of interest, life-cycle processes,
scenarios, stakeholder, functional and implementation context analysis,
circumstances and modes, to functional analysis, hazard analysis,
allocation to the implementation architecture, and requirements with
measures of performance per element, applied simultaneously to product
and service elements.

# Tests and results

There are no tests. The two applications are qualitative:

- **TIM** (§4): nine pico-satellites, a formation that may imply
  production of "up to 10 satellites"; five life-cycle concepts listed
  (production; testing, including batch thermal-vacuum, vibration and
  anechoic tests; launch all at once or staggered; servicing and
  rebalancing; decommissioning).
- **PESE/SGDC2** (§5): test at LIT from 2020, about 25% Brazilian content
  in cost; anticipated LIT facility requirements (thermal vacuum,
  vibration and acoustics, EMI/EMC, mass properties, antenna
  measurement, functional testing) and logistics.

No numerical, cost or schedule outcome is reported.

# Notation map

The paper uses no mathematical symbols. Its terms have no registry
counterpart.

| Loureiro et al. (2018) | Registry | Note |
|---|---|---|
| SCE (Systems Concurrent Engineering) | words | |
| CONOPS, SOA, MoE, MoP | words (concept of operations, system operational architecture, measures of effectiveness and performance) | |
| mode, state, scenario, circumstance | words | "mode" is a system operating mode, not a wave or oscillation mode |
| AIT, MGSE, EGSE | words (assembly, integration and test; mechanical and electrical ground support equipment) | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Loureiro_Lessons_learned_in_20_years_of_application_of_Systems_Concur.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier), pages 44–52.
   * **Identity.** doi:10.1016/j.actaastro.2018.05.042, printed on page 1
     and checked on Crossref: title, authors (G. Loureiro, W.F. Panades,
     A. Silva; the vitae print Waldemar Panadés Filho and Ana Claudia de
     Paula Silva), Acta Astronaut. 151:44–52 match; issued 2018-10, no
     published-online field. Page 1: received 27 Feb 2018, revised 4 May
     2018, accepted 20 May 2018, online 22 May 2018. Page 1 matches the
     filename title.
   * **How it was read.** Full text layer. Figs. 1–5 are framework
     diagrams, captured from captions and text only; Figs. 6–9 are
     illustrations. The supplementary data (Appendix A) are not in this
     PDF.
   * **Recorded as printed.**
     * The Abstract derives modes from "circumstances, interface states
       and internal states of the system"; §3 (lesson 2), §6 (lesson 8)
       and §7 derive them from circumstances and functional and
       implementation hazard analysis; §6 lesson 11 adds "conditions
       imposed by stakeholder".
     * §4 calls TIM a formation of nine pico-satellites, then says it
       "implies the production of up to 10 satellites", unexplained.
     * §1 gives IAC 1998 as the first presentation and also "since 1999".
     * §7 claims partial results without presenting any.
   * **Reference list.** 17 printed entries ([1]–[17]), matching the
     Crossref reference count. Ref. [15] prints a garbled author list
     ("J. d. L. Hermann Steyn Giovanni Beltrame"), split on a best-effort
     basis in the bibliography.

---
type: Source
title: "Yang, Hou & Wang (2018) — Uncertain surface accuracy evaluation based on non-probabilistic approach for large spacecraft"
description: "Proposes an interval (non-probabilistic) evaluation of the surface accuracy of large spacecraft surfaces, a mean-relative RMS index propagated by first-order Taylor interval extension with a subinterval min/max search, shown on a 2-D parabola against Monte Carlo, an SSPS solar sub-array and a 160 m solar sail."
resource: "doi:10.1016/j.actaastro.2018.06.002"
source_kind: paper
authors: [Yang C., Hou X., Wang L.]
year: 2018
venue: "Acta Astronaut. 151:95–102"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Yang_Uncertain_surface_accuracy_evaluation_based_on_non-probabili.pdf"
tags: [context, space-structures, surface-accuracy, interval-analysis, uncertainty]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper proposes an interval (non-probabilistic) way to evaluate the
surface accuracy of large spacecraft surfaces when measurements are
uncertain. The usual root-mean-square (RMS) out-of-plane deformation
index is made relative to the mean deformation (a "modified RMS",
Eq. 2). Each uncertain parameter is an interval of known bounds, and the
RMS bounds follow from a first-order Taylor interval extension
(Eqs. 4–11). To limit the interval-expansion error of the first-order
expansion at larger uncertainty, each parameter interval is split into
$N$ subintervals and the RMS bounds are the minimum and maximum over
subinterval combinations (Eqs. 12–20, after Zhou, Jiang and Han [29]).
Three examples, all with four subintervals: a 2-D parabola deformation
checked against a Monte Carlo run of $10^6$ samples; a
100 m × 100 m flexible solar sub-array of a multi-rotary-joint space
solar power satellite (SSPS) under solar pressure (static); and a 160 m
solar sail (nonlinear dynamic, four load cases). The solar sail is the
only propulsion link: the paper states that its thrust acceleration is
set by the surface accuracy (§5.3), but sail propulsion is not
modelled. The paper has no plasma content.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Deterministic index** (§2, Eq. 1):
   $R=\sqrt{\frac1n\sum_{p=1}^{n}z_p^2}$, with $z_p$ the out-of-plane
   deformation at measurement point $p$ and $n$ the number of points.
2. **Modified RMS** (§2, Eqs. 2–3): Eq. 1 ignores the re-fit after
   deformation, so
   $R^*=\sqrt{\frac1n\sum_{p=1}^{n}(z_p-\eta)^2}$ with the mean
   deformation $\eta=\frac1n\sum_{p=1}^{n}z_p$. Only planar surfaces are
   treated; the curved case "can be easily derived" (stated, not shown).
3. **Interval parameters** (§3, Eq. 4):
   $\alpha_i^I=\alpha_i^c+\Delta\alpha_i\,e=[\alpha_i^c-\Delta\alpha_i,\ \alpha_i^c+\Delta\alpha_i]$,
   with $e=[-1,1]$, midpoint $\alpha_i^c$ and radius $\Delta\alpha_i$.
4. **First-order interval extension** (§3, Eqs. 6–11), valid for small
   $\Delta\alpha_i/\alpha_i^c$: $(R^*)^I=(R^*)^c+\Delta(R^*)^I$ with
   radius
   $\Delta R^*=\sum_i\left|\partial R^*(\alpha^c)/\partial\alpha_i\right|\Delta\alpha_i$
   (Eq. 8) and bounds $(R^*)^c\mp\Delta R^*$ (Eqs. 9–10); Eq. 11 gives
   the chain rule through $z_p$ and $\eta$. Derived.
5. **Subinterval technique** (§4, Eqs. 12–20, attributed to [29]): each
   $\alpha_i^I$ is split into $N$ equal subintervals, giving $S=N^{un}$
   groups; $R^*$ is evaluated per group; adjacent subintervals share an
   endpoint, so the union over groups gives the full interval, with the
   bounds as the minimum and maximum over groups. Motivated by avoiding
   interval expansion.
6. **2-D parabola** (§5.1, Table 1, shown numerically): at 1%
   uncertainty the interval is [0.030937, 0.031412] m; the largest
   relative difference from the Monte Carlo bounds is 1.30% (lower bound
   at 5%). The proposed bounds lie outside the Monte Carlo bounds at
   every level (see Recorded as printed).
7. **SSPS solar sub-array** (§5.2, Table 2): maximum static deformation
   under solar pressure about 3.3 mm, at the four corners; at 1%
   uncertainty the whole-array interval is [0.0008645, 0.0008775] m;
   the surface RMS increases in the order Center < Side < whole <
   Corner.
8. **Solar sail** (§5.3, Figs. 9–12): the dynamic RMS bounds form "wide
   belt zones" in time, stated to enclose all uncertain random cases;
   graphical only. The RMS values rise across load cases in the order
   double pre-stress < 0.8 reflectivity < initial design < 1 μm
   thickness.
9. **Scope** (§6, stated): the method serves static loading (result an
   interval) and dynamic loading (a belt zone in time) and needs only
   the bounds of the uncertainties, not their probability densities.

# Methods

* Index: modified RMS $R^*$ of the out-of-plane deformation about its
  mean (Eqs. 2–3), planar surfaces only.
* Uncertainty model: independent interval parameters with an "uncertain
  level" (relative radius $\Delta\alpha_i/\alpha_i^c$) of 1–5%. The
  paper does not say which physical quantities are the interval
  parameters; "measurement uncertainties and errors" suggests the
  measured deformations $z_p$, but this is not defined.
* Propagation: first-order Taylor interval extension (Eqs. 6–11) plus a
  subinterval min/max search (Eqs. 12–20); $N=4$ in every example. The
  text says the subinterval index $j$ is "randomly selected" per
  parameter in each group.
* Validation: Monte Carlo with $10^6$ samples, for the 2-D example
  only; the sampling distribution is not stated.
* Finite-element models: (i) solar sub-array 100 m × 100 m, truss as
  combined bar and beam elements, membrane as 2-D shell elements,
  corner nodes constrained, solar-pressure load, nonlinear static
  solution (§5.2); FE code, mesh and pressure value not stated. (ii)
  160 m "five-connected-sail" solar sail (membrane, beams, central body,
  slider, roll stabiliser bars), solar pressure $9.12\times10^{-6}$ Pa,
  nonlinear dynamic solution (§5.3); FE code, mesh, material and time
  step not stated. The multi-rotary-joint SSPS concept (about 10 km,
  about 10000 t) is taken from Hou et al. [6].

# Tests and results

* **2-D parabola** (§5.1, Fig. 1): $y=\frac{1}{250}x^2-\frac{1}{25}x$,
  $x\in[0,10]$, 100 random sample points. Table 1 (m), uncertain levels
  1/2/3/4/5%:

  | bound | 1% | 2% | 3% | 4% | 5% |
  |---|---|---|---|---|---|
  | lower, Monte Carlo | 0.031005 | 0.03084 | 0.030681 | 0.030528 | 0.030381 |
  | lower, proposed | 0.030937 | 0.030699 | 0.030462 | 0.030224 | 0.029987 |
  | relative difference | 0.22% | 0.46% | 0.72% | 1.00% | 1.30% |
  | upper, Monte Carlo | 0.031337 | 0.031506 | 0.031679 | 0.031858 | 0.032041 |
  | upper, proposed | 0.031412 | 0.03165 | 0.031888 | 0.032126 | 0.032364 |
  | relative difference | 0.24% | 0.46% | 0.66% | 0.84% | 1.01% |

* **SSPS sub-array** (§5.2, Figs. 4–6, Table 2, m), levels 1/2/3/4/5%:

  | region (area ratio) | lower bounds | upper bounds |
  |---|---|---|
  | whole | 0.0008645 / 0.0008579 / 0.0008514 / 0.0008449 / 0.0008383 | 0.0008775 / 0.0008841 / 0.0008906 / 0.0008972 / 0.0009037 |
  | Corner (1/16) | 0.0010078 / 0.0010002 / 0.0009926 / 0.0009850 / 0.0009774 | 0.0010231 / 0.0010307 / 0.0010383 / 0.0010459 / 0.0010535 |
  | Side (1/8) | 0.0007026 / 0.0006973 / 0.0006920 / 0.0006867 / 0.0006814 | 0.0007133 / 0.0007186 / 0.0007239 / 0.0007292 / 0.0007345 |
  | Center (1/4) | 0.0001226 / 0.0001217 / 0.0001207 / 0.0001198 / 0.0001189 | 0.0001244 / 0.0001254 / 0.0001263 / 0.0001272 / 0.0001281 |

* **Solar sail** (§5.3): vibration amplitudes at four marked positions
  (Fig. 8), largest at the membrane edge; RMS belt zones at 1%, 2% and
  5% for the initial design (Fig. 9), double pre-stress (Fig. 10), 0.8
  reflectivity (Fig. 11) and 1 μm thickness (Fig. 12). Plots only; no
  Monte Carlo sample count is given for the sail.

# Notation map

The paper is structural uncertainty analysis; none of its quantities has
a registry counterpart.

| Yang, Hou & Wang (2018) | Registry | Note |
|---|---|---|
| $R$, $R^*$ | words (surface RMS error; modified RMS about the mean) | |
| $z_p$ | words (out-of-plane deformation at point $p$) | **collision:** registry $z$ is the axial coordinate |
| $\eta$ | words (mean deformation) | **collision:** registry $\eta$ is the thrust efficiency |
| $n$ | words (number of measurement points) | **collision** with the number density $n_s$ |
| $\alpha_i^I$, $\alpha_i^c$, $\Delta\alpha_i$ | words (interval parameter, midpoint, radius) | not $\alpha_{\mathrm B}$, $\alpha_E$, $\alpha_\tau$, $\alpha_n$ |
| $e=[-1,1]$ | words (unit interval) | **collision:** registry $e$ is the elementary charge |
| $N$, $un$ | words (subinterval count; number of uncertain parameters) | |
| $S=N^{un}$ | words (number of subinterval groups) | **collision** with the shape function $S(\mathbf x)$ and the Sobol' index $S_j$ |
| superscripts $I$, $c$ | words (interval, midpoint) | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Yang_Uncertain_surface_accuracy_evaluation_based_on_non-probabili.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier), 8 pages
     (95–102).
   * **Identity.** doi:10.1016/j.actaastro.2018.06.002, printed on page 1
     and checked on Crossref: title, the three authors, Acta Astronaut.
     151:95–102 match; issue October 2018 (no published-online field on
     Crossref); page 1 gives received 27 Jan 2018, revised 26 Apr 2018,
     accepted 1 Jun 2018, online 2 Jun 2018. Page 1 matches the filename
     title.
   * **How it was read.** Full text layer. Eqs. 15–16 and 18 are garbled
     there; on rendered page 3 their structure is legible (adjacent
     subintervals meet at a shared endpoint; the union is a min/max
     envelope), but the over- and underlines marking lower and upper
     bounds in Eqs. 15–16 and 18–20 are partly ambiguous, so those
     equations are paraphrased, not reproduced. The absolute value in
     Eq. 8 was read on the rendered page. Figs. 1–12 were not digitised;
     the solar-sail results are graphical only.
   * **Recorded as printed.**
     * Eq. 6 sums over $i=1,\dots,n$, with $n$ defined in Eq. 1 as the
       number of measurement points; the sum should run over the
       uncertain parameters ($un$ in §4), unless the parameters are the
       $n$ measurements, which the paper never states.
     * Eq. 6 has no absolute value while Eq. 8 has
       $\left|\partial R^*/\partial\alpha_i\right|$; Eq. 8 is the correct
       interval radius, and Eq. 6 is consistent only read as an
       interval-arithmetic expression.
     * §4: Eq. 13 counts $S=N^{un}$ groups, but the text says $j$ is
       "randomly selected" per parameter and Eq. 18 takes the extremes
       over "$i=1..un$, $j=1..N$" only. Whether all $N^{un}$ combinations
       are enumerated is not stated; with a random sample the minimum
       and maximum are not guaranteed bounds.
     * §5.1 calls the result a "tighter and more precise interval", yet
       Table 1 puts the proposed bounds strictly outside the Monte Carlo
       bounds at every level: the proposed interval is wider
       (conservative), not tighter.
     * Reader's check: the printed relative differences agree with
       Table 1, e.g. $(0.031005-0.030937)/0.031005=0.22\%$ and
       $(0.030381-0.029987)/0.030381=1.30\%$. The proposed bounds are
       nearly symmetric about 0.031175 m at every level, with a
       radius growing linearly in the level, the signature of a
       first-order extension; what the four subintervals change in this
       example is unclear.
     * The abstract and §6 present the method as validated against
       Monte Carlo ("effectiveness and veracity"); Monte Carlo is shown
       for the 2-D example only, and the sail's enclosure claim (§5.3) is
       graphical.
     * Reference-list slips verified on Crossref: [21] Greschik et al.,
       AIAA J. 39(2), printed with year 2015, is 2001
       (doi:10.2514/2.1306); [18] Coleman et al., J. Spacecraft Rockets
       printed "49 (49) (2011)", is vol. 49 issue 5, 2012
       (doi:10.2514/1.A32021); [25] article number printed "07501", is
       075011 (doi:10.1088/0957-0233/25/7/075011). Not verified: [26] Qiu
       & Elishakoff printed "Comput. Meth. Appl. Math. 152" (likely
       Comput. Methods Appl. Mech. Eng.); [6] journal printed "J.
       Astronaut 11 (2015)".
   * **Reference list.** 32 printed entries ([1]–[32]), matching the
     Crossref reference count; [19] is printed with the label "Shi et
     al., 2013" in place of a number but is cited as [19] in the text.
     Ref. [31] (Yang, Lu & Yang 2018, IEEE Sens. J. 18:2031) is a
     different work from this source and must not take the key
     `yang-2018-b`.

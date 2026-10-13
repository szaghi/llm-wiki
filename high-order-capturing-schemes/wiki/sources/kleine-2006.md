---
type: Source
title: "Kleine, Grönig & Takayama (2006) — Simultaneous shadow, schlieren and interferometric visualization of compressible flows"
description: "Experimental optics paper: shadowgraph, schlieren and interferometry record the second derivative, the gradient and the value of density, so a compressible flow should be recorded by more than one, simultaneously when runs do not repeat; three combined set-ups are shown, with a 90° corner shock diffraction at M_s = 1.6 recorded four ways and a blast-wave reflection near the regular-to-Mach transition as illustrations. No simulation."
resource: "doi:10.1016/j.optlaseng.2005.04.009"
source_kind: paper
authors: [Kleine H., Grönig H., Takayama K.]
year: 2006
venue: "Opt. Lasers Eng. 44:170–189"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2006-OptLasersEng-Kleine-101016joptlaseng200504009.pdf"
tags: [2d, mach-reflection, blast-wave]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

An experimental flow-visualization paper with no numerical scheme and no
simulation. The three density-sensitive optical families record different
quantities: the shadowgraph the second derivative of density (light-ray
displacement), schlieren the density gradient (deflection), and
reference-beam interferometry the density itself (phase retardation). Each
has blind spots, so a flow should be recorded by more than one, and by all
of them in the same run when the flow does not repeat (explosions,
instabilities, uncontrolled chemistry) (§2, §2.4). Three combined
set-ups are described: a Mach–Zehnder interferometer with colour schlieren
from one white-light source and one recording (§3.1); holographic
interferometry with colour schlieren as two coupled systems (§3.2); and
imaging holographic interferometry with a shadowgraph or schlieren branch
split off the object beam (§3.3).

Its relevance to this bundle is limited to two illustrations that a
numerical benchmark could be set against: the vortex of a shock diffracting
at a 90° corner at $M_s = 1.6$ in nitrogen, recorded four ways (Fig. 2),
and a blast wave reflecting from a wall near the transition from regular
to [Mach reflection](/definitions/mach-reflection.md) (Fig. 6). Both are
qualitative.

# Key claims

1. **Which quantity each method records** (§2, Eq. 1). With a linear
   relation between refractive index and density (Gladstone–Dale), the
   shadowgraph responds to the second derivatives of density, schlieren to
   the gradient, interferometry to the density. All three integrate along
   the line of sight, so local values follow only for plane flow or for a
   known (e.g. axisymmetric) variation along the beam.
2. **Interferometry has a fixed sensitivity** (§2.3, Eqs. 4–5). Phase
   differences below a tenth of a fringe are "commonly accepted" as
   unresolvable; infinite-fringe monochrome records carry a sign
   ambiguity; fringe counting fails across a shock or contact, so the
   finite-fringe mode is preferred for quantitative work.
3. **Short-path and weak features are invisible to interferometry**
   (§2.3, Figs. 1–2). Near the tip of a cone the bow-shock path is short,
   so the first fringe appears only well downstream. In the diffraction
   vortex the slipstream roll-up, the peripheral instabilities and the
   secondary shocks are hard to read on the interferogram but clear on
   schlieren.
4. **Synchronization limits of two sources** (§3.2). Exposure instants
   may differ by ±2 µs (below 1 µs is readily achievable); laser pulses
   of at most 50 ns against a spark of about 1 µs mean objects faster than
   800 m/s are not frozen in the schlieren image.
5. **Conclusion** (§4). A combination performs as its most restrictive
   component allows; it is worth using only when markedly more information
   is expected.

# Tests

No numerical tests. The illustrations:

* **Fig. 1** (§2.3, from Kleine's 1994 thesis): shock-generated
  supersonic flow around a cone of 50° opening angle, $M_s = 2.93 \pm 0.02$
  in nitrogen, post-shock flow $\mathrm{Ma} = 1.34$; holographic
  interferogram (infinite fringe, 0.054 kg/m³ per fringe) and
  direction-indicating colour schlieren.
* **Fig. 2** (§2.3, adapted from the thesis): the vortex after
  diffraction of an $M_s = 1.6 \pm 0.02$ shock at a sharp 90° corner in
  nitrogen, as (a) shadowgram, (b) magnitude-indicating colour schlieren
  with horizontal cutoff, (c) direction-indicating colour schlieren and
  (d) holographic interferogram (infinite fringe, 0.054 kg/m³ per fringe).
  No triple-point, vortex-position or pressure number is given; the
  quantitative study, with a CFD comparison, is Kleine, Ritzerfeld &
  Grönig (2003, CFD J. 12:142), cited as ref. [1]. A comparison of a
  [corner-diffraction](/benchmarks/shock-diffraction.md) simulation at
  this $M_s$ should take its numbers from there, not from this paper.
* **Fig. 5** (§3.1): a candle-plume test of the combined Mach–Zehnder and
  colour-schlieren system, calibrated with a plano-convex lens.
* **Fig. 6** (§3.2): a 10 mg silver-azide charge 30 mm above a rigid
  wall, laser-ignited; at 120 µs the primary blast wave reflects from the
  wall near the transition from regular to Mach reflection. The
  interferogram misses the boundary of the combustion cloud and barely
  shows the secondary shock; schlieren shows both. The transition height or
  angle is not quantified.
* **Fig. 9** (§3.3): a 10 mg silver-azide cylinder 22 µs after ignition;
  the flow is markedly non-spherical.

The shock-tube facility of Figs. 1–2 (dimensions, driver gas) is not
described in this paper.

# Notation map

The paper's mathematics is optical and appears on no concept page; its
symbols are not carried over.

| Kleine et al. (2006) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$ | $\rho$ | |
| $M_S$ | $M_s$ | |
| $M_2$ | $\mathrm{Ma}$ | post-shock flow Mach number |
| $n$, $K$, $\lambda$, $h$, $S$, $q$, $\xi_{\max}$, $L$, $l$, $I$, $\Delta\Phi$, $z$ | words | refractive index, Gladstone–Dale constant, wavelength, unobstructed source image, schlieren sensitivity, mask gap, maximum deflection, test-section depth, shadow distance, intensity, optical path difference, beam axis; each collides with a registry symbol |

# Pages created or updated

* Updated [Shock diffraction at a backward-facing corner](/benchmarks/shock-diffraction.md) (the $M_s = 1.6$ corner vortex recorded four ways, qualitative).
* Cited by [Regular and Mach reflection](/definitions/mach-reflection.md) (blast-wave reflection near the transition, qualitative).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/2006-OptLasersEng-Kleine-101016joptlaseng200504009.pdf`.
   * **Version.** The publisher's typeset article (Elsevier, 20 pages)
     with final volume and pages, still carrying the "ARTICLE IN PRESS"
     running header; available online 8 June 2005.
   * **Identity.** doi:10.1016/j.optlaseng.2005.04.009, printed on page 1
     and checked on Crossref: Optics and Lasers in Engineering 44(3–4):
     170–189, March 2006, authors Kleine, Grönig, Takayama (UNSW/ADFA
     Canberra; Stoßwellenlabor, RWTH Aachen; Shock Wave Research Center,
     Tohoku University).
   * **How it was read.** Text extraction, all sections; pp. 3, 6, 8,
     11–14 and 17–18 checked on page images for equations, captions and
     units (the text layer renders µ as "m" and ± as "7" or blank; the
     times 120 µs and 22 µs come from the images).
   * **Reference list:** 20 entries, all merged. Same-author-year
     suffixes follow printed order: `kleine-2003` (ref. [1], the
     quantitative corner-diffraction study) and `kleine-2003-b`
     (ref. [17]); `kleine-2001` (ref. [4]) and `kleine-2001-b`
     (ref. [20]). Kleine & Grönig (1991, Shock Waves 1:51) is the same
     `kleine-1991` cited by [Kleine et al. (1995)](/sources/kleine-1995.md).
     Abbreviated page ranges were expanded. No DOIs are printed.

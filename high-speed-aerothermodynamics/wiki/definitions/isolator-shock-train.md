---
type: Definition
title: "Isolator and shock train"
description: "The duct between a scramjet or ramjet inlet throat and the combustor that holds the back-pressure-driven shock train so that combustor pressure does not unstart the inlet; its margin is measured by how far upstream the shock-train leading edge stands at a given back pressure."
status: established
aliases: [scramjet isolator, pseudo-shock, precombustion shock train, terminal shock]
tags: [isolator, shock-train, inlet, unstart, separation]
timestamp: 2026-10-14T00:00:00Z
---

# Isolator and shock train

## Function

The isolator is the duct downstream of the inlet throat. It contains the
shock train that the combustor back pressure drives into it, isolates the
inlet from that back pressure and so prevents
[unstart](/definitions/inlet-start-and-unstart.md)
([Meng et al. (2018)](/sources/meng-2018.md), §1). The shock train is a
sequence of shocks and separated regions through which the supersonic core
flow is compressed toward the imposed back pressure $p_b$; as $p_b$ rises
its leading edge moves upstream, and when it reaches the isolator entrance
the inlet is at its back-pressure limit. The leading-edge position at a
given $p_b$ is therefore the isolator's margin metric (§4.3, Fig. 14).

## Waltrup–Billig shock-train length

[Meng et al. (2018)](/sources/meng-2018.md), §1, Eq. 1, attribute to
Waltrup & Billig (1973) a correlation for the shock-train length: the
length, times $\mathrm{Ma}^2-1$ at the shock-train entrance, times the
momentum-thickness Reynolds number raised to an exponent, divided by the
square root of the product of duct diameter and momentum thickness,
equals 50 times the excess of the static pressure ratio across the
shock train over one, plus 170 times the square of that excess. The exponent is printed only as a symbol, with no
value. The correlation is stated, not used or tested, in that paper; the
printed form is on its Source page.

## Separation-mode switch

In back-pressured curved isolators of varying cross-section the shock
trains are asymmetric, and the large-scale separation switches from the
bottom wall (BLS) to the top wall (TLS) "without any changes of the
boundary conditions" ([Meng et al. (2018)](/sources/meng-2018.md), §4.3,
Figs. 13–14). The authors relate this to behaviour seen in experiments and
CFD of others. Separation and a shock appear at a back pressure twice the reference
pressure (P1, undefined in the paper; presumably the isolator-entrance
static pressure) in all four configurations they compare.

## Shape and performance

* **Curved shape-transition isolators** (800 mm long, 40 mm offset,
  entrance Mach 2): without back pressure the circular duct recovers most
  total pressure ($\sigma_0=0.91$), the rectangular one least (about
  0.87), and the rectangular-to-circular ones lie between; the optimised
  rectangular-to-circular isolator is 1.59% better than a baseline design
  and holds its shock-train leading edge furthest downstream at a back
  pressure four times the entrance static pressure
  ([Meng et al. (2018)](/sources/meng-2018.md), §4.2–4.3, Figs. 9–14).
  The authors attribute the remaining loss differences to wetted area,
  which they do not compute. $\sigma_0$ is unaffected below a back-pressure
  ratio of 1 and the four shapes are "near equivalent" above 3 (Fig. 15).
  The design method is in
  [Shape-transition isolator design](/methods/shape-transition-isolator-design.md).
* **Reflected shocks in a constant-area isolator.** In the 10 mm × 194 mm
  isolator of a two-ramp inlet at $\mathrm{Ma}_\infty=5.9$, the started
  flow carries strong reflected shocks with large reflection angles; the
  unstarted flow weaker ones that decay faster
  ([Liu H. et al. (2018)](/sources/liu-2018-d.md), §5.1). Down the
  isolator the large uncertainty intervals of the wall pressure
  coefficient (width above 1.0) shrink while the small ones between
  pressure valleys grow, which the authors call a "cumulative effect of
  uncertainty due to the multiple reflections of shock waves" (§5.2,
  Figs. 15–16).
* **Terminal shock in an intake diffuser.** In a section-controllable
  inward-turning intake the terminal-shock position in the divergent duct,
  measured from the throat as a fraction of the throat-to-exit length, is
  plotted against $p_b/p_\infty$ and is the same with and without
  boundary-layer bleed at equal back pressure
  ([Zuo & Huang (2018)](/sources/zuo-2018.md), §3.4, Fig. 18); without
  bleed the exit $\sigma_0$ is 0.598 at $p_b/p_\infty=4.2$, 0.374 and 0.373
  at 22.2 and 48.6, and rises again to 0.509 at 73.4 (Table 4).

# Citations

1. [Meng et al. (2018)](/sources/meng-2018.md), §1 (Eq. 1), §4.2–4.3 (Figs. 9–15).
2. [Liu H. et al. (2018)](/sources/liu-2018-d.md), §5.1, §5.2 (Figs. 15–16).
3. [Zuo & Huang (2018)](/sources/zuo-2018.md), §3.4 (Table 4, Fig. 18).

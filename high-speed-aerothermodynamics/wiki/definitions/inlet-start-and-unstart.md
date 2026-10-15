---
type: Definition
title: "Inlet start, unstart and hysteresis"
description: "A supersonic or hypersonic inlet is started when its internal shock system is swallowed and the captured flow passes the throat, and unstarted when a large separation and its shock stand at the entrance; the switch depends on freestream Mach number and back pressure and shows hysteresis, and is judged through total-pressure recovery, mass capture, back-pressure ratio and contraction ratio."
status: established
aliases: [inlet unstart, intake unstart, start/unstart hysteresis, intake performance parameters]
tags: [inlet, unstart, hysteresis, isolator, performance]
timestamp: 2026-10-14T00:00:00Z
---

# Inlet start, unstart and hysteresis

## Started and unstarted flow

[Liu H. et al. (2018)](/sources/liu-2018-d.md), §5.1, Figs. 11–12, show
both states of the same two-ramp inlet (ramps at 9° and 14°, a 10 mm high,
194 mm long isolator) at one freestream condition,
$\mathrm{Ma}_\infty=5.9$:

* **Started.** The cowl shock impinges just after the throat with a small
  separation and a weak separation shock; the shocks reflected along the
  isolator have large reflection angles.
* **Unstarted.** A large separation bubble sits upstream of the throat
  behind a strong separation shock; a recompression shock forms across the
  throat, a second small bubble appears on the cowl, and the reflected
  shocks are weaker and decay faster, with a pressure plateau on the wall
  (Fig. 12(b)).

An inlet therefore unstarts either from the freestream side (Mach number
below a critical value) or from the back (a downstream pressure rise
pushing the shock system out); the back-pressure route is the one the
isolator is designed to contain ([Isolator and shock train](/definitions/isolator-shock-train.md)).

## Hysteresis

Varying $\mathrm{Ma}_\infty$ between 3.3 and 7 gives different unstart and
restart paths for mass capture and $\sigma_0$
([Liu H. et al. (2018)](/sources/liu-2018-d.md), §4.5, Fig. 8, own RANS
simulation). On the restart path a first step up at
$\mathrm{Ma}_\infty=5$ does not reach the started mode because a separation
bubble remains at the entrance. At $\mathrm{Ma}_\infty=5.9$, inside the
loop, both modes exist, and two Mach-number routes to the same state
(7 → 5.9 and 7 → 6.5 → 5.9) give identical wall pressure distributions
(§4.5, Figs. 9–10). Which state a computation lands in thus depends on its
history, not only on the freestream condition.

Uncertainty in the freestream matters differently in the two states: the
95% interval widths of the exit Mach number and of $\sigma_0$ at a station
nine throat heights downstream are about twice as large in the started as
in the unstarted flow, while the normalised mass capture is not
(§5.2, Table 6); the analysis is described in
[Non-intrusive polynomial chaos and Sobol' indices](/methods/non-intrusive-polynomial-chaos.md).

## Performance parameters

### Total-pressure recovery $\sigma_0$

$\sigma_0=p_{0,\mathrm{out}}/p_{0,\infty}$ at a stated station. Values in
the sources:

* Inviscid parent flows at $\mathrm{Ma}_\infty=4$ with exit Mach 1.4:
  0.683 (2-D multi-wedge), 0.740 (2-D isentropic), 0.984 (Busemann),
  0.874 (the authors' inward-turning parent flow)
  ([Zuo & Huang (2018)](/sources/zuo-2018.md), §2.3.2, Table 1).
* A section-controllable inward-turning intake at $\mathrm{Ma}_\infty=4$
  (RANS): 0.740 at the throat without bleed, 0.764 with bleed (Tables 4–5).
* The two-ramp inlet at $\mathrm{Ma}_\infty=5.9$: 0.445 started, 0.104
  unstarted, at the isolator station $x=316$ mm
  ([Liu H. et al. (2018)](/sources/liu-2018-d.md), Table 6).
* Curved isolators at entrance Mach 2: about 0.87–0.91 at the exit without
  back pressure ([Meng et al. (2018)](/sources/meng-2018.md), §4.1–4.2,
  Figs. 8–11).

From one-dimensional mass-flow-function relations,
[Zuo & Huang (2018)](/sources/zuo-2018.md), §2.3.2, Eqs. 1–2, write
$\sigma_0$ as $\mathrm{CR}$ times the ratio of the mass-flow functions at
the freestream and exit Mach numbers, and the static pressure ratio as the
same product times the ratio of the isentropic total-to-static factors;
at fixed entrance and exit Mach numbers both therefore depend only on
$\mathrm{CR}$.

### Mass capture ratio $\varphi$

The section-controllable intake captures $\varphi=0.997$ at its design
Mach number 4 in all back-pressure cases (Table 4; the §3.4 text prints
0.992) ([Zuo & Huang (2018)](/sources/zuo-2018.md)). An enclosed capture
section prevents lateral spillage at design, and a V-shaped cowl closure
spills less than a planar intake at low Mach number (§2.3.1, Figs. 3–4;
argued qualitatively). [Liu H. et al. (2018)](/sources/liu-2018-d.md),
Table 6, report instead a mass capture rate normalised by freestream
values and the isolator cross-section area (about $4.4\times10^{-3}$
started, $3.3\times10^{-3}$ unstarted), which is not the ratio
$\varphi$.

### Back pressure $p_b$

The imposed exit pressure sets the position of the terminal shock or shock
train. In the section-controllable intake the largest back-pressure ratio
$p_b/p_\infty$ computed with the flow still established is 73.4 without
bleed ($\sigma_0=0.509$ at the exit) and 76.7 with bleed
($\sigma_0=0.528$); at equal back pressure the terminal-shock position is
unchanged by bleed ([Zuo & Huang (2018)](/sources/zuo-2018.md), §3.4,
Tables 4–5, Fig. 18). The paper does not locate the unstart limit beyond
these tabulated points; at 76.7 the throat values change (throat Mach
1.622 → 1.476, throat $\sigma_0$ 0.764 → 0.754, bleed fraction 2.528% →
2.579%), which the paper does not discuss. In curved isolators the back
pressure, as a ratio to a reference pressure (P1, undefined in the paper;
presumably the isolator-entrance static pressure), was raised
in steps 1, 2, 3, 3.5 and 4 until the shock train reached the entrance
([Meng et al. (2018)](/sources/meng-2018.md), §4.3).

### Contraction ratio $\mathrm{CR}$

The section-controllable intake has capture area 88460 mm² and throat area
14851 mm², $\mathrm{CR}\approx5.96$, and an internal ratio
$\mathrm{CR}_i\approx2.18$ (section area 32381 mm² at cowl closure)
([Zuo & Huang (2018)](/sources/zuo-2018.md), §3.1.1). The inviscid parent
flows of Table 1 have $\mathrm{CR}$ 6.58 (wedge), 6.99 (isentropic), 9.10
(Busemann) and 7.39 (inward-turning). In an osculating inward-turning
design the osculating planes cannot all keep the same $\mathrm{CR}$, so
the throat Mach number is non-uniform and some planes approach Mach 1,
an unstart risk for ramjet intakes whose throat Mach number is close to 1;
designers therefore pick a slightly higher throat Mach number at the cost
of terminal-shock loss (§2.2; stated). A scramjet intake for Mach 6
typically has a throat Mach number of 3.0 (§2.2).

# Citations

1. [Liu H. et al. (2018)](/sources/liu-2018-d.md), §4.5 (Figs. 8–10), §5.1 (Figs. 11–12), §5.2 (Table 6).
2. [Zuo & Huang (2018)](/sources/zuo-2018.md), §2.2, §2.3.1–2.3.2 (Eqs. 1–2, Table 1, Figs. 3–4), §3.1.1, §3.4 (Tables 4–5, Fig. 18).
3. [Meng et al. (2018)](/sources/meng-2018.md), §4.1–4.3 (Figs. 8–11, 15).

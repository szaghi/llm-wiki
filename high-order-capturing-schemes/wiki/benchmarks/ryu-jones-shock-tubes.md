---
type: Benchmark
title: "Ryu–Jones and Dai–Woodward one-dimensional MHD shock tubes"
description: "A set of one-dimensional ideal-MHD Riemann problems, four of them (1a, 1b, 2a, 3a) from Dai and Woodward's published tables, popularized by Ryu and Jones, that together produce every 1D wave structure: fast and slow shocks and rarefactions, rotational and contact discontinuities, switch-on and switch-off waves, tangential discontinuities and compound waves; checked against a nonlinear Riemann solver."
status: established
aliases: [Ryu–Jones shock tube, Dai–Woodward shock tube, RJ2a, MHD Riemann problems]
tags: [mhd, riemann-problem, verification, benchmark, 1d]
timestamp: 2026-10-13T00:00:00Z
---

# Ryu–Jones and Dai–Woodward one-dimensional MHD shock tubes

**The set** ([Ryu & Jones (1995)](/sources/ryu-1995.md), §4). Twelve
problems on $[0, 1]$ with $\gamma = 5/3$, units without $4\pi$, run on 512
cells at Courant number 0.8 with a second-order TVD code and compared with
a nonlinear MHD Riemann solver. States are $(\rho, v_x, v_y, v_z, B_y, B_z, p)$;
the preprint labels the last entry $E$, but it must be the gas pressure,
since read as $E$ three of the left states have negative pressure. The
position of the initial jump is not stated.

| Problem | Left | Right | $B_x$ | $t$ | Waves |
|---|---|---|---|---|---|
| 1a (DW Table VI) | $(1, 10, 0, 0, 5/\sqrt{4\pi}, 0, 20)$ | $(1, -10, 0, 0, 5/\sqrt{4\pi}, 0, 1)$ | $5/\sqrt{4\pi}$ | 0.08 | two fast shocks, a slow rarefaction, a slow shock, a contact |
| 1b (DW Table IIIa) | $(1, 0, 0, 0, 5/\sqrt{4\pi}, 0, 1)$ | $(0.1, 0, 0, 0, 2/\sqrt{4\pi}, 0, 10)$ | $3/\sqrt{4\pi}$ | 0.03 | fast and slow shocks, contact, slow and fast rarefactions |
| 2a (DW Table Ia) | $(1.08, 1.2, 0.01, 0.5, 3.6/\sqrt{4\pi}, 2/\sqrt{4\pi}, 0.95)$ | $(1, 0, 0, 0, 4/\sqrt{4\pi}, 2/\sqrt{4\pi}, 1)$ | $2/\sqrt{4\pi}$ | 0.2 | two fast shocks, two rotational discontinuities, two slow shocks, a contact |
| 2b (in no published DW table) | $(1, 0, 0, 0, 6/\sqrt{4\pi}, 0, 1)$ | $(0.1, 0, 2, 1, 1/\sqrt{4\pi}, 0, 10)$ | $3/\sqrt{4\pi}$ | 0.035 | as 2a, with rarefactions on the right |
| 3a (DW Table IIa) | $(0.1, 50, 0, 0, -1/\sqrt{4\pi}, -2/\sqrt{4\pi}, 0.4)$ | $(0.1, 0, 0, 0, 1/\sqrt{4\pi}, 2/\sqrt{4\pi}, 0.2)$ | 0 | 0.01 | two magnetosonic shocks, a tangential discontinuity |
| 3b | $(1, -1, 0, 0, 1, 0, 1)$ | $(1, 1, 0, 0, 1, 0, 1)$ | 0 | 0.1 | two magnetosonic rarefactions |
| 4a | $(1, 0, 0, 0, 1, 0, 1)$ | $(0.2, 0, 0, 0, 0, 0, 0.1)$ | 1 | 0.15 | a switch-on fast shock |
| 4b | $(0.4, -0.66991, 0.98263, 0, 0.0025293, 0, 0.52467)$ | $(1, 0, 0, 0, 1, 0, 1)$ | 1.3 | 0.15 | a contact and a switch-off fast rarefaction |
| 4c | $(0.65, 0.667, -0.257, 0, 0.55, 0, 0.5)$ | $(1, 0.4, -0.94, 0, 0, 0, 0.75)$ | 0.75 | 0.15 | a switch-off slow shock |
| 4d | $(1, 0, 0, 0, 0, 0, 1)$ | $(0.3, 0, 0, 1, 1, 0, 0.2)$ | 0.7 | 0.16 | a switch-on slow rarefaction |
| 5a (Brio–Wu at $\gamma = 5/3$) | $(1, 0, 0, 0, 1, 0, 1)$ | $(0.125, 0, 0, 0, -1, 0, 0.1)$ | 0.75 | 0.1 | a slow compound wave |
| 5b | $(1, 0, 0, 0, 1, 0, 1)$ | $(0.4, 0, 0, 0, -1, 0, 0.4)$ | 1.3 | 0.16 | a fast compound wave |

The tabulated analytic solutions are not in the preprint read here. The
"DW Table" labels follow the published Dai & Woodward (1994) numbering;
Ryu & Jones's figure captions cite the in-press numbering ("DW table 7"
for 1a, "5a" for 2b, "3a" for 1b, "2a" for 3a), which the table showed
until the 2026-10-13 deep lint (see *Later uses (batch 11)*).

**What it measures.**
* Planar-field problems (set 1) produce no rotational discontinuity, as the
  eigenstructure predicts; rotating fields (set 2) produce two.
* Resolution of each structure: strong shocks 2–4 cells, rotational
  discontinuities 3–5 with steepening, contacts 6–8, tangential
  discontinuities more than 10 (§4).
* Compound waves (set 5) are where code and exact solver disagree: the
  code forms an intermediate shock attached to a rarefaction, while an
  ideal solver that admits rotational discontinuities does not
  ([Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md)).

**Uses in the corpus.**
* MPWENO on a Ryu–Jones problem: slow shocks crisp, 400 zones about equal to
  TVD on 800 ([Balsara & Shu (2000)](/sources/balsara-2000.md), §§VI–VII).
* ADER-WENO MHD on Ryu–Jones and Dai–Woodward problems
  ([Balsara et al. (2009)](/sources/balsara-2009.md), §§6–7).
* GP-WENO on a Ryu–Jones problem ([Reyes et al. (2018)](/sources/reyes-2018.md);
  [GP-WENO](/methods/gp-weno.md)).
* Problem 2a in rotated form, in 2D and 3D, with GLM, CT and FD-CT
  ([grid-oblique MHD shock tubes](/benchmarks/oblique-mhd-shock-tubes.md);
  [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.2.2;
  [Seo & Ryu (2023)](/sources/seo-2023.md), §3.5). Problem 1a is the
  Ryu–Jones–Frank colliding-flow tube that Tóth rotates
  ([Derigs et al. (2018)](/sources/derigs-2018.md), §5.5).

**Later uses (batch 11).**
* *Dai–Woodward table numbers in the published paper.* The published
  [Dai & Woodward (1994)](/sources/dai-1994.md) numbers its tables in
  Roman numerals, Ia/Ib to Va/Vb and VI; the "DW Table" labels in the
  table above were taken from Ryu & Jones and did not all match it
  (corrected in the table at the 2026-10-13 deep lint). In the
  published paper (Gaussian units; fields here divided by $\sqrt{4\pi}$):
  * 2a is DW Table Ia, 3a is DW Table IIa and 1b is DW Table IIIa; states,
    $B_x$ and $\gamma$ agree.
  * 1a is DW **Table VI** (Fig. 8). This corrected the earlier label "1a
    (DW Table 7)": the published paper has no Table 7.
  * 2b is in **no** published DW table. DW Table Va is a different
    problem: left $(\rho, v_x, v_y, v_z, B_y, B_z, p) = (1.1, 4, 0, 0, 5/\sqrt{4\pi}, -3.5/\sqrt{4\pi}, 5.6)$,
    right $(1, -4, 0, 0, 4/\sqrt{4\pi}, 2/\sqrt{4\pi}, 1)$, $B_x = 5/\sqrt{4\pi}$,
    $\gamma = 5/3$ (the text prints the right $v_x$ as 0, Table Va as
    $-4.0$, the state actually computed). This corrected the earlier label
    "2b (DW Table 5a)", and with it the description's earlier "several
    taken from Dai and Woodward", which holds for 1a, 1b, 2a and 3a only. The source of the
    Ryu–Jones labels is not recorded in either paper as read here.
  * DW Table IVa is the [Brio–Wu](/benchmarks/brio-wu-shock-tube.md)
    problem at its original $\gamma = 2$, where problem 5a uses 5/3
    ([Brio & Wu (1988)](/sources/brio-1988.md), §V).
* *What Dai and Woodward pose.* Their problems are Riemann-solver tests:
  each table lists the eight region states of the fan and the Newton
  iteration history (3 to 6 iterations). Only the Table VI (1a) states
  are also simulated: on $[0, 1]$ with the jump at 0.5, 200 uniform
  zones, to $t = 0.08$. For those states the solver's single-strong-wave
  initial guess fails, and the simulation code falls back to the average
  of the left and right states at the failing interfaces. The Fig. 8
  caption prints the right pressure as 2, against 1 in the text and in
  Table VI. The domain and the end time match the 1a entry above; the
  jump position, which the Ryu–Jones preprint does not state, is 0.5 in
  Dai and Woodward's run.
* *Wave content in Dai and Woodward's solutions.* For 2a: fast shocks of
  Mach 1.22 and 1.28, slow shocks of Mach 1.09 and 1.07, rotations of 12°
  and 9°. For 3a: magnetosonic shocks of Mach 12.4 (right) and 10.3
  (left). For 1b: a left fast shock of Mach 1.724, a left slow shock of
  Mach 1.457 and no rotation. For 1a: fast shocks of Mach 6.54 (right) and
  2.49 (left), a weak slow shock, a slow rarefaction and the contact.
  Their solver computes rarefactions as rarefaction shocks, so it is exact
  only for fans without rarefactions (§§4–5).

# Citations

1. [Ryu & Jones (1995)](/sources/ryu-1995.md), §§4–5 (arXiv preprint; no figures or tables).
2. [Balsara & Shu (2000)](/sources/balsara-2000.md), §§VI–VII.
3. [Balsara et al. (2009)](/sources/balsara-2009.md), §§6–7.
4. [Reyes et al. (2018)](/sources/reyes-2018.md).
5. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.2.2.
6. [Seo & Ryu (2023)](/sources/seo-2023.md), §3.5.
7. [Derigs et al. (2018)](/sources/derigs-2018.md), §5.5.
8. [Dai & Woodward (1994)](/sources/dai-1994.md), §§4–5, Tables I–VI, Fig. 8.
9. [Brio & Wu (1988)](/sources/brio-1988.md), §V.

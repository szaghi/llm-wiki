---
type: Benchmark
title: "Ryu–Jones and Dai–Woodward one-dimensional MHD shock tubes"
description: "A set of one-dimensional ideal-MHD Riemann problems, several taken from Dai and Woodward and popularized by Ryu and Jones, that together produce every 1D wave structure: fast and slow shocks and rarefactions, rotational and contact discontinuities, switch-on and switch-off waves, tangential discontinuities and compound waves; checked against a nonlinear Riemann solver."
status: established
aliases: [Ryu–Jones shock tube, Dai–Woodward shock tube, RJ2a, MHD Riemann problems]
tags: [mhd, riemann-problem, verification, benchmark, 1d]
timestamp: 2026-10-09T00:00:00Z
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
| 1a (DW Table 7) | $(1, 10, 0, 0, 5/\sqrt{4\pi}, 0, 20)$ | $(1, -10, 0, 0, 5/\sqrt{4\pi}, 0, 1)$ | $5/\sqrt{4\pi}$ | 0.08 | two fast shocks, a slow rarefaction, a slow shock, a contact |
| 1b (DW Table 3a) | $(1, 0, 0, 0, 5/\sqrt{4\pi}, 0, 1)$ | $(0.1, 0, 0, 0, 2/\sqrt{4\pi}, 0, 10)$ | $3/\sqrt{4\pi}$ | 0.03 | fast and slow shocks, contact, slow and fast rarefactions |
| 2a (DW Table 1a) | $(1.08, 1.2, 0.01, 0.5, 3.6/\sqrt{4\pi}, 2/\sqrt{4\pi}, 0.95)$ | $(1, 0, 0, 0, 4/\sqrt{4\pi}, 2/\sqrt{4\pi}, 1)$ | $2/\sqrt{4\pi}$ | 0.2 | two fast shocks, two rotational discontinuities, two slow shocks, a contact |
| 2b (DW Table 5a) | $(1, 0, 0, 0, 6/\sqrt{4\pi}, 0, 1)$ | $(0.1, 0, 2, 1, 1/\sqrt{4\pi}, 0, 10)$ | $3/\sqrt{4\pi}$ | 0.035 | as 2a, with rarefactions on the right |
| 3a (DW Table 2a) | $(0.1, 50, 0, 0, -1/\sqrt{4\pi}, -2/\sqrt{4\pi}, 0.4)$ | $(0.1, 0, 0, 0, 1/\sqrt{4\pi}, 2/\sqrt{4\pi}, 0.2)$ | 0 | 0.01 | two magnetosonic shocks, a tangential discontinuity |
| 3b | $(1, -1, 0, 0, 1, 0, 1)$ | $(1, 1, 0, 0, 1, 0, 1)$ | 0 | 0.1 | two magnetosonic rarefactions |
| 4a | $(1, 0, 0, 0, 1, 0, 1)$ | $(0.2, 0, 0, 0, 0, 0, 0.1)$ | 1 | 0.15 | a switch-on fast shock |
| 4b | $(0.4, -0.66991, 0.98263, 0, 0.0025293, 0, 0.52467)$ | $(1, 0, 0, 0, 1, 0, 1)$ | 1.3 | 0.15 | a contact and a switch-off fast rarefaction |
| 4c | $(0.65, 0.667, -0.257, 0, 0.55, 0, 0.5)$ | $(1, 0.4, -0.94, 0, 0, 0, 0.75)$ | 0.75 | 0.15 | a switch-off slow shock |
| 4d | $(1, 0, 0, 0, 0, 0, 1)$ | $(0.3, 0, 0, 1, 1, 0, 0.2)$ | 0.7 | 0.16 | a switch-on slow rarefaction |
| 5a (Brio–Wu at $\gamma = 5/3$) | $(1, 0, 0, 0, 1, 0, 1)$ | $(0.125, 0, 0, 0, -1, 0, 0.1)$ | 0.75 | 0.1 | a slow compound wave |
| 5b | $(1, 0, 0, 0, 1, 0, 1)$ | $(0.4, 0, 0, 0, -1, 0, 0.4)$ | 1.3 | 0.16 | a fast compound wave |

The tabulated analytic solutions are not in the preprint read here.

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

# Citations

1. [Ryu & Jones (1995)](/sources/ryu-1995.md), §§4–5 (arXiv preprint; no figures or tables).
2. [Balsara & Shu (2000)](/sources/balsara-2000.md), §§VI–VII.
3. [Balsara et al. (2009)](/sources/balsara-2009.md), §§6–7.
4. [Reyes et al. (2018)](/sources/reyes-2018.md).
5. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.2.2.
6. [Seo & Ryu (2023)](/sources/seo-2023.md), §3.5.
7. [Derigs et al. (2018)](/sources/derigs-2018.md), §5.5.

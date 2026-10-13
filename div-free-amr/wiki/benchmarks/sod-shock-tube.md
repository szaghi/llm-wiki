---
type: Benchmark
title: "Sod shock tube"
description: "1D Euler Riemann problem with a left rarefaction, a contact and a right shock, from Sod's 1978 scheme survey; the hydrodynamic base of the Brio-Wu MHD tube, with no divergence content of its own and no output time in the original."
status: established
aliases: [Sod problem, Sod tube]
tags: [benchmark, shock-capturing]
timestamp: 2026-10-13T00:00:00Z
---

# Sod shock tube

A one-dimensional gas-dynamics Riemann problem: two gases at rest,
separated by a diaphragm, the left one denser and at higher pressure. The
exact solution is a left-moving rarefaction, a contact (pressure and
velocity continuous, density and internal energy discontinuous) and a
right-moving shock. It tests how many zones a scheme spends on the
contact and the shock, overshoots, and the corners of the rarefaction.

## Set-up

From [Sod (1978)](/sources/sod-1978.md) §3 (p. 14, Figs. 2–3):
* Left state: density 1, pressure 1, velocity 0. Right state: density
  0.125, pressure 0.1, velocity 0.
* $\gamma = 1.4$; $h = 0.01$ (the plots span $[0,1]$, 100 points); Courant
  number 0.9 in every calculation.
* **Diaphragm position and output time are not printed.** The diaphragm
  is drawn symbolically. The shock and contact sit near $x = 0.75$ and
  $x = 0.63$ in every figure; with the exact wave speeds and a diaphragm
  at $x = 0.5$ this implies $t \approx 0.14$, a reader's estimate, not a
  printed value. An output time attributed to Sod (1978) is therefore not
  his.

## What it has shown

* **Sod's survey** (Figs. 4–15). Godunov, Lax–Wendroff and MacCormack
  spread the contact over 6–8 zones and the shock over 4–6; Rusanov is
  "extremely diffusive" (14–16 zones at the contact); artificial
  compression cuts the widths to 1–4 zones; Glimm's random choice method
  has zero-width discontinuities but a noisy rarefaction; the upwind
  scheme with a centred pressure term produces a nonphysical expansion
  shock. The "Godunov" scheme of the survey is a Lax–Friedrichs-type
  two-step scheme, not the Riemann-solver scheme
  ([Sod (1978)](/sources/sod-1978.md), Table I).
* **Higher-order Godunov MHD solvers on the hydrodynamic limit.**
  [Zachary, Malagoli & Colella (1994)](/sources/zachary-malagoli-colella-1994.md)
  §3.1: $\gamma = 1.4$, 100 points, 50 steps at Courant number 0.8 (the
  time is not given on the Source page); the shock spans 3 points and the
  contact is more diffuse without contact detection. The same paper runs a
  strong magnetized variant (zero normal field, left pressure 1000,
  $\gamma = 5/3$, 200 points).
* **WENO.** [Jiang & Shu (1996)](/sources/jiang-shu-1996.md) §8.2 Ex. 1
  run it, alongside the Lax problem, on 101 points, and an oblique version on
  $96\times16$ (§8.3 Ex. 1); output times of the 1D runs are not on the
  Source page.
* **AMR codes.** A test of the CASTRO suite
  ([Almgren et al. (2010)](/sources/almgren-2010.md) §8), and, as a
  two-phase variant, the weak-scaling workload of ALPACA to 512 nodes
  ([Hoppe et al. (2022)](/sources/hoppe-2022.md) §9.1).

## Relation to the divergence constraint

None directly: the problem is hydrodynamic and 1D. Its density and
pressure data are the base of the Brio–Wu MHD tube, which adds a normal
field 0.75, a transverse field $\pm1$ and sets $\gamma = 2$
([Brio & Wu (1988)](/sources/brio-wu-1988.md);
[rotated shock tube](/benchmarks/rotated-shock-tube.md)). Even in that
form a 1D run holds the normal field as a parameter and cannot measure a
divergence; rotation against the grid is what makes it a constraint test.

# Citations

1. [Sod (1978)](/sources/sod-1978.md), §§3–4, Table I, Figs. 2–15.
2. [Zachary, Malagoli & Colella (1994)](/sources/zachary-malagoli-colella-1994.md), §3.1, Figs. 1–2, 4.
3. [Jiang & Shu (1996)](/sources/jiang-shu-1996.md), §§8.2–8.3.
4. [Almgren et al. (2010)](/sources/almgren-2010.md), §8.
5. [Hoppe, Winter, Adami & Adams (2022)](/sources/hoppe-2022.md), §9.1, Fig. 20b.
6. [Brio & Wu (1988)](/sources/brio-wu-1988.md), §V.

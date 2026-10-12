---
type: Benchmark
title: "Hypersonic blunt-body carbuncle test (Mach 20 cylinder)"
description: "Mach 20 flow onto a circular cylinder on a body-fitted polar grid, run to a steady bow shock: complete low-dissipation Riemann solvers grow a carbuncle on the stagnation line, so the test checks shock-instability cures and the stagnation-line pressure; distinct from the Mach 3 embedded-boundary cylinder test."
status: established
aliases: [blunt-body carbuncle test, Mach 20 cylinder, hypersonic cylinder]
tags: [benchmark, euler, shock-instability, 2d, steady]
timestamp: 2026-10-12T00:00:00Z
---

# Hypersonic blunt-body carbuncle test

**Set-up.** Mach 20 flow onto a cylinder of unit radius. The grid is
body-fitted and polar, and the run continues to a steady bow shock. This
is not the [Mach 3 cylinder on a Cartesian embedded grid](/benchmarks/supersonic-cylinder-flow.md).
* **Simon & Mandal (2019).** $320\times20$ cells (circumferential by
  radial), the set-up of Huang et al., CFL 0.5, 30 000 iterations, first
  order ([Simon & Mandal (2019)](/sources/simon-2019.md), §9.4).
* **Simon & Mandal (2019b).** $320\times40$ cells. The inflow is
  $(\rho, v_x, v_y, p) = (1.4, 20, 0, 1)$. The radial grid line at $y = 0$
  is perturbed in a saw-tooth pattern by $10^{-4}$. 20 000 iterations,
  first order ([Simon & Mandal (2019b)](/sources/simon-2019-b.md), §7.3).
* **Xie et al. (2021).** $60\times280$ cells (radial by circumferential),
  initial $\rho = 1.4$, $p = 1.4$, $v_x = 20$, $v_y = 0$ as printed.
  Implicit LU-SGS, 50 000 steps, CFL 0.5; the spatial order is not
  stated ([Xie et al. (2021)](/sources/xie-2021.md), §6.4).

**Results.**
* HLLC and HLLEM form a carbuncle on the stagnation line. Both selective
  wave modification variants remove it, and their stagnation-line
  pressure is closer to the inviscid stagnation value 515.60 at the
  paper's point B (Simon & Mandal 2019, §9.4).
* For HLLEM, variant E of the selective wave modification gives the
  smoothest shock, P is comparable, and anti-diffusion control is clean.
  The shear-only control of Xie et al. (2017) turns asymmetric near the
  centreline (Simon & Mandal 2019b, §7.3).
* Godunov, Roe, HLLEM and HLLC all form carbuncles. With the
  entropy-control term, Roe gets the correct stagnation-line pressure
  "with only one interior point" in the shock (Xie et al., §6.4, Figs. 17–18).
* A shallow-water analogue gives the same picture. On a supercritical bow
  shock ahead of a cylinder, the complete augmented Roe solver forms a
  carbuncle at the nose. The two-wave HLLS solver and the shear-wave
  fixes do not, also under grid and inflow perturbations
  ([Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §§4.2.1, 6.4).

See [numerical shock instability](/definitions/numerical-shock-instability.md)
and [its cures](/methods/shock-instability-cures.md).

# Citations

1. [Simon & Mandal (2019)](/sources/simon-2019.md), §9.4.
2. [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §7.3.
3. [Xie et al. (2021)](/sources/xie-2021.md), §6.4.
4. [Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §§4.2.1, 6.4.

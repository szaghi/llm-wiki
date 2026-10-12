---
type: Benchmark
title: "Orszag–Tang vortex"
description: "A doubly periodic 2D MHD flow started from smooth sinusoidal velocity and magnetic fields that steepens into interacting shocks and current sheets; used to compare MHD solvers, divergence controls and AMR against uniform-grid references."
status: established
aliases: [Orszag-Tang, OT vortex]
tags: [benchmark, mhd, verification, amr]
timestamp: 2026-10-12T00:00:00Z
---

# Orszag–Tang vortex

**Set-up.** A uniform-density, uniform-pressure gas on a doubly periodic
unit square, with velocity $\mathbf v = (-\sin 2\pi y, \sin 2\pi x)$ and a
magnetic field whose $x$ component varies as $-\sin 2\pi y$ and whose $y$
component varies as $\sin 4\pi x$. The smooth initial state steepens into
shocks and current sheets. No exact solution exists; comparisons are
against reference runs or other codes.

**Runs.** The three sources print the same flow with different
normalizations:

* [Stone et al. (2008)](/sources/stone-2008.md), §8.4, Figs. 22–24.
  $\rho = 25/(36\pi)$, $p = 5/(12\pi)$, domain $(1, 1)$, the field derived
  from a vector potential whose $z$ component is
  $\frac{1}{\sqrt{4\pi}}\left[\frac{\cos(4\pi x)}{4\pi} + \frac{\cos(2\pi y)}{2\pi}\right]$
  (printed with an amplitude $1/\sqrt{4\pi}$). $192^2$, PPM, Roe, CTU with
  [constrained transport](/methods/constrained-transport.md), $t = 1/2$
  (stated equivalent to $t = \pi$ in Tóth 2000). Pressure slices at
  $y = 0.3125$ and $0.427$ are compared with a $512^2$ reference (Fig. 23).
  An isothermal version (Fig. 24) appears to differ significantly from
  Balsara (1998) Fig. 8. The authors judge the test "not … extremely
  discriminating". The paper's equations use units without $4\pi$, while
  this set-up carries $\sqrt{4\pi}$ (Gaussian) factors.
* [Bryan et al. (2014)](/sources/bryan-2014.md), §11.2.10, Fig. 14.
  $\rho = 25/(36\pi)$, $p = 5/(12\pi)$, $\mathbf v = (-\sin 2\pi y, \sin 2\pi x)$,
  $\mathbf B = (-\sin 2\pi y, \sin 4\pi x)$, to $t = 0.48$. The
  [constrained-transport](/methods/constrained-transport.md) solver and the
  [Dedner GLM](/methods/glm-divergence-cleaning.md) solver give
  "approximately equal effective resolution". The resolution is not
  printed; the comparison is qualitative.
* [Zhang et al. (2018)](/sources/zhang-2018.md), §5.1(iii), eq. 18,
  Figs. 9–10. Uniform $\rho$ and $p$; velocity amplitude $c_s$ and field
  amplitude $\sqrt{p/\gamma}$ in the same sinusoidal pattern, coordinates
  in units of the box side; $\gamma = 5/3$, Courant factor 1/2; PLM or
  PPM with Roe (which reconstruction the figure uses is not stated
  precisely); output at half a box sound-crossing time. AMR on a $256^2$
  base with 3 levels, refining where $|\mathbf J|/|\mathbf B| > 3.2/h_l$,
  about $3.6\times10^5$ cells, filling fractions 24.0%, 8.5% and 3.3%,
  against a $1024^2$ uniform reference (equal to AMR level 2). AMR/uniform
  ratios of magnetic and gas pressure are about 1 except at shocks and
  reconnection layers (Fig. 10). The reconnection is described as
  resembling a Sweet–Parker variant.

The magnetic-field amplitudes differ between the sources ($1/\sqrt{4\pi}$
in Stone et al., 1 in Bryan et al.). Stone et al.'s set-up is in Gaussian
units (its $\sqrt{4\pi}$ factors); Bryan et al.'s field units for this test
are not stated, so whether the two set-ups are the same problem is not
established.

**What it shows.** Used qualitatively in all three: symmetry, absence of
oscillations, agreement of [AMR](/methods/adaptive-mesh-refinement.md)
with uniform grids, and the effective resolution of competing
divergence-control schemes. No error norms are reported.

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §8.4.
2. [Bryan et al. (2014)](/sources/bryan-2014.md), §11.2.10 (arXiv v1).
3. [Zhang et al. (2018)](/sources/zhang-2018.md), §5.1(iii) (arXiv v4).

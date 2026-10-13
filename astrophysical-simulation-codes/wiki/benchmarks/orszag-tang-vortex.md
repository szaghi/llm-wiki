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

## Later uses (batch 3)

* *2D, IDEFIX* ([Lesur et al. (2023)](/sources/lesur-2023.md), §4.2,
  Figs. 10–11; [IDEFIX](/software/idefix.md)). The Stone et al. (2008)
  normalization: unit periodic square, $p = 5/(12\pi)$, $\rho = 25/(36\pi)$,
  $\mathbf v = (-\sin 2\pi y, \sin 2\pi x)$, field components
  $-B_0\sin 2\pi y$ and $B_0\sin 4\pi x$ with $B_0 = 1/\sqrt{4\pi}$, to
  $t = 0.5$. Cuts at $y = 0.316$ and $0.425$ (Stone et al. 2008: 0.3125
  and 0.427); RK3+PPM+Roe is "most accurate" among the combinations
  shown; $|\nabla\cdot\mathbf B| \ll 10^{-12}$ in all runs, with
  [constrained transport](/methods/constrained-transport.md). Recorded as
  printed: the text gives the resolution as "$128^3$, plus a reference
  case at $512^3$", Fig. 10 as $128^2$ up to $1024^2$, and Fig. 11 a
  $1024^2$ reference.
* *3D extension as a performance workload, IDEFIX*
  ([Lesur et al. (2023)](/sources/lesur-2023.md), §5, Tables 3–4, Fig. 18).
  $\mathbf v = (-\sin 2\pi y,\ \sin 2\pi x + \cos 2\pi z,\ \cos 2\pi x)$ and
  field components $B_0$ times $(-\sin 2\pi y,\ \sin 4\pi x,\ \cos 2\pi x + \sin 2\pi y)$,
  $B_0 = 1/\sqrt{4\pi}$, to $t = 1.0$; HLLD, PLM, RK2, double precision.
  The solution is compared with [PLUTO](/software/pluto.md) "to check for convergence", but no
  result is shown. The throughput and weak-scaling numbers are on the
  [IDEFIX](/software/idefix.md) page.
* *3D, Cholla* ([Caddy & Schneider (2024)](/sources/caddy-2024.md),
  §3.1.6, Fig. 12; [Cholla](/software/cholla.md)). Periodic unit cube,
  $192^3$ cells, $t = 0.5$, $\rho = 25/(36\pi)$, $p = 5/(12\pi)$; the
  velocity is printed with the opposite sign to the set-up above,
  $(\sin 2\pi y, -\sin 2\pi x)$; the field comes from a vector potential
  whose $z$ component is $(B_0/4\pi)(\cos 4\pi x + 2\cos 2\pi y)$, with
  $B_0$ printed ambiguously as "$1\sqrt{4\pi}$". With $B_0 = 1/\sqrt{4\pi}$
  this is Stone et al.'s potential (compiler's algebra). Qualitative
  comparison with Stone et al. (2008), Fig. 22; also a regression test of
  the code's suite.
* *3D variant as a performance workload, gPLUTO*
  ([Rossazza et al. (2026)](/sources/rossazza-2026.md), §4.1, eq. 9,
  Figs. 5–7, Tables 2–4; [gPLUTO](/software/gpluto.md)). Periodic unit
  cube, $\rho = 25/9$, $p = 5/3$,
  $\mathbf v = (-\zeta\sin 2\pi y,\ \zeta\sin 2\pi x,\ 0.2\sin 2\pi z)$ with
  $\zeta = 1 + \sin(2\pi z)/5$, $\mathbf B = (-\sin 2\pi y, \sin 4\pi x, 0)$,
  "similar to" Helzel et al. (2011); $t = 0.5$; SSP-RK3, WENOZ, HLLD,
  FP64; upwind [constrained transport](/methods/constrained-transport.md)
  for weak scaling and [GLM cleaning](/methods/glm-divergence-cleaning.md)
  for strong scaling. Per-node grids of $704\times704\times352$ (Leonardo
  Booster, MareNostrum 5 ACC), $704\times704\times350$ (Leonardo DCGP)
  and $512^3$ (MeluXina). Performance only: no solution, error norm or
  divergence diagnostic is shown. The scaling results are on the
  [gPLUTO](/software/gpluto.md) and
  [parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md)
  pages.

On normalization (compiler's algebra, not stated by the sources): ideal
MHD is invariant under multiplying $\rho$, $p$ and $B^2$ by one constant
at fixed $\mathbf v$. With the factor $4\pi$, the Stone et al. (2008),
IDEFIX and Cholla values $\rho = 25/(36\pi)$, $p = 5/(12\pi)$, field
amplitude $1/\sqrt{4\pi}$ become gPLUTO's $\rho = 25/9$, $p = 5/3$, field
amplitude 1, so gPLUTO's 3D variant has the same 2D core plus its
$z$-modulation. Bryan et al.'s $\rho = 25/(36\pi)$, $p = 5/(12\pi)$ with
field amplitude 1 maps onto neither, which leaves open the question of
its field units raised above. Of the batch-3 runs, only IDEFIX's 2D test
reports a quantitative diagnostic (the divergence bound); the 3D versions
are used as qualitative regression tests (Cholla) or as performance
workloads (IDEFIX, gPLUTO).

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §8.4.
2. [Bryan et al. (2014)](/sources/bryan-2014.md), §11.2.10 (arXiv v1).
3. [Zhang et al. (2018)](/sources/zhang-2018.md), §5.1(iii) (arXiv v4).
4. [Lesur et al. (2023)](/sources/lesur-2023.md), §4.2, §5 (arXiv v1).
5. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.1.6 (arXiv v2).
6. [Rossazza et al. (2026)](/sources/rossazza-2026.md), §4.1 (arXiv v1).

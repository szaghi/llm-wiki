---
type: Benchmark
title: "Orszag–Tang vortex"
description: "Periodic two-dimensional ideal-MHD benchmark in which smooth vortical velocity and magnetic fields steepen into interacting shocks and current sheets; used for high-order MHD shock capturing, density-bound limiting and divergence control."
status: established
aliases: [Orszag–Tang, Orszag–Tang MHD vortex, OT vortex]
tags: [benchmark, mhd, dg, teno, limiting]
timestamp: 2026-10-21T12:00:00Z
---

# Orszag–Tang vortex

The Orszag–Tang vortex is the ideal-MHD analogue of a two-dimensional
vortex problem: on a periodic unit square, a smooth velocity field
$v=(-\sin2\pi y,\ \sin2\pi x)$ and a magnetic field with a doubled $x$
wavenumber are superposed on a uniform density and pressure. The
smooth data steepen into MHD shocks by the output times, so a scheme
must capture them, keep density within bounds and control
$\nabla\cdot B$, while the structure that develops between the shocks
serves as a visual measure of resolution.

## Setup

[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md)
§5.3.1 print, on periodic $[0,1]^2$,

$$
\begin{aligned}
\rho&=\frac{25}{36\pi},\qquad p=\frac{5}{12\pi},\qquad
(v_1,v_2)=\big(-\sin(2\pi y),\ \sin(2\pi x)\big),\\
(B_1,B_2)&=\frac{1}{\sqrt{4\pi}}\big(-\sin(2\pi y),\ -\sin(4\pi x)\big),
\end{aligned}
$$

with $\gamma$ not stated, to $t=1$ (figures at $t=0.5$ and $1$), in
GLM-MHD form (divergence cleaning by the field $\psi_{\mathrm{GLM}}$;
$\nabla\cdot B=0$ is not enforced exactly).
[Fu (2023)](/sources/fu-2023.md) §5.3 reproduces Orszag–Tang results
from the TENO-MHD paper it reviews, on $200\times200$, with a
WENO5-JS reference on $512\times512$ and 30 density contours from 1.1
to 6.3, without reprinting the data; the reviewed work (Fu & Tang) uses
an unstaggered constrained-transport framework for the [divergence-free](/properties/divergence-free-magnetic-field.md)
constraint.

## Runs in the sources

| Source | Scheme | Grid | Divergence treatment |
|---|---|---|---|
| [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) §5.3.1 | split-form [DGSEM](/methods/dgsem.md), $N=3$, Chandrashekar–Klingenberg volume flux, LLF surface flux, subcell-wise [FV blending](/methods/subcell-finite-volume-limiting.md) | $256^2$ elements | GLM cleaning |
| [Fu (2023)](/sources/fu-2023.md) §5.3, Fig. 19 (reproduced) | [TENO-A](/methods/adaptive-teno.md), 5 to 8 points | $200^2$ | constrained transport |

## Findings

**Bounds that can always be met.** Rueda-Ramírez et al. impose on
density a local discrete maximum principle ("TVD-like" bounds, Eq.
(53)) taken from the low-order solution of the next Runge–Kutta stage,
following earlier work. Because the low-order finite-volume methods are
monotone in primitive variables, these bounds can always be met.
Second-order finite volumes (minmod on primitive variables) give looser
bounds than first-order ones, hence less limiting and more turbulent
structures (Figs. 10–11). The same paper applies the blending to the
[KPP problem](/benchmarks/kpp-rotating-wave.md), the
[Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
and the [high-Mach jet](/benchmarks/high-mach-astrophysical-jet.md),
with different bounds for each.

**Adaptive dissipation at high order.** Fu (2023) shows TENO5-A to
TENO8-A on $200^2$ against WENO5-JS on $512^2$, as evidence that the
adaptive TENO family carries over to MHD with constrained transport
(Fig. 19).

## Qualifications

- Both sources compare contour plots; neither reports an error norm.
- Fu (2023) is a review: the run is reproduced from the cited TENO-MHD
  work and its setup is not reprinted, so grid, time and data
  differences between the two runs cannot be checked from the bundle.
  Its contour range, 1.1 to 6.3, lies far above the uniform initial
  density $25/(36\pi)\approx0.221$ of Rueda-Ramírez et al., which
  points to a different normalization of the data *(compiler check, not
  in the sources)*.

# Citations

- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §5.3.1, Eq. (53), Figs. 10–11 (arXiv v2).
- [Fu (2023)](/sources/fu-2023.md) — §5.3, Fig. 19 (reproduced).

---
type: Benchmark
title: "Orszag–Tang vortex"
description: "Periodic two-dimensional ideal-MHD benchmark in which smooth vortical velocity and magnetic fields steepen into interacting shocks and current sheets; used for high-order MHD shock capturing, density-bound limiting, entropy stability and divergence control, in two normalizations that differ by a rescaling."
status: established
aliases: [Orszag–Tang, Orszag–Tang MHD vortex, OT vortex]
tags: [benchmark, mhd, dg, teno, limiting]
timestamp: 2026-10-22T12:00:00Z
---

# Orszag–Tang vortex

The Orszag–Tang vortex is the ideal-MHD analogue of a two-dimensional
vortex problem: on a periodic square, a smooth velocity field
$v=(-\sin2\pi y,\ \sin2\pi x)$ (in unit-square coordinates) and a
magnetic field with a doubled $x$ wavenumber are superposed on a
uniform density and pressure. The smooth data steepen into MHD shocks
by the output times, so a scheme must capture them, keep density within
bounds and control $\nabla\cdot B$, while the structure that develops
between the shocks serves as a visual measure of resolution.

## Setup

Two normalizations are printed.

**Unit square.** [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md)
§5.3.1 and [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md)
§6.2 print, on periodic $[0,1]^2$,

$$
\begin{aligned}
\rho&=\frac{25}{36\pi},\qquad p=\frac{5}{12\pi},\qquad
(v_1,v_2)=\big(-\sin(2\pi y),\ \sin(2\pi x)\big),\\
(B_1,B_2)&=\frac{1}{\sqrt{4\pi}}\big(-\sin(2\pi y),\ -\sin(4\pi x)\big),
\end{aligned}
$$

to $t=1$, in GLM-MHD form (divergence cleaning by the field
$\psi_{\mathrm{GLM}}$; $\nabla\cdot B=0$ is not enforced exactly). The
2022 paper does not state $\gamma$; the 2021 paper states $\gamma=5/3$,
$\mu_0=1$ (magnetic permeability, page-local) and a unit sound speed.

**$2\pi$-periodic square.** [Liu et al. (2021)](/sources/liu-2021.md)
§4.2 print, on periodic $[0,2\pi]^2$ with $\gamma=5/3$,
$\rho=\gamma^2$, $p=\gamma$, $v=(-\sin y,\ \sin x,\ 0)$,
$B=(-\sin y,\ \sin2x,\ 0)$, to $t=3$.

The two are one problem up to a rescaling *(compiler check, not in the
sources)*. Multiplying $\rho$, $p$ and $|B|^2$ of the unit-square data
by $4\pi$ gives $\rho=25/9=\gamma^2$, $p=5/3=\gamma$ and $|B|$ of order
one, and leaves every wave speed unchanged, since ideal MHD is
invariant under a common scaling of $\rho$, $p$ and $|B|^2$ at fixed
velocity; both states have unit sound speed,
$\gamma p/\rho=1$. Stretching $x$ by $2\pi$ at unchanged velocity
stretches $t$ by $2\pi$, so Liu et al.'s $t=3$ corresponds to
$t=3/(2\pi)\approx0.477$ in the unit square, close to the $t=0.5$
snapshots and pressure slices of Rueda-Ramírez et al. (2021); both
unit-square papers run to $t=1$. The printed sign of $B_2$ differs
($-\sin4\pi x$ against $+\sin2x$); no source comments on it.

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
| [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) §6.2 | entropy-stable DGSEM, $N=3$ and $7$, element-wise blending with first-order FV or the TVD-ES [subcell scheme](/methods/tecno-scheme.md), indicator on $p$; code [FLUXO](/software/fluxo.md) | $256^2$, $512^2$, $1024^2$ DOFs | GLM cleaning with Powell and GLM non-conservative terms |
| [Liu et al. (2021)](/sources/liu-2021.md) §4.2 | finite-volume [WLS-ENO](/methods/wls-eno.md), locally divergence-free, second and third order, HLL flux, positivity-preserving framework | $200^2$ (both orders), $600^2$ (second order) | locally divergence-free reconstruction plus Godunov–Powell source term |

## Findings

**Bounds that can always be met.** Rueda-Ramírez et al. (2022) impose on
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

**Second-order subcells and convergence to a reference code.**
Rueda-Ramírez et al. (2021) first run pure finite volumes ($\alpha=1$)
on $256^2$ DOFs with $N=7$ at $t=0.5$: the entropy-stable TVD
reconstruction resolves more and imprints the irregular
Legendre–Gauss–Lobatto subcell mesh less than first-order FV, and of
three treatments of the boundary subcells the one without boundary
reconstruction is best (Fig. 6). The blended scheme then converges with
resolution towards Athena solutions (second-order FV, constrained
transport, Rusanov flux, $1024^2$ and $2048^2$) in pressure slices at
$y=0.3125$ and $y=0.4277$; $N=7$ captures some features better than
$N=3$ and needs a smaller blending coefficient (Figs. 7–10). The total
mathematical entropy stays constant while the solution is smooth and
decreases once shocks form (Fig. 11); see
[entropy stability](/properties/entropy-stability.md).

**Divergence and energy without a limiter.** Liu et al. use no limiter
besides the positivity-preserving one: their locally divergence-free
WLS-ENO captures the shocks sharply (density profiles along
$y=0.625\pi$, shocks near $x=0.5$, $1.6$, $4.4$), keeps the divergence
norm controlled over time and conserves total energy to a relative
deviation within $10^{-5}$ at third order on $200^2$ (Figs. 5–8).

**Adaptive dissipation at high order.** Fu (2023) shows TENO5-A to
TENO8-A on $200^2$ against WENO5-JS on $512^2$, as evidence that the
adaptive TENO family carries over to MHD with constrained transport
(Fig. 19).

## Qualifications

- All four sources compare contour plots or slices; none reports an
  error norm. Rueda-Ramírez et al. (2021) compare with another code.
- Fu (2023) is a review: the run is reproduced from the cited TENO-MHD
  work and its setup is not reprinted, so grid, time and data
  differences between the runs cannot be checked from the bundle.
  Its contour range, 1.1 to 6.3, lies far above the uniform initial
  density $25/(36\pi)\approx0.221$ of the unit-square normalization and
  brackets the uniform density $\gamma^2=25/9\approx2.78$ of the
  $2\pi$-periodic one, which points to that normalization *(compiler
  check, not in the sources)*.
- Liu et al. cite "Orszag-Tang (1979)" without a reference-list entry.

# Citations

- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §5.3.1, Eq. (53), Figs. 10–11 (arXiv v2).
- [Fu (2023)](/sources/fu-2023.md) — §5.3, Fig. 19 (reproduced).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §6.2, Figs. 6–11 (arXiv v1).
- [Liu et al. (2021)](/sources/liu-2021.md) — §4.2, Figs. 5–8.

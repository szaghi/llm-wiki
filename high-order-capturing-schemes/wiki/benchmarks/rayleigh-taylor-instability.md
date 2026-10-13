---
type: Benchmark
title: "Rayleigh–Taylor instability"
description: "Heavy fluid (density 2) below light fluid (density 1) on [0, 0.25]×[0, 1], accelerated toward the light fluid, γ = 5/3, with a single-mode velocity perturbation of the interface: the Xu–Shu set-up, run to t = 1.95 to compare the small-scale roll-up and bubble and spike positions of low-dissipation schemes and Riemann solvers."
status: established
aliases: [Rayleigh–Taylor, RT instability, Xu–Shu Rayleigh–Taylor problem]
tags: [benchmark, euler, 2d, contact-discontinuity, source-terms, low-dissipation]
timestamp: 2026-10-13T00:00:00Z
---

# Rayleigh–Taylor instability

**Set-up.** Both sources credit the problem to Xu and Shu (2005), which
is not ingested. A contact at $y = \tfrac12$ separates a heavy fluid
below from a light fluid above, in hydrostatic balance under a unit
acceleration pointing from the heavy to the light fluid. A
single-mode velocity perturbation makes the heavy fluid rise in spikes
and the light fluid sink in bubbles, which roll up on the contact. On
$[0, 0.25]\times[0, 1]$ with $\gamma = 5/3$,
$$(\rho, v_x, v_y, p) = \begin{cases}(2,\ 0,\ -0.025\,c\cos(8\pi x),\ 1 + 2y), & 0 \le y < \tfrac12,\\ (1,\ 0,\ -0.025\,c\cos(8\pi x),\ y + \tfrac32), & \tfrac12 \le y \le 1,\end{cases}$$
with $c = \sqrt{\gamma p/\rho}$ the local sound speed
([Fu, Hu & Adams (2016)](/sources/fu-2016.md), §5.6, eq. 41;
[Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §III I, eq. 27).
The perturbation is one wavelength across the domain and symmetric
about $x = 0.125$ (compiler's check).
* *Source term.* Deng et al. add $\rho$ to the right-hand side of the
  $y$-momentum equation and $\rho v_y$ to the energy equation, that is
  $\mathbf g = (0, 1)$ in a balance law with source $\mathbf s(u)$.
  Fu et al. do not print the source term; their pressure is the same
  hydrostatic profile, $\partial_y p = \rho$ in each layer (compiler's
  check).
* *Boundaries* ([Fu, Hu & Adams (2016)](/sources/fu-2016.md), §5.6).
  Reflective on the left and right; fixed states
  $(\rho, v_x, v_y, p) = (2, 0, 0, 1)$ at the bottom and $(1, 0, 0, 2.5)$
  at the top. Deng et al. print no boundary conditions.
* *End time.* $t = 1.95$ ([Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md),
  §III I). Fu et al. print none, in text or captions.
* *As printed.* Deng et al.'s text places the initial contact at
  $y = 0.0$, against $y = 0.5$ in their eq. 27.

**Runs.**

| Source | Scheme | Grid | Compared | Findings |
|---|---|---|---|---|
| [Fu, Hu & Adams (2016)](/sources/fu-2016.md), §5.6, Figs. 19–20 | characteristic FD with Roe-averaged eigenvectors and global Lax–Friedrichs splitting, wavelet-based multiresolution, SSP-RK2, CFL 0.6 (§5) | $128\times512$ and $256\times1024$ ($h = 1/512$ and $1/1024$) | [WENO-JS](/methods/weno.md), [WENO-Z](/methods/weno-z.md), WENO-CU6, WENO-CU6-M and four [TENO](/methods/teno.md) schemes | TENO5 and TENO5-opt resolve "much richer vortical structures" than WENO-JS and WENO-Z; at $128\times512$ they match WENO-JS and WENO-Z at $256\times1024$. Their low dissipation breaks the symmetry of the flow, which a more dissipative scheme keeps even on much finer grids; WENO-CU6 loses it at $256\times1024$ |
| [Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §III I, Fig. 15 | second-order MUSCL finite volume, CFL 0.4 (the paper's default) | $60\times240$ | [HLL](/methods/hll-riemann-solver.md), [HLLC](/methods/hllc-riemann-solver.md) and HLL-BVD ([approximate Riemann solvers](/methods/approximate-riemann-solvers.md)) | HLL is the most diffusive and cannot keep the contact sharp; HLLC and HLL-BVD both give high resolution, HLL-BVD the sharper interfaces. HLL underestimates the growth of bubble and spike tips |

Comparisons are visual in both sources: density contours, and in Deng
et al. the bubble and spike tip positions against time. Neither gives
an error norm or a reference solution. On the tip positions Deng et
al.'s caption calls HLLC and HLL-BVD "practically indistinguishable",
while their text says "the HLL and HLL-BVD produce very similar
prediction" right after saying HLL underestimates the tips; the caption
is taken here, and the text's "HLL" is recorded as printed.

**What the test measures.** The instability grows from a contact, so it
rewards schemes that keep contacts sharp and resolve small vortical
scales. Fu et al. use it for the dissipation of the reconstruction,
Deng et al. for the contact dissipation of the Riemann solver
([contact sharpening](/methods/contact-sharpening.md) is a related route).
Symmetry is not a correctness criterion on its own: Fu et al. read its
loss as a consequence of low dissipation, citing Shi, Zhang and Shu
(2003, not ingested), whose dissipative runs stay symmetric even when
refined.

**With shocks.** A survey figure (reproduced from Zhang, Shu and Zhou,
2006, not ingested) shows a ninth-order WENO simulation of the flow at
$T = 6.0$ and of a Mach 12 shock hitting the interface from above or
below at $T = 3.0$; the shocks "speed up the transition" to full
instability. The set-up is not printed
([Shu (2009)](/sources/shu-2009.md), §6, Fig. 6.2).

# Citations

1. [Fu, Hu & Adams (2016)](/sources/fu-2016.md), §§5, 5.6, Figs. 19–20.
2. [Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §§III, III I, Fig. 15.
3. [Shu (2009)](/sources/shu-2009.md), §6, Fig. 6.2.

---
type: Benchmark
title: "Sedov–Taylor blast wave"
description: "A point explosion in a uniform cold medium whose self-similar solution (shock radius growing as $t^{2/5}$ for a spherical blast and $t^{1/2}$ for a cylindrical one) is known analytically; it tests strong-shock capturing, the preservation of spherical or cylindrical symmetry on Cartesian and curvilinear grids, and AMR."
status: established
aliases: [Sedov blast, Sedov–Taylor explosion, point explosion]
tags: [benchmark, hydro, verification, amr]
timestamp: 2026-10-12T00:00:00Z
---

# Sedov–Taylor blast wave

**Set-up.** A finite energy is deposited in a small region of a uniform
medium at negligible pressure. The resulting blast is self-similar, and
the analytic solution gives the shock radius and the profiles of density,
velocity and pressure. In $d$ dimensions the symmetry is spherical (3D,
or 2D axisymmetric) or cylindrical (2D Cartesian).

**Runs.**

* [Almgren et al. (2010)](/sources/almgren-2010.md), §8.2, eq. 44,
  Figs. 6–8. Explosion energy 1 erg, ambient $\rho = 1$ g cm⁻³ and
  $p = 10^{-5}$ dyn cm⁻², deposited within radius 0.01 cm as a pressure
  $(\gamma - 1)$ times the energy over the initial volume, with 10-fold
  subsampling of the initial region; $\gamma = 1.4$. Base cell 0.03125 cm
  (32 cells on $[0, 1]$ cm; the 2D axisymmetric case uses one quadrant
  $[0, 0.5]$), with 3 levels of ratio 2 (effective cell 0.00390625 cm) or 4
  levels (0.001953125 cm); CFL 0.5 with the first step shrunk by a factor
  100; refinement where $\rho > 3$, $|\nabla\rho| > 0.01$, $p > 3$ or
  $|\nabla p| > 0.01$; new PPM limiters. Spherical blasts in 1D spherical,
  2D $r$–$z$ and 3D Cartesian coordinates at $t = 0.01$ s (Figs. 6–7); a
  cylindrical blast in 2D Cartesian at $t = 0.1$ s (Fig. 8). Exact solution
  from the Kamm & Timmes (2007) code. Density, velocity and pressure match
  well; the internal energy is hardest near the origin and improves with 4
  levels. Qualitative only.
* [Bryan et al. (2014)](/sources/bryan-2014.md), §11.2.5, Figs. 8–9. 2D,
  $\rho = 1$, explosion energy 10 in one central cell, reflecting box of
  side 1, $100\times100$ root grid with 4 AMR levels (ratio 2; refined on
  shocks and density and energy slopes), output at $t = 0.07$. The shock
  radius follows (energy$/\rho$)$^{1/5}t^{2/5}$ with a constant 1.0 "for
  cylindrical symmetry and an ideal gas with $\gamma = 1.4$" (eq. 104), as
  printed; $t^{2/5}$ is the spherical law, and a cylindrical blast grows as
  (energy per unit length$/\rho$)$^{1/4}t^{1/2}$, so eq. 104 mixes the two
  (compiler's check against the standard similarity solution). PPM
  matches the analytic profiles "extremely well"; ZEUS lags, with early
  energy loss and a diamond-shaped front, which Clarke (2010) attributes to
  its internal-energy formulation.
* [Stone et al. (2020)](/sources/stone-2020.md), §3.4.4, Figs. 23–25. 3D,
  periodic box of side 1, $\rho = 1$, $p = 0.001$, total energy 1 within
  radius 0.01 (pressure $1.6\times10^5$), $\gamma = 5/3$. VL2+PLM with
  HLLE (hydro) or HLLD (MHD, with $B_x = \sqrt3$, $B_y = 1$). AMR on a
  $128^3$ root with 2 levels (effective $512^3$), refining where the cell
  size times the maximum of $|\nabla p|/p$ exceeds 0.1 (hydro) or 0.2
  (MHD), derefining below a quarter of that (eq. 28), against uniform
  $512^3$. Visually identical to the uniform run; spherical symmetry kept
  in hydro and reflection symmetry in MHD; excellent agreement with the
  analytic solution (sedov3.f, Timmes). The CFL number is not printed.
* *Spherical-polar mesh* ([Stone et al. (2020)](/sources/stone-2020.md),
  §3.5.3, Figs. 30–32). The same blast on a wedge
  $0.5 < r < 1.5$, $\pi/6 < \theta < \pi/2$, $-\pi/5 < \phi < \pi/5$ with
  nonuniform radial spacing and AMR, the MHD field along the pole.
  Spherical symmetry is maintained and the result agrees with the
  Cartesian run; the peak is slightly smeared by the larger cells at large
  radius.

Blasts in strongly magnetized media, with anisotropic shocks, are the
[MHD blast wave](/benchmarks/mhd-blast-wave.md).

**What it shows.** Symmetry preservation and AMR fidelity on both
Cartesian and curvilinear meshes
([Stone et al. (2020)](/sources/stone-2020.md), §3.4.4, §3.5.3;
[Almgren et al. (2010)](/sources/almgren-2010.md), §8.2), and it
separates PPM from ZEUS, which solves the internal rather than the total energy ([Bryan et al. (2014)](/sources/bryan-2014.md), §11.2.5). All
comparisons are visual or profile overlays; no error norms are reported.

# Citations

1. [Almgren et al. (2010)](/sources/almgren-2010.md), §8.2 (arXiv v1).
2. [Bryan et al. (2014)](/sources/bryan-2014.md), §11.2.5 (arXiv v1).
3. [Stone et al. (2020)](/sources/stone-2020.md), §3.4.4, §3.5.3.

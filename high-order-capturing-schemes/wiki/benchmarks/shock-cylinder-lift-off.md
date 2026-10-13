---
type: Benchmark
title: "Shock-driven cylinder lift-off"
description: "A Mach 3 (or 6) shock in a [0, 1] × [0, 0.2] channel hits a free cylinder of radius 0.05 resting near the lower wall, lifting and carrying it; the standard test of moving-boundary inverse Lax–Wendroff treatments, in inviscid, viscous, 3D and elastic variants."
status: established
aliases: [cylinder lift-off, shock–cylinder interaction with a moving body, Tan–Shu lift-off problem]
tags: [benchmark, euler, navier-stokes, moving-boundary, boundary-treatment, fsi]
timestamp: 2026-10-13T00:00:00Z
---

# Shock-driven cylinder lift-off

**Set-up** (after Tan and Shu 2011, as used by the papers below). In the
channel $[0, 1]\times[0, 0.2]$, a shock starts at $x = 0.08$ and moves
right into gas at rest with $\rho = 1.4$, $p = 1$. A free cylinder of
radius 0.05 and density 10.77 sits near the lower wall. The reflected
shock hits the wall, the uneven pressure lifts the body, and later Mach
reflections from the walls reach it. The grid is Cartesian and the body
boundary is imposed by moving-boundary
[inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md).

**Variants.**
* *Viscous, rigid.* Centre $(0.15, 0.05)$, so the body touches the wall,
  with an isothermal no-slip surface at $T_b = 5/7$, $\mathrm{Pr} = 0.7$,
  $h = 1/640$, $\mathrm{Re} = 10^7$, 1000 and 500, and $M_s = 3$ and 6.
  All runs are stable. At $\mathrm{Re} = 1000$, $M_s = 3$, the centre
  trajectory converges from $h = 1/160$ to $1/1280$
  ([Liu et al. (2023)](/sources/liu-2023.md), Example 6, Fig. 8).
* *3D, rigid.* The same cylinder extruded in $z$, and a sphere of the
  same radius and centre, at $M_s = 3$ and 6, inviscid and viscous.
  Results agree visually with the 2D runs, and only contour plots are
  given ([Liu et al. (2022)](/sources/liu-2022.md), §§5.2–5.3).
* *Elastic.* A deforming elastic cylinder centred at $(0.15, 0.055)$, at
  $M_s = 3$, $h = 1/800$, compared with a rigid-body ILW computation. The
  stiffer solid approaches the rigid case, and the mass-centre position
  converges under refinement. The rigid reference at $t = 0.16$ is
  $(x_c, y_c) = (0.33987, 0.076657)$
  ([Liu et al. (2025)](/sources/liu-2025.md), Example 6, Table 7).

**Later uses (batch 11).** *Origin.* The problem was introduced by
[Falcovitz, Alfandary & Hanoch (1997)](/sources/falcovitz-1997.md), §5,
Fig. 5, so the set-up line above ("after Tan and Shu 2011") names a later
form of it, not its source. The original is the same problem in other
units: domain $100\times20$ on $200\times40$ cells (mesh $R/10$); a
50-sided polygon of radius $R = 5$ centred at $(15, 5)$, resting on the
floor, density 0.01; gas at rest with $\rho = 0.0013$, $p = 10^{-6}$,
$\gamma = 1.40$; an $M_s = 3.0$ shock starting 8 from the left;
post-shock inflow on the left, non-reflecting outflow on the right, rigid
walls top and bottom; CFL about 0.5. Every length is 100 times the
Tan–Shu value, and the solid-to-gas density ratio is the same
($0.01/0.0013 = 10.77/1.4 = 7.69$; the caption prints 8). Apart from the
×100 lengths, only the gas state differs. *Compiler's arithmetic, not printed:* with the original
sound speed $\sqrt{1.4\times10^{-6}/0.0013} = 0.0328$, one Tan–Shu time
unit is about $3.05\times10^3$ original units, so the original plots at
$T = 500$ and 1000 correspond to $t \approx 0.164$ and 0.33, and the
grid to $h = 1/200$. The original scheme is a dimensionally split GRP
scheme with conservative moving cut cells
([cut-cell finite volume](/methods/cut-cell-finite-volume.md)), not ILW.
It runs Mach 3 only (the Mach 6 case is later), and its output is
qualitative: the initial lift comes from the asymmetric shock reflection
at the floor; there is no trajectory, resolution study or comparison.
Whether Tan and Shu cite the original cannot be checked here.

# Citations

1. [Liu et al. (2023)](/sources/liu-2023.md), Example 6.
2. [Liu et al. (2022)](/sources/liu-2022.md), §§5.2–5.3.
3. [Liu et al. (2025)](/sources/liu-2025.md), Example 6.
4. [Falcovitz, Alfandary & Hanoch (1997)](/sources/falcovitz-1997.md), §5.

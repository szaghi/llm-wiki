---
type: Benchmark
title: "Brio–Wu MHD shock tube"
description: "The MHD analogue of Sod's problem, (ρ, p, B_y) = (1, 1, 1 | 0.125, 0.1, −1) with B_x = 0.75 and γ = 2: fast rarefactions, a compound wave (intermediate shock attached to a slow rarefaction), a contact and a slow shock; also run rotated on a 2D grid to test divergence control."
status: established
aliases: [Brio-Wu problem, Brio–Wu Riemann problem, MHD shock tube]
tags: [benchmark, mhd, riemann-problem, 1d]
timestamp: 2026-10-08T00:00:00Z
---

# Brio–Wu MHD shock tube

**Set-up** (Brio and Wu, as stated by [Jiang & Wu (1999)](/sources/jiang-1999.md), §3.1).
On $[-1, 1]$, $(\rho, v_x, v_y, v_z, B_y, B_z, p) = (1, 0, 0, 0, 1, 0, 1)$
for $x < 0$ and $(0.125, 0, 0, 0, -1, 0, 0.1)$ for $x > 0$, with
$B_x = 0.75$ and $\gamma = 2$, run to $t = 0.2$. The waves are, from left to
right: a fast rarefaction; a compound wave, in which an intermediate shock
($B_y$ from 0.58 to −0.31) is attached to a slow rarefaction ($B_y$ from
−0.31 to −0.53); a contact; a slow shock; and a fast rarefaction. MHD is
not genuinely nonlinear, and the structure of intermediate shocks is not
unique, so a capturing scheme's result can depend on its numerical
dissipation (§§1, 4).

**Results.**
* Fifth-order FD-WENO with characteristic decomposition on 800 points
  agrees with Brio and Wu's second-order result, with 4–5 points per
  shock. Small oscillations at the trailing edge of the right-moving fast
  rarefaction disappear when the problem is computed in a moving frame
  ([Jiang & Wu (1999)](/sources/jiang-1999.md), §3.1, Fig. 2).
* **Rotated by 45° on a 2D grid** ($600^2$ on $[-1, 1]^2$): with a
  projection of $\mathbf B$ onto divergence-free fields the result matches
  the 1D one. Without it, spurious oscillations appear near the slow
  rarefaction inside the compound wave (Fig. 3;
  [constrained transport and other divergence treatments](/methods/constrained-transport.md)).
* **High-Mach variant:** left pressure 1000, $B_x = 0$, 200 points to
  $t = 0.012$ (a Mach 15.5 shock). The exact solution follows from the
  gas-dynamic Riemann problem with the total pressure. The strong shock
  takes about 5 points and the tangential discontinuity about 7, with no
  artificial compression (Fig. 4).
* Used with a Ryu–Jones MHD Riemann problem to test MPWENO: slow shocks
  stay crisp, and 400 zones match a TVD scheme on 800
  ([Balsara & Shu (2000)](/sources/balsara-2000.md), §§VI–VII).
* Used for GP-WENO: slow-shock oscillations are comparable to those of
  WENO-JS ([Reyes et al. (2018)](/sources/reyes-2018.md), §5;
  [GP-WENO](/methods/gp-weno.md)).

# Citations

1. [Jiang & Wu (1999)](/sources/jiang-1999.md), §§1, 3.1, 4, Figs. 2–4.
2. [Balsara & Shu (2000)](/sources/balsara-2000.md), §§VI–VII.
3. [Reyes et al. (2018)](/sources/reyes-2018.md), §5.

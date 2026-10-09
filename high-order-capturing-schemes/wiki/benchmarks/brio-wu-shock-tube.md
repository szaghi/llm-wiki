---
type: Benchmark
title: "Brio–Wu MHD shock tube"
description: "The MHD analogue of Sod's problem, (ρ, p, B_y) = (1, 1, 1 | 0.125, 0.1, −1) with B_x = 0.75 and γ = 2: fast rarefactions, a compound wave (intermediate shock attached to a slow rarefaction), a contact and a slow shock; also run rotated on a 2D grid to test divergence control."
status: established
aliases: [Brio-Wu problem, Brio–Wu Riemann problem, MHD shock tube]
tags: [benchmark, mhd, riemann-problem, 1d]
timestamp: 2026-10-09T00:00:00Z
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

**Later uses (batch 6).** With GLM cleaning, rotated by 45°, MP5 gives the
best normal field and the gain from third to fifth order is a factor
1.5–2 ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.2.1).
The 1D problem also confirms that FD-WENO with SSP-RK(10,4) stays
essentially non-oscillatory up to CFL 3.07, without results shown
([Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §3).
Rotated versions and other MHD Riemann problems are collected on
[grid-oblique MHD shock tubes](/benchmarks/oblique-mhd-shock-tubes.md).

**Later uses (batch 7).**
* *What the compound wave is.* At 8192 cells and $\gamma = 5/3$, a TVD code
  forms a "2-4" intermediate shock followed by a slow rarefaction
  (pre-shock Alfvénic Mach number 1.03, post-shock 0.910). A nonlinear
  Riemann solver that admits rotational discontinuities instead returns a
  rotational discontinuity and a slow shock, so code and exact solver
  disagree only there. An analogous fast compound problem, with
  $(\rho, p) = (1, 1 \mid 0.4, 0.4)$, $B_y = \pm1$ and $B_x = 1.3$, forms a "1-3"
  intermediate shock preceded by a fast rarefaction. The authors take no
  side on the reality of intermediate shocks ([Ryu & Jones (1995)](/sources/ryu-1995.md), §§4–5;
  [Ryu–Jones shock tubes](/benchmarks/ryu-jones-shock-tubes.md)).
* *Entropy tests.* Rotated 45° on a periodic box with an
  entropy-conservative flux, the entropy error scales as $\Delta t^3$ down to
  round-off; a modified Brio–Wu with $v_{x,L} = 1.75$ shows Roe's entropy
  glitch in the rarefaction, which an entropy-stable flux avoids
  ([Derigs et al. (2018)](/sources/derigs-2018.md), §§5.6–5.7).

# Citations

1. [Jiang & Wu (1999)](/sources/jiang-1999.md), §§1, 3.1, 4, Figs. 2–4.
2. [Balsara & Shu (2000)](/sources/balsara-2000.md), §§VI–VII.
3. [Reyes et al. (2018)](/sources/reyes-2018.md), §5.
4. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.2.1 (arXiv v2).
5. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §3 (arXiv v2).
6. [Ryu & Jones (1995)](/sources/ryu-1995.md), §§4–5.
7. [Derigs et al. (2018)](/sources/derigs-2018.md), §§5.6–5.7.

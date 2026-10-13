---
type: Benchmark
title: "Brio–Wu MHD shock tube"
description: "The MHD analogue of Sod's problem, (ρ, p, B_y) = (1, 1, 1 | 0.125, 0.1, −1) with B_x = 0.75 and γ = 2: fast rarefactions, a compound wave (intermediate shock attached to a slow rarefaction), a contact and a slow shock; also run rotated on a 2D grid to test divergence control."
status: established
aliases: [Brio-Wu problem, Brio–Wu Riemann problem, MHD shock tube]
tags: [benchmark, mhd, riemann-problem, 1d]
timestamp: 2026-10-13T00:00:00Z
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

**Later uses (batch 8).**
* *Gaussian units, $\gamma = 5/3$.* HLLEM with GLM cleaning at second
  order runs the Brio–Wu data in Gaussian units
  ($B_x = \tfrac34\sqrt{4\pi}$, $B_y = \pm\sqrt{4\pi}$) but with
  $\gamma = 5/3$ instead of 2, against an exact solution ([Dumbser & Balsara (2016)](/sources/dumbser-2016.md), §3.5).

**Later uses (batch 11).**
* *The original set-up.* [Brio & Wu (1988)](/sources/brio-1988.md), §V,
  print the same states, $B_x = 0.75$ and $\gamma = 2$, noting that the
  hydrodynamic data are those of [Sod's shock tube](/benchmarks/sod-shock-tube.md).
  Their units differ from the set-up above: 800 points with $h = 1$,
  $\Delta t = 0.2$ ("CFL ~ 0.8"), shown after 400 steps ($t = 80$), with
  the jump in the middle and no boundary conditions stated. The
  $[-1, 1]$, $t = 0.2$ form attributed above to Jiang & Wu is the exact
  rescaling of this run (800 cells of width $1/400$). The original wave
  list is the one above, with the compound wave called a "slow compound
  wave"; its $B_y$ values are 0.5849 ahead of the intermediate shock
  (numerical input to the jump relations),
  $-0.3073$ where the shock speed equals the slow characteristic speed,
  and $-0.5341$ at the tail of the attached rarefaction (these two analytic; the
  second-order upwind scheme gives $-0.5341$, with the other variables
  within 0.005), consistent with the rounded values above (§VI). That MHD
  is not genuinely nonlinear is proved there
  ([nonconvexity of ideal MHD](/results/mhd-nonconvexity.md)).
* *The original scheme comparison* (Figs. 2–6). A second-order Roe-type
  scheme with Harten's artificial compression on the linearly degenerate
  field is non-oscillatory with sharp discontinuities; with an
  arithmetic-mean instead of a Roe state its constant states agree to 4
  significant digits and its transition regions to 2. Two-step
  Lax–Wendroff with Lapidus viscosity undershoots at the rarefaction tail,
  oscillates between the waves, takes 4–5 points per shock, 5–8 for the
  slow shock and 10–15 for the contact. First-order Lax–Friedrichs has not
  yet formed the intermediate states and spreads the slow shock over
  about 20 points; on 20,000 points and 10,000 steps it converges to the
  upwind solution. FCT at CFL about 0.4 (800 steps of 0.1) undershoots at
  the rarefaction tail and the contact and oscillates over the constant
  states; at CFL 0.8 the oscillations grow "drastically". The Roe-type
  scheme costs about 10 times the Lax–Wendroff floating-point work per
  point per step, but on 200 points it is "more efficient than the
  Lax–Wendroff scheme with 800 grid points" (§VII;
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)).
* *Variant with right $B_y = -0.4$* (§V, no figure). The upwind and
  Lax–Friedrichs solutions contain "an almost stationary slow
  intermediate shock where the magnetic field changes its sign";
  Lax–Wendroff could not be made stable "with any value of artificial
  viscosity".
* *High-Mach variant, as originally run* (§V, Fig. 7). Left pressure 1000
  and $B_x = 0$, with the Mach 15.5 shock and the exact solution, are in
  the original. It prints no grid size (the Fig. 7 abscissa spans 0–200)
  and no end time, so the "200 points to $t = 0.012$" of the Results list
  above are Jiang & Wu's. With the second-order upwind scheme, Harten's
  artificial compression "does not prevent the tangential discontinuity
  from spreading", and together with the second-order correction it
  causes a density undershoot near the tangential discontinuity that
  diffuses in time. This contrasts with the result above, where
  fifth-order WENO holds the tangential discontinuity to about 7 points
  without artificial compression.
* *A regular solution of the same states.* A nonlinear Riemann solver
  that excludes intermediate shocks returns, at $\gamma = 2$ itself (in
  Gaussian units, $B_x = 0.75\sqrt{4\pi}$, $B_y = \pm\sqrt{4\pi}$), two
  fast rarefactions, two slow shocks (Mach 2.2 to the right, 1.05 to the
  left), a rotational discontinuity rotating the transverse field by about
  180° and a contact. A simulation started from the states behind the two
  fast waves still forms the compound wave, and the authors conclude that
  "this Riemann problem does not have a unique solution"
  ([Dai & Woodward (1994)](/sources/dai-1994.md), p. 368, Tables IVa–b,
  §6). This is the origin, at $\gamma = 2$, of the observation credited to
  Ryu & Jones in the batch-7 block, who make it at $\gamma = 5/3$.

# Citations

1. [Jiang & Wu (1999)](/sources/jiang-1999.md), §§1, 3.1, 4, Figs. 2–4.
2. [Balsara & Shu (2000)](/sources/balsara-2000.md), §§VI–VII.
3. [Reyes et al. (2018)](/sources/reyes-2018.md), §5.
4. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §4.2.1 (arXiv v2).
5. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §3 (arXiv v2).
6. [Ryu & Jones (1995)](/sources/ryu-1995.md), §§4–5.
7. [Derigs et al. (2018)](/sources/derigs-2018.md), §§5.6–5.7.
8. [Dumbser & Balsara (2016)](/sources/dumbser-2016.md), §3.5.
9. [Brio & Wu (1988)](/sources/brio-1988.md), §§V–VII, Figs. 2–9.
10. [Dai & Woodward (1994)](/sources/dai-1994.md), p. 368, Tables IVa–b, §6.

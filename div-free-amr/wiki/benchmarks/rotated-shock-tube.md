---
type: Benchmark
title: "Rotated shock tube"
description: "1D MHD Riemann problems rotated obliquely to the grid; the exactly constant normal field makes its deviation a direct measure of divergence errors and of non-conservative jump defects."
status: established
aliases: [oblique shock tube]
tags: [benchmark, divergence-constraint, mhd]
timestamp: 2026-10-13T00:00:00Z
---

# Rotated shock tube

A one-dimensional MHD Riemann problem whose discontinuities are rotated by
an angle (the rotation angle) against the Cartesian grid. In the exact solution the
normal field component $B_n$ is constant, so its numerical deviation
measures the error the divergence constraint should have prevented.
Comparing a cut through the 2D run with a high-resolution 1D reference
also measures the jump conditions.

## Setup

* **The unrotated Brio–Wu problem**
  ([Brio & Wu (1988)](/sources/brio-wu-1988.md) §V), the most common
  initial data. Left state: density 1, velocity 0, pressure 1, transverse
  field 1. Right state: density 0.125, velocity 0, pressure 0.1, transverse
  field $-1$. Normal field $0.75$, $\gamma = 2$; the data are Sod's
  hydrodynamic tube with a field added. The original reference uses 800
  points. The solution has fast rarefactions on both sides, a contact, a
  slow shock, and a **slow compound wave**: a slow shock with an attached
  slow rarefaction. The transverse field changes sign across that slow
  shock, so it is an intermediate shock. The paper proves that the MHD
  system is nonconvex, which is what admits the compound wave (§VI). In
  1D the normal field is a fixed parameter of the scheme, so the unrotated
  problem cannot test the divergence constraint; rotation against the grid
  is what makes it one.
  * **Sod's data, not Sod's $\gamma$.** The density and pressure data are
    those of the [Sod shock tube](/benchmarks/sod-shock-tube.md), but Sod
    uses $\gamma = 1.4$; $\gamma = 2$ is Brio & Wu's choice
    ([Sod (1978)](/sources/sod-1978.md) §3).
  * **A solution without the compound wave.**
    [Dai & Woodward (1994)](/sources/dai-woodward-1994.md) solve the
    Brio–Wu data ($\gamma = 2$, Gaussian units) with their three-component
    nonlinear Riemann solver: two fast rarefactions, two slow shocks (Mach
    2.2 and 1.05), a −180° rotational discontinuity and a contact (Table
    IV). Fed back as a Riemann problem with only shocks and
    discontinuities, a 1D simulation still produces the compound wave, and
    they conclude: "Apparently, this Riemann problem does not have a unique
    solution" (p. 368). The compound wave "will be generated through the
    conservation law … no matter what approximation we use" (§6).
  * **The compound wave at high resolution.** At 8192 cells and
    $\gamma = 5/3$, [Ryu & Jones (1995)](/sources/ryu-jones-1995.md) §5
    resolve the slow compound structure as a "2-4" intermediate shock
    followed by a slow rarefaction. Their exact Riemann solver, which
    allows rotational discontinuities, gives instead a rotational
    discontinuity plus a slow shock; the authors do not decide which is
    physical.
  * **Other variants.** Ryu & Jones (Fig. 5a) run the Brio–Wu data at
    $\gamma = 5/3$ instead of 2.
    [Zachary, Malagoli & Colella (1994)](/sources/zachary-malagoli-colella-1994.md)
    §3.1 run it unrotated in Gaussian units (transverse field
    $\pm\sqrt{4\pi}$, normal field $0.75\sqrt{4\pi}$, 800 points), and a
    strong variant with zero normal field, left pressure 1000 and
    $\gamma = 5/3$.
* **The Ryu–Jones shock tubes**
  ([Ryu & Jones (1995)](/sources/ryu-jones-1995.md) §4, Figs. 1–5). Twelve
  1D problems at 512 cells, $\gamma = 5/3$, each compared with an exact
  nonlinear Riemann solver. Five come from Dai & Woodward's tables and one
  is Brio–Wu; the other six are new (switch-on and switch-off waves,
  compound waves). States
  are listed as density, three velocity components, two transverse field
  components and a seventh entry that Ryu & Jones label total energy
  (presumably the pressure; compiler reading below):

  | Problem | Left | Right | Normal field | $t$ | Waves |
  |---|---|---|---|---|---|
  | 1a | $(1, 10, 0, 0, 5/\sqrt{4\pi}, 0, 20)$ | $(1, -10, 0, 0, 5/\sqrt{4\pi}, 0, 1)$ | $5/\sqrt{4\pi}$ | 0.08 | fast shocks, slow rarefaction, contact, slow shock |
  | 2a | $(1.08, 1.2, 0.01, 0.5, 3.6/\sqrt{4\pi}, 2/\sqrt{4\pi}, 0.95)$ | $(1, 0, 0, 0, 4/\sqrt{4\pi}, 2/\sqrt{4\pi}, 1)$ | $2/\sqrt{4\pi}$ | 0.2 | fast shocks, rotational discontinuities, slow shocks, contact |

  Problem 2a has a fully three-dimensional field and seven structures.
  *Compiler reading:* the "RJ2a" of
  [Felker & Stone (2018)](/sources/felker-2018.md) names it by this figure
  number. The full set is on the Source page. In 1D, as for Brio–Wu, the normal field
  is a fixed parameter and no divergence can be measured.
  * **Which problems are Dai & Woodward's: a qualification.** Ryu & Jones
    cite Dai & Woodward "in press". In the published paper
    ([Dai & Woodward (1994)](/sources/dai-woodward-1994.md)) four of the
    five problems they credit to it appear, after conversion from Gaussian
    units: 1a is Table VI (same states, $t = 0.08$; Dai & Woodward also run
    it on 200 zones), 1b is Table IIIa, 2a is Table Ia, 3a is Table IIa.
    2b, credited to "DW table 5a", does not match Table Va, which has
    normal field 5 against 3. The table numbering also differs (RJ's
    "table 7" is Table VI), so Ryu & Jones quoted another version.
  * *Compiler reading:* in all four matches the seventh entry of the state
    equals Dai & Woodward's pressure, not a total energy (1a: 20 and 1;
    a total energy of 20 is below the kinetic energy 50 of the left state).
    The entry is presumably the pressure; Ryu & Jones label it total
    energy, and the [Ryu & Jones](/sources/ryu-jones-1995.md) Source page
    records their label.
* **Narrow strip** ([Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md),
  credited to Tóth): a domain $[0,1]\times[0, 2/N]$ on an $N\times2$ grid
  with shifted periodic boundaries, rotation angle $\tan^{-1}2 \approx 63.4°$. It
  is compared with a 1024-cell 1D run.
* **Choose the angle with care.** If the initial field is uniform, or the
  fronts run along cell sides or diagonals (for example a 45° rotation), every
  discrete divergence stays exactly zero and the test cannot discriminate
  between schemes. At a generic angle the fronts are discretized with unequal
  $x$ and $y$ jumps, so $B_n$ is constant only approximately, even for a
  scheme that holds its divergence exactly
  ([Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md) §4.2).
  * **Qualification: what "stays zero" requires.** At 45° the solution
    depends only on the coordinate along the diagonal, and every divergence
    stencil reduces to a difference of $B_n$ along it. Zero initially, the
    divergences stay exactly zero only for schemes that hold $B_n$ fixed
    (CT). Schemes that diffuse the normal field show $B_n$ errors at 45°
    ([Powell (1994)](/sources/powell-1994.md) §3;
    [Jiang & Wu (1999)](/sources/jiang-1999.md) §3.1). The angle therefore
    separates the held-class schemes from the rest, but not held-class
    schemes from each other.
* **The 45° diagonal tubes of the Ryu codes.**
  [Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md) §3.1 run
  Ryu–Jones 1a and 2a along the diagonal of $[0,1]^2$ on $256^2$, at
  $t = 0.08\sqrt2$ and $0.2\sqrt2$, against the exact solver; results are
  "virtually the same as with the one-dimensional code".
  [Ryu et al. (1998)](/sources/ryu-1998.md) §3.1 repeat both with their CT
  code. Neither paper reports a divergence or normal-field diagnostic; the
  1998 plot of the parallel field stays flat at about 0.564, which is the
  2a normal field $2/\sqrt{4\pi} \approx 0.5642$.
  *Compiler reading:* both papers use exactly the angle the caveat above
  calls least discriminating; neither discusses it.
* **The 45° Brio–Wu tube of the eight-wave report.**
  [Powell (1994)](/sources/powell-1994.md) §3 (Figs. 2–8) runs the Brio–Wu
  data rotated by 45° with a first-order Roe-type eight-wave scheme, on 600
  and 1200 cells. Rotated and unrotated results are "nearly
  indistinguishable for all but the normal component of velocity"; the
  normal-field errors, "on the order of a few percent … on the coarse
  grid", "are reduced as the grid is refined" (Fig. 8). No divergence norm
  is reported.
* **The 45° Brio–Wu tube with and without projection.**
  [Jiang & Wu (1999)](/sources/jiang-1999.md) §3.1 run the Brio–Wu problem
  rotated by 45° on $600^2$ with fifth-order WENO and Powell's $8\times8$
  eigensystem. Without the Poisson correction the run shows spurious
  oscillations near the slow rarefaction inside the compound wave; with it
  the run agrees with their 1D result on 800 points
  ([projection method](/methods/projection-method.md)).

* **Read through macro-cells.** At a generic angle the discrete solution
  varies on the grid scale along the fronts, so even an exact-CT scheme
  shows a roughly 10% oscillation of the cell-centered $B_n$ at fast shocks.
  Averaged conservatively onto macro-cells, which are the grid's symmetry
  period ($2\times1$ cells for $\tan^{-1}2$), $B_n$ is constant to
  round-off. Schemes that create a true *jump* in $B_n$ cannot pass this
  test. Removing the cell-level oscillation would need a viscosity stencil
  at least macro-cell-wide
  ([Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md) §5.3).

## What it has shown

* **Non-conservative source terms give wrong jumps.** The
  [eight-wave](/methods/eight-wave.md) scheme produces incorrect jump
  conditions across strong shocks, and they do not converge away with
  resolution ([Tóth (2000)](/sources/toth-2000.md)).
* **Monopoles from collocated fluxes.** Between upwind CT and its collocated
  base scheme with the same solver, the $B_n$ error drops 2.7–21×. The
  central divergence of the interpolated cell-centered field remains
  $O(10$–$100)$ at fronts in both schemes, while the staggered invariant
  stays at round-off
  ([UCT](/methods/upwind-constrained-transport.md);
  [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md)).
* **A cleaning scheme for scale** ([Zaghi (2026)](/sources/zaghi-2026.md),
  hypothesis). Fifth-order WENO with GLM gives
  a $B_n$ error of $2.79\cdot10^{-3}$ at 63.4° and $4.17\cdot10^{-3}$ at
  45° (256 cells), first order. The record quotes $3.7\cdot10^{-3}$ at 63.4°
  for Tóth's second-order base scheme. At discontinuities the scheme order
  barely matters for this measure.
* **High-order cleaning at 45° and in 3D**
  ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md)).
  * 2D Brio–Wu on a $600\times6$ strip. The authors choose a rotation
    angle of 45° because it minimizes the $B_n$ error, which is the configuration the
    angle caveat above calls least discriminating.
  * 3D Ryu–Jones on $768\times8\times8$, rotated by two angles whose
    tangents are $-1/2$ and $1/4$, so that planar symmetry is an integer cell shift.
  * Third- and fifth-order schemes reach an L1 error of $B_n$ of about
    2–$9\cdot10^{-5}$, with a peak $B_n$ oscillation of about 0.7% for
    MP5. Going from third to fifth order gains only a factor 1.5–2 at
    discontinuities.
  * Their divergence monitor is built from reconstructed interface values
    ([GLM](/methods/glm-divergence-cleaning.md)), so its
    $\approx 10^{-2}$ level is not comparable with the monitors above.

* **Base scheme against collocated CT**
  ([Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md)). At
  a rotation angle of $\tan^{-1}0.5$ on $180\times150$, fifth-order FD-WENO without
  CT shows spurious oscillations in density, the transverse field and $B_n$.
  The authors attribute them to divergence errors. With potential-based
  CT the cuts agree with a 5000-cell 1D reference. No divergence norm is
  reported.
* **An early 45° run of a conservative CT scheme**
  ([Dai & Woodward (1998, JCP)](/sources/dai-woodward-1998.md) Figs. 11–13;
  [Dai & Woodward (1998, ApJ)](/sources/dai-woodward-1998-b.md) Figs. 3–5).
  $256^2$, normal field 5, $t = 0.06$; 45° chosen "only because it is easy
  to set initial conditions which exactly satisfy the divergence-free
  condition". The jump conditions are satisfied, and the authors state
  "there would be O(1) truncation errors in the jump conditions if the
  scheme were not conservative for any one of eight conserved quantities".
  $B_n$ is flat at plot scale for fast shocks and dips to about 4.99997 in
  the case with slow shocks (axis reading); "the variation … is a symptom
  of truncation errors".
  *Compiler reading:* the plotted $B_n$ is presumably the split-updated
  cell field, which the scheme does not hold; a held face invariant forces
  a constant face $B_n$ at 45°, so the dip does not bear on the angle
  caveat.

# Citations

1. [Tóth (2000)](/sources/toth-2000.md): the rotated shock-tube test and the eight-wave failure.
2. [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md), §4.2, Tables 2–3, Figs. 4–7.
3. [Zaghi (2026)](/sources/zaghi-2026.md): FLUME `verification.md` (MV-8).
4. [Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md), §5.3, Fig. 10.
5. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md), §§4.2.1–4.2.2, Table 2, Fig. A.7.
6. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §7.2, Figs. 2–4.
7. [Brio & Wu (1988)](/sources/brio-wu-1988.md), §§IV, V, VI, Figs. 2, 9.
8. [Ryu & Jones (1995)](/sources/ryu-jones-1995.md), §§4–5, Figs. 1–6 (captions).
9. [Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md), §3.1, Figs. 1–2 (captions).
10. [Ryu, Miniati, Jones & Frank (1998)](/sources/ryu-1998.md), §3.1, Figs. 2a–b.
11. [Zachary, Malagoli & Colella (1994)](/sources/zachary-malagoli-colella-1994.md), §3.1, Figs. 3–4.
12. [Felker & Stone (2018)](/sources/felker-2018.md), §5.
13. [Dai & Woodward (1998, JCP)](/sources/dai-woodward-1998.md), §4.1, Figs. 11–13.
14. [Dai & Woodward (1998, ApJ)](/sources/dai-woodward-1998-b.md), §3, Figs. 3–5.
15. [Powell (1994)](/sources/powell-1994.md), §3, Figs. 2–8.
16. [Jiang & Wu (1999)](/sources/jiang-1999.md), §3.1, Fig. 3.
17. [Dai & Woodward (1994)](/sources/dai-woodward-1994.md), §5, Tables I–VI, Fig. 8.
18. [Sod (1978)](/sources/sod-1978.md), §3.

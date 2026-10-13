---
type: Benchmark
title: "Double Mach reflection"
description: "A Mach 10 shock hitting a 30° wedge (posed as a 60° shock on a flat wall): two Mach stems, a wall jet and slip-line roll-up; the standard 2D robustness and resolution test."
status: established
aliases: [double Mach reflection, DMR]
tags: [benchmark, euler, 2d, strong-shocks, mach-reflection]
timestamp: 2026-10-13T00:00:00Z
---

# Double Mach reflection

**Set-up** (Woodward & Colella). Domain $[0, 4]\times[0, 1]$; a
right-moving Mach 10 shock at $x = 1/6$ on the bottom, inclined at 60° to
the $x$-axis; reflecting wall for $x > 1/6$, exact post-shock data to the
left of it; the top boundary follows the exact shock motion; undisturbed
gas $\rho = 1.4$, $p = 1$; $t = 0.2$; usually only $[0, 3]\times[0,1]$
shown ([Jiang & Shu (1996)](/sources/jiang-1996.md), §8.3 Example 3;
[Suresh & Huynh (1997)](/sources/suresh-1997.md);
[Balsara & Shu (2000)](/sources/balsara-2000.md), §VII.b).

**Results.**
* WENO-LF-4, WENO-LF-5 and ENO-LF-4 on $240\times 59$ and
  $480\times 119$ resolve both Mach stems; WENO with pressure–entropy
  weights fails because of the strong reflected waves
  ([Jiang & Shu (1996)](/sources/jiang-1996.md);
  [characteristic decomposition](/methods/characteristic-decomposition.md)).
* MP5 and WENO5 on $240\times 60$ capture both stems and the wall jet;
  CPU 5553 s versus 6843 s, against 4122 s for constant reconstruction
  ([Suresh & Huynh (1997)](/sources/suresh-1997.md), Fig. 4.7).
* $r = 5$ MPWENO with LLF fluxes and artificial compression on
  $480\times 120$ captures the slip-line roll-up seen in much finer runs.
  With RF fluxes a mild carbuncle appears where the normal shock meets
  the wall; using LLF near shocks removes it without loss of order
  ([Balsara & Shu (2000)](/sources/balsara-2000.md)).

**Later uses (batch 2).** WENO-Z of orders 5, 9, 11 at up to
$1600 \times 400$ (higher order compensates resolution; $q \le 2$
unstable for WENO-M at $r > 3$ and WENO-Z at $r > 4$)
([Castro et al. (2011)](/sources/castro-2011.md)); WENO-CU6 at
$480 \times 120$ resolves vortical structure comparable to WENO5 at
twice the resolution ([Hu, Wang & Adams (2010)](/sources/hu-2010.md));
TENO6 at an effective $1024 \times 256$ comparable to ninth-order WENO-JS
at $1/960$, WENO-CU6-M fails ([Fu, Hu & Adams (2016)](/sources/fu-2016.md));
WENO-ZQ at $1600 \times 400$ ([Zhu & Qiu (2016)](/sources/zhu-2016.md));
WENO-AO(7,5,3) at $1600 \times 400$ resolves the Kelvin–Helmholtz
roll-up of the Mach-stem slip line ([Balsara, Garain & Shu (2016)](/sources/balsara-2016.md)).

**Later uses (batch 3).** FV-WENO ($r = 3$) with HLLC or MUSTA at
$480\times120$, $960\times240$ and $1920\times480$ gives the accepted
pattern on all meshes. HLLC rolls up the slip surfaces more than MUSTA,
a sign of less numerical diffusion. Since slip surfaces are physically
unstable, Euler computations have no converged limit, and their
roll-up measures only the scheme's effective viscosity
([Titarev & Toro (2004)](/sources/titarev-2004.md), §5.3). WENO-CU6-M1
with the cut-off positivity limiter at $240\times60$ predicts a strong
near-wall jet, as WENO-CU6-M2 does, where earlier computations at this
resolution smear it ([Hu, Adams & Shu (2013)](/sources/hu-2013.md), §3.4).
AFD-WENO at $1920\times480$, with a flattening algorithm, captures the
instabilities around the Mach stem
([Balsara et al. (2025)](/sources/balsara-2025.md), §VIII.a).

**Later uses (batch 4).**
* RKDG with WENO limiters, $K = 1$–$3$, up to $1920\times480$. Only
  2–25% of cells are troubled, and results are comparable to TVB at
  $M = 50$ ([Qiu & Shu (2005)](/sources/qiu-2005.md), Example 3.9, Table 4).
* Fourth-order ADER-WENO with HLL on $960\times240$ and $1920\times480$
  resolves the Mach-stem roll-up. Following Cockburn and Shu, the
  authors state that second order would need four times more zones per
  direction ([Balsara et al. (2009)](/sources/balsara-2009.md), §6.4).
* Third-order ADER-WENO on AMR ($150\times50$ base, $r_{\mathrm{AMR}} = 4$,
  two levels, equivalent $2400\times800$) agrees qualitatively with
  published roll-up ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4).
* ADER-DG with subcell limiting on $350\times100$, $K = 1, 2, 5, 9$.
  Higher $K$ flags fewer cells in the vortex region and keeps more
  small-scale structure ([Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.4). With AMR ($75\times25$ base,
  $K = 2, 5, 8$) the vortex roll-up grows richer from $K = 2$ to 5 ([Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.3).
* *A geometric variant:* a vertical Mach 10 shock hitting an equilateral
  triangle embedded in a Cartesian grid (upper half by symmetry,
  $t = 0.2$). The ramp boundary is imposed by weighted extrapolation of
  ghost cells. High-order extrapolation resolves the reflection pattern
  better than first order, with WLS-GAW best
  ([Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §5.2.3;
  [weighted extrapolation](/methods/weighted-extrapolation.md)).

**Later uses (batch 5).**
* *On the real wedge.* The 30° wedge cut through a Cartesian grid, with a
  vertical Mach 10 shock starting at the wedge foot and the wall imposed
  by fifth-order SILW plus WENO extrapolation; $h = 1/320$, $t = 0.2$.
  Exactly conservative boundary fluxes and plain SILW look the same
  ([Ding, Shu & Zhang (2020)](/sources/ding-2020.md), Example 9). The
  flux-based ILW runs the same configuration at $h = \sqrt3/480$ and
  $\sqrt3/960$ ([Lu et al. (2021)](/sources/lu-2021.md), Example 3.10;
  [inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md)).
* *On adaptive grids.* Fourth-order finite volume on two levels with
  refinement ratio 4 (effective $1024\times256$) is called "comparable to
  that of the best state-of-the-art shock-capturing methods". No set-up
  or error measure is given ([McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §4.4;
  [fourth-order finite volume](/methods/fourth-order-finite-volume.md)).
  Fifth-order FD with MP5 on a three-level dynamic grid (base
  $240\times60$, effective $960\times240$, CFL 0.8) resolves the
  Kelvin–Helmholtz roll-up. It costs about 3 times the second-order
  scheme, on one processor and on 32 with AMR
  ([Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md), §5.7, Table 6;
  [high-order AMR](/methods/high-order-amr.md)).
  Fifth-order FD-WENO on three levels (base $720\times240$, ratio 2)
  fails at once with negative density when inter-level transfer uses
  pure WENO or Lagrange interpolation. A hybrid that switches to
  conservative second-order interpolation at shocks runs to the end
  ([Wang et al. (2025)](/sources/wang-2025.md), §6.4.2, preprint).

**Later uses (batch 7).**
* *Euler vs Navier–Stokes DG with only the positivity limiter.* Euler DG
  shows more structure than TVB-limited DG but becomes more oscillatory on
  finer meshes and at higher degree; at $\mathrm{Re} = 100$ and 500 the
  viscous runs become less oscillatory under refinement, a version of the
  problem in which convergence is meaningful ([Zhang (2017)](/sources/zhang-2017.md), Example 8).
* Fourth-order ADER-WENO on $1920\times480$ resolves the Mach-stem roll-up
  ([Balsara (2017)](/sources/balsara-2017-d.md), §IX.2).

**Later uses (batch 8).**
* *Kinked Mach stem at first order.* On $480\times120$ with CFL 0.8,
  first-order HLLC and HLLEM kink the Mach stem and form a spurious triple
  point. Selective wave modification and anti-diffusion control remove
  it. Both papers print the end time as $t = 0.02$, not 0.2, recorded as
  printed ([Simon & Mandal (2019)](/sources/simon-2019.md), §9.5; [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §7.2).
* On $960\times240$ to $t = 0.2$, first order in space with third-order
  TVD Runge–Kutta, Godunov, Roe, HLLEM and HLLC all kink the stem. With
  the entropy-control term the kinks are "barely noticeable"
  ([Xie et al. (2021)](/sources/xie-2021.md), §6.3; [numerical shock instability](/definitions/numerical-shock-instability.md)).

**Later uses (batch 10).** *On an embedded wedge.* The wall is a 30°
ramp cutting the Cartesian grid through $(1/6, 0)$ in $[0, 3]\times[0, 1.75]$,
so the shock is aligned with the grid and the wall is not. Second-order
MUSCL with [state redistribution](/methods/state-redistribution.md),
CFL 0.85, $h = 1/240$ and $1/480$, run to $t = 0.2$, with smallest volume
fractions $1.65\times10^{-6}$ and $2.95\times10^{-7}$. The results are
comparable to grid-aligned runs at the same resolution; the wall shocks
agree across three resolutions and the unstable contact shifts slightly
([Berger & Giuliani (2021)](/sources/berger-2021.md), §5.3, Figs. 12–13).

**Later uses (batch 11).** *The original paper.*
[Woodward & Colella (1984)](/sources/woodward-1984.md) (§IVc, p. 136)
print the set-up line above, with these precisions. The shock "initially
makes a 60° angle with a reflecting wall"; the paper tilts the shock
rather than the wall to avoid oblique boundaries, and **prints no wedge
angle**. The "30° wedge" of this page's description is the equivalent
geometry ($90° - 60°$), a later reading, not a printed value. The shock
foot at $x = 1/6$ follows from the condition that keeps the reflected
shock attached, rather than being stated. The post-shock state is not
printed; the right boundary at $x = 4$ has zero gradients. The paper does
not discuss slip-line roll-up, which this page's description takes from
later sources.
* *Grids and scheme comparison* (Fig. 9, $h = 1/30$, $1/60$, $1/120$, so
  up to $480\times120$; the PPMDE run of Fig. 4 is labelled Courant 0.8). Godunov does not resolve the wall
  jet even on the finest grid. MacCormack is "far superior" to Godunov
  here but oscillates where shocks are slow and grid-aligned. BBC is
  MacCormack without the oscillations. ETBFCT gives staircase contours, a
  misshapen main Mach stem and a jet without the mushroom tip. MUSCL
  resolves the jet on the middle grid, but its thin shocks are unstable
  where slow and grid-aligned. PPMDE with Lapidus viscosity 0.1 removes
  that instability and is "more efficient by factors of more than 4.9
  and 1.3" than BBC and MacCormack; PPMLR by more than 4.4 and 1.2 ([PPM](/methods/ppm.md)).
* *Starting error.* Initializing and imposing the shock as a one-zone
  jump creates an overheated strip about 2 zones wide, visible only in
  the vertical velocity, from the upper right corner to the wall near
  $x = 2$; it "mars all the computed results".
* *Flow features.* A dense jet shoots right along the wall ("shaped
  charge"). Under the reflected shock near the wall there is little
  vertical motion, so schemes whose dissipation vanishes at zero velocity
  oscillate there; single-step Eulerian MUSCL is noisy along the nearly
  steady reflected shock while MUSCL as Lagrange plus remap is not
  (Fig. 10).

**Later uses (batch 11, Riemann-solver papers; merged at the 2026-10-13
deep lint).**
* *A carbuncle test at second order.* Mach 10 shock at 60° to the
  $x$-axis (the text also says "reflected by 30° ramp") on
  $[0, 3.2]\times[0, 1]$ to $t = 0.2$, zero-gradient right boundary; the
  grid and the other boundaries are not printed. With MUSCL, HLLC kinks
  the Mach stem, "which gives rise to a spurious triple point and polluted
  region after shock"; HLL and HLL-BVD show no kink, and HLL-BVD rolls up
  the slip line with less diffusion than HLL
  ([Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §III H, Fig. 14;
  [numerical shock instability](/definitions/numerical-shock-instability.md)).
* *Fourth-order ADER–WENO with a multidimensional HLLI solver.* The
  standard set-up on $[0, 4]\times[0, 1]$ with $1920\times480$ cells to
  $t = 0.2$: a "very well-resolved roll-up of the Mach stem", judged
  visually ([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §5.2;
  [multidimensional Riemann solvers](/methods/multidimensional-riemann-solvers.md)).

**Later uses (batch 12).** *Single Mach reflection on wedges, a weak-shock
relative* ([Toro (1997)](/sources/toro-1997.md), §17.2,
Figs. 17.9–17.12). Not the Mach 10 set-up above.
* *Reflection types.* Toro lists four: regular, single Mach, complex Mach
  and double Mach reflection, citing Ben-Dor and Glaz et al.
  ([regular and Mach reflection](/definitions/mach-reflection.md)).
* *Set-up.* Domain $25.0\times16.5$, wedge apex at $x = 4.69$, initial
  shock at $x = 4.0$, air at rest ($\rho = 1.225$ kg/m³,
  $p = 1.01325\times10^5$ Pa), post-shock state from the
  Rankine–Hugoniot relations. To avoid start-up errors the shock runs
  90 % of the way to the apex and the state behind it is then reset. WAF
  with dimensional splitting, [HLLC](/methods/hllc-riemann-solver.md),
  the VANLEER limiter, Courant number 0.9.
* *Runs.* $M_s = 1.7$ on a 25° wedge, on a curvilinear $800\times528$
  mesh and with a CHIMERA–AMR–Cartesian method (base $50\times33$, two
  levels, factor 4): a single Mach reflection, in "excellent"
  qualitative agreement with a photograph by K. Takayama. $M_s = 1.2$ on
  a 30° wedge, curvilinear $420\times240$: a single Mach reflection,
  "satisfactory". The comparison is with photographs only; no
  triple-point angles or positions are printed.
* *HLL against HLLC.* On the $M_s = 1.2$ case Colella's piecewise-linear
  method with HLLC is close to WAF–HLLC, while with HLL it smears the
  slip surface "very significantly" (PLM runs by T. Saito), the 2D face
  of HLL's contact defect ([HLLEM](/methods/hllem-riemann-solver.md)).
* The $M_s = 1.7$, 25° configuration is the gas-only case of
  [Yeom & Chang (2010)](/sources/yeom-2010.md), who compare with an
  interferogram reproduced from the book's 2nd edition (§4.1).

**Later uses (batch 15).** *An early AMR run of the same case*
([Berger & Colella (1989)](/sources/berger-1989.md), §7, Fig. 7.1).
$M_s = 10$, $\gamma = 1.4$, the shock's direction of propagation at 30°
to the reflecting surface. Domain $2.0\times0.4$, coarse $h = 0.02$, three
levels with $r_{\mathrm{AMR}} = 4$ (finest $h = 0.00125$, uniform
equivalent $1600\times320$), 4 times finer per direction than Woodward
and Colella's finest grid; the frame, boundary conditions and initial
shock position are not printed, so this is not stated to be the
$[0, 4]\times[0, 1]$ set-up above. The paper reports a Kelvin–Helmholtz
roll-up of the principal slip line, not self-similar, formed where the
weak shock from the second triple point meets the slip line and carried
into the roll-up at the tip of the wall jet. Run time 5674 s on a Cray
X-MP/22, estimated at one eighth of a uniform fine grid's
([high-order AMR](/methods/high-order-amr.md)). The text gives
$t = 1.20$ and the caption $t = 0.12$.

# Citations

1. [Jiang & Shu (1996)](/sources/jiang-1996.md), §8.3 Example 3.
2. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §4.3 Example 2.
3. [Balsara & Shu (2000)](/sources/balsara-2000.md), §VII.b.
4. [Castro, Costa & Don (2011)](/sources/castro-2011.md), §5.5.
5. [Hu, Wang & Adams (2010)](/sources/hu-2010.md), §3.7.
6. [Fu, Hu & Adams (2016)](/sources/fu-2016.md), §5.5.
7. [Zhu & Qiu (2016)](/sources/zhu-2016.md), Example 3.8.
8. [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §5.5.
9. [Titarev & Toro (2004)](/sources/titarev-2004.md), §5.3.
10. [Hu, Adams & Shu (2013)](/sources/hu-2013.md), §3.4.
11. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §VIII.a.
12. [Qiu & Shu (2005)](/sources/qiu-2005.md), Example 3.9.
13. [Balsara et al. (2009)](/sources/balsara-2009.md), §6.4.
14. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4.
15. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.4.
16. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.3.
17. [Baeza, Mulet & Zorío (2016)](/sources/baeza-2016.md), §5.2.3.
18. [Ding, Shu & Zhang (2020)](/sources/ding-2020.md), Example 9.
19. [Lu et al. (2021)](/sources/lu-2021.md), Example 3.10.
20. [McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §4.4.
21. [Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md), §5.7 (accepted manuscript).
22. [Wang et al. (2025)](/sources/wang-2025.md), §6.4.2 (arXiv preprint).
23. [Zhang (2017)](/sources/zhang-2017.md), Example 8.
24. [Balsara (2017)](/sources/balsara-2017-d.md), §IX.2.
25. [Simon & Mandal (2019)](/sources/simon-2019.md), §9.5.
26. [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §7.2.
27. [Xie et al. (2021)](/sources/xie-2021.md), §6.3.
28. [Berger & Giuliani (2021)](/sources/berger-2021.md), §5.3 (arXiv v1).
29. [Woodward & Colella (1984)](/sources/woodward-1984.md), §§IVc, VIc, Figs. 4, 9, 10.
30. [Toro (1997)](/sources/toro-1997.md), §17.2.
31. [Yeom & Chang (2010)](/sources/yeom-2010.md), §4.1.
32. [Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §III H, Fig. 14.
33. [Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §5.2.
34. [Berger & Colella (1989)](/sources/berger-1989.md), §7, Fig. 7.1, Tables I–II.

---
type: Benchmark
title: "Sod shock tube"
description: "The 1D Riemann problem (1, 0, 1 | 0.125, 0, 0.1): rarefaction, contact and shock with a monotone density profile; the baseline check of shock, contact and rarefaction resolution."
status: established
aliases: [Sod problem, Sod's problem]
tags: [benchmark, euler, riemann-problem, 1d]
timestamp: 2026-10-13T00:00:00Z
---

# Sod shock tube

**Set-up** (Sod 1978): $(\rho, v, p)_L = (1, 0, 1)$,
$(\rho, v, p)_R = (0.125, 0, 0.1)$, $\gamma = 1.4$
([Liu, Osher & Chan (1994)](/sources/liu-1994.md);
[Jiang & Shu (1996)](/sources/jiang-1996.md)). The density profile is
monotone, so intermediate states need not be "built up" — which makes it
an easier test than [Lax's](/benchmarks/lax-shock-tube.md)
([Harten et al. (1987)](/sources/harten-1987.md)).

**Uses.**
* Second- and fourth-order ENO with characteristic reconstruction;
  component-wise fourth-order ENO shows some noise, at a practically
  acceptable level ([Harten et al. (1987)](/sources/harten-1987.md),
  Figs. 9–11).
* With the self-similar Riemann solution, convergence of any scheme is
  limited to first order; comparisons should count time steps to resolved
  intermediate states ([Harten et al. (1987)](/sources/harten-1987.md)).
* Contact sharpening by subcell resolution and artificial compression
  ([Shu & Osher (1989)](/sources/shu-1989.md), Example 6).
* WENO $r = 3$ with Roe flux and characteristic reconstruction
  ([Liu, Osher & Chan (1994)](/sources/liu-1994.md), Example 4);
  WENO5 better than WENO5-PS, better than WENO3; artificial compression
  sharpens the contact most ([Jiang & Shu (1996)](/sources/jiang-1996.md)).
* MP5 resolves contact and shock sharply
  ([Suresh & Huynh (1997)](/sources/suresh-1997.md), Example 1).
* Central WENO: component-wise indicators give irregular weights at the
  contact; global indicators are better
  ([Levy, Puppo & Russo (1999)](/sources/levy-1999.md), Test 5).
* Run with MPWENO with good results, not shown
  ([Balsara & Shu (2000)](/sources/balsara-2000.md)).

**Later uses (batch 2).** Grid convergence: WENO5 and WENO5M both
converge at about 5/6 order in $L_1$ for density, WENO5M with about 10 %
smaller errors, to $h = 1/102400$ ([Henrick et al. (2005)](/sources/henrick-2005.md),
Table 9) — the convergence rate of captured contacts.
[Borges et al. (2008)](/sources/borges-2008.md);
[Martín et al. (2006)](/sources/martin-2006.md) (a pressure-ratio-2 tube:
at $r = 4$, WENO-JS $q = 1$ and SYMOO show dispersive density errors);
[Hu, Wang & Adams (2010)](/sources/hu-2010.md); [Fu, Hu & Adams (2016)](/sources/fu-2016.md);
[Rathan & Naga Raju (2017)](/sources/rathan-2017.md) (a modified Sod).

**Later uses (batch 3).** Compact-reconstruction WENO on 100 points
smears the discontinuities less than WENO-JS and WENO-Z
([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 3). GP-WENO
($\ell/h = 12$, 128 cells): GP-R2 is comparable to WENO-JS on the same
5-cell stencil, and GP-R3 is clean. GP-R1 smears most yet oscillates
most at the shock, because its smoothness indicators approximate the
RKHS norm worst ([Reyes et al. (2018)](/sources/reyes-2018.md), §5.4).
Fifth-order AFD-WENO matches the exact solution
([Balsara et al. (2025)](/sources/balsara-2025.md), §VII.a).

**Later uses (batch 4).** ADER-DG with $K = 9$ and subcell limiting on
only $20\times5$ cells to $t = 0.2$ resolves the shock within one cell
at the exact location. The contact is an S-shaped profile inside a
single unlimited cell ([Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.1). With AMR the contact cell is at
the finest level and stays unlimited. With $K = 2$ and about 15% of
cells limited, the limiter overhead is about 1.5 in CPU time
([Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.2).

**Later uses (batch 5).** A dimensional, thermally perfect air version
with Sod's ratios ($\rho_L/\rho_R = 8$, $p_L/p_R = 10$, $\rho_R = 0.125$ kg/m³,
$p_R = 10^4$ Pa) runs on two AMR levels with fourth-order finite volume:
"good agreement" with the exact solution and "no severe oscillations"
([Owen, Guzik & Gao (2018)](/sources/owen-2018.md), §4.1). With two
levels (finest $h = 1/256$, $t = 0.2$), WENO and hybrid inter-level
interpolation are indistinguishable when regridding every 2 steps. At
every 5 steps WENO interpolation oscillates at the shock and contact and
overshoots the shock speed ([Wang et al. (2025)](/sources/wang-2025.md), §6.3.1, preprint).

**Later uses (batch 7).**
* *Toro's modified Sod* ($v_{x,L} = 0.75$, a sonic rarefaction): Roe's solver
  shows an entropy-violating glitch that shrinks with resolution but never
  vanishes; an entropy-stable flux does not ([Derigs et al. (2018)](/sources/derigs-2018.md), §5.7).

**Later uses (batch 8).**
* *Toro's modified Sod with HLLEM* at second order: no sonic glitch, in
  contrast to Roe ([Dumbser & Balsara (2016)](/sources/dumbser-2016.md), §3.6.1).

**Later uses (batch 9).** Entropy-conservative or entropy-stable SBP DG
of degree 3 on 128 elements, with RK4 and no shock capturing, shows small
overshoots at the discontinuities. Relaxation neither removes nor
smears them, and $\vert\gamma^n_{\mathrm R} - 1\vert < 5\times10^{-4}$
([Ranocha et al. (2020)](/sources/ranocha-2020.md), §4.3, Figs. 8–9a; [relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md)).

**Later uses (batch 10).** *In a rotated channel with AMR.* The Sod states
in a 2D channel slanted at 30° to the grid, so both walls are cut cells,
with one adaptive level whose coarse–fine boundaries cross the walls and
move. With weighted state redistribution and re-redistribution the
profiles approach the exact solution as $h$ halves twice, and mass is
conserved; no error norms are given ([Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §4.2, Fig. 4;
[state redistribution](/methods/state-redistribution.md)).

**Later uses (batch 11).** *The original paper.* [Sod (1978)](/sources/sod-1978.md)
(§3, p. 14) prints the states and $\gamma$ of the set-up above, gas at
rest on both sides of a diaphragm, $h = 0.01$ (100 points) and $\nu = 0.9$
for every scheme. It prints **no diaphragm position, no end time and no
boundary conditions**: the run stops before any wave reaches either
end, and the figures span $x \in [0, 1]$. The usual diaphragm at
$x = 0.5$ and end time $t = 0.2$ (the latter in some uses above) are
therefore later conventions, not Sod's. *Compiler reading:* with the diaphragm at $x = 0.5$ (which the
Glimm mass in Table III fits), the plotted shock and contact positions
correspond to $t \approx 0.14$; this is inferred from the figures, not
printed.
* Sod runs nine schemes plus artificial-compression variants and reports
  contact and shock widths in zones: Godunov 7–8 and 5–6, two-step
  Lax–Wendroff 6–8 and 4–6, MacCormack 7–8 and 5–6, Rusanov 14–16 and
  6–8, Boris–Book antidiffusion 5–7 and 1–2, the Harten–Zwas hybrid 8–9
  and 5–6, Hyman's predictor–corrector 6–8 and 3–4. Artificial
  compression brings Godunov to 3–4 and 1–2 and Rusanov to 2–3 and 1–2
  ([contact sharpening](/methods/contact-sharpening.md)). Glimm's random
  choice gives zero-width discontinuities at random but on-average exact
  positions. An upwind scheme with centred pressure differences forms a
  nonphysical shock at the left end of the rarefaction.
* Without corrective procedures Godunov and Hyman are best. Sod calls the
  problem a "sitting duck" for Riemann-solver-based methods and places a
  method's "true value" in multidimensional problems (p. 25), a caveat
  akin to the self-similarity remark of Harten et al. above.
* Sod's "energy" plots are the specific internal energy (2.5 on the left,
  2.0 on the right), not the energy density $E$.

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), §7.
2. [Shu & Osher (1989)](/sources/shu-1989.md), Example 6.
3. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), Example 4.
4. [Jiang & Shu (1996)](/sources/jiang-1996.md), §8.2 Example 1.
5. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §4.2.
6. [Levy, Puppo & Russo (1999)](/sources/levy-1999.md), Test 5.
7. [Balsara & Shu (2000)](/sources/balsara-2000.md), §VI.b.
8. [Henrick, Aslam & Powers (2005)](/sources/henrick-2005.md), §5.7.
9. [Borges et al. (2008)](/sources/borges-2008.md), §5.2.1.
10. [Martín et al. (2006)](/sources/martin-2006.md), §5.2.
11. [Hu, Wang & Adams (2010)](/sources/hu-2010.md), §3.2.
12. [Fu, Hu & Adams (2016)](/sources/fu-2016.md), §5.2.
13. [Rathan & Naga Raju (2017)](/sources/rathan-2017.md), Example 5.
14. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Example 3.
15. [Reyes et al. (2018)](/sources/reyes-2018.md), §5.4.
16. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §VII.a.
17. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.1.
18. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.2.
19. [Owen, Guzik & Gao (2018)](/sources/owen-2018.md), §4.1 (accepted manuscript).
20. [Wang et al. (2025)](/sources/wang-2025.md), §6.3.1 (arXiv preprint).
21. [Derigs et al. (2018)](/sources/derigs-2018.md), §5.7.
22. [Dumbser & Balsara (2016)](/sources/dumbser-2016.md), §3.6.1.
23. [Ranocha et al. (2020)](/sources/ranocha-2020.md), §4.3 (arXiv v4).
24. [Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §4.2 (arXiv v1).
25. [Sod (1978)](/sources/sod-1978.md), §§3–4, Figs. 2–15, Tables II–IV.

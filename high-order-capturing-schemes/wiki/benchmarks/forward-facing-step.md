---
type: Benchmark
title: "Mach 3 wind tunnel with a forward-facing step"
description: "Mach 3 inflow over a step (0.2 high at x = 0.6 in a [0,3]×[0,1] tunnel; Emery 1968, in the standard form of Woodward and Colella): reflected shocks, a Mach stem and a vortex sheet from it, plus a corner singularity."
status: established
aliases: [forward facing step, Mach 3 step]
tags: [benchmark, euler, 2d, vortex-sheet]
timestamp: 2026-10-13T00:00:00Z
---

# Mach 3 wind tunnel with a forward-facing step

**Set-up** (introduced by Emery in 1968; standard form and corner
treatment by Woodward & Colella, see *Later uses (batch 11)*; attribution
corrected at the 2026-10-13 deep lint). A tunnel 1 wide and 3 long; a step
0.2 high with its corner at $(0.6, 0.2)$; Mach 3 inflow
($\rho = 1.4$, $p = 1$, $\gamma = 1.4$) at the left, outflow at the
right, reflecting walls; the corner singularity treated as Woodward and
Colella did ([Jiang & Shu (1996)](/sources/jiang-1996.md), §8.3
Example 2; [Balsara & Shu (2000)](/sources/balsara-2000.md), §VII.a).

**Results.**
* WENO-LF-4 and WENO-LF-5 on $122\times 39$ and $242\times 79$ resolve the
  contact from the Mach stem slightly better than ENO-LF-4, with fewer
  small bumps; the pressure–entropy-weight version fails at the strong
  reflected waves ([Jiang & Shu (1996)](/sources/jiang-1996.md)).
* $r = 5$ MPWENO with RF fluxes and no compression on $240\times 80$ to
  $t = 4$ gives sharp shocks and a vortex sheet a few zones wide, with
  little spreading along the domain
  ([Balsara & Shu (2000)](/sources/balsara-2000.md), Fig. 6).

**Later uses (batch 2).** WENO-AO(7,5,3) on $600 \times 200$ shows a
crisp vortex-sheet roll-up at $t = 3$, compared with WENO-ZQ
([Balsara, Garain & Shu (2016)](/sources/balsara-2016.md)); WENO-ZQ and
WENO-JS at $600 \times 200$, $t = 4$ ([Zhu & Qiu (2016)](/sources/zhu-2016.md)).

**Later uses (batch 3).** Fifth-order HLL-based AFD-WENO on
$1440\times480$ to $t = 0.4$, with the corner singularity treated as by
Woodward–Colella and with flattening, gives sharp profiles and a
pronounced roll-up of the vortex sheet
([Balsara et al. (2025)](/sources/balsara-2025.md), §VIII.a).

**Later uses (batch 4).**
* Fourth-order ADER-WENO at $240\times80$, $480\times160$ and
  $960\times320$ to $t = 4$. Roll-up of the vortex sheet starts at
  $480\times160$. The authors judge that an exceptionally good second-order
  scheme would need $960\times320$ to show it ([Balsara et al. (2009)](/sources/balsara-2009.md), §6.3).
* Third-order ADER-WENO on AMR (equivalent $2400\times800$, $t = 2.5$)
  rolls up the slip line much better than a second-order AMR run
  ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4; [high-order AMR](/methods/high-order-amr.md)).
* ADER-DG with $K = 5$ and subcell limiting on $300\times100$ to $t = 4$.
  Kelvin–Helmholtz vortices along the upper shear layer emit acoustic
  waves visible in the isolines, and limiting is confined to the
  shocks ([Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.5). With AMR, on a $150\times50$ base and
  $r_{\mathrm{AMR}} = 4$, the instability is well resolved
  ([Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.4).

**Later uses (batch 7).**
* The sixth-order ADER-DG run with subcell limiting on $300\times100$ is
  reproduced at CFL 0.4; "a very small fraction of zones" is limited
  ([Balsara (2017)](/sources/balsara-2017-d.md), §IX.1).

**Later uses (batch 8).**
* *Solver failure at second order* ($120\times40$, $t = 4$, limited
  Green–Gauss gradients). HLLC and HLLEM perturb the normal-shock stems
  near both walls and badly kink the reflected-shock stem. The
  [shock-instability cures](/methods/shock-instability-cures.md) remove the
  perturbations and improve the kink "considerably"
  ([Simon & Mandal (2019)](/sources/simon-2019.md), §9.7; [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §7.5).

**Later uses (batch 11).** *The Woodward–Colella paper and the origin.*
[Woodward & Colella (1984)](/sources/woodward-1984.md) (§IVb) state
that the problem "was introduced more than a decade ago" by Emery (1968,
J. Comput. Phys. 2:306), with earlier results by van Leer and by Colella.
The description and set-up line above, which attributed the problem
to Woodward–Colella, were corrected accordingly at the 2026-10-13 deep
lint: the problem originates with Emery; Woodward & Colella gave it its
standard form, with the corner treatment below. Their set-up agrees with the line above and adds: initial state
equal to the inflow everywhere, with velocity 3 ($\rho = 1.4$, $p = 1$),
zero gradients at the right, where the exit is always supersonic.
* *Corner treatment* (pp. 131–132). In the first row of zones above the
  step, the first four zones right of the corner; in the next row, the
  first two. There the density is reset so that the entropy equals that
  of the zone just left of and below the corner, and the speed (not the
  direction) so that the total enthalpy per unit mass equals that of the
  same zone. It assumes nearly steady flow, is "clearly inappropriate at
  the very outset", and leaves large errors in flow direction that may
  cause the overexpansion seen at the corner.
* *Evolution* (Fig. 3, PPMLR, $h = 1/80$, i.e. $240\times80$). A Mach stem
  forms at about $t = 1.5$ and moves slowly upstream; the upper contact
  shows a physical Kelvin–Helmholtz instability at $t = 2.5$–3, seeded by
  small numerical entropy oscillations behind the Mach shock. The flow is
  still unsteady at $t = 4$ and steady by $t = 12$. The Mach stem is the
  slowest feature to converge: its formation is a threshold phenomenon,
  and a slightly lower step gives regular reflection.
* *Scheme comparison* (Fig. 7, $t = 4$, $h = 1/20$, $1/40$, $1/80$, mostly
  Courant 0.8). Godunov misshapes and misplaces the shocks even on the
  finest grid, shows a strong numerical boundary layer on the step with a
  spurious second Mach reflection, rarefaction shocks near the sonic line
  above the corner, and a 2D instability of strong stationary shocks
  ([numerical shock instability](/definitions/numerical-shock-instability.md)).
  MUSCL's shocks are one zone wide, thin enough to show the same
  instability. ETBFCT shows staircase contours and spurious Mach
  reflections on the step that do not diminish with refinement. PPMDE is
  essentially noise-free, with the Mach stem right on the middle grid,
  and about 3.6 and 4.4 times more efficient than BBC and MacCormack;
  PPMLR equals it at 18 % more CPU time ([PPM](/methods/ppm.md)).

**Later uses (batch 11, Balsara & Nkonga; merged at the 2026-10-13 deep
lint).** Fourth-order ADER–WENO with a multidimensional HLLI solver at
the vertices, $960\times320$ cells to $t = 4$: the roll-up of the vortex
sheet from the triple point is captured "very well", judged visually
([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §5.1;
[multidimensional Riemann solvers](/methods/multidimensional-riemann-solvers.md)).

**Later uses (batch 14).** *Van Leer's runs.* The "earlier results by
van Leer" are [van Leer (1979)](/sources/vanleer-1979.md), §4, Figs. 7–11 (runs by P. R. Woodward): Mach 3
inflow, step one fifth of the entrance height, plane symmetry,
impulsively started, $\gamma = 1.4$, square meshes. MUSCL on
$60 \times 20$, $30 \times 10$ and $15 \times 5$ cells, and Godunov's
method (all slopes set to zero) on a mesh printed as $80 \times 30$, at
$t \approx 4$ in units of entrance height over inflow sound speed: the
paper states that these results "are far from stationary", and that the
Mach stem on the $15 \times 5$ grid is "an artifact due to the
monotonicity algorithms" (p. 123). MUSCL on $45 \times 15$ cells is run
to a steady state at $t = 16.02$ (Fig. 10).

# Citations

1. [Jiang & Shu (1996)](/sources/jiang-1996.md), §8.3 Example 2.
2. [Balsara & Shu (2000)](/sources/balsara-2000.md), §VII.a.
3. [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §5.6.
4. [Zhu & Qiu (2016)](/sources/zhu-2016.md), Example 3.9.
5. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §VIII.a.
6. [Balsara et al. (2009)](/sources/balsara-2009.md), §6.3.
7. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4.
8. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.5.
9. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.4.
10. [Balsara (2017)](/sources/balsara-2017-d.md), §IX.1.
11. [Simon & Mandal (2019)](/sources/simon-2019.md), §9.7.
12. [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §7.5.
13. [Woodward & Colella (1984)](/sources/woodward-1984.md), §§IVb, VIb, Figs. 3, 7, 8.
14. [Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §5.1.
15. [van Leer (1979)](/sources/vanleer-1979.md), §4, Figs. 7–11.

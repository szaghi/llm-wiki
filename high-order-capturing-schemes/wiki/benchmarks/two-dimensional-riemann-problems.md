---
type: Benchmark
title: "Two-dimensional Riemann problems (four-quadrant configurations)"
description: "Four constant states meeting at the origin of [-0.5, 0.5]² (Schulz-Rinne; Lax–Liu; Kurganov–Tadmor configurations, γ = 1.4): tests genuinely two-dimensional wave interaction, and, at very low dissipation, the onset of Kelvin–Helmholtz roll-up along slip lines."
status: established
aliases: [2D Riemann problems, four-quadrant Riemann problem, Kurganov-Tadmor configurations, Lax-Liu configurations]
tags: [benchmark, euler, 2d, riemann-problem]
timestamp: 2026-10-13T00:00:00Z
---

# Two-dimensional Riemann problems

**Setup.** Constant states in the four quadrants of
$[-0.5, 0.5]^2$, joined at the origin, for the Euler equations with
$\gamma = 1.4$. The configurations follow the classification of
Schulz-Rinne and of Lax and Liu, as catalogued by Kurganov and Tadmor,
who are the reference most papers here compare with
([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4;
[Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.6;
[Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.5). The
quadrant states and final times are tabulated in each paper and are not
reproduced here, because the text layer of the tables is not legible.
The same problems were used to construct genuinely multidimensional
HLL-type Riemann solvers (Balsara, cited by
[Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.6).

## Results in this corpus

* **Third-order ADER-WENO on AMR**, four configurations, base grid
  $50 \times 50$. Results agree with the published references
  ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4;
  [high-order AMR](/methods/high-order-amr.md)).
* **ADER-DG $K = 5$ with subcell limiting**, $100 \times 100$ cells,
  five problems (Kurganov–Tadmor configurations 3, 4, 6, 8 and 12).
  The limiter acts only along strong discontinuities, apart from a few
  start-up cells. Much more small-scale structure than usually reported
  appears, from Kelvin–Helmholtz instability along the shear waves. A
  sixth-order ADER-WENO AMR run at an equivalent $1250^2$ confirms the
  instability for the RP3 case, and the authors take this as evidence
  that the structures are physical
  ([Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.6;
  [a posteriori subcell limiting](/methods/a-posteriori-subcell-limiting.md)).
* **ADER-DG $K = 5$ with subcell limiting and AMR**, base grid $50^2$,
  $r_{\mathrm{AMR}} = 3$, two levels. With AMR the instabilities also
  appear in RP2 (along the diagonal of the cocoon) and RP4 (along the
  bottom-left quadrant boundary), and the limiter works only at the
  finest level ([Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.5).

* **Fifth-order FD-WENO on block-structured AMR**, one configuration
  with discontinuities at $x = y = 0.8$ on $[0, 1]^2$, $t = 0.8$, three
  levels on a $448^2$ base. The paper prints the states
  $(\rho, v_x, v_y, p) = (1.5, 0, 0, 1.5)$, $(0.5323, 1.206, 0, 0.3)$,
  $(0.138, 1.206, 1.206, 0.029)$ and $(0.5323, 0, 1.206, 0.3)$ (eq. 34). Its
  troubled-cell detector flags shocks and shocklets while filtering weak
  acoustic waves. The results are qualitative
  ([Wang et al. (2025)](/sources/wang-2025.md), §6.4.1, preprint).

* **Second-order HLL-type solvers** (MUSCL), two four-contact
  configurations on $[-0.5, 0.5]^2$ with $600^2$ cells (printed states
  $(\rho, v_x, v_y, p)$: case 1 $(2, 0.75, 0.5, 1)$ upper left,
  $(1, -0.75, 0.5, 1)$ lower left, $(1, 0.75, -0.5, 1)$ upper right,
  $(3, -0.75, -0.5, 1)$ lower right; case 2 the same with the signs of
  $v_x$ reversed; end time and boundaries not printed). HLL-BVD resolves
  contacts and shear better than HLL and HLLC; HLL is the most diffusive
  and misses the Kelvin–Helmholtz roll-up. Comparisons are visual
  ([Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §III E,
  eqs. 23–24, Figs. 8–9; merged at the 2026-10-13 deep lint).

**Compiler's reading** (not a source claim; marked at the 2026-10-13
deep lint). Agreement with Kurganov and Tadmor concerns the main wave
structures. The Euler equations carry no physical viscosity, so the
scale at which the extra roll-up appears is set by the numerical
dissipation and the grid: as for the
[double Mach reflection](/benchmarks/double-mach-reflection.md), it is a
qualitative measure of numerical dissipation, not a converged quantity.
This differs in emphasis from Dumbser et al. (2014), who take the
Kelvin–Helmholtz structures as physical because a sixth-order AMR run at
an equivalent $1250^2$ reproduces them in RP3 (above). The two readings
are compatible if the instability of the shear waves is physical and only
its onset scale is numerical; no source in the corpus settles the point
with a convergence study.

# Citations

1. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4.
2. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.6.
3. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.5.
4. [Wang et al. (2025)](/sources/wang-2025.md), §6.4.1 (arXiv preprint).
5. [Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §III E, eqs. 23–24, Figs. 8–9.

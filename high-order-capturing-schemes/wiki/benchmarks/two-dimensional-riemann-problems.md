---
type: Benchmark
title: "Two-dimensional Riemann problems (four-quadrant configurations)"
description: "Four constant states meeting at the origin of [-0.5, 0.5]² (Schulz-Rinne; Lax–Liu; Kurganov–Tadmor configurations, γ = 1.4): tests genuinely two-dimensional wave interaction, and, at very low dissipation, the onset of Kelvin–Helmholtz roll-up along slip lines."
status: established
aliases: [2D Riemann problems, four-quadrant Riemann problem, Kurganov-Tadmor configurations, Lax-Liu configurations]
tags: [benchmark, euler, 2d, riemann-problem]
timestamp: 2026-10-08T00:00:00Z
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

**Reading.** Agreement with Kurganov and Tadmor concerns the main wave
structures. The additional roll-up at very low dissipation is a
resolution effect, with no physical viscosity in the Euler equations.
As for the [double Mach reflection](/benchmarks/double-mach-reflection.md),
it is a qualitative measure of numerical dissipation, not a converged
quantity.

# Citations

1. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4.
2. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.6.
3. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.5.

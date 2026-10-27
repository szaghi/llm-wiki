---
type: Benchmark
title: "RAE 2822 airfoil"
description: "The supercritical RAE 2822 airfoil in transonic flow, case 9 of Cook et al. at corrected Mach 0.734, incidence 2.79° and Reynolds number 6.5 million: a steady RANS test of high-order DG discretizations, shock treatment and mesh adaptation, where uniform refinement gained nothing and adaptation decided accuracy."
status: established
aliases: [RAE2822, RAE 2822, RAE-2822, RAE 2822 case 9, ADIGMA MTC5]
tags: [benchmark, rans, compressible, dg, mesh-adaptation, boundary-layer]
timestamp: 2026-10-27T11:00:00Z
---

# RAE 2822 airfoil

The RAE 2822 is a supercritical airfoil whose transonic **case 9**, for
which [Wang et al. (2013)](/sources/wang-2013.md), §4.8, cite the
experimental database of Cook et al. (AGARD AR-138, their ref. 27), is a
steady RANS test "investigated numerically by many authors" (§4.8): at free-stream Mach number $M$
about 0.73 a supersonic pocket on the suction side ends in a shock that
interacts with the attached turbulent boundary layer, so that lift,
drag and the shock position depend on the boundary-layer displacement and
on the shock treatment of the discretization. The quantities compared are
the lift and drag coefficients $C_L$, $C_D$ and the surface pressure
coefficient $C_p$. All three ingested sources run it with high-order
discontinuous Galerkin RANS, so in this bundle it tests the step from
second-order to high-order RANS on a flow with a shock: convergence of
forces under refinement, robustness of the turbulence-model equations at
the shock, and [mesh adaptation](/methods/mesh-adaptation.md).

## Case definition

[Wang et al. (2013)](/sources/wang-2013.md), §4.8 (case C2.2 of the First
International Workshop on High-Order CFD Methods, also ADIGMA MTC5),
specify the case as:

- experimental conditions $M=0.730$, $\alpha=3.19^\circ$ ($\alpha$
  page-local: angle of attack), $Re=6.5\times10^6$ on the chord; computed
  at the corrected conditions $M=0.734$, $\alpha=2.79^\circ$;
- two-dimensional RANS with the [Spalart–Allmaras](/methods/spalart-allmaras-model.md),
  Wilcox [$k$-$\omega$](/methods/k-omega-model.md) or an explicit algebraic
  Reynolds-stress model ([Reynolds-stress models](/methods/reynolds-stress-model.md));
- transition fixed at 3% chord on both sides, $Pr=0.71$, constant
  viscosity;
- a far field placed so that it changes the forces by less than $10^{-6}$
  (0.01 counts), the tolerance the workshop also asks of the reference
  forces (§3.2);
- target quantities: lift and drag coefficients and the skin-friction
  distribution.

The two later sources run the same corrected conditions
($M_\infty=0.734$, $\alpha=2.79^\circ$, $Re=6.5\times10^6$):
[Jiang et al. (2025)](/sources/jiang-2025.md), §4.2, and
[Schotte et al. (2026)](/sources/schotte-2026.md), §4.3, who call it
case 9.

## Runs

| Item | [Wang et al. (2013)](/sources/wang-2013.md), §5.4 | [Jiang et al. (2025)](/sources/jiang-2025.md), §4.2 | [Schotte et al. (2026)](/sources/schotte-2026.md), §4.3 |
|---|---|---|---|
| Closure | SA (MIT, Michigan), EARSM and $k$-$\omega$ (Bergamo) | the $k$-$\sqrt kL$ model of [scale-adaptive simulation](/methods/scale-adaptive-simulation.md), run as steady RANS | negative Spalart–Allmaras (SA-neg) |
| Discretization | three DG groups, polynomial degrees $N=1$ and 3 | modal DG, $N=2$ and 3, 8958 elements | modal DG in CODA, $N=1$ and 2, anisotropic adapted meshes |
| Shock treatment | not specified per group | Hermite-WENO limiting in troubled cells | Laplacian [artificial viscosity](/methods/artificial-viscosity-shock-capturing.md) with the Persson–Peraire sensor and a positivity limiter |
| Reference | the workshop's hp-independent forces | measured $C_L=0.803$, $C_D=0.0168$ | finite-volume solution on 230,084 hexahedra |

## What the case tests

**No gain from high order under uniform refinement.** In the workshop,
[Wang et al. (2013)](/sources/wang-2013.md), §5.4, Table V, Fig. 23, find
"a large spread among the groups and virtually no improvement from high
order under uniform mesh refinement", which they attribute partly to an
initial mesh whose wake is not aligned with the flow and partly to the
choice of turbulence model; adaptive mesh optimisation was "markedly
superior". In their conclusions they add that high-order RANS was still
less robust than low-order RANS in converging to a steady state, which
they "believe" related to non-smoothness introduced by the turbulence
models, and call for "smooth turbulence models" (§6). For non-smooth
problems, shocks among them, the workshop found no evidence to rank high
order against low order (§6).

**A two-equation model in DG.** [Jiang et al. (2025)](/sources/jiang-2025.md),
§4.2, Figs. 6–7, obtain $C_L=0.779$ ($N=2$) and 0.782 ($N=3$),
$C_D=0.0177$ and 0.0176 against the measured 0.803 and 0.0168, errors
"around the range of 3% and 5%"; the density residual falls by almost five
orders at $N=3$, $C_p$ agrees with the experiment with a small deviation at
the shock, and the von Kármán length oscillates at the shock without
visibly affecting the eddy viscosity. The Hermite-WENO limiting that
captures the shock is the one they use to remove oscillations of $k$ at
the boundary-layer edge (§3.1; see [WENO scheme](/methods/weno-scheme.md)).

**Mesh adaptation at high order.** [Schotte et al. (2026)](/sources/schotte-2026.md),
§4.3, Table 4, Figs. 15–16, compare adaptation strategies built on a
Mach-number Hessian, unscaled or scaled by a DG small-scale estimator
(SSED, or SSL with a lifting term):

| Strategy | DOF | $C_L$ | $C_D$ |
|---|---|---|---|
| $N=1$, unscaled Hessian | 67,395 | 0.8235 | 0.01893 |
| $N=2$, unscaled Hessian | 63,378 | 0.8238 | 0.01894 |
| $N=2$, SSED | 69,954 | 0.8222 | 0.01884 |
| $N=2$, SSL | 37,560 | 0.8229 | 0.01885 |
| finite volume, hexahedra | 230,084 | 0.816 | 0.0189 |

The $N=1$ and SSL strategies refine the shock more finely at similar
degrees of freedom, SSED the least; the scaled strategies are less
accurate on very coarse meshes but converge earlier, SSL with the fewest
degrees of freedom; the finite-volume results are not mesh-converged on
the finest grid. The details of the metric are on
[mesh adaptation](/methods/mesh-adaptation.md).

**What the sources report together.** The workshop found adaptive mesh
optimisation "markedly superior" to uniform refinement on this case
([Wang et al. (2013)](/sources/wang-2013.md), §5.4);
[Schotte et al. (2026)](/sources/schotte-2026.md) compare adaptation
strategies only, the SSL-scaled $N=2$ adaptation converging with the
fewest degrees of freedom. Jiang et al. run fixed meshes; their $C_L$
changes by 0.4% between $N=2$ and 3 *(compiler check, not in the
sources)*.

## Qualifications

- The sources compare with different references: the hp-independent
  forces of the workshop, the measured forces (Jiang et al.), and a
  finite-volume solution that the authors themselves call not converged
  (Schotte et al.). No source compares its forces with another's.
- The forces differ between closures and solvers: about 0.78 for lift
  with the $k$-$\sqrt kL$ model on a fixed mesh, about 0.82 with SA-neg on
  adapted meshes, against the 0.803 measured that Jiang et al. print;
  drag 0.0176–0.0177 against 0.0188–0.0189 *(compiler check, not in the
  sources)*. The two studies use different closures, shock treatments and
  meshes, so the difference is not attributed to any one of them.
- [Schotte et al. (2026)](/sources/schotte-2026.md) state that the adapted
  strategies "always provide a higher $C_l$ and lower $C_d$" than finite
  volume, while their Table 4 prints the $N=1$ and unscaled $N=2$ drag
  (0.01893, 0.01894) above the three-digit finite-volume 0.0189; the slip
  is also recorded on [mesh adaptation](/methods/mesh-adaptation.md).
- [Wang et al. (2013)](/sources/wang-2013.md) print no force values for
  the workshop entries in the text; their comparison is the error against
  degrees of freedom and work units of Fig. 23. Their statement on smooth
  turbulence models is worded as a belief ("believe"), with no
  demonstration in the paper.

# Citations

- [Wang et al. (2013)](/sources/wang-2013.md) — §3.2; §4.8 (case C2.2); §5.4, Table V, Fig. 23; §6.
- [Jiang et al. (2025)](/sources/jiang-2025.md) — §3.1; §4.2, Figs. 6–7.
- [Schotte et al. (2026)](/sources/schotte-2026.md) — §4.3, Table 4, Figs. 15–16.

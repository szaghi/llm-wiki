---
type: Benchmark
title: "NACA 0012 airfoil"
description: "The symmetric NACA 0012 airfoil, static at chord Reynolds numbers of 1 to 6 million from attached incidence to 45° and transonic at Mach 0.804, and pitching in deep dynamic stall at 135,000: a validation case of RANS discretizations and near-wall treatments, of data-driven RANS corrections, and of the span of wall-resolved LES."
status: established
aliases: [NACA0012, NACA 0012, NACA-0012]
tags: [benchmark, rans, hybrid-rans-les, les, data-driven, immersed-boundary, dg, separated-flow]
timestamp: 2026-10-26T20:47:00Z
---

# NACA 0012 airfoil

The NACA 0012 is a symmetric airfoil of 12% thickness. At low Mach number
and chord Reynolds numbers $Re_c$ of a few million its boundary layers are
attached at small incidence $\alpha$ (page-local: angle of attack), lift
grows linearly with $\alpha$, and near stall the suction peak and the thin
leading-edge boundary layer dominate the forces; at very high incidence the
flow separates massively from the leading edge. The quantities compared are
the lift and drag coefficients $C_L$ and $C_D$, the pressure coefficient
$C_p$ and the skin friction $C_f$ along the chord $c$. Reference data
recalled by the sources are the measurements of Ladson (forces and $C_p$) and
the compilation of McCroskey. In this bundle the static airfoil validates
discretizations and near-wall treatments of RANS and hybrid RANS/LES, and
is a non-regression test of data-driven RANS corrections: an attached flow
that a correction trained on separated flows must not spoil. The pitching
airfoil in deep dynamic stall tests wall-resolved LES and its spanwise
domain size.

## Configurations in the sources

| Item | [Zhao et al. (2023b)](/sources/zhao-2023-b.md) | [Constant et al. (2024)](/sources/constant-2024.md) | [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) |
|---|---|---|---|
| Flow | $M=0.15$, $Re_c\approx6\times10^6$, $\alpha=0^\circ$, $10^\circ$; transonic $M=0.804$, $Re_c=4.09\times10^6$, $\alpha=0.05^\circ$ | $M=0.15$, $Re_c=6\times10^6$, $\alpha=0^\circ$ to $15^\circ$ | $Re_c=3\times10^6$, $\alpha=2^\circ$, $6^\circ$, $10^\circ$, $15^\circ$ and $45^\circ$; Mach number not stated |
| Model | [$k$-$\omega$ SST](/methods/k-omega-sst-model.md) RANS, wall-resolved | [Spalart–Allmaras](/methods/spalart-allmaras-model.md) RANS with Musker's wall function | SST RANS, SST-IDDES and SST-based [continuous eddy simulation](/methods/continuous-eddy-simulation.md) |
| Discretization | interior-penalty DG of degree $N=2$ for the mean flow, first-order finite volumes for SST | ghost-cell [immersed boundary](/methods/immersed-boundary-method.md) on octree Cartesian grids, second-order finite volumes (FastS) | [lattice Boltzmann](/methods/lattice-boltzmann-method.md) D3Q19 on octree Cartesian grids with immersed boundaries ([ProLB](/software/prolb.md)) |
| Grid | 5883 elements (grid independence on 6834, 8844, 10854); 8954 cells transonic | IBM6: $h_{\min}/c=10^{-4}$, target $y^+=100$, $3.8\times10^6$ cells; body-fitted wall-resolved reference with $h_{\min}/c=10^{-6}$, $y^+=1$, $8\times10^6$ cells | 7 refinement levels to $\Delta_{\min}\approx0.18\%c$; span equal to chord, periodic |
| Reference | Ladson ($C_p$), McCroskey (forces), ONERA data (transonic) | the body-fitted wall-resolved solution | Ladson (forces, $C_p$); for $45^\circ$ the data of Shur et al. as cited |

Data-driven RANS corrections ([Wu et al. (2025)](/sources/wu-2025.md),
§4.5; [Oulghelou et al. (2025)](/sources/oulghelou-2025.md), §5.1.3) and
deep dynamic stall ([Baldan & Guardone (2025)](/sources/baldan-2025.md)):

| Item | Wu et al. (2025) | Oulghelou et al. (2025) | Baldan & Guardone (2025) |
|---|---|---|---|
| Flow | $Re_c=6\times10^6$, $M\approx0.15$, $\alpha=0^\circ$ | $Re_c=6\times10^6$, chord 1 m, $\alpha=0^\circ$–$18^\circ$, NASA TMR set-up | pitching $\alpha(t)=10^\circ+15^\circ\sin(\varpi_{\mathrm p}t)$ ($\varpi_{\mathrm p}$ page-local: angular pitching frequency; the source's $\omega$), reduced frequency 0.1, $Re_c=1.35\times10^5$, $U_\infty=14$ m/s, incompressible |
| Model | $k$-$\omega$ SST and two symbolic-regression corrections of it (SR-CLS, SR-CND) | SST, two expert corrections and their learned blend | wall-resolved LES with the [WALE model](/methods/wale-model.md); 2D URANS and 3D SBES of the authors' earlier work |
| Discretization | OpenFOAM simpleFoam; C-grid of 640 surface, 120 wake and 136 wall-normal cells, $\Delta y^+\approx0.6$ | OpenFOAM (modified), $225\times65$ grid of the NASA TMR | ANSYS Fluent, second-order finite volume, SIMPLEC, rigidly rotating O-grid of $934\times334$ nodes, first cell $10^{-4}c$, far field $50c$ |
| Reference | SST itself (NASA TMR) for $C_f$ | Ladson; Gregory & O'Reilly; Abbott & von Doenhoff | experiment of Lee & Gerontakos (loads) |

High-order RANS discretizations of the $k$-$\omega$ family
([Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md), §5.4;
[Ghidoni et al. (2026)](/sources/ghidoni-2026.md), §4.4):

| Item | Elzaabalawy et al. (2023) | Ghidoni et al. (2026) |
|---|---|---|
| Flow | $Re_c=6\times10^6$, $\alpha=0^\circ$, steady incompressible; inlet eddy-viscosity ratio 6 | $Re_c=6\times10^6$, $M=0.15$, $-15^\circ\le\alpha\le15^\circ$, steady |
| Model | two-equation [$k$-$\omega$ models](/methods/k-omega-model.md) (the model of this case is not named in §5.4), wall-resolved | Wilcox $k$-$\omega$ (2006/2007 version) in log-$\omega$ form, with an explicit [wall function](/methods/rans-wall-function.md) |
| Discretization | hybridizable DG, degree $N=3$ triangles | modal DG, $N=1$ to 6 |
| Grid | first element at $y^+=2$, clustered at leading and trailing edges, $x^+<3$ at the trailing edge | hybrid meshes (hexahedra in the boundary layer, prisms outside), far field at $50c$; wall-resolved reference of 6535 elements with 200 on the airfoil; meshes with first-element height $y_1^+$ up to 320 |
| Reference | Ladson ($C_p$); NASA TMR SST ($C_f$) | the wall-resolved $N=6$ solution; FUN3D $k$-$\omega$ (NASA TMR); Ladson, Gregory & O'Reilly, Abbott & von Doenhoff |

## What the case tests

**Attached and moderate incidence.** [Zhao et al. (2023b)](/sources/zhao-2023-b.md),
§5.2, obtain $C_p$ coinciding with Ladson's experiment at $0^\circ$ for
polynomial degrees 1 to 3, and agreement with experiment at $10^\circ$ (Figs.
5-4, 5-6). Their forces (Table 5-1) are:

| $\alpha$ | $C_L$ IPDG / McCroskey | $C_D$ IPDG / McCroskey |
|---|---|---|
| $0^\circ$ | 0.00 / 0.00 | 0.0084 / 0.0083 |
| $10^\circ$ | 0.93 / 1.05 | 0.011 / 0.012 |

The authors attribute the $10^\circ$ lift deficit "probably" to the RANS
assumption; it is 11.4% *(compiler check, not in the sources)*. On the
lattice Boltzmann solver, [Mozaffari et al. (2024)](/sources/mozaffari-2024.md),
§3.2, find $C_L$ and $C_D$ close to Ladson's data at $2^\circ$, $6^\circ$ and
$10^\circ$ for all three models, with a slight RANS discrepancy at $15^\circ$
(Fig. 12). IDDES, CES and RANS give identical mean $C_p$ at $10^\circ$; at
$15^\circ$ the hybrids differ slightly downstream of the leading edge
because the fine leading-edge grid lets them run as LES in the outer
boundary layer with only the first few nodes in RANS (Figs. 10–11); see
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) and
[detached-eddy simulation](/methods/detached-eddy-simulation.md).

**Near stall with an immersed boundary and a wall function.**
[Constant et al. (2024)](/sources/constant-2024.md) (read in the HAL
author manuscript) use the airfoil at $15^\circ$ as the "critical flow
incidence" for wall-function boundary conditions on Cartesian grids:

- A modelling height estimated from a flat-plate skin-friction correlation
  places the first computed point at a $y^+$ far above the target near the
  leading edge: the relative error is "close to 300%" for a target of 300
  at $15^\circ$ (§4.1, Fig. 10). After their one-pass adaptation, the
  largest suction-side $y^+$ falls from 435 to 243 for a target of 100
  (§6.1, Fig. 18).
- Over the first 10% of the chord the equilibrium wall function cannot
  represent the velocity profile; beyond it the log region is established
  (§6.1, Figs. 19–21); see
  [equilibrium wall model](/methods/equilibrium-wall-model.md) and
  [wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md).
- Extrapolating the wall pressure from the image point with zero normal
  gradient misplaces the suction peak; a first- or second-order
  reconstruction from a second layer of image points corrects it (§6.1,
  Figs. 23–24).

Forces at $15^\circ$ (Table 3):

| Solution | $C_D\times10^3$ | error | $C_L$ |
|---|---|---|---|
| body-fitted, wall-resolved | 20.85 | — | 1.516 |
| IBM, single modelling height, zeroth-order pressure | 40.44 | 94% | 1.416 |
| IBM, adapted height, zeroth-order pressure | 30.57 | 47% | — |
| IBM, adapted height, second-order pressure | 24.51 | 17% | 1.476 |

Only the adapted solution keeps the lift error below 3% at every incidence
(Fig. 25). The authors relate the remaining drag error of about 20% at
$15^\circ$ to the sensitivity of this test case reported by others, and to
the equilibrium wall model at the leading edge (§6.1).

**High-order RANS of the $k$-$\omega$ family.**
[Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md), §5.4, use the
airfoil to show that their hybridizable DG treatment of the
$\omega$ equation (interpolation of $1/\omega$, removal of the
wall-touching elements from the $\omega$ problem) works on curved geometry.
$C_f$ is over-estimated against the NASA TMR SST solution, which they
attribute to the raised inlet eddy viscosity; $C_p$ lies slightly below
the TMR reference but closer to Ladson's experiment. $\omega$ oscillates in
the wake, and at lower inlet eddy-viscosity ratios the oscillations
"obstruct the convergence of the solver", "one of the drawbacks of using
high-order methods while using the $k-\omega$ model" (Figs. 28–36).

[Ghidoni et al. (2026)](/sources/ghidoni-2026.md), §4.4, test the
first-element height that a wall function tolerates on a modal DG
discretization: $C_p$, $C_f$, $C_D$ and $C_L$ agree with the wall-resolved
reference for all $y_1^+$ and degrees (Figs. 13–14). At $N=6$ the $C_f$
difference grows for $y_1^+>80$ near the leading edge; at $y_1^+=320$ the
$C_f$ peak is under-estimated and recovers from $x/c=0.15$, so the effect on
$C_D$ and $C_L$ is negligible. At $\alpha=15^\circ$ the suction side shows
incipient separation from $x/c=0.72$ that reattaches only at the trailing
edge; the wall function avoids the $C_f$ under-estimation it shows in the
recirculation of the [backward-facing step](/benchmarks/backward-facing-step.md),
which the authors attribute to the smaller recirculation.

**Massive separation at $45^\circ$.** [Mozaffari et al. (2024)](/sources/mozaffari-2024.md),
§3.2, Table 2, after 234 flow-through times with 110 averaged:

| Model | $C_L$ | $C_D$ |
|---|---|---|
| SST RANS | 2.238 | 2.053 |
| SST-IDDES | 1.231 | 1.038 |
| SST-CES | 1.192 | 0.993 |
| reference (Shur et al., as cited) | 1.097 | 1.180 |

The RANS lift and drag exceed the reference by factors of about 2.0 and
1.7 *(compiler check, not in the sources)*; the two hybrids "perform
almost the same without any superiority" (§3.2).

**Transonic shock.** At $M=0.804$, [Zhao et al. (2023b)](/sources/zhao-2023-b.md),
§5.3, place the shock at $x\approx0.47c$ with $C_p$ extrema consistent with
ONERA data, but "the ending position of the shock wave slightly lags
behind", attributed to an overestimated shock–boundary-layer interaction
(Figs. 5-9–5-11); see
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).

**Implicit LES polars.** As recalled by [Ferrer et al. (2023)](/sources/ferrer-2023.md),
§4.1, Fig. 7, from the group's earlier paper, a DG implicit LES at
$Re_c=10^6$ on 18,000 hexahedra with $N=4$ (2.2 million degrees of freedom)
gives lift and drag polars in "very good agreement" with experimental data
not named in that paper; see [implicit LES](/definitions/implicit-les.md)
and [HORSES3D](/software/horses3d.md).

**Non-regression of data-driven RANS corrections.** Both data-driven
sources use the static airfoil as a flow their corrections were not
trained on.

- [Wu et al. (2025)](/sources/wu-2025.md), §4.5, Fig. 50, take SST as
  accurate for the attached $C_f$ at $\alpha=0^\circ$ and test whether two
  [symbolic-regression](/methods/symbolic-regression-closure.md) corrections
  of the SST $\omega$-destruction term, fitted to
  [field-inversion](/methods/field-inversion-machine-learning.md) data of
  separated flows, leave it unchanged ("L2 generalizability" in their
  four-level scale, Table 1). SR-CND, whose correction is gated by the DDES
  shielding function so that it vanishes in attached boundary layers, gives
  nearly the same $C_f$ as SST; SR-CLS, trained by classic ungated
  inversion, overpredicts it. The same pair behaves the same way on the
  zero-pressure-gradient [flat plate](/benchmarks/turbulent-boundary-layer.md).
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md), §5.1.3, run the
  polar from $0^\circ$ to $18^\circ$ with three experts (baseline SST; a
  separated-flow correction; a jet correction) and a random-forest
  [blend of the experts](/methods/turbulence-model-aggregation.md). The jet
  expert gives the largest $C_L$ and $C_D$ discrepancies; SST "performs
  better than" the separated-flow expert "for most of the present flows,
  the latter model being too dissipative", so that expert "should be
  replaced or supplemented"; the blend reproduces the lift-curve slope,
  drag and surface pressure near SST, giving the separated-flow expert
  weight in moderately separated suction-side regions and SST in attached
  ones (Figs. 15–16). No error table is printed for this case. Projected in
  latent feature spaces (PCA, t-SNE, autoencoder), the airfoil features
  lie mostly inside the training region, with outliers "especially at
  higher angles of attack" (§5.1, Fig. 10).

**Deep dynamic stall and the spanwise domain.**
[Baldan & Guardone (2025)](/sources/baldan-2025.md) (read in arXiv v2)
simulate the Lee & Gerontakos pitching airfoil, $-5^\circ\le\alpha\le25^\circ$,
with wall-resolved LES on four spanwise-periodic extrusions,
$L_z/c=0.2$, 0.4, 0.8 and 1.2, at the same $\Delta z=10^{-3}c$ (62.7 to
374.7 million nodes). The wall resolution satisfies $\Delta x^+<40$,
$\Delta y^+<5$, $\Delta z^+<20$ on all grids, including the instant when
the near-wall velocity exceeds twice the free stream (§2.1, Fig. 7). The
cycle takes 144,000 time steps of $2.337\times10^{-6}$ s
($2.181\times10^{-4}$ convective times, CFL about 1); one cycle is recorded
after a quarter cycle is discarded, without phase averaging (§1.2).

- *Upstroke.* With the flow attached and a
  [laminar separation bubble](/definitions/laminar-separation-bubble.md)
  near the leading edge, the span does not matter: from $-5^\circ$ to about
  $22^\circ$ the four spans differ by at most 0.05 in $C_L$ (Fig. 3).
  Transition starts near the trailing edge around $\alpha=2^\circ$ and moves
  towards the bubble by $10^\circ$; the dynamic-stall vortex forms beyond
  $15^\circ$ and reaches the trailing edge at $22^\circ$ (Fig. 6).
- *Downstroke.* Once the bubble bursts and the dynamic-stall vortex forms,
  the two short spans force a quasi-two-dimensional vortex with a more
  coherent core and higher peak velocity, and the trailing-edge-vortex
  interaction produces spurious lift peaks exceeding the upstroke $C_L$ by
  0.5 and $C_D$ by 0.3. The two long spans develop three-dimensional
  structures and follow the experimental downstroke trend with a $C_L$
  offset of about 0.25 (Figs. 3–4). At $10^\circ$ in the downstroke the
  1.2$c$ span is fully stalled while 0.8$c$ still shows oscillatory wake
  patterns (Fig. 4).
- *Recommendation.* A span of at least one chord is needed to capture the
  dynamic-stall vortex in the downstroke; the 0.05$c$–0.2$c$ spans common in
  the LES literature are adequate only for the attached upstroke, the part
  that ramp-up studies simulate (§3).
- *Model comparison.* The 1.2$c$ LES, 2D URANS ($k$-$\omega$ SST with an
  intermittency transition model) and 3D SBES agree within 0.1 in $C_L$ in
  attached flow, all put peak lift at $22^\circ$ against $24^\circ$
  measured, diverge in the early stalled downstroke ($24^\circ$–$18^\circ$)
  and reconverge later; a $C_L$ offset of 0.2 from experiment persists
  (§2.2, Fig. 9). The authors infer that the experiment–simulation
  discrepancies usually blamed on turbulence models come instead from other
  factors, such as wind-tunnel effects or the model's surface roughness
  (§3). The span requirement belongs also to
  [grid-point requirements of LES](/results/les-grid-point-requirements.md).

**What the sources share.** Away from stall the RANS solutions of all
three discretizations match the reference forces; the discrepancies
gather at the leading edge at high incidence: the $10^\circ$ lift deficit
in [Zhao et al. (2023b)](/sources/zhao-2023-b.md), the wall-function
leading-edge error at $15^\circ$ in
[Constant et al. (2024)](/sources/constant-2024.md), the $15^\circ$ RANS
discrepancy in [Mozaffari et al. (2024)](/sources/mozaffari-2024.md).
The two high-order $k$-$\omega$ studies place their difficulty at the
leading edge as well (the $C_f$ peak at $y_1^+=320$ in
[Ghidoni et al. (2026)](/sources/ghidoni-2026.md)) and, for the
discretization itself, in the wake (the $\omega$ oscillations of
[Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md)).

## Qualifications

- The configurations differ in Reynolds number ($1.35\times10^5$, $10^6$,
  $3\times10^6$, $4.09\times10^6$, $6\times10^6$) and reference ($C_p$ and forces of experiments, a
  body-fitted computation); no source compares its errors with another's.
- [Constant et al. (2024)](/sources/constant-2024.md) print a lift error
  of 5.6% for the non-adapted solution in Table 3, while the table's own
  coefficients give 6.6%, and call the non-adapted lift error at $15^\circ$
  "almost 10%" in the text *(compiler check, not in the sources)*.
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) head the
  $45^\circ$ reference column "Exp." while citing Shur et al.'s
  detached-eddy simulation of an airfoil at high incidence; they mention
  $60^\circ$ without reporting results. The chord is not stated.

- [Baldan & Guardone (2025)](/sources/baldan-2025.md) print the angular
  frequency of the pitching motion as "18.67 [Hz]"; their own step count
  and step size give a period of 0.3365 s, so 18.67 is in rad/s
  *(compiler check, not in the sources)*. They say transition starts at the
  trailing edge "progressing downstream" (Introduction), while §2.1 has it
  progressing towards the bubble, i.e. upstream. Their Table 1 quad count
  (311,622) does not match the hexahedra of Table 2, which correspond to
  $933\times333$ quads per layer *(compiler check, not in the sources)*.
  The $C_L$ offset from experiment is printed as about 0.25 (§2.1) and 0.2
  (§2.2).
- Their inference that turbulence modelling is not the main source of
  discrepancy rests on one recorded cycle per model without phase
  averaging (§1.2, §2.2); the URANS and SBES come from the authors' earlier
  work with the same solver, and the 0.8$c$ and 1.2$c$ spans still differ
  at $10^\circ$ in the downstroke (Fig. 4).
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) caption their
  Fig. 33 with $Re=6.6\times10^6$, while the text and the other figures of
  the case give $6\times10^6$. [Ghidoni et al. (2026)](/sources/ghidoni-2026.md)
  print the element counts of their coarser meshes as
  "$5\,929<n_e<2\,899$" (§4.4), an inverted inequality.
- [Wu et al. (2025)](/sources/wu-2025.md) refer to "Figure 45" for the
  airfoil C-grid, which is their Fig. 49. The NACA 0012 claims of
  [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) ("accurate
  predictions of lift, drag", §6) rest on plots without error metrics.

# Citations

- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §5.2, Table 5-1, Figs. 5-4–5-6; §5.3, Figs. 5-9–5-11.
- [Constant et al. (2024)](/sources/constant-2024.md) — §4.1, Fig. 10; §5.1, Figs. 12–13; §6.1, Tables 1–3, Figs. 18–25.
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §3.2, Table 2, Figs. 9–12.
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §4.1, Fig. 7 (recalled result).
- [Wu et al. (2025)](/sources/wu-2025.md) — author manuscript: Table 1; §4.5, Figs. 49–50.
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — arXiv v2: §5.1, Fig. 10; §5.1.3, Figs. 15–16; §6.
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §5.4, Figs. 28–36.
- [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) — §4.4, Figs. 13–14.
- [Baldan & Guardone (2025)](/sources/baldan-2025.md) — arXiv v2: Introduction; §1.1–1.2, Eq. 1, Tables 1–2; §2.1, Figs. 3–8; §2.2, Fig. 9; §3.

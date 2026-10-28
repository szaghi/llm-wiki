---
type: Benchmark
title: "Turbine cascades (T106, T161, VKI LS89)"
description: "Linear turbine cascades as transition, loss, vortex and mesh-adaptation benchmarks: the high-lift low-pressure T106A, T106C, T108 and T161 cascades with laminar separation near exit Reynolds number 10⁵, the transonic VKI LS89 vane with bypass transition and heat transfer, and a transonic rotor cascade whose tip-leakage vortex a hybrid RANS/LES resolves."
status: established
aliases: [turbine cascade, linear turbine cascade, LPT cascade, T106A, T106C, T106c, T108, T161, MTU T161, VKI LS89, LS89 vane, Pak-B cascade, Pack B, L2F, tip-leakage turbine cascade, Arts transonic turbine cascade]
tags: [benchmark, turbomachinery, transition, implicit-les, rans, boundary-layer, des, mesh-adaptation]
timestamp: 2026-10-28T07:09:00Z
---

# Turbine cascades (T106, T161, VKI LS89)

A linear cascade is a row of identical blades in a wind tunnel, computed
over one blade passage with pitchwise periodicity. Turbine blades turn and
accelerate the flow, so the suction-side boundary layer is laminar over
much of the blade and its transition decides the losses. Two families
appear in the sources. **Low-pressure-turbine (LPT) cascades** of high
lift (T106C, T108, T161, Pak-B) run at exit Reynolds numbers of order
$10^5$ and low free-stream turbulence, where the suction-side layer
separates laminar and transitions in the separated shear layer (a
[laminar separation bubble](/definitions/laminar-separation-bubble.md),
open at the lowest Reynolds numbers). The **VKI LS89 high-pressure-turbine
vane** runs transonic, with a shock on the suction side and exit Reynolds
numbers of $6\times10^5$ to $2\times10^6$, where free-stream turbulence
drives bypass transition and the measured wall heat transfer is the
discriminating quantity. A third use is a **transonic high-pressure
turbine rotor cascade with tip clearance**, where the tip-leakage vortex,
not the blade boundary layer, is the object. The quantities compared are the isentropic Mach
number $M_{is}$ (page-local: from the wall pressure and the inlet total
pressure) along the blade, the wake total-pressure loss and its integral,
secondary-flow losses near the end walls, and on LS89 the heat-transfer
coefficient (HTC). Reynolds and Mach numbers are those of the isentropic
exit state, $Re_{2,is}$ and $M_{2,is}$ (page-local), on the chord.

## Configurations in the sources

| Cascade | Source | Conditions | Method |
|---|---|---|---|
| T106C (aft-loaded LPT) | [Wang (2024)](/sources/wang-2024-b.md), §4.2, Table 3 | exit $Re=8\times10^4$, exit Mach 0.65, no free-stream turbulence, pitch/chord 0.95, inlet angle 32.7° (HiOCFD-4 workshop case) | implicit LES, flux reconstruction recovering nodal DG, $N=3$, $1.23\times10^5$ hexahedra, $7.87\times10^6$ degrees of freedom per equation, local modal filter |
| T106C | [Pacciani et al. (2025)](/sources/pacciani-2025.md), §6.2, Table 5 | $Re_{2,is}=0.8$, 1.2, $1.6\times10^5$, $M_{2,is}=0.6$, $Tu=0.8\%$ | steady 2D RANS, [laminar kinetic energy model](/methods/laminar-kinetic-energy-transition-model.md) on [$k$-$\omega$ SST](/methods/k-omega-sst-model.md) |
| T106c | [Ims & Wang (2023)](/sources/ims-2023.md), §5.1 | $M_{is}=0.65$, $Re_{is}=80{,}000$ (chord; isentropic values, subscript as printed), pitch $0.95C$, span $0.1C$, inflow angle 32.7° (HiOCFD4/5 workshops; page-local $C$ the chord) | implicit LES, flux reconstruction ([hpMusic](/software/hpmusic.md)), $N=2$, adaptive h-refinement by three error indicators; reference: hpMusic DNS of Alhawwary & Wang |
| T106a | [Ims & Wang (2023)](/sources/ims-2023.md), §5.2 | $M_{is}=0.4$, $Re_{is}=60{,}000$, pitch $0.798C$, span $0.1C$, blade angle 46.1° ("differing slightly from the workshop's version") | as above at $N=1$ from a coarser start mesh; reference: $N=4$ on the uniformly refined base mesh; random-refinement control |
| T108 (front-loaded LPT) | [Pacciani et al. (2025)](/sources/pacciani-2025.md), §6.2 | as T106C, pitch/chord 1.1 | as above |
| T161 (high-lift LPT between diverging end walls) | [Morsbach et al. (2024)](/sources/morsbach-2024.md), §3.1–3.2, Tables 1–2 | $Re_{2,is}=9\times10^4$, $M_{2,is}=0.6$, inflow angle 41°, synthetic turbulent end-wall layers and free-stream turbulence | implicit LES, [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) $N=5$ with kinetic-energy-preserving split form, $1.89\times10^8$ degrees of freedom; RANS with SST and SSG/LRR-ω plus γ-$Re_\theta$ |
| T106A (LPT) | [Ma et al. (2022)](/sources/ma-2022.md), §3.3 | $Re\approx6\times10^4$ on exit velocity and axial chord; single passage, pitchwise and spanwise periodic; geometry and boundary conditions from Wang et al.; Mach number and inflow turbulence not printed | implicit LES with weighted compact nonlinear schemes (WCNS-E, WCNS-T, linear WCNS-E), block-structured grid of about $1.2\times10^7$ points |
| Pak-B (LPT) | [Menter et al. (2022)](/sources/menter-2022.md), Fig. 24 | $Re=5\times10^4$ to $1.72\times10^5$ on inlet velocity and axial chord, $Tu=0.08\%$ to 4% | RANS with three [local-correlation transition models](/methods/local-correlation-based-transition-model.md) |
| VKI LS89 (transonic HPT vane) | [Wang (2024)](/sources/wang-2024-b.md), §4.3, Tables 5–6 | MUR129: exit $Re=1.13\times10^6$, no free-stream turbulence in the computation (0.8% measured), wall temperature 297.75 K | implicit LES, $N=2$ and 3, 10 to 20 spanwise layers, $6.6\times10^6$ to $31.3\times10^6$ degrees of freedom |
| VKI LS89 | [Pacciani et al. (2025)](/sources/pacciani-2025.md), §6.1, Table 4 | Mur224, Mur228 ($Re_{2,is}\approx6\times10^5$), Mur239, Mur247 ($\approx2.1\times10^6$), $M_{2,is}\approx0.92$–0.93, $Tu=6\%$ and 1% | steady 2D RANS, laminar kinetic energy model, $3\times10^5$ cells |
| VKI LS89 | [Alauzet et al. (2022)](/sources/alauzet-2022.md), §8.1 | several exit pressure ratios | steady RANS with the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md) on adapted tetrahedral meshes |
| Transonic HPT rotor cascade with flat-tip clearance $0.07c$ (SNECMA profile, experiment of Arts et al.) | [Yang & Ma (2022)](/sources/yang-2022-b.md), §2.2–2.3 | $M_{2,is}=0.95$, inlet total pressure 183 kPa and temperature 380 K, outlet static pressure 101 kPa, inlet $Tu=5\%$, zero incidence; Reynolds number not printed | SST-based DES with the $F_2$ shielding of ANSYS CFX ($C_{DES}=0.61$), about $1.3\times10^7$ hexahedra, $y^+\approx1$; URANS with SST and $k$-$\omega$ for comparison |

## What the case tests

**Separated-flow transition on high-lift LPT blades.** On T106C at an exit
Reynolds number of $8\times10^4$, the implicit LES of
[Wang (2024)](/sources/wang-2024-b.md) (read in arXiv v2) gives an
$M_{is}$ distribution in "excellent agreement" with the experiment of
Michálek et al. and with the CPR $N=3$ results of Alhawwary & Wang, with
HLLC or Roe fluxes and with negligible effect of the local modal filter;
mean $y^+\approx0.5$, $x^+\approx20$, $z^+\approx6$, averaged over five
convective times (§4.2, Table 4, Figs. 6–8). The RANS of
[Pacciani et al. (2025)](/sources/pacciani-2025.md) at the same
$Re_{2,is}=0.8\times10^5$ predicts the measured open separation but a too
early transition and a smaller separated region, hence a narrower wake and
an underestimated integral loss, which the authors call satisfactory for 2D
RANS given the three-dimensional secondary flows that LES shows; at 1.2 and
$1.6\times10^5$ the bubbles close and the agreement improves (§6.2,
Figs. 18–20). On T108 the bubbles are short at all three Reynolds numbers,
with $M_{is}$, wake loss and its Reynolds-number lapse rate well matched
but a post-reattachment wall shear stress below the measurement (§6.2,
Figs. 21–23).

**Scheme dissipation and leading-edge separation on T106A.**
[Ma et al. (2022)](/sources/ma-2022.md), §3.3, run the T106A cascade at
$Re\approx6\times10^4$ as [implicit LES](/definitions/implicit-les.md)
with three variants of a weighted compact nonlinear finite-difference
scheme: the original explicit fifth-order nonlinear interpolation
(WCNS-E), the same with its weights frozen at the linear ones
(WCNS-E(linear)), and the authors' seventh-order nonlinear tri-diagonal
compact interpolation (WCNS-T; see [WENO schemes](/methods/weno-scheme.md)).
Against the experiment of Stieger and the DNS of Michelassi et al.:

- the WCNS-T wall pressure coefficient is "reasonably better" than that of
  WCNS-E, with differences remaining on the front half of the suction side
  (Fig. 11);
- the early separation near the leading edge is not captured by nonlinear
  WCNS-E, whereas WCNS-E(linear) gives a qualitatively correct behaviour,
  so the nonlinear weighting of the explicit interpolation itself degrades
  the prediction (Fig. 12); see
  [numerical dissipation](/properties/numerical-dissipation.md);
- both schemes capture transition, with finer vortical structures for
  WCNS-T, especially far downstream (Fig. 13).

The comparisons are graphical; no loss or separation length is printed.

**Wall-resolved LES as reference for RANS.**
[Morsbach et al. (2024)](/sources/morsbach-2024.md) compute T161 with
turbulent end-wall boundary layers generated synthetically (see
[inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
The LES matches the measured blade loading, including the plateau of the
separation bubble between $x/c_{ax}=0.7$ and 0.9 ($c_{ax}$ the axial
chord, registry §11), the midspan wake loss within the confidence intervals, and the
secondary loss cores (§4.1–4.2, Figs. 7, 9–10). Both RANS models miss the
bubble and underestimate the midspan mixed-out loss by 35% (SST) and 29%
(SSG/LRR-ω, see [Reynolds-stress model](/methods/reynolds-stress-model.md)),
and overpredict the peak secondary loss by 34% and 48%; a reduced inflow
length scale, "common practice", brings the SST midspan loss within 2.7%
through "a lucky cancellation of errors" with an open separation (§4.1–4.2,
Figs. 8–10). The authors suggest tuned transition or laminar-kinetic-energy
models for the midspan transition (§5).

**Bypass transition and heat transfer on the transonic vane.** On LS89,
[Pacciani et al. (2025)](/sources/pacciani-2025.md), §6.1, Figs. 15–16,
tune the inlet length scale to the leading-edge heat transfer and then
predict the suction-side onset reasonably to very well at both Reynolds
numbers, with pressure-side transition at $Tu=6\%$ and high Reynolds number
as measured; the shock, impinging at $x/c_{ax}=0.83$, fixes transition
only at low $Tu$ (Mur247). Transition develops too quickly, "as in most RANS
results in the literature". [Wang (2024)](/sources/wang-2024-b.md), §4.3,
Figs. 13–17, finds that $M_{is}$ is insensitive to resolution and, after
Arts, already predicted reasonably by an inviscid 2D computation, so it is
"insufficient to validate a solver" on LS89; all set-ups place transition
well, and the HTC in the turbulent region improves from $N=2$ to $N=3$ and
with spanwise refinement, a spanwise spacing $z^+\approx45$–60 being
sufficient for the mean HTC. The HTC depends more on the filter threshold
than on the Riemann solver; HLLC is more robust than Roe; the entropy filter
of Dzanic & Witherden stabilizes without tuning but is more dissipative at
high frequencies and about 15% more expensive per iteration than the local
modal filter (§4.3.2, §4.4.3; see
[subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)
and [numerical dissipation](/properties/numerical-dissipation.md)).
[Alauzet et al. (2022)](/sources/alauzet-2022.md), §8.1, use LS89 for
[mesh adaptation](/methods/mesh-adaptation.md): the adapted solutions
converge to the same functionals whatever the initial mesh and error
estimate, except at the lowest pressure ratio, where the feature-based and
goal-oriented approaches give different answers (§8.1.3, Fig. 18).

**Correlation-based transition on Pak-B.** As reported on
[local-correlation-based transition models](/methods/local-correlation-based-transition-model.md),
[Menter et al. (2022)](/sources/menter-2022.md) find that all three models
reproduce the bubble-size trends; γ-alg-SST is on the small-bubble side at
$Re=5\times10^4$, $Tu=0.08\%$, and γ-SST over-predicts the bubble at
$Re=5\times10^4$, $Tu=2.85\%$ (Fig. 24).

**Tip-leakage vortex in a transonic turbine rotor cascade.**
[Yang & Ma (2022)](/sources/yang-2022-b.md) compute one passage of the
cascade of Arts et al. (chord $c=71.8$ mm, blade height 100 mm, solidity
1.315, inlet and exit flow angles $53.36^\circ$ and $-65^\circ$, a tip gap of
$0.07c$, about 5% of the span) with a
[detached-eddy simulation](/methods/detached-eddy-simulation.md) on the
[$k$-$\omega$ SST model](/methods/k-omega-sst-model.md); the paper calls the
simulation "DES", "DES-type" and "DDES". The convective flux blends
central and upwind differences; the authors take the blending factor near
zero along the vortex and the wake, and a $-5/3$ range in velocity spectra
at monitor points, as evidence of resolution, instead of a grid study
(§3.1, Figs. 4–5). The only experimental comparison is the mid-span
isentropic Mach number, which DES and URANS reproduce comparably except
near the suction-side shock (Fig. 6). Against URANS the DES gives more
small-scale structures near the tip, a longer-lived wake vortex layer and
sharper shocks, and URANS over-predicts the Reynolds shear stress along
the vortex (§3.2, Figs. 7–9). The vortex starts near $0.2c$, keeps a
supersonic core, wanders with one characteristic frequency of about
2200 Hz inside the passage, and breaks down near the trailing edge behind
the shock in a "spiral-type" breakdown that the authors describe as found
for the first time in a transonic turbine (§4.1, Figs. 10–11). Along the
vortex the turbulent kinetic energy and the Reynolds stresses are nearly
zero upstream of $z/c=0.8$ and rise sharply through the shocks near the
trailing edge; an anisotropy map of the vortex core moves from
one-component through two-component states to near isotropy downstream of
the trailing edge (§4.5–4.6, Figs. 18–19). All results come from one grid,
with statistics over 0.002 s after 0.004 s of settling (§3.1). Unlike the
other cascades of this page, no transition or loss is assessed. Tip
leakage in a compressor appears on [NASA Rotor 37](/benchmarks/nasa-rotor-37.md).

**What turbine blade rows demand of models (review).**
[Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) review DNS and
LES of turbine cascades and stages for what they reveal about RANS
failures. The studies below are the authors' own or others' as the review
cites them.

- *Loading.* High-lift LPT profiles carry stronger pressure gradients,
  measured by the Zweifel coefficient: 1.15 for Pack B and 1.59 for L2F
  (Fig. 3b, after McQuilling 2007). In strongly favourable gradients a
  boundary layer is "likely to eventually relaminarize" once the acceleration parameter
  $K_{\mathrm{acc}}=(\nu/U_e^2)\,dU_e/ds$ exceeds $3.5\times10^{-6}$ ($U_e$ the edge
  velocity, $s$ the surface coordinate, page-local; §3.3.1, Eq. 1).
- *Inflow turbulence and heat transfer on HPT vanes.* In LES of an HPT
  vane at the isentropic Reynolds number (page-local, as printed)
  $Re_{is}=5.7\times10^5$ with inflow turbulence intensities of
  6–20% and length scales of 5–20% of the chord, larger length scales give
  an earlier rise and a higher overall heat transfer on both sides
  (Pichler et al. 2017b; §3.2.1, Fig. 4a). In DNS/LES of an HPT vane at the
  same $Re_{is}$ (Zhao & Sandberg 2020a), low intensity (6.5%, length scale 4.8% of the
  axial chord) gives leading-edge streaks whose spanwise spacing follows
  the inflow length scale and that break down through the sinuous mode in
  the favourable and the varicose mode in the adverse gradient. High
  intensity with a large length scale (20%, 20.1%) gives earlier
  transition through breakdown of vortical structures without an obvious
  streak instability (§3.3.3.2, Fig. 5).
- *Where RANS loses accuracy on LS89.* An entropy-loss analysis of LES and
  RANS of the VKI LS89 vane (Zhao & Sandberg 2020c) confines mean-flow
  entropy generation to the suction-side boundary layer. It finds the
  largest contribution in turbulence production in the near wake, where
  RANS departs most from the high-fidelity data. This points to near-wake
  production as the main cause of wrong RANS total loss (§4.2).
- *Transonic trailing edges.* LES attributes the additional loss of a
  transonic HPT vane to the interaction of the shock with the
  trailing-edge vortex shedding just downstream of the trailing edge, not
  to the passage shock itself (Zhao & Sandberg 2020b; §3.2.2).
- *Incoming wakes on LPT blades.* In LES of an LPT stage at
  $Re_{is}=10^5$ (Pichler et al. 2017a), once the wake apex passes the
  separation point the separation and reattachment points move downstream
  at about one half and one quarter of the local isentropic velocity, and
  the bubble is absent for about 25% of the time (§3.3.3.4, Fig. 6; see
  [laminar separation bubble](/definitions/laminar-separation-bubble.md)).
  Unsteady losses from wake distortion do not grow monotonically with the
  reduced frequency, because at high frequency the wakes merge before
  entering the passage, "fogging" (§3.2.2).
- *Consequences for RANS.* The
  [$\gamma$-$Re_\theta$ model](/methods/local-correlation-based-transition-model.md)
  suppresses wake-induced transition, since the low $Re_\theta$ of the
  incoming wakes is not fed into the blade boundary layers (§3.3.3.4). The
  [laminar kinetic energy model](/methods/laminar-kinetic-energy-transition-model.md)
  of Pacciani et al. (2014) was built so that no laminar kinetic energy
  forms on the wake-induced path (§3.3.3). Acceleration and turning in the
  passage misalign the Reynolds stress and the strain rate in wake cores,
  which invalidates the linear
  [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)
  (§3.2.3). URANS double-counts the trailing-edge shedding, once resolved
  and once in the closure; a gene-expression-programming closure trained
  on the stochastic part of a triple decomposition of wake LES data (Lav et
  al. 2019) improves the near and far wake (§3.2.3). Reynolds averaging
  needs a spectral gap between the deterministic (rotor–stator, shedding)
  frequencies and the turbulence, and the authors state that without it
  "any model based on Reynolds averaging will fail" (§3.1.2, Fig. 1).
- *Data-driven closures trained on LPT data.* Gene-expression-programming
  models of the explicit algebraic stress trained on single phases of
  phase-locked LPT data perform well on the training phase and can perform
  poorly on others; two distinct models suffice across all phases (Akolekar
  et al. 2019; §4.3, Eq. 2, Fig. 7). CFD-driven training on HPT data
  predicted LPT wake-loss profiles for other geometries and Reynolds
  numbers (Zhao et al. 2020). Field inversion with a neural network on the
  Spalart–Allmaras model in a low-Reynolds-number LPT cascade reached an a
  posteriori accuracy similar to that of a costlier two-equation model with
  $\gamma$-$Re_\theta$ transition (Ferrero et al. 2020; §4.3). See
  [symbolic-regression closures](/methods/symbolic-regression-closure.md)
  and [field inversion](/methods/field-inversion-machine-learning.md).

**Machine-learnt closures for turbine wakes (second review).**
[Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md), a review of
machine-learnt stress and heat-flux closures from the same group, report
the turbine studies with further detail; as above, every result is cited
from the works the review names.

- *Steady wake mixing.* CFD-driven gene-expression programming, in which
  each candidate closure is run in the RANS solver during training, gave
  simpler models than training on frozen high-fidelity data and improved
  the wake profiles in all a posteriori tests on other high- and
  low-pressure-turbine geometries; the improvement came "predominantly"
  from increased diffusion (§4.1; see
  [model-consistent training](/methods/model-consistent-training.md)).
- *Phase-locked training with incoming wakes.* On LPT DNS with 20 phases
  per wake-passing cycle (Akolekar et al. 2019), models trained on one
  phase work on that phase and on some others (trained on phase 13, they
  work on phase 5) but fail on others (trained on phase 10, they fail on
  phase 18); the linear coefficient and the non-linear contribution follow
  the wake–wake interaction, so two models trained on two representative
  phases suffice (§4.4.1, Fig. 10), in agreement with the summary of
  [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) above.
- *No spectral gap.* When the deterministic unsteadiness overlaps the
  turbulence spectrum (see [spectral gap](/definitions/spectral-gap.md)),
  a triple decomposition into mean, deterministic and stochastic parts is
  used instead; the stochastic anisotropy was insensitive to the
  decomposition used (Fourier, POD or DMD), and the closure trained on it
  sharply reduces the modelled diffusion, so that URANS resolves more
  scales and improves the near and far wake (Lav et al. 2019; §4.4.2).
- *Transition.* CFD-driven multi-expression training of corrections to a
  [laminar kinetic energy model](/methods/laminar-kinetic-energy-transition-model.md)
  for LPTs is listed among the data-driven transition models, which the
  authors call "still far from mature" (§4.3).

The two findings concern different contexts: added diffusion improves
steady RANS wake mixing (§4.1), while reduced modelled diffusion improves
URANS once the deterministic part is resolved (§4.4.2). The closure forms are on
[explicit algebraic Reynolds-stress models](/methods/explicit-algebraic-reynolds-stress-model.md)
and [symbolic-regression closures](/methods/symbolic-regression-closure.md).

**Adaptive implicit LES on T106c and T106a.**
[Ims & Wang (2023)](/sources/ims-2023.md) use the two HiOCFD cascades to
compare three cell-wise error indicators that drive isotropic
h-refinement of an implicit LES at fixed polynomial degree: the unsteady
residual evaluated at degree $N+1$, the Persson–Peraire smoothness
indicator and a curvilinear variant of the Toosi–Larsson small-scale-energy
indicator (see [mesh adaptation](/methods/mesh-adaptation.md)). Each round
marks the 20% of cells with the largest time-averaged indicator, plus the
cells forced by size and clumping constraints (§4). Evidence is visual: entropy snapshots,
maps of the marked cells, the $uv$ Reynolds-stress field and spectra of the
turbulent kinetic energy at a wake monitor point; no error norm, cell count
or cost is printed.

- On T106c all three indicators improve vortex resolution and refine
  roughly the same regions, near the blade surface and in the active wake,
  and none refines much at the leading edge, "possibly", the authors
  write, because the laminar flow there is already resolved (§5.1,
  Figs. 5–12). The smoothness
  indicator favours small boundary-layer cells on both surfaces, the
  small-scale-energy indicator large wake cells (once even at the domain
  exit), the residual indicator lies between (§5.1). Indicators also
  refine along the edge of the suction-side separation bubble into the
  wake ([laminar separation bubble](/definitions/laminar-separation-bubble.md)).
- Against the DNS, the $uv$ field and the high-frequency part of the
  wake spectrum converge fastest with the small-scale-energy and residual
  indicators, "nearly in lockstep", the former slightly ahead; the
  smoothness indicator lags at both refinements; the low-frequency peaks
  are already aligned on the base mesh (§5.1, Figs. 13–16).
- T106a, with a coarser start mesh, $N=1$ and unresolved laminar flow, is
  "less challenging for the flow solver but more challenging for the error
  indicators"; the ranking is the same (§5.2, Figs. 18–30). Random
  refinement with the same budget improves the solution "at a pace almost
  equal to" the smoothness indicator, does not disturb the flow at the
  random hanging-node boundaries, and moves the low-frequency peaks toward
  the reference faster than the two vortex-sensitive indicators, which the
  authors read as those indicators de-emphasizing the laminar flow (§5.2.1,
  Figs. 31–34).

The T106c DNS reference of Ims & Wang is the hpMusic DNS of Alhawwary &
Wang (their ref. [26]); [Wang (2024)](/sources/wang-2024-b.md) compares its
T106C implicit LES with the CPR $N=3$ results of Alhawwary & Wang and with
the experiment of Michálek et al. (§4.2, Table 4, Fig. 8).

**What the sources share.** Steady RANS with transition models captures
the onset of separated-flow and bypass transition on these blades but not
its extent: transition develops too quickly on LS89 and sets in too early
on T106C at $Re_{2,is}=0.8\times10^5$
([Pacciani et al. (2025)](/sources/pacciani-2025.md)), and the T161 bubble
is missed with γ-$Re_\theta$ ([Morsbach et al. (2024)](/sources/morsbach-2024.md)).
Both implicit LES ([Morsbach et al. (2024)](/sources/morsbach-2024.md),
[Wang (2024)](/sources/wang-2024-b.md)) reach the measured blade loading
with no explicit SGS model; see [implicit LES](/definitions/implicit-les.md)
and [grid-point requirements](/results/les-grid-point-requirements.md).

## Qualifications

- On T106C [Wang (2024)](/sources/wang-2024-b.md) imposes no free-stream
  turbulence, while [Pacciani et al. (2025)](/sources/pacciani-2025.md)
  impose $Tu=0.8\%$ and a length scale of $2.5\times10^{-3}$ axial chords;
  the two runs do not share an inflow, and their comparisons with
  experiment rest on different quantities ($M_{is}$ against $M_{is}$, wake
  loss and lapse rate).
- The LS89 runs of [Wang (2024)](/sources/wang-2024-b.md) (MUR129, no inlet
  turbulence against 0.8% measured) and of
  [Pacciani et al. (2025)](/sources/pacciani-2025.md) (Mur224–Mur247 at 1%
  and 6%) are different operating points. Pacciani et al. tune the inlet
  length scale per case to the leading-edge heat transfer.
- [Pacciani et al. (2025)](/sources/pacciani-2025.md) cite Fig. 14(a) for a
  Mach-contour plot of Mur224 whose caption places it in panel (b) for
  Mur239, and assign Mur239–Mur247 to Fig. 15(a) where the caption puts
  them in (b).
- [Wang (2024)](/sources/wang-2024-b.md) summarizes the filter-threshold
  range as $[-(N+2),-(N+1)]$ in the conclusions while Table 2b gives
  $[-3.7,-2.7]$ for $N=2$ and $[-5.3,-4.3]$ for $N=3$; the ranges overlap
  but differ *(compiler check, not in the sources)*. The paper attributes
  the entropy filter to ref. [31], while the entropy-filter paper of Dzanic
  & Witherden in its list is ref. [42].
- [Yang & Ma (2022)](/sources/yang-2022-b.md) call the blade row a
  "transonic turbine cascade" (high-pressure turbine rotor profile), not a
  compressor; their $x$ is spanwise and $z$ axial. Their grid of
  $169\times155\times404$ points is about $1.06\times10^7$, against "about 13
  million" cells printed *(compiler check, not in the sources)*; the text
  does not give the size of the 69-layer tip-gap block. The vorticity-transport section
  (§4.2) finds the stretching–tilting term dominant and then closes with
  "the viscous diffusion effect dominates"; the abstract sides with the
  first. The anisotropy map is attributed to "Lumley et al. [31]", while
  reference [31] is Strelets' DES paper.
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) is a review
  without computations of its own: every result in its paragraph above is
  cited from the works it names, with figures reproduced from them. It
  prints its Reynolds numbers as $Re_{is}$ without saying whether they are
  the exit values $Re_{2,is}$ used elsewhere on this page; the review writes the acceleration parameter in terms
  of the isentropic Mach number without stating the reference length of
  its $Re$ (Eq. 1).
- [Ma et al. (2022)](/sources/ma-2022.md) print neither the Mach number nor
  the inflow turbulence of their T106A run, and "about 12 million" points
  without the grid dimensions; the T106A profile differs from the T106C
  of Wang (2024) and Pacciani et al. (2025).
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) print 67.9 million
  degrees of freedom for the coarse mesh, whose element count and $N=5$
  give 67.5 million *(compiler check, not in the sources)*.

- [Ims & Wang (2023)](/sources/ims-2023.md) count their adaptation rounds
  differently in text and captions: §5.1 describes two refinements and a
  third marking "as reference only", the Fig. 9 caption speaks of rounds
  #1–#3, and in §5.2 Figs. 19 and 20 show the T106a wake "after the third
  refinement" while the Fig. 21 caption says "after the second
  refinement". Their T106a blade angle (46.1°) differs slightly from the
  workshop's, as they state, and the $uv$ stress is plotted without its
  sign or normalization.

# Citations

- [Wang (2024)](/sources/wang-2024-b.md) — §2.3–2.4; §4.2, Tables 3–4, Figs. 6–8; §4.3, Tables 5–8, Figs. 12–17; §4.4, Figs. 18–21; §5.
- [Pacciani et al. (2025)](/sources/pacciani-2025.md) — §6.1, Table 4, Figs. 14–16; §6.2, Table 5, Figs. 18–23; §7.
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §3.1–3.3, Tables 1–2; §4.1–4.2, Figs. 7–15; §5.
- [Menter et al. (2022)](/sources/menter-2022.md) — Pak-B cascade, Fig. 24.
- [Alauzet et al. (2022)](/sources/alauzet-2022.md) — §8.1.2–8.1.3, Figs. 17–18.
- [Yang & Ma (2022)](/sources/yang-2022-b.md) — §1; §2.1–2.3, Eqs. 1–6; §3.1–3.2, Figs. 4–9; §4.1–4.6, Figs. 10–19; §5.
- [Ma et al. (2022)](/sources/ma-2022.md) — §3.3, Figs. 10–13 (T106A implicit LES).
- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) — review: §2.5, Fig. 8; §4.1; §4.3; §4.4.1–4.4.2, Fig. 10.
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — review: §3.1.2, Fig. 1 (spectral gap); §3.2.1–3.2.3, Fig. 4 (inflow turbulence, wakes, shedding, Boussinesq misalignment); §3.3.1, Eq. 1; §3.3.3, Figs. 5–6 (bypass and wake-induced transition); §4.2 (entropy loss on LS89); §4.3, Eq. 2, Fig. 7 (data-driven closures).
- [Ims & Wang (2023)](/sources/ims-2023.md) — §3–§4 (indicators, marking, constraints); §5.1, Figs. 5–16 (T106c); §5.2, Figs. 18–30 (T106a); §5.2.1, Figs. 31–34 (random refinement); §5.3, §6.

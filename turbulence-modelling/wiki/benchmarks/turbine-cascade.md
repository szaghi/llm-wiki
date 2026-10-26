---
type: Benchmark
title: "Turbine cascades (T106, T161, VKI LS89)"
description: "Linear turbine cascades as transition and loss benchmarks: the high-lift low-pressure T106C, T108 and T161 cascades with laminar separation at exit Reynolds numbers near 10⁵, and the transonic VKI LS89 vane with bypass transition and heat transfer, run by implicit DG and flux-reconstruction LES and by RANS transition models."
status: established
aliases: [turbine cascade, linear turbine cascade, LPT cascade, T106C, T106c, T108, T161, MTU T161, VKI LS89, LS89 vane, Pak-B cascade]
tags: [benchmark, turbomachinery, transition, implicit-les, rans, boundary-layer]
timestamp: 2026-10-26T10:26:00Z
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
discriminating quantity. The quantities compared are the isentropic Mach
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
| T108 (front-loaded LPT) | [Pacciani et al. (2025)](/sources/pacciani-2025.md), §6.2 | as T106C, pitch/chord 1.1 | as above |
| T161 (high-lift LPT between diverging end walls) | [Morsbach et al. (2024)](/sources/morsbach-2024.md), §3.1–3.2, Tables 1–2 | $Re_{2,is}=9\times10^4$, $M_{2,is}=0.6$, inflow angle 41°, synthetic turbulent end-wall layers and free-stream turbulence | implicit LES, [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) $N=5$ with kinetic-energy-preserving split form, $1.89\times10^8$ degrees of freedom; RANS with SST and SSG/LRR-ω plus γ-$Re_\theta$ |
| Pak-B (LPT) | [Menter et al. (2022)](/sources/menter-2022.md), Fig. 24 | $Re=5\times10^4$ to $1.72\times10^5$ on inlet velocity and axial chord, $Tu=0.08\%$ to 4% | RANS with three [local-correlation transition models](/methods/local-correlation-based-transition-model.md) |
| VKI LS89 (transonic HPT vane) | [Wang (2024)](/sources/wang-2024-b.md), §4.3, Tables 5–6 | MUR129: exit $Re=1.13\times10^6$, no free-stream turbulence in the computation (0.8% measured), wall temperature 297.75 K | implicit LES, $N=2$ and 3, 10 to 20 spanwise layers, $6.6\times10^6$ to $31.3\times10^6$ degrees of freedom |
| VKI LS89 | [Pacciani et al. (2025)](/sources/pacciani-2025.md), §6.1, Table 4 | Mur224, Mur228 ($Re_{2,is}\approx6\times10^5$), Mur239, Mur247 ($\approx2.1\times10^6$), $M_{2,is}\approx0.92$–0.93, $Tu=6\%$ and 1% | steady 2D RANS, laminar kinetic energy model, $3\times10^5$ cells |
| VKI LS89 | [Alauzet et al. (2022)](/sources/alauzet-2022.md), §8.1 | several exit pressure ratios | steady RANS with the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md) on adapted tetrahedral meshes |

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

**Wall-resolved LES as reference for RANS.**
[Morsbach et al. (2024)](/sources/morsbach-2024.md) compute T161 with
turbulent end-wall boundary layers generated synthetically (see
[inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
The LES matches the measured blade loading, including the plateau of the
separation bubble between $x/C_{ax}=0.7$ and 0.9 (page-local: axial chord
$C_{ax}$), the midspan wake loss within the confidence intervals, and the
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
as measured; the shock, impinging at $x/C_{ax}=0.83$, fixes transition
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
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) print 67.9 million
  degrees of freedom for the coarse mesh, whose element count and $N=5$
  give 67.5 million *(compiler check, not in the sources)*.

# Citations

- [Wang (2024)](/sources/wang-2024-b.md) — §2.3–2.4; §4.2, Tables 3–4, Figs. 6–8; §4.3, Tables 5–8, Figs. 12–17; §4.4, Figs. 18–21; §5.
- [Pacciani et al. (2025)](/sources/pacciani-2025.md) — §6.1, Table 4, Figs. 14–16; §6.2, Table 5, Figs. 18–23; §7.
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §3.1–3.3, Tables 1–2; §4.1–4.2, Figs. 7–15; §5.
- [Menter et al. (2022)](/sources/menter-2022.md) — Pak-B cascade, Fig. 24.
- [Alauzet et al. (2022)](/sources/alauzet-2022.md) — §8.1.2–8.1.3, Figs. 17–18.

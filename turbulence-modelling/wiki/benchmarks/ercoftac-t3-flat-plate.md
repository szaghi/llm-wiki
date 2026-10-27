---
type: Benchmark
title: "ERCOFTAC T3 flat-plate transition cases"
description: "The ERCOFTAC T3 series of flat-plate boundary layers under free-stream turbulence, at zero (T3A, T3B, T3A-) and variable pressure gradient (T3C1–T3C5): the calibration and validation case of RANS transition models, also in high-order discretizations, where onset is predicted well at zero pressure gradient and tends to be delayed in adverse pressure gradient without a correction."
status: established
aliases: [T3 flat plates, ERCOFTAC T3A, T3A, T3B, T3A-, T3C, T3C1–T3C5, Rolls-Royce T3 plates, Savill T3 test cases]
tags: [benchmark, transition, rans, boundary-layer, flux-reconstruction, dg]
timestamp: 2026-10-27T06:13:00Z
---

# ERCOFTAC T3 flat-plate transition cases

The T3 cases are flat-plate boundary layers developing under grid-generated
free-stream turbulence, measured for the ERCOFTAC data base (credited by
the sources to Savill, to Pironneau et al., and to the ERCOFTAC Data Base).
The inlet velocity, turbulence intensity $Tu$ and free-stream decay vary
from case to case, so transition moves along the plate. **T3A, T3B and
T3A-** have zero pressure gradient and bypass transition at
$Tu\approx3$–$7\%$ and about 1%; **T3C1–T3C5** have the variable pressure
gradient of an aft-loaded turbine blade, prescribed through the shape of
the upper wall, with favourable (T3C1, T3C5) and adverse (T3C2–T3C4)
gradients at onset; T3C4 transitions through a laminar separation. The
quantity compared is the skin-friction coefficient $C_f$ along the plate,
whose minimum marks the transition onset, plotted against the
plate Reynolds number $Re_x$ (page-local: $U_\infty x/\nu$). In this bundle
the series calibrates and validates
[local-correlation-based transition models](/methods/local-correlation-based-transition-model.md),
[laminar kinetic energy models](/methods/laminar-kinetic-energy-transition-model.md)
and an intermittency-coupled
[Reynolds-stress model](/methods/reynolds-stress-model.md), and it
verifies transition models in high-order
[flux reconstruction](/methods/flux-reconstruction.md) and modal
discontinuous Galerkin solvers. The
transition-model intermittency $\gamma$ and $Tu$ follow the registry
(transition pages only).

## Inlet conditions in the sources

Every source tunes the inlet $Tu$ and eddy-viscosity ratio so that the
computed free-stream turbulence decay matches the measured one, and the
printed inlet values therefore differ between sources
([Menter et al. (2022)](/sources/menter-2022.md), Table 2;
[Liu et al. (2024)](/sources/liu-2024.md), Table 2, Figs. 3–4;
[Pacciani et al. (2025)](/sources/pacciani-2025.md), Table 1):

| Case | pressure gradient | Menter et al. (2022): $U_0$ [m/s], $Tu$ [%], $\nu_t/\nu$ | Liu et al. (2024) | Pacciani et al. (2025) |
|---|---|---|---|---|
| T3A | zero | 5.40, 3.30, 12.0 | 5.2, 3.5, 11.5 | 5.4, 3.3, 11.5 |
| T3B | zero | 9.40, 6.50, 80.0 | 9.4, 6.5, 90 | 9.2, 6.2, 60.0 |
| T3A- | zero | 19.80, 0.90, 8.0 | 19.8, 0.9, 8 | 19.8, 0.874, 5.2 |
| T3C1 | favourable | — | 5.9, 7.78, 60 | 6.4, 8.0, 54.0 |
| T3C2 | adverse | 5.29, 3.00, 8.0 | 5, 4, 9 | 5.5, 2.8, 9.0 |
| T3C3 | adverse | 4.00, 3.00, 5.0 | 3.7, 4, 6 | 4.1, 3.0, 7.0 |
| T3C4 | adverse, separated | 1.37, 3.00, 2.0 | 1.2, 3.5, 2.5 | 1.3, 2.9, 2.5 |
| T3C5 | favourable | 9.00, 3.00, 15.0 | 8.4, 3.7, 15 | 9.2, 3.5, 18.0 |

Grids are two-dimensional and wall-resolved: $231\times148$ (zero
pressure gradient) and $257\times129$ (T3C) cells with first-cell height
$2\times10^{-5}$ m and mean $y^+$ from 0.02 to 0.35 in
[Menter et al. (2022)](/sources/menter-2022.md), Table 3, with the upper
boundary of the T3C cases a prescribed experimental streamline; the level
F ($365\times193$, $y^+<0.4$) of a five-level study in
[Liu et al. (2024)](/sources/liu-2024.md), Table 3, with onset insensitive
from the "upper-medium" level on; and a single-block H mesh of $288\times128$ cells
without the plate leading edge in
[Pacciani et al. (2025)](/sources/pacciani-2025.md), §5.1, whose grid
study on T3A- ($165\times65$, $289\times129$, $541\times221$) finds the
medium and fine grids coincident (Table 3). Menter et al. include the
plate leading edge (radius 0.75 mm, plate length 1.5 m).

Two high-order sources print their own settings
([Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md), §4.2, Table 3;
[Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md), §IV A, Tables II–III):

| Case | Vandenhoeck et al. (2022): $U_\infty$ [m/s], $Tu$ [%], $\nu_t/\nu$ | Ghidoni & Noventa (2026): $Re_\infty\times10^{-5}$, $Tu$ [%], $\nu_t/\nu$ |
|---|---|---|
| T3A | 5.4, 3.5, 13.3 | 6.12, 3.3, 12 |
| T3B | 9.4, 6.5, 100.0 | 10.52, 6.5, 95 |
| T3A- | 19.8, 0.874, 8.72 | 22.25, 0.48, 8.72 |
| T3C2 | — | 5.61, 3.0, 11 |
| T3C3 | — | 4.15, 3.0, 6 |
| T3C4 | — | 1.35, 3.0, 8 |
| T3C5 | — | 9.42, 4.0, 5 |

Vandenhoeck et al. run [flux reconstruction](/methods/flux-reconstruction.md)
in [COOLFluiD](/software/coolfluid.md) on a mesh of only 143
quadrilaterals (10 on the plate, 11 wall-normal, 3 upstream), first-element
$y^+\simeq3$ (T3A), 7 (T3B) and 10 (T3A-), at polynomial degrees 0 to 5
(6 for T3A). Ghidoni & Noventa ($Re_\infty$ page-local: free-stream
Reynolds number on the plate length $L$) run a modal DG solver at degree 4 on 4000
elements ($100\times40$, $y_1^+=1$), with 2000- and 8000-element meshes
for T3A; their domain spans $-0.2<x/L<1$ with a symmetry plane ahead of
the plate, and the upper-wall height is fitted to reproduce the measured
pressure gradient, by sixth-degree polynomials for T3C. They set the T3A-
intensity to 0.48% rather than the measured 0.9% because, with 0.9%, the
onset correlations they compare disagree by 137.62% (Coupland against
Abu-Ghannam & Shaw), against 1.39% with 0.48%, a choice they credit to
earlier authors (§IV A, Fig. 6).

The Schubauer–Klebanoff plate (natural transition at very low $Tu$) is
run with the series by [Menter et al. (2022)](/sources/menter-2022.md)
($U_0=50.10$ m/s, $Tu=0.03\%$, $\nu_t/\nu=1.0$; Table 2) and by
[Pacciani et al. (2025)](/sources/pacciani-2025.md) ("T3A-SK",
$U_{in}=50.1$ m/s, $Tu=0.3\%$, $\nu_t/\nu=1.2$; Table 1), and by
[Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md) with the five
Schubauer–Skramstad plates ($Re_\infty=59.35\times10^5$, $\nu_t/\nu=1$,
$Tu=0.3\%$ for the Schubauer–Klebanoff plate and 0.1–0.34% for the
others).

## What the case tests

**Bypass onset at zero pressure gradient.** All three sources report
onset in agreement with experiment on T3A and T3B:
the algebraic γ-alg-SST model agrees with the transport models and the
experiment ([Menter et al. (2022)](/sources/menter-2022.md), Fig. 8); the
SSG/LRR-ω-γ Reynolds-stress model agrees well on T3A, T3B and T3A-
([Liu et al. (2024)](/sources/liu-2024.md), Fig. 6a–c); the revised
laminar-kinetic-energy model is calibrated on T3A to $c_1=0.02$, $c_5=24$
([Pacciani et al. (2025)](/sources/pacciani-2025.md), §5.1.1, Figs. 2–3).
T3A also exposes coupling defects: without its sublayer limiter the
algebraic model underpredicts $C_f$ after transition and departs from the
log law ([Menter et al. (2022)](/sources/menter-2022.md), §2.2, Fig. 1);
with the original coupling through the Wilcox low-Reynolds damping, the
laminar-kinetic-energy model gives an "erratic" $C_f$, a series of
re-laminarizations and re-transitions
([Pacciani et al. (2025)](/sources/pacciani-2025.md), §4.2, Fig. 1).
Downstream of transition the skin friction of SSG/LRR-ω-γ is typically
higher than that of the fully turbulent SST and SSG/LRR-ω models, which
give similar accuracy on these single-shear flows
([Liu et al. (2024)](/sources/liu-2024.md), Fig. 6).

**Transition models in high-order discretizations.**
[Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md), §4.2, verify the
Langtry–Menter model, written with $\ln\omega$ as the transported variable
of [$k$-$\omega$ SST](/methods/k-omega-sst-model.md), in flux
reconstruction: the lowest degrees are inadequate (degree 0 shows no
transition), higher degrees approach the experiment and the two highest
coincide; on T3A and T3A- the result is very close to the finite-volume
solution of Langtry and Menter that they cite, obtained on about 39,000
elements with a rounded leading edge, and on T3B it is "remarkably closer"
to the experiment, which they attribute "most likely" to the accuracy of
the scheme (Figs. 12–13). The $C_f$ at degree 5 on T3A is nearly identical
for three correction-function parameters (Fig. 14). At degree 5 the
$u^+$ profiles agree with experiment; $k^+$ under-predicts the measured
near-wall values and the model does not reproduce the measured
transitional maximum of $k^+$, which the authors attribute to the
Langtry–Menter model itself (Figs. 15–16). They also use T3A at degrees 2
and 4 to compare source-term Jacobians of their implicit solver: without
one, the CFL limit had to drop from 1250 to 500 (§3.2.3, Figs. 6–7).
[Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md), §IV A, Fig. 7,
find their $C_f$ error on T3A converged in degree and mesh: 3.89%, 3.46%,
3.39% and 3.38% for degrees 1–4 on 4000 elements, 3.38% at degree 4 on
8000.

**A momentum-thickness threshold in a laminar-kinetic-energy model.**
[Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md) replace the
transfer-term thresholds of the Walters–Cokljat
[laminar kinetic energy model](/methods/laminar-kinetic-energy-transition-model.md)
by a comparison of a local momentum-thickness Reynolds number with the
Langtry–Menter onset correlations. Their errors on the series, as mean
absolute $C_f$ deviation over the mean measured $C_f$ (§IV A, Figs. 4–8):

| Case | $C_f$ error | onset error |
|---|---|---|
| T3A | 3.38% | 8.22% |
| T3B | 15.81% | 22.22% |
| T3A- | 7.67% | — |
| T3C2 | 7.56% (31.81% without the pressure-gradient correction) | 2.98% (18.65%) |
| T3C3 | 4.61% | — |
| T3C4 | 12.67% | — |
| T3C5 | 5.89% (8.94%) | 21.64% (36.08%) |

On T3B the start of transition agrees ($Re_x=6.72\times10^4$ against
$5.89\times10^4$) but the end lies downstream ($1.59\times10^5$ against
$1.22\times10^5$): the momentum-thickness threshold limits the energy
transfer, so the transition region is longer and the peak $C_f$ lower than
with the original model, a regression the authors acknowledge (Fig. 5).
On T3C4 separation, onset and reattachment are captured but the peak shape
factor, i.e. the bubble height, is underestimated (Fig. 8). The
pressure-gradient correction thus reduces the adverse-gradient onset error
in their model, the difficulty that Menter et al. (2022), Liu et al. (2024)
and Pacciani et al. (2025) also report (below). Sweeping
the inlet $Tu$ from its reference value to a tenth of it at T3A Reynolds
number moves the onset monotonically, without the slope reversals the
authors report for earlier laminar-kinetic-energy variants (Fig. 15). On
the Schubauer–Klebanoff plate the onset error is 8.34% and on the five
Schubauer–Skramstad plates 3.00%–6.01% (Table IV).

**Low free-stream turbulence.** On T3A- and the Schubauer–Klebanoff plate
the transition path is "definitely too steep" with both the
laminar-kinetic-energy model and γ-$Re_\theta$, a model without a natural
transition term, "in line with" Menter et al. (2015) as the authors recall
([Pacciani et al. (2025)](/sources/pacciani-2025.md), §5.1.1, Figs. 7–8).
The Schubauer–Klebanoff plate serves [Menter et al. (2022)](/sources/menter-2022.md)
as the hysteresis test of the algebraic model (§2.3, Figs. 2–3).

**Pressure gradient: delayed onset in adverse gradient.** The sources agree
that adverse-gradient onset is the hard part of the series:

- With a constant onset threshold $c_5=24$, the laminar-kinetic-energy model
  delays onset significantly on T3C2, T3C3 and T3C4; making $c_5$ a
  function of a local pressure-gradient parameter corrects it, but the
  transition region stays too short. On T3C4 a small separation is
  computed, but the separation term does not activate because the
  pressure-gradient correction triggers transition first
  ([Pacciani et al. (2025)](/sources/pacciani-2025.md), §5.1.3, Figs. 11–13).
- SSG/LRR-ω-γ agrees well on the favourable cases T3C1 and T3C5 and delays
  onset on T3C2–T3C4, "similar to the problem existing in the SST–γ model"
  as the authors recall from Menter et al. (2015); T3C4 behaves as
  separation-induced transition ([Liu et al. (2024)](/sources/liu-2024.md),
  Fig. 6d–h).
- γ-alg-SST agrees "satisfactorily" on T3C, with earlier bypass transition
  than the transport models; on T3C3 and T3C4 γ-alg-SST and the one-equation
  γ-SST model predict the bubble transition later than γ-$Re_\theta$-SST
  ([Menter et al. (2022)](/sources/menter-2022.md), Fig. 9).

See [laminar separation bubble](/definitions/laminar-separation-bubble.md)
for T3C4.

**Favourable gradient and the laminar skin friction.** On T3B and T3C1 the
laminar-kinetic-energy model places onset correctly but misses the laminar
$C_f$ (overestimated on T3C1), which the authors attribute to the missing
leading edge in their mesh; the coefficient $c_{\mu,\ell}$ of its laminar
fluctuation viscosity changes the transitional $C_f$ ramp in favourable
gradient, not the onset, and the value 0.03 then agrees "very well" with
γ-$Re_\theta$ ([Pacciani et al. (2025)](/sources/pacciani-2025.md),
§5.1.1–5.1.2, Figs. 6, 9–10).

**Grid sensitivity of algebraic models.** On T3A the transport models stay
reasonable with streamwise spacings of $10\delta$, while γ-alg-SST deviates
from $2\delta$ on and is "clearly less forgiving"
([Menter et al. (2022)](/sources/menter-2022.md), §4, Fig. 26).

**Host turbulence model.** The same laminar-kinetic-energy coupling on the
Wilcox $k$-$\omega$ model gives the same T3A onset as on
[$k$-$\omega$ SST](/methods/k-omega-sst-model.md) but a quicker transition
and a different turbulent $C_f$ level, so the constants "should be
retouched" per turbulence model
([Pacciani et al. (2025)](/sources/pacciani-2025.md), §5.1.1, Fig. 5).

**A check of a transitional hybrid.** [Möller et al. (2024)](/sources/moller-2024.md),
§II.F, run T3C5 (bypass transition at a free-stream turbulence intensity
comparable to their compressor cascade) with DDES-$\gamma$, their coupling
of SST-based [delayed DES](/methods/detached-eddy-simulation.md) with
Menter's one-equation
[$\gamma$ model](/methods/local-correlation-based-transition-model.md), and
state that it gives results identical to RANS-$\gamma$ (results not shown).
The authors argue that in a laminar or transitional layer $\gamma=0$
keeps the modelled turbulent kinetic energy and the RANS length scale near
zero, so the region is declared "RANS mode" although it is "more a laminar
mode" (§II.D, Fig. 1); on their cascade the attached pressure-side layer
likewise stays in RANS mode and the hybrid does not improve bypass
transition over RANS-$\gamma$ without resolved inflow turbulence (§III.B,
§IV). Their cascade results are on the
[compressor cascade](/benchmarks/compressor-cascade.md) page.

## Qualifications

- The inlet values of the table are simulation settings, each source
  tuning them to the measured free-stream decay (Menter et al., §3;
  Pacciani et al., §5.1: "to match the experimental turbulence decay";
  Liu et al., Figs. 3–4); they are not a common specification, and the
  T3A- and T3B eddy-viscosity ratios differ by up to a factor 1.5
  *(compiler check, not in the sources)*. The Schubauer–Klebanoff inlet
  intensity is printed as 0.03% by
  [Menter et al. (2022)](/sources/menter-2022.md), Table 2, and 0.3% by
  [Pacciani et al. (2025)](/sources/pacciani-2025.md), Table 1 (both
  checked in the PDFs), with viscosity ratios 1.0 and 1.2; neither source
  discusses the difference or prints the measured intensity at the plate.
  Because both values are inlet settings of different computational
  domains, not statements about the experiment, this is recorded as a
  difference in printed set-up, not a contradiction.
- The intermittency $\gamma$ is not the same object in the three sources: a
  transported or algebraic field of the local-correlation family in
  [Menter et al. (2022)](/sources/menter-2022.md) and
  [Liu et al. (2024)](/sources/liu-2024.md) (where it multiplies the
  production, the pressure–strain and, through $\max(\gamma,0.1)$, the
  dissipation of the Reynolds stresses), and the algebraic ratio of
  turbulent to total fluctuation energy in
  [Pacciani et al. (2025)](/sources/pacciani-2025.md).
- [Liu et al. (2024)](/sources/liu-2024.md) say their grid levels double
  the points in each direction; their Table 3 dimensions are approximately
  doubled (for example 186 to 365 streamwise) *(compiler check, not in the
  sources)*.
- After the T3 series all three sources continue their transition
  validation on airfoils and cascades: the S809 airfoil in
  [Menter et al. (2022)](/sources/menter-2022.md) and
  [Pacciani et al. (2025)](/sources/pacciani-2025.md), compressor cascades
  in [Liu et al. (2024)](/sources/liu-2024.md) (see
  [compressor cascades](/benchmarks/compressor-cascade.md)), and
  [turbine cascades](/benchmarks/turbine-cascade.md) in Menter et al. and
  Pacciani et al. On S809 Menter et al. report natural transition starting
  at $\alpha=6^\circ$ (algebraic) and $7^\circ$ (transport models) against
  about $5^\circ$ measured (Figs. 20–22), and Pacciani et al. a suction-side
  onset slightly upstream of the measurement at all angles (§6.3,
  Figs. 24–25); the two use different metrics.

- [Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md) print the T3A
  intensity as 3.3% in Table II and as 2.3% in §IV A. Their onset errors
  match $|Re_{x,tr}-Re_{x,tr}^{\mathrm{ref}}|/Re_{x,tr}^{\mathrm{ref}}$
  ($Re_{x,tr}$ page-local: $Re_x$ at the onset; ref: measured) in
  Tables IV and IX; by that measure the printed onsets reproduce the T3A
  and T3B errors (8.22% and 22.22%) within the rounding of the printed
  $Re_{x,tr}$, but give 9.7% for the Schubauer–Klebanoff plate (printed
  8.34%) *(compiler check, not in the sources)*. They give two different start and end pairs for the same
  Schubauer–Klebanoff onset (§IV A).
- The two high-order sources' inlet settings differ from each other as the
  others do (T3A $Tu$ 3.5% against 3.3%, T3B $\nu_t/\nu$ 100 against 95),
  and Ghidoni & Noventa's T3A- intensity of 0.48% is a deliberate departure
  from the measured value, which Menter et al. (2022), Liu et al. (2024),
  Pacciani et al. (2025) and Vandenhoeck et al. (2022) keep (0.874–0.9%).
  Vandenhoeck et al. predict the T3A- onset significantly earlier than the
  experiment and do not compare its profiles (§4.2).

# Citations

- [Menter et al. (2022)](/sources/menter-2022.md) — §2.2, Fig. 1; §2.3, Figs. 2–3; §3, §3.1, Tables 2–3, Figs. 7–9; §3 (S809), Figs. 20–22; §4, Fig. 26.
- [Liu et al. (2024)](/sources/liu-2024.md) — Introduction; numerical setup, Tables 2–3, Figs. 3–6.
- [Pacciani et al. (2025)](/sources/pacciani-2025.md) — §4.2, Fig. 1; §5.1.1–5.1.3, Tables 1, 3, Figs. 2–13; §6.3, Figs. 24–25.
- [Möller et al. (2024)](/sources/moller-2024.md) — accepted manuscript: §II.D, Fig. 1; §II.F; §III.B; §IV.
- [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md) — §3.2.3, Figs. 6–7; §4.2, Table 3, Figs. 11–16.
- [Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md) — §IV A, Tables II–IV, Figs. 4–8, 15.

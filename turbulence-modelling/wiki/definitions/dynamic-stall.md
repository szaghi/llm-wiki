---
type: Definition
title: "Dynamic stall"
description: "Unsteady stall of an airfoil pitched beyond its static stall angle: a leading-edge separation bubble bursts, a dynamic-stall vortex forms, convects and sheds, and lift overshoots the static maximum; the stages, the stall type at low Reynolds number, and what LES, DDES and URANS reproduce of it."
status: established
aliases: [deep dynamic stall, dynamic stall onset, dynamic-stall vortex, DSV, pitching-airfoil stall]
tags: [separated-flow, transition, hybrid-rans-les, des, les, boundary-layer, dynamic-stall]
timestamp: 2026-10-27T10:39:00Z
---

# Dynamic stall

Dynamic stall is the stall of an airfoil whose incidence $\alpha$
(page-local: angle of attack) increases in time past the static stall
angle. The boundary layer stays attached longer than in the static case,
lift keeps growing, and stall comes through a large leading-edge vortex,
the **dynamic-stall vortex** (DSV), which forms from the separated shear
layer, convects along the suction side and sheds; the loads then collapse,
and on a return stroke the flow reattaches at a lower incidence than the
one at which it separated. In the two ingested sources the airfoil is a
[NACA 0012](/benchmarks/naca-0012-airfoil.md) at chord Reynolds numbers
$Re_c$ of $1.35\times10^5$ and $2\times10^5$, where the trigger is the
bursting of a leading-edge
[laminar separation bubble](/definitions/laminar-separation-bubble.md). The
term decides how a pitching-airfoil case is classified (stall type,
deep against ramp-up motion) and which part of the cycle a simulation must
resolve.

## Motions in the sources

- **Constant-rate pitch-up (ramp).** [Batther & Lee (2022)](/sources/batther-2022.md),
  §2.1, Eq. (1), replicate the LES set-up of Visbal and Garmann that they
  cite: $Re_c=2\times10^5$, $M=0.10$, pitch rate
  $\dot\alpha(t^*)=\dot\alpha_0^+\left(1-e^{-4.6t^*/t_0}\right)$ with
  $t^*=tU_\infty/c$, $\dot\alpha_0^+=0.05$ and $t_0=0.5$ (page-local
  symbols: the asymptotic non-dimensional pitch rate and the ramp time
  constant; the rate reaches 99% of $\dot\alpha_0^+$ at $t_0$), started
  from a well-resolved static solution (Table 2 gives its wall units at
  $4^\circ$); 35,000 steps of
  $\Delta t^*=2.56\times10^{-4}$ cover the upstroke, about 1300 per degree.
- **Sinusoidal pitching (deep dynamic stall).**
  [Baldan & Guardone (2025)](/sources/baldan-2025.md) (read in arXiv v2)
  reproduce the Lee & Gerontakos experiment,
  $\alpha(t)=10^\circ+15^\circ\sin(\varpi_{\mathrm p}t)$ ($\varpi_{\mathrm p}$
  page-local: angular pitching frequency), reduced frequency 0.1,
  $Re_c=1.35\times10^5$, $U_\infty=14$ m/s; the cycle includes the
  downstroke, which ramp-up studies do not simulate (§2.1, §3).

## Stages

The two sources describe the same sequence, with stage angles that depend
on the motion.

| Stage | [Batther & Lee (2022)](/sources/batther-2022.md), Table 3 (ramp, DDES) | [Baldan & Guardone (2025)](/sources/baldan-2025.md), Introduction; §2.1, Fig. 6 (sinusoid, LES) |
|---|---|---|
| attached flow, transition moving upstream | transition point moves upstream from about $8^\circ$ | transition starts at the trailing edge near $2^\circ$ and reaches the bubble by $10^\circ$ |
| leading-edge bubble | forms at $10.6^\circ$ (laminar separation, turbulent reattachment); suction rises at $12.9^\circ$; at $15.2^\circ$ the adverse pressure gradient acts on the bubble, which shows two reattachment branches | present in the upstroke, with attached flow |
| bubble bursting ("suction collapse") | $16.9^\circ$: suction lost as the bubble collapses; lift still grows linearly | the bubble–boundary-layer interaction triggers the vortex |
| DSV formation | $18.6^\circ$: the separated shear layer rolls up; the $C_L$–$\alpha$ slope rises sharply | DSV develops beyond $15^\circ$ |
| DSV convection and shedding | $21.5^\circ$: DSV fully formed, convects to about 50% of the chord and detaches; stall onset just after $23.2^\circ$ | DSV reaches the trailing edge at $22^\circ$ and interacts with the trailing-edge vortex |
| full stall and reattachment | (upstroke only) | suction side fully stalled at maximum incidence and early downstroke; reattachment at reduced incidence owing to the negative pitch rate |

Batther & Lee add that the DSV reaches its maximum strength at about 40% of
the chord, where it starts to shed, coinciding with the peak lift just
before stall onset (§4.2.3); that the lift-slope jump at $18.6^\circ$ was
also documented by the references they cite (§4.2.3, Table 3); and that
strong high-frequency surface-pressure oscillations at $x/c=0.05$ precede
DSV formation, as in the Lorber and Carta experiment they cite (§4.2.5,
Fig. 16). Streamwise "vortex sheets" (Q-criterion iso-surfaces) appear at
about $18^\circ$ and persist beyond stall; the authors hypothesise that they
trigger the DSV detachment (§4.2.4, Fig. 13). Baldan & Guardone's
Q-criterion views show hairpins marking transition at $10^\circ$ in the
upstroke, a mainly two-dimensional DSV near $20^\circ$, a fully
three-dimensional flow at maximum incidence and relaminarization near
$0^\circ$ in the downstroke (§2.1, Fig. 8).

## Stall type

Following the classification of McCroskey et al. and of Benton and Visbal
that they cite, [Batther & Lee (2022)](/sources/batther-2022.md), §4.2.2,
§4.2.5, distinguish:

- **leading-edge bubble-bursting stall**: the leading-edge laminar
  separation bubble bursts under the pressure gradient (low Reynolds
  number);
- **turbulent leading-edge (mixed-type) stall**: trailing-edge reversed
  flow propagates upstream and bursts the bubble (the case of Benton and
  Visbal at $Re_c=10^6$, as Batther & Lee cite it).

Their $Re_c=2\times10^5$ case is of the first type: the reversed flow near
the trailing edge (negative $C_f$) does not propagate upstream during the
motion, and the bubble's history before its collapse "seemingly does not
have a significant impact" on DSV formation (§4.2.3, §4.3.1). Lift keeps
increasing after the collapse, unlike in static stall (§4.2.3).

## What simulations reproduce

**Wall-resolved LES and the spanwise domain.** Batther & Lee take the
wall-resolved LES of Visbal and Garmann (74 million points,
$1349\times410\times133$) as their reference; that study, as they report
it, found spans from 10% to 120% of the chord equivalent for the ramp-up
(§2.1). [Baldan & Guardone (2025)](/sources/baldan-2025.md), §2.1, §3,
find the same span insensitivity in the attached upstroke (at most 0.05 in
$C_L$ across $L_z/c=0.2$–1.2 up to about $22^\circ$) but not in the
downstroke: once the bubble bursts, the short spans force a quasi-two-dimensional
DSV and spurious lift peaks, and a span of at least one chord is needed.
Baldan & Guardone themselves judge the short spans of the LES literature
acceptable only for attached-flow, ramp-up motions (§3). The numbers are on
[NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md) and
[grid-point requirements of LES](/results/les-grid-point-requirements.md).

**DDES with transition closures.** [Batther & Lee (2022)](/sources/batther-2022.md)
answer the question of Visbal and Garmann, whether RANS or hybrid methods
can reproduce the abrupt bubble bursting and suction collapse, with
[delayed detached-eddy simulation](/methods/detached-eddy-simulation.md) in
NASA's OVERFLOW 2.3 (fifth-order central differences with scalar
dissipation, 30 sub-iterations per step), on an O-grid of
$811\times200\times100$ points (about 16 million, 22% of the LES), span
$0.1c$, upper-surface $y^+\approx0.4$ (§2–§3, Tables 1–2). The DDES
formulation itself (shielding function, constants) is not printed. Four
RANS closures run inside DDES: SST Langtry–Menter and SA Medida–Baeder
$\gamma$–$Re_{\theta t}$ [correlation-based transition models](/methods/local-correlation-based-transition-model.md),
Coder's SA amplification-factor-transport model, and the fully turbulent
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md). Their
findings (§4.2–§4.5, §5, Figs. 14–22):

- every transitional DDES captures the bubble formation, its bursting and
  the DSV formation of the LES, but predicts lift stall slightly earlier
  and a slightly lower peak $C_L$;
- against the LES, DDES gives a larger bubble at $15.2^\circ$ with weaker
  reverse flow, more oscillation around it, an earlier suction collapse and
  a faster DSV convection;
- the amplification-factor-transport model is closest to the LES; SST
  Langtry–Menter stalls earliest, through an earlier loss of suction; the
  SA Medida–Baeder model oscillates at low incidence;
- after the collapse ($16.9^\circ$ to $23.2^\circ$) all transition models
  give similar $C_p$, "a common ground for the flow physics post suction
  collapse, regardless of the transition model";
- fully turbulent SA underpredicts lift at low incidence and forms an
  abrupt turbulent separation bubble between $14.1^\circ$ and $14.5^\circ$
  instead of a laminar one, which the authors say "has not yet been
  documented in literature"; they judge a fully turbulent model not
  optimal in this Reynolds-number range (§4.4).

**URANS, SBES and LES against experiment.** In deep dynamic stall
[Baldan & Guardone (2025)](/sources/baldan-2025.md), §2.2, Fig. 9, find
their 1.2-chord LES, a 2D URANS on [$k$-$\omega$ SST](/methods/k-omega-sst-model.md)
with an intermittency equation and a 3D stress-blended eddy simulation
within 0.1 of one another in attached $C_L$, all with peak lift at
$22^\circ$ against $24^\circ$ measured, and with a persistent $C_L$ offset
of about 0.2 from the experiment; they attribute the experiment–simulation
gap to wind-tunnel effects or surface roughness rather than to the
turbulence model (§3); see
[model-form uncertainty](/definitions/model-form-uncertainty.md) and
[hybrid RANS/LES](/definitions/hybrid-rans-les.md).

**Where the sources agree.** Both place the decisive event at the leading
edge: the bursting of the laminar separation bubble starts the DSV, and in
both a hybrid or RANS model captures the sequence but not its timing
exactly (DDES early in [Batther & Lee (2022)](/sources/batther-2022.md);
all three models at $22^\circ$ against $24^\circ$ in
[Baldan & Guardone (2025)](/sources/baldan-2025.md)). The direction of the
timing error is measured against different references: Batther & Lee
compare with an LES, Baldan & Guardone with an experiment.

## Qualifications

- [Batther & Lee (2022)](/sources/batther-2022.md) use no experimental
  dynamic-stall data; their only experimental comparison is a static 2D
  RANS validation at $Re_c=10^6$ (§4.1, Fig. 3). They compare three grids
  of one family and do not print the DDES shielding; the retained grid has
  $\Delta x^+$ of 17.6 (upper-surface average) to 23.1 ($x/c=0.8$) and
  $\Delta z^+$ of 7.2 to 9.4 (Table 2).
- Batther & Lee state the DDES time step both as "one order of magnitude
  larger than that used in LES" (§2.1) and as "roughly 8% of that used in
  LES" (§4.5); the two cannot both hold. They give the cost as "roughly
  20 s per time step using 192 cores", "about 1500 total CPU hours"
  (§4.2.1); 20 s for each of the 35,000 upstroke steps on 192 cores is
  about $3.7\times10^4$ core-hours *(compiler check, not in the sources)*.
  §4.2.2 calls $10.6^\circ$ "stage 3", which Table 3 lists as stage 2.
- [Baldan & Guardone (2025)](/sources/baldan-2025.md) compute one cycle
  per model, without phase averaging or cycle-to-cycle statistics (§2.2);
  their Introduction says transition progresses "downstream" from the
  trailing edge, while §2.1 has it moving towards the bubble.
- Not every pitching-airfoil benchmark is a dynamic-stall case. The
  transonic AGARD Case 3 pitching NACA 0012 that
  [Sugaya & Imamura (2021)](/sources/sugaya-2021.md), §3.2, run with
  Spalart–Allmaras RANS on a moving Cartesian grid ($M_\infty=0.6$,
  $Re=4.8\times10^6$, $\alpha=4.86^\circ+2.44^\circ\sin\varpi_{\mathrm p}t$,
  reduced frequency 0.081, pivot at quarter chord) stays between
  $2.42^\circ$ and $7.30^\circ$ *(compiler check, not in the sources)*; the
  authors report shock motion and the $C_L$ and pitching-moment hysteresis
  loops, with an inversion of the lift trajectory near $6^\circ$, and
  describe no stall vortex (Figs. 10–13). The case is recorded on
  [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md).

# Citations

- [Batther & Lee (2022)](/sources/batther-2022.md) — §1; §2.1, Eq. (1); §2.2, Tables 1–2; §3; §4.1, Fig. 3; §4.2.1–4.2.5, Table 3, Figs. 4–16; §4.3.1, Figs. 17–20; §4.4, Figs. 21–22; §4.5; §5.
- [Baldan & Guardone (2025)](/sources/baldan-2025.md) — arXiv v2: Introduction, Fig. 1; §2.1, Figs. 3–8; §2.2, Fig. 9; §3.
- [Sugaya & Imamura (2021)](/sources/sugaya-2021.md) — §3.2, Figs. 10–13 (a pitching case outside the definition).

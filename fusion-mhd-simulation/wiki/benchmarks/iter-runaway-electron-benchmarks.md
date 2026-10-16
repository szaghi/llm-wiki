---
type: Benchmark
title: "ITER runaway-electron benchmarks (JOREK–GO, JOREK–DINA)"
description: "Code-to-code tests of the JOREK runaway-electron fluid model: RE beam formation after neon and deuterium–neon injection in a circular 15 MA ITER-like plasma against the 1D code GO, and simultaneous RE beam formation and cold VDE in a 15 MA ITER free-boundary plasma against the 2D code DINA, preceded by a non-ITER current-conversion test against GO."
status: established
aliases: [JOREK-GO benchmark, JOREK-DINA RE benchmark]
tags: [benchmark, verification, runaway-electrons, disruption, vde]
timestamp: 2026-10-16T00:00:00Z
---

# ITER runaway-electron benchmarks (JOREK–GO, JOREK–DINA)

These benchmarks test the [runaway-electron fluid model](/methods/runaway-electron-fluid-model.md)
of [JOREK](/software/jorek.md) against two lower-dimensional disruption
codes: GO, a 1D time-dependent RE fluid code with background
electrodynamics, and DINA, a 2D axisymmetric free-boundary evolution code
with an RE fluid and impurity charge-state tracking
([Bandaru et al. (2024)](/sources/bandaru-2024.md), §III–IV). Neither
reference code is in this bundle; their descriptions are those of the
JOREK papers.

## Precursor: current conversion against GO (2019 model)

[Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§4.7, Fig. 24) report the
first JOREK–GO test, on a large-aspect-ratio circular plasma ($R=10$ m,
$a=1$ m, $I_p=0.67$ MA, $B_\phi=1$ T on axis, $T=1.7$ keV and
$n=10^{20}$ m$^{-3}$ at the centre, $\eta=1.1\times10^{-7}$ Ω m). A large
imposed $\kappa_\perp$ cools the core to about 25 eV in about 60 ms; Dreicer
generation starts at $E_\parallel/E_D\ge0.01$ and avalanche at
$E_\parallel/E_c\ge1.7$, and GO takes its temperature evolution from JOREK.
Total and RE currents agree with deviations around 1%. This is not an ITER
case and uses the 2019 source set.

## Benchmark 1: RE formation after material injection (JOREK–GO, 1D)

**Setup** ([Bandaru et al. (2024)](/sources/bandaru-2024.md), §III.A,
Table I). Circular 50/50 DT plasma, $R_0=6$ m, $a=2$ m, $I_p=15$ MA,
$n_e=10^{20}$ m$^{-3}$, $J=1.69[1-(r/a)^2]^{0.41}$ MA m$^{-2}$,
$T_e=20[1-(r/a)^2]$ keV. JOREK runs at $R_0=50$ m to mimic the cylinder,
and profiles are compared as flux-surface averages. At $t=0$ a uniform
D+Ne mixture appears: case A pure neon (neon density equal to the initial
electron density), case B deuterium-dominated (deuterium and neon densities
7 and 0.08 times the initial electron density). For 6 ms the temperature is
forced to relax exponentially from its initial profile toward 50 eV with a
1 ms time constant, bringing the core to about 100 eV; afterwards it evolves self-consistently with
radiation, Ohmic heating, ionization losses and
$\chi_\perp=0.4$ m²/s. Sources: Compton, tritium and avalanche; no
hot-tail, no Dreicer. JOREK freezes the flow ($u=0$, $v_\parallel=0$) and uses
$f_{\mathrm{adv}}=10^{-3}$, $D_{\parallel,\mathrm{RE}}=1.54$ m²/s and all
particle diffusivities 0.015 m²/s. GO was rerun with coronal equilibrium,
a fixed boundary temperature and a conducting wall at the plasma boundary,
to match JOREK's assumptions; the authors state that the differences from
the published GO cases of Vallhagen et al. (2020) are "significant", so the
comparison is not against those published numbers.

**Results** (§III.B, Figs. 1–4).
- $I_p$ and $I_{\mathrm{RE}}$: "a good match" in both cases; case A forms a
  much larger RE beam.
- RE current-density profiles: "decent match"; spatiotemporal maps:
  "excellent agreement".
- $T_e$ settles at 6–9 eV and drops to about 1 eV after conversion to REs
  (case A). In case B the late-time $T_e$ "only matches qualitatively ...
  mainly a time-shift, and the reason for this is not fully clear".
- In case B a neutral front moves inward from the boundary and flattens
  $T_e$ step by step, driven by deuterium line-radiation feedback.
No plateau values are quoted in the text.

## Benchmark 2: RE beam formation with a cold VDE (JOREK–DINA, 2D)

**Setup** (§IV.A). Elongated ITER free-boundary equilibrium,
$I_p=15$ MA, uniform $n_e=10^{19}$ m$^{-3}$, $T_e\approx15$ keV in the core,
$q_0\approx1$, $q_{\mathrm{edge}}\approx3.7$, with the ITER vessel (two
6 cm shells, $\eta_w=0.8\times10^{-6}$ Ω m) and coils coupled through
[JOREK–STARWALL](/methods/resistive-wall-coupling.md). After 1.5 ms of
near-equilibrium evolution an artificial cooling with
$\kappa_\perp=1.27\times10^{24}$ m$^{-1}$s$^{-1}$ brings the core to about
20 eV by 2 ms, with the parallel conductivity raised at the same time to
suppress [halo currents](/definitions/halo-current.md). At 2 ms uniform
neon ($4.88\times10^{22}$ atoms, $n_{\mathrm{imp}}=0.62\times10^{20}$
m$^{-3}$) appears inside the last closed surface together with a one-off
artificial RE seed; tritium and Compton sources are off. JOREK: neutrals
not evolved, $\eta=\eta_{\mathrm{Sp}}Z_{\mathrm{eff}}$,
$f_{\mathrm{adv}}=0$, $D_{\parallel,\mathrm{RE}}=1.54\times10^8$ m²/s.
DINA tracks charge states with large radial charge-state diffusion (flat
$Z_{\mathrm{eff}}$) and neglects partial screening in the avalanche; a
"DINA-C" run mimics coronal equilibrium.

**Results** (§IV.B, Figs. 5–9).
- Plateau RE current about 10 MA in DINA and DINA-C, matched best by JOREK
  seeds of 0.1–1 A against 3.8 kA in DINA. A seed of $10^{-4}$ A still
  gives about 9.5 MA (not plotted).
- The current rises during the JOREK plateau, attributed to the decay of
  vessel currents adding electric field (vessel current "not shown").
- $T_e$ drops to about 2 eV, nearly uniform; reasonable agreement. DINA-C
  oscillates between about 3 and 8 ms (not plotted).
- The plasma moves upward in a cold
  [VDE](/definitions/vertical-displacement-event.md) that continues
  through the plateau; time scale about $2\times10^{-2}$ s in both codes,
  "a good match". The motion is much faster than the vessel time
  $\tau_{L/R}=0.5$ s, which the authors explain by the small stabilization
  parameter of a multi-conductor model (Leuer 1989); the poloidal Alfvén
  time is about $1.1\times10^{-5}$ s.
- The internal inductance $l_i(3)$ differs "significantly" between the
  codes, attributed to the different RE source models and possibly to
  different integration domains (Fig. 9a).
- A scan of the vessel resistivity (Fig. 9b): at the nominal value the
  results are not converged to the ideal-wall limit; reducing the
  resistivity by a factor of about 10 or more removes the fast vertical
  motion and makes halo currents negligible.

## Spread and its attribution

- **Seed current.** The JOREK seed that reproduces DINA's plateau is 3.6
  to 4.6 orders of magnitude smaller than DINA's (0.1–1 A against 3.8 kA;
  compiler's arithmetic). Bandaru et al. attribute it "largely" to DINA's
  neglect of partially ionized impurities in the avalanche, i.e. to a
  difference of source model, not of numerics (§IV.B).
- **Case B time shift** in $T_e$ against GO: unexplained (§III.B).
- **Halo current.** §IV.B states that the halo current "can be seen to be
  negligible in all cases", while the vessel-resistivity discussion says
  halo currents "drop to negligible values in the lower vessel resistivity
  cases", which implies non-negligible values at the nominal resistivity
  late in the VDE (recorded on the Source page).

## Contradictions

**JOREK–DINA seed discrepancy** — Open.
[Bandaru et al. (2024)](/sources/bandaru-2024.md) (§IV.B, Fig. 7a) need a
JOREK seed of 0.1–1 A to reproduce the 10 MA plateau that DINA obtains
with 3.8 kA. They attribute the gap to DINA's avalanche model without
partial screening, which is a stated cause, not a demonstrated one. The
plateau is nearly seed-independent, so plateau agreement does not by
itself test the avalanche rate. Rerunning JOREK with its partial-screening
terms switched off, or DINA with them on, at the DINA seed would settle
whether the source model accounts for the whole gap.

# Citations

- [Bandaru et al. (2024)](/sources/bandaru-2024.md) — §III–V, Table I, Figs. 1–9.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §4.7, Fig. 24.

---
type: Definition
title: "Soft β limit of stellarators"
description: "A β limit set not by disruptive MHD but by enhanced transport from mild, saturated pressure-driven activity, typical of net-current-free stellarators; JOREK3D simulations of W7-AS attribute it to visco-resistive activity that leaves field lines ergodically confined in radially separated sub-volumes, but reach no β flat top."
status: established
aliases: [soft beta limit, soft β-limit, W7-AS beta limit]
tags: [stellarator, mhd, reduced-mhd, ballooning, verification]
timestamp: 2026-10-16T12:00:00Z
---

# Soft β limit of stellarators

The β limit of net-zero-current stellarators is "often soft, in the sense
that large scale disruptive [MHD] activity is avoided": the achievable β
saturates because pressure-driven MHD activity enhances transport, not
because a global instability terminates the discharge
([Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §1, citing Weller et
al.). A soft limit is a transport limit with an MHD cause; a hard limit is
a stability boundary beyond which the plasma is lost. The distinction is
load-bearing for interpreting linear stability limits such as the
[Mercier criterion](/definitions/interchange-mode.md), which stellarator
experiments can exceed without losing the plasma (§1).

## The W7-AS case

The experimental reference is W7-AS shot #51751 and its β scans:
$B\approx0.9$ T, density about $2\times10^{20}\ \mathrm m^{-3}$, temperatures
of order 100 eV, 3.2 MW of neutral-beam heating from two counter-directed
sources (so no net momentum input). Low-$n$ activity appears at
$1.5\,\%<\beta<2.5\,\%$, MHD activity is suppressed above about 2.5 %, and
the experimental β limit is 3.4 %
([Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §4, §4.5). The two
figures, 2.5 % and 3.4 %, are different quantities.

## Simulation of the limit

[Ramasamy et al. (2024)](/sources/ramasamy-2024.md) simulate the scan with
[JOREK3D](/software/jorek3d.md) ([stellarator reduced MHD](/methods/stellarator-reduced-mhd.md);
the simplified scan without parallel flow, the experimental-parameter runs
with it), starting from fixed-boundary
[VMEC](/software/vmec.md) reconstructions with central pressures of 1, 4,
8 and 10 kPa (the 14 kPa case, with a strong Shafranov shift, could not be
imported accurately into the JOREK ansatz) and 3.2 MW of uniform heating
(§4.1–4.2, Table 3). The findings:

* **The activity is resistive.** At 10 kPa, a tenfold increase of $\eta$
  (to about $1.9\times10^{-5}\ \Omega$ m) makes the initial MHD activity destroy
  confinement and β falls; lower $\eta$ makes the activity milder and
  confined to the edge, and at $\eta=1.93\times10^{-7}\ \Omega$ m β rises
  to about the experimental 3.4 % by 3.5 ms. The baseline
  ($\eta=1.93\times10^{-6}\ \Omega$ m) is capped near 2.35 % by a mild
  crash (§4.2, Fig. 9).
* **Ergodic but confined.** With approximately experimental coefficients
  (Spitzer $\eta$, Spitzer–Härm $\kappa_\parallel$, a Braginskii-range
  perpendicular viscosity) and $n$ up to 50, Poincaré plots show ergodic
  field lines that remain separated into radially localized sub-volumes;
  islands do not overlap enough to flatten $T$ across the radius, so β
  keeps rising. Confinement is worst when the ergodic region crosses
  $\iota=0.5$, marked by a $(10,5)$ chain; most ergodization lies outside
  $\iota=0.5$, as in earlier PIES equilibrium studies (§4.3.3, Fig. 12).
* **Conclusion.** "the simulations support the conclusion that the MHD
  activity is viscoresistive. At viscoresistive parameters which approach
  the experimental values, a soft β limit can be observed, because the
  induced MHD activity is mild enough for field lines to remain
  ergodically confined within nested plasma sub-volumes" (§4.5, §5).
* **Low-$n$ structure.** In full-torus runs at
  $\eta=1.93\times10^{-5}\ \Omega$ m the $N_{\rm fp}$-symmetry-breaking
  family containing $n=1$ dominates and a $(2,1)$ island appears at about
  0.46 ms, "in line with past experimental observations"; at Spitzer
  $\eta$ the family containing $n=2$ dominates, core surfaces survive and a
  $(4,2)$ deformation sits near $\iota=0.5$ (§4.4, Fig. 13; see
  [toroidal mode families](/definitions/toroidal-mode-family.md)).

## Sensitivities and caveats

* **Toroidal resolution.** The rate of rise of β falls as the highest
  toroidal mode number grows to about 50 and is converged above;
  under-resolved runs show artificially good confinement, so high-$n$
  modes matter. Doubling the poloidal resolution changes little (§4.3.1,
  Fig. 10).
* **Transport coefficients.** Tripling $\kappa_\perp$ (0.231 to
  0.693 m²/s) makes β fall below its initial value; the result "is
  sensitive to the thermal transport parameters" (§4.3.2, Fig. 11).
* **No flat top.** In the experimental-parameter runs β rises from 2.25 %
  to about 2.6–2.7 % within about 1.1 ms and no flat top near 3.4 % is
  reached (§4.3, §4.5). "Soft β limit is observed" in the paper therefore
  means mild, non-disruptive saturation of the MHD activity, not a β
  plateau (reader's note on the Source page).
* **Fixed boundary.** Without the free-boundary Shafranov shift and
  tokamak-like shear growth, the $\iota=0.5$ surface stays in the plasma at
  high β, which artificially enhances the activity; the 1 and 4 kPa runs
  flatten at β above 1.3 %, below the experiment. Missing island divertor,
  radial electric field, impurities and radiation are further named
  limitations (§4.2, §4.5).

## Contrast with tokamak β limits

In tokamaks a pressure-driven low-$n$ mode in a weak-shear core can flatten
the pressure abruptly: the $n=3$ ideal and resistive
[infernal modes](/definitions/infernal-mode.md) of
[Sato et al. (2024)](/sources/sato-2024.md) produce a "beta collapse" in
MHD, and kinetic thermal ions suppress the collapse of the resistive one
(§3.2). That limit is set by the nonlinear flattening of the profile, not
by mild ergodic transport.

# Citations

* [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) — definition, W7-AS experiment, JOREK3D simulations, sensitivities and caveats.
* [Sato et al. (2024)](/sources/sato-2024.md) — tokamak beta collapse by infernal modes, for contrast.

---
type: Definition
title: "Reduced speed of light approximation"
description: "Replacing the speed of light c by a smaller ĉ = f_c c in the time derivatives of explicit radiation moment equations to relax the light-speed time step, with two validity criteria (ionization-front propagation in RAMSES-RT; time-scale ordering in Hyperion), and Quokka's finding that a closed system then relaxes to a biased equilibrium, about 20 % too hot at ĉ = 0.1c."
status: established
aliases: [RSLA, reduced speed of light, RSL, ĉ approximation]
tags: [radiation, reduced-speed-of-light, time-integration]
timestamp: 2026-10-12T00:00:00Z
---

# Reduced speed of light approximation

Explicit radiation transport is limited by the light-crossing time of a
cell, $\Delta t < h/(3c)$ in 3D, a step "typically 300 times shorter" than
the hydrodynamic one ([Rosdahl et al. (2013)](/sources/rosdahl-2013.md),
§4.1, eq. 31). The reduced speed of light approximation (RSLA, after
Gnedin & Abel 2001) replaces $c$ by
$$\hat c = f_c\,c,\qquad f_c\le1,$$
so the radiation step grows by $1/f_c$. Both
[M1 codes](/methods/m1-radiation-transport.md) in the bundle use it.

## Where $\hat c$ enters

* **Hyperion** ([Skinner & Ostriker (2013)](/sources/skinner-2013.md),
  §§2.1, 3.2) puts $\hat c$ only in the time derivatives,
  $\frac{1}{\hat c}\partial_t E_{\mathrm r}$ and
  $\frac{1}{\hat c}\partial_t(\mathbf F_{\mathrm r}/c)$. The true $c$
  stays in the source terms and in the ratio of flux to energy, so
  quasi-steady radiation fields do not depend on $\hat c$. With
  $\hat c\neq c$ total energy and momentum are **not** conserved; the
  conserved combinations are $E + (c/\hat c)E_{\mathrm r}$ and
  $\rho\mathbf v + (1/\hat c)\mathbf F_{\mathrm r}/c$.
* **RAMSES-RT** ([Rosdahl et al. (2013)](/sources/rosdahl-2013.md),
  §§4.1–4.2, 5.4, 6) uses the reduced light speed in the Courant
  condition, $\Delta t = 0.8\,h/(3\hat c)$ in the tests, with
  $f_c = 1/100$ by default. In super-comoving variables photons are
  over-diluted under the RSLA, and redshift dilution of photon energy is
  not included (§5.4).

## Validity criteria, side by side

The two sources derive criteria from different physics, and neither
compares its criterion with the other's.

| | [Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §4.2 | [Skinner & Ostriker (2013)](/sources/skinner-2013.md), §§3.2, 4.3.4 |
|---|---|---|
| Physics | propagation of an ionization front into neutral gas (Strömgren sphere with finite light speed) | ordering of radiation, diffusion and flow time scales; linear radiation-hydrodynamic waves |
| Criterion | $f_c = \min\left(1,\ \sim10\times\dfrac{\text{crossing time}}{\text{time scale simulated}}\right)$ | $\hat c$ much larger than the maximum gas signal speed times $\max\{1,\tau_{\max}\}$ (eq. 35) |
| Regime excluded | IGM reionization ($f_c = 1$ needed) | dynamic diffusion (RSLA "not viable") |

**Ionization-front criterion** (Rosdahl et al. 2013, §4.2, eqs. 32–33,
Fig. 2, Table 1). With finite light speed the I-front radius follows the
Shapiro et al. (2006) solution, governed by the ratio of the crossing
time to the recombination time. For any nonzero ratio the front joins the
infinite-light-speed solution after one crossing time. Reducing $c$ by
$f_c$ multiplies the effective ratio by $1/f_c$, which gives the recipe
above. Minimum admissible values (Table 1):

| Regime | minimum $f_c$ |
|---|---|
| Milky Way ISM | $3\times10^{-2}$ |
| Milky Way cloud | $6\times10^{-4}$ |
| Iliev et al. tests 1, 2, 5 | $2\times10^{-2}$ |
| Iliev et al. test 4 (IGM reionization) | 1 |

The text concludes that galaxy-scale ISM work tolerates
$f_c\simeq10^{-4}$–$10^{-3}$ (§4.3), while IGM reionization needs the true
$c$, better done on GPUs (with ATON). The paper's own numbers disagree:
Table 1 gives a minimum of $3\times10^{-2}$ for the Milky Way ISM, while
the text accepts $10^{-4}$–$10^{-3}$ for galaxy-scale ISM work (both
printed). Its default test value, $f_c = 1/100$, is also below the
Table 1 minimum ($2\times10^{-2}$) for Iliev tests 1, 2 and 5, which is
consistent with the early ionization-front lag those tests show.

**Time-scale criterion** (Skinner & Ostriker 2013, §3.2, eqs. 33–36). Two
conditions combine:
1. Newtonian limit: $\hat c$ much larger than the maximum gas signal
   speed (eq. 33).
2. Static diffusion: the ordering of time scales is preserved only if
   $\hat c$ exceeds that speed times the largest optical depth $\tau_{\max}$
   (eq. 34).

Equivalently, the radiation subcycles per gas step must exceed
$\max\{1,\tau_{\max}\}$ (eq. 36). In practice about 10 subcycles suffice
for optically thin problems and 10–100 for $\tau_{\max}\sim10$; the RSLA is
"generally" practical for optical depths $\lesssim10$ (§5).

**Linear-wave analysis** (Skinner & Ostriker 2013, §4.3.4, eqs. 87–93).
The dispersion relations, extended to include $\hat c$, show:
* When gas pressure dominates radiation pressure, acoustic modes are
  unaffected provided $\hat c$ much larger than the isothermal sound speed times $\max\{1,\tau_\lambda\}$, with
  $\tau_\lambda$ the optical depth across a wavelength.
* When radiation pressure dominates in the optically thick limit, the
  radiation-modified acoustic mode is **always** affected: its phase speed
  scales as $(\hat c/c)^{1/2} = f_c^{1/2}$ (eq. 91), correct only as
  $\hat c\to c$, so the algorithm is then feasible only with
  $\hat c\approx c$ and $c$ at most "10 or so" sound speeds.

## Observed effects

* **I-front lag.** The RSLA delays early ionization fronts: in the
  isothermal Strömgren test, the dense-clump test and the photo-evaporation
  test the front lags at first, for about 7 Myr in the last, then leads
  the reference code ([Rosdahl et al. (2013)](/sources/rosdahl-2013.md),
  §§6.2, 6.4, 6.8). In the cosmological test 4 the run with $f_c = 1$ lags
  C²-Ray and a run printed as $f_c = 100$ approaches it; the authors argue
  the infinite-$c$ codes give premature fronts (§6.5).
* **Radiation force.** In a radiation-driven dusty shell, maximum relative
  errors in mean radius and mean velocity grow from 3.1 % and 7.0 % at
  $\hat c$ equal to 860 isothermal sound speeds to 5.3 % and 13 % at 430 and 8.5 % and 23 % at 215; too
  small a $\hat c$ makes the radiation force too strong
  ([Skinner & Ostriker (2013)](/sources/skinner-2013.md), §4.3.6, Fig. 29).
* **Infeasible regimes.** The original parameters of the Krumholz et al.
  (2007) advected radiation pulse (optical depth 2900) cannot be run with
  the RSLA; the radiation pressure tube runs with $\hat c$ equal to 10 isothermal sound speeds at
  optical depth about $1.28\times10^3$, justified by a diffusion-to-sound
  time ratio of about 13
  ([Skinner & Ostriker (2013)](/sources/skinner-2013.md), §§4.3.2–4.3.3).

## Later uses (batch 3)

### Quokka: same placement, a closed-box bias

**Placement.** [Quokka](/software/quokka.md) writes the radiation
equations as
$\partial_t E_{\mathrm r} + \nabla\cdot(\frac{\hat c}{c}\mathbf F_{\mathrm r})$
and $\partial_t\mathbf F_{\mathrm r} + \nabla\cdot(c\hat c\,\mathsf P_{\mathrm r})$,
with $\hat c$ times the radiation four-force on the right
([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.1, eqs. 11–12).
Multiplied through by $\hat c$, Hyperion's form above is the same, so the
two codes place $\hat c$ alike: in the time derivatives only. Citing
[Skinner & Ostriker (2013)](/sources/skinner-2013.md), the paper states
that with $\hat c\neq c$ neither total energy nor momentum is conserved
(§2.1). Quokka subcycles the explicit radiation inside each hydro step
(§2.2).

**Closed-box equilibrium** (§3.2.3, eqs. 57–58, Fig. 11). With a gas heat
capacity proportional to $T^3$, a closed, uniform box conserves
$\rho e + (c/\hat c)E_{\mathrm r}$, not $\rho e + E_{\mathrm r}$. The
equilibrium temperature it reaches therefore depends on $\hat c$ whenever
$\hat c\neq c$. In the radiation–matter exchange test (after Turner &
Stone 2001; initial $E_{\mathrm r} = 10^{12}$ and gas energy $10^2$ erg
cm⁻³, $\rho = 10^{-7}$ g cm⁻³) the code matches the exact solution of
the modified system to better than one part in $10^5$ per step, and with
$\hat c = 0.1c$ ($f_c = 0.1$) the equilibrium temperature is about 20 %
higher than the physical one. The authors call this "a generic failing of
the RSLA" and present it as "contrary to previous claims in the
literature", without naming those claims.

**How this relates to Hyperion's statement.**
[Skinner & Ostriker (2013)](/sources/skinner-2013.md), §2.1, state that
quasi-steady radiation fields do not depend on $\hat c$, because $\hat c$
multiplies only the time derivatives; they also give the conserved
combination $E + (c/\hat c)E_{\mathrm r}$ (above). Quokka's result follows
from that same combination: the steady-state equations do not contain
$\hat c$, but which steady state a closed system reaches is fixed by the
conserved combination, which does. The two statements concern different
things (the form of the steady equations against the end state of an
isolated system). Quokka's own reconciliation is the same: with open
boundaries that do not conserve the combination, the correct steady state
is reached (§3.3, §5.1). Because Quokka presents its result as contrary to
earlier claims, the disagreement is kept open under Contradictions, with
this reconciliation as the proposed resolution.

**Open-boundary runs** ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3.3).
* Radiation pressure tube (Krumholz et al. 2007): $\hat c$ equal to 10
  initial sound speeds, about $4.03\times10^8$ cm s⁻¹, optical depth per
  cell about $10^2$; agreement with the diffusion solution better than
  0.2 % (§3.3.1, Fig. 14). Skinner & Ostriker use the same factor of 10
  for this test (above).
* Optically thin radiation-driven wind with $\hat c$ equal to 10 times a
  flow Mach number of the solution times the isothermal sound speed
  (§3.3.2).
* [Subcritical radiative shock](/benchmarks/subcritical-radiative-shock.md)
  with $\hat c$ equal to 10 times the upstream velocity plus sound speed
  (§3.3.3).
* Radiation-driven dust shell with $\hat c$ equal to 860 sound speeds, the
  largest value Skinner & Ostriker use (§3.3.4).

**Validity** (§5.1). $\hat c$ must exceed the speed of the fastest
radiation-driven fronts in streaming problems, and about $c$ divided by
the optical depth in diffusion problems; following Skinner & Ostriker
(2013), no constant $\hat c$ preserves the ordering of hydrodynamic,
diffusion and reduced light speeds everywhere. This agrees with the
time-scale criterion above. The paper also drops the velocity terms of
order velocity over light speed times optical depth beyond the flux term,
because they matter only where that product reaches one, where the
approximation cannot be used (§2.1); this matches the dynamic-diffusion
exclusion in the table above.

## Contradictions

* **Do quasi-steady states depend on $\hat c$?** *Open.*
  [Skinner & Ostriker (2013)](/sources/skinner-2013.md), §2.1: quasi-steady
  radiation fields do not depend on $\hat c$, which multiplies only the
  time derivatives. [Wibking & Krumholz (2022)](/sources/wibking-2022.md),
  §3.2.3: in a closed box the equilibrium temperature does depend on
  $\hat c$ (about 20 % too high at $f_c = 0.1$), "contrary to previous
  claims in the literature". *Proposed resolution (compiler, not a
  closure):* the steady equations are $\hat c$-free, but a closed system
  conserves $E + (c/\hat c)E_{\mathrm r}$, which fixes which steady state
  it reaches; Skinner & Ostriker give the same conserved combination. The
  entry closes by a source that states this, or by the human.

# Citations

1. [Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §§4.1–4.3, 5.4, 6.2, 6.4, 6.5, 6.8 (arXiv v2).
2. [Skinner & Ostriker (2013)](/sources/skinner-2013.md), §§2.1, 3.1–3.2, 4.3.2–4.3.6, 5 (arXiv v1).
3. [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §§2.1–2.2, 3.2.3, 3.3, 5.1 (arXiv v2).

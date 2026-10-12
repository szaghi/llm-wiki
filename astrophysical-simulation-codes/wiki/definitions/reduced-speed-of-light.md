---
type: Definition
title: "Reduced speed of light approximation"
description: "Replacing the speed of light c by a smaller ĉ = f_c c in the time derivatives of explicit radiation moment equations to relax the light-speed time step, with two validity criteria: one from ionization-front propagation (RAMSES-RT) and one from time-scale ordering in the streaming and static-diffusion regimes (Hyperion)."
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

# Citations

1. [Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §§4.1–4.3, 5.4, 6.2, 6.4, 6.5, 6.8 (arXiv v2).
2. [Skinner & Ostriker (2013)](/sources/skinner-2013.md), §§2.1, 3.1–3.2, 4.3.2–4.3.6, 5 (arXiv v1).

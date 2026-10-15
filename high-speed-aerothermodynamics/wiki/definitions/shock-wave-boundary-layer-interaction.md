---
type: Definition
title: "Shock-wave/boundary-layer interaction"
description: "Interaction of an incident, ramp-, jet- or duct-generated shock with a wall boundary layer, classed as laminar steady, laminar unsteady, transitional or turbulent by steadiness, dimensionality and spectrum, with the separation and peak-heating correlations used to size it."
status: established
aliases: [SWBLI, SBLI, SWTBLI, shock/boundary-layer interaction, shock wave turbulent boundary layer interaction]
tags: [swbli, separation, aeroheating, transition, inlet, isolator, jet-in-crossflow]
timestamp: 2026-10-14T00:00:00Z
---

# Shock-wave/boundary-layer interaction

A shock-wave/boundary-layer interaction (SWBLI) is the coupled flow that
forms where a shock meets a wall boundary layer: the pressure rise across
the shock is fed upstream through the subsonic part of the boundary layer,
the layer thickens or separates, and the separation in turn generates its
own shocks. The interaction raises local pressure and wall heat flux
$q_w$ and is the governing local flow of compression ramps, flares,
inlet cowls and isolators, and of the region around a transverse jet.

## Four-class categorisation

[Knight & Mortazavi (2018)](/sources/knight-2018.md), §1, Table 1, present
as "the general consensus" a classification by steadiness, dimensionality
and power spectrum:

| Class | Steadiness | Dimensionality | Spectrum |
|---|---|---|---|
| Laminar steady | steady | 2-D/axisymmetric or 3-D | — |
| Laminar unsteady | unsteady | 2-D or 3-D | discrete frequencies |
| Transitional | unsteady | 3-D | discrete frequencies with a developing cascade to higher frequency, typically with downstream distance |
| Turbulent | unsteady | 3-D | broad spectrum |

The class follows the state of the incoming boundary layer at the
interaction: in the reviewed Mach-6 flat-plate data the same 4°
wedge-generated shock gives transitional interactions at the two lower
impingement Reynolds numbers and a turbulent one at the highest (§2.7,
Table 9), and the impingement-station intermittency organises the peak
heating (§2.9, §2.10). The review
illustrates the classes with spectra (Figs. 1–3) and schlieren images
(Fig. 4: laminar and transitional with a 4° wedge, turbulent with an 18°
ramp). Transitional interactions can carry the largest peak heating of the
four; see [Peak heating of transitional shock/boundary-layer interactions](/results/transitional-swbli-peak-heating.md).

Further observations attributed in the same review:

* **Unsteadiness of the shock foot.** For a cylinder-induced interaction at
  $\mathrm{Ma}_\infty=2.01$, the probability densities of the forward-shock
  and upstream-influence positions are significantly broader for
  transitional inflow than for turbulent inflow; at one transitional
  station the separation-location distribution has skewness −1.88 and
  kurtosis 6.99, implying large upstream excursions (§2.12, Figs. 35–37,
  Lash et al. / Combs et al.).
* **Upstream separation distance.** For cylinder-induced interactions the
  normalised separation distance decreases monotonically from laminar
  through transitional to turbulent inflow; for turbulent inflow
  separation sits about two diameters ahead of the cylinder (§2.6,
  Fig. 20, Murphree et al.). The review normalises the Fig. 20 ordinate
  inconsistently: the text and caption give the separation distance over
  the boundary-layer thickness, while the plotted axis label gives it over
  the cylinder diameter.
* **Görtler vortices** on the concave flare surface are the excess-heating
  mechanism proposed by the original authors of the hollow-cylinder flare
  data (§2.5, Fig. 16).

## Correlations

All correlations below are attributed by [Knight & Mortazavi (2018)](/sources/knight-2018.md);
the review tests them only against the data it collects. Here
$q_{w,\max}$ is the peak wall heat flux in the interaction,
$q_{w,\mathrm{ref}}$ the undisturbed (reference) wall heat flux upstream,
$p_2/p_1$ the inviscid surface pressure ratio across the interaction and
$p_{\max}/p_\infty$ the peak interaction pressure ratio.

### Roberts separation length

$$\frac{L_{\mathrm{sep}}\,\mathrm{Ma}_\infty^{3/2}}{\text{flat-plate transition length}}\approx\sqrt{\frac{p_2}{p_1}}$$

(§2.1, Eq. 1, attributed to Roberts). The Heffner et al. hollow-cylinder
flare data at flare angles 10°, 20° and 30°, $\mathrm{Ma}_\infty=4.96$,
"generally overpredict the correlation but show the same trend" (Fig. 5).

### Hung–Barnett peak heating

$$\begin{aligned}
\text{laminar:}\quad & q_{w,\max}/q_{w,\mathrm{ref}} = 0.13\,(p_2/p_1)^{1.13},\\
\text{transitional:}\quad & q_{w,\max}/q_{w,\mathrm{ref}} = 0.468\,(\mathrm{Re}_L\times10^{-6})\,(p_2/p_1)^{1.13},\\
\text{turbulent:}\quad & q_{w,\max}/q_{w,\mathrm{ref}} = (p_2/p_1)^{0.80},
\end{aligned}$$

with the laminar reference heat flux in the first two and the turbulent
one in the third (§2.1, Eqs. 2–4). $\mathrm{Re}_L$ is a Reynolds number
based on a length $L$ that the review does not define for the
correlation; in the hollow-cylinder flare data it compares against
(§2.5) $L$ is the length of the cylinder ahead of the flare. Against the Heffner data (Fig. 6) the
transitional form underpredicts the peak and the turbulent form agrees
more closely.

### Holden turbulent peak heating

$$\frac{q_{w,\max}}{q_{w,\mathrm{ref}}}=\left(\frac{p_{\max}}{p_\infty}\right)^{0.85}$$

(§2.5, Eq. 5). With a trip forcing a fully turbulent inflow the
hollow-cylinder flare peak agreed closely with it; with natural
transition the measured peak was on average 3.4 times larger (§2.5,
Table 6). It is the baseline against which the transitional excess is
measured in two of the reviewed datasets (Tables 6, 9).

### Schülein intermittency correlation

The intermittency of the incoming layer at the impingement station is
defined from three Stanton numbers $\mathrm{St}$: the value measured at
the impingement station without the shock (the impinging value), the
laminar value, and a transitional reference value set to 5.5 times the
laminar one. The intermittency is the impinging value minus the laminar
value, divided by the transitional reference minus the laminar value
(§2.10, Eqs. 9–10, Fig. 30). The peak Stanton number of the interaction, relative
to the case without shock, is largest at an intermittency of about 0.1
(early transition), nearly three times its value for a fully turbulent
inflow.

### Shock/shock interactions

For Edney type III/IV shock/shock interactions the peak heating ratio is
below 10 for $\mathrm{Re}_D<10^4$ (a Reynolds number on a length $D$
the review does not define, presumably the body diameter) and rises rapidly above it, with a sharp
increase at a shear-layer Reynolds number of about 2000 (§2.3, Fig. 11,
attributed to Holden et al.; the rise is "presumably" transition of the
shear layer or attaching jet).

## Interactions in inlets and isolators

* **Inward-turning compression.** [Zuo & Huang (2018)](/sources/zuo-2018.md),
  §2.4, argue qualitatively that an inward-turning compression
  makes the interaction harder than a planar one: the wall pressure rises
  continuously with no constant-pressure plateau before the reflected
  shock, and the pressure ahead of the reflected shock is about twice the
  planar value (§2.3.4, Fig. 6); the boundary-layer profile at the
  shoulder is "much more shrunken" (Fig. 7, a k–ε computation) and the
  adverse pressure gradient is strongest near the centreline (Fig. 8). See
  [Inward-turning intake design](/methods/inward-turning-intake-design.md);
  the control they apply is [boundary-layer bleed](/methods/boundary-layer-bleed.md).
* **Cowl-shock impingement and unstart.** In the started two-ramp inlet of
  [Liu H. et al. (2018)](/sources/liu-2018-d.md), §5.1, the cowl shock
  impinges just after the throat with a small separation and a weak
  separation shock; in the unstarted state a large separation bubble with
  a strong separation shock sits upstream of the throat. Near these
  separation bubbles all five uncertain inputs (Mach number, unit Reynolds
  number, angle of attack, freestream and wall temperature) have
  comparable Sobol' indices for the wall pressure coefficient (§5.3,
  Fig. 18). See [Inlet start, unstart and hysteresis](/definitions/inlet-start-and-unstart.md).
* **Shock trains.** In back-pressured curved isolators the shock train is
  asymmetric and its large-scale separation switches from the bottom wall
  to the top wall without any change of boundary conditions
  ([Meng et al. (2018)](/sources/meng-2018.md), §4.3, Figs. 13–14); see
  [Isolator and shock train](/definitions/isolator-shock-train.md).

## Interactions behind a transverse jet

Behind a sonic jet in a $\mathrm{Ma}_\infty=2.95$ crossflow, the shocks
produced where the flows wrapping around the jet collide ("collision
shocks") interact with the wall boundary layer and induce a V-shaped
separation zone whose separation lines end on a slip line
([Liu Y. et al. (2018)](/sources/liu-2018-c.md), §3, Figs. 8–9). The
included angle of the V is 33.2°–34.5° and is stated to be independent of
$J$; the separation length grows as a power law in $J$. These authors
distinguish this zone, by mechanism and position, from the horseshoe
separation induced upstream by the jet bow shock. See
[Transverse jet in supersonic crossflow](/definitions/jet-in-supersonic-crossflow.md).

## Standard test configurations

The canonical configurations collected by [Knight & Mortazavi (2018)](/sources/knight-2018.md),
§§2.1–2.14, each with a freestream-condition table:

| Configuration | Representative study | $\mathrm{Ma}_\infty$ | Section |
|---|---|---|---|
| Hollow cylinder with flare (10°/20°/30°; 15°) | Heffner et al. 1993; Benay et al. 2006 / Bur & Chanetz 2009 | 4.96; 5 | §2.1, §2.5 |
| Curved compression ramp (5° + 5° + 10°) | Holden & Chadwick 1995 | 10.0–11.94 | §2.2 |
| Flat plate with 5.5° compression corner (computational) | Balakumar et al. 2005 | 5.373 | §2.4 |
| Cylinder normal to a flat plate | Murphree et al. 2006/07; Lash et al. 2016/17; Leidy et al. 2017 (with upstream protuberance) | 5; 2.01; 6.0 and 7.0 | §2.6, §2.12, §2.14 |
| Oblique shock impinging on a flat plate (4° generator) | Willems et al. 2013/15; Sandham et al. 2014; Schülein 2014 | 5.7–6 | §2.7, §2.9, §2.10 |
| Hemisphere-cylinder with 8° flare | Estruch-Samper et al. / Vanstone et al. | 8.9 | §2.8 |
| 7° sliced cone with 30° ramp, quiet and noisy freestream | Edelman et al. 2016 / Gray et al. 2017 | 5.8–6.0 | §2.11 |
| Flat plate with sharp or blunt leading edge and weak N-wave shock | Vaganov et al. 2016 | 2.5 | §2.13 |
| Edney III/IV shock/shock | Holden et al. 1998 | — | §2.3 |

The review names the facilities RWG, H2K, HEG, the Boeing/AFOSR Mach-6
Quiet Tunnel and T-325, and calls for study of transitional interactions
at transonic and low supersonic Mach numbers (§3).

# Citations

1. [Knight & Mortazavi (2018)](/sources/knight-2018.md), §1 (Table 1, Figs. 1–4), §§2.1–2.14 (Eqs. 1–5, 9–10; Tables 2–15; Figs. 5–41), §3.
2. [Zuo & Huang (2018)](/sources/zuo-2018.md), §2.3.4 (Fig. 6), §2.4 (Figs. 7–8).
3. [Liu H. et al. (2018)](/sources/liu-2018-d.md), §5.1 (Figs. 11–12), §5.3 (Fig. 18).
4. [Meng et al. (2018)](/sources/meng-2018.md), §4.3 (Figs. 13–14).
5. [Liu Y. et al. (2018)](/sources/liu-2018-c.md), §3 (Figs. 8–9, 11).

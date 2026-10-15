---
type: Result
title: "Peak heating of transitional shock/boundary-layer interactions"
description: "A shock interacting with a transitional boundary layer can produce a peak wall heat flux well above both the laminar and the fully turbulent interaction of the same strength, about 2.2–3.7 times the Holden turbulent correlation (mean 3.4 on the hollow-cylinder flare) in the reviewed hypersonic datasets."
status: established
aliases: [transitional SWBLI heating overshoot, SWTBLI peak heating]
tags: [swbli, aeroheating, transition, correlation, dns]
timestamp: 2026-10-14T00:00:00Z
---

# Peak heating of transitional shock/boundary-layer interactions

**Statement.** In a [shock-wave/boundary-layer interaction](/definitions/shock-wave-boundary-layer-interaction.md)
whose incoming boundary layer is transitional, the peak wall heat flux
$q_{w,\max}$ can exceed both the laminar and the fully turbulent
interaction peaks at the same imposed pressure rise. Turbulent-interaction
correlations therefore do not bound the heating. This is the central
message of the review of [Knight & Mortazavi (2018)](/sources/knight-2018.md)
(abstract, §3), built on the experiments and DNS listed below; each number
is from the cited work as reported in the review, not from a new
measurement. Here $q_{w,\mathrm{ref}}$ is the undisturbed wall heat flux
upstream and the Holden correlation is
$q_{w,\max}/q_{w,\mathrm{ref}}=(p_{\max}/p_\infty)^{0.85}$ (§2.5, Eq. 5).

## Evidence

| Configuration | Data | Excess over turbulent level | Section |
|---|---|---|---|
| Hollow cylinder + 15° flare, $\mathrm{Ma}_\infty=5$, natural transition (Benay et al. / Bur & Chanetz) | $q_{w,\max}/q_{w,\mathrm{ref}}=12.4$–$14.5$ over $\mathrm{Re}_L=0.405$–$2.031\times10^6$ (length scale $L$ = the 252 mm cylinder ahead of the flare), against 3.9 from Holden | 3.2–3.7, mean 3.4 (Table 6); consistent with Longo | §2.5, Table 6 |
| Same model, trip forcing a fully turbulent inflow | close to Holden | none | §2.5 |
| Oblique shock (4° wedge) on a flat plate, $\mathrm{Ma}_\infty=6$, impingement at 331 mm (Willems et al.) | $q_{w,\max}/q_{w,\mathrm{ref}}=8.1$, 5.4, 2.8 at impingement Reynolds numbers 1, 2 and $4\times10^6$; Holden gives 2.5 with inviscid $p_{\max}/p_\infty=2.96$ | 3.2, 2.2, 1.1: transitional at the two lower Reynolds numbers, turbulent at the highest | §2.7, Table 9 |
| Oblique shock on a flat plate, $\mathrm{Ma}_\infty\approx6$ (Schülein) | peak Stanton number relative to the no-shock case against incoming-layer intermittency | about 3 times the fully turbulent peak at intermittency about 0.1 | §2.10, Eqs. 9–10, Fig. 30 |
| Oblique shock on a flat plate, DNS plus RWG/H2K experiment (Sandham et al.) | peak $\mathrm{St}$ relative to the laminar value against an intermittency factor, turbulent level from Van Driest II | peak reached when the layer is transitional at the impingement station | §2.9, Fig. 28(b) |
| Edney III/IV shock/shock (Holden et al.) | peak heating ratio below 10 for $\mathrm{Re}_D<10^4$ (length scale $D$, not defined in the review; presumably the body diameter), rising rapidly above, sharp increase at shear-layer Reynolds number about 2000 | attributed "presumably" to transition of the shear layer or attaching jet | §2.3, Fig. 11 |
| Cylinder with upstream protuberance, $\mathrm{Ma}_\infty=6$ (Leidy et al.) | no-protuberance peak rises from unit Reynolds number $2.9$ to $4.3\times10^6$ m⁻¹ and falls at $6.5\times10^6$ m⁻¹ | read as laminar → transitional → turbulent inflow | §2.14, Fig. 41 |

The Hung–Barnett transitional correlation underpredicts the transitional
peak of the Heffner et al. hollow-cylinder flare data (§2.1, Eq. 3,
Fig. 6). Two related observations in the review: turbulent spots carry
4–5 times the laminar heat transfer (§2.8, $\mathrm{Ma}_\infty=8.9$), and
on a 7° sliced cone with a 30° ramp the noisy-freestream peak ramp heat
transfer is about one half of the quiet-freestream level, transition then
occurring upstream on the cone (§2.11, Fig. 32).

## Mechanism

No single mechanism is established. For the hollow-cylinder flare the
original authors attribute the excess to Görtler vortices (§2.5, Fig. 16).
Laminar axisymmetric Navier–Stokes computations substantially underpredict
that peak, and the maximum linear-stability N-factor found was 1.0
against the 2–4 associated with transition in that tunnel (§2.5,
Fig. 17).

## Prediction

The review judges DNS the most promising prediction method: it "has
successfully reproduced experimental surface heat transfer
distributions" (§3). Its limitation is the inflow. The Sandham et al. DNS
(8 runs, $2401\times232\times360$ grid) imposed a random density
perturbation on the laminar similarity profile, with an amplitude tuned
*a posteriori* to the experiment and different for RWG and H2K; at a unit
Reynolds number of $4\times10^6$ m⁻¹ only the high-amplitude run agreed
with RWG (§2.9, Eq. 6, Fig. 27). Matching without tuning would require
time-dependent inflow data for five variables (three velocity components
and two thermodynamic variables), which cannot presently be measured. The
review names dynamic inflow boundary conditions as the open problem and
calls for collaborative work on them (§3).

# Citations

1. [Knight & Mortazavi (2018)](/sources/knight-2018.md), abstract; §2.1 (Eq. 3, Fig. 6); §2.3 (Fig. 11); §2.5 (Eq. 5, Table 6, Figs. 16–17); §2.7 (Table 9); §2.8; §2.9 (Eq. 6, Figs. 27–28); §2.10 (Eqs. 9–10, Fig. 30); §2.11 (Fig. 32); §2.14 (Fig. 41); §3.

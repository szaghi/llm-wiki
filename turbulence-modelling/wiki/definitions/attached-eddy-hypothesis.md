---
type: Definition
title: "Attached-eddy hypothesis"
description: "The attached-eddy hypothesis models the logarithmic region of wall turbulence as a hierarchy of self-similar eddies whose size scales with wall distance; this page gives the consequences the sources test (logarithmic normal stresses, inverse-wavenumber spectra, uniform momentum zones, inactive motions) and where compressible DNS up to Mach 11 depart from them."
status: established
aliases: [attached eddy model, attached-eddy model, Townsend's attached eddies, wall-attached eddies, inactive motions, uniform momentum zones]
tags: [boundary-layer, dns, compressible, hypersonic]
timestamp: 2026-10-27T10:57:00Z
---

# Attached-eddy hypothesis

The **attached-eddy hypothesis** describes the logarithmic region of
wall-bounded turbulence as populated by a hierarchy of energy-containing
eddies "attached" to the wall, each with a size proportional to its distance
from the wall. In the words of [Cogo et al. (2022)](/sources/cogo-2022.md),
§5.4, "according to the classical theory (Prandtl 1925) and to the
predictions of the attached eddies model (Perry & Marušić 1995), the typical
size of the energetic eddies is proportional to their distance from the
wall", $l_m=\kappa y$, which under a constant-stress layer leads directly to
the logarithmic [law of the wall](/definitions/law-of-the-wall.md). The
sources of this bundle do not state the hypothesis formally; they invoke it,
with Perry & Li (1990), Perry & Marušić (1995) and the review of Marusic &
Monty (2019), for the consequences listed below, and use them as diagnostics
of how far compressible [boundary layers](/benchmarks/turbulent-boundary-layer.md)
behave like incompressible ones (compare
[Morkovin's hypothesis](/definitions/morkovin-hypothesis.md)).

Huang et al. (2022) write $z$ wall-normal and $y$ spanwise; both are swapped
here to the registry's $y$ wall-normal and $z$ spanwise. $\lambda_x$,
$\lambda_z$ are streamwise and spanwise wavelengths, $k_z=2\pi/\lambda_z$ the
spanwise wavenumber (page-local).

## Consequences used as diagnostics

**Logarithmic decay of the wall-parallel normal stresses.** "Consistent with
the prediction of the attached eddy hypothesis",
[Huang et al. (2022)](/sources/huang-2022.md), §4.2, Eq. (4.8), fit the
streamwise ($i=1$) and spanwise ($i=3$; the source's $i=2$) normal stresses in
[Morkovin scaling](/definitions/morkovin-hypothesis.md) at $Re_\tau=1172$ by
$$\frac{\langle\rho u_i''u_i''\rangle}{\tau_w}=B_i-A_i\log(y/\delta)$$
(no sum over $i$; page-local $A_i$, $B_i$, with $B_i$ not the log-law
intercept $B$; the base of the logarithm is not printed). For the
quasi-adiabatic cases at Mach 2.5 and 4.9 they find $B_1=2.39$, $A_1=1.03$,
"the same as those reported in Pirozzoli & Bernardini (2011)", and a common
spanwise slope $A_3=0.27$ (as Baidya et al. 2021) with $B_3$ from 1.5 at
Mach 2.5 to 1.3 at Mach 4.9.

**Plateau of the wall-normal stress and the shear stress.** Again
"consistent with the attached eddy hypothesis", the wall-normal normal
stress has a near-wall plateau at $Re_\tau=1172$, narrower in the Mach 10.9
case, and the Reynolds shear stress of that case has a plateau over
$15\lesssim y^*\lesssim1000$ that widens with Reynolds number (Huang et al.
2022, §4.2, Figs. 13–14). Cogo et al. (2022, §5.1) read the corresponding
plateau of the wall-normal stress and the shear stress at Mach 2 as "the
formation of an equilibrium layer", without a significant Mach effect in the
supersonic regime.

**Inverse-wavenumber spectra.** The premultiplied spanwise spectra of the
streamwise velocity of the quasi-adiabatic cases show a local plateau near
$\lambda_z^*\approx1000$, "indicative of a $k_z^{-1}$ scaling associated
with the attached eddy hypothesis" (Huang et al. 2022, §5, Fig. 21).

**Inactive motions.** Large outer eddies induce wall-parallel velocity
fluctuations near the wall without contributing to the shear stress. They
are "expected to induce a logarithmic growth with $Re_\tau$ of both $u$ and
$w$" near the wall in the low-speed regime, which Cogo et al. (2022, §5.1,
Fig. 10) confirm in the supersonic regime; Huang et al. (2022, §4.2)
attribute the slight rise of the near-wall stress peaks with Reynolds number
to "the increased influence of the inactive outer modes". Cogo et al.
(2022, §5.2) relate the excess production they find farther out in the
hypersonic log layer to the argument of Pirozzoli et al. (2021) that excess
log-layer production feeds inactive motions, which do not contribute to the
shear stress but transfer energy elsewhere.

**Uniform momentum zones.** A uniform zone of a quantity is a region of the
$x$–$y$ plane with small wall-normal variation, detected as a local peak in
the histogram of the sampled values, with histogram minima marking sharp
gradients between zones (Cogo et al. 2022, §3.2, after De Silva et al.
2016). Their existence is attributed to the hierarchical distribution of
coherent structures and is "closely related to the fundamental hypothesis of
the attached eddy model", which has been used to reproduce statistics and to
generate synthetic instantaneous fields (as recalled there). Cogo et al.
confirm uniform zones of streamwise velocity at $Re_\tau\approx2000$ at
Mach 2 and 5.86 and report uniform **temperature** zones for the first time:
mean counts 3.6 and 2.5 for velocity, 5.9 and 4.9 for temperature, fewer at
the higher Mach number (84 planes per case, histogram bin $0.5u_\tau$, peak
prominence $0.1$ of the maximum, tuned to De Silva et al.'s velocity count).
The temperature arrangement supports Pirozzoli & Bernardini's view of
temperature as an "attached variable"; whether the zone count grows
logarithmically with $Re_\tau$ needs data over more than a decade of
$Re_\tau$. No clear zones are found for the total temperature.

**Eddy-size scale.** From an eddy-viscosity ansatz, Pirozzoli (2012), adapted
to compressible flow by Modesti & Pirozzoli (2016), as recalled by Cogo et
al. (2022, §5.4, Eq. 5.9), define an eddy-size scale
$l_{12}^*\sim(u_\tau\delta)\,(\partial_y\langle u\rangle_{VD})^{-1/2}$ from
the van Driest-transformed mean shear; Cogo et al. propose replacing it by
the shear of the total-stress-based transformation of Griffin et al. (2021)
(Eq. 5.10; see [compressible velocity transformations](/definitions/compressible-velocity-transformation.md)).
Normalizing $\lambda_z$ by $l_{12}^*$ collapses the velocity and temperature
spectra at $y/\delta=0.2$–$0.8$ better than $\delta$, and the new scale
slightly better still, especially at Mach 5.86 (Figs. 15–16).

## Eddy size as the argument for wall modelling

In passing, the WMLES review of [Bose & Park (2018)](/sources/bose-2018.md)
(§1, Fig. 1) states, after Jiménez (2012) as cited, that near the edge of the
buffer layer the near-wall eddies are of spanwise size $O(10^2)$ wall units
and grow linearly with wall distance, so that they shrink relative to
$\delta$ as $Re_\tau$ grows and a grid that resolves them becomes
prohibitive (see [wall-modelled LES](/methods/wall-modelled-les.md) and
[grid-point requirements](/results/les-grid-point-requirements.md)). The
review does not name the attached-eddy hypothesis.

## Departures under strong wall cooling

Huang et al. (2022) find that the Mach 10.9 boundary layer with
$T_w/T_r=0.20$ shows none of the above signatures up to $Re_\tau=1172$
($Re_\tau^*$ about 6200): no logarithmic region of the streamwise stress, no
$k_z^{-1}$ plateau, no outer spectral peak (which sits at
$y/\delta\approx0.22$, $\lambda_z/\delta\approx0.8$ in the quasi-adiabatic
cases), an inner spectral peak higher in outer units, and no outer peak in
the spanwise spectrum of the wall shear stress, which they read as a
weakened inner–outer interaction (§4.2, §5, Figs. 21–26). Their explanation:
"the strong wall cooling … tends to reduce the scale separation between the
large and small turbulence scales, diminishing an overlap region wherein the
attached eddy model is valid, even at Reynolds numbers as high as
$Re_\tau=1172$" (§5). The van Driest log-law diagnostic of the same case also
has no wide constant region (§4.1, Fig. 11). Superstructures longer than
$10\delta$ are nevertheless present at all three Mach numbers (§5), as they
are in the cooled Mach 2 and 5.86 cases of Cogo et al. (2022, §3.1).

## Qualifications

- Neither source tests the hypothesis itself; both report DNS features they
  call consistent or inconsistent with it, at $Re_\tau$ up to about 2000
  (Cogo et al.) and 1200 (Huang et al.).
- Cogo et al. (2022) print Eqs. (5.9)–(5.10) as
  $l_{12}^*\sim(u_\tau\delta)(\partial\tilde u/\partial y)^{-1/2}$; as
  printed the right-hand side is not a length, which requires the factor
  $(u_\tau\delta)^{1/2}$ *(compiler check, not in the sources)*; the cited
  Pirozzoli (2012) form is not in the bundle.
- Huang et al. (2022, §4.2) print the range of their $B_2$ (here $B_3$) as ending at "M5Tw020", a
  case that does not exist; the sentence concerns the quasi-adiabatic Mach
  4.9 case M5Tw091.

# Citations

- [Cogo et al. (2022)](/sources/cogo-2022.md) — §3.1 (superstructures); §3.2, Figs. 6–7 (uniform momentum and temperature zones, attached-eddy model); §5.1, Fig. 10 (inactive motions, equilibrium layer); §5.2; §5.4, Eqs. (5.9)–(5.10), Figs. 15–16 (eddy-size scale).
- [Huang et al. (2022)](/sources/huang-2022.md) — §4.1, Fig. 11; §4.2, Eq. (4.8), Figs. 13–14 (logarithmic stresses, plateaus, inactive modes); §5, Figs. 21–26 (spectra, scale separation under cooling).
- [Bose & Park (2018)](/sources/bose-2018.md) — §1, Fig. 1 (eddy size and WMLES resolution; passing mention).

---
type: Definition
title: "Attached-eddy hypothesis"
description: "The attached-eddy hypothesis models the logarithmic region of wall turbulence as a hierarchy of self-similar eddies whose size scales with wall distance; this page gives the consequences the sources test (logarithmic normal stresses, inverse-wavenumber spectra, uniform momentum zones, inactive motions) and where compressible DNS up to Mach 11 depart from them."
status: established
aliases: [attached eddy model, attached-eddy model, Townsend's attached eddies, wall-attached eddies, inactive motions, uniform momentum zones]
tags: [boundary-layer, dns, compressible, hypersonic]
timestamp: 2026-10-28T12:22:00Z
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
the attached eddy model", which, Cogo et al. note citing Perry & Marušić
(1995) and De Silva et al. (2016), has been shown to reproduce flow
statistics and to generate synthetic instantaneous velocity fields. Cogo et al.
confirm uniform zones of streamwise velocity at $Re_\tau\approx2000$ at
Mach 2 and 5.86 and report uniform **temperature** zones for the first time:
mean counts 3.6 and 2.5 for velocity, 5.9 and 4.9 for temperature, fewer at
the higher Mach number (84 planes per case, histogram bin $0.5u_\tau$, peak
prominence $0.1$ of the maximum, tuned to De Silva et al.'s velocity count).
The temperature arrangement supports Pirozzoli & Bernardini's view of
temperature as an "attached variable"; whether the zone count grows
logarithmically with $Re_\tau$ needs data over more than a decade of
$Re_\tau$. No clear zones are found for the total temperature.

**Eddy-size scale.** Cogo et al. (2022, §5.4, Eq. 5.9) cite an eddy-size
scale that Pirozzoli (2012) derives from an eddy-viscosity ansatz and
Modesti & Pirozzoli (2016) adapt to compressible flow,
$l_{12}^*\sim(u_\tau\delta)\,(\partial_y\langle u\rangle_{VD})^{-1/2}$ from
the van Driest-transformed mean shear; Cogo et al. propose replacing it by
the shear of the total-stress-based transformation of Griffin et al. (2021)
(Eq. 5.10; see [compressible velocity transformations](/definitions/compressible-velocity-transformation.md)).
Normalizing $\lambda_z$ by $l_{12}^*$ collapses the velocity and temperature
spectra at $y/\delta=0.2$–$0.8$ better than $\delta$, and the new scale
slightly better still, especially at Mach 5.86 (Figs. 15–16).

## The incompressible picture in a boundary-layer review

The review of [Devenport & Lowe (2022)](/sources/devenport-2022.md), §2.2,
places the hypothesis (Townsend; Perry & Chong, as cited) in the
incompressible zero-pressure-gradient boundary layer and lists what it
predicts: the log law, the spectral slope, a logarithmic decrease of the
wall-parallel normal stresses with wall distance and a constant wall-normal
stress, predictions the review calls confirmed. It ties the hypothesis to
the **inactive motion** of Townsend and Bradshaw (1967): low-frequency
large-scale motion that contributes to $R_{11}$ and $R_{33}$ but not to
$R_{22}$ or $R_{12}$. The review attributes the growth with $\log Re$ of
the inner peak of $R_{11}/u_\tau^2$ near $y^+\approx15$ to the near-wall
footprint of these inactive outer motions, and notes amplitude modulation
of the near-wall cycle by the outer motion (Mathis et al., as cited), with
the outer peak of $R_{11}$ at streamwise wavelengths of 2–4 $\delta$ (§2.2,
Figs. 4–6, from cited experiments). It lists four families of coherent
structure after Smits et al.: near-wall streaks and quasi-streamwise
vortices (spanwise spacing about 100 wall units, length about 1000),
hairpins inclined at about $45^\circ$, large-scale motions of 2–3 $\delta$,
and very-large-scale motions or superstructures about ten times longer.
The review also cites Marusic & Perry's eddy types A and B (and C) as the
attached-eddy account of pressure-gradient history effects in adverse
pressure gradient (see the [wall law in adverse pressure
gradient](/definitions/adverse-pressure-gradient-wall-law.md)). The review
covers only incompressible layers; the supersonic test of the inactive-motion
growth is that of Cogo et al. (2022, §5.1) above.

## Eddy size as the argument for wall modelling

In passing, the WMLES review of [Bose & Park (2018)](/sources/bose-2018.md)
(§1, Fig. 1) states, after Jiménez (2012) as cited, that near the edge of the
buffer layer the near-wall eddies are of spanwise size $O(10^2)$ wall units
and grow linearly with wall distance, so that they shrink relative to
$\delta$ as $Re_\tau$ grows and a grid that resolves them becomes
prohibitive (see [wall-modelled LES](/methods/wall-modelled-les.md) and
[grid-point requirements](/results/les-grid-point-requirements.md)). The
review does not name the attached-eddy hypothesis.

## Attached and detached variables as a recovery diagnostic

Downstream of an oblique
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
at Mach 2.28, [Yu et al. (2023)](/sources/yu-2023.md) (§3, Fig. 6) use the
attached-eddy classification (Townsend 1976; Hwang 2015, as cited) to decide
which near-wall statistics measure recovery. Below $y^+\approx30$ the
wall-normal stress and the Reynolds shear stress in wall scaling collapse
on the reference-station profiles from $x^*=10$ ($x^*$ the distance from
impingement in reference thicknesses, page-local). They call these
"detached variables": the outer large-scale motions leave no strong
footprint on them near the wall because of the no-penetration condition.
The streamwise and spanwise stresses are "wall-attached variables". The
streamwise one collapses below $y^+\approx40$ but stays above the reference
value; the spanwise one keeps decreasing and has not converged by the last
station ($x^*=16.7$). The authors conjecture two competing effects: the
growing Reynolds number intensifies the wall-attached near-wall
fluctuations, while the decaying outer large-scale motions weaken their
footprints. They therefore judge near-wall recovery by the detached
variables. The spanwise spectra support the same split (§5.1, Fig. 12).
The mixing-layer-induced outer peak penetrates to the wall in the $u$ and
$w$ spectra (a "superposition effect", stronger and wider in scale for
$w$), but not in the $v$ spectrum, "the wall-normal velocity is not a
wall-attached variable".

## Inner–outer interaction in wall-modelled LES

[Maeyama & Kawai (2023)](/sources/maeyama-2023.md) (§6, App. C) find that
[wall-modelled LES](/methods/wall-modelled-les.md) of a Mach 2.28 boundary
layer at $Re_\tau$ up to about 14 000 does not reproduce the Reynolds-number
growth of the outer peak of the premultiplied spanwise spectrum of $u$ at
$y/\delta\approx0.15$, nor that of the log-region streamwise stress. A
spanwise cut-off at $\lambda_z/\delta=0.7$ places the deficit in the large
scales, which the grid nominally resolves (§6.2, Fig. 22). They
speculate (their word, "just speculation as of now") that the outer peak
grows through the inner–outer interaction with the inner peak, which the
modulation of the near-wall cycle by the outer motions raises with
Reynolds number (Hutchins & Marusic 2007; Mathis et al. 2009, as cited).
On this reading the outer peak cannot grow when the near-wall structures
are not resolved. They set this against the conclusion of Mizuno & Jiménez
(2013, as cited) that log-region structures do not depend on seeding from
the wall (§6.2). The paper does not name the attached-eddy hypothesis.

## Attached eddies as the argument for WMLES grid convergence

[Hu et al. (2024)](/sources/hu-2024.md) build a proposition on the
grid convergence of [wall-modelled LES](/methods/wall-modelled-les.md) on
the attached-eddy notion that eddy size scales with wall distance (§3,
Fig. 2). A wall-stress model takes LES data at the matching height
$h_{\mathrm{wm}}$ and returns the wall stress; once the attached eddies at
$y=h_{\mathrm{wm}}$ are resolved, the model input, and with it the wall
stress, stops changing with refinement, so convergence should start at a
grid spacing $\Delta_i=C_{\mathrm H}h_{\mathrm{wm},i}$ for matching height
$h_{\mathrm{wm},i}$, with a ratio $C_{\mathrm H}$ (page-local; the source's
$C$) that "could potentially be the same" for all matching heights. On a
channel at $Re_\tau=1000$, Spalart's boundary layer under a rotating
free stream and a channel with a sudden spanwise pressure gradient, the
mean wall stress, mean velocity and mean flow direction indeed collapse
better against $\Delta/h_{\mathrm{wm}}$ than against $\Delta/\delta$, with
onset near $\Delta/h_{\mathrm{wm}}\approx0.3$–$0.4$ (§6.1–6.2, Figs. 3–11).
The streamwise r.m.s. velocity does not: "the matching location has no
control over convergence of the Reynolds stress" (§6.2).

To explain the difference they decompose the premultiplied streamwise
spectrum of the channel after Hu, Yang & Zheng (2020, as they cite it) into
three eddy classes (§6.2, Eq. 13, Figs. 13–14): attached eddies occupy
$\alpha_{\mathrm A}y<\lambda_x<\beta_{\mathrm A}\delta$ for $y^+>100$, with
$\alpha_{\mathrm A}=5.7$, $\beta_{\mathrm A}=2$ (page-local names for the
source's $\alpha$, $\beta$; the source's third constant $\gamma=100$ is the
lower bound of $y^+$), small-scale eddies the region of shorter wavelengths,
and large-scale wall-detached eddies the third class; the energy of each
class is summed from the discrete spectrum (Parseval) over
$100\le y^+\le350$, where the mean log law also holds. Over cases with
$h_{\mathrm{wm}}=0.2\delta$ the attached-eddy energy is grid-converged while
the small-scale-eddy energy is not and grows with refinement. The authors
conclude that the small-scale eddies, which do not scale with wall
distance but contribute non-negligibly to the Reynolds stress, are why the
attached-eddy-based proposition holds for mean quantities and fails for
fluctuations. Assuming four cells per scale, they estimate from DNS spectra
that grid spacings of 80 to 30 viscous units capture 70 to 90% of the
small-scale-eddy energy, and take about 80%, $\Delta^+\approx50$ at
$Re_\tau=1000$, as the requirement for converging the streamwise normal
stress, a resolution at which WMLES "starts to approach WRLES" (§6.2, §7).

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

## Unsupervised structure identification

In passing, the review of artificial intelligence in turbulence research by
[Fang et al. (2026)](/sources/fang-2026.md) (§3.5) reports that latent
Dirichlet allocation clustering of $Q^-$ (ejection) events in channel
turbulence by Frihat et al. (as the review cites them) finds the scale of
the identified coherent structures to "increase linearly with the wall
distance", which the review calls "further confirming Townsend's
wall-attached vortex hypothesis". The review quotes the result without
numbers; the clustering study itself is not in the bundle.

## Qualifications

- Neither Cogo et al. (2022) nor Huang et al. (2022) test the hypothesis
  itself; both report DNS features they call consistent or inconsistent
  with it, at $Re_\tau$ up to about 2000
  (Cogo et al.) and 1200 (Huang et al.). Hu et al. (2024) use it as the
  premise of a grid-convergence proposition for WMLES, tested on LES at
  $Re_\tau\approx1000$, not as an object of test.
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
- [Devenport & Lowe (2022)](/sources/devenport-2022.md) — §2.2, Figs. 4–6 (predictions of the hypothesis, inactive motion, inner-peak growth, coherent-structure families); Marusic & Perry eddy types for APG history.
- [Yu et al. (2023)](/sources/yu-2023.md) — §3, Fig. 6 (attached and detached variables after a shock interaction); §5.1, Fig. 12 (superposition footprints in the $u$, $w$ spectra, none in $v$).
- [Maeyama & Kawai (2023)](/sources/maeyama-2023.md) — §6.1–6.2, Figs. 19–22; App. C (outer peak missed by WMLES; inner–outer interaction speculation; Mizuno & Jiménez 2013 as cited).
- [Hu et al. (2024)](/sources/hu-2024.md) — §3, Fig. 2 (matching-height proposition); §6.2, Eq. (13), Figs. 13–14 (attached, small-scale and detached eddy energies; $\Delta^+\approx50$ estimate); §7.
- [Fang et al. (2026)](/sources/fang-2026.md) — §3.5 (clustering result quoted from a cited study; passing mention).

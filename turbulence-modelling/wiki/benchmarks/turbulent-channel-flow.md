---
type: Benchmark
title: "Turbulent channel flow"
description: "Pressure-driven flow between two parallel walls, periodic in the wall-parallel directions, the canonical wall-bounded test: here a priori DNS data at Re_τ 395 to 2000, wall-modelled LES at Re_τ 1000 to 10¹⁰, hybrid RANS/LES at 5200 and 20,000, and compressible channels to bulk Mach 4."
status: established
aliases: [plane channel flow, channel flow, half-channel flow, compressible channel flow]
tags: [benchmark, wall-model, wmles, hybrid-rans-les, boundary-layer]
timestamp: 2026-10-25T13:30:00Z
---

# Turbulent channel flow

Plane channel flow is the flow between two parallel walls a distance $2\delta$
apart, driven by a mean pressure gradient (or an equivalent body force) and
periodic in the streamwise ($x$) and spanwise ($z$) directions; $y$ is
wall-normal. It is statistically stationary and homogeneous in $x$, $z$ and
time, so the mean velocity $\langle u\rangle(y)$ and the Reynolds stresses
$R_{ij}(y)$ converge from plane and time averages, and DNS exists up to high
friction Reynolds number $Re_\tau=u_\tau\delta/\nu_w$. The **half-channel**
variant simulates $0\le y\le\delta$ with a symmetry condition at $y=\delta$.
The compressible variant adds an energy source and isothermal walls, giving
wall heat flux. In this bundle the channel is the calibration and sanity
check for wall models, the first test of hybrid RANS/LES, and a source of
a priori data for subgrid and RANS closures.

## Configurations in the sources

| Source | Purpose | $Re_\tau$ | Domain ($x\times y\times z$) | Grid |
|---|---|---|---|---|
| [Flad & Gassner (2017)](/sources/flad-2017.md), §6.2, App. E | DG LES | 590 | $2\pi\times2\times\pi$ | $8^3$ elements, $N=7$; $\Delta x^+\approx58$, $\Delta z^+\approx29$, $\Delta y^+$ from 7 to 28 |
| [Agrawal et al. (2022)](/sources/agrawal-2022.md), §V, §VII.D | a priori SGS test; WMLES | 395, 2000 (a priori); 4200 (WMLES) | $2\pi\delta\times2\delta\times\pi\delta$ | $128\times40\times64$, uniform, $\Delta^+\approx200$ |
| [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), §IV.B, App. B | WMLES error calibration | 4200 | not printed | isotropic Voronoi, $\Delta/\delta=1/3$ to $1/160$ |
| [Fowler et al. (2022)](/sources/fowler-2022.md), §5 | WMLES of a new wall model | $10^3$ to $5\times10^5$ | $8\pi\times2\times3\pi$ (units $\delta$) | $128\times30\times48$; $\Delta x^+=\Delta z^+=196$, $\Delta y^+=67$ at $Re_\tau=1000$ |
| [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md), §II–III | half-channel WMLES of learned wall models | 180 to $10^{10}$ (eleven values) | $2\pi\delta\times\delta\times2\pi\delta$ | $24^3$, $32^3$, $48^3$, $72^3$ |
| [Haering et al. (2022)](/sources/haering-2022.md), §III B, §V A | a priori filtering; hybrid RANS/LES | 1000 (a priori); about 5200; 20,000 | $8\pi\delta\times2\delta\times3\pi\delta$ | $N_y=110$; $\Delta x^+$ from 701 to 1552 |
| [Griffin et al. (2023)](/sources/griffin-2023.md), §4 | compressible WMLES | 319 to 1842 | $\pi\delta\times2\delta\times(\pi\sqrt3/4)\delta$ | 12 points per half-height (9 to 48 in grid studies) |

Reference DNS named by the sources: Moser, Kim & Mansour at $Re_\tau=590$
(Flad & Gassner); Lozano-Durán & Jiménez at 2000 and 4200 (Agrawal et al.;
Lozano-Durán et al.); Lee & Moser at 1000 and 5200 (Haering et al.; Fowler
et al.; Vadrot et al.); the Johns Hopkins database at 1000 (Fowler et al.;
Vadrot et al.); Trettel & Larsson for the compressible channels (Griffin et
al.). The flow is driven at constant mass flow, constant centreline velocity
or constant pressure gradient, said per source.

## What the case tests

**Mean-velocity error of wall-modelled LES.** All the
[wall-modelled LES](/methods/wall-modelled-les.md) studies use the channel as
the case where the [law of the wall](/definitions/law-of-the-wall.md) holds
and any error is attributable to the LES or the wall model.
[Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), §IV.B, Fig. 7b,
calibrate the mean-velocity error of WMLES with the
[equilibrium wall model](/methods/equilibrium-wall-model.md) and dynamic
Smagorinsky at $Re_\tau=4200$ as $\varepsilon_u\approx0.08\,\Delta/\delta$,
with $\Delta$ the isotropic cell size of their Voronoi grids (linear convergence, the same trend for a staggered finite-difference
solver), and bound it by about 15%, the difference between DNS and an
inviscid solution. Their App. B, Figs. 23–24, documents non-monotonic
convergence for $\Delta/\delta\approx0.03$–$0.05$, which they relate to the
grid's ability to support near-wall streaks; they "still lack a satisfactory
explanation". [Agrawal et al. (2022)](/sources/agrawal-2022.md), §VII.D,
Figs. 8–10, match the wall model at the second off-wall point at
$Re_\tau=4200$ and find that their tensor-coefficient model reduces the error
of the apparent von Kármán constant against the DNS value $\kappa=0.38$ from
7% (dynamic Smagorinsky) to 5%, lowers near-wall intensities, and needs no
clipping where dynamic Smagorinsky does.
[Fowler et al. (2022)](/sources/fowler-2022.md), §5.1, find their
[LaRTE wall model](/methods/lagrangian-relaxation-towards-equilibrium-wall-model.md)
"nearly indistinguishable" from the equilibrium model in mean statistics
from $Re_\tau=10^3$ to $5\times10^5$ on one fixed grid, with a slight
log-layer undershoot at $10^3$; they attribute WMLES-to-DNS differences in
the near-wall stresses to grid and SGS model, because two wall models agree.
[Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) use eleven Reynolds
numbers to test whether [machine-learning wall models](/methods/machine-learning-wall-model.md)
extrapolate: one reproduces the mean at all $Re_\tau$, one fits a log law
with $\kappa=0.32$, and a reinforcement-learning model gives a
[log-layer mismatch](/definitions/log-layer-mismatch.md) of $+2.2$ to
$-3.2$ in wall units across the range (Table III). They advocate the
channel as a sanity check every learned closure should pass (§V).

**Grid convergence of the classical compressible wall model.**
[Griffin et al. (2023)](/sources/griffin-2023.md), §4, run nine compressible
channels at bulk Mach 0.7 to 4 and dimensionless wall heat flux $-B_q$ from
0.010 to 0.19 (Table 1) with 12 points per half-height and matching at
$0.3\delta$. Their [inverse-velocity-transformation wall model](/methods/inverse-velocity-transformation-wall-model.md)
keeps wall-stress and heat-flux errors small at all heat fluxes, while the
classical model's errors grow with $-B_q$. With fixed matching height and
9, 18, 36 points per half-height ($2.0\times10^4$ to $1.3\times10^6$ control
volumes against $6.4\times10^8$ for the DNS), the classical model's
log-intercept error persists under refinement (§4.1, Fig. 13). See
[compressible velocity transformations](/definitions/compressible-velocity-transformation.md).

**Hybrid RANS/LES and transition from RANS.**
[Haering et al. (2022)](/sources/haering-2022.md), §V A, run the
[active model split](/methods/active-model-split.md) method at
$Re_\tau\approx5200$ on four grids from $\Delta x^+\approx701$ to 1552
(84K to 408K times fewer cells than the DNS). The mean is nearly
grid-independent with no log-layer mismatch, and the resolved fraction
reaches $\beta\approx0.4$ at the centreline on the fine grid. Started from
RANS, the hybrid state develops in time with a transient overshoot that heals
by eight flow-throughs, and in space (a $16\pi$-long channel with a RANS
inlet) without overshoot but slowly. At $Re_\tau=20{,}000$ the mean
departs from the log law for $y^+=200$–$2000$, which the authors attribute
to the RANS base model.

**Element-based LES.** [Flad & Gassner (2017)](/sources/flad-2017.md),
§6.2, Fig. 11, compare split-form DG LES with the dynamic Smagorinsky model
against no-model, de-aliased DG at $Re_\tau=590$; the split-form LES gives
better Reynolds-stress profiles, and both are called "acceptable".

**A priori data for closures.** [Agrawal et al. (2022)](/sources/agrawal-2022.md),
§V, Figs. 1–2, filter channel DNS at $Re_\tau=395$ and 2000 (filter width
three grid spacings) and find higher stress-tensor correlations for their
tensor-coefficient model than for dynamic Smagorinsky, mostly near the wall,
and identical dissipation correlations. [Haering et al. (2022)](/sources/haering-2022.md),
§III B, Fig. 1, box-filter DNS at $Re_\tau=1000$ (excluding $y^+<300$) to
fit $\alpha=\beta^{1.7}$ between the modelled-energy fraction and the
computable unresolved fraction. [Fowler et al. (2022)](/sources/fowler-2022.md),
§2.3, Fig. 2, time-filter Johns Hopkins DNS at $Re_\tau=1000$ to show that
filtering at their relaxation time collapses near-wall profiles onto the law
of the wall.

**RANS calibration and identifiability.** As recalled by
[Duraisamy et al. (2019)](/sources/duraisamy-2019.md), §5.1, channel DNS
was the first data set used to assign Bayesian posterior distributions to
RANS model parameters (Oliver & Moser 2011; Cheung et al. 2011), and a
stochastic discrepancy model for the Reynolds stress was tested in channel
flow at several Reynolds numbers. [Duraisamy (2021)](/sources/duraisamy-2021.md),
§VII, Fig. 4, shows a channel case in which a model-consistent perturbation
of the anisotropy, inferred from mean-velocity data, reproduces the mean
velocity and shear stress but not the anisotropy (non-identifiability; no
Reynolds number given). See
[model-form uncertainty](/definitions/model-form-uncertainty.md) and
[field inversion and machine learning](/methods/field-inversion-machine-learning.md).

## Qualifications

- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) write $z$ for the
  wall-normal coordinate; the table above translates their half-channel to
  $y$ wall-normal.
- [Fowler et al. (2022)](/sources/fowler-2022.md) give the wall-model height
  as $h_{\mathrm{wm}}^+\approx34$ in the a priori test (§2.3) and
  $h_{\mathrm{wm}}^+=33$ for the $Re_\tau=1000$ LES (Table 1), with
  $h_{\mathrm{wm}}=\delta/30$ in both; at $Re_\tau=1000$ the value is
  $1000/30\approx33.3$ *(compiler check, not in the sources)*. Their own
  symbol for the wall-model height is $\Delta$.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) print the
  channel grids as $\Delta/\delta=1/3,1/5,1/10$ in §IV.C and as
  $1/3,1/6,1/10$ in the Fig. 8 caption.
- The sources differ on where the equilibrium wall model is matched: the
  second off-wall point on staggered grids
  ([Agrawal et al. (2022)](/sources/agrawal-2022.md)), the first off-wall
  cell centre without temporal filtering
  ([Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md)), half the
  first wall-normal cell ([Fowler et al. (2022)](/sources/fowler-2022.md))
  or $0.3\delta$ ([Griffin et al. (2023)](/sources/griffin-2023.md)); this is a
  difference of practice, discussed on [log-layer mismatch](/definitions/log-layer-mismatch.md).

# Citations

- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §V, Figs. 1–2; §VII.D, Figs. 7–10.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §IV.B–C, Figs. 7–8; App. B, Figs. 23–24.
- [Fowler et al. (2022)](/sources/fowler-2022.md) — §2.3, Fig. 2; §5.1, Table 1, Figs. 4–10.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §II–IV, Table III, Figs. 5–15, App. A–B.
- [Haering et al. (2022)](/sources/haering-2022.md) — §III B, Fig. 1; §V A, Table I, Figs. 2–8.
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §4, Table 1, Figs. 8–15.
- [Flad & Gassner (2017)](/sources/flad-2017.md) — §6.2, App. E, Fig. 11.
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §5.1 (recalled calibration studies).
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §VII, Fig. 4.

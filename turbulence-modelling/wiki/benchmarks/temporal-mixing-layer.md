---
type: Benchmark
title: "Temporally developing mixing layer"
description: "A periodic shear layer between two counter-flowing streams that transitions and then grows linearly in momentum thickness: the inhomogeneous a posteriori test of gradient-type and ensemble-Kalman-calibrated subgrid models and of neural-operator surrogates of LES, against filtered DNS on grids of 64×64×32 to 128×128×64."
status: established
aliases: [temporal mixing layer, temporally evolving mixing layer, TML, free-shear mixing layer, temporally evolving free-shear layer]
tags: [benchmark, les, sgs-model, data-driven, neural-network, dns, combustion]
timestamp: 2026-10-29T05:14:00Z
---

# Temporally developing mixing layer

Two streams of opposite velocity $\pm\Delta U/2$ (page-local: $\Delta U$
the velocity difference) meet in a periodic box. In the temporal version
the layer evolves in time rather than downstream: the box is periodic in
the streamwise ($x$) and spanwise ($z$) directions, and the cross-stream
direction $y$ is periodic too in the sources below, with numerical
diffusion (buffer) zones near its boundaries, which
[Wang et al. (2023c)](/sources/wang-2023-c.md) use to avoid a second
mixing layer. Seeded by small random perturbations of a tanh profile, the
layer transitions to turbulence and then grows, with the momentum
thickness
$$\theta=\int\Big[\tfrac14-\Big(\frac{\langle u\rangle}{\Delta U}\Big)^2\Big]dy$$
(registry $\theta$, applied to the shear layer; averages over $x$ and $z$)
growing linearly in time. Time is scaled by $\tau_\theta=\theta_0/\Delta U$
(page-local), $\theta_0$ the initial momentum thickness. The flow is
inhomogeneous in $y$ and unforced; the four LES sources of the next
section use it as their second a posteriori test after
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md),
and Wang et al. (2023c) attribute the gradient model's poorer spectrum
there to "the absence of control by the large-scale forcing" (§IV).
The quantities compared are $\theta(t)$, the resolved kinetic energy per
component, energy spectra at fixed times, PDFs of velocity increments, mean
velocity and Reynolds shear stress profiles, and $Q$-criterion iso-surfaces,
always against filtered DNS (fDNS).

## Configurations in the sources

The three incompressible sources use $\Delta U=2$ and $\theta_0=0.08$, so
$\tau_\theta=0.04$, and an initial streamwise velocity
$$u=\frac{\Delta U}{2}\Big[\tanh\frac{y}{2\theta_0}-\tanh\frac{y+L_y/2}{2\theta_0}-\tanh\frac{y-L_y/2}{2\theta_0}\Big]+\lambda_1$$
with Gaussian noise $\lambda_i\sim\mathcal N(0,0.01)$ (page-local, not the Taylor microscale) on each component
([Li et al. (2024)](/sources/li-2024.md), Eq. 33;
[Zhao et al. (2025)](/sources/zhao-2025.md), Eq. 23). Wang et al. (2023c)
place the layer at the centre of $0<y\le L_y$, scale the tanh width by a
constant chosen so that the initial momentum thickness is $\theta_0$, and
perturb with a digital filter
([Wang et al. (2023c)](/sources/wang-2023-c.md), §IV).

| Item | [Wang et al. (2023c)](/sources/wang-2023-c.md) | [Li et al. (2024)](/sources/li-2024.md) | [Zhao et al. (2025)](/sources/zhao-2025.md) |
|---|---|---|---|
| Domain ($x\times y\times z$) | $8\pi\times8\pi\times4\pi$ | $8\pi\times8\pi\times4\pi$ | $8\pi\times8\pi\times4\pi$ |
| DNS grid | $512\times512\times256$ | $256\times256\times128$ | $256\times256\times128$ |
| Viscosity | $\nu=0.0005$ | not printed | $\nu=0.008$, initial $Re_\theta=20$ |
| DNS time step | 0.002 | 0.002 | 0.001 |
| Filter | Gaussian, $\Delta=8h_{\mathrm{DNS}}$, filter-to-grid ratio 2 | Gaussian, $\Delta=4h_{\mathrm{DNS}}$, ratio 1 | sharp spectral, $\Delta=8h_{\mathrm{DNS}}$, ratio 2 |
| LES grid | $128\times128\times64$ | $64\times64\times32$ | $64\times64\times32$ |
| Models | gradient model plus Smagorinsky term with an ensemble-Kalman-calibrated coefficient (EnKF-MM); dynamic Smagorinsky; dynamic mixed; gradient model | transformer neural operator (TNO); Fourier neural operator (FNO); dynamic Smagorinsky (DSM); dynamic mixed (DMM) | LESnets (physics-informed FNO and implicit FNO trained on the Smagorinsky LES residual); data-driven FNO and IFNO; Smagorinsky ($C_s=\sqrt{0.001}$) |
| Time window | $t/\tau_\theta=50$ to 800 | to $t/\tau_\theta\approx650$ | 250 network steps, about $t/\tau_\theta=50$–250 |
| Data | — | 200 DNS runs × 90 snapshots every $10\tau_\theta$; 10 new runs for testing | 200 DNS runs (2000 training cases of 11 fields); 5 new runs for testing |

These three solve the incompressible equations pseudo-spectrally with
second-order Adams–Bashforth time stepping. The initial
$Re_\theta=\Delta U\theta_0/\nu$ of Wang et al. is 320 *(compiler check,
not in the sources)*.

A fourth source runs a **weakly compressible** variant from the same
group. [Wang et al. (2022)](/sources/wang-2022-j.md), §V, Table IV, solve
the Favre-filtered compressible equations at $M=0.2$, $Re=2000$, $Pr=0.7$,
$\gamma=1.4$ with eighth-order finite differences, the reference velocity
being $\Delta U/2$. The domain is $8\pi\times8\pi\times4\pi$ (streamwise,
cross-stream, spanwise), periodic with numerical-diffusion buffer zones near
the cross-stream boundaries; the initial tanh profile is that of Wang et
al. (2023c) with $\theta_0=0.08$ and width constant $C_\theta\approx1.05$
(page-local); the DNS grid is $512\times512\times256$ with $\Delta
t=0.0005$. The initial perturbations come from a digital filter
([inflow turbulence generation](/methods/inflow-turbulence-generation.md))
of width $\Delta_d$ (page-local) equal to 8, 16, 32 or $64h_{\mathrm{DNS}}$;
the linear-growth region of $\theta$ is "clearly longer and more concrete"
for $\Delta_d=8$ and $16h_{\mathrm{DNS}}$, which become the benchmarks
(Fig. 8). The LES uses a Gaussian filter of width $\Delta=8h_{\mathrm{DNS}}$,
a filter-to-grid ratio of 2 and $128\times128\times64$ points, and starts
from the filtered and coarse-grained DNS field. A second configuration
(App. B) is a cube of side 59, about four wavelengths of the most unstable
mode, seeded with digital-filter noise ($\Delta_d=16h_{\mathrm{DNS}}$)
plus two- and three-dimensional linear-stability modes of wavelengths
$L/4$, $L/2$ and $L$ ($L$ the box side, page-local), at a vorticity-thickness
Reynolds number of 50, DNS $256^3$ and LES $64^3$.

## What the case tests

**A posteriori calibration of a mixed model.**
[Wang et al. (2023c)](/sources/wang-2023-c.md) (read in arXiv v3), §IV,
calibrate the single coefficient $C_{\mathrm f}$ of their mixed model by an
[ensemble Kalman filter](/methods/ensemble-kalman-closure-calibration.md)
against fDNS spectra observed every $10\tau_\theta$ from $t/\tau_\theta=50$
to 800. Unlike in isotropic turbulence, a shifting step that moves every
member by the difference between the best member and the ensemble mean
"must be additionally incorporated" for convergence; 20 and 40 members
converge, 10 need an inflation factor of 1.5, and the result is
$C_{\mathrm f}\approx0.01$ (Fig. 11, Table IV). Against fDNS:

- the momentum thickness grows linearly in all models; the dynamic
  Smagorinsky model delays transition, the dynamic mixed model captures it
  better but drifts later, the gradient model over- then underpredicts,
  and EnKF-MM is best (Fig. 12);
- at $t/\tau_\theta=600$ and 800 the gradient model's spectrum is much
  worse than in isotropic turbulence, "presumably due to the absence of
  control by the large-scale forcing"; the dynamic models overestimate
  large-scale energy (Fig. 13);
- the dynamic models give much too much kinetic energy in the
  linear-growth region and the gradient model much too little; EnKF-MM
  captures the reduced growth rate (Fig. 14).

See [gradient model](/methods/gradient-model.md) and
[scale-similarity and mixed models](/methods/scale-similarity-model.md).

**A constant-coefficient spatial gradient model.**
[Wang et al. (2022)](/sources/wang-2022-j.md), §V, Figs. 9–16, run their
SGM-7-19, a structural model built from products of first-order filtered
velocity gradients on a seven-point stencil with Taylor-derived constant
coefficients (recorded on the [gradient model](/methods/gradient-model.md)
page), against the dynamic Smagorinsky (DSM) and dynamic mixed (DMM)
models and [implicit LES](/definitions/implicit-les.md), with filtered DNS
as reference:

- *Momentum thickness.* DSM captures the transitional region but deviates
  in the linear-growth region, DMM is worse than DSM, SGM-7-19 is best,
  and ILES also follows the filtered DNS (Fig. 9).
- *Initial perturbation scale.* All LES agree better with filtered DNS
  when $\Delta_d=16h_{\mathrm{DNS}}$ than when $\Delta_d=8h_{\mathrm{DNS}}$,
  i.e. when the initial perturbation scale exceeds the LES filter width,
  so that filtering the initial field does not remove the perturbations
  (Figs. 9–13, Conclusions).
- *Spectra and energy.* ILES does not recover the filtered spectrum (the
  two-dimensional mid-plane spectrum and the streamwise spectrum at
  $t=30$) despite its good $\theta$ and over-predicts the mid-plane
  kinetic energy; the explicit models do better on the spectrum, SGM-7-19
  closest; SGM-7-19 and DMM predict the mid-plane kinetic energy best and
  SGM-7-19 the streamwise kinetic energy of the whole domain (Figs.
  10–13).
- *Increments, stress and structures.* SGM-7-19 matches the PDFs of
  spanwise velocity increments at $r/\Delta=1$ to 8, including the large
  separations, where in forced isotropic turbulence all models coincide;
  DSM and DMM over-predict the Reynolds shear stress $\langle u'v'\rangle$
  across the layer and give larger vortex structures at $Q=0.6$ (Figs.
  14–16).
- *Linear-stability seeding (App. B).* SGM-7-19 again gives the best
  $\theta$, DSM under-predicts and DMM over-predicts the growth; DSM
  over-dissipates the vorticity rollers and DMM produces strip-shaped
  noise (Figs. 17–20).
- *Cost.* The SGS modelling time per step on 32 cores is 0.245 s (DSM),
  0.575 s (DMM) and 0.425 s (SGM-7-19), printed as 1, 2.3 and 1.7 relative
  to DSM (Table V).

Across the two gradient-type studies on this case, the plain
[gradient model](/methods/gradient-model.md) of Wang et al. (2023c)
over- then under-predicts $\theta$, while the higher-order spatial
gradient model of Wang et al. (2022) gives the best $\theta$ of its
comparison; the two use different grids, filters and models, so the
results are side by side, not a ranking. In both studies the dynamic
Smagorinsky model departs from the filtered DNS in $\theta$: it delays the
transition in Wang et al. (2023c) and deviates in the linear-growth region
in Wang et al. (2022).

**Neural-operator surrogates of LES.** Two sources replace the LES solver
by an autoregressive [neural operator](/methods/neural-operator-les-surrogate.md)
that advances the filtered velocity on the LES grid.

- [Li et al. (2024)](/sources/li-2024.md) (read in arXiv v2), §V B, train
  a transformer neural operator (linear attention, rotary position
  embedding, Fourier regressor) on five past fields. It agrees with fDNS in
  momentum thickness through transition and stays "relatively stable" in
  linear growth, while DMM overestimates $\theta$ and DSM underestimates it
  early and overestimates it later (Fig. 16). DSM and DMM underestimate the
  three kinetic-energy components early and overestimate them later; the
  TNO "closely matches the fDNS data … throughout the entire development"
  (Fig. 17). The FNO's $\theta$ "becomes unreliable" beyond
  $t/\tau_\theta\approx400$ and its kinetic energies diverge after 200; at
  $t/\tau_\theta\approx650$ all models deviate in the spectrum, the TNO
  least (Fig. 18). DSM and DMM give larger vortex structures than fDNS in
  $Q=0.2$ iso-surfaces (Fig. 20). Cost per time node: DSM 83.55 and DMM
  97.86 CPU·s against 1.691 GPU·s (20.18 CPU·s) for the TNO and 0.426
  GPU·s for the FNO (Table II).
- [Zhao et al. (2025)](/sources/zhao-2025.md) (read in arXiv v3), §3.2,
  train LESnets with the residual of the Smagorinsky-closed LES equations
  as the only loss, no labelled data. In the mixing layer the data-driven
  FNO does not diverge (unlike in decaying isotropic turbulence), the
  data-driven models predict $\theta$ better than the Smagorinsky LES, and
  LESnets, whose only loss is the residual of that LES, are comparable to
  it (Figs. 13–14). Inference for 250 steps takes 3.18 s for LESnets against
  126.79 s for the Smagorinsky LES on CPUs, about a 40-fold speed-up
  excluding training (Table 6).

The two surrogate studies agree that the reference LES with dynamic or
constant-coefficient Smagorinsky misses $\theta$. They differ on the
data-driven FNO trained on fDNS: in Li et al. its $\theta$ becomes
unreliable beyond $t/\tau_\theta\approx400$ and its kinetic energies
diverge after 200, while in Zhao et al. it does not diverge over the 250
network steps tested. The set-ups differ (Gaussian filter at ratio 1
against sharp spectral at ratio 2, different networks, data and
viscosity), so the difference is recorded as one of set-up, and their LES
errors are not comparable.

**Why the temporal version.** [Kim & Leonard (2024)](/sources/kim-2024-b.md),
§4.2, give the historical reason: a spatially growing free shear layer
needs inflow and outflow conditions and a long domain, so most early
simulations computed temporally growing layers, "an approximation to a
spatially growing free-shear flow in an advected frame of reference". The
price they list is that the spatial growth, and with it the asymmetric
entrainment, is absent, and that the statistics must be made insensitive
to the initial mean and disturbances, usually by waiting for a
self-similar state. Mansour et al. (1978) and Riley & Metcalfe (1980) were
"among the first" to simulate turbulent mixing layers; roll-up and
pairing agreed with experiments once the temporal–spatial relation was
accounted for, and Riley & Metcalfe showed how suppressing subharmonic
modes suppresses pairing in a forced layer. Metcalfe et al. (1987), Moser
& Rogers (1991, 1993) and Rogers & Moser (1992) followed on secondary
instability, mixing transition and three-dimensional evolution, Moser &
Rogers (1994) on the temporal wake; Lowery & Reynolds (1986) made the
first DNS of a spatially growing mixing layer, with an advective outflow
condition and inlet forcing by inviscid eigenfunctions or random
perturbations. The authors attribute the success of the Mansour et al.
mixing-layer LES "in large part" to energy-conserving numerics (§3.1; see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).

**Mixing layers in one-dimensional turbulence.** The review of
[Chen et al. (2024b)](/sources/chen-2024-c.md) records the mixing layer as
a calibration flow of the stochastic
[one-dimensional turbulence](/methods/one-dimensional-turbulence.md) model:
the vector formulation of Kerstein et al. (2001) is printed for "mixing
layer and wake" and its eddy locations are compared with DNS of
time-developing free shear flows (Table 1, Eq. 6, Fig. 8); the
variable-density formulation of Ashurst & Kerstein (2005) was run at
density ratios 1, 2, 4 and 8 and convective Mach numbers 0.3, 0.7 and 1.1,
with growth rates that agree with DNS at 0.3 and 0.7 and "a large
discrepancy between ODT and DNS growth rates" at 1.1, which the review
attributes to the incompressible solver and a simple kinematic model
(§2.3.4, §3.1). The authors' own conservative compressible ODT reuses the
Ashurst–Kerstein eddy energy and is reported on a compressible planar and
a supersonic scalar mixing layer (Table 2, Eq. 16; §2.3).

**Reacting mixing layers as a priori databases.** The review of
[conditional source-term estimation](/methods/conditional-source-term-estimation.md)
by [Salehi et al. (2024)](/sources/salehi-2024.md), §3.1.1, Fig. 21,
cites DNS of temporal mixing layers of heptane at 60 and 80 atm (Bellan
and coworkers; turbulent Reynolds numbers 1000 and 2000, grids from
$480\times530\times288$ to $768\times804\times460$, one-step chemistry, a
Peng–Robinson equation of state) on which the closure was tested a priori
with 1, 8 and 22 ensembles: with the DNS probability density the
estimation performs very well, with a presumed β-PDF it errs
significantly, and in the doubly conditional variant the joint-PDF model
is by far the largest error source. The same review describes the first a
priori test of the method, on a DNS of Vervisch ($128\times64\times64$,
one-step chemistry, top-hat filter $16\times8\times8$, four ensembles),
as a shear-free temporal mixing layer (Figs. 19–20); the mixing layers
of this page are sheared; see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).

**Two-dimensional double-vortex pairing for shock-capturing schemes.**
[Kokkinakis & Drikakis (2025)](/sources/kokkinakis-2025.md), §III E, use a
two-dimensional relative of the configuration, the double-vortex
pairing of Winant & Browand, to measure the numerical dissipation of WENO
reconstructions (see [WENO schemes](/methods/weno-scheme.md) and
[numerical dissipation](/properties/numerical-dissipation.md)). Two streams
of 4.06 and 1.44 cm/s ($\Delta U=2.62$ cm/s) are computed in the frame of
their mean, so that they move at $\pm\Delta U/2=\pm1.31$ cm/s, with the
profile $u=-\tfrac{\Delta U}{2}\tanh\big(y/(2\theta_0)\big)$,
$\theta_0=0.03$ cm, $\nu=0.01$ cm²/s, $\gamma=5/3$, a Mach number of 0.2 on
$\Delta U$, and $Re\simeq1600$ on $\Delta U$, the streamwise period and
$\nu$. The perturbation is the sum of two Kelvin–Helmholtz eigenmodes, the
second of twice the wavenumber, with amplitudes $0.025\Delta U$ and
$0.05\Delta U$; the box is periodic in $x$ and reflective in $y$, the
initial pressure solves a Poisson equation, and a passive scalar marks the
streams. On $64^2$ cells against a $256^2$ reference, run to $t=6$ s, every
enhanced WENO5 sharpens the scalar field relative to WENO5-JS and the
authors' hybrid WENO5-H++ agrees best with the reference (Fig. 5). Their
Tables II–III, normalized by the downsampled reference lengths (inner 2.90
cm, outer 3.15 cm) and by the accumulated numerical dissipation of
WENO5-JS:

| Scheme | inner vortex length | outer vortex length | accumulated numerical dissipation |
|---|---|---|---|
| WENO5-JS | 0.373 | 0.496 | 1 |
| WENO5-Z+ | 0.534 | 0.586 | 0.942 |
| WENO5-ZM | 0.609 | 0.674 | 0.888 |
| WENO5-MD | 0.679 | 0.895 | 0.829 |
| WENO5-H++ | 0.745 | 0.868 | 0.822 |

The rotation angle of the merged vortex is the same for all schemes, and
the authors name the initial velocity jump between the streams "the
leading contributing factor" of the accumulated dissipation (§III E 3). At
finer grids the differences between the WENO5 variants shrink (stated,
not shown). The runs use no subgrid model.

**Mixing-layer statistics as a reference elsewhere.** Statistics of free
shear layers also serve as a reference outside this configuration.
[Yu et al. (2023)](/sources/yu-2023.md) identify a mixing layer embedded
in the boundary layer recovering behind an impinging shock (see
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md))
and compare its stress ratios $\langle v'v'\rangle/\langle u'u'\rangle$ and
$-\langle u'v'\rangle/\langle u'u'\rangle$ (Favre-weighted in the source)
with measurements and simulations of free compressible mixing layers
against the convective Mach number, adapted as the maximum velocity
defect over the sum of the sound speeds at the wall and at the layer edge
(§5.1, Eq. 5.1, Fig. 14). Over their range, 0.32 down to 0, the ratios
match the free-layer data and they see no compressibility effect; the
anisotropy of the embedded layer (0.49, 0.23, 0.28, 0.15 for the $uu$,
$vv$, $ww$, $-uv$ stresses over $2k$) lies on the axisymmetric-expansion
line of the Lumley triangle, which they call the typical mixing-layer state
(App. A, Fig. 19); [Helm & Martín (2022)](/sources/helm-2022.md) give
another side of the triangle as typical of mixing layers (an open
contradiction on the
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
page). None of the incompressible LES configurations above
enters their comparison.

## Qualifications

- The dynamic models of [Li et al. (2024)](/sources/li-2024.md) average
  the Germano coefficients over the whole domain (their Eqs. 8, 10–11), a
  global average in a flow inhomogeneous in $y$; the paper does not discuss
  it. Their Eq. 9 prints the Smagorinsky part of the mixed model with
  coefficient $C_1\Delta^2|\bar S|\bar S_{ij}$ while the Germano tensors
  use $-2\Delta^2|\bar S|\bar S_{ij}$, a factor $-2$ apart *(compiler
  check, not in the sources)*. Their Fig. 18 caption labels the third panel
  "(b)".
- [Zhao et al. (2025)](/sources/zhao-2025.md) cite "Eq. (19)" for the
  $Q$-criterion, which is their Eq. (18).
- [Wang et al. (2023c)](/sources/wang-2023-c.md) integrate the momentum
  thickness over $-L_y/4$ to $L_y/4$ while defining the profile on
  $0<y\le L_y$, implicitly shifting the origin to the layer centre, and
  print a prefactor $\tfrac14$ before the integral that Li et al. (Eq. 34)
  and Zhao et al. (Eq. 24) do not have (Wang et al., Eq. 24); the
  Reynolds number of their mixing layer is not printed.
- The three configurations share $\Delta U$, $\theta_0$ and the domain
  size but differ in viscosity, DNS resolution, filter and LES grid, and
  each compares its own models only.
- [Wang et al. (2022)](/sources/wang-2022-j.md) define the momentum
  thickness in Favre form with the same prefactor $\tfrac14$ (Eq. 29),
  with velocities normalized by $\Delta U/2$; at constant density and with
  $U=\langle u\rangle/(\Delta U/2)$ the integrand $\tfrac14(1-U)(1+U)$
  equals $\tfrac14-(\langle u\rangle/\Delta U)^2$, the form defined above,
  so the prefactor belongs to that normalization *(compiler check, not in
  the sources)*. The paper does not state the
  reference length of $Re=2000$, and states the backscatter clipping of
  SGM-7-19 for the isotropic-turbulence runs only. Their ILES of the
  mixing layer runs on the eighth-order central scheme, and its
  dissipation mechanism is not described.
- [Kokkinakis & Drikakis (2025)](/sources/kokkinakis-2025.md) state in
  the abstract that WENO5-H++ "reduces numerical dissipation by nearly
  20%", and in the conclusions "nearly 20%" and "~18%", while their Table
  III gives 0.822 of WENO5-JS, a reduction of 17.8% *(compiler check, not
  in the sources)*; they call the WENO5-H++ inner vortex length "more than
  twice" that of WENO5-JS, while Table II gives $0.745/0.373=1.997$
  *(compiler check, not in the sources)*. Their double-vortex pairing is
  two-dimensional, unlike the three-dimensional layers above.

# Citations

- [Wang et al. (2023c)](/sources/wang-2023-c.md) — arXiv v3: §IV, Eqs. 23–27, Tables III–IV, Figs. 11–17.
- [Li et al. (2024)](/sources/li-2024.md) — arXiv v2: §II, Eqs. 7–11; §V B, Eqs. 33–35, Table II, Figs. 14–21.
- [Zhao et al. (2025)](/sources/zhao-2025.md) — arXiv v3: §3.2, Table 3, Eqs. 18, 23, Figs. 11–14; §5.1, Table 6.
- [Wang et al. (2022)](/sources/wang-2022-j.md) — §V, Eqs. 28–33, Table IV, Figs. 8–16; §VI, Table V; App. B, Figs. 17–20.
- [Yu et al. (2023)](/sources/yu-2023.md) — §5.1, Eq. 5.1, Fig. 14; App. A, Fig. 19 (free-mixing-layer data as reference for a mixing layer embedded in a boundary layer).
- [Kim & Leonard (2024)](/sources/kim-2024-b.md) — §3.1; §4.2 (historical).
- [Chen et al. (2024b)](/sources/chen-2024-c.md) — Table 1, Eq. 6, Fig. 8; §2.3, Table 2, Eq. 16; §2.3.4, §3.1.
- [Salehi et al. (2024)](/sources/salehi-2024.md) — §3.1.1, Figs. 19–21 (cited reacting DNS, review).
- [Kokkinakis & Drikakis (2025)](/sources/kokkinakis-2025.md) — §III E, Eqs. 18–21, Tables II–III, Figs. 5–6 (two-dimensional double-vortex pairing).

---
type: Benchmark
title: "Temporally developing mixing layer"
description: "A periodic shear layer between two counter-flowing streams that transitions and then grows linearly in momentum thickness: the inhomogeneous a posteriori test of subgrid models calibrated by ensemble Kalman filtering and of neural-operator surrogates of LES, against filtered DNS on grids of 64×64×32 to 64×128×128."
status: established
aliases: [temporal mixing layer, temporally evolving mixing layer, TML, free-shear mixing layer, temporally evolving free-shear layer]
tags: [benchmark, les, sgs-model, data-driven, neural-network, dns]
timestamp: 2026-10-26T15:57:00Z
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
inhomogeneous in $y$ and unforced; all three sources use it as their
second a posteriori test after
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md),
and Wang et al. (2023c) attribute the gradient model's poorer spectrum
there to "the absence of control by the large-scale forcing" (§IV).
The quantities compared are $\theta(t)$, the resolved kinetic energy per
component, energy spectra at fixed times, PDFs of velocity increments, mean
velocity and Reynolds shear stress profiles, and $Q$-criterion iso-surfaces,
always against filtered DNS (fDNS).

## Configurations in the sources

All three sources use $\Delta U=2$ and $\theta_0=0.08$, so
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

All three solve the incompressible equations pseudo-spectrally with
second-order Adams–Bashforth time stepping. The initial
$Re_\theta=\Delta U\theta_0/\nu$ of Wang et al. is 320 *(compiler check,
not in the sources)*.

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

# Citations

- [Wang et al. (2023c)](/sources/wang-2023-c.md) — arXiv v3: §IV, Eqs. 23–27, Tables III–IV, Figs. 11–17.
- [Li et al. (2024)](/sources/li-2024.md) — arXiv v2: §II, Eqs. 7–11; §V B, Eqs. 33–35, Table II, Figs. 14–21.
- [Zhao et al. (2025)](/sources/zhao-2025.md) — arXiv v3: §3.2, Table 3, Eqs. 18, 23, Figs. 11–14; §5.1, Table 6.

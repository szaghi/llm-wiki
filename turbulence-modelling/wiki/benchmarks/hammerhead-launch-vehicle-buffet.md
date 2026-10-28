---
type: Benchmark
title: "Hammerhead launch-vehicle buffet"
description: "Transonic buffet behind the payload fairing of the NASA Model 11 hammerhead launch vehicle at Mach 0.81 and zero incidence, a massively separated axisymmetric shear-layer flow on which Reynolds-stress-based IDDES variants are compared with SST-IDDES through the pressure-fluctuation peak, shear-layer breakdown and resolved spectra."
status: established
aliases: [hammerhead launch vehicle, NASA Model 11, Model 11 hammerhead, hammerhead buffet, Coe and Nute Model 11]
tags: [benchmark, des, hybrid-rans-les, reynolds-stress-model, separated-flow, compressible]
timestamp: 2026-10-27T21:09:00Z
---

# Hammerhead launch-vehicle buffet

A launch vehicle is called *hammerhead* when its payload fairing is wider
than the stage below it. At transonic speed the boundary layer of the
fairing separates at the boat tail, the free shear layer extends, breaks up
through the Kelvin–Helmholtz instability and impinges on the second-stage
booster, and a shock oscillates at the junction between the adapter and the
first-stage booster; the impingement and the shock motion drive the
buffeting loads. The test case is Model 11 of the NASA Ames wind-tunnel
programme of Coe & Nute (1962, NASA TM X-778), whose fairing-to-second-stage
diameter ratio, 1.6, is the largest of the configurations of that report.
[Wang et al. (2021)](/sources/wang-2021-l.md), §3.3, describe the flow
behind the boat tail as one that "can be regarded as an axisymmetric
back-step flow" (see [backward-facing step](/benchmarks/backward-facing-step.md)).
In this bundle the case tests the LES branch of
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) in a free shear layer
that leaves an attached, RANS-treated boundary layer: how fast the
resolved instability develops, and how large the modelled stress is
while it does.

## Configuration

Both sources come from one group and one solver (the unstructured
cell-centred finite-volume code HUNS3D, second-order Roe flux, dual time
stepping); [Li et al. (2022)](/sources/li-2022-k.md) reuse the RSM-IDDES
results of [Wang et al. (2021)](/sources/wang-2021-l.md) and its grid.

| Item | [Wang et al. (2021)](/sources/wang-2021-l.md), §3.3 | [Li et al. (2022)](/sources/li-2022-k.md), §III C |
|---|---|---|
| Flow conditions | $M=0.81$, $Re=4.2\times10^6$ on the first-stage diameter $D_{\mathrm{ref}}=12$ in, angle of attack $0^\circ$ | $M=0.81$, $Re=4.0\times10^6$ on the same diameter, angle of attack $0^\circ$ (see Contradictions) |
| Domain | half model with a symmetry plane | half body with a symmetry plane (Fig. 14) |
| Grid | O–H topology, average first-cell $y^+<0.5$, growth 1.21, refined zone of 140 azimuthal × 470 streamwise points downstream of the fairing, about 18.5 million cells | O–H topology refined downstream of the fairing; parameters and grid sensitivity referred to Wang et al. (2021) and an earlier study |
| Time step | $\Delta t=0.01$, made dimensionless with the free-stream sound speed and 1 m | not stated |
| Data processing | experimental and computed signals band-pass filtered between 10 and 800 Hz | not stated |
| Models compared | SST-IDDES, RSM-IDDES | SST-IDDES, RSM-IDDES (results of Wang et al.), RSM-DynIDDES |
| Reference | Coe & Nute experiment: mean and rms pressure coefficient | the same |

RSM-IDDES is the IDDES of Shur et al. built on the SSG/LRR-$\omega$
[differential Reynolds-stress model](/methods/reynolds-stress-model.md), in
which the dissipation of the turbulent kinetic energy carries the hybrid
length scale and the modelled Reynolds stress acts as the subgrid stress in
the LES region; its DES constants, calibrated on decaying
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md) with
the scheme used here, are 0.3 (SSG branch) and 0.5 (LRR branch).
RSM-DynIDDES replaces the constant by $C_{\mathrm{DES}}=C_kC_s$ with $C_s$
from the compressible [dynamic procedure](/methods/dynamic-procedure.md)
and $C_k$ fixed (1.67 SSG, 2.78 LRR). The construction is recorded on
[detached-eddy simulation](/methods/detached-eddy-simulation.md); SST-IDDES
is the same IDDES on the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md).

## Results

**Shear-layer breakdown.** RSM-IDDES starts the shear-layer instability
earlier than SST-IDDES and produces smaller vortices after breakdown
([Wang et al. (2021)](/sources/wang-2021-l.md), Fig. 9a); its mean shear
layer is shorter, reaches the wall earlier and forms a smaller separation
bubble (Figs. 12–13). RSM-DynIDDES places the break point where RSM-IDDES
does, upstream of SST-IDDES, and resolves more small-scale structures
([Li et al. (2022)](/sources/li-2022-k.md), Fig. 15); the attachment line
($C_f=0$) and the recirculation region on the second-stage booster of the
two RSM variants coincide and lie upstream of those of SST-IDDES (Fig. 17).

**Modelled stress as the mechanism.** Both sources attribute the delay of
SST-IDDES to its larger modelled subgrid stress in the extension region of
the free shear layer, following the view of Spalart that a large modelled
stress delays the Kelvin–Helmholtz instability: all subgrid-stress
components of RSM-IDDES are smaller there and in the breakdown region
([Wang et al. (2021)](/sources/wang-2021-l.md), Figs. 10, 13), and the
dynamic coefficient lowers the modelled stress further in the vortex
development region ([Li et al. (2022)](/sources/li-2022-k.md), Fig. 16,
"Region B").

**Pressure coefficients.** All models reproduce the mean $C_p$; the RSM
variants are closer to the experiment in the recirculation region
$0.35<x<0.65$ behind the boat tail ([Wang et al. (2021)](/sources/wang-2021-l.md),
Fig. 11a), and RSM-DynIDDES gives nearly the same mean $C_p$ as RSM-IDDES
([Li et al. (2022)](/sources/li-2022-k.md), Fig. 18a). Wang et al. estimate
the experimental peak of the rms pressure coefficient at $x=0.58$, matched
in position by RSM-IDDES, while SST-IDDES places it near $x=0.62$; both
over-predict its magnitude, RSM-IDDES less (Figs. 11b, 12b). At the
location of the experimental maximum, Li et al. print
(§III C, Fig. 18b):

| Method | rms of $C_p$ |
|---|---|
| SST-IDDES | 0.0897 |
| RSM-IDDES | 0.0719 |
| RSM-DynIDDES | 0.0554 |
| experiment | 0.0454 |

In the shock-oscillation region at the adapter–first-stage junction the
three methods nearly agree (Fig. 18b). Li et al. conclude that the dynamic
coefficient "only improves the prediction of the high-frequency part".

**Resolution and spectra.** Wang et al. find that both models resolve more
than 80% of the turbulent kinetic energy along their extraction line,
which they take as meeting the DES resolution requirement (Fig. 14b); Li
et al. rely on that check for the same grid. The velocity-fluctuation
spectra are broadband: RSM-IDDES has more amplitude at middle and high
frequency inside the separation bubble, and more energy at medium and high
wavenumbers with a wider $k^{-5/3}$ range at nearly identical low-wavenumber
content (Wang et al., Figs. 15–16). RSM-DynIDDES has the largest
high-frequency power spectral density along the shear layer upstream of
$x\approx0.65$, the three methods agreeing beyond it, and the largest
fraction of the turbulent kinetic energy at high wavenumbers, followed by
RSM-IDDES and SST-IDDES (Li et al., Figs. 20–22).

## Qualifications

- The improvement of RSM-DynIDDES rests on the rms pressure coefficient at
  one location and on figure-level comparisons of spectra and fields; no
  integrated buffet load or frequency is printed for this case by either
  source.
- The DES constants of the RSM variants are calibrated with the
  second-order Roe flux used here, and Wang et al. attribute the gap
  between these constants and their theoretical values to the scheme's
  [numerical dissipation](/properties/numerical-dissipation.md) (§2.3,
  §3.1); the modelled and numerical dissipation in the shear layer are
  not separated in either source.

## Contradictions

**Reynolds number of the Model 11 buffet case.** *Open.*
[Wang et al. (2021)](/sources/wang-2021-l.md), §3.3, print
$Re=4.2\times10^6$ on the 12-in first-stage diameter;
[Li et al. (2022)](/sources/li-2022-k.md), §III C, print
$Re=4.0\times10^6$ on the same diameter and Mach number, and state that
the computational conditions correspond to the wind-tunnel test while
reusing the RSM-IDDES results of Wang et al. Li et al. do not comment on
the difference.

# Citations

- [Wang et al. (2021)](/sources/wang-2021-l.md) — §3.3, Figs. 9–16 (configuration, grid, SST-IDDES against RSM-IDDES).
- [Li et al. (2022)](/sources/li-2022-k.md) — §III C, Figs. 13–22 (configuration; RSM-DynIDDES against RSM-IDDES and SST-IDDES).

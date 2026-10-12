---
type: Benchmark
title: "Radiation shadow test"
description: "Radiation entering a 1.0 × 0.12 cm box from one side meets a dense, opaque ellipsoidal cloud and must cast a sharp shadow behind it (Hayes & Norman 2003); it separates moment closures that keep beams (M1, local Eddington tensors) from flux-limited diffusion, and exposes the artefacts of local closures."
status: established
aliases: [shadow test, Hayes–Norman shadow, shadow behind a dense cloud, opaque cloud shadow]
tags: [benchmark, radiation, verification, amr]
timestamp: 2026-10-12T00:00:00Z
---

# Radiation shadow test

**Set-up** (Hayes & Norman 2003). Both sources use a 2D Cartesian box
$1.0\times0.12$ cm of $280\times80$ cells (Quokka's base grid), gas at
$T = 290$ K with ambient density $10^{-3}$ g cm⁻³, a dense cloud of
density 1 g cm⁻³, and radiation at $1740$ K ($6\times290$ K) entering
from the left boundary. In
[Skinner & Ostriker (2013)](/sources/skinner-2013.md) (§4.1.1, eqs. 54–55)
the cloud is an ellipsoid with a smooth ("fuzzy") edge, centred at
$(0.5, 0)$ cm on the reflecting lower boundary, with semi-axes 0.10 and
0.06 cm; the Quokka paper does not print the cloud geometry. In both, the
absorption coefficient grows as the square of the density, so the cloud is
optically thick while the ambient gas is nearly transparent, and a correct
method keeps a sharp shadow behind it. The test probes whether radiation
can stream in a fixed direction ($f_{\mathrm r}\to1$), which a local
[M1 closure](/methods/m1-radiation-transport.md) allows and flux-limited
diffusion does not.

**Runs.**

* [Skinner & Ostriker (2013)](/sources/skinner-2013.md), §4.1.1,
  eqs. 54–56, Figs. 2–3. [Athena](/software/athena.md)'s Hyperion module
  (unsplit VL, HLL with closed-form M1 eigenvalues), uniform grid,
  $\hat c = c$. Opacity
  $\kappa = 100\,(T/290\,\mathrm K)^{-3.5}\,(\rho/10^{-3}\,\mathrm{g\,cm^{-3}})$
  cm² g⁻¹ (eq. 56). Dirichlet left, outflow
  right and top, reflecting bottom; run for 10 light-crossing times.
  With thermal emission neglected the shadow is sharp (Fig. 2); with
  emission it is less sharp, from the numerical diffusion of the
  operator-split implicit exchange, but still preserved (Fig. 3).
  Comparable to González et al. (2007). Flux-limited diffusion "fails
  immediately".
* [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3.2.4,
  Fig. 12. [Quokka](/software/quokka.md) (HLL with frozen Eddington
  factors, default Levermore closure), $280\times80$ base grid with 2 AMR levels,
  refined where the relative gradient of $E_{\mathrm r}$ exceeds 0.1; no
  reduced speed of light; CFL 0.4; run to $t = 5\times10^{-11}$ s. Absorption coefficient
  $\rho\kappa = 0.1\,(\rho/10^{-3}\,\mathrm{g\,cm^{-3}})^2$ cm⁻¹,
  $\mu = 10$,
  $\gamma = 5/3$. The Newton tolerance of the matter–radiation exchange
  is lowered to $10^{-15}$; with the default, unphysical radiation shocks
  reflect off the cloud. The shadow is sharp, with residual shock-like
  artefacts inside it from a transient beam that curves around the cloud,
  "an unavoidable artefact of using a local VET closure". Qualitative only.

**Variants.** The two opacity laws differ: Skinner & Ostriker keep a
temperature dependence ($\propto T^{-3.5}$); Quokka's law has none. At
$T = 290$ K the printed laws coincide, with $\rho\kappa = 0.1$ cm⁻¹ in the
ambient gas and $10^5$ cm⁻¹ at cloud density (derived from the printed
values). Skinner &
Ostriker run 10 light-crossing times of the box; Quokka's end time is
about 1.5 crossing times of the 1 cm length (derived, with
$c\approx3\times10^{10}$ cm s⁻¹). Neither run reports an error norm.

**Related test, not this one.** [Rosdahl et al. (2013)](/sources/rosdahl-2013.md),
§6.4, run the ionizing-photon shadow of a dense clump from the Iliev et
al. (2006) comparison (test 3), where the shadow survives with HLL fluxes
and erodes with global Lax–Friedrichs fluxes; that is a different set-up.

# Citations

1. [Skinner & Ostriker (2013)](/sources/skinner-2013.md), §4.1.1 (arXiv v1).
2. [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3.2.4 (arXiv v2).
3. [Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §6.4 (arXiv v2), related test only.
